#!/usr/bin/env bash
# usage: stage4_one.sh <gpu> <env> <model> <tag> [vllm flags...]
# env: fgvd on the Blackwell box (driver 580 / cu13), verl-clean on the A100 nodes
# (driver 550 / cu12.4 -- fgvd's torch 2.11+cu130 will not start there).
cd /home/xiang/research_hun/try_clone
GPU=$1; ENV=$2; MODEL=$3; TAG=$4; shift 4
export PATH=/home/xiang/miniconda3/envs/$ENV/bin:$PATH
export HF_HUB_OFFLINE=1 VLLM_LOGGING_LEVEL=WARNING PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export CUDA_VISIBLE_DEVICES=$GPU
echo "=== stage4 $TAG on $(hostname -s) gpu $GPU env $ENV ==="
/home/xiang/miniconda3/envs/$ENV/bin/python src/run_model.py --model "$MODEL" --tag "$TAG" \
  --kinds "$(cat scripts/stage4_kinds.txt)" --only-ids data/items/frozen_v1.json \
  --out results/raw/${TAG}_stage4.jsonl --max-model-len 4096 "$@" || echo "FAILED: $TAG"
echo "stage4 $TAG DONE"
