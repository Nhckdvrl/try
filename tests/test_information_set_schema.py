import copy

import pytest

from src.information_set_schema import InformationSetItem, validate_collection


def valid_record():
    return {
        "source_id": "native_source",
        "independent_unit_id": "unit-1",
        "boundary_type": "perspective",
        "reference_context": {"dialogue": "Alice left. Bob moved the cup."},
        "oob_variant": {"question": "Where does Alice think the cup is?", "answer": "table"},
        "admissible_variant": {"question": "Where is the cup?", "answer": "shelf"},
        "provenance": {
            "source_url": "https://example.org/data",
            "source_revision": "v1",
            "source_file": "source.json",
            "source_file_sha256": "a" * 64,
            "source_record_id": "row-1",
            "reuse_status": "READY",
        },
        "transformation_id": "native-v1",
    }


def test_valid_source_native_record():
    item = InformationSetItem.from_dict(valid_record())
    assert item.record_id == "native_source:unit-1:native-v1"
    assert validate_collection([item])["n_independent_units"] == 1


@pytest.mark.parametrize("field", ["source_id", "independent_unit_id", "transformation_id"])
def test_required_identifiers_cannot_be_empty(field):
    record = valid_record()
    record[field] = ""
    with pytest.raises(ValueError):
        InformationSetItem.from_dict(record)


def test_old_universal_rule_fields_are_rejected_even_when_nested():
    record = valid_record()
    record["oob_variant"]["exclude_rule"] = "ignore this"
    with pytest.raises(ValueError, match="universal compiler"):
        InformationSetItem.from_dict(record)


def test_variants_must_encode_an_actual_intervention():
    record = valid_record()
    record["oob_variant"] = copy.deepcopy(record["admissible_variant"])
    with pytest.raises(ValueError, match="must differ"):
        InformationSetItem.from_dict(record)


def test_duplicate_record_id_is_rejected():
    item = InformationSetItem.from_dict(valid_record())
    with pytest.raises(ValueError, match="duplicate"):
        validate_collection([item, item])
