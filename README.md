# Advance commitment to ignore evidence

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

A policy commonly exists before the information it will later govern. This project
asks whether such a prospective exclusion policy actually controls later evidence,
what determines whether it succeeds, and where that difference becomes causal inside
the model.

## Final result

The core explanatory programme closed after G18 and was **reopened exactly once for the frozen G19 ReGround method evaluation**.

The paper has three established contributions and one pending method contribution:

1. **Prospective exclusion gap.** Across 12 instruction-tuned models, two masked
   diffusion LMs, four vendors and five task families, the same exclusion rule works
   substantially better after evidence than before it.
2. **Target addressability.** G18 prospectively confirms on 100 fresh items / 30 fresh
   skeletons / three families / five models that semantic target representations
   support stronger prospective exclusion than reference or surface resemblance alone:
   **Delta_semantic = +8.91 [7.15,10.76] rating points**, positive in 5/5 models.
3. **Causal mechanism.** A target-dependent mid-network rule state causally changes
   later evidence suppression, replicated in Qwen3-8B and Mistral-Small-24B.
4. **Pending — ReGround.** A frozen two-pass inference-time policy compiler resolves
   the same prospective semantic policy against retrieved documents and compiles a
   selective exclusion ledger. It becomes a contribution only if G19 passes its
   preregistered gates.

The paper does **not** claim that every model perfectly preserves an internal policy
and then ignores it, that identifiers never work, that the phenomenon exists only at
the numerical value zero, or that a universal semantic-binding circuit has been
identified.

## Start here

1. [PAPER_DRAFT_MAINLINE.md](PAPER_DRAFT_MAINLINE.md) — paper-story mother draft:
   question, datasets, claims, experiments, numbers, proof logic and figure plan.
2. [PAPER_FRAME.md](PAPER_FRAME.md) — authoritative final scientific framing.
3. [PAPER_OUTLINE.md](PAPER_OUTLINE.md) — section-by-section writing blueprint.
4. [STATUS.md](STATUS.md) — compact factual ledger and experiment scope.
5. [ACL_EMNLP_ALIGNMENT_STANDARD.md](ACL_EMNLP_ALIGNMENT_STANDARD.md) — Outstanding-
   shaped reference standard and gap analysis.
6. [RELATED_WORK_2026.md](RELATED_WORK_2026.md) — occupied neighbouring questions and
   novelty positioning.
7. [EXPERIMENTS.md](EXPERIMENTS.md) — full experiment registry.
8. [METHOD_REGROUND.md](METHOD_REGROUND.md) — frozen method design, baselines and gates.\n9. [RESEARCH_HISTORY.md](RESEARCH_HISTORY.md) — chronology, stopped branches and\n   corrections.

## Main empirical assets

### G0 — broad phenomenon
- 144 frozen items;
- five task families;
- 12 instruction-tuned checkpoints + two masked diffusion LMs;
- Exclude-before / Exclude-after with matched Admit controls;
- independent rule and memory probes.

### G18 — centrepiece confirmation
- 100 fresh items;
- 30 fresh skeletons;
- legal judgment, evidence inference and ranking/selection;
- five frozen checkpoints from four vendors;
- 6 target representations × 3 rule states;
- 9,000 generations;
- raw rating points with a separate no-rule baseline for every preview.

See [results/g18_semantic_targeting_results.md](results/g18_semantic_targeting_results.md).

### Agent counterfactual
Real SYSTEM → TOOL → assistant structure. The key invariant is not that identifier
policies never work; it is that identifier-specific protection does not follow the
same proposition across D7→D9, while proposition-targeted control does.

### Mechanism
- evidence-span causal gate;
- late answer-level resolution;
- matched-chronology rule-state interchange;
- Qwen3-8B + Mistral-Small-24B replication.

See [stages/STAGE5.md](stages/STAGE5.md) and results/mech/.

### G19 — ReGround method evaluation (pending)
- same semantic policy information in Semantic-Pre / Semantic-Generic / Semantic-Restate / Gold / Self;
- same-D7 / same-D9 / lexical-overlap wrong-D9 retrieval variants;
- ReGround-Self uses the same checkpoint as a short semantic resolver;
- 100 items / 30 skeletons / three families / five models;
- 13,500 decision conditions + 1,500 resolver calls;
- no G19 result is claimed before generation.

See [METHOD_REGROUND.md](METHOD_REGROUND.md) and
[preregistrations/PREREGISTRATION_G19_REGROUND.md](preregistrations/PREREGISTRATION_G19_REGROUND.md).

## Historical records

The controlled stage files in [stages/](stages/) are preserved as historical records,
including their own in-round corrections. Do not infer the current paper claim from an
old stage heading; use PAPER_FRAME.md and STATUS.md.

The BTF-3 hindsight branch is stopped. Its data, preregistrations and integrity
corrections remain for provenance but are not part of the present paper.

## Reproduction

See [REPRODUCE.md](REPRODUCE.md). Git freeze commits and tags remain the authority for
chronology relative to model outputs.
