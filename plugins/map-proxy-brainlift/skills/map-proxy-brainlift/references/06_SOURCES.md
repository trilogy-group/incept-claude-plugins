# Bibliography — MAP Proxy Adaptive Assessment Validity Directory
**Version:** 2.0 | **Date:** 2026-07-03

Complete APA bibliography for all sources cited across the validity documentation package. Organized by category.

---

## Primary NWEA Sources

**[NWEA-2025-TR]**
NWEA. (2026). *MAP Growth Technical Report for 2024–2025*. NWEA/HMH (published April 2, 2026; © HMH Education Company).
*Used for:* the *example* blueprint of 13/13/13 + up to 4 field-test items (Table 3.2 — an example, not a mandated split; the engine adopts TimeBack's operational 14/13/13 = 40 scored, consistent with NWEA's published 40–43 structure), item formats (Figures 4.3, 4.9–4.11), Rasch 1PL model specification (§3.2), MLEF scoring with 3.8-logit fence (§3.4), reliability benchmark (≥0.93), SEM target (≤4.0 RIT), constrained CAT algorithm (§3.3), RIT-to-θ transformation formula.
Verification status: [NWEA-VERIFIED] — direct PDF extraction.

**[NWEA-2025-NM]**
NWEA. (2025). *MAP Growth Norms Technical Manual 2025*. NWEA. Released August 2025, effective 2025–2026 school year.
Retrieved from NWEA portal (https://teach.mapnwea.org).
*Used for:* Grade 2–5 fall/spring mean RIT and SD values (Table A.1); post-COVID norm shift description; G2 fall mean 170.1, G3 fall mean 184.7, G4 fall mean 195.9, G5 fall mean 203.7; G3 fall–spring growth ~9 RIT.
Verification status: [NWEA-VERIFIED] — primary PDF; norms supersede 2020 values for 2025–2026.

**[NWEA-2020-NM]**
Thum, Y. M., & Kuhfeld, M. (2020). *NWEA 2020 MAP Growth achievement status and growth norms for students and schools* (NWEA Research Report No. 2020-04). NWEA. Retrieved from https://teach.mapnwea.org/impl/NormsTables.pdf
*Used for:* G3 norms backup values (fall 186.62, winter 193.90, spring 197.12); G3 fall-to-spring growth 10.5 RIT (SD 7.8) under 2020 norms. Note: superseded — under the 2025 norms, G3 fall→spring growth is ≈9 RIT (184.7→193.8) [NWEA-2025-NM].
Verification status: [NWEA-VERIFIED] — independently re-verified June 2026.

**[NWEA-2019-TR]**
NWEA. (2019). *MAP Growth Technical Report 2019*. NWEA. Retrieved from https://www.nwea.org.
*Used for:* Historical context on Rasch 1PL model specification and MLEF scoring; equal-interval RIT scale property.
Verification status: [NWEA-VERIFIED — prior pass; not re-confirmed June 2026].

**[NWEA-MAP-TEST-DESC]**
NWEA. (2025). *MAP Growth test description*. Retrieved from https://teach.mapnwea.org/impl/maphelp/Content/AboutMAP/MAPTestDescription.htm
*Used for:* Reading 2–5 "40 to 43 questions" item count — the load-bearing NWEA source for the engine's 40-scored / 43-cap session structure; three instructional areas; untimed administration.
Verification status: [NWEA-VERIFIED] — re-extracted June 2026.

**[NWEA-MAP-WORD-COUNT]**
NWEA. (2025). *MAP Reading Word Count guide*. Retrieved from https://cms-admin.mapnwea.org (login-gated).
*Used for:* Literary passages 400–600 words; informational passages 250–500 words; G3 on-grade Lexile 560–650L.
Verification status: [NWEA-VERIFIED] — via Sherlock verification session 768ea82a, June 2026.

**[NWEA-NSCAS-KEYS]**
NWEA / Nebraska Department of Education. (2024–2025). *NSCAS Growth paper answer keys* (Nebraska Statewide Accountability System). Retrieved from Nebraska DEdepartment of Education portal.
*Used for:* Composite Item (EBSR) partial credit scoring confirmation: Part A only = 1 point, both parts = 2 points.
Verification status: [NWEA-VERIFIED] — via Sherlock verification session 768ea82a, Claim 5.

**[NWEA-TEI-BLOG]**
NWEA. (2025, March). *Item pool depth and technology-enhanced items in MAP Growth*. NWEA Blog. Retrieved from https://www.nwea.org/blog.
*Used for:* ">30% TEI pool-wide" figure; TEI floor derivation (>30% of 40 items = ≥12; engine floor: ≥12, gap-match counted as TE per TimeBack parity — was ≥15 pre-parity).
Verification status: [NWEA-VERIFIED] — official NWEA blog.

**[NWEA-DURATIONS]**
NWEA. (2025). *Average MAP Growth test durations*. Retrieved from https://www.nwea.org/uploads/Average-MAP-Growth-Test-Durations.pdf
*Used for:* Untimed administration; typical G3 Reading session approximately 50–60 minutes.
Verification status: [NWEA-VERIFIED].

**[NWEA-CCSS-IA]**
NWEA. (2025, April). *MAP Growth CCSS Instructional Areas — ELA*. NWEA.
*Used for:* CCSS standard-to-goal-area crosswalk for reading standards in MAP Growth.
Verification status: [NWEA-VERIFIED].

---

## Foundational Psychometric Literature

**[Rasch-1960]**
Rasch, G. (1960). *Probabilistic models for some intelligence and attainment tests*. Danish Institute for Educational Research.
*Used for:* The 1-parameter logistic model P(correct | θ, b) = 1/(1 + exp(−(θ−b))); equal-interval measurement property of the logit scale.

**[Wright-Stone-1979]**
Wright, B. D., & Stone, M. H. (1979). *Best test design*. MESA Press.
*Used for:* Rasch calibration sample-size guidance (SE(b̂) shrinks approximately with 1/√N); target N ≈ 200 well-targeted responses per item for SE ≤ 0.30 logits; N ≈ 800 per item for SE ≤ 0.15 logits.

**[Linacre-1994]**
Linacre, J. M. (1994). Sample size and item calibration stability. *Rasch Measurement Transactions, 7*(4), 328.
*Used for:* Optimal sample size recommendations for item calibration; confirmation of Wright & Stone (1979) formula.

**[Han-2016]**
Han, K. T. (2016). Maximum likelihood score estimation method with fences for short-length tests and computerized adaptive tests. *Applied Psychological Measurement, 40*(4), 289–301. https://doi.org/10.1177/0146621615573389
*Used for:* MLEF scoring algorithm; 3.8-logit fence offset; fence item direction (lower = correct, upper = wrong); Newton-Raphson maximization of fenced log-likelihood.

**[Kingsbury-1989]**
Kingsbury, G. G., & Zara, A. R. (1989). Procedures for selecting items for computerized adaptive tests. *Applied Measurement in Education, 2*(4), 359–375.
*Used for:* Constrained CAT with content quotas; maximum Fisher information item selection with constraints; MAP Growth's documented algorithm basis.

**[Stocking-1994]**
Stocking, M. L. (1994). *Three practical issues for modern adaptive testing item pools* (ETS Research Report No. RR-94-5). Educational Testing Service.
*Used for:* CAT pool-to-test ratio recommendations: minimum 6×, recommended 10× test length; pool-size planning for item security.

**[Kolen-Brennan-2014]**
Kolen, M. J., & Brennan, R. L. (2014). *Test equating, scaling, and linking: Methods and practices* (3rd ed.). Springer.
*Used for:* Linear equating methodology (§4.2); concurrent calibration design (§6); anchor-item equating (§5); sample size requirements for linking (§4.3); expected LoA improvement after scale linking.

**[AERA-2014]**
American Educational Research Association, American Psychological Association, & National Council on Measurement in Education. (2014). *Standards for educational and psychological testing*. American Educational Research Association.
*Used for:* Validity framework (Chapter 1); reliability benchmarks (Chapter 2); concurrent validity study design (§4.3); content validity evidence (§1.7); reliability ≥ 0.85 for screening decisions; reliability ≥ 0.90 for high-stakes individual decisions; floor/ceiling documentation requirement (§4.9).

**[Sympson-Hetter-1983]**
Sympson, J. B., & Hetter, R. D. (1983). *Controlling item-exposure rates in computerized adaptive testing* (Proceedings of the 27th annual meeting of the Military Testing Association). Military Testing Association.
*Used for:* Empirical item exposure control methodology for CAT; recommended post-pilot implementation to replace top-K soft cap.

---

## Additional Academic Literature

**[Masters-1982]**
Masters, G. N. (1982). A Rasch model for partial credit scoring. *Psychometrika, 47*(2), 149–174.
*Used for:* Rasch Partial Credit Model (PCM) for polytomous EBSR items; step threshold parameterization.

**[Bland-Altman-1986]**
Bland, J. M., & Altman, D. G. (1986). Statistical methods for assessing agreement between two methods of clinical measurement. *The Lancet, 327*(8476), 307–310.
*Used for:* Bland-Altman method for computing 95% Limits of Agreement in Simulation 4 (score comparability); standard method-comparison statistical approach.

**[Hambleton-1991]**
Hambleton, R. K., Swaminathan, H., & Rogers, H. J. (1991). *Fundamentals of item response theory*. Sage.
*Used for:* IRT background; Fisher information formula I(θ) = P(θ)(1−P(θ)) for Rasch items; test information function.

---

## Internal Project Documents

**[CAT-EXAM-SPEC]**
Incept-MAP-proxy team. (2026). *MAP Growth Reading — Adaptive CAT Exam Spec* (Version 1.0). Included in this package as the CAT Exam Spec tab; source lives in the engine repository (docs/exam-spec).
*Used for:* All design decisions and decision records for the CAT implementation; domain quota derivation; bank composition tables; gap analysis history.

**[G3-EXAM-SPEC]**
Incept-MAP-proxy team. (2026). *Grade 3 Reading — MAP Growth Equivalent Examination Spec* (Version 2.0). The superseded fixed-form G3 exam spec in the engine repository (docs/exam-spec).
*Used for:* Historical fixed-form design context; G3-specific norm values; domain quota rationale; distractor taxonomy.

**[VALIDATION-REPORT]**
Incept-MAP-proxy team. (2026). *MAP Engine Psychometric Validation Report v3 — TimeBack-Parity Configuration* (2026-07-03). The v3 validation report in the engine repository. **Authoritative.**
*Used for:* All seven simulation results; exact numeric values for r, RMSE, bias, reliability, SEM, LoA, blueprint adherence, TEI floor audit, exposure, session-length distribution, and floor/ceiling characterization.
Historical records (superseded, retained for the audit trail, all in the engine repository): the v2 re-based run report (2026-07-02), the v1 production-path re-run report (2026-07-02), and the initial G3-scoped run report (2026-06-25).

**[MAP-POPULATION-BASELINE]**
Incept-MAP-proxy team. (2026). *MAP Reading Population Baseline — Grades 2–5* (2026-07-03). The population-baseline analysis in the engine repository (research/oneroster-map).
*Used for:* the two-population truth in the problem statement — full current G3 population n=915 / mean RIT 196.0 / 46th percentile [EXTERNAL-REVIEW, corroborated]; the retirement and decomposition of the old "206.4 ≈ 72nd percentile" figure (repeat-record + stale-cohort + coverage bias); per-grade baseline tables; the per-grade which-tail-binds verdicts (G2 floor, G3 floor, G4 mild ceiling, G5 ceiling).

**[ADAPTIVE-BRAINLIFT]**
Incept-MAP-proxy team. (2026). *Adaptive MAP Proxy — Design Brainlift* (Version 1.0, 2026-06-18). The adaptive-design brainlift in the engine repository (docs).
*Used for:* Comprehensive design rationale; algorithm design notes; MAP similarity/gap matrix; pre-pilot vs. post-pilot claim matrix.

**[SHERLOCK-REPORT]**
Incept-MAP-proxy team. (2026). *MAP Coherence Sherlock Verification Report* (Session 768ea82a, 2026-06-17). The Sherlock verification report in the engine repository (docs/engine).
*Used for:* NWEA format name verification (Claim 1); 2025 norms verification (Claim 2); passage word count verification (Claim 3); EBSR partial credit scoring verification (Claim 5).

---

## Citation Tag Legend

| Tag | Meaning |
|---|---|
| `[NWEA-VERIFIED]` | Confirmed from NWEA primary PDF or official web source |
| `[SIMULATION]` | Produced by our Monte Carlo simulations (engine/scripts/validation/) |
| `[ACADEMIC]` | From peer-reviewed literature cited above |
| `[DERIVED]` | Calculated or inferred from primary sources |
| `[DERIVED-hope]` | A literature-based expectation we state in advance but cannot yet defend from our own evidence (e.g., post-linking LoA projections) — Open until measured |
| `[EXTERNAL-REVIEW]` | Figure produced by an independent reviewer from a source our credentials cannot reach (`rpt2_map_scores`); adopted where corroborated, never silently |
| `[AUTHORING-DECISION]` | Our design choice, not from an external source |
| `[SECONDARY]` | From a non-primary, non-peer-reviewed source (use with caution) |
| `[ASSEMBLED]` | Synthesized from multiple sources; not a single primary claim |
