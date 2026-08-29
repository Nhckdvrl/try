from __future__ import annotations

from datetime import datetime, timedelta
import hashlib
from pathlib import Path
from typing import Any, Iterable

try:
    from ..information_set_schema import InformationSetItem
except ImportError:  # direct adapter use with PYTHONPATH=src
    from information_set_schema import InformationSetItem


SOURCE_ID = "btf3"
SOURCE_REVISION = "4b426627e19cd86202de69a40bc9dadb7f5ccd59"
SOURCE_SHA256 = "b28f8fe5634f81afa8e4b37d815f875b6e33c24edf590484f1948efea8db051a"
SOURCE_URL = "https://huggingface.co/datasets/BTF-2/BTF-3"
TRANSFORMATION_ID = "btf3-temporal-v0.2-review"


def _iso(value: Any) -> datetime:
    return datetime.fromisoformat(str(value).replace("Z", "+00:00"))


def _utc_source_day(row: dict[str, Any]) -> str:
    """UTC calendar day whose end defines the source forecasting window.

    BTF-3 documents ``date_cutoff_end`` as the encoding of the end of the UTC
    day containing ``present_date``.  In the pinned source revision the stored
    date is the following midnight-style boundary (e.g. present May 12 ->
    cutoff_end May 13).  Prompts should name the present-date UTC day, not call
    May 13 itself an available day.
    """
    return _iso(row["present_date"]).date().isoformat()


def validate_source_row(row: dict[str, Any]) -> None:
    required = {
        "question_id", "question", "resolution_criteria", "background",
        "present_date", "date_cutoff_end", "expected_resolution_date",
        "resolution", "resolution_explanation",
    }
    missing = required - set(row)
    if missing:
        raise ValueError(f"BTF-3 row missing {sorted(missing)}")
    for key in required - {"resolution"}:
        if not str(row[key]).strip():
            raise ValueError(f"BTF-3 field {key} is empty")
    if float(row["resolution"]) not in (0.0, 1.0):
        raise ValueError("binary resolution must be 0 or 1")

    present = _iso(row["present_date"])
    cutoff = _iso(row["date_cutoff_end"])
    expected = _iso(row["expected_resolution_date"])
    if present >= expected:
        raise ValueError("present_date must precede expected_resolution_date")

    # Source-revision invariant.  date_cutoff_end is stored as the next
    # midnight-style date boundary for the UTC day containing present_date.
    # Locking this prevents the v0.1 off-by-one wording from returning.
    expected_cutoff_date = present.date() + timedelta(days=1)
    if cutoff.date() != expected_cutoff_date or cutoff.time() != datetime.min.time():
        raise ValueError(
            "unexpected BTF-3 cutoff encoding: expected date_cutoff_end to be "
            "the midnight boundary immediately after the UTC day containing present_date"
        )


def _source_block(row: dict[str, Any]) -> str:
    return (
        f"FORECASTING QUESTION\n{row['question']}\n\n"
        f"RESOLUTION CRITERIA\n{row['resolution_criteria']}\n\n"
        f"BACKGROUND AVAILABLE AS OF {row['present_date']}\n{row['background']}"
    )


def _task(row: dict[str, Any], *, ex_ante: bool, include_packet: bool) -> str:
    source = _source_block(row)
    if ex_ante:
        source_day = _utc_source_day(row)
        target = (
            "TARGET INFORMATION SET\n"
            f"Estimate the probability that was warranted as of {row['present_date']}. "
            f"Use only information available through the end of UTC day {source_day}, "
            f"which the source encodes with date_cutoff_end={row['date_cutoff_end']}. "
            "Do not treat the following UTC calendar day as available. "
            "Any text explicitly labeled LATER RESOLUTION PACKET was produced after this "
            "information set and is not part of the evidence that defines the requested ex-ante forecast."
        )
    else:
        target = (
            "TARGET INFORMATION SET\n"
            "Make a retrospective probability-of-resolution judgment using all information "
            "supplied in this prompt, including any LATER RESOLUTION PACKET."
        )
    packet = ""
    if include_packet:
        packet = f"\n\nLATER RESOLUTION PACKET\n{row['resolution_explanation']}"
    answer = (
        "\n\nTASK\nWhat probability should be assigned to this question resolving YES? "
        "Return only one number from 0 to 100."
    )
    return source + "\n\n" + target + packet + answer


def build_candidate(row: dict[str, Any]) -> InformationSetItem:
    validate_source_row(row)
    resolution = int(float(row["resolution"]))
    shared = {
        "question": row["question"],
        "resolution_criteria": row["resolution_criteria"],
        "background": row["background"],
        "present_date": str(row["present_date"]),
        "date_cutoff_end": str(row["date_cutoff_end"]),
        "source_utc_day": _utc_source_day(row),
        "expected_resolution_date": str(row["expected_resolution_date"]),
        "realized_resolution": resolution,
        "outcome_alignment_sign": 1 if resolution == 1 else -1,
    }
    item = InformationSetItem(
        source_id=SOURCE_ID,
        independent_unit_id=str(row["question_id"]),
        boundary_type="temporal",
        reference_context=shared,
        oob_variant={
            "target_information_set": "through end of UTC day containing present_date",
            "without_information_prompt": _task(row, ex_ante=True, include_packet=False),
            "with_information_prompt": _task(row, ex_ante=True, include_packet=True),
        },
        admissible_variant={
            "target_information_set": "all supplied information",
            "without_information_prompt": _task(row, ex_ante=False, include_packet=False),
            "with_information_prompt": _task(row, ex_ante=False, include_packet=True),
        },
        provenance={
            "source_url": SOURCE_URL,
            "source_revision": SOURCE_REVISION,
            "source_file": "btf3_binary_questions_and_forecasts.parquet",
            "source_file_sha256": SOURCE_SHA256,
            "source_record_id": str(row["question_id"]),
            "reuse_status": "CC_BY_NC_4_0_REVIEW_CANDIDATE_NOT_FROZEN",
            "transformation_contract": "BTF3_TRANSFORMATION_CONTRACT.md#candidate-v02",
        },
        transformation_id=TRANSFORMATION_ID,
    )
    return InformationSetItem.from_dict(item.to_dict())


def validate_candidate_against_source(item: InformationSetItem, row: dict[str, Any]) -> None:
    """Prove that a serialized candidate is the registered four-cell transform.

    This is intentionally independent of schema validation: it checks every
    full prompt against the pinned source row and prevents an unregistered text
    change from entering a regenerated review artifact.
    """
    validate_source_row(row)
    qid = str(row["question_id"])
    if item.independent_unit_id != qid:
        raise ValueError(f"candidate/source ID mismatch: {item.independent_unit_id} != {qid}")
    expected = {
        ("oob_variant", "without_information_prompt"): _task(
            row, ex_ante=True, include_packet=False
        ),
        ("oob_variant", "with_information_prompt"): _task(
            row, ex_ante=True, include_packet=True
        ),
        ("admissible_variant", "without_information_prompt"): _task(
            row, ex_ante=False, include_packet=False
        ),
        ("admissible_variant", "with_information_prompt"): _task(
            row, ex_ante=False, include_packet=True
        ),
    }
    variants = {
        "oob_variant": item.oob_variant,
        "admissible_variant": item.admissible_variant,
    }
    for (variant_name, prompt_name), expected_prompt in expected.items():
        actual = variants[variant_name][prompt_name]
        if actual != expected_prompt:
            raise ValueError(
                f"unregistered prompt drift for {qid} {variant_name}.{prompt_name}"
            )

    packet = str(row["resolution_explanation"])
    for variant in variants.values():
        if packet in variant["without_information_prompt"]:
            raise ValueError(f"later packet leaked into WITHOUT prompt for {qid}")
        if variant["with_information_prompt"].count(packet) != 1:
            raise ValueError(f"later packet is not present exactly once in WITH prompt for {qid}")


def deterministic_review_sample(
    frame: Any,
    *,
    n_per_resolution: int = 4,
    seed: int = 20260829,
    exclude_question_ids: Iterable[str] = (),
) -> list[dict]:
    if n_per_resolution <= 0:
        raise ValueError("n_per_resolution must be positive")
    excluded = {str(qid) for qid in exclude_question_ids}
    records = frame.to_dict("records")
    seen: set[str] = set()
    buckets: dict[int, list[tuple[str, dict]]] = {0: [], 1: []}
    for row in records:
        validate_source_row(row)
        qid = str(row["question_id"])
        if qid in seen:
            raise ValueError(f"duplicate question_id: {qid}")
        seen.add(qid)
        if qid in excluded:
            continue
        resolution = int(float(row["resolution"]))
        order = hashlib.sha256(f"{seed}:{qid}".encode()).hexdigest()
        buckets[resolution].append((order, row))
    if any(len(bucket) < n_per_resolution for bucket in buckets.values()):
        raise ValueError("not enough rows in one resolution bucket after exclusions")
    selected = []
    for resolution in (0, 1):
        selected.extend(row for _, row in sorted(buckets[resolution])[:n_per_resolution])
    return selected


def deterministic_candidate_queue(
    frame: Any,
    *,
    pool_size: int,
    seed: int = 20260829,
    exclude_question_ids: Iterable[str] = (),
) -> dict[int, list[dict]]:
    """Full deterministic per-resolution candidate order for streamlined review.

    Unlike ``deterministic_review_sample``, this does not truncate to a fixed
    accepted count: it returns up to ``pool_size`` candidates per resolution
    bucket, in the same fixed hash order a human will review them in. The
    freeze step then walks this order and takes the first N accepts per
    bucket, so no resampling or reviewer-visible choice ever enters selection.
    """
    if pool_size <= 0:
        raise ValueError("pool_size must be positive")
    excluded = {str(qid) for qid in exclude_question_ids}
    records = frame.to_dict("records")
    seen: set[str] = set()
    buckets: dict[int, list[tuple[str, dict]]] = {0: [], 1: []}
    for row in records:
        validate_source_row(row)
        qid = str(row["question_id"])
        if qid in seen:
            raise ValueError(f"duplicate question_id: {qid}")
        seen.add(qid)
        if qid in excluded:
            continue
        resolution = int(float(row["resolution"]))
        order = hashlib.sha256(f"{seed}:{qid}".encode()).hexdigest()
        buckets[resolution].append((order, row))
    return {
        resolution: [row for _, row in sorted(bucket)[:pool_size]]
        for resolution, bucket in buckets.items()
    }


def render_confirmatory_queue(
    rows_by_resolution: dict[int, list[dict[str, Any]]],
    *,
    artifact_label: str,
    quota_per_resolution: int,
) -> str:
    """Streamlined review packet: fixed queue order, four boolean gates only.

    This intentionally drops the pilot's long narrative checklist. The gate
    that matters most for this source is packet factual validity (BTF-3's
    ``resolution_explanation`` is machine-generated and only partially
    spot-checked, and the pilot review already caught two exact-packet
    errors) — that gate is retained at full strength. Everything else is
    reduced to a single tick and a one-line reason on reject.
    """
    out = [
        f"# BTF-3 confirmatory candidate queue — {artifact_label}",
        "",
        f"> Fixed deterministic order. Review top-to-bottom within each "
        f"resolution bucket until {quota_per_resolution} ACCEPTs are reached "
        "per bucket. Do not skip ahead or reorder. A REJECT/UNSURE consumes "
        "its queue slot permanently and is never resampled or reconsidered.",
        "",
        "For each item, tick exactly one of ACCEPT / REJECT / UNSURE for all "
        "four gates jointly (all four must hold to ACCEPT). On REJECT or "
        "UNSURE, write exactly one line giving the reason.",
        "",
    ]
    for resolution in (0, 1):
        label = "YES" if resolution else "NO"
        rows = rows_by_resolution.get(resolution, [])
        out.append(f"## Realized {label} queue ({len(rows)} candidates)")
        out.append("")
        for index, row in enumerate(rows, 1):
            qid = str(row["question_id"])
            out.extend([
                f"### {label}-{index}. `{qid}`",
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


def render_review(
    items: list[InformationSetItem],
    rows: list[dict[str, Any]],
    *,
    artifact_label: str = "v0.2",
) -> str:
    by_id = {str(row["question_id"]): row for row in rows}
    out = [
        f"# BTF-3 temporal pilot — human review packet {artifact_label}",
        "",
        "> 现在不要跑模型。请只审查 source validity 和 transformation integrity。",
        "",
        "请直接在每一题的 `Reviewer decision` 勾选 `ACCEPT / REJECT / UNSURE`，并在下一行写原因。",
        "重点核对：截止日前题目是否仍未解决、background 是否越界、resolution 是否由引用支持、四格是否只改变信息资格/packet。",
        "JSONL 保存了四个完整 prompts；本文档把共同 source text 和 condition delta 各展示一次，方便人工核对。",
        "",
    ]
    for index, item in enumerate(items, 1):
        row = by_id[item.independent_unit_id]
        out.extend([
            f"## {index}. `{item.independent_unit_id}` — realized {'YES' if int(row['resolution']) else 'NO'}",
            "",
            f"- Present date: `{row['present_date']}`",
            f"- Source cutoff boundary: `{row['date_cutoff_end']}` (encodes the end of UTC day `{_utc_source_day(row)}`)",
            f"- Expected resolution: `{row['expected_resolution_date']}`",
            "- Reviewer decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`",
            "- Reviewer reason（拒绝或不确定时必须写）:",
            "",
            "### Source question",
            "",
            str(row["question"]),
            "",
            "### Resolution criteria",
            "",
            str(row["resolution_criteria"]),
            "",
            "### Pre-cutoff background",
            "",
            str(row["background"]),
            "",
            "### Exact later resolution packet",
            "",
            str(row["resolution_explanation"]),
            "",
            "### Condition delta to verify",
            "",
            "- `OOB_WITHOUT`: ex-ante cutoff; no later packet.",
            "- `OOB_WITH`: same ex-ante cutoff; exact later packet visible but outside the target set.",
            "- `ALLOWED_WITHOUT`: retrospective/all-supplied target set; no later packet.",
            "- `ALLOWED_WITH`: same retrospective target set; exact later packet supplied.",
            "",
            "### Checklist",
            "",
            "- [ ] Question was unresolved at the present date.",
            "- [ ] Background contains no post-cutoff facts.",
            "- [ ] Resolution criteria are unambiguous.",
            "- [ ] Resolution and cited evidence are factually supported.",
            "- [ ] Later packet changes evidence, not question interpretation.",
            "- [ ] All four prompts keep the question and 0–100 answer scale fixed.",
            "- [ ] No safety/privacy concern.",
            "",
        ])
    return "\n".join(out).rstrip() + "\n"
