# Claude project instructions

This is the default project context for local agents.

## Read these first

1. MAINLINE_AUDIT_2026-09-04_V2.md — current scientific audit; G21 downgraded.
2. PAPER_FRAME.md — active deferred-control composition frame.
3. NEXT_EXPERIMENTS_POST_RESET.md — G20 v3 design logic; not yet frozen.
4. STATUS.md — stable findings vs active hypothesis.
5. PAPER_DRAFT_MAINLINE.md — current mother draft.
6. PAPER_OUTLINE.md — conditional paper structure.
7. RELATED_WORK_2026.md — occupied literature and novelty boundary.
8. ACL_EMNLP_ALIGNMENT_STANDARD.md — Outstanding-shaped narrative standard.
9. EXPERIMENTS.md / RESEARCH_HISTORY.md — chronology and full registry.

Historical stage files and preregistrations are evidence/provenance. They may contain
interpretations that were later superseded.

## Scientific objective

The original paper question is still the paper identity:

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

Do not broaden the paper into a general provenance, source-scope, or policy-alignment
paper.

The old headline:

> semantic target information makes prospective exclusion work better

is retired as too obvious.

The current hypothesis is:

> **LLMs may construct a target-conditioned exclusion state when the exclusion rule is
> processed, rather than storing a deferred exclusion operator that is reliably
> composed with a target once that target becomes available later.**

Compact form:

> **target → EXCLUDE works better than EXCLUDE → target.**

This is a candidate explanation of G0, not yet an established finding.

## Current mainline logic

### G0 is a composition-order reversal

Retrospective:
`target evidence → EXCLUDE → judgment`

Prospective:
`EXCLUDE → target evidence → judgment`

### G18 factorizes G0

G18 supplies target semantics before the rule while keeping the actual decision evidence
after the rule:

`target semantics → EXCLUDE → later evidence`

This strengthens exclusion.

Use G18 as factorization/diagnostic evidence, not the headline novelty.

### Stage 4 identifies the effective target

Proposition-targeted suppression can follow content across D7→D9; identifier-only
protection does not universally do so.

Use this only to support that the effective control target is substantially
content-conditioned.

### Stage 5 identifies a causal control state

- Qwen3-8B rule-span causal window L14–18 / 36.
- Mistral-Small-24B L12–16 / 40.
- causal interchange changes later evidence suppression.
- state exists before later evidence processing.
- shared steering direction failed.

Do not claim a universal vector or literal TARGET_FOUND feature.

## Active experiment — G20 v3 only

### Deferred Control Composition / Non-Commutative Exclusion

Core:

```
TARGET-FIRST:
P → EXCLUDE → U → CHECKPOINT → EVIDENCE → QUESTION

RULE-FIRST:
U → EXCLUDE → P → CHECKPOINT → EVIDENCE → QUESTION
```

At CHECKPOINT, both orders have already seen target + rule + neutral block.

The important claim is therefore not:
> earlier decoder rule tokens cannot see later P.

It is:
> even at a downstream state where all information is available, the model may retain
> an order-dependent exclusion state.

Mandatory:
- high RULE-FIRST target comprehension;
- TARGET-FIRST > RULE-FIRST exclusion;
- rule replay selectively rescues RULE-FIRST;
- target-replay control if feasible;
- Admit/arithmetic/routing late-composition controls;
- only after behavioral qualification, checkpoint causal interchange.

Strong mechanism:
> TARGET-FIRST checkpoint state rescues RULE-FIRST and reverse patch breaks it, while
> matched Admit/control effects are much smaller.

Do not run a mechanism round before the behavior qualifies.

## G21 status

### Source–Proposition Scope Entanglement

**DOWNGRADED / NOT CURRENTLY AUTHORIZED.**

Reason:
it may be an interesting scope phenomenon, but it does not explain the original G0
prospective/retrospective reversal.

Do not:
- run G21 as the next experiment;
- make it a paper contribution;
- allocate a main figure to it;
- use it to rename/reframe the paper.

Retain the design as future-paper / secondary-consequence provenance.

If revived later, preserve the deconfounded conditional-marginal metric. Never use
B-alone as the primary baseline.

## Stable established findings

### G0
- 144 frozen items / five families.
- 12 instruct models / four vendors + two masked diffusion LMs.
- same exclusion rule works better after evidence than before.
- timing-gap direction same in 12/12 instruct models; 10/12 CIs exclude zero.
- matched Admit rule has no analogous order effect.

### Policy access/enforcement
- separate declarative probe often/at ceiling recovers zero weight;
- Qwen3-8B and Gemma-3-12B can state zero on-policy while prospective evidence still
  affects judgment;
- Phi-4-mini does not show the same strong dissociation.

Correct headline:
> explicit policy access is not sufficient for enforcement in at least some models.

Do not write “the rule is perfectly held and ignored.”

### Boundary
- hard suppression is the difficult regime;
- explicit arithmetic future weighting can prospectively nullify exactly in 4/5 models;
- non-multiplicative transforms retain smaller gaps.

Do not write “only exactly zero.”

### G18
- 100 fresh items / 30 skeletons / 3 families / 5 models;
- Delta_semantic +8.91 [7.15,10.76], 5/5 positive;
- para-empty +12.85 [10.32,15.42].

The below-preview-baseline paraphrase result remains a clue that successful control can
be content-level/over-strong, but do not turn it into a G21 scope paper.

### Agent
ID-only policy can work on its named D7 in Gemma/Qwen3.5.

The safe invariant:
- ID-specific protection does not follow the same proposition D7→D9;
- proposition-targeted suppression does.

### Mechanism
Stage 5 is two-model and causal, not a probe-only result.

## Cancelled work

### ReGround G19
**CANCELLED BEFORE FREEZE AND BEFORE ANY MODEL GENERATION.**

Do not run src/run_reground.py or src/analyze_reground.py.

### G16
Stopped at frozen bridge gate. Do not repair/re-run.

### G17
Frozen ratio estimand failed; posthoc raw-point result remains suggestive only. Do not
confirm it.

### BTF-3 hindsight branch
Stopped. Do not restart.

## Research style

The project is aligning to **Outstanding-shaped scientific abstraction**.

A new experiment is justified only if it can reveal or kill a non-obvious computation
that directly explains G0.

Good:
> After target resolution, does an earlier exclusion rule remain behaviorally
> under-composed?
> Does replaying the operator specifically reconstruct control?
> At a shared post-resolution state, do the two composition histories remain causally
> different?

Bad:
> Does another semantic wording help?
> Does source scope collapse? (interesting, but not current paper)
> Does a 70B model show the same sign?
> Does another reminder improve compliance?
> Can the obvious post-retrieval compiler work?

Do not organize the paper as a reviewer-objection checklist.

## Current experiment authorization

NEXT_EXPERIMENTS_POST_RESET.md is a **design document only**.

Before any G20 generation:
1. build fresh materials;
2. complete design audit;
3. create a dedicated preregistration;
4. implement frozen analyzer and tests;
5. commit/tag the complete design;
6. only then generate.

No result-driven prompt repair.

## Evidence discipline

- Preserve preregistrations/history verbatim.
- Do not overwrite negative/corrected results.
- Use raw rating points for preview/new designs where leverage baselines change.
- Cluster bootstrap by independent skeleton.
- Keep breadth claims attached to the experiment that actually has the breadth.
- G20 claims do not inherit G0's 14-model breadth automatically.

## Environment / GPU policy

Prefer existing local environments and shared caches.

Usable nodes when idle:
fvcrc10, fvcrc11, fvcrc12, fvcrc13, fvcrc15, fvcrc20, fvcrc21.

Check occupancy before launching. During daytime avoid >8 GPUs total unless explicitly
authorized.

## Git policy

Land completed work directly on main with coherent commits.

Current root documents are authoritative; stages/ and preregistrations/ preserve
chronology. Cancelled/stopped work stays visible and must not silently become active.
