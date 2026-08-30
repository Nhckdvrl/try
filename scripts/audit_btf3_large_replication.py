#!/usr/bin/env python3
"""Fail-closed audit of the frozen BTF-3 Large Replication v1 artifact.

Every check is a hard gate. The script exits non-zero on the first failure and
writes BTF3_LARGE_REPLICATION_V1_FREEZE_REPORT.md only when all checks pass, so
the freeze report cannot exist for an artifact that failed audit.
"""
from __future__ import annotations

import argparse
import json
from math import isfinite
from pathlib import Path
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from adapters.btf3_large_replication import (  # noqa: E402
    QUOTA_PER_RESOLUTION,
    ROUND_ID,
    build_exclusion_universe,
    file_sha256,
    normalize_question,
)
from adapters.btf3_temporal import SOURCE_SHA256, validate_candidate_against_source  # noqa: E402
from information_set_schema import InformationSetItem, validate_collection  # noqa: E402
from freeze_btf3_large_replication import load_decisions  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact", type=Path, nargs="?", default=Path("data/external/review/btf3_temporal_large_replication_v1.jsonl"))
    parser.add_argument("--manifest", type=Path, default=Path(f"data/external/review/{ROUND_ID}_queue.json"))
    parser.add_argument("--reviewed", type=Path, nargs="+", required=True)
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("data/external/raw/btf3/btf3_binary_questions_and_forecasts.parquet"),
    )
    parser.add_argument("--pilot-jsonl", type=Path, default=Path("data/external/review/btf3_temporal_pilot_v0.2r2.jsonl"))
    parser.add_argument("--confirmatory-jsonl", type=Path, default=Path("data/external/review/btf3_temporal_confirmatory_v1.jsonl"))
    parser.add_argument("--prior-candidates-json", type=Path, default=Path("data/external/review/btf3_confirmatory_v1_candidates.json"))
    parser.add_argument("--prior-reviewed-md", type=Path, default=Path("data/external/review/btf3_confirmatory_v1_reviewed.md"))
    parser.add_argument("--expected-count", type=int, default=2 * QUOTA_PER_RESOLUTION)
    parser.add_argument("--expected-per-resolution", type=int, default=QUOTA_PER_RESOLUTION)
    parser.add_argument("--report", type=Path, default=Path("data/external/review/BTF3_LARGE_REPLICATION_V1_FREEZE_REPORT.md"))
    args = parser.parse_args()

    checks: list[tuple[str, str]] = []

    def gate(name: str, ok: bool, detail: str) -> None:
        if not ok:
            raise ValueError(f"AUDIT FAILED — {name}: {detail}")
        checks.append((name, detail))

    source_sha = file_sha256(args.source)
    gate("source SHA-256 matches the pinned revision", source_sha == SOURCE_SHA256, source_sha)

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    digest_path = args.manifest.with_suffix(".sha256")
    manifest_sha = file_sha256(args.manifest)
    gate(
        "queue manifest SHA-256 unchanged since queue freeze",
        digest_path.exists() and digest_path.read_text(encoding="utf-8").split()[0] == manifest_sha,
        manifest_sha,
    )
    for label, info in manifest["queues"].items():
        gate(
            f"{label} queue file unchanged since queue freeze",
            file_sha256(Path(info["path"])) == info["sha256"],
            info["sha256"],
        )

    items = [
        InformationSetItem.from_dict(json.loads(line))
        for line in args.artifact.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    validate_collection(items)
    checks.append(("schema validation", "PASS"))
    gate("exact item count", len(items) == args.expected_count, f"{len(items)}")

    ids = [item.independent_unit_id for item in items]
    gate("unique independent units", len(ids) == len(set(ids)), f"{len(set(ids))} unique")

    exclusions = build_exclusion_universe(
        pilot_jsonl=args.pilot_jsonl,
        confirmatory_jsonl=args.confirmatory_jsonl,
        prior_candidates_json=args.prior_candidates_json,
        prior_reviewed_md=args.prior_reviewed_md,
    )
    for name, excluded in exclusions["categories"].items():
        overlap = sorted(set(excluded) & set(ids))
        gate(f"zero overlap with {name}", not overlap, f"0 of {len(excluded)} excluded IDs present")

    # Independently re-derive the selection from the frozen queue order and the
    # recorded decisions: the artifact must be exactly the first-N ACCEPT prefix.
    decisions = load_decisions(list(args.reviewed))
    expected_ids: list[str] = []
    for label, info in sorted(manifest["queues"].items()):
        queue = json.loads(Path(info["path"]).read_text(encoding="utf-8"))
        accepted: list[str] = []
        for entry in queue["order"]:
            if len(accepted) >= args.expected_per_resolution:
                break
            qid = entry["question_id"]
            if qid not in decisions:
                break
            if decisions[qid][0] == "ACCEPT":
                accepted.append(qid)
        gate(
            f"{label} bucket reached quota in frozen queue order",
            len(accepted) == args.expected_per_resolution,
            f"{len(accepted)} ACCEPTs",
        )
        expected_ids.extend(accepted)
    gate(
        "artifact is exactly the first-N ACCEPT prefix of the frozen queue",
        sorted(expected_ids) == sorted(ids),
        f"{len(expected_ids)} IDs re-derived independently",
    )

    frame = pd.read_parquet(args.source)
    source_rows = {str(row["question_id"]): row for row in frame.to_dict("records")}
    counts = {0: 0, 1: 0}
    normalized: dict[str, str] = {}
    for item in items:
        row = source_rows.get(item.independent_unit_id)
        if row is None:
            raise ValueError(f"AUDIT FAILED — artifact ID absent from pinned source: {item.independent_unit_id}")
        validate_candidate_against_source(item, row)
        resolution = int(float(row["resolution"]))
        counts[resolution] += 1
        sign = int(item.reference_context["outcome_alignment_sign"])
        if sign != (1 if resolution == 1 else -1):
            raise ValueError(f"AUDIT FAILED — outcome sign mapping for {item.independent_unit_id}")
        if int(item.reference_context["realized_resolution"]) != resolution:
            raise ValueError(f"AUDIT FAILED — realized_resolution mismatch for {item.independent_unit_id}")
        for variant in (item.oob_variant, item.admissible_variant):
            for key in ("without_information_prompt", "with_information_prompt"):
                text = variant[key]
                if not isinstance(text, str) or not text.strip():
                    raise ValueError(f"AUDIT FAILED — empty prompt cell for {item.independent_unit_id}")
                if "nan" == text.strip().lower() or not isfinite(len(text)):
                    raise ValueError(f"AUDIT FAILED — malformed prompt cell for {item.independent_unit_id}")
        norm = normalize_question(row["question"])
        if norm in normalized:
            raise ValueError(
                f"AUDIT FAILED — duplicate normalized question: {item.independent_unit_id} vs {normalized[norm]}"
            )
        normalized[norm] = item.independent_unit_id
    checks.append(("four prompt cells present, exact-transform and packet-leakage validation", "PASS (all items)"))
    checks.append(("outcome sign mapping and realized_resolution", "PASS (all items)"))
    checks.append(("no duplicate normalized question", f"{len(normalized)} distinct questions"))
    gate(
        "realized-outcome balance",
        counts == {0: args.expected_per_resolution, 1: args.expected_per_resolution},
        f"{counts[1]} YES / {counts[0]} NO",
    )

    artifact_sha = file_sha256(args.artifact)
    report = [
        "# BTF-3 Large Replication v1 — freeze report",
        "",
        f"- artifact: `{args.artifact}`",
        f"- artifact SHA-256: `{artifact_sha}`",
        f"- source: `{args.source}` (SHA-256 `{source_sha}`)",
        f"- queue manifest: `{args.manifest}` (SHA-256 `{manifest_sha}`)",
        f"- units: {len(items)} ({counts[1]} realized YES / {counts[0]} realized NO)",
        "",
        "Every check below is fail-closed: this report is only written when all of them pass.",
        "",
        "| check | detail |",
        "|---|---|",
    ]
    report.extend(f"| {name} | {detail} |" for name, detail in checks)
    report.extend([
        "",
        "No target-model output was inspected or generated at any point in selection, review, "
        "freeze, or audit for this round.",
        "",
    ])
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text("\n".join(report), encoding="utf-8")
    print(json.dumps({"artifact_sha256": artifact_sha, "units": len(items), "yes": counts[1], "no": counts[0], "checks": len(checks)}, indent=2))
    print(f"wrote {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
