"""G23B analysis — estimands, carrier gate and branch logic frozen in
PREREGISTRATION_G23B_GATE_VS_CANCELLATION.md §§6–8.

Everything is in **raw sign-aligned rating points**. No ratio, no trimming, no
winsorisation: the reopened line's ratios destroyed their own intervals and
Stage 3E already solved that by moving to raw points.

Phase A — carrier qualification (prereg §6), cells B/P/E/PE, **no rule**:

    ProfferLeak = s · [Y(P)  − Y(B)]
    Leverage_U   = s · [Y(E)  − Y(B)]
    Leverage_K   = s · [Y(PE) − Y(P)]

    gate 1  pooled ProfferLeak 95% CI upper bound < +3.0
    gate 2  no model mean ProfferLeak >= +3.0
    gate 3  pooled mean Leverage_K > 0
    gate 4  Leverage_K > 0 in at least 2/3 model means

Phase B — branch test (prereg §7), rows need all 7 cells and E2/E3:

    Supp_U = s · [Y(E)  − Y(U)]          Supp_K = s · [Y(PE) − Y(K)]
    Supp_I = s · [Y(E)  − Y(I)]

    SemanticRescue        = Supp_K − Supp_U
    InstantiationPremium  = Supp_I − Supp_K
    RetrospectiveAdvantage = Supp_I − Supp_U   (sanity; = SR + IP exactly)

    PASS(X)          : pooled mean >= 3.0 AND pooled CI low > 0
                       AND mean(X) > 0 in >= 2/3 models
    WITHIN_FLOOR(X)  : pooled CI upper bound < +3.0

    carrier-invalid | branch-not-replicated | instantiation-dependent |
    hybrid | semantic-preactivation | unresolved        (prereg §8)

AUDIT FIX — FLAG 1 (prereg §6 ordering): gates 3/4 are computed on the E1
complete-case set, i.e. **before** E2/E3 are applied. Applying E3 first would
drop every item with Leverage_K <= 0 and make gates 3/4 true by construction
(the mean of strictly positive numbers is always > 0), turning two carrier
checks into tautologies. E2/E3 therefore define the Phase-B branch-analysis set,
where they do real work (an item with no influence to suppress cannot contribute
a Supp). The prereg text still carries the old ordering; it is amended at the
design tag after review. Flagged, not silent.

Inference: cluster bootstrap over independent skeletons, seed 20260923, 10,000
resamples, percentile intervals. Per-model analyses cluster by skeleton; pooled
analysis also clusters by skeleton, keeping all model observations for the same
skeleton together.

    PYTHONPATH=src python3 src/analyze_g23b.py             # Phase A
    PYTHONPATH=src python3 src/analyze_g23b.py --phase b    # Phase B
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import random
import statistics as st
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from conditions_g23b import PHASE_A, PHASE_B  # noqa: E402
from schema import load_items  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SEED = 20260923
N_RESAMPLES = 10_000
MODELS = ("qwen3-8b", "gemma3-12b", "mistral-small-24b")

FLOOR = 3.0                  # rating points, same raw-point floor as G18/G23A
MIN_MODELS_POSITIVE = 2      # of 3
DESIGN_TAG = "g23b-gate-vs-cancellation-design-v1"

CELLS_PHASE_A = [f"g23b_{c}" for c in ("b", "p", "e", "pe")]
CELLS_ALL = CELLS_PHASE_A + [f"g23b_{c}" for c in ("u", "k", "i")]


def phase_a_path(tag: str) -> str:
    return os.path.join(ROOT, f"results/raw/{tag}_g23b_phasea.jsonl")


def phase_b_path(tag: str) -> str:
    return os.path.join(ROOT, f"results/raw/{tag}_g23b_phaseb.jsonl")


# ---------------------------------------------------------------------------
# Estimation
# ---------------------------------------------------------------------------
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
# Row construction and the frozen exclusions
# ---------------------------------------------------------------------------
def _cells(path: str) -> dict:
    y = collections.defaultdict(dict)
    with open(path) as handle:
        for line in handle:
            rec = json.loads(line)
            if rec.get("value") not in (None, "None"):
                y[rec["item_id"]][rec["kind_name"]] = rec["value"]
    return y


def rows_phase_a(items: dict, paths: dict):
    """Phase-A rows: E1 (all four carrier cells present) only.

    The carrier gates run on this complete-case set — see the module docstring's
    FLAG-1 note on why E2/E3 are not applied here. Their per-item outcome is
    returned so the report can state what Phase B will exclude.
    """
    rows, drops = [], collections.Counter()
    for tag, path in paths.items():
        if not path or not os.path.exists(path):
            continue
        for item_id, cells in _cells(path).items():
            item = items.get(item_id)
            if item is None:
                drops[f"{tag}:unknown_item"] += 1
                continue
            missing = [k for k in CELLS_PHASE_A if k not in cells]
            if missing:
                drops[f"{tag}:incomplete"] += 1
                continue
            s = 1.0 if item.critical_direction == "increase" else -1.0
            yb, yp = cells["g23b_b"], cells["g23b_p"]
            ye, ype = cells["g23b_e"], cells["g23b_pe"]
            lev_u = s * (ye - yb)
            lev_k = s * (ype - yp)
            rows.append({
                "tag": tag, "item_id": item_id, "cluster": item.meta["skeleton"],
                "direction": item.critical_direction,
                "proffer_leak": s * (yp - yb),
                "leverage_u": lev_u, "leverage_k": lev_k,
                "e2_drop": not (lev_u > 0), "e3_drop": not (lev_k > 0),
            })
            if not lev_u > 0:
                drops[f"{tag}:would_drop_nonpositive_leverage_u"] += 1
            if not lev_k > 0:
                drops[f"{tag}:would_drop_nonpositive_leverage_k"] += 1
    return rows, drops


def rows_phase_b(items: dict, paths_a: dict, paths_b: dict):
    """Phase-B rows: E1 (all seven cells) AND E2 (Leverage_U > 0) AND
    E3 (Leverage_K > 0), computed from phase-A cells + phase-B cells."""
    rows, drops = [], collections.Counter()
    for tag in paths_b:                       # caller decides which models run
        pa, pb = paths_a.get(tag), paths_b.get(tag)
        if not pa or not os.path.exists(pa) or not pb or not os.path.exists(pb):
            drops[f"{tag}:missing_phase_file"] += 1
            continue
        cells_a, cells_b = _cells(pa), _cells(pb)
        for item_id in cells_b:
            item = items.get(item_id)
            if item is None:
                drops[f"{tag}:unknown_item"] += 1
                continue
            merged = dict(cells_a.get(item_id, {}))
            merged.update(cells_b[item_id])
            missing = [k for k in CELLS_ALL if k not in merged]
            if missing:
                drops[f"{tag}:incomplete"] += 1
                continue
            s = 1.0 if item.critical_direction == "increase" else -1.0
            yb, yp = merged["g23b_b"], merged["g23b_p"]
            ye, ype = merged["g23b_e"], merged["g23b_pe"]
            yu, yk, yi = merged["g23b_u"], merged["g23b_k"], merged["g23b_i"]
            lev_u, lev_k = s * (ye - yb), s * (ype - yp)
            if not lev_u > 0:
                drops[f"{tag}:nonpositive_leverage_u"] += 1
                continue
            if not lev_k > 0:
                drops[f"{tag}:nonpositive_leverage_k"] += 1
                continue
            supp_u = s * (ye - yu)
            supp_k = s * (ype - yk)
            supp_i = s * (ye - yi)
            rows.append({
                "tag": tag, "item_id": item_id, "cluster": item.meta["skeleton"],
                "direction": item.critical_direction,
                "supp_u": supp_u, "supp_k": supp_k, "supp_i": supp_i,
                "sem_rescue": supp_k - supp_u,
                "inst_prem": supp_i - supp_k,
                "retro_adv": supp_i - supp_u,
            })
    return rows, drops


# ---------------------------------------------------------------------------
# Frozen gates and the branch classification
# ---------------------------------------------------------------------------
def carrier_gate(pooled: dict, per_model: dict) -> dict:
    """The four aggregate carrier gates of prereg §6, on the E1 set (FLAG 1)."""
    proffer = pooled.get("proffer_leak", {})
    lev_k = pooled.get("leverage_k", {})
    model_proffer = [m.get("proffer_leak", {}) for m in per_model.values()]
    model_lev_k = [m.get("leverage_k", {}) for m in per_model.values()]
    gate1 = bool(proffer.get("ci_high", float("nan")) < FLOOR)
    gate2 = all(m.get("mean", float("nan")) < FLOOR for m in model_proffer)
    gate3 = bool(lev_k.get("mean", float("nan")) > 0)
    gate4 = sum(1 for m in model_lev_k if m.get("mean", float("nan")) > 0) \
        >= MIN_MODELS_POSITIVE
    return {
        "gate1_pooled_profferleak_ci_high_lt_floor": gate1,
        "gate2_no_model_mean_profferleak_ge_floor": gate2,
        "gate3_pooled_mean_leverage_k_gt_0": gate3,
        "gate4_leverage_k_positive_in_2_of_3_models": gate4,
        "floor_points": FLOOR,
        "n_models": len(model_proffer),
        "passed": gate1 and gate2 and gate3 and gate4,
    }


def pass_gate(stats: dict, per_model_means) -> bool:
    """PASS(X) of prereg §8."""
    return bool(stats.get("mean", float("nan")) >= FLOOR
                and stats.get("ci_low", float("nan")) > 0
                and sum(1 for m in per_model_means if m > 0) >= MIN_MODELS_POSITIVE)


def within_floor(stats: dict) -> bool:
    """WITHIN_FLOOR(X) of prereg §8."""
    return bool(stats.get("ci_high", float("nan")) < FLOOR)


LICENSED = {
    "instantiation-dependent":
        "Knowing exactly what the future evidence will say is not enough to "
        "recover retrospective exclusion; prior evidential instantiation adds a "
        "meaningful suppression advantage.",
    "hybrid":
        "Semantic preactivation helps prospective exclusion, but prior "
        "evidential instantiation adds a further independent advantage.",
    "semantic-preactivation":
        "Exact pre-rule semantic target information is sufficient to recover "
        "exclusion efficacy to within the preregistered meaningful margin of "
        "retrospective exclusion.",
    "unresolved":
        "No preregistered branch pattern was met after a valid carrier and a "
        "successful retrospective sanity check; no H-GATE/H-CANCEL verdict is "
        "forced.",
    "branch-not-replicated":
        "PASS(RetrospectiveAdvantage) failed: the U-vs-I phenomenon did not "
        "cleanly replicate in the new materials, so the branch interpretation "
        "is not promoted.",
    "carrier-invalid":
        "The Phase-A carrier gate failed; G23B stops before any U/K/I rule "
        "output is interpreted.",
}

CAUTION = {
    "semantic-preactivation":
        "Not proof of a standing gate: a non-evidential proffer may still "
        "preactivate evidence-like internal representations. The next step is "
        "late target resolution / control composition, not a cancellation sweep.",
    "instantiation-dependent":
        "Behavioural support for the retrospective-cancellation / "
        "evidence-state-revision account; it does not prove a specific internal "
        "cancellation circuit.",
}


def classify(carrier_ok: bool, pooled: dict, per_model: dict) -> str:
    """The frozen decision order of prereg §8."""
    if not carrier_ok:
        return "carrier-invalid"
    ra = pooled.get("retro_adv", {})
    sr = pooled.get("sem_rescue", {})
    ip = pooled.get("inst_prem", {})
    ra_means = [m.get("retro_adv", {}).get("mean", float("nan"))
                for m in per_model.values()]
    sr_means = [m.get("sem_rescue", {}).get("mean", float("nan"))
                for m in per_model.values()]
    ip_means = [m.get("inst_prem", {}).get("mean", float("nan"))
                for m in per_model.values()]
    if not pass_gate(ra, ra_means):
        return "branch-not-replicated"
    if pass_gate(ip, ip_means) and within_floor(sr):
        return "instantiation-dependent"
    if pass_gate(sr, sr_means) and pass_gate(ip, ip_means):
        return "hybrid"
    if pass_gate(sr, sr_means) and within_floor(ip):
        return "semantic-preactivation"
    return "unresolved"


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------
def _fmt(stats: dict, width: int = 10) -> str:
    if not stats or not stats.get("n"):
        return f"{'—':>{width}}"
    return f"{stats['mean']:>+{width}.2f}"


def _ci(stats: dict) -> str:
    return f"[{stats['ci_low']:+.2f}, {stats['ci_high']:+.2f}]"


def _gather(rows, keys):
    """{key: [(cluster, value)]} pooled, plus per-model copies."""
    pooled = {k: [] for k in keys}
    per_model = collections.defaultdict(lambda: {k: [] for k in keys})
    for r in rows:
        for k in keys:
            pooled[k].append((r["cluster"], r[k]))
            per_model[r["tag"]][k].append((r["cluster"], r[k]))
    return pooled, per_model


def _stats(pairs_by_key) -> dict:
    return {k: summarise(v) for k, v in pairs_by_key.items()}


def _base_report(phase: str) -> dict:
    return {
        "design_tag": DESIGN_TAG,
        "phase": phase,
        "estimand": ("raw sign-aligned rating points; no ratio, no trimming, "
                     "no winsorisation"),
        "bootstrap": {"seed": SEED, "n_resamples": N_RESAMPLES,
                      "cluster": ("independent skeleton; pooled keeps models "
                                  "sharing a skeleton together")},
        "floor_points": FLOOR,
        "exclusions": ("E1 complete case for the executed phase; "
                       "E2 Leverage_U > 0; E3 Leverage_K > 0 "
                       "(E2/E3 define the Phase-B branch set; the Phase-A "
                       "carrier gates run on E1 — FLAG-1)"),
        "per_model": {}, "drops": {}, "models_missing": [],
    }


def phase_a(items: dict, report: dict) -> tuple:
    paths = {t: phase_a_path(t) for t in MODELS}
    present = [t for t in MODELS if os.path.exists(paths[t])]
    report["models_missing"] = [t for t in MODELS if t not in present]
    rows, drops = rows_phase_a(items, paths)
    for t in MODELS:
        report["drops"][t] = {k.split(":", 1)[1]: v for k, v in drops.items()
                              if k.startswith(f"{t}:")}

    keys = ("proffer_leak", "leverage_u", "leverage_k")
    pooled_pairs, model_pairs = _gather(rows, keys)
    pooled_stats, model_stats = _stats(pooled_pairs), {}
    for t in present:
        model_stats[t] = _stats(model_pairs.get(t, {k: [] for k in keys}))
        model_stats[t]["n"] = sum(1 for r in rows if r["tag"] == t)
        report["per_model"][t] = model_stats[t]
    report["pooled"] = pooled_stats

    head = f"{'model':<20}{'n':>4}{'ProfferLeak':>14}{'Leverage_U':>13}{'Leverage_K':>13}"
    print("Phase A — carrier qualification (no exclusion rule anywhere)")
    print(f"  cells: {' / '.join(CELLS_PHASE_A)}   (s = +1 increase, -1 decrease)")
    print(head)
    print("-" * len(head))
    for t in present:
        m = model_stats[t]
        print(f"{t:<20}{m['proffer_leak']['n']:>4}"
              f"{_fmt(m['proffer_leak'], 14)}{_fmt(m['leverage_u'], 13)}"
              f"{_fmt(m['leverage_k'], 13)}")
    print("-" * len(head))
    print(f"{'POOLED':<20}{pooled_stats['proffer_leak']['n']:>4}"
          f"{_fmt(pooled_stats['proffer_leak'], 14)}"
          f"{_fmt(pooled_stats['leverage_u'], 13)}"
          f"{_fmt(pooled_stats['leverage_k'], 13)}")

    gates = carrier_gate(pooled_stats, model_stats)
    report["carrier_gates"] = gates
    print(f"\ncarrier gates (floor {FLOOR}, cluster bootstrap, seed {SEED})")
    print(f"  gate 1  pooled ProfferLeak CI high < +{FLOOR} : "
          f"{gates['gate1_pooled_profferleak_ci_high_lt_floor']}  "
          f"({_ci(pooled_stats['proffer_leak'])})")
    worst = max((m["proffer_leak"]["mean"] for m in model_stats.values()
                 if m["proffer_leak"]["n"]), default=float("nan"))
    print(f"  gate 2  no model mean ProfferLeak >= +{FLOOR} : "
          f"{gates['gate2_no_model_mean_profferleak_ge_floor']}  (max {worst:+.2f})")
    print(f"  gate 3  pooled mean Leverage_K > 0        : "
          f"{gates['gate3_pooled_mean_leverage_k_gt_0']}  "
          f"({_fmt(pooled_stats['leverage_k'])})")
    pos = sum(1 for m in model_stats.values() if m["leverage_k"]["n"]
              and m["leverage_k"]["mean"] > 0)
    print(f"  gate 4  Leverage_K > 0 in >= 2/3 models   : "
          f"{gates['gate4_leverage_k_positive_in_2_of_3_models']}  ({pos}/{gates['n_models']})")
    print(f"CARRIER GATE: {'PASS — Phase B may run' if gates['passed'] else 'FAIL — G23B stops (carrier-invalid)'}")

    would = {t: {k.split(':', 1)[1]: v for k, v in drops.items()
                 if k.startswith(f"{t}:would_drop")}
             for t in MODELS}
    report["branch_set_would_drop"] = would
    print("\nPhase-B branch-set exclusions E2/E3 (counted now, applied in Phase B):")
    for t in present:
        w = would[t]
        print(f"  {t:<20} E2 nonpositive Leverage_U: "
              f"{w.get('would_drop_nonpositive_leverage_u', 0)}   "
              f"E3 nonpositive Leverage_K: "
              f"{w.get('would_drop_nonpositive_leverage_k', 0)}")
    if report["models_missing"]:
        print(f"  MISSING (reported by name, not substituted): {report['models_missing']}")
    return rows, model_stats, pooled_stats


def phase_b(items: dict, report: dict) -> tuple:
    rows_a, _ = rows_phase_a(items, {t: phase_a_path(t) for t in MODELS})
    present_a = sorted({r["tag"] for r in rows_a})
    paths_b = {t: phase_b_path(t) for t in MODELS}
    present_b = [t for t in MODELS if os.path.exists(paths_b[t])]
    report["models_missing"] = ([t for t in MODELS if t not in present_a]
                                + [t for t in MODELS if t in present_a
                                   and t not in present_b])
    rows, drops = rows_phase_b(items, {t: phase_a_path(t) for t in MODELS},
                               paths_b)
    for t in MODELS:
        report["drops"][t] = {k.split(":", 1)[1]: v for k, v in drops.items()
                              if k.startswith(f"{t}:")}

    # the carrier gate must still hold, recomputed from the Phase-A files
    keys_a = ("proffer_leak", "leverage_u", "leverage_k")
    pooled_a, model_pairs_a = _gather(rows_a, keys_a)
    pooled_stats_a = _stats(pooled_a)
    model_stats_a = {t: _stats(model_pairs_a.get(t, {k: [] for k in keys_a}))
                     for t in present_a}
    gates = carrier_gate(pooled_stats_a, model_stats_a)
    report["carrier_gates"] = gates

    keys = ("supp_u", "supp_k", "supp_i", "sem_rescue", "inst_prem", "retro_adv")
    pooled_pairs, model_pairs = _gather(rows, keys)
    pooled_stats, model_stats = _stats(pooled_pairs), {}
    present = [t for t in MODELS if any(r["tag"] == t for r in rows)]
    for t in present:
        model_stats[t] = _stats(model_pairs.get(t, {k: [] for k in keys}))
        model_stats[t]["n"] = sum(1 for r in rows if r["tag"] == t)
        report["per_model"][t] = model_stats[t]
    report["pooled"] = pooled_stats

    head = (f"{'model':<20}{'n':>4}{'Supp_U':>10}{'Supp_K':>10}{'Supp_I':>10}"
            f"{'SemRescue':>12}{'InstPrem':>11}{'RetroAdv':>11}")
    print("Phase B — branch test (U / K / I rule cells)")
    print(f"  cells: {' / '.join(CELLS_ALL)}   (rows need all 7 + E2 + E3)")
    print(head)
    print("-" * len(head))
    for t in present:
        m = model_stats[t]
        print(f"{t:<20}{m['n']:>4}{_fmt(m['supp_u'])}{_fmt(m['supp_k'])}"
              f"{_fmt(m['supp_i'])}{_fmt(m['sem_rescue'], 12)}"
              f"{_fmt(m['inst_prem'], 11)}{_fmt(m['retro_adv'], 11)}")
    print("-" * len(head))
    print(f"{'POOLED':<20}{pooled_stats['supp_u']['n']:>4}"
          f"{_fmt(pooled_stats['supp_u'])}{_fmt(pooled_stats['supp_k'])}"
          f"{_fmt(pooled_stats['supp_i'])}{_fmt(pooled_stats['sem_rescue'], 12)}"
          f"{_fmt(pooled_stats['inst_prem'], 11)}{_fmt(pooled_stats['retro_adv'], 11)}")

    print("\npooled contrasts with cluster-bootstrap intervals")
    for key, label in (("sem_rescue", "SemanticRescue       = Supp_K − Supp_U"),
                       ("inst_prem", "InstantiationPremium = Supp_I − Supp_K"),
                       ("retro_adv", "RetrospectiveAdvantage = Supp_I − Supp_U")):
        s = pooled_stats[key]
        print(f"  {label:<44}{s['mean']:>+8.2f} {_ci(s)}")

    def means(key):
        return [m[key]["mean"] for m in model_stats.values() if m[key]["n"]]

    checks = {
        "pass_retrospective_advantage": pass_gate(pooled_stats["retro_adv"],
                                                  means("retro_adv")),
        "pass_semantic_rescue": pass_gate(pooled_stats["sem_rescue"],
                                          means("sem_rescue")),
        "within_floor_semantic_rescue": within_floor(pooled_stats["sem_rescue"]),
        "pass_instantiation_premium": pass_gate(pooled_stats["inst_prem"],
                                                means("inst_prem")),
        "within_floor_instantiation_premium": within_floor(pooled_stats["inst_prem"]),
    }
    verdict = classify(gates["passed"], pooled_stats, model_stats)
    report["branch_checks"] = checks
    report["verdict"] = verdict
    report["licensed_interpretation"] = LICENSED[verdict]
    if verdict in CAUTION:
        report["caution"] = CAUTION[verdict]

    print(f"\n  carrier gate still holds           : {gates['passed']}")
    for k, v in checks.items():
        print(f"  {k:<37}: {v}")
    print(f"VERDICT: {verdict}")
    print(f"LICENSED: {LICENSED[verdict]}")
    if verdict in CAUTION:
        print(f"CAUTION: {CAUTION[verdict]}")
    if report["models_missing"]:
        print(f"MISSING (reported by name, not substituted): {report['models_missing']}")
    return rows, model_stats, pooled_stats


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", choices=["a", "b"], default="a")
    args = ap.parse_args()

    items = {i.item_id: i for i in
             load_items(os.path.join(ROOT, "data/items/g23b_v1.jsonl"))}
    report = _base_report(args.phase)
    if args.phase == "a":
        phase_a(items, report)
        out = os.path.join(ROOT, "results/g23b_carrier_analysis.json")
    else:
        phase_b(items, report)
        out = os.path.join(ROOT, "results/g23b_branch_analysis.json")
    with open(out, "w") as handle:
        json.dump(report, handle, indent=1)
    print(f"\nwrote {os.path.relpath(out, ROOT)}")


if __name__ == "__main__":
    main()
