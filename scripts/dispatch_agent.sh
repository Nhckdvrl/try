#!/usr/bin/env bash
d () {
  local host=$1 gpu=$2 env=$3 model=$4 tag=$5; shift 5
  ssh -o BatchMode=yes -o StrictHostKeyChecking=no "$host" \
    "cd /home/xiang/research_hun/try_clone && nohup bash scripts/agent_one.sh $gpu $env '$model' '$tag' $* \
     > logs/agent/${tag}.log 2>&1 < /dev/null &"
  echo "  agent $tag -> $host:gpu$gpu ($env)"
}
V=verl-clean
d fvcrc10 0 $V Qwen/Qwen3-8B                 qwen3-8b          --gpu-frac 0.85
d fvcrc10 1 $V google/gemma-3-12b-it         gemma3-12b        --gpu-frac 0.85
d fvcrc12 1 $V microsoft/Phi-4-mini-instruct phi4-mini         --gpu-frac 0.75
d fvcrc21 1 fgvd Qwen/Qwen3.5-27B            qwen3.5-27b       --gpu-frac 0.70 --max-num-seqs 128 --enforce-eager
