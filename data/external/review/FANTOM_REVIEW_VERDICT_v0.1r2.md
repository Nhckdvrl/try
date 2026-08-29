# FANToM perspective v0.1r2 — replacement-only review verdict

**Review date:** 2026-08-29

**Model outputs inspected:** none.

The six v0.1 source units already accepted by the human reviewer were retained byte-equivalently. This ledger reviews only the two deterministic replacements selected after excluding parts `244-0` and `252-0`.

## Decisions

| part_id | set_id | target | decision | reason |
|---|---|---|---|---|
| `14-0` | `14-0-2` | Jamie | **REJECT** | The source `wrong_answer`, used as the truth-belief candidate, says there is no information about Jamie's belief. The exact packet instead supplies Aubree's student-activism experience. Explicitly briefing Jamie with that packet would not make the no-information candidate correct, so the allowed causal arm is semantically invalid. |
| `216-0` | `216-0-1` | Camryn | **ACCEPT** | Camryn joins only after Aurora and Skylar's detailed discussion of adjustment, training, time, and patience. After joining, Camryn hears only that they were talking about pets and then discusses pet loss; the earlier concerns are not repeated. The unbriefed ignorance candidate is defensible, and explicit briefing with the exact packet makes the truth-belief candidate correct. |

## Consequence

- Preserve v0.1r2 as an immutable failed replacement artifact.
- Retain Camryn in the next regeneration.
- Exclude Jamie's `part_id` in addition to the two v0.1 rejects.
- Draw one further deterministic replacement without model outputs.
- Review only that final new source unit; do not reopen the seven accepted units.
