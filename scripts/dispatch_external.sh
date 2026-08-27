#!/usr/bin/env bash
d () {
  local host=$1 gpu=$2 env=$3 model=$4 tag=$5; shift 5
  ssh -o BatchMode=yes -o StrictHostKeyChecking=no "$host" \
    "cd /home/xiang/research_hun/try_clone && nohup bash scripts/external_one.sh $gpu $env '$model' '$tag' $* \
     > logs/external/${tag}.log 2>&1 < /dev/null &"
  echo "  external $tag -> $host:gpu$gpu"
}
V=verl-clean
d fvcrc12 0 $V Qwen/Qwen3-8B                 qwen3-8b          --gpu-frac 0.80
d fvcrc12 1 $V google/gemma-3-12b-it         gemma3-12b        --gpu-frac 0.80
d fvcrc21 1 fgvd microsoft/Phi-4-mini-instruct phi4-mini       --gpu-frac 0.70
d fvcrc21 3 fgvd data/mistral_small_24b_hf   mistral-small-24b --gpu-frac 0.70 --max-num-seqs 128
