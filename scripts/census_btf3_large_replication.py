#!/usr/bin/env python3
"""Mechanical census of the BTF-3 pool before any Large Replication v1 sampling.

This runs *before* the queue is built and answers one question only: does a
strictly-fresh, automatically-eligible pool of at least 128 realized-YES and
128 realized-NO candidates exist at all? If it does not, the round stops — no
eligibility gate may be relaxed to reach the quota.

It writes results/btf3_large_replication_pool_census.json and exits non-zero
when the hard floor is not met.
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
    SEED,
    build_exclusion_universe,
    eligible_rows,
    file_sha256,
    full_deterministic_queue,
    normalize_question,
)
from adapters.btf3_temporal import SOURCE_SHA256, validate_source_row  # noqa: E402


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
    parser.add_argument("--out", type=Path, default=Path("results/btf3_large_replication_pool_census.json"))
    args = parser.parse_args()

    source_sha = file_sha256(args.source)
    if source_sha != SOURCE_SHA256:
        raise ValueError(f"source SHA-256 mismatch: {source_sha} != pinned {SOURCE_SHA256}")

    frame = pd.read_parquet(args.source)
    records = frame.to_dict("records")
    raw_total = len(records)
    raw_by_resolution = {"0": 0, "1": 0}
    schema_failures = 0
    for row in records:
        try:
            validate_source_row(row)
        except ValueError:
            schema_failures += 1
            continue
        raw_by_resolution[str(int(float(row["resolution"])))] += 1

    eligible = eligible_rows(frame)
    exclusions = build_exclusion_universe(
        pilot_jsonl=args.pilot_jsonl,
        confirmatory_jsonl=args.confirmatory_jsonl,
        prior_candidates_json=args.prior_candidates_json,
        prior_reviewed_md=args.prior_reviewed_md,
    )

    # Sequential funnel: each step reports what is *left* after applying that
    # exclusion category on top of the previous ones, in the fixed order below.
    funnel_order = [
        "pilot_v0_2r2",
        "confirmatory_v1_frozen",
        "confirmatory_v1_candidate_queue",
        "confirmatory_v1_review_reject_or_unsure",
        "historical_pilot_rejects",
    ]
    remaining = {str(row["question_id"]) for row in eligible}
    funnel = [{"step": "automatic_eligibility", "remaining": len(remaining)}]
    applied: set[str] = set()
    for name in funnel_order:
        applied |= set(exclusions["categories"][name])
        remaining -= set(exclusions["categories"][name])
        funnel.append({"step": f"minus_{name}", "remaining": len(remaining)})

    prior_used_questions = set()
    prior_used_ids = set(exclusions["categories"]["pilot_v0_2r2"]) | set(
        exclusions["categories"]["confirmatory_v1_frozen"]
    )
    by_id = {str(row["question_id"]): row for row in eligible}
    for qid in prior_used_ids:
        if qid in by_id:
            prior_used_questions.add(normalize_question(by_id[qid]["question"]))

    built = full_deterministic_queue(
        frame,
        seed=args.seed,
        exclude_question_ids=exclusions["union"],
        exclude_normalized_questions=prior_used_questions,
    )
    queue = built["queue"]
    counts = {"0": len(queue[0]), "1": len(queue[1])}
    funnel.append({"step": "minus_hard_duplicate_questions", "remaining": counts["0"] + counts["1"]})

    # Duplicate structure of the *raw* eligible pool, reported for the record.
    norm_counts: dict[str, int] = {}
    for row in eligible:
        norm_counts[normalize_question(row["question"])] = (
            norm_counts.get(normalize_question(row["question"]), 0) + 1
        )
    raw_duplicate_groups = sum(1 for count in norm_counts.values() if count > 1)
    raw_duplicate_rows = sum(count for count in norm_counts.values() if count > 1)

    quota_met = counts["0"] >= args.quota_per_resolution and counts["1"] >= args.quota_per_resolution
    census = {
        "round_id": "btf3_large_replication_v1",
        "seed": args.seed,
        "quota_per_resolution": args.quota_per_resolution,
        "source": {"path": str(args.source), "sha256": source_sha},
        "raw_pool": {
            "total_rows": raw_total,
            "automatic_eligibility_failures": schema_failures,
            "eligible_total": len(eligible),
            "eligible_realized_no": raw_by_resolution["0"],
            "eligible_realized_yes": raw_by_resolution["1"],
            "exact_normalized_question_duplicate_groups": raw_duplicate_groups,
            "exact_normalized_question_duplicate_rows": raw_duplicate_rows,
        },
        "exclusions": {
            "category_counts": exclusions["category_counts"],
            "union_count": exclusions["union_count"],
            "sources": exclusions["sources"],
        },
        "funnel": funnel,
        "final_eligible": {
            "realized_no": counts["0"],
            "realized_yes": counts["1"],
            "total": counts["0"] + counts["1"],
            "dropped_duplicate_within_round": len(built["dropped_duplicate_within_round"]),
            "dropped_duplicate_against_prior_rounds": len(built["dropped_duplicate_against_prior_rounds"]),
        },
        "hard_gate": {
            "requirement": "at least quota_per_resolution eligible candidates in EACH realized-outcome bucket",
            "realized_no_ok": counts["0"] >= args.quota_per_resolution,
            "realized_yes_ok": counts["1"] >= args.quota_per_resolution,
            "passed": quota_met,
        },
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(census, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(census["final_eligible"] | census["hard_gate"], indent=2, sort_keys=True))
    print(f"wrote {args.out}")
    if not quota_met:
        print(
            "HARD GATE FAILED: the strictly-fresh eligible pool cannot supply the quota. "
            "Stop. Do not relax any eligibility gate to reach 128 per bucket.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
