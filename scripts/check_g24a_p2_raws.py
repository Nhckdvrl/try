#!/usr/bin/env python3
"""Integrity check for Pilot P2 raw decision rows (zero model-output *read*
in the analytic sense — only structural/numeric validity is examined).

Expected layout per model tag (scripts/run_g24a_p2.sh, two invocations):
  results/raw/<tag>_g24a_p2_plus.jsonl    1,000 rows = 200 ids x 5 kinds
  results/raw/<tag>_g24a_p2_minus.jsonl     800 rows = 200 ids x 4 kinds

Checks per tag:
   1. row counts exactly 1,000 / 800
   2. unique (item_id, kind_name) pairs; full grid coverage
   3. plus file item ids == frozen ids_plus; minus file == ids_minus
   4. kind sets: plus has the 5 kinds, minus has the 4 evidence kinds
      and ZERO rows with kind_name == "base"  (base never issued on arm-)
   5. base rows exactly 200, one per plus item (shared Y0 present)
   6. task_family == g24a_vitaminc, model_tag == tag, kind == "digit",
      readout == "digit_expectation_0_100"
   7. value finite in [0, 100]; mass in (0, 1]; count unparsed/low-mass
   8. rule_to_answer_tokens: int for the four rule conditions, None for base
   9. claim grid: each of the 200 claims contributes exactly 5 + 4 rows
      (= the registered 9 cells) for this tag

Cross-model (when all five frozen panel tags are present):
  10. 200 claims x 9 cells x 5 models = 9,000 rows exactly

Usage:
  python scripts/check_g24a_p2_raws.py                 # whatever is present
  python scripts/check_g24a_p2_raws.py --require5      # full panel required
  python scripts/check_g24a_p2_raws.py --smoke         # smoke-suffixed files
"""
from __future__ import annotations

import argparse
import glob
import json
import math
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ITEMS = os.path.join(ROOT, "data", "items", "g24a_p2_v1.jsonl")
IDS_PLUS = os.path.join(ROOT, "data", "items", "g24a_p2_ids_plus.json")
IDS_MINUS = os.path.join(ROOT, "data", "items", "g24a_p2_ids_minus.json")

PANEL = ["mistral-small-24b", "llama31-8b", "qwen3-8b", "qwen35-9b", "gemma3-12b"]
KINDS_PLUS = ["base", "admit_post", "exclude_post",
              "strong_exclude_post", "counterfactual_delete_post"]
KINDS_MINUS = KINDS_PLUS[1:]


def load(path):
    return [json.loads(l) for l in open(path, encoding="utf-8")]


def check_arm(rows, arm, ids_expect, tag):
    label = f"{tag}/{arm}"
    kinds = KINDS_PLUS if arm == "plus" else KINDS_MINUS
    want_rows = len(ids_expect) * len(kinds)
    assert len(rows) == want_rows, f"{label}: {len(rows)} rows != {want_rows}"

    # 2. unique pairs + grid coverage
    pairs = [(r["item_id"], r["kind_name"]) for r in rows]
    assert len(set(pairs)) == len(pairs), f"{label}: duplicate (item,kind) rows"
    got = set(pairs)
    want = {(i, k) for i in ids_expect for k in kinds}
    assert got == want, (f"{label}: grid mismatch "
                         f"(missing {len(want - got)}, extra {len(got - want)})")

    # 4. no base on arm-
    if arm == "minus":
        assert not any(r["kind_name"] == "base" for r in rows), \
            f"{label}: base rows present on arm-"
    else:
        n_base = sum(1 for r in rows if r["kind_name"] == "base")
        assert n_base == len(ids_expect), \
            f"{label}: {n_base} base rows != {len(ids_expect)} (shared Y0)"

    unparsed = lowmass = 0
    for r in rows:
        # 6. provenance / readout
        assert r["task_family"] == "g24a_vitaminc", (label, r["item_id"])
        assert r["model_tag"] == tag, (label, r["model_tag"])
        assert r["kind"] == "digit", (label, r["item_id"], r["kind"])
        assert r["readout"] == "digit_expectation_0_100", (label, r["readout"])
        # 7. numeric validity (report, then assert)
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
    ap.add_argument("--require5", action="store_true",
                    help="fail unless all five frozen panel tags are present")
    ap.add_argument("--smoke", action="store_true",
                    help="check the _smoke-suffixed smoke outputs instead")
    args = ap.parse_args()

    suffix = "_smoke" if args.smoke else ""
    items = {d["item_id"]: d["meta"]["p2_id"] for d in
             (json.loads(l) for l in open(ITEMS, encoding="utf-8"))}
    if args.smoke:
        # the smoke runner wrote first-N id lists to logs/
        ids_plus = json.load(open(os.path.join(ROOT, "logs",
                                               "g24a_p2_smoke_ids_plus.json")))
        ids_minus = json.load(open(os.path.join(ROOT, "logs",
                                                "g24a_p2_smoke_ids_minus.json")))
        assert len(ids_plus) == len(ids_minus) == 4, (len(ids_plus), len(ids_minus))
    else:
        ids_plus = json.load(open(IDS_PLUS))
        ids_minus = json.load(open(IDS_MINUS))
        assert len(ids_plus) == len(ids_minus) == 200
    assert not (set(ids_plus) & set(ids_minus))

    pat = os.path.join(ROOT, "results", "raw", f"*_g24a_p2{suffix}_plus.jsonl")
    plus_files = sorted(glob.glob(pat))
    tags = [os.path.basename(p).split("_g24a_p2")[0] for p in plus_files]
    if args.require5:
        assert set(tags) == set(PANEL), f"panel mismatch: {sorted(tags)}"
        assert len(tags) == 5, tags

    total_rows = 0
    any_unparsed = any_lowmass = 0
    for pfile in plus_files:
        tag = os.path.basename(pfile).split("_g24a_p2")[0]
        mfile = pfile.replace("_plus.jsonl", "_minus.jsonl")
        assert os.path.exists(mfile), f"missing arm- file for {tag}: {mfile}"
        rows_p = load(pfile)
        rows_m = load(mfile)
        up, lp = check_arm(rows_p, "plus", set(ids_plus), tag)
        um, lm = check_arm(rows_m, "minus", set(ids_minus), tag)
        any_unparsed += up + um
        any_lowmass += lp + lm
        total_rows += len(rows_p) + len(rows_m)

        # 9. claim grid: 9 cells per claim for this tag = 5 arm+ kinds
        # (incl. base) + 4 arm- kinds; key on (arm, kind_name) since the
        # arm- kind names are a subset of arm+'s
        n_claims = len({items[i] for i in ids_plus})
        by_claim: dict[str, set] = {}
        for r in rows_p:
            by_claim.setdefault(items[r["item_id"]], set()).add(("plus", r["kind_name"]))
        for r in rows_m:
            by_claim.setdefault(items[r["item_id"]], set()).add(("minus", r["kind_name"]))
        assert len(by_claim) == n_claims, f"{tag}: {len(by_claim)} claims != {n_claims}"
        bad = {c: sorted(k) for c, k in by_claim.items() if len(k) != 9}
        assert not bad, f"{tag}: claims without exactly 9 cells: {list(bad)[:3]}"
        print(f"  {tag}: {len(rows_p)} + {len(rows_m)} = "
              f"{len(rows_p) + len(rows_m)} rows OK "
              f"(9 cells x {n_claims} claims), unparsed={up + um}, "
              f"mass<0.5={lp + lm}")

    # 10. cross-model grid
    per_tag = len(ids_plus) * len(KINDS_PLUS) + len(ids_minus) * len(KINDS_MINUS)
    want_total = per_tag * len(tags)
    if args.require5:
        assert per_tag == 1800, per_tag
        assert want_total == 9000, want_total
    assert total_rows == want_total, f"total {total_rows} != {want_total}"
    scope = ("full panel: 200 claims x 9 cells x 5 models"
             if args.require5 else
             f"smoke: {len(ids_plus)} ids/arm" if args.smoke else "partial")
    print(f"OK: {len(tags)} tag(s), {total_rows} rows ({scope})"
          f", unparsed={any_unparsed}, digit-mass<0.5={any_lowmass}")
    if any_unparsed:
        print(f"  NOTE: {any_unparsed} rows without a numeric value")
        if not args.smoke:
            sys.exit(1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
