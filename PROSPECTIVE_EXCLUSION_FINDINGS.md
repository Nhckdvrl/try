# Prospective evidence exclusion — full results (G0 and the controlled stages)

> **Status, 2026-09-03.** This is a **live main-line results document**. It was
> written under the original *Can LLMs Unring the Bell?* title and was briefly
> filed under `archive/` while the project ran the BTF-3 hindsight branch; that
> branch is stopped and this line is the paper. The text below is preserved as
> written, including its original framing and its open items, because it is the
> record of what was found when. Current framing is in `PAPER_FRAME.md`; the
> later controlled stages are in `stages/`.


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

**What this establishes, and what it does not.** The asymmetry persists under
bidirectional prompt attention, which rules out causal masking as a *necessary*
explanation: this is not an architectural irreversibility. That is the whole of
the claim. It moves the explanation from architectural impossibility toward
learned or representational properties of instruction binding and contextual
control — but it does not identify which. Bidirectional attention still leaves
text order, positional encodings, directional anaphora ("the preceding evidence"
vs "the following evidence"), and instruction-tuning distribution intact. Three
accounts remain live and this experiment separates none of them:

* **H-A, decision proximity.** Instructions nearer the answer are weighted more.
  The `exclude_pre_repeat` rescue is consistent with this. *(Tested below —
  rejected.)*
* **H-B, prospective binding.** A rule about evidence that does not yet exist has
  to be held as a future constraint; a rule about evidence already present can
  attach to a concrete span. The difficulty would be binding, not distance.
* **H-C, scope prior from language.** "The preceding evidence is invalid" is a far
  more common construction, with a far clearer referent, than a rule about
  evidence the reader has not seen. *(Tested below — contributes, but does not
  explain the effect.)*

The attention correlate measured on Qwen3-8B below is consistent with all three;
it is not evidence for any one of them. The next section separates them.

## Separating the three accounts

Three experiments on the same frozen items, four models (Qwen3-8B, Gemma-3-12B,
Mistral-Small-24B, Qwen3.5-27B). Full tables in `results/stage2_tables.md`.

### 1. Distance does not matter; Before/After is the whole effect

Exclusion arm only, `REI ~ Distance + Before + Distance:Before`, cluster bootstrap over case skeletons. Distance is the measured token count from the RULING block to the answer position.

| model | Distance (per 100 tok) | Before (rule precedes evidence) | Distance x Before |
|---|---|---|---|
| Qwen3-8B | -0.0030 [-0.0199, +0.0129] p=0.7520 | **+0.3788 [+0.2247, +0.5376] p=0.0000** | -0.0311 [-0.0616, -0.0038] p=0.0245 |
| Gemma-3-12B | +0.0017 [-0.0093, +0.0137] p=0.7500 | **+0.3338 [+0.1934, +0.4687] p=0.0000** | -0.0129 [-0.0289, +0.0039] p=0.1315 |
| Mistral-Small-24B | -0.0038 [-0.0232, +0.0139] p=0.6845 | **+0.2215 [+0.1218, +0.3282] p=0.0000** | -0.0107 [-0.0289, +0.0059] p=0.2110 |
| Qwen3.5-27B | +0.0074 [-0.0066, +0.0215] p=0.3030 | **+0.3028 [+0.1541, +0.4580] p=0.0000** | -0.0323 [-0.0574, -0.0041] p=0.0240 |

The cleanest single comparison, Qwen3-8B: a rule **587 tokens** from the answer
but placed *after* the evidence gives REI +0.095, while a rule **156 tokens** from
the answer — nearly four times closer — placed *before* the evidence gives +0.463.
Within the Before arm, moving the rule further from the answer *reduces* leakage
(+0.463 -> +0.350 -> +0.272), the opposite of what recency predicts.

### 2. Removing directional anaphora shrinks the gap but does not close it

One identical sentence in both orders — `Evidence E7 is excluded. It must have
zero influence on your final judgment.` — with no *preceding* / *following* /
*above* / *below*.

| model | `id_exclude_pre` | `id_exclude_post` | pre - post | pre - pre_with_marker |
|---|---|---|---|---|
| Qwen3-8B | +0.213 [+0.107, +0.320] | -0.001 [-0.099, +0.094] | +0.214 [+0.133, +0.299] p=0.0000 | -0.111 [-0.204, -0.017] p=0.0250 |
| Gemma-3-12B | +0.281 [+0.151, +0.402] | +0.120 [-0.007, +0.243] | +0.160 [+0.048, +0.272] p=0.0080 | -0.025 [-0.148, +0.076] p=0.7060 |
| Mistral-Small-24B | +0.006 [-0.103, +0.109] | -0.008 [-0.116, +0.089] | +0.014 [-0.076, +0.100] p=0.7590 | +0.050 [-0.029, +0.116] p=0.1815 |
| Qwen3.5-27B | -0.059 [-0.199, +0.073] | -0.205 [-0.329, -0.086] | +0.146 [+0.023, +0.283] p=0.0260 | -0.036 [-0.125, +0.053] p=0.4405 |

The identifier framing lowers leakage a lot in absolute terms (Qwen3-8B +0.45 -> +0.21, Mistral +0.19 -> +0.01), so referential clarity matters. But the
asymmetry survives it in three of four models. `id_exclude_pre_marker` — the rule
before the evidence, plus the evidence block headed `EVIDENCE E7 — EXCLUDED` and
no restatement of the rule — never helps, and hurts on Qwen3-8B (p=0.025). A
binding cue at the moment the evidence arrives is not enough.

### 3. The position effect exists only at zero requested weight

Same items, rule replaced by a requested weight. `w = 1.00` is the leverage anchor.

| requested w | Qwen3-8B | Gemma-3-12B | Mistral-Small-24B | Qwen3.5-27B |
|---:|---|---|---|---|
| 0.00 | +0.48 / -0.05 | +0.58 / +0.15 | +0.06 / -0.04 | -0.07 / -0.20 |
| 0.25 | +0.57 / +0.47 | +0.58 / +0.67 | +0.48 / +0.40 | +0.33 / +0.22 |
| 0.50 | +0.58 / +0.48 | +0.65 / +0.69 | +0.51 / +0.49 | +0.54 / +0.50 |
| 0.75 | +0.84 / +0.82 | +0.83 / +0.86 | +0.72 / +0.67 | +0.68 / +0.72 |
| 1.00 | +0.95 / +1.05 | +0.97 / +1.03 | +1.01 / +0.98 | +0.95 / +1.04 |

Cells are *rule before evidence* / *rule after evidence*. Mean pre-post gap across
the four models, by requested weight:

| requested w | 0.00 | 0.25 | 0.50 | 0.75 | 1.00 |
|---|---|---|---|---|---|
| mean pre - post | **+0.298** | +0.050 | +0.028 | -0.001 | -0.050 |

The asymmetry collapses to nothing the moment the requested weight is anything
other than zero. This is not general position-dependent control precision: it is
specific to complete suppression.

A position-independent finding falls out of the same sweep: models barely
distinguish 0.25 from 0.50 (Qwen3-8B: +0.57 vs +0.58; Mistral: +0.48 vs +0.51).
Requested-weight following is poor in the middle of the range regardless of order.


**Verdict.** H-A is rejected: distance to the answer has no main effect in any
model, and within the Before arm more distance *helps*. H-C is not the
explanation: stripping every directional referent shrinks the effect
substantially but leaves it significant in three of four models. What remains is
prospective binding — but *generic* prospective binding is too broad an account,
and Stage 3A below narrows it. A model that applies w=0.25 to future evidence is
already binding a rule to an object that does not exist yet; what it cannot do is
drive that object's contribution to zero.

Two results cut against the obvious follow-ups and are worth stating plainly.
Tagging the evidence block as excluded at the moment it arrives does not rescue
the Pre condition; it made Qwen3-8B worse. And the failure is not a general
inability to follow positional instructions — at any non-zero requested weight,
order stops mattering.

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

## Stage 3A — what the failure actually is

Six models, the same frozen 144 items. Full tables in `results/stage3_tables.md`.

### The declarative policy is perfect; the decision ignores it

A separate call, same context, asks what weight the evidence should get. The
decision run never sees this question.

| model | says weight (mean) | says exactly 0 | REI, rule BEFORE | REI, rule AFTER |
|---|---:|---:|---|---|
| Qwen3-8B | 0.00% | 100.0% | +0.511 [+0.417, +0.605] | +0.181 [+0.080, +0.276] |
| Gemma-3-12B | 0.00% | 100.0% | +0.419 [+0.289, +0.539] | +0.076 [-0.115, +0.258] |
| Mistral-24B | 0.00% | 100.0% | +0.085 [-0.040, +0.204] | +0.003 [-0.121, +0.121] |
| Qwen3.5-27B | 0.00% | 100.0% | -0.021 [-0.187, +0.135] | -0.301 [-0.471, -0.147] |
| Qwen3-32B | 0.00% | 100.0% | +0.237 [+0.137, +0.338] | -0.083 [-0.183, +0.017] |
| Phi-4-mini | 0.00% | 100.0% | +0.644 [+0.510, +0.777] | +0.387 [+0.233, +0.545] |

Every model, in both arms, states the required weight as exactly 0 on 100% of
items — and then, with the rule stated first, gives that evidence up to 0.64 of
its normal causal weight. **This is not a retrieval failure.** The rule is
recalled and correctly bound at the declarative level in the prospective
condition just as well as in the retrospective one, and the decision still reads
the evidence. It separates this from prospective-memory benchmarks, which ask
whether the model remembers to act at all.

### Zero behaves differently from any small weight

One identical sentence, `The causal weight assigned to X is exactly W% of its
normal evidential weight`; only the number changes, so prohibition and
attenuation are worded the same. Cells are the pre-post gap.

| model | w=0 | w=0.01 | w=0.025 | w=0.05 | w=0.1 | w=0.25 | w=0.5 | w=0.75 | w=1 | gap(0) - mean gap(w>0) |
|---|---|---|---|---|---|---|---|---|---|---|
| Qwen3-8B | **+0.33** | +0.01 | +0.01 | +0.02 | -0.03 | -0.03 | -0.05 | -0.05 | -0.14 | **+0.362** |
| Gemma-3-12B | **+0.34** | +0.04 | -0.05 | -0.02 | -0.08 | -0.07 | +0.13 | +0.03 | -0.06 | **+0.354** |
| Mistral-24B | **+0.08** | +0.04 | +0.04 | +0.12 | +0.04 | +0.06 | +0.02 | -0.02 | +0.01 | **+0.045** |
| Qwen3.5-27B | **+0.28** | +0.05 | +0.10 | +0.12 | +0.07 | +0.18 | +0.09 | +0.07 | -0.03 | **+0.197** |
| Qwen3-32B | **+0.32** | +0.19 | +0.12 | +0.07 | +0.12 | +0.06 | +0.08 | -0.01 | +0.09 | **+0.229** |
| Phi-4-mini | **+0.26** | +0.05 | +0.13 | +0.25 | -0.06 | +0.06 | +0.10 | +0.05 | +0.15 | **+0.165** |

The gap is largest at exactly zero in all six models, and the excess over the
non-zero levels is large in five of six (Mistral-24B is near its floor
throughout). On Qwen3-8B the ratio is `gap(0)/gap(1%) = +0.331 / +0.009`, a
factor of 38.

The sharpest reading is within a column rather than across: **retrospectively a
model treats "exactly 0" as categorical** (Qwen3-8B REI +0.181 at w=0 versus
+0.422 at w=1%), **while prospectively it does not** (+0.511 versus +0.430 —
almost the same). Zero registers as special only once the object exists.

A caveat worth stating: fitting `REI ~ w + Before + w:Before + I[w=0]:Before`,
the extra kink term `I[w=0] x Before` is clearly positive on Qwen3-8B (+0.105,
p=0.016) and Qwen3.5-27B (+0.207, p=0.006), not identified on Gemma-3-12B,
Qwen3-32B and Phi-4-mini, and negative on Mistral-24B (-0.118, p=0.019). The
descriptive pattern is uniform; the formal discontinuity term is not.

A second, position-independent result falls out: between w=1% and w=50% the
effective weight barely moves at all (Qwen3-8B: +0.43, +0.45, +0.47, +0.47,
+0.46, +0.48). Models do not implement fractional evidence weights; they land
near one half whatever is asked.

### It is not prospective-memory decay

Stage 2 varied rule-to-answer distance. This varies rule-to-**evidence**
distance — how long the rule must be held before its target appears. Cells are
the pre-post gap.

| model | 0 tok | ~100 tok | ~300 tok | ~1000 tok |
|---|---|---|---|---|
| Qwen3-8B | +0.342 | +0.331 | +0.275 | +0.303 |
| Gemma-3-12B | +0.351 | +0.016 | -0.032 | -0.062 |
| Mistral-24B | +0.108 | +0.102 | +0.129 | +0.023 |
| Qwen3.5-27B | +0.258 | +0.280 | +0.205 | +0.217 |
| Qwen3-32B | +0.318 | +0.280 | +0.113 | +0.222 |
| Phi-4-mini | +0.245 | +0.233 | +0.155 | +0.126 |

Four of six models keep the gap essentially intact out to a thousand tokens of
delay between the rule and the evidence it governs. Gemma-3-12B is the clear
exception — its gap collapses from +0.35 to -0.06 — so a maintenance component
exists for some models and cannot be dismissed in general. But for most, the
failure is already at full strength when the rule sits immediately before its
target, which is not what decay predicts.

### Announcing the object in advance makes it worse

Identical rule (`Evidence E7 has decision weight 0.`) at every level; what
changes is how much of E7 exists when the rule is stated.

| model | L0 never mentioned | L1 'you will receive E7' | L2 [content pending] | L3 + type | L4 + type & direction | L5 full content first |
|---|---|---|---|---|---|---|
| Qwen3-8B | +0.561 | +0.754 | +0.848 | +0.804 | +0.754 | +0.329 |
| Gemma-3-12B | +0.836 | +0.921 | +0.923 | +0.918 | +0.912 | +0.596 |
| Mistral-24B | -0.046 | +0.327 | +0.906 | +0.829 | +0.757 | +0.041 |
| Qwen3.5-27B | +0.041 | +0.043 | +0.473 | +0.480 | +0.346 | -0.206 |
| Qwen3-32B | +0.481 | +0.701 | +0.844 | +0.865 | +0.797 | -0.007 |
| Phi-4-mini | +0.778 | +0.948 | +0.995 | +0.855 | +0.864 | +0.184 |

This is uniform across all six models and it inverts the obvious prediction.
Giving the rule a named placeholder to attach to does not help; it makes
suppression *worse* than never mentioning the object at all, and adding the item
type or even its direction does not recover. Only L5 — the content actually
present before the rule — is reliably good. Whatever the model needs in order to
route evidence to zero, a referent is not enough; it appears to need the content.

### A class policy carried on the evidence itself does work

| model | specific `E7 has weight 0` (pre / post) | class `any unauthorised item has weight 0` (pre / post) |
|---|---|---|
| Qwen3-8B | +0.561 / +0.329 | **+0.100** / +0.145 |
| Gemma-3-12B | +0.836 / +0.596 | **+0.532** / +0.328 |
| Mistral-24B | -0.046 / +0.041 | **-0.077** / -0.108 |
| Qwen3.5-27B | +0.041 / -0.206 | **-0.262** / -0.297 |
| Qwen3-32B | +0.481 / -0.007 | **+0.113** / -0.153 |
| Phi-4-mini | +0.778 / +0.184 | **+0.557** / +0.240 |

The class-wide policy applies to a tag printed on the evidence block itself, so
it can be resolved where the evidence is rather than held as a pending intention
about an identifier. It beats the item-specific rule prospectively in five of six
models, and on Qwen3-8B it also removes the position effect (+0.100 pre versus
+0.145 post). This is the same shape as the ledger result and points the fix in
the same direction.

Task preview does not help: telling the model the final question before the rule
makes Qwen3-8B *worse* (+0.642 with preview versus +0.511 without, p=0.007). The
missing binding target is not the objective.

### It is not one sentence

Eight hand-written ruling wordings, frozen before running, each with a matched
admit form so the leverage anchor sits in the same register. Mean pre-post gap
across five models:

| wording | construction | mean gap | models with gap > 0 |
|---|---|---|---|
| `pp1` | legal formal | +0.262 | 5/5 |
| `pp2` | plain | +0.401 | 5/5 |
| `pp3` | causal | +0.393 | 5/5 |
| `pp4` | counterfactual | +0.536 | 5/5 |
| `pp5` | weighting | +0.422 | 5/5 |
| `pp6` | policy | +0.340 | 5/5 |
| `pp7` | relevance | +0.411 | 5/5 |
| `pp8` | procedural | +0.282 | 5/5 |

Every construction type, in every model: 40 of 40 model x wording cells have a
positive gap. The counterfactual phrasing (`decide exactly as you would if X had
never appeared`) is the *worst* prospectively, not the best.

## Stage 3B — a tagged evidence stream is routed correctly

48 new numeric items with 2/4/8/16 reports, half tagged `[verified]` and half
`[unverified]`, and a routing policy stated either before or after the stream.
Ground truth is exact, so the answer can be regressed on both group means:
`Y ~ a + b*mean_admitted + c*mean_excluded`, where `c` is leakage.

| model | naive (no policy) | policy BEFORE the stream | policy AFTER |
|---|---|---|---|
| qwen3-8b | +0.480 | -0.174 | +0.004 |
| gemma3-12b | +0.475 | -0.014 | -0.019 |
| mistral-small-24b | +0.536 | +0.001 | +0.001 |
| phi4-mini | +0.496 | +0.016 | +0.003 |
| qwen3.5-9b | +0.406 | -0.000 | -0.001 |

With no policy the models average the whole stream, leaking about 0.48 of the
excluded mean. With the policy, leakage goes to roughly zero **in both arms**.
A policy that is resolved against a tag travelling with each report is executed
prospectively; a rule about a named future object is not. This is the same
dissociation as the class-policy result above, and it is what makes the fix
practical: the agent case (policy fixed before retrieval) is the *solvable* one,
provided the policy attaches to provenance rather than to an identifier.

One caveat: Qwen3-8B is unstable prospectively at the longest streams (N=16,
mean absolute error 7.6 against 0.3 retrospectively), so stream length is worth
pushing further than 16.


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
median over items). This is a correlate of the asymmetry, not an explanation of
it — the diffusion result rules out the architectural reading, and the remaining
accounts (H-A/H-B/H-C above) all predict something like it:

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

Open items, in the order they are worth doing: ruling paraphrases (a single
wording is now the biggest exposure, given that the headline is about rule
position); 20-30 independent legal skeletons, and either rewriting or dropping
the `procedural_hearsay` arm; two small naturalistic human-materials sets as
external validation; then the bidirectional patching below. Specifically: five
conditions on a naturalistic legal corpus rather than authored
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
