# Prospective evidence control in language models

> **Can a language model bind a control rule to evidence that does not yet exist—and
> keep that rule scoped to the right evidence once the target appears?**

The project began from a broad prospective-exclusion paradox: the same exclusion rule
is systematically less effective when stated before its target evidence than after it.
The post-G18 novelty audit retired the too-obvious headline
"semantic target information helps". The active paper now asks two sharper questions:

1. **Binding deadline:** can an unresolved rule be late-bound when its target becomes
   semantically identifiable only after the rule has already been processed?
2. **Scope precision:** when semantic binding succeeds, does exclusion remain scoped to
   the intended source/occurrence, or spill over to independently admissible evidence
   expressing the same proposition?

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
whether the zero-weight state is expressed. Policy accessibility is therefore not a
complete account of enforcement.

### G18 — semantic diagnostic, not the paper headline
- 100 fresh items / 30 fresh skeletons / three families;
- five models / four vendors;
- 9,000 generations;
- frozen raw-point analysis with a no-rule baseline for every preview.

Primary result:
**Delta_semantic = +8.91 [7.15,10.76] rating points**, positive in 5/5 models.

The important post-reset clue is the decomposition: under a paraphrase preview the
later evidence contributes only about +3 points without the rule, yet the exclusion
condition drives it to about **-28 points** relative to preview-only baseline. This
suggests possible semantic over-binding / scope spillover rather than merely a useful
specificity effect.

### Agent counterfactual
Identifier-specific protection does not follow the same proposition from D7 to D9,
whereas proposition-targeted suppression does. Under the reset, this is evidence that
semantic control can cross document identity—potentially useful for proposition-scoped
policies, potentially a scope error for source-scoped policies.

### Mechanism
Matched-chronology causal interchange finds a target-dependent rule state before later
evidence integration:
- Qwen3-8B: L14–18 / 36;
- Mistral-Small-24B: L12–16 / 40.

Interchanging the state changes later evidence suppression. A reusable shared steering
direction was not found.

## Active novelty reset

Read these first:

1. [NOVELTY_RESET_2026-09-04.md](NOVELTY_RESET_2026-09-04.md)
2. [NEXT_EXPERIMENTS_POST_RESET.md](NEXT_EXPERIMENTS_POST_RESET.md)
3. [PAPER_FRAME.md](PAPER_FRAME.md)
4. [PAPER_DRAFT_MAINLINE.md](PAPER_DRAFT_MAINLINE.md)
5. [PAPER_OUTLINE.md](PAPER_OUTLINE.md)
6. [STATUS.md](STATUS.md)
7. [RELATED_WORK_2026.md](RELATED_WORK_2026.md)
8. [ACL_EMNLP_ALIGNMENT_STANDARD.md](ACL_EMNLP_ALIGNMENT_STANDARD.md)

## Next experiments

### G20 — Binding Deadline / Late Target Revelation
Use the same semantic target information in both arms, but move it across the
rule-processing boundary:

PRE-BIND:
semantic target → rule → unrelated block → evidence

LATE-BIND:
unrelated block → rule → semantic target → evidence

A rule-replay factorial tests whether reprocessing the identical rule after late target
revelation reconstructs control. Matched Admit, arithmetic, and masked-diffusion
controls distinguish the hypothesis from generic order, memory, and autoregressive
attention accounts.

### G21 — Source-Scope Collapse
Exclude Source A while explicitly preserving independent Source B. Manipulate whether B
expresses the same proposition as A or only a lexical/semantic control. Measure how
much of B's independently established evidential contribution survives.

The key possible finding is not "semantic policies generalize", but:
> **source-scoped exclusion can become proposition-scoped suppression.**

## Cancelled before generation

### G19 — ReGround
The post-retrieval policy compiler was designed and preregistered but **cancelled before
freeze and before any model generation**. The method was judged too obvious as a
scientific contribution: resolve the policy after retrieval and mark the matching
document excluded.

Historical files are retained:
- [METHOD_REGROUND.md](METHOD_REGROUND.md)
- [preregistrations/PREREGISTRATION_G19_REGROUND.md](preregistrations/PREREGISTRATION_G19_REGROUND.md)

Do not run them.

## Historical records

The controlled files in [stages/](stages/) and original preregistrations are preserved
for chronology. Their local interpretations may predate G18 and the novelty reset.
Current scientific framing lives in the root documents above.

The BTF-3 hindsight branch remains stopped and is not part of this paper.
