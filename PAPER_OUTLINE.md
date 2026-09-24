# Paper outline — prospective semantic exclusion

**Updated:** 2026-09-24 after the G18-style triviality re-audit.

## Working title

> **Can Language Models Commit to Ignore Future Evidence?**

---

## 1. Introduction

Natural setup: policies often precede the information they govern.

Mother question:

> **Can an LLM commit now to make future evidence causally irrelevant?**

Current contribution structure:

1. **Prospective exclusion asymmetry / natural-evidence leak.**
2. **Semantic causal zero vs explicit/verifiable prospective zero.**

Stage 5 / G23C / G24B are supporting causal evidence, not a third headline contribution.

A third RQ is optional and remains open. Add it only if it passes the reviewer-obvious
veto.

---

## 2. Common setup and distinction from prior work

Define:
- evidence causal eligibility;
- prospective vs retrospective exclusion;
- why this is not generic instruction position, memory availability, belief revision,
  or in-context unlearning.

Keep the novelty object on **future evidence use**, not generic policy compliance.

---

## 3. RQ1 — Can models pre-commit to ignore future evidence?

### 3.1 Controlled breadth

G0:
- 144 items;
- five task families;
- broad instruction-model panel;
- matched Admit control.

### 3.2 Obvious-explanation controls

- wording robustness;
- rule-to-evidence delay;
- policy probes;
- masked-diffusion comparison.

These are controls, not separate findings.

### 3.3 Agent-like role structure

System policy -> future tool output -> assistant decision.

### 3.4 Source-grounded natural evidence

G24A:
- FEVER + SciFact;
- 600 selected items;
- five models;
- frozen verdict `prospective-only`.

Report exact scope:
- pooled prospective leak passes;
- retrospective leak is not distinguishable from zero;
- model/source consistency is heterogeneous.

### Finding 1

> **Prospective exclusion is systematically weaker than retrospective exclusion, and
> source-grounded future evidence can remain influential despite a prior zero-use
> ruling.**

---

## 4. RQ2 — What is special about semantic causal zero?

### 4.1 G23A zero sweep

Report:
- `Gap(0)=+13.86 [+8.54,+19.18]`;
- attenuation-gap mean `+5.03 [+3.16,+6.83]`;
- `Delta_zero=+8.83 [+4.39,+13.33]`;
- 3/3 model deltas positive.

Do not sell “zero is harder” by itself.

### 4.2 Explicit/verifiable zero boundary

Show that prospective zero can be executed exactly in arithmetic / explicit numerical
weighting where contribution is directly specified and checkable.

### 4.3 Policy-access controls

Correct rule recall / requested-weight access shows that simple forgetting is
insufficient.

This is supporting evidence only.

### Finding 2

> **The hard part is not a future zero instruction per se: complete semantic evidence
> exclusion incurs an extra prospective cost even when explicit/verifiable prospective
> zero is executable.**

---

## 5. Mechanistic evidence for the behavioral findings

This section is explanatory, not a separate contribution.

### 5.1 Stage 5 — rule-time causal window

Same chronology; target-context manipulation; two architectures.

### 5.2 G23C — policy-state interchange

Report the preregistered L14 target-conditioning effect and negative-layer controls.

### 5.3 G24B — donor/recipient factorization

Fix recipient prompt and show donor-side policy interaction remains:
`DTI = +4.02 [+2.27,+6.14]`.

### Interpretation limit

These results show causal involvement of the rule-time state.

They do **not** by themselves yield a surprising law that “target-present states are
more target-conditioned”; that consequence is too close to the visible manipulation.

G23C-R is HOLD until a stronger parent question exists.

---

## 6. Open third question — only if non-trivial

Before any new experiment, require:

1. treatment does not contain the answer;
2. two plausible accounts differ under the same visible content;
3. reviewer cannot dismiss the expected finding in one obvious sentence;
4. the result would materially change the paper's scientific understanding, not just
   increase robustness.

If no candidate passes, omit this section and keep a two-finding paper.

---

## 7. Related work

- instruction position / forgetting;
- evidence use / belief revision;
- in-context unlearning / knowledge suppression;
- contextualization race conditions;
- latent task/function states.

---

## 8. Discussion

Emphasize:
- knowing a rule is not the contribution; semantic causal control is;
- zero is not intrinsically hard; semantic causal zero is;
- mechanism evidence is suggestive/explanatory but not inflated into novelty.

---

## 9. Conclusion

> **LLMs can understand a future evidence policy yet fail to make later semantic
> evidence causally inert; the failure is specifically stronger for complete semantic
> exclusion than for explicit/verifiable prospective zero.**
