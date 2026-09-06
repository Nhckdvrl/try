# Sasano-Lab Local-Prior RQ Search Reset — 2026-09-06 V16

**Target:** NAACL Main, calibrated against ACL / EMNLP / NAACL Main and especially Best / Outstanding / Best Theme papers.

> **NO APPROVED PAPER MAINLINE.**
>
> **NO TARGET-MODEL COMPUTE AUTHORIZED.**

V16 changes the **candidate generator**, not the scientific acceptance bar.

The V14–V15 search became too global:
- Bayesian behavior / cognitive-economics style questions;
- typological-science robustness;
- language-documentation resource policy;
- generic scientific-measurement / old-problem-new-method search.

These directions were not invalid in principle, but they moved too far away from the kinds of concrete NLP/language objects that Sasano Lab repeatedly turns into tractable research questions.

V16 therefore introduces a **local-prior → high-level-alignment** search order:

> **Use recent Sasano-Lab research to constrain where to search.**
>
> **Then use ACL / EMNLP / NAACL Main / Outstanding to decide whether a candidate is strong enough.**

Local style is a search prior, **not** a quality ceiling.

---

# 1. Recent lab audit: what people are actually studying

The audit focused on recent activity in:
- r_hamdi
- r_kisako
- r_oshika
- r_kurauchi

and other r_* channels with research progress/reports in roughly the last month, including:
- r_guo
- r_yano
- r_kan
- r_fujiwara
- r_han
- r_tsujimoto
- plus recent camera-ready/progress activity in r_utami.

The goal is **not to copy labmates' topics**. Their work is used only to infer the lab's natural problem scale, data style, and acceptable paper identities.

---

# 2. Concrete examples and the problem shapes they reveal

## 2.1 Hamdi — semantic/ontological distinction first, mechanism second

Recent lines include:

### Real vs fictional entities

Natural question:

> Does an LLM internally distinguish whether an entity exists in the real world or is fictional, separately from what it knows about the entity?

The work uses:
- well-known real/fictional entities across domains;
- linear probes / SAE analyses;
- causal interventions;
- behavioral controls.

The key point is not “use SAE.”

The scientific object is:
> **real-vs-fictional status**

and the behavioral consequence is natural:
> whether a model corrects a false premise or plays along with it.

### Random choice

Another line studies whether arbitrary/random choices correspond to a decodable choice state and whether that state can be causally controlled.

Again:
> **a concrete behavior/state first; mechanism follows.**

### Advisor signal

Recent Sasano comments repeatedly push paper organization toward:

1. What is the research question?
2. How was it investigated?
3. What was found?
4. Why does it matter?

Technical method must not become the paper identity.

---

## 2.2 Kisako — one natural resource axis over familiar techniques

Paper:

> **When Is 0.1% Enough? Analyzing the Combined Effects of Dimensionality Reduction and Quantization on Text Embedding Compression**

The individual techniques are not claimed as novel.

The contribution is the interaction of:
- dimensionality;
- quantization;

under a common:
> **bits × dimensions storage budget**

across task families.

This is a useful local shape:

> **known task + known methods + one natural joint axis / trade-off**

But it is also a warning:
- the work was considered interesting locally;
- EMNLP still rejected it.

Therefore:

> **systematic combination/ablation is not sufficient for our NAACL Main target unless there is a stronger structural law, prediction, or decision consequence.**

---

## 2.3 Oshika — decompose a real NLP artifact into a missing structural decision

Accepted Japanese journal work:

> **Optimal placement of cited papers for automatic related-work generation**

Instead of “generate related work” as one giant task, the work isolates:

> given a set of cited papers, how should citations be grouped and ordered into a coherent related-work structure?

The reviewer feedback is especially informative:
- a human-written related-work section is not necessarily the unique gold;
- multiple good rhetorical structures may exist;
- rhetorical moves matter:
  - introduce field;
  - organize prior work;
  - identify gap;
  - position own work.

Current doctoral work also uses multiple existing citation-function / citation-intent datasets with incompatible label inventories and studies transfer to unseen label schemes.

The transferable lesson is:

> **Take a familiar pipeline and isolate a structurally meaningful sub-decision that existing evaluation collapses.**

Not:
> “build a bigger scientific-writing agent.”

---

## 2.4 Kurauchi — narrow language task + architecture-enabled observation

Recent achievements include:

> **Generation of detailed kanji readings using LLMs**

which received an IPSJ Yamashita Memorial Research Award.

A newer research line asks:

> **When does compositional semantic information form during masked diffusion language-model generation?**

The intended distinction is among:
- surface token appearance;
- lexical commitment;
- semantic emergence;

using concrete linguistic objects such as:
- negation scope;
- temporal/event ordering.

This is an important problem shape:

> **A new model architecture creates a new observable axis that separates two processes previously entangled.**

This is much more concrete than generic “Old Problem / New Method.”

The model primitive matters only because it creates a precise measurement opportunity.

---

## 2.5 Yano — established linguistic theory → one explicit model capability

Recent paper:

> **FrameBench: A Language Understanding Benchmark Based on Frame Semantics**

Question:

> Can models make the implicit semantic enrichment licensed by frame semantics and distinguish the frame evoked by the same verb in different contexts?

Important ingredients:
- established linguistic theory;
- English/Japanese;
- FrameNet-style resources;
- native-speaker verification;
- a concrete comprehension capability.

This is close to the paper identity we should search around.

---

## 2.6 Kan — real lexical-semantic ambiguity, not generic cognitive bias

Current work studies:

> **figurative vs literal interpretations of idioms**

with:
- MAGPIE as a natural idiom dataset;
- probing/causal methods;
- concern about synthetic candidate sets and fixed templates.

A recent EACL 2026 long paper is already extremely close, and Sasano explicitly warned about this collision.

This gives two lessons:

1. lexical/semantic ambiguity is a natural lab object;
2. direct literature collision must kill/rewrite quickly even when the topic fits the lab perfectly.

---

## 2.7 Han Yi — structured semantic-resource relation inference

Current task:

> **(child frame, relation) → parent frame**

for FrameNet relations such as Inheritance / Using.

The work:
- compares embedding/relation-mapping/classifier/cross-encoder/LLM retrieval;
- explicitly tests whether the LLM simply memorized FrameNet relations from pretraining;
- considers completion of existing and newly constructed frame resources.

Transferable shape:

> **existing structured linguistic resource + missing relation + clean externally defined target**

But generic “LLM completes a knowledge graph/resource” is not enough for us; Main-scale requires a stronger structural insight.

---

## 2.8 Guo — explicit vs implicit information in a natural communication artifact

Recent work builds annotation rules over lecture speech/slides and distinguishes:
- lecture discourse;
- unrelated content;
- on-slide content;
- figure explanation;
- implicit educational content.

The underlying object is concrete:

> **What useful instructional content exists in speech but is not explicitly written on the slide?**

Again:
> a naturally occurring information relation, not a generic agent task.

---

## 2.9 Fujiwara — learning dynamics under controlled expression form

Current pilot compares acquisition of the same meaning expressed by:
- common words;
- difficult words;
- emoji;

and asks how quickly/through what evidence the meaning is learned.

The important lesson is not this exact synthetic setup—the current materials themselves expose naturalness risks.

The useful shape is:

> **hold intended meaning constant, vary a linguistically meaningful access form, and study acquisition/access differences.**

For our project this shape is acceptable only when data/gold can be made externally natural.

---

## 2.10 Tsujimoto — a very small overlooked factor in factual knowledge

A current thesis seed asks whether factual knowledge accuracy for a target word/entity is influenced by the frequency of semantically related superordinate/subordinate terms.

The motivating ACL 2026 Main paper **RedirectQA** is especially important:
- standard factual recall is normally tested under one canonical surface form;
- RedirectQA uses naturally existing Wikipedia redirects;
- it separates entity-level frequency from surface-form frequency;
- the paper finds both matter, with entity frequency contributing beyond surface frequency.

This is almost the ideal V16 shape:

> **familiar important task + one previously confounded natural variable + natural external data + a result that changes how the task should be measured/interpreted.**

Do not copy Tsujimoto's specific hypernym/hyponym question.

---

# 3. What Sasano-Lab research is actually clustered around

The recent topic ecology is much narrower than V14–V15 implied.

## Cluster A — lexical / semantic / factual knowledge

Examples:
- real vs fictional;
- literal vs figurative idiom interpretation;
- frame semantics;
- factual knowledge under surface variation;
- related-word frequency;
- meaning acquisition.

## Cluster B — structured linguistic/NLP resources and relations

Examples:
- FrameNet frame relations;
- citation functions and citation placement;
- lecture SCUs / slide–speech relations;
- detailed kanji readings.

## Cluster C — representation / generation process

Examples:
- causal internal representation;
- random choice states;
- diffusion-time semantic emergence;
- embedding compression.

These clusters all stay close to:
> **language understanding, lexical/semantic structure, factual knowledge, structured NLP resources, representation, and generation.**

They are far closer to Sasano Lab's center of gravity than:
- broad behavioral economics;
- language-documentation policy;
- cross-linguistic typological science;
- generic scientific-workflow agents.

---

# 4. High-level papers show that narrow/local does NOT mean weak

V16 must not lower the NAACL Main bar.

Strong recent precedents show that an extremely concrete linguistic/NLP object can be Best/Outstanding/Main.

## ACL 2026 Best — The Imperfective Paradox in Large Language Models

One classical semantic distinction:
- progressive accomplishment does not entail completion;
- progressive activity does.

The paper reveals a systematic teleological bias and pushes beyond benchmark accuracy.

## ACL 2026 Outstanding — CxMP

One narrow issue:
> grammatical acceptability is not the same as understanding meaning encoded by constructions.

Uses controlled minimal pairs grounded in Construction Grammar.

## ACL 2026 Main — RedirectQA

One overlooked axis:
> factual knowledge of an entity vs access through a particular surface name.

Uses natural Wikipedia redirects and decomposes frequency effects.

## EMNLP 2025 Outstanding — Causal Interventions Reveal Shared Structure Across English Filler–Gap Constructions

One established syntactic object:
> filler–gap dependencies.

Mechanism is used to test whether different constructions share abstract structure and to reveal factors relevant to linguistic theory.

## NAACL 2025 Outstanding — NLI under the Microscope

One established task:
> NLI.

New move:
> decompose hypotheses into atomic inferences and study consistency / critical subproblems.

## ACL 2025 Outstanding — A New Formulation of Zipf's Meaning–Frequency Law through Contextual Diversity

One old linguistic law:
> meaning–frequency relation.

New move:
> replace hard meaning counts with contextual diversity derived from contextualized representations.

### Calibration lesson

These papers are not broad because of topic labels.

They are Main/Outstanding/Best because they have:

> **a concrete object + a precise overlooked relation + a defensible measurement/design + a conclusion that changes understanding of the object.**

---

# 5. V16 candidate-generator rule

From now on, do NOT begin with:

> What broad old NLP problem has changed in the LLM era?

and do NOT begin with:

> What behavioral/mechanistic phenomenon has nobody benchmarked?

Instead begin with:

> **What concrete language/NLP object do we care about?**

Then ask:

> **Within this object, which two quantities/conditions are routinely conflated, or which structural relation is assumed but not directly tested?**

Then:

> **Can existing natural data/resources separate them?**

Only then:

> **Does LLM/Transformer architecture make this comparison newly meaningful or newly feasible?**

---

# 6. Preferred V16 question shapes

## Shape 1 — Natural confound split

Template:

> Existing task treats A and B as one factor.
>
> A natural resource lets us vary A while holding B approximately fixed.
>
> Which one actually explains model behavior?

RedirectQA is the clearest precedent.

High prior domains:
- lexical access;
- factual knowledge;
- semantic relations;
- paraphrase/form variation;
- structured language resources.

---

## Shape 2 — Explicit vs implicit licensed meaning

Template:

> Surface text states X.
>
> Linguistic structure licenses Y without literally stating Y.
>
> Does the model distinguish valid enrichment from unsupported completion?

High-level precedents:
- FrameBench;
- CxMP;
- Imperfective Paradox.

Requirement:
> Y must come from an established linguistic theory/resource, not author-written “common sense.”

---

## Shape 3 — Competing interpretations with real ambiguity

Template:

> The same expression supports interpretation A and B.
>
> Context/structure provides a principled disambiguator.
>
> What does the model retain, suppress, revise, or use?

Requirement:
- existing natural dataset or published linguistic materials;
- not generic “different probe → different answer.”

---

## Shape 4 — Structured sub-decision hidden inside a familiar pipeline

Template:

> A familiar task is evaluated end-to-end.
>
> But one intermediate decision has its own natural structure/gold and may dominate failures.
>
> Isolating it changes what the task actually requires.

Examples of style:
- citation placement;
- atomic NLI decomposition;
- semantic-resource relations.

Requirement:
> not merely “agentize/decompose the pipeline.”

---

## Shape 5 — Architecture-enabled separation

Template:

> Process A and B are entangled in ordinary autoregressive generation.
>
> A model architecture/training regime exposes an axis along which they can be separated.
>
> Their ordering/relation answers a pre-existing linguistic/NLP question.

Use with caution:
- DLM is fast-moving;
- architecture must enable the scientific measurement, not merely be fashionable.

---

## Shape 6 — Natural common budget / trade-off

Template:

> Two known controls consume the same real resource budget.
>
> Their interaction has a nontrivial structural consequence / regime change.

Kisako provides local precedent.

But for NAACL Main:
> **“we ran the grid and found the best combination” is not enough.**

Need:
- law/regime;
- principled prediction;
- or general decision rule.

---

# 7. Search-space restrictions after V16

## Primary search area

Prioritize:
- lexical semantics;
- compositional semantics;
- factual/parametric knowledge;
- semantic access;
- linguistic inference;
- structured semantic resources;
- frame/construction/relation reasoning;
- discourse/citation structure where not overlapping labmates;
- text representation/embedding behavior where a natural structural axis exists.

## Secondary / conditional

- diffusion-LM generation dynamics;
- causal interpretability;
- Japanese-specific language phenomena;
- efficiency/compression.

These are allowed only when the scientific object is strong.

## Strong negative prior

Do not spend broad search budget on:
- behavioral economics transplanted to LLMs;
- broad typological database policy;
- language-documentation resource allocation;
- generic scientific-workflow agents;
- generic LLM-as-judge / annotator;
- generic RAG;
- agent benchmark construction;
- generic “LLM bias” hunting;
- mechanism-first feature hunting;
- synthetic ontology/world tasks.

This is a **search-priority correction**, not a claim that these areas can never produce strong papers.

---

# 8. Collision map from the local scan

The following local-looking lanes are already crowded and should not be naively activated:

- generic FrameNet/frame identification;
- generic idiom literal-vs-figurative mechanism;
- generic lexical ambiguity representation;
- generic presupposition detection/challenge;
- generic related-work generation;
- generic citation/evidence generation;
- generic schema transfer/alignment;
- generic “LLM completes a semantic resource.”

Therefore:

> **Use labmates to learn the shape, not to copy the neighboring task.**

---

# 9. New two-layer gate

Every future candidate must pass BOTH layers.

## Layer L — Local-prior fit

Can the question be naturally described as one of:
- a lexical/semantic/factual relation;
- a structured NLP resource relation;
- an explicit/implicit meaning distinction;
- a natural representation/generation trade-off;
- a concrete language-understanding subproblem?

Would its data/method feel normal in the recent Sasano-Lab research ecology?

If not:
> very strong evidence is required before spending search budget.

## Layer M — Main-level fit

Still require all existing gates:
- naturalness;
- importance;
- non-obviousness;
- scientific tension;
- structural specificity;
- independent parent novelty;
- data/gold provenance;
- outcome robustness;
- reviewer compression;
- Main-scale growth;
- crowdedness/workload;
- durability;
- explicit kill criteria.

Local fit can never override novelty or Main-level weakness.

---

# 10. Current candidates after reset

## IFG
**KILLED in V15.**

No change.

## DRP
**KILLED in V15.**

No change.

## TCR
Scientifically not proven impossible, but:

# **DE-PRIORITIZED / LEGACY SEARCH-ONLY / NO COMPUTE**

Reason:
- typological database robustness is too far from the now-identified local search prior;
- it requires a large cross-linguistic/documentation/scientific-inference apparatus before reaching a concrete NLP object;
- opportunity cost is high.

Do not continue TCR front-end work by default.

It may return only if later evidence makes it clearly stronger than local-prior candidates.

## HOM
**SEARCH-ONLY / NO COMPUTE**, unchanged.

## New approved mainline
**NONE.**

## New registered candidate
**NONE YET.**

V16 deliberately resets the search space before manufacturing replacements.

---

# 11. Immediate bounded search program

The next candidate search should be restricted to four bounded lanes:

### Lane A — lexical/semantic access under natural form or relation changes

Look for:
- existing natural resources;
- an overlooked factor that can be separated without synthetic worlds;
- a scientific conclusion about knowledge access / representation.

Avoid copying RedirectQA or Tsujimoto's exact hierarchy-frequency question.

### Lane B — explicit vs implicit/compositional meaning

Search specific established linguistic phenomena with:
- published materials or natural corpora;
- exact or theory-backed predictions;
- meaningful model failures beyond “LLMs are inconsistent.”

ACL 2026 Best/Outstanding sets the bar.

### Lane C — structured relations inside existing NLP resources/tasks

Look for an established resource/task where:
- one relation/sub-decision is underspecified or conflated;
- gold already exists;
- isolating it changes the interpretation of end-to-end performance.

Avoid FrameNet relation inference and citation placement because labmates are already there.

### Lane D — representation/learning efficiency with one natural axis

Search only where:
- the budget/axis is real;
- interaction is structurally predictable;
- the result can become a rule/regime, not an ablation grid.

---

# 12. V16 governing sentence

> **Search locally, judge globally.**

More explicitly:

> **Start from a concrete language/NLP object that would look natural in Sasano Lab. Find one structurally meaningful overlooked axis inside that object. Use existing natural data to isolate it. Then demand ACL/EMNLP/NAACL Main-level novelty and claim architecture.**

This replaces the V14–V15 habit of searching the whole NLP/scientific-methodology space first.

No target-model compute is authorized.
