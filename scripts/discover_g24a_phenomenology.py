#!/usr/bin/env python3
"""G24A phenomenology map — DISCOVERY layer (three-layer process, layer 1).

No KILL gates anywhere: every stratum is reported, small or messy. The only
hard stops are integrity failures (missing files, duplicate rows). Outputs
are observations for hypothesis formation, NOT confirmatory claims.

Per item x model, with s = +1 (critical_direction == "increase") else -1:

    Y_admit  = (Y_admit_pre + Y_admit_post) / 2        (G0 canonical)
    E_i      = s * (Y_admit - Y_base)                   (evidence leverage,
                                                         = G0 signed_L)
    L_pre_i  = s * (Y_excl_pre - Y_base)                (prospective residual)
    L_post_i = s * (Y_excl_post - Y_base)               (retrospective residual)
    gain_pre  = L_pre / E,  gain_post = L_post / E      (undefined iff E == 0)

Sections: integrity; definition cross-check vs g24a_analysis_v1; distributions;
E-vs-L binned structure + rank correlations; region counts vs reference lines
L = 0 and L = E; pre/post correspondence; Y_base strata; floor/ceiling table;
rule-probe context; case-reading lists (high-leak / near-zero residual / flips
/ E<0). CSV of all 3,000 item-model rows for plotting; optional scatter PNGs.

Usage:
  /home/xiang/miniconda3/envs/fgvd/bin/python scripts/discover_g24a_phenomenology.py
"""
from __future__ import annotations

import argparse
import ast
import csv
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
import statistics as st

ITEMS = "data/items/g24a_v1.jsonl"
RUNS = [f"results/raw/{m}_g24a.jsonl" for m in
        ("llama31-8b", "qwen3-8b", "qwen35-9b", "gemma3-12b",
         "mistral-small-24b")]
MAIN_CELLS = ("base", "admit_pre", "admit_post", "exclude_pre",
              "exclude_post")
PROBE_CELLS = ("rule_probe_exclude_pre", "rule_probe_exclude_post",
               "rule_probe_admit_post")
OUT_PREFIX = "results/discovery/g24a_phenomenology_v1"
SELECTOR = "mistral-small-24b"
# published confirmatory numbers for the definition cross-check (informational
# only — reproducing them proves the E/L plumbing matches G0; nothing gates on
# them): results/g24a/g24a_analysis_v1.md pooled-4 block. Refreshed 2026-09-25
# from the full re-run output (commit e3e954d) after the 52 claim rewrites +
# 4 direction flips were applied and all raws regenerated.
PUBLISHED = {
    "alignment": 0.84, "n_usable": 2007, "median_absL": 32.7,
    "REI_pre": 0.541, "REI_post": -0.072, "frac_post_gt_pre": 0.32,
}
FLOOR, CEIL = 5.0, 95.0          # descriptive scale endpoints (0-100 readout)
E_BIN_WIDTH = 10.0               # fixed-width E bins, no thresholds implied
GAIN_BIN_WIDTH = 0.1


def quantiles(vals):
    s = sorted(vals)
    n = len(s)
    if not n:
        return None
    q = lambda f: s[min(n - 1, max(0, int(round(f * (n - 1)))))]
    return {"n": n, "mean": st.mean(s), "sd": st.pstdev(s) if n > 1 else 0.0,
            "min": s[0], "p5": q(0.05), "p10": q(0.10), "p25": q(0.25),
            "median": st.median(s),
            "p75": q(0.75), "p90": q(0.90), "p95": q(0.95), "max": s[-1]}


def _ranks(vals):
    order = sorted(range(len(vals)), key=lambda i: vals[i])
    ranks = [0.0] * len(vals)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and vals[order[j + 1]] == vals[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[order[k]] = avg
        i = j + 1
    return ranks


def spearman(xs, ys):
    """Rank correlation with average ranks for ties (no scipy dependency)."""
    if len(xs) < 3:
        return None
    rx, ry = _ranks(xs), _ranks(ys)
    mx, my = st.mean(rx), st.mean(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    dx = math.sqrt(sum((a - mx) ** 2 for a in rx))
    dy = math.sqrt(sum((b - my) ** 2 for b in ry))
    return None if dx == 0 or dy == 0 else num / (dx * dy)


def mean_or_none(vals):
    return st.mean(vals) if vals else None


def med_or_none(vals):
    return st.median(vals) if vals else None


# ---------------------------------------------------------------------------
# load
# ---------------------------------------------------------------------------
def load_items(path):
    items = {}
    for line in open(path, encoding="utf-8"):
        it = json.loads(line)
        meta = it.get("meta")
        if isinstance(meta, str):
            try:
                meta = ast.literal_eval(meta)
            except (ValueError, SyntaxError):
                meta = {"_raw": meta}
        it["_meta"] = meta or {}
        items[it["item_id"]] = it
    return items


def load_runs(paths, integrity):
    """model -> item_id -> kind -> row. Records integrity observations."""
    runs = {}
    for path in paths:
        model = Path(path).name.replace("_g24a.jsonl", "")
        per_item = defaultdict(dict)
        counts = Counter()
        n = 0
        for lineno, line in enumerate(open(path, encoding="utf-8"), 1):
            row = json.loads(line)
            n += 1
            counts[row["kind_name"]] += 1
            key = (row["item_id"], row["kind_name"])
            if row["kind_name"] in per_item[row["item_id"]]:
                integrity["duplicates"].append(f"{path}:{lineno}:{key}")
            per_item[row["item_id"]][row["kind_name"]] = row
        integrity["files"][model] = {
            "path": path, "rows": n, "kinds": dict(sorted(counts.items()))}
        runs[model] = per_item
    return runs


def build_rows(items, runs):
    """One record per (model, item): raw cells + E/L/gain + descriptive flags."""
    rows = []
    for model in sorted(runs):
        for item_id, it in items.items():
            cells = runs[model].get(item_id, {})
            vals = {}
            missing = []
            for kind in MAIN_CELLS:
                r = cells.get(kind)
                if r is None or r.get("value") is None:
                    missing.append(kind)
                    vals[kind] = None
                else:
                    vals[kind] = r["value"]
            probes = {k: cells.get(k, {}).get("p_yes")
                      for k in PROBE_CELLS}
            masses = [cells[k].get("mass") for k in MAIN_CELLS
                      if k in cells and cells[k].get("mass") is not None]
            rec = {
                "model": model, "item_id": item_id,
                "task_family": it["task_family"],
                "source": it["_meta"].get("source"),
                "stratum": it["_meta"].get("stratum"),
                "direction": it["critical_direction"],
                "claim": (it.get("base_context") or "").strip(),
                "missing": missing,
                "mass_min": min(masses) if masses else None,
                **{f"Y_{k}": vals[k] for k in MAIN_CELLS},
                **{f"p_{k}": probes[k] for k in PROBE_CELLS},
            }
            if not missing:
                s = 1.0 if it["critical_direction"] == "increase" else -1.0
                ya = (vals["admit_pre"] + vals["admit_post"]) / 2.0
                e = s * (ya - vals["base"])
                lpre = s * (vals["exclude_pre"] - vals["base"])
                lpost = s * (vals["exclude_post"] - vals["base"])
                rec.update({
                    "s": s, "Y_admit": ya, "E": e, "L_pre": lpre,
                    "L_post": lpost,
                    # non-shared-baseline estimands (C's baseline is
                    # Y_admit_*, not Y_base): A = admitted effect per phase,
                    # C = retraction from the admitted judgment (C=0: no
                    # change; C=-A: back to baseline; C<-A: overshoot)
                    "A_pre": s * (vals["admit_pre"] - vals["base"]),
                    "A_post": s * (vals["admit_post"] - vals["base"]),
                    "C_pre": s * (vals["exclude_pre"] - vals["admit_pre"]),
                    "C_post": s * (vals["exclude_post"] - vals["admit_post"]),
                    "gain_pre": None if e == 0 else lpre / e,
                    "gain_post": None if e == 0 else lpost / e,
                    "e_pos": e > 0,
                    "floor": [k for k in MAIN_CELLS
                              if vals[k] <= FLOOR],
                    "ceil": [k for k in MAIN_CELLS
                             if vals[k] >= CEIL],
                })
            rows.append(rec)
    return rows


# ---------------------------------------------------------------------------
# sections
# ---------------------------------------------------------------------------
def integrity_block(runs, rows, items):
    per_cell_missing = Counter()
    for r in rows:
        for k in r["missing"]:
            per_cell_missing[f"{r['model']}/{k}"] += 1
    complete = [r for r in rows if not r["missing"]]
    health = {
        "models": sorted(runs),
        "n_items": len(items),
        "expected_rows": len(items) * len(runs),
        "rows_built": len(rows),
        "complete_rows": len(complete),
        "incomplete_rows": len(rows) - len(complete),
        "missing_by_cell": dict(sorted(per_cell_missing.items())),
        "mass_lt_05_by_model": dict(sorted(Counter(
            r["model"] for r in rows
            if r["mass_min"] is not None and r["mass_min"] < 0.5).items())),
        "unparsed_values": sum(1 for r in rows
                               for k in MAIN_CELLS if r[f"Y_{k}"] is None),
    }
    return health


def cross_check(rows):
    """Reproduce the published pooled-4 numbers from this table (info only)."""
    p4 = [r for r in rows if r["model"] != SELECTOR and not r["missing"]]
    usable = [r for r in p4 if r["e_pos"]]
    wins = lambda x: max(-3.0, min(3.0, x))
    got = {
        "alignment": st.mean([1.0 if r["E"] > 0 else 0.0 for r in p4]),
        "n_usable": len(usable),
        "median_absL": st.median([abs(r["E"]) for r in usable]),
        "REI_pre": st.mean([wins(r["L_pre"] / abs(r["E"]))
                            for r in usable]),
        "REI_post": st.mean([wins(r["L_post"] / abs(r["E"]))
                             for r in usable]),
        "frac_post_gt_pre": st.mean(
            [1.0 if (r["L_post"] / abs(r["E"])) >
                (r["L_pre"] / abs(r["E"])) else 0.0 for r in usable]),
    }
    checks = {}
    for k, pub in PUBLISHED.items():
        if k == "n_usable":
            tol = 0.5
        elif k == "median_absL":
            tol = 0.05            # MD prints one decimal (32.7)
        elif k in ("alignment", "frac_post_gt_pre"):
            tol = 0.01            # MD prints two decimals
        else:
            tol = 0.002           # MD prints three decimals
        checks[k] = {"published": pub, "recomputed": got[k],
                     "ok": abs(got[k] - pub) <= tol}
    return got, checks


def e_vs_l_block(rows, pred=lambda r: True):
    """Fixed-width E bins x mean/median L and gain, plus rank correlations."""
    sub = [r for r in rows if not r["missing"] and pred(r)]
    bins = []
    lo = -100.0
    while lo < 100.0 - 1e-9:
        hi = lo + E_BIN_WIDTH
        sel = [r for r in sub
               if (lo <= r["E"] < hi or (hi >= 100.0 - 1e-9
                                         and r["E"] >= hi))]
        if sel:
            bins.append({
                "E_range": [lo, hi], "n": len(sel),
                "mean_E": mean_or_none([r["E"] for r in sel]),
                "median_L_pre": med_or_none([r["L_pre"] for r in sel]),
                "mean_L_pre": mean_or_none([r["L_pre"] for r in sel]),
                "median_L_post": med_or_none([r["L_post"] for r in sel]),
                "mean_L_post": mean_or_none([r["L_post"] for r in sel]),
                "median_gain_pre": med_or_none([r["gain_pre"] for r in sel]),
                "median_gain_post": med_or_none([r["gain_post"]
                                                 for r in sel]),
            })
        lo = hi
    xs_e = [r["E"] for r in sub]
    return {
        "n": len(sub),
        "spearman_E_Lpre": spearman(xs_e, [r["L_pre"] for r in sub]),
        "spearman_E_Lpost": spearman(xs_e, [r["L_post"] for r in sub]),
        "spearman_Lpre_Lpost": spearman([r["L_pre"] for r in sub],
                                        [r["L_post"] for r in sub]),
        "bins": bins,
    }


def region_block(rows, pred=lambda r: True):
    """Counts vs the two natural reference lines L = 0 and L = E.

    Short region codes (legend is written into the report):
      L_neg     L < 0        (opposite to the annotated direction)
      E_nonpos  E <= 0       (admitted evidence moves the wrong way)
      L_gt_E    L > E        (residual beyond the full admitted effect)
      L_mid     E/2 <= L <= E
      L_small   0 <= L < E/2
    """
    sub = [r for r in rows if not r["missing"] and pred(r)]
    out = {}
    for arm, key in (("pre", "L_pre"), ("post", "L_post")):
        reg = Counter()
        for r in sub:
            v = r[key]
            if v < 0:
                reg["L_neg"] += 1
            elif r["E"] <= 0:
                reg["E_nonpos"] += 1
            elif v > r["E"]:
                reg["L_gt_E"] += 1
            elif v >= 0.5 * r["E"]:
                reg["L_mid"] += 1
            else:
                reg["L_small"] += 1
        out[arm] = {"n": len(sub),
                    "regions": {k: reg.get(k, 0)
                                for k in ("L_neg", "E_nonpos", "L_gt_E",
                                          "L_mid", "L_small")},
                    "frac_L_neg": reg.get("L_neg", 0) / len(sub)
                    if sub else None}
    return out


REGION_LEGEND = {
    "L_neg": "L < 0 (opposite to annotated direction)",
    "E_nonpos": "E <= 0 (admitted evidence moves wrong way)",
    "L_gt_E": "L > E (beyond full admitted effect)",
    "L_mid": "E/2 <= L <= E (large residual)",
    "L_small": "0 <= L < E/2 (small residual)",
}


def histogram(vals, width, lo=None, hi=None):
    """Fixed-width histogram; returns bin -> count (no thresholds)."""
    if not vals:
        return {}
    lo = min(vals) if lo is None else lo
    hi = max(vals) if hi is None else hi
    bins = defaultdict(int)
    for v in vals:
        b = lo + math.floor((v - lo) / width) * width
        b = min(b, hi - width + width * 1e-9)
        bins[round(b, 6)] += 1
    return dict(sorted(bins.items()))


def strat_grid(rows):
    """model x source x direction descriptive grid."""
    groups = defaultdict(list)
    for r in rows:
        if r["missing"]:
            continue
        groups[(r["model"], r["source"], r["direction"])].append(r)
    grid = {}
    for k in sorted(groups):
        g = groups[k]
        grid["/".join(k)] = {
            "n": len(g),
            "frac_E_pos": st.mean([1.0 if r["E"] > 0 else 0.0
                                   for r in g]),
            "median_E": med_or_none([r["E"] for r in g]),
            "median_L_pre": med_or_none([r["L_pre"] for r in g]),
            "median_L_post": med_or_none([r["L_post"] for r in g]),
            "median_gain_pre": med_or_none([r["gain_pre"] for r in g
                                            if r["gain_pre"] is not None]),
            "spearman_E_Lpre": spearman([r["E"] for r in g],
                                        [r["L_pre"] for r in g]),
        }
    return grid


def base_deciles(rows):
    """Y_base deciles x E / L_pre / gain — descriptive strata."""
    sub = [r for r in rows if not r["missing"]]
    ordered = sorted(sub, key=lambda r: r["Y_base"])
    out = []
    for i in range(10):
        chunk = ordered[i * len(ordered) // 10:(i + 1) * len(ordered) // 10]
        if not chunk:
            continue
        out.append({
            "Y_base_range": [round(chunk[0]["Y_base"], 1),
                             round(chunk[-1]["Y_base"], 1)],
            "n": len(chunk),
            "median_E": med_or_none([r["E"] for r in chunk]),
            "median_L_pre": med_or_none([r["L_pre"] for r in chunk]),
            "median_gain_pre": med_or_none([r["gain_pre"] for r in chunk
                                            if r["gain_pre"] is not None]),
            "frac_E_pos": st.mean([1.0 if r["E"] > 0 else 0.0
                                   for r in chunk]),
        })
    return out


def floor_ceil_block(rows):
    out = {}
    for model in sorted({r["model"] for r in rows}):
        sub = [r for r in rows if r["model"] == model and not r["missing"]]
        out[model] = {
            "n": len(sub),
            "floor_le5": {k: sum(1 for r in sub if r[f"Y_{k}"] <= FLOOR)
                          for k in MAIN_CELLS},
            "ceil_ge95": {k: sum(1 for r in sub if r[f"Y_{k}"] >= CEIL)
                          for k in MAIN_CELLS},
        }
    return out


def probe_block(rows):
    out = {}
    for model in sorted({r["model"] for r in rows}):
        sub = [r for r in rows if r["model"] == model]
        out[model] = {}
        for k in PROBE_CELLS:
            v = [r[f"p_{k}"] for r in sub if r.get(f"p_{k}") is not None]
            out[model][k] = {"n": len(v), "mean_p_yes": mean_or_none(v)}
    return out


def case_lists(rows, n_show=6):
    """Reading samples — descriptive selections, no pass/fail semantics."""
    ok = [r for r in rows if not r["missing"]]
    ep = [r for r in ok if r["E"] > 0]
    fmt = lambda r: {
        "model": r["model"], "item_id": r["item_id"],
        "stratum": r["stratum"], "direction": r["direction"],
        "Y_base": round(r["Y_base"], 1), "Y_admit": round(r["Y_admit"], 1),
        "Y_exclude_pre": round(r["Y_exclude_pre"], 1),
        "Y_exclude_post": round(r["Y_exclude_post"], 1),
        "E": round(r["E"], 1), "L_pre": round(r["L_pre"], 1),
        "L_post": round(r["L_post"], 1),
        "claim": r["claim"][:90],
    }
    hi_leak = sorted(ep, key=lambda r: r["L_pre"], reverse=True)[:n_show]
    near_zero = sorted(ep, key=lambda r: abs(r["L_pre"]))[:n_show]
    flips = sorted([r for r in ep if r["L_pre"] < 0],
                   key=lambda r: r["L_pre"])[:n_show]
    neg_e = sorted([r for r in ok if r["E"] <= 0],
                   key=lambda r: r["E"])[:n_show]
    # reading strata with real leverage: among E >= 40 (a stratum for
    # qualitative reading, not a gate), the strongest removal candidates
    # (small |L_pre| despite big E) and the strongest full-leak candidates
    # (L_pre at or above E).
    strong = [r for r in ep if r["E"] >= 40.0]
    removal = sorted(strong, key=lambda r: abs(r["L_pre"]))[:n_show]
    full_leak = sorted(strong,
                       key=lambda r: r["L_pre"] - r["E"],
                       reverse=True)[:n_show]
    return {"largest_L_pre": [fmt(r) for r in hi_leak],
            "smallest_abs_L_pre": [fmt(r) for r in near_zero],
            "L_pre_negative_flips": [fmt(r) for r in flips],
            "E_nonpositive": [fmt(r) for r in neg_e],
            "E_ge40_smallest_abs_L_pre": [fmt(r) for r in removal],
            "E_ge40_L_closest_to_E": [fmt(r) for r in full_leak]}


def write_csv(rows, path):
    cols = (["model", "item_id", "task_family", "source", "stratum",
             "direction", "s", "Y_base", "Y_admit_pre", "Y_admit_post",
             "Y_admit", "Y_exclude_pre", "Y_exclude_post", "E", "L_pre",
             "L_post", "A_pre", "A_post", "C_pre", "C_post",
             "gain_pre", "gain_post", "e_pos", "claim"])
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for r in sorted(rows, key=lambda r: (r["model"], r["item_id"])):
            w.writerow([r.get(c) for c in cols])


def _md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join("---" for _ in headers) + "|"]
    for row in rows:
        out.append("| " + " | ".join(str(c) for c in row) + " |")
    return out


def _fm(x, nd=2):
    if x is None:
        return "n/a"
    if isinstance(x, float):
        return f"{x:+.{nd}f}"
    return str(x)


def write_md(report, path, fig_info):
    """Human-readable map — every number generated from the report dict."""
    L = []

    def add(x):
        L.append("\n".join(x) if isinstance(x, list) else x)
    add("# G24A Prospective Exclusion Phenomenology Map (discovery layer)")
    add("")
    add("**Layer 1 of the three-layer process (discovery -> hypothesis "
        "formation -> confirmation). No KILL gates: every stratum is "
        "reported, small or messy. Observations only — these numbers may "
        "seed hypothesis formation but are NOT confirmatory claims.**")
    add("")
    add("Unit: item x model. Definitions (G0-compatible):")
    add("")
    add("- `Y_admit = (admit_pre + admit_post)/2`")
    add("- `E = s*(Y_admit - Y_base)` — evidence leverage "
        "(s = +1 increase / -1 decrease; G0 `signed_L`)")
    add("- `L_pre = s*(Y_exclude_pre - Y_base)` — prospective residual")
    add("- `L_post = s*(Y_exclude_post - Y_base)` — retrospective residual")
    add("- `gain = L / E` (ratio; unbounded as E -> 0, so medians/strata "
        "are used, never the mean)")
    add("- `A_pre = s*(Y_admit_pre - Y_base)`, `A_post = s*(Y_admit_post - "
        "Y_base)` — admitted effect per phase (baseline Y_base)")
    add("- `C_pre = s*(Y_exclude_pre - Y_admit_pre)`, `C_post = "
        "s*(Y_exclude_post - Y_admit_post)` — retraction from the admitted "
        "judgment after the exclude ruling; its baseline is the "
        "corresponding Y_admit_* phase, NOT Y_base (`C = 0`: no change; "
        "`C = -A`: exactly back to baseline; `C < -A`: overshoot)")
    add("")
    add("Identity reference lines: `L = E` (residual equals the full "
        "admitted effect = as-if-not-excluded), `L = 0` (removal), "
        "`L < 0` (opposite to the annotated direction).")
    add("")
    add("**Standing caveat (2026-09-25): `rho(E, L*)` shares `Y_base` "
        "mechanically and is DEMOTED to non-primary — treat it as "
        "description, not evidence. The primary cross-baseline quantities "
        "are `A*`/`C*` (section 3 note; matched-pair audit in "
        "`g24a_reversibility_v1`).**")
    add("")

    it = report["integrity"]
    add("## 0. Data and integrity")
    add("")
    add("\n".join(_md_table(
        ["models", "items", "rows", "complete", "incomplete",
         "unparsed cells", "mass<0.5 rows"],
        [[len(it["models"]), it["n_items"], it["rows_built"],
          it["complete_rows"], it["incomplete_rows"],
          it["unparsed_values"],
          sum(it["mass_lt_05_by_model"].values())]])))
    add("")
    add("Duplicate (item, kind) rows: "
        f"{len(report['duplicate_rows'])}.")
    add("")

    add("## 1. Definition cross-check vs `g24a_analysis_v1` (informational)")
    add("")
    cc = report["definition_cross_check_vs_g24a_analysis_v1"]
    add(_md_table(["quantity", "published", "recomputed", "match"],
                  [[k, v["published"], round(v["recomputed"], 4),
                    "OK" if v["ok"] else "DIFF"]
                   for k, v in cc["checks"].items()]))
    add("")

    add("## 2. Distributions (all rows, no exclusions)")
    add("")
    d = report["distributions"]
    rows = []
    for key in ("E", "L_pre", "L_post", "A_pre", "A_post", "C_pre",
                "C_post", "Y_base", "Y_admit",
                "gain_pre_Egt0", "gain_post_Egt0"):
        s = d[key]
        note = "  (mean poisoned by E->0 tails; use quantiles)" \
            if key.startswith("gain") else ""
        rows.append([f"`{key}`{note}", s["n"], _fm(s["mean"]),
                     _fm(s["p10"], 1), _fm(s["p25"], 1),
                     _fm(s["median"], 1), _fm(s["p75"], 1),
                     _fm(s["p90"], 1)])
    add(_md_table(["quantity", "n", "mean", "p10", "p25", "med", "p75",
                   "p90"], rows))
    add("")
    add("### gain stratified by |E| (E>0; ratio stability strata)")
    add("")
    rows = []
    for name, v in d["gain_by_absE_strata"].items():
        if not v["n"]:
            continue
        g, h = v["gain_pre"], v["gain_post"]
        rows.append([name, v["n"], f"{_fm(g['p25'])} / {_fm(g['median'])} / "
                     f"{_fm(g['p75'])}", _fm(h["median"]), _fm(v["median_L_pre"], 1)])
    add(_md_table(["abs(E) stratum", "n", "gain_pre p25/med/p75",
                   "gain_post med", "med L_pre"], rows))
    add("")

    add("## 3. E vs residual structure (binned; identity = full leak)")
    add("")
    st = report["structure_E_vs_L"]
    add("Pooled: spearman(E, L_pre) = "
        f"{_fm(st['overall']['spearman_E_Lpre'], 3)}, "
        f"spearman(E, L_post) = {_fm(st['overall']['spearman_E_Lpost'], 3)} "
        f"(n={st['overall']['n']}).")
    add("")
    add("**Status of these rho values: DEMOTED (2026-09-25). `E` and `L*` "
        "both contain `Y_base`, so `rho(E, L*)` is mechanically inflated by "
        "the shared baseline — descriptive only, NOT primary evidence.**")
    add("")
    ac = report["ac_cross_baseline"]
    add("Non-shared-baseline cross-correlations (Spearman, all complete "
        f"rows, n={ac['n_complete']}): rho(A_post, C_pre) = "
        f"{_fm(ac['spearman_Apost_Cpre'], 3)}, rho(A_pre, C_post) = "
        f"{_fm(ac['spearman_Apre_Cpost'], 3)}, rho(C_pre, C_post) = "
        f"{_fm(ac['spearman_Cpre_Cpost'], 3)}.")
    add("")
    add("Note: bins with E < 0 are rows where the admitted evidence moved "
        "against its annotated direction; for them `gain = L/E` is pure "
        "(E, L) geometry — a positive gain means L shares E's negative "
        "sign, not 'leakage in the annotated sense'.")
    add("")
    for model, blk in st["per_model"].items():
        add(f"### {model}  (n={blk['n']}, "
            f"rho(E,L_pre)={_fm(blk['spearman_E_Lpre'], 3)}, "
            f"rho(E,L_post)={_fm(blk['spearman_E_Lpost'], 3)})")
        add("")
        rows = []
        for b in blk["bins"]:
            rows.append([f"[{b['E_range'][0]:.0f}, {b['E_range'][1]:.0f})",
                         b["n"], _fm(b["mean_E"], 1),
                         _fm(b["median_L_pre"], 1),
                         _fm(b["median_gain_pre"]),
                         _fm(b["median_L_post"], 1)])
        add(_md_table(["E bin", "n", "mean E", "med L_pre", "med gain_pre",
                       "med L_post"], rows))
        add("")

    add("## 4. Regions vs the reference lines (counts)")
    add("")
    add("Legend: " + "; ".join(f"`{k}` = {v}"
                                for k, v in report["regions_vs_L0_and_LE"]
                                ["legend"].items()) + ".")
    add("")
    rg = report["regions_vs_L0_and_LE"]
    rows = []
    for scope in ("overall", "per_model"):
        blocks = {("pooled" if scope == "overall" else m):
                  (rg[scope] if scope == "overall" else rg[scope][m])
                  for m in ([None] if scope == "overall"
                            else sorted(rg[scope]))}
        for name, blk in blocks.items():
            for arm in ("pre", "post"):
                a = blk[arm]
                rows.append([name, arm, a["n"],
                             a["regions"]["L_neg"],
                             a["regions"]["E_nonpos"],
                             a["regions"]["L_gt_E"],
                             a["regions"]["L_mid"],
                             a["regions"]["L_small"],
                             _fm(a["frac_L_neg"], 3)])
    add(_md_table(["scope", "arm", "n", "L_neg", "E_nonpos", "L_gt_E",
                   "L_mid", "L_small", "frac L_neg"], rows))
    add("")

    add("## 5. Pre/post item-level correspondence")
    add("")
    pc = report["pre_post_correspondence"]
    add(f"spearman(L_pre, L_post) = {_fm(pc['spearman'], 3)}; quadrants: "
        + ", ".join(f"{k} = {v}" for k, v in pc["quadrants"].items()) + ".")
    add("")

    add("## 6. Stratified grid (model / source / direction)")
    add("")
    rows = []
    for k, v in report["strat_grid_model_source_direction"].items():
        rows.append([k, v["n"], _fm(v["frac_E_pos"], 2),
                     _fm(v["median_E"], 1), _fm(v["median_L_pre"], 1),
                     _fm(v["median_L_post"], 1),
                     _fm(v["median_gain_pre"]), _fm(v["spearman_E_Lpre"], 2)])
    add(_md_table(["stratum", "n", "frac E>0", "med E", "med L_pre",
                   "med L_post", "med gain_pre", "rho(E,L_pre)"], rows))
    add("")

    add("## 7. Y_base deciles")
    add("")
    rows = [[f"[{v['Y_base_range'][0]}, {v['Y_base_range'][1]}]", v["n"],
             _fm(v["median_E"], 1), _fm(v["median_L_pre"], 1),
             _fm(v["median_gain_pre"]), _fm(v["frac_E_pos"], 2)]
            for v in report["y_base_deciles"]]
    add(_md_table(["Y_base range", "n", "med E", "med L_pre",
                   "med gain_pre", "frac E>0"], rows))
    add("")

    add("## 8. Floor (<=5) / ceiling (>=95) counts per cell")
    add("")
    rows = []
    for m, v in report["floor_ceiling"].items():
        rows.append([m, "floor<=5",
                     *[v["floor_le5"][k] for k in MAIN_CELLS]])
        rows.append([m, "ceiling>=95",
                     *[v["ceil_ge95"][k] for k in MAIN_CELLS]])
    add(_md_table(["model", "kind", *MAIN_CELLS], rows))
    add("")

    add("## 9. Rule-probe context (stated knowledge of the ruling)")
    add("")
    rows = []
    for m, v in report["rule_probes_context"].items():
        rows.append([m,
                     _fm(v["rule_probe_exclude_pre"]["mean_p_yes"], 3),
                     _fm(v["rule_probe_exclude_post"]["mean_p_yes"], 3),
                     _fm(v["rule_probe_admit_post"]["mean_p_yes"], 3)])
    add(_md_table(["model", "p_yes exclude_pre", "p_yes exclude_post",
                   "p_yes admit_post"], rows))
    add("")

    add("## 10. Reading samples (descriptive selections)")
    add("")
    for name, srows in report["case_reading_samples"].items():
        add(f"### {name}")
        add("")
        rows = [[r["model"], r["item_id"], r["stratum"], r["direction"],
                 f"{r['Y_base']:.1f}", f"{r['Y_admit']:.1f}",
                 f"{r['Y_exclude_pre']:.1f}", f"{r['Y_exclude_post']:.1f}",
                 f"{r['E']:+.1f}", f"{r['L_pre']:+.1f}",
                 f"{r['L_post']:+.1f}",
                 r["claim"].replace("|", "/")[:60]]
                for r in srows]
        add(_md_table(["model", "item", "stratum", "dir", "Y0", "adm",
                       "excl_pre", "excl_post", "E", "L_pre", "L_post",
                       "claim"], rows))
        add("")

    add("## 11. Histograms (raw counts)")
    add("")
    h = report["region_histograms"]
    add("### L_pre (width 5, range [-100, 100))")
    add("")
    add("  " + "  ".join(f"{k}:{v}" for k, v in
                         h["L_pre_hist_width5"].items()))
    add("")
    add("### L_post - L_pre (width 5, range [-100, 100))")
    add("")
    add("  " + "  ".join(f"{k}:{v}" for k, v in
                         h["Lpost_minus_Lpre_hist_width5"].items()))
    add("")
    add("### gain_pre, E>0 (width 0.1 over [-1, 2); tails listed after)")
    add("")
    gh = {float(k): v for k, v in h["gain_pre_hist_width01"].items()}
    left = sum(v for k, v in gh.items() if k < -1.0)
    right = sum(v for k, v in gh.items() if k >= 2.0)
    inside = {k: v for k, v in sorted(gh.items())
              if -1.0 <= k < 2.0}
    add("  " + "  ".join(f"{k:+.1f}:{v}" for k, v in inside.items()))
    add("")
    add(f"  tails: below -1.0 = {left} rows; at/above 1.9 (incl. >=2.0 "
        f"clipped into 1.9 display bin) = {inside.get(1.9, 0)} rows; "
        f"raw >=2.0 = {right} rows.")
    add("")
    add("## 12. Figures")
    add("")
    for f in (fig_info or {}).get("figs") or []:
        add(f"- `{f}`")
    if not (fig_info or {}).get("figs"):
        add(f"- (not generated: {(fig_info or {}).get('note')})")
    add("")
    Path(path).write_text("\n".join(L), encoding="utf-8")


def try_figs(rows, outdir):
    """Optional scatters; failure to import matplotlib is not an error."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as exc:                                    # noqa: BLE001
        return {"figs": None, "note": f"matplotlib unavailable: {exc}"}
    outdir.mkdir(parents=True, exist_ok=True)
    ok = [r for r in rows if not r["missing"]]
    made = []
    for xk, yk, name, ref in (
            ("E", "L_pre", "E_vs_Lpre", True),
            ("E", "L_post", "E_vs_Lpost", True),
            ("L_pre", "L_post", "Lpre_vs_Lpost", False)):
        fig, ax = plt.subplots(figsize=(7, 7))
        ax.scatter([r[xk] for r in ok], [r[yk] for r in ok],
                   s=6, alpha=0.25, linewidths=0)
        if ref:
            lim = [-100, 100]
            ax.plot(lim, lim, "k--", lw=0.8, label="L = E")
            ax.axhline(0, color="gray", lw=0.6)
            ax.axvline(0, color="gray", lw=0.6)
            ax.set_xlim(lim)
            ax.set_ylim(lim)
            ax.legend()
        ax.set_xlabel(xk)
        ax.set_ylabel(yk)
        fig.tight_layout()
        p = outdir / f"{name}.png"
        fig.savefig(p, dpi=110)
        plt.close(fig)
        made.append(str(p))
    return {"figs": made}


# ---------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-prefix", default=OUT_PREFIX)
    ap.add_argument("--items", default=ITEMS)
    args = ap.parse_args()

    integrity = {"duplicates": [], "files": {}}
    items = load_items(args.items)
    paths = [p for p in RUNS if Path(p).exists()]
    if len(paths) != len(RUNS):
        raise SystemExit(f"missing run files: {set(RUNS) - set(paths)}")
    runs = load_runs(paths, integrity)
    if integrity["duplicates"]:
        raise SystemExit(f"INTEGRITY: duplicate rows: "
                         f"{integrity['duplicates'][:5]}")

    rows = build_rows(items, runs)
    complete = [r for r in rows if not r["missing"]]

    xcheck, checks = cross_check(rows)
    ep = [r for r in complete if r["E"] > 0]

    structure = {
        "overall": e_vs_l_block(rows),
        "pooled4_non_selector": e_vs_l_block(
            rows, lambda r: r["model"] != SELECTOR),
        "per_model": {m: e_vs_l_block(rows, lambda r, m=m:
                                      r["model"] == m)
                      for m in sorted(runs)},
        "per_source": {s: e_vs_l_block(rows, lambda r, s=s:
                                       r["source"] == s)
                       for s in sorted({r["source"] for r in complete})},
    }
    regions = {
        "overall": region_block(rows),
        "per_model": {m: region_block(rows, lambda r, m=m:
                                      r["model"] == m)
                      for m in sorted(runs)},
    }
    distributions = {
        k: quantiles([r[k] for r in complete])
        for k in ("E", "L_pre", "L_post", "A_pre", "A_post", "C_pre",
                  "C_post", "gain_pre", "gain_post",
                  "Y_base", "Y_admit")}
    distributions["gain_pre_Egt0"] = quantiles(
        [r["gain_pre"] for r in ep])
    distributions["gain_post_Egt0"] = quantiles(
        [r["gain_post"] for r in ep])
    # gain is a ratio: unbounded as E -> 0, so also report it stratified by
    # |E| (descriptive strata — arithmetic stability, NOT pass/fail cutoffs).
    gain_strata = {}
    for lo, hi in ((0, 10), (10, 20), (20, 40), (40, 60), (60, 101)):
        sel = [r for r in ep if lo <= r["E"] < hi]
        gain_strata[f"absE [{lo},{hi})"] = {
            "n": len(sel),
            "gain_pre": quantiles([r["gain_pre"] for r in sel]),
            "gain_post": quantiles([r["gain_post"] for r in sel]),
            "median_L_pre": med_or_none([r["L_pre"] for r in sel]),
        }
    distributions["gain_by_absE_strata"] = gain_strata

    report = {
        "layer": "discovery (no KILL gates; observations only)",
        "definitions": {
            "E": "s*( (admit_pre+admit_post)/2 - base )",
            "L_pre": "s*( exclude_pre - base )",
            "L_post": "s*( exclude_post - base )",
            "gain_pre": "L_pre / E (undefined iff E == 0)",
            "A_pre": "s*( admit_pre - base )  (non-shared-baseline)",
            "A_post": "s*( admit_post - base )  (non-shared-baseline)",
            "C_pre": "s*( exclude_pre - admit_pre )  (retraction; "
                     "baseline is admit_pre, NOT base)",
            "C_post": "s*( exclude_post - admit_post )  (retraction; "
                      "baseline is admit_post, NOT base)",
        },
        "integrity": integrity_block(runs, rows, items),
        "duplicate_rows": integrity["duplicates"],
        "definition_cross_check_vs_g24a_analysis_v1": {
            "recomputed": xcheck, "checks": checks},
        "distributions": distributions,
        "ac_cross_baseline": {
            "note": (
                "rho(E, L*) shares Y_base mechanically (both anchored on "
                "Y_base) -> DEMOTED to non-primary on 2026-09-25. These "
                "Spearman cross-correlations use non-overlapping baselines "
                "(each C's baseline is its own Y_admit_* phase); Spearman "
                "over all complete rows."),
            "n_complete": len(complete),
            "spearman_Apost_Cpre": spearman([r["A_post"] for r in complete],
                                             [r["C_pre"] for r in complete]),
            "spearman_Apre_Cpost": spearman([r["A_pre"] for r in complete],
                                             [r["C_post"] for r in complete]),
            "spearman_Cpre_Cpost": spearman([r["C_pre"] for r in complete],
                                             [r["C_post"] for r in complete]),
        },
        "structure_E_vs_L": structure,
        "regions_vs_L0_and_LE": {"legend": REGION_LEGEND, **regions},
        "region_histograms": {
            "L_pre_hist_width5": histogram([r["L_pre"] for r in complete], 5.0,
                                           -100.0, 100.0),
            "gain_pre_hist_width01": histogram(
                [r["gain_pre"] for r in ep], GAIN_BIN_WIDTH, -1.0, 2.0),
            "Lpost_minus_Lpre_hist_width5": histogram(
                [r["L_post"] - r["L_pre"] for r in complete], 5.0,
                -100.0, 100.0),
        },
        "y_base_deciles": base_deciles(rows),
        "strat_grid_model_source_direction": strat_grid(rows),
        "floor_ceiling": floor_ceil_block(rows),
        "rule_probes_context": probe_block(rows),
        "case_reading_samples": case_lists(rows),
        "pre_post_correspondence": {
            "spearman": spearman([r["L_pre"] for r in complete],
                                 [r["L_post"] for r in complete]),
            "quadrants": dict(sorted(Counter(
                f"L_pre_{'>=' if r['L_pre'] >= 0 else '<'}0, "
                f"L_post_{'>=' if r['L_post'] >= 0 else '<'}0"
                for r in complete).items())),
        },
    }

    Path(args.out_prefix).parent.mkdir(parents=True, exist_ok=True)
    json.dump(report, open(args.out_prefix + ".json", "w"),
              indent=1, ensure_ascii=False, default=str)
    write_csv(rows, Path(args.out_prefix + "_itemmodel.csv"))
    fig_info = try_figs(rows, Path(args.out_prefix).parent / "figs")
    json.dump(fig_info, open(args.out_prefix + "_figs.json", "w"), indent=1)
    write_md(report, args.out_prefix + ".md", fig_info)

    # ---- stdout: the map at a glance ------------------------------------
    print(f"rows {len(rows)} (complete {len(complete)}), "
          f"items {len(items)}, models {len(runs)}")
    print("cross-check vs g24a_analysis_v1 pooled-4:",
          {k: (v["ok"], round(v["recomputed"], 3))
           for k, v in checks.items()})
    d = distributions
    for k in ("E", "L_pre", "L_post", "gain_pre_Egt0"):
        s = d[k]
        print(f"  {k:14s} n={s['n']} mean={s['mean']:+.2f} "
              f"med={s['median']:+.2f} p10={s['p10']:+.2f} "
              f"p90={s['p90']:+.2f}")
    ov = structure["overall"]
    rho_pp = report["pre_post_correspondence"]["spearman"]
    fmt_rho = lambda x: "n/a" if x is None else f"{x:+.3f}"
    print(f"  spearman(E,L_pre)={fmt_rho(ov['spearman_E_Lpre'])} "
          f"spearman(E,L_post)={fmt_rho(ov['spearman_E_Lpost'])} "
          f"spearman(L_pre,L_post)={fmt_rho(rho_pp)}")
    acv = report["ac_cross_baseline"]
    print(f"  ac cross-baseline (demoted-sharedY0 fix): "
          f"rho(A_post,C_pre)={fmt_rho(acv['spearman_Apost_Cpre'])} "
          f"rho(A_pre,C_post)={fmt_rho(acv['spearman_Apre_Cpost'])} "
          f"rho(C_pre,C_post)={fmt_rho(acv['spearman_Cpre_Cpost'])}")
    print("  per-model spearman(E,L_pre):",
          {m: (round(v['spearman_E_Lpre'], 3) if v['spearman_E_Lpre'] is not None else None)
           for m, v in structure["per_model"].items()})
    print("  per-model pre-regions:",
          {m: regions["per_model"][m]["pre"]["regions"]
           for m in sorted(runs)})
    print(f"wrote {args.out_prefix}.json / _itemmodel.csv / _figs.json "
          f"{fig_info.get('figs')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
