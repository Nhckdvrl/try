#!/usr/bin/env bash
# vLLM selects the mistral-common tokenizer backend when tekken.json / params.json
# are present, and that backend has no `is_fast` under transformers 5.x. This builds
# a directory exposing only the HF-format tokenizer.json, which both accept.
set -e
SRC=$(ls -d "${HF_HOME:-$HOME/.cache/huggingface}"/hub/models--mistralai--Mistral-Small-24B-Instruct-2501/snapshots/*/ | head -1)
DST="$(dirname "$0")/../data/mistral_small_24b_hf"
mkdir -p "$DST"
for f in "$SRC"*; do
  b=$(basename "$f")
  case "$b" in tekken.json|params.json|SYSTEM_PROMPT.txt|README.md) continue;; esac
  ln -sf "$f" "$DST/$b"
done
echo "shim -> $DST"
