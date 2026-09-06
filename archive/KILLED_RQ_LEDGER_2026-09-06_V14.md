# Killed Research-Question Ledger — 2026-09-06 V14

**Status:** current kill / do-not-reactivate authority.  
**Inherits:** `archive/KILLED_RQ_LEDGER_2026-09-06_V13.md` and all earlier ledgers.  
**Rule:** V13 remains full provenance; this file records new V14 closures and is the current top-level authority.

---

# 1. Evaluation stochasticity / item-vs-generation budget

## Proposed question

> With a fixed benchmark budget, should LLM evaluation spend calls on more test items or more stochastic generations per item?

**KILL — DIRECT 2026 METHODOLOGICAL OCCUPATION.**

ACL 2026 Findings **Beyond the Singular: Revealing the Value of Multiple Generations in Benchmark Evaluation** already introduces hierarchical statistical modeling that explicitly incorporates benchmark/item variation and LLM generation randomness and motivates multiple generations.

Adjacent 2026 variance-decomposition work further separates scenario/generation/judge sources and studies allocation.

Do not revive as:
- hierarchical bootstrap for LLMs;
- repeated-run confidence intervals;
- optimal number of generations;
- stochastic leaderboard stability.

A new evaluation direction would need a different estimand, not another allocation rule for the same variance components.

---

# 2. Comparative/historical-linguistics LLM hypothesis-cycle agent

**KILL CURRENT FORMULATION — PARENT METHOD NOW OCCUPIED.**

The attractive formulation was:
> propose sound-correspondence rule → search counterexamples → revise rule → reconstruct.

But:
- ACL 2025 Main **Programming by Example meets Historical Linguistics** already formulates sound-law induction with LLMs;
- ACL 2026 work explicitly induces sound-change rules from Middle Chinese to modern dialects;
- computational historical linguistics already automates correspondence learning, cognacy and reconstruction.

Do not resurrect by adding an agent loop, reflection or counterexample-search wrapper.

Return only with a genuinely different scientific estimand, not a more autonomous pipeline.

---

# 3. Model-assisted rare-event probability sampling

## Proposed question

> Can an LLM/model oversample likely rare positives while known inclusion probabilities preserve unbiased corpus prevalence/effect estimates?

**DIRECT KILL — SAME STATISTICAL PARENT ALREADY OCCUPIED.**

2026 work on measuring policy-violating content already combines model-assisted unequal-probability sampling with design-based prevalence estimation and LLM labeling.

Moving the application from policy-violating content to rare linguistic phenomena does not create a new methodological parent.

Do not resurrect via:
- corpus linguistics;
- sociolinguistics;
- semantic phenomena;
- "importance weighting" terminology.

---

# 4. Source-language selection / budget-constrained multilingual transfer

**KILL AS A SEARCH LANE.**

The parent question is now directly active in 2026:
- systematic genetic/geographic/embedding-based source-language selection;
- **Budget-Xfer**, explicitly formulating source-language/data allocation under a fixed annotation budget.

Do not use:
> "which related language should teach the target LLM?"

as an old-problem/new-method candidate.

---

# 5. Historical/dialect normalization — "is normalization still necessary in the LLM era?"

**DO NOT ACTIVATE CURRENT FORMULATION.**

Why it looked attractive:
- normalization is a long-standing preprocessing response to sparsity/orthographic variation;
- strong LLMs can increasingly process nonstandard/historical forms directly;
- normalization can erase scientifically meaningful dialect/diachronic signals.

Why not promoted:
- the downstream value of historical normalization was already questioned in NAACL 2018;
- NAACL 2024 work explicitly develops normalization that preserves historical wordforms rather than modernizing them;
- 2025–2026 LLM/dialect work is already dense around normalization and dialect robustness;
- August 2026 work directly benchmarks invariance to meaning-preserving Vietnamese dialect forms.

Reviewer compression:
> "A preprocessing ablation: normalization helps nuisance variation but removes signal."

That is too foreseeable and too small for the current standard.

Return only with a stronger classical law/estimand that is not generic raw-vs-normalized comparison.

---

# 6. Local vs global structured prediction / label-bias revisit

**KILL CURRENT LLM-ERA REVISIT.**

EACL 2026 already directly studies prompt-based structured prediction combined with combinatorial/global inference and shows structured objectives/inference retain value in the LLM era.

Earlier neural/autoregressive work also connects classical label-bias/local-normalization issues to modern sequence models.

Do not revive by changing the structured task.

---

# 7. Generic WSI / dynamic sense-inventory modernization

**DO NOT ACTIVATE.**

Why:
- WSI is a durable old problem;
- recent work explicitly states that WSI remains unsolved in the LLM era;
- however, LLM-generated definitions/sense induction and task/application-specific sense inventories are already active/old ideas.

A formulation like:
> "let the LLM create a task-specific sense inventory"

is not yet a new parent question.

Return only if a classical assumption about lexical-semantic measurement is genuinely invalidated and a new structural estimand follows.

---

# 8. Generic universal-schema / schema-mediation replacement

**DO NOT ACTIVATE.**

Natural-language definitions/guidelines may let LLMs operate across schemas, but 2025–2026 work already studies:
- unseen schema information extraction;
- schema shifts;
- ontology/schema alignment;
- label-definition adherence;
- LLM-refined taxonomies.

Do not use:
> "Do we still need one canonical schema?"

without a scientific inference result that cannot be compressed to schema alignment.

---

# 9. Generic corpus/treebank annotation auditing

**DO NOT ACTIVATE.**

LLM-assisted corpus/treebank/discourse annotation auditing is already being directly explored, including cross-model agreement and under-annotation discovery.

A future audit must alter scientific inference or measurement validity, not simply find more annotation errors.

---

# 10. Generic MDL + LLM grammar/rule induction

**DO NOT ACTIVATE.**

MDL is a mature grammar-induction principle, and 2026 ACL work already uses MDL-guided LLM rule learning for tool adaptation; concurrent grammar-induction work combines LLMs, Bayesian priors and explicit rules.

Do not revive as:
> "LLM proposes grammar rules, MDL selects the shortest set."

A natural-language grammar candidate needs a genuinely new scientific question beyond rule compression/generalization.

---

# 11. Anti-resurrection rule added in V14

> **An old problem is not protected by age.**

For any "classic problem revisited" direction, search the abstract parent:
- old law;
- old cost model;
- old measurement assumption;
- old data-acquisition decision.

If a recent paper already changes that parent with modern models, a new task/domain is an exact cell.

> **The LLM-era contribution must identify which old assumption breaks and why that changes the scientific conclusion or optimal method.**
