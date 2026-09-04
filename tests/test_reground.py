from schema import Item
from reground import (
    compiler_message,
    decision_messages,
    gold_selection,
    parse_selection,
    retrieved_docs,
    selector_prompt,
    target_descriptor,
    wrong_proposition,
)
from schema import SYSTEM, ANSWER_FORMATS


def _item():
    return Item(
        item_id="x",
        task_family="legal_judgment",
        surface_domain="demo",
        base_context="The base case is balanced.",
        critical_evidence="A witness says the defendant confessed.",
        critical_label="the witness statement",
        critical_direction="increase",
        exclusion_reason="access_control",
        evidence_truth="true_but_forbidden",
        admit_rule="Use the witness statement.",
        exclude_rule="Do not use the witness statement.",
        question="Rate the probability of guilt.",
        output_spec="Use a scale from 0 to 9.",
        memory_question="What did the witness say?",
        rule_probe_question="May the witness statement influence the answer?",
        meta={
            "skeleton": "demo:x",
            "previews": {
                "para": "PRELIMINARY NOTE\nA witness reports that the defendant admitted it.",
                "empty": "PRELIMINARY NOTE\nA witness reports that the interview room was repainted.",
            },
        },
    )


def test_target_and_wrong_are_distinct():
    it = _item()
    assert "admitted" in target_descriptor(it)
    assert "repainted" in wrong_proposition(it)
    assert target_descriptor(it) != wrong_proposition(it)


def test_variants_place_expected_documents():
    it = _item()
    assert ("D7", it.critical_evidence) in retrieved_docs(it, "same_d7")
    assert ("D9", it.critical_evidence) in retrieved_docs(it, "same_d9")
    wrong = dict(retrieved_docs(it, "wrong_d9"))
    assert wrong["D7"] == wrong_proposition(it)


def test_selector_parser_is_strict_to_document_ids():
    assert parse_selection("D9") == {"D9"}
    assert parse_selection("D7, D11") == {"D7", "D11"}
    assert parse_selection("NONE") == set()
    assert parse_selection("none - no match") == set()


def test_gold_selection():
    assert gold_selection("same_d7") == {"D7"}
    assert gold_selection("same_d9") == {"D9"}
    assert gold_selection("wrong_d9") == set()


def test_compiler_none_explicitly_prevents_overextension():
    msg = compiler_message(set())
    assert "EXCLUDED DOCUMENTS: NONE" in msg
    assert "Do not exclude any retrieved document" in msg


def test_self_decision_never_copies_semantic_descriptor():
    it = _item()
    msgs = decision_messages(
        it,
        "self",
        "same_d9",
        SYSTEM,
        ANSWER_FORMATS["reasoned"],
        selection={"D9"},
    )
    rendered = "\n".join(m["content"] for m in msgs)
    assert "EXCLUDED DOCUMENTS: D9" in rendered
    # The semantic descriptor belongs to the hidden resolver, not the final prompt.
    assert target_descriptor(it) not in rendered


def test_semantic_pre_exposes_descriptor_as_control():
    it = _item()
    msgs = decision_messages(
        it,
        "sempre",
        "same_d7",
        SYSTEM,
        ANSWER_FORMATS["reasoned"],
    )
    rendered = "\n".join(m["content"] for m in msgs)
    assert target_descriptor(it) in rendered


def test_selector_prompt_has_hard_negative_but_not_answer_question():
    it = _item()
    prompt = selector_prompt(it, "wrong_d9")
    assert target_descriptor(it) in prompt
    assert wrong_proposition(it) in prompt
    assert it.question not in prompt
