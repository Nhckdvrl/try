# Old-Problem / New-Method Research-Question Search — 2026-09-06 V14

**Target:** NAACL Main, calibrated against ACL / EMNLP / NAACL Main and especially Best / Outstanding / Best Theme work.  
**Status:** current research-question/search authority after V13.  
**Important:** **NO APPROVED PAPER MAINLINE. NO TARGET-MODEL COMPUTE AUTHORIZED.**

---

# 0. Why V14 exists

V13 correctly broadened the project beyond behavioral/mechanistic gap papers. The current round makes that broadening operational.

The advisor constraint is treated as a design prior:

> Prefer durable, older scientific/NLP problems over fast-moving crowded LLM subfields, especially when the LLM era invalidates an old methodological assumption or makes a previously impractical scientific operation feasible.

High-level precedent confirms that this is a legitimate Main/Outstanding paper identity.

- **EMNLP 2025 Outstanding — Generative or Discriminative? Revisiting Text Classification in the Era of Transformers.** It revisits Efron-style classical generative/discriminative tradeoffs and asks how the classical law changes under modern Transformer architectures.
  - https://aclanthology.org/2025.emnlp-main.486/
  - https://2025.emnlp.org/program/awards/
- **ACL 2025 — Are Optimal Algorithms Still Optimal? Rethinking Sorting in LLM-Based Pairwise Ranking with Batching and Caching.** It shows that an old algorithmic optimality result can change when the cost model changes from comparison count to LLM inference, batching and caching.
  - https://aclanthology.org/2025.acl-short.83/

Therefore the desired shape is not:

> old task + GPT

but one of:

1. **classical law reassessment:** an old scientific prediction depended on assumptions that modern model classes change;
2. **cost/primitive shift:** an old optimal method depended on a computational primitive/cost model that LLMs change;
3. **new measurability:** an old scientific quantity was previously hard to observe at scale, and LLMs make a defensible measurement/intervention newly possible.

---

# 1. V14 additional hard gates

## 1.1 Classical-Assumption Rewrite Gate

Before promoting an old-problem/new-method candidate, write:

> **What exact old assumption no longer holds in the LLM era?**

If the answer is merely:
- models are bigger;
- GPT is better;
- annotation is cheaper;
- prompts are convenient;

then the candidate is not yet a methodological contribution.

A strong candidate must identify a load-bearing assumption whose failure changes:
- a theoretical prediction;
- an optimal algorithm;
- a resource-allocation policy;
- a measurement model;
- or a feasible experimental intervention.

## 1.2 Durability Gate

Ask:

> **If frontier model names, prompting conventions, agent frameworks and APIs all change in two years, does the research question remain important?**

Positive priors:
- linguistic theory;
- statistical inference;
- scientific measurement;
- resource design;
- language documentation;
- classical NLP methodology;
- model-class-independent computational principles.

Negative priors:
- current API quirks;
- current agent frameworks;
- prompt recipes;
- proprietary feature races;
- model-zoo arms races.

---

# 2. Current three-topic front-end set

This is deliberately a **heterogeneous** set. There is no claim that all three have equal maturity.

| topic | paper identity | current verdict |
|---|---|---|
| **IFG — Task-Conditioned Evidence Weighting / Inference–Forecast Gap** | behavioral/scientific discovery | **SERIOUS / D2 / NO COMPUTE** |
| **DRP — Documentation Resource Portfolio in the LLM Era** | resource-allocation / methodology | **SERIOUS-SEARCH CANDIDATE / NO COMPUTE** |
| **TCR — Typological Coverage Robustness under Grammar-Book Expansion** | LLM-enabled scientific measurement / audit | **SERIOUS-SEARCH CANDIDATE / NO COMPUTE** |

**No paper mainline is approved.**

HOM remains search-only and is not counted in the current three-topic front-end set.

---

# 3. Topic 1 — IFG

## 3.1 RQ

> **Does an LLM weight the very same evidence differently depending on whether it is asked what is true now or what will happen next?**

Technical form:

> Under the same DGP, prior and realized signal, does changing only the requested target statistic change the evidence-weighting rule even though latent-state inference and forecast revision are linked by an exact LoIE mapping?

Human anchor:
- Tony Q. Fan, Yucheng Liang, Cameron Peng. *The Inference-Forecast Gap in Belief Updating*. Econometrica 2026.
- https://onlinelibrary.wiley.com/doi/10.3982/ECTA23334

## 3.2 Why it remains non-obvious

The Econometrica design supplies an exact no-gap condition from the Law of Iterated Expectations. An incorrect/non-Bayesian posterior can still be internally coherent if forecast revision is derived from that same posterior.

Thus the decisive question is not:
> are LLMs Bayesian?

It is:
> **does the task request itself select a different update computation?**

## 3.3 Collision boundary

BayesBench 2026 already owns the broad law:
> better latent inference does not reliably transfer to downstream prediction.

BayesBench:
- https://arxiv.org/abs/2606.30850

Its recommender environment directly elicits a latent-type posterior and a held-out rating prediction from the same history and tests conditioned prediction. Therefore IFG may not claim:
- generic inference/prediction inconsistency;
- generic "knows but cannot use";
- generic latent-state readout failure.

IFG survives only because its paired readouts are connected by a minimal exact known-DGP/LoIE mapping rather than unseen-item generalization.

## 3.4 Data

**D2.**
Published human experimental materials, DGPs, instructions, human responses and a public replication package already exist.

## 3.5 Immediate kill criteria

KILL if:
1. another paper owns the same-evidence paired inference→forecast estimand;
2. the tasks cannot be computationally matched;
3. infer-then-map control removes the apparent gap;
4. output-scale/arithmetic difficulty explains the effect;
5. the only conclusion is "LLMs are imperfect Bayesians" or "LLMs replicate human IFG."

---

# 4. Topic 2 — DRP: Documentation Resource Portfolio in the LLM Era

Working title:

> **What Should We Document for an LLM? Reallocating Scarce Language-Documentation Resources Across Dictionaries, Grammars, Parallel Text and IGT**

## 4.1 One-sentence RQ

> **When one foundation model can directly consume dictionaries, grammar descriptions, parallel examples and interlinear annotations, how should scarce documentation effort be allocated across these resource types to maximize reusable capability across language tasks?**

## 4.2 Old problem

Language documentation has always faced scarcity:
- speaker/linguist time is limited;
- transcription, translation and IGT are expensive;
- dictionaries, descriptive grammars, elicited paradigms and natural texts serve different scientific purposes.

This predates LLMs by decades.

A useful historical methodological anchor is the field-linguistics principle that text collection and elicitation provide complementary evidence rather than one universally dominating the other.

## 4.3 What changed in the LLM era

Historically these resource types fed different bespoke pipelines.

An instruction-tuned LLM can now consume all of them through one inference interface:
- dictionary entries;
- grammar-book excerpts;
- retrieved parallel examples;
- morphological analyses / IGT.

This makes **cross-resource substitution and complementarity directly comparable within one model class**, creating a resource-portfolio question that was difficult to formulate cleanly before.

## 4.4 Pre-result scientific tension

### H1 — Reusable-description account
Grammar and lexicon are broad scientific assets; although expensive, they should transfer across many downstream tasks and therefore have high portfolio value.

### H2 — Demonstration-dominant account
Modern LLMs mainly exploit concrete examples. Parallel demonstrations/dictionaries may dominate explicit grammatical description even across tasks.

### H3 — Task-complementarity account
No resource globally dominates: the optimal portfolio changes qualitatively by task, and resource combinations have non-additive value.

This tension is already suggested by conflicting recent evidence.

- ACL 2024 Findings **Hire a Linguist!** uses dictionaries, grammar books and morphological analysis across five tasks/eight languages and shows linguistic descriptions can materially help.
  - https://aclanthology.org/2024.findings-acl.925/
- ACL 2025 Main **Understanding In-Context Machine Translation for Low-Resource Languages: A Case Study on Manchu** finds dictionaries and retrieved parallel examples helpful while grammar books contribute little to MT.
  - https://aclanthology.org/2025.acl-long.429/
- ACL 2025 Main **Read it in Two Steps** identifies grammar-rule retrieval/application bottlenecks and improves grammar use with code-formatted rules.
  - https://aclanthology.org/2025.acl-long.202/
- EMNLP 2025 **Explicit Learning and the LLM in Machine Translation** finds measurable but complexity-sensitive learning from grammar explanations.
  - https://aclanthology.org/2025.emnlp-main.1599/

These papers make the question more—not less—interesting, because they disagree about the computational value of resource types under different tasks/designs.

## 4.5 Surviving novelty

The contribution cannot be:
> which resource helps low-resource MT?

That is occupied.

It must be:

> **cross-task marginal and complementary value of independently existing documentation resource types under a shared resource budget, with the scientific goal of informing what documentation effort is computationally reusable in the LLM era.**

This is a resource-policy/methodology question, not a new prompting pipeline.

## 4.6 Data path

Target D0–D2:
- existing grammar books;
- existing dictionaries;
- existing parallel corpora;
- existing IGT/morphological resources;
- existing downstream test sets.

Potentially useful multilingual substrates already exist in LingoLLM/GlossLM/ODIN and low-resource MT/documentation projects.

A clean contamination control can use enciphered forms where appropriate, following existing ACL precedent rather than inventing a synthetic language ontology.

The **main unresolved data issue is cost**. Do not invent arbitrary "expert-hour" labels. Promotion requires either:
- independently documented annotation/fieldwork time estimates;
- actual project logs;
- or a resource-budget formulation whose units are scientifically defensible.

## 4.7 Reviewer compression

> "This is just a bigger resource ablation across several tasks."

This compression is currently the main threat.

The candidate survives only if the paper estimates a genuine **resource portfolio / marginal-value frontier** and yields a stable documentation-policy conclusion that single-task ablations cannot answer.

## 4.8 Kill criteria

KILL if:
1. a recent paper already optimizes cost-normalized resource portfolios across these resource types/tasks;
2. resource cost cannot be externally grounded;
3. conclusions reduce to "parallel examples help MT, grammar helps grammar";
4. results are model/prompt-specific with no stable resource-policy law;
5. proving the claim requires collecting a new bespoke multilingual resource campaign.

## 4.9 Verdict

> **SERIOUS-SEARCH CANDIDATE / NO COMPUTE.**

Do not implement until the cost/provenance and direct-parent audit are complete.

---

# 5. Topic 3 — TCR: Typological Coverage Robustness under Grammar-Book Expansion

Working title:

> **Would Linguistic Universals Survive Better Coverage? LLM-Assisted Sensitivity Analysis of Typological Conclusions**

## 5.1 One-sentence RQ

> **When grammar books let us fill typological evidence that was previously missing because of documentation/coding limits, which claimed cross-linguistic universals remain stable and which depend on the historical coverage pattern of the database?**

## 5.2 Old scientific problem

Typological databases have long supported claims about:
- linguistic universals;
- feature dependencies;
- genealogical constraints;
- areal patterns.

But missingness and uneven documentation are a longstanding methodological limitation.

Grambank itself contains 195 features over roughly 2,467 varieties and still has missing cells; its 2023 analysis reports substantially less missingness than WALS but nevertheless requires cropping/imputation for some analyses.

- https://grambank.clld.org/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10115409/

## 5.3 What changed in the LLM era

Thousands of grammatical descriptions exist outside the structured database.

2026 SIGTYP shows that grammar-book RAG can recover Grambank feature values from reference material:
- **A RAG Approach for Typological Database Completion**
- https://aclanthology.org/2026.sigtyp-main.7/

Therefore database coverage is no longer purely a fixed human-coding constraint. It can become an experimentally manipulated quantity.

## 5.4 Pre-result scientific tension

### H1 — Robust-universal account
Missingness mostly affects power. Expanding coverage changes uncertainty but not the direction/support of well-founded universals.

### H2 — Documentation-selection account
Historical documentation/database inclusion is structured by family, region and feature salience. Filling missing evidence can materially weaken, strengthen or reverse apparent universals.

### H3 — Measurement-error account
Automatic extraction mainly adds noisy labels; apparent changes are attenuation/error artifacts unless extraction uncertainty is propagated.

These accounts make distinct predictions before expansion.

## 5.5 Existing scientific anchor

Nature Human Behaviour 2026:
- **Enduring constraints on grammar revealed by Bayesian spatiophylogenetic analyses**
- tests 191 reformulated universals using Grambank;
- controls for genealogy and geography;
- finds support for roughly one third;
- releases data/code.
- https://www.nature.com/articles/s41562-025-02325-z

That paper gives an unusually strong, externally defined scientific target for sensitivity analysis.

## 5.6 Surviving novelty

The contribution cannot be:
> use LLM/RAG to fill Grambank.

That parent is occupied by SIGTYP 2026.

The surviving question is:

> **Does LLM-enabled expansion of previously missing typological evidence change the substantive scientific conclusions drawn from the database?**

This changes the estimand from **feature-prediction accuracy** to **robustness of scientific inference under coverage intervention**.

## 5.7 Data/gold path

Strong D0/D1 structure:
1. use already-coded Grambank cells as masked extraction gold;
2. use existing grammar books/sketches as evidence;
3. pre-register a set of already published universals/feature relations;
4. reuse existing spatiophylogenetic analysis code;
5. propagate extraction uncertainty rather than treating LLM labels as perfect;
6. manually validate only the load-bearing newly extracted cells/relations.

No bespoke linguistic world or author-defined truth labels are required.

## 5.8 Reviewer compression

> "This is Grambank RAG plus rerunning a Nature paper."

This is a serious threat.

A valid rebuttal requires:
- targeted coverage expansion based on documented missingness structure;
- uncertainty-aware inference;
- a pre-specified scientific robustness estimand;
- conclusions about which typological claims are coverage-stable versus coverage-sensitive.

If the paper is mainly an extraction benchmark, KILL.

## 5.9 Kill criteria

KILL if:
1. recent work already studies downstream universals/correlations after LLM-driven database expansion;
2. grammar sources for missing cells are inaccessible/unreliable at useful scale;
3. extraction error dominates any scientific sensitivity estimate;
4. only a trivial handful of universals can change;
5. the strongest conclusion is merely "more data improves confidence intervals."

## 5.10 Verdict

> **SERIOUS-SEARCH CANDIDATE / NO COMPUTE.**

This is currently the strongest newly broadened non-behavioral topic, but still needs a direct-parent literature audit before implementation.

---

# 6. Why these three and not three mechanistic topics

The set intentionally spans three paper identities:

1. **IFG:** a clean structural behavioral discovery question;
2. **DRP:** an old resource-allocation problem whose feasible decision surface changes because one LLM can consume heterogeneous linguistic resources;
3. **TCR:** an old scientific-inference problem where LLM extraction turns historical database coverage into a manipulable variable.

This is closer to the requested advisor-compatible portfolio than three variants of:
> find an LLM bias / gap / mechanism.

---

# 7. Search failures from the V13→V14 expansion

The following directions were explicitly explored and rejected or closed. See the V14 kill ledger for anti-resurrection detail.

- historical/comparative-linguistics "agent hypothesis cycle";
- evaluation-budget allocation across test items vs repeated stochastic generations;
- model-assisted rare-event probability sampling with unbiased prevalence estimation;
- source-language selection / budget allocation for cross-lingual transfer;
- historical/dialect normalization as a generic "is preprocessing still needed?" question;
- local-vs-global structured prediction / classical label-bias revisit;
- generic Word Sense Induction / dynamic sense inventory modernization;
- generic cross-schema/universal-schema replacement;
- generic corpus/treebank annotation auditing;
- generic MDL + LLM rule/grammar induction.

The repeated lesson:

> **Old is not novel. The LLM must invalidate a load-bearing old assumption, not merely become a stronger component in an old pipeline.**

---

# 8. Next work before any compute

## IFG
Complete remaining direct collision audit and exact experimental reconstruction.

## DRP
1. search exact resource-portfolio / documentation-budget parent literature;
2. identify 3–5 languages with independently existing heterogeneous resources and multiple task golds;
3. find defensible resource-cost evidence;
4. construct a no-compute portfolio estimand and kill sentence.

## TCR
1. map the 191 Nature universals to missing Grambank cells/languages;
2. quantify how much additional grammar evidence is actually available;
3. audit all work on typological missing-data correction/database completion;
4. define uncertainty propagation for extracted feature values;
5. estimate whether enough universals are identifiable to support a Main-scale claim.

---

# 9. V14 authority

> **Do not search only for new LLM behaviors. Search for old, durable scientific or NLP problems whose load-bearing assumptions are changed by the LLM era.**

> **Old task + GPT is not a contribution. Old assumption + new model class + changed prediction/method/measurement can be.**

And retain all previous rules:

> **The scientific object should exist before us.**  
> **The data should exist before our hypothesis.**  
> **The scientific tension should exist before the result.**  
> **The structural relation should exist before the gap.**  
> **The new method should change what science can test, not just who performs the work.**
