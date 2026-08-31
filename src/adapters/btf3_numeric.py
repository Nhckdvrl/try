"""BTF-3 numeric-track adapter — a second task type for the same question.

The binary track asks for the probability that a yes/no question resolves YES.
The numeric track asks for a *quantity*. To keep the readout, the estimator, and
every threshold in this project byte-identical, each numeric question is turned
into a threshold question by a frozen rule:

    "Will the resolved value be strictly less than <cutpoint_3> <units>?"

`cutpoint_3` is the source's own middle cutpoint — chosen by the dataset's
authors, not by us, and never by anything a model produced. The source's
resolution criteria are carried verbatim as the definition of the measured
quantity, and the threshold sentence is the only text this transform adds.

Two things this buys that the binary track cannot:

* a **different task type** for the same scientific object, so the phenomenon
  is not a property of probability-of-YES readouts;
* a ready-made independent ex-ante anchor, `sota_forecast_cdf_3`, which is by
  construction the SOTA forecaster's `P(value < cutpoint_3)` — the exact
  quantity the model is asked for.

Nothing here consults any target-model output.
"""
from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any

try:
    from ..information_set_schema import InformationSetItem
except ImportError:  # direct adapter use with PYTHONPATH=src
    from information_set_schema import InformationSetItem

SOURCE_ID = "btf3-numeric"
SOURCE_REVISION = "4b426627e19cd86202de69a40bc9dadb7f5ccd59"
SOURCE_URL = "https://huggingface.co/datasets/BTF-2/BTF-3"
SOURCE_FILE = "btf3_numeric_questions_and_forecasts.parquet"
SOURCE_SHA256 = "1bee10210dabcfcc41d052e7d6458d3674f87b40e1a8f07ab1796fc040ca0747"
TRANSFORMATION_ID = "btf3-numeric-threshold-v0.1"
CUTPOINT = "cutpoint_3"
ANCHOR = "sota_forecast_cdf_3"

REQUIRED = (
    "question_id", "question", "resolution_criteria", "background",
    "present_date", "date_cutoff_end", "expected_resolution_date",
    "units", CUTPOINT, "resolution", "resolution_explanation",
)


def _iso(value: Any) -> datetime:
    return datetime.fromisoformat(str(value).replace("Z", "+00:00"))


def _utc_source_day(row: dict[str, Any]) -> str:
    return _iso(row["present_date"]).date().isoformat()


def _format_number(value: float) -> str:
    """Render a cutpoint without inventing precision the source did not have."""
    text = f"{float(value):.10g}"
    return text


def validate_source_row(row: dict[str, Any]) -> None:
    missing = [key for key in REQUIRED if key not in row]
    if missing:
        raise ValueError(f"BTF-3 numeric row missing {missing}")
    for key in REQUIRED:
        value = row[key]
        if value is None or (isinstance(value, str) and not value.strip()):
            raise ValueError(f"BTF-3 numeric field {key} is empty")
    for key in (CUTPOINT, "resolution"):
        number = float(row[key])
        if number != number:  # NaN
            raise ValueError(f"BTF-3 numeric field {key} is NaN")
    if float(row["resolution"]) == float(row[CUTPOINT]):
        # A resolution exactly on the cutpoint makes "strictly less than" a
        # knife-edge; such rows are excluded rather than resolved by convention.
        raise ValueError("resolution sits exactly on the cutpoint")

    present = _iso(row["present_date"])
    cutoff = _iso(row["date_cutoff_end"])
    expected = _iso(row["expected_resolution_date"])
    if present >= expected:
        raise ValueError("present_date must precede expected_resolution_date")
    if cutoff.date() != present.date() + timedelta(days=1) or cutoff.time() != datetime.min.time():
        raise ValueError(
            "unexpected BTF-3 cutoff encoding: date_cutoff_end must be the midnight "
            "boundary immediately after the UTC day containing present_date"
        )


def threshold_sentence(row: dict[str, Any]) -> str:
    return (
        f"Will the resolved value be strictly less than "
        f"{_format_number(row[CUTPOINT])} {row['units']}?"
    )


def _source_block(row: dict[str, Any]) -> str:
    return (
        f"FORECASTING QUESTION\n{threshold_sentence(row)}\n\n"
        f"QUANTITY BEING MEASURED\n{row['question']}\n\n"
        f"RESOLUTION CRITERIA\n{row['resolution_criteria']}\n\n"
        f"BACKGROUND AVAILABLE AS OF {row['present_date']}\n{row['background']}"
    )


def _task(row: dict[str, Any], *, ex_ante: bool, include_packet: bool) -> str:
    source = _source_block(row)
    if ex_ante:
        target = (
            "TARGET INFORMATION SET\n"
            f"Estimate the probability that was warranted as of {row['present_date']}. "
            f"Use only information available through the end of UTC day {_utc_source_day(row)}, "
            f"which the source encodes with date_cutoff_end={row['date_cutoff_end']}. "
            "Do not treat the following UTC calendar day as available. "
            "Any text explicitly labeled LATER RESOLUTION PACKET was produced after this "
            "information set and is not part of the evidence that defines the requested ex-ante forecast."
        )
    else:
        target = (
            "TARGET INFORMATION SET\n"
            "Make a retrospective probability judgment using all information supplied in "
            "this prompt, including any LATER RESOLUTION PACKET."
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
    below = float(row["resolution"]) < float(row[CUTPOINT])
    resolution = 1 if below else 0
    anchor = row.get(ANCHOR)
    shared = {
        "question": threshold_sentence(row),
        "source_question": row["question"],
        "units": str(row["units"]),
        "cutpoint": float(row[CUTPOINT]),
        "resolved_value": float(row["resolution"]),
        "resolution_criteria": row["resolution_criteria"],
        "background": row["background"],
        "present_date": str(row["present_date"]),
        "date_cutoff_end": str(row["date_cutoff_end"]),
        "source_utc_day": _utc_source_day(row),
        "expected_resolution_date": str(row["expected_resolution_date"]),
        "realized_resolution": resolution,
        "outcome_alignment_sign": 1 if resolution == 1 else -1,
        "exante_anchor": None if anchor is None or anchor != anchor else float(anchor),
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
            "source_file": SOURCE_FILE,
            "source_file_sha256": SOURCE_SHA256,
            "source_record_id": str(row["question_id"]),
            "reuse_status": "CC_BY_NC_4_0_REVIEW_CANDIDATE_NOT_FROZEN",
            "transformation_contract": "BTF3_NUMERIC_TRANSFORMATION_CONTRACT.md#v0.1",
            "cutpoint_field": CUTPOINT,
            "anchor_field": ANCHOR,
        },
        transformation_id=TRANSFORMATION_ID,
    )
    return InformationSetItem.from_dict(item.to_dict())


def validate_candidate_against_source(item: InformationSetItem, row: dict[str, Any]) -> None:
    """Prove a serialized candidate is exactly the registered four-cell transform."""
    validate_source_row(row)
    qid = str(row["question_id"])
    if item.independent_unit_id != qid:
        raise ValueError(f"candidate/source ID mismatch: {item.independent_unit_id} != {qid}")
    expected = {
        ("oob_variant", "without_information_prompt"): _task(row, ex_ante=True, include_packet=False),
        ("oob_variant", "with_information_prompt"): _task(row, ex_ante=True, include_packet=True),
        ("admissible_variant", "without_information_prompt"): _task(row, ex_ante=False, include_packet=False),
        ("admissible_variant", "with_information_prompt"): _task(row, ex_ante=False, include_packet=True),
    }
    variants = {"oob_variant": item.oob_variant, "admissible_variant": item.admissible_variant}
    for (variant_name, prompt_name), expected_prompt in expected.items():
        if variants[variant_name][prompt_name] != expected_prompt:
            raise ValueError(f"unregistered prompt drift for {qid} {variant_name}.{prompt_name}")

    packet = str(row["resolution_explanation"])
    for variant in variants.values():
        if packet in variant["without_information_prompt"]:
            raise ValueError(f"later packet leaked into WITHOUT prompt for {qid}")
        if variant["with_information_prompt"].count(packet) != 1:
            raise ValueError(f"later packet is not present exactly once in WITH prompt for {qid}")
