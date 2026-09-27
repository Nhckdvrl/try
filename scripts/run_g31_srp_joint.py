"""G31 registered crossed-X/E2 selective evidence control pilot: one model/GPU."""

import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ITEMS = ROOT / "data/items/g31_selected_v1.jsonl"
SYSTEM = "You are a careful fact-checker. Apply the stated evidence eligibility rules exactly. Give the requested answer only."
PROB_TASK = (
    "Considering only currently admissible information, what is the probability "
    "from 0 to 100 percent that the CLAIM is true? Reply with exactly one line: "
    "PROBABILITY: <number from 0 to 100>."
)
BINARY_TASK = (
    "Considering only currently admissible information, is the CLAIM true or false? "
    "Reply with exactly one line: ANSWER: TRUE or ANSWER: FALSE."
)
P_RE = re.compile(r"^\s*PROBABILITY\s*:\s*(\d+(?:\.\d+)?)\s*%?\s*\.?\s*$", re.I | re.M)
B_RE = re.compile(r"^\s*ANSWER\s*:\s*(TRUE|FALSE)\s*\.?\s*$", re.I | re.M)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def make_messages(item, condition, x_role, e_role, mode):
    claim = item["claim"]
    e2 = item["evidence_s"] if e_role == "support" else item["evidence_r"]
    task = PROB_TASK if mode == "probability" else BINARY_TASK
    if condition == "D":
        return [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": f"CLAIM\n{claim}\n\nCURRENT SOURCE EVIDENCE E2\n{e2}\n\n{task}"},
        ]
    x = item[{"support": "x_s", "refute": "x_r", "irrelevant": "x_i"}[x_role]]
    initial = (
        "This temporary case note is currently admissible for judging the claim."
        if condition == "A" else
        "This temporary case note is excluded from the moment it is shown and is not admissible for judging the claim."
    )
    final = (
        "The temporary case note remains admissible. Current source evidence E2 is also admissible. Use both."
        if condition == "A" else
        "The temporary case note remains excluded and must have zero influence on your judgment. "
        "Current source evidence E2 is the only admissible additional evidence."
    )
    return [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": f"CLAIM\n{claim}\n\nTEMPORARY CASE NOTE X\n{x}\n\n{initial}\n\nPlease read this information. I will ask for a judgment in the next turn."},
        {"role": "assistant", "content": "Understood."},
        {"role": "user", "content": f"UPDATE\n{final}\n\nCURRENT SOURCE EVIDENCE E2\n{e2}\n\n{task}"},
    ]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--tag", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--limit", type=int)
    ap.add_argument("--gpu-frac", type=float, default=.85)
    ap.add_argument("--tp", type=int, default=1)
    args = ap.parse_args()
    raw = ITEMS.read_bytes()
    items = [json.loads(s) for s in raw.splitlines() if s]
    assert items and len(items) == len({x["id"] for x in items})
    if args.limit:
        items = items[:args.limit]

    from transformers import AutoTokenizer
    from vllm import LLM, SamplingParams

    tok = AutoTokenizer.from_pretrained(args.model)
    prompts, rows = [], []
    for item in items:
        for e_role in ("support", "refute"):
            for condition, x_roles in (
                ("D", ("none",)), ("I", ("irrelevant",)),
                ("N", ("support", "refute")), ("A", ("support", "refute")),
            ):
                for x_role in x_roles:
                    for mode in ("probability", "binary"):
                        msg = make_messages(item, condition, x_role, e_role, mode)
                        kw = {"tokenize": True, "add_generation_prompt": True}
                        try:
                            ids = tok.apply_chat_template(msg, enable_thinking=False, **kw)
                        except TypeError:
                            ids = tok.apply_chat_template(msg, **kw)
                        if hasattr(ids, "keys"):
                            ids = ids["input_ids"]
                        if ids and isinstance(ids[0], (list, tuple)):
                            ids = ids[0]
                        prompts.append({"prompt_token_ids": list(ids)})
                        rows.append({
                            "id": item["id"], "model_tag": args.tag, "e2_role": e_role,
                            "condition": condition, "x_role": x_role, "mode": mode,
                            "items_sha256": sha(raw), "prompt_sha256": sha(json.dumps(msg, sort_keys=True, ensure_ascii=False).encode()),
                            "messages": msg,
                        })
    llm = LLM(model=args.model, tensor_parallel_size=args.tp, gpu_memory_utilization=args.gpu_frac,
              max_model_len=4096, dtype="bfloat16", disable_log_stats=True, enforce_eager=True)
    outputs = llm.generate(prompts, SamplingParams(temperature=0, max_tokens=24), use_tqdm=False)
    assert len(outputs) == len(rows)
    for row, result in zip(rows, outputs):
        out = result.outputs[0]
        row["raw"] = out.text
        row["finish_reason"] = out.finish_reason
        if row["mode"] == "probability":
            match = P_RE.search(out.text)
            value = float(match.group(1)) if match else None
            row["value"] = value if value is not None and 0 <= value <= 100 else None
        else:
            match = B_RE.search(out.text)
            row["choice"] = match.group(1).upper() if match else None
    path = Path(args.out)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows))
    print(f"wrote {len(rows)} rows; probability parse failures="
          f"{sum(r['value'] is None for r in rows if r['mode']=='probability')}; "
          f"binary parse failures={sum(r['choice'] is None for r in rows if r['mode']=='binary')}")


if __name__ == "__main__":
    main()
