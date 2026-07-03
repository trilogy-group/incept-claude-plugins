# Concurrent Validity Study Design — MAP Proxy Adaptive Assessment
**Version:** 2.0 | **Date:** 2026-07-03 | **Audience:** Investors, researchers, school partners

This document describes the research design for the concurrent validity study that will link the Incept MAP Proxy to NWEA's RIT scale and enable the product's primary commercial claim: "a student scoring X on our test would score approximately X on MAP."

---

## 1. Why Simulations Are Insufficient for Scale Linking

### 1.1 The fundamental problem

The Incept MAP Proxy and NWEA MAP Growth both measure reading ability using the Rasch 1PL model with MLEF scoring. However, the two tests are on different Rasch scales:

- **NWEA's RIT scale** is anchored to decades of empirical calibration across hundreds of thousands of students and a bank of 40,000+ items with known parameters [NWEA-2025-TR].
- **Our logit scale** is anchored to b_provisional values assigned by content experts, with no empirical calibration data.

Even if the algorithm is correct (proven by simulations), the scales may differ in origin (the constant c in RIT = a×θ + c) and in slope (a). A student who would score RIT 195 on MAP might score θ̂ = −0.5 logits on our test — but under the approximate formula RIT ≈ 200 + 10θ, that maps to RIT 195. Or it might map to RIT 188. Without paired scores, we cannot know.

This is not an algorithm problem — it is a measurement scaling problem. It is solved by scale linking, not by better simulations [Kolen-Brennan-2014 §1].

### 1.2 Why Simulation 4 (internal cross-bank consistency) is not sufficient

Simulation 4 — relabelled **internal cross-bank consistency (synthetic)**, because that is what it is — used a **synthetic MAP-like bank** with items drawn from an approximate difficulty distribution. The synthetic bank is not NWEA's actual bank. Even if it were, simulations assume the Rasch model is correctly specified — that all items discriminate equally and no guessing occurs. Real MAP items have been calibrated against millions of student responses; our provisional items have not. The v3 result (2026-07-03: r 0.912, 95% LoA [−10.7, +10.2] RIT, with disclosed synthetic-bank caveats) is a consistency check on the engine, not evidence of MAP agreement.

The study described in this document will replace the synthetic comparisons with real paired scores and, if successful, unlock RIT output in the engine. Any projected post-linking LoA is a hope stated in advance, not a result — see §4.2.

---

## 2. Study Design: Concurrent Validity and Scale Linking

### 2.1 Design overview

**Research question:** What is the linear transformation that maps our Rasch logit (θ̂) to NWEA MAP RIT, and how accurate is the resulting RIT estimate?

**Design type:** Concurrent administration study (students take both tests within 2 weeks) [AERA-2014 §4.3].

### 2.2 Sample requirements

| Stage | N | Purpose | SE(a), SE(c) achievable |
|---|---|---|---|
| Feasibility pilot | ~40 | Usability, engagement, early red flags | (no linking claims) |
| Stage 2 (calibration, accrued via regular use) | ~300-student-equivalent response volume, growing to 1,000 | Calibrate item b values; refine linking | SE(linking) ≈ 1.5–2 RIT at N=1,000 |
| Stage 3 (full validation) | 2,000 | Cross-validated linking; concurrent validity | SE(linking) ≈ 1.0–1.5 RIT |

Sample size formulas for linking precision are from Kolen & Brennan (2014 [Kolen-Brennan-2014] §4.3). For a linear equating with N=1,000, the RMSE of the linking transformation is approximately 1–2 RIT — sufficient for educational decision-making.

**The honest arithmetic behind the ladder.** The pilot is ~40 students (1–2 classes) × ~40 items ≈ 1,600 responses against a 766-item bank — far below the ~200 responses per item that calibration requires, so the pilot makes **no calibration claims**. Its purpose is feasibility: completion rate, session duration, rapid-guess rates, teacher and student experience, and early item red flags from response patterns. Calibration then **accrues from regular use**: ongoing sessions accumulate toward the calibration thresholds (a ~300-student-equivalent response volume for core-band calibration), and the linking cohort (N ≥ 1,000 concurrent pairs) accrues through usage at the Fall 2026 MAP window — not through a separate recruitment.

**Grade composition target (linking cohort):** balanced across G2–G5, with at least 200 students per grade in the accrued linking cohort. This ensures item calibration is adequate across the full bank, not just the grade-center.

**Ability distribution target:** representative of the intended test-taking population. Schools serving a wide range of RIT levels are preferred to avoid restriction of range, which reduces linking precision [Kolen-Brennan-2014 §2.4].

**Tail coverage (pre-committed).** Natural CAT exposure concentrates responses at the population center: tail-band items would see only ~50–100 responses each under proportional usage — below the calibration floor. Two commitments follow. First, within the ~40-student pilot, deliberately include **≥8 below-median G2 readers and ≥8 above-median G5 readers** — this is coverage and feasibility at the edges (floor/ceiling UX and flag behavior), not calibration. Second, the **≥150 responses per tail-band item** target (floor bands ≈ RIT 155–180; ceiling bands ≈ RIT 225–245) attaches to the calibration stage that accrues from regular use. Per (grade × difficulty band) cell:

| Cell | Pilot (~40) inclusion | Calibration target (accrued via regular use) |
|---|---|---|
| G2 × floor bands (RIT 155–180) | ≥8 below-median G2 readers (floor UX, flag behavior) | ≥150 responses per item |
| G3–G4 × core bands (RIT 181–220) | Remainder of the cohort, proportional | ≥200 responses per item (natural exposure suffices) |
| G5 × ceiling bands (RIT 225–245) | ≥8 above-median G5 readers (ceiling UX, flag behavior) | ≥150 responses per item |

### 2.3 Counterbalancing design

All students take both tests (within 2 weeks). Order is counterbalanced to control for practice effects and fatigue:

| Group | Week 1 | Week 2 |
|---|---|---|
| A (50%) | Incept proxy | NWEA MAP |
| B (50%) | NWEA MAP | Incept proxy |

The 2-week window is the standard practice for concurrent validity studies in educational assessment [AERA-2014 §4.3]. Shorter windows risk carryover from item exposure; longer windows introduce growth as a confound.

**Exclusion criteria:**
- Students who experienced illness or unusual testing conditions on either test
- Students whose MAP scores are invalid (NWEA flags)
- Students whose Incept proxy sessions were incomplete (< 30 items administered)

### 2.4 Administration requirements

- The NWEA MAP must be administered via the school's existing NWEA account under standard conditions
- The Incept proxy can be administered in any modern browser, without lockdown software
- Both tests must be administered in the same testing window (fall, winter, or spring — not across seasons)
- Schools must be NWEA-authorized MAP administrations; we cannot use unofficial MAP administrations

---

## 3. Scale Linking Methodology

### 3.1 Linear equating (Tucker method)

The primary linking approach is linear equating [Kolen-Brennan-2014 §4.2]:

```
RIT_ours = a × θ̂ + c
```

where:
- θ̂ is our MLEF logit score for a student
- RIT_ours is our estimate of what that student would score on MAP
- a and c are estimated by OLS regression of paired (θ̂, MAP RIT) scores

The regression is fit on 80% of the concurrent study sample and validated on the held-out 20% [DERIVED from standard cross-validation practice].

**SE_RIT for individual students:**
```
SE_RIT_ours = a × SE(θ̂)
```

This is the per-student score uncertainty in RIT units, reported alongside the score.

### 3.2 Alternative: concurrent calibration

The stronger approach places both test banks on a common scale through concurrent Rasch calibration [Kolen-Brennan-2014 §6]. Both our items and a subset of NWEA anchor items are calibrated in the same Rasch analysis, directly placing our b values on NWEA's logit scale. This eliminates the need for a post-hoc linear transformation.

**Requirement:** NWEA anchor items must be released or shared under a data-sharing agreement. This is more complex to negotiate but produces superior scale accuracy.

**Recommendation:** Begin with linear equating (lower barrier) and negotiate concurrent calibration as the long-term approach for achieving ±2 RIT absolute accuracy.

### 3.3 Anchor-item equating (if NWEA releases public items)

If NWEA releases a set of publicly available items with known calibrated b values (as some state departments have done with released MAP items), anchor item equating [Kolen-Brennan-2014 §5] can be used:

1. Embed 5–10 NWEA-released items in our test bank with their published b values
2. Use these anchor items to fix the scale origin
3. Calibrate our non-anchor items relative to the anchor scale

**Status:** No NWEA anchor items are publicly available as of June 2026. This approach is contingent on NWEA policy changes.

### 3.4 Pre-committed EBSR scoring decision

Our EBSR partial-credit scoring (PCM 0/1/2) is a disclosed deviation from MAP's dichotomous composite rule. Rather than deciding by argument, the decision is **pre-committed to data, before RIT unlock**:

- **Procedure:** the pilot scores every EBSR both ways in parallel — PCM 0/1/2 and dichotomous — via the dual-scoring comparator already built into the engine (PR #33).
- **Decision statistic:** the mean absolute linking-residual difference between the two scoring rules, computed on EBSR-heavy sessions (≥3 EBSR items), with a bootstrap 95% confidence interval.
- **Criterion:** dichotomous scoring wins if its linking residuals are lower *and* the CI excludes zero; otherwise PCM is retained. The decision is made before RIT output is unlocked, so the shipped RIT transformation is fitted under the winning rule.
- **Selection caveat, flagged for item-fit analysis:** the PCM step Δ=0.5 also affects Fisher information and therefore item *selection*, not just scoring — the item-fit analysis will examine whether EBSR selection behavior differs materially between rules.

### 3.5 Norms handling in the linking data (Stage-3 data-prep dependency)

The linking regression itself is **norm-independent**: it regresses our θ̂ on the raw `testritscore` from paired MAP records, which no norm set touches. However, Alpha's historical MAP records carry norm-**referenced** fields (percentiles, growth projections) computed under `normsreferencedata: "2020"`; any context display that juxtaposes those fields with 2025-norm figures must reinterpret them under the 2025 norms first. This reinterpretation is a named **Stage-3 data-preparation dependency** — it does not affect the linking coefficients, only the surrounding context reporting.

---

## 4. Expected Results Pre- and Post-Calibration

### 4.1 Pre-calibration (current state)

Based on the internal cross-bank consistency simulation (Sim 4, synthetic — NOT MAP agreement) [SIMULATION] and the psychometric literature on pre-calibration assessments:

| Metric | Current estimate | Basis |
|---|---|---|
| Correlation with MAP | r ≈ 0.85–0.92 | Sim 4, v3 run: r=0.912 against a *synthetic* bank [SIMULATION] |
| 95% LoA | ±8–15 RIT | Sim 4, v3 run: [−10.7, +10.2] RIT (synthetic-bank caveats disclosed) [SIMULATION] |
| Mean difference | small residual expected | v3: overall bias −0.38 RIT (the v1 +2.62 overestimate was root-caused to the Owen running estimate and resolved); a residual −0.4 to −1.0 RIT negative bias persists in the RIT 175–190 bands and is under scorer-only decomposition; the linking intercept absorbs any constant component [SIMULATION] |

### 4.2 Post-calibration (N=1,000 concurrent study) — a stated hope, not a projection we can defend

**Status: Open / [DERIVED-hope].** The figures below are what comparable N=1,000 equating studies have achieved [Kolen-Brennan-2014]. Nothing in our simulation evidence *entitles* us to them — the synthetic consistency check cannot ground a claim about agreement with real MAP scores. We state them in advance so the linking study has a benchmark to be judged against, and we will report whatever the data says:

| Metric | Hoped-for post-linking | Basis |
|---|---|---|
| Correlation with MAP | r ≈ 0.88–0.95 | [DERIVED-hope; equating literature] |
| 95% LoA | ±5–8 RIT | [DERIVED-hope; N=1,000 equating studies, Kolen-Brennan-2014] |
| Mean difference | < 1 RIT | [DERIVED; by design of linear equating] |

If achieved, the improvement would reflect: (1) empirical b calibration reducing item-level uncertainty from σ≈0.5 logits to σ≈0.3 logits, and (2) the linear transformation correcting any systematic scale offset.

A 95% LoA of ±5–8 RIT would make the proxy suitable for instructional decisions and cohort-level reporting [DERIVED]. MAP's own reported SEM is ≤4 RIT [NWEA-2025-TR]; a proxy adding ±5–8 RIT on top of this produces a total uncertainty of ±6–9 RIT — not sufficient for individual high-stakes placement decisions without additional validation. If the pilot lands outside these ranges, the honest deliverable is the measured range, not this table.

---

## 5. Stage-Gated Rollout

### Stage 1 (current): Algorithm validity only ✅

**Status:** Complete
**What's unlocked:** Logit score (θ̂ ± SE) output, diagnostic domain sub-scores, blueprint-compliant adaptive delivery
**What's blocked:** RIT output, percentile, CGP, growth tracking
**Evidence required:** None beyond simulations (done)

### Stage 2a (~40 students): Feasibility pilot

**Status:** The current ask — 1–2 classes, G2–G5, one adaptive session each
**Trigger:** Approval of the pilot
**Purpose (feasibility, not calibration):** ~40 students × ~40 items ≈ 1,600 responses cannot calibrate a 766-item bank (calibration needs ~200 responses per item), so the pilot claims none. It establishes:
- Completion rate and session duration under real classroom conditions
- Rapid-guess rates and engagement-flag behavior
- Teacher and student experience (including floor/ceiling UX for the deliberately included tail readers: ≥8 below-median G2, ≥8 above-median G5)
- Early item red flags from response patterns (obviously broken items, suspicious response clusters)

**Success/kill criteria (usage-based — all meaningful at N=40):** session completion ≥ 90%; session duration within the expected 30–60-minute envelope; rapid-guess rate < 10%. Criteria that require calibration-scale data (e.g., proportion of items passing Rasch fit statistics) belong to Stage 2b, not the pilot.

**Timeline:** days of testing inside 1–2 classes
**Cost:** negligible (existing infrastructure)

### Stage 2b (accrued via regular use): Item calibration + internal structure

**Status:** Accrues automatically as the instrument is used between MAP windows — no separate recruitment
**Trigger:** Accumulated response volume reaching calibration thresholds (~300-student-equivalent for the core band; ≥150 responses per tail-band item for the tails)
**Activities:**
- Rasch-calibrate items as their response counts cross thresholds; retire items failing fit statistics
- Conduct confirmatory factor analysis to verify domain structure
- Compute post-calibration reliability (expected: rise to ≥ 0.93)

**What's unlocked after Stage 2b:** Improved logit score accuracy; preliminary reliability data for investors/partners; ability to claim "calibrated bank" vs. "provisional bank"

**Timeline:** a function of usage volume; core-band thresholds are reachable within a school term of regular use
**Cost:** ~$500 (infrastructure) + school coordination cost

### Stage 3 (N=1,000 concurrent): Scale linking + concurrent validity

**Status:** Requires NWEA-authorized school partnership
**Trigger:** Completion of concurrent administration study (Incept + MAP, same students, same season)
**Activities:**
- Concurrent study: N ≥ 1,000 paired sessions — accrued through regular use at the Fall 2026 MAP window, not separately recruited — with both tests taken within 2 weeks (tail coverage per §2.2)
- Data prep: link on raw `testritscore` (norm-independent); reinterpret historical norm-referenced fields (`normsreferencedata: "2020"`) under 2025 norms for any context display (§3.5)
- Decide the EBSR scoring rule on the pre-committed statistic (§3.4) — before RIT unlock
- Fit linear transformation RIT_ours = a × θ̂ + c
- Compute correlation, mean difference, 95% LoA vs. MAP
- **Unlock RIT output core-band-first (band-aware gate):** RIT unlocks for the calibrated core band (requires r ≥ 0.80 and mean diff < 5 RIT there); **floor- and ceiling-flagged scores stay logit-only** until tail-targeted calibration reaches SE(b̂) ≤ 0.30 in those bands too. A single global unlock would let core-band success mask tail unreliability — the gate is band-aware by design
- Publish technical report on concurrent validity

**What's unlocked after Stage 3:** RIT output (core band first, tails on their own evidence), percentile rank, CGP (conditional growth percentile), full product commercial claim
**Timeline:** reads out at the Fall 2026 MAP window, once the paired cohort has accrued
**Cost:** ~$2,000 (infrastructure) + school coordination + possible NWEA data-sharing agreement

### Stage 4 (N=5,000+): Full operational validation

- Cross-grade validation (separate linking studies per grade band)
- DIF (Differential Item Functioning) analysis across demographic groups
- Test-retest reliability study
- Sympson-Hetter exposure control calibration
- Publication in peer-reviewed journal

---

## 6. RIT Output: Currently Blocked

RIT output is blocked in the engine pre-scale-linking [AUTHORING-DECISION]. The engine computes `RIT_approx = 200 + 10 × θ̂` internally for display in developer-facing logs, but this value is not surfaced in the student score report or API response. The score report outputs:

**Pre-pilot (current):**
- Overall logit score: θ̂ ± b-uncertainty-adjusted SE — the Fisher SE inflated by the current validation run's RMSE/SEM ratio (1.08 under v3), with an explicit `se_basis` field naming the adjustment; the inflation is removed automatically post-calibration (engine PR #33)
- Domain logit scores: θ̂_literary, θ̂_informational, θ̂_vocabulary ± SE
- Reliable range flag: "above/within/below reliable range"

**Post-scale-linking (Stage 3+):**
- Overall RIT: RIT_ours ± SE_RIT (unlocked core-band-first; floor/ceiling-flagged scores stay logit-only until tail calibration reaches SE(b̂) ≤ 0.30)
- Domain RITs: unlocked (same band-aware gate)
- National percentile: unlocked (requires 2025 norms mapping)
- CGP: unlocked (requires prior RIT + conditional growth norms)

---

## Sources

- [Kolen-Brennan-2014] Kolen, M. J., & Brennan, R. L. (2014). *Test equating, scaling, and linking: Methods and practices* (3rd ed.). Springer.
- [AERA-2014] American Educational Research Association, American Psychological Association, & National Council on Measurement in Education. (2014). *Standards for educational and psychological testing*. AERA.
- [NWEA-2025-TR] NWEA. (2026). *MAP Growth Technical Report for 2024–2025*. NWEA/HMH.
- [Wright-Stone-1979] Wright, B. D., & Stone, M. H. (1979). *Best test design*. MESA Press.
