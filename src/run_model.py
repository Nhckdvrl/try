"""Run one model over a set of conditions with vLLM.

Readout
-------
The four rating families ask for a single digit 0-9.  We do not take the greedy
digit: we take one forward pass, read the next-token distribution, renormalise
it over the ten digit tokens and report the expectation, rescaled to 0-100.
A pilot with greedy integers on a 0-100 scale produced a handful of round values
(20/45/65/85) plus occasional flips, which is far too coarse for a residual-
influence ratio.  The expectation is deterministic, continuous, and needs no
parsing.

The numeric-aggregation family has an open-ended answer, so it keeps a greedy
decode with a strict numeric parse.  No LLM judge is used anywhere.
"""
import argparse, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
FORCED_LINE = "ITEM DECISION WEIGHT: 0%\nFINAL DECISION: "

from schema import (load_items, compile_prompt, compile_probe, SYSTEM, CONDITIONS,
                    EXTRA_CONDITIONS, V2_CONDITIONS, V3_CONDITIONS, V4_CONDITIONS, V5_CONDITIONS, ROUTING_CONDITIONS, LINEAR_CONDITIONS, V6_CONDITIONS, V7_CONDITIONS, G17_CONDITIONS, AGENT_CONDITIONS, EXT_CONDITIONS, PROBES,
                    compile_messages,
                    ANSWER_CUE,
                    rule_char_offset)

ROOT = os.path.join(os.path.dirname(__file__), "..")
ITEMS = os.path.join(ROOT, "data", "items", "items_v1.jsonl")
DIGITS = [str(d) for d in range(10)]


def parse_number(text):
    m = re.search(r"-?\d+(?:\.\d+)?", text.replace(",", ""))
    return float(m.group()) if m else None


def _dist(out):
    """{decoded_token: prob} for the first generated position."""
    import math
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


def yes_probability(out):
    d = _dist(out)
    y = n = 0.0
    for tokstr, prob in d.items():
        t = (tokstr or "").strip().upper()
        if t in ("YES", "Y"):
            y += prob
        elif t in ("NO", "N"):
            n += prob
    mass = y + n
    if mass <= 0:
        return None, 0.0
    return y / mass, mass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--tag", required=True)
    ap.add_argument("--kinds", required=True)
    ap.add_argument("--items", default=ITEMS)
    ap.add_argument("--only-ids", default=None)
    ap.add_argument("--out", required=True)
    ap.add_argument("--tp", type=int, default=1)
    ap.add_argument("--gpu-frac", type=float, default=0.85)
    # hybrid Mamba models allocate one recurrent-state block per decode sequence,
    # so the default scheduler width can exceed what fits
    ap.add_argument("--max-num-seqs", type=int, default=0)
    ap.add_argument("--enforce-eager", action="store_true",
                    help="skip CUDA graph capture (saves memory on large hybrid models)")
    ap.add_argument("--max-model-len", type=int, default=2048)
    ap.add_argument("--mode", default="reasoned", choices=["reasoned", "direct", "cued"])
    ap.add_argument("--reason-tokens", type=int, default=110)
    ap.add_argument("--samples", type=int, default=16)
    ap.add_argument("--temperature", type=float, default=0.8)
    args = ap.parse_args()

    items = load_items(args.items)
    if args.only_ids:
        keep = set(json.load(open(args.only_ids)))
        items = [i for i in items if i.item_id in keep]
    kinds = args.kinds.split(",")

    from transformers import AutoTokenizer
    from vllm import LLM, SamplingParams
    tok = AutoTokenizer.from_pretrained(args.model)

    # Prompts are carried as token ids, not text: several chat templates emit their
    # own BOS, and passing the rendered string to vLLM would add a second one.
    def chat_ids(user, msgs=None):
        kw = dict(tokenize=True, add_generation_prompt=True)
        if msgs is None:
            msgs = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}]
        try:
            enc = tok.apply_chat_template(msgs, enable_thinking=False, **kw)
        except TypeError:
            enc = tok.apply_chat_template(msgs, **kw)
        except Exception:
            # some templates reject a `tool` role; fold it into a user turn
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

    recs = []
    for it in items:
        digit_scale = it.task_family not in ("numeric_aggregation", "selective_routing",
                                             "linear_weighting", "ext_ramsey")
        for k in kinds:
            if k in AGENT_CONDITIONS:
                kind = "digit" if digit_scale else "openreal"
                rec = dict(item_id=it.item_id, task_family=it.task_family, kind_name=k,
                           kind=kind,
                           ids=chat_ids(None, compile_messages(it, k, mode=args.mode)))
                recs.append(rec)
                continue
            if k in CONDITIONS or k in EXTRA_CONDITIONS or k in V2_CONDITIONS \
                    or k in V3_CONDITIONS or k in V4_CONDITIONS \
                    or k in ROUTING_CONDITIONS or k in V5_CONDITIONS \
                    or k in LINEAR_CONDITIONS or k in V6_CONDITIONS \
                    or k in V7_CONDITIONS or k in G17_CONDITIONS or k in EXT_CONDITIONS:
                user = compile_prompt(it, k, mode=args.mode)
                kind = "digit" if digit_scale else "openreal"
                if k.startswith("sc_b"):
                    kind = "twoline_gen"       # model writes the weight, then decides
                elif k.startswith("sc_c"):
                    kind = "twoline_forced"    # weight is teacher-forced to 0%
                elif k.startswith("op_"):
                    kind = "onpolicy"          # sampled; condition on what it says
            elif k in PROBES:
                user = compile_probe(it, k)
                kind = ("memory" if k.startswith("memory")
                        else "wprobe" if k.startswith("wprobe") else "rule")
            else:
                raise SystemExit(f"unknown kind {k}")
            rec = dict(item_id=it.item_id, task_family=it.task_family, kind_name=k,
                       kind=kind, ids=chat_ids(user))
            if kind in ("digit", "openreal"):
                off = rule_char_offset(it, k, mode=args.mode)
                # tokens from the start of the RULING block to the answer position
                rec["rule_to_answer_tokens"] = None if off is None else len(raw_ids(user[off:]))
            recs.append(rec)

    llm = LLM(model=args.model, tensor_parallel_size=args.tp,
              gpu_memory_utilization=args.gpu_frac, max_model_len=args.max_model_len,
              dtype="bfloat16", max_logprobs=40, disable_log_stats=True,
              enforce_eager=args.enforce_eager,
              **({"max_num_seqs": args.max_num_seqs} if args.max_num_seqs else {}))

    dec_kinds = ("digit", "openreal", "twoline_gen", "twoline_forced", "onpolicy")
    dec = [r for r in recs if r["kind"] in dec_kinds]
    if dec:
        forced = [r for r in dec if r["kind"] == "twoline_forced"]
        for r in forced:
            r["reasoning"], r["reason_truncated"] = "", False
            r["stated_weight"] = 0.0
            r["ids2"] = r["ids"] + raw_ids(FORCED_LINE)

        two = [r for r in dec if r["kind"] == "twoline_gen"]
        if two:
            outs = llm.generate([tp(r["ids"]) for r in two],
                                SamplingParams(temperature=0.0, max_tokens=24,
                                               stop=["FINAL DECISION:"]))
            for r, o in zip(two, outs):
                r["reasoning"] = o.outputs[0].text
                r["reason_truncated"] = o.outputs[0].finish_reason != "stop"
                r["stated_weight"] = parse_number(o.outputs[0].text)
                r["ids2"] = r["ids"] + raw_ids(o.outputs[0].text.rstrip()
                                               + "\nFINAL DECISION: ")

        op = [r for r in dec if r["kind"] == "onpolicy"]
        if op:
            outs = llm.generate([tp(r["ids"]) for r in op],
                                SamplingParams(n=args.samples, temperature=args.temperature,
                                               top_p=0.95, seed=0, max_tokens=24,
                                               stop=["FINAL DECISION:"]))
            flat = []
            for r, o in zip(op, outs):
                r["samples"] = []
                for c in o.outputs:
                    rec = dict(stated_weight=parse_number(c.text), text=c.text)
                    r["samples"].append(rec)
                    flat.append((r, rec, r["ids"] + raw_ids(c.text.rstrip()
                                                            + "\nFINAL DECISION: ")))
            outs2 = llm.generate([tp(i) for _, _, i in flat],
                                 SamplingParams(temperature=0.0, max_tokens=1, logprobs=40))
            for (r, rec, _), o in zip(flat, outs2):
                rec["value"], rec["mass"] = digit_expectation(o)
            for r in op:
                r["readout"] = "onpolicy_samples"
                r["value"] = None
                r["ids2"] = r["ids"]

        rest = [r for r in dec if r["kind"] in ("digit", "openreal")]
        if args.mode == "reasoned":
            # Stage 1: greedy rationale, stopped at the answer cue.
            sp1 = SamplingParams(temperature=0.0, max_tokens=args.reason_tokens,
                                 stop=[ANSWER_CUE])
            outs = llm.generate([tp(r["ids"]) for r in rest], sp1)
            for r, o in zip(rest, outs):
                r["reasoning"] = o.outputs[0].text
                r["reason_truncated"] = o.outputs[0].finish_reason != "stop"
                # trailing space: without it the next token is a bare space, not a digit
                cue = o.outputs[0].text.rstrip() + "\n" + ANSWER_CUE + " "
                r["ids2"] = r["ids"] + raw_ids(cue)
        else:
            cue = raw_ids(ANSWER_CUE + " ") if args.mode == "cued" else []
            for r in rest:
                r["reasoning"], r["reason_truncated"] = "", False
                r["ids2"] = r["ids"] + cue

        # Stage 2: read the answer at a fixed position.
        dig = [r for r in dec if r["kind"] in ("digit", "twoline_gen", "twoline_forced")]
        if dig:
            outs = llm.generate([tp(r["ids2"]) for r in dig],
                                SamplingParams(temperature=0.0, max_tokens=1, logprobs=40))
            for r, o in zip(dig, outs):
                r["raw"] = o.outputs[0].text
                r["value"], r["mass"] = digit_expectation(o)
                r["readout"] = "digit_expectation_0_100"
        opn = [r for r in dec if r["kind"] == "openreal"]
        if opn:
            outs = llm.generate([tp(r["ids2"]) for r in opn],
                                SamplingParams(temperature=0.0, max_tokens=12))
            for r, o in zip(opn, outs):
                r["raw"] = o.outputs[0].text
                r["value"], r["mass"] = parse_number(r["raw"]), 1.0
                r["readout"] = "greedy_number"

    rul = [r for r in recs if r["kind"] == "rule"]
    if rul:
        outs = llm.generate([tp(r["ids"]) for r in rul],
                            SamplingParams(temperature=0.0, max_tokens=1, logprobs=40))
        for r, o in zip(rul, outs):
            r["raw"] = o.outputs[0].text
            r["p_yes"], r["mass"] = yes_probability(o)
            r["yesno"] = None if r["p_yes"] is None else ("YES" if r["p_yes"] >= 0.5 else "NO")
            r["readout"] = "yes_probability"

    wp = [r for r in recs if r["kind"] == "wprobe"]
    if wp:
        # declarative policy state: greedy short answer, strict numeric parse
        outs = llm.generate([tp(r["ids"]) for r in wp],
                            SamplingParams(temperature=0.0, max_tokens=8))
        for r, o in zip(wp, outs):
            r["raw"] = o.outputs[0].text
            r["value"] = parse_number(r["raw"])
            r["readout"] = "greedy_number_percent"

    mem = [r for r in recs if r["kind"] == "memory"]
    if mem:
        outs = llm.generate([tp(r["ids"]) for r in mem],
                            SamplingParams(temperature=0.0, max_tokens=48))
        for r, o in zip(mem, outs):
            r["raw"] = o.outputs[0].text
            r["readout"] = "greedy_text"

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as f:
        for r in recs:
            r["n_prompt_tokens"] = len(r.pop("ids"))
            r.pop("ids2", None)
            r["model_tag"] = args.tag
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    bad = sum(1 for r in dec if r["value"] is None)
    lowmass = sum(1 for r in dec if r["kind"] == "digit" and r.get("mass", 1) < 0.5)
    print(f"wrote {len(recs)} rows -> {args.out}")
    trunc = sum(1 for r in dec if r.get("reason_truncated"))
    print(f"  decisions {len(dec)} (unparsed {bad}, digit-mass<0.5 {lowmass}, "
          f"rationale hit token cap {trunc})")
    if rul:
        m = sum(r["mass"] for r in rul) / len(rul)
        print(f"  rule probes {len(rul)} (mean YES/NO mass {m:.3f})")


if __name__ == "__main__":
    main()
