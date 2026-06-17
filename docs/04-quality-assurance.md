# Quality-Assurance Report

This is a **living** document. Every published unit logs its QA pass/fail
status here. It is also where we record gaps and revisions.

---

## QA gates (every unit must pass all five)

1. **Curriculum alignment.** Every objective traces to an official
   competency from the Teaching Map (`sources/teaching_map_all_in_one.txt`).
2. **Bloom's accuracy.** Every objective verb is from the Bloom's level
   claimed; the verb-level table in `docs/01-pedagogical-framework.md` is
   the canonical reference.
3. **Assessment validity.** Every test item, exit ticket, performance task
   and rubric criterion maps to at least one stated objective.
4. **Competency alignment.** Every activity advances at least one of
   C1 (Interaction) / C2 (Production) / C3 (Interpretation).
5. **Gap detection.** Missing skills, sources, or strands are flagged.

---

## Phase status by deliverable

Status legend: `pending` = not yet built · `draft` = built, not reviewed ·
`pass` = all five gates passed · `flagged` = gate failure, see notes below ·
`scope-deferred` = decision on whether/how to build is pending an upstream
validation gate.

### Phase 2A — 2AS Foreign Languages standalone (current focus)

Per project decision (2026-06-17), Phase 2 is currently scoped down to
**Phase 2A** — the 2AS Foreign Languages stream as a self-contained,
validated model. **No derivation work for any other stream until the user
validates 2AS FL.** After validation the user will decide whether the
remaining streams are derived from 2AS FL or independently authored; that
decision is therefore not pre-committed here.

| Grade | Stream | Yearly plan | Scope & sequence | Pacing guide | Assessment calendar | Competency map |
|-------|--------|-------------|-------------------|--------------|----------------------|-----------------|
| **2AS** | **Foreign Languages** | draft — awaiting validation | draft — awaiting validation | draft — awaiting validation | draft — awaiting validation | draft — awaiting validation |

### Phase 2B+ — other streams (scope-deferred)

These are listed only so the registry is complete. **Not authored, not
scheduled.** Build (or derivation) decision is gated on the outcome of
Phase 2A validation.

| Grade | Stream | Status |
|-------|--------|--------|
| 2AS | Letters & Philosophy | scope-deferred |
| 2AS | Sciences / Maths / Tech-Maths | scope-deferred |
| 2AS | Management & Economy | scope-deferred |
| 1AS | Common Core Letters | scope-deferred |
| 1AS | Common Core Sciences & Tech | scope-deferred |
| 3AS | Foreign Languages | scope-deferred |
| 3AS | Letters / Philosophy | scope-deferred |
| 3AS | Sciences / Maths / Tech-Maths / Mgmt-Econ | scope-deferred |

### Phase 3 — Unit-by-unit overview log

Status legend: `pending` = not yet built · `draft` = built, not reviewed ·
`pass` = all five gates passed · `flagged` = gate failure, see notes below.

### 1AS — At the Crossroads

| # | Unit | Phase 3 (Overview) | Phase 5 (Lessons) | Phase 6 (Assessments) | Phase 7 (Rubrics) | Notes |
|---|------|--------------------|-------------------|------------------------|-------------------|-------|
| 1 | Getting Through | pending | pending | pending | pending | |
| 2 | Once Upon a Time | pending | pending | pending | pending | |
| 3 | Our Findings Show | pending | pending | pending | pending | |
| 4 | Eureka | pending | pending | pending | pending | |
| 5 | Back to Nature | pending | pending | pending | pending | |

### 2AS — Getting There

The 2AS package authoritatively covers **7 units** from the textbook
*Getting There* (textbook units 1, 2, 3, 4, 6, 7, 8). Textbook Unit 5 is
intentionally excluded per project decision — the official Teaching Map
omits it and no stream's syllabus theme depends on it.

| # | Unit | Phase 3 | Phase 5 | Phase 6 | Phase 7 | Notes |
|---|------|---------|---------|---------|---------|-------|
| 1 | Signs of the Time | pending | pending | pending | pending | |
| 2 | Make Peace! | pending | pending | pending | pending | |
| 3 | Waste Not Want Not | pending | pending | pending | pending | |
| 4 | Budding Scientist | pending | pending | pending | pending | |
| 6 | No Man Is an Island | pending | pending | pending | pending | |
| 7 | Science or Fiction | pending | pending | pending | pending | |
| 8 | Business Is Business | pending | pending | pending | pending | |

### 3AS — New Prospects

| # | Unit | Phase 3 | Phase 5 | Phase 6 | Phase 7 | Notes |
|---|------|---------|---------|---------|---------|-------|
| 1 | Exploring the Past | pending | pending | pending | pending | |
| 2 | Business Ethics | pending | pending | pending | pending | |
| 3 | Education | pending | pending | pending | pending | |
| 4 | Safety First | pending | pending | pending | pending | |
| 5 | Astronomy & Solar System | pending | pending | pending | pending | |
| 6 | Feelings & Emotions | pending | pending | pending | pending | |

---

## Gaps & revisions log

| Date | Item | Severity | Action |
|------|------|----------|--------|
| Phase 0 | 2AS textbook Unit 5 has no Teaching-Map page (source jumps from Unit 4 to Unit 6) | medium | **Decision (2026-06-17): skip entirely.** The 2AS package is authored as a 7-unit course covering textbook units 1, 2, 3, 4, 6, 7, 8. Textbook numbering preserved so teachers can match pages in *Getting There*. Cross-checked against the annual-distribution PDF — no stream's theme list depends on Unit 5. |
| Phase 0 | The three .pps decks are image-only — no text content recoverable beyond shape metadata | low | None needed; PDFs cover all syllabus-level content. |
| Phase 0 | Source documents do not specify lesson-by-lesson timing | low | Add defensible default ESA timings (60-min slot baseline) labelled as *pedagogical scaffolding*. |

---

## Sign-off

The user reviews this report at each pause point. When all units show `pass`
in all four phase columns, the curriculum is ready for adoption.
