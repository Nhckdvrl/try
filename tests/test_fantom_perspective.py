import copy
import json
from pathlib import Path

import pytest

from src.adapters.fantom_perspective import (
    build_candidate,
    deterministic_review_sample,
    validate_candidate_against_source,
    validate_source_row,
)


RAW = Path("data/external/raw/fantom/fantom_v1.json")


def source_rows():
    return json.loads(RAW.read_text(encoding="utf-8"))


@pytest.mark.skipif(not RAW.exists(), reason="raw FANToM cache absent")
def test_candidate_uses_one_source_question_and_exact_packet():
    row = deterministic_review_sample(source_rows(), n=1)[0]
    item = build_candidate(row)
    packet = item.reference_context["critical_packet"]
    prompts = (
        item.oob_variant["without_information_prompt"],
        item.oob_variant["with_information_prompt"],
        item.admissible_variant["without_information_prompt"],
        item.admissible_variant["with_information_prompt"],
    )
    assert all(item.reference_context["belief_question"] in prompt for prompt in prompts)
    assert packet not in prompts[0] and packet not in prompts[2]
    assert prompts[1].count(packet) == 1 and prompts[3].count(packet) == 1
    assert all("Return only one number from 0 to 100" in prompt for prompt in prompts)
    validate_candidate_against_source(item, row)


@pytest.mark.skipif(not RAW.exists(), reason="raw FANToM cache absent")
def test_prompt_drift_fails_closed():
    row = deterministic_review_sample(source_rows(), n=1)[0]
    item = build_candidate(row)
    item.oob_variant["with_information_prompt"] += "\nUNREGISTERED"
    with pytest.raises(ValueError, match="unregistered FANToM prompt drift"):
        validate_candidate_against_source(item, row)


@pytest.mark.skipif(not RAW.exists(), reason="raw FANToM cache absent")
def test_selection_is_deterministic_and_one_per_part():
    rows = source_rows()
    eligible = []
    for row in rows:
        try:
            validate_source_row(row)
        except ValueError:
            continue
        eligible.append(row)
    assert len(eligible) == 636
    assert len({row["part_id"] for row in eligible}) == 335
    a = deterministic_review_sample(rows, n=8, seed=17)
    b = deterministic_review_sample(rows, n=8, seed=17)
    assert [row["set_id"] for row in a] == [row["set_id"] for row in b]
    assert len({row["part_id"] for row in a}) == 8


@pytest.mark.skipif(not RAW.exists(), reason="raw FANToM cache absent")
def test_rejected_parts_are_replaced_without_changing_sample_size():
    rows = source_rows()
    initial = deterministic_review_sample(rows, n=8)
    rejected = [initial[1]["part_id"], initial[4]["part_id"]]
    replacement = deterministic_review_sample(
        rows, n=8, exclude_part_ids=rejected
    )
    replacement_parts = {row["part_id"] for row in replacement}
    assert not set(rejected) & replacement_parts
    assert len(replacement_parts) == 8
    assert len({row["part_id"] for row in initial} & replacement_parts) == 6


@pytest.mark.skipif(not RAW.exists(), reason="raw FANToM cache absent")
def test_accessible_or_second_order_rows_are_ineligible():
    row = deterministic_review_sample(source_rows(), n=1)[0]
    bad = copy.deepcopy(row)
    for qa in bad["beliefQAs"]:
        if qa["tom_type"] == "first-order":
            qa["missed_info_accessibility"] = "accessible"
    with pytest.raises(ValueError, match="first-order inaccessible"):
        validate_source_row(bad)
