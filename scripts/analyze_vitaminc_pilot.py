#!/usr/bin/env python3
"""Pilot gate analyzer (spec v2) — tiny by design, no elaborate analysis.

Stage A (after raw_r1a.jsonl, 600 rows):
    A_S = Y_S - Y_0,  A_R = Y_0 - Y_R   (per item)
    usable iff A_S >= 10 and A_R >= 10
    exit 0 = continue (n_usable >= 120),  exit 2 = KILL (< 120)

Stage B (after raw_r1b.jsonl, +400 rows):
    C^S_pre = Y_EXCL-pre(S) - Y_0,  C^R_pre = Y_0 - Y_EXCL-pre(R)
    exit 0 = INVERSION_SERIOUS (both means <= -3; would justify the future
             EXCL_post stage, pending user)
    exit 3 = HEADLINE_KILL (both means > 0: attenuation/leakage only)
    exit 4 = NO_STORY (anything else: one-sided or weak; truth-prior /
             floor-ceiling / label asymmetry first)

Run:
  /home/xiang/miniconda3/envs/fgvd/bin/python scripts/analyze_vitaminc_pilot.py --stage a
  /home/xiang/miniconda3/envs/fgvd/bin/python scripts/analyze_vitaminc_pilot.py --stage b
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
import statistics
from pathlib import Path

ROOT = Path("results/pilots/vitaminc_pilot_r1")
USABLE_MIN = 10.0          # per-item A_S / A_R threshold
N_USABLE_MIN = 120         # stage-a gate: >= 120 of 200
CONT_THRESHOLD = -3.0      # stage-b: both means <= -3


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load(path: Path) -> dict:
    """pilot_id -> {cell: value}; verifies exactly one row per (item, cell)."""
    seen = defaultdict(dict)
    n = 0
    meta = {"mass_lt_05": 0, "truncated": 0, "unparsed": 0}
    for line in path.open(encoding="utf-8"):
        row = json.loads(line)
        n += 1
        pid, cell = row["pilot_id"], row["cell"]
        if cell in seen[pid]:
            raise SystemExit(f"duplicate row {pid}/{cell}")
        seen[pid][cell] = row["value"]
        if row["value"] is None:
            meta["unparsed"] += 1
        if row["mass"] < 0.5:
            meta["mass_lt_05"] += 1
        if row.get("reason_truncated"):
            meta["truncated"] += 1
    meta["rows"] = n
    return dict(seen), meta


def stats(vals):
    s = sorted(vals)
    return {
        "n": len(s),
        "mean": statistics.mean(s),
        "median": statistics.median(s),
        "p10": s[max(0, len(s) // 10 - 1)],
        "p90": s[min(len(s) - 1, int(len(s) * 0.9))],
        "min": s[0],
        "max": s[-1],
    }


def stage_a(pool_ids, raw_path: Path) -> int:
    cells_by_item, meta = load(raw_path)
    complete, incomplete = [], []
    a_s, a_r = [], []
    for pid in pool_ids:
        cells = cells_by_item.get(pid, {})
        vals = [cells.get("y0"), cells.get("yplus"), cells.get("yminus")]
        if any(v is None for v in vals):
            incomplete.append(pid)
            continue
        y0, ys, yr = vals
        s_diff, r_diff = ys - y0, y0 - yr
        complete.append(pid)
        a_s.append(s_diff)
        a_r.append(r_diff)
    n_usable = sum(1 for s, r in zip(a_s, a_r)
                   if s >= USABLE_MIN and r >= USABLE_MIN)
    # strict ordering, informational (v1's G3 semantics, reported not gated)
    strict = sum(1 for s, r in zip(a_s, a_r) if s > 0 and r > 0)

    report = {
        "stage": "a",
        "raw": {"path": str(raw_path), "sha256": sha256(raw_path),
                "rows": meta["rows"]},
        "readout_health": meta,
        "n_items": len(pool_ids),
        "n_complete": len(complete),
        "incomplete_ids": incomplete,
        "A_S": stats(a_s) if a_s else None,
        "A_R": stats(a_r) if a_r else None,
        "usable_rule": f"usable iff A_S >= {USABLE_MIN} and A_R >= {USABLE_MIN}",
        "n_usable": n_usable,
        "gate": f"continue iff n_usable >= {N_USABLE_MIN} of {len(pool_ids)}",
        "n_positive_both_strict": strict,
        "verdict": "CONTINUE" if n_usable >= N_USABLE_MIN else "KILL",
    }
    out = ROOT / "report_r1a.json"
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"[stage a] raw sha256 {report['raw']['sha256']} rows {meta['rows']}")
    print(f"[stage a] complete {len(complete)}/{len(pool_ids)} "
          f"(unparsed {meta['unparsed']}, mass<0.5 {meta['mass_lt_05']}, "
          f"truncated {meta['truncated']})")
    if a_s:
        print(f"[stage a] A_S mean/median {report['A_S']['mean']:.2f}/"
              f"{report['A_S']['median']:.2f} | A_R mean/median "
              f"{report['A_R']['mean']:.2f}/{report['A_R']['median']:.2f}")
    print(f"[stage a] usable {n_usable}/{len(pool_ids)} "
          f"(strict both-positive {strict})")
    print(f"[stage a] verdict = {report['verdict']} "
          f"(gate: usable >= {N_USABLE_MIN})")
    print(f"[stage a] report -> {out}")
    return 0 if n_usable >= N_USABLE_MIN else 2


def stage_b(pool_ids, raw_path: Path) -> int:
    cells_by_item, meta = load(raw_path)
    c_s, c_r = [], []
    incomplete = []
    for pid in pool_ids:
        cells = cells_by_item.get(pid, {})
        y0 = cells.get("y0")
        ex_s = cells.get("exclpre_plus")
        ex_r = cells.get("exclpre_minus")
        if y0 is None or ex_s is None or ex_r is None:
            incomplete.append(pid)
            continue
        c_s.append(ex_s - y0)
        c_r.append(y0 - ex_r)
    if not c_s:
        raise SystemExit("no complete items for stage b")
    mean_s, mean_r = statistics.mean(c_s), statistics.mean(c_r)
    if mean_s <= CONT_THRESHOLD and mean_r <= CONT_THRESHOLD:
        verdict = "INVERSION_SERIOUS"
        code = 0
    elif mean_s > 0 and mean_r > 0:
        verdict = "HEADLINE_KILL"
        code = 3
    else:
        verdict = "NO_STORY"
        code = 4

    report = {
        "stage": "b",
        "raw": {"path": str(raw_path), "sha256": sha256(raw_path),
                "rows": meta["rows"]},
        "readout_health": meta,
        "n_items": len(pool_ids),
        "n_complete": len(c_s),
        "incomplete_ids": incomplete,
        "C_S_pre": stats(c_s),
        "C_R_pre": stats(c_r),
        "continuation_gate": {
            "rule": f"both mean(C) <= {CONT_THRESHOLD}",
            "mean_C_S": mean_s,
            "mean_C_R": mean_r,
            "pass": verdict == "INVERSION_SERIOUS",
        },
        "fractions": {
            "C_S_lt_0": sum(1 for v in c_s if v < 0) / len(c_s),
            "C_R_lt_0": sum(1 for v in c_r if v < 0) / len(c_r),
            "both_lt_0": sum(1 for s, r in zip(c_s, c_r) if s < 0 and r < 0) / len(c_s),
        },
        "verdict": verdict,
        "meaning": {
            "INVERSION_SERIOUS": "inversion is a serious phenomenon; would justify the future EXCL_post stage (pending user)",
            "HEADLINE_KILL": "C_pre > 0 both sides: attenuation/leakage only -> headline KILL",
            "NO_STORY": "one-sided or weak: no inversion story; truth-prior / floor-ceiling / label asymmetry first",
        }[verdict],
    }
    out = ROOT / "report_r1b.json"
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"[stage b] raw sha256 {report['raw']['sha256']} rows {meta['rows']}")
    print(f"[stage b] complete {len(c_s)}/{len(pool_ids)} "
          f"(unparsed {meta['unparsed']}, mass<0.5 {meta['mass_lt_05']}, "
          f"truncated {meta['truncated']})")
    print(f"[stage b] mean C_S {mean_s:.2f} | mean C_R {mean_r:.2f} "
          f"(gate: both <= {CONT_THRESHOLD})")
    print(f"[stage b] C_S<0 {report['fractions']['C_S_lt_0']:.1%} | "
          f"C_R<0 {report['fractions']['C_R_lt_0']:.1%} | "
          f"both<0 {report['fractions']['both_lt_0']:.1%}")
    print(f"[stage b] verdict = {verdict} -> {report['meaning']}")
    print(f"[stage b] report -> {out}")
    return code


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", choices=["a", "b"], required=True)
    ap.add_argument("--raw", default=None)
    args = ap.parse_args()
    pool_ids = [json.loads(l)["pilot_id"]
                for l in (ROOT / "pool_v2.jsonl").open(encoding="utf-8")]
    if len(pool_ids) != 200:
        raise SystemExit(f"pool has {len(pool_ids)} items, expected 200")
    raw = Path(args.raw) if args.raw else ROOT / (
        "raw_r1a.jsonl" if args.stage == "a" else "raw_r1b.jsonl")
    if not raw.exists():
        raise SystemExit(f"missing {raw}")
    return stage_a(pool_ids, raw) if args.stage == "a" else stage_b(pool_ids, raw)


if __name__ == "__main__":
    raise SystemExit(main())
