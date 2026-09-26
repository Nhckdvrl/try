#!/usr/bin/env python3
"""Integrity check for §14 explanation-experiment raw decision rows (zero
model-output *read* in the analytic sense — only structural/numeric validity).

Expected layout per model tag (scripts/run_g24a_meta.sh, TWO invocations):
  results/raw/<tag>_g24a_meta_plus.jsonl    1,400 rows = 200 ids x 7 kinds
  results/raw/<tag>_g24a_meta_minus.jsonl   1,200 rows = 200 ids x 6 kinds

Checks per tag (both segments):
   1. row counts exactly 1,400 / 1,200
   2. unique (item_id, kind_name) pairs; full grid coverage per segment
   3. item ids == frozen data/items/g24a_p2_ids_{plus,minus}.json
   4. kind sets == the §14 run contract (7 plus / 6 minus; base plus-only)
   5. base rows exactly 200, plus arm only
   6. task_family == g24a_vitaminc, model_tag == tag, kind == "digit",
      readout == "digit_expectation_0_100"
   7. value finite in [0, 100]; mass in (0, 1]; count unparsed/low-mass
   8. rule_to_answer_tokens: int > 0 for the six ruling cells, None for base
   9. claim grid: each of the 200 claims contributes exactly 13 cells
      across the two segments

Cross-model (when all six frozen tags are present):
   10. 200 claims x 13 cells x 6 models = 15,600 rows exactly

Usage:
  python scripts/check_g24a_meta_raws.py                # whatever is present
  python scripts/check_g24a_meta_raws.py --require6     # full panel required
  python scripts/check_g24a_meta_raws.py --smoke        # smoke-suffixed files
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

PANEL = ["mistral-small-24b", "llama31-8b", "qwen3-8b", "qwen35-9b",
         "gemma3-12b", "qwen3-32b"]
KINDS_PLUS = ["base", "admit_post", "exclude_post",
              "strong_exclude_post", "counterfactual_delete_post",
              "meta_neutral_post", "random_reason_post"]
KINDS_MINUS = ["admit_post", "exclude_post",
               "strong_exclude_post", "counterfactual_delete_post",
               "meta_neutral_post", "random_reason_post"]
CELLS_PER_CLAIM = 13


def load(path):
    return [json.loads(l) for l in open(path, encoding="utf-8")]


def check_rows(rows, tag, ids_expect, kinds, fam_of, is_plus):
    label = tag
    want_rows = len(ids_expect) * len(kinds)
    assert len(rows) == want_rows, f"{label}: {len(rows)} rows != {want_rows}"

    # 2. unique pairs + grid coverage
    pairs = [(r["item_id"], r["kind_name"]) for r in rows]
    assert len(set(pairs)) == len(pairs), f"{label}: duplicate (item,kind) rows"
    got = set(pairs)
    want = {(i, k) for i in ids_expect for k in kinds}
    assert got == want, (f"{label}: grid mismatch "
                         f"(missing {len(want - got)}, extra {len(got - want)})")

    n_base = sum(1 for r in rows if r["kind_name"] == "base")
    if is_plus:
        assert n_base == len(ids_expect), \
            f"{label}: {n_base} base rows != {len(ids_expect)}"
    else:
        assert n_base == 0, f"{label}: base issued on arm- ({n_base} rows)"

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
        ids_plus = json.load(open(os.path.join(ROOT, "logs",
                                               "g24a_meta_smoke_ids_plus.json")))
        ids_minus = json.load(open(os.path.join(ROOT, "logs",
                                                "g24a_meta_smoke_ids_minus.json")))
        assert len(ids_plus) == len(ids_minus) == 4, (len(ids_plus), len(ids_minus))
    else:
        ids_plus = json.load(open(IDS_PLUS))
        ids_minus = json.load(open(IDS_MINUS))
        assert len(ids_plus) == len(ids_minus) == 200, (len(ids_plus), len(ids_minus))
        assert len(set(ids_plus) | set(ids_minus)) == 400
    assert set(ids_plus) <= set(fam_of) and set(ids_minus) <= set(fam_of), \
        "id list not a subset of the item file"
    assert not (set(ids_plus) & set(ids_minus)), "arm id lists overlap"

    pat = os.path.join(ROOT, "results", "raw", f"*_g24a_meta{suffix}_*.jsonl")
    files = sorted(glob.glob(pat))
    tags = sorted({os.path.basename(p).split("_g24a_meta")[0] for p in files})
    if args.require6:
        assert set(tags) == set(PANEL), f"panel mismatch: {sorted(tags)}"
        assert len(tags) == 6, tags

    total_rows = 0
    any_unparsed = any_lowmass = 0
    per_tag_rows = len(ids_plus) * len(KINDS_PLUS) + len(ids_minus) * len(KINDS_MINUS)
    for tag in tags:
        u = lm = 0
        tag_rows = 0
        for arm, ids, kinds in (("plus", ids_plus, KINDS_PLUS),
                                ("minus", ids_minus, KINDS_MINUS)):
            f = os.path.join(ROOT, "results", "raw",
                             f"{tag}_g24a_meta{suffix}_{arm}.jsonl")
            if not os.path.exists(f):
                if args.require6:
                    raise AssertionError(f"{tag}: missing segment {arm}")
                continue
            rows = load(f)
            u_a, lm_a = check_rows(rows, tag, set(ids), kinds, fam_of,
                                   arm == "plus")
            u += u_a
            lm += lm_a
            tag_rows += len(rows)
        any_unparsed += u
        any_lowmass += lm
        total_rows += tag_rows

        # 9. claim grid: 13 cells per claim across both segments
        #    (kind names repeat across arms -> count (arm, kind) tuples)
        by_claim: dict[str, set] = {}
        for arm in ("plus", "minus"):
            f = os.path.join(ROOT, "results", "raw",
                             f"{tag}_g24a_meta{suffix}_{arm}.jsonl")
            if not os.path.exists(f):
                continue
            for r in load(f):
                by_claim.setdefault(claim_of[r["item_id"]], set()).add(
                    (arm, r["kind_name"]))
        assert len(by_claim) == len(ids_plus), \
            f"{tag}: {len(by_claim)} claims != {len(ids_plus)}"
        bad = {c: sorted(k) for c, k in by_claim.items()
               if len(k) != CELLS_PER_CLAIM}
        assert not bad, f"{tag}: claims without exactly {CELLS_PER_CLAIM} cells: " \
                        f"{list(bad)[:3]}"
        print(f"  {tag}: {tag_rows} rows OK ({CELLS_PER_CLAIM} cells x "
              f"{len(ids_plus)} claims), unparsed={u}, mass<0.5={lm}")

    # 10. cross-model grid
    want_total = per_tag_rows * len(tags)
    if args.require6:
        assert per_tag_rows == 2600, per_tag_rows
        assert want_total == 15600, want_total
    assert total_rows == want_total, f"total {total_rows} != {want_total}"
    scope = ("full panel: 200 claims x 13 cells x 6 models"
             if args.require6 else
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
