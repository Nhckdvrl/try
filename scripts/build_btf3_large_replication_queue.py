#!/usr/bin/env python3
"""Freeze the immutable candidate queue for BTF-3 Large Replication v1.

This freezes *order*, not membership: the complete eligible pool is written out
once, per realized-outcome bucket, in fixed SHA-256 hash order. Human review
then walks that order until 128 ACCEPTs per bucket, so no reviewer choice, pool
regrow, or resample can ever enter selection.

Nothing here inspects any target-model output, and no prompt semantics change:
prompts are still built by the unchanged adapters.btf3_temporal transform at
freeze time.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from adapters.btf3_large_replication import (  # noqa: E402
    QUOTA_PER_RESOLUTION,
    ROUND_ID,
    SEED,
    build_exclusion_universe,
    eligible_rows,
    file_sha256,
    full_deterministic_queue,
    normalize_question,
    order_key,
    render_review_chunk,
)
from adapters.btf3_temporal import SOURCE_SHA256  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("data/external/raw/btf3/btf3_binary_questions_and_forecasts.parquet"),
    )
    parser.add_argument("--pilot-jsonl", type=Path, default=Path("data/external/review/btf3_temporal_pilot_v0.2r2.jsonl"))
    parser.add_argument("--confirmatory-jsonl", type=Path, default=Path("data/external/review/btf3_temporal_confirmatory_v1.jsonl"))
    parser.add_argument("--prior-candidates-json", type=Path, default=Path("data/external/review/btf3_confirmatory_v1_candidates.json"))
    parser.add_argument("--prior-reviewed-md", type=Path, default=Path("data/external/review/btf3_confirmatory_v1_reviewed.md"))
    parser.add_argument("--quota-per-resolution", type=int, default=QUOTA_PER_RESOLUTION)
    parser.add_argument("--seed", type=int, default=SEED)
    parser.add_argument("--chunk-size", type=int, default=64, help="review display chunk size (presentation only)")
    parser.add_argument(
        "--render-chunks",
        type=int,
        default=4,
        help="how many leading chunks per bucket to render now; more can be rendered later from the same frozen queue",
    )
    parser.add_argument("--output-dir", type=Path, default=Path("data/external/review"))
    args = parser.parse_args()

    source_sha = file_sha256(args.source)
    if source_sha != SOURCE_SHA256:
        raise ValueError(f"source SHA-256 mismatch: {source_sha} != pinned {SOURCE_SHA256}")

    frame = pd.read_parquet(args.source)
    exclusions = build_exclusion_universe(
        pilot_jsonl=args.pilot_jsonl,
        confirmatory_jsonl=args.confirmatory_jsonl,
        prior_candidates_json=args.prior_candidates_json,
        prior_reviewed_md=args.prior_reviewed_md,
    )
    by_id = {str(row["question_id"]): row for row in eligible_rows(frame)}
    prior_used_questions = {
        normalize_question(by_id[qid]["question"])
        for qid in set(exclusions["categories"]["pilot_v0_2r2"])
        | set(exclusions["categories"]["confirmatory_v1_frozen"])
        if qid in by_id
    }

    built = full_deterministic_queue(
        frame,
        seed=args.seed,
        exclude_question_ids=exclusions["union"],
        exclude_normalized_questions=prior_used_questions,
    )
    queue = built["queue"]
    for resolution, rows in queue.items():
        if len(rows) < args.quota_per_resolution:
            raise ValueError(
                f"resolution={resolution} has only {len(rows)} eligible candidates, "
                f"below the quota {args.quota_per_resolution}; the round stops here "
                "(no eligibility gate may be relaxed)"
            )

    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    buckets = {0: "NO", 1: "YES"}
    queue_files: dict[str, dict[str, object]] = {}
    for resolution, label in buckets.items():
        rows = queue[resolution]
        path = output / f"{ROUND_ID}_{label.lower()}_queue.json"
        payload = {
            "round_id": ROUND_ID,
            "bucket": label,
            "realized_resolution": resolution,
            "seed": args.seed,
            "quota": args.quota_per_resolution,
            "n_candidates": len(rows),
            "order": [
                {
                    "position": index,
                    "question_id": str(row["question_id"]),
                    "order_key": order_key(str(row["question_id"]), seed=args.seed),
                }
                for index, row in enumerate(rows, 1)
            ],
        }
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        queue_files[label] = {"path": str(path), "n_candidates": len(rows), "sha256": file_sha256(path)}

        rendered = []
        for chunk_index in range(args.render_chunks):
            start = chunk_index * args.chunk_size
            chunk_rows = rows[start : start + args.chunk_size]
            if not chunk_rows:
                break
            chunk_path = output / (
                f"{ROUND_ID}_{label.lower()}_review_"
                f"{start + 1:03d}-{start + len(chunk_rows):03d}.md"
            )
            chunk_path.write_text(
                render_review_chunk(
                    chunk_rows,
                    bucket_label=label,
                    start_index=start + 1,
                    quota_per_resolution=args.quota_per_resolution,
                ),
                encoding="utf-8",
            )
            rendered.append({"path": str(chunk_path), "sha256": file_sha256(chunk_path)})
        queue_files[label]["rendered_review_chunks"] = rendered

    manifest_path = output / f"{ROUND_ID}_queue.json"
    manifest = {
        "round_id": ROUND_ID,
        "seed": args.seed,
        "quota_per_resolution": args.quota_per_resolution,
        "chunk_size": args.chunk_size,
        "source": {
            "path": str(args.source),
            "sha256": source_sha,
            "file": "btf3_binary_questions_and_forecasts.parquet",
        },
        "exclusions": exclusions,
        "automatic_eligibility": {
            "contract": "BTF3_TRANSFORMATION_CONTRACT.md#automatic-eligibility-checks",
            "eligible_rows_in_source": len(by_id),
        },
        "hard_duplicate_rule": {
            "definition": "identical whitespace-collapsed casefolded question text",
            "resolution": "earlier global hash rank kept, later occurrences dropped before review",
            "dropped_within_round": built["dropped_duplicate_within_round"],
            "dropped_against_prior_rounds": built["dropped_duplicate_against_prior_rounds"],
        },
        "queues": queue_files,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    # The manifest's own digest, recorded beside it so the frozen queue can be
    # verified later without re-deriving it.
    digest_path = output / f"{ROUND_ID}_queue.sha256"
    digest_path.write_text(f"{file_sha256(manifest_path)}  {manifest_path.name}\n", encoding="utf-8")

    print(json.dumps({label: info["n_candidates"] for label, info in queue_files.items()}, indent=2))
    print(f"wrote {manifest_path} (sha256 in {digest_path})")
    print("no items are frozen yet — human review in queue order, then scripts/freeze_btf3_large_replication.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
