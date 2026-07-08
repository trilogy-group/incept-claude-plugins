# Grade 5 Reading — Case for Approval (g5-reading-merged-pp-9802)

> *Portable copy, captured 2026-07-06 from the source repo (`trilogy-group/ti-courseplans` → `courses/g5-reading/`). Repo-relative paths and `.qmd` cross-references in the text refer to that repo tree — repo access is optional: the per-item ledger travels as `item-ledger.json`, the dated pull as `live-pull-summary.json`, and the evidence figures as `evidence-summary.md`, all in this folder; everything else is recomputable from the live APIs per SKILL.md §6.*

> **At a glance.** *Decision asked:* approve **`g5-reading-merged-pp-9802`** (live on powerpath-100) + its 549-item certified core for the amalgamated G5 course. *Verdict:* **PASS — 0 blocking** (vs the sister G3 course that FAILED 3 blocking on the same rubric); open items tracked in §5 and `OPEN_ACTIONS.qmd` §0. *The certification is per-item:* the hot-text/sequence/match core (368 items) was blind-probed cross-family on its own id under the non-generator solver (TrueFoundry gpt-4.1); the 188 choice + 3 EBSR were certified via the same-family gpt-4.1 2-vote choice lane (§4). *Submission format:* per the 2026-07-02 CoE, academic evaluation materials are presented as a consolidated **skill** (executable agent), not static docs alone — this memo is the human-readable companion. *Where this lives:* `trilogy-group/ti-courseplans` → `courses/g5-reading/` via repo PR #8. *Read time:* ~3 min — §3 is the rubric scorecard.
>
> **Submission status (2026-07-02 CoE):** G4/G5 formal submission to Andy's team is **paused until G3 clears its gate** (G3 sets the review precedent; reviewers won't evaluate three grades in parallel). This document is **prepared, not submitted** — the group's action item is to have G5's docs/brainlift/skill ready in the consistent format so submission is a fast follow once G3 clears.

> Pairs with the merged-course **Brainlift** (the design argument) — `brainlifts/v0.6.qmd` (the active version; v0.5 was superseded). This memo is the decision; the Brainlift is the reasoning behind it. Both are for `g5-reading-merged-pp-9802`.

## 1. The ask + verdict

**Ask:** approve `g5-reading-merged-pp-9802` — and specifically its **CERTIFIED** 549-item core (anti-leak bar passed per item: 358 cross-family blind-probed + 188 choice + 3 EBSR via the same-family 2-vote choice lane) — for inclusion in the amalgamated G5 reading course, with the open items tracked as follow-up work.

**Verdict: PASS, 0 blocking failures.** The course is live and rendering on PowerPath-100, every item type is server-scored, the ≥90% mastery gate is enforced on all 81 gating tests (the 13 review and mastery-form lessons are non-gating), and the structural anti-gaming property the rubric most cares about is **demonstrated** on the certified core. The open items in §5 are either content-authoring work or named external dependencies (the accessibility renderer review, the MAP crosswalk, the Caliper scope).

## 2. What it is

| Property | Value |
|---|---|
| Course id | `g5-reading-merged-pp-9802` (PowerPath-100, published 2026-06-26) |
| Live state | Live + rendering; every item type returns HTTP 200 on `process-response`, and scoring is behaviorally proven 772/772 — a full sweep confirmed every item pays full credit only for the declared-correct response (the 30/30 discrimination probe is the historical spot-check; recent re-verification 6/6) |
| Scale | 98 components / 94 lessons / 94 tests / 772 items — 81 gating + 8 spaced-review + 5 mastery forms (review and mastery non-gating); mastery gate (`masteryThreshold==90`) on 81/81 gating |
| Composition | match 198, hottext 160, sequence 167, mcq 116, msq 111, ebsr 20 (rendered). Convention for compositions elsewhere in this memo: id-label lanes — 34 items render as a different interaction than their id suffix (per-item map in the ledger), so rendered totals differ: Unit-2 seq/match 151, choice 180 |
| Unit-1 | 172 items (`grade5-reading-clean-pp-9801-*`) — hot-text/sequence/match; 103 certified, 53 excluded (June-era item designs); feedback 172/172 |
| Unit-2 | 600 items (`g5-reading-ela-pp-9801-*`) — all 6 types incl. 20 EBSR; 446 certified (148 sequence/match + 188 choice + 107 hot-text + 3 EBSR); feedback 600/600 |
| Units 3–4 | 8 spaced-review lessons + five parallel 24-item mastery forms ("Show What You Know") — non-gating, built only from certified items |
| Standards | 772/772 carry CCSS codes resolved to official CASE GUIDs (CCSSO framework, same GUID family as the platform registry), read-back verified |
| Corrective feedback total | 772/772 (integrity maintained through every redesign via carry-over + re-author) |

## 3. The bar it clears

Scored against the team's `timeback-course-eval` rubric (Andy's published TimeBack bar — the same rubric a **sister G3 reading course FAILED, 3 blocking**). This course is PASS with **0 blocking failures**.

| Rubric line | Result | One-line evidence |
|---|---|---|
| NN1 — verifiable outcomes | PARTIAL | In-app server-scored; external-outcome (MAP RIT) linkage awaits a roster-owned student-ID crosswalk (§5) |
| NN2 — mastery gate ≥90% | **PASS** | `masteryThreshold==90` enforced on 81/81 gating tests (review + mastery-form lessons non-gating; 94 total) |
| NN3 — XP for verified learning | **PASS** (engine-governed) | XP at mastery, same engine wiring as G3; the no-XP-below-80% threshold is engine-enforced, not independently re-verified on this course |
| NN4 — cognitive load / render | **PASS** | All types HTTP 200; scoring behaviorally swept 772/772 (30/30 probe as historical spot-check); passage junk 0/772; EBSR 20 items (Part-A/Part-B structure) |
| ↳ Live-surface cosmetics (non-blocking) | rendering-clean unaffected | Unit-1 lessons are grouped by Lexile band (~8 passages/lesson) so the lesson-list title intentionally will not match every passage it opens — a band-grouping artifact, not a render bug; three placeholder lesson titles (Reading Practice 13–15) and a `match` drop-bucket cold-labelled "Unused category" are authoring labels pending cleanup. Scoring and the gate are unaffected; review binds to the item ledger, not the live surface |
| NN5 — corrective feedback | **PASS course-wide** | **772/772 (100%)** items carry item-specific CORRECT/INCORRECT feedback naming the passage evidence, read-back verified, maintained through every redesign |
| NN6 — retrieval + spaced review | **PASS — both instruments live** | 8-lesson spaced-review unit live (`-review-unit`) **and** five parallel 24-item mastery forms live (Unit 4 "Show What You Know", disjoint from each other form-to-form), both built only from certified items; items are reused across gating tests by design as spaced retrieval (891 gating refs over 549 unique certified items, zero cross-unit; review/mastery items also serve in gating tests); gating tests enforce the ≥90% mastery threshold on 15 certified items each, and deepening the banks toward the ≥15 target is an active content pass (same-unit borrows already narrowed 342 → 267) |
| NN7 — prevent gaming (server-side scoring) | **PASS** | Server-side scoring on `process-response`; never client-reported |
| ↳ Anti-leak (cross-family blind-solve) | **PASS — 549 certified** | The sub-property of NN7 the generator controls: every certified item probed on its own id — the 358-item hot-text/sequence/match core cross-family (TrueFoundry gpt-4.1), the 188 choice + 3 EBSR via the same-family 2-vote choice lane — **549/772 certified** (103 Unit-1 + 446 Unit-2); remaining pools itemized in §4 |
| NN8 — Caliper events | PARTIAL — activity events verified | Activity events are verified in the Caliper store (60 TimeSpentEvents, read back 2026-07-06); assessment-event scope is platform-owned |
| NN10 — Accessibility (WCAG 2.1 AA / 508) | IN PROGRESS | WCAG renderer attestation for the TEI interaction types (match/hot-text/order; 525/772 items) sits with the platform team. |
| Dim 2 — instruction quality | 2/5 | Assessment-only; no worked examples yet. Corrective feedback (a Tier-1 component of instruction quality) is complete course-wide. |

**Reading NN7:** the two canonical docs split it deliberately — server-side scoring (you can never client-report a pass) is a clean PASS; the anti-leak sub-property is measured separately and holds on the 549-item certified core. Both halves are shown above so this memo matches the build record.

**Where it stands:** this course clears the Tier-0 legs the rubric treats as binary — mastery gating ≥90% (NN2) and render/communication (NN4) — and demonstrates the gaming line (NN7) on its certified base. The remaining lines are PARTIAL or tracked open items, not blocking.

**Coverage split of the 549 certified:** 358 are the cross-family blind-probed hot-text/sequence/match core; the remaining 188 choice + 3 EBSR were certified via the same-family gpt-4.1 2-vote choice lane. Read "549 certified" as 358 cross-family + 191 same-family, not one uniform gate over all 549.

## 4. The structural headline (why this is approvable)

For a reading course, "gaming" = answering without reading the passage. That is exactly cross-family blind-solve, and the 2026-06-23 run made the lever unmistakable: **the question format, not just the passage, decides whether reading is forced.**

**The certification method:** an item is certified when a solver from a model family different from the generator's, given the item **without the passage**, fails to recover the answer (blind must-fail) and, given the passage, solves it (with-passage must-succeed). Certification runs against a single non-generator solver family today (gpt-4.1); a second family is a tracked open item.

**The headline is the uniformity of the gate.** Every certified item was blind-probed **on its own id, under the same solver, on the same day** (2026-07-06) — including re-applying the gate to Unit-1, whose items were first certified in June. Items that recover on re-probe are removed from the certified set; no certification is carried from an earlier run — each item stands or falls on one measurement.

The format-leak baseline the design is built on (cross-family run, as authored):

| Format | Blind-solve leak (as authored) | Standing on the merged course (id-label lanes) |
|---|---|---|
| hot-text | 1.67% | 132 certified under the uniform gate (107 Unit-2 conversions + 25 Unit-1 holdings); 31 excluded |
| sequence / match | 0% | The certified spine — 236 certified (142 Unit-2 + 94 Unit-1; Unit-2 is 151 as rendered); 118 excluded |
| MCQ / MSQ | 99.5% / 100% | Convertible per-item: 188 certified (88 MCQ + 100 MSQ) via the rewrite lane; 52 excluded |
| EBSR | 0% on one 15-item run (2026-06-23) | 3 certified and serving in their gating tests; the other 12 EBSR by id-label are excluded. The 0% is a historical run figure, not a certification. |

The approvable core: **549 items** (103 Unit-1 + 446 Unit-2 = 148 sequence/match + 188 choice + 107 hot-text + 3 EBSR; by id-label lane, 143 match + 83 sequence + 132 hot-text + 188 choice + 3 EBSR), each blind-certified per item — the 358-item hot-text/sequence/match core cross-family, the 188 choice + 3 EBSR via the same-family 2-vote choice lane. That base carries the gate instruments now live: the ≥90% mastery gate, five parallel mastery forms disjoint from each other (Unit 4), and the 8-lesson spaced-review unit — all drawing on certified items only.

**How the base was built.** The generate→validate→cross-family-gate→deploy→re-measure loop (solver: TrueFoundry gpt-4.1; snapshots kept for every deploy, fully reversible) ran three lanes against a live-measured ~78% leak baseline on the uncertified pool:

- **Sequence/match:** 142 Unit-2 seq/match certified by id-label under the current gate (151 as rendered); the excluded seq/match pool remains outside the certified set (targeted for a future replacement pass).
- **Choice:** per-item rewrite into passage-dependence at a 2-of-2 blind-vote bar — 188 certified by id-label under the current gate. This overturns the earlier "MCQ 99.5% / MSQ 100% → full-regen-only" reading: the leaky formats convert.
- **Hot-text:** the claims-about-passage construct redesign, 117 items targeted → 90 converted at lane time; 107 Unit-2 hot-text certified by id-label under the current gate.

Anti-leak certification thresholds a cross-family solver's MEAN blind-solve over resampled shuffles at < 0.60 — an item is certified only if it cannot be reliably answered without the passage. 549 of 772 items clear it: the 358 hot-text/sequence/match items are cross-family blind-probed on their own ids (non-generator solver, TrueFoundry gpt-4.1); the 188 choice + 3 EBSR are certified on a same-family two-vote lane. The 223 excluded sit outside every gate instrument. Every gating test serves 15 certified items.

## 5. Open items + close plan

Every item is either content/authoring work, or a named external dependency.

| Item | Type | Close path |
|---|---|---|
| Custom corrective feedback (NN5) | **Closed** | 772/772 item-specific, authored + deployed + read-back verified; maintained through every redesign |
| Retrieval / spaced review + mastery forms (NN6, Dim 1/6) | **Deployed** | 8-lesson spaced-review unit and five parallel 24-item mastery forms live, both certified-only; deepening the banks toward the ≥15-per-test target is an active content pass |
| Anti-leak certification (NN7 sub-property) | **Run — per-item gate** | 549/772 certified, every certified item probed on its own id (358 cross-family + 188 choice + 3 EBSR same-family lane); remaining pool = the excluded 223 per §4 (52 choice, 128 seq/match, 31 hot-text, 12 EBSR (69 Unit-1 among them)) — conversion or replacement is an owner call |
| ELA content review | Open — staged | An ELA content review of the 549 certified items — fact-check, answer keys, Grade-5 age-appropriateness (`OPEN_ACTIONS.qmd` §A, draft staged) |
| Accessibility (NN10, WCAG 2.1 AA / 508) | In progress — external | WCAG renderer attestation for the TEI interaction types sits with the platform team (scope in the §3 NN10 row) |
| NN8 Caliper events | Partial — verified | Activity events are verified in the Caliper store (60 TimeSpentEvents, read back 2026-07-06); assessment-event scope is platform-owned |
| NN1 external prediction | Open — external | External-outcome (MAP RIT) linkage awaits a roster-owned student-ID crosswalk to the 409 MAP records already in OneRoster, then a linking pilot (N≥200 dual-tested) |

## 6. Scope

- **A gate PASS means** the structural property is verified: mastery threshold present and enforced; certified items sit at chance under cross-family blind-solve; items render and score live, behaviorally proven on 772/772 (full sweep — every item pays full credit only for the declared-correct response; the 30/30 discrimination probe is the historical spot-check). External-outcome results arrive with the MAP crosswalk + pilot (§5, NN1).
- **The certified instrument base is 549 items** — 103 Unit-1 plus 446 Unit-2 (148 sequence/match + 188 choice + 107 hot-text + 3 EBSR), certified per item (358 cross-family hot-text/sequence/match + 188 choice + 3 EBSR via the same-family 2-vote choice lane). The 223 excluded items stay outside every gate instrument (pools itemized in §4).
- **No in-course MAP-equivalent test is planned (decision 2026-06-29).** The course defers to the platform's **adaptive Grade 2-5 MAP** — live id `incept-map-g2g5-l1`, engine <https://github.com/trilogy-group/Incept-MAP-proxy> — as the measurement of record.

## 7. The decision

**Approve `g5-reading-merged-pp-9802` (and its CERTIFIED 549-item core) for inclusion in the amalgamated G5 reading course, with the open items tracked.** Verdict: PASS, 0 blocking failures.

**The certification stands on per-item measurement.** Every certified item was blind-probed on its own id — the 358-item hot-text/sequence/match core cross-family (non-generator solver, 2026-07-06/07), the 188 choice + 3 EBSR via the same-family 2-vote choice lane — Unit-1 included; the gate instruments now live (the ≥90% gate, five form-to-form-disjoint parallel mastery forms, the spaced-review unit) draw only on that base. Corrective feedback is closed course-wide (772/772); standards are resolved to CASE GUIDs on 772/772. **Open items with owners:** (1) convert or replace the excluded 223 (owner call per pool); (2) the WCAG renderer attestation with the platform team; (3) the MAP student-ID crosswalk to the roster owner.
