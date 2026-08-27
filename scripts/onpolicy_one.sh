#!/usr/bin/env bash
cd /home/xiang/research_hun/try_clone
GPU=$1; ENV=$2; MODEL=$3; TAG=$4; shift 4
export PATH=/home/xiang/miniconda3/envs/$ENV/bin:$PATH
export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 VLLM_LOGGING_LEVEL=WARNING
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True CUDA_VISIBLE_DEVICES=$GPU
PY=/home/xiang/miniconda3/envs/$ENV/bin/python
echo "=== OP $TAG on $(hostname -s) gpu $GPU ==="
$PY src/run_model.py --model "$MODEL" --tag "$TAG" \
  --kinds base,inc_none_full,op_pre,op_post --only-ids data/items/frozen_v1.json \
  --out results/raw/${TAG}_onpolicy.jsonl --max-model-len 4096 --samples 16 \
  --temperature 0.8 "$@" || echo "FAILED: $TAG onpolicy"
echo "OP $TAG DONE"
