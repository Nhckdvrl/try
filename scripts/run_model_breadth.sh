#!/usr/bin/env bash
# G4 breadth panel: run the frozen 256-unit artifact through the unmodified
# runner on one checkpoint per GPU. Driven by data/model_panel_g4.json.
#
# Usage:
#   scripts/run_model_breadth.sh <gpu> <tag> [<gpu> <tag> ...]
# Each pair launches one checkpoint on that GPU in the background.
set -euo pipefail

cd /home/xiang/research_hun/try_clone
export PATH=/home/xiang/miniconda3/envs/fgvd/bin:$PATH
export HF_HUB_OFFLINE=1
export VLLM_LOGGING_LEVEL=WARNING
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export TOKENIZERS_PARALLELISM=false

ART=data/external/review/btf3_temporal_large_replication_v1.jsonl
PANEL=data/model_panel_g4.json
HUB=${HF_HUB:-/home/xiang/.cache/huggingface/hub}

field() { python -c "
import json,sys
panel=json.load(open('$PANEL'))
for c in panel['checkpoints']:
    if c['tag']=='$1':
        print(c['$2']); break
else:
    sys.exit(1)
"; }

model_path() {
  local mid=$1 rev=$2
  echo "$HUB/models--${mid//\//--}/snapshots/$rev"
}

run_one() {
  local gpu=$1 tag=$2
  local mid rev path extra=""
  mid=$(field "$tag" model_id)
  rev=$(field "$tag" revision)
  path=$(model_path "$mid" "$rev")
  # Node-local copies are faster than NFS when present.
  [ -d "/var/tmp/xiang-isr-models/$tag" ] && path="/var/tmp/xiang-isr-models/$tag"
  case "$tag" in
    qwen35-*|qwen38-*) extra="--enforce-eager" ;;
    mistral-*) extra="--tokenizer-mode mistral" ;;
  esac
  echo "[$tag] gpu=$gpu path=$path"
  CUDA_VISIBLE_DEVICES=$gpu python src/run_information_set.py \
    --artifact "$ART" --model "$path" --model-id "$mid" --model-revision "$rev" \
    --tag "$tag" --out "results/raw/isr_${tag}_btf3_large_replication_v1.jsonl" \
    --max-model-len 8192 --gpu-frac 0.88 --max-num-seqs 64 $extra
}

mkdir -p logs results/raw
pids=()
while [ "$#" -gt 0 ]; do
  gpu=$1; tag=$2; shift 2
  run_one "$gpu" "$tag" >"logs/isr_g4_${tag}.log" 2>&1 &
  pids+=($!)
done
status=0
for pid in "${pids[@]}"; do wait "$pid" || status=1; done
echo "breadth batch finished (status $status)"
exit $status
