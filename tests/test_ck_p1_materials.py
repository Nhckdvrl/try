from __future__ import annotations
from collections import Counter, defaultdict
from ck_p1_materials import DEPTHS, FORBIDDEN_VISIBLE_TERMS, STRUCTURES, build_contexts, validate_contexts

def test_ck_p1_has_24_independent_matched_quartets():
    rows = build_contexts()
    validate_contexts(rows)
    assert len(rows) == 96
    counts = Counter(row["skeleton_id"] for row in rows)
    assert len(counts) == 24 and set(counts.values()) == {4}

def test_each_quartet_keeps_content_and_query_fixed():
    by = defaultdict(list)
    for row in build_contexts():
        by[row["skeleton_id"]].append(row)
    for quartet in by.values():
        assert {row["structure"] for row in quartet} == set(STRUCTURES)
        assert len({row["proposition"] for row in quartet}) == 1
        assert len({row["outer_agent"] for row in quartet}) == 1
        assert len({tuple(q["statement"] for q in row["queries"]) for row in quartet}) == 1

def test_gold_is_the_frozen_staircase():
    expected = {
        "K1": ("TRUE","FALSE","FALSE","FALSE","FALSE"),
        "K2": ("TRUE","TRUE","FALSE","FALSE","FALSE"),
        "K3": ("TRUE","TRUE","TRUE","FALSE","FALSE"),
        "CK": ("TRUE","TRUE","TRUE","TRUE","TRUE"),
    }
    for row in build_contexts():
        assert tuple(q["depth"] for q in row["queries"]) == DEPTHS
        assert tuple(q["gold"] for q in row["queries"]) == expected[row["structure"]]

def test_qualification_is_only_true_for_joint_structure():
    for row in build_contexts():
        assert row["qualification"]["gold"] == ("TRUE" if row["structure"] == "CK" else "FALSE")

def test_visible_material_does_not_teach_formal_answer():
    for row in build_contexts():
        visible = (row["story"] + " " + " ".join(q["prompt"] for q in row["queries"])).lower()
        for term in FORBIDDEN_VISIBLE_TERMS:
            assert term not in visible

def test_public_cue_is_not_one_lexical_template():
    ck = [row for row in build_contexts() if row["structure"] == "CK"]
    assert Counter(row["modality"] for row in ck) == {"spoken": 12, "display": 12}
    assert any("announces" in row["story"] for row in ck)
    assert any("screen clearly displays" in row["story"] for row in ck)

def test_outer_agent_is_balanced():
    rows = [row for row in build_contexts() if row["structure"] == "K1"]
    assert sum(row["outer_agent"] == row["agent_a"] for row in rows) == 12

def test_no_story_exceeds_five_sentences():
    for row in build_contexts():
        assert row["story"].count(".") <= 5
