# Can LLMs Unring the Bell? — G0 results

Twelve instruct models from four vendors plus two masked diffusion LMs, over 144
frozen items across five task families, five conditions plus independent rule and
memory probes. Everything below was
produced after `data/items/frozen_v1.json` was committed; the Exclude conditions
had never been generated at freeze time (`PREREGISTRATION_G0.md`).

## Headline: the preregistered temporal hypothesis is inverted

Humans show the Unring-the-Bell pattern: an exclusion instruction that arrives
*after* the evidence works poorly. Every model tested shows the opposite, at
large effect size — six instruct families from four vendors, plus two masked
diffusion LMs (below).

| model | usable n | RuleAcc pre | RuleAcc post | REI Exclude-Pre | REI Exclude-Post | Δ_time | UTB |
|---|---:|---:|---:|---|---|---|---|
| Phi-4-mini (3.8B) | 138/144 | 0.903 | 0.984 | +0.50 [+0.32, +0.67] | +0.24 [+0.09, +0.38] | -0.30 [-0.46, -0.14] | -0.15 [-0.35, +0.05] |
| Gemma-3-4B | 133/144 | 0.962 | 1.000 | +0.43 [+0.23, +0.61] | +0.28 [+0.06, +0.48] | -0.16 [-0.33, +0.00] | -0.20 [-0.40, +0.01] |
| Gemma-3-12B | 141/144 | 0.889 | 1.000 | +0.43 [+0.28, +0.57] | +0.07 [-0.06, +0.20] | -0.35 [-0.44, -0.26] | -0.38 [-0.51, -0.25] |
| Qwen2.5-7B | 134/144 | 0.822 | 1.000 | +0.54 [+0.36, +0.70] | +0.22 [+0.06, +0.37] | -0.30 [-0.45, -0.14] | -0.44 [-0.62, -0.26] |
| Qwen2.5-32B | 140/144 | 0.990 | 1.000 | +0.30 [+0.20, +0.41] | +0.00 [-0.08, +0.07] | -0.26 [-0.36, -0.15] | -0.29 [-0.41, -0.17] |
| Mistral-Small-24B | 141/144 | 0.983 | 0.999 | +0.19 [+0.08, +0.31] | -0.03 [-0.14, +0.08] | -0.21 [-0.31, -0.12] | -0.16 [-0.27, -0.05] |
| Qwen3-4B | 137/144 | 0.942 | 1.000 | +0.58 [+0.41, +0.75] | +0.14 [-0.02, +0.30] | -0.39 [-0.56, -0.22] | -0.38 [-0.56, -0.18] |
| Qwen3-8B | 144/144 | 0.997 | 1.000 | +0.45 [+0.34, +0.56] | +0.12 [+0.02, +0.21] | -0.32 [-0.43, -0.21] | -0.35 [-0.47, -0.22] |
| Qwen3-14B | 143/144 | 0.874 | 1.000 | +0.49 [+0.37, +0.60] | -0.07 [-0.19, +0.04] | -0.55 [-0.65, -0.46] | -0.49 [-0.61, -0.38] |
| Qwen3-32B | 143/144 | 0.861 | 1.000 | +0.21 [+0.08, +0.34] | -0.09 [-0.19, -0.00] | -0.29 [-0.39, -0.19] | -0.36 [-0.48, -0.25] |
| Qwen3.5-9B | 136/144 | 0.936 | 1.000 | +0.07 [-0.11, +0.24] | -0.18 [-0.35, -0.03] | -0.29 [-0.46, -0.12] | -0.36 [-0.55, -0.18] |
| Qwen3.5-27B | 142/144 | 0.971 | 0.999 | -0.05 [-0.21, +0.11] | -0.29 [-0.44, -0.15] | -0.22 [-0.34, -0.09] | -0.21 [-0.36, -0.06] |
| Qwen3-8B (replicate) | 144/144 | 0.998 | 1.000 | +0.49 [+0.37, +0.60] | +0.10 [+0.00, +0.19] | -0.37 [-0.49, -0.26] | -0.40 [-0.53, -0.27] |

`REI = 0` means the model decided as if it had never seen the evidence; `REI = 1`
means it used the evidence as fully as when told it was admissible. CIs are
10,000-resample item-level paired bootstraps, winsorised at ±3. The last row is
an independent replicate of Qwen3-8B (see *Reproducibility*).

Against the preregistration:

* **H1 (rule knowledge) — passes.** On the independent probe with the rule after
  the evidence, models say NO to "may you use this?" with p ≈ 1.0, and YES with
  p = 1.0 in the Admit control. They also still recall the evidence in the memory
  probe. Not a comprehension failure. Note the `RuleAcc pre` column: stated rule
  knowledge is *slightly* weaker when the rule precedes the evidence (0.82–0.99),
  so a small M1 component rides along with the gating failure.
* **H2 (residual influence) — passes weakly, and mostly in Pre.** Post-exclusion
  residue is +0.07 to +0.28 in the smaller models and at or below zero from
  Qwen2.5-32B, Mistral-24B, Qwen3-14B/32B and both Qwen3.5 models.
* **H3 (post worse than pre) — fails, and reverses.** Δ_time is negative in all
  twelve models; ten of twelve CIs exclude zero.
* **H4 (not a mere order effect) — passes, for the reversed effect.** UTB is
  −0.15 to −0.49 (Phi-4-mini and Gemma-3-4B touch zero). It is not generic
  recency: with an *admitting* rule, order does not matter anywhere
  (`admit_pre` ≈ `admit_post` ≈ 1.0 in every model).

**The finding is therefore not "LLMs cannot unring the bell". It is that they
cannot pre-commit not to ring it.** Told in advance that evidence is
inadmissible, models then read it and use a large fraction of its force anyway.
Told the identical thing afterwards, they discard it almost completely.

Scale and generation both help, and the newest models overshoot: Qwen3.5-9B and
-27B have no Pre residue left (+0.07, −0.05) but now *overcorrect* after
exclusion (−0.18, −0.29), and Δ_time stays negative. The asymmetry outlives the
residue.

## What fixes Pre — and it is not more instruction

| model | `admit_pre` | `admit_post` | `admit_pre_repeat` | `exclude_pre` | `exclude_pre_repeat` | `exclude_post` | `exclude_post_reencode` | `ledger` | `sanitation` |
|---|---|---|---|---|---|---|---|---|---|
| Phi-4-mini (3.8B) | +1.00 | +0.96 | +0.93 | +0.50 | +0.31 | +0.24 | +0.10 | +0.07 | -0.05 |
| Gemma-3-4B | +1.00 | +1.00 | +0.94 | +0.43 | +0.25 | +0.28 | +0.28 | +0.08 | -0.05 |
| Gemma-3-12B | +0.98 | +1.02 | +1.00 | +0.43 | +0.23 | +0.07 | +0.05 | -0.05 | -0.02 |
| Qwen2.5-7B | +0.93 | +1.06 | +1.06 | +0.54 | +0.28 | +0.22 | +0.14 | +0.09 | -0.09 |
| Qwen2.5-32B | +1.01 | +0.98 | +1.00 | +0.30 | +0.03 | +0.00 | -0.02 | -0.01 | -0.02 |
| Mistral-Small-24B | +1.02 | +0.98 | +0.97 | +0.19 | +0.01 | -0.03 | +0.01 | -0.06 | -0.02 |
| Qwen3-4B | +0.97 | +1.01 | +1.02 | +0.58 | +0.12 | +0.14 | +0.11 | +0.12 | -0.16 |
| Qwen3-8B | +0.99 | +1.01 | +1.01 | +0.45 | +0.07 | +0.12 | +0.02 | -0.01 | -0.03 |
| Qwen3-14B | +1.02 | +0.98 | +1.09 | +0.49 | +0.10 | -0.07 | -0.02 | -0.03 | -0.10 |
| Qwen3-32B | +0.95 | +1.04 | +1.08 | +0.21 | -0.03 | -0.09 | -0.11 | -0.08 | -0.06 |
| Qwen3.5-9B | +0.91 | +1.08 | +1.06 | +0.07 | -0.12 | -0.18 | -0.27 | -0.27 | -0.04 |
| Qwen3.5-27B | +0.95 | +1.02 | +1.05 | -0.05 | -0.29 | -0.29 | -0.32 | -0.25 | -0.13 |
| Qwen3-8B (replicate) | +0.98 | +1.02 | +1.02 | +0.49 | +0.08 | +0.10 | +0.05 | -0.01 | +0.01 |

| model | pre − post (asymmetry) | pre − pre_repeat (rule-recency rescue) | admit_pre − admit_pre_repeat (control) |
|---|---|---|---|
| Phi-4-mini (3.8B) | +0.26 [+0.08, +0.43] p=0.0052 | +0.18 [+0.04, +0.31] p=0.0164 | +0.08 [-0.10, +0.24] p=0.3790 |
| Gemma-3-4B | +0.15 [+0.02, +0.29] p=0.0238 | +0.18 [+0.06, +0.30] p=0.0032 | +0.06 [-0.07, +0.18] p=0.3210 |
| Gemma-3-12B | +0.36 [+0.27, +0.44] p=0.0000 | +0.20 [+0.12, +0.27] p=0.0000 | -0.02 [-0.10, +0.05] p=0.7524 |
| Qwen2.5-7B | +0.32 [+0.17, +0.48] p=0.0000 | +0.26 [+0.06, +0.45] p=0.0118 | -0.13 [-0.26, +0.01] p=0.0706 |
| Qwen2.5-32B | +0.30 [+0.16, +0.46] p=0.0000 | +0.27 [+0.15, +0.42] p=0.0000 | +0.00 [-0.06, +0.07] p=0.9414 |
| Mistral-Small-24B | +0.22 [+0.13, +0.32] p=0.0000 | +0.18 [+0.11, +0.26] p=0.0000 | +0.05 [-0.02, +0.11] p=0.1406 |
| Qwen3-4B | +0.44 [+0.27, +0.61] p=0.0000 | +0.47 [+0.32, +0.61] p=0.0000 | -0.05 [-0.18, +0.10] p=0.5056 |
| Qwen3-8B | +0.33 [+0.22, +0.45] p=0.0000 | +0.38 [+0.28, +0.47] p=0.0000 | -0.03 [-0.09, +0.04] p=0.4018 |
| Qwen3-14B | +0.55 [+0.45, +0.67] p=0.0000 | +0.39 [+0.28, +0.48] p=0.0000 | -0.06 [-0.14, +0.00] p=0.0628 |
| Qwen3-32B | +0.31 [+0.20, +0.42] p=0.0000 | +0.24 [+0.14, +0.35] p=0.0000 | -0.13 [-0.25, -0.04] p=0.0010 |
| Qwen3.5-9B | +0.26 [+0.06, +0.44] p=0.0156 | +0.19 [+0.03, +0.37] p=0.0232 | -0.15 [-0.30, -0.04] p=0.0068 |
| Qwen3.5-27B | +0.24 [+0.10, +0.39] p=0.0002 | +0.24 [+0.11, +0.37] p=0.0002 | -0.10 [-0.21, -0.02] p=0.0052 |
| Qwen3-8B (replicate) | +0.38 [+0.26, +0.51] p=0.0000 | +0.40 [+0.31, +0.50] p=0.0000 | -0.03 [-0.10, +0.03] p=0.3198 |

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

## The architectural explanation is wrong

The plan's section 11.4 proposes a causal-transformer account: with `E → R` the
evidence tokens are contextualised before the rule exists, so the binding has to
be redone downstream; with `R → E` it does not. That predicts the asymmetry
should weaken or vanish under bidirectional attention.

It does not. LLaDA-8B-Instruct and Dream-v0-Instruct-7B are masked diffusion LMs:
attention over the prompt is bidirectional, so rule and evidence see each other
regardless of order. Read at an identical fixed position (`ANSWER: <mask>`, one
forward pass, expectation over the ten digit tokens), restricted to
`legal_judgment` + `evidence_inference`:

| model | attention | usable n | RuleAcc post | REI Exclude-Pre | REI Exclude-Post | pre − post | pre − pre_repeat |
|---|---|---:|---:|---|---|---|---|
| phi4-mini | causal | 72 | 0.982 | +0.55 [+0.28, +0.81] | +0.28 [+0.03, +0.52] | +0.27 [+0.17, +0.37] p=0.0000 | +0.23 [+0.18, +0.28] p=0.0000 |
| gemma3-12b | causal | 75 | 1.000 | +0.64 [+0.46, +0.79] | +0.25 [+0.10, +0.37] | +0.39 [+0.29, +0.50] p=0.0000 | +0.22 [+0.16, +0.28] p=0.0000 |
| qwen2.5-7b | causal | 70 | 1.000 | +0.63 [+0.41, +0.82] | +0.19 [+0.02, +0.35] | +0.43 [+0.28, +0.62] p=0.0000 | +0.22 [+0.14, +0.31] p=0.0000 |
| qwen3-8b | causal | 75 | 1.000 | +0.43 [+0.20, +0.65] | +0.27 [+0.06, +0.46] | +0.17 [+0.07, +0.27] p=0.0002 | +0.17 [+0.11, +0.22] p=0.0000 |
| mistral-small-24b | causal | 75 | 0.999 | +0.30 [+0.17, +0.41] | +0.06 [-0.02, +0.13] | +0.24 [+0.14, +0.34] p=0.0000 | +0.24 [+0.16, +0.31] p=0.0000 |
| llada-8b | masked diffusion | 69 | 0.996 | +0.56 [+0.32, +0.79] | +0.25 [+0.02, +0.46] | +0.31 [+0.21, +0.43] p=0.0000 | +0.18 [+0.10, +0.27] p=0.0000 |
| dream-7b | masked diffusion | 73 | 0.998 | +0.70 [+0.55, +0.84] | +0.29 [+0.14, +0.42] | +0.42 [+0.35, +0.49] p=0.0000 | +0.16 [+0.11, +0.21] p=0.0000 |

Every validity anchor holds for the diffusion models exactly as for the causal
ones (`admit_pre` / `admit_post` REI = 1.011 / 0.989 for LLaDA and 1.022 / 0.978
for Dream; digit mass 0.945 and 0.998; median |L| 29 and 21). Dream shows the
*largest* asymmetry in the whole comparison.

So the asymmetry is not a consequence of the causal mask. It is a learned prior
that an instruction governs what follows it — one that survives the removal of
the architectural constraint that would explain it. The attention correlate
measured on Qwen3-8B below is a symptom of that prior, not its cause.

Two implementation notes, since both models need care: Dream keeps the shifted
convention of the autoregressive checkpoint it was initialised from (position i
predicts token i+1) and degenerates to `<|endoftext|>` unless the prompt ends in
a *block* of masks rather than one; with a single mask and no shift its digit
mass is 0.000. LLaDA needs neither.

## Reproducibility

Qwen3-8B was run twice end to end in separate processes with identical commands.
Item-level correlations between runs: REI_pre r = 0.97, REI_post r = 0.87,
Δ_time r = 0.87; aggregate estimates move by at most 0.06 REI, against effects of
0.2–0.6. Raw Y differs by a median of 0.017 points on the 0–100 scale, but 6.9%
of cells differ by more than 5 points: vLLM batching is not bitwise deterministic,
and at a near-tie the greedy rationale takes a different path. The readout itself
is deterministic; the rationale in front of it is not.

Item-level bootstrap assumes items are independent, and they are not — the 60
legal items are 10 case skeletons crossed with 6 evidence types. Resampling
clusters (38 of them) instead barely widens the intervals: Qwen3-8B Δ_time
[-0.427, -0.211] → [-0.446, -0.186]; Gemma-3-12B [-0.443, -0.266] →
[-0.458, -0.248]. Full table in `results/cluster_robustness.md`.

## Where the residue survives

| model | legal_judgment | evidence_inference | ranking_selection | outcome_evaluation | numeric_aggregation |
|---|---|---|---|---|---|
| Phi-4-mini (3.8B) | +0.29 / +0.51 (n=42) | +0.83 / +0.26 (n=30) | +0.34 / -0.30 (n=26) | +0.72 / +0.55 (n=21) | +0.37 / +0.00 (n=19) |
| Gemma-3-4B | +0.00 / -0.12 (n=40) | +0.88 / +0.78 (n=30) | +0.77 / +0.47 (n=21) | +0.40 / +0.40 (n=21) | +0.27 / +0.01 (n=21) |
| Gemma-3-12B | +0.39 / +0.19 (n=44) | +0.85 / +0.16 (n=30) | +0.20 / -0.25 (n=25) | +0.24 / -0.01 (n=21) | +0.37 / +0.19 (n=21) |
| Qwen2.5-7B | +0.37 / +0.12 (n=43) | +0.94 / +0.02 (n=30) | +0.64 / +0.48 (n=21) | +0.37 / +0.24 (n=21) | +0.36 / +0.44 (n=19) |
| Qwen2.5-32B | +0.17 / -0.06 (n=45) | +0.46 / +0.09 (n=30) | +0.22 / -0.02 (n=27) | +0.35 / +0.17 (n=20) | +0.43 / -0.15 (n=18) |
| Mistral-Small-24B | +0.18 / -0.03 (n=43) | +0.29 / +0.05 (n=30) | +0.12 / -0.06 (n=27) | +0.34 / +0.02 (n=21) | +0.03 / -0.14 (n=20) |
| Qwen3-4B | +0.45 / +0.05 (n=40) | +0.65 / +0.11 (n=30) | +0.59 / +0.27 (n=26) | +0.82 / +0.43 (n=20) | +0.48 / -0.07 (n=21) |
| Qwen3-8B | +0.53 / +0.25 (n=45) | +0.51 / +0.10 (n=30) | +0.51 / -0.14 (n=27) | +0.39 / +0.40 (n=21) | +0.19 / -0.07 (n=21) |
| Qwen3-14B | +0.30 / -0.35 (n=44) | +0.55 / -0.00 (n=30) | +0.93 / -0.00 (n=27) | +0.56 / +0.29 (n=21) | +0.13 / -0.02 (n=21) |
| Qwen3-32B | +0.42 / +0.08 (n=45) | +0.25 / -0.10 (n=30) | +0.00 / -0.43 (n=27) | +0.01 / -0.12 (n=20) | +0.21 / +0.01 (n=21) |
| Qwen3.5-9B | -0.22 / -0.23 (n=43) | +0.61 / -0.30 (n=30) | -0.19 / -0.35 (n=26) | +0.21 / +0.07 (n=20) | +0.09 / +0.09 (n=17) |
| Qwen3.5-27B | -0.08 / -0.33 (n=44) | +0.19 / -0.15 (n=30) | -0.58 / -0.41 (n=27) | +0.22 / -0.25 (n=21) | +0.09 / -0.28 (n=20) |
| Qwen3-8B (replicate) | +0.52 / +0.24 (n=45) | +0.50 / +0.11 (n=30) | +0.64 / -0.25 (n=27) | +0.49 / +0.42 (n=21) | +0.18 / -0.08 (n=21) |

| model | true_but_forbidden | false_or_unreliable |
|---|---|---|
| Phi-4-mini (3.8B) | +0.44 / +0.31 (n=96) | +0.62 / +0.07 (n=42) |
| Gemma-3-4B | +0.38 / +0.27 (n=91) | +0.52 / +0.29 (n=42) |
| Gemma-3-12B | +0.36 / +0.13 (n=98) | +0.58 / -0.05 (n=43) |
| Qwen2.5-7B | +0.58 / +0.28 (n=91) | +0.45 / +0.08 (n=43) |
| Qwen2.5-32B | +0.20 / -0.01 (n=98) | +0.53 / +0.04 (n=42) |
| Mistral-Small-24B | +0.07 / -0.07 (n=99) | +0.49 / +0.07 (n=42) |
| Qwen3-4B | +0.61 / +0.24 (n=96) | +0.52 / -0.10 (n=41) |
| Qwen3-8B | +0.37 / +0.20 (n=100) | +0.63 / -0.07 (n=44) |
| Qwen3-14B | +0.43 / -0.06 (n=100) | +0.62 / -0.10 (n=43) |
| Qwen3-32B | +0.03 / -0.12 (n=99) | +0.63 / -0.03 (n=44) |
| Qwen3.5-9B | -0.04 / -0.16 (n=97) | +0.35 / -0.25 (n=39) |
| Qwen3.5-27B | -0.18 / -0.30 (n=98) | +0.24 / -0.25 (n=44) |
| Qwen3-8B (replicate) | +0.41 / +0.16 (n=100) | +0.66 / -0.05 (n=44) |

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
median over items). Read as a correlate of the learned positional prior, not as
its cause — the diffusion results above rule out the architectural reading:

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
moves with scale; the same attention and span-gate analysis inside LLaDA, which
would show directly what a bidirectional model does with an early rule; and
whether counterfactual exclusion training on the verifiable families transfers to
the legal ones.

Dataset limitations to fix before a formal version: only 10 independent legal
case skeletons; `procedural_hearsay` collapsed to 2 surviving items, so that arm
of the exclusion-reason axis is effectively untested; a single ruling wording
with no paraphrase control; and screening performed on Qwen3-8B alone (the frozen
set transfers well — 133–144 of 144 items stay usable on every other model — but
it was not screened on them).
