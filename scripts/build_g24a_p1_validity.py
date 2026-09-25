#!/usr/bin/env python3
"""Serialize the Pilot P1 zero-model data-validity dispositions.

Review coverage (all grounded, line-by-line reads of the review material):
  * initial 96 groups  : data/items/g24a_p1_review_v1.md
  * replacement groups : data/items/g24a_p1_review_replacements_v1.md

Criterion (data integrity only): E must, as a matter of fact, make the
increase claim MORE likely true and the decrease claim LESS likely true.
Rejected = direction reversed / claim not undermined on the decrease side /
no bearing on the claim's assertion / claim asserts a different specific
fact than E states.  Kept (with notes) = weak-but-direction-correct, which
is the natural state of FEVER/SciFact material and is displayed as leverage
later, never filtered.

Replacement rule (user, verbatim): same source, next group in frozen seed
order; never selected by how well it fits any hypothesis.

Output: data/items/g24a_p1_validity_v1.jsonl  (104 lines:
  96 initial + 8 replacements; verdicts for every group consulted).

Usage: python scripts/build_g24a_p1_validity.py
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

POOL_CSV = "data/items/g24a_p1_pool_v1.csv"
OUT = "data/items/g24a_p1_validity_v1.jsonl"
SEED = 20260926
INITIAL_N = {"fever": 64, "scifact": 32}

# --- verdicts (mine, zero model output consulted) -------------------------
INVALID = {
    "fever": {
        14: "inc labeled increase but E refutes it (E: teams up with Iron Fist; "
            "claim: did not team up) - negation rewrite on the increase side",
        26: "inc 'technical writer' vs E 'novelist and essayist' - E does not "
            "make the claim more likely (profession substitution)",
        37: "dec claim (PM in 2009 after the first PM of India) is consistent "
            "with E (PM 2004-2014) - decrease side not undermined",
        50: "inc 'Wales is an island' vs E 'country that is part of ... the "
            "island of Great Britain' - E undercuts the claim",
        56: "inc 'did not experience the defeat' vs E 'Early in his reign, "
            "Great Britain defeated France' - direction reversed",
        63: "inc 'landlocked' vs E 'deepwater offshore' - direction reversed",
    },
    "scifact": {
        5: "inc (FoxO3a activation mediated by ROS) not addressed by E "
           "(Sir2/FOXO longevity, no ROS, no neuronal death) - no bearing",
        7: "dec (normal granulomas form in the presence of TNF) is consistent "
           "with E (TNF maintains granuloma integrity) - decrease side not "
           "undermined; presence/absence are not contradictories here",
    },
}

KEEP_NOTES = {
    ("fever", 3): "inc weak: actress -> 'on a television show' (weak positive, direction ok)",
    ("fever", 4): "inc weak: actor -> 'is famous' (weak positive, direction ok)",
    ("fever", 20): "dec weak: cricketer vs musician (wiki closed-world refutation)",
    ("fever", 30): "paraphrase: resignation effective 2010-01-01 == retirement from WWE",
    ("fever", 35): "agent 'he' supplied by claim context (dataset anaphora style)",
    ("fever", 42): "'eponymous actor': film subject listed as actor in E",
    ("fever", 45): "dec weak: actor vs dancer (wiki closed-world refutation)",
    ("fever", 47): "inc weak: third series commissioned -> 'has three series'",
    ("fever", 48): "dec weak: profession-stated vs singer (wiki closed-world refutation)",
    ("fever", 52): "dec weak: album vs song (category refutation)",
    ("fever", 66): "claim name typo 'Morse Corde' ~ 'Morse code'; direction intact",
    ("fever", 67): "predicate looseness: E says distributed, claim says produced; "
                   "same-studio involvement weak positive, direction ok",
    ("fever", 68): "inc weak: power ballad -> 'is single'",
    ("scifact", 0): "knockout-mice detail not in E; main clause supported",
    ("scifact", 1): "modality: E projects reduction ('could mitigate'), claim in "
                    "past tense; direction ok",
    ("scifact", 2): "'premenopausal' clause not in E; main association supported",
    ("scifact", 11): "exercise-specific attribution from lifestyle composite; direction ok",
    ("scifact", 12): "association (recruitment under inflammation) -> capacity; direction ok",
    ("scifact", 17): "ND3/ND6 detail not in E; main clause supported",
    ("scifact", 31): "therapy components not in E; superiority direction supported",
    ("scifact", 32): "agent (Microcin J25) supplied by claim context; E describes "
                     "the inhibition itself",
    ("scifact", 33): "weak bearing: E has insulin-maintenance, claims have myeloid "
                     "skew; mirror structure keeps both directions correct",
}


def main() -> int:
    pool = list(csv.DictReader(open(POOL_CSV, newline="", encoding="utf-8")))
    by_src = {"fever": [], "scifact": []}
    for row in pool:
        by_src[row["source"]].append(row)
    for src in by_src:
        by_src[src].sort(key=lambda r: int(r["seed_rank_within_source"]))
    sha = {(r["source"], int(r["seed_rank_within_source"])): r["group_sha"]
           for r in pool}

    lines = []
    for src in ("fever", "scifact"):
        n = INITIAL_N[src]
        inv = INVALID[src]
        # replacements: k-th invalid initial group is replaced by rank n+k
        repl_rank_of_invalid = {rank: n + k for k, rank in enumerate(sorted(inv))}
        # sanity: replacement ranks must be reserve (>= n) and all valid
        assert all(r >= n for r in repl_rank_of_invalid.values())
        assert all(r not in inv for r in repl_rank_of_invalid.values())

        # review coverage = initial ranks 0..n-1 plus the n_invalid reserve
        # ranks n..n+n_invalid-1 (exactly the groups consulted)
        for rank in range(0, n + len(inv)):
            row = by_src[src][rank]
            assert int(row["seed_rank_within_source"]) == rank
            is_initial = rank < n
            entry = {
                "source": src,
                "seed_rank": rank,
                "role": "initial" if is_initial else "replacement",
                "group_sha": row["group_sha"],
                "reviewed": True,
            }
            if rank in inv:
                entry["verdict"] = "invalid"
                entry["note"] = inv[rank]
                entry["replaced_by_rank"] = repl_rank_of_invalid[rank]
                entry["replaced_by_sha"] = sha[(src, repl_rank_of_invalid[rank])]
            else:
                entry["verdict"] = "valid"
                entry["note"] = KEEP_NOTES.get((src, rank), "ok")
                if not is_initial:
                    inv_rank = next(r for r, rp in repl_rank_of_invalid.items()
                                    if rp == rank)
                    entry["replaces_rank"] = inv_rank
                    entry["replaces_sha"] = sha[(src, inv_rank)]
            lines.append(entry)

    # stable, auditable order: by source then seed rank
    lines.sort(key=lambda e: (e["source"], e["seed_rank"]))
    with open(OUT, "w", encoding="utf-8") as fh:
        for e in lines:
            fh.write(json.dumps(e, ensure_ascii=False) + "\n")

    # read-back checks
    back = [json.loads(l) for l in open(OUT, encoding="utf-8")]
    assert len(back) == 104, len(back)
    n_inv = sum(1 for e in back if e["verdict"] == "invalid")
    assert n_inv == 8, n_inv
    for src, k in INITIAL_N.items():
        valid_initial = sum(1 for e in back if e["source"] == src
                            and e["role"] == "initial"
                            and e["verdict"] == "valid")
        valid_repl = sum(1 for e in back if e["source"] == src
                         and e["role"] == "replacement"
                         and e["verdict"] == "valid")
        assert valid_initial + valid_repl == k, (src, valid_initial, valid_repl)
    print(f"wrote {OUT}: 104 reviewed (96 initial + 8 replacement), "
          f"8 invalid (6 fever, 2 scifact), final strata 64 fever + 32 scifact")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
