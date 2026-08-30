#!/usr/bin/env python3
"""Freeze the BTF-3 Large Replication v1 artifact (128 YES + 128 NO).

Walks each bucket's immutable queue in its frozen order and takes the first 128
ACCEPTs. Refuses to emit a partial, reordered, or resampled artifact: a bucket
that has not reached quota from the decisions recorded so far fails loudly with
how many more reviewed candidates are needed.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from adapters.btf3_large_replication import (  # noqa: E402
    QUOTA_PER_RESOLUTION,
    ROUND_ID,
    file_sha256,
)
from adapters.btf3_temporal import build_candidate  # noqa: E402
from information_set_schema import validate_collection  # noqa: E402
from freeze_btf3_confirmatory import parse_decisions  # noqa: E402


def load_decisions(paths: list[Path]) -> dict[str, tuple[str, str]]:
    decisions: dict[str, tuple[str, str]] = {}
    for path in paths:
        for qid, verdict in parse_decisions(path.read_text(encoding="utf-8")).items():
            if qid in decisions and decisions[qid] != verdict:
                raise ValueError(f"conflicting recorded decisions for {qid}")
            decisions[qid] = verdict
    return decisions


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=Path(f"data/external/review/{ROUND_ID}_queue.json"))
    parser.add_argument("--reviewed", type=Path, nargs="+", required=True, help="reviewed review-chunk markdown files")
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("data/external/raw/btf3/btf3_binary_questions_and_forecasts.parquet"),
    )
    parser.add_argument("--quota-per-resolution", type=int, default=QUOTA_PER_RESOLUTION)
    parser.add_argument("--output-dir", type=Path, default=Path("data/external/review"))
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    digest_path = args.manifest.with_suffix(".sha256")
    if digest_path.exists():
        recorded = digest_path.read_text(encoding="utf-8").split()[0]
        actual = file_sha256(args.manifest)
        if recorded != actual:
            raise ValueError(f"queue manifest changed after freeze: {actual} != recorded {recorded}")
    if manifest["quota_per_resolution"] != args.quota_per_resolution:
        raise ValueError("quota mismatch between manifest and freeze invocation")

    decisions = load_decisions(list(args.reviewed))
    accepted_by_bucket: dict[str, list[str]] = {}
    reject_log: list[str] = []
    reviewed_prefix: dict[str, int] = {}
    shortfall: dict[str, int] = {}
    for label, info in manifest["queues"].items():
        queue = json.loads(Path(info["path"]).read_text(encoding="utf-8"))
        if file_sha256(Path(info["path"])) != info["sha256"]:
            raise ValueError(f"{label} queue file changed after freeze")
        accepted: list[str] = []
        consumed = 0
        for entry in queue["order"]:
            if len(accepted) >= args.quota_per_resolution:
                break
            qid = entry["question_id"]
            if qid not in decisions:
                break
            consumed += 1
            decision, reason = decisions[qid]
            if decision == "ACCEPT":
                accepted.append(qid)
            else:
                reject_log.append(f"- `{qid}` ({label}-{entry['position']}): {decision} — {reason}")
        accepted_by_bucket[label] = accepted
        reviewed_prefix[label] = consumed
        if len(accepted) < args.quota_per_resolution:
            shortfall[label] = args.quota_per_resolution - len(accepted)

    if shortfall:
        raise ValueError(
            f"quota not reached from recorded decisions: {shortfall} more ACCEPTs needed per bucket. "
            "Render and review the next chunk of the SAME frozen queue — never reorder, resample, "
            "or revisit an already-decided candidate."
        )

    unexpected = set(decisions) - {
        entry["question_id"]
        for info in manifest["queues"].values()
        for entry in json.loads(Path(info["path"]).read_text(encoding="utf-8"))["order"]
    }
    if unexpected:
        raise ValueError(f"decisions recorded for candidates outside the frozen queue: {sorted(unexpected)}")

    frame = pd.read_parquet(args.source)
    rows_by_id = {str(row["question_id"]): row for row in frame.to_dict("records")}
    accepted_ids = [qid for label in sorted(accepted_by_bucket) for qid in accepted_by_bucket[label]]
    rows = [rows_by_id[qid] for qid in accepted_ids]
    items = [build_candidate(row) for row in rows]
    validate_collection(items)

    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    jsonl = output / "btf3_temporal_large_replication_v1.jsonl"
    jsonl.write_text("".join(item.to_json() + "\n" for item in items), encoding="utf-8")

    counts = {
        "YES": sum(1 for row in rows if int(float(row["resolution"])) == 1),
        "NO": sum(1 for row in rows if int(float(row["resolution"])) == 0),
    }
    verdict = output / "btf3_temporal_large_replication_v1_verdict.md"
    lines = [
        "# BTF-3 Large Replication v1 — freeze verdict",
        "",
        f"- accepted: {len(items)} ({counts['YES']} YES / {counts['NO']} NO)",
        f"- quota per realized outcome: {args.quota_per_resolution}",
        f"- queue prefix consumed: " + ", ".join(f"{label}-1..{n}" for label, n in sorted(reviewed_prefix.items())),
        f"- rejected/unsure inside the consumed prefix: {len(reject_log)}",
        f"- artifact SHA-256: `{file_sha256(jsonl)}`",
        "",
        "## Rejections and reasons",
        "",
    ]
    lines.extend(reject_log or ["(none)"])
    verdict.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"wrote {len(items)} frozen units to {jsonl}")
    print(json.dumps({"counts": counts, "reviewed_prefix": reviewed_prefix, "rejects": len(reject_log)}, indent=2))
    print(f"artifact sha256: {file_sha256(jsonl)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
