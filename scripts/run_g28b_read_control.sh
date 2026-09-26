#!/usr/bin/env bash
set -euo pipefail
cd /home/xiang/research_hun/try_clone
export PATH=/home/xiang/miniconda3/envs/verl-clean/bin:$PATH
export HF_HUB_OFFLINE=1 VLLM_LOGGING_LEVEL=WARNING TOKENIZERS_PARALLELISM=false VLLM_USE_FLASHINFER_SAMPLER=0
PY=/home/xiang/miniconda3/envs/verl-clean/bin/python
HUB=/home/xiang/.cache/huggingface/hub
GPU=${1:?GPU required}
TAG=${2:?model tag required}
case "$TAG" in
  mistral-small-24b) MODEL=data/mistral_small_24b_hf ;;
  qwen3-8b) MODEL=$HUB/models--Qwen--Qwen3-8B/snapshots/b968826d9c46dd6066d109eabc6255188de91218 ;;
  gemma3-12b) MODEL=$HUB/models--google--gemma-3-12b-it/snapshots/96b6f1eccf38110c56df3a15bffe176da04bfd80 ;;
  llama31-8b) MODEL=$HUB/models--NousResearch--Meta-Llama-3.1-8B-Instruct/snapshots/d10aef7999a2b5ba950ab3974312feeedbfe0b77 ;;
  *) echo "Unknown tag: $TAG" >&2; exit 2 ;;
esac
test -d "$MODEL"
mkdir -p logs results/raw
echo "G28B $TAG on GPU $GPU; environment verl-clean; $(date -Iseconds)"
CUDA_VISIBLE_DEVICES="$GPU" "$PY" scripts/run_g28b_read_control.py \
  --model "$MODEL" --tag "$TAG" \
  --out "results/raw/${TAG}_g28b_read_control_v1.jsonl"
