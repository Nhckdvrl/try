#!/usr/bin/env bash
# G24A selection pass — compute authorized by STATUS commit efd303b (§11.6,
# immediately after tag g24a-natural-evidence-confirmation-design-v1).
#
# Base/Admit kinds ONLY on the full frozen candidate pool (13,283 items) with
# the frozen selection model. No Exclude/probe row may appear in this output;
# src/select_g24a.py aborts if one does (prereg §5, §9.2).
#
# Usage: scripts/run_g24a_selection.sh [gpu]     (default gpu 0)
set -euo pipefail
cd /home/xiang/research_hun/try_clone
export PATH=/home/xiang/miniconda3/envs/fgvd/bin:$PATH
export HF_HUB_OFFLINE=1
export VLLM_LOGGING_LEVEL=WARNING
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export TOKENIZERS_PARALLELISM=false
# G23A precedent: same runner, same env on this cluster
export VLLM_USE_FLASHINFER_SAMPLER=0
PY=/home/xiang/miniconda3/envs/fgvd/bin/python
GPU=${1:-0}

mkdir -p logs results/raw
echo "=== G24A selection pass mistral-small-24b gpu$GPU $(date '+%F %T') tag=g24a-natural-evidence-confirmation-design-v1 ==="
echo "=== runner (prereg §4): mode reasoned, reason-tokens 110, max-model-len 4096, tp 1, temp 0 ==="
CUDA_VISIBLE_DEVICES=$GPU $PY src/run_model.py \
  --model data/mistral_small_24b_hf \
  --tag mistral-small-24b \
  --kinds base,admit_pre,admit_post \
  --items data/items/g24a_candidates_v1.jsonl \
  --out results/raw/g24a_mistral-small-24b_selection.jsonl \
  --mode reasoned --reason-tokens 110 --max-model-len 4096 --tp 1 \
  --gpu-frac 0.85 --enforce-eager
echo "G24A SELECTION DONE"
