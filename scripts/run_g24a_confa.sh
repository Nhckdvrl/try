#!/usr/bin/env bash
# G24A Confirmation A run — RQ1/F1 replication, registration §13.2 (frozen,
# user 2026-09-26):
#   500 fresh FEVER/SciFact items x 5 cells x 6 models = 15,000 decision rows.
# Cells: base, admit_pre, admit_post, exclude_pre, exclude_post (G24A
# standard five; items render through the unmodified G24A module).
#
# ONE invocation per model (run_model --out opens "w"): 500 ids x 5 kinds
# = 2,500 rows/model.
#
# Model snapshots pinned exactly as run_g24a_p2.sh (data/model_panel_g4.json)
# PLUS the frozen Qwen3-32B addition of §13.4 (revision
# 9216db5781bf21249d130ec9da846c4624c16137).  Same runner args as P2-P4
# (mode reasoned, reason-tokens 110, max-model-len 4096, tp 1, gpu-frac
# 0.85, eager, temp-0 digit expectation) — §13.4 froze them for 32B too.
#
# GPU layout (4 GPUs, 6 models): the five frozen-panel tags follow P2-P4's
# layout; Qwen3-32B is its OWN segment (one A100, tp 1, gpu-frac 0.85) —
# launch it alone on a free GPU (e.g. GPU0 after mistral finishes), never
# co-resident with another vLLM instance:
#   GPU0 mistral-small-24b | GPU1 llama31-8b then gemma3-12b
#   GPU2 qwen3-8b          | GPU3 qwen35-9b
#   qwen3-32b: own GPU segment (own segment per §13.4)
#
# Usage: scripts/run_g24a_confa.sh <gpu> <tag>
#   e.g. scripts/run_g24a_confa.sh 2 qwen3-8b
# Smoke (4 ids, suffixed outputs, does NOT touch full raws):
#   G24A_CONFA_SMOKE=1 scripts/run_g24a_confa.sh <gpu> <tag>
set -euo pipefail
cd /home/xiang/research_hun/try_clone
export PATH=/home/xiang/miniconda3/envs/fgvd/bin:$PATH
export HF_HUB_OFFLINE=1
export VLLM_LOGGING_LEVEL=WARNING
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export TOKENIZERS_PARALLELISM=false
export VLLM_USE_FLASHINFER_SAMPLER=0
PY=/home/xiang/miniconda3/envs/fgvd/bin/python
HUB=/home/xiang/.cache/huggingface/hub

GPU=${1:?usage: run_g24a_confa.sh <gpu> <tag>}
TAG=${2:?usage: run_g24a_confa.sh <gpu> <tag>}
ITEMS=${G24A_CONFA_ITEMS:-data/items/g24a_confa_v1.jsonl}
IDS=${G24A_CONFA_IDS:-data/items/g24a_confa_ids.json}
SUF=${G24A_CONFA_SUF:-}
# kind list mirrors scripts/verify_g24a_confa_prompts.py (KINDS); the
# verifier parses this line — keep the two files in sync.
KINDS=base,admit_pre,admit_post,exclude_pre,exclude_post

case "$TAG" in
  mistral-small-24b) model=data/mistral_small_24b_hf ;;
  llama31-8b)   model=$HUB/models--NousResearch--Meta-Llama-3.1-8B-Instruct/snapshots/d10aef7999a2b5ba950ab3974312feeedbfe0b77 ;;
  qwen3-8b)     model=$HUB/models--Qwen--Qwen3-8B/snapshots/b968826d9c46dd6066d109eabc6255188de91218 ;;
  qwen35-9b)    model=$HUB/models--Qwen--Qwen3.5-9B/snapshots/c202236235762e1c871ad0ccb60c8ee5ba337b9a ;;
  gemma3-12b)   model=$HUB/models--google--gemma-3-12b-it/snapshots/96b6f1eccf38110c56df3a15bffe176da04bfd80 ;;
  qwen3-32b)    model=$HUB/models--Qwen--Qwen3-32B/snapshots/9216db5781bf21249d130ec9da846c4624c16137 ;;
  *) echo "unknown tag $TAG (frozen panel only)" >&2; exit 1 ;;
esac
test -d "$model" || { echo "missing model dir: $model" >&2; exit 1; }
test -f "$ITEMS" || { echo "missing item file: $ITEMS" >&2; exit 1; }
test -f "$IDS" || { echo "missing id list: $IDS" >&2; exit 1; }

if [ "${G24A_CONFA_SMOKE:-0}" = "1" ]; then
  SUF=${G24A_CONFA_SUF:-_smoke}
  $PY - <<'PYEOF'
import json, pathlib
ids = json.load(open("data/items/g24a_confa_ids.json"))
p = pathlib.Path("logs/g24a_confa_smoke_ids.json")
p.parent.mkdir(exist_ok=True)
p.write_text(json.dumps(ids[:4]) + "\n")
PYEOF
  IDS=logs/g24a_confa_smoke_ids.json
  echo "=== SMOKE: 4 ids, outputs carry suffix '$SUF' ==="
fi

mkdir -p logs results/raw
echo "=== G24A ConfA $TAG gpu$GPU $(date '+%F %T') items=$ITEMS ids=$IDS ==="
echo "=== runner: mode reasoned, reason-tokens 110, max-model-len 4096, tp 1, temp 0 ==="
CUDA_VISIBLE_DEVICES=$GPU $PY src/run_model.py \
  --model "$model" --tag "$TAG" --kinds "$KINDS" --items "$ITEMS" \
  --only-ids "$IDS" \
  --out "results/raw/${TAG}_g24a_confa${SUF}.jsonl" \
  --mode reasoned --reason-tokens 110 --max-model-len 4096 --tp 1 \
  --gpu-frac 0.85 --enforce-eager
echo "G24A ConfA DONE: $TAG (2500 rows)"
