# Final-Three Research Question Audit — 2026-09-06 V9

**Target:** NAACL Main, calibrated against ACL / EMNLP / NAACL Main and especially Best / Outstanding work.  
**Authority:** supersedes V8 for active research-question ranking.  
**Rule:** active set contains **exactly three** candidates. Everything else is KILL / ARCHIVE unless a genuinely different scientific axis is discovered.

> **NO APPROVED PAPER MAINLINE YET.**
>
> The three active research questions are:
>
> 1. **AE — Actuality Entailment / Ability–Actuality Composition**
> 2. **CK — Finite Mutual Knowledge vs Common Knowledge**
> 3. **GRN — Goal-Relative Necessity / Anankastic Reasoning**

---

# 0. Why these three survive

The final-three bar is stronger than “no exact paper found.”

Each survivor must have all of:

1. a natural scientific object that predates our benchmark;
2. a one-minute research question;
3. a core RQ not already owned by modern LLM/NLP work;
4. a core claim space not reducible to a small missing benchmark cell;
5. competing accounts that make different predictions;
6. a shallow, auditable substrate;
7. multiple scientifically informative outcomes;
8. a plausible Main-scale growth path;
9. direct alignment with the kind of question selection seen in recent ACL/EMNLP high-level papers.

Recent ACL evidence that focused human cognitive / linguistic objects can be top-level NLP questions includes:
- ACL 2026 Best Paper, **The Imperfective Paradox in Large Language Models**;
- ACL 2026 Outstanding, **CxMP**;
- ACL 2026 Main, **CogToM**;
- ACL 2026 Best Theme, **CoSToM**;
- ACL 2026 Outstanding, **Mind the (DH) Gap!**.

The lesson is not to copy their experiment counts. It is to select a natural object whose model-side behavior can reveal a structural law.

---

# 1. Rank 1 — AE: Actuality Entailment / Ability–Actuality Composition

## 1.1 Research Question

> **How do language models compose modality and grammatical aspect when an agent’s ability and an event’s actual realization come apart?**

A sharper operational version:

> **Do LLMs preserve the distinction between “could/was able to do X” and “actually did X,” while also learning the genuine linguistic environments in which aspect turns an ability modal into an actuality inference?**

This is not a generic factuality benchmark.

The scientific object is the interaction:

```
modality / ability
×
viewpoint aspect
→
actuality inference
```

## 1.2 Why this is a natural scientific object

Actuality entailments are a mature formal-semantic puzzle.

A classic cross-linguistic pattern is:
- imperfective ability can describe a capacity that was never realized;
- corresponding perfective ability can force or strongly license the inference that the event actually occurred.

A 2025 *Annual Review of Linguistics* survey describes the phenomenon as a still-theoretically-active interaction between modality and aspect and notes unresolved questions that can discriminate existing analyses.

This is not an ontology invented for a benchmark.

References:
- https://www.annualreviews.org/content/journals/10.1146/annurev-linguistics-011724-121222
- https://academic.oup.com/book/45889/chapter/401433613

## 1.3 Paper Identity

**Focused scientific / behavioral linguistic discovery.**

Mechanism is optional for C1.  
Representation analysis becomes useful only if the behavioral law suggests a real modality–aspect dissociation.

## 1.4 High-Level Calibration

Closest paper identity anchor:

### ACL 2026 Best — The Imperfective Paradox in Large Language Models

That paper asks whether models compose aspect with lexical event structure and discovers a pervasive **Teleological Bias**: goal-oriented progressive events are incorrectly inferred to have completed, even under explicit cancellation.

AE is adjacent but not the same axis.

Imperfective Paradox:

```
progressive aspect
×
event class / telicity
→
does process entail completion?
```

AE:

```
modal ability / necessity
×
viewpoint aspect
→
does hypotheticality survive, or is actuality inferred?
```

Critically, the theoretical predictions can oppose a simple completion heuristic:
- progressive goal events generally do **not** license completion;
- some perfective modal constructions **do** license actuality.

This makes AE a direct test of whether LLMs have a compositional modality–aspect system or merely a global “goal events complete” prior.

Anchor:
- https://aclanthology.org/2026.acl-long.689/

## 1.5 Novelty assassination

Searches conducted:
- “actuality entailment” + LLM;
- “actuality entailment” + language model / transformer / NLP;
- “ability actuality” + LLM;
- modality × aspect + LLM;
- ACL Anthology searches around actuality inference.

Current result:

> **No modern LLM/NLP paper was located whose load-bearing RQ is actuality entailment or the modality × aspect composition that produces it.**

Nearest NLP work on factuality does not isolate this compositional axis.

The main threat is the ACL 2026 Imperfective Paradox paper, but its load-bearing factor is event class under progressive aspect, not modal force × viewpoint aspect.

## 1.6 Reviewer Kill Sentence

> **“This is just another aspectual entailment benchmark after the Imperfective Paradox paper.”**

### Why that compression is not currently valid

The two accounts make different predictions.

A model with only the previously discovered Teleological Bias can:
- hallucinate completion for telic/goal events in general;
- fail to condition that inference on modal type and aspect.

A model with genuine actuality-entailment competence must:
- preserve unrealized ability in non-AE environments;
- selectively infer realization in AE-licensing environments;
- handle modal/aspect contrasts even when event goal structure is matched.

The decisive experiment must include both phenomena so that a generic goal-completion bias cannot solve AE.

## 1.7 Competing hypotheses

**H1 — Compositional actuality-entailment competence**  
Model selectively derives actuality where modality × aspect licenses it.

**H2 — Modal preservation**  
Ability remains hypothetical everywhere; model under-generates genuine actuality inferences.

**H3 — Teleological over-actualization**  
Goal-directed complements are treated as realized regardless of the modal/aspect configuration.

**H4 — Morphological / lexical heuristic**  
Model memorizes frequent surface forms rather than computing the interaction.

## 1.8 Decisive prediction

Use matched event content while crossing:
- modal vs nonmodal;
- perfective vs imperfective;
- goal-oriented vs matched controls;
- AE-licensing vs non-AE modal flavors.

The strongest pilot includes at least one language with overt aspect morphology and human-validated examples.

A simple “can/could” English-only benchmark is **not** enough.

## 1.9 Naturalness / data

Use established naturally interpretable linguistic contrasts, not synthetic worlds.

Likely pilot:
- one overt-aspect language with strong AE diagnostics;
- a small English ability/actuality contrast only as secondary support;
- 30–60 independent lexical/event items;
- deterministic or human-normed entailment labels;
- manually audited translations / native-speaker validation.

A Main paper may later need multilingual evidence because the clearest phenomenon is cross-linguistic.

## 1.10 What would be trivial

- models know the word “able”;
- perfective morphology is decodable;
- “was able to” often correlates with successful events in corpora;
- explicit prompting with the linguistic rule improves accuracy;
- one language shows a small accuracy difference.

## 1.11 Main-scale claim architecture

Possible, not pre-claimed:

**C1 — modality–aspect structural law**  
Models systematically preserve, lose, or over-generate hypotheticality as a function of aspect.

**C2 — dissociation from teleological completion bias**  
The AE pattern cannot be explained by the ACL-2026-style goal-completion heuristic alone.

**C3 — model/training/language regime**  
The composition law differs systematically across reasoning vs conversational training, model families, or aspect systems.

Mechanism is optional unless it becomes explanatory.

## 1.12 Pilot kill rules

KILL if:
1. the phenomenon reduces to English lexical collocation;
2. the same error is fully predicted by generic telicity/Teleological Bias;
3. native-speaker / established linguistic gold is unstable;
4. the effect appears only under explicit metalinguistic instructions;
5. a new LLM paper is found that already makes modality × aspect actuality inference its core contribution;
6. the strongest result sentence is merely “LLMs sometimes confuse ability with actuality.”

## 1.13 Verdict

> **TOP ACTIVE CANDIDATE / MATERIAL DESIGN AUTHORIZED / NOT MAINLINE UNTIL PILOT LAW**

---

# 2. Rank 2 — CK: Finite Mutual Knowledge vs Common Knowledge

## 2.1 Research Question

Do not ask:

> “Can LLMs do Theory of Mind?”

Do not ask:

> “Can LLMs identify public information?”

Ask:

> **How do LLMs represent the qualitative boundary between finite mutual knowledge and genuine common knowledge, and what computation do they use to cross that boundary?**

The key scientific distinction is:

```
arbitrarily deep but finite nested knowledge
≠
common knowledge
```

No finite stack of “A knows B knows…” logically becomes common knowledge.

## 2.2 Why it matters

Common knowledge is not an esoteric ToM depth benchmark. It is a distinct coordination resource.

Two agents can both know a fact, and know that each other knows it, while still lacking the public/common state needed for coordination.

This matters directly to:
- multi-agent coordination;
- group communication;
- public announcements;
- shared plans;
- negotiation;
- common-ground formation.

## 2.3 Human scientific anchor

De Freitas, Huang & Pinker (PNAS 2026) provide a new human theory and experiment:
- humans have capacity-limited recursive mentalizing;
- publicly salient events license an intuitive common-knowledge state;
- humans also show recursion collapse and finite-to-common extrapolation errors.

This is a **calibration anchor**, not an LLM novelty kill.

Reference:
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13486529/

## 2.4 Paper Identity

**Scientific / behavioral cognitive discovery**, with optional downstream coordination.

Mechanism is not mandatory for C1.

## 2.5 Direct LLM neighbors

### OmniToM (2026)

Explicitly models actor beliefs, recursive order, truth status, and knowledge access, but caps the schema at finite recursive orders and does not make the finite-mutual-vs-common boundary its load-bearing question.

### CoSToM — ACL 2026 Best Theme

Studies ToM representations and causal steering, not common-knowledge closure.

### Approximate common-knowledge multi-agent workshop work

Studies whether interacting agents converge to approximate common knowledge through alignment / acknowledgment / stability. This is different from the cognitive question of whether a single LLM represents **public common knowledge** as qualitatively distinct from any finite recursive state.

References:
- https://arxiv.org/abs/2605.26322
- https://aclanthology.org/2026.acl-long.421/

## 2.6 Reviewer Kill Sentence

> **“This is just another higher-order ToM / public-vs-private benchmark.”**

### Why that compression is not valid if designed correctly

Generic ToM predicts performance as a function of recursive depth.

CK asks whether:
- publicness creates a qualitatively different route to deep closure;
- finite reciprocal knowledge is incorrectly over-closed into common knowledge;
- public common knowledge behaves differently in downstream coordination even when shallow belief questions are matched.

A finite-depth ToM model and a public-compression model make different predictions on the same first-order facts.

## 2.7 Competing hypotheses

**H1 — Finite recursion only**  
Public knowledge is handled as another observed fact; nested-belief difficulty grows with depth.

**H2 — Public common-knowledge compression**  
Public observability triggers a special state supporting deep closure without explicit recursive expansion.

**H3 — Finite-to-common overclosure**  
Models incorrectly treat reciprocal or doubly reciprocal knowledge as if it were common knowledge.

**H4 — Recognition / coordination dissociation**  
Models classify the epistemic structure correctly but use the wrong state during coordination.

## 2.8 Decisive design

Matched information conditions:
1. Private
2. Reciprocal
3. Doubly Reciprocal
4. Public

Hold first-order proposition and who individually knows it fixed where possible.

Probe:
- finite depths;
- a meta-level arbitrary-depth/common-knowledge judgment;
- one downstream coordination consequence.

The pilot must distinguish **depth cost** from **public closure**.

## 2.9 Outcome robustness

All are scientifically informative:
- human-like public compression;
- no compression, only finite recursion;
- systematic overclosure;
- systematic underclosure;
- reasoning-model / conversational-model split;
- explicit-ToM vs coordination dissociation.

A mere replication of the human publicness effect is weaker, but the RQ survives because the model-side computation remains identifiable.

## 2.10 What would be trivial

- models know who saw an announcement;
- public is easier than private;
- deeper nested sentences are harder;
- prompting “this is common knowledge” improves performance;
- a ToM feature is linearly decodable.

## 2.11 Main-scale claim architecture

Potential:

**C1 — common-knowledge boundary law**  
LLMs cross or fail to cross the finite-mutual/common boundary in a systematic way.

**C2 — coordination consequence**  
The epistemic-state law predicts a discontinuity/error in actual coordination, not merely QA.

**C3 — training / family regime or causal mechanism**  
Only if the discovered C1 suggests one.

## 2.12 Pilot kill rules

KILL if:
1. all results reduce to generic recursion-depth degradation;
2. the model only responds to lexical “public/everyone” cues;
3. public/private recognition fully explains all outcomes;
4. no distinction survives natural nontechnical scenarios;
5. a new paper directly isolates finite mutual knowledge vs common knowledge in LLMs;
6. the strongest sentence is “LLMs are better on public information.”

## 2.13 Verdict

> **ACTIVE CANDIDATE / SMALL DISCOVERY PILOT AUTHORIZED / NOT MAINLINE UNTIL PILOT LAW**

---

# 3. Rank 3 — GRN: Goal-Relative Necessity / Anankastic Reasoning

## 3.1 Research Question

> **When natural language says “If you want X, you must/need to do Y,” do LLMs interpret Y as a goal-relative necessary means, or do they collapse the statement into an unconditional obligation or ordinary conditional?**

The deeper object is:

> **Can an LLM bind necessity to the goal that makes it necessary?**

This is a direct language–planning interface question.

## 3.2 One-example

Suppose:
- the user wants to reach a destination;
- only Route A reaches it.

Then:

> If you want to reach the destination, you need to take Route A.

expresses a goal-relative means relation.

If:
- the user abandons the destination goal, or
- Route B is added and also reaches it,

the necessity of Route A changes.

An unconditional deontic “You must take Route A” does not behave this way.

## 3.3 Scientific anchor

Formal semantics calls the core construction an **anankastic conditional**.

A 2026 *Linguistics and Philosophy* paper continues to develop the theory, showing that the object is scientifically active rather than a closed textbook curiosity.

The literature characterizes the construction as expressing that the consequent is a necessary condition for realizing the goal expressed in the antecedent.

References:
- https://link.springer.com/article/10.1007/s10988-026-09459-x
- https://semprag.org/article/view/sp.9.8

## 3.4 Paper Identity

**Focused scientific / behavioral linguistic discovery with use-inspired agent relevance.**

No mechanism needed for C1.

## 3.5 High-Level alignment

This candidate has the same legitimate paper identity as:
- ACL 2026 Best **Imperfective Paradox**: classic formal-semantic distinction → structural LLM law;
- ACL 2026 Outstanding **CxMP**: controlled form–meaning minimal pairs → constructional understanding law.

It also connects naturally to agent planning because anankastic modality expresses necessary means relative to goals.

## 3.6 Novelty assassination

Searches conducted:
- “anankastic conditional” + LLM;
- anankastic + transformer / language model;
- means-end conditionals + LLM;
- teleological modality + LLM;
- ACL Anthology searches.

Current result:

> **No modern LLM/NLP paper was located whose core RQ is whether necessity is represented as goal-relative means-end necessity.**

Important neighbors do not own this axis:

### ModalBench — ICLR 2026 workshop

Tests Kripke modal/deontic logic, including K/T/S4/S5/D and deontic paradoxes.

It does not test whether a natural-language necessity modal is **teleologically restricted by an agent goal**.

### EACL 2026 deontic Wason

Compares deontic vs descriptive conditionals and human-like matching biases.

It does not study goal-conditioned means-end necessity.

References:
- https://github.com/mujtabahasan/modalbench
- https://aclanthology.org/2026.eacl-short.42/

## 3.7 Reviewer Kill Sentence

> **“This is just deontic/modal reasoning or a small planning-precondition benchmark.”**

### Why that compression can be defeated

Deontic obligation and instrumental necessity make different predictions.

If the goal disappears:
- goal-relative necessity should disappear;
- an unconditional obligation need not.

If an alternative route appears:
- “must take A to achieve X” can become false;
- the action can remain permitted, useful, or even preferred.

A standard modal-logic/deontic benchmark does not test this binding.

A generic planner can know a route graph without testing whether the **linguistic necessity operator** is scoped to the goal.

## 3.8 Competing hypotheses

**H1 — Goal-relative means-end semantics**  
Necessity updates with the goal and the feasible means structure.

**H2 — Deontic leakage**  
“must/need” is stored as a global obligation and persists after the goal disappears.

**H3 — Ordinary conditional heuristic**  
Model treats antecedent desire as a factual condition rather than a goal that sets the modal ordering.

**H4 — Lexical advice heuristic**  
Model follows familiar “if you want…” templates without representing necessary means.

## 3.9 Decisive design

Use shallow explicit action graphs / ordinary scenarios.

Cross:
- goal active vs abandoned;
- unique necessary route vs alternative route added;
- anankastic vs near-anankastic surface-matched cases;
- strong “must/have to” vs weak “should” where theory predicts different force.

Queries:
- is Y still required?
- does not doing Y violate a rule, or merely prevent X?
- what changes when goal X is dropped?
- what changes when an alternative path exists?

Gold should be derived from the explicit task structure, not world knowledge.

## 3.10 Naturalness

Examples can come from:
- travel routes;
- software setup;
- cooking;
- document submission;
- device configuration;
- ordinary multi-step tasks.

No invented institutional ontology is needed.

The research object appears constantly in assistant instructions:
- “If you want to sync, you need to sign in.”
- “If you want to submit, you have to attach the file.”

Misreading these as unconditional obligations produces concrete agent failures.

## 3.11 Outcome robustness

Interesting outcomes:
- correct goal-relative semantics;
- persistent deontic leakage;
- failure to revise necessity after an alternative appears;
- correct explicit route reasoning but wrong linguistic inference;
- reasoning/conversational model split;
- strong-vs-weak modal asymmetry.

## 3.12 What would be trivial

- the model can find a path in a graph;
- the model knows “must” is stronger than “should”;
- explicit “Y is necessary for X” is answered correctly;
- adding more instructions improves planning;
- deontic logic formulas are solved.

## 3.13 Main-scale claim architecture

Possible:

**C1 — goal-binding law**  
LLMs systematically bind—or fail to bind—natural-language necessity to the goal that licenses it.

**C2 — dynamic update / deontic leakage**  
Goal cancellation and alternative means reveal whether necessity is represented structurally or persists as an obligation-like residue.

**C3 — downstream agent consequence**  
The same law predicts unnecessary actions, refusal, or overconstraint in realistic instruction-following tasks.

## 3.14 Pilot kill rules

KILL if:
1. performance reduces to graph reachability;
2. the effect is just the lexical strength of “must” vs “should”;
3. natural paraphrases eliminate the structure;
4. only metalinguistic questions expose the difference;
5. a modern LLM paper is found whose core claim already concerns anankastic / goal-relative necessity;
6. the strongest sentence is merely “LLMs make mistakes on anankastic conditionals.”

## 3.15 Verdict

> **ACTIVE CANDIDATE / MATERIAL DESIGN AUTHORIZED / NO TARGET-MODEL PILOT UNTIL FINAL HUMAN-GOLD AUDIT**

---

# 4. Final-three comparison

| dimension | AE | CK | GRN |
|---|---|---|---|
| natural scientific object | **very high** | **very high** | **very high** |
| direct LLM core-RQ novelty | **highest** | **high, crowded ToM neighborhood** | **very high** |
| one-minute intelligibility | high | high | **very high** |
| exact competing predictions | **very high** | **very high** | **very high** |
| data simplicity | high, but multilingual validation needed | **very high** | **very high** |
| outcome robustness | **very high** | **very high** | high |
| community importance | high | **very high** | high |
| Main-scale growth path | **very high** | **very high** | high–very high |
| strongest risk | adjacency to Imperfective Paradox | crowded ToM / human-replication compression | “just deontic/planning” compression |

Force ranking:

1. **AE** — cleanest combination of direct novelty, precise theory, and top-paper-aligned paper identity.
2. **CK** — largest scientific/agentic importance; slightly higher neighboring-literature risk.
3. **GRN** — strongest newly found natural language–planning interface; needs final human-gold/material audit before pilot.

---

# 5. Killed directions are not reserves

The following are **not active candidates** and must not appear in current ranking:

- A — opportunity-conditioned preference evidence;
- B — competence × reporting fidelity;
- L — source-conditioned confidence semantics;
- EPM — perspective-relative epistemic modality;
- HWP — hypothetical-world persistence;
- FC — free-choice inference;
- ambiguity / maintain-multiple-interpretations;
- DM / disposition–manifestation;
- IF / institutional fact;
- structured-source-model variants;
- causal-credit-from-experience variants;
- prospective-memory variants;
- previously killed C / D / preference drift / preference uncertainty / inverse-planning lanes.

Reasons are recorded in:
- `archive/KILLED_RQ_LEDGER_2026-09-06_V9.md`.

Do not keep these as “backup candidates.”

---

# 6. Current experiment boundary

Allowed next work:

### AE
- material design;
- native-speaker / established-example gold validation;
- deterministic analyzer;
- **no target-model run until material audit is complete**.

### CK
- existing small CK-P1 may proceed after re-auditing the material against V9 C1;
- add a downstream coordination query only if it remains clean and does not inflate P0.

### GRN
- material design and human-gold audit only;
- no target-model run until the anankastic / near-anankastic contrasts are independently validated.

Not authorized:
- mechanism work;
- SAE / patching / steering;
- LoRA / RL;
- large model zoo;
- resurrection of killed candidates.

---

# 7. Post-pilot rule

For each of the three:

1. write one sentence beginning **“Models …”**;
2. search the literature for that exact structural law;
3. compare the law against Best / Outstanding / strong Main papers;
4. KILL if the sentence is trivial, already owned, or benchmark-local;
5. only then promote one question to the paper mainline.

> **Three active questions. Zero backups. Zero approved mainline until a pilot produces a real, novel law.**
