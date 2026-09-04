# Reproduction guide

Navigation guide for reproducing the **current paper on advance evidence exclusion**.
The repository also contains the stopped BTF-3 hindsight branch; its scripts and
results remain available but are not the default reproduction target.

## 1. Before running anything

Read:

1. [`EXPERIMENTS.md`](EXPERIMENTS.md) for the scientific role and result of each round;
2. [`PROSPECTIVE_EXCLUSION_FINDINGS.md`](PROSPECTIVE_EXCLUSION_FINDINGS.md) and
   [`stages/`](stages/) for the full result tables;
3. the exact original design in [`preregistrations/`](preregistrations/) for the round
   you intend to reproduce;
4. [`CLAUDE.md`](CLAUDE.md) for environment and GPU policy.

Do not infer a frozen design from the current paper narrative. The original
preregistration and freeze commit/tag are the authority for an experiment's exact
estimands, thresholds, sample and analysis plan.

## 2. Environment

Prefer the project's **existing local conda/virtual environment** and shared model
cache. Do not create a clean environment by default.

Much of the main line used the existing `fgvd` environment; the masked diffusion
models (LLaDA-8B, Dream-7B) used `dlm_clean`. Inspect the script and the current
environment before assuming either. A new environment is warranted only for a genuine
dependency/CUDA incompatibility.

## 3. GPU use

Check occupancy before launching. Idle cards on `fvcrc10`–`fvcrc13`, `fvcrc15`,
`fvcrc20` and `fvcrc21` may be used. During daytime, avoid occupying more than eight
GPUs total unless explicitly authorised otherwise.

## 4. Main paper evidence

Frozen items: `data/items/frozen_v1.json` (144 items, five families). Additional
frozen sets: `data/items/routing_v1.jsonl` (tagged streams),
`data/items/frozen_semaddr.json` (similarity ladder), `data/items/linear_v1.jsonl`.

### The reversal (G0)

- `PROSPECTIVE_EXCLUSION_FINDINGS.md` — full narrative and all model tables;
- `results/g0_*.json` / `results/g0_*.md`, `results/stage1_*` — per-model outputs;
- `results/cross_model_tables.md`, `results/cued_diffusion_tables.md` — panel and
  diffusion-model results;
- `results/cluster_robustness.md` — case-skeleton cluster bootstrap.

Design: `preregistrations/PREREGISTRATION_G0.md`.

### What the failure is not, and what it is

- `results/stage2_tables.md` — distance, anaphora, first weight sweep;
- `stages/STAGE3.md`, `results/stage3_tables.md`, `results/stage3_pooled.md` — the
  declarative probe, the zero discontinuity, delay, the announcement ladder, class
  policy;
- `stages/STAGE3C.md` — inclusion implicature and the arithmetic boundary condition;
- `results/paraphrase_tables.md` — eight ruling wordings;
- `results/routing_tables.md` — tagged evidence streams (`src/gen_routing.py`,
  `src/analyze_routing.py`).

### Target addressability

- `stages/STAGE3D.md`, `results/semaddr_tables.md` — similarity ladder;
- `stages/STAGE3E.md`, `results/stage7_tables.md` — duplicate control and the
  proposition relation matrix;
- `results/onpolicy_tables.md` — on-policy check of the teacher-forced result.

Condition builders: `src/conditions_v3.py` (weights, delay, ladder, class policy),
`src/conditions_v6.py` / `src/conditions_v7.py` (discovery previews and relation
matrix).

**G18 confirmatory centrepiece:**
- items: `data/items/g18_v1.jsonl`;
- design: `preregistrations/PREREGISTRATION_G18_SEMANTIC_TARGETING.md`;
- code: `src/conditions_g18.py`, `src/analyze_g18.py`;
- result: `results/g18_semantic_targeting_results.md` and
  `results/g18_semantic_targeting_analysis.json`.

### Agent

- `stages/STAGE4.md`, `results/agent_tables.md`, `results/agent_marginal.md`;
- builders in `src/conditions_agent.py`, analysis in `src/analyze_agent.py`.

### Mechanism

- `results/mech/mechanism_report.md` — span gate, attention, answer-position patching;
- `results/mech/patch_matched_report.md`, `stages/STAGE5.md` — matched-chronology
  bidirectional interchange, including the withdrawal of the earlier
  recovery-fraction analysis;
- `results/mech/direct_readout.json` — fixed-position readout validation;
- code: `src/mech/span_mask.py`, `src/mech/patch_matched.py`, `src/mech/analyze_mech.py`.

### Readout methodology

`results/metric_audit.md` and `src/metric_audit.py` — the three piloted readouts that
failed, and why single-token rating readouts can anti-correlate with the model's own
stated reasoning.

## 5. Frozen G19 method evaluation — ReGround

G16 and G17 are complete historical rounds. The only open generation round is the
explicitly authorised **G19 ReGround** method evaluation.

Read before running:
- `METHOD_REGROUND.md`;
- `preregistrations/PREREGISTRATION_G19_REGROUND.md`;
- `G19_FREEZE.md`.

Implementation:
- `src/reground.py`;
- `src/run_reground.py`;
- `src/analyze_reground.py`;
- `tests/test_reground.py`.

The freeze authority is the commit that creates `G19_FREEZE.md` over the complete
design/code tree. Do not use an earlier sequential implementation commit as the
experimental freeze.

Each model writes:
`results/raw/<tag>_reground.jsonl`.

Example runner shape:

    PYTHONPATH=src python3 src/run_reground.py \
      --model <checkpoint-path> \
      --tag qwen3-8b \
      --out results/raw/qwen3-8b_reground.jsonl

After all five frozen model tags are present:

    PYTHONPATH=src python3 src/analyze_reground.py \
      qwen3-8b gemma3-12b phi4-mini qwen3.5-27b mistral-small-24b

This writes:
- `results/reground_analysis.json`;
- `results/reground_results.md`.

The analyzer implements the preregistered raw-point gates. Do not substitute REI or a
different baseline after seeing G19 outputs.

## 6. Stopped branch (BTF-3 hindsight)

Retained for provenance; see `EXPERIMENTS.md` §C. Entry points:
`BTF3_TRANSFORMATION_CONTRACT.md`, `results/btf3_large_replication_v1_results.md`,
`results/g1[12]_*`, `results/mech/g1[345]_*`.

Two corrections apply to anything reproduced from this branch:

- `preregistrations/POSTHOC_REDACTION_AUDIT_CORRECTION.md` — the verdict redactor
  leaves 34/256 packets asserting the outcome. Re-run
  `PYTHONPATH=src python3 src/audit_redaction_leakage.py` to regenerate the audit and
  the leak-free re-estimates. **Do not repair and re-run the frozen redactor.**
- Llama boundary-probe figures must be reported at two-frame scope (73.63%), not the
  single-frame 97.66%.

The preregistered G4 breadth panel is at 5 of 17 checkpoints and **will not be
completed**.
