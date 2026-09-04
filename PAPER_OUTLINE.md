# Paper outline — novelty-reset version

**Updated:** 2026-09-04.
**Status:** G20/G21 pending; this is the intended paper shape if the new hypotheses survive.

## Working title candidates

Primary candidate:
> **Can Language Models Bind Rules to Evidence They Have Not Seen?**

If scope collapse becomes the strongest result:
> **When Ignoring a Source Makes Models Ignore the Fact**

More technical:
> **Binding Deadlines and Scope Collapse in Prospective Evidence Control**

Avoid "Target Addressability" in the title. It is now a diagnostic phrase, not the
paper identity.

## Abstract structure

1. Policies can precede their evidential targets.
2. Broad result: exclusion-before-evidence is systematically weaker than identical
   exclusion-after-evidence across 12 instruct + 2 diffusion models / five families.
3. Policy availability alone does not explain the effect.
4. **If G20 passes:** reveal the same target semantics after rather than before rule
   processing; later revelation fails, while replaying the rule after target revelation
   restores exclusion → binding deadline.
5. **If G21 passes:** successful semantic binding can suppress an independently
   admissible source expressing the same proposition → source/provenance scope collapse.
6. Existing Qwen+Mistral interchange localizes a target-dependent causal rule state
   before evidence integration.

Do not write "semantic target descriptions improve exclusion" as the abstract novelty.

---

# 1. Introduction

Opening problem:

> Policies often exist before the objects they govern. A reliable model must not only
> remember the rule; it must bind the rule when its future target becomes available
> and preserve the intended scope.

Natural examples:
- system policy before retrieval;
- exclusion of a source before testimony arrives;
- memory/tool governance before the actual record is fetched.

Two requirements:
- **binding strength**
- **scope precision**

Question:
> **Can LLMs establish a future control relation that is both strong and precisely
> scoped?**

Contribution list is conditional:
1. broad prospective exclusion paradox;
2. source–proposition scope entanglement (G21 if confirmed);
3. dynamic late-binding failure (G20 if confirmed);
4. causal mid-network rule state.

G18 is mentioned as the diagnostic that motivated 2–3, not as a contribution called
"semantic targets help".

---

# 2. Experimental setup

## 2.1 G0 broad set
144 frozen items / five families.

Conditions:
- Base
- Admit-before / after
- Exclude-before / after

Readout:
continuous 0–100 digit expectation / REI for stable G0 anchors.

## 2.2 Fresh G20 set
Planned:
- 120 items
- 36 skeletons
- three families
- semantic target block P and matched unrelated U
- P/U token-length matching across tested tokenizers

## 2.3 Fresh G21 dual-source set
Planned:
- ~100 items
- 30–36 skeletons
- three families
- excluded Source A
- independently admissible Source B
- semantic relation manipulation between A and B

Use raw sign-aligned rating points for new experiments.

---

# 3. A paradox of prospective exclusion

**Figure 1.**

Show:
- 12 instruct models: Exclude-before vs Exclude-after
- Admit control
- optional diffusion inset

Claim:
> **Models are worse at pre-committing to exclusion than at excluding the same
> evidence after seeing it.**

One compact paragraph:
- separate rule probe;
- on-policy Qwen/Gemma dissociation;
- distance/wording/diffusion controls.

Do not turn the section into "not memory, not position, not wording..." lists.

Boundary paragraph:
explicit arithmetic future weighting can succeed, so this is not generic inability to
compose any prior rule with later input.

---

# 4. G18 diagnostic — semantic target information changes control

Keep this section short.

Report:
- 100 fresh items / 30 skeletons / 3 families / 5 models
- Delta_semantic +8.91 [7.15,10.76], 5/5 positive
- para-empty +12.85 [10.32,15.42]

Then immediately say:

> This result by itself is not the explanation: more specific target information
> helping is unsurprising. Two aspects are scientifically informative.

Aspect 1:
successful target information is available before rule processing.

Aspect 2:
semantic preview + exclusion produces below-preview-baseline suppression
(marg≈−28), suggesting possible scope spillover.

This section exists to motivate G20/G21.

---

# 5. Source–Proposition Scope Entanglement

**First priority; only a main-text claim if G21 confirms it.**

**Figure 2.**

Source A appears before a source-scoped policy. Independent Source B appears after it.

Policy:
> Only Source A is excluded. Source B remains fully admissible, including when it
> independently supports the same proposition.

B semantic relation:
- paraphrase;
- entailment;
- gist;
- lexical-overlap wrong proposition;
- unrelated decision-relevant control.

A proposition-scoped policy is the positive control.

### 5.1 Main metric

Use conditional marginals to remove A/B redundancy:

BMarginal_no = Y(A+B) - Y(A)

BMarginal_source = Y(A+SourcePolicy+B) - Y(A+SourcePolicy)

SourceSpillover = BMarginal_no - BMarginal_source

Do **not** use B-alone leverage as the primary baseline.

### 5.2 Strong tests
- A itself must be successfully excluded.
- B must have measurable conditional no-policy leverage.
- semantic-equivalent B should show more SourceSpillover than lexical-wrong/unrelated.
- proposition-scoped policy should suppress B as expected.
- post-B "B remains admissible" reminder tests whether declarative scope can restore
  causal scope.
- separate scope probe asks whether the model knows B is allowed.

Claim if confirmed:

> **A source-scoped exclusion rule becomes proposition-scoped in effect: the model
> discounts an allowed independent source because it says the same thing as the
> excluded source.**

### 5.3 Agent transfer

SYSTEM: D7 excluded; D9 explicitly allowed.
TOOL D7: proposition p.
TOOL D9: independent paraphrase p or lexical-wrong control.

Measure D9's conditional marginal contribution.

---

# 6. Dynamic Late Binding

**Second priority; only a main-text claim if strengthened G20 confirms it.**

The claim is not that earlier causal hidden states cannot see later tokens.

**Figure 3.**

PRE:
P → rule → U → evidence

LATE:
U → rule → P → evidence

Same P/U/rule/evidence; same information before final decision.

### 6.1 Mandatory comprehension
Full-context probe must show that the model correctly knows what the late-resolved
target is.

### 6.2 Rule replay
LATE+REPLAY vs PRE+REPLAY with identical second rule and matched neutral slots.

The critical result is a **selective LATE replay rescue**.

### 6.3 Positive late-binding controls
- Admit;
- arithmetic;
- use/select routing.

### 6.4 Architecture control
Dream/LLaDA become load-bearing. At least one bidirectional model should preserve the
core pattern for a strong computational claim.

Claim if confirmed:

> **The model can identify a late-resolved target but still fails to dynamically
> attach an earlier exclusion policy to it; reprocessing the rule restores control.**

# 7. Mechanism

**Figure 4.**

## 7.1 Existing evidence
- evidence-span gate: residual excluded evidence is causally read;
- answer-position patching: final gating resolved late;
- rule-span matched-chronology interchange: target-dependent causal state in mid layers.

Qwen:
L14–18 / 36.

Mistral:
L12–16 / 40.

Claim:
> **A target-dependent control state forms during rule processing and causally
> determines later evidence suppression.**

This is already established.

## 7.2 Conditional mechanism follow-up

If G20:
test whether late target revelation fails to reconstruct the successful rule state and
whether rule replay reconstructs it.

If G21:
test content-vs-provenance causal contributions to Source-B suppression.

No new mechanism before behavioral confirmation.

---

# 8. Discussion

## 8.1 Beyond instruction position
The critical variable is not simply where the rule appears, but whether its target has
been resolved by the time control computation is formed.

## 8.2 Beyond prompt specificity
Semantic information is not unconditionally beneficial: it may trade binding strength
for scope precision.

## 8.3 Provenance matters
Policy systems often govern sources, documents, users, time windows or evidence
occurrences. Proposition-level generalization can therefore be a failure rather than a
feature.

## 8.4 Architectural implication
If G20 survives diffusion models, the binding deadline is a learned computational
strategy, not merely a causal-attention impossibility.

---

# 9. Related work

Organize around occupied questions:

1. instruction position / multi-constraint order
2. prospective memory
3. negative constraints
4. entity–attribute binding
5. instruction vectors / causal instruction states
6. provenance and source attribution
7. context distraction / contextualization mechanisms

Positioning:

> Prior work asks where instructions should be placed, whether they are remembered,
> how entities are bound, or whether evidence provenance can be recovered. We study a
> different control problem: **whether a rule can be late-bound to a future evidential
> target and whether successful semantic binding preserves the source/occurrence scope
> of that rule.**

---

# 10. Limitations

Before new results:
- G20/G21 are pending and must not be written as findings.
- controlled authored tasks;
- on-policy access/enforcement dissociation is heterogeneous;
- existing mechanism is on two architectures;
- G18 over-suppression currently has multiple possible readings.

After G20/G21:
update based on actual outcome, not intended narrative.

---

# Main figure hierarchy

Figure 1 — prospective exclusion paradox

Figure 2 — source–proposition scope entanglement / allowed-source conditional retention (if confirmed)

Figure 3 — dynamic late binding / rule replay interaction (if confirmed)

Figure 4 — Qwen+Mistral causal rule state

G18 factorial becomes a compact bridge panel or appendix unless one of its
decomposition plots is needed to motivate Figure 3.

---

# Appendix

- full G0 model×family tables
- wording / distance / delay
- weight and arithmetic boundaries
- full G18 factorial and decomposition
- Stage 3D content×identity
- Stage 3E redundancy
- tagged streams
- on-policy trajectories
- Stage 4 old D7→D9 tables
- G16/G17
- failed shared steering direction
- cancelled ReGround G19 design as repository provenance, not a paper experiment

The main text must not read like the chronological experiment ledger.
