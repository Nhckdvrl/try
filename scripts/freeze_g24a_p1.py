#!/usr/bin/env python3
"""Freeze Pilot P1 material: 96 strictly-unseen (1,1) exact-evidence groups.

Pilot P1 "Retraction operator discrimination" (user spec, 2026-09-25):
  * pool: census groups with n_inc == 1, n_dec == 1 AND
    evidence_seen_in_discovery600 == False  -> expect 224 (168 fever + 56 scifact)
  * one fixed seed, per-stratum seeded order over group_sha-sorted lists
  * initial 96 = first 64 fever + first 32 scifact; the remaining 104 fever +
    24 scifact stay in seed order as the SAME-SOURCE replacement reserve
    (data-validity swaps only, decided AFTER a zero-model review; never by
    "looks good for the hypothesis")
  * no model output is read at any point (asserted below)

Outputs:
  data/items/g24a_p1_pool_v1.csv       - all 224 groups, seed ranks, selection flags
  data/items/g24a_p1_review_v1.md       - the initial 96 in seed order, for the
                                          zero-model data-validity review
                                          (evidence + the two claims, NO gold
                                          labels shown: reviewer judges text
                                          semantics directly)

Usage: python scripts/freeze_g24a_p1.py
"""
from __future__ import annotations

import ast
import csv
import json
import random
import sys
from collections import Counter
from pathlib import Path

CENSUS_CSV = "results/discovery/g24a_fresh_pair_census_v1_groups.csv"
CANDIDATES = "data/items/g24a_candidates_v1.jsonl"
POOL_CSV = "data/items/g24a_p1_pool_v1.csv"
REVIEW_MD = "data/items/g24a_p1_review_v1.md"
SEED = 20260926            # fixed before any inspection; documented in commit
N_FEVER, N_SCI = 64, 32    # initial 96 stratum sizes
EXPECT_POOL = {"fever": 168, "scifact": 56}


def main() -> int:
    for p in (CENSUS_CSV, CANDIDATES, POOL_CSV, REVIEW_MD):
        if "results/raw" in p:
            raise SystemExit("REFUSAL: freeze must not read model output")

    # --- 1. strict-fresh (1,1) pool from the census -----------------------
    groups = []
    with open(CENSUS_CSV, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if r["n_inc"] == "1" and r["n_dec"] == "1" \
                    and r["evidence_seen_in_discovery600"] == "False":
                groups.append(r)
    by_src = Counter(r["source"] for r in groups)
    assert dict(by_src) == EXPECT_POOL, (dict(by_src), EXPECT_POOL)
    assert len(groups) == 224, len(groups)

    # --- 2. deterministic per-stratum seed order --------------------------
    order = {}
    for src in ("fever", "scifact"):
        lst = sorted([r for r in groups if r["source"] == src],
                     key=lambda r: r["group_sha"])
        random.Random(SEED).shuffle(lst)
        for i, r in enumerate(lst):
            r["_seed_rank"] = i
        order[src] = lst

    initial = order["fever"][:N_FEVER] + order["scifact"][:N_SCI]
    assert len(initial) == 96
    reserve = order["fever"][N_FEVER:] + order["scifact"][N_SCI:]

    # --- 3. verify every item id + load claims/evidence from candidates ----
    disc600 = {json.loads(l)["item_id"]
               for l in open("data/items/g24a_v1.jsonl", encoding="utf-8")}
    cand = {}
    for l in open(CANDIDATES, encoding="utf-8"):
        it = json.loads(l)
        cand[it["item_id"]] = it
    gold_xtab = Counter()
    for r in groups:
        inc_id = r["inc_item_ids"]
        dec_id = r["dec_item_ids"]
        assert "," not in inc_id and "," not in dec_id, r["group_sha"]
        assert inc_id not in disc600 and dec_id not in disc600, \
            (inc_id, dec_id, "item overlaps discovery 600")
        assert inc_id in cand and dec_id in cand
        i_it, d_it = cand[inc_id], cand[dec_id]
        assert i_it["critical_direction"] == "increase"
        assert d_it["critical_direction"] == "decrease"
        assert i_it["critical_evidence"] == d_it["critical_evidence"] \
            == r["evidence"], r["group_sha"]
        gold_xtab[(i_it["meta"].get("stratum")
                   if isinstance(i_it["meta"], dict)
                   else ast.literal_eval(i_it["meta"]).get("stratum"))] += 1

    # --- 4. pool csv -------------------------------------------------------
    with open(POOL_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["seed_rank_within_source", "source", "group_sha",
                    "selected_96", "role", "inc_item_id", "dec_item_id",
                    "auto_type", "jaccard_mean", "entity_overlap_mean"])
        allrows = order["fever"] + order["scifact"]
        for r in sorted(allrows, key=lambda x: (x["source"], x["_seed_rank"])):
            role = ("initial" if r in initial else "reserve")
            w.writerow([r["_seed_rank"], r["source"], r["group_sha"],
                        "yes" if r in initial else "no", role,
                        r["inc_item_ids"], r["dec_item_ids"],
                        r["auto_type"], r["jaccard_mean"],
                        r["entity_overlap_mean"]])
    # read-back assertion
    back = list(csv.DictReader(open(POOL_CSV, newline="", encoding="utf-8")))
    assert len(back) == 224
    assert sum(1 for r in back if r["selected_96"] == "yes") == 96
    assert Counter((r["source"], r["selected_96"]) for r in back)[("fever", "yes")] == 64
    assert Counter((r["source"], r["selected_96"]) for r in back)[("scifact", "yes")] == 32

    # --- 5. review material (initial 96, seed order, no labels) ------------
    L = ["# G24A P1 initial-96 zero-model data-validity review material",
         "",
         f"Seed {SEED}; strata 64 fever + 32 scifact from the strict-fresh "
         "224 (evidence_seen_in_discovery600 = False, topology (1,1)).",
         "",
         "Review criterion (data integrity ONLY): the shared evidence E must "
         "as a matter of fact SUPPORT the increase claim and UNDERMINE "
         "(contradict) the decrease claim. Invalid groups are replaced by the "
         "next group of the same source in frozen seed order. No stylistic / "
         "hypothesis-based selection.",
         "",
         "Gold labels are deliberately not shown: judge from the text.",
         ""]
    for r in initial:
        i_it = cand[r["inc_item_ids"]]
        d_it = cand[r["dec_item_ids"]]
        L += [f"## rank={r['_seed_rank']} source={r['source']} "
              f"sha={r['group_sha']}",
              "",
              f"EVIDENCE E:\n{r['evidence']}",
              "",
              f"INCREASE claim [{i_it['item_id']}]:\n{i_it['base_context']}",
              "",
              f"DECREASE claim [{d_it['item_id']}]:\n{d_it['base_context']}",
              ""]
    Path(REVIEW_MD).write_text("\n".join(L) + "\n", encoding="utf-8")

    print(f"pool: {len(groups)} strict-fresh (1,1) "
          f"(fever {by_src['fever']}, scifact {by_src['scifact']}) "
          f"== expected {EXPECT_POOL}")
    print(f"seed {SEED}: initial 96 = 64 fever + 32 scifact; "
          f"reserve = {len(order['fever']) - N_FEVER} fever + "
          f"{len(order['scifact']) - N_SCI} scifact")
    print(f"item/discovery overlap: 0 (asserted for all 224 groups); "
          f"direction vs stratum xtab: {dict(gold_xtab)}")
    print(f"wrote {POOL_CSV} (224 rows, 96 selected) + {REVIEW_MD} "
          f"(96 groups)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
