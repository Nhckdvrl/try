"""G12 paired redacted YES/NO donor-packet construction."""
from __future__ import annotations

import hashlib
import random

try:
    from .btf3_hindsight_depth import redact_verdicts
    from .btf3_packet_swap import (
        PAIRING_SEED,
        PACKET_HEADER,
        TASK_HEADER,
        derangement,
        extract_packet,
    )
except ImportError:
    from adapters.btf3_hindsight_depth import redact_verdicts
    from adapters.btf3_packet_swap import (
        PAIRING_SEED,
        PACKET_HEADER,
        TASK_HEADER,
        derangement,
        extract_packet,
    )


def _balanced_assignment(items, donor_indices: list[int], *, seed: int, forbidden: list[int]) -> list[int]:
    """Assign every donor exactly twice, avoiding own and frozen-G8 donors."""
    if len(donor_indices) * 2 != len(items):
        raise ValueError("G12 requires exactly half the donors in each outcome stratum")
    recipients = list(range(len(items)))
    random.Random(seed).shuffle(recipients)
    pool = donor_indices * 2
    random.Random(seed + 1).shuffle(pool)
    for shift in range(len(pool)):
        rotated = pool[shift:] + pool[:shift]
        if all(d != r and d != forbidden[r] for r, d in zip(recipients, rotated)):
            out = [0] * len(items)
            for r, d in zip(recipients, rotated):
                out[r] = d
            return out
    raise RuntimeError("could not construct a balanced assignment without forbidden donors")


def build_donor_pairs(items, *, seed: int = PAIRING_SEED) -> list[dict]:
    signs = [int(item.reference_context.get("outcome_alignment_sign", 1)) for item in items]
    yes = [i for i, sign in enumerate(signs) if sign == 1]
    no = [i for i, sign in enumerate(signs) if sign == -1]
    if len(yes) != 128 or len(no) != 128:
        raise ValueError(f"expected 128/128 outcomes, got {len(yes)}/{len(no)}")
    frozen_g8 = derangement(len(items), seed=seed)
    yes_assignment = _balanced_assignment(items, yes, seed=seed + 101, forbidden=frozen_g8)
    no_assignment = _balanced_assignment(items, no, seed=seed + 202, forbidden=frozen_g8)
    packets = [extract_packet(item.oob_variant["with_information_prompt"]) for item in items]

    records = []
    for i, item in enumerate(items):
        base = item.oob_variant["with_information_prompt"]
        start = base.index(PACKET_HEADER) + len(PACKET_HEADER)
        end = base.index(TASK_HEADER, start)
        entry = {
            "independent_unit_id": item.independent_unit_id,
            "recipient_direction": signs[i],
        }
        for label, donor in (("yes", yes_assignment[i]), ("no", no_assignment[i])):
            red = redact_verdicts(packets[donor])
            entry[label] = {
                "donor_unit_id": items[donor].independent_unit_id,
                "donor_index": donor,
                "prompt": base[:start] + red.text + base[end:],
                "verdict_sentences_removed": red.n_removed,
                "clauses_preserved": len(red.preserved_clauses),
            }
        records.append(entry)
    return records


def assignment_digest(records: list[dict]) -> str:
    payload = "\n".join(
        f"{r['independent_unit_id']}|Y:{r['yes']['donor_unit_id']}|N:{r['no']['donor_unit_id']}"
        for r in records
    )
    return hashlib.sha256(payload.encode()).hexdigest()

