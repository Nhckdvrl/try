"""G17 analysis — frozen gates from PREREGISTRATION_G17_BINDING_BY_WEIGHT.md.

Does the binding requirement exist only at complete suppression, or at every
requested weight? If only at zero, the paper's two regularities are one.

    PYTHONPATH=src python3 src/analyze_g17.py
"""
from __future__ import annotations

import collections
import json
import os
import random
import statistics as st
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from schema import load_items  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SEED = 20260829
N_RESAMPLES = 10_000
WEIGHTS = ("w000", "w025", "w050")
MODELS = ("qwen3-8b", "gemma3-12b", "phi4-mini", "qwen35-27b")

RESCUE_FLOOR = 0.15      # gate 1
DELTA_FLOOR = 0.15       # gate 2
MIN_MODELS = 3           # gate 1


def cluster_of(item) -> str:
    if item.task_family == "legal_judgment":
        return "legal:" + item.meta["case"]
    return item.task_family + ":" + item.base_context[:60]


def clustered_ci(by_cluster: dict, seed: int = SEED):
    rng = random.Random(seed)
    keys = list(by_cluster)
    reps = []
    for _ in range(N_RESAMPLES):
        pool = []
        for _ in range(len(keys)):
            pool += by_cluster[keys[rng.randrange(len(keys))]]
        reps.append(st.fmean(pool))
    reps.sort()
    return reps[int(0.025 * N_RESAMPLES)], reps[int(0.975 * N_RESAMPLES)]


def summarise(pairs) -> dict:
    """pairs: iterable of (cluster_key, value)."""
    by = collections.defaultdict(list)
    for key, value in pairs:
        by[key].append(value)
    flat = [v for vs in by.values() for v in vs]
    if not flat:
        return {"n": 0, "mean": float("nan"), "ci_low": float("nan"),
                "ci_high": float("nan"), "n_clusters": 0}
    low, high = clustered_ci(by)
    return {"n": len(flat), "n_clusters": len(by), "mean": st.fmean(flat),
            "ci_low": low, "ci_high": high}


def rei_rows(items: dict, path: str):
    """One row per usable item: REI for each of the six crossed cells."""
    y = collections.defaultdict(dict)
    with open(path) as handle:
        for line in handle:
            rec = json.loads(line)
            if rec.get("value") not in (None, "None"):
                y[rec["item_id"]][rec["kind_name"]] = float(rec["value"])
    rows = []
    for item_id, cells in y.items():
        item = items.get(item_id)
        if item is None:
            continue
        need = ["g17_base", "g17_admit"] + [f"g17_{w}_{p}" for w in WEIGHTS
                                            for p in ("none", "para")]
        if any(k not in cells for k in need):
            continue
        s = 1.0 if item.critical_direction == "increase" else -1.0
        leverage = cells["g17_admit"] - cells["g17_base"]
        if s * leverage <= 0:
            continue
        rei = {c: s * (cells[c] - cells["g17_base"]) / abs(leverage) for c in need[2:]}
        rows.append({"item_id": item_id, "cluster": cluster_of(item), "rei": rei})
    return rows


def main() -> None:
    items = {i.item_id: i for i in load_items(os.path.join(ROOT, "data/items/items_v1.jsonl"))}
    report = {"design_tag": "g17-binding-by-weight-design-v1",
              "bootstrap": {"seed": SEED, "n_resamples": N_RESAMPLES},
              "per_model": {}, "pooled": {}}

    pooled_rescue = {w: [] for w in WEIGHTS}
    pooled_delta = []
    per_model_gate1 = []

    print(f"{'model':<14}{'n':>4}   " + "".join(f"{'rescue ' + w:>26}" for w in WEIGHTS))
    print("-" * 96)
    for tag in MODELS:
        path = os.path.join(ROOT, f"results/raw/{tag}_g17.jsonl")
        if not os.path.exists(path):
            print(f"{tag:<14}  (missing)")
            continue
        rows = rei_rows(items, path)
        entry = {"n": len(rows), "rescue": {}, "rei": {}}
        line = f"{tag:<14}{len(rows):>4}   "
        for w in WEIGHTS:
            resc = [(r["cluster"], r["rei"][f"g17_{w}_none"] - r["rei"][f"g17_{w}_para"])
                    for r in rows]
            stats = summarise(resc)
            entry["rescue"][w] = stats
            for arm in ("none", "para"):
                entry["rei"].setdefault(w, {})[arm] = summarise(
                    [(r["cluster"], r["rei"][f"g17_{w}_{arm}"]) for r in rows])
            pooled_rescue[w] += [(f"{tag}|{c}", v) for c, v in resc]
            line += f"{stats['mean']:>+8.3f} [{stats['ci_low']:+.3f},{stats['ci_high']:+.3f}]"
        print(line)
        delta = [(r["cluster"],
                  (r["rei"]["g17_w000_none"] - r["rei"]["g17_w000_para"])
                  - ((r["rei"]["g17_w025_none"] - r["rei"]["g17_w025_para"])
                     + (r["rei"]["g17_w050_none"] - r["rei"]["g17_w050_para"])) / 2)
                 for r in rows]
        entry["delta"] = summarise(delta)
        pooled_delta += [(f"{tag}|{c}", v) for c, v in delta]
        g1 = entry["rescue"]["w000"]
        entry["gate1_pass"] = g1["mean"] >= RESCUE_FLOOR and g1["ci_low"] > 0
        per_model_gate1.append(entry["gate1_pass"])
        report["per_model"][tag] = entry

    print("-" * 96)
    line = f"{'POOLED':<14}{'':>4}   "
    for w in WEIGHTS:
        stats = summarise(pooled_rescue[w])
        report["pooled"].setdefault("rescue", {})[w] = stats
        line += f"{stats['mean']:>+8.3f} [{stats['ci_low']:+.3f},{stats['ci_high']:+.3f}]"
    print(line)

    delta_stats = summarise(pooled_delta)
    report["pooled"]["delta"] = delta_stats
    print(f"\ninteraction  Delta = rescue(0) - mean[rescue(.25), rescue(.50)] = "
          f"{delta_stats['mean']:+.3f} [{delta_stats['ci_low']:+.3f}, "
          f"{delta_stats['ci_high']:+.3f}]")

    gate1 = sum(per_model_gate1)
    gate1_ok = gate1 >= MIN_MODELS
    gate2_ok = delta_stats["mean"] >= DELTA_FLOOR and delta_stats["ci_low"] > 0
    nonzero_null = all(
        report["pooled"]["rescue"][w]["ci_low"] <= 0 <= report["pooled"]["rescue"][w]["ci_high"]
        for w in ("w025", "w050"))

    if not gate1_ok:
        verdict = "no-rescue"
    elif not gate2_ok:
        verdict = "independent"
    elif nonzero_null:
        verdict = "unified"
    else:
        verdict = "partial"

    report["gates"] = {"gate1_models_passing": gate1, "gate1_pass": gate1_ok,
                       "gate2_pass": gate2_ok, "nonzero_levels_null": nonzero_null}
    report["verdict"] = verdict
    print(f"\ngate1 {gate1}/{len(per_model_gate1)} models  gate2 {gate2_ok}  "
          f"non-zero levels null {nonzero_null}")
    print(f"VERDICT: {verdict}")

    out = os.path.join(ROOT, "results/g17_binding_by_weight_analysis.json")
    with open(out, "w") as handle:
        json.dump(report, handle, indent=1)
    print(f"wrote {os.path.relpath(out, ROOT)}")


if __name__ == "__main__":
    main()
