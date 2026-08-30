#!/usr/bin/env bash
set -euo pipefail

cd /home/xiang/research_hun/try_clone
export PATH=/home/xiang/miniconda3/envs/fgvd/bin:$PATH
export HF_HUB_OFFLINE=1
export VLLM_LOGGING_LEVEL=WARNING
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

ARTIFACT=data/external/review/btf3_temporal_confirmatory_v1.jsonl
QWEN_MODEL_PATH=${ISR_QWEN_MODEL_PATH:-/var/tmp/xiang-isr-models/qwen35-9b}
GEMMA_MODEL_PATH=${ISR_GEMMA_MODEL_PATH:-/var/tmp/xiang-isr-models/gemma3-12b}
MISTRAL_MODEL_PATH=${ISR_MISTRAL_MODEL_PATH:-/var/tmp/xiang-isr-models/mistral-small-24b}

# Only m1_before and m2v2 are new data collection under v2. REPEAT-AFTER
# reuses v1's already-collected m1 results unchanged (see
# PREREGISTRATION_G1_FACTORIZATION_V2.md); m3 is deferred entirely.

run_model() {
  local manipulation=$1
  local gpu=$2
  local model_path=$3
  local model_id=$4
  local revision=$5
  local tag=$6
  local extra=${7:-}
  export CUDA_VISIBLE_DEVICES=$gpu
  python src/run_factorization.py \
    --artifact "$ARTIFACT" --manipulation "$manipulation" \
    --baseline "results/raw/isr_${tag}_btf3_confirmatory_v1.jsonl" \
    --model "$model_path" --model-id "$model_id" \
    --model-revision "$revision" --tag "$tag" \
    --out "results/raw/isr_${tag}_factorization_${manipulation}.jsonl" \
    --max-model-len 8192 --gpu-frac 0.85 --max-num-seqs 64 $extra
}

mkdir -p logs results/raw
for manipulation in m1_before m2v2; do
  run_model "$manipulation" 0 \
    "$QWEN_MODEL_PATH" \
    Qwen/Qwen3.5-9B c202236235762e1c871ad0ccb60c8ee5ba337b9a qwen35-9b \
    --enforce-eager >"logs/isr_factorization_${manipulation}_qwen35-9b.log" 2>&1 &
  pid_qwen=$!
  run_model "$manipulation" 1 \
    "$GEMMA_MODEL_PATH" \
    google/gemma-3-12b-it 96b6f1eccf38110c56df3a15bffe176da04bfd80 gemma3-12b \
    "" >"logs/isr_factorization_${manipulation}_gemma3-12b.log" 2>&1 &
  pid_gemma=$!
  run_model "$manipulation" 2 \
    "$MISTRAL_MODEL_PATH" \
    mistralai/Mistral-Small-24B-Instruct-2501 9527884be6e5616bdd54de542f9ae13384489724 mistral-small-24b \
    "--tokenizer-mode mistral" >"logs/isr_factorization_${manipulation}_mistral-small-24b.log" 2>&1 &
  pid_mistral=$!

  wait "$pid_qwen"
  wait "$pid_gemma"
  wait "$pid_mistral"
  echo "manipulation $manipulation: all three models finished"
done

echo "all v2 factorization runs finished"
