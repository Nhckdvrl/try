# BTF-3 exclusion-reason transformation audit

Artifact: `data/external/review/btf3_temporal_large_replication_v1.jsonl`  
SHA-256: `0b6fd8d0304f6b7cde336a6518b1058983a9b93529e90cbb577d1878acf0901d`  
Units: 256 × 2 cells

## Result

**PASS.** 512/512 temporal-arm prompts are byte-identical to the frozen artifact; every other arm differs from it at exactly one contiguous span inside `TARGET INFORMATION SET`, before `LATER RESOLUTION PACKET`; nothing after the packet header changes in any arm.

## Frozen sentence

```text
Any text explicitly labeled LATER RESOLUTION PACKET was produced after this information set and is not part of the evidence that defines the requested ex-ante forecast.
```

## Arms

| arm | sentence | Δ chars vs temporal (mean) | Δ tokens (mean) |
|---|---|---:|---:|
| `temporal` | Any text explicitly labeled LATER RESOLUTION PACKET was produced after this information set and is not part of the evidence that defines the requested ex-ante forecast. | 0 | 0 |
| `bare` | Any text explicitly labeled LATER RESOLUTION PACKET is not part of the evidence that defines the requested ex-ante forecast. | -44 | -7 |
| `unreliable` | Any text explicitly labeled LATER RESOLUTION PACKET was assembled by an unverified automated process, may contain fabricated claims, and is not part of the evidence that defines the requested ex-ante forecast. | 41 | 8 |
| `procedural` | Any text explicitly labeled LATER RESOLUTION PACKET was obtained through a channel this forecasting protocol does not permit for this question; its contents are accurate, but it is not part of the evidence that defines the requested ex-ante forecast. | 82 | 15 |

## Position channel

`packet_to_task_token_span_invariant`: **True**. The edited sentence precedes the packet, so the token distance between the packet header and `TASK` is identical in all four arms. The positional channel that G2 Experiment A found to matter is closed by construction, not by argument.

## Disclosure

The `unreliable` arm asserts that the packet may contain fabricated claims. That is false of our materials and is a deliberate counterfactual framing manipulation. The `procedural` arm affirms the packet's accuracy, which the `temporal` arm does not; it is therefore a conservative test of a non-temporal licensing reason. Both disclosures are repeated wherever the arms are reported.
