# Project status — final experimental ledger

**As of:** 2026-09-04, after G18 and the frozen ReGround design. **Experimental programme: reopened exactly once for G19 method evaluation.**
**Target:** ARR 2026-10-12 → NAACL 2027.

This file is the compact factual ledger. The final scientific story is in
[PAPER_FRAME.md](PAPER_FRAME.md); the writing blueprint is in
[PAPER_DRAFT_MAINLINE.md](PAPER_DRAFT_MAINLINE.md). Historical stage documents are
preserved as records of what was believed at the time and are not retroactively
rewritten.

## 1. Scientific question

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

The paper studies a common structure: a policy is available before the information it
will later govern. The core question is not merely whether the policy can be recalled,
but whether it actually controls the later evidence's contribution to a decision.

## 2. Final main line

| # | Claim | Load-bearing evidence | Breadth | Status |
|---|---|---|---|---|
| 1 | **Prospective exclusion is systematically harder than post-evidence exclusion.** | G0: same exclusion rule before vs after evidence; matched Admit control has no order effect. Delta_time has the same sign in all 12 instruct models, with 10/12 intervals excluding zero. | 12 instruct + 2 masked diffusion LMs, 4 vendors, 5 task families, 144 frozen items | **established** |
| 2 | **Explicit access to the policy is not sufficient for enforcement.** | Separate probes recover the required zero-weight policy at ceiling; more importantly, on-policy and teacher-forced state-externalisation show that in Qwen3-8B and Gemma-3-12B, evidence can still influence the decision even when the trajectory explicitly states zero weight. | separate probe: broad panel; on-policy causal dissociation: 3 models, strongest in Qwen/Gemma | **established, model-heterogeneous** |
| 3 | **The difficult regime is hard suppression of semantically integrated evidence, not future-directed instruction following in general.** | Same-wording weight sweep shows a sharp concentration at requested zero; explicit arithmetic contribution is implemented prospectively with zero pre/post gap in 4/5 models. Non-multiplicative cap/sign-flip manipulations retain smaller gaps, so this is a concentration, not a universal “zero only” law. | 3–6 models depending on test | **boundary condition** |
| 4 | **Prospective exclusion depends on target addressability: semantic target representations support stronger exclusion than reference or surface resemblance alone.** | **G18 confirmatory factorial**: Delta_semantic = **+8.91 [+7.15,+10.76] rating points**, positive in 5/5 models. Para-minus-empty = **+12.85 [+10.32,+15.42]**, positive in 5/5, CI excluding zero in 4/5. | **100 fresh items, 30 fresh skeletons, 3 families, 5 models, 4 vendors; 9,000 generations** | **prospectively confirmed** |
| 5 | **Semantic control can follow information across a change of identifier.** | Agent SYSTEM→TOOL counterfactual: when the same proposition arrives as D9, identifier policies lose their protection while proposition policies continue to suppress it. Identifier-only policies can work on their named D7 in some models; the invariant is the cross-identifier dissociation. | 4 models, real chat roles | **established** |
| 6 | **A target-dependent rule state causally carries successful vs failed prospective exclusion.** | Matched-chronology rule-span interchange changes later suppression before the later evidence is processed. Qwen3-8B: L14–18/36; Mistral-Small-24B: L12–16/40. The mid-network localisation and causal transfer replicate; Qwen's rescue/break asymmetry does not. | 2 models, 2 architectures | **causal mechanism established** |

## 3. G18 — the centrepiece confirmation

G18 was frozen specifically because the target-addressability account had been
discovered through Stage 3C→3D→3E, including a design rebuild and a change from REI to
raw rating points. The confirmatory round therefore used the final estimand from the
start, on fresh materials.

Design:
- 6 target representations: none, identifier stub, lexical-overlap/wrong proposition,
  paraphrase, entailing-specific statement, unrelated length-matched content;
- 3 rule states: preview only, preview + evidence, preview + exclusion rule + evidence;
- every preview level has its own no-rule baseline;
- raw sign-aligned rating points only; no leverage-normalised ratio;
- 100 fresh items / 30 fresh skeletons / three families;
- 5 frozen checkpoints across four vendors.

Pooled ExclusionEffect:
- entail **31.16 [27.99,34.40]**
- paraphrase **30.93 [28.19,33.66]**
- identifier 26.27 [23.65,28.96]
- unrelated 22.06 [19.16,24.97]
- none 21.84 [19.21,24.66]
- lexical-overlap / wrong proposition 18.08 [15.71,20.57]

The primary frozen contrast is Delta_semantic = **+8.91 [+7.15,+10.76]** and is
positive in every model.

### G18 decomposition

The semantic preview also makes the later evidence highly redundant:
marg(no rule) falls to about +3 points under paraphrase/entailment. Yet with the
exclusion rule, marg(exclude) becomes about -28 points, below the preview-only
baseline; this sign is negative in 5/5 models under paraphrase and positive in 5/5
under the lexical-overlap/wrong-proposition control.

This is reported as a surprising consequence of semantic target identification. It
licenses **block-transcending suppression once the proposition is identified**, but
does not by itself distinguish proposition-level generalisation from answer-level
overcorrection.

## 4. Supporting characterisation — important, not separate contributions

These experiments explain or bound the main line but should not become independent
paper stories:

- eight natural-language ruling formulations: positive prospective/post gap in 40/40
  model×wording cells;
- distance and rule-to-evidence delay: ordinary recency/forgetting is insufficient;
- masked diffusion models: the effect does not require a left-to-right causal prompt
  mask;
- Stage 3A/3D preview ladders and content×identity 2×2: discovery evidence for target
  addressability;
- Stage 3E duplicate/redundancy audit: established the correct raw-point estimand;
- tagged evidence stream: meaningful evidence-carried provenance/class semantics can
  support prospective selective routing;
- G16: bridge gate failed; no class-marker mechanism claim;
- G17: frozen ratio estimand failed; post-result raw-point reanalysis is suggestive
  only and is not needed for the paper.

## 5. Mechanistic scope

Licensed:
- downstream access to excluded evidence is causally necessary for the residual
  decision shift in Qwen3-8B;
- successful and failed content-preview conditions differ in a causal rule-span state
  in the middle of the network;
- interchanging this state changes later suppression in Qwen3-8B and
  Mistral-Small-24B;
- the shared invariant is mid-network localisation plus causal transfer.

Not licensed:
- a universal reusable “semantic binding vector”;
- a dedicated neuron/circuit named “target found”;
- a mechanism for class-marker binding;
- mechanism generality beyond the two tested architectures.

## 6. Method extension — ReGround

After G18, the authors explicitly reopened the programme for one positive method test
rather than another explanatory/control round. **ReGround** resolves a stored semantic
policy descriptor against the documents that actually arrived, compiles the matched
IDs into a trusted post-retrieval exclusion ledger, and then lets the original model
decide. It has a gold upper bound and an end-to-end self-resolving version.

G19 is frozen before generation in
`preregistrations/PREREGISTRATION_G19_REGROUND.md`. It uses the G18 100-item / 30-skeleton
set in an agentic retrieval wrapper, five models, same-D7 / same-D9 / lexical-overlap
wrong-D7 variants, generic-reminder and ID-restatement baselines, and raw-point target
error plus collateral-damage metrics. The primary method must improve over both the
prospective ID baseline and a generic post-retrieval reminder while preserving the
hard negative.

Until G19 has run, ReGround is a **designed, frozen method**, not a claimed result.

### Practical implications already supported

Independently of G19, the completed experiments support three design implications:

1. **Restate exclusion after retrieval when possible.** The identical post-evidence
   policy is consistently more effective than the prospective form.
2. **Prefer semantically meaningful/provenance-based policy targets over arbitrary
   resource names when the semantics are available.** The tagged stream and G18 show
   why target representation matters.
3. **Do not treat an identifier policy as semantic protection.** In the agent
   counterfactual, semantic policies follow the proposition across D7→D9 whereas
   identifier policies do not.

No claim is made that these are a fully evaluated deployment mitigation suite.

## 7. Corrections and negative results retained

- G0's preregistered human-motivated prediction reversed.
- Stage 3D's first similarity-ladder construction was rebuilt after a design problem
  was identified; Stage 3E then found the redundancy confound and changed the metric.
  G18 exists precisely to confirm the final account prospectively.
- Stage 5's initial recovery-fraction summary overstated rescue and was withdrawn.
- G16 stopped at its frozen bridge gate.
- G17's frozen ratio estimand was defective; its post-result raw-point pattern is
  labelled suggestive only.
- The abandoned BTF-3 hindsight branch and its integrity corrections remain in the
  repository but are not part of this paper.

## 8. Programme status

**Reopened once for G19 ReGround by explicit author decision.** This is a positive
method evaluation derived from the confirmed target-addressability mechanism, not a
repair of G18/G16/G17. No other experimental branch is reopened: no model-size sweep,
frontier API panel, new natural corpus, third mechanism model, or successor to
G16/G17.

G19 outcomes are frozen to `success`, `partial`, or `no-benefit`; every outcome closes
the programme permanently. Remaining work in parallel: paper writing, figures,
appendix compression, and reviewer simulation.
