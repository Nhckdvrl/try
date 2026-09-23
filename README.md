# Research project — V17 Natural Main-Level RQ Standard

Primary target: **NAACL Main**.

Calibration:
- ACL Main;
- EMNLP Main;
- NAACL Main;
- especially Best / Outstanding / Best Theme papers.

> **NO APPROVED PAPER MAINLINE.**
>
> **ONE PILOT EXCEPTION IS ACTIVE:** Unring the Bell / G23A v3.
>
> **TARGET-MODEL COMPUTE IS AUTHORIZED ONLY FOR THE FROZEN G23A v3 PILOT.**

---

## Current authority

1. [NATURAL_MAIN_RQ_STANDARD_2026-09-06_V17.md](NATURAL_MAIN_RQ_STANDARD_2026-09-06_V17.md)
   — **current concise selection standard and candidate generator.**
2. [archive/KILLED_RQ_LEDGER_2026-09-06_V17.md](archive/KILLED_RQ_LEDGER_2026-09-06_V17.md)
   — **current kill / do-not-reactivate authority.**
3. [STATUS.md](STATUS.md)
   — compact current state.
4. [SASANO_LAB_LOCAL_PRIOR_RQ_SEARCH_2026-09-06_V16.md](SASANO_LAB_LOCAL_PRIOR_RQ_SEARCH_2026-09-06_V16.md)
   — local-lab audit and provenance.

Older methodology/search documents remain historical provenance, not current authority.

---

## V17 in one sentence

> **A natural, durable NLP/language problem; one genuinely new scientific axis inside it; trustworthy simple data and independent gold; a parent-level novel question with multiple informative outcomes; and a small decisive experiment that can naturally grow into a Main paper.**

Short form:

> **Real object. New axis. Good data. New parent question. Decisive paper.**

And:

> **Search locally, judge globally.**

---

## Five hard gates

A candidate reaches pilot only if all are YES:

1. **REAL OBJECT** — naturally important, understandable, durable.
2. **NEW AXIS** — one non-obvious relation; at least two plausible accounts.
3. **GOOD DATA** — simple credible data; independent gold.
4. **NEW PARENT** — parent novelty survives reviewer compression.
5. **DECISIVE PAPER** — outcome-robust, natural C1→C2→C3, manageable workload.

Any clear failure:

> **KILL BEFORE COMPUTE.**

---

## Data priority

Prefer:
1. existing natural dataset/corpus/resource;
2. published human/linguistic materials;
3. small controlled theory-grounded stimuli.

Avoid by default:
- large synthetic worlds;
- template-heavy author-built datasets;
- LLM-generated main evidence;
- LLM-as-judge gold;
- complicated data construction needed only to make the RQ exist.

---

## Current state

| object | status |
|---|---|
| IFG | KILL |
| DRP | KILL |
| TCR | KILL / ARCHIVE |
| HOM | KILL CURRENT FORMULATION |
| CK | KILL |
| PD | ARCHIVE / DO NOT ACTIVATE |
| Unring the Bell / G23A | **PILOT AUTHORIZED — v3 ONLY** |
| active candidate | **G23A v3 only** |
| approved mainline | **NONE** |

There is no candidate-count quota.

The G23A exception does not promote Unring the Bell to an approved paper mainline.
It authorizes one frozen, decisive pilot under
`g23a-zero-gating-design-v3`; the outcome determines whether the line advances.

---

## Search region

Highest prior:
- lexical semantics / semantic access;
- compositional and implicit meaning;
- factual / parametric knowledge;
- linguistic inference;
- established linguistic phenomena;
- structured semantic/NLP relations;
- stable evaluation/measurement units.

Conditional:
- causal interpretability;
- diffusion/generation dynamics;
- efficiency/compression;
- Japanese-specific phenomena.

Only enter conditional lanes after a strong concrete scientific object is identified.

Low prior:
- generic agents;
- generic RAG;
- prompt tricks;
- LLM-as-judge/annotator;
- broad cognitive-bias transplantation;
- behavioral-economics phenomenon hunting;
- typology/documentation policy;
- bespoke synthetic worlds;
- mechanism-first feature hunting.

---

## Mechanism rule

Deep evidence is required; activation patching is not.

> **Use the simplest evidence strong enough for the claim.**

Mechanistic causal intervention is required only when the central claim is mechanistic/causal.

Never add mechanism merely to make a weak question look deep.


---

## G23A pilot authorization — 2026-09-23

Authorized target-model compute is limited to the exact frozen design at
`g23a-zero-gating-design-v3` / commit
`c8a4dc6a48e407fe529c2fb5e35061064a858c5c`.

Authorized panel:
- Qwen3-8B;
- Gemma-3-12B;
- Mistral-Small-24B.

Authorized scope:
- 12 frozen decision conditions;
- 13 frozen probes;
- 72 frozen items;
- 5,400 generations total across the three checkpoints.

Run the complete frozen panel before inspecting or interpreting model-specific G23A
outcomes. Then run the frozen analyzer once over the complete panel.

Not authorized by this exception:
- G23B;
- new mechanism runs;
- checkpoint substitution after seeing results;
- extra models for robustness;
- changes to materials, conditions, probes, estimand, gates, exclusions, bootstrap,
  or verdict logic after generation starts.

A checkpoint that fails to load is reported by name and is not replaced.
