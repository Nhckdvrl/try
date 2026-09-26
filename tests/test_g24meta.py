"""§14 RQ3 explanation experiment (second-order retraction operators) —
nothing here touches a model.

Runs on code and the committed P2 item file only:

* conditions: exactly the two frozen cells; MNR wording byte-identical to
  registration §14.2; ``random_reason_post`` = P1's ``CF_DELETE_RULE``
  byte-identical (first-order core held fixed) + the random-procedural
  reason sentence;
* layout: the G24A POST arm (CLAIM / EVIDENCE E / RULING), one identical
  question/output tail across the whole 13-cell run contract;
* dispatch: the new name-first branch leaves g24a / g24p1 / g24p3 / g24p4
  cells bit-for-bit (legacy prompts re-derivable from their own modules);
  no condition-name collision with any registry;
* materials: reuses the committed P2 file (400 arm items) — both new cells
  compile over every item;
* runner/schema wiring locks.
"""
from __future__ import annotations

import os

import conditions_g24a as g24a
import conditions_g24meta as g24meta
import conditions_g24p1 as g24p1
import conditions_g24p3 as g24p3
import conditions_g24p4 as g24p4
from schema import (CONDITIONS, EXTRA_CONDITIONS, V2_CONDITIONS, V3_CONDITIONS,
                    V4_CONDITIONS, V5_CONDITIONS, V6_CONDITIONS, V7_CONDITIONS,
                    ROUTING_CONDITIONS, LINEAR_CONDITIONS, G17_CONDITIONS,
                    G18_CONDITIONS, G23A_CONDITIONS, G23B_CONDITIONS,
                    G25A_CONDITIONS, G26A_CONDITIONS, G24P1_CONDITIONS,
                    G24P3_CONDITIONS, G24P4_CONDITIONS, G24META_CONDITIONS,
                    PROBES, Item, _blocks, compile_prompt, load_items)

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
P2_ITEMS = os.path.join(ROOT, "data/items/g24a_p2_v1.jsonl")
G0_ITEMS = os.path.join(ROOT, "data/items/items_v1.jsonl")

ITEMS = load_items(P2_ITEMS)

# Registration §14.2, verbatim (wording lock — must never drift).
MNR_EXPECTED = (
    "Evidence E must have no influence on your judgment. Importantly, the "
    "fact that Evidence E was shown, withheld, or retracted is itself purely "
    "procedural and provides no information about the claim or about the "
    "truth or reliability of Evidence E. Judge exactly as if neither "
    "Evidence E nor any retraction event had occurred.")
RANDOM_REASON_EXPECTED = (
    "Evidence E was excluded by a random administrative procedure that is "
    "independent of its content, truth, reliability, and the claim.")


def test_condition_registry_frozen_and_disjoint():
    assert G24META_CONDITIONS == ["meta_neutral_post", "random_reason_post"]
    other = (set(CONDITIONS) | set(EXTRA_CONDITIONS) | set(V2_CONDITIONS)
             | set(V3_CONDITIONS) | set(V4_CONDITIONS) | set(V5_CONDITIONS)
             | set(V6_CONDITIONS) | set(V7_CONDITIONS) | set(ROUTING_CONDITIONS)
             | set(LINEAR_CONDITIONS) | set(G17_CONDITIONS) | set(G18_CONDITIONS)
             | set(G23A_CONDITIONS) | set(G23B_CONDITIONS) | set(G25A_CONDITIONS)
             | set(G26A_CONDITIONS) | set(G24P1_CONDITIONS) | set(G24P3_CONDITIONS)
             | set(G24P4_CONDITIONS) | set(PROBES))
    assert not (set(G24META_CONDITIONS) & other), "condition-name collision"
    assert g24meta.is_g24meta("meta_neutral_post")
    assert g24meta.is_g24meta("random_reason_post")
    for legacy in ("base", "admit_post", "exclude_post", "strong_exclude_post",
                   "counterfactual_delete_post", "withheld_cf", "irrelevant_cf"):
        assert not g24meta.is_g24meta(legacy)


def test_wording_frozen_verbatim():
    assert g24meta.META_NEUTRAL_RULE == MNR_EXPECTED
    assert g24meta.RANDOM_PROCEDURAL_REASON == RANDOM_REASON_EXPECTED
    # structural spot-checks of the second-order neutralizer
    assert "shown, withheld, or retracted" in MNR_EXPECTED
    assert "purely procedural" in MNR_EXPECTED
    assert "neither Evidence E nor any retraction event" in MNR_EXPECTED


def test_random_reason_rule_is_cf_core_plus_reason():
    rule = g24meta.random_reason_rule()
    assert rule.startswith(g24p1.CF_DELETE_RULE)          # first-order core byte-identical
    assert rule == g24p1.CF_DELETE_RULE + " " + RANDOM_REASON_EXPECTED


def test_post_layout_and_ruling_content():
    it = ITEMS[0]
    for cond, ruling in (("meta_neutral_post", MNR_EXPECTED),
                         ("random_reason_post", g24meta.random_reason_rule())):
        blocks = _blocks(it, cond)
        assert blocks == g24meta.blocks(it, cond)
        assert len(blocks) == 3
        assert blocks[0] == g24a.CLAIM_HEADER + "\n" + it.base_context
        assert blocks[1] == g24a.EVIDENCE_HEADER + "\n" + it.critical_evidence
        assert blocks[2] == "RULING\n" + ruling


def test_every_p2_item_compiles_both_cells_identical_tail():
    tail = compile_prompt(ITEMS[0], "meta_neutral_post").split("TASK\n")[-1]
    assert ITEMS[0].question in tail and ITEMS[0].output_spec in tail
    assert len(ITEMS) == 400                          # committed P2 arm items
    for it in ITEMS:
        for cond in G24META_CONDITIONS:
            p = compile_prompt(it, cond)
            assert p.split("TASK\n")[-1] == tail
            assert p.count("EVIDENCE E\n") == 1 and p.count("RULING") == 1
            assert it.critical_evidence in p
        assert compile_prompt(it, "meta_neutral_post") != \
            compile_prompt(it, "random_reason_post")


def test_legacy_dispatch_unaffected_by_g24meta_branch():
    it = ITEMS[0]
    for cond in ("base", "admit_post", "exclude_post"):
        assert not g24meta.is_g24meta(cond)
        assert _blocks(it, cond) == g24a.blocks(it, cond)
    for cond in g24p1.G24P1_CONDITIONS:
        assert _blocks(it, cond) == g24p1.blocks(it, cond)
    for cond in g24p4.G24P4_CONDITIONS:
        assert _blocks(it, cond) == g24p4.blocks(it, cond)
    g0 = load_items(G0_ITEMS)[0]
    assert compile_prompt(g0, "base").startswith("BACKGROUND\n")
    assert not compile_prompt(g0, "base").startswith("CLAIM\n")


def test_run_contract_tail_matches_g24a_base():
    """The 13 §14 cells share one tail: new cells vs the unmodified G24A base."""
    it = ITEMS[0]
    base_tail = compile_prompt(it, "base").split("TASK\n")[-1]
    for cond in ("meta_neutral_post", "random_reason_post", "admit_post",
                 "exclude_post", "strong_exclude_post",
                 "counterfactual_delete_post"):
        p = compile_prompt(it, cond)
        assert p.split("TASK\n")[-1] == base_tail


def test_run_model_and_schema_wiring_locks():
    with open(os.path.join(ROOT, "src/run_model.py"), encoding="utf-8") as fh:
        runner = fh.read()
    assert runner.count("G24META_CONDITIONS") == 2   # import + membership chain
    with open(os.path.join(ROOT, "src/schema.py"), encoding="utf-8") as fh:
        schema_src = fh.read()
    assert "import conditions_g24meta as g24meta" in schema_src
    assert "g24meta.G24META_CONDITIONS" in schema_src
    assert "g24meta.is_g24meta(cond)" in schema_src
    # the new branch must sit BEFORE the g24a task_family catch-all
    assert schema_src.index("g24meta.is_g24meta(cond)") < \
        schema_src.index("g24a.is_g24a(item)")
