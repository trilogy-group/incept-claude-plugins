# Limitations — MAP Proxy Adaptive Assessment
**Version:** 2.0 | **Date:** 2026-07-03 (v3 TimeBack-parity validation) | **Audience:** All (especially due-diligence reviewers)

This document provides a complete, honest disclosure of all known limitations of the Incept MAP Proxy. Its purpose is to make the investor case credible by demonstrating that we understand what we don't know. Every limitation includes: the limitation statement, its practical impact, and the mitigation plan.

---

## Limitation 1: b_provisional Values Are Assigned, Not Calibrated

### Statement
All 650 items in the bank carry provisional difficulty parameters (b_provisional) assigned by content experts based on target RIT band and passage Lexile. No empirical response data has been collected. The statistical uncertainty on each b̂ is effectively infinite: SE(b̂) = ∞ [Wright-Stone-1979]. This means we do not know how hard any individual item actually is for students.

### Practical impact
Item selection uses b_provisional values to compute Fisher information. If an item's true difficulty is 5–10 RIT harder than its provisional value, the CAT will select it for students at a lower ability level than appropriate — wasting an item slot on a near-ceiling item instead of an informative one. This reduces measurement precision. Simulation 3 shows the engine tolerates this at the expected σ ≈ 0.5–1.0 logits level (reliability ≥ 0.85 maintained) [SIMULATION], but precision is below what it will be post-calibration.

**Quantitative impact:** RMSE under the v3 run (2026-07-03) is 3.44 RIT — within the <4.0 target — and is expected to improve further toward ~3.0 RIT after N=1,000 empirical calibration. Reliability is expected to rise from 0.929 to ≥ 0.93 [DERIVED; based on Sim 3 results and calibration literature]. Meanwhile, because provisional b values understate score uncertainty, **score reports emit a b-uncertainty-adjusted SE** — the Fisher SE inflated by the current validation run's RMSE/SEM ratio (1.08 under v3) — with an explicit `se_basis` field; the inflation is removed automatically once empirical calibration lands (engine PR #33).

### Mitigation
Field trial (N ≥ 1,000 students): Rasch-calibrate all items. Items with INFIT > 1.30 or point-biserial < 0.20 are retired or revised. Core-band items (RIT 185–210) will achieve SE(b̂) ≤ 0.30 logits (3 RIT) — the operational calibration target [Wright-Stone-1979; Linacre-1994]. Timeline: 6–12 months with school partnership.

---

## Limitation 2: A Residual Band-Level Negative Bias Remains, and the Reported SE Requires Inflation Pre-Calibration

### Statement
The v1 production-path re-run (2026-07-02) flagged RMSE 4.73 RIT and a **+2.62 RIT systematic overestimate** — we reported the regression rather than the earlier, prettier number. Both were subsequently root-caused and resolved: the bias lived in the **Owen running estimate's prior shrinkage**, not in the shipped score, and re-basing the final score on the score report's MLEF `overall_logit` (v2) removed it. Under the authoritative v3 run (2026-07-03, TimeBack-parity configuration), RMSE is **3.44 RIT** (within the <4.0 target) and overall bias is **−0.38 RIT** (reliable-range −0.27; max per-band 0.83 — all within criteria). What remains: a **residual negative bias of −0.4 to −1.0 RIT in the RIT 175–190 bands** (largest −1.04 at 175–180, below the reliable floor), and marginal reliability of 0.929 vs the ≥0.93 target (≈0.001 gap).

### Practical impact
Students in the 175–190 bands read slightly low on average pre-calibration; for a student near a policy threshold in those bands, this could misclassify in the *conservative* direction. Core-band precision meets targets (SEM 3.18 RIT, reliability 0.929). Because provisional b values understate uncertainty, the plain Fisher SE would read too tight — so **score reports emit a b-uncertainty-adjusted SE** (Fisher SE × RMSE/SEM ratio = 1.08 under v3) with an explicit `se_basis` field naming the adjustment [engine PR #33]. The adjustment is removed automatically post-calibration.

### Mitigation
A scorer-only decomposition (S12) of the residual 175–190-band bias is the queued follow-up. Empirical calibration — accrued through regular use toward a ~300-student-equivalent response volume for the core band — replaces the expert-assigned b values that drive both the residual bias and the reliability gap. The plan is designed to resolve this; simulation supports but cannot guarantee it.

---

## Limitation 3: RIT Output Is Blocked — No Scale Linking Yet

### Statement
The engine produces logit scores (θ̂ ± SE) but not RIT scores. RIT output is intentionally blocked until the linear scale-linking transformation RIT_ours = a × θ̂ + c is estimated from a concurrent validity study [AUTHORING-DECISION; Kolen-Brennan-2014].

### Practical impact
The most significant commercial limitation. Without RIT output:
- Schools cannot directly compare proxy scores to historical MAP data
- Growth over time can only be tracked as logit changes, not RIT changes
- Percentile rank, Conditional Growth Percentile (CGP), and norm-referenced reports are unavailable
- The product cannot be marketed as a "MAP equivalent" in the fullest sense — only as a "MAP-design proxy"

The logit score is a valid ability estimate on an internal scale. It supports within-class comparisons, relative ranking, and diagnostic domain identification. It does not support cross-school or national norm comparisons.

### Mitigation
Stage 3 concurrent validity study (N ≥ 1,000 paired sessions accrued through regular use at the Fall 2026 MAP window; same students take both Incept proxy and NWEA MAP within 2 weeks). After fitting the linear transformation, RIT output is unlocked. Full study design in the Concurrent Validity Plan tab.

---

## Limitation 4: No Concurrent Validity Data

### Statement
We have not yet administered our test and the real MAP to the same students. The [−10.7, +10.2] RIT 95% Limits of Agreement from Simulation 4 — relabelled **internal cross-bank consistency (synthetic)**, because that is what it measures — is based on a synthetic MAP-like bank, not actual NWEA items, and carries disclosed caveats (format relabelling to satisfy the TEI floor; the synthetic bank's quota fit) [SIMULATION].

### Practical impact
We cannot currently claim "a student who scores X on our test would score X on MAP." This is the fundamental commercial claim the product depends on, and it is not yet proven. The v3 consistency result (r=0.912, LoA [−10.7, +10.2] RIT) is an engine consistency check — explicitly not MAP agreement evidence.

**What we can claim pre-pilot:**
- The algorithm correctly ranks students by reading ability (r=0.963, v3 run) [SIMULATION]
- The test is reliable at the core ability range (rel=0.929) [SIMULATION]
- The blueprint is consistent with MAP's published 40–43 structure (14/13/13 TimeBack operational split, disclosed) [AUTHORING-DECISION; NWEA-VERIFIED for 40–43]
- Items have passed a 14-dimension quality gate [AUTHORING-DECISION]

### Mitigation
Same as Limitation 3: concurrent validity study. Target: r ≥ 0.80, mean difference < 5 RIT, 95% LoA < ±8 RIT — with RIT unlock core-band-first (see the Concurrent Validity Plan tab, §5).

---

## Limitation 5: G2 Items Pending Deeper Validation

### Statement
Grade 2 items (161–180 band) have the fewest items in the bank (51 items in the 161–170 band, 45 in 171–180) and the least validated b_provisional values. G2 vocabulary standards L.2.4 and L.2.5 each have only 3 items after gap fixes. Some G2 match/sequence items underwent limited quality-check validation during a quality-check service outage in June 2026.

### Practical impact
G2 students at or below the 50th percentile (RIT < 170) may receive less accurate ability estimates due to bank thinness in that region. The reliable range identified in Simulation 6 begins at RIT 181 — below this, reliability degrades toward 0.85 [SIMULATION]. G2 students at the 8th–25th percentile may receive scores that are directionally correct but less precise.

### Mitigation
The floor expansion is now **merged** (+92 edge items, PR #30 — floor to ~RIT 155), harness-validated and pending calibration/adoption into the operational bank; the v3 reliable floor of RIT 181 will be re-characterized once adopted. Students below RIT 155 route to the official K–2 MAP instrument — an explicit boundary, not a stretched proxy. Tail-band calibration is protected by the pre-committed tail coverage plan: the ~40-student pilot deliberately includes both tails, and the ≥150-responses-per-tail-band-item target attaches to the calibration stage that accrues from regular use (the Concurrent Validity Plan tab, §2.2). All G2 items generated during the outage window should be re-validated once the quality-check service is restored.

---

## Limitation 6: Simulation Assumes Rasch Model Is Correctly Specified

### Statement
All simulations assume the Rasch 1PL model correctly describes student-item interactions. Real student responses may exhibit:
- **Item discrimination variability:** Some items are better discriminators than others (i.e., the 2PL model with discrimination parameter a might be more accurate)
- **Guessing behavior:** On hard MCQ items, students may guess — the Rasch model assigns P > 0 even for very low-ability students, but the actual P floor is 0.25 for 4-option MCQ
- **Multidimensionality:** Reading comprehension may involve multiple correlated dimensions (vocabulary, inference, text structure), violating the Rasch model's unidimensionality assumption
- **Fatigue:** Later items may be systematically harder due to test-taker fatigue — not modeled

### Practical impact
If the Rasch model is misspecified, all simulation results — including the r=0.963 theta recovery and rel=0.929 reliability — overestimate actual field performance. The standard Rasch model fit indices (INFIT mean square 0.70–1.30; OUTFIT < 2.0; pt-biserial > 0.20) will identify items where the misspecification is worst, after the field trial. NWEA uses the Rasch model because it has been empirically validated for MAP's item types [NWEA-2025-TR] — this provides reasonable prior evidence that the model is appropriate.

### Mitigation
Post-field-trial item fit analysis. Items failing Rasch fit statistics are retired. Confirmatory factor analysis on pilot data to test the unidimensionality assumption. NWEA's documented use of Rasch provides model validity precedent [NWEA-2025-TR]. The guessing concern is partially addressed by MSQ and EBSR items (lower guess-rate than MCQ); MCQ items have a 25% guess floor that the Rasch model will underestimate for very low-ability students.

---

## Limitation 7: Small Bank vs. NWEA's 40,000+ Item Pool

### Statement
The Incept bank contains 650 items; NWEA's operational pool contains 40,000+ items [NWEA-2025-TR]. NWEA's larger pool enables:
- Tighter item security (any individual item sees far fewer exposures)
- Greater adaptive precision (more choices near any student's exact ability level)
- Differential Item Functioning (DIF) screening across demographic groups
- More nuanced content coverage (many more items per standard, per grade, per Lexile level)

### Practical impact
With 650 operational items (v3 run, 2026-07-03):
- 38/650 items (5.8%) exceed the 30% exposure rate [SIMULATION] — higher than NWEA's operational target; max item exposure 91%
- 241 items were never used in the v3 run (v1: 322; initial G3-scoped run: 246) — randomesque top-5 selection in both selection phases recovered ~80 items, but utilization remains concentrated
- The v1 deterministic-first-passage finding is **fixed** by randomesque selection; two easy-band cells (`literary/171-180`, `informational/171-180`) remain never-served — b-band-aware passage scoring is the queued follow-up
- Item security is weaker: students who take the test multiple times will see repeated items (mean pairwise between-session overlap 29.4%)
- Fine-grained within-standard discrimination (e.g., distinguishing RL.3.2 at RIT 185 vs. 193) is limited by items per cell

This does not make the test invalid, but it limits the product's claims relative to the full MAP.

### Mitigation
Bank expansion is the long-term solution — the staged sets already raise the harness-loadable pool to 766 items (the Item Bank tab, §2.1). Near-term mitigations shipped: randomesque selection, the topic-cap constraint (no topic_tag repeats within a session), and the Lexile-band filter. Exposure-aware scoring is the open engineering follow-up; post-pilot Sympson-Hetter exposure control [ACADEMIC; Sympson-Hetter-1983] will impose hard item-level caps, and a per-standard session cap (max 2 items/standard) is proposed in PR #35. Target bank size for operational security: 800–1,000 items (20–25× the test length [Stocking-1994]).

---

## Limitation 8: Simulation Scope

### Statement
The six Monte Carlo simulations were run on a Grade-3-configured 630-item bank (the bank as of the simulation date), with true ability drawn from a G3 fall prior N(−1.5, 1.0), and used a closed-form Fisher-information selector rather than the full production shadow-test path [SIMULATION].

### Practical impact
The initial-run results (r=0.948, rel=0.928, RMSE=4.12 RIT) could not expose production-path effects: the v1 production re-run (2026-07-02) surfaced an RMSE regression (4.73) and a +2.62 RIT bias in the Owen running estimate; the v2/v3 runs root-caused and resolved both (see Limitation 2).

### Mitigation
**Complete.** The validation now runs the engine's real selection code end-to-end under the TimeBack-parity configuration: v3 (2026-07-03) — production `select_next()` with randomesque exposure control, all 650 items, G2–G5 prior, ~17,900 sessions, seven studies (the v3 validation report in the engine repository — authoritative throughout this package; the v1/v2 reports retained as historical records). The remaining follow-up is the residual 175–190-band bias decomposition (Limitation 2).

---

## Summary: Known vs. Unknown

| Question | Status | When answered |
|---|---|---|
| Does the algorithm rank students correctly? | **Known** (r=0.963, v3 production path) | Simulation 1, v3 [SIMULATION] |
| Is the test reliable at core ability range? | **Known** (rel=0.929) | Simulation 2, v3 [SIMULATION] |
| Why did v1 scores overestimate by +2.6 RIT? | **Known — resolved** (Owen running-estimate prior shrinkage; final score re-based on shipped MLEF; v3 bias −0.38) | v2 root-cause analysis [SIMULATION] |
| Why do the 175–190 bands read −0.4 to −1.0 RIT low? | **Unknown — follow-up** | Scorer-only decomposition (S12, queued) |
| Are items content-valid (CCSS-aligned)? | **Likely** (14-dimension quality-check gate) | Field trial will confirm |
| What are each item's true difficulty parameters? | **Unknown** (b_provisional only) | After N=1,000 field trial |
| Does score X on our test equal score X on MAP? | **Unknown** | After concurrent validity study |
| Which EBSR scoring rule links better? | **Pre-committed procedure** (dual-scoring; decision statistic fixed) | Before Stage-3 RIT unlock |
| Is the test free from demographic bias (DIF)? | **Unknown** | After N=5,000 with diverse sample |
| Are domain sub-scores reliable (≥0.80)? | **Likely** (13–14 items/domain) | Field trial will confirm |
| Is the Rasch model correctly specified? | **Assumed** (NWEA precedent) | Item fit analysis post-pilot |

---

## Sources

- [Wright-Stone-1979] Wright, B. D., & Stone, M. H. (1979). *Best test design*. MESA Press.
- [Linacre-1994] Linacre, J. M. (1994). Sample size and item calibration stability. *Rasch Measurement Transactions, 7*(4), 328.
- [NWEA-2025-TR] NWEA. (2026). *MAP Growth Technical Report for 2024–2025*. NWEA/HMH.
- [Kolen-Brennan-2014] Kolen, M. J., & Brennan, R. L. (2014). *Test equating, scaling, and linking* (3rd ed.). Springer.
- [AERA-2014] American Educational Research Association, American Psychological Association, & National Council on Measurement in Education. (2014). *Standards for educational and psychological testing*. AERA.
- [Stocking-1994] Stocking, M. L. (1994). *Three practical issues for modern adaptive testing item pools*. ETS Research Report RR-94-5.
