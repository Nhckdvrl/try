set -e
K=exclude_pre_repeat,admit_pre_repeat,exclude_post_reencode,sanitation,ledger
export PATH=/home/xiang/miniconda3/envs/fgvd/bin:$PATH HF_HUB_OFFLINE=1 VLLM_LOGGING_LEVEL=WARNING CUDA_VISIBLE_DEVICES=2
PY=/home/xiang/miniconda3/envs/fgvd/bin/python
for M in "Qwen/Qwen3-4B qwen3-4b" "Qwen/Qwen3-8B qwen3-8b" "Qwen/Qwen3-14B qwen3-14b" "Qwen/Qwen3-32B qwen3-32b"; do
  set -- $M
  $PY src/run_model.py --model $1 --tag $2 --kinds $K --only-ids data/items/frozen_v1.json \
      --out results/raw/$2_extra.jsonl --max-model-len 3072 --gpu-frac 0.88
done
