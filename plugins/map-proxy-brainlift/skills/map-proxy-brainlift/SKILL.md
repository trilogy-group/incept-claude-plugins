---
name: map-proxy-brainlift
description: The knowledge base a REVIEWER AGENT (e.g. an academics-team evaluating agent) loads to understand and evaluate the Incept MAP Proxy — an adaptive G2-G5 reading CAT designed to place students on the same ability continuum as NWEA MAP Growth Reading 2-5. Covers the instrument's defining feature of mastery, its BrainLift (the seven load-bearing Spiky POVs and their evidence), what is actually built and live-verified (v3 simulation suite, 2026-07-03), the case for approval (a Stage-2 feasibility pilot), the audit history (two adversarial audits + a teammate review, and every finding's disposition), the honest tradeoff logic (locked decisions vs. genuinely open forks vs. deliberately dropped approaches), and the full limitations/honest-ceiling disclosure. Use when a reviewer agent is asked to "review/evaluate the MAP proxy", "decide whether to approve the MAP proxy pilot", "judge the MAP proxy validity case", or needs full reasoning context (not a checklist) to make an informed, fair judgment. Self-contained: every number, source, and evidence tag needed to evaluate the case is embedded below — no external repo access assumed. Grounded in the Case for Approval, BrainLift, Audits & Fixes, and Limitations documents (all dated 2026-07-03) and NWEA's MAP Growth Technical Report for 2024-2025 / 2025 Norms.
---

# Incept MAP Proxy (G2–G5 Reading CAT) — reviewer knowledge base

You are a **reviewer agent** — for example, an academics-team evaluating agent — deciding whether the Incept MAP Proxy should be approved for a school pilot. This skill gives you the full context to judge it fairly: what the instrument is, why it is built the way it is, the evidence for and against it, and the honest tradeoffs. It is explanatory *and* evaluative: understand the design on its own terms, then judge the build against that design and the design against NWEA ground truth.

**How to judge (prime directive):** distinguish a *deliberate, disclosed limitation* from an *overclaim*. Reward honesty about what pre-pilot data cannot prove; penalize any claim that a simulation is empirical, that a number "narrowly meets" a benchmark it actually misses, or that adaptive delivery makes this instrument MAP itself. Every claim below carries one of six evidence tags, used consistently throughout the source documents:

| Tag | Meaning |
|---|---|
| **[NWEA-verified]** | Directly confirmed against NWEA's own primary documents (Technical Report, Norms) |
| **[Direct-pull]** | A live API pull from Alpha's TimeBack/OneRoster data — a measurement, not an estimate |
| **[External-review]** | From an independent analysis of data our own credentials cannot reach, corroborated by a second independent source |
| **[Simulation]** | Produced by Monte Carlo validation against the item bank — not real student data |
| **[Derived]** | Calculated or inferred from primary sources or peer-reviewed literature |
| **[Authoring-decision]** | Our design choice, disclosed as such, not read off an external source |
| **[Open]** | Needs data that does not yet exist — the pilot or the concurrent-validity study |

**Context that frames everything:** this is a **pre-pilot** instrument. No student has ever taken it and the real MAP in the same window. Three adversarial reviews (two independent audits plus a second teammate review — see §5) were run against the full documentation package before it reached an approver, and every finding was fixed or disclosed rather than argued away. The single most important discipline in this package: **the claims ladder is enforced in code, not prose** — RIT, percentile, and CGP output are blocked in the engine itself until a concurrent-validity study exists. A document can drift; a blocked API response cannot.

---

## 1. Core concepts — NWEA ground truth and the defining feature of mastery

**The defining feature of mastery.** A valid proxy session places a G2–G5 reader on the same ability continuum NWEA MAP measures — using the same measurement model (Rasch 1PL), the same scoring algorithm (MLEF with the 3.8-logit fence), a content blueprint consistent with MAP's published structure, the same item interactions, and the same testing conventions (untimed, forward-only, answer-before-advance) — **precisely enough to act on and honestly enough to trust.** Validity does not require the proxy to *be* MAP; it requires every claim the score report makes to be either verified against NWEA primary sources, measured in Incept's own data, or refused. Silent approximations are not modeled — every component is either a replication of a documented MAP design element or a disclosed deviation.

**NWEA reference facts** [NWEA-verified unless noted]:

| Fact | Value |
|---|---|
| Measurement model | Rasch 1PL — "scaling is accomplished using the Rasch model" |
| Scoring algorithm | MLEF (Han 2016), 3.8-logit fence, verbatim (TR Equations 10–11) |
| Blueprint | TR Table 3.2 shows an **example** blueprint of 13 Literary/13 Informational/13 Vocabulary + up to 4 field-test items — not a published requirement. The public test description separately states **40–43 questions**. |
| Domains | Exactly three: Literary Text · Informational Text · Vocabulary & Word Meaning (K–2 has four — do not confuse them) |
| Item formats confirmed in Reading 2–5 specifically | MCQ, multi-select, and composite (EBSR) — confirmed in Reading figures. Hot-text and drag-and-drop are documented for MAP Growth more broadly (other subjects' figures). Gap-match appears only in NWEA secondary materials. **Only 3 of 6 formats are Reading-2–5-confirmed; do not present all six as equally confirmed.** |
| Published quality bar | Marginal reliability **0.96** (G2–5 Reading, Table 7.7); CSEM ≈ **3.3–3.6 RIT** (Table 7.5) |
| 2025 norms (effective 2025–26) | G2 170.1→181.7 · **G3 184.7→193.8 (~9 RIT growth)** · G4 195.9→202.1 · G5 203.7→208.4. A 1–3 RIT downward shift vs. 2020 norms; the RIT scale itself is unchanged. Alpha's stored MAP metadata still carries `normsreferencedata: "2020"` — every norm-referenced number must state its norm year. |
| Untimed, forward-only | A power test — no clock, once an item is answered it is locked |
| RIT scale | `RIT = a·θ + c` — NWEA's proprietary, unpublished linear transform. Recoverable only via paired-score regression (same students, both tests, same window) |

**Two corrections worth naming explicitly, because catching them is itself evidence of rigor:** the domain blueprint was originally an authoring guess of 45/40/15 before NWEA's actual Table 3.2 was located; and the original "five item formats" list was missing EBSR/composite entirely. Both were corrected against primary sources, not defended.

---

## 2. The BrainLift — the seven load-bearing positions (DOK4 Spiky POVs)

Every other section of this skill derives from these seven positions.

**SPOV1 — Measurement cadence is the #1 problem, not curriculum.** The full current G3 population is **n≈915, mean RIT 196.0, 46th percentile** [External-review, corroborated independently]. Alpha's own OneRoster data slice is coverage-biased (mean percentile ~74 in every grade); the earlier "206.4 ≈ 72nd percentile" framing is **retired** — see §5, finding 1. Even the platform's high-achieving *measured subset* grows below median at G3 (CGP 49.2, n=65), and the fall baseline hasn't moved in eight years. The binding constraint is that growth velocity is measured only 2–3 times a year, so every instructional correction is a season late. **The re-baselining sharpens the case, not weakens it**: a 46th-percentile population with a real low tail needs interim measurement more than a coasting 72nd-percentile one ever did.

**SPOV2 — Replicate MAP's published machinery exactly; approximate nothing silently.** Every measurement-design choice traces to NWEA's own Technical Report — Rasch 1PL, MLEF with the verbatim fence, a blueprint anchored to what NWEA actually publishes (not an authoring guess). Where the engine deviates (EBSR partial credit vs. the TR's dichotomous scoring), the deviation is disclosed and argued, never passed off as parity. Each element was re-verified against the actual TR PDF in July 2026, including by an adversarial fact-check agent instructed to refute the claims.

**SPOV3 — The claims ladder is enforced in code, not prose.** Pre-pilot output is logit ± SE and domain sub-scores; RIT, percentile, and CGP are blocked in the engine itself. A teacher cannot misread a score report into a RIT claim because the number does not exist in the API response. The two audits found number-drift in *documents* (0.930 vs. 0.928 reliability) — exactly why the load-bearing gate lives in code, where drift can't reach it.

**SPOV4 — Rasch 1PL is the only honest pre-pilot model.** 3PL requires estimating discrimination and guessing parameters from ≥1,000 responses per item that do not exist pre-pilot; using 3PL now would mean inventing parameters and calling them measurement. Rasch requires only difficulty, which can be provisionally assigned and empirically corrected later — and it is MAP's own stated model. The robustness simulation shows the engine tolerates provisional-parameter error to σ=1.0 logits without reliability collapsing below 0.85.

**SPOV5 — Adaptive or nothing for a cross-grade instrument.** A fixed 40-item form cannot measure RIT ~161–227 (G2 fall through G5 spring) with SEM ≤ 4 — items informative for a struggling G2 reader are noise for an advanced G5 reader. This is arithmetic (Fisher information concentrates near |θ−b|≈0), not preference. The original fixed-form G3 design was superseded for this reason, on the record. MAP itself is adaptive for the same reason.

**SPOV6 — Format familiarity is measurement hygiene, not test prep.** Alpha students currently practice on 100% MCQ material; their first multi-select or two-part evidence item would otherwise be on the scored official MAP. Interface novelty is construct-irrelevant variance (AERA/APA/NCME Standard 1.13). This is why the UI is deliberately "MAP-like" (familiar conventions) rather than a claimed replica — see §5, finding 6, for why that framing changed.

**SPOV7 — Alpha is the linking lab; anywhere else it's a partnership hunt.** Concurrent validity requires the same students taking both tests within two weeks. Alpha already administers official MAP network-wide (386 assessment line items since 2017) [Direct-pull], and proxy results already land in the same OneRoster gradebook via Caliper. The Stage-3 linking study is therefore a scheduling decision inside an existing testing calendar, not a research-partnership hunt — the only missing piece is a student-ID crosswalk (provisioning work, not research).

**Key derived insights (DOK3), condensed:**
- **Two products, one engine, staged.** Pre-linking: an interim diagnostic (logit growth curves, domain sub-scores, engagement flags). Post-linking: a RIT-scale proxy (percentile, CGP-style growth, historical comparability). Neither stage borrows the other's claims.
- **The pilot is designed to resolve precision, not guaranteed to.** The v3 run closed the two flagged v1 issues (RMSE, bias — see §3), leaving one reported gap (reliability 0.929 vs. ≥0.93) and a residual band-level bias, both root-caused to expert-assigned difficulty parameters. Empirical calibration accrued from regular use is the closer — this is exactly why the ask is real usage, not more simulation.
- **Domain sub-scores match what the platform already stores** — Alpha's MAP imports carry the same three Reading 2–5 goal areas in OneRoster metadata, so per-domain history (including the documented weak domain, Informational Text) is queryable across proxy and official MAP in one structure.
- **Bank economics bind at the edges, and the edges differ by grade** — not at the average. See §3.

---

## 3. What is actually built (live-verified, v3 run 2026-07-03 — authoritative)

**Live artifacts:**

| Artifact | Status |
|---|---|
| Adaptive engine | Live on Cloud Run — Fisher-information CAT, domain quotas, Rasch 1PL, MLEF with 3.8-logit fence |
| Operational item bank | **650 items**, 13 fixture files, provisional difficulties ≈ RIT 175–220 — this is what the v3 validation ran against |
| Staged bank expansions | +92 edge items (floor to ~RIT 155, ceiling to 235) and +44 items (26 standard-gap + 18 G5 super-ceiling, RIT 231–250) — merged and harness-loadable, giving **766 items** total, b −4.45→+4.55 ≈ RIT 155–245. Adoption into the *production* bank is a reviewable decision pending calibration — do not present 766 as the currently-scored bank. |
| Item formats | 6 (see §1 for which 3 are Reading-2–5-confirmed) |
| Quality gate | 14-dimension quality check, ≥0.85 pass threshold, before any item enters the bank (text-dependence ablation, CCSS alignment, near-neighbor distractors, Lexile-to-band matching) |
| Session structure | **14 Literary / 13 Informational / 13 Vocabulary = 40 scored items**, extending to 43 for precision; SE stop 0.35 evaluated only at ≥40 items — the TimeBack-parity operational blueprint, disclosed as distinct from NWEA's example 13/13/13 |
| TEI floor | ≥12 technology-enhanced items per session (gap-match counted), enforced at the assembled-session level, not just an authoring target |
| TimeBack integration | Live in staging — Cognito SSO login, Caliper gradebook events, course registered under Alpha School |
| Score output | Logit θ ± SE only, plus 3 domain sub-scores; RIT is code-blocked pre-linking. The reported SE is **b-uncertainty-adjusted** (Fisher SE × 1.08 under v3, `se_basis`-labeled) because plain Fisher SE understates uncertainty from unconverted provisional b-values — the inflation removes itself automatically once empirical calibration lands. |

**v3 simulation results** (production selection path + randomesque exposure control, 650 items, G2–G5 prior, ~17,900 sessions across 7 studies) — report every miss alongside every hit:

| Metric | v3 result | Benchmark | Verdict |
|---|---|---|---|
| Theta recovery r | **0.963** | ≥0.90 | Meets |
| RMSE | **3.44 RIT** | <4.0 RIT | Meets |
| Systematic bias | **−0.38 RIT** (reliable-range −0.27; max per-band 0.83) | \|bias\|<0.5 overall, ≤1.5 per band | Meets |
| SEM (core band) | **3.18 RIT** | ≤4.0 RIT (MAP's published CSEM: 3.3–3.6) | Meets |
| Marginal reliability | **0.929** | ≥0.93 target; MAP published: 0.96 | **0.001 short — the one reported gap** |
| Blueprint adherence | **100%** (±1 vs. 14/13/13) | 100% | Meets |
| TEI floor met | **100% of sessions** (mean 16.2 ≥ 12) | 100% | Meets |
| Internal cross-bank consistency (synthetic, **not MAP agreement**) | r=0.912, 95% LoA [−10.7, +10.2] RIT | r≥0.85 | Meets, with synthetic-bank caveats |
| Robustness to parameter error | reliability ≥0.915 through σ=1.0 logits | ≥0.85 | Meets |
| MLEF divergences | **0 / ~17,900 sessions** | 0 | Meets |
| Reliable measurement range | **RIT 181–227** | — | Scoped honestly; G2 fall median (~170) sits below it |

**Report the history, not just the final table — it is itself evidence of rigor.** The first production-path run (v1, 2026-07-02) *regressed* RMSE to 4.73 and surfaced a **+2.62 RIT systematic overestimate**, and both were published rather than hidden. Root-cause (v2): the bias lived in the Owen running estimate's prior shrinkage, not in the shipped score; re-basing the final score on the engine's actual MLEF value removed it (bias fell to −0.46, RMSE to 3.70). v3 re-validates everything under the TimeBack-parity configuration with randomesque exposure control, landing at RMSE 3.44 / bias −0.38. **A reviewer should treat this progression as a strength (the team found and fixed its own regression) — not soften it into "always been fine."**

**What is not yet resolved, stated plainly:**
- A residual **negative bias of −0.4 to −1.0 RIT in the RIT 175–190 bands** (worst: −1.04 at 175–180) — a scorer-only decomposition is the queued follow-up, not yet complete.
- Reliability sits **0.929 vs. the ≥0.93 target** (≈0.001 short) — and far below MAP's own published 0.96. Empirical calibration is the closer, not a documentation fix.
- **38/650 items exceed 30% exposure**; **241/650 are never used** in the v3 run (improved from 322 in v1 via randomesque selection, but not solved) — item security is weaker than NWEA's 40,000+-item pool allows.
- Two bank cells (`literary/171-180`, `informational/171-180`) remain **never served** by selection — a starvation issue, not a bank-size issue.

---

## 4. The case for approval — what's being asked, and on what basis

**The ask:** approve a **Stage-2 feasibility pilot** — **~40 students, 1–2 classes, one ~45-minute adaptive session each** — and approve in principle a Stage-3 linking study where students take the proxy within two weeks of their official Fall 2026 MAP sitting, with the N≥1,000 paired cohort accruing through regular use inside Alpha's existing MAP calendar (not a separate recruitment).

**The pilot is deliberately small, and the case says so.** ~40 students × ~40 items ≈ 1,600 responses against a 766-item bank — nowhere near the ~200 responses per item that calibration requires. **The pilot claims feasibility only** (completion rate, session duration, rapid-guess rates, teacher/student experience, early item red flags) — not calibration. Calibration accrues from regular use afterward, toward a ~300-student-equivalent response volume for the core band.

**The argument, in order:**
1. Alpha's current population sits near the 46th percentile with a real low tail, its growth signal is invisible between MAP windows — measurably, not rhetorically (§2 SPOV1) — and the only interim standardized instrument in the platform (STAAR G3.2022: 33 items, 100% MCQ, no domain sub-scores) has **18 result records, at most one a real student** [Direct-pull].
2. The instrument implements MAP's own published measurement design, verified against NWEA primary sources, and its adaptive engine passes its v3 simulation suite with every miss disclosed alongside every hit (§3).
3. Three adversarial reviews of this documentation package were run before it reached an approver, and every finding was fixed or disclosed (§5) — what a reviewer is evaluating has already survived the review a skeptical reader would give it.

**Three design commitments made in advance** (so the plan cannot be quietly re-scoped later):
- The 40-student pilot deliberately includes **≥8 below-median G2 readers and ≥8 above-median G5 readers** — floor/ceiling UX and flag behavior get tested even at this size.
- RIT unlock at Stage 3 is **band-aware**: the calibrated core band unlocks first; floor/ceiling-flagged scores stay logit-only until tail-targeted calibration reaches SE(b̂) ≤ 0.30 there too.
- The EBSR partial-credit-vs-dichotomous scoring question is **pre-committed** to a dual-scoring comparison with a named decision statistic (bootstrap 95% CI on mean absolute linking-residual difference), decided before RIT unlock — not left to be resolved ad hoc.

**What this case explicitly does not ask for:** a RIT-equivalence claim. There is no paired proxy↔MAP data yet, and the engine refuses to emit RIT scores until there is.

---

## 5. Audit history — what was found, and what changed (evidence the self-critique already happened)

Before this package reached an approver, **two independent adversarial audits** (one checking every number against the engine's own artifacts, one fact-checking every external claim against NWEA primary sources) plus **a second teammate review** were run against it. The highest-signal findings and their dispositions — treat a reviewer's job as verifying these are still true, not re-discovering them:

| # | What was found | What is now true |
|---|---|---|
| 1 | Population baseline (206.4 RIT / 72nd percentile) was a coverage-biased slice, not the full population | **Re-baselined**: full population is n=915, mean RIT 196.0, 46th percentile [External-review]. The old figure was a compound of repeat-record over-weighting (+5.4 RIT), cohort staleness, and — largest — OneRoster source-coverage bias (the batch import is itself a high-achieving slice, ~74th percentile in every grade, of a population sitting near 46th) |
| 2 | Reliability was reported as "0.930 ✅" against a 0.93 benchmark the underlying data actually showed as 0.928 (below) | Now stated honestly everywhere as **0.929** (v3), with MAP's own published 0.96 given as context |
| 3 | The one failing metric (RMSE 4.12) was omitted from summary tables | RMSE appears in every summary table now, including the v1 regression to 4.73 — the full history is reported, not just the final number |
| 4 | Item-bank source table summed to 520 while claiming 650 | Replaced with a programmatically-counted 13-file breakdown summing to exactly 650 |
| 5 | Simulations were G3-scoped (630 items, simplified selector) but described as "G2–G5, production code" | Re-run on the true production path, root-caused, and re-validated under TimeBack parity (v3) — all 650 items, G2–G5 prior |
| 6 | A section framed the UI as a "pixel-accurate replica" built by scraping NWEA's practice site — a legal liability presented as a selling point | Rewritten as **MAP-like UI**: familiar conventions justified by response-process validity (AERA Standard 1.13), with a trademark disclaimer and a legal-review gate before external use |
| 7 | "$28/student," "competitors are fixed-form," "open-source engine" — each contradicted by public evidence | All removed; the approval case carries no pricing and no competitive claims |
| 8 | "All six formats confirmed in MAP Reading 2–5" overstated the source | Bounded: 3 formats confirmed Reading-specific, 3 documented more broadly — see §1 |
| 9 | Concurrent-study cohort size stated as N=100–200 in one file and N=1,000 in another | N ≥ 1,000, consistent everywhere |
| 10 | A public no-login test URL allowed anonymous farming of the item bank | Gated behind a `PUBLIC_TEST_ENABLED` flag (default off) |
| 11 | A single RIT-unlock gate would have hidden tail unreliability | Pre-committed to core-band-first, band-aware unlock (§4) |
| 12 | "The pilot fixes exactly that [precision gap]" overclaimed what a study can promise | Reworded: the plan is *designed* to resolve it; simulation supports but cannot guarantee it |
| 13 | The internal cross-bank consistency simulation read as MAP-agreement evidence | Relabeled explicitly as "internal cross-bank consistency (synthetic)" — not MAP agreement |
| 14 | Pool-to-test ratio quoted two ways (16.7× vs. 1.7×) without reconciling them | Both framings now stated together everywhere: 650/40 = 16.3× session length; 1.6× vs. Stocking's 10× recommended floor |
| 15 | Format-familiarization benefit was implied for all six formats | Bounded: strongest for the 3 Reading-2–5-confirmed formats; the other 3 are low-harm additional practice, not a claimed prep benefit |
| 16 | Distribution (being enrolled in TimeBack) was treated as equivalent to adoption | Argued, not assumed — the empty STAAR slot (18 results, ≤1 real student) is the explicit cautionary tale; pilot success/kill criteria are completion-rate based |

**The discipline this demonstrates:** any claim that would embarrass the team if independently checked *was* checked, by an agent instructed to try to break it. A reviewer should spend less time re-deriving these numbers and more time confirming the disclosed gaps (§3, §6) haven't quietly been re-softened in a newer document.

---

## 6. Honest ceiling and limitations (the load-bearing disclosure)

**The single most defensible remaining critique, stated by the team itself:** every psychometric result in this package is either design parity (verified against NWEA documents) or simulation. **None of it is yet empirical.** The b-parameters are expert-assigned; the reliability and RMSE figures assume the Rasch model is correctly specified; the internal cross-bank consistency check used a synthetic bank, not real NWEA items. **If the Rasch model is misspecified for these items, every simulated figure is optimistic.** This is the gap between a demonstrably-right design and a proven instrument, and no amount of additional documentation closes it — only the pilot and the concurrent-validity study can.

**Limitations, condensed (full detail in the source Limitations document):**

| # | Limitation | Current state |
|---|---|---|
| 1 | b-values are expert-assigned, not calibrated; SE(b̂) effectively infinite pre-pilot | Score reports emit a b-uncertainty-adjusted SE (×1.08) that self-removes post-calibration |
| 2 | Residual band-level bias + reliability gap | −0.4 to −1.0 RIT bias in RIT 175–190 bands; reliability 0.929 vs. 0.93 target — both traced to the same root cause (provisional b-values under a wide prior); scorer-only decomposition (S12) queued |
| 3 | RIT output blocked — no scale linking yet | The single most significant commercial limitation; deliberate, per SPOV3 |
| 4 | No concurrent validity data exists | The core cross-bank "consistency" number (r=0.912) is a synthetic-bank check, explicitly not MAP-agreement evidence |
| 5 | G2 items are the thinnest and least-validated band | Floor expansion to ~RIT 155 merged but not yet adopted into the production bank; sub-155 students route to the official K–2 MAP instrument as an explicit, owned boundary |
| 6 | All simulations assume Rasch is correctly specified | Real responses may show discrimination variability, guessing floors, multidimensionality, or fatigue effects — none modeled; post-field-trial item-fit analysis is the check |
| 7 | 650 (or 766 harness-loadable) items vs. NWEA's 40,000+ | Weaker item security (29.4% mean pairwise session overlap), limited fine-grained within-standard discrimination — disclosed as a scope limit, not a validity defect |
| 8 | Original simulation scope (G3-only, closed-form selector) understated production-path effects | Complete — v3 runs the real production selection code end-to-end |

**Known vs. unknown, the honest summary:** the algorithm ranks students correctly (known, r=0.963) and is reliable at the core range (known, 0.929) — but whether the Rasch model is correctly specified is *assumed*, whether score X on the proxy equals score X on MAP is *unknown* until the concurrent study, and whether the test is free of demographic bias (DIF) is *unknown* until N=5,000 with a diverse sample. **A reviewer should treat "known" and "assumed"/"unknown" as different categories throughout this package, not synonyms for "the numbers look fine."**

---

## 7. Tradeoff logic — locked decisions, genuinely open forks, and deliberately dropped approaches

**Locked (the floor every version of the plan agrees on) — do not relitigate these as if they were undecided:**

| Decision | Why locked |
|---|---|
| Adaptive CAT, not fixed form | A 40-item fixed form cannot span RIT ~161–227 with SEM ≤ 4 (SPOV5) |
| Rasch 1PL | MAP's stated model; the only model honest with zero response data (SPOV4) |
| MLEF scoring, 3.8-logit fence; EAP cold-start for first 2 items only | Verbatim NWEA-verified design |
| 14/13/13 blueprint = 40 scored, extending to 43; SE stop 0.35 at ≥40 items; TEI floor ≥12 | TR Table 3.2 is an *example* 13/13/13, not a requirement; TimeBack's operational split is disclosed as an authoring decision, consistent with NWEA's published 40–43 structure |
| Six formats, with per-format confirmation status disclosed | Disclosure beats overclaim (SPOV2) |
| EBSR partial credit (0/1/2) | A disclosed deviation from the TR's dichotomous rule, preserving partial-response information |
| Untimed, forward-only, answer-before-advance | Part of the measured construct, not just a UX choice |
| RIT/percentile/CGP output blocked in code until linking passes (r≥0.80, mean diff <5 RIT, held out) | The claims ladder enforced where drift can't reach it (SPOV3) |
| 2025 norms as the reference | Current NWEA reference; norm year must be stated on every norm-referenced number |
| MAP-like UI, no replica claims, trademark disclaimer, legal review before external use | Response-process validity without the IP exposure the audit flagged |

**Genuinely open forks — real judgment calls, not blockers, and not yet decided:**

- **Q1 — Product name.** "MAP Proxy" uses HMH's registered mark. Direction is set (rename before anything external; internal pilot may proceed under the working name pending counsel) but the new name itself is open. *A reviewer evaluating this skill itself should note it currently uses the working name "Incept MAP Proxy" throughout, per that same pending-counsel allowance — not as a final naming decision.*
- **Q2 — EBSR scoring alignment.** Partial credit vs. MAP's dichotomous rule — the *procedure* to decide is pre-committed (dual-scoring comparator, named decision statistic, decided before RIT unlock), but the outcome is the data's call, not yet known.
- **Q3 — G2 form target.** Alpha's G2 records split across MAP K–2 (4 goal areas) and Reading 2–5 (3 areas); the proxy is built to 2–5 only. Current lean: stay 2–5-only, route below-floor G2 students to the official K–2 instrument. Medium confidence — genuinely open.
- **Q4 — Linking method.** Linear equating (lower barrier, direction set) vs. concurrent calibration with NWEA anchor items (superior, needs a data-sharing agreement — an org call, not a design one).
- **Q5 — Post-pilot exposure control.** Randomesque selection ships now (never-used items down 322→241); whether to add Sympson-Hetter item-level caps and/or a per-standard session cap stays open until real pilot exposure data exists.

**Deliberately dropped — re-proposing any of these is a regression, not a fresh idea:**

| Dropped approach | Why |
|---|---|
| Fixed-form 40-item G3 exam (the original spec) | Cannot span G2–G5 with SEM ≤ 4 in 39 items |
| 3PL IRT model | Would invent, not measure, discrimination/guessing parameters with zero response data |
| EAP scoring throughout | Prior-dependent shrinkage biases extreme scores; kept only as a 2-item cold-start |
| 45/40/15 domain weights | Superseded by NWEA's actual Table 3.2 once located — the team's own earlier assumption, corrected |
| "Five formats" constraint | Missing EBSR/composite entirely; superseded by the TR's actual format documentation |
| Approximate RIT output (200+10θ) pre-linking | The transform's coefficients are exactly what the linking study is for — emitting an approximation would be the overclaim the design exists to prevent |
| "Pixel-accurate MAP replica" UI framing | A written admission of scraping a registered trademark's assets |
| Pricing / market-size / competitor claims in approval documents | Two figures were audit-contradicted ($28/student; "competitors are fixed-form"); the approval case is now facts-only by decision |
| Timed sections | MAP is an untimed power test; a clock changes the construct being measured |
| Public no-login test URL, unshipped | Farmable by anonymous sessions; gated behind a flag before pilot |

**Name the seam a reviewer should resolve:** whether this package is honestly framed as "design parity + simulation-validated algorithm, real-world equivalence explicitly Open" — or whether any newer document has let a flagged number (the 175–190 band bias, the 0.929 reliability, the synthetic-bank LoA) or an unearned phrase ("proven," "MAP-equivalent," a specific RIT projection) slip back in unqualified. Given the audit history in §5, the correct default assumption is that the current package is honest — the reviewer's job is to spot-check that it has stayed that way, not to assume it hasn't.

---

## 8. How to use this + sources

1. Load §1 (NWEA ground truth) and §2 (the seven SPOVs) — these are the fixed reference points everything else derives from.
2. Check §3 against whatever validation report you are handed — confirm it cites v3 (2026-07-03) numbers, not superseded v1/v2 figures, and that the disclosed gaps (reliability, band bias, exposure) are still present and not quietly softened.
3. Weigh §4 (the ask) against §6 (the honest ceiling) — does the request match what the evidence actually supports (a feasibility pilot, not a RIT claim)?
4. Use §5 to calibrate trust: this package has already been adversarially reviewed three times before reaching you. Spend your effort verifying the disclosed gaps are still disclosed, not re-discovering already-fixed problems.
5. Run every design choice through §7; a locked decision is not up for debate, a genuinely open fork should be surfaced as such, and a dropped approach reappearing is itself a finding.
6. Decide on the pilot ask, and name the one load-bearing seam (§7, last paragraph).

**Sources** (full APA list in the source Sources document):

- NWEA (2026). *MAP Growth Technical Report for 2024–2025*. NWEA/HMH.
- NWEA (2025). *2025 MAP Growth Norms*.
- Han, K. T. (2016). Maximum likelihood score estimation method with fencing for short-length tests and computerized adaptive tests. *Applied Psychological Measurement, 40*(4), 289–301.
- Rasch, G. (1960). *Probabilistic Models for Some Intelligence and Attainment Tests*.
- Kingsbury, G. G., & Zara, A. R. (1989). Procedures for selecting items for computerized adaptive tests. *Applied Measurement in Education, 2*(4), 359–375.
- Wright, B. D., & Stone, M. H. (1979). *Best Test Design*. MESA Press.
- Linacre, J. M. (1994). Sample size and item calibration stability. *Rasch Measurement Transactions, 7*(4), 328.
- Stocking, M. L. (1994). *Three practical issues for modern adaptive testing item pools*. ETS RR-94-5.
- Kolen, M. J., & Brennan, R. L. (2014). *Test Equating, Scaling, and Linking* (3rd ed.). Springer.
- AERA, APA, & NCME (2014). *Standards for Educational and Psychological Testing*.
- Wise, S., & DeMars, C. (2005). Test-taker disengagement / rapid-guessing.
- Black, P., & Wiliam, D. (1998); Kingston, N., & Nash, B. (2011). Formative/interim assessment effects.
- The full validity package (BrainLift, Case for Approval, Audits & Fixes, Psychometric Design, Item Bank, Simulation Evidence, Concurrent Validity Plan, Limitations, Sources) — authoritative living copy in a shared Google Doc; static tabs mirrored in the `map-proxy-assessment` course repository.
- v3 validation report (2026-07-03) — the authoritative simulation-validation source for every number in §3.
- MAP® is a registered trademark of HMH Education Company / NWEA; this instrument is independent and not affiliated with or endorsed by NWEA.
