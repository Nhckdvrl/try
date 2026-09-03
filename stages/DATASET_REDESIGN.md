# Current data design: BTF-3 temporal hindsight reconstruction

This file replaces the older multi-source *Information-Set Reasoning* redesign
note. The current paper no longer targets a cross-boundary benchmark. Its
positive natural-task evidence is temporal and source-native, with BTF-3 as the
primary dataset.

## 1. Scientific object

The task is to reconstruct an ex-ante probability judgment from a historical
information state **after later evidence is available in context**.

The key distinction is between:

```text
information available to the model now
vs.
information licensed to affect the historical judgment
```

The desired behavior has two directions:

```text
Responsiveness:        use the future packet when it is licensed
Out-of-set invariance: do not use the same packet when reasoning ex ante
```

The failure quantity is `OutOfSetIntrusion`.

## 2. Source-native BTF-3 transformation

For every eligible BTF-3 binary forecasting question, retain verbatim:

- question;
- resolution criteria;
- historical background;
- source time fields;
- realized binary outcome;
- exact source-native resolution explanation.

The adapter adds only section labels, target-time framing, and a parseable
0–100 probability instruction.

The same future packet is used in a 2×2 design:

| target information set | packet absent | packet present |
|---|---|---|
| historical / ex ante | `OOB_WITHOUT` | `OOB_WITH` |
| retrospective / all supplied information licensed | `ALLOWED_WITHOUT` | `ALLOWED_WITH` |

Only the packet presence and target admissibility framing vary. The question and
historical context stay fixed.

For realized outcome `r`, with `s = 2r - 1`:

```text
Responsiveness      = s * (p_allowed_with - p_allowed_without)
OutOfSetIntrusion   = s * (p_oob_with - p_oob_without)
BoundarySelectivity = Responsiveness - OutOfSetIntrusion
```

Raw probability-point contrasts are primary.

## 3. Independent sampling rounds

The paper keeps discovery and replication rounds separate.

### Discovery pilot

- 8 accepted BTF-3 units;
- balanced 4 YES / 4 NO;
- used only as discovery evidence.

### Confirmatory round

- 64 fresh independent `question_id`s;
- 32 YES / 32 NO;
- none reused from the pilot;
- primary inference performed only on those 64 units.

### Large replication

- 256 additional fresh independent `question_id`s;
- 128 YES / 128 NO;
- none reused from the pilot, the 64-item confirmatory sample, or even the prior
  confirmatory candidate queue;
- preregistered replication gate evaluated on the 256 units alone.

The 64 + 256 pooled view is descriptive only and never rescues a failed
large-replication gate.

## 4. Candidate selection and review

Selection is deterministic and prospective.

- outcome buckets are ordered by a frozen deterministic queue;
- review proceeds in queue order;
- the first quota-satisfying ACCEPTs are frozen;
- rejected / unsure items are never hand-repaired back into the sample;
- previously used or permanently rejected IDs are excluded mechanically;
- target-model outputs are not used for selection or review.

Human review uses four source-level gates:

1. **pre-cutoff intact** — the question was unresolved at the target time and
   historical background contains no material post-cutoff information;
2. **realized outcome valid** — the source resolution is supported;
3. **exact packet factually valid** — the source-native resolution packet does
   not contain a material factual error that would require silent repair;
4. **criteria unambiguous** — the outcome follows the source's own resolution
   criteria without a genuine alternative interpretation.

Full details remain in [`BTF3_TRANSFORMATION_CONTRACT.md`](../BTF3_TRANSFORMATION_CONTRACT.md)
and the large-replication preregistration.

## 5. Boundary probes and qualification

Every unit also receives boundary probes that ask whether the supplied future
packet belongs to the target information set.

This is essential to the paper's main dissociation:

```text
boundary recognition ≈ ceiling
while
causal influence of out-of-set evidence > 0
```

The large-replication thresholds, parsers, model revisions, decoding, bootstrap
rules, and 5-point SESOI were frozen before model output under
[`PREREGISTRATION_BTF3_LARGE_REPLICATION.md`](../preregistrations/PREREGISTRATION_BTF3_LARGE_REPLICATION.md).

## 6. Data-quality audit

The 256-unit large-replication artifact passed fail-closed checks for:

- exact count and 128/128 outcome balance;
- unique IDs;
- zero overlap with prior rounds and excluded queues;
- schema validity;
- transformation integrity;
- packet placement;
- full prompt token census under all three frozen chat templates.

Because the original review did not use external web lookup, a later protocol
froze a 64-item hash-selected audit sample **before citations were opened**.
That audit returned 63 PASS, 1 MATERIAL_ERROR, and 0 UNVERIFIABLE. The one error
is a question/criteria date-window contradiction; excluding it has negligible
impact on all primary model estimates.

This audit is a robustness check, not proof that every packet in the 256-unit
artifact is factually perfect.

## 7. Depth transformations on the frozen 256 units

Two later analyses reuse the same 256-item membership rather than collecting a
new sample.

### Explicit-verdict redaction

A subtractive transformation removes explicit YES/NO resolution-verdict
sentences while retaining the remaining post-cutoff evidence. A fail-closed
audit verifies that assertive verdict sentences are removed and records no-op
cases separately.

Purpose:

> test whether hindsight contamination reduces to copying an explicit outcome
> label.

It does not: contamination survives the redaction manipulation.

### Qwen3.5 size analysis

The same 256 questions and unchanged baseline prompts are evaluated on available
dense Qwen3.5 checkpoints (4B, 9B, 27B). This is a within-family size analysis,
not a new dataset and not a scaling-law study.

## 8. External-source attempts are not part of the positive dataset

Several source directions were explored while the project was broader:

- FANToM perspective tasks failed qualification;
- ForecastBench was rejected at source-audit time for the intended
  source-native future-packet design;
- SCOTUS failed mechanical context-length calibration;
- FOMC passed source engineering but failed its preregistered 24-unit
  qualification gate.

These attempts are retained in the repository for auditability. They do **not**
contribute positive examples to the current paper and should not be presented as
part of a multi-source benchmark.

## 9. Current dataset claim

The paper may say:

> The headline effect is confirmed on 64 prospectively selected BTF-3 questions
> and independently replicated on a further 256 unseen questions, balanced
> across realized outcomes, using an unchanged source-native causal design.

It may **not** say:

- the effect has been replicated across natural sources;
- BTF-3 establishes a general temporal reasoning benchmark;
- all resolution packets are externally certified as correct;
- the redacted packets contain no outcome-entailing evidence.