# Case for Approval

# Incept MAP Proxy — Grades 2–5 Reading

## Assessment bundle & case for approval

Product: Incept MAP Proxy Adaptive Assessment — Grades 2–5 Reading · **map-proxy-assessment**
Target reference test: NWEA MAP Growth — Reading 2–5
Prepared for: the Alpha growth-program approver
Date: July 3, 2026
A note on evidence. Every number in this document is drawn from one of five sources, and nothing is asserted beyond them:
(1) live pulls of Alpha's MAP history from TimeBack's OneRoster API (1,844 G2–G5 Reading records; pulled 2026-06-17/25, re-pulled in full 2026-07-03) — labelled **Direct-pull**;
(2) an independent whole-population analysis of the reporting database (`rpt2_map_scores`) that our own credentials cannot reach, corroborated by a second independent rpt2 analysis and our own coverage-bias decomposition — labelled **External-review** (full workup: the population-baseline analysis in the engine repository);
(3) NWEA's own primary documents (*MAP Growth Technical Report for 2024–2025*; 2025 Norms) — labelled **NWEA-verified**;
(4) seven Monte Carlo validation studies against the item bank (2026-07-03 v4 run: production selection path + randomesque selection, full 786-item bank, G2–G5 prior, TimeBack-parity configuration; ~17,900 sessions) — labelled **Simulation**;
(5) external peer-reviewed literature — labelled **Derived**.
Where a claim needs data that does not yet exist (a concurrent MAP cohort), it is labelled **Open**. That discipline is deliberate — it is the same standard we are asking the instrument to be held to.

## 1. The ask

Approve the Incept MAP Proxy for a Stage-2 feasibility pilot (**~40 students, 1–2 classes**, G2–G5, one ~45-minute adaptive session each), and approve in principle a Stage-3 linking study in which students take the proxy within two weeks of their official Fall 2026 MAP sitting — the N≥1,000 paired-score cohort accruing through regular use inside Alpha's existing MAP calendar, not a separate recruitment.

The pilot is deliberately small, and we are honest about what that size can and cannot do. ~40 students × ~40 items is roughly 1,600 responses against a 786-item bank — nowhere near the ~200 responses per item that calibration requires — so the pilot claims no calibration. Its job is feasibility: completion rate, session duration, rapid-guess rates, teacher and student experience, and early item red flags from response patterns. Calibration then accrues from regular use — ongoing sessions accumulate toward the calibration thresholds (a ~300-student-equivalent response volume for the core band) — and the linking study reads out at the Fall 2026 MAP window once the paired cohort has accrued. The ladder is: pilot (~40, feasibility) → calibration via accumulated regular use → linking at the Fall 2026 window.

The case rests on three things, in order:
1. Alpha's current population sits near the 46th percentile with a real low tail, its growth signal is invisible between MAP windows — measurably, not rhetorically — and the only interim standardized instrument in the platform is effectively unused.
2. This instrument implements MAP's own published measurement design — model, scoring algorithm, blueprint structure, formats — verified against NWEA primary sources, and its adaptive engine passes seven simulation studies whose misses are reported alongside their hits.
3. Three adversarial reviews of this documentation package were run before it reached you (two audits plus a second teammate review), and every finding was either fixed or disclosed in this document. What you are reading has already survived the review a skeptical reader would give it.

Three design commitments are made in advance, so the plan cannot be quietly re-scoped later: (a) the ~40-student pilot deliberately includes **≥8 below-median G2 readers and ≥8 above-median G5 readers** — coverage and feasibility at the edges (floor/ceiling UX and flag behavior), with the ≥150-responses-per-tail-band-item target attached to the calibration stage that accrues from regular use, not to the pilot; (b) RIT unlock at Stage 3 is band-aware — the calibrated core band unlocks first, while floor/ceiling-flagged scores stay logit-only until tail-targeted calibration reaches SE(b̂) ≤ 0.30 there too; (c) the EBSR scoring question is pre-committed to a dual-scoring comparison with a named decision statistic, decided before RIT unlock (details in the Concurrent Validity Plan tab).

We are not asking you to approve a RIT-equivalence claim. We have no paired proxy↔MAP data yet, and the engine refuses to emit RIT scores until we do. We are asking you to approve the pilot that starts the ladder toward that data — a plan which, because Alpha already administers MAP network-wide, is a scheduling decision rather than a research-partnership hunt.

## 2. The problem: the growth signal arrives too late to act on

**First, the population truth — including a correction of our own earlier framing.** Earlier drafts of this package described Alpha's G3 readers as high-achieving: "mean RIT 206.4 ≈ 72nd percentile," computed from 409 OneRoster records. That figure is **retired**. An adversarial review recomputed the *full current* G3 population from the reporting view `rpt2_map_scores`: **n = 915, mean RIT 196.0, mean percentile 46.3** (External-review — corroborated by an independent rpt2 analysis and by our own coverage-bias decomposition; full workup in the population-baseline analysis in the engine repository). The old figure was not an arithmetic slip but a compound of three biases we have now quantified (Direct-pull → computed): repeat-record over-weighting of long-tenured students (+5.4 RIT at G3), cohort staleness (91/173 G3 latest records predate SY 2024-25; current-year-only mean is 198.3), and — largest and unfixable from OneRoster — source coverage: the OneRoster MAP batch import is itself a selected, high-achieving slice, sitting at mean percentile ~74 in *every* grade while the full reporting population sits near 46.

The honest per-grade baseline (our reachable OneRoster views, with the External-review population figure where it exists):

| Grade | OneRoster slice, latest/student | Current cohort (SY 2025-26) | Slice mean percentile | Full population (External-review) | Which tail binds (bank ~RIT 155–250) |
| :---- | :---- | :---- | :---- | :---- | :---- |
| G2 | 194.8 (n=176) | 185.5 (n=60) | ~74 | — | **Floor** — only grade with a visible below-155 tail; rpt2 shows the bottom-quartile G2 mean at RIT 156.6, exactly at the new floor |
| G3 | 207.4 (n=173) | 198.3 (n=42) | ~74 | **196.0, 46th pctile (n=915)** | **Floor** — weakly on our slice, decisively on the true population (mean percentile 46 implies a fat low tail our slice never sees) |
| G4 | 215.7 (n=232) | 211.5 (n=70) | ~75 | — | **Ceiling (mild)** — ~1 in 20 current G4 above RIT 235; no floor exposure |
| G5 | 222.6 (n=230) | 220.7 (n=70) | ~75+ | — | **Ceiling (badly)** — ~20% of current G5 sit above even RIT 235; the bank cannot yet measure the top quintile of G5 |

**This reframing strengthens the case, it does not weaken it.** A 72nd-percentile population arguably coasts; a 46th-percentile population with a real low tail is exactly the population for which waiting a season between growth measurements is most costly. And the tails table above is now the bank-expansion roadmap, not an average that hides both edges.

What remains true from the original problem statement — now explicitly scoped to the **measured subset** (the OneRoster slice with fall-to-fall growth data, which skews high-achieving; the true population numbers below may differ; accumulated regular use will measure them):

| # | Fact | The measured number (measured subset) |
| :---- | :---- | :---- |
| 1 | **G3 growth velocity is below median** | Mean fall-to-fall CGP **49.2** (n=65 with growth data); **52%** grew slower than national peers who started at the same RIT; **40%** achieved the 2× growth target |
| 2 | **The decline is grade-specific** | G2 grows *above* median (CGP 55.5; 63% meet projection) — the velocity collapse appears at G3 |
| 3 | **The weak domain is nameable** | Informational Text is the weakest MAP sub-goal at *both* G2 and G3 in this subset — despite a nonfiction-heavy incumbent course |

If even the platform's high-achieving, best-covered slice grows below median at G3, the burden of proof sits with anyone claiming the fuller, lower-achieving population is doing better.

Two further measured facts frame the stakes:
• Official MAP runs 2–3 windows per year. A student growing at CGP 35 in October is invisible until the winter report. The 2× growth program is a velocity target managed without an interim velocity measurement.
• The only interim standardized instrument in TimeBack — the STAAR G3.2022 test — is fixed-form, 100% MCQ, produces no RIT-scale score and no domain sub-scores, and has **18 result records, at most one of them a real student** (Direct-pull).

This is the bar to beat — not "MAP is inaccessible," but a measurement layer with nameable, fixable gaps.

## 3. Audits and fixes — the short version

Three adversarial reviews were run against this documentation package before it reached you: two independent audits (one checking every number against the engine's own artifacts, one fact-checking every external claim against NWEA primary sources) and a second teammate review. Every finding was either fixed or disclosed in this document. The full scorecard — each finding and its disposition, one line each — lives in the Audits & Fixes tab.

## 4. What we built

A complete, MAP-design-aligned adaptive assessment, live in TimeBack staging:

| Artifact | Count / status | Note |
| :---- | :---- | :---- |
| Adaptive engine | Live (Cloud Run) | Fisher-information CAT with domain quotas; Rasch 1PL; MLEF scoring with the 3.8-logit fence (NWEA-verified design) |
| Items | 650 operational (786 harness-loadable) | 13 bank files, G2–G5 band labels, provisional difficulties spanning ≈ RIT 175–220 in the operational core; the authoritative v4 validation ran against the full 786-item bank (staged expansions below) |
| Item formats | 6 | See section 5 |
| Quality gate | 14 dimensions | Every item passed a 14-dimension quality check with a ≥0.85 pass threshold before entering the bank: text-dependence ablation, CCSS alignment, near-neighbor distractors, Lexile-to-band matching |
| CCSS coverage | 50+ standards | RL / RI / L strands, G2–G5 |
| Session structure | 40 scored (14/13/13), extending to 43 for precision | NWEA's TR Table 3.2 shows an *example* 13/13/13 blueprint; its public test description states 40–43 questions. The engine adopts TimeBack's operational 14/13/13 = 40 split — consistent with NWEA's published structure, identical across both Alpha engines (authoring decision; NWEA-verified for 40–43) |
| Domain sub-scores | 3 | Literary · Informational · Vocabulary — the same three instructional areas Alpha's MAP imports already carry in OneRoster |
| TimeBack integration | Live (staging) | Cognito SSO login; scores written to the gradebook via Caliper events; course *Incept MAP Adaptive Assessment — Grade 3* registered under Alpha School |
| Score output | Logit ± SE only | RIT output is code-blocked until scale linking (deliberate); the reported SE is b-uncertainty-adjusted (see §7) |

**Bank status — both tails, stated plainly.** The operational bank is 650 items. Staged expansions are now merged and harness-loadable: +92 edge items (PR #30; floor to ~RIT 155, ceiling to 235) and +44 items (PR #35, all CI green: 26 standard-gap items closing nine under-target standards, plus 18 G5 super-ceiling items at RIT 231–250 — directly answering the ~20%-of-G5-above-235 finding in §2). Total: **786 items harness-loadable** (the `load_bank()` build dedups to 786 unique items, which differs from the naive fixture sum), difficulty b −4.45 → +4.55 ≈ RIT 155–250 — and this full 786-item bank is what the authoritative v4 validation ran against; adoption into the production bank remains a reviewable decision pending calibration. Students below RIT 155 route to the official K–2 MAP instrument — we own that boundary explicitly rather than stretching the proxy past its floor.

## 5. Item-format breadth (live)

The incumbent measurement layer is 100% single-select MCQ — all 1,077 incumbent course items and the 33-item STAAR test (Direct-pull). The proxy teaches nothing, but it tests the way MAP tests:

| Format | Items | Share of bank | Reading 2–5 evidence |
| :---- | :---- | :---- | :---- |
| MCQ (single-select) | 265 | 40.8% | Confirmed in TR Reading figures |
| Sequence / drag-to-order | 102 | 15.7% | Documented in MAP Growth pool (other subjects' figures) |
| MSQ (multi-select) | 90 | 13.8% | Confirmed in TR Reading figures |
| Gap-match / classify | 76 | 11.7% | NWEA secondary materials only |
| EBSR (2-part evidence) | 63 | 9.7% | Confirmed in TR Reading figures (composite) |
| Hot-text | 54 | 8.3% | Documented in MAP Growth pool (other subjects' figures) |

One scope note on the familiarization benefit: it is strongest for the three formats confirmed in Reading 2–5 specifically (MCQ, multi-select, EBSR/composite) — the other three are low-harm additional practice, not a claimed MAP-preparation benefit.

Stated plainly: NWEA's Technical Report confirms three of these six formats in Reading 2–5 specifically; the other three are documented for MAP Growth more broadly or in NWEA secondary materials. One deliberate deviation: the TR scores composite items dichotomously; our EBSR uses partial credit (0/1/2) to preserve information from partial responses. Neither point affects the measurement model, and both are disclosed rather than argued.

## 6. Why this beats the incumbent measurement layer

| Incumbent gap | What the proxy does | Evidence |
| :---- | :---- | :---- |
| No RIT-scale signal between MAP windows | 40–43-item adaptive session, immediate logit score ± SE, any modern browser | Live deployment; Simulation 1 (r = 0.967 ability recovery, v4) |
| No domain diagnosis | Literary / Informational / Vocabulary sub-scores every session — the domains Alpha's MAP data says matter (Informational weakest at G2 and G3) | Direct-pull + live score report |
| One format (100% MCQ) | Six formats under MAP's interaction rules — forward-only, answer-before-advance, untimed | Live; section 5 |
| Fixed form, gameable by repetition | Adaptive selection with domain quotas, topic caps, and randomesque exposure control; pool ratio stated both ways — 650/40 = 16.3× session length; vs Stocking's recommended 10× floor (400 items) = 1.6×; staged expansions raise the pool further (see the Item Bank tab) | Simulation 5 (blueprint held in 100% of sessions, ±1) |
| No engagement validity check | Per-item timing captured; rapid-guessing flagged — mirroring NWEA's own >25% rapid-guess validity rule | Engine telemetry; NWEA-verified rule |
| Effectively unused (18 results, ≤1 real student) | Enrollment via existing TimeBack course tile; pilot occupies the existing unused standardized-test slot | Direct-pull |

**Distribution is not adoption — and we do not conflate them.** The empty STAAR slot is the cautionary tale: an instrument that was distributed in the platform and produced no actionable output went unused (18 results, at most one real student). Being enrolled in TimeBack gets the proxy in front of students; it does not make anyone use it twice. The insight features in development (per-domain reports, growth tracking, teacher views) are the adoption mechanism. And adoption is *measured*, not assumed: the pilot carries completion-rate success/kill criteria, and a proxy nobody voluntarily re-administers fails on those criteria regardless of its psychometrics.

## 7. Simulation evidence and benchmarks

Seven Monte Carlo studies. Provenance: 2026-07-03 v4 run — production selection path + randomesque selection, full 786-item bank, G2–G5 prior, TimeBack-parity configuration (14/13/13 = 40 scored, hard cap 43, SE stop 0.35, TEI floor ≥12); ~17,900 sessions; authoritative source: the v4 validation report in the engine repository. Misses included (Simulation):

| Metric | Result (v4) | Reference point | In plain terms | Status |
| :---- | :---- | :---- | :---- | :---- |
| Ability recovery (r with true ability) | 0.967 | ≥ 0.90 | Does the test rank stronger readers above weaker ones? | Meets |
| RMSE | 3.20 RIT | < 4.0 RIT | How far off is the score from the truth, on average? | Meets |
| Systematic bias | −0.04 RIT (reliable-range −0.04; max per-band 0.83) | abs(bias) < 0.5 overall; ≤ 1.5 per band | Does the test systematically score too high or too low? | Meets — near-eliminated on the full bank |
| SEM (core band) | 3.14 RIT | ≤ 4.0 RIT (MAP published CSEM ≈ 3.3–3.6) | How precise is one session's score? | Meets |
| Marginal reliability (core range) | 0.931 | ≥ 0.93 target; MAP published: 0.96 | Would a retake give a similar score? | **Meets the 0.93 target (0.931); MAP's 0.96 is the higher operational bar** |
| Blueprint adherence | 100% of sessions (±1 vs 14/13/13 on the 40-item scored form) | 100% | Does every session deliver the right mix of reading domains? | Meets |
| TEI floor | 100% of sessions ≥ 12 TE items (mean 16.2, gap-match counted) | 100% | Does every session include enough interactive (beyond-MCQ) items? | Meets |
| Internal cross-bank consistency (synthetic — NOT MAP agreement) | r 0.918; 95% LoA [−10.0, +10.0] RIT | r ≥ 0.85 | Does the engine score the same student consistently on a different item set? | Meets, with synthetic-bank caveats |
| Parameter-error robustness | reliability ≥ 0.915 at σ ≤ 1.0 logits | ≥ 0.85 | Does it still work when our difficulty estimates are imperfect? | Meets |
| MLEF divergences | 0 in ~17,900 sessions | 0 | Does scoring ever break on extreme answer patterns? | Meets |
| Reliable range | RIT 160–230 | G3–G5 + G4/G5 ceiling + median-and-above G2 | Across which ability range can we trust the score? | Median G2 fall reader (~RIT 170) now inside the reliable range; only the bottom ~5% (below RIT 160) route to K–2 MAP |
| Session length | mean 40.6 items; 76.5% stop at 40, 15.1% reach the 43 cap | 40–43 | Do sessions stay within MAP's 40–43-item structure? | Meets |

The path to these numbers is part of the evidence, and we report it rather than the final table alone. The first production-path run (v1, 2026-07-02) regressed RMSE to 4.73 and surfaced a +2.62 RIT systematic overestimate — we published both. The root cause was then isolated (v2): the +2.62 lived in the Owen running estimate's prior shrinkage, not in the shipped score; re-basing the final score on the score report's MLEF value removed it (bias −0.46, RMSE 3.70). The v3 run re-validated everything under the TimeBack-parity constants adopted in engine PRs #26/#34 (14/13/13, 40 scored, SE 0.35, TEI ≥12) with randomesque exposure control on the 650-item bank (RMSE 3.44, bias −0.38). The authoritative v4 run then re-ran the identical validation on the full 786-item bank (after the floor/ceiling/standard-gap expansions merged): RMSE 3.20, bias −0.04 (near-eliminated), zero MLEF divergences. Remaining open items, stated plainly: the 171–180 selection cells improved but are not yet fully served; 38 items are over-exposed (>30%) and 289 never used (never-used rose with the larger bank — per-band exposure balancing is the open follow-up).

One honesty instrument shipped with the score report itself: because provisional b values understate true score uncertainty, reports emit a **b-uncertainty-adjusted SE** — the Fisher SE inflated by the current validation run's RMSE/SEM ratio (1.02 under v4) — with an explicit `se_basis` field naming the adjustment; it is removed automatically once empirical calibration lands (engine PR #33).

## 8. The BrainLift — the thinking behind the instrument

The full BrainLift lives in the BrainLift tab. Its defining feature of measurement: a valid proxy session places a G2–G5 reader on the same ability continuum MAP measures — via the same model (Rasch 1PL), the same scoring (MLEF), a blueprint consistent with MAP's published structure (14/13/13 = 40 scored, extending to 43), the same formats and testing conventions — precisely enough to act on (SEM ≤ 4 RIT) and honestly enough to trust (no RIT claim before an empirical link to NWEA's scale exists).

Its load-bearing positions, in brief: measurement cadence — not curriculum — is the binding constraint on the 2× program; replicate MAP's published machinery exactly rather than approximating it; enforce the claims ladder in code (RIT output blocked until linked); Rasch 1PL is the only honest pre-pilot model; a fixed form cannot span G2–G5 in 40 items; format familiarity is measurement hygiene, not test prep; and Alpha is the one place where the linking study is a calendar entry rather than a partnership negotiation.

## 9. The one honest tension

Every psychometric result in this package is either design parity (verified against NWEA documents) or simulation. **None of it is yet empirical.** The b-parameters are expert-assigned; the reliability and RMSE figures assume the Rasch model is correctly specified; the internal cross-bank consistency simulation used a synthetic MAP-like bank, not NWEA items — it is a consistency check, not MAP agreement. If the Rasch model is misspecified for our items, every simulated figure is optimistic. We name this as the single most defensible remaining critique — it is the gap between a demonstrably-right design and a proven instrument, and it cannot be closed by more documents. The pilot is designed to resolve it; simulation supports but cannot guarantee that it will. We would rather state that than let a reviewer find it.

## 10. Done vs. in flight — stated plainly

Live and verifiable today:
• 650-item operational bank (13 files, counted programmatically), 6 formats, 14-dimension quality gate.
• Adaptive engine live on Cloud Run under the TimeBack-parity configuration (14/13/13 = 40 scored, cap 43, SE stop 0.35, TEI floor ≥12); TimeBack staging course with SSO and Caliper gradebook writes.
• Seven simulation studies validated under the parity configuration on the full 786-item bank (v4, 2026-07-03): all green criteria met, including marginal reliability 0.931 — now meeting the ≥0.93 target (MAP's published 0.96 remains the higher operational bar).
• The v1 +2.62 RIT bias root-caused (Owen running-estimate prior shrinkage) and resolved by re-basing the final score on the shipped MLEF value (v2); overall bias fell to −0.04 RIT on the full bank under v4 (near-eliminated).
• Randomesque exposure control in both selection phases — the deterministic-first-passage finding is fixed; never-used items are 289 on the full 786-item bank (they rose with the larger bank; per-band exposure balancing is the open follow-up).
• RIT output blocked in code; score reports show logit ± b-uncertainty-adjusted SE (×1.02, `se_basis`-labelled; engine PR #33) and domain sub-scores with a "not a RIT score" label.
• Two adversarial audits plus a second teammate review run; all findings fixed or disclosed (full scorecard in the Audits & Fixes tab).
• Public /test route gated behind a flag so the item bank cannot be farmed anonymously.
• Staged bank expansions merged: +92 edge items (PR #30) and +44 items (PR #35: 26 standard-gap closing nine under-target standards + 18 G5 super-ceiling at RIT 231–250; 26/26 and 18/18 passed quality checks after re-authoring, min 0.950) — **786 items harness-loadable** (the `load_bank()` build dedups to 786 unique items), ≈ RIT 155–250; production adoption a reviewable decision pending calibration.
• EBSR dual-scoring comparator built and wired for the pilot (engine PR #33).

In flight / proposed (engineering-confirmed, not yet complete):
• Insight features in development (will be available): per-domain student reports in plain language, growth-velocity tracking, growth-vs-similar-peers comparison for teachers, engagement flags, and a teacher class heatmap — all pre-linking-safe by design.
• Per-band exposure balancing: never-used items rose to 289 with the larger 786-item bank, and 38 items exceed 30% exposure — exposure-aware scoring is the open follow-up.
• Full service of the 171–180 selection cells — improved under v4 but not yet fully served.
• A per-standard session cap (max 2 items/standard/session) to mitigate over-concentrated standards — proposed in PR #35, not shipped.

Open (needs the pilot / external action):
• The ~40-student feasibility pilot (1–2 classes; completion, duration, rapid-guess rates, teacher/student experience, early item red flags). Empirical item calibration — accrues from regular use (a ~300-student-equivalent response volume for the core band; ≥150 responses per tail-band item for the tails). Concurrent validity and scale linking (N≥1,000 pairs accrued via usage, within 2 weeks of official MAP at the Fall 2026 window). Any RIT, percentile, or CGP output — core band first, tails after tail-targeted calibration.
• Legal review of the product name and UI provenance before anything external. DIF analysis, test-retest, accessibility (WCAG) audit — Stage 4.
• Student-ID crosswalk provisioning between MAP records and internal IDs for the linking analysis.

## 11. What we will and won't claim

• We will claim: the measurement design matches MAP's published design, verified against NWEA primary sources (with the 14/13/13 operational split disclosed as TimeBack's, consistent with NWEA's published 40–43 structure); the adaptive engine passes its v4 simulation suite on the full 786-item bank, meeting the ≥0.93 reliability target (0.931; MAP's 0.96 remains the higher operational bar); the instrument is live, integrated, and pilot-ready; and Alpha's own MAP data — re-baselined to the full population — shows exactly the growth-velocity blind spot an interim instrument addresses.
• We will not claim: that a proxy score equals a MAP score (Open — that is the linking study's job); that simulated reliability is operational reliability; a RIT gain, a growth multiple, or "proven." The engine enforces the first of these by refusing to emit RIT.

## 12. The ask, restated

Approve the ~40-student feasibility pilot (1–2 classes) and schedule the Stage-3 linking window at the Fall 2026 MAP sitting. The design is right and verified; the engine is live and integrated; the documentation has survived adversarial audit; the claims are enforced in code, not just prose. Approving the pilot starts the ladder that turns a demonstrably-right instrument into a proven one: real students first, calibration accruing from regular use, and real paired MAP data — collected inside a testing calendar Alpha already runs.

*Prepared from live TimeBack OneRoster pulls (2026-06-17/25, full re-pull 2026-07-03), the external-review population baseline (the population-baseline analysis in the engine repository), the NWEA MAP Growth Technical Report for 2024–2025 and 2025 Norms, seven Monte Carlo validation studies (v4 run, 2026-07-03, TimeBack-parity configuration, full 786-item bank; the v4 validation report in the engine repository), two adversarial documentation audits (2026-07-02), and a second teammate review (2026-07-02). Full evidence package: the Validity Case tab and its companion tabs. MAP® is a registered trademark of HMH Education Company / NWEA; this instrument is independent and not affiliated with or endorsed by NWEA.*
