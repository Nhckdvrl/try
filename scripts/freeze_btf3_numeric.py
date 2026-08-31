#!/usr/bin/env python3
"""Freeze the G9 numeric-track artifact: 128 units, 64 below / 64 above cutpoint.

Selection uses only source fields — validity, a non-null anchor, and a seeded
deterministic shuffle within each stratum. No target-model output participates.
Writes the artifact, its SHA-256, a freeze report, and the spot-audit sample.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import random
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import pandas as pd  # noqa: E402

from adapters.btf3_numeric import (  # noqa: E402
    ANCHOR,
    CUTPOINT,
    SOURCE_SHA256,
    build_candidate,
    validate_candidate_against_source,
    validate_source_row,
)
from information_set_schema import file_sha256  # noqa: E402

SELECTION_SEED = 20260901
AUDIT_SEED = 20260902
N_PER_STRATUM = 64
N_AUDIT = 32


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        default=ROOT / "data/external/raw/btf3/btf3_numeric_questions_and_forecasts.parquet",
    )
    parser.add_argument(
        "--out", type=Path, default=ROOT / "data/external/review/btf3_numeric_v1.jsonl"
    )
    parser.add_argument(
        "--report", type=Path, default=ROOT / "data/external/review/BTF3_NUMERIC_V1_FREEZE_REPORT.md"
    )
    parser.add_argument(
        "--audit-sample",
        type=Path,
        default=ROOT / "data/external/review/btf3_numeric_v1_audit_sample.json",
    )
    args = parser.parse_args()

    observed = file_sha256(args.source)
    if observed != SOURCE_SHA256:
        raise SystemExit(
            f"source hash mismatch: {observed} != pinned {SOURCE_SHA256}"
        )

    rows = pd.read_parquet(args.source).to_dict("records")
    valid, rejections = [], {}
    for row in rows:
        try:
            validate_source_row(row)
        except ValueError as exc:
            rejections[str(exc)] = rejections.get(str(exc), 0) + 1
            continue
        valid.append(row)

    eligible = [
        row
        for row in valid
        if row.get(ANCHOR) is not None and row[ANCHOR] == row[ANCHOR]
    ]
    below = [r for r in eligible if float(r["resolution"]) < float(r[CUTPOINT])]
    above = [r for r in eligible if float(r["resolution"]) > float(r[CUTPOINT])]
    if len(below) < N_PER_STRATUM or len(above) < N_PER_STRATUM:
        raise SystemExit(f"not enough units: below={len(below)} above={len(above)}")

    rng = random.Random(SELECTION_SEED)
    below = sorted(below, key=lambda r: str(r["question_id"]))
    above = sorted(above, key=lambda r: str(r["question_id"]))
    rng.shuffle(below)
    rng.shuffle(above)
    selected = below[:N_PER_STRATUM] + above[:N_PER_STRATUM]
    selected.sort(key=lambda r: str(r["question_id"]))

    items = []
    for row in selected:
        item = build_candidate(row)
        validate_candidate_against_source(item, row)
        items.append(item)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8") as handle:
        for item in items:
            handle.write(json.dumps(item.to_dict(), ensure_ascii=False, sort_keys=True) + "\n")
    digest = file_sha256(args.out)

    audit_rng = random.Random(AUDIT_SEED)
    audit = sorted(audit_rng.sample([i.independent_unit_id for i in items], N_AUDIT))
    args.audit_sample.write_text(
        json.dumps(
            {
                "artifact": str(args.out),
                "artifact_sha256": digest,
                "audit_seed": AUDIT_SEED,
                "n": N_AUDIT,
                "unit_ids": audit,
                "protocol": "PROTOCOL_BTF3_PACKET_FACTUALITY_AUDIT.md",
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    lines = [
        "# BTF-3 numeric v1 — freeze report",
        "",
        f"Source: `{args.source.name}`, SHA-256 `{observed}` (matches the pinned value).",
        f"Artifact: `{args.out}`  ",
        f"**Artifact SHA-256: `{digest}`**",
        "",
        "## Source filtering",
        "",
        f"- rows in source: {len(rows)}",
        f"- pass source validation: {len(valid)}",
        f"- also carry `{ANCHOR}`: {len(eligible)}",
        f"- below cutpoint: {len(below)}; above cutpoint: {len(above)}",
        "",
        "Rejections, by reason:",
        "",
    ]
    for reason, count in sorted(rejections.items(), key=lambda kv: -kv[1]):
        lines.append(f"- {count}: {reason}")
    lines += [
        "",
        "## Selection",
        "",
        f"{N_PER_STRATUM} below + {N_PER_STRATUM} above = {len(items)} units, by seeded "
        f"deterministic shuffle (seed `{SELECTION_SEED}`) within each stratum, over rows "
        "sorted by `question_id`. Selection uses only source fields; no target-model "
        "output participates.",
        "",
        "## Verification run on every candidate",
        "",
        "All four prompts of every selected unit were regenerated from the pinned source "
        "row and compared byte-for-byte; the later packet is absent from both WITHOUT "
        "prompts and present exactly once in each WITH prompt.",
        "",
        "## Review provenance",
        "",
        "This artifact has **automated validation plus a 32-item spot audit** "
        f"(seed `{AUDIT_SEED}`, ids in `{args.audit_sample.name}`) — not the per-item human "
        "review the 256-unit binary artifact received. It is reported as a replication in a "
        "second task type with lighter review provenance, per "
        "`PREREGISTRATION_G9_NUMERIC.md` §4.",
        "",
    ]
    args.report.write_text("\n".join(lines), encoding="utf-8")

    print(json.dumps({
        "units": len(items),
        "artifact_sha256": digest,
        "valid_rows": len(valid),
        "eligible_rows": len(eligible),
        "out": str(args.out),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
