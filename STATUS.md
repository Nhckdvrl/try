# Project status — post-mainline-audit ledger

**As of:** 2026-09-04.
**Target:** ARR 2026-10-12 → NAACL 2027.

The broad phenomenon, G18 diagnostic, agent transfer, and two-model mechanism are
complete. The previous ReGround G19 method design was **cancelled before generation**.
A second mainline audit has now also **downgraded G21 Source–Proposition Scope
Entanglement from paper-center status** because it does not naturally explain the
original G0 prospective/retrospective reversal.

Read first:
- [MAINLINE_AUDIT_2026-09-04_V2.md](MAINLINE_AUDIT_2026-09-04_V2.md)
- [NOVELTY_RESET_2026-09-04.md](NOVELTY_RESET_2026-09-04.md)
- [NEXT_EXPERIMENTS_POST_RESET.md](NEXT_EXPERIMENTS_POST_RESET.md)

Historical stage documents and preregistrations remain unchanged as provenance.

## 1. Stable empirical core

| # | Finding | Load-bearing evidence | Breadth | Status |
|---|---|---|---|---|
| 1 | **Prospective exclusion is systematically harder than post-evidence exclusion.** | G0: same exclusion rule before vs after evidence; matched Admit control has no analogous order effect. Delta_time has the same sign in all 12 instruct models, with 10/12 intervals excluding zero. | 12 instruct + 2 masked diffusion LMs, 4 vendors, 5 task families, 144 frozen items | **established** |
| 2 | **Explicit policy access is not sufficient for enforcement in at least some models.** | Separate policy probes recover zero weight; on-policy and teacher-forced state externalisation show that Qwen3-8B and Gemma-3-12B can explicitly state zero while prospective evidence still influences the decision. Phi-4-mini does not show the same dissociation. | 3-model on-policy test + broader declarative probe | **established, heterogeneous** |
| 3 | **The failure is not a generic inability to execute future numeric rules.** | Requested-weight characterization; exact arithmetic contribution task yields zero pre/post gap in 4/5 models at weight zero; non-multiplicative transforms retain smaller gaps. | 3–6 models depending on test | **boundary condition** |
| 4 | **Pre-rule target semantics strongly alter prospective exclusion, but this is a factorization result rather than the final novelty.** | G18: Delta_semantic = **+8.91 [+7.15,+10.76] rating points**, positive in 5/5 models; para-minus-empty = **+12.85 [+10.32,+15.42]**. | 100 fresh items, 30 fresh skeletons, 3 families, 5 models / 4 vendors; 9,000 generations | **prospectively confirmed diagnostic** |
| 5 | **Effective suppression is substantially content-conditioned rather than purely identifier-conditioned.** | Stage 3D content×identity and Stage 4 D7→D9 counterfactuals. | 4 models | **established diagnostic** |
| 6 | **A target-dependent rule state causally carries successful vs failed prospective exclusion.** | Matched-chronology rule-span interchange changes later suppression before the later evidence is processed. Qwen3-8B: L14–18/36; Mistral-Small-24B: L12–16/40. | 2 architectures | **causal mechanism established** |

## 2. Current mainline hypothesis

The strongest unified account is now:

> **LLMs appear to construct a target-conditioned exclusion state when the exclusion
> rule is processed, rather than storing a deferred exclusion operator that is
> reliably composed with a target once that target becomes available later.**

Equivalent high-level formulation:

> **Prospective evidence exclusion is a non-commutative control-composition problem:
> target → EXCLUDE works substantially better than EXCLUDE → target.**

Why this is natural:

- G0 retrospective = target evidence → exclusion rule.
- G0 prospective = exclusion rule → target evidence.
- G18 preview rescue restores target semantics before the exclusion rule while keeping
  the actual decision evidence after the rule.
- Stage 5 finds the causal success/failure state around rule processing.
- arithmetic future weighting succeeds, so deferred composition is not generically
  impossible.

This remains a hypothesis until the redesigned G20 is run.

## 3. G18 — retained as factorization evidence

G18 remains important because it cleanly manipulates what target representation is
available **before the rule** and nets out preview redundancy.

Pooled ExclusionEffect:
- entail **31.16 [27.99,34.40]**
- paraphrase **30.93 [28.19,33.66]**
- identifier 26.27 [23.65,28.96]
- unrelated 22.06 [19.16,24.97]
- none 21.84 [19.21,24.66]
- lexical-overlap / wrong proposition 18.08 [15.71,20.57]

Primary frozen contrast:
- Delta_semantic **+8.91 [+7.15,+10.76]**, 5/5 positive.

The below-baseline paraphrase pattern remains a useful clue that successful control is
content-level rather than a clean deletion of one later occurrence, but it is **not**
being expanded into a source-scope paper.

## 4. Active novelty-bearing experiment

### G20 v3 — Deferred Control Composition / Non-Commutative Exclusion

First priority.

Core conditions:

```
TARGET-FIRST:
P → EXCLUDE → U → CHECKPOINT → EVIDENCE → QUESTION

RULE-FIRST:
U → EXCLUDE → P → CHECKPOINT → EVIDENCE → QUESTION
```

At the shared CHECKPOINT both arms have already seen the same target semantics, rule,
and neutral block. The scientific question is whether the earlier order still leaves a
different causal control state.

Load-bearing requirements:
- high late-target comprehension;
- TARGET-FIRST > RULE-FIRST exclusion;
- selective RULE-FIRST rescue when the exclusion rule is replayed after P;
- ideally rule replay > target replay;
- matched Admit/arithmetic/routing late composition works;
- post-resolution checkpoint interchange causally changes later suppression;
- replication beyond a single model family.

This is designed specifically to avoid the trivial decoder causal-mask claim.

## 5. G21 status

### Source–Proposition Scope Entanglement

**Downgraded / not authorized as the next paper-defining experiment.**

Reason:
it asks whether successful semantic exclusion preserves source scope. That may be
interesting, but it does not explain the G0 prospective/retrospective reversal.

Keep the design as:
- a possible future paper;
- a secondary consequence if later evidence demands it;
- repository provenance.

Do not allocate a main claim, main figure, or current experiment budget to it.

## 6. Existing mechanism under the new story

Licensed:
- excluded evidence is still causally read when prospective suppression fails;
- a target-dependent rule state forms in the middle of the network before later
  evidence is processed;
- interchanging that state changes later suppression in Qwen3-8B and
  Mistral-Small-24B;
- the shared state is item-specific on current evidence; a universal steering
  direction was not found.

The ideal next mechanism test is at a **post-resolution shared checkpoint**, not another
earlier rule-token localization.

If TARGET-FIRST and RULE-FIRST still differ causally after both target and rule are
available, that would establish history-dependent control composition rather than a
trivial inability of an earlier hidden state to see future tokens.

## 7. Cancelled ReGround G19

Status:
- **cancelled before G19_FREEZE.md**
- **no model generations**
- **no result**

Reason:
the method “resolve the semantic policy after retrieval and compile matching document
IDs” is a sensible engineering mitigation but too obvious to serve as a novel
contribution.

Do not run or revive it in its current form.

## 8. Supporting characterization

Useful, but not separate contributions:
- eight natural-language rule formulations;
- delay/distance tests;
- masked diffusion replication;
- Stage 3A/3D semantic ladders and content×identity 2×2;
- Stage 3E redundancy deconfounding and relation matrix;
- tagged provenance streams;
- Stage 4 D7→D9;
- G16 failed class-marker mechanism bridge;
- G17 failed frozen ratio estimand + posthoc raw-point pattern.

## 9. Programme status

**Open only for a redesigned, novelty-driven G20 v3 and its directly coupled
post-resolution mechanism.**

Do not add:
- G21 as current mainline;
- model-size sweeps;
- frontier API breadth;
- more semantic-preview ladders;
- generic reminder/restatement experiments;
- ReGround-v2;
- a third mechanism model before G20 behavior exists.

The next experiment must directly explain the original prospective exclusion reversal.
