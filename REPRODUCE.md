# Reproducing the G0 results

## Environment

Two conda envs are used, both already on this machine:

| env | transformers | used for |
|---|---|---|
| `fgvd` | 5.12 + vLLM 0.23 | every causal instruct model |
| `dlm_clean` | 4.57 | LLaDA / Dream (their remote code predates the 5.x API) |

`fgvd`'s `bin` must be **on PATH**, not just invoked by absolute path: vLLM's
flashinfer backend JIT-compiles and needs `ninja`. Run everything with
`HF_HUB_OFFLINE=1`.

```bash
export PATH=/home/xiang/miniconda3/envs/fgvd/bin:$PATH
export HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=2
```

## 1. Build and validate the dataset

```bash
python src/build_dataset.py       # 180 items -> data/items/items_v1.jsonl
python src/validate_dataset.py    # 8 structural checks, must report 0 errors
```

`validate_dataset.py` is the guarantee that the five conditions differ only in
the ways the design claims: same block multiset for pre vs post, a single
differing `RULING` block for admit vs exclude, no evidence or rule leaking into
`base`, no probe question inside a decision prompt.

## 2. Screen and freeze

Screening uses **only** `base`, `admit_pre`, `admit_post` and the admit rule
probe. The exclude conditions must not be run before the freeze.

```bash
python src/run_model.py --model Qwen/Qwen3-8B --tag qwen3-8b \
  --kinds base,admit_pre,admit_post,rule_probe_admit_post \
  --out results/raw/qwen3-8b_screen.jsonl --max-model-len 3072
python src/screen.py --runs results/raw/qwen3-8b_screen.jsonl \
  --out data/items/frozen_v1.json --report results/screen_report_qwen3-8b.json
```

`data/items/frozen_v1.json` in this repo is the frozen set (144 items) used for
everything reported.

## 3. Run the models

```bash
bash scripts/run_families.sh          # all causal instruct models, all conditions
bash scripts/run_cued_and_diffusion.sh # fixed-position readout
bash scripts/run_diffusion.sh          # LLaDA / Dream (needs dlm_clean)
```

Per-model quirks, all handled by flags in `src/run_model.py`:

* **Qwen3.5-27B** is a hybrid Mamba model — needs `--max-num-seqs 128
  --enforce-eager`, and `--gpu-frac` at most ~0.80.
* **Mistral-Small-24B** — run `scripts/make_mistral_shim.sh` first and point
  `--model` at `data/mistral_small_24b_hf`.
* **Dream** — `--logits-shift 1 --n-mask 8`. **LLaDA** — defaults (`0`, `1`).

## 4. Analyse

```bash
python src/analyze.py --runs results/raw/qwen3-8b_main.jsonl \
  --tag qwen3-8b --out-prefix results/g0_qwen3-8b
python src/summarize_all.py        # -> results/cross_model_tables.md
python src/summarize_cued.py       # -> results/cued_diffusion_tables.md
python src/cluster_robustness.py   # -> results/cluster_robustness.md
```

## 5. Mechanism (Qwen3-8B)

```bash
python src/mech/validate_direct_readout.py     # is the fixed-position readout valid?
python src/mech/experiments.py                 # attention / patching / span gate
python src/mech/analyze_mech.py
python src/mech/repeat_check.py
```

## Note on run-to-run variation

The readout is deterministic, but the greedy rationale in front of it is not:
vLLM batching is not bitwise deterministic, so at a near-tie the rationale can
take a different path. A full replicate of Qwen3-8B (`qwen3-8b-rep2`) gives
item-level r = 0.87–0.97 and aggregate estimates within 0.06 REI. Expect small
differences, not different conclusions.
