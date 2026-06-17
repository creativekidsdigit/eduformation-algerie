# Unit Overview Template (2AS Foreign Languages)

> **🔒 FROZEN PENDING REVIEW (revision 2 — 2026-06-17).**
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
stream. The only methodology metadata permitted on top of sourced
content is the Bloom's-level annotation in Stage 1.5 (limited per the
rule below).

---

## 🚨 NO FABRICATION ESCALATION RULE

If a required field is not found in source documents:

1. Write: **`Not specified in source documents`**
2. Do **NOT**:
   - infer from other units
   - infer from textbook patterns
   - infer from pedagogy
3. Do **NOT** leave blank fields

This rule prevents silent hallucination filling. It applies to **every**
field in every authored unit overview. A blank cell is a critical QA
failure; an `Not specified in source documents` cell is correct
behaviour when the source is silent.

---

## ❗ MANDATORY SOURCE TAGGING (every cell)

Every populated cell in every section below carries one of the
following allowed tags. Multiple tags per cell are permitted when the
content draws on more than one source.

| Tag | Meaning |
|-----|---------|
| `[TM]` | Content sourced from the official Teaching Map PDF. |
| `[AD]` | Content sourced from the official Annual Distribution PDF. |
| `[TB]` | Content sourced from the textbook *Getting There* (page reference required). |
| `[TM+AD]` | Content combines Teaching Map and Annual Distribution (both cited). |
| `[TM+TB]` | Content combines Teaching Map and Textbook (both cited). |

Multi-source cells **may** carry either the combined tag (e.g.
`[TM+AD]`) or two separate tags (e.g. `[TM] [AD]`); both forms are
acceptable. Cells with no applicable source carry **`Not specified in
source documents`** (no tag) per the No Fabrication Escalation Rule.
**Untagged sourced content is forbidden.**

---

## ❗ BLOOM'S TAXONOMY USAGE (controlled range)

Bloom's-level annotations are subject to the following controlled rules:

| Bloom's level | When permitted |
|---------------|----------------|
| **Remember** | Always permitted. |
| **Understand** | Default range (allowed without source-verb justification). |
| **Apply** | Default range (allowed without source-verb justification). |
| **Analyse** | Only when explicitly supported by a source verb (cite the verb). |
| **Evaluate** | Only when explicitly stated in the Teaching Map *or* required by the unit's project description (cite the source phrase). |
| **Create** | Only when explicitly stated in the Teaching Map *or* required by the unit's project description (cite the source phrase). |

The default range is **Understand → Apply**, with **Remember** always
available. Higher levels (Analyse, Evaluate, Create) are not forbidden —
they are required where the source justifies them, and forbidden where
it does not. Each objective at Analyse-or-above MUST cite the exact
source phrase that supports the level.

---

## Header

| Field | Value | Source |
|-------|-------|--------|
| Level | 2AS | `[AD]` |
| Stream | Foreign Languages | `[AD]` |
| Coefficient | 4 | `[AD]` |
| Weekly hours | 5 | `[AD]` |
| Textbook | *Getting There* | `[TB]` |
| Textbook unit number | `{{txt-unit-number}}` | `[TB]` |
| Teaching position (1..6) | `{{1..6}}` | `[AD]` |
| Unit title | `{{title from teaching map}}` | `[TM]` |
| Annual-distribution theme | `{{theme}}` | `[AD]` |
| Project / portfolio artefact | `{{project from teaching map}}` | `[TM]` |
| Annual-distribution week range | `{{e.g. T1 W2-W5}}` | `[AD]` |

---

## Stage 1 — Source-Mandated Content

### 1.1 Competencies (foregrounded by the unit's source aims)

> Source: `[TM]` — the per-unit aim sections explicitly tag C1
> (Interaction), C2 (Production), C3 (Interpretation). Only competencies
> the Teaching Map *names* for this unit appear here. No emphasis
> weighting, no inference.

| Code | Name | Foregrounded by source? | Source phrase (verbatim) | Source tag |
|------|------|--------------------------|---------------------------|-----------|
| C1 | Interaction | `{{yes / no / Not specified in source documents}}` | `{{exact aim phrase}}` | `[TM]` |
| C2 | Production | `{{yes / no / Not specified in source documents}}` | `{{exact aim phrase}}` | `[TM]` |
| C3 | Interpretation | `{{yes / no / Not specified in source documents}}` | `{{exact aim phrase}}` | `[TM]` |

### 1.2 Productive language (grammar + functional)

> Source: `[TM]` "Productive Lge / Exp." column. Verbatim only. The
> textbook page reference may add a `[TB]` tag when the productive item
> is anchored to a specific textbook activity.

| Grammar / form | Functional language / expression | Teaching-Map page | Source tag |
|----------------|------------------------------------|--------------------|-----------|
| `{{verbatim}}` | `{{verbatim}}` | `{{p.??}}` | `[TM]` or `[TM+TB]` |
| `{{...}}` | `{{...}}` | `{{p.??}}` | `[TM]` or `[TM+TB]` |

### 1.3 Vocabulary glossary

> Source: `[TM]` "Glossary (Lexis)" page for this unit. Verbatim only.

| Word | Word class | Definition (verbatim) | Synonyms | Antonyms | Source tag |
|------|------------|------------------------|----------|----------|-----------|
| `{{word}}` | `{{n / v / adj}}` | `{{def from source}}` | `{{syn or "Not specified in source documents"}}` | `{{ant or "Not specified in source documents"}}` | `[TM]` |

### 1.4 Per-phase activities and aims (unit-specific detail)

> Source: `[TM]` "Phase" + "Aim" + "Act. P. & N°" columns. The
> per-unit specific activities and aims for each of the textbook's six
> phases. The structural enforcement layer is in Section 1.6 below.

| Phase | Source-listed activities | Source-listed aim | Source tag |
|-------|---------------------------|--------------------|-----------|
| Listen & Consider | `{{Acts. p.??}}` | `{{aim verbatim}}` | `[TM]` or `[TM+TB]` |
| Read & Consider | `{{Acts. p.??}}` | `{{aim verbatim}}` | `[TM]` or `[TM+TB]` |
| Listening & Speaking | `{{Acts. p.??}}` | `{{aim verbatim}}` | `[TM]` or `[TM+TB]` |
| Reading & Writing | `{{Acts. p.??}}` | `{{aim verbatim}}` | `[TM]` or `[TM+TB]` |
| Write It Up | `{{Acts. p.??}}` | `{{aim verbatim}}` | `[TM]` or `[TM+TB]` |
| Write It Out | `{{Acts. p.??}}` | `{{aim verbatim}}` | `[TM]` or `[TM+TB]` |

### 1.5 Bloom's-tagged objectives

> Each objective must be either **verbatim-based** on a source aim, or
> **clearly derived from an explicit source verb**. If the source aim
> verb does not explicitly support a level above Apply, the objective
> is downgraded to Understand or Apply, OR the cell is marked
> `Not specified in source documents`. The source aim is shown in the
> first column for traceability; the restated objective is in the
> second column. The Bloom's level is methodology metadata controlled
> per the Bloom's Taxonomy Usage rule above.

| # | Source aim (verbatim) | Restated objective (SWBAT…) | Competency | Bloom's level | Source-verb justification (required for Analyse / Evaluate / Create) | Source tag |
|---|------------------------|------------------------------|------------|---------------|----------------------------------------------------------------------|-----------|
| 1 | `{{verbatim aim}}` | `{{Students will be able to <verb> <content>}}` | `{{C? from TM}}` | `{{Remember / Understand / Apply}}` | n/a | `[TM]` |
| 2 | `{{verbatim aim}}` | `{{...}}` | `{{C?}}` | `{{R / U / A}}` | n/a | `[TM]` |
| n | `{{verbatim aim with explicit "write" / "produce" / "analyse" / "judge" verb}}` | `{{...}}` | `{{C?}}` | `{{Analyse / Evaluate / Create}}` | `{{cite source phrase + verb}}` | `[TM]` |

### 1.6 Teaching Map Phase Structure (STRICT)

> Source: `[TM]`. The textbook's six phases are **non-negotiable** as a
> structure: every authored unit overview must contain all six phases,
> in this exact order, with no phase omitted, renamed, merged, or
> reordered. This section is **descriptive only** — it is the
> structural enforcement layer for the per-phase data filled into
> Section 1.4. **No instructional procedures, no timings, no warm-ups,
> no engage-study-activate notes, no lesson sequencing.**

| Phase | Source Activities | Aim | Source |
|-------|--------------------|------|--------|
| Listen & Consider | `{{Acts. p.??}}` | `{{aim verbatim}}` | `[TM]` |
| Read & Consider | `{{Acts. p.??}}` | `{{aim verbatim}}` | `[TM]` |
| Listening & Speaking | `{{Acts. p.??}}` | `{{aim verbatim}}` | `[TM]` |
| Reading & Writing | `{{Acts. p.??}}` | `{{aim verbatim}}` | `[TM]` |
| Write It Up | `{{Acts. p.??}}` | `{{aim verbatim}}` | `[TM]` |
| Write It Out | `{{Acts. p.??}}` | `{{aim verbatim}}` | `[TM]` |

If the Teaching Map page for a unit does not list activities for a
given phase, the corresponding cell is marked
`Not specified in source documents` per the No Fabrication Escalation
Rule. The phase row itself is **never deleted**.

---

## Stage 2 — Source-Mandated Assessments

> Only assessments that exist in the official source documents appear
> here. Phase quizzes, exit tickets, and other formative tools are
> **not** in the source and therefore not part of the unit overview.

### 2.1 Project artefact (mandated by Teaching Map)

| Field | Value | Source tag |
|-------|-------|-----------|
| Project description | `{{verbatim from Teaching Map "Project:" line}}` | `[TM]` |
| Portfolio deliverables | `{{verbatim list from Teaching Map "Portfolio" column}}` | `[TM]` |
| Project rubric file | `../rubrics/project-rubric-{{slug}}.md` (file pointer; rubric levels not specified in source documents) | n/a (file pointer only) |

### 2.2 Trimester written exam (mandated by Annual Distribution)

| Field | Value | Source tag |
|-------|-------|-----------|
| Trimester this unit feeds | `{{T1 / T2 / T3 from AD week range}}` | `[AD]` |
| Source phrase | `{{e.g. اختبارات الثلاثي الأول}}` | `[AD]` |
| Exam file (placeholder) | `../assessments/2as_fl_t{{n}}_exam.md` (to be authored later; format not specified in source documents) | n/a (file pointer only) |

---

## Alignment matrix (Stage 1 ⇄ Stage 2 traceability)

> Every objective from Stage 1.5 must trace to ≥ 1 phase activity
> (Section 1.4 / 1.6) and ≥ 1 source-mandated assessment (Stage 2).
> Only sourced content appears in this matrix.

| # | Competency `[TM]` | Restated objective (Stage 1.5) | Phase + activity (Section 1.4 / 1.6) | Source-mandated assessment (Stage 2) |
|---|--------------------|---------------------------------|---------------------------------------|----------------------------------------|
| 1 | `{{C?}}` | `{{obj 1}}` | `{{phase + Acts.}}` | `{{project / trimester exam}}` |
| 2 | `{{C?}}` | `{{obj 2}}` | `{{...}}` | `{{...}}` |
| n | `{{C?}}` | `{{...}}` | Write It Out + project assembly | project artefact |

---

## Source citations

> Every line above traces to one of the following. Required when
> authoring; line numbers refer to the extracted text files in
> `sources/`.

- Teaching Map: `../../../sources/teaching_map_all_in_one.txt` lines `{{l1-l2}}` (textbook unit `{{n}}`) — `[TM]`
- Annual Distribution: `../../../sources/official_syllabus_annual_distribution.txt` lines `{{l1-l2}}` (FL stream pacing) — `[AD]`
- Textbook: *Getting There*, Unit `{{n}}`, pages `{{p.??-p.??}}` — `[TB]`

---

## ✅ Validation checklist (must be ticked before submission)

- [ ] **All fields source-traceable** — every populated cell carries one of the allowed source tags (`[TM]` / `[AD]` / `[TB]` / `[TM+AD]` / `[TM+TB]`, including multi-tag cells where applicable), or is marked `Not specified in source documents`.
- [ ] **No inferred content** — no field is filled by analogy, derivation, cross-stream borrowing, cross-unit borrowing, textbook-pattern guessing, or pedagogical scaffolding. Bloom's level annotations are the only methodology metadata permitted, and they are bound by the controlled-range rule above.
- [ ] **Exact textbook sequence compliance** — within-unit activity references follow the textbook's pagination as cited by the Teaching Map's *Act. p. & n°* column. Inter-unit teaching order follows the Annual Distribution (Reading A, confirmed 2026-06-17).
- [ ] **No pedagogical expansion beyond curriculum scope** — the unit overview contains no warm-ups, engage-study-activate sequences, timing breakdowns, instructional procedures, phase quizzes, exit tickets, or other lesson-flow content. Section 1.6 is descriptive of the source's phase structure only; lesson-flow belongs to a later phase.

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
