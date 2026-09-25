#!/usr/bin/env python3
"""Pre-run verification for Pilot P1 prompts (zero model output read).

Checks, for all 192 items x 5 conditions = 960 prompts:
  1. compile_prompt succeeds; TASK tail present (question + output spec +
     answer format)
  2. block order CLAIM -> EVIDENCE E -> RULING for the four rule conditions;
     base has no RULING
  3. the two new rulings appear VERBATIM (independent hard-coded copy of
     the user's 2026-09-25 spec; a typo in the module fails this)
  4. base / admit_post / exclude_post on P1 items are byte-identical to
     conditions_g24a.blocks output (they must NOT be hijacked by the new
     name-dispatch branch; they render through the unmodified G24A module)
  5. within one item, exclude_post / strong_exclude_post /
     counterfactual_delete_post share identical prefix (claim+evidence)
     and identical suffix (TASK tail) - the ruling string is the only
     difference
  6. rule_char_offset: None for base, points at the RULING block otherwise
  7. the 5 condition names pass run_model's kind whitelist (membership in
     the exported condition lists that its `or` chain unions)
  8. no probe kinds in the pilot's kind set (4,800 decision rows only)
  9. item-level identical-text: admit_rule == ADMIT_RULE,
     exclude_rule == EXCLUDE_RULE for every item
 10. regression: a G24A discovery item still compiles all five G0
     conditions unchanged; no new condition name collides with g25/g26

Prints ruling word counts (rough length parity between the two new
operators; no token-matching filler is asserted - exploratory design).

Usage: python scripts/verify_g24a_p1_prompts.py   (exit 0 = all pass)
"""
from __future__ import annotations

import os
import sys

ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, os.path.join(ROOT, "src"))

import schema                                   # noqa: E402
import conditions_g24a as g24a                  # noqa: E402
import conditions_g24p1 as g24p1                # noqa: E402
import conditions_g25 as g25                    # noqa: E402
import conditions_g26a as g26                   # noqa: E402

ITEMS = os.path.join(ROOT, "data", "items", "g24a_p1_v1.jsonl")
DISCOVERY = os.path.join(ROOT, "data", "items", "g24a_v1.jsonl")
KINDS = ["base", "admit_post", "exclude_post",
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
    assert KINDS[3:] == g24p1.G24P1_CONDITIONS

    items = schema.load_items(ITEMS)
    assert len(items) == 192, len(items)

    n = 0
    for it in items:
        assert it.admit_rule == g24a.ADMIT_RULE, it.item_id
        assert it.exclude_rule == g24a.EXCLUDE_RULE, it.item_id
        for k in KINDS:
            p = schema.compile_prompt(it, k)
            assert "TASK\n" + it.question in p, (it.item_id, k)
            assert it.output_spec in p, (it.item_id, k)
            off = schema.rule_char_offset(it, k)
            if k == "base":
                assert off is None, (it.item_id, k, off)
                assert "RULING" not in p, (it.item_id, k)
            else:
                assert off is not None and off > 0, (it.item_id, k, off)
                i_c = p.index("CLAIM\n")
                i_e = p.index("EVIDENCE E\n")
                i_r = p.index("RULING\n")
                assert i_c < i_e < i_r, (it.item_id, k, i_c, i_e, i_r)
            if k in ("strong_exclude_post", "counterfactual_delete_post"):
                want = (g24p1.STRONG_EXCLUDE_RULE
                        if k == "strong_exclude_post" else g24p1.CF_DELETE_RULE)
                assert want in p, (it.item_id, k)
            # the three G24A conditions must be rendered by the unmodified
            # G24A module - byte-identical block lists
            if k in ("base", "admit_post", "exclude_post"):
                assert schema._blocks(it, k) == g24a.blocks(it, k), (it.item_id, k)
            n += 1
    assert n == 960, n

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
    for k in KINDS:
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

    print(f"OK: {n} prompts verified "
          f"(192 items x {len(KINDS)} conditions), "
          f"wordings verbatim, G24A conditions untouched, whitelist passes")
    print("ruling lengths (words): "
          f"exclude_post={len(g24a.EXCLUDE_RULE.split())}, "
          f"strong={len(g24p1.STRONG_EXCLUDE_RULE.split())}, "
          f"cfdelete={len(g24p1.CF_DELETE_RULE.split())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
