"""G30 frozen diagnostic-signal pilot: one model per GPU."""

import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ITEMS = ROOT / "data/items/g30_bayesian_status_pilot_v1.jsonl"
SYSTEM = "You are a careful forecaster. Follow the information-status rules exactly. Give the requested answer only."
OUTPUT = "\n\nUse exactly two lines for your final response:\nPROBABILITY: <number from 0 to 100>\nCHOICE: BLUE or YELLOW"
P_RE = re.compile(r"^\s*PROBABILITY\s*:\s*(\d+(?:\.\d+)?)\s*%?\s*$", re.I | re.M)
C_RE = re.compile(r"^\s*CHOICE\s*:\s*(BLUE|YELLOW)\s*$", re.I | re.M)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--tag", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--limit", type=int)
    ap.add_argument("--gpu-frac", type=float, default=0.85)
    args = ap.parse_args()
    raw = ITEMS.read_bytes()
    items = [json.loads(x) for x in raw.splitlines() if x]
    assert len(items) == 40 and len({r["id"] for r in items}) == 40
    if args.limit:
        items = items[: args.limit]
    from transformers import AutoTokenizer
    from vllm import LLM, SamplingParams

    tokenizer = AutoTokenizer.from_pretrained(args.model)
    rows = []
    prompts = []
    for item in items:
        for condition in ("D", "N", "I", "R"):
            stimulus = item[f"stimulus_{condition}"] + OUTPUT
            messages = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": stimulus}]
            kw = {"tokenize": True, "add_generation_prompt": True}
            try:
                ids = tokenizer.apply_chat_template(messages, enable_thinking=False, **kw)
            except TypeError:
                ids = tokenizer.apply_chat_template(messages, **kw)
            if hasattr(ids, "keys"):
                ids = ids["input_ids"]
            if ids and isinstance(ids[0], (list, tuple)):
                ids = ids[0]
            prompts.append({"prompt_token_ids": list(ids)})
            rows.append({
                "id": item["id"], "model_tag": args.tag, "condition": condition,
                "prior_blue": item["prior_blue"], "reliability": item["reliability"],
                "e1_report": item["e1_report"], "e2_report": item["e2_report"],
                "bayes_p_blue_after_e2_pct": item["bayes_p_blue_after_e2_pct"],
                "items_sha256": sha(raw), "prompt_sha256": sha(json.dumps(messages, sort_keys=True).encode()),
                "messages": messages,
            })
    llm = LLM(model=args.model, tensor_parallel_size=1, gpu_memory_utilization=args.gpu_frac,
              max_model_len=4096, dtype="bfloat16", disable_log_stats=True, enforce_eager=True)
    outputs = llm.generate(prompts, SamplingParams(temperature=0, max_tokens=80), use_tqdm=False)
    assert len(outputs) == len(rows)
    for row, result in zip(rows, outputs):
        out = result.outputs[0]
        row["raw"] = out.text
        row["finish_reason"] = out.finish_reason
        pm = P_RE.search(out.text)
        cm = C_RE.search(out.text)
        p = float(pm.group(1)) if pm else None
        row["probability_blue"] = p if p is not None and 0 <= p <= 100 else None
        row["choice"] = cm.group(1).upper() if cm else None
    path = Path(args.out)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    print(f"wrote {len(rows)} rows; probability parse failures="
          f"{sum(r['probability_blue'] is None for r in rows)}; choice parse failures="
          f"{sum(r['choice'] is None for r in rows)}")


if __name__ == "__main__":
    main()
