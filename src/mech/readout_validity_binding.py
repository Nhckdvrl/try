"""Is the mechanism readout valid for the binding contrast?

Every mechanism result in this project (span gate, answer-position patching, Stage 5
interchange, G16) uses the fixed-position one-token `direct` readout. That readout was
validated against the behavioural readout on the *position* contrast only —
`results/mech/direct_readout.json` contains `base`, `admit_pre/post`,
`exclude_pre/post` and nothing else.

G16 found a precise null on the class-versus-identifier binding contrast, where the
behavioural readout shows a large effect across six models. Two candidates remain:
G16's 17-token length pad, or the readout itself.

This script isolates the readout. It runs Stage 3A's **unmodified** prompts —
`id_base`, `id_admit_pre`, `id_admit_post`, `oe_L0`, `cls_pre`, no padding, no changed
grammar — through the direct readout, and compares the resulting REI against the
behavioural REI already in `results/raw/*_stage3.jsonl`.

Pre-committed interpretation, written before running:

* If the direct readout reproduces the class advantage, the readout is fine and G16's
  null is caused by its padded construction.
* If the direct readout nulls out on prompts that are byte-identical to Stage 3A's,
  the readout does not track this contrast, and every mechanism result that depends on
  it inherits that limitation. That is the bad outcome and it must be reported as
  such, not explored away.

    PYTHONPATH=src python3 src/mech/readout_validity_binding.py
"""
from __future__ import annotations

import argparse
import json
import os
import sys

import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from common import ROOT, digit_expectation, digit_ids, frozen_items, load_model  # noqa: E402
from schema import SYSTEM, compile_prompt  # noqa: E402

CONDITIONS = ("id_base", "id_admit_pre", "id_admit_post", "oe_L0", "cls_pre")
FAMILIES = ("legal_judgment", "evidence_inference")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="/var/tmp/xiang-isr-models/qwen3-8b")
    ap.add_argument("--out", default=os.path.join(ROOT, "results", "mech",
                                                  "readout_validity_binding.json"))
    args = ap.parse_args()

    tok, model = load_model(args.model)
    dids = digit_ids(tok).to(model.device)
    items = frozen_items(FAMILIES)
    print(f"{len(items)} items x {len(CONDITIONS)} conditions, direct readout",
          flush=True)

    records = []
    with torch.no_grad():
        for n, item in enumerate(items):
            y = {}
            for cond in CONDITIONS:
                user = compile_prompt(item, cond, mode="direct")
                text = tok.apply_chat_template(
                    [{"role": "system", "content": SYSTEM},
                     {"role": "user", "content": user}],
                    tokenize=False, add_generation_prompt=True)
                text += "ANSWER: "
                ids = tok(text, return_tensors="pt",
                          add_special_tokens=False)["input_ids"].to(model.device)
                y[cond] = float(digit_expectation(model(input_ids=ids).logits[0, -1],
                                                  dids))
            records.append({"item_id": item.item_id,
                            "task_family": item.task_family,
                            "direction": item.critical_direction, "y": y})
            if (n + 1) % 15 == 0:
                print(f"  {n + 1}/{len(items)}", flush=True)

    payload = {
        "note": "readout-validity check; Stage 3A prompts unmodified, direct readout",
        "model": args.model,
        "conditions": list(CONDITIONS),
        "families": list(FAMILIES),
        "records": records,
    }
    with open(args.out, "w") as handle:
        json.dump(payload, handle, indent=1)
    print(f"wrote {os.path.relpath(args.out, ROOT)}")


if __name__ == "__main__":
    main()
