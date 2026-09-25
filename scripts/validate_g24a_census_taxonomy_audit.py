#!/usr/bin/env python3
"""Canonical validator + agreement analysis for the G24A fresh-pair census
blind taxonomy audit (Layer-2, zero compute).

The audit design:
  * sample: 120 of the 1,582 fresh groups, seed 20260925, stratified
    100 fever + 20 scifact (manifest: *_taxaudit_sample.csv, carries the
    auto labels for scoring AFTER coding)
  * 3 blind coders (local agents), one batch file each (*_taxaudit_batchN.md)
    containing evidence + all claims and NO auto labels
  * coder outputs: *_taxaudit_batchN.jsonl, 40 lines each, batch order

Checks (all must pass; exit 1 otherwise):
  1. manifest: 120 unique shas, every sha present in groups.csv, manifest
     auto_type/negation_present equal groups.csv (manifest is derived data)
  2. each batch md: 40 `## sha=` headers; jsonl has exactly 40 lines in the
     same order as the md
  3. jsonl records: keys exactly {group_sha,type,negation_present,note},
     type within the 5-label set, negation_present in {yes,no}
  4. union of coded shas == manifest sha set (no dupes, no misses)
  5. every coded sha is a fresh-group sha (membership in groups.csv)

Agreement (auto rules vs blind coders): 5-way exact agreement overall and
per source, full confusion matrix, negation-flag binary agreement,
population-weighted blind proportions (fever weight 1515/100, scifact
67/20) and unweighted sample proportions.

Writes: results/discovery/g24a_fresh_pair_census_v1_taxaudit_summary.json
Exit 0 = valid.

Usage: python scripts/validate_g24a_census_taxonomy_audit.py
"""
from __future__ import annotations

import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

PFX = "results/discovery/g24a_fresh_pair_census_v1"
TYPES = ["explicit_negation", "antonym_opposite", "exclusive_alternative",
         "numeric_value", "indirect_contradiction"]
SAMPLES = {"fever": 100, "scifact": 20}   # stratum sizes, seed 20260925


def fail(msg: str) -> int:
    print(f"INVALID: {msg}", file=sys.stderr)
    return 1


def main() -> int:
    groups = {}
    with open(PFX + "_groups.csv", newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            groups[r["group_sha"]] = r
    if len(groups) != 1582:
        return fail(f"groups.csv has {len(groups)} rows, expected 1582")

    # 1. manifest
    with open(PFX + "_taxaudit_sample.csv", newline="", encoding="utf-8") as fh:
        man = list(csv.DictReader(fh))
    if len(man) != 120:
        return fail(f"manifest has {len(man)} rows, expected 120")
    man_sha = [r["group_sha"] for r in man]
    if len(set(man_sha)) != 120:
        return fail("manifest shas not unique")
    for r in man:
        g = groups.get(r["group_sha"])
        if g is None:
            return fail(f"manifest sha {r['group_sha']} not in groups.csv")
        if r["auto_type"] != g["auto_type"] or r["n_inc"] != g["n_inc"] \
                or r["n_dec"] != g["n_dec"] or r["source"] != g["source"]:
            return fail(f"manifest row {r['group_sha']} != groups.csv")
    strata = Counter(r["source"] for r in man)
    if dict(strata) != SAMPLES:
        return fail(f"strata {dict(strata)} != expected {SAMPLES}")

    # 2+3. batches
    coded = []
    for bi in (1, 2, 3):
        md = Path(f"{PFX}_taxaudit_batch{bi}.md").read_text(encoding="utf-8")
        hdrs = [ln.split("## sha=")[1].split()[0]
                for ln in md.splitlines() if ln.startswith("## sha=")]
        if len(hdrs) != 40:
            return fail(f"batch{bi} md has {len(hdrs)} headers, expected 40")
        lines = Path(f"{PFX}_taxaudit_batch{bi}.jsonl").read_text(
            encoding="utf-8").strip().splitlines()
        if len(lines) != 40:
            return fail(f"batch{bi} jsonl has {len(lines)} lines, expected 40")
        for i, ln in enumerate(lines):
            try:
                rec = json.loads(ln)
            except json.JSONDecodeError as e:
                return fail(f"batch{bi} line {i + 1}: bad JSON: {e}")
            if set(rec) != {"group_sha", "type", "negation_present", "note"}:
                return fail(f"batch{bi} line {i + 1}: keys {sorted(rec)}")
            if rec["group_sha"] != hdrs[i]:
                return fail(f"batch{bi} line {i + 1}: sha "
                            f"{rec['group_sha']} != md header {hdrs[i]}")
            if rec["type"] not in TYPES:
                return fail(f"batch{bi} line {i + 1}: bad type {rec['type']}")
            if rec["negation_present"] not in ("yes", "no"):
                return fail(f"batch{bi} line {i + 1}: bad negation_present")
            if rec["group_sha"] not in groups:
                return fail(f"batch{bi}: sha {rec['group_sha']} not fresh")
            coded.append(rec)
    if len(coded) != 120:
        return fail(f"{len(coded)} coded records, expected 120")
    if {r["group_sha"] for r in coded} != set(man_sha):
        return fail("coded sha set != manifest sha set")

    # 5-way agreement
    by_sha = {r["group_sha"]: r for r in man}
    conf = defaultdict(Counter)
    exact_src = Counter()
    n_src = Counter()
    neg_ok = Counter()
    neg_src_ok = Counter()
    neg_src_n = Counter()
    for rec in coded:
        g = groups[rec["group_sha"]]
        conf[g["auto_type"]][rec["type"]] += 1
        src = g["source"]
        n_src[src] += 1
        if rec["type"] == g["auto_type"]:
            exact_src[src] += 1
        neg_src_n[src] += 1
        if rec["negation_present"] == g["negation_present"]:
            neg_src_ok[src] += 1
        neg_ok["yes" if rec["negation_present"] == g["negation_present"]
               else "no"] += 1
    n = len(coded)
    exact = sum(exact_src.values())
    neg_n = sum(neg_src_ok.values())

    # weighted (population) blind proportions
    w = {"fever": 1515 / 100, "scifact": 67 / 20}
    wcount = Counter()
    blind_dist = Counter()
    blind_by_src = defaultdict(Counter)
    wneg = Counter()
    for rec in coded:
        src = groups[rec["group_sha"]]["source"]
        blind_dist[rec["type"]] += 1
        blind_by_src[src][rec["type"]] += 1
        wcount[rec["type"]] += w[src]
        wneg[rec["negation_present"]] += w[src]
    wtotal = sum(wcount.values())
    auto_dist = Counter(g["auto_type"] for g in
                        (groups[r["group_sha"]] for r in man))
    neg_blind = Counter(r["negation_present"] for r in coded)
    neg_auto = Counter(groups[r["group_sha"]]["negation_present"] for r in man)

    summary = {
        "design": {"seed": 20260925, "n": 120,
                   "strata": {"fever": 100, "scifact": 20},
                   "population": {"fresh_groups": 1582, "fever": 1515,
                                  "scifact": 67},
                   "coders": "3 local agents, blind to auto labels, 1 batch each"},
        "validity": {"manifest_rows": 120, "batch_headers": [40, 40, 40],
                     "coded_records": 120, "sha_sets_match": True,
                     "label_domains_ok": True},
        "agreement": {
            "five_way_exact": {"overall": exact, "n": n,
                               "pct": round(100 * exact / n, 1),
                               "fever": {"exact": exact_src["fever"],
                                         "n": n_src["fever"],
                                         "pct": round(100 * exact_src["fever"]
                                                      / n_src["fever"], 1)},
                               "scifact": {"exact": exact_src["scifact"],
                                           "n": n_src["scifact"],
                                           "pct": round(100 * exact_src["scifact"]
                                                        / n_src["scifact"], 1)}},
            "negation_flag": {"exact": neg_n, "n": n,
                              "pct": round(100 * neg_n / n, 1),
                              "fever_pct": round(100 * neg_src_ok["fever"]
                                                 / neg_src_n["fever"], 1),
                              "scifact_pct": round(100 * neg_src_ok["scifact"]
                                                   / neg_src_n["scifact"], 1)},
            "confusion_auto_rows_blind_cols": {
                a: dict(conf[a]) for a in TYPES},
        },
        "distributions": {
            "auto_on_sample": dict(auto_dist),
            "blind_on_sample": dict(blind_dist),
            "blind_sample_by_source": {s: dict(c)
                                       for s, c in blind_by_src.items()},
            "blind_population_weighted_pct": {
                t: round(100 * wcount[t] / wtotal, 1) for t in TYPES},
            "auto_population_pct": None,   # filled by census from full CSV
            "negation_flag": {"auto": dict(neg_auto), "blind": dict(neg_blind),
                              "blind_population_weighted_pct": {
                                  k: round(100 * v / sum(wneg.values()), 1)
                                  for k, v in wneg.items()}},
        },
        "notes": "auto labels are deterministic tags; blind proportions are "
                 "the audited landscape estimate. Agreement is reported, "
                 "not silently reconciled.",
    }
    with open(PFX + "_taxaudit_summary.json", "w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=1, ensure_ascii=False)

    print(f"VALID: manifest 120 | batches 40/40/40 | coded 120 | sha sets match")
    print(f"5-way agreement: {exact}/{n} = {100 * exact / n:.1f}% "
          f"(fever {exact_src['fever']}/{n_src['fever']}, "
          f"scifact {exact_src['scifact']}/{n_src['scifact']})")
    print(f"negation-flag agreement: {neg_n}/{n} = {100 * neg_n / n:.1f}%")
    print("confusion (auto -> blind):")
    for a in TYPES:
        print(f"  {a:24s} {dict(conf[a].most_common())}")
    print("blind sample dist:", dict(blind_dist.most_common()))
    print("blind weighted %:",
          {t: round(100 * wcount[t] / wtotal, 1) for t in TYPES})
    print("blind weighted negation_flag %:",
          {k: round(100 * v / sum(wneg.values()), 1)
           for k, v in wneg.items()})
    print(f"wrote {PFX}_taxaudit_summary.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
