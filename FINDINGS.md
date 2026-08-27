# Can LLMs Unring the Bell? — G0 results

Qwen3-4B / 8B / 14B / 32B, 144 frozen items across five task families, five
conditions plus independent rule and memory probes. Everything below was
produced after `data/items/frozen_v1.json` was committed; the Exclude conditions
had never been generated at freeze time (`PREREGISTRATION_G0.md`).

## Headline: the preregistered temporal hypothesis is inverted

Humans show the Unring-the-Bell pattern: an exclusion instruction that arrives
*after* the evidence works poorly. These models show the opposite, in every
model, at large effect size.

| model | n | RuleAcc (independent probe) | REI Exclude-Pre | REI Exclude-Post | Δ_time = post − pre | UTB (order-adjusted) |
|---|---:|---:|---|---|---|---|
| Qwen3-4B | 137 | 1.000 | +0.58 [+0.41, +0.75] | +0.14 [-0.02, +0.30] | -0.39 [-0.56, -0.22] | -0.38 [-0.56, -0.18] |
| Qwen3-8B | 144 | 1.000 | +0.45 [+0.34, +0.56] | +0.12 [+0.02, +0.21] | -0.32 [-0.43, -0.21] | -0.35 [-0.47, -0.22] |
| Qwen3-14B | 143 | 1.000 | +0.49 [+0.37, +0.60] | -0.07 [-0.19, +0.04] | -0.55 [-0.65, -0.46] | -0.49 [-0.61, -0.38] |
| Qwen3-32B | 143 | 1.000 | +0.21 [+0.08, +0.34] | -0.09 [-0.19, -0.00] | -0.29 [-0.39, -0.19] | -0.36 [-0.48, -0.25] |

`REI = 0` means the model decided as if it had never seen the evidence; `REI = 1`
means it used the evidence as fully as when told it was admissible. CIs are
10,000-resample item-level paired bootstraps, winsorised at ±3.

Against the preregistration:

* **H1 (rule knowledge) — passes.** On the independent probe the models say NO
  to "may you use this?" with p ≈ 1.000 in every model and every family, and YES
  with p = 1.000 in the Admit control. They also still recall the evidence
  content in the memory probe. So this is not a comprehension failure.
* **H2 (residual influence) — passes only weakly, and only Pre.** Post-exclusion
  residue is +0.12 to +0.14 in the two small models and indistinguishable from
  zero (slightly negative) in 14B and 32B.
* **H3 (post worse than pre) — fails, and reverses.** Δ_time is negative in all
  four models with CIs far from zero.
* **H4 (not a mere order effect) — passes, for the reversed effect.** UTB is
  −0.29 to −0.49. It is not generic recency: with an *admitting* rule, order does
  not matter at all (see the next table, `admit_pre` vs `admit_post`, both ≈ 1.0).

**The finding is therefore not "LLMs cannot unring the bell". It is that they
cannot pre-commit not to ring it.** Told in advance that a piece of evidence is
inadmissible, these models then read it and use roughly half its force anyway.
Told the identical thing after reading it, they discard it almost completely.

## What fixes Pre — and it is not more instruction

| condition | Qwen3-4B | Qwen3-8B | Qwen3-14B | Qwen3-32B |
|---|---|---|---|---|
| `admit_pre` | +0.97 | +0.99 | +1.02 | +0.95 |
| `admit_post` | +1.01 | +1.01 | +0.98 | +1.04 |
| `admit_pre_repeat` | +1.02 | +1.01 | +1.09 | +1.08 |
| `exclude_pre` | +0.58 | +0.45 | +0.49 | +0.21 |
| `exclude_pre_repeat` | +0.12 | +0.07 | +0.10 | -0.03 |
| `exclude_post` | +0.14 | +0.12 | -0.07 | -0.09 |
| `exclude_post_reencode` | +0.11 | +0.02 | -0.02 | -0.11 |
| `ledger` | +0.12 | -0.01 | -0.03 | -0.08 |
| `sanitation` | -0.16 | -0.03 | -0.10 | -0.06 |

`exclude_pre_repeat` is the *same rule text, said twice* — once before the
evidence and once after. It removes essentially all of the Pre residue
(paired contrast vs `exclude_pre`: +0.24 to +0.47, p < 1e-4 in every model) and
lands on top of `exclude_post`. The rescue is positional, not rhetorical: the
extra copy carries no new information, and the matched `admit_pre_repeat`
control moves nothing.

The two structural mitigations both work and are indistinguishable from full
context sanitation. An explicit `[ADMISSIBLE] / [EXCLUDED]` ledger reaches
REI ≈ 0 while still showing the model the excluded item — so removing the
information is not required, only routing it correctly.

## Where the residue survives

| split | 4B pre / post | 8B pre / post | 14B pre / post | 32B pre / post |
|---|---|---|---|---|
| `true_but_forbidden` | +0.61 / +0.24 | +0.37 / +0.20 | +0.43 / -0.06 | +0.03 / -0.12 |
| `false_or_unreliable` | +0.52 / -0.10 | +0.63 / -0.07 | +0.62 / -0.10 | +0.63 / -0.03 |
| `legal_judgment` | +0.45 / +0.05 | +0.53 / +0.25 | +0.30 / -0.35 | +0.42 / +0.08 |
| `evidence_inference` | +0.65 / +0.11 | +0.51 / +0.10 | +0.55 / -0.00 | +0.25 / -0.10 |
| `ranking_selection` | +0.59 / +0.27 | +0.51 / -0.14 | +0.93 / -0.00 | +0.00 / -0.43 |
| `outcome_evaluation` | +0.82 / +0.43 | +0.39 / +0.40 | +0.56 / +0.29 | +0.01 / -0.12 |
| `numeric_aggregation` | +0.48 / -0.07 | +0.19 / -0.07 | +0.13 / -0.02 | +0.21 / +0.01 |

Two things survive post-exclusion where nothing else does:

* **True-but-forbidden beats false-or-unreliable.** Information the model is told
  is *wrong* is discarded cleanly (post REI ≈ −0.10 in all four models). Information
  it is told is *true but not permitted* leaves residue in the smaller models.
  The hard case is normative gating, not belief revision — the H5 direction.
* **Outcome evaluation is the one family with order-independent residue**
  (8B: +0.39 pre / +0.40 post; Δ_time ≈ 0). This is ordinary outcome bias, and it
  behaves like the human effect rather than like the positional effect above.

Scale helps but does not finish the job: 32B is near zero almost everywhere, yet
still shows +0.21 Pre residue and a −0.36 UTB.

## Mechanism (Qwen3-8B, 75 items)

Restricted to `legal_judgment` + `evidence_inference`, the two families where a
fixed-position readout tracks the behavioural one (item-level r = 0.76 and 0.90;
`results/mech/direct_readout.json`). Full report in `results/mech/`.

**C. Evidence-span causal gate.** Blocking every query position downstream of the
evidence from attending to the evidence span:

| condition | REI ungated | REI gated | removed |
|---|---|---|---|
| `exclude_pre` | +0.46 | −0.12 [−0.24, +0.01] | +0.58 [+0.44, +0.74], p < 1e-4 |
| `exclude_post` | +0.32 | −0.08 [−0.22, +0.06] | +0.40 [+0.31, +0.50], p < 1e-4 |

The residual influence is carried by direct attention reads of the excluded span
at and after the decision. Cutting that one path returns the answer to Base. This
is **M3, a decision-gating / readout failure** — not M1: the model has the
invalidity (RuleAcc ≈ 1.0) and still routes the evidence into the answer.

**A. Attention routing at the answer position.** Per-token attention from the
answer position, rule span relative to evidence span (summed over all 36 layers,
median over items):

| condition | rule : evidence |
|---|---|
| `exclude_pre` | 2.14 [1.83, 2.78] |
| `exclude_pre_repeat` | 2.68 [2.44, 3.38] |
| `exclude_post` | 2.64 [2.27, 3.60] |

The behavioural rescue has the predicted attention signature: repeating the rule
after the evidence moves the ratio onto `exclude_post`, and REI follows
(+0.46 → +0.30 → +0.32). A rule the answer position barely looks at is a rule
that does not gate. (`results/mech/mechanism_report.md` reports the same
quantity band-averaged rather than layer-summed, so its absolute values differ;
the ordering is identical.)

**B. Answer-position patching, Post → Pre.** Patching the residual stream at the
answer position recovers none of the Pre/Post gap below layer 18, then rises
sharply: 50% recovery at layer 21, ≈85% by layer 27, of 36. The gating decision
is made late, in the upper-middle layers, well after both the evidence and the
rule have been encoded.

## Methodological findings worth keeping

Three readouts were piloted on Base/Admit only, before the dataset was frozen:

1. **Greedy integer on a 0–100 scale collapses.** Qwen3-8B emitted essentially
   {20, 45, 65, 85}, too coarse for a ratio metric.
2. **A one-token answer with no rationale can be anti-correlated with the model's
   own judgment.** On `ranking_selection` the model reasons "the report shows
   Vendor A's reliability is 2/10 … 0" but, forced to answer immediately, emits
   9 with p = 0.98. Any paper using single-token rating readouts on this kind of
   task needs to check this.
3. **A 6σ outlier is silently discarded even when the rule says to use it.** The
   first numeric-aggregation design had no leverage at all: the model dropped the
   invalid reading in the Admit condition. The critical reading has to be
   *plausible*, which also makes the design cleaner — invalidity is then knowable
   only from the rule, never from the value.

The adopted readout is a greedily decoded two-sentence rationale followed by the
expectation of the next-token distribution over the digits 0–9 at a fixed
position. Deterministic, continuous, no parsing, no LLM judge.

## What this means for the plan

The plan's Stage 0 gate is passed, but the paper's spine changes. The temporal
claim survives with its sign flipped, and it is now a claim about *where an
instruction sits relative to the information it governs*, with a causal
mechanism and a working fix. Section 13's decision table maps this to
"generality holds; timing claim inverted" — keep the main question, drop the
human-analogy framing, and lead with the pre-commitment failure.

Open items: five conditions on a naturalistic legal corpus rather than authored
vignettes; wording paraphrases of the ruling; whether the layer-21 gating locus
moves with scale; and whether counterfactual exclusion training on the verifiable
families transfers to the legal ones.
