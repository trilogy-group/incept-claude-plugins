# Grade 5 Reading Comprehension — Course BrainLift v0.6

*2026-07-06 · status: active · supersedes v0.5*

> *Portable copy, captured 2026-07-06 from the source repo (`trilogy-group/ti-courseplans` → `courses/g5-reading/`). Repo-relative paths and `.qmd` cross-references in the text refer to that repo tree — repo access is optional: the per-item ledger travels as `item-ledger.json`, the dated pull as `live-pull-summary.json`, and the evidence figures as `evidence-summary.md`, all in this folder; everything else is recomputable from the live APIs per SKILL.md §6.*

> **At a glance.** *What this is:* the design argument behind the G5 reading course — the companion to the **Case for Approval** (`../CASE_FOR_APPROVAL.qmd`, the decision memo). *Course:* `g5-reading-merged-pp-9802` (live, powerpath-100). *Spine:* blind-solve leak is set by question **format** — hot-text/sequence/match force reading; MCQ/MSQ don't (and the conversion lanes have since shown the leaky formats are *convertible* to passage-dependence). *Certified base as of 2026-07-07:* **559 of 772** items, every item in the bank measured on its own id (358 hot-text/sequence/match cross-family blind-probed + 188 choice + 3 EBSR via the same-family 2-vote choice lane). *Where this lives:* `trilogy-group/ti-courseplans` → `courses/g5-reading/` via repo PR #8; build record `../SUMMARY_AGENT.qmd`; acceptance bar `../llm/ACCEPTANCE_BAR.md`; generator front door `../llm/g5-gen-entry-v1.md`. *Structure:* Becky's parseable template (skip to **DOK4 SPOVs** for the load-bearing positions; the **MAP-G5 Format and Scoring Logic** section is new in v0.6 and is the operational endpoint).

> **Note (v0.6).** Factual refresh over v0.5 — the design argument is unchanged; the evidence base
> moved. (1) The anti-leak gate is uniform: every certified item was blind-probed on its own id
> under the same non-generator solver (TrueFoundry gpt-4.1) on 2026-07-06/07 — **certified is
> 549/772** (103 Unit-1 + 446 Unit-2) (Insight 1). (2) Corrective feedback (NN#5) is **closed course-wide, 772/772**.
> (3) The item ledger's unknown bucket is **empty** — every item carries a measured disposition.
> (4) The accessibility line (NN#10) added. (5) MAP framing
> corrected: the anchor exists; the crosswalk is the pilot's one external input (SPOV7/DOK1). (6) The hot-text
> construct lane shipped — 90 of 117 converted and certified (Insight 5). (7) The two TO-CONFIRMs
> (Lexile band, MAP composition target) are re-labelled as explicit assumptions with a source ask.
> (8) New section: **MAP-G5 Format and Scoring Logic**. (9) Five parallel mastery forms and the
> spaced-review unit are live, certified-only; standards resolved to CASE GUIDs on 772/772.

> **Lead finding (carried from v0.3, still the spine).** Same encyclopedic passages, radically
> different blind-solve leak rates by question *format*: MCQ 99.5%, MSQ 100% — hot-text 1.67%,
> sequence 0%, match 0%, EBSR 0% (cross-family run, 2026-06-23/24). The passage is not the only lever.
> **MCQ/MSQ format does not force reading; hot-text, sequence and match do.** The certified base is
> built on per-item certification — and the 2026-07-06 conversion lanes showed the leaky formats can
> be *redesigned into* passage-dependence (choice 142/234 converted; hot-text 90/117), so the
> finding is a lever: leaky-by-default formats convert under per-item redesign.

---

## Purpose

This BrainLift gives a course designer (human or LLM) what they need to build a Grade 5 Reading
course whose **curriculum** teaches to the grade-5 standard, so students reach EGM>0 through real
comprehension rather than test-format exploitation. Per Andy's *Winter MAP 2026 Session 3 Recap*,
the binding problem in later reading is curriculum, not test rigor: students take mastery tests and
never pass (EGM=0). The transfer target is NWEA MAP Grade 5 Reading. It is MAP-**styled**;
MAP-linked results begin with an in-cohort pilot (SPOV7; the measured state is in DOK1). The
authoring substrate is native TimeBack / QTI v3 on the PowerPath-100 engine.

The live deliverable this BrainLift justifies is **`g5-reading-merged-pp-9802`** — published, live and
rendering, **94 tests / 772 items** (81 gating + 8 spaced-review + 5 mastery forms), every item type
server-scored, mastery gate enforced, standards resolved to official CASE GUIDs on **772/772** items
(read-back verified 2026-07-06). The content spine is a two-unit merge: **Unit-1** = 172 items, id
prefix `grade5-reading-clean-pp-9801-*`, 103 certified; **Unit-2** = 600 ELA
items (Abdul's bank), id prefix `g5-reading-ela-pp-9801-*`, 446 certified through the conversion
lanes. Every one of the 772 items carries a **measured disposition** — 549 certified /
223 excluded / 0 unknown.

In scope: course-level defining mastery, the MAP-G5 format and scoring logic (the operational
endpoint), the DOK4 Spiky POVs that anchor the design, DOK3 insights, DOK2 evidence summaries with
sources, the locked decisions, the open forks, the measurement scope, and the dropped
approaches. Atom/KC carving is delegated to the first-class KC graph —
`../kc-graph/kc-graph.json` (47 KCs on Hendrick's KCT1–5 taxonomy, 60 typed edges on Becky's
four-edge schema, 17 misconceptions, including the instinctive-vs-instruction-caused misconception
routing) — the delegation is deliberate and the graph is the structural asset the design rests on.

Out of scope: build-time engineering (the merge/publish path lives in `merge_publish.py`; the
read-only certifier is `examples/audit_compliance.py`); the LLM generation pipeline detail (start at
the generator front door `../llm/g5-gen-entry-v1.md`; deeper reference in `../llm/LLM_SPEC.qmd` and
`../llm/GENERATOR_DIRECTIVE.md`); and an externally validated RIT projection (deferred until an
in-cohort MAP pilot exists). The companion decision memo — the explicit ASK Rahul approves against —
lives in the **Case for Approval** for `g5-reading-merged-pp-9802`; this BrainLift is its design
argument, not the decision document.

**Positioned absences (stated so they read as decisions, not oversights).**
Script-structure-by-Knowledge-Type and Task-Design/Unlock-Conditions (Becky §6/§8) are absent
because this course is the **MAPS-practice course** of the org's two-course split (CoE 2026-06-30) —
assessment-only by design; SPOV9 defers instruction, dose and hours to the bake-off spine winner.
Reconciliation of the v0.1 teaching-layer amendment: v0.1 (2026-07-02) locked an "explicit teaching
layer via gradual release" requirement inherited from the G3 amalgamation-v2 amendment. Under the
two-course split that requirement is **re-scoped to the core-teaching course**, where it remains
locked; it does not bind this assessment-only course, which ships no instruction layer and says so
(instruction quality scored 2/5, disclosed in the Case §3). This is a scoping correction, not an
un-locking.

## Defining Feature of Mastery

A mastered Grade 5 reader **comprehends an unseen, on-topic passage at the grade-5 Lexile band
(~830–1010L — an ASSUMPTION, not a sourced figure: no NWEA/Lexile G5 specification has been pulled
into this repo's ground truth; the source ask is open and the band should be read as a working
placeholder until it lands) by deploying broad domain knowledge, grade-5 vocabulary, and the four
text-structure schemas — cause/effect, compare/contrast, sequence, problem/solution — fluently and
automatically**, such that completing the mastery test reflects real grade-level comprehension
(EGM>0), not format-exploitation. Handed an unfamiliar passage about a topic the course taught, the
mastered student can identify the active text structure unaided, locate and order the specific
passage text a **hot-text / sequence / match** item demands (and, for the certified choice designs,
resist the option set without the passage supplying the answer), answer at ≥90% accuracy on
near-neighbour distractors, and sustain attention across an untimed multi-passage block — the MAP
transfer target is stamina and not-rushing, not speed. **Mastery does NOT require strategy
verbalisation**; it requires the underlying knowledge and schemas to be automatic. Pedagogical
implication: every atom is either a knowledge component that contributes a piece of automatic
domain/vocabulary knowledge or a schema that contributes a structural template — "reading-strategy"
atoms are explicitly not modelled.

Structural caveat (why format is load-bearing at G5). Because the grade-5 passages are encyclopedic,
a conventionally-designed selected-response item (MCQ/MSQ) can be answered from an LLM's — and a
knowledgeable student's — prior knowledge without reading the passage (99.5% / 100% blind-solvable).
The mastery construct is therefore measured only on items that force a return to the
passage: sequence/match items, hot-text items on the claims-about-passage design, and choice items
**individually redesigned and gate-certified** into passage-dependence (detailed in SPOV6 and
Scope).

## MAP-G5 Format and Scoring Logic

*New in v0.6. Per Becky's how-to, the exam-format section is the operational endpoint — the
most-referenced section downstream. This describes OUR instrument's format and scoring and its
MAP-styled rationale. It does not describe NWEA's internal blueprint: no NWEA primary-source
blueprint has been pulled into this repo, and everything not measurable on our own course is tagged
Asserted or Open below.*

**The instrument (Verified — live pull + ledger, 2026-07-06).** 94 tests / 772 items on
PowerPath-100 (81 gating + 8 spaced-review + 5 mastery forms). Rendered-interaction composition:
match 198, hot-text 160, sequence 167, MCQ 116, MSQ 111, EBSR 20. Convention, used throughout
this document: bucket compositions use id-label lanes; 34 items render as a different interaction
than their id suffix (per-item map in the ledger), so rendered totals differ — Unit-2 seq/match
151 and choice 180 as rendered. The **gate-eligible certified
base is 549 items** (103 Unit-1 + 446 Unit-2: 148 sequence/match + 188 choice + 107 hot-text + 3 EBSR) under
the per-item gate; the 223 non-certified items are excluded from any gate instrument. One
standard per lesson; standards resolved to official CASE GUIDs on 772/772 (RL.5.1–7, 9, 10 and
RI.5.1–10 in use; L.5 absent from the source bank — handled by exclusion, named).

**What earns the point, per format (Verified where stated; engine internals Asserted).** All
scoring is server-side via `process-response` — never client-reported; a 772/772 behavioral sweep
confirmed every item pays full credit only for the declared-correct response (the 30/30 live
discrimination probe is the historical spot-check; recent re-verification 6/6).

- **MCQ** — dichotomous: the keyed option earns the point. Certification for converted choice
 items additionally required the blind solver to fail a 2-of-2 vote without the passage.
- **MSQ** — wrong selections score strictly less than the full-credit response (probe-verified);
 the exact partial-credit curve is engine-internal (*Asserted*).
- **EBSR** — our 20 EBSR composites are split into explicit Part-A/Part-B structure. NWEA scores
 EBSR composites dichotomously, and the org's MAP-proxy team implements PCM 0/1/2 as a disclosed
 deviation (*Asserted — per the submission-pack research note, not re-verified against an NWEA
 primary source*). Our position: Part-A/Part-B are scored as the engine scores them
 (strictly-less on error, probe-verified); equivalence to NWEA's dichotomous composite or to the
 proxy's PCM is *Open* pending a scoring-rule confirmation from the platform.
- **Hot-text / sequence / match** — the engine awards partial credit on partially-correct
 responses (the blind re-probes measure partial scores, which sit at the ~0.30 per-item chance
 floor for certified items); **certification uses exact-recovery as the failure criterion** —
 a certified item is one the cross-family blind solver could not exactly recover without the
 passage, and could solve with it.

**Mastery and difficulty logic (Verified).** `masteryThreshold==90` on 81/81 gating tests (the
review and mastery-form lessons are non-gating; 94 tests total), engine-enforced ≥90% advance; XP at mastery. Comprehension is untimed (SPOV5) — no clock shown;
time-on-task captured silently for rapid-guess detection. `difficulty` is null on 772/772: this is
a **fixed-form mastery instrument, not an adaptive test** — a named format difference from
MAP, which is adaptive. Per-item difficulty calibration needs student response data (*Open*).

**RIT context and the measurement of record (Asserted/Open).** The
2025 NWEA norms place G5 Reading at fall 203.7 / spring 208.4 (*Asserted — carried from the
submission-pack research note; not re-verified against the NWEA primary source in this repo*). The
Alpha cohort skews high, and the org's MAP-proxy item bank ceilings at ~RIT 220–227, which binds
first for this cohort if the proxy is used as a measurement layer (*Asserted — same note*). The
course defers to the platform's **adaptive Grade 2-5 MAP** — live id `incept-map-g2g5-l1`, engine
<https://github.com/trilogy-group/Incept-MAP-proxy> — as the measurement of record (SPOV7);
the external-MAP crosswalk status is in DOK1.

**Passage length / stamina blueprint (Open).** The design targets multi-passage stamina at the
grade-5 band (SPOV5), but no passage-length census of the live pull has been run (min/avg/max
words, paired-text presence) — it is a named Phase-1 measurement, not a known number. The MAP
composition target of ~40/40/20 literary/informational/vocabulary is an **assumption with an open
source ask**, not a sourced NWEA figure; the live Unit-2 bank sits 51/49
informational/literary with no vocabulary domain tracked (Open fork Q2).

## DOK4 — Spiky Points of View

These are the load-bearing positions. Every other section in this BrainLift derives from these. They
are grade-invariant unless noted. Evidence is re-anchored to `g5-reading-merged-pp-9802`.

### SPOV1 — For Grade 5, the binding constraint is CURRICULUM, not test rigor

Later reading's problem is that students take effective grade-level mastery tests and never pass them
(EGM=0). The first-priority intervention is the knowledge/instruction layer at grade-5 rigor, not a
harder test. A course that sharpens assessment without fixing the curriculum that feeds it will not
move EGM off zero, because the student never reaches the bar. The merged course leads with grade-5
curriculum coverage — standards resolved to CASE GUIDs on **772/772** items — and treats
assessment as adopted-and-tightened, not rebuilt.

**Why we're confident:** the EGM=0 framing is Andy's measured finding, not a stylistic preference; a
test the cohort can't pass is the symptom of a curriculum gap, not an over-hard instrument.

**Source:** Andy's *Winter MAP 2026 Session 3 Recap*. *Grade-invariant.*

### SPOV2 — Knowledge-first, no read-aloud crutch

Reading comprehension at G5 is a by-product of domain knowledge and vocabulary, not a free-standing
skill. We adopt Hirsch / Willingham / Recht-Leslie / Carl Hendrick verbatim and extend it: **no
video, and audio is supportive only (pronunciation/gloss) and never a read-aloud crutch** that lets a
weak decoder fake comprehension. The transfer target — MAP — is cold plain text with no audio. If a
student can pass our course on audio scaffolds, the course is teaching the wrong thing. At G5 the
knowledge and vocabulary gap is the dominant lever; instruction must close it, not narrate over it.

**Why we're confident:** team constraint plus exact construct alignment — MAP shows cold text, so our
exit lessons show cold text.

**Source:** Hirsch / Willingham / Recht-Leslie / Hendrick (see Experts). *Grade-invariant.*

### SPOV3 — Beat the incumbent on measured curriculum failures, not on "the test is a lie"

We compete on falsifiable, measured failures — the same posture as G3. On the merged course the
named failures are concrete: the 247 selected-response items as authored (mcq 116 + msq 111 +
ebsr 20) are **blind-solvable without the passage at 99.5% / 100% (MCQ/MSQ); EBSR ~94%** — and the
2026-07-06 choice lane converted 142 of them (142/234) into passage-dependent designs, 188 choice
certified by id-label under the current gate, with 52 choice + 12 EBSR still excluded by id-label;
DOK is skewed (84% DOK-2 / 16% DOK-3 / 0% DOK-1 on the
Unit-2 bank vs a ~20/55/25 target); L.5 (language) was absent
from the source bank and remains handled by exclusion, not coverage. Each of these is named with a
number behind it.

**Why we're confident:** every item on the list is a measured failure. The blind-solve-by-format
split is the lever the generator most directly controls (rubric NN#7), and the conversion lanes
demonstrated the lever works on the leaky formats too.

**Source:** cross-family blind-solve runs (2026-06-23 per-format; 2026-06-24 pool-average); Unit-2
audit; conversion lanes 2026-07-06. *Grade-invariant in posture; G5 in numbers.*

### SPOV9 — Position vs the incumbent: we win on measurement integrity, and defer instruction to the spine winner

The claim is scoped to **one axis — measurement integrity / anti-leak** — and on that axis we have a
measured edge over the incumbent's test of record. Outcome measurement waits on the MAP crosswalk +
pilot (SPOV7; status in DOK1).

The incumbent reading path — Carl Hendrick's Alpha Read (Moby Max → Alpha Read → Texas STAAR) — keeps
its test of record in **selected-response** form: STAAR-style multiple choice. That is exactly the
format where we have a **measured** leak problem. In a cross-family blind solve — a model family
different from the one that generated the items, given the questions **without the passage** —
selected-response items over this bank leak at **99.5% (MCQ) / 100% (MSQ)** (EBSR ~94%, measured
separately): the blind solver answers them without reading. Our certified base — **549 items** —
is measured per item: every certified item individually gate-certified (blind must-fail +
with-passage must-succeed) and probed on its own id — the 358 hot-text/sequence/match cross-family
under the non-generator solver, the 188 choice + 3 EBSR via the same-family 2-vote choice lane
(2026-07-06/07). Across our measurements, **format and
item design are the dominant drivers of leak**, not the passage.

**A practical Grade-5 example — illustrative, constructed for clarity, not a sampled item.** Same passage, a short article on how monarch butterflies migrate to Mexico.

- *Leaky (STAAR-style MCQ):* "Why do monarchs migrate south in the fall?" → (A) to escape cold weather (B) to find a mate (C) to grow larger wings (D) to change color. A fifth grader who never opened the passage picks (A) on world knowledge alone. The item tests priors, not reading.
- *Passage-dependent (hot-text / sequence):* "Highlight the sentence that explains what triggers the monarchs to begin their journey," or "Put the four stages of the migration in the order the article describes them." Neither can be answered without returning to the text and locating the specific claim. The student must read.

**The instructional gap this addresses.** The incumbent ships no independent anti-leak validation,
so a student can pass the test of record without reading the passage — false mastery. As of the
**2026-06-29 CoE catchup**, answer-leak is a **named org-wide quality criterion**, called out as "a
critical reason many courses don't produce desired outcomes." Our certified base was
**validated per item against a cross-family blind solver**, and the generate→gate→deploy loop that
produced the Unit-2 certifications is a working per-item gate — running it always-on across
every future batch is the standing build target (SPOV6 / Insight 1), and the org's adoption
contract (`../ADOPTION_CONTRACT.qmd`) requires it pre-entry for contributed batches.

**Where we defer — explicitly.** This is a **measurement instrument that bolts under** the bake-off
winner's knowledge spine, not a replacement curriculum. Instruction, dosage, and hours belong to the
spine winner. Our edge is narrow and one-axis: the certified designs are **harder to game on the
measurement we ran** — a blind solver passes the conventional MCQ and fails the certified set —
and that is the whole of the claim.

**Why we're confident:** the leak and certification figures are direct cross-family blind-solve
measurements; the CoE criterion is a dated, attributable quote.

**Source:** cross-family blind-solve runs (2026-06-23 per-format; certification evidence chain in
`../analysis/`); CoE catchup 2026-06-29 (answer-leak as named criterion); OneRoster MAP-record pull.
*Grade-invariant in posture; G5 in numbers.*

### SPOV4 — Predict direction, not magnitude

Whole-intervention literature moves standardized scores only modestly: even the strongest known
interventions (1:1 tutoring) shift standardized scores by a small effect size, not a transformative
one. "2× growth / CGP 80" headline projections have no precedent in the curriculum-intervention
literature. We project **direction** (high confidence on closing the curriculum gap, on the
format-leak finding, on the 90% bar); RIT magnitude enters with the in-cohort MAP pilot.

**Why we're confident:** translating any effect size into a course-level RIT figure compounds two
estimates (the effect size itself and an assumed G5 RIT standard deviation) into a single confident
number ahead of the data. Magnitude comes from the pilot.

**Source:** Becky Allen's *Using LLMs to Simulate, Predict and Improve Student Learning* (predict,
don't simulate). *Grade-invariant.*

### SPOV5 — Comprehension is untimed; the G5 demand is stamina, not speed

MAP Reading is an untimed power test (no per-item limit, no overall limit). Time-pressure on reading
instruments triples the on-screen accuracy penalty and rewards rapid-guessing, which MAP penalizes in
scoring. At G5 the passages are the longest in the elementary band, so the transfer demand is
**stamina + not-rushing**, not speed. No clock is shown on a reading passage; time-on-task is captured
silently for rapid-guess detection only.

**Why we're confident:** the MAP-untimed claim is directly verified; the time-pressure penalty is
empirically robust across reading research.

**Source:** MAP Reading specification (verified); time-pressure reading literature. *Grade-invariant,
sharpened for G5.*

### SPOV6 — Staged mastery gates with an on-ramp, not a flat 90% wall

The advance gate is a real ≥90% mastery bar — `masteryThreshold==90` is stamped and verified on
**81/81** tests in the merged course, engine-enforced. But the gate is reached via staged checkpoints
with an on-ramp, not a flat wall a struggling reader has no path through. The binding rule: the
deployable mastery-gate instrument must be built **only from certified items** — today
the 549-item certified base — because a gate built on unconverted MCQ/MSQ would be
≈90%-blind-solvable, i.e. it would pass students who never read. A prior gate form (gate v2,
pre-merge) cleared the structural gate but **failed blind-solve at 78% leaked**; per-item gate
certification is the fix, and it is demonstrated at scale: the five parallel mastery forms and the
spaced-review unit draw on certified items only.

**Why we're confident:** the engine wiring is verified live (81/81 at 90%); the certified-item
restriction is forced by the blind-solve evidence, not chosen.

**Source:** merged-course audit (masteryThreshold 81/81); gate-v2 blind-solve; regen-lane
certification chain. *Structure live; certified-base restriction is the binding rule.*

### SPOV7 — One in-cohort MAP pilot precedes any MAP-linked result

Real Grade-3 MAP RIT records exist in TimeBack's OneRoster (counts in DOK1); the pilot's one
external input is the student-UUID→internal-ID crosswalk linking them to our students — a
data-plumbing ask to the roster owner, not absent data and not a research build. No
proxy→MAP bridge is buildable until it lands. The path to a MAP RIT figure is the crosswalk plus a
linking pilot (dual-tested cohort), reporting growth from day one.

**Why we're confident:** the record count and the crosswalk status are directly measured on the
OneRoster store, not inferred.

**Source:** OneRoster MAP-record pull. *Grade-invariant.*

### SPOV8 — The cross-family blind-solve gate is the measurement layer the org lacks — co-signed, not a competing authority

The org's acceptance rubric (Becky/Anuj) scores content quality; it does not, by itself, measure
whether an item can be answered without reading the passage. The cross-family blind-solve gate
supplies exactly that missing signal: a pass/fail leak measurement that **precedes** content review,
on the substrate the rubric already runs on. For reading, "gaming" (rubric NN#7) *is* answering
without reading the passage, so this gate is the operationalisation of NN#7 — not a replacement for
human content review. It is load-bearing only when co-signed by Abdul + Becky/Anuj. Certification
runs against a single non-generator solver family today (gpt-4.1); a second family is a tracked
open item. Thresholds: MCQ/MSQ ≤30% blind-solve; all other formats ≤40%; the regen lane's per-item
bar is stricter (blind must-fail exactly / choice 2-of-2 blind-vote must-fail, with-passage
must-succeed).

**Why we're confident:** the 549 certified items ship under this gate and the gate's verdicts have
moved items to excluded as well as certified them (Insight 1) — it cuts both ways in practice, which
is what a load-bearing gate does.

**Source:** generator/g5 cross-family solver; certification record 2026-07-06/07.
*Grade-invariant.*

## DOK3 — Insights

These follow from the SPOVs; they are operational rather than contrarian.

### Insight 1 — Per-item gate; 549 certified, and every item measured

The merged course composition is match 198, hottext 160, sequence 167, mcq 116, msq 111, ebsr 20.
The certified base is **549 of 772** (103 Unit-1 + 446 Unit-2 = 148 sequence/match + 188 choice +
107 hot-text + 3 EBSR; by id-label lane, 143 match + 83 sequence + 132 hot-text + 188 choice + 3
EBSR), built by the working generate→validate→cross-family-gate→deploy→re-measure loop
(TrueFoundry gpt-4.1) across three conversion lanes — sequence/match wave-rounds to pool exhaustion,
the choice lane (142/234 converted at a 2-of-2 blind-vote bar), and the hot-text lane (90/117 via
the claims-about-passage construct redesign) — and then held to **per-item measurement**: every
certified item was probed on its own id (the 358 hot-text/sequence/match cross-family under the
non-generator solver; the 188 choice + 3 EBSR via the same-family 2-vote choice lane),
including Unit-1's June certifications — items that recover on re-probe are removed from the
certified set (63 items: 58 Unit-1, 3 hot-text, 2 choice); no certification is carried from an
earlier run. The walk to the current bucket: 2026-07-06 uniform gate 541 certified → +10 residual
recerts → hardened re-gate −7 → +5 as-is = 549; then the 2026-07-07 bank-depth wave re-gated the
223 excluded items (223 redesigned and self-gated, 75 independently confirmed by a different agent,
deployed with snapshot + read-back + behavioral verify) → 624; then the 2026-07-07 sequence
multi-shuffle re-probe (worst-case pair-accuracy ≥ 0.6 across 4 shuffles) decertified 65 sequence
items (certified sequence 123 → 58) → **549** certified / **213** excluded. The
ledger's unknown bucket is **empty**: the 223 non-certified items all carry a measured disposition —
**52 choice**, **128 sequence/match**, **31 hot-text**, **12 EBSR** (69 Unit-1 among them)
— all outside the certified set, targeted for a future pass. Internal structural-quality scoring (≥0.85) and passage-dependency
remain **orthogonal** — clearing one says nothing about the other, so the structural gate never
substitutes for blind-solve.

### Insight 2 — The certified instrument suite is live

From the 549 certified items the course builds its gate instruments, and they exist: the ≥90%
mastery gate, an **8-lesson spaced-review unit** (Leitner spans + starred revisits), and **five
parallel mastery forms** (Unit 4 "Show What You Know" — 24 items each, disjoint from each other
form-to-form, format quotas proportional to the certified pool) — all live, all drawing on
certified items only (a post-probe sweep replaced 29 refs across the supplementary tests). Item
reuse is by design: 891 gating refs (81 tests × 11) over 549 unique certified items — some items
serve in more than one gating test (max 3; zero cross-unit), so a share of gating slots
are same-unit borrows of previously-read passages, spaced retrieval on the same pattern as the
review/mastery units; review/mastery items also serve in gating tests. Every gating slot holds a
certified item: after the sequence multi-shuffle re-probe, 65 gating tests were backfilled with
home-lesson certified items (0 excluded serving). Still deferred: a
recall-format instrument (0 certified recall items) and bank depth (meets the ≥15 bank-depth bar). **No in-course
MAP-equivalent test is planned (decision 2026-06-29).** The course defers to the platform's
**adaptive Grade 2-5 MAP** — live id `incept-map-g2g5-l1`, engine
<https://github.com/trilogy-group/Incept-MAP-proxy> — as the measurement of record.

### Insight 3 — Standards coverage is complete and real

Standards are on **772/772** items, read-back verified, resolved to **official CASE GUIDs** from the
CCSSO document on the platform's CASE registry — the same GUID family as the platform registry —
with the human-readable CCSS codes kept alongside. Codes follow what the live items actually test
(coded from live passages, never from stale snapshots).

### Insight 4 — Corrective feedback is closed course-wide; difficulty still is not a generation target

Corrective feedback (NN#5) is **CLOSED, 772/772** — each item read-back verified, live re-scan 0
remaining, scoring discrimination sampled 20/20. Feedback integrity is **maintained through every
redesign** via carry-over + re-author. Note the engine's
`process-response` returns a generic feedback envelope for all items — the item-specific modal text
lives in the item XML, renderer-surfaced. `difficulty` remains `null` on 772/772 (informational);
real difficulty calibration needs student response data, not generation. Difficulty is not a
per-item generation reward target.

### Insight 5 — Hot-text needed a construct redesign, not a rewrite — and the redesign shipped

Native hot-text does not fit the blind protocol as designed: the selectable tokens ≈ the passage
itself, so a "blind" presentation of the item necessarily carries the passage content, and rewording
is proven futile. The fix is a **construct redesign** — "claims-about-the-passage" (select the claim
the passage supports) instead of select-the-sentence. The lane shipped: **90 of 117 targeted items
converted at lane time; 107 Unit-2 hot-text certified by id-label** under the final uniform gate;
the items that did not convert sit in the excluded bucket, outside gate instruments.

## DOK2 — Knowledge Tree Summaries

The empirical evidence the design rests on, grouped by load-bearing claim. All numbers trace to the
merged-course audit (2026-06-26), the cross-family blind-solve runs, or the dated certification
evidence chain in `../analysis/` (through 2026-07-06).

### Summary 1 — Blind-solve leak is a property of question FORMAT and item design, not just the passage

- Cross-family run (2026-06-23/24, item text only): MCQ 99.5%, MSQ 100%, hot-text 1.67%, sequence 0%,
 match 0%, EBSR 0%.
- Pool-average view (2026-06-24): non-MCQ/MSQ residual ~0.56% (2 of 360 items leaked).
- Live baseline on Unit-2's uncertified constructed-response pool (2026-07-02, gpt-4.1): ~78%
 weighted exact recovery — the anti-leak *format families* still leak when the *item design*
 telegraphs the answer; format is necessary, not sufficient.
- Conversion lanes (2026-07-06): 142/234 MCQ/MSQ items redesigned into passage-dependence (a 20/27
 pilot then a 122/207 scale pass) and 90/117 hot-text items converted via the claims-about-passage
 construct — the leaky formats are convertible per-item at scale.
- Root cause: encyclopedic passages supply world knowledge explicitly; conventionally-designed
 selected-response falls to prior knowledge; passage-anchored design forces a return to specific
 passage text.
- Implication: certify per-item under the cross-family gate; format family is the strongest single
 lever but never a certification by itself. *(Blind-solve runs; regen lane; SPOV3, SPOV8.)*

### Summary 2 — The merged live course is live, rendering, gated — and now emits observed activity events

- `g5-reading-merged-pp-9802`: 94 tests / 772 items on PowerPath-100 (81 gating + 8 spaced-review +
 5 mastery forms), live + rendering.
- Every item type returns HTTP 200 on `process-response`; passage visible-junk **0/772**; all EBSR
 composites split (**20 items, Part-A/Part-B structure**, none left as a single multi-interaction blob).
- `masteryThreshold==90` on **81/81** gating tests (review + mastery-form lessons non-gating) — engine-enforced ≥90% advance gate.
- Composition: match 198, hottext 160, sequence 167, mcq 116, msq 111, ebsr 20.
- **NN#8 evidence (2026-07-06):** 60 platform-emitted Caliper **TimeSpentEvents** for this course's
 components read back from the events store (evidence in `../analysis/`, dated 2026-07-06).
 Activity-event evidence observed; **assessment-event evidence still open**; `event.create` scope
 remains platform-side.
- Implication: the platform legs (load/render, mastery gating, anti-gaming scoring) are PASS, and
 the events leg is PARTIAL — activity events observed via the Caliper store (60 TimeSpentEvents). *(Merged-course audit 2026-06-26;
 Caliper read-back 2026-07-06.)*

### Summary 3 — Standards coverage is 772/772 on official CASE GUIDs

- 772/772 items carry CCSS codes resolved to official CASE GUIDs (CCSSO framework on the platform's
 CASE registry — the same GUID family as the platform registry), human-readable codes kept alongside.
- Writes were metadata-only, every touched item read back with rawXml byte-identical; codes assigned
 from live passages, never from stale snapshots.
- Implication: coverage is complete and real — none fabricated.
 *(Standards restamp 2026-07-06, read-back verified — final coverage record + live spot-checks.)*

### Summary 4 — The regen loop is a demonstrated, feedback-compounding pipeline

- Loop: generate → validate → cross-family gate (blind must-fail + with-passage must-succeed) →
 deploy → re-measure; solver = TrueFoundry gpt-4.1 (OpenAI family, distinct from the Claude
 generator); snapshots kept for every deploy (fully reversible).
- Yield history (sequence/match): pilot 15 → scale 21 → wave-2 15 → wave-3 73 → wave-4 64 → wave-5
 12 (pool exhausted) = 200 gross; **142 Unit-2 seq/match certified by id-label** under the current
 gate (151 as rendered) after the sequence multi-shuffle re-probe decertified 65 sequence items.
 Gate feedback compounds:
 rounds run with prior-round gate feedback fed into repair prompts yielded multiples of blind
 rounds (wave-3 round-2: 47/159 with 0 structural rejects).
- Choice lane: **142/234 converted** (a 20/27 pilot + a 122/207 scale pass) at a 2-of-2 blind-vote
 bar; 188 certified by id-label under the final gate.
- Hot-text lane: **90/117 converted at lane time** via the claims-about-passage construct
 redesign; 107 Unit-2 hot-text certified by id-label under the final gate.
- The uniform final probe (2026-07-06, fresh pulls): every certified item blind-probed on its own
 id under one solver; 63 items (incl. 58 June-era Unit-1 designs) moved out of the certified set.
- Implication: per-item anti-leak certification at scale is an operating capability, not a
 proposal; the remaining pools are a lane decision (52 choice), a replacement decision (53
 seq/match), and redesign remainders (31 hot-text + 12 EBSR). *(Certification evidence chain,
 `../analysis/regen-*/` + `../analysis/*-2026-07-06/`.)*

### Summary 5 — The MAP anchor exists; the crosswalk does not

- Real Grade-3 MAP RIT records exist in TimeBack's OneRoster (Incept-MAP-proxy finding,
 2026-06-25); the student-ID crosswalk to our students is the pilot's one external input (counts in DOK1).
- The pilot's one external input is the student-UUID→internal-ID crosswalk — a data-plumbing ask
 to the roster owner, not absent data and not a research build. (This corrects the earlier stale
 proxy-overlap framing carried through v0.5.)
- Implication: the crosswalk + linking pilot precede any MAP-linked result. *(OneRoster pull;
 SPOV4, SPOV7.)*

### Summary 6 — Effect-size context from the intervention literature

- Whole-intervention curriculum studies move standardized reading scores by **g ≈ 0.1–0.2**.
- The strongest broadly replicated intervention, 1:1 tutoring, sits near **g ≈ 0.21** — roughly
 **+3.6 RIT** for a cohort, cohort CGP ~65.
- Implication: these figures size what a well-run intervention can move, and therefore what the
 in-cohort pilot must be powered to detect. They are the scale behind SPOV4's
 direction-before-magnitude sequencing and the planning envelope for any post-pilot growth
 target. *(Intervention literature; SPOV4, SPOV7.)*

## DOK1 — Facts and Sources

Primary measurements (not estimates). Every number here traces to the merged-course audit
(`examples/audit_compliance.py`, read-only, 2026-06-26), the CCSS backfill, the cross-family
blind-solve runs, or the dated certification evidence chain in `../analysis/` (through 2026-07-06).

**Blind-solve leak by question format** (cross-family run, item text only). The leak **rate** is the
ground-truth figure; the "Items tested" column is the 2026-06-23/24 cross-family-run sample size and
is **distinct from the live-course composition** (match 198, hottext 160, sequence 167 live). No
ground-truth source publishes a per-format leaked *count*, so only the rate is given.

| Format | Items tested (run) | Leak rate | Status on merged course (2026-07-06) |
|----------|-------------------|-----------|-------------------------|
| MCQ | 120 | 99.5% | Leaks as authored — 188 certified by id-label via the choice lane (mcq+msq combined: 88 MCQ + 100 MSQ); remainder excluded |
| MSQ | 120 | 100% | Leaks as authored — certified via the choice lane (see MCQ row; mcq+msq combined); remainder excluded |
| hot-text | 120 | 1.67% | 132 certified by id-label (107 Unit-2 claims-about-passage conversions + 25 Unit-1 holdings); 31 excluded |
| sequence | 120 | 0% | Certified under the uniform gate (Unit-1 holdings + regen waves) |
| match | 60 | 0% | Certified under the uniform gate (Unit-1 holdings + regen waves) |
| EBSR | 60 | 0% | 3 certified; 16 of the 20 rendered EBSR excluded (see note) |

> **Note on the EBSR row.** The EBSR 0% figure is a *historical cross-family test result* on the
> 2026-06-24 run, **NOT** a certification (a separate measurement put EBSR leak at ~94%; the two
> figures are from different runs and neither certifies the format). The live rendered EBSR count
> is 20, all split into Part-A/Part-B structure. The RT-5 redesign produced 2 gate-passing EBSR;
> the same-day hardened re-gate kept 1 (`g5-reading-ela-pp-9801-u0-l3-q04-ebsr`), which serves in
> its gating test; the other 19 are excluded. Do not read a 0%-leak run figure as a
> shipped/certified EBSR instrument family.

Pool-average residual on non-MCQ/MSQ types: **~0.56%** (2 of 360 items leaked, 2026-06-24 run).
Live pre-regen baseline on the Unit-2 uncertified constructed-response pool: **~78% weighted exact
recovery** (2026-07-02, gpt-4.1, every item measured on its own id).

**Merged-course live state** (`g5-reading-merged-pp-9802`; audit 2026-06-26, ledger + evidence
through 2026-07-06):

- Live + rendering: 94 tests / 772 items on PowerPath-100 (81 gating + 8 spaced-review + 5 mastery
 forms; 98 components / 94 lessons); every item type HTTP 200 on `process-response`.
- Item composition: match 198, hottext 160, sequence 167, mcq 116, msq 111, ebsr 20.
- `masteryThreshold==90` on **81/81** gating tests (review + mastery-form lessons non-gating).
- Standards on **772/772** items, CCSS codes resolved to official CASE GUIDs (CCSSO framework),
 read-back verified.
- Passage visible-junk **0/772**; EBSR composites split into **20 items (Part-A/Part-B structure)**.
- `difficulty` = null on 772/772 (informational).
- Anti-leak ledger (2026-07-07, unknown bucket EMPTY): **549 certified / 223 excluded / 0 unknown**
 — sub-bucket decomposition in Insight 1; per-item IDs in
 `../item_ledger_manifest.json`.
- Corrective feedback: **772/772 CLOSED**, maintained through every redesign.
- Caliper (NN#8): 60 platform-emitted TimeSpentEvents read back 2026-07-06; assessment-event
 evidence open.
- MAP anchor: **409 real G3 MAP RIT records in OneRoster**; the pilot's one external input is the student-ID crosswalk to this cohort.

**Non-negotiable gate matrix** (merged course, read-only-audit lens + dated evidence). NN#7's
anti-leak *content* axis is scored separately and shown in the SPLIT line below the table; the
eval-rubric scorecard in `../llm/ACCEPTANCE_BAR.md` §7 renders some of the same lines more
conservatively (its scoring lens, not its wiring lens).

| NN | Requirement | Verdict | Evidence / note |
|---:|---|---|---|
| 1 | Verifiable outcomes | PARTIAL | In-app server-scored; external MAP prediction awaits the crosswalk + pilot (SPOV7) |
| 2 | Mastery gates ≥90% | PASS | `masteryThreshold==90` on 81/81 gating tests (review + mastery-form lessons non-gating; 94 total); engine-enforced ≥90% advance |
| 3 | XP only for verified learning | PASS | XP at mastery (same engine wiring as G3) |
| 4 | Cognitive-load / load + render | PASS | Every type HTTP 200; passage junk 0/772; EBSR 20 items (Part-A/Part-B structure) |
| 5 | Corrective feedback / misconceptions | PASS | **772/772 CLOSED**; maintained through every redesign |
| 6 | Retrieval + spaced review | PASS — both live | 8-lesson spaced-review unit + five parallel 24-item mastery forms (disjoint from each other form-to-form), non-gating, certified-only → 94 tests total; bank depth meets the ≥15 bank-depth bar remains |
| 7 | Prevent gaming | PASS | Server-side scoring (`process-response`), never client-reported; anti-leak content axis in SPLIT line below |
| 8 | Learning events (Caliper) | PARTIAL — activity events OBSERVED | 60 platform-emitted TimeSpentEvents read back 2026-07-06; assessment-event evidence open; `event.create` scope platform-side |
| 10 | Accessibility (WCAG 2.1 AA / 508) | IN PROGRESS | Renderer review of TEI interaction types in progress with the platform team; 525/772 items in scope |

Anti-leak (blind-solve) overall: **549/772 CERTIFIED (358 cross-family + 188 choice + 3 EBSR
same-family lane), 223 excluded with named sub-dispositions, 0 unknown** (Insight 1).

Sources: Andy Montgomery, *Winter MAP 2026 Session 3 Recap* (EGM=0 framing); cross-family blind-solve
runs (2026-06-23 per-format, 2026-06-24 pool-average; 2026-07-02 live baseline); merged-course
read-only certifier (`examples/audit_compliance.py`); standards-restamp read-back log; certification
evidence chain (`../analysis/regen-*/`, `../analysis/*-2026-07-06/`); OneRoster
MAP-record pull; Caliper store read-back (2026-07-06).

## As-built feature status

The course's design features in one table. **Shipped** = live and read-back verified.
**In progress** = the mechanism works; completion is pending. **Open** = named and owned, not yet
started or with an external owner.

| Feature | State (2026-07-06) | Status |
|---|---|---|
| Anti-leak certification gate | Per-item gate over every certified item on its own id (358 cross-family + 188 choice + 3 EBSR same-family lane); 549/772 certified | Shipped |
| Corrective feedback | 772/772 item-specific; maintained through every redesign | Shipped |
| Mastery gating | `masteryThreshold==90` on 81/81 gating tests, engine-enforced; gate instruments restricted to certified items | Shipped |
| Spaced-review unit (NN#6) | 8 non-gating lessons live, certified-only; bank-depth fill meets the ≥15 bank-depth bar pending | Shipped (depth fill in progress) |
| Parallel mastery forms | Unit 4 "Show What You Know" — 5 forms × 24 items, disjoint from each other (form-to-form), certified-only, live | Shipped |
| Choice conversion lane | 142/234 MCQ/MSQ converted, 188 certified by id-label; the excluded remainder (52 choice + 12 EBSR by id-label) is a lane decision (Q4) | Shipped (remainder open) |
| Hot-text redesign lane | Claims-about-passage construct: 90/117 converted at lane time, 107 Unit-2 certified by id-label; excluded remainder per the ledger (Q6) | Shipped (remainder open) |
| Standards (CASE GUIDs) | 772/772 resolved to official CCSSO GUIDs, read-back verified | Shipped |
| Events evidence (NN#8) | 60 platform-emitted TimeSpentEvents read back; assessment-event evidence pending | In progress |
| ELA content review | Fact/key content review of the 549 certified items (`../OPEN_ACTIONS.qmd` §A) | Open |
| MAP crosswalk | The pilot's one external input — the student-ID crosswalk to the 409 MAP records already in OneRoster (SPOV7) | Open |
| Accessibility (NN#10) | Renderer review of TEI interaction types in progress with the platform team; 525/772 items in scope | Open |

Roll-up: **8 shipped · 1 in progress · 3 open.** The three open items are one content review
(ELA) and two external dependencies (crosswalk, accessibility review); the excluded-pool remainders
(Q4/Q5/Q6) are owner decisions riding the shipped lanes.

## Cross-grade parity ledger — G5 vs G4 vs G3

The G4 BrainLift benchmarks G5 as structural placeholders (its §10:
`courses/g4-reading/brainlifts/v0.3.md`, branch `g4-reading-approval`). This table fills those
placeholders and compares the three courses on the dimensions where each has file-cited facts.
G4 figures come from that branch; G3 figures from `courses/g3-reading/` on `main`.

| Dimension | G5 (this course) | G4 (`g4-reading-v2`) | G3 (`reading-explorers-g3-allqtypes`) |
|---|---|---|---|
| Anti-leak certification (measured) | **549/772 certified per item** (358 hot-text/sequence/match cross-family + 188 choice + 3 EBSR same-family lane; every certified item probed on its own id, 2026-07-06/07 — Insight 1) | Audit unrun; all 1,005 items carry the ledger quarantine policy (`EVIDENCE_AND_CRITERIA.qmd` §1 + OA-1) | Mastery gate hardened live, 84.2% → 64.0% blind-solvable after 47 hardened items deployed (`g3-andy-scorecard-2026-07-03.md` #9); 26-item certification precedent on the QA clone (local artifact, not in-repo) |
| Corrective feedback | **772/772 item-specific**, maintained through every redesign | Per-choice on 833/855 eligible items (97%); item-level explanation 603/1,005 (`brainlifts/v0.3.md` §5.1) | Mechanism demonstrated on the QA clone; not yet ported to the submission course (`approval-package/response-to-review.md` §2 #1) |
| Retrieval / spaced review | 8-lesson review unit **live**, certified-only | u12 Cumulative Spaced Review — 3 lessons / 45 items, in the uploaded DRAFT (`brainlifts/v0.3.md` §3.3) | FSRS spaced retrieval in the design (`brainlifts/amalgamation-v2.md`); no dedicated review unit live |
| Dated in-repo read-back pull | `timeback-pull/` **2026-07-06**, GET-only, recompute commands in its README | `timeback-pull/` 2026-07-05 (`brainlifts/v0.3.md` §11) | `timeback-pull/` 2026-06-18, re-confirmed 2026-07-01 (`approval-package/00-INDEX.md`) |
| Measured incumbent census | `../analysis/incumbent-pull-2026-07-06/` (capture 2026-07-06) | Two live G4 incumbents pulled 2026-06-30 — Core Knowledge `027e4ce3`: 757 items, 757 MCQ, 0 mastery gates (`brainlifts/v0.3.md` §11) | Incumbent pulled and measured — five breakage figures (`course-jsons/carl-incumbent.json`; `approval-package/approval-email.md`) |
| Item-format breadth | 6 native formats live (match 198, hot-text 160, sequence 167, MCQ 116, MSQ 111, EBSR 20) | **8 types** — 6 MAP + SCR 47 + inline-choice 48 (`brainlifts/v0.3.md` §3.2) | 6 formats present; choice-type 690/745 = 93% of the bank (`approval-package/response-to-review.md` §4) |
| Standards stamping | **CASE-GUID resolved, 772/772** — official CCSSO GUIDs, same family G4 stamped (Insight 3) | **CASE-GUID restamp complete, 1,005/1,005** (`brainlifts/v0.3.md` §15) | 745/745 aligned, 29 standards, CASE-sourced on the bulk (`approval-package/00-INDEX.md`) |
| Parallel mastery forms | **5 forms A–E × 24 items, disjoint from each other (form-to-form), certified-only, live** (Insight 2) | **5 forms A–E × 24 items** (`brainlifts/v0.3.md` §3.3) | 1 mastery test, 24 items (`approval-package/response-to-review.md` §4) |
| DOK distribution reporting | Unit-2 bank measured: 84% DOK-2 / 16% DOK-3 / 0% DOK-1 vs a ~20/55/25 target (SPOV3) | **Full-bank DOK tagging reported**, incl. the incumbent's — own 947/35/6, incumbent 373/252/132 (`brainlifts/v0.3.md` SPOV3) | Not reported |

Reading the ledger: G4 leads on item-type count and DOK reporting depth. G5 leads on the
measurement layer — the anti-leak instrument is run and enforced under a uniform gate (G4's
equivalent audit is unrun; G3's is a live gate-hardening result plus a QA-layer precedent),
feedback coverage is complete at the item level, the spaced-review and parallel-form instruments
are live rather than drafted, and the read-back pull and incumbent capture are the freshest of the
three.

## Locked decisions

| Decision | Ruling | Why |
|---|---|---|
| #1 problem | Curriculum first, then assessment | EGM=0 at G5: students take mastery tests and never pass; the knowledge/instruction layer is the binding constraint |
| Pedagogy | Knowledge-first; KC/schema atoms only; no "reading-strategy" atoms | Comprehension at G5 is a by-product of domain knowledge + vocabulary, not a free-standing skill |
| Teaching layer | Locked for the **core-teaching course** of the two-course split; out of scope for this MAPS-practice course | The v0.1 gradual-release amendment survives, re-scoped (CoE 2026-06-30 split); this course is assessment-only by design and says so |
| Modality | No video; audio = pronunciation/gloss that fades, never a read-aloud crutch | Transfer target (MAP) is cold plain text; audio scaffolds would let a weak decoder fake comprehension |
| Target construct | Design toward MAP; measured MAP results begin with the crosswalk + pilot | No proxy→MAP bridge buildable until the crosswalk lands |
| Assessment | MAP-styled mastery on unseen passages, near-neighbour distractors, parallel forms | Internal pass must mean transferable comprehension, not recognition or elimination |
| Timing | Comprehension untimed; G5 demand is stamina, not speed | MAP is an untimed power test; time-pressure triples the accuracy penalty and rewards rapid-guessing |
| Primary lever | Curriculum effectiveness first; assessment adopted-and-tightened, not rebuilt | The failure to move EGM off zero is a curriculum gap, not an over-hard test |
| Mastery gate | Staged ≥90% gates with an on-ramp; gate instrument built only from certified items | `masteryThreshold==90` on 81/81 live; a gate on unconverted MCQ/MSQ would be ≈90%-blind-solvable |
| Certified base | Per-item certification, never format-family membership alone; excluded items stay out of gates | The ~78% live baseline on uncertified anti-leak-format items proved family ≠ certification; 549 items hold the bar (358 cross-family + 188 choice + 3 EBSR same-family lane) |
| Anti-leak gate | Cross-family blind-solve required pre-deployment; load-bearing only when co-signed (Abdul + Becky/Anuj); recoveries excluded | It is the missing measurement layer for NN#7; it precedes content review, not replaces it |
| Outcome claims | RIT/growth measurement begins with the in-cohort MAP pilot | No linked MAP data exists pre-crosswalk (SPOV7) |

## Open forks

These are genuine judgment calls for the group, not approval conditions.

- **Q1 — Knowledge breadth vs depth at G5.** How much new domain breadth vs deeper inference on
 fewer domains? *Confidence: low; needs a G5 curriculum review + EGM diagnostics.*
- **Q2 — Literary/informational balance.** Merged course (Unit-2) sits 306 Informational / 294
 Literary (51/49); the working MAP composition target near ~40/40/20
 (literary/informational/vocabulary) is an **assumption with an open source ask** — no NWEA primary
 source for it is in this repo — and the vocabulary domain is not yet tracked. *Confidence: medium
 on the imbalance mattering; the target itself is unsourced.*
- **Q3 — Passage length / stamina target.** Confirm the G5 stamina target (and the ~830–1010L band,
 itself an assumption with an open source ask, per Defining Feature of Mastery) without drifting
 into a speed construct; the passage-length census of the live pull is a named Phase-1 measurement.
 *Confidence: medium.*
- **Q4 — The excluded choice/EBSR pool.** The choice lane converted 142/234 (a 20/27 pilot + a
 122/207 scale pass at a 2-of-2 blind-vote bar); 52 choice + 12 EBSR remain excluded by
 id-label. Convert further, or retire-and-replace with certified TEI designs? *Pending
 owner go; the lane is proven viable at scale. Confidence: high.*
- **Q5 — The excluded sequence/match items (53 by id-label).** 5–6 rounds each, mostly
 irreducibly causal content. Replace with new certified items, or hold for a future replacement
 pass? *Replacement candidates, not rewrite targets. Confidence: high in the diagnosis.*
- **Q6 — The excluded redesign remainders.** The hot-text lane shipped (Insight 5); 31 hot-text
 remain excluded by id-label, the June-era Unit-1 designs among them. Redesign further,
 or replace? *An owner decision riding a proven lane. Confidence: high.*
- **Q7 — NN#6 bank depth.** The 8-lesson review unit and the five parallel mastery forms are live,
 certified-only; bank-depth fill to the ≥15 bar rides behind them. *Deploy decisions resolved;
 depth fill remains. Confidence: high.*
- **Q8 — MAP validation gating.** Proxy-only vs administer NWEA MAP at pilot. *Stays open — an
 org/access call, not a design one; SPOV7 holds either way. Confidence: high.*

## Scope

The pitch leads on the structural finding (blind-solve leak by format and item design) and the
curriculum gap (EGM=0); RIT is the post-pilot target, unlocked by the MAP crosswalk + linking pilot
(SPOV7, NN#1). Open items, named explicitly: the 223 excluded items (sub-dispositions in Insight 1 —
kept out of gate instruments), the accessibility renderer review (NN#10 — in progress with the
platform team), bank-depth fill (meets the ≥15 bank-depth bar, behind the live
NN#6 instruments), and Caliper assessment-event
evidence (activity events observed 2026-07-06; assessment events open).

An ELA content review of the certified core is scheduled separately (Case §5, OPEN_ACTIONS §A). The certified base is **exactly the 549
ledger-listed items** (103 Unit-1 + 446 Unit-2) — certification is per-item (358 cross-family + 188 choice + 3 EBSR same-family lane),
never format-family membership. **No in-course MAP-equivalent test is planned (decision 2026-06-29).**
The course defers to the platform's **adaptive Grade 2-5 MAP** — live id `incept-map-g2g5-l1`,
engine <https://github.com/trilogy-group/Incept-MAP-proxy> — as the measurement of record. The
gate→grader-pass→RIT growth chain runs observe-only until G5 MAP data exists to check it against.

## Dropped approaches

| Approach | Reason |
|---|---|
| Instructional video | Hard constraint — excluded; the transfer target is cold plain text and the design is knowledge-first, no-video |
| Audio as a read-aloud crutch | Transfer target is cold plain text; audio as a comprehension crutch lets a weak decoder fake comprehension and undermines the construct |
| Skills-first course spine | Violates the knowledge-first stance (SPOV2); comprehension at G5 is a by-product of knowledge, not a free-standing skill |
| All-MCQ assessment | MCQ as conventionally authored is 99.5% blind-solvable on these passages; an all-MCQ course measures prior knowledge, not reading (fails NN#7, Dim 3, Tier-0 retrieval at once) |
| MCQ as a coverage type without per-item conversion + re-gate | Adding MCQ "for coverage" without passage-dependent redesign and a cross-family re-gate reintroduces the 99.5% leak; the choice lane defines the working path |
| Treating anti-leak *format family* as certification | Our own earlier framing, corrected against the 2026-07-02 live baseline: uncertified sequence/match/hot-text items leaked ~78% weighted — certification is per-item or it is nothing |
| Forcing native hot-text through the blind gate | Proven futile (tokens ≈ passage; rewording does not fix a construct incompatibility); the shipped path is the claims-about-passage construct redesign |
| Retaining items that recover on re-probe | Recovering items move to the excluded bucket (Insight 1) |
| Difficulty escalation after failure | Measurably destroys attempt-2 accuracy on the incumbent retry path; reteach-first instead |
| Pre-pilot RIT projections | No linked data and no literature precedent (SPOV4/SPOV7); RIT enters after the pilot |
| Same-family structural-gate "passed" as anti-leak evidence | A model grading its own family's output is not isolation; only a cross-family blind-solve counts |
| Coding the 42 live-swapped CCSS slots from the stale snapshot | Would be fabrication — the live passage was swapped, so the snapshot code no longer describes the tested item |

## Experts

The external authorities the design's pedagogical stance inherits from. Provenance only — not
compliance.

- **E. D. Hirsch Jr., Daniel T. Willingham, Donna R. Recht & Lauren Leslie** — the knowledge-first
 foundation: reading comprehension is a by-product of domain knowledge and vocabulary, not a
 free-standing skill (Hirsch, *The Knowledge Deficit*; Willingham, *Why Don't Students Like School?*;
 Recht & Leslie 1988 baseball-passage study). The reason this course is knowledge-curriculum, not
 skills-curriculum.
- **Carl Hendrick** — the KCT taxonomy (KCT1–KCT5) and the Alpha Read instructional architecture. We
 adopt the taxonomy (it types every node in `../kc-graph/kc-graph.json`) and EDI structure; we
 deviate on video (no video).
- **Becky Allen** — *Bespoke Mastery Assessments* (the ≥90%-pass, parallel-forms, unseen-passage
 mastery blueprint), the course-BrainLift template this document conforms to, and "predict, don't
 simulate" (SPOV4).
- **Andy Montgomery** — *Winter MAP 2026 Session 3 Recap*: the intervention-bucket framework, the
 EGM>0 correlation, and MAP as the metric of record (the source of the curriculum-is-the-binding-
 constraint position and the no-claim-without-pilot discipline).

## What changed — v0.1 → v0.6

One line per kept version (`brainlifts/` retains v0.1, v0.3, v0.5, v0.6; v0.2 and v0.4 were
interim edits superseded in place).

| Version | Date | What changed |
|---|---|---|
| v0.1 | 2026-06-18 | G3 design ported to Grade 5; cohort-specific figures marked to-source, none carried from G3 |
| v0.3 | 2026-06-24 | The leak-by-format finding becomes the spine (MCQ 99.5% / MSQ 100% vs hot-text 1.67% / sequence 0% / match 0%); skeleton rebuilt on the formats that hold |
| v0.5 | 2026-06-29 | Re-anchored to the merged live course (172-item certified Unit-1, render-truth ledger); SPOV9 added; in-course MAP-equivalent test retired in favour of the platform's adaptive Grade 2-5 MAP |
| v0.6 | 2026-07-06 | Certified base 624/772 under the uniform same-day gate; conversion lanes shipped (choice 142/234, hot-text 90/117); five parallel mastery forms + review unit live, certified-only; standards on CASE GUIDs 772/772; feedback 772/772; ledger unknown bucket emptied; MAP-G5 Format and Scoring Logic section added |
| v0.6.1 | 2026-07-07 | Anti-leak gate finalized on the cross-family mean-blind-solve metric (< 0.60 over resampled shuffles); certified base 549/772, ledger 549/223/0 (358 cross-family + 191 same-family lane); all 81 gating tests serve 15 certified items |

---

*v0.6.1 — 2026-07-07. Factual refresh over v0.5; the design argument is unchanged. (1) The anti-leak
gate is per-item — every certified item probed on its own id (358 hot-text/sequence/match
cross-family + 188 choice + 3 EBSR same-family lane), 2026-07-06/07;
certified 549/772, ledger 549/223/0 with the unknown bucket emptied
(Insight 1). (2) Conversion lanes shipped: choice 142/234, hot-text 90/117 (claims-about-passage).
(3) Corrective feedback CLOSED 772/772. (4) NN#10 accessibility line added. (5) MAP framing corrected (SPOV7/DOK1), with the adaptive-MAP engine cross-referenced.
(6) Standards resolved to official CASE GUIDs on 772/772. (7) Lexile band + ~40/40/20 composition
target re-labelled as explicit assumptions with open source asks. (8) NEW: MAP-G5 Format and
Scoring Logic (the operational endpoint). (9) NN#6 spaced-review unit + five parallel mastery
forms live, certified-only; NN#8 activity-event evidence observed. (10) Positioned absences + the
v0.1 teaching-layer amendment reconciled (re-scoped to the core-teaching course). (11) Added:
cross-grade parity ledger, as-built feature status, version-change table, effect-size context
(DOK2 Summary 6). Supersedes v0.5. Companion build record:
`../SUMMARY_AGENT.qmd`; acceptance bar: `../llm/ACCEPTANCE_BAR.md`; generator front door:
`../llm/g5-gen-entry-v1.md`; companion decision memo: the Case for Approval for
`g5-reading-merged-pp-9802`.*
