#!/usr/bin/env python3
"""G24A §14 explanation experiment — RQ3 second-order / meta-evidence readout.

Frozen estimands (registered pre-run, registration §14.4, user 2026-09-26;
reporting, NOT gates).  Cells per (model, claim): Y0 = plus base;
ADM+/ADM- = admit_post; then per retraction operator op in
{EXC exclude_post, STR strong_exclude_post, CF counterfactual_delete_post,
MNR meta_neutral_post, RND random_reason_post}: OP+/OP- = plus/minus.
M_op = (OP+ + OP-) / 2.

CRE (counterfactual restoration error, §14.4 — the intervention-layer
criterion), all pooled over (model, claim):
  CRE_abs_op   = mean|Y0 - M_op|        (cell-level abs first; expected
                 MNR < CF and RND < CF)
  CRE_sgn_op   = mean(Y0 - M_op)
  contrasts    CRE_MNR - CRE_CF, CRE_RND - CRE_CF  (expected < 0)

Separation (first-order direction; must NOT reopen under meta-neutralizing):
  sep_op = mean(OP+ - OP-) for the five operators plus sep_admit
  gaps   sep_MNR - sep_admit (expected < 0), sep_MNR - sep_cf (~0, no
         registered sign)

Reconstruction trajectory (claim-level, each claim averaged over the 6
models first):
  corr(M_op, Y0), OLS slope(M_op, Y0) per operator
  contrasts slope_MNR - slope_CF and corr_MNR - corr_CF (expected > 0,
  moving toward 1)

Reporting method (§14.4, identical to §13.5): paired percentile bootstrap
95% CIs, resampling CLAIMS with every model's cells moving together,
B = 10,000, seed "g24a_meta_ci_v1"; per-model consistency as n/6 on the
registered side (≈0 quantities: n/6 on the POOLED sign — descriptive,
threshold-free).  No p-values, no thresholds, no selection:
200 claims x 13 cells x 6 models.  Registered expectations are QUOTED,
never evaluated as pass/fail; everything is reported as-is.

Input:  results/raw/{tag}_g24a_meta_{plus,minus}.jsonl x 6 tags
        (check_g24a_meta_raws.py --require6 must be green first)
        data/items/g24a_p2_v1.jsonl                (arm / claim map)
        results/g24a/g24a_confb_analysis_v1.json   (committed context)
        results/g24a/g24a_p2_compression_v1.json   (committed context)
Output: results/g24a/g24a_meta_analysis_v1.{md,json}
        results/g24a/g24a_meta_analysis_v1_cells.csv
Usage: python src/analyze_g24a_meta.py
"""
from __future__ import annotations

import csv
import json
import math
import random
import statistics
import sys

RAW = "results/raw/{tag}_g24a_meta{arm}.jsonl"
ITEMS = "data/items/g24a_p2_v1.jsonl"
CONF_JSON = "results/g24a/g24a_confb_analysis_v1.json"
P2_JSON = "results/g24a/g24a_p2_compression_v1.json"
OUT_MD = "results/g24a/g24a_meta_analysis_v1.md"
OUT_JSON = "results/g24a/g24a_meta_analysis_v1.json"
OUT_CSV = "results/g24a/g24a_meta_analysis_v1_cells.csv"

PANEL = ["mistral-small-24b", "llama31-8b", "qwen3-8b", "qwen35-9b",
         "gemma3-12b", "qwen3-32b"]
OPS = ["exclude_post", "strong_exclude_post", "counterfactual_delete_post",
       "meta_neutral_post", "random_reason_post"]
OP_KEY = {"exclude_post": "EXC", "strong_exclude_post": "STR",
          "counterfactual_delete_post": "CF", "meta_neutral_post": "MNR",
          "random_reason_post": "RND"}
CELL_MAP = {
    ("plus", "base"): "Y0",
    ("plus", "admit_post"): "ADM+",
    ("minus", "admit_post"): "ADM-",
}
for _op in OPS:
    CELL_MAP[("plus", _op)] = OP_KEY[_op] + "+"
    CELL_MAP[("minus", _op)] = OP_KEY[_op] + "-"
CELLS = ["Y0", "ADM+", "ADM-"] + [OP_KEY[o] + s for o in OPS
                                  for s in ("+", "-")]
B = 10_000                      # registered bootstrap resamples
SEED = "g24a_meta_ci_v1"


def quantiles(xs, qs):
    xs = sorted(xs)
    out = []
    for q in qs:
        i = q * (len(xs) - 1)
        lo, hi = int(i), min(int(i) + 1, len(xs) - 1)
        out.append(xs[lo] + (xs[hi] - xs[lo]) * (i - lo))
    return out


def corr_slope(xs, ys):
    """Pearson r and OLS slope/intercept for paired claim-level series."""
    n = len(xs)
    mx, my = statistics.fmean(xs), statistics.fmean(ys)
    sxx = sum((x - mx) ** 2 for x in xs)
    syy = sum((y - my) ** 2 for y in ys)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    if sxx == 0 or syy == 0:
        return float("nan"), float("nan"), float("nan")
    return sxy / math.sqrt(sxx * syy), sxy / sxx, my - (sxy / sxx) * mx


def main() -> int:
    # --- item map: item_id -> (p2_id, arm) ---------------------------------
    arm_of, claim_of = {}, {}
    for line in open(ITEMS, encoding="utf-8"):
        d = json.loads(line)
        arm_of[d["item_id"]] = d["meta"]["arm"]
        claim_of[d["item_id"]] = d["meta"]["p2_id"]
    claims = sorted(set(claim_of.values()))
    assert len(claims) == 200, len(claims)
    assert len(arm_of) == 400, len(arm_of)

    # --- raws -> y[(model, claim)]{cell} -----------------------------------
    y = {}
    for tag in PANEL:
        y[tag] = {}
        n_tag = 0
        for arm in ("_plus", "_minus"):
            for line in open(RAW.format(tag=tag, arm=arm), encoding="utf-8"):
                r = json.loads(line)
                n_tag += 1
                assert r["value"] is not None, \
                    (tag, r["item_id"], r["kind_name"], "run the checker first")
                key = (arm_of[r["item_id"]], r["kind_name"])
                assert key in CELL_MAP, (tag, r["item_id"], key)
                rec = (claim_of[r["item_id"]], CELL_MAP[key])
                assert rec not in y[tag], (tag, rec)
                y[tag][rec] = float(r["value"])
        assert n_tag == 2600, (tag, n_tag)
    assert sum(len(v) for v in y.values()) == 6 * 200 * 13
    for tag in PANEL:
        for c in claims:
            for cell in CELLS:
                assert (c, cell) in y[tag], (tag, c, cell)

    # --- cells csv ----------------------------------------------------------
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["model", "p2_id", "cell", "value"])
        for tag in PANEL:
            for (c, cell), v in sorted(y[tag].items()):
                w.writerow([tag, c, cell, v])

    # --- per-claim components (model-averaged first; abs per-model first) ---
    def mavg(claim, cell):
        return statistics.fmean(y[m][(claim, cell)] for m in PANEL)

    keys = ["Y0", "ADM+", "ADM-"]
    for k in (OP_KEY[o] for o in OPS):
        keys += [k + "+", k + "-", "M_" + k, "sep_" + k,
                 "cre_signed_" + k, "cre_abs_" + k]
    comp = {k: [] for k in keys}
    for c in claims:
        v = {cell: mavg(c, cell) for cell in CELLS}
        comp["Y0"].append(v["Y0"])
        comp["ADM+"].append(v["ADM+"])
        comp["ADM-"].append(v["ADM-"])
        for op in OPS:
            k = OP_KEY[op]
            comp[k + "+"].append(v[k + "+"])
            comp[k + "-"].append(v[k + "-"])
            m_op = (v[k + "+"] + v[k + "-"]) / 2
            comp["M_" + k].append(m_op)
            comp["sep_" + k].append(v[k + "+"] - v[k + "-"])
            comp["cre_signed_" + k].append(v["Y0"] - m_op)
            # cell-level absolute value FIRST, then averaged over models
            comp["cre_abs_" + k].append(statistics.fmean(
                abs(y[m][(c, "Y0")] - (y[m][(c, k + "+")]
                                       + y[m][(c, k + "-")]) / 2)
                for m in PANEL))
    comp["sep_ADM"] = [a - b for a, b in zip(comp["ADM+"], comp["ADM-"])]

    def estimands(idx):
        out = {k: statistics.fmean(comp[k][j] for j in idx) for k in comp}
        mu = out
        out["cre_mnr_minus_cf"] = mu["cre_abs_MNR"] - mu["cre_abs_CF"]
        out["cre_rnd_minus_cf"] = mu["cre_abs_RND"] - mu["cre_abs_CF"]
        out["sep_mnr_minus_adm"] = mu["sep_MNR"] - mu["sep_ADM"]
        out["sep_mnr_minus_cf"] = mu["sep_MNR"] - mu["sep_CF"]
        ys = [comp["Y0"][j] for j in idx]
        for op in OPS:
            k = OP_KEY[op]
            r, slope, intercept = corr_slope(ys, [comp["M_" + k][j]
                                                  for j in idx])
            out["corr_" + k] = r
            out["slope_" + k] = slope
        out["slope_mnr_minus_cf"] = out["slope_MNR"] - out["slope_CF"]
        out["corr_mnr_minus_cf"] = out["corr_MNR"] - out["corr_CF"]
        return out

    all_idx = list(range(200))
    point = estimands(all_idx)
    assert all(point[k] == point[k] for k in point), "NaN in point estimates"

    # --- paired bootstrap over claims --------------------------------------
    rng = random.Random(SEED)
    keep = {k: [] for k in point}
    skipped = 0
    for _ in range(B):
        idx = [rng.randrange(200) for _ in range(200)]
        est = estimands(idx)
        if any(v != v for v in est.values()):
            skipped += 1
            continue
        for k, v in est.items():
            keep[k].append(v)
    ci = {k: quantiles(v, (0.025, 0.975)) for k, v in keep.items()}
    assert all(len(v) == B - skipped for v in keep.values())

    # --- per-model estimands + consistency (n/6) ---------------------------
    per_model = {}
    for m in PANEL:
        def cell(c, name, _m=m):
            return y[_m][(c, name)]
        e = {}
        e["Y0"] = statistics.fmean(cell(c, "Y0") for c in claims)
        e["sep_ADM"] = statistics.fmean(cell(c, "ADM+") - cell(c, "ADM-")
                                        for c in claims)
        ys = [cell(c, "Y0") for c in claims]
        for op in OPS:
            k = OP_KEY[op]
            e["sep_" + k] = statistics.fmean(
                cell(c, k + "+") - cell(c, k + "-") for c in claims)
            e["cre_signed_" + k] = statistics.fmean(
                cell(c, "Y0") - (cell(c, k + "+") + cell(c, k + "-")) / 2
                for c in claims)
            e["cre_abs_" + k] = statistics.fmean(
                abs(cell(c, "Y0") - (cell(c, k + "+") + cell(c, k + "-")) / 2)
                for c in claims)
            r, slope, intercept = corr_slope(
                ys, [(cell(c, k + "+") + cell(c, k + "-")) / 2
                     for c in claims])
            e["corr_" + k], e["slope_" + k] = r, slope
        e["cre_mnr_minus_cf"] = e["cre_abs_MNR"] - e["cre_abs_CF"]
        e["cre_rnd_minus_cf"] = e["cre_abs_RND"] - e["cre_abs_CF"]
        e["sep_mnr_minus_adm"] = e["sep_MNR"] - e["sep_ADM"]
        e["sep_mnr_minus_cf"] = e["sep_MNR"] - e["sep_CF"]
        e["slope_mnr_minus_cf"] = e["slope_MNR"] - e["slope_CF"]
        e["corr_mnr_minus_cf"] = e["corr_MNR"] - e["corr_CF"]
        e["cell_means"] = {name: statistics.fmean(cell(c, name)
                                                  for c in claims)
                           for name in CELLS}
        per_model[m] = e

    pooled_sign = {k: (point[k] > 0) for k in ("sep_MNR", "sep_CF")}
    consistency = {
        "cre_abs_mnr_lt_cf": sum(
            1 for m in PANEL if per_model[m]["cre_abs_MNR"]
            < per_model[m]["cre_abs_CF"]),
        "cre_abs_rnd_lt_cf": sum(
            1 for m in PANEL if per_model[m]["cre_abs_RND"]
            < per_model[m]["cre_abs_CF"]),
        "sep_mnr_lt_adm": sum(
            1 for m in PANEL if per_model[m]["sep_MNR"]
            < per_model[m]["sep_ADM"]),
        "sep_mnr_pooled_sign": sum(
            1 for m in PANEL if (per_model[m]["sep_MNR"] > 0)
            == pooled_sign["sep_MNR"]),
        "slope_mnr_gt_cf": sum(1 for m in PANEL
                               if per_model[m]["slope_MNR"]
                               > per_model[m]["slope_CF"]),
        "corr_mnr_gt_cf": sum(1 for m in PANEL
                              if per_model[m]["corr_MNR"]
                              > per_model[m]["corr_CF"]),
    }

    # --- committed context (descriptive only, never a gate) ----------------
    try:
        conf = json.load(open(CONF_JSON, encoding="utf-8"))
        ctx = {
            "confB_recon_abs": conf["rq2"][
                "recon_abs_mean_abs_Y0_minus_MCF"]["pooled"],
            "confB_sep_admit": conf["rq2"]["separation_admit"]["pooled"],
            "confB_sep_cf": conf["rq2"]["separation_cf"]["pooled"],
            "confB_slope": conf["rq3"]["ols_slope"]["pooled"],
            "confB_corr": conf["rq3"]["corr_MCF_Y0"]["pooled"],
        }
    except Exception:
        ctx = {}
    try:
        p2 = json.load(open(P2_JSON, encoding="utf-8"))["operators"]
        ctx.update({
            "discovery_slope_cf": p2["counterfactual_delete_post"]["ols_slope"],
            "discovery_corr_cf": p2["counterfactual_delete_post"]["corr_M_Y0"],
        })
    except Exception:
        pass

    payload = {
        "spec": "registration §14.4 (estimands + directions registered "
                "pre-run, user 2026-09-26); reporting, NOT gates",
        "n_claims": len(claims),
        "n_models": len(PANEL),
        "n_rows": sum(len(v) for v in y.values()),
        "bootstrap": {"unit": "claim", "paired": True, "B": B, "seed": SEED,
                      "skipped_nan_replicates": skipped},
        "context_committed_descriptive": ctx,
        "cell_means": {k: {"pooled": point[k], "ci95": ci[k],
                           "per_model": {m: per_model[m]["cell_means"][k]
                                         for m in PANEL}}
                       for k in CELLS},
        "cre": {
            k: {"abs": {"pooled": point["cre_abs_" + k],
                        "ci95": ci["cre_abs_" + k],
                        "per_model": {m: per_model[m]["cre_abs_" + k]
                                      for m in PANEL}},
                "signed": {"pooled": point["cre_signed_" + k],
                           "ci95": ci["cre_signed_" + k],
                           "per_model": {m: per_model[m]["cre_signed_" + k]
                                         for m in PANEL}}}
            for k in ("EXC", "STR", "CF", "MNR", "RND")},
        "cre_contrasts": {
            "mnr_minus_cf": {"pooled": point["cre_mnr_minus_cf"],
                             "ci95": ci["cre_mnr_minus_cf"],
                             "per_model": {m: per_model[m]["cre_mnr_minus_cf"]
                                           for m in PANEL}},
            "rnd_minus_cf": {"pooled": point["cre_rnd_minus_cf"],
                             "ci95": ci["cre_rnd_minus_cf"],
                             "per_model": {m: per_model[m]["cre_rnd_minus_cf"]
                                           for m in PANEL}},
        },
        "separation": {
            k: {"pooled": point["sep_" + k], "ci95": ci["sep_" + k],
                "per_model": {m: per_model[m]["sep_" + k] for m in PANEL}}
            for k in ("ADM", "EXC", "STR", "CF", "MNR", "RND")},
        "separation_contrasts": {
            "mnr_minus_admit": {"pooled": point["sep_mnr_minus_adm"],
                                "ci95": ci["sep_mnr_minus_adm"],
                                "per_model": {m: per_model[m]["sep_mnr_minus_adm"]
                                              for m in PANEL}},
            "mnr_minus_cf": {"pooled": point["sep_mnr_minus_cf"],
                             "ci95": ci["sep_mnr_minus_cf"],
                             "per_model": {m: per_model[m]["sep_mnr_minus_cf"]
                                           for m in PANEL}},
        },
        "trajectory": {
            k: {"corr": {"pooled": point["corr_" + k],
                         "ci95": ci["corr_" + k],
                         "per_model": {m: per_model[m]["corr_" + k]
                                       for m in PANEL}},
                "slope": {"pooled": point["slope_" + k],
                          "ci95": ci["slope_" + k],
                          "per_model": {m: per_model[m]["slope_" + k]
                                        for m in PANEL}}}
            for k in ("EXC", "STR", "CF", "MNR", "RND")},
        "trajectory_contrasts": {
            "slope_mnr_minus_cf": {"pooled": point["slope_mnr_minus_cf"],
                                   "ci95": ci["slope_mnr_minus_cf"],
                                   "per_model": {m: per_model[m]["slope_mnr_minus_cf"]
                                                 for m in PANEL}},
            "corr_mnr_minus_cf": {"pooled": point["corr_mnr_minus_cf"],
                                  "ci95": ci["corr_mnr_minus_cf"],
                                  "per_model": {m: per_model[m]["corr_mnr_minus_cf"]
                                                for m in PANEL}},
        },
        "consistency_n_of_6": consistency,
        "registered_expectations": {
            "cre_abs_MNR_vs_CF": "CRE(MNR) < CRE(CF)",
            "cre_abs_RND_vs_CF": "CRE(RND) < CRE(CF)",
            "sep_MNR": "≈ separation(CF) ≈ 0, ≪ separation(admit); the ≈0 "
                       "side has no registered sign -> consistency counts "
                       "pooled-sign agreement (descriptive, threshold-free)",
            "slope_MNR": "> slope(CF), moving toward 1",
            "corr_MNR": "> corr(CF) (same direction)",
        },
    }
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=1, sort_keys=True)
        fh.write("\n")

    # --- markdown -----------------------------------------------------------
    def row(label, key, expect, fmt="+.2f"):
        sv, slo, shi = (format(point[key], fmt),
                       format(ci[key][0], fmt),
                       format(ci[key][1], fmt))
        return f"| {label} | {sv} | [{slo}, {shi}] | {expect} |"

    n_rows = sum(len(v) for v in y.values())
    L = ["# G24A §14 explanation experiment — second-order / meta-evidence "
         "readout (v1, 2026-09-26)", ""]
    L.append("Registration §14.4 estimands on the committed 200 discovery "
             "same-claim pairs x 13 cells x 6 models (incl. the frozen "
             f"Qwen3-32B) = {n_rows:,} rows. "
             "**Reporting, NOT gates**: paired percentile bootstrap 95% "
             "CIs over claims (B = 10,000, seed `g24a_meta_ci_v1`), "
             "per-model consistency n/6, no p-values, no thresholds, no "
             "selection — every claim and model is included. Integrity: "
             "`check_g24a_meta_raws.py --require6` green. The four legacy "
             "operators were re-run in this batch (byte-identical prompts), "
             "so every contrast below is same-run, same-anchor.")
    L += ["", "## 1. All thirteen cell means (pooled, 0..100)", "",
          "| cell | pooled | 95% CI | per-model (6) |", "|---|---:|---:|---|"]
    for k in CELLS:
        v, (lo, hi) = point[k], ci[k]
        pm = ", ".join(f"{per_model[m]['cell_means'][k]:.1f}" for m in PANEL)
        L.append(f"| {k} | {v:.2f} | [{lo:.2f}, {hi:.2f}] | {pm} |")
    L += ["", "## 2. CRE — counterfactual restoration error (§14.4 "
          "criterion)", "",
          "| estimand | pooled | 95% CI | registered expectation |",
          "|---|---:|---:|---|"]
    labels = {"EXC": "ordinary exclude_post", "STR": "strong_exclude_post",
              "CF": "counterfactual_delete_post", "MNR": "meta_neutral_post (MNR)",
              "RND": "random_reason_post"}
    for k in ("EXC", "STR", "CF", "MNR", "RND"):
        L.append(row(f"CRE_abs({labels[k]}) = mean|Y0 − M|", "cre_abs_" + k,
                     "MNR < CF, RND < CF" if k in ("MNR", "RND") else "table"))
    for k in ("EXC", "STR", "CF", "MNR", "RND"):
        L.append(row(f"CRE_sgn({labels[k]}) = mean(Y0 − M)", "cre_signed_" + k,
                     "descriptive (no registered sign)"))
    L.append(row("CRE(MNR) − CRE(CF)", "cre_mnr_minus_cf", "< 0"))
    L.append(row("CRE(RND) − CRE(CF)", "cre_rnd_minus_cf", "< 0"))
    L += ["", "## 3. Separation — first-order direction (must not reopen)",
          "",
          "| estimand | pooled | 95% CI | registered expectation |",
          "|---|---:|---:|---|"]
    L.append(row("sep(admit_post)", "sep_ADM", "direction anchor"))
    for k in ("EXC", "STR", "CF", "MNR", "RND"):
        L.append(row(f"sep({labels[k]})", "sep_" + k,
                     "≈ 0 (MNR/CF/RND) / table"))
    L.append(row("sep(MNR) − sep(admit)", "sep_mnr_minus_adm", "< 0"))
    L.append(row("sep(MNR) − sep(CF)", "sep_mnr_minus_cf",
                 "≈ 0 (no registered sign)"))
    L += ["", "## 4. Reconstruction trajectory (claim-level, "
          "model-averaged)", "",
          "| estimand | pooled | 95% CI | registered expectation |",
          "|---|---:|---:|---|"]
    for k in ("EXC", "STR", "CF", "MNR", "RND"):
        L.append(row(f"corr(M_{k}, Y0)", "corr_" + k, "> 0", "+.3f"))
    for k in ("EXC", "STR", "CF", "MNR", "RND"):
        L.append(row(f"OLS slope (M_{k} ~ Y0)", "slope_" + k,
                     "MNR > CF, toward 1" if k in ("MNR",) else "table",
                     "+.3f"))
    L.append(row("slope(MNR) − slope(CF)", "slope_mnr_minus_cf", "> 0", "+.3f"))
    L.append(row("corr(MNR) − corr(CF)", "corr_mnr_minus_cf", "> 0", "+.3f"))
    if ctx:
        L += ["", "- Committed context (descriptive, never a gate):"]
        if "confB_recon_abs" in ctx:
            L.append(f"  - fresh ConfB (same-run §13.5): CRE(CF) = "
                     f"{ctx['confB_recon_abs']:.2f}, sep(admit) = "
                     f"{ctx['confB_sep_admit']:.2f}, sep(CF) = "
                     f"{ctx['confB_sep_cf']:.2f}, slope = "
                     f"{ctx['confB_slope']:.3f}, corr = "
                     f"{ctx['confB_corr']:.3f}.")
        if "discovery_slope_cf" in ctx:
            L.append(f"  - discovery P2 (5 models): slope(CF) = "
                     f"{ctx['discovery_slope_cf']:.3f}, corr(CF) = "
                     f"{ctx['discovery_corr_cf']:.3f}.")
    L += ["", "## 5. Per-model consistency (n/6)", ""]
    labels6 = [
        ("cre_abs_mnr_lt_cf", "CRE(MNR) < CRE(CF)"),
        ("cre_abs_rnd_lt_cf", "CRE(RND) < CRE(CF)"),
        ("sep_mnr_lt_adm", "sep(MNR) < sep(admit)"),
        ("sep_mnr_pooled_sign",
         "sep(MNR) on the pooled sign (≈0 has no registered sign)"),
        ("slope_mnr_gt_cf", "slope(MNR) > slope(CF)"),
        ("corr_mnr_gt_cf", "corr(MNR) > corr(CF)"),
    ]
    for k, label in labels6:
        L.append(f"- {label}: **{consistency[k]} / 6**")
    L += ["", "Per-model values:", "",
          "| model | CRE_EXC | CRE_STR | CRE_CF | CRE_MNR | CRE_RND | "
          "sep_adm | sep_MNR | r_CF | r_MNR | slope_CF | slope_MNR |",
          "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for m in PANEL:
        e = per_model[m]
        L.append(
            f"| {m} | {e['cre_abs_EXC']:.2f} | {e['cre_abs_STR']:.2f} | "
            f"{e['cre_abs_CF']:.2f} | {e['cre_abs_MNR']:.2f} | "
            f"{e['cre_abs_RND']:.2f} | {e['sep_ADM']:.2f} | "
            f"{e['sep_MNR']:+.2f} | {e['corr_CF']:+.3f} | "
            f"{e['corr_MNR']:+.3f} | {e['slope_CF']:+.3f} | "
            f"{e['slope_MNR']:+.3f} |")
    L += ["", "## 6. Reading rules (registered)", ""]
    L.append("- Everything above is reported as-is whatever the outcome "
             "(§14.4 interpretation rule); CIs quantify claim-sampling "
             "uncertainty, n/6 shows whether a pattern spans the panel "
             "rather than resting on one model.")
    L.append("- Registered expectations are quoted for the reader, never "
             "evaluated as pass/fail — there are no gates, thresholds, or "
             "p-values anywhere in this report.")
    L.append("- Pooled means average all (model, claim) cells (discovery "
             "convention); corr/slope use claim-level series first averaged "
             "over the 6 models; `mean|Y0 − M|` takes the cell-level "
             "absolute value before averaging. The bootstrap recomputes "
             "every ratio and correlation inside each resample "
             f"(NaN replicates skipped: {skipped}/{B}).")
    L.append("- Conceptual framing (§14.4): CRE = |Y0 − M| is proposed as "
             "*the* retraction-success criterion — evidence suppression "
             "(forget rate) and counterfactual restoration are different "
             "properties, and a retraction operator succeeds only when the "
             "judgment it leaves behind equals the judgment that never saw "
             "the evidence.")
    L.append("- Scope: this is RQ3's explanation experiment (§14 ruling); "
             "internal layerwise/patching analysis is out of scope this "
             "round and requires a new user ruling.")
    L.append("")
    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))

    print(f"wrote {OUT_MD}, {OUT_JSON}, {OUT_CSV}")
    for k in [*(f"cre_abs_{x}" for x in ("EXC", "STR", "CF", "MNR", "RND")),
              "cre_mnr_minus_cf", "cre_rnd_minus_cf",
              *(f"sep_{x}" for x in ("ADM", "EXC", "STR", "CF", "MNR", "RND")),
              "sep_mnr_minus_adm", "sep_mnr_minus_cf",
              *(f"slope_{x}" for x in ("CF", "MNR", "RND")),
              "slope_mnr_minus_cf"]:
        lo, hi = ci[k]
        print(f"  {k:22s} {point[k]:+9.3f}  CI [{lo:+.3f}, {hi:+.3f}]")
    print("  consistency n/6:", consistency)
    return 0


if __name__ == "__main__":
    sys.exit(main())
