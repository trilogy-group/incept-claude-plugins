---
name: map-proxy-brainlift
description: The knowledge base a REVIEWER AGENT loads to understand and evaluate the Incept MAP Proxy (an adaptive G2-G5 reading CAT designed to approximate NWEA MAP Growth Reading 2-5) properly and with full context — the engine's design and what's actually built, its BrainLift (the load-bearing psychometric + product positions and their evidence), the case for approval, and the honest tradeoff logic (which choices are deliberate/defensible, the real remaining gaps, and the Verified/Simulation/Asserted/Open status of every claim). Use when a reviewer agent is asked to "review/evaluate the MAP proxy", "decide whether to approve the MAP proxy for pilot", "judge the MAP proxy validity case", "audit the MAP proxy approval package", or needs full reasoning context (not a checklist) to make an informed, fair judgment. Everything here is grounded in docs/validity/*, CLAUDE.md (C1-C13), the 2026-07-02 production-path re-run report, and NWEA's MAP Growth Technical Report 2025. Recompute numbers from engine/scripts/validation/ if re-verifying, or use the companion map-approval-case agent for a live adversarial audit.
---

# Incept MAP Proxy (G2–G5 Reading CAT) — reviewer knowledge base

You are a **reviewer agent** deciding whether the Incept MAP Proxy — a computer-adaptive reading assessment designed to approximate NWEA MAP Growth Reading 2–5 — should be approved for a school pilot, an investor case, or a stakeholder decision. This skill gives you the **full context to judge it fairly and correctly**: what the engine is, why it was built the way it was, the evidence, the case for approval, and the honest tradeoffs. It is explanatory *and* evaluative: understand the design on its own terms, then judge the build against that design and the design against NWEA ground truth.

**How to judge (prime directive):** distinguish a *deliberate, disclosed limitation* from an *overclaim*. Reward honesty about what pre-pilot data cannot prove (concurrent validity, RIT output, calibration); penalize any claim that a simulation is empirical, that a "narrowly below benchmark" number is a pass, or that adaptive delivery is proprietary-equivalent to MAP's CAT. Tag every claim **[NWEA-VERIFIED]** (from a primary NWEA source), **[SIMULATION]** (Monte Carlo, not real students), **[DIRECT-PULL]** (live OneRoster/engine data), **[DERIVED]**, **[AUTHORING-DECISION]**, or **[OPEN]** (needs data that doesn't exist yet — a pilot cohort or concurrent-validity study).

**Context that frames everything:** this is a **pre-pilot** psychometric proxy, not a finished, calibrated test. No student has ever taken it and the real MAP in the same window. Every number you will read is either a Monte Carlo simulation against provisional (expert-assigned, uncalibrated) item difficulties, or a live pull of engine/content statistics. The entire case rests on distinguishing "the algorithm and blueprint are demonstrably right" from "the score is demonstrably equivalent to a MAP RIT" — the second claim is explicitly not yet available, by design (C9).

---

## 1. Core concepts (the psychometric + platform reference points)

**C1 — MAP Growth is a Rasch 1PL, MLEF-scored, Constrained CAT.** NWEA's MAP Growth Technical Report 2025 [NWEA-2025-TR] specifies: Rasch 1PL IRT model, MLEF (Han 2016) scoring with a 3.8-logit fence, Fisher-information-maximizing item selection under content-area quotas (Kingsbury & Zara 1989), and a 39-scored-item form (+ up to 4 unscored field-test items, 43 max). A proxy that claims equivalence must match these specifics, not just "be adaptive."

**C2 — Domain blueprint is equal thirds, not an estimate.** Literary Text · Informational Text · Vocabulary & Word Meaning, 13/13/13 items — directly from NWEA Tech Report 2025 Table 3.2 [NWEA-2025-TR]. The earlier 45/40/15 authoring guess was superseded once this table was located; a design still citing 45/40/15 is stale.

**C3 — Item formats: only 3 of 6 are Reading-2–5-confirmed.** MCQ, MSQ, and Composite/EBSR are confirmed specifically for Reading 2–5 in NWEA's figures (4.3, 4.9–4.11). Hot-text and drag-and-drop are documented in the MAP Growth pool generally (other subjects' figures); gap-match appears in NWEA secondary materials. Presenting all six as "Reading-2–5-confirmed" without this distinction is an overclaim.

**C4 — Correct 2025-norms G3 figures: fall ~185, spring ~194, growth ~9 RIT.** [NWEA-2025-NM]. The pre-2026 207/213/+6 figures are simply wrong; an earlier "spring ~197" correction also turned out to be the 2020 value carried forward by mistake. Any document citing older numbers fails a norm-accuracy check immediately.

**C5 — MAP is untimed, forward-only, and not in TimeBack.** MAP Reading is a power test — no clock, no back-navigation once an item is answered [NWEA-VERIFIED]. Separately, MAP itself is administered only through NWEA's own platform; it has no presence inside TimeBack (OneRoster/QTI/PowerPath), so no internal dataset can currently contain a real MAP score to validate against. Any "internal proxy score correlates with real MAP" claim is necessarily a **simulation claim**, not an empirical one, until a concurrent-validity study exists.

**C6 — RIT is NWEA's proprietary scale transform, not something we can derive.** `RIT = a·θ + c` — the constants `a` and `c` are NWEA's, unpublished, and can only be recovered by paired-score regression (same students, both tests, same window). A logit score is a valid *internal* ability estimate; it is not a RIT number until scale-linked (C9 below).

**C7 — Bank calibration reality.** All item difficulties (`b_provisional`) in the bank are content-expert assignments, not empirically estimated. SE(b̂) is effectively infinite pre-calibration [Wright-Stone-1979]. Simulations that assume these values are exact will always overstate real-world precision; the honest framing is "the algorithm tolerates this uncertainty at the simulated level," not "the algorithm is this precise."

---

## 2. The BrainLift — why the engine is built this way (positions + evidence)

**B1 — Rasch 1PL over 3PL** (because C1, C7). Without ≥1,000 calibrated responses per item, discrimination (`a`) and guessing (`c`) parameters cannot be estimated — using 3PL pre-calibration would mean inventing parameters, not measuring them [Wright-Stone-1979; Linacre-1994]. Rasch 1PL is also MAP's own stated model.

**B2 — MLEF over EAP/sum-score** (because C1). MLEF (Han 2016) gives a continuous ability estimate weighted by item information; it's MAP's documented method. Sum score treats a correct answer on an easy item identically to a hard one. EAP shrinks extreme scores toward the prior. Our engine uses EAP only as a 2-item cold-start stabilizer, then switches to MLEF with NWEA's 3.8-logit fence.

**B3 — CAT, not fixed-form** (because C1). A fixed-form administered to a G2–G5-wide population wastes items at floor/ceiling for any individual student and cannot hit MAP's SE ≤3–4 RIT target across a wide range. The engine implements Fisher-information selection with domain quotas and shadow-test feasibility checking — the same constrained-CAT structure NWEA describes [Kingsbury-Zara-1989].

**B4 — Equal-thirds blueprint, enforced at assembly** (because C2, C12). 13/13/13 is not just a target — the assembled-form check (`count(TEI) ≥ 12` out of the 34 non-vocabulary items) is a hard gate, not an aspiration.

**B5 — RIT output deliberately blocked pre-linking** (because C6, C9). The engine computes an internal `RIT_approx = 200 + 10θ` for developer logs only; it is never surfaced to a student or school. This is a design choice to avoid presenting an unlinked number as if it were a real RIT.

**B6 — Interface fidelity as a validity argument, with a legal caveat** (response-process validity, AERA/APA/NCME Standards 2014 §1.13). The original framing (visual elements extracted via Playwright scraping of `practice.mapnwea.org`, described as a "pixel-accurate replica") was flagged as a legal/trademark risk — "MAP" is an HMH-owned registered trademark — and has since been revised: the UI is now described as "MAP-like" and the scraping/replica framing removed from external-facing material. Judge this positively as a self-correction, but confirm no shipped document still uses the retired framing.

**Deliberately dropped / corrected** (re-proposing these = a regression): the 45/40/15 domain-weight guess (superseded by NWEA's actual 13/13/13 table); the "$28/student" NWEA pricing figure (corrected to $13.50–15.50/student per NWEA's published pricing); presenting all 6 formats as equally Reading-2–5-confirmed (only 3 are); "pixel-accurate replica" / scraping framing in externally-shareable docs.

---

## 3. What is actually built (live-verified as of 2026-07-02; see [DIRECT-PULL] tags)

Authoritative re-run: `engine/scripts/validation/report_g2g5_650.md`, 650-item bank (G2–G5: 241 literary · 243 informational · 166 vocabulary), production selection path (real `select_next()`, not the old closed-form harness), 15,350 Monte Carlo sessions.

| Metric | Value | Verdict vs. benchmark |
|---|---|---|
| Theta recovery r (Sim 1) | **0.954** | Exceeds MAP's ≈0.90 benchmark |
| RMSE (Sim 1) | **4.73 RIT** | **Flagged** — above MAP's <4.0 RIT target, and worse than the prior 4.12 claim |
| Bias (Sim 1) | **+2.62 RIT** | **Flagged** — a systematic overestimate, not the ~0 expected; root-cause open (P1 bead) |
| Marginal reliability, operational range (Sim 2) | **0.929** | Meets AERA's ≥0.85 screening floor; below MAP's own ≥0.93 |
| SEM, operational range (Sim 2) | **3.18 RIT** | — |
| Blueprint adherence (Sim 5) | **100.0% (±1)** | Exactly matches C2/C12 |
| Reliable measurement range (Sim 6) | **RIT 181–230** | Covers core G2–G5 range; degrades below RIT 181 |
| Score comparability vs. synthetic MAP-like bank (Sim 4) | r=0.909, 95% LoA [−7.9, +8.3] RIT | [SIMULATION] against a *synthetic* bank, not real NWEA items — not concurrent validity |

**Do not present RMSE 4.73 or the +2.62 RIT bias as "narrowly meets" or otherwise soften them — they are honest misses against MAP's own published targets, and the bias in particular is unresolved.** The likely causes (per the report): theta updates only at passage boundaries (3–5 items at a time) rather than per-item, and MLEF fence behavior interacting with composite-item PCM scoring at low theta. Both need investigation before any linking study — this is exactly the kind of thing C9 exists to prevent from reaching an RIT claim prematurely.

**Older, superseded numbers** (0.948 r / 4.12 RMSE / 630 items / −0.24 bias) must never be quoted as current — they used a closed-form Fisher-max selector, not the real production selector, and were missing one bank file.

---

## 4. The case for approval (what's being asked, and on what basis)

**The ask, per the current approval package** (ti-courseplans `courses/map-proxy-assessment/validity/`, mirrored in this repo's `docs/validity/`): approve a **pilot** — not a RIT-equivalence claim, not a finished product. The argument, in order:

1. **The algorithm and blueprint are demonstrably right**, at the simulation level: theta recovery exceeds the MAP benchmark, blueprint adherence is exact, and the engine tolerates realistic pre-calibration error without reliability collapse (Sim 3: reliability stays ≥0.85 through σ=1.0 logits).
2. **The engine matches MAP's documented psychometric machinery**, not just "an adaptive test" — same IRT model, same scoring algorithm, same fence constant, same blueprint table — each individually [NWEA-VERIFIED], not inferred.
3. **What the pilot buys**: item calibration (Stage 2, N≥1,000) and, ultimately, a concurrent-validity study (Stage 3, N≥1,000 paired sessions) that is the *only* honest path to a linked RIT number, because MAP is not in TimeBack (C5) and no other route to real paired data exists.

**Two value propositions — do not blur them** (mirrors the `map-approval-case` agent's framing):

- **Practice/prep instrument**: frequent, low-stakes, MAP-format-matched exposure with immediate domain-level feedback, targeting a measured weak domain (Informational Text, per Alpha OneRoster cohort data: G3 mean RIT 206.4, CGP 49.2, 40% hitting 2× growth).
- **Measurement proxy**: psychometric parity evidence (Rasch/MLEF/CAT, simulations) plus the staged, disclosed path to concurrent validity.

---

## 5. Scope & honest next-steps (what is bounded, and what a pilot confirms)

- **RMSE and bias are open, not resolved.** RMSE 4.73 RIT (vs <4.0 target) and +2.62 RIT systematic bias are real, current, flagged findings from the latest production-path re-run — not settled by the older, better-looking numbers. A reviewer should treat root-cause analysis of the bias as a precondition for any linking study, not a footnote.
- **No concurrent validity data exists.** Simulation 4's r=0.909 is against a *synthetic* MAP-like bank, not real NWEA items or real paired student scores. This is the single largest gap between "the algorithm is right" and "the score means what MAP's score means" — and it is Open by design, requiring a pilot cohort that doesn't exist yet.
- **Item bank is uncalibrated and comparatively small.** 650 items vs. NWEA's 40,000+; b_provisional values carry effectively infinite SE pre-field-trial; 41/650 items exceed a 30% exposure rate and 322/650 are never served in the current simulation — bank depth is a real constraint on item security and fine-grained discrimination, not a blocker to piloting.
- **Legal/trademark review is open.** "MAP" is an HMH-registered trademark; UI language has been revised to "MAP-like" and scraping/replica framing removed, but a full legal review of naming and UI provenance is an open gate (per project memory) before wide external distribution.
- **RIT output is blocked by design, and that restraint is a strength, not a gap to paper over.** The product deliberately reports only logit θ ± SE pre-linking. Reward this honesty; do not accept any document that back-doors an "approximate RIT" into a student- or school-facing report.
- **A positive simulation read is a target, not a proof.** Whole-intervention effects on standardized reading scores in the literature move g≈0.1–0.2; a strong Sim 1 r does not itself predict a large real-world MAP gain. Treat any "this will raise MAP scores by X" claim as [OPEN] unless it cites pilot data.

---

## 6. Tradeoff logic (judge the recurring decisions fairly)

| Decision | Deliberate/defensible (reward) | Genuine red flag (penalize) | Caveat (don't cry wolf) |
|---|---|---|---|
| IRT model | Rasch 1PL, matches MAP's stated model, avoids inventing 3PL parameters pre-calibration | Claiming 3PL-level precision from an uncalibrated 1PL bank | Rasch is the *correct* pre-pilot choice, not a shortcut |
| Domain weights | 13/13/13 traced to NWEA Table 3.2 | Still citing 45/40/15 anywhere | The correction itself is a strength — shows the team fact-checks against primary sources |
| Item formats | Naming which 3 of 6 are Reading-2–5-confirmed vs. pool-wide | Presenting all 6 as equally confirmed | The distinction is subtle; check every doc states it correctly |
| RMSE/bias reporting | Disclosing 4.73 RIT and +2.62 RIT as flagged, open findings | Downgrading them to "narrowly below" or omitting them from a summary | A number moving the wrong direction between report versions is itself a finding — don't let a later doc quietly drop it |
| Concurrent validity | Naming Sim 4 as synthetic-bank simulation, not real MAP comparison | Any phrase implying "we've shown our score equals a MAP score" | A high simulated r is genuinely encouraging — just not commercial proof |
| RIT output | Blocked pre-linking, disclosed as the top limitation | A specific RIT/percentile/CGP number appearing anywhere pre-pilot | Direction-only claims (e.g., "we expect this to help") are fine; magnitude claims are not |
| UI fidelity | "MAP-like" interface for response-process validity, legally reviewed language | "Pixel-accurate replica," scraped-from-competitor framing, or unresolved trademark language in shareable docs | Interface fidelity is a legitimate validity argument (AERA 1.13) when framed and named correctly |
| Bank size/exposure | 650 items disclosed against NWEA's 40,000+, exposure-control plan named | Presenting the 650-item bank as pilot-scale-sufficient without the exposure caveat | 650 is genuinely adequate for a Stage-1/2 pilot per Stocking's pool-ratio guidance; the disclosure is what matters |

**Blockers vs. improvements:** separate what should stop a pilot from proceeding (an unresolved legal/trademark exposure on external material, a document making an unlicensed RIT or concurrent-validity claim) from what a pilot itself will fix (calibration, bias root-cause, bank depth). **Name the seam:** the one structural question a reviewer should resolve is whether this package is honestly framed as "algorithm + blueprint proven, RIT/concurrent-validity explicitly open" — or whether any document has let a flagged number (RMSE, bias) or an unproven claim (RIT equivalence, "meets MAP benchmark") slip through unqualified.

---

## 7. How to use this + sources

1. Load §1 (fixed reference points) and §2 (why the engine is built this way).
2. Check §3 against the *latest* validation report, not older superseded numbers — confirm RMSE/bias are still disclosed as flagged.
3. Weigh §4 (the ask) against §5 (honest tensions) — is the disclosure complete, and does it match the current re-run?
4. Run each design choice through §6; tag NWEA-VERIFIED/SIMULATION/DIRECT-PULL/DERIVED/AUTHORING-DECISION/OPEN.
5. For a full adversarial line-by-line audit of a specific document, hand off to the **map-approval-case** agent (`.claude/agents/map-approval-case.md` in this repo) — it applies this same ground truth at document-review granularity (number consistency, benchmark honesty, source discipline, legal/reputational risk).
6. Decide on the pilot ask, and name the one load-bearing seam (§6, last line).

**Sources (grounding, re-verifiable):**

- **Validity package** (this repo): `docs/validity/MAP_PROXY_VALIDITY_CASE.md` (master brainlift), `01_PSYCHOMETRIC_DESIGN.md`, `02_ITEM_BANK.md`, `03_SIMULATION_EVIDENCE.md`, `04_CONCURRENT_VALIDITY_PLAN.md`, `05_LIMITATIONS.md`, `06_SOURCES.md`.
- **Latest validation re-run**: `engine/scripts/validation/report_g2g5_650.md` (2026-07-02, 650 items, production selection path) — this supersedes `engine/scripts/validation/report.md`.
- **Repo ground truth / hard constraints**: `CLAUDE.md` in this repo — constraints C1–C13 and the NWEA-verified facts table (item formats, domain weights, 2025 RIT norms, Lexile bands).
- **Design brainlift**: `docs/ADAPTIVE_MAP_BRAINLIFT.md`.
- **Exam spec (current)**: `docs/exam-spec/CAT_MAP_EXAM_SPEC.md` (adaptive CAT; supersedes the historical `G3_MAP_EXAM_SPEC.md` fixed-form design).
- **Approval-case authoritative docs** (external, ti-courseplans repo): `courses/map-proxy-assessment/validity/00_CASE_FOR_APPROVAL.md`, `00_BRAINLIFT.md` — mirrored into this repo via PR #25.
- **Companion agent** (same repo, `.claude/agents/`): `map-approval-case.md` — adversarial gap-audit + case-building agent; use it for line-by-line document review, use this skill for the reasoning context that audit is checked against.
- **Primary NWEA sources**: *MAP Growth Technical Report 2025* [NWEA-2025-TR], *MAP Growth Norms Technical Manual 2025* [NWEA-2025-NM] — full APA citations in `docs/validity/06_SOURCES.md`.
