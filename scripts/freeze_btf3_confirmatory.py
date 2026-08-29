#!/usr/bin/env python3
"""Freeze the BTF-3 confirmatory artifact from a reviewed candidate queue.

Reads the fixed queue order from the candidates manifest (never resampled)
and the human decisions from the reviewed markdown, walks each resolution
bucket in queue order, and takes the first N ACCEPTs per bucket. Refuses to
produce a partial or reordered artifact: if a bucket does not reach quota
from decisions recorded so far, it fails loudly with how many more reviewed
candidates are needed, rather than silently reordering or resampling.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from adapters.btf3_temporal import build_candidate, render_review  # noqa: E402
from information_set_schema import validate_collection  # noqa: E402


_DECISION = re.compile(
    r"^\s*-\s*Decision:\s*`\[([ xX])\]\s*ACCEPT\s*\[([ xX])\]\s*REJECT\s*\[([ xX])\]\s*UNSURE`\s*$"
)
_REASON = re.compile(
    r"^\s*-\s*Reason(?:\s*\(required for REJECT/UNSURE, one line\))?:\s*(.*)$"
)
_HEADING = re.compile(r"^### (?:YES|NO)-\d+\. `([^`]+)`\s*$")


def parse_decisions(markdown: str) -> dict[str, tuple[str, str]]:
    """Return {question_id: (decision, reason)} for every reviewed candidate."""
    decisions: dict[str, tuple[str, str]] = {}
    current_qid: str | None = None
    pending_reason: str | None = None
    lines = markdown.splitlines()
    for index, line in enumerate(lines):
        heading = _HEADING.match(line)
        if heading:
            current_qid = heading.group(1)
            continue
        match = _DECISION.match(line)
        if match and current_qid is not None:
            marks = [group.strip().lower() == "x" for group in match.groups()]
            if sum(marks) != 1:
                raise ValueError(f"{current_qid}: exactly one of ACCEPT/REJECT/UNSURE must be ticked")
            decision = ("ACCEPT", "REJECT", "UNSURE")[marks.index(True)]
            reason = ""
            for follow in lines[index + 1 : index + 4]:
                reason_match = _REASON.match(follow)
                if reason_match:
                    reason = reason_match.group(1).strip()
                    break
            if decision != "ACCEPT" and not reason:
                raise ValueError(f"{current_qid}: {decision} requires a one-line reason")
            decisions[current_qid] = (decision, reason)
            current_qid = None
    return decisions


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True, help="*_candidates.json from build_btf3_confirmatory_candidates.py")
    parser.add_argument("--reviewed", type=Path, required=True, help="reviewed *_candidates.md with decisions filled in")
    parser.add_argument("--source", default="data/external/raw/btf3/btf3_binary_questions_and_forecasts.parquet")
    parser.add_argument("--artifact-label", default="confirmatory_v1")
    parser.add_argument("--output-dir", default="data/external/review")
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    quota = manifest["quota_per_resolution"]
    queue = manifest["queue"]
    decisions = parse_decisions(args.reviewed.read_text(encoding="utf-8"))

    accepted_ids: list[str] = []
    reject_log: list[str] = []
    shortfall: dict[str, int] = {}
    for resolution_key, ordered_ids in queue.items():
        accepted_this_bucket: list[str] = []
        for qid in ordered_ids:
            if len(accepted_this_bucket) >= quota:
                break
            if qid not in decisions:
                raise ValueError(f"queue candidate {qid} (resolution={resolution_key}) has no recorded decision")
            decision, reason = decisions[qid]
            if decision == "ACCEPT":
                accepted_this_bucket.append(qid)
            else:
                reject_log.append(f"- `{qid}` (resolution={resolution_key}): {decision} — {reason}")
        if len(accepted_this_bucket) < quota:
            shortfall[resolution_key] = quota - len(accepted_this_bucket)
        accepted_ids.extend(accepted_this_bucket)

    if shortfall:
        raise ValueError(
            f"quota not reached from the reviewed pool: {shortfall} more ACCEPTs needed per bucket "
            "(re-run build_btf3_confirmatory_candidates.py with a larger --pool-size, review only the "
            "newly appended tail candidates, and re-run this freeze -- do not reorder or resample)"
        )

    frame = pd.read_parquet(args.source)
    rows_by_id = {str(row["question_id"]): row for row in frame.to_dict("records")}
    rows = [rows_by_id[qid] for qid in accepted_ids]
    items = [build_candidate(row) for row in rows]
    validate_collection(items)

    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    jsonl = output / f"btf3_temporal_{args.artifact_label}.jsonl"
    verdict = output / f"btf3_temporal_{args.artifact_label}_verdict.md"
    jsonl.write_text("".join(item.to_json() + "\n" for item in items), encoding="utf-8")

    counts = {"0": sum(1 for r in rows if int(float(r["resolution"])) == 0),
              "1": sum(1 for r in rows if int(float(r["resolution"])) == 1)}
    verdict_lines = [
        f"# BTF-3 confirmatory freeze verdict — {args.artifact_label}",
        "",
        f"- accepted: {len(items)} ({counts['1']} YES / {counts['0']} NO)",
        f"- quota per resolution: {quota}",
        f"- rejected/unsure from queue: {len(reject_log)}",
        "",
        "## Rejections and reasons",
        "",
    ]
    verdict_lines.extend(reject_log or ["(none)"])
    verdict.write_text("\n".join(verdict_lines) + "\n", encoding="utf-8")

    print(f"wrote {len(items)} frozen confirmatory units to {jsonl}")
    print(f"resolution balance: {counts}")
    print(f"wrote verdict to {verdict}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
