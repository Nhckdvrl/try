# Prospective evidence control in language models

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

The project begins from a broad prospective-exclusion paradox: the same exclusion rule
is systematically less effective when stated before its target evidence than after it.

The current mainline no longer treats “semantic target information helps” as the paper
novelty, and no longer centers the separate G21 source-scope question.

The active hypothesis is:

> **LLMs may construct a target-conditioned exclusion state when the rule is processed,
> rather than storing a deferred exclusion operator that is reliably composed with a
> target once the target appears later.**

Compactly:

> **target → EXCLUDE works better than EXCLUDE → target.**

## Stable empirical core

### G0 — prospective exclusion paradox
- 144 frozen items;
- five task families;
- 12 instruction-tuned checkpoints from four vendors;
- two masked diffusion LMs;
- same exclusion rule before vs after evidence;
- 12/12 instruct models show the same timing-gap direction;
- matched Admit control does not show the analogous order effect.

### Policy access vs enforcement
In Qwen3-8B and Gemma-3-12B, prospective evidence can still affect the decision even
on trajectories that explicitly state zero weight; Phi-4-mini is more mediated by
whether the zero-weight state is expressed.

### Arithmetic boundary
When evidence contribution is explicitly represented as arithmetic
`base + w*delta`, four of five tested models execute prospective `w=0` exactly.
The failure is therefore not a generic inability to obey any future-directed zero rule.

### G18 — factorization evidence
- 100 fresh items / 30 fresh skeletons / three families;
- five models / four vendors;
- 9,000 generations;
- frozen raw-point analysis with a no-rule baseline for every preview.

Primary result:
**Delta_semantic = +8.91 [7.15,10.76] rating points**, positive in 5/5 models.

The important reading is temporal/computational:

```
target semantics → EXCLUDE rule → later evidence
```

works much better than the ordinary prospective arrangement where no target semantics
exist when the rule is processed.

### Agent counterfactual
Proposition-targeted suppression can follow the same content across D7→D9, while
identifier-specific protection does not. This is retained as evidence that the effective
control target is substantially content-conditioned.

### Mechanism
Matched-chronology causal interchange finds a target-dependent rule state before later
evidence integration:
- Qwen3-8B: L14–18 / 36;
- Mistral-Small-24B: L12–16 / 40.

Interchanging the state changes later evidence suppression. A reusable shared steering
direction was not found.

## Read first

1. [MAINLINE_AUDIT_2026-09-04_V2.md](MAINLINE_AUDIT_2026-09-04_V2.md)
2. [STATUS.md](STATUS.md)
3. [PAPER_FRAME.md](PAPER_FRAME.md)
4. [NEXT_EXPERIMENTS_POST_RESET.md](NEXT_EXPERIMENTS_POST_RESET.md)
5. [PAPER_DRAFT_MAINLINE.md](PAPER_DRAFT_MAINLINE.md)
6. [PAPER_OUTLINE.md](PAPER_OUTLINE.md)
7. [RELATED_WORK_2026.md](RELATED_WORK_2026.md)
8. [ACL_EMNLP_ALIGNMENT_STANDARD.md](ACL_EMNLP_ALIGNMENT_STANDARD.md)

## Next experiment

### G20 v3 — Deferred Control Composition

Core conditions:

```
TARGET-FIRST:
P → EXCLUDE → U → CHECKPOINT → EVIDENCE → QUESTION

RULE-FIRST:
U → EXCLUDE → P → CHECKPOINT → EVIDENCE → QUESTION
```

By the shared checkpoint both arms have seen the same target semantics, exclusion rule,
and neutral material.

The key possible finding is:

> **Even after the late target is correctly resolved, the model does not reconstruct
> the same exclusion control state unless the exclusion operator is processed again.**

Load-bearing tests:
- high late-target comprehension;
- TARGET-FIRST > RULE-FIRST exclusion;
- selective rescue from replaying the exclusion rule after the late target;
- target-replay control;
- Admit/arithmetic/routing late-composition controls;
- post-resolution checkpoint activation interchange.

This design specifically avoids making the trivial claim that an earlier decoder token
cannot attend to later tokens.

## G21 — downgraded

Source–Proposition Scope Entanglement remains an interesting future experiment, but it
does not explain the original G0 reversal.

Current status:
- not a main contribution;
- not a main figure;
- not authorized as the next generation round;
- retain as future-paper / secondary-consequence provenance.

## Cancelled before generation

### G19 — ReGround
The post-retrieval policy compiler was designed and preregistered but **cancelled before
freeze and before any model generation**.

Historical files:
- [METHOD_REGROUND.md](METHOD_REGROUND.md)
- [preregistrations/PREREGISTRATION_G19_REGROUND.md](preregistrations/PREREGISTRATION_G19_REGROUND.md)

Do not run them.

## Current scientific arc

```
Can models pre-commit to ignore future evidence?
        ↓
G0: exclusion-before-evidence is systematically weaker
        ↓
G18: restoring target semantics before rule processing restores control
        ↓
G20 v3: does late target resolution reconstruct the same control?
        ↓
rule replay + post-resolution causal state
        ↓
order-invariant deferred policy–target composition as the method problem
```

The BTF-3 hindsight branch remains stopped and is not part of this paper.
