#!/usr/bin/env bash
# Fixed-position ("cued") readout: the only readout a masked diffusion LM and a
# causal LM can both be given at the identical position.
cd /home/xiang/research_hun/try_clone
until grep -q "ALL DONE" logs/run_families.log; do sleep 30; done
export PATH=/home/xiang/miniconda3/envs/fgvd/bin:$PATH
export HF_HUB_OFFLINE=1 VLLM_LOGGING_LEVEL=WARNING CUDA_VISIBLE_DEVICES=2
PY=/home/xiang/miniconda3/envs/fgvd/bin/python
K=base,admit_pre,admit_post,exclude_pre,exclude_post,exclude_pre_repeat,admit_pre_repeat,ledger,sanitation,rule_probe_exclude_pre,rule_probe_exclude_post,rule_probe_admit_post

# --- causal baselines under the same fixed-position readout ---
for M in "Qwen/Qwen3-8B qwen3-8b" "google/gemma-3-12b-it gemma3-12b" \
         "microsoft/Phi-4-mini-instruct phi4-mini" "Qwen/Qwen2.5-7B-Instruct qwen2.5-7b" \
         "/home/xiang/.cache/huggingface/hub/models--mistralai--Mistral-Small-24B-Instruct-2501/snapshots/9527884be6e5616bdd54de542f9ae13384489724/ mistral-small-24b"; do
  set -- $M
  echo "=== CUED $2 ==="
  $PY src/run_model.py --model "$1" --tag "$2" --mode cued --kinds $K \
      --only-ids data/items/frozen_v1.json --out results/raw/$2_cued.jsonl \
      --max-model-len 3072 --gpu-frac 0.85 || echo "FAILED: cued $2"
done

# --- masked diffusion LMs ---
echo "=== DIFF llada-8b ==="
$PY src/run_diffusion.py --model GSAI-ML/LLaDA-8B-Instruct --tag llada-8b --kinds $K \
    --out results/raw/llada-8b_cued.jsonl || echo "FAILED: llada"
echo "=== DIFF dream-7b ==="
$PY src/run_diffusion.py --model Dream-org/Dream-v0-Instruct-7B --tag dream-7b --kinds $K \
    --out results/raw/dream-7b_cued.jsonl || echo "FAILED: dream"
echo "CUED DONE"
