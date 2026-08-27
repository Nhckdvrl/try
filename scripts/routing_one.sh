#!/usr/bin/env bash
cd /home/xiang/research_hun/try_clone
GPU=$1; ENV=$2; MODEL=$3; TAG=$4; shift 4
export PATH=/home/xiang/miniconda3/envs/$ENV/bin:$PATH
export HF_HUB_OFFLINE=1 VLLM_LOGGING_LEVEL=WARNING PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export CUDA_VISIBLE_DEVICES=$GPU
echo "=== ROUTE $TAG on $(hostname -s) gpu $GPU env $ENV ==="
/home/xiang/miniconda3/envs/$ENV/bin/python src/run_model.py --model "$MODEL" --tag "$TAG" \
  --kinds rt_oracle,rt_naive,rt_pre,rt_post,rule_probe_exclude_pre,rule_probe_exclude_post \
  --items data/items/routing_v1.jsonl --out results/raw/${TAG}_routing.jsonl \
  --max-model-len 4096 "$@" || echo "FAILED: $TAG"
echo "ROUTE $TAG DONE"
