#!/usr/bin/env python3
"""G24A §10 mechanical stratum sampling — matched qualitative round.

Exactly as registered in results/discovery/g24a_competing_accounts_v1.md §10
(thresholds fixed there pre-reading; first match wins; no hypothesis-
flattering substitutions):

  Stratum frame per (model, group) cell = the cell's INCREASE-side
  (support) trajectory from results/g24a/g24a_p1_analysis_v1_cells.csv:
    Y0 = value(kind=base), R_k = Y_k - Y0   (increase side: s = +1)
  1. overshoot            — R_CF <= -10
  2. exclude-bad-improved — R_Exc <= -15 AND R_Strong >= R_Exc + 10
                            AND R_CF >= R_Exc + 10
  3. near-base            — |R_CF| <= 5
  (first match wins; cells matching nothing are ineligible)

  4 cells per (model, stratum), fixed-seed sample within stratum
  (all available if <4; shortfalls reported).  3 strata x 4 x 5 models
  = 60 cells expected.

Seed: 20260927 (the project's frozen seed), applied per draw as
Random(f"{seed}:{model}:{stratum}") over candidates sorted by group_sha,
so each draw is independent and reproducible in isolation.

Outputs (zero model output read; rationales are carried verbatim for the
later reading step, not interpreted here):
  data/items/g24a_p1_qual_cells_v1.jsonl   60 sampled cells + full frame
  results/g24a/g24a_p1_qual_review_v1.md    reading material: both claims'
                                            texts, Y trajectories, and all
                                            10 rationales per cell

Usage: python scripts/sample_g24a_p1_qual_cells.py
"""
from __future__ import annotations

import csv
import json
import random
from collections import defaultdict
from pathlib import Path

CELLS_CSV = "results/g24a/g24a_p1_analysis_v1_cells.csv"
ITEMS = "data/items/g24a_p1_v1.jsonl"
RAWS = [f"results/raw/{m}_g24a_p1.jsonl" for m in
        ["mistral-small-24b", "llama31-8b", "gemma3-12b",
         "qwen3-8b", "qwen35-9b"]]
MODELS = ["mistral-small-24b", "llama31-8b", "gemma3-12b",
          "qwen3-8b", "qwen35-9b"]
OUT_CELLS = "data/items/g24a_p1_qual_cells_v1.jsonl"
OUT_REVIEW = "results/g24a/g24a_p1_qual_review_v1.md"
SEED = 20260927
PER_STRATUM = 4
STRATA = ["overshoot", "exclude-bad-improved", "near-base"]
KINDS = ["base", "admit_post", "exclude_post", "strong_exclude_post",
         "counterfactual_delete_post"]
KIND_LABEL = {"base": "Base", "admit_post": "AdmitPost",
              "exclude_post": "ExcludePost",
              "strong_exclude_post": "StrongExcludePost",
              "counterfactual_delete_post": "CounterfactualDeletePost"}


def stratum_of(r_exc, r_strong, r_cf):
    """First-match-wins exactly as §10 lists them."""
    if r_cf <= -10:
        return "overshoot"
    if r_exc <= -15 and r_strong >= r_exc + 10 and r_cf >= r_exc + 10:
        return "exclude-bad-improved"
    if abs(r_cf) <= 5:
        return "near-base"
    return None


def main() -> None:
    # ---- frame from the P1 cells csv ---------------------------------------
    Y = defaultdict(dict)          # (model, item_id, kind) -> value
    pol = {}                       # item_id -> polarity
    grp = {}                       # item_id -> group_sha
    for r in csv.DictReader(open(CELLS_CSV, encoding="utf-8")):
        Y[(r["model"], r["item_id"], r["kind"])] = float(r["value"])
        pol[r["item_id"]] = r["polarity"]
        grp[r["item_id"]] = r["group_sha"]
    assert len(Y) == 4800, len(Y)

    # (group, polarity) -> exactly one item; (model, group) -> 2 items
    group_items = defaultdict(dict)
    for iid in pol:
        group_items[grp[iid]][pol[iid]] = iid
    assert len(group_items) == 96, len(group_items)
    assert all(set(v) == {"increase", "decrease"} for v in group_items.values())

    frame = defaultdict(list)     # (model, stratum) -> [group_sha]
    cell_q = {}                   # (model, group) -> stratum quantities
    ineligible = 0
    for m in MODELS:
        for g in sorted(group_items):
            inc = group_items[g]["increase"]
            y0 = Y[(m, inc, "base")]
            r_exc = Y[(m, inc, "exclude_post")] - y0
            r_str = Y[(m, inc, "strong_exclude_post")] - y0
            r_cf = Y[(m, inc, "counterfactual_delete_post")] - y0
            s = stratum_of(r_exc, r_str, r_cf)
            cell_q[(m, g)] = {"Y0": y0, "R_exc": r_exc, "R_strong": r_str,
                              "R_cf": r_cf, "stratum": s}
            if s is None:
                ineligible += 1
            else:
                frame[(m, s)].append(g)

    # ---- fixed-seed sampling -----------------------------------------------
    sampled, shortfalls = [], []
    for m in MODELS:
        for s in STRATA:
            cands = sorted(frame[(m, s)])
            rng = random.Random(f"{SEED}:{m}:{s}")
            k = min(PER_STRATUM, len(cands))
            pick = sorted(rng.sample(cands, k)) if k else []
            if len(cands) < PER_STRATUM:
                shortfalls.append({"model": m, "stratum": s,
                                   "available": len(cands),
                                   "picked": len(pick)})
            for g in pick:
                sampled.append({
                    "model": m, "stratum": s, "group_sha": g,
                    **cell_q[(m, g)],
                    "items": {"increase": group_items[g]["increase"],
                              "decrease": group_items[g]["decrease"]},
                    "seed": SEED})

    assert len({(c["model"], c["group_sha"]) for c in sampled}) == len(sampled)
    if len(sampled) != 60:
        print(f"NOTE: {len(sampled)} cells (expected 60); shortfalls below")

    # ---- rationales from the P1 raws ---------------------------------------
    R = {}                        # (model, item_id, kind) -> (reasoning, trunc)
    for path in RAWS:
        tag = Path(path).name.split("_")[0]
        for line in open(path, encoding="utf-8"):
            r = json.loads(line)
            R[(tag, r["item_id"], r["kind_name"])] = (
                r.get("reasoning", ""), bool(r.get("reason_truncated")))
    assert len(R) == 4800, len(R)

    # ---- items: claim texts --------------------------------------------------
    items = {}
    for line in open(ITEMS, encoding="utf-8"):
        it = json.loads(line)
        items[it["item_id"]] = it

    # ---- write cells jsonl ----------------------------------------------------
    Path(OUT_CELLS).parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_CELLS, "w", encoding="utf-8") as fh:
        for c in sampled:
            c["Y"] = {iid: {k: Y[(c["model"], iid, k)] for k in KINDS}
                      for iid in c["items"].values()}
            fh.write(json.dumps(c, ensure_ascii=False) + "\n")

    # ---- write review md ------------------------------------------------------
    lines = ["# G24A §10 matched qualitative round — reading material", "",
             "Mechanical sample: 4 cells / (model x stratum), strata on the "
             "increase-side trajectory per prereg §10 (first match wins; "
             "thresholds frozen pre-reading), seed "
             f"{SEED} per (model, stratum) draw over group_sha order. "
             "Behavioral labels only — NOT mechanisms; label vocabulary: "
             "`still_uses_evidence`, `no_evidence=>uncertain`, "
             "`no_evidence=>claim_less_likely`, `exclusion_implies_distrust`, "
             "`reconstructs_prior/world_knowledge`, `other`.", "",
             f"- frame: {480 - ineligible} of 480 (model,group) cells match "
             f"a stratum; {ineligible} ineligible",
             f"- sampled: {len(sampled)} cells "
             f"({PER_STRATUM}/stratum/model, shortfalls: {shortfalls or 'none'})",
             "- per cell: both claims' texts, both claims' Y trajectories, "
             "and all 10 rationales (read at Base / Admit / Exclude / Strong "
             "/ CF for each claim)", ""]
    for m in MODELS:
        lines += [f"## {m}", ""]
        for s in STRATA:
            cells = [c for c in sampled
                     if c["model"] == m and c["stratum"] == s]
            lines += [f"### stratum: {s} ({len(cells)} cells)", ""]
            for c in cells:
                g = c["group_sha"]
                lines += [f"#### cell {g} — {s} "
                          f"(increase-side R: Exc {c['R_exc']:.1f}, "
                          f"Strong {c['R_strong']:.1f}, CF {c['R_cf']:.1f}; "
                          f"Y0 {c['Y0']:.1f})", ""]
                for pol_lab in ("increase", "decrease"):
                    iid = c["items"][pol_lab]
                    it = items[iid]
                    lines += [f"**{pol_lab} claim** `{iid}`: "
                              f"{it['base_context']}", ""]
                    ys = " | ".join(f"{KIND_LABEL[k]} {Y[(m, iid, k)]:.1f}"
                                    for k in KINDS)
                    lines += [f"Y: {ys}", ""]
                    for k in KINDS:
                        txt, trunc = R[(m, iid, k)]
                        mark = " *(truncated)*" if trunc else ""
                        lines += [f"- **{KIND_LABEL[k]}**{mark}: {txt.strip()}",
                                  ""]
                lines += ["---", ""]
    Path(OUT_REVIEW).write_text("\n".join(lines), encoding="utf-8")

    n_rat = len(sampled) * 10
    print(f"wrote {OUT_CELLS}: {len(sampled)} cells")
    print(f"wrote {OUT_REVIEW}: {n_rat} rationales "
          f"({len(sampled)} cells x 10 readings)")
    for m in MODELS:
        print("  " + m + ": " + ", ".join(
            f"{s}={len([c for c in sampled if c['model'] == m and c['stratum'] == s])}"
            for s in STRATA))
    print(f"frame size per stratum: " + ", ".join(
        f"{s}={sum(len(frame[(m, s)]) for m in MODELS)}" for s in STRATA))
    if shortfalls:
        print(f"shortfalls: {shortfalls}")


if __name__ == "__main__":
    main()
