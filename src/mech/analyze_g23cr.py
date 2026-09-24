"""G23C-R frozen analyzer — joint fresh-material replication of G23C + G24B.

Implements `preregistrations/PREREGISTRATION_G23C_R_FRESH_REPLICATION.md`
verbatim: the §8 Phase-1 bridge (parent gates, code-shared), the §9 union of
frozen parent interventions (10 unique scientific patches + 4-cell identity),
the §10 inference (seed 20260924, 10,000 percentile cluster resamples over
the G18 frozen `meta["skeleton"]`), the §11 G23C replication classifier, the
§12 G24B replication classifier, the §13 overall four-outcome verdict, the
§14 interpretation discipline and the §5 tokenizer-audit position gate.

Stdlib only: the same module imports in the test environment (no torch) and on
the run host.  The runner `g23cr_fresh_replication.py` imports the frozen
constants from here so there is exactly one copy of them.

Parent machinery is imported, never re-implemented — this is how §16's
"parent scientific gates must not drift" holds by construction:

- from `analyze_g23c`: cells, floors, model ids, `summarise`/`_bundle`/
  `pass_gate`/`pooled_gate`, `bridge_quantities`/`bridge_stats`,
  `switch_quantity`/`estimands_from_switches`, the parent G23C `classify`,
  `_identity_check`, `_bridge_section`, `_fmt`, `_warn_drops`;
- from `analyze_g24b`: the 8-cell donor x recipient grid, `donor_quantities`,
  the parent G24B `classify`, and the frozen seed 20260924.

Settled before the design freeze (prereg §16 / this docstring):
- materials: exactly the 70 G18 `legal_judgment` + `evidence_inference`
  items from `data/items/g18_v1.jsonl` (40/30, 20 frozen skeletons),
  `ranking_selection` excluded; cluster key = frozen `meta["skeleton"]`;
  items enter exhaustively, never selected on any effect or model output;
- previews: byte-for-byte `meta["previews"]["para"]` (M) and
  `meta["previews"]["unrel"]` (U); no new paraphrase/filler/repair;
- the 10 unique scientific patches are exactly the 8-cell G24B grid plus
  `ME -> MA` and `UE -> UA` (the two G23C 0->100 directions); identity for
  all 4 cells x 3 layers, with `ME -> ME` / `UE -> UE` reused from the grid
  as §9.3 permits;
- sub-classifiers call the parent `classify` functions with `bridge_pass=True`
  (the bridge is the overall §13 stop rule) and map parent outcome names to
  the prereg `g23c-*` / `g24b-*` names; descriptive licensed texts are the
  parent LICENSED entries verbatim (no new claim language);
- only `g23c-replicated` (parent: `target-conditioned-policy-state`) and
  `g24b-replicated` (parent: `donor-conditioned-policy-state`) count toward
  the overall verdict, exactly as §11/§12 state;
- §5 position gate: per (item, model) pair the absolute M-vs-U `rule_end`
  position difference is the max over both policy values (0% and 100% — the
  conservative reading); the design stops before compute when strictly more
  than 5% of pairs exceed 4 tokens; checks 1-6 are absolute;
- §13 decision order: bridge-failed -> jointly-replicated ->
  partial-replication -> not-replicated; no outcome launches another round.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

# ------------------------------------------------------- frozen parent parts
from analyze_g23c import (  # noqa: E402
    ROOT, CELLS, CELL_TABLE, FAMILIES, MODELS, MODEL_IDS, DIRECTIONS,
    PRIMARY_LAYER, CONTROL_LAYERS, FLOOR, BRIDGE_FLOOR, IDENTITY_TOL,
    N_RESAMPLES, MIN_MODELS_POSITIVE,  # noqa: F401
    frozen_layers, nearest_layer_24, load_frozen_meta,  # noqa: F401
    summarise as _summarise, pooled_gate, pass_gate,  # noqa: F401
    bridge_quantities, bridge_stats, switch_quantity,
    estimands_from_switches, _bundle, _fmt, _warn_drops,
    _identity_check, _bridge_section, classify as g23c_parent_classify,
    LICENSED as G23C_PARENT_LICENSED, VERDICTS as G23C_PARENT_VERDICTS,
)
from analyze_g24b import (  # noqa: E402
    PATCHES as GRID8, DONORS, RECIPIENTS, donor_quantities,
    classify as g24b_parent_classify, LICENSED as G24B_PARENT_LICENSED,
    VERDICTS as G24B_PARENT_VERDICTS, G24B_SEED,
)

# ------------------------------------------------------------------ §16 spec
DESIGN_TAG = "g23c-r-fresh-joint-replication-design-v1"
SEED = G24B_SEED                      # §10: 20260924
G23CR_LAYERS = (4, 14, 24)            # §7: no layer search
SITE = "rule_end"                     # §7: single site

ITEMS_PATH = os.path.join(ROOT, "data", "items", "g18_v1.jsonl")

# §9.3: 8-cell grid + the two G23C 0->100 directions = 10 unique patches.
SCIENTIFIC = tuple(GRID8) + ("ME_to_MA", "UE_to_UA")

# §9.1: parent G23C switch direction -> union patch name.
DIR2PATCH = {"M_100to0": "MA_to_ME", "M_0to100": "ME_to_MA",
             "U_100to0": "UA_to_UE", "U_0to100": "UE_to_UA"}

# §5: tokenizer/site audit position gate.
POSITION_TOL_TOKENS = 4
POSITION_GATE_FRAC = 0.05

# §11 / §12: parent outcome name -> replication-round name.  Only the two
# `*-replicated` names count toward the overall verdict.
MAP_G23C = {"target-conditioned-policy-state": "g23c-replicated",
            "generic-policy-state": "g23c-generic-policy-state",
            "target-readiness-only": "g23c-target-readiness-only",
            "unresolved": "g23c-unresolved"}
MAP_G24B = {"donor-conditioned-policy-state": "g24b-replicated",
            "donor-generic-policy-state": "g24b-donor-generic-policy-state",
            "no-donor-policy-state": "g24b-no-donor-policy-state",
            "unresolved": "g24b-unresolved"}

# §11 / §12 / §13 / §14 licensed statements (verbatim from the prereg).
LICENSED_G23C_REP = (
    "On a disjoint frozen material set, the causal efficacy of the rule-time "
    "zero-vs-full policy state is again stronger when the target proposition "
    "is available during policy processing.")
LICENSED_G24B_REP = (
    "On a disjoint frozen material set and with the recipient prompt held "
    "fixed, matched-target donor states again carry a larger causally "
    "transportable zero-versus-full policy effect than unrelated-target "
    "donor states.")
LICENSED_JOINT = (
    "The RQ3 mechanism replicates on a material set frozen independently of "
    "the discovery set: target availability during policy processing "
    "modulates both the causal efficacy and the donor-side policy content of "
    "the rule-time state.")
LICENSED_PARTIAL = "Exactly one parent headline replicates."
LICENSED_NOT_REPL = ("Neither parent headline replicates despite a passing "
                     "bridge.")
LICENSED_BRIDGE_FAILED = ("VERDICT = bridge-failed. STOP BEFORE ALL PATCHING.")
JOINT_INTERPRETATION = (
    "target availability during policy processing changes the causally "
    "transportable policy information available at the rule-time state, and "
    "this property reproduces on disjoint materials.")

OVERALL_LICENSED = {"jointly-replicated": LICENSED_JOINT,
                    "partial-replication": LICENSED_PARTIAL,
                    "not-replicated": LICENSED_NOT_REPL,
                    "bridge-failed": LICENSED_BRIDGE_FAILED}

OVERALL_VERDICTS = ("jointly-replicated", "partial-replication",
                    "not-replicated", "bridge-failed")


def summarise(pairs, seed=SEED):
    """Parent percentile cluster bootstrap, with this round's frozen seed."""
    return _summarise(pairs, seed=seed)


# ---------------------------------------------------------------- §3 materials
def g18_meta() -> dict:
    """item_id -> {cluster, family, s} for the 70 in-scope G18 items.

    `cluster` is the frozen G18 `meta["skeleton"]` (prereg §3 / §10); the two
    preregistered families only; every item enters exhaustively.
    """
    out = {}
    with open(ITEMS_PATH) as handle:
        for line in handle:
            if not line.strip():
                continue
            r = json.loads(line)
            if r["task_family"] not in FAMILIES:
                continue
            out[r["item_id"]] = {
                "cluster": r["meta"]["skeleton"],
                "family": r["task_family"],
                "s": 1.0 if r["critical_direction"] == "increase" else -1.0,
            }
    return out


def load_g18_items():
    """The same 70 items as schema.Item objects (runner cell construction)."""
    from schema import load_items
    keep = set(g18_meta())
    return [i for i in load_items(ITEMS_PATH) if i.item_id in keep]


# ------------------------------------------------------------- §5 audit gate
def _first_last_diff(a, b):
    """(first_diff_index, a_end_of_divergence, b_end_of_divergence).

    Divergence occupies [p, len(a)-s) in a and [p, len(b)-s) in b where s is
    the common suffix length (both counted from the end).
    """
    n = min(len(a), len(b))
    p = 0
    while p < n and a[p] == b[p]:
        p += 1
    s = 0
    while s < n - p and a[len(a) - 1 - s] == b[len(b) - 1 - s]:
        s += 1
    return p, len(a) - s, len(b) - s


def diff_within(ids_a, ids_b, lo, hi) -> bool:
    """True iff the two token sequences differ only inside [lo, hi)."""
    p, ea, eb = _first_last_diff(ids_a, ids_b)
    return p >= lo and ea <= hi and eb <= hi


def position_gate(pair_diffs) -> dict:
    """§5: the design stops before compute when strictly more than 5% of
    item/model pairs have an absolute M-vs-U `rule_end` difference > 4 tokens.

    `pair_diffs` maps a pair key to its absolute difference (tokens).
    """
    n = len(pair_diffs)
    over = [k for k, d in pair_diffs.items() if d > POSITION_TOL_TOKENS]
    frac = (len(over) / n) if n else 0.0
    return {"n_pairs": n, "n_over": len(over), "frac_over": frac,
            "tol_tokens": POSITION_TOL_TOKENS,
            "max_frac": POSITION_GATE_FRAC, "over": sorted(over),
            "passed": bool(n) and frac <= POSITION_GATE_FRAC}


# ---------------------------------------------------------------- completeness
def _complete_y(rec) -> bool:
    return all(isinstance(rec.get("y", {}).get(c), (int, float))
               for c in CELLS)


def _complete_scientific(rec, layers) -> bool:
    p = rec.get("patch", {})
    return all(isinstance(p.get(n, {}).get(str(L)), (int, float))
               for n in SCIENTIFIC for L in layers)


def _complete_identity(rec, layers) -> bool:
    i = rec.get("identity", {})
    return all(isinstance(i.get(str(L), {}).get(c), (int, float))
               for L in layers for c in CELLS)


def gather(paths: dict, meta: dict, phase: str):
    """-> (rows, drops, layers); mirrors the parent `gather`s over this
    round's 10-patch union, its design tag and the G18 item set."""
    rows, drops = {}, {}
    layers_seen = set()
    for tag, path in paths.items():
        if not os.path.exists(path):
            raise SystemExit(f"missing {tag} file: {path}")
        d = json.load(open(path))
        design = d.get("design", {})
        want = frozen_layers(design["n_layers"])
        if tuple(design.get("layers", ())) != want \
                or design.get("primary") != PRIMARY_LAYER \
                or tuple(design.get("controls") or ()) != (CONTROL_LAYERS[0],
                                                           want[2]) \
                or design.get("design_tag") != DESIGN_TAG:
            raise SystemExit(
                f"{tag}: design layer block {design.get('layers')} / "
                f"primary={design.get('primary')} / controls="
                f"{design.get('controls')} / design_tag="
                f"{design.get('design_tag')} does not match the frozen "
                f"configuration {want} (primary {PRIMARY_LAYER}) — refusing "
                "to analyze.")
        layers_seen.add(want)
        drops[tag] = {"missing_item": 0, "unknown_item": 0, "incomplete": 0}
        by_id = {r["item_id"]: r for r in d["records"]}
        rows[tag] = []
        for iid in meta:
            rec = by_id.get(iid)
            if rec is None:
                drops[tag]["missing_item"] += 1
                continue
            need = _complete_y(rec) and (
                phase == "bridge"
                or (_complete_scientific(rec, want)
                    and _complete_identity(rec, want)))
            if not need:
                drops[tag]["incomplete"] += 1
                continue
            rows[tag].append((iid, rec))
        for iid in by_id:
            if iid not in meta:
                drops[tag]["unknown_item"] += 1
    if len(layers_seen) != 1:
        raise SystemExit(f"models disagree on frozen layers: {layers_seen}")
    return rows, drops, layers_seen.pop()


# --------------------------------------------------------------- §11/§12 maps
def map_g23c(parent_verdict: str) -> str:
    return MAP_G23C[parent_verdict]


def map_g24b(parent_verdict: str) -> str:
    return MAP_G24B[parent_verdict]


def licensed_g23c(sub_name: str, parent_verdict: str) -> str:
    """§11: the replication statement when replicated, else the parent text."""
    if sub_name == "g23c-replicated":
        return LICENSED_G23C_REP
    return G23C_PARENT_LICENSED[parent_verdict]


def licensed_g24b(sub_name: str, parent_verdict: str) -> str:
    if sub_name == "g24b-replicated":
        return LICENSED_G24B_REP
    return G24B_PARENT_LICENSED[parent_verdict]


# -------------------------------------------------------------------- phases
def phase_bridge(meta, paths=None):
    paths = paths or {t: os.path.join(ROOT, "results", "mech",
                                      f"g23cr_bridge_{t}.json")
                      for t in MODELS}
    rows, drops, layers = gather(paths, meta, phase="bridge")
    bridge = bridge_stats(rows, meta)
    passed = bool(bridge["gates"]["passed"])
    return {"design": {"seed": SEED, "resamples": N_RESAMPLES,
                       "floor": FLOOR, "bridge_floor": BRIDGE_FLOOR,
                       "n_items_expected": len(meta),
                       "n_complete": {t: len(rows.get(t, []))
                                      for t in MODELS},
                       "n_clusters": len({m["cluster"]
                                          for m in meta.values()})},
            "design_tag": DESIGN_TAG,
            "pooled": {k: bridge[k]["pooled"] for k in
                       ("policy_effect_m", "policy_effect_u",
                        "target_policy_interaction")},
            "per_model": {t: {k: bridge[k]["per_model"][t] for k in
                              ("policy_effect_m", "policy_effect_u",
                               "target_policy_interaction")}
                          for t in bridge["policy_effect_m"]["per_model"]},
            "gates": bridge["gates"],
            "drops": drops,
            "verdict": None if passed else "bridge-failed",
            "licensed": None if passed else OVERALL_LICENSED["bridge-failed"]}


def _controls_tc(layer_reports, layers):
    """§11.3: the parent G23C control clause, both frozen layers."""
    tc14 = layer_reports[str(PRIMARY_LAYER)]["target_conditioning"]
    tc14_mean = tc14["pooled"]["mean"]
    controls = {"layers": {}, "passed": True}
    for L in (layers[0], layers[2]):
        tcl = layer_reports[str(L)]["target_conditioning"]
        absent = not tcl["pass"]
        weaker = (tc14_mean == tc14_mean
                  and tcl["pooled"]["mean"] == tcl["pooled"]["mean"]
                  and (tc14_mean - tcl["pooled"]["mean"]) >= FLOOR)
        ok = bool(absent or weaker)
        controls["layers"][str(L)] = {
            "tc_mean": tcl["pooled"]["mean"], "tc_pass": tcl["pass"],
            "pattern_absent": bool(absent),
            "weaker_by_at_least_floor": bool(weaker), "ok": ok}
        controls["passed"] = bool(controls["passed"] and ok)
    return controls


def _controls_dti(layer_reports, layers):
    """§12.3: the parent G24B control clause, both frozen layers."""
    dti14 = layer_reports[str(PRIMARY_LAYER)]["dti"]
    dti14_mean = dti14["pooled"]["mean"]
    controls = {"layers": {}, "passed": True}
    for cl in (CONTROL_LAYERS[0], layers[2]):
        cb = layer_reports[str(cl)]["dti"]
        absent = not cb["pass"]
        weaker = (dti14_mean == dti14_mean
                  and cb["pooled"]["mean"] == cb["pooled"]["mean"]
                  and (dti14_mean - cb["pooled"]["mean"]) >= FLOOR)
        ok = bool(absent or weaker)
        controls["layers"][str(cl)] = {
            "dti_pass": cb["pass"], "absent": bool(absent),
            "weaker_by_floor": bool(weaker), "ok": ok,
            "dti_mean": cb["pooled"]["mean"]}
        controls["passed"] = bool(controls["passed"] and ok)
    return controls


def phase_full(meta, paths=None):
    paths = paths or {t: os.path.join(ROOT, "results", "mech",
                                      f"g23cr_patch_{t}.json")
                      for t in MODELS}
    rows, drops, layers = gather(paths, meta, phase="full")
    # §11.4/§12.4: identity is an implementation check; a violation raises so
    # no verdict ever prints from a broken patcher.
    identity = _identity_check(rows, layers)
    bridge = bridge_stats(rows, meta)

    design = {"seed": SEED, "resamples": N_RESAMPLES, "floor": FLOOR,
              "bridge_floor": BRIDGE_FLOOR,
              "identity_tolerance": IDENTITY_TOL,
              "layers": list(layers), "primary": PRIMARY_LAYER,
              "controls": [CONTROL_LAYERS[0], layers[2]],
              "n_items_expected": len(meta),
              "n_complete": {t: len(rows.get(t, [])) for t in MODELS},
              "n_clusters": len({m["cluster"] for m in meta.values()})}

    # §13.1: bridge failure ends the round before any parent statistic.
    if not bridge["gates"]["passed"]:
        return {"design": design, "design_tag": DESIGN_TAG,
                "identity": identity, "bridge": _bridge_section(bridge),
                "g23c_sub_verdict": None, "g24b_sub_verdict": None,
                "g23c_licensed": None, "g24b_licensed": None,
                "joint_interpretation": None,
                "layers": None, "controls_g23c": None,
                "controls_g24b": None, "drops": drops,
                "verdict": "bridge-failed",
                "licensed": OVERALL_LICENSED["bridge-failed"]}

    # §9: both parent estimand families from the same records, per layer.
    layer_reports = {}
    for L in layers:
        sw = {d: {t: [] for t in rows} for d in DIRECTIONS}
        ptm, ptu, tc = ({t: [] for t in rows} for _ in range(3))
        keys = ("donor_policy_m", "donor_policy_u", "dti",
                "dti_ME", "dti_UE")
        dq = {k: {t: [] for t in rows} for k in keys}
        cells = {n: {t: [] for t in rows} for n in SCIENTIFIC}
        for tag, recs in rows.items():
            for iid, rec in recs:
                cluster, s = meta[iid]["cluster"], meta[iid]["s"]
                # §9.1 G23C switches (parent formulas, raw readouts)
                per_dir = {d: switch_quantity(d, s, rec["y"],
                                              rec["patch"][DIR2PATCH[d]]
                                              [str(L)])
                           for d in DIRECTIONS}
                m, u, t = estimands_from_switches(per_dir)
                for d in DIRECTIONS:
                    sw[d][tag].append((cluster, per_dir[d]))
                ptm[tag].append((cluster, m))
                ptu[tag].append((cluster, u))
                tc[tag].append((cluster, t))
                # §9.2 G24B donor grid (parent formulas, aligned readouts)
                py = {n: s * rec["patch"][n][str(L)] for n in GRID8}
                q = donor_quantities(py, str(L))
                for k in keys:
                    dq[k][tag].append((cluster, q[k]))
                for n in SCIENTIFIC:
                    cells[n][tag].append((cluster, s * rec["patch"][n]
                                          [str(L)]))
        layer_reports[str(L)] = {
            "switches": {d: _bundle(sw[d]) for d in DIRECTIONS},
            "policy_transfer_m": _bundle(ptm, FLOOR),
            "policy_transfer_u": _bundle(ptu, FLOOR),
            "target_conditioning": _bundle(tc, FLOOR),
            "donor_policy_m": _bundle(dq["donor_policy_m"], FLOOR),
            "donor_policy_u": _bundle(dq["donor_policy_u"], FLOOR),
            "dti": _bundle(dq["dti"], FLOOR),
            "dti_ME": _bundle(dq["dti_ME"]),
            "dti_UE": _bundle(dq["dti_UE"]),
            "patches": {n: _bundle(cells[n]) for n in SCIENTIFIC},
        }

    primary = layer_reports[str(PRIMARY_LAYER)]
    ptm_pass = primary["policy_transfer_m"]["pass"]
    ptu_pass = primary["policy_transfer_u"]["pass"]
    tc_pass = primary["target_conditioning"]["pass"]
    dpm_pass = primary["donor_policy_m"]["pass"]
    dpu_pass = primary["donor_policy_u"]["pass"]
    dti_pass = primary["dti"]["pass"]

    controls_g23c = _controls_tc(layer_reports, layers)
    controls_g24b = _controls_dti(layer_reports, layers)

    # §11 / §12: parent classifiers, bridge handled by the overall §13 rule.
    p23c = g23c_parent_classify(True, ptm_pass, ptu_pass, tc_pass,
                                controls_g23c["passed"])
    p24b = g24b_parent_classify(True, dpm_pass, dpu_pass, dti_pass,
                                controls_g24b["passed"])
    sub23c, sub24b = map_g23c(p23c), map_g24b(p24b)
    repl23c = sub23c == "g23c-replicated"
    repl24b = sub24b == "g24b-replicated"

    # §13 overall decision order.
    if repl23c and repl24b:
        verdict = "jointly-replicated"
    elif repl23c or repl24b:
        verdict = "partial-replication"
    else:
        verdict = "not-replicated"

    return {"design": design, "design_tag": DESIGN_TAG,
            "identity": identity, "bridge": _bridge_section(bridge),
            "layers": layer_reports,
            "controls_g23c": controls_g23c,
            "controls_g24b": controls_g24b,
            "gates_g23c": {"policy_transfer_m_pass": ptm_pass,
                           "policy_transfer_u_pass": ptu_pass,
                           "target_conditioning_pass": tc_pass},
            "gates_g24b": {"donor_policy_m_pass": dpm_pass,
                           "donor_policy_u_pass": dpu_pass,
                           "dti_pass": dti_pass},
            "g23c_sub_verdict": sub23c, "g24b_sub_verdict": sub24b,
            "g23c_replicated": repl23c, "g24b_replicated": repl24b,
            "g23c_licensed": licensed_g23c(sub23c, p23c),
            "g24b_licensed": licensed_g24b(sub24b, p24b),
            "joint_interpretation": (JOINT_INTERPRETATION
                                     if verdict == "jointly-replicated"
                                     else None),
            "drops": drops, "verdict": verdict,
            "licensed": OVERALL_LICENSED[verdict]}


# ------------------------------------------------------------------- report
def print_bridge(rep):
    d = rep["design"]
    print("G23C-R — Phase 1 bridge (direct readout, 70 G18 items, no hooks)")
    print(f"  seed {d['seed']}, {d['resamples']} cluster resamples, "
          f"bridge floor {d['bridge_floor']}, complete {d['n_complete']} "
          f"of {d['n_items_expected']} (expected per model), "
          f"clusters {d['n_clusters']}")
    print("  cells: ME=M0  MA=M100  UE=U0  UA=U100 (G18 para/unrel previews)")
    for t in MODELS:
        pm = rep["per_model"][t]
        print(f"  {t:<20} PolicyEffect_M  {_fmt(pm['policy_effect_m'])}")
        print(f"  {'':<20} PolicyEffect_U  {_fmt(pm['policy_effect_u'])}")
        print(f"  {'':<20} TargetPolicyInt {_fmt(pm['target_policy_interaction'])}")
    print(f"  POOLED PolicyEffect_M  {_fmt(rep['pooled']['policy_effect_m'])}")
    print(f"  POOLED TargetPolicyInt {_fmt(rep['pooled']['target_policy_interaction'])}")
    g = rep["gates"]
    print(f"  gate1 pooled PolicyEffect_M >= {d['bridge_floor']} & CI low > 0 : {g['gate1_pooled_policy_effect_m']}")
    print(f"  gate2 pooled TargetPolicyInteraction >= {d['bridge_floor']} & CI low > 0 : {g['gate2_pooled_target_policy_interaction']}")
    print(f"  gate3 positive model means in 2/2 (both quantities) : {g['gate3_positive_model_means_2_of_2']}")
    _warn_drops(rep["drops"])
    print("BRIDGE: PASS — proceed to Phase 2 joint patching"
          if g["passed"] else
          "BRIDGE: FAIL — STOP BEFORE ALL PATCHING (verdict bridge-failed)")
    if not g["passed"]:
        print(f"LICENSED: {rep['licensed']}")


def print_full(rep):
    d = rep["design"]
    print("G23C-R — joint fresh-material replication (G23C + G24B)")
    print(f"  layers {d['layers']} (primary L{d['primary']}, controls "
          f"L{d['controls'][0]}/L{d['controls'][1]}), site {SITE}, seed "
          f"{d['seed']}, {d['resamples']} resamples, floor {d['floor']}, "
          f"identity tol {d['identity_tolerance']}")
    print(f"  complete per model: {d['n_complete']} of "
          f"{d['n_items_expected']}, clusters {d['n_clusters']}")
    idr = rep["identity"]
    print(f"  identity patch: max |delta| {idr['max_abs_delta']:.4f} <= "
          f"{idr['tolerance']} over {idr['n_checked']} checks")
    print(f"  bridge gates: {rep['bridge']['gates']}")
    _warn_drops(rep["drops"])
    if rep["layers"] is None:
        print("stop rule: bridge failed — no parent statistic computed")
        print(f"VERDICT: {rep['verdict']}")
        print(f"LICENSED: {rep['licensed']}")
        return
    for L in d["layers"]:
        e = rep["layers"][str(L)]
        tag = "PRIMARY" if L == d["primary"] else "control"
        print(f"  --- L{L} ({tag})")
        for name in ("policy_transfer_m", "policy_transfer_u",
                     "target_conditioning", "donor_policy_m",
                     "donor_policy_u", "dti", "dti_ME", "dti_UE"):
            b = e[name]
            p = b.get("pass")
            print(f"      {name:<22} {_fmt(b['pooled'])} "
                  f"pass={p if p is not None else '-'}")
    print(f"  controls G23C (§11.3): {rep['controls_g23c']}")
    print(f"  controls G24B (§12.3): {rep['controls_g24b']}")
    print(f"  G23C sub-verdict: {rep['g23c_sub_verdict']} "
          f"(replicated={rep['g23c_replicated']})")
    print(f"  G24B sub-verdict: {rep['g24b_sub_verdict']} "
          f"(replicated={rep['g24b_replicated']})")
    print(f"VERDICT: {rep['verdict']}")
    print(f"LICENSED (overall): {rep['licensed']}")
    print(f"LICENSED (G23C): {rep['g23c_licensed']}")
    print(f"LICENSED (G24B): {rep['g24b_licensed']}")
    if rep.get("joint_interpretation"):
        print(f"INTERPRETATION (§14): {rep['joint_interpretation']}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", choices=["bridge", "full"], required=True)
    args = ap.parse_args()

    meta = g18_meta()
    if args.phase == "bridge":
        rep = phase_bridge(meta)
        print_bridge(rep)
        out = os.path.join(ROOT, "results", "mech",
                           "g23cr_bridge_analysis.json")
    else:
        rep = phase_full(meta)
        print_full(rep)
        out = os.path.join(ROOT, "results", "mech", "g23cr_analysis.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(rep, open(out, "w"), indent=1)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
