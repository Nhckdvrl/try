# Project status — 2026-09-23, V17 + G23A PILOT EXCEPTION

> **NO APPROVED PAPER MAINLINE.**
>
> **ACTIVE PILOT:** Unring the Bell / G23A v3.
>
> **TARGET-MODEL COMPUTE AUTHORIZED ONLY FOR THE FROZEN G23A v3 PILOT.**

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
| Unring the Bell / G23A | **PILOT AUTHORIZED — v3 ONLY** |
| active candidate | **G23A v3 only** |
| approved mainline | **NONE** |

The clean-slate policy remains the default. G23A is a single explicit exception after
the legacy Unring line was re-audited, the old paper stories were archived, and a
decisive fresh pilot was frozen. This is **not** an approved paper mainline.

TCR is now killed because too much source auditing/database reconstruction and cross-linguistic inference are required before the scientific estimand is even secured.

HOM is now killed because the current question remains a competence check of an established semantic distinction despite excellent data.

---

## Compute boundary

Default rule remains: no target-model compute until a candidate clears the V17 pilot
bar.

### Explicit exception — G23A v3

**Authorized now:** the exact frozen G23A design at
`g23a-zero-gating-design-v3`, which resolves exactly to
`c8a4dc6a48e407fe529c2fb5e35061064a858c5c`.

Run exactly:
- Qwen3-8B;
- Gemma-3-12B;
- Mistral-Small-24B;
- 72 frozen items;
- 12 decision conditions + 13 probes;
- 5,400 generations total.

Execution discipline:
1. run all three frozen checkpoints;
2. do not inspect, interpret, or adapt to a single-model G23A result mid-run;
3. do not replace a failed checkpoint after seeing outcomes;
4. after the complete panel finishes, run the frozen `src/analyze_g23a.py` once;
5. accept the frozen verdict logic as written.

This exception authorizes **G23A only**. It does not authorize G23B, mechanism runs,
extra checkpoints, material changes, new conditions/probes, or post-generation changes
to the estimator, exclusions, bootstrap, gates, or verdict logic.
