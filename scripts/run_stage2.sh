#!/usr/bin/env bash
cd /home/xiang/research_hun/try_clone
export PATH=/home/xiang/miniconda3/envs/fgvd/bin:$PATH
export HF_HUB_OFFLINE=1 VLLM_LOGGING_LEVEL=WARNING CUDA_VISIBLE_DEVICES=2
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
PY=/home/xiang/miniconda3/envs/fgvd/bin/python
K=base,pos_adm_pre_d0,pos_adm_pre_d1,pos_adm_pre_d2,pos_adm_post_d0,pos_adm_post_d1,pos_adm_post_d2,pos_exc_pre_d0,pos_exc_pre_d1,pos_exc_pre_d2,pos_exc_post_d0,pos_exc_post_d1,pos_exc_post_d2,id_base,id_admit_pre,id_admit_post,id_exclude_pre,id_exclude_post,id_exclude_pre_marker,w000_pre,w000_post,w025_pre,w025_post,w050_pre,w050_post,w075_pre,w075_post,w100_pre,w100_post
run () {
  echo "=== S2 $2 ==="
  $PY src/run_model.py --model "$1" --tag "$2" --kinds $K \
      --only-ids data/items/frozen_v1.json --out results/raw/$2_stage2.jsonl \
      --max-model-len 4096 ${3:-} || echo "FAILED: $2"
}
run Qwen/Qwen3-8B          qwen3-8b     "--gpu-frac 0.80"
run google/gemma-3-12b-it  gemma3-12b   "--gpu-frac 0.80"
run data/mistral_small_24b_hf mistral-small-24b "--gpu-frac 0.78 --max-num-seqs 128"
run Qwen/Qwen3.5-27B       qwen3.5-27b  "--gpu-frac 0.78 --max-num-seqs 128 --enforce-eager"
echo "STAGE2 DONE"
