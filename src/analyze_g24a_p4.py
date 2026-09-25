#!/usr/bin/env python3
"""G24A Pilot P4 — irrelevant-visible evidence control readout (registration §12).

Frozen comparisons (user 2026-09-26; interpretation branches, NOT gates):

  A1  Y_irrelevant_visible - Y_withheld_only      (same claims; P3 raws)
  A2  Y_irrelevant_visible - Y_base               (P3 base = P2 base re-run)
  B1  Y_irrelevant_cf - Y_withheld_cf             (frame-only anchor)
  B2  Y_irrelevant_cf vs M_CF^actual              (relevant-evidence anchor;
      claim-level, from the committed P2 cells)
  + position: where IrrelCF sits on the WithheldCF -> M_CF^actual segment
      (span fraction), and the trajectory / dispersion tables.

Descriptive only: no gates, no claim selection (all 200), no p-values, no
bootstrap, nothing filtered.  Inputs: the five checked P4 raws
(check_g24a_p4_raws.py --require5 must be green first), the five committed
P3 raws, the committed g24a_p2_analysis_v1_cells.csv, and the committed
g24a_p3_analysis_v1.json (temp-0 noise floor reference).

Outputs: results/g24a/g24a_p4_analysis_v1.md, .json, .csv
Usage: python src/analyze_g24a_p4.py
"""
from __future__ import annotations

import csv
import json
import statistics
from collections import defaultdict

RAW4 = "results/raw/{tag}_g24a_p4.jsonl"
RAW3 = "results/raw/{tag}_g24a_p3.jsonl"
P2_CELLS = "results/g24a/g24a_p2_analysis_v1_cells.csv"
P3_JSON = "results/g24a/g24a_p3_analysis_v1.json"
ITEMS = "data/items/g24a_p4_v1.jsonl"
ITEMS3 = "data/items/g24a_p3_v1.jsonl"
OUT_MD = "results/g24a/g24a_p4_analysis_v1.md"
OUT_JSON = "results/g24a/g24a_p4_analysis_v1.json"
OUT_CSV = "results/g24a/g24a_p4_analysis_v1_cells.csv"

PANEL = ["mistral-small-24b", "llama31-8b", "qwen3-8b", "qwen35-9b",
         "gemma3-12b"]
COND4 = ["irrelevant_visible", "irrelevant_cf"]
LABEL4 = {"irrelevant_visible": "IrrelVisible", "irrelevant_cf": "IrrelCF"}
# P3 anchor cells reused read-only
COND3 = ["base", "prior_only", "withheld_only", "withheld_cf"]
LABEL3 = {"base": "Base", "prior_only": "PriorOnly",
          "withheld_only": "WithheldOnly", "withheld_cf": "WithheldCF"}


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
    # --- claim keys + P4 raws ---------------------------------------------
    item2claim = {}
    for path in (ITEMS, ITEMS3):           # p4 cells + p3 anchor cells
        for line in open(path, encoding="utf-8"):
            d = json.loads(line)
            item2claim[d["item_id"]] = d["meta"]["p2_id"]
    claims = sorted(set(item2claim.values()))
    assert len(claims) == 200, len(claims)

    y4 = {}  # (model, claim, cond) -> value
    n4 = 0
    for tag in PANEL:
        for line in open(RAW4.format(tag=tag), encoding="utf-8"):
            r = json.loads(line)
            n4 += 1
            key = (tag, item2claim[r["item_id"]], r["kind_name"])
            assert key not in y4, key
            assert r["value"] is not None, key
            y4[key] = float(r["value"])
    assert n4 == 2000 and len(y4) == 2000, n4

    # --- P3 anchor raws (same claim keys) ---------------------------------
    y3 = {}
    n3 = 0
    for tag in PANEL:
        for line in open(RAW3.format(tag=tag), encoding="utf-8"):
            r = json.loads(line)
            n3 += 1
            if r["kind_name"] in COND3:
                key = (tag, item2claim[r["item_id"]], r["kind_name"])
                assert key not in y3, key
                y3[key] = float(r["value"])
    assert n3 == 5000, n3
    for tag in PANEL:
        for c in claims:
            for k in COND3:
                assert (tag, c, k) in y3, (tag, c, k)
            for k in COND4:
                assert (tag, c, k) in y4, (tag, c, k)

    # --- P2 committed cells: M_CF^actual, Y0 ------------------------------
    p2 = defaultdict(dict)
    for r in csv.DictReader(open(P2_CELLS, newline="", encoding="utf-8")):
        p2[(r["model"], r["p2_id"])][(r["arm"], r["kind"])] = float(r["value"])
    assert len(p2) == 1000

    def p2v(claim, arm, kind, model=None):
        if model is not None:
            return p2[(model, claim)][(arm, kind)]
        return statistics.fmean(p2[(m, claim)][(arm, kind)] for m in PANEL)

    mcf = {c: (p2v(c, "plus", "counterfactual_delete_post") +
               p2v(c, "minus", "counterfactual_delete_post")) / 2
           for c in claims}
    y0 = {c: p2v(c, "plus", "base") for c in claims}
    assert abs(statistics.fmean(y0.values()) - 50.24) < 0.01
    assert abs(statistics.fmean(mcf.values()) - 45.20) < 0.02

    # --- committed P3 noise floor (reference only) -------------------------
    p3json = json.load(open(P3_JSON, encoding="utf-8"))
    noise = p3json["base_rerun_vs_p2_base"]

    # --- trajectory + anchors ---------------------------------------------
    def m3(c, k):
        return statistics.fmean(y3[(m, c, k)] for m in PANEL)

    def m4(c, k):
        return statistics.fmean(y4[(m, c, k)] for m in PANEL)

    cells = ["base", "withheld_only", "irrelevant_visible",
             "withheld_cf", "irrelevant_cf"]
    labels = {"base": "Base", "withheld_only": "WithheldOnly",
              "irrelevant_visible": "IrrelVisible", "withheld_cf": "WithheldCF",
              "irrelevant_cf": "IrrelCF"}
    traj = {}
    for k in cells:
        if k in COND3:
            traj[k] = statistics.fmean(y3[(m, c, k)]
                                       for m in PANEL for c in claims)
        else:
            traj[k] = statistics.fmean(y4[(m, c, k)]
                                       for m in PANEL for c in claims)
    traj["m_cf_actual"] = statistics.fmean(mcf.values())
    traj_model = {}
    for m in PANEL:
        for k in cells:
            if k in COND3:
                traj_model[(m, k)] = statistics.fmean(y3[(m, c, k)]
                                                      for c in claims)
            else:
                traj_model[(m, k)] = statistics.fmean(y4[(m, c, k)]
                                                      for c in claims)
        traj_model[(m, "m_cf_actual")] = statistics.fmean(
            p2v(c, "plus", "counterfactual_delete_post", m) +
            p2v(c, "minus", "counterfactual_delete_post", m) for c in claims) / 2

    def disp4(k):
        return statistics.fmean(abs(y4[(m, c, k)] - 50)
                                for m in PANEL for c in claims)

    def disp3(k):
        return statistics.fmean(abs(y3[(m, c, k)] - 50)
                                for m in PANEL for c in claims)

    # --- A1: IrrelVisible - WithheldOnly (paired, cross-run) ---------------
    def paired(cond_new, old_is_p4: bool, cond_old):
        def get(m, c, old):
            return (y4 if old_is_p4 else y3)[(m, c, old)]
        diffs = [y4[(m, c, cond_new)] - get(m, c, cond_old)
                 for m in PANEL for c in claims]
        claim_diff = [statistics.fmean(
            y4[(m, c, cond_new)] - get(m, c, cond_old) for m in PANEL)
            for c in claims]
        per_model = {m: statistics.fmean(
            y4[(m, c, cond_new)] - get(m, c, cond_old) for c in claims)
            for m in PANEL}
        corr = statistics.correlation(
            [statistics.fmean(y4[(m, c, cond_new)] for m in PANEL)
             for c in claims],
            [statistics.fmean(get(m, c, cond_old) for m in PANEL)
             for c in claims])
        return {
            "mean_diff": statistics.fmean(diffs),
            "mean_abs_diff": statistics.fmean(abs(v) for v in diffs),
            "q_claim_mean_diff": quantiles(claim_diff),
            "per_model_mean_diff": per_model,
            "corr_claim": corr,
        }

    a1 = paired("irrelevant_visible", False, "withheld_only")
    a2 = paired("irrelevant_visible", False, "base")
    b1 = paired("irrelevant_cf", False, "withheld_cf")

    # --- B2: IrrelCF vs M_CF^actual ---------------------------------------
    got = {c: m4(c, "irrelevant_cf") for c in claims}
    x, yy = [mcf[c] for c in claims], [got[c] for c in claims]
    a, b = ols(x, yy)
    b2 = {
        "mean_actual_center": statistics.fmean(x),
        "mean_irrel_cf": statistics.fmean(yy),
        "mean_diff": statistics.fmean(got[c] - mcf[c] for c in claims),
        "mean_abs_diff": statistics.fmean(abs(got[c] - mcf[c]) for c in claims),
        "q_claim_diff": quantiles([got[c] - mcf[c] for c in claims]),
        "corr": statistics.correlation(x, yy),
        "ols_intercept": a,
        "ols_slope": b,
        "mean_abs_actual_minus_50": statistics.fmean(abs(v - 50) for v in x),
        "mean_abs_irrel_minus_50": statistics.fmean(abs(v - 50) for v in yy),
        "per_model": {},
    }
    for m in PANEL:
        g = statistics.fmean(y4[(m, c, "irrelevant_cf")] for c in claims)
        w = statistics.fmean(
            (p2v(c, "plus", "counterfactual_delete_post", m) +
             p2v(c, "minus", "counterfactual_delete_post", m)) / 2
            for c in claims)
        b2["per_model"][m] = (w, g, g - w)

    # --- position on the WithheldCF -> M_CF^actual segment -----------------
    wh = traj["withheld_cf"]
    ic = traj["irrelevant_cf"]
    mc = traj["m_cf_actual"]
    span = (ic - wh) / (mc - wh)

    # --- cells csv ---------------------------------------------------------
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["model", "p4_claim", "cond", "value"])
        for (m, c, k), v in sorted(y4.items()):
            w.writerow([m, c, k, v])

    payload = {
        "spec": "registration §12 (wording + material rule frozen pre-run, "
                "user 2026-09-26)",
        "n_rows": n4,
        "n_claims": len(claims),
        "trajectory": traj,
        "trajectory_per_model": {f"{m}|{k}": traj_model[(m, k)]
                                 for m in PANEL for k in cells +
                                 ["m_cf_actual"]},
        "A1_irrel_visible_vs_withheld_only": a1,
        "A2_irrel_visible_vs_base": a2,
        "B1_irrel_cf_vs_withheld_cf": b1,
        "B2_irrel_cf_vs_M_CF_actual": b2,
        "position_span_withheldcf_to_actual": span,
        "dispersion_mean_abs_y_minus_50": {
            "Base": disp3("base"), "WithheldOnly": disp3("withheld_only"),
            "IrrelVisible": disp4("irrelevant_visible"),
            "WithheldCF": disp3("withheld_cf"),
            "IrrelCF": disp4("irrelevant_cf"),
            "M_CF_actual": b2["mean_abs_actual_minus_50"],
        },
        "noise_floor_reference": {
            "mean_abs_diff": noise["mean_abs_diff"], "corr": noise["corr"],
            "source": "committed g24a_p3_analysis_v1.json (base re-run vs "
                      "P2 base)"},
    }
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=1, sort_keys=True)
        fh.write("\n")

    # ---- markdown ---------------------------------------------------------
    L = []
    L.append("# G24A Pilot P4 — irrelevant-visible evidence control (v1, 2026-09-26)")
    L.append("")
    L.append("Frozen comparisons per registration §12 (wording + material "
             "rule frozen pre-run, user 2026-09-26): A1 IrrelVisible vs "
             "WithheldOnly, A2 IrrelVisible vs Base, B1 IrrelCF vs "
             "WithheldCF, B2 IrrelCF vs M_CF^actual, and the position on "
             "the WithheldCF → M_CF^actual segment. Descriptive only — "
             "**no gates, no claim selection (all 200), no p-values, "
             "nothing filtered**; the three §12 branches are read by hand "
             "and have no decision role. Integrity: "
             "`check_g24a_p4_raws.py --require5` green "
             f"({n4} rows = 200 claims × 2 cells × 5 models). "
             "Discovery-only lineage as before.")
    L.append("")
    L.append("## 1. Trajectory — mean Y (0..100), pooled over 5 models × 200 claims")
    L.append("")
    order = ["base", "withheld_only", "irrelevant_visible", "withheld_cf",
             "irrelevant_cf", "m_cf_actual"]
    L.append("| anchor | " + " | ".join(
        labels.get(k, "M_CF^actual") for k in order) + " |")
    L.append("|---|" + "---:|" * len(order))
    L.append("| pooled | " + " | ".join(f"{traj[k]:.2f}" for k in order) + " |")
    for m in PANEL:
        L.append(f"| {m} | " + " | ".join(
            f"{traj_model[(m, k)]:.2f}" for k in order) + " |")
    L.append("")
    disp = payload["dispersion_mean_abs_y_minus_50"]
    L.append(f"Dispersion (pooled, mean|Y−50|): Base {disp['Base']:.2f} → "
             f"WithheldOnly {disp['WithheldOnly']:.2f} → IrrelVisible "
             f"{disp['IrrelVisible']:.2f}; WithheldCF {disp['WithheldCF']:.2f} "
             f"→ IrrelCF {disp['IrrelCF']:.2f} vs M_CF^actual "
             f"{disp['M_CF_actual']:.2f} (Y0 reference 22.55).")
    L.append("")
    L.append("## 2. Reference scales")
    L.append("")
    L.append(f"- temp-0 noise floor (committed): same-prompt re-run "
             f"mean|diff| = {noise['mean_abs_diff']:.2f}, corr "
             f"{noise['corr']:.3f} — every Δ below is read against this.")
    L.append(f"- anchors: WithheldCF (frame only) {wh:.2f}; IrrelCF "
             f"{ic:.2f}; M_CF^actual (relevant evidence) {mc:.2f}.")
    L.append("")
    L.append("## 3. A1 — IrrelVisible vs WithheldOnly (frame alone)")
    L.append("")
    L.append(f"- mean(Y_IrrelVisible − Y_WithheldOnly) = "
             f"**{a1['mean_diff']:+.2f}**; mean|Δ| = {a1['mean_abs_diff']:.2f}")
    L.append("- per-model mean Δ: " + ", ".join(
        f"{m} {a1['per_model_mean_diff'][m]:+.2f}" for m in PANEL))
    L.append(f"- claim-mean Δ quantiles [p10…p90]: "
             f"{a1['q_claim_mean_diff'][0]:+.1f} … "
             f"{a1['q_claim_mean_diff'][4]:+.1f} (median "
             f"{a1['q_claim_mean_diff'][2]:+.1f}); claim-level corr "
             f"{a1['corr_claim']:.3f}")
    L.append("")
    L.append("## 4. A2 — IrrelVisible vs Base")
    L.append("")
    L.append(f"- mean(Y_IrrelVisible − Y_Base) = **{a2['mean_diff']:+.2f}**; "
             f"mean|Δ| = {a2['mean_abs_diff']:.2f}")
    L.append("- per-model mean Δ: " + ", ".join(
        f"{m} {a2['per_model_mean_diff'][m]:+.2f}" for m in PANEL))
    L.append(f"- claim-mean Δ quantiles [p10…p90]: "
             f"{a2['q_claim_mean_diff'][0]:+.1f} … "
             f"{a2['q_claim_mean_diff'][4]:+.1f} (median "
             f"{a2['q_claim_mean_diff'][2]:+.1f}); claim-level corr "
             f"{a2['corr_claim']:.3f}")
    L.append("")
    L.append("## 5. B1 — IrrelCF vs WithheldCF (frame-only anchor)")
    L.append("")
    L.append(f"- mean(Y_IrrelCF − Y_WithheldCF) = **{b1['mean_diff']:+.2f}** "
             f"(paired over 5×200 cells); mean|Δ| = {b1['mean_abs_diff']:.2f}")
    L.append("- per-model mean Δ: " + ", ".join(
        f"{m} {b1['per_model_mean_diff'][m]:+.2f}" for m in PANEL))
    L.append(f"- claim-mean Δ quantiles [p10…p90]: "
             f"{b1['q_claim_mean_diff'][0]:+.1f} … "
             f"{b1['q_claim_mean_diff'][4]:+.1f} (median "
             f"{b1['q_claim_mean_diff'][2]:+.1f}); claim-level corr "
             f"{b1['corr_claim']:.3f}")
    L.append("")
    L.append("## 6. B2 — IrrelCF vs the actual-evidence center M_CF^actual")
    L.append("")
    L.append(f"- mean: IrrelCF {b2['mean_irrel_cf']:.2f} vs M_CF^actual "
             f"{b2['mean_actual_center']:.2f} → mean diff "
             f"**{b2['mean_diff']:+.2f}**; mean|diff| (claim-level) = "
             f"{b2['mean_abs_diff']:.2f}")
    L.append(f"- claim-level corr(IrrelCF, M_CF^actual) = {b2['corr']:.3f}; "
             f"OLS IrrelCF = {b2['ols_intercept']:.2f} + "
             f"{b2['ols_slope']:.3f}·M_CF^actual")
    L.append(f"- mean|Y−50|: IrrelCF {b2['mean_abs_irrel_minus_50']:.2f} vs "
             f"M_CF^actual {b2['mean_abs_actual_minus_50']:.2f} "
             f"(Y0 reference 22.55)")
    L.append("- claim-mean diff quantiles [p10…p90]: "
             f"{b2['q_claim_diff'][0]:+.1f} … {b2['q_claim_diff'][4]:+.1f} "
             f"(median {b2['q_claim_diff'][2]:+.1f})")
    L.append("- per-model (M_CF^actual, IrrelCF, Δ): " + "; ".join(
        f"{m} ({b2['per_model'][m][0]:.1f}, {b2['per_model'][m][1]:.1f}, "
        f"{b2['per_model'][m][2]:+.1f})" for m in PANEL))
    L.append("")
    L.append("## 7. Position on the WithheldCF → M_CF^actual segment")
    L.append("")
    L.append(f"- WithheldCF {wh:.2f} → IrrelCF {ic:.2f} → M_CF^actual "
             f"{mc:.2f}: span fraction = **{span:.3f}** (0 = identical to "
             "the frame-only anchor, 1 = identical to the relevant-evidence "
             "anchor; values outside [0,1] mean IrrelCF sits outside the "
             "segment).")
    L.append(f"- distance to each anchor: |IrrelCF − WithheldCF| = "
             f"{abs(ic - wh):.2f}, |IrrelCF − M_CF^actual| = "
             f"{abs(ic - mc):.2f} (noise floor "
             f"{noise['mean_abs_diff']:.2f}).")
    L.append("")
    L.append("## 8. §12 branches (read by hand — no decision role)")
    L.append("")
    L.append(f"- *IrrelCF ≈ WithheldCF* → only decision-relevant evidence "
             f"leaves the extra trace.  Observed Δ = {b1['mean_diff']:+.2f} "
             f"({abs(b1['mean_diff']) / noise['mean_abs_diff']:.1f}× the "
             f"{noise['mean_abs_diff']:.2f} floor).")
    L.append(f"- *IrrelCF ≈ M_CF^actual* → seeing any evidence-like content "
             f"and then retracting produces the distortion.  Observed Δ = "
             f"{b2['mean_diff']:+.2f} "
             f"({abs(b2['mean_diff']) / noise['mean_abs_diff']:.1f}× the "
             f"{noise['mean_abs_diff']:.2f} floor).")
    L.append(f"- *in between* → frame + visible-content + relevance "
             f"contribute in three layers (span {span:.3f} above).")
    L.append("")
    L.append("## 9. Caveats")
    L.append("")
    L.append("- All numbers are descriptive condition means; the §12 "
             "branches are interpretation aids, not gates.  A1/B1 are "
             "cross-run paired comparisons (P4 vs P3), each cell being its "
             "own run of the same claims — the noise floor in §2 calibrates "
             "run-to-run drift.")
    L.append("- The irrelevant text is mechanically screened "
             "(page-disjoint, no shared length≥5 token, seeded) but is "
             "naturally phrased evidence, not adversarially constructed; "
             "zero model involvement in selection (material rule §12, "
             "asserted per item by the verifier).")
    L.append("- Discovery-only claims; nothing here is confirmatory; no RQ "
             "declared or implied.  After P4: discovery stops (§12).")
    L.append("")
    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))

    print(f"wrote {OUT_MD}, {OUT_JSON}, {OUT_CSV}")
    print("trajectory: " + "  ".join(
        f"{labels.get(k, 'M_CF')}={traj[k]:.2f}" for k in order))
    print(f"A1 IrrelVisible-WithheldOnly: {a1['mean_diff']:+.2f}   "
          f"A2 IrrelVisible-Base: {a2['mean_diff']:+.2f}")
    print(f"B1 IrrelCF-WithheldCF: {b1['mean_diff']:+.2f}   "
          f"B2 IrrelCF-M_CF: {b2['mean_diff']:+.2f} "
          f"(corr {b2['corr']:.3f}); span={span:.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
