# Related work — deferred evidence control

The paper asks one central question:

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

The current candidate explanation is narrower:

> **When target semantics are unavailable at exclusion-rule processing time, can the
> model later compose the already-processed exclusion operator with a target that is
> resolved before the governed evidence arrives?**

This avoids three occupied/obvious claims:
- later instructions can be easier to follow;
- more specific semantic constraints can help;
- identifying irrelevant information and then telling the model to ignore it can
  improve performance.

G21 source/proposition scope is retained only as future-work provenance and is not part
of the current novelty position.

## 1. Generic instruction position and order are occupied

### Instruction Position Matters — ACL 2024 Findings
https://aclanthology.org/2024.findings-acl.693/

Moving task instructions after the input can improve sequence-generation instruction
following, motivated by instruction locality/forgetting.

Implication:
our G0 sign alone is not novel.

### Order Matters — ACL 2025 Findings
https://aclanthology.org/2025.findings-acl.646/

Shows strong position bias in multi-constraint instruction following and a hard-to-easy
order advantage.

Implication:
“order matters” is not sufficient as our claim.

Our stronger variable is the ordering of **target semantic resolution** and the
**exclusion operator**, with a downstream checkpoint where both are already available.

## 2. Constraint specificity is occupied

### Chain-of-Specificity — COLING 2025
https://aclanthology.org/2025.coling-main.164/

Emphasizing/refining specific constraints improves adherence.

Implication:
“make the target more specific” cannot be our headline.

G18 is therefore factorization evidence:
pre-rule target semantics alter exclusion, but the novelty comes from whether the same
semantics can be integrated **after** the rule.

## 3. Identify-then-ignore is occupied

### I3C — NAACL 2024 Main
https://aclanthology.org/2024.naacl-long.379/

I3C identifies candidate irrelevant conditions, verifies them, and then explicitly
instructs the model to ignore them.

Implication:
post-hoc identification plus explicit ignore instruction is occupied in spirit. This is
why ReGround G19 remains cancelled.

Our question is earlier:
can a rule remain executable while its target is unresolved?

## 4. Prospective memory is adjacent but different

### TriggerBench — 2026
https://arxiv.org/abs/2606.23459

Evaluates whether models spontaneously recall and act on latent future-triggered
constraints. It finds prospective memory harder than retrospective memory and sensitive
to context/interference.

### Did You Forget What I Asked? — 2026
https://arxiv.org/abs/2603.23530

Studies deferred formatting constraints under concurrent task load and shows trailing
reminders can restore compliance.

Our distinction:

> the exclusion rule can remain accessible, and the late target can be correctly
> recognized, yet the model may still fail to create the causal non-use relation.

Thus our object is not merely memory of the instruction or trigger detection. It is
**deferred control composition**.

## 5. In-context forgetting studies the opposite chronology

### Do LLMs Forget What They Should? / ICF-Bench — ICLR 2026
https://proceedings.iclr.cc/paper_files/paper/2026/hash/b13d00a62d438856cfe6fbd13b6b2cb8-Abstract-Conference.html

Defines in-context forgetting as selectively discarding already-present information in
multi-turn dialogue. Its instructional-forgetting example has:

```
information appears → later forget instruction → query
```

This is important adjacent work, but its chronology is retrospective.

Our entry phenomenon is explicitly:

```
forget/exclude instruction → later evidence appears → decision
```

and compares it against the retrospective arrangement.

Therefore do not claim “first in-context forgetting.” The missing question is
pre-commitment before the governed evidence exists.

## 6. Generic binding is occupied

### Representational Analysis of Binding in Language Models — EMNLP 2024 Main
https://aclanthology.org/2024.emnlp-main.967/

Studies entity–attribute Binding IDs and localizes a low-rank binding subspace.

### Cell-Based Representation of Relational Binding — ACL 2026 Main
https://aclanthology.org/2026.acl-long.2194/

Extends binding analysis to entity–relation cells with causal representation editing.

Our distinction:
we do not claim to discover binding in general.

The relevant relation is:

```
EXCLUDE operator ↔ semantic evidence target
```

and the question is temporal:
can that relation be created **after** the operator has already been processed?

Use phrases such as:
- deferred control composition;
- target-conditioned control;
- operator–target composition.

Avoid “first binding mechanism.”

## 7. Instruction representations are occupied

### Patches of Nonlinearity — ACL 2026 Main
https://aclanthology.org/2026.acl-long.559/

Localizes instruction representations and shows non-linear causal interaction;
instruction vectors can act as circuit selectors conditioned on task representations.

Implication:
Stage 5's mid-layer state is not novelty by itself.

Our mechanism matters only if it touches the new dependency:
- target-first vs rule-first;
- after both target and rule are available;
- causal persistence of the order-dependent control state.

## 8. Dependency-order mechanisms: closest conceptual neighbor

### Racing Thoughts — NAACL 2025 Main
https://aclanthology.org/2025.naacl-long.155/

Explains contextualization errors through a race-condition hypothesis: one computation
must finish before a dependent computation integrates its result.

This is the closest conceptual prior.

Our candidate dependency is distinct:

> **target semantic resolution must be composed with an exclusion operator; when the
> operator is processed first, later target resolution may fail to reconstruct the
> effective control state.**

The redesigned G20 uses a **post-resolution checkpoint** where both operands are
available. A causal state difference there is stronger than the trivial statement that
an earlier decoder token cannot see later input.

Position this as a new control dependency, not as the first order-sensitive computation
in LLMs.

## 9. Negative constraints

### Semantic Gravity Wells — 2026
https://arxiv.org/abs/2601.08070

Studies negative output constraints, including priming of forbidden tokens and late
override of suppression signals.

Our distinction:
the governed object here is not a generated token but the **causal contribution of
contextual evidence to a judgment**.

Existing arithmetic and Admit controls further distinguish semantic evidence
nullification from generic negative wording.

## 10. Distraction / irrelevance mechanisms

### Llama See, Llama Do — ACL 2025 Outstanding
https://aclanthology.org/2025.acl-long.791/

Turns broad distraction into contextual entrainment and causally identifies relevant
attention heads.

Narrative lesson:
“models use evidence they should not” is not enough. The paper needs a sharper
computational regularity.

Our candidate regularity:
**target/operator composition is history-dependent and exclusion-specific.**

### Do LLMs Know Tool Irrelevance? — ACL 2026 Main
https://aclanthology.org/2026.acl-long.1473/

Factorizes tool refusal into structural alignment versus semantic relevance and finds
competing causal pathways.

Narrative lesson:
the factorization must expose a non-obvious dependency, not simply add robustness.

## 11. Policy and instruction hierarchy

### IHEval — NAACL 2025 Main
https://aclanthology.org/2025.naacl-long.425/

Evaluates conflicts across system/user/history/tool instruction hierarchy.

### COMPASS — ACL 2026 Main
https://aclanthology.org/2026.acl-long.2139/

Evaluates organization-specific allowlist/denylist compliance and finds large
prohibition failures.

These occupy:
- general policy following;
- denylist failure;
- authority conflicts.

Our novelty cannot be “models fail policies.”

Our question is:

> when a valid exclusion policy precedes its target, does the model preserve it as a
> deferred executable relation, or does effective control depend on target semantics
> already existing when the policy is processed?

## 12. Provenance/source work — secondary relevance only

### TROVE — ACL 2025 Main
https://aclanthology.org/2025.acl-long.577/

### GenProve — ACL 2026 Main
https://aclanthology.org/2026.acl-long.228/

### MemIR — 2026
https://arxiv.org/abs/2605.25869

These establish substantial prior work on provenance tracking, source-role separation,
and provenance-aware generation.

Because G21 is no longer the paper center, do not spend main-text novelty budget
distinguishing source-scope collapse from all provenance literature.

Use provenance only to motivate practical settings where evidence identity matters.

## 13. Exact novelty position after the audit

Do not claim:
- first instruction-order effect;
- first prospective-memory failure;
- first in-context forgetting work;
- first binding mechanism;
- first policy-following failure;
- first provenance-aware evidence control;
- first result that semantic specificity helps.

The candidate missing dependency is:

> **Whether exclusion control can be deferred across target resolution: after an
> exclusion operator is processed with no semantic target instantiated, can a model
> later recognize that target and reconstruct the same causal evidence-suppression state
> before the evidence arrives?**

The strongest evidence would combine:
1. correct late-target comprehension;
2. target-first > rule-first exclusion;
3. selective exclusion-rule replay rescue;
4. successful late composition in Admit/arithmetic/routing controls;
5. a shared post-resolution checkpoint whose state remains causally order-dependent.

Targeted search has not identified an ACL/EMNLP/NAACL/ICLR work directly isolating
this exact dependency. Treat that as literature positioning, not proof of priority.
Write “we study” rather than “we are the first.”

## 14. Cancelled / downgraded branches

### ReGround G19
Cancelled before freeze/generation. Too close to identify-then-ignore / ordinary policy
evaluation to serve as a method novelty.

### G21 Source–Proposition Scope Entanglement
Retained as future-work provenance. Potentially interesting, but not a natural
explanation of G0 and therefore not a current paper contribution.
