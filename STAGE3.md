# Stage 3 — naming the phenomenon

Stage 2 left three accounts standing for the Pre/Post asymmetry: decision
proximity (H-A), prospective binding (H-B) and linguistic scope (H-C), and showed
the effect only at a requested weight of zero. But the Stage-2 `w=0` rule was
also the only *prohibition* in its family, so "exact zero is special" and
"suppressive semantics are special" were confounded; and generic prospective
binding is too broad, since a model that can apply `w=0.25` to future evidence
can evidently bind a rule to an object that does not exist yet.

Stage 3A runs seven experiments on the frozen 144 items. Full tables in
`results/stage3_tables.md`, `results/stage3_pooled.md`, `results/routing_tables.md`.

## A. Zero is a discontinuity, not the end of a curve

One identical sentence at every level — *"The causal weight assigned to X is
exactly w% of its normal evidential weight"* — so prohibition and attenuation are
worded the same way. Pre-minus-post gap by requested weight:

| model | w=0 | 0.01 | 0.025 | 0.05 | 0.10 | 0.25 | 0.50 | 0.75 | 1.00 |
|---|---|---|---|---|---|---|---|---|---|
| Qwen3-8B | **+0.331** | +0.009 | +0.012 | +0.023 | -0.030 | -0.025 | -0.053 | -0.048 | -0.135 |
| Gemma-3-12B | **+0.343** | +0.035 | -0.053 | -0.016 | -0.080 | -0.070 | +0.126 | +0.032 | -0.063 |
| Phi-4-mini | **+0.256** | +0.047 | +0.133 | +0.247 | -0.064 | +0.056 | +0.104 | +0.053 | +0.152 |

Headline test, per item, pooled over models with a cluster bootstrap over
(model x case skeleton):

> (gap at w=0) − (mean gap over the eight non-zero weights)
> = **+0.295 [+0.185, +0.405], p < 1e-4** (n = 422 item-model pairs)

In the pooled regression `REI ~ w + Before + w:Before + I[w=0]:Before` with model
fixed effects, the discontinuity term is **+0.096 [+0.034, +0.160], p = 0.005**.
Per model it is positive in all three but reaches significance only in Qwen3-8B
(p = 0.016; Gemma p = 0.12, Phi p = 0.12) — the per-model design is underpowered
for an interaction, which is why the pooled contrast is the headline.

**An honest caveat that sharpens rather than weakens this.** Between w = 0.01 and
w = 0.5 the effective weight is flat at roughly 0.43–0.53 in *both* arms: the
models are not implementing those attenuations at all. So "no position effect
there" partly reflects "no instruction effect there". The defensible statement is
narrower and more interesting:

> The only requested weights these models actually implement are 1 and 0, and
> they implement 0 only retrospectively. Prospectively, "exactly 0%" suppresses
> no more than "1%" (Qwen3-8B: +0.511 vs +0.430).

## B. It is not prospective-memory decay

Filler inserted between the rule and the evidence it governs — Stage 2 only moved
the rule away from the *answer*, this moves it away from its *target*:

| model | arm | 0 tok | ~100 | ~300 | ~1000 |
|---|---|---|---|---|---|
| Qwen3-8B | rule BEFORE | +0.517 | +0.471 | +0.487 | +0.583 |
| | rule AFTER | +0.175 | +0.139 | +0.212 | +0.280 |
| Gemma-3-12B | rule BEFORE | +0.436 | +0.325 | +0.364 | +0.327 |
| | rule AFTER | +0.085 | +0.309 | +0.396 | +0.389 |
| Phi-4-mini | rule BEFORE | +0.635 | +0.689 | +0.665 | +0.643 |
| | rule AFTER | +0.390 | +0.456 | +0.510 | +0.517 |

**Prospective suppression is flat in delay in all three models.** It fails at full
size when the rule sits immediately against the evidence, and is no worse a
thousand tokens earlier. Retrospective suppression is the arm that decays with
distance from its target — for Gemma-3-12B it collapses entirely by 100 tokens.
The asymmetry narrows with delay only because the good arm degrades, never
because the failing arm improves. Whatever this is, it is not a maintenance or
recall failure.

## C. Partially specifying the future object makes it worse

Identical rule (`Evidence E7 has decision weight 0.`) at every level; only how
much of E7 exists when the rule is stated changes.

| level | Qwen3-8B | Gemma-3-12B | Phi-4-mini |
|---|---|---|---|
| L0 E7 never mentioned before the rule | +0.561 | +0.836 | +0.778 |
| L1 "you will later receive Evidence E7" | +0.754 | +0.921 | +0.948 |
| L2 `[E7: content pending]` | +0.848 | +0.923 | +0.995 |
| L3 + item type | +0.804 | +0.918 | +0.855 |
| L4 + type and direction | +0.754 | +0.912 | +0.864 |
| L5 full content **before** the rule | **+0.329** | **+0.596** | **+0.184** |

The ladder does not interpolate; every partial stub is *worse* than no stub, in
all three models, and only the full content ahead of the rule helps. Announcing a
future object and describing it does not create anything the rule can attach to.

## D. Non-multiplicative transforms

| transform | Qwen3-8B pre / post / gap |
|---|---|
| sign flip (target −1.0) | +0.636 / +0.496 / **+0.140** p=0.009 |
| cap contribution | +0.361 / +0.222 / **+0.139** p<1e-4 |

Both show a real but roughly half-size gap. So the effect is *largest* at exact
zero, not confined to it; "only w=0" would be an overstatement.

## E. The declarative policy is perfect while the causal one fails

A separate call on the same context asks what weight the item should get. The
decision run never sees this question.

| model | arm | says weight | says exactly 0 | REI in the decision run |
|---|---|---:|---:|---|
| Qwen3-8B | rule BEFORE | 0.00% | **100.0%** | **+0.511** |
| | rule AFTER | 0.00% | 100.0% | +0.181 |
| Gemma-3-12B | rule BEFORE | 0.00% | **100.0%** | **+0.419** |
| | rule AFTER | 0.00% | 100.0% | +0.076 |
| Phi-4-mini | rule BEFORE | 0.00% | **100.0%** | **+0.644** |
| | rule AFTER | 0.00% | 100.0% | +0.387 |

Every model, every item, both arms: asked immediately after the evidence arrives,
the model states the weight is exactly zero — and then gives the item half its
force. This closes off the reading that the latent rule was simply not retrieved
when its trigger appeared. The rule is retrieved, correctly bound to the right
item, and correctly reported; it does not control the decision.

## F. A class predicate works prospectively where an item reference does not

| rule | Qwen3-8B | Gemma-3-12B | Phi-4-mini |
|---|---|---|---|
| specific `E7 has weight 0`, rule first | +0.561 | +0.836 | +0.778 |
| specific, rule last | +0.329 | +0.596 | +0.184 |
| class `any item marked unauthorised has weight 0`, rule first | **+0.100** | +0.532 | +0.557 |
| class, rule last | +0.145 | +0.328 | +0.240 |

The class rule differs in one respect: its criterion travels *with* the evidence,
as a tag on the block, so the routing decision is re-made locally at arrival
rather than held as a reference to a named future object.

## G. Task preview does not rescue it

Previewing the final question at the top of the file does not help and slightly
hurts (Qwen3-8B: +0.511 → +0.642; rescue −0.131, p = 0.007). The missing binding
target is not the objective.

## Stage 3B — selective routing over a tagged stream

48 numeric items, N ∈ {2,4,8,16} reports, half tagged `[verified]` and half
`[unverified]`, with an exact ground truth. Regressing the answer on both group
means, `Y ~ a + b·mean_admitted + c·mean_excluded`:

| condition | Qwen3-8B b / c / err | Mistral-24B b / c / err |
|---|---|---|
| oracle (only admitted shown) | 0.998 / +0.003 / 0.4 | 1.002 / +0.001 / 0.2 |
| naive (all reports, no policy) | 0.526 / **+0.480** / 21.1 | 0.456 / **+0.536** / 22.4 |
| policy BEFORE the reports | 0.774 / −0.174 / 7.6 | 1.002 / +0.001 / 0.1 |
| policy AFTER the reports | 0.996 / +0.004 / 0.3 | 1.002 / +0.001 / 0.2 |

The leakage channel is wide open — without a policy the excluded group gets
c ≈ 0.5 — yet a tag-based policy stated **in advance** closes it almost
completely. Mistral is exact in both orders. Qwen3-8B is exact up to N = 8 and
becomes unstable at N = 16 in the prospective arm (mean error 7.6 vs 0.3), which
looks like instability rather than systematic leakage.

## Where this leaves the account

* **Not decay** (B), **not recall** (E), **not the objective** (G), **not
  distance** (Stage 2), **not mainly anaphora** (Stage 2).
* **Not generic prospective binding either.** A policy whose criterion arrives
  attached to the evidence is executed prospectively and correctly (F, 3B), and
  non-zero prospective weights show no positional effect at all (A).
* What fails is narrower: **a prospective rule that must hold a reference to a
  specific future item, and that demands that item's causal weight be exactly
  zero.** Announcing and describing the item in advance does not help (C); only
  the item's actual content, present before the rule, does (C-L5, and the whole
  Pre/Post contrast).

The working name is the **prospective nullification gap**: models can
prospectively remember a future rule, state it correctly at the moment its target
arrives, and prospectively apply non-zero weights and class-level routing — yet
cannot prospectively assign zero causal weight to a specific item they have not
yet seen.
