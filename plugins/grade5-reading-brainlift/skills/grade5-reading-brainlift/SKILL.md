---
name: grade5-reading-brainlift
description: The complete, self-contained brief and operator manual for the live Grade-5 reading course EduLLM Grade 5 Reading (sourcedId g5-reading-merged-pp-9802; PowerPath-100, alpha.timeback.com). This folder is fully portable — SKILL.md plus co-located references/ (per-item ledger, evidence summary, decision memo, BrainLift, dated pull record, cover email) and scripts/ (nine stdlib-only Python tools including a self-contained TimeBack API client); no repository access required. It serves two audiences from one file. (1) Evaluators and reviewers — load this when asked to "review g5-reading-merged-pp-9802", "evaluate g5-reading-merged-pp-9802", "judge the grade 5 reading course", "access the G5 course", "open the course", or assess the G5 reading bake-off entry; it carries the access path (sign-in, the enrolled reviewer accounts, the blank-course fallback), the full design argument (the leak-by-format finding, per-item cross-family certification, the conversion-by-rewrite result), the live-verified build state (94 tests / 772 items, 541 certified under a uniform same-day gate, feedback 772/772), the review frame (the CoE two-course split, the D6-D12 demands register, the three governing review items), and the source map that makes every number recomputable. (2) Operators — load this when asked to "work on the G5 reading course", "run the anti-leak gate", "deploy G5 items", "regen G5 items", "author G5 feedback", "run a blind probe", "enroll a reviewer", or for any "G5 reading operations" task; it documents authentication (env names only), the read/write API surface (QTI PUT-update rule, OneRoster, Caliper), the reviewer-enrollment recipe, and the bundled scripts (scripts/) that authenticate, run the blind-solve gate, regen batches with snapshot/rollback, feedback scan/author/deploy, and live probes. Grounded in the co-located references/ files (item-ledger.json, evidence-summary.md, case-for-approval.md, brainlift.md, live-pull-summary.json, cover-email.md) and the live course at https://alpha.timeback.com/app/course/g5-reading-merged-pp-9802.
---

# EduLLM Grade 5 Reading — g5-reading-merged-pp-9802 — brief + operator manual

> **Packaging note.** This skill was authored to be portable with co-located `references/`
> (item-ledger.json, live-pull-summary.json, evidence-summary.md, case-for-approval.md,
> brainlift.md, cover-email.md) and `scripts/` (nine Python tools including
> `timeback_client.py`) directories, as described throughout this file. **Those two
> directories are not yet present in this plugin** — only this SKILL.md has been added so
> far. Until they are supplied, treat every `references/*` and `scripts/*` reference below as
> a pointer to a file that does not yet exist here: an evaluator cannot recompute a cited
> figure from a bundled file (fall back to the live APIs in §6.2, credentials permitting), and
> an operator cannot run any of the §6 recipes. Add the two directories to
> `skills/grade5-reading-brainlift/` alongside this file to complete the package.

**Course:** **EduLLM Grade 5 Reading** — sourcedId `g5-reading-merged-pp-9802`, live on
PowerPath-100 — https://alpha.timeback.com/app/course/g5-reading-merged-pp-9802. (The course
and class objects were renamed to this title on 2026-07-06; the sourcedId and URL are unchanged.)
**State (2026-07-06):** 94 tests (81 gating at ≥90% + 8 non-gating review lessons in Unit 3 + 5
non-gating parallel mastery forms in Unit 4) / 772 items. Certified 541/772 under a uniform
same-day cross-family gate. Feedback 772/772. Every item carries a measured disposition.

## Start here — what do you want to do?

One router, every branch ≤3 hops. Take the first line that matches.

- **SEE the course as a student** → **§2 Access**. The title to look for (**EduLLM Grade 5
  Reading**), the direct link, the sign-in path, the enrolled reviewer accounts, the
  blank-course fallback, and the no-login alternative are all there.
- **REVIEW / JUDGE the course** → read **§3 The design argument**, then **§4 What is built**,
  then **`references/evidence-summary.md`**. If you hold credentials, recompute any figure via
  **§6 Operations**. The decision ask is **`references/case-for-approval.md`**.
- **UNDERSTAND the method (the gate, certification)** → **§5 How it was built** — the regen
  loop, the cross-family blind gate, and the winning item designs per format.
- **OPERATE (probe / regen / feedback / deploy / enroll)** → pre-check: do you have
  `TIMEBACK_SSO_CLIENT_ID` / `TIMEBACK_SSO_CLIENT_SECRET` in your env (**§6.1**)?
  - **No** → read-only paths: the bundled `references/` data (per-item ledger, evidence
    summary, dated pull record) — no live calls.
  - **Yes** → **§6 Operations**; each operation is a numbered recipe with its script:
    **§6.2** read anything · **§6.3** run the blind gate · **§6.4** regen a batch ·
    **§6.5** feedback · **§6.6** enroll a reviewer · **§6.7** Caliper. The seq/match probe
    additionally needs `TFY_API_KEY` / `TFY_BASE_URL` (§6.3).
- **Something looks wrong / a number doesn't match** → recompute from live: **§6.2** (read) +
  **§6.3** (re-probe) on the per-item IDs in **`references/item-ledger.json`**; the dated counts
  record is **`references/live-pull-summary.json`**.

## 1. What this is

**Portability.** This folder is complete. What travels: this file, `references/` (the per-item
ledger, the evidence summary, the decision memo, the design BrainLift, the dated pull record,
the cover email), and `scripts/` (nine stdlib-only Python tools, including `timeback_client.py`
— a self-contained API client). What you need to operate: credentials, by env name only —
`TIMEBACK_SSO_CLIENT_ID` / `TIMEBACK_SSO_CLIENT_SECRET` for the platform (§6.1) and
`TFY_API_KEY` / `TFY_BASE_URL` for the cross-family solver (§6.3). What's optional: access to
the source repo (`trilogy-group/ti-courseplans`) and the origin machine's artifacts — every
load-bearing number here either travels in `references/` or is recomputable from the live APIs.
Drop this folder into `.claude/skills/` or open this file in any Claude Code session.

The thesis in one paragraph: on encyclopedic grade-5 passages, whether a reading item can be
answered *without reading the passage* is set primarily by question **format** — MCQ leaks at
99.5% and MSQ at 100% to a blind solver, while hot-text (1.67%), sequence (0%) and match (0%)
force a return to the text. Format alone is not certification: the uncertified anti-leak-format
pool still leaked ~78% on a live baseline, so certification is **per-item** — a cross-family
blind solver must fail the item without the passage and solve it with the passage. And the leaky
formats are **convertible**: the choice lane redesigned 142 of 234 MCQ/MSQ items (61%) into
passage-dependence by rewrite, and the hot-text lane converted 90 of 117 via the
claims-about-passage construct. The product of that discipline is a 541-item certified
measurement instrument inside a live 772-item course, held to one uniform measurement: every
certified item blind-probed on its own id under the same solver on the same day (2026-07-06).

This file is both the design brief (sections 3–4, 7) and the operator manual (sections 5–6).
An agent with this folder and the listed credentials can read the live course, run the gate,
regenerate items, deploy with rollback, author feedback, and re-probe.

## 2. Access — open the course as a student

The course title to look for is **EduLLM Grade 5 Reading**. (Renamed 2026-07-06; the sourcedId
and URL did not change: `g5-reading-merged-pp-9802`.)

1. **Direct link:** https://alpha.timeback.com/app/course/g5-reading-merged-pp-9802
2. **Sign in** at https://alpha.timeback.com with your `@alpha.school` (or `@2hourlearning.com`)
   account. The flow is a **student-seat experience** (PowerPath): reviewer accounts are
   enrolled in the course class as students so the course renders for them. An account that is
   not enrolled may see a blank page or no course at all — that is an enrollment state, not a
   broken course.
3. **If the direct link shows nothing:** check the course list / dashboard for **EduLLM Grade 5
   Reading**. If it still isn't there, your account isn't enrolled — send your email or account
   id and enrollment takes one API call (§6.6). A set of reviewer accounts is pre-enrolled
   (roster of ~10 reviewers, internal — see the project's own reviewer-access records for the
   current list; redacted here since this skill is published in a public repository).
4. **What you'll see:** 4 units — Units 1 & 2 (81 gated lessons, ≥90% mastery to advance),
   Unit 3 "Review What You've Read" (8 spaced-review lessons, non-gating), Unit 4 "Show What
   You Know" (5 mastery checks, non-gating).
5. **No-login alternative:** the item bank and structure are fully inspectable via the API
   (§6.2) or the bundled `references/` data (per-item ledger, evidence summary, dated pull).

## 3. The design argument

**Defining feature of mastery.** A mastered G5 reader comprehends an unseen on-topic passage at
the grade-5 band by deploying domain knowledge, grade-5 vocabulary, and the four text-structure
schemas (cause/effect, compare/contrast, sequence, problem/solution) automatically — locating and
ordering the specific passage text an item demands at ≥90% accuracy, untimed. Mastery does not
require strategy verbalisation; "reading-strategy" atoms are not modelled. Atom/KC carving is a
first-class KC graph: 47 KCs on Carl Hendrick's KCT1–5 taxonomy, 60 typed edges on Becky
Allen's four-edge schema, 17 misconceptions (the graph file itself lives in the source repo —
access optional; the design argument that rests on it travels in `references/brainlift.md`).

**The positions that carry the weight:**

1. **Format sets the default leak.** Same passages, cross-family blind solve, item text only:
   MCQ 99.5% / MSQ 100% vs hot-text 1.67% / sequence 0% / match 0% (2026-06-23/24 runs). The
   passage is not the only lever; the format is the strongest single one.
2. **Format is not certification.** The uncertified Unit-2 pool of anti-leak *formats* still
   leaked ~78% weighted on its own IDs (live baseline, gpt-4.1, 2026-07-02) — item design can
   telegraph the answer inside a safe format. Certification is per-item or it is nothing.
3. **Certification = cross-family blind-fail + with-passage-pass.** The solver family must
   differ from the generator family (a model grading its own family's output does not count).
   An item is certified only when the blind solve fails AND the with-passage solve succeeds —
   the second leg guards against items made "safe" by being unanswerable.
4. **Conversion by redesign is proven.** The leaky formats convert to passage-dependence:
   choice 142/234 (a 20/27 pilot, then a 122/207 scale pass, at a 2-of-2 blind-vote bar) and
   hot-text 90/117 (claims-about-passage construct). Leaky-by-default is not leaky-by-necessity.
5. **The gate is uniform and bidirectional.** Every certified item was probed on its own id under
   the same solver on the same day; items that recovered — including 58 of Unit-1's June-era
   designs — moved to the excluded bucket. A gate that only ever certifies is a rubber stamp;
   this one cuts both ways, and no certification is carried from an earlier run.
6. **The measurement layer bolts under any instruction spine.** This is the MAPS-practice course
   of the org's two-course split (CoE 2026-06-30): a measurement instrument that attaches under
   whichever curriculum spine wins the bake-off. Instruction, dose, and hours belong to the
   spine winner; corrective feedback (772/772) is the one instruction component this course owns.
7. **Predict direction, not magnitude.** No RIT figure exists pre-crosswalk-and-pilot; a
   course-level RIT projection would compound two estimates into one misleading number. The
   course defers to the platform's adaptive Grade 2-5 MAP — live id `incept-map-g2g5-l1`, engine
   https://github.com/trilogy-group/Incept-MAP-proxy (repo access optional — the live instrument
   id `incept-map-g2g5-l1` is the operative reference) — as the measurement of record; no
   in-course MAP-equivalent test (decision 2026-06-29).
8. **Comprehension is untimed.** MAP Reading is an untimed power test; the G5 demand is stamina.
   No clock shown; time-on-task captured silently for rapid-guess detection.
9. **The mastery gate is built only from certified items.** A gate on unconverted MCQ/MSQ would
   be ~90% blind-solvable and would pass students who never read. A pre-merge gate form cleared
   structural checks but leaked 78% blind — the certified-items-only rule is forced by evidence.
10. **Knowledge-first, no read-aloud crutch.** Comprehension at G5 is a by-product of domain
    knowledge and vocabulary (Hirsch / Willingham / Recht-Leslie / Hendrick). No video; audio is
    pronunciation/gloss only. The transfer target is cold plain text.

**Deliberately dropped** (checked absent from the shipped course): instructional video; audio as
a read-aloud crutch; a skills-first spine; all-MCQ assessment; MCQ "for coverage" without
per-item conversion + re-gate; treating format family as certification; forcing native hot-text
through a gate protocol it structurally does not fit (tokens ≈ passage — the shipped path is the
claims-about-passage construct redesign); keeping recovering items certified; difficulty
escalation after failure (reteach-first instead); any pre-pilot RIT or growth figure.

**Attribution:** the Bespoke-Mastery assessment blueprint, the course-BrainLift template, and
predict-direction-not-magnitude are **Becky Allen**; the KCT1–5 knowledge taxonomy is
**Carl Hendrick**. The EGM=0 finding (later-reading students take mastery tests and never pass —
the binding constraint is curriculum, not test rigor) is Andy Montgomery's *Winter MAP 2026
Session 3 Recap*.

## 4. What is built (live-verified)

**Architecture.** Two content units + two supplementary units on PowerPath-100 (98 components /
94 lessons):

- **Unit-1** — 172 items, id prefix `grade5-reading-clean-pp-9801-*`; 114 certified under the
  uniform gate, 58 excluded (June-era item designs).
- **Unit-2** — 600 items, id prefix `g5-reading-ela-pp-9801-*`; 427 certified via the conversion
  lanes (197 sequence/match + 140 choice + 90 hot-text).
- **Review unit (NN6)** — 8 non-gating spaced-review lessons (Leitner spans + starred revisits),
  certified-only. Component `g5-reading-merged-pp-9802-review-unit`, lessons `-review-1..8`.
- **Mastery unit** — Unit 4 "Show What You Know": five parallel non-gating mastery forms, 24 items
  each, fully disjoint, certified-only, format quotas proportional to the certified pool.
  Component `g5-reading-merged-pp-9802-mastery-unit`, lessons `-mastery-form-a..e`.
- 94 tests total: 81 gating with engine-enforced `masteryThreshold==90`, 8 review + 5 mastery
  non-gating. A post-probe sweep replaced 29 refs across the supplementary tests so both
  supplementary units reference certified items only.
- Rendered composition: match 198, hot-text 160, sequence 167, MCQ 116, MSQ 111, EBSR 20
  (EBSR split into Part-A/Part-B structure). Every type returns HTTP 200 on `process-response`;
  a 30/30 live discrimination probe confirmed correct ⇒ full credit, wrong ⇒ strictly less.
- Standards on 755/772 items — CCSS codes resolved to official CASE GUIDs (CCSSO framework),
  read-back verified; 17 uncoded, all hot-text-lane items with the restamp pending.

**The ledger** (`references/item-ledger.json` — every item in exactly one bucket, per-ID; the
full per-item disposition travels with this folder):

| Bucket | Count | Composition |
|---|---:|---|
| Certified | **541** | 114 Unit-1 + 427 Unit-2 (197 sequence/match + 140 choice + 90 hot-text) |
| Excluded | **231** | 58 Unit-1 (June-era designs) + 107 choice (85 + 20 EBSR + 2 probe) + 39 seq/match + 27 hot-text (24 + 3 probe) |
| Unknown | **0** | every item measured on its own id |

Excluded items stay live in the course body but are hard-excluded from gate instruments.
The uniform gate (2026-07-06, fresh pulls, gpt-4.1): every certified item blind-probed on its own
id under the same solver on the same day — sequence/match partial scores at the ~0.30 per-item
chance floor, choice at the 2-of-2 blind-vote bar; 63 items (58 Unit-1 +
3 hot-text + 2 choice) moved out of the certified set.

**Feedback.** 772/772 item-specific CORRECT/INCORRECT modal feedback, closed course-wide,
read-back verified, and maintained through every redesign via carry-over + re-author.

**Events (NN8).** 60 platform-emitted Caliper TimeSpentEvents for this course read back from the
events store (2026-07-06). Assessment-event evidence is an open platform-side item.

**Evidence.** The headline evidence a reviewer needs — the uniform gate method and result, the
final probe statistics, the conversion-lane yields, the same-day incumbent census, the mastery
and review instrument composition, the feedback and standards state, and the pre-submission
audit roll-up — travels in **`references/evidence-summary.md`**, each figure tagged
"measured 2026-07-06" or "recomputable live". The dated raw evidence chain (per-wave gate
outputs, deploy snapshots, probe JSONs) is archived in the source repo's `analysis/` tree —
access optional: every certification verdict is re-derivable from the live course via §6.3 on
the per-item IDs in `references/item-ledger.json`.

Sequence/match wave yields: 15 + 21 + 15 + 73 + 64 + 12 = 200 gross, 197 net under the final gate,
pool exhausted. Choice lane: 20/27 + 122/207 = 142/234 converted, 140 certified. Hot-text lane:
90/117 certified.

## 5. How it was built — the regen loop as a repeatable method

The loop that produced the Unit-2 certifications, generalized:

1. **Agents emit structured text-edits, not XML.** Each item's redesign is a JSON edit record
   keyed to the original element identifiers (stem text, per-affordance text, key). Element IDs
   are never changed — only inner text and the key.
2. **Deterministic rebuild + validate.** A library (`scripts/g5_regen_lib.py`) applies the edits
   to the original rawXml by identifier and validates structure preservation: same interaction
   type, same affordance-ID set, key is a valid reference/permutation, no empty texts, and (for
   sequence) no ordinal self-labels ("first", "then", "finally"…) in option text. A
   `key_evidence` field must be a verbatim passage substring — the correctness anchor.
3. **Cross-family gate.** Blind solve MUST fail; with-passage solve MUST succeed. Solver =
   TrueFoundry gpt-4.1 (OpenAI family; generator was Claude family). Sequence/match use the
   probe's exact/partial scoring (keep = blind exact 0 and partial < 0.6; with-passage exact 1
   or partial ≥ 0.8). Choice uses 2 blind votes, both must fail, plus a with-passage pass.
4. **Deploy with rollback.** Snapshot the current live XML of every keeper BEFORE the PUT
   (`originals_snapshot.json`), then PUT, then **read back and parse the live XML** to confirm
   the intended key landed. Every deploy is reversible by PUTting the snapshot.
5. **Live re-probe.** Pull the deployed items fresh (never from cache), rebuild the blind
   bundle from live XML, run the gate again. Items that recover on repeat probes get one
   decisive redesign attempt; if that fails the gate, decertify.
6. **Feedback carry-over.** Regen deploys carry existing modal-feedback blocks into the rebuilt
   XML; when the redesign changes what the item asks, re-author the feedback (the old text
   explains the old item).

**Winning item designs per format** (what actually passed the gate):

- **Sequence:** order-of-mention — "in the order the article presents them," where the order is
  arbitrary relative to world knowledge. Causal/chronological orders a solver can reconstruct
  from priors are the exhaustion mode (the 38 replacement candidates are mostly irreducibly causal).
- **Match:** arbitrary-structural-fact pairing — details matched to categories where the pairing
  is a fact of this passage, not of the world.
- **Choice:** signal-word identification, exact-wording ("which phrase does the author use"),
  not-stated/which-source discrimination — designs where the option set is undecidable without
  the text.
- **Hot-text:** claims-about-the-passage (select the claim the passage supports) instead of
  select-the-sentence — the shipped lane: 90/117 converted and certified. Native hot-text is
  construct-incompatible with the blind protocol (the selectable tokens ARE the passage), which
  is why the 27 unconverted items sit excluded.

## 6. Operations

Everything below is copy-runnable given credentials. Secret VALUES never appear anywhere —
env names only. All scripts live in `scripts/` next to this file.

### 6.1 Auth + API surface

```
TIMEBACK_SSO_CLIENT_ID      # Cognito M2M client-credentials pair
TIMEBACK_SSO_CLIENT_SECRET
TIMEBACK_SSO_ISSUER_URL     # Cognito issuer (token endpoint derives from it)
```

The client is **`scripts/timeback_client.py`** — bundled, stdlib-only, self-contained. It
exposes `mint_token()` (client-credentials POST against Cognito; also accepts
`TIMEBACK_CLIENT_ID`/`TIMEBACK_CLIENT_SECRET`; token URL overridable via `TIMEBACK_TOKEN_URL`
or derivable from `TIMEBACK_SSO_ISSUER_URL`), `get_json(url, tok)`, `post_json(url, body, tok,
method=...)`, and the base constants. (The origin machine's `push_to_timeback.py` from the
alpha-read-packager repo exposes the same `mint_token`/`get_json`/`QTI` surface; the bundled
scripts use it when present and fall back to `timeback_client` otherwise — no repo needed.)

```
QTI = https://qti.alpha-1edtech.ai/api                      (TIMEBACK_QTI_BASE)
OR  = https://api.alpha-1edtech.ai/ims/oneroster            (TIMEBACK_OR_BASE)
Caliper = https://caliper.alpha-1edtech.ai/caliper/events
```

Never print token or secret values. Set the env vars in your shell (on the origin machine they
load from a gitignored `.env`; `build_blind_bundle.py` auto-loads that file only if it exists).

### 6.2 Read anything

```
GET {QTI}/assessment-items/{id}      -> {"rawXml": ...}    # the item, as rendered
GET {QTI}/stimuli/{id}                                     # the passage
GET {QTI}/assessment-tests/{id}                            # test structure
GET {OR}/rostering/v1p2/courses/components?filter=...      # course/unit/lesson tree
GET {OR}/rostering/v1p2/courses/component-resources/{id}
GET {OR}/gradebook/v1p2/assessmentLineItems/{id}
GET {OR}/resources/v1p2/resources/{id}
```

Two rules that save hours:

- **Updates are PUT, not POST.** The QTI API honors `PUT /assessment-items/{id}` and
  `PUT /stimuli/{id}` with body `{"format":"xml","xml":"..."}`. POST to an existing id returns
  409 (`timeback_client.post_json(..., method="PUT")` covers the update path). Always
  GET-read-back after a PUT to confirm the land.
- **`masteryThreshold` lives on component / assessmentLineItem metadata, NOT test metadata.**
  A `None` on the test object is not a missing gate — check the component layer before
  concluding anything about gating.

### 6.3 Run the blind gate (probe an item set)

```bash
# 1. Build a blind bundle from FRESH live pulls (seq/match/hot-text auto-detected from XML):
python3 scripts/build_blind_bundle.py ids.json bundle.jsonl

# 2. Run the cross-family solver (needs TFY_API_KEY + TFY_BASE_URL in env):
python3 scripts/run_probe_tfy.py --bundle bundle.jsonl --out blind_out.json --threads 8
python3 scripts/run_probe_tfy.py --bundle wp_bundle.jsonl --out wp_out.json --with-passage

# 3. Read the summary: per-item exact + partial scores in the --out json.
```

`run_probe_tfy.py` wraps `blind_solve_probe.py`, bundled alongside it in `scripts/` (the probe
scorer travels with the skill) — overriding its model to **gpt-4.1**, the only authorized solver,
chosen because it is genuinely cross-family from the Claude generator. Endpoint =
`TFY_BASE_URL` + `/openai/chat/completions`. The cross-family requirement is load-bearing:
solver family ≠ generator family, always. Choice items do not go through this probe — they use
`choice_gate_deploy.py`'s 2-vote solve (stage `classify`), which calls the TFY gateway directly
and is fully self-contained; without the solver file you can still gate choice items, read
everything, and deploy — only the seq/match/hot-text exact/partial scorer needs it.

### 6.4 Regen a batch

**Chunk-file pattern.** Split the input rows into chunk files of ~7 items and have parallel
authoring agents read their chunk **via the Read tool** — loading data through bash subprocesses
stalls parallel agents. Each agent emits an edits array; concatenate into `edits.json`.

**Edit schema.** Sequence/match:
`{item_id, type, stem, aff:{id:text}, categories:{id:label}, key_order:[ids] | key_match:{srcId:catId}, key_evidence}`.
Choice: `{item_id, stem, aff:{id:text}, key_choice:[ids], key_evidence}`.
`key_evidence` must be a verbatim passage substring (the rebuild stage rejects otherwise).

**Sequence/match lane** (`scripts/seqmatch_gate_deploy.py`):

```bash
# expects /tmp/g5_regen_input.jsonl (probe rows + "stimulus" passage text per item)
python3 scripts/seqmatch_gate_deploy.py rebuild edits.json    # -> /tmp/g5_regen_work/{rebuilt.json, blind_bundle.jsonl, wp_bundle.jsonl, rejects.json}
python3 scripts/run_probe_tfy.py --bundle /tmp/g5_regen_work/blind_bundle.jsonl --out blind.json
python3 scripts/run_probe_tfy.py --bundle /tmp/g5_regen_work/wp_bundle.jsonl --out wp.json --with-passage
python3 scripts/seqmatch_gate_deploy.py classify blind.json wp.json   # -> keepers.json + classify_report.json
python3 scripts/seqmatch_gate_deploy.py deploy                # snapshots originals_snapshot.json, PUTs, read-back verifies
python3 scripts/seqmatch_gate_deploy.py remeasure             # fresh live pull -> deployed_blind_bundle.jsonl for the final probe
```

**Choice lane** (`scripts/choice_gate_deploy.py`):

```bash
# expects /tmp/g5_choice_pilot_input.jsonl + TFY_API_KEY/TFY_BASE_URL
python3 scripts/choice_gate_deploy.py rebuild edits.json
python3 scripts/choice_gate_deploy.py classify    # runs the 2-blind-votes + with-passage gate inline
python3 scripts/choice_gate_deploy.py deploy      # snapshots CURRENT LIVE xml, carries modal feedback into the rebuilt xml, PUTs, read-back verifies
```

**Rollback.** Every deploy stage writes `originals_snapshot.json` first (past runs' snapshots
are archived in the source repo — access optional; new runs write their own). To roll back, PUT
the snapshot XML per item and read back.

### 6.5 Feedback

```bash
python3 scripts/fb_scan.py                                    # pulls all Unit-2 items live -> /tmp/g5_u2_live_items.json + /tmp/g5_u2_fb_scan.json (generic = text shared by >=5 items or empty)
python3 scripts/build_fb_input.py ids.json out_prefix         # -> out_prefix_input.json + out_prefix_chunks/chunk_NN.json (8 items/chunk; stem+options+key+passage per item)
# ...parallel agents author {item_id, feedback_correct, feedback_incorrect} per chunk...
python3 scripts/fb_deploy.py authored.json workdir [--dry-run]  # replaces-or-inserts CORRECT/INCORRECT modal blocks; snapshots pre-PUT XML; read-back verifies text-in-live-XML
```

Authoring style: item-specific both ways. CORRECT text states why the keyed answer is right,
anchored to the passage evidence; INCORRECT text redirects to where/how in the passage to find
it. Regen deploys carry feedback over; when a redesign changes the question, re-author.

**Verification standard:** authored-text-present-in-live-XML plus a scoring-discrimination
sample — never the `process-response` envelope, which returns a generic payload for every item.

### 6.6 Enroll a reviewer

Reviewer access is a **student-role enrollment** in the course class
`g5-reading-merged-pp-9802-class` — the PowerPath flow is a student-seat experience, so an
unenrolled account may see a blank or absent course (§2). One enrollment = three calls through
`scripts/timeback_client.py`:

```python
import urllib.parse
from timeback_client import mint_token, get_json, post_json, OR
tok, _ = mint_token()

# 1. Resolve the user by email filter
st, users = get_json(OR + "/rostering/v1p2/users?filter=" +
                     urllib.parse.quote("email='reviewer@alpha.school'"), tok)
uid = users["users"][0]["sourcedId"]

# 2. POST the enrollment (role=student) into the course class
st, resp = post_json(OR + "/rostering/v1p2/enrollments", {"enrollment": {
    "role": "student", "user": {"sourcedId": uid},
    "class": {"sourcedId": "g5-reading-merged-pp-9802-class"}}}, tok)

# 3. Read back — the verification is the student list, not the POST status
st, back = get_json(OR + "/rostering/v1p2/classes/g5-reading-merged-pp-9802-class/students", tok)
```

Read-back is the standard here as everywhere (§6.2): confirm the account appears in the class's
student list before telling anyone they're in.

### 6.7 Caliper

```
GET https://caliper.alpha-1edtech.ai/caliper/events     (same bearer token)
```

The server ignores filter query params — pull and **filter client-side** (by course/component
IRI substrings). Evidence of working reads: 60 TimeSpentEvents, measured 2026-07-06
(`references/evidence-summary.md` §6); recomputable live with the same bearer token.

### 6.8 The scripts, exactly

Nine scripts, all stdlib-only, all importing only from their own directory plus (optionally)
the origin machine's packager repo. **The API-auth dependency is solved in-folder:** every
script that needs the platform tries the packager helper first and falls back to the bundled
`timeback_client.py` — on a fresh machine with only env creds, everything below runs except the
one noted external (the seq/match probe solver).

| Script | Does | Paths / notes |
|---|---|---|
| `timeback_client.py` | **Bundled API client** — `mint_token()` (Cognito client-credentials), `get_json`, `post_json` (PUT for updates), QTI/OneRoster/Caliper base constants. No dependencies, no baked paths | Env per §6.1; token URL overridable (`TIMEBACK_TOKEN_URL` / derived from `TIMEBACK_SSO_ISSUER_URL`) |
| `g5_regen_lib.py` | Library: parse QTI rawXml → probe row (`parse_xml` for hot-text/sequence/match, `parse_choice`); structure-preserving `validate`/`validate_choice`; deterministic `rebuild`/`rebuild_choice` (edits by element id); `load_item`/`passage_of` from a local readback mirror | `RB_ITEMS`/`RB_STIM` (lines 9–10) → origin-machine readback mirror of the 772 items — ADAPT or recreate with live GETs (`GET {QTI}/assessment-items/{id}` / `/stimuli/{id}-s`); only `load_item`/`passage_of` touch it |
| `run_probe_tfy.py` | Runs the blind/with-passage probe through TFY gpt-4.1; forwards `--bundle/--out/--with-passage/--threads` | Uses the co-located `blind_solve_probe.py` (bundled). Env: `TFY_API_KEY`, `TFY_BASE_URL` |
| `build_blind_bundle.py` | Fresh live pull of an ID list → typed probe rows → `bundle.jsonl` (seq/match/hot-text) | Falls back to `timeback_client`; `ENV` line 8 auto-loads a local `.env` only if present |
| `seqmatch_gate_deploy.py` | 4-stage regen driver: rebuild / classify / deploy / remeasure (see 6.4) | Falls back to `timeback_client`; `WORK=/tmp/g5_regen_work`; `INPUT=/tmp/g5_regen_input.jsonl` (module-level, must exist even for later stages) |
| `choice_gate_deploy.py` | 3-stage choice driver with inline 2-vote gate and feedback-carrying deploy — fully self-contained gate | Falls back to `timeback_client`; `WORK=/tmp/g5_choice_pilot_work`; `INPUT=/tmp/g5_choice_pilot_input.jsonl`. Env: `TFY_API_KEY`, `TFY_BASE_URL` |
| `fb_scan.py` | Live feedback census of Unit-2 (see 6.5) | Falls back to `timeback_client`; `MANIFEST` falls back to `references/item-ledger.json`; writes `/tmp/g5_u2_live_items.json`, `/tmp/g5_u2_fb_scan.json` |
| `build_fb_input.py` | Builds feedback-authoring records + chunk files for an ID list | Reads `/tmp/g5_u2_live_items.json` (run `fb_scan.py` first); `RB_STIM` line 11 → readback stimuli mirror — ADAPT or recreate with live GETs |
| `fb_deploy.py` | Injects authored feedback into FRESH live XML, PUT + read-back (see 6.5) | Falls back to `timeback_client` |

Input JSONL rows for the gate drivers are probe rows plus a `passage` (choice) or `stimulus`
(seq/match) field — i.e. the output shape of `build_blind_bundle.py` with the passage text
attached per item. Build them fresh from live pulls; never reuse a cached bundle.

### 6.9 Gotchas (consolidated, each one cost real time)

- **PUT, not POST, for updates.** POST to an existing QTI ID returns 409; the repo helpers are
  create-only. PUT + GET-read-back is the update path.
- **Parallel agents load data via the Read tool.** Passing data through bash subprocesses
  (`$(cat ...)` into prompts) stalls parallel agents; chunk files + Read work.
- **Copied drivers inherit stale paths.** A sed-copied driver keeps the old `WORK`/`INPUT`
  constants — grep both immediately after any copy.
- **match/hot-text `process-response` payloads are arrays of `"id cat"` strings** (directed
  pairs), not objects.
- **Workflow/tool args must be real JSON**, not a `$(cat file)` string interpolation.
- **Detect multi-interaction (EBSR) items by counting OPENING tags** (`<qti-choice-interaction`),
  not all tag occurrences — closers double the count.
- **`masteryThreshold` is on the component/assessmentLineItem, not the test** (6.2).
- **The `process-response` envelope is generic** — it proves scoring, never feedback content;
  verify feedback in the live XML (6.5).
- **Probe fresh, not cached.** Certification and re-probes always rebuild bundles from live
  GETs; a cached bundle can certify XML that is no longer deployed.

## 7. Review context

**Frame first.** Under the CoE two-course split (2026-06-30), this is the **MAPS-practice
course**; a separate core course owns teaching. The G3 reviewer's own verdict hinged on that
frame ("a well-built, MAP-styled practice-and-assessment engine… If it is decided that this
should be a MAP practice app, the recommendations below would be different"), and the reviewer's
adoption path (D12) is: adopt it as MAP format-familiarisation and cold-reading practice, paired
with named instruction — the pairing source is the core-teaching course of the split.

**The demands register** (from the G3 review, applied to G5; summarized in full here — the
source register lives in the source repo, access optional):

- **Three frame-independent review items:** **D9** — the mastery gate must demonstrably
  block a real miss in a live walkthrough (the G3 exploit: a ~20% click-through earned a stamp);
  **D10** — accessibility: keyboard/AT operability on every interaction type, renderer-reviewed
  (renderer review in progress with the platform team; 525/772 items sit on non-choice types);
  **D11** — counts reconciliation: one dated pull, every artifact quoting identical numbers.
- **Survive the practice frame (STAAR-justified):** **D6** stamina — passage-length distribution,
  ramp toward test length, paired-text sets; **D7** short written responses replacing some
  single-select; **D8** format rebalance + tag spot-audit with an error rate.
- **D1–D5** (gradual release, taught lenses, knowledge sequencing, genre balance, explain-your-
  thinking) spec the core-teaching course, not this one — though D1's floor (corrective feedback
  explaining why right/wrong) is met here, 772/772.

**The case in three sentences.** The incumbent's test of record is selected-response with no
anti-leak validation, and on this bank that format is 99.5–100% blind-solvable — a reading test
a student can pass without reading. This course ships a 541-item instrument in which every item
was individually certified by a cross-family blind gate (blind must-fail, with-passage
must-succeed) under one uniform same-day measurement — every certified item probed on its own
id. Approving it approves a construct, a content layer, and a
measurement instrument; outcome measurement starts when the MAP crosswalk lands.

**Every number is recomputable live:** the ledger is per-ID (`references/item-ledger.json`),
the course is readable via section 6.2, the probes re-run via 6.3, and the evidence figures are
dated per measurement (`references/evidence-summary.md`). An evaluator who distrusts a figure
should re-pull it.

## 8. Scope — current open items

| Item | State | Owner |
|---|---|---|
| ELA content review on the 541 certified | Draft staged 2026-07-06, pending approver review; send pending | Course team |
| MAP student-ID crosswalk | The pilot's one external input — links our readers to the 409 MAP records already in OneRoster; one-pager staged | Course team sends; roster owner executes |
| Accessibility renderer review | 525/772 non-choice items in scope; in progress with the platform team | TimeBack renderer team |
| 107 choice excluded (85 + 20 EBSR + 2 probe) | Harder-design pass or replacement | Course team |
| 39 seq/match excluded | Replacement candidates (generation), not rewrite | Course team |
| 27 hot-text + 58 Unit-1 excluded | Redesign further or replace | Course team |
| Credential rotation (Cognito M2M pair + TFY key) | Both transited transcripts | Course team |
| Caliper assessment events | Activity events observed (60); assessment-event scope platform-side | Platform |
| Formal submission | Prepared; G4/G5 submission paused until G3 clears its gate (CoE 2026-07-02) | Org |

## 9. Source map

**Live (the primary source — everything below is recomputable from it):**

- Course: https://alpha.timeback.com/app/course/g5-reading-merged-pp-9802
- QTI API: https://qti.alpha-1edtech.ai/api · OneRoster: https://api.alpha-1edtech.ai/ims/oneroster · Caliper: https://caliper.alpha-1edtech.ai/caliper/events

**In this folder — `references/` (Claude loads these on demand via Read):**

| File | Contents |
|---|---|
| `references/item-ledger.json` | The full per-item disposition: 541 certified / 231 excluded (58 U1 + 107 choice + 39 seq/match + 27 hot-text) / 0 unknown, every ID listed, captured 2026-07-06 |
| `references/live-pull-summary.json` | The dated counts-provenance record: the 2026-07-06 GET read-back (98 components / 94 lessons / 94 tests / 772 unique items, `ledger_matches_pull: true`) |
| `references/evidence-summary.md` | The headline evidence with numbers: uniform gate method + result, final probe stats, conversion lanes, incumbent census, mastery/review composition, feedback + standards state, audit roll-up (26 rows / 2 open) |
| `references/case-for-approval.md` | The decision memo: the ask + rubric scorecard (PASS, 0 blocking) |
| `references/brainlift.md` | The full design BrainLift v0.6 (SPOVs, MAP-G5 format/scoring logic, locked decisions, dropped approaches, cross-grade parity ledger) |
| `references/cover-email.md` | The staged approval cover email (draft) |

**In this folder — `scripts/`:** the nine operational tools (§6.8), including the
self-contained `timeback_client.py`.

**Source repo (`trilogy-group/ti-courseplans` → `courses/g5-reading/`) — access optional.**
Holds the archival layer this folder was cut from: the dated raw evidence chain (`analysis/`),
the KC graph, the submission pack, the compliance ledger, and the original `.qmd` sources of the
`references/` documents. Nothing operational depends on it.

**Off-repo (origin machine) — optional conveniences:** the alpha-read-packager repo
(`push_to_timeback.py` — superseded here by `timeback_client.py`; `blind_solve_probe.py` — now bundled in `scripts/`; the
one file §6.3 needs for seq/match probes; `audit_compliance.py` — the read-only certifier) and
a local 772-item readback mirror (`items/*.xml`, `stimuli/*.xml`) that `g5_regen_lib`'s
`load_item`/`passage_of` read — recreate with live GETs if absent.
