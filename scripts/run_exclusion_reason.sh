#!/usr/bin/env bash
# G3 exclusion-reason: six new conditions x three frozen checkpoints on the
# 256-unit large-replication artifact. The `temporal` arm is NOT run — its
# prompts are byte-identical to that round's out-of-set prompts (verified by
# scripts/audit_exclusion_reason.py) and are read from its output.
set -euo pipefail

cd /home/xiang/research_hun/try_clone
export PATH=/home/xiang/miniconda3/envs/fgvd/bin:$PATH
export HF_HUB_OFFLINE=1
export VLLM_LOGGING_LEVEL=WARNING
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

ART=data/external/review/btf3_temporal_large_replication_v1.jsonl
QWEN_MODEL_PATH=${ISR_QWEN_MODEL_PATH:-/var/tmp/xiang-isr-models/qwen35-9b}
GEMMA_MODEL_PATH=${ISR_GEMMA_MODEL_PATH:-/var/tmp/xiang-isr-models/gemma3-12b}
MISTRAL_MODEL_PATH=${ISR_MISTRAL_MODEL_PATH:-/var/tmp/xiang-isr-models/mistral-small-24b}
CONDITIONS=${ISR_G3_CONDITIONS:-"reason_bare_with reason_bare_without reason_unreliable_with reason_unreliable_without reason_procedural_with reason_procedural_without"}

run_model() {
  local gpu=$1 model_path=$2 model_id=$3 revision=$4 tag=$5 extra=${6:-}
  export CUDA_VISIBLE_DEVICES=$gpu
  for condition in $CONDITIONS; do
    echo "[$tag] $condition"
    python src/run_exclusion_reason.py \
      --artifact "$ART" --condition "$condition" \
      --model "$model_path" --model-id "$model_id" --model-revision "$revision" --tag "$tag" \
      --out "results/raw/isr_${tag}_g3_${condition}.jsonl" \
      --max-model-len 8192 --gpu-frac 0.85 --max-num-seqs 64 $extra
  done
}

mkdir -p logs results/raw
run_model 0 "$QWEN_MODEL_PATH" Qwen/Qwen3.5-9B c202236235762e1c871ad0ccb60c8ee5ba337b9a qwen35-9b \
  --enforce-eager >logs/isr_g3_qwen35-9b.log 2>&1 &
pid_qwen=$!
run_model 1 "$GEMMA_MODEL_PATH" google/gemma-3-12b-it 96b6f1eccf38110c56df3a15bffe176da04bfd80 gemma3-12b \
  "" >logs/isr_g3_gemma3-12b.log 2>&1 &
pid_gemma=$!
run_model 2 "$MISTRAL_MODEL_PATH" mistralai/Mistral-Small-24B-Instruct-2501 9527884be6e5616bdd54de542f9ae13384489724 mistral-small-24b \
  "--tokenizer-mode mistral" >logs/isr_g3_mistral-small-24b.log 2>&1 &
pid_mistral=$!

wait "$pid_qwen"; wait "$pid_gemma"; wait "$pid_mistral"
echo "all G3 exclusion-reason conditions finished"
