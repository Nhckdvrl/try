"""G24A design tests — nothing here touches a model.

Runs on code, the frozen candidates file and synthetic records only:

* prereg §9 controls — character-identical PRE/POST rulings, selection
  blindness (Base/Admit rows only; first-eligible quotas), G0 prompt
  non-interference, identical question/output tail, gold-label sign
  convention, cluster integrity of the pooled bootstrap;
* the builder's frozen strata order and metadata literals;
* the selector's leverage math, τ boundary, quota/shortfall behaviour and its
  guards;
* the analyzer's inherited G0 estimands, frozen inference constants, the §8
  literal decision order, the §7 sufficiency gate, and two end-to-end runs
  (confirmatory path and no-leak path);
* the prereg wording lock (verdict names and licensed claims byte-aligned).
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys

import pytest

import conditions_g24a as g24a
from build_g24a_items import items_from_pools, STRATA, FROZEN_STRATA_COUNTS, SEED
import select_g24a as sg
import analyze_g24a as ag
from schema import (CONDITIONS, PROBES, Item, _blocks, compile_probe,
                    compile_prompt, load_items)

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
CAND = os.path.join(ROOT, "data", "items", "g24a_candidates_v1.jsonl")
CAND_SHA = "91ebad9850d6f7d39a9b26fcf98c1f998d16aa68cde3a480541df13da721f5cd"
PREREG = os.path.join(ROOT, "preregistrations",
                      "PREREGISTRATION_G24A_NATURAL_EVIDENCE.md")
G0_ITEMS = os.path.join(ROOT, "data", "items", "items_v1.jsonl")

ITEMS = load_items(CAND)
FIVE = ["base", "admit_pre", "admit_post", "exclude_pre", "exclude_post"]
TRIPLE = ["rule_probe_exclude_pre", "rule_probe_exclude_post",
          "rule_probe_admit_post"]
MODEL_TAGS = ["gemma3-12b", "llama31-8b", "mistral-small-24b",
              "qwen3-8b", "qwen35-9b"]


# ---------------------------------------------------------------------------
# candidates file (frozen input of the selection pass)
# ---------------------------------------------------------------------------
def test_candidates_sha256_frozen():
    assert hashlib.sha256(open(CAND, "rb").read()).hexdigest() == CAND_SHA


def test_candidates_strata_counts_order_and_ranks():
    assert len(ITEMS) == 13283
    got = {}
    for it in ITEMS:
        got[it.meta["stratum"]] = got.get(it.meta["stratum"], 0) + 1
    want = {f"{s}/{l}": n for (s, l), n in FROZEN_STRATA_COUNTS.items()}
    assert got == want
    # frozen strata blocks in prereg §5.1 order, ranks = file positions
    assert [it.meta["candidate_rank"] for it in ITEMS] == list(range(13283))
    bounds, start = [], 0
    for (s, l), n in FROZEN_STRATA_COUNTS.items():
        bounds.append((start, start + n, f"{s}/{l}"))
        start += n
    assert start == 13283
    for lo, hi, stratum in bounds:
        assert all(ITEMS[i].meta["stratum"] == stratum for i in range(lo, hi))
    # explicit prereg §5.1 order
    assert [b[2] for b in bounds] == ["fever/SUPPORTS", "fever/REFUTES",
                                      "scifact/SUPPORT", "scifact/CONTRADICT"]
    assert len({it.item_id for it in ITEMS}) == 13283


def test_candidates_metadata_literals_and_sign_convention():
    label_dir = {"SUPPORTS": "increase", "SUPPORT": "increase",
                 "REFUTES": "decrease", "CONTRADICT": "decrease"}
    for it in ITEMS:
        assert it.exclusion_reason == "none_stated"
        assert it.evidence_truth == "true_but_forbidden"
        assert it.admit_rule == g24a.ADMIT_RULE
        assert it.exclude_rule == g24a.EXCLUDE_RULE
        assert it.question == g24a.QUESTION
        assert it.output_spec == g24a.OUTPUT_SPEC
        assert it.rule_probe_question == g24a.RULE_PROBE_QUESTION
        assert it.memory_question == ""
        assert it.ground_truth is None
        assert it.critical_label == "evidence E"
        assert it.task_family == f"g24a_{it.meta['source']}"
        assert it.critical_direction == label_dir[it.meta["gold_label"]]  # §9.5
        assert it.meta["cluster"]
        assert it.meta["stratum"] == f"{it.meta['source']}/{it.meta['gold_label']}"


# ---------------------------------------------------------------------------
# §9.1 rule identity, §3 block orders, §9.4 tail, §9.3 G0 non-interference
# ---------------------------------------------------------------------------
def test_rule_identity_pre_post_byte_identical():
    for it in ITEMS:
        b = [_blocks(it, c) for c in FIVE]
        assert b[1][1] == b[2][2], it.item_id          # ADMIT text pre == post
        assert b[3][1] == b[4][2], it.item_id          # EXCLUDE text pre == post
        assert b[1][1] == "RULING\n" + g24a.ADMIT_RULE
        assert b[3][1] == "RULING\n" + g24a.EXCLUDE_RULE


def test_block_orders_exact_all_items():
    for it in ITEMS:
        base, apre, apost, epre, epost = [_blocks(it, c) for c in FIVE]
        assert len(base) == 1 and base[0].startswith("CLAIM\n")
        assert "EVIDENCE E\n" not in base[0]
        for b, arm in ((apre, "admit"), (epre, "exclude")):
            assert len(b) == 3 and b[0].startswith("CLAIM\n")
            assert b[1].startswith("RULING\nEvidence E is " + arm)  # rule PRE
            assert b[2].startswith("EVIDENCE E\n")
        for b, arm in ((apost, "admit"), (epost, "exclude")):
            assert len(b) == 3 and b[0].startswith("CLAIM\n")
            assert b[1].startswith("EVIDENCE E\n")
            assert b[2].startswith("RULING\nEvidence E is " + arm)   # rule POST
        assert "\nBACKGROUND\n" not in "".join(apre)


def test_prompt_tail_identical_across_conditions():
    sample = ITEMS[::97]
    assert len(sample) >= 100
    for it in sample:
        tails, prompts = None, [compile_prompt(it, c) for c in FIVE]
        for p in prompts:
            i = p.rindex("\nTASK\n")
            tail = p[i:]
            tails = tail if tails is None else tails
            assert tail == tails
            assert g24a.QUESTION in tail and g24a.OUTPUT_SPEC in tail
        assert prompts[0].startswith("CLAIM\n")
        assert "\nEVIDENCE E\n" not in prompts[0]
        for p in prompts[1:]:
            assert "\nEVIDENCE E\n" in p and "\nRULING\n" in p
        # pre: ruling text precedes evidence; post: evidence precedes ruling
        i_rule_pre = prompts[3].index("RULING\n")
        i_evid_pre = prompts[3].index("EVIDENCE E\n")
        assert i_rule_pre < i_evid_pre
        i_evid_post = prompts[4].index("EVIDENCE E\n")
        i_rule_post = prompts[4].index("RULING\n")
        assert i_evid_post < i_rule_post


def test_g0_items_prompts_unchanged_by_dispatch():
    g0 = load_items(G0_ITEMS)[0]
    base = compile_prompt(g0, "base")
    assert base.startswith("BACKGROUND\n")
    assert not base.startswith("CLAIM\n")
    exc = compile_prompt(g0, "exclude_post")
    assert exc.startswith("BACKGROUND\n")
    assert "\nRULING\n" + g0.exclude_rule in exc
    assert "\nCLAIM\n" not in exc
    # dispatch both ways
    assert _blocks(ITEMS[0], "base") == g24a.blocks(ITEMS[0], "base")
    assert _blocks(g0, "base") != g24a.blocks(ITEMS[0], "base")


def test_probe_and_condition_wiring():
    assert set(g24a.G24A_CONDITIONS) == set(FIVE)
    assert set(FIVE) <= set(CONDITIONS)
    assert set(TRIPLE) <= set(PROBES)
    for it in (ITEMS[0], next(x for x in ITEMS if x.meta["source"] == "scifact")):
        p_pre = compile_probe(it, "rule_probe_exclude_pre")
        p_post = compile_probe(it, "rule_probe_exclude_post")
        p_adm = compile_probe(it, "rule_probe_admit_post")
        for p in (p_pre, p_post, p_adm):
            assert g24a.RULE_PROBE_QUESTION in p and p.endswith("YES or NO.")
        assert p_pre.index("RULING\n") < p_pre.index("EVIDENCE E\n")
        assert p_post.index("EVIDENCE E\n") < p_post.index("RULING\n")
        assert "is excluded" in p_pre and "is excluded" in p_post
        assert "is admitted" in p_adm


# ---------------------------------------------------------------------------
# builder (pure function)
# ---------------------------------------------------------------------------
def _fever_rec(i, label):
    return {"source": "fever", "fever_id": 1000 + i, "label": label,
            "direction": "increase" if label == "SUPPORTS" else "decrease",
            "claim": f"claim{i}", "evidence_block": f"evidence{i}",
            "evidence_sentences": [f"sent{i}"], "cluster": f"page{i}",
            "evidence_pages": [f"page{i}"], "n_groups": 2, "group0_tuples": 1}


def _sci_rec(i, label):
    return {"source": "scifact", "scifact_id": i, "split": "train",
            "label": label,
            "direction": "increase" if label == "SUPPORT" else "decrease",
            "claim": f"claim{i}", "evidence_block": f"evidence{i}",
            "evidence_sentences": [f"sent{i}"], "cluster": str(500 + i),
            "evidence_doc_id": 500 + i, "rationale_idxs": [0]}


def _mini_pools():
    fever = [_fever_rec(i, "SUPPORTS") for i in range(6)] + \
            [_fever_rec(10 + i, "REFUTES") for i in range(6)]
    sci = [_sci_rec(i, "SUPPORT") for i in range(6)] + \
          [_sci_rec(10 + i, "CONTRADICT") for i in range(6)]
    return fever, sci


def test_builder_frozen_order_determinism_and_ids():
    fever, sci = _mini_pools()
    a = items_from_pools(fever, sci)
    b = items_from_pools(list(fever), list(sci))
    assert json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)  # determinism
    assert len(a) == 24
    assert [x["meta"]["candidate_rank"] for x in a] == list(range(24))
    strata = [x["meta"]["stratum"] for x in a]
    assert strata == ["fever/SUPPORTS"] * 6 + ["fever/REFUTES"] * 6 + \
           ["scifact/SUPPORT"] * 6 + ["scifact/CONTRADICT"] * 6
    ids = [x["item_id"] for x in a]
    # within-stratum order is shuffled: membership, not position
    assert set(ids[:6]) == {f"g24a_fever_{1000 + i}" for i in range(6)}
    assert set(ids[6:12]) == {f"g24a_fever_{1010 + i}" for i in range(6)}
    assert set(ids[12:18]) == {f"g24a_scifact_{i}" for i in range(6)}
    assert set(ids[18:24]) == {f"g24a_scifact_{10 + i}" for i in range(6)}
    # metadata passthrough (positional after shuffle -> check by construction)
    for x in a:
        assert x["critical_direction"] == \
            ("increase" if x["meta"]["source"] == "fever" and
             x["meta"]["gold_label"] == "SUPPORTS" or
             x["meta"]["source"] == "scifact" and
             x["meta"]["gold_label"] == "SUPPORT" else "decrease")
        assert x["meta"]["block_chars"] == len(x["critical_evidence"])
        assert x["admit_rule"] == g24a.ADMIT_RULE
    by_id = {x["item_id"]: x for x in a}
    s0 = by_id["g24a_scifact_0"]
    assert s0["meta"]["cluster"] == "500" and s0["meta"]["evidence_doc_id"] == 500
    f3 = by_id["g24a_fever_1003"]
    assert f3["meta"]["cluster"] == "page3"
    # a different seed must produce a different order for these fixed inputs
    c = items_from_pools(list(fever), list(sci), seed=7)
    assert [x["item_id"] for x in c] != ids


# ---------------------------------------------------------------------------
# selector
# ---------------------------------------------------------------------------
def test_selector_constants_frozen():
    assert sg.TAU == 10.0
    assert sg.QUOTAS == {("fever", "SUPPORTS"): 200, ("fever", "REFUTES"): 200,
                         ("scifact", "SUPPORT"): 100,
                         ("scifact", "CONTRADICT"): 100}
    assert sg.SELECT_KINDS == {"base", "admit_pre", "admit_post"}
    assert not any("exclude" in k or "probe" in k for k in sg.SELECT_KINDS)
    assert sg.SELECTION_MODEL_TAG == "mistral-small-24b"
    assert SEED == 20260924


def test_leverage_math_both_directions_and_missing():
    up = {"critical_direction": "increase"}
    dn = {"critical_direction": "decrease"}
    assert sg.leverage(up, {"base": 50, "admit_pre": 60, "admit_post": 70}) == 15.0
    assert sg.leverage(dn, {"base": 50, "admit_pre": 40, "admit_post": 30}) == 15.0
    assert sg.leverage(up, {"base": 50, "admit_post": 70}) is None
    assert sg.leverage(up, None) is None


def _cand(source, label, idx, direction, iid):
    return {"item_id": iid, "critical_direction": direction,
            "meta": {"source": source, "gold_label": label,
                     "candidate_rank": idx}}


def test_select_first_eligible_quota_boundary_and_shortfall():
    q = {("fever", "SUPPORTS"): 2, ("fever", "REFUTES"): 4,
         ("scifact", "SUPPORT"): 2, ("scifact", "CONTRADICT"): 2}
    cands = [
        # fever/SUPPORTS: 9.99 ineligible, then10.0 (τ boundary, inclusive),
        #15 selected, third eligible never examined once quota hit
        _cand("fever", "SUPPORTS", 0, "increase", "f0"),
        _cand("fever", "SUPPORTS", 1, "increase", "f1"),
        _cand("fever", "SUPPORTS", 2, "increase", "f2"),
        _cand("fever", "SUPPORTS", 3, "increase", "f3"),
        # fever/REFUTES: all eligible but pool exhausted before quota
        _cand("fever", "REFUTES", 4, "decrease", "r0"),
        _cand("fever", "REFUTES", 5, "decrease", "r1"),
        # scifact/SUPPORT: one missing value, one eligible
        _cand("scifact", "SUPPORT", 6, "increase", "s0"),
        _cand("scifact", "SUPPORT", 7, "increase", "s1"),
        # scifact/CONTRADICT: both below τ
        _cand("scifact", "CONTRADICT", 8, "decrease", "c0"),
        _cand("scifact", "CONTRADICT", 9, "decrease", "c1"),
    ]
    rows = {
        "f0": {"base": 50, "admit_pre": 59.99, "admit_post": 59.99},  #9.99
        "f1": {"base": 50, "admit_pre": 60, "admit_post": 60},        #10.0 == τ
        "f2": {"base": 50, "admit_pre": 65, "admit_post": 65},        #15
        "f3": {"base": 50, "admit_pre": 70, "admit_post": 70},        #20
        "r0": {"base": 50, "admit_pre": 30, "admit_post": 30},        #20
        "r1": {"base": 50, "admit_pre": 25, "admit_post": 25},        #25
        "s0": {"base": 50, "admit_post": 90},                         # missing
        "s1": {"base": 50, "admit_pre": 62, "admit_post": 62},        #12
        "c0": {"base": 50, "admit_pre": 47.5, "admit_post": 47.5},    #5 < τ
        "c1": {"base": 50, "admit_pre": 47, "admit_post": 47},        #6 < τ
    }
    sel, rep = sg.select(cands, rows, quotas=q)
    assert [x["item_id"] for x in sel] == ["f1", "f2", "r0", "r1", "s1"]
    assert all(any(x is c for c in cands) for x in sel)               # same records
    st = rep["strata"]
    assert st["fever/SUPPORTS"] == dict(pool=4, examined=3, eligible=2,
                                        selected=2, missing_value=0,
                                        below_tau=1, quota=2, shortfall=0)
    assert st["fever/REFUTES"] == dict(pool=2, examined=2, eligible=2,
                                       selected=2, missing_value=0,
                                       below_tau=0, quota=4, shortfall=2)
    assert st["scifact/SUPPORT"] == dict(pool=2, examined=2, eligible=1,
                                         selected=1, missing_value=1,
                                         below_tau=0, quota=2, shortfall=1)
    assert st["scifact/CONTRADICT"] == dict(pool=2, examined=2, eligible=0,
                                            selected=0, missing_value=0,
                                            below_tau=2, quota=2, shortfall=2)
    assert rep["selected_total"] == 5 and rep["quota_total"] == 10
    assert rep["all_quotas_filled"] is False
    assert rep["leverage_selected_min"] == 10.0        # τ boundary inclusive
    assert rep["leverage_selected_p50"] == 15.0        # sorted [10,12,15,20,25]
    assert rep["leverage_selected_max"] == 25.0
    assert rep["tau"] == 10.0 and rep["seed_order"] == 20260924


def test_select_real_shape_full_walk_regression():
    """Real-shaped quotas (200/200/100/100): the first stratum fills its
    quota before the others are touched — the walk MUST continue (the global
    stop compares every stratum's own stats). Guards the bug where the
    current stratum was compared against all quotas, stopping as soon as it
    reached the largest quota value."""
    q = dict(sg.QUOTAS)                      # frozen real quotas
    cands, rows = [], {}
    shape = [(("fever", "SUPPORTS"), "increase", 300),
             (("fever", "REFUTES"), "decrease", 200),
             (("scifact", "SUPPORT"), "increase", 100),
             (("scifact", "CONTRADICT"), "decrease", 100)]
    idx = 0
    for (source, label), direction, n in shape:
        for j in range(n):
            iid = f"{source}_{label}_{j}"
            cands.append(_cand(source, label, idx, direction, iid))
            idx += 1
            rows[iid] = {"base": 50.0,
                         "admit_pre": 50.0 + (15.0 if direction == "increase"
                                              else -15.0),
                         "admit_post": 50.0 + (15.0 if direction == "increase"
                                               else -15.0)}
    sel, rep = sg.select(cands, rows, quotas=q)
    st = rep["strata"]
    # every stratum walked to exhaustion of its candidate list
    assert [st[k]["pool"] for k in
            ["fever/SUPPORTS", "fever/REFUTES",
             "scifact/SUPPORT", "scifact/CONTRADICT"]] == [300, 200, 100, 100]
    assert sum(x["selected"] for x in st.values()) == 600
    assert rep["selected_total"] == 600 and rep["all_quotas_filled"] is True
    # first-eligible in frozen order: FS ranks0..199, then FR starts at300
    assert [x["meta"]["candidate_rank"] for x in sel[:3]] == [0, 1, 2]
    assert sel[199]["meta"]["candidate_rank"] == 199     # FS quota filled
    assert sel[200]["meta"]["candidate_rank"] == 300     # walk reached FR
    assert sel[599]["meta"]["candidate_rank"] == 699     # last SC candidate
    assert st["fever/SUPPORTS"]["examined"] == 200      # stops at quota


def _write_rows(path, recs):
    with open(path, "w") as fh:
        for r in recs:
            fh.write(json.dumps(r) + "\n")
    return str(path)


def test_load_rows_guards(tmp_path):
    ok = [{"item_id": "a", "kind_name": k, "value": 50.0,
           "model_tag": "mistral-small-24b"}
          for k in ("base", "admit_pre", "admit_post")]
    p = _write_rows(tmp_path / "ok.jsonl", ok)
    assert set(sg.load_rows([p])["a"]) == {"base", "admit_pre", "admit_post"}
    # §9.2: any Exclude kind or probe in selection rows aborts
    bad = [{"item_id": "a", "kind_name": "exclude_pre", "value": 50.0,
            "model_tag": "mistral-small-24b"}]
    with pytest.raises(SystemExit, match="Exclude"):
        sg.load_rows([_write_rows(tmp_path / "bad.jsonl", bad)])
    probe = [{"item_id": "a", "kind_name": "rule_probe_exclude_post",
              "p_yes": 0.1, "model_tag": "mistral-small-24b"}]
    with pytest.raises(SystemExit, match="Exclude"):
        sg.load_rows([_write_rows(tmp_path / "probe.jsonl", probe)])
    # frozen selection model only
    wrong = [dict(ok[0], model_tag="gemma3-12b")]
    with pytest.raises(SystemExit, match="frozen"):
        sg.load_rows([_write_rows(tmp_path / "wrong.jsonl", wrong)])
    with pytest.raises(SystemExit, match="frozen"):
        sg.load_rows([p], expect_tag="not-mistral")
    two = [ok[0], dict(ok[0], model_tag="gemma3-12b")]
    with pytest.raises(SystemExit, match="one model"):
        sg.load_rows([_write_rows(tmp_path / "two.jsonl", two)])


# ---------------------------------------------------------------------------
# analyzer: frozen inference + §8 decision order + §7 gate
# ---------------------------------------------------------------------------
def test_analyzer_constants_frozen():
    assert ag.SEED == 20260924 and ag.B == 10000
    assert ag.DESIGN_TAG == "g24a-natural-evidence-confirmation-design-v1"
    assert ag.SELECTOR_TAG == "mistral-small-24b"
    assert ag.NON_SELECTOR == ["llama31-8b", "qwen3-8b", "qwen35-9b",
                               "gemma3-12b"]
    assert ag.ALL_MODELS == MODEL_TAGS
    assert ag.SUFFICIENCY_MIN == 300
    assert set(ag.VERDICTS) == set(ag.LICENSED)
    assert ag.METRICS == ("REI_pre", "REI_post", "delta_time", "UTB_norm")


def test_cluster_boot_deterministic_point_and_ci():
    pairs = [(f"c{i % 5}", {m: (i % 7) / 7.0 for m in ag.METRICS})
             for i in range(40)]
    r1 = ag.cluster_boot(pairs, n=200)
    r2 = ag.cluster_boot(pairs, n=200)
    assert r1 == r2
    import statistics as st
    for m in ag.METRICS:
        mu, lo, hi, p = r1[m]
        assert abs(mu - st.mean([v[m] for _, v in pairs])) < 1e-12
        assert lo <= mu <= hi and 0.0 <= p <= 1.0
    assert all(math_isnan(v) for v in ag.cluster_boot([])["REI_pre"])


def math_isnan(x):
    import math
    return math.isnan(x)


def test_cluster_integrity_resamples_whole_clusters():
    """A replicate must be a whole-cluster draw: with A = {1,1}, B = {0} only
    cluster-size-weighted means {1, 2/3, 0} are reachable — row-level
    resampling would also produce 1/3."""
    pairs = [("A", {m: 1.0 for m in ag.METRICS}),
             ("A", {m: 1.0 for m in ag.METRICS}),
             ("B", {m: 0.0 for m in ag.METRICS})]
    point, reps = ag._cluster_boot_reps(pairs, n=400, seed=ag.SEED)
    allowed = [1.0, 2.0 / 3.0, 0.0]
    assert all(any(abs(x - a) < 1e-9 for a in allowed) for x in reps["REI_pre"])
    assert not any(abs(x - 1.0 / 3.0) < 1e-9 for x in reps["REI_pre"])
    assert abs(point["REI_pre"] - 2.0 / 3.0) < 1e-12


def _mkitem(iid, direction, source="fever", cluster="p0", gold="SUPPORTS"):
    d = dict(item_id=iid, task_family=f"g24a_{source}",
             surface_domain="wikipedia", base_context=f"claim {iid}",
             critical_evidence=f"evidence {iid}", critical_label="evidence E",
             critical_direction=direction, exclusion_reason="none_stated",
             evidence_truth="true_but_forbidden", admit_rule=g24a.ADMIT_RULE,
             exclude_rule=g24a.EXCLUDE_RULE, question=g24a.QUESTION,
             output_spec=g24a.OUTPUT_SPEC, memory_question="",
             rule_probe_question=g24a.RULE_PROBE_QUESTION, ground_truth=None,
             meta={"source": source, "gold_label": gold, "cluster": cluster,
                   "stratum": f"{source}/{gold}"})
    return Item(**d)


def _runs(item_id, y, probes=True):
    r = {k: {"value": v} for k, v in y.items()}
    if probes:
        r["rule_probe_exclude_pre"] = {"p_yes": 0.1}
        r["rule_probe_exclude_post"] = {"p_yes": 0.2}
        r["rule_probe_admit_post"] = {"p_yes": 0.8}
    return {item_id: r}


def test_build_table_estimands_both_directions_inherited_from_g0():
    from analyze import build_table
    inc = _mkitem("up", "increase")
    rows = build_table([inc], _runs("up", dict(
        base=50, admit_pre=70, admit_post=70, exclude_pre=60,
        exclude_post=55)))
    r = rows[0]
    assert r["usable"] and r["L"] == 20 and r["signed_L"] == 20
    assert r["REI_pre"] == 0.5 and r["REI_post"] == 0.25
    assert r["delta_time"] == -0.25 and r["REI_admit"] == 1.0
    assert r["UTB_norm"] == -0.25
    assert r["p_use_pre"] == 0.1 and r["p_use_admit"] == 0.8

    dn = _mkitem("dn", "decrease")
    rows = build_table([dn], _runs("dn", dict(
        base=50, admit_pre=30, admit_post=30, exclude_pre=45,
        exclude_post=48)))
    r = rows[0]
    assert r["usable"] and r["L"] == -20 and r["signed_L"] == 20
    assert abs(r["REI_pre"] - 0.25) < 1e-12
    assert abs(r["REI_post"] - 0.10) < 1e-12
    assert abs(r["UTB_norm"] - (-0.15)) < 1e-12

    # sL <= 0 -> unusable, no REI keys
    rows = build_table([inc], _runs("up", dict(
        base=50, admit_pre=45, admit_post=45, exclude_pre=60,
        exclude_post=55)))
    assert rows and not rows[0]["usable"] and "REI_pre" not in rows[0]

    # any missing condition -> row dropped entirely
    y = dict(base=50, admit_pre=70, admit_post=70, exclude_pre=60)
    assert build_table([inc], _runs("up", y)) == []


def test_attach_cluster_keys_and_summarise_empty():
    it = _mkitem("x", "increase", source="scifact", cluster="8551160",
                 gold="CONTRADICT")
    from analyze import build_table
    rows = build_table([it], _runs("x", dict(
        base=50, admit_pre=70, admit_post=70, exclude_pre=60,
        exclude_post=55)))
    ag.attach(rows, {"x": it}, "qwen3-8b")
    assert rows[0]["_cluster"] == "scifact/8551160"
    assert rows[0]["model_tag"] == "qwen3-8b"
    assert rows[0]["gold_label"] == "CONTRADICT"
    assert ag.summarize([], "empty") is None


def test_load_runs_guards(tmp_path):
    rec = {"item_id": "a", "kind_name": "base", "value": 50.0,
           "model_tag": "qwen3-8b"}
    p = _write_rows(tmp_path / "mistral.jsonl",
                    [dict(rec, model_tag="mistral-small-24b")])
    with pytest.raises(SystemExit, match="frozen G24A panel"):
        ag.load_runs([_write_rows(tmp_path / "evil.jsonl",
                                  [dict(rec, model_tag="evil-model")])])
    files = [_write_rows(tmp_path / f"{t}.jsonl", [dict(rec, model_tag=t)])
             for t in ["llama31-8b", "qwen3-8b", "qwen35-9b", "gemma3-12b"]]
    with pytest.raises(SystemExit, match="missing model outputs"):
        ag.load_runs(files)                      # selection model absent
    runs = ag.load_runs(files + [p])
    assert set(runs) == set(MODEL_TAGS)


def test_classify_decision_order_and_gate_precedence():
    # §8 decision order, strictly literal
    assert ag.classify(True, True, True, True, True) == "natural-evidence-leak"
    assert ag.classify(True, True, True, False, True) == \
        "natural-evidence-leak-inconsistent"
    assert ag.classify(True, True, True, True, False) == \
        "natural-evidence-leak-inconsistent"
    assert ag.classify(True, True, False, True, True) == "prospective-only"
    assert ag.classify(True, False, True, True, True) == "retrospective-only"
    assert ag.classify(True, False, False, True, True) == "not-confirmed"
    # §7 gate: unresolved regardless of endpoint values
    assert ag.classify(False, True, True, True, True) == "unresolved"


def test_pass_requires_strictly_positive_ci_lower():
    assert ag._pass(None) is False and ag._pass_post(None) is False
    assert ag._pass({"REI_pre": (0.5, 0.0, 0.9, 0.2)}) is False   # strict >0
    assert ag._pass({"REI_pre": (0.5, 0.01, 0.9, 0.0)}) is True
    assert ag._pass({"REI_pre": (float("nan"),) * 4}) is False
    assert ag._pass_post({"REI_post": (0.4, -0.1, 0.9, 0.4)}) is False
    assert ag._pass_post({"REI_post": (0.4, 0.05, 0.9, 0.0)}) is True


# ---------------------------------------------------------------------------
# end-to-end (synthetic panel, no model)
# ---------------------------------------------------------------------------
def _synth_items(n_fever=200, n_sci=150):
    items = []
    for i in range(n_fever):
        gold = "SUPPORTS" if i % 2 == 0 else "REFUTES"
        items.append(_itodict(_mkitem(
            f"g24a_fever_t{i}",
            "increase" if gold == "SUPPORTS" else "decrease",
            source="fever", cluster=f"fever_p{i // 2}", gold=gold)))
    for i in range(n_sci):
        gold = "SUPPORT" if i % 2 == 0 else "CONTRADICT"
        items.append(_itodict(_mkitem(
            f"g24a_scifact_t{i}",
            "increase" if gold == "SUPPORT" else "decrease",
            source="scifact", cluster=f"sci_d{i // 2}", gold=gold)))
    return items


def _itodict(it):
    from dataclasses import asdict
    return asdict(it)


def _synth_rows(d, midx, leak=True):
    """Deterministic synthetic decision/probe rows for one item × one model."""
    i = int(d["item_id"].rsplit("_t", 1)[1])
    s = 1.0 if d["critical_direction"] == "increase" else -1.0
    base = 40.0 + (i % 17)
    la = 20.0 + 0.4 * midx                      # signed leverage, all > τ
    vals = {
        "base": base,
        "admit_pre": base + s * (la + 0.3),
        "admit_post": base + s * (la - 0.3),
    }
    if leak:
        vals["exclude_pre"] = base + s * la * 0.5
        vals["exclude_post"] = base + s * la * 0.4
    else:
        sh = 1.0 if i % 2 == 0 else -1.0        # alternates inside each cluster
        vals["exclude_pre"] = base + s * la * 0.5 * sh
        vals["exclude_post"] = base + s * la * 0.4 * sh
    rows = [dict(item_id=d["item_id"], kind_name=k, value=v,
                 model_tag=MODEL_TAGS[midx]) for k, v in vals.items()]
    for pk, v in (("rule_probe_exclude_pre", 0.1),
                  ("rule_probe_exclude_post", 0.1),
                  ("rule_probe_admit_post", 0.9)):
        rows.append(dict(item_id=d["item_id"], kind_name=pk, p_yes=v,
                         model_tag=MODEL_TAGS[midx]))
    return rows


def _e2e(tmp_path, leak):
    items = _synth_items()
    items_path = tmp_path / "items.jsonl"
    with open(items_path, "w") as fh:
        for d in items:
            fh.write(json.dumps(d) + "\n")
    run_files = []
    for midx, tag in enumerate(MODEL_TAGS):
        recs = [r for d in items for r in _synth_rows(d, midx, leak=leak)]
        run_files.append(_write_rows(tmp_path / f"{tag}.jsonl", recs))
    import analyze_g24a
    old_b = analyze_g24a.B
    analyze_g24a.B = 300                       # fast tests; engine unchanged
    old_argv = sys.argv
    try:
        sys.argv = ["analyze_g24a.py", "--runs", *run_files,
                    "--items", str(items_path), "--tag", "synth",
                    "--out-prefix", str(tmp_path / "out")]
        rc = ag.main()
    finally:
        sys.argv = old_argv
        analyze_g24a.B = old_b
    assert rc == 0
    md = open(tmp_path / "out.md").read()
    res = json.load(open(tmp_path / "out.json"))
    return items, md, res


def test_e2e_confirmatory_path_natural_evidence_leak(tmp_path):
    items, md, res = _e2e(tmp_path, leak=True)
    assert res["verdict"] == "natural-evidence-leak"
    ep = res["endpoints"]
    assert ep["P1"] and ep["P2"] and ep["C1"] and ep["C2"] and ep["sufficiency"]
    assert len(ep["C1_models"]) == 5
    assert ep["sources"] == {"fever": True, "scifact": True}
    p4 = res["strata"]["pooled-4 (primary)"]
    assert p4["n"] == 350 * 4 and p4["n_rows"] == 350 * 4
    assert p4["n_items"] == 350 and p4["n_clusters"] == 175     #100 + 75
    assert p4["REI_pre"][0] == pytest.approx(0.5)
    assert p4["REI_post"][0] == pytest.approx(0.4)
    assert p4["REI_pre"][1] > 0 and p4["REI_post"][1] > 0        # CIs >0
    assert p4["rule_acc_pre"] == pytest.approx(0.9)
    assert p4["alignment_rate"] == 1.0
    assert 20.0 <= p4["median_absL"] <= 21.5
    assert p4["frac_post_gt_pre"] == 0.0
    assert res["usable_pooled4_items"] == 350
    for tag, led in res["ledger"].items():
        assert led == {"expected": 350, "complete": 350,
                       "partial": 0, "absent": 0}, tag
    assert res["selector_model"] == "mistral-small-24b"
    assert res["non_selector_models"] == ag.NON_SELECTOR
    assert res["licensed"] == ag.LICENSED["natural-evidence-leak"]
    assert "## Verdict" in md and "**natural-evidence-leak**" in md
    assert "INCOMPLETE" not in md
    assert f"{res['items_sha256']}" and res["runs_sha256"]
    # per-source blocks exist and are positive
    for src in ("fever", "scifact"):
        s = res["strata"][f"pooled-4 {src}"]
        assert s["REI_pre"][0] > 0 and s["REI_post"][0] > 0


def test_e2e_no_leak_not_confirmed(tmp_path):
    items, md, res = _e2e(tmp_path, leak=False)
    assert res["verdict"] == "not-confirmed"
    ep = res["endpoints"]
    assert not ep["P1"] and not ep["P2"]
    assert ep["sufficiency"]                 # gate passed; endpoints decide
    p4 = res["strata"]["pooled-4 (primary)"]
    # cluster means are0 up to float noise (+0.5/-0.5 pairs): CI hugs0
    assert p4["REI_pre"][1] <= 1e-9 and p4["REI_pre"][2] >= -1e-9
    assert p4["REI_post"][1] <= 1e-9 and p4["REI_post"][2] >= -1e-9
    assert abs(p4["REI_pre"][0]) < 1e-9
    assert res["usable_pooled4_items"] == 350
    assert "**not-confirmed**" in md


def test_e2e_sufficiency_gate_forces_unresolved(tmp_path):
    # same confirmatory data but a tiny selected set -> gate fails first
    items, md, res = _e2e_small(tmp_path)
    assert res["verdict"] == "unresolved"
    assert res["endpoints"]["sufficiency"] is False
    assert res["endpoints"]["P1"] is True      # endpoints pass; gate overrides
    assert res["licensed"] == ag.LICENSED["unresolved"]


def _e2e_small(tmp_path):
    items = _synth_items(n_fever=60, n_sci=40)
    items_path = tmp_path / "items_small.jsonl"
    with open(items_path, "w") as fh:
        for d in items:
            fh.write(json.dumps(d) + "\n")
    run_files = []
    for midx, tag in enumerate(MODEL_TAGS):
        recs = [r for d in items for r in _synth_rows(d, midx, leak=True)]
        run_files.append(_write_rows(tmp_path / f"small_{tag}.jsonl", recs))
    import analyze_g24a
    old_b = analyze_g24a.B
    analyze_g24a.B = 300
    old_argv = sys.argv
    try:
        sys.argv = ["analyze_g24a.py", "--runs", *run_files,
                    "--items", str(items_path), "--tag", "small",
                    "--out-prefix", str(tmp_path / "out_small")]
        rc = ag.main()
    finally:
        sys.argv = old_argv
        analyze_g24a.B = old_b
    assert rc == 0
    return items, open(tmp_path / "out_small.md").read(), \
        json.load(open(tmp_path / "out_small.json"))


# ---------------------------------------------------------------------------
# prereg wording lock
# ---------------------------------------------------------------------------
def _norm(t):
    t = t.replace(">", " ").replace("*", " ").replace("`", " ")
    return re.sub(r"\s+", " ", t).strip()


def test_prereg_wording_lock():
    raw = open(PREREG).read()
    norm = _norm(raw)
    for v in ag.VERDICTS:
        assert v in raw, f"verdict {v} missing from prereg"
        assert _norm(ag.LICENSED[v]) in norm, f"licensed claim {v} drifted"
    for token in (ag.DESIGN_TAG, "20260924", "mistral-small-24b",
                  "τ = 10.0", "300 of 600", "13,283", "12,648", "635",
                  "**600**", "first-eligible", "g24a_candidates_v1.jsonl",
                  "g24a_v1.jsonl"):
        assert token in raw, f"prereg drifted: {token!r} gone"
    assert "NO G24A TARGET-MODEL COMPUTE IS AUTHORIZED BY THIS FILE" in raw
