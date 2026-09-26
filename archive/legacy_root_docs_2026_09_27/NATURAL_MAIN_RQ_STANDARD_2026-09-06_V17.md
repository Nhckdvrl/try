# Natural Main-Level Research Question Standard — V17 (2026-09-06)

**Primary target: NAACL Main.**  
Calibration: ACL / EMNLP / NAACL Main, with Best / Outstanding / Best Theme papers weighted most heavily. Use ICLR / ICML / NeurIPS / AAAI only when the paper identity is genuinely close.

> **Current project state: CLEAN SLATE.**
>
> **NO APPROVED PAPER MAINLINE.**
>
> **NO TARGET-MODEL COMPUTE AUTHORIZED.**

This document supersedes the long multi-gate selection checklists as the current **working selection standard**.

The purpose is not to lower standards. It is to remove duplicated rules and make the real priorities impossible to miss.

---

# 0. One-sentence target

We want:

> **A natural, durable NLP/language problem; one genuinely new scientific axis inside it; trustworthy simple data and independent gold; a parent-level novel question with multiple informative outcomes; and a small decisive experiment that can naturally grow into a Main paper.**

Shorter:

> **Real object. New axis. Good data. New parent question. Decisive paper.**

The lab-search prior is:

> **Search locally, judge globally.**

Recent Sasano-Lab work tells us where natural questions tend to live. ACL / EMNLP / NAACL determine whether they are strong enough.

---

# 1. Real object: the question must be natural before it is clever

Start from a **real NLP/language object**, not from a method, model, benchmark, or newly invented term.

High-prior objects include:
- lexical / compositional semantics;
- factual and parametric knowledge;
- language understanding and inference;
- established linguistic phenomena;
- structured linguistic/NLP resources;
- representation or generation processes when tied to a concrete language question;
- classical NLP tasks whose measurement or assumptions may be wrong.

The RQ should be explainable in one ordinary sentence.

A good test:

> **If “LLM”, model names, and dataset names disappear, is there still an important question?**

Another good test:

> **Would an ACL/EMNLP/NAACL reviewer understand why this matters before seeing our result?**

Prefer questions that feel like:
> “Yes, this is a real thing, and I do not already know the answer.”

Avoid:
> “Technically this distinction exists, but why would anyone ask this?”

**Durability is part of naturalness.** If the question dies when a current API/model/framework changes, it is weak by default.

---

# 2. New axis: find one meaningful relation that existing work hides

A candidate needs **one clear new scientific axis**, not many clever distinctions.

Strong recurring shapes:

### A. Separate two factors currently conflated
Example identity:
> factual knowledge of an entity vs access through one surface name.

### B. Replace a questionable measurement/unit
Example identity:
> hard sense count vs contextual diversity;
> whole-hypothesis NLI vs atomic inferences.

### C. Test a structural relation or competing account
Example identity:
> compositional semantics vs a learned heuristic;
> shared abstract syntax vs construction-specific processing.

### D. Revisit an old problem only when a load-bearing assumption changed
Not:
> old task + LLM.

Required:
> old conclusion depended on assumption A;
> modern models invalidate/change A;
> therefore a prediction, measurement, or optimal method changes.

The key requirement is **scientific tension before compute**.

Write two plausible accounts:

> **Account A predicts X.**  
> **Account B predicts Y.**

Both must be reasonable before seeing results.

If the setup is merely:

> correct behavior = X; failure = Y,

then it is usually a benchmark, not yet a scientific question.

Also avoid generic:
- probe A vs probe B inconsistency;
- verbal vs numeric gap;
- “does the model know textbook distinction X?”;
- “can the model do old task Y?”

A structural relation is useful only when it serves a new parent question. Mathematical elegance cannot rescue an occupied or unimportant question.

---

# 3. Good data: data and gold must be believable before the experiment

**Data is a first-order selection criterion, not implementation detail.**

Preferred order:

### Best
**Existing natural dataset / corpus / resource that already contains the needed variation.**

Examples of the desired shape:
- Wikipedia redirects;
- FrameNet-style relations;
- naturally annotated lexical ambiguity;
- existing speech/text/resource alignments.

### Also strong
**Published human or linguistic experimental materials.**

This is especially useful for semantics, syntax, psycholinguistics, and classical laws.

### Acceptable when necessary
**Small controlled stimuli grounded in established linguistic theory or formal rules**, with independently defensible gold.

Controlled data is not automatically bad. The problem is **author-created worlds whose labels and relevance exist only because we invented them**.

Default negative prior:
- large template-generated datasets;
- bespoke synthetic worlds/ontologies;
- LLM-generated examples as the main evidence;
- LLM-generated questions + LLM judge as gold;
- complex construction needed only to force a contrast.

Two hard questions:

> **Did the scientific object exist before our hypothesis?**

> **Can the gold be justified without asking the same kind of model we are evaluating?**

Gold should preferably come from:
- existing annotations/resources;
- human judgments;
- published linguistic analysis;
- formal derivation;
- deterministic algorithms;
- independent corpus evidence.

If data validity is unclear, **KILL before compute**.

---

# 4. New parent question: novelty must survive reviewer compression

Do not search for an unmatched title.

Search for ownership of:
- the parent RQ;
- decisive prediction;
- core scientific conclusion;
- measurement reformulation;
- causal estimand;
- old-assumption rewrite.

For every candidate write:

> **“This is just ______.”**

Then try to defeat it.

A valid rebuttal must rely on a genuinely different:
- scientific quantity;
- prediction;
- structural relation;
- measurement;
- causal claim;
- theoretical conclusion.

Not merely:
- another dataset;
- another language;
- another model;
- more scale;
- better controls;
- a cleaner equation;
- activation patching added later.

Minimum literature calibration before pilot:
- ~3 strong same-identity ACL/EMNLP/NAACL papers;
- nearest direct collisions;
- older theoretical/task parent when relevant.

**Local fit never overrides novelty.** A topic can look perfect for Sasano Lab and still be killed immediately by a close paper.

---

# 5. Decisive paper: simple experiment, informative outcomes, natural growth

A strong candidate should not require a giant engineering project to become interesting.

Before compute, we should be able to imagine:

### C1 — Core answer
The new axis/law/measurement result.

### C2 — Why / boundary
A principled moderator, control, causal test, or failure explanation.

### C3 — Consequence
A revised interpretation, evaluation rule, theoretical implication, or method that follows naturally from C1.

This is **claim architecture**, not experiment count.

Do not fill a paper with:
- ten more models;
- ten more benchmarks;
- many prompts;
- languages added only for scale;
- mechanism analysis that does not change the claim.

### Outcome robustness

Before pilot, list plausible outcomes.

A candidate is healthy when several outcomes teach us something:
- old account survives;
- new account wins;
- a principled boundary appears;
- architecture/training changes the regime;
- a plausible theory is falsified.

Danger:
> only one surprising positive effect creates a paper.

### Evidence depth

The evidence must match the claim.

- If the claim is behavioral/measurement: strong controls, decomposition, robustness may be enough.
- If the claim is causal/mechanistic: use causal interventions, not only probes/correlations.
- If the claim is a classical law: derive and test the relevant law/assumption.
- If the claim is resource/evaluation methodology: validate the measurement and downstream consequence.

**Mechanism is an escalation path, not a rescue device for a weak RQ.**

### Workload

Prefer:
> **small but decisive.**

Strong negative prior for projects that require, before the question is even established:
- building a large agent system;
- collecting massive new annotations;
- constructing a giant benchmark;
- training many large models;
- large-scale RL;
- complex multilingual resource construction.

---

# 6. The five hard gates

A candidate is allowed to reach a pilot only if all five are clearly YES:

1. **REAL OBJECT** — Is the question naturally important and durable?
2. **NEW AXIS** — Is there one non-obvious relation with at least two plausible accounts?
3. **GOOD DATA** — Do we have simple, credible data and independent gold?
4. **NEW PARENT** — Does parent-level novelty survive the “This is just X” attack?
5. **DECISIVE PAPER** — Are multiple outcomes informative, and can C1→C2→C3 grow naturally with manageable work?

If one is clearly NO:

# **KILL**

Do not “run a small experiment and see.”

Compute comes after selection.

---

# 7. Immediate kill signals

Default KILL or very strong negative prior when:

- importance requires a newly invented concept/name;
- RQ is “does the model know X ≠ Y?”;
- the only interesting outcome is an unexpected failure/bias;
- the main dataset must be invented specifically for the hypothesis;
- gold depends on LLM-as-judge or author intuition;
- closest parent paper already owns the scientific proposition;
- novelty is only dataset/model/language/prompt/scale;
- mechanism is being added to make a weak phenomenon look deep;
- project requires huge infrastructure before a decisive answer exists;
- the topic is a fast-moving agent/RL/prompt/API race without a durable scientific axis;
- reviewer can naturally compress it to a crowded generic category.

---

# 8. Preferred search region

Use recent Sasano-Lab work as a **search prior**, not a template.

Highest priority:
- lexical semantics and semantic access;
- compositional/implicit meaning;
- factual/parametric knowledge;
- linguistic inference;
- established linguistic phenomena;
- structured semantic/NLP relations;
- evaluation/measurement units inside stable NLP tasks.

Conditional:
- causal interpretability;
- diffusion/generation dynamics;
- efficiency/compression;
- Japanese-specific phenomena.

Only pursue the conditional lanes when a strong concrete object already exists.

Low priority by default:
- generic agent workflows;
- LLM-as-judge/annotator;
- generic RAG;
- prompt tricks;
- broad cognitive-bias transplantation;
- behavioral-economics phenomenon hunting;
- typology/documentation policy;
- bespoke synthetic worlds;
- model-specific feature hunting.

---

# 9. What recent strong papers teach us

The point is their **paper shape**, not their topic.

- **ACL 2026 Best — The Imperfective Paradox in Large Language Models**  
  One classic semantic phenomenon; compositional semantics competes with a teleological heuristic.

- **ACL 2026 Outstanding — CxMP**  
  A familiar linguistic evaluation conflated grammatical acceptability with understanding constructional meaning.

- **ACL 2026 Main — RedirectQA / Revisiting Non-Verbatim Memorization**  
  Natural Wikipedia redirects separate possession of entity facts from access through a particular surface form.

- **EMNLP 2025 Outstanding — Generative or Discriminative?**  
  A classical result from simple model families is re-examined because modern architectures change the relevant regime.

- **EMNLP 2025 Outstanding — Causal Interventions Reveal Shared Structure Across English Filler–Gap Constructions**  
  A concrete syntactic object plus causal internal evidence changes what can be said about linguistic structure.

- **NAACL 2025 Outstanding — NLI under the Microscope**  
  A long-standing task becomes scientifically more informative by changing the unit of analysis to atomic inferences.

- **ACL 2025 Outstanding — A New Formulation of Zipf's Meaning–Frequency Law through Contextual Diversity**  
  The old scientific law remains the object; the new contribution is a better operationalization of “meaning.”

Common denominator:

> **concrete object + one overlooked axis + credible measurement/data + conclusion that changes how we understand the object.**

---

# 10. Pre-pilot candidate card

No candidate may receive compute until this fits on one page:

**RQ — one sentence**  
What exactly are we asking?

**Why ACL/NLP cares — two sentences max**  
Why is the object already important?

**A vs B**  
What two plausible accounts make different predictions?

**Data + gold**  
What exact existing/natural/published data will we use? Who defines the gold?

**Closest parent + reviewer compression**  
What is the nearest paper? “This is just ____.” Why is that false?

**Outcome map**  
What do positive / null / heterogeneous / reverse outcomes teach us?

**Main growth**  
What are C1, C2, C3?

**Minimum decisive pilot**  
What is the smallest experiment capable of killing or promoting the candidate?

If the card becomes complicated, the topic probably is too.

---

# 11. Governing principles

> **The object should exist before us.**

> **The question should be understandable before the method.**

> **The data should be trustworthy before the experiment.**

> **The tension should exist before the result.**

> **The new axis should change understanding, not merely add another benchmark dimension.**

> **Novelty belongs to the parent scientific question, not the wording or dataset.**

> **Use the simplest evidence strong enough for the claim.**

> **Search locally, judge globally.**

> **The question should look important to ACL / EMNLP / NAACL before it looks clever to us.**
