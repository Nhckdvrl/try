#!/usr/bin/env bash
# Sequential lane for the large breadth checkpoints, one at a time, eager only.
# The earlier failure on fvcrc20 was four concurrent 30-70GB loads plus vLLM's
# post-load compile/profiling on a node already at load 22-25 from other users:
# weights finished loading, then the engines sat at 0% GPU for an hour. One at a
# time with --enforce-eager skips the stage that stalled.
set -uo pipefail
cd /home/xiang/research_hun/try_clone
export PATH=/home/xiang/miniconda3/envs/fgvd/bin:$PATH
export HF_HUB_OFFLINE=1 VLLM_LOGGING_LEVEL=WARNING PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export TOKENIZERS_PARALLELISM=false
ART=data/external/review/btf3_temporal_large_replication_v1.jsonl
HUB=${HF_HUB:-/home/xiang/.cache/huggingface/hub}
GPU=${1:-0}; shift
meta() { python -c "
import json
for c in json.load(open('data/model_panel_g4.json'))['checkpoints']:
    if c['tag']=='$1': print(c['$2']); break
"; }
for tag in "$@"; do
  out="results/raw/isr_${tag}_btf3_large_replication_v1.jsonl"
  [ -s "$out" ] && { echo "[skip] $tag"; continue; }
  mid=$(meta "$tag" model_id); rev=$(meta "$tag" revision)
  path="$HUB/models--${mid//\//--}/snapshots/$rev"
  [ -d "/var/tmp/xiang-isr-models/$tag" ] && path="/var/tmp/xiang-isr-models/$tag"
  echo "[big] $tag start $(date +%H:%M:%S)"
  CUDA_VISIBLE_DEVICES=$GPU timeout 7200 python src/run_information_set.py \
    --artifact "$ART" --model "$path" --model-id "$mid" --model-revision "$rev" \
    --tag "$tag" --out "$out" --max-model-len 8192 --gpu-frac 0.90 \
    --max-num-seqs 32 --enforce-eager >"logs/isr_g4big_${tag}.log" 2>&1 \
    && echo "[big] $tag done $(date +%H:%M:%S)" \
    || echo "[big] $tag FAILED/timeout $(date +%H:%M:%S)"
done
echo "[big] lane finished"
