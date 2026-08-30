#!/usr/bin/env bash
# Stage the Qwen3.5 size-sweep checkpoints byte-for-byte onto local NVMe, the
# same way the frozen panel was staged, and record the exact revision hash of
# each snapshot so the preregistration can pin it before any run.
set -euo pipefail

CACHE=${HF_HOME:-$HOME/.cache/huggingface}/hub
DEST=/var/tmp/xiang-isr-models

stage() {
  local repo=$1 tag=$2
  local repo_dir="$CACHE/models--Qwen--$repo"
  if [ ! -d "$repo_dir/snapshots" ]; then
    echo "MISSING: $repo has no local snapshot under $repo_dir" >&2
    return 1
  fi
  local revision
  revision=$(ls "$repo_dir/snapshots" | head -1)
  mkdir -p "$DEST/$tag"
  cp -rL "$repo_dir/snapshots/$revision/." "$DEST/$tag/"
  echo "$tag  Qwen/$repo  $revision"
}

stage Qwen3.5-2B qwen35-2b || true
stage Qwen3.5-4B qwen35-4b
stage Qwen3.5-27B qwen35-27b
