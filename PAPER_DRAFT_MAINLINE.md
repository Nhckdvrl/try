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

# 5. Candidate Contribution 2 — Source–Proposition Scope Entanglement

**First priority, pending G21.**

The strongest new question is not whether semantic content helps exclusion. It is
whether semantic control preserves **which source is governed**.

Use:

Source A
→ source-scoped exclusion policy
→ independent Source B
→ decision

The source policy says:
- A is excluded;
- **only A** is excluded;
- B and other independent sources remain fully admissible even if they support the
  same proposition.

B varies:
- paraphrase / mutual entailment;
- more-specific entailment;
- gist;
- high lexical overlap but different proposition;
- unrelated but decision-relevant control.

A separate proposition-scoped policy explicitly says that A's proposition is excluded
regardless of source. This is the positive control for true proposition-level
suppression.

## 5.1 Redundancy-deconfounded metric

Do not compare B-alone with A+B.

Same-proposition sources are naturally redundant. Instead measure B's conditional
marginal with A already present:

BMarginal_no = Y(A+B) - Y(A)

BMarginal_source = Y(A+SourcePolicy+B) - Y(A+SourcePolicy)

SourceSpillover = BMarginal_no - BMarginal_source

Thus any spillover is **additional loss of allowed-B influence caused by the
source-scoped exclusion policy**, beyond ordinary semantic redundancy.

Primary semantic contrast:

mean(SourceSpillover[paraphrase, entail])
-
mean(SourceSpillover[lexical-wrong, unrelated])

## 5.2 Claim if confirmed

> **Exclusion entangles source identity with proposition identity: a policy that
> excludes Source A suppresses the causal contribution of independent, explicitly
> admissible Source B when B expresses the same proposition.**

The strongest version also shows:
- A itself is successfully excluded;
- B has non-trivial conditional leverage;
- proposition-scoped policy suppresses B as expected;
- lexical overlap without semantic identity does not reproduce the effect;
- a post-B reminder that B remains admissible does not fully restore B;
- the model can declaratively answer that B is allowed while behaviorally discounting
  it.

That is a much less normal phenomenon than "semantic target descriptions improve
constraint following".

---

# 6. Candidate Contribution 3 — Dynamic Late Binding

**Second priority, pending strengthened G20.**

The first version of the Binding Deadline idea had its own obviousness problem:
decoder-only rule tokens cannot literally attend to later target tokens.

The publishable claim therefore cannot be:
> the earlier rule-token state does not update.

The stronger test asks whether the **whole model**, at answer time, can dynamically
compose an earlier unresolved exclusion rule with a later target mapping.

PRE:
P → rule → U → evidence

LATE:
U → rule → P → evidence

Both contain the same semantic information before evidence and answer.

## 6.1 Mandatory late-target comprehension

On an independent full-context probe, the model must correctly identify which later
evidence the earlier rule applies to.

If it cannot, G20 is merely target-comprehension failure.

## 6.2 Rule replay

LATE+REPLAY:
U → rule → P → identical rule → evidence

PRE+REPLAY:
P → rule → U → identical rule → evidence

A selective LATE replay rescue tests whether reprocessing the rule after target
resolution repairs enforcement rather than simply adding recency.

## 6.3 Positive late-binding controls

The same earlier-rule/later-target structure must work substantially better for:
- Admit;
- explicit arithmetic;
- use/select routing.

This shows the model is capable of late composition in general.

Masked diffusion models are load-bearing. At least one should preserve the exclusion
pattern despite bidirectional prompt attention before we make a strong rule-compilation
claim.

## 6.4 Claim if confirmed

> **LLMs can understand a late-resolved target yet fail to dynamically attach an
> earlier exclusion policy to it; reprocessing the rule after target resolution
> restores control.**

This is a downstream control-algorithm failure, not the trivial fact that causal
hidden states cannot look backward.

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

### G21 passes
Source–proposition scope entanglement becomes the new centerpiece.

### G21 fails
Do not rescue it with B-alone metrics or more prompt variants; proceed to the strengthened G20 only on its pre-frozen design.

### G20 passes
Dynamic late-binding failure becomes a major explanatory contribution, provided the comprehension, positive-control and masked-diffusion criteria also pass.

### G20 fails
Do not fall back to the trivial rule-token causal-mask story.

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
