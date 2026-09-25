#!/usr/bin/env python3
"""Pre-run verification for Confirmation-A prompts (zero model output read).

Checks, for all 500 items x 5 conditions = 2,500 prompts:
  1. KINDS == schema.CONDITIONS == g24a.G24A_CONDITIONS (the G0 five, no
     probe kinds, no mechanism cells - §13.2)
  2. compile_prompt succeeds; TASK tail present (question + output spec)
  3. item-level identical text: admit_rule == ADMIT_RULE, exclude_rule ==
     EXCLUDE_RULE, question/output_spec == module constants (§9.1
     identical-text guarantee)
  4. block order: base = CLAIM only (no EVIDENCE, no RULING); pre cells
     CLAIM -> RULING -> EVIDENCE; post cells CLAIM -> EVIDENCE -> RULING
  5. rulings appear VERBATIM; base rule_char_offset is None, rule cells
     point at the RULING block
  6. unmodified module: schema._blocks(it, k) == g24a.blocks(it, k) for
     EVERY item x condition (all five cells render through the *unmodified*
     G24A module by construction)
  7. pre/post arms carry the identical block multiset - position of the
     rule relative to the evidence is the only difference
  8. kind whitelist: all five pass run_model's union membership chain and
     are not probes
  9. data integrity: ids file == file order; every item's
     (source, seed_rank) resolves to its pool row with matching item_id /
     claim_sha / evidence / direction; blind call agrees with direction
     (S & increase, R & decrease); 0 id-overlap with every other rendered
     item file
 10. regression: a G24A discovery item still compiles all five conditions
     unchanged; no dispatch collision with g24p1 / g25 / g26

Usage: python scripts/verify_g24a_confa_prompts.py   (exit 0 = all pass)
"""
from __future__ import annotations

import csv
import glob
import hashlib
import json
import os
import re
import sys
from collections import Counter

ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, os.path.join(ROOT, "src"))

import schema                                   # noqa: E402
import conditions_g24a as g24a                  # noqa: E402
import conditions_g24p1 as g24p1                # noqa: E402
import conditions_g25 as g25                    # noqa: E402
import conditions_g26a as g26                   # noqa: E402

ITEMS = os.path.join(ROOT, "data", "items", "g24a_confa_v1.jsonl")
IDS = os.path.join(ROOT, "data", "items", "g24a_confa_ids.json")
POOL = os.path.join(ROOT, "data", "items", "g24a_confa_pool_v1.csv")
VALIDITY = os.path.join(ROOT, "data", "items", "g24a_confa_validity_v1.jsonl")
RESERVE_VALIDITY = os.path.join(
    ROOT, "data", "items", "g24a_confa_reserve_validity_v1.jsonl")
DISCOVERY = os.path.join(ROOT, "data", "items", "g24a_v1.jsonl")
CANDIDATES = os.path.join(ROOT, "data", "items",
                          "g24a_candidates_v1.jsonl")
KINDS = ["base", "admit_pre", "admit_post", "exclude_pre", "exclude_post"]
PRE = {"admit_pre", "exclude_pre"}


def norm_claim(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().casefold().rstrip(" .")


def main() -> int:
    assert KINDS == schema.CONDITIONS == g24a.G24A_CONDITIONS, \
        (KINDS, schema.CONDITIONS, g24a.G24A_CONDITIONS)

    items = schema.load_items(ITEMS)
    assert len(items) == 500, len(items)
    fam = Counter(it.task_family for it in items)
    assert fam == Counter({"g24a_fever": 334, "g24a_scifact": 166}), fam

    # ---- per item x condition -------------------------------------------
    n = 0
    for it in items:
        assert it.admit_rule == g24a.ADMIT_RULE, it.item_id
        assert it.exclude_rule == g24a.EXCLUDE_RULE, it.item_id
        assert it.question == g24a.QUESTION, it.item_id
        assert it.output_spec == g24a.OUTPUT_SPEC, it.item_id
        for k in KINDS:
            p = schema.compile_prompt(it, k)
            assert "TASK\n" + it.question in p, (it.item_id, k)
            assert it.output_spec in p, (it.item_id, k)
            off = schema.rule_char_offset(it, k)
            assert schema._blocks(it, k) == g24a.blocks(it, k), (it.item_id, k)
            if k == "base":
                assert off is None, (it.item_id, k, off)
                assert "RULING" not in p, (it.item_id, k)
                assert "EVIDENCE E" not in p, (it.item_id, k)
                assert p.index("CLAIM\n") < p.index("TASK\n")
            else:
                assert off is not None and off > 0, (it.item_id, k, off)
                want = (g24a.ADMIT_RULE if k.startswith("admit")
                        else g24a.EXCLUDE_RULE)
                assert want in p, (it.item_id, k)
                i_c = p.index("CLAIM\n")
                i_e = p.index("EVIDENCE E\n")
                i_r = p.index("RULING\n")
                if k in PRE:
                    assert i_c < i_r < i_e, (it.item_id, k, i_c, i_r, i_e)
                else:
                    assert i_c < i_e < i_r, (it.item_id, k, i_c, i_e, i_r)
            n += 1
    assert n == 2500, n

    # ---- pre/post arms: identical multiset, order is the only difference --
    it = items[0]
    b_pre, b_post = (schema._blocks(it, k) for k in
                     ("admit_pre", "admit_post"))
    assert sorted(b_pre) == sorted(b_post), "admit arms differ in content"
    b_pre, b_post = (schema._blocks(it, k) for k in
                     ("exclude_pre", "exclude_post"))
    assert sorted(b_pre) == sorted(b_post), "exclude arms differ in content"

    # ---- kind whitelist ---------------------------------------------------
    lists = [schema.CONDITIONS, schema.EXTRA_CONDITIONS, schema.V2_CONDITIONS,
             schema.V3_CONDITIONS, schema.V4_CONDITIONS, schema.ROUTING_CONDITIONS,
             schema.V5_CONDITIONS, schema.LINEAR_CONDITIONS, schema.V6_CONDITIONS,
             schema.V7_CONDITIONS, schema.G17_CONDITIONS, schema.G18_CONDITIONS,
             schema.G23A_CONDITIONS, schema.G23B_CONDITIONS, schema.G25A_CONDITIONS,
             schema.G26A_CONDITIONS, schema.G24P1_CONDITIONS, schema.AGENT_CONDITIONS,
             schema.EXT_CONDITIONS, schema.PROBES]
    for k in KINDS:
        assert any(k in lst for lst in lists), f"{k} not in run_model whitelist"
        assert k not in schema.PROBES, f"{k} must not be a probe kind"
        assert not g24p1.is_g24p1(k), (k, "g24p1 collision")
        assert not g25.is_g25(k), (k, "g25 collision")
        assert not g26.is_g26(k), (k, "g26 collision")

    # ---- data integrity: ids / pool / validity / freshness ---------------
    ids = json.load(open(IDS, encoding="utf-8"))
    assert ids == [it.item_id for it in items], "ids file order mismatch"
    assert len(set(ids)) == 500

    pool = {(r["source"], int(r["seed_rank_within_source"])): r
            for r in csv.DictReader(open(POOL, newline="", encoding="utf-8"))}
    verdicts = {}
    for path in (VALIDITY, RESERVE_VALIDITY):
        for line in open(path, encoding="utf-8"):
            d = json.loads(line)
            verdicts[(d["source"], d["seed_rank"])] = d["call"]

    for it in items:
        m = it.meta
        assert m["pilot"] == "g24a_confa", it.item_id
        src = it.task_family.replace("g24a_", "")
        row = pool[(src, m["confa_seed_rank"])]
        assert row["item_id"] == it.item_id, it.item_id
        assert row["direction"] == it.critical_direction, it.item_id
        assert hashlib.sha256(
            norm_claim(it.base_context).encode()).hexdigest()[:12] \
            == row["claim_sha"], it.item_id
        assert row["evidence"] == it.critical_evidence, it.item_id
        call = verdicts[(src, m["confa_seed_rank"])]
        assert call == m["blind_call"], it.item_id
        assert ((call == "S" and it.critical_direction == "increase")
                or (call == "R" and it.critical_direction == "decrease")), \
            it.item_id
        if m["confa_role"] == "reserve":
            assert "confa_replaced_seed_rank" in m, it.item_id

    # 0 id-overlap with every other rendered item file
    other_ids = set()
    for f in sorted(glob.glob(os.path.join(ROOT, "data", "items", "*.jsonl"))):
        if f in (ITEMS, CANDIDATES):
            continue
        first = open(f, encoding="utf-8").readline()
        if "item_id" not in json.loads(first):
            continue
        for line in open(f, encoding="utf-8"):
            other_ids.add(json.loads(line)["item_id"])
    assert not (set(ids) & other_ids), "id overlaps a rendered item file"

    # ---- regression: discovery item, all five conditions unchanged --------
    disc = schema.load_items(DISCOVERY)
    for k in KINDS:
        assert schema._blocks(disc[0], k) == g24a.blocks(disc[0], k), k
        schema.compile_prompt(disc[0], k)

    print(f"OK: {n} prompts verified (500 items x {len(KINDS)} conditions); "
          "wordings verbatim, G24A module untouched, pre/post arms "
          "multiset-identical, whitelist passes, pool/validity/freshness "
          "integrity holds")
    print(f"ruling lengths (words): admit={len(g24a.ADMIT_RULE.split())}, "
          f"exclude={len(g24a.EXCLUDE_RULE.split())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
