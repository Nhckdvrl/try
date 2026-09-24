#!/usr/bin/env python3
"""Run the VitaminC exclusion pilot (spec v2) with vLLM.

Standalone runner: builds prompts from the pool file per cell, mirrors
src/run_model.py's chat-template handling and two-stage readout (greedy
rationale stopped at ANSWER:, then one forced token whose 0-9 expectation is
rescaled x100/9). No schema/conditions import; frozen G26A files untouched.

Stage-1a:  --cells y0,yplus,yminus            (600 rows)
Stage-1b:  --cells exclpre_plus,exclpre_minus  (400 rows, only if gates green)

Run:
  CUDA_VISIBLE_DEVICES=0 /home/xiang/miniconda3/envs/fgvd/bin/python \
    scripts/run_vitaminc_pilot.py --cells y0,yplus,yminus \
    --out results/pilots/vitaminc_pilot_r1/raw_r1a.jsonl
"""
from __future__ import annotations

import argparse
import json
import math
import os
from pathlib import Path

# Engine env — mirrors scripts/run_g26a_phasea.sh byte-for-byte. Without
# VLLM_USE_FLASHINFER_SAMPLER=0 the vLLM engine warmup dies on this machine
# (flashinfer JIT check_cuda_arch: "SM 12.x requires CUDA >= 12.9" ->
# "FlashInfer requires sm75 or higher"), which is output-neutral: greedy
# argmax and the forced-token logits are identical either way.
os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("VLLM_LOGGING_LEVEL", "WARNING")
os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
os.environ.setdefault("VLLM_USE_FLASHINFER_SAMPLER", "0")

# G0/G24A lineage constants, byte-identical to spec v2 (src/schema.py values,
# imported as literals so no frozen file is modified or load-order dependent).
SYSTEM = ("You are a careful decision maker. Follow every instruction in the "
          "context exactly. Answer with the requested format and nothing else.")
QUESTION = "Considering everything above, rate the likelihood that the claim is true."
OUTPUT_SPEC = ("Use a scale from 0 to 9, where 0 means certainly false and "
               "9 means certainly true.")
REASON_TAIL = ("Think in at most two short sentences. Then write a final line "
               "of exactly this form:\nANSWER: <your answer>")
ANSWER_CUE = "ANSWER:"
RULING_BLOCK = ("RULING\nThe evidence shown below is excluded. It must not "
                "influence your final judgment.")
SEP = "\n\n"

CELLS = ("y0", "yplus", "yminus", "exclpre_plus", "exclpre_minus")
DIGITS = [str(d) for d in range(10)]


def blocks_for(cell: str, item: dict) -> list[str]:
    claim = f"CLAIM\n{item['claim']}"
    if cell == "y0":
        return [claim]
    if cell == "yplus":
        return [f"EVIDENCE\n{item['evidence_s']}", claim]
    if cell == "yminus":
        return [f"EVIDENCE\n{item['evidence_r']}", claim]
    if cell == "exclpre_plus":
        return [RULING_BLOCK, f"EVIDENCE\n{item['evidence_s']}", claim]
    if cell == "exclpre_minus":
        return [RULING_BLOCK, f"EVIDENCE\n{item['evidence_r']}", claim]
    raise ValueError(f"unknown cell {cell!r}")


def user_prompt(cell: str, item: dict) -> str:
    return (SEP.join(blocks_for(cell, item)) + SEP + "TASK\n" + QUESTION
            + "\n" + OUTPUT_SPEC + "\n" + REASON_TAIL)


def digit_expectation(out):
    """Same math as src/run_model.py::digit_expectation (0-9 EV x100/9)."""
    lp = out.outputs[0].logprobs
    if not lp:
        return None, 0.0
    dist = {v.decoded_token: math.exp(v.logprob) for v in lp[0].values()}
    p = {k: 0.0 for k in DIGITS}
    for tokstr, prob in dist.items():
        t = (tokstr or "").strip()
        if t in p:
            p[t] += prob
    mass = sum(p.values())
    if mass <= 0:
        return None, 0.0
    ev = sum(int(k) * v for k, v in p.items()) / mass
    return ev * 100.0 / 9.0, mass


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pool", default="results/pilots/vitaminc_pilot_r1/pool_v2.jsonl")
    ap.add_argument("--cells", required=True, help="comma list")
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", default="data/mistral_small_24b_hf")
    ap.add_argument("--tag", default="mistral-small-24b")
    ap.add_argument("--tp", type=int, default=1)
    ap.add_argument("--gpu-frac", type=float, default=0.85)
    ap.add_argument("--max-model-len", type=int, default=2048)
    ap.add_argument("--reason-tokens", type=int, default=110)
    ap.add_argument("--enforce-eager", action=argparse.BooleanOptionalAction,
                    default=True,
                    help="skip CUDA graph capture (G26A harness parity)")
    args = ap.parse_args()

    cells = args.cells.split(",")
    for c in cells:
        if c not in CELLS:
            raise SystemExit(f"unknown cell {c!r} (allowed: {CELLS})")
    items = [json.loads(l) for l in open(args.pool, encoding="utf-8")]
    if len(items) != 200:
        raise SystemExit(f"pool has {len(items)} items, expected 200")

    from transformers import AutoTokenizer
    from vllm import LLM, SamplingParams
    tok = AutoTokenizer.from_pretrained(args.model)

    # Mirrors run_model.py::chat_ids: prompts as token ids (no double BOS).
    def chat_ids(user: str) -> list[int]:
        msgs = [{"role": "system", "content": SYSTEM},
                {"role": "user", "content": user}]
        kw = dict(tokenize=True, add_generation_prompt=True)
        try:
            enc = tok.apply_chat_template(msgs, enable_thinking=False, **kw)
        except TypeError:
            enc = tok.apply_chat_template(msgs, **kw)
        ids = enc["input_ids"] if hasattr(enc, "keys") else enc
        return list(ids[0]) if ids and isinstance(ids[0], (list, tuple)) else list(ids)

    def raw_ids(text: str) -> list[int]:
        return tok(text, add_special_tokens=False)["input_ids"]

    def tp(ids):
        return {"prompt_token_ids": list(ids)}

    recs = []
    for it in items:
        for c in cells:
            recs.append({"pilot_id": it["pilot_id"], "cell": c, "kind": "digit",
                         "ids": chat_ids(user_prompt(c, it))})

    llm = LLM(model=args.model, tensor_parallel_size=args.tp,
              gpu_memory_utilization=args.gpu_frac, max_model_len=args.max_model_len,
              dtype="bfloat16", max_logprobs=40, disable_log_stats=True,
              enforce_eager=args.enforce_eager)

    # Stage 1: greedy rationale, stopped at the answer cue.
    sp1 = SamplingParams(temperature=0.0, max_tokens=args.reason_tokens,
                         stop=[ANSWER_CUE])
    outs = llm.generate([tp(r["ids"]) for r in recs], sp1)
    for r, o in zip(recs, outs):
        r["reasoning"] = o.outputs[0].text
        r["reason_truncated"] = o.outputs[0].finish_reason != "stop"
        cue = o.outputs[0].text.rstrip() + "\n" + ANSWER_CUE + " "
        r["ids2"] = r["ids"] + raw_ids(cue)

    # Stage 2: read the digit at the fixed answer position.
    outs = llm.generate([tp(r["ids2"]) for r in recs],
                        SamplingParams(temperature=0.0, max_tokens=1, logprobs=40))
    for r, o in zip(recs, outs):
        r["raw"] = o.outputs[0].text
        r["value"], r["mass"] = digit_expectation(o)
        r["readout"] = "digit_expectation_0_100"

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as fh:
        for r in recs:
            r["n_prompt_tokens"] = len(r.pop("ids"))
            r.pop("ids2", None)
            r["model_tag"] = args.tag
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    bad = sum(1 for r in recs if r["value"] is None)
    lowmass = sum(1 for r in recs if r["mass"] < 0.5)
    trunc = sum(1 for r in recs if r["reason_truncated"])
    print(f"wrote {len(recs)} rows -> {out}")
    print(f"  cells {cells} | unparsed {bad} | digit-mass<0.5 {lowmass} | "
          f"rationale hit token cap {trunc}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
