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
`pass-with-edits-applied` = approved with required edits, edits now in place.

### Phase 1 — Foundations

| Deliverable | Status | Notes |
|-------------|--------|-------|
| Master curriculum map (`docs/00-curriculum-map.md`) | **pass-with-edits-applied** (2026-06-17) | User verdict: PASS WITH MINOR EDITS. All 4 required edits applied: (1) inferred content tagged `pending verification from official teaching map`; (2) Source Hierarchy added to `02-source-attribution.md`; (3) FROZEN REFERENCE notice added at top; (4) Stream Integrity Rule added to `01-pedagogical-framework.md`. |
| Pedagogical framework (`docs/01-pedagogical-framework.md`) | pass-with-edits-applied | Stream Integrity Rule (Section 1.b) added; competency-definition disclosure added. |
| Source attribution (`docs/02-source-attribution.md`) | pass-with-edits-applied | Source Hierarchy section added at top (4-level priority). |
| Implementation plan (`docs/03-implementation-plan.md`) | pass-with-edits-applied | Phase 2B+ row updated to forbid derivation. |
| QA log (this file) | pass-with-edits-applied | Phase 2A approval recorded. |

### Phase 2A — 2AS Foreign Languages standalone (current focus)

Per project decisions (2026-06-17), Phase 2 is **scoped down to Phase 2A**:
the 2AS Foreign Languages stream as a self-contained, independently
authored model. **No derivation work for any other stream — ever
(Stream Integrity Rule).** All other streams will be independently
authored from the official source documents on their own merit.

| Grade | Stream | Yearly plan | Scope & sequence | Assessment calendar | Competency map |
|-------|--------|-------------|---------------------|----------------------|-----------------|
| **2AS** | **Foreign Languages** | draft (edits applied) | draft (edits applied) | draft (edits applied) | draft (edits applied) |

> Note: pacing guide was authored in error (5th deliverable) and was
> deleted on 2026-06-17 to match the user's approved scope of 4
> deliverables. Day-by-day pacing is deferred to a later phase.

### Phase 2B+ — All other streams (independently authored, not derived)

Per the **Stream Integrity Rule** (`docs/01-pedagogical-framework.md`
Section 1.b), every other stream below will be authored **independently
from the official source documents**, not derived, mapped, trimmed, or
transformed from 2AS Foreign Languages. Build order is TBD pending
Phase 2A validation.

| Grade | Stream | Status |
|-------|--------|--------|
| 2AS | Letters & Philosophy | pending — independent author |
| 2AS | Sciences / Maths / Tech-Maths | pending — independent author |
| 2AS | Management & Economy | pending — independent author |
| 1AS | Common Core Letters | pending — independent author |
| 1AS | Common Core Sciences & Tech | pending — independent author |
| 3AS | Foreign Languages | pending — independent author |
| 3AS | Letters / Philosophy | pending — independent author |
| 3AS | Sciences / Maths / Tech-Maths / Mgmt-Econ | pending — independent author |

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
| 2026-06-17 | Phase 1 governance edits required by user (PASS WITH MINOR EDITS) | medium | **Resolved.** All 4 edits applied: (1) inferred content tagged `pending verification from official teaching map`; (2) Source Hierarchy added to `02-source-attribution.md` (priority: Teaching Map > Annual Distribution > Textbook sequence > Derived inference); (3) FROZEN REFERENCE notice on `00-curriculum-map.md`; (4) Stream Integrity Rule added to `01-pedagogical-framework.md`. |
| 2026-06-17 | Pacing guide authored beyond the 4 approved Phase 2A deliverables | low | **Resolved.** `curriculum/2AS/annual_plan/pacing-guide.md` deleted; cross-references in the 4 surviving files updated. Day-by-day pacing deferred to a later phase. |
| 2026-06-17 | Derivation between streams was previously open as a possibility | medium | **Resolved.** Stream Integrity Rule forbids derivation; every stream is now an independent pedagogical pathway authored from official sources. QA log and implementation plan updated. |
| 2026-06-17 | Textbook-order ambiguity for FL stream (Annual Distribution prescribes 1→2→3→4→7→6; textbook numerical TOC would be 1→2→3→4→6→7) | medium | **Open.** Surfaced to user for decision. Phase 2A currently follows the Annual Distribution order (priority-2 source) per the Source Hierarchy. If the user means strict textbook numerical TOC order, all 4 Phase 2A deliverables must be re-ordered (units 6 and 7 swapped). See response after Phase 2A commit. |
| Phase 0 | 2AS textbook Unit 5 has no Teaching-Map page (source jumps from Unit 4 to Unit 6) | medium | **Decision (2026-06-17): skip entirely.** The 2AS package is authored as a 7-unit course covering textbook units 1, 2, 3, 4, 6, 7, 8. Textbook numbering preserved so teachers can match pages in *Getting There*. Cross-checked against the annual-distribution PDF — no stream's theme list depends on Unit 5. |
| Phase 0 | The three .pps decks are image-only — no text content recoverable beyond shape metadata | low | None needed; PDFs cover all syllabus-level content. |
| Phase 0 | Source documents do not specify lesson-by-lesson timing | low | When lesson plans are authored (Phase 5), defensible default ESA timings will be added, labelled as *pedagogical scaffolding* per the Source Hierarchy priority-4. |

---

## Sign-off

The user reviews this report at each pause point. When all units show `pass`
in all four phase columns, the curriculum is ready for adoption.
