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

G23C asks whether the Stage-5 state is an **executable target × policy state**.

The experiment uses the same matched chronology and varies policy value inside the same
preview:

```text
matched preview:   0% vs 100%
unrelated preview: 0% vs 100%
```

At the previously localized rule-time layer, exchange the policy-value hidden state
bidirectionally.

Critical test:

> **Does 0↔100 policy-state interchange move later evidence use much more strongly when
> the target proposition was available before the rule?**

If yes:

> **Target availability enables formation of a rule-time state that causally carries the
> evidence-use policy for that target.**

This directly connects:
- the broad prospective exclusion failure;
- the zero-amplified behavioral boundary;
- and the mechanism.

If no, Stage 5 remains a target-readiness result and the paper must not overclaim an
executable policy state.

---

## 7. Final intended claims if G23C succeeds

### C1
Prospective exclusion is systematically weaker than retrospective exclusion.

### C2
The asymmetry is not reducible to simple policy forgetting.

### C3
The prospective timing cost is discontinuously amplified at complete exclusion.

### C4
When target semantics are available during policy processing, a mid-network rule-time
state causally carries the zero-vs-full evidence-use policy for that target.

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

Possible subtitle after mechanism confirmation:

> **Prospective Evidence Exclusion Requires Target-Conditioned Policy State**

Do not use the subtitle unless G23C passes.
