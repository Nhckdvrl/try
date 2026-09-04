# Paper frame — novelty-reset candidate

**Updated:** 2026-09-04 after the novelty audit.
**Status:** G0/G18/Stage4/Stage5 complete; new central claims are hypotheses pending G20/G21.

This file replaces the earlier "target addressability is the novelty" framing.
Historical development remains in RESEARCH_HISTORY.md and the stage files.

## 1. Natural question

> **Can a language model bind a control rule to evidence that does not yet exist—and
> keep that rule scoped to the right evidence once the target appears?**

This is stronger than asking whether "semantic descriptions help". Real policies often
precede the objects they govern, and real policies are frequently source-, document-,
or occurrence-scoped rather than proposition-global.

The paper now separates two requirements:

1. **effective binding** — the rule must actually control the later target;
2. **precise scope** — the rule must not suppress semantically equivalent evidence
   outside its intended source/occurrence.

## 2. Stable entry phenomenon

Across 12 instruction-tuned models, two masked diffusion LMs, four vendors, and five
task families, the same exclusion rule is substantially weaker when stated before the
evidence than after it. The matched Admit rule does not show the same order effect.

This remains Figure 1 and the natural empirical hook.

The paper should say:

> **Models can understand an exclusion policy yet fail to pre-commit its control to
> evidence that has not been instantiated.**

The on-policy/teacher-forced evidence supports a separation between explicit policy
access and enforcement in Qwen/Gemma; do not universalize that stronger dissociation to
every model.

## 3. G18 is now a diagnostic, not the headline explanation

G18 prospectively confirms that target semantics change exclusion:
Delta_semantic = **+8.91 [+7.15,+10.76]** rating points, positive in 5/5 models.

That result is real, but "more specific target information helps" is too obvious to
serve as the paper's main scientific novelty.

G18 matters for two deeper reasons.

### 3.1 It locates the dependency at rule time

All successful semantic previews are available **before the rule**. Combined with
Stage 5, this suggests that what matters may be whether target information exists when
the rule state is formed, not whether semantic information is present somewhere before
the final answer.

### 3.2 It reveals possible over-binding

Under paraphrase preview:
- later evidence marginal without rule ≈ +3 points;
- with exclusion ≈ **−28 points** relative to preview-only baseline.

Thus semantic grounding does not merely remove the later evidence block. It can drive
the decision below the state produced by the semantically equivalent preview itself.

This motivates a scope question:

> **Does successful semantic binding suppress the proposition beyond the specific
> evidence occurrence or source that the rule was meant to govern?**

## 4. Candidate Contribution 2 — Source–Proposition Scope Entanglement

**First priority, pending G21.**

### Claim if confirmed

> **A source-scoped exclusion rule can become proposition-scoped in effect: excluding
> Source A reduces the causal contribution of an independent, explicitly admissible
> Source B when B expresses the same proposition.**

This is tested with Source A before the policy so that target binding is already
successful. Source B arrives after the policy.

The primary metric is a redundancy-deconfounded conditional marginal:

BMarginal_no = Y(A+B) - Y(A)

BMarginal_source = Y(A+SourcePolicy+B) - Y(A+SourcePolicy)

SourceSpillover = BMarginal_no - BMarginal_source

A separate proposition-scoped policy is the positive control. High lexical overlap
with a different proposition and unrelated-but-relevant B are semantic controls.

The strongest pattern is:
- A itself is successfully excluded;
- B has measurable conditional leverage under no policy;
- source-scoped policy removes B leverage only for semantic-equivalent B;
- proposition-scoped policy removes B as expected;
- an explicit post-B reminder that B remains admissible does not fully restore it;
- a separate scope probe can still report that B is allowed.

That would establish a causal **scope-enforcement failure**, not mere provenance
confusion or semantic redundancy.

## 5. Candidate Contribution 3 — Dynamic Late Binding

**Second priority, pending strengthened G20.**

### Claim if confirmed

> **Even when the model can identify a late-revealed target before decision time,
> exclusion may still depend on whether target resolution preceded rule processing;
> replaying the identical rule after target revelation selectively restores control.**

This claim is deliberately stronger than "earlier rule states cannot see later
tokens", which is trivial in decoder-only Transformers.

G20 qualifies only if:
- a full-context probe shows the late target mapping is understood;
- matched Admit/arithmetic/routing late-binding controls succeed;
- PRE target > LATE target for exclusion;
- replay selectively repairs LATE rather than acting as generic recency;
- at least one masked-diffusion model with bidirectional prompt attention preserves the
  pattern.

Without these properties, G20 should not become a central claim.

## 6. Higher-level hypothesis — under-binding vs over-binding

If G21 and the strengthened G20 both pass, the paper has a substantially stronger abstraction:

> **LLMs face a binding–scope trade-off in prospective evidence control.**

### Under-binding
Without an instantiated target at rule time, the control relation is weak and later
evidence leaks.

### Over-binding
With enough semantic target information, the control relation becomes strong but can
lose provenance/occurrence precision and spread to the proposition.

The scientific problem is therefore not "how to make a rule more specific". It is:

> **Can a model establish a future control relation that is both strong and
> correctly scoped?**

## 7. Mechanism

The existing Stage 5 result remains important.

Matched success/failure conditions show:
- a target-dependent causal rule state in the middle of the network;
- it exists before later evidence is processed;
- transplanting it changes subsequent suppression;
- the localization replicates in Qwen3-8B and Mistral-Small-24B.

Under the new framing this supports:

> **the critical computation occurs when the rule is processed, before later evidence
> integration.**

It does not yet prove:
- that later target revelation cannot update the policy;
- that the state ignores provenance scope.

Those are exactly what G20/G21 test.

If G21 passes, one follow-up mechanism round may test whether causal control tracks
Source-B proposition content more strongly than Source-B provenance/label identity.
Do not run that mechanism before the behavior exists.

## 8. Agent relevance

The earlier D7→D9 agent result is reinterpreted.

Old reading:
> semantic policy generalization is useful because it follows the proposition.

New reading:
> the model's control naturally follows semantic identity across document identity,
> which may be either desirable or a **scope error**, depending on whether the policy
> was proposition-scoped or source-scoped.

G21's agent transfer should therefore use an explicitly source-scoped policy and an
independent allowed D9 source.

## 9. What is explicitly removed

Do not center:
- "Target Addressability Governs Prospective Exclusion";
- "semantic targets outperform identifiers";
- ReGround as a novel method;
- generic post-retrieval rule restatement;
- a universal semantic binding vector.

These may appear as supporting history, diagnostics, or cancelled designs.

## 10. Literature-facing positioning

The new space is intentionally between several occupied literatures:

- instruction position / multi-constraint order: studies where instructions are
  placed, not whether target resolution crosses a rule-processing boundary;
- prospective memory: studies whether deferred instructions are remembered, not
  whether an unresolved rule can be late-bound after its target appears;
- entity binding: studies entity–attribute association, not binding of control rules
  to future evidence;
- instruction vectors: studies localized instruction states, not whether later target
  information can update them;
- provenance/source attribution: studies where claims came from, not whether
  source-scoped exclusion spreads across semantically equivalent evidence;
- negative output constraints: studies forbidden output generation, not source- and
  occurrence-scoped causal evidence use.

## 11. Candidate final arc

Can models pre-commit what later evidence should not matter?
    ↓
Broadly, no: prospective exclusion is weaker than retrospective exclusion.
    ↓
Why? A rule may have a **binding deadline**: target resolution after rule processing
does not reliably rebind it, even before the evidence arrives.
    ↓
But successful semantic binding introduces a second failure:
**scope collapse** can spread exclusion from one evidence instance/source to the
proposition.
    ↓
A target-dependent mid-network rule state forms before evidence integration and
causally controls later suppression.
    ↓
The resulting scientific object is not prompt specificity; it is the ability to bind
future control **strongly and precisely**.

## 12. Programme status

ReGround G19 is cancelled before generation.

Active work:
1. build/audit/freeze **G21 Source–Proposition Scope Entanglement first**;
2. freeze the strengthened G20 independently before seeing G21 if feasible;
3. run no new mechanism, breadth or mitigation round until at least one new behavioral phenomenon qualifies.
