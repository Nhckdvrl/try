# Project status — 2026-09-23, G23A COMPLETE / G23B DESIGN FROZEN / PHASE A AUTHORIZED

> **NO APPROVED PAPER MAINLINE.**
>
> **G23A v3 COMPLETE:** `zero-amplified`, `Δ_zero = +8.83 [+4.39,+13.33]`.
>
> **ACTIVE NEXT STEP:** G23B Phase A carrier run (B / P / E / PE) under frozen tag
> `g23b-gate-vs-cancellation-design-v1`.
>
> **G23B PHASE A COMPUTE AUTHORIZED — PHASE B (U/K/I) NOT AUTHORIZED UNTIL THE
> PHASE-A CARRIER GATE PASSES.**

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
| Unring the Bell / G23B | **DESIGN FROZEN — PHASE A AUTHORIZED / PHASE B HELD** |
| active candidate | **G23B Phase A carrier audit** |
| approved mainline | **NONE** |

The clean-slate policy remains the default. G23A is a single explicit exception after
the legacy Unring line was re-audited, the old paper stories were archived, and a
decisive fresh pilot was frozen. This is **not** an approved paper mainline.

TCR is now killed because too much source auditing/database reconstruction and cross-linguistic inference are required before the scientific estimand is even secured.

HOM is now killed because the current question remains a competence check of an established semantic distinction despite excellent data.

---

## Compute boundary

G23A v3 target-model compute is complete and its outputs are committed.

G23B design work completed and frozen 2026-09-23: materials, conditions, analyzer,
tests, prereg amendments settling the three audit flags, and tag
`g23b-gate-vs-cancellation-design-v1` on commit `e7701a9`. Governing file:
`preregistrations/PREREGISTRATION_G23B_GATE_VS_CANCELLATION.md`.

Authorized now:
- **G23B Phase A target-model generation only**: cells `g23b_b`, `g23b_p`,
  `g23b_e`, `g23b_pe` × the 60 frozen items × the three G23A checkpoints;
- one run of the frozen Phase-A analyzer (`src/analyze_g23b.py --phase a`) on
  those committed outputs, and reporting of the four carrier gates;
- dummy / synthetic code tests that do not query target models.

Not authorized now:
- any G23B Phase B generation (cells `g23b_u`, `g23b_k`, `g23b_i`);
- any U/K/I exclusion-rule output;
- G23B mechanism runs;
- extra robustness checkpoints;
- modifications to G23A's frozen results.

Hard stop: if the Phase-A carrier gate fails, G23B stops before any U/K/I rule
output is generated (prereg §6). Phase B requires a further explicit update to
this file after a passing Phase-A report.

The six design-freeze preconditions from the previous revision of this section are
all met as of 2026-09-23: (1) fresh materials exist; (2) the Phase-A carrier
qualification logic is frozen; (3) the U/K/I estimands and branch classifier are
implemented; (4) tests pass; (5) a dedicated G23B design tag is created; (6) this
repository-level authority update. **This update authorizes Phase A only.**
