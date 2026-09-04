# Paper mainline draft — novelty-reset version

**Status:** provisional scientific mother draft after 2026-09-04 novelty audit.
**Target:** Outstanding-shaped organisation; NAACL Main as realistic acceptance target.

The previous center—"semantic target information improves exclusion"—has been
retired as too obvious. This draft separates **established evidence** from the two new
hypotheses that must earn the final story.

---

# 0. One-paragraph candidate abstract

> Policies often precede the evidence they are meant to govern. We find that language
> models are systematically worse at excluding evidence when an exclusion rule is
> stated before the evidence than after it, across twelve instruction-tuned models,
> two masked diffusion language models, and five task families. The failure cannot be
> reduced to policy access alone: in some models the policy can be explicitly
> recovered while the excluded evidence still affects the decision. Existing
> experiments reveal that target semantics alter a causal rule state before the
> evidence is processed, but this observation raises a deeper question than prompt
> specificity: **when can a control rule bind to a target that does not yet exist, and
> how precisely is that binding scoped?** We therefore test two hypotheses. First, a
> **binding deadline**: target information revealed after a rule has been processed may
> fail to retroactively instantiate the earlier control relation, unless the rule is
> processed again. Second, **semantic scope collapse**: once exclusion binds through
> semantic content, it may spread from the intended evidence source or occurrence to
> independently admissible evidence expressing the same proposition. A previously
> identified mid-network rule state provides a causal mechanism linking target
> availability to later evidence suppression.

The last two empirical claims enter the final abstract only if G20/G21 confirm them.

---

# 1. The natural problem

A system can know a policy before it knows the object to which the policy will later
apply.

Examples:
- a system policy exists before a retrieval result;
- a source may be ruled inadmissible before its testimony is fetched;
- an agent may be told not to use a class of memories before those memories are
  instantiated.

The obvious mental model is **late binding**:
the system stores the rule now, resolves its target later, and then applies the rule
when the target appears.

The project asks whether LLMs actually implement that kind of dynamic control.

A second requirement is usually implicit: a policy should preserve **scope**.
Excluding Source A should not make an independent Source B inadmissible merely because
B says the same thing.

Thus the final scientific object has two dimensions:

> **Can a language model bind a future control rule strongly enough to work, and
> precisely enough to govern only what the rule actually scopes over?**

---

# 2. Established phenomenon — prospective exclusion fails

## 2.1 Dataset

G0 uses 144 frozen items across five families:
- legal judgment;
- evidence inference;
- ranking / selection;
- outcome evaluation;
- numeric aggregation.

Every item provides:
- Base;
- Admit-before / Admit-after;
- Exclude-before / Exclude-after.

The evidence and rule content are matched across timing conditions.

## 2.2 Model breadth

- 12 instruction-tuned checkpoints;
- four vendors;
- roughly 3.8B–32B parameters;
- two masked diffusion LMs.

## 2.3 Result

The exclusion timing gap has the same sign in all 12 instruct models; 10/12 confidence
intervals exclude zero.

Representative REI:
- Phi-4-mini: pre +0.50 vs post +0.24
- Gemma-3-12B: +0.43 vs +0.07
- Qwen2.5-32B: +0.30 vs +0.00
- Mistral-Small-24B: +0.19 vs −0.03
- Qwen3-8B: +0.45 vs +0.12
- Qwen3-14B: +0.49 vs −0.07
- Qwen3.5-27B: −0.05 vs −0.29

Matched Admit order is approximately flat.

### Established headline

> **Language models are systematically worse at pre-committing to evidence exclusion
> than at excluding the same evidence after it has appeared.**

This is Figure 1.

---

# 3. The problem is not just forgetting the rule

The separate declarative probe recovers the intended zero-weight policy at or near
ceiling.

The stronger on-policy result is model-heterogeneous:
- Qwen3-8B and Gemma-3-12B can spontaneously state zero weight while prospective
  evidence still affects the answer;
- Phi-4-mini largely mediates the behavior through whether zero is stated.

Teacher-forcing the correct zero-weight state does not fully restore Qwen/Gemma
prospective suppression.

Supporting controls:
- ~1,000-token rule-to-evidence delay does not monotonically worsen the prospective
  effect;
- eight rule wordings preserve the gap;
- masked diffusion models preserve the phenomenon.

### Established conclusion

> **Policy accessibility and policy enforcement can separate.**

Do not turn that into a universal hidden-state claim.

---

# 4. G18 — diagnostic evidence, not the final novelty

G18 uses:
- 100 fresh items;
- 30 fresh skeletons;
- three families;
- five checkpoints / four vendors;
- 9,000 generations;
- six target representations with their own no-rule baselines;
- raw sign-aligned rating points.

Pooled ExclusionEffect:
- entail: **31.16 [27.99,34.40]**
- paraphrase: **30.93 [28.19,33.66]**
- identifier: 26.27 [23.65,28.96]
- unrelated: 22.06 [19.16,24.97]
- none: 21.84 [19.21,24.66]
- lexical-overlap / wrong proposition: 18.08 [15.71,20.57]

Frozen semantic contrast:

> **+8.91 [7.15,10.76]**, positive in 5/5 models.

This proves semantic target information changes prospective exclusion.

It does **not** earn a headline such as:
> more specific semantic targets are better.

That is too obvious.

Instead G18 contributes two clues for the new story.

## 4.1 Clue 1 — the successful target always precedes rule processing

The target manipulation in G18 is available before the rule.

Stage 5 then finds a causal success/failure state **at the rule span**, before the later
evidence is processed.

This motivates a temporal hypothesis:
> perhaps target information must exist when the rule is processed.

## 4.2 Clue 2 — semantic success overshoots its literal block

Under paraphrase:
- marg(no-rule) ≈ +3;
- marg(exclude) ≈ **−28** relative to preview-only baseline.

The exclusion does more than remove the later evidence's marginal contribution.

This motivates a scope hypothesis:
> perhaps successful semantic binding spreads to semantically equivalent information
> outside the rule's intended evidence occurrence.

---

# 5. Candidate Contribution 2 — the Binding Deadline

**Pending G20.**

The key experiment is intentionally not another semantic-specificity ladder.

Use the **same semantic target block P and same unrelated block U** and swap only their
order relative to the exclusion rule:

PRE-BIND:
P → rule → U → evidence

LATE-BIND:
U → rule → P → evidence

Thus:
- same semantic information;
- same evidence;
- same rule;
- target is available before decision in both;
- only whether target resolution occurs before or after rule processing changes.

A second factorial replays the identical rule after both blocks:

PRE + REPLAY:
P → rule → U → rule → evidence

LATE + REPLAY:
U → rule → P → rule → evidence

## Claim if confirmed

> **Prospective exclusion has a binding deadline. An unresolved rule is not reliably
> late-bound when its target is revealed later; reprocessing the rule after target
> revelation restores the control relation.**

Why this is scientifically stronger:
- the old "semantic information helps" account predicts PRE and LATE should both help;
- ordinary prospective memory predicts a reminder effect, not a target-relative
  binding deadline;
- generic instruction position is controlled because the first rule remains fixed;
- masked-diffusion replication would show that the effect is not merely an
  autoregressive attention restriction.

Matched Admit and arithmetic controls ask whether the deadline is specific to
destructive evidence control rather than generic late composition.

---

# 6. Candidate Contribution 3 — Semantic Scope Collapse

**Pending G21.**

G21 makes scope explicit.

Suppose:
- Source A is excluded;
- Source B is independent and explicitly admissible;
- A and B express the same proposition.

Correct behavior:
> remove A, preserve B.

Potential LLM behavior:
> once the exclusion is semantically bound, B loses influence too.

## Core estimand

Measure Source B alone:

BLeverage = Y(B) − Y(Base)

Then measure B in the presence of excluded A:

BRetained = Y(A+B+ExcludeA) − Y(A+ExcludeA)

Spillover:

Spillover = BLeverage − BRetained

The decisive contrast compares:
- B paraphrases/entails A's proposition;
versus
- lexical-overlap wrong meaning / unrelated B.

## Claim if confirmed

> **Semantic exclusion can collapse provenance scope: a rule that excludes one
> evidence source suppresses an independent admissible source when both express the
> same proposition.**

An explicit:
> Source B remains admissible and should retain full evidential weight

condition makes the test especially strong.

This is not "semantic policies generalize well". It is the opposite:
> semantic generalization becomes a control error when policy scope is source-specific.

---

# 7. Candidate higher-level result — a binding–scope trade-off

If both new experiments pass, the paper has one memorable abstraction.

## Under-binding

The target is unresolved when the rule is processed.

Result:
> later target/evidence is insufficiently controlled.

## Over-binding

The semantic target is instantiated strongly enough for the rule to work.

Result:
> suppression spreads beyond the intended source/occurrence.

### Final scientific claim

> **Current LLMs struggle to bind prospective evidence-control rules both strongly and
> precisely: unresolved rules under-bind future targets, while semantic binding can
> over-bind across provenance boundaries.**

This is not a prompt engineering observation.

It is a statement about the internal control abstraction used by the model.

---

# 8. Mechanism — existing causal evidence

Stage 5 compares two same-chronology conditions:
- unrelated preview → rule → evidence;
- paraphrase preview → rule → evidence.

Qwen3-8B:
- behavioral gap +13.2 [8.6,18.1];
- rule-span break +13.3 [8.1,18.9] at layer 14;
- rescue smaller but significant around −3.6 [−5.9,−1.4];
- causal window L14–18 / 36.

Mistral-Small-24B:
- behavioral gap +18.2 [10.0,26.9];
- break +18.3 [12.6,24.5];
- rescue −16.1 [−24.2,−9.0];
- causal window L12–16 / 40.

Shared result:

> **A target-dependent mid-network rule state forms before the later evidence is
> processed, and causally changes later suppression.**

Under the novelty reset, the most important mechanistic interpretation is:
> the critical computation happens at rule processing.

The failed shared steering direction is useful:
the control state appears item-specific, not a generic one-dimensional "ignore"
feature.

## Mechanism after G20/G21

If G20 passes:
test whether late target revelation fails to reconstruct the successful policy state
unless the rule is replayed.

If G21 passes:
test whether causal control follows Source-B semantic content more strongly than its
source/provenance label.

Do not run these before the new behavioral effects exist.

---

# 9. Literature positioning

## Instruction position

Instruction Position Matters and Order Matters show that placement changes compliance.
They do not isolate **target resolution crossing the rule-processing boundary**.

## Prospective memory

Prospective-memory work studies whether deferred constraints are remembered under
load and shows trailing reminders can help. Here the target is revealed before the
decision and the question is whether an unresolved rule can be **late-bound**.

## Binding

Representational Analysis of Binding studies entity–attribute associations and Binding
IDs. This paper concerns binding **control scope** to future evidence.

## Instruction vectors

Patches of Nonlinearity shows localized instruction representations and circuit
selection. It does not ask whether a later target can update an earlier control state.

## Provenance

TROVE, GenProve, GAVEL, Label Effects and source-conflict work study attribution,
source tracking, citation, or trust.

The new source-scope question is different:
> **does a source-scoped exclusion rule preserve the contribution of an allowed source
> that says the same thing?**

## Negative constraints

Semantic Gravity Wells studies forbidden output tokens and semantic priming.
Our dependent variable is the causal use of evidence inside a decision, with explicit
source/occurrence scope.

---

# 10. Outstanding-shaped comparison

### Llama See, Llama Do

Known coarse problem:
> context distracts.

New sharp object:
> contextual entrainment.

Our target:
> not "semantic context helps", but **binding deadline + scope collapse**.

### Racing Thoughts

Known coarse problem:
> contextualization sometimes fails.

Sharp mechanism:
> a dependency must resolve before downstream integration; violations create race
> conditions.

Our potential analogue:
> target resolution may have to complete **before rule compilation**, not merely before
> final decision.

### Tool Irrelevance

Known coarse problem:
> models call irrelevant tools.

Sharp factor:
> structural alignment vs semantic relevance.

Our potential factorization:
> **binding strength vs scope precision**, with target timing determining the first and
> semantic/provenance identity determining the second.

---

# 11. Figure plan if G20/G21 pass

## Figure 1 — Prospective exclusion paradox
Broad G0 panel + Admit control.

## Figure 2 — Binding deadline
PRE vs LATE target permutation, with rule replay interaction.
Small diffusion / Admit inset.

## Figure 3 — Scope collapse
Source A excluded, Source B allowed.
Show B retention by semantic relation and explicit-B-admissible condition.

## Figure 4 — Causal rule state
Qwen + Mistral mid-layer interchange, interpreted as rule-time control computation.

G18 moves to a compact diagnostic panel or main-text bridge, with full factorial in
appendix.

---

# 12. Current stop/go logic

### G20 passes
Binding deadline becomes the new explanatory center.

### G20 fails
Do not force the story. The old "semantic information helps" account remains too
normal; proceed to G21 because scope collapse can independently provide the novelty.

### G21 passes
Scope collapse becomes at least a major contribution and possibly the centerpiece.

### Both fail
Do not revive ReGround or "target addressability" as a headline. Re-evaluate whether
the broad G0 + existing mechanism is sufficient for a smaller paper.

---

# 13. What is no longer active

- ReGround G19: cancelled before generation.
- "Target Addressability Governs Prospective Exclusion": retired as headline.
- generic post-retrieval restatement: supporting control only.
- more identifier-vs-semantic ladders: not useful.
- more model size breadth: not the missing scientific value.

The next gain must be a genuinely new computational phenomenon.
