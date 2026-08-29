from __future__ import annotations

import hashlib
from typing import Any

try:
    from ..information_set_schema import InformationSetItem
except ImportError:  # direct adapter use with PYTHONPATH=src
    from information_set_schema import InformationSetItem


SOURCE_ID = "fantom_v1"
SOURCE_REVISION = "1cae6fa30f5ba04ca0fff5f5716b5ba7055e2e85"
SOURCE_ARCHIVE_SHA256 = "1d08dfa0ea474c7f83b9bc7e3a7b466eab25194043489dd618b4c5223e1253a4"
SOURCE_JSON_SHA256 = "6a898e95df9fa48608232e45a8eb8f531e4d633aaf1a023a2b910991a6bc7c6e"
SOURCE_URL = "https://github.com/skywalker023/fantom"
TRANSFORMATION_ID = "fantom-perspective-v0.1-review"


def _boundary_probe(row: dict[str, Any]) -> dict[str, Any]:
    target = str(row["joining_speaker"])
    matches = [
        qa
        for qa in row["infoAccessibilityQAs_binary"]
        if target.lower() in str(qa.get("question", "")).lower()
    ]
    if len(matches) != 1 or not str(matches[0].get("correct_answer", "")).startswith("no"):
        raise ValueError("expected one source-native inaccessible boundary probe for joining speaker")
    return matches[0]


def eligible_first_order_qa(row: dict[str, Any]) -> dict[str, Any]:
    target = str(row.get("joining_speaker", "")).strip()
    matches = [
        qa
        for qa in row.get("beliefQAs", [])
        if qa.get("tom_type") == "first-order"
        and qa.get("missed_info_accessibility") == "inaccessible"
        and target.lower() in str(qa.get("question", "")).lower()
    ]
    if len(matches) != 1:
        raise ValueError("expected exactly one first-order inaccessible belief QA for joining speaker")
    return matches[0]


def validate_source_row(row: dict[str, Any]) -> None:
    required = {
        "set_id",
        "part_id",
        "conv_id",
        "short_context",
        "joining_speaker",
        "factQA",
        "beliefQAs",
        "infoAccessibilityQAs_binary",
    }
    missing = required - set(row)
    if missing:
        raise ValueError(f"FANToM row missing {sorted(missing)}")
    for key in required - {"factQA", "beliefQAs", "infoAccessibilityQAs_binary"}:
        if not str(row[key]).strip():
            raise ValueError(f"FANToM field {key} is empty")
    fact = row["factQA"]
    for key in ("question", "correct_answer", "wrong_answer"):
        if not str(fact.get(key, "")).strip():
            raise ValueError(f"FANToM factQA.{key} is empty")
    belief = eligible_first_order_qa(row)
    for key in ("question", "correct_answer", "wrong_answer"):
        if not str(belief.get(key, "")).strip():
            raise ValueError(f"FANToM belief QA {key} is empty")
    if belief["correct_answer"].strip() == belief["wrong_answer"].strip():
        raise ValueError("FANToM belief answer candidates must differ")
    _boundary_probe(row)


def _option_map(row: dict[str, Any]) -> dict[str, str]:
    belief = eligible_first_order_qa(row)
    truth_first = int(hashlib.sha256(str(row["set_id"]).encode()).hexdigest(), 16) % 2 == 0
    if truth_first:
        return {
            "truth_label": "A",
            "source_correct_label": "B",
            "A": str(belief["wrong_answer"]),
            "B": str(belief["correct_answer"]),
        }
    return {
        "truth_label": "B",
        "source_correct_label": "A",
        "A": str(belief["correct_answer"]),
        "B": str(belief["wrong_answer"]),
    }


def _source_block(row: dict[str, Any]) -> str:
    belief = eligible_first_order_qa(row)
    options = _option_map(row)
    return (
        f"CONVERSATION\n{row['short_context']}\n\n"
        f"BELIEF QUESTION\n{belief['question']}\n\n"
        f"CANDIDATE A\n{options['A']}\n\n"
        f"CANDIDATE B\n{options['B']}"
    )


def _fact_packet(row: dict[str, Any]) -> str:
    fact = row["factQA"]
    return f"Question: {fact['question']}\nAnswer: {fact['correct_answer']}"


def _task(row: dict[str, Any], *, allowed: bool, include_packet: bool) -> str:
    target = str(row["joining_speaker"])
    truth_label = _option_map(row)["truth_label"]
    if allowed:
        target_block = (
            "TARGET INFORMATION SET\n"
            f"Judge what {target} would believe at the evaluation point. If a SEPARATE FACT "
            f"PACKET is supplied below, assume {target} is explicitly told its exact contents "
            "after the conversation and before the belief question. If no packet is supplied, "
            f"assume {target} receives no additional information after the conversation."
        )
    else:
        target_block = (
            "TARGET INFORMATION SET\n"
            f"Judge what {target} believed at the end of the conversation shown, before any later "
            "briefing. A SEPARATE FACT PACKET, if supplied below, is an evaluator annotation that "
            f"{target} never saw or heard. It is not part of {target}'s information set at the "
            "evaluation point."
        )
    packet = f"\n\nSEPARATE FACT PACKET\n{_fact_packet(row)}" if include_packet else ""
    answer = (
        f"\n\nTASK\nWhat probability should be assigned that Candidate {truth_label} is the "
        "correct description of the target person's belief? Return only one number from 0 to 100."
    )
    return _source_block(row) + "\n\n" + target_block + packet + answer


def build_candidate(row: dict[str, Any]) -> InformationSetItem:
    validate_source_row(row)
    belief = eligible_first_order_qa(row)
    boundary = _boundary_probe(row)
    options = _option_map(row)
    item = InformationSetItem(
        source_id=SOURCE_ID,
        independent_unit_id=str(row["part_id"]),
        boundary_type="perspective",
        reference_context={
            "set_id": str(row["set_id"]),
            "part_id": str(row["part_id"]),
            "conversation_id": str(row["conv_id"]),
            "target_character": str(row["joining_speaker"]),
            "belief_question": str(belief["question"]),
            "source_correct_belief_answer": str(belief["correct_answer"]),
            "truth_belief_answer": str(belief["wrong_answer"]),
            "truth_belief_option": options["truth_label"],
            "source_correct_option": options["source_correct_label"],
            "fact_question": str(row["factQA"]["question"]),
            "fact_answer": str(row["factQA"]["correct_answer"]),
            "fact_distractor": str(row["factQA"]["wrong_answer"]),
            "boundary_probe_question": str(boundary["question"]),
            "boundary_probe_answer": str(boundary["correct_answer"]),
            "critical_packet": _fact_packet(row),
        },
        oob_variant={
            "target_information_set": "target character at end of source conversation",
            "without_information_prompt": _task(row, allowed=False, include_packet=False),
            "with_information_prompt": _task(row, allowed=False, include_packet=True),
        },
        admissible_variant={
            "target_information_set": "target character after an explicit post-conversation briefing",
            "without_information_prompt": _task(row, allowed=True, include_packet=False),
            "with_information_prompt": _task(row, allowed=True, include_packet=True),
        },
        provenance={
            "source_url": SOURCE_URL,
            "source_revision": SOURCE_REVISION,
            "source_file": "fantom_v1.json",
            "source_file_sha256": SOURCE_JSON_SHA256,
            "source_archive_sha256": SOURCE_ARCHIVE_SHA256,
            "source_record_id": str(row["set_id"]),
            "reuse_status": "OFFICIAL_EVALUATION_ONLY_LOCAL_REVIEW_REDISTRIBUTION_VERIFY",
            "transformation_contract": "FANTOM_TRANSFORMATION_CONTRACT.md#candidate-v01",
        },
        transformation_id=TRANSFORMATION_ID,
    )
    return InformationSetItem.from_dict(item.to_dict())


def validate_candidate_against_source(item: InformationSetItem, row: dict[str, Any]) -> None:
    validate_source_row(row)
    if item.independent_unit_id != str(row["part_id"]):
        raise ValueError("candidate/source independent-unit mismatch")
    expected = build_candidate(row)
    if item.to_dict() != expected.to_dict():
        raise ValueError(f"unregistered FANToM prompt drift for {row['set_id']}")
    packet = _fact_packet(row)
    for variant in (item.oob_variant, item.admissible_variant):
        if packet in variant["without_information_prompt"]:
            raise ValueError("fact packet leaked into WITHOUT prompt")
        if variant["with_information_prompt"].count(packet) != 1:
            raise ValueError("fact packet must occur exactly once in WITH prompt")


def deterministic_review_sample(
    rows: list[dict[str, Any]],
    *,
    n: int = 8,
    seed: int = 20260829,
    exclude_part_ids: tuple[str, ...] | list[str] = (),
) -> list[dict[str, Any]]:
    if n <= 0:
        raise ValueError("n must be positive")
    excluded = {str(part_id) for part_id in exclude_part_ids}
    by_part: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        try:
            validate_source_row(row)
        except ValueError:
            continue
        part_id = str(row["part_id"])
        if part_id in excluded:
            continue
        by_part.setdefault(part_id, []).append(row)
    representatives = []
    for part_id, candidates in by_part.items():
        selected = min(
            candidates,
            key=lambda row: hashlib.sha256(
                f"{seed}:row:{row['set_id']}".encode()
            ).hexdigest(),
        )
        representatives.append((
            hashlib.sha256(f"{seed}:part:{part_id}".encode()).hexdigest(),
            selected,
        ))
    if len(representatives) < n:
        raise ValueError("not enough eligible independent FANToM parts")
    return [row for _, row in sorted(representatives)[:n]]
