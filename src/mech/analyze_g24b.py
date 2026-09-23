"""G24B frozen analyzer — donor-state vs recipient-context factorization.

Implements `preregistrations/PREREGISTRATION_G24B_DONOR_RECIPIENT_FACTORIZATION.md`
verbatim: the §4 bridge (with its §12 cross-check against the frozen G23C
bridge gates), the §6 donor-side estimands in raw sign-aligned rating points,
the §7 cluster bootstrap (case skeletons, seed 20260924, 10,000 percentile
resamples) and the §8 five-outcome map with the §9.1 identity-patch check.

Stdlib only: the same module imports in the test environment (no torch) and on
the run host.  The runner `g24b_donor_state.py` imports the frozen constants
from here so there is exactly one copy of them.

The analysis reuses G23C's machinery verbatim — the item meta loader, the
dict-file completeness/`gather`, the percentile cluster `summarise`, the
`_bundle`/`pass_gate`/`pooled_gate` gates, `bridge_stats` and
`_identity_check` — so G24B differs from G23C only in the donor x recipient
grid, the donor-side estimand aggregation, the seed, the design tag, the
classifier and the licensed wording.

Settled before the design freeze (prereg §12):
- recipients are exactly the two policy-0 cells {ME, UE}; the grid is exactly
  the 8 ordered pairs donors {ME,MA,UE,UA} x recipients {ME,UE}; the primary
  pools the two recipients by a per-item mean, recipient-specific interactions
  are report-only;
- §8 condition 2 ("absent or substantially weaker" at the negative layers) is
  frozen as: at each of L4 / L24 PASS(DonorTargetInteraction) is false, OR the
  pooled primary mean at L14 exceeds that control layer by >= the 3.0 floor;
- §8 classifier order is strictly literal: no-donor-policy-state fires when
  DonorPolicy_M fails; donor-generic-policy-state additionally requires the
  primary NOT to pass — a passing primary whose control clause fails yields
  `unresolved`, never `donor-generic-policy-state`;
- §9.1 identity tolerance = 0.5 rating points; a violation aborts the
  analysis with no scientific verdict (shared `_identity_check`, which
  scans every CELLS x layer against its own baseline);
- §7 skeletons use the repository-standard `cluster_of` key computed in
  `load_frozen_meta` (legal: case, else family + base_context[:60]); the 75
  items give 15 clusters; the pooled bootstrap keeps both models' observations
  of one skeleton in a single cluster;
- §4 bridge gate booleans are cross-checked against the frozen G23C bridge
  (results/mech/g23c_bridge_analysis.json); the comparison helper lives here
  and phase_bridge stays input-parameterized for synthetic fixtures.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

# Frozen substrate, estimands, gates, identity check and bootstrap are
# imported from the G23C analyzer (§11.1: one copy of the cells, floors,
# model ids, completeness guards and gates).  Only the donor x recipient
# grid, the seed, the design tag, the estimand aggregation, the classifier
# and the licensed wording are G24B's own.
from analyze_g23c import (  # noqa: E402
    ROOT, CELLS, CELL_TABLE, FAMILIES, MODELS, MODEL_IDS,  # noqa: F401
    PRIMARY_LAYER, CONTROL_LAYERS, FLOOR, BRIDGE_FLOOR, IDENTITY_TOL,
    N_RESAMPLES, MIN_MODELS_POSITIVE,  # noqa: F401
    frozen_layers, nearest_layer_24, load_frozen_meta, summarise as _summarise,
    pooled_gate, pass_gate, bridge_quantities, bridge_stats, _bundle, _fmt,
    _warn_drops, _identity_check, _bridge_section,
)

DESIGN_TAG = "g24b-donor-recipient-factorization-design-v1"
G24B_SEED = 20260924

# §6: every cell is a donor; only the two policy-0 cells are recipients.
DONORS = ("ME", "MA", "UE", "UA")
RECIPIENTS = ("ME", "UE")
PATCHES = {f"{d}_to_{r}": (d, r) for r in RECIPIENTS for d in DONORS}

LICENSED = {
    "donor-conditioned-policy-state":
        "With the recipient prompt held fixed, rule-end states from "
        "matched-target donors carry a larger causally transportable "
        "zero-versus-full policy effect than rule-end states from "
        "unrelated-target donors: target availability during policy "
        "processing changes what policy information the rule-time state "
        "itself contains.",
    "donor-generic-policy-state":
        "the rule-end state carries causally transportable policy value "
        "regardless of the donor's target context; the intervention does "
        "not show that the transported policy information is "
        "target-conditioned.",
    "no-donor-policy-state":
        "the rule-end state is not shown to carry a causally transportable "
        "policy distinction into a fixed recipient; G23C's within-preview "
        "interchange alone cannot separate state-side target conditioning "
        "from matched-recipient sensitivity.",
    "bridge-failed":
        "The frozen behavioral bridge fails. Stop before donor-recipient "
        "patching.",
    "unresolved":
        "Any other pattern.",
}

VERDICTS = ("donor-conditioned-policy-state", "donor-generic-policy-state",
            "no-donor-policy-state", "bridge-failed", "unresolved")


def summarise(pairs, seed=G24B_SEED):
    """G23C's percentile cluster bootstrap, with G24B's frozen seed."""
    return _summarise(pairs, seed=seed)


def _complete_y(rec):
    return all(isinstance(rec.get("y", {}).get(c), (int, float)) for c in CELLS)


def _complete_grid(rec, layers):
    """Every record carries all 8 grid patches at every frozen layer."""
    p = rec.get("patch", {})
    return all(isinstance(p.get(n, {}).get(str(L)), (int, float))
               for n in PATCHES for L in layers)


def _complete_identity(rec, layers):
    return all(isinstance(rec.get("identity", {}).get(str(L), {}).get(c),
                          (int, float)) for L in layers for c in CELLS)


def gather(paths, meta, phase):
    """G24B's completeness + frozen-design guard (mirrors G23C `gather`,
    but over the 8-cell donor x recipient grid and this design's tag)."""
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
                or (_complete_grid(rec, want) and _complete_identity(rec,
                                                                     want)))
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


# ---------------------------------------------------------------- estimands
def donor_quantities(patch_y, s, layer_key=None):
    """§6 per-item donor-side estimands at one layer (raw aligned points).

    patch_y maps patch-name -> signed-aligned patched readout (the caller has
    already multiplied by s).  DonorPolicy_M(R) = Y(MA->R) - Y(ME->R);
    DonorPolicy_U(R) = Y(UA->R) - Y(UE->R); DonorTargetInteraction(R) = the
    difference; the primary pools the two frozen recipients by a per-item mean.
    """
    if len(patch_y) != len(PATCHES):
        raise SystemExit(
            f"[g24b] {layer_key}: need all {len(PATCHES)} grid patches, got "
            f"{len(patch_y)}")
    out = {}
    for r in RECIPIENTS:
        pm = patch_y[f"MA_to_{r}"] - patch_y[f"ME_to_{r}"]
        pu = patch_y[f"UA_to_{r}"] - patch_y[f"UE_to_{r}"]
        out[f"pm_{r}"] = pm
        out[f"pu_{r}"] = pu
        out[f"dti_{r}"] = pm - pu
    out["donor_policy_m"] = (out["pm_ME"] + out["pm_UE"]) / 2.0
    out["donor_policy_u"] = (out["pu_ME"] + out["pu_UE"]) / 2.0
    out["dti"] = (out["dti_ME"] + out["dti_UE"]) / 2.0
    return out


# ---------------------------------------------------------------- bridge
def gate_triple(gates):
    """Boolean gate triple + passed flag of a §4 bridge gates block."""
    return (bool(gates["gate1_pooled_policy_effect_m"]),
            bool(gates["gate2_pooled_target_policy_interaction"]),
            bool(gates["gate3_positive_model_means_2_of_2"]),
            bool(gates["passed"]))


def require_frozen_bridge(gates, frozen_path=None):
    """§12 bridge cross-check: abort unless the boolean triple matches the
    frozen G23C bridge.  Returns True when it matches."""
    if frozen_path is None:
        frozen_path = os.path.join(ROOT, "results", "mech",
                                   "g23c_bridge_analysis.json")
    if not os.path.exists(frozen_path):
        raise SystemExit(
            f"[g24b] frozen G23C bridge analysis not found: {frozen_path}")
    frozen = json.load(open(frozen_path))
    if gate_triple(gates) != gate_triple(frozen["gates"]):
        raise SystemExit(
            "[g24b] bridge gate triple does not match the frozen G23C bridge "
            f"({gate_triple(gates)} != {gate_triple(frozen['gates'])}); the "
            "frozen baseline is no longer reproducible — abort.")
    return True


def bridge_section(bridge):
    """Report view of bridge_stats (same as G23C's `_bridge_section`)."""
    return _bridge_section(bridge)


# ---------------------------------------------------------------- classify
def classify(bridge_pass, dpm_pass, dpu_pass, dti_pass, controls_ok):
    """§8 outcome map, in its strictly literal decision order."""
    if not bridge_pass:
        return "bridge-failed"
    if not dpm_pass:
        return "no-donor-policy-state"
    if dti_pass and controls_ok:
        return "donor-conditioned-policy-state"
    if dpu_pass and not dti_pass:
        return "donor-generic-policy-state"
    return "unresolved"


# ---------------------------------------------------------------- phases
def phase_bridge(meta, paths=None, frozen_bridge=None):
    paths = paths or {t: os.path.join(ROOT, "results", "mech",
                                      f"g24b_bridge_{t}.json")
                      for t in MODELS}
    rows, drops, layers = gather(paths, meta, phase="bridge")
    bridge = bridge_stats(rows, meta)
    if frozen_bridge is not None:
        require_frozen_bridge(bridge["gates"], frozen_path=frozen_bridge)
    return {"design": {"seed": G24B_SEED, "resamples": N_RESAMPLES,
                       "floor": FLOOR, "bridge_floor": BRIDGE_FLOOR,
                       "n_items_expected": len(meta),
                       "n_complete": {t: len(rows.get(t, [])) for t in MODELS},
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
            "verdict": None if bridge["gates"]["passed"] else "bridge-failed",
            "licensed": None if bridge["gates"]["passed"]
                        else LICENSED["bridge-failed"]}


def phase_full(meta, paths=None):
    paths = paths or {t: os.path.join(ROOT, "results", "mech",
                                      f"g24b_patch_{t}.json")
                      for t in MODELS}
    rows, drops, layers = gather(paths, meta, phase="full")
    # §9.1 identity: all CELLS x layers within IDENTITY_TOL of baseline.
    identity = _identity_check(rows, layers)
    bridge = bridge_stats(rows, meta)

    # §8 stop rule: a failed bridge ends the round before any donor statistic.
    if not bridge["gates"]["passed"]:
        return {"design": {"seed": G24B_SEED, "resamples": N_RESAMPLES,
                           "floor": FLOOR, "bridge_floor": BRIDGE_FLOOR,
                           "layers": list(layers),
                           "primary": PRIMARY_LAYER,
                           "controls": [CONTROL_LAYERS[0], layers[2]],
                           "n_items_expected": len(meta),
                           "n_complete": {t: len(rows.get(t, []))
                                          for t in MODELS}},
                "design_tag": DESIGN_TAG,
                "identity": identity,
                "bridge": bridge_section(bridge),
                "drops": drops,
                "layers": None,
                "controls": None,
                "verdict": "bridge-failed",
                "licensed": LICENSED["bridge-failed"]}

    # §6 donor-side quantities at each frozen layer
    layer_reports = {}
    for L in layers:
        # per-model pair lists keyed by estimand name
        keys = ("donor_policy_m", "donor_policy_u", "dti",
                "dti_ME", "dti_UE")
        cells = {n: {t: [] for t in rows} for n in PATCHES}
        qty = {k: {t: [] for t in rows} for k in keys}
        for tag, recs in rows.items():
            for iid, rec in recs:
                cluster, s = meta[iid]["cluster"], meta[iid]["s"]
                patch_y = {n: s * rec["patch"][n][str(L)] for n in PATCHES}
                q = donor_quantities(patch_y, str(L))
                for k in keys:
                    qty[k][tag].append((cluster, q[k]))
                for n in PATCHES:
                    cells[n][tag].append((cluster, patch_y[n]))
        layer_reports[str(L)] = {
            "donor_policy_m": _bundle(qty["donor_policy_m"], floor=FLOOR),
            "donor_policy_u": _bundle(qty["donor_policy_u"], floor=FLOOR),
            "dti": _bundle(qty["dti"], floor=FLOOR),
            "dti_ME": _bundle(qty["dti_ME"]),
            "dti_UE": _bundle(qty["dti_UE"]),
            "patches": {n: _bundle(cells[n]) for n in PATCHES},
        }

    primary = layer_reports[str(PRIMARY_LAYER)]
    dpm_pass = primary["donor_policy_m"]["pass"]
    dpu_pass = primary["donor_policy_u"]["pass"]
    dti_pass = primary["dti"]["pass"]

    # §8 condition 2 / §12: control clause on the primary, both frozen layers.
    controls = {"layers": {}, "passed": True}
    l14_mean = primary["dti"]["pooled"]["mean"]
    for cl in (CONTROL_LAYERS[0], layers[2]):
        cb = layer_reports[str(cl)]["dti"]
        absent = not cb["pass"]
        weaker = (l14_mean - cb["pooled"]["mean"]) >= FLOOR
        ok = bool(absent or weaker)
        controls["layers"][str(cl)] = {
            "dti_pass": cb["pass"], "absent": absent,
            "weaker_by_floor": weaker, "ok": ok,
            "dti_mean": cb["pooled"]["mean"]}
        controls["passed"] = bool(controls["passed"] and ok)
    controls_ok = bool(controls["passed"])

    verdict = classify(bridge["gates"]["passed"], dpm_pass, dpu_pass,
                       dti_pass, controls_ok)
    return {"design": {"seed": G24B_SEED, "resamples": N_RESAMPLES,
                       "floor": FLOOR, "bridge_floor": BRIDGE_FLOOR,
                       "identity_tolerance": IDENTITY_TOL,
                       "layers": list(layers),
                       "primary": PRIMARY_LAYER,
                       "controls": [CONTROL_LAYERS[0], layers[2]],
                       "n_items_expected": len(meta),
                       "n_complete": {t: len(rows.get(t, [])) for t in MODELS},
                       "n_clusters": len({m["cluster"]
                                          for m in meta.values()})},
            "design_tag": DESIGN_TAG,
            "identity": identity,
            "bridge": bridge_section(bridge),
            "layers": layer_reports,
            "controls": controls,
            "controls_ok": controls_ok,
            "gates": {"donor_policy_m_pass": dpm_pass,
                      "donor_policy_u_pass": dpu_pass,
                      "dti_pass": dti_pass},
            "drops": drops,
            "verdict": verdict,
            "licensed": LICENSED[verdict]}


# ---------------------------------------------------------------- print
def print_bridge(rep):
    d = rep["design"]
    print("G24B — phase bridge (direct readout, Stage-5 2x2, no patching)")
    print(f"  seed {d['seed']}, {d['resamples']} cluster resamples, "
          f"bridge floor {d['bridge_floor']}, complete {d['n_complete']} "
          f"of {d['n_items_expected']} (expected per model)")
    print("  cells: ME=M0  MA=M100  UE=U0  UA=U100")
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
    if not g["passed"]:
        print("BRIDGE: FAIL — stop before donor-recipient patching "
              "(verdict bridge-failed)")
        print(f"LICENSED: {rep['licensed']}")


def print_full(rep):
    d = rep["design"]
    print("G24B — donor-state vs recipient-context factorization")
    print(f"  layers {d['layers']} (primary L{d['primary']}, controls "
          f"L{d['controls'][0]}/L{d['controls'][1]}), seed {d['seed']}, "
          f"{d['resamples']} resamples, floor {d['floor']}, identity tol "
          f"{d['identity_tolerance']}")
    print(f"  complete per model: {d['n_complete']} of "
          f"{d['n_items_expected']}, clusters {d['n_clusters']}")
    idr = rep["identity"]
    print(f"  identity patch: max |delta| {idr['max_abs_delta']:.4f} <= "
          f"{idr['tolerance']} over {idr['n_checked']} checks")
    print(f"  bridge gates: {rep['bridge']['gates']}")
    _warn_drops(rep["drops"])
    if rep["layers"] is None:
        print("stop rule: bridge failed — donor statistics not computed")
        print(f"VERDICT: {rep['verdict']}")
        print(f"LICENSED: {rep['licensed']}")
        return
    for L in d["layers"]:
        e = rep["layers"][str(L)]
        tag = "PRIMARY" if L == d["primary"] else "control"
        print(f"  --- L{L} ({tag})")
        for name in ("donor_policy_m", "donor_policy_u", "dti",
                     "dti_ME", "dti_UE"):
            p = e[name].get("pass")
            print(f"      {name:<20} {_fmt(e[name]['pooled'])} "
                  f"pass={p if p is not None else '-'}")
        for n in PATCHES:
            print(f"      patch {n:<10} {_fmt(e['patches'][n]['pooled'])}")
    print(f"  controls (§8.2/§12): {rep['controls']}")
    print(f"VERDICT: {rep['verdict']}")
    print(f"LICENSED: {rep['licensed']}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", choices=["bridge", "full"], required=True)
    ap.add_argument("--bridge-frozen", default=os.path.join(
        ROOT, "results", "mech", "g23c_bridge_analysis.json"),
        help="frozen G23C bridge analysis for the mandatory §12 "
             "cross-check (default: the frozen file; tests override)")
    args = ap.parse_args()

    meta = load_frozen_meta()
    if args.phase == "bridge":
        rep = phase_bridge(meta, frozen_bridge=args.bridge_frozen)
        print_bridge(rep)
        out = os.path.join(ROOT, "results", "mech",
                           "g24b_bridge_analysis.json")
    else:
        rep = phase_full(meta)
        print_full(rep)
        out = os.path.join(ROOT, "results", "mech", "g24b_analysis.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(rep, open(out, "w"), indent=1)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
