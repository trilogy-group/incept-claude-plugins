# Audits & Fixes

## What the audits demanded, and what we fixed

Before the Case for Approval reached its approver, two adversarial audits were run against the full documentation package: one checking every number against the engine's own artifacts and the repo's ground truth, one fact-checking every external claim against NWEA primary sources. The verdict on the psychometric spine was clean — Rasch model and MLEF scoring with the 3.8-logit fence verified verbatim against NWEA's Technical Report. On the blueprint, precision matters: NWEA's Technical Report Table 3.2 shows an *example* blueprint of 13/13/13 + up to 4 field-test items; NWEA's public test description states 40–43 questions. The engine adopts TimeBack's operational split of 14/13/13 = 40 scored items, extending to 43 for precision — consistent with NWEA's published structure and identical across both Alpha engines [AUTHORING-DECISION; NWEA-VERIFIED for the 40–43 structure]. The audits also found real problems. This table is the honest scorecard.

| # | What the audit found | What is now true in this package |
| :---- | :---- | :---- |
| 1 | Summary tables reported reliability as "0.930 ✅" against a ≥0.93 benchmark the underlying reports state as 0.928, below | Reliability is stated honestly everywhere — **0.931 under the authoritative v4 full-bank run, now meeting the ≥0.93 benchmark** — with the context that MAP's published Reading 2–5 figure (0.96) is the higher operational bar |
| 2 | The one failing metric (RMSE 4.12 vs <4.0 target) was omitted from every summary table | RMSE appears in every summary table — the v1 production re-run regressed it to 4.73 and we reported that; the v4 full-bank run measures **3.20 RIT, well within the <4.0 target** (Case for Approval §7) |
| 3 | The item-bank source table summed to 520 while claiming 650 | Replaced with the verified 13-file breakdown; the fixtures were counted programmatically and sum to exactly 650 |
| 4 | Simulations were G3-scoped (630 items, G3 prior, simplified selector) but described as "G2–G5, production code" | **Re-run on the true production path (v1 2026-07-02), root-caused and re-based (v2), re-validated under the TimeBack-parity configuration (v3 2026-07-03, 650 items), and finally re-validated on the full 786-item bank (v4 2026-07-03)** — G2–G5 prior; the Case for Approval §7 carries the authoritative v4 numbers, and the v1 regression story is preserved, not overwritten |
| 5 | "Reliable across full G2–G5" — but the reliable floor (RIT 181) sits above the national G2 fall mean (~170) | **Largely resolved on the full bank:** the v4 reliable range reaches down to RIT 160, so the median G2 fall reader (~170) is now inside it; only the bottom ~5% (below RIT 160) route to K–2 MAP, and G2 reports carry a floor flag |
| 6 | A section celebrated the UI as a "pixel-accurate replica" built by scraping NWEA's practice site — a legal liability framed as a selling point | Rewritten as **MAP-like UI**: familiar testing conventions justified by response-process validity, with a trademark disclaimer; legal review of name and UI provenance requested before anything goes beyond internal |
| 7 | "$28/student", "competitors are fixed-form", "open-source engine" — each contradicted by public evidence | All corrected or removed; the approval case carries no pricing and no competitive claims |
| 8 | "All six formats confirmed in MAP Reading 2–5" overstated the cited source | Bounded to the evidence: three formats confirmed Reading-specific; the EBSR partial-credit scoring is disclosed as our deviation from MAP's dichotomous scoring |
| 9 | Concurrent-study cohort stated as N=100–200 in one file and N=1,000 in another | N ≥ 1,000, consistent everywhere |
| 10 | The public no-login test URL allows anonymous farming of the item bank | Route gated behind `PUBLIC_TEST_ENABLED` (default off) — PR open with all CI checks green; the authenticated TimeBack path verified intact |

## Second adversarial review (teammate, 2026-07-02) — disposition

A second, independent teammate review was run after the first two audits. All 12 findings, one line each:

| # | Finding | Disposition |
| :---- | :---- | :---- |
| 1 | Population baseline (206.4 / 72nd pctile) is a biased slice | **Re-baselined** — full-population figures adopted (196.0 / 46th pctile, n=915); the Case for Approval §2 rewritten around the two-population truth |
| 2 | Reported SE understates true uncertainty under provisional b values | **Shipped** — score reports now emit b-uncertainty-adjusted SE (×1.02 under v4) with an `se_basis` field; auto-removed post-calibration |
| 3 | Natural CAT exposure under-samples tail items for calibration | **Pre-committed** — the ~40-student pilot deliberately includes both tails (≥8 below-median G2, ≥8 above-median G5); the ≥150-responses-per-tail-band-item target is attached to the calibration stage that accrues from regular use |
| 4 | A single RIT unlock gate hides tail unreliability | **Pre-committed** — core-band-first, band-aware RIT unlock; floor/ceiling scores stay logit-only until tail SE(b̂) ≤ 0.30 |
| 5 | EBSR partial-credit deviation could contaminate linking undetected | **Pre-committed** — dual-scoring comparator built; decision statistic and criterion fixed before RIT unlock |
| 6 | Standard-level coverage gaps (e.g., RI.4.1) unaddressed | **Closed** — PR #35 (all CI green) merged 26 standard-gap items closing nine under-target standards; G5 L.5.x strand partially closed (no certified source material — hand-authored, disclosed) |
| 7 | G2 low tail effectively outside the instrument | **Largely closed** — floor expansion to ~RIT 155 merged (+92 edge items, PR #30) and validated on the full bank; the v4 reliable range reaches RIT 160, so the median G2 fall reader is now inside it and only the bottom ~5% (below RIT 160) route to official K–2 MAP, stated explicitly |
| 8 | "The pilot fixes exactly that" overclaims what a study can promise | **Fixed** — reworded: the plan is designed to resolve it; simulation supports but cannot guarantee it |
| 9 | "Sim 4" reads as MAP agreement evidence | **Relabeled** — now "internal cross-bank consistency (synthetic)," explicitly not MAP agreement; the ±5–8 RIT post-linking figure demoted to Open/Derived-hope |
| 10 | Pool-to-test ratio quoted two ways (16.7× vs 1.7×) without reconciliation | **Reconciled** — both framings stated and labeled everywhere they appear (650/40 = 16.3× session length; 1.6× vs Stocking's 10× recommended floor) |
| 11 | Format-familiarization benefit implied for all six formats | **Bounded** — one-line scope added: strongest for the 3 Reading-2–5-confirmed formats; the other 3 are low-harm additional practice |
| 12 | Distribution treated as adoption | **Argued, not assumed** — adoption paragraph added (Case for Approval §6); measured by the pilot's completion-rate success/kill criteria |
