# Killed Research-Question Ledger — 2026-09-06 V15

**Status:** current kill / do-not-reactivate authority.  
**Inherits:** V14 and all earlier ledgers.  
**Rule:** a new domain/task/model name does not revive an occupied parent question.

---

# 1. DRP — Documentation Resource Portfolio in the LLM Era

## Verdict

# **KILL CURRENT FORMULATION**

Original question:

> Under a shared LLM consumer, how should scarce language-documentation effort be allocated among grammar, dictionary, parallel data, IGT/morphology and related resources?

## Direct reasons

1. ICLR 2025 **Can LLMs Really Learn to Translate a Low-Resource Language from One Grammar Book?** already separates grammatical explanation from parallel examples, tests multiple tasks, and makes a data-collection recommendation: task-appropriate evidence matters; parallel examples dominate for MT while grammatical information is more useful for linguistic tasks.
2. 2026 **Customizing ASR for Language Documentation and Resource Prioritization** explicitly treats scarce documentation time as an allocation problem and compares correction vs alignment effort.
3. Finite-budget annotation/resource allocation has substantial older methodological precedent.
4. Grammar, dictionary, IGT, transcription and parallel corpora are not independent commodities; a universal scalar cost would require strong author-imposed accounting assumptions.
5. Without a defensible cost model, the paper collapses to a cross-task resource ablation.

Do not resurrect by adding more resources/tasks/languages or by inventing cost units.

---

# 2. Generic computational-typologist / schema-free grammar querying

## Verdict

# **DO NOT ACTIVATE**

EMNLP 2026 already contains **LLM Agents as Computational Typologists**, following EMNLP 2025 Outstanding **LingGym** and recent grammar-book typological extraction work.

Do not claim novelty from:

> LLM reads a grammar, plans evidence retrieval, and answers an arbitrary typological question.

A future typology question must have an independent scientific estimand beyond the extraction/agent capability.

---

# 3. Generic multi-probe posterior inconsistency

## Verdict

# **DO NOT ACTIVATE**

Recent 2026 Bayesian/hypothesis-updating work already measures the same posterior through multiple elicitation/probe modes and reports non-equivalence.

Together with BayesBench and value/belief-action work, the parent

> “different probes reveal different beliefs”

is occupied.

IFG is not exempt: it survives only through a pre-existing exact LoIE mapping plus target-statistic intervention.

---

# 4. Annotation guidelines as LLM supervision

## Verdict

# **DO NOT ACTIVATE**

Direct neighbors include:
- ACL 2024 work on whether LLMs can follow concept annotation guidelines;
- ACL 2025 work using annotation guidelines in event-extraction instruction tuning;
- ACL 2026 Main **Refining and Reusing Annotation Guidelines for LLM Annotation**.

Therefore the old-assumption story

> “guidelines used to train humans; now LLMs can consume them directly”

is already occupied at the parent-method level.

Do not revive as guideline-vs-example ablation.

---

# 5. Dependence-aware aggregation of LLM annotators/judges

## Verdict

# **DIRECT KILL AS NEW RQ**

A superficially strong old-assumption rewrite is:

> Dawid–Skene / majority-vote style aggregation relies on conditional independence; LLM judges share architectures/data/prompts and therefore have correlated errors.

But 2026 **Dependence-Aware Label Aggregation for LLM-as-a-Judge via Ising Models** already directly makes this assumption break the core contribution.

Do not change task/domain and reactivate.

---

# 6. Generic contextual LLM replacement for lexicon-based social-science measurement

## Verdict

# **DO NOT ACTIVATE**

2025–2026 social-science/NLP methodology already directly compares lexicon, supervised, transformer and LLM measurement/annotation paradigms and discusses downstream statistical inference under LLM annotation error.

A candidate needs an object-specific scientific conclusion that changes, not merely:

> contextual LLM measurement is more accurate than dictionaries.

---

# 7. Inherited V14 and earlier kills

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

# Anti-resurrection rule

> **Old + important + LLM does not imply new.**

A classic revisit survives only when:
1. the old result/method depends on a precise load-bearing assumption;
2. a modern primitive invalidates that assumption;
3. the break changes a theoretical prediction, optimal policy, measurement model or feasible intervention;
4. the parent reformulation is not already owned by recent literature.
