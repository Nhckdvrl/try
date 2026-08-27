# Stage 3C — attacking the narrow claim

Five models (Qwen3-8B, Gemma-3-12B, Phi-4-mini, Mistral-Small-24B, Qwen3.5-27B)
on the frozen 144 items, plus a new 48-item verifiable task. Two of these results
overturn readings in `STAGE3.md`; both corrections are marked there.

## P0-1 Inclusion implicature (H-D) — rejected

The competing account: presenting an item at all signals it is relevant, and
`w=0` is the only condition where presentation and stated weight contradict each
other. That would explain the zero discontinuity, the ladder, and the class-policy
result at once. Neutralised with a presentation policy at the top of the file
that never mentions the item, exclusion, or zero.

| model | none | auto-display | audit | relevance-positive | audit rescue (prospective) |
|---|---|---|---|---|---|
| Qwen3-8B | +0.299 | +0.137 | +0.265 | +0.245 | +0.089 [-0.019, +0.191] p=0.10 |
| Gemma-3-12B | +0.277 | +0.236 | +0.233 | +0.309 | -0.033 [-0.151, +0.074] p=0.54 |
| Phi-4-mini | +0.330 | +0.264 | +0.226 | +0.234 | +0.095 [-0.090, +0.280] p=0.33 |
| Mistral-24B | +0.090 | -0.027 | +0.045 | +0.123 | +0.131 [-0.023, +0.299] p=0.11 |
| Qwen3.5-27B | +0.177 | +0.196 | +0.080 | +0.173 | +0.145 [-0.006, +0.299] p=0.06 |

Telling the model in as many words that display does not imply relevance does not
rescue the prospective arm in any model. And the relevance-*positive* control,
which should make the implicature worse, produces gaps as large as or larger than
the no-policy baseline in four of five. H-D does not explain the effect.

## P0-2 A task where intermediate weights are implementable — the discontinuity disappears

The near-zero sweep's weakness: between w=0.01 and w=0.5 the models give roughly
the same effective weight, so they are not implementing those attenuations at all.
New task, exact answer `base + w·delta`, screened on whether the model tracks
w at 0.25/0.5/0.75 retrospectively before w=0 is looked at.

| model | items tracking w | w=0, rule BEFORE | w=0, rule AFTER | pre − post |
|---|---:|---|---|---|
| Qwen3-8B | 13/48 | +0.000 | +0.000 | **+0.000** |
| Gemma-3-12B | 34/48 | +0.000 | +0.000 | **+0.000** |
| Mistral-24B | 29/48 | +0.000 | +0.000 | **+0.000** |
| Qwen3.5-27B | 48/48 | +0.000 | +0.000 | **+0.000** |
| Phi-4-mini | 16/48 | +0.000 | +0.438 | −0.438 (fails retrospectively) |

Qwen3.5-27B is exact at every weight in both arms. **When an item's contribution
is stated explicitly and arithmetically, prospective nullification is perfect.**

This is the single most informative result in Stage 3C. The prospective
nullification gap is not an abstract forward-reference failure and not a general
property of the value zero. It is specific to evidence whose contribution to the
judgment has to be *inferred* rather than read off:

> Explicit symbolic weighting succeeds prospectively; implicit semantic evidence
> nullification fails.

## P0-3 State externalisation — the declarative story needs qualifying, and then hardens

| model | decision only | model writes the weight first | weight forced to 0% |
|---|---|---|---|
| Qwen3-8B | +0.301 p<1e-4 | +0.129 p=0.020 | +0.077 p=0.20 |

What the model writes when the weight statement is a step in its own decision:

| model | stated weight, prospective | says exactly 0% | stated weight, retrospective | says exactly 0% |
|---|---:|---:|---:|---:|
| Qwen3-8B | 37.3% | 33% | 15.1% | 74% |
| Gemma-3-12B | 25.7% | 56% | 10.4% | 69% |
| Phi-4-mini | 9.5% | 77% | 8.8% | 81% |
| Mistral-24B | 14.9% | 85% | 17.4% | 79% |
| Qwen3.5-27B | 9.0% | 91% | 13.9% | 86% |

Asked as its own task the policy comes back perfectly (100% say 0%, Stage 3A E).
Asked as a step inside the decision it does not: on Qwen3-8B only a third of
prospective items state zero, against three quarters retrospectively. So the
declarative state is not simply intact-but-ignored; **it is itself degraded
inside the decision trajectory, and degraded more when the target did not exist
when the rule was read.**

The stronger test survives. Teacher-forcing `ITEM DECISION WEIGHT: 0%` into the
generation leaves REI_pre at +0.434 (against +0.485 unforced). Writing the correct
policy into the model's own output does not restore correct causal use.

## P0-4 Identity predicate vs arbitrary tag — the class-policy reading was wrong

Clean 2x2: both conditional, both locally checkable when the item arrives, tag
`Z9` semantically empty.

| model | `if ID is E7 -> weight 0` pre / post | `if tag is Z9 -> weight 0` pre / post |
|---|---|---|
| Qwen3-8B | +0.717 / +0.644 | +0.704 / +0.550 |
| Gemma-3-12B | +0.789 / +0.840 | +0.720 / +0.881 |
| Phi-4-mini | +0.765 / +0.573 | +0.689 / +0.749 |
| Mistral-24B | +0.073 / +0.412 | +0.086 / +0.391 |
| Qwen3.5-27B | −0.264 / −0.143 | −0.376 / −0.124 |

A semantically empty tag predicate leaks exactly as badly as an identity
predicate. Stage 3A's class-policy advantage came from the *meaning* of
"unauthorised", not from class-vs-item or from local checkability. Note also that
the conditional `if ... then weight 0` framing is a much weaker instruction than a
plain assertion in the three smaller models (leakage ~0.7 against ~0.5).

## P1-7 Salience control — the ladder is only partly salience

The same preview stubs with no rule at all:

| model | L0 | L1 | L2 | L3 | L4 |
|---|---|---|---|---|---|
| Qwen3-8B | +0.704 | +0.700 | +0.749 | +0.763 | +0.732 |
| Gemma-3-12B | +0.717 | +0.698 | +0.734 | +0.794 | +0.799 |
| Phi-4-mini | +0.761 | +0.906 | +0.768 | +0.893 | +0.881 |
| Mistral-24B | +0.842 | +0.841 | +0.825 | +0.905 | +0.862 |
| Qwen3.5-27B | +0.837 | +0.726 | +0.723 | +0.763 | +0.722 |

Previewing an item does raise its weight with no rule present, by about +0.05 on
average — against the +0.29 rise the same previews produce under an exclusion
rule. Salience is a real but minor contributor; it does not account for the
ladder.

## P1-8 Occurrence vs content binding — the sharpest result

`E → rule → E again`: the full content is present when the rule is stated, and
the evidence the decision reads still appears after the rule.

| model | E → rule → E | rule-first | rule-last |
|---|---|---|---|
| Qwen3-8B | **+0.148** | +0.485 | +0.184 |
| Gemma-3-12B | +0.231 | +0.447 | +0.154 |
| Phi-4-mini | +0.487 | +0.623 | +0.206 |
| Mistral-24B | **−0.079** | +0.078 | +0.005 |
| Qwen3.5-27B | **−0.312** | −0.054 | −0.267 |

In four of five models a preview of the content restores retrospective-level
suppression, or better. **What matters is whether the content existed when the
rule was read, not where the evidence the decision reads sits.** The rule binds to
content, not to an occurrence.

## Where the account stands after Stage 3C

Killed: causal masking (diffusion), distance (Stage 2), directional anaphora
(Stage 2, largely), prospective-memory decay (3A-B), the objective (3A-G),
inclusion implicature (3C-P0-1), class-vs-item structure (3C-P0-4), salience
(3C-P1-7, mostly).

What is left is narrow and now has a positive characterisation rather than a list
of negations:

> To make an item causally inert, these models appear to need a representation of
> **what** they are suppressing at the time the policy is bound. Given the
> content — retrospectively, or as a preview before the rule (P1-8) — suppression
> works. Given only a reference to a future item, it does not, no matter how the
> reference is phrased (paraphrases), how close the rule sits to its target (3A-B),
> whether the reference is an identity or a predicate (P0-4), or whether the model
> is told the display is not a relevance signal (P0-1). And the whole phenomenon
> vanishes when the item's contribution is arithmetic rather than semantic
> (P0-2) — precisely the case where no content representation is needed to know
> what zero weight means.
