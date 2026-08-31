#!/usr/bin/env bash
# One GPU lane: run a comma-separated list of breadth-panel tags sequentially.
# Usage: scripts/breadth_lane.sh <gpu> <tag1,tag2,...>
set -uo pipefail
cd /home/xiang/research_hun/try_clone
gpu=$1; IFS=',' read -ra tags <<< "$2"
for t in "${tags[@]}"; do
  out="results/raw/isr_${t}_btf3_large_replication_v1.jsonl"
  if [ -s "$out" ]; then echo "[skip] $t already has output"; continue; fi
  echo "[lane $gpu] starting $t at $(date +%H:%M:%S)"
  bash scripts/run_model_breadth.sh "$gpu" "$t" || echo "[lane $gpu] FAILED $t"
  echo "[lane $gpu] finished $t at $(date +%H:%M:%S)"
done
echo "[lane $gpu] all done"
