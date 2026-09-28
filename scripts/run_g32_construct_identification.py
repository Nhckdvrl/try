"""Frozen G32 prompt compiler and deterministic, one-model inference runner.

Seven identification cells plus two active-X material-calibration cells per
contract and legal-E polarity. No old model outputs enter item selection.
"""

import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ITEMS = ROOT / "data/items/g32_selected_v1.jsonl"
CONTRACTS = {
    "open_world": (
        "Judge whether the CLAIM is true. Use the ADMISSIBLE RECORD and any "
        "background knowledge you already have."
    ),
    "record_only": (
        "Judge whether the CLAIM is true using only the ADMISSIBLE RECORD. "
        "Do not supplement the record with background knowledge, remembered "
        "facts, or assumptions about the subject."
    ),
}
DIRECT = (
    "Give your judgment now. Reply with exactly one line: "
    "PROBABILITY: <number from 0 to 100>."
)
SIM = (
    "Imagine a fresh instance of this same model, under the same task rule, "
    "that was given only the CLAIM and the ADMISSIBLE RECORD above and never "
    "encountered the temporary note X or any message about it. Predict the "
    "probability that instance would report. Reply with exactly one line: "
    "PROBABILITY: <number from 0 to 100>."
)
CELLS = ("B", "F_D", "F_S", "D+", "D-", "S+", "S-", "A+", "A-")
P_RE = re.compile(r"^\s*PROBABILITY\s*:\s*(\d+(?:\.\d+)?)\s*%?\s*\.?\s*$", re.I)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def make_messages(item, contract, e_role, cell):
    if contract not in CONTRACTS or cell not in CELLS:
        raise ValueError((contract, cell))
    e = item["evidence_s" if e_role == "support" else "evidence_r"]
    pieces = ["TASK RULE\n" + CONTRACTS[contract], "CLAIM\n" + item["claim"],
              "ADMISSIBLE RECORD E\n" + e]
    if cell != "B":
        x = "[REDACTED]" if cell.startswith("F_") else item["x_s" if cell.endswith("+") else "x_r"]
        status = (
            "The temporary note is admissible along with record E."
            if cell.startswith("A") else
            "The temporary note is EXCLUDED from the moment it is displayed. "
            "Do not use its contents as a ground for judging the claim."
        )
        pieces.extend(("TEMPORARY NOTE X\n" + x, "STATUS OF NOTE X\n" + status))
    pieces.append("QUESTION\n" + (SIM if cell in ("F_S", "S+", "S-") else DIRECT))
    return [
        {"role": "system", "content": "Follow the task rule. Return only the requested probability."},
        {"role": "user", "content": "\n\n".join(pieces)},
    ]


def cases(items, item_bytes):
    for item in items:
        for contract in CONTRACTS:
            for e_role in ("support", "refute"):
                for cell in CELLS:
                    msg = make_messages(item, contract, e_role, cell)
                    yield {"id": item["id"], "contract": contract, "e_role": e_role,
                           "cell": cell, "items_sha256": digest(item_bytes),
                           "prompt_sha256": digest(json.dumps(msg, ensure_ascii=False, sort_keys=True).encode()),
                           "messages": msg}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--tag", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--limit", type=int)
    ap.add_argument("--tp", type=int, default=1)
    ap.add_argument("--gpu-frac", type=float, default=.85)
    args = ap.parse_args()
    raw = ITEMS.read_bytes()
    items = [json.loads(s) for s in raw.splitlines() if s]
    if args.limit:
        items = items[:args.limit]
    assert len(items) == len({x["id"] for x in items})
    rows = list(cases(items, raw))

    from transformers import AutoTokenizer
    from vllm import LLM, SamplingParams
    tok_kwargs = {"fix_mistral_regex": True} if args.tag == "mistral-small-24b" else {}
    tok = AutoTokenizer.from_pretrained(args.model, **tok_kwargs)
    prompts = []
    for row in rows:
        kw = {"tokenize": True, "add_generation_prompt": True}
        try:
            ids = tok.apply_chat_template(row["messages"], enable_thinking=False, **kw)
        except TypeError:
            ids = tok.apply_chat_template(row["messages"], **kw)
        if isinstance(ids, dict):
            ids = ids["input_ids"]
        if ids and isinstance(ids[0], (list, tuple)):
            ids = ids[0]
        prompts.append({"prompt_token_ids": list(ids)})
    llm = LLM(model=args.model, tensor_parallel_size=args.tp,
              gpu_memory_utilization=args.gpu_frac, max_model_len=4096,
              dtype="bfloat16", disable_log_stats=True, enforce_eager=True)
    outs = llm.generate(prompts, SamplingParams(temperature=0, max_tokens=24), use_tqdm=False)
    for row, result in zip(rows, outs):
        out = result.outputs[0]
        row["model_tag"] = args.tag
        row["raw"] = out.text
        row["finish_reason"] = out.finish_reason
        m = P_RE.fullmatch(out.text)
        val = float(m.group(1)) if m else None
        row["value"] = val if val is not None and 0 <= val <= 100 else None
    path = Path(args.out)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    print(f"wrote {len(rows)} rows; parse failures={sum(r['value'] is None for r in rows)}")


if __name__ == "__main__":
    main()
