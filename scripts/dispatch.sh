#!/usr/bin/env bash
# dispatch <stage> <host> <gpu> <env> <model> <tag> <flags...>
d () {
  local stage=$1 host=$2 gpu=$3 env=$4 model=$5 tag=$6; shift 6
  ssh -o BatchMode=yes -o StrictHostKeyChecking=no "$host" \
    "cd /home/xiang/research_hun/try_clone && nohup bash scripts/${stage}_one.sh $gpu $env '$model' '$tag' $* \
     > logs/${stage}/${tag}.log 2>&1 < /dev/null &"
  echo "  $stage $tag -> $host:gpu$gpu ($env)"
}
V=verl-clean
# ---- Stage 3A, the four core models first ----
d stage3 fvcrc10 0 $V Qwen/Qwen3-8B                 qwen3-8b          --gpu-frac 0.90
d stage3 fvcrc10 1 $V google/gemma-3-12b-it         gemma3-12b        --gpu-frac 0.90
d stage3 fvcrc12 0 $V data/mistral_small_24b_hf     mistral-small-24b --gpu-frac 0.90
d stage3 fvcrc21 2 fgvd Qwen/Qwen3.5-27B            qwen3.5-27b       --gpu-frac 0.78 --max-num-seqs 128 --enforce-eager
d stage3 fvcrc13 0 $V Qwen/Qwen3-32B                qwen3-32b         --gpu-frac 0.92
d stage3 fvcrc13 1 $V microsoft/Phi-4-mini-instruct phi4-mini         --gpu-frac 0.85
# ---- Stage 4 paraphrases in parallel ----
d stage4 fvcrc10 2 $V Qwen/Qwen3-8B                 qwen3-8b          --gpu-frac 0.90
d stage4 fvcrc10 3 $V google/gemma-3-12b-it         gemma3-12b        --gpu-frac 0.90
d stage4 fvcrc12 1 $V data/mistral_small_24b_hf     mistral-small-24b --gpu-frac 0.90
d stage4 fvcrc13 2 $V Qwen/Qwen3-32B                qwen3-32b         --gpu-frac 0.92
d stage4 fvcrc13 3 $V microsoft/Phi-4-mini-instruct phi4-mini         --gpu-frac 0.85
