#!/usr/bin/env bash
cd /home/xiang/research_hun/try_clone
until grep -q "RETRY2 DONE" logs/rerun_qwen35_27b_v2.log 2>/dev/null; do sleep 30; done
export PATH=/home/xiang/miniconda3/envs/fgvd/bin:$PATH
export HF_HUB_OFFLINE=1 VLLM_LOGGING_LEVEL=WARNING CUDA_VISIBLE_DEVICES=2
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
PY=/home/xiang/miniconda3/envs/fgvd/bin/python
M=data/mistral_small_24b_hf
K=base,admit_pre,admit_post,exclude_pre,exclude_post,exclude_pre_repeat,admit_pre_repeat,exclude_post_reencode,sanitation,ledger,rule_probe_exclude_pre,rule_probe_exclude_post,rule_probe_admit_post,memory_probe_exclude_post
KC=base,admit_pre,admit_post,exclude_pre,exclude_post,exclude_pre_repeat,admit_pre_repeat,ledger,sanitation,rule_probe_exclude_pre,rule_probe_exclude_post,rule_probe_admit_post
echo "=== mistral main (retry 2, frac 0.78) ==="
$PY src/run_model.py --model $M --tag mistral-small-24b --kinds $K \
  --only-ids data/items/frozen_v1.json --out results/raw/mistral-small-24b_all.jsonl \
  --max-model-len 3072 --gpu-frac 0.78 --max-num-seqs 128 || echo "FAILED: mistral main v2"
echo "=== mistral cued (retry 2, frac 0.78) ==="
$PY src/run_model.py --model $M --tag mistral-small-24b --mode cued --kinds $KC \
  --only-ids data/items/frozen_v1.json --out results/raw/mistral-small-24b_cued.jsonl \
  --max-model-len 3072 --gpu-frac 0.78 --max-num-seqs 128 || echo "FAILED: mistral cued v2"
echo "MISTRAL2 DONE"
