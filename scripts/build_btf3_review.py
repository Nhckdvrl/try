#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from adapters.btf3_temporal import (
    build_candidate,
    deterministic_review_sample,
    render_review,
    validate_candidate_against_source,
)
from information_set_schema import validate_collection


DEFAULT_REJECTED = [
    # v0.1: correct outcome, but the packet gives the wrong tournament end date.
    "b6fc94e7-a0b9-56b6-87a1-ba94f29781e9",
    # v0.2: correct outcome, but the packet claims a late-July recess precluded
    # a late-June committee report.  Preserve the artifact; reject the unit.
    "34d3588a-ffb0-5290-b964-bceb68be18f1",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="data/external/raw/btf3/btf3_binary_questions_and_forecasts.parquet")
    parser.add_argument("--n-per-resolution", type=int, default=4)
    parser.add_argument("--seed", type=int, default=20260829)
    parser.add_argument("--output-dir", default="data/external/review")
    parser.add_argument(
        "--exclude-question-id",
        action="append",
        default=None,
        help=(
            "Question ID to exclude from deterministic selection. May be repeated. "
            "If omitted, all source units rejected in the v0.1 and v0.2 "
            "human audits are excluded."
        ),
    )
    args = parser.parse_args()

    exclusions = DEFAULT_REJECTED if args.exclude_question_id is None else args.exclude_question_id

    frame = pd.read_parquet(args.source)
    rows = deterministic_review_sample(
        frame,
        n_per_resolution=args.n_per_resolution,
        seed=args.seed,
        exclude_question_ids=exclusions,
    )
    items = [build_candidate(row) for row in rows]
    validate_collection(items)
    for item, row in zip(items, rows, strict=True):
        validate_candidate_against_source(item, row)

    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    # v0.2 is an immutable failed replacement round.  v0.2r2 uses the same
    # corrected transformation, but selects a second replacement source unit.
    jsonl = output / "btf3_temporal_pilot_v0.2r2.jsonl"
    markdown = output / "btf3_temporal_pilot_v0.2r2.md"
    jsonl.write_text("".join(item.to_json() + "\n" for item in items), encoding="utf-8")
    markdown.write_text(render_review(items, rows, artifact_label="v0.2r2"), encoding="utf-8")
    print(f"wrote {len(items)} review candidates to {jsonl} and {markdown}")
    if exclusions:
        print("excluded question IDs:", ", ".join(exclusions))
    print("human review is still required before any model run")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
