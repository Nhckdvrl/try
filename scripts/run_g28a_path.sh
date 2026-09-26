#!/usr/bin/env bash
# Registered G28A full run. Usage: scripts/run_g28a_path.sh <gpu-index> <model-tag>
set -euo pipefail
cd /home/xiang/research_hun/try_clone
export PATH=/home/xiang/miniconda3/envs/verl-clean/bin:$PATH
export HF_HUB_OFFLINE=1
export VLLM_LOGGING_LEVEL=WARNING
export TOKENIZERS_PARALLELISM=false
export VLLM_USE_FLASHINFER_SAMPLER=0
PY=/home/xiang/miniconda3/envs/verl-clean/bin/python
HUB=/home/xiang/.cache/huggingface/hub
GPU=${1:?usage: run_g28a_path.sh <gpu-index> <model-tag>}
TAG=${2:?usage: run_g28a_path.sh <gpu-index> <model-tag>}
case "$TAG" in
  mistral-small-24b) MODEL=data/mistral_small_24b_hf ;;
  qwen3-8b) MODEL=$HUB/models--Qwen--Qwen3-8B/snapshots/b968826d9c46dd6066d109eabc6255188de91218 ;;
  llama31-8b) MODEL=$HUB/models--NousResearch--Meta-Llama-3.1-8B-Instruct/snapshots/d10aef7999a2b5ba950ab3974312feeedbfe0b77 ;;
  gemma3-12b) MODEL=$HUB/models--google--gemma-3-12b-it/snapshots/96b6f1eccf38110c56df3a15bffe176da04bfd80 ;;
  qwen35-9b) MODEL=$HUB/models--Qwen--Qwen3.5-9B/snapshots/c202236235762e1c871ad0ccb60c8ee5ba337b9a ;;
  *) echo "Unknown tag: $TAG" >&2; exit 2 ;;
esac
test -d "$MODEL"
mkdir -p logs results/raw
echo "G28A $TAG on GPU $GPU; environment verl-clean; $(date -Iseconds)"
CUDA_VISIBLE_DEVICES="$GPU" "$PY" scripts/run_g28a_path.py \
  --model "$MODEL" --tag "$TAG" \
  --out "results/raw/${TAG}_g28a_path_v1.jsonl"
