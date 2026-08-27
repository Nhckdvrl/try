#!/usr/bin/env bash
launch () {
  local host=$1 gpu=$2 model=$3 tag=$4; shift 4
  ssh -o BatchMode=yes -o StrictHostKeyChecking=no "$host" \
    "cd /home/xiang/research_hun/try_clone && nohup bash scripts/stage4_one.sh $gpu '$model' '$tag' $* \
     > logs/stage4/$tag.log 2>&1 < /dev/null &"
  echo "launched S4 $tag on $host gpu$gpu"
}
launch fvcrc20 1 Qwen/Qwen3-8B              qwen3-8b          --gpu-frac 0.85
launch fvcrc20 2 google/gemma-3-12b-it      gemma3-12b        --gpu-frac 0.85
launch fvcrc20 3 data/mistral_small_24b_hf  mistral-small-24b --gpu-frac 0.80
launch fvcrc13 2 Qwen/Qwen3.5-27B           qwen3.5-27b       --gpu-frac 0.88 --max-num-seqs 128 --enforce-eager
launch fvcrc13 3 Qwen/Qwen3-32B             qwen3-32b         --gpu-frac 0.92
launch fvcrc10 3 microsoft/Phi-4-mini-instruct phi4-mini      --gpu-frac 0.85
