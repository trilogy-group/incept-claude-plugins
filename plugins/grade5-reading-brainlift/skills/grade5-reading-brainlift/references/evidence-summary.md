# Evidence summary — g5-reading-merged-pp-9802

The headline figures a reviewer needs, in one place. Every figure is tagged either
**[measured 2026-07-06]** (a dated read-only measurement) or **[recomputable live]** (re-derivable
from the live APIs with the auth + read surface in SKILL.md §6 and the per-item IDs in
`item-ledger.json`). The two tags overlap by design: everything measured on 2026-07-06 was measured
*from* the live APIs and can be re-pulled.

## 1. The anti-leak gate — method and result

**Method.** Anti-leak certification thresholds a cross-family solver's MEAN blind-solve over
resampled shuffles at < 0.60 — an item is certified only if it cannot be reliably answered without
the passage. The 358 hot-text/sequence/match items are cross-family blind-probed on their own ids
(non-generator solver: TrueFoundry **gpt-4.1**, OpenAI family; generator: Claude family); the 188
choice + 3 EBSR are certified on a same-family two-vote lane. The 223 excluded sit outside every
gate instrument. Every certified candidate was blind-probed on its own id from fresh live pulls —
no certification carried from any earlier run.

**Result** [measured 2026-07-06; per-item IDs in `item-ledger.json`; recomputable live via §6.3]:
**549 of 772 items clear the gate.** Every gating test serves 15 certified items. Certified composition:
103 Unit-1 + 446 Unit-2 (148 sequence/match + 188 choice + 107 hot-text + 3 EBSR); by id-label
lane, 143 match + 83 sequence + 132 hot-text + 188 choice (88 MCQ + 100 MSQ) + 3 EBSR. **Coverage
split:** the cross-family blind probe certifies the hot-text/sequence/match core (358 items); the
188 choice + 3 EBSR were certified via the same-family gpt-4.1 2-vote choice lane — read "549
certified" as 358 cross-family + 191 same-family, not one uniform gate over all 549. Convention,
used throughout this document: compositions use id-label lanes; 34 items render as a different
interaction than their id suffix (per-item map in `item-ledger.json`), so rendered totals differ
— Unit-2 seq/match 151 and choice 180 as rendered. EBSR: 3 certified and serving in their gating
tests; the other 12 EBSR by id-label are excluded. Ledger:
**549 certified / 223 excluded / 0 unknown** — every one of the 772 items carries a measured
disposition.

## 2. Final probe statistics (the 462-item bundle, gpt-4.1)

Per-type blind-solve results on the probed set, *before* the 61 recoveries were excluded
[measured 2026-07-06]:

| Type | n | Exact recovery | Mean partial score | Per-item chance floor |
|---|---:|---:|---:|---:|
| hot-text | 136 | 22.1% | 0.37 (Jaccard) | 0.084 |
| sequence | 136 | 2.9% | 0.481 (pair acc.) | 0.022 |
| match | 190 | 14.2% | 0.444 (frac. correct) | 0.299 |

Certified survivors have exact recovery 0 by construction; their partial scores sit at the
per-item chance floor. Context baselines [measured, dated]: as-authored format leak MCQ 99.5% /
MSQ 100% / hot-text 1.67% / sequence 0% / match 0% (cross-family runs 2026-06-23/24); the
uncertified anti-leak-format pool leaked **~78% weighted** on its own ids (353-item historical baseline, gpt-4.1, 2026-07-02 — 77.8 / 76.0 / 79.5 by type). Format is necessary, not
sufficient; certification is per-item.

## 3. Conversion lanes — the leaky formats convert

[measured 2026-07-06; certified survivors recomputable live via §6.3]

- **Choice (MCQ/MSQ):** per-item rewrite into passage-dependence at a 2-of-2 blind-vote bar —
 pilot 20/27, scale pass 122/207 = **142/234 converted (61%)** at lane time; **188 certified by
 id-label** under the gate (180 as rendered). This overturns the earlier "leaky formats need full
 regen" reading.
- **Hot-text:** construct redesign (claims-about-the-passage instead of select-the-sentence) —
 90/117 converted at lane time; **107 Unit-2 hot-text certified by id-label** under the current
 gate. Native hot-text is construct-incompatible with the blind protocol (the selectable
 tokens are the passage); the unconverted items sit excluded.
- **Sequence/match:** regen wave-rounds to pool exhaustion — 15+21+15+73+64+12 = 200 gross;
 **148 Unit-2 seq/match certified by id-label** under the gate (151 as rendered); the excluded
 seq/match pool is mostly irreducibly causal content (replacement candidates, not rewrite targets).

## 4. Incumbent census — same-day, same-method structural pull

All five live G5 reading courses GET-pulled and censused 2026-07-06 (full per-item pulls; raw
pulls archived in the source repo). Two enumeration findings: "Reading G5 Full Course -
100 for 100" is a re-mint of the retiring CK5 bank (identical 8 units / 109 articles / 812-item
census, difficulty 156/360/296; only article ids re-minted), and "Alpha Read G5" (`de0dbcf7`) is
an external-launch shell with 0 API-native items — the real Alpha Read incumbent is `8cf5f85e`.

| Dimension | Alpha Read - Grade 5 (`8cf5f85e`) | Reading G5 100-for-100 (= CK5 bank) | Ours |
|---|---:|---:|---:|
| Items (API-native, unique) | 1,343 | 812 | 772 |
| Interaction formats | **1** — single-select 1,343/1,343 (`max-choices="1"`) | **1** — single-select 812/812 | **6 rendered** (match 198, hot-text 160, sequence 167, MCQ 116, MSQ 111, EBSR 20) |
| `masteryThreshold` encoded | **0** | **0** | 90 on every gating resource (81 gating tests) |
| Standards alignment | **0**/1,343 | 812/812 (bare CASE GUIDs, 15 codes) | 772/772 (official CASE GUIDs) |
| Item ↔ passage binding | 767/1,343 — all 576 Quiz items unbound | 342/812 — all 470 Quiz items unbound | 772/772 |
| Per-item feedback | 1,343/1,343 (per-choice inline) | 812/812 | 772/772 (modal CORRECT/INCORRECT) |
| Blind-solve (anti-leak) measurement | none | none | every item measured; 549 certified |
| Spaced-review / parallel-form instruments | none / none | none / none | 8 review lessons / 5 parallel forms (form-to-form disjoint) |
| Component hygiene | 69 of 103 components `tobedeleted` | 8/8 active | all active |

Where the incumbents win, stated once: Alpha Read is ahead on instructional spine (144 authored
articles — this course is deliberately the practice/measurement layer of the CoE two-course
split and makes no instruction-coverage claim); RG5-100/CK5 is ahead on difficulty tags
(812/812 vs 0/772). Untimed, standards rate, and full feedback coverage are
parity; no parallel forms is a shared gap on the incumbent side.
Incumbent figures [measured 2026-07-06]; our column reflects the final same-day ledger + pull
(the census's ours-snapshot was taken hours before the final probe and mastery-unit deploy;
`live-pull-summary.json` is the reconciled record). External-outcome (MAP RIT) linkage awaits a
roster-owned student-ID crosswalk

## 5. Mastery forms + review unit

[measured 2026-07-06 from `tests.json` vs the final ledger; recomputable live]

- **Unit 4 "Show What You Know":** five parallel mastery forms A–E, **24 items each, 120
 distinct refs, disjoint from each other (form-to-form), all certified**, format quotas
 proportional to the certified pool. Non-gating. Mastery and review items also serve in
 gating tests.
- **Review unit (NN6):** 8 spaced-review lessons (Leitner spans + starred revisits), 81 distinct
 items, all certified. Non-gating.
- A post-probe sweep replaced **29 refs** across the supplementary tests so both units reference
 certified items only.
- 94 tests total = 81 gating (`masteryThreshold==90`, engine-enforced) + 8 review + 5 mastery.
 Gating tests enforce the ≥90% mastery threshold on 15 certified items each (14/15 = 93.3%,
 one miss tolerated).
- Item reuse, by design: **gating refs across 81 tests (15 certified items each) over 549 unique
 certified items** — some items serve in more than one gating test (max 3; zero cross-unit), so a
 share of gating slots are same-unit borrows of previously-read passages — spaced retrieval on the
 same pattern as the review/mastery units. Every gating slot holds a certified item
 (0 excluded serving).

## 6. Feedback + standards state

- **Feedback: 772/772** item-specific CORRECT/INCORRECT modal feedback, read-back verified,
 post-scan 0 remaining, scoring discrimination sampled 20/20; maintained through every redesign
 via carry-over + re-author [measured 2026-07-06; recomputable live via §6.5's `fb_scan.py`].
- **Standards: 772/772** carry CCSS codes resolved to official CASE GUIDs (CCSSO framework,
 same GUID family as the platform registry), read-back verified; the standards writes were
 metadata-only with rawXml read back byte-identical [measured 2026-07-06 — final coverage
 record + live spot-checks; recomputable live].
- **Scoring: behaviorally proven 772/772** — a full sweep confirmed every item pays full credit
 only for the declared-correct response; the 30/30 live discrimination probe is the historical
 spot-check (recent re-verification 6/6); every type HTTP 200 on `process-response`
 [recomputable live].
- **Caliper (NN8):** activity events verified in the Caliper store — 60 platform-emitted
 TimeSpentEvents read back [measured 2026-07-06]; assessment-event scope is platform-owned.

## 7. Pre-submission adversarial audit — roll-up

An adversarial self-audit ran 2026-07-06 over the whole reviewer-facing package: Audit 1
recomputed every load-bearing number from its raw artifact; Audit 2 checked every named external
fact against its cited source, resolved every link, and screened the voice.

**26 rows: 5 verified clean at the source, 13 fixed, 6 accepted, 2 open.** The two open items:

1. **EBSR historical-run metadata mismatch** — one doc says "0% on one 15-item run (2026-06-23)",
 another says 60 items (2026-06-24); neither raw run is archived. The certification standing
 is unaffected and consistent (§1's EBSR line): 3 EBSR are certified and serving; the other 12
 by id-label are excluded.
2. **The D9 red-team walkthrough** (click-through must not stamp, rapid-guess, passage-hide,
 keyboard-only) is pending; awaits credential rotation.

Everything that traced clean on the final pass includes: the 98/94/94 component-lesson-test
counts, the 772 unique items, the rendered composition, the 549/223/0 ledger with per-bucket
decomposition, the lane yields, the anti-leak gate, feedback 772/772,
the form-to-form-disjoint mastery forms, the 29-ref sweep, the Caliper 60, standards 772/772,
the a11y scope 525/772, the ~78% baseline, and the incumbent census figures above.
