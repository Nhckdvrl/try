from src.adapters.btf3_factorization import (
    build_m1,
    build_m1_repeat_before,
    build_m2,
    build_m2_v2,
    build_m3,
    extract_packet,
)
from src.adapters.btf3_temporal import build_candidate


def row(qid="q1", resolution=1.0):
    return {
        "question_id": qid,
        "question": "Will event X occur by June 1?",
        "resolution_criteria": "YES iff X occurs by June 1.",
        "background": "As of May 1, X had not occurred.",
        "present_date": "2026-05-01 12:00:00",
        "date_cutoff_end": "2026-05-02",
        "expected_resolution_date": "2026-06-01T00:00:00",
        "resolution": resolution,
        "resolution_explanation": "RESOLUTION: YES. X occurred on May 20.",
    }


def test_extract_packet_pulls_exact_source_native_text():
    item = build_candidate(row())
    packet = extract_packet(item.oob_variant["with_information_prompt"])
    assert packet == "RESOLUTION: YES. X occurred on May 20."


def test_m1_adds_reminder_but_keeps_everything_else_byte_identical():
    item = build_candidate(row())
    baseline = item.oob_variant["with_information_prompt"]
    m1 = build_m1(item)
    assert "REMINDER" in m1
    assert "RESOLUTION: YES. X occurred on May 20." in m1
    # removing the reminder block should reproduce the baseline exactly
    reminder_start = m1.index("\n\nREMINDER")
    reminder_end = m1.index("\n\nTASK\n")
    without_reminder = m1[:reminder_start] + m1[reminder_end:]
    assert without_reminder == baseline


def test_m2_partitions_evidence_under_new_labels_and_hides_old_ones():
    item = build_candidate(row())
    prompt, boundary = build_m2(item)
    assert "AVAILABLE AT T" in prompt
    assert "LEARNED AFTER T" in prompt
    assert "As of May 1, X had not occurred." in prompt
    assert "RESOLUTION: YES. X occurred on May 20." in prompt
    assert "BACKGROUND AVAILABLE AS OF" not in prompt
    assert "LATER RESOLUTION PACKET" not in prompt
    assert "LEARNED AFTER T" in boundary
    assert "Return only YES or NO" in boundary


def test_m3_embeds_prior_assessment_and_packet_after_ex_ante_source():
    item = build_candidate(row())
    m3 = build_m3(item, 42.0)
    assert "PRIOR ASSESSMENT" in m3
    assert "42" in m3
    assert "RESOLUTION: YES. X occurred on May 20." in m3
    # "LATER RESOLUTION PACKET" also appears once in the shared ex-ante
    # framing text itself; check ordering against the actual packet content
    # and the appended packet block's own final occurrence of the label.
    assert m3.index("PRIOR ASSESSMENT") < m3.index("RESOLUTION: YES. X occurred on May 20.")
    assert m3.rindex("LATER RESOLUTION PACKET") < m3.index("RESOLUTION: YES. X occurred on May 20.")
    assert m3.index("RESOLUTION: YES. X occurred on May 20.") < m3.index("\n\nTASK\n")


def test_m3_prior_value_formatting_has_no_trailing_zero():
    item = build_candidate(row())
    m3 = build_m3(item, 65.0)
    assert "was 65." in m3
    assert "65.0" not in m3


def test_repeat_before_and_repeat_after_are_byte_identical_except_position():
    item = build_candidate(row())
    before = build_m1_repeat_before(item)
    after = build_m1(item)
    assert len(before) == len(after)
    assert before != after
    # REPEAT-BEFORE: reminder sits before the packet.
    assert before.index("REMINDER") < before.index("RESOLUTION: YES. X occurred on May 20.")
    # REPEAT-AFTER: reminder sits after the packet, right before TASK.
    assert after.index("RESOLUTION: YES. X occurred on May 20.") < after.index("REMINDER")
    # stripping the reminder out of each should reproduce the same baseline.
    baseline = item.oob_variant["with_information_prompt"]
    b_start, b_end = before.index("\n\nREMINDER"), before.index("\n\nLATER RESOLUTION PACKET\n")
    assert before[:b_start] + before[b_end:] == baseline
    a_start, a_end = after.index("\n\nREMINDER"), after.index("\n\nTASK\n")
    assert after[:a_start] + after[a_end:] == baseline


def test_m2_v2_is_baseline_plus_two_inserted_labels_only():
    item = build_candidate(row())
    baseline = item.oob_variant["with_information_prompt"]
    m2v2 = build_m2_v2(item)
    assert "AVAILABLE AT TARGET TIME" in m2v2
    assert "LEARNED AFTER TARGET TIME" in m2v2
    # everything else, including the framing paragraph and TASK question,
    # must be byte-identical to baseline -- stripping the two inserted
    # labels must reproduce it exactly.
    stripped = m2v2.replace("AVAILABLE AT TARGET TIME\n\n", "").replace("LEARNED AFTER TARGET TIME\n\n", "")
    assert stripped == baseline
    assert "BACKGROUND AVAILABLE AS OF" in m2v2  # kept, not renamed
    assert "LATER RESOLUTION PACKET" in m2v2  # kept, not renamed
    assert "TARGET INFORMATION SET" in m2v2  # framing paragraph preserved


def test_m2_v2_reuses_generic_boundary_probe():
    from src.run_information_set import boundary_probe

    item = build_candidate(row())
    m2v2 = build_m2_v2(item)
    probe = boundary_probe(m2v2, expected="NO")
    assert "LATER RESOLUTION PACKET" in probe
    assert "Return only YES or NO" in probe
