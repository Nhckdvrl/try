#!/usr/bin/env python3
"""G24A Confirmation B — RQ2/F2 + RQ3/F3 replication readout (§13.5).

Frozen estimands (registered pre-run, user 2026-09-26; reporting, NOT
gates).  Cells per (model, claim): Y0 = plus base; A+ = plus admit_post;
CF+ = plus counterfactual_delete_post; A- = minus admit_post;
CF- = minus counterfactual_delete_post; W = plus withheld_cf;
I = control irrelevant_cf.  M_CF = (CF+ + CF-) / 2.

RQ2 / F2 (suppression != restoration), all pooled over (model, claim):
  separation_admit = mean(A+ - A-)
  separation_cf    = mean(CF+ - CF-)
  gap              = separation_cf - separation_admit   (expected < 0)
  erased fraction  = 1 - separation_cf / separation_admit   (descriptive)
  signed reconstruction error   mean(Y0 - M_CF)          (expected != 0)
  absolute reconstruction error mean|Y0 - M_CF|          (cell-level
      absolute value first, then averaged; expected still large)

RQ3 / F3 (retraction induces a new inference state), claim-level with
each claim averaged over the 6 models first:
  corr(M_CF, Y0) > 0 with OLS slope < 1 (discovery: 0.701 / 0.385)
  center ordering (mean):       W > I ~ M_CF   -> gaps W-I (>0), W-M (>0),
                                                 I-M (~0, no registered sign)
  dispersion ordering (mean|Y-50|): W > I > M_CF -> gaps dW-dI (>0),
                                                 dI-dM (>0)

Reporting method (§13.5): paired percentile bootstrap 95% CIs,
resampling CLAIMS with every model's cells moving together, B = 10,000,
seed "g24a_confb_ci_v1"; per-model consistency as n/6 on the registered
side.  For expectations with no registered sign (~0: I-M and the signed
reconstruction error) consistency is reported as n/6 on the sign of the
POOLED estimate — a descriptive panel-agreement count, threshold-free.
No p-values, no thresholds, no selection: 200 claims x 7 cells x 6 models.

Input:  results/raw/{tag}_g24a_confb_{plus,minus,control}.jsonl x 6 tags
        (check_g24a_confb_raws.py --require6 must be green first)
        data/items/g24a_confb_v1.jsonl   (arm / claim map)
        results/g24a/g24a_p3_analysis_v1.json  (temp-0 noise floor,
        descriptive reference only)
Output: results/g24a/g24a_confb_analysis_v1.{md,json}
        results/g24a/g24a_confb_analysis_v1_cells.csv
Usage: python src/analyze_g24a_confb.py
"""
from __future__ import annotations

import csv
import json
import math
import random
import statistics
import sys

RAW = "results/raw/{tag}_g24a_confb{arm}.jsonl"
ITEMS = "data/items/g24a_confb_v1.jsonl"
P3_JSON = "results/g24a/g24a_p3_analysis_v1.json"
OUT_MD = "results/g24a/g24a_confb_analysis_v1.md"
OUT_JSON = "results/g24a/g24a_confb_analysis_v1.json"
OUT_CSV = "results/g24a/g24a_confb_analysis_v1_cells.csv"

PANEL = ["mistral-small-24b", "llama31-8b", "qwen3-8b", "qwen35-9b",
         "gemma3-12b", "qwen3-32b"]
# raw row -> canonical cell name (arm, kind) per §13.3's 7 issued cells
CELL_MAP = {
    ("plus", "base"): "Y0",
    ("plus", "admit_post"): "A+",
    ("plus", "counterfactual_delete_post"): "CF+",
    ("minus", "admit_post"): "A-",
    ("minus", "counterfactual_delete_post"): "CF-",
    ("plus", "withheld_cf"): "W",
    ("control", "irrelevant_cf"): "I",
}
CELLS = ["Y0", "A+", "CF+", "A-", "CF-", "W", "I"]
B = 10_000                      # registered bootstrap resamples
SEED = "g24a_confb_ci_v1"


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
    # --- item map: item_id -> (cfb_id, arm) --------------------------------
    arm_of, cfb_of = {}, {}
    for line in open(ITEMS, encoding="utf-8"):
        d = json.loads(line)
        arm_of[d["item_id"]] = d["meta"]["arm"]
        cfb_of[d["item_id"]] = d["meta"]["cfb_id"]
    claims = sorted(set(cfb_of.values()))
    assert len(claims) == 200, len(claims)
    assert len(arm_of) == 600, len(arm_of)

    # --- raws -> y[(model, claim)]{cell} -----------------------------------
    y = {}
    for tag in PANEL:
        y[tag] = {}
        n_tag = 0
        for arm in ("_plus", "_minus", "_control"):
            for line in open(RAW.format(tag=tag, arm=arm), encoding="utf-8"):
                r = json.loads(line)
                n_tag += 1
                assert r["value"] is not None, \
                    (tag, r["item_id"], r["kind_name"], "run the checker first")
                key = (arm_of[r["item_id"]], r["kind_name"])
                assert key in CELL_MAP, (tag, r["item_id"], key)
                rec = (cfb_of[r["item_id"]], CELL_MAP[key])
                assert rec not in y[tag], (tag, rec)
                y[tag][rec] = float(r["value"])
        assert n_tag == 1400, (tag, n_tag)
    assert sum(len(v) for v in y.values()) == 6 * 200 * 7
    for tag in PANEL:
        for c in claims:
            for cell in CELLS:
                assert (c, cell) in y[tag], (tag, c, cell)

    # --- cells csv ----------------------------------------------------------
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["model", "cfb_id", "cell", "value"])
        for tag in PANEL:
            for (c, cell), v in sorted(y[tag].items()):
                w.writerow([tag, c, cell, v])

    # --- per-claim components (model-averaged first) ------------------------
    def mavg(claim, cell):
        return statistics.fmean(y[m][(claim, cell)] for m in PANEL)

    comp = {k: [] for k in
            ("Y0", "A+", "CF+", "A-", "CF-", "W", "I", "M_CF",
             "sep_admit", "sep_cf", "recon_signed", "recon_abs",
             "dW", "dI", "dM")}
    for c in claims:
        v = {cell: mavg(c, cell) for cell in CELLS}
        mcf = (v["CF+"] + v["CF-"]) / 2
        comp["Y0"].append(v["Y0"])
        comp["A+"].append(v["A+"])
        comp["CF+"].append(v["CF+"])
        comp["A-"].append(v["A-"])
        comp["CF-"].append(v["CF-"])
        comp["W"].append(v["W"])
        comp["I"].append(v["I"])
        comp["M_CF"].append(mcf)
        comp["sep_admit"].append(v["A+"] - v["A-"])
        comp["sep_cf"].append(v["CF+"] - v["CF-"])
        comp["recon_signed"].append(v["Y0"] - mcf)
        # cell-level absolute value FIRST, then averaged over models
        comp["recon_abs"].append(statistics.fmean(
            abs(y[m][(c, "Y0")] - (y[m][(c, "CF+")] + y[m][(c, "CF-")]) / 2)
            for m in PANEL))
        for name, cell in (("dW", "W"), ("dI", "I")):
            comp[name].append(statistics.fmean(
                abs(y[m][(c, cell)] - 50.0) for m in PANEL))
        comp["dM"].append(statistics.fmean(
            abs((y[m][(c, "CF+")] + y[m][(c, "CF-")]) / 2 - 50.0)
            for m in PANEL))

    def estimands(idx):
        out = {k: statistics.fmean(comp[k][j] for j in idx)
               for k in comp}
        mu = out
        out["gap_sep"] = mu["sep_cf"] - mu["sep_admit"]
        out["erased"] = (1 - mu["sep_cf"] / mu["sep_admit"]
                         if mu["sep_admit"] else float("nan"))
        out["W_minus_I"] = mu["W"] - mu["I"]
        out["W_minus_M"] = mu["W"] - mu["M_CF"]
        out["I_minus_M"] = mu["I"] - mu["M_CF"]
        out["dW_minus_dI"] = mu["dW"] - mu["dI"]
        out["dI_minus_dM"] = mu["dI"] - mu["dM"]
        r, slope, intercept = corr_slope(
            [comp["Y0"][j] for j in idx], [comp["M_CF"][j] for j in idx])
        out["corr_MCF_Y0"] = r
        out["slope"] = slope
        out["intercept"] = intercept
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

    # --- per-model estimands + consistency (n/6) ----------------------------
    per_model = {}
    for m in PANEL:
        def cell(c, name, _m=m):
            return y[_m][(c, name)]
        e = {}
        e["sep_admit"] = statistics.fmean(
            cell(c, "A+") - cell(c, "A-") for c in claims)
        e["sep_cf"] = statistics.fmean(
            cell(c, "CF+") - cell(c, "CF-") for c in claims)
        e["gap_sep"] = e["sep_cf"] - e["sep_admit"]
        e["erased"] = (1 - e["sep_cf"] / e["sep_admit"]
                       if e["sep_admit"] else float("nan"))
        e["recon_signed"] = statistics.fmean(
            cell(c, "Y0") - (cell(c, "CF+") + cell(c, "CF-")) / 2
            for c in claims)
        e["recon_abs"] = statistics.fmean(
            abs(cell(c, "Y0") - (cell(c, "CF+") + cell(c, "CF-")) / 2)
            for c in claims)
        e["M_CF"] = statistics.fmean(
            (cell(c, "CF+") + cell(c, "CF-")) / 2 for c in claims)
        e["Y0"] = statistics.fmean(cell(c, "Y0") for c in claims)
        e["W"] = statistics.fmean(cell(c, "W") for c in claims)
        e["I"] = statistics.fmean(cell(c, "I") for c in claims)
        e["W_minus_I"] = e["W"] - e["I"]
        e["W_minus_M"] = e["W"] - e["M_CF"]
        e["I_minus_M"] = e["I"] - e["M_CF"]
        e["dW"] = statistics.fmean(abs(cell(c, "W") - 50.0) for c in claims)
        e["dI"] = statistics.fmean(abs(cell(c, "I") - 50.0) for c in claims)
        e["dM"] = statistics.fmean(
            abs((cell(c, "CF+") + cell(c, "CF-")) / 2 - 50.0)
            for c in claims)
        e["dW_minus_dI"] = e["dW"] - e["dI"]
        e["dI_minus_dM"] = e["dI"] - e["dM"]
        r, slope, intercept = corr_slope(
            [cell(c, "Y0") for c in claims],
            [(cell(c, "CF+") + cell(c, "CF-")) / 2 for c in claims])
        e["corr_MCF_Y0"], e["slope"], e["intercept"] = r, slope, intercept
        e["cell_means"] = {name: statistics.fmean(cell(c, name)
                                                  for c in claims)
                           for name in CELLS}
        per_model[m] = e

    pooled_sign = {k: (point[k] > 0) for k in
                   ("recon_signed", "I_minus_M")}
    consistency = {
        "sep_cf_lt_sep_admit": sum(
            1 for m in PANEL if per_model[m]["sep_cf"]
            < per_model[m]["sep_admit"]),
        "recon_signed_pooled_sign": sum(
            1 for m in PANEL if (per_model[m]["recon_signed"] > 0)
            == pooled_sign["recon_signed"]),
        "corr_gt_0": sum(1 for m in PANEL
                         if per_model[m]["corr_MCF_Y0"] > 0),
        "slope_lt_1": sum(1 for m in PANEL
                          if per_model[m]["slope"] < 1),
        "W_minus_I_gt_0": sum(1 for m in PANEL
                              if per_model[m]["W_minus_I"] > 0),
        "W_minus_M_gt_0": sum(1 for m in PANEL
                              if per_model[m]["W_minus_M"] > 0),
        "I_minus_M_pooled_sign": sum(
            1 for m in PANEL if (per_model[m]["I_minus_M"] > 0)
            == pooled_sign["I_minus_M"]),
        "dW_minus_dI_gt_0": sum(1 for m in PANEL
                                if per_model[m]["dW_minus_dI"] > 0),
        "dI_minus_dM_gt_0": sum(1 for m in PANEL
                                if per_model[m]["dI_minus_dM"] > 0),
    }

    try:
        noise = json.load(open(P3_JSON, encoding="utf-8"))[
            "base_rerun_vs_p2_base"]["mean_abs_diff"]
    except Exception:
        noise = None

    payload = {
        "spec": "registration §13.5 (estimands + directions registered "
                "pre-run, user 2026-09-26); reporting, NOT gates",
        "n_claims": len(claims),
        "n_models": len(PANEL),
        "n_rows": sum(len(v) for v in y.values()),
        "bootstrap": {"unit": "claim", "paired": True, "B": B, "seed": SEED,
                      "skipped_nan_replicates": skipped},
        "noise_floor_reference_mean_abs_diff": noise,
        "cell_means": {k: {"pooled": point[k], "ci95": ci[k],
                           "per_model": {m: per_model[m]["cell_means"][k]
                                         for m in PANEL}}
                       for k in CELLS},
        "rq2": {
            "separation_admit": {"pooled": point["sep_admit"],
                                 "ci95": ci["sep_admit"],
                                 "per_model": {m: per_model[m]["sep_admit"]
                                               for m in PANEL}},
            "separation_cf": {"pooled": point["sep_cf"],
                              "ci95": ci["sep_cf"],
                              "per_model": {m: per_model[m]["sep_cf"]
                                            for m in PANEL}},
            "gap_cf_minus_admit": {"pooled": point["gap_sep"],
                                   "ci95": ci["gap_sep"],
                                   "per_model": {m: per_model[m]["gap_sep"]
                                                 for m in PANEL}},
            "erased_fraction": {"pooled": point["erased"],
                                "ci95": ci["erased"],
                                "per_model": {m: per_model[m]["erased"]
                                              for m in PANEL}},
            "recon_signed_mean_Y0_minus_MCF": {
                "pooled": point["recon_signed"], "ci95": ci["recon_signed"],
                "per_model": {m: per_model[m]["recon_signed"]
                              for m in PANEL}},
            "recon_abs_mean_abs_Y0_minus_MCF": {
                "pooled": point["recon_abs"], "ci95": ci["recon_abs"],
                "per_model": {m: per_model[m]["recon_abs"]
                              for m in PANEL}},
        },
        "rq3": {
            "corr_MCF_Y0": {"pooled": point["corr_MCF_Y0"],
                            "ci95": ci["corr_MCF_Y0"],
                            "per_model": {m: per_model[m]["corr_MCF_Y0"]
                                          for m in PANEL}},
            "ols_slope": {"pooled": point["slope"], "ci95": ci["slope"],
                          "per_model": {m: per_model[m]["slope"]
                                        for m in PANEL}},
            "ols_intercept": {"pooled": point["intercept"],
                              "ci95": ci["intercept"],
                              "per_model": {m: per_model[m]["intercept"]
                                            for m in PANEL}},
            "center_means": {k: {"pooled": point[k], "ci95": ci[k],
                                 "per_model": {m: per_model[m][k]
                                               for m in PANEL}}
                             for k in ("W", "I", "M_CF")},
            "center_gaps": {k: {"pooled": point[k], "ci95": ci[k],
                                "per_model": {m: per_model[m][k]
                                              for m in PANEL}}
                            for k in ("W_minus_I", "W_minus_M", "I_minus_M")},
            "dispersion_means_abs_Y_minus_50": {
                k: {"pooled": point[k], "ci95": ci[k],
                    "per_model": {m: per_model[m][k] for m in PANEL}}
                for k in ("dW", "dI", "dM")},
            "dispersion_gaps": {k: {"pooled": point[k], "ci95": ci[k],
                                    "per_model": {m: per_model[m][k]
                                                  for m in PANEL}}
                                for k in ("dW_minus_dI", "dI_minus_dM")},
        },
        "consistency_n_of_6": consistency,
        "registered_expectations": {
            "gap_sep": "< 0 (suppression erases direction: separation_cf "
                       "<<< separation_admit)",
            "recon_signed": "expected still large (!= ~0); no registered "
                            "sign -> consistency counts pooled-sign "
                            "agreement (descriptive, threshold-free)",
            "recon_abs": "expected still large (!= ~0), read against the "
                         "committed temp-0 noise floor as descriptive scale",
            "corr_MCF_Y0": "> 0", "ols_slope": "< 1",
            "W_minus_I": "> 0", "W_minus_M": "> 0",
            "I_minus_M": "approximately 0 (no registered sign) -> "
                         "consistency counts pooled-sign agreement",
            "dW_minus_dI": "> 0", "dI_minus_dM": "> 0",
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

    L = ["# G24A Confirmation B — RQ2/F2 + RQ3/F3 replication (v1, "
         "2026-09-26)", ""]
    L.append("Registration §13.5 estimands on 200 fresh VitaminC SR pairs "
             "(3 items each) x 7 cells x 6 models (incl. the frozen "
             f"Qwen3-32B) = {sum(len(v) for v in y.values()):,} rows. "
             "**Reporting, NOT gates**: paired percentile bootstrap 95% "
             "CIs over claims (B = 10,000, seed `g24a_confb_ci_v1`), "
             "per-model consistency n/6, no p-values, no thresholds, no "
             "selection — every claim and model is included. Integrity: "
             "`check_g24a_confb_raws.py --require6` green.")
    L += ["", "## 1. All seven cell means (pooled, 0..100)", "",
          "| cell | pooled | 95% CI | per-model (6) |", "|---|---:|---:|---|"]
    for k in CELLS:
        v, (lo, hi) = point[k], ci[k]
        pm = ", ".join(f"{per_model[m]['cell_means'][k]:.1f}" for m in PANEL)
        L.append(f"| {k} | {v:.2f} | [{lo:.2f}, {hi:.2f}] | {pm} |")
    L += ["", "## 2. RQ2 / F2 — suppression vs restoration", "",
          "| estimand | pooled | 95% CI | registered expectation |",
          "|---|---:|---:|---|"]
    L.append(row("separation_admit = mean(A+ − A−)", "sep_admit",
                 "admitted direction effect"))
    L.append(row("separation_cf = mean(CF+ − CF−)", "sep_cf",
                 "post-retraction direction effect"))
    L.append(row("gap = separation_cf − separation_admit", "gap_sep",
                 "< 0 (cf ≪ admit)"))
    L.append(row("erased fraction = 1 − cf/admit", "erased",
                 "descriptive", "+.3f"))
    L.append(row("mean(Y0 − M_CF)", "recon_signed",
                 "≠ ~0 (no registered sign)"))
    L.append(row("mean|Y0 − M_CF|", "recon_abs",
                 "still large (≠ ~0)"))
    L += ["", "## 3. RQ3 / F3 — new inference state (claim-level)", "",
          "| estimand | pooled | 95% CI | registered expectation |",
          "|---|---:|---:|---|"]
    L.append(row("corr(M_CF, Y0)", "corr_MCF_Y0", "> 0", "+.3f"))
    L.append(row("OLS slope (M_CF ~ Y0)", "slope", "< 1", "+.3f"))
    L.append(row("OLS intercept", "intercept", "descriptive", "+.2f"))
    L.append(row("center mean W (WithheldCF)", "W", "> I ≈ M_CF"))
    L.append(row("center mean I (IrrelCF)", "I", "≈ M_CF"))
    L.append(row("center mean M_CF", "M_CF", "anchor"))
    L.append(row("W − I", "W_minus_I", "> 0"))
    L.append(row("W − M_CF", "W_minus_M", "> 0"))
    L.append(row("I − M_CF", "I_minus_M", "≈ 0 (no registered sign)"))
    L.append(row("dW = mean|W − 50|", "dW", "> dI > dM"))
    L.append(row("dI = mean|I − 50|", "dI", "middle"))
    L.append(row("dM = mean|M_CF − 50|", "dM", "smallest"))
    L.append(row("dW − dI", "dW_minus_dI", "> 0"))
    L.append(row("dI − dM", "dI_minus_dM", "> 0"))
    if noise is not None:
        L += ["", f"- Descriptive scale reference (committed, discovery): "
              f"temp-0 noise floor mean|diff| = {noise:.2f} — every "
              "reconstruction/center gap above is read against this, "
              "calibration only (never a gate)."]
    L += ["", "## 4. Per-model consistency (n/6)", ""]
    labels = [
        ("sep_cf_lt_sep_admit", "separation_cf < separation_admit"),
        ("recon_signed_pooled_sign",
         "mean(Y0 − M_CF) on the pooled sign (≈0 has no registered sign)"),
        ("corr_gt_0", "corr(M_CF, Y0) > 0"),
        ("slope_lt_1", "OLS slope < 1"),
        ("W_minus_I_gt_0", "W − I > 0"),
        ("W_minus_M_gt_0", "W − M_CF > 0"),
        ("I_minus_M_pooled_sign",
         "I − M_CF on the pooled sign (≈0 has no registered sign)"),
        ("dW_minus_dI_gt_0", "dW − dI > 0"),
        ("dI_minus_dM_gt_0", "dI − dM > 0"),
    ]
    for k, label in labels:
        L.append(f"- {label}: **{consistency[k]} / 6**")
    L += ["", "Per-model values:", "",
          "| model | sep_adm | sep_cf | erased | Y0−MCF | |Y0−MCF| | r | "
          "slope | W | I | M_CF | W−I | I−M | dW−dI | dI−dM |",
          "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"
          "---:|---:|---:|"]
    for m in PANEL:
        e = per_model[m]
        L.append(
            f"| {m} | {e['sep_admit']:.2f} | {e['sep_cf']:.2f} | "
            f"{e['erased']:.3f} | {e['recon_signed']:+.2f} | "
            f"{e['recon_abs']:.2f} | {e['corr_MCF_Y0']:+.3f} | "
            f"{e['slope']:+.3f} | {e['W']:.2f} | {e['I']:.2f} | "
            f"{e['M_CF']:.2f} | {e['W_minus_I']:+.2f} | "
            f"{e['I_minus_M']:+.2f} | {e['dW_minus_dI']:+.2f} | "
            f"{e['dI_minus_dM']:+.2f} |")
    L += ["", "## 5. Reading rules (registered)", ""]
    L.append("- Everything above is reported as-is whatever the outcome "
             "(§13.5 interpretation rule); CIs quantify claim-sampling "
             "uncertainty, n/6 shows whether a pattern spans the panel "
             "rather than resting on one model.")
    L.append("- Pooled means average all (model, claim) cells (discovery "
             "convention); corr/slope and the center/dispersion ordering "
             "use claim-level series first averaged over the 6 models.")
    L.append("- `mean|Y0 − M_CF|` takes the cell-level absolute value "
             "before averaging; the bootstrap recomputes every ratio and "
             "correlation inside each resample "
             f"(NaN replicates skipped: {skipped}/{B}).")
    L.append("- After ConfA + ConfB are reported: experiments stop "
             "(§13.1).")
    L.append("")
    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))

    print(f"wrote {OUT_MD}, {OUT_JSON}, {OUT_CSV}")
    for k in ("sep_admit", "sep_cf", "gap_sep", "erased", "recon_signed",
              "recon_abs", "corr_MCF_Y0", "slope", "W_minus_I", "W_minus_M",
              "I_minus_M", "dW_minus_dI", "dI_minus_dM"):
        lo, hi = ci[k]
        print(f"  {k:12s} {point[k]:+9.3f}  CI [{lo:+.3f}, {hi:+.3f}]")
    print("  consistency n/6:", consistency)
    return 0


if __name__ == "__main__":
    sys.exit(main())
