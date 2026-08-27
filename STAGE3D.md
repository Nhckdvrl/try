# Stage 3D — semantic addressability, and the on-policy test

Two questions left over from Stage 3C:

1. P1-8 showed a preview of the evidence before the rule restores suppression —
   but the preview was the *same string*, so it could not separate "the rule needs
   a representation of its target" from "the rule only suppresses text it has
   already seen verbatim".
2. The teacher-forced `0%` result could be an off-policy artefact.

## A design error, found and fixed before reporting

The first version of the similarity ladder was built on the bare identity rule
`Evidence E7 has decision weight 0`. Stage 3C P0-4 had already shown that form to
be a weak instruction, and with it REI with no preview was **+0.861** — almost no
suppression left to rescue. Every preview then made things *worse* (REI up to
+1.18) because a second copy of the evidence adds salience. The ladder was rebuilt
on the assertive form used in P1-8 (`The causal weight assigned to <the recorded
phone call> is exactly 0% of its normal evidential weight`), which gives REI
+0.57 with no preview and leaves real room to rescue. Only the rebuilt version is
reported.

## Similarity ladder

`preview(E') → rule(weight 0%) → EVIDENCE (fixed) → judgment`. Only the preview
changes. Rescue = REI(no preview) − REI(with preview); positive means the preview
let the rule bind. `*` marks p < 0.05, cluster bootstrap over case skeletons.

| preview placed before the rule | Qwen3-8B | Gemma-3-12B | Phi-4-mini | Qwen3.5-27B |
|---|---|---|---|---|
| exact same text | **+0.323\*** | +0.124 | +0.143 | **+0.541\*** |
| lexical paraphrase, same proposition | **+0.310\*** | +0.108 | **+0.217\*** | **+0.540\*** |
| entailing summary, no verbatim content | −0.035 | −0.243\* | −0.077 | +0.214\* |
| different fact, same entity and direction | −0.270\* | −0.534\* | −0.271\* | −0.330\* |
| high lexical overlap, different meaning | +0.057 | −0.177\* | +0.078 | −0.064 |
| same case, unrelated procedural fact | −0.047 | −0.069\* | +0.025 | +0.211\* |
| unrelated fact | +0.016 | +0.014 | +0.006 | +0.123 |

The ordering `exact ≈ paraphrase > summary ≈ 0 > same-direction-different-fact`
holds in all four models. Three things follow, and one does not:

* **Not string matching.** A reworded preview rescues as much as the identical
  text (0.323 vs 0.310; 0.541 vs 0.540), while a preview with high lexical overlap
  and a different meaning rescues nothing anywhere.
* **Not topic or direction priming.** Same case, same entity, same direction but a
  different fact does not rescue — it makes leakage significantly *worse* in all
  four models.
* **The gist is not enough.** An entailing summary that keeps the proposition but
  drops the specific content fails to rescue in three of four models.
* **Caveat.** The positive rungs reach individual significance in only two of four
  models; Gemma-3-12B's exact/paraphrase rescues are +0.124/+0.108, n.s. The
  *pattern* is uniform, the per-model effect sizes are not.

## Content × identity — the clean 2×2

Preview is always the original evidence. The rule always names `E7`. The item the
decision reads varies independently in content and in label.

| preview content matches | label matches the rule | Qwen3-8B | Gemma-3-12B | Phi-4-mini | Qwen3.5-27B |
|---|---|---|---|---|---|
| yes | yes (E7) | **+0.480** | **+0.492** | **+0.505** | **−0.463** |
| yes | no (E9) | +0.637 | +0.669 | +0.533 | +0.068 |
| no | yes (E7) | +0.739 | +0.856 | +0.839 | +0.490 |
| no | no (E9) | +0.920 | +0.944 | +0.882 | +0.961 |

The ordering is identical in every model, and the decisive cell comparison is the
middle pair:

> **Matching content under the wrong label suppresses better than the right label
> with the wrong content** — +0.637 vs +0.739, +0.669 vs +0.856, +0.533 vs +0.839,
> +0.068 vs +0.490.

Content is the larger factor in all four (main effect 0.26 / 0.36 / 0.33 / 0.95
against 0.16 / 0.11 / 0.04 / 0.53 for the label). Behaviourally, exclusion is
**content-addressed more than identifier-addressed**, with the identifier making a
smaller separate contribution.

## On-policy state externalisation

16 samples per item at T=0.8; trajectories split by what the model wrote on its
own `ITEM DECISION WEIGHT` line. This answers the objection that teacher-forcing a
reasoning step pushes the model off-policy.

| model | arm | trajectories stating 0% | REI when it stated 0% | REI when it stated >0% |
|---|---|---:|---|---|
| Qwen3-8B | rule BEFORE | 31% | **+0.225 [+0.028, +0.455]** | +0.506 |
| Qwen3-8B | rule AFTER | 72% | +0.100 [−0.082, +0.296] | +0.685 |
| Gemma-3-12B | rule BEFORE | 55% | **+0.592 [+0.361, +0.831]** | +0.742 |
| Gemma-3-12B | rule AFTER | 66% | +0.059 [−0.117, +0.254] | +0.475 |
| Phi-4-mini | rule BEFORE | 54% | +0.022 [−0.423, +0.473] | +0.495 |
| Phi-4-mini | rule AFTER | 57% | −0.035 [−0.434, +0.362] | +0.251 |

In Qwen3-8B and Gemma-3-12B the claim survives on-policy: restricted to
trajectories where the model spontaneously wrote that the item carries zero
weight, the prospective arm still leaks (CIs exclude zero) while the retrospective
arm does not. The asymmetry itself survives conditioning on the stated policy.

**It does not survive in Phi-4-mini**, where stating zero is enough — its leakage
is entirely mediated by whether the policy gets written. So "states the correct
policy and uses the evidence anyway" is a property of some models, not all, and
should be reported that way.

The rate of stating zero is itself position-dependent in every model (31% vs 72%,
55% vs 66%, 54% vs 57%), consistent with Stage 3C P0-3: the declarative state
degrades inside the decision trajectory, and degrades more prospectively.

## Where this leaves the account

The positive characterisation from Stage 3C now has direct evidence:

> To make a future item causally inert, these models need a representation of its
> **specific propositional content** at the time the rule is read. Wording is
> irrelevant — a paraphrase works as well as the exact text. Topical and
> directional overlap are not enough, and neither is lexical overlap. A gist-level
> summary is generally not enough either. And what the suppression attaches to is
> the content rather than the symbolic label the rule names.

Open: Mistral-Small-24B is still running for both experiments. The next steps are
the future-denylist / system→tool setting, and same-chronology bidirectional
patching using the now-available success/failure pair
(`rule → E` vs `preview(E) → rule → E`), where the evidence the decision reads
sits after the rule on both sides.
