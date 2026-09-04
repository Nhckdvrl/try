# Paper mainline draft — v3 scientific fork

**Status:** provisional mother draft after the third mainline audit.
**Target:** NAACL / ACL / EMNLP Main-level paper.
**Authoritative ledger:** [SCIENTIFIC_REGISTER_2026-09-04_V3.md](SCIENTIFIC_REGISTER_2026-09-04_V3.md)

This draft intentionally does **not** commit to a final explanation before G22.

---

# 0. Core question

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

Policies often precede the objects they govern:
- system policy before retrieval;
- evidence admissibility rule before testimony;
- agent policy before tool output.

If an LLM can represent a standing exclusion policy as an executable rule, the same
policy should remain effective when its target arrives later.

Empirically, it often does not.

---

# 1. Broad phenomenon

Across twelve instruction-tuned models, two masked diffusion LMs, four vendors, and five
task families, exclusion stated before evidence is systematically weaker than the same
exclusion stated after evidence.

Matched Admit controls do not show the analogous order effect.

### Main headline

> **Models are systematically worse at pre-committing to evidence exclusion than at
> excluding the same evidence after it appears.**

This remains the paper's entry point.

---

# 2. The reversal is not ordinary instruction failure

The effect survives:
- wording changes;
- substantial rule-to-evidence delay;
- masked diffusion architectures.

A separate policy probe often returns the intended zero weight.

In Qwen3-8B and Gemma-3-12B, even trajectories that explicitly state zero can still use
the prospective evidence.

At the same time, explicit future arithmetic weighting can be executed exactly.

Therefore the problem is not simply:
- instruction forgetting;
- inability to understand zero;
- inability to execute any future rule.

---

# 3. What information about the future target helps?

The Stage 3A object-existence ladder progressively adds information before the rule.

A name, identifier, content-pending marker, type, or expected direction does not
reliably rescue.

Full target content before the rule does.

This suggests that the relevant missing variable is not generic referential
availability.

But what exactly does “full content” supply?

That became the central unresolved question.

---

# 4. G18 confirmed a strong effect but mixed two variables

G18 was designed to test semantic target information prospectively.

It succeeded prospectively on fresh materials:

> `Delta_semantic = +8.91 [7.15,+10.76]`, positive in 5/5 models.

However, the semantic previews are substantive assertions of almost the same proposition
as the later evidence.

The no-rule marginal of the later evidence collapses from roughly 32 points to roughly 3
points under those previews.

Therefore G18 does **not** isolate:
- knowing what the future target will mean;
from
- having that proposition already active as evidence.

The corrected conclusion is:

> **Having the target proposition already represented before exclusion strongly changes
> later suppression.**

This is a factorization clue, not the final novelty.

The semantic exclusion arm also falls about 28 points below the preview-only baseline.
This is retained as a potential clue about active revision/cancellation, but not
interpreted as source-scope collapse.

---

# 5. Two additional clues constrain the explanation

## 5.1 Stage 4 — content-conditioned control

In system→tool prompts, proposition-targeted exclusion can follow content across a
document-ID change while identifier-only protection does not universally do so.

This supports the importance of semantic content.

But the proposition is already written inside the system policy, so this experiment
also does not separate semantic knowledge from evidential instantiation.

## 5.2 Stage 3B — tagged routing is not yet a clean positive exception

A standing policy plus `[verified]/[unverified]` labels yields near-zero leakage.

However the no-policy baseline removes the labels.

Thus success could reflect:
- the standing policy;
- local semantics of `[unverified]`;
- or both.

The old conclusion “class policies prove prospective gating works” is therefore
downgraded.

---

# 6. Existing causal mechanism

Stage 5 compares matched prospective success/failure chronologies where later evidence
appears after the rule in both arms.

It identifies target-dependent causal rule-time windows:
- Qwen3-8B L14–18 / 36;
- Mistral-Small-24B L12–16 / 40.

Interchanging the state changes later evidence suppression.

The strongest licensed statement is:

> **Target availability changes a causal control state formed around exclusion-rule
> processing.**

What computation that state performs remains open.

That open computational interpretation is precisely what the next behavioral
factorization should determine.

---

# 7. The central scientific fork

The paper now asks:

> **What must exist when exclusion is processed for future evidence to become causally
> inert?**

Three candidate accounts remain.

### A. Deferred target binding / eager control compilation

A semantic target representation is enough, but it must be available while exclusion
is processed. Late target resolution may be understood without rebuilding the same
control relation.

### B. Evidential-instantiation / retrospective revision

Knowing exactly what future evidence will say is not enough. Exclusion becomes effective
only after a matching evidential state already exists, suggesting that natural-language
exclusion behaves more like revision/cancellation of an existing representation than a
future gate.

### C. Local semantic control

Prospective control may work when the arriving item itself carries a locally meaningful
control feature, but fail when an earlier policy must create a novel relation to an
arbitrary future object.

The next experiment is designed to distinguish these, not to confirm one favorite
story.

---

# 8. G22 — Target Knowledge vs Evidential Instantiation

G22 is registered but not frozen.

Core target states:

### U — unresolved

```
EXCLUDE target
→ future E(P)
```

### K — known but non-evidential

```
non-evidential specification of P
→ EXCLUDE target
→ future E(P)
```

The specification fixes the target semantics but must not itself be used as case
evidence.

### I — evidentially instantiated

```
asserted evidence P
→ EXCLUDE target
→ future E(P)
```

This approximates the successful G18 semantic condition.

The decisive requirement is that K be genuinely judgment-neutral.

If K is not neutral, G22 fails as a factorization and must not be run in that form.

---

# 9. Conditional paper route A — semantic knowledge is sufficient

If K approaches I:

> **The model can use a non-evidential semantic representation to prepare future
> exclusion.**

Then the next question becomes temporal:

> what happens if that same target mapping becomes known only after the exclusion rule?

Only at this point should the paper test:
- mapping-before vs mapping-after;
- high late-mapping comprehension;
- shared post-resolution checkpoint;
- neutral processing buffer;
- exclusion-operator replay;
- target/mapping replay.

A strong result would be:

> **The model knows the late mapping but does not reconstruct the causal control state
> that forms when target semantics are available during policy processing.**

Then the paper can legitimately develop a deferred-composition / eager-compilation
mechanism.

---

# 10. Conditional paper route B — evidential instantiation is required

If K remains close to U but I strongly rescues:

> **Knowing exactly what future evidence will say is not enough to pre-exclude it.**

This is a much stronger distinction than semantic specificity.

The paper would then ask whether successful exclusion is:

- a passive future gate; or
- an active revision/cancellation operation over an already-present evidence state.

The G18 below-baseline effect becomes relevant here.

A key discriminator would be:
- target present;
- exclusion rule;
- **no later repeated evidence**.

If exclusion shifts judgment even without a later evidence occurrence, the mechanism is
not merely blocking future readout.

Stage 5 would then be used to causally test the target-specific revision state.

---

# 11. Conditional paper route C — local semantic control dominates

If G22 does not cleanly support A or B, deconfound Stage 3B.

Question:

> does `[unverified]` routing work because a standing policy is executed, or because
> the incoming semantic label itself locally evokes discounting?

This can explain some positive exceptions but must not become the main paper unless it
also explains the G0 reversal naturally.

---

# 12. Current claims

### Claim 1 — established

> **Prospective exclusion is systematically harder than retrospective exclusion.**

### Claim 2 — open

> **The decisive target state required for effective exclusion remains unknown.**

G22 resolves it.

### Claim 3 — established with model heterogeneity

> **Explicit policy access can be insufficient for causal enforcement.**

### Claim 4 — established at two-model mechanism scope

> **Target availability changes a causal rule-time state that affects later
> suppression.**

The final computational label for that state is deliberately left open.

---

# 13. Method opening

The final method problem should follow from whichever G22 branch survives.

General form:

> **How should future evidence policies be represented so they remain executable before
> their target exists?**

Potential directions:
- persistent structured policy state;
- factorized policy operator and target instance;
- delayed target instantiation;
- explicit runtime rule state;
- training for future-target policy application;
- activation/routing reconstruction of the required control state.

Do not revive ReGround as the contribution.

---

# 14. What the paper explicitly rejects

- “semantic target information helps” as novelty;
- G21 source-scope as paper center;
- G20 replay as a standalone novelty;
- generic tag semantics;
- generic instruction-order conclusions;
- generic binding claims;
- another breadth sweep.

The final paper must read as one natural question becoming progressively more precise.
