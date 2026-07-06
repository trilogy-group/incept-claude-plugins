# Item Bank Documentation — MAP Proxy Adaptive Assessment
**Version:** 2.0 | **Date:** 2026-07-03 | **Audience:** Content reviewers, technical reviewers

---

## 1. Bank Overview

The operational item bank contains **650 unique items** across grades 2–5 (provisional b spans −2.5 to +2.0 logits ≈ RIT 175–220; band labels run 161–220). Staged expansions bring the harness-loadable total to **786 items** spanning ≈ RIT 155–250 (the `load_bank()` build dedups to 786 unique items, which differs from the naive fixture sum; see §2.1) — and this full 786-item bank is what the authoritative v4 validation (2026-07-03) ran against. All items carry provisional difficulty parameters (b_provisional) assigned by content experts. No item has been empirically calibrated; empirical calibration requires a field trial of N ≥ 1,000 students [Wright-Stone-1979][Linacre-1994].

Pool-to-test ratio, stated in both framings so the two numbers that circulate are reconciled rather than contradictory [Stocking-1994]:
- **Session-length framing:** 650 / 40 = **16.3× session length** (the framing used when comparing against a fixed form).
- **Stocking-floor framing:** against the *recommended* 10× floor of 10 × 40 = 400 items, the bank is **1.6× the recommended floor** (minimum 6× floor = 240 items; 2.7×).
- Staged expansions raise the pool further (786 harness-loadable).
- NWEA's operational pool: 40,000+ items [NWEA-2025-TR]. Bank: 650 items (**1.6% of NWEA scale**).

Wherever a pool ratio is quoted elsewhere in this package (the Case for Approval tab §6, the package README, the Validity Case tab §3.2), it uses these two labeled framings.

---

## 2. Bank Composition by Source File

| File | Items | Grades | RIT band labels | b_provisional basis |
|---|---|---|---|---|
| `items.json` (original G3) | 38 | G3 | 181–210 | Expert-assigned from target band |
| `bank_forms.json` (Form A/B) | 80 | G3 | 181–210 | Expert-assigned from target band |
| `bank_g2.json` | 52 | G2 | 161–180 | Expert-assigned from target band |
| `bank_g3_expansion.json` | 18 | G3 | 181–210 | Expert-assigned from target band |
| `bank_g4.json` | 62 | G4 | 191–210 | Expert-assigned from target band |
| `bank_g5.json` | 150 | G5 | 201–220 | Expert-assigned; G5 items from quality-check-certified JSONL |
| `bank_gap_fixes.json` | 118 | G2–G5 | 161–220 | Expert-assigned (gap remediation, June 2026) |
| `bank_match.json` | 56 | G2–G5 | 191–220 | API-generated (G3–G4 vocab) + quality-check-certified JSONL (G5 RI/RL) |
| `bank_g2_match.json` | 16 | G2 | 161–180 | Expert-assigned from target band |
| `bank_g3_match.json` | 4 | G3 | 191–200 | Expert-assigned from target band |
| `bank_g2_sequence.json` | 16 | G2 | 161–180 | Expert-assigned from target band |
| `bank_g4_sequence.json` | 20 | G4 | 201–210 | Expert-assigned from target band |
| `bank_ebsr_191_200.json` | 20 | G3–G4 | 191–200 | Expert-assigned from target band |
| **Total** | **650** | **G2–G5** | **161–220** | **All provisional** |

Provisional b values across the bank span −2.5 to +2.0 logits ≈ **RIT 175–220**; the 161–220 figures above are authoring band labels, not measured difficulty.

### 2.1 Staged expansions (merged, harness-loadable; production adoption pending)

Two expansion sets are merged and load in the validation harness; adopting them into the production bank is a reviewable decision, pending calibration planning:

| Set | Items | Coverage | Status |
|---|---|---|---|
| Edge expansion (PR #30) | +92 | Floor extension to ~RIT 155; ceiling to 235 | Merged; harness-validated |
| Standard-gap + G5 super-ceiling (PR #35) | +44 (26 + 18) | 26 standard-gap items closing nine under-target standards (see §5 note); 18 G5 super-ceiling items at **RIT 231–250** (b to +4.55), directly answering the ~20%-of-current-G5-above-RIT-235 population finding | Merged, all CI green; 26/26 and 18/18 passed quality checks after re-authoring, minimum score 0.950 |
| **Harness-loadable total** | **786** (dedup via `load_bank()`) | b −4.45 → +4.55 ≈ **RIT 155–250** | Operational bank remains 650 until adoption; v4 validation ran against the full 786 |

Notes, stated plainly:
- **Sub-155 students route to the official K–2 MAP instrument.** The floor extension is honest coverage, not a claim to measure emergent decoding; below RIT 155 the proxy is the wrong tool and says so.
- The G5 L.5.x vocabulary strand is only **partially** closed (L.5.4 3→5; L.5.5 and L.5.6 0→1 each): no certified source material exists for those standards, so the new items are hand-authored and flagged as such. Two trial super-ceiling vocabulary items were held through the gate despite DOK-3 scarcity.
- A **per-standard session cap** (max 2 items per standard per session) is *proposed* in PR #35 to mitigate the over-concentrated standards in §7.2 — proposed, not shipped.

---

## 3. Format Distribution

### 3.1 Current bank

| Format | Count | % of bank |
|---|---|---|
| MCQ (Multiple Choice) | 265 | 40.8% |
| Sequence (Drag-to-Order) | 102 | 15.7% |
| MSQ (Multi-Select) | 90 | 13.8% |
| Gap-match | 76 | 11.7% |
| EBSR (Composite/Evidence-Based SR) | 63 | 9.7% |
| Hot-text (Selectable Text) | 54 | 8.3% |
| **Total** | **650** | **100%** |

### 3.2 Comparison to MAP benchmark

NWEA's Technical Report confirms MCQ, multi-select, and composite/EBSR in Reading 2–5 specifically (Figures 4.3, 4.9–4.11) [NWEA-VERIFIED]; hot-text and drag-and-drop are documented for MAP Growth in other subjects' examples, and gap-match appears only in NWEA secondary materials [SECONDARY]. The domain × format allocation targets below were authored against the pre-parity 39-item form (counts sum to 39); the parity form adds one Literary item (14/13/13 = 40 scored) and the per-form TEI floor is ≥12 with gap-match counted as TE:

| Format | Per-session target | Bank target (~10 forms equiv.) | Current bank |
|---|---|---|---|
| MCQ | 22 (56.4%) | ~220 | 265 ✅ |
| MSQ | 6 (15.4%) | ~60 | 90 ⚠️ slight over |
| EBSR | 3 (7.7%) | ~30 | 63 ✅ |
| Hot-text | 2 (5.1%) | ~20 | 54 ⚠️ over |
| Sequence | 4 (10.3%) | ~40 | 102 ✅ |
| Gap-match | 2 (5.1%) | ~20 | 76 ✅ |

The bank's MSQ and hot-text counts are above the per-form targets. This does not block delivery — the CAT enforces per-session quotas — but means these formats will be seen more frequently than intended before additional MCQ/EBSR items are added.

---

## 4. RIT Band Distribution

### 4.1 Current distribution

| RIT Band | θ range | Items | % of bank |
|---|---|---|---|
| 161–170 | −3.9 to −3.0 | 51 | 7.8% |
| 171–180 | −3.0 to −2.0 | 45 | 6.9% |
| 181–190 | −2.0 to −1.0 | 69 | 10.6% |
| 191–200 | −1.0 to 0.0 | 144 | 22.2% |
| 201–210 | 0.0 to +1.0 | 161 | 24.8% |
| 211–220 | +1.0 to +2.0 | 180 | 27.7% |

### 4.2 Recommended density vs. actual

For N=1,000 students to produce ≥200 responses per item (minimum operational calibration target [Wright-Stone-1979]), items must be concentrated where CAT exposure is highest — near the population mean:

| Band | Target density (≥200 exp/item) | Items needed | Current | Status |
|---|---|---|---|---|
| 160–170 | 15 | 5–8 | 51 | ✅ over (good for tails) |
| 170–180 | 80 | 10–15 | 45 | ✅ adequate |
| **180–190** | **190 (G3 fall core)** | **20–30** | **69** | **✅ adequate** |
| 190–200 | 200 (population center) | 20–30 | 144 | ✅ strong |
| 200–210 | 130 | 15–20 | 161 | ✅ strong |
| 210–220 | 65 | 10–15 | 180 | ✅ strong |

Note: The band 181–190 was a critical gap as of pre-June 2026 (only 20 items). Gap-fix efforts (June 2026) added 33 items, bringing the band to 69 items — now adequate for field trial [AUTHORING-DECISION; gap fix documented in the CAT Exam Spec tab, §9.3].

---

## 5. CCSS Standard Coverage Matrix

> **Superseded counts — refreshed per the PR #35 audit (786-item basis).** The
> matrix below predates the staged expansions and, per the PR #35 audit, was
> **stale even for the 650-item bank**: items added in `bank_gap_fixes.json`
> and `bank_match.json` were never counted into it (e.g., L.3.5 shows 2 below
> but the fixtures actually held 14; RI.4.1 shows 2 but held 5). PR #35 then
> closed nine under-target standards on top of the corrected counts (L.3.5
> 14→18, RI.4.1 5→9, and RI.3.5 / RI.3.8 / RL.3.4 / RI.4.4 / RL.4.4 / RI.4.2 /
> RL.4.1 to target), and partially closed the G5 L.5.x strand (L.5.4 3→5,
> L.5.5/L.5.6 0→1 each — no certified source material; hand-authored). The
> authoritative per-standard table is the **PR #35 audit table** in the engine
> repo; the matrix below is retained as the historical 2026-06-25 record and
> should not be quoted for current coverage.

### 5.1 Grade 2 (RIT 161–185)

| Standard | Description | Items | Target | Status |
|---|---|---|---|---|
| RL.2.1 | Ask/answer questions from text | 4 | 4 | ✅ |
| RL.2.2 | Theme/central message | 4 | 4 | ✅ |
| RL.2.3 | Character/setting/events | 4 | 4 | ✅ |
| RL.2.4 | Word/phrase meanings | 4 | 4 | ✅ |
| RL.2.5 | Story structure | 3 | 4 | ⚠️ |
| RL.2.6 | Point of view | 4 | 4 | ✅ |
| RI.2.1 | Ask/answer questions | 4 | 4 | ✅ |
| RI.2.2 | Main idea | 4 | 4 | ✅ |
| RI.2.3 | Connections/relationships | 4 | 4 | ✅ |
| RI.2.4 | Domain-specific vocabulary | 4 | 4 | ✅ |
| RI.2.5 | Text features | 4 | 4 | ✅ |
| RI.2.6 | Author purpose | 4 | 4 | ✅ |
| L.2.4 | Vocabulary acquisition | 3 | 4 | ⚠️ |
| L.2.5 | Word relationships | 3 | 4 | ⚠️ |
| L.2.6 | Academic vocabulary | 5 | 4 | ✅ |

### 5.2 Grade 3 (RIT 178–210)

| Standard | Description | Items | Target | Status |
|---|---|---|---|---|
| RL.3.1 | Cite text evidence | 7 | 8 | ✅ |
| RL.3.2 | Theme + evidence | 9 | 8 | ✅ |
| RL.3.3 | Character development | 28 | 8 | ❌ Over-concentrated |
| RL.3.4 | Word/phrase meaning | 4 | 6 | ⚠️ |
| RL.3.5 | Story structure/text features | 6 | 6 | ✅ |
| RL.3.6 | Point of view | 6 | 6 | ✅ |
| RI.3.1 | Evidence/explicit information | 7 | 8 | ✅ |
| RI.3.2 | Main idea | 10 | 8 | ✅ |
| RI.3.3 | Cause/effect connections | 19 | 8 | ❌ Over-concentrated |
| RI.3.4 | Domain vocab in informational text | 6 | 6 | ✅ |
| RI.3.5 | Text structure | 3 | 6 | ⚠️ |
| RI.3.6 | Author purpose | 6 | 6 | ✅ |
| RI.3.8 | Argument/evidence | 3 | 6 | ⚠️ |
| RI.3.9 | Compare two texts | 5 | 4 | ✅ |
| L.3.4 | Context clues/morphology | 31 | 10 | ❌ Over-concentrated (prefix only) |
| L.3.5 | Word relationships/figurative | 2 | 6 | ❌ |
| L.3.6 | Academic vocabulary | 4 | 4 | ✅ |

**G3 notes:** RL.3.3 (character development) and RI.3.3 (cause/effect) are over-concentrated. L.3.4 is dominated by prefix-meaning items (26 of 31 marked `deprioritize=True` in bank_forms.json). L.3.5 remains thin. These represent known content balance issues to address in bank expansion.

### 5.3 Grade 4 (RIT 190–220)

| Standard | Description | Items | Target | Status |
|---|---|---|---|---|
| RL.4.1 | Cite text evidence | 4 | 6 | ⚠️ |
| RL.4.2 | Theme/summary | 6 | 6 | ✅ |
| RL.4.3 | Character development | 4 | 6 | ⚠️ |
| RL.4.4 | Figurative language/word meaning | 4 | 6 | ⚠️ |
| RL.4.5 | Drama/poetry structure | 2 | 4 | ⚠️ |
| RL.4.6 | Point of view | 2 | 4 | ⚠️ |
| RI.4.1 | Evidence | 2 | 6 | ❌ |
| RI.4.2 | Main idea | 4 | 6 | ⚠️ |
| RI.4.3 | Explain events/concepts | 6 | 6 | ✅ |
| RI.4.4 | Domain vocab | 4 | 6 | ⚠️ |
| RI.4.5 | Text structure | 4 | 6 | ⚠️ |
| RI.4.6 | Author purpose | 2 | 4 | ⚠️ |
| RI.4.8 | Argument/evidence | 2 | 4 | ⚠️ |
| L.4.4 | Vocabulary acquisition | 6 | 6 | ✅ |
| L.4.5 | Figurative language | 6 | 6 | ✅ |
| L.4.6 | Academic vocabulary | 4 | 4 | ✅ |

**G4 notes:** RI.4.1 (evidence citing in informational) has only 2 items — the most critical G4 gap. Most standards are slightly under-represented but not at critical thresholds.

### 5.4 Grade 5 (RIT 200–220; bank ceiling b=+2.0 ≈ RIT 220)

| Standard | Description | Items | Target | Status |
|---|---|---|---|---|
| RL.5.1 | Cite evidence | 10 | 8 | ✅ |
| RL.5.2 | Theme + summary | 10 | 8 | ✅ |
| RL.5.3 | Character comparison | 10 | 8 | ✅ |
| RL.5.4 | Word/phrase meaning | 15 | 8 | ⚠️ slight over |
| RL.5.5 | Text structure/genre | 10 | 6 | ✅ |
| RL.5.6 | Point of view | 10 | 6 | ✅ |
| RI.5.1 | Evidence | 9 | 8 | ✅ |
| RI.5.2 | Main idea | 9 | 8 | ✅ |
| RI.5.3 | Explain relationships | 8 | 8 | ✅ |
| RI.5.4 | Domain vocab | 8 | 6 | ✅ |
| RI.5.5 | Text structure | 8 | 6 | ✅ |
| RI.5.6 | Author purpose | 8 | 6 | ✅ |
| RI.5.8 | Argument/evidence | 8 | 6 | ✅ |

**G5 notes:** G5 is the best-balanced grade in the bank. RI.5.4 was formerly over-concentrated at 35 items; re-tagging in June 2026 brought it to 8 items (within the 6–8 target). G5 coverage is now strong.

---

## 6. Quality Assurance: The 14-Dimension Quality Check

### 6.1 Overview

Every item in the bank has passed a 14-dimension quality check at a ≥0.85 pass threshold before entering the operational bank [AUTHORING-DECISION]. Items that fail are either revised or excluded.

### 6.2 The 14 evaluation dimensions

| Dimension | Description | Gate type |
|---|---|---|
| Dim 1: CCSS alignment | Item tests the claimed CCSS standard | Soft gate (≥0.80) |
| Dim 2: Cognitive demand | Appropriate Bloom's taxonomy level for the RIT band | Soft gate |
| Dim 3: RIT band match | Item difficulty consistent with target RIT band | Soft gate |
| Dim 4: Passage quality | Literary/informational text meets authoring spec | Soft gate |
| Dim 5: Passage Lexile | Lexile within target range for the RIT band | Soft gate |
| Dim 6: Passage word count | Length within 150–500w range (format-dependent) | Hard gate |
| Dim 7: Readability | Flesch-Kincaid Grade Level consistent with band | Soft gate |
| Dim 8: Item stem clarity | Stem is unambiguous and grammatically correct | Hard gate |
| Dim 9: Answer key defensibility | Correct answer is uniquely defensible from text | Hard gate |
| Dim 10: Text-dependence | **Ablation test:** model cannot answer without passage (≥3/5 failures) | **Hard gate** |
| Dim 11: Distractor coverage | Four distractor types present (scope, conflation, prior knowledge, partial) | Hard gate |
| Dim 12: Near-neighbor distractors | Distractors require careful reading to reject | Soft gate |
| Dim 13: Format compliance | Item structure matches format token (MCQ/MSQ/EBSR/hot-text/sequence/gap-match) | Hard gate |
| Dim 14: EBSR Part B verbatim | Part B options are verbatim passage sentences (EBSR only) | Hard gate |

**Dim 10 (text-dependence ablation) is the most critical gate.** The test: present the item without the passage to a language model (temperature 0.3, N=5 trials). If the model selects the correct answer in ≥3/5 trials, the item fails — it is answerable from background knowledge alone, not from careful reading of the specific passage. Items failing Dim 10 are invalid as MAP proxies regardless of other quality dimensions.

### 6.3 Quality-check limitations

The quality-check gate is a pre-pilot control — not a substitute for empirical validation:

- Text-dependence ablation uses a language model, which may have different knowledge than a typical G3–G5 student. Items that fail for LLMs may be valid for students (false positives) or vice versa.
- The 14-dimension evaluation cannot assess Rasch model fit, item discrimination, or guessing behavior — these require empirical response data.
- The ≥0.85 threshold is an authoring decision, not an empirically validated cutoff [AUTHORING-DECISION].

---

## 7. Known Gaps and Limitations

### 7.1 No empirical b calibration

The most fundamental gap: all b_provisional values are expert-assigned. SE(b̂) = ∞ pre-calibration. The provisional values carry an estimated uncertainty of σ ≈ 0.5–1.0 logits (5–10 RIT) [AUTHORING-DECISION; DERIVED]. This is acceptable for pre-pilot operation (Simulation 3 confirms robustness) but must be resolved before RIT output can be unlocked [Wright-Stone-1979].

### 7.2 G3 content concentration

Three G3 standards are over-represented: RL.3.3 (28 items vs. target 8), RI.3.3 (19 items vs. target 8), and L.3.4 (31 items with 26 marked deprioritized). The CAT's topic-cap constraint limits how often any single topic_tag appears per session, providing some mitigation, but the bank-level imbalance means these standards will still be slightly over-tested [AUTHORING-DECISION]. A per-standard session cap (max 2 items per standard per session) is proposed in PR #35 as the structural mitigation — proposed, not shipped.

### 7.3 G4 RI.4.1 underrepresentation — closed

Grade 4 "citing evidence in informational text" (RI.4.1) was the most critical G4 gap (the historical matrix showed 2 items; the corrected fixture count was 5). PR #35 raised it to **9 items — at target**. Retained here because the finding drove the expansion; the gap itself is closed in the 786-item staged bank.

### 7.4 PCM step parameter

The Rasch PCM step parameter Δ = 0.5 logits for EBSR items is an authoring estimate. Post-pilot calibration will reveal whether Part B is actually harder or easier than assumed [AUTHORING-DECISION].

---

## 8. Bank Expansion Plan

### 8.1 Priority queue — status after PR #30 / PR #35

| Priority | Gap | Status |
|---|---|---|
| P1 | G4 RI.4.1 (evidence citing, informational) | **Closed** — 9 items, at target (PR #35) |
| P1 | G3 L.3.5 (word relationships/figurative) | **Closed** — 18 items (corrected count 14 → 18; PR #35) |
| P1 | Both tails: floor to ~RIT 155, G5 super-ceiling RIT 231–250 | **Merged** — +92 (PR #30) and +18 (PR #35); adoption pending calibration |
| P2 | G3 RI.3.5, RI.3.8; G4 RL.4.4, RI.4.4, RI.4.2, RL.4.1, RL.3.4 | **Closed to target** (PR #35) |
| P2 | G5 L.5.5 / L.5.6 | **Partially closed** (0→1 each; no certified source material — hand-authored) |
| P3 | G2 RL.2.5 (story structure, 1 item gap) | Open |
| P3 | MCQ balance (format ratio adjustment) | Open |

### 8.2 Long-term target

| Phase | Bank target | CAT ratio (vs 40-item session) | Purpose |
|---|---|---|---|
| Current operational | 650 items | 16.3× | Pre-pilot operation |
| Staged (harness-loadable) | 786 items | 19.7× | Both-tails coverage (v4-validated), pending adoption |
| Field trial (N=1,000) | ≥400 active items | ≥10× (Stocking recommended floor) | Empirical calibration coverage |
| Operational | 800–1,000 items | 20–25× | Security + exposure control |

---

## Sources

- [NWEA-2025-TR] NWEA. (2026). *MAP Growth Technical Report for 2024–2025*. NWEA/HMH. Figures 4.3, 4.9–4.11, Table 3.2.
- [NWEA-2025-NM] NWEA. (2025). *MAP Growth Norms Technical Manual 2025*. NWEA.
- [Wright-Stone-1979] Wright, B. D., & Stone, M. H. (1979). *Best test design*. MESA Press.
- [Linacre-1994] Linacre, J. M. (1994). Sample size and item calibration stability. *Rasch Measurement Transactions, 7*(4), 328.
- [Stocking-1994] Stocking, M. L. (1994). *Three practical issues for modern adaptive testing item pools*. ETS Research Report RR-94-5.
