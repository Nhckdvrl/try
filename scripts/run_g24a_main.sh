#!/usr/bin/env bash
# G24A main pass — compute authorized by STATUS commit efd303b (§11.6).
# One frozen panel model on its pinned snapshot revision, 8 kinds (5
# conditions + 3 rule probes) on the selected <=600-item file
# data/items/g24a_v1.jsonl. GPU layout per prereg §11:
#   GPU0 mistral-small-24b | GPU1 llama31-8b then gemma3-12b
#   GPU2 qwen3-8b          | GPU3 qwen35-9b
#
# Usage: scripts/run_g24a_main.sh <gpu> <tag>
#   e.g. scripts/run_g24a_main.sh 2 qwen3-8b
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

GPU=${1:?usage: run_g24a_main.sh <gpu> <tag>}
TAG=${2:?usage: run_g24a_main.sh <gpu> <tag>}
ITEMS=${G24A_ITEMS:-data/items/g24a_v1.jsonl}
KINDS=base,admit_pre,admit_post,exclude_pre,exclude_post,rule_probe_exclude_pre,rule_probe_exclude_post,rule_probe_admit_post

# Pinned snapshot revisions from data/model_panel_g4.json (prereg §4).
case "$TAG" in
  mistral-small-24b) model=data/mistral_small_24b_hf ;;
  llama31-8b)   model=$HUB/models--NousResearch--Meta-Llama-3.1-8B-Instruct/snapshots/d10aef7999a2b5ba950ab3974312feeedbfe0b77 ;;
  qwen3-8b)     model=$HUB/models--Qwen--Qwen3-8B/snapshots/b968826d9c46dd6066d109eabc6255188de91218 ;;
  qwen35-9b)    model=$HUB/models--Qwen--Qwen3.5-9B/snapshots/c202236235762e1c871ad0ccb60c8ee5ba337b9a ;;
  gemma3-12b)   model=$HUB/models--google--gemma-3-12b-it/snapshots/96b6f1eccf38110c56df3a15bffe176da04bfd80 ;;
  *) echo "unknown tag $TAG (frozen panel only)" >&2; exit 1 ;;
esac
test -d "$model" || { echo "missing model dir: $model" >&2; exit 1; }
test -f "$ITEMS" || { echo "missing selected items: $ITEMS" >&2; exit 1; }

mkdir -p logs results/raw
echo "=== G24A main $TAG gpu$GPU $(date '+%F %T') items=$ITEMS tag=g24a-natural-evidence-confirmation-design-v1 ==="
echo "=== runner (prereg §4): mode reasoned, reason-tokens 110, max-model-len 4096, tp 1, temp 0 ==="
CUDA_VISIBLE_DEVICES=$GPU $PY src/run_model.py \
  --model "$model" --tag "$TAG" --kinds "$KINDS" --items "$ITEMS" \
  --out "results/raw/${TAG}_g24a.jsonl" \
  --mode reasoned --reason-tokens 110 --max-model-len 4096 --tp 1 \
  --gpu-frac 0.85 --enforce-eager
echo "G24A MAIN DONE: $TAG"
