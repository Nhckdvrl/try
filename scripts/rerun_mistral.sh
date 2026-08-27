#!/usr/bin/env bash
cd /home/xiang/research_hun/try_clone
until grep -q "RETRY DONE" logs/rerun_qwen35_27b.log 2>/dev/null; do sleep 30; done
export PATH=/home/xiang/miniconda3/envs/fgvd/bin:$PATH
export HF_HUB_OFFLINE=1 VLLM_LOGGING_LEVEL=WARNING CUDA_VISIBLE_DEVICES=2
PY=/home/xiang/miniconda3/envs/fgvd/bin/python
# vLLM picks the mistral-common tokenizer backend when tekken.json/params.json are
# present, and that backend has no `is_fast`. This shim dir exposes only the
# HF-format tokenizer.json, which vLLM and transformers both accept.
M=data/mistral_small_24b_hf
K=base,admit_pre,admit_post,exclude_pre,exclude_post,exclude_pre_repeat,admit_pre_repeat,exclude_post_reencode,sanitation,ledger,rule_probe_exclude_pre,rule_probe_exclude_post,rule_probe_admit_post,memory_probe_exclude_post
KC=base,admit_pre,admit_post,exclude_pre,exclude_post,exclude_pre_repeat,admit_pre_repeat,ledger,sanitation,rule_probe_exclude_pre,rule_probe_exclude_post,rule_probe_admit_post
echo "=== mistral main (retry) ==="
$PY src/run_model.py --model $M --tag mistral-small-24b --kinds $K \
  --only-ids data/items/frozen_v1.json --out results/raw/mistral-small-24b_all.jsonl \
  --max-model-len 3072 --gpu-frac 0.90 || echo "FAILED: mistral main"
echo "=== mistral cued (retry) ==="
$PY src/run_model.py --model $M --tag mistral-small-24b --mode cued --kinds $KC \
  --only-ids data/items/frozen_v1.json --out results/raw/mistral-small-24b_cued.jsonl \
  --max-model-len 3072 --gpu-frac 0.90 || echo "FAILED: mistral cued"
echo "MISTRAL DONE"
