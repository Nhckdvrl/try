# Paper mainline draft — prospective semantic exclusion

**Updated:** 2026-09-23.  
**Status:** current mother draft after G23A and the stopped G23B v1 branch.  
**Target:** ACL / EMNLP / NAACL Main.

---

## 0. Core question

> **Can language models commit in advance to ignore evidence they have not yet seen?**

Real systems often specify policies before the information those policies govern:
admissibility rules before testimony, system policy before retrieval, or agent
constraints before tool output.

A model that can maintain an executable standing policy should apply the same rule when
the target arrives later.

Empirically, this is systematically difficult.

---

## 1. Prospective exclusion reversal

Across the original broad panel, an exclusion rule is weaker when stated before its
evidence than when stated after the same evidence.

Matched Admit controls do not show the analogous order effect.

> **Prospective exclusion is systematically harder than retrospective exclusion.**

---

## 2. Controls: the gap is not just forgetting

Several controls make generic instruction forgetting insufficient:

- long delay does not remove the specific asymmetry;
- multiple rule wordings preserve it;
- Admit lacks the same order effect;
- models can separately state the intended exclusion policy;
- prospective arithmetic zeroing can be executed exactly.

The failure therefore lies between **knowing the policy** and **making later semantic
evidence causally inert**.

---

## 3. Semantic causal zero has an extra prospective cost

G23A freezes the strongest clean behavioral law:

`Δ_zero = +8.83 [+4.39,+13.33]` rating points.

The non-zero instruction gap is also positive, so this is not “only zero fails.”

The frozen G23A result alone is not the novelty claim: a reviewer could reasonably say
that requesting exactly zero influence is stricter than requesting partial influence.

The non-trivial contrast is with the explicit/verifiable controls:

> **Prospective zero can be executed exactly when the contribution is explicit and
> verifiable, while complete semantic evidence exclusion still incurs an additional
> prospective cost.**

The scientific object is therefore **semantic causal zero**, not the numeral 0 itself.

---

## 4. A tempting behavioral explanation could not be identified

A natural explanation was that retrospective exclusion can act on an already existing
evidence state, whereas prospective exclusion must maintain a pending gate.

G23B attempted to separate exact semantic knowledge from evidential instantiation using
a natural legal proffer.

The carrier failed before any branch outcome was generated:

`ProfferLeak = +8.07 [+4.86,+11.23]`.

Thus the experiment does not distinguish standing gating from cancellation. More
importantly, it shows why that factorization is difficult: putting the exact semantic
payload in context already changes the merits judgment despite explicit instructions
that it is not evidence.

The paper should report this as an identification failure, not turn it into a result for
either mechanism.

---

## 5. Existing causal evidence

Stage 5 avoids the Pre/Post chronology confound.

Both success and failure runs place the actual evidence after the zero-use rule. They
differ only in whether a matching proposition is available before the rule.

In Qwen3-8B and Mistral-Small-24B, a mid-network rule-time state is causally involved:
swapping the failing state into a successful run strongly destroys later suppression,
and successful-state transfer can rescue suppression.

This is before the later decision evidence is processed.

Current safe interpretation:

> **successful prospective exclusion depends on a target-conditioned causal state formed
> during rule processing.**

But Stage 5 alone does not show that this state carries the policy value itself.

---

## 6. Mechanistic support: rule-time policy state

G23C prospectively tested whether the Stage-5 rule-time state carries the policy value
with stronger causal efficacy when the semantic target is available.

Frozen primary result:

```text
PolicyTransfer_M = +13.03 [+11.69,+14.31]
PolicyTransfer_U =  +4.89 [ +3.73, +6.18]
TargetConditioning = +8.15 [ +6.91, +9.44]
```

Both model-level target-conditioning means are positive. The same pattern is absent at
the frozen negative layers L4 and L24, and identity patches are exact.

G24B subsequently fixes the recipient prompt and still finds a positive donor-side
interaction at L14:
`DonorTargetInteraction = +4.02 [+2.27,+6.14]`.

These interventions establish that the rule-time state participates causally in later
suppression and that target context changes its transportable policy effect.

However, this is **supporting mechanism evidence**, not a third headline novelty claim:
the matched condition visibly contains matching target semantics before the rule, so a
reviewer can reasonably expect the resulting state to be more target-specific.

Do not present “target present -> more target-conditioned policy state” as an independent
contribution.

---

## 7. Current contribution structure

### Headline Finding 1

> **Prospective evidence exclusion is systematically weaker than retrospective
> exclusion, and source-grounded natural evidence can still leak under a prior zero-use
> ruling.**

G24A must be reported with its exact scope: pooled prospective leak passed, while the
retrospective endpoint did not; cross-model/source consistency was not uniform.

### Headline Finding 2

> **Semantic causal zero is disproportionately difficult prospectively even though
> future zero can be executed exactly for explicit/verifiable contributions.**

G23A provides the zero amplification; exact arithmetic/numeric controls provide the
critical non-obvious boundary.

### Supporting controls

“Policy access != enforcement” belongs here. It rules out forgetting but is not itself
novel enough to headline.

### Supporting mechanism

Stage 5 / G23C / G24B provide causal internal evidence. They explain the behavioral
findings but are not counted as a third contribution under the current novelty audit.

### Open slot

A third headline RQ is optional. Add one only if it survives the reviewer-obvious veto.
Do not manufacture one to satisfy a preferred section count.

---

## 8. Positioning

The paper is not primarily:
- instruction placement;
- belief revision;
- knowledge unlearning;
- a function-vector paper.

Those works respectively ask where instructions should occur, how beliefs change,
whether knowledge can be suppressed, or whether task functions are encoded in latent
states.

Our object is:

> **whether a policy can prospectively control the causal eligibility of future semantic
> evidence, and what state makes that control executable.**

---

## 9. Working title

Primary:

> **Can Language Models Commit to Ignore Future Evidence?**

Do not use a subtitle centered on “target-conditioned policy state.” That mechanism
claim is now supporting evidence rather than the paper's novelty center.


---

## 10. Current next step

Do **not** run G23C-R yet.

First perform a novelty search for a genuinely non-obvious third question growing from
RQ1/RQ2. If none survives, write the paper around the two headline findings and use
Stage 5/G23C/G24B as mechanistic support.

G23C-R remains a parked replication design and requires a new authority decision before
compute.
