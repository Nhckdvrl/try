#!/usr/bin/env bash
# G25A main pass — 400 items × 16 decision cells × 4 pooled models
# (= 25,600 rows) + O3 requested-weight-access probes (2 kinds × 400 × 4
# = 3,200 rows) -> <= 28,800 rows total, per prereg G25A §11 compute budget.
#
# AUTHORIZATION: this script does NOT authorize itself (prereg §0). Compute
# is released only by the explicit STATUS flip recorded in STATUS.md
# (prereg §11 step 3 / §12 last box — user-owned). As of 2026-09-24 the flip
# is PENDING: the design tag must be recorded first, then the ledger entry.
# The runtime warning below re-checks that on every launch.
#
# GPU layout (4 pooled models; the selector model mistral-small-24b is NEVER
# pooled — prereg §5/§6):
#   GPU1 llama31-8b then gemma3-12b | GPU2 qwen3-8b | GPU3 qwen35-9b
#   GPU0 free (panel has no 5th model; kept idle to mirror G24A layout)
#
# Usage: scripts/run_g25a_main.sh <gpu> <tag>
#   e.g. scripts/run_g25a_main.sh 2 qwen3-8b
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

GPU=${1:?usage: run_g25a_main.sh <gpu> <tag>}
TAG=${2:?usage: run_g25a_main.sh <gpu> <tag>}
ITEMS=${G25A_ITEMS:-data/items/g25_v1.jsonl}
ITEMS_SHA=7c6993244d7808d8e65696c00a55f4fc14c7f3011f34f0266e450f1367173147
KINDS=g25_base,g25_norule,g25_pre_w000,g25_pre_w001,g25_pre_w002,g25_pre_w005,g25_pre_w010,g25_pre_w025,g25_pre_w100,g25_post_w000,g25_post_w001,g25_post_w002,g25_post_w005,g25_post_w010,g25_post_w025,g25_post_w100,wprobe_g25_pre_w000,wprobe_g25_pre_w100

# Pinned snapshot revisions from data/model_panel_g4.json (frozen panel;
# identical snapshots to the G24A pass — prereg §5).
case "$TAG" in
  llama31-8b)   model=$HUB/models--NousResearch--Meta-Llama-3.1-8B-Instruct/snapshots/d10aef7999a2b5ba950ab3974312feeedbfe0b77 ;;
  qwen3-8b)     model=$HUB/models--Qwen--Qwen3-8B/snapshots/b968826d9c46dd6066d109eabc6255188de91218 ;;
  qwen35-9b)    model=$HUB/models--Qwen--Qwen3.5-9B/snapshots/c202236235762e1c871ad0ccb60c8ee5ba337b9a ;;
  gemma3-12b)   model=$HUB/models--google--gemma-3-12b-it/snapshots/96b6f1eccf38110c56df3a15bffe176da04bfd80 ;;
  *) echo "unknown tag $TAG (pooled-4 panel only; selector mistral is never pooled)" >&2; exit 1 ;;
esac
test -d "$model" || { echo "missing model dir: $model" >&2; exit 1; }
test -f "$ITEMS" || { echo "missing selected items: $ITEMS" >&2; exit 1; }

# Frozen items file must match its recorded sha256 before any forward pass.
have=$(sha256sum "$ITEMS" | cut -d' ' -f1)
test "$have" = "$ITEMS_SHA" || {
  echo "items sha256 mismatch: $have != $ITEMS_SHA (prereg §12)" >&2; exit 1; }

# STATUS-flip check (prereg §0/§11/§12): compute is released ONLY by the
# user-owned ledger flip, recorded as the exact token G25A-FLIP=RECORDED.
# Absent the token the script refuses unconditionally — no bypass variable,
# no way to run this script silently before the flip.
if ! grep -q "G25A-FLIP=RECORDED" STATUS.md; then
  echo "WARNING: token G25A-FLIP=RECORDED not found in STATUS.md" >&2
  echo "WARNING: the G25A STATUS flip (step 8) is user-owned and unrecorded;" >&2
  echo "WARNING: no forward pass is authorized before it (prereg §0, §11, §12)." >&2
  echo "refusing to run: record the STATUS flip first, then re-run." >&2
  exit 1
fi

mkdir -p logs results/raw
echo "=== G25A main $TAG gpu$GPU $(date '+%F %T') items=$ITEMS tag=g25a-near-zero-design-v1 ==="
echo "=== runner (prereg §11): mode reasoned, reason-tokens 110, max-model-len 4096, tp 1, temp 0 ==="
CUDA_VISIBLE_DEVICES=$GPU $PY src/run_model.py \
  --model "$model" --tag "$TAG" --kinds "$KINDS" --items "$ITEMS" \
  --out "results/raw/${TAG}_g25a.jsonl" \
  --mode reasoned --reason-tokens 110 --max-model-len 4096 --tp 1 \
  --gpu-frac 0.85 --enforce-eager
echo "G25A MAIN DONE: $TAG"
