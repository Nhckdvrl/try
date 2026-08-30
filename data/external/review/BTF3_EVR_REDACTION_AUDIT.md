# BTF-3 explicit-verdict redaction — pre-run audit

- artifact: `data/external/review/btf3_temporal_large_replication_v1.jsonl` (SHA-256 `0b6fd8d0304f6b7cde336a6518b1058983a9b93529e90cbb577d1878acf0901d`)
- units: 256
- assertive verdict sentences surviving redaction: **0** (hard gate: must be 0)
- verdict sentences removed: 368 (mean 1.44, max 3)
- packets that stated no explicit verdict at all: **19** (kept in the sample; reported, never dropped)
- characters retained: mean 0.979, min 0.721
- clause-preserved rewrites ("resolves NO because X" → "X."): 38 units
- surviving conditional criteria restatements: 77 sentences

Conditional restatements are kept deliberately: they paraphrase the
question's own resolution rules and disclose no outcome. Removing them
would strip the criteria rather than the answer.

## Surviving conditional restatements (first 10, for inspection)

- The criteria also stipulate resolving NO if no credible reporting confirms SAF control.
- The resolution criteria explicitly state: "If no such bill appears on the tracker with a Commons First Reading date on or before 30 June 2026, this question resolves No."
- The question resolves YES only if, between April 30, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC), the IDF/Israeli government officially announced a withdrawal of ground forces from a named area previously within the "orange line"/"Yellow Line" restricted zone, OR Reuters/AP/AFP reported a physical IDF vacation of an area resulting in a net reduction of the restricted zone boundary.
- It resolves NO if any candidate exceeded 50% and won outright in the first round.
- Because Strike Tracker, RTBF, VRT NWS and The Brussels Times collectively report only strike NOTICES for police (with the Liège one suspended) and no actual police cessation of work during May 13–June 30, 2026, the criteria's default applies: the question resolves NO.
- Antecedent/precondition check: The question resolves NO if the June 2026 Monetary Policy Report is not published by July 1, 2026, and otherwise on whether the 2026 annual-average CPIF forecast strictly exceeds 1.5%.
- The resolution criteria state that if the evidence only shows "deep concern" or calls the attacker "unclear," the question resolves NO.
- The question resolves YES only if, between May 12, 2026 and 11:59 PM AEST July 1, 2026, the Minister for Home Affairs, the Minister for Immigration, or the Department of Home Affairs completed a visa cancellation/refusal whose decision EXPLICITLY cited (a) the Combatting Antisemitism, Hate and Extremism (Criminal and Migration Laws) Act 2026 by name, or (b) the specific new amendments to Sections 500A/501 of the Migration Act introduced by that Act.
- Because no publicly confirmed visa cancellation or refusal explicitly citing the Act or its s.500A/s.501 amendments was identified within May 12 – July 1, 2026, and the resolution criteria specify that absence of such an identified action resolves NO.
- Because the resolution criteria state the question resolves NO "if the Court issues a majority opinion holding that federal law does not prohibit states from counting mail-in ballots received after Election Day," and that is exactly what happened, the correct resolution is NO (0).

## Hard checks passed

| check | result |
|---|---|
| packets byte-match the pinned source | PASS |
| zero assertive verdict sentences survive | PASS |
| redaction is subtractive (no added or paraphrased content) | PASS |
| original packet absent wherever a verdict was removed | PASS |
| redacted packet present in every EVR prompt | PASS |
| positional pairs differ only by reminder position | PASS |
| reminder inserted exactly once per positional prompt | PASS |

No target-model output was consulted or produced by this audit.
