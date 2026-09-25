#!/usr/bin/env bash
# G24A Confirmation B run — RQ2/F2 + RQ3/F3 replication, registration §13.3
# (frozen, user 2026-09-26):
#   200 fresh VitaminC SR pairs x 7 cells x 6 models = 8,400 decision rows.
# Cells (7): base, admit_post (arm+), counterfactual_delete_post (arm+),
# admit_post (arm-), counterfactual_delete_post (arm-), withheld_cf,
# irrelevant_cf.
#
# THREE invocations per model (run_model --out opens "w"; cell groups are
# anchored to arms exactly as §13.3 — base and withheld_cf on plus only,
# irrelevant_cf on control only):
#   plus   : 200 ids x 4 kinds (base, admit_post, counterfactual_delete_post,
#            withheld_cf)                          ->   800 rows
#   minus  : 200 ids x 2 kinds (admit_post, counterfactual_delete_post)
#                                                      ->   400 rows
#   control: 200 ids x 1 kind  (irrelevant_cf)      ->   200 rows
#                                                     = 1,400 rows/model
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
# Usage: scripts/run_g24a_confb.sh <gpu> <tag>
#   e.g. scripts/run_g24a_confb.sh 2 qwen3-8b
# Smoke (4 ids/arm, suffixed outputs, does NOT touch full raws):
#   G24A_CONFB_SMOKE=1 scripts/run_g24a_confb.sh <gpu> <tag>
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

GPU=${1:?usage: run_g24a_confb.sh <gpu> <tag>}
TAG=${2:?usage: run_g24a_confb.sh <gpu> <tag>}
ITEMS=${G24A_CONFB_ITEMS:-data/items/g24a_confb_v1.jsonl}
IDS_PLUS=${G24A_CONFB_IDS_PLUS:-data/items/g24a_confb_ids_plus.json}
IDS_MINUS=${G24A_CONFB_IDS_MINUS:-data/items/g24a_confb_ids_minus.json}
IDS_CONTROL=${G24A_CONFB_IDS_CONTROL:-data/items/g24a_confb_ids_control.json}
SUF=${G24A_CONFB_SUF:-}
# kind lists mirror scripts/verify_g24a_confb_prompts.py (KINDS_PLUS /
# KINDS_MINUS / KINDS_CONTROL); the verifier parses these lines — keep the
# two files in sync.
KINDS_PLUS=base,admit_post,counterfactual_delete_post,withheld_cf
KINDS_MINUS=admit_post,counterfactual_delete_post
KINDS_CONTROL=irrelevant_cf

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
test -f "$IDS_PLUS" || { echo "missing id list: $IDS_PLUS" >&2; exit 1; }
test -f "$IDS_MINUS" || { echo "missing id list: $IDS_MINUS" >&2; exit 1; }
test -f "$IDS_CONTROL" || { echo "missing id list: $IDS_CONTROL" >&2; exit 1; }

if [ "${G24A_CONFB_SMOKE:-0}" = "1" ]; then
  SUF=${G24A_CONFB_SUF:-_smoke}
  $PY - <<'PYEOF'
import json, pathlib
for arm in ("plus", "minus", "control"):
    ids = json.load(open(f"data/items/g24a_confb_ids_{arm}.json"))
    p = pathlib.Path(f"logs/g24a_confb_smoke_ids_{arm}.json")
    p.parent.mkdir(exist_ok=True)
    p.write_text(json.dumps(ids[:4]) + "\n")
PYEOF
  IDS_PLUS=logs/g24a_confb_smoke_ids_plus.json
  IDS_MINUS=logs/g24a_confb_smoke_ids_minus.json
  IDS_CONTROL=logs/g24a_confb_smoke_ids_control.json
  echo "=== SMOKE: 4 ids/arm, outputs carry suffix '$SUF' ==="
fi

mkdir -p logs results/raw
echo "=== G24A ConfB plus $TAG gpu$GPU $(date '+%F %T') items=$ITEMS ids=$IDS_PLUS ==="
echo "=== runner: mode reasoned, reason-tokens 110, max-model-len 4096, tp 1, temp 0 ==="
CUDA_VISIBLE_DEVICES=$GPU $PY src/run_model.py \
  --model "$model" --tag "$TAG" --kinds "$KINDS_PLUS" --items "$ITEMS" \
  --only-ids "$IDS_PLUS" \
  --out "results/raw/${TAG}_g24a_confb${SUF}_plus.jsonl" \
  --mode reasoned --reason-tokens 110 --max-model-len 4096 --tp 1 \
  --gpu-frac 0.85 --enforce-eager

echo "=== G24A ConfB minus $TAG gpu$GPU $(date '+%F %T') items=$ITEMS ids=$IDS_MINUS ==="
CUDA_VISIBLE_DEVICES=$GPU $PY src/run_model.py \
  --model "$model" --tag "$TAG" --kinds "$KINDS_MINUS" --items "$ITEMS" \
  --only-ids "$IDS_MINUS" \
  --out "results/raw/${TAG}_g24a_confb${SUF}_minus.jsonl" \
  --mode reasoned --reason-tokens 110 --max-model-len 4096 --tp 1 \
  --gpu-frac 0.85 --enforce-eager

echo "=== G24A ConfB control $TAG gpu$GPU $(date '+%F %T') items=$ITEMS ids=$IDS_CONTROL ==="
CUDA_VISIBLE_DEVICES=$GPU $PY src/run_model.py \
  --model "$model" --tag "$TAG" --kinds "$KINDS_CONTROL" --items "$ITEMS" \
  --only-ids "$IDS_CONTROL" \
  --out "results/raw/${TAG}_g24a_confb${SUF}_control.jsonl" \
  --mode reasoned --reason-tokens 110 --max-model-len 4096 --tp 1 \
  --gpu-frac 0.85 --enforce-eager
echo "G24A ConfB DONE: $TAG (plus 800, minus 400, control 200 = 1400 rows)"
