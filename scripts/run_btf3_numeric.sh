#!/usr/bin/env bash
# G9 numeric track: the unmodified runner on the frozen 128-unit numeric artifact.
# Usage: scripts/run_btf3_numeric.sh <gpu> <tag> [<gpu> <tag> ...]
set -uo pipefail
cd /home/xiang/research_hun/try_clone
export PATH=/home/xiang/miniconda3/envs/fgvd/bin:$PATH
export HF_HUB_OFFLINE=1 VLLM_LOGGING_LEVEL=WARNING PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
ART=data/external/review/btf3_numeric_v1.jsonl
HUB=${HF_HUB:-/home/xiang/.cache/huggingface/hub}
meta() { python -c "
import json
for c in json.load(open('data/model_panel_g4.json'))['checkpoints']:
    if c['tag']=='$1': print(c['$2']); break
"; }
run_model() {
  local gpu=$1 tag=$2 mid rev path extra=""
  mid=$(meta "$tag" model_id); rev=$(meta "$tag" revision)
  path="$HUB/models--${mid//\//--}/snapshots/$rev"
  [ -d "/var/tmp/xiang-isr-models/$tag" ] && path="/var/tmp/xiang-isr-models/$tag"
  case "$tag" in qwen35-*|qwen38-*) extra="--enforce-eager" ;; mistral-*) extra="--tokenizer-mode mistral" ;; esac
  out="results/raw/isr_${tag}_btf3_numeric_v1.jsonl"
  [ -s "$out" ] && { echo "[skip] $out"; return; }
  CUDA_VISIBLE_DEVICES=$gpu python src/run_information_set.py \
    --artifact "$ART" --model "$path" --model-id "$mid" --model-revision "$rev" --tag "$tag" \
    --out "$out" --max-model-len 8192 --gpu-frac 0.85 --max-num-seqs 64 $extra
}
mkdir -p logs results/raw
pids=()
while [ "$#" -gt 0 ]; do
  gpu=$1; tag=$2; shift 2
  run_model "$gpu" "$tag" >"logs/isr_g9_${tag}.log" 2>&1 &
  pids+=($!)
done
for pid in "${pids[@]}"; do wait "$pid"; done
echo "G9 numeric batch finished"
