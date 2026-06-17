# Unit Overview Template (2AS Foreign Languages)

> **🔒 FROZEN PENDING REVIEW (revised 2026-06-17).**
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

## ❗ MANDATORY SOURCE TAGGING (every cell)

Every populated cell in every section below carries exactly one of the
four source tags:

| Tag | Meaning |
|-----|---------|
| `[Teaching Map]` | Content is verbatim from the official Teaching Map PDF. |
| `[Annual Distribution]` | Content is verbatim from the official Annual Distribution PDF. |
| `[Textbook: Getting There]` | Content is from the textbook (page reference). |
| `[Mixed: TM + AD]` | Content combines two official sources, both of which are cited. |

If no source applies, the cell value is `Not specified in source
documents` (no tag). **Untagged sourced content is forbidden.**

---

## ❗ LIMITED BLOOM'S TAXONOMY USAGE

By default, only the following Bloom's levels may appear in Stage 1.5
objectives:

- **Remember**
- **Understand**
- **Apply**

Higher levels (**Analyse / Evaluate / Create**) are **only** permitted
when the source aim verb explicitly supports them (e.g. the Teaching Map
states "Make PP write…" → Create; "Analyse the difference…" → Analyse).
If the source uses a Remember/Understand/Apply verb, the Bloom's level
must be Remember/Understand/Apply.

The default ceiling is **Apply**. Anything above Apply must cite the
exact source phrase that supports it.

---

## Header

| Field | Value | Source |
|-------|-------|--------|
| Level | 2AS | `[Annual Distribution]` |
| Stream | Foreign Languages | `[Annual Distribution]` |
| Coefficient | 4 | `[Annual Distribution]` |
| Weekly hours | 5 | `[Annual Distribution]` |
| Textbook | *Getting There* | `[Textbook: Getting There]` |
| Textbook unit number | `{{txt-unit-number}}` | `[Textbook: Getting There]` |
| Teaching position (1..6) | `{{1..6}}` | `[Annual Distribution]` |
| Unit title | `{{title from teaching map}}` | `[Teaching Map]` |
| Annual-distribution theme | `{{theme}}` | `[Annual Distribution]` |
| Project / portfolio artefact | `{{project from teaching map}}` | `[Teaching Map]` |
| Annual-distribution week range | `{{e.g. T1 W2-W5}}` | `[Annual Distribution]` |

---

## Stage 1 — Source-Mandated Content

### 1.1 Competencies (foregrounded by the unit's source aims)

> Source: `[Teaching Map]` — the per-unit aim sections explicitly tag C1
> (Interaction), C2 (Production), C3 (Interpretation). Only competencies
> the Teaching Map *names* for this unit appear here. No emphasis
> weighting, no inference.

| Code | Name | Foregrounded by source? | Source phrase (verbatim) | Source tag |
|------|------|--------------------------|---------------------------|-----------|
| C1 | Interaction | `{{yes / no / Not specified in source documents}}` | `{{exact aim phrase}}` | `[Teaching Map]` |
| C2 | Production | `{{yes / no / Not specified in source documents}}` | `{{exact aim phrase}}` | `[Teaching Map]` |
| C3 | Interpretation | `{{yes / no / Not specified in source documents}}` | `{{exact aim phrase}}` | `[Teaching Map]` |

### 1.2 Productive language (grammar + functional)

> Source: `[Teaching Map]` "Productive Lge / Exp." column. Verbatim only.

| Grammar / form | Functional language / expression | Teaching-Map page | Source tag |
|----------------|------------------------------------|--------------------|-----------|
| `{{verbatim}}` | `{{verbatim}}` | `{{p.??}}` | `[Teaching Map]` |
| `{{...}}` | `{{...}}` | `{{p.??}}` | `[Teaching Map]` |

### 1.3 Vocabulary glossary

> Source: `[Teaching Map]` "Glossary (Lexis)" page for this unit.
> Verbatim only.

| Word | Word class | Definition (verbatim) | Synonyms | Antonyms | Source tag |
|------|------------|------------------------|----------|----------|-----------|
| `{{word}}` | `{{n / v / adj}}` | `{{def from source}}` | `{{syn or "Not specified in source documents"}}` | `{{ant or "Not specified in source documents"}}` | `[Teaching Map]` |

### 1.4 Per-phase activities and aims

> Source: `[Teaching Map]` "Phase" + "Aim" + "Act. P. & N°" columns.
> The textbook's six unit phases are the source's own structure;
> activities and aims are verbatim. No instructional procedures, no
> timings, no warm-ups, no engage-study-activate notes.

| Phase | Source-listed activities | Source-listed aim | Source tag |
|-------|---------------------------|--------------------|-----------|
| Listen & Consider | `{{Acts. p.??}}` | `{{aim verbatim}}` | `[Teaching Map]` |
| Read & Consider | `{{Acts. p.??}}` | `{{aim verbatim}}` | `[Teaching Map]` |
| Listening & Speaking | `{{Acts. p.??}}` | `{{aim verbatim}}` | `[Teaching Map]` |
| Reading & Writing | `{{Acts. p.??}}` | `{{aim verbatim}}` | `[Teaching Map]` |
| Write It Up | `{{Acts. p.??}}` | `{{aim verbatim}}` | `[Teaching Map]` |
| Write It Out | `{{Acts. p.??}}` | `{{aim verbatim}}` | `[Teaching Map]` |

### 1.5 Bloom's-tagged objectives

> The objective text is restated from the source aim (column 2 of 1.4).
> The competency tag (C1/C2/C3) comes verbatim from the Teaching Map.
> The Bloom's level is methodology metadata, capped at **Apply** unless
> the cited source aim verb explicitly supports a higher level (cite
> the verb).

| # | Source aim (verbatim) | Restated objective (SWBAT…) | Competency | Bloom's level | Source tag |
|---|------------------------|------------------------------|------------|---------------|-----------|
| 1 | `{{verbatim aim}}` | `{{Students will be able to <verb> <content>}}` | `{{C? from TM}}` | `{{Remember / Understand / Apply}}` | `[Teaching Map]` |
| 2 | `{{verbatim aim}}` | `{{...}}` | `{{C?}}` | `{{R / U / A}}` | `[Teaching Map]` |
| n | `{{verbatim aim with explicit "write" / "produce" verb}}` | culminating production (project artefact) | C2 | `Create` *(only if source aim verb explicitly = write / produce / create / compose; otherwise Apply)* | `[Teaching Map]` |

If the unit has no source aim that supports a higher Bloom's level, the
ceiling is Apply — including for the project objective.

---

## Stage 2 — Source-Mandated Assessments

> Only assessments that exist in the official source documents appear
> here. Phase quizzes, exit tickets, and other formative tools are
> **not** in the source and therefore not part of the unit overview.

### 2.1 Project artefact (mandated by Teaching Map)

| Field | Value | Source tag |
|-------|-------|-----------|
| Project description | `{{verbatim from Teaching Map "Project:" line}}` | `[Teaching Map]` |
| Portfolio deliverables | `{{verbatim list from Teaching Map "Portfolio" column}}` | `[Teaching Map]` |
| Project rubric file | `../rubrics/project-rubric-{{slug}}.md` (file pointer; rubric levels not specified in source documents) | n/a (file pointer only) |

### 2.2 Trimester written exam (mandated by Annual Distribution)

| Field | Value | Source tag |
|-------|-------|-----------|
| Trimester this unit feeds | `{{T1 / T2 / T3 from AD week range}}` | `[Annual Distribution]` |
| Source phrase | `{{e.g. اختبارات الثلاثي الأول}}` | `[Annual Distribution]` |
| Exam file (placeholder) | `../assessments/2as_fl_t{{n}}_exam.md` (to be authored later; format not specified in source documents) | n/a (file pointer only) |

---

## Alignment matrix (Stage 1 ⇄ Stage 2 traceability)

> Every objective from Stage 1.5 must trace to ≥ 1 phase activity
> (Stage 1.4) and ≥ 1 source-mandated assessment (Stage 2). Only
> sourced content appears in this matrix.

| # | Competency `[TM]` | Restated objective (Stage 1.5) | Phase + activity (Stage 1.4) | Source-mandated assessment (Stage 2) |
|---|--------------------|---------------------------------|-------------------------------|----------------------------------------|
| 1 | `{{C?}}` | `{{obj 1}}` | `{{phase + Acts.}}` | `{{project / trimester exam}}` |
| 2 | `{{C?}}` | `{{obj 2}}` | `{{...}}` | `{{...}}` |
| n | C2 | culminating production | Write It Out + project assembly | project artefact |

---

## Source citations

> Every line above traces to one of the following. Required when
> authoring; line numbers refer to the extracted text files in
> `sources/`.

- Teaching Map: `../../../sources/teaching_map_all_in_one.txt` lines `{{l1-l2}}` (textbook unit `{{n}}`) — `[Teaching Map]`
- Annual Distribution: `../../../sources/official_syllabus_annual_distribution.txt` lines `{{l1-l2}}` (FL stream pacing) — `[Annual Distribution]`
- Textbook: *Getting There*, Unit `{{n}}`, pages `{{p.??-p.??}}` — `[Textbook: Getting There]`

---

## ✅ Validation checklist (must be ticked before submission)

- [ ] **All fields source-traceable** — every populated cell carries one of the four source tags (`[Teaching Map]` / `[Annual Distribution]` / `[Textbook: Getting There]` / `[Mixed: TM + AD]`), or is marked `Not specified in source documents`.
- [ ] **No inferred content** — no field is filled by analogy, derivation, cross-stream borrowing, or pedagogical scaffolding. Bloom's level annotations are the only methodology metadata permitted, and they are capped at Apply unless the source aim verb explicitly supports a higher level.
- [ ] **Exact textbook sequence compliance** — within-unit activity references follow the textbook's pagination as cited by the Teaching Map's *Act. p. & n°* column. Inter-unit teaching order follows the Annual Distribution (Reading A, confirmed 2026-06-17).
- [ ] **No pedagogical expansion beyond curriculum scope** — the unit overview contains no warm-ups, engage-study-activate sequences, timing breakdowns, instructional procedures, phase quizzes, exit tickets, or other lesson-flow content. Such content belongs in lesson plans (a later phase), not in unit overviews.

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
