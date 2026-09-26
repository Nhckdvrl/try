# Mainline audit — G22 is a branching discriminator, not automatic novelty

**Date:** 2026-09-05  
**Target:** NAACL / ACL / EMNLP Main, using an Outstanding-shaped scientific bar.  
**Repository state audited:** main at `7f141e3ae15c63e8bcbdd7bacb6fb7cbf3c7f05e`.

This audit does **not** authorize model generation. It refines the scientific role of
the registered G22 design after re-reading G0, Stage 3C/3D/3E, Stage 4, Stage 5, G18,
and the 2024–2026 literature around instruction position, standing instructions,
prospective memory, binding, instruction representations, dependency order,
selective forgetting, and provenance.

---

# 1. Paper identity is unchanged

The paper remains:

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

The natural phenomenon remains G0:

> the same exclusion policy is systematically weaker before its target evidence appears
> than after it appears.

Nothing discovered after G0 should replace this question with a different paper about
generic provenance, labels, source trust, instruction position, or semantic specificity.

---

# 2. The strongest current causal graph

The clean descent is:

```
G0: prospective exclusion < retrospective exclusion
        ↓
not generic recency / forgetting / wording / decoder masking
(Admit order control, delay, paraphrases, diffusion models)
        ↓
not generic inability to obey a future zero rule
(explicit arithmetic succeeds)
        ↓
policy access is not causal enforcement
(Qwen/Gemma can state zero and still use prospective evidence)
        ↓
successful exclusion changes sharply with the target state available
when the exclusion policy is processed
(object-existence ladder, G18, Stage 4)
        ↓
a target-dependent causal rule-time state exists
(Stage 5, two architectures)
        ↓
MISSING FACTOR:
is exact non-evidential target knowledge enough,
or must the proposition already be instantiated as evidence?
        ↓
G22
        ↓
Branch A: K is sufficient → test late policy-target composition
Branch B: only I is sufficient → test retrospective state revision/cancellation
```

This is a single story. G21 does not sit naturally in this descent.

---

# 3. Working mechanism hypothesis

The best current **hypothesis**, not yet a claim, is:

> **Natural-language exclusion is compiled against a target state rather than stored as
> a reliably pending, unbound gate.**

More explicitly:

> During policy processing, the model constructs a target-conditioned control state from
> whatever representation of the target is currently available. When no suitable target
> state exists, it does not reliably preserve an unbound exclusion relation that can be
> attached later.

This hypothesis explains the existing assets without pretending the unresolved part is
already known:

- **G0:** retrospective exclusion has a target state available; prospective exclusion may
  not.
- **G18:** a content-matched pre-rule representation strongly changes exclusion, but G18
  mixes semantic knowledge with evidential instantiation.
- **Stage 4:** effective control can be content-conditioned across document identity.
- **Stage 5:** target availability changes a mid-network causal state while the rule is
  processed.
- **Arithmetic boundary:** an explicit symbolic `w=0` computation does not require the
  same semantic evidence-control construction.

The unresolved question is what counts as the required target state. G22 exists to
answer that.

---

# 4. G22's scientific role — corrected

G22 should **not** be called the paper's novelty-bearing experiment in advance.

It is a **branching discriminator**.

Its scientific value depends on the outcome:

## Route A — K rescues

If exact target semantics are known before the rule through a genuinely
non-evidential, judgment-neutral carrier and `K ≈ I`, then:

> “knowing what the future target will say helps exclusion”

is **not** enough novelty by itself. It is too close to specificity / target
availability / identify-then-ignore results already surrounding the area.

In this branch, G22 is a bridge. The novelty-bearing follow-up becomes:

> **The model correctly understands a target resolved after policy processing but fails
> to instantiate the causal exclusion relation unless the exclusion operator is
> processed again.**

That is the non-obvious late-composition prediction. It must be separated from the
trivial fact that earlier decoder states cannot attend to future tokens.

A valid follow-up therefore needs:
- the same semantic catalog in early/late conditions;
- only the target mapping time changed;
- high late-mapping comprehension;
- positive controls showing late-resolved information can drive ordinary
  use/select/arithmetic behavior;
- a shared post-resolution checkpoint;
- neutral extra-computation control;
- only then operator replay / backpatch / frozen-backpatch.

## Route B — only I rescues

If K is neutral and fully understood but `K ≈ U` while evidential instantiation
strongly rescues, G22 itself becomes a non-obvious result:

> **Knowing exactly what future evidence will say is insufficient for pre-exclusion;
> natural-language exclusion becomes effective mainly once a matching evidential state
> already exists.**

This directly explains the prospective/retrospective reversal and suggests that
exclusion is not implemented primarily as a standing future gate.

The next mechanism question is then:

> **passive gating or active target-specific revision/cancellation?**

A strong follow-up should test whether exclusion transforms an already-instantiated
target state even when no later repeated evidence arrives, and use the Stage-5 causal
window to distinguish constructive revision from mere blocked readout.

## Route C — carrier/local semantics dominate

If K cannot be made judgment-neutral, or the result depends strongly on arbitrary
carrier semantics, G22 does not license a mainline claim.

Stop and reassess. Do not rescue the paper by promoting G21 or another adjacent result.

---

# 5. G20 / G21 decision

## G21 — KILL as current mainline

Source–Proposition Scope Entanglement remains scientifically interesting, but it does
not explain why the same exclusion policy is weaker before evidence than after it.

It can become:
- a future side project; or
- a later secondary consequence **only if** the final mechanism independently predicts
  a semantic-enforcement / provenance-scope trade-off.

Do not generate G21 for the current paper.

## G20 — CONDITIONAL GO

Deferred composition is a serious mainline candidate **only if G22 first shows that
clean non-evidential target knowledge is sufficient when available before the rule**.

Do not run the current G20 design.

If Route A is supported, redesign the follow-up around one exact dependency:
correct late target resolution versus causal policy-target composition.

---

# 6. Claim architecture

An Outstanding-shaped paper does not need every paragraph to be independently novel.
The useful pattern is one broad phenomenon, one non-obvious law beneath it, and one
causal mechanism, with boundaries/supporting results around them.

## Claim 1 — broad phenomenon, established

> **Language models are systematically worse at pre-committing to exclude unseen
> evidence than at excluding the same evidence after it appears.**

Evidence:
G0 breadth, Admit control, wording/delay checks, diffusion models.

## Claim 2 — the novelty-bearing computational law, open

Final wording depends on G22:

### Route A final form
> **Exact target knowledge can support exclusion, but a target resolved after policy
> processing can be understood without reconstructing the causal exclusion relation.**

### Route B final form
> **Exact knowledge of future evidence is insufficient; effective exclusion requires an
> already-instantiated matching evidential state.**

This should be the paper's memorable second claim.

## Claim 3 — access/computation dissociation, established supporting claim

> **Knowing the policy is not the same as enforcing it: explicit policy access can
> coexist with causal leakage, while explicit symbolic future weighting can succeed.**

This isolates the failure to semantic evidence control rather than generic instruction
following.

## Claim 4 — causal mechanism, partially established

Current safe form:

> **Target availability changes a mid-network rule-time state that causally controls
> later evidence suppression.**

The final paper should sharpen this with the mechanism selected by Route A or Route B,
rather than add another generic layer sweep.

---

# 7. Exactly one experiment worth preparing now

Prepare **G22 only**.

Do not generate until the K carrier is natural enough to defend scientifically and
passes a preregistered neutrality criterion.

The load-bearing design problem is not “add more controls.” It is constructing a state
that genuinely means:

> the model knows exactly what a future record will contain, while that description is
> not itself evidence for the current judgment.

Promising carriers are typed interface / retrieval-manifest representations in which
the payload is a property of a future message or record, not a truth assertion about
the world.

A quoted paraphrase of the future evidence is risky because it may simply recreate
G18's evidential-instantiation confound.

If no natural K carrier survives a small material audit, do not run G22.

---

# 8. Experiments that should not be done now

- G21.
- ReGround / G19.
- the current G20 design.
- another semantic-specificity ladder.
- another reminder / “repeat the rule later” experiment without a demonstrated
  composition failure.
- additional model-size sweeps for optics.
- frontier/70B runs for robustness alone.
- generic provenance/source-label experiments.
- more Stage-5 layer sweeps before the behavioral branch is resolved.
- D22-A unless Route C becomes genuinely competitive.

Existing experimental breadth is already large enough. The missing quantity is not
model count; it is the second scientific descent.

---

# 9. Mechanism and method opening

The current mechanism asset should be used to answer a branch-specific causal question.

## If Route A

Mechanistic target:

> a late-resolved target is semantically understood, but the target-conditioned control
> state was compiled during an earlier window and is not reconstructed automatically.

Method opening:

> **How can a policy remain executable while unbound, then attach to a target that is
> resolved later?**

This motivates persistent/factorized policy state, late binding, explicit runtime
reference monitors, or training for control-state reconstruction.

## If Route B

Mechanistic target:

> exclusion operates by transforming an existing target/evidence state rather than by
> installing a future gate.

Method opening:

> **How can models learn genuine prospective evidence gates instead of relying on
> retrospective state revision?**

This motivates typed evidence state, persistent policy operators, or training objectives
that enforce future causal invariance.

A later source/proposition result could motivate factorizing
`(policy semantics, target semantics, provenance/scope)`, but that is not yet an
established result of this paper.

---

# 10. Literature boundary from the 2024–2026 audit

Adjacent space is already occupied by:

- **Instruction Position Matters** (ACL 2024 Findings): generic instruction-position
  effects.
- **NLSI / standing instructions** (NAACL 2024): persistent instructions and later
  applicability.
- **I3C** (NAACL 2024): identify irrelevant conditions and explicitly ignore them.
- **Chain-of-Specificity** (COLING 2025): specificity improves constraint following.
- **Racing Thoughts** (NAACL 2025): dependency-order failures and causal critical-window
  methodology.
- **Representational Analysis of Binding** (EMNLP 2024): generic binding
  representations.
- **Patches of Nonlinearity** (ACL 2026): localized instruction representations and
  nonlinear circuit selection.
- **in-context knowledge unlearning / selective forgetting** (ACL 2025 Findings):
  post-hoc forgetting/non-use mechanisms.
- **TROVE / GenProve and related provenance work**: source/provenance attribution and
  typed provenance.

This audit did **not** find an ACL/EMNLP/NAACL paper that directly isolates the exact
dependency:

> non-evidential knowledge of a future evidence target versus prior evidential
> instantiation at exclusion time,

nor the stronger conditional Route-A dependency:

> correct late target understanding without causal reconstruction of an earlier
> exclusion relation.

Treat this as current positioning, not a priority proof.

---

# 11. Outstanding-shaped bar

Before G22, the project has:
- a strong natural question;
- a broad, replicated, cross-family/cross-model phenomenon;
- unusually useful boundaries;
- a real causal mechanism asset.

What it does **not** yet have is the final non-obvious law explaining the reversal.

Therefore:

- **Route B + causal revision/cancellation evidence:** plausibly Outstanding-shaped
  scientific organization.
- **Route A + clean late-composition failure + causal backpatch/reprocessing evidence:**
  plausibly Outstanding-shaped scientific organization.
- **K merely helps and no deeper composition failure is shown:** not enough; this risks
  repeating the G18 “of course target information helps” problem.

The next generation should buy the missing law, not more confidence intervals.
