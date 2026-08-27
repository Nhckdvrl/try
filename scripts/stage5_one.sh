#!/usr/bin/env bash
cd /home/xiang/research_hun/try_clone
GPU=$1; ENV=$2; MODEL=$3; TAG=$4; shift 4
export PATH=/home/xiang/miniconda3/envs/$ENV/bin:$PATH
export HF_HUB_OFFLINE=1 VLLM_LOGGING_LEVEL=WARNING PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export CUDA_VISIBLE_DEVICES=$GPU
PY=/home/xiang/miniconda3/envs/$ENV/bin/python
echo "=== S5 $TAG on $(hostname -s) gpu $GPU env $ENV ==="
$PY src/run_model.py --model "$MODEL" --tag "$TAG" --kinds "$(cat scripts/stage5_kinds.txt)" \
  --only-ids data/items/frozen_v1.json --out results/raw/${TAG}_stage5.jsonl \
  --max-model-len 4096 "$@" || echo "FAILED: $TAG stage5"
echo "=== LINEAR $TAG ==="
$PY src/run_model.py --model "$MODEL" --tag "$TAG" --kinds "$(cat scripts/linear_kinds.txt)" \
  --items data/items/linear_v1.jsonl --out results/raw/${TAG}_linear.jsonl \
  --max-model-len 3072 "$@" || echo "FAILED: $TAG linear"
echo "S5 $TAG DONE"
