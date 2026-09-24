"""G25A selection: pure filtering of the frozen G24A candidates (prereg §5).

Implements prereg §5 and nothing else:

* the eligibility rule is **imported** from ``select_g24a`` — byte-identical
  ``leverage(item, rows) ≥ TAU = 10.0`` with all three values present;
* quotas Option B (user-confirmed): ``fever/SUPPORTS 150``,
  ``fever/REFUTES 150``, ``scifact/SUPPORT 100`` → n = 400;
  ``scifact/CONTRADICT`` is not a quota stratum (documented pool exhaustion,
  stratum audit §3) and is never selected;
* every ``item_id`` in ``data/items/g24a_v1.jsonl`` (the 600) is excluded
  before eligibility (§2 disjointness, enforced in code and tested);
* candidates file frozen order, first-eligible fill per stratum; shortfall is
  reported, never topped up (§5);
* selection reads only Base/Admit rows through ``select_g24a.load_rows`` — any
  Exclude kind or probe row aborts (§9.2 blindness by construction).

Dry-run anchor (prereg §5; executed 2026-09-24, now reproduced here): quotas
fill 400/400 (150/150/100), 342 distinct ``source/cluster`` keys of which 126
are shared with the G24A 600, selected leverage min/p50/max =
10.0/36.8/99.9, and ``sha256("\\n".join(sorted(item_ids)))[:16] ==
"0b38e0837ed9fd60"``.  ``main()`` recomputes every anchor and aborts on any
mismatch — this script exists to reproduce the frozen selection, not to make
a new one.

Usage:
    PYTHONPATH=src python src/select_g25a.py
    # overrides: --rows --candidates --g24a-items --out-items --report
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build_g24a_items import SEED  # noqa: E402
from select_g24a import (SELECT_KINDS, SELECTION_MODEL_TAG, TAU,  # noqa: E402
                         leverage, load_rows)

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

QUOTAS = {("fever", "SUPPORTS"): 150, ("fever", "REFUTES"): 150,
          ("scifact", "SUPPORT"): 100}
QUOTA_STRATA = tuple(QUOTAS)                      # frozen §5 (Option B) order
DROPPED_STRATUM = "scifact/CONTRADICT"            # pool exhaustion (§5, audit §3)

# dry-run anchor, prereg §5 (the hash is over "\n".join(sorted(item_ids)))
ANCHOR_ID_SHA16 = "0b38e0837ed9fd60"
ANCHOR = {"selected_total": 400,
          "quotas": {f"{s}/{l}": q for (s, l), q in QUOTAS.items()},
          "clusters": 342,
          "clusters_shared_with_g24a": 126,
          "leverage_min": 10.0, "leverage_p50": 36.8, "leverage_max": 99.9}


def cluster_key(rec: dict) -> str:
    """Bootstrap/overlap cluster key — G24A's source namespacing (§2, §5)."""
    meta = rec["meta"]
    return f"{meta['source']}/{meta['cluster']}"


def load_jsonl(path: str) -> list[dict]:
    with open(path) as handle:
        return [json.loads(line) for line in handle if line.strip()]


def load_excluded(paths: list[str]) -> tuple[set[str], set[str]]:
    """item_ids and cluster_keys of the G24A 600 (the disjointness set)."""
    ids, clusters = set(), set()
    for rec in (r for p in paths for r in load_jsonl(p)):
        ids.add(rec["item_id"])
        clusters.add(cluster_key(rec))
    return ids, clusters


def census(candidates: list[dict], rows: dict,
           excluded: set[str]) -> dict:
    """Full-pool walk per stratum, exclusion checked first (§2/§5 pool facts).

    Reproduces ``PAPER_RQ2_SWEEP_STRATUM_AUDIT_2026-09-24.md`` §2 exactly:
    ``remaining = pool − excluded`` and ``eligible`` is counted on the
    remaining only.  No quota stop — this is a census, not the selection.
    """
    stats: dict[str, dict] = {}
    for rec in candidates:
        stratum = rec["meta"]["stratum"]
        st = stats.setdefault(stratum, {"pool": 0, "excluded": 0,
                                        "missing_value": 0, "below_tau": 0,
                                        "eligible": 0})
        st["pool"] += 1
        if rec["item_id"] in excluded:
            st["excluded"] += 1
            continue
        lev = leverage(rec, rows.get(rec["item_id"], {}))
        if lev is None:
            st["missing_value"] += 1
        elif lev < TAU:
            st["below_tau"] += 1
        else:
            st["eligible"] += 1
    for st in stats.values():
        st["remaining"] = st["pool"] - st["excluded"]
    return stats


def select(candidates: list[dict], rows: dict, excluded: set[str],
           quotas: dict | None = None) -> tuple[list[dict], dict]:
    """First-eligible selection in frozen file order (pure; testable).

    ``quotas`` defaults to the frozen Option-B table; tests may inject a
    smaller table — the walk logic is identical either way.
    """
    quotas = dict(QUOTAS if quotas is None else quotas)
    selected: list[dict] = []
    stats = {f"{s}/{lab}": {"pool": 0, "excluded": 0, "examined": 0,
                            "eligible": 0, "selected": 0, "missing_value": 0,
                            "below_tau": 0, "quota": quotas[(s, lab)],
                            "shortfall": quotas[(s, lab)]}
             for s, lab in quotas}
    levs: list[float] = []
    all_full = False
    for rec in candidates:
        s_lab = (rec["meta"]["source"], rec["meta"]["gold_label"])
        if s_lab not in quotas:
            continue                       # dropped stratum: never selected
        st = stats[f"{s_lab[0]}/{s_lab[1]}"]
        st["pool"] += 1
        if rec["item_id"] in excluded:
            st["excluded"] += 1            # §2 disjointness, enforced here
            continue
        if st["selected"] >= quotas[s_lab]:
            continue                       # stratum full: not examined further
        st["examined"] += 1
        lev = leverage(rec, rows.get(rec["item_id"], {}))
        if lev is None:
            st["missing_value"] += 1
            continue
        if lev < TAU:
            st["below_tau"] += 1
            continue
        st["eligible"] += 1
        st["selected"] += 1
        selected.append(rec)               # byte-identical candidate record
        levs.append(lev)
        # global stop: EVERY quota stratum at its own quota
        if all(stats[f"{a}/{b}"]["selected"] >= quotas[(a, b)]
               for a, b in quotas):
            all_full = True
            break
    for st in stats.values():
        st["shortfall"] = st["quota"] - st["selected"]
    assert (not all_full) or all(
        st["shortfall"] == 0 for st in stats.values()), \
        "early stop without all quotas genuinely full"

    ids = sorted(rec["item_id"] for rec in selected)
    clusters = {cluster_key(rec) for rec in selected}
    report = {
        "tau": TAU,
        "seed_order": SEED,
        "selection_model_tag": SELECTION_MODEL_TAG,
        "selection_kinds": sorted(SELECT_KINDS),
        "quota_strata": [f"{s}/{l}" for s, l in quotas],
        "dropped_stratum": DROPPED_STRATUM,
        "strata": stats,
        "selected_total": len(selected),
        "quota_total": sum(quotas.values()),
        "all_quotas_filled": all_full or all(
            st["shortfall"] == 0 for st in stats.values()),
        "clusters": len(clusters),
        "leverage_selected_min": min(levs) if levs else None,
        "leverage_selected_p50": (sorted(levs)[len(levs) // 2] if levs else None),
        "leverage_selected_max": max(levs) if levs else None,
        "selected_ids_sha16": hashlib.sha256(
            "\n".join(ids).encode()).hexdigest()[:16],
        "anchor_expected_sha16": ANCHOR_ID_SHA16,
    }
    report["anchor_ok"] = (
        report["selected_ids_sha16"] == ANCHOR_ID_SHA16
        and report["selected_total"] == ANCHOR["selected_total"]
        and {k: v["selected"] for k, v in stats.items()} == ANCHOR["quotas"]
        and report["clusters"] == ANCHOR["clusters"]
        and round(report["leverage_selected_min"], 1) == ANCHOR["leverage_min"]
        and round(report["leverage_selected_p50"], 1) == ANCHOR["leverage_p50"]
        and round(report["leverage_selected_max"], 1) == ANCHOR["leverage_max"])
    return selected, report


def _report_md(report: dict) -> str:
    lines = ["# G25A selection report v1", "",
             f"- eligibility: imported G24A rule — signed mean Admit leverage "
             f"≥ {report['tau']} readout points (Base/Admit rows only, model "
             f"`{report['selection_model_tag']}`; no Exclude/probe row read)",
             f"- quotas (Option B): {', '.join(report['quota_strata'])} → "
             f"{report['quota_total']}; `{report['dropped_stratum']}` dropped "
             f"(pool exhaustion, stratum audit §3)",
             f"- disjointness: every item_id of the G24A 600 excluded before "
             f"eligibility (item-level; cluster overlap disclosed, not hidden)",
             f"- selected {report['selected_total']} / quota "
             f"{report['quota_total']}; all quotas filled: "
             f"{report['all_quotas_filled']}",
             f"- clusters (`source/cluster`): {report['clusters']} "
             f"(anchor 342; shared with G24A 600: see anchor check)",
             f"- selected-item leverage: min "
             f"{report['leverage_selected_min']:.1f}, p50 "
             f"{report['leverage_selected_p50']:.1f}, max "
             f"{report['leverage_selected_max']:.1f}",
             f"- selected ids sha256[:16]: `{report['selected_ids_sha16']}` "
             f"(expected `{report['anchor_expected_sha16']}`) — anchor_ok: "
             f"{report['anchor_ok']}",
             "", "| stratum | pool | excluded | examined | eligible | "
             "selected | shortfall | missing | <τ |",
             "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for name, st in report["strata"].items():
        lines.append(
            f"| {name} | {st['pool']} | {st['excluded']} | {st['examined']} | "
            f"{st['eligible']} | {st['selected']} | {st['shortfall']} | "
            f"{st['missing_value']} | {st['below_tau']} |")
    lines += ["", "Census (full pool, exclusion first; audit §2 reproduction):",
              "", "| stratum | pool | excluded (=remaining sub) | remaining "
              "| missing | <τ | eligible |", "| --- | --- | --- | --- | --- | "
              "--- | --- |"]
    for name, st in report.get("census", {}).items():
        lines.append(
            f"| {name} | {st['pool']} | {st['excluded']} | "
            f"{st['remaining']} | {st['missing_value']} | {st['below_tau']} | "
            f"{st['eligible']} |")
    if any(st["shortfall"] for st in report["strata"].values()):
        lines += ["", "SHORTFALL: at least one stratum exhausted its pool "
                      "before quota; quotas/τ/order were NOT changed (§5)."]
    if report.get("selected_sha256"):
        lines += ["", f"selected file sha256: `{report['selected_sha256']}`"]
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rows", nargs="+",
                    default=[os.path.join(
                        ROOT, "results/raw/"
                              "g24a_mistral-small-24b_selection.jsonl")])
    ap.add_argument("--candidates", default=os.path.join(
        ROOT, "data/items/g24a_candidates_v1.jsonl"))
    ap.add_argument("--g24a-items", nargs="+", default=[os.path.join(
        ROOT, "data/items/g24a_v1.jsonl")])
    ap.add_argument("--out-items", default=os.path.join(
        ROOT, "data/items/g25_v1.jsonl"))
    ap.add_argument("--report", default=os.path.join(
        ROOT, "data/items/g25_selection_report_v1"))
    ap.add_argument("--expect-tag", default=SELECTION_MODEL_TAG)
    args = ap.parse_args()

    rows = load_rows(args.rows, args.expect_tag)          # §9.2 guards
    candidates = load_jsonl(args.candidates)
    excluded, g24a_clusters = load_excluded(args.g24a_items)
    selected, report = select(candidates, rows, excluded)
    report["census"] = census(candidates, rows, excluded)
    report["clusters_shared_with_g24a"] = len(
        {cluster_key(r) for r in selected} & g24a_clusters)
    report["candidates_sha256"] = hashlib.sha256(
        open(args.candidates, "rb").read()).hexdigest()
    report["rows_sha256"] = {p: hashlib.sha256(open(p, "rb").read()).hexdigest()
                             for p in args.rows}
    report["g24a_items_sha256"] = {
        p: hashlib.sha256(open(p, "rb").read()).hexdigest()
        for p in args.g24a_items}

    if not report["anchor_ok"] or \
            report["clusters_shared_with_g24a"] != \
            ANCHOR["clusters_shared_with_g24a"]:
        raise SystemExit(
            "DRY-RUN ANCHOR MISMATCH — this script must reproduce the frozen "
            f"§5 selection; got sha16={report['selected_ids_sha16']} "
            f"n={report['selected_total']} clusters={report['clusters']} "
            f"shared={report['clusters_shared_with_g24a']} "
            f"lev=({report['leverage_selected_min']}, "
            f"{report['leverage_selected_p50']}, "
            f"{report['leverage_selected_max']})")

    os.makedirs(os.path.dirname(args.out_items), exist_ok=True)
    with open(args.out_items, "w") as fh:
        for rec in selected:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    report["selected_sha256"] = hashlib.sha256(
        open(args.out_items, "rb").read()).hexdigest()
    # every selected record is byte-identical to a candidate record
    cand_lines = {line.rstrip("\n") for line in open(args.candidates)}
    with open(args.out_items) as fh:
        sel_lines = [line.rstrip("\n") for line in fh]
    assert all(line in cand_lines for line in sel_lines), \
        "selected != candidate bytes"
    assert len(set(sel_lines)) == len(sel_lines), "duplicate selected record"

    with open(args.report + ".json", "w") as fh:
        json.dump(report, fh, indent=1, ensure_ascii=False)
    with open(args.report + ".md", "w") as fh:
        fh.write(_report_md(report))
    print(_report_md(report))
    print(f"wrote {len(selected)} selected items -> {args.out_items}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
