#!/usr/bin/env python3
"""Merge Confirmation-B blind validity verdicts with the frozen pool.

Inputs (all zero-model, blind): 
  data/items/g24a_confb_validity_v1.jsonl          - active 200 verdicts
  data/items/g24a_confb_reserve_validity_v1.jsonl  - reserve ranks 200-279
  data/items/g24a_confb_reserve_ext_validity_v1.jsonl - extension ranks 280-303
  data/items/g24a_confb_pool_v1.csv                - frozen 280 rows
  data/items/g24a_confb_pool_ext_v1.csv            - seed-order continuation
  the three review MDs (A/B rendering integrity)

Checks:
  * every review MD block reproduces its pool row exactly
    (CLAIM = claim, Evidence A = evidence_s, Evidence B = evidence_r) —
    the freeze's A/B orientation rule (A = evidence_s) is applied here,
    after all 304 verdicts were recorded (blindness preserved);
  * every verdict record matches its pool row on (cfb_id, case_id, claim_sha);
  * for each VALID record, the recorded supporting side, mapped through the
    review rendering, must equal pool evidence_s — i.e. dataset orientation
    must agree with the blind call (0 mismatches required);
  * swap plan (P2 replacement rule): the i-th invalid active in seed order
    is replaced by the i-th VALID reserve in seed order (ranks 200+).

Output: data/items/g24a_confb_selected_v1.jsonl - exactly 200 pairs with
provenance (role, own seed rank, replaced rank/id, blind call + note).

Usage: python scripts/merge_g24a_confb_validity.py
"""
from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path

POOL_CSV = "data/items/g24a_confb_pool_v1.csv"
POOL_EXT_CSV = "data/items/g24a_confb_pool_ext_v1.csv"
VERDICTS = ("data/items/g24a_confb_validity_v1.jsonl",
            "data/items/g24a_confb_reserve_validity_v1.jsonl",
            "data/items/g24a_confb_reserve_ext_validity_v1.jsonl")
REVIEW_MDS = ("data/items/g24a_confb_review_v1.md",
              "data/items/g24a_confb_reserve_review_v1.md",
              "data/items/g24a_confb_reserve_ext_review_v1.md")
OUT = "data/items/g24a_confb_selected_v1.jsonl"
N_ACTIVE = 200


def load_pool() -> dict[int, dict]:
    pool = {}
    for path in (POOL_CSV, POOL_EXT_CSV):
        for r in csv.DictReader(open(path, newline="", encoding="utf-8")):
            pool[int(r["seed_rank"])] = r
    return pool


def parse_review(path: str) -> dict[int, dict]:
    blocks: dict[int, dict] = {}
    text = Path(path).read_text(encoding="utf-8")
    parts = text.split("## seed_rank=")[1:]
    for part in parts:
        rank = int(part.split()[0])
        lines = part.split("\n")[1:]          # drop the header rest-of-line
        # expected: "", "CLAIM:", claim, "", "Evidence A:", a, "", "Evidence B:", b, "", ...
        while lines and lines[0] == "":
            lines.pop(0)
        assert lines[0] == "CLAIM:", (path, rank, lines[:2])
        claim = lines[1]
        assert lines[2] == "" and lines[3] == "Evidence A:", (path, rank)
        a = lines[4]
        assert lines[5] == "" and lines[6] == "Evidence B:", (path, rank)
        b = lines[7]
        assert lines[8] == "", (path, rank, lines[8:10])
        blocks[rank] = {"claim": claim, "a": a, "b": b}
    return blocks


def main() -> int:
    pool = load_pool()
    assert len(pool) == 304, len(pool)

    # --- review rendering integrity: A == evidence_s, B == evidence_r ------
    seen_review: set[int] = set()
    for md in REVIEW_MDS:
        blocks = parse_review(md)
        for rank, blk in blocks.items():
            assert rank not in seen_review, rank
            seen_review.add(rank)
            p = pool[rank]
            assert blk["claim"] == p["claim"], (md, rank, "claim")
            assert blk["a"] == p["evidence_s"], (md, rank, "A!=evidence_s")
            assert blk["b"] == p["evidence_r"], (md, rank, "B!=evidence_r")
    print(f"review rendering verified: {len(seen_review)} blocks across "
          f"{len(REVIEW_MDS)} MDs (A == evidence_s, B == evidence_r)")

    # --- verdicts -----------------------------------------------------------
    verdicts: dict[int, dict] = {}
    for path in VERDICTS:
        for line in open(path, encoding="utf-8"):
            v = json.loads(line)
            rank = v["seed_rank"]
            assert rank not in verdicts, rank
            p = pool[rank]
            assert (v["cfb_id"], v["case_id"], v["claim_sha"]) == \
                (p["cfb_id"], p["case_id"], p["claim_sha"]), rank
            assert v["reviewed"] is True, rank
            assert v["verdict"] in ("valid", "invalid"), rank
            if v["verdict"] == "valid":
                assert v.get("supports") in ("A", "B"), rank
                # orientation check through the verified rendering:
                # supports=A means evidence_s is the claim-supporting side.
                side = p["evidence_s"] if v["supports"] == "A" else p["evidence_r"]
                assert side == p["evidence_s"], (
                    rank, "orientation mismatch: blind call says evidence_r "
                          "supports - dataset S side would be wrong")
            else:
                assert "supports" not in v, rank
            verdicts[rank] = v
    assert len(verdicts) == 304, len(verdicts)
    print("verdicts:", len(verdicts),
          dict(Counter(v["verdict"] for v in verdicts.values())),
          "| all valid calls orient to evidence_s")

    active_valid = sorted(r for r, v in verdicts.items()
                          if v["verdict"] == "valid" and pool[r]["active_200"] == "yes")
    active_invalid = sorted(r for r, v in verdicts.items()
                            if v["verdict"] == "invalid" and pool[r]["active_200"] == "yes")
    reserve_valid = sorted(r for r, v in verdicts.items()
                           if v["verdict"] == "valid" and pool[r]["active_200"] == "no")
    assert len(active_valid) + len(active_invalid) == N_ACTIVE
    print(f"active: {len(active_valid)} valid / {len(active_invalid)} invalid | "
          f"reserve valid: {len(reserve_valid)}")
    if len(reserve_valid) < len(active_invalid):
        raise SystemExit(f"shortfall: need {len(active_invalid)} valid reserves, "
                         f"have {len(reserve_valid)}")

    # --- swap plan: i-th invalid active <- i-th valid reserve (seed order) --
    swaps = list(zip(active_invalid, reserve_valid[:len(active_invalid)]))
    selected = list(active_valid) + [new for _, new in swaps]
    selected.sort()
    assert len(selected) == N_ACTIVE, len(selected)
    assert len({pool[r]["case_id"] for r in selected}) == N_ACTIVE
    assert len({pool[r]["claim_sha"] for r in selected}) == N_ACTIVE

    replaced_of = {new: old for old, new in swaps}
    with open(OUT, "w", encoding="utf-8") as fh:
        for rank in selected:
            p = pool[rank]
            v = verdicts[rank]
            rec = {
                "seed_rank": rank,
                "cfb_id": p["cfb_id"],
                "case_id": p["case_id"],
                "split": p["split"],
                "first_lineno": p["first_lineno"],
                "page": p["page"],
                "claim_sha": p["claim_sha"],
                "claim": p["claim"],
                "evidence_s": p["evidence_s"],
                "evidence_r": p["evidence_r"],
                "role": "active" if p["active_200"] == "yes" else "reserve",
                "meta": {
                    "pilot": "g24a_confb",
                    "confb_role": "active" if p["active_200"] == "yes" else "reserve",
                    "confb_seed_rank": rank,
                    "blind_call": v.get("supports"),
                    "blind_note": v["note"],
                },
            }
            if rank in replaced_of:
                old = replaced_of[rank]
                rec["meta"]["confb_replaced_seed_rank"] = old
                rec["meta"]["confb_replaced_cfb_id"] = pool[old]["cfb_id"]
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")

    kept = sum(1 for r in selected if pool[r]["active_200"] == "yes")
    print(f"selected {N_ACTIVE}: {kept} kept actives + {len(swaps)} swaps "
          f"(swapped ranks {active_invalid[0]}..{active_invalid[-1]} <- "
          f"{reserve_valid[0]}..{reserve_valid[len(swaps) - 1]})")
    print(f"wrote {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
