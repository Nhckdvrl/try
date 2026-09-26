"""Run frozen G29 revocation-status paths on one model/GPU."""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "src"), str(ROOT / "scripts")]
from run_model import digit_expectation
from schema import ANSWER_CUE, SYSTEM

BINARY_TASK = ("TASK\nConsidering only admissible evidence, is the claim true or false? "
               "Give exactly one line: ANSWER: TRUE or ANSWER: FALSE. Do not give a rationale.")
RATING_TASK = ("TASK\nConsidering only admissible evidence, rate the likelihood that the claim is true. "
               "Use a scale from 0 to 9, where 0 means certainly false and 9 means certainly true. "
               "Think in at most two short sentences. Then write a final line of exactly this form:\nANSWER: <your answer>")


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def messages(claim, e1, e2, condition, task):
    if condition == "D":
        return [{"role": "user", "content": f"CLAIM\n{claim}\n\nEVIDENCE E2\n{e2}\n\n{task}"}]
    first_status = {
        "R": "Evidence E1 is currently admissible for judging the claim.",
        "N": "Evidence E1 is excluded from the moment it is shown; it is not admissible for judging the claim.",
        "A": "Evidence E1 is currently admissible for judging the claim.",
    }[condition]
    last_status = {
        "R": "Evidence E1 has now been withdrawn. It is not admissible and must have zero influence on your final judgment. Evidence E2 is the only admissible additional evidence.",
        "N": "Evidence E1 remains excluded. It is not admissible and must have zero influence on your final judgment. Evidence E2 is the only admissible additional evidence.",
        "A": "Evidence E1 remains admissible. Evidence E2 is also admissible additional evidence. Consider both when judging the claim.",
    }[condition]
    return [
        {"role": "user", "content": f"CLAIM\n{claim}\n\nEVIDENCE E1\n{e1}\n\n{first_status}\n\nPlease read this information. I will ask for a judgment in the next turn."},
        {"role": "assistant", "content": "Understood."},
        {"role": "user", "content": f"UPDATE\n{last_status}\n\nEVIDENCE E2\n{e2}\n\n{task}"},
    ]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--tag", required=True)
    ap.add_argument("--items", default=str(ROOT / "data/items/g29_selected_v1.jsonl"))
    ap.add_argument("--out", required=True)
    ap.add_argument("--limit", type=int)
    ap.add_argument("--gpu-frac", type=float, default=.85)
    args = ap.parse_args()
    pairs = [json.loads(s) for s in Path(args.items).read_text().splitlines() if s]
    assert len(pairs) == len({p["id"] for p in pairs}) and pairs
    if args.limit:
        pairs = pairs[:args.limit]

    from transformers import AutoTokenizer
    from vllm import LLM, SamplingParams
    tok = AutoTokenizer.from_pretrained(args.model)

    def chat_ids(msg):
        full = [{"role": "system", "content": SYSTEM}] + msg
        kw = dict(tokenize=True, add_generation_prompt=True)
        try:
            enc = tok.apply_chat_template(full, enable_thinking=False, **kw)
        except TypeError:
            enc = tok.apply_chat_template(full, **kw)
        ids = enc["input_ids"] if hasattr(enc, "keys") else enc
        return list(ids[0]) if ids and isinstance(ids[0], (list, tuple)) else list(ids)

    rows = []
    for p in pairs:
        for final_role, e2, e1 in (("support", p["evidence_s"], p["evidence_r"]),
                                    ("refute", p["evidence_r"], p["evidence_s"])):
            for condition in ("R", "N", "A", "D"):
                for mode, task in (("binary", BINARY_TASK), ("rating", RATING_TASK)):
                    msg = messages(p["claim"], e1, e2, condition, task)
                    rows.append(dict(id=p["id"], model_tag=args.tag, final_role=final_role,
                                     condition=condition, mode=mode, messages=msg,
                                     prompt_sha256=digest(msg), ids=chat_ids(msg)))

    llm = LLM(model=args.model, tensor_parallel_size=1,
              gpu_memory_utilization=args.gpu_frac, max_model_len=4096,
              dtype="bfloat16", max_logprobs=40, disable_log_stats=True,
              enforce_eager=True)
    binary = [r for r in rows if r["mode"] == "binary"]
    rating = [r for r in rows if r["mode"] == "rating"]
    outs = llm.generate([{"prompt_token_ids": r["ids"]} for r in binary],
                        SamplingParams(temperature=0, max_tokens=16), use_tqdm=False)
    for r, o in zip(binary, outs):
        r["raw"] = o.outputs[0].text
        match = re.search(r"ANSWER\s*:\s*(TRUE|FALSE)\b", r["raw"], re.I)
        r["choice"] = match.group(1).upper() if match else None
        r["finish_reason"] = o.outputs[0].finish_reason
        del r["ids"]

    out1 = llm.generate([{"prompt_token_ids": r["ids"]} for r in rating],
                        SamplingParams(temperature=0, max_tokens=110, stop=[ANSWER_CUE]),
                        use_tqdm=False)
    for r, o in zip(rating, out1):
        r["reasoning"] = o.outputs[0].text
        r["reason_truncated"] = o.outputs[0].finish_reason != "stop"
        cue = r["reasoning"].rstrip() + "\n" + ANSWER_CUE + " "
        r["ids2"] = r["ids"] + tok(cue, add_special_tokens=False)["input_ids"]
    out2 = llm.generate([{"prompt_token_ids": r["ids2"]} for r in rating],
                        SamplingParams(temperature=0, max_tokens=1, logprobs=40),
                        use_tqdm=False)
    for r, o in zip(rating, out2):
        r["raw"] = o.outputs[0].text
        r["value"], r["mass"] = digit_expectation(o)
        del r["ids"], r["ids2"]
    path = Path(args.out)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    print(f"wrote {len(rows)} rows to {path}; binary unparsed={sum(r['choice'] is None for r in binary)}; "
          f"rating unparsed={sum(r['value'] is None for r in rating)}; "
          f"rating mass<.5={sum(r['mass'] < .5 for r in rating)}; "
          f"rationale caps={sum(r['reason_truncated'] for r in rating)}")


if __name__ == "__main__":
    main()
