#!/usr/bin/env bash
set -euo pipefail

cd /home/xiang/research_hun/try_clone
export PATH=/home/xiang/miniconda3/envs/fgvd/bin:$PATH
export HF_HUB_OFFLINE=1
export VLLM_LOGGING_LEVEL=WARNING
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

FOMC=data/external/review/fomc_temporal_pilot_v1.jsonl
QWEN_MODEL_PATH=${ISR_QWEN_MODEL_PATH:-/var/tmp/xiang-isr-models/qwen35-9b}
GEMMA_MODEL_PATH=${ISR_GEMMA_MODEL_PATH:-/var/tmp/xiang-isr-models/gemma3-12b}
MISTRAL_MODEL_PATH=${ISR_MISTRAL_MODEL_PATH:-/var/tmp/xiang-isr-models/mistral-small-24b}

run_model() {
  local gpu=$1
  local model_path=$2
  local model_id=$3
  local revision=$4
  local tag=$5
  local extra=${6:-}
  export CUDA_VISIBLE_DEVICES=$gpu
  python src/run_information_set.py \
    --artifact "$FOMC" --model "$model_path" --model-id "$model_id" \
    --model-revision "$revision" --tag "$tag" \
    --out "results/raw/isr_${tag}_fomc_pilot_v1.jsonl" \
    --max-model-len 8192 --gpu-frac 0.85 --max-num-seqs 64 $extra
}

mkdir -p logs results/raw
run_model 0 \
  "$QWEN_MODEL_PATH" \
  Qwen/Qwen3.5-9B c202236235762e1c871ad0ccb60c8ee5ba337b9a qwen35-9b \
  --enforce-eager >logs/isr_fomc_pilot_qwen35-9b.log 2>&1 &
pid_qwen=$!
run_model 1 \
  "$GEMMA_MODEL_PATH" \
  google/gemma-3-12b-it 96b6f1eccf38110c56df3a15bffe176da04bfd80 gemma3-12b \
  "" >logs/isr_fomc_pilot_gemma3-12b.log 2>&1 &
pid_gemma=$!
run_model 2 \
  "$MISTRAL_MODEL_PATH" \
  mistralai/Mistral-Small-24B-Instruct-2501 9527884be6e5616bdd54de542f9ae13384489724 mistral-small-24b \
  "--tokenizer-mode mistral" >logs/isr_fomc_pilot_mistral-small-24b.log 2>&1 &
pid_mistral=$!

wait "$pid_qwen"
wait "$pid_gemma"
wait "$pid_mistral"

echo "all three FOMC pilot runs finished"
