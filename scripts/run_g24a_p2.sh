#!/usr/bin/env bash
# Pilot P2 run — same-claim counterfactual reconstruction, user-ruled
# 2026-09-25 (prereg §9; no scientific gate, no staged stop, no selector,
# no probes):
#   200 claims x 9 cells x 5 panel models = 9,000 decision rows.
# Cells: base (claim only, evidence-free) + {admit_post, exclude_post,
# strong_exclude_post, counterfactual_delete_post} x {arm+, arm-}.
#
# TWO invocations per model (run_model --out opens "w", so separate files):
#   arm+ : 200 ids x 5 kinds (incl. base)  -> 1,000 rows
#   arm- : 200 ids x 4 kinds (no base)     ->   800 rows
# base is never issued on arm-: its prompt is byte-identical across arms
# (verified by verify_g24a_p2_prompts.py), so Y0 is shared by construction
# and re-running it would only duplicate rows.  -> exactly 9 rows/claim.
#
# Model snapshots pinned exactly as run_g24a_main.sh (data/model_panel_g4.json).
# Same runner args as G24A/P1 (mode reasoned, reason-tokens 110,
# max-model-len 4096, tp 1, gpu-frac 0.85, eager, temp-0 digit expectation).
#
# GPU layout (4 GPUs, 5 models — gemma follows llama on GPU1 as in G24A/P1):
#   GPU0 mistral-small-24b | GPU1 llama31-8b then gemma3-12b
#   GPU2 qwen3-8b          | GPU3 qwen35-9b
#
# Usage: scripts/run_g24a_p2.sh <gpu> <tag>
#   e.g. scripts/run_g24a_p2.sh 2 qwen3-8b
# Smoke (4 ids/arm, suffixed outputs, does NOT touch full raws):
#   G24P2_SMOKE=1 scripts/run_g24a_p2.sh <gpu> <tag>
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

GPU=${1:?usage: run_g24a_p2.sh <gpu> <tag>}
TAG=${2:?usage: run_g24a_p2.sh <gpu> <tag>}
ITEMS=${G24P2_ITEMS:-data/items/g24a_p2_v1.jsonl}
IDS_PLUS=${G24P2_IDS_PLUS:-data/items/g24a_p2_ids_plus.json}
IDS_MINUS=${G24P2_IDS_MINUS:-data/items/g24a_p2_ids_minus.json}
SUF=${G24P2_SUF:-}
# kind lists mirror scripts/verify_g24a_p2_prompts.py (KINDS_PLUS /
# KINDS_MINUS); the verifier asserts KINDS_MINUS == KINDS_PLUS[1:] and that
# base never appears in KINDS_MINUS — keep the two files in sync.
KINDS_PLUS=base,admit_post,exclude_post,strong_exclude_post,counterfactual_delete_post
KINDS_MINUS=admit_post,exclude_post,strong_exclude_post,counterfactual_delete_post

case "$TAG" in
  mistral-small-24b) model=data/mistral_small_24b_hf ;;
  llama31-8b)   model=$HUB/models--NousResearch--Meta-Llama-3.1-8B-Instruct/snapshots/d10aef7999a2b5ba950ab3974312feeedbfe0b77 ;;
  qwen3-8b)     model=$HUB/models--Qwen--Qwen3-8B/snapshots/b968826d9c46dd6066d109eabc6255188de91218 ;;
  qwen35-9b)    model=$HUB/models--Qwen--Qwen3.5-9B/snapshots/c202236235762e1c871ad0ccb60c8ee5ba337b9a ;;
  gemma3-12b)   model=$HUB/models--google--gemma-3-12b-it/snapshots/96b6f1eccf38110c56df3a15bffe176da04bfd80 ;;
  *) echo "unknown tag $TAG (frozen panel only)" >&2; exit 1 ;;
esac
test -d "$model" || { echo "missing model dir: $model" >&2; exit 1; }
test -f "$ITEMS" || { echo "missing item file: $ITEMS" >&2; exit 1; }
test -f "$IDS_PLUS" || { echo "missing id list: $IDS_PLUS" >&2; exit 1; }
test -f "$IDS_MINUS" || { echo "missing id list: $IDS_MINUS" >&2; exit 1; }

if [ "${G24P2_SMOKE:-0}" = "1" ]; then
  SUF=${G24P2_SUF:-_smoke}
  $PY - <<'PYEOF'
import json, pathlib
for arm in ("plus", "minus"):
    ids = json.load(open(f"data/items/g24a_p2_ids_{arm}.json"))
    p = pathlib.Path(f"logs/g24a_p2_smoke_ids_{arm}.json")
    p.parent.mkdir(exist_ok=True)
    p.write_text(json.dumps(ids[:4]) + "\n")
PYEOF
  IDS_PLUS=logs/g24a_p2_smoke_ids_plus.json
  IDS_MINUS=logs/g24a_p2_smoke_ids_minus.json
  echo "=== SMOKE: 4 ids/arm, outputs carry suffix '$SUF' ==="
fi

mkdir -p logs results/raw
echo "=== G24A P2 arm+ $TAG gpu$GPU $(date '+%F %T') items=$ITEMS ids=$IDS_PLUS ==="
echo "=== runner: mode reasoned, reason-tokens 110, max-model-len 4096, tp 1, temp 0 ==="
CUDA_VISIBLE_DEVICES=$GPU $PY src/run_model.py \
  --model "$model" --tag "$TAG" --kinds "$KINDS_PLUS" --items "$ITEMS" \
  --only-ids "$IDS_PLUS" \
  --out "results/raw/${TAG}_g24a_p2${SUF}_plus.jsonl" \
  --mode reasoned --reason-tokens 110 --max-model-len 4096 --tp 1 \
  --gpu-frac 0.85 --enforce-eager

echo "=== G24A P2 arm- $TAG gpu$GPU $(date '+%F %T') items=$ITEMS ids=$IDS_MINUS ==="
CUDA_VISIBLE_DEVICES=$GPU $PY src/run_model.py \
  --model "$model" --tag "$TAG" --kinds "$KINDS_MINUS" --items "$ITEMS" \
  --only-ids "$IDS_MINUS" \
  --out "results/raw/${TAG}_g24a_p2${SUF}_minus.jsonl" \
  --mode reasoned --reason-tokens 110 --max-model-len 4096 --tp 1 \
  --gpu-frac 0.85 --enforce-eager
echo "G24A P2 DONE: $TAG (arm+ 1000 rows, arm- 800 rows)"
