# Project status — 2026-09-24, G23C + G24A + G24B COMPLETE / THREE-RQ PAPER EXPANSION ACTIVE

> **NO APPROVED PAPER MAINLINE.**
>
> **G23A v3 COMPLETE:** `zero-amplified`, `Δ_zero = +8.83 [+4.39,+13.33]`.
>
> **G23B v1 STOPPED AT THE FROZEN PHASE-A CARRIER GATE:** `carrier-invalid`.
>
> **G23C v1 COMPLETE:** frozen verdict `target-conditioned-policy-state`,
> L14 `TargetConditioning = +8.15 [+6.91,+9.44]`.
>
> **G24A v1 COMPLETE (2026-09-24):** frozen verdict `prospective-only` —
> pooled-4 `REI_pre = +0.541 [+0.477,+0.603]` (P1 PASS) vs
> `REI_post = −0.067 [−0.158,+0.021]` (P2 FAIL); sufficiency gate 595/600;
> integrity ledger 5/5 models × 600 items complete. Report:
> `results/g24a/g24a_analysis_v1.{md,json}`. Licensed §8 wording applies
> verbatim; no other claim language is authorized from this round.
>
> **G24B v1 COMPLETE (2026-09-24):** frozen verdict
> `donor-conditioned-policy-state` — L14 primary
> `DonorTargetInteraction = +4.02 [+2.27,+6.14]` (floor 3.0, positive in
> 2/2 models: qwen3-8b +3.17, mistral-small-24b +4.88);
> `DonorPolicy_M = +10.81 [+8.31,+13.41]`, `DonorPolicy_U = +6.79
> [+5.22,+8.78]` both pass; controls L4 `dti = −0.15` / L24 `dti = +0.07`
> both absent → clause OK; identity `max |Δ| = 0.0000` over 1,800 checks;
> bridge PASS with the §12 cross-check against frozen G23C gates; 75/75
> items × 2 models complete, zero drops. Report:
> `results/mech/g24b_analysis.json`. Licensed §8 wording applies verbatim;
> no other claim language is authorized from this round.
>
> **ACTIVE:** paper-scale three-RQ expansion under
> `PAPER_SCALE_AUDIT_2026-09-23.md`.
>
> **G24A AUTHORIZED EXPERIMENT (record — EXECUTED AND COMPLETE):** source-grounded
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
> Executed exactly once per this authority: selection pass
> `results/raw/g24a_mistral-small-24b_selection.jsonl` (39,849 rows,
> Base/Admit-only) → selected 600/600
> `data/items/g24a_v1.jsonl` sha256 `b0d02f7a…`, report
> `data/items/g24a_selection_report_v1.{md,json}` (shortfall0; a selector
> early-stop bug was found by structural audit and fixed back to prereg §5.4
> before selection — see commit `b3fe84d`) → main pass5 ×4,800 rows =
> 24,000/24,000 → verdict above.
>
> **G24B AUTHORIZED EXPERIMENT (record — EXECUTED AND COMPLETE):** donor-state vs
> recipient-context factorization — prereg
> `preregistrations/PREREGISTRATION_G24B_DONOR_RECIPIENT_FACTORIZATION.md`,
> tag `g24b-donor-recipient-factorization-design-v1` (commit `a1c787f`,
> tagged before any G24B forward pass). Compute authorized = prereg §4/§6/§9
> layout only: bridge phase (the four Stage-5 cells, direct readout, no hooks,
> the two frozen models × 75 items) → gate read with the §12 boolean-triple
> cross-check against frozen `results/mech/g23c_bridge_analysis.json` (abort on
> mismatch) → only if the bridge passes, patch phase (four baselines with
> rule-end state capture + 8 donor×recipient grid patches × layers (4,14,24) +
> four-cell identity patches, the same two models × 75 items) →
> `src/mech/analyze_g24b.py --phase bridge|full`. Nothing else. Scientific gap:
> G23C's within-preview interchange cannot separate state-side target
> conditioning from matched-recipient sensitivity; this round fixes the
> recipient prompt and varies only the donor state.
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

G23A v3, G23B v1, G23C v1, G24A v1 and G24B v1 are closed rounds.

The earlier statement “G23C-R then write” is superseded by
`PAPER_SCALE_AUDIT_2026-09-23.md`.

Current paper target:

- **RQ1 / generality:** G0 breadth + controls + agent setting + a new source-grounded
  natural-evidence confirmation;
- **RQ2 / structural boundary:** G23A zero amplification + explicit/verifiable
  prospective-zero controls + policy-access/enforcement dissociation;
- **RQ3 / mechanism:** Stage 5 + G23C + donor-vs-recipient causal factorization +
  fresh-material replication.

Authorized now: nothing — no target-model compute. The G24B round is
complete (verdict above); the next authorization must name a single frozen
experiment and its exact scientific gap (candidates: G23C-R, per
`PAPER_SCALE_AUDIT_2026-09-23.md`).

Still design only:
- G23C-R design/finalization (fresh-material replication);
- paper writing work under `PAPER_SCALE_AUDIT_2026-09-23.md`.

Not authorized:
- any further G24B compute (closed round);
- G23C-R forward passes;
- new layer/site/model searches;
- any new carrier rescue;
- arbitrary “extra ablations” not tied to RQ1/RQ2/RQ3.

Next compute authorization must name a single frozen experiment and its exact scientific
gap.
