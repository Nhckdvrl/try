"""G25A analysis — estimands and gates frozen in PREREGISTRATION_G25A_NEAR_ZERO.md.

Everything is in **raw sign-aligned rating points** (G23A discipline: no ratio
in any primary, no trimming, no caps — Stage 3E and G17 already showed why).

    ResInf(arm, w) = s · [ Y(g25_<arm>_<w>) − Y(g25_base) ]
    Gap(w)         = ResInf(pre, w) − ResInf(post, w)
    Δ_local0       = Gap(w000) − mean[ Gap(w001), Gap(w002), Gap(w005) ]   (co-primary 1)
    Gap01          = Gap(w000) − Gap(w001)                                  (co-primary 2)
    L              = mean(Y(g25_pre_w100), Y(g25_post_w100)) − Y(g25_base)
    Resp(w)        = mean(ResInf(pre, w), ResInf(post, w))
    GradedPos      = Resp(w100) − mean[ Resp(w001), Resp(w002), Resp(w005) ]
    REI_c          = s · (Y_c − base) / |L|          (secondary; winsorised ±3)

**Usability (§6):** an item×model row needs all 16 decision cells present and
``s·L > 0``; otherwise it is unusable **for that model only**, reported as
``n/400`` — never filtered on an outcome.

**Gradedness is not a gate.** ``GradedPos``/``Resp(w)`` are the §6
interpretation diagnostic for a *passing* verdict (§1 three-way split):
``classify()`` does not receive them as input, and the flat branch's mechanism
sentence is a categorical zero-vs-nonzero semantic-control regime — never
"nullification operation". The confirmatory verdict is decided by the two
preregistered co-primaries only.

**RuleAcc (§7 O4 / §8 I2; clarified pre-tag 2026-09-24):** the pooled
fraction of §4 requested-weight-access probe rows (``wprobe_g25_pre_w000``,
``wprobe_g25_pre_w100``) whose stated weight is within ``PROBE_TOL_PP = 2.0``
percentage points of the requested one. Unparsed probe rows leave the
denominator and are counted (``n_unparsed``); absent probe data fails I2
(→ ``order-artifact``: investigate before any interpretation).

**Inference (§7):** cluster bootstrap over ``source/cluster`` (G24A analysis
keys; the same keying that reproduces the §5 anchor's 342 clusters / 126
shared), seed ``20260924``, ``B = 10,000``, percentile 95% CIs, two-sided
bootstrap p (G0 convention). A pooled replicate draws K observed clusters
with replacement and every row of a drawn cluster — items × models — moves
together; a cluster never splits.

**Gate order (§8, literal):** integrity (I1 anchor symmetry, I2 RuleAcc) →
sufficiency (S1: ≥ 360/400 items usable on ≥ 3/4 pooled models) →
co-primaries (G1, G2; intersection–union; G3 ≥ 3/4 model means positive per
primary is reported and licenses the cross-model sentence only).

Usage:
    PYTHONPATH=src python src/analyze_g25.py \
        --runs results/raw/g25_llama31-8b.jsonl ... \
        --items data/items/g25_v1.jsonl \
        --tag g25-v1 --out-prefix results/g25a/g25a_analysis_v1
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import math
import os
import random
import statistics as st
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from analyze import wins  # noqa: E402  (G0/G24A winsorisation, ±3)
from conditions_g25 import (ARMS, CONTEXT_WKEYS, G25A_CONDITIONS,  # noqa: E402
                            G25A_NUMERIC_PROBES, LOCAL_WKEYS, WKEYS,
                            WEIGHTS)
from schema import load_items  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SEED = 20260924
B = 10_000

POOLED_MODELS = ["llama31-8b", "qwen3-8b", "qwen35-9b", "gemma3-12b"]
SELECTOR_TAG = "mistral-small-24b"   # never in pooled inference (§4)
DESIGN_TAG = "g25a-near-zero-design-v1"

FLOOR = 3.0                 # O4: both primary gates, G23A's floor
MIN_MODELS_POSITIVE = 3     # G3: ≥ 3/4 pooled models, per primary
SUFFICIENCY_MIN_ITEMS = 360  # S1: usable on ≥ 3/4 pooled models
SUFFICIENCY_MIN_MODELS = 3
RULEACC_MIN = 0.8           # I2 (O4)
PROBE_TOL_PP = 2.0          # stated weight within 2 pp of requested (G23A value)

REQUIRED = list(G25A_CONDITIONS)     # complete case = all 16 decision cells
VERDICTS = ["exact-zero-boundary", "boundary-not-replicated",
            "partial-boundary", "no-natural-gap", "order-artifact",
            "unresolved"]
LICENSED = {
    "exact-zero-boundary":
        "Complete semantic causal exclusion shows an additional prospective "
        "cost even though prospective zero can be executed exactly when the "
        "contribution is explicit and verifiable. On source-grounded natural "
        "materials this replicates with both co-primary boundary contrasts "
        "(Δ_local0 and Gap(0)−Gap(1)) clearing a cluster-bootstrap CI above "
        "zero and the frozen 3.0-point floor on the pooled-4 panel; the "
        "object is strictly the causal eligibility of future evidence under a "
        "prior prospective policy.",
    "boundary-not-replicated":
        "The boundary claim is withdrawn for natural materials: the "
        "zero-vs-local-nonzero discontinuity did not replicate even though the "
        "timing gap at zero is positive. RQ2 is re-audited as a smooth "
        "semantic-weighting failure under prospective control; the Finding 2 "
        "sentence is rescoped to its actual evidence base pending register "
        "revision. Same question, honest answer.",
    "partial-boundary":
        "Exactly one co-primary passed; the claim is strictly the passing "
        "contrast. The word \"boundary\" may appear only if Δ_local0 (G1) "
        "passed, and no plateau sentence unless the full Gap(w) curve "
        "supports it.",
    "no-natural-gap":
        "The G23A timing gap does not manifest on natural materials at zero: "
        "the Gap(0) CI contains 0 (G24A measured levels under standing "
        "rulings, not this timing shape). Finding 2 stays scoped to the "
        "synthetic materials; report as-is.",
    "order-artifact":
        "An integrity gate failed (I1 anchor symmetry, or I2 RuleAcc below "
        "0.8 — including absent probe data): no claim is licensed; integrity "
        "investigation precedes any interpretation.",
    "unresolved":
        "Not evaluable as preregistered (sufficiency S1 failed, the CIs "
        "straddle the gates ambiguously, or no evaluable data exists); "
        "everything is reported and no verdict is granted.",
}
# §1/§6/§8 three-way interpretation split — a LABEL on a passing verdict,
# never an input to the verdict itself.
INTERP = {
    "graded":
        "GradedPos CI strictly above 0: a sharp zero boundary over graded "
        "semantic weighting — the graded positive-weight response carries the "
        "discontinuity claim.",
    "flat":
        "GradedPos CI does not clear 0 with a flat Resp(w): the discontinuity "
        "is still licensed, but the mechanism sentence is a categorical "
        "zero-vs-nonzero semantic-control regime — never \"a dedicated "
        "semantic nullification operation\". The Resp(w) table ships either "
        "way.",
}


# ---------------------------------------------------------------------------
# frozen inference: scalar cluster bootstrap (G0/G24A engine, one metric)
# ---------------------------------------------------------------------------
def _boot_reps(by: dict, n: int, seed: int):
    """(point mean, replicate means) — test hook for whole-cluster integrity.

    ``by`` maps cluster key -> list of values; keys are sorted so the RNG
    stream is deterministic across row orders.
    """
    keys = sorted(by)                       # deterministic across row orders
    stats = [(len(by[k]), sum(by[k])) for k in keys]
    point = st.fmean(v for k in keys for v in by[k])
    rng = random.Random(seed)
    reps = []
    K = len(stats)
    for _ in range(n):
        size = 0
        total = 0.0
        for _ in range(K):
            sz, sm = stats[rng.randrange(K)]
            size += sz
            total += sm
        reps.append(total / size)
    return point, reps


def cluster_boot(pairs, n=None, seed=SEED):
    """(cluster_key, value) pairs -> {mean, ci_low, ci_high, p, n, n_clusters}.

    Each replicate draws K = observed cluster count clusters with replacement
    and takes the cluster-size-weighted mean over the drawn clusters' rows —
    equal to the plain mean over the concatenated rows (G24A check #6: a
    cluster never splits across the resample).
    """
    n = n or B
    by: dict = collections.defaultdict(list)
    for key, value in pairs:
        by[key].append(value)
    if not by:
        return {"n": 0, "n_clusters": 0, "mean": float("nan"),
                "ci_low": float("nan"), "ci_high": float("nan"),
                "p": float("nan")}
    keys = sorted(by)                       # deterministic across row orders
    point, reps = _boot_reps(by, n, seed)
    K = len(by)
    ordered = sorted(reps)
    if point > 0:
        cnt = sum(1 for x in reps if x <= 0)
    else:
        cnt = sum(1 for x in reps if x >= 0)
    p = min(1.0, 2.0 * cnt / n)
    return {"n": sum(len(v) for v in by.values()), "n_clusters": K,
            "mean": point, "ci_low": ordered[int(0.025 * n)],
            "ci_high": ordered[int(0.975 * n)], "p": p}


# ---------------------------------------------------------------------------
# row construction and the frozen usability rule (§6)
# ---------------------------------------------------------------------------
def rows_for(items: dict, path: str):
    """One row per item×model that is usable: all 16 cells present, s·L > 0.

    Drop reasons are exactly three and none depends on an outcome value:
    unknown item, incomplete, nonpositive anchor (s·L ≤ 0).
    """
    y: dict = collections.defaultdict(dict)
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
        base = cells["g25_base"]
        L = st.fmean((cells["g25_pre_w100"], cells["g25_post_w100"])) - base
        if s * L <= 0:
            drops["nonpositive_anchor"] += 1      # unusable for this model
            continue

        resinf = {(arm, w): s * (cells[f"g25_{arm}_{w}"] - base)
                  for w in WKEYS for arm in ARMS}
        gap = {w: resinf[("pre", w)] - resinf[("post", w)] for w in WKEYS}
        delta_local0 = gap["w000"] - st.fmean(gap[w] for w in LOCAL_WKEYS)
        gap01 = gap["w000"] - gap["w001"]
        resp = {w: st.fmean((resinf[("pre", w)], resinf[("post", w)]))
                for w in WKEYS}
        gradedpos = resp["w100"] - st.fmean(resp[w] for w in LOCAL_WKEYS)
        rei = {(arm, w): s * (cells[f"g25_{arm}_{w}"] - base) / abs(L)
               for w in WKEYS for arm in ARMS}
        meta = item.meta
        rows.append({
            "item_id": item_id,
            "cluster": f"{meta['source']}/{meta['cluster']}",
            "source": meta["source"],
            "gold_label": meta["gold_label"],
            "stratum": meta["stratum"],
            "direction": item.critical_direction,
            "s": s, "L": L, "sL": s * L,
            "resinf": resinf, "gap": gap, "resp": resp,
            "delta_local0": delta_local0, "gap01": gap01,
            "gradedpos": gradedpos, "rei": rei,
            # flattened aliases so the summariser can address metrics by name
            **{f"gap_{w}": gap[w] for w in WKEYS},
            **{f"resp_{w}": resp[w] for w in WKEYS},
        })
    return rows, drops


def probes_for(path: str) -> dict:
    """Requested-weight-access readout: stated vs requested, and RuleAcc (I2)."""
    stated: dict = collections.defaultdict(dict)   # wkey -> {item_id: value}
    n_rows = n_unparsed = 0
    with open(path) as handle:
        for line in handle:
            rec = json.loads(line)
            kind = rec.get("kind_name", "")
            if kind not in G25A_NUMERIC_PROBES:
                continue
            n_rows += 1
            wkey = kind.split("_")[-1]
            if rec.get("value") is None:
                n_unparsed += 1
            else:
                stated[wkey][rec["item_id"]] = float(rec["value"])

    levels, within_total, parsed_total = {}, 0, 0
    for wkey in WKEYS:
        target = WEIGHTS[wkey] * 100.0
        errs, within = [], 0
        for value in stated.get(wkey, {}).values():
            err = abs(value - target)
            errs.append(err)
            within += err <= PROBE_TOL_PP
        if errs:
            levels[wkey] = {"n": len(errs),
                            "median_abs_error_pp": st.median(errs),
                            "frac_within_tol": within / len(errs),
                            "within_tol": within}
            within_total += within
            parsed_total += len(errs)
    rule_acc = (within_total / parsed_total) if parsed_total else float("nan")
    return {"stated_weight": levels, "rule_acc": rule_acc,
            "n_probe_rows": n_rows, "n_unparsed": n_unparsed,
            "n_probe_parsed": parsed_total}


# ---------------------------------------------------------------------------
# §8 literal decision order — verdict from the two co-primaries ONLY
# ---------------------------------------------------------------------------
def classify(i1: bool, i2: bool, s1: bool, g1: bool, g2: bool, gap0: dict):
    """integrity → sufficiency → co-primaries, top-down through the §8 table.

    ``gap0`` is the pooled Gap(w000) summary (the map's ``Gap(0)>0`` /
    ``Gap(0) CI contains 0`` rows).  **Gradedness (§6 GradedPos/Resp) is not
    an input**: it interprets a passing verdict and can never change it
    (prereg §1 three-way split, §6 "not a gate", user ruling 2026-09-24).
    """
    if gap0 is None or gap0["n"] == 0 or math.isnan(gap0["ci_low"]):
        # no evaluable data: S1 fails too, but this is not an integrity event
        return "unresolved"
    gap0_pos = gap0["ci_low"] > 0                 # §8 row 2 "Gap(0) > 0"
    gap0_zero = gap0["ci_low"] <= 0 <= gap0["ci_high"]   # §8 row 4
    if not (i1 and i2):
        return "order-artifact"                   # integrity first
    if not s1:
        return "unresolved"                       # sufficiency second
    if g1 and g2:
        return "exact-zero-boundary"
    if not g1 and gap0_pos:
        # row 2 precedes row 3 (table order): G1 is *the* boundary contrast
        return "boundary-not-replicated"
    if g1 != g2:
        return "partial-boundary"
    if gap0_zero:
        return "no-natural-gap"
    return "unresolved"                           # CIs straddle ambiguously


def gate(summary: dict) -> bool:
    """G-gate: CI low strictly > 0 AND point ≥ FLOOR (O4), NaN-safe."""
    if summary is None or summary["n"] == 0 or math.isnan(summary["ci_low"]):
        return False
    return summary["ci_low"] > 0 and summary["mean"] >= FLOOR


def gradedness_label(graded: dict) -> str:
    """§6: CI strictly above 0 -> 'graded', else 'flat' (descriptive only)."""
    if graded is None or graded["n"] == 0 or math.isnan(graded["ci_low"]):
        return "flat"
    return "graded" if graded["ci_low"] > 0 else "flat"


# ---------------------------------------------------------------------------
# analysis
# ---------------------------------------------------------------------------
def _block(rows, key):
    return [(r["cluster"], r) for r in rows if key(r)]


def _summarise_rows(pairs, metrics):
    """{metric: cluster_boot over (cluster, row[metric])} for row dicts."""
    return {m: cluster_boot([(c, v[m]) for c, v in pairs]) for m in metrics}


def _fmt(stats: dict, width: int = 8) -> str:
    if not stats or stats["n"] == 0 or math.isnan(stats["mean"]):
        return f"{'—':>{width}}"
    return f"{stats['mean']:>+{width}.2f}"


def _ci(stats: dict) -> str:
    return f"[{stats['ci_low']:+.2f}, {stats['ci_high']:+.2f}]"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", nargs="+", required=True)
    ap.add_argument("--items", default="data/items/g25_v1.jsonl")
    ap.add_argument("--tag", required=True)
    ap.add_argument("--out-prefix", default="results/g25a/g25a_analysis_v1")
    args = ap.parse_args()

    items_list = load_items(args.items)
    items = {i.item_id: i for i in items_list}

    # --- runs: exactly the frozen pooled panel, no selector (§4) -----------
    per_model_rows, drops, probes, ledger = {}, {}, {}, {}
    for path in args.runs:
        tags = set()
        n_lines = 0
        with open(path) as fh:
            for line in fh:
                if line.strip():
                    n_lines += 1
                    tags.add(json.loads(line).get("model_tag"))
        if len(tags) != 1:
            raise SystemExit(f"{path}: rows must carry one model_tag, got {tags}")
        tag = tags.pop()
        if tag not in POOLED_MODELS:
            raise SystemExit(
                f"{path}: model_tag {tag!r} not in the frozen pooled panel "
                f"{POOLED_MODELS} (selector {SELECTOR_TAG} is never pooled, "
                f"prereg §4)")
        rows, d = rows_for(items, path)
        per_model_rows[tag] = rows
        drops[tag] = dict(d)
        probes[tag] = probes_for(path)
        ledger[tag] = {"rows_in_file": n_lines, "usable": len(rows),
                       "drops": dict(d)}
    missing = [m for m in POOLED_MODELS if m not in per_model_rows]
    if missing:
        raise SystemExit(
            f"missing model outputs for {missing} — mechanical incompleteness; "
            f"rerun those files (prereg §7), never re-run selectively by outcome")

    pooled = [r for tag in POOLED_MODELS for r in per_model_rows[tag]]

    report = {
        "design_tag": DESIGN_TAG,
        "estimand": "Δ_local0 and Gap01 (Gap(w000)−Gap(w001)) in raw "
                     "sign-aligned rating points; Gap(w)/Resp(w) full curves",
        "exclusions": ["complete case: all 16 decision cells present",
                       "usability: s·L > 0 with L = mean(w100_pre, "
                       "w100_post) − base, per model",
                       f"selector {SELECTOR_TAG} never pooled (prereg §4)"],
        "bootstrap": {"seed": SEED, "n_resamples": B,
                      "cluster": "source/cluster; pooled keeps models sharing "
                                 "a cluster together"},
        "floor_points": FLOOR,
        "ruleacc_min": RULEACC_MIN,
        "ruleacc_definition": f"pooled fraction of §4 probe rows within "
                              f"{PROBE_TOL_PP} pp of the requested weight "
                              f"(unparsed excluded, counted)",
        "sufficiency": {"min_items": SUFFICIENCY_MIN_ITEMS,
                        "min_models": SUFFICIENCY_MIN_MODELS},
        "claim_scope": "causal eligibility of future evidence under a prior "
                       "prospective policy; the two co-primaries decide the "
                       "verdict — gradedness (§6) is interpretation only",
        "drops": drops, "ledger": ledger,
        "per_model": {}, "pooled": {}, "strata": {},
    }

    # --- per-model + pooled estimands --------------------------------------
    gap_metrics = {f"gap_{w}" for w in WKEYS} | {"delta_local0", "gap01"}
    resp_metrics = {f"resp_{w}" for w in WKEYS} | {"gradedpos"}
    core = sorted(gap_metrics | resp_metrics | {"sL"})

    head = "".join(f"{w:>9}" for w in WKEYS)
    print("Gap(w) — evidence influence LOST when the rule moves from after the "
          "evidence to before it. Positive = the G0 reversal.")
    print(f"{'model':<14}{'n':>5}{head}{'Δ_local0':>11}{'Gap01':>9}")
    print("-" * (19 + 9 * len(WKEYS) + 20))

    for tag in POOLED_MODELS:
        rows = per_model_rows[tag]
        pairs = _block(rows, lambda r: True)
        entry = {"n": len(rows), "items_total": len(items_list),
                 "usable_frac": f"{len(rows)}/{len(items_list)}"}
        for m in core:
            entry[m] = cluster_boot([(c, r[m]) for c, r in pairs])
        entry["probe"] = probes[tag]
        report["per_model"][tag] = entry
        line = f"{tag:<14}{len(rows):>5}"
        for w in WKEYS:
            line += _fmt(entry[f"gap_{w}"], 9)
        line += f"{entry['delta_local0']['mean']:>+11.2f}"
        line += f"{entry['gap01']['mean']:>+9.2f}"
        print(line)
    print("-" * (19 + 9 * len(WKEYS) + 20))
    line = f"{'POOLED':<14}{len(pooled):>5}"
    pooled_pairs = _block(pooled, lambda r: True)
    pooled_stats = {m: cluster_boot([(c, r[m]) for c, r in pooled_pairs])
                    for m in core}
    for w in WKEYS:
        line += _fmt(pooled_stats[f"gap_{w}"], 9)
    line += f"{pooled_stats['delta_local0']['mean']:>+11.2f}"
    line += f"{pooled_stats['gap01']['mean']:>+9.2f}"
    print(line + "\n")
    report["pooled"] = pooled_stats

    # pooled Resp(w) table + secondary REI (winsorised ±3)
    # Resp per arm: raw sign-aligned points, never winsorised (§6 reports
    # raw points; ±3 winsorisation belongs to the ratio-scale REI only)
    report["pooled"]["resp_arm"] = {
        f"{arm}_{w}": cluster_boot(
            [(r["cluster"], r["resinf"][(arm, w)]) for r in pooled])
        for w in WKEYS for arm in ARMS}
    report["pooled"]["rei"] = {
        f"{arm}_{w}": cluster_boot(
            [(r["cluster"], wins(r["rei"][(arm, w)])) for r in pooled])
        for w in WKEYS for arm in ARMS}
    report["pooled"]["rei_winsorised"] = 3.0

    print("Resp(w) — how much evidence influence survives, averaged over the "
          "two timings (§6 gradedness diagnostic, NOT a gate)")
    print(f"  {'w':<7}{'Resp(w)':>10}{'95% CI':>24}   "
          f"{'pre':>9}{'post':>9}")
    for w in WKEYS:
        g = pooled_stats[f"resp_{w}"]
        pre = report["pooled"]["resp_arm"][f"pre_{w}"]
        post = report["pooled"]["resp_arm"][f"post_{w}"]
        print(f"  {w:<7}{_fmt(g, 10)}{_ci(g):>24}   "
              f"{_fmt(pre, 9)}{_fmt(post, 9)}")
    gp = pooled_stats["gradedpos"]
    label = gradedness_label(gp)
    print(f"\n  GradedPos = Resp(100) − mean[Resp(1,2,5)] = {gp['mean']:+.2f} "
          f"{_ci(gp)}  → §6 label: {label}")
    report["gradedness_label"] = label
    mono = [pooled_stats[f"resp_{w}"]["mean"] for w in WKEYS]
    report["resp_monotone_nondecreasing"] = all(
        a <= b for a, b in zip(mono, mono[1:]))
    print(f"  Resp(w) nondecreasing along 0→100: "
          f"{report['resp_monotone_nondecreasing']} (descriptive only; "
          f"linearity of rating points in weight is NEVER assumed)")

    # --- strata (§7: per stratum, per label direction; descriptive) --------
    strata_defs = {
        **{f"stratum {s}": (lambda r, s=s: r["stratum"] == s)
           for s in sorted({r["stratum"] for r in pooled})},
        **{f"label-direction {d}": (lambda r, d=d: r["direction"] == d)
           for d in sorted({r["direction"] for r in pooled})},
        **{f"model {t}": (lambda r, t=t: r["_tag"] == t)
           for t in POOLED_MODELS},
    }
    stratum_metrics = sorted({"gap_w000", "gap_w001", "delta_local0",
                              "gap01", "gradedpos"})
    for name, key in strata_defs.items():
        if name.startswith("model "):
            tag = name.split(" ", 1)[1]
            sel = [(r["cluster"], r) for r in per_model_rows[tag]]
        else:
            sel = [(r["cluster"], r) for r in pooled if key(r)]
        if not sel:
            continue
        report["strata"][name] = {
            m: cluster_boot([(c, r[m]) for c, r in sel])
            for m in stratum_metrics}
        report["strata"][name]["n"] = len(sel)
        report["strata"][name]["n_clusters"] = len(
            {c for c, _ in sel})

    # --- sufficiency, integrity, gates, verdict (§8 order) -----------------
    models_by_item: dict = collections.Counter()
    for r in pooled:
        models_by_item[r["item_id"]] += 1
    usable_items = sum(1 for iid, cnt in models_by_item.items()
                       if cnt >= SUFFICIENCY_MIN_MODELS)
    s1 = usable_items >= SUFFICIENCY_MIN_ITEMS

    gap100 = pooled_stats["gap_w100"]
    i1 = (gap100["n"] > 0 and not math.isnan(gap100["ci_low"])
          and gap100["ci_low"] <= 0 <= gap100["ci_high"])
    pooled_parsed = sum(probes[t]["n_probe_parsed"] for t in POOLED_MODELS)
    pooled_within = 0
    for t in POOLED_MODELS:
        for lvl in probes[t]["stated_weight"].values():
            pooled_within += lvl["within_tol"]
    pooled_ruleacc = (pooled_within / pooled_parsed
                      if pooled_parsed else float("nan"))
    i2 = (not math.isnan(pooled_ruleacc)) and pooled_ruleacc >= RULEACC_MIN

    d_local = pooled_stats["delta_local0"]
    d_gap01 = pooled_stats["gap01"]
    g1, g2 = gate(d_local), gate(d_gap01)
    model_pos = {
        "delta_local0": [t for t in POOLED_MODELS
                         if report["per_model"][t]["delta_local0"]["mean"] > 0],
        "gap01": [t for t in POOLED_MODELS
                  if report["per_model"][t]["gap01"]["mean"] > 0],
    }
    g3 = {m: len(tags) >= MIN_MODELS_POSITIVE for m, tags in model_pos.items()}

    gap0_stats = pooled_stats["gap_w000"]
    verdict = classify(i1, i2, s1, g1, g2, gap0_stats)
    interp = (INTERP[label] if verdict == "exact-zero-boundary" else None)
    report["gates"] = {
        "i1_gap_w100_ci_contains_0": i1,
        "i2_ruleacc_ge_min": i2,
        "ruleacc_pooled": pooled_ruleacc,
        "ruleacc_min": RULEACC_MIN,
        "ruleacc_per_model": {t: probes[t]["rule_acc"] for t in POOLED_MODELS},
        "probe_rows": {t: probes[t]["n_probe_rows"] for t in POOLED_MODELS},
        "probe_unparsed": {t: probes[t]["n_unparsed"] for t in POOLED_MODELS},
        "s1_usable_items_ge_min": s1,
        "usable_items_ge_3of4": usable_items,
        "g1_delta_local0": g1,
        "g2_gap01": g2,
        "floor_points": FLOOR,
        "g3_models_positive": {m: {"n": len(tags), "models": tags,
                                   "pass": g3[m]}
                               for m, tags in model_pos.items()},
    }
    report["verdict"] = verdict
    report["licensed"] = LICENSED[verdict]
    report["gradedness_interpretation"] = interp

    out = ["## Verdict", f"**{verdict}**", "", LICENSED[verdict], ""]
    if interp:
        out += [f"- §6 gradedness interpretation: {interp}",
                f"- GradedPos: {gp['mean']:+.2f} {_ci(gp)} "
                f"(label: {label}) — interpretation only, never a gate", ""]
    out += [
        f"- I1 (Gap(w100) 95% CI contains 0): {'PASS' if i1 else 'FAIL'} — "
        f"{gap100['mean']:+.2f} {_ci(gap100)}",
        f"- I2 (pooled RuleAcc ≥ {RULEACC_MIN}): "
        f"{'PASS' if i2 else 'FAIL'} — "
        f"{pooled_ruleacc:.3f} over {pooled_parsed} parsed probe rows "
        f"(unparsed: {sum(probes[t]['n_unparsed'] for t in POOLED_MODELS)})",
        f"- S1 (≥ {SUFFICIENCY_MIN_ITEMS} items usable on ≥ "
        f"{SUFFICIENCY_MIN_MODELS}/4 models): "
        f"{'PASS' if s1 else 'FAIL'} — {usable_items}/{len(items_list)}",
        f"- G1 (Δ_local0 CI low > 0 and point ≥ {FLOOR}): "
        f"{'PASS' if g1 else 'FAIL'} — {d_local['mean']:+.2f} "
        f"{_ci(d_local)} (boot_p={d_local['p']:.4f})",
        f"- G2 (Gap(0)−Gap(1) CI low > 0 and point ≥ {FLOOR}): "
        f"{'PASS' if g2 else 'FAIL'} — {d_gap01['mean']:+.2f} "
        f"{_ci(d_gap01)} (boot_p={d_gap01['p']:.4f})",
        f"- G3 (≥ {MIN_MODELS_POSITIVE}/4 model means positive, per primary; "
        f"cross-model sentence only): "
        f"Δ_local0 {'PASS' if g3['delta_local0'] else 'FAIL'} "
        f"({len(model_pos['delta_local0'])}/4), "
        f"Gap01 {'PASS' if g3['gap01'] else 'FAIL'} "
        f"({len(model_pos['gap01'])}/4)",
        "",
        "## Gap(w) — pooled decomposition",
        f"  {'w':<7}{'ResInf(pre)':>13}{'ResInf(post)':>14}{'Gap(w)':>22}",
    ]
    for w in WKEYS:
        pre = report["pooled"]["resp_arm"][f"pre_{w}"]
        post = report["pooled"]["resp_arm"][f"post_{w}"]
        g = pooled_stats[f"gap_{w}"]
        out.append(f"  {w:<7}{_fmt(pre, 13)}{_fmt(post, 14)}"
                   f"{_fmt(g, 9)} {_ci(g)}")
    out += ["", "## Co-primaries (pooled-4)",
            f"- Δ_local0 = Gap(0) − mean[Gap(1), Gap(2), Gap(5)]: "
            f"{d_local['mean']:+.2f} {_ci(d_local)} "
            f"n_clusters={d_local['n_clusters']} seed={SEED} B={B}",
            f"- Gap(0)−Gap(1): {d_gap01['mean']:+.2f} {_ci(d_gap01)} "
            f"n_clusters={d_gap01['n_clusters']}",
            "", "## Usability ledger (§6: all 16 cells + s·L > 0, per model)",
            json.dumps(ledger, sort_keys=True), ""]
    txt = "\n".join(out)
    print(txt)

    os.makedirs(os.path.dirname(args.out_prefix) or ".", exist_ok=True)
    with open(args.out_prefix + ".md", "w") as fh:
        fh.write(txt + "\n")
    report["items_sha256"] = hashlib.sha256(
        open(args.items, "rb").read()).hexdigest()
    report["runs_sha256"] = {p: hashlib.sha256(open(p, "rb").read()).hexdigest()
                             for p in args.runs}
    report["tag"] = args.tag
    report["pooled_models"] = POOLED_MODELS
    with open(args.out_prefix + ".json", "w") as fh:
        json.dump(report, fh, indent=1, ensure_ascii=False,
                  default=float)
    print(f"wrote {os.path.relpath(args.out_prefix + '.md', ROOT)} "
          f"and {os.path.relpath(args.out_prefix + '.json', ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
