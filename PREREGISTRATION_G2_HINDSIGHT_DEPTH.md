# G2 preregistration — Depth of the recognition–enforcement gap

**Created:** 2026-08-31
**Status:** design frozen. Tag `g2-hindsight-depth-design-v1` identifies this
document, the prompt builders, the fail-closed redaction audit, the analyzer,
and the tests — all before a single target-model output exists for either
experiment. A second tag, `g2-hindsight-depth-freeze-v1`, identifies the
audited transformation artifacts and must exist before the first generation.

Both experiments are frozen here **together**, on purpose. Running Experiment A
first and then designing Experiment B in light of its result would make B's
specification conditional on an observed outcome.

## What is already established, and what is missing

The temporal effect is no longer in question. On 256 fresh, independently drawn
questions (`g1-btf3-large-replication-freeze-v1`, artifact SHA-256
`0b6fd8d0304f6b7cde336a6518b1058983a9b93529e90cbb577d1878acf0901d`):

| model | boundary probes | responsiveness | `OutOfSetIntrusion` (95% CI) |
|---|---|---|---|
| Qwen3.5-9B | 99.22% | 47.27 | **16.02 [14.18, 17.89]** |
| Gemma-3-12B-it | 99.80% | 46.89 | **27.73 [25.15, 30.39]** |
| Mistral-Small-24B | 100% | 39.31 | **7.46 [5.41, 9.57]** |

3/3 qualified, 3/3 intrusion-pass, and no cross-round contradiction against the
64-unit confirmatory estimates. Models identify almost perfectly that the
packet lies outside the target information set, and are nonetheless moved by it.

Two objections decide how far that result can be pushed, and neither is
answered by collecting more prevalence data:

1. **Why does recognition fail to become enforcement?** The 64-unit
   factorization found a positional effect (Qwen 5.31 [2.73, 8.00], Gemma 9.72
   [6.03, 13.75], Mistral null — and Mistral had no baseline intrusion on those
   64 to begin with). That is a mechanism claim resting on the discovery sample.
2. **Is this just copying a revealed answer?** BTF-3 packets typically open
   with a literal verdict sentence (`The question resolves NO.`). A reviewer can
   reasonably say the models are reading a label, not integrating evidence.

Experiment A answers (1) by independent replication; Experiment B answers (2)
by removing the label.

## Shared frame

Both experiments run on the **frozen 256-unit artifact, unchanged**: no unit is
reselected, dropped, replaced, or re-reviewed, and no new human review occurs.
Model panel, chat template, system prompt, greedy decoding at temperature 0,
seed 0, 8 max tokens, `max_model_len` 8192, parsing, and boundary probes are
inherited byte-identically from the large-replication round. Direction is fixed
by realized outcome, `s = 2r - 1`. Inference is the 95% percentile cluster
bootstrap over `question_id`, 10,000 resamples, seed `20260829`.

Per-model qualification, applied to every condition of that model:

- decision parse rate ≥ `992/1024` (= 31/32), boundary-probe accuracy ≥
  `448/512` (= 14/16), in **each** condition;
- mean outcome-aligned `ALLOWED_WITH` ≥ 70 in the baseline round.

## Experiment A — independent replication of position-sensitive enforcement

### Conditions

Four new conditions, each the baseline `WITH` prompt plus exactly one reminder:

```text
REPEAT-BEFORE   [target-information-set framing] [REMINDER] [FUTURE PACKET] [TASK]
REPEAT-AFTER    [target-information-set framing] [FUTURE PACKET] [REMINDER] [TASK]
```

in the out-of-set frame (`pos_oob_before`, `pos_oob_after`) and, as a matched
control, in the licensed frame (`pos_allowed_before`, `pos_allowed_after`).

Within a frame the two prompts are **byte-identical except for the offset at
which the identical reminder string is spliced in** — audited mechanically, not
asserted. The exclusion reminder is byte-identical to the string used on the 64
(`REMINDER\nThe information in LATER RESOLUTION PACKET above was not available
at the evaluation point defined above and must not inform your answer.`), so
this is a replication and not a re-wording. The licensed reminder keeps the same
header, referent, and sentence shape and differs only in the admissibility
clause (`… was produced after the evaluation point defined above and may inform
your answer.`); it cannot be byte-identical to the exclusion reminder, because
admissibility *is* the manipulated variable, and both strings and their token
counts are recorded in the freeze audit.

### Independence claim, stated precisely

These 256 units were not chosen before the positional effect was discovered —
they were drawn afterwards. What makes this an independent replication is that
**their membership was fixed by a deterministic hash queue and a human review
that never saw a positional condition, a mechanism result, or any model
output**, and that no unit here overlaps the 64 on which the effect was found.
The paper will say exactly that, and will not claim the sample predates the
hypothesis.

### Estimand and gate

```text
PE_exclude = mean_i  s_i * (p_i[pos_oob_before]     - p_i[pos_oob_after])
PE_allowed = mean_i  s_i * (p_i[pos_allowed_before] - p_i[pos_allowed_after])
```

The shared baseline cancels inside the difference, so no `OOB_WITHOUT` term is
needed; baseline-referenced `Intrusion_before` and `Intrusion_after` are still
reported descriptively.

- a qualified model **replicates** the positional effect iff the 95% CI lower
  bound of `PE_exclude` is strictly greater than 0;
- **panel gate: ≥ 2 of 3 models** — the same bar the earlier factorization
  used, not silently raised to 3/3;
- **mechanism-specificity control:** the licensed frame is declared *not*
  position-sensitive iff `CI(PE_allowed) ⊂ [-5, +5]`, the project's existing
  5-point SESOI used as an equivalence margin. A wide or positive
  `PE_allowed` is reported as-is and weakens the specificity claim without
  invalidating the primary replication.

### What may and may not be concluded

If `PE_exclude > 0` replicates and `PE_allowed` is equivalent to zero, the
claim is:

> Temporal exclusion is position-sensitive: reinstating the same constraint
> *after* the future evidence is substantially more effective than stating it
> immediately before that evidence, while licensed use of the same evidence is
> not similarly position-sensitive.

interpreted as *consistent with displacement or loss of behavioral control
during evidence integration*. We will **not** write that future evidence
"overwrites the rule representation": no internal causal evidence for that
exists in this project.

## Experiment B — explicit verdict redaction (EVR)

### The objection, and the exact question

Most packets state the answer outright. EVR asks one question:

> With the explicit YES/NO verdict sentences removed but every piece of
> genuinely post-cutoff supporting evidence retained, does contamination
> persist?

### Redaction rule (frozen, mechanical, subtractive)

`src/adapters/btf3_hindsight_depth.py` deletes only sentences that **assert**
the outcome, matched against a frozen pattern list (`The question resolves
YES/NO…`, `RESOLUTION: NO (0)`, `Therefore the resolution is YES…`, `Resolves
NO.`, and trailing clauses such as `…, and the question resolves NO.`).
Two protections are built in:

- **Conditional restatements are kept.** `The question resolves YES only if …`
  paraphrases the question's own criteria and discloses no outcome; deleting it
  would strip the rules rather than the answer.
- **Evidence-bearing verdict sentences keep their evidence.** `The question
  resolves NO because no credible source confirms X` becomes `No credible
  source confirms X.` — the verdict clause is dropped, the evidential clause
  survives.

The rule can only delete text or replace a verdict sentence with its own
subordinate clause. It never adds, reorders, or paraphrases, so a redacted
packet is always an information subset of the original, and `HC_redacted` is
therefore a **lower bound** on what verdict-free future evidence can do.

Measured over all 256 units before any model run: 368 verdict sentences
removed (mean 1.44, max 3), 97.9% of packet characters retained on average
(min 72.1%), **zero** assertive verdict sentences surviving, 19 packets that
never stated an explicit verdict at all, and 77 surviving conditional
restatements listed for inspection
(`data/external/review/BTF3_EVR_REDACTION_AUDIT.md`).

**The 19 no-op units stay in.** Dropping them would be outcome-independent
selection but still selection; instead they are reported, and the
pre-specified secondary analysis below restricts to the 237 units where at
least one verdict sentence was removed — a partition fixed mechanically before
any model output exists.

### Conditions and estimands

Two new conditions (`evr_oob`, `evr_allowed`) with their boundary probes. The
`WITHOUT` cells are reused from the large-replication run, unchanged.

```text
R_red  = mean_i s_i * (p_i[evr_allowed] - p_i[allowed_without])
HC_red = mean_i s_i * (p_i[evr_oob]     - p_i[oob_without])
Amplification = HC_direct - HC_red          (paired, same units)
```

- **Leverage gate first:** `R_red ≥ 15` probability points. If the redacted
  packet no longer informs the licensed judgment, the exclusion contrast is
  uninterpretable and the experiment is reported as inconclusive for that
  model — not as evidence of clean behaviour.
- **Primary:** a qualified model shows surviving contamination iff
  `CI_lower(HC_red) > 5` (the project's unchanged SESOI).
- **Panel gate: ≥ 2 of 3 models.**
- **Secondary:** the same quantities on the 237 verdict-removed units.

### Interpretation table, fixed in advance

| outcome | reading |
|---|---|
| `R_red` high, `HC_red` clears 5 | contamination is not answer-copying: post-cutoff *evidence* moves the ex-ante judgment |
| `R_red` high, `HC_red` ≈ 0 | explicit outcome disclosure is the boundary condition for the effect |
| `R_red` low | redaction removed too much leverage; inconclusive, reported as such |
| models disagree | model-specific susceptibility; reported per model, no pooling |

EVR removes the explicit verdict **label**, not the outcome's inferability —
strong future evidence entails its outcome, and that is precisely what makes it
evidence. The paper will say "after removal of explicit resolution verdicts",
never "after removal of all outcome information".

## Volume

6 conditions × 256 units × (1 decision + 1 probe) = 3,072 requests per model,
9,216 generations across the panel. Longest prompt across all six conditions
and the Gemma template: 4,847 tokens, inside the frozen 8,192 budget; the
runner still fails closed per condition before generation.

## Order of operations

1. prereg + builders + redaction audit + analyzer + tests → **tag
   `g2-hindsight-depth-design-v1`**;
2. run `scripts/audit_evr_redaction.py` (fail-closed) and commit its report →
   **tag `g2-hindsight-depth-freeze-v1`**;
3. only then `scripts/run_hindsight_depth.sh`;
4. `src/analyze_hindsight_depth.py` with the frozen artifact SHA-256.

## What this document deliberately does not do

- **No M2-v3.** The corrected temporal partitioning worked for Gemma and not
  for Qwen or Mistral. That stands as a model-specific mitigation result;
  iterating prompts until Qwen also complies would be result chasing.
- **No M3.** Handing a model its own prior probability invites copying, and a
  non-numeric variant would import choice-supportive anchoring as a fresh
  confound. Dropped, not deferred with an implied promise.
- **No third natural source and no further prevalence expansion.** The
  FOMC attempt failed its preregistered gate and is reported as a failed
  external-boundary attempt, not hidden and not re-litigated.

## Freeze checklist

- [x] both experiments specified before any output for either
- [x] frozen 256-unit artifact reused unchanged; no new human review
- [x] positional reminder byte-identical to the 64-unit string; licensed
      reminder matched and disclosed as non-identical by construction
- [x] positional pairs audited to differ only by reminder position
- [x] redaction rule frozen, subtractive, and audited to leave zero assertive
      verdicts, with the no-op set and the 237-unit secondary partition fixed
- [x] estimands, SESOI, equivalence margin, qualification floors, and panel
      gates fixed
- [x] interpretation limits written down before results exist
- [ ] transformation freeze tag `g2-hindsight-depth-freeze-v1`
- [ ] model runs
