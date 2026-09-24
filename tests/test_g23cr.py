"""G23C-R design tests — nothing here touches a model.

Loads only the stdlib-only frozen analyzer (`src/mech/analyze_g23cr.py`); the
runner is checked as source text.  Covers prereg §16's mandatory list — the
70-item G18 loader / skeleton clustering, the byte-for-byte preview reuse, the
§5 tokenizer-audit gate semantics, the exact 10-patch union table, sign
conventions, identity patch, fixed layers/site/models, both parent classifiers
without gate drift, the four overall verdicts end to end on synthetic records,
the Phase-1 stop rule, drop accounting, the frozen design guard, runner wiring,
and the prereg wording lock.

Honest state pin: the committed §5 audit FAILED its position gate (17/140
item/model pairs), so the design is NOT frozen — these tests pin that fact
(`test_audit_v1_record_stops_the_design`, `test_checklist_still_unchecked`)
and must only change together with a consciously re-frozen design version.
"""
from __future__ import annotations

import importlib.util
import json
import os
from collections import Counter

import pytest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
_spec = importlib.util.spec_from_file_location(
    "analyze_g23cr", os.path.join(ROOT, "src/mech/analyze_g23cr.py"))
ag = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ag)

PREREG_PATH = os.path.join(
    ROOT, "preregistrations/PREREGISTRATION_G23C_R_FRESH_REPLICATION.md")
RUNNER_PATH = os.path.join(ROOT, "src/mech/g23cr_fresh_replication.py")
ANALYZER_PATH = os.path.join(ROOT, "src/mech/analyze_g23cr.py")
AUDIT_PATH = os.path.join(ROOT, "results/mech/g23cr_audit_v1.json")
G18_PATH = os.path.join(ROOT, "data/items/g18_v1.jsonl")
LAYERS = (4, 14, 24)

# The exact §9.3 union: 8-cell G24B grid + the two G23C 0->100 directions.
EXPECTED_PATCHES = {
    "ME_to_ME", "MA_to_ME", "UE_to_ME", "UA_to_ME",
    "ME_to_UE", "MA_to_UE", "UE_to_UE", "UA_to_UE",
    "ME_to_MA", "UE_to_UA",
}


# ---------------------------------------------------------------------------
# Synthetic fixtures
# ---------------------------------------------------------------------------
def _meta(n=6):
    """n items, alternating sign, two skeleton clusters."""
    return {f"i{k}": {"cluster": f"c{k // 2 % 2}", "family": "legal_judgment",
                      "s": 1.0 if k % 2 == 0 else -1.0}
            for k in range(n)}


def _y(s, pe_m=20.0, pe_u=10.0):
    me = 50.0
    return {"ME": me, "MA": me + s * pe_m,
            "UE": 50.0, "UA": 50.0 + s * pe_u}


def _design(phase, n_items, n_layers=36):
    Ls = list(ag.frozen_layers(n_layers))
    return {"design_tag": ag.DESIGN_TAG, "model": "m", "tag": "t",
            "phase": phase, "n_layers": n_layers, "layers": Ls,
            "primary": ag.PRIMARY_LAYER, "controls": [ag.CONTROL_LAYERS[0],
                                                      Ls[2]],
            "sites": ["rule_end"], "n_items": n_items,
            "identity_tol": ag.IDENTITY_TOL,
            "families": list(ag.FAMILIES), "seed": ag.SEED,
            "patches": sorted(ag.SCIENTIFIC)}


def _t(pm_ME, pm_UE, pu_ME, pu_UE, sw_m0, sw_u0):
    """Per-layer target knobs (§9.1/§9.2 coupled construction).

    Couplings that cannot be set independently (same physical patch):
      sw_M_100to0 == pm_ME   (MA_to_ME serves both estimands)
      sw_U_100to0 == pu_UE   (UA_to_UE serves both estimands)
    Free knobs: sw_m0 (ME_to_MA), sw_u0 (UE_to_UA), pm_UE, pu_ME.
    """
    return {"pm_ME": pm_ME, "pm_UE": pm_UE, "pu_ME": pu_ME, "pu_UE": pu_UE,
            "sw_m0": sw_m0, "sw_u0": sw_u0}


def _targets(l14, ctrl=None):
    zero = {k: 0.0 for k in l14}
    c = ctrl if ctrl is not None else zero
    return {"4": c, "14": l14, "24": dict(c)}


# jointly-replicated: PT_M=10, TC=10, DPM=10, DTI=10, controls zero
GOLD = _targets(_t(pm_ME=10.0, pm_UE=10.0, pu_ME=0.0, pu_UE=0.0,
                   sw_m0=10.0, sw_u0=0.0))
# G23C only: PT_M=mean(0,10)=5, TC=5; DPM=0 -> G24B no-donor
G23C_ONLY = _targets(_t(pm_ME=0.0, pm_UE=0.0, pu_ME=0.0, pu_UE=0.0,
                        sw_m0=10.0, sw_u0=0.0))
# G24B only: DPM=10, DTI=10; PT_M=mean(10,-10)=0, TC=0 -> G23C readiness-only
G24B_ONLY = _targets(_t(pm_ME=10.0, pm_UE=10.0, pu_ME=0.0, pu_UE=0.0,
                        sw_m0=-10.0, sw_u0=0.0))
NONE14 = _targets(_t(0.0, 0.0, 0.0, 0.0, 0.0, 0.0))
# controls trap, G23C side: TC=10 also at L4/L24 (dti still weaker/arm-ok)
CTRL_TRAP_G23C = _targets(
    GOLD["14"],
    ctrl=_t(pm_ME=10.0, pm_UE=0.0, pu_ME=0.0, pu_UE=0.0,
            sw_m0=10.0, sw_u0=0.0))
# controls trap, G24B side: DTI=10 also at L4/L24 (TC absent there)
CTRL_TRAP_G24B = _targets(
    GOLD["14"],
    ctrl=_t(pm_ME=10.0, pm_UE=10.0, pu_ME=0.0, pu_UE=0.0,
            sw_m0=0.0, sw_u0=0.0))


def _patches_for(s, y, t):
    """The 10 union patches at one layer, constructed to hit knobs `t`."""
    g = {}
    for R in ("ME", "UE"):
        g[f"ME_to_{R}"] = y[R]
        g[f"MA_to_{R}"] = y[R] + t[f"pm_{R}"] * s
        g[f"UE_to_{R}"] = y[R]
        g[f"UA_to_{R}"] = y[R] + t[f"pu_{R}"] * s
    g["ME_to_MA"] = y["MA"] - s * t["sw_m0"]
    g["UE_to_UA"] = y["UA"] - s * t["sw_u0"]
    assert set(g) == EXPECTED_PATCHES, set(g) ^ EXPECTED_PATCHES
    return g


def _bridge_obj(meta, tag, pe_m=20.0, pe_u=10.0,
                pe_m_by_cluster=None, pe_m_by_model=None, pe_u_by_model=None):
    pm_by_model = pe_m_by_model or {}
    pu_by_model = pe_u_by_model or {}
    records = []
    for iid, m in meta.items():
        s = m["s"]
        pm = pm_by_model.get(tag, pe_m)
        pm = (pe_m_by_cluster or {}).get(m["cluster"], pm)
        pu = pu_by_model.get(tag, pe_u)
        records.append({"item_id": iid,
                        "direction": "increase" if s > 0 else "decrease",
                        "y": _y(s, pm, pu), "n_tok": {}})
    return {"design": _design("bridge", len(meta)), "records": records}


def _patch_obj(meta, targets=GOLD, ctrl_targets=None, pe_m=20.0, pe_u=10.0,
               identity_off=0.0, drop_identity_layer=None,
               drop_patch_layer=None):
    # targets always carries all three layers (see _targets); an explicit
    # ctrl_targets overrides only the two control layers.
    if ctrl_targets is not None:
        merged = {"4": ctrl_targets["4"], "14": targets["14"],
                  "24": ctrl_targets["24"]}
    else:
        merged = targets
    records = []
    for iid, m in meta.items():
        s = m["s"]
        y = _y(s, pe_m, pe_u)
        by_L = {str(L): _patches_for(s, y, merged[str(L)]) for L in LAYERS}
        if drop_patch_layer is not None:
            for name in by_L[str(drop_patch_layer)]:
                by_L[str(drop_patch_layer)][name] = None
        rec = {
            "item_id": iid, "direction": "increase" if s > 0 else "decrease",
            "y": y, "n_tok": {c: 0 for c in ag.CELLS},
            "patch": {n: {str(L): by_L[str(L)][n] for L in LAYERS}
                      for n in ag.SCIENTIFIC},
            "identity": {str(L): {c: y[c] + identity_off for c in ag.CELLS}
                         for L in LAYERS}}
        if drop_identity_layer is not None:
            rec["identity"].pop(str(drop_identity_layer))
        records.append(rec)
    return {"design": _design("patch", len(meta)), "records": records}


def _write(path, obj):
    with open(path, "w") as handle:
        json.dump(obj, handle)
    return path


def _bridge_paths(tmp_path, meta, **kw):
    paths = {}
    for t in ag.MODELS:
        kw_t = {k: v for k, v in kw.items() if not k.endswith("_by_model")}
        over = {k: {t: kw[k][t]}
                for k in kw if k.endswith("_by_model") and t in kw[k]}
        paths[t] = _write(str(tmp_path / f"bridge_{t}.json"),
                          _bridge_obj(meta, t, **kw_t, **over))
    return paths


def _patch_paths(tmp_path, meta, **kw):
    return {t: _write(str(tmp_path / f"patch_{t}.json"),
                      _patch_obj(meta, **kw))
            for t in ag.MODELS}


# ---------------------------------------------------------------------------
# §3 materials: the 70-item G18 loader, byte-for-byte previews, skeletons
# ---------------------------------------------------------------------------
def test_scope_is_the_70_g18_items():
    meta = ag.g18_meta()
    assert len(meta) == 70
    assert Counter(m["family"] for m in meta.values()) == {
        "legal_judgment": 40, "evidence_inference": 30}
    assert Counter(m["s"] for m in meta.values()) == {1.0: 50, -1.0: 20}
    # §3/§10: frozen meta["skeleton"] is the cluster key -> 20 skeletons
    assert len({m["cluster"] for m in meta.values()}) == 20
    prefixes = Counter(m["cluster"].split(":")[0] for m in meta.values())
    assert prefixes == {"legal": 40, "infer": 30}


def test_schema_loader_agrees_and_previews_are_byte_for_byte():
    meta = set(ag.g18_meta())
    items = ag.load_g18_items()
    assert len(items) == 70
    assert {i.item_id for i in items} == meta
    for it in items:
        pv = it.meta["previews"]
        # §4: para -> M, unrel -> U, both present and distinct
        assert isinstance(pv["para"], str) and pv["para"]
        assert isinstance(pv["unrel"], str) and pv["unrel"]
        assert pv["para"] != pv["unrel"]
        # every attribute `build()` needs
        for attr in ("base_context", "critical_evidence", "question",
                     "output_spec", "critical_label", "critical_direction"):
            assert getattr(it, attr)
        assert it.meta["skeleton"]


def test_g18_items_are_disjoint_from_stage5():
    g18 = {json.loads(l)["item_id"] for l in open(G18_PATH) if l.strip()}
    s5_path = os.path.join(ROOT, "data/items/items_v1.jsonl")
    s5 = {json.loads(l)["item_id"] for l in open(s5_path) if l.strip()}
    assert g18 & s5 == set()


# ---------------------------------------------------------------------------
# Frozen constants, patch table, parent verdict maps
# ---------------------------------------------------------------------------
def test_constants_are_frozen():
    assert ag.DESIGN_TAG == "g23c-r-fresh-joint-replication-design-v1"
    assert ag.SEED == 20260924
    assert ag.FLOOR == 3.0
    assert ag.BRIDGE_FLOOR == 5.0
    assert ag.IDENTITY_TOL == 0.5
    assert ag.N_RESAMPLES == 10_000
    assert ag.PRIMARY_LAYER == 14
    assert ag.CONTROL_LAYERS == (4, 24)
    assert ag.MIN_MODELS_POSITIVE == 2
    assert ag.MODELS == ("qwen3-8b", "mistral-small-24b")
    assert set(ag.MODEL_IDS) == set(ag.MODELS)
    assert ag.G23CR_LAYERS == (4, 14, 24)
    assert ag.SITE == "rule_end"
    assert ag.POSITION_TOL_TOKENS == 4
    assert ag.POSITION_GATE_FRAC == 0.05
    assert ag.ITEMS_PATH.endswith("g18_v1.jsonl")
    assert ag.FAMILIES == ("legal_judgment", "evidence_inference")


def test_frozen_layers_no_layer_search():
    assert ag.frozen_layers(36) == (4, 14, 24)      # Qwen3-8B
    assert ag.frozen_layers(40) == (4, 14, 24)      # Mistral-Small-24B


def test_scientific_patch_table_is_exactly_the_union():
    # §9.3: 8-cell grid + ME->MA + UE->UA = 10 unique patches
    assert len(ag.SCIENTIFIC) == 10
    assert set(ag.SCIENTIFIC) == EXPECTED_PATCHES
    assert set(ag.GRID8) < set(ag.SCIENTIFIC)
    assert set(ag.SCIENTIFIC) - set(ag.GRID8) == {"ME_to_MA", "UE_to_UA"}
    # every patch name parses to a real donor/recipient pair
    for name in ag.SCIENTIFIC:
        donor, recip = name.split("_to_")
        assert donor in ag.CELLS and recip in ag.CELLS


def test_dir2patch_covers_all_four_g23c_directions():
    assert set(ag.DIR2PATCH) == set(ag.DIRECTIONS)
    expected = {"M_100to0": ("MA", "ME"), "M_0to100": ("ME", "MA"),
                "U_100to0": ("UA", "UE"), "U_0to100": ("UE", "UA")}
    for d, name in ag.DIR2PATCH.items():
        assert name in ag.SCIENTIFIC
        assert tuple(name.split("_to_")) == expected[d], (d, name)


def test_parent_verdict_maps_cover_parents_without_drift():
    assert set(ag.MAP_G23C) == set(ag.G23C_PARENT_VERDICTS) - {"bridge-failed"}
    assert set(ag.MAP_G24B) == set(ag.G24B_PARENT_VERDICTS) - {"bridge-failed"}
    # only the parent's target-conditioned outcome counts as replicated
    assert ag.map_g23c("target-conditioned-policy-state") == "g23c-replicated"
    for v in ag.MAP_G23C:
        if v != "target-conditioned-policy-state":
            assert ag.map_g23c(v) != "g23c-replicated"
    assert ag.map_g24b("donor-conditioned-policy-state") == "g24b-replicated"
    for v in ag.MAP_G24B:
        if v != "donor-conditioned-policy-state":
            assert ag.map_g24b(v) != "g24b-replicated"
    # descriptive licensed texts reuse the parent wording verbatim
    for v in ag.MAP_G23C:
        if v != "target-conditioned-policy-state":
            assert ag.licensed_g23c(ag.MAP_G23C[v], v) == \
                ag.G23C_PARENT_LICENSED[v]
    for v in ag.MAP_G24B:
        if v != "donor-conditioned-policy-state":
            assert ag.licensed_g24b(ag.MAP_G24B[v], v) == \
                ag.G24B_PARENT_LICENSED[v]
    assert ag.licensed_g23c("g23c-replicated", "x") == ag.LICENSED_G23C_REP
    assert ag.licensed_g24b("g24b-replicated", "x") == ag.LICENSED_G24B_REP


# ---------------------------------------------------------------------------
# §5 audit gate semantics
# ---------------------------------------------------------------------------
def test_position_gate_strict_thresholds():
    # all within tolerance -> pass
    g = ag.position_gate({str(i): 4 for i in range(20)})
    assert g["passed"] is True and g["n_over"] == 0
    # strictly greater than 4 counts as over
    g = ag.position_gate({"a": 5, "b": 4})
    assert g["n_over"] == 1 and g["frac_over"] == 0.5
    assert g["passed"] is False
    # exactly 5% is NOT "more than 5%" -> pass
    g = ag.position_gate({str(i): (9 if i < 7 else 1) for i in range(140)})
    assert g["frac_over"] == pytest.approx(0.05)
    assert g["passed"] is True
    # 8/140 > 5% -> fail
    g = ag.position_gate({str(i): (9 if i < 8 else 1) for i in range(140)})
    assert g["frac_over"] > 0.05 and g["passed"] is False
    # empty audit never passes
    assert ag.position_gate({})["passed"] is False


def test_diff_within_containment():
    # divergence inside the window
    assert ag.diff_within([1, 2, 3, 4, 5], [1, 2, 9, 4, 5], 2, 3) is True
    # length shift inside the window (the preview-length case)
    assert ag.diff_within([0, 5, 6, 7], [0, 1, 2, 3, 6, 7], 1, 4) is True
    # divergence starting before the window
    assert ag.diff_within([1, 2, 3, 4, 5], [1, 9, 3, 4, 5], 2, 3) is False
    # divergence ending after the window
    assert ag.diff_within([1, 2, 3, 4], [1, 2, 9, 8], 2, 3) is False
    # identical sequences: no divergence to contain inside a small window
    assert ag.diff_within([1, 2, 3], [1, 2, 3], 0, 1) is False


# ---------------------------------------------------------------------------
# §9.1/§9.2 estimand sign conventions (both item directions)
# ---------------------------------------------------------------------------
def test_switch_and_donor_sign_conventions():
    for s in (1.0, -1.0):
        y = _y(s)
        t = _t(pm_ME=10.0, pm_UE=8.0, pu_ME=2.0, pu_UE=6.0,
               sw_m0=4.0, sw_u0=-2.0)
        patches = _patches_for(s, y, t)
        # G23C switches via the parent formula (raw readouts)
        sw = {d: ag.switch_quantity(d, s, y, patches[ag.DIR2PATCH[d]])
              for d in ag.DIRECTIONS}
        assert sw["M_100to0"] == pytest.approx(t["pm_ME"])   # coupled
        assert sw["M_0to100"] == pytest.approx(t["sw_m0"])
        assert sw["U_100to0"] == pytest.approx(t["pu_UE"])   # coupled
        assert sw["U_0to100"] == pytest.approx(t["sw_u0"])
        pt_m, pt_u, tc = ag.estimands_from_switches(sw)
        assert pt_m == pytest.approx((t["pm_ME"] + t["sw_m0"]) / 2)
        assert pt_u == pytest.approx((t["sw_u0"] + t["pu_UE"]) / 2)
        assert tc == pytest.approx(pt_m - pt_u)
        # G24B donor quantities via the parent function (aligned readouts)
        py = {n: s * patches[n] for n in ag.GRID8}
        q = ag.donor_quantities(py, "L14")
        assert q["donor_policy_m"] == pytest.approx(
            (t["pm_ME"] + t["pm_UE"]) / 2)
        assert q["donor_policy_u"] == pytest.approx(
            (t["pu_ME"] + t["pu_UE"]) / 2)
        assert q["dti"] == pytest.approx(
            ((t["pm_ME"] - t["pu_ME"]) + (t["pm_UE"] - t["pu_UE"])) / 2)


def test_bridge_quantities_sign_aligned():
    y_inc = {"ME": 50.0, "MA": 70.0, "UE": 50.0, "UA": 60.0}
    assert ag.bridge_quantities(+1.0, y_inc) == (20.0, 10.0, 10.0)
    y_dec = {"ME": 50.0, "MA": 30.0, "UE": 50.0, "UA": 40.0}
    assert ag.bridge_quantities(-1.0, y_dec) == (20.0, 10.0, 10.0)


def test_pass_gate_floor_ci_and_model_positivity():
    s = {"n": 6, "n_clusters": 2, "mean": 3.0, "ci_low": 0.1, "ci_high": 5.0}
    assert ag.pass_gate(s, [4.0, 4.0]) is True
    assert ag.pass_gate({**s, "mean": 2.9}, [4.0, 4.0]) is False
    assert ag.pass_gate({**s, "ci_low": 0.0}, [4.0, 4.0]) is False
    assert ag.pass_gate(s, [4.0, -1.0]) is False
    assert ag.pooled_gate(s, ag.BRIDGE_FLOOR) is False


# ---------------------------------------------------------------------------
# §10 pooled skeleton clustering
# ---------------------------------------------------------------------------
def test_bootstrap_is_deterministic_and_clustered():
    pairs = [("c1", 1.0), ("c1", 5.0), ("c2", 3.0)]
    a = ag.summarise(pairs)
    b = ag.summarise(pairs)
    assert a == b
    assert a["n"] == 3 and a["n_clusters"] == 2
    assert a["ci_low"] <= a["mean"] <= a["ci_high"]


def test_pooled_bootstrap_keeps_both_models_of_one_skeleton_together():
    pairs = [("c1", 1.0), ("c1", 2.0), ("c1", 3.0), ("c1", 4.0), ("c2", 5.0)]
    out = ag.summarise(pairs)
    assert out["n"] == 5
    assert out["n_clusters"] == 2


# ---------------------------------------------------------------------------
# §9.3 identity patch integrity
# ---------------------------------------------------------------------------
def test_identity_patch_passes_within_tolerance_and_aborts_outside(tmp_path):
    meta = _meta()
    rep = ag.phase_full(meta, _patch_paths(tmp_path, meta, identity_off=0.4))
    assert rep["identity"]["passed"] is True
    assert rep["identity"]["max_abs_delta"] <= 0.5
    # items x layers x cells x both models — all four cells reported
    assert rep["identity"]["n_checked"] == 6 * 3 * 4 * 2

    with pytest.raises(SystemExit, match="IDENTITY PATCH FAILED"):
        ag.phase_full(meta, _patch_paths(tmp_path, meta, identity_off=0.6))


# ---------------------------------------------------------------------------
# §8 Phase-1 bridge: three gates, each can fail, stop before patching
# ---------------------------------------------------------------------------
def test_bridge_gate_pass_and_each_can_fail(tmp_path):
    meta = _meta()
    rep = ag.phase_bridge(meta, _bridge_paths(tmp_path, meta))
    g = rep["gates"]
    assert g == {"gate1_pooled_policy_effect_m": True,
                 "gate2_pooled_target_policy_interaction": True,
                 "gate3_positive_model_means_2_of_2": True, "passed": True}
    assert rep["verdict"] is None
    assert rep["licensed"] is None
    assert rep["design"]["n_complete"] == {t: 6 for t in ag.MODELS}
    assert rep["design"]["n_clusters"] == 2

    rep1 = ag.phase_bridge(meta, _bridge_paths(tmp_path, meta,
                                               pe_m=4.0, pe_u=-6.0))
    assert rep1["gates"]["gate1_pooled_policy_effect_m"] is False
    assert rep1["gates"]["gate2_pooled_target_policy_interaction"] is True
    assert rep1["verdict"] == "bridge-failed"
    assert rep1["licensed"] == ag.LICENSED_BRIDGE_FAILED

    rep2 = ag.phase_bridge(meta, _bridge_paths(tmp_path, meta,
                                               pe_m=20.0, pe_u=16.0))
    assert rep2["gates"]["gate2_pooled_target_policy_interaction"] is False

    rep3 = ag.phase_bridge(
        meta,
        _bridge_paths(tmp_path, meta,
                      pe_m_by_model={"qwen3-8b": 30.0,
                                     "mistral-small-24b": -1.0},
                      pe_u_by_model={"qwen3-8b": 10.0,
                                     "mistral-small-24b": -7.0}))
    assert rep3["gates"]["gate3_positive_model_means_2_of_2"] is False
    assert rep3["gates"]["passed"] is False


# ---------------------------------------------------------------------------
# §11-§13 outcome map — all four overall verdicts, end to end
# ---------------------------------------------------------------------------
def test_verdict_order_is_literal_and_exhaustive():
    assert ag.OVERALL_VERDICTS == ("jointly-replicated", "partial-replication",
                                   "not-replicated", "bridge-failed")
    assert set(ag.OVERALL_LICENSED) == set(ag.OVERALL_VERDICTS)
    # sub-classifier truth tables are the parents' own logic
    assert ag.g23c_parent_classify(True, True, False, True, True) == \
        "target-conditioned-policy-state"
    assert ag.g23c_parent_classify(True, False, True, True, True) == \
        "target-readiness-only"
    assert ag.g23c_parent_classify(True, True, False, True, False) == \
        "unresolved"
    assert ag.g24b_parent_classify(True, False, True, True, True) == \
        "no-donor-policy-state"
    assert ag.g24b_parent_classify(True, True, True, True, True) == \
        "donor-conditioned-policy-state"
    assert ag.g24b_parent_classify(True, True, False, False, True) == \
        "unresolved"


def test_end_to_end_jointly_replicated(tmp_path):
    meta = _meta()
    rep = ag.phase_full(meta, _patch_paths(tmp_path, meta, targets=GOLD))
    assert rep["bridge"]["gates"]["passed"] is True
    L14 = rep["layers"]["14"]
    # G23C side: PT_M=10, PT_U=0, TC=10
    assert L14["policy_transfer_m"]["pooled"]["mean"] == pytest.approx(10.0)
    assert L14["policy_transfer_u"]["pooled"]["mean"] == pytest.approx(0.0)
    assert L14["target_conditioning"]["pooled"]["mean"] == pytest.approx(10.0)
    assert L14["policy_transfer_m"]["pass"] is True
    assert L14["target_conditioning"]["pass"] is True
    # switches reported per direction (report-only, no floor)
    assert L14["switches"]["M_100to0"]["pooled"]["mean"] == pytest.approx(10.0)
    assert L14["switches"]["M_0to100"]["pooled"]["mean"] == pytest.approx(10.0)
    assert L14["switches"]["U_100to0"]["pooled"]["mean"] == pytest.approx(0.0)
    assert "pass" not in L14["switches"]["M_100to0"]
    # G24B side: DPM=10, DPU=0, DTI=10, both recipients reported
    assert L14["donor_policy_m"]["pooled"]["mean"] == pytest.approx(10.0)
    assert L14["donor_policy_u"]["pooled"]["mean"] == pytest.approx(0.0)
    assert L14["dti"]["pooled"]["mean"] == pytest.approx(10.0)
    assert L14["dti_ME"]["pooled"]["mean"] == pytest.approx(10.0)
    assert L14["dti_UE"]["pooled"]["mean"] == pytest.approx(10.0)
    assert L14["donor_policy_m"]["pass"] is True
    assert L14["dti"]["pass"] is True
    # all 10 union patches reported before averaging
    assert set(L14["patches"]) == EXPECTED_PATCHES
    # controls: both clauses satisfied by the absent arm
    assert rep["controls_g23c"]["passed"] is True
    assert rep["controls_g24b"]["passed"] is True
    assert rep["g23c_sub_verdict"] == "g23c-replicated"
    assert rep["g24b_sub_verdict"] == "g24b-replicated"
    assert rep["g23c_replicated"] is True and rep["g24b_replicated"] is True
    assert rep["verdict"] == "jointly-replicated"
    assert rep["licensed"] == ag.LICENSED_JOINT
    assert rep["g23c_licensed"] == ag.LICENSED_G23C_REP
    assert rep["g24b_licensed"] == ag.LICENSED_G24B_REP
    assert rep["joint_interpretation"] == ag.JOINT_INTERPRETATION
    # design/drop bookkeeping
    assert rep["design"]["seed"] == 20260924
    assert rep["design"]["layers"] == [4, 14, 24]
    assert rep["design"]["controls"] == [4, 24]
    assert rep["design"]["n_clusters"] == 2
    assert rep["design"]["n_complete"] == {t: 6 for t in ag.MODELS}
    assert rep["drops"] == {t: {"missing_item": 0, "unknown_item": 0,
                                "incomplete": 0} for t in ag.MODELS}


def test_end_to_end_partial_g23c_only(tmp_path):
    meta = _meta()
    rep = ag.phase_full(meta, _patch_paths(tmp_path, meta, targets=G23C_ONLY))
    L14 = rep["layers"]["14"]
    # PT_M = mean(0, 10) = 5 passes; TC = 5 passes; DPM = 0 fails
    assert L14["policy_transfer_m"]["pooled"]["mean"] == pytest.approx(5.0)
    assert L14["target_conditioning"]["pooled"]["mean"] == pytest.approx(5.0)
    assert L14["donor_policy_m"]["pooled"]["mean"] == pytest.approx(0.0)
    assert rep["g23c_sub_verdict"] == "g23c-replicated"
    assert rep["g24b_sub_verdict"] == "g24b-no-donor-policy-state"
    assert rep["verdict"] == "partial-replication"
    assert rep["licensed"] == ag.LICENSED_PARTIAL
    # non-replicated side reports the parent wording, not a new claim
    assert rep["g24b_licensed"] == \
        ag.G24B_PARENT_LICENSED["no-donor-policy-state"]
    assert rep["joint_interpretation"] is None


def test_end_to_end_partial_g24b_only(tmp_path):
    meta = _meta()
    rep = ag.phase_full(meta, _patch_paths(tmp_path, meta, targets=G24B_ONLY))
    L14 = rep["layers"]["14"]
    # PT_M = mean(10, -10) = 0 fails -> G23C readiness-only; G24B passes
    assert L14["policy_transfer_m"]["pooled"]["mean"] == pytest.approx(0.0)
    assert L14["donor_policy_m"]["pooled"]["mean"] == pytest.approx(10.0)
    assert L14["dti"]["pooled"]["mean"] == pytest.approx(10.0)
    assert rep["g23c_sub_verdict"] == "g23c-target-readiness-only"
    assert rep["g24b_sub_verdict"] == "g24b-replicated"
    assert rep["verdict"] == "partial-replication"
    assert rep["licensed"] == ag.LICENSED_PARTIAL
    assert rep["g23c_licensed"] == \
        ag.G23C_PARENT_LICENSED["target-readiness-only"]


def test_end_to_end_not_replicated(tmp_path):
    meta = _meta()
    rep = ag.phase_full(meta, _patch_paths(tmp_path, meta, targets=NONE14))
    assert rep["bridge"]["gates"]["passed"] is True
    assert rep["g23c_sub_verdict"] == "g23c-target-readiness-only"
    assert rep["g24b_sub_verdict"] == "g24b-no-donor-policy-state"
    assert rep["verdict"] == "not-replicated"
    assert rep["licensed"] == ag.LICENSED_NOT_REPL
    assert rep["joint_interpretation"] is None


def test_end_to_end_stop_rule_bridge_failure_blocks_all_statistics(tmp_path):
    meta = _meta()
    rep = ag.phase_full(meta, _patch_paths(tmp_path, meta, pe_m=0.0,
                                           pe_u=0.0))
    assert rep["bridge"]["gates"]["passed"] is False
    assert rep["verdict"] == "bridge-failed"
    assert rep["layers"] is None
    assert rep["controls_g23c"] is None and rep["controls_g24b"] is None
    assert rep["g23c_sub_verdict"] is None and rep["g24b_sub_verdict"] is None
    assert rep["licensed"] == ag.LICENSED_BRIDGE_FAILED
    # identity still checked first: broken patcher never yields a verdict
    with pytest.raises(SystemExit, match="IDENTITY PATCH FAILED"):
        ag.phase_full(meta, _patch_paths(tmp_path, meta, pe_m=0.0,
                                         pe_u=0.0, identity_off=0.6))


def test_end_to_end_controls_trap_g23c_side(tmp_path):
    # TC equally strong at L4/L24 -> G23C control clause fails -> G23C
    # unresolved (not replicated) while G24B still replicates -> partial
    meta = _meta()
    rep = ag.phase_full(meta, _patch_paths(tmp_path, meta,
                                           targets=CTRL_TRAP_G23C))
    assert rep["controls_g23c"]["passed"] is False
    assert rep["controls_g24b"]["passed"] is True
    assert rep["g23c_sub_verdict"] == "g23c-unresolved"
    assert rep["g24b_sub_verdict"] == "g24b-replicated"
    assert rep["verdict"] == "partial-replication"


def test_end_to_end_controls_trap_g24b_side(tmp_path):
    # DTI equally strong at L4/L24 -> G24B control clause fails while G23C
    # controls stay satisfied (TC absent there) -> partial the other way
    meta = _meta()
    rep = ag.phase_full(meta, _patch_paths(tmp_path, meta,
                                           targets=CTRL_TRAP_G24B))
    assert rep["controls_g23c"]["passed"] is True
    assert rep["controls_g24b"]["passed"] is False
    assert rep["g23c_sub_verdict"] == "g23c-replicated"
    assert rep["g24b_sub_verdict"] == "g24b-unresolved"
    assert rep["verdict"] == "partial-replication"


# ---------------------------------------------------------------------------
# Drop accounting and the frozen design guard
# ---------------------------------------------------------------------------
def test_drops_missing_unknown_incomplete(tmp_path):
    meta = _meta()
    paths = _patch_paths(tmp_path, meta)
    obj = json.load(open(paths[ag.MODELS[0]]))
    obj["records"] = obj["records"][:-1]                       # missing item
    obj["records"].append({"item_id": "nope", "direction": "increase",
                           "y": _y(1.0), "n_tok": {}, "patch": {},
                           "identity": {}})
    obj["records"][0]["patch"]["MA_to_ME"].pop("24")            # incomplete
    _write(paths[ag.MODELS[0]], obj)

    rep = ag.phase_full(meta, paths)
    assert rep["drops"][ag.MODELS[0]] == {"missing_item": 1,
                                          "unknown_item": 1,
                                          "incomplete": 1}
    assert rep["design"]["n_complete"][ag.MODELS[0]] == 4
    assert rep["drops"][ag.MODELS[1]] == {"missing_item": 0,
                                          "unknown_item": 0,
                                          "incomplete": 0}

    # a missing identity layer is incomplete for the patch phase ...
    p2 = _patch_paths(tmp_path, meta, drop_identity_layer=4)
    rep2 = ag.phase_full(meta, p2)
    assert rep2["drops"][ag.MODELS[0]]["incomplete"] == 6

    # ... while the bridge phase only needs the four baselines
    b_paths = _bridge_paths(tmp_path, meta)
    b_obj = json.load(open(b_paths[ag.MODELS[0]]))
    b_obj["records"].pop()
    _write(b_paths[ag.MODELS[0]], b_obj)
    b_rep = ag.phase_bridge(meta, b_paths)
    assert b_rep["drops"][ag.MODELS[0]]["missing_item"] == 1


def test_gather_rejects_a_non_frozen_layer_design(tmp_path):
    meta = _meta()
    obj = _patch_obj(meta)
    obj["design"]["layers"] = [4, 10, 24]
    path = _write(str(tmp_path / "bad.json"), obj)
    with pytest.raises(SystemExit, match="frozen configuration"):
        ag.gather({t: path for t in ag.MODELS}, meta, phase="full")


def test_gather_rejects_a_foreign_design_tag(tmp_path):
    meta = _meta()
    obj = _patch_obj(meta)
    obj["design"]["design_tag"] = "some-other-tag"
    path = _write(str(tmp_path / "bad2.json"), obj)
    with pytest.raises(SystemExit, match="frozen configuration"):
        ag.gather({t: path for t in ag.MODELS}, meta, phase="full")


# ---------------------------------------------------------------------------
# Runner wiring — byte-for-byte previews by import, audit before compute
# ---------------------------------------------------------------------------
def test_runner_wiring_matches_the_prereg():
    with open(RUNNER_PATH) as handle:
        src = handle.read()
    # §6: the Stage-5 builders are imported, never re-implemented
    assert "from patch_matched import build, sites_of" in src
    for ddef in ("def build(", "def sites_of("):
        assert ddef not in src
    # §4: no new preview construction anywhere in the runner (the module
    # docstring may name it only to record that it is NOT used)
    assert "from patch_matched import matched_previews" not in src
    assert "matched_previews(" not in src
    assert 'item.meta["previews"]' in src
    # the G18 loader, not the Stage-5 loader
    assert "load_g18_items" in src
    assert "frozen_items" not in src
    # §7/§8: frozen layers only, single site, the 10-patch union, identity
    assert '"--layer' not in src
    assert "frozen_layers(" in src
    assert "rule_end" in src
    assert "register_forward_hook" in src
    assert "SCIENTIFIC" in src
    assert "ME_to_ME" in src and "UE_to_UE" in src       # grid-reused identity
    assert 'for cell in ("MA", "UA")' in src             # fresh identity runs
    # three phases; the audit is tokenizer-only (no model load in run_audit)
    assert 'choices=["audit", "bridge", "patch"]' in src
    audit_body = src.split("def run_audit")[1].split("def main")[0]
    assert "AutoTokenizer" in audit_body
    assert "load_model(" not in audit_body
    assert "load_model(" in src                          # ... but used later


def test_analyzer_reuses_parent_classifiers_and_estimators():
    with open(ANALYZER_PATH) as handle:
        src = handle.read()
    # parent machinery is called, never re-implemented
    for defname in ("def classify(", "def donor_quantities(",
                    "def switch_quantity(", "def bridge_stats(",
                    "def _identity_check("):
        assert defname not in src
    assert "g23c_parent_classify(True" in src
    assert "g24b_parent_classify(True" in src
    assert "g18_meta" in src and "meta[\"skeleton\"]" in src
    # §10: this round's frozen seed wraps the parent bootstrap
    assert "G24B_SEED" in src


# ---------------------------------------------------------------------------
# Honest state pins: §5 audit FAILED -> not frozen, no compute
# ---------------------------------------------------------------------------
def test_audit_v1_record_stops_the_design():
    with open(AUDIT_PATH) as handle:
        audit = json.load(handle)
    assert audit["passed"] is False
    assert audit["design_tag"] == ag.DESIGN_TAG
    assert audit["audit"] == "tokenizer-only"
    assert audit["items"] == 70 and audit["cells"] == ["ME", "MA", "UE", "UA"]
    # checks 1-6 all green; only the position gate fails
    for m in audit["models"]:
        f = audit["per_model"][m]["failures"]
        assert all(len(v) == 0 for v in f.values()), m
        assert audit["per_model"][m]["n_checked_cells"] == 280
    g = audit["gate_all_models"]
    assert g["n_pairs"] == 140 and g["n_over"] == 17
    assert g["frac_over"] > 0.05 and g["passed"] is False
    assert audit["per_model"]["qwen3-8b"]["gate"]["n_over"] == 7
    assert audit["per_model"]["mistral-small-24b"]["gate"]["n_over"] == 10


def test_checklist_still_unchecked_and_prereg_is_parked():
    with open(PREREG_PATH) as handle:
        prereg = handle.read()
    # the round never froze: every §16 box stays unchecked
    boxes = [l for l in prereg.splitlines() if l.startswith("- [")]
    assert len(boxes) == 12
    assert all(b.startswith("- [ ]") for b in boxes)
    assert "NO G23C-R COMPUTE." in prereg
    # parked by the novelty restructure (commit c051821), never tagged
    assert "HOLD — DESIGN PRESERVED, NO COMPUTE" in prereg
    assert "downgraded from headline novelty" in prereg
    assert ag.DESIGN_TAG not in prereg          # never tagged


# ---------------------------------------------------------------------------
# Prereg wording lock
# ---------------------------------------------------------------------------
def _norm(text):
    return " ".join(text.replace(">", " ").replace("*", " ").split())


def test_licensed_texts_are_verbatim_in_the_prereg():
    with open(PREREG_PATH) as handle:
        prereg = handle.read()
    flat = _norm(prereg)
    for sentence in (ag.LICENSED_G23C_REP, ag.LICENSED_G24B_REP,
                     ag.LICENSED_JOINT, ag.LICENSED_PARTIAL,
                     ag.LICENSED_NOT_REPL, ag.LICENSED_BRIDGE_FAILED,
                     ag.JOINT_INTERPRETATION):
        assert _norm(sentence) in flat, sentence
    for name in ag.OVERALL_VERDICTS:
        assert name in prereg
    for term in ("g23c-replicated", "g24b-replicated",
                 "g23c-generic-policy-state", "g23c-target-readiness-only",
                 "g23c-unresolved", "g24b-donor-generic-policy-state",
                 "g24b-no-donor-policy-state", "g24b-unresolved",
                 "PolicyTransfer_M", "PolicyTransfer_U", "TargetConditioning",
                 "DonorPolicy_M", "DonorPolicy_U", "DonorTargetInteraction",
                 "ME -> MA", "UE -> UA", "rule_end", "L14 primary",
                 "L4/L14/L24", "seed `20260924`", "10,000 percentile",
                 "20 independent skeletons", "byte-for-byte", "skeleton"):
        assert term in prereg, term


def test_prereg_records_the_audit_and_anti_repair_rules():
    with open(PREREG_PATH) as handle:
        prereg = handle.read()
    # §5 stop rule + the forbidden repairs, verbatim
    assert "Do not pad, truncate, rewrite, or drop individual items" in prereg
    assert "redesigned and re-frozen before compute" in prereg
    assert "more than **5% of item/model pairs**" in prereg
    assert "greater than **4 tokens**" in prereg
    # no outcome of this round launches another round, and the paper-writing
    # order (Sections 4/5/6 first) is codified in the prereg itself
    assert "No automatic G23D follows any outcome." in prereg
    assert "It is not a license to add another experiment now." in prereg
    # materials honesty: disjoint/frozen, not "fresh data"
    assert "disjoint" in prereg and "frozen" in prereg
