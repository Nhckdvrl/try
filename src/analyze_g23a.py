"""G23A analysis — estimand and gates frozen in PREREGISTRATION_G23A_ZERO_GATING.md.

Everything is in **raw sign-aligned rating points**. No REI, no leverage-normalised
ratio, no trimming, no winsorisation: G17's ratio destroyed its own intervals and
Stage 3E had already solved the same failure by moving to raw points.

    ResInf(arm, w) = s · [ Y(g23a_<arm>_<w>) − Y(g23a_base) ]
    Gap(w)         = ResInf(pre, w) − ResInf(post, w)
    Δ_zero         = Gap(w000) − mean[ Gap(w001), Gap(w025), Gap(w050) ]

`Gap(w)` is the evidence influence still reaching the judgment when the rule is
stated before the evidence, minus the same influence when the rule follows it.
Positive = the prospective statement of the rule loses more of the evidence's
effect than the retrospective one, i.e. the G0 reversal at that requested weight.

Scope of the primary contrast (v3 semantic freeze): `Δ_zero` identifies a
**discontinuity at the zero-valued instruction** — that complete exclusion carries an
extra prospective timing cost *relative to non-zero weight instructions*. It does **not**
establish that the non-zero arms behaviourally implemented their requested weights:
the numeric probe only shows the model can state which weight was requested
(`requested_weight_access_ok`), and `TargetDeviation` is a descriptor that cannot alone
prove linear execution (`ResInf(w) = w·Leverage` assumes rating points are linear in
evidential weight, which natural judgment need not be).

Inference: cluster bootstrap over independent skeletons, seed 20260923, 10,000
resamples, percentile intervals. Per-model analyses cluster by skeleton; pooled analysis
also clusters by skeleton, keeping all model observations for the same item together.

    PYTHONPATH=src python3 src/analyze_g23a.py
"""
from __future__ import annotations

import collections
import json
import os
import random
import statistics as st
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from conditions_g23a import (ARMS, G23A_CONDITIONS, G23A_NUMERIC_PROBES,  # noqa: E402
                              G23A_RULE_PROBES, NONZERO_WKEYS, WKEYS)
from schema import load_items  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SEED = 20260923
N_RESAMPLES = 10_000
MODELS = ("qwen3-8b", "gemma3-12b", "mistral-small-24b")

DELTA_FLOOR = 3.0            # rating points, same pooled floor G18 used
MIN_MODELS_POSITIVE = 2      # of 3
PROBE_TOL_PP = 2.0           # stated weight within 2 percentage points of requested
WEIGHT_FRACTION = {"w000": 0.0, "w001": 0.01, "w025": 0.25,
                   "w050": 0.50, "w100": 1.00}
ATTEN_WKEYS = ("w001", "w025", "w050")


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
    """Mean over (cluster, value) pairs with a cluster bootstrap interval."""
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


# ---------------------------------------------------------------------------
# Row construction and the frozen exclusion criteria
# ---------------------------------------------------------------------------
REQUIRED = list(G23A_CONDITIONS)


def rows_for(items: dict, path: str):
    """One row per item that survives both frozen exclusions.

    E1  complete case: all 12 decision cells present and parseable.
    E2  positive signed leverage: s · [Y(norule) − Y(base)] > 0, i.e. the evidence
        moves the rating in its own direction when no rule is present. This is the
        project's standing criterion; without it an item has no influence to gate.

    Nothing else is ever excluded, and no value is transformed or capped.
    """
    y = collections.defaultdict(dict)
    with open(path) as handle:
        for line in handle:
            rec = json.loads(line)
            if rec.get("value") not in (None, "None"):
                y[rec["item_id"]][rec["kind_name"]] = rec["value"]

    rows, drops = [], collections.Counter()
    for item_id, cells in y.items():
        item = items.get(item_id)
        if item is None:
            drops["unknown_item"] += 1
            continue
        missing = [k for k in REQUIRED if k not in cells]
        if missing:
            drops["incomplete"] += 1
            continue
        s = 1.0 if item.critical_direction == "increase" else -1.0
        y0, yE = cells["g23a_base"], cells["g23a_norule"]
        leverage = s * (yE - y0)
        if leverage <= 0:
            drops["nonpositive_leverage"] += 1
            continue

        resinf = {(arm, w): s * (cells[f"g23a_{arm}_{w}"] - y0)
                  for w in WKEYS for arm in ARMS}
        gap = {w: resinf[("pre", w)] - resinf[("post", w)] for w in WKEYS}
        delta = gap["w000"] - st.fmean(gap[w] for w in ATTEN_WKEYS)
        target_dev = {
            (arm, w): resinf[(arm, w)] - WEIGHT_FRACTION[w] * leverage
            for w in WKEYS for arm in ARMS
        }
        rows.append({
            "item_id": item_id, "cluster": item.meta["skeleton"],
            "family": item.task_family, "direction": item.critical_direction,
            "leverage": leverage, "resinf": resinf, "gap": gap,
            "gap_atten": st.fmean(gap[w] for w in ATTEN_WKEYS),
            "target_dev": target_dev,
            "delta": delta,
        })
    return rows, drops


def probes_for(path: str) -> dict:
    """Policy-access descriptors: stated weights and the yes/no permission probes."""
    stated = collections.defaultdict(dict)   # (wkey, arm) -> {item_id: value}
    yesno = collections.defaultdict(list)    # probe -> [p_yes]
    with open(path) as handle:
        for line in handle:
            rec = json.loads(line)
            k = rec.get("kind_name", "")
            if k in G23A_NUMERIC_PROBES and rec.get("value") is not None:
                _, _, arm, wkey = k.split("_")
                stated[(wkey, arm)][rec["item_id"]] = float(rec["value"])
            elif k in G23A_RULE_PROBES and rec.get("p_yes") is not None:
                yesno[k].append(float(rec["p_yes"]))

    weights = {}
    for wkey in WKEYS:
        errs, within = [], 0
        target = WEIGHT_FRACTION[wkey] * 100.0
        for arm in ARMS:
            for value in stated.get((wkey, arm), {}).values():
                errs.append(abs(value - target))
                within += abs(value - target) <= PROBE_TOL_PP
        if errs:
            weights[wkey] = {"n": len(errs),
                             "median_abs_error_pp": st.median(errs),
                             "frac_within_tol": within / len(errs)}
    return {"stated_weight": weights,
            "permission_yes": {k: {"n": len(v), "mean_p_yes": st.fmean(v)}
                               for k, v in sorted(yesno.items())}}


def verdict_for(delta: dict, nonzero: dict, positive_models: int,
                n_models: int) -> str:
    """The frozen five-way decision rule of PREREGISTRATION_G23A_ZERO_GATING §7."""
    gate_ci = delta["ci_low"] > 0
    gate_floor = delta["mean"] >= DELTA_FLOOR
    gate_models = positive_models >= MIN_MODELS_POSITIVE
    if gate_ci and gate_floor:
        return "zero-amplified" if gate_models else "model-dependent"
    if gate_ci:
        return "sub-threshold"
    return "smooth-timing" if nonzero["ci_low"] > 0 else "no-replication"


def _fmt(stats: dict, width: int = 9) -> str:
    if not stats["n"]:
        return f"{'—':>{width}}"
    return f"{stats['mean']:>+{width}.2f}"


def _ci(stats: dict) -> str:
    return f"[{stats['ci_low']:+.2f}, {stats['ci_high']:+.2f}]"


def main() -> None:
    items = {i.item_id: i for i in load_items(os.path.join(ROOT, "data/items/g23a_v1.jsonl"))}
    report = {"design_tag": "g23a-zero-gating-design-v3",
              "estimand": "Gap(w) and Δ_zero in raw sign-aligned rating points",
              "exclusions": ["complete case: all 12 decision cells present",
                             "signed leverage s·[Y(norule) − Y(base)] > 0"],
              "bootstrap": {"seed": SEED, "n_resamples": N_RESAMPLES,
                            "cluster": "independent skeleton; pooled keeps models sharing a skeleton together"},
              "claim_scope": "discontinuity at the zero-valued instruction relative to "
                             "non-zero weight instructions; does not establish that the "
                             "non-zero arms behaviourally implemented their weights",
              "targetdev_status": "descriptive only: raw-point deviation from w·Leverage; "
                                  "assumes linearity of rating points in evidential weight "
                                  "and never gates the verdict",
              "per_model": {}, "pooled": {}, "drops": {}}

    pooled = {k: [] for k in
              (["leverage"] + [f"resinf_{a}_{w}" for w in WKEYS for a in ARMS]
               + [f"gap_{w}" for w in WKEYS]
               + [f"targetdev_{a}_{w}" for w in WKEYS for a in ARMS]
               + [f"abstargetdev_{a}_{w}" for w in WKEYS for a in ARMS]
               + ["gap_atten", "delta"])}
    positive_models = 0
    model_delta = {}

    head_w = "".join(f"{w:>10}" for w in WKEYS)
    print("Gap(w) — rating points of evidence influence LOST when the rule moves")
    print("from after the evidence to before it. Positive = the G0 reversal.")
    print(f"{'model':<20}{'n':>4}{head_w}{'Δ_zero':>14}")
    print("-" * (24 + 10 * len(WKEYS) + 14))

    for tag in MODELS:
        path = os.path.join(ROOT, f"results/raw/{tag}_g23a.jsonl")
        if not os.path.exists(path):
            print(f"{tag:<20}  (missing)")
            continue
        rows, drops = rows_for(items, path)
        report["drops"][tag] = dict(drops)
        entry = {"n": len(rows), "drops": dict(drops), "gap": {}, "resinf": {},
                 "target_deviation": {}, "abs_target_deviation": {}}

        line = f"{tag:<20}{len(rows):>4}"
        for w in WKEYS:
            g = [(r["cluster"], r["gap"][w]) for r in rows]
            entry["gap"][w] = summarise(g)
            pooled[f"gap_{w}"] += [(c, v) for c, v in g]
            line += f"{entry['gap'][w]['mean']:>+10.2f}"
        for w in WKEYS:
            for arm in ARMS:
                rr = [(r["cluster"], r["resinf"][(arm, w)]) for r in rows]
                entry["resinf"][f"{arm}_{w}"] = summarise(rr)
                pooled[f"resinf_{arm}_{w}"] += [(c, v) for c, v in rr]
                td = [(r["cluster"], r["target_dev"][(arm, w)]) for r in rows]
                atd = [(cluster, abs(v)) for cluster, v in td]
                entry["target_deviation"][f"{arm}_{w}"] = summarise(td)
                entry["abs_target_deviation"][f"{arm}_{w}"] = summarise(atd)
                pooled[f"targetdev_{arm}_{w}"] += [(c, v) for c, v in td]
                pooled[f"abstargetdev_{arm}_{w}"] += [(c, v) for c, v in atd]
        entry["gap_atten"] = summarise([(r["cluster"], r["gap_atten"]) for r in rows])
        entry["leverage"] = summarise([(r["cluster"], r["leverage"]) for r in rows])
        entry["delta"] = summarise([(r["cluster"], r["delta"]) for r in rows])
        pooled["gap_atten"] += [(r["cluster"], r["gap_atten"]) for r in rows]
        pooled["delta"] += [(r["cluster"], r["delta"]) for r in rows]
        pooled["leverage"] += [(r["cluster"], r["leverage"]) for r in rows]
        model_delta[tag] = entry["delta"]
        positive_models += entry["delta"]["mean"] > 0
        report["per_model"][tag] = entry
        report["per_model"][tag]["probes"] = probes_for(path)
        line += f"{entry['delta']['mean']:>+9.2f}"
        print(line)

    print("-" * (24 + 10 * len(WKEYS) + 14))
    line = f"{'POOLED':<20}{sum(report['per_model'][t]['n'] for t in report['per_model']):>4}"
    pooled_stats = {}
    for w in WKEYS:
        s = summarise(pooled[f"gap_{w}"])
        pooled_stats[f"gap_{w}"] = s
        line += f"{s['mean']:>+10.2f}"
    delta_stats = summarise(pooled["delta"])
    nonzero_stats = summarise(pooled["gap_atten"])
    pooled_stats["delta"] = delta_stats
    pooled_stats["gap_atten"] = nonzero_stats
    pooled_stats["leverage"] = summarise(pooled["leverage"])
    pooled_stats["resinf"] = {k: summarise(pooled[f"resinf_{k}"])
                              for w in WKEYS for k in (f"pre_{w}", f"post_{w}")}
    pooled_stats["target_deviation"] = {
        k: summarise(pooled[f"targetdev_{k}"])
        for w in WKEYS for k in (f"pre_{w}", f"post_{w}")
    }
    pooled_stats["abs_target_deviation"] = {
        k: summarise(pooled[f"abstargetdev_{k}"])
        for w in WKEYS for k in (f"pre_{w}", f"post_{w}")
    }
    print(line + f"{delta_stats['mean']:>+9.2f}")
    report["pooled"] = pooled_stats

    print("\npooled, decomposed — how much of the evidence still reaches the judgment")
    print(f"  {'w':<7}{'ResInf(pre)':>14}{'ResInf(post)':>14}{'Gap(w)':>22}")
    for w in WKEYS:
        pre = pooled_stats["resinf"][f"pre_{w}"]
        post = pooled_stats["resinf"][f"post_{w}"]
        g = pooled_stats[f"gap_{w}"]
        print(f"  {w:<7}{_fmt(pre, 14)}{_fmt(post, 14)}   {g['mean']:>+8.2f} {_ci(g)}")
    print(f"\n  mean signed leverage (evidence's own pull, no rule): "
          f"{pooled_stats['leverage']['mean']:+.2f}")
    print(f"  Gap over non-zero weight instructions 1/25/50: {nonzero_stats['mean']:+.2f} "
          f"{_ci(nonzero_stats)}")
    print("\n  raw target-deviation diagnostic — |ResInf - requested_fraction * leverage|")
    print(f"  {'w':<7}{'PRE MAE':>12}{'POST MAE':>12}")
    for w in WKEYS:
        pre = pooled_stats["abs_target_deviation"][f"pre_{w}"]
        post = pooled_stats["abs_target_deviation"][f"post_{w}"]
        print(f"  {w:<7}{pre['mean']:>12.2f}{post['mean']:>12.2f}")

    # ---- frozen gates -----------------------------------------------------
    gate_ci = delta_stats["ci_low"] > 0
    gate_floor = delta_stats["mean"] >= DELTA_FLOOR
    gate_models = positive_models >= MIN_MODELS_POSITIVE
    verdict = verdict_for(delta_stats, nonzero_stats, positive_models,
                          len(model_delta))
    report["gates"] = {
        "gate_ci_delta_gt_0": gate_ci,
        "gate_floor": gate_floor,
        "floor_points": DELTA_FLOOR,
        "models_positive": positive_models,
        "n_models": len(model_delta),
        "gate_models": gate_models,
    }
    report["verdict"] = verdict

    print(f"\nΔ_zero = {delta_stats['mean']:+.2f} {_ci(delta_stats)}   "
          f"(floor {DELTA_FLOOR}, {delta_stats['n_clusters']} clusters, seed {SEED})")
    print(f"gate 1a (CI low > 0): {gate_ci}   "
          f"gate 1b (≥ {DELTA_FLOOR} points): {gate_floor}   "
          f"gate 2 (≥ {MIN_MODELS_POSITIVE}/{len(model_delta)} models positive): {gate_models}")
    print(f"VERDICT: {verdict}")

    # ---- requested-weight access descriptor (Outcome D) --------------------
    # This table shows the model can *state* which weight was requested. It is not
    # evidence that behaviour implemented that weight; see TargetDeviation below.
    print("\nrequested-weight access — stated weight vs requested weight "
          "(pooled over both orders)")
    print(f"  {'w':<7}{'n':>5}{'median |error| (pp)':>22}{'within ±2 pp':>15}")
    access_ok = True
    probe_report = {}
    for tag in MODELS:
        p = report["per_model"].get(tag, {}).get("probes")
        if not p:
            continue
        probe_report[tag] = p
    for wkey in WKEYS:
        errs, within, n = [], 0, 0
        for tag in probe_report:
            s = probe_report[tag]["stated_weight"].get(wkey)
            if not s:
                continue
            errs.append(s["median_abs_error_pp"])
            within += s["frac_within_tol"] * s["n"]
            n += s["n"]
        if not n:
            continue
        med = st.median(errs)
        access_ok = access_ok and med <= PROBE_TOL_PP
        print(f"  {wkey:<7}{int(n):>5}{med:>22.1f}{within / n:>15.2f}")
    report["requested_weight_access_ok"] = access_ok

    print("\nyes/no permission probes (mean P(YES); w=0 should be NO, w=100 YES)")
    for tag, p in probe_report.items():
        cells = "  ".join(f"{k.replace('rule_probe_g23a_', '')}="
                          f"{v['mean_p_yes']:.2f}"
                          for k, v in p["permission_yes"].items())
        print(f"  {tag:<20}{cells}")

    if verdict in ("zero-amplified", "model-dependent") and access_ok:
        print("\nDISSOCIATION (Outcome D): explicit policy access / requested-weight "
              "recall coexists with a timing gap that only zero shows —\n  "
              "explicit policy access / requested-weight recall ≠ causal enforcement "
              "at w = 0.\n  The probe shows the model knows which numerical policy was "
              "requested, not that behaviour\n  quantitatively implements it; "
              "behavioural implementation is reported separately as the\n  descriptive "
              "TargetDeviation.")
    report["dissociation_outcome_D"] = bool(
        verdict in ("zero-amplified", "model-dependent") and access_ok)

    out = os.path.join(ROOT, "results/g23a_zero_gating_analysis.json")
    with open(out, "w") as handle:
        json.dump(report, handle, indent=1)
    print(f"\nwrote {os.path.relpath(out, ROOT)}")


if __name__ == "__main__":
    main()
