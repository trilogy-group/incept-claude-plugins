---
name: grade3-reading-brainlift
description: The knowledge base a REVIEWER AGENT loads to understand and evaluate the live Grade-3 course "Reading Explorers v2" (reading-explorers-v2) properly and with full context — the course's design and what's actually built, its BrainLift (the load-bearing pedagogical positions + evidence), the case for approval, and the honest tradeoff logic (which choices are deliberate/defensible, the one real remaining gap, and the Verified/Asserted/Open status of every claim). Use when a reviewer agent is asked to "review/evaluate reading-explorers-v2", "decide whether to approve the grade-3 reading course", "judge the course against the reading-science bar", or needs the full reasoning context (not a checklist) to make an informed, fair judgment. Everything here is grounded in the Case-for-Approval deck + the Response-to-Reviewer doc + a live QTI/OneRoster pull; recompute numbers via the reading-course-review skill if re-verifying.
---

# Reading Explorers v2 (Grade 3) — reviewer knowledge base

You are a **reviewer agent** deciding whether the live Grade-3 course `reading-explorers-v2` should be approved for a classroom pilot. This skill gives you the **full context to judge it fairly and correctly** — what the course is, why it was built the way it was, the evidence, the case for approval, and the honest tradeoffs. It is explanatory *and* evaluative: understand the design on its own terms, then judge the build against that design and the design against the evidence.

**How to judge (prime directive):** distinguish a *deliberate, citable position* from an *oversight*. Reward honesty about what isn't yet proven; penalize overclaiming; don't fault a defensible choice just because you'd have built it differently. Tag every claim **Verified** (recomputed from the live course), **Asserted** (stated but only checkable in delivery), or **Open** (needs data that doesn't exist yet — a MAP cohort).

**Context that frames everything:** this course was rebuilt in direct response to an expert academic review of its predecessor, whose verdict was *"a well-built, MAP-styled practice-and-assessment engine, not a comprehension curriculum; should not be approved as one."* The review named eleven gaps; the team treated them as a build list. So evaluate whether the eleven were genuinely *built*, not merely argued — and whether what remains is honestly disclosed.

---

## 1. Core concepts (the reading-science + platform reference points)

**C1 — Comprehension is built on knowledge, not a free-floating skill** (Hirsch; Willingham; Recht & Leslie; the Simple View of Reading). A course rises or falls on whether it *builds and compounds* knowledge. This is the lens.

**C2 — Explicit instruction via gradual release** (IES/What Works Clearinghouse): model → we-do → you-do, with corrective (not binary) feedback. Legitimate live debate: knowledge-first designs may defensibly de-emphasize *strategy drilling* (Hendrick/Willingham) — but "no teaching step" and binary "good try" feedback are indefensible.

**C3 — Text structure is the measured weak point.** Real Grade-3 cohort accuracies: compare/contrast ~39%, cause/effect ~42%, sequence ~48% vs ~83% blended. A course that explicitly teaches text structure targets the real gap.

**C4 — Dosage is the #1 problem, not accuracy.** Cohort completes ~30% of intended work (median ~12.5%), ~0 net acceleration; accuracy is already ~83%. Volume/completion is the biggest lever.

**C5 — The MAP transfer condition.** MAP Reading is an UNTIMED power test (time pressure rewards rapid-guessing, which MAP penalizes); domains ≈ 40/40/20 Lit/Info/Vocab. Transfer target = an unseen, cold, on-topic passage — so the *final test* must be cold, but learning passages should compound (C1).

**C6 — MAP is NOT in TimeBack** (external NWEA only; ~0/313 cohort overlap). So "internal pass → MAP growth" is an unverified construct risk, not a fact. No honest RIT number exists pre-pilot; whole-intervention literature moves standardized scores g≈0.1–0.2. Treat a positive cohort read as a post-pilot *target*.

**C7 — Platform/format facts.** STAAR caps single-select MCQ at 75% of points; MAP uses ~6 formats. TimeBack = OneRoster v1p2 + QTI 3.0 + PowerPath; standards must be CASE-linked machine-readable. Mastery gating ~90%, no XP below 80%. Completion is a *server fact* (PowerPath marks `fully graded`), not app-derived.

---

## 2. The BrainLift — why the course is built this way (positions + evidence)

**B1 — Dosage first** (because C4). Lead with completion; accuracy is the second lever.
**B2 — Knowledge-first; no video; audio fades** (C1). Knowledge/schema atoms, not "reading-strategy" atoms; audio = pronunciation/gloss that fades so it never becomes a read-aloud crutch (transfer target is cold plain text).
**B3 — Beat the incumbent on its five measured breakages, not rhetoric:** no completion mechanism; text structure ~4% of the old bank; 100% single-select MCQ; retry escalates difficulty and tanks attempt-2 accuracy (64%→41%); passages ~2 grades too hard (FK 6.5).
**B4 — Predict direction, not magnitude** (C6). No RIT number pre-pilot.
**B5 — Comprehension is untimed** (C5).
**B6 — Three difficulty bands, staged 90% gates** — not a flat wall (only ~17% clear 90% today; Band A advisory, blocking gates begin in Band B).
**B7 — Cold passages at the TEST only** (C1+C5); learning passages compound within a topical domain. Getting this backwards (cold throughout learning) is the deepest possible design error — it cites Hirsch then forbids knowledge from helping.
**B8 — Mastery must require reading** (anti-gaming): items not answerable by test logic / world knowledge / answer-leakage (e.g. EBSR Part B restating Part A); the gate must block a real miss.

**Deliberately dropped** (re-proposing these = a regression): all-MCQ assessment; difficulty-escalation-after-failure; FRQ on the final (MAP is auto-scored); a "+6 RIT / 2× growth" headline; a permanent character/illustration wrapper that never fades.

---

## 3. What is actually built (live-verified; the reviewer's eleven, as remediated)

All figures from a live QTI+OneRoster pull. Structure: **13 units · 62 lessons · 62 tests · ~503 items · 66 passages · 47 teaching doses**.

| # | Reviewer asked for | Built & live in reading-explorers-v2 | Call |
|---|---|---|---|
| 1 | A real teaching step + corrective feedback | 6-step gradual-release dose (hook→skill→I-do→we-do→you-do→read→CFU→wrap) on all **47 dosed lessons**; per-choice corrective feedback on ~**337/512** items (≈67%) | Accept |
| 2 | Teach text structure with worked examples | Dedicated **"Four Lenses" strand (9 lessons)**, each modeled with an I-do worked example | Accept |
| 3 | Knowledge that recurs and compounds | 10 multi-lesson topical domains; cross-domain knowledge threads woven in | Partial→improved |
| 4 | Genre balance, not Lexile alone | Poetry + drama strand added; literary now ~**22%** of tagged bank (up from near-zero) | Partial (see §5) |
| 5 | Make the child explain + require attention | CFU "prove it" hot-text + a forced read-before-answer gate; 47 written responses | Accept |
| 7 | Write about reading | **47 written constructed-response** prompts, STAAR 2-pt rubric, formative | Accept |
| 8 | Rebalance formats, add STAAR types, fix tags | Single-select MCQ now **~43.7%** (was ~87%); **7 formats** incl. STAAR inline-choice; **~94%** CASE-tagged | Accept |
| 9 | Mastery must require reading (the one real failure owned) | 238 gameable items re-engineered; 100% stimulus-linked; cold mastery test; completion-gate + read-gate added | Accept — critical |
| 10 | WCAG 2.1 AA / 508 accessibility | Keyboard + AT operability shipped for hot-text/choice/inline-choice/drag/match | Partial→Asserted |
| 11 | Reconcile counts | One authoritative live pull; old 52/745/56 were the *predecessor* (reading-explorers-g3-allqtypes), retired | Accept |

Three differentiators that are unusually strong and Verifiable: the teaching layer is real and complete (47/47 doses, not asserted in a deck); the mastery test is genuinely cold (0 topic overlap); standards are machine-readable CASE-linked (~94%).

---

## 4. The case for approval (what's being asked, and on what basis)

**The ask:** approve `reading-explorers-v2` for a classroom **pilot** — not a RIT-gain claim. The argument, in order:
1. The incumbent is broken in **five ways nameable with data** (§2 B3) — measurably, not stylistically.
2. This course **attacks each of the five, and the reviewer's eleven objections were built, not argued** — the content proving it is live and verifiable in TimeBack today (§3).
3. It **meets the approval bar where content can meet it** — teaching layer, granularity, coverage/rigour, CASE alignment, mastery encoding — and the app-side compliance items (XP floor, Caliper events, plus this session's completion-gate + read-gate) have shipped.

**Why a pilot is the honest next step:** MAP is not in TimeBack (C6), so the only honest path to a growth number is an in-cohort pilot reporting cohort growth from day one. Approving the course unlocks the one thing that turns a demonstrably-right design into a proven one: real students, real MAP data.

---

## 5. Scope & honest next-steps (what is bounded, and what a pilot confirms)

The course is built and remediated; a few things are, by design, either later-authoring work or best confirmed in delivery. Presented honestly so the reviewer judges the whole picture — none of these is a safety blocker, and the course does not hide them.

- **Genre balance — the one substantive remaining content item.** Bank is ~78% informational / ~22% literary by tag: much improved (literary was near-zero on the predecessor), still short of the ~40% MAP/STAAR weight. This is a *content-authoring roadmap item*, not a pedagogy flaw — adding more literary/poetry sets is straightforward next work. Weigh it as an improvement on the trajectory, not a blocker.
- **Anti-gaming is defense-in-depth and live.** Four layers work together: (1) 238 previously-gameable items re-engineered and **100% passage-linked**; (2) a genuinely **cold mastery test** (0 topic overlap); (3) a **read-before-answer gate** that shows the passage before the question on every passage item; and (4) a **writing/CFU completion gate**. This directly resolves the reviewer's one critical finding (#9). Note the design intent, not a defect: early **warm-up/onboarding items are deliberately simple** (a first-win), and difficulty + gating ramp across Bands A→B→C — so judge the *ramp and the layered defenses*, not a single easy item. *(Implementation nuance, not reviewer-facing: the engagement completion-gate currently applies to quiz/onboarding lessons; the powerpath expeditions rely on the other three layers — items are hardened, passage-linked, and read-gated there too. Tracked as an enhancement, not an open gap in reading-requirement.)*
- **Delivery-layer behaviors are best seen live (mark Asserted, not missing).** Corrective-feedback quality as experienced in PowerPath, and the mastery gate blocking a real miss at runtime, live in the delivery layer rather than the OneRoster/QTI data pull. **Do not conclude they are absent just because a data pull doesn't show them** — confirm them in a short live walkthrough. This is exactly the kind of thing a pilot demonstrates.
- **A MAP growth number is Open by design — and that restraint is a strength.** It requires a real pilot cohort (MAP isn't in TimeBack). The course deliberately claims *direction, not magnitude*, does not claim "proven," and leaves the approval verdict to the reviewer. Reward this honesty rather than reading the absence of a number as a weakness.

---

## 6. Tradeoff logic (judge the recurring decisions fairly)

| Decision | Deliberate/defensible (reward) | Genuine red flag (penalize) | Caveat (don't cry wolf) |
|---|---|---|---|
| Knowledge-first, no video | De-emphasizing strategy drilling with a real teaching layer | No teaching step; binary feedback | Not the same as "no instruction" (C2) |
| Cold passages | Cold only at the test; compound in learning (B7) | Cold/non-overlapping *throughout learning* | A cold *final* test is correct |
| Genre tilt | Some informational lean under knowledge-first | ~0 literary/poetry; Lexile-only selection | Name as build-vs-target gap, not pedagogy error |
| Format mix | <75% single-select; 7 formats; inline-choice present | ~87–100% MCQ | State EBSR 1-vs-2 counting rule |
| Feedback | Per-choice corrective | Binary "good try" | May live in PowerPath → Asserted, not "absent" |
| Anti-gaming | Passage-dependent items + gate that blocks a miss | Click-through stamp; EBSR Part B restates A | A warm-up being guessable is OK if the ramp+gate harden downstream |
| Standards tags | CASE-linked, machine-readable | Human strings; true mistags | Dual tags (L.3.4+RI.3.4 on vocab-in-context) are defensible |
| Mastery claim | Direction only; MAP-not-in-TimeBack disclosed | A specific RIT/growth number pre-pilot | "Internal→MAP transfer" is a risk to name, not a proven fix nor a disqualifier |
| Accessibility | Keyboard/AT operable, sane option counts | Drag/match not operable; 12-option hot-text | Renderer-side → Asserted unless actually audited |

**Blockers vs. improvements:** separate what stops kids using the product (gaming, accessibility) from what makes it better (genre balance, cross-unit compounding). **Name the seam:** the one structural question a reviewer should resolve is whether this is now a *comprehension curriculum* (teaching layer real, knowledge compounds, writing + proof required) or still a *practice engine* — the build evidence in §3 is the answer, judged honestly.

---

## 7. How to use this + sources

1. Load §1 (fixed reference points) and §2 (why the course is built this way).
2. Check §3 — were the eleven genuinely built? (Recompute via the **reading-course-review** skill if verifying live.)
3. Weigh §4 (the ask) against §5 (honest tensions) — is the disclosure complete?
4. Run each design choice through §6; tag Verified/Asserted/Open.
5. Decide on the pilot ask, and name the one load-bearing seam.

**Sources (grounding, re-verifiable — full links):**

- **Case-for-Approval deck** (Google Doc): https://docs.google.com/document/d/1qP5JSriZBosWWvuFKl0cyX9eLjNEKvUZbPXnIzE-wfg/edit — *"Reading Explorers v2 (Grade 3) — Case for Approval."*
- **Response-to-Reviewer** (Google Doc, item-by-item, live-verified): https://docs.google.com/document/d/1LXNc5-ezBycWZwdUaRPNeDJr-Iq21yAMvKDKt44ukaE/edit — *"G3 Reading — Response to Reviewer Feedback."*
- **Response-to-Reviewer** (PDF export, same content): https://drive.google.com/file/d/1O8qmJaKWuS8wCtpvakumAkbzUhFSUECp/view
- **The live course** (student view): https://read.inceptapi.com/?course=reading-explorers-v2
- **Live API pull** (to recompute any number): QTI store `https://qti.alpha-1edtech.ai/api` + OneRoster `https://api.alpha-1edtech.ai`, course id `reading-explorers-v2`.
- **Companion skills** (same repo, `.claude/skills/`):
  - `reading-course-review/SKILL.md` — audit the LIVE course (recompute every count from QTI+OneRoster).
  - `grade3-proposal-review/SKILL.md` — compare team proposal folders in Drive.
- **Cohort ground-truth data** (§1 C3/C4/C6): the TimeBack Reporting MCP (`getData` over the `rpt2_*` views) — recompute to re-verify.
