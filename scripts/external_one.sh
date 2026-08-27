#!/usr/bin/env bash
cd /home/xiang/research_hun/try_clone
GPU=$1; ENV=$2; MODEL=$3; TAG=$4; shift 4
export PATH=/home/xiang/miniconda3/envs/$ENV/bin:$PATH
export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 VLLM_LOGGING_LEVEL=WARNING
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True CUDA_VISIBLE_DEVICES=$GPU
PY=/home/xiang/miniconda3/envs/$ENV/bin/python
echo "=== EXT $TAG on $(hostname -s) gpu $GPU ==="
$PY src/run_model.py --model "$MODEL" --tag "$TAG" \
  --kinds ext_base,ext_admit,ext_pre,ext_post,rule_probe_exclude_post \
  --items data/items/external_ramsey.jsonl --out results/raw/${TAG}_extramsey.jsonl \
  --max-model-len 3072 "$@" || echo "FAILED: $TAG ramsey"
$PY src/run_model.py --model "$MODEL" --tag "$TAG" \
  --kinds base,admit_pre,admit_post,exclude_pre,exclude_post,rule_probe_exclude_pre,rule_probe_exclude_post \
  --items data/items/external_bh.jsonl --out results/raw/${TAG}_extbh.jsonl \
  --max-model-len 3072 "$@" || echo "FAILED: $TAG bh"
echo "EXT $TAG DONE"
