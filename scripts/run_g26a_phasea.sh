#!/usr/bin/env bash
# G26A Phase A — 4 no-rule cells × N_A = 3,640 feasible train items ×
# 1 selector model (mistral-small-24b, O1) = EXACTLY 14,560 rows
# (prereg §11 amended ceiling; §0 feasibility-gate amendment).
#
# AUTHORIZATION: this script does NOT authorize itself (prereg §0). Compute
# is released only by the explicit STATUS flip recorded in STATUS.md —
# the runtime gate below greps for the exact token G26A-FLIP1=RECORDED and
# refuses to launch without it. Phase A NEVER runs a rule cell: the kind
# list below is exactly Y0, YA, YB, YAB (selection blindness, §5), and the
# script refuses any kind list containing excl/admit/probe strings.
#
# Usage: scripts/run_g26a_phasea.sh <gpu>
#   e.g. scripts/run_g26a_phasea.sh 1
set -euo pipefail
cd /home/xiang/research_hun/try_clone
export PATH=/home/xiang/miniconda3/envs/fgvd/bin:$PATH
export HF_HUB_OFFLINE=1
export VLLM_LOGGING_LEVEL=WARNING
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export TOKENIZERS_PARALLELISM=false
export VLLM_USE_FLASHINFER_SAMPLER=0
PY=/home/xiang/miniconda3/envs/fgvd/bin/python

GPU=${1:?usage: run_g26a_phasea.sh <gpu>}

ITEMS=data/items/g26_phasea_pool_v1.jsonl
ITEMS_SHA=ad0ac715a609f49f9ad98af5cf6a3022a1b1e6f904d7a1f22ae2d490a7e2c95c
N_A=3640
ROWS_EXPECTED=$((N_A * 4))   # 14,560
KINDS=g26_y0,g26_ya,g26_yb,g26_yab
OUT=results/raw/g26a_phasea_mistral-small-24b.jsonl

# --- authorization gate: STATUS flip #1 must be recorded (user-owned) -----
if ! grep -q "G26A-FLIP1=RECORDED" STATUS.md; then
  echo "REFUSED: STATUS.md has no G26A-FLIP1=RECORDED token (prereg §0/§11:" >&2
  echo "this script does not authorize itself; wait for the user's flip #1)" >&2
  exit 5
fi

# --- blindness: kinds must be exactly the 4 no-rule cells ------------------
case "$KINDS" in
  *excl*|*admit*|*probe*) echo "REFUSED: rule/probe kind in Phase A" >&2; exit 5 ;;
esac
if [ "$KINDS" != "g26_y0,g26_ya,g26_yb,g26_yab" ]; then
  echo "REFUSED: kind list drifted from the prereg 4 no-rule cells" >&2
  exit 5
fi

# --- frozen pool: sha256 pin + row budget ---------------------------------
if [ ! -f "$ITEMS" ]; then
  echo "REFUSED: missing $ITEMS" >&2
  exit 5
fi
ACTUAL_SHA=$(sha256sum "$ITEMS" | cut -d' ' -f1)
if [ "$ACTUAL_SHA" != "$ITEMS_SHA" ]; then
  echo "REFUSED: $ITEMS sha256 $ACTUAL_SHA != pinned $ITEMS_SHA" >&2
  echo "(pool is frozen at the Phase-A tag; rebuilds need a prereg §0 amendment)" >&2
  exit 5
fi

# --- one-shot discipline: never overwrite an existing output ---------------
if [ -f "$OUT" ]; then
  echo "REFUSED: $OUT already exists — Phase A is one-shot; a rerun for" >&2
  echo "mechanical incompleteness is a separate, explicit decision." >&2
  exit 5
fi

mkdir -p logs results/raw
echo "=== G26A Phase A selector mistral-small-24b gpu$GPU $(date '+%F %T') ==="
echo "=== auth: G26A-FLIP1=RECORDED in STATUS.md | items sha256 $ITEMS_SHA ==="
echo "=== kinds: $KINDS (NO rule cell, NO probe — blindness by construction) ==="
echo "=== budget: N_A=$N_A x 4 = $ROWS_EXPECTED rows (§11 ceiling) ==="
echo "=== runner: mode reasoned, reason-tokens 110, max-model-len 4096, tp 1, temp 0 ==="

CUDA_VISIBLE_DEVICES=$GPU $PY src/run_model.py \
  --model data/mistral_small_24b_hf \
  --tag mistral-small-24b \
  --kinds "$KINDS" \
  --items "$ITEMS" \
  --out "$OUT" \
  --mode reasoned --reason-tokens 110 --max-model-len 4096 --tp 1 \
  --gpu-frac 0.85 --enforce-eager

# --- post-run: exact row count, then freeze by hash ------------------------
N_ROWS=$(wc -l < "$OUT")
if [ "$N_ROWS" -ne "$ROWS_EXPECTED" ]; then
  echo "INCOMPLETE (mechanical): $N_ROWS rows != expected $ROWS_EXPECTED" >&2
  echo "(missing rows must be rerun before any gate computation, §11/exit 4)" >&2
  exit 4
fi
echo "G26A PHASE A DONE rows=$N_ROWS sha256=$(sha256sum "$OUT" | cut -d' ' -f1)"
