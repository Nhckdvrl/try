# Mainline audit — Simple-data reset after takeover

**Date:** 2026-09-06  
**Target:** NAACL / ACL / EMNLP Main.  
**Status:** working scientific decision record.  
**Relationship to prior ledgers:** this audit does **not** erase preregistrations, failed experiments, or the 2026-09-04/05 ledgers. It supersedes their **experiment priority** where they conflict with the present reset.

The governing rule is now:

> **Simple question. Simple data. Non-obvious finding. Deep analysis.**

The repository contains substantial empirical assets, but sunk cost is not evidence that the existing paper identity should survive.

---

# 1. Executive decision

The current paper identity

> *Can a language model commit in advance to ignore evidence it has not yet seen?*

is no longer treated as the default mainline.

The G0 phenomenon is empirically strong, but its **conceptual neighborhood is too crowded** to justify continuing to narrow the same question until novelty appears. Generic versions of the takeaway are already surrounded by work on instruction position, standing instructions, identify-and-ignore methods, contextualization race conditions, in-context forgetting/unlearning, and self-blinding.

Therefore:

| object | decision | reason |
|---|---|---|
| G0 prospective-vs-retrospective exclusion | **HIGH-RISK / ASSET, NOT DEFAULT PAPER CENTER** | strong replicated phenomenon; conceptual compression risk remains high |
| G18 semantic targeting | **SUPPORTING ONLY** | strong result, but “more target semantics helps” is not novelty and semantic preview also instantiates evidence |
| G22 U/K/I factorization | **KILL AS NEXT EXPERIMENT** | scientific distinction is intelligible, but K requires increasingly artificial carriers; design complexity is now evidence against the research object |
| G20 deferred composition | **PAUSE** | only worth revisiting if a simpler phenomenon independently motivates it |
| G21 source–proposition scope | **HIGH-RISK / NO CURRENT MAINLINE** | does not explain G0; 2026 provenance/evidence-arbitration work makes the independent topic crowded |
| ReGround G19 | **KILL** | already cancelled; mitigation is too close to an obvious engineering fix |
| explicit-outcome paradox lead | **SMALL PILOT** | genuinely counterintuitive direction; one clean experiment can confirm or kill |
| exact-zero discontinuity | **KEEP — HIGHEST-PRIORITY CANDIDATE** | existing data suggest a simple, non-obvious law not reducible to generic position or forgetting effects |

No new model generation is authorized by this audit. The immediate work is novelty assassination and a minimal fresh pilot design for the strongest candidate.

---

# 2. What from the old project is genuinely valuable

## 2.1 G0 is a real discovery, even if it may not be a sufficient paper question

The reversal is broad and replicated:
- 144 frozen items;
- five task families;
- 12 instruction-tuned models / four vendors;
- two masked diffusion LMs;
- the direction is shared by 12/12 instruct models;
- matched Admit controls do not show the same order effect.

This is **not** being discarded as noise.

What is downgraded is the inference that a strong empirical phenomenon automatically implies a sufficiently novel paper identity.

## 2.2 Policy access vs causal use is a reusable asset

Qwen/Gemma can recover or state the intended zero-weight policy while prospective evidence still changes the judgment.

This is useful whenever a future mainline needs a **recognition / implementation dissociation**, but it is not by itself new enough to define the paper.

## 2.3 The arithmetic boundary is unusually important

Future-directed exact arithmetic weighting can work even where semantic evidence exclusion fails.

This prevents the project from collapsing to:
> “models cannot remember or execute future instructions.”

It may become a key boundary for a stronger theory of semantic influence control.

## 2.4 Stage 5 is a mechanism toolbox, not a conclusion generator

The repository already has causal localization and interchange machinery on Qwen and Mistral. That is valuable **after** a new behavioral law survives.

Do not choose a question merely because the existing mechanism code can analyze it.

---

# 3. Results that should not carry novelty

## 3.1 G18 target addressability

Frozen G18 is numerically strong:
- 100 fresh items;
- 30 skeletons;
- five models / four vendors;
- 9,000 generations;
- pooled semantic advantage +8.91 [+7.15,+10.76].

But the semantic preview itself states almost the same proposition as the later evidence. The later evidence's no-rule marginal collapses from about 32 points to about 3.

Thus the safe fact is:
> prior representation of the proposition changes later exclusion strongly.

The rejected novelty story is:
> knowing the target more specifically makes it easier to exclude.

That is both partly confounded here and conceptually too unsurprising.

## 3.2 G22

G22 asks a legitimate theoretical distinction:
- U: unresolved target;
- K: known but non-evidential target;
- I: evidentially instantiated target.

The problem is not that the distinction is logically meaningless. The problem is that producing K naturally has already required retrieval manifests, interface metadata, future-record descriptions, and special neutrality gates.

This violates the present selection rule:

> If a latent state can only be isolated by building a miniature experimental world around it, pause the question rather than adding another carrier.

A future naturally occurring K substrate could revive the distinction. The current hand-built G22 should not.

---

# 4. The strongest buried anomaly: exact zero is special

The repository already contains a result that is more interesting than most of the later factorization program.

With the same sentence

> “The causal weight assigned to X is exactly W% of its normal evidential weight”

and only W changed, the **prospective–retrospective gap is concentrated at exactly zero**.

Across six models, the gap is descriptively largest at w=0. On Qwen3-8B:
- w=0 gap: +0.33;
- w=1% gap: +0.01.

The old analysis reports a 38× ratio between those two temporal gaps.

At the coarser sweep, the four-model mean pre–post gap is:
- w=0: +0.298;
- w=.25: +0.050;
- w=.50: +0.028;
- w=.75: −0.001;
- w=1: −0.050.

This is scientifically different from saying that “future rules are hard.” A nonzero weighting rule still refers to a future object. The extra failure appears when semantic influence must become **exactly absent**.

Important caveats:
- models do **not** accurately implement fractional weights; 1–50% often collapse toward a middling effective influence;
- the formal kink term is not uniform across every model;
- Mistral is near a floor;
- existing data were not designed around this as the main question.

Therefore the current candidate is not:
> “LLMs can accurately apply 1% but not 0%.”

It is:

> **Complete semantic non-use may be a qualitatively different control operation from partial discounting, and that difference becomes strongly order-sensitive.**

This is a candidate law, not an established headline.

---

# 5. Candidate A — Zero-boundary in semantic influence control

**Verdict: KEEP / highest-priority novelty assassination + SMALL PILOT**

## 5.1 Research Question

> **Is exact non-use of information a qualitatively different control problem for LLMs from assigning it any non-zero influence?**

## 5.2 One-example

> “You will later see Report B. Give it 1% of its normal evidential weight.”  
> versus  
> “You will later see Report B. Give it 0% of its normal evidential weight.”

Same future report, same wording, one number changes. Does 0 behave like the endpoint of a smooth control curve, or like a different operation?

## 5.3 Minimal Dataset

First pilot should be shallow:
- two evidence polarities per item;
- W in {0%, epsilon%} only, initially epsilon=1%;
- rule before vs rule after evidence.

That is a 2×2 main design. Add no ontology, no K/I/U states, no source lifecycle.

A second sweep over a few nonzero values is justified only if the zero-vs-epsilon interaction replicates.

## 5.4 Gold

Use a paired causal-influence estimand:
- construct two otherwise identical prompts where target evidence supports opposite answers;
- measure how much the numeric judgment changes;
- at W=0 the correct target-evidence influence is zero by construction.

No LLM judge is needed.

The first pilot should judge the **zero-vs-epsilon temporal interaction**, not whether the model numerically realizes exactly 1%.

## 5.5 Novelty Threat Map

Current threats:
1. **Instruction Position Matters** (Findings ACL 2024): generic placement effects.
2. **Racing Thoughts** (NAACL 2025): dependency-order / critical-window contextualization failures.
3. **I3C** (NAACL 2024): identify and ignore irrelevant conditions.
4. **Answer When Needed, Forget When Not** (Findings ACL 2025): selective in-context unlearning and late “pretend to forget” behavior.
5. **ICF-Bench / Do LLMs Forget What They Should?** (ICLR 2026): in-context forgetting as a capability distinct from memory.
6. **Self-Blinding** (2026): explicit ignore/pretend-not-to-know prompts can fail or backfire.
7. **Step-by-Step Mastery** (Findings ACL 2025): soft-constraint following.
8. General negated-instruction / prohibition literature.

These kill any generic claims about forgetting, negative instructions, or position.

What has **not yet been located** in the current search is a paper isolating:
> the same semantic evidence-control relation, same wording, with a discontinuity specifically between exact zero and arbitrarily small nonzero influence, interacting with whether the target already exists.

That exact conceptual boundary requires continued search before registration.

## 5.6 Growth Path

If the fresh effect is strong:

**C1 — phenomenon**
> semantic influence control has a sharp zero boundary: exact non-use is disproportionately order-sensitive.

**C2 — stronger law / dissociation**
> the zero singularity appears in semantic evidence control but disappears in explicitly computable arithmetic control; therefore it is not generic scalar instruction following or prospective memory.

Potential second dissociation:
> zero may become categorical only after the target is represented.

**C3 — mechanism / intervention**
Use the existing Stage-5 machinery to test whether w=0 recruits a target-dependent suppressive control state that w=epsilon does not, and whether causal intervention can create/remove the categorical state.

Do not run mechanism until C1 is confirmed on fresh simple data.

---

# 6. Candidate B — Explicitness paradox

**Verdict: SMALL PILOT**

## 6.1 Research Question

> **Can making an outcome more explicit make it easier—not harder—for a model to keep that outcome from contaminating an earlier judgment?**

## 6.2 One-example

> Two future packets contain the same evidence. One ends with “Outcome: YES”; the other ends with a length-matched neutral sentence.  
> The surprising repository observation is that removing “Outcome: YES” makes hindsight contamination larger.

## 6.3 Minimal Dataset

- identical evidence body;
- explicit verdict vs matched neutral sentence;
- optional header present/absent as one preregistered secondary factor.

Fresh evidence-only materials; no regex redaction.

## 6.4 Gold

Within-item shift of the earlier-time judgment caused by the future packet.

No judge required if the response is a constrained scalar probability.

## 6.5 Novelty Threat Map

High-risk neighbors:
- hindsight/outcome-bias literature;
- Self-Blinding and ignore-known-information failures;
- instruction/salience effects;
- pragmatic accommodation / epistemic vigilance work.

The candidate survives only if its **directional law** is the contribution:
> explicit conclusion-shaped information is *easier* to quarantine than equally informative implicit evidence.

A mere “models show hindsight bias” paper is dead.

## 6.6 Growth Path

C1: replicate explicit-vs-implicit reversal.  
C2: test whether the law follows conclusion explicitness rather than length/salience/header.  
C3: localize whether explicit verdict tokens enable a separable/quarantinable representation and causally manipulate it.

Kill immediately if the clean 2×2 does not reproduce.

---

# 7. Candidate C — Source-local exclusion without proposition-wide suppression

**Verdict: HIGH-RISK / NOT PRIORITY**

## 7.1 Research Question

> **Can an LLM suppress one occurrence of a proposition while still using the same proposition from an allowed source?**

## 7.2 One-example

> Source A says “the drug reduced symptoms.” Source B independently says the same thing.  
> The instruction says to ignore Source A only. Does Source B retain its normal influence?

## 7.3 Minimal Dataset

- A-only;
- B-only;
- A+B;
- A-excluded + B.

No lifecycle metadata; source labels must be natural and stable.

## 7.4 Gold

Difference in target judgment attributable to B with and without an exclusion on A.

## 7.5 Novelty Threat Map

This area is now crowded:
- 2026 **Auditing Provenance Sensitivity in LLM Agent Action Selection** varies source authority while holding proposition/task/position fixed;
- 2026 **Evidence Arbitration in Large Language Models** manipulates source reliability, recency, modality, and provenance;
- ACL 2026 epistemic-vigilance work studies source reliability and linguistic framing;
- broader provenance and prompt-injection work studies authority separation.

Therefore a generic “models mix source and proposition” story is unsafe.

## 7.6 Growth Path

Only worth reviving if a clean pilot reveals a strong and highly specific **same-proposition spillover law** that the above provenance work does not already imply.

At present this is behind Candidates A and B.

---

# 8. Candidate shapes currently killed or deprioritized

The following “X != Y?” shapes are useful for brainstorming but are **not safe research questions merely because they sound clean**:

- mention vs assert;
- presuppose vs assert;
- know vs endorse;
- believe vs rely on;
- source reliability vs proposition truth.

ACL 2026 work on accommodation / epistemic vigilance already directly studies at-issueness, linguistic encoding, and source reliability. 2026 belief/provenance work further crowds neighboring abstractions.

Do not spend GPU on these without a much sharper, non-obvious law.

---

# 9. Updated literature threats that the old ledger underweighted

The following must be included in future novelty audits:

- Qian et al., **Do LLMs Forget What They Should? Evaluating In-Context Forgetting in Large Language Models**, ICLR 2026.
- Christian & Mazor, **Self-Blinding and Counterfactual Self-Simulation Mitigate Biases and Sycophancy in Large Language Models**, 2026 preprint.
- Cheng, Hawkins & Jurafsky, **Accommodation and Epistemic Vigilance**, ACL 2026.
- Bigoulaeva et al., **Patches of Nonlinearity: Instruction Vectors in Large Language Models**, ACL 2026.
- Liao, **Auditing Provenance Sensitivity in LLM Agent Action Selection**, 2026 preprint.
- Carletti et al., **When Text and Numbers Disagree: Evidence Arbitration in Large Language Models**, 2026 preprint.

These do not all kill Candidate A. They substantially raise the bar for generic forgetting, provenance, instruction-processing, and source-reliability claims.

---

# 10. Experiment priority after this audit

Do **not** run G22.

Do **not** expand G0 with more model breadth.

Do **not** run another mechanism sweep.

The next research actions are:

1. Continue exact novelty assassination of Candidate A, especially work on scalar/graded control, negated constraints, selective forgetting, and evidence weighting.
2. Redesign Candidate A onto a fresh Figure-1-level substrate with four main cells.
3. Define a non-ratio causal influence metric and explicit kill criteria.
4. Run only a small discovery panel after the design is frozen.
5. In parallel, keep Candidate B ready as a single clean kill/confirm pilot.
6. If Candidate A is killed by literature or fails the fresh pilot, move to new simple-data RQ search rather than rescuing it with extra latent states.

---

# 11. Kill criteria for Candidate A

Kill or strongly demote if any of the following happens:

- exact prior work already demonstrates the zero-vs-small-nonzero discontinuity in semantic influence control;
- fresh data show only a generic negative-instruction effect with no special zero boundary;
- the interaction is driven by one model family or one template;
- the effect disappears on strong modern models;
- the clean metric requires unstable leverage ratios;
- explaining the effect requires reconstructing G22-like latent-state machinery;
- the only surviving takeaway becomes “0% is harder than 1%.”

The target is a **law about categorical non-use versus graded influence**, not a cute numeric prompt effect.

---

# 12. Current scientific priority

The repository's best next move is no longer:

> identify exactly what K-state exists at policy processing.

It is:

> **ask whether the project has already uncovered a simpler and deeper boundary: models can represent graded influence, yet exact semantic non-use behaves like a qualitatively different operation.**

That hypothesis is still killable. It is currently the first thing worth trying to kill.
