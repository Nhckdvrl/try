#!/usr/bin/env bash
export HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=2
PY=/home/xiang/miniconda3/envs/fgvd/bin/python
MP=$(ls -d /home/xiang/.cache/huggingface/hub/models--mistralai--Mistral-Small-24B-Instruct-2501/snapshots/*/ | head -1)
$PY src/mech/experiments.py --model google/gemma-3-12b-it \
    --out results/mech/experiments_gemma3-12b.json || echo "FAILED: gemma3-12b"
$PY src/mech/experiments.py --model Qwen/Qwen2.5-7B-Instruct \
    --out results/mech/experiments_qwen2.5-7b.json || echo "FAILED: qwen2.5-7b"
$PY src/mech/experiments.py --model "$MP" \
    --out results/mech/experiments_mistral-small-24b.json || echo "FAILED: mistral"
echo "MECH DONE"
