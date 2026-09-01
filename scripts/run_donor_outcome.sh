#!/usr/bin/env bash
set -uo pipefail
cd /home/xiang/research_hun/try_clone
export PATH=/home/xiang/miniconda3/envs/fgvd/bin:$PATH
export HF_HUB_OFFLINE=1 VLLM_LOGGING_LEVEL=WARNING PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
HUB=${HF_HUB:-/home/xiang/.cache/huggingface/hub}
meta(){ python -c "import json
for c in json.load(open('data/model_panel_g4.json'))['checkpoints']:
    if c['tag']=='$1': print(c['$2']); break"; }
run(){ local gpu=$1 tag=$2 mid rev path extra=""; mid=$(meta "$tag" model_id); rev=$(meta "$tag" revision); path="$HUB/models--${mid//\//--}/snapshots/$rev"; [ -d "/var/tmp/xiang-isr-models/$tag" ]&&path="/var/tmp/xiang-isr-models/$tag"; case "$tag" in qwen35-*) extra="--enforce-eager";; mistral-*) extra="--tokenizer-mode mistral";; esac; out="results/raw/isr_${tag}_g12_donor_outcome.jsonl"; [ -s "$out" ]&&{ echo skip; return; }; CUDA_VISIBLE_DEVICES=$gpu python src/run_donor_outcome.py --model "$path" --model-id "$mid" --model-revision "$rev" --tag "$tag" --out "$out" --max-num-seqs 64 $extra; }
mkdir -p logs results/raw; run "$1" "$2" >"logs/isr_g12_$2.log" 2>&1
