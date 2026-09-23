"""G23A: materials, prompt assembly, estimator, exclusions, verdict rule.

Nothing here touches a model; every test runs on code or synthetic rows only.
"""
from __future__ import annotations

import json
import os
import re
from collections import Counter

import pytest

from conditions_g23a import (ARMS, G23A_CONDITIONS, G23A_NUMERIC_PROBES,
                              G23A_PROBES, G23A_RULE_PROBES, NONZERO_WKEYS,
                              WKEYS, WEIGHTS, blocks)
from gen_g23a import build, check_fresh
from schema import compile_probe, compile_prompt, load_items

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ITEMS = build()


# ---------------------------------------------------------------------------
# Materials
# ---------------------------------------------------------------------------
def test_shape_72_items_72_skeletons_24_per_family():
    assert len(ITEMS) == 72
    assert Counter(i.task_family for i in ITEMS) == {
        "legal_judgment": 24, "evidence_inference": 24, "ranking_selection": 24}
    skeletons = [i.meta["skeleton"] for i in ITEMS]
    assert len(set(skeletons)) == 72, "one item per independent skeleton"


def test_directions_balanced_inside_every_family():
    for fam in {i.task_family for i in ITEMS}:
        dirs = Counter(i.critical_direction for i in ITEMS if i.task_family == fam)
        assert set(dirs.values()) == {12}, (fam, dict(dirs))


def test_domains_unique_and_fresh():
    assert len({i.surface_domain for i in ITEMS}) == 72
    check_fresh(ITEMS, ROOT)   # asserts no id / domain / skeleton collision


def test_no_llm_gold_and_contexts_are_substantial():
    for i in ITEMS:
        assert i.ground_truth is None
        assert len(i.base_context) >= 120
        assert i.critical_evidence.strip()
        assert i.critical_label.strip() == i.critical_label
        assert i.evidence_truth == "true_but_forbidden"
        assert i.exclusion_reason == "weight_rule"


def test_frozen_artifact_matches_the_preregistered_sha():
    path = os.path.join(ROOT, "data/items/g23a_v1.jsonl")
    if not os.path.exists(path):
        pytest.skip("materials not built in this checkout")
    import hashlib
    digest = hashlib.sha256(open(path, "rb").read()).hexdigest()
    assert digest == ("03be16945cc03da60b06ec44d25f047d1e214e9e078b91f72cf583abd4eeb433")
    on_disk = load_items(path)
    assert [i.item_id for i in on_disk] == [i.item_id for i in ITEMS]


# ---------------------------------------------------------------------------
# Prompt assembly
# ---------------------------------------------------------------------------
def _blocks_of(prompt: str):
    return prompt.split("\n\n")


def test_condition_set_is_the_twelve_preregistered_cells():
    assert len(G23A_CONDITIONS) == 12
    assert set(G23A_CONDITIONS) == {"g23a_base", "g23a_norule"} | {
        f"g23a_{arm}_{w}" for w in WKEYS for arm in ARMS}
    assert WKEYS == ("w000", "w001", "w025", "w050", "w100")
    assert NONZERO_WKEYS == ("w001", "w025", "w050", "w100")
    assert [WEIGHTS[w] for w in WKEYS] == [0.0, 0.01, 0.25, 0.5, 1.0]


def test_base_has_no_rule_and_no_evidence_norule_the_reverse():
    it = ITEMS[0]
    base = compile_prompt(it, "g23a_base")
    assert "RULING" not in base and "ADDITIONAL INFORMATION" not in base
    norule = compile_prompt(it, "g23a_norule")
    assert norule.count("ADDITIONAL INFORMATION") == 1
    assert "RULING" not in norule


def test_pre_and_post_differ_only_by_block_order():
    for w in WKEYS:
        pre, post = (compile_prompt(ITEMS[0], f"g23a_pre_{w}"),
                     compile_prompt(ITEMS[0], f"g23a_post_{w}"))
        assert pre != post
        assert sorted(_blocks_of(pre)) == sorted(_blocks_of(post))
        assert pre.count("ADDITIONAL INFORMATION") == post.count(
            "ADDITIONAL INFORMATION") == 1
        assert pre.count("RULING") == post.count("RULING") == 1


def test_only_the_number_changes_across_weights():
    stripped = None
    for w in WKEYS:
        rule = [b for b in _blocks_of(compile_prompt(ITEMS[0], f"g23a_pre_{w}"))
                if b.startswith("RULING")][0]
        without_digits = re.sub(r"\d+%?", "<n>", rule)
        if stripped is None:
            stripped = without_digits
        else:
            assert without_digits == stripped
    for w, frac in WEIGHTS.items():
        pct = f"{frac * 100:g}%"
        assert pct in compile_prompt(ITEMS[0], f"g23a_pre_{w}")


def test_all_items_compile_every_condition():
    for it in ITEMS:
        for c in G23A_CONDITIONS:
            p = compile_prompt(it, c)
            assert p.endswith(compile_prompt(it, "g23a_base").split("TASK\n")[-1])
        assert compile_prompt(it, "g23a_pre_w000") != compile_prompt(
            it, "g23a_pre_w100")


def test_blocks_helper_orders_background_rule_evidence():
    it = ITEMS[0]
    B, E = "B", "E"
    assert blocks(it, "g23a_base", B, E) == [B]
    assert blocks(it, "g23a_norule", B, E) == [B, E]
    pre = blocks(it, "g23a_pre_w025", B, E)
    post = blocks(it, "g23a_post_w025", B, E)
    assert pre == [B, pre[1], E] and post == [B, E, post[2]]
    assert pre[1] == post[2]


# ---------------------------------------------------------------------------
# Probes
# ---------------------------------------------------------------------------
def test_probe_inventory_is_thirteen():
    assert len(G23A_NUMERIC_PROBES) == 10 and len(G23A_RULE_PROBES) == 3
    assert len(G23A_PROBES) == 13
    assert all(p.startswith("wprobe") for p in G23A_NUMERIC_PROBES)
    assert all(p.startswith("rule_probe") for p in G23A_RULE_PROBES)


def test_probes_compile_and_ask_one_question():
    it = ITEMS[3]
    for p in G23A_PROBES:
        q = compile_probe(it, p)
        assert "TASK\n" in q
        if p.startswith("rule_probe"):
            assert "YES or NO" in q
            assert "Rate " not in q.split("TASK\n")[-1]
        else:
            assert "0 to 100" in q
    # the numeric probe is asked over the matching decision context
    assert ("RULING" in compile_probe(it, "wprobe_g23a_pre_w001"))
    assert ("RULING" not in compile_probe(it, "wprobe_g23a_post_w001").split(
        "ADDITIONAL INFORMATION")[0])


def test_probe_question_does_not_leak_into_decisions():
    it = ITEMS[1]
    assert it.rule_probe_question not in compile_prompt(it, "g23a_post_w000")


# ---------------------------------------------------------------------------
# Estimator, exclusions, verdict rule
# ---------------------------------------------------------------------------
def _raw(path, rows):
    with open(path, "w") as handle:
        for row in rows:
            handle.write(json.dumps(row) + "\n")


def _cells(item_id, **over):
    cells = {"g23a_base": 50.0, "g23a_norule": 70.0}
    for w in WKEYS:
        for arm in ARMS:
            cells[f"g23a_{arm}_{w}"] = 50.0
    cells.update(over)
    return [{"item_id": item_id, "kind_name": k, "value": v}
            for k, v in cells.items()]


def test_gap_and_delta_are_computed_as_preregistered(tmp_path):
    from analyze_g23a import rows_for
    items = {i.item_id: i for i in ITEMS}
    path = tmp_path / "raw.jsonl"
    # +direction item: evidence pulls up 20 points with no rule. Under the rule the
    # prospective arm keeps 15 points at w=0 and the retrospective arm keeps none;
    # at every non-zero weight both arms keep exactly 10.
    over = {}
    for w in WKEYS:
        over[f"g23a_pre_{w}"] = 65.0 if w == "w000" else 60.0
        over[f"g23a_post_{w}"] = 50.0 if w == "w000" else 60.0
    rows_in = _cells(ITEMS[0].item_id, **over)
    _raw(path, rows_in)
    rows, drops = rows_for(items, str(path))
    assert drops == {} and len(rows) == 1
    r = rows[0]
    assert r["leverage"] == pytest.approx(20.0)
    assert r["resinf"][("pre", "w000")] == pytest.approx(15.0)
    assert r["resinf"][("post", "w000")] == pytest.approx(0.0)
    assert r["gap"]["w000"] == pytest.approx(15.0)
    assert all(r["gap"][w] == pytest.approx(0.0) for w in NONZERO_WKEYS)
    assert r["delta"] == pytest.approx(15.0)


def test_nonpositive_leverage_and_incomplete_rows_are_dropped(tmp_path):
    from analyze_g23a import rows_for
    items = {i.item_id: i for i in ITEMS}
    good, bad = ITEMS[0], ITEMS[1]              # both "increase"
    path = tmp_path / "raw.jsonl"
    rows_in = _cells(good.item_id, g23a_norule=70.0)          # leverage +20
    rows_in += _cells(bad.item_id, g23a_norule=40.0)          # leverage −10
    incomplete = [r for r in _cells(ITEMS[2].item_id)
                  if r["kind_name"] != "g23a_pre_w025"]        # one cell missing
    rows_in += incomplete
    _raw(path, rows_in)
    rows, drops = rows_for(items, str(path))
    assert [r["item_id"] for r in rows] == [good.item_id]
    assert drops["nonpositive_leverage"] == 1 and drops["incomplete"] == 1


def test_probe_reader_reports_stated_weight_and_permission(tmp_path):
    from analyze_g23a import probes_for
    path = tmp_path / "raw.jsonl"
    rows = [
        {"item_id": "a", "kind_name": "wprobe_g23a_pre_w001", "value": 1.0},
        {"item_id": "a", "kind_name": "wprobe_g23a_post_w001", "value": 5.0},
        {"item_id": "a", "kind_name": "wprobe_g23a_pre_w000", "value": 0.0},
        {"item_id": "a", "kind_name": "rule_probe_g23a_w000_pre", "p_yes": 0.02},
        {"item_id": "a", "kind_name": "rule_probe_g23a_w100_pre", "p_yes": 0.97},
    ]
    _raw(path, rows)
    out = probes_for(str(path))
    assert out["stated_weight"]["w001"]["n"] == 2
    assert out["stated_weight"]["w001"]["frac_within_tol"] == 0.5  # 1 vs 3 pp
    assert out["stated_weight"]["w000"]["median_abs_error_pp"] == 0.0
    assert out["permission_yes"]["rule_probe_g23a_w000_pre"]["mean_p_yes"] == 0.02
    assert "w025" not in out["stated_weight"]


def test_verdict_rule_is_exhaustive_and_frozen():
    from analyze_g23a import ATTEN_WKEYS, DELTA_FLOOR, MIN_MODELS_POSITIVE, verdict_for
    def stats(mean, lo, hi):
        return {"mean": mean, "ci_low": lo, "ci_high": hi}

    # sharp zero-specific gap, all models positive
    assert verdict_for(stats(12.0, 6.0, 18.0), stats(0.5, -2.0, 3.0), 3, 3) == \
        "zero-amplified"
    # right shape but only one model agrees
    assert verdict_for(stats(12.0, 6.0, 18.0), stats(0.5, -2.0, 3.0), 1, 3) == \
        "model-dependent"
    # right direction, below the frozen floor
    assert verdict_for(stats(DELTA_FLOOR - 0.1, 0.2, 5.0),
                       stats(0.5, -2.0, 3.0), 3, 3) == "sub-threshold"
    # non-zero weights carry the gap too -> generic timing failure
    assert verdict_for(stats(1.0, -4.0, 6.0), stats(4.0, 1.0, 7.0), 3, 3) == \
        "smooth-timing"
    # nothing survives anywhere
    assert verdict_for(stats(0.4, -3.0, 4.0), stats(0.2, -2.0, 2.5), 0, 3) == \
        "no-replication"
    assert MIN_MODELS_POSITIVE == 2
    assert ATTEN_WKEYS == ("w001", "w025", "w050")


def test_w100_is_admit_anchor_not_part_of_delta(tmp_path):
    from analyze_g23a import rows_for
    items = {i.item_id: i for i in ITEMS}
    path = tmp_path / "raw.jsonl"
    over = {}
    for w in WKEYS:
        over[f"g23a_pre_{w}"] = 60.0
        over[f"g23a_post_{w}"] = 60.0
    over["g23a_pre_w000"] = 59.0
    over["g23a_post_w000"] = 50.0
    # Deliberately make the 100% Admit anchor order-sensitive. It must not enter Δ_zero.
    over["g23a_pre_w100"] = 80.0
    over["g23a_post_w100"] = 50.0
    _raw(path, _cells(ITEMS[0].item_id, **over))
    rows, drops = rows_for(items, str(path))
    assert drops == {} and len(rows) == 1
    assert rows[0]["gap"]["w100"] == pytest.approx(30.0)
    assert rows[0]["delta"] == pytest.approx(9.0)


def test_target_deviation_is_raw_not_ratio(tmp_path):
    from analyze_g23a import rows_for
    items = {i.item_id: i for i in ITEMS}
    path = tmp_path / "raw.jsonl"
    # leverage=20; exact 25% implementation is ResInf=5.
    over = {"g23a_pre_w025": 55.0, "g23a_post_w025": 55.0}
    _raw(path, _cells(ITEMS[0].item_id, **over))
    rows, drops = rows_for(items, str(path))
    assert drops == {} and len(rows) == 1
    r = rows[0]
    assert r["leverage"] == pytest.approx(20.0)
    assert r["target_dev"][("pre", "w025")] == pytest.approx(0.0)
    assert r["target_dev"][("post", "w025")] == pytest.approx(0.0)


def test_v3_semantic_freeze_claim_scope_and_probe_naming():
    """v3 is an interpretive-only freeze.

    The claim must stay scoped to instructions (a discontinuity at w=0 relative to
    non-zero weight instructions), and the numeric probe must not be labelled
    "weighting competence": it only shows the model can state the requested weight.
    """
    import analyze_g23a

    with open(analyze_g23a.__file__, encoding="utf-8") as handle:
        src = handle.read()
    assert "requested_weight_access_ok" in src
    assert "weighting_competent" not in src
    assert "quantitative weighting" not in src

    with open(os.path.join(ROOT, "preregistrations/"
                             "PREREGISTRATION_G23A_ZERO_GATING.md"),
              encoding="utf-8") as handle:
        prereg = handle.read()
    assert "discontinuously amplified at `w = 0`" in prereg
    assert "explicit policy access / requested-weight recall" in prereg
    assert "quantitative weighting competence" not in prereg
    # TargetDeviation stays descriptive: it may contradict an implementation
    # claim, never confirm one, and never enters a gate.
    assert "never be promoted into an actionability" in prereg
