from __future__ import annotations

from datetime import datetime
import hashlib
from pathlib import Path
from typing import Any

try:
    from ..information_set_schema import InformationSetItem
except ImportError:  # direct adapter use with PYTHONPATH=src
    from information_set_schema import InformationSetItem


SOURCE_ID = "btf3"
SOURCE_REVISION = "4b426627e19cd86202de69a40bc9dadb7f5ccd59"
SOURCE_SHA256 = "b28f8fe5634f81afa8e4b37d815f875b6e33c24edf590484f1948efea8db051a"
SOURCE_URL = "https://huggingface.co/datasets/BTF-2/BTF-3"


def _iso(value: Any) -> datetime:
    return datetime.fromisoformat(str(value).replace("Z", "+00:00"))


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
    if _iso(row["present_date"]) >= _iso(row["expected_resolution_date"]):
        raise ValueError("present_date must precede expected_resolution_date")


def _source_block(row: dict[str, Any]) -> str:
    return (
        f"FORECASTING QUESTION\n{row['question']}\n\n"
        f"RESOLUTION CRITERIA\n{row['resolution_criteria']}\n\n"
        f"BACKGROUND AVAILABLE AS OF {row['present_date']}\n{row['background']}"
    )


def _task(row: dict[str, Any], *, ex_ante: bool, include_packet: bool) -> str:
    source = _source_block(row)
    if ex_ante:
        target = (
            "TARGET INFORMATION SET\n"
            f"Estimate the probability that was warranted as of {row['present_date']}. "
            f"The task's information set ends at the close of UTC day {row['date_cutoff_end']}. "
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
            "target_information_set": "through date_cutoff_end",
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
            "transformation_contract": "BTF3_TRANSFORMATION_CONTRACT.md#candidate-v0.1",
        },
        transformation_id="btf3-temporal-v0.1-review",
    )
    return InformationSetItem.from_dict(item.to_dict())


def deterministic_review_sample(frame: Any, *, n_per_resolution: int = 4, seed: int = 20260829) -> list[dict]:
    if n_per_resolution <= 0:
        raise ValueError("n_per_resolution must be positive")
    records = frame.to_dict("records")
    seen: set[str] = set()
    buckets: dict[int, list[tuple[str, dict]]] = {0: [], 1: []}
    for row in records:
        validate_source_row(row)
        qid = str(row["question_id"])
        if qid in seen:
            raise ValueError(f"duplicate question_id: {qid}")
        seen.add(qid)
        resolution = int(float(row["resolution"]))
        order = hashlib.sha256(f"{seed}:{qid}".encode()).hexdigest()
        buckets[resolution].append((order, row))
    if any(len(bucket) < n_per_resolution for bucket in buckets.values()):
        raise ValueError("not enough rows in one resolution bucket")
    selected = []
    for resolution in (0, 1):
        selected.extend(row for _, row in sorted(buckets[resolution])[:n_per_resolution])
    return selected


def render_review(items: list[InformationSetItem], rows: list[dict[str, Any]]) -> str:
    by_id = {str(row["question_id"]): row for row in rows}
    out = [
        "# BTF-3 temporal pilot — human review packet v0.1",
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
            f"- Source cutoff end: `{row['date_cutoff_end']}`",
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
