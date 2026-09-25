#!/usr/bin/env python3
"""G24A P2 — claim-level center compression analysis M_k (discovery artifact).

Registered as a discovery artifact by the user ruling 2026-09-26 ("先把
M_k=(Y_{k,+}+Y_{k,-})/2 的 claim-level compression analysis 正式补进 discovery
artifact"), BEFORE the P3 operator-only control.

Definition (frozen):
    M_k = (Y_{k,+} + Y_{k,-}) / 2   — the center, across the two polarity
    arms, of the SAME claim under retraction operator k.

Computation: claim-level over the 200 P2 claims, each Y the mean over the 5
panel models, read from the committed frozen cells csv
(results/g24a/g24a_p2_analysis_v1_cells.csv).  Nothing is filtered, no gate,
no selection, no p-values — descriptive only.

Reported per operator k in {exclude_post, strong_exclude_post,
counterfactual_delete_post}:
    corr(M_k, Y0)               claim-dependence of the landing center
    OLS  M_k = a + b * Y0       landing regression (restoration would be
                                a = 0, b = 1)
    mean|M_k - 50|              dispersion around the neutral midpoint
    plus per-model corr(M_k, Y0) robustness row, and the per-claim
    compression fraction |M_k - 50| < |Y0 - 50|

Cross-checks against the user's quoted figures (asserted): corr(M_CF, Y0) =
0.701, M_CF = 25.84 + 0.385 * Y0, mean|Y0-50| = 22.55, mean|M_CF-50| = 12.57;
and against the frozen readout: pooled mean Y0 = 50.24.

Outputs:
    results/g24a/g24a_p2_compression_v1.md
    results/g24a/g24a_p2_compression_v1.json

Usage: python scripts/analyze_g24a_p2_compression.py
"""
from __future__ import annotations

import csv
import json
import statistics
from collections import defaultdict

CSV = "results/g24a/g24a_p2_analysis_v1_cells.csv"
OUT_MD = "results/g24a/g24a_p2_compression_v1.md"
OUT_JSON = "results/g24a/g24a_p2_compression_v1.json"

KINDS = ["exclude_post", "strong_exclude_post", "counterfactual_delete_post"]
KIND_LABEL = {"exclude_post": "Exclude",
              "strong_exclude_post": "StrongExclude",
              "counterfactual_delete_post": "CounterfactualDelete"}


def ols(x, y):
    mx, my = statistics.fmean(x), statistics.fmean(y)
    b = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y)) / \
        sum((xi - mx) ** 2 for xi in x)
    return my - b * mx, b


def main() -> int:
    cells = defaultdict(dict)  # (model, claim) -> {(arm, kind): y}
    for r in csv.DictReader(open(CSV, newline="", encoding="utf-8")):
        cells[(r["model"], r["p2_id"])][(r["arm"], r["kind"])] = float(r["value"])

    models = sorted({m for (m, _) in cells})
    claims = sorted({c for (_, c) in cells})
    assert len(models) == 5 and len(claims) == 200, (len(models), len(claims))

    def m5(claim, arm, kind):
        return statistics.fmean(cells[(m, claim)][(arm, kind)] for m in models)

    y0 = {c: m5(c, "plus", "base") for c in claims}
    mk = {k: {c: (m5(c, "plus", k) + m5(c, "minus", k)) / 2 for c in claims}
          for k in KINDS}

    # cross-check against the frozen readout
    pooled_y0 = statistics.fmean(y0.values())
    assert abs(pooled_y0 - 50.24) < 0.01, pooled_y0

    x = [y0[c] for c in claims]
    d0 = [abs(v - 50) for v in x]
    mean_abs_y0 = statistics.fmean(d0)
    assert abs(mean_abs_y0 - 22.55) < 0.01, mean_abs_y0

    rows = {}
    for k in KINDS:
        y = [mk[k][c] for c in claims]
        a, b = ols(x, y)
        corr = statistics.correlation(x, y)
        per_model_corr = {m: statistics.correlation(
            [y0[c] for c in claims],
            [statistics.fmean(cells[(m, c)][(arm, k)] for arm in ("plus", "minus"))
             for c in claims]) for m in models}
        frac = sum(1 for c in claims
                   if abs(mk[k][c] - 50) < abs(y0[c] - 50)) / len(claims)
        rows[k] = {
            "corr_M_Y0": corr,
            "ols_intercept": a,
            "ols_slope": b,
            "mean_abs_M_minus_50": statistics.fmean(abs(v - 50) for v in y),
            "mean_M": statistics.fmean(y),
            "per_model_corr": per_model_corr,
            "compressed_claim_fraction": frac,
        }

    cf = rows["counterfactual_delete_post"]
    assert abs(cf["corr_M_Y0"] - 0.701) < 0.001, cf["corr_M_Y0"]
    assert abs(cf["ols_intercept"] - 25.84) < 0.01, cf["ols_intercept"]
    assert abs(cf["ols_slope"] - 0.385) < 0.001, cf["ols_slope"]
    assert abs(cf["mean_abs_M_minus_50"] - 12.57) < 0.01, cf["mean_abs_M_minus_50"]

    payload = {
        "definition": "M_k = (Y_{k,+} + Y_{k,-})/2, claim-level, 5-model means",
        "input_csv": CSV,
        "n_claims": len(claims),
        "n_models": len(models),
        "mean_Y0": pooled_y0,
        "mean_abs_Y0_minus_50": mean_abs_y0,
        "operators": rows,
    }
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=1, sort_keys=True)
        fh.write("\n")

    # ---- markdown artifact ------------------------------------------------
    L = []
    L.append("# G24A P2 — claim-level center compression M_k (discovery artifact v1, 2026-09-26)")
    L.append("")
    L.append("Registered by user ruling 2026-09-26 (before P3). Descriptive only: no "
             "gate, no claim selection, no p-values, nothing filtered — all 200 "
             "discovery claims, all 5 panel models, read from the committed frozen "
             "cells csv (`g24a_p2_analysis_v1_cells.csv`). Discovery-only lineage "
             "per `g24a_p2_figures_v1.md` §0.")
    L.append("")
    L.append("## 0. Definition")
    L.append("")
    L.append("$$M_k = \\frac{Y_{k,+} + Y_{k,-}}{2}$$ — the center, across the two "
             "polarity arms, of the SAME claim after retraction operator $k$ "
             "(each $Y$ a 5-model mean; $Y_0$ the shared evidence-free Base).")
    L.append("")
    L.append("Reference points: restoration to the counterfactual would give "
             "$M_k = Y_0$ exactly (corr = 1, slope = 1, intercept = 0, "
             "$|M_k - 50| = |Y_0 - 50|$); a flat neutral attractor would give "
             "corr = 0 with $M_k = 50$.")
    L.append("")
    L.append("## 1. Numbers (claim-level, n = 200)")
    L.append("")
    L.append(f"Baseline: mean $Y_0$ = {pooled_y0:.2f}, mean $|Y_0 - 50|$ = "
             f"{mean_abs_y0:.2f}.")
    L.append("")
    L.append("| operator k | corr($M_k$, $Y_0$) | OLS $M_k$ = a + b·$Y_0$ | "
             "mean $|M_k - 50|$ | compressed claims $|M_k-50| < |Y_0-50|$ |")
    L.append("|---|---:|---:|---:|---:|")
    for k in KINDS:
        r = rows[k]
        L.append(f"| {KIND_LABEL[k]} | {r['corr_M_Y0']:.3f} | "
                 f"{r['ols_intercept']:.2f} + {r['ols_slope']:.3f}·$Y_0$ | "
                 f"{r['mean_abs_M_minus_50']:.2f} | "
                 f"{100 * r['compressed_claim_fraction']:.0f}% |")
    L.append("")
    L.append("Per-model corr($M_{CF}$, $Y_0$) (robustness row): "
             + ", ".join(f"{m} {rows['counterfactual_delete_post']['per_model_corr'][m]:.3f}"
                         for m in models) + ".")
    L.append("")
    L.append("## 2. Reading (descriptive)")
    L.append("")
    L.append("- **Claim-dependent**: corr($M_{CF}$, $Y_0$) = "
             f"{cf['corr_M_Y0']:.3f} — the landing center is NOT a flat 50; "
             "claims keep part of their prior ordering.")
    L.append("- **Strongly compressed**: slope "
             f"{cf['ols_slope']:.3f} (restoration = 1), mean $|Y_0-50|$ "
             f"{mean_abs_y0:.2f} → mean $|M_{{CF}}-50|$ "
             f"{cf['mean_abs_M_minus_50']:.2f} "
             f"({100 * (1 - cf['mean_abs_M_minus_50'] / mean_abs_y0):.0f}% "
             "contraction toward the midpoint), monotone in instruction "
             "strength (Exclude → StrongExclude → CounterfactualDelete).")
    L.append(f"- **Not restoration**: the attractor line has intercept "
             f"{cf['ols_intercept']:.2f} and slope {cf['ols_slope']:.3f}; "
             f"mean $M_{{CF}}$ = {cf['mean_M']:.2f} vs mean $Y_0$ = "
             f"{pooled_y0:.2f} (a small shared downward shift of "
             f"{cf['mean_M'] - pooled_y0:.2f} rides on top of the "
             "compression).")
    L.append("- Form: **claim-specific prior → strongly compressed prior** "
             "(\"retraction-induced confidence contraction\"), not "
             "counterfactual restoration.")
    L.append("")
    L.append("Converging context (already committed): polarity separation "
             "56.32 → 12.01 across arms at CF (79% of evidence-specific "
             "direction erased, `g24a_p2_figures_v1.md`); CF moves judgments "
             "> 20 points even where Admit did nothing (102/186 support, "
             "75/143 refute cells); §10 rationale reading found `still_uses_"
             "evidence` at only 4/106 under CF while numerical residual stays "
             "large, and `exclusion_implies_distrust` = 0/530 — the "
             "evidence's *content* is largely gone while the *act of being "
             "asked to retract* still moves the number.")
    L.append("")
    L.append("Motivation for the next step: P3 operator-only control "
             "(registration §11) — does the compressed attractor need actual "
             "evidence at all, or does the retraction / evidence-unavailable "
             "language frame induce the contraction by itself?")
    L.append("")
    L.append("## 3. Provenance")
    L.append("")
    L.append("- Script: `scripts/analyze_g24a_p2_compression.py` "
             "(asserts: 5 models × 200 claims, pooled mean $Y_0$ = 50.24, "
             "mean $|Y_0-50|$ = 22.55, and the quoted CF figures "
             "0.701 / 25.84 / 0.385 / 12.57).")
    L.append(f"- Machine-readable: `{OUT_JSON}`.")
    L.append("- No model was run for this artifact; inputs are the frozen P2 "
             "raws already checked by `check_g24a_p2_raws.py --require5`.")
    L.append("")
    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))

    print(f"wrote {OUT_MD} and {OUT_JSON}")
    print(f"mean|Y0-50| = {mean_abs_y0:.2f}")
    for k in KINDS:
        r = rows[k]
        print(f"  {KIND_LABEL[k]:20s} corr={r['corr_M_Y0']:.3f} "
              f"OLS={r['ols_intercept']:.2f}+{r['ols_slope']:.3f}*Y0 "
              f"mean|M-50|={r['mean_abs_M_minus_50']:.2f} "
              f"compressed={100 * r['compressed_claim_fraction']:.0f}% "
              f"mean M={r['mean_M']:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
