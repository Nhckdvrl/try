#!/usr/bin/env bash
# G31: <gpu-index> <model-tag> [limit for smoke]
set -euo pipefail
cd /home/xiang/research_hun/try_clone
export PATH=/home/xiang/miniconda3/envs/verl-clean/bin:$PATH
export HF_HUB_OFFLINE=1
export CUDA_DEVICE_ORDER=PCI_BUS_ID
export VLLM_LOGGING_LEVEL=WARNING
export TOKENIZERS_PARALLELISM=false
export VLLM_USE_FLASHINFER_SAMPLER=0
export VLLM_WORKER_MULTIPROC_METHOD=spawn
export G31_FVCRC14_NVML_WORKAROUND=1
export PYTHONPATH=/home/xiang/research_hun/try_clone/scripts/g31_nvml_workaround:${PYTHONPATH:-}
PY=/home/xiang/miniconda3/envs/verl-clean/bin/python
HUB=/home/xiang/.cache/huggingface/hub
GPU=${1:?gpu}
TAG=${2:?tag}
LIMIT=${3:-}
TP=${4:-1}
case "$TAG" in
  mistral-small-24b) MODEL=data/mistral_small_24b_hf ;;
  qwen3-8b) MODEL=$HUB/models--Qwen--Qwen3-8B/snapshots/b968826d9c46dd6066d109eabc6255188de91218 ;;
  gemma3-12b) MODEL=$HUB/models--google--gemma-3-12b-it/snapshots/96b6f1eccf38110c56df3a15bffe176da04bfd80 ;;
  llama31-8b) MODEL=$HUB/models--NousResearch--Meta-Llama-3.1-8B-Instruct/snapshots/d10aef7999a2b5ba950ab3974312feeedbfe0b77 ;;
  *) echo "unknown model: $TAG" >&2; exit 2 ;;
esac
test -d "$MODEL"
ARGS=()
if [[ -n "$LIMIT" ]]; then ARGS=(--limit "$LIMIT"); fi
CUDA_VISIBLE_DEVICES="$GPU" "$PY" scripts/run_g31_srp_joint.py \
  --model "$MODEL" --tag "$TAG" --tp "$TP" \
  --out "results/raw/${TAG}_g31_srp_joint_v1${LIMIT:+_smoke}.jsonl" "${ARGS[@]}"
