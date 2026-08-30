from src.adapters.fomc_temporal import (
    build_candidate,
    derive_labeled_units,
    extract_statement_body,
    validate_candidate_against_manifest,
)


def meeting(date, verb, rng, url_suffix="a"):
    return {
        "date": date,
        "statement_url": f"https://www.federalreserve.gov/newsevents/pressreleases/monetary{date}{url_suffix}.htm",
        "statement_text_sha256": "0" * 64,
        "action_verb": verb,
        "action_range": rng,
        "extraction_method": "verb",
    }


def test_derive_labeled_units_labels_by_next_meetings_own_verb():
    meetings = {
        "20081216": meeting("20081216", "establish", "0 to 1/4"),
        "20090128": meeting("20090128", "keep", "0 to 1/4"),
        "20090318": meeting("20090318", "maintain", "0 to 1/4"),
        "20150318": meeting("20150318", "raise", "1/4 to 1/2"),
    }
    units = derive_labeled_units(meetings, pool_start="20081216")
    assert units == [
        {"previous": "20081216", "next": "20090128", "verb": "keep", "change": 0},
        {"previous": "20090128", "next": "20090318", "verb": "maintain", "change": 0},
        {"previous": "20090318", "next": "20150318", "verb": "raise", "change": 1},
    ]


def test_pool_start_meeting_never_becomes_a_next_meeting():
    meetings = {
        "20081216": meeting("20081216", "establish", "0 to 1/4"),
        "20090128": meeting("20090128", "keep", "0 to 1/4"),
    }
    units = derive_labeled_units(meetings, pool_start="20081216")
    assert all(u["next"] != "20081216" for u in units)


def test_extraction_failure_drops_the_pair_not_the_whole_run():
    meetings = {
        "20081216": meeting("20081216", "establish", "0 to 1/4"),
        "20090128": meeting("20090128", None, None),
        "20090318": meeting("20090318", "maintain", "0 to 1/4"),
    }
    units = derive_labeled_units(meetings, pool_start="20081216")
    assert len(units) == 1
    assert units[0] == {"previous": "20090128", "next": "20090318", "verb": "maintain", "change": 0}


def test_extract_statement_body_isolates_text_between_dateline_and_footer():
    page = (
        "nav chrome ... For immediate release Share The Committee decided to "
        "raise the target range for the federal funds rate to 1/4 to 1/2 percent. "
        "Last Update: June 15, 2022 footer chrome"
    )
    body = extract_statement_body(page)
    assert body == (
        "The Committee decided to raise the target range for the federal funds "
        "rate to 1/4 to 1/2 percent."
    )
    assert "nav chrome" not in body
    assert "footer chrome" not in body


def test_build_candidate_holds_source_text_and_target_question_fixed():
    meetings = {
        "20220615": meeting("20220615", "raise", "1-1/2 to 1-3/4"),
        "20220727": meeting("20220727", "raise", "2-1/4 to 2-1/2"),
    }
    unit = {"previous": "20220615", "next": "20220727", "verb": "raise", "change": 1}
    prev_text = "The Committee decided to raise the target range to 1-1/2 to 1-3/4 percent."
    next_text = "The Committee decided to raise the target range to 2-1/4 to 2-1/2 percent."
    item = build_candidate(
        unit, meetings, previous_text=prev_text, next_text=next_text, manifest_sha256="a" * 64
    )
    oob = item.oob_variant
    allowed = item.admissible_variant
    assert next_text not in oob["without_information_prompt"]
    assert next_text not in allowed["without_information_prompt"]
    assert next_text in oob["with_information_prompt"]
    assert next_text in allowed["with_information_prompt"]
    for prompt in (
        oob["without_information_prompt"], oob["with_information_prompt"],
        allowed["without_information_prompt"], allowed["with_information_prompt"],
    ):
        assert prev_text in prompt
        assert "Return only one number from 0 to 100" in prompt
    assert item.reference_context["outcome_alignment_sign"] == 1
    assert item.independent_unit_id == "20220615_20220727"
    validate_candidate_against_manifest(item, meetings, previous_text=prev_text, next_text=next_text)


def test_build_candidate_hold_has_negative_alignment_sign():
    meetings = {
        "20250129": meeting("20250129", "maintain", "4-1/4 to 4-1/2"),
        "20250319": meeting("20250319", "maintain", "4-1/4 to 4-1/2"),
    }
    unit = {"previous": "20250129", "next": "20250319", "verb": "maintain", "change": 0}
    item = build_candidate(
        unit, meetings, previous_text="prev text", next_text="next text", manifest_sha256="a" * 64
    )
    assert item.reference_context["outcome_alignment_sign"] == -1
    assert item.reference_context["realized_resolution"] == 0
