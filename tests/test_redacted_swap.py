from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from adapters.btf3_hindsight_depth import residual_verdict_hits
from adapters.btf3_packet_swap import PACKET_HEADER, TASK_HEADER, build_swapped, pairing_digest
from adapters.btf3_redacted_swap import build_redacted_swapped
from information_set_schema import load_jsonl

ARTIFACT = ROOT / "data/external/review/btf3_temporal_large_replication_v1.jsonl"


def test_redacted_swap_preserves_pairing_and_changes_only_packet():
    items = load_jsonl(ARTIFACT)
    full = build_swapped(items)
    red = build_redacted_swapped(items)
    assert pairing_digest(full) == pairing_digest(red)
    assert [r["donor_unit_id"] for r in full] == [r["donor_unit_id"] for r in red]
    for a, b in zip(full, red, strict=True):
        a0, a1 = a["prompt"].index(PACKET_HEADER) + len(PACKET_HEADER), a["prompt"].index(TASK_HEADER)
        b0, b1 = b["prompt"].index(PACKET_HEADER) + len(PACKET_HEADER), b["prompt"].index(TASK_HEADER)
        assert a["prompt"][:a0] == b["prompt"][:b0]
        assert a["prompt"][a1:] == b["prompt"][b1:]


def test_no_assertive_verdict_survives_and_redaction_is_subtractive():
    records = build_redacted_swapped(load_jsonl(ARTIFACT))
    assert sum(r["verdict_sentences_removed"] for r in records) > 0
    for r in records:
        start = r["prompt"].index(PACKET_HEADER) + len(PACKET_HEADER)
        end = r["prompt"].index(TASK_HEADER, start)
        assert not [h for h in residual_verdict_hits(r["prompt"][start:end]) if h["assertive"]]

