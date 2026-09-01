"""G11: apply G2 verdict redaction to G8's frozen foreign-packet swap."""
from __future__ import annotations

try:
    from .btf3_hindsight_depth import redact_verdicts
    from .btf3_packet_swap import (
        PAIRING_SEED,
        PACKET_HEADER,
        TASK_HEADER,
        build_swapped,
    )
except ImportError:
    from adapters.btf3_hindsight_depth import redact_verdicts
    from adapters.btf3_packet_swap import (
        PAIRING_SEED,
        PACKET_HEADER,
        TASK_HEADER,
        build_swapped,
    )


def build_redacted_swapped(items, *, seed: int = PAIRING_SEED) -> list[dict]:
    records = build_swapped(items, seed=seed)
    for record in records:
        prompt = record["prompt"]
        start = prompt.index(PACKET_HEADER) + len(PACKET_HEADER)
        end = prompt.index(TASK_HEADER, start)
        result = redact_verdicts(prompt[start:end])
        record["prompt"] = prompt[:start] + result.text + prompt[end:]
        record["verdict_sentences_removed"] = result.n_removed
        record["clauses_preserved"] = len(result.preserved_clauses)
    return records

