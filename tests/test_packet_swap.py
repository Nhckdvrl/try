"""Tests for the G8 packet-swap pairing, builder, and decision rules."""

from __future__ import annotations

from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from adapters.btf3_packet_swap import (  # noqa: E402
    PACKET_HEADER,
    TASK_HEADER,
    build_swapped,
    derangement,
    extract_packet,
    pairing_digest,
)
from analyze_packet_swap import interpretation  # noqa: E402
from information_set_schema import load_jsonl  # noqa: E402

ARTIFACT = ROOT / "data/external/review/btf3_temporal_large_replication_v1.jsonl"


@pytest.fixture(scope="module")
def items():
    return load_jsonl(ARTIFACT)


@pytest.mark.parametrize("n", [2, 3, 10, 256])
def test_derangement_is_a_single_cycle_bijection(n):
    mapping = derangement(n)
    assert sorted(mapping) == list(range(n))
    assert all(mapping[i] != i for i in range(n))
    # single cycle: following the map from 0 visits every element before returning
    seen, node = set(), 0
    for _ in range(n):
        seen.add(node)
        node = mapping[node]
    assert seen == set(range(n)) and node == 0


def test_derangement_is_deterministic():
    assert derangement(256) == derangement(256)
    assert derangement(256) != derangement(256, seed=1)


def test_swapped_prompt_changes_only_the_packet(items):
    records = build_swapped(items)
    for record, item in list(zip(records, items))[:20]:
        source = item.oob_variant["with_information_prompt"]
        swapped = record["prompt"]
        head = source[: source.index(PACKET_HEADER) + len(PACKET_HEADER)]
        tail = source[source.index(TASK_HEADER, source.index(PACKET_HEADER)):]
        assert swapped.startswith(head)
        assert swapped.endswith(tail)


def test_no_unit_receives_its_own_packet(items):
    records = build_swapped(items)
    packets = {item.independent_unit_id: extract_packet(item.oob_variant["with_information_prompt"])
               for item in items}
    for record in records:
        assert record["donor_unit_id"] != record["independent_unit_id"]
        assert extract_packet(record["prompt"] + TASK_HEADER if TASK_HEADER not in record["prompt"] else record["prompt"]) == packets[record["donor_unit_id"]]


def test_every_packet_is_used_exactly_once(items):
    records = build_swapped(items)
    donors = [r["donor_unit_id"] for r in records]
    assert sorted(donors) == sorted(r["independent_unit_id"] for r in records)


def test_pairing_has_both_directions(items):
    records = build_swapped(items)
    opposite = sum(1 for r in records if r["direction"] != r["donor_direction"])
    # the analysis needs a usable number of opposite-direction pairs
    assert opposite >= 50


def test_pairing_digest_is_stable(items):
    assert pairing_digest(build_swapped(items)) == pairing_digest(build_swapped(items))


@pytest.mark.parametrize(
    "donor_positive,substantial,row",
    [
        (True, True, "H-presence-strong"),
        (True, False, "H-presence-strong"),
        (False, True, "H-presence-weak"),
        (False, False, "H-content"),
    ],
)
def test_interpretation_table(donor_positive, substantial, row):
    assert interpretation(donor_positive, substantial)[0] == row
