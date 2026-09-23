"""G23B design tests — nothing here touches a model.

Runs on code and synthetic records only: materials promises (60 items / 60
skeletons / 30-30 / fresh / no gold), the seven frozen cells and their block
orders, the byte-identical rule across U/K/I, the §4 proffer carrier, the
analyzer's estimands / four carrier gates / six-verdict decision order, the
FLAG-1 behaviour (Phase-A gates run on the E1 set, not post-E2/E3), the phase
file wiring and the prereg semantic freeze.
"""
from __future__ import annotations

import hashlib
import json
import os
from collections import Counter

import pytest

from conditions_g23b import (G23B_CONDITIONS, PHASE_A, PHASE_B, PHASE_A_CELLS,
                             PHASE_B_CELLS, proffer)
from gen_g23b import build, check_fresh
from schema import compile_prompt, load_items, _blocks, PROBES
import analyze_g23b as ag

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ITEMS = load_items(os.path.join(ROOT, "data/items/g23b_v1.jsonl"))
BY_ID = {i.item_id: i for i in ITEMS}
SHA256 = "8cb4cfe4dacb0e5f4368c6d1e568083fd38f05b54ae03489d0208b4b7332cda8"

VERDICTS = {"carrier-invalid", "branch-not-replicated", "instantiation-dependent",
            "hybrid", "semantic-preactivation", "unresolved"}


# ---------------------------------------------------------------------------
# Materials
# ---------------------------------------------------------------------------
def test_shape_60_items_60_skeletons_legal_only():
    assert len(ITEMS) == 60
    assert Counter(i.task_family for i in ITEMS) == {"legal_judgment": 60}
    assert len({i.meta["skeleton"] for i in ITEMS}) == 60   # one item per skeleton
    assert len({i.critical_label for i in ITEMS}) == 60


def test_directions_balanced_30_30():
    assert Counter(i.critical_direction for i in ITEMS) == {"increase": 30,
                                                            "decrease": 30}


def test_exclusion_reason_groups_are_four_even_bands():
    counts = Counter(i.exclusion_reason for i in ITEMS)
    assert counts == {"procedural_illegality": 15, "epistemic_invalidation": 15,
                      "access_control": 15, "temporal_irrelevance": 15}


def test_domains_and_skeletons_are_fresh():
    check_fresh(ITEMS, ROOT)     # no id / surface / skeleton from G0, G18, G23A
    assert len({i.surface_domain for i in ITEMS}) == 60


def test_no_llm_gold_and_contexts_are_substantial():
    for i in ITEMS:
        assert i.ground_truth is None        # no LLM-as-judge anywhere
        assert i.evidence_truth == "true_but_forbidden"
        assert len(i.base_context) >= 120
        assert i.critical_evidence
        assert i.output_spec.startswith("Use a scale from 0 to 9")


def test_frozen_artifact_matches_the_pinned_sha():
    with open(os.path.join(ROOT, "data/items/g23b_v1.jsonl"), "rb") as handle:
        assert hashlib.sha256(handle.read()).hexdigest() == SHA256


def test_file_matches_the_generator():
    with open(os.path.join(ROOT, "data/items/g23b_v1.jsonl")) as handle:
        lines = [l for l in handle.read().splitlines() if l]
    assert lines == [i.to_json() for i in build()]


# ---------------------------------------------------------------------------
# Conditions — the seven frozen cells
# ---------------------------------------------------------------------------
def test_condition_set_is_the_seven_preregistered_cells():
    assert set(G23B_CONDITIONS) == {"g23b_b", "g23b_p", "g23b_e", "g23b_pe",
                                    "g23b_u", "g23b_k", "g23b_i"}
    assert PHASE_A_CELLS == ("b", "p", "e", "pe")
    assert PHASE_B_CELLS == ("u", "k", "i")
    assert PHASE_A == ["g23b_b", "g23b_p", "g23b_e", "g23b_pe"]
    assert PHASE_B == ["g23b_u", "g23b_k", "g23b_i"]
    assert not (set(G23B_CONDITIONS) & set(PROBES))   # G23B runs no probes


def _kinds(item, cond):
    return ["B" if b.startswith("BACKGROUND")
            else "P" if b.startswith("OFFER OF PROOF")
            else "R" if b.startswith("RULING")
            else "E" for b in _blocks(item, cond)]


def test_block_orders_are_exactly_prereg_section_5():
    expected = {
        "g23b_b": ["B"], "g23b_p": ["B", "P"], "g23b_e": ["B", "E"],
        "g23b_pe": ["B", "P", "E"], "g23b_u": ["B", "R", "E"],
        "g23b_k": ["B", "P", "R", "E"], "g23b_i": ["B", "E", "R"],
    }
    for i in ITEMS:
        for cond, want in expected.items():
            assert _kinds(i, cond) == want, (i.item_id, cond)


def test_phase_a_contains_no_rule_anywhere():
    for i in ITEMS:
        for cond in PHASE_A:
            prompt = compile_prompt(i, cond, mode="reasoned")
            assert "RULING" not in prompt
            assert "must not let it play any role" not in prompt


def test_rule_is_byte_identical_across_u_k_i():
    for i in ITEMS:
        rules = {b for cond in PHASE_B for b in _blocks(i, cond)
                 if b.startswith("RULING")}
        assert rules == {"RULING\n" + i.exclude_rule}, i.item_id


def test_k_is_u_with_the_proffer_inserted():
    for i in ITEMS:
        u, k = _blocks(i, "g23b_u"), _blocks(i, "g23b_k")
        assert k[0] == u[0] and k[1] == proffer(i) and k[2:] == u[1:]


def test_proffer_carrier_is_frozen_and_carries_the_payload_verbatim():
    for i in ITEMS:
        p = proffer(i)
        assert p.startswith("OFFER OF PROOF — NOT EVIDENCE\n\n")
        assert "For the limited purpose of deciding admissibility," in p
        assert i.critical_label in p
        assert i.critical_evidence in p                 # same proposition as E
        assert p.count(i.critical_evidence) == 1
        assert f"    {i.critical_evidence}" in p        # indented payload
        assert p.rstrip().endswith("must not affect the merits judgment.")
        # §4 forbids changing the proposition's status inside the carrier:
        wrapper = p.replace(i.critical_evidence, "").lower()
        for word in ("ignore", "hypothetical", "uncertain", "unreliable",
                     "false", "inadmissible", "must not let it play any role"):
            assert word not in wrapper, (i.item_id, word)
        assert "RULING" not in p                        # never a second rule


def test_every_item_compiles_every_condition():
    for i in ITEMS:
        for cond in G23B_CONDITIONS:
            prompt = compile_prompt(i, cond, mode="reasoned")
            assert "ANSWER:" in prompt and i.question in prompt


# ---------------------------------------------------------------------------
# Analyzer — rows, exclusions, estimands
# ---------------------------------------------------------------------------
def _write(path, rows):
    with open(path, "w") as handle:
        for r in rows:
            handle.write(json.dumps(r) + "\n")


def _cells(item_id, **over):
    vals = {"g23b_b": 50.0, "g23b_p": 50.0, "g23b_e": 70.0, "g23b_pe": 70.0,
            "g23b_u": 60.0, "g23b_k": 60.0, "g23b_i": 50.0}
    vals.update(over)
    return [{"item_id": item_id, "kind_name": k, "value": v}
            for k, v in vals.items()]


def test_phase_a_rows_keep_nonpositive_leverage_items_flagged(tmp_path):
    # FLAG 1: gates 3/4 run on the E1 set, so an item with Leverage_K <= 0 must
    # still be returned by rows_phase_a (flagged), not silently dropped.
    item_id = ITEMS[0].item_id
    path = str(tmp_path / "a.jsonl")
    _write(path, _cells(item_id, g23b_pe=40.0))     # lev_k = 40 - 50 = -10
    rows, drops = ag.rows_phase_a({item_id: BY_ID[item_id]}, {"m": path})
    assert len(rows) == 1
    assert rows[0]["e3_drop"] is True
    assert drops["m:would_drop_nonpositive_leverage_k"] == 1
    assert drops["m:would_drop_nonpositive_leverage_u"] == 0


def test_phase_a_drops_incomplete_and_unknown(tmp_path):
    item_id = ITEMS[0].item_id
    path = str(tmp_path / "a.jsonl")
    rows_in = [r for r in _cells(item_id) if r["kind_name"] != "g23b_pe"]
    rows_in.append({"item_id": "nope", "kind_name": "g23b_b", "value": 1.0})
    _write(path, rows_in)
    rows, drops = ag.rows_phase_a({item_id: BY_ID[item_id]}, {"m": path})
    assert rows == []
    assert drops["m:incomplete"] == 1
    assert drops["m:unknown_item"] == 1


def test_phase_b_applies_e1_e2_e3(tmp_path):
    a, b = str(tmp_path / "a.jsonl"), str(tmp_path / "b.jsonl")
    inc = ITEMS[0].item_id                                # direction +1
    # complete, leverage positive in both -> kept
    _write(a, _cells(inc))
    _write(b, [{"item_id": inc, "kind_name": k, "value": v} for k, v in
               (("g23b_u", 60.0), ("g23b_k", 60.0), ("g23b_i", 50.0))])
    rows, drops = ag.rows_phase_b(BY_ID, {"m": a}, {"m": b})
    assert len(rows) == 1 and drops == {}

    # E3: Leverage_K <= 0 -> excluded from the branch set
    _write(a, _cells(inc, g23b_b=50.0, g23b_p=50.0, g23b_e=70.0, g23b_pe=45.0))
    rows, drops = ag.rows_phase_b(BY_ID, {"m": a}, {"m": b})
    assert rows == []
    assert drops["m:nonpositive_leverage_k"] == 1

    # E2: Leverage_U <= 0 -> excluded first
    _write(a, _cells(inc, g23b_b=50.0, g23b_p=50.0, g23b_e=48.0, g23b_pe=70.0))
    rows, drops = ag.rows_phase_b(BY_ID, {"m": a}, {"m": b})
    assert rows == []
    assert drops["m:nonpositive_leverage_u"] == 1


def _pair(v, cluster="c"):
    return ag.summarise([(cluster, v)])


def test_estimands_match_preregistered_formulas(tmp_path):
    a, b = str(tmp_path / "a.jsonl"), str(tmp_path / "b.jsonl")
    inc = ITEMS[0].item_id                                # s = +1
    dec = next(i.item_id for i in ITEMS
               if i.critical_direction == "decrease")     # s = -1
    _write(a, _cells(inc, g23b_b=50.0, g23b_p=50.0, g23b_e=70.0, g23b_pe=70.0) +
           _cells(dec, g23b_b=50.0, g23b_p=50.0, g23b_e=30.0, g23b_pe=30.0))
    _write(b, _cells(inc, g23b_u=60.0, g23b_k=60.0, g23b_i=50.0,
                     g23b_b=50.0, g23b_p=50.0, g23b_e=70.0, g23b_pe=70.0) +
           _cells(dec, g23b_u=40.0, g23b_k=40.0, g23b_i=50.0,
                  g23b_b=50.0, g23b_p=50.0, g23b_e=30.0, g23b_pe=30.0))
    rows, drops = ag.rows_phase_b(BY_ID, {"m": a}, {"m": b})
    assert len(rows) == 2 and drops == {}
    for r in rows:
        assert r["supp_u"] == pytest.approx(10.0)
        assert r["supp_k"] == pytest.approx(10.0)
        assert r["supp_i"] == pytest.approx(20.0)
        assert r["sem_rescue"] == pytest.approx(0.0)
        assert r["inst_prem"] == pytest.approx(10.0)
        assert r["retro_adv"] == pytest.approx(10.0)
        # identity of prereg §7: RetroAdv = SemRescue + InstPremium, exactly
        assert r["retro_adv"] == pytest.approx(r["sem_rescue"] + r["inst_prem"])


def test_phase_a_estimands_match_preregistered_formulas(tmp_path):
    item_id = ITEMS[0].item_id                            # s = +1
    path = str(tmp_path / "a.jsonl")
    _write(path, _cells(item_id, g23b_b=50.0, g23b_p=53.0,
                        g23b_e=70.0, g23b_pe=73.0))
    rows, _ = ag.rows_phase_a({item_id: BY_ID[item_id]}, {"m": path})
    r = rows[0]
    assert r["proffer_leak"] == pytest.approx(3.0)        # s*(P - B)
    assert r["leverage_u"] == pytest.approx(20.0)         # s*(E - B)
    assert r["leverage_k"] == pytest.approx(20.0)         # s*(PE - P)


# ---------------------------------------------------------------------------
# Analyzer — gates and verdict
# ---------------------------------------------------------------------------
def _s(mean, lo, hi, n=60):
    return {"n": n, "n_clusters": n, "mean": mean, "ci_low": lo, "ci_high": hi}


def _models(proffer=0.0, lev_k=20.0):
    return {t: {"proffer_leak": _s(proffer, proffer - 1, proffer + 1),
                "leverage_k": _s(lev_k, lev_k - 1, lev_k + 1)}
            for t in ag.MODELS}


def test_constants_are_frozen():
    assert ag.FLOOR == 3.0
    assert ag.MIN_MODELS_POSITIVE == 2
    assert ag.SEED == 20260923
    assert ag.N_RESAMPLES == 10_000
    assert ag.DESIGN_TAG == "g23b-gate-vs-cancellation-design-v1"


def test_carrier_gate_all_four_on_the_e1_set():
    pooled = {"proffer_leak": _s(0.0, -1.0, 1.0), "leverage_k": _s(20.0, 18.0, 22.0)}
    g = ag.carrier_gate(pooled, _models())
    assert g["passed"] is True
    assert all(v for k, v in g.items() if k.startswith("gate"))


def test_carrier_gate_each_gate_can_fail():
    pooled_ok = {"proffer_leak": _s(0.0, -1.0, 1.0), "leverage_k": _s(20.0, 18.0, 22.0)}
    # gate 1: pooled ProfferLeak CI upper bound reaches the floor
    g = ag.carrier_gate({**pooled_ok, "proffer_leak": _s(2.0, 0.0, 4.0)}, _models())
    assert g["gate1_pooled_profferleak_ci_high_lt_floor"] is False
    assert g["passed"] is False
    # gate 2: one model's mean ProfferLeak is at the floor
    mods = _models()
    mods[ag.MODELS[0]]["proffer_leak"] = _s(3.0, 2.0, 4.0)
    g = ag.carrier_gate(pooled_ok, mods)
    assert g["gate2_no_model_mean_profferleak_ge_floor"] is False
    # gate 3: pooled mean Leverage_K is not positive
    g = ag.carrier_gate({**pooled_ok, "leverage_k": _s(-1.0, -3.0, 0.0)}, _models())
    assert g["gate3_pooled_mean_leverage_k_gt_0"] is False
    # gate 4: only one model positive on Leverage_K
    mods = _models()
    mods[ag.MODELS[1]]["leverage_k"] = _s(-2.0, -4.0, 0.0)
    mods[ag.MODELS[2]]["leverage_k"] = _s(-2.0, -4.0, 0.0)
    g = ag.carrier_gate(pooled_ok, mods)
    assert g["gate4_leverage_k_positive_in_2_of_3_models"] is False


def test_pass_gate_and_within_floor_semantics():
    assert ag.pass_gate(_s(3.0, 0.1, 5.0), [4.0, 4.0, 4.0]) is True
    assert ag.pass_gate(_s(2.9, 0.1, 5.0), [4.0, 4.0, 4.0]) is False   # floor
    assert ag.pass_gate(_s(5.0, 0.0, 8.0), [4.0, 4.0, 4.0]) is False   # ci_low
    assert ag.pass_gate(_s(5.0, 1.0, 8.0), [4.0, -1.0, -1.0]) is False  # 2/3
    assert ag.within_floor(_s(0.0, -2.0, 2.9)) is True
    assert ag.within_floor(_s(0.0, -2.0, 3.0)) is False


def _branch_pooled(ra, sr, ip):
    return {"retro_adv": _s(*ra), "sem_rescue": _s(*sr), "inst_prem": _s(*ip)}


def _branch_models(ra, sr, ip):
    return {t: {"retro_adv": _s(*ra[:3]), "sem_rescue": _s(*sr[:3]),
                "inst_prem": _s(*ip[:3])} for t in ag.MODELS}


def test_verdict_rule_is_exhaustive_and_frozen():
    # carrier gate fails first — before any branch statistic
    assert ag.classify(False, _branch_pooled((10, 8, 12), (6, 4, 8), (6, 4, 8)),
                       _branch_models((10, 8, 12), (6, 4, 8), (6, 4, 8))) == \
        "carrier-invalid"
    # retrospective sanity fails -> branch not promoted
    assert ag.classify(True, _branch_pooled((1, -2, 4), (6, 4, 8), (6, 4, 8)),
                       _branch_models((1, -2, 4), (6, 4, 8), (6, 4, 8))) == \
        "branch-not-replicated"
    # Supp_I > Supp_K (meaningful), Supp_K ~ Supp_U (within floor)
    assert ag.classify(True, _branch_pooled((10, 8, 12), (0, -1, 1), (10, 8, 12)),
                       _branch_models((10, 8, 12), (0, -1, 1), (10, 8, 12))) == \
        "instantiation-dependent"
    # both contrasts meaningful
    assert ag.classify(True, _branch_pooled((12, 10, 14), (6, 4, 8), (6, 4, 8)),
                       _branch_models((12, 10, 14), (6, 4, 8), (6, 4, 8))) == \
        "hybrid"
    # semantic rescue meaningful, premium within floor
    assert ag.classify(True, _branch_pooled((6, 4, 8), (6, 4, 8), (0, -1, 1)),
                       _branch_models((6, 4, 8), (6, 4, 8), (0, -1, 1))) == \
        "semantic-preactivation"
    # both within floor / sub-threshold -> no forced verdict
    assert ag.classify(True, _branch_pooled((6, 4, 8), (1, -2, 2.9),
                                            (1, -2, 2.9)),
                       _branch_models((6, 4, 8), (1, -2, 2.9), (1, -2, 2.9))) == \
        "unresolved"


def test_bootstrap_is_deterministic_and_clustered():
    pairs = [("c1", 1.0), ("c1", 5.0), ("c2", 3.0)]
    a = ag.summarise(pairs)
    b = ag.summarise(pairs)
    assert a == b                                    # same seed -> same interval
    assert a["n"] == 3 and a["n_clusters"] == 2
    assert a["ci_low"] <= a["mean"] <= a["ci_high"]


# ---------------------------------------------------------------------------
# Analyzer — end to end on synthetic phase files
# ---------------------------------------------------------------------------
def _phase_paths(tmp_path, monkeypatch):
    paths_a, paths_b = {}, {}
    for t in ag.MODELS:
        paths_a[t] = str(tmp_path / f"{t}_g23b_phasea.jsonl")
        paths_b[t] = str(tmp_path / f"{t}_g23b_phaseb.jsonl")
    monkeypatch.setattr(ag, "phase_a_path", lambda tag: paths_a[tag])
    monkeypatch.setattr(ag, "phase_b_path", lambda tag: paths_b[tag])
    return paths_a, paths_b


def _golden_vals(item, leak_item=None):
    """Values whose contrasts give SR=0, IP=10, RA=10, gates all pass."""
    inc = item.critical_direction == "increase"
    ye = 70.0 if inc else 30.0
    # full suppression pulls the judgment back to the background (50) for both
    # directions; partial (U/K) recovers half of the evidence's move.
    vals = {"g23b_b": 50.0, "g23b_p": 50.0, "g23b_e": ye, "g23b_pe": ye,
            "g23b_u": 60.0 if inc else 40.0,
            "g23b_k": 60.0 if inc else 40.0,
            "g23b_i": 50.0}
    if leak_item and item.item_id == leak_item:
        vals["g23b_p"] = 80.0            # proffer alone moves the judgment
    return vals


def _fill(paths_a, paths_b, sample, leak_item=None):
    for t in ag.MODELS:
        a_rows, b_rows = [], []
        for it in sample:
            vals = _golden_vals(it, leak_item)
            for k in ("g23b_b", "g23b_p", "g23b_e", "g23b_pe"):
                a_rows.append({"item_id": it.item_id, "kind_name": k,
                               "value": vals[k]})
            for k in ("g23b_u", "g23b_k", "g23b_i"):
                b_rows.append({"item_id": it.item_id, "kind_name": k,
                               "value": vals[k]})
        if t in paths_a:
            _write(paths_a[t], a_rows)
        if t in paths_b:
            _write(paths_b[t], b_rows)


def test_end_to_end_phase_a_gate_passes(tmp_path, monkeypatch, capsys):
    paths_a, _ = _phase_paths(tmp_path, monkeypatch)
    _fill(paths_a, {}, ITEMS[:6])
    report = ag._base_report("a")
    ag.phase_a(BY_ID, report)
    assert report["carrier_gates"]["passed"] is True
    assert report["pooled"]["proffer_leak"]["mean"] == pytest.approx(0.0)
    assert report["pooled"]["leverage_k"]["mean"] == pytest.approx(20.0)
    assert report["models_missing"] == []


def test_end_to_end_leaky_proffer_fails_the_carrier_gate(tmp_path, monkeypatch):
    paths_a, paths_b = _phase_paths(tmp_path, monkeypatch)
    _fill(paths_a, paths_b, ITEMS[:6], leak_item=ITEMS[0].item_id)
    report = ag._base_report("b")
    ag.phase_b(BY_ID, report)
    assert report["carrier_gates"]["passed"] is False
    assert report["verdict"] == "carrier-invalid"


def test_end_to_end_branch_verdict_instantiation_dependent(tmp_path, monkeypatch):
    paths_a, paths_b = _phase_paths(tmp_path, monkeypatch)
    _fill(paths_a, paths_b, ITEMS[:6])
    report = ag._base_report("b")
    ag.phase_b(BY_ID, report)
    assert report["carrier_gates"]["passed"] is True
    assert report["pooled"]["sem_rescue"]["mean"] == pytest.approx(0.0)
    assert report["pooled"]["inst_prem"]["mean"] == pytest.approx(10.0)
    assert report["branch_checks"]["pass_retrospective_advantage"] is True
    assert report["branch_checks"]["pass_instantiation_premium"] is True
    assert report["branch_checks"]["within_floor_semantic_rescue"] is True
    assert report["verdict"] == "instantiation-dependent"
    assert report["drops"] == {t: {} for t in ag.MODELS}


def test_phase_file_naming():
    assert ag.phase_a_path("qwen3-8b").endswith(
        "results/raw/qwen3-8b_g23b_phasea.jsonl")
    assert ag.phase_b_path("qwen3-8b").endswith(
        "results/raw/qwen3-8b_g23b_phaseb.jsonl")


# ---------------------------------------------------------------------------
# Semantic freeze + wiring
# ---------------------------------------------------------------------------
def test_semantic_freeze_matches_the_preregistration():
    with open(os.path.join(ROOT,
                           "preregistrations/PREREGISTRATION_G23B_"
                           "GATE_VS_CANCELLATION.md")) as handle:
        prereg = handle.read()
    for name in VERDICTS:
        assert name in prereg
        assert name in ag.LICENSED
    assert set(ag.LICENSED) == VERDICTS
    for term in ("ProfferLeak", "Leverage_K", "Supp_U", "Supp_K", "Supp_I",
                 "SemanticRescue", "InstantiationPremium",
                 "RetrospectiveAdvantage"):
        assert term in prereg
    # the FLAG-1 gate-order decision stays visible in the frozen analyzer
    with open(os.path.join(ROOT, "src/analyze_g23b.py")) as handle:
        source = handle.read()
    assert "FLAG-1" in source
    assert "AUDIT FIX" in source


def test_prereg_pins_the_adopted_rule_and_proffer_wording():
    """The three settled audit flags must stay visible in the frozen prereg."""
    with open(os.path.join(ROOT,
                           "preregistrations/PREREGISTRATION_G23B_"
                           "GATE_VS_CANCELLATION.md")) as handle:
        prereg = handle.read()
    # FLAG-3: the adopted proffer wording, prereg <-> rendered proffer
    assert "states the content" in prereg
    assert ("expected from [evidence label] when that evidence is later "
            "presented:") in prereg
    for i in ITEMS:
        assert "content expected from" in proffer(i)
    # FLAG-2: the adopted categorical-exclusion frame, prereg <-> materials
    frame = "you must not let it play any role when you reach your verdict."
    assert frame in prereg
    for i in ITEMS:
        assert frame in i.exclude_rule
    # FLAG-1: gate ordering recorded in the prereg
    assert "Gate ordering (FLAG-1" in prereg
    assert "Gates 3/4 are never evaluated after E3" in prereg.replace("*", "")


def test_wiring_schema_and_run_model():
    import schema
    import run_model
    assert schema.G23B_CONDITIONS == G23B_CONDITIONS
    assert set(run_model.G23B_CONDITIONS) == set(G23B_CONDITIONS)
