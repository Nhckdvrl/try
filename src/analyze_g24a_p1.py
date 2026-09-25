"""Pilot P1 analysis — retraction-operator discrimination (Layer 2).

Readout is EXACTLY the frozen §4 of results/discovery/g24a_competing_accounts_v1.md
(spec frozen pre-run; freeze commit 1497c63, doc commit 7047098):

    polarity s = +1 for increase claims, -1 for decrease claims
    A  = s(Y_Admit  - Y_Base)      leverage
    C_k = s(Y_k     - Y_Admit)     intervention effect
    R_k = s(Y_k     - Y_Base)      residual
    D_k = |Y_k      - Y_Base|      "did it return to pre-evidence?"
    ideal removal: R_k = 0, C_k = -A ; within-pair dC_k = C_k^inc - C_k^dec

Y is the temp-0 digit-expectation decision value (0..100) per claim row.
Per-item identity C_k = R_k - A (s is a per-item sign, so it is exact) is
asserted for every cell; aggregation is a plain mean over the balanced
design (5 models x 192 items).  NO p-values, NO bootstrap, NO gates, NO
selection: small-A items are kept and displayed in leverage bands
(descriptive only, never a filter).

Outputs:
    <out-prefix>.md    human report
    <out-prefix>.json  all numbers + integrity block
    <out-prefix>_cells.csv  model,item_id,group_sha,polarity,kind,value

Usage:
    python src/analyze_g24a_p1.py \
        --runs results/raw/mistral-small-24b_g24a_p1.jsonl ... (5 files) \
        --items data/items/g24a_p1_v1.jsonl \
        --out-prefix results/g24a/g24a_p1_analysis_v1
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from collections import defaultdict

EXPECTED_MODELS = ["mistral-small-24b", "llama31-8b", "gemma3-12b",
                   "qwen3-8b", "qwen35-9b"]
COND = ["base", "admit_post", "exclude_post", "strong_exclude_post",
        "counterfactual_delete_post"]
KIND_LABEL = {"base": "Base", "admit_post": "AdmitPost",
              "exclude_post": "ExcludePost",
              "strong_exclude_post": "StrongExcludePost",
              "counterfactual_delete_post": "CounterfactualDeletePost"}
KS = ["exclude_post", "strong_exclude_post", "counterfactual_delete_post"]
POLARITIES = ["increase", "decrease"]
ROWS_PER_MODEL = 192 * 5          # items x conditions
BANDS = [(-10**9, 0), (0, 10), (10, 20), (20, 30), (30, 40), (40, 10**9)]


def sgn(x: float, polarity: str) -> float:
    """Frozen polarity multiplier: +1 increase claim, -1 decrease claim."""
    return x if polarity == "increase" else -x


def mean(xs):
    xs = list(xs)
    return sum(xs) / len(xs) if xs else float("nan")


def table(header_cells, rows):
    """GitHub markdown table: header, separator, then row lists."""
    sep = ["---"] * len(header_cells)
    lines = ["| " + " | ".join(header_cells) + " |",
             "|" + "|".join(sep) + "|"]
    lines += ["| " + " | ".join(r) + " |" for r in rows]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", nargs="+", required=True)
    ap.add_argument("--items", required=True)
    ap.add_argument("--out-prefix", required=True)
    args = ap.parse_args()

    # ---- items: polarity + group membership --------------------------------
    items = {}
    for line in open(args.items, encoding="utf-8"):
        it = json.loads(line)
        items[it["item_id"]] = it
    assert len(items) == 192, len(items)
    polar = {i: it["critical_direction"] for i, it in items.items()}
    group = {i: it["meta"]["group_sha"] for i, it in items.items()}
    groups = defaultdict(list)
    for iid, g in group.items():
        groups[g].append(iid)
    assert len(groups) == 96
    for g, ids in groups.items():
        assert sorted(polar[i] for i in ids) == ["decrease", "increase"], g

    # ---- integrity: this is the ONLY hard-stop category ---------------------
    integrity = {"rows_total": 0, "value_none": 0, "mass_lt_05": 0,
                 "rationale_truncated": 0, "runs": {}}
    Y = {}            # (model, item_id, kind) -> value
    for path in args.runs:
        tag = os.path.basename(path).split("_")[0]
        rows = [json.loads(l) for l in open(path, encoding="utf-8")]
        integrity["runs"][tag] = len(rows)
        n = len(rows)
        assert n == ROWS_PER_MODEL, f"{tag}: {n} rows != {ROWS_PER_MODEL}"
        seen = set()
        for r in rows:
            key = (r["item_id"], r["kind_name"])
            assert key not in seen, f"{tag}: duplicate {key}"
            seen.add(key)
            assert r["item_id"] in items, f"{tag}: unknown item {r['item_id']}"
            assert r["kind_name"] in COND, f"{tag}: unknown kind {r['kind_name']}"
            assert r["kind"] == "digit", f"{tag}: kind={r['kind']}"
            if r.get("value") is None:
                integrity["value_none"] += 1
                continue
            if (r.get("mass") or 0) < 0.5:
                integrity["mass_lt_05"] += 1
            if r.get("reason_truncated"):
                integrity["rationale_truncated"] += 1
            Y[(tag, r["item_id"], r["kind_name"])] = float(r["value"])
        assert len(seen) == ROWS_PER_MODEL, f"{tag}: {len(seen)} distinct rows"
        integrity["rows_total"] += n
    assert integrity["rows_total"] == 5 * ROWS_PER_MODEL, integrity["rows_total"]
    assert integrity["value_none"] == 0, f"unparsed decisions: {integrity}"
    assert set(t for t, *_ in Y) == set(EXPECTED_MODELS), \
        f"model tags mismatch: {sorted(set(t for t, *_ in Y))}"
    for tag in EXPECTED_MODELS:
        for iid in items:
            for k in COND:
                assert (tag, iid, k) in Y, f"missing cell {tag} {iid} {k}"
    print(f"integrity OK: {integrity['rows_total']} rows (5 x 960), "
          f"0 unparsed, mass<0.5={integrity['mass_lt_05']}, "
          f"truncated={integrity['rationale_truncated']}")

    # ---- per-item frozen quantities ----------------------------------------
    itemq = {}       # (model, item) -> dict with A, C_k, R_k, D_k, polarity, group
    for tag in EXPECTED_MODELS:
        for iid in items:
            p = polar[iid]
            A = sgn(Y[(tag, iid, "admit_post")] - Y[(tag, iid, "base")], p)
            q = {"A": A, "polarity": p, "group": group[iid]}
            for k in KS:
                C = sgn(Y[(tag, iid, k)] - Y[(tag, iid, "admit_post")], p)
                R = sgn(Y[(tag, iid, k)] - Y[(tag, iid, "base")], p)
                D = abs(Y[(tag, iid, k)] - Y[(tag, iid, "base")])
                assert abs(C - (R - A)) < 1e-9, (tag, iid, k)
                q[f"C|{k}"], q[f"R|{k}"], q[f"D|{k}"] = C, R, D
            itemq[(tag, iid)] = q

    def cells(tags, polarity):
        """(model, item) cells for the given scope; polarity None = both."""
        return [(t, i) for t in tags for i in items
                if polarity is None or polar[i] == polarity]

    def agg(cs, key):
        return mean(itemq[c][key] for c in cs)

    def quant(tags, polarity, keybase):
        if keybase == "A":
            return agg(cells(tags, polarity), "A")
        return {k: agg(cells(tags, polarity), f"{keybase}|{k}") for k in KS}

    A_pool = quant(EXPECTED_MODELS, None, "A")
    A_pol = {p: quant(EXPECTED_MODELS, p, "A") for p in POLARITIES}
    A_mod = {m: quant([m], None, "A") for m in EXPECTED_MODELS}
    C_pool = quant(EXPECTED_MODELS, None, "C")
    C_pol = {p: quant(EXPECTED_MODELS, p, "C") for p in POLARITIES}
    C_mod = {m: quant([m], None, "C") for m in EXPECTED_MODELS}
    R_pool = quant(EXPECTED_MODELS, None, "R")
    R_pol = {p: quant(EXPECTED_MODELS, p, "R") for p in POLARITIES}
    R_mod = {m: quant([m], None, "R") for m in EXPECTED_MODELS}
    D_pool = quant(EXPECTED_MODELS, None, "D")
    D_pol = {p: quant(EXPECTED_MODELS, p, "D") for p in POLARITIES}
    D_mod = {m: quant([m], None, "D") for m in EXPECTED_MODELS}

    # ---- trajectories: raw Y means ------------------------------------------
    traj = {}        # scope -> polarity -> kind -> mean Y
    for scope, tags in ([("pooled", EXPECTED_MODELS)]
                        + [(m, [m]) for m in EXPECTED_MODELS]):
        traj[scope] = {}
        for plab in POLARITIES + ["all"]:
            plist = items if plab == "all" else \
                [i for i in items if polar[i] == plab]
            traj[scope][plab] = {
                k: mean(Y[(t, i, k)] for t in tags for i in plist)
                for k in COND}

    # ---- dC_k within pair (group) -------------------------------------------
    dC = {}
    for k in KS:
        per_model = {}
        for m in EXPECTED_MODELS:
            vals = []
            for g in groups:
                ci = [itemq[(m, i)][f"C|{k}"] for i in groups[g]
                      if polar[i] == "increase"][0]
                cd = [itemq[(m, i)][f"C|{k}"] for i in groups[g]
                      if polar[i] == "decrease"][0]
                vals.append(ci - cd)
            per_model[m] = {"mean": mean(vals),
                            "pct_negative": 100.0 * sum(v < 0 for v in vals)
                            / len(vals),
                            "n": len(vals)}
        pooled = [itemq[(m, i)][f"C|{k}"] - itemq[(m, j)][f"C|{k}"]
                  for m in EXPECTED_MODELS for g in groups
                  for i in [x for x in groups[g] if polar[x] == "increase"]
                  for j in [x for x in groups[g] if polar[x] == "decrease"]]
        dC[k] = {"per_model": per_model,
                 "pooled": {"mean": mean(pooled),
                            "pct_negative": 100.0
                            * sum(v < 0 for v in pooled) / len(pooled),
                            "n": len(pooled)}}

    # ---- leverage bands (descriptive only — never a filter) -----------------
    bands = []
    for lo, hi in BANDS:
        sel = [(t, i) for t in EXPECTED_MODELS for i in items
               if lo <= itemq[(t, i)]["A"] < hi]
        if not sel:
            continue
        lab = f"({'-inf' if lo <= -10**9 else lo}, " \
              f"{'inf' if hi >= 10**9 else hi})"
        entry = {"band": lab, "n": len(sel), "mean_A": agg(sel, "A")}
        for k in KS:
            entry[f"C_{k}"] = agg(sel, f"C|{k}")
            entry[f"R_{k}"] = agg(sel, f"R|{k}")
        bands.append(entry)

    # ---- retraction fraction display: C_k / -A (per polarity; display only) --
    frac = {}
    for p in POLARITIES + [None]:
        a = A_pool if p is None else A_pol[p]
        c = C_pool if p is None else C_pol[p]
        frac[p or "all"] = {k: c[k] / -a for k in KS}

    # ---- cells csv -----------------------------------------------------------
    os.makedirs(os.path.dirname(args.out_prefix), exist_ok=True)
    csv_path = args.out_prefix + "_cells.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["model", "item_id", "group_sha", "polarity", "kind", "value"])
        for t in EXPECTED_MODELS:
            for i in items:
                for k in COND:
                    w.writerow([t, i, group[i], polar[i], k, Y[(t, i, k)]])

    # ---- json ----------------------------------------------------------------
    out = {
        "spec": "g24a_competing_accounts_v1.md §4 (frozen pre-run); "
                "s = +1 increase / -1 decrease; no gates, no p-values",
        "integrity": integrity,
        "traj": traj,
        "A": {"pooled": A_pool, "per_polarity": A_pol, "per_model": A_mod},
        "C": {"pooled": C_pool, "per_polarity": C_pol, "per_model": C_mod},
        "R": {"pooled": R_pool, "per_polarity": R_pol, "per_model": R_mod},
        "D": {"pooled": D_pool, "per_polarity": D_pol, "per_model": D_mod},
        "dC": dC,
        "leverage_bands": bands,
        "retraction_fraction": frac,
    }
    with open(args.out_prefix + ".json", "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)

    # ---- markdown (single list literal; every line stays inside brackets) ----
    hdr = ["polarity"] + [KIND_LABEL[k] for k in COND]
    t_traj = table(hdr, [[p] + [f"{traj['pooled'][p][k]:.2f}" for k in COND]
                         for p in POLARITIES + ["all"]])
    t_models_all = table(hdr, [[m] + [f"{traj[m]['all'][k]:.2f}" for k in COND]
                               for m in EXPECTED_MODELS])
    t_models_pol = table(hdr,
                         [[m + " inc"] + [f"{traj[m]['increase'][k]:.2f}"
                                          for k in COND]
                          for m in EXPECTED_MODELS]
                         + [[m + " dec"] + [f"{traj[m]['decrease'][k]:.2f}"
                                            for k in COND]
                            for m in EXPECTED_MODELS])
    t_frozen = table(["quantity"] + [KIND_LABEL[k] for k in KS], [
        ["A (leverage)"] + [f"{A_pool:.2f}"] * len(KS),
        ["C_k"] + [f"{C_pool[k]:.2f}" for k in KS],
        ["R_k"] + [f"{R_pool[k]:.2f}" for k in KS],
        ["D_k"] + [f"{D_pool[k]:.2f}" for k in KS],
        ["C_k / -A (display)"] + [f"{frac['all'][k]:.2f}" for k in KS],
    ])
    t_pol = table(["polarity x k"] + [KIND_LABEL[k] for k in KS],
                  [[f"{p} C_k"] + [f"{C_pol[p][k]:.2f}" for k in KS]
                   for p in POLARITIES]
                  + [[f"{p} R_k"] + [f"{R_pol[p][k]:.2f}" for k in KS]
                     for p in POLARITIES]
                  + [[f"{p} D_k"] + [f"{D_pol[p][k]:.2f}" for k in KS]
                     for p in POLARITIES])
    t_permodel = table(
        ["model", "A"] + [f"C {KIND_LABEL[k]}" for k in KS]
        + [f"R {KIND_LABEL[k]}" for k in KS],
        [[m, f"{A_mod[m]:.2f}"]
         + [f"{C_mod[m][k]:.2f}" for k in KS]
         + [f"{R_mod[m][k]:.2f}" for k in KS]
         for m in EXPECTED_MODELS])
    t_dc = table(["k", "pooled mean", "% negative", "n"] + EXPECTED_MODELS,
                 [[KIND_LABEL[k], f"{dC[k]['pooled']['mean']:.2f}",
                   f"{dC[k]['pooled']['pct_negative']:.1f}%",
                   str(dC[k]["pooled"]["n"])]
                  + [f"{dC[k]['per_model'][m]['mean']:.2f}"
                     for m in EXPECTED_MODELS] for k in KS])
    t_bands = table(["A band", "n", "mean A"]
                    + [f"C/R {KIND_LABEL[k]}" for k in KS],
                    [[b["band"], str(b["n"]), f"{b['mean_A']:.2f}"]
                     + [f"{b[f'C_{k}']:.1f} / {b[f'R_{k}']:.1f}" for k in KS]
                     for b in bands])
    t_frac = table(["polarity"] + [KIND_LABEL[k] for k in KS],
                   [[p] + [f"{frac[p][k]:.2f}" for k in KS]
                    for p in POLARITIES + ["all"]])

    md = "\n".join([
        "# Pilot P1 — retraction-operator discrimination (Layer 2)",
        "",
        "Frozen readout: `g24a_competing_accounts_v1.md` §4 — "
        "A = s(Y_Admit − Y_Base), C_k = s(Y_k − Y_Admit), "
        "R_k = s(Y_k − Y_Base), D_k = |Y_k − Y_Base|; ideal removal "
        "R_k = 0 / C_k = −A; no-effect C_k = 0; s = +1 increase, "
        "−1 decrease.  No gates, no p-values, no bootstrap, no selection "
        "— leverage bands are descriptive only.",
        "",
        "## Integrity",
        "",
        f"- rows: {integrity['rows_total']} (5 models × 960) — expected 4,800",
        f"- unparsed decisions: {integrity['value_none']}",
        f"- digit-mass < 0.5: {integrity['mass_lt_05']}",
        f"- rationale hit token cap: {integrity['rationale_truncated']}",
        "- per model: " + ", ".join(f"{m}={n}"
                                    for m, n in integrity["runs"].items()),
        "- per-item identity C_k = R_k − A asserted on every cell",
        "",
        "## 1. Trajectories — mean Y (0..100), pooled over 5 models",
        "",
        t_traj,
        "",
        "Per model (all):",
        "",
        t_models_all,
        "",
        "Per polarity, per model:",
        "",
        t_models_pol,
        "",
        "## 2. Frozen quantities (pooled over 5 models × 192 claims)",
        "",
        t_frozen,
        "",
        f"A by polarity: increase {A_pol['increase']:.2f}, "
        f"decrease {A_pol['decrease']:.2f}",
        "",
        t_pol,
        "",
        "## 3. Per model — A, C_k, R_k",
        "",
        t_permodel,
        "",
        "## 4. Within-pair dC_k = C_k^inc − C_k^dec",
        "",
        t_dc,
        "",
        "## 5. Leverage bands (descriptive only — nothing filtered)",
        "",
        t_bands,
        "",
        "## 6. P/Q/R/S discriminating quantities (pre-registered reading aids)",
        "",
        "Map: `g24a_competing_accounts_v1.md` §4. Values below are the "
        "frozen quantities each pattern discriminates on:",
        "",
        "- **P** (disregard ≠ act-as-if-unseen): ExcludePost C/−A large, "
        "StrongExclude still large, CounterfactualDelete close to −1 with "
        "decrease-side R near 0 → per k: C/−A and decrease-side R_k.",
        "- **Q** (generic instruction strength): StrongExclude and "
        "CounterfactualDelete improve similarly → gap between their C/−A.",
        "- **R** (contradiction persists / Account A): neither new "
        "operator rescues — C_k ≈ 0 while Y_intervention ≈ Y_Admit on the "
        "decrease side.",
        "- **S** (exclusion semantically misimplemented): "
        "CounterfactualDelete brings both sides to Base while ordinary "
        "exclusion overshoots (C/−A > 1) or sticks (≈ 0).",
        "",
        "Numbers (per polarity, C_k / −A):",
        "",
        t_frac,
        "",
        "Decrease-side R_k (residual vs Base; 0 = ideal return): "
        + ", ".join(f"{KIND_LABEL[k]}={R_pol['decrease'][k]:.2f}" for k in KS),
        "",
        "## 7. Caveats",
        "",
        "- Exploratory discriminator (no KILL gate by ruling); any "
        "item-level statement carries the temp-0 retest caveat "
        "(`g24a_data_quality_audit_v1.md` §E).",
        "- `e3e954d` lineage is discovery-only; this pilot's items are "
        "strict-fresh and validity-reviewed zero-model.",
        "- No rationale coding in this round (deferred by ruling).",
        "",
    ])
    md_path = args.out_prefix + ".md"
    open(md_path, "w", encoding="utf-8").write(md)
    print(f"wrote {md_path}, {args.out_prefix}.json, {csv_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
