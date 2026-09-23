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

## 2. The gap is not just forgetting

Several controls make generic instruction forgetting insufficient:

- long delay does not remove the specific asymmetry;
- multiple rule wordings preserve it;
- Admit lacks the same order effect;
- models can separately state the intended exclusion policy;
- prospective arithmetic zeroing can be executed exactly.

The failure therefore lies between **knowing the policy** and **making later semantic
evidence causally inert**.

---

## 3. Complete exclusion has an extra timing cost

G23A freezes the strongest clean behavioral law:

`Δ_zero = +8.83 [+4.39,+13.33]` rating points.

The non-zero instruction gap is also positive, so this is not “only zero fails.”

The correct result is:

> **Prospective processing has a generic timing cost, and the cost is discontinuously
> larger when the requested evidential weight is exactly zero.**

This makes complete semantic exclusion a distinctive control problem rather than just a
generic instruction-position effect.

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

## 6. G23C closes the mechanism loop

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

Therefore the mechanism statement is:

> **The causal efficacy of the rule-time zero-vs-full policy state is
> target-conditioned.**

This directly connects the broad prospective exclusion failure and the zero-amplified
behavioral boundary to a mid-network causal state formed before later evidence is read.

The claim is deliberately narrower than “the target×policy conjunction is stored in one
hidden vector.” Recipient context and downstream computation may still contribute.

---

## 7. Current claims after G23C

### C1
Prospective exclusion is systematically weaker than retrospective exclusion.

### C2
The asymmetry is not reducible to simple policy forgetting.

### C3
The prospective timing cost is discontinuously amplified at complete exclusion.

### C4
When target semantics are available during policy processing, exchanging the mid-network
rule-time zero-vs-full policy state has a substantially larger causal effect on later
evidence use.

No stronger claims are needed.

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

Possible subtitle:

> **Prospective Evidence Exclusion Depends on Target-Conditioned Policy State**

Use cautiously until G23C-R finishes; the primary title remains safer.


---

## 10. Final confirmatory round — G23C-R

G23C-R repeats only the G23C mechanism result on a fresh frozen material set:
70 G18 legal/inference items, 20 skeletons, all disjoint from the Stage-5 discovery
materials.

It uses the same two models, direct readout, rule-end site, L4/L14/L24, bridge and
target-conditioning gates.

This is a robustness replication, not a new scientific branch. No later mechanism round
is planned regardless of outcome.
