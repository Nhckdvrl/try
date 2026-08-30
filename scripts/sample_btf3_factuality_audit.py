#!/usr/bin/env python3
"""Draw the deterministic 64-item factuality-audit subsample from the frozen 256.

Selection is fixed by hash before any citation is opened, so the audited
subsample cannot drift toward items that happen to look clean:

    h_i = SHA256("btf3-factual-audit-v1:" + question_id)

ascending within each realized-outcome bucket, first 32 per bucket.

This script never reads any target-model output, and it never modifies the
primary artifact. The audit it feeds cannot change the 256-unit membership.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from adapters.btf3_large_replication import file_sha256  # noqa: E402
from adapters.btf3_temporal import _utc_source_day  # noqa: E402
from information_set_schema import load_jsonl  # noqa: E402

AUDIT_ID = "btf3-factual-audit-v1"
PER_BUCKET = 32


def audit_key(question_id: str) -> str:
    return hashlib.sha256(f"{AUDIT_ID}:{question_id}".encode()).hexdigest()


def render_packet(rows: list[dict], *, label: str, start_index: int) -> str:
    out = [
        f"# BTF-3 packet factuality audit v1 — realized {label} ({len(rows)} items)",
        "",
        "> External lookup is REQUIRED here: open the citations named in each",
        "> packet and check them. No target-model output may be consulted.",
        "> Nothing decided here changes the frozen 256-unit primary sample.",
        "",
        "For each item mark every check, then record one overall verdict:",
        "`PASS` (no material error), `MATERIAL_ERROR` (one or more checks fail",
        "in a way that changes the outcome or its support), or `UNVERIFIABLE`",
        "(cited sources could not be reached or no longer exist). Give exactly",
        "one line of reason for MATERIAL_ERROR and UNVERIFIABLE.",
        "",
    ]
    for offset, row in enumerate(rows):
        index = start_index + offset
        out.extend([
            f"### {label}-{index}. `{row['question_id']}`",
            "",
            f"- Present date: `{row['present_date']}` (information window ends end of UTC day `{row['source_utc_day']}`)",
            f"- Expected resolution: `{row['expected_resolution_date']}`",
            f"- Recorded realized outcome: **{label}**",
            "",
            "**Question**",
            "",
            row["question"],
            "",
            "**Resolution criteria**",
            "",
            row["resolution_criteria"],
            "",
            "**Exact later resolution packet (the object under audit)**",
            "",
            row["resolution_explanation"],
            "",
            "**Checks (open the cited sources):**",
            "- [ ] realized outcome is correct against the cited/primary evidence",
            "- [ ] cited sources exist and actually support what the packet says they support",
            "- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on",
            "- [ ] no temporal-logic error inside the packet",
            "- [ ] criteria and the claimed outcome genuinely align",
            "",
            "- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`",
            "- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):",
            "",
        ])
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact", type=Path, default=Path("data/external/review/btf3_temporal_large_replication_v1.jsonl"))
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("data/external/raw/btf3/btf3_binary_questions_and_forecasts.parquet"),
    )
    parser.add_argument("--per-bucket", type=int, default=PER_BUCKET)
    parser.add_argument("--output-dir", type=Path, default=Path("data/external/review"))
    args = parser.parse_args()

    import pandas as pd

    items = load_jsonl(args.artifact)
    frame = pd.read_parquet(args.source)
    source_rows = {str(row["question_id"]): row for row in frame.to_dict("records")}

    buckets: dict[int, list[tuple[str, dict]]] = {0: [], 1: []}
    for item in items:
        qid = item.independent_unit_id
        row = source_rows[qid]
        resolution = int(float(row["resolution"]))
        buckets[resolution].append((
            audit_key(qid),
            {
                "question_id": qid,
                "realized_resolution": resolution,
                "question": str(row["question"]),
                "resolution_criteria": str(row["resolution_criteria"]),
                "resolution_explanation": str(row["resolution_explanation"]),
                "present_date": str(row["present_date"]),
                "expected_resolution_date": str(row["expected_resolution_date"]),
                "source_utc_day": _utc_source_day(row),
            },
        ))

    selection: dict[str, list[dict]] = {}
    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    for resolution, label in ((1, "YES"), (0, "NO")):
        ranked = [row for _, row in sorted(buckets[resolution], key=lambda pair: pair[0])]
        if len(ranked) < args.per_bucket:
            raise ValueError(f"bucket {label} has only {len(ranked)} items")
        chosen = ranked[: args.per_bucket]
        selection[label] = chosen
        path = output / f"btf3_factuality_audit_v1_{label.lower()}.md"
        path.write_text(render_packet(chosen, label=label, start_index=1), encoding="utf-8")

    manifest_path = output / "btf3_factuality_audit_v1_sample.json"
    manifest = {
        "audit_id": AUDIT_ID,
        "selection_rule": 'SHA256("btf3-factual-audit-v1:" + question_id) ascending, first N per realized-outcome bucket',
        "per_bucket": args.per_bucket,
        "primary_artifact": {
            "path": str(args.artifact),
            "sha256": file_sha256(args.artifact),
            "units": len(items),
        },
        "source": {"path": str(args.source), "sha256": file_sha256(args.source)},
        "sample": {
            label: [
                {"position": index, "question_id": row["question_id"], "audit_key": audit_key(row["question_id"])}
                for index, row in enumerate(rows, 1)
            ]
            for label, rows in selection.items()
        },
        "changes_primary_membership": False,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({label: len(rows) for label, rows in selection.items()}, indent=2))
    print(f"wrote {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
