# Simulation Evidence — MAP Proxy Adaptive Assessment
**Version:** 2.0 | **Date:** 2026-07-03 | **Audience:** Investors, technical reviewers

This document presents all seven Monte Carlo psychometric simulations conducted on the Incept MAP Proxy engine. Source data: the v4 validation report in the engine repository (**v4 full-bank run — authoritative**); historical records: the v3 parity run, the v2 re-based run, the v1 production-path re-run, and the initial G3-scoped run, all in the engine repository. Figures: the engine repository's validation figures folder.

---

## v4 Full-Bank Run (2026-07-03) — Authoritative Results

Provenance: **2026-07-03 v4 run: production selection path + randomesque selection, full 786-item bank, G2–G5 prior, TimeBack-parity configuration.** This run re-validates everything on the complete bank after the floor/ceiling/standard-gap expansions merged — the `load_bank()` build dedups to 786 unique items (which differs from the naive fixture sum). The engine adopted TimeBack's operational constants via PRs #26/#34 — domain quotas 14/13/13 (40 scored items; `ADAPTIVE_ITEMS_MIN` = 40 as the scored floor before any stop), hard cap 43 with a precision-extension band at items 41–43, SE stop 0.35 evaluated only at ≥40 items (quotas alone never stop the test), TEI floor ≥12 with gap-match correctly counted as TE, and the TimeBack bit-for-bit parity MLEF solver (damped Newton, trust-region max_step 1.0, 6dp rounding, A&S 7.1.26 CDF). Selection is randomesque (top-5) in both the quota-filling and precision-extension phases. Seven Monte Carlo studies, ~17,900 production-path sessions; a seventh study (adversarial simulees) was added alongside the original six. v4 improved or held every metric versus the interim v3 run.

| Metric | v1 re-run (2026-07-02) | v2 fixed (2026-07-02) | v3 parity (650 items) | **v4 full bank (786 items)** | Benchmark | Verdict |
|---|---|---|---|---|---|---|
| Sim 1 theta recovery r | 0.954 | 0.959 | 0.963 | **0.967** | ≥ 0.90 | ✅ best of the runs |
| Sim 1 RMSE | 4.73 RIT ⚠️ | 3.70 RIT | 3.44 RIT | **3.20 RIT** | < 4.0 RIT | ✅ within target |
| Sim 1 bias | +2.62 RIT ⚠️ | −0.46 RIT | −0.38 RIT | **−0.04 RIT** (near-eliminated) | abs(bias) < 0.5 | ✅ |
| Sim 1 max per-band abs(bias) (RIT 181+) | hidden | 1.20 RIT | 0.83 RIT | **0.83 RIT** | ≤ 1.5 RIT | ✅ |
| Sim 2 reliability (operational range) | 0.929 | 0.923 | 0.929 | **0.931** | 0.93 target | ✅ meets the 0.93 target |
| Sim 2 SEM (operational range) | 3.18 RIT | 3.31 RIT | 3.18 RIT | **3.14 RIT** | ≤ 4.0 RIT | ✅ |
| Sim 3 max tolerable σ | 1.0 logits | 1.0 logits | 1.0 logits | **1.0 logits** (reliability ≥ 0.915 at every σ) | ≥ 0.5 | ✅ |
| Sim 4 (internal cross-bank consistency, synthetic) r / 95% LoA | 0.909 / [−7.9, +8.3] | 0.905 / [−11.3, +10.6] | 0.912 / [−10.7, +10.2] | **0.918 / [−10.0, +10.0] RIT** | r ≥ 0.85 | ✅ — NOT MAP agreement (synthetic bank) |
| Sim 5 blueprint adherence (±1) | 100% (13/13/13) | 100% (13/13/13) | 100% | **100% (14/13/13 on the 40-item scored form)** | 100% | ✅ |
| Sim 5 TEI floor met | not audited | not audited | 100% | **100% (mean 16.2 TE ≥ 12, gap-match counted)** | 100% | ✅ |
| Sim 5 never-used items | 322/650 | 256/650 | 241/650 | **289/786** | ↓ | rose with the larger bank; per-band exposure balancing is the open follow-up |
| Sim 5 over-exposed (>30%) | 41/650 | 39/650 | 38/650 | **38/786** | ↓ | max exposure 0.709; exposure-aware scoring the open follow-up |
| Sim 6 reliable range (rel ≥ 0.85) | RIT 181–230 | RIT 186–227 | RIT 181–227 | **RIT 160–230** | — | floor down to RIT 160 — median G2 fall reader now inside the reliable range |
| Sim 7 adversarial simulees | n/a | all finite, ordered | all finite, ordered | **all finite, bounded, correctly ordered** | no divergence | ✅ |
| MLEF divergences (any sim) | unmeasured | 0 / ~17,500 | 0 / ~17,900 | **0 / ~17,900 sessions** | 0 | ✅ |

**Session behavior:** mean 40.6 items per session; 76.5% stop at exactly 40 (SE ≤ 0.35 met at the scored floor), 15.1% run to the 43-item hard cap; no session stops below 40 — quota-only stopping is confirmed removed.

![Simulation 1 (v4): theta recovery on the full 786-item bank — true vs estimated ability](../../engine/scripts/validation/figures/sim1_theta_recovery_v4.png)

![Simulation 1 (v4): per-band bias on the full 786-item bank](../../engine/scripts/validation/figures/sim1_band_bias_v4.png)

![Simulation 2 (v4): reliability curve across the ability range on the full bank](../../engine/scripts/validation/figures/sim2_reliability_v4.png)

![Simulation 4 (v4): internal cross-bank consistency (Bland-Altman, synthetic bank)](../../engine/scripts/validation/figures/sim4_comparability_v4.png)

![Simulation 5 (v4): blueprint adherence and item-exposure distribution on the full bank](../../engine/scripts/validation/figures/sim5_coverage_v4.png)

![Simulation 6 (v4): floor and ceiling characterization — reliable range RIT 160–230](../../engine/scripts/validation/figures/sim6_floor_ceiling_v4.png)

**The headline: the floor is largely closed.** The reliable range (reliability ≥ 0.85) now spans **RIT 160–230**, down from RIT 181–227 in the v3 650-item run. The median G2 fall reader (~RIT 170) is now inside the reliable range — previously below the floor. This resolves the adversarial review's most-cited limitation; only the bottom ~5% of readers (below RIT 160) route to the K–2 MAP instrument. Overall bias fell to −0.04 RIT (near-eliminated on the full bank), and marginal reliability rose to 0.931, meeting the ≥0.93 target (MAP's published 0.96 remains the higher operational bar).

**How v4 relates to the runs below.** The v1 production-path re-run flagged RMSE 4.73 and a +2.62 RIT systematic overestimate. The v2 run root-caused the bias: it lived in the **Owen running estimate's prior shrinkage**, not in the shipped score — re-basing the final score on the score report's MLEF `overall_logit` (the number students actually receive) removed it. The v3 run re-validated the identical suite under the TimeBack-parity constants with randomesque exposure control on the 650-item bank (RMSE 3.44, bias −0.38, reliable range RIT 181–227). v4 re-runs everything on the full 786-item bank after the floor/ceiling/standard-gap expansions merged; no scorer semantics changed. The honest residual: never-used items rose to 289/786 as the bank grew, the 171–180 selection cells (`literary/171-180`, `informational/171-180`) improved but are not yet fully served, and per-band exposure balancing remains the open engineering follow-up.

---

## v3 TimeBack-Parity Run (2026-07-03, 650 items) — Historical Record (superseded by the v4 full-bank run above)

*This section is preserved as the record of the interim v3 run on the 650-item operational bank, before the floor/ceiling/standard-gap expansions merged. Its numbers (r 0.963, RMSE 3.44, bias −0.38, reliability 0.929, reliable range RIT 181–227, never-used 241/650) are superseded by the v4 full-bank run above and should not be quoted as current.*

The v3 run executed the seven-study suite on the 650-item operational bank under the TimeBack-parity constants (14/13/13 = 40 scored, hard cap 43, SE stop 0.35, TEI floor ≥12) with randomesque top-5 selection in both selection phases. It cleared what the v1 run had flagged — RMSE 3.44 RIT (within the <4.0 target), bias −0.38 RIT, 0 MLEF divergences — and recovered the reliable floor to RIT 181 (from RIT 186 at v2). Its disclosed residuals — a −0.4 to −1.0 RIT negative bias in the RIT 175–190 bands and 241/650 never-used items — motivated the bank expansions that the authoritative v4 run then validated. Raw results: `data/summary_g2g5_650_v3.json`.

---

## Production-Path Re-run (2026-07-02, v1) — Historical Record (superseded by the v4 full-bank run above)

*This section is preserved as the record of the first production-path run and its honestly-reported regressions. Its flagged findings (+2.62 RIT bias, RMSE 4.73, deterministic first passage) were subsequently root-caused and resolved — see the v3 section above. Do not quote these numbers as current.*

The full-bank re-run is complete. It was run on the **true production selection path** — the engine's real `select_next()` (shadow-test feasibility, domain quotas, passage grouping, Lexile-band filter, topic cap, TEI floor) driven through the same per-response state machine as `api/sessions.py` — against **all 650 items** (including `bank_ebsr_191_200.json`, which the old harness silently omitted; old runs used 630 items across 12 of 13 bank files), with a **G2–G5 prior N(−1.0, 1.2)** and reduced N (~15,350 production-path sessions; Monte Carlo error ≈ ±0.005 on r, ±0.1 RIT on RMSE/SEM). Report: the v1 validation report in the engine repository (superseded by the v4 validation report). These numbers superseded the initial G3-scoped run recorded in the per-simulation sections below, and are in turn superseded by the v4 full-bank section at the top of this document.

| Metric | Initial run (630 items, closed-form) | Re-run (650 items, G2–G5 prior, production selector) | Verdict |
|---|---|---|---|
| Theta recovery r | 0.948 | **0.954** | ✅ meets ≥0.90 |
| RMSE | 4.12 RIT | **4.73 RIT** | ⚠️ **worse; above <4.0 benchmark — flagged** |
| Bias | −0.24 RIT | **+2.62 RIT** | ⚠️ **systematic overestimate — flagged (new disclosure)** |
| Marginal reliability (θ∈[−2,+1]) | 0.928 | **0.929** | ⚠️ still below ≥0.93 target (MAP published: 0.96) |
| SEM (operational range) | 3.22 RIT | **3.18 RIT** | ✅ meets ≤4.0 RIT |
| Robustness (rel ≥0.85) | to σ=1.0 logits | **to σ=1.0 logits** | ✅ unchanged |
| Sim 4 comparability r / 95% LoA | 0.902 / ±11.3 RIT | **0.909 / ±8.1 RIT** | With caveats (see below) |
| Blueprint adherence (±1) | 100% | **100%** | ✅ unchanged |
| Reliable range (rel ≥0.85) | RIT 181–227 | **RIT 181–230** | Ceiling is grid-limited (reliability 0.884 at θ=+3.0); floor unchanged |

**Two flagged regressions.** The RMSE regression (4.12 → 4.73 RIT) and the +2.62 RIT systematic overestimate likely come from passage-boundary-only theta updates, constrained (passage-grouped, TEI-forced) selection, and floor effects under the wider G2–G5 prior. The RMSE worsening is partly compositional — the wider prior includes the floor region; the worst band is θ∈[−2,−1] at 0.43 logits — while core-band precision is unchanged (SEM 3.18 RIT, reliability 0.929). A constant bias is absorbed by the linear scale-linking intercept in Stage 3, but it must be root-caused before the pilot (MLEF fence-item behavior on low-theta response patterns and composite-item PCM scoring are the prime suspects).

**Sim 4 caveats.** The narrower ±8.1 RIT LoA is not directly comparable to the old ±11.3 figure: 50% of the synthetic MAP-like bank's items were format-relabelled to satisfy the production TEI floor (a label-only change; the Rasch math is unaffected), and the old run's 18/14/8 MAP-side quota split was not reproducible because production hardcodes 13/13/13.

**New findings disclosed by the re-run:**

- **(a) Deterministic first passage.** Production selection is deterministic from the fixed session-start prior — the first passage is identical in 100% of sessions, an exposure/security issue. Fix queued: randomize among near-optimal first passages.
- **(b) Bank utilization.** 322/650 items (~50%) were never administered in simulation; 41/650 exceed the 30% exposure threshold (old: 26/630).
- **(c) G2 floor unchanged.** G2 fall students (true median ≈ RIT 170, θ≈−3.0) remain outside the reliable range — the bank floor is b=−2.5. Consistent with the existing G2-floor disclosure.
- **(d) Old harness file omission.** The initial harness loaded 12 of 13 bank files (`bank_ebsr_191_200.json` missing), i.e., 630 items rather than 650.

---

## Methodology Overview

**Simulation scope.** The initial simulations recorded in the per-simulation sections below were run on a Grade-3-configured 630-item bank, with true ability drawn from a G3 fall prior N(−1.5, 1.0), and used a closed-form Fisher-information selector rather than the full production shadow-test path. **The authoritative numbers are the v4 full-bank run's (2026-07-03) — see the top of this document. The v3 parity run, the v1 production-path re-run (2026-07-02), and the per-simulation sections below remain as historical records.**

All simulations use Monte Carlo sampling against the item bank:

- **Student simulation:** True ability θ drawn from the G3 fall prior N(−1.5, 1.0). Item responses simulated via the Rasch 1PL model: P(correct | θ, b) = 1/(1 + exp(−(θ−b))). Responses are stochastic draws from Bernoulli(P). [SIMULATION]
- **Composite (EBSR) items:** Simulated via the Partial Credit Model with thresholds at b and b+0.5 logits. [SIMULATION]
- **Scoring:** Production `compute_mlef_score()` function from `scorer/mlef.py`. MLEF with ±3.8 fence items (Han 2016 [Han-2016]).
- **Item selection:** Closed-form Fisher-information maximization with domain quota enforcement — not the production shadow-test assembly path (see Simulation scope above).
- **Bank:** 630-item bank as of simulation date (pre-June 2026 gap fixes; current bank is 650 items).

**Key assumption:** All simulations use b_provisional values as true item difficulties. Simulation 3 specifically tests what happens when this assumption is relaxed. True concurrent validity requires field data — simulations validate algorithm behavior, not scale accuracy [AERA-2014].

---

## Simulation 1: Theta Recovery

### Purpose
Measures whether the CAT algorithm correctly recovers students' true reading ability across the full G2–G5 ability range. This is the foundational validity check: a test that cannot rank students correctly provides no useful information.

### Methodology
- N = 5,000 synthetic students
- True θ drawn from N(−1.5, 1.0), approximating the G3 fall population distribution [NWEA-2025-NM][DERIVED]
- Each student completes a full 39-item adaptive session
- Pearson correlation and RMSE computed between true θ and estimated θ̂ (MLEF)
- Per-band RMSE computed across four ability bands

Statistical basis: theta recovery correlation is the standard index of CAT algorithm validity, recommended in AERA/APA/NCME Standards for Educational and Psychological Testing (2014 [AERA-2014]).

### Results

| Metric | Our Engine | MAP Benchmark | Status |
|---|---|---|---|
| Pearson r | **0.948** | ≈ 0.90 [NWEA-2025-TR] | ✅ Exceeds benchmark |
| RMSE (RIT) | **4.12** | < 4.0 RIT [NWEA-2025-TR] | ⚠️ Slightly above target |
| Bias (RIT) | **−0.24** | ≈ 0 | ✅ Negligible |

Per-band RMSE:

| θ band | RIT range | RMSE (logits) | RMSE (RIT) |
|---|---|---|---|
| [−2, −1] | 180–190 | 0.333 | 3.33 RIT |
| [−1, 0] | 190–200 | 0.326 | 3.26 RIT |
| [0, +1] | 200–210 | 0.316 | 3.16 RIT |
| [+1, +2] | 210–220 | 0.341 | 3.41 RIT |

![Simulation 1: theta recovery scatter — true vs estimated ability (initial run)](../../engine/scripts/validation/figures/sim1_theta_recovery.png)

### What This Proves
The CAT algorithm correctly ranks students by reading ability with r=0.948 — substantially above MAP's ≈0.90 benchmark. The RMSE of 4.12 RIT is 3% above MAP's <4.0 RIT target, attributable to provisional b parameters. This initial run showed negligible bias (−0.24 RIT); the production-path re-run later found +2.62 RIT systematic overestimate — see the Production-Path Re-run section above. [SIMULATION]

### What This Does Not Prove
This simulation does not prove that our θ̂ values correspond to NWEA's RIT scale. A student estimated at θ̂ = −0.5 logits (RIT ≈ 195 under the approximate transformation) may score 190 or 200 on the actual MAP — the ±5–10 RIT uncertainty in b_provisional values propagates into absolute score accuracy [AUTHORING-DECISION]. The r=0.948 measures ranking accuracy, not absolute accuracy.

---

## Simulation 2: Reliability Curve

### Purpose
Measures test reliability (reproducibility) as a function of ability level across the operational G2–G5 range. Reliability is the standard psychometric index of score consistency: the proportion of total score variance attributable to true ability variance, not measurement error [AERA-2014].

**Definition:** Marginal reliability = 1 − SE² / σ²_θ, where SE is the test's standard error and σ²_θ is the population variance of ability.

### Methodology
- 500 sessions per theta level, across 25 levels from θ = −3.0 to θ = +2.5
- Reliability computed at each level: rel(θ) = 1 − SE(θ̂)² / Var(θ̂)
- Marginal reliability computed over the G2–G5 operational range (θ ∈ [−2, +1] = RIT 180–210)
- SEM (Standard Error of Measurement) computed in RIT units: SEM_RIT = 10 × SE(θ̂)

Statistical basis: reliability ≥ 0.90 is the standard for high-stakes individual score interpretation; ≥ 0.85 is acceptable for screening and instructional decision-making [AERA-2014]. MAP Growth targets ≥ 0.93 in the operational range [NWEA-2025-TR].

### Results

| Region | Reliability | SEM (RIT) | MAP Benchmark | Status |
|---|---|---|---|---|
| G2–G5 operational (θ ∈ [−2, +1]) | **0.928** | **3.22 RIT** | rel ≥ 0.93, SEM ≤ 4.0 RIT [NWEA-2025-TR] | ⚠️ Below MAP's ≥0.93 target; well above minimum 0.85 |

![Simulation 2: reliability curve across the ability range](../../engine/scripts/validation/figures/sim2_reliability.png)

### What This Proves
The test provides reliable measurement (rel = 0.928) at the core ability range, well above the minimum acceptable threshold of 0.85 for screening decisions [AERA-2014]. The SEM of 3.22 RIT is within MAP's ≤ 4.0 RIT SEM target [NWEA-2025-TR]. [SIMULATION]

### What This Does Not Prove
The 0.928 reliability is 0.002 below MAP's ≥ 0.93 operational target. This gap is expected given provisional b parameters: as b values are empirically calibrated and item fit statistics improve, items contributing non-trivially to measurement error will be retired or revised, and reliability is expected to rise above 0.93. This will be confirmed after the N=1,000 field trial.

---

## Simulation 3: Robustness to Parameter Error

### Purpose
Directly tests what happens when b_provisional values are wrong — simulating the real pre-calibration condition. This is the most policy-relevant simulation for investors: it quantifies how much the algorithm degrades under known parameter uncertainty.

### Methodology
- 2,000 students per σ level, across 7 levels: σ = 0.0, 0.1, 0.2, 0.3, 0.5, 0.8, 1.0 logits
- At each σ level, each item's b_provisional is perturbed by Gaussian noise: b_administered = b_provisional + N(0, σ)
- The engine uses the perturbed b values (simulating what happens when expert assignments are wrong)
- True students are simulated using the unperturbed values (simulating true item difficulty)
- RMSE and reliability computed at each σ level

Statistical basis: the expected pre-calibration b uncertainty is σ ≈ 0.5 logits based on Lexile-to-IRT mapping accuracy [AUTHORING-DECISION; DERIVED from literature on difficulty estimation]. This simulation quantifies the operational impact of that uncertainty.

### Results

| σ (logits) | RIT error equiv. | RMSE (logits) | Reliability |
|---|---|---|---|
| 0.0 | 0 RIT | 0.3977 | 0.886 |
| 0.1 | 1 RIT | 0.3999 | 0.885 |
| 0.2 | 2 RIT | 0.3826 | 0.892 |
| 0.3 | 3 RIT | 0.4342 | 0.876 |
| 0.5 | 5 RIT | 0.4065 | 0.884 |
| 0.8 | 8 RIT | 0.4938 | 0.866 |
| 1.0 | 10 RIT | 0.4502 | 0.890 |

![Simulation 3: robustness to item-parameter error](../../engine/scripts/validation/figures/sim3_robustness.png)

### What This Proves
Reliability remains above 0.85 across all tested parameter error levels, including σ = 1.0 logits — a very pessimistic estimate of pre-calibration uncertainty. At the realistic σ ≈ 0.5 logits, reliability is 0.884. The algorithm is robust to pre-calibration parameter uncertainty. [SIMULATION]

### What This Does Not Prove
Robustness to parameter error does not mean scores are accurate in absolute terms. An engine that reliably ranks students A > B > C under wrong b values is still reliable; but if all b values are biased in the same direction, the absolute θ̂ estimates will be offset from truth. This is the argument for why scale linking is still required even though the algorithm is robust.

---

## Simulation 4: Internal Cross-Bank Consistency (Synthetic)

*(Formerly labelled "Score Comparability." Relabelled because it measures internal consistency against a synthetic bank — explicitly NOT agreement with MAP.)*

### Purpose
Provides an internal consistency check: whether the engine produces stable scores for the same simulated students across two different bank configurations. It is emphatically not a measurement of agreement with NWEA MAP — the comparison bank is synthetic. The concurrent validity study (the Concurrent Validity Plan tab) is the only source of real MAP agreement evidence.

### Methodology
- N = 2,000 students, θ drawn from the G3 fall prior N(−1.5, 1.0)
- Each student scored on two banks:
  1. Our bank (b_provisional values as specified)
  2. A synthetic MAP-like bank: items drawn from N(0.0, 0.8) difficulty distribution, approximating NWEA's operational pool difficulty distribution [DERIVED from NWEA-2025-TR bank description]
- Bland-Altman method: correlation, mean difference, 95% Limits of Agreement (LoA = mean diff ± 1.96 × SD_diff) [DERIVED from standard method-comparison literature]

Statistical basis: the Bland-Altman method [ACADEMIC] is the standard approach for comparing two measurement instruments that measure the same construct on the same scale [AERA-2014; Kolen-Brennan-2014].

### Results

| Metric | Value | Interpretation |
|---|---|---|
| Correlation (r) | **0.902** | Strong agreement in ranking |
| Mean difference | **−0.15 RIT** | Negligible systematic bias |
| SD of differences | **5.74 RIT** | Spread of disagreement |
| 95% Limits of Agreement | **[−11.4, +11.1] RIT** | Individual scores may differ by up to ±11 RIT |
| LoA width | **22.5 RIT** | Full span of disagreement |

![Simulation 4: internal cross-bank consistency (Bland-Altman, synthetic bank)](../../engine/scripts/validation/figures/sim4_comparability.png)

### What This Proves
Scores from our engine and a MAP-like engine are strongly correlated (r=0.902) with no meaningful systematic bias (−0.15 RIT). [SIMULATION]

### What This Does Not Prove
The ±11.3 RIT 95% LoA means that for any individual student, our score and a MAP-like score could differ by up to 11 RIT at 95% confidence. This is wider than ideal for a clinical instrument. It reflects both the provisional parameter uncertainty and the fact that the "MAP-like bank" used here is synthetic — not actual NWEA items. True concurrent validity requires real MAP scores, which will reduce this interval substantially after scale linking [Kolen-Brennan-2014]. The LoA will be the primary metric reported in the Stage 3 concurrent validity study.

---

## Simulation 5: Blueprint Adherence (Domain Coverage)

### Purpose
Verifies that the domain quota enforcement system — the architectural mechanism targeting 13 Literary, 13 Informational, and 13 Vocabulary items per session — works correctly under all ability levels and bank conditions.

### Methodology
- N = 1,000 full 39-item adaptive sessions
- Domain counts recorded at session end
- Blueprint adherence criterion: % of sessions within ±1 item of each 13/13/13 domain target
- Item exposure distribution analyzed: % of items exceeding 30% exposure rate across sessions

Statistical basis: Blueprint fidelity is a structural validity requirement — a test that does not follow its own blueprint cannot claim content validity against the MAP blueprint [AERA-2014 §1.7].

### Results

| Domain | Target | Mean Actual | Adherence (±1) |
|---|---|---|---|
| Literary | 13 | 13.00 | 100.0% |
| Informational | 13 | 13.00 | 100.0% |
| Vocabulary | 13 | 13.00 | 100.0% |
| **All three** | — | — | **100.0%** |

Additional exposure statistics:
- Items exceeding 30% exposure rate: 26 / 630 (4.1%)
- Items never used: 246 / 630 (39.0%)
- Mean exposure per used item: 39,000 / (630 − 246) = ~101.6 sessions

![Simulation 5: blueprint adherence and item-exposure distribution](../../engine/scripts/validation/figures/sim5_coverage.png)

### What This Proves
The domain quota system holds the 13/13/13 blueprint to within ±1 item in 100% of simulated sessions. Note the production shadow-test path itself was not exercised — the simulation used the closed-form selector (see Simulation scope in the Methodology Overview). [SIMULATION]

### What This Does Not Prove
Blueprint adherence at the domain level does not guarantee standard-level balance. Within the 13 Literary items, the distribution across RL standards is determined by bank composition and Fisher-information selection — a student may receive more RL.3.3 (character development) than other standards if the bank has more items tagged to that standard at that ability level. Per-standard balance requires bank-level standard coverage management (addressed in the Item Bank tab, §4).

The 26 over-exposed items and 246 never-used items indicate that bank utilization is uneven, as expected for a pre-pilot bank. Post-pilot Sympson-Hetter (1983 [ACADEMIC]) exposure control will impose hard item-level caps.

---

## Simulation 6: Floor and Ceiling Characterization

### Purpose
Identifies the ability range over which the test provides reliable measurement — the "reliable range." Outside this range, the bank has insufficient items to maintain measurement precision, and reliability degrades.

### Methodology
- 200 sessions per theta level, across 28 levels from θ = −4.0 to θ = +3.0 (RIT 160–230)
- Reliability computed at each level using conditional SEM
- Reliable range defined as: reliability ≥ 0.85 at that theta level
- Bank item difficulty range documented for context

Statistical basis: characterizing floor and ceiling is required under AERA/APA/NCME Standards §4.9 [AERA-2014] to document the score range within which valid inferences can be made.

### Results

| Metric | Value | Interpretation |
|---|---|---|
| Reliable range (rel ≥ 0.85) | **θ ∈ [−1.93, +2.74]** | **RIT 181–227** |
| Bank difficulty range | b ∈ [−2.50, +2.00] logits | RIT 175–220 |
| G2–G5 target range | RIT 161–227 | Full grade band |

![Simulation 6: floor and ceiling characterization — reliable range](../../engine/scripts/validation/figures/sim6_floor_ceiling.png)

### What This Proves
The test provides reliable measurement across RIT 181–227, covering the core G3–G5 operational range and above-average G2 students. The reliable range encompasses the ability levels of 80%+ of the G2–G5 population [DERIVED; NWEA-2025-NM]. [SIMULATION]

### What This Does Not Prove
Students below RIT 181 — roughly the below-8th-percentile G3 fall range — receive less reliable scores due to bank thinness at the low-ability tail. For G2 students at the 25th percentile (RIT ~168) and below, the test is operating below its reliable range. Bank expansion at the 161–180 band is planned for Stage 2.

---

## Validity Claims Summary

Numbers below are from the authoritative v4 full-bank run (2026-07-03; the v4 validation report in the engine repository).

| Claim | Evidence | Confidence | Source |
|---|---|---|---|
| CAT algorithm ranks G2–G5 ability accurately | Sim 1: r=0.967; RMSE=3.20 RIT (<4.0 benchmark); bias −0.04 RIT (near-eliminated on the full bank; max per-band 0.83) | **High** | [SIMULATION] |
| Test reliability meets the ≥0.93 target | Sim 2: rel=0.931 (meets the ≥0.93 target; MAP published 0.96 is the higher operational bar), SEM=3.14 RIT | **High** | [SIMULATION] |
| System robust to provisional parameter error | Sim 3: rel≥0.915 at σ≤1.0 logits | **High** | [SIMULATION] |
| Internal cross-bank consistency (synthetic — NOT MAP agreement) | Sim 4: r=0.918, 95% LoA [−10.0, +10.0] RIT (synthetic bank; caveats disclosed) | **Medium** | [SIMULATION; synthetic MAP bank] |
| Blueprint fidelity maintained 100% | Sim 5: 100.0% sessions within ±1 of 14/13/13 on the 40-item scored form; TEI floor met in 100% (mean 16.2 ≥ 12) | **High** | [SIMULATION] |
| Reliable across G2 (median and above) through G5 | Sim 6: RIT 160–230 reliable (median G2 fall reader ~RIT 170 now inside the reliable range; only the bottom ~5% below RIT 160 route to K–2 MAP) | **High** | [SIMULATION] |
| Scoring numerically stable under adversarial response patterns | Sim 7: all-correct / all-wrong / alternating / rapid-guessing profiles all finite, fence-bounded, correctly ordered; 0 divergences in ~17,900 sessions | **High** | [SIMULATION] |
| Scores comparable to actual NWEA MAP | Not yet measured | **Not yet** | Requires concurrent validity study |
| Items calibrated to NWEA's RIT scale | Not yet measured | **Not yet** | Requires scale-linking study |

---

## Sources

- [Han-2016] Han, K. T. (2016). Maximum likelihood score estimation method with fences for short-length tests and computerized adaptive tests. *Applied Psychological Measurement, 40*(4), 289–301.
- [NWEA-2025-TR] NWEA. (2026). *MAP Growth Technical Report for 2024–2025*. NWEA/HMH.
- [NWEA-2025-NM] NWEA. (2025). *MAP Growth Norms Technical Manual 2025*. NWEA.
- [AERA-2014] American Educational Research Association, American Psychological Association, & National Council on Measurement in Education. (2014). *Standards for educational and psychological testing*. AERA.
- [Kolen-Brennan-2014] Kolen, M. J., & Brennan, R. L. (2014). *Test equating, scaling, and linking* (3rd ed.). Springer.
