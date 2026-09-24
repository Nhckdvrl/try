# Paper frame — prospective semantic exclusion

**Updated:** 2026-09-23 after G23A success and G23B carrier failure;
**RQ2 reframed 2026-09-24** — see `PAPER_RQ2_BOUNDARY_REFRAME.md`.  
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

## Paper-level novelty architecture

Do **not** force the project into three headline RQs merely because three sections are
convenient.

Sasano's relevant criterion is:
- each RQ should map one-to-one to a finding;
- the paper should emphasize the most surprising finding;
- technically valid but obvious results should not be inflated into contributions.

At present the project has **two novelty-bearing research questions**.

### RQ1 — prospective causal eligibility of future evidence

> **Can an LLM commit in advance to make future evidence causally irrelevant to a
> later decision?**

Finding target:

> **Prospective exclusion is systematically weaker than retrospective exclusion, and
> source-grounded natural evidence can still leak under a prior zero-use ruling.**

Main evidence:
- G0 controlled breadth;
- Admit / wording / delay / diffusion controls;
- agent-like system-policy -> tool-output setting;
- G24A natural/source-grounded FEVER + SciFact round.

Important scope:
G24A's frozen verdict is `prospective-only`; its cross-model and cross-source
consistency clauses did **not** both pass. Do not rewrite it as uniform replication
across all models/datasets.

### RQ2 — smooth weighting problem versus exact-zero control boundary

(Reframed 2026-09-24; full argument, hypotheses and confirmatory design in
`PAPER_RQ2_BOUNDARY_REFRAME.md`.)

> **Is prospective exclusion a smooth evidence-weighting problem, or is exact
> semantic zero a qualitatively different control boundary?**

Finding target (draft, pending the natural-evidence confirmatory):

> **Semantic prospective control exhibits a sharp exact-zero boundary rather than a
> smooth difficulty curve: the timing gap is flat across requested weights from 1%
> to 50% but jumps at exactly 0% — although 0% and 1% require nearly identical
> suppression — and exact zero is executed perfectly when the contribution is
> explicitly arithmetic.**

Licensed §12.3 form must remain reachable verbatim:

> **Complete semantic evidence exclusion shows an additional prospective cost, even
> though prospective zero can be executed exactly when the contribution is explicit
> and verifiable.**

Main evidence:
- G23A weight ladder (flat 1–50, jump at 0; `Gap(0)−Gap(1) = 8.27` points for one
  point of demanded suppression; `Delta_zero=+8.83 [+4.39,+13.33]`);
- exact arithmetic / explicit weighting boundary (4/5 models prospective-zero exact);
- planned confirmatory: fresh natural near-zero sweep from the frozen G24A candidate
  pool (design only; STATUS-gated);
- source-grounded numeric invalidation boundary;
- policy-access probes only as controls.

The standalone claim “models can state a policy but fail to follow it” is not novel
enough to be a contribution. The generic representation-versus-deployment framing is
owned by ACL 2026 Main; keep every sentence on **causal eligibility of future
evidence**.

### Mechanistic evidence — supporting layer, not RQ3

Stage 5, G23C and G24B provide valid causal evidence about the rule-time state.

However, the current mechanism headline is vulnerable to the reviewer-obvious
compression:

> “If target semantics were present before the rule, the resulting hidden state can
> naturally carry more target-specific policy information.”

G24B removes the recipient-sensitivity confound, but does not make that scientific
statement non-obvious.

Therefore:
- do not count Stage 5/G23C/G24B as a third novelty-bearing finding;
- do not run G23C-R merely to make the same claim more robust;
- use the mechanism results only to explain/interpret RQ1–RQ2 unless a stronger,
  genuinely non-trivial question is found.

### Third-RQ slot — OPEN, not mandatory

A third headline RQ is allowed only if it passes the G18 triviality veto:
1. treatment does not directly contain the answer;
2. a reviewer cannot dismiss it with one obvious sentence;
3. at least two live accounts make different predictions under the same visible task
   content;
4. the expected headline contains a genuinely non-obvious relation.

If no such RQ is found, write a strong two-finding paper rather than adding an obvious
third finding.

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

> **The rule-time hidden state is causally involved in later suppression, and its
> transportable policy effect depends on the preceding target context.**

This is useful mechanistic evidence, but not by itself a novelty-bearing headline.
The visible manipulation already differs in whether matching target semantics were
present, so “the state becomes more target-conditioned” is too close to the default
expectation to carry a contribution on its own.

---

## 6. Current paper spine

The paper should currently read:

```text
Natural problem:
Can an LLM commit now to ignore evidence that arrives later?

        ↓

RQ1 / Finding 1
Prospective exclusion is systematically weaker than retrospective exclusion,
including a source-grounded natural-evidence prospective leak.

        ↓

RQ2 / Finding 2
Smooth weighting problem, or exact-zero control boundary?
The timing gap is flat from 1% to 50% and jumps at exactly 0%
(0 vs 1 differs by one point of demanded suppression but by
8.27 rating points), while arithmetic prospective zero is
executed exactly. Pending the natural-evidence near-zero
confirmatory.

        ↓

Mechanistic support
Stage 5 / G23C / G24B show that rule-time internal state participates causally
in later suppression and depends on target context.

        ↓

OPEN
Candidate: scope of a prospective exclusion policy — novelty audit
complete: no parent-level prior found (PROCEED, narrowed;
PAPER_RQ3_SCOPE_NOVELTY_AUDIT.md). Still not registrable until the
five gates pass. If it (or another) fails the triviality veto,
stop at two headline findings.
```

The mechanism line is explanatory evidence, not the third contribution.

---

## 7. Mechanism evidence — valid but novelty-limited

### Stage 5

Matched chronology localizes a rule-time causal window in Qwen3-8B and
Mistral-Small-24B before later evidence is processed.

### G23C

Frozen L14:
- `PolicyTransfer_M = +13.03 [+11.69,+14.31]`;
- `PolicyTransfer_U = +4.89 [+3.73,+6.18]`;
- `TargetConditioning = +8.15 [+6.91,+9.44]`.

### G24B

With recipient context fixed:
- `DonorPolicy_M = +10.81 [+8.31,+13.41]`;
- `DonorPolicy_U = +6.79 [+5.22,+8.78]`;
- `DonorTargetInteraction = +4.02 [+2.27,+6.14]`.

This resolves the donor-vs-recipient technical confound.

### Interpretation

These are real causal results. They support the interpretation that target context
affects what policy-relevant information is available in the rule-time state.

They do **not** currently earn an independent headline contribution because a reviewer
can still reasonably say:

> “A state produced after seeing matching target semantics can naturally carry more
> target-specific policy information than one produced after unrelated content.”

No amount of fresh replication changes that novelty problem by itself.

### G23C-R

`PREREGISTRATION_G23C_R_FRESH_REPLICATION.md` is **HOLD / NO COMPUTE**.

Fresh-material replication is valuable only after a non-trivial parent mechanistic
question is identified. Do not run it by roadmap inertia.

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

## 9. Main-level status after novelty re-audit

The project currently has two plausible headline findings and one supporting mechanism
line.

What is missing is **not** another robustness check. It is either:
- a genuinely non-obvious third question that grows naturally from RQ1/RQ2; or
- evidence that the two-finding paper is already scientifically complete enough to
  submit without inventing a third contribution.

Do not use experiment count as a substitute for novelty.

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
