#!/usr/bin/env python3
"""Build the VitaminC exclusion-pilot item pool (spec v1, F1-F5).

results/pilots/vitaminc_pilot_r1/spec_v1.md freezes the filter chain; this
script is its mechanical transcription. Deterministic: train file order,
first 200 qualifying groups, never effect-sorted, no model involved.

Run:
  /home/xiang/miniconda3/envs/fgvd/bin/python scripts/build_vitaminc_pilot_pool.py
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import difflib
import hashlib
import json
from pathlib import Path

SOURCE = "data/external/raw/vitaminc/train.jsonl"
SOURCE_SHA = "7461c6fd1a13459590317c5ccdc8651dd2daf7c1ad8ae4b10ccd88d164fccd5a"
SIM_MIN = 0.80
N_POOL = 200
LABELS = ("SUPPORTS", "REFUTES", "NOT ENOUGH INFO")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sim(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, a.split(), b.split(), autojunk=False).ratio()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default=SOURCE)
    ap.add_argument("--out", default="results/pilots/vitaminc_pilot_r1/pool_v1.jsonl")
    args = ap.parse_args()
    src = Path(args.source)
    if sha256(src) != SOURCE_SHA:
        raise SystemExit(f"source sha256 mismatch: {src}")

    # --- F1 + grouping in first-encounter (file) order ---------------------
    groups: dict[tuple[str, str], list[tuple[str, str, int]]] = defaultdict(list)
    page_of_case: dict[str, str] = {}
    n_rows = n_real = 0
    with src.open(encoding="utf-8") as handle:
        for lineno, line in enumerate(handle, start=1):
            line = line.rstrip("\n")
            if not line:
                continue
            row = json.loads(line)
            n_rows += 1
            if row.get("revision_type") != "real":
                continue
            n_real += 1
            label = row.get("label")
            claim = row.get("claim") or ""
            evidence = row.get("evidence") or ""
            if label not in LABELS or not claim or not evidence:
                continue  # malformed (audit measured: 0 such rows in train)
            key = (str(row.get("case_id")), claim)
            groups[key].append((label, evidence, lineno))
            page_of_case.setdefault(str(row.get("case_id")), str(row.get("page")))

    # --- F2..F5 in file order ---------------------------------------------
    pool = []
    seen_claims: set[str] = set()
    stats = {"groups": len(groups), "f2_shape": 0, "f3_sim": 0, "f4_dup": 0}
    for (case_id, claim), rows in groups.items():
        s_rows = [r for r in rows if r[0] == "SUPPORTS"]
        r_rows = [r for r in rows if r[0] == "REFUTES"]
        # F2: exactly one SUPPORTS row and exactly one REFUTES row, texts differ
        if len(s_rows) != 1 or len(r_rows) != 1:
            continue
        if s_rows[0][1] == r_rows[0][1]:
            continue
        stats["f2_shape"] += 1
        # F3: evidence-pair token similarity >= 0.80
        s_text, r_text = s_rows[0][1], r_rows[0][1]
        s_value = sim(s_text, r_text)
        if s_value < SIM_MIN:
            continue
        stats["f3_sim"] += 1
        # F4: dedup by exact claim text, keep first
        if claim in seen_claims:
            stats["f4_dup"] += 1
            continue
        # F5: first N_POOL in train file order
        if len(pool) >= N_POOL:
            break
        seen_claims.add(claim)
        pool.append({
            "pilot_id": f"p{len(pool) + 1:04d}",
            "case_id": case_id,
            "claim": claim,
            "evidence_s": s_text,
            "evidence_r": r_text,
            "sim": s_value,
            "page": page_of_case.get(case_id),
            "train_first_lineno": min(s_rows[0][2], r_rows[0][2]),
        })

    if len(pool) != N_POOL:
        raise SystemExit(f"pool has {len(pool)} rows, expected {N_POOL}")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as handle:
        for item in pool:
            handle.write(json.dumps(item, ensure_ascii=False) + "\n")

    sims = sorted(item["sim"] for item in pool)
    print(f"source rows {n_rows} (real {n_real})")
    print(f"groups {stats['groups']} | F2 shape ok {stats['f2_shape']} | "
          f"F3 sim ok {stats['f3_sim']} | F4 dup dropped {stats['f4_dup']}")
    print(f"pool {len(pool)} -> {out}")
    print(f"sim min/median/max {sims[0]:.4f}/{sims[len(sims)//2]:.4f}/{sims[-1]:.4f}")
    print(f"pool sha256 {sha256(out)}")
    print(f"first {pool[0]['pilot_id']} line {pool[0]['train_first_lineno']} | "
          f"last {pool[-1]['pilot_id']} line {pool[-1]['train_first_lineno']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
