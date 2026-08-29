#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from adapters.fantom_perspective import (  # noqa: E402
    build_candidate,
    deterministic_review_sample,
    validate_candidate_against_source,
)
from information_set_schema import file_sha256, load_jsonl, validate_collection  # noqa: E402


DEFAULT_REJECTED_PART_IDS = ["244-0", "252-0", "14-0", "111-0"]


def render_review(items, rows) -> str:
    out = [
        "# FANToM perspective candidate v0.1r4 — final replacement review",
        "",
        "> Do not run models before human review and the repository-wide preregistration freeze.",
        "> Source: Kim et al., FANToM (EMNLP 2023), official MIT-licensed repository; this is an evaluation-only transformed review artifact, not an original FANToM score reproduction.",
        "",
    ]
    for index, (item, row) in enumerate(zip(items, rows, strict=True), 1):
        rc = item.reference_context
        out.extend([
            f"## {index}. part `{row['part_id']}` / set `{row['set_id']}`",
            "",
            f"- Target character: `{row['joining_speaker']}`",
            "- Reviewer decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`",
            "- Reviewer reason:",
            "",
            "### Source short conversation",
            "",
            str(row["short_context"]),
            "",
            "### Source belief question and candidates",
            "",
            str(rc["belief_question"]),
            "",
            f"- Source-correct unbriefed belief: {rc['source_correct_belief_answer']}",
            f"- Truth-belief candidate: {rc['truth_belief_answer']}",
            "",
            "### Exact separate fact packet",
            "",
            str(rc["critical_packet"]),
            "",
            "### Source-native probes",
            "",
            f"- Boundary: {rc['boundary_probe_question']} → `{rc['boundary_probe_answer']}`",
            f"- Fact: {rc['fact_question']} → {rc['fact_answer']}",
            f"- Fact distractor: {rc['fact_distractor']}",
            "",
            "### Checklist",
            "",
            "- [ ] Target did not hear/learn the critical fact in the conversation.",
            "- [ ] Source-correct candidate describes the unbriefed target belief.",
            "- [ ] Exact packet would make the truth-belief candidate correct if told to target.",
            "- [ ] Packet is complete and consistent with the conversation.",
            "- [ ] Belief question remains meaningful before and after explicit briefing.",
            "- [ ] Four cells change only target-set framing and exact packet insertion.",
            "- [ ] No safety/privacy concern.",
            "",
        ])
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="data/external/raw/fantom/fantom_v1.json")
    parser.add_argument("--n", type=int, default=8)
    parser.add_argument("--seed", type=int, default=20260829)
    parser.add_argument("--output-dir", default="data/external/review")
    parser.add_argument(
        "--exclude-part-id",
        action="append",
        default=None,
        help="Rejected part_id to exclude; may be repeated. Defaults to v0.1 rejects.",
    )
    args = parser.parse_args()

    rows = json.loads(Path(args.source).read_text(encoding="utf-8"))
    exclusions = (
        DEFAULT_REJECTED_PART_IDS
        if args.exclude_part_id is None
        else args.exclude_part_id
    )
    selected = deterministic_review_sample(
        rows, n=args.n, seed=args.seed, exclude_part_ids=exclusions
    )
    items = [build_candidate(row) for row in selected]
    validate_collection(items)
    for item, row in zip(items, selected, strict=True):
        validate_candidate_against_source(item, row)

    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    jsonl = output / "fantom_perspective_pilot_v0.1r4.jsonl"
    markdown = output / "fantom_perspective_pilot_v0.1r4.md"
    jsonl.write_text("".join(item.to_json() + "\n" for item in items), encoding="utf-8")
    markdown.write_text(render_review(items, selected), encoding="utf-8")
    # Audit the serialized bytes, not only the in-memory objects.
    serialized = load_jsonl(jsonl)
    source_by_set = {str(row["set_id"]): row for row in selected}
    for item in serialized:
        validate_candidate_against_source(
            item, source_by_set[item.provenance["source_record_id"]]
        )
    print(f"wrote {len(items)} review candidates to {jsonl} and {markdown}")
    print("excluded part IDs:", ", ".join(exclusions))
    print(f"serialized JSONL SHA-256: {file_sha256(jsonl)}")
    print("human review remains required before any model run")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
