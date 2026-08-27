#!/usr/bin/env bash
# All conditions + probes for every locally available instruct family.
export PATH=/home/xiang/miniconda3/envs/fgvd/bin:$PATH
export HF_HUB_OFFLINE=1 VLLM_LOGGING_LEVEL=WARNING CUDA_VISIBLE_DEVICES=2
PY=/home/xiang/miniconda3/envs/fgvd/bin/python
K=base,admit_pre,admit_post,exclude_pre,exclude_post,exclude_pre_repeat,admit_pre_repeat,exclude_post_reencode,sanitation,ledger,rule_probe_exclude_pre,rule_probe_exclude_post,rule_probe_admit_post,memory_probe_exclude_post

run () {  # $1=model path/id  $2=tag  $3=gpu_frac
  echo "=== $2 ==="
  $PY src/run_model.py --model "$1" --tag "$2" --kinds $K \
      --only-ids data/items/frozen_v1.json --out results/raw/$2_all.jsonl \
      --max-model-len 3072 --gpu-frac "${3:-0.88}" || echo "FAILED: $2"
}

# reproducibility replicate of the reference model (identical command, fresh process)
run Qwen/Qwen3-8B qwen3-8b-rep2 0.85

run google/gemma-3-4b-it            gemma3-4b    0.85
run microsoft/Phi-4-mini-instruct   phi4-mini    0.85
run Qwen/Qwen2.5-7B-Instruct        qwen2.5-7b   0.85
run google/gemma-3-12b-it           gemma3-12b   0.88
run Qwen/Qwen3.5-9B                 qwen3.5-9b   0.88
run Qwen/Qwen2.5-32B-Instruct       qwen2.5-32b  0.90
run Qwen/Qwen3.5-27B                qwen3.5-27b  0.90
run "/home/xiang/.cache/huggingface/hub/models--mistralai--Mistral-Small-24B-Instruct-2501/snapshots/9527884be6e5616bdd54de542f9ae13384489724/"                           mistral-small-24b 0.90
echo "ALL DONE"
