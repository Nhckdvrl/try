# Paper frame — prospective semantic exclusion

**Updated:** 2026-09-23 after G23A success and G23B carrier failure.  
**Target:** ACL / EMNLP / NAACL Main.  
**Authoritative evidence ledger:** [SCIENTIFIC_REGISTER_2026-09-04_V3.md](SCIENTIFIC_REGISTER_2026-09-04_V3.md)

The paper has one natural question:

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

The current paper is **not** a “standing gate vs retrospective cancellation” paper.
G23B v1 could not identify that binary because its exact-semantic non-evidential carrier
was behaviorally invalid.

The paper-level object is:

> **prospective semantic evidence exclusion under a zero-use policy.**

---

## 1. C1 — the broad phenomenon

Across the original G0 breadth panel, the same exclusion rule is systematically weaker
when stated before evidence than after evidence.

Matched Admit controls do not show the analogous order effect.

Headline:

> **Models are worse at pre-committing to exclude unseen evidence than at excluding the
> same evidence after it appears.**

This remains Figure 1 and the paper's natural hook.

---

## 2. C2 — not simple instruction forgetting

The existing controls rule out the easy compression “the model just forgot the earlier
instruction”:

- the asymmetry survives substantial rule-to-evidence delay;
- it survives wording changes;
- matched Admit does not show the same pattern;
- separate policy probes can recover the intended zero policy while behavior still
  leaks;
- explicit prospective arithmetic zeroing can succeed.

Safe claim:

> **Declarative access to the policy is not sufficient for causal enforcement.**

---

## 3. C3 — zero amplifies the prospective timing cost

G23A v3 is the clean new behavioral law.

Frozen result:

`Δ_zero = Gap(0) - mean[Gap(1),Gap(25),Gap(50)] = +8.83 [+4.39,+13.33]`

All preregistered gates passed and all three model-level deltas were positive.

The non-zero instruction gap itself is also positive:

`mean[Gap(1),Gap(25),Gap(50)] = +5.03 [+3.16,+6.83]`.

Therefore the licensed law is:

> **There is a generic prospective timing cost, plus a discontinuous additional cost
> at the zero-valued instruction.**

Do not strengthen this into “non-zero numerical weighting is correctly implemented.”
The numeric probes show requested-policy access, not behavioral linear weighting.

---

## 4. C4 attempt — G23B failed as an identification strategy

G23B tried to separate:

- U: future target unresolved;
- K: exact semantics known but supposedly non-evidential;
- I: evidence already instantiated.

Its Phase-A carrier failed before any U/K/I rule outcome was generated:

`ProfferLeak = +8.07 [+4.86,+11.23]`.

All three model means exceeded the +3 point neutrality floor.

Therefore:

> **G23B is carrier-invalid, not evidence for standing gating or retrospective
> cancellation.**

The failure is scientifically useful because it exposes an identification problem:
placing the full proposition in natural-language context can already make it
behaviorally evidential even when the prompt explicitly says otherwise.

Do not immediately search over alternative proffer wording.

---

## 5. C5 — existing causal mechanism asset

Stage 5 uses matched chronology:

```text
FAILURE  unrelated preview -> zero rule -> evidence -> answer
SUCCESS  matched preview   -> zero rule -> evidence -> answer
```

Both conditions process the decision evidence after the rule.

Qwen3-8B and Mistral-Small-24B independently show a mid-network rule-time causal window.
Transplanting the failing state into the successful run strongly breaks later
suppression; successful-state rescue is strong in Mistral and smaller but non-zero in
Qwen.

Safe current claim:

> **What target state is available while the exclusion rule is processed changes a
> causal rule-time state that later affects evidence suppression.**

What remains unresolved is whether this state actually carries the **policy value for
that target**, or merely a generic target/context readiness state.

---

## 6. Current paper spine

The paper should now read:

```text
Natural problem:
Can an LLM commit now to ignore evidence that arrives later?

        ↓

C1 — G0
Prospective exclusion is systematically weaker than retrospective exclusion.

        ↓

C2 — controls
The gap is not reducible to simple instruction forgetting or inability to represent 0.

        ↓

C3 — G23A
The timing cost is discontinuously amplified at w=0.
Generic timing cost + extra complete-exclusion cost.

        ↓

C5 — Stage 5
Target availability during rule processing changes a mid-network causal state
before later evidence is read.

        ↓

Missing link
Does that state carry an executable target × policy relation?
```

That missing link is G23C.

---

## 7. G23C — completed mechanism link

Frozen verdict: **`target-conditioned-policy-state`**.

Key result at the preregistered primary site/layer:

```text
PolicyTransfer_M = +13.03 [+11.69,+14.31]
PolicyTransfer_U =  +4.89 [ +3.73, +6.18]
TargetConditioning = +8.15 [ +6.91, +9.44]
```

The same target-conditioning pattern is absent at the frozen negative layers:
L4 ≈ `-0.03`, L24 ≈ `+0.07`.

Identity patches reproduce the recipient exactly (max absolute delta 0.0).

The strongest safe mechanism statement is:

> **The causal efficacy of the rule-time zero-vs-full policy state is substantially
> stronger when the target proposition is available during policy processing.**

This closes the main mechanistic link between G23A and Stage 5.

It does **not** prove that the complete target×policy conjunction is localized in one
token state; downstream context may still participate in the interaction.

### Final replication

The only remaining mechanism round is G23C-R:
[preregistrations/PREREGISTRATION_G23C_R_FRESH_REPLICATION.md](preregistrations/PREREGISTRATION_G23C_R_FRESH_REPLICATION.md)

It repeats the exact G23C intervention on 70 frozen G18 legal/inference items from
20 skeletons that are disjoint from the Stage-5 discovery materials.

No G23C-R compute is authorized yet. Regardless of its outcome, no automatic G23D
follows.

---

## 8. Nearest-prior compression audit

### Generic instruction position

“Instruction Position Matters in Sequence Generation with Large Language Models”
(Findings ACL 2024) studies instruction forgetting / placement in translation and
summarization.

Reviewer compression:
> “This is just earlier instructions being weaker.”

Our answer:
- Admit control;
- policy-access probes;
- arithmetic future-zero control;
- G23A zero discontinuity;
- target-conditioned rule-time causal state.

### Belief revision

“Belief Revision: The Adaptability of Large Language Models Reasoning”
(EMNLP 2024 Main) asks whether new evidence should change a belief.

Our object is different:
the evidence may remain true and understood; the question is whether it is **allowed to
causally contribute** to a separate decision.

### In-context unlearning / reversing edits

Pawelczyk et al. (ICML 2024), Takashiro et al. (Findings ACL 2025), and Youssef et al.
(NAACL 2025) study removing knowledge influence, selective forgetting, or reversing an
existing in-context edit.

Our object is not knowledge availability:
it is **prospective control of the causal eligibility of future evidence**.

### Racing Thoughts

Lepori et al. (NAACL 2025) show that dependency order can create contextualization race
conditions and use causal interventions to locate the failure.

This is the closest mechanistic style, but the dependency here is different:
a policy must become executable for a semantic target that may not yet exist, and G23A
shows a categorical zero boundary not implied by ordinary contextualization failure.

### Function / in-context vectors

Function-vector and in-context-vector work establishes that task information can be
causally transported in hidden states.

G23C must therefore **not** claim novelty from “a causal vector/state exists.”
Its contribution is the conditional relation:

> **whether a policy value becomes causally executable for a particular semantic target
> depends on target availability during rule processing.**

The old held-out shared steering direction already failed, so the paper should avoid
claims of one reusable global vector.

---

## 9. Main-level status after G23C

The core chain now exists:

1. broad, counterintuitive natural phenomenon;
2. controls against the obvious explanation;
3. a preregistered structural law at complete exclusion;
4. a causal policy-state effect whose efficacy is target-conditioned.

The remaining question is robustness, not a missing story component.

G23C-R is therefore confirmatory only. If it replicates, close the experimental
programme and write. If it does not, downgrade the mechanism scope to the original
Stage-5/G23C materials; do not invent another mechanism branch.

---

## 10. What is not the paper

- target addressability as novelty;
- a generic instruction-order benchmark;
- generic prospective memory;
- generic forgetting/unlearning;
- a standing-gate-vs-cancellation binary;
- another K-carrier wording search;
- a reusable function-vector claim;
- G20/G21 as rescue stories;
- another model-size sweep.
