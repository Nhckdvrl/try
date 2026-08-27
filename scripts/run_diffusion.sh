#!/usr/bin/env bash
# LLaDA / Dream need transformers 4.57 (their remote code predates the 5.x
# `all_tied_weights_keys` API), so they run in the dlm_clean env on a second GPU.
cd /home/xiang/research_hun/try_clone
export HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=3
PY=/home/xiang/miniconda3/envs/dlm_clean/bin/python
K=base,admit_pre,admit_post,exclude_pre,exclude_post,exclude_pre_repeat,admit_pre_repeat,ledger,sanitation,rule_probe_exclude_pre,rule_probe_exclude_post,rule_probe_admit_post
echo "=== llada-8b ==="
$PY src/run_diffusion.py --model GSAI-ML/LLaDA-8B-Instruct --tag llada-8b --kinds $K \
    --out results/raw/llada-8b_cued.jsonl || echo "FAILED: llada"
echo "=== dream-7b ==="
$PY src/run_diffusion.py --model Dream-org/Dream-v0-Instruct-7B --tag dream-7b --kinds $K \
    --out results/raw/dream-7b_cued.jsonl || echo "FAILED: dream"
echo "DIFFUSION DONE"
