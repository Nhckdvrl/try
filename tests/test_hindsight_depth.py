from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from adapters.btf3_factorization import M1_REMINDER  # noqa: E402
from adapters.btf3_hindsight_depth import (  # noqa: E402
    ALLOWED_REMINDER,
    EXCLUDE_REMINDER,
    build_evr,
    build_positional,
    is_assertive_verdict,
    redact_verdicts,
    residual_verdict_hits,
)
from information_set_schema import InformationSetItem  # noqa: E402
import analyze_hindsight_depth as g2  # noqa: E402


PACKET = (
    "The question resolves NO.\n"
    "Evidence:\n"
    "- Reuters reported on May 28, 2026 that the plan was postponed.\n"
    "The official index lists no qualifying entry.\n"
    "Therefore the question resolves NO."
)


def make_item(packet: str = PACKET) -> InformationSetItem:
    def prompt(frame: str, with_packet: bool) -> str:
        text = (
            "FORECASTING QUESTION\nWill X happen?\n\n"
            "RESOLUTION CRITERIA\nResolves YES if X happens.\n\n"
            "BACKGROUND AVAILABLE AS OF 2026-05-12\nSome background.\n\n"
            f"TARGET INFORMATION SET\n{frame}"
        )
        if with_packet:
            text += f"\n\nLATER RESOLUTION PACKET\n{packet}"
        return text + "\n\nTASK\nReturn only one number from 0 to 100."

    return InformationSetItem.from_dict({
        "source_id": "btf3",
        "independent_unit_id": "q1",
        "boundary_type": "temporal",
        "reference_context": {"realized_resolution": 0, "outcome_alignment_sign": -1},
        "oob_variant": {
            "target_information_set": "ex ante",
            "without_information_prompt": prompt("ex ante", False),
            "with_information_prompt": prompt("ex ante", True),
        },
        "admissible_variant": {
            "target_information_set": "all supplied",
            "without_information_prompt": prompt("all supplied", False),
            "with_information_prompt": prompt("all supplied", True),
        },
        "provenance": {
            "source_url": "u",
            "source_revision": "r",
            "reuse_status": "s",
            "source_file": "f.parquet",
            "source_file_sha256": "0" * 64,
            "source_record_id": "q1",
        },
        "transformation_id": "t",
    })


def test_exclusion_reminder_is_byte_identical_to_the_64_unit_string():
    assert EXCLUDE_REMINDER == M1_REMINDER


def test_positional_pair_differs_only_by_reminder_position():
    item = make_item()
    for frame, reminder in (("oob", EXCLUDE_REMINDER), ("allowed", ALLOWED_REMINDER)):
        before = build_positional(item, frame=frame, position="before")
        after = build_positional(item, frame=frame, position="after")
        assert before != after
        assert before.count(reminder) == 1 and after.count(reminder) == 1
        assert before.replace(reminder, "", 1) == after.replace(reminder, "", 1)
        assert before.index(reminder) < before.index("LATER RESOLUTION PACKET")
        assert after.index(reminder) > after.index("LATER RESOLUTION PACKET")


def test_reminders_differ_only_in_the_admissibility_clause():
    assert EXCLUDE_REMINDER.startswith("\n\nREMINDER\nThe information in LATER RESOLUTION PACKET above")
    assert ALLOWED_REMINDER.startswith("\n\nREMINDER\nThe information in LATER RESOLUTION PACKET above")
    assert "must not inform your answer" in EXCLUDE_REMINDER
    assert "may inform your answer" in ALLOWED_REMINDER


def test_redaction_removes_assertive_verdicts_and_keeps_evidence():
    result = redact_verdicts(PACKET)
    assert result.n_removed == 2
    assert "resolves NO" not in result.text
    assert "Reuters reported on May 28, 2026" in result.text
    assert "The official index lists no qualifying entry." in result.text
    assert not [hit for hit in residual_verdict_hits(result.text) if hit["assertive"]]


def test_redaction_keeps_conditional_criteria_restatements():
    packet = "The question resolves YES only if a law is published by July 1.\nNo law was published."
    result = redact_verdicts(packet)
    assert result.n_removed == 0
    assert "only if" in result.text
    assert not is_assertive_verdict("The question resolves YES only if a law is published by July 1.")


def test_redaction_preserves_the_evidence_clause_of_a_because_verdict():
    packet = "The question resolves NO because no credible source confirms SAF control."
    result = redact_verdicts(packet)
    assert result.n_removed == 1
    assert result.text == "No credible source confirms SAF control."


def test_redaction_trims_a_trailing_verdict_clause_but_keeps_the_main_clause():
    packet = "No qualifying injunction was issued during the window, and the question resolves NO."
    result = redact_verdicts(packet)
    assert result.text == "No qualifying injunction was issued during the window."
    assert result.n_removed == 1


def test_redaction_is_subtractive_never_additive():
    result = redact_verdicts(PACKET)
    assert len(result.text) < len(PACKET)
    for clause in result.preserved_clauses:
        assert clause.rstrip(".") in PACKET


def test_evr_prompt_swaps_only_the_packet():
    item = make_item()
    prompt, result = build_evr(item, frame="oob")
    assert PACKET not in prompt
    assert result.text in prompt
    assert "TARGET INFORMATION SET" in prompt and "TASK" in prompt


def test_evr_is_a_noop_when_the_packet_states_no_verdict():
    packet = "Reuters reported the meeting occurred on June 3, 2026."
    item = make_item(packet)
    prompt, result = build_evr(item, frame="allowed")
    assert result.n_removed == 0
    assert packet in prompt


def test_thresholds_are_inherited_unchanged():
    assert g2.PARSE_RATE_FLOOR == 992 / 1024
    assert g2.BOUNDARY_FLOOR == 448 / 512
    assert g2.INTRUSION_SESOI == 5.0
    assert g2.EQUIVALENCE_MARGIN == 5.0
    assert g2.MIN_RESPONSIVENESS == 15.0
    assert g2.MIN_MODELS == 2
    assert g2.SEED == 20260829 and g2.N_RESAMPLES == 10_000


def test_paired_effect_cancels_the_shared_baseline():
    left = {"a": 70.0, "b": 40.0}
    right = {"a": 50.0, "b": 30.0}
    directions = {"a": 1, "b": 1}
    result = g2.paired_effect(left, right, directions)
    assert result["mean"] == pytest.approx(15.0)
    assert result["units"] == 2


def test_paired_effect_respects_direction_sign():
    left = {"a": 70.0}
    right = {"a": 50.0}
    assert g2.paired_effect(left, right, {"a": -1})["mean"] == pytest.approx(-20.0)


def test_paired_effect_can_restrict_to_a_declared_subset():
    left = {"a": 70.0, "b": 90.0}
    right = {"a": 50.0, "b": 50.0}
    directions = {"a": 1, "b": 1}
    assert g2.paired_effect(left, right, directions, units=["a"])["mean"] == pytest.approx(20.0)


def test_analyzer_encodes_the_changed_subset_veto():
    source = (ROOT / "src" / "analyze_hindsight_depth.py").read_text(encoding="utf-8")
    assert "contamination_survives_on_changed_subset" in source
    assert "experiment_b_survival_headline_permitted" in source
    # the headline requires the panel gate on BOTH the full sample and the subset
    assert "evr_models >= MIN_MODELS and evr_subset_models >= MIN_MODELS" in source
