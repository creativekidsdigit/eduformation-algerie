# Algerian Secondary School English Curriculum (1AS / 2AS / 3AS)

A complete, teacher-ready Competency-Based English curriculum for the three years
of Algerian secondary education, derived from the **official Ministry of National
Education syllabus** (Programme officiel & Distribution annuelle, Inspectorat de
l'enseignement secondaire).

> **Authoritative source:** Every competency, outcome, theme, unit, project,
> productive-language item, and time allocation in this package is extracted
> directly from the official documents listed in `docs/02-source-attribution.md`.
> Nothing is invented. Where this package adds pedagogical scaffolding
> (Bloom's-aligned objectives, rubric descriptors, differentiation strategies,
> formative-assessment instruments) those additions are clearly labelled as
> *pedagogical scaffolding* and are mapped back to the official competencies.

## Curriculum at a glance

| Year | Streams | Annual Hours | Coefficients | Units | Textbook |
|------|---------|--------------|--------------|-------|----------|
| **1AS** | Common Core Sciences & Technology / Common Core Letters | 81 / 108 | 2 / 3 | 5 | At the Crossroads |
| **2AS** | Letters & Philosophy / Foreign Languages / Sciences-Maths-TM / Management & Economy | 108 / 135 / 81 / 81 | 3 / 4 / 2 / 2 | 5–7 | Getting There |
| **3AS** | Letters / Foreign Languages / Sciences-Maths-TM / Mgmt & Economy | 108 / 108 / 81 / 81 | 3 / **5** / 2 / 2 | 4 of 6 | New Prospects |

## Package structure

```
eduformation-algerie/
|- README.md                     <- you are here
|- docs/                          Foundational documents
|   |- 00-curriculum-map.md       Master curriculum map (Phase 1 deliverable)
|   |- 01-pedagogical-framework.md  CBA, Bloom's, Backward Design, Six A's, ESA
|   |- 02-source-attribution.md    Official sources, citation, fidelity policy
|   |- 03-implementation-plan.md   How to roll this out in your school
|   |- 04-quality-assurance.md     QA process, alignment matrix, gap report
|
|- curriculum/                    Teacher-ready deliverables (per grade)
|   |- 1AS/                       First Year Secondary
|   |   |- annual_plan/           Yearly plan, scope & sequence, pacing, assessment calendar
|   |   |- unit_plans/            Unit overviews (one file per unit)
|   |   |- lesson_plans/          Full lesson plans (warm-up -> reflection)
|   |   |- assessments/           Diagnostic / formative / summative
|   |   |- rubrics/               Reading, writing, listening, speaking, project
|   |   |- worksheets/            Student handouts
|   |   |- teacher_guide/         Teaching notes
|   |   |- answer_keys/           Keys for every assessment & worksheet
|   |- 2AS/  ... (same structure)
|   |- 3AS/  ... (same structure)
|   |- _shared/                   Cross-grade tools (generic rubrics, differentiation banks)
|
|- sources/                       Original PDFs/PPS + extracted plain text (do not edit)
```

## How to use

1. Start with **`docs/00-curriculum-map.md`** to understand the whole architecture.
2. Read **`docs/01-pedagogical-framework.md`** to align your team on the
   Competency-Based Approach (CBA), Bloom's taxonomy alignment, Backward Design,
   the official "Six A's of Project Design", and the Engage-Study-Activate model.
3. Open **`curriculum/<grade>/annual_plan/`** for your scope and sequence.
4. For each upcoming unit, open the matching file in **`unit_plans/`** then
   sequence through the **`lesson_plans/`**.
5. Use **`assessments/`** + **`rubrics/`** for evaluation, and
   **`teacher_guide/`** + **`answer_keys/`** to support your delivery.

## Quality assurance commitment

Every unit in this package goes through five QA gates before publication:

1. **Curriculum alignment** — every objective traces to an official competency.
2. **Bloom's taxonomy accuracy** — verbs match the cognitive level claimed.
3. **Assessment validity** — every assessment item targets a stated objective.
4. **Competency alignment** — every activity advances at least one competency.
5. **Gap detection** — missing skills/strands are surfaced and addressed.

Per-unit quality reports are emitted into `docs/04-quality-assurance.md`.

## Status

| Phase | Deliverable | Status |
|-------|-------------|--------|
| 0 | Source acquisition & extraction | Complete |
| 1 | Curriculum analysis & master map | **Complete — pause for user review** |
| 2 | Annual plans (3 grades) | Pending review |
| 3 | Unit plans (per unit) | Pending review |
| 4 | Objective alignment (Bloom's + tables) | Pending review |
| 5 | Lesson plans | Pending review |
| 6 | Assessment system | Pending review |
| 7 | Rubrics | Pending review |
| 8 | Differentiation pack | Pending review |
| 9 | Teacher resource pack | Pending review |
