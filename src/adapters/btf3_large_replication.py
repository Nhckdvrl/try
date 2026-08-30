"""Selection machinery for the BTF-3 Large Replication v1 round (256 fresh units).

This module deliberately adds no new task semantics. Prompt construction,
automatic eligibility, and the four-cell causal design are imported unchanged
from :mod:`adapters.btf3_temporal`, so a 64 -> 256 expansion is a strict
replication of the confirmatory round rather than a new experiment.

What is new here is *selection discipline*:

- a strict-freshness exclusion universe (pilot, confirmatory sample, the entire
  prior confirmatory candidate queue including its unreviewed tail, historical
  rejects, and every prior REJECT/UNSURE);
- one complete immutable per-bucket queue over *all* eligible candidates,
  rather than a truncated pool that might have to be regrown mid-review;
- a mechanical hard-duplicate rule on normalized question text, applied before
  review so the frozen queue can never contain two renderings of one question.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
from typing import Any, Iterable

try:
    from .btf3_temporal import _utc_source_day, validate_source_row
except ImportError:  # direct adapter use with PYTHONPATH=src
    from adapters.btf3_temporal import _utc_source_day, validate_source_row


ROUND_ID = "btf3_large_replication_v1"
SEED = 20260831
QUOTA_PER_RESOLUTION = 128

# The two source units rejected by human review during the pilot rounds. They
# are permanently excluded from every later BTF-3 selection round.
HISTORICAL_REJECTED_IDS = (
    "b6fc94e7-a0b9-56b6-87a1-ba94f29781e9",
    "34d3588a-ffb0-5290-b964-bceb68be18f1",
)

_WHITESPACE = re.compile(r"\s+")
_DECISION_HEADING = re.compile(r"^#{2,4} (?:YES|NO)-\d+\. `([^`]+)`\s*$")
_DECISION_LINE = re.compile(
    r"^\s*-\s*Decision:\s*`\[([ xX])\]\s*ACCEPT\s*\[([ xX])\]\s*REJECT\s*\[([ xX])\]\s*UNSURE`\s*$"
)


def normalize_question(text: Any) -> str:
    """Normalization used only for the mechanical hard-duplicate rule."""
    return _WHITESPACE.sub(" ", str(text)).strip().casefold()


def order_key(question_id: str, *, seed: int = SEED) -> str:
    return hashlib.sha256(f"{seed}:{question_id}".encode()).hexdigest()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _jsonl_unit_ids(path: Path) -> list[str]:
    ids = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.strip():
            ids.append(str(json.loads(line)["independent_unit_id"]))
    return ids


def _reviewed_non_accept_ids(path: Path) -> list[str]:
    """Every prior candidate whose recorded decision was REJECT or UNSURE."""
    text = Path(path).read_text(encoding="utf-8")
    lines = text.splitlines()
    out: list[str] = []
    current: str | None = None
    for line in lines:
        heading = _DECISION_HEADING.match(line)
        if heading:
            current = heading.group(1)
            continue
        match = _DECISION_LINE.match(line)
        if match and current is not None:
            marks = [group.strip().lower() == "x" for group in match.groups()]
            if sum(marks) != 1:
                raise ValueError(f"{current}: exactly one decision must be ticked")
            decision = ("ACCEPT", "REJECT", "UNSURE")[marks.index(True)]
            if decision != "ACCEPT":
                out.append(current)
            current = None
    return out


def build_exclusion_universe(
    *,
    pilot_jsonl: Path,
    confirmatory_jsonl: Path,
    prior_candidates_json: Path,
    prior_reviewed_md: Path,
    historical_rejected_ids: Iterable[str] = HISTORICAL_REJECTED_IDS,
) -> dict[str, Any]:
    """Strict-freshness exclusion universe, derived from committed artifacts.

    Nothing here is hand-typed except the two historical rejects, which no
    longer live in any queue file. Every other category is read back out of the
    artifact that defines it, together with that artifact's SHA-256, so the
    exclusion set cannot silently drift from the rounds it claims to exclude.
    """
    pilot_ids = _jsonl_unit_ids(pilot_jsonl)
    confirmatory_ids = _jsonl_unit_ids(confirmatory_jsonl)
    manifest = json.loads(Path(prior_candidates_json).read_text(encoding="utf-8"))
    prior_queue_ids = [str(qid) for ids in manifest["queue"].values() for qid in ids]
    prior_non_accept_ids = _reviewed_non_accept_ids(prior_reviewed_md)
    categories = {
        "pilot_v0_2r2": sorted(set(pilot_ids)),
        "confirmatory_v1_frozen": sorted(set(confirmatory_ids)),
        "confirmatory_v1_candidate_queue": sorted(set(prior_queue_ids)),
        "confirmatory_v1_review_reject_or_unsure": sorted(set(prior_non_accept_ids)),
        "historical_pilot_rejects": sorted(set(str(x) for x in historical_rejected_ids)),
    }
    union = sorted({qid for ids in categories.values() for qid in ids})
    return {
        "categories": categories,
        "category_counts": {name: len(ids) for name, ids in categories.items()},
        "union": union,
        "union_count": len(union),
        "sources": {
            "pilot_jsonl": {
                "path": str(pilot_jsonl),
                "sha256": file_sha256(pilot_jsonl),
            },
            "confirmatory_jsonl": {
                "path": str(confirmatory_jsonl),
                "sha256": file_sha256(confirmatory_jsonl),
            },
            "prior_candidates_json": {
                "path": str(prior_candidates_json),
                "sha256": file_sha256(prior_candidates_json),
            },
            "prior_reviewed_md": {
                "path": str(prior_reviewed_md),
                "sha256": file_sha256(prior_reviewed_md),
            },
        },
    }


def eligible_rows(frame: Any) -> list[dict[str, Any]]:
    """All source rows that pass the unchanged automatic eligibility contract."""
    records = frame.to_dict("records")
    seen: set[str] = set()
    out = []
    for row in records:
        validate_source_row(row)
        qid = str(row["question_id"])
        if qid in seen:
            raise ValueError(f"duplicate question_id in source: {qid}")
        seen.add(qid)
        out.append(row)
    return out


def full_deterministic_queue(
    frame: Any,
    *,
    seed: int = SEED,
    exclude_question_ids: Iterable[str] = (),
    exclude_normalized_questions: Iterable[str] = (),
) -> dict[str, Any]:
    """Complete immutable candidate order over every eligible candidate.

    Unlike the confirmatory round's ``deterministic_candidate_queue``, this
    truncates nothing: the entire eligible pool is ordered once, so review can
    never exhaust the queue and force a regrow-and-append step.

    Hard duplicates (identical normalized question text) are resolved
    mechanically here, before any review: the candidate with the earlier global
    hash rank is kept and every later one is dropped, with the drop recorded.
    """
    excluded_ids = {str(qid) for qid in exclude_question_ids}
    prior_questions = {str(text) for text in exclude_normalized_questions}

    ranked = sorted(
        (
            (order_key(str(row["question_id"]), seed=seed), row)
            for row in eligible_rows(frame)
            if str(row["question_id"]) not in excluded_ids
        ),
        key=lambda pair: pair[0],
    )

    kept: dict[int, list[dict[str, Any]]] = {0: [], 1: []}
    first_seen: dict[str, str] = {}
    dropped_within_round: list[dict[str, str]] = []
    dropped_against_prior_rounds: list[dict[str, str]] = []
    for _, row in ranked:
        qid = str(row["question_id"])
        norm = normalize_question(row["question"])
        if norm in prior_questions:
            dropped_against_prior_rounds.append({"question_id": qid, "normalized_question": norm})
            continue
        if norm in first_seen:
            dropped_within_round.append(
                {"question_id": qid, "kept_question_id": first_seen[norm], "normalized_question": norm}
            )
            continue
        first_seen[norm] = qid
        kept[int(float(row["resolution"]))].append(row)

    return {
        "queue": kept,
        "dropped_duplicate_within_round": dropped_within_round,
        "dropped_duplicate_against_prior_rounds": dropped_against_prior_rounds,
        "seed": seed,
    }


def render_review_chunk(
    rows: list[dict[str, Any]],
    *,
    bucket_label: str,
    start_index: int,
    quota_per_resolution: int = QUOTA_PER_RESOLUTION,
    round_label: str = ROUND_ID,
) -> str:
    """One display chunk of the immutable queue.

    Chunking is presentation only. Selection order is defined solely by the
    frozen queue manifest; a chunk boundary never means anything statistically.
    """
    end_index = start_index + len(rows) - 1
    out = [
        f"# {round_label} — realized {bucket_label} review chunk "
        f"{bucket_label}-{start_index:03d}–{bucket_label}-{end_index:03d}",
        "",
        "> Display chunk of the immutable queue "
        f"(`{round_label}_{bucket_label.lower()}_queue.json`). Review strictly "
        f"top-to-bottom; stop only when this bucket reaches "
        f"{quota_per_resolution} ACCEPTs overall. Do not skip ahead, reorder, "
        "or prefer better-looking questions. A REJECT/UNSURE permanently "
        "consumes its queue slot and is never resampled, re-reviewed, or "
        "hand-repaired.",
        "",
        "All four gates must hold to ACCEPT. On REJECT or UNSURE write exactly "
        "one line of reason.",
        "",
    ]
    for offset, row in enumerate(rows):
        index = start_index + offset
        qid = str(row["question_id"])
        out.extend([
            f"### {bucket_label}-{index}. `{qid}`",
            "",
            f"- Present date: `{row['present_date']}`",
            f"- Source cutoff boundary: `{row['date_cutoff_end']}` "
            f"(encodes end of UTC day `{_utc_source_day(row)}`)",
            f"- Expected resolution: `{row['expected_resolution_date']}`",
            "",
            "**Question**",
            "",
            str(row["question"]),
            "",
            "**Resolution criteria**",
            "",
            str(row["resolution_criteria"]),
            "",
            "**Pre-cutoff background**",
            "",
            str(row["background"]),
            "",
            "**Exact later resolution packet**",
            "",
            str(row["resolution_explanation"]),
            "",
            "**Gates (all four must hold to ACCEPT):**",
            "- [ ] pre-cutoff intact — background/question contain no post-cutoff facts",
            "- [ ] realized outcome valid — resolution matches the cited evidence",
            "- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`",
            "- [ ] criteria unambiguous — resolution criteria admit only one reading",
            "",
            "- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`",
            "- Reason (required for REJECT/UNSURE, one line):",
            "",
        ])
    return "\n".join(out).rstrip() + "\n"
