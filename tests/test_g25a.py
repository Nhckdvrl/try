"""G25A design tests — nothing here touches a model.

Runs on code, the frozen candidate/selection files and synthetic records only:

* materials: the frozen ``g25_v1.jsonl`` (sha256, strata 150/150/100,
  byte-identity to candidates, item-level disjointness from the G24A 600,
  342 source/cluster keys, 126 shared with G24A);
* selection: constants frozen, ``leverage`` imported (not reimplemented),
  first-eligible quota walk with exclusion/τ-boundary/shortfall behaviour,
  the real full-walk reproduction of the §5 dry-run anchor
  (``0b38e0837ed9fd60``) and the stratum-audit census, blindness guards;
* conditions: the 16 cells, the rule byte-identical to
  ``conditions_v3.uniform_weight_rule`` (and to G23A's rendered rule),
  one-sentence-one-number, pre/post order-only difference, identical tail,
  G24A/G0 dispatch non-interference, O3 probe wiring, runner/source locks;
* analyzer: frozen constants, cluster bootstrap determinism + whole-cluster
  integrity, estimands both directions, usability drops, RuleAcc readout,
  §8 literal decision order (incl. row precedence), gate strictness;
* **gradedness never gates**: ``classify`` takes no gradedness input, and an
  end-to-end graded panel vs flat panel produce the *same* verdict with only
  the §6 interpretation label differing;
* prereg/wording locks (register §12.3 verbatim start, forbidden phrases,
  the nullification-operation prohibition only ever in "never ..." form).
"""
from __future__ import annotations

import hashlib
import inspect
import json
import os
import re
import sys
from collections import Counter

import pytest

import analyze_g25 as a25
import conditions_g24a as g24a
import conditions_g25 as g25
import select_g24a as sg
import select_g25a as s25
from conditions_v3 import WEIGHT_PROBE_Q, uniform_weight_rule
from gen_g23a import build as build_g23a_items
from schema import (G25A_CONDITIONS, PROBES, Item, _blocks, compile_probe,
                    compile_prompt, load_items)

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ITEMS_PATH = os.path.join(ROOT, "data/items/g25_v1.jsonl")
G25_SHA = "7c6993244d7808d8e65696c00a55f4fc14c7f3011f34f0266e450f1367173147"
CAND = os.path.join(ROOT, "data/items/g24a_candidates_v1.jsonl")
CAND_SHA = "91ebad9850d6f7d39a9b26fcf98c1f998d16aa68cde3a480541df13da721f5cd"
G24A_ITEMS = os.path.join(ROOT, "data/items/g24a_v1.jsonl")
# pin: was b0d02f7a... (written at 44f0eed, 09-24) and went stale when
# 92d8cd0 (09-25, "G24A: apply review fixes to item file: 52 claim
# rewrites + 4 direction flips") rewrote g24a_v1.jsonl without updating
# this line.  Repinned to the current committed file; every other
# assertion in this test (item-level disjointness, G25<->candidates byte
# identity, 472-cluster anchor) re-verified against it.
G24A_SHA = "6dfe6dd4cdcb58d80f3679b6ea0896e0f20486d6c5144ab7fdbe2a51476c35f1"
SELECTION_ROWS = os.path.join(
    ROOT, "results/raw/g24a_mistral-small-24b_selection.jsonl")
PREREG = os.path.join(ROOT, "preregistrations",
                      "PREREGISTRATION_G25A_NEAR_ZERO.md")
G0_ITEMS = os.path.join(ROOT, "data/items/items_v1.jsonl")

ITEMS = load_items(ITEMS_PATH)


# ---------------------------------------------------------------------------
# materials: the frozen items file
# ---------------------------------------------------------------------------
def test_g25_items_file_sha_shape_and_strata():
    digest = hashlib.sha256(open(ITEMS_PATH, "rb").read()).hexdigest()
    assert digest == G25_SHA
    assert len(ITEMS) == 400
    ids = [i.item_id for i in ITEMS]
    assert len(set(ids)) == 400
    assert Counter(i.meta["stratum"] for i in ITEMS) == {
        "fever/SUPPORTS": 150, "fever/REFUTES": 150, "scifact/SUPPORT": 100}
    assert all(i.meta["source"] in ("fever", "scifact") for i in ITEMS)
    assert all(i.critical_label.strip() == "evidence E" for i in ITEMS)


def test_disjoint_from_g24a_and_byte_identical_to_candidates():
    assert hashlib.sha256(open(G24A_ITEMS, "rb").read()).hexdigest() == G24A_SHA
    g24a_ids = {json.loads(l)["item_id"] for l in open(G24A_ITEMS)}
    g25_ids = {i.item_id for i in ITEMS}
    assert not (g25_ids & g24a_ids), "item-level disjointness (§2) violated"
    # every selected record is byte-identical to a candidate record
    cand_lines = {l.rstrip("\n") for l in open(CAND)}
    with open(ITEMS_PATH) as fh:
        sel_lines = [l.rstrip("\n") for l in fh]
    assert len(sel_lines) == 400
    assert all(l in cand_lines for l in sel_lines)


def test_cluster_key_counts_match_the_dry_run_anchor():
    g25_clusters = {s25.cluster_key(json.loads(i.to_json())) for i in ITEMS}
    assert len(g25_clusters) == 342
    g24a_clusters = {s25.cluster_key(json.loads(l)) for l in open(G24A_ITEMS)}
    assert len(g24a_clusters) == 472
    assert len(g25_clusters & g24a_clusters) == 126


# ---------------------------------------------------------------------------
# selection: constants, pure functions, full-walk anchor
# ---------------------------------------------------------------------------
def test_selector_constants_and_rule_identity_frozen():
    assert s25.QUOTAS == {("fever", "SUPPORTS"): 150,
                          ("fever", "REFUTES"): 150,
                          ("scifact", "SUPPORT"): 100}
    assert s25.QUOTA_STRATA == (("fever", "SUPPORTS"),
                                ("fever", "REFUTES"),
                                ("scifact", "SUPPORT"))
    assert s25.DROPPED_STRATUM == "scifact/CONTRADICT"
    assert s25.TAU == 10.0
    assert s25.SELECT_KINDS == {"base", "admit_pre", "admit_post"}
    assert not any("exclude" in k or "probe" in k for k in s25.SELECT_KINDS)
    assert s25.SELECTION_MODEL_TAG == "mistral-small-24b"
    assert s25.ANCHOR_ID_SHA16 == "0b38e0837ed9fd60"
    assert s25.ANCHOR["clusters"] == 342
    assert s25.ANCHOR["clusters_shared_with_g24a"] == 126
    # the eligibility rule is IMPORTED from G24A, never rederived (§5)
    assert s25.leverage is sg.leverage
    assert s25.load_rows is sg.load_rows
    assert s25.cluster_key({"meta": {"source": "fever",
                                     "cluster": "p1"}}) == "fever/p1"


def test_leverage_math_both_directions_and_missing():
    up = {"critical_direction": "increase"}
    dn = {"critical_direction": "decrease"}
    assert s25.leverage(up, {"base": 50, "admit_pre": 60, "admit_post": 70}) == 15.0
    assert s25.leverage(dn, {"base": 50, "admit_pre": 40, "admit_post": 30}) == 15.0
    assert s25.leverage(up, {"base": 50, "admit_post": 70}) is None
    assert s25.leverage(up, None) is None


def _cand(source, label, idx, direction, iid):
    return {"item_id": iid, "critical_direction": direction,
            "meta": {"source": source, "gold_label": label,
                     "candidate_rank": idx, "stratum": f"{source}/{label}",
                     "cluster": f"c{idx}"}}


def test_select_first_eligible_quota_exclusion_and_shortfall():
    q = {("fever", "SUPPORTS"): 2, ("fever", "REFUTES"): 1,
         ("scifact", "SUPPORT"): 1}
    cands = [
        # fever/SUPPORTS: an eligible G24A item FIRST — must be skipped,
        # then 9.99 ineligible, then τ boundary inclusive (10.0), then 15;
        # the 4th eligible is never examined once the quota is hit
        _cand("fever", "SUPPORTS", 0, "increase", "x_excluded"),
        _cand("fever", "SUPPORTS", 1, "increase", "f_lo"),
        _cand("fever", "SUPPORTS", 2, "increase", "f_tau"),
        _cand("fever", "SUPPORTS", 3, "increase", "f_15"),
        _cand("fever", "SUPPORTS", 4, "increase", "f_never"),
        # fever/REFUTES: pool exhausted before quota -> shortfall
        _cand("fever", "REFUTES", 5, "decrease", "r0"),
        _cand("fever", "REFUTES", 6, "decrease", "r_below"),
        # scifact/SUPPORT: one missing value, then eligible
        _cand("scifact", "SUPPORT", 7, "increase", "s_missing"),
        _cand("scifact", "SUPPORT", 8, "increase", "s_ok"),
        # scifact/CONTRADICT: dropped stratum — never selected, never in stats
        _cand("scifact", "CONTRADICT", 9, "decrease", "c0"),
    ]
    rows = {
        "x_excluded": {"base": 50, "admit_pre": 90, "admit_post": 90},
        "f_lo": {"base": 50, "admit_pre": 59.99, "admit_post": 59.99},
        "f_tau": {"base": 50, "admit_pre": 60, "admit_post": 60},
        "f_15": {"base": 50, "admit_pre": 65, "admit_post": 65},
        "f_never": {"base": 50, "admit_pre": 70, "admit_post": 70},
        "r0": {"base": 50, "admit_pre": 30, "admit_post": 30},
        "r_below": {"base": 50, "admit_pre": 47, "admit_post": 47},
        "s_missing": {"base": 50, "admit_post": 90},
        "s_ok": {"base": 50, "admit_pre": 62, "admit_post": 62},
        "c0": {"base": 50, "admit_pre": 99, "admit_post": 99},
    }
    sel, rep = s25.select(cands, rows, excluded={"x_excluded"}, quotas=q)
    assert [x["item_id"] for x in sel] == ["f_tau", "f_15", "r0", "s_ok"]
    assert all(any(x is c for c in cands) for x in sel)  # same records, not copies
    st = rep["strata"]
    assert "scifact/CONTRADICT" not in st          # dropped stratum invisible
    # f_never / r_below are never examined: the walk skips candidates of an
    # already-full stratum before reading leverage (§4 first-eligible rule)
    assert st["fever/SUPPORTS"] == dict(
        pool=5, excluded=1, examined=3, eligible=2, selected=2,
        missing_value=0, below_tau=1, quota=2, shortfall=0)
    assert st["fever/REFUTES"] == dict(
        pool=2, excluded=0, examined=1, eligible=1, selected=1,
        missing_value=0, below_tau=0, quota=1, shortfall=0)
    assert st["scifact/SUPPORT"] == dict(
        pool=2, excluded=0, examined=2, eligible=1, selected=1,
        missing_value=1, below_tau=0, quota=1, shortfall=0)
    assert rep["selected_total"] == 4 and rep["quota_total"] == 4
    assert rep["all_quotas_filled"] is True
    assert rep["leverage_selected_min"] == 10.0        # τ boundary inclusive
    assert rep["tau"] == 10.0 and rep["seed_order"] == 20260924
    # shortfall case: shrink fever/REFUTES quota below its eligible pool
    _, rep2 = s25.select(cands, rows, excluded={"x_excluded"},
                         quotas={**q, ("fever", "REFUTES"): 5})
    assert rep2["strata"]["fever/REFUTES"]["selected"] == 1
    assert rep2["strata"]["fever/REFUTES"]["shortfall"] == 4
    assert rep2["all_quotas_filled"] is False


def test_select_real_walk_reproduces_the_dry_run_anchor():
    """§5/§9.4: the harness re-run must reproduce the id list exactly."""
    candidates = s25.load_jsonl(CAND)
    rows = sg.load_rows([SELECTION_ROWS])
    excluded, g24a_clusters = s25.load_excluded([G24A_ITEMS])
    sel, rep = s25.select(candidates, rows, excluded)
    assert rep["anchor_ok"] is True
    assert rep["selected_ids_sha16"] == "0b38e0837ed9fd60"
    assert rep["selected_total"] == 400
    assert {k: v["selected"] for k, v in rep["strata"].items()} == {
        "fever/SUPPORTS": 150, "fever/REFUTES": 150, "scifact/SUPPORT": 100}
    # first-eligible stream pins (regression against the frozen walk)
    assert {k: v["examined"] for k, v in rep["strata"].items()} == {
        "fever/SUPPORTS": 889, "fever/REFUTES": 2139, "scifact/SUPPORT": 200}
    assert all(v["shortfall"] == 0 for v in rep["strata"].values())
    assert rep["clusters"] == 342
    assert (len({s25.cluster_key(r) for r in sel} & g24a_clusters) == 126)
    lev = sorted(sg.leverage(r, rows[r["item_id"]]) for r in sel)
    assert (round(lev[0], 1), round(lev[len(lev) // 2], 1),
            round(lev[-1], 1)) == (10.0, 36.8, 99.9)
    # the on-disk items file is exactly this walk
    assert [r["item_id"] for r in sel] == [i.item_id for i in ITEMS]


def test_selection_census_reproduces_the_frozen_stratum_audit():
    candidates = s25.load_jsonl(CAND)
    rows = sg.load_rows([SELECTION_ROWS])
    excluded, _ = s25.load_excluded([G24A_ITEMS])
    cen = s25.census(candidates, rows, excluded)
    assert cen == {
        "fever/SUPPORTS": dict(pool=6326, excluded=200, missing_value=0,
                               below_tau=4255, eligible=1871, remaining=6126),
        "fever/REFUTES": dict(pool=6322, excluded=200, missing_value=0,
                              below_tau=5318, eligible=804, remaining=6122),
        "scifact/SUPPORT": dict(pool=417, excluded=100, missing_value=0,
                                below_tau=148, eligible=169, remaining=317),
        "scifact/CONTRADICT": dict(pool=218, excluded=100, missing_value=0,
                                   below_tau=117, eligible=1, remaining=118),
    }


def test_selection_blindness_guards(tmp_path):
    """§9.2: any Exclude kind or probe row in selection input aborts."""
    def _write(name, rows):
        p = tmp_path / name
        with open(p, "w") as fh:
            for r in rows:
                fh.write(json.dumps(r) + "\n")
        return str(p)

    ok = [{"item_id": "a", "kind_name": k, "value": 50.0,
           "model_tag": "mistral-small-24b"}
          for k in ("base", "admit_pre", "admit_post")]
    p = _write("ok.jsonl", ok)
    assert set(sg.load_rows([p])["a"]) == {"base", "admit_pre", "admit_post"}
    with pytest.raises(SystemExit, match="Exclude"):
        sg.load_rows([_write("bad.jsonl",
                             [dict(ok[0], kind_name="exclude_pre")])])
    with pytest.raises(SystemExit, match="Exclude"):
        sg.load_rows([_write("probe.jsonl",
                             [{"item_id": "a", "kind_name":
                               "rule_probe_exclude_post", "p_yes": 0.1,
                               "model_tag": "mistral-small-24b"}])])
    with pytest.raises(SystemExit, match="frozen"):
        sg.load_rows([_write("wrong.jsonl", [dict(ok[0], model_tag="gemma3-12b")])])
    # selection never touches sweep outputs (§9.2 second clause)
    with open(s25.__file__, encoding="utf-8") as fh:
        src = fh.read()
    assert "results/raw/g25" not in src


# ---------------------------------------------------------------------------
# conditions: 16 cells, byte-identical rule, order-only differences
# ---------------------------------------------------------------------------
def test_condition_set_is_the_sixteen_preregistered_cells():
    assert len(G25A_CONDITIONS) == 16
    assert set(G25A_CONDITIONS) == {"g25_base", "g25_norule"} | {
        f"g25_{arm}_{w}" for w in g25.WKEYS for arm in g25.ARMS}
    assert G25A_CONDITIONS == g25.G25A_CONDITIONS   # schema exports the tuple
    assert g25.WKEYS == ("w000", "w001", "w002", "w005", "w010", "w025", "w100")
    assert g25.LOCAL_WKEYS == ("w001", "w002", "w005")
    assert g25.CONTEXT_WKEYS == ("w010", "w025", "w100")
    assert g25.ARMS == ("pre", "post")
    assert [g25.WEIGHTS[w] for w in g25.WKEYS] == \
        [0.0, 0.01, 0.02, 0.05, 0.10, 0.25, 1.00]
    assert g25.G25A_NUMERIC_PROBES == ["wprobe_g25_pre_w000",
                                       "wprobe_g25_pre_w100"]
    assert all(p in PROBES for p in g25.G25A_PROBES)


def _blocks_of(prompt: str):
    return prompt.split("\n\n")


def test_rule_is_the_g23a_function_verbatim_with_exact_wording():
    pct = {"w000": "0", "w001": "1", "w002": "2", "w005": "5",
           "w010": "10", "w025": "25", "w100": "100"}
    it = ITEMS[0]
    for w in g25.WKEYS:
        rule = [b for b in _blocks_of(compile_prompt(it, f"g25_pre_{w}"))
                if b.startswith("RULING")][0]
        assert rule == uniform_weight_rule(it, g25.WEIGHTS[w])
        assert rule == ("RULING\nThe causal weight assigned to evidence E is "
                        f"exactly {pct[w]}% of its normal evidential weight.")
    # cross-round byte identity: G25A and G23A share ONE function object,
    # and with an identical critical_label the rendered sentence is byte-equal
    # (G23A's own items carry other labels — substitute one to compare)
    import conditions_g23a as g23amod
    assert g25.uniform_weight_rule is g23amod.uniform_weight_rule
    import dataclasses
    g23a_sub = dataclasses.replace(build_g23a_items()[0],
                                    critical_label="evidence E")
    for w in ("w000", "w001", "w025", "w100"):
        assert (uniform_weight_rule(g23a_sub, g23amod.WEIGHTS[w])
                == uniform_weight_rule(it, g25.WEIGHTS[w]))


def test_only_the_number_changes_across_weights():
    stripped = None
    for w in g25.WKEYS:
        rule = [b for b in _blocks_of(compile_prompt(ITEMS[0], f"g25_pre_{w}"))
                if b.startswith("RULING")][0]
        without_digits = re.sub(r"\d+%?", "<n>", rule)
        if stripped is None:
            stripped = without_digits
        else:
            assert without_digits == stripped
    # the candidates' admit/exclude strings are NOT used (§3)
    p = compile_prompt(ITEMS[0], "g25_pre_w000")
    assert ITEMS[0].admit_rule not in p
    assert ITEMS[0].exclude_rule not in p


def test_base_and_norule_layouts():
    it = ITEMS[0]
    base = compile_prompt(it, "g25_base")
    assert base.startswith("CLAIM\n")
    assert "RULING" not in base and "EVIDENCE E" not in base
    norule = compile_prompt(it, "g25_norule")
    assert norule.count("EVIDENCE E\n") == 1 and "RULING" not in norule


def test_pre_and_post_differ_only_by_block_order():
    for w in g25.WKEYS:
        pre, post = compile_prompt(ITEMS[0], f"g25_pre_{w}"), \
                    compile_prompt(ITEMS[0], f"g25_post_{w}")
        assert pre != post
        assert sorted(_blocks_of(pre)) == sorted(_blocks_of(post))
        assert pre.count("RULING") == post.count("RULING") == 1
        assert pre.count("EVIDENCE E\n") == post.count("EVIDENCE E\n") == 1
        assert pre.index("RULING") < pre.index("EVIDENCE E\n")
        assert post.index("RULING") > post.index("EVIDENCE E\n")


def test_one_tail_identical_across_all_sixteen_cells():
    it = ITEMS[0]
    tails = {compile_prompt(it, c).split("TASK\n")[-1]
             for c in G25A_CONDITIONS}
    assert len(tails) == 1
    tail = tails.pop()
    assert it.question in tail and it.output_spec in tail
    assert "ANSWER:" in tail            # same answer format everywhere


def test_all_items_compile_every_cell():
    tail = compile_prompt(ITEMS[0], "g25_base").split("TASK\n")[-1]
    for it in ITEMS:
        for c in G25A_CONDITIONS:
            p = compile_prompt(it, c)
            assert p.split("TASK\n")[-1] == tail
        assert compile_prompt(it, "g25_pre_w000") != \
            compile_prompt(it, "g25_pre_w100")


def test_g24a_five_and_g0_dispatch_unaffected_by_g25_branch():
    it = ITEMS[0]
    assert not g25.is_g25("admit_pre") and not g25.is_g25("base")
    assert _blocks(it, "admit_pre") == g24a.blocks(it, "admit_pre")
    assert _blocks(it, "exclude_post") == g24a.blocks(it, "exclude_post")
    g0 = load_items(G0_ITEMS)[0]
    assert compile_prompt(g0, "base").startswith("BACKGROUND\n")
    assert not compile_prompt(g0, "base").startswith("CLAIM\n")


def test_probes_compile_over_the_matching_decision_context():
    it = ITEMS[3]
    for probe, w in (("wprobe_g25_pre_w000", "0"), ("wprobe_g25_pre_w100", "100")):
        q = compile_probe(it, probe)
        assert "TASK\n" in q
        assert WEIGHT_PROBE_Q.format(lab=it.critical_label) in q
        assert f"exactly {w}% of its normal evidential weight" in q
        assert q.index("RULING") < q.index("EVIDENCE E\n")   # pre arm
    # probe question never appears inside a decision prompt (README 3.1)
    probe_q = WEIGHT_PROBE_Q.format(lab=it.critical_label)
    assert all(probe_q not in compile_prompt(it, c) for c in G25A_CONDITIONS)


def test_run_model_and_schema_wiring_locks():
    with open(os.path.join(ROOT, "src/run_model.py"), encoding="utf-8") as fh:
        runner = fh.read()
    assert runner.count("G25A_CONDITIONS") == 2   # import + membership chain
    with open(os.path.join(ROOT, "src/schema.py"), encoding="utf-8") as fh:
        schema_src = fh.read()
    assert "import conditions_g25 as g25" in schema_src
    assert "g25.G25A_PROBES" in schema_src
    assert "g25.is_g25(cond)" in schema_src
    assert "wprobe_g25_" in schema_src


# ---------------------------------------------------------------------------
# analyzer: constants, bootstrap, estimands, gates, decision order
# ---------------------------------------------------------------------------
def test_analyzer_constants_frozen():
    assert a25.SEED == 20260924 and a25.B == 10_000
    assert a25.DESIGN_TAG == "g25a-near-zero-design-v1"
    assert a25.FLOOR == 3.0
    assert a25.MIN_MODELS_POSITIVE == 3
    assert a25.SUFFICIENCY_MIN_ITEMS == 360
    assert a25.SUFFICIENCY_MIN_MODELS == 3
    assert a25.RULEACC_MIN == 0.8 and a25.PROBE_TOL_PP == 2.0
    assert a25.POOLED_MODELS == ["llama31-8b", "qwen3-8b", "qwen35-9b",
                                 "gemma3-12b"]
    assert a25.SELECTOR_TAG == "mistral-small-24b"
    assert a25.SELECTOR_TAG not in a25.POOLED_MODELS
    assert len(a25.REQUIRED) == 16
    assert set(a25.VERDICTS) == set(a25.LICENSED)
    assert set(a25.INTERP) == {"graded", "flat"}


def test_cluster_boot_deterministic_point_ci_and_p():
    import statistics as st
    pairs = [(f"c{i % 5}", (i % 7) / 7.0) for i in range(40)]
    r1 = a25.cluster_boot(pairs, n=200)
    r2 = a25.cluster_boot(pairs, n=200)
    assert r1 == r2
    assert abs(r1["mean"] - st.mean(v for _, v in pairs)) < 1e-12
    assert r1["ci_low"] <= r1["mean"] <= r1["ci_high"]
    assert 0.0 <= r1["p"] <= 1.0
    assert r1["n"] == 40 and r1["n_clusters"] == 5
    empty = a25.cluster_boot([])
    assert empty["n"] == 0 and math_isnan(empty["mean"])


def math_isnan(x):
    import math
    return math.isnan(x)


def test_cluster_integrity_resamples_whole_clusters():
    """A replicate is a whole-cluster draw: with A={1,1}, B={0} only
    cluster-size-weighted means {1, 2/3, 0} are reachable — row-level
    resampling would also produce 1/3."""
    by = {"A": [1.0, 1.0], "B": [0.0]}
    point, reps = a25._boot_reps(by, n=400, seed=a25.SEED)
    allowed = [1.0, 2.0 / 3.0, 0.0]
    assert all(any(abs(x - a) < 1e-9 for a in allowed) for x in reps)
    assert not any(abs(x - 1.0 / 3.0) < 1e-9 for x in reps)
    assert abs(point - 2.0 / 3.0) < 1e-12


def _cells(item_id, direction="increase", **over):
    # complete case = all 16 prereg cells, incl. the norule control cell
    cells = {"g25_base": 50.0, "g25_norule": 50.0}
    for w in g25.WKEYS:
        cells[f"g25_pre_{w}"] = 50.0
        cells[f"g25_post_{w}"] = 50.0
    # a positive anchor by default: w100 both arms lift20 points signed
    s = 1.0 if direction == "increase" else -1.0
    for arm in ("pre", "post"):
        cells[f"g25_{arm}_w100"] = 50.0 + s * 20.0
    cells.update(over)
    return [{"item_id": item_id, "kind_name": k, "value": v}
            for k, v in cells.items()]


def _raw(path, rows):
    with open(path, "w") as fh:
        for row in rows:
            fh.write(json.dumps(row) + "\n")


def test_rows_estimands_both_directions_and_usability_drops(tmp_path):
    from analyze_g25 import rows_for
    items = {i.item_id: i for i in ITEMS}
    up = ITEMS[0]
    assert up.critical_direction == "increase"   # file leads with fever SUPPORTS
    dn = next(i for i in ITEMS if i.critical_direction == "decrease")
    path = tmp_path / "raw.jsonl"

    # +direction: leverage 20 via w100 anchor; put graded structure in place.
    # pre arm loses an extra 8 points ONLY at w000; post arm tracks levels.
    lvl = {"w000": 0.0, "w001": 4.0, "w002": 6.0, "w005": 8.0,
           "w010": 12.0, "w025": 16.0, "w100": 20.0}
    over = {}
    for w in g25.WKEYS:
        over[f"g25_pre_{w}"] = 50.0 + lvl[w] + (8.0 if w == "w000" else 0.0)
        over[f"g25_post_{w}"] = 50.0 + lvl[w]
    rows_in = _cells(up.item_id, "increase", **over)
    # −direction: evidence pulls DOWN; cells below base must sign-align +
    over_dn = {k: 50.0 - (v - 50.0) for k, v in over.items()
               if k != "g25_base"}
    rows_in += _cells(dn.item_id, "decrease", **over_dn)
    # unusable: anchor cells forced flat onto base -> L = 0 -> s·L <= 0
    flat = dict(over)
    flat["g25_pre_w100"] = 50.0
    flat["g25_post_w100"] = 50.0
    rows_in += _cells(ITEMS[2].item_id, "increase", **flat)
    # incomplete: one decision cell missing
    rows_in += [r for r in _cells(ITEMS[3].item_id, "increase")
                if r["kind_name"] != "g25_post_w005"]
    # unknown item id
    rows_in += _cells("no_such_item", "increase")
    _raw(path, rows_in)

    rows, drops = rows_for(items, str(path))
    assert drops["unknown_item"] == 1
    assert drops["nonpositive_anchor"] == 1
    assert drops["incomplete"] == 1
    assert len(rows) == 2
    r = next(x for x in rows if x["item_id"] == up.item_id)
    assert r["s"] == 1.0
    assert r["gap"]["w000"] == pytest.approx(8.0)
    assert all(r["gap"][w] == pytest.approx(0.0) for w in g25.WKEYS
               if w != "w000")
    assert r["delta_local0"] == pytest.approx(8.0)
    assert r["gap01"] == pytest.approx(8.0)
    assert r["L"] == pytest.approx(20.0) and r["sL"] == pytest.approx(20.0)
    assert r["resp"]["w100"] == pytest.approx(20.0)
    assert r["gradedpos"] == pytest.approx(20.0 - (4.0 + 6.0 + 8.0) / 3.0)
    assert r["rei"][("pre", "w100")] == pytest.approx(20.0 / 20.0)
    rd = next(x for x in rows if x["item_id"] == dn.item_id)
    assert rd["s"] == -1.0
    # identical signed structure after sign alignment (both directions, §9.7)
    assert rd["gap"]["w000"] == pytest.approx(8.0)
    assert rd["delta_local0"] == pytest.approx(8.0)
    assert rd["sL"] == pytest.approx(20.0)
    assert rd["cluster"] == f"{dn.meta['source']}/{dn.meta['cluster']}"


def test_probes_for_ruleacc_and_unparsed(tmp_path):
    from analyze_g25 import probes_for
    path = tmp_path / "raw.jsonl"
    rows = [
        {"item_id": "a", "kind_name": "wprobe_g25_pre_w000", "value": 0.0},
        {"item_id": "b", "kind_name": "wprobe_g25_pre_w000", "value": 1.0},
        {"item_id": "c", "kind_name": "wprobe_g25_pre_w000", "value": 5.0},
        {"item_id": "d", "kind_name": "wprobe_g25_pre_w000", "value": None},
        {"item_id": "a", "kind_name": "wprobe_g25_pre_w100", "value": 100.0},
        {"item_id": "b", "kind_name": "wprobe_g25_pre_w100", "value": 98.0},
        {"item_id": "c", "kind_name": "wprobe_g25_pre_w100", "value": 70.0},
    ]
    _raw(path, rows)
    out = probes_for(str(path))
    assert out["n_probe_rows"] == 7 and out["n_unparsed"] == 1
    assert out["n_probe_parsed"] == 6
    assert out["stated_weight"]["w000"]["n"] == 3
    assert out["stated_weight"]["w000"]["median_abs_error_pp"] == 1.0
    assert out["stated_weight"]["w000"]["frac_within_tol"] == pytest.approx(2 / 3)
    assert out["stated_weight"]["w100"]["frac_within_tol"] == pytest.approx(2 / 3)
    assert out["rule_acc"] == pytest.approx(4 / 6)
    assert "w001" not in out["stated_weight"]


def test_gate_is_ci_strict_plus_frozen_floor():
    assert a25.gate({"n": 5, "mean": 4.0, "ci_low": 0.5, "ci_high": 5.0}) is True
    assert a25.gate({"n": 5, "mean": 2.9, "ci_low": 0.5, "ci_high": 5.0}) is False
    assert a25.gate({"n": 5, "mean": 4.0, "ci_low": 0.0, "ci_high": 5.0}) is False
    assert a25.gate({"n": 5, "mean": float("nan"), "ci_low": float("nan"),
                     "ci_high": float("nan")}) is False
    assert a25.gate(None) is False


def _stats(mean, lo, hi, n=10):
    return {"n": n, "n_clusters": 5, "mean": mean, "ci_low": lo,
            "ci_high": hi, "p": 0.0}


def test_classify_is_literal_six_input_decision_order():
    """§8: integrity → sufficiency → co-primaries, top-down table rows."""
    pos = _stats(8.0, 6.0, 10.0)
    strad = _stats(0.5, -2.0, 3.0)
    neg = _stats(-4.0, -7.0, -1.0)
    empty = _stats(float("nan"), float("nan"), float("nan"), n=0)
    # table row 1
    assert a25.classify(True, True, True, True, True, pos) == \
        "exact-zero-boundary"
    # table row 2 (precedence over row 3: G1 fails while Gap(0)>0)
    assert a25.classify(True, True, True, False, True, pos) == \
        "boundary-not-replicated"
    assert a25.classify(True, True, True, False, False, pos) == \
        "boundary-not-replicated"
    # table row 3: G1 passes, G2 fails -> partial (row 2 cannot fire)
    assert a25.classify(True, True, True, True, False, pos) == \
        "partial-boundary"
    # table row 4
    assert a25.classify(True, True, True, False, False, strad) == \
        "no-natural-gap"
    # integrity first, regardless of endpoints
    assert a25.classify(False, True, True, True, True, pos) == "order-artifact"
    assert a25.classify(True, False, True, True, True, pos) == "order-artifact"
    # sufficiency second
    assert a25.classify(True, True, False, True, True, pos) == "unresolved"
    # no evaluable data: not an integrity event
    assert a25.classify(True, True, True, True, True, empty) == "unresolved"
    # negative-significant Gap(0) with both gates failed: no row fits
    assert a25.classify(True, True, True, False, False, neg) == "unresolved"


def test_gradedness_cannot_reach_the_verdict_function():
    """User ruling 2026-09-24: GradedPos is never a third gate."""
    sig = inspect.signature(a25.classify)
    assert list(sig.parameters) == ["i1", "i2", "s1", "g1", "g2", "gap0"]
    assert a25.classify.__code__.co_argcount == 6
    assert not any("graded" in v or "resp" in v
                   for v in a25.classify.__code__.co_varnames)
    # the §6 label is computed strictly outside the verdict path
    assert a25.gradedness_label(_stats(14.0, 13.0, 15.0)) == "graded"
    assert a25.gradedness_label(_stats(0.0, -1.0, 1.0)) == "flat"
    assert a25.gradedness_label(_stats(float("nan"), float("nan"),
                                       float("nan"), n=0)) == "flat"


# ---------------------------------------------------------------------------
# wording locks
# ---------------------------------------------------------------------------
def test_wording_locks_register_verbatim_and_forbidden_phrases():
    with open(a25.__file__, encoding="utf-8") as fh:
        src = fh.read()
    # register §12.3 Finding 2 form stays the verbatim licensed claim
    assert a25.LICENSED["exact-zero-boundary"].startswith(
        "Complete semantic causal exclusion shows an additional prospective "
        "cost even though")
    # §1/§8 three-way split phrasings, byte-aligned
    assert "sharp zero boundary over graded semantic weighting" in \
        a25.INTERP["graded"]
    # §1's verbatim downgraded form (hyphenated before "regime"; §1 line 75)
    assert "categorical zero-vs-nonzero semantic-control regime" in \
        a25.INTERP["flat"]
    # the forbidden operation appears only in "never ..." form
    assert ("never \"a dedicated semantic nullification operation\""
            in a25.INTERP["flat"])
    # "nullification operation" appears ONLY inside a "never ..." prohibition
    for m in re.finditer(r"nullification operation", src):
        assert "never" in src[max(0, m.start() - 60):m.start()]
    assert "nullification operation" not in a25.LICENSED["exact-zero-boundary"]
    # generic frame owned by ACL 2026 Main is never used (gate5 hazard)
    assert "representation-vs-deployment" not in src
    assert "in-context unlearning" not in src
    # prereg carries the locks too (whitespace-folded: lines are hard-wrapped)
    with open(PREREG, encoding="utf-8") as fh:
        prereg = " ".join(fh.read().split())
    assert "0b38e0837ed9fd60" in prereg
    assert "never \"a dedicated semantic nullification operation\"" in prereg
    assert "categorical zero-vs-nonzero semantic control" in prereg
    assert "not a gate" in prereg
    assert "This document does not authorize itself" in prereg
    assert "Register §12.3 form remains the verbatim licensed claim" in prereg


# ---------------------------------------------------------------------------
# end-to-end (synthetic panel, no model): verdict + gradedness split
# ---------------------------------------------------------------------------
def _mkitem(iid, direction, source, cluster, gold, rank):
    return Item(**dict(
        item_id=iid, task_family=f"g24a_{source}",
        surface_domain="wikipedia", base_context=f"claim {iid}",
        critical_evidence=f"evidence {iid}", critical_label="evidence E",
        critical_direction=direction, exclusion_reason="none_stured",
        evidence_truth="true_but_forbidden", admit_rule=g24a.ADMIT_RULE,
        exclude_rule=g24a.EXCLUDE_RULE, question=g24a.QUESTION,
        output_spec=g24a.OUTPUT_SPEC, memory_question="",
        rule_probe_question=g24a.RULE_PROBE_QUESTION, ground_truth=None,
        meta={"source": source, "gold_label": gold, "cluster": cluster,
              "stratum": f"{source}/{gold}", "candidate_rank": rank}))


def _synth_items():
    """400 items in the frozen strata shape, 200 pair-clusters."""
    items, rank = [], 0
    for source, gold, n, direction in (
            ("fever", "SUPPORTS", 150, "increase"),
            ("fever", "REFUTES", 150, "decrease"),
            ("scifact", "SUPPORT", 100, "increase")):
        for i in range(n):
            items.append(_mkitem(f"g25syn_{source}_{gold}_{i}", direction,
                                 source, f"{source[:3]}_c{i // 2}", gold, rank))
            rank += 1
    return items


_LEVELS = {"w000": 0.0, "w001": 4.0, "w002": 6.0, "w005": 8.0,
           "w010": 12.0, "w025": 16.0, "w100": 20.0}
_FLAT = {"w000": 0.0, "w001": 8.0, "w002": 8.0, "w005": 8.0,
         "w010": 8.0, "w025": 8.0, "w100": 8.0}


def _extra(mode, w):
    """Timing cost carried by the pre arm, by weight, per scenario."""
    if mode in ("graded", "flat", "suff"):
        return 8.0 if w == "w000" else 0.0
    if mode == "smooth":                 # gap everywhere except the anchor
        return 0.0 if w == "w100" else 8.0
    if mode == "null":                   # no timing gap anywhere
        return 0.0
    raise ValueError(mode)


def _rows_one(d, midx, mode):
    iid = d.item_id
    i = int(iid.rsplit("_", 1)[1])
    s = 1.0 if d.critical_direction == "increase" else -1.0
    levels = _FLAT if mode == "flat" else _LEVELS
    base = 40.0 + (i % 17)
    rows = [{"item_id": iid, "kind_name": "g25_base",
             "value": base, "model_tag": a25.POOLED_MODELS[midx]},
            {"item_id": iid, "kind_name": "g25_norule",
             "value": base, "model_tag": a25.POOLED_MODELS[midx]}]
    for w in g25.WKEYS:
        for arm in ("pre", "post"):
            resinf = levels[w] + (_extra(mode, w) if arm == "pre" else 0.0)
            rows.append({"item_id": iid,
                         "kind_name": f"g25_{arm}_{w}",
                         "value": base + s * resinf,
                         "model_tag": a25.POOLED_MODELS[midx]})
    # usability kill for the sufficiency scenario: models 0/1 lose the anchor
    if mode == "suff" and midx < 2 and i < 100:
        for r in rows:
            if r["kind_name"] in ("g25_pre_w100", "g25_post_w100"):
                r["value"] = base     # L = 0 -> s·L <= 0 -> unusable here
    # O3 probes: exact recall -> RuleAcc = 1.0
    rows.append({"item_id": iid, "kind_name": "wprobe_g25_pre_w000",
                 "value": 0.0, "model_tag": a25.POOLED_MODELS[midx]})
    rows.append({"item_id": iid, "kind_name": "wprobe_g25_pre_w100",
                 "value": 100.0, "model_tag": a25.POOLED_MODELS[midx]})
    return rows


def _e2e(tmp_path, mode):
    items = _synth_items()
    items_path = tmp_path / "items.jsonl"
    with open(items_path, "w") as fh:
        for d in items:
            fh.write(d.to_json() + "\n")
    run_files = []
    for midx, tag in enumerate(a25.POOLED_MODELS):
        recs = [r for d in items for r in _rows_one(d, midx, mode)]
        p = tmp_path / f"{tag}.jsonl"
        with open(p, "w") as fh:
            for r in recs:
                fh.write(json.dumps(r) + "\n")
        run_files.append(str(p))

    old_b = a25.B
    a25.B = 200                      # fast tests; engine unchanged
    old_argv = sys.argv
    try:
        sys.argv = ["analyze_g25.py", "--runs", *run_files,
                    "--items", str(items_path), "--tag", "synth",
                    "--out-prefix", str(tmp_path / "out")]
        rc = a25.main()
    finally:
        sys.argv = old_argv
        a25.B = old_b
    assert rc == 0
    md = open(tmp_path / "out.md").read()
    res = json.load(open(tmp_path / "out.json"))
    return md, res


def test_e2e_boundary_with_graded_positives(tmp_path):
    md, res = _e2e(tmp_path, "graded")
    assert res["verdict"] == "exact-zero-boundary"
    assert res["gradedness_label"] == "graded"
    assert "sharp zero boundary over graded semantic weighting" in \
        res["gradedness_interpretation"]
    g = res["gates"]
    assert g["i1_gap_w100_ci_contains_0"] is True
    assert g["i2_ruleacc_ge_min"] is True
    assert g["s1_usable_items_ge_min"] is True
    assert g["g1_delta_local0"] is True and g["g2_gap01"] is True
    assert all(v["pass"] for v in g["g3_models_positive"].values())
    assert res["design_tag"] == "g25a-near-zero-design-v1"
    assert res["ledger"] and set(res["ledger"]) == set(a25.POOLED_MODELS)
    assert "## Verdict" in md and "**exact-zero-boundary**" in md
    assert res["strata"]["stratum fever/SUPPORTS"]["n"] == 150 * 4
    assert res["items_sha256"] and len(res["runs_sha256"]) == 4


def test_e2e_same_verdict_under_flat_positives(tmp_path):
    """boundary + flat positives: SAME verdict, only the mechanism sentence
    downgrades — gradedness never flips a primary result (§1 split)."""
    md, res = _e2e(tmp_path, "flat")
    assert res["verdict"] == "exact-zero-boundary"
    assert res["gradedness_label"] == "flat"
    assert res["gradedness_interpretation"].count(
        "categorical zero-vs-nonzero semantic-control regime") == 1
    assert "never \"a dedicated semantic nullification operation\"" in \
        res["gradedness_interpretation"]
    assert res["gates"]["g1_delta_local0"] is True
    assert res["gates"]["g2_gap01"] is True
    assert "categorical zero-vs-nonzero semantic-control regime" in md


def test_e2e_smooth_response_kills_the_boundary(tmp_path):
    md, res = _e2e(tmp_path, "smooth")
    assert res["verdict"] == "boundary-not-replicated"
    assert res["gates"]["g1_delta_local0"] is False
    assert res["gates"]["g2_gap01"] is False
    assert res["gradedness_interpretation"] is None
    assert "withdrawn for natural materials" in res["licensed"]


def test_e2e_no_gap_anywhere_is_no_natural_gap(tmp_path):
    md, res = _e2e(tmp_path, "null")
    assert res["verdict"] == "no-natural-gap"
    assert res["gates"]["i1_gap_w100_ci_contains_0"] is True
    assert "does not manifest on natural materials" in res["licensed"]


def test_e2e_sufficiency_gate_wins_over_passing_primaries(tmp_path):
    """S1 is evaluated BEFORE the co-primaries: a passing shape on300
    items is `unresolved`, not a boundary."""
    md, res = _e2e(tmp_path, "suff")
    assert res["verdict"] == "unresolved"
    assert res["gates"]["s1_usable_items_ge_min"] is False
    assert res["gates"]["usable_items_ge_3of4"] < 360
    # the primaries still pass on the surviving rows — and must not matter
    assert res["gates"]["g1_delta_local0"] is True
    assert "not evaluable as preregistered" in res["licensed"].lower()
