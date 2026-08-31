#!/usr/bin/env bash
# G6 layer-window masking sweep. One checkpoint per GPU.
# Usage: scripts/run_span_sweep.sh [--limit N] <gpu> <tag> [<gpu> <tag> ...]
set -uo pipefail
cd /home/xiang/research_hun/try_clone
export PATH=/home/xiang/miniconda3/envs/fgvd/bin:$PATH
export HF_HUB_OFFLINE=1 PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export TOKENIZERS_PARALLELISM=false
HUB=${HF_HUB:-/home/xiang/.cache/huggingface/hub}

LIMIT=0
SUFFIX=""
if [ "${1:-}" = "--limit" ]; then LIMIT=$2; SUFFIX="_n$2"; shift 2; fi

meta() { python -c "
import json
for c in json.load(open('data/model_panel_g4.json'))['checkpoints']:
    if c['tag']=='$1': print(c['$2']); break
"; }

run_model() {
  local gpu=$1 tag=$2 mid rev path
  mid=$(meta "$tag" model_id); rev=$(meta "$tag" revision)
  path="$HUB/models--${mid//\//--}/snapshots/$rev"
  [ -d "/var/tmp/xiang-isr-models/$tag" ] && path="/var/tmp/xiang-isr-models/$tag"
  out="results/raw/mech_${tag}_g6_span_sweep${SUFFIX}.jsonl"
  [ -s "$out" ] && { echo "[skip] $out"; return; }
  echo "[$tag] sweep on gpu $gpu, limit=$LIMIT, $(date +%H:%M:%S)"
  CUDA_VISIBLE_DEVICES=$gpu python src/mech/run_span_sweep.py \
    --model "$path" --model-id "$mid" --model-revision "$rev" --tag "$tag" \
    --out "$out" --limit "$LIMIT" --attn sdpa
}

mkdir -p logs results/raw
pids=()
while [ "$#" -gt 0 ]; do
  gpu=$1; tag=$2; shift 2
  run_model "$gpu" "$tag" >"logs/mech_g6_${tag}${SUFFIX}.log" 2>&1 &
  pids+=($!)
done
status=0
for pid in "${pids[@]}"; do wait "$pid" || status=1; done
echo "G6 sweep batch finished (status $status)"
exit $status
