#!/usr/bin/env python3
"""Integrity check for Confirmation-B raw decision rows (zero model-output
*read* in the analytic sense — only structural/numeric validity).

Expected layout per model tag (scripts/run_g24a_confb.sh, three
invocations):
  results/raw/<tag>_g24a_confb_plus.jsonl      800 rows = 200 ids x 4 kinds
  results/raw/<tag>_g24a_confb_minus.jsonl     400 rows = 200 ids x 2 kinds
  results/raw/<tag>_g24a_confb_control.jsonl   200 rows = 200 ids x 1 kind

Checks per tag:
   1. row counts exactly 800 / 400 / 200 (= 1,400)
   2. unique (item_id, kind_name) pairs; full grid coverage per file
   3. item ids == the frozen ids_{plus,minus,control}.json files
   4. kind sets: plus = base, admit_post, counterfactual_delete_post,
      withheld_cf; minus = admit_post, counterfactual_delete_post (ZERO
      base rows); control = irrelevant_cf (exactly 200)
   5. base rows exactly 200, one per plus item (shared Y0 present)
   6. task_family == g24a_vitaminc, model_tag == tag, kind == "digit",
      readout == "digit_expectation_0_100"
   7. value finite in [0, 100]; mass in (0, 1]; count unparsed/low-mass
   8. rule_to_answer_tokens: int > 0 for every ruling cell (all six
      non-base cells carry a ruling), None for base
   9. claim grid: each of the 200 claims contributes exactly 7 cells
      (4 + 2 + 1) for this tag

Cross-model (when all six frozen tags are present):
  10. 200 claims x 7 cells x 6 models = 8,400 rows exactly

Usage:
  python scripts/check_g24a_confb_raws.py                # whatever is present
  python scripts/check_g24a_confb_raws.py --require6     # full panel required
  python scripts/check_g24a_confb_raws.py --smoke        # smoke-suffixed files
"""
from __future__ import annotations

import argparse
import glob
import json
import math
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ITEMS = os.path.join(ROOT, "data", "items", "g24a_confb_v1.jsonl")
IDS_PLUS = os.path.join(ROOT, "data", "items", "g24a_confb_ids_plus.json")
IDS_MINUS = os.path.join(ROOT, "data", "items", "g24a_confb_ids_minus.json")
IDS_CONTROL = os.path.join(ROOT, "data", "items", "g24a_confb_ids_control.json")

PANEL = ["mistral-small-24b", "llama31-8b", "qwen3-8b", "qwen35-9b",
         "gemma3-12b", "qwen3-32b"]
KINDS_PLUS = ["base", "admit_post", "counterfactual_delete_post", "withheld_cf"]
KINDS_MINUS = ["admit_post", "counterfactual_delete_post"]
KINDS_CONTROL = ["irrelevant_cf"]


def load(path):
    return [json.loads(l) for l in open(path, encoding="utf-8")]


def check_file(rows, arm, tag, ids_expect):
    label = f"{tag}/{arm}"
    kinds = {"plus": KINDS_PLUS, "minus": KINDS_MINUS,
             "control": KINDS_CONTROL}[arm]
    want_rows = len(ids_expect) * len(kinds)
    assert len(rows) == want_rows, f"{label}: {len(rows)} rows != {want_rows}"

    # 2. unique pairs + grid coverage
    pairs = [(r["item_id"], r["kind_name"]) for r in rows]
    assert len(set(pairs)) == len(pairs), f"{label}: duplicate (item,kind) rows"
    got = set(pairs)
    want = {(i, k) for i in ids_expect for k in kinds}
    assert got == want, (f"{label}: grid mismatch "
                         f"(missing {len(want - got)}, extra {len(got - want)})")

    # 4. no base outside plus; base count on plus
    if arm != "plus":
        assert not any(r["kind_name"] == "base" for r in rows), \
            f"{label}: base rows present on {arm}"
    if arm == "plus":
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
    cfb_of = {}
    for d in (json.loads(l) for l in open(ITEMS, encoding="utf-8")):
        cfb_of[d["item_id"]] = d["meta"]["cfb_id"]
    if args.smoke:
        paths = {arm: os.path.join(ROOT, "logs",
                                   f"g24a_confb_smoke_ids_{arm}.json")
                 for arm in ("plus", "minus", "control")}
        ids = {arm: json.load(open(p)) for arm, p in paths.items()}
        assert all(len(v) == 4 for v in ids.values()), \
            {k: len(v) for k, v in ids.items()}
    else:
        ids = {"plus": json.load(open(IDS_PLUS)),
               "minus": json.load(open(IDS_MINUS)),
               "control": json.load(open(IDS_CONTROL))}
        for arm, v in ids.items():
            assert len(v) == 200 and len(set(v)) == 200, (arm, len(v))
    assert not (set(ids["plus"]) & set(ids["minus"]))
    assert not (set(ids["plus"]) & set(ids["control"]))
    assert not (set(ids["minus"]) & set(ids["control"]))
    for arm, v in ids.items():
        assert set(v) <= set(cfb_of), f"{arm} ids not a subset of the item file"

    pat = os.path.join(ROOT, "results", "raw",
                       f"*_g24a_confb{suffix}_plus.jsonl")
    plus_files = sorted(glob.glob(pat))
    tags = [os.path.basename(p).split("_g24a_confb")[0] for p in plus_files]
    if args.require6:
        assert set(tags) == set(PANEL), f"panel mismatch: {sorted(tags)}"
        assert len(tags) == 6, tags

    total_rows = 0
    any_unparsed = any_lowmass = 0
    for pfile in plus_files:
        tag = os.path.basename(pfile).split("_g24a_confb")[0]
        mfile = pfile.replace("_plus.jsonl", "_minus.jsonl")
        cfile = pfile.replace("_plus.jsonl", "_control.jsonl")
        assert os.path.exists(mfile), f"missing minus file for {tag}: {mfile}"
        assert os.path.exists(cfile), f"missing control file for {tag}: {cfile}"
        rows_p, rows_m, rows_c = load(pfile), load(mfile), load(cfile)
        u1, l1 = check_file(rows_p, "plus", tag, set(ids["plus"]))
        u2, l2 = check_file(rows_m, "minus", tag, set(ids["minus"]))
        u3, l3 = check_file(rows_c, "control", tag, set(ids["control"]))
        any_unparsed += u1 + u2 + u3
        any_lowmass += l1 + l2 + l3
        total_rows += len(rows_p) + len(rows_m) + len(rows_c)

        # 9. claim grid: 7 cells per claim for this tag (keyed on (arm, kind)
        # since admit/cf kind names appear in both arms)
        by_claim: dict[str, set] = {}
        for r in rows_p:
            by_claim.setdefault(cfb_of[r["item_id"]], set()) \
                    .add(("plus", r["kind_name"]))
        for r in rows_m:
            by_claim.setdefault(cfb_of[r["item_id"]], set()) \
                    .add(("minus", r["kind_name"]))
        for r in rows_c:
            by_claim.setdefault(cfb_of[r["item_id"]], set()) \
                    .add(("control", r["kind_name"]))
        n_claims = len(set(cfb_of[i] for i in ids["plus"]))
        assert len(by_claim) == n_claims, \
            f"{tag}: {len(by_claim)} claims != {n_claims}"
        bad = {c: sorted(k) for c, k in by_claim.items() if len(k) != 7}
        assert not bad, f"{tag}: claims without exactly 7 cells: {list(bad)[:3]}"
        print(f"  {tag}: {len(rows_p)} + {len(rows_m)} + {len(rows_c)} = "
              f"{len(rows_p) + len(rows_m) + len(rows_c)} rows OK "
              f"(7 cells x {n_claims} claims), "
              f"unparsed={u1 + u2 + u3}, mass<0.5={l1 + l2 + l3}")

    # 10. cross-model grid
    per_tag = (len(ids["plus"]) * len(KINDS_PLUS)
               + len(ids["minus"]) * len(KINDS_MINUS)
               + len(ids["control"]) * len(KINDS_CONTROL))
    want_total = per_tag * len(tags)
    if args.require6:
        assert per_tag == 1400, per_tag
        assert want_total == 8400, want_total
    assert total_rows == want_total, f"total {total_rows} != {want_total}"
    scope = ("full panel: 200 claims x 7 cells x 6 models"
             if args.require6 else
             f"smoke: {len(ids['plus'])} ids/arm" if args.smoke else "partial")
    print(f"OK: {len(tags)} tag(s), {total_rows} rows ({scope})"
          f", unparsed={any_unparsed}, digit-mass<0.5={any_lowmass}")
    if any_unparsed:
        print(f"  NOTE: {any_unparsed} rows without a numeric value")
        if not args.smoke:
            sys.exit(1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
