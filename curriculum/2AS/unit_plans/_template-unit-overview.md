# Unit Overview Template (2AS Foreign Languages)

> **🔒 FROZEN PENDING REVIEW (revision 4 — 2026-06-17).**
> This template is locked. It cannot be edited, restructured, or
> re-ordered without explicit user approval. After review, the user
> will either approve it as-is (then it becomes the **immutable shape**
> of every 2AS FL unit overview) or request specific edits (then a
> single edit pass is applied and the file is re-frozen). No
> "optimisation pass" or silent refactor is permitted while this
> notice is in place.

---

## ❗ STRICT NO-INFERENCE RULE (mandatory)

All content in every authored unit overview **must be directly traceable
to one of the official curriculum sources**:

- **Teaching Map PDF** — `sources/teaching_map_all_in_one.pdf` (and its
  extracted text `sources/teaching_map_all_in_one.txt`)
- **Annual Distribution PDF** — `sources/official_syllabus_annual_distribution.pdf`
  (and its extracted text)
- **Textbook** — *Getting There* (page numbers as referenced by the
  Teaching Map's *Act. p. & n°* column)

If a field is not explicitly present in any of these sources, mark it
**`Not specified in source documents`**. Do not infer, derive,
extrapolate, or fill from analogy. Do not cross-pollinate from another
stream. No methodology metadata of any kind is permitted on top of
sourced content.

---

## ❗ Source Tagging Rule

- Allowed tags:
  - `[Teaching Map]`
  - `[Annual Distribution]`
  - `[Textbook]`
- Every field MUST have at least one tag
- No untagged content allowed

---

## ❌ FORBIDDEN IN TEMPLATE

The following are forbidden anywhere in any authored unit overview:

- No pedagogy frameworks
- No Bloom's taxonomy
- No objectives rewriting
- No competency weighting
- No alignment matrices
- No inferred relationships
- No instructional design structure

Any cell that would otherwise contain such content is replaced with
`Not specified in source documents` per the No Fabrication Escalation
Rule at the bottom of this template.

---

# UNIT SOURCE EXTRACTION TABLE

## Header

| Field | Value | Source |
|-------|-------|--------|
| Unit title | `{{title from teaching map}}` | `[Teaching Map]` |
| Textbook unit number | `{{txt-unit-number}}` | `[Textbook]` |
| Stream | Foreign Languages (2AS) | `[Annual Distribution]` |
| Week position | `{{e.g. T1 W2-W5}}` | `[Annual Distribution]` |
| Duration | `{{e.g. 4 weeks × 5 h = 20 h}}` | `[Annual Distribution]` |

---

## Section A — Source Extract (Teaching Map) `[Teaching Map]`

### A.1 Competencies (verbatim)

> Only list competencies exactly as written in the Teaching Map
> (C1 / C2 / C3). If not explicitly assigned →
> `Not specified in source documents`.

| Competency code | Verbatim source phrase | Source |
|------------------|-------------------------|--------|
| `{{C1 / C2 / C3 / Not specified in source documents}}` | `{{exact aim phrase}}` | `[Teaching Map]` |

### A.2 Aim (verbatim)

| Source statement | Source |
|------------------|--------|
| `{{verbatim aim from Teaching Map "Aim" column}}` | `[Teaching Map]` |
| `{{additional verbatim aim line, if present}}` | `[Teaching Map]` |

### A.3 Grammar (verbatim)

| Source statement | Source |
|------------------|--------|
| `{{verbatim from Teaching Map "Productive Lge / Exp." column}}` | `[Teaching Map]` |
| `{{...}}` | `[Teaching Map]` |

### A.4 Vocabulary (verbatim)

> Reproduce the Teaching Map's glossary table for this unit verbatim.
> Words / classes / definitions / synonyms / antonyms exactly as
> printed.

| Word | Word class | Definition | Synonyms | Antonyms | Source |
|------|------------|------------|----------|----------|--------|
| `{{word}}` | `{{n / v / adj}}` | `{{def from source}}` | `{{syn or "Not specified in source documents"}}` | `{{ant or "Not specified in source documents"}}` | `[Teaching Map]` |

### A.5 Source Statements Only (verbatim aim / objective excerpts)

> Verbatim excerpts from the Teaching Map only. No rewriting, no
> restating, no SWBAT transformation.

| Source Statement | Source       |
|------------------|--------------|
| `{{verbatim excerpt}}` | Teaching Map |
| `{{verbatim excerpt}}` | Teaching Map |

---

## Section B — Source Extract (Annual Distribution) `[Annual Distribution]`

| Field | Verbatim content | Source |
|-------|------------------|--------|
| Unit theme | `{{verbatim theme phrase from AD, e.g. "Diversity"}}` | `[Annual Distribution]` |
| Project (if stated) | `{{verbatim project line if present in AD; otherwise "Not specified in source documents"}}` | `[Annual Distribution]` |
| Time allocation | `{{verbatim weeks/hours allocation from AD pacing table}}` | `[Annual Distribution]` |

---

## Section C — Source Extract (Textbook) `[Textbook]`

| Field | Verbatim content | Source |
|-------|------------------|--------|
| Unit sequence (textbook order vs. taught order) | `{{e.g. "Textbook Unit 7 — taught at FL teaching position 5"}}` | `[Textbook]` |
| Page references (if available) | `{{p.??-p.?? as cited in TM "Act. P. & N°" column}}` | `[Textbook]` |

---

## Section D — Assessment (ONLY if explicitly stated)

> Only assessments that are **explicitly named** in the Teaching Map or
> the Annual Distribution may be recorded here. If a source does not
> name the assessment, the cell is `NO` with no source line; do not
> infer.

| Assessment | YES/NO | Source line (verbatim) | Source |
|------------|--------|--------------------------|--------|
| Written exam | `{{YES / NO}}` | `{{verbatim source line, e.g. اختبارات الثلاثي الأول}}` | `[Annual Distribution]` |
| Project | `{{YES / NO}}` | `{{verbatim Teaching Map "Project:" line}}` | `[Teaching Map]` |

---

## ✅ Validation checklist (must be ticked before submission)

- [ ] **All fields source-traceable** — every populated cell carries one of the allowed source tags (`[Teaching Map]` / `[Annual Distribution]` / `[Textbook]`), or is marked `Not specified in source documents`.
- [ ] **No inferred content** — no field is filled by analogy, derivation, cross-stream borrowing, cross-unit borrowing, textbook-pattern guessing, pedagogy frameworks, Bloom's taxonomy, objectives rewriting, competency weighting, alignment matrices, or instructional design structure (the full FORBIDDEN list above is empty in this file).
- [ ] **Exact textbook sequence compliance** — within-unit references follow the textbook's pagination as cited by the Teaching Map's *Act. P. & N°* column. Inter-unit teaching order follows the Annual Distribution (Reading A, confirmed 2026-06-17).
- [ ] **No pedagogical expansion beyond curriculum scope** — the unit overview contains no warm-ups, engage-study-activate sequences, timing breakdowns, instructional procedures, phase quizzes, exit tickets, objectives, rubric levels, or other lesson-flow / instructional-design content.

---

## Governance reminders (do not delete from authored files)

- This unit overview was authored per the **Stream Integrity Rule**
  (`../../../docs/01-pedagogical-framework.md` Section 1.b): it stands
  alone for the FL stream, not derived from any other stream.
- The teaching order **1 → 2 → 3 → 4 → 7 → 6** is the Annual
  Distribution order (Reading A, confirmed by user 2026-06-17).
- This unit overview must not be **structurally** rewritten,
  reorganised, or "optimised" without explicit user approval.
- Phase 1 docs (`docs/00-curriculum-map.md`) are FROZEN — any conflict
  between this unit overview and Phase 1 must be raised with the user
  for resolution, not silently corrected.

---

## 🚨 NO FABRICATION ESCALATION RULE

If a required field is not found in sources:

- Write exactly: **`Not specified in source documents`**
- Do NOT:
  - infer
  - generalize from other units
  - reuse textbook patterns
  - "complete logically"
