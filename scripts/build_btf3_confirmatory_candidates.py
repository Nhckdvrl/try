#!/usr/bin/env python3
"""Generate the BTF-3 confirmatory candidate queue for streamlined human review.

This does not freeze anything. It emits, before any human review, a fixed
deterministic per-resolution candidate order (larger than the target quota)
plus a companion machine-readable queue file. The queue order is what
scripts/freeze_btf3_confirmatory.py later walks to take the first N accepts
per bucket -- nothing about the queue order may change after review starts.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from adapters.btf3_temporal import (  # noqa: E402
    deterministic_candidate_queue,
    render_confirmatory_queue,
)

# Same two source units the pilot rejected after human review; permanently
# excluded from every later BTF-3 selection round regardless of pool size.
DEFAULT_REJECTED = [
    "b6fc94e7-a0b9-56b6-87a1-ba94f29781e9",
    "34d3588a-ffb0-5290-b964-bceb68be18f1",
]

# The eight pilot units (btf3_temporal_pilot_v0.2r2.jsonl) already had model
# output observed against them in g1-pilot-freeze-v1.2; they must never
# re-enter primary confirmatory selection.
PILOT_QUESTION_IDS = [
    "0c1f9c71-e9da-5093-9eb8-05244ca3f49e",
    "4181856c-d761-5721-a7dc-a4698f1fb1ac",
    "482705b8-b542-5934-abed-599fd4d27302",
    "84569bb0-4029-5ddd-9ce5-b787dc0d41e0",
    "b0102690-c6ec-5482-8452-0151f77289b9",
    "b92bacb5-8086-5dd2-a64f-9ec00c427248",
    "d72e1700-1552-5775-83d9-80ba7723f068",
    "e6927299-6264-5334-be53-ec3a46dd0e78",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="data/external/raw/btf3/btf3_binary_questions_and_forecasts.parquet")
    parser.add_argument("--pool-size", type=int, default=64, help="candidates per resolution bucket, ahead of the quota")
    parser.add_argument("--quota-per-resolution", type=int, default=32)
    parser.add_argument("--seed", type=int, default=20260830)
    parser.add_argument("--artifact-label", default="confirmatory_v1")
    parser.add_argument("--output-dir", default="data/external/review")
    parser.add_argument("--exclude-question-id", action="append", default=None)
    parser.add_argument(
        "--pilot-question-id",
        action="append",
        default=None,
        help="Pilot question IDs to exclude. Defaults to the 8 pilot IDs already used in v1.2.",
    )
    args = parser.parse_args()

    pilot_ids = args.pilot_question_id if args.pilot_question_id is not None else PILOT_QUESTION_IDS
    if len(pilot_ids) != 8:
        raise ValueError(
            f"expected all 8 pilot question IDs to be excluded, got {len(pilot_ids)}; "
            "pass --pilot-question-id for each of the 8 btf3_temporal_pilot_v0.2r2.jsonl IDs"
        )
    exclusions = (args.exclude_question_id or DEFAULT_REJECTED) + pilot_ids

    frame = pd.read_parquet(args.source)
    queue = deterministic_candidate_queue(
        frame,
        pool_size=args.pool_size,
        seed=args.seed,
        exclude_question_ids=exclusions,
    )
    for resolution, rows in queue.items():
        if len(rows) < args.quota_per_resolution:
            raise ValueError(
                f"resolution={resolution} pool has only {len(rows)} candidates, "
                f"below the quota {args.quota_per_resolution}; raise --pool-size"
            )

    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    markdown = output / f"btf3_{args.artifact_label}_candidates.md"
    manifest = output / f"btf3_{args.artifact_label}_candidates.json"

    markdown.write_text(
        render_confirmatory_queue(
            queue, artifact_label=args.artifact_label, quota_per_resolution=args.quota_per_resolution
        ),
        encoding="utf-8",
    )
    manifest.write_text(
        json.dumps(
            {
                "source": args.source,
                "pool_size": args.pool_size,
                "quota_per_resolution": args.quota_per_resolution,
                "seed": args.seed,
                "excluded_question_ids": sorted(set(exclusions)),
                "queue": {
                    str(resolution): [str(row["question_id"]) for row in rows]
                    for resolution, rows in queue.items()
                },
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"wrote candidate queue to {markdown} and {manifest}")
    for resolution, rows in queue.items():
        print(f"  resolution={resolution}: {len(rows)} candidates queued")
    print("no items are frozen yet -- human review, then run scripts/freeze_btf3_confirmatory.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
