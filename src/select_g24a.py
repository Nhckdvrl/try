"""G24A selection: eligible-by-Base/Admit, first-eligible per frozen quota.

Implements prereg §5 and nothing else:

* input rows may contain ONLY ``base``, ``admit_pre``, ``admit_post`` — any
  exclude kind or probe in the selection rows aborts (§9.2);
* the row set must come from exactly one model tag, defaulted to the frozen
  selection model ``mistral-small-24b`` (§4);
* eligibility: ``s · (mean(admit_pre, admit_post) − base) ≥ TAU`` with all
  three values non-null (§5.3);
* walk the candidates file in its frozen order, take the first eligible item
  per stratum until the quota, stop a stratum at its quota (§5.4);
* shortfall is reported, never re-ruled (§5.5).

Selected items are byte-identical copies of their candidate records, so every
selected line is verifiable against the candidates file.

Usage:
    PYTHONPATH=src python src/select_g24a.py \
        --rows results/raw/mistral-small-24b_g24a_selection.jsonl \
        --candidates data/items/g24a_candidates_v1.jsonl \
        --out-items data/items/g24a_v1.jsonl \
        --report data/items/g24a_selection_report_v1
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build_g24a_items import SEED, STRATA  # noqa: E402

TAU = 10.0
QUOTAS = {("fever", "SUPPORTS"): 200, ("fever", "REFUTES"): 200,
          ("scifact", "SUPPORT"): 100, ("scifact", "CONTRADICT"): 100}
SELECT_KINDS = {"base", "admit_pre", "admit_post"}
SELECTION_MODEL_TAG = "mistral-small-24b"
SIGNED = {"increase": 1, "decrease": -1}


def load_rows(paths: list[str], expect_tag: str = SELECTION_MODEL_TAG) -> dict:
    """{item_id: {kind: value}} from selection-pass run files, guarded."""
    rows: dict[str, dict] = {}
    tags = set()
    for p in paths:
        for line in open(p):
            r = json.loads(line)
            if r.get("kind_name") not in SELECT_KINDS:
                raise SystemExit(
                    f"selection input contains non-Base/Admit kind "
                    f"{r.get('kind_name')!r} — Exclude/probe outcomes may "
                    f"never enter selection (prereg §5, §9.2)")
            tags.add(r.get("model_tag"))
            rows.setdefault(r["item_id"], {})[r["kind_name"]] = r.get("value")
    if len(tags) != 1:
        raise SystemExit(f"selection rows must come from one model, got {tags}")
    tag = tags.pop()
    if tag != expect_tag:
        raise SystemExit(f"selection model tag {tag!r} != frozen "
                         f"{expect_tag!r} (prereg §4)")
    return rows


def leverage(item: dict, values: dict | None) -> float | None:
    """Signed Admit leverage s·(mean(admit)−base); None if any value missing."""
    ks = ("base", "admit_pre", "admit_post")
    if not values:
        return None
    vals = [values.get(k) for k in ks]
    if any(v is None for v in vals):
        return None
    s = SIGNED[item["critical_direction"]]
    return s * ((vals[1] + vals[2]) / 2.0 - vals[0])


def select(candidates: list[dict], rows: dict,
           tau: float = TAU, quotas: dict = QUOTAS) -> tuple[list[dict], dict]:
    """First-eligible selection in frozen file order (pure; testable)."""
    selected: list[dict] = []
    stats = {f"{s}/{lab}": {"pool": 0, "examined": 0, "eligible": 0,
                            "selected": 0, "missing_value": 0,
                            "below_tau": 0, "quota": quotas[(s, lab)]}
             for s, lab in STRATA}
    levs: list[float] = []
    all_full = False
    for it in candidates:
        s_lab = (it["meta"]["source"], it["meta"]["gold_label"])
        if s_lab not in quotas:
            raise SystemExit(f"unknown stratum {s_lab} in {it['item_id']}")
        st = stats[f"{s_lab[0]}/{s_lab[1]}"]
        st["pool"] += 1
        if st["selected"] >= quotas[s_lab]:
            continue                       # stratum full: not examined further
        st["examined"] += 1
        lev = leverage(it, rows.get(it["item_id"], {}))
        if lev is None:
            st["missing_value"] += 1
            continue
        if lev < tau:
            st["below_tau"] += 1
            continue
        st["eligible"] += 1
        st["selected"] += 1
        selected.append(it)                # byte-identical candidate record
        levs.append(lev)
        if all(st["selected"] >= quotas[k] for k in quotas):
            all_full = True
            break
    for st in stats.values():
        st["shortfall"] = st["quota"] - st["selected"]
    report = {
        "tau": tau,
        "seed_order": SEED,
        "selection_model_tag": SELECTION_MODEL_TAG,
        "selection_kinds": sorted(SELECT_KINDS),
        "strata": stats,
        "selected_total": len(selected),
        "quota_total": sum(quotas.values()),
        "all_quotas_filled": all_full or all(
            st["shortfall"] == 0 for st in stats.values()),
        "leverage_selected_min": min(levs) if levs else None,
        "leverage_selected_p50": (sorted(levs)[len(levs) // 2] if levs else None),
        "leverage_selected_max": max(levs) if levs else None,
    }
    return selected, report


def _quantile_md(report: dict) -> str:
    lines = ["# G24A selection report v1", "",
             f"- selection model: `{report['selection_model_tag']}` "
             f"(kinds: {', '.join(report['selection_kinds'])} — no Exclude, "
             f"no probes)",
             f"- eligibility: signed mean Admit leverage ≥ {report['tau']} "
             f"readout points; candidate order = builder shuffle seed "
             f"{report['seed_order']}",
             f"- selected {report['selected_total']} / quota "
             f"{report['quota_total']}; all quotas filled: "
             f"{report['all_quotas_filled']}",
             f"- selected-item leverage (selection model): "
             f"min {report['leverage_selected_min']:.1f}, "
             f"p50 {report['leverage_selected_p50']:.1f}, "
             f"max {report['leverage_selected_max']:.1f}",
             "", "| stratum | pool | examined | eligible | selected | "
             "shortfall | missing | <τ |", "| --- | --- | --- | --- | --- | "
             "--- | --- | --- |"]
    for name, st in report["strata"].items():
        lines.append(f"| {name} | {st['pool']} | {st['examined']} | "
                     f"{st['eligible']} | {st['selected']} | {st['shortfall']} "
                     f"| {st['missing_value']} | {st['below_tau']} |")
    if any(st["shortfall"] for st in report["strata"].values()):
        lines += ["", "SHORTFALL: at least one stratum exhausted its pool "
                      "before quota; quotas/τ/order were NOT changed "
                      "(prereg §5.5)."]
    lines += ["", f"selected file sha256: `{report['selected_sha256']}`"]
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rows", nargs="+", required=True)
    ap.add_argument("--candidates", default="data/items/g24a_candidates_v1.jsonl")
    ap.add_argument("--out-items", default="data/items/g24a_v1.jsonl")
    ap.add_argument("--report", default="data/items/g24a_selection_report_v1")
    ap.add_argument("--expect-tag", default=SELECTION_MODEL_TAG)
    args = ap.parse_args()

    rows = load_rows(args.rows, args.expect_tag)
    candidates = [json.loads(l) for l in open(args.candidates) if l.strip()]
    selected, report = select(candidates, rows)

    os.makedirs(os.path.dirname(args.out_items), exist_ok=True)
    with open(args.out_items, "w") as fh:
        for it in selected:
            fh.write(json.dumps(it, ensure_ascii=False) + "\n")
    report["selected_sha256"] = hashlib.sha256(
        open(args.out_items, "rb").read()).hexdigest()
    report["candidates_sha256"] = hashlib.sha256(
        open(args.candidates, "rb").read()).hexdigest()
    # every selected record is byte-identical to a candidate record
    cand_lines = {l.rstrip("\n") for l in open(args.candidates)}
    sel_lines = [l.rstrip("\n") for l in open(args.out_items)]
    assert all(l in cand_lines for l in sel_lines), "selected != candidate bytes"

    with open(args.report + ".json", "w") as fh:
        json.dump(report, fh, indent=1, ensure_ascii=False)
    with open(args.report + ".md", "w") as fh:
        fh.write(_quantile_md(report))
    print(_quantile_md(report))
    print(f"wrote {len(selected)} selected items -> {args.out_items}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
