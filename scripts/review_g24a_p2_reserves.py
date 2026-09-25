#!/usr/bin/env python3
"""Emit review material for Pilot P2 RESERVE pairs (zero-model, seed order).

The active-200 validity review (data/items/g24a_p2_review_v1.md) found
44 invalid pairs (data-validity failures: refute arm does not refute,
orientation reversed, compatible/absent evidence, broken text).  Per the
user's rule, an invalid pair is replaced by the NEXT pair of the same pool
in frozen seed order - never by any hypothesis-flattering criterion.

The pool's original 40-pair reserve was extended to 80 at freeze time
(deterministic: identical seed + identical candidate list -> identical
shuffle prefix, active 200 untouched, pool rows 0-239 byte-identical).
This script prints ALL 80 reserve pairs (seed_rank 200..279) in frozen
seed order; they are consulted in order until 44 valid replacements are
collected.  The k-th invalid ACTIVE pair (in seed order) is replaced by
the k-th VALID reserve pair (in seed order).

Inputs : data/items/g24a_p2_pool_v1.csv  (committed seed order)
Output : data/items/g24a_p2_review_reserves_v1.md

Usage: python scripts/review_g24a_p2_reserves.py
"""
from __future__ import annotations

import csv
from pathlib import Path

POOL_CSV = "data/items/g24a_p2_pool_v1.csv"
OUT_MD = "data/items/g24a_p2_review_reserves_v1.md"

# Invalid active ranks found in the active-200 review (44; review evidence).
INVALID_ACTIVE_RANKS = [
    7, 8, 9, 13, 22, 25, 30, 31, 32, 42, 45, 50, 52, 56, 61, 63, 78, 80,
    86, 90, 95, 97, 100, 106, 109, 118, 119, 124, 127, 139, 151, 152, 155,
    157, 162, 166, 168, 173, 182, 183, 188, 195, 197, 199,
]
N_ACTIVE, N_RESERVE = 200, 80


def main() -> int:
    pool = list(csv.DictReader(open(POOL_CSV, newline="", encoding="utf-8")))
    assert len(pool) == N_ACTIVE + N_RESERVE, len(pool)
    active = [r for r in pool if r["active_200"] == "yes"]
    reserve = [r for r in pool if r["active_200"] == "no"]
    assert len(active) == N_ACTIVE and len(reserve) == N_RESERVE
    assert [int(r["seed_rank"]) for r in reserve] == list(
        range(N_ACTIVE, N_ACTIVE + N_RESERVE))
    for r in active:
        assert int(r["seed_rank"]) < N_ACTIVE
    n_needed = len(INVALID_ACTIVE_RANKS)

    L = [
        "# G24A P2 reserve-pair zero-model validity review material",
        "",
        "Same criterion as the active-200 review: exactly one of Evidence A /",
        "Evidence B supports the claim as a matter of fact, and the other",
        "contradicts it as a matter of fact; claim must be self-contained.",
        f"The active-200 review found {n_needed} invalid pairs; reserves are",
        "consulted in frozen seed order (rank 200 upward) until",
        f"{n_needed} valid replacements are collected.  The k-th invalid",
        "active pair (seed order) maps to the k-th VALID reserve (seed",
        "order).  Evidence A / Evidence B stay UNLABELED; recorded S/R",
        "orientation lives only in the pool csv.",
        "",
    ]
    for r in reserve:
        rank = int(r["seed_rank"])
        L += [
            f"## seed_rank={rank} p2_id={r['p2_id']} case={r['case_id']} "
            f"page={r['page']!r}",
            "",
            f"CLAIM:\n{r['claim']}",
            "",
            f"Evidence A:\n{r['evidence_s']}",
            "",
            f"Evidence B:\n{r['evidence_r']}",
            "",
        ]
    Path(OUT_MD).write_text("\n".join(L) + "\n", encoding="utf-8")
    back = Path(OUT_MD).read_text(encoding="utf-8")
    assert back.count("## seed_rank=") == N_RESERVE
    print(f"wrote {OUT_MD}: {N_RESERVE} reserve pairs "
          f"({n_needed} replacements needed)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
