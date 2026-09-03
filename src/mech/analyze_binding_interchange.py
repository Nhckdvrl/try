"""G16 analysis — frozen gates from PREREGISTRATION_G16_BINDING_INTERCHANGE.md.

Gate 1 is evaluated from the baselines alone and is a stopping rule: if the bridge
fails, the patched phase must not be run and the verdict is `bridge-failed`.

    PYTHONPATH=src python3 src/mech/analyze_binding_interchange.py            # gate 1
    PYTHONPATH=src python3 src/mech/analyze_binding_interchange.py --patched  # all gates
"""
from __future__ import annotations

import argparse
import json
import os
import random
import statistics
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from binding_interchange import BRIDGE_FLOOR, GAP_FLOOR, LAYERS, SITES  # noqa: E402
from binding_prompts import FAMILIES  # noqa: E402
from common import ROOT, frozen_items  # noqa: E402

SEED = 20260829
N_RESAMPLES = 10_000
MAGNITUDE_FLOOR = 3.0


def cluster_of(item) -> str:
    """Case skeleton / latent problem, matching src/cluster_robustness.py."""
    if item.task_family == "legal_judgment":
        return "legal:" + item.meta["case"]
    return item.task_family + ":" + item.base_context[:60]


def clustered_ci(by_cluster: dict, seed: int = SEED) -> tuple[float, float]:
    rng = random.Random(seed)
    keys = list(by_cluster)
    reps = []
    for _ in range(N_RESAMPLES):
        pool = []
        for _ in range(len(keys)):
            pool += by_cluster[keys[rng.randrange(len(keys))]]
        reps.append(statistics.fmean(pool))
    reps.sort()
    return reps[int(0.025 * N_RESAMPLES)], reps[int(0.975 * N_RESAMPLES)]


def summarise(values_by_item: dict, clusters: dict) -> dict:
    by_cluster = defaultdict(list)
    for item_id, value in values_by_item.items():
        by_cluster[clusters[item_id]].append(value)
    flat = [v for vs in by_cluster.values() for v in vs]
    low, high = clustered_ci(by_cluster)
    return {"n": len(flat), "n_clusters": len(by_cluster),
            "mean": statistics.fmean(flat), "ci_low": low, "ci_high": high}


def gate1(baselines: dict, clusters: dict) -> dict:
    bridge = {r["item_id"]: r["bridge"] for r in baselines["records"]}
    stats = summarise(bridge, clusters)
    excl = {
        arm: summarise({r["item_id"]: r["exclusion_effect"][arm]
                        for r in baselines["records"]}, clusters)
        for arm in ("id", "cls")
    }
    passed = stats["mean"] >= BRIDGE_FLOOR and stats["ci_low"] > 0
    return {"bridge": stats, "exclusion_effect": excl,
            "floor": BRIDGE_FLOOR, "passed": passed}


def _sign_map(items) -> dict:
    return {i.item_id: (1.0 if i.critical_direction == "increase" else -1.0)
            for i in items}


def gates_2_to_5(baselines: dict, patched: dict, clusters: dict, signs: dict) -> dict:
    """Break/rescue per (site, layer), sign-aligned, against each item's own baseline."""
    base_y = {r["item_id"]: r["y"] for r in baselines["records"]}
    cells: dict = {}
    for site in SITES:
        for li, layer in enumerate(LAYERS):
            per_transfer: dict = {}
            for name, recipient in (("break", "cls_exclude"), ("rescue", "id_exclude"),
                                    ("admit_break", "cls_admit"),
                                    ("admit_rescue", "id_admit")):
                shift, orth = {}, {}
                for rec in patched["records"]:
                    block = rec["patch"].get(name, {}).get(site)
                    if not block or block["patched"][li] is None:
                        continue
                    item_id = rec["item_id"]
                    s = signs[item_id]
                    # positive = moved toward using the excluded evidence
                    shift[item_id] = s * (block["patched"][li] - base_y[item_id][recipient])
                    orth[item_id] = s * (block["orthogonal"][li] - base_y[item_id][recipient])
                if shift:
                    per_transfer[name] = {
                        "patched": summarise(shift, clusters),
                        "orthogonal": summarise(orth, clusters),
                        "minus_orthogonal": summarise(
                            {k: shift[k] - orth[k] for k in shift}, clusters),
                    }
            cells[f"{site}@L{layer}"] = per_transfer

    qualifying = []
    for site in SITES:
        for li, layer in enumerate(LAYERS):
            cell = cells.get(f"{site}@L{layer}", {})
            if "break" not in cell or "rescue" not in cell:
                continue
            brk, rsc = cell["break"]["patched"], cell["rescue"]["patched"]
            bidirectional = brk["ci_low"] > 0 and rsc["ci_high"] < 0
            magnitude = abs(brk["mean"]) >= MAGNITUDE_FLOOR
            if bidirectional and magnitude:
                qualifying.append({"site": site, "layer": layer,
                                   "break": brk["mean"], "rescue": rsc["mean"],
                                   "abs_break": abs(brk["mean"])})

    # gate 4: same sign pattern at a neighbouring tested layer, same site
    for q in qualifying:
        li = LAYERS.index(q["layer"])
        neighbours = [LAYERS[i] for i in (li - 1, li + 1) if 0 <= i < len(LAYERS)]
        q["adjacent_ok"] = False
        for layer in neighbours:
            cell = cells.get(f"{q['site']}@L{layer}", {})
            if "break" in cell and "rescue" in cell:
                if (cell["break"]["patched"]["mean"] > 0
                        and cell["rescue"]["patched"]["mean"] < 0):
                    q["adjacent_ok"] = True

    qualifying.sort(key=lambda q: -q["abs_break"])
    strongest = next((q for q in qualifying if q["adjacent_ok"]), None)

    verdict = "not-established"
    if strongest:
        cell = cells[f"{strongest['site']}@L{strongest['layer']}"]
        spec = cell["break"]["minus_orthogonal"]["ci_low"] > 0
        admit = cell.get("admit_break", {}).get("patched")
        admit_quiet = admit is None or abs(admit["mean"]) < MAGNITUDE_FLOOR
        strongest["specificity_ok"] = spec
        strongest["admit_quiet"] = admit_quiet
        if spec and admit_quiet:
            verdict = ("confirmed-binding-state-established-by-policy"
                       if strongest["site"] in ("rule_end", "rule_span")
                       else "confirmed-binding-state-late-only")

    return {"cells": cells, "qualifying": qualifying, "strongest": strongest,
            "verdict": verdict}


def diagnose(baselines: dict, clusters: dict, signs: dict) -> dict:
    """Explicitly post-result. Why the frozen bridge estimator behaved as it did.

    The frozen estimand anchors each arm on its own admit cell. That is only valid
    if both admit cells actually restore full evidential weight. `cls_admit` tells
    the model that an item marked as coming from an unauthorised source carries the
    full weight of a verified one, which is close to self-contradictory, so its
    anchor can collapse toward its own exclude cell and shrink the arm's measured
    exclusion effect for reasons that have nothing to do with binding.

    The common-anchor variant below is the estimator Stage 3A used: both arms scored
    against the same admit cell. It is reported as a diagnostic and changes no gate.
    """
    y = {r["item_id"]: r["y"] for r in baselines["records"]}

    def common(cell):
        return {i: signs[i] * (y[i]["id_admit"] - y[i][cell]) for i in y}

    id_common, cls_common = common("id_exclude"), common("cls_exclude")
    return {
        "note": "post-result diagnostic; changes no frozen gate or verdict",
        "anchor_gap_id_admit_minus_cls_admit": summarise(
            {i: signs[i] * (y[i]["id_admit"] - y[i]["cls_admit"]) for i in y}, clusters),
        "common_anchor_exclusion_effect": {
            "id": summarise(id_common, clusters),
            "cls": summarise(cls_common, clusters),
        },
        "common_anchor_bridge": summarise(
            {i: cls_common[i] - id_common[i] for i in y}, clusters),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--patched", action="store_true")
    ap.add_argument("--dir", default=os.path.join(ROOT, "results", "mech"))
    args = ap.parse_args()

    items = frozen_items(FAMILIES)
    clusters = {i.item_id: cluster_of(i) for i in items}
    signs = _sign_map(items)

    with open(os.path.join(args.dir, "g16_baselines.json")) as handle:
        baselines = json.load(handle)

    report = {"design_tag": baselines.get("design_tag"),
              "bootstrap": {"seed": SEED, "n_resamples": N_RESAMPLES,
                            "clusters": "case skeleton / latent problem"},
              "gate1": gate1(baselines, clusters),
              "posthoc_diagnostic": diagnose(baselines, clusters, signs)}

    g1 = report["gate1"]
    print(f"gate 1 bridge = {g1['bridge']['mean']:+.2f} "
          f"[{g1['bridge']['ci_low']:+.2f}, {g1['bridge']['ci_high']:+.2f}] "
          f"(n={g1['bridge']['n']}, {g1['bridge']['n_clusters']} clusters, "
          f"floor {BRIDGE_FLOOR}) -> {'PASS' if g1['passed'] else 'FAIL'}")
    for arm in ("id", "cls"):
        s = g1["exclusion_effect"][arm]
        print(f"  ExclusionEffect {arm:3s} = {s['mean']:+.2f} "
              f"[{s['ci_low']:+.2f}, {s['ci_high']:+.2f}]")

    d = report["posthoc_diagnostic"]
    print("\npost-result diagnostic (changes no gate):")
    a = d["anchor_gap_id_admit_minus_cls_admit"]
    print(f"  admit-anchor gap id-cls = {a['mean']:+.2f} [{a['ci_low']:+.2f}, {a['ci_high']:+.2f}]"
          "   <- cls_admit does not restore full weight")
    for arm in ("id", "cls"):
        s = d["common_anchor_exclusion_effect"][arm]
        print(f"  common-anchor ExclusionEffect {arm:3s} = {s['mean']:+.2f} "
              f"[{s['ci_low']:+.2f}, {s['ci_high']:+.2f}]")
    b = d["common_anchor_bridge"]
    print(f"  common-anchor bridge = {b['mean']:+.2f} [{b['ci_low']:+.2f}, {b['ci_high']:+.2f}]")

    if not g1["passed"]:
        report["verdict"] = "bridge-failed"
        print("\nverdict: bridge-failed — do NOT run the patched phase")
    elif args.patched:
        with open(os.path.join(args.dir, "g16_patched.json")) as handle:
            patched = json.load(handle)
        report.update(gates_2_to_5(baselines, patched, clusters, signs))
        print(f"\nqualifying (site, layer) cells: {len(report['qualifying'])}")
        if report["strongest"]:
            s = report["strongest"]
            print(f"strongest: {s['site']} L{s['layer']}  break {s['break']:+.2f}  "
                  f"rescue {s['rescue']:+.2f}  specificity "
                  f"{'ok' if s.get('specificity_ok') else 'FAIL'}  admit "
                  f"{'quiet' if s.get('admit_quiet') else 'NOISY'}")
        print(f"verdict: {report['verdict']}")
    else:
        print("\ngate 1 passed — patched phase may run "
              f"(items with |bridge| >= {GAP_FLOOR} will be patched)")

    out = os.path.join(args.dir, "g16_analysis.json")
    with open(out, "w") as handle:
        json.dump(report, handle, indent=1)
    print(f"wrote {os.path.relpath(out, ROOT)}")


if __name__ == "__main__":
    main()
