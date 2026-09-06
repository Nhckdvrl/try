# Old-Problem / New-Method Research-Question Search — 2026-09-06 V15

**Target:** NAACL Main, calibrated against ACL / EMNLP / NAACL Main and especially Best / Outstanding / Best Theme work.  
**Status:** current candidate/search authority after V14.  
**Important:** **NO APPROVED PAPER MAINLINE. NO TARGET-MODEL COMPUTE AUTHORIZED.**

---

# 0. V15 executive correction: portfolio contraction is evidence, not failure

V14 intentionally created a heterogeneous three-topic front-end portfolio. V15 applies the same gates without protecting that portfolio.

Current result:

| object | V15 verdict |
|---|---|
| **TCR — Typological Coverage Robustness under Grammar-Book Expansion** | **SERIOUS-SEARCH / FRONT-END COVERAGE-LEVERAGE AUDIT / D0–D1 PATH / NO COMPUTE** |
| **IFG — Task-Conditioned Evidence Weighting / Inference–Forecast Gap** | **KILL CURRENT FORMULATION** |
| **DRP — Documentation Resource Portfolio in the LLM Era** | **KILL CURRENT FORMULATION** |
| **HOM — Plural Homogeneity** | **SEARCH-ONLY / NO COMPUTE** |
| replacement candidate | **NONE REGISTERED** |

There is deliberately **no requirement to keep three candidates alive**.

The V15 lesson is exactly the intended behavior of the research process:

> **A beautiful diagnostic is not enough if another paper already owns the parent scientific proposition.**

> **A socially important resource problem is not enough if recent work already occupies resource value, collection policy, and cost-aware allocation.**

> **An apparently data-rich audit is not enough unless the added observations have enough leverage to change scientific conclusions.**

---

# 1. IFG assassination — KILL current formulation

## 1.1 V14 surviving claim

IFG had already been narrowed to:

> Under the same DGP, prior and realized evidence, latent-state inference and next-outcome forecast are connected by an exact Law-of-Iterated-Expectations mapping. Does changing only the requested target statistic change the model's evidence-weighting computation?

The Econometrica human experiment remains an unusually clean D2 substrate:

- Tony Q. Fan, Yucheng Liang, Cameron Peng. **The Inference-Forecast Gap in Belief Updating.** Econometrica, 2026.
- https://onlinelibrary.wiley.com/doi/10.3982/ECTA23334

The exact mapping is scientifically better than a generic “two prompts differ” comparison.

## 1.2 New direct parent collision

Hua-Dong Xiong (2026), **Hypothesis generation and updating in large language models**, measures the posterior over the same hypothesis space through three probes:

- posterior prediction;
- hypothesis evaluation;
- hypothesis generation.

It explicitly asks whether **the same posterior is expressed across probes**, maps the readouts into a common Bayesian interpretation, and reports systematic cross-probe inconsistency.

- https://arxiv.org/abs/2605.05851

Together with the already-audited BayesBench neighborhood, this means the broad parent proposition is no longer ours:

> **Different task/probe requests can expose mutually incompatible effective beliefs even when they are intended as readouts of one latent posterior.**

## 1.3 Why the LoIE bridge does not rescue parent novelty

IFG still has a cleaner structural diagnostic:

- same evidence;
- exact known DGP;
- inference→forecast bridge;
- no unseen-item generalization required.

But under P9 and P13 the strongest reviewer compression is now:

> **“This is another cross-probe posterior inconsistency paper, with a particularly clean exact mapping.”**

That is a better experiment, not clearly a new parent research question.

The likely claims are also too easy to compress into occupied space:

- LLMs express task-conditioned beliefs;
- posterior-like knowledge is not task invariant;
- prediction and inference probes are inconsistent;
- LLMs reproduce a human inference/forecast dissociation.

The project standard does not protect exact-cell novelty merely because the cell has elegant mathematics.

## 1.4 Verdict

# **KILL CURRENT IFG FORMULATION.**

No pilot.

Do not revive it by:
- changing Bayesian task family;
- adding more model families;
- adding mechanistic probes;
- describing the effect as “task-conditioned evidence weighting” without a new causal prediction.

### Return condition

IFG-like work can return only if a new intervention yields a **causal or structural prediction that is not entailed by generic cross-probe posterior inconsistency**.

The burden is not “nobody used this exact Econometrica task on an LLM.” It is “the parent scientific conclusion is genuinely different.”

---

# 2. DRP assassination — KILL current formulation

## 2.1 V14 question

> When one foundation model can consume dictionaries, grammar descriptions, parallel examples and IGT, how should scarce documentation effort be allocated across these resource types to maximize reusable capability across language tasks?

The intended novelty was not a single-task resource ablation, but cross-task marginal value, complementarity and a cost-normalized resource portfolio.

## 2.2 Why the parent neighborhood is now too closed

Recent work occupies multiple load-bearing pieces simultaneously.

### Resource-type value and policy conclusion

ICLR 2025:

**Can LLMs Really Learn to Translate a Low-Resource Language from One Grammar Book?**

- separates parallel examples from grammatical explanations;
- evaluates where grammar descriptions help and do not help;
- explicitly concludes that translation-oriented XLR data collection is better focused on parallel data than linguistic description.

https://proceedings.iclr.cc/paper_files/paper/2025/hash/20f44da80080d76bbc35bca0027f14e6-Abstract-Conference.html

ACL 2025 Main:

**Understanding In-Context Machine Translation for Low-Resource Languages: A Case Study on Manchu**

already systematically compares dictionary, grammar-book and retrieved-parallel resources.

https://aclanthology.org/2025.acl-long.429/

### Cost-aware resource allocation

EACL 2026 Findings:

**Active Learning with Non-Uniform Costs for African Natural Language Processing**

explicitly models heterogeneous annotation costs and solves a knapsack-style fixed-budget allocation problem.

https://aclanthology.org/2026.findings-eacl.349/

### Language-documentation resource prioritization

CustomNLP4U 2026:

**Customizing ASR for Language Documentation and Resource Prioritization**

directly asks how to prioritize scarce documentation work and compares time spent on transcription correction versus alignment.

https://aclanthology.org/2026.customnlp4u-1.13/

## 2.3 Why “cross-task + Pareto frontier” is not enough

One can still build a larger experiment that contains:

- grammar;
- dictionary;
- parallel text;
- IGT;
- several downstream tasks;
- cost curves;
- Pareto fronts.

But that does not automatically create a new parent question.

Reviewer compression remains strong:

> **“This is a larger cost-aware resource ablation that aggregates several already studied resource trade-offs.”**

The unresolved cost problem is also fundamental: dictionary building, grammar writing, transcription, translation and IGT are not naturally denominated in one externally validated cost unit. Invented expert-hours would weaken both gold and policy validity.

## 2.4 Verdict

# **KILL CURRENT DRP FORMULATION.**

Do not preserve it because language documentation is important or because no one has plotted exactly this multi-resource Pareto frontier.

### Return condition

A documentation-resource question may return only with a new estimand that cannot be reduced to:
- resource ablation;
- annotation-cost optimization;
- task-specific data prioritization;
- or multi-task aggregation.

For example, a genuine invariant/substitution law or a scientifically necessary resource-interaction principle could qualify, but none has been established.

---

# 3. TCR deep audit — survives, but is weaker than V14 implied

Working title:

> **Would Linguistic Universals Survive Better Coverage? LLM-Assisted Sensitivity Analysis of Typological Conclusions**

Current status:

# **SERIOUS-SEARCH / FRONT-END COVERAGE-LEVERAGE AUDIT / D0–D1 PATH / NO COMPUTE**

## 3.1 Parent question

> **When existing grammatical descriptions make previously uncoded typological evidence recoverable, which published cross-linguistic conclusions remain stable and which depend on the historical coverage pattern of the database?**

This is still distinct from the occupied extraction task:

> “Can RAG predict Grambank feature values from grammar books?”

SIGTYP 2026 owns that extraction/completion parent:

- Jonathan Hus, Antonios Anastasopoulos. **A RAG Approach for Typological Database Completion.**
- https://aclanthology.org/2026.sigtyp-main.7/

The only possible TCR contribution is downstream **scientific-inference robustness under realized coverage expansion**.

## 3.2 External scientific target remains unusually strong

Nature Human Behaviour 2026:

**Enduring constraints on grammar revealed by Bayesian spatiophylogenetic analyses**

- starts from >2,000 documented universals;
- identifies 146 original synchronic implicational universals that match Grambank variables/criteria;
- reformulates them into 191 testable simple universals;
- uses Grambank v1.0 with 2,430 languages and 195 features;
- controls genealogical and geographic non-independence;
- releases data, code and outputs.

Paper:
https://www.nature.com/articles/s41562-025-02325-z

Public analysis repository:
https://github.com/SimonGreenhill/TestingLinguisticUniversals

This makes the scientific claims, mappings and inference procedure pre-existing rather than author-invented.

## 3.3 New no-compute code audit: baseline coverage is already high

The public **SI Data 1/results.txt** contains the 191 formal Grambank mappings and sample sizes.

Direct front-end audit of the released table gives:

- 191 rows / simple universals;
- **main_n min = 329**;
- **Q1 ≈ 1,469**;
- **median ≈ 1,678**;
- **Q3 ≈ 1,871**;
- **max = 2,225**;
- **mean ≈ 1,652.5**;
- the 191 formulas reference **126 distinct Grambank features**;
- median formula references roughly **4 Grambank feature occurrences**.

This materially changes the prior.

The original V14 intuition “coverage is incomplete, therefore expansion may matter” is insufficient because many existing analyses already contain well over a thousand languages.

### New threat

For many universals, realistic new cells may produce only:

> **more data → slightly narrower credible interval**

which is an explicit TCR kill condition.

## 3.4 Missingness is structured, but not every missing value is legitimately fillable

Grambank/typological documentation work has already shown that description quality and gaps vary across space, time and grammatical domains.

- Lesage et al. 2022. **Overlooked Data in Typological Databases: What Grambank Teaches Us About Gaps in Grammars.**
- https://aclanthology.org/2022.lrec-1.309/

Important operational distinction:

- an explicitly uncertain/unknown coding after consulting a source is **not equivalent** to an unattempted cell;
- TCR must not turn “the grammar does not support a confident answer” into a forced binary label.

The clean expansion target is therefore primarily:

1. genuinely unattempted language-feature cells for which a grammar/sketch already exists;
2. languages with usable grammatical descriptions but not yet represented for the relevant features;
3. only secondarily, uncertain cells where additional independent source evidence actually exists.

## 3.5 Robustness/error literature is a serious collision neighborhood

TCR does **not** own the generic proposition:

> “Typological scientific conclusions may be sensitive to bad database values.”

A current study:

**The effect of mistakes in typological datasets: A cautionary tale**

tests 20 universals with Grambank / World Morphosyntax and injects random and structured mistakes. At high mistake rates, especially non-random ones, effects can disappear, appear or reverse.

https://laurabecker.gitlab.io/papers/mistakes_typological_datasets_LB_MM_MGN.pdf

Becker & Guzmán Naranjo 2025 also explicitly study replication and methodological robustness in quantitative typology:

https://www.degruyterbrill.com/document/doi/10.1515/lingty-2023-0076/html

Therefore TCR cannot claim:
- “typological databases have errors”;
- “non-random noise changes conclusions”;
- “we should perform sensitivity analysis.”

Its only plausible independent axis is:

> **Replace hypothetical corruption with real, grammar-backed observations from the historically omitted part of the language-feature matrix, and estimate the scientific effect of that realized coverage selection.**

That is narrower, but still potentially independent.

## 3.6 Nature 2026 already handles important alternative explanations

The Nature paper already addresses:
- genealogy;
- geography;
- historical bias in earlier language samples;
- implementation/mapping of universals to Grambank features.

Therefore the TCR story cannot be:

> “prior universal tests ignored genealogical/areal sampling.”

That is occupied by the target paper itself.

It also cannot rely on vague “database bias.” The missingness mechanism must be tied to **which actual new language-feature observations become available**.

---

# 4. New hard gate for TCR: Coverage Leverage Gate

Before any target-model extraction, TCR must prove that feasible new observations have enough scientific leverage to matter.

For each of the 191 released universals, construct a no-LLM audit:

1. parse its exact Grambank feature formula;
2. identify languages/cells currently excluded because one or more required values are missing;
3. separate:
   - unattempted/unavailable coding,
   - explicit uncertainty,
   - logically inapplicable values where relevant;
4. map excluded languages by:
   - family,
   - macro-area,
   - source/documentation period,
   - grammatical domain;
5. determine whether an independently existing grammar/sketch/source is available;
6. estimate the **maximum realistically attainable new coverage**;
7. compute a sensitivity/leverage bound:
   - how much could the effect estimate move under defensible assignments to those feasible cells?
   - can support status plausibly change?
   - is missingness concentrated exactly where it has high genealogical/geographic leverage?

The desired outcome of this audit is **not** a positive TCR result. It is a decision about whether TCR deserves any LLM extraction at all.

## 4.1 Pre-compute kill criteria

# KILL TCR before extraction if:

1. most universals already have such high effective coverage that feasible additions cannot materially alter effect sizes;
2. missing cells are broadly diffuse rather than structurally concentrated;
3. accessible grammars mostly correspond to cells already coded;
4. plausible assignments to recoverable cells cannot change substantive posterior conclusions except by narrowing intervals;
5. the only high-leverage cells are exactly those where existing grammars are known to be insufficient/ambiguous;
6. a recent paper is found that already performs real grammar-backed coverage expansion and re-estimates published typological universals/correlations;
7. the credible contribution becomes primarily extraction accuracy.

This is stricter than V14.

---

# 5. TCR competing hypotheses after V15

The scientific tension remains viable only in the following form.

### H1 — Coverage-stable science

Historically uncoded but recoverable observations are approximately exchangeable with current evidence after genealogy/geography are modeled.

Prediction:
> feasible real coverage expansion leaves substantive effect estimates/support largely stable.

### H2 — Documentation-selection science

Recoverable omissions are structurally concentrated by family, area, domain or documentation history, and this concentration intersects the tested universals.

Prediction:
> adding real omitted evidence systematically changes a nontrivial preregistered subset of effect estimates/support.

### H3 — Source-limited measurement

The apparent missingness is not mainly a coding bottleneck; the underlying grammars genuinely lack decisive evidence.

Prediction:
> grammar-backed expansion has low attainable coverage or high epistemic uncertainty, and robust scientific conclusions cannot be changed defensibly.

H3 is a scientifically meaningful negative result for the **feasibility audit**, but if it dominates then the LLM paper itself should be killed rather than written as an extraction benchmark.

---

# 6. Extraction uncertainty — only if TCR survives the leverage audit

If and only if the no-compute leverage analysis survives:

- validate masked extraction on already-coded cells;
- stratify validation by feature/domain/source type;
- do not treat one LLM answer as gold;
- retain “insufficient evidence” as a first-class outcome;
- manually verify only load-bearing newly added cells;
- propagate label uncertainty into the spatiophylogenetic model or perform calibrated sensitivity analyses.

A paper that inserts hard LLM labels into Grambank and reruns the Nature code is not acceptable.

---

# 7. TCR variants considered but NOT activated

## 7.1 “Test universals directly from grammar books without a fixed database schema”

At first glance this is stronger:

> LLMs make the fixed Grambank feature inventory unnecessary, so scientific hypotheses previously untestable because of schema limitations become testable.

Do **not** activate yet.

Why:
- the Nature study starts from >2,000 universals but excludes many for substantive reasons: phonology/semantics, excessive specificity, diachrony, non-implicational form;
- we do not yet have evidence that a large, clean subset was excluded **only** because a fixed feature schema could not express it;
- gold becomes much weaker;
- this risks resurrecting the already-closed generic “universal schema / schema mediation” lane.

Only revisit if an external exclusion table demonstrates a sizeable, scientifically coherent class whose sole bottleneck is representation in Grambank.

## 7.2 “LLMs enable gradient/token-based typology instead of categorical databases”

Do not activate.

Token-based and corpus-based typology already has direct precedent, including quantitative word-order work and recent multilingual token-based typology. LLMs do not automatically create a new parent question here.

## 7.3 “Direct grammar reading fixes Grambank operationalization errors”

Do not activate as a standalone parent.

The target Nature analysis already records implementation quality/limitations, while quantitative-typology robustness and annotation-error work is active. A direct-grammar version currently compresses to dataset/operationalization auditing.

---

# 8. New search lane assassination: LLM-generated hypotheses + selective inference

A potentially attractive Old-Problem/New-Method idea was:

> LLMs can inspect data and generate hypotheses at scale; classical hypothesis tests assume the tested hypothesis was fixed independently of the evaluation data. Do we need a new validity protocol for LLM-assisted discovery?

**DO NOT ACTIVATE / PARENT OCCUPIED.**

Why:
- post-selection inference, sample splitting and adaptive-data-analysis validity are mature statistical problems;
- recent data-driven-science work explicitly discusses the same “use data to generate a hypothesis, then test it on the same data” double-dipping problem;
- current AI-scientist work makes the application timely but does not change the underlying statistical parent;
- it also pulls the paper toward a fast-moving agent/scientific-agent lane, a negative advisor prior.

The LLM changes scale and convenience, but the load-bearing statistical structure is already known.

---

# 9. What V15 says about the search process

The correct current portfolio is intentionally sparse:

### Surviving front-end candidate
- **TCR** — one more no-compute assassination round required.

### Search-only
- **HOM** — unchanged; not counted.

### Newly killed
- **IFG current formulation**
- **DRP current formulation**

### Newly explored and not registered
- LLM-generated hypothesis → selective/post-selection inference;
- schema-free direct universal testing;
- gradient/token-based typology revisit.

There is **no approved replacement candidate**.

This is preferable to manufacturing two weak topics to preserve a list of three.

---

# 10. Next work

## 10.1 TCR — immediate, no target model

Build the **Coverage Leverage Map** from the released Nature/Grambank data:

- 191 universal → required Grambank feature IDs;
- current usable language count;
- exclusion/missingness by required feature;
- family/area distribution of excluded languages;
- source availability for recoverable observations;
- best-case attainable new coverage;
- worst-/best-case effect sensitivity;
- identify which universals could cross a substantive decision boundary.

Only after this should grammar-book extraction be considered.

## 10.2 Continue durable Old-Problem/New-Method search

Search should continue in parallel across:
- classical statistical/measurement laws in NLP;
- corpus and language-science measurement;
- language documentation and typology;
- historical linguistic methodology;
- durable evaluation/statistical design;
- old algorithms whose optimality relies on a computational primitive that LLMs genuinely change.

But retain the anti-resurrection rule:

> **A new interface, cheaper annotator, stronger semantic model, or multi-task aggregation is not by itself a rewritten old assumption.**

---

# 11. V15 authority

> **The scientific object should exist before us.**

> **The data should exist before our hypothesis.**

> **The scientific tension should exist before the result.**

> **The structural relation should exist before the gap.**

> **A new method should change what science can test, not just who performs the work.**

> **A classic revisit must identify which old assumption breaks in the LLM era.**

> **Prefer questions whose importance survives model/API churn.**

New V15 operational addition:

> **Before using an LLM to expand a scientific dataset, prove that the realistically recoverable observations have enough leverage to change the scientific estimand.**

No target-model compute is authorized.
