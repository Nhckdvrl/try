#!/usr/bin/env bash
cd /home/xiang/research_hun/try_clone
export HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=3
K=base,admit_pre,admit_post,exclude_pre,exclude_post,exclude_pre_repeat,admit_pre_repeat,ledger,sanitation,rule_probe_exclude_pre,rule_probe_exclude_post,rule_probe_admit_post
echo "=== dream-7b (shift 1) ==="
/home/xiang/miniconda3/envs/dlm_clean/bin/python src/run_diffusion.py \
  --model Dream-org/Dream-v0-Instruct-7B --tag dream-7b --kinds $K --logits-shift 1 \
  --out results/raw/dream-7b_cued.jsonl || echo "FAILED: dream"
echo "DREAM DONE"
