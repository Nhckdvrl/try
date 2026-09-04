"""Run the G19 ReGround method evaluation with vLLM.

ReGround-Self uses the *same* checkpoint for a short policy-resolution call, then
compiles the predicted document IDs into a trusted ledger before the normal decision
call.  ReGround-Gold uses the known experimental match and is an upper bound.

Example:
  PYTHONPATH=src python3 src/run_reground.py \
    --model /path/to/Qwen3-8B --tag qwen3-8b \
    --out results/raw/qwen3-8b_reground.jsonl
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(__file__))

from schema import load_items, SYSTEM, ANSWER_FORMATS, ANSWER_CUE
from reground import (
    VARIANTS, METHODS, decision_messages, selector_prompt, parse_selection,
    gold_selection,
)

ROOT = os.path.join(os.path.dirname(__file__), "..")
ITEMS = os.path.join(ROOT, "data", "items", "g18_v1.jsonl")
DIGITS = [str(d) for d in range(10)]


def _dist(out):
    lp = out.outputs[0].logprobs
    if not lp:
        return {}
    return {v.decoded_token: math.exp(v.logprob) for v in lp[0].values()}


def digit_expectation(out):
    d = _dist(out)
    p = {k: 0.0 for k in DIGITS}
    for tokstr, prob in d.items():
        t = (tokstr or "").strip()
        if t in p:
            p[t] += prob
    mass = sum(p.values())
    if mass <= 0:
        return None, 0.0
    ev = sum(int(k) * v for k, v in p.items()) / mass
    return ev * 100.0 / 9.0, mass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--tag", required=True)
    ap.add_argument("--items", default=ITEMS)
    ap.add_argument("--out", required=True)
    ap.add_argument("--tp", type=int, default=1)
    ap.add_argument("--gpu-frac", type=float, default=0.85)
    ap.add_argument("--max-num-seqs", type=int, default=0)
    ap.add_argument("--enforce-eager", action="store_true")
    ap.add_argument("--max-model-len", type=int, default=3072)
    ap.add_argument("--mode", default="reasoned", choices=["reasoned", "direct", "cued"])
    ap.add_argument("--reason-tokens", type=int, default=110)
    args = ap.parse_args()

    items = load_items(args.items)

    from transformers import AutoTokenizer
    from vllm import LLM, SamplingParams

    tok = AutoTokenizer.from_pretrained(args.model)

    def chat_ids(msgs):
        kw = dict(tokenize=True, add_generation_prompt=True)
        try:
            enc = tok.apply_chat_template(msgs, enable_thinking=False, **kw)
        except TypeError:
            enc = tok.apply_chat_template(msgs, **kw)
        except Exception:
            flat = []
            for m in msgs:
                if m["role"] == "tool":
                    flat.append({"role": "user", "content": "TOOL OUTPUT\n" + m["content"]})
                else:
                    flat.append(m)
            enc = tok.apply_chat_template(flat, **kw)
        ids = enc["input_ids"] if hasattr(enc, "keys") else enc
        return list(ids[0]) if ids and isinstance(ids[0], (list, tuple)) else list(ids)

    def raw_ids(text):
        return tok(text, add_special_tokens=False)["input_ids"]

    def tp(ids):
        return {"prompt_token_ids": list(ids)}

    llm = LLM(
        model=args.model,
        tensor_parallel_size=args.tp,
        gpu_memory_utilization=args.gpu_frac,
        max_model_len=args.max_model_len,
        dtype="bfloat16",
        max_logprobs=40,
        disable_log_stats=True,
        enforce_eager=args.enforce_eager,
        **({"max_num_seqs": args.max_num_seqs} if args.max_num_seqs else {}),
    )

    # ------------------------------------------------------------------
    # Stage A: short semantic resolver pass for ReGround-Self.
    # One call per item x {same-D7, same-D9, wrong-D7}.
    # ------------------------------------------------------------------
    sel_rows = []
    for it in items:
        for variant in VARIANTS:
            msgs = [
                {
                    "role": "system",
                    "content": (
                        "You are a trusted policy resolver. Match propositions by "
                        "meaning. Follow the output format exactly."
                    ),
                },
                {"role": "user", "content": selector_prompt(it, variant)},
            ]
            ids = chat_ids(msgs)
            sel_rows.append(
                dict(
                    item_id=it.item_id,
                    variant=variant,
                    ids=ids,
                    expected=sorted(gold_selection(variant)),
                )
            )

    t0 = time.perf_counter()
    sel_outs = llm.generate(
        [tp(r["ids"]) for r in sel_rows],
        SamplingParams(temperature=0.0, max_tokens=8),
    )
    selector_seconds = time.perf_counter() - t0

    selections = {}
    for r, o in zip(sel_rows, sel_outs):
        raw = o.outputs[0].text
        pred = sorted(parse_selection(raw))
        selections[(r["item_id"], r["variant"])] = pred
        r["raw"] = raw
        r["pred"] = pred
        r["correct"] = pred == r["expected"]
        r["n_prompt_tokens"] = len(r["ids"])

    # ------------------------------------------------------------------
    # Stage B: decision prompts.
    # ------------------------------------------------------------------
    recs = []
    ans_fmt = ANSWER_FORMATS[args.mode]

    for it in items:
        msgs = decision_messages(
            it, "base", None, SYSTEM, ans_fmt
        )
        recs.append(
            dict(
                item_id=it.item_id,
                task_family=it.task_family,
                method="base",
                variant="base",
                kind_name="rg_base",
                ids=chat_ids(msgs),
            )
        )

        for variant in VARIANTS:
            for method in METHODS:
                pred = None
                if method == "self":
                    pred = selections[(it.item_id, variant)]
                msgs = decision_messages(
                    it, method, variant, SYSTEM, ans_fmt, selection=pred
                )
                row = dict(
                    item_id=it.item_id,
                    task_family=it.task_family,
                    method=method,
                    variant=variant,
                    kind_name=f"rg_{method}_{variant}",
                    ids=chat_ids(msgs),
                )
                if method == "self":
                    sr = next(
                        x for x in sel_rows
                        if x["item_id"] == it.item_id and x["variant"] == variant
                    )
                    row["selector_raw"] = sr["raw"]
                    row["selector_pred"] = sr["pred"]
                    row["selector_expected"] = sr["expected"]
                    row["selector_correct"] = sr["correct"]
                    row["selector_prompt_tokens"] = sr["n_prompt_tokens"]
                    row["resolver_batch_seconds"] = selector_seconds
                    row["resolver_batch_n"] = len(sel_rows)
                recs.append(row)

            if variant in ("same_d7", "same_d9"):
                msgs = decision_messages(
                    it, "sanitize", variant, SYSTEM, ans_fmt
                )
                recs.append(
                    dict(
                        item_id=it.item_id,
                        task_family=it.task_family,
                        method="sanitize",
                        variant=variant,
                        kind_name=f"rg_sanitize_{variant}",
                        ids=chat_ids(msgs),
                    )
                )

    # Primary reasoned readout: short greedy rationale, then one-token digit
    # expectation at a fixed answer position.
    if args.mode == "reasoned":
        outs = llm.generate(
            [tp(r["ids"]) for r in recs],
            SamplingParams(
                temperature=0.0,
                max_tokens=args.reason_tokens,
                stop=[ANSWER_CUE],
            ),
        )
        for r, o in zip(recs, outs):
            r["reasoning"] = o.outputs[0].text
            r["reason_truncated"] = o.outputs[0].finish_reason != "stop"
            cue = o.outputs[0].text.rstrip() + "\n" + ANSWER_CUE + " "
            r["ids2"] = r["ids"] + raw_ids(cue)
    else:
        cue = raw_ids(ANSWER_CUE + " ") if args.mode == "cued" else []
        for r in recs:
            r["reasoning"] = ""
            r["reason_truncated"] = False
            r["ids2"] = r["ids"] + cue

    outs2 = llm.generate(
        [tp(r["ids2"]) for r in recs],
        SamplingParams(temperature=0.0, max_tokens=1, logprobs=40),
    )
    for r, o in zip(recs, outs2):
        r["raw"] = o.outputs[0].text
        r["value"], r["mass"] = digit_expectation(o)
        r["readout"] = "digit_expectation_0_100"
        r["n_prompt_tokens"] = len(r["ids"])
        r.pop("ids")
        r.pop("ids2")
        r["model_tag"] = args.tag

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    bad = sum(r["value"] is None for r in recs)
    lowmass = sum(r.get("mass", 1.0) < 0.5 for r in recs)
    acc = sum(r["correct"] for r in sel_rows) / max(1, len(sel_rows))
    print(f"wrote {len(recs)} decisions -> {args.out}")
    print(
        f"resolver: {len(sel_rows)} calls, exact-set accuracy {acc:.3f}, "
        f"batch wall time {selector_seconds:.1f}s"
    )
    print(f"decisions: unparsed {bad}, digit-mass<0.5 {lowmass}")


if __name__ == "__main__":
    main()
