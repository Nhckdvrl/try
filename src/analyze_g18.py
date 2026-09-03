"""G18 analysis — frozen gates from PREREGISTRATION_G18_SEMANTIC_TARGETING.md.

    ExclusionEffect(level) = marg(level, no rule) − marg(level, exclude)

in raw sign-aligned rating points, each level scored against its own preview-only
baseline. No ratio is computed anywhere.

    PYTHONPATH=src python3 src/analyze_g18.py
"""
from __future__ import annotations

import collections
import json
import os
import random
import statistics as st
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from conditions_g18 import LEVELS  # noqa: E402
from schema import load_items  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SEED = 20260829
N_RESAMPLES = 10_000
MODELS = ("qwen3-8b", "gemma3-12b", "phi4-mini", "qwen35-27b", "mistral-small-24b")
SEMANTIC = ("para", "entail")
NONSEMANTIC = ("ident", "empty", "unrel")
DELTA_FLOOR = 3.0
MIN_MODELS_POSITIVE = 4


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
    by = collections.defaultdict(list)
    for key, value in pairs:
        by[key].append(value)
    flat = [v for vs in by.values() for v in vs]
    if not flat:
        return {"n": 0, "n_clusters": 0, "mean": float("nan"),
                "ci_low": float("nan"), "ci_high": float("nan")}
    low, high = clustered_ci(by)
    return {"n": len(flat), "n_clusters": len(by), "mean": st.fmean(flat),
            "ci_low": low, "ci_high": high}


def rows_for(items: dict, path: str):
    y = collections.defaultdict(dict)
    with open(path) as handle:
        for line in handle:
            rec = json.loads(line)
            if rec.get("value") not in (None, "None"):
                y[rec["item_id"]][rec["kind_name"]] = float(rec["value"])
    rows = []
    need = [f"g18_{lv}_{rs}" for lv in LEVELS for rs in ("only", "norule", "excl")]
    for item_id, cells in y.items():
        item = items.get(item_id)
        if item is None or any(k not in cells for k in need):
            continue
        s = 1.0 if item.critical_direction == "increase" else -1.0
        marg_norule, marg_excl, effect = {}, {}, {}
        for lv in LEVELS:
            base = cells[f"g18_{lv}_only"]
            marg_norule[lv] = s * (cells[f"g18_{lv}_norule"] - base)
            marg_excl[lv] = s * (cells[f"g18_{lv}_excl"] - base)
            effect[lv] = marg_norule[lv] - marg_excl[lv]
        rows.append({"item_id": item_id, "cluster": item.meta["skeleton"],
                     "family": item.task_family, "marg_norule": marg_norule,
                     "marg_excl": marg_excl, "effect": effect})
    return rows


def main() -> None:
    items = {i.item_id: i for i in load_items(os.path.join(ROOT, "data/items/g18_v1.jsonl"))}
    report = {"design_tag": "g18-semantic-targeting-design-v1",
              "estimand": "ExclusionEffect in raw sign-aligned rating points",
              "bootstrap": {"seed": SEED, "n_resamples": N_RESAMPLES},
              "per_model": {}, "pooled": {}}

    pooled_effect = {lv: [] for lv in LEVELS}
    pooled_marg = {lv: [] for lv in LEVELS}
    pooled_excl = {lv: [] for lv in LEVELS}
    pooled_delta, pooled_para_empty = [], []
    signs = []

    header = f"{'model':<20}{'n':>4}  " + "".join(f"{lv:>10}" for lv in LEVELS) + f"{'Δ_sem':>12}"
    print("ExclusionEffect — rating points the RULE removes, per-preview baseline")
    print(header)
    print("-" * len(header))
    for tag in MODELS:
        path = os.path.join(ROOT, f"results/raw/{tag}_g18.jsonl")
        if not os.path.exists(path):
            print(f"{tag:<20}  (missing)")
            continue
        rows = rows_for(items, path)
        entry = {"n": len(rows), "exclusion_effect": {}, "marg_norule": {},
                 "marg_excl": {}}
        line = f"{tag:<20}{len(rows):>4}  "
        for lv in LEVELS:
            e = [(r["cluster"], r["effect"][lv]) for r in rows]
            m = [(r["cluster"], r["marg_norule"][lv]) for r in rows]
            entry["exclusion_effect"][lv] = summarise(e)
            entry["marg_norule"][lv] = summarise(m)
            x = [(r["cluster"], r["marg_excl"][lv]) for r in rows]
            entry["marg_excl"][lv] = summarise(x)
            pooled_excl[lv] += [(f"{tag}|{c}", v) for c, v in x]
            pooled_effect[lv] += [(f"{tag}|{c}", v) for c, v in e]
            pooled_marg[lv] += [(f"{tag}|{c}", v) for c, v in m]
            line += f"{entry['exclusion_effect'][lv]['mean']:>10.2f}"
        delta = [(r["cluster"],
                  st.fmean(r["effect"][l] for l in SEMANTIC)
                  - st.fmean(r["effect"][l] for l in NONSEMANTIC)) for r in rows]
        entry["delta_semantic"] = summarise(delta)
        pooled_delta += [(f"{tag}|{c}", v) for c, v in delta]
        signs.append(entry["delta_semantic"]["mean"] > 0)
        pe = [(r["cluster"], r["effect"]["para"] - r["effect"]["empty"]) for r in rows]
        entry["para_minus_empty"] = summarise(pe)
        pooled_para_empty += [(f"{tag}|{c}", v) for c, v in pe]
        line += f"{entry['delta_semantic']['mean']:>+12.2f}"
        print(line)
        report["per_model"][tag] = entry

    print("-" * len(header))
    line = f"{'POOLED':<20}{'':>4}  "
    for lv in LEVELS:
        s = summarise(pooled_effect[lv])
        report["pooled"].setdefault("exclusion_effect", {})[lv] = s
        report["pooled"].setdefault("marg_norule", {})[lv] = summarise(pooled_marg[lv])
        report["pooled"].setdefault("marg_excl", {})[lv] = summarise(pooled_excl[lv])
        line += f"{s['mean']:>10.2f}"
    delta_stats = summarise(pooled_delta)
    report["pooled"]["delta_semantic"] = delta_stats
    report["pooled"]["para_minus_empty"] = summarise(pooled_para_empty)
    print(line + f"{delta_stats['mean']:>+12.2f}")

    print("\npooled, decomposed — how many points the later evidence moves the rating")
    print(f"  {'level':<8}{'marg(no rule)':>15}{'marg(exclude)':>15}"
          f"{'ExclusionEffect':>20}")
    for lv in LEVELS:
        s = report["pooled"]["exclusion_effect"][lv]
        m = report["pooled"]["marg_norule"][lv]
        x = report["pooled"]["marg_excl"][lv]
        print(f"  {lv:<8}{m['mean']:>+15.2f}{x['mean']:>+15.2f}"
              f"{s['mean']:>+13.2f} [{s['ci_low']:+.2f},{s['ci_high']:+.2f}]")

    pe = report["pooled"]["para_minus_empty"]
    print(f"\nΔ_semantic = {delta_stats['mean']:+.2f} "
          f"[{delta_stats['ci_low']:+.2f}, {delta_stats['ci_high']:+.2f}]  "
          f"(floor {DELTA_FLOOR}, {delta_stats['n_clusters']} clusters)")
    print(f"para − empty (length- and lexically-matched) = {pe['mean']:+.2f} "
          f"[{pe['ci_low']:+.2f}, {pe['ci_high']:+.2f}]")

    gate1 = delta_stats["mean"] >= DELTA_FLOOR and delta_stats["ci_low"] > 0
    gate2 = sum(signs) >= MIN_MODELS_POSITIVE
    verdict = "confirmed" if (gate1 and gate2) else ("partial" if gate1 else "not-confirmed")
    report["gates"] = {"gate1_pooled": gate1, "gate2_models_positive": sum(signs),
                       "gate2_pass": gate2, "n_models": len(signs)}
    report["verdict"] = verdict
    print(f"\ngate1 (pooled Δ ≥ {DELTA_FLOOR}, CI>0): {gate1}   "
          f"gate2 (≥{MIN_MODELS_POSITIVE}/5 positive): {sum(signs)}/{len(signs)}")
    print(f"VERDICT: {verdict}")

    out = os.path.join(ROOT, "results/g18_semantic_targeting_analysis.json")
    with open(out, "w") as handle:
        json.dump(report, handle, indent=1)
    print(f"wrote {os.path.relpath(out, ROOT)}")


if __name__ == "__main__":
    main()
