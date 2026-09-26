#!/usr/bin/env python3
"""Pre-run verification for the §14 explanation-experiment prompts
(zero model output read).

Checks, for all 400 items x 7 plus-kinds = 2,800 prompts:

  1. compile_prompt succeeds; TASK tail present (question + output spec +
     answer format)
  2. block order CLAIM -> EVIDENCE E -> RULING for the six evidence-bearing
     conditions; base has no RULING and no EVIDENCE E
  3. the two new rulings appear VERBATIM (independent hard-coded copy of the
     user's 2026-09-26 §14.2 spec; a typo in the module fails this), and
     the registration doc carries the same strings (doc <-> code lock)
  4. the four legacy operators render through the UNMODIFIED G24A/P1
     modules: schema._blocks == conditions_g24a.blocks (base/admit_post/
     exclude_post) and == conditions_g24p1.blocks (strong_exclude_post/
     counterfactual_delete_post) — i.e. the in-batch re-run is
     character-identical to P1/P2 by construction
  5. within one item, all six post operators share identical prefix
     (claim+evidence) and identical TASK tail — the ruling string is the
     only difference — and the six rulings are pairwise distinct
     (random_reason_post's core is CF byte-identical + reason sentence)
  6. rule_char_offset: None for base, points at the RULING block otherwise
  7. the 13 condition names pass run_model's kind whitelist (incl.
     schema.G24META_CONDITIONS) and none is a probe kind
  8. item-level constants: admit_rule/exclude_rule/question/output_spec are
     the module constants (task_family "g24a_vitaminc" is dispatch-only)
  9. regression: a G24A discovery item still compiles all five G0
     conditions unchanged; no condition name collides across g24meta /
     g24p1 / g24p3 / g24p4 / g25 / g26

Arm-matrix contracts (the properties that make the 13-cell design
estimable, inherited verbatim from P2):

 10. group structure: 200 claims x exactly 2 arms (plus/minus), unique ids
 11. shared claim block: within a claim the two arms are identical in
     base_context, question, output_spec, admit_rule, exclude_rule —
     only critical_evidence / critical_direction differ
 12. shared Y0: the base prompt (claim only) is BYTE-IDENTICAL across arms
     for every claim and evidence-free — Y0 is one number per (model,
     claim) by construction, so base is issued on arm+ only
 13. exact evidence per arm: for every evidence-bearing condition the
     rendered EVIDENCE E block equals that arm's own critical_evidence
     byte-for-byte
 14. arm id lists: ids_plus / ids_minus are disjoint, cover all 400 items,
     and their sizes match the run contract (arm+ x 7 kinds incl. base,
     arm- x 6 kinds excl. base)
 15. run script binding: scripts/run_g24a_meta.sh carries the same
     KINDS_PLUS / KINDS_MINUS lines and the same id files

Usage: python scripts/verify_g24a_meta_prompts.py   (exit 0 = all pass)
"""
from __future__ import annotations

import json
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, os.path.join(ROOT, "src"))

import schema                                   # noqa: E402
import conditions_g24a as g24a                  # noqa: E402
import conditions_g24p1 as g24p1                # noqa: E402
import conditions_g24p3 as g24p3                # noqa: E402
import conditions_g24p4 as g24p4                # noqa: E402
import conditions_g24meta as g24meta            # noqa: E402
import conditions_g25 as g25                    # noqa: E402
import conditions_g26a as g26                   # noqa: E402

ITEMS = os.path.join(ROOT, "data", "items", "g24a_p2_v1.jsonl")
IDS_PLUS = os.path.join(ROOT, "data", "items", "g24a_p2_ids_plus.json")
IDS_MINUS = os.path.join(ROOT, "data", "items", "g24a_p2_ids_minus.json")
DISCOVERY = os.path.join(ROOT, "data", "items", "g24a_v1.jsonl")
VALIDITY = os.path.join(ROOT, "data", "items", "g24a_p2_validity_v1.jsonl")
REG = os.path.join(ROOT, "results", "discovery", "g24a_competing_accounts_v1.md")

# The run contract (frozen here; scripts/run_g24a_meta.sh mirrors it): base
# runs on arm+ only, the six evidence-bearing kinds run on both arms.
KINDS_PLUS = ["base", "admit_post", "exclude_post",
              "strong_exclude_post", "counterfactual_delete_post",
              "meta_neutral_post", "random_reason_post"]
KINDS_MINUS = ["admit_post", "exclude_post",
               "strong_exclude_post", "counterfactual_delete_post",
               "meta_neutral_post", "random_reason_post"]

# Independent copies of the verbatim wordings (§14.2, user 2026-09-26).
# If the module drifts from the spec, these comparisons fail.
SPEC_MNR = (
    "Evidence E must have no influence on your judgment. Importantly, the "
    "fact that Evidence E was shown, withheld, or retracted is itself purely "
    "procedural and provides no information about the claim or about the "
    "truth or reliability of Evidence E. Judge exactly as if neither "
    "Evidence E nor any retraction event had occurred.")
SPEC_RANDOM_REASON = (
    "Evidence E was excluded by a random administrative procedure that is "
    "independent of its content, truth, reliability, and the claim.")
# Legacy locks (from P1's spec, user 2026-09-25) — the four re-run cells
# must not have drifted either.
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
    # --- wording locks: module vs independent spec --------------------------
    assert g24meta.META_NEUTRAL_RULE == SPEC_MNR, "MNR wording drifted"
    assert g24meta.RANDOM_PROCEDURAL_REASON == SPEC_RANDOM_REASON, \
        "random-procedural reason drifted"
    assert g24meta.random_reason_rule() == \
        g24p1.CF_DELETE_RULE + " " + SPEC_RANDOM_REASON, \
        "random-reason core is not CF byte-identical"
    assert g24p1.STRONG_EXCLUDE_RULE == SPEC_STRONG, "strong wording drifted"
    assert g24p1.CF_DELETE_RULE == SPEC_CF, "counterfactual wording drifted"
    # doc <-> code lock: the registration carries the same verbatim strings
    doc = open(REG, encoding="utf-8").read()
    assert "## 14." in doc and "meta_neutral_post" in doc \
        and "random_reason_post" in doc, "registration §14 missing"
    for s in (SPEC_MNR, SPEC_RANDOM_REASON):
        assert s in doc, "spec string missing from registration §14"
    # --- run contract -------------------------------------------------------
    assert KINDS_PLUS[5:] == g24meta.G24META_CONDITIONS, "run contract drift"
    assert "base" not in KINDS_MINUS, KINDS_MINUS
    assert KINDS_MINUS == KINDS_PLUS[1:], "run contract drift"
    assert len(KINDS_PLUS) + len(KINDS_MINUS) == 13

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
                # exact per-arm evidence block (13)
                got = p.split("EVIDENCE E\n", 1)[1].split("\n\nRULING\n", 1)[0]
                assert got == it.critical_evidence, (it.item_id, k)
            # new cells: the §14 ruling renders verbatim (3)
            if k == "meta_neutral_post":
                assert SPEC_MNR in p, (it.item_id, k)
            if k == "random_reason_post":
                assert SPEC_RANDOM_REASON in p and g24p1.CF_DELETE_RULE in p, \
                    (it.item_id, k)
            if k in ("strong_exclude_post", "counterfactual_delete_post"):
                want = (g24p1.STRONG_EXCLUDE_RULE
                        if k == "strong_exclude_post" else g24p1.CF_DELETE_RULE)
                assert want in p, (it.item_id, k)
            # legacy cells render through their UNMODIFIED modules (4)
            if k in ("base", "admit_post", "exclude_post"):
                assert schema._blocks(it, k) == g24a.blocks(it, k), (it.item_id, k)
            if k in ("strong_exclude_post", "counterfactual_delete_post"):
                assert schema._blocks(it, k) == g24p1.blocks(it, k), (it.item_id, k)
            # new cells dispatch through the g24meta module
            if k in g24meta.G24META_CONDITIONS:
                assert schema._blocks(it, k) == g24meta.blocks(it, k), (it.item_id, k)
            n += 1
    assert n == 2800, n

    # ruling is the ONLY difference between the six post operators (5):
    # identical prefix through the evidence block, identical TASK tail
    it = items[0]
    posts = ["admit_post", "exclude_post", "strong_exclude_post",
             "counterfactual_delete_post", "meta_neutral_post",
             "random_reason_post"]
    ps = {k: schema.compile_prompt(it, k) for k in posts}
    heads = [p[:p.index("RULING\n")] for p in ps.values()]
    assert len(set(heads)) == 1, "prefix differs across post operators"
    tails = [p[p.index("TASK\n"):] for p in ps.values()]
    assert len(set(tails)) == 1, "tail differs across post operators"
    rulings = {k: p[p.index("RULING\n"):p.index("TASK\n")] for k, p in ps.items()}
    assert len(set(rulings.values())) == len(posts), "rulings not distinct"
    # CF core shared by cf and random-reason (first-order core held fixed)
    assert ps["random_reason_post"].split("RULING\n", 1)[1].startswith(SPEC_CF)

    # kind whitelist (7): every kind in the lists unioned by run_model's
    # membership chain; none is a probe
    lists = [schema.CONDITIONS, schema.EXTRA_CONDITIONS, schema.V2_CONDITIONS,
             schema.V3_CONDITIONS, schema.V4_CONDITIONS, schema.ROUTING_CONDITIONS,
             schema.V5_CONDITIONS, schema.LINEAR_CONDITIONS, schema.V6_CONDITIONS,
             schema.V7_CONDITIONS, schema.G17_CONDITIONS, schema.G18_CONDITIONS,
             schema.G23A_CONDITIONS, schema.G23B_CONDITIONS, schema.G25A_CONDITIONS,
             schema.G26A_CONDITIONS, schema.G24P1_CONDITIONS, schema.G24P3_CONDITIONS,
             schema.G24P4_CONDITIONS, schema.G24META_CONDITIONS,
             schema.AGENT_CONDITIONS, schema.EXT_CONDITIONS, schema.PROBES]
    for k in KINDS_PLUS:
        assert any(k in lst for lst in lists), f"{k} not in run_model whitelist"
        assert k not in schema.PROBES, f"{k} must not be a probe kind"

    # regression (9): G24A discovery item unchanged for all five G0 conditions
    disc = schema.load_items(DISCOVERY)
    for k in ["base", "admit_pre", "admit_post", "exclude_pre", "exclude_post"]:
        assert schema._blocks(disc[0], k) == g24a.blocks(disc[0], k), k
        schema.compile_prompt(disc[0], k)
    # no name collisions across the operator registries
    for k in KINDS_PLUS:
        assert not g25.is_g25(k), k
        assert not g26.is_g26(k), k
    for k in ("meta_neutral_post", "random_reason_post"):
        assert not g24p1.is_g24p1(k) and not g24p3.is_g24p3(k) \
            and not g24p4.is_g24p4(k), k
    for k in ("base", "exclude_post", "g25_w000_post", "g26_admit_t0",
              "withheld_cf", "irrelevant_cf"):
        assert not g24meta.is_g24meta(k), k

    # --- arm-matrix contracts (10-14) ---------------------------------------
    groups: dict[str, dict[str, schema.Item]] = {}
    for it in items:
        arm = it.meta["arm"]
        assert arm in ("plus", "minus"), it.item_id
        groups.setdefault(it.meta["p2_id"], {})[arm] = it
    assert len(groups) == 200, len(groups)
    for p2_id, arms in groups.items():
        assert set(arms) == {"plus", "minus"}, p2_id
        pm, mm = arms["plus"], arms["minus"]
        # shared claim block: identical except the evidence itself (11)
        assert pm.base_context == mm.base_context, p2_id
        assert pm.question == mm.question and pm.output_spec == mm.output_spec, p2_id
        assert pm.admit_rule == mm.admit_rule and pm.exclude_rule == mm.exclude_rule, p2_id
        assert pm.critical_evidence != mm.critical_evidence, p2_id
        assert (pm.critical_direction, mm.critical_direction) == ("increase", "decrease"), p2_id
        # shared Y0: base prompt byte-identical, evidence-free (12)
        assert schema.compile_prompt(pm, "base") == schema.compile_prompt(mm, "base"), \
            f"base differs across arms: {p2_id}"
    val = [json.loads(l) for l in open(VALIDITY, encoding="utf-8")]
    assert len(val) == 262, len(val)
    valid_ids = {e["p2_id"] for e in val if e["verdict"] == "valid"}
    assert valid_ids == set(groups), "item claims != validity run set"

    # arm id lists (14): disjoint, covering, sized for the run contract
    ids_plus = json.load(open(IDS_PLUS))
    ids_minus = json.load(open(IDS_MINUS))
    all_ids = {it.item_id for it in items}
    assert len(ids_plus) == len(ids_minus) == 200, (len(ids_plus), len(ids_minus))
    assert not (set(ids_plus) & set(ids_minus)), "arm id lists overlap"
    assert set(ids_plus) | set(ids_minus) == all_ids, "arm id lists do not cover items"
    assert all(i.endswith("_plus") for i in ids_plus), ids_plus[:3]
    assert all(i.endswith("_minus") for i in ids_minus), ids_minus[:3]
    # base is a plus-only kind: minus base prompt == plus base prompt (12)
    for p2_id, arms in groups.items():
        assert arms["minus"].item_id in set(ids_minus), p2_id
        assert schema.compile_prompt(arms["minus"], "base") == \
            schema.compile_prompt(arms["plus"], "base"), p2_id

    # run script binding (15): kind lists + id files live in run_g24a_meta.sh
    run_sh = os.path.join(ROOT, "scripts", "run_g24a_meta.sh")
    text = open(run_sh, encoding="utf-8").read()
    m_plus = re.search(r"^KINDS_PLUS=(\S+)$", text, re.M)
    m_minus = re.search(r"^KINDS_MINUS=(\S+)$", text, re.M)
    assert m_plus and m_minus, "run script kind lists not found"
    assert m_plus.group(1).split(",") == KINDS_PLUS, "run script KINDS_PLUS drift"
    assert m_minus.group(1).split(",") == KINDS_MINUS, "run script KINDS_MINUS drift"
    assert "base" not in m_minus.group(1).split(","), "base issued on arm- in run script"
    for arm in ("plus", "minus"):
        rel = f"data/items/g24a_p2_ids_{arm}.json"
        assert rel in text, f"run script does not use {rel}"
    # runner args frozen by §13.4 / §14.3 (present, unchanged)
    for frag in ("--mode reasoned", "--reason-tokens 110",
                 "--max-model-len 4096", "--tp 1", "--gpu-frac 0.85",
                 "--enforce-eager"):
        assert frag in text, f"run script lost {frag}"
    assert "9216db5781bf21249d130ec9da846c4624c16137" in text, "32B snapshot drifted"

    rows = len(ids_plus) * len(KINDS_PLUS) + len(ids_minus) * len(KINDS_MINUS)
    print(f"OK: {n} prompts verified (400 items x {len(KINDS_PLUS)} conditions), "
          f"wordings verbatim (module <-> spec <-> registration), legacy cells "
          f"byte-identical to G24A/P1, whitelist passes")
    print(f"arm matrix: 200 claims x 2 arms; shared claim block; base "
          f"byte-identical across arms (shared Y0); evidence block exact per arm")
    print(f"run contract: arm+ = {len(ids_plus)} ids x {len(KINDS_PLUS)} kinds "
          f"(incl. base), arm- = {len(ids_minus)} ids x {len(KINDS_MINUS)} kinds "
          f"(base never issued on arm-); rows/model = {rows}; "
          f"rows/6 models = {rows * 6}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
