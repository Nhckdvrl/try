#!/usr/bin/env bash
# Sequential queue for GPUs 0-2 on this node. Each stage waits for the previous
# one's outputs, so nothing contends and a stalled stage does not silently skip
# the rest. GPU 3 runs the breadth lane independently.
set -uo pipefail
cd /home/xiang/research_hun/try_clone
export PATH=/home/xiang/miniconda3/envs/fgvd/bin:$PATH

wait_gone() { while pgrep -f "$1" >/dev/null; do sleep 60; done; }

echo "[queue] waiting for G5 deliberation to finish  $(date +%H:%M:%S)"
wait_gone "src/run_deliberation.py"

echo "[queue] G8 packet swap  $(date +%H:%M:%S)"
bash scripts/run_packet_swap.sh 0 qwen35-9b 1 gemma3-12b 2 mistral-small-24b
python src/analyze_packet_swap.py > results/g8_packet_swap_console.txt 2>&1 || echo "[queue] G8 analysis failed"

echo "[queue] G9 numeric track  $(date +%H:%M:%S)"
bash scripts/run_btf3_numeric.sh 0 qwen35-9b 1 gemma3-12b 2 mistral-small-24b
python src/analyze_btf3_large_replication.py \
  results/raw/isr_qwen35-9b_btf3_numeric_v1.jsonl \
  results/raw/isr_gemma3-12b_btf3_numeric_v1.jsonl \
  results/raw/isr_mistral-small-24b_btf3_numeric_v1.jsonl \
  --expected-artifact-sha256 cb0c925ade9b76eee71f9a6f9dc695da44fb717510e15a5156e6416967ef6b15 \
  --out results/g9_numeric_analysis.json > results/g9_numeric_console.txt 2>&1 \
  || echo "[queue] G9 analysis failed"
python src/analyze_exante_anchor.py \
  --source data/external/raw/btf3/btf3_numeric_questions_and_forecasts.parquet \
  --out results/g9_numeric_anchor_analysis.json > results/g9_numeric_anchor_console.txt 2>&1 \
  || echo "[queue] G9 anchor analysis skipped (expected: needs the numeric-track loader)"

echo "[queue] G6 validation sweep, 4 units  $(date +%H:%M:%S)"
bash scripts/run_span_sweep.sh --limit 4 0 qwen35-9b

echo "[queue] done  $(date +%H:%M:%S)"
