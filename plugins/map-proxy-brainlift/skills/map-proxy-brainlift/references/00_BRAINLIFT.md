# BrainLift

# Assessment BrainLift: Incept MAP Proxy (Grades 2–5 Reading)

## Purpose

This BrainLift gives an assessment designer (human or LLM) what they need to build and validate a G2–G5 reading assessment that closes the measurement gap Alpha's own MAP data names: a full current population sitting near the 46th percentile with a real low tail (G3: n=915, mean RIT 196.0 [EXTERNAL-REVIEW]), growth velocity that collapses at G3 even in the platform's high-achieving measured subset (fall-to-fall CGP 49.2 vs. G2's 55.5), a 2× growth program managed with only 2–3 official MAP windows per year, an interim standardized instrument (STAAR G3.2022) with at most one real student user, and a domain weakness (Informational Text, weakest at both G2 and G3 in the measured subset) that no in-platform instrument can currently detect per-student. The instrument's reference target is NWEA MAP Growth Reading 2–5. It is MAP-designed, not MAP-claimed — score output is Rasch logit ± SE only, and RIT output is blocked in code until an in-cohort concurrent study links the scales. Authoring substrate is the Incept adaptive engine (FastAPI / Cloud Run), a 650-item quality-check-gated operational bank (786 harness-loadable with the staged tail expansions), and native TimeBack delivery (Cognito SSO, Caliper gradebook events, OneRoster result structures).

In scope: the defining feature of valid proxy measurement, DOK4 Spiky POVs that anchor the design, DOK3 Insights derived from the build and two adversarial audits, DOK2 evidence summaries with sources, the locked decisions, the open forks left for the group, and the honest measurement-ceiling discipline.

Out of scope: build-time engineering specifics (live in the engine repo `trilogy-group/Incept-MAP-proxy`), item authoring prompts (live in the generator spec in the engine repository), the concurrent-study statistical procedures (live in the Concurrent Validity Plan tab), curriculum/instruction design (this is a measurement instrument, not a course), and any externally validated RIT projection (deferred until the in-cohort concurrent study).

## Defining Feature of Mastery

A valid proxy session **places a G2–G5 reader on the same ability continuum NWEA MAP measures — using the same measurement model (Rasch 1PL), the same scoring algorithm (MLEF with the 3.8-logit fence), a content blueprint consistent with MAP's published structure (14 Literary / 13 Informational / 13 Vocabulary = 40 scored, extending to 43), the same item interactions, and the same testing conventions (untimed, forward-only, answer-before-advance) — precisely enough to act on and honestly enough to trust.** Given one ~30–45-minute adaptive session, the instrument produces: an overall ability estimate θ̂ with SEM ≤ 4 RIT-equivalents at the core range; three domain sub-scores aligned to the exact instructional areas Alpha's MAP imports already carry; per-item timing with rapid-guess flags mirroring NWEA's >25% validity rule; and — deliberately — **no RIT, percentile, or CGP** until a concurrent study empirically links our logit scale to NWEA's. Validity does NOT require the proxy to *be* MAP; it requires every claim the score report makes to be either verified against NWEA primary sources, measured in our own data, or refused. Design implication: every component is either a replication of a documented MAP design element (tagged NWEA-verified) or a disclosed deviation (tagged authoring decision); silent approximations are not modelled.

Structural caveat (grade-range edges). Under the authoritative v4 full-bank run, the simulated reliable range now spans **RIT 160–230** — the median G2 fall reader (national mean ~170) sits inside the reliable range, where earlier runs put it below the floor. Which tail binds is grade-specific, per the re-baselined population data [EXTERNAL-REVIEW + COMPUTED — see the population-baseline analysis in the engine repository]: **G2 floor (largely closed), G3 floor, G4 mild ceiling, G5 ceiling** (~20% of current G5 sit above even RIT 235). Both edges are named, flagged in score reports, and addressed by the merged tail expansions (floor to ~RIT 155, ceiling to 250 with the G5 super-ceiling set — harness-loadable, adoption pending calibration); only the bottom ~5% of readers (below RIT 160) route to the K–2 MAP instrument, and neither edge is hidden inside an average.

## DOK4 — Spiky Points of View

These are the load-bearing positions. Every other section in this BrainLift derives from these.

### SPOV1 — Measurement cadence is the #1 problem, not curriculum

The two-population truth first, because we got it wrong once: the full current G3 population is **n≈915, mean RIT 196.0, 46th percentile** [EXTERNAL-REVIEW, corroborated by an independent rpt2 analysis and our own coverage-bias decomposition — the population-baseline analysis in the engine repository]. Our OneRoster slice is coverage-biased — mean percentile ~74 in *every* grade — and the old "206.4 ≈ 72nd percentile" framing is **retired**: it was a compound of repeat-record over-weighting, stale cohorts, and source coverage bias, not an arithmetic error alone. Even that high-achieving measured subset grows below the 50th CGP at G3, and the fall baseline hasn't moved in eight years of curriculum iteration. **The binding constraint on the 2× program is that growth velocity is measured 2–3 times a year, so every instructional correction is a season late.** An assessment that produces a trustworthy interim ability estimate every 4–6 weeks attacks the constraint directly; another curriculum revision does not. And the re-baselining *sharpens* the case: a 46th-percentile population with a real low tail needs interim measurement more than a coasting 72nd-percentile one ever did.

**Why we're confident:** the population figures are externally reviewed and independently corroborated; the growth-velocity numbers are direct pulls, not estimates — CGP 49.2 (n=65 with growth data, measured subset), 52% below-median, 40% 2× rate, flat 196.9→198.4 baseline. And the G2 contrast (CGP 55.5) shows the problem is grade-localized, which cadence-blind annual iteration keeps missing.

### SPOV2 — Replicate MAP's published machinery exactly; approximate nothing silently

Every measurement-design choice is taken from NWEA's own Technical Report, not from intuition: Rasch 1PL ("scaling is accomplished using the Rasch model"), MLEF scoring with the verbatim 3.8-logit fence, and a blueprint anchored to what NWEA actually publishes: Technical Report Table 3.2 shows an *example* blueprint of 13/13/13 + up to 4 field-test items, and NWEA's public test description states 40–43 questions. The engine adopts TimeBack's operational split of 14/13/13 = 40 scored items, extending to 43 for precision — consistent with NWEA's published structure and identical across both Alpha engines [AUTHORING-DECISION; NWEA-VERIFIED for the 40–43 structure]. Where we deviate (EBSR partial credit vs. the TR's dichotomous scoring), the deviation is disclosed and argued, never passed off as parity.

**Why we're confident:** each element was re-verified against the actual TR PDF in July 2026 — including by an adversarial fact-check agent instructed to refute the claims. The blueprint even corrected our own earlier 45/40/15 assumption.

### SPOV3 — The claims ladder is enforced in code, not prose

Pre-pilot output is logit ± SE and domain sub-scores; RIT, percentile, and CGP are **blocked in the engine**. Documents can drift; code paths don't. A teacher cannot misread a score report into a RIT claim because the number does not exist in the response.

**Why we're confident:** the strongest honesty mechanism we found in any comparable product is a disclaimer; ours is a refusal. The two audits found number-drift in our *documents* (0.930 vs 0.928) — which is exactly why the load-bearing claim gate lives in code.

### SPOV4 — Rasch 1PL is the only honest pre-pilot model

3PL requires estimating discrimination and guessing parameters, which need ≥1,000 responses per item that do not exist pre-pilot. Using 3PL now would mean inventing parameters and calling them measurement. Rasch requires only difficulty, which can be provisionally assigned and then empirically corrected — and it is MAP's own stated calibration model.

**Why we're confident:** this is both the psychometric literature's position (Wright & Stone 1979; Linacre 1994) and NWEA's documented practice; the robustness simulation shows the engine tolerates provisional-parameter error to σ=1.0 logits without reliability collapsing below 0.85.

### SPOV5 — Adaptive or nothing for a cross-grade instrument

A fixed 40-item form cannot measure RIT ~161–227 (G2 fall through G5 spring) with SEM ≤ 4: items informative for a struggling G2 reader are noise for an advanced G5 reader. The earlier fixed-form G3 design was superseded for this reason, on the record.

**Why we're confident:** this is arithmetic, not preference — Fisher information concentrates near |θ − b| ≈ 0, and 40 items spread across a 6.5-logit range leaves too little information anywhere. MAP itself is adaptive for the same reason.

### SPOV6 — Format familiarity is measurement hygiene, not test prep

Alpha students practice on 100% MCQ material; their first multi-select or two-part evidence item is on the scored official MAP. Interface novelty is construct-irrelevant variance (AERA/APA/NCME Standard 1.13). Rendering MAP's item interactions under MAP's testing conventions removes noise from the official measurement — it does not inflate ability, and we do not claim it does.

**Why we're confident:** the response-process argument is standards-based, and the deviation risk runs the other direction — which is why the UI is "MAP-like" (familiar conventions), with the earlier "pixel-accurate replica" framing dropped and the trademark boundary made explicit.

### SPOV7 — Alpha is the linking lab; anywhere else it's a partnership hunt

Concurrent validity requires the same students taking both tests within two weeks. Alpha already administers official MAP network-wide (386 assessment line items since 2017), and proxy results already land in the same OneRoster gradebook via Caliper. The Stage-3 linking study is therefore a scheduling decision inside an existing testing calendar.

**Why we're confident:** the MAP data inventory is a direct API pull, and the integration is live in staging — the only missing piece is a student-ID crosswalk, which is provisioning work, not research.

## DOK3 — Insights (derived takeaways)

These are settled positions that follow from the SPOVs but are operational rather than contrarian.

### Insight 1 — Two products on one engine, unlocked in stages

Pre-linking, the instrument is an **interim diagnostic**: logit growth curves, domain sub-scores, engagement flags — enough for teachers to act between MAP windows. Post-linking, the same engine becomes a **RIT-scale proxy**: percentile, CGP-style growth reads, historical comparability with Alpha's nine years of MAP records. Neither stage borrows the other's claims; the stage gate is the concurrent study.

### Insight 2 — The pilot is designed to resolve precision; simulation supports but cannot guarantee it

The authoritative v4 full-bank run (2026-07-03) cleared what the v1 production run had flagged and improved on the interim v3 run: RMSE 3.20 RIT (was 4.73 at v1, 3.44 at v3 — within the <4.0 target), bias −0.04 RIT (the +2.62 overestimate was root-caused to the Owen running estimate's prior shrinkage and resolved by re-basing the final score on the shipped MLEF value; on the full 786-item bank the residual bias is near-eliminated), and marginal reliability 0.931 — now meeting the ≥0.93 target. What remains is the distance to MAP's published 0.96 operational bar, which shares one root-cause family with any residual band-level imprecision: expert-assigned b-parameters under the wide G2–G5 prior. The robustness simulation shows the *algorithm* tolerates parameter uncertainty; empirical calibration — accrued through regular use toward a ~300-student-equivalent response volume for the core band — replaces the guessed parameters. The plan is designed to resolve this; simulation supports but cannot guarantee it — which is exactly why the ask is real usage (a ~40-student feasibility pilot, then calibration accruing from regular sessions), not more simulation.

### Insight 3 — Report the domains MAP reports, in the schema the platform already stores

Alpha's MAP imports carry three Reading 2–5 goal areas (Literary Text, Informational Text, Vocabulary) in OneRoster result metadata. The proxy emits sub-scores for exactly those three, so per-domain history is queryable across proxy and official MAP in one structure — and the documented weak domain (Informational) is trackable per-student, per-session.

### Insight 4 — Bank economics bind at the edges, and the edges differ by grade

Pool ratio stated both ways: 650/40 = 16.3× session length; against Stocking's recommended 10× floor (400 items), 1.6× — adequate, not lavish, and the staged expansions raise it further (786 harness-loadable). The binding constraints are the edges, and the re-baselined population data says which edge binds where [EXTERNAL-REVIEW + COMPUTED]: **G2 floor** (the only grade with a visible below-155 tail — largely closed now that the v4 reliable range reaches RIT 160), **G3 floor** (decisively on the true 46th-percentile population), **G4 mild ceiling**, **G5 ceiling — badly** (~20% of current G5 above even RIT 235). The old ceiling-first framing keyed to "G3 mean 206.4" is retired with that number. Bank expansion priorities follow the population, not the average — hence the merged floor extension to ~RIT 155, the G5 super-ceiling set at RIT 231–250, and explicit routing of sub-155 students to the official K–2 MAP.

### Insight 5 — Engagement telemetry mirrors NWEA's own validity rules

NWEA invalidates tests above 25% rapid-guessing; disengagement deflates scores (Wise & DeMars 2005). The proxy captures per-item timing silently and flags rushing — so a disengaged student is coached before the official window, and a proxy score carries its own validity flag rather than silent noise.

### Insight 6 — Adversarial audit is part of the build, not the review

The documentation package was audited by two independent adversarial agents (internal-consistency; external fact-check) and then by a second teammate review before reaching any approver. Findings — a rounded-up reliability, a bank table that didn't sum, sims broader-scoped in prose than in code, a legally hazardous UI section, a coverage-biased population baseline, an under-stated SE — were fixed or disclosed in the Case for Approval's scorecards. The discipline: any claim that would embarrass us if checked *was* checked, by an agent instructed to break it.

### Insight 7 — The score report's honesty is a feature teachers need, not a legal hedge

Pre-linking reports carry "not a RIT score" labels, floor/ceiling flags, and SEs. A teacher who trusts a flagged, bounded number acts on it; a teacher burned once by an overclaimed number ignores the instrument forever. Honest uncertainty display is adoption strategy.

## DOK2 — Knowledge Tree Summaries

The empirical evidence the design rests on, grouped by load-bearing claim.

### Summary 1 — Alpha's G3 growth problem is real, grade-specific, and invisible between windows — and the population is lower-achieving than our slice showed

- Full current G3 population: **n=915, mean RIT 196.0, mean percentile 46.3** [EXTERNAL-REVIEW; corroborated by an independent rpt2 analysis]. Our OneRoster slice (409 G3 records / 173 students, 8 schools, 2017–2026) is coverage-biased at mean percentile ~74 in every grade; the old "206.4 ≈ 72nd pctile" figure is retired (repeat-record + stale-cohort + coverage bias — decomposed in the population-baseline analysis in the engine repository).
- Measured subset (OneRoster slice with growth data): mean f2f CGP 49.2 (n=65); 52% below-median growth; 40% 2× rate.
- G2 measured subset (399 records, 176 students): CGP 55.5, 63% meeting projection — above median.
- Fall baseline flat across eight years: 196.9 (2018-19) → 198.4 (2025-26) *(slice)*.
- Which tail binds, per grade: G2 floor · G3 floor · G4 mild ceiling · G5 ceiling (~20% above RIT 235) [COMPUTED + EXTERNAL-REVIEW].
- Implication: an interim velocity measure, domain-diagnostic, deliverable every 4–6 weeks — needed *more*, not less, by a 46th-percentile population with a real low tail. *(Direct-pull; External-review.)*

### Summary 2 — The incumbent interim instrument is unused and structurally insufficient

- STAAR G3.2022: 33 items, 100% MCQ, fixed linear form, %-correct scoring, no domain sub-scores.
- 18 result records total; at most 1 real student; the rest staff testing.
- All 1,077 incumbent course items are MCQ; no TEI formats anywhere in the platform.
- Implication: the proxy replaces an empty slot, not a working instrument. *(Direct-pull.)*

### Summary 3 — MAP's measurement design is public and replicable

- Rasch 1PL stated as the scaling model; MLEF scoring with the 3.8-logit fence verbatim (Equations 10–11).
- Blueprint: TR Table 3.2 shows an *example* Reading 2–5 blueprint of 13/13/13 + up to 4 field-test items; the public test description states 40–43 questions. The engine adopts TimeBack's operational 14/13/13 = 40 scored split, extending to 43 — consistent with the published structure, identical across both Alpha engines [AUTHORING-DECISION; NWEA-VERIFIED for 40–43].
- Formats: MCQ, multi-select, composite confirmed in Reading 2–5 figures; hot-text, drag-and-drop in the wider pool; gap-match in secondary materials. Composite scored dichotomously.
- Published quality bars: marginal reliability 0.96 (G2–5 Reading, Table 7.7), CSEM ≈ 3.3–3.6 RIT (Table 7.5).
- Implication: design parity is checkable, so we checked it — and hold ourselves to the published bars, including the ones we don't yet meet. *(NWEA-verified.)*

### Summary 4 — The engine passes its v4 full-bank simulation suite, meeting the ≥0.93 reliability target

- v4 run (2026-07-03): production selection path + randomesque selection, full 786-item bank, G2–G5 prior N(−1.0, 1.2), TimeBack-parity configuration; ~17,900 sessions across 7 studies (the v4 validation report in the engine repository).
- Ability recovery r = 0.967 (≥0.90 benchmark); RMSE 3.20 RIT (<4.0); bias −0.04 RIT (near-eliminated on the full bank; max per-band 0.83); SEM 3.14 RIT (≤4.0); blueprint 100% (±1 vs 14/13/13); TEI floor 100% (mean 16.2 ≥ 12); 0 MLEF divergences; robust to parameter error to σ=1.0 logits.
- Marginal reliability 0.931 now meets the ≥0.93 target; MAP's published 0.96 remains the higher operational bar — empirical calibration is the closer.
- History reported, not smoothed: the v1 production re-run flagged RMSE 4.73 and bias +2.62; v2 root-caused the bias to the Owen running estimate's prior shrinkage and re-based the final score on the shipped MLEF value; v3 re-validated on the 650-item bank; v4 re-ran on the full 786-item bank, improving or holding every metric. Exposure follow-ups remain: 38 over-exposed, 289 never used (rose with the larger bank — per-band exposure balancing queued), and the 171–180 selection cells not yet fully served.
- Implication: algorithm validity is demonstrated on the production path across the full bank; the remaining distance to MAP's operational reliability awaits calibration. *(Simulation.)*

### Summary 5 — 2025 norms reset the reference points

- 2025 norms (effective 2025-26): G3 Reading fall 184.7 / spring 193.8 (~9 RIT growth); G2 170.1/181.7; G4 195.9/202.1; G5 203.7/208.4.
- Shift of 1–3 RIT downward vs 2020 norms; the RIT scale itself unchanged.
- Alpha's stored MAP metadata still carries 2020-norms growth references (`normsreferencedata: "2020"`).
- Implication: all norm-referenced computations must state their norm year; the proxy uses 2025. *(NWEA-verified; Direct-pull.)*

### Summary 6 — Interim assessment and engagement literature support the use case, bounded

- Formative feedback loops: Black & Wiliam (1998); interim-assessment programs ~0.2–0.3 SD (Kingston & Nash 2011).
- Disengagement deflates scores; rapid-guessing is the NWEA-recognized marker (Wise & DeMars 2005).
- We use these to justify the *mechanism* (earlier correction, cleaner measurement), never to project a RIT gain.
- Implication: direction, not magnitude. *(Derived.)*

### Summary 7 — The remaining validity gap is empirical, and only the pilot closes it

- b-parameters expert-assigned; SE(b̂) effectively infinite pre-calibration (Wright & Stone 1979). Score reports meanwhile emit a b-uncertainty-adjusted SE (Fisher SE × 1.02 under v4, `se_basis`-labelled) rather than pretending calibrated precision.
- The internal cross-bank consistency simulation (synthetic — explicitly NOT MAP agreement) used a synthetic MAP-like bank: r 0.918, 95% LoA [−10.0, +10.0] RIT under v4 — a consistency check, not evidence of equivalence.
- Concurrent design: N ≥ 1,000 pairs accrued through regular use at the Fall 2026 MAP window, counterbalanced, within 2 weeks, same season; tail-targeted calibration accumulation (≥150 responses per tail-band item, accrued from regular use — the ~40-student feasibility pilot seeds both tails with ≥8 below-median G2 and ≥8 above-median G5 readers); unlock gate r ≥ 0.80, mean diff < 5 RIT, held-out validation, core-band-first RIT unlock (Kolen & Brennan 2014).
- Implication: the ask is the study, not the claim. *(Simulation; Open.)*

## DOK1 — Facts and Sources

Primary measurements (not estimates):

- G3 population: n=915, mean RIT 196.0, mean percentile 46.3. *(External-review, `rpt2_map_scores`; corroborated by independent rpt2 analysis 2026-06-23; adopted as authoritative — the population-baseline analysis in the engine repository.)* The retired slice figure: 206.4 across 409 records / 173 students (mean pctile ~74 — coverage-biased). *(OneRoster pull 2026-06-17, re-pulled 2026-07-03.)*
- G3 measured subset: CGP 49.2 (n=65); 52% below-median; 40% 2× rate; Informational Text −0.5 RIT vs overall. *(OneRoster pull.)*
- G2: 399 records / 176 students; slice mean RIT 193.6 (SY 2025-26 cohort: 185.5, n=60); CGP 55.5 (n=81); 63% meeting projection; 43.6% 2× rate; Informational weakest of the three 2–5 goals. *(OneRoster pulls 2026-06-25 / 2026-07-03.)*
- Per-grade tails (bank ~RIT 155–250): G2 floor largely closed (v4 reliable range reaches RIT 160); G3 floor binds; G4 mild ceiling; G5 ceiling binds badly (~20% of current G5 above RIT 235). *(Computed + External-review.)*
- STAAR G3.2022: 33 items, all MCQ; 18 results; ≤1 real student. *(OneRoster/QTI pull.)*
- MAP infrastructure: 386 MAP ALIs (120 Reading), 2017–2026, ~15 schools; 51 NWEA metadata fields per result; three Reading 2–5 goal areas in current terms. *(OneRoster pull.)*
- Bank: 650 operational items across 13 files (counted programmatically); b_provisional ≈ RIT 175–220; formats 265/102/90/76/63/54 (MCQ/seq/MSQ/gap/EBSR/hot-text). Staged: +92 edge (PR #30) and +44 standard-gap/super-ceiling (PR #35); the `load_bank()` build dedups to 786 harness-loadable unique items, b −4.45→+4.55 ≈ RIT 155–250, adoption pending calibration. *(Engine fixtures.)*
- Simulations (v4 run 2026-07-03: production path + randomesque, full 786-item bank, G2–G5 prior, TimeBack-parity configuration): r=0.967; RMSE 3.20; bias −0.04 RIT; reliability 0.931; SEM 3.14; blueprint 100% (±1 vs 14/13/13); TEI floor 100% (mean 16.2); 0 divergences in ~17,900 sessions; reliable range RIT 160–230; robustness to σ=1.0. *(The v4 validation report in the engine repository — authoritative.)*
- NWEA: Rasch; MLEF + 3.8-logit fence; example blueprint 13/13/13 (Table 3.2); 40–43 items (test description); reliability 0.96; CSEM 3.3–3.6; 2025 norms G3 185/194. *(MAP Growth Technical Report for 2024–2025; 2025 Norms quick reference.)*

Sources: NWEA (2026) *MAP Growth Technical Report for 2024–2025*; NWEA (2025) *2025 MAP Growth Norms*; Han (2016) *Applied Psychological Measurement 40*(4) 289–301; Rasch (1960); Kingsbury & Zara (1989); Wright & Stone (1979); Linacre (1994); Stocking (1994); Kolen & Brennan (2014); AERA/APA/NCME (2014); Black & Wiliam (1998); Kingston & Nash (2011); Wise & DeMars (2005). Full APA list: the Sources tab.

## Experts

The external authorities the design's measurement stance inherits from:

- **Georg Rasch** — *Probabilistic Models for Some Intelligence and Attainment Tests* (1960). The measurement model; the equal-interval, sample-free construction the RIT scale inherits.
- **Kyung T. Han** — MLEF (2016). The exact scoring algorithm MAP documents, including the fence mechanism the engine replicates.
- **G. Gage Kingsbury & Anthony Zara** — CAT item-selection procedures (1989). The Fisher-information selection-with-constraints design.
- **Benjamin Wright & Mark Stone** — *Best Test Design* (1979). Calibration sample-size discipline; why pre-pilot b values are provisional by definition.
- **John M. Linacre** — item-calibration stability (1994). The N-per-item targets behind the pilot size.
- **Martha Stocking** — item-pool sizing (1994). The 6×–10× pool-to-test floor the 650-item bank clears.
- **Michael Kolen & Robert Brennan** — *Test Equating, Scaling, and Linking* (2014). The concurrent-study and linear-linking design, sample sizes, and error bounds.
- **AERA/APA/NCME** — *Standards for Educational and Psychological Testing* (2014). The validity framework, including response-process validity (Standard 1.13) behind the MAP-like UI decision.
- **Steven Wise & Christine DeMars** — test-taker disengagement (2005). The rapid-guessing validity threat the telemetry mirrors.
- **Paul Black & Dylan Wiliam; Neal Kingston & Brooke Nash** — formative/interim assessment effects. The bounded instructional-mechanism claim.
- **NWEA / HMH** — *MAP Growth Technical Report for 2024–2025*; *2025 Norms*. The primary source every parity claim traces to.
- **The Alpha growth-program owner** — Alpha growth-program framing (2× target; MAP as the accountability metric). The internal decision context this instrument serves.

## Locked decisions (the floor every version of the plan agrees on)

| Decision | Ruling | Why locked |
| :---- | :---- | :---- |
| **Delivery model** | Adaptive CAT, not fixed form | A 40-item fixed form cannot span RIT ~161–227 with SEM ≤ 4 (SPOV5); the fixed-form G3 spec is superseded on the record |
| **IRT model** | Rasch 1PL | MAP's stated model; the only model honest with zero response data (SPOV4) |
| **Scoring** | MLEF, 3.8-logit fence; EAP cold-start for first 2 items only | Verbatim NWEA-verified design (TR Equations 10–11) |
| **Blueprint** | 14/13/13 Literary/Informational/Vocabulary = 40 scored, extending to 43 for precision; SE stop 0.35 at ≥40 items; TEI floor ≥12 (gap-match counted) | TR Table 3.2 is an *example* 13/13/13 blueprint; the test description states 40–43 questions. TimeBack's operational split, identical across both Alpha engines [AUTHORING-DECISION; NWEA-VERIFIED for 40–43]; supersedes both the earlier 45/40/15 assumption and the pre-parity 13/13/13 / 39-scored / SE 0.30 / TEI 15 configuration |
| **Formats** | Six interactions, with Reading-specific confirmation status disclosed per format | TR §4; disclosure beats overclaim (SPOV2) |
| **EBSR scoring** | Partial credit 0/1/2 — a disclosed deviation from the TR's dichotomous rule | Preserves partial-response information; flagged as authoring decision, never claimed as parity |
| **Testing conventions** | Untimed, forward-only, answer-before-advance | MAP is an untimed power test; conventions are part of the measured construct |
| **Claims gate** | RIT/percentile/CGP output blocked in code until concurrent linking passes (r ≥ 0.80, mean diff < 5 RIT, held-out) | The claims ladder is enforced where drift can't reach it (SPOV3) |
| **Item quality gate** | A 14-dimension quality check with a ≥0.85 pass threshold before bank entry | Text-dependence, near-neighbor distractors, CCSS alignment, Lexile matching — pre-empirical floor |
| **Norms reference** | 2025 norms (G3 185/194, growth ~9) | Current NWEA reference; norm year stated on every norm-referenced number |
| **UI stance** | MAP-like conventions; no replica claims; trademark disclaimer; legal review before external use | Response-process validity without the IP exposure the audit flagged |
| **Pilot shape** | Stage 2: ~40-student feasibility pilot (1–2 classes; usability, engagement, early red flags — no calibration claims), with calibration accruing from regular use (~300-student-equivalent response volume for the core band) → Stage 3: N≥1,000 concurrent pairs accrued via usage within 2 weeks of official Fall 2026 MAP | ~1,600 pilot responses cannot calibrate a 786-item bank; honesty demands the feasibility framing; Kolen–Brennan sample-size and design requirements govern the linking stage; Alpha's calendar makes it schedulable (SPOV7) |

## Open forks (still under debate)

These are genuine judgment calls for the group, not blockers.

- **Q1 — Product name.** "MAP Proxy" uses HMH's registered mark. **Direction set:** rename before anything external; internal pilot may proceed under the working name pending counsel. **Still open:** the new name, and whether "MAP-aligned" is safe in marketing copy. *Confidence: high that rename is needed; the name itself is open.*
- **Q2 — EBSR scoring alignment.** Keep partial credit (more information per item) vs. switch to MAP's dichotomous rule (tighter parity for linking). **Pre-committed (no longer a judgment call at readout time):** the pilot scores EBSR both ways in parallel (comparator built — engine PR #33); the decision statistic is the mean absolute linking-residual difference on EBSR-heavy (≥3 EBSR) sessions with a bootstrap 95% CI; dichotomous wins if its residuals are lower with the CI excluding zero — decided *before* RIT unlock. Note the PCM Δ=0.5 step also affects item *selection*, not just scoring — flagged for the item-fit analysis. *Confidence: high on the procedure; the outcome is the data's call.*
- **Q3 — G2 form target.** Alpha's G2 records split across MAP K–2 (4 goal areas) and Reading 2–5 (3 areas). The proxy is built to 2–5. **Recommend:** stay 2–5-only; below-floor G2 students route to the K–2 official instrument rather than a stretched proxy. *Confidence: medium.*
- **Q4 — Linking method.** Linear equating (lower barrier) vs. concurrent calibration with NWEA anchor items (superior, needs a data-sharing agreement). **Direction set:** linear first; anchor-item negotiation is an org call, not a design one. *Confidence: high.*
- **Q5 — Exposure control post-pilot.** Randomesque top-5 selection now ships in both selection phases; on the full 786-item bank never-used items are 289 (they rose with the larger bank) and 38 remain over-exposed — per-band exposure balancing is the open follow-up. Topic caps + randomesque vs. Sympson–Hetter item-level caps, and a proposed per-standard session cap (max 2 items/standard — PR #35, not shipped). **Stays open** until pilot exposure data exists. *Confidence: medium.*

## Honest ceiling / measurement discipline

**Honest ceiling.** Pre-linking, the instrument cannot produce a RIT, a percentile, or a CGP — and does not. Simulated reliability (0.931, v4) meets our ≥0.93 target but still sits below MAP's published 0.96 operational bar; the [−10.0, +10.0] RIT limits of agreement come from an internal cross-bank consistency check against a synthetic bank — explicitly not MAP agreement. If the Rasch model is misspecified for our items, every simulated figure is optimistic. **Lead the case on the measured problem** — a 46th-percentile population with a real low tail, the growth-velocity blind spot, the unused incumbent, the domain diagnosis — and treat scale-linked equivalence as the post-pilot target, not a present fact.

**Measurement discipline.** The calibration loop, item retirement, and any proxy→MAP mapping run observe-only until in-cohort paired data exists to check them against. When it does: validate the tails (the G2 floor and Alpha's high-RIT ceiling), not just the core band; disaggregate by campus and subgroup before any network claim; and treat a linking correlation below 0.70 as a published kill criterion, not a footnote. No "proven," no "MAP-equivalent," no growth multiple before the pilot reads out.

## Dropped approaches (with rationale)

| Approach | Reason dropped |
| :---- | :---- |
| Fixed-form 40-item G3 exam (the original spec) | Cannot span G2–G5 with SEM ≤ 4 in 39 items; superseded by the CAT on the record |
| 3PL IRT model | Discrimination/guessing parameters cannot be estimated with zero response data — would be invented, not measured |
| EAP scoring throughout | Prior-dependent shrinkage biases extreme scores; MLEF is MAP's documented method (EAP kept only as 2-item cold-start) |
| 45/40/15 domain weights | Superseded by NWEA TR Table 3.2's published equal thirds — our own earlier assumption, corrected against the primary source |
| "Five formats" constraint | Superseded by the TR's format documentation (EBSR/composite was missing from the old list) |
| Approximate RIT output (200 + 10θ) pre-linking | The transformation's coefficients are exactly what the linking study estimates; emitting the approximation would be the overclaim the design exists to prevent |
| "Pixel-accurate MAP replica" UI framing | Written admission of scraping a registered trademark's assets; replaced with MAP-like conventions + disclaimer; legal review gate added |
| Pricing / market-size / competitor claims in approval documents | Two audit-contradicted figures ($28/student; "competitors are fixed-form"); approval case is facts-only by decision |
| Timed sections | MAP is an untimed power test; a clock changes the construct and rewards the rapid-guessing MAP penalizes |
| Public no-login test URL (as shipped) | 650-item bank farmable by anonymous sessions; gated behind a flag before pilot |

---

*Word count: ~3,300 — under the 10,000-word cap.*
