#!/usr/bin/env python3
"""Build the Pilot P2 item file: 200 valid claims x 2 arms = 400 items.

Inputs (all committed before any model run):
  data/items/g24a_p2_pool_v1.csv         - active 200 + reserve 80, seed order
  data/items/g24a_p2_validity_v1.jsonl   - 262 consulted, my verdicts

Selection rule (fixed before reading anything): every validity entry with
verdict "valid" — 156 surviving actives + 44 replacement reserves = 200
claims — in seed order.  The k-th invalid active is already paired with the
k-th valid reserve inside the validity file; the build only takes the valid
set and cross-checks that every invalid active's replaced_by_p2_id is in it.

Item construction (arm matrix, prereg §9):
  arm+ item : critical_evidence = evidence_s (natural SUPPORT), direction
              increase
  arm- item : critical_evidence = evidence_r (natural REFUTE), direction
              decrease
  shared     : base_context = the claim; question / output_spec / ADMIT /
              EXCLUDE wording taken from the unmodified G24A module, so the
              two arms differ in NOTHING but which evidence block is
              rendered, and `base` (claim only, evidence-free) compiles
              byte-identical across arms — Y0 is the same number by
              construction.

task_family is "g24a_vitaminc": registered into G24A_TASK_FAMILIES so
base / admit_post / exclude_post render through the *unmodified* G24A
module (character-identical prompts by construction); the two P1 operators
already dispatch on condition name inside schema._blocks, unchanged.

Also writes the frozen arm id lists used by the two-invocation run:
  data/items/g24a_p2_ids_plus.json   (200 ids, kinds = all 5, incl. base)
  data/items/g24a_p2_ids_minus.json  (200 ids, kinds = 4, no base)

Output: data/items/g24a_p2_v1.jsonl (400 lines).

Usage: python scripts/build_g24a_p2_items.py
"""
from __future__ import annotations

import csv
import json
import os
import sys
from pathlib import Path

POOL_CSV = "data/items/g24a_p2_pool_v1.csv"
VALIDITY = "data/items/g24a_p2_validity_v1.jsonl"
OUT = "data/items/g24a_p2_v1.jsonl"
IDS_PLUS = "data/items/g24a_p2_ids_plus.json"
IDS_MINUS = "data/items/g24a_p2_ids_minus.json"
DISCOVERY = "data/items/g24a_v1.jsonl"
P1_ITEMS = "data/items/g24a_p1_v1.jsonl"
TASK_FAMILY = "g24a_vitaminc"

ITEM_KEYS = [
    "item_id", "task_family", "surface_domain", "base_context",
    "critical_evidence", "critical_label", "critical_direction",
    "exclusion_reason", "evidence_truth", "admit_rule", "exclude_rule",
    "question", "output_spec", "memory_question", "rule_probe_question",
    "ground_truth", "meta",
]


def main() -> int:
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
    import schema
    import conditions_g24a as g24a

    pool = {r["p2_id"]: r for r in
            csv.DictReader(open(POOL_CSV, newline="", encoding="utf-8"))}
    assert len(pool) == 280, len(pool)

    validity = [json.loads(l) for l in open(VALIDITY, encoding="utf-8")]
    assert len(validity) == 262, len(validity)
    valid = [e for e in validity if e["verdict"] == "valid"]
    invalid = [e for e in validity if e["verdict"] == "invalid"]
    assert (len(valid), len(invalid)) == (200, 62), (len(valid), len(invalid))
    assert len({e["p2_id"] for e in valid}) == 200
    assert sum(e["role"] == "active" for e in valid) == 156
    assert sum(e["role"] == "reserve" for e in valid) == 44
    # every invalid ACTIVE's replacement is in the valid set (chains complete)
    valid_ids = {e["p2_id"] for e in valid}
    for e in invalid:
        if e["role"] == "active":
            assert e["replaced_by_p2_id"] in valid_ids, e
        else:
            assert e["p2_id"] not in valid_ids

    # --- build items -------------------------------------------------------
    out_lines = []
    for e in valid:
        row = pool[e["p2_id"]]
        assert row["claim_sha"] == e["claim_sha"], e["p2_id"]
        claim, es, er = row["claim"], row["evidence_s"], row["evidence_r"]
        assert claim and es and er and es != er, e["p2_id"]
        for arm, ev, want_dir in (("plus", es, "increase"),
                                  ("minus", er, "decrease")):
            it = {
                "item_id": f"{e['p2_id']}_{arm}",
                "task_family": TASK_FAMILY,
                "surface_domain": "wikipedia",
                "base_context": claim,
                "critical_evidence": ev,
                "critical_label": "evidence E",
                "critical_direction": want_dir,
                "exclusion_reason": g24a.EXCLUSION_REASON,
                "evidence_truth": g24a.EVIDENCE_TRUTH,
                "admit_rule": g24a.ADMIT_RULE,
                "exclude_rule": g24a.EXCLUDE_RULE,
                "question": g24a.QUESTION,
                "output_spec": g24a.OUTPUT_SPEC,
                "memory_question": g24a.MEMORY_QUESTION,
                "rule_probe_question": g24a.RULE_PROBE_QUESTION,
                "ground_truth": None,
                "meta": {
                    "pilot": "g24a_p2",
                    "p2_id": e["p2_id"],
                    "case_id": e["case_id"],
                    "claim_sha": e["claim_sha"],
                    "arm": arm,
                    "evidence_field": "evidence_s" if arm == "plus" else "evidence_r",
                    "p2_role": e["role"],
                    "validity_note": e["note"],
                    "seed_rank": e["seed_rank"],
                    "split": row["split"],
                    "page": row["page"],
                    "first_lineno": int(row["first_lineno"]),
                },
            }
            assert list(it.keys()) == ITEM_KEYS, it["item_id"]
            out_lines.append(it)

    with open(OUT, "w", encoding="utf-8") as fh:
        for it in out_lines:
            fh.write(json.dumps(it, ensure_ascii=False) + "\n")

    ids_plus = [it["item_id"] for it in out_lines if it["meta"]["arm"] == "plus"]
    ids_minus = [it["item_id"] for it in out_lines if it["meta"]["arm"] == "minus"]
    Path(IDS_PLUS).write_text(json.dumps(ids_plus, indent=1) + "\n")
    Path(IDS_MINUS).write_text(json.dumps(ids_minus, indent=1) + "\n")

    # --- read-back verification -------------------------------------------
    items = schema.load_items(OUT)
    assert len(items) == 400, len(items)
    assert len({i.item_id for i in items}) == 400, "duplicate item ids"
    disc_ids = {json.loads(l)["item_id"] for l in open(DISCOVERY, encoding="utf-8")}
    p1_ids = {json.loads(l)["item_id"] for l in open(P1_ITEMS, encoding="utf-8")}
    assert not ({i.item_id for i in items} & (disc_ids | p1_ids)), "id overlap"

    groups = {}
    for it in items:
        assert it.task_family == TASK_FAMILY, it.item_id
        assert schema._blocks is not None
        import conditions_g24a as g
        assert g.is_g24a(it), it.item_id  # routes to the unmodified G24A module
        assert it.admit_rule == g.ADMIT_RULE, it.item_id
        assert it.exclude_rule == g.EXCLUDE_RULE, it.item_id
        assert it.question == g.QUESTION and it.output_spec == g.OUTPUT_SPEC
        assert isinstance(it.meta, dict) and it.meta["pilot"] == "g24a_p2"
        groups.setdefault(it.meta["p2_id"], []).append(it)

    assert len(groups) == 200, len(groups)
    n_base = 0
    for p2_id, g in groups.items():
        assert len(g) == 2, p2_id
        by_arm = {i.meta["arm"]: i for i in g}
        assert set(by_arm) == {"plus", "minus"}, p2_id
        pm, mm = by_arm["plus"], by_arm["minus"]
        # shared claim / question / rulings: the ONLY difference is the evidence
        assert pm.base_context == mm.base_context, p2_id
        assert pm.question == mm.question and pm.output_spec == mm.output_spec, p2_id
        assert pm.admit_rule == mm.admit_rule and pm.exclude_rule == mm.exclude_rule, p2_id
        assert pm.critical_evidence != mm.critical_evidence, p2_id
        assert pm.meta["claim_sha"] == mm.meta["claim_sha"], p2_id
        assert pm.critical_direction == "increase", p2_id
        assert mm.critical_direction == "decrease", p2_id
        # the base prompt (claim only) is byte-identical across arms -> shared Y0
        p_plus = schema.compile_prompt(pm, "base")
        p_minus = schema.compile_prompt(mm, "base")
        assert p_plus == p_minus, f"base prompt differs across arms: {p2_id}"
        assert "EVIDENCE E\n" not in p_plus, f"base not evidence-free: {p2_id}"
        n_base += 1
        # each evidence-bearing prompt renders its OWN arm's evidence block
        for cond in ("admit_post", "exclude_post", "strong_exclude_post",
                     "counterfactual_delete_post"):
            for item in (pm, mm):
                p = schema.compile_prompt(item, cond)
                got = (p.split("EVIDENCE E\n", 1)[1]
                       .split("\n\nRULING\n", 1)[0])
                assert got == item.critical_evidence, (item.item_id, cond)
                assert "TASK\n" + item.question in p, (item.item_id, cond)
    assert n_base == 200, n_base

    # frozen arm id lists for the two-invocation run
    plus = json.loads(Path(IDS_PLUS).read_text())
    minus = json.loads(Path(IDS_MINUS).read_text())
    assert len(plus) == len(minus) == 200, (len(plus), len(minus))
    assert not (set(plus) & set(minus))
    assert set(plus) | set(minus) == {i.item_id for i in items}

    print(f"wrote {OUT}: 400 items / 200 claims (156 active + 44 reserve), "
          f"task_family={TASK_FAMILY}, base prompt byte-identical across arms "
          f"(shared Y0), evidence block exact per arm")
    print(f"wrote {IDS_PLUS} + {IDS_MINUS}: 200 ids each, disjoint, union=400")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
