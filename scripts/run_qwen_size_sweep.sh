#!/usr/bin/env bash
# Qwen3.5 within-family size sweep on the frozen 256-unit artifact.
# Same runner, prompts, decoding, parser, and thresholds as the large
# replication round; only the checkpoint changes. 9B is NOT re-run -- its
# existing large-replication output is reused.
set -euo pipefail

cd /home/xiang/research_hun/try_clone
export PATH=/home/xiang/miniconda3/envs/fgvd/bin:$PATH
export HF_HUB_OFFLINE=1
export VLLM_LOGGING_LEVEL=WARNING
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

ART=data/external/review/btf3_temporal_large_replication_v1.jsonl
DEST=${ISR_MODEL_DIR:-/var/tmp/xiang-isr-models}

run_size() {
  local gpu=$1 tag=$2 model_id=$3 revision=$4
  local path="$DEST/$tag"
  if [ ! -d "$path" ]; then
    echo "SKIP $tag: checkpoint not staged at $path" >&2
    return 0
  fi
  export CUDA_VISIBLE_DEVICES=$gpu
  python src/run_information_set.py \
    --artifact "$ART" --model "$path" --model-id "$model_id" \
    --model-revision "$revision" --tag "$tag" \
    --out "results/raw/isr_${tag}_btf3_large_replication_v1.jsonl" \
    --max-model-len 8192 --gpu-frac 0.85 --max-num-seqs 64 --enforce-eager \
    >"logs/isr_sweep_${tag}.log" 2>&1
}

mkdir -p logs results/raw
run_size 0 qwen35-2b  Qwen/Qwen3.5-2B  "${ISR_QWEN35_2B_REVISION:-UNPINNED}" &
pid_2b=$!
run_size 1 qwen35-4b  Qwen/Qwen3.5-4B  "${ISR_QWEN35_4B_REVISION:-851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a}" &
pid_4b=$!
wait "$pid_2b"; wait "$pid_4b"

# 27B alone afterwards so it can take the largest GPU without contention.
run_size 2 qwen35-27b Qwen/Qwen3.5-27B "${ISR_QWEN35_27B_REVISION:-fc05daec18b0a78c049392ed2e771dde82bdf654}"
echo "size sweep finished"
