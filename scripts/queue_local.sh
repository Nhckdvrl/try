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

echo "[queue] G10 few-shot  $(date +%H:%M:%S)"
bash scripts/run_fewshot.sh 0 qwen35-9b 1 gemma3-12b 2 mistral-small-24b
python src/analyze_fewshot.py > results/g10_fewshot_console.txt 2>&1 || echo "[queue] G10 analysis failed"

echo "[queue] G5 state-arm full-text pass (qualitative only)  $(date +%H:%M:%S)"
for pair in "0 qwen35-9b --enforce-eager" "1 gemma3-12b " "2 mistral-small-24b --tokenizer-mode|mistral"; do
  set -- $pair; gpu=$1; tag=$2; shift 2; extra=$(echo "${*:-}" | tr '|' ' ')
  out="results/raw/isr_${tag}_g5full_delib_state_oob_with.jsonl"
  [ -s "$out" ] && continue
  path="/var/tmp/xiang-isr-models/$tag"
  mid=$(python -c "
import json
for c in json.load(open('data/model_panel_g4.json'))['checkpoints']:
    if c['tag']=='$tag': print(c['model_id']); break")
  rev=$(python -c "
import json
for c in json.load(open('data/model_panel_g4.json'))['checkpoints']:
    if c['tag']=='$tag': print(c['revision']); break")
  CUDA_VISIBLE_DEVICES=$gpu python src/run_deliberation.py --condition delib_state_oob_with \
    --model "$path" --model-id "$mid" --model-revision "$rev" --tag "$tag" \
    --out "$out" --max-model-len 8192 --max-tokens 640 --gpu-frac 0.85 --max-num-seqs 64 \
    --keep-full-raw $extra > "logs/isr_g5full_${tag}.log" 2>&1 &
done
wait

echo "[queue] G6 validation sweep, 4 units  $(date +%H:%M:%S)"
bash scripts/run_span_sweep.sh --limit 4 0 qwen35-9b

echo "[queue] done  $(date +%H:%M:%S)"
