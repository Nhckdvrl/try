> **Supersession notice — later on 2026-09-04:** the subsequent mainline audit in
> [MAINLINE_AUDIT_2026-09-04_V2.md](MAINLINE_AUDIT_2026-09-04_V2.md) concluded that
> G21 is interesting but does **not** naturally explain the original G0 reversal.
> Therefore G21 is downgraded from paper-center status. The active mainline is now G20
> v3 Deferred Control Composition / non-commutative exclusion. The historical reasoning
> below is preserved for provenance; its final G21-first priority is superseded.

# Novelty reset — 2026-09-04

## Why this reset exists

The post-G18 paper frame had converged on:

> semantic target information makes prospective exclusion work better.

That statement is empirically true, but as a **headline explanation it is too normal**.
A reviewer can compress it to:

> if the model knows more specifically what it will later have to ignore, of course
> the rule is easier to apply.

That is not a sufficiently memorable scientific abstraction for the paper we want.
Likewise, the first ReGround method design—resolve the policy after retrieval and then
restating the matched document IDs—is a natural engineering response, but not by
itself a novel research contribution.

This reset does **not** discard G18 or the existing mechanism. It changes their role.

- G18 is retained as a diagnostic showing that target semantics affect control.
- Its below-baseline oversuppression becomes a clue, not a success story.
- Stage 5 is retained as evidence that a target-dependent rule state is formed before
  the later evidence is processed.
- ReGround G19 is cancelled before generation.

The active scientific question is now deeper:

> **How do language models bind a control rule to evidence that is not yet
> instantiated, and how precisely can that binding preserve the intended scope?**

## 1. What the literature already occupies

### Generic instruction order is occupied

Instruction Position Matters and Order Matters establish that instruction/constraint
position changes compliance. Our novelty cannot be "later instructions work better".

### Prospective memory is occupied

Prospective-memory work shows that deferred constraints can be forgotten and that
trailing reminders help. Our novelty cannot be "remember the rule later".

### Negative constraints are occupied

Semantic Gravity Wells studies why explicitly named forbidden output tokens can be
primed or late-layer overridden. Our object must remain control over the **causal use
of contextual evidence**, not forbidden output generation.

### Generic binding is occupied

Representational Analysis of Binding in Language Models studies entity–attribute
Binding IDs and low-rank binding subspaces. Our novelty cannot be "LLMs bind things".

### Instruction-state localisation is occupied

Patches of Nonlinearity shows that instruction representations can be localized and
act as circuit selectors. Our novelty cannot be "there is a mid-layer instruction
state".

### Provenance/source tracking is occupied

TROVE, GenProve, GAVEL, attribution-bias work, Label Effects, and source-conflict
benchmarks study where claims came from, whether citations are correct, and how source
labels change trust. They do not ask whether an **exclusion rule can be bound to a
future evidence instance while preserving source/occurrence scope**.

## 2. The two novel hypotheses hidden in our existing results

### Hypothesis A — a binding deadline

G18 was previously read as:

> semantic target information helps.

A stronger hypothesis is temporal:

> **A control rule may have to be processed after its target is instantiated. Target
> information supplied later—even before the actual evidence arrives—may be too late
> to retroactively form the effective rule state.**

This would mean LLMs do not dynamically late-bind an unresolved control rule. They
**eagerly compile** the rule against whatever target representation is available at
rule time.

Why this is plausible from existing data:
- content available before the rule rescues prospective exclusion;
- merely naming a future referent does not;
- Stage 5 finds a causal success/failure state at the rule span **before the evidence
  is read**;
- the state is item-specific rather than a reusable global steering direction.

Why this would be novel:
- it is not ordinary position bias: the critical manipulation is the position of
  **target resolution relative to the rule**, while the evidence stays after the rule;
- it is not prospective memory: the rule remains present and target information is
  supplied before the decision;
- it is not generic autoregressive causality if the same failure survives matched
  positive controls and bidirectional masked-diffusion models.

### Hypothesis B — semantic scope collapse

G18 contains an anomaly that should no longer be treated as a side note:

- paraphrase preview makes the later evidence nearly redundant: marg(no-rule) ~ +3;
- adding an exclusion rule drives marg(exclude) to about **-28**, below the
  preview-only baseline.

The old framing called this "block-transcending suppression". The stronger hypothesis:

> **Once an exclusion rule successfully binds through semantic content, its effect may
> lose provenance/occurrence precision and spread from the excluded evidence instance
> to semantically equivalent information outside the rule's intended scope.**

This is a **scope failure**, not a specificity benefit.

Why existing results point this way:
- G18 below-baseline suppression already suggests the previewed occurrence is being
  discounted even though the rule names the later block;
- Stage 3D content×identity shows content dominates label identity;
- Stage 4 shows semantic policies follow a proposition across D7→D9;
- meaningful provenance labels can help selective routing, whereas semantic-empty tags
  do not.

The new question is therefore not whether semantics help, but whether semantic binding
**collapses source/occurrence scope into proposition scope**.

## 3. A stronger unifying story: under-binding vs over-binding

The current project may reveal a control trade-off:

### Under-binding

When the target has not been instantiated at rule time:

> the policy remains abstract and later evidence leaks into the decision.

### Over-binding

When a sufficiently specific semantic target has been instantiated:

> the policy binds, but suppression may spread to semantically equivalent evidence
> outside the intended source or occurrence.

The important scientific object becomes:

> **Can LLMs bind a future control rule both effectively and precisely?**

This is substantially less obvious than "more target information helps".

A successful final paper would show that current LLMs have difficulty maintaining both
axes at once:

1. **binding strength** — does the rule actually control the target?
2. **scope precision** — does it control only the intended evidence instance/source?

## 4. Candidate final narrative

### Act I — the paradox

The same exclusion rule is weaker before evidence than after evidence across the broad
G0 panel.

This is the empirical entry point.

### Act II — rules have a binding deadline

Move the **same semantic target description** from before the rule to after the rule
while keeping it before the actual evidence. If the post-rule target fails to rescue,
but replaying the identical rule after target revelation restores exclusion, then the
model has a rule-time binding deadline.

The headline becomes:

> **LLMs compile exclusion rules against the targets available when the rule is read;
> later target resolution does not reliably update that control relation.**

### Act III — successful binding can collapse scope

Give two independently sourced evidence instances. Exclude Source A but explicitly
retain Source B. If A and B express the same proposition, test whether excluding A also
suppresses B.

The headline becomes:

> **Semantic binding solves the under-binding problem by sacrificing provenance
> precision: exclusion can spread from a source-scoped rule to the proposition
> itself.**

### Act IV — causal mechanism

Use the existing Stage-5 result as the computational bridge:
- the target-dependent rule state forms in the middle of the network;
- it exists before the later evidence is processed;
- interchanging it changes later suppression;
- it replicates in Qwen and Mistral.

A new mechanism round is justified only if the new behavioral scope result passes.
The first target would be whether the causal state is sensitive to semantic identity
more than provenance identity.

## 5. Why this is Outstanding-shaped rather than merely Main-shaped

The strongest phenomenon papers do not stop at a sensible factor.

- Llama See, Llama Do turns "context distracts" into the specific mechanistic
  regularity of contextual entrainment.
- Racing Thoughts turns contextualization mistakes into an ordering/dependency
  hypothesis about when one computation must finish before another begins.
- Tool Irrelevance turns a known tool-use failure into a conflict between structural
  and semantic pathways.

The corresponding move here is no longer:

> target semantics help.

It is:

> **prospective evidence control has a binding-time and scope problem: rules appear to
> be compiled before unresolved targets can be late-bound, while successful semantic
> binding can erase the provenance boundary that defines what should be excluded.**

That is a new computational claim with two directly testable consequences.

## 6. What is removed from the main narrative

The following are no longer paper identities:

- "Target Addressability Governs Prospective Exclusion" as the central novelty;
- "semantic descriptions are better than identifiers" as a headline;
- ReGround as a novel method;
- a general claim that semantic policies are simply preferable to identifier policies.

G18 stays in the paper, but as evidence that motivated the stronger hypotheses and as
a deconfounded diagnostic of semantic dependence.

## 7. Current decision

**Do not run the frozen ReGround design.**

The next behavioral work should target the two hypotheses above, in this order:

1. **G20 — Binding Deadline / Late Target Revelation**
2. **G21 — Source-Scope Collapse**

Both experiments must be designed before any new generation so they can be evaluated
without another post-result narrative pivot.

If neither phenomenon appears, the paper falls back to the broad G0 phenomenon +
mechanism and should be re-evaluated rather than reviving the normal
"semantic-target-helps" story.


## 8. Second audit — G20 obviousness and G21 redundancy

A second pass applied the same "too normal?" test to the replacement experiments.

### G20 needed a stronger formulation

The first Binding Deadline design risked another trivial story. In a decoder-only
Transformer, an earlier rule-token hidden state cannot literally attend to later target
tokens because of the causal mask. Therefore "later target information does not update
the earlier rule token" is an architectural fact, not a discovery.

G20 remains interesting only under a stronger criterion:

> The full model can correctly identify the late target at answer time, can perform
> matched late-binding operations in Admit/arithmetic/routing controls, yet still fails
> to enforce the earlier exclusion unless the rule is reprocessed.

A selective rule-replay rescue and replication in at least one bidirectional masked
diffusion model are therefore load-bearing, not optional decoration.

### G21's first metric repeated the Stage-3E redundancy mistake

Comparing B-alone leverage with B's contribution after semantically equivalent Source A
is present would confound source-scope spillover with ordinary semantic redundancy.

The corrected G21 uses a difference-in-differences:

- BMarginal_no = Y(A+B) - Y(A)
- BMarginal_source = Y(A+SourceScoped(A)+B) - Y(A+SourceScoped(A))
- SourceSpillover = BMarginal_no - BMarginal_source

Thus the question is whether the **source-scoped exclusion policy removes additional
allowed-B influence beyond whatever redundancy A already creates**.

G21 also gains an explicit positive-control policy:
- source-scoped: exclude A only, preserve B;
- proposition-scoped: exclude proposition p from any source.

The strongest result would be source-scoped behavior moving toward proposition-scoped
behavior only when B is semantically equivalent to A.

### Updated priority

**G21 is now first priority.**

It tests a genuinely non-obvious control failure:
> the model may understand provenance and policy scope declaratively yet entangle
> source identity with proposition identity during causal evidence weighting.

G20 remains valuable, but only if it survives the stronger comprehension, positive
late-binding, replay-specificity, and bidirectional-architecture criteria in
NEXT_EXPERIMENTS_POST_RESET.md.
