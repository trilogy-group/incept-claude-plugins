# MAP Proxy Adaptive Assessment — Validity Case
**Version:** 2.0 | **Date:** 2026-07-03 | **Status:** Pre-pilot (v4 TimeBack-parity validation, full 786-item bank)
**Audience:** Investors, board members, technical reviewers

---

## Executive Summary

The Incept MAP Proxy is a computer adaptive test (CAT) for reading ability in grades 2–5, designed to deliver the psychometric performance of the NWEA MAP Growth Reading assessment at lower cost and with immediate results. The proxy implements the same Item Response Theory model (Rasch 1PL), the same scoring algorithm (MLEF; Han 2016 [Han-2016]), the six item formats documented across MAP Growth (three of them confirmed in Reading 2–5 specifically), and a content blueprint consistent with MAP's published structure — NWEA's Technical Report Table 3.2 shows an *example* 13/13/13 blueprint and its public test description states 40–43 questions; the engine adopts TimeBack's operational 14/13/13 = 40-scored split, extending to 43 for precision [AUTHORING-DECISION; NWEA-VERIFIED for the 40–43 structure] — verified from NWEA's primary technical reports [NWEA-2025-TR].

**Three things we can already prove.** First, the CAT algorithm works: Monte Carlo simulations (2026-07-03 v4 run: production selection path + randomesque selection, full 786-item bank, G2–G5 prior, TimeBack-parity configuration) demonstrate theta recovery of r=0.967 against MAP's ≥0.90 benchmark, RMSE 3.20 RIT (within the <4.0 target), bias −0.04 RIT (near-eliminated, within the |bias|<0.5 criterion), and marginal reliability of 0.931 at the core ability range — meeting the ≥0.93 benchmark (MAP's published operational figure, 0.96, remains the higher bar). The earlier v1 production run's flagged RMSE 4.73 / bias +2.62 were root-caused (Owen running-estimate prior shrinkage) and resolved by re-basing the final score on the shipped MLEF value [SIMULATION]. Second, item quality is gated: all 650 items in the operational bank have passed a 14-dimension quality check with a ≥0.85 pass threshold before entering the bank [AUTHORING-DECISION]. Third, blueprint fidelity holds: 100% of simulated sessions landed within ±1 of the 14/13/13 domain quota on the 40-item scored form — Literary, Informational, and Vocabulary — and 100% met the ≥12 TEI floor (mean 16.2) [SIMULATION].

**One thing we still need to prove.** Concurrent validity — the claim that a student scoring X on our proxy would score X on the real MAP — requires a scale-linking study in which the same students take both tests within two weeks. This study is not yet complete; RIT output is intentionally blocked until it is. The path is a staged rollout: a ~40-student feasibility pilot (1–2 classes), item calibration accruing from regular use (a ~300-student-equivalent response volume for the core band), then a concurrent validity cohort of N≥1,000 paired sessions — accrued through usage at the Fall 2026 MAP window — to establish the RIT transformation.

**Why this matters.** NWEA MAP Growth costs approximately $13.50–$15.50 per student per year for MAP Growth alone (published NWEA pricing; full-suite bundles cost more) [DERIVED from public procurement/pricing documents], requires managed IT infrastructure, and returns results via the NWEA portal, typically next-day. No open-source, MAP-format-parity adaptive proxy on a RIT-like scale exists; established commercial adaptive diagnostics (iReady, Star Reading) exist but are closed, on their own scales, without MAP's format profile [DERIVED]. The Incept proxy targets the same psychometric output at under $3/student with results available immediately after the session, using a codebase that can be deployed in any web browser. The addressable market is every school that wants MAP-quality reading diagnostics without MAP's price and logistics.

---

## 1. What Problem This Solves

### 1.1 MAP Growth: what it measures and why it matters

NWEA MAP Growth is the dominant adaptive reading assessment for K–12 students in the United States [NWEA-2025-TR]. It measures student reading ability on a continuous, grade-independent RIT (Rasch Unit) scale, enabling growth tracking across school years without rescaling. A G3 RIT of 210 and a G5 RIT of 210 represent identical absolute reading ability — a property the RIT scale inherits from the Rasch model's equal-interval construction [Rasch-1960][NWEA-2025-TR].

MAP's key diagnostic output is the Conditional Growth Percentile (CGP): how much a student grew relative to academically matched peers (same prior RIT, same grade, same weeks of instruction). CGP is the honest measure of instructional effectiveness — it controls for starting ability and asks whether the student grew more or less than expected. No other widely deployed reading assessment offers this at scale.

### 1.2 The cost and logistics barrier

MAP Growth is sold as a district subscription. NWEA's publicly available pricing and partner agreements place the per-student cost at approximately $13.50–$15.50 per student per year for MAP Growth alone; full-suite bundles cost more [DERIVED from public procurement/pricing documents]. The assessment requires:

- A district technology agreement with NWEA
- Managed browser lockdown or NWEA's Secure Testing Browser
- Scheduling across IT-managed lab time or 1:1 devices
- Results returned via the NWEA portal, typically next-day

For charter networks, micro-schools, tutoring companies, and international schools without existing NWEA contracts, these requirements make MAP economically and operationally inaccessible.

### 1.3 The Incept proxy: same model, immediate results, under $3/student

The Incept proxy delivers:

- The same Rasch 1PL IRT model [NWEA-VERIFIED] MAP uses
- The same MLEF scoring algorithm [NWEA-VERIFIED] documented in NWEA's technical reports
- The six item formats documented across MAP Growth — MCQ, multi-select, and composite/EBSR confirmed in Reading 2–5 specifically [NWEA-VERIFIED]; hot-text, drag-and-drop, and gap-match from wider MAP Growth documentation (see §2.5)
- A 40–43-item adaptive form with a 14/13/13 domain split (TimeBack's operational blueprint, consistent with NWEA's published 40–43 structure) [AUTHORING-DECISION; NWEA-VERIFIED for 40–43]
- Immediate score output after the final item
- Deployment in any modern web browser, no managed infrastructure required

Pre-pilot cost is under $3/student including item generation, quality checks, and API serving. Post-pilot operational cost is projected at $1–2/student at scale [AUTHORING-DECISION; projection based on current infrastructure costs].

### 1.4 Market context

NWEA serves more than 13 million students annually across the United States [NWEA published figure]. The K–12 assessment market is estimated at $2.5–3.0 billion annually in the United States [DERIVED from EdTech market research]. MAP Growth holds the dominant position in adaptive reading and math assessment for grades K–12 [DERIVED]. No open-source, MAP-format-parity adaptive proxy on a RIT-like scale exists; established commercial adaptive diagnostics (iReady, Star Reading) exist but are closed, on their own scales, without MAP's format profile [DERIVED].

---

## 2. Design Decisions and Their Justification

### 2.1 40-item scored form, 14/13/13

NWEA's Technical Report Table 3.2 shows an *example* blueprint of 13/13/13 + up to 4 field-test items; NWEA's public test description states 40–43 questions [NWEA-VERIFIED]. The engine adopts TimeBack's operational split of 14/13/13 = 40 scored items, extending to 43 for precision — consistent with NWEA's published structure and identical across both Alpha engines [AUTHORING-DECISION; NWEA-VERIFIED for the 40–43 structure]:
- Literary Text: 14 items
- Informational Text: 13 items
- Vocabulary: 13 items

Engine constants: `ADAPTIVE_ITEMS_MIN` = 40 (scored floor before any stop), HARD_CAP = 43, with a precision-extension band at items 41–43 (SE stop 0.35, evaluated only at ≥40 items; quotas alone never stop the test) and a TEI floor of ≥12 (gap-match counted as TE).

The near-equal-thirds split was corrected from an earlier 45/40/15 authoring estimate after we located NWEA Tech Report 2025 Table 3.2 — the only published domain-weight example for MAP Reading 2–5 [NWEA-VERIFIED]. The decision record is preserved in the CAT Exam Spec tab, §3.2.

### 2.2 CAT not fixed-form

MAP Growth is a Constrained CAT: after each response, the engine re-estimates student ability (θ) and selects the next item to maximize measurement precision, subject to content-area quotas [Kingsbury-1989]. A fixed-form cannot:

1. Measure students across the full G2–G5 ability range (RIT 161–227) in 40 items
2. Achieve MAP's published SE ≤ 3–4 RIT across the operational range [NWEA-2025-TR]
3. Track growth meaningfully when the same items are administered repeatedly

Our engine implements a true Fisher-information CAT with domain quota enforcement and shadow-test feasibility checking. The earlier fixed-form G3 exam design has been superseded.

### 2.3 Rasch 1PL model — why not 3PL

The 3-parameter logistic (3PL) model estimates item discrimination (a) and pseudo-guessing (c) in addition to difficulty (b). MAP Growth's Technical Report specifies the Rasch 1PL as its calibration model [NWEA-VERIFIED; NWEA-2025-TR]. Without at least 1,000 calibrated responses per item [Wright-Stone-1979][Linacre-1994], discrimination and guessing parameters cannot be estimated reliably — using 3PL pre-calibration would mean inventing parameters, not measuring them. The Rasch model requires only the difficulty parameter b, which can be provisionally assigned from Lexile and domain information while awaiting empirical calibration.

### 2.4 MLEF scoring — why not EAP or sum score

Maximum Likelihood Estimation with Fencing (MLEF; Han 2016 [Han-2016]) is MAP Growth's documented scoring algorithm [NWEA-VERIFIED; NWEA-2025-TR §3.4]. It computes a continuous ability estimate θ̂ on the logit scale, weighting each response by the Fisher information of that item. A raw sum score treats a correct answer on a b=−2.0 item identically to a correct answer on a b=+1.0 item — MLEF does not. EAP (Expected A Posteriori) introduces prior-dependent shrinkage that biases extreme scores; MLEF avoids this for students with ≥3 responses. Our engine uses EAP only for the first 2 items as a cold-start stabilizer, then switches to MLEF.

The 3.8-logit fence offset is NWEA's documented constant [NWEA-VERIFIED; NWEA-2025-TR].

### 2.5 Six item formats

The proxy implements six item formats. Three are confirmed in Reading 2–5 specifically by NWEA's Technical Report (MCQ, multi-select, composite — Figures 4.3, 4.9–4.11) [NWEA-VERIFIED]; hot-text and drag-and-drop are documented for MAP Growth in other subjects' examples; gap-match is documented only in NWEA secondary materials [SECONDARY]:

| Format | Our token | NWEA name | Scoring |
|---|---|---|---|
| Multiple Choice | `mcq` | Multiple-Choice | Binary 0/1 |
| Multi-Select | `msq` | Multiple Select | Binary 0/1 (all-or-nothing) |
| Evidence-Based Selected Response | `ebsr` | Composite Item | Partial credit 0/1/2 (PCM) |
| Highlight/Select | `hot-text` | Selectable Text / Hot Text | Binary 0/1 |
| Sequence/Order | `sequence` | Drag-and-Drop | Binary 0/1 |
| Gap-Match | `gap-match` | Match/Classify | Binary 0/1 |

EBSR (Composite Item) uses the Rasch Partial Credit Model: both parts correct = 2 points, Part A only = 1 point, Part A wrong = 0 regardless of Part B. Note that this is a deliberate deviation from MAP: NWEA's Technical Report states that composite items are scored dichotomously (students "must answer each part correctly" for credit). Our PCM 0/1/2 scoring preserves information from partial responses [AUTHORING-DECISION]. The pilot will score EBSR both ways in parallel and decide the rule on a pre-committed statistic before RIT unlock (see the Concurrent Validity Plan tab).

One scope note on format familiarization: the benefit is strongest for the three formats confirmed in Reading 2–5 specifically (MCQ, multi-select, EBSR/composite); the other three are low-harm additional practice, not a claimed MAP-preparation benefit.

### 2.6 G2–G5 scope with 2025 norms

The proxy covers grades 2–5 (target ability range RIT 161–227; current item bank provisional b spans ≈ RIT 175–220) using a single cross-grade adaptive bank. Grade norms are sourced from the NWEA 2025 Norms Technical Manual (released August 2025, effective 2025–2026) [NWEA-2025-NM]:

| Grade | Fall mean RIT | Spring mean RIT | Fall→Spring growth |
|---|---|---|---|
| G2 | 170.1 | 181.7 | ~11 RIT |
| G3 | 184.7 | 193.8 | ~9 RIT |
| G4 | 195.9 | 202.1 | ~6 RIT |
| G5 | 203.7 | 208.4 | ~5 RIT |

The 2025 norms shifted the national reference distribution 1–3 RIT lower than 2020 norms, reflecting post-COVID learning trends. The RIT scale itself did not change — a score of 185 means the same absolute reading ability under both norm sets [NWEA-2025-NM].

---

## 3. Item Bank

### 3.1 Current composition

The operational bank contains **650 unique items** across grades 2–5, in 13 source files:

| Source file | Items | Grades | RIT band labels |
|---|---|---|---|
| items.json (original G3) | 38 | G3 | 181–210 |
| bank_forms.json (Form A/B) | 80 | G3 | 181–210 |
| bank_g2.json | 52 | G2 | 161–180 |
| bank_g3_expansion.json | 18 | G3 | 181–210 |
| bank_g4.json | 62 | G4 | 191–210 |
| bank_g5.json | 150 | G5 | 201–220 |
| bank_gap_fixes.json | 118 | G2–G5 | 161–220 |
| bank_match.json | 56 | G2–G5 | 191–220 |
| bank_g2_match.json | 16 | G2 | 161–180 |
| bank_g3_match.json | 4 | G3 | 191–200 |
| bank_g2_sequence.json | 16 | G2 | 161–180 |
| bank_g4_sequence.json | 20 | G4 | 201–210 |
| bank_ebsr_191_200.json | 20 | G3–G4 | 191–200 |
| **Total** | **650** | **G2–G5** | **161–220** |

All items carry provisional difficulty parameters (b_provisional) assigned by content experts based on target RIT band and passage Lexile. The provisional b values span −2.5 to +2.0 logits ≈ RIT 175–220 (band labels run 161–220). Empirical calibration is blocked until the field trial (N≥1,000) [Wright-Stone-1979].

**Staged expansions (merged, harness-loadable; production adoption a reviewable decision pending calibration):** +92 edge items (PR #30; floor to ~RIT 155, ceiling to 235) and +44 items (PR #35: 26 standard-gap items closing nine under-target standards + 18 G5 super-ceiling items at RIT 231–250) — **786 items harness-loadable** (the `load_bank()` build dedups to 786 unique items, which differs from the naive fixture sum), b −4.45 → +4.55 ≈ RIT 155–250. This full 786-item bank is what the authoritative v4 validation ran against. Students below RIT 155 route to the official K–2 MAP instrument. Details in the Item Bank tab.

### 3.2 Format distribution

| Format | Count | % of bank | MAP target (for 400+ items, ~10 forms) |
|---|---|---|---|
| MCQ | 265 | 40.8% | ~220 (56.4% per form) |
| Sequence | 102 | 15.7% | ~40 (10.3% per form) |
| MSQ | 90 | 13.8% | ~60 (15.4% per form) |
| Gap-match | 76 | 11.7% | ~20 (5.1% per form) |
| EBSR | 63 | 9.7% | ~30 (7.7% per form) |
| Hot-text | 54 | 8.3% | ~20 (5.1% per form) |

Pool ratio, both framings labeled: 650/40 = **16.3× session length**; against Stocking's recommended 10× floor (10 × 40 = 400 items), **1.6×** [Stocking-1994]. The staged expansions raise the pool further (786 harness-loadable — see §3.1 and the Item Bank tab).

### 3.3 RIT band distribution

| RIT Band | θ range | Items | Target density |
|---|---|---|---|
| 161–170 | −3.9 to −3.0 | 51 | 20–30 |
| 171–180 | −3.0 to −2.0 | 45 | 30–40 |
| 181–190 | −2.0 to −1.0 | 69 | 60–80 (G3 fall core) |
| 191–200 | −1.0 to 0.0 | 144 | 80–100 |
| 201–210 | 0.0 to +1.0 | 161 | 60–80 |
| 211–220 | +1.0 to +2.0 | 180 | 40–60 |

### 3.4 CCSS standard coverage

The bank covers 50+ CCSS standards across Reading Literature (RL), Reading Informational (RI), and Language (L) strands for grades 2–5. Key coverage summary:

- **G2:** RL.2.1–RL.2.6, RI.2.1–RI.2.6, L.2.4–L.2.6
- **G3:** RL.3.1–RL.3.6, RI.3.1–RI.3.9, L.3.4–L.3.6
- **G4:** RL.4.1–RL.4.6, RI.4.1–RI.4.8, L.4.4–L.4.6
- **G5:** RL.5.1–RL.5.6, RI.5.1–RI.5.8

Full per-standard item counts are documented in the Item Bank tab.

### 3.5 The quality-check gate

Every item in the bank has passed a 14-dimension quality check at a ≥0.85 pass threshold before entering the operational bank. The 14 dimensions include:

- Text-dependence (ablation test: model cannot answer without the passage)
- CCSS alignment verification
- Distractor quality (four near-neighbor distractor types required)
- Passage Lexile matching to RIT band
- EBSR Part B verbatim passage evidence requirement
- Format-specific structural rules

The quality-check gate is a pre-pilot quality control mechanism, not a substitute for empirical Rasch calibration. It ensures items are educationally sound; calibration will determine whether the assigned b_provisional values are accurate.

---

## 4. Simulation Evidence

Seven Monte Carlo simulations were conducted against the item bank (~17,900 production-path sessions in the v4 run). Full methodology and figures are in the Simulation Evidence tab.

**Simulation scope.** The per-simulation sections below record the *initial* run: a Grade-3-configured 630-item bank, G3 fall prior N(−1.5, 1.0), closed-form Fisher-information selector. **The authoritative numbers are the v4 run's — 2026-07-03: production selection path + randomesque selection, full 786-item bank, G2–G5 prior, TimeBack-parity configuration (14/13/13, 40–43 items, SE stop 0.35, TEI floor ≥12)** — results in the Simulation Evidence tab ("v4 Full-Bank Run") and the v4 validation report in the engine repository: r=0.967, RMSE 3.20 RIT, bias −0.04 RIT, reliability 0.931, SEM 3.14, blueprint 100% (±1 vs 14/13/13), TEI floor 100% (mean 16.2), internal cross-bank consistency (synthetic) r 0.918 / LoA [−10.0, +10.0] RIT, reliable range RIT 160–230, 0 MLEF divergences. The path is disclosed, not smoothed: the first production run (v1, 2026-07-02) regressed RMSE to 4.73 and surfaced a +2.62 RIT overestimate; the bias was root-caused to the Owen running estimate's prior shrinkage and resolved by re-basing the final score on the shipped MLEF value (v2); the v3 run re-validated on the 650-item bank (RMSE 3.44, bias −0.38), and the authoritative v4 run re-ran everything on the full 786-item bank after the floor/ceiling/standard-gap expansions merged, improving or holding every metric (bias −0.04, reliable range down to RIT 160). Remaining follow-ups: the 171–180 selection cells improved but are not yet fully served, and never-used items rose to 289 with the larger bank (per-band exposure balancing queued). Initial-run record:

### Simulation 1: Theta Recovery (N=5,000)

Students with true ability drawn from the G3 fall prior N(−1.5, 1.0). The engine recovered theta estimates correlated r=**0.948** with true theta (MAP benchmark: ≈0.90 [NWEA-2025-TR]), RMSE=**4.12 RIT** (MAP target: <4.0 RIT — slightly above, pre-calibration). Bias: −0.24 RIT (negligible systematic error). [SIMULATION]

**Proves:** The CAT algorithm correctly ranks students by reading ability. (The v1 production-path re-run later surfaced a +2.62 RIT systematic overestimate; it was root-caused to the Owen running estimate's prior shrinkage and resolved — v4 bias is −0.04 RIT on the full bank. See the Simulation scope note above.)

### Simulation 2: Reliability (500 sessions × 25 theta levels)

Marginal reliability in the G2–G5 operational range (θ ∈ [−2, +1], RIT 180–210): **0.928**. SEM: **3.22 RIT**. MAP benchmark: reliability ≥0.93 [NWEA-2025-TR]. [SIMULATION]

**Proves:** Reliability is within 0.002 of the 0.93 benchmark pre-calibration; expected to exceed it after empirical calibration. Note MAP's published operational figure is 0.96.

### Simulation 3: Robustness to Parameter Error (2,000 students × 7 σ levels)

b_provisional values were perturbed with Gaussian noise from σ=0.0 to σ=1.0 logits. Reliability remained above 0.85 across all conditions. At the realistic pre-calibration uncertainty of σ≈0.5 logits, reliability was 0.884. [SIMULATION]

**Proves:** The engine is robust to provisional parameter uncertainty; algorithm validity does not depend on having perfectly calibrated b values.

### Simulation 4: Internal Cross-Bank Consistency — Synthetic (N=2,000)

*(Formerly labelled "Score Comparability." Relabelled because this is an internal consistency check against a synthetic bank — explicitly NOT evidence of MAP agreement.)*

Students scored on our bank and a synthetic MAP-like bank (difficulty distribution approximating NWEA's operational pool). Correlation: r=**0.902**. Mean difference: −0.15 RIT (negligible bias). 95% Limits of Agreement: **±11.3 RIT**. [SIMULATION]

**Proves (initial run):** Scores from our engine and a synthetic MAP-like configuration are internally consistent. Under v4, r=0.918 and 95% LoA [−10.0, +10.0] RIT (see Simulation scope note); LoA and bias against *real* MAP scores are the metrics only the scale-linking study can produce.

### Simulation 5: Blueprint Adherence (N=1,000)

Domain quota enforcement verified across 1,000 simulated sessions. Every session delivered within ±1 of the 13/13/13 quota (Literary / Informational / Vocabulary). Blueprint adherence: **100% of sessions within ±1** [SIMULATION].

**Proves:** The domain quota system holds in simulation (the production shadow-test path itself was not exercised — see Simulation scope note above).

### Simulation 6: Floor/Ceiling Characterization (200 sessions × 28 θ levels)

Reliable measurement range (reliability ≥0.85) under the authoritative v4 full-bank run: **RIT 160–230**. This covers G3–G5, the G4/G5 ceiling, and median-and-above G2 students — the median G2 fall student (~RIT 170) is now inside the reliable range (previously below the floor), which resolves the adversarial review's most-cited limitation. Only the bottom ~5% of readers (below RIT 160) fall below the floor and route to the K–2 MAP instrument. Floor effects below RIT 160 and ceiling effects above RIT 230 are expected given the bank's difficulty distribution [SIMULATION].

**Proves:** The test provides reliable measurement across the G3–G5 operational range and for above-average G2 students.

---

## 5. What the Evidence Proves

Numbers below are from the 2026-07-03 v4 run (production path + randomesque selection, full 786-item bank, TimeBack-parity configuration — authoritative):

| Claim | Evidence | Confidence | Source |
|---|---|---|---|
| CAT algorithm ranks students correctly | r=0.967; RMSE=3.20 RIT (<4.0 target); bias −0.04 RIT (near-eliminated on the full bank; within abs(bias)<0.5) | High | [SIMULATION] |
| Test is reliable at core operational range | rel=0.931 (meets the ≥0.93 target; MAP published 0.96 is the higher operational bar), SEM=3.14 RIT | High | [SIMULATION] |
| Algorithm is robust to pre-calibration error | rel≥0.915 at σ≤1.0 | High | [SIMULATION] |
| Internal cross-bank consistency (synthetic — NOT MAP agreement) | r 0.918, 95% LoA [−10.0, +10.0] RIT (synthetic bank; caveats disclosed) | Medium | [SIMULATION] |
| Blueprint is enforced at every session | 100% within ±1 of 14/13/13 on the 40-item scored form, production selector; TEI floor 100% (mean 16.2 ≥ 12) | High | [SIMULATION] |
| Scoring is numerically stable | 0 MLEF divergences in ~17,900 sessions; adversarial simulees finite, bounded, correctly ordered | High | [SIMULATION] |
| Reliable across G2 (median and above) through G5 | RIT 160–230 (median G2 fall reader now inside the reliable range; only the bottom ~5% below RIT 160 route to K–2 MAP) | High | [SIMULATION] |
| Items are CCSS-aligned | 14-dimension quality-check gate | Medium (pre-empirical) | [AUTHORING-DECISION] |
| Content coverage consistent with MAP's published structure | 14/13/13 = 40 scored (TimeBack operational split; NWEA publishes an example 13/13/13 and 40–43 questions) | High | [AUTHORING-DECISION; NWEA-VERIFIED for 40–43] |
| Rasch model matches MAP's model | NWEA Tech Report | High | [NWEA-VERIFIED] |
| MLEF scoring matches MAP's method | NWEA Tech Report | High | [NWEA-VERIFIED] |

---

## 6. What It Does Not Yet Prove (Honest Disclosure)

### 6.1 Scale linking to NWEA's RIT scale

The RIT scale is NWEA's proprietary transformation of the Rasch logit: `RIT = 200 + 10θ` (approximate). Our b_provisional values are not anchored to NWEA's scale. A student scoring θ̂ = −0.5 logits on our test does not necessarily correspond to RIT 195 on the actual MAP — the linear transformation coefficients must be estimated empirically from paired scores. Until this is done, RIT output is intentionally blocked in the engine [AUTHORING-DECISION].

### 6.2 Concurrent validity

We cannot yet claim "a student scoring X on our test would score X on MAP." Concurrent validity requires:
1. The same students take both tests within 2 weeks
2. Scores are compared: correlation, mean difference, 95% limits of agreement
3. A linear transformation is fitted and validated on a held-out sample

This study is the primary outstanding requirement for the product to make its full commercial claim [AERA-2014].

### 6.3 Item parameter calibration

All b_provisional values are assigned by content experts, not estimated from student response data. The SE(b̂) is effectively infinite pre-calibration [Wright-Stone-1979]. After a field trial of N=1,000 students, core-band items (b ≈ −1.0 to +0.5) will achieve SE(b̂) ≤ 0.30 logits (3 RIT) — the operational calibration target.

---

## 7. Roadmap to Full Validity

### Stage 1 (current): Algorithm + Content Validity ✅

- CAT algorithm validated via simulation on the production path under the TimeBack-parity configuration (v4, 2026-07-03, full 786-item bank): r=0.967, RMSE 3.20, bias −0.04, reliability 0.931 [SIMULATION]
- Content blueprint consistent with MAP's published structure: 14/13/13 = 40 scored (TimeBack operational split), 6 formats (3 confirmed in Reading 2–5 specifically), 50+ CCSS standards [AUTHORING-DECISION; NWEA-VERIFIED]
- Item quality gated: 650 operational items passing the 14-dimension quality check (786 harness-loadable with staged expansions)
- RIT output blocked; logit score ± b-uncertainty-adjusted SE output only

### Stage 2: Feasibility Pilot (~40 students) + Calibration Accrued Through Regular Use

- Feasibility pilot: ~40 students (1–2 classes), one adaptive session each — usability, engagement (completion rate, duration, rapid-guess rates), teacher/student experience, and early item red flags. Deliberately includes ≥8 below-median G2 and ≥8 above-median G5 readers for floor/ceiling coverage. No calibration claims: ~1,600 responses cannot calibrate a 786-item bank
- Calibration accrues from regular use: ongoing sessions accumulate toward calibration thresholds (a ~300-student-equivalent response volume for the core band; ≥150 responses per tail-band item for the tails)
- Rasch calibration: estimate empirical b̂ for each item as thresholds are crossed; retire items failing fit statistics (INFIT > 1.30, outfit > 2.00, pt-biserial < 0.20)
- Internal structure: confirm one dominant factor per domain (confirmatory factor analysis)
- Reliability post-calibration: marginal reliability already meets the ≥0.93 target (0.931 under v4); empirical calibration is expected to close the remaining gap to MAP's published 0.96 operational bar as b values improve — the plan is designed to resolve this; simulation supports but cannot guarantee it
- **Timeline:** pilot within days of approval; calibration a function of usage volume

### Stage 3 (N=1,000 concurrent): Scale Linking + Concurrent Validity

- Concurrent validity study: same students take both our test and official MAP within 2 weeks
- Scale linking: fit linear transformation `RIT_ours = a × θ̂ + c`
- Unlock RIT output in score reports
- Report correlation (target: r ≥ 0.80), mean difference (target: < 5 RIT)
- **Timeline:** 12–24 months from field trial start, requires NWEA-authorized school partner

### Cost Estimate

| Stage | N | Cost estimate |
|---|---|---|
| Stage 2 feasibility pilot + accrued calibration | ~40 students (pilot); calibration accrues from regular use | ~$500 (infrastructure + serving) |
| Stage 3 concurrent study | 1,000 paired sessions (accrued via usage) | ~$2,000 + school partnership |
| Full operational validation | 5,000 students | ~$8,000 |

---

## 8. Competitive Differentiation

| Feature | Incept MAP Proxy | NWEA MAP Growth | Other competitors |
|---|---|---|---|
| Adaptive delivery | Fisher-info CAT | Constrained CAT (proprietary) | Adaptive (iReady, Star) but closed-scale, without MAP format parity |
| IRT model | Rasch 1PL (matches MAP) | Rasch 1PL [NWEA-VERIFIED] | Varies |
| Scoring algorithm | MLEF (matches MAP) | MLEF [NWEA-VERIFIED] | Typically EAP or sum score |
| Item formats | 6 (3 confirmed in Reading 2–5; 3 from wider MAP Growth documentation) | 6 across MAP Growth [NWEA-VERIFIED] | Varies |
| EBSR/Composite format | Yes (PCM 0/1/2 — deliberate deviation from MAP's dichotomous scoring) | Yes (dichotomous) | Rare |
| Quality gate | 14-dimension quality checks | Empirical calibration (≥1,000) | None publicly documented |
| G2–G5 cross-grade bank | Yes (650 items) | Yes (40,000+ items) | Grade-restricted |
| Per-student cost [DERIVED] | <$3 (pre-pilot) | $13.50–15.50/year (Growth alone) | $5–15 |
| Infrastructure requirement | Browser, no lockdown | Managed browser/NWEA SB | Varies |
| Immediate results | Yes | Next day via portal | Varies |
| RIT output | Pre-pilot: blocked | Yes | N/A |
| Engine source | Available to partners (private repository) | No | No |

---

## 9. Student-Facing Interface: MAP-like UI

The interface follows MAP's publicly documented interaction conventions, so that students experience familiar testing conventions and the official test measures reading rather than interface novelty:

- **Forward-only navigation**: once an item is answered, it is locked; no back button [NWEA-VERIFIED]
- **Answer-before-advance**: NEXT is disabled until a response is given
- **Split-pane passage/question layout** for multi-paragraph passages; stacked layout for short passages
- **All six item interactions rendered**: MCQ, MSQ, EBSR (Part B unlocks after Part A), hot-text, sequence (drag-to-order), gap-match
- **Zoom controls** in the toolbar

### 9.1 Live deployment

The full adaptive test is live. The direct no-login route is gated behind the `PUBLIC_TEST_ENABLED` flag (default off) so the item bank cannot be farmed anonymously:

**Direct assessment URL (flag-gated):**
```
https://map-proxy-engine-hba75nbzeq-uc.a.run.app/test
```
Delivers a 40–43-item adaptive G2–G5 reading assessment in a browser. Results appear immediately on completion.

**TimeBack-integrated URL (with student identity):**
```
https://map-proxy-engine-hba75nbzeq-uc.a.run.app/timeback/login
```
Redirects to Cognito SSO → authenticated adaptive session → score recorded to TimeBack gradebook via Caliper event.

**TimeBack course:** *Incept MAP Adaptive Assessment — Grade 3*
Registered on TimeBack staging under org `Alpha School`. Students enrolled in this course see the assessment tile in their TimeBack dashboard and launch directly into the OAuth-authenticated adaptive session.

### 9.2 Why familiar testing conventions matter for validity

Interaction design is a component of **response process validity** (AERA/APA/NCME Standards, 2014, Standard 1.13 [AERA-2014]). If students interact with items differently on our platform than on MAP — different cognitive load from an unfamiliar UI, different navigation affordances, different format rendering — response patterns will differ and scores will not be comparable. By following MAP's documented interaction conventions, we minimize this source of measurement error.

MAP® is a registered trademark of HMH Education Company / NWEA; this instrument is independent and not affiliated with or endorsed by NWEA.

---

## Sources

Full APA bibliography in the Sources tab. Key references:

- [NWEA-2025-TR] NWEA. (2026). *MAP Growth Technical Report for 2024–2025*. NWEA/HMH.
- [NWEA-2025-NM] NWEA. (2025). *MAP Growth Norms Technical Manual 2025*. NWEA.
- [NWEA-2019-TR] NWEA. (2019). *MAP Growth Technical Report 2019*. NWEA.
- [Han-2016] Han, K. T. (2016). Maximum likelihood score estimation method with fences for short-length tests and computerized adaptive tests. *Applied Psychological Measurement, 40*(4), 289–301.
- [Rasch-1960] Rasch, G. (1960). *Probabilistic models for some intelligence and attainment tests*. Danish Institute for Educational Research.
- [Kingsbury-1989] Kingsbury, G. G., & Zara, A. R. (1989). Procedures for selecting items for computerized adaptive tests. *Applied Measurement in Education, 2*(4), 359–375.
- [Wright-Stone-1979] Wright, B. D., & Stone, M. H. (1979). *Best test design*. MESA Press.
- [Linacre-1994] Linacre, J. M. (1994). Sample size and item calibration stability. *Rasch Measurement Transactions, 7*(4), 328.
- [Stocking-1994] Stocking, M. L. (1994). *Three practical issues for modern adaptive testing item pools*. ETS Research Report RR-94-5.
- [Kolen-Brennan-2014] Kolen, M. J., & Brennan, R. L. (2014). *Test equating, scaling, and linking: Methods and practices* (3rd ed.). Springer.
- [AERA-2014] American Educational Research Association, American Psychological Association, & National Council on Measurement in Education. (2014). *Standards for educational and psychological testing*. AERA.
