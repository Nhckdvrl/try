#!/usr/bin/env python3
"""G25A — integrity investigation of record (the §8 "order-artifact" action).

Frozen verdict: `order-artifact` (I1 anchor symmetry fails). Prereg §8 line
"No claim; integrity investigation precedes any interpretation" makes THIS
script that investigation. Zero-model and deterministic: it reads only the
four frozen raws, the frozen analysis v1 and the frozen items file. It
DIAGNOSES: nothing is corrected, re-run, reweighted or reclassified, and no
claim is licensed. The verdict is reproduced, never recomputed differently.

Sections:
  i1             Gap(w100) anatomy — cluster CIs recomputed with the frozen
                 analyzer's OWN machinery (asserted equal to analysis v1 to
                 1e-9), item-/cluster-level distributions, leave-one-model-out
                 points, stratum points, extreme rows with their raw values.
  anchor_parse   per-model per-weight probe accuracy: was the inert
                 "exactly 100%" sentence read as intended?
  distance       rule_to_answer_tokens by arm/w exactly as the harness
                 recorded them (structural pre/post asymmetry documentation).
  s1             nonpositive-anchor drop anatomy; reproduction of 354/400.
  g2             floor miss of Gap01 (point vs FLOOR) with its CI.
  readout        what digit_expectation_0_100 IS (G0–G24A lineage asserted)
                 and digit-mass validity on the anchor rows.
  i1 additions   saturation bucket decomposition of the anchor gap and
                 argmax-digit flip counts — where the -1.06 lives, described,
                 never corrected.
  identifiability  what the anchor CAN and CANNOT identify — prose only; no
                 post-hoc corrected estimand is computed anywhere.

Citation asserts: items sha256, all four run sha256, per-model usability
ledgers, all five gap_w100 cluster CIs, pooled RuleAcc and the S1 count are
re-derived from the raws and must equal analysis v1.

Output: results/audits/g25a_integrity_investigation_v1.json
"""

from __future__ import annotations

import collections
import hashlib
import json
import os
import statistics as st
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

# Reuse the frozen analyzer's machinery — same code, same seeds, no parallel
# statistics that could drift from analysis v1.
from analyze_g25 import (ARMS, B, DESIGN_TAG, FLOOR,  # noqa: E402
                         LOCAL_WKEYS, POOLED_MODELS, PROBE_TOL_PP,
                         REQUIRED, RULEACC_MIN, SEED,
                         SUFFICIENCY_MIN_ITEMS, SUFFICIENCY_MIN_MODELS,
                         WKEYS, WEIGHTS, cluster_boot, load_items,
                         probes_for, rows_for)

ANALYSIS = os.path.join(ROOT, "results", "g25a", "g25a_analysis_v1.json")
ITEMS = os.path.join(ROOT, "data", "items", "g25_v1.jsonl")
OUT = os.path.join(ROOT, "results", "audits",
                   "g25a_integrity_investigation_v1.json")
RUNS = {m: os.path.join(ROOT, "results", "raw", f"{m}_g25a.jsonl")
        for m in POOLED_MODELS}

ANCHOR_W = "w100"           # inert sentence: "exactly 100% of its normal …"
RULE_PREFIX = "g25_"


def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def dist(vals) -> dict:
    """Shape of a numeric sample — descriptive only, no CI, no gate."""
    vals = list(vals)
    n = len(vals)
    if n == 0:
        return {"n": 0}
    return {
        "n": n,
        "mean": st.fmean(vals),
        "median": st.median(vals),
        "stdev": st.stdev(vals) if n > 1 else 0.0,
        "min": min(vals),
        "max": max(vals),
        "frac_neg": sum(v < 0 for v in vals) / n,
        "frac_zero": sum(v == 0 for v in vals) / n,
        "frac_pos": sum(v > 0 for v in vals) / n,
    }


def close(a: float, b: float, tol: float = 1e-9) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def read_run(path: str):
    """Cells + rule→answer distances + readout aux (mass, argmax digit)."""
    cells: dict = collections.defaultdict(dict)
    r2a: dict = collections.defaultdict(lambda: collections.defaultdict(list))
    mass: dict = collections.defaultdict(dict)
    raw_digit: dict = collections.defaultdict(dict)
    n_lines = 0
    with open(path) as fh:
        for line in fh:
            if not line.strip():
                continue
            rec = json.loads(line)
            n_lines += 1
            kind = rec.get("kind_name", "")
            if rec.get("value") not in (None, "None"):
                cells[rec["item_id"]][kind] = rec["value"]
            tok = rec.get("rule_to_answer_tokens")
            if kind.startswith(RULE_PREFIX) and tok is not None:
                r2a[kind][rec["item_id"]] = tok
            if kind.startswith(RULE_PREFIX):
                if rec.get("mass") is not None:
                    mass[kind][rec["item_id"]] = float(rec["mass"])
                raw_txt = (rec.get("raw") or "").strip()
                raw_digit[kind][rec["item_id"]] = (
                    raw_txt[0] if raw_txt and raw_txt[0].isdigit() else None)
    return (dict(cells), {k: dict(v) for k, v in r2a.items()},
            {k: dict(v) for k, v in mass.items()},
            {k: dict(v) for k, v in raw_digit.items()}, n_lines)


def main() -> int:
    with open(ANALYSIS) as fh:
        A = json.load(fh)

    # ---- citation asserts: this audit reads exactly what analysis v1 read --
    assert A["design_tag"] == DESIGN_TAG
    items_sha = sha256(ITEMS)
    assert items_sha == A["items_sha256"], (items_sha, A["items_sha256"])
    for m, path in RUNS.items():
        rel = f"results/raw/{m}_g25a.jsonl"
        got = sha256(path)
        assert got == A["runs_sha256"][rel], (rel, got)

    items = {i.item_id: i for i in load_items(ITEMS)}

    report: dict = {
        "design_tag": DESIGN_TAG,
        "frozen_verdict": A["verdict"],
        "frozen_gates": A["gates"],
        "purpose": "§8 order-artifact required action: integrity investigation "
                   "before any interpretation. Diagnostic only — nothing "
                   "corrected, nothing re-run, no claim licensed, verdict "
                   "unchanged.",
        "citations": {
            "analysis_json_sha256": sha256(ANALYSIS),
            "items_sha256": items_sha,
            "runs_sha256": {m: sha256(p) for m, p in RUNS.items()},
            "bootstrap": {"seed": SEED, "n_resamples": B,
                          "cluster": "source/cluster"},
        },
    }

    # ---- load raws; usability exactly as the frozen analyzer computes it --
    per_model_cells, per_model_r2a, per_model_rows = {}, {}, {}
    per_model_mass, per_model_rawd, drops = {}, {}, {}
    ledger = {}
    for m, path in RUNS.items():
        cells, r2a, mass, rawd, n_lines = read_run(path)
        rows, d = rows_for(items, path)
        assert n_lines == 7200, (m, n_lines)
        assert len(d) == 1 and "nonpositive_anchor" in d, (m, d)
        assert len(rows) == A["ledger"][m]["usable"], (m, len(rows))
        assert dict(d) == A["ledger"][m]["drops"], (m, d)
        per_model_cells[m], per_model_r2a[m] = cells, r2a
        per_model_mass[m], per_model_rawd[m] = mass, rawd
        per_model_rows[m], drops[m] = rows, dict(d)
        ledger[m] = {"rows_in_file": n_lines, "usable": len(rows),
                     "drops": dict(d)}

    pooled_rows = [r for m in POOLED_MODELS for r in per_model_rows[m]]

    # ---- i1: cluster CIs re-derived with the frozen machinery -------------
    def gap_block(rows):
        return cluster_boot([(r["cluster"], r["gap_" + ANCHOR_W]) for r in rows])

    i1_recomputed = {"pooled": gap_block(pooled_rows), "per_model": {}}
    assert close(i1_recomputed["pooled"]["mean"], A["pooled"]["gap_w100"]["mean"])
    assert close(i1_recomputed["pooled"]["ci_low"], A["pooled"]["gap_w100"]["ci_low"])
    assert close(i1_recomputed["pooled"]["ci_high"], A["pooled"]["gap_w100"]["ci_high"])
    for m in POOLED_MODELS:
        got = gap_block(per_model_rows[m])
        want = A["per_model"][m]["gap_w100"]
        assert close(got["mean"], want["mean"]) and close(got["ci_low"], want["ci_low"]) \
            and close(got["ci_high"], want["ci_high"]), (m, got, want)
        i1_recomputed["per_model"][m] = got
    pooled_ci = i1_recomputed["pooled"]
    i1_contains_0 = pooled_ci["ci_low"] <= 0.0 <= pooled_ci["ci_high"]
    assert i1_contains_0 == A["gates"]["i1_gap_w100_ci_contains_0"]

    # ---- i1: complete-case pass (own reader, cross-checked to rows_for) ----
    complete = {}          # model -> item -> full record
    usable_sets = {}
    for m in POOLED_MODELS:
        items_map, n_complete = {}, 0
        for item_id, cells in per_model_cells[m].items():
            item = items.get(item_id)
            if item is None:
                continue
            missing = [k for k in REQUIRED if k not in cells]
            if missing:
                continue
            n_complete += 1
            s = 1.0 if item.critical_direction == "increase" else -1.0
            base = cells["g25_base"]
            L = st.fmean((cells[f"g25_pre_{ANCHOR_W}"],
                          cells[f"g25_post_{ANCHOR_W}"])) - base
            # gap(w100) = s·(pre − base) − s·(post − base) = s·(pre − post)
            gap100 = s * (cells[f"g25_pre_{ANCHOR_W}"]
                          - cells[f"g25_post_{ANCHOR_W}"])
            items_map[item_id] = {
                "s": s, "L": L, "sL": s * L, "usable": s * L > 0,
                "gap_w100": gap100, "base": base,
                "pre": cells[f"g25_pre_{ANCHOR_W}"],
                "post": cells[f"g25_post_{ANCHOR_W}"],
                "stratum": item.meta["stratum"],
                "cluster": f"{item.meta['source']}/{item.meta['cluster']}",
            }
        complete[m] = items_map
        assert n_complete == len(items_map)
        assert n_complete == len(per_model_rows[m]) + drops[m]["nonpositive_anchor"], \
            (m, n_complete, len(per_model_rows[m]), drops[m])
        # cross-check: own gap_w100 equals the analyzer's row value, item by item
        for r in per_model_rows[m]:
            mine = items_map[r["item_id"]]["gap_w100"]
            assert close(mine, r["gap_w100"]), (m, r["item_id"], mine, r["gap_w100"])
        usable_sets[m] = {iid for iid, v in items_map.items() if v["usable"]}
        assert usable_sets[m] == {r["item_id"] for r in per_model_rows[m]}

    def sample(m_filter=None, usable_only=True):
        for m in POOLED_MODELS:
            if m_filter is not None and m != m_filter:
                continue
            for iid, v in complete[m].items():
                if usable_only and not v["usable"]:
                    continue
                if not usable_only and v["usable"]:
                    continue
                yield m, iid, v

    # ---- i1: distributions -------------------------------------------------
    gap_usable = [v["gap_w100"] for _, _, v in sample()]
    gap_dropped = [v["gap_w100"] for _, _, v in sample(usable_only=False)]
    per_model_dist = {m: dist(v["gap_w100"] for v in complete[m].values()
                              if v["usable"]) for m in POOLED_MODELS}
    dropped_dist = {m: dist(v["gap_w100"] for v in complete[m].values()
                            if not v["usable"]) for m in POOLED_MODELS}

    # cluster-level shape (the bootstrap's resampling unit)
    by_cluster: dict = collections.defaultdict(list)
    for _, _, v in sample():
        by_cluster[v["cluster"]].append(v["gap_w100"])
    assert len(by_cluster) == pooled_ci["n_clusters"], \
        (len(by_cluster), pooled_ci["n_clusters"])
    cluster_means = [st.fmean(vs) for vs in by_cluster.values()]

    # leave-one-model-out pooled point estimates (is one model driving it?)
    loo = {}
    for drop_m in POOLED_MODELS:
        vals = [v["gap_w100"] for m, _, v in sample() if m != drop_m]
        loo[f"without_{drop_m}"] = st.fmean(vals)

    # stratum point estimates
    by_stratum: dict = collections.defaultdict(list)
    for _, _, v in sample():
        by_stratum[v["stratum"]].append(v["gap_w100"])

    # extreme rows, raw values intact (one-by-one inspection, data mandate)
    extremes = sorted(sample(), key=lambda t: -abs(t[2]["gap_w100"]))[:5]
    extreme_rows = [
        {"model": m, "item_id": iid, "stratum": v["stratum"],
         "cluster": v["cluster"], "s": v["s"],
         "base": v["base"], "pre_w100": v["pre"], "post_w100": v["post"],
         "gap_w100": v["gap_w100"]}
        for m, iid, v in extremes]

    # where does the -1.06 live? bucket decomposition of the anchor gap
    # (description of the investigated quantity itself — NOT a correction,
    # NOT a replacement estimand: no corrected Gap appears anywhere here).
    def bucket_of(g: float) -> str:
        a = abs(g)
        return "abs_lt_10" if a < 10 else ("abs_10_to_50" if a < 50
                                            else "abs_ge_50")

    buckets: dict = collections.defaultdict(list)
    per_model_sat = {m: 0 for m in POOLED_MODELS}
    for m, _, v in sample():
        buckets[bucket_of(v["gap_w100"])].append(v["gap_w100"])
        if abs(v["gap_w100"]) >= 50:
            per_model_sat[m] += 1
    overall_mean = st.fmean(gap_usable)
    saturation = {}
    for name in ("abs_lt_10", "abs_10_to_50", "abs_ge_50"):
        vals = buckets.get(name, [])
        share = len(vals) / len(gap_usable)
        bmean = st.fmean(vals) if vals else 0.0
        saturation[name] = {"n": len(vals), "share": share, "mean": bmean,
                            "mean_contribution": share * bmean}
    assert close(sum(v["mean_contribution"] for v in saturation.values()),
                 overall_mean)

    # argmax-digit flips at the anchor (decoded first token), usable rows
    flip = {"both_digit_rows": 0, "argmax_flips": 0, "missing_raw": 0}
    flip_gaps, noflip_gaps = [], []
    for m, iid, v in sample():
        dg_pre = per_model_rawd[m][f"g25_pre_{ANCHOR_W}"].get(iid)
        dg_post = per_model_rawd[m][f"g25_post_{ANCHOR_W}"].get(iid)
        if dg_pre is None or dg_post is None:
            flip["missing_raw"] += 1
            continue
        flip["both_digit_rows"] += 1
        (flip_gaps if dg_pre != dg_post else noflip_gaps).append(v["gap_w100"])
    flip["argmax_flips"] = len(flip_gaps)
    flip["frac_flips"] = (len(flip_gaps) / flip["both_digit_rows"]
                          if flip["both_digit_rows"] else None)
    flip["gap_mean_flip"] = st.fmean(flip_gaps) if flip_gaps else None
    flip["gap_mean_noflip"] = st.fmean(noflip_gaps) if noflip_gaps else None

    # ---- readout mechanics + validity at the anchor -----------------------
    g24a_lineage = os.path.join(ROOT, "results", "raw",
                                "qwen3-8b_g24a.jsonl")
    with open(g24a_lineage) as fh:
        first = json.loads(fh.readline())
    assert first.get("readout") == "digit_expectation_0_100"
    anchor_mass = []
    for m, iid, _ in sample():
        for a in ARMS:
            tok = per_model_mass[m].get(f"g25_{a}_{ANCHOR_W}", {})
            if iid in tok:
                anchor_mass.append(tok[iid])
    report["readout"] = {
        "mechanism": "run_model.digit_expectation: value = 100/9 × E[digit] "
                     "over the first-generated-token distribution restricted "
                     "to tokens '0'..'9' and renormalised by digit mass; "
                     "`raw` holds the decoded first token (argmax view) and "
                     "`mass` the digit-token probability mass. An |anchor gap| "
                     "near 100 therefore means the digit distribution "
                     "collapsed toward opposite ends in the two arms — a "
                     "behavioral flip under the house readout, not a parse "
                     "artifact (values like 1.66e-10 are E[d]≈0, not "
                     "malformed numbers).",
        "lineage": "identical readout as G0/G23A/G24A — asserted on the "
                   "first row of a tracked g24a raw",
        "g24a_first_row_readout": first.get("readout"),
        "anchor_w100_digit_mass": dist(anchor_mass),
        "anchor_rows_mass_lt_0_5": sum(x < 0.5 for x in anchor_mass),
        "anchor_rows": len(anchor_mass),
    }

    report["i1"] = {
        "gate": "Gap(w100) 95% CI contains 0 (order symmetry at the anchor)",
        "pooled_recomputed": pooled_ci,
        "per_model_recomputed": i1_recomputed["per_model"],
        "models_negative_point": sum(
            i1_recomputed["per_model"][m]["mean"] < 0 for m in POOLED_MODELS),
        "gap100_usable_pooled": dist(gap_usable),
        "gap100_usable_per_model": per_model_dist,
        "gap100_dropped_nonpositive_anchor": {
            "pooled": dist(gap_dropped), "per_model": dropped_dist},
        "cluster_means": {**dist(cluster_means),
                          "n_clusters": len(cluster_means),
                          "frac_clusters_negative": sum(
                              x < 0 for x in cluster_means) / len(cluster_means)},
        "leave_one_model_out_pooled_mean": loo,
        "stratum_points": {k: dist(v) for k, v in sorted(by_stratum.items())},
        "saturation_decomposition": {
            "buckets": saturation,
            "per_model_abs_ge_50": per_model_sat,
            "meaning": "share × bucket-mean reproduces the overall mean "
                       "(asserted); this explains where the failed gate's "
                       "-1.06 lives and corrects nothing.",
        },
        "argmax_digit_flips": flip,
        "extreme_rows_abs_top5": extreme_rows,
    }

    # ---- anchor_parse: probe accuracy per model × requested weight ---------
    probe_per_model, within_by_w, parsed_by_w = {}, collections.Counter(), \
        collections.Counter()
    for m in POOLED_MODELS:
        p = probes_for(RUNS[m])
        probe_per_model[m] = p
        assert p["n_unparsed"] == A["gates"]["probe_unparsed"][m]
        assert close(p["rule_acc"], A["gates"]["ruleacc_per_model"][m], 1e-9)
        for wkey, lvl in p["stated_weight"].items():
            within_by_w[wkey] += lvl["within_tol"]
            parsed_by_w[wkey] += lvl["n"]
    pooled_ruleacc = (sum(within_by_w.values()) / sum(parsed_by_w.values()))
    assert close(pooled_ruleacc, A["gates"]["ruleacc_pooled"], 1e-12)
    report["anchor_parse"] = {
        "question": "was the inert 'exactly 100%' sentence (and the w=0 "
                    "sentence) read as intended, per probe?",
        "per_model": probe_per_model,
        "pooled_by_weight": {
            w: {"within_tol": within_by_w[w], "n_parsed": parsed_by_w[w],
                "frac_within_tol": within_by_w[w] / parsed_by_w[w],
                "tol_pp": PROBE_TOL_PP}
            for w in sorted(parsed_by_w)},
        "pooled_ruleacc_recomputed": pooled_ruleacc,
        "ruleacc_min": RULEACC_MIN,
    }

    # ---- distance: harness-recorded rule→answer tokens --------------------
    dist_rows = {}
    for m in POOLED_MODELS:
        arm_tok = {a: [] for a in ARMS}
        anchor_tok = {a: [] for a in ARMS}
        for kind, by_item in per_model_r2a[m].items():
            # kind = g25_<arm>_<w>
            parts = kind.split("_")
            arm, wkey = parts[-2], parts[-1]
            for tok in by_item.values():
                arm_tok[arm].append(tok)
                if wkey == ANCHOR_W:
                    anchor_tok[arm].append(tok)
        dist_rows[m] = {
            "all_rule_cells": {a: dist(v) for a, v in arm_tok.items()},
            "anchor_w100_cells": {a: dist(v) for a, v in anchor_tok.items()},
        }
    pooled_anchor = {a: [t for m in POOLED_MODELS
                         for t in per_model_r2a[m][f"g25_{a}_{ANCHOR_W}"].values()]
                     for a in ARMS}
    report["distance"] = {
        "field": "rule_to_answer_tokens as recorded by the harness "
                 "(structural property of the layout, not an outcome)",
        "per_model": dist_rows,
        "pooled_anchor_w100": {a: dist(v) for a, v in pooled_anchor.items()},
        "note": "pre places the rule ahead of the evidence block and post "
                "places it adjacent to the judgment; the asymmetry is the "
                "manipulation's own geometry and is what an inert-sentence "
                "anchor (I1) is designed to expose.",
    }

    # ---- s1: usability / nonpositive-anchor anatomy ------------------------
    usable_k = collections.Counter()
    for iid in items:
        k = sum(1 for m in POOLED_MODELS if iid in usable_sets[m]
                and complete[m][iid]["usable"])
        usable_k[k] += 1
    ge3 = sum(v for k, v in usable_k.items() if k >= SUFFICIENCY_MIN_MODELS)
    assert ge3 == A["gates"]["usable_items_ge_3of4"], (ge3, A["gates"])
    report["s1"] = {
        "requirement": f">= {SUFFICIENCY_MIN_ITEMS} items usable on "
                       f">= {SUFFICIENCY_MIN_MODELS}/4 pooled models",
        "items_by_usable_model_count": {str(k): usable_k[k] for k in range(5)},
        "usable_ge_3of4": ge3,
        "usable_ge_3of4_frozen": A["gates"]["usable_items_ge_3of4"],
        "passes": ge3 >= SUFFICIENCY_MIN_ITEMS,
        "per_model_usable": {m: len(per_model_rows[m]) for m in POOLED_MODELS},
        "per_model_drops": drops,
        "drop_reason": "s·L <= 0 with L = mean(w100_pre, w100_post) − base — "
                       "the anchor row itself shows no positive evidence "
                       "leverage for that item on that model (§6 rule; no "
                       "outcome-dependent filtering).",
    }

    # ---- g2: floor miss anatomy -------------------------------------------
    g1, g2 = A["pooled"]["delta_local0"], A["pooled"]["gap01"]
    report["g2"] = {
        "co_primaries": {
            "delta_local0": {**g1,
                             "ci_low_gt_0": g1["ci_low"] > 0,
                             "point_ge_floor": g1["mean"] >= FLOOR},
            "gap01": {**g2,
                      "ci_low_gt_0": g2["ci_low"] > 0,
                      "point_ge_floor": g2["mean"] >= FLOOR},
        },
        "floor_points": FLOOR,
        "gap01_shortfall": FLOOR - g2["mean"],
        "note": "G2 fails the preregistered 3.0 floor by this much while its "
                "CI low stays > 0 — recorded as measured; no re-grading, no "
                "rounding toward the gate.",
    }

    # ---- identifiability: prose only, no corrected numbers computed --------
    report["identifiability"] = {
        "anchor_estimates": "Gap(w100) isolates the pre/post position effect "
                            "of the one sentence that carries no restriction "
                            "content ('exactly 100%').",
        "what_it_does_not_identify": "All other weights (0…25) carry rule "
            "content, so their position effect = inert-sentence geometry + "
            "content×position interaction. The design contains no cell that "
            "separates the two; the anchor identifies the offset ONLY at "
            "w=100. A constant-across-w additive offset would cancel inside "
            "both co-primary contrasts (Δ_local0, Gap01 are differences of "
            "Gaps) — but constancy across w is NOT testable in this design.",
        "not_done_here": "No baseline subtraction, no bias-corrected Gap, no "
            "item exclusion, no reclassification. Any such change would be a "
            "design change, which the tag forbids without a prereg amendment "
            "and a user decision.",
        "verdict_status": "order-artifact stands exactly as frozen: no claim "
                          "licensed from this run.",
    }

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as fh:
        json.dump(report, fh, indent=1, sort_keys=True)
        fh.write("\n")

    # ---- stdout summary ----------------------------------------------------
    ci = report["i1"]["pooled_recomputed"]
    print(f"verdict (frozen): {A['verdict']} — investigation changes nothing")
    print(f"I1 pooled Gap(w100): {ci['mean']:+.2f} "
          f"[{ci['ci_low']:+.2f}, {ci['ci_high']:+.2f}] "
          f"contains0={i1_contains_0} | models negative: "
          f"{report['i1']['models_negative_point']}/4")
    d = report["i1"]["gap100_usable_pooled"]
    print(f"item-level gap100 (n={d['n']}): mean {d['mean']:+.2f} "
          f"median {d['median']:+.2f} | frac_neg {d['frac_neg']:.3f} "
          f"frac_pos {d['frac_pos']:.3f} frac_zero {d['frac_zero']:.3f}")
    print("leave-one-out:", ", ".join(f"{k.split('_', 1)[1]} {v:+.2f}"
                                      for k, v in loo.items()))
    print(f"S1: {ge3}/400 usable on >= 3/4 (need {SUFFICIENCY_MIN_ITEMS}) "
          f"| histogram {report['s1']['items_by_usable_model_count']}")
    print(f"G2 shortfall vs floor {FLOOR}: {report['g2']['gap01_shortfall']:+.3f}")
    ap = report["anchor_parse"]["pooled_by_weight"]
    print("anchor parse pooled:", {w: round(v['frac_within_tol'], 4)
                                   for w, v in ap.items()})
    s50 = saturation["abs_ge_50"]
    print(f"saturated |gap100|>=50: {s50['n']} rows ({s50['share']:.3f} of "
          f"{len(gap_usable)}), bucket mean {s50['mean']:+.2f} -> contributes "
          f"{s50['mean_contribution']:+.3f} of the overall {overall_mean:+.3f}")
    print(f"argmax-digit flips at anchor: {flip['argmax_flips']}/"
          f"{flip['both_digit_rows']} ({flip['frac_flips']:.3f}) | "
          f"anchor rows with digit mass<0.5: "
          f"{report['readout']['anchor_rows_mass_lt_0_5']}")
    print(f"wrote {os.path.relpath(OUT, ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
