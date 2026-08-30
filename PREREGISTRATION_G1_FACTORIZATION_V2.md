# G1 factorization v2 — Testing Instruction Displacement and Temporal Partitioning

**Created:** 2026-08-30
**Status:** preregistration draft. No tooling, no sample, no model run yet.
Written after `PREREGISTRATION_G1_FACTORIZATION.md`'s v1 result: M1 (rule
repetition) validated as a partial mechanism in 2/3 models, but M2 and M3
were inconclusive due to disclosed, post-hoc-discovered implementation
defects (M2: missing target-information-set framing, boundary-probe
accuracy collapsed to 0.0–0.5; M3: task instruction invited verbatim
copying of the stated prior value). This document does not simply
"bugfix and re-run" those two conditions. It reprioritizes around the
actual scientific gap the v1 result leaves open.

## Why this document exists, and what it deliberately does not attempt

M1's v1 result (Qwen delta 3.75 [1.02, 6.61], Gemma delta 13.97 [9.56,
18.67], Mistral ≈0 as expected) is real, but a reviewer has a fair
objection: repeating the exclusion instruction a second time is
confounded with simply *emphasizing an instruction more*. That alone
does not establish "instruction displacement/overwriting by future
evidence" — it is equally consistent with "any repeated instruction,
regardless of where it sits relative to the evidence, works a little
better." The v1 write-up already called this out as Threat 4
(manipulation confound). This document exists to resolve exactly that
confound before doing anything else, via a **positional control** — not
by adding more mitigation candidates.

Separately, M2's v1 failure was a clean implementation bug (a missing
framing paragraph), not a finding about temporal partitioning itself. It
is corrected here with a **minimal, surgical fix** — inserting two label
lines into the already-validated baseline prompt, changing nothing else
— rather than a prompt redesign.

**M3 is deferred, not attempted in this document.** Per the user's own
diagnosis: M3's v1 failure was not a wording bug but a conceptual one —
handing the model a literal numeric target and asking it to "restate"
that number invites copying regardless of instruction wording ("restate"
vs. "recompute" does not fix this). A genuine test of a stable epistemic
state requires a non-numeric externalization (e.g. a structured
qualitative evidence summary formed before the future packet appears,
with no probability value to copy) that has not yet been designed. That
redesign is out of scope for this document.

## Priority 1 (primary): M1 positional control

**Question:** is M1's effect really caused by *temporal displacement* of
the exclusion rule relative to the inadmissible evidence, or would any
second repetition of the instruction help regardless of where it sits?

**Design:** the exact same second reminder text used in v1's M1
(`REPEAT-AFTER`, unchanged, its existing results are reused — see
below), byte-identical in wording and length, placed at a different
position:

- **`REPEAT-AFTER`** (= v1's `M1`, unchanged): reminder inserted between
  the `LATER RESOLUTION PACKET` block and `TASK` — i.e. *after* the model
  has been shown the inadmissible evidence.
- **`REPEAT-BEFORE`** (new): the identical reminder text inserted between
  the `TARGET INFORMATION SET` framing and the `LATER RESOLUTION PACKET`
  block — i.e. *before* the model is shown the inadmissible evidence.

Nothing else differs between the two conditions: same reminder string,
same token count, same number of repetitions (two total: the original
instruction plus one repeat), same source content, same target question.
The only manipulated variable is where the repeated reminder sits
relative to the future packet.

**`REPEAT-AFTER` reuses v1's already-collected M1 results
(`results/raw/isr_{model}_factorization_m1.jsonl`, commit `3f79542`) —
it is not re-run.** `build_m1` (the function that produced it) is
unchanged; re-running it would only add sampling noise to an already-frozen
result, not new information. Only `REPEAT-BEFORE` is new data collection.

**Primary outcome:**

```text
Intrusion_before = s * (p_oob_with_repeat_before - p_oob_without)
Intrusion_after  = s * (p_oob_with_repeat_after  - p_oob_without)   [reused from v1]
PositionalEffect = Intrusion_before - Intrusion_after
```

(paired per unit, same `p_oob_without` baseline as v1, same
`outcome_alignment_sign`.) A positive `PositionalEffect` means
`REPEAT-AFTER` leaves less intrusion than `REPEAT-BEFORE` — i.e.
position specifically matters, supporting the overwriting/displacement
account. A `PositionalEffect` indistinguishable from zero means both
positions help about equally, which does **not** support a
position-specific overwriting account — the effect would be better
described as generic instruction emphasis.

**Inference:** 95% percentile cluster bootstrap on `PositionalEffect`,
clustered by `independent_unit_id`, 10,000 resamples, seed `20260829`
(unchanged discipline from v1). `REPEAT-BEFORE`'s own boundary-probe
accuracy (≥14/16 floor) and `ALLOWED_WITH` alignment guard (carried from
baseline, ≥70) are checked exactly as v1's manipulations were, to rule
out the position manipulation degrading general comprehension.

## Priority 2: M2, minimally corrected

**Root cause of v1's failure (confirmed, not re-litigated):**
`build_m2`'s prompt never included the baseline's own
`TARGET INFORMATION SET` framing paragraph (the sentence defining what
"the evaluation point" refers to), and the boundary-probe question then
asked about "the evaluation point defined above" with no antecedent —
this is why Gemma answered "YES" to all 64 probes and accuracy collapsed
to 0.0–0.5 across models.

**Fix, deliberately minimal — insertion only, no reconstruction:** start
from the exact baseline `OOB_WITH` prompt (`item.oob_variant
["with_information_prompt"]`, the same byte-identical text already
validated in the confirmatory run and in M1/M3), and insert exactly two
new label lines, changing nothing else:

- `AVAILABLE AT TARGET TIME` immediately before the existing
  `BACKGROUND AVAILABLE AS OF {date}` header;
- `LEARNED AFTER TARGET TIME` immediately before the existing
  `LATER RESOLUTION PACKET` header.

The `TARGET INFORMATION SET` framing paragraph, the `LATER RESOLUTION
PACKET` header itself (kept, not renamed — so it still has a valid
antecedent), and the final `TASK` question are all byte-identical to
baseline. The boundary probe reuses `run_information_set.py`'s existing
generic `boundary_probe()` function unmodified (no custom M2 boundary
question this time) — it still asks about `LATER RESOLUTION PACKET`,
which is still literally present in the prompt. This directly tests
whether adding explicit temporal-availability labels around otherwise
*unchanged* baseline content reduces intrusion, without reopening any of
v1's implementation risk.

**Primary outcome and inference:** identical structure to v1's
`Delta_M`/bootstrap/validity-guard discipline
(`PREREGISTRATION_G1_FACTORIZATION.md`), applied to this corrected
`M2-v2` condition. New data collection (all 64 units × 3 models); the
v1 M2 run is not reused (it is invalid, not merely superseded).

## Stop/go rule

Both results are reported regardless of outcome; the four possible
combinations are each a clean, reportable finding — no combination is
treated as "the experiment failed to produce anything usable":

1. **`PositionalEffect` CI lower bound > 0 in ≥2/3 models AND `M2-v2`
   validated (≥2/3 models)**: the depth story reaches the target framing
   — "models recognize the boundary but fail to enforce it; enforcement
   is position-sensitive (refreshing the rule after exposure to
   inadmissible evidence restores control that repeating it beforehand
   does not), and explicit temporal partitioning independently reduces
   contamination while preserving legitimate evidence use." This is the
   strong outcome.
2. **`PositionalEffect` not distinguishable from zero, but `M2-v2`
   validated**: M1 is downgraded from an "instruction-overwriting
   mechanism" claim to a "simple reminder mitigation" claim (real, but
   not position-specific); `M2-v2`'s partitioning result stands
   independently as the paper's primary mitigation finding.
3. **`PositionalEffect` CI lower bound > 0, but `M2-v2` not validated**:
   the positional/overwriting account is strengthened as the paper's
   mechanism story; partitioning is reported as not (yet) an effective
   mitigation, without further redesign in this document.
4. **Neither**: M1's v1 result (2/3 models, generic repetition reduces
   intrusion) still stands on its own as a real, already-validated
   finding from `PREREGISTRATION_G1_FACTORIZATION.md` — it is not erased
   by this document — but this document's own contribution (a
   mechanistic, position-specific story, or an independent
   partitioning-based mitigation) would not be established, and the
   project should not immediately design a v3 without a new rationale.

No manipulation in this document is redesigned or re-parameterized after
seeing its own model output, matching v1's and every prior source's
discipline.

## Process fix (explicit, binding)

v1 disclosed a real process gap: prereg, tooling, and the first model run
all landed in one working session with no tag checkpoint between
freezing the design and running the first model. **This document is
frozen, tagged, and the tag is confirmed to exist and to point at a
commit containing this document and the (untested-against-real-output)
tooling below, before any `REPEAT-BEFORE` or `M2-v2` model output is
generated.** Tag: `g1-factorization-v2`.

## Freeze checklist

- [x] scope reprioritized: positional control (primary) + minimally
      corrected M2 (secondary); M3 explicitly deferred
- [x] `REPEAT-BEFORE`/`REPEAT-AFTER` design, with `REPEAT-AFTER` data
      reuse from v1 disclosed and justified
- [x] `M2-v2` minimal-fix design (insertion only, byte-identical
      framing/task/boundary-probe question)
- [x] primary outcomes (`PositionalEffect`, `Delta_M2v2`) and inference
      method (unchanged from v1: unit-clustered bootstrap, 10,000
      resamples, seed 20260829)
- [x] stop/go rule covering all four outcome combinations
- [x] manipulation adapter tooling —
      `build_m1_repeat_before`/`build_m2_v2` in
      `src/adapters/btf3_factorization.py`, `src/run_factorization.py`
      extended with the `m1_before`/`m2v2` conditions,
      `src/analyze_positional_control.py`
- [x] tests — `tests/test_btf3_factorization.py`,
      `tests/test_analyze_positional_control.py`
- [x] commit
- [x] immutable Git tag (`g1-factorization-v2`), confirmed to exist
      (local and remote `git ls-remote --tags`) and to point at the
      commit containing this document and the tooling above, before any
      new model output
