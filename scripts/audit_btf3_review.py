#!/usr/bin/env python3
"""Fail-closed audit of a generated BTF-3 four-cell review artifact."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from adapters.btf3_temporal import (  # noqa: E402
    SOURCE_SHA256,
    validate_candidate_against_source,
)
from information_set_schema import InformationSetItem, validate_collection  # noqa: E402


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact", type=Path)
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("data/external/raw/btf3/btf3_binary_questions_and_forecasts.parquet"),
    )
    parser.add_argument("--expected-count", type=int, default=8)
    parser.add_argument("--expected-per-resolution", type=int, default=4)
    parser.add_argument("--exclude-question-id", action="append", default=[])
    parser.add_argument("--require-question-id", action="append", default=[])
    args = parser.parse_args()

    actual_sha = sha256(args.source)
    if actual_sha != SOURCE_SHA256:
        raise ValueError(f"source SHA-256 mismatch: {actual_sha}")

    items = [
        InformationSetItem.from_dict(json.loads(line))
        for line in args.artifact.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    validate_collection(items)
    if len(items) != args.expected_count:
        raise ValueError(f"expected {args.expected_count} items, found {len(items)}")

    frame = pd.read_parquet(args.source)
    source_rows = {str(row["question_id"]): row for row in frame.to_dict("records")}
    ids = [item.independent_unit_id for item in items]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate independent_unit_id in artifact")

    excluded = set(args.exclude_question_id)
    required = set(args.require_question_id)
    if excluded & set(ids):
        raise ValueError(f"rejected IDs re-entered artifact: {sorted(excluded & set(ids))}")
    if not required <= set(ids):
        raise ValueError(f"required IDs missing: {sorted(required - set(ids))}")

    counts = {0: 0, 1: 0}
    for item in items:
        try:
            row = source_rows[item.independent_unit_id]
        except KeyError as error:
            raise ValueError(f"artifact ID absent from pinned source: {item.independent_unit_id}") from error
        validate_candidate_against_source(item, row)
        counts[int(float(row["resolution"]))] += 1
    expected_counts = {0: args.expected_per_resolution, 1: args.expected_per_resolution}
    if counts != expected_counts:
        raise ValueError(f"resolution imbalance: {counts} != {expected_counts}")

    report = {
        "artifact": str(args.artifact),
        "artifact_sha256": sha256(args.artifact),
        "source_sha256": actual_sha,
        "items": len(items),
        "independent_units": len(set(ids)),
        "resolution_counts": counts,
        "excluded_ids_absent": sorted(excluded),
        "required_ids_present": sorted(required),
        "schema_validation": "PASS",
        "exact_source_transform_validation": "PASS",
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
