#!/usr/bin/env bash
cd /home/xiang/research_hun/try_clone
export HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=3
K=base,admit_pre,admit_post,exclude_pre,exclude_post,exclude_pre_repeat,admit_pre_repeat,ledger,sanitation,rule_probe_exclude_pre,rule_probe_exclude_post,rule_probe_admit_post
PY=/home/xiang/miniconda3/envs/dlm_clean/bin/python
echo "=== dream-7b (shift 1, block of 8 masks) ==="
$PY src/run_diffusion.py --model Dream-org/Dream-v0-Instruct-7B --tag dream-7b --kinds $K \
  --logits-shift 1 --n-mask 8 --out results/raw/dream-7b_cued.jsonl || echo "FAILED: dream"
echo "=== llada-8b (re-verify with new indexing) ==="
$PY src/run_diffusion.py --model GSAI-ML/LLaDA-8B-Instruct --tag llada-8b --kinds $K \
  --logits-shift 0 --n-mask 1 --out results/raw/llada-8b_cued.jsonl || echo "FAILED: llada"
echo "DREAM2 DONE"
