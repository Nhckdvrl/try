"""Packet-swap builder for PREREGISTRATION_G8_RELEVANCE.md.

One manipulation on the frozen 256-unit artifact: unit *i* keeps everything —
its question, criteria, background, target information set, and task — but its
``LATER RESOLUTION PACKET`` is replaced by the packet of a different unit
``pi(i)``. The substituted packet is still explicitly labelled as post-cutoff
and is still out of set; the only thing that changes is that it is no longer
*about this question*.

The pairing is a fixed derangement computed from the frozen artifact order with
a recorded seed. It is constructed so that:

* no unit receives its own packet;
* the pairing is a single cycle, so it is a bijection and every packet is used
  exactly once;
* realized outcomes are crossed deliberately — the analysis needs units whose
  foreign packet points the opposite way, so pairing is *not* stratified by
  outcome, and the resulting cross-tabulation is reported.

Nothing here consults any target-model output.
"""
from __future__ import annotations

import hashlib

try:
    from ..information_set_schema import InformationSetItem
except ImportError:  # direct use with PYTHONPATH=src
    from information_set_schema import InformationSetItem

PACKET_HEADER = "\n\nLATER RESOLUTION PACKET\n"
TASK_HEADER = "\n\nTASK\n"
PAIRING_SEED = 20260901


def extract_packet(prompt: str) -> str:
    """The packet body, without its header, from a WITH prompt."""
    start = prompt.index(PACKET_HEADER) + len(PACKET_HEADER)
    end = prompt.index(TASK_HEADER, start)
    return prompt[start:end]


def derangement(n: int, *, seed: int = PAIRING_SEED) -> list[int]:
    """A fixed single-cycle derangement of ``range(n)``.

    Built from a seeded shuffle turned into one cycle, so it is a derangement by
    construction rather than by rejection sampling — the result does not depend
    on how many attempts a rejection loop happened to need.
    """
    import random

    order = list(range(n))
    random.Random(seed).shuffle(order)
    mapping = [0] * n
    for index, unit in enumerate(order):
        mapping[unit] = order[(index + 1) % n]
    assert all(mapping[i] != i for i in range(n)), "single-cycle map must be a derangement"
    assert sorted(mapping) == list(range(n)), "must be a bijection"
    return mapping


def build_swapped(items: list[InformationSetItem], *, seed: int = PAIRING_SEED) -> list[dict]:
    """One record per unit: the WITH prompt carrying another unit's packet."""
    mapping = derangement(len(items), seed=seed)
    packets = [extract_packet(item.oob_variant["with_information_prompt"]) for item in items]
    records = []
    for index, item in enumerate(items):
        donor = mapping[index]
        prompt = item.oob_variant["with_information_prompt"]
        start = prompt.index(PACKET_HEADER) + len(PACKET_HEADER)
        end = prompt.index(TASK_HEADER, start)
        swapped = prompt[:start] + packets[donor] + prompt[end:]
        records.append({
            "independent_unit_id": item.independent_unit_id,
            "donor_unit_id": items[donor].independent_unit_id,
            "prompt": swapped,
            "direction": int(item.reference_context.get("outcome_alignment_sign", 1)),
            "donor_direction": int(items[donor].reference_context.get("outcome_alignment_sign", 1)),
            "realized_resolution": item.reference_context.get("realized_resolution"),
            "donor_realized_resolution": items[donor].reference_context.get("realized_resolution"),
        })
    return records


def pairing_digest(records: list[dict]) -> str:
    """Stable digest of the pairing, so the freeze can be checked after the fact."""
    payload = "\n".join(f"{r['independent_unit_id']}->{r['donor_unit_id']}" for r in records)
    return hashlib.sha256(payload.encode()).hexdigest()
