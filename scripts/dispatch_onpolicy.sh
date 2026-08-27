#!/usr/bin/env bash
d () {
  local host=$1 gpu=$2 env=$3 model=$4 tag=$5; shift 5
  ssh -o BatchMode=yes -o StrictHostKeyChecking=no "$host" \
    "cd /home/xiang/research_hun/try_clone && nohup bash scripts/onpolicy_one.sh $gpu $env '$model' '$tag' $* \
     > logs/onpolicy/${tag}.log 2>&1 < /dev/null &"
  echo "  onpolicy $tag -> $host:gpu$gpu"
}
V=verl-clean
d fvcrc21 1 fgvd Qwen/Qwen3-8B                qwen3-8b          --gpu-frac 0.70
d fvcrc21 3 fgvd google/gemma-3-12b-it        gemma3-12b        --gpu-frac 0.70
d fvcrc12 1 $V microsoft/Phi-4-mini-instruct phi4-mini         --gpu-frac 0.70
d fvcrc13 3 $V data/mistral_small_24b_hf     mistral-small-24b --gpu-frac 0.70
