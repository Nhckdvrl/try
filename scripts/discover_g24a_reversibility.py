#!/usr/bin/env python3
"""G24A evidence-reversibility / direction-asymmetry audit (discovery layer).

Layer 1 of the three-layer process: no KILL gates, observations only.
No new model runs, no prereg — this audits EXISTING rerun rows.

Motivation (user, 2026-09-25): rho(E, L*) shares Y_base mechanically and
was demoted; the primary quantities are the non-shared-baseline pair

    A_pre  = s*(Y_admit_pre  - Y_base)         (admitted effect, pre)
    A_post = s*(Y_admit_post - Y_base)         (admitted effect, post)
    C_pre  = s*(Y_exclude_pre  - Y_admit_pre)  (retraction, pre;  C=0 none,
    C_post = s*(Y_exclude_post - Y_admit_post) C=-A back to base,
                                                 C<-A overshoot)

Core control: the 600-item file contains groups of items with EXACTLY the
same evidence text but claims in both directions. Within such a group the
evidence content is fixed, so comparing retraction of the supported claim
vs the contradicted claim isolates direction from evidence identity.

Sections:
  0. data & integrity (group detection, counts)
  1. estimands + cross-baseline correlation panel (vs demoted shared-Y0)
  2. CORE: exact-evidence matched pairs (pooled / model / model x source)
  3. claim-pair contradiction taxonomy (optional input, hand-classified)
  4. rationale paired coding (optional input, behavioral description only)
  5. baseline / leverage common-support strata

Outputs: results/discovery/g24a_reversibility_v1.{md,json}
         results/discovery/g24a_reversibility_v1_pairs.csv
Usage:   PYTHONPATH=src python scripts/discover_g24a_reversibility.py
"""
from __future__ import annotations

import csv
import hashlib
import json
import statistics as st
from collections import Counter, defaultdict
from pathlib import Path

ITEMMODEL = "results/discovery/g24a_phenomenology_v1_itemmodel.csv"
ITEMS = "data/items/g24a_v1.jsonl"
OUT_PREFIX = "results/discovery/g24a_reversibility_v1"
CLAIM_PAIRS = OUT_PREFIX + "_claim_pairs.csv"          # section 3 (hand-made)
CODING_GLOB = "_coding_"                                # section 4 (agents)
MODELS = ["gemma3-12b", "llama31-8b", "mistral-small-24b", "qwen3-8b",
          "qwen35-9b"]
SOURCES = ["fever", "scifact"]


# ---------------------------------------------------------------------------
# load & derive
# ---------------------------------------------------------------------------
def load_rows():
    rows = list(csv.DictReader(open(ITEMMODEL, encoding="utf-8")))
    for r in rows:
        for k in ("Y_base", "Y_admit_pre", "Y_admit_post",
                  "Y_exclude_pre", "Y_exclude_post", "s"):
            r[k] = float(r[k])
        r["A_pre"] = r["s"] * (r["Y_admit_pre"] - r["Y_base"])
        r["A_post"] = r["s"] * (r["Y_admit_post"] - r["Y_base"])
        r["C_pre"] = r["s"] * (r["Y_exclude_pre"] - r["Y_admit_pre"])
        r["C_post"] = r["s"] * (r["Y_exclude_post"] - r["Y_admit_post"])
    return rows


def load_groups():
    """Exact-evidence groups containing both claim directions."""
    by_ev = defaultdict(list)
    for l in open(ITEMS, encoding="utf-8"):
        it = json.loads(l)
        by_ev[it["critical_evidence"]].append(it)
    groups = {}
    for ev, its in by_ev.items():
        inc = [i for i in its if i["critical_direction"] == "increase"]
        dec = [i for i in its if i["critical_direction"] == "decrease"]
        if inc and dec:
            sha = hashlib.sha256(ev.encode("utf-8")).hexdigest()[:10]
            groups[sha] = {
                "evidence": ev,
                "inc": [i["item_id"] for i in inc],
                "dec": [i["item_id"] for i in dec],
                "source": (inc + dec)[0]["meta"].get("source"),
                "claims": {i["item_id"]: i["base_context"] for i in inc + dec},
            }
    return groups


def build_pairs(rows, groups):
    rowby = {(r["item_id"], r["model"]): r for r in rows}
    pairs = []
    for sha, g in sorted(groups.items()):
        for m in MODELS:
            def side(ids, k):
                return st.mean(rowby[(i, m)][k] for i in ids)
            p = {
                "group_sha": sha, "model": m, "source": g["source"],
                "inc_items": ",".join(g["inc"]),
                "dec_items": ",".join(g["dec"]),
            }
            for k in ("C_pre", "C_post", "A_pre", "A_post"):
                p[f"{k}_inc"] = side(g["inc"], k)
                p[f"{k}_dec"] = side(g["dec"], k)
            p["Y0_inc"] = side(g["inc"], "Y_base")
            p["Y0_dec"] = side(g["dec"], "Y_base")
            p["dC_pre"] = p["C_pre_inc"] - p["C_pre_dec"]
            p["dC_post"] = p["C_post_inc"] - p["C_post_dec"]
            p["dA_post"] = p["A_post_inc"] - p["A_post_dec"]
            p["dA_pre"] = p["A_pre_inc"] - p["A_pre_dec"]
            p["dY0"] = p["Y0_inc"] - p["Y0_dec"]
            pairs.append(p)
    return pairs


def quant(v):
    v = sorted(v)
    if not v:
        return None
    q = lambda f: v[min(len(v) - 1, max(0, int(round(f * (len(v) - 1)))))]
    return {"n": len(v), "min": v[0], "p10": q(0.10), "p25": q(0.25),
            "median": st.median(v), "p75": q(0.75), "p90": q(0.90),
            "max": v[-1], "mean": st.mean(v)}


def neg_frac(sub, key):
    return None if not sub else sum(1 for p in sub if p[key] < 0) / len(sub)


def paired_summary(sub):
    return {
        "n": len(sub),
        "dC_pre_median": st.median(p["dC_pre"] for p in sub) if sub else None,
        "dC_pre_neg_frac": neg_frac(sub, "dC_pre"),
        "dC_post_median": st.median(p["dC_post"] for p in sub) if sub else None,
        "dC_post_neg_frac": neg_frac(sub, "dC_post"),
    }


# ---------------------------------------------------------------------------
# optional inputs (sections 3 & 4)
# ---------------------------------------------------------------------------
def load_claim_pairs():
    if not Path(CLAIM_PAIRS).exists():
        return None
    return list(csv.DictReader(open(CLAIM_PAIRS, encoding="utf-8")))


def load_coding():
    files = sorted(Path("results/discovery").glob(
        f"{OUT_PREFIX.split('/')[-1]}_coding_*.jsonl"))
    if not files:
        return None
    cells = []
    for f in files:
        for l in open(f, encoding="utf-8"):
            if l.strip():
                c = json.loads(l)
                c["_file"] = f.name
                cells.append(c)
    return cells


# ---------------------------------------------------------------------------
# markdown helpers
# ---------------------------------------------------------------------------
def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join("---" for _ in headers) + "|"]
    for row in rows:
        out.append("| " + " | ".join(str(c) for c in row) + " |")
    return out


def fm(x, n=2):
    if x is None:
        return "n/a"
    return f"{x:+.{n}f}" if isinstance(x, float) else str(x)


def pct(x):
    return "n/a" if x is None else f"{100 * x:.1f}%"


# ---------------------------------------------------------------------------
def main() -> int:
    rows = load_rows()
    groups = load_groups()
    pairs = build_pairs(rows, groups)

    n_inc = sum(len(g["inc"]) for g in groups.values())
    n_dec = sum(len(g["dec"]) for g in groups.values())
    size_dist = Counter((len(g["inc"]), len(g["dec"]))
                        for g in groups.values())
    assert len(pairs) == len(groups) * len(MODELS), "pair count mismatch"

    # cross-baseline spearman panel (recomputed here for self-containment)
    def spearman(xs, ys):
        def rk(v):
            order = sorted(range(len(v)), key=lambda i: v[i])
            out = [0.0] * len(v)
            i = 0
            while i < len(order):
                j = i
                while j + 1 < len(order) and v[order[j + 1]] == v[order[i]]:
                    j += 1
                avg = (i + j) / 2 + 1
                for k in range(i, j + 1):
                    out[order[k]] = avg
                i = j + 1
            return out
        a, b = rk(xs), rk(ys)
        ma, mb = st.mean(a), st.mean(b)
        cov = sum((x - ma) * (y - mb) for x, y in zip(a, b))
        va = sum((x - ma) ** 2 for x in a)
        vb = sum((y - mb) ** 2 for y in b)
        return cov / (va * vb) ** 0.5

    ac_panel = {
        "spearman_Apost_Cpre": spearman([r["A_post"] for r in rows],
                                         [r["C_pre"] for r in rows]),
        "spearman_Apre_Cpost": spearman([r["A_pre"] for r in rows],
                                         [r["C_post"] for r in rows]),
        "spearman_Cpre_Cpost": spearman([r["C_pre"] for r in rows],
                                         [r["C_post"] for r in rows]),
    }

    # section 2 tables
    pooled = paired_summary(pairs)
    per_model = {m: paired_summary([p for p in pairs if p["model"] == m])
                 for m in MODELS}
    per_ms = {}
    for m in MODELS:
        for s in SOURCES:
            sub = [p for p in pairs if p["model"] == m and p["source"] == s]
            if sub:
                per_ms[f"{m}/{s}"] = paired_summary(sub)

    # side medians: C_post by model x source x direction (all rows, not
    # only matched groups — the context table behind the matched result)
    side_med = {}
    for m in MODELS:
        for s in SOURCES:
            for d in ("increase", "decrease"):
                v = [r["C_post"] for r in rows
                     if r["model"] == m and r["source"] == s
                     and r["direction"] == d]
                side_med[f"{m}/{s}/{d}"] = {"n": len(v),
                                            "median_C_post": st.median(v)}

    # section 3: taxonomy
    tax = load_claim_pairs()
    tax_block = None
    if tax:
        by_type = defaultdict(lambda: {"pairs": [], "shas": []})
        for t in tax:
            by_type[t["contradiction_type"]]["shas"].append(t["group_sha"])
        pairby = defaultdict(list)
        for p in pairs:
            pairby[p["group_sha"]].append(p)
        for typ, blk in by_type.items():
            sub = [p for sha in blk["shas"] for p in pairby.get(sha, [])]
            blk["summary"] = paired_summary(sub)
        nonneg = [t for t in tax
                  if t["contradiction_type"] != "explicit_negation"]
        sub_nonneg = [p for t in nonneg for p in pairby.get(t["group_sha"], [])]
        tax_block = {
            "counts_by_type": dict(Counter(t["contradiction_type"]
                                           for t in tax)),
            "by_type": {k: v["summary"] for k, v in by_type.items()},
            "non_explicit_negation": paired_summary(sub_nonneg),
            "non_explicit_negation_by_model": {
                m: paired_summary([p for p in sub_nonneg
                                   if p["model"] == m])
                for m in MODELS},
            "n_classified": len(tax),
            "negation_present_counts": dict(Counter(
                t.get("negation_present", "") for t in tax)),
        }

    # section 4: rationale coding
    coding = load_coding()
    code_block = None
    if coding:
        labels = Counter()
        by_side = {"inc": Counter(), "dec": Counter()}
        pattern = Counter()
        by_model = defaultdict(lambda: {"inc": Counter(), "dec": Counter()})
        for c in coding:
            il = c.get("inc_label", "missing")
            dl = c.get("dec_label", "missing")
            labels[il] += 1
            labels[dl] += 1
            by_side["inc"][il] += 1
            by_side["dec"][dl] += 1
            by_model[c["model"]]["inc"][il] += 1
            by_model[c["model"]]["dec"][dl] += 1
            pattern[f"inc={il} | dec={dl}"] += 1
        code_block = {
            "cells": len(coding),
            "by_side": {k: dict(v) for k, v in by_side.items()},
            "pattern_counts": dict(pattern.most_common()),
            "by_model": {m: {s: dict(v) for s, v in sd.items()}
                         for m, sd in by_model.items()},
        }

    # section 5: common support
    cs = {
        "dY0": quant([p["dY0"] for p in pairs]),
        "dA_post": quant([p["dA_post"] for p in pairs]),
        "dA_pre": quant([p["dA_pre"] for p in pairs]),
        "subsets": {},
    }
    for thr in (5, 10, 20):
        sub = [p for p in pairs if abs(p["dY0"]) <= thr]
        cs["subsets"][f"|dY0|<={thr}"] = paired_summary(sub)
    for thr in (10, 20):
        sub = [p for p in pairs if abs(p["dA_post"]) <= thr]
        cs["subsets"][f"|dA_post|<={thr}"] = paired_summary(sub)
    sub = [p for p in pairs if abs(p["dY0"]) <= 10
           and abs(p["dA_post"]) <= 10]
    cs["subsets"]["|dY0|<=10 and |dA_post|<=10"] = paired_summary(sub)

    report = {
        "layer": "discovery (no KILL gates; observations only)",
        "lineage_note": (
            "Rows are the 2026-09-25 full re-run (commit e4319cb) on the "
            "corrected item file (92d8cd0). The SELECTION pass still used "
            "pre-fix claims, so this artifact is discovery-only and is "
            "NOT a strict prereg-confirmatory rerun; confirmatory lineage "
            "for paper RQ1 is an open governance item."),
        "integrity": {
            "rows": len(rows),
            "groups": len(groups),
            "items_in_groups": n_inc + n_dec,
            "inc_items": n_inc, "dec_items": n_dec,
            "size_dist": {str(k): v for k, v in sorted(size_dist.items())},
            "pairs": len(pairs),
            "unique_evidence_texts": len({g["evidence"]
                                           for g in groups.values()}),
        },
        "estimands": {
            "A_pre": "s*(admit_pre - base)",
            "A_post": "s*(admit_post - base)",
            "C_pre": "s*(exclude_pre - admit_pre)  (C=0 none, C=-A back to"
                     " baseline, C<-A overshoot)",
            "C_post": "s*(exclude_post - admit_post)",
            "cross_baseline_panel": ac_panel,
            "demoted": "rho(E, L*) shares Y_base mechanically; descriptive"
                       " only since 2026-09-25 (see phenomenology v1)",
        },
        "matched_pairs_core": {
            "definition": "dX = mean(X | increase-side items) - "
                          "mean(X | decrease-side items) within an "
                          "exact-evidence group, per model",
            "pooled": pooled,
            "per_model": per_model,
            "per_model_source": per_ms,
            "C_post_side_medians": side_med,
        },
        "common_support": cs,
        "taxonomy": tax_block,
        "rationale_coding": code_block,
    }

    # ---- pairs csv --------------------------------------------------------
    cols = ["group_sha", "model", "source", "inc_items", "dec_items",
            "C_pre_inc", "C_pre_dec", "C_post_inc", "C_post_dec",
            "A_pre_inc", "A_pre_dec", "A_post_inc", "A_post_dec",
            "Y0_inc", "Y0_dec", "dC_pre", "dC_post", "dA_pre", "dA_post",
            "dY0"]
    with open(OUT_PREFIX + "_pairs.csv", "w", newline="",
              encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for p in pairs:
            w.writerow([p[c] if not isinstance(p[c], float)
                        else round(p[c], 6) for c in cols])

    # ---- md ---------------------------------------------------------------
    L = ["# G24A evidence reversibility / direction-asymmetry audit v1",
         "",
         "**Layer 1 (discovery). No KILL gates; every stratum is reported. "
         "Observations only — not confirmatory claims, no new model runs, "
         "no prereg.**",
         "",
         f"Lineage: {report['lineage_note']}",
         "",
         "Estimands (non-shared-baseline): `A_pre = s*(admit_pre - base)`, "
         "`A_post = s*(admit_post - base)`; `C_pre = s*(exclude_pre - "
         "admit_pre)`, `C_post = s*(exclude_post - admit_post)`. `C = 0`: "
         "exclusion changed nothing; `C = -A`: exactly back to baseline; "
         "`C < -A`: overshoot beyond baseline.",
         "",
         "## 0. Data and integrity",
         "",
         *md_table(["quantity", "value"], [
             ["rows (item x model)", len(rows)],
             ["exact-evidence groups (both directions present)",
              len(groups)],
             ["items in groups", f"{n_inc + n_dec} "
              f"({n_inc} increase / {n_dec} decrease)"],
             ["group size dist (inc,dec)",
              json.dumps(report["integrity"]["size_dist"])],
             ["group x model pairs", len(pairs)],
         ]),
         "",
         "Detection = byte-exact `critical_evidence` equality, groups must "
         "contain at least one claim of each direction. Within a group the "
         "evidence text is fixed, so the inc-vs-dec contrast cannot be "
         "driven by evidence identity.",
         "",
         "## 1. Cross-baseline correlation panel (replaces shared-Y0 rho)",
         "",
         f"- rho(A_post, C_pre) = {fm(ac_panel['spearman_Apost_Cpre'], 3)}",
         f"- rho(A_pre, C_post) = {fm(ac_panel['spearman_Apre_Cpost'], 3)}",
         f"- rho(C_pre, C_post) = {fm(ac_panel['spearman_Cpre_Cpost'], 3)}",
         "",
         "Spearman over all 3000 complete rows; matches the independent "
         "recomputation exactly. `rho(E, L*)` (0.643/0.542 pre/post) is "
         "mechanically inflated by the shared Y_base and stays DEMOTED.",
         "",
         "## 2. CORE: exact-evidence matched pairs",
         "",
         f"`dC = mean(C | increase side) - mean(C | decrease side)` "
         f"within group, per model. n = {pooled['n']} pairs.",
         "",
         *md_table(["scope", "n", "median dC_pre", "% dC_pre<0",
                    "median dC_post", "% dC_post<0"],
                   [["**pooled**", pooled["n"],
                     fm(pooled["dC_pre_median"]), pct(pooled["dC_pre_neg_frac"]),
                     fm(pooled["dC_post_median"]),
                     pct(pooled["dC_post_neg_frac"])],
                    *[[
                        m, per_model[m]["n"],
                        fm(per_model[m]["dC_pre_median"]),
                        pct(per_model[m]["dC_pre_neg_frac"]),
                        fm(per_model[m]["dC_post_median"]),
                        pct(per_model[m]["dC_post_neg_frac"])]
                      for m in MODELS]]),
         "",
         "By model x source (median dC_post):",
         "",
         *md_table(["model/source", "n", "median dC_post", "% neg"],
                   [[k, v["n"], fm(v["dC_post_median"]),
                     pct(v["dC_post_neg_frac"])]
                    for k, v in per_ms.items()]),
         "",
         "Context: median C_post by model x source x direction (all rows):",
         "",
         *md_table(["cell", "n", "median C_post"],
                   [[k, v["n"], fm(v["median_C_post"])]
                    for k, v in side_med.items()]),
         "",
         "Reading: negative dC_post = the SUPPORTED (increase) side is "
         "retracted MORE than the CONTRADICTED (decrease) side under the "
         "same evidence text; a contradicted claim's post-retraction "
         "residual stays near zero (C_dec ~ 0 = `seen and never comes "
         "back`) while the supported side overshoots negative.",
         "",
    ]

    if tax_block:
        L += ["## 3. Claim-pair contradiction taxonomy (hand-classified)",
              "",
              f"Classified pairs: {tax_block['n_classified']}/"
              f"{len(groups)}. Types: "
              f"{json.dumps(tax_block['counts_by_type'])}",
              "",
              *md_table(["type", "n pairs", "median dC_pre", "% neg pre",
                         "median dC_post", "% neg post"],
                        [[t, blk["n"], fm(blk["dC_pre_median"]),
                          pct(blk["dC_pre_neg_frac"]),
                          fm(blk["dC_post_median"]),
                          pct(blk["dC_post_neg_frac"])]
                         for t, blk in tax_block["by_type"].items()]),
              "",
              "**Non-explicit-negation subset** (the user's key question):",
              "",
              *md_table(["n pairs", "median dC_pre", "% neg pre",
                         "median dC_post", "% neg post"],
                        [[tax_block["non_explicit_negation"]["n"],
                          fm(tax_block["non_explicit_negation"]["dC_pre_median"]),
                          pct(tax_block["non_explicit_negation"]["dC_pre_neg_frac"]),
                          fm(tax_block["non_explicit_negation"]["dC_post_median"]),
                          pct(tax_block["non_explicit_negation"]["dC_post_neg_frac"])]]),
              "",
              "Non-explicit-negation subset, per model (recurrence check):",
              "",
              *md_table(["model", "n", "median dC_pre", "% neg pre",
                         "median dC_post", "% neg post"],
                        [[m, v["n"], fm(v["dC_pre_median"]),
                          pct(v["dC_pre_neg_frac"]),
                          fm(v["dC_post_median"]),
                          pct(v["dC_post_neg_frac"])]
                         for m, v in
                         tax_block["non_explicit_negation_by_model"].items()]),
              ""]
    else:
        L += ["## 3. Claim-pair contradiction taxonomy",
              "",
              "PENDING: `_claim_pairs.csv` not present yet.", ""]

    if code_block:
        L += ["## 4. Rationale paired coding (behavioral description)",
              "",
              f"Cells coded: {code_block['cells']}/"
              f"{len(pairs)} (group x model, exclude_post, both sides). "
              "Labels are behavioral descriptions of the rationale text, "
              "NOT mechanism evidence.",
              "",
              *md_table(["side", "label counts"],
                        [[s, json.dumps(code_block["by_side"][s])]
                         for s in ("inc", "dec")]),
              "",
              "Combined patterns (top):",
              "",
              *md_table(["pattern (inc | dec)", "n"],
                        [[k, v] for k, v in
                         list(code_block["pattern_counts"].items())[:12]]),
              ""]
    else:
        L += ["## 4. Rationale paired coding",
              "",
              "PENDING: `_coding_*.jsonl` not present yet.", ""]

    L += ["## 5. Baseline / leverage common support",
          "",
          "Pair differences of the potential confounds:",
          "",
          *md_table(["quantity", "n", "p10", "median", "p90"],
                    [["dY0 (Y_base inc - dec)", cs["dY0"]["n"],
                      fm(cs["dY0"]["p10"], 1), fm(cs["dY0"]["median"], 1),
                      fm(cs["dY0"]["p90"], 1)],
                     ["dA_post (A_post inc - dec)", cs["dA_post"]["n"],
                      fm(cs["dA_post"]["p10"], 1),
                      fm(cs["dA_post"]["median"], 1),
                      fm(cs["dA_post"]["p90"], 1)],
                     ["dA_pre", cs["dA_pre"]["n"], fm(cs["dA_pre"]["p10"], 1),
                      fm(cs["dA_pre"]["median"], 1),
                      fm(cs["dA_pre"]["p90"], 1)]]),
          "",
          "dC_post inside common-support strata (descriptive, no cutoffs "
          "gating anything):",
          "",
          *md_table(["subset", "n", "median dC_post", "% neg"],
                    [[k, v["n"], fm(v["dC_post_median"]),
                      pct(v["dC_post_neg_frac"])]
                     for k, v in cs["subsets"].items()]),
          "",
          "## Provenance",
          "",
          f"- inputs: `{ITEMMODEL}` (columns A/C from commit 7feb552), "
          f"`{ITEMS}` (item file at 92d8cd0), rows from rerun e4319cb",
          "- pairs CSV: " + OUT_PREFIX + "_pairs.csv",
          "- taxonomy: " + CLAIM_PAIRS + " (hand-classified, section 3)",
          "- coding: " + OUT_PREFIX + "_coding_<model>.jsonl (section 4)",
          ""]

    Path(OUT_PREFIX).parent.mkdir(parents=True, exist_ok=True)
    json.dump(report, open(OUT_PREFIX + ".json", "w"),
              indent=1, ensure_ascii=False, default=str)
    open(OUT_PREFIX + ".md", "w", encoding="utf-8").write(
        "\n".join(L) + "\n")

    print(f"groups={len(groups)} items={n_inc + n_dec} pairs={len(pairs)}")
    print("ac panel:", {k: round(v, 3) for k, v in ac_panel.items()})
    print(f"pooled: dC_pre med {fm(pooled['dC_pre_median'])} "
          f"neg {pct(pooled['dC_pre_neg_frac'])} | dC_post med "
          f"{fm(pooled['dC_post_median'])} neg "
          f"{pct(pooled['dC_post_neg_frac'])}")
    for m in MODELS:
        v = per_model[m]
        print(f"  {m:20s} pre {fm(v['dC_pre_median'], 2)} "
              f"{pct(v['dC_pre_neg_frac']):>6s}  post "
              f"{fm(v['dC_post_median'], 2)} {pct(v['dC_post_neg_frac']):>6s}")
    print("taxonomy:", "present" if tax_block else "PENDING")
    print("coding:", "present" if code_block else "PENDING")
    print(f"wrote {OUT_PREFIX}.md / .json / _pairs.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
