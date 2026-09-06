# Project status — 2026-09-06, V12 NON-OBVIOUSNESS-FIRST

> **NO APPROVED PAPER MAINLINE.**
>
> **NO TARGET-MODEL COMPUTE AUTHORIZED YET.**

Current methodology:
[ALIGNMENT_FIRST_RQ_STANDARD_2026-09-06.md](ALIGNMENT_FIRST_RQ_STANDARD_2026-09-06.md)

Current candidate/search authority:
[NON_OBVIOUSNESS_FIRST_RQ_SEARCH_2026-09-06_V12.md](NON_OBVIOUSNESS_FIRST_RQ_SEARCH_2026-09-06_V12.md)

Current kill authority:
[archive/KILLED_RQ_LEDGER_2026-09-06_V12.md](archive/KILLED_RQ_LEDGER_2026-09-06_V12.md)

Data-first provenance:
[DATA_FIRST_RQ_RECONSTRUCTION_2026-09-06_V11.md](DATA_FIRST_RQ_RECONSTRUCTION_2026-09-06_V11.md)

---

## Governing correction in V12

Naturalness + novelty + D0–D2 data are still insufficient when the research question itself is obvious.

New hard gate:

> **A Main-level scientific question must contain a non-obvious tension before the experiment is run.**

Default weak form:

> “X and Y are theoretically different; does the model distinguish them?”

This correction demotes/kills candidates that previously survived primarily because their scientific objects and data were clean.

High-level calibration:
- NAACL 2025 **Semantic Leakage** — irrelevant information changes generation;
- EMNLP 2025 Outstanding **Value–Action Gap** — stated values and actions diverge;
- ACL 2026 Outstanding **DH Gap** — representation changes risky choice, with reasoning/conversational regime split;
- ACL 2026 Best **Imperfective Paradox** — Teleological Bias overrides the licensed semantic computation.

---

## Current ranking

### #1 IFG — Task-Conditioned Evidence Weighting / Inference–Forecast Gap

**Status:** SERIOUS CANDIDATE / D2 / CONTINUE FRONT-END AUDIT / NO COMPUTE.

RQ:

> **Does an LLM weight the very same evidence differently depending on whether it is asked what is true now or what will happen next?**

Why it survives:
- same DGP + same prior + same realized signal;
- inference and forecast revision are normatively linked by LoIE;
- human Econometrica 2026 work finds underreaction in inference and overreaction in forecast revision;
- the replication package and experimental instructions exist independently of our LLM hypothesis;
- BayesBench is a major neighbor but currently does not appear to run the exact paired same-evidence IFG estimand.

Remaining threat:
> “This is just Bayesian reasoning / another human cognitive bias.”

Survival requires a within-evidence structural dissociation, not generic Bayesian error or human replication.

### HOM — Plural Homogeneity

**Status:** DEMOTED / SEARCH-ONLY / NO COMPUTE.

Reason:
current question still risks “known formal-semantic distinction → does the model know it?”

D2 data quality remains good but no longer authorizes a pilot by itself.

### PD — Partition Dependence

**Status:** SCREENED / NOT ACTIVE.

Attractive non-obvious invariance violation, D2 and quantitative, but current neighborhood includes broad cognitive-bias work, choice-set effects and EMNLP 2025 confidence distortion with changing numbers/groupings of answer choices.

### CK

**Status:** KILL CURRENT FORMULATION.

Reason:
the primary RQ reduces too easily to a textbook common-knowledge distinction. PNAS D2 materials are excellent, but **good data cannot rescue an obvious question**.

### AE / GRN

Remain KILL under V11 reasons.

---

## Newly killed during V12 search

- simple LLM hindsight bias — directly included in an existing 30-bias LLM evaluation;
- dependent/copy-counted evidence in RAG — direct 2026 collision;
- CK current finite-mutual-vs-common formulation — non-obviousness failure.

These are not backups.

---

## Next work

For IFG only:
1. retrieve/inspect the Econometrica replication package and experimental instructions;
2. reconstruct exact paired inference↔forecast estimand;
3. complete BayesBench line-by-line collision matrix;
4. inspect the 2026 hypothesis-generation/updating evaluation–generation gap;
5. search forecasting/calibration work for same-evidence task-framing experiments;
6. only if the axis remains unoccupied, decide whether a minimum pilot is authorized.

In parallel:
- continue new-topic search from D0–D2 datasets and high-level **question shapes**, not from named human biases;
- do not force a second or third active candidate.

---

## Current one-line rule

> **Do not ask whether the model knows a distinction; ask whether a natural system-level assumption about how the model should use the same information breaks in a surprising, prediction-changing way.**
