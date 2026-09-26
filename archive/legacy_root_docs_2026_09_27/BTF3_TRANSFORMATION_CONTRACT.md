# BTF-3 temporal transformation contract — candidate v0.2

**Status:** v0.2r2 source and transformation review passed. Pilot-ready after the repository-wide G1 preregistration is frozen; this document alone does not authorize a run.

## Audit correction from v0.1

Human review of the eight-unit v0.1 packet found two blockers before any model output was produced:

1. one source `resolution_explanation` contains a non-material but real factual error (the 2026 Travelers Championship is described as concluding June 28; official PGA TOUR reporting shows a weather-delayed playoff on Monday June 29), so that source unit is rejected rather than silently repaired;
2. the v0.1 adapter described `date_cutoff_end` as the **close of that named UTC day**. BTF-3 documents the field as the source encoding for the end of the UTC day containing `present_date`; in rows where `present_date` is May 12 and `date_cutoff_end` is May 13, the intended information window is the May 12 UTC day, not all of May 13. The old wording could therefore grant one extra day.

The committed v0.1 JSONL is retained unchanged as an audit artifact. It is **not model-ready**. The corrected adapter produced v0.2 with a replacement NO unit, but human review found a second exact-packet error: the Argentine Senate packet says a congressional recess running through late July "precludes" a late-June committee report. A recess beginning in July cannot preclude committee action in late June. The outcome itself appears correct, but the source-native packet is rejected under the same no-silent-repair rule. The v0.2 artifact is also retained unchanged.

The next artifact is named v0.2r2: it uses the unchanged v0.2 transformation semantics, excludes both rejected source units, and draws another deterministic NO replacement while retaining 4 YES / 4 NO balance. Only that new source unit and the regenerated transformation integrity require new human review; the seven previously accepted source units retain their source-validity decisions.

## Source task

BTF-3 supplies a binary forecasting question, resolution criteria, background available as of `present_date`, a source-encoded cutoff boundary, expected resolution date, resolved outcome, and a sourced but machine-generated resolution explanation.

The source card says the information window ends at the end of the UTC day containing `present_date`. In the current source revision, `date_cutoff_end` is represented as the following midnight-style date boundary. The adapter must therefore describe the target window by the **UTC calendar day containing `present_date`**, and may show `date_cutoff_end` only as the source boundary encoding. It must never say that all of the calendar day named by `date_cutoff_end` is available.

The source itself warns that resolution explanations were only partially human spot-checked. Reviewer approval is therefore required per item.

## Causal design

For each `question_id`, construct a 2 × 2 design while holding the question, criteria, background, answer scale, and outcome packet text fixed:

| Target information set | No resolution packet | Exact resolution packet supplied |
|---|---|---|
| Ex ante: through the end of the UTC day containing source `present_date` | `OOB_WITHOUT` | `OOB_WITH` |
| Retrospective: all supplied information | `ALLOWED_WITHOUT` | `ALLOWED_WITH` |

Every condition asks for a probability from 0 to 100 that the binary question resolves YES. The same exact `resolution_explanation` appears in both `*_WITH` conditions. Only the target information set changes.

For resolved outcome `r ∈ {0,1}`, define `s = 2r - 1`:

```text
Responsiveness      = s * (p_allowed_with - p_allowed_without)
OutOfSetIntrusion   = s * (p_oob_with - p_oob_without)
BoundarySelectivity = Responsiveness - OutOfSetIntrusion
```

This difference-in-differences isolates the causal contribution of the same future packet under licensed versus out-of-set task definitions. Raw four-cell probabilities and Brier scores must also be reported.

## What remains source-native

- question, resolution criteria, and background are copied verbatim;
- `present_date`, `date_cutoff_end`, and expected resolution date retain source values;
- the outcome packet is the exact source `resolution_explanation`;
- output remains a binary forecast probability.

The adapter adds only section labels, target-time framing, and a parseable answer instruction. It does not rewrite cases into `BACKGROUND / RULING / EVIDENCE` or invent positive/negative counterfactual outcomes.

## Known threats

1. **Task-time manipulation:** retrospective probability is not identical to a live forecast, although the question and output scale are fixed. This is a deliberate eligibility manipulation and must be described honestly.
2. **Direct answer disclosure:** most resolution explanations state YES/NO. This gives strong allowed leverage but may make the OOB condition unusually stark.
3. **Parametric contamination:** a model may already know the 2026 outcome. The within-target packet contrast helps but does not eliminate all contamination.
4. **Resolution quality:** explanations are machine-generated and partially checked; every pilot item needs human verification against its cited sources. Do not hand-edit a bad source packet into a good one while continuing to call it source-native; reject and replace the unit unless a separately versioned transformation explicitly permits corrections.
5. **Instruction compliance:** the ex-ante wording explicitly defines the cutoff. A separate boundary-knowledge probe is still required.
6. **One-sided natural outcome:** each question has only its realized outcome. Pooling direction-aligns realized YES/NO questions; it does not create an item-level counterfactual world.
7. **Cutoff representation:** `date_cutoff_end` is a boundary encoding, not a license to include the following UTC calendar day. Tests must lock this semantics.

## Automatic eligibility checks

- binary resolution is exactly 0 or 1;
- `present_date < expected_resolution_date`;
- source cutoff boundary follows the source-revision invariant for the UTC day containing `present_date`;
- question ID is unique;
- question, criteria, background, and resolution explanation are non-empty;
- generated JSONL passes `information_set_schema.py`;
- sample selection is deterministic and balanced by realized resolution;
- excluded/rejected question IDs cannot re-enter a regenerated review set accidentally.

## Human rejection rules

Reject an item if any of the following holds:

- source resolution is unsupported or materially contradicted by its citations;
- the exact packet contains a factual error that we would otherwise have to silently rewrite before presenting it to the model;
- question was already resolved by `present_date`;
- background contains material post-cutoff information;
- resolution criteria or outcome are genuinely ambiguous;
- the packet changes the interpretation of the question instead of informing it;
- the prompt pair differs anywhere beyond the registered packet or target-set framing;
- the item requires unsafe, private, or normatively inappropriate content.

Reviewer decisions must be made without model outputs and recorded as `accept / reject / unsure` plus a reason for reject/unsure. A transformation-level bug blocks the whole artifact even when individual source units are accepted.

## v0.1 human-review outcome

- 7 source units: ACCEPT
- 1 source unit: REJECT (`b6fc94e7-a0b9-56b6-87a1-ba94f29781e9`)
- v0.1 transformation artifact: BLOCKED / REGENERATION REQUIRED
- model runs authorized: **none**

See `data/external/review/BTF3_REVIEW_VERDICT_v0.1.md` and the completed review packet.

## v0.2 replacement-review outcome

- 7 previously accepted source units: retained
- 1 replacement source unit: REJECT (`34d3588a-ffb0-5290-b964-bceb68be18f1`)
- reason: exact resolution packet contains a temporally impossible supporting claim
- v0.2 transformation semantics: pass automatic checks; artifact blocked by source packet
- model runs authorized: **none**

See `data/external/review/BTF3_REVIEW_VERDICT_v0.2.md`.

## v0.2r2 final review outcome

- 7 previously accepted source units: retained byte-equivalently
- BRICS replacement (`b92bacb5-8086-5dd2-a64f-9ec00c427248`): ACCEPT
- regenerated transformation integrity: PASS
- final pilot artifact: 8 accepted units, balanced 4 NO / 4 YES
- model outputs inspected during selection/review: none

The reviewer independently verified that the BRICS meeting began after the source cutoff, that the official outcome was a chair's statement rather than a joint statement/communiqué/declaration, and that contemporaneous pre-cutoff reporting already used the 11-member wording. The latter had some contemporaneous terminology variation around Saudi membership but does not affect the question or outcome.

This closes the BTF-3-specific human gate. Model execution remains blocked only by the cross-source G1 freeze requirements in `PREREGISTRATION_G1.md`.

## Confirmatory phase: 64-unit candidate-queue protocol

The exploratory pilot (`btf3_temporal_pilot_v0.2r2.jsonl`, 8 units) passed the
G1 stop/go rule in `g1-pilot-freeze-v1.2`: 3/3 models qualified, 2/3 showed
`OutOfSetIntrusion` clearing the 5-point SESOI. This authorizes a
confirmatory expansion of BTF-3 specifically (not a repeat of the pilot
count): **64 fresh independent `question_id`s, 32 realized-YES / 32
realized-NO, drawn from source units never shown to any target model.**

The pilot's own review already caught two source units with a correct
outcome but a factually/temporally broken exact resolution packet
(`b6fc94e7-...`, `34d3588a-...`). Because BTF-3's `resolution_explanation`
is machine-generated and only partially spot-checked, that packet-factual
gate cannot be relaxed at 64 units just because it is 8x the pilot volume.
What changes is the review's *shape*, not its presence:

- **Candidate queue, not one-shot sample.** `scripts/build_btf3_confirmatory_candidates.py`
  draws a deterministic per-resolution order (`deterministic_candidate_queue`
  in `src/adapters/btf3_temporal.py`) of `--pool-size` candidates per bucket
  (default 64, i.e. double the 32 quota, since the pilot rejected roughly 1
  in 4 candidate units), permanently excluding: the two historical rejected
  IDs above, and all 8 pilot IDs from `btf3_temporal_pilot_v0.2r2.jsonl`
  (they already had target-model output observed against them in
  `g1-pilot-freeze-v1.2` and can never re-enter primary confirmatory
  selection). This queue order is written to a `*_candidates.json` manifest
  before any human review begins and never changes afterward.
- **Four mechanical gates per candidate**, all required to ACCEPT: pre-cutoff
  intact, realized outcome valid, exact packet factually valid, criteria
  unambiguous. A REJECT or UNSURE requires exactly one line of reason and
  permanently consumes that queue slot — it is never re-reviewed, and the
  unit is never hand-repaired into an acceptable one.
- **Quota, not sample size.** `scripts/freeze_btf3_confirmatory.py` walks each
  bucket's queue in the frozen order and takes the **first 32 ACCEPTs**. The
  final 64-item artifact is whichever 64 question_ids happen to survive
  review in queue order — not the first 64 drawn. If a bucket runs out of
  ACCEPTs before reaching 32, the fix is to re-run the candidate-queue
  builder with a larger `--pool-size` and review only the newly appended
  tail; already-reviewed candidates are never reconsidered or reordered.
- **No resampling, no reordering, no post-hoc replacement** once review of a
  candidate starts, mirroring the pilot's replacement-round discipline
  (`v0.1` → `v0.2` → `v0.2r2`) but without per-unit narrative memos.
- Model panel is unchanged: the same three frozen checkpoints
  (`Qwen/Qwen3.5-9B`, `google/gemma-3-12b-it`,
  `mistralai/Mistral-Small-24B-Instruct-2501`) — no post-pilot substitution.
- Primary confirmatory inference uses only the 64 frozen units. The original
  8 pilot units remain a pilot-replication / descriptive appendix and are
  never pooled into primary confirmatory estimates.
- All selection and review happens strictly before any confirmatory-run
  model output, exactly as for the pilot.

`scripts/audit_btf3_review.py` (unchanged) is the fail-closed check for the
resulting artifact: `--expected-count 64 --expected-per-resolution 32`, plus
`--exclude-question-id` for the 2 historical rejects and all 8 pilot IDs.
