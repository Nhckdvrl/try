#!/usr/bin/env python3
"""Integrity check for Confirmation-A raw decision rows (zero model-output
*read* in the analytic sense — only structural/numeric validity).

Expected layout per model tag (scripts/run_g24a_confa.sh, one invocation):
  results/raw/<tag>_g24a_confa.jsonl    2,500 rows = 500 ids x 5 kinds

Checks per tag:
   1. row counts exactly 2,500
   2. unique (item_id, kind_name) pairs; full grid coverage
   3. item ids == frozen data/items/g24a_confa_ids.json
   4. kind set == the G24A five (base, admit_pre, admit_post, exclude_pre,
      exclude_post)
   5. base rows exactly 500, one per item
   6. task_family == the item's own (g24a_fever 334 / g24a_scifact 166),
      model_tag == tag, kind == "digit", readout == "digit_expectation_0_100"
   7. value finite in [0, 100]; mass in (0, 1]; count unparsed/low-mass
   8. rule_to_answer_tokens: int > 0 for the four ruling cells, None for base
   9. claim grid: each of the 500 claims contributes exactly 5 cells

Cross-model (when all six frozen tags are present):
  10. 500 claims x 5 cells x 6 models = 15,000 rows exactly

Usage:
  python scripts/check_g24a_confa_raws.py                # whatever is present
  python scripts/check_g24a_confa_raws.py --require6     # full panel required
  python scripts/check_g24a_confa_raws.py --smoke        # smoke-suffixed files
"""
from __future__ import annotations

import argparse
import glob
import json
import math
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ITEMS = os.path.join(ROOT, "data", "items", "g24a_confa_v1.jsonl")
IDS = os.path.join(ROOT, "data", "items", "g24a_confa_ids.json")

PANEL = ["mistral-small-24b", "llama31-8b", "qwen3-8b", "qwen35-9b",
         "gemma3-12b", "qwen3-32b"]
KINDS = ["base", "admit_pre", "admit_post", "exclude_pre", "exclude_post"]


def load(path):
    return [json.loads(l) for l in open(path, encoding="utf-8")]


def check_rows(rows, tag, ids_expect, fam_of, claim_of):
    label = tag
    want_rows = len(ids_expect) * len(KINDS)
    assert len(rows) == want_rows, f"{label}: {len(rows)} rows != {want_rows}"

    # 2. unique pairs + grid coverage
    pairs = [(r["item_id"], r["kind_name"]) for r in rows]
    assert len(set(pairs)) == len(pairs), f"{label}: duplicate (item,kind) rows"
    got = set(pairs)
    want = {(i, k) for i in ids_expect for k in KINDS}
    assert got == want, (f"{label}: grid mismatch "
                         f"(missing {len(want - got)}, extra {len(got - want)})")

    n_base = sum(1 for r in rows if r["kind_name"] == "base")
    assert n_base == len(ids_expect), \
        f"{label}: {n_base} base rows != {len(ids_expect)}"

    unparsed = lowmass = 0
    for r in rows:
        # 6. provenance / readout
        assert r["task_family"] == fam_of[r["item_id"]], (label, r["item_id"])
        assert r["model_tag"] == tag, (label, r["model_tag"])
        assert r["kind"] == "digit", (label, r["item_id"], r["kind"])
        assert r["readout"] == "digit_expectation_0_100", (label, r["readout"])
        # 7. numeric validity
        v, m = r.get("value"), r.get("mass")
        if v is None or not math.isfinite(v):
            unparsed += 1
        else:
            assert 0.0 <= v <= 100.0, (label, r["item_id"], r["kind_name"], v)
            assert 0.0 < m <= 1.0 + 1e-6, (label, r["item_id"], m)
            if m < 0.5:
                lowmass += 1
        # 8. rule distance present iff a ruling block exists
        rat = r.get("rule_to_answer_tokens")
        if r["kind_name"] == "base":
            assert rat is None, (label, r["item_id"], "base has rule distance")
        else:
            assert isinstance(rat, int) and rat > 0, (label, r["item_id"], rat)
        assert "reasoning" in r, (label, r["item_id"])
    return unparsed, lowmass


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--require6", action="store_true",
                    help="fail unless all six frozen tags are present")
    ap.add_argument("--smoke", action="store_true",
                    help="check the _smoke-suffixed smoke outputs instead")
    args = ap.parse_args()

    suffix = "_smoke" if args.smoke else ""
    fam_of, claim_of = {}, {}
    for d in (json.loads(l) for l in open(ITEMS, encoding="utf-8")):
        fam_of[d["item_id"]] = d["task_family"]
        claim_of[d["item_id"]] = d["base_context"]
    if args.smoke:
        ids = json.load(open(os.path.join(ROOT, "logs",
                                          "g24a_confa_smoke_ids.json")))
        assert len(ids) == 4, len(ids)
    else:
        ids = json.load(open(IDS))
        assert len(ids) == 500 and len(set(ids)) == 500, len(ids)
    assert set(ids) <= set(fam_of), "id list not a subset of the item file"

    pat = os.path.join(ROOT, "results", "raw", f"*_g24a_confa{suffix}.jsonl")
    files = sorted(glob.glob(pat))
    tags = [os.path.basename(p).split("_g24a_confa")[0] for p in files]
    if args.require6:
        assert set(tags) == set(PANEL), f"panel mismatch: {sorted(tags)}"
        assert len(tags) == 6, tags

    total_rows = 0
    any_unparsed = any_lowmass = 0
    for f in files:
        tag = os.path.basename(f).split("_g24a_confa")[0]
        rows = load(f)
        u, lm = check_rows(rows, tag, set(ids), fam_of, claim_of)
        any_unparsed += u
        any_lowmass += lm
        total_rows += len(rows)

        # 9. claim grid: 5 cells per claim for this tag
        by_claim: dict[str, set] = {}
        for r in rows:
            by_claim.setdefault(claim_of[r["item_id"]], set()).add(r["kind_name"])
        assert len(by_claim) == len(ids), \
            f"{tag}: {len(by_claim)} claims != {len(ids)}"
        bad = {c: sorted(k) for c, k in by_claim.items() if len(k) != 5}
        assert not bad, f"{tag}: claims without exactly 5 cells: {list(bad)[:3]}"
        print(f"  {tag}: {len(rows)} rows OK (5 cells x {len(ids)} claims), "
              f"unparsed={u}, mass<0.5={lm}")

    # 10. cross-model grid
    per_tag = len(ids) * len(KINDS)
    want_total = per_tag * len(tags)
    if args.require6:
        assert per_tag == 2500, per_tag
        assert want_total == 15000, want_total
    assert total_rows == want_total, f"total {total_rows} != {want_total}"
    scope = ("full panel: 500 claims x 5 cells x 6 models"
             if args.require6 else
             f"smoke: {len(ids)} ids" if args.smoke else "partial")
    print(f"OK: {len(tags)} tag(s), {total_rows} rows ({scope})"
          f", unparsed={any_unparsed}, digit-mass<0.5={any_lowmass}")
    if any_unparsed:
        print(f"  NOTE: {any_unparsed} rows without a numeric value")
        if not args.smoke:
            sys.exit(1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
