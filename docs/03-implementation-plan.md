# Implementation Plan

This is the operational roll-out plan for the curriculum: how this package
moves from `docs/` into a teacher's lesson book, classroom by classroom.

---

## Build order (the agent's working sequence)

| Phase | Deliverable | Folder | Approx. file count |
|-------|-------------|--------|--------------------|
| 0 ✓ | Source acquisition + extraction | `sources/` | 5 PDFs/PPS + extracted .txt |
| 1 ✓ | Master curriculum map + framework | `docs/00–02` | 4 markdown |
| 1 ✓ | Implementation plan (this file) | `docs/03` | 1 markdown |
| **2A — current** | Annual plans for 2AS Foreign Languages **only** (4 deliverables: yearly plan + scope & sequence + assessment calendar + competency map). Authored independently from official source documents per the Stream Integrity Rule. | `curriculum/2AS/annual_plan/` | 4 markdown |
| 2B+ — pending | Annual plans for the remaining 8 stream-grade combinations. Each stream **independently authored** from the official source documents — derivation, trimming, mapping, or normalisation between streams is forbidden by the Stream Integrity Rule (`docs/01-pedagogical-framework.md` Section 1.b). | `curriculum/<grade>/annual_plan/` | 32 markdown (8 streams × 4 deliverables) |
| **3A — preparation only** | Unit overviews for 2AS Foreign Languages **only** (6 units: 1, 2, 3, 4, 7, 6). Backward Design Stage 1 + Stage 2 per unit. **Template + index are authored as preparation; authoring of the 6 individual unit files is on hold pending explicit user authorisation.** | `curriculum/2AS/unit_plans/` | template (1) + index (1) + units (6, on hold) |
| 3B+ — pending | Unit overviews for the remaining 8 stream-grade combinations. Each independently authored from official sources per the Stream Integrity Rule. | `curriculum/<grade>/unit_plans/` | TBD (one set per stream) |
| 4 | Bloom's-aligned objective tables (embedded in unit & lesson files) | inline | — |
| 5 | Lesson plans (avg 8 lessons / unit × 18 units) | `curriculum/<grade>/lesson_plans/` | ~144 files |
| 6 | Diagnostic + formative + summative assessments | `curriculum/<grade>/assessments/` | ~3 diagnostic + 18 unit tests + 6 trimester exams = **27** |
| 7 | Rubrics (R-W-L-S + project per grade) | `curriculum/<grade>/rubrics/` + `_shared/rubrics/` | 5 shared + 18 project = **23** |
| 8 | Differentiation pack | `_shared/differentiation/` | 4 (struggling / ADHD / advanced / inclusive) |
| 9 | Teacher guide + answer keys + assessment guide + pacing + classroom guide | `curriculum/<grade>/teacher_guide/` + `answer_keys/` | ~12 files |
| QA | Per-unit quality reports | `docs/04-quality-assurance.md` | 1 living report |

Total expected output: ~250 files.

---

## Recommended pause points (for user review)

This is a large package. We pause for explicit user sign-off **before**:

1. ✅ **Now** — after the master curriculum map (Phase 1).
2. After Phase 2 (annual plans) — to confirm pacing & assessment calendar are
   correct for your school's calendar.
3. After Phase 3 (unit overviews for Year 1) — to confirm objective style
   and depth before scaling to 2AS / 3AS.
4. After Phase 5 first lesson — to confirm lesson template & timing fits
   your slot (45 / 60 / 90 minutes).
5. Before final delivery — to choose how to publish (PR? branch? zip?).

If you want to skip any pause, say so and we will continue without stopping.

---

## How a teacher uses this package, week by week

### Before the year starts (1 week)

1. Read `README.md`, `docs/00-curriculum-map.md`, and
   `docs/01-pedagogical-framework.md`.
2. Open `curriculum/<your-grade>/annual_plan/yearly_plan.md` and copy the
   pacing into your school's calendar.
3. Reproduce the diagnostic test (`assessments/diagnostic-entry-test.md`).
4. Skim the project list — buy / book any materials needed.

### Week 1 of the year

1. Administer the diagnostic + skills checklist.
2. Record results in the *baseline* row of the formative log.
3. Use Lesson 1 of Unit 1 as your week-1 launch.

### Per unit (typically 4–6 weeks)

1. Open the unit overview in `unit_plans/`. Print the alignment matrix.
2. Day-by-day, run the lesson plans in order. Each lesson contains:
   - Bloom's-tagged objectives
   - ESA flow with timings
   - Differentiation row
   - Materials list
3. Use the formative tools at the end of each lesson (exit ticket etc.).
4. Run the unit test from `assessments/`. Use the matching rubric in
   `rubrics/`.
5. Mark the project against the project rubric. Place artefacts in the
   student portfolio.

### Per trimester

1. Run the trimester written exam blueprint from `assessments/`.
2. Use the answer key in `answer_keys/`.
3. Triangulate exam results, project portfolio, and the formative log to
   produce the report card.

### End of year

1. Reflect using the QA gap report and the differentiation outcomes.
2. Submit improvement notes (the curriculum is editable).

---

## Adoption levers (low-, mid-, high-fidelity)

| Adoption level | What you do | Effort |
|----------------|-------------|--------|
| **Low** (you have textbooks, want better lessons) | Use only `lesson_plans/` and `rubrics/` | 2–3 hrs / week |
| **Mid** (you want CBA + Backward Design) | Use unit overviews, lesson plans, assessment system, rubrics | 1 day prep / unit |
| **High** (whole department adopts) | Use the entire package; align teachers via `teacher_guide/`; deploy `differentiation/` and the QA process | 1 week department PD + ongoing |

---

## Editing & extension

Every file is plain Markdown. You can:

- Edit directly in any text editor.
- Translate units (Arabic / French / Tamazight) by copying and adding a
  `_ar.md` / `_fr.md` / `_tzm.md` suffix.
- Compose to PDF or DOCX with pandoc, e.g.
  `pandoc unit-1.md -o unit-1.docx`.
- Re-skin into a school template by editing the lesson-plan template in
  `docs/01-pedagogical-framework.md` (section 7).

---

## What changes year-on-year (maintenance cost is low)

Because the curriculum tracks the **official syllabus**, content does not
churn. The expected per-year edits are:

1. School-calendar dates in `annual_plan/pacing-guide.md` (week numbers,
   holidays).
2. Diagnostic results in `teacher_guide/baseline.md`.
3. New realia in worksheets (e.g. fresh news article for Unit 3 of 1AS).
4. Errata recorded in `docs/04-quality-assurance.md`.
