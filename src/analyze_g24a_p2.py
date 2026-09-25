"""Pilot P2 analysis — same-claim counterfactual reconstruction (Layer 2).

Readout is EXACTLY the frozen §9 of results/discovery/g24a_competing_accounts_v1.md
(spec frozen pre-run):

    evidence polarity e: +1 = arm+ (E_support), -1 = arm- (E_refute),
    shared Y0 = the single evidence-free Base row per (claim, model)
    (renders byte-identical for both arms - verified pre-run)

    A_e   = e * (Y_admit,e  - Y0)   leverage (displayed continuous,
                                    never filtered - the old "both
                                    directions A>=10" gate is dead)
    R_k,e = e * (Y_k,e      - Y0)   polarity-aligned residual
    C_k,e = e * (Y_k,e      - Y_admit,e)  intervention effect
    D_k,e = |Y_k,e - Y0|            distance from pre-evidence Base
    ideal deletion: R_k,+ = R_k,- = 0 (and gap R_k,+ - R_k,- = 0)
    per-cell identity C_k,e = R_k,e - A_e (exact; asserted everywhere)

Reading aids (sign): aligned A < 0 = evidence moved against its own
direction; aligned R < 0 = over-correction past Base (in BOTH arms: after
support retraction Y below Y0, after refute retraction Y above Y0); raw
(unaligned) means are reported alongside so the pooled cancellation view
is visible.

Y is the temp-0 digit-expectation decision value (0..100).  Aggregation is
a plain mean over the balanced design (5 models x 200 claims x 2 arms).
NO p-values, NO bootstrap, NO gates, NO selection: A is displayed as a
continuous variable only and leverage bands are descriptive.

Outputs:
    <out-prefix>.md    human report
    <out-prefix>.json  all numbers + integrity block
    <out-prefix>_cells.csv  model,p2_id,item_id,arm,kind,value

Usage:
    python src/analyze_g24a_p2.py \
        --runs results/raw/mistral-small-24b_g24a_p2_plus.jsonl \
               results/raw/mistral-small-24b_g24a_p2_minus.jsonl ... \
        --items data/items/g24a_p2_v1.jsonl \
        --out-prefix results/g24a/g24a_p2_analysis_v1
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
COND_PLUS = ["base", "admit_post", "exclude_post", "strong_exclude_post",
             "counterfactual_delete_post"]
COND_MINUS = COND_PLUS[1:]
ARMS = ["plus", "minus"]
E = {"plus": 1, "minus": -1}          # evidence polarity e
ARM_LABEL = {"plus": "arm+ (support)", "minus": "arm- (refute)"}
KIND_LABEL = {"base": "Base", "admit_post": "AdmitPost",
              "exclude_post": "ExcludePost",
              "strong_exclude_post": "StrongExcludePost",
              "counterfactual_delete_post": "CounterfactualDeletePost"}
KS = ["exclude_post", "strong_exclude_post", "counterfactual_delete_post"]
N_CLAIMS, N_MODELS = 200, 5
ROWS_PER_MODEL = N_CLAIMS * 9          # 1,000 plus + 800 minus
BANDS = [(-10**9, 0), (0, 10), (10, 20), (20, 30), (30, 40), (40, 10**9)]


def mean(xs):
    xs = list(xs)
    return sum(xs) / len(xs) if xs else float("nan")


def table(header_cells, rows):
    sep = ["---"] * len(header_cells)
    lines = ["| " + " | ".join(header_cells) + " |",
             "|" + "|".join(sep) + "|"]
    lines += ["| " + " | ".join(r) + " |" for r in rows]
    return "\n".join(lines)


def jsonable(o):
    """Recursively stringify tuple keys ((k, e) -> \"k|e\") for json.dump."""
    if isinstance(o, dict):
        return {("|".join(map(str, k)) if isinstance(k, tuple) else k): jsonable(v)
                for k, v in o.items()}
    if isinstance(o, list):
        return [jsonable(x) for x in o]
    return o


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", nargs="+", required=True,
                    help="10 files: <tag>_g24a_p2_plus.jsonl + _minus.jsonl "
                         "x 5 models")
    ap.add_argument("--items", required=True)
    ap.add_argument("--out-prefix", required=True)
    args = ap.parse_args()

    # ---- items: arms, claim keys, shared-block assertion ---------------------
    items = {}
    for line in open(args.items, encoding="utf-8"):
        it = json.loads(line)
        items[it["item_id"]] = it
    assert len(items) == N_CLAIMS * 2, len(items)
    claims = defaultdict(dict)                  # p2_id -> arm -> item dict
    for iid, it in items.items():
        arm = it["meta"]["arm"]
        assert arm in ARMS and it["task_family"] == "g24a_vitaminc", iid
        assert arm not in claims[it["meta"]["p2_id"]], f"duplicate arm {iid}"
        claims[it["meta"]["p2_id"]][arm] = it
    assert len(claims) == N_CLAIMS, len(claims)
    for p2_id, arms in claims.items():
        assert set(arms) == set(ARMS), p2_id
        # shared Y0 structural guarantee: identical claim/question/rules
        pm, mm = arms["plus"], arms["minus"]
        assert pm["base_context"] == mm["base_context"], p2_id
        assert pm["question"] == mm["question"], p2_id
        assert pm["output_spec"] == mm["output_spec"], p2_id
        assert pm["admit_rule"] == mm["admit_rule"], p2_id
        assert pm["exclude_rule"] == mm["exclude_rule"], p2_id
        assert pm["critical_evidence"] != mm["critical_evidence"], p2_id

    # ---- integrity: this is the ONLY hard-stop category ----------------------
    integrity = {"rows_total": 0, "value_none": 0, "mass_lt_05": 0,
                 "rationale_truncated": 0, "runs": {}}
    Y = {}            # (model, item_id, kind) -> value
    for path in args.runs:
        base = os.path.basename(path)
        assert base.endswith("_g24a_p2_plus.jsonl") or \
            base.endswith("_g24a_p2_minus.jsonl"), base
        tag, arm = base.split("_g24a_p2_")[0], \
            base.split("_g24a_p2_")[1].removesuffix(".jsonl")
        assert arm in ARMS, (base, arm)
        rows = [json.loads(l) for l in open(path, encoding="utf-8")]
        integrity["runs"][f"{tag}/{arm}"] = len(rows)
        want_rows = N_CLAIMS * (len(COND_PLUS) if arm == "plus"
                                else len(COND_MINUS))
        n = len(rows)
        assert n == want_rows, f"{tag}/{arm}: {n} rows != {want_rows}"
        kinds = COND_PLUS if arm == "plus" else COND_MINUS
        assert "base" not in kinds or arm == "plus"
        seen = set()
        for r in rows:
            key = (r["item_id"], r["kind_name"])
            assert key not in seen, f"{tag}: duplicate {key}"
            seen.add(key)
            assert r["item_id"] in items, f"{tag}: unknown item {r['item_id']}"
            assert items[r["item_id"]]["meta"]["arm"] == arm, \
                (tag, r["item_id"], arm)
            assert r["kind_name"] in kinds, f"{tag}: unknown kind {r['kind_name']}"
            assert r["kind"] == "digit", f"{tag}: kind={r['kind']}"
            assert r["model_tag"] == tag, (tag, r["model_tag"])
            if r.get("value") is None:
                integrity["value_none"] += 1
                continue
            if (r.get("mass") or 0) < 0.5:
                integrity["mass_lt_05"] += 1
            if r.get("reason_truncated"):
                integrity["rationale_truncated"] += 1
            Y[(tag, r["item_id"], r["kind_name"])] = float(r["value"])
        want_grid = {(iid, k) for iid, it in items.items()
                     if it["meta"]["arm"] == arm for k in kinds}
        assert seen == want_grid, (tag, arm, len(seen), len(want_grid))
        integrity["rows_total"] += n
    assert integrity["rows_total"] == N_MODELS * ROWS_PER_MODEL, \
        integrity["rows_total"]
    assert integrity["value_none"] == 0, f"unparsed decisions: {integrity}"
    assert set(t for t, *_ in Y) == set(EXPECTED_MODELS), \
        f"model tags mismatch: {sorted(set(t for t, *_ in Y))}"
    # full grid: every (model, item, kind) exists; base exists ONLY on arm+
    for tag in EXPECTED_MODELS:
        for iid, it in items.items():
            kinds = COND_PLUS if it["meta"]["arm"] == "plus" else COND_MINUS
            for k in kinds:
                assert (tag, iid, k) in Y, f"missing cell {tag} {iid} {k}"
            assert (tag, iid, "base") not in Y or it["meta"]["arm"] == "plus", \
                f"base row on arm-: {tag} {iid}"
    print(f"integrity OK: {integrity['rows_total']} rows (5 x 1800 = 9000), "
          f"0 unparsed, mass<0.5={integrity['mass_lt_05']}, "
          f"truncated={integrity['rationale_truncated']}")

    # ---- shared Y0: one base row per (claim, model), used by BOTH arms -------
    Y0 = {}            # (model, p2_id) -> base value
    for tag in EXPECTED_MODELS:
        for p2_id, arms in claims.items():
            Y0[(tag, p2_id)] = Y[(tag, arms["plus"]["item_id"], "base")]

    # ---- per-cell frozen quantities ------------------------------------------
    # cellq[(model, p2_id)] -> A[e], R[k|e], C[k|e], D[k|e], raw A/R
    cellq = {}
    for tag in EXPECTED_MODELS:
        for p2_id, arms in claims.items():
            y0 = Y0[(tag, p2_id)]
            q = {"A": {}, "A_raw": {}, "R": {}, "R_raw": {}, "C": {}, "D": {}}
            for e_label in ARMS:
                e = E[e_label]
                y_adm = Y[(tag, arms[e_label]["item_id"], "admit_post")]
                q["A"][e_label] = e * (y_adm - y0)
                q["A_raw"][e_label] = y_adm - y0
                for k in KS:
                    y_k = Y[(tag, arms[e_label]["item_id"], k)]
                    R = e * (y_k - y0)
                    C = e * (y_k - y_adm)
                    assert abs(C - (R - q["A"][e_label])) < 1e-9, \
                        (tag, p2_id, e_label, k)
                    q["R"][(k, e_label)] = R
                    q["R_raw"][(k, e_label)] = y_k - y0
                    q["C"][(k, e_label)] = C
                    q["D"][(k, e_label)] = abs(y_k - y0)
            cellq[(tag, p2_id)] = q

    def agg(cs, getter):
        return mean(getter(cellq[c]) for c in cs)

    all_cells = [(t, c) for t in EXPECTED_MODELS for c in claims]
    model_cells = {m: [(m, c) for c in claims] for m in EXPECTED_MODELS}

    # pooled + per-model + per-arm
    A = {"pooled": {e: mean(cellq[c]["A"][e] for c in all_cells)
                    for e in ARMS},
         "per_model": {m: {e: mean(cellq[c]["A"][e] for c in model_cells[m])
                           for e in ARMS}
                       for m in EXPECTED_MODELS},
         "raw_pooled": {e: mean(cellq[c]["A_raw"][e] for c in all_cells)
                        for e in ARMS}}
    R = {b: {} for b in ("pooled", "per_model")}
    R["pooled"] = {(k, e): mean(cellq[c]["R"][(k, e)] for c in all_cells)
                   for k in KS for e in ARMS}
    R["per_model"] = {m: {(k, e): mean(cellq[c]["R"][(k, e)]
                                       for c in model_cells[m])
                          for k in KS for e in ARMS}
                      for m in EXPECTED_MODELS}
    R_raw_pooled = {(k, e): mean(cellq[c]["R_raw"][(k, e)] for c in all_cells)
                    for k in KS for e in ARMS}
    D_pooled = {(k, e): mean(cellq[c]["D"][(k, e)] for c in all_cells)
                for k in KS for e in ARMS}
    C_pooled = {(k, e): mean(cellq[c]["C"][(k, e)] for c in all_cells)
                for k in KS for e in ARMS}
    C_per_model = {m: {(k, e): mean(cellq[c]["C"][(k, e)]
                                    for c in model_cells[m])
                       for k in KS for e in ARMS}
                   for m in EXPECTED_MODELS}

    # between-polarity gap (ideal deletion: 0)
    gap = {k: {"R_plus_minus_R_minus":
               R["pooled"][(k, "plus")] - R["pooled"][(k, "minus")]}
           for k in KS}

    # direction counts (descriptive; never filtered)
    counts = {"A_negative": {e: sum(1 for c in all_cells
                                    if cellq[c]["A"][e] < 0) for e in ARMS},
              "A_cells": len(all_cells),
              "R_negative": {(k, e): sum(1 for c in all_cells
                                         if cellq[c]["R"][(k, e)] < 0)
                             for k in KS for e in ARMS}}
    # raw (unaligned) means: the pooled cancellation view
    raw_all = {"R": {k: mean(mean(cellq[c]["R_raw"][(k, e)] for e in ARMS)
                             for c in all_cells) for k in KS},
               "R_arm": {(k, e): R_raw_pooled[(k, e)] for k in KS
                         for e in ARMS}}

    # trajectories: raw mean Y per kind per arm (pooled + per model)
    traj = {}
    for scope, tags in ([("pooled", EXPECTED_MODELS)]
                        + [(m, [m]) for m in EXPECTED_MODELS]):
        traj[scope] = {}
        for e in ARMS:
            kinds = COND_PLUS if e == "plus" else COND_MINUS
            traj[scope][e] = {
                "base": mean(Y0[(t, c)] for t in tags for c in claims),
                **{k: mean(Y[(t, claims[c][e]["item_id"], k)]
                           for t in tags for c in claims) for k in kinds}}

    # leverage bands on aligned A (descriptive only - never a filter)
    bands = []
    for lo, hi in BANDS:
        entry = {"band": f"({'-inf' if lo <= -10**9 else lo}, "
                         f"{'inf' if hi >= 10**9 else hi})"}
        keep = False
        for e in ARMS:
            sel = [c for c in all_cells if lo <= cellq[c]["A"][e] < hi]
            entry[f"n_{e}"] = len(sel)
            entry[f"meanA_{e}"] = mean(cellq[c]["A"][e] for c in sel)
            for k in KS:
                entry[f"R_{k}_{e}"] = mean(cellq[c]["R"][(k, e)] for c in sel)
            keep = keep or bool(sel)
        if keep:
            bands.append(entry)

    # retraction fraction display: C_k,e / -A_e (per arm)
    frac = {e: {k: C_pooled[(k, e)] / -A["pooled"][e] if A["pooled"][e] != 0
                else float("nan") for k in KS} for e in ARMS}

    # ---- cells csv -----------------------------------------------------------
    os.makedirs(os.path.dirname(args.out_prefix), exist_ok=True)
    csv_path = args.out_prefix + "_cells.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["model", "p2_id", "item_id", "arm", "kind", "value"])
        for t in EXPECTED_MODELS:
            for c in sorted(claims):
                # exactly one base row per (model, claim), on the plus side
                # (the plus kind loop below writes it; arm- has no base)
                for e in ARMS:
                    for k in (COND_PLUS if e == "plus" else COND_MINUS):
                        w.writerow([t, c, claims[c][e]["item_id"], e, k,
                                    Y[(t, claims[c][e]["item_id"], k)]])

    # ---- json ----------------------------------------------------------------
    out = {
        "spec": "g24a_competing_accounts_v1.md §9 (frozen pre-run); "
                "e = +1 support / -1 refute; A_e = e(Y_admit,e - Y0), "
                "R_k,e = e(Y_k,e - Y0); ideal R = 0; A continuous, "
                "never filtered; no gates, no p-values, no selection",
        "integrity": integrity,
        "traj": traj,
        "A": A, "R": R, "C": {"pooled": C_pooled, "per_model": C_per_model},
        "D_pooled": D_pooled,
        "R_raw_pooled": R_raw_pooled,
        "raw_pooled_unaligned": raw_all,
        "gap_R_plus_minus_minus": gap,
        "counts": counts,
        "retraction_fraction": frac,
        "leverage_bands": bands,
    }
    with open(args.out_prefix + ".json", "w", encoding="utf-8") as fh:
        json.dump(jsonable(out), fh, indent=1)

    # ---- markdown ------------------------------------------------------------
    t_traj = table(["arm"] + [KIND_LABEL[k] for k in COND_PLUS],
                   [[ARM_LABEL[e]]
                    + [f"{traj['pooled'][e][k]:.2f}"
                       if k in traj["pooled"][e] else "-"
                       for k in COND_PLUS] for e in ARMS])
    t_models = table(["model", "arm"] + [KIND_LABEL[k] for k in COND_PLUS],
                     [[m, ARM_LABEL[e]]
                      + [f"{traj[m][e][k]:.2f}"
                         if k in traj[m][e] else "-" for k in COND_PLUS]
                      for m in EXPECTED_MODELS for e in ARMS])
    t_A = table(["quantity"] + [ARM_LABEL[e] for e in ARMS], [
        ["A_e (aligned)"] + [f"{A['pooled'][e]:.2f}" for e in ARMS],
        ["A_e raw (Y_admit - Y0)"] + [f"{A['raw_pooled'][e]:.2f}"
                                      for e in ARMS],
        ["cells with aligned A < 0"]
        + [f"{counts['A_negative'][e]} / {counts['A_cells']}"
           for e in ARMS],
    ])
    t_R = table(["k"] + [f"{ARM_LABEL[e]}" for e in ARMS]
                + ["gap R+ - R-", "C_k", "D_k", "C/-A"], [
                    [KIND_LABEL[k]]
                    + [f"{R['pooled'][(k, e)]:.2f}" for e in ARMS]
                    + [f"{gap[k]['R_plus_minus_R_minus']:.2f}",
                       f"{C_pooled[(k, 'plus')]:.2f} / "
                       f"{C_pooled[(k, 'minus')]:.2f}",
                       f"{D_pooled[(k, 'plus')]:.2f} / "
                       f"{D_pooled[(k, 'minus')]:.2f}",
                       f"{frac['plus'][k]:.2f} / {frac['minus'][k]:.2f}"]
                    for k in KS])
    t_raw = table(["quantity (unaligned mean)"] + [KIND_LABEL[k] for k in KS],
                  [["R+ raw (support arm)"]
                   + [f"{raw_all['R_arm'][(k, 'plus')]:.2f}" for k in KS],
                   ["R− raw (refute arm)"]
                   + [f"{raw_all['R_arm'][(k, 'minus')]:.2f}" for k in KS],
                   ["R raw (both arms pooled)"]
                   + [f"{raw_all['R'][k]:.2f}" for k in KS]])
    t_counts = table(["cell class (aligned)"] + [ARM_LABEL[e] for e in ARMS],
                     [[f"{KIND_LABEL[k]}: R < 0 (over-correction past Base)"]
                      + [f"{counts['R_negative'][(k, e)]} / 1000"
                         for e in ARMS] for k in KS])
    t_permodel = table(
        ["model"] + [f"A {ARM_LABEL[e]}" for e in ARMS]
        + [f"R {KIND_LABEL[k]} ({ARM_LABEL['plus']})" for k in KS]
        + [f"R {KIND_LABEL[k]} ({ARM_LABEL['minus']})" for k in KS],
        [[m] + [f"{A['per_model'][m][e]:.2f}" for e in ARMS]
         + [f"{R['per_model'][m][(k, 'plus')]:.2f}" for k in KS]
         + [f"{R['per_model'][m][(k, 'minus')]:.2f}" for k in KS]
         for m in EXPECTED_MODELS])
    t_bands = table(["A band (aligned)", "n+ / n-", "mean A+ / A-"]
                    + [f"R+ / R- {KIND_LABEL[k]}" for k in KS],
                    [[b["band"],
                      f"{b['n_plus']} / {b['n_minus']}",
                      f"{b['meanA_plus']:.1f} / {b['meanA_minus']:.1f}"]
                     + [f"{b[f'R_{k}_plus']:.1f} / {b[f'R_{k}_minus']:.1f}"
                        if b[f"n_plus"] or b[f"n_minus"] else "-"
                        for k in KS] for b in bands])

    md = "\n".join([
        "# Pilot P2 — same-claim counterfactual reconstruction (Layer 2)",
        "",
        "Frozen readout: `g24a_competing_accounts_v1.md` §9 — "
        "e = +1 arm+ (E_support) / −1 arm− (E_refute); "
        "A_e = e(Y_Admit,e − Y0), R_k,e = e(Y_k,e − Y0), "
        "C_k,e = e(Y_k,e − Y_Admit,e), D_k,e = |Y_k,e − Y0|; "
        "ideal deletion R_k,+ = R_k,− = 0 (gap = 0).  Y0 is a single "
        "evidence-free Base row per (claim, model) — byte-identical prompt "
        "for both arms, shared by construction.  A is continuous, never "
        "filtered; no gates, no p-values, no bootstrap, no selection.",
        "",
        "Sign reading: aligned A < 0 = evidence moved against its own "
        "direction; aligned R < 0 = over-correction past Base (support "
        "retraction leaves Y < Y0; refute retraction leaves Y > Y0).",
        "",
        "## Integrity",
        "",
        f"- rows: {integrity['rows_total']} (5 models × 1,800) — "
        "expected 9,000",
        f"- unparsed decisions: {integrity['value_none']}",
        f"- digit-mass < 0.5: {integrity['mass_lt_05']}",
        f"- rationale hit token cap: {integrity['rationale_truncated']}",
        "- per file: " + ", ".join(f"{k}={n}"
                                   for k, n in integrity["runs"].items()),
        "- per-cell identity C = R − A asserted on every cell",
        "- shared-Y0: exactly one Base row per (claim, model), arm− file "
        "contains no base rows (asserted)",
        "",
        "## 1. Trajectories — mean Y (0..100), pooled over 5 models × 200 claims",
        "",
        t_traj,
        "",
        "Per model × arm:",
        "",
        t_models,
        "",
        "## 2. Leverage A_e (pooled, continuous — nothing filtered)",
        "",
        t_A,
        "",
        "## 3. Residuals R_k,e (pooled; ideal = 0, gap = 0)",
        "",
        t_R,
        "",
        "Unaligned (raw) means — the pooled cancellation view:",
        "",
        t_raw,
        "",
        "## 4. Over-correction cell counts (descriptive, /1000 cells per "
        "(k, arm))",
        "",
        t_counts,
        "",
        "## 5. Per model — A and R",
        "",
        t_permodel,
        "",
        "## 6. Leverage bands on aligned A (descriptive only — nothing "
        "filtered)",
        "",
        t_bands,
        "",
        "## 7. Reading aid (both outcomes informative — §9)",
        "",
        "(a) if the same-claim asymmetry persists (|gap| large relative to "
        "|A|), evidence polarity itself affects reversibility; "
        "(b) if it largely disappears, P1/G24A's asymmetry was mainly "
        "claim prior/form (Account B), not evidence polarity.  Numbers: "
        + ", ".join(f"{KIND_LABEL[k]} gap={gap[k]['R_plus_minus_R_minus']:.2f}"
                    for k in KS)
        + ".",
        "",
        "## 8. Caveats",
        "",
        "- Temp-0 retest caveat carries over "
        "(`g24a_data_quality_audit_v1.md` §E).",
        "- Zero-model validity review applied pre-run (44/200 replacements "
        "from frozen reserve order); no model-conditioned selection.",
        "- P1/P2 outcome maps are separate; P1's frozen map is untouched.",
        "- No rationale coding in this round (60-cell §10 reading is a "
        "separate P1-based step).",
        "",
    ])
    md_path = args.out_prefix + ".md"
    open(md_path, "w", encoding="utf-8").write(md)
    print(f"wrote {md_path}, {args.out_prefix}.json, {csv_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
