---
name: grade3-reading-brainlift
description: The substantive, self-contained knowledge base a REVIEWER AGENT loads to understand and evaluate the live Grade-3 course "Reading Explorers v2" (reading-explorers-v2) with full context — carrying the invariant ground-truth data (cohort metrics, incumbent breakages, MAP construct facts, live course counts), the BrainLift's load-bearing positions (7 Spiky POVs / 7 Insights / evidence tree / experts / locked decisions), the reviewer's 11 findings with the item-by-item response and live-verified result, and the DOK-4 cross-source syntheses (the non-obvious conclusions that require triangulating the BrainLift + reviewer feedback + response together). Use when a reviewer agent must review/evaluate reading-explorers-v2, decide whether to approve it for pilot, judge it against the reading-science bar, or reason about any design choice on its merits. This is the DECISION knowledge base; it carries the substance, and links each section to the source doc for more. Companion skills: reading-course-review (audit the live course), grade3-proposal-review (compare proposals).
---

# Reading Explorers v2 (Grade 3) — Reviewer Knowledge Base

You are a **reviewer agent** deciding whether the live Grade-3 course `reading-explorers-v2` should be approved for a classroom pilot. This document carries the substance you need to judge it — the ground-truth data, the design's load-bearing positions and evidence, the reviewer's findings and how they were answered, and the higher-order syntheses that only emerge when you read the three source documents *together*. Each section ends with a link to the source for more depth; the substance is here, the link is the citation.

## 0. How to use this + prime directive

**Read order:** the invariant data (§2) and the defining feature of mastery (§1) are your fixed reference points. §3–4 are *why* the course is built this way. §5 is the reviewer's spine (finding → response → live state). §6 is the heart — nine DOK-4 cross-source conclusions, **S1 first** (it fixes the scope: the team concedes "practice engine, not curriculum" and asks to pair-with-instruction, so read nothing below as a curriculum claim). §7–8 are pedigree/provenance, settled decisions, dropped approaches, and honesty limits.

**Prime directive.** Judge the *build against its stated design* and the *design against the evidence* — not against a different course you would have built. Distinguish a **deliberate, citable position** from an **oversight**. Reward honesty about what isn't yet proven; penalize overclaiming.

**Tag every claim** with its epistemic status:
- **Verified** — recomputed from the live course / a direct measurement.
- **Asserted** — stated in a design/deck but only checkable in delivery (e.g. PowerPath feedback quality, gate runtime behavior). Never silently promote to Verified.
- **Open** — needs data that does not yet exist (any MAP RIT/growth figure — requires a pilot cohort). Never invent a magnitude.

**The one question to resolve.** The reviewer's verdict on the predecessor was: *"a well-built, MAP-styled practice-and-assessment engine, not a comprehension curriculum; should not be approved as one."* The load-bearing question for your review is therefore: **has v2 become a comprehension curriculum, or is it still a practice engine?** §5 and §6 give you the evidence to decide, honestly.

---

## 1. Defining feature of mastery (what "done" means)

A mastered Grade-3 reader **comprehends an unseen, on-topic passage at the end-of-Grade-3 Lexile band (~520–820L, the CCSS stretch band)** by deploying the four text-structure schemas — cause/effect, compare/contrast, sequence, problem/solution — and **bounded inference automatically**, on cold, topic-switching, MAP-format items, **without rushing**.

Concretely, given an unfamiliar passage on a taught topic, the mastered student can: identify the active text structure unaided; answer literal + vocabulary + inferential MCQ + multi-select + hot-text + drag-to-order + match + 2-part EBSR items at **≥90% accuracy on near-neighbor distractors**; write a one-or-two-sentence response naming the structure with a cited line; and sustain attention across an untimed multi-passage block (the MAP transfer target is **stamina + not-rushing, not speed**).

**Key stance:** mastery does *not* require strategy verbalization — it requires the underlying **knowledge and schemas to be automatic**. Every atom is either a knowledge component (a piece of automatic knowledge) or a schema (a structural template); "reading-strategy" atoms are explicitly *not* modelled.

**G3 pivot caveat:** Grade 3 sits at the *learning-to-read → reading-to-learn* transition. Below-floor decoders (entry Lexile ≪ 400L — the highest RIT-headroom segment) get an in-course **Foundations** strand (non-ASR by default: silent maze + WCPM self-check; ASR oral-reading only as a confirming enhancement, never a blocker). Fluent readers skip the on-ramp, never the knowledge core.

*Source: [BrainLift](https://docs.google.com/document/d/1qP5JSriZBosWWvuFKl0cyX9eLjNEKvUZbPXnIzE-wfg/edit?tab=t.3ux9kqm3q4x6) → open the **"BrainLift"** tab, heading **"Defining Feature of Mastery."***

---

## 2. The invariant data (ground truth — these numbers are the bedrock)

### 2a. The incumbent (AlphaRead) is broken in five measurable ways
| # | Breakage | Measured value |
|---|---|---|
| 1 | No completion mechanism | **~30%** of intended work done; **median completion 12.5%**; **~0 net acceleration (+0.026 grades-ahead)** |
| 2 | Under-samples the construct | Text-structure items are **~4%** of the item bank |
| 3 | One item format | **100% single-select MCQ** — covers 1 of MAP's 6 formats |
| 4 | Retry makes students worse | Difficulty escalates after a miss; attempt-2 supporting-details accuracy drops **64% → 41%** (a 23 pp drop caused by the retry path, not the student) |
| 5 | Passages too hard | **Flesch-Kincaid 6.5** on a Grade-3 instrument (~2 grades hot) |

### 2b. The four weakest skills (text structure) — measured on students who *did* complete items
- Compare/contrast **39%** · Cause/effect **42%** · Sequence **48%** — vs **83% blended** daily accuracy.
- Only **~17%** of the cohort clears **90%** on any equivalent mastery instrument.
- Interpretation: the completion floor (12.5%) is further from acceptable than the 39% skill is — **fix the floor first**.

### 2c. The MAP transfer construct (all directly verified facts)
- MAP Reading is an **untimed power test** — no per-item limit, no overall limit. Time pressure ~triples the on-screen accuracy penalty and rewards rapid-guessing, which MAP penalizes.
- **6 item formats**, all auto-scored, **no FRQ/constructed-response**: MCQ, multi-select, hot-text, drag-to-order, match, 2-part EBSR.
- Domain mix ≈ **40/40/20 Literary/Informational/Vocabulary**.
- Grade-3 end-of-year Lexile band ≈ **520–820L** (CCSS "stretch" band); the course targets a personal Lexile staircase **~400 → 820L** (Band A opens ~400–460L). *Source note: the BrainLift tab says 520–820L; the older "Case for Approval" tab still says ~480–600L — 520–820L is the corrected CCSS stretch band and the one to trust.*
- **MAP is not in TimeBack: 0 of 66 STAAR students have a MAP sitting; 0 of 313 MAP students have STAAR** (measured by sourcedId join). No proxy→MAP bridge is buildable from existing data. Internal ≈ STAAR (gap ~1.9).

### 2d. The live v2 course (authoritative fresh pull, 1 Jul 2026 — QTI + OneRoster)
- **13 units · 62 lessons · 62 tests · 512 items · 66 passages · 47 teaching doses · 47 writing prompts.** (512 = distinct wired items; 513 refs, 1 dangling. An earlier deck pull showed ~503/~43.7% MCQ; the ~9-item drift is dedup timing — **512 is authoritative**.)
- **Lesson mix (62):** 40 reading-expedition · 5 lens-practice · 4 lens-intro · 2 onboarding · 2 drama · 2 poem · 3 stamina-long · 3 stamina-paired · 1 mastery.
- **New-course passage difficulty: Flesch-Kincaid median 6.2** — at grade, vs the incumbent's **FK 6.5** (~2 grades hot). The single cleanest before/after on text difficulty. 66 passages (47 distinct canonical + cold set).
- **Full item-format breadth (559 questions = 512 QTI + 47 app-delivered writing):**

| Format | Count | % of all questions |
|---|---|---|
| MCQ (single-select) | 229 | **41.0%** (44.7% of the 512-item QTI bank) |
| MSQ (multi-select) | 62 | 11.1% |
| EBSR (2-part evidence) | 56 | 10.0% |
| Hot-text | 49 | 8.8% |
| Order / sequence | 47 | 8.4% |
| Written constructed-response | 47 | 8.4% |
| Match | 44 | 7.9% |
| Inline-choice (STAAR) | 25 | 4.5% |

  Roll-ups: **selected-response (MCQ+MSQ+EBSR) 61.5%** · richer technology-enhanced (hot-text/order/match/inline-choice) ≈ 30% · constructed-response 8.4%. **7 interaction formats** live. MCQ trajectory: **~87% (predecessor) → ~68% mid-cycle → 41% now** (via #8b inline-choice conversion + dedup). Well under STAAR's **75%-of-points** single-select cap. *STAAR **text-entry** type is still absent (inline-choice present).*
- **~94% of items CASE-tagged** (472/503 on the deck pull; 481/512 tagged on the fresh pull → ~94%); **100% of items stimulus-linked** (every scored item points at a passage).
- **193 items retagged** to correct CCSS this cycle (vocab-in-context → RI.3.4/RL.3.4; comprehension items wrongly on L.3.4 fixed), CASE bindings updated with **0 errors**.
- **47 written constructed-response** prompts (one per dosed lesson; STAAR **2-pt rubric** = accurate answer × cited evidence; server-scored; formative/out-of-gradebook). Corrective per-choice feedback on **337/512** items (~67%) — choice-family (MCQ/MSQ/EBSR) 292/348, order 45/47.
- **App-side compliance shipped to main (engineering/validator-confirmed):** real **Caliper** learning-event envelopes emitted server-side (confirmed against the live validator); **XP 80% floor** applied by the TimeBack pipeline (broker records raw correctness). These are *Verified shipped*, not asserted.
- Retired predecessor counts: the deck's **52 tests / 745 items / 56 passages** (and the **47/713** variant) are `reading-explorers-g3-allqtypes` (18-Jun pull), **not v2**. Arithmetic check: 745 − 24 mastery − 8 lens-intro = 713 exactly.

### 2e. The honest effect-size ceiling
- Whole-intervention literature moves standardized scores **g ≈ 0.1–0.2**; even 1:1 tutoring is **g ≈ 0.21 ≈ +3.6 RIT ≈ cohort CGP ~65** (and the SD→RIT step is itself an estimate on an assumed G3 RIT SD).
- **A "2× growth / CGP 80" headline has no precedent** in the curriculum-intervention literature. Treat any RIT number as the post-pilot target, never a present fact.

*Sources: [BrainLift](https://docs.google.com/document/d/1qP5JSriZBosWWvuFKl0cyX9eLjNEKvUZbPXnIzE-wfg/edit?tab=t.3ux9kqm3q4x6) → **"BrainLift"** tab, headings **"DOK2 — Knowledge Tree Summaries"** and **"DOK1 — Facts and Sources"** (the Andy Montgomery Session-3 figures are under DOK1/Experts). Live pull via `qti.alpha-1edtech.ai` + `api.alpha-1edtech.ai`; cohort figures via the TimeBack Reporting MCP.*

---

## 3. The 7 Spiky POVs — the load-bearing positions (DOK-4 within the BrainLift)

Every design choice derives from these. Each is paired with the invariant number it rests on.

1. **Dosage is the #1 problem, not skill.** Binding constraint is *volume* (12.5% median completion, ~0 acceleration), not aptitude — the cohort never reaches the content. Lead with a completion engine; accuracy is the second lever. *(Confidence: the 12.5% floor is further from acceptable than the 39% skill.)*
2. **Knowledge-first; no video; audio fades.** Comprehension is a by-product of knowledge (Hirsch/Willingham/Recht-Leslie/Hendrick). Extends Hendrick one notch: **no video at all**; audio = pronunciation/gloss that fades and never lets a non-decoder fake comprehension. *(Confidence: MAP shows cold plain text; exit lessons show cold plain text — exact construct alignment.)*
3. **Beat the incumbent on its five measured breakages, not rhetoric.** (The five in §2a.) Every competitive claim traces to a number, not "the test is a lie." Do *not* claim "false mastery" beyond the STAAR proxy (internal ≈ STAAR, gap 1.9) — that's an unmeasured risk.
4. **Predict direction, not magnitude.** High confidence on *direction* (completion lift, the 39–48% skills, the 90% bar, retry-stops-degrading, acceleration turning positive); **no RIT number pre-pilot** (§2e). Discipline, not a hedge.
5. **Comprehension is untimed; speed is a different construct.** MAP is untimed (verified). Timing kept only where speed *is* the construct (Foundations fluency: WCPM/maze). Time-on-task captured silently everywhere (rapid-guess detection) — but no clock on a reading passage.
6. **Three difficulty bands; staged 90% gates, not a flat wall.** Band A advisory (no hard wall on the on-ramp); blocking ≥90% gates begin in Band B; final 90% gate is the course-end mastery test. *(Confidence: only ~17% clear 90% today — a flat wall has no on-ramp for the other 83%.)*
7. **One in-cohort MAP pilot, or no MAP claim at all.** MAP not in TimeBack (0/66, 0/313). The only honest path to a RIT figure is to run the pilot and report cohort CGP from day one.

*Source: [BrainLift](https://docs.google.com/document/d/1qP5JSriZBosWWvuFKl0cyX9eLjNEKvUZbPXnIzE-wfg/edit?tab=t.3ux9kqm3q4x6) → open the **"BrainLift"** tab, heading **"DOK4 — Spiky Points of View."***

---

## 4. The 7 operational Insights (DOK-3 — settled, derived positions)

1. **Four engines, in priority order.** (1) *Completion/dosage* — daily doses sized so finishing = the 25-min/25-XP goal; "done" counts only when the check is attempted; no pay-for-volume, no leaderboards. (2) *Transfer* — teach MAP's exact skill+format profile, near-neighbor distractors from item one. (3) *Engagement→rigor fade* — a "home-run" opener + recurring cast that fades across 9 dimensions to cold plain text. (4) *Mastery+measurement* — staged ≥90% gates on unseen passages, spaced retrieval, no-escalation reteach-first, a personal Lexile staircase climbing toward the end-of-G3 band (~400 → 820L).
2. **Topic-coherence is itself the 9th faded scaffold.** MAP interleaves unrelated passages; cold context-switching *is* the construct. So "you always know the topic" fades gradually: full coherence in Band A → mixing phases in across late Band B → full mixed cold gauntlet in Band C. (v2-original insight — block-for-acquisition, interleave-for-transfer.)
3. **Schema mastery is enforced inside expeditions, not the Schema Toolkit.** The four schemas are introduced soft (no wall, can't fail out); each reaches its enforced ≥90% checkpoint later, inside the expedition, before the first passage that depends on it. So cause/effect (the 42% skill) is exercised early without a wall, gated once load rises.
4. **Retry resolves to three states, not pass/fail.** ✓ *Mastered* (≥90% on unseen + holds on spaced re-check → certify) · ◐ *Developing* (cleared a real lower threshold → keep moving, stays on spaced queue, visible/tracked, *not* a silent step-down) · ✗ *Not-yet* (diagnose → re-teach in a different modality → retry on a *parallel same-difficulty* passage → escalate after 2 cycles). **Never re-serve the identical item; never hand a harder item after failure** (directly counters the incumbent's 64%→41%).
5. **Two separate instruments: gate vs growth.** Gating = the 12-item adaptive mock (≥85% within 14 days) + cold-readiness check + 24-item final. Growth proxy = a *separate* ~40-item held-out instrument (40/40/20, never taught to or gated on, so a rise isn't format-practice inflation). The only fully honest growth read is external MAP at pilot.
6. **The item factory is staged honestly, not "ready."** Real pipeline (anti-leak 2-stage generation → grounded-grader best-of-N → flip-band "stably-pass" certification → provenance + recert), but difficulty calibration (p_m ≥ 0.90) is a *target measured*, not a property shipped — needs student-outcome data that doesn't exist yet; week-1 deliverables are forms + leak-control + provenance only. Four **Stan-v3 locked corrections** a reviewer should note: (i) a **mandatory** age-appropriateness/sensitive-content screen on every auto-generated passage (baked into the acceptance rubric — it's a product for 8-year-olds); (ii) fix the generator's grade setting (**was calibrating at grade 11, not grade 3**); (iii) certification certifies item *quality*, not learning; (iv) for reading, "anti-leak" is a **build-time lint** (answer not in the stem, honest distractors), **not** a comprehension guarantee — because *finding the answer in the passage is the reading skill*. Fallback = hand-authoring **480+** near-neighbor items (a real schedule cost, not a free safety net).
7. **Word Assist boundary: practice on, scored off.** Click-any-word audio definition available in dose steps 1–4 (hook/teach/guided/read), **OFF** in steps 5–6 (scored check/CFU) in every band — so strugglers keep support while learning, and every scored item is a clean cold measure.

*Source: [BrainLift](https://docs.google.com/document/d/1qP5JSriZBosWWvuFKl0cyX9eLjNEKvUZbPXnIzE-wfg/edit?tab=t.3ux9kqm3q4x6) → open the **"BrainLift"** tab, heading **"DOK3 — Insights."***

---

## 5. The reviewer's 11 findings → response → live state (the spine)

This carries the reviewer feedback and the response together. Call = the response's stance; Live = what a fresh pull shows.

| # | What the evidence base requires | What the reviewer found (in the predecessor) | Call | Live-verified result in v2 |
|---|---|---|---|---|
| 1 | Explicit strategy instruction via gradual release + corrective feedback (IES/WWC) | No teaching step; binary "good try, look again" | **Accept** | 6-step gradual-release dose (hook→teach→I-do→we-do→you-do→read→CFU→wrap) on **47 dosed lessons**; per-choice corrective feedback ~337/512 (**Asserted** for delivery quality) |
| 2 | Teach text structure with worked examples, not just labels | "Learn the Lens" gave a thin description + an application question; no modelling | **Accept** | Dedicated **"Four Lenses" strand (9 lessons)**, each modelled with an I-do worked example before items |
| 3 | Build knowledge that recurs and compounds | *"The deepest issue"* — sequenced as a Lexile staircase; cold non-overlap *everywhere* → "cites Hirsch then forbids knowledge from helping" | **Partial** | 10 multi-lesson topical domains + cross-domain knowledge threads woven in; compounding **improved but still partial** (honest) |
| 4 | Texts chosen for genre/quality, not Lexile alone | Lexile-driven; ~0 poetry/drama; short of its own 40/40/20 | **Partial** | Poetry + drama strand added; literary now **~22%** of tagged bank (was near-zero) — still below ~40% (see §6) |
| 5 | Make the child explain thinking + require attention | Every interaction silent/auto-scored; nothing requires reading before answering | **Accept** | CFU "prove it" hot-text + a **forced read-before-answer gate** + 47 written responses |
| 6 | *(the reviewer had no #6-numbered gap in the same sense — items renumber; see stamina)* | Stamina: passages 58–217w (avg ~166); can master one snippet at a time | **Partial** | Longer + paired-text stamina sets added; still short of STAAR's ~2,740w multi-passage reality |
| 7 | Write about reading (short constructed response) | *"No writing at all; every response is a click."* | **Accept** | **47 written constructed-response** prompts keyed to lesson vocabulary, STAAR 2-pt rubric, formative |
| 8 | Format breadth under the STAAR 75% MCQ cap; add STAAR types; fix mistags | All 6 MAP formats present (genuine strength) but **~87% single-select MCQ**; STAAR inline-choice/text-entry missing; ≥1 mistag ("a vocab item labelled Inference & Evidence") | **Partial — counter the number** | Single-select MCQ **41% of questions / 44.7% of bank**; **7 formats** incl. STAAR inline-choice; **~94%** CASE-tagged; **193 retagged**. *Counter:* the cited example is defensible (vocab items carry L.3.4+RI.3.4, both word-meaning); but a full audit found a **genuine systematic mistag** elsewhere and fixed it. *text-entry still absent* |
| 9 | Mastery must require reading (product integrity) | **Earned a stamp on "The Amazing Axolotl" at ~20% accuracy by clicking through** without reading, then advanced with the passage hidden | **Accept — critical, no counter** | Course-wide answerability audit (~700 pre-dedup items, ~half gameable, 5 root-cause patterns) → **dual-gate** re-generation (InceptBench ≥0.85 **AND** unanswerable-without-passage) → dedup to **512 items, 100% passage-linked**; cold mastery test; read-gate + writing/CFU completion-gate (see §6 for scope) |
| 10 | WCAG 2.1 AA / Section 508 accessibility | Drag/match not keyboard/AT operable; a **12-option** hot-text (excessive load for an 8-yr-old) | **Accept — criteria gap** | Keyboard/AT operability shipped for hot-text/choice/inline-choice/drag/match + focus rings + drag announcements (**Asserted** pending an a11y audit). *Remaining authoring change: hot-text option cap 6/≤3* |
| 11 | Reconcile the claims and the counts | Email said 52/745/56; infographic said 47/713; "45 instructional tests" are tests, not instruction | **Partial — reconciled** | One authoritative live pull (§2d); predecessor 52/745/56 retired; "45 instructional tests" = PowerPath tests not instruction (wording fix); 745−24−8=713 explains the deck variant |

**Reviewer's own framing to preserve:** "If it is decided this should be a MAP practice app, the recommendations would be different." And it credited the format breadth + well-built EBSRs as *"a genuine strength."* The response owns #9 as a real product-integrity failure; corrects overstated numbers; and defends the deliberate design choices as choices.

*Sources: [Reviewer feedback](https://docs.google.com/document/d/1mK96r9bk35NzK4X1PWHRd7Gt5zi_ao2B/edit) (the 11 numbered items under "What a comprehension course must do" + "What the tests require" + "Product integrity") · [Response-to-Reviewer](https://docs.google.com/document/d/1LXNc5-ezBycWZwdUaRPNeDJr-Iq21yAMvKDKt44ukaE/edit) (the item-by-item Accept/Partial/Counter section). Live results verifiable via the API pull in §2d.*

---

## 6. DOK-4 cross-source syntheses (the heart — conclusions that need all three docs)

Each of these nine syntheses can only be reached by triangulating the three docs — **BrainLift (intent)** = [Case-for-Approval doc, "BrainLift" tab](https://docs.google.com/document/d/1qP5JSriZBosWWvuFKl0cyX9eLjNEKvUZbPXnIzE-wfg/edit?tab=t.3ux9kqm3q4x6) · **reviewer feedback (what the build did)** = [feedback doc](https://docs.google.com/document/d/1mK96r9bk35NzK4X1PWHRd7Gt5zi_ao2B/edit) · **response (what changed)** = [response doc](https://docs.google.com/document/d/1LXNc5-ezBycWZwdUaRPNeDJr-Iq21yAMvKDKt44ukaE/edit). Each cites which section of each it draws from, plus status. **S1 is the master inference — read it first, and do not read the rest as claiming curriculum status.**

**S1 — The curriculum-vs-practice seam (the master inference — read this one carefully).**
The BrainLift *intends* a knowledge-first comprehension curriculum (SPOV2, four engines). The reviewer *found* a practice-and-assessment engine — because the build shipped the assessment layer (Engine 2/4) far ahead of the instruction+knowledge layer (Engine 1's teaching, and knowledge compounding). The response made the **teaching layer real** (item 1: 47 six-step doses — Verified) which retires the literal "no teaching step" charge, and it added corrective feedback, writing, threads, stamina, and gaming/a11y fixes.
**But the response does *not* claim v2 has become a comprehension curriculum.** It states in its own words that **"the reviewer is mostly right,"** frames the whole disagreement as a **scoping decision the team never made explicit** (comprehension curriculum vs MAP-practice engine — and notes the BrainLift is *internally split* on which it is), and its actual recommendation is to **approve v2 for what it excels at — a MAP-styled practice/format-familiarisation + cold-reading engine — and *pair it* with the instruction layer**, not to relabel it a curriculum. *Conclusion for the reviewer: the honest verdict is "the teaching layer is now real and live; the knowledge-compounding sequence is still partial; and the team concedes the top-line 'practice engine, not curriculum' characterization rather than refuting it — it argues for an explicit scope, not against the verdict." Do not read S-anything below as a claim of curriculum status.* *(BrainLift Engines + SPOV2 + "internal split" · Feedback verdict (top & bottom) + #1/#3 · Response "strategic frame" + #1/#3 + Net. Status: Verified teaching layer; Partial compounding; verdict largely conceded.)*

**S2 — The knowledge-first paradox (the design contradicted its own thesis).**
This is the sharpest cross-source point and the reviewer's **"deepest issue with the design."** The BrainLift cites Hirsch/Willingham that comprehension *is* knowledge (SPOV2) — yet its own early build made assessment passages cold and non-overlapping *throughout learning* so a student "can't pass on recall." The reviewer named exactly this: **"It cites Hirsch and Willingham and then forbids knowledge from helping,"** with the killer illustration — *"a child can find the main idea fifty times on fifty disconnected passages and never accumulate the knowledge that makes main ideas easy to find."* Crucially, the BrainLift *itself* already contains the fix as **Insight 2** (topic-coherence is a faded scaffold — cold belongs at the *test*, not throughout), so the reviewer and the design actually **agree on the principle** ("reserve cold, non-overlapping passages for the test only"). The response resolved it **not** by a risky whole-course reorder (a readability check showed reorder would jumble the difficulty ramp) but by weaving **three named knowledge-compounding threads** through existing passages, each rung reusing+deepening the prior: (1) *survive→energy→energy-flows* (Mammal→Human Body→Ecology); (2) *sun makes energy→energy travels in waves→energy powers living things* (Space→Light&Sound→Ecology); (3) *adapt-to-survive* (Animals→Hopi dry-farming→Age of Exploration). **6 passages edited** (openers now say "you already know…"), ramp preserved, mastery test kept cold. *Conclusion: principle agreed across docs; defect was build-vs-design drift; fix is real but Partial — threads compound within three arcs, not yet a whole-course knowledge sequence (the reorder was judged too risky).* *(BrainLift SPOV2 + Insight 2 · Feedback #3 · Response #3 threads. Status: principle agreed; fix Partial.)*

**S3 — Anti-gaming is now defense-in-depth, but not absolute (and the scope limit is known).**
The BrainLift asserts "mastery means mastery" / prevent-gaming (and the team's own eval had marked mastery-gating **PASS (encoded)**); the reviewer *falsified it live* (axolotl click-through at ~20%, then advanced with the passage hidden — #9, the one critical integrity failure — and the response **owns it without counter** as "a genuine product-integrity failure," noting a gate that doesn't require reading turns kid-outcome data into noise). The key cross-source realization: **#9 is as much a *content* defect as a *gate* defect** — a course-wide answerability audit (3rd-grader persona, passage withheld, ~700 pre-dedup items) found **~half were gameable** by test logic or world knowledge, with **5 root-cause patterns (biggest: EBSR Part B restating Part A)**. The response built a **defense-in-depth** stack: (1) a durable **dual-gate** — an item ships only if **InceptBench ≥0.85 AND a 3rd-grader can't answer it without the passage** (proven necessary: it rejected a gameable item InceptBench alone scored **1.0**) — regenerating the gameable items (the deck reports **238 re-engineered**) then deduping to **512 items, 100% passage-linked**; (2) a genuinely cold 24-item mastery test (0 topic overlap); (3) a read-before-answer gate (passage shown ~15s before the question, fires on passage change, applies to the CFU "prove it" step) plus soft non-blocking "look at the passage first" / "not so fast — reread" nudges (the latter on answers submitted within **~3s**; presentation-only, never changes a score, off in the mastery test); (4) a writing/CFU completion-gate. *Conclusion: #9 is resolved as layered defense and is live — with two honest caveats a reviewer should know: (a) the **completion-gate covers quiz/onboarding lessons, not the 40 powerpath expeditions** (which mark complete upstream during the questions; those rely on the other three layers), and (b) the axolotl is a deliberately simple Band-A first-win item — "a motivated child could still clear an item or two by guesswork, by design"; the claim is only that **by mid-course, the ramp + cold test mean a student cannot pass on world-knowledge or test-logic.** Judge the ramp + the layered defenses, not a single easy item.* *(BrainLift Engine 1 "honest completion" + Insight 4 · Feedback #9 · Response #9 audit + dual-gate + session gate work. Status: Verified layers; expedition completion-gate scope-limited; early-item gaming residual by design.)*

**S4 — Honesty discipline is the same standard the reviewer is asked to apply.**
The BrainLift's SPOV4 (direction-not-magnitude) and SPOV7 (no MAP claim without a pilot) are *matched* by the response's explicit refusal to claim "proven," a RIT number, or that the reviewer's bar is "cleared" (it says that's the reviewer's call). *Conclusion: the course and the reviewer share one epistemic standard — measured-or-labelled. A reviewer should reward this restraint as evidence of trustworthiness, and read the absence of a RIT number as discipline, not weakness.* *(BrainLift SPOV4/7 + honesty ceiling · Response "what we will/won't claim." Status: consistent; MAP figure Open by design.)*

**S5 — Genre balance is the one substantive remaining content gap.**
The BrainLift targets MAP's ~40/40/20 (so ~40% literary). The reviewer flagged Lexile-only selection with ~0 poetry/drama (#4). The response added a poetry/drama strand and reports **~22% literary** — real movement from near-zero, still below ~40%. *Conclusion: this is a content-authoring roadmap item (more literary/poetry sets), not a pedagogy flaw — the single most defensible remaining critique. Weigh it as an improvement on trajectory, not a blocker.* *(BrainLift locked-decision 40/40/20 · Feedback #4 · Response #4. Status: Partial, improving.)*

**S6 — Format breadth: the incumbent's worst metric became a clean strength.**
Incumbent = **1 of 6** formats (100% MCQ, §2a). The BrainLift committed to teaching all 6 (Summary 3). The reviewer *confirmed* all 6 present and EBSRs well-built ("genuine strength" / "the clearest advantage over the incumbent") while flagging ~87% MCQ and missing STAAR types (#8). The response shows **MCQ 41% of questions (44.7% of the QTI bank) + 7 formats incl. STAAR inline-choice + ~94% CASE** — the trajectory **87% → ~68% → 41%**, under the STAAR 75%-of-points cap. *Conclusion: a nearly-closed before→after where all three sources agree; the course's clearest verifiable win — with one honest remainder: STAAR **text-entry** is still absent (inline-choice is present).* *(BrainLift Summary 3 · Feedback #8 · Response #8. Status: Verified; text-entry Open.)*

**S7 — Dosage is the thesis the reviewer didn't test (a gap in the review, not the course).**
The BrainLift's #1 position (SPOV1: dosage is *the* problem — 12.5% median completion, ~30% work done, +0.026 grades-ahead) is the course's central bet — yet the reviewer's 11 items are almost entirely about *comprehension-instruction quality*, not completion mechanics. *Conclusion: the reviewer evaluated the course as a curriculum (fair to its thesis) but did not probe the completion engine that the BrainLift says matters most; the completion/dosage claim remains **Asserted/Open** — it's the thing the pilot most needs to measure, and it's why "approve the pilot" is the ask (the pilot is what produces both the dosage read and the MAP data).* *(BrainLift SPOV1 + Engine 1 · Feedback scope (no completion item) · Response "the ask." Status: Asserted; pilot-critical.)*

**S8 — Deliberate position vs oversight: the distinction the prime directive turns on.**
This synthesis is the reviewer's actual job, and it needs all three docs to do fairly. The response sorts the 11 findings into **four kinds**, and a reviewer should not collapse them: **(i) genuine product failures owned outright** — #9 gaming and #10 accessibility (the latter a *criteria gap*: the team's own eval never checked a11y); **(ii) the build under-delivering the team's *own* spec** — #6 stamina, #7 writing, #3 knowledge-compounding (the response repeatedly says "the build under-delivered our own design"); **(iii) citable design positions the team defends, not oversights** — #1 (knowledge-first / "reading-strategy atoms explicitly not modelled," per Hendrick+Willingham that strategy instruction has a low ceiling) and #5 (no oral-language, because MAP is silent cold reading and audio scaffolds would teach the wrong thing); **(iv) reviewer factual errors the response corrects with data** — the **~87% MCQ** number (was the old course), the specific **mistag example** (vocab items on L.3.4+RI.3.4 are defensible), and the "no teaching step" framing (true only for 7 unbuilt front-matter lessons, since instruction lives in PowerPath, absent from the OneRoster/QTI pull). The BrainLift independently corroborates kind (iii) as *locked decisions* and lists its own **verified-false misclaims it refused to make** — "MAP is 68% grammar" and "~45% literary" (MAP is ~40/40/20) — evidence the team polices its own numbers. *Conclusion: reward kind (i)/(ii) honesty and kind (iii) as defensible design (agree or not, they're citable, not sloppy); treat kind (iv) as the discipline the prime directive asks you to apply — "a deliberate citable position is not an oversight." The one place to still push is where a defended position (iii) also under-delivered the spec (iii∩ii): #3.* *(BrainLift locked decisions + Dropped-approaches (68%-grammar/45%-literary rejected) · Feedback #1/#5/#8 · Response #1/#5/#8a/#8b. Status: mixed — own-failures Verified-owned, design positions Asserted-defended, reviewer-errors Verified-corrected.)*

**S9 — The team's own approval scorecard already says where the gap is (self-audit as evidence).**
The BrainLift's "Case for Approval" tab carries the team's *own* pass/fail against an 8-dimension eval rubric + a Tier-0/1/2 learning-science hierarchy — and a reviewer should weigh that it **flags its own remaining gap** rather than hiding it. Scored **PASS:** granularity, coverage & rigour (7 formats/94% CASE/cold test), misconception-hardening (238 items + near-neighbor distractors), and — shipped/validator-confirmed — **Caliper event emission** (Tier-0-adjacent). Scored **PASS (encoded) · Asserted (runtime):** instruction quality and mastery-truthfulness (the runtime proof of a miss *blocking* advancement is the piece a live walkthrough must confirm — the exact seam the reviewer exploited in #9). Scored **Partial — the one self-named engine gap:** *retrieval practice + spaced review* — cold-passage retrieval and cross-domain threads exist, but the **platform spaced-repetition scheduler (FSRS) is "the one remaining engine-side integration item."** *Conclusion: the team's own audit and the reviewer's findings converge on the same short list — runtime mastery-gate proof (now largely built, S3) and the spaced-review scheduler; the pilot is what closes both. A self-audit that surfaces its own weakest dimension is itself a trust signal.* *(BrainLift "Approval-criteria coverage" + "Learning-science hierarchy" + "Done vs in flight" · Response scorecard. Status: mixed — most Verified/shipped; spaced-review Open.)*

---

## 7. Experts & evidence base (the pedigree the design inherits)

The design's stance is not ad hoc; it inherits from named authorities. A reviewer should recognize these as the reading-science canon:
- **E.D. Hirsch Jr.** (*The Knowledge Deficit*) & **Daniel Willingham** (*Why Don't Students Like School?*) — knowledge, not skill, is the engine of comprehension (the whole knowledge-first stance).
- **Recht & Leslie (1988)** — the baseball-passage study: domain knowledge dominates decoding for comprehension at G3.
- **Natalie Wexler** (*The Knowledge Gap*) & **Robert Pondiscio** — the G3–4 reading cliff as content-light K-2 failure; simplifying content widens the gap.
- **Doug Lemov** (*Reading Reconsidered*) & **Maryanne Wolf** (*Reader, Come Home*) — complex text, deep reading, sustained attention.
- **Carl Hendrick** — the incumbent (AlphaRead) author; the design adopts his KCT1–KCT5 taxonomy + EDI structure but **deviates on video** (his uses Schema/KC videos; this uses none).
- **Bonnie Meyer & Karen Wijekumar** — the four text-structure subsumer schemas the course explicitly over-trains.
- **Becky Allen** — the mastery-assessment blueprint (90% pass, 24-item form, 5 parallel forms, p_m≥0.90 target) + teacher-as-predictor validation framing.
- **Andy Montgomery** (Winter MAP 2026 Session-3 Recap) — the Three Intervention Buckets (More Efficient / More Effective / More Rigorous), the EGM>0→4.5X vs EGM=0→2.8X correlation, and the naming of **Grade-3 Reading as the worst combined slice** (why this course exists).
- **Pritish Chakravarty** — the 13-criterion third-party-app eval rubric used as the design audit lens.
- **IES / What Works Clearinghouse** — *Improving Reading Comprehension in K–3* (NCEE 2010-4038): the strongest-evidence guide the reviewer applies, and the source the response's 6-step gradual-release dose ("model it → do it together → release it") is built to match.
- **Sarah Cottinghat** — the expert academic reviewer of the first build; author of the verdict *"a well-built, MAP-styled practice-and-assessment engine, not a comprehension curriculum"* and the 11 findings this whole review turns on.

**The KCT atom taxonomy (what "knowledge-first, no strategy atoms" concretely means).** Every teachable unit is one of five knowledge-component types — **Domain · Vocabulary · Text-structure · Meaning-relationship · Inference** — inherited from Hendrick's KCT1–KCT5. There is deliberately **no "reading-strategy" atom type**; that is the design decision the reviewer's #1 contests and the response defends (S8-iii).

**Provenance — this is a synthesis of seven independent proposals.** v2 is the amalgamation of seven upstream Grade-3 BrainLifts, labelled A–G in the DOK1 sources: **A** Anuj (dosage-first + prediction engine) · **B** Abdul (4 engines + 3 bands) · **C** Praveen (blended plan + critique passes; source of the topic-coherence-fade Insight 2) · **D** Stan (item-factory + measurement; +v3 corrections) · **E** Parth (skeleton + ladder) · **F** Anirudh (388 starter QTI files + BrainLift) · **G** Samkit (52-lesson 5-stage fade). The "locked decisions" (§8) are precisely the points on which **all seven converged** — which is why they're treated as the floor, not one author's preference.

*Source: [BrainLift](https://docs.google.com/document/d/1qP5JSriZBosWWvuFKl0cyX9eLjNEKvUZbPXnIzE-wfg/edit?tab=t.3ux9kqm3q4x6) → open the **"BrainLift"** tab, headings **"Experts"** and **"DOK1 — Facts and Sources"** (proposal authors A–G); reviewer name + IES/WWC citation are in the [feedback doc](https://docs.google.com/document/d/1mK96r9bk35NzK4X1PWHRd7Gt5zi_ao2B/edit) ("Sources").*

---

## 8. Locked decisions, open forks, and the honesty ceiling

**Locked (every v2 proposal converged on these):** dosage-first; explicitly teach the four schemas + inference co-equal; knowledge-first / no reading-strategy atoms; **no video** (audio fades); design-toward-MAP with no measured MAP claim pre-pilot; MAP-styled mastery on unseen passages replacing STAAR; **untimed** comprehension; ~60 daily doses ≈ one semester; **3 mastery-gated bands**; staged 90% gates (advisory in A, blocking from B).

**Open forks (genuine judgment calls, not blockers):** (Q4) decoding/fluency ownership — in-course strand committed, non-ASR default, ASR-as-enhancement still open; (Q5) audio policy — supportive-only default vs early-full-read-aloud-faded; (Q6) MAP validation — proxy-only vs administer NWEA MAP at pilot (an org/access call; the SPOV7 honesty floor holds either way).

**Approaches deliberately dropped (with rationale — a reviewer should read these as evidence of design intent, not omission).** Each was considered and rejected on a stated ground:
- **All-MCQ assessment** — reproduces the incumbent's #1 broken metric (1 of 6 formats). → 7 formats.
- **Difficulty escalation after a miss** — destroys attempt-2 accuracy (the 64%→41% evidence). → no-escalation, reteach-first, three-state retry.
- **The "+6 RIT / 2× growth / CGP 80" headline** — no precedent in the intervention literature; the SD→RIT conversion is itself an estimate. → direction-not-magnitude (SPOV4).
- **A permanent illustration/character wrapper** — scaffolds that don't fade teach dependency. → the "Scout" cast fades across 9 dimensions to cold text.
- **A skills-first course spine** — violates knowledge-first. → KCT atoms only.
- **Audio as a first-class instructional feature** — undermines the cold-text construct. → audio = fading pronunciation/gloss only.
- **FRQ/constructed-response on the *final*** — MAP is 100% auto-scored, so it wouldn't transfer to the MAP target (short written CR is kept *formative* + STAAR-aligned, not on the MAP-styled final).
- **Two misclaims the team verified false and refused to make** — *"MAP is 68% grammar"* (false) and *"~45% literary"* (false; MAP is ~40/40/20). *This is load-bearing for the reviewer: the team caught and killed its own convenient-but-wrong numbers — the honesty discipline of S4/S8 in action.*

**Honesty ceiling / measurement discipline:** lead the pitch on the *broken metrics* (dosage, completion, the 39–48% skills, the 90% bar, acceleration); treat RIT as the post-pilot target. The calibration loop, weak-item retirement, the proxy→MAP link, and any RIT number run **observe-only** (log what they'd decide, change nothing) until an in-cohort MAP test exists. When it does: validate the *tails* (struggling + advanced), not just the average; trust growth among students who mastered the skill over a single pooled effectiveness number (which "behaves backwards on this cohort"). **No "proven" or "builds any course" claim before the pilot.**

*Source: [BrainLift](https://docs.google.com/document/d/1qP5JSriZBosWWvuFKl0cyX9eLjNEKvUZbPXnIzE-wfg/edit?tab=t.3ux9kqm3q4x6) → open the **"BrainLift"** tab, headings **"Locked decisions" / "Open forks" / "Dropped approaches (with rationale)" / "Honest ceiling / measurement discipline."***

---

## 9. Sources (full links — substance is above; these are for depth)

- **BrainLift** — [Case-for-Approval doc](https://docs.google.com/document/d/1qP5JSriZBosWWvuFKl0cyX9eLjNEKvUZbPXnIzE-wfg/edit), **"BrainLift" tab** (tab id `t.3ux9kqm3q4x6`). The DOK-tiered design rationale, evidence tree, experts, locked decisions.
- **Case for Approval** — same doc, **"Case for Approval" tab** — the pilot ask, incumbent breakages, what's built, the one honest tension.
- **Reviewer feedback** — [Google Doc](https://docs.google.com/document/d/1mK96r9bk35NzK4X1PWHRd7Gt5zi_ao2B/edit) — the 11 items + knowledge-first lens + "practice-engine not curriculum" verdict.
- **Response-to-Reviewer** — [Google Doc](https://docs.google.com/document/d/1LXNc5-ezBycWZwdUaRPNeDJr-Iq21yAMvKDKt44ukaE/edit) — item-by-item Accept/Partial/Counter with live-verified results.
- **The live course** (student view) — https://read.inceptapi.com/?course=reading-explorers-v2
- **Live API pull** (recompute any number) — QTI `https://qti.alpha-1edtech.ai/api` + OneRoster `https://api.alpha-1edtech.ai`, course `reading-explorers-v2`.
- **Cohort ground-truth** (§2a/2b/2c) — the TimeBack Reporting MCP (`getData` over the `rpt2_*` views).
- **Companion skills** (`.claude/skills/`): `reading-course-review/SKILL.md` (audit the live course, recompute every count); `grade3-proposal-review/SKILL.md` (compare proposal folders)
