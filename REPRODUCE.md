# Reproduction guide

This file is a navigation guide for reproducing the **current hindsight paper**. The repository also contains the older controlled *Unring the Bell* program; those scripts/results remain available but are not the default reproduction target.

## 1. Before running anything

Read:

1. [`EXPERIMENTS.md`](EXPERIMENTS.md) for the scientific role and result of each round;
2. the exact original design in [`preregistrations/`](preregistrations/) for the round you intend to reproduce;
3. [`BTF3_TRANSFORMATION_CONTRACT.md`](BTF3_TRANSFORMATION_CONTRACT.md) for the natural forecasting transformation;
4. [`CLAUDE.md`](CLAUDE.md) for environment and GPU policy.

Do not infer a frozen design from the current paper narrative. The original preregistration and freeze commit/tag are the authority for an experiment's exact estimands, thresholds, sample, and analysis plan.

## 2. Environment

Prefer the project's **existing local conda/virtual environment** and shared model cache. Do not create a clean environment by default.

Historically, much of the project used the existing `fgvd` environment; older diffusion-model experiments also used `dlm_clean`. Before reproducing a current BTF-3 or mechanism round, inspect the script and current environment rather than assuming that an old G0 environment recipe is still the right entry point.

A new environment is warranted only for a genuine dependency/CUDA incompatibility.

## 3. GPU use

Check GPU occupancy before launching. Idle cards on `fvcrc10`, `fvcrc11`, `fvcrc12`, `fvcrc13`, `fvcrc15`, `fvcrc20`, and `fvcrc21` may be used. During daytime, avoid occupying more than eight GPUs total unless explicitly authorized otherwise.

## 4. Main paper evidence

### Hindsight phenomenon

Key outputs:

- `results/btf3_confirmatory_v1_results.md` — 64-item prospective confirmation;
- `results/btf3_large_replication_v1_results.md` — 256-item fresh large replication;
- `results/btf3_cross_round_replication.json` — cross-round comparison;
- `results/btf3_factuality_audit_v1_results.md` — source-packet audit.

Exact design documents are in `preregistrations/PREREGISTRATION_BTF3_LARGE_REPLICATION.md` and the relevant earlier BTF/G1 preregistrations.

### Directional outcome pull

Key outputs:

- `results/g8_packet_swap_analysis.json` — foreign resolved-event intervention;
- `results/g11_redacted_swap_results.md` / `results/g11_redacted_swap_analysis.json` — verdict-redacted foreign packets;
- `results/g12_donor_outcome_results.md` / `results/g12_donor_outcome_analysis.json` — paired outcome-direction intervention.

Exact designs:

- `preregistrations/PREREGISTRATION_G8_RELEVANCE.md`;
- `preregistrations/PREREGISTRATION_G11_REDACTED_SWAP.md`;
- `preregistrations/PREREGISTRATION_G12_DONOR_OUTCOME.md`.

### Mechanism

Key outputs:

- `results/mech/g13_shared_outcome_results.md` and analysis JSON;
- `results/mech/g14_decision_outcome_results.md` and analysis JSON;
- `results/mech/g15_decision_confirmation_results.md` and analysis JSON.

Exact designs:

- `preregistrations/PREREGISTRATION_G13_SHARED_OUTCOME.md`;
- `preregistrations/PREREGISTRATION_G14_DECISION_STATE.md`;
- `preregistrations/PREREGISTRATION_G15_DECISION_CONFIRMATION.md`.

G14 is discovery for the recipient-conditioned answer-state formulation; G15 is the fresh prospective confirmation. Preserve that chronology when reproducing or extending the mechanism work.

## 5. Supporting and historical experiments

Supporting current-paper characterization (verdict redaction, size sweep, G3, G4) is indexed in `EXPERIMENTS.md` and has exact preregistrations under `preregistrations/`.

The original G0 / controlled prospective-nullification experiments are historical. Their detailed narrative is archived in `archive/UNRING_THE_BELL_FINDINGS.md`; old G0 raw/model-analysis outputs remain under `results/`. Use them when studying the research history, not as the default starting point for the current paper.

## 6. Reproduction principle

Reproduce a round from its **frozen contract + preregistration + committed sample + analysis script**, not from a prose summary. If a historical environment no longer runs, first try to repair compatibility in the existing project environment; only then create a minimal new environment and record the reason.
