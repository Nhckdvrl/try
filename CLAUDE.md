# Claude project instructions

This is the default project context for local agents.

## Read these first

1. NOVELTY_RESET_2026-09-04.md — why the old semantic-target story was retired.
2. PAPER_FRAME.md — active candidate scientific frame.
3. NEXT_EXPERIMENTS_POST_RESET.md — G20/G21 design logic; not yet frozen.
4. STATUS.md — stable findings vs active hypotheses.
5. PAPER_DRAFT_MAINLINE.md — current mother draft.
6. PAPER_OUTLINE.md — conditional paper structure.
7. RELATED_WORK_2026.md — occupied literature and novelty boundary.
8. ACL_EMNLP_ALIGNMENT_STANDARD.md — Outstanding-shaped narrative standard.
9. EXPERIMENTS.md / RESEARCH_HISTORY.md — chronology and full registry.

Historical stage files and preregistrations are evidence/provenance. They may contain
interpretations that were later superseded.

## Scientific objective

The old headline:

> semantic target information makes prospective exclusion work better

is **retired as too obvious**.

Do not restore it as the paper novelty.

The active question is:

> **Can a language model bind a control rule to evidence that does not yet exist, and
> keep that rule scoped to the correct evidence source/occurrence once the target
> appears?**

Two active hypotheses:

### H1 — Source–Proposition Scope Entanglement (first priority)

A source-scoped exclusion policy may behaviorally become proposition-scoped.

Planned G21:
- Source A appears before the policy and is excluded;
- Source B is independent and explicitly admissible;
- vary whether B paraphrases/entails A, has lexical overlap with different meaning, or
  is unrelated but decision-relevant;
- compare source-scoped and proposition-scoped policies;
- use conditional B marginals:
  BMarginal_no = Y(A+B)-Y(A)
  BMarginal_source = Y(A+SourcePolicy+B)-Y(A+SourcePolicy)
- SourceSpillover = BMarginal_no-BMarginal_source.

Never use B-alone as the primary baseline; that repeats the Stage-3E redundancy error.

### H2 — Dynamic Late Binding (second priority)

The first "binding deadline" phrasing was too close to the trivial causal-mask fact
that earlier decoder hidden states cannot see later tokens.

Planned G20 is only publishable if:
- the model correctly identifies the late target on a full-context probe;
- Admit/arithmetic/routing late-binding controls work;
- exclusion still has PRE>LATE;
- replaying the identical rule selectively repairs LATE;
- at least one masked-diffusion model with bidirectional prompt attention preserves the
  pattern.

The claim is then about failure of downstream dynamic control composition, not about
an earlier rule token literally updating.

## Stable established findings

### G0
- 144 frozen items / five families.
- 12 instruct models / four vendors + two masked diffusion LMs.
- same exclusion rule works better after evidence than before.
- timing-gap direction same in 12/12 instruct models; 10/12 CIs exclude zero.
- matched Admit rule has no analogous order effect.

Do not claim this is exactly the reverse of a matched human experiment. It reversed a
human-literature-motivated preregistered prediction.

### Policy access/enforcement
- separate declarative probe often/at ceiling recovers zero weight;
- Qwen3-8B and Gemma-3-12B can state zero on-policy while prospective evidence still
  affects judgment;
- Phi-4-mini does not show the same dissociation.

Correct headline:
> explicit policy access is not sufficient for enforcement in at least some models.

Do not write "the rule is perfectly held and ignored".

### Boundary
- hard suppression is the difficult regime;
- explicit arithmetic future weighting can prospectively nullify exactly in 4/5 models;
- non-multiplicative transforms retain smaller gaps.

Do not write "only exactly zero".

### G18
G18 is a **prospectively confirmed diagnostic**, not the final novelty:
- 100 fresh items / 30 skeletons / 3 families / 5 models;
- Delta_semantic +8.91 [7.15,10.76], 5/5 positive;
- para-empty +12.85 [10.32,15.42].

The scientifically important clue after reset:
semantic paraphrase condition has marg(no-rule) about +3 but marg(exclude) about -28,
below preview-only baseline. This motivates possible over-binding/scope spillover.

Do not headline "Target Addressability Governs Prospective Exclusion".

### Agent
ID-only policy can work on its named D7 in Gemma/Qwen3.5. The invariant is:
- ID-specific protection does not follow the same proposition D7→D9;
- proposition-targeted suppression does.

Under reset, this is not automatically a benefit. For a source-scoped policy,
following content across identity may be a scope error.

### Mechanism
Stage 5 is **two-model**, not Qwen-only:
- Qwen3-8B rule-span causal window L14–18 / 36;
- Mistral-Small-24B L12–16 / 40;
- causal transfer changes later evidence suppression;
- state exists before later evidence processing;
- shared steering direction failed → no universal reusable vector.

Correct use:
> target availability changes a causal rule-time state that later controls evidence
> suppression.

Do not claim literal TARGET_FOUND feature or universal semantic-binding vector.

## Cancelled work

### ReGround G19
**CANCELLED BEFORE FREEZE AND BEFORE ANY MODEL GENERATION.**

Do not run src/run_reground.py or src/analyze_reground.py.

The code/preregistration are preserved only because they were written before the
novelty audit. The method—resolve semantic policy after retrieval and compile matching
IDs—was judged too obvious as paper novelty.

### G16
Stopped at frozen bridge gate. Do not repair/re-run.

### G17
Frozen ratio estimand failed; posthoc raw-point result remains suggestive only. Do not
confirm it.

### BTF-3 hindsight branch
Stopped. Do not restart.

## Research style

The project is explicitly aligning to **Outstanding-shaped scientific abstraction**.

A new experiment is justified only if it can reveal or kill a new non-obvious
phenomenon.

Good:
> Does target resolution have to precede rule processing?
> Does successful semantic exclusion destroy source scope?

Bad:
> Does another semantic wording help?
> Does a 70B model show the same sign?
> Does another reminder improve compliance?
> Can we make the obvious post-retrieval compiler work?

Do not organize the paper as a reviewer-objection checklist.

## Current experiment authorization

NEXT_EXPERIMENTS_POST_RESET.md is a **design document only**.

Before any G20 or G21 generation:
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
- New G20/G21 claims do not inherit G0's 14-model breadth automatically.

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