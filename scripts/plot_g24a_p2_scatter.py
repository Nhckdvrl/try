#!/usr/bin/env python3
"""G24A P2 — user-requested descriptive scatter figures (no gates, no filtering).

Post-analysis diagnostics requested after the frozen §9 readout
(`g24a_p2_analysis_v1.md`); they carry NO decision role: every (model, claim)
cell is plotted, nothing is selected on A, no thresholds are applied.

Fig 1: per-claim (R_CF,+ , R_CF,-) scatter — ideal deletion = origin (0,0).
       Primary points: 1,000 (model, claim) cells coloured by model (shows
       model-specific scatter). Overlay: 200 claim means (average over the
       5 models) as black open circles — shows whether the pattern is
       claim-stable or model noise.
Fig 2: leverage-vs-residual, two panels:
       (a) A+  vs R_CF,+   (b) A-  vs R_CF,-   — continuous relation only.

Estimands are exactly the frozen §9 definitions (e = +1 support / -1 refute):
    Y0      = plus-arm base value for (model, claim)   [shared across arms]
    A+      = Y_plus,admit  - Y0
    A-      = Y0 - Y_minus,admit
    R_CF,+  = Y_plus,cf     - Y0
    R_CF,-  = Y0 - Y_minus,cf
Sign reading: aligned R < 0 = over-correction past Base; R > 0 = residual
(the evidence still moves the judgment in its own direction).

Usage:  python scripts/plot_g24a_p2_scatter.py
Input:  results/g24a/g24a_p2_analysis_v1_cells.csv   (frozen, read-only)
Output: results/g24a/g24a_p2_fig1_rf_scatter.png
        results/g24a/g24a_p2_fig2_a_vs_r.png
"""
from __future__ import annotations

import csv
import statistics
from collections import defaultdict

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

CSV = "results/g24a/g24a_p2_analysis_v1_cells.csv"
OUT1 = "results/g24a/g24a_p2_fig1_rf_scatter.png"
OUT2 = "results/g24a/g24a_p2_fig2_a_vs_r.png"

CF = "counterfactual_delete_post"
ADMIT = "admit_post"
MODELS = [
    "mistral-small-24b",
    "llama31-8b",
    "gemma3-12b",
    "qwen3-8b",
    "qwen35-9b",
]
COLORS = {
    "mistral-small-24b": "#1f77b4",
    "llama31-8b": "#d62728",
    "gemma3-12b": "#2ca02c",
    "qwen3-8b": "#9467bd",
    "qwen35-9b": "#ff7f0e",
}


def load(path):
    cells = defaultdict(dict)  # (model, p2_id) -> {(arm, kind): value}
    with open(path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            key = (row["model"], row["p2_id"])
            cells[key][(row["arm"], row["kind"])] = float(row["value"])
    return cells


def quantiles(xs, qs=(0.10, 0.25, 0.50, 0.75, 0.90)):
    xs = sorted(xs)
    out = []
    for q in qs:
        i = q * (len(xs) - 1)
        lo, hi = int(i), min(int(i) + 1, len(xs) - 1)
        out.append(xs[lo] + (xs[hi] - xs[lo]) * (i - lo))
    return out


def main():
    cells = load(CSV)

    rows = []  # (model, claim, A+, A-, R+, R-)
    for (model, claim), v in sorted(cells.items()):
        y0 = v[("plus", "base")]
        a_plus = v[("plus", ADMIT)] - y0
        a_minus = y0 - v[("minus", ADMIT)]
        r_plus = v[("plus", CF)] - y0
        r_minus = y0 - v[("minus", CF)]
        rows.append((model, claim, a_plus, a_minus, r_plus, r_minus))

    assert len(rows) == 1000, f"expected 1000 (model, claim) cells, got {len(rows)}"

    # cross-check against the frozen §9 readout (pooled means)
    a_p = [r[2] for r in rows]
    a_m = [r[3] for r in rows]
    r_p = [r[4] for r in rows]
    r_m = [r[5] for r in rows]
    mp, mm = statistics.fmean(r_p), statistics.fmean(r_m)
    ap, am = statistics.fmean(a_p), statistics.fmean(a_m)
    print(f"pooled A+ = {ap:.2f} (expect 39.10), A- = {am:.2f} (expect 17.23)")
    print(f"pooled R_CF,+ = {mp:.2f} (expect 0.97), R_CF,- = {mm:.2f} (expect 11.04)")
    for got, want in ((ap, 39.10), (am, 17.23), (mp, 0.97), (mm, 11.04)):
        assert abs(got - want) < 0.02, (got, want)

    # claim means (average over models) — 200 points
    by_claim = defaultdict(list)
    for model, claim, _, _, rp, rm in rows:
        by_claim[claim].append((rp, rm))
    claim_pts = [
        (
            statistics.fmean(p[0] for p in pts),
            statistics.fmean(p[1] for p in pts),
        )
        for _, pts in sorted(by_claim.items())
    ]
    assert len(claim_pts) == 200

    # ---- Fig 1: (R_CF,+, R_CF,-) -----------------------------------------
    fig, ax = plt.subplots(figsize=(7.2, 6.4))
    for model in MODELS:
        xs = [r[4] for r in rows if r[0] == model]
        ys = [r[5] for r in rows if r[0] == model]
        ax.scatter(xs, ys, s=14, alpha=0.55, color=COLORS[model], label=model,
                   linewidths=0)
    ax.scatter([p[0] for p in claim_pts], [p[1] for p in claim_pts], s=26,
               facecolors="none", edgecolors="black", linewidths=0.7,
               label="claim mean (5 models)")
    ax.axhline(0, color="grey", lw=0.8)
    ax.axvline(0, color="grey", lw=0.8)
    ax.scatter([0], [0], marker="*", s=220, color="black", zorder=5,
               label="ideal deletion (0, 0)")
    ax.scatter([mp], [mm], marker="X", s=140, color="#444444", zorder=5,
               label=f"pooled mean ({mp:.1f}, {mm:.1f})")
    ax.set_xlabel(r"$R_{CF,+}$  (support arm: $Y_{CF}-Y_0$)")
    ax.set_ylabel(r"$R_{CF,-}$  (refute arm: $Y_0-Y_{CF}$)")
    ax.set_title("P2 Fig 1 — per-claim CF residual, both polarities (shared $Y_0$)\n"
                 "1,000 (model, claim) cells, all shown, no filtering")
    ax.legend(fontsize=8, loc="upper left")
    ax.set_aspect("equal", adjustable="datalim")
    fig.tight_layout()
    fig.savefig(OUT1, dpi=160)
    plt.close(fig)
    print(f"wrote {OUT1}")

    # ---- Fig 2: A vs R_CF, two panels ------------------------------------
    fig, axes = plt.subplots(1, 2, figsize=(11.6, 5.2), sharey=False)
    panels = [
        (axes[0], a_p, r_p, r"A+", r"R_{CF,+}",
         "support arm: leverage $A_+$ vs residual $R_{CF,+}$"),
        (axes[1], a_m, r_m, r"A-", r"R_{CF,-}",
         "refute arm: leverage $A_-$ vs residual $R_{CF,-}$"),
    ]
    for ax, xs, ys, xl, yl, title in panels:
        for model in MODELS:
            idx = [i for i, r in enumerate(rows) if r[0] == model]
            ax.scatter([xs[i] for i in idx], [ys[i] for i in idx], s=13,
                       alpha=0.5, color=COLORS[model], label=model,
                       linewidths=0)
        ax.axhline(0, color="grey", lw=0.8)
        ax.axvline(0, color="grey", lw=0.8)
        ax.set_xlabel(f"{xl}  (aligned leverage)")
        ax.set_ylabel(f"{yl}  (aligned residual)")
        ax.set_title(title, fontsize=10)
    axes[0].legend(fontsize=7, loc="lower right")
    fig.suptitle("P2 Fig 2 — leverage vs CF residual (continuous, no A filtering, "
                 "no gates)\n1,000 (model, claim) cells per panel, all shown",
                 fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.90))
    fig.savefig(OUT2, dpi=160)
    plt.close(fig)
    print(f"wrote {OUT2}")

    # ---- numbers for the companion note ----------------------------------
    print("\nA+ quantiles [p10,p25,p50,p75,p90]:",
          [f"{q:.1f}" for q in quantiles(a_p)])
    print("A- quantiles [p10,p25,p50,p75,p90]:",
          [f"{q:.1f}" for q in quantiles(a_m)])
    print("R_CF,+ quantiles:", [f"{q:.1f}" for q in quantiles(r_p)])
    print("R_CF,- quantiles:", [f"{q:.1f}" for q in quantiles(r_m)])
    print("\nper-model means (A+, A-, R+, R-, dR = R+ - R-):")
    for model in MODELS:
        sub = [r for r in rows if r[0] == model]
        ap_m = statistics.fmean(r[2] for r in sub)
        am_m = statistics.fmean(r[3] for r in sub)
        rp_m = statistics.fmean(r[4] for r in sub)
        rm_m = statistics.fmean(r[5] for r in sub)
        print(f"  {model:18s} {ap_m:6.2f} {am_m:6.2f} {rp_m:7.2f} {rm_m:7.2f}"
              f" {rp_m - rm_m:7.2f}")
    print("\nclaims with both |R+|<=5 and |R-|<=5 (near-perfect restoration):",
          sum(1 for p in claim_pts if abs(p[0]) <= 5 and abs(p[1]) <= 5),
          "/ 200")
    print("claims with |claim-mean dR| <= 5:",
          sum(1 for p in claim_pts if abs(p[0] - p[1]) <= 5), "/ 200")

    # structure of Fig 1: are the two arms' CF outcomes coupled per claim?
    r_cells = statistics.correlation(r_p, r_m)
    r_claims = statistics.correlation(
        [p[0] for p in claim_pts], [p[1] for p in claim_pts])
    print(f"\ncorr(R_CF,+, R_CF,-): cells = {r_cells:.3f}, "
          f"claim means = {r_claims:.3f}")
    sep_admit = statistics.fmean(a_p[i] + a_m[i] for i in range(len(rows)))
    sep_cf = statistics.fmean(r_p[i] + r_m[i] for i in range(len(rows)))
    print(f"arm separation (Y+ - Y-) at admit = {sep_admit:.2f}, "
          f"at CF = {sep_cf:.2f} ({100 * (1 - sep_cf / sep_admit):.0f}% erased)")
    print(f"shared drift (Y_CF - Y0, both arms avg) = "
          f"{statistics.fmean((r_p[i] - r_m[i]) / 2 for i in range(len(rows))):.2f}")
    for lbl, aa, rr in (("A+", a_p, r_p), ("A-", a_m, r_m)):
        n0 = sum(1 for x in aa if abs(x) <= 1)
        n_big = sum(1 for x, y in zip(aa, rr) if abs(x) <= 1 and abs(y) > 20)
        print(f"{lbl} cells with |A|<=1: {n0}/1000; "
              f"of those |R_CF|>20: {n_big}")


if __name__ == "__main__":
    main()
