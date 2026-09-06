# Killed Research-Question Ledger — 2026-09-06 V15

**Status:** current kill / do-not-reactivate authority.  
**Inherits:** V14 and all earlier ledgers.  
**Rule:** a new domain/task/model name does not revive an occupied parent question.

---

# 1. IFG — Task-Conditioned Evidence Weighting / Inference–Forecast Gap

## Verdict

# **KILL CURRENT FORMULATION**

Former surviving question:

> Under the same DGP, prior and realized evidence, does changing only the requested target statistic cause an LLM to use a different evidence-weighting computation, even though inference and forecast are linked by an exact LoIE mapping?

## Direct reason

Hua-Dong Xiong (2026), **Hypothesis generation and updating in large language models**, already measures one Bayesian hypothesis posterior through posterior prediction, hypothesis evaluation and hypothesis generation and explicitly asks whether the **same posterior is expressed across probes**.

- https://arxiv.org/abs/2605.05851

Together with the BayesBench neighborhood audited in V14, the parent proposition

> different task/probe requests expose incompatible effective latent beliefs

is too directly occupied.

The Econometrica inference–forecast design remains unusually clean because the readouts have an exact DGP / Law-of-Iterated-Expectations bridge:

- https://onlinelibrary.wiley.com/doi/10.3982/ECTA23334

But under P9/P13 that is now a particularly elegant diagnostic cell rather than a clearly independent parent RQ.

Reviewer compression:

> **“Another cross-probe posterior inconsistency paper, with a nicer exact mapping.”**

Do not resurrect by:
- changing Bayesian task family;
- renaming the axis “task-conditioned evidence weighting”;
- adding models/prompts;
- adding mechanism after the fact;
- claiming “LLMs reproduce the human IFG.”

Return only if a new causal intervention or structural law gives a prediction that cannot be reduced to generic cross-probe posterior inconsistency.

---

# 2. DRP — Documentation Resource Portfolio in the LLM Era

## Verdict

# **KILL CURRENT FORMULATION**

Original question:

> Under a shared LLM consumer, how should scarce language-documentation effort be allocated among grammar, dictionary, parallel data, IGT/morphology and related resources?

## Direct reasons

### Resource-type value and policy are already active

ICLR 2025 **Can LLMs Really Learn to Translate a Low-Resource Language from One Grammar Book?**
- separates grammatical explanation from parallel examples;
- evaluates several tasks;
- makes a direct collection-policy recommendation.
- https://proceedings.iclr.cc/paper_files/paper/2025/hash/20f44da80080d76bbc35bca0027f14e6-Abstract-Conference.html

ACL 2025 Main **Understanding In-Context Machine Translation for Low-Resource Languages: A Case Study on Manchu**
- already compares dictionary, grammar-book and retrieved-parallel resources.
- https://aclanthology.org/2025.acl-long.429/

### Cost-aware resource allocation is already active

EACL 2026 Findings **Active Learning with Non-Uniform Costs for African Natural Language Processing**
- explicitly models heterogeneous annotation costs and solves a fixed-budget knapsack allocation problem.
- https://aclanthology.org/2026.findings-eacl.349/

### Documentation prioritization is already active

CustomNLP4U 2026 **Customizing ASR for Language Documentation and Resource Prioritization**
- explicitly compares scarce documentation time spent on transcription correction vs alignment.
- https://aclanthology.org/2026.customnlp4u-1.13/

## Why “cross-task + Pareto frontier” does not save it

Grammar writing, dictionary building, transcription, translation and IGT do not share a natural externally validated scalar cost. Without one, the resource-policy estimand weakens into a larger ablation.

Reviewer compression:

> **“A larger cost-aware resource ablation / portfolio optimization.”**

Do not resurrect by adding more resources, tasks, languages, frontier algorithms or author-invented cost units.

Return only if a new estimand/formal cross-resource law cannot be reduced to resource value, acquisition cost, task-specific prioritization or multi-task aggregation.

---

# 3. Generic computational typologist / schema-free grammar querying

## Verdict

# **DO NOT ACTIVATE**

Direct neighborhood:
- EMNLP 2025 Outstanding **LingGym: How Far Are LLMs from Thinking Like Field Linguists?**
  - https://aclanthology.org/2025.emnlp-main.69/
- accepted EMNLP 2026 **LLM Agents as Computational Typologists** is listed by the authors.

Do not claim novelty from:

> LLM reads a grammar, plans evidence retrieval and answers an arbitrary typological question.

A future typology question must have an independent scientific estimand beyond extraction/agent capability.

The stronger variant

> “fixed Grambank schemas are no longer necessary because LLMs can test arbitrary universals directly from grammar prose”

is also **not activated**:
- Nature 2026 excludes many of >2,000 candidate universals for substantive reasons beyond schema coverage;
- no large clean set has yet been shown to be blocked solely by representation;
- gold/operationalization become weaker;
- this risks resurrecting V14's universal-schema kill.

---

# 4. Annotation guidelines as LLM supervision

## Verdict

# **DO NOT ACTIVATE**

Direct neighbors include:
- earlier work on LLM compliance with concept annotation guidelines;
- work using annotation guidelines in information-extraction instruction tuning;
- ACL 2026 Main **Refining and Reusing Annotation Guidelines for LLM Annotation**.
  - https://aclanthology.org/2026.acl-long.1760/

Therefore:

> “guidelines used to train humans; now LLMs can consume them directly”

is already occupied at the parent-method level.

Do not revive as guideline-vs-example ablation.

---

# 5. Dependence-aware aggregation of LLM annotators/judges

## Verdict

# **DIRECT KILL AS NEW RQ**

A superficially strong old-assumption rewrite is:

> Dawid–Skene / majority-vote style aggregation relies on conditional independence; LLM judges share architectures/data/prompts and therefore have correlated errors.

But 2026 **Dependence-Aware Label Aggregation for LLM-as-a-Judge via Ising Models** directly makes this assumption break the core contribution.

- https://arxiv.org/abs/2601.22336

Do not change task/domain and reactivate.

---

# 6. Generic contextual LLM replacement for lexicon-based social-science measurement

## Verdict

# **DO NOT ACTIVATE**

2025–2026 social-science/NLP methodology already directly compares lexicon, supervised, transformer and LLM measurement/annotation paradigms and discusses downstream statistical inference under LLM annotation error.

A candidate needs an object-specific scientific conclusion that changes, not merely:

> contextual LLM measurement is more accurate than dictionaries.

---

# 7. LLM-generated hypotheses + selective inference

## Verdict

# **DO NOT ACTIVATE — MATURE STATISTICAL PARENT**

Attractive formulation:

> LLMs inspect data and generate hypotheses at scale; classical tests assume the tested hypothesis was fixed independently of the evaluation data.

But the load-bearing issue is already classical:
- data snooping / double dipping;
- post-selection inference;
- sample splitting;
- selective inference;
- adaptive data analysis.

Recent data-driven-science work explicitly discusses the same validity problem for machine/AI-assisted hypothesis generation.

Reviewer compression:

> **“Post-selection inference applied to an AI scientist.”**

The LLM changes speed/scale rather than the inferential structure, and the direction also enters a fast-moving scientific-agent lane.

---

# 8. Gradient/token-based typology as an LLM-era replacement for categorical databases

## Verdict

# **DO NOT ACTIVATE**

Corpus/token-based typology already has direct precedent, including quantitative word-order typology and recent multilingual token-based typology.

The claim

> “categorical typological databases are crude; use continuous/token-level evidence”

predates current LLMs.

An LLM semantic extractor does not itself create a new parent question.

---

# 9. Generic corpus representativeness / semantic coverage with LLMs

## Verdict

# **DO NOT REGISTER CURRENT FORM**

Corpus representativeness is a durable old problem, but replacing lexical/topic proxies with stronger semantic embeddings or LLM classifiers does not yet identify a load-bearing assumption that only the LLM era breaks.

Reviewer compression:

> **“A stronger semantic measurement of an old corpus-diversity construct.”**

Return only if a scientific quantity was genuinely unobservable with older representations and the new measurement changes a substantive linguistic conclusion.

---

# 10. Inherited V14 and earlier kills

All V14 entries remain active:
- evaluation item-vs-generation budget;
- historical-linguistics agent hypothesis cycle;
- model-assisted rare-event probability sampling;
- source-language fixed-budget selection;
- generic historical/dialect normalization revisit;
- local-vs-global structured prediction revisit;
- generic WSI/dynamic sense inventory;
- generic universal schema/schema mediation;
- generic corpus/treebank auditing;
- generic MDL + LLM grammar/rule induction.

All V9–V13 kills remain inherited.

---

# V15 anti-resurrection rules

> **Old + important + LLM does not imply new.**

A classic revisit survives only when:
1. the old result/method depends on a precise load-bearing assumption;
2. a modern primitive invalidates that assumption;
3. the break changes a theoretical prediction, optimal policy, measurement model or feasible intervention;
4. the parent reformulation is not already owned by recent literature.

V15 adds:

> **Diagnostic elegance does not restore parent novelty.**

An exact equation, cleaner matched design or stronger control is not enough if another paper already owns the scientific proposition tested by that diagnostic.

And:

> **Larger portfolios do not restore methodological novelty.**

Combining several occupied resource comparisons into one multi-task/cost-aware study is not a new parent question unless the joint estimand yields a distinct scientific law or policy conclusion.
