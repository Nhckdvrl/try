#!/usr/bin/env bash
d () {
  local host=$1 gpu=$2 env=$3 model=$4 tag=$5; shift 5
  ssh -o BatchMode=yes -o StrictHostKeyChecking=no "$host" \
    "cd /home/xiang/research_hun/try_clone && nohup bash scripts/routing_one.sh $gpu $env '$model' '$tag' $* \
     > logs/routing/${tag}.log 2>&1 < /dev/null &"
  echo "  routing $tag -> $host:gpu$gpu ($env)"
}
V=verl-clean
d fvcrc10 0 $V Qwen/Qwen3-8B                 qwen3-8b          --gpu-frac 0.90
d fvcrc10 2 $V google/gemma-3-12b-it         gemma3-12b        --gpu-frac 0.90
d fvcrc21 1 fgvd data/mistral_small_24b_hf   mistral-small-24b --gpu-frac 0.80 --max-num-seqs 128
d fvcrc21 3 fgvd Qwen/Qwen3.5-9B             qwen3.5-9b        --gpu-frac 0.80
