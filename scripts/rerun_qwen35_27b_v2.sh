#!/usr/bin/env bash
cd /home/xiang/research_hun/try_clone
until grep -q "MISTRAL DONE" logs/rerun_mistral.log 2>/dev/null; do sleep 30; done
export PATH=/home/xiang/miniconda3/envs/fgvd/bin:$PATH
export HF_HUB_OFFLINE=1 VLLM_LOGGING_LEVEL=WARNING CUDA_VISIBLE_DEVICES=2
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
K=base,admit_pre,admit_post,exclude_pre,exclude_post,exclude_pre_repeat,admit_pre_repeat,exclude_post_reencode,sanitation,ledger,rule_probe_exclude_pre,rule_probe_exclude_post,rule_probe_admit_post,memory_probe_exclude_post
echo "=== qwen3.5-27b (retry 2: eager, frac 0.80, seqs 128) ==="
/home/xiang/miniconda3/envs/fgvd/bin/python src/run_model.py --model Qwen/Qwen3.5-27B \
  --tag qwen3.5-27b --kinds $K --only-ids data/items/frozen_v1.json \
  --out results/raw/qwen3.5-27b_all.jsonl --max-model-len 3072 --gpu-frac 0.80 \
  --max-num-seqs 128 --enforce-eager || echo "FAILED: qwen3.5-27b retry2"
echo "RETRY2 DONE"
