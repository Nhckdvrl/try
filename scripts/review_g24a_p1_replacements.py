#!/usr/bin/env python3
"""Emit review material for Pilot P1 replacement groups (zero-model, seed order).

The initial-96 validity review (data/items/g24a_p1_review_v1.md) found
semantic failures.  Per the user's rule, a failed group is replaced by the
NEXT group of the SAME source in frozen seed order - never by any
hypothesis-flattering criterion.  This script prints exactly that material
for the next-in-order groups that are needed to refill the strata to
64 fever + 32 valid scifact groups.

Inputs : data/items/g24a_p1_pool_v1.csv  (committed seed order)
         data/items/g24a_candidates_v1.jsonl
Output : data/items/g24a_p1_review_replacements_v1.md

Usage: python scripts/review_g24a_p1_replacements.py
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

POOL_CSV = "data/items/g24a_p1_pool_v1.csv"
CANDIDATES = "data/items/g24a_candidates_v1.jsonl"
OUT_MD = "data/items/g24a_p1_review_replacements_v1.md"

# Invalid groups found in the initial-96 review (by source, seed rank),
# and how many same-source reserve groups are therefore needed.
INVALID = {
    "fever": [14, 26, 37, 50, 56, 63],   # 6 -> need ranks 64..69
    "scifact": [5, 7],                   # 2 -> need ranks 32..33
}
INITIAL_N = {"fever": 64, "scifact": 32}


def main() -> int:
    pool = list(csv.DictReader(open(POOL_CSV, newline="", encoding="utf-8")))
    cand = {}
    for line in open(CANDIDATES, encoding="utf-8"):
        it = json.loads(line)
        cand[it["item_id"]] = it

    by_src = {"fever": [], "scifact": []}
    for row in pool:
        by_src[row["source"]].append(row)
    for src in by_src:
        by_src[src].sort(key=lambda r: int(r["seed_rank_within_source"]))

    L = [
        "# G24A P1 replacement-group zero-model validity review material",
        "",
        "Same criterion as the initial-96 review: the shared evidence E must",
        "as a matter of fact SUPPORT the increase claim and UNDERMINE the",
        "decrease claim.  Replacements are the next group of the same source",
        "in frozen seed order (fever ranks 64-69 for 6 invalid initial",
        "groups; scifact ranks 32-33 for 2).  Gold labels not shown.",
        "",
    ]
    n_needed = {src: len(INVALID[src]) for src in INVALID}
    for src in ("fever", "scifact"):
        for i in range(n_needed[src]):
            rank = INITIAL_N[src] + i
            row = by_src[src][rank]
            assert row["seed_rank_within_source"] == str(rank), row
            i_it = cand[row["inc_item_id"]]
            d_it = cand[row["dec_item_id"]]
            assert i_it["critical_direction"] == "increase"
            assert d_it["critical_direction"] == "decrease"
            # census-vs-candidates evidence equality for all 224 groups was
            # asserted at freeze time; here re-assert the within-group identity
            assert i_it["critical_evidence"] == d_it["critical_evidence"]
            L += [
                f"## replacement_for_invalid#{i} source={src} rank={rank} "
                f"sha={row['group_sha']}",
                "",
                f"EVIDENCE E:\n{i_it['critical_evidence']}",
                "",
                f"INCREASE claim [{i_it['item_id']}]:\n{i_it['base_context']}",
                "",
                f"DECREASE claim [{d_it['item_id']}]:\n{d_it['base_context']}",
                "",
            ]

    Path(OUT_MD).write_text("\n".join(L) + "\n", encoding="utf-8")
    back = Path(OUT_MD).read_text(encoding="utf-8")
    n_groups = back.count("## replacement_for_invalid#")
    assert n_groups == sum(n_needed.values()), (n_groups, n_needed)
    print(f"wrote {OUT_MD}: {n_groups} replacement groups "
          f"(fever {n_needed['fever']}, scifact {n_needed['scifact']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
