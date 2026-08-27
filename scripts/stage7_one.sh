#!/usr/bin/env bash
cd /home/xiang/research_hun/try_clone
GPU=$1; ENV=$2; MODEL=$3; TAG=$4; shift 4
export PATH=/home/xiang/miniconda3/envs/$ENV/bin:$PATH
export HF_HUB_OFFLINE=1 HF_HUB_DISABLE_TELEMETRY=1 TRANSFORMERS_OFFLINE=1
export VLLM_LOGGING_LEVEL=WARNING PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export CUDA_VISIBLE_DEVICES=$GPU
PY=/home/xiang/miniconda3/envs/$ENV/bin/python
echo "=== S6 $TAG on $(hostname -s) gpu $GPU env $ENV ==="
$PY src/run_model.py --model "$MODEL" --tag "$TAG" --kinds "$(cat scripts/stage7_kinds.txt)" \
  --only-ids data/items/frozen_semaddr.json --out results/raw/${TAG}_stage7.jsonl \
  --max-model-len 4096 "$@" || echo "FAILED: $TAG stage7"
echo "S6 $TAG DONE"
