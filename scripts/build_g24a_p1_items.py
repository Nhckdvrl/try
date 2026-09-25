#!/usr/bin/env python3
"""Build the Pilot P1 item file: 96 valid groups x 2 claims = 192 items.

Inputs (all committed before any model run):
  data/items/g24a_p1_pool_v1.csv           - 224 strict-fresh (1,1) groups, seed order
  data/items/g24a_p1_validity_v1.jsonl     - 104 consulted groups, my verdicts
  data/items/g24a_candidates_v1.jsonl      - frozen candidate pool

Selection rule (fixed before reading anything): per source, walk the seed
order and take groups whose validity verdict is "valid" until the stratum
is full (64 fever, 32 scifact).  Invalid groups are skipped, so the k-th
invalid initial group is filled by the k-th reserve group - exactly the
chain recorded in the validity file.

Item construction: candidate JSON copied field-for-field, EXCEPT meta is
converted from the candidates' repr-string to a real JSON object and
annotated with pilot provenance (group sha, seed rank, role, validity
note).  task_family is deliberately left as g24a_fever / g24a_scifact so
that Base / AdmitPost / ExcludePost render through the *unmodified* G24A
module (character-identical prompts by construction); the two new P1
operators dispatch on condition name inside schema._blocks.

Output: data/items/g24a_p1_v1.jsonl (192 lines).

Usage: python scripts/build_g24a_p1_items.py
"""
from __future__ import annotations

import ast
import csv
import json
from collections import Counter
from pathlib import Path

POOL_CSV = "data/items/g24a_p1_pool_v1.csv"
VALIDITY = "data/items/g24a_p1_validity_v1.jsonl"
CANDIDATES = "data/items/g24a_candidates_v1.jsonl"
DISCOVERY = "data/items/g24a_v1.jsonl"
OUT = "data/items/g24a_p1_v1.jsonl"
TARGET = {"fever": 64, "scifact": 32}

ITEM_KEYS = [
    "item_id", "task_family", "surface_domain", "base_context",
    "critical_evidence", "critical_label", "critical_direction",
    "exclusion_reason", "evidence_truth", "admit_rule", "exclude_rule",
    "question", "output_spec", "memory_question", "rule_probe_question",
    "ground_truth", "meta",
]


def main() -> int:
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
    import conditions_g24a as g24a

    pool = list(csv.DictReader(open(POOL_CSV, newline="", encoding="utf-8")))
    by_src = {"fever": [], "scifact": []}
    for row in pool:
        by_src[row["source"]].append(row)
    for src in by_src:
        by_src[src].sort(key=lambda r: int(r["seed_rank_within_source"]))

    validity = {}
    for line in open(VALIDITY, encoding="utf-8"):
        e = json.loads(line)
        validity[(e["source"], e["seed_rank"])] = e
    assert len(validity) == 104, len(validity)

    cand = {}
    for line in open(CANDIDATES, encoding="utf-8"):
        it = json.loads(line)
        assert list(it.keys()) == ITEM_KEYS, it["item_id"]
        cand[it["item_id"]] = it
    disc_ids = {json.loads(l)["item_id"] for l in open(DISCOVERY, encoding="utf-8")}

    # --- selection: first TARGET[source] valid groups in seed order --------
    selected = {"fever": [], "scifact": []}
    for src in TARGET:
        for row in by_src[src]:
            rank = int(row["seed_rank_within_source"])
            v = validity.get((src, rank))
            if v is None:
                break  # consulted range exhausted before stratum full
            if v["verdict"] == "valid":
                selected[src].append((row, v))
            if len(selected[src]) == TARGET[src]:
                break
        assert len(selected[src]) == TARGET[src], (src, len(selected[src]))

    # --- build items -------------------------------------------------------
    out_lines = []
    for src in ("fever", "scifact"):
        for row, v in selected[src]:
            for key, want_dir in (("inc_item_id", "increase"),
                                  ("dec_item_id", "decrease")):
                base = cand[row[key]]
                it = json.loads(json.dumps(base))  # deep copy
                assert it["critical_direction"] == want_dir, it["item_id"]
                assert it["task_family"] == f"g24a_{src}", it["task_family"]
                assert it["admit_rule"] == g24a.ADMIT_RULE, it["item_id"]
                assert it["exclude_rule"] == g24a.EXCLUDE_RULE, it["item_id"]
                meta = it["meta"]
                if isinstance(meta, str):
                    meta = ast.literal_eval(meta)
                assert isinstance(meta, dict)
                meta["pilot"] = "g24a_p1"
                meta["group_sha"] = row["group_sha"]
                meta["group_seed_rank"] = int(row["seed_rank_within_source"])
                meta["group_role"] = v["role"]
                meta["validity_note"] = v["note"]
                it["meta"] = meta
                assert list(it.keys()) == ITEM_KEYS, it["item_id"]
                out_lines.append(it)

    with open(OUT, "w", encoding="utf-8") as fh:
        for it in out_lines:
            fh.write(json.dumps(it, ensure_ascii=False) + "\n")

    # --- read-back verification -------------------------------------------
    back = [json.loads(l) for l in open(OUT, encoding="utf-8")]
    assert len(back) == 192, len(back)
    ids = [it["item_id"] for it in back]
    assert len(set(ids)) == 192, "duplicate item ids"
    assert not (set(ids) & disc_ids), "item id overlaps discovery 600"
    by_group = {}
    for it in back:
        assert isinstance(it["meta"], dict) and it["meta"]["pilot"] == "g24a_p1"
        by_group.setdefault(it["meta"]["group_sha"], []).append(it)
    assert len(by_group) == 96, len(by_group)
    strata = Counter(g[0]["task_family"] for g in by_group.values())
    assert strata == {"g24a_fever": 64, "g24a_scifact": 32}, strata
    for sha, g in by_group.items():
        assert len(g) == 2, sha
        dirs = sorted(i["critical_direction"] for i in g)
        assert dirs == ["decrease", "increase"], sha
        assert g[0]["critical_evidence"] == g[1]["critical_evidence"], sha
        roles = {i["meta"]["group_role"] for i in g}
        assert len(roles) == 1, sha
        assert validity_entry_matches(validity, g), sha

    print(f"wrote {OUT}: 192 items / 96 groups "
          f"(64 fever + 32 scifact; all verdicts valid; "
          f"0 id overlap with discovery; meta is a JSON object)")
    return 0


def validity_entry_matches(validity, group):
    it = group[0]
    src = it["task_family"].split("_")[1]
    e = validity[(src, it["meta"]["group_seed_rank"])]
    return e["verdict"] == "valid" and e["group_sha"] == it["meta"]["group_sha"] \
        and e["role"] == it["meta"]["group_role"]


if __name__ == "__main__":
    raise SystemExit(main())
