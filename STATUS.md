# Project status — post-novelty reset ledger

**As of:** 2026-09-04.
**Target:** ARR 2026-10-12 → NAACL 2027.

The broad phenomenon, G18 diagnostic, agent transfer, and two-model mechanism are
complete. The previous ReGround G19 method design was **cancelled before generation**
after a novelty audit. No G19 output exists.

The active scientific reset is documented in:
- [NOVELTY_RESET_2026-09-04.md](NOVELTY_RESET_2026-09-04.md)
- [NEXT_EXPERIMENTS_POST_RESET.md](NEXT_EXPERIMENTS_POST_RESET.md)

Historical stage documents and preregistrations remain unchanged as provenance.

## 1. Stable empirical core

| # | Finding | Load-bearing evidence | Breadth | Status |
|---|---|---|---|---|
| 1 | **Prospective exclusion is systematically harder than post-evidence exclusion.** | G0: same exclusion rule before vs after evidence; matched Admit control has no analogous order effect. Delta_time has the same sign in all 12 instruct models, with 10/12 intervals excluding zero. | 12 instruct + 2 masked diffusion LMs, 4 vendors, 5 task families, 144 frozen items | **established** |
| 2 | **Explicit policy access is not sufficient for enforcement in at least some models.** | Separate policy probes recover zero weight; on-policy and teacher-forced state externalisation show that Qwen3-8B and Gemma-3-12B can explicitly state zero while prospective evidence still influences the decision. Phi-4-mini does not show the same dissociation. | 3-model on-policy test + broader declarative probe | **established, heterogeneous** |
| 3 | **The failure is not a generic inability to execute future numeric rules.** | Requested-weight characterization; exact arithmetic contribution task yields zero pre/post gap in 4/5 models at weight zero; non-multiplicative transforms retain smaller gaps. | 3–6 models depending on test | **boundary condition** |
| 4 | **Target semantics change prospective exclusion, but this is now a diagnostic rather than the paper's headline novelty.** | G18: Delta_semantic = **+8.91 [+7.15,+10.76] rating points**, positive in 5/5 models; para-minus-empty = **+12.85 [+10.32,+15.42]**. | 100 fresh items, 30 fresh skeletons, 3 families, 5 models / 4 vendors; 9,000 generations | **prospectively confirmed diagnostic** |
| 5 | **Suppression can follow semantic content across identifier changes.** | Stage 4 SYSTEM→TOOL counterfactual: ID-specific protection does not follow D7→D9, while proposition-targeted suppression does. | 4 models | **established; interpretation under reset** |
| 6 | **A target-dependent rule state causally carries successful vs failed prospective exclusion.** | Matched-chronology rule-span interchange changes later suppression before the later evidence is processed. Qwen3-8B: L14–18/36; Mistral-Small-24B: L12–16/40. | 2 architectures | **causal mechanism established** |

## 2. Why the old central story was retired

The post-G18 narrative had become:

> semantic target information makes the rule easier to apply.

Although empirically supported, this is too normal as a scientific headline. It is too
close to prompt specificity / identify-then-ignore / richer target specification.

The paper should not claim novelty from:
- "semantic information helps";
- "specific targets are easier than arbitrary IDs";
- "restating/grounding a policy after retrieval helps".

Those observations can remain supporting evidence.

## 3. G18 — retained, but reinterpreted

G18 remains important because it cleanly manipulates what target representation is
available before the rule and nets out preview redundancy.

Pooled ExclusionEffect:
- entail **31.16 [27.99,34.40]**
- paraphrase **30.93 [28.19,33.66]**
- identifier 26.27 [23.65,28.96]
- unrelated 22.06 [19.16,24.97]
- none 21.84 [19.21,24.66]
- lexical-overlap / wrong proposition 18.08 [15.71,20.57]

Primary frozen contrast:
- Delta_semantic **+8.91 [+7.15,+10.76]**, 5/5 positive.

The key clue for the reset is the decomposition:
- under paraphrase, marg(no-rule) is only about **+3** points;
- with exclusion, marg(exclude) becomes about **−28** points.

Thus successful semantic binding can push the judgment below the preview-only baseline.
This is no longer framed merely as a strong rescue. It motivates the hypothesis that
exclusion may lose occurrence/source precision and spread to the proposition itself.

## 4. Active hypotheses

### H1 — Binding Deadline

> **A prospective control rule may be effectively compiled against the target
> representation available when the rule is processed. A target revealed later—even
> before the actual evidence—may not reliably retroactively bind the earlier rule.**

Critical new experiment: G20 Late Target Revelation.

The decisive pattern would be:
- target-before-rule > target-after-rule;
- replaying the identical rule after late target revelation selectively restores
  exclusion;
- matched Admit/arithmetic controls do not show the same failure;
- at least one masked-diffusion model preserves the effect, ruling out a purely
  left-to-right architectural explanation.

### H2 — Semantic Scope Collapse

> **When semantic binding succeeds, exclusion may spread beyond the intended
> evidence source/occurrence and suppress independently admissible evidence expressing
> the same proposition.**

Critical new experiment: G21 Source-Scope Collapse.

The decisive pattern would be:
- Source A is successfully excluded;
- Source B independently contributes when alone;
- B loses contribution when it expresses the same proposition as excluded A;
- lexical overlap without proposition identity does not cause the loss;
- an explicit statement that B remains admissible does not fully restore it.

## 5. Candidate higher-level story

The strongest prospective paper would no longer be "target addressability".

It would be:

> **LLMs struggle to bind future control rules both effectively and precisely.**
>
> When the target is unresolved at rule time, the rule under-binds and later evidence
> leaks. When a semantic target is available, suppression can become strong enough to
> over-bind, potentially collapsing a source/occurrence-scoped policy into
> proposition-level suppression.

This is an **under-binding / over-binding** account with two independent axes:
1. binding strength;
2. scope precision.

## 6. Existing mechanism under the new story

Licensed:
- excluded evidence is still causally read when prospective suppression fails;
- a target-dependent rule state forms in the middle of the network before later
  evidence is processed;
- interchanging that state changes later suppression in Qwen3-8B and
  Mistral-Small-24B;
- the shared state is item-specific on current evidence; a universal steering
  direction was not found.

Under the reset, Stage 5 supports the idea that **rule processing itself is the
critical computational event**. It does not yet prove a binding deadline or source
scope collapse; those require G20/G21.

## 7. Cancelled ReGround G19

The ReGround design is retained in:
- METHOD_REGROUND.md
- preregistrations/PREREGISTRATION_G19_REGROUND.md

Status:
- **cancelled before G19_FREEZE.md**
- **no model generations**
- **no result**

Reason:
the method "resolve the semantic policy after retrieval and compile matching document
IDs" is a sensible engineering mitigation but too obvious to serve as a novel fourth
contribution. Do not run or revive it in its current form.

## 8. Supporting characterization

Still useful, but not separate contributions:
- eight natural-language rule formulations;
- delay/distance tests;
- masked diffusion replication;
- Stage 3A/3D semantic ladders and content×identity 2×2;
- Stage 3E redundancy deconfounding and relation matrix;
- tagged provenance streams;
- G16 failed class-marker mechanism bridge;
- G17 failed frozen ratio estimand + posthoc raw-point pattern.

## 9. Programme status

**Open only for novelty-driven G20/G21 design and execution.**

Do not add:
- model-size sweeps;
- frontier API breadth;
- more semantic-preview ladders;
- generic reminder/restatement experiments;
- ReGround-v2;
- a third mechanism model before the new behavioral claim exists.

The next experiment must discover or kill a genuinely less-obvious computational
phenomenon.
