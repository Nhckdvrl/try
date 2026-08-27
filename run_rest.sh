set -e
KINDS=base,admit_pre,admit_post,exclude_pre,exclude_post,rule_probe_exclude_pre,rule_probe_exclude_post,rule_probe_admit_post,memory_probe_exclude_post
export PATH=/home/xiang/miniconda3/envs/fgvd/bin:$PATH
export HF_HUB_OFFLINE=1 VLLM_LOGGING_LEVEL=WARNING CUDA_VISIBLE_DEVICES=2
PY=/home/xiang/miniconda3/envs/fgvd/bin/python
$PY src/run_model.py --model Qwen/Qwen3-14B --tag qwen3-14b --kinds $KINDS \
  --only-ids data/items/frozen_v1.json --out results/raw/qwen3-14b_main.jsonl --max-model-len 3072
$PY src/run_model.py --model Qwen/Qwen3-32B --tag qwen3-32b --kinds $KINDS \
  --only-ids data/items/frozen_v1.json --out results/raw/qwen3-32b_main.jsonl --max-model-len 3072 --gpu-frac 0.88
$PY src/run_model.py --model Qwen/Qwen3-4B --tag qwen3-4b --kinds $KINDS \
  --only-ids data/items/frozen_v1.json --out results/raw/qwen3-4b_main.jsonl --max-model-len 3072
