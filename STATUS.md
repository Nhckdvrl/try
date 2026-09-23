# Project status — 2026-09-23, G23A COMPLETE / G23B STOPPED / G23C FROZEN — COMPUTE AUTHORIZED

> **NO APPROVED PAPER MAINLINE.**
>
> **G23A v3 COMPLETE:** `zero-amplified`, `Δ_zero = +8.83 [+4.39,+13.33]`.
>
> **G23B v1 STOPPED AT THE FROZEN PHASE-A CARRIER GATE:** `carrier-invalid`.
>
> **ACTIVE NEXT STEP:** G23C target-conditioned policy-state interchange — design
> frozen and tagged `g23c-target-conditioned-policy-state-design-v1`.
>
> **G23C COMPUTE AUTHORIZED — this is the explicit STATUS update of prereg §11.6:**
> bridge phase first, both models, 75 frozen items; policy-state interchange only
> if the §4 bridge gate passes. If it fails, the round stops at `bridge-failed`.

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
| Unring the Bell / G23C | **FROZEN / AUTHORIZED — §4 stop rule** |
| active candidate | **G23C target-conditioned policy-state interchange** |
| approved mainline | **NONE** |

The clean-slate policy remains the default. G23A is a single explicit exception after
the legacy Unring line was re-audited, the old paper stories were archived, and a
decisive fresh pilot was frozen. This is **not** an approved paper mainline.

TCR is now killed because too much source auditing/database reconstruction and cross-linguistic inference are required before the scientific estimand is even secured.

HOM is now killed because the current question remains a competence check of an established semantic distinction despite excellent data.

---

## Compute boundary

G23A v3 is complete and remains the last successful frozen behavioral result.

G23B v1 Phase A is complete. Frozen carrier result:

- pooled `ProfferLeak = +8.07 [+4.86,+11.23]`;
- model means `+6.36 / +8.34 / +9.50`;
- gate 1 = FAIL;
- gate 2 = FAIL;
- gate 3 = PASS;
- gate 4 = PASS;
- frozen verdict: **carrier-invalid**.

Therefore the preregistered hard stop is in force.

Not authorized:
- G23B Phase B `U/K/I`;
- reworded / replacement proffer carrier under the same preregistration;
- a G23B-v2 carrier search;
- mechanism runs framed as if G23B had selected cancellation or standing-gate;
- extra model or prompt robustness runs.

The next registered design is G23C:
`preregistrations/PREREGISTRATION_G23C_TARGET_CONDITIONED_POLICY_STATE.md`.

G23C is a new mechanistic question, not a G23B carrier rescue. It asks whether the
existing Stage-5 rule-time state carries the 0-vs-100 policy value in a
target-conditioned form.

Authorized now:
- design/prereg refinement;
- exact Stage-5 cell reconstruction;
- implementation and synthetic tests;
- prompt/token/site audit without model forward passes;
- G23C bridge phase — `g23c_policy_state.py --phase bridge` on Qwen3-8B and
  Mistral-Small-24B, all 75 frozen items, then `analyze_g23c.py --phase bridge`;
- G23C policy-state interchange — `--phase patch` on both models, **only after**
  the §4 bridge gate passes on both, then `analyze_g23c.py --phase full`.

Not authorized:
- any G23C interchange run if the bridge gate fails (stop at `bridge-failed`);
- layer search, or patching any layer outside the frozen (4, 14, 24);
- any patch site other than `rule_end`;
- new behavioral generation;
- carrier redesign — G23B stays closed;
- re-interpretation or re-run after a stop-rule verdict without a new design.
