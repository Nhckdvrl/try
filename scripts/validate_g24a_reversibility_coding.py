#!/usr/bin/env python3
"""Validate the G24A reversibility rationale-coding files (step 4 artifact).

Ground truth = the raw run rows (results/raw/<model>_g24a.jsonl), NOT the
derived batch files. Checks per coding file (one per model, 53 lines each):

  * parses as JSONL; exactly 53 lines; gnum == 1..53 each exactly once
  * model tag matches the file name
  * labels are in the rubric's valid set
  * group_sha matches the hand-classified claim_pairs CSV for that gnum
  * inc_item / dec_item belong to the correct side of that group
  * every quote is a character-exact substring of the corresponding
    item's exclude_post reasoning in the RAW file, and <= 20 words

Exit 0 = all files pass; exit 1 with a printed error list otherwise.

Usage: HF_HUB_OFFLINE=1 python scripts/validate_g24a_reversibility_coding.py
"""
from __future__ import annotations

import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

MODELS = ["gemma3-12b", "llama31-8b", "mistral-small-24b", "qwen3-8b",
          "qwen35-9b"]
VALID_LABELS = {"reset_to_uncertainty", "still_cites_for_falsity", "other",
                "unclear"}
PREFIX = "results/discovery/g24a_reversibility_v1"


def main() -> int:
    # group membership + sha from the hand-classified CSV
    tax = {}
    for r in csv.DictReader(open(PREFIX + "_claim_pairs.csv",
                                 encoding="utf-8")):
        tax[int(r["gnum"])] = {
            "sha": r["group_sha"],
            "inc": set(r["inc_item_ids"].split(",")),
            "dec": set(r["dec_item_ids"].split(",")),
        }
    assert len(tax) == 53, f"claim_pairs has {len(tax)} rows, expected 53"

    errors = []
    for model in MODELS:
        path = f"{PREFIX}_coding_{model}.jsonl"
        if not Path(path).exists():
            errors.append(f"{model}: coding file missing ({path})")
            continue
        rows = []
        for ln, line in enumerate(open(path, encoding="utf-8"), 1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as e:
                errors.append(f"{model}: line {ln} not JSON: {e}")
        if len(rows) != 53:
            errors.append(f"{model}: {len(rows)} lines, expected 53")
        gnums = sorted(r.get("gnum") for r in rows if "gnum" in r)
        if gnums != list(range(1, 54)):
            errors.append(f"{model}: gnum coverage != 1..53 "
                          f"(min={gnums[:1]} max={gnums[-1:]} "
                          f"unique={len(set(gnums))})")

        # raw exclude_post reasoning per item (ground truth)
        raw = {}
        for line in open(f"results/raw/{model}_g24a.jsonl",
                         encoding="utf-8"):
            r = json.loads(line)
            if r["kind_name"] == "exclude_post":
                raw[r["item_id"]] = r

        nq = 0
        for r in rows:
            g = r.get("gnum")
            tag = f"{model} g{g}"
            if r.get("model") != model:
                errors.append(f"{tag}: model field {r.get('model')!r}")
            t = tax.get(g)
            if t is None:
                continue
            if r.get("group_sha") != t["sha"]:
                errors.append(f"{tag}: group_sha mismatch")
            for side in ("inc", "dec"):
                item = r.get(f"{side}_item")
                if item not in t[side]:
                    errors.append(f"{tag}: {side}_item {item!r} not in "
                                  f"group's {side} side {sorted(t[side])}")
                lab = r.get(f"{side}_label")
                if lab not in VALID_LABELS:
                    errors.append(f"{tag}: invalid {side}_label {lab!r}")
                quote = r.get(f"{side}_quote", "")
                rr = raw.get(item, {}).get("reasoning", "")
                if quote not in rr:
                    errors.append(f"{tag}: {side}_quote not a substring of "
                                  f"RAW reasoning for {item}")
                elif len(quote.split()) > 20:
                    errors.append(f"{tag}: {side}_quote > 20 words")
                else:
                    nq += 1
        print(f"{model:20s} lines={len(rows)} quotes_pass={nq}/106")

    if errors:
        print(f"\nFAILED: {len(errors)} error(s)")
        for e in errors[:40]:
            print("  -", e)
        return 1
    print("ALL CODING FILES VALID (5 models x 53 cells, "
          "265 quotes verified against raw)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
