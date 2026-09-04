# Prospective evidence exclusion in language models

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

This repository studies a robust reversal:

> the same exclusion rule is systematically less effective when stated **before** its
> target evidence than **after** it.

The project is currently in a **scientific factorization audit**. No new generation is
authorized.

## Current authority

Read in this order:

1. [SCIENTIFIC_REGISTER_2026-09-04_V3.md](SCIENTIFIC_REGISTER_2026-09-04_V3.md)
2. [STATUS.md](STATUS.md)
3. [PAPER_FRAME.md](PAPER_FRAME.md)
4. [NEXT_EXPERIMENTS_POST_RESET.md](NEXT_EXPERIMENTS_POST_RESET.md)
5. [G22_DESIGN_AUDIT.md](G22_DESIGN_AUDIT.md) — registered G22 design constraints.
6. [PAPER_DRAFT_MAINLINE.md](PAPER_DRAFT_MAINLINE.md)
7. [PAPER_OUTLINE.md](PAPER_OUTLINE.md)
8. [RELATED_WORK_2026.md](RELATED_WORK_2026.md)
9. [ACL_EMNLP_ALIGNMENT_STANDARD.md](ACL_EMNLP_ALIGNMENT_STANDARD.md)
10. [RESEARCH_HISTORY.md](RESEARCH_HISTORY.md)

Historical reset/audit documents remain for provenance but are not current authority.

---

## Stable empirical core

### G0 — prospective exclusion reversal

- 144 frozen items;
- five task families;
- 12 instruction-tuned models / four vendors;
- two masked diffusion LMs;
- same exclusion rule before vs after evidence;
- 12/12 instruct models show the same timing-gap direction;
- matched Admit control has no analogous order effect.

### Policy access vs enforcement

In Qwen3-8B and Gemma-3-12B, prospective evidence can still affect decisions even on
trajectories that explicitly state zero weight. Phi-4-mini is more mediated by whether
zero is expressed.

### Arithmetic boundary

Future numeric weighting can work exactly. On the verifiable linear task, four of five
models execute prospective `w=0` exactly on qualified items.

### Object-existence ladder

A name, identifier, content-pending stub, type, or direction is not enough to reliably
rescue prospective exclusion. Full target content before the rule is.

### G18 — confirmed, but interpretation narrowed

G18:
- 100 fresh items / 30 skeletons / three families;
- five models / four vendors;
- 9,000 generations;
- `Delta_semantic = +8.91 [7.15,+10.76]`, 5/5 positive.

But semantic previews themselves substantively assert the target proposition. Their
no-rule later-evidence marginal collapses from ~32 to ~3 points.

Therefore G18 shows:

> **having the target proposition already represented before exclusion strongly changes
> suppression.**

It does not yet show that non-evidential knowledge of a future target is sufficient.

### Stage 4 / Stage 5

Stage 4:
effective exclusion can be strongly content-conditioned across document IDs.

Stage 5:
Qwen3-8B and Mistral-Small-24B show a target-dependent causal rule-time state that
changes later suppression.

---

## Current scientific fork

The central unresolved question is:

> **What must exist when exclusion is processed for future evidence to become causally
> inert?**

Live accounts:

1. **Deferred target binding / eager control compilation** — semantic target knowledge
   is sufficient but must be available when policy is processed.
2. **Evidential instantiation / retrospective revision** — knowing future content is
   insufficient; exclusion acts mainly on an already-present evidence state.
3. **Local semantic control** — successful prospective routing may rely on semantic
   features available locally at evidence arrival rather than a persistent
   policy→future-object relation.

None is established.

---

## Registered next design

### G22 — Target Knowledge vs Evidential Instantiation

**Design audit only. Not preregistered. Not frozen. No generation.**

Three target states:

```
UNRESOLVED:
EXCLUDE → future E(P)

KNOWN-BUT-NON-EVIDENTIAL:
non-evidential target specification(P) → EXCLUDE → future E(P)

EVIDENTIALLY-INSTANTIATED:
asserted evidence(P) → EXCLUDE → future E(P)
```

The middle condition must be genuinely judgment-neutral before the experiment is valid.

If semantic knowledge alone rescues, the next step is a clean early-vs-late mapping
composition test.

If only evidential instantiation rescues, the next step is passive gate vs active
evidence-state revision/cancellation.

---

## Important corrections / downgrades

- **Target Addressability** is not the paper novelty.
- **G21 Source–Proposition Scope Entanglement** is not current mainline.
- **G20 v3** is not currently authorized; its composition hypothesis is conditional on
  G22.
- G18 below-baseline suppression does not by itself establish scope collapse.
- Stage 3B tagged routing does not yet prove standing-policy execution because there is
  no semantic-labels-present/no-policy baseline.
- ReGround G19 remains cancelled before generation.

---

## Current authorization

Allowed:
- literature search;
- design audit;
- material drafting;
- dummy analyzer/tests;
- repository cleanup.

Not allowed:
- G20/G21/G22 generation;
- tagged-routing diagnostic generation;
- new mechanism runs;
- ReGround.

No result-driven prompt repair.
