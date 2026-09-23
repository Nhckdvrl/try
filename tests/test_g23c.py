"""G23C design tests — nothing here touches a model.

Loads only the stdlib-only frozen analyzer (`src/mech/analyze_g23c.py`); the
runner is checked as source text.  Covers prereg §11.4's mandatory list —
sign conventions, identity patch, pooled skeleton clustering, fixed layers and
the §4/§8 stop rule — plus the §3 cell table, the three §4 bridge gates, all
five §8 verdicts end to end on synthetic records, drop accounting, the frozen
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
    "analyze_g23c", os.path.join(ROOT, "src/mech/analyze_g23c.py"))
ag = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ag)

PREREG_PATH = os.path.join(
    ROOT, "preregistrations/PREREGISTRATION_G23C_TARGET_CONDITIONED_POLICY_STATE.md")
RUNNER_PATH = os.path.join(ROOT, "src/mech/g23c_policy_state.py")
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


def _patched(direction, s, y, v):
    """Inverse of ag.switch_quantity: recipient output achieving switch v."""
    if direction == "M_100to0":
        return y["ME"] + v * s
    if direction == "M_0to100":
        return y["MA"] - v * s
    if direction == "U_100to0":
        return y["UE"] + v * s
    if direction == "U_0to100":
        return y["UA"] - v * s
    raise ValueError(direction)


def _design(phase, n_items, n_layers=36):
    Ls = list(ag.frozen_layers(n_layers))
    return {"design_tag": ag.DESIGN_TAG, "model": "m", "tag": "t",
            "phase": phase, "n_layers": n_layers, "layers": Ls,
            "primary": ag.PRIMARY_LAYER, "controls": [ag.CONTROL_LAYERS[0],
                                                      Ls[2]],
            "sites": ["rule_end"], "n_items": n_items,
            "identity_tol": ag.IDENTITY_TOL, "families": list(ag.FAMILIES),
            "seed": ag.SEED}


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


GOLD_L14 = {"M_100to0": 10.0, "M_0to100": 10.0,
            "U_100to0": 0.0, "U_0to100": 0.0}
CTRL_ZERO = {d: 0.0 for d in ag.DIRECTIONS}


def _patch_obj(meta, l14=GOLD_L14, ctrl=CTRL_ZERO, pe_m=20.0, pe_u=10.0,
               identity_off=0.0):
    targets = {4: ctrl, 14: l14, 24: ctrl}
    records = []
    for iid, m in meta.items():
        s = m["s"]
        y = _y(s, pe_m, pe_u)
        records.append({
            "item_id": iid, "direction": "increase" if s > 0 else "decrease",
            "y": y, "n_tok": {c: 0 for c in ag.CELLS},
            "patch": {d: {str(L): _patched(d, s, y, targets[L][d])
                          for L in LAYERS}
                      for d in ag.DIRECTIONS},
            "identity": {str(L): {c: y[c] + identity_off for c in ag.CELLS}
                         for L in LAYERS}})
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
# Scope, constants, cell table
# ---------------------------------------------------------------------------
def test_scope_is_the_75_stage5_items():
    meta = ag.load_frozen_meta()
    assert len(meta) == 75
    assert Counter(m["family"] for m in meta.values()) == {
        "legal_judgment": 45, "evidence_inference": 30}
    assert Counter(m["s"] for m in meta.values()) == {1.0: 40, -1.0: 35}
    # §7 skeleton key: repository-standard cluster_of → 15 clusters
    # (10 legal cases + 5 evidence latent problems)
    assert len({m["cluster"] for m in meta.values()}) == 15
    for m in meta.values():
        assert m["cluster"].startswith("legal:") or \
            m["cluster"].startswith("evidence_inference:")


def test_constants_are_frozen():
    assert ag.FLOOR == 3.0
    assert ag.BRIDGE_FLOOR == 5.0
    assert ag.IDENTITY_TOL == 0.5
    assert ag.SEED == 20260923
    assert ag.N_RESAMPLES == 10_000
    assert ag.PRIMARY_LAYER == 14
    assert ag.CONTROL_LAYERS == (4, 24)
    assert ag.MIN_MODELS_POSITIVE == 2
    assert ag.DESIGN_TAG == "g23c-target-conditioned-policy-state-design-v1"
    assert ag.MODELS == ("qwen3-8b", "mistral-small-24b")
    assert set(ag.MODEL_IDS) == set(ag.MODELS)


def test_cell_table_is_the_stage5_2x2_and_directions_match_section_6():
    # §3: ME=M0, MA=M100, UE=U0, UA=U100
    assert ag.CELLS == ("ME", "MA", "UE", "UA")
    assert ag.CELL_TABLE == {"ME": ("match", False), "MA": ("match", True),
                             "UE": ("unrel", False), "UA": ("unrel", True)}
    # §6 donor -> recipient
    assert ag.DIRECTIONS == {"M_100to0": ("MA", "ME"),
                             "M_0to100": ("ME", "MA"),
                             "U_100to0": ("UA", "UE"),
                             "U_0to100": ("UE", "UA")}


def test_frozen_layers_no_layer_search():
    assert ag.frozen_layers(36) == (4, 14, 24)      # Qwen3-8B
    assert ag.frozen_layers(40) == (4, 14, 24)      # Mistral-Small-24B
    assert ag.frozen_layers(20) == (4, 14, 19)      # nearest valid < 25 layers
    assert ag.nearest_layer_24(24) == 23
    assert ag.nearest_layer_24(25) == 24


def test_phase_file_naming():
    assert ag.bridge_path("qwen3-8b").endswith(
        "results/mech/g23c_bridge_qwen3-8b.json")
    assert ag.patch_path("mistral-small-24b").endswith(
        "results/mech/g23c_patch_mistral-small-24b.json")


# ---------------------------------------------------------------------------
# §4 bridge estimands and gates
# ---------------------------------------------------------------------------
def test_bridge_quantities_sign_aligned_formulas():
    y_inc = {"ME": 50.0, "MA": 70.0, "UE": 50.0, "UA": 60.0}
    assert ag.bridge_quantities(+1.0, y_inc) == (20.0, 10.0, 10.0)
    # s = -1 with evidence lowering the judgment: MA < ME, UA < UE
    y_dec = {"ME": 50.0, "MA": 30.0, "UE": 50.0, "UA": 40.0}
    assert ag.bridge_quantities(-1.0, y_dec) == (20.0, 10.0, 10.0)
    # TargetPolicyInteraction is a difference of the two aligned effects
    pe_m, pe_u, tpi = ag.bridge_quantities(+1.0, {"ME": 50, "MA": 65,
                                                  "UE": 50, "UA": 50})
    assert tpi == pe_m - pe_u == 15.0


def test_bridge_gate_all_three_pass_and_each_can_fail(tmp_path):
    meta = _meta()
    rep = ag.phase_bridge(meta, _bridge_paths(tmp_path, meta))
    g = rep["gates"]
    assert g == {"gate1_pooled_policy_effect_m": True,
                 "gate2_pooled_target_policy_interaction": True,
                 "gate3_positive_model_means_2_of_2": True, "passed": True}
    assert rep["verdict"] is None

    # gate 1 alone fails: pooled PolicyEffect_M below the 5.0 floor (TPI ok)
    rep1 = ag.phase_bridge(meta, _bridge_paths(tmp_path, meta,
                                               pe_m=4.0, pe_u=-6.0))
    g1 = rep1["gates"]
    assert g1["gate1_pooled_policy_effect_m"] is False
    assert g1["gate2_pooled_target_policy_interaction"] is True   # tpi = 10
    assert g1["gate3_positive_model_means_2_of_2"] is True
    assert g1["passed"] is False
    assert rep1["verdict"] == "bridge-failed"
    assert rep1["licensed"] == ag.LICENSED["bridge-failed"]

    # gate 2 alone fails: TPI below the floor (PolicyEffect_M ok)
    rep2 = ag.phase_bridge(meta, _bridge_paths(tmp_path, meta,
                                               pe_m=20.0, pe_u=16.0))
    g2 = rep2["gates"]
    assert g2["gate1_pooled_policy_effect_m"] is True
    assert g2["gate2_pooled_target_policy_interaction"] is False  # tpi = 4
    assert g2["passed"] is False

    # gate 3 alone fails: one model's mean not positive while the pooled
    # means and intervals still clear the floor
    rep3 = ag.phase_bridge(
        meta,
        _bridge_paths(tmp_path, meta,
                      pe_m_by_model={"qwen3-8b": 30.0,
                                     "mistral-small-24b": -1.0},
                      pe_u_by_model={"qwen3-8b": 10.0,
                                     "mistral-small-24b": -7.0}))
    g3 = rep3["gates"]
    assert g3["gate1_pooled_policy_effect_m"] is True
    assert g3["gate2_pooled_target_policy_interaction"] is True
    assert g3["gate3_positive_model_means_2_of_2"] is False
    assert g3["passed"] is False

    # CI clause: mean clears the floor but a negative cluster drags CI low <= 0
    rep4 = ag.phase_bridge(meta, _bridge_paths(
        tmp_path, meta, pe_m_by_cluster={"c0": 40.0, "c1": -20.0},
        pe_u=0.0))
    pooled = rep4["pooled"]["policy_effect_m"]
    assert pooled["mean"] >= 5.0
    assert rep4["gates"]["gate1_pooled_policy_effect_m"] is False


def test_bridge_gate_never_preselects_by_behavioral_gap(tmp_path):
    # §4/§7: an item with a zero PolicyEffect gap stays in the analysis.
    meta = _meta()
    obj = _bridge_obj(meta, ag.MODELS[0])
    obj["records"][0]["y"] = _y(meta["i0"]["s"], pe_m=0.0, pe_u=0.0)
    paths = {t: _write(str(tmp_path / f"b_{t}.json"), obj if t == ag.MODELS[0]
                       else _bridge_obj(meta, t))
             for t in ag.MODELS}
    rep = ag.phase_bridge(meta, paths)
    assert rep["design"]["n_complete"] == {t: 6 for t in ag.MODELS}
    assert rep["pooled"]["policy_effect_m"]["n"] == 12   # 6 items x 2 models
    assert not hasattr(ag, "MIN_GAP")


# ---------------------------------------------------------------------------
# §6 switch sign conventions and transfer estimands
# ---------------------------------------------------------------------------
def test_switch_sign_conventions_toward_donor_is_positive():
    y = {"ME": 50.0, "MA": 70.0, "UE": 50.0, "UA": 60.0}     # s = +1
    # donor M100 (higher) into M0 recipient: y rises toward the donor
    assert ag.switch_quantity("M_100to0", +1.0, y, 60.0) == +10.0
    # donor M0 (lower) into M100 recipient: y falls toward the donor
    assert ag.switch_quantity("M_0to100", +1.0, y, 60.0) == +10.0
    assert ag.switch_quantity("U_100to0", +1.0, y, 55.0) == +5.0
    assert ag.switch_quantity("U_0to100", +1.0, y, 55.0) == +5.0
    # no movement -> zero in every direction
    assert ag.switch_quantity("M_100to0", +1.0, y, y["ME"]) == 0.0
    assert ag.switch_quantity("M_0to100", +1.0, y, y["MA"]) == 0.0
    # sign alignment flips the reading for decreasing evidence
    yd = {"ME": 50.0, "MA": 30.0, "UE": 50.0, "UA": 40.0}    # s = -1
    # donor M100 (lower) into M0: y falls toward the donor -> positive
    assert ag.switch_quantity("M_100to0", -1.0, yd, 40.0) == +10.0
    assert ag.switch_quantity("M_0to100", -1.0, yd, 40.0) == +10.0
    # moving away from the donor is negative
    assert ag.switch_quantity("M_100to0", +1.0, y, 40.0) == -10.0


def test_estimands_from_switches_mean_and_conditioning():
    sw = {"M_100to0": 8.0, "M_0to100": 12.0,
          "U_100to0": 3.0, "U_0to100": 5.0}
    pt_m, pt_u, tc = ag.estimands_from_switches(sw)
    assert pt_m == 10.0            # mean of the two M directions
    assert pt_u == 4.0
    assert tc == 6.0               # PT_M - PT_U
    zero = {d: 0.0 for d in ag.DIRECTIONS}
    assert ag.estimands_from_switches(zero) == (0.0, 0.0, 0.0)


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
    # both models observed items of skeleton c1 and c2 -> 4 obs, 2 clusters
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
    assert ag.classify(True, False, True, True, True) == "target-readiness-only"
    assert ag.classify(True, True, True, True, True) == \
        "target-conditioned-policy-state"
    assert ag.classify(True, True, True, False, True) == "generic-policy-state"
    assert ag.classify(True, True, False, False, True) == "unresolved"
    # strict literal: TC passes but the control clause fails -> unresolved
    assert ag.classify(True, True, True, True, False) == "unresolved"


def test_end_to_end_target_conditioned(tmp_path):
    meta = _meta()
    rep = ag.phase_full(meta, _patch_paths(tmp_path, meta))
    assert rep["bridge"]["gates"]["passed"] is True
    L14 = rep["layers"]["14"]
    assert L14["policy_transfer_m"]["pooled"]["mean"] == pytest.approx(10.0)
    assert L14["policy_transfer_u"]["pooled"]["mean"] == pytest.approx(0.0)
    assert L14["target_conditioning"]["pooled"]["mean"] == pytest.approx(10.0)
    assert L14["policy_transfer_m"]["pass"] is True
    assert L14["target_conditioning"]["pass"] is True
    # both directions reported separately before averaging (§9.5)
    assert L14["switches"]["M_100to0"]["pooled"]["mean"] == pytest.approx(10.0)
    assert L14["switches"]["M_0to100"]["pooled"]["mean"] == pytest.approx(10.0)
    assert rep["controls"]["passed"] is True
    assert rep["verdict"] == "target-conditioned-policy-state"
    assert rep["licensed"] == ag.LICENSED["target-conditioned-policy-state"]
    assert rep["design"]["n_complete"] == {t: 6 for t in ag.MODELS}
    assert rep["drops"] == {t: {"missing_item": 0, "unknown_item": 0,
                                "incomplete": 0} for t in ag.MODELS}


def test_end_to_end_generic_readiness_unresolved(tmp_path):
    meta = _meta()
    # generic: PT_M and PT_U both pass, TC does not
    both = {"M_100to0": 10.0, "M_0to100": 10.0,
            "U_100to0": 10.0, "U_0to100": 10.0}
    rep = ag.phase_full(meta, _patch_paths(tmp_path, meta, l14=both))
    assert rep["verdict"] == "generic-policy-state"
    assert rep["licensed"] == ag.LICENSED["generic-policy-state"]

    # readiness: bridge passes but PolicyTransfer_M does not
    none14 = {d: 0.0 for d in ag.DIRECTIONS}
    rep2 = ag.phase_full(meta, _patch_paths(tmp_path, meta, l14=none14))
    assert rep2["bridge"]["gates"]["passed"] is True
    assert rep2["layers"]["14"]["policy_transfer_m"]["pass"] is False
    assert rep2["verdict"] == "target-readiness-only"
    assert rep2["licensed"] == ag.LICENSED["target-readiness-only"]

    # unresolved: the TC pattern is equally present at the control layers
    ctrl_same = dict(GOLD_L14)
    rep3 = ag.phase_full(meta, _patch_paths(tmp_path, meta, l14=GOLD_L14,
                                            ctrl=ctrl_same))
    assert rep3["layers"]["14"]["target_conditioning"]["pass"] is True
    assert rep3["controls"]["passed"] is False
    assert rep3["verdict"] == "unresolved"

    # control clause satisfied by the "substantially weaker" arm: TC at a
    # control layer passes but trails L14 by >= one floor
    ctrl_weaker = {"M_100to0": 10.0, "M_0to100": 10.0,
                   "U_100to0": 3.0, "U_0to100": 3.0}     # TC = 7, gap = 3.0
    rep4 = ag.phase_full(meta, _patch_paths(tmp_path, meta, l14=GOLD_L14,
                                            ctrl=ctrl_weaker))
    assert rep4["controls"]["layers"]["4"]["tc_pass"] is True
    assert rep4["controls"]["layers"]["4"]["weaker_by_at_least_floor"] is True
    assert rep4["verdict"] == "target-conditioned-policy-state"

    # same shape but the gap is under the floor -> unresolved
    ctrl_near = {"M_100to0": 10.0, "M_0to100": 10.0,
                 "U_100to0": 2.0, "U_0to100": 2.0}       # TC = 8, gap = 2.0
    rep5 = ag.phase_full(meta, _patch_paths(tmp_path, meta, l14=GOLD_L14,
                                            ctrl=ctrl_near))
    assert rep5["controls"]["layers"]["4"]["tc_pass"] is True
    assert rep5["controls"]["layers"]["4"]["weaker_by_at_least_floor"] is False
    assert rep5["verdict"] == "unresolved"


def test_end_to_end_stop_rule_bridge_failure_blocks_transfer(tmp_path):
    # §4: the bridge is evaluated before any interchange statistic; on failure
    # the round stops and no transfer statistics are reported.
    meta = _meta()
    rep = ag.phase_full(meta, _patch_paths(tmp_path, meta,
                                           pe_m=0.0, pe_u=0.0))
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
                           "y": _y(1.0), "n_tok": {}, "patch": {}, "identity": {}})
    obj["records"][0]["patch"]["M_100to0"].pop("24")           # incomplete
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
    assert "from analyze_g23c import" in src      # one copy of the frozen spec
    # runtime §9.2 / §9.3 construction checks
    assert "ba[2] != bb[2]" in src
    assert "ba[1] != bb[1]" in src
    assert "not precede evidence" in src
    # §5/§6: frozen layers only, single site, four directions, identity
    assert '"--layer' not in src                  # no layer search CLI
    assert "frozen_layers(" in src
    assert "rule_end" in src
    assert "register_forward_hook" in src
    assert 'if args.phase == "patch":' in src
    assert "identity" in src
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
    for term in ("PolicyTransfer_M", "PolicyTransfer_U", "TargetConditioning",
                 "PolicyEffect_M", "PolicyEffect_U", "TargetPolicyInteraction",
                 "Switch_M_100to0", "Switch_M_0to100", "Switch_U_100to0",
                 "Switch_U_0to100", "rule_end", "layer 14",
                 "seed `20260923`", "10,000 percentile resamples",
                 "3.0 rating points", "M100 -> M0", "M0   -> M100"):
        assert term in prereg, term
    assert ag.DESIGN_TAG in prereg
    assert "Stage-5 ME / MA / UE / UA cells" in prereg


def test_prereg_records_the_settled_interpretations():
    with open(PREREG_PATH) as handle:
        prereg = handle.read()
    # §12 freeze record: the settled points stay visible in the frozen prereg
    assert "## 12. Freeze checklist and record" in prereg
    assert "0.5 rating points" in prereg          # §9.1 tolerance
    assert "cluster_of" in prereg                 # §7 skeleton key
    assert "meta.case" in prereg
    assert "15 clusters" in prereg                # 10 legal + 5 latent problems
    assert "strictly literal" in prereg           # §8 classifier order
    assert "75" in prereg                         # §3 scope
    assert "(4, 14, 24)" in prereg                # §5 resolved layers
    # header flipped from draft to frozen
    assert "FROZEN DESIGN" in prereg
    assert "DRAFT ONLY" not in prereg
