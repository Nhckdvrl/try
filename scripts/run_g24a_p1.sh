#!/usr/bin/env bash
# Pilot P1 run — Layer-2 retraction-operator discrimination, user-ruled
# 2026-09-25 (no scientific gate, no staged stop, no selector, no probes):
#   192 items x 5 conditions x 5 panel models = 4,800 decision rows.
# Conditions: base, admit_post, exclude_post (G24A wording, untouched),
# strong_exclude_post (strong-wording control), counterfactual_delete_post.
# Model snapshots pinned exactly as run_g24a_main.sh
# (data/model_panel_g4.json).  Same runner args as G24A (mode reasoned,
# reason-tokens 110, max-model-len 4096, tp 1, gpu-frac 0.85, eager,
# decisions read by temp-0 digit expectation).
#
# GPU layout (4 GPUs, 5 models — gemma follows llama on GPU1 as in G24A):
#   GPU0 mistral-small-24b | GPU1 llama31-8b then gemma3-12b
#   GPU2 qwen3-8b          | GPU3 qwen35-9b
#
# Usage: scripts/run_g24a_p1.sh <gpu> <tag>
#   e.g. scripts/run_g24a_p1.sh 2 qwen3-8b
set -euo pipefail
cd /home/xiang/research_hun/try_clone
export PATH=/home/xiang/miniconda3/envs/fgvd/bin:$PATH
export HF_HUB_OFFLINE=1
export VLLM_LOGGING_LEVEL=WARNING
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export TOKENIZERS_PARALLELISM=false
export VLLM_USE_FLASHINFER_SAMPLER=0
PY=/home/xiang/miniconda3/envs/fgvd/bin/python
HUB=/home/xiang/.cache/huggingface/hub

GPU=${1:?usage: run_g24a_p1.sh <gpu> <tag>}
TAG=${2:?usage: run_g24a_p1.sh <gpu> <tag>}
ITEMS=${G24P1_ITEMS:-data/items/g24a_p1_v1.jsonl}
KINDS=base,admit_post,exclude_post,strong_exclude_post,counterfactual_delete_post

case "$TAG" in
  mistral-small-24b) model=data/mistral_small_24b_hf ;;
  llama31-8b)   model=$HUB/models--NousResearch--Meta-Llama-3.1-8B-Instruct/snapshots/d10aef7999a2b5ba950ab3974312feeedbfe0b77 ;;
  qwen3-8b)     model=$HUB/models--Qwen--Qwen3-8B/snapshots/b968826d9c46dd6066d109eabc6255188de91218 ;;
  qwen35-9b)    model=$HUB/models--Qwen--Qwen3.5-9B/snapshots/c202236235762e1c871ad0ccb60c8ee5ba337b9a ;;
  gemma3-12b)   model=$HUB/models--google--gemma-3-12b-it/snapshots/96b6f1eccf38110c56df3a15bffe176da04bfd80 ;;
  *) echo "unknown tag $TAG (frozen panel only)" >&2; exit 1 ;;
esac
test -d "$model" || { echo "missing model dir: $model" >&2; exit 1; }
test -f "$ITEMS" || { echo "missing item file: $ITEMS" >&2; exit 1; }

mkdir -p logs results/raw
echo "=== G24A P1 $TAG gpu$GPU $(date '+%F %T') items=$ITEMS ==="
echo "=== runner: mode reasoned, reason-tokens 110, max-model-len 4096, tp 1, temp 0 ==="
CUDA_VISIBLE_DEVICES=$GPU $PY src/run_model.py \
  --model "$model" --tag "$TAG" --kinds "$KINDS" --items "$ITEMS" \
  --out "results/raw/${TAG}_g24a_p1.jsonl" \
  --mode reasoned --reason-tokens 110 --max-model-len 4096 --tp 1 \
  --gpu-frac 0.85 --enforce-eager
echo "G24A P1 DONE: $TAG"
