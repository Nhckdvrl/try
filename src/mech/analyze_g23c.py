"""G23C frozen analyzer — target-conditioned policy-state interchange.

Implements `preregistrations/PREREGISTRATION_G23C_TARGET_CONDITIONED_POLICY_STATE.md`
verbatim: the §4 bridge gate, the §6 switch/transfer estimands in raw sign-aligned
rating points, the §7 cluster bootstrap (case skeletons, seed 20260923, 10,000
percentile resamples) and the §8 five-outcome map with the §9.1 identity-patch
integrity check.

Stdlib only: the same module imports in the test environment (no torch) and on
the run host.  The runner `g23c_policy_state.py` imports the frozen constants
from here so there is exactly one copy of them.

Settled before the design freeze (prereg §12):
- §8 condition 3 ("absent or substantially weaker" at the negative layers) is
  frozen as: at each of L4 / L24 the TC pattern is absent (PASS(TC) is false),
  OR TC at L14 exceeds TC at that control layer by >= the 3.0 floor;
- §8 classifier order is strictly literal: generic-policy-state additionally
  requires TargetConditioning NOT to pass — TC passing while the control clause
  fails yields `unresolved`, not `generic-policy-state`;
- §9.1 identity tolerance = 0.5 rating points; a violation aborts the analysis
  with no scientific verdict;
- §7 "independent case skeletons" uses the repository-standard `cluster_of`
  (src/cluster_robustness.py): `legal:` + meta.case for legal_judgment, else
  family + base_context[:60] (the latent problem); in the pooled bootstrap both
  models' observations of the same skeleton share one cluster;
- §4 gates 1/2 are pooled-stat gates; gate 3 adds per-model positivity for the
  same two quantities.
"""
from __future__ import annotations

import argparse
import json
import os
import random
import statistics as st
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")

# ---------------------------------------------------------------- frozen spec
DESIGN_TAG = "g23c-target-conditioned-policy-state-design-v1"
MODELS = ("qwen3-8b", "mistral-small-24b")
MODEL_IDS = {"qwen3-8b": "Qwen/Qwen3-8B",
             "mistral-small-24b": "data/mistral_small_24b_hf"}
FAMILIES = ("legal_judgment", "evidence_inference")

# Stage-5 cell names, prereg §3 (M0/M100/U0/U100 renamed for clarity):
#   ME = matched   preview + weight 0%    = M0
#   MA = matched   preview + weight 100%  = M100
#   UE = unrelated preview + weight 0%    = U0
#   UA = unrelated preview + weight 100%  = U100
CELLS = ("ME", "MA", "UE", "UA")
CELL_TABLE = {"ME": ("match", False), "MA": ("match", True),
              "UE": ("unrel", False), "UA": ("unrel", True)}

# (preview, admit) -> cell above;  donor cell -> recipient cell, prereg §6:
DIRECTIONS = {"M_100to0": ("MA", "ME"),    # patch M100 -> M0
              "M_0to100": ("ME", "MA"),    # patch M0   -> M100
              "U_100to0": ("UA", "UE"),    # patch U100 -> U0
              "U_0to100": ("UE", "UA")}    # patch U0   -> U100

PRIMARY_LAYER = 14            # §5, fixed from the completed Stage-5 localization
CONTROL_LAYERS = (4, 24)      # §5 negative controls; no layer search
FLOOR = 3.0                   # §7 meaningful floor, rating points
BRIDGE_FLOOR = 5.0            # §4 bridge floor, rating points
IDENTITY_TOL = 0.5            # §9.1 identity patch, rating points
SEED = 20260923               # §7
N_RESAMPLES = 10_000          # §7
MIN_MODELS_POSITIVE = 2       # §8 "positive in 2/2 models"

VERDICTS = ("target-conditioned-policy-state", "generic-policy-state",
            "target-readiness-only", "bridge-failed", "unresolved")

LICENSED = {
    "target-conditioned-policy-state":
        "When the target proposition is available during policy processing, the "
        "rule-time state carries causally exchangeable information about whether "
        "that target should have zero or full decision weight.",
    "generic-policy-state":
        "the rule-time state carries policy value, but the intervention does not "
        "show that policy encoding depends on target availability.",
    "target-readiness-only":
        "Stage 5's transferable state is not shown to carry the policy value "
        "itself; it may instead reflect target/context readiness or another "
        "covarying state.",
    "bridge-failed":
        "The frozen behavioral bridge fails. Stop before patching.",
    "unresolved":
        "Any other pattern.",
}


def nearest_layer_24(n_layers: int) -> int:
    """§5: layer 24, or the nearest valid layer if the model is shallower."""
    return min(CONTROL_LAYERS[1], n_layers - 1)


def frozen_layers(n_layers: int) -> tuple:
    """The only layers G23C may patch: (4, 14, nearest-valid-24)."""
    return (CONTROL_LAYERS[0], PRIMARY_LAYER, nearest_layer_24(n_layers))


# ---------------------------------------------------------------- items
def load_frozen_meta() -> dict:
    """item_id -> {cluster, family, s} for the Stage-5 frozen items in the two
    preregistered families.  `cluster` is the §7 skeleton, keyed exactly as the
    repository-standard cluster_of (legal: meta.case, else family +
    base_context[:60] = latent problem)."""
    keep = set(json.load(open(os.path.join(ROOT, "data", "items",
                                           "frozen_v1.json"))))
    out = {}
    with open(os.path.join(ROOT, "data", "items", "items_v1.jsonl")) as handle:
        for line in handle:
            if not line.strip():
                continue
            r = json.loads(line)
            if r["item_id"] in keep and r["task_family"] in FAMILIES:
                cluster = (r["task_family"] + ":" + r["base_context"][:60]
                           if r["task_family"] != "legal_judgment"
                           else "legal:" + r["meta"]["case"])
                out[r["item_id"]] = {
                    "cluster": cluster,
                    "family": r["task_family"],
                    "s": 1.0 if r["critical_direction"] == "increase" else -1.0,
                }
    return out


# ---------------------------------------------------------------- file wiring
def bridge_path(tag: str) -> str:
    return os.path.join(ROOT, "results", "mech", f"g23c_bridge_{tag}.json")


def patch_path(tag: str) -> str:
    return os.path.join(ROOT, "results", "mech", f"g23c_patch_{tag}.json")


# ---------------------------------------------------------------- completeness
def _complete_y(rec) -> bool:
    return all(isinstance(rec.get("y", {}).get(c), (int, float)) for c in CELLS)


def _complete_patch(rec, layers) -> bool:
    p = rec.get("patch", {})
    return all(isinstance(p.get(d, {}).get(str(L)), (int, float))
               for d in DIRECTIONS for L in layers)


def _complete_identity(rec, layers) -> bool:
    i = rec.get("identity", {})
    return all(isinstance(i.get(str(L), {}).get(c), (int, float))
               for L in layers for c in CELLS)


def gather(paths: dict, meta: dict, phase: str):
    """-> (rows, drops, layers).

    rows[tag] = [(item_id, rec), ...] for complete observations only.  Drops are
    the §4/§7 accounting (missing id, unknown id, incomplete cells); no item is
    ever selected or dropped on its behavioral gap.  The recorded layer set of
    every file must equal the frozen layer set for its own depth — otherwise the
    run is rejected (no layer search, §5).
    """
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
                f"{design.get('controls')} does not match the frozen "
                f"configuration {want} — refusing to analyze.")
        layers_seen.add(want)
        drops[tag] = {"missing_item": 0, "unknown_item": 0, "incomplete": 0}
        by_id = {r["item_id"]: r for r in d["records"]}
        rows[tag] = []
        for iid, _m in meta.items():
            rec = by_id.get(iid)
            if rec is None:
                drops[tag]["missing_item"] += 1
                continue
            need = _complete_y(rec) and (
                phase == "bridge"
                or (_complete_patch(rec, want) and _complete_identity(rec, want)))
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
def summarise(pairs, seed: int = SEED):
    """Percentile cluster bootstrap: resample skeletons, keep every observation
    of a sampled skeleton (both models' rows of a case) together (§7)."""
    out = {"n": len(pairs), "n_clusters": 0, "mean": float("nan"),
           "ci_low": float("nan"), "ci_high": float("nan")}
    if not pairs:
        return out
    by = {}
    for c, v in pairs:
        by.setdefault(c, []).append(v)
    clusters = sorted(by)
    out["n_clusters"] = len(clusters)
    out["mean"] = st.mean(v for _, v in pairs)
    rng = random.Random(seed)
    reps = []
    for _ in range(N_RESAMPLES):
        pick = [rng.choice(clusters) for _ in clusters]
        reps.append(st.mean(v for c in pick for v in by[c]))
    reps.sort()
    out["ci_low"] = reps[int(0.025 * (N_RESAMPLES - 1))]
    out["ci_high"] = reps[int(0.975 * (N_RESAMPLES - 1))]
    return out


def pooled_gate(stats: dict, floor: float) -> bool:
    """§4 gates 1-2: pooled mean >= floor AND CI lower bound > 0."""
    m = stats["mean"]
    return bool(m == m and m >= floor and stats["ci_low"] == stats["ci_low"]
                and stats["ci_low"] > 0)


def pass_gate(stats: dict, model_means, floor: float = FLOOR) -> bool:
    """§8 PASS(X): pooled mean >= floor, CI lower > 0, positive in 2/2 models."""
    if not pooled_gate(stats, floor):
        return False
    positive = sum(1 for m in model_means if m == m and m > 0)
    return positive >= MIN_MODELS_POSITIVE


def bridge_quantities(s, y):
    """§4 sign-aligned bridge quantities for one item."""
    pe_m = s * (y["MA"] - y["ME"])
    pe_u = s * (y["UA"] - y["UE"])
    return pe_m, pe_u, pe_m - pe_u


def switch_quantity(direction: str, s, y, patched: float) -> float:
    """§6 donor-direction-aligned switch, raw sign-aligned points."""
    if direction == "M_100to0":       # recipient ME, donor MA
        return s * (patched - y["ME"])
    if direction == "M_0to100":       # recipient MA, donor ME
        return s * (y["MA"] - patched)
    if direction == "U_100to0":       # recipient UE, donor UA
        return s * (patched - y["UE"])
    if direction == "U_0to100":       # recipient UA, donor UE
        return s * (y["UA"] - patched)
    raise ValueError(direction)


def estimands_from_switches(sw: dict) -> tuple:
    """§6: PolicyTransfer_* = mean of the two directions (per item);
    TargetConditioning = PolicyTransfer_M - PolicyTransfer_U."""
    pt_m = st.mean([sw["M_100to0"], sw["M_0to100"]])
    pt_u = st.mean([sw["U_100to0"], sw["U_0to100"]])
    return pt_m, pt_u, pt_m - pt_u


def classify(bridge_pass: bool, ptm_pass: bool, ptu_pass: bool,
             tc_pass: bool, controls_ok: bool) -> str:
    """§8 outcome map, in its literal decision order."""
    if not bridge_pass:
        return "bridge-failed"
    if not ptm_pass:
        return "target-readiness-only"
    if tc_pass and controls_ok:
        return "target-conditioned-policy-state"
    if ptu_pass and not tc_pass:
        return "generic-policy-state"
    return "unresolved"


# ---------------------------------------------------------------- shared parts
def _bundle(pairs_by_model, floor=None):
    pooled = [(c, v) for t in pairs_by_model for c, v in pairs_by_model[t]]
    b = {"pooled": summarise(pooled),
         "per_model": {t: summarise(pairs_by_model[t]) for t in pairs_by_model}}
    if floor is not None:
        b["pass"] = pass_gate(
            b["pooled"], [b["per_model"][t]["mean"] for t in b["per_model"]],
            floor)
    return b


def bridge_stats(rows, meta):
    """§4 quantities from the four baselines, pooled over both models."""
    q = {t: {k: [] for k in ("pe_m", "pe_u", "tpi")} for t in rows}
    for tag, recs in rows.items():
        for iid, rec in recs:
            pe_m, pe_u, tpi = bridge_quantities(meta[iid]["s"], rec["y"])
            cluster = meta[iid]["cluster"]
            for k, v in (("pe_m", pe_m), ("pe_u", pe_u), ("tpi", tpi)):
                q[tag][k].append((cluster, v))
    out = {"policy_effect_m": _bundle({t: q[t]["pe_m"] for t in q}),
           "policy_effect_u": _bundle({t: q[t]["pe_u"] for t in q}),
           "target_policy_interaction": _bundle({t: q[t]["tpi"] for t in q})}

    def all_means(b):
        return [b["per_model"][t]["mean"] for t in b["per_model"]]

    g1 = pooled_gate(out["policy_effect_m"]["pooled"], BRIDGE_FLOOR)
    g2 = pooled_gate(out["target_policy_interaction"]["pooled"], BRIDGE_FLOOR)
    g3 = (all(m == m and m > 0 for m in all_means(out["policy_effect_m"]))
          and all(m == m and m > 0
                  for m in all_means(out["target_policy_interaction"])))
    out["gates"] = {"gate1_pooled_policy_effect_m": g1,
                    "gate2_pooled_target_policy_interaction": g2,
                    "gate3_positive_model_means_2_of_2": g3,
                    "passed": bool(g1 and g2 and g3)}
    return out


def _bridge_section(bridge: dict) -> dict:
    """Report view of bridge_stats: raw pooled stats, raw per-model stats,
    the three §4 gates."""
    keys = ("policy_effect_m", "policy_effect_u", "target_policy_interaction")
    return {"pooled": {k: bridge[k]["pooled"] for k in keys},
            "per_model": {t: {k: bridge[k]["per_model"][t] for k in keys}
                          for t in MODELS},
            "gates": bridge["gates"]}


def _identity_check(rows, layers) -> dict:
    """§9.1 — an implementation check, not a scientific result.  Raises on a
    violation so no verdict is ever printed from a broken patcher."""
    worst, n, offender = 0.0, 0, None
    for tag, recs in rows.items():
        for iid, rec in recs:
            for L in layers:
                for c in CELLS:
                    delta = abs(rec["identity"][str(L)][c] - rec["y"][c])
                    n += 1
                    if delta > worst:
                        worst, offender = delta, (tag, iid, L, c)
    report = {"n_checked": n, "max_abs_delta": worst,
              "tolerance": IDENTITY_TOL, "passed": worst <= IDENTITY_TOL}
    if not report["passed"]:
        raise SystemExit(
            f"IDENTITY PATCH FAILED: max |delta| = {worst:.4f} > "
            f"{IDENTITY_TOL} at {offender} — implementation bug, no verdict "
            f"is reported.")
    return report


# ---------------------------------------------------------------- phases
def phase_bridge(meta: dict, paths: dict = None) -> dict:
    paths = paths or {t: bridge_path(t) for t in MODELS}
    rows, drops, layers = gather(paths, meta, phase="bridge")
    bridge = bridge_stats(rows, meta)
    return {"design": {"seed": SEED, "resamples": N_RESAMPLES,
                       "floor": FLOOR, "bridge_floor": BRIDGE_FLOOR,
                       "n_items_expected": len(meta),
                       "n_complete": {t: len(rows.get(t, [])) for t in MODELS},
                       "n_clusters": len({m["cluster"] for m in meta.values()})},
            "pooled": {k: bridge[k]["pooled"] for k in ("policy_effect_m",
                                                        "policy_effect_u",
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


def phase_full(meta: dict, paths: dict = None) -> dict:
    paths = paths or {t: patch_path(t) for t in MODELS}
    rows, drops, layers = gather(paths, meta, phase="full")
    identity = _identity_check(rows, layers)          # §9.1, aborts if broken
    bridge = bridge_stats(rows, meta)

    # §4 / §8 stop rule: a failed bridge ends the round before any transfer
    # statistic is computed.
    if not bridge["gates"]["passed"]:
        return {"design": {"seed": SEED, "resamples": N_RESAMPLES,
                           "floor": FLOOR, "bridge_floor": BRIDGE_FLOOR,
                           "layers": list(layers),
                           "primary": PRIMARY_LAYER,
                           "controls": [CONTROL_LAYERS[0], layers[2]],
                           "n_items_expected": len(meta),
                           "n_complete": {t: len(rows.get(t, []))
                                          for t in MODELS}},
                "identity": identity,
                "bridge": _bridge_section(bridge),
                "drops": drops,
                "layers": None,
                "controls": None,
                "verdict": "bridge-failed",
                "licensed": LICENSED["bridge-failed"]}

    # §6 switches at each frozen layer
    layer_reports = {}
    for L in layers:
        sw = {d: {t: [] for t in rows} for d in DIRECTIONS}
        ptm, ptu, tc = ({t: [] for t in rows} for _ in range(3))
        for tag, recs in rows.items():
            for iid, rec in recs:
                cluster, s = meta[iid]["cluster"], meta[iid]["s"]
                per_dir = {d: switch_quantity(d, s, rec["y"],
                                              rec["patch"][d][str(L)])
                           for d in DIRECTIONS}
                m, u, t = estimands_from_switches(per_dir)
                for d in DIRECTIONS:
                    sw[d][tag].append((cluster, per_dir[d]))
                ptm[tag].append((cluster, m))
                ptu[tag].append((cluster, u))
                tc[tag].append((cluster, t))
        layer_reports[str(L)] = {
            "switches": {d: _bundle(sw[d]) for d in DIRECTIONS},
            "policy_transfer_m": _bundle(ptm, FLOOR),
            "policy_transfer_u": _bundle(ptu, FLOOR),
            "target_conditioning": _bundle(tc, FLOOR)}

    primary = layer_reports[str(PRIMARY_LAYER)]
    ptm_pass = primary["policy_transfer_m"]["pass"]
    ptu_pass = primary["policy_transfer_u"]["pass"]
    tc_pass = primary["target_conditioning"]["pass"]
    tc14 = primary["target_conditioning"]["pooled"]["mean"]

    # §8 condition 3, operationalized in §12: at each control layer the TC
    # pattern is absent (does not pass) or weaker than L14 by >= one floor.
    ctrl = [L for L in layers if L != PRIMARY_LAYER]
    controls = {"layers": {}, "passed": True}
    for L in ctrl:
        tcl = layer_reports[str(L)]["target_conditioning"]
        absent = not tcl["pass"]
        weaker = (tc14 == tc14 and tcl["pooled"]["mean"] == tcl["pooled"]["mean"]
                  and (tc14 - tcl["pooled"]["mean"]) >= FLOOR)
        ok = bool(absent or weaker)
        controls["layers"][str(L)] = {
            "tc_mean": tcl["pooled"]["mean"],
            "tc_pass": tcl["pass"],
            "pattern_absent": bool(absent),
            "weaker_by_at_least_floor": bool(weaker),
            "ok": ok}
        controls["passed"] = controls["passed"] and ok
    controls["passed"] = bool(controls["passed"])

    verdict = classify(True, ptm_pass, ptu_pass, tc_pass, controls["passed"])

    return {"design": {"seed": SEED, "resamples": N_RESAMPLES, "floor": FLOOR,
                       "bridge_floor": BRIDGE_FLOOR,
                       "identity_tolerance": IDENTITY_TOL,
                       "layers": list(layers), "primary": PRIMARY_LAYER,
                       "controls": [CONTROL_LAYERS[0], layers[2]],
                       "n_items_expected": len(meta),
                       "n_complete": {t: len(rows.get(t, [])) for t in MODELS},
                       "n_clusters": len({m["cluster"] for m in meta.values()})},
            "identity": identity,
            "bridge": _bridge_section(bridge),
            "layers": layer_reports,
            "controls": controls,
            "drops": drops,
            "verdict": verdict,
            "licensed": LICENSED[verdict]}


# ---------------------------------------------------------------- report I/O
def _fmt(stats):
    if stats["n"] == 0:
        return "(no data)"
    return (f"{stats['mean']:+.2f} [{stats['ci_low']:+.2f}, "
            f"{stats['ci_high']:+.2f}] n={stats['n']}/{stats['n_clusters']}cl")


def _warn_drops(drops):
    if any(any(v for v in d.values()) for d in drops.values()):
        print(f"WARNING: non-complete rows excluded: {drops}")


def print_bridge(rep):
    d = rep["design"]
    print("G23C — phase bridge (direct readout, Stage-5 2x2, no patching)")
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
    if g["passed"]:
        print("BRIDGE: PASS — proceed to policy-state interchange")
    else:
        print("BRIDGE: FAIL — stop before policy-state interchange "
              "(verdict bridge-failed)")
        print(f"LICENSED: {rep['licensed']}")


def print_full(rep):
    d = rep["design"]
    print("G23C — target-conditioned policy-state interchange")
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
        print("stop rule: bridge failed — transfer statistics not computed")
        print(f"VERDICT: {rep['verdict']}")
        print(f"LICENSED: {rep['licensed']}")
        return
    for L in d["layers"]:
        e = rep["layers"][str(L)]
        tag = "PRIMARY" if L == d["primary"] else "control"
        print(f"  --- L{L} ({tag})")
        for name in ("policy_transfer_m", "policy_transfer_u",
                     "target_conditioning"):
            print(f"      {name:<20} {_fmt(e[name]['pooled'])} "
                  f"pass={e[name]['pass']}")
        for dn in DIRECTIONS:
            print(f"      switch {dn:<16} {_fmt(e['switches'][dn]['pooled'])}")
    print(f"  controls (§8.3/§12): {rep['controls']}")
    print(f"VERDICT: {rep['verdict']}")
    print(f"LICENSED: {rep['licensed']}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", choices=["bridge", "full"], required=True)
    args = ap.parse_args()

    meta = load_frozen_meta()
    if args.phase == "bridge":
        rep = phase_bridge(meta)
        print_bridge(rep)
        out = os.path.join(ROOT, "results", "mech",
                           "g23c_bridge_analysis.json")
    else:
        rep = phase_full(meta)
        print_full(rep)
        out = os.path.join(ROOT, "results", "mech", "g23c_analysis.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(rep, open(out, "w"), indent=1)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
