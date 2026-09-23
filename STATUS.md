# Project status — 2026-09-23, G23C COMPLETE / THREE-RQ PAPER EXPANSION ACTIVE

> **NO APPROVED PAPER MAINLINE.**
>
> **G23A v3 COMPLETE:** `zero-amplified`, `Δ_zero = +8.83 [+4.39,+13.33]`.
>
> **G23B v1 STOPPED AT THE FROZEN PHASE-A CARRIER GATE:** `carrier-invalid`.
>
> **G23C v1 COMPLETE:** frozen verdict `target-conditioned-policy-state`,
> L14 `TargetConditioning = +8.15 [+6.91,+9.44]`.
>
> **ACTIVE:** paper-scale three-RQ expansion under
> `PAPER_SCALE_AUDIT_2026-09-23.md`.
>
> **G24A FROZEN AND AUTHORIZED (single experiment):** source-grounded
> natural-evidence confirmation on FEVER + SciFact — prereg
> `preregistrations/PREREGISTRATION_G24A_NATURAL_EVIDENCE.md`, tag
> `g24a-natural-evidence-confirmation-design-v1` (commit `25316a9`, tagged
> before any G24A forward pass), source audit
> `data/external/review/G24A_SOURCE_DATA_AUDIT_v1` PASS 53/53, candidates
> `data/items/g24a_candidates_v1.jsonl` (13,283 items). Compute authorized =
> prereg §11 layout only: selection pass (`base,admit_pre,admit_post`,
> `mistral-small-24b`, no Exclude/probe rows) → selected ≤600-item file per
> §5 quotas (200/200/100/100, τ=10.0, seed 20260924) → main pass (5 frozen
> panel models × 8 kinds, reasoned, max-model-len 4096, 4 local GPUs) →
> `src/analyze_g24a.py`. Nothing else.
>
> **NO OTHER TARGET-MODEL COMPUTE AUTHORIZED.**

Current selection standard:
[NATURAL_MAIN_RQ_STANDARD_2026-09-06_V17.md](NATURAL_MAIN_RQ_STANDARD_2026-09-06_V17.md)

Current kill authority:
[archive/KILLED_RQ_LEDGER_2026-09-06_V17.md](archive/KILLED_RQ_LEDGER_2026-09-06_V17.md)

V16 local-prior provenance:
[SASANO_LAB_LOCAL_PRIOR_RQ_SEARCH_2026-09-06_V16.md](SASANO_LAB_LOCAL_PRIOR_RQ_SEARCH_2026-09-06_V16.md)

---

## V17 governing rule

The previous methodology accumulated too many overlapping gates.

V17 compresses selection into five hard questions:

1. **REAL OBJECT** — Is the NLP/language question naturally important and durable?
2. **NEW AXIS** — Is there one non-obvious structural relation with at least two plausible accounts?
3. **GOOD DATA** — Are the data simple/credible and the gold independent?
4. **NEW PARENT** — Does parent-level novelty survive “This is just X”?
5. **DECISIVE PAPER** — Are several outcomes informative, and can C1→C2→C3 grow naturally with manageable work?

If any core answer is clearly NO:

> **KILL BEFORE COMPUTE.**

---

## Search prior

> **Search locally, judge globally.**

Use recent Sasano-Lab work to keep candidate generation near concrete NLP/language objects:
- lexical / compositional semantics;
- factual/parametric knowledge;
- language understanding/inference;
- structured semantic/NLP resources and relations;
- stable evaluation/measurement questions;
- representation/generation only when tied to a concrete language object.

Use ACL / EMNLP / NAACL Main / Best / Outstanding to set the scientific bar.

Do not copy labmates' exact topics.

---

## Data rule

Strong preference:
1. existing natural dataset/corpus/resource;
2. published human/linguistic materials;
3. small controlled theory-grounded stimuli when necessary.

Strong negative prior:
- large bespoke synthetic worlds;
- LLM-generated main datasets;
- LLM judge as gold;
- complicated author-created contrasts.

> **Data validity can kill a topic before novelty does.**

---

## Current candidate state

| object | status |
|---|---|
| IFG | **KILL** |
| DRP | **KILL** |
| TCR | **KILL / ARCHIVE** |
| HOM | **KILL CURRENT FORMULATION** |
| CK | **KILL** |
| PD | **ARCHIVE / DO NOT ACTIVATE** |
| Unring the Bell / G23A | **COMPLETE — zero-amplified** |
| Unring the Bell / G23B v1 | **STOPPED — carrier-invalid at Phase A** |
| Unring the Bell / G23C | **COMPLETE — target-conditioned-policy-state** |
| Unring the Bell / G23C-R | **DESIGN / PREREG ACTIVE — NO COMPUTE** |
| active candidate | **G23C-R fresh-material mechanism replication** |
| approved mainline | **NONE** |

The clean-slate policy remains the default. G23A is a single explicit exception after
the legacy Unring line was re-audited, the old paper stories were archived, and a
decisive fresh pilot was frozen. This is **not** an approved paper mainline.

TCR is now killed because too much source auditing/database reconstruction and cross-linguistic inference are required before the scientific estimand is even secured.

HOM is now killed because the current question remains a competence check of an established semantic distinction despite excellent data.

---

## Compute boundary

G23A v3, G23B v1 and G23C v1 are closed rounds.

The earlier statement “G23C-R then write” is superseded by
`PAPER_SCALE_AUDIT_2026-09-23.md`.

Current paper target:

- **RQ1 / generality:** G0 breadth + controls + agent setting + a new source-grounded
  natural-evidence confirmation;
- **RQ2 / structural boundary:** G23A zero amplification + explicit/verifiable
  prospective-zero controls + policy-access/enforcement dissociation;
- **RQ3 / mechanism:** Stage 5 + G23C + donor-vs-recipient causal factorization +
  fresh-material replication.

Immediate authorized work is **design only**:
- design G24A on source-grounded evidence datasets;
- audit dataset licensing/provenance, estimand and selection rules;
- write implementation/tests without target-model generation;
- refine G24B and G23C-R only at design level.

Not authorized:
- G24A generation before its own freeze/tag/authority update;
- G24B patching;
- G23C-R forward passes;
- new layer/site/model searches;
- any new carrier rescue;
- arbitrary “extra ablations” not tied to RQ1/RQ2/RQ3.

Next compute authorization must name a single frozen experiment and its exact scientific
gap.
