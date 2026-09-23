"""G24B design tests — nothing here touches a model.

Loads only the stdlib-only frozen analyzer (`src/mech/analyze_g24b.py`); the
runner is checked as source text.  Covers prereg §11.4's mandatory list — sign
conventions, identity patch, pooled skeleton clustering, fixed layers and the
§4/§8 stop rule — plus the §3 cell table, the three §4 bridge gates, all five
§8 verdicts end to end on synthetic records, drop accounting, the frozen
layer/design guard, runner wiring (§11.1 construction by import) and the
prereg semantic freeze.
"""
from __future__ import annotations

import importlib.util
import json
import os
from collections import Counter

import pytest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
_spec = importlib.util.spec_from_file_location(
    "analyze_g24b", os.path.join(ROOT, "src/mech/analyze_g24b.py"))
ag = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ag)

PREREG_PATH = os.path.join(
    ROOT, "preregistrations/PREREGISTRATION_G24B_DONOR_RECIPIENT_FACTORIZATION.md")
RUNNER_PATH = os.path.join(ROOT, "src/mech/g24b_donor_state.py")
G23C_PREREG = os.path.join(
    ROOT, "preregistrations/PREREGISTRATION_G23C_TARGET_CONDITIONED_POLICY_STATE.md")
LAYERS = (4, 14, 24)


# ---------------------------------------------------------------------------
# Synthetic fixtures
# ---------------------------------------------------------------------------
def _meta(n=6):
    """n items, alternating sign, two clusters (c0 gets items 0,1,4,5)."""
    return {f"i{k}": {"cluster": f"c{k // 2 % 2}", "family": "legal_judgment",
                      "s": 1.0 if k % 2 == 0 else -1.0}
            for k in range(n)}


def _y(s, pe_m=20.0, pe_u=10.0):
    """Baselines whose §4 quantities are exactly (pe_m, pe_u, pe_m - pe_u)."""
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
            "identity_tol": ag.IDENTITY_TOL, "families": list(ag.FAMILIES),
            "seed": ag.G24B_SEED}


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


def _patched(name, s, y, v):
    """Recipient output achieving signed-aligned switch v for grid cell `name`."""
    donor, recip = ag.PATCHES[name]
    # pm: v = s*(MA->recip - ME->recip); for identity/other cells fall through.
    # We express the recipient readout directly: baseline of recipient + v*s
    # is wrong for every donor; instead build from the recipient's own cell.
    # Simpler: recipient readout = y[recip] + v * s for the *matched* policy
    # donor, but the estimator differences donors within a fixed recipient, so
    # we set outputs so the estimator recovers the target.  We define outputs
    # per (donor,recip) below in _grid_for_targets instead.
    raise NotImplementedError


def _grid_for_targets(s, y, targets):
    """targets: {L: {pm_ME, pu_ME, pm_UE, pm_UE-ish donor_policy}} -> grid dict.

    Builds the 8 grid patched readouts so that donor_quantities() recovers the
    requested per-recipient pm/pu.  We set, per recipient R:
        ME_to_R = y[R]                       (reference donor, policy-0 matched)
        MA_to_R = ME_to_R + pm_R * s         (matched donor, policy-100)
        UE_to_R = y[R] + off_ue_R            (unrelated policy-0 donor)
        UA_to_R = UE_to_R + pu_R * s         (unrelated donor, policy-100)
    with off chosen so UE_to_R stays distinct but the contrast only sees pu_R.
    Setting off_ue_R = 0 makes UE_to_R == y[R] (recipient baseline), which is a
    legitimate patched output (the unrelated-0 donor state can equal baseline).
    """
    out = {}
    for L in LAYERS:
        t = targets[str(L)]
        g = {}
        for R in ag.RECIPIENTS:
            base = y[R]
            pm, pu = t[f"pm_{R}"], t[f"pu_{R}"]
            g[f"ME_to_{R}"] = base
            g[f"MA_to_{R}"] = base + pm * s
            g[f"UE_to_{R}"] = base
            g[f"UA_to_{R}"] = base + pu * s
        out[str(L)] = g
    return out


def _targets(pm_ME, pu_ME, pm_UE, pu_UE):
    t14 = {"pm_ME": pm_ME, "pu_ME": pu_ME, "pm_UE": pm_UE, "pu_UE": pu_UE}
    zero = {k: 0.0 for k in t14}
    return {"4": zero, "14": t14, "24": zero}


GOLD = _targets(pm_ME=10.0, pu_ME=0.0, pm_UE=10.0, pu_UE=0.0)   # dti = 10
CTRL_ZERO = _targets(pm_ME=0.0, pu_ME=0.0, pm_UE=0.0, pu_UE=0.0)


def _patch_obj(meta, targets=GOLD, ctrl_targets=None, pe_m=20.0, pe_u=10.0,
               identity_off=0.0):
    if ctrl_targets is None:
        ctrl_targets = {"4": {k: 0.0 for k in targets["14"]},
                        "24": {k: 0.0 for k in targets["14"]}}
    merged = {"4": ctrl_targets["4"], "14": targets["14"],
              "24": ctrl_targets["24"]}
    records = []
    for iid, m in meta.items():
        s = m["s"]
        y = _y(s, pe_m, pe_u)
        grid_by_L = _grid_for_targets(s, y, merged)
        rec = {
            "item_id": iid, "direction": "increase" if s > 0 else "decrease",
            "y": y, "n_tok": {c: 0 for c in ag.CELLS},
            "patch": {n: {str(L): grid_by_L[str(L)][n] for L in LAYERS}
                      for n in ag.PATCHES},
            "identity": {str(L): {c: y[c] + identity_off for c in ag.CELLS}
                         for L in LAYERS}}
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
# Scope, constants, cell table, grid
# ---------------------------------------------------------------------------
def test_scope_is_the_75_stage5_items():
    meta = ag.load_frozen_meta()
    assert len(meta) == 75
    assert Counter(m["family"] for m in meta.values()) == {
        "legal_judgment": 45, "evidence_inference": 30}
    assert Counter(m["s"] for m in meta.values()) == {1.0: 40, -1.0: 35}
    # §7 skeleton key: repository-standard cluster_of -> 15 clusters
    assert len({m["cluster"] for m in meta.values()}) == 15
    for m in meta.values():
        assert m["cluster"].startswith("legal:") or \
            m["cluster"].startswith("evidence_inference:")


def test_constants_are_frozen():
    assert ag.FLOOR == 3.0
    assert ag.BRIDGE_FLOOR == 5.0
    assert ag.IDENTITY_TOL == 0.5
    assert ag.G24B_SEED == 20260924
    assert ag.N_RESAMPLES == 10_000
    assert ag.PRIMARY_LAYER == 14
    assert ag.CONTROL_LAYERS == (4, 24)
    assert ag.MIN_MODELS_POSITIVE == 2
    assert ag.DESIGN_TAG == "g24b-donor-recipient-factorization-design-v1"
    assert ag.MODELS == ("qwen3-8b", "mistral-small-24b")
    assert set(ag.MODEL_IDS) == set(ag.MODELS)


def test_cell_table_and_eight_grid():
    # §3: ME=M0, MA=M100, UE=U0, UA=U100
    assert ag.CELLS == ("ME", "MA", "UE", "UA")
    assert ag.CELL_TABLE == {"ME": ("match", False), "MA": ("match", True),
                             "UE": ("unrel", False), "UA": ("unrel", True)}
    # §6: every cell is a donor; only the two policy-0 cells are recipients
    assert ag.DONORS == ("ME", "MA", "UE", "UA")
    assert ag.RECIPIENTS == ("ME", "UE")
    assert len(ag.PATCHES) == 8
    assert set(ag.PATCHES) == {
        f"{d}_to_{r}" for r in ag.RECIPIENTS for d in ag.DONORS}
    # grid stores (donor, recipient)
    assert ag.PATCHES["MA_to_ME"] == ("MA", "ME")
    assert ag.PATCHES["UA_to_UE"] == ("UA", "UE")


def test_frozen_layers_no_layer_search():
    assert ag.frozen_layers(36) == (4, 14, 24)      # Qwen3-8B
    assert ag.frozen_layers(40) == (4, 14, 24)      # Mistral-Small-24B
    assert ag.frozen_layers(20) == (4, 14, 19)      # nearest valid < 25 layers
    assert ag.nearest_layer_24(24) == 23
    assert ag.nearest_layer_24(25) == 24


# ---------------------------------------------------------------------------
# §4 bridge estimands and gates (reused from G23C, cross-checked)
# ---------------------------------------------------------------------------
def test_bridge_quantities_sign_aligned_formulas():
    y_inc = {"ME": 50.0, "MA": 70.0, "UE": 50.0, "UA": 60.0}
    assert ag.bridge_quantities(+1.0, y_inc) == (20.0, 10.0, 10.0)
    y_dec = {"ME": 50.0, "MA": 30.0, "UE": 50.0, "UA": 40.0}
    assert ag.bridge_quantities(-1.0, y_dec) == (20.0, 10.0, 10.0)


def test_gate_triple_and_frozen_cross_check(tmp_path):
    good = {"gate1_pooled_policy_effect_m": True,
            "gate2_pooled_target_policy_interaction": True,
            "gate3_positive_model_means_2_of_2": True, "passed": True}
    assert ag.gate_triple(good) == (True, True, True, True)
    frozen = _write(str(tmp_path / "frozen.json"), {"gates": good})
    assert ag.require_frozen_bridge(good, frozen_path=frozen) is True
    # a mismatch aborts: baseline no longer reproducible
    bad = dict(good, gate1_pooled_policy_effect_m=False, passed=False)
    with pytest.raises(SystemExit, match="no longer reproducible"):
        ag.require_frozen_bridge(bad, frozen_path=frozen)
    with pytest.raises(SystemExit, match="not found"):
        ag.require_frozen_bridge(good, frozen_path=str(tmp_path / "nope.json"))


def test_bridge_gate_all_three_pass_and_each_can_fail(tmp_path):
    meta = _meta()
    rep = ag.phase_bridge(meta, _bridge_paths(tmp_path, meta))
    g = rep["gates"]
    assert g == {"gate1_pooled_policy_effect_m": True,
                 "gate2_pooled_target_policy_interaction": True,
                 "gate3_positive_model_means_2_of_2": True, "passed": True}
    assert rep["verdict"] is None

    rep1 = ag.phase_bridge(meta, _bridge_paths(tmp_path, meta,
                                               pe_m=4.0, pe_u=-6.0))
    assert rep1["gates"]["gate1_pooled_policy_effect_m"] is False
    assert rep1["gates"]["gate2_pooled_target_policy_interaction"] is True
    assert rep1["gates"]["passed"] is False
    assert rep1["verdict"] == "bridge-failed"
    assert rep1["licensed"] == ag.LICENSED["bridge-failed"]

    rep2 = ag.phase_bridge(meta, _bridge_paths(tmp_path, meta,
                                               pe_m=20.0, pe_u=16.0))
    assert rep2["gates"]["gate2_pooled_target_policy_interaction"] is False
    assert rep2["gates"]["passed"] is False

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
# §6 donor-side estimands and sign conventions
# ---------------------------------------------------------------------------
def test_donor_quantities_pooled_over_recipients():
    # signed-aligned outputs; pm_ME=10, pu_ME=0, pm_UE=8, pu_UE=2
    py = {}
    for R, pm, pu in (("ME", 10.0, 0.0), ("UE", 8.0, 2.0)):
        py[f"ME_to_{R}"] = 50.0
        py[f"MA_to_{R}"] = 50.0 + pm
        py[f"UE_to_{R}"] = 50.0
        py[f"UA_to_{R}"] = 50.0 + pu
    q = ag.donor_quantities(py, "L14")
    assert q["pm_ME"] == pytest.approx(10.0)
    assert q["pu_ME"] == pytest.approx(0.0)
    assert q["dti_ME"] == pytest.approx(10.0)
    assert q["pm_UE"] == pytest.approx(8.0)
    assert q["pu_UE"] == pytest.approx(2.0)
    assert q["dti_UE"] == pytest.approx(6.0)
    assert q["donor_policy_m"] == pytest.approx(9.0)     # mean(10, 8)
    assert q["donor_policy_u"] == pytest.approx(1.0)     # mean(0, 2)
    assert q["dti"] == pytest.approx(8.0)                # mean(10, 6)


def test_donor_quantities_requires_full_grid():
    with pytest.raises(SystemExit, match="need all 8 grid patches"):
        ag.donor_quantities({"MA_to_ME": 1.0}, "L14")


def test_pass_gate_floor_ci_and_model_positivity():
    s = {"n": 6, "n_clusters": 2, "mean": 3.0, "ci_low": 0.1, "ci_high": 5.0}
    assert ag.pass_gate(s, [4.0, 4.0]) is True
    assert ag.pass_gate({**s, "mean": 2.9}, [4.0, 4.0]) is False     # floor
    assert ag.pass_gate({**s, "ci_low": 0.0}, [4.0, 4.0]) is False   # ci strict
    assert ag.pass_gate(s, [4.0, -1.0]) is False                     # 1/2
    assert ag.pooled_gate(s, ag.BRIDGE_FLOOR) is False               # 5.0 floor


# ---------------------------------------------------------------------------
# §7 pooled skeleton clustering
# ---------------------------------------------------------------------------
def test_bootstrap_is_deterministic_and_clustered():
    pairs = [("c1", 1.0), ("c1", 5.0), ("c2", 3.0)]
    a = ag.summarise(pairs)
    b = ag.summarise(pairs)
    assert a == b                                    # same seed -> same interval
    assert a["n"] == 3 and a["n_clusters"] == 2
    assert a["ci_low"] <= a["mean"] <= a["ci_high"]


def test_pooled_bootstrap_keeps_both_models_of_one_skeleton_in_one_cluster():
    pairs = [("c1", 1.0), ("c1", 2.0), ("c1", 3.0), ("c1", 4.0), ("c2", 5.0)]
    out = ag.summarise(pairs)
    assert out["n"] == 5
    assert out["n_clusters"] == 2     # never 5 rows / never doubled by model


# ---------------------------------------------------------------------------
# §9.1 identity patch integrity
# ---------------------------------------------------------------------------
def test_identity_patch_passes_within_tolerance_and_aborts_outside(tmp_path):
    meta = _meta()
    rep = ag.phase_full(meta, _patch_paths(tmp_path, meta, identity_off=0.4))
    assert rep["identity"]["passed"] is True
    assert rep["identity"]["max_abs_delta"] <= 0.5
    # items x layers x cells x both models
    assert rep["identity"]["n_checked"] == 6 * 3 * 4 * 2

    with pytest.raises(SystemExit, match="IDENTITY PATCH FAILED"):
        ag.phase_full(meta, _patch_paths(tmp_path, meta, identity_off=0.6))


# ---------------------------------------------------------------------------
# §8 outcome map — all five verdicts, end to end
# ---------------------------------------------------------------------------
def test_verdict_order_is_literal_and_exhaustive():
    assert ag.classify(False, True, True, True, True) == "bridge-failed"
    assert ag.classify(True, False, True, True, True) == "no-donor-policy-state"
    assert ag.classify(True, True, True, True, True) == \
        "donor-conditioned-policy-state"
    # generic: both donor-policy transfers pass, primary does not
    assert ag.classify(True, True, True, False, True) == \
        "donor-generic-policy-state"
    # dpu fails (and dti fails) -> neither no-donor (dpm passed) nor generic
    # (dpu failed) nor conditioned (dti failed) -> unresolved
    assert ag.classify(True, True, False, False, True) == "unresolved"
    # strict literal: dti passes but control clause fails -> unresolved
    assert ag.classify(True, True, True, True, False) == "unresolved"
    # dpm fails -> no-donor wins even if dti would pass
    assert ag.classify(True, False, True, True, True) == "no-donor-policy-state"


def test_end_to_end_donor_conditioned(tmp_path):
    meta = _meta()
    rep = ag.phase_full(meta, _patch_paths(tmp_path, meta, targets=GOLD))
    assert rep["bridge"]["gates"]["passed"] is True
    L14 = rep["layers"]["14"]
    # GOLD: pm_ME=10, pu_ME=0, pm_UE=10, pu_UE=0
    assert L14["donor_policy_m"]["pooled"]["mean"] == pytest.approx(10.0)
    assert L14["donor_policy_u"]["pooled"]["mean"] == pytest.approx(0.0)
    assert L14["dti"]["pooled"]["mean"] == pytest.approx(10.0)
    assert L14["dti_ME"]["pooled"]["mean"] == pytest.approx(10.0)
    assert L14["dti_UE"]["pooled"]["mean"] == pytest.approx(10.0)
    assert L14["donor_policy_m"]["pass"] is True
    assert L14["dti"]["pass"] is True
    # all eight grid cells reported before averaging (§9.5)
    assert set(L14["patches"]) == set(ag.PATCHES)
    assert rep["controls"]["passed"] is True
    assert rep["verdict"] == "donor-conditioned-policy-state"
    assert rep["licensed"] == ag.LICENSED["donor-conditioned-policy-state"]
    assert rep["design"]["n_complete"] == {t: 6 for t in ag.MODELS}
    assert rep["drops"] == {t: {"missing_item": 0, "unknown_item": 0,
                                "incomplete": 0} for t in ag.MODELS}


def test_end_to_end_generic_none_unresolved(tmp_path):
    meta = _meta()
    # generic: donor policy transfers (pm, pu both > 0) but dti == 0
    generic = _targets(pm_ME=10.0, pu_ME=10.0, pm_UE=10.0, pu_UE=10.0)
    rep = ag.phase_full(meta, _patch_paths(tmp_path, meta, targets=generic))
    assert rep["verdict"] == "donor-generic-policy-state"
    assert rep["licensed"] == ag.LICENSED["donor-generic-policy-state"]

    # no-donor: bridge passes but DonorPolicy_M does not (pm == 0 everywhere)
    none14 = _targets(pm_ME=0.0, pu_ME=0.0, pm_UE=0.0, pu_UE=0.0)
    rep2 = ag.phase_full(meta, _patch_paths(tmp_path, meta, targets=none14))
    assert rep2["bridge"]["gates"]["passed"] is True
    assert rep2["layers"]["14"]["donor_policy_m"]["pass"] is False
    assert rep2["verdict"] == "no-donor-policy-state"
    assert rep2["licensed"] == ag.LICENSED["no-donor-policy-state"]

    # unresolved: dti equally present at the control layers
    # (controls carry GOLD's L14 pattern, not zeros)
    same_ctrl = {"4": GOLD["14"], "24": GOLD["14"]}
    rep3 = ag.phase_full(meta, _patch_paths(tmp_path, meta,
                                            targets=GOLD,
                                            ctrl_targets=same_ctrl))
    assert rep3["layers"]["14"]["dti"]["pass"] is True
    assert rep3["controls"]["passed"] is False
    assert rep3["verdict"] == "unresolved"

    # control clause satisfied by the "substantially weaker" arm: dti at a
    # control layer passes but trails L14 by >= one floor
    # dti_ctrl = (pm - pu) = (10 - 7) = 3; L14 dti = 10; gap = 7 >= 3.0
    w = {"pm_ME": 10.0, "pu_ME": 7.0, "pm_UE": 10.0, "pu_UE": 7.0}
    ctrl_weaker = {"4": w, "24": w}
    rep4 = ag.phase_full(meta, _patch_paths(tmp_path, meta, targets=GOLD,
                                            ctrl_targets=ctrl_weaker))
    assert rep4["controls"]["layers"]["4"]["dti_pass"] is True
    assert rep4["controls"]["layers"]["4"]["weaker_by_floor"] is True
    assert rep4["verdict"] == "donor-conditioned-policy-state"

    # same shape but the gap is under the floor -> unresolved
    # dti_ctrl = (10 - 1) = 9; L14 dti = 10; gap = 1.0 < 3.0 -> not weaker,
    # and the control dti still passes -> both clauses false -> unresolved
    n = {"pm_ME": 10.0, "pu_ME": 1.0, "pm_UE": 10.0, "pu_UE": 1.0}
    ctrl_near = {"4": n, "24": n}
    rep5 = ag.phase_full(meta, _patch_paths(tmp_path, meta, targets=GOLD,
                                            ctrl_targets=ctrl_near))
    assert rep5["controls"]["layers"]["4"]["dti_pass"] is True
    assert rep5["controls"]["layers"]["4"]["weaker_by_floor"] is False
    assert rep5["verdict"] == "unresolved"


def test_end_to_end_stop_rule_bridge_failure_blocks_transfer(tmp_path):
    # §4: the bridge is evaluated before any donor statistic; on failure the
    # round stops and no donor statistics are reported.
    meta = _meta()
    rep = ag.phase_full(meta, _patch_paths(tmp_path, meta, pe_m=0.0,
                                           pe_u=0.0))
    assert rep["bridge"]["gates"]["passed"] is False
    assert rep["verdict"] == "bridge-failed"
    assert rep["layers"] is None
    assert rep["controls"] is None
    assert rep["licensed"] == ag.LICENSED["bridge-failed"]
    # identity still checked first: broken patcher never yields a verdict
    with pytest.raises(SystemExit, match="IDENTITY PATCH FAILED"):
        ag.phase_full(meta, _patch_paths(tmp_path, meta, pe_m=0.0,
                                         pe_u=0.0, identity_off=0.6))


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
    obj["records"][0]["patch"]["MA_to_ME"].pop("24")           # incomplete
    _write(paths[ag.MODELS[0]], obj)

    rep = ag.phase_full(meta, paths)
    d = rep["drops"][ag.MODELS[0]]
    assert d == {"missing_item": 1, "unknown_item": 1, "incomplete": 1}
    # 6 items - 1 missing - 1 incomplete = 4 complete
    assert rep["design"]["n_complete"][ag.MODELS[0]] == 4
    assert rep["drops"][ag.MODELS[1]] == {"missing_item": 0,
                                          "unknown_item": 0, "incomplete": 0}
    # the same records are complete for the bridge phase (y only)
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
# Runner wiring — §11.1 reconstruction by import, no layer flag
# ---------------------------------------------------------------------------
def test_runner_reconstructs_stage5_cells_by_import():
    with open(RUNNER_PATH) as handle:
        src = handle.read()
    # §11.1: the Stage-5 builders are imported, never re-implemented
    assert "from patch_matched import matched_previews, build, sites_of" in src
    for ddef in ("def matched_previews", "def build(", "def sites_of("):
        assert ddef not in src
    # cells reused from the G23C runner (one copy of the construction checks)
    assert "from g23c_policy_state import build_cells" in src
    assert "def build_cells" not in src
    assert "from analyze_g24b import" in src      # one copy of the frozen spec
    assert "from analyze_g23c import" in src
    # §5/§6: frozen layers only, single site, the 8-grid, identity
    assert '"--layer' not in src                  # no layer search CLI
    assert "frozen_layers(" in src
    assert "rule_end" in src
    assert "register_forward_hook" in src
    assert 'if args.phase == "patch":' in src
    assert "identity" in src
    assert "PATCHES" in src and "RECIPIENTS" in src and "DONORS" in src
    # §11 dry run: tokenizer-only audit, no forward pass
    assert "--dry-run" in src and "DRY RUN OK" in src


# ---------------------------------------------------------------------------
# Prereg semantic freeze
# ---------------------------------------------------------------------------
def _norm(text):
    return " ".join(text.replace(">", " ").replace("*", " ").split())


def test_semantic_freeze_matches_the_preregistration():
    with open(PREREG_PATH) as handle:
        prereg = handle.read()
    assert set(ag.LICENSED) == set(ag.VERDICTS)
    for name in ag.VERDICTS:
        assert name in prereg
    flat = _norm(prereg)
    for sentence in ag.LICENSED.values():
        assert _norm(sentence) in flat
    for term in ("DonorPolicy_M", "DonorPolicy_U", "DonorTargetInteraction",
                 "PolicyEffect_M", "PolicyEffect_U", "TargetPolicyInteraction",
                 "ME -> ME", "MA -> ME", "UA -> ME", "ME -> UE",
                 "UA -> UE", "rule_end", "layer 14",
                 "seed `20260924`", "10,000 percentile resamples",
                 "3.0 rating points", "0.5 rating points",
                 "M100", "M0", "U100", "U0"):
        assert term in prereg, term
    assert ag.DESIGN_TAG in prereg
    assert "Stage-5 ME / MA / UE / UA cells" in prereg


def test_prereg_records_the_settled_interpretations():
    with open(PREREG_PATH) as handle:
        prereg = handle.read()
    # §12 freeze record: the settled points stay visible in the frozen prereg
    assert "## 12. Freeze checklist and record" in prereg
    assert "cluster_of" in prereg                 # §7 skeleton key
    assert "meta.case" in prereg
    assert "15 clusters" in prereg                # 10 legal + 5 latent problems
    assert "strictly literal" in prereg           # §8 classifier order
    assert "75" in prereg                         # §3 scope
    assert "(4, 14, 24)" in prereg                # §5 resolved layers
    assert "recipients are exactly the two policy-0 cells" in prereg
    # header flipped from draft to frozen
    assert "FROZEN DESIGN" in prereg
    assert "DRAFT ONLY" not in prereg


def test_bridge_cross_check_documents_the_frozen_g23c_reference():
    # §12: the G24B bridge is cross-checked against the frozen G23C bridge.
    with open(PREREG_PATH) as handle:
        prereg = handle.read()
    assert "g23c_bridge_analysis.json" in prereg
    assert "cross-check" in prereg
