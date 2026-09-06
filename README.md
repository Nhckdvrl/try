# Research project — Non-Obviousness-First RQ reconstruction

Target: **NAACL Main**, calibrated against ACL / EMNLP / NAACL Main and especially Best / Outstanding / Best Theme papers.

> **NO APPROVED PAPER MAINLINE YET.**
>
> Current candidate authority:
> **V12 NON-OBVIOUSNESS-FIRST SEARCH.**
>
> There is **one serious candidate under front-end audit** and **no compute authorization yet**.

---

## Current authority

Read in this order:

1. [ALIGNMENT_FIRST_RQ_STANDARD_2026-09-06.md](ALIGNMENT_FIRST_RQ_STANDARD_2026-09-06.md)
   — governing methodology; now includes the hard **Non-Obviousness / Scientific-Tension Gate**.
2. [NON_OBVIOUSNESS_FIRST_RQ_SEARCH_2026-09-06_V12.md](NON_OBVIOUSNESS_FIRST_RQ_SEARCH_2026-09-06_V12.md)
   — **current candidate/search authority**.
3. [DATA_FIRST_RQ_RECONSTRUCTION_2026-09-06_V11.md](DATA_FIRST_RQ_RECONSTRUCTION_2026-09-06_V11.md)
   — data-first provenance and prior CK/HOM audit; superseded where V12 differs.
4. [DATA_FIRST_RQ_AUDIT_2026-09-06_V10.md](DATA_FIRST_RQ_AUDIT_2026-09-06_V10.md)
   — data-first methodology provenance.
5. [DURABLE_RQ_SEARCH_2026-09-06_V9_FINAL3.md](DURABLE_RQ_SEARCH_2026-09-06_V9_FINAL3.md)
   — older novelty/history provenance only.
6. [archive/KILLED_RQ_LEDGER_2026-09-06_V12.md](archive/KILLED_RQ_LEDGER_2026-09-06_V12.md)
   — current kill authority.
7. [STATUS.md](STATUS.md)
   — compact current state.

---

## Current search state

| object | status |
|---|---|
| **IFG — Task-Conditioned Evidence Weighting / Inference–Forecast Gap** | **SERIOUS CANDIDATE / D2 / CONTINUE FRONT-END AUDIT / NO COMPUTE** |
| **HOM — Plural Homogeneity / Truth-Value Gaps** | **DEMOTED / SEARCH-ONLY / NO COMPUTE** |
| **PD — Partition Dependence** | **SCREENED / NOT ACTIVE** |
| **CK — Finite Mutual Knowledge vs Common Knowledge** | **KILL CURRENT FORMULATION** |
| **AE** | **KILL** |
| **GRN** | **KILL** |

There is no requirement to maintain three candidates.

---

## Current serious question

### IFG

> **Does an LLM weight the very same evidence differently depending on whether it is asked what is true now or what will happen next?**

Why it is being taken seriously:
- the question contains a non-obvious tension before any LLM is run;
- inference and forecast revision can be paired under the same DGP, prior, and realized signal;
- the Law of Iterated Expectations supplies an exact no-gap benchmark;
- Econometrica 2026 provides published human experiments, instructions, human results, and a public replication package;
- current close LLM neighbors (especially BayesBench) study inference/prediction more broadly but do not appear to own the exact matched same-evidence task-conditioned update estimand.

This is **not** yet a paper mainline and **not** yet pilot-authorized.

See V12 for the full candidate card and kill criteria.

---

## New hard question-quality rule

Default KILL form:

> “Theory says X and Y are different. Does the model know/distinguish X and Y?”

A candidate must be interesting **before** results.

Prefer questions that expose:
- an invariance violation;
- representation/use or statement/action dissociation;
- irrelevant-information leakage;
- a principled computation vs learned-prior conflict;
- a qualitative training/model-regime split;
- another independently motivated scientific tension.

> **Good data cannot rescue an obvious question.**

---

## Compute boundary

Currently not authorized:
- IFG target-model pilot until final neighboring-paper/data inspection is complete;
- CK;
- HOM;
- PD;
- AE;
- GRN;
- model-zoo sweeps;
- mechanisms/SAE/patching/steering;
- LoRA/RL;
- synthetic benchmark expansion.

For any future promoted candidate:

```
high-level question-shape calibration
→ non-obviousness/scientific-tension gate
→ novelty assassination
→ data provenance/gold audit
→ minimum decisive pilot
→ “Models ...” structural law
→ post-result literature assassination
→ Main/Findings/KILL
```

> **Question quality first. No forced candidate count.**
