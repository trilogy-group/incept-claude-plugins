# Course Approval request — EduLLM Grade 5 Reading (g5-reading-merged-pp-9802)

*DRAFT — NOT transmitted. Editable source for the cover email; sender of record is Rahul.
Confirm To/Cc and the links before any send; nothing goes out without Stan's explicit OK.*

---

**From:** Rahul Subramaniam <rahul.subramaniam@devfactory.com>
**To:** Andy Montgomery <andy.montgomery@alpha.school>
**Cc:** Stan Huseletov
**Subject:** Course Approval request — EduLLM Grade 5 Reading (g5-reading-merged-pp-9802)

---

Hi Andy,

I'd like your approval for **EduLLM Grade 5 Reading — `g5-reading-merged-pp-9802`** as the
**MAPS-practice course** of the two-course split we agreed at the CoE: this course owns
MAP-styled practice and measurement; the comprehension-teaching layer is a separate core course.

The headline is a measured anti-leak instrument. On encyclopedic grade-5 passages, a cross-family
blind solver — given the questions without the passage — answers conventionally-authored MCQ at
99.5% and MSQ at 100%. The fix is per-item certification: an item ships only if the blind solver
fails it without the passage and solves it with the passage. **549 of the course's 772 items are
certified** — the hot-text/sequence/match core (358 items) blind-probed cross-family on its own id,
and 188 choice + 3 EBSR via a same-family 2-vote choice lane, held through a hardened re-gate, a
bank-depth wave that independently re-gated the remaining pool, and a sequence multi-shuffle
re-probe. The leaky formats turned out to be fixable, not just excludable:
per-item redesign lanes carried the certified core to **188 choice items** (88 MCQ + 100 MSQ) and
**132 hot-text items** (counts by item id-label; 34 items render as a different interaction than
their id suffix — per-item map in the ledger). The incumbents, measured on the same pull: **both
are 100% single-select with 0 mastery gates.**

The rest of the build, live and read-back verified: **94 tests / 772 items** on PowerPath-100,
every item type server-scored, a ≥90% mastery gate engine-enforced on all 81 gating tests,
**corrective feedback on 772/772 items**, and **five parallel 24-item mastery forms plus an
8-lesson spaced-review unit live** — both built only from certified items. Every one of the 772
items carries a measured disposition — 549 certified / 223 excluded / 0 unknown; standards
resolved to official CASE GUIDs on 772/772; scoring behaviorally swept on 772/772 (every item
pays full credit only for the declared-correct response).

**The ask:** approve `g5-reading-merged-pp-9802` as the MAPS-practice course of the split.
MAP-linked outcome measurement then needs one input the course can't produce itself — the
student-ID crosswalk and an in-cohort pilot.

Two links:

- **The live course** — https://alpha.timeback.com/app/course/g5-reading-merged-pp-9802
- **The approval bundle** — `COURSE_BUNDLE_FOR_APPROVAL.qmd` in the source repo (the course, the
 per-item ledger, and every artifact behind the numbers; the per-item ledger also travels
 as `item-ledger.json` in this folder)

Happy to walk through any of it live.

Rahul
