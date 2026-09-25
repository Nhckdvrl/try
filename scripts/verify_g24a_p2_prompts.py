#!/usr/bin/env python3
"""Pre-run verification for Pilot P2 prompts (zero model output read).

Checks, for all 400 items x 5 conditions = 2,000 prompts:

  1. compile_prompt succeeds; TASK tail present (question + output spec +
     answer format)
  2. block order CLAIM -> EVIDENCE E -> RULING for the four rule conditions;
     base has no RULING
  3. the two new rulings appear VERBATIM (independent hard-coded copy of
     the user's 2026-09-25 spec; a typo in the module fails this)
  4. base / admit_post / exclude_post on P2 items are byte-identical to
     conditions_g24a.blocks output (they render through the unmodified G24A
     module; task_family "g24a_vitaminc" is dispatch-only)
  5. within one item, exclude_post / strong_exclude_post /
     counterfactual_delete_post share identical prefix (claim+evidence)
     and identical suffix (TASK tail) - the ruling string is the only
     difference
  6. rule_char_offset: None for base, points at the RULING block otherwise
  7. the 5 condition names pass run_model's kind whitelist
  8. no probe kinds in the pilot's kind set (9,000 decision rows only)
  9. item-level identical-text: admit_rule == ADMIT_RULE,
     exclude_rule == EXCLUDE_RULE, question/output_spec == module constants
 10. regression: a G24A discovery item still compiles all five G0
     conditions unchanged; no new condition name collides with g25/g26

Arm-matrix contracts (prereg §9; the properties that make the 9-cell design
estimable):

 11. group structure: 200 claims x exactly 2 arms (plus/minus), unique ids
 12. shared claim block: within a claim the two arms are identical in
     base_context, question, output_spec, admit_rule, exclude_rule -
     only critical_evidence / critical_direction differ
 13. shared Y0: the base prompt (claim only) is BYTE-IDENTICAL across arms
     for every claim, and contains no EVIDENCE E block - so Y0 is one
     number by construction and the arm- run may omit base
 14. exact evidence per arm: for each of the four evidence-bearing
     conditions, the rendered EVIDENCE E block equals that arm's own
     evidence_s (plus) / evidence_r (minus) byte-for-byte
 15. arm id lists: ids_plus / ids_minus are disjoint, cover all 400 items,
     and their sizes match the run contract (arm+ x 5 kinds incl. base,
     arm- x 4 kinds excl. base) - base is never issued on arm-

Prints ruling word counts (rough length parity between the two new
operators; no token-matching filler is asserted - exploratory design).

Usage: python scripts/verify_g24a_p2_prompts.py   (exit 0 = all pass)
"""
from __future__ import annotations

import json
import os
import sys

ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, os.path.join(ROOT, "src"))

import schema                                   # noqa: E402
import conditions_g24a as g24a                  # noqa: E402
import conditions_g24p1 as g24p1                # noqa: E402
import conditions_g25 as g25                    # noqa: E402
import conditions_g26a as g26                   # noqa: E402

ITEMS = os.path.join(ROOT, "data", "items", "g24a_p2_v1.jsonl")
IDS_PLUS = os.path.join(ROOT, "data", "items", "g24a_p2_ids_plus.json")
IDS_MINUS = os.path.join(ROOT, "data", "items", "g24a_p2_ids_minus.json")
DISCOVERY = os.path.join(ROOT, "data", "items", "g24a_v1.jsonl")
VALIDITY = os.path.join(ROOT, "data", "items", "g24a_p2_validity_v1.jsonl")

# The run contract (frozen here; scripts/run_g24a_p2.sh mirrors it): base
# runs on arm+ only, the four evidence-bearing kinds run on both arms.
KINDS_PLUS = ["base", "admit_post", "exclude_post",
              "strong_exclude_post", "counterfactual_delete_post"]
KINDS_MINUS = ["admit_post", "exclude_post",
               "strong_exclude_post", "counterfactual_delete_post"]

# Independent copy of the user's verbatim wordings (2026-09-25).  If the
# module drifts from the spec, this comparison fails.
SPEC_STRONG = ("Evidence E is inadmissible. Completely disregard it when "
               "judging the claim. It must have no influence on your "
               "judgment in either direction, directly or indirectly. "
               "Judge the claim using only information available without "
               "relying on Evidence E.")
SPEC_CF = ("Evaluate the claim exactly as you would have if Evidence E had "
           "never been shown. Reconstruct the judgment you would have made "
           "before encountering Evidence E. Evidence E must have no "
           "influence on the answer in either direction, directly or "
           "indirectly.")


def main() -> int:
    assert g24p1.STRONG_EXCLUDE_RULE == SPEC_STRONG, "strong wording drifted"
    assert g24p1.CF_DELETE_RULE == SPEC_CF, "counterfactual wording drifted"
    assert KINDS_PLUS[3:] == g24p1.G24P1_CONDITIONS
    assert "base" not in KINDS_MINUS, KINDS_MINUS
    assert KINDS_MINUS == KINDS_PLUS[1:], "run contract drift"

    items = schema.load_items(ITEMS)
    assert len(items) == 400, len(items)

    n = 0
    for it in items:
        assert it.task_family == "g24a_vitaminc", it.item_id
        assert g24a.is_g24a(it), it.item_id
        assert it.admit_rule == g24a.ADMIT_RULE, it.item_id
        assert it.exclude_rule == g24a.EXCLUDE_RULE, it.item_id
        assert it.question == g24a.QUESTION, it.item_id
        assert it.output_spec == g24a.OUTPUT_SPEC, it.item_id
        assert it.meta["pilot"] == "g24a_p2", it.item_id
        for k in KINDS_PLUS:
            p = schema.compile_prompt(it, k)
            assert "TASK\n" + it.question in p, (it.item_id, k)
            assert it.output_spec in p, (it.item_id, k)
            off = schema.rule_char_offset(it, k)
            if k == "base":
                assert off is None, (it.item_id, k, off)
                assert "RULING" not in p, (it.item_id, k)
                assert "EVIDENCE E\n" not in p, (it.item_id, k, "base not evidence-free")
            else:
                assert off is not None and off > 0, (it.item_id, k, off)
                i_c = p.index("CLAIM\n")
                i_e = p.index("EVIDENCE E\n")
                i_r = p.index("RULING\n")
                assert i_c < i_e < i_r, (it.item_id, k, i_c, i_e, i_r)
                # exact per-arm evidence block (14)
                got = p.split("EVIDENCE E\n", 1)[1].split("\n\nRULING\n", 1)[0]
                assert got == it.critical_evidence, (it.item_id, k)
            if k in ("strong_exclude_post", "counterfactual_delete_post"):
                want = (g24p1.STRONG_EXCLUDE_RULE
                        if k == "strong_exclude_post" else g24p1.CF_DELETE_RULE)
                assert want in p, (it.item_id, k)
            # the three G24A conditions must be rendered by the unmodified
            # G24A module - byte-identical block lists
            if k in ("base", "admit_post", "exclude_post"):
                assert schema._blocks(it, k) == g24a.blocks(it, k), (it.item_id, k)
            n += 1
    assert n == 2000, n

    # ruling is the ONLY difference between the three post operators:
    # identical prefix through the evidence block, identical TASK tail
    it = items[0]
    ps = {k: schema.compile_prompt(it, k)
          for k in ("exclude_post", "strong_exclude_post",
                    "counterfactual_delete_post")}
    heads = [p[:p.index("RULING\n")] for p in ps.values()]
    assert heads[0] == heads[1] == heads[2], "prefix differs"
    tails = [p[p.index("TASK\n"):] for p in ps.values()]
    assert tails[0] == tails[1] == tails[2], "tail differs"
    rulings = {k: p[p.index("RULING\n"):p.index("TASK\n")] for k, p in ps.items()}
    assert len(set(rulings.values())) == 3, "rulings not distinct"

    # kind whitelist: every pilot kind must be in the lists unioned by
    # run_model's membership chain
    lists = [schema.CONDITIONS, schema.EXTRA_CONDITIONS, schema.V2_CONDITIONS,
             schema.V3_CONDITIONS, schema.V4_CONDITIONS, schema.ROUTING_CONDITIONS,
             schema.V5_CONDITIONS, schema.LINEAR_CONDITIONS, schema.V6_CONDITIONS,
             schema.V7_CONDITIONS, schema.G17_CONDITIONS, schema.G18_CONDITIONS,
             schema.G23A_CONDITIONS, schema.G23B_CONDITIONS, schema.G25A_CONDITIONS,
             schema.G26A_CONDITIONS, schema.G24P1_CONDITIONS, schema.AGENT_CONDITIONS,
             schema.EXT_CONDITIONS, schema.PROBES]
    for k in KINDS_PLUS:
        assert any(k in lst for lst in lists), f"{k} not in run_model whitelist"
        assert k not in schema.PROBES, f"{k} must not be a probe kind"

    # regression: G24A discovery item unchanged for all five G0 conditions
    disc = schema.load_items(DISCOVERY)
    for k in ["base", "admit_pre", "admit_post", "exclude_pre", "exclude_post"]:
        assert schema._blocks(disc[0], k) == g24a.blocks(disc[0], k), k
        schema.compile_prompt(disc[0], k)
    # no name collisions
    for k in ["base", "exclude_post", "g25_w000_post", "g26_admit_t0"]:
        assert not g24p1.is_g24p1(k), k
    assert not g25.is_g25("strong_exclude_post")
    assert not g26.is_g26("strong_exclude_post")
    assert not g26.is_g26("counterfactual_delete_post")

    # --- arm-matrix contracts (11-15) ------------------------------------
    groups: dict[str, dict[str, schema.Item]] = {}
    for it in items:
        arm = it.meta["arm"]
        assert arm in ("plus", "minus"), it.item_id
        groups.setdefault(it.meta["p2_id"], {})[arm] = it
    assert len(groups) == 200, len(groups)
    for p2_id, arms in groups.items():
        assert set(arms) == {"plus", "minus"}, p2_id
        pm, mm = arms["plus"], arms["minus"]
        # shared claim block: identical except the evidence itself (12)
        assert pm.base_context == mm.base_context, p2_id
        assert pm.question == mm.question and pm.output_spec == mm.output_spec, p2_id
        assert pm.admit_rule == mm.admit_rule and pm.exclude_rule == mm.exclude_rule, p2_id
        assert pm.critical_evidence != mm.critical_evidence, p2_id
        assert (pm.critical_direction, mm.critical_direction) == ("increase", "decrease"), p2_id
        # shared Y0: base prompt byte-identical, evidence-free (13)
        assert schema.compile_prompt(pm, "base") == schema.compile_prompt(mm, "base"), \
            f"base differs across arms: {p2_id}"
    # every claim's validity entry is "valid" (run set = 200 unique claims)
    val = [json.loads(l) for l in open(VALIDITY, encoding="utf-8")]
    assert len(val) == 262, len(val)
    valid_ids = {e["p2_id"] for e in val if e["verdict"] == "valid"}
    assert valid_ids == set(groups), "item claims != validity run set"

    # arm id lists (15): disjoint, covering, and sized for the run contract
    ids_plus = json.load(open(IDS_PLUS))
    ids_minus = json.load(open(IDS_MINUS))
    all_ids = {it.item_id for it in items}
    assert len(ids_plus) == len(ids_minus) == 200, (len(ids_plus), len(ids_minus))
    assert not (set(ids_plus) & set(ids_minus)), "arm id lists overlap"
    assert set(ids_plus) | set(ids_minus) == all_ids, "arm id lists do not cover items"
    assert all(i.endswith("_plus") for i in ids_plus), ids_plus[:3]
    assert all(i.endswith("_minus") for i in ids_minus), ids_minus[:3]
    # base is a plus-only kind by contract: for every minus item the base
    # prompt exists and equals its plus twin (so omitting it loses no rows)
    for p2_id, arms in groups.items():
        assert arms["minus"].item_id in set(ids_minus), p2_id
        assert schema.compile_prompt(arms["minus"], "base") == \
            schema.compile_prompt(arms["plus"], "base"), p2_id

    print(f"OK: {n} prompts verified (400 items x {len(KINDS_PLUS)} conditions), "
          f"wordings verbatim, G24A conditions untouched, whitelist passes")
    print(f"arm matrix: 200 claims x 2 arms; shared claim block; base "
          f"byte-identical across arms (shared Y0); evidence block exact per arm")
    print(f"run contract: arm+ = {len(ids_plus)} ids x {len(KINDS_PLUS)} kinds "
          f"(incl. base), arm- = {len(ids_minus)} ids x {len(KINDS_MINUS)} kinds "
          f"(base never issued on arm-); rows/model = "
          f"{len(ids_plus) * len(KINDS_PLUS) + len(ids_minus) * len(KINDS_MINUS)}")
    print("ruling lengths (words): "
          f"exclude_post={len(g24a.EXCLUDE_RULE.split())}, "
          f"strong={len(g24p1.STRONG_EXCLUDE_RULE.split())}, "
          f"cfdelete={len(g24p1.CF_DELETE_RULE.split())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
