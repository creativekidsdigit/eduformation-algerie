# Unit Overview Template (2AS Foreign Languages)

> **This is a generic template — no unit content.** It is staged for
> Phase 3A authoring. When authorising Phase 3A, replace every
> `{{placeholder}}` with the corresponding sourced content. Do not
> remove or reorder the section headers; do not invent content for any
> field that the source documents are silent on (tag with
> `pending verification from official teaching map` instead).

> **Source hierarchy** (every cell below must cite where its content
> comes from): 1 = Teaching Map PDF · 2 = Annual Distribution PDF ·
> 3 = Textbook sequence · 4 = Derived pedagogical inference (must be
> labelled).

---

## Header

| Field | Value | Source |
|-------|-------|--------|
| Level | 2AS | priority 2 |
| Stream | Foreign Languages | priority 2 |
| Coefficient | 4 | priority 2 |
| Weekly hours | 5 | priority 2 |
| Textbook | *Getting There* | priority 3 |
| Textbook unit number | `{{txt-unit-number}}` | priority 3 |
| Teaching position | `{{1..6}}` | priority 2 (Annual Distribution order) |
| Unit title | `{{title from teaching map}}` | priority 1 |
| Annual-distribution theme | `{{theme}}` | priority 2 |
| Project / portfolio artefact | `{{project from teaching map}}` | priority 1 |
| Duration (weeks × 5 h) | `{{n weeks × 5 h = ?? h}}` | priority 2 (annual distribution week count) |

## Stage 1 — Desired Results (Backward Design)

### 1.1 Foregrounded competencies

> Source: priority 1 (Teaching Map "Aim" column tags units with C1/C2/C3).
> The *labels* are sourced; the *emphasis weighting* (★★★ / ★★ / ★) is
> priority-4 pedagogical inference and must be tagged.

| Code | Name | Foregrounded? | Source |
|------|------|---------------|--------|
| C1 | Interaction | `{{primary / secondary / touched}}` *(priority 4 — pending verification from official teaching map)* | priority 1 |
| C2 | Production | `{{primary / secondary / touched}}` *(priority 4 — pending verification from official teaching map)* | priority 1 |
| C3 | Interpretation | `{{primary / secondary / touched}}` *(priority 4 — pending verification from official teaching map)* | priority 1 |

### 1.2 Productive language (grammar + functional)

> Source: priority 1 (Teaching Map "Productive Lge / Exp." column).
> Verbatim from the source. Do not paraphrase.

| Grammar / form | Functional language / expressions | Teaching-Map page |
|----------------|------------------------------------|-------------------|
| `{{grammar item 1}}` | `{{functional language 1}}` | `{{p.??}}` |
| `{{grammar item 2}}` | `{{functional language 2}}` | `{{p.??}}` |
| `{{...}}` | `{{...}}` | `{{p.??}}` |

### 1.3 Vocabulary glossary

> Source: priority 1 (Teaching Map "Glossary (Lexis)" page for this unit).
> Verbatim from the source.

| Word | Word class | Definition (source) | Synonyms | Antonyms |
|------|------------|---------------------|----------|----------|
| `{{word}}` | `{{n / v / adj}}` | `{{def from source}}` | `{{syn}}` | `{{ant}}` |
| `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |

### 1.4 Skills focus per phase

> Source: priority 1 (Teaching Map "Phase" + "Aim" + "Act. P. & N°"
> columns). The textbook's six unit phases are non-negotiable per
> `../../../docs/01-pedagogical-framework.md` Section 6.

| Phase | Source-listed activities (Teaching Map p.& n°) | Source-listed aim |
|-------|-------------------------------------------------|-------------------|
| Listen & Consider | `{{Acts. p.??}}` | `{{aim}}` |
| Read & Consider | `{{Acts. p.??}}` | `{{aim}}` |
| Listening & Speaking | `{{Acts. p.??}}` | `{{aim}}` |
| Reading & Writing | `{{Acts. p.??}}` | `{{aim}}` |
| Write It Up | `{{Acts. p.??}}` | `{{aim}}` |
| Write It Out | `{{Acts. p.??}}` | `{{aim}}` |

### 1.5 Bloom's-tagged objectives

> Source: priority 4 — *pedagogical inference*. Bloom's verbs are mapped
> from the source's stated aims, not lifted verbatim from the source.
> Each objective MUST cite both a competency tag (C1/C2/C3) and a Bloom's
> level (Remember / Understand / Apply / Analyse / Evaluate / Create).

| # | Objective (SWBAT…) | Competency | Bloom's |
|---|---------------------|------------|---------|
| 1 | `{{Students will be able to <verb> <content> using <productive language> in <context>}}` | `{{C?}}` | `{{level}}` |
| 2 | `{{...}}` | `{{C?}}` | `{{level}}` |
| 3 | `{{...}}` | `{{C?}}` | `{{level}}` |
| 4 | `{{...}}` | `{{C?}}` | `{{level}}` |
| n | The unit's culminating Create-level objective: produce the project artefact | C2 (and one other if the project has an oral leg) | Create |

## Stage 2 — Acceptable Evidence (Backward Design)

> Source: priority 4 — *pedagogical scaffolding*. The Annual Distribution
> prescribes only the trimester written exam; everything else is
> consistent with the Six A's "Assessment Practices" pillar.

### 2.1 Project rubric (summative, end of unit)

| Field | Value |
|-------|-------|
| Rubric file | `../rubrics/project-rubric-{{slug}}.md` (to be authored in Phase 7) |
| Levels | Excellent · Good · Developing · Beginning |
| Criteria (≥ 4) | `{{tied to Stage-1 objectives}}` |
| Self-assessment row | yes (Six A's, Assessment Practices) |

### 2.2 Unit summative test (end of unit, ~1 h)

| Field | Value |
|-------|-------|
| Test file | `../assessments/2as_fl_unit_{{n}}_test.md` (to be authored in Phase 6) |
| Sections | Reading · Writing · Listening · Speaking |
| Competencies covered | `{{C1, C2, C3 — per the foregrounded set above}}` |
| Time | 60 minutes |

### 2.3 Phase quiz (formative — meso)

| Field | Value |
|-------|-------|
| Quiz file | `../assessments/2as_fl_unit_{{n}}_phase_quiz.md` |
| Trigger week | `{{week from Phase 2A assessment-calendar.md}}` |
| Focus | One high-leverage transfer item from this unit |

### 2.4 Exit-ticket protocol (formative — micro)

Source: priority 4 — pedagogical scaffolding. 2-minute exit ticket at
the end of each lesson; bank lives at `../assessments/exit-tickets-bank.md`.

## Alignment matrix (Stage 1 ⇄ Stage 2 traceability)

> Required by the QA Gate "Curriculum alignment" + "Assessment validity".
> Every objective must link to ≥ 1 activity and ≥ 1 evidence row.

| # | Competency | Objective (Stage 1.5) | Activity (Stage 1.4) | Assessment (Stage 2) |
|---|------------|------------------------|----------------------|-----------------------|
| 1 | `{{C?}}` | `{{obj 1}}` | `{{phase + Acts.}}` | `{{rubric / test / quiz / exit ticket}}` |
| 2 | `{{C?}}` | `{{obj 2}}` | `{{...}}` | `{{...}}` |
| n | `{{C?}}` | culminating Create | Write It Out + project assembly | project rubric |

## Source citations

> Every line above must trace to a source. Required citations:

- Teaching Map: `../../../sources/teaching_map_all_in_one.txt` lines `{{l1-l2}}` (textbook unit `{{n}}`)
- Annual Distribution: `../../../sources/official_syllabus_annual_distribution.txt` lines `{{l1-l2}}` (FL stream pacing)
- Textbook: *Getting There*, Unit `{{n}}`, pages `{{p.??-p.??}}`

## QA gate self-check

> Before marking this unit overview as `draft`, the author must tick all
> five gates from `../../../docs/04-quality-assurance.md`:

- [ ] **Curriculum alignment** — every Stage 1.5 objective traces to a competency tag from the Teaching Map.
- [ ] **Bloom's accuracy** — every objective verb matches its Bloom's level per `../../../docs/01-pedagogical-framework.md` Section 3.
- [ ] **Assessment validity** — every Stage 2 evidence row maps to ≥ 1 Stage 1.5 objective.
- [ ] **Competency alignment** — every Stage 1.4 activity advances ≥ 1 of C1/C2/C3.
- [ ] **Gap detection** — any Teaching-Map silence is tagged
  `pending verification from official teaching map` (NOT filled by inference).

---

## Governance reminders (do not delete from authored files)

- This unit overview was authored per the **Stream Integrity Rule**:
  it stands alone for the FL stream, not derived from any other stream.
- The teaching order **1 → 2 → 3 → 4 → 7 → 6** is the Annual
  Distribution order (Reading A, confirmed by user 2026-06-17).
- This unit overview must not be **structurally** rewritten,
  reorganised, or "optimised" without explicit user approval.
- Phase 1 docs (`docs/00-curriculum-map.md`) are FROZEN — any conflict
  between this unit overview and Phase 1 must be raised with the user
  for resolution, not silently corrected.
