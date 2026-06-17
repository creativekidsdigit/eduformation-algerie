# Pedagogical Framework

This document defines the **non-negotiable instructional model** the rest of
the curriculum is built on. It is a synthesis of (a) what the official
Algerian Teaching Map mandates, and (b) the standard CBA / Backward-Design /
Bloom's pedagogy the user requested.

---

## 1. Competency-Based Approach (CBA)

The Algerian secondary syllabus is officially organised around three
*communicative competencies*. They appear as **C1 / C2 / C3** at the head of
every unit aim in the Teaching Map (e.g. 1AS Unit 2: *"C1 = Interaction:
guessing & responding to a tale; C2 = production: expressing literary
preferences; C3 = interpretation: guessing"*).

| Code | Name | What the learner does |
|------|------|------------------------|
| **C1** | **Interaction** | Negotiates meaning live: asks, answers, justifies, responds, agrees, disagrees, requests, instructs |
| **C2** | **Production** | Produces an extended, organised oral or written text for a purpose and an audience |
| **C3** | **Interpretation** | Extracts, infers and interprets meaning from written or oral input |

Every objective, activity and assessment in this curriculum is tagged with
one of the three competency codes.

---

## 2. Backward Design (Wiggins & McTighe)

We design every unit in **three stages**, in this order:

1. **Identify desired results.** Take the official theme + project +
   productive language from the Teaching Map. Translate into 4–8 measurable
   Bloom's-tagged objectives.
2. **Determine acceptable evidence.** Decide *how* you will know each
   objective has been met before designing any activity. Each unit has at
   least: a project rubric, a unit test (R-W-L-S), formative checkpoints.
3. **Plan learning experiences.** Sequence Engage-Study-Activate lessons
   across the six textbook phases so that every activity advances at least
   one objective and gathers at least one piece of evidence.

The result is captured in a **Competency × Objective × Activity × Assessment**
alignment matrix at the head of each lesson.

---

## 3. Bloom's Taxonomy (revised, 2001)

| Level | Cognitive verb (sample) | Tied to which Algerian competency? |
|-------|--------------------------|-------------------------------------|
| Remember | recall, define, list, name | C1, C3 |
| Understand | explain, summarise, paraphrase, interpret | C3 |
| Apply | use, demonstrate, complete, perform | C1, C2 |
| Analyse | compare, differentiate, organise, attribute | C2, C3 |
| Evaluate | judge, justify, critique, defend | C1, C2 |
| Create | design, compose, produce, plan, construct | **C2 (especially the unit project)** |

Lessons with no objective above *Apply* are revised — every unit must touch
the upper half of the taxonomy at least once, because the unit project itself
sits in the **Create** band.

---

## 4. The official "Six A's of Project Design"

Quoted directly from the Teaching Map (page 5–6 of the source). These are
**not optional**: every unit project we ship is checked against the six A's.

1. **Authenticity** — the project emanates from a problem or question
   meaningful to the learner; the artefact has personal or social value
   beyond school.
2. **Academic Rigor** — leads to acquisition and application of discipline-
   central knowledge; develops higher-order thinking.
3. **Applied Learning** — solves a semi-structured real-world problem;
   develops team-work, technology, problem-solving, communication.
4. **Active Exploration** — significant time on field-based work; varied
   methods, media and sources; expectation of presentation.
5. **Adult Connections** — opportunities to meet and observe adults with
   relevant expertise; adult work becomes visible.
6. **Assessment Practices** — exemplars; clear milestones per phase; timely
   feedback; structured self-assessment with criteria the learner helped to set.

---

## 5. Engage – Study – Activate (ESA)

Quoted from the Teaching Map (page 7–8 of the source, Callum Robertson / BBC
English, adapted by Mr. Allouane).

| ESA stage | Purpose | Default timing in a 60-min lesson |
|-----------|---------|------------------------------------|
| **Engage** | Spark interest, activate prior knowledge, set the *why* | 10 min |
| **Study** | Focused work on a language form, function, or text feature | 25 min |
| **Activate** | Free, personalised use of *all* the language students know to complete a real task | 20 min |
| Closure / Reflection | Self-assessment, exit ticket | 5 min |

For 45-minute and 90-minute slots we provide ESA timings in the lesson plans.

---

## 6. The six textbook phases (every unit follows this cycle)

Extracted from the Teaching Map column structure, present in every unit page.

1. **Listen & Consider** — input phase 1 (oral text), discover language form.
2. **Read & Consider** — input phase 2 (written text), refine language form.
3. **Listening & Speaking (Your Turn)** — controlled & semi-controlled oral
   practice.
4. **Reading & Writing** — controlled & semi-controlled written practice.
5. **Write It Up** — guided production with a model.
6. **Write It Out** — free production, the project artefact.

This is the source of the unit-internal sequence we use in every grade.

---

## 7. Lesson-plan template (used in `lesson_plans/`)

```
TITLE
LEVEL  · STREAM  · UNIT  · LESSON N° · DURATION
PHASE (Listen & Consider | Read & Consider | …)
COMPETENCY (C1 / C2 / C3)
THEME
PRODUCTIVE LANGUAGE (grammar + functional expressions)
VOCABULARY focus
SKILLS focus (listening · speaking · reading · writing)
MATERIALS

OBJECTIVES (Bloom's-tagged)
  1. SWBAT <verb> <content> using <PL> in <context>. (Cx, Bloom: <level>)
  …

ALIGNMENT MATRIX
  | # | Competency | Objective | Activity | Assessment |

LESSON FLOW
  Warm-up                (5 min, Engage)
  Engagement activity    (10 min, Engage)
  Guided practice        (15 min, Study)
  Independent practice   (15 min, Activate)
  Reflection / closure   (5 min)
  Homework

DIFFERENTIATION
  · Struggling
  · ADHD-friendly
  · Advanced
  · Inclusive

EVIDENCE COLLECTED THIS LESSON  (what goes into the formative log)
```

---

## 8. Quality-assurance gates

A unit is considered "ready for classroom use" only when it passes the
following five gates (see `docs/04-quality-assurance.md` for the live report):

1. Curriculum alignment — every objective traces to an official competency.
2. Bloom's accuracy — verbs match the cognitive level claimed.
3. Assessment validity — every test item maps to at least one stated objective.
4. Competency alignment — every activity advances at least one of C1/C2/C3.
5. Gap detection — missing skills/strands flagged and addressed.

---

**This framework governs every artefact in `curriculum/`.**
