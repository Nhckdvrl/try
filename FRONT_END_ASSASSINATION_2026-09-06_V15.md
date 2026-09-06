# V15 — FRONT-END ASSASSINATION / COLLISION TIGHTENING

**Date:** 2026-09-06  
**Target:** NAACL Main; calibrated against ACL / EMNLP / NAACL Main and especially Best / Outstanding / Best Theme work.

> **NO APPROVED PAPER MAINLINE.**
>
> **NO TARGET-MODEL COMPUTE AUTHORIZED.**
>
> V15 deliberately shrinks the live portfolio. Candidate count is not a goal.

---

# 0. Governing rule

V14 remains the methodology base:

> **Alignment-First + Data-First + Non-Obviousness-First + Structural Specificity + Old-Problem/New-Method + Durability.**

V15 adds no weaker standard. It records what happened when the three V14 front-end themes were attacked at the parent-question level.

Current statuses:

| topic | V15 status |
|---|---|
| **IFG — Task-Conditioned Evidence Weighting / Inference–Forecast Gap** | **SERIOUS / HIGH-COLLISION / D2 / FRONT-END CONTROL AUDIT / NO COMPUTE** |
| **TCR — Typological Coverage Robustness under Grammar-Book Expansion** | **CONDITIONAL SERIOUS-SEARCH / RECONSTRUCTION GATE / D0–D1 PATH / NO COMPUTE** |
| **DRP — Documentation Resource Portfolio in the LLM Era** | **KILLED — CURRENT FORMULATION** |
| **HOM** | **SEARCH-ONLY / NO COMPUTE** |

There is no obligation to maintain three live candidates.

---

# 1. DRP — KILL current formulation

## Original attraction

DRP asked:

> When one foundation model can consume dictionaries, grammar descriptions, parallel examples and IGT, how should scarce documentation effort be allocated across resource types to maximize reusable cross-task capability?

The intended old-assumption rewrite was:

> heterogeneous linguistic resources previously fed different bespoke pipelines; a shared LLM consumer might make their substitution/complementarity directly comparable.

## Why the parent no longer survives

### Collision 1 — the resource-type question is already partly owned

ICLR 2025, **Can LLMs Really Learn to Translate a Low-Resource Language from One Grammar Book?**, separates grammatical explanations from parallel examples and finds that almost all MT improvement comes from parallel examples; it then tests grammar-oriented tasks and explicitly argues for **task-appropriate data collection**.

This already occupies a large part of the proposed DRP scientific tension:

- grammar may be reusable;
- examples may dominate;
- value may be task dependent.

Adding more resource types and more tasks does not create a new parent question.

### Collision 2 — finite documentation/resource prioritization is not new

2026 **Customizing ASR for Language Documentation and Resource Prioritization** explicitly compares how scarce project time should be spent on transcription correction versus manual alignment and derives a prioritization recommendation.

Older finite-budget NLP work, e.g. **Clean or Annotate: How to Spend a Limited Data Collection Budget**, already treats allocation under a common annotation budget as the methodological object.

Therefore “scarce resource → compare marginal utility → allocate budget” is not independently ours.

### Structural problem — the assets are not cleanly substitutable

Dictionary, grammar, IGT, transcription, translated examples and parallel corpora are often not independent products. Documentation workflows frequently derive higher-level resources from a primary corpus and from overlapping fieldwork/analysis effort.

A scalar budget such as

```
grammar = x hours
dictionary = y hours
IGT sentence = z minutes
```

would therefore require strong causal/accounting assumptions. Without independently documented production costs, the portfolio frontier becomes author-defined.

## Reviewer compression

> **“This is a bigger resource ablation plus an arbitrary cost model.”**

V15 cannot rebut this strongly enough.

## Verdict

# **KILL DRP CURRENT FORMULATION**

Do not rescue by:
- adding more languages;
- adding more tasks;
- adding more resource types;
- estimating token counts as “cost”;
- inventing expert-hour conversion factors;
- calling the factorial ablation a Pareto frontier.

Return only if a genuinely external decision problem supplies both:
1. a real shared budget/accounting unit; and
2. a scientific/operational estimand not already reducible to task-appropriate resource selection.

---

# 2. TCR — downgrade to reconstruction gate

## Surviving question

> **Does changing historically missing typological coverage change published linguistic conclusions, rather than merely improve feature extraction accuracy?**

Only this scientific-inference estimand is potentially ours.

## New direct collision

EMNLP 2026 lists **LLM Agents as Computational Typologists** (Changbing Yang, Christopher Hammerly, Freda Shi, Jian Zhu). The described system turns a typological query into an evidence-grounded judgment by planning evidence needs and retrieving from grammar sources.

Together with:
- EMNLP 2025 Outstanding **LingGym: How Far Are LLMs from Thinking Like Field Linguists?**
- SIGTYP 2026 grammar-book RAG for typological database completion;
- prior typological feature prediction / database completion;

this kills any TCR rescue whose novelty is:

> “LLMs can read grammars and answer arbitrary typological questions.”

TCR can survive only if the **downstream published-science robustness estimand** is demonstrably independent.

## Data-only leverage audit of Nature Human Behaviour 2026

Repository-level audit of the public analysis for **Enduring constraints on grammar revealed by Bayesian spatiophylogenetic analyses**:

- 191 tested universals;
- 120 distinct Grambank features occur in their formalizations;
- per-universal main analysis language count:
  - min: 329
  - Q1: 1469
  - median: 1678
  - mean: ~1652.5
  - Q3: 1871
  - max: 2225
- 61/191 analyses already use at least 1800 languages;
- only 3/191 use fewer than 1000;
- 89/191 are significant in the reported spatiophylogenetic analysis and 102/191 are not.

This is a warning against the naive story:

> “Grambank is sparse, therefore filling missing cells should substantially change many universals.”

For many claims the existing effective sample is already large. Extra coverage may only narrow intervals.

However, a small number of estimates sit close to a decision boundary, so a **targeted sensitivity** formulation remains logically possible.

## Extraction-quality warning

The 2026 grammar-book RAG database-completion paper reports only roughly **51–70% exact feature accuracy across five languages**, with false positives a major failure mode.

This matters scientifically because grammar silence is not equivalent to feature absence. Grambank itself distinguishes:
- cells not yet coded;
- source-insufficient / unknown states.

Therefore TCR must not treat “LLM completion” as gold.

## V15 reconstruction gate

Before any target-model experiment, TCR must establish a **data-only leverage matrix**:

1. map each published universal to required Grambank features — largely done (120 distinct features);
2. distinguish genuinely uncoded cells from source-checked-but-insufficient cells;
3. identify uncoded languages that actually have accessible grammar/sketch evidence;
4. focus on claims whose current posterior/CI is close enough to a scientifically meaningful boundary that plausible new evidence could matter;
5. estimate a feature-specific extraction-error envelope using already coded cells;
6. ask whether the possible coverage expansion can move inference **after** propagating that error.

### Mandatory kill rule

KILL TCR if:
- meaningful leverage requires thousands of new cells;
- most missing cells are source-insufficient rather than merely uncoded;
- extraction error dominates the maximum plausible scientific shift;
- the result is mainly narrower confidence intervals;
- only cherry-picked one-off universals can move;
- the paper identity becomes grammar-RAG / computational typologist rather than scientific robustness.

## Current verdict

# **CONDITIONAL SERIOUS-SEARCH / RECONSTRUCTION GATE / NO COMPUTE**

The broad “complete Grambank and rerun 191 universals” version is no longer acceptable.

---

# 3. IFG — survives, but only after further narrowing

## Exact human design is cleaner than initially feared

Econometrica 2026 **The Inference-Forecast Gap in Belief Updating** uses a permanent latent state Good/Bad.

In baseline:
- next signal mean = 100 in Good;
- next signal mean = 0 in Bad;
- inference elicits posterior probability of Good;
- forecast elicits expected next signal.

Therefore if the posterior Good probability is expressed as a percentage, the normative forecast is numerically the **same number**:

> posterior-Good percentage = expected next signal.

Corresponding inference and forecast rounds use the same realized evidence.

This creates an unusually clean same-evidence, same-scale structural test and weakens the objection that direct forecasting simply requires harder arithmetic.

## Collision tightening

IFG cannot own any of the following:
- generic Bayesian imperfection;
- latent inference vs downstream prediction;
- “different probes reveal different beliefs”;
- knowing-vs-using;
- forecast updating inconsistency.

Why:

### BayesBench
Already elicits latent-type posteriors and downstream predictions from the same rating history under exact Bayesian references.

### 2026 multi-probe Bayesian work
Recent work measures a posterior using prediction, hypothesis evaluation and hypothesis generation and finds these measurements are not interchangeable.

### 2026 probabilistic forecasting work
Recent forecasting methods such as likelihood-elicitation/aggregation explicitly decompose evidence likelihoods and aggregate them into forecasts.

The lane is therefore crowded. IFG remains alive only because of its **object-specific exact mapping and intervention on target-statistic similarity**.

## Surviving pre-result accounts

### H1 — Task-invariant posterior
The model computes one evidence-conditioned latent belief state. Direct inference and direct forecast should satisfy the exact LoIE mapping, apart from response noise. Reframing target/nontarget similarity should not systematically change the mapped posterior.

### H2 — Query-conditioned heuristic selection
Changing only the requested statistic changes which evidence-processing heuristic is selected. The exact paired residual should therefore move in the direction predicted by target/nontarget similarity manipulations.

### H3 — Arithmetic / output / scale artifact
Any apparent gap comes from arithmetic or response-format differences. The baseline 1:1 mapping and deterministic-outcome controls should largely remove it.

## Required C1/C2/C3 architecture

### C1 — exact paired residual
For the same DGP/prior/signal:

```
r = direct_forecast - map(direct_inference)
```

where `map` is fixed by the DGP, not fitted post hoc.

### C2 — structural intervention
Use the Econometrica More-Similar / Less-Similar logic to make competing heuristic-selection accounts predict **directional changes in r**, not merely “gap/no gap.”

### C3 — infer-then-map control
Elicit inference, then deterministically map that answer to the forecast. Compare it with direct forecast.

If infer→map is coherent while direct forecast shifts with requested statistic, the behavioral evidence favors query-conditioned computation/readout over inability to perform the normative mapping.

Do not describe this as proof of a unique internal “belief state.”

## IFG immediate kill rules

KILL if:
- an equivalent same-evidence + exact-mapping + target-statistic intervention already exists for LLMs;
- direct and infer→map answers coincide once format/arithmetic are matched;
- the similarity intervention does not produce the pre-specified directional pattern;
- the strongest claim collapses to “LLMs are imperfect Bayesians” or “different prompts give different answers.”

## Current verdict

# **SERIOUS / HIGH-COLLISION / D2 / FRONT-END CONTROL AUDIT / NO COMPUTE**

---

# 4. New anti-resurrection additions

Do not promote the following without a different parent estimand:

1. **Generic cross-resource documentation portfolio / larger resource ablation.**
2. **Generic multi-probe posterior inconsistency.**
3. **“LLM can read a grammar and act as a computational typologist.”**
4. **Generic annotation-guideline-as-LLM-supervision.** ACL 2024/2025 and ACL 2026 already directly study LLM use/refinement of annotation guidelines.
5. **Dependence-aware aggregation of multiple LLM judges.** 2026 work already directly replaces conditional-independence aggregation with dependence-aware models.
6. **Generic lexicon/dictionary → contextual LLM text measurement.** Current social-science measurement literature already directly compares lexicon/supervised/LLM paradigms.
7. **Classic MT challenge revisit.** TACL/ACL-era work already systematically revisits multiple classic MT assumptions in the LLM era.

---

# 5. Search result: no replacement candidate promoted this pass

This is intentional.

Several superficially attractive old-problem/new-method shapes were checked and rejected because recent work already owns the parent:
- guideline vs examples as supervision;
- dependence-aware LLM annotator aggregation;
- schema-free / on-demand computational typology;
- contextual LLM replacement for lexical text measurement.

V15 therefore leaves the portfolio with:
- one serious high-collision candidate (IFG);
- one conditional reconstruction candidate (TCR);
- an empty third slot.

> **A blank slot is preferable to a weak topic.**

---

# 6. Next no-compute work

## IFG
1. retrieve/inspect the full Econometrica replication package;
2. reconstruct all baseline/treatment DGPs and exact mappings;
3. write the paired residual and directional predictions before observing LLM outputs;
4. finish 2025–2026 collision search;
5. pre-register arithmetic/output-format/infer→map controls;
6. only then decide whether a minimum decisive pilot is authorized.

## TCR
1. build the feature × language × source-state leverage table;
2. separate blank uncoded from source-insufficient;
3. cross-reference accessible grammar/sketch availability;
4. quantify near-boundary posterior sensitivity;
5. propagate plausible feature-specific extraction error;
6. KILL if there is no small, decisive, externally grounded subset.

## Search
Continue durable old-assumption search. Prefer:
- classical laws whose premises changed, not merely tasks with a new model;
- measurement problems where a previously impossible intervention becomes possible;
- old cost models whose optimal policy changes under a genuinely new primitive;
- stable scientific questions with existing natural data/gold.

No target-model compute is authorized by V15.
