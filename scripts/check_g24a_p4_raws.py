#!/usr/bin/env python3
"""Integrity check for Pilot P4 raw decision rows (zero model-output *read*
in the analytic sense — only structural/numeric validity is examined).

Expected layout per model tag (scripts/run_g24a_p4.sh, one invocation):
  results/raw/<tag>_g24a_p4.jsonl    400 rows = 200 ids x 2 kinds

Checks per tag:
    1. row counts exactly 400
    2. unique (item_id, kind_name) pairs; full grid coverage
    3. item ids == frozen data/items/g24a_p4_ids.json
    4. kind sets: exactly the 2 registered P4 kinds, nothing else
    5. task_family == g24a_vitaminc, model_tag == tag, kind == "digit",
       readout == "digit_expectation_0_100"
    6. value finite in [0, 100]; mass in (0, 1]; count unparsed/low-mass
    7. rule_to_answer_tokens: int for irrelevant_cf (RULING block),
       None for irrelevant_visible (no RULING by construction)
    8. claim grid: each of the 200 claims contributes exactly 2 rows

Cross-model (when all five frozen panel tags are present):
     9. 200 claims x 2 cells x 5 models = 2,000 rows exactly

Usage:
  python scripts/check_g24a_p4_raws.py                 # whatever is present
  python scripts/check_g24a_p4_raws.py --require5      # full panel required
  python scripts/check_g24a_p4_raws.py --smoke         # smoke-suffixed files
"""
from __future__ import annotations

import argparse
import glob
import json
import math
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ITEMS = os.path.join(ROOT, "data", "items", "g24a_p4_v1.jsonl")
IDS = os.path.join(ROOT, "data", "items", "g24a_p4_ids.json")

PANEL = ["mistral-small-24b", "llama31-8b", "qwen3-8b", "qwen35-9b", "gemma3-12b"]
KINDS = ["irrelevant_visible", "irrelevant_cf"]
RULING_KINDS = {"irrelevant_cf"}
NO_RULING_KINDS = {"irrelevant_visible"}


def load(path):
    return [json.loads(l) for l in open(path, encoding="utf-8")]


def check_tag(rows, ids_expect, tag):
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

    # 4. kind names exactly the registered two
    assert {r["kind_name"] for r in rows} == set(KINDS), label

    unparsed = lowmass = 0
    for r in rows:
        # 5. provenance / readout
        assert r["task_family"] == "g24a_vitaminc", (label, r["item_id"])
        assert r["model_tag"] == tag, (label, r["model_tag"])
        assert r["kind"] == "digit", (label, r["item_id"], r["kind"])
        assert r["readout"] == "digit_expectation_0_100", (label, r["readout"])
        # 6. numeric validity (report, then assert)
        v, m = r.get("value"), r.get("mass")
        if v is None or not math.isfinite(v):
            unparsed += 1
        else:
            assert 0.0 <= v <= 100.0, (label, r["item_id"], r["kind_name"], v)
            # mass is a sum of exp(logprobs): float error can push it a
            # few 1e-8 above 1.0
            assert 0.0 < m <= 1.0 + 1e-6, (label, r["item_id"], m)
            if m < 0.5:
                lowmass += 1
        # 7. rule distance present iff a RULING block exists
        rat = r.get("rule_to_answer_tokens")
        if r["kind_name"] in NO_RULING_KINDS:
            assert rat is None, (label, r["item_id"], r["kind_name"], rat)
        else:
            assert r["kind_name"] in RULING_KINDS, (label, r["kind_name"])
            assert isinstance(rat, int) and rat > 0, (label, r["item_id"], rat)
        assert "reasoning" in r, (label, r["item_id"])
    return unparsed, lowmass


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--require5", action="store_true",
                    help="fail unless all five frozen panel tags are present")
    ap.add_argument("--smoke", action="store_true",
                    help="check the _smoke-suffixed smoke outputs instead")
    args = ap.parse_args()

    suffix = "_smoke" if args.smoke else ""
    if args.smoke:
        # the smoke runner wrote the first-N id list to logs/
        ids = json.load(open(os.path.join(ROOT, "logs",
                                          "g24a_p4_smoke_ids.json")))
        assert len(ids) == 4, len(ids)
    else:
        ids = json.load(open(IDS))
        assert len(ids) == 200, len(ids)
    items = {d["item_id"]: d["meta"]["p2_id"] for d in
             (json.loads(l) for l in open(ITEMS, encoding="utf-8"))}
    assert set(ids) <= set(items), "id list not covered by the item file"

    pat = os.path.join(ROOT, "results", "raw", f"*_g24a_p4{suffix}.jsonl")
    files = sorted(glob.glob(pat))
    tags = [os.path.basename(p).split("_g24a_p4")[0] for p in files]
    if args.require5:
        assert set(tags) == set(PANEL), f"panel mismatch: {sorted(tags)}"
        assert len(tags) == 5, tags

    total_rows = 0
    any_unparsed = any_lowmass = 0
    for pfile in files:
        tag = os.path.basename(pfile).split("_g24a_p4")[0]
        rows = load(pfile)
        up, lp = check_tag(rows, set(ids), tag)
        any_unparsed += up
        any_lowmass += lp
        total_rows += len(rows)

        # 8. claim grid: 2 cells per claim for this tag
        by_claim: dict[str, set] = {}
        for r in rows:
            by_claim.setdefault(items[r["item_id"]], set()).add(r["kind_name"])
        assert len(by_claim) == len({items[i] for i in ids}), \
            f"{tag}: {len(by_claim)} claims != expected"
        bad = {c: sorted(k) for c, k in by_claim.items() if len(k) != 2}
        assert not bad, f"{tag}: claims without exactly 2 cells: {list(bad)[:3]}"
        print(f"  {tag}: {len(rows)} rows OK (2 cells x {len(by_claim)} claims), "
              f"unparsed={up}, mass<0.5={lp}")

    # 9. cross-model grid
    per_tag = len(ids) * len(KINDS)
    want_total = per_tag * len(tags)
    if args.require5:
        assert per_tag == 400, per_tag
        assert want_total == 2000, want_total
    assert total_rows == want_total, f"total {total_rows} != {want_total}"
    scope = ("full panel: 200 claims x 2 cells x 5 models"
             if args.require5 else
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
