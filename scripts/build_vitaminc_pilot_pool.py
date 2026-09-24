#!/usr/bin/env python3
"""Build the VitaminC exclusion-pilot item pool — spec v2 chain (F1-F7).

results/pilots/vitaminc_pilot_r1/spec_v2.md freezes the filter chain; this
script is its mechanical transcription:

    F1 real rows, valid label, non-empty claim/evidence
    F2 canonical 1S+1R group with differing evidence texts
    F3 evidence-pair token similarity >= 0.90
    F4 normalized claim dedup (casefold, ws-collapse, rstrip " ."), keep first
    F5 non-template claims (audit D4 regex must NOT match)
    F6 at most one qualifying claim per revision/case, keep first
    F7 fixed-seed random sample of 200 over file-ordered candidates

Deterministic (seed 20260925), never effect-sorted, no model involved.

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
import random
import re

SOURCE = "data/external/raw/vitaminc/train.jsonl"
SOURCE_SHA = "7461c6fd1a13459590317c5ccdc8651dd2daf7c1ad8ae4b10ccd88d164fccd5a"
SIM_MIN = 0.90
N_POOL = 200
SEED = 20260925
LABELS = ("SUPPORTS", "REFUTES", "NOT ENOUGH INFO")
# F5: audit D4 template regex, byte-identical to results/audits/..._v1.json
TEMPLATE_RE = re.compile(
    r"(less than|more than|fewer than|over|under|at least|at most)\b[^.]{0,20}\d",
    re.IGNORECASE,
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sim(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, a.split(), b.split(), autojunk=False).ratio()


def norm_claim(claim: str) -> str:
    return re.sub(r"\s+", " ", claim).strip().casefold().rstrip(" .")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default=SOURCE)
    ap.add_argument("--out", default="results/pilots/vitaminc_pilot_r1/pool_v2.jsonl")
    args = ap.parse_args()
    src = Path(args.source)
    if sha256(src) != SOURCE_SHA:
        raise SystemExit(f"source sha256 mismatch: {src}")

    # --- F1 + grouping in first-encounter (file) order ---------------------
    groups: dict[tuple[str, str], list[tuple[str, str, int]]] = defaultdict(list)
    page_of_case: dict[str, str] = {}
    n_rows = n_real = n_malformed = 0
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
                n_malformed += 1
                continue
            key = (str(row.get("case_id")), claim)
            groups[key].append((label, evidence, lineno))
            page_of_case.setdefault(str(row.get("case_id")), str(row.get("page")))

    # --- F2..F6 over all groups, in file order -----------------------------
    candidates = []
    seen_norm: set[str] = set()
    seen_case: set[str] = set()
    stats = {"groups": len(groups), "f2_shape": 0, "f3_sim": 0, "f4_dup": 0,
             "f5_template": 0, "f6_case_dup": 0}
    for (case_id, claim), rows in groups.items():
        s_rows = [r for r in rows if r[0] == "SUPPORTS"]
        r_rows = [r for r in rows if r[0] == "REFUTES"]
        if len(s_rows) != 1 or len(r_rows) != 1:
            continue
        s_text, r_text = s_rows[0][1], r_rows[0][1]
        if s_text == r_text:
            continue
        stats["f2_shape"] += 1
        # F3
        s_value = sim(s_text, r_text)
        if s_value < SIM_MIN:
            continue
        stats["f3_sim"] += 1
        # F4 normalized claim dedup, keep first
        key_norm = norm_claim(claim)
        if key_norm in seen_norm:
            stats["f4_dup"] += 1
            continue
        # F5 non-template
        if TEMPLATE_RE.search(claim):
            stats["f5_template"] += 1
            continue
        # F6 one per revision/case, keep first
        if case_id in seen_case:
            stats["f6_case_dup"] += 1
            continue
        seen_norm.add(key_norm)
        seen_case.add(case_id)
        candidates.append({
            "case_id": case_id,
            "claim": claim,
            "evidence_s": s_text,
            "evidence_r": r_text,
            "sim": s_value,
            "page": page_of_case.get(case_id),
            "train_first_lineno": min(s_rows[0][2], r_rows[0][2]),
        })

    if len(candidates) < N_POOL:
        raise SystemExit(f"only {len(candidates)} candidates, need {N_POOL}")

    # --- F7 fixed-seed sample, then file order for ids ---------------------
    rng = random.Random(SEED)
    chosen = rng.sample(candidates, N_POOL)
    chosen.sort(key=lambda c: c["train_first_lineno"])
    for i, item in enumerate(chosen, start=1):
        item["pilot_id"] = f"p{i:04d}"

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as handle:
        for item in chosen:
            handle.write(json.dumps(item, ensure_ascii=False) + "\n")

    sims = sorted(item["sim"] for item in chosen)
    lines = sorted(item["train_first_lineno"] for item in chosen)
    print(f"source rows {n_rows} (real {n_real}, malformed {n_malformed})")
    print(f"groups {stats['groups']} | F2 {stats['f2_shape']} | F3 {stats['f3_sim']} | "
          f"F4 dup {stats['f4_dup']} | F5 template {stats['f5_template']} | "
          f"F6 case dup {stats['f6_case_dup']} | candidates {len(candidates)}")
    print(f"sample seed {SEED} -> pool {len(chosen)} -> {out}")
    print(f"sim min/median/max {sims[0]:.4f}/{sims[len(sims)//2]:.4f}/{sims[-1]:.4f}")
    print(f"line range {lines[0]}..{lines[-1]} (informational only)")
    print(f"pool sha256 {sha256(out)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
