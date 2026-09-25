#!/usr/bin/env python3
"""G24A Confirmation A — RQ1/F1 replication readout (registration §13.5).

Frozen estimands (registered pre-run; reporting, NOT gates; user
2026-09-26).  Sign-normalize every effect by critical_direction (+1
increase, -1 decrease; signed effect = d x (Y_cell - Y_base)):

  E1 signed(ExcludePre - Base)    E2 signed(ExcludePost - Base)
  E3 signed(AdmitPre  - Base)     E4 signed(AdmitPost  - Base)
  leak fractions E1/E3 and E2/E4

Registered expectations (quoted, never evaluated as pass/fail):
  E1 >> E2 (prospective leaks >> retrospective); E2/E4 close to 0
  (retrospective ~= removal); E1/E3 substantially > 0.

Reporting method (§13.5, user's explicit order for confirmation):
  * paired percentile bootstrap 95% CIs, resampling CLAIMS with all
    models' cells moving together, B = 10,000, seed "g24a_confa_ci_v1";
  * per-model consistency reported as n/6 (models on the registered
    side).  For E2/E4 — an expectation with no registered sign
    ("close to 0", thresholds are banned) — consistency is reported as
    n/6 models with E2/E4 < E1/E3, the ratio-level counterpart of the
    registered E1 - E2 > 0, using only registered quantities.
  * no p-values, no thresholds, no selection: all 500 items x 6 models.

Input:  results/raw/{tag}_g24a_confa.jsonl x 6 tags
        (check_g24a_confa_raws.py --require6 must be green first)
        data/items/g24a_confa_v1.jsonl   (critical_direction)
Output: results/g24a/g24a_confa_analysis_v1.{md,json}
        results/g24a/g24a_confa_analysis_v1_cells.csv
Usage: python src/analyze_g24a_confa.py
"""
from __future__ import annotations

import csv
import json
import random
import statistics
import sys

RAW = "results/raw/{tag}_g24a_confa.jsonl"
ITEMS = "data/items/g24a_confa_v1.jsonl"
OUT_MD = "results/g24a/g24a_confa_analysis_v1.md"
OUT_JSON = "results/g24a/g24a_confa_analysis_v1.json"
OUT_CSV = "results/g24a/g24a_confa_analysis_v1_cells.csv"

PANEL = ["mistral-small-24b", "llama31-8b", "qwen3-8b", "qwen35-9b",
         "gemma3-12b", "qwen3-32b"]
KINDS = ["base", "admit_pre", "admit_post", "exclude_pre", "exclude_post"]
B = 10_000                      # registered bootstrap resamples
SEED = "g24a_confa_ci_v1"


def quantiles(xs, qs):
    xs = sorted(xs)
    out = []
    for q in qs:
        i = q * (len(xs) - 1)
        lo, hi = int(i), min(int(i) + 1, len(xs) - 1)
        out.append(xs[lo] + (xs[hi] - xs[lo]) * (i - lo))
    return out


def main() -> int:
    # --- items: direction + claim key --------------------------------------
    d_of, claim_of = {}, {}
    for line in open(ITEMS, encoding="utf-8"):
        d = json.loads(line)
        d_of[d["item_id"]] = 1 if d["critical_direction"] == "increase" else -1
        claim_of[d["item_id"]] = d["base_context"]
    assert len(d_of) == 500, len(d_of)
    assert len(set(claim_of.values())) == 500, "one claim per item expected"
    items = sorted(d_of)

    # --- raws ---------------------------------------------------------------
    y = {}                       # (model, item, kind) -> value
    for tag in PANEL:
        n_tag = 0
        for line in open(RAW.format(tag=tag), encoding="utf-8"):
            r = json.loads(line)
            n_tag += 1
            assert r["value"] is not None, \
                (tag, r["item_id"], r["kind_name"], "run the raw checker first")
            key = (tag, r["item_id"], r["kind_name"])
            assert key not in y, key
            y[key] = float(r["value"])
        assert n_tag == 2500, (tag, n_tag)
    assert len(y) == 500 * 5 * 6, len(y)
    for m in PANEL:
        for i in items:
            for k in KINDS:
                assert (m, i, k) in y, (m, i, k)

    # --- cells csv ----------------------------------------------------------
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["model", "item_id", "kind", "direction", "value"])
        for (m, i, k), v in sorted(y.items()):
            w.writerow([m, i, k, d_of[i], v])

    # --- per-claim components (model-averaged) ------------------------------
    def sgn(m, i, k):
        return d_of[i] * (y[(m, i, k)] - y[(m, i, "base")])

    comp = {name: [] for name in
            ("base", "admit_pre", "admit_post", "exclude_pre", "exclude_post",
             "E1", "E2", "E3", "E4")}
    for i in items:
        for k in ("base", "admit_pre", "admit_post", "exclude_pre",
                  "exclude_post"):
            comp[k].append(statistics.fmean(y[(m, i, k)] for m in PANEL))
        comp["E1"].append(statistics.fmean(sgn(m, i, "exclude_pre")
                                           for m in PANEL))
        comp["E2"].append(statistics.fmean(sgn(m, i, "exclude_post")
                                           for m in PANEL))
        comp["E3"].append(statistics.fmean(sgn(m, i, "admit_pre")
                                           for m in PANEL))
        comp["E4"].append(statistics.fmean(sgn(m, i, "admit_post")
                                           for m in PANEL))

    def estimands(idx):
        mu = {k: statistics.fmean(comp[k][j] for j in idx)
              for k in comp}
        e1, e2, e3, e4 = mu["E1"], mu["E2"], mu["E3"], mu["E4"]
        out = {k: mu[k] for k in comp}
        out["E1_minus_E2"] = e1 - e2
        out["E1_over_E3"] = e1 / e3 if e3 else float("nan")
        out["E2_over_E4"] = e2 / e4 if e4 else float("nan")
        return out

    all_idx = list(range(500))
    point = estimands(all_idx)

    # --- paired bootstrap over claims --------------------------------------
    rng = random.Random(SEED)
    keep = {k: [] for k in point}
    skipped = 0
    for _ in range(B):
        idx = [rng.randrange(500) for _ in range(500)]
        est = estimands(idx)
        if any(v != v for v in est.values()):     # NaN denominator skip
            skipped += 1
            continue
        for k, v in est.items():
            keep[k].append(v)
    ci = {k: quantiles(v, (0.025, 0.975)) for k, v in keep.items()}
    assert all(len(v) == B - skipped for v in keep.values())

    # --- per-model estimands + consistency (n/6) ----------------------------
    per_model = {}
    for m in PANEL:
        def mm(i, k):
            return d_of[i] * (y[(m, i, k)] - y[(m, i, "base")])
        e = {}
        for tag_k, kind in (("E1", "exclude_pre"), ("E2", "exclude_post"),
                            ("E3", "admit_pre"), ("E4", "admit_post")):
            e[tag_k] = statistics.fmean(mm(i, kind) for i in items)
        e["E1_minus_E2"] = e["E1"] - e["E2"]
        e["E1_over_E3"] = e["E1"] / e["E3"] if e["E3"] else float("nan")
        e["E2_over_E4"] = e["E2"] / e["E4"] if e["E4"] else float("nan")
        e["cell_means"] = {k: statistics.fmean(y[(m, i, k)]
                                               for i in items)
                           for k in KINDS}
        per_model[m] = e

    consistency = {
        "E1_minus_E2_gt_0": sum(1 for m in PANEL
                                if per_model[m]["E1_minus_E2"] > 0),
        "E1_over_E3_gt_0": sum(1 for m in PANEL
                               if per_model[m]["E1_over_E3"] > 0),
        "E2_over_E4_lt_E1_over_E3": sum(1 for m in PANEL
                                        if per_model[m]["E2_over_E4"]
                                        < per_model[m]["E1_over_E3"]),
    }

    payload = {
        "spec": "registration §13.5 (estimands + directions registered "
                "pre-run, user 2026-09-26); reporting, NOT gates",
        "n_items": len(items),
        "n_models": len(PANEL),
        "n_rows": len(y),
        "bootstrap": {"unit": "claim", "paired": True, "B": B, "seed": SEED,
                      "skipped_nan_replicates": skipped},
        "cell_means": {k: {"pooled": point[k], "ci95": ci[k],
                           "per_model": {m: per_model[m]["cell_means"][k]
                                         for m in PANEL}}
                       for k in KINDS},
        "E1_exclude_pre": {"pooled": point["E1"], "ci95": ci["E1"]},
        "E2_exclude_post": {"pooled": point["E2"], "ci95": ci["E2"]},
        "E3_admit_pre": {"pooled": point["E3"], "ci95": ci["E3"]},
        "E4_admit_post": {"pooled": point["E4"], "ci95": ci["E4"]},
        "E1_minus_E2": {"pooled": point["E1_minus_E2"],
                        "ci95": ci["E1_minus_E2"],
                        "per_model": {m: per_model[m]["E1_minus_E2"]
                                      for m in PANEL}},
        "E1_over_E3": {"pooled": point["E1_over_E3"],
                       "ci95": ci["E1_over_E3"],
                       "per_model": {m: per_model[m]["E1_over_E3"]
                                     for m in PANEL}},
        "E2_over_E4": {"pooled": point["E2_over_E4"],
                       "ci95": ci["E2_over_E4"],
                       "per_model": {m: per_model[m]["E2_over_E4"]
                                     for m in PANEL}},
        "consistency_n_of_6": consistency,
        "per_model": {m: {k: per_model[m][k] for k in
                          ("E1", "E2", "E3", "E4", "E1_minus_E2",
                           "E1_over_E3", "E2_over_E4")}
                      for m in PANEL},
        "registered_expectations": {
            "E1_minus_E2": "> 0 (prospective leaks >> retrospective)",
            "E1_over_E3": "> 0 (prospective leak fraction > 0)",
            "E2_over_E4": "close to 0 (retrospective ~= removal); no "
                          "registered sign, so consistency is reported as "
                          "E2/E4 < E1/E3 (registered quantities only)",
        },
    }
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=1, sort_keys=True)
        fh.write("\n")

    # --- markdown -----------------------------------------------------------
    def row(label, key, expect):
        v, (lo, hi) = point[key], ci[key]
        return (f"| {label} | {v:+.2f} | [{lo:+.2f}, {hi:+.2f}] | {expect} |")

    L = ["# G24A Confirmation A — RQ1/F1 replication (v1, 2026-09-26)", ""]
    n_rows = len(y)
    L.append("Registration §13.5 estimands on 500 fresh FEVER/SciFact items "
             "x 5 cells x 6 models (incl. the frozen Qwen3-32B) = "
             f"{n_rows:,} rows; effects sign-normalized by "
             "critical_direction (+1 increase / -1 decrease). "
             "**Reporting, NOT gates**: paired percentile bootstrap 95% "
             "CIs over claims (B = 10,000, seed "
             f"`{SEED}`), per-model consistency n/6, no p-values, no "
             "thresholds, no selection — every item and model is included. "
             "Integrity: `check_g24a_confa_raws.py --require6` green "
             f"({n_rows} rows).")
    L += ["", "## 1. All five cell means (pooled, 0..100)", "",
          "| cell | pooled | 95% CI | per-model (6) |", "|---|---:|---:|---|"]
    for k in KINDS:
        v, (lo, hi) = point[k], ci[k]
        pm = ", ".join(f"{per_model[m]['cell_means'][k]:.1f}" for m in PANEL)
        L.append(f"| {k} | {v:.2f} | [{lo:.2f}, {hi:.2f}] | {pm} |")
    L += ["", "## 2. Primary estimands (signed by direction)", "",
          "| estimand | pooled | 95% CI | registered expectation |",
          "|---|---:|---:|---|"]
    L.append(row("E1 signed(ExcludePre − Base)", "E1",
                 "prospective leakage > 0"))
    L.append(row("E2 signed(ExcludePost − Base)", "E2",
                 "retrospective leakage, expected small vs E1"))
    L.append(row("E3 signed(AdmitPre − Base)", "E3",
                 "timing-matched admitted baseline"))
    L.append(row("E4 signed(AdmitPost − Base)", "E4",
                 "timing-matched admitted baseline"))
    L.append(row("E1 − E2", "E1_minus_E2", "> 0 (E1 ≫ E2)"))
    L.append(row("E1 / E3", "E1_over_E3", "> 0 (substantially > 0)"))
    L.append(row("E2 / E4", "E2_over_E4", "close to 0 (no registered sign)"))
    L += ["", "## 3. Per-model consistency (n/6)", ""]
    for k, label in (("E1_minus_E2_gt_0", "E1 − E2 > 0"),
                     ("E1_over_E3_gt_0", "E1 / E3 > 0"),
                     ("E2_over_E4_lt_E1_over_E3",
                      "E2 / E4 < E1 / E3 (the ≈0 estimand's sign-free "
                      "consistency: registered quantities only)")):
        L.append(f"- {label}: **{consistency[k]} / 6**")
    L += ["", "Per-model values:", "",
          "| model | E1 | E2 | E3 | E4 | E1−E2 | E1/E3 | E2/E4 |",
          "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for m in PANEL:
        e = per_model[m]
        L.append(f"| {m} | {e['E1']:+.2f} | {e['E2']:+.2f} | "
                 f"{e['E3']:+.2f} | {e['E4']:+.2f} | {e['E1_minus_E2']:+.2f} | "
                 f"{e['E1_over_E3']:+.3f} | {e['E2_over_E4']:+.3f} |")
    L += ["", "## 4. Reading rules (registered)", ""]
    L.append("- Everything above is reported as-is whatever the outcome "
             "(§13.5 interpretation rule); CIs quantify claim-sampling "
             "uncertainty, n/6 shows whether a pattern spans the panel "
             "rather than resting on one model.")
    L.append("- Leak fractions E1/E3 and E2/E4 divide pooled signed means; "
             "the bootstrap recomputes the ratio inside each resample "
             f"(NaN-denominator replicates skipped: {skipped}/{B}).")
    L.append("- After ConfA + ConfB are reported: experiments stop (§13.1).")
    L.append("")
    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))

    print(f"wrote {OUT_MD}, {OUT_JSON}, {OUT_CSV}")
    for k in ("E1", "E2", "E3", "E4", "E1_minus_E2", "E1_over_E3",
              "E2_over_E4"):
        lo, hi = ci[k]
        print(f"  {k:12s} {point[k]:+8.3f}  CI [{lo:+.3f}, {hi:+.3f}]")
    print("  consistency n/6:", consistency)
    return 0


if __name__ == "__main__":
    sys.exit(main())
