# G1 factorization v1 — M1/M2/M3 results

**Base artifact:** `btf3_temporal_confirmatory_v1.jsonl` (unchanged, no new
sampling). Baseline reference: the already-collected confirmatory run
(commit `8c7ab5f`). All 9 manipulation runs (3 manipulations × 3 models)
executed cleanly: 128 rows each, parse failures negligible (1 boundary
probe failure for Gemma/M1, 1 decision failure each for Gemma/M2 and
Mistral/M2, out of 64 units).

## Headline result

```
manipulation_verdicts:
  m1: 2/3 models meaningfully reduce intrusion -> VALIDATED
  m2: 0/3                                       -> not validated
  m3: 1/3                                       -> not validated
at_least_one_manipulation_validated: true
```

**M1 (rule repetition) is a validated partial mechanism.** Per the
preregistered stop/go rule, this alone is enough for
`at_least_one_manipulation_validated = true` — the paper's depth
contribution (confirmed phenomenon → decomposed failure mode → partial,
evidence-based mitigation) is achieved. **But M2 and M3's null results
must not be read as clean evidence against their candidate mechanisms —
both runs have a disclosed, real implementation problem discovered only
after generating output, reported here rather than silently fixed and
re-run**, per the preregistration's own "no redesign after seeing
results" rule.

## M1 — rule repetition: clean, validated

| model | Delta_M mean [95% CI] | boundary acc | meaningfully reduces |
|---|---|---:|---|
| Qwen3.5-9B | 3.75 [1.02, 6.61] | 1.000 | **yes** |
| Gemma-3-12B-it | 13.97 [9.56, 18.67] | 0.969 | **yes** |
| Mistral-Small-24B | -0.47 [-2.50, 1.41] | 1.000 | no |

A single repeated reminder, placed right before the task question,
substantially reduces intrusion in the two models that showed baseline
intrusion (Qwen, Gemma) — Gemma's reduction is large (~14 points, more
than half of its 27.2-point baseline intrusion). Mistral, which never
showed baseline intrusion, is correctly unaffected (near-zero delta) —
exactly the selective pattern the preregistration's validity guards were
designed to distinguish from generic instruction-following improvement.
Boundary-probe accuracy stays high throughout (0.97–1.00), so this is not
explained by the manipulation accidentally improving general
comprehension. **This supports the instruction-salience/overwriting
account**: the exclusion instruction's effect appears to decay across the
prompt and partially recovers when restated adjacent to the task.

## M2 — temporal partitioning: confounded, not a clean test

| model | Delta_M mean [95% CI] | boundary acc |
|---|---|---:|
| Qwen3.5-9B | -4.45 [-12.58, 4.09] | **0.500** |
| Gemma-3-12B-it | 5.22 [-1.29, 11.94] | **0.000** |
| Mistral-Small-24B | 7.33 [2.40, 12.37] | **0.297** |

Boundary-probe accuracy collapses under M2 (0.0–0.5, vs. 0.81–1.00 for
M1/M3 and ~1.00 at baseline) — this is what correctly blocks all three
models from "meaningfully reducing" under the frozen validity guard, but
inspecting raw output (e.g. Gemma answers "YES" to all 64 M2 boundary
probes, expected "NO" throughout) points to a **real prompt-construction
gap, not a genuine finding about routing failure**: `build_m2`'s prompt
never includes an explicit "TARGET INFORMATION SET" framing paragraph
defining what "the evaluation point" refers to (M1 and M3 both inherit
this paragraph from the baseline prompt; M2 was rebuilt from raw
`AVAILABLE AT T`/`LEARNED AFTER T` blocks and this framing sentence was
never added). The boundary-probe question then asks about "the evaluation
point defined above" — a phrase with no antecedent in M2's own prompt.
**This is an implementation defect discovered only after generating
output, disclosed here rather than patched and silently re-run.** M2's
result is therefore **inconclusive on the information-routing hypothesis,
not evidence against it.**

## M3 — ex-ante commitment: degenerate, uninterpretable as designed

| model | Delta_M mean [95% CI] | boundary acc | meaningfully reduces |
|---|---|---:|---|
| Qwen3.5-9B | 12.75 [8.50, 16.98] | 1.000 | yes (see caveat) |
| Gemma-3-12B-it | 27.20 [22.00, 32.34] | 0.812 | no (boundary acc < 0.875) |
| Mistral-Small-24B | 3.28 [-1.17, 7.58] | 1.000 | no |

**Every one of the 192 M3 decisions (64 units × 3 models) exactly
reproduces that model's own baseline `OOB_WITHOUT` value, verbatim.**
Inspection confirms models are not re-deriving a judgment; they copy the
literal number stated in `PRIOR ASSESSMENT` back out. This makes
`Intrusion_M3 ≡ 0` for every unit by construction, which makes
`Delta_M3 ≡ Intrusion_baseline` exactly — the M3 numbers above are
mathematically identical to the confirmatory run's own baseline intrusion
values (compare: Qwen 12.75 [8.5, 17.0] and Gemma 27.2 [22.0, 32.3] in
`results/btf3_confirmatory_v1_results.md` — the same numbers to two
decimal places). **M3 as specified does not test the ex-ante-commitment
mechanism at all — it tests whether a model will copy a number it is
told, which is a different and far less interesting question.** The
task instruction ("Restate what the probability was... the prior
assessment already reflects it") was too leading and effectively invited
this degenerate response. This is a genuine design flaw, disclosed here;
**M3's result is uninterpretable regarding its intended mechanism, not
negative evidence against it.**

## What this does and doesn't establish

- **The paper's depth contribution stands on M1 alone**, which is a
  clean, validated, selective partial mechanism (instruction-salience/
  overwriting), with intact boundary-probe accuracy and no effect on the
  one model that never showed baseline intrusion.
- **M2 and M3 need a corrected, separately-preregistered re-run** before
  either can speak to their intended mechanisms — not a patch to this
  run. M2 needs the missing "TARGET INFORMATION SET" framing paragraph
  added to its prompt; M3 needs a task instruction that does not invite
  verbatim copying of the stated prior value (e.g. withholding the exact
  number and instead asking the model to reason from a qualitative
  description of its own prior stance, or requiring a fresh derivation
  while only asserting that a prior judgment existed).
- Per the preregistration's own discipline, **neither M2 nor M3 is
  redesigned or re-run within this document** — this v1 factorization
  round is complete as specified, with M1 validated and M2/M3 flagged as
  needing a v2 attempt in a future, freshly preregistered round if
  pursued further.
