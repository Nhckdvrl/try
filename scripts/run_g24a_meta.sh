#!/usr/bin/env bash
# G24A §14 explanation run — RQ3 second-order / meta-evidence experiment
# (registration §14, user-ruled 2026-09-26; no scientific gate, no staged
# stop, no selector, no probes):
#   200 discovery claims x 13 cells x 6 panel models = 15,600 decision rows.
# Cells: base (claim only, evidence-free, PLUS arm only) + {admit_post,
# exclude_post, strong_exclude_post, counterfactual_delete_post,
# meta_neutral_post, random_reason_post} x {arm+, arm-}.
#
# TWO invocations per model (run_model --out opens "w", so separate files):
#   arm+ : 200 ids x 7 kinds (incl. base)  -> 1,400 rows
#   arm- : 200 ids x 6 kinds (no base)     -> 1,200 rows
# base is never issued on arm-: its prompt is byte-identical across arms
# (verified by verify_g24a_meta_prompts.py), so Y0 is shared by construction
# and re-running it would only duplicate rows.  -> exactly 13 rows/claim.
#
# Material: the committed P2 item file and id lists byte-reused (§14.1) —
# same 200 discovery same-claim pairs, no new sampling. The four legacy
# operators are re-run IN THIS BATCH so the CRE table is self-contained and
# 6-model complete (P1/P2 only ever ran 5 models); their prompts render
# through the unmodified G24A/P1 modules, character-identical to P1/P2.
#
# Model snapshots pinned exactly as run_g24a_confa.sh (data/model_panel_g4.json)
# PLUS the frozen Qwen3-32B addition of §13.4 (revision
# 9216db5781bf21249d130ec9da846c4624c16137).  Same runner args as P2-P4
# (mode reasoned, reason-tokens 110, max-model-len 4096, tp 1, gpu-frac
# 0.85, eager, temp-0 digit expectation).
#
# GPU layout (per §14.5: six free A100 80GB — fvcrc10 + fvcrc12, one model
# per card); Qwen3-32B keeps its OWN segment (one A100, tp 1, gpu-frac 0.85),
# never co-resident with another vLLM instance:
#   fvcrc10 GPU0 mistral-small-24b | GPU1 qwen3-32b
#   fvcrc10 GPU2 llama31-8b        | GPU3 qwen3-8b
#   fvcrc12 GPU0 qwen35-9b         | GPU1 gemma3-12b
#
# Usage: scripts/run_g24a_meta.sh <gpu> <tag>
#   e.g. scripts/run_g24a_meta.sh 2 qwen3-8b
# Run env (§14.5 reconstruction for the 550/12.4-driver fvcrc10/12 cards):
#   prefix G24A_META_PY=/home/xiang/.venvs/vllm023-cu128/bin/python
#   (default PY = frozen fgvd env, for CUDA-13 driver machines)
# Smoke (4 ids/arm, suffixed outputs, does NOT touch full raws):
#   G24A_META_SMOKE=1 scripts/run_g24a_meta.sh <gpu> <tag>
set -euo pipefail
cd /home/xiang/research_hun/try_clone
export PATH=/home/xiang/miniconda3/envs/fgvd/bin:$PATH
export HF_HUB_OFFLINE=1
export VLLM_LOGGING_LEVEL=WARNING
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export TOKENIZERS_PARALLELISM=false
export VLLM_USE_FLASHINFER_SAMPLER=0
# PY may be overridden for the §14.3 run-environment addendum (see the
# registration): the frozen default is the fgvd env; the fvcrc10/12 A100
# reconstruction (same vllm/transformers versions, torch cu128 build tag)
# is passed via G24A_META_PY.
PY=${G24A_META_PY:-/home/xiang/miniconda3/envs/fgvd/bin/python}
HUB=/home/xiang/.cache/huggingface/hub

GPU=${1:?usage: run_g24a_meta.sh <gpu> <tag>}
TAG=${2:?usage: run_g24a_meta.sh <gpu> <tag>}
ITEMS=${G24A_META_ITEMS:-data/items/g24a_p2_v1.jsonl}
IDS_PLUS=${G24A_META_IDS_PLUS:-data/items/g24a_p2_ids_plus.json}
IDS_MINUS=${G24A_META_IDS_MINUS:-data/items/g24a_p2_ids_minus.json}
SUF=${G24A_META_SUF:-}
# kind lists mirror scripts/verify_g24a_meta_prompts.py (KINDS_PLUS /
# KINDS_MINUS); the verifier parses these lines — keep the two files in sync.
KINDS_PLUS=base,admit_post,exclude_post,strong_exclude_post,counterfactual_delete_post,meta_neutral_post,random_reason_post
KINDS_MINUS=admit_post,exclude_post,strong_exclude_post,counterfactual_delete_post,meta_neutral_post,random_reason_post

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

if [ "${G24A_META_SMOKE:-0}" = "1" ]; then
  SUF=${G24A_META_SUF:-_smoke}
  $PY - <<'PYEOF'
import json, pathlib
for arm in ("plus", "minus"):
    ids = json.load(open(f"data/items/g24a_p2_ids_{arm}.json"))
    p = pathlib.Path(f"logs/g24a_meta_smoke_ids_{arm}.json")
    p.parent.mkdir(exist_ok=True)
    p.write_text(json.dumps(ids[:4]) + "\n")
PYEOF
  IDS_PLUS=logs/g24a_meta_smoke_ids_plus.json
  IDS_MINUS=logs/g24a_meta_smoke_ids_minus.json
  echo "=== SMOKE: 4 ids/arm, outputs carry suffix '$SUF' ==="
fi

mkdir -p logs results/raw
echo "=== G24A §14 meta arm+ $TAG gpu$GPU $(date '+%F %T') items=$ITEMS ids=$IDS_PLUS ==="
echo "=== runner: mode reasoned, reason-tokens 110, max-model-len 4096, tp 1, temp 0 ==="
CUDA_VISIBLE_DEVICES=$GPU $PY src/run_model.py \
  --model "$model" --tag "$TAG" --kinds "$KINDS_PLUS" --items "$ITEMS" \
  --only-ids "$IDS_PLUS" \
  --out "results/raw/${TAG}_g24a_meta${SUF}_plus.jsonl" \
  --mode reasoned --reason-tokens 110 --max-model-len 4096 --tp 1 \
  --gpu-frac 0.85 --enforce-eager

echo "=== G24A §14 meta arm- $TAG gpu$GPU $(date '+%F %T') items=$ITEMS ids=$IDS_MINUS ==="
CUDA_VISIBLE_DEVICES=$GPU $PY src/run_model.py \
  --model "$model" --tag "$TAG" --kinds "$KINDS_MINUS" --items "$ITEMS" \
  --only-ids "$IDS_MINUS" \
  --out "results/raw/${TAG}_g24a_meta${SUF}_minus.jsonl" \
  --mode reasoned --reason-tokens 110 --max-model-len 4096 --tp 1 \
  --gpu-frac 0.85 --enforce-eager
echo "G24A §14 meta DONE: $TAG (arm+ 1400 rows, arm- 1200 rows)"
