"""Does the fixed-position (no rationale) readout track the behavioural one?

Mechanism claims are only meaningful for families where it does.
"""
import os, sys, json, argparse
import torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import load_model, mech_prompt, digit_ids, digit_expectation, frozen_items, ROOT

CONDS = ["base", "admit_pre", "admit_post", "exclude_pre", "exclude_post"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="Qwen/Qwen3-8B")
    ap.add_argument("--tag", default="qwen3-8b")
    ap.add_argument("--out", default=os.path.join(ROOT, "results", "mech", "direct_readout.json"))
    args = ap.parse_args()

    tok, m = load_model(args.model)
    dids = digit_ids(tok).to(m.device)
    items = [i for i in frozen_items() if i.task_family != "numeric_aggregation"]
    rows = []
    with torch.no_grad():
        for n, it in enumerate(items):
            rec = dict(item_id=it.item_id, task_family=it.task_family,
                       direction=it.critical_direction)
            for c in CONDS:
                p = mech_prompt(tok, it, c)
                ids = tok(p, return_tensors="pt", add_special_tokens=False).to(m.device)
                out = m(**ids)
                rec[c] = float(digit_expectation(out.logits[0, -1], dids))
            rows.append(rec)
            if (n + 1) % 25 == 0:
                print(f"  {n+1}/{len(items)}", flush=True)
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    json.dump(rows, open(args.out, "w"), indent=1)
    print(f"wrote {len(rows)} -> {args.out}")


if __name__ == "__main__":
    main()
