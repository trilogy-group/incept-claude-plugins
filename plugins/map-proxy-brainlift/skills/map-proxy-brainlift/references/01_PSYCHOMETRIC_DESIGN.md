# Psychometric Design — MAP Proxy Adaptive Assessment
**Version:** 2.0 | **Date:** 2026-07-03 (TimeBack-parity configuration, engine PRs #26/#34) | **Audience:** Technical reviewers, psychometricians

This document provides a complete technical description of the psychometric model underlying the Incept MAP Proxy. Every equation is cited to its primary source. All engine implementation references are to files in `engine/src/map_engine/`.

---

## 1. Rasch 1-Parameter Logistic Model

### 1.1 The model

The Rasch (1960 [Rasch-1960]) 1-parameter logistic (1PL) model defines the probability that a student with latent ability θ (theta) answers an item with difficulty b correctly:

```
P(correct | θ, b) = 1 / (1 + exp(−(θ − b)))
```

**θ (theta):** Latent ability, expressed in logits on a continuous scale. The logit is the log-odds of a correct response. In the G2–G5 context, the prior at session start is θ₀ = −1.0 logits (corresponding approximately to RIT ≈ 190, the midpoint of the G2–G5 ability distribution under 2025 NWEA norms [NWEA-2025-NM]).

**b (difficulty):** The θ value at which P(correct) = 0.50. An item with b = −1.0 is correctly answered by 50% of students at ability θ = −1.0, by 73% of students at θ = 0.0, and by 27% of students at θ = −2.0.

**Equal-interval property:** The logit scale is equal-interval — one logit represents the same amount of ability gain anywhere on the scale [NWEA-2025-TR]. This property carries forward to the RIT scale (RIT = 200 + 10θ, approximately), enabling arithmetic operations on RIT scores that are not meaningful on percentile scales.

### 1.2 Why not 3PL

The 3-parameter logistic (3PL) model adds item discrimination (a) and pseudo-guessing (c):

```
P(correct | θ, a, b, c) = c + (1−c) × 1 / (1 + exp(−a(θ − b)))
```

MAP Growth's Technical Report specifies the Rasch 1PL as its calibration model [NWEA-2025-TR §3.2][NWEA-VERIFIED]. The practical reason is sample size: estimating a and c reliably requires at minimum 500–1,000 responses per item [Wright-Stone-1979]. Without this data, 3PL would mean assigning invented discrimination and guessing parameters — not measuring them. The Rasch model's single-parameter simplicity is not a limitation for a pre-pilot bank; it is the epistemically honest choice given the available data.

### 1.3 Implementation

From `scorer/mlef.py` (lines 21–28):

```python
def rasch_p(theta: float, b: float) -> float:
    exponent = np.clip(-(theta - b), -500, 500)
    return float(1.0 / (1.0 + np.exp(exponent)))
```

The clip to ±500 prevents numerical overflow on extreme ability/difficulty values without affecting precision in the operational range (θ ∈ [−4, +3]).

---

## 2. MLEF Scoring (Han 2016)

### 2.1 Why MLEF over sum score and EAP

**Sum score:** Treats every correct answer identically regardless of item difficulty. A student who answered 20 easy items correctly and a student who answered 20 hard items correctly receive the same raw score — which maps to different ability levels. MLEF weights each response by the information content of that item.

**EAP (Expected A Posteriori):** Introduces a prior distribution N(μ, σ²) and computes θ̂ as the posterior mean. This regularises extreme response patterns but introduces bias: students with very high or very low ability are shrunk toward the prior mean. For typical G2–G5 students (near the population center), the bias is small. For students at the extremes — the key population for growth tracking — EAP systematically underestimates ability.

**MLEF (Maximum Likelihood Estimation with Fencing; Han 2016 [Han-2016]):** Pure MLE diverges to ±∞ for all-correct or all-incorrect response patterns. MLEF inserts two fictional "fence" items to prevent this divergence without introducing prior-based bias:

```
Lower fence: b_low  = min(b_administered) − 3.8 logits,  response u = 1 (simulated correct)
Upper fence: b_high = max(b_administered) + 3.8 logits,  response u = 0 (simulated wrong)
```

The lower fence, answered correctly, pulls θ away from −∞ for a perfect-fail student. The upper fence, answered incorrectly, pulls θ away from +∞ for a perfect-pass student. The fence offset of 3.8 logits is NWEA's documented constant [NWEA-VERIFIED; NWEA-2025-TR §3.4].

### 2.2 The MLEF algorithm

**Step 1 — Insert fence items.** Construct the fenced response vector:

```
b_fenced = [b_1, b_2, ..., b_n, b_low, b_high]
u_fenced = [u_1, u_2, ..., u_n, 1, 0]
```

**Step 2 — Maximize log-likelihood (Newton-Raphson).** The log-likelihood over the fenced response vector is:

```
log L(θ) = Σᵢ [uᵢ log Pᵢ(θ) + (1−uᵢ) log(1−Pᵢ(θ))]
```

The score function (first derivative) is:

```
dL/dθ = Σᵢ [uᵢ − Pᵢ(θ)]
```

The observed Fisher information (second derivative, negated) is:

```
I(θ) = Σᵢ Pᵢ(θ)(1 − Pᵢ(θ))
```

Newton-Raphson update at iteration k:

```
θₖ₊₁ = θₖ + [dL/dθ|θₖ] / I(θₖ)
```

Convergence criterion: |θₖ₊₁ − θₖ| < 1×10⁻⁶ or 50 iterations exhausted.

**Production solver (TimeBack parity, engine PR #26):** the shipped implementation is a *damped* Newton — each update step is clipped to a trust region of max_step = 1.0 logits — with 6-decimal rounding and the Abramowitz & Stegun 7.1.26 normal-CDF approximation, matching TimeBack's solver bit-for-bit. The v4 validation recorded 0 divergences in ~17,900 production-path sessions, and all 25 divergence regression tests pass against this solver.

**Step 3 — Compute SE (administered items only, fence excluded).** The standard error is computed over the n administered items — not including the artificial fence items, which would artificially inflate precision:

```
SE(θ̂) = 1 / √[Σᵢ₌₁ⁿ Pᵢ(θ̂)(1 − Pᵢ(θ̂))]
```

This is the inverse square root of the Fisher information summed over real items only. In RIT units: SE_RIT = 10 × SE(θ̂) (approximate pre-scale-linking).

### 2.3 EAP cold-start

For the first 2 items, the likelihood function is nearly flat and MLE is unstable. The engine uses Expected A Posteriori (EAP) estimation with a Normal prior N(−1.0, 1.2) — the G2–G5 population prior [NWEA-2025-NM][AUTHORING-DECISION] — on an 81-point quadrature grid over [−4, 4] logits. After 3 or more responses, the engine switches to full MLEF. This matches MAP's documented cold-start approach [NWEA-2025-TR §3.4].

### 2.4 Implementation

From `scorer/mlef.py` (lines 163–210):

```python
# Fence construction
b_lower_val = float(b_raw.min()) - fence_offset   # fence_offset = 3.8
b_upper_val = float(b_raw.max()) + fence_offset
b_fenced = np.concatenate([b_raw, [b_lower_val, b_upper_val]])
u_fenced = np.concatenate([u_raw, [1.0, 0.0]])   # lower=correct, upper=wrong

# SE over non-fence items only
se_info = fisher_information(theta_hat, b_raw.tolist())
se_theta = round(float(1.0 / np.sqrt(se_info + 1e-10)), 2)
```

---

## 3. Partial Credit Model for EBSR (Composite Items)

### 3.1 The two-part EBSR structure

MAP's Composite Item (internally called EBSR — Evidence-Based Selected Response) is a two-part format:

- **Part A:** Answer a comprehension question (inference, theme, character motivation, etc.)
- **Part B:** Select the exact passage sentence that supports Part A

Our scoring rule [AUTHORING-DECISION]:
- Both parts correct: 2 points
- Part A correct only: 1 point
- Part A incorrect: 0 points (regardless of Part B)

Note this partial-credit rule is a deliberate deviation from MAP: NWEA's Technical Report states composite items are scored dichotomously (students must answer each part correctly for credit). We use PCM 0/1/2 because it preserves information from partial responses.

### 3.2 Rasch Partial Credit Model (PCM) approximation

The Rasch Partial Credit Model (Masters, 1982 [ACADEMIC; not in primary refs but standard citation]) represents polytomous items as a sequence of binary thresholds. For a 3-category EBSR item (scores 0, 1, 2), we expand to two binary pseudo-items at thresholds b and b+Δ:

```
Pseudo-item 1: difficulty = b         (threshold for 0→1, i.e., Part A correct)
Pseudo-item 2: difficulty = b + Δ     (threshold for 1→2, i.e., Part B also correct)
```

The pseudo-item responses are:
- Score 0: pseudo-item 1 = 0, pseudo-item 2 = 0
- Score 1: pseudo-item 1 = 1, pseudo-item 2 = 0
- Score 2: pseudo-item 1 = 1, pseudo-item 2 = 1

The step parameter Δ = 0.5 logits is an authoring estimate [AUTHORING-DECISION]. It represents the additional difficulty of providing verbatim textual evidence beyond getting Part A correct. Post-pilot Rasch PCM calibration will estimate the actual Δ from response data.

### 3.3 Implementation

From `scorer/mlef.py` (lines 63–73):

```python
if itype == "composite":
    b_expanded.append(float(b))           # Part A threshold
    u_expanded.append(1 if u >= 1 else 0) # credit if score >= 1
    b_expanded.append(float(b) + delta)   # Part B threshold
    u_expanded.append(1 if u == 2 else 0) # full credit only if score == 2
```

### 3.4 Fisher information for EBSR items

For EBSR composite items, Fisher information is summed across both pseudo-items [AUTHORING-DECISION based on standard PCM literature]:

```
I_EBSR(θ) = P₁(θ)(1−P₁(θ)) + P₂(θ)(1−P₂(θ))
```

where P₁ uses b and P₂ uses b+Δ. This sum is typically 10–30% larger than a single binary item at the same difficulty, reflecting the additional measurement power of the two-part format.

---

## 4. Fisher Information Item Selection

### 4.1 The principle

Fisher information measures how much a single item contributes to precision of the θ estimate. For a binary Rasch item:

```
I(θ, b) = P(θ, b) × (1 − P(θ, b))
```

This is maximized when b = θ — i.e., when item difficulty exactly matches student ability. At that point P = 0.5, so I = 0.25, the theoretical maximum for a binary item. Items much easier or harder than the student's ability contribute nearly zero information [AERA-2014].

The CAT's item selection rule — select the item that maximizes Fisher information at the current θ̂ — ensures that measurement precision is concentrated at the student's true ability level, not wasted on floor or ceiling items [Kingsbury-1989].

### 4.2 Constrained selection

Raw Fisher-information maximization would repeatedly select the same few items near the population mean. MAP Growth adds content constraints — domain quotas — that ensure blueprint coverage regardless of student ability [NWEA-2025-TR §3.3][Kingsbury-1989]. Our engine implements:

1. **Domain quotas:** 14 Literary / 13 Informational / 13 Vocabulary on the 40-item scored form. NWEA's TR Table 3.2 shows an *example* 13/13/13 blueprint; the engine adopts TimeBack's operational 14/13/13 split [AUTHORING-DECISION; NWEA-VERIFIED for the 40–43 structure]
2. **Shadow feasibility:** Before selecting a passage group (3–5 items), verify that the remaining bank items can still satisfy all remaining domain quotas [AUTHORING-DECISION based on shadow-test literature]
3. **Topic cap:** No topic_tag may appear more than twice per session [AUTHORING-DECISION]
4. **Lexile band filter:** Items must have b_provisional within ±1.5 logits of current θ̂ [AUTHORING-DECISION]
5. **TEI floor:** ≥12 Technology-Enhanced Items per session, with gap-match now correctly counted as TE (per TimeBack `TECHNOLOGY_ENHANCED_FORMATS`) [DERIVED from NWEA ">30% TEI" blog, March 2025; NWEA-VERIFIED]
6. **Randomesque exposure control:** selection among the top-5 information-ranked candidates, applied in both the quota-filling phase and the precision-extension phase (items 41–43) [AUTHORING-DECISION; Kingsbury-1989 randomesque procedure]

### 4.3 Implementation

From `assembly/adaptive_selector.py` (lines 60–75):

```python
def fisher_information_at(theta, b, item_type="binary", delta=0.5):
    p1 = 1.0 / (1.0 + math.exp(-(theta - b)))
    info = p1 * (1.0 - p1)
    if item_type == "composite":
        p2 = 1.0 / (1.0 + math.exp(-(theta - (b + delta))))
        info += p2 * (1.0 - p2)
    return info
```

Passage-level selection scores a passage by the sum of Fisher information across all its items at the current θ̂, with a 30% boost for passages containing TEI items when the TEI floor has not yet been met.

---

## 5. CAT Termination Rules

Under the TimeBack-parity configuration (engine PRs #26/#34), the engine uses a **precision stop**: a session may end only when the scored floor, the quotas, the TEI floor, *and* the SE target are all satisfied — quotas alone never stop the test. Sessions that reach 40 items without meeting SE ≤ 0.35 continue into a precision-extension band (items 41–43, still selected with randomesque exposure control) until the SE target or the hard cap is reached:

```python
# From assembly/adaptive_selector.py should_terminate() (parity configuration):
if n >= HARD_CAP:                                                        return True  # (1) always
if n >= ADAPTIVE_ITEMS_MIN and quotas_done and tei_floor_met \
        and se <= SE_STOP:                                               return True  # (2) precision stop
# quotas alone never stop the test; items 41-43 form the precision-extension band
```

| Rule | Condition | Rationale |
|---|---|---|
| Hard cap | 43 items administered | MAP maximum per NWEA's published 40–43 structure [NWEA-VERIFIED] |
| Precision stop | ≥40 items AND quotas met AND TEI floor met AND SE ≤ 0.35 | 40 scored items is the floor before any stop; SE is evaluated only at ≥40 items |
| Precision extension | items 41–43 when SE > 0.35 at the scored floor | Buys additional precision for hard-to-measure students before the cap |

In the v4 validation, sessions averaged 40.6 items: 76.5% stopped at exactly 40 (SE ≤ 0.35 met at the scored floor), 15.1% ran to the 43-item hard cap, and no session stopped below 40.

**Constants (TimeBack-parity values; pre-parity values shown for the record):**

| Parameter | Value | Source |
|---|---|---|
| ADAPTIVE_ITEMS_MIN (scored floor) | 40 (was 39 as "TOTAL_ITEMS" pre-parity) | TimeBack operational configuration, consistent with NWEA's published 40–43 structure [AUTHORING-DECISION; NWEA-VERIFIED for 40–43] |
| HARD_CAP | 43 | NWEA's published maximum [NWEA-VERIFIED] |
| SE_STOP_THRESHOLD | 0.35 logits, evaluated only at ≥40 items (was 0.30 with an early stop at ≥20) | TimeBack parity [AUTHORING-DECISION; ASSEMBLED] |
| DOMAIN_QUOTAS | 14/13/13 (was 13/13/13) | TimeBack operational split [AUTHORING-DECISION] |
| TEI_FLOOR | 12, gap-match counted as TE (was 15) | >30% of 40 items = ≥12 [DERIVED; NWEA blog March 2025] |
| FENCE_OFFSET | 3.8 logits | NWEA documented constant [NWEA-VERIFIED] |
| PRIOR_MEAN | −1.0 logits | G2–G5 population midpoint [DERIVED; NWEA-2025-NM] |
| PRIOR_SD | 1.2 logits | G2–G5 cross-grade SD [DERIVED; NWEA-2025-NM] |

---

## 6. b_provisional Assignment

### 6.1 How b_provisional is assigned

All items in the bank carry provisional difficulty parameters (b_provisional) assigned at authoring time using two inputs:

1. **Target RIT band:** Each item is authored for a specific RIT band (e.g., 181–190). The midpoint of that band converts to a logit: b_prov = (midpoint − 200) / 10.
2. **Lexile filter:** Items are filtered during CAT selection to ensure they are within ±1.5 logits (≈±15 RIT) of the student's current θ̂. This provides a coarse guard against serving items far outside the student's zone of proximal development.

Example: an item authored for band 191–200 receives b_provisional = (195 − 200) / 10 = −0.5 logits.

### 6.2 Expected accuracy

The uncertainty in b_provisional is estimated at σ ≈ 0.5–1.0 logits (5–10 RIT) based on the typical discrepancy between Lexile-derived difficulty estimates and empirically calibrated Rasch b values [AUTHORING-DECISION; DERIVED from literature on Lexile→IRT mapping]. Simulation 3 confirms the engine is robust to this level of uncertainty: reliability remains above 0.85 at σ = 1.0 logits [SIMULATION].

### 6.3 Calibration target

After a field trial of N = 1,000 students:

- Core-band items (b ≈ −1.0 to +0.5): ~250–350 exposures → SE(b̂) ≤ 0.30 logits (3 RIT) [DERIVED; Wright-Stone-1979]
- Tail-band items (b < −2.0 or b > +1.5): ~50–100 exposures → SE(b̂) ≤ 0.60 logits (6 RIT) (Stage 1 quality only)

SE(b̂) shrinks approximately with 1/√N; following Linacre (1994 [Linacre-1994]) and Wright & Stone (1979 [Wright-Stone-1979]), we target N ≈ 200 well-targeted responses per item for SE(b̂) ≤ 0.30 logits, and N ≈ 800 for SE(b̂) ≤ 0.15. These are conservative targets.

### 6.4 Current status

| Stage | b̂ quality | SE(b̂) | Status |
|---|---|---|---|
| Current (pre-field-trial) | Provisional (Lexile-derived) | ±∞ (no data) | [AUTHORING-DECISION] |
| After N=1,000 field trial | Stage 2 calibration | ≤ 0.30 logits (core band) | Target |
| After N=5,000 operational | Stage 3 calibration | ≤ 0.15 logits | NWEA-equivalent |

---

## 7. RIT-to-θ Transformation

### 7.1 The formula

NWEA's published approximation [NWEA-2025-TR]:

```
RIT = 200 + 10 × θ
```

This linear transformation maps Rasch logits to the RIT scale. It is an approximation of NWEA's proprietary transformation. The exact NWEA coefficients are not publicly available.

### 7.2 Pre-pilot constraint

Because our b_provisional values are not yet anchored to NWEA's scale, applying `RIT = 200 + 10θ` to our θ̂ estimates would produce numbers that look like MAP RITs but are not comparable to them. The engine intentionally blocks RIT output pre-pilot [AUTHORING-DECISION]. All scores are reported as Rasch logit θ̂ ± SE(θ̂).

Post-scale-linking, the correct transformation is:

```
RIT_ours = a × θ̂ + c
SE_RIT   = a × SE(θ̂)
```

where a and c are estimated via OLS regression of our θ̂ scores against paired NWEA MAP RITs from the concurrent validity study [Kolen-Brennan-2014].

---

## 8. Summary of Design Choices vs. MAP

| Design dimension | MAP Growth | Incept Proxy | Match? | Evidence |
|---|---|---|---|---|
| IRT model | Rasch 1PL | Rasch 1PL | MATCH | [NWEA-VERIFIED; NWEA-2025-TR] |
| Scoring algorithm | MLEF, fence=3.8 | MLEF, fence=3.8 | MATCH | [NWEA-VERIFIED; NWEA-2025-TR §3.4] |
| Cold-start | EAP (prior = population) | EAP items 1–2, MLEF from item 3 | MATCH | [NWEA-2025-TR §3.4] |
| EBSR scoring | Dichotomous (both parts required) | PCM 0/1/2 pseudo-item expansion | DELIBERATE DEVIATION | [AUTHORING-DECISION; preserves partial-response information] |
| Item selection | Max Fisher info + constraints | Max Fisher info + domain quotas + randomesque | MATCH (direction) | [NWEA-2025-TR §3.3] |
| Domain quotas | Example blueprint 13/13/13 (Table 3.2) | 14/13/13 = 40 scored (TimeBack operational split) | CONSISTENT (disclosed operational choice) | [AUTHORING-DECISION; NWEA-2025-TR Table 3.2] |
| Test length | 40–43 questions (test description) | 40 scored, extending to 43 for precision | MATCH | [NWEA-VERIFIED] |
| Termination | SE threshold + quotas | Precision stop: ≥40 items, quotas, TEI ≥12, SE ≤ 0.35 | MATCH (approx) | [ASSEMBLED; NWEA-2025-TR] |
| b-parameter source | Empirical calibration (≥1,000) | Provisional (Lexile-derived) | GAP | Pre-pilot constraint |
| RIT output | Calibrated NWEA scale | Blocked pre-pilot | GAP | Intentional design |
| PCM step Δ | Empirically calibrated | 0.5 logits (provisional) | GAP | Pre-pilot estimate |

---

## Sources

Full APA bibliography in the Sources tab. Key references for this document:

- [Rasch-1960] Rasch, G. (1960). *Probabilistic models for some intelligence and attainment tests*. Danish Institute for Educational Research.
- [Han-2016] Han, K. T. (2016). Maximum likelihood score estimation method with fences for short-length tests and computerized adaptive tests. *Applied Psychological Measurement, 40*(4), 289–301.
- [NWEA-2025-TR] NWEA. (2026). *MAP Growth Technical Report for 2024–2025*. NWEA/HMH. §§ 3.2, 3.3, 3.4, Table 3.2.
- [Wright-Stone-1979] Wright, B. D., & Stone, M. H. (1979). *Best test design*. MESA Press.
- [Linacre-1994] Linacre, J. M. (1994). Sample size and item calibration stability. *Rasch Measurement Transactions, 7*(4), 328.
- [Kingsbury-1989] Kingsbury, G. G., & Zara, A. R. (1989). Procedures for selecting items for computerized adaptive tests. *Applied Measurement in Education, 2*(4), 359–375.
- [Stocking-1994] Stocking, M. L. (1994). *Three practical issues for modern adaptive testing item pools*. ETS Research Report RR-94-5.
- [AERA-2014] American Educational Research Association et al. (2014). *Standards for educational and psychological testing*. AERA.
- [Kolen-Brennan-2014] Kolen, M. J., & Brennan, R. L. (2014). *Test equating, scaling, and linking* (3rd ed.). Springer.
