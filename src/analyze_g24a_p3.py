#!/usr/bin/env python3
"""G24A Pilot P3 — operator-only control readout (registration §11).

Frozen comparisons (user 2026-09-26; interpretation branches, NOT gates):

  C1  Y_prior_only  - Y_base
  C2  Y_withheld_only - Y_base
  C3  Y_withheld_cf vs M_CF^actual = (Y_CF,+ + Y_CF,-)/2 from the committed
      P2 cells (claim-level, 5-model means)
  plus (descriptive companion) Y_withheld_strong vs M_strong^actual, and the
  base re-run vs P2's base (temp-0 noise floor that calibrates C1/C2).

Descriptive only: no gates, no claim selection (all 200), no p-values, no
bootstrap, nothing filtered.  Inputs: the five checked raws
(check_g24a_p3_raws.py --require5 must be green first) + the committed
g24a_p2_analysis_v1_cells.csv.

Outputs: results/g24a/g24a_p3_analysis_v1.md, .json, .csv
Usage: python src/analyze_g24a_p3.py
"""
from __future__ import annotations

import csv
import json
import math
import statistics
from collections import defaultdict

RAW = "results/raw/{tag}_g24a_p3.jsonl"
P2_CELLS = "results/g24a/g24a_p2_analysis_v1_cells.csv"
ITEMS = "data/items/g24a_p3_v1.jsonl"
OUT_MD = "results/g24a/g24a_p3_analysis_v1.md"
OUT_JSON = "results/g24a/g24a_p3_analysis_v1.json"
OUT_CSV = "results/g24a/g24a_p3_analysis_v1_cells.csv"

PANEL = ["mistral-small-24b", "llama31-8b", "qwen3-8b", "qwen35-9b",
         "gemma3-12b"]
COND = ["base", "prior_only", "withheld_only", "withheld_strong",
        "withheld_cf"]
LABEL = {"base": "Base", "prior_only": "PriorOnly",
         "withheld_only": "WithheldOnly", "withheld_strong": "WithheldStrong",
         "withheld_cf": "WithheldCF"}


def quantiles(xs, qs=(0.10, 0.25, 0.50, 0.75, 0.90)):
    xs = sorted(xs)
    out = []
    for q in qs:
        i = q * (len(xs) - 1)
        lo, hi = int(i), min(int(i) + 1, len(xs) - 1)
        out.append(xs[lo] + (xs[hi] - xs[lo]) * (i - lo))
    return out


def ols(x, y):
    mx, my = statistics.fmean(x), statistics.fmean(y)
    b = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y)) / \
        sum((xi - mx) ** 2 for xi in x)
    return my - b * mx, b


def main() -> int:
    # --- P3 raws ----------------------------------------------------------
    item2claim = {}
    for line in open(ITEMS, encoding="utf-8"):
        d = json.loads(line)
        item2claim[d["item_id"]] = d["meta"]["p2_id"]
    claims = sorted(set(item2claim.values()))
    assert len(claims) == 200

    y = {}  # (model, claim, cond) -> value
    n_rows = 0
    for tag in PANEL:
        for line in open(RAW.format(tag=tag), encoding="utf-8"):
            r = json.loads(line)
            n_rows += 1
            claim = item2claim[r["item_id"]]
            key = (tag, claim, r["kind_name"])
            assert key not in y, key
            assert r["value"] is not None, key
            y[key] = float(r["value"])
    assert n_rows == 5000, n_rows
    assert len(y) == 5000
    for tag in PANEL:
        for c in claims:
            for k in COND:
                assert (tag, c, k) in y, (tag, c, k)

    # --- P2 committed cells: Y0, M_k (claim-level and per-model) ----------
    p2 = defaultdict(dict)  # (model, claim) -> {(arm, kind): v}
    for r in csv.DictReader(open(P2_CELLS, newline="", encoding="utf-8")):
        p2[(r["model"], r["p2_id"])][(r["arm"], r["kind"])] = float(r["value"])
    assert len(p2) == 1000

    def p2v(claim, arm, kind, model=None):
        if model is not None:
            return p2[(model, claim)][(arm, kind)]
        return statistics.fmean(p2[(m, claim)][(arm, kind)] for m in PANEL)

    def mk(claim, kind, model=None):
        return (p2v(claim, "plus", kind, model) +
                p2v(claim, "minus", kind, model)) / 2

    def y0(claim, model=None):
        return p2v(claim, "plus", "base", model)

    # cross-checks against the committed compression artifact
    mcf_claim = {c: mk(c, "counterfactual_delete_post") for c in claims}
    y0_claim = {c: y0(c) for c in claims}
    assert abs(statistics.fmean(y0_claim.values()) - 50.24) < 0.01

    # --- trajectory -------------------------------------------------------
    traj = {k: statistics.fmean(y[(m, c, k)] for m in PANEL for c in claims)
            for k in COND}
    traj_model = {(m, k): statistics.fmean(y[(m, c, k)] for c in claims)
                  for m in PANEL for k in COND}

    # --- base rerun vs P2 base (temp-0 noise floor) -----------------------
    rerun_claim = {c: statistics.fmean(y[(m, c, "base")] for m in PANEL)
                   for c in claims}
    d_base = [rerun_claim[c] - y0_claim[c] for c in claims]
    noise = {
        "mean_diff": statistics.fmean(d_base),
        "mean_abs_diff": statistics.fmean(abs(v) for v in d_base),
        "q": quantiles(d_base),
        "corr": statistics.correlation(
            [rerun_claim[c] for c in claims], [y0_claim[c] for c in claims]),
        "mean_abs_y_rerun_minus_50": statistics.fmean(
            abs(rerun_claim[c] - 50) for c in claims),
        "mean_abs_y0_minus_50": statistics.fmean(
            abs(y0_claim[c] - 50) for c in claims),
    }

    # --- C1 / C2: condition vs base (same run, paired per claim+model) ----
    def vs_base(cond):
        diffs = [y[(m, c, cond)] - y[(m, c, "base")]
                 for m in PANEL for c in claims]
        claim_diff = [statistics.fmean(
            y[(m, c, cond)] - y[(m, c, "base")] for m in PANEL)
            for c in claims]
        per_model = {m: statistics.fmean(
            y[(m, c, cond)] - y[(m, c, "base")] for c in claims)
            for m in PANEL}
        return {
            "mean_diff": statistics.fmean(diffs),
            "mean_abs_diff": statistics.fmean(abs(v) for v in diffs),
            "q_claim_mean_diff": quantiles(claim_diff),
            "per_model_mean_diff": per_model,
            "mean_abs_cond_minus_50": statistics.fmean(
                abs(y[(m, c, cond)] - 50) for m in PANEL for c in claims),
            "mean_abs_base_minus_50": statistics.fmean(
                abs(y[(m, c, "base")] - 50) for m in PANEL for c in claims),
            "corr_claim": statistics.correlation(
                [statistics.fmean(y[(m, c, cond)] for m in PANEL)
                 for c in claims],
                [statistics.fmean(y[(m, c, "base")] for m in PANEL)
                 for c in claims]),
        }

    c1 = vs_base("prior_only")
    c2 = vs_base("withheld_only")

    # --- C3: withheld_cf vs M_CF^actual ----------------------------------
    def vs_p2center(cond, kind):
        got = {c: statistics.fmean(y[(m, c, cond)] for m in PANEL)
               for c in claims}
        want = {c: mk(c, kind) for c in claims}
        diffs = [got[c] - want[c] for c in claims]
        x, yy = [want[c] for c in claims], [got[c] for c in claims]
        a, b = ols(x, yy)
        per_model = {}
        for m in PANEL:
            g = statistics.fmean(y[(m, c, cond)] for c in claims)
            w = statistics.fmean(mk(c, kind, m) for c in claims)
            per_model[m] = (w, g, g - w)
        return {
            "mean_actual_center": statistics.fmean(x),
            "mean_withheld": statistics.fmean(yy),
            "mean_diff": statistics.fmean(diffs),
            "mean_abs_diff": statistics.fmean(abs(v) for v in diffs),
            "q_claim_diff": quantiles(diffs),
            "corr": statistics.correlation(x, yy),
            "ols_intercept": a,
            "ols_slope": b,
            "mean_abs_actual_minus_50": statistics.fmean(abs(v - 50) for v in x),
            "mean_abs_withheld_minus_50": statistics.fmean(abs(v - 50) for v in yy),
            "per_model": per_model,
        }

    c3 = vs_p2center("withheld_cf", "counterfactual_delete_post")
    c3s = vs_p2center("withheld_strong", "strong_exclude_post")

    # --- write cells csv (long form, descriptive) -------------------------
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["model", "p3_claim", "cond", "value"])
        for (m, c, k), v in sorted(y.items()):
            w.writerow([m, c, k, v])

    payload = {
        "spec": "registration §11 (wording frozen pre-run, user 2026-09-26)",
        "n_rows": n_rows,
        "n_claims": len(claims),
        "trajectory": traj,
        "trajectory_per_model": {f"{m}|{k}": traj_model[(m, k)]
                                 for m in PANEL for k in COND},
        "base_rerun_vs_p2_base": noise,
        "C1_prior_only_vs_base": c1,
        "C2_withheld_only_vs_base": c2,
        "C3_withheld_cf_vs_M_CF_actual": c3,
        "withheld_strong_vs_M_strong_actual": c3s,
    }
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=1, sort_keys=True)
        fh.write("\n")

    # ---- markdown --------------------------------------------------------
    L = []
    L.append("# G24A Pilot P3 — operator-only control readout (v1, 2026-09-26)")
    L.append("")
    L.append("Frozen comparisons per registration §11 (wording frozen pre-run, "
             "user 2026-09-26): C1 prior_only vs base, C2 withheld_only vs "
             "base, C3 withheld_cf vs M_CF^actual. Descriptive only — **no "
             "gates, no claim selection (all 200), no p-values, nothing "
             "filtered**; interpretation branches have no decision role. "
             "Integrity: `check_g24a_p3_raws.py --require5` green "
             f"({n_rows} rows = 200 claims × 5 cells × 5 models). "
             "Discovery-only lineage as before.")
    L.append("")
    L.append("## 1. Trajectory — mean Y (0..100), pooled over 5 models × 200 claims")
    L.append("")
    L.append("| cell | " + " | ".join(LABEL[k] for k in COND) + " |")
    L.append("|---|" + "---:|" * len(COND))
    L.append("| pooled | " + " | ".join(f"{traj[k]:.2f}" for k in COND) + " |")
    for m in PANEL:
        L.append(f"| {m} | " + " | ".join(
            f"{traj_model[(m, k)]:.2f}" for k in COND) + " |")
    L.append("")
    L.append(f"Dispersion around the neutral midpoint (pooled, "
             f"mean|Y−50|): Base {c1['mean_abs_base_minus_50']:.2f} → "
             f"PriorOnly {c1['mean_abs_cond_minus_50']:.2f}, WithheldOnly "
             f"{c2['mean_abs_cond_minus_50']:.2f} (see §§3-4); for "
             f"reference P2's actual-evidence M_CF mean|M−50| = 12.57 "
             "(committed compression artifact).")
    L.append("")
    L.append("## 2. Base re-run vs P2 Base — temp-0 noise floor")
    L.append("")
    L.append(f"- claim-level corr(rerun, P2 base) = {noise['corr']:.3f}; "
             f"mean diff = {noise['mean_diff']:+.2f}; mean|diff| = "
             f"{noise['mean_abs_diff']:.2f} (p10..p90: "
             f"{noise['q'][0]:+.1f} … {noise['q'][4]:+.1f})")
    L.append(f"- mean|Y−50|: rerun {noise['mean_abs_y_rerun_minus_50']:.2f} "
             f"vs P2 {noise['mean_abs_y0_minus_50']:.2f}")
    L.append("- This is the scale against which C1/C2 must be read: two "
             "temp-0 runs of the *same* prompt differ by the mean|diff| "
             "above.")
    L.append("")
    L.append("## 3. C1 — PriorOnly vs Base")
    L.append("")
    L.append(f"- mean(Y_PriorOnly − Y_Base) = **{c1['mean_diff']:+.2f}** "
             f"(paired over 5×200 cells); mean|Δ| = {c1['mean_abs_diff']:.2f}")
    L.append("- per-model mean Δ: " + ", ".join(
        f"{m} {c1['per_model_mean_diff'][m]:+.2f}" for m in PANEL))
    L.append(f"- claim-mean Δ quantiles [p10…p90]: "
             f"{c1['q_claim_mean_diff'][0]:+.1f} … "
             f"{c1['q_claim_mean_diff'][4]:+.1f} (median "
             f"{c1['q_claim_mean_diff'][2]:+.1f})")
    L.append(f"- claim-level corr(PriorOnly, Base) = {c1['corr_claim']:.3f}")
    L.append("")
    L.append("## 4. C2 — WithheldOnly vs Base")
    L.append("")
    L.append(f"- mean(Y_WithheldOnly − Y_Base) = **{c2['mean_diff']:+.2f}**; "
             f"mean|Δ| = {c2['mean_abs_diff']:.2f}")
    L.append("- per-model mean Δ: " + ", ".join(
        f"{m} {c2['per_model_mean_diff'][m]:+.2f}" for m in PANEL))
    L.append(f"- claim-mean Δ quantiles [p10…p90]: "
             f"{c2['q_claim_mean_diff'][0]:+.1f} … "
             f"{c2['q_claim_mean_diff'][4]:+.1f} (median "
             f"{c2['q_claim_mean_diff'][2]:+.1f})")
    L.append(f"- claim-level corr(WithheldOnly, Base) = {c2['corr_claim']:.3f}")
    L.append("")
    L.append("## 5. C3 — WithheldCF vs the actual-evidence center M_CF^actual")
    L.append("")
    L.append(f"- mean: WithheldCF {c3['mean_withheld']:.2f} vs M_CF^actual "
             f"{c3['mean_actual_center']:.2f} → mean diff "
             f"**{c3['mean_diff']:+.2f}**; mean|diff| (claim-level) = "
             f"{c3['mean_abs_diff']:.2f}")
    L.append(f"- claim-level corr(WithheldCF, M_CF^actual) = {c3['corr']:.3f}; "
             f"OLS WithheldCF = {c3['ols_intercept']:.2f} + "
             f"{c3['ols_slope']:.3f}·M_CF^actual")
    L.append(f"- mean|Y−50|: WithheldCF {c3['mean_abs_withheld_minus_50']:.2f} "
             f"vs M_CF^actual {c3['mean_abs_actual_minus_50']:.2f} "
             f"(P2 Y0 reference: {noise['mean_abs_y0_minus_50']:.2f})")
    L.append("- claim-mean diff quantiles [p10…p90]: "
             f"{c3['q_claim_diff'][0]:+.1f} … {c3['q_claim_diff'][4]:+.1f} "
             f"(median {c3['q_claim_diff'][2]:+.1f})")
    L.append("- per-model (M_CF^actual, WithheldCF, Δ): " + "; ".join(
        f"{m} ({c3['per_model'][m][0]:.1f}, {c3['per_model'][m][1]:.1f}, "
        f"{c3['per_model'][m][2]:+.1f})" for m in PANEL))
    L.append("")
    L.append("Companion (descriptive): WithheldStrong vs M_strong^actual — "
             f"mean {c3s['mean_withheld']:.2f} vs {c3s['mean_actual_center']:.2f} "
             f"({c3s['mean_diff']:+.2f}), corr {c3s['corr']:.3f}, "
             f"mean|Y−50| {c3s['mean_abs_withheld_minus_50']:.2f} vs "
             f"{c3s['mean_abs_actual_minus_50']:.2f}.")
    L.append("")
    L.append("## 6. Caveats")
    L.append("")
    L.append("- All numbers are descriptive condition means; the §11 "
             "interpretation branches (operator-induced recalibration vs "
             "state-dependent trace vs non-equivalent base) are read by "
             "hand against §§2-5, not by any threshold.")
    L.append("- Discovery-only claims; nothing here is confirmatory; no RQ "
             "declared or implied.")
    L.append("- WithheldCF never shows evidence content (leakage-asserted "
             "2,000× pre-run); its Δ vs M_CF^actual is bounded below by "
             "the temp-0 floor in §2.")
    L.append("")
    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))

    print(f"wrote {OUT_MD}, {OUT_JSON}, {OUT_CSV}")
    print("trajectory: " + "  ".join(f"{LABEL[k]}={traj[k]:.2f}" for k in COND))
    print(f"base rerun vs P2 base: corr={noise['corr']:.3f} "
          f"mean|d|={noise['mean_abs_diff']:.2f}")
    print(f"C1 prior_only-base: {c1['mean_diff']:+.2f}   "
          f"C2 withheld_base: {c2['mean_diff']:+.2f}")
    print(f"C3 withheld_cf - M_CF: {c3['mean_diff']:+.2f} "
          f"(corr {c3['corr']:.3f})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
