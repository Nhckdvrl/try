# Paper mainline draft — claims, evidence, and proof structure

**Status:** post-G18 mother draft. Experimental programme closed.
**Target:** Outstanding-shaped scientific narrative; NAACL Main submission.

This document is the paper's intellectual mother draft. It is not an experiment log.
The reader should encounter one natural question, one broad phenomenon, one decisive
explanatory variable, one externalisation, and one causal mechanism.

---

# 0. The paper in one paragraph

> **Can language models commit in advance to ignore evidence they have not yet seen?**
> Across twelve instruction-tuned models, two masked diffusion language models, and
> five task families, the same exclusion policy is substantially less effective when
> stated before its target evidence than after it. The failure is not explained by
> policy availability alone: models can explicitly recover the policy, yet prospective
> evidence can still enter the decision. We show that the decisive variable is
> **target addressability**. In a prospectively frozen confirmation on 100 fresh items,
> 30 fresh skeletons, three task families, and five models, policies backed by a
> specific semantic representation of the future target remove substantially more
> evidence influence than policies backed only by reference or surface resemblance.
> The same semantic-vs-identifier distinction appears in a SYSTEM→TOOL agent
> counterfactual. Mechanistically, target availability changes a mid-network rule
> state before the later evidence is processed, and interchanging that state causally
> changes subsequent evidence suppression in Qwen3-8B and Mistral-Small-24B.

The scientific object is **prospective evidence exclusion**.
The explanatory variable is **target addressability**.
The mechanistic result is a **target-dependent rule state that controls later
evidence gating**.

Do not make “instruction position,” “zero weight,” “binding,” or “agent policy” the
paper's identity. They are parts of the route to the explanation.

---

# 1. Why the question matters

Policies usually exist before the data they govern.

A system prompt may prohibit a source before retrieval runs. An agent may be told not
to use a class of memories before those memories are fetched. A decision process may
rule evidence inadmissible before the evidence appears. In all of these cases, the
model must establish a control relation between a policy that exists now and an
informational target that will only be instantiated later.

The ordinary assumption is that understanding and remembering the policy should be
enough. If the model knows that a future item must not affect the answer, then once the
item arrives, the policy should govern it.

This paper shows that this assumption is wrong.

The first surprise is temporal: language models often exclude evidence better after
they have already seen it than when they were warned in advance. The deeper result is
representational: prospective control depends on what representation of the future
target is available when the policy is processed.

This gives the paper a clean scientific descent:

**advance exclusion gap → policy access is not enough → target addressability →
agent identity counterfactual → causal rule-state mechanism**

---

# 2. Data and measurement

## 2.1 G0: broad phenomenon set

The original phenomenon is measured on **144 frozen items** selected from 180 before
any Exclude condition was generated.

The items span five task families:

1. **legal judgment** — evidence changes a legal or adjudicative rating;
2. **evidence inference** — a new fact shifts a belief or inference;
3. **ranking / selection** — evidence changes which option should be preferred;
4. **outcome evaluation** — evidence changes an assessment of an outcome or case;
5. **numeric aggregation** — evidence contributes to an explicit aggregate.

The common causal structure is the important part. Each item has:

- **Base:** judgment without the target evidence;
- **Admit:** the evidence is explicitly allowed to affect the decision;
- **Exclude:** the same evidence is explicitly assigned zero decision weight;
- **rule timing:** the Admit/Exclude policy is stated before or after the evidence.

This makes the broad phenomenon an order comparison over the **same policy and same
evidence**, with the matched Admit arm separating exclusion-specific timing from a
generic “later instructions are stronger” effect.

### G0 model breadth

The instruct panel covers twelve checkpoints from four vendors, including roughly
3.8B–32B scale models, plus two masked diffusion language models.

The exact instruct panel includes Phi, Gemma, Qwen2.5, Qwen3, Qwen3.5, and
Mistral families. This breadth is used to establish the phenomenon. The later
mechanism is not required to reproduce on all fourteen models.

### G0 readout

For four rating families, the model produces a short rationale and then a fixed-position
digit distribution is converted to a continuous 0–100 rating. This gives a
deterministic continuous behavioral measure with no LLM judge.

The original normalized quantity is **REI**:

- REI = 0 means the decision behaves like Base;
- REI = 1 means the evidence exerts its full admitted effect.

G0 and the discovery rounds use REI where its denominator is stable.

---

## 2.2 G18: the centerpiece confirmation set

The semantic-target account was discovered iteratively in Stage 3C–3E. That process
included a rebuilt similarity manipulation and a later discovery that previewing the
target changes the evidence's baseline leverage. The final explanation therefore
needed a new experiment designed correctly from the start.

G18 is that experiment.

### Freshness and breadth

- **100 fresh items**
- **30 fresh independent skeletons**
- **3 task families**
  - legal judgment: 40
  - evidence inference: 30
  - ranking / selection: 30
- no item-ID or skeleton overlap with the discovery set
- **5 frozen checkpoints from 4 vendors**
- **9,000 generations**

The model panel is:

- Qwen3-8B
- Gemma-3-12B
- Phi-4-mini
- Qwen3.5-27B
- Mistral-Small-24B

The panel was frozen before any G18 output.

### G18 factorial

The later evidence is held fixed. What changes is the representation of its target
available **before the exclusion rule**.

Six target representations:

1. **none** — no information about the target;
2. **identifier** — a referential stub naming the future item, without content;
3. **empty semantic control** — high lexical overlap with the evidence, but a
   different proposition;
4. **paraphrase** — the same proposition in different wording;
5. **entailing-specific** — a more specific statement that entails the future evidence;
6. **unrelated** — unrelated content matched to the paraphrase condition in length.

Each target representation is crossed with three states:

- preview only;
- preview + evidence, no exclusion rule;
- preview + exclusion rule + evidence.

This means every target representation has its **own no-rule baseline**.

### G18 estimand

G18 uses raw sign-aligned rating points, not a leverage-normalized ratio.

For each target representation:

- marg(no rule) measures how much the later evidence adds after the preview;
- marg(exclude) measures how much it adds after preview + exclusion rule;
- **ExclusionEffect = marg(no rule) − marg(exclude)**.

ExclusionEffect therefore measures how much evidence influence the rule removes beyond
whatever the preview already did.

This baseline structure is essential because a semantic preview makes the later
evidence highly redundant.

---

# 3. Claim 1 — models fail to pre-commit to exclusion

## Main claim

> **The same evidence-exclusion policy is systematically less effective when stated
> before the evidence than after it.**

This is the phenomenon that motivates the paper.

Across the twelve instruction-tuned models, the temporal contrast has the same sign in
**12/12 models**, and **10/12 confidence intervals exclude zero**. The matched Admit
condition is approximately order invariant, so the result is not simply that a later
rule always dominates an earlier rule.

Representative G0 values show the scale:

- Phi-4-mini: Exclude-Pre REI +0.50 vs Exclude-Post +0.24
- Gemma-3-12B: +0.43 vs +0.07
- Qwen2.5-32B: +0.30 vs +0.00
- Mistral-Small-24B: +0.19 vs −0.03
- Qwen3-8B: +0.45 vs +0.12
- Qwen3-14B: +0.49 vs −0.07
- Qwen3.5-27B: −0.05 vs −0.29

The newest models sometimes overcorrect, but the **before-vs-after ordering remains**.

The effect also appears in two masked diffusion language models, showing that the
phenomenon is not tied to the standard left-to-right causal prompt mask.

### Why this is worth a paper despite Instruction Position Matters

The broad sign “instruction after input can be stronger” is not itself novel.
The paper's contribution is that, for evidence exclusion, the sign survives after
ordinary instruction-position explanations are weakened, and the later experiments
identify a new variable—target addressability—that controls the failure.

The phenomenon is the entrance to the paper, not the final novelty.

---

# 4. Claim 2 — policy access is not enforcement

## Main claim

> **A model can have explicit access to the exclusion policy without successfully
> enforcing it on later evidence.**

This claim should be stated strongly in the paper. The evidence does not require us to
say that every model has a perfectly preserved hidden policy representation. It is
enough that explicit policy access and causal enforcement demonstrably separate.

### Separate policy probe

When asked separately what weight the evidence should receive, models recover the
zero-weight policy at or near ceiling. This establishes that the prospective failure
is not simply “the model cannot understand the instruction.”

### Decision-trajectory externalisation

The stronger test puts the policy statement inside the model's own decision process.

In Stage 3C:

- Qwen3-8B spontaneously writes exactly 0% on 33% of prospective trajectories vs
  74% retrospectively;
- Gemma-3-12B: 56% vs 69%;
- Phi-4-mini: 77% vs 81%;
- Mistral-24B: 85% vs 79%;
- Qwen3.5-27B: 91% vs 86%.

This shows that policy accessibility inside the trajectory is itself model dependent.

But the decisive result is that **correct policy externalisation is still not always
enough**.

For Qwen3-8B, forcing “ITEM DECISION WEIGHT: 0%” into the trajectory leaves substantial
prospective evidence influence. The on-policy analysis similarly shows that in
Qwen3-8B and Gemma-3-12B, trajectories that explicitly state zero can still leak
prospectively.

Therefore the paper can make the broad conclusion:

> **Knowing or stating the policy is not the same as making the evidence causally
> inert.**

### Supporting localisation

Four supporting results sharpen the interpretation:

- rule-to-evidence delay up to roughly 1,000 tokens does not systematically erase the
  effect;
- rule-to-answer distance has no main effect, and farther rules can even perform better;
- eight natural-language ruling constructions preserve the gap;
- masked diffusion LMs preserve it without a left-to-right prompt mask.

These should occupy one compact paragraph in the main text. They are not four
independent contributions.

---

# 5. Boundary condition — the hard part is making semantic evidence inert

A useful characterization is that the effect is strongest when the rule demands hard
suppression of semantically integrated evidence.

The original requested-weight sweep shows a sharp concentration at zero. However, the
paper should not promote “zero is magical” into a universal theory.

The cleaner boundary is Stage 3C's explicit arithmetic task.

When the contribution is directly computable as base + weight × delta:

- Qwen3-8B: pre/post gap 0.000
- Gemma-3-12B: 0.000
- Mistral-24B: 0.000
- Qwen3.5-27B: 0.000

Phi-4-mini fails the retrospective arithmetic condition and is not evidence against
the boundary.

Thus:

> **Prospective exclusion is not a generic inability to obey future-directed
> weighting instructions. It becomes difficult when the model must infer the semantic
> contribution of evidence and make that contribution causally inert.**

This is a bridge to target addressability, not a separate paper claim.

---

# 6. Claim 3 — target addressability decides prospective exclusion

This is the conceptual center and should be the most memorable section.

## Main claim

> **Prospective exclusion depends on what representation of the future target is
> available when the policy is processed. Specific semantic target representations
> support substantially stronger control than reference or surface resemblance alone.**

G18 prospectively confirms this claim on fresh materials.

## G18 primary result

Pooled ExclusionEffect:

| target representation | ExclusionEffect |
|---|---:|
| entailing-specific | **31.16 [27.99, 34.40]** |
| paraphrase | **30.93 [28.19, 33.66]** |
| identifier | 26.27 [23.65, 28.96] |
| unrelated | 22.06 [19.16, 24.97] |
| none | 21.84 [19.21, 24.66] |
| lexical overlap, wrong proposition | 18.08 [15.71, 20.57] |

The preregistered primary contrast is:

> **Δ_semantic = +8.91 [7.15, 10.76] rating points**

and is positive in **5/5 models**.

Model-wise Δ_semantic:

- Qwen3-8B: +15.29 [10.67, 19.80]
- Gemma-3-12B: +7.57 [4.15, 10.90]
- Phi-4-mini: +4.66 [1.88, 7.59]
- Qwen3.5-27B: +10.41 [6.13, 15.01]
- Mistral-Small-24B: +6.62 [3.54, 9.59]

The cleanest surface-matched contrast is:

> **paraphrase − lexical-wrong-proposition = +12.85 [10.32, 15.42]**

again positive in 5/5 models.

### Scientific interpretation

The result is not that identifiers have zero effect. The stronger and more useful
claim is:

> **The policy's control depends on how well its future target is semantically
> addressable. Arbitrary reference provides some control, but a matching proposition
> provides substantially more; surface resemblance without the proposition does not.**

This is the paper's new regularity.

It is analogous in narrative role to contextual entrainment in Llama See, Llama Do or
structural alignment bias in Tool Irrelevance: a broad known-looking failure becomes a
new scientific object only after the governing variable is isolated.

---

# 7. The G18 decomposition — exclusion can extend beyond the named block

G18 reveals a stronger behavior that the discovery rounds could not measure cleanly.

Under the lexical-wrong-proposition condition:

- marg(no rule) = +32.48
- marg(exclude) = +14.40

The evidence remains influential even after exclusion.

Under a paraphrase of the actual proposition:

- marg(no rule) = +3.27
- marg(exclude) = **−27.66**

The semantic preview makes the later evidence almost redundant, yet the exclusion rule
pushes the judgment far **below the preview-only baseline**.

The sign is:

- negative in **5/5 models** under paraphrase;
- positive in **5/5 models** under the lexical-overlap/wrong-proposition control.

This gives a striking main-text observation:

> **Once the target is semantically identified, exclusion is no longer confined to
> the literal later evidence block named by the rule.**

Two mechanisms are consistent with the behavior:

1. the exclusion policy generalizes to the proposition wherever it appears;
2. the model overcorrects once the forbidden proposition is clearly identified.

The paper does not need to choose between them. Both show that semantic target
identification changes the scope of exclusion.

This result should be a visual panel in Figure 2, not hidden in the appendix.

---

# 8. Discovery experiments that explain why G18 looks this way

The earlier rounds should not be narrated chronologically. They support the explanatory
factor that G18 confirms.

Three findings are worth retaining in the main text.

### 8.1 A future name is not the same as a target

Previewing only an identifier, type, direction, or incomplete stub does not recreate
post-evidence suppression. Full content preview does.

This originally suggested that the problem is not merely “the policy refers to
something in the future,” but what representation of that future object exists at rule
time.

### 8.2 Semantic structure, not string match

Stage 3D finds:

- exact text ≈ paraphrase;
- high lexical overlap with different meaning provides little or no rescue;
- same entity/direction but different fact does not rescue.

Thus the relevant variable is not verbatim overlap.

### 8.3 Content outranks identity

The content × identity 2×2 independently varies whether the previewed content matches
and whether the later label matches the rule.

Across four models:

> **matching content under the wrong label suppresses better than the right label with
> the wrong content.**

This gives the behavioral bridge from “future reference” to “semantic addressability.”

Stage 3E then shows that preview-induced redundancy is real, motivating the raw-point
baseline design that G18 freezes prospectively.

These are discovery evidence. G18 is the load-bearing confirmation.

---

# 9. Claim 4 — semantic control follows information across identifiers in an agent

## Main claim

> **Identifier scope and semantic scope are different control relations: semantic
> exclusion follows the information across a change of document identity, whereas
> identifier-specific protection does not.**

The agent setting uses real chat roles:

**SYSTEM policy → TOOL document → assistant judgment**

The important result is not that identifier policies never work.

In deconfounded Stage 4:

- Gemma-3-12B ID-only policy removes +15.8 rating points of document influence;
- Qwen3.5-27B removes +21.9;
- Qwen3-8B and Phi-4-mini show little ID-only effect.

So the ability to act on a named document differs by model.

The clean invariant appears when the **same proposition moves from D7 to D9**.

ID-only ToolMarginal for D9 is near the no-policy baseline in all four models:

- Qwen3-8B: +23.9 vs no-policy +24.6
- Gemma-3-12B: +28.9 vs +29.2
- Phi-4-mini: +23.2 vs +23.2
- Qwen3.5-27B: +36.5 vs +39.1

A proposition-targeted policy continues to suppress D9 almost as well as D7:

- Qwen3-8B: D7 +14.2 vs D9 +12.3
- Gemma-3-12B: +11.8 vs +10.8
- Phi-4-mini: +11.9 vs +11.8
- Qwen3.5-27B: +27.0 vs +29.0

Therefore:

> **Semantic control tracks information across surface identity; identifier control
> stays attached to the identifier.**

This is the deployment-shaped externalisation of target addressability.

---

# 10. Claim 5 — a target-dependent rule state causally controls later suppression

The mechanism section should answer one question:

> **Does target addressability change the internal state of the rule before later
> evidence arrives, and does that state causally affect whether the evidence is
> suppressed?**

The answer is yes.

## 10.1 The excluded evidence is still causally read

In Qwen3-8B, blocking downstream access to the excluded evidence span moves the answer
back toward the no-evidence Base condition.

This establishes that the residual behavior genuinely depends on later use of the
evidence, rather than being only a static side effect of the earlier rule.

## 10.2 Final resolution happens late

Answer-position patching shows little recovery in lower layers and strong recovery
later in the network.

This separates two stages:

1. an earlier rule-state difference created when the policy is processed;
2. a later decision-level resolution where evidence is finally allowed or suppressed.

## 10.3 Matched-chronology rule-state interchange

The key mechanism experiment compares:

**FAILURE:** unrelated padded preview → exclusion rule → evidence → answer

**SUCCESS:** paraphrase preview → exclusion rule → evidence → answer

The evidence used for the decision comes after the rule in both runs. The preview is
length matched. The only scientific difference is whether a matching target
proposition was available before the rule.

### Qwen3-8B

Behavioral failure-success gap:

> +13.2 [8.6, 18.1] rating points

Rule-span interchange localizes to layers 14–18 / 36:

- installing the failing state into a successful run adds **+13.3 [8.1, 18.9]**
  leakage at layer 14;
- installing the successful state into a failing run produces a smaller but
  significant rescue around **−3.6 [−5.9, −1.4]**.

### Mistral-Small-24B replication

Behavioral gap:

> +18.2 [10.0, 26.9]

A corresponding causal window appears at layers 12–16 / 40:

- rescue reaches **−16.1 [−24.2, −9.0]** at layer 14;
- break reaches **+18.3 [12.6, 24.5]** at layer 12;
- the effect is essentially gone above relative depth 0.45.

Thus the architecture-invariant result is:

> **A target-dependent rule state forms in the middle of the network before the later
> evidence is processed, and causally determines whether that evidence will be
> suppressed.**

The exact rescue/break symmetry is model specific. Qwen is much easier to break than to
rescue; Mistral is nearly symmetric.

### What this mechanism means

This is enough for a strong mechanistic explanation.

It does **not** require claiming that the state is literally a discrete
“TARGET_FOUND” feature, nor that a reusable steering vector exists. In fact, the
shared-direction steering test fails, suggesting an item-specific causal state rather
than a universal one-dimensional control knob.

That limitation does not weaken the central causal claim:

> **Target availability changes the rule computation before later evidence appears,
> and that changed rule computation controls subsequent evidence use.**

---

# 11. The paper's three final contributions

The Introduction should present only three contributions.

## Contribution 1 — Prospective exclusion gap

> Language models systematically struggle more to exclude evidence prospectively than
> after the evidence has appeared, across a broad model and task panel.

Evidence:
- 12 instruct models + 2 diffusion LMs
- 5 task families
- matched Admit control
- policy access / trajectory dissociation

## Contribution 2 — Target addressability

> Prospective exclusion is governed by how the future target is represented when the
> policy is processed. A specific semantic target enables substantially stronger
> control than arbitrary reference or surface resemblance.

Evidence:
- G18 frozen fresh-item confirmation
- Δ_semantic +8.91 [7.15, 10.76]
- 5/5 models positive
- para-empty +12.85 [10.32, 15.42]
- decomposition below preview-only baseline
- agent D7→D9 counterfactual

## Contribution 3 — Causal mechanism

> Target availability changes a mid-network rule state before later evidence is read,
> and interchanging this state changes subsequent evidence suppression.

Evidence:
- evidence-span causal gate
- late answer resolution
- Qwen3-8B causal interchange
- Mistral-Small-24B replication

Everything else supports these three claims.

---

# 12. Figure plan

## Figure 1 — The phenomenon

Goal: the reader should understand the temporal reversal in seconds.

Panel A:
- Exclude-before vs Exclude-after across the 12 instruct models.

Panel B:
- matched Admit-before vs Admit-after, showing no generic order effect.

Panel C, small:
- diffusion-model replication or model-scale grouping if visually useful.

Do not overload Figure 1 with rule probes, distance, or eight paraphrases.

---

## Figure 2 — Target addressability

This is the paper's most important figure.

Panel A:
G18 6×3 factorial schematic.

Panel B:
ExclusionEffect by target representation:
entail / para / identifier / unrelated / none / lexical-wrong-proposition.

Annotate:
- Δ_semantic +8.91
- para-empty +12.85

Panel C:
decomposition for para vs empty:

- para: +3 no-rule → −28 exclude
- empty: +32 no-rule → +14 exclude

The visual message:
**the policy's effect changes when the target is semantically identified, not merely
mentioned or lexically resembled.**

---

## Figure 3 — Externalisation and mechanism

Panel A:
Agent D7→D9 identity counterfactual.

Panel B:
matched-chronology causal-interchange schematic.

Panel C:
Qwen and Mistral layer curves on relative depth.

Optional inset:
evidence-span gate / late answer patching.

---

# 13. Outstanding-shaped alignment

The goal is not to claim Outstanding quality in advance. The goal is to use
Outstanding papers as a design reference so that execution degradation still leaves a
strong Main paper.

## ACL 2025 Outstanding — Llama See, Llama Do

Their structure:

**distraction → contextual entrainment → semantic modulation → entrainment heads →
causal ablation**

The key lesson is that “irrelevant context distracts” is too coarse. The paper wins by
finding a new regularity underneath the known failure and making its mechanism act on
that regularity.

Our counterpart:

**prospective exclusion failure → target addressability → G18 factorization →
target-dependent rule state → causal interchange**

The structural alignment is strong.

Their additional advantage is a direct mitigation-like ablation of entrainment heads.
We do not need to imitate this by inventing a new experiment: our interchange already
causally changes the central behavior, and our behavioral experiments imply concrete
policy-design changes.

## EMNLP 2025 Outstanding — Causal Interventions Reveal Shared Structure

Their scientific contribution is causal theory refinement, not deployment mitigation.
Distributed Interchange Interventions test whether different constructions share an
abstract representation.

This is an important precedent for our mechanism section. The value of our
interchange is that it answers a theory question about prospective exclusion:
**does target availability change a rule state that later controls evidence?**

A new engineering method is not necessary for that contribution to be complete.

## ACL 2024 Outstanding — CausalGym

CausalGym's core standard is that interpretability should be judged by causal efficacy,
not by the ability to decode information from activations.

This supports our hierarchy of evidence:

- separate rule probes: useful behavioral evidence;
- readout correlations: supporting;
- span gate and interchange: mechanism-bearing evidence.

Our paper should emphasize interventions that change behavior, not layer-probe
accuracy.

## NAACL 2025 Main — Racing Thoughts

Their arc is:

**natural contextualization failure → algorithmic hypothesis → causal evidence →
inference-time implications**

Our paper is highly aligned in shape:

**natural prospective exclusion failure → target-addressability explanation → causal
rule state → policy-design implications**

Racing Thoughts also shows that controlled stress tests are legitimate when the goal is
to reveal a model computation rather than build a representative benchmark.

## ACL 2026 Main — Do LLMs Know Tool Irrelevance?

This is the closest factorization analogy.

Their broad failure—unnecessary tool invocation—becomes novel only after structural
alignment is separated from semantic relevance using SABEval.

Our equivalent centerpiece is G18:

- target representation manipulated directly;
- fresh materials;
- semantic / referential / lexical factors separated;
- independent baselines;
- frozen confirmation.

G18 is therefore the experiment that should dominate the narrative, just as SABEval's
factorization dominates theirs.

## EMNLP 2025 Main — Reason to Rote

Reason to Rote uses only two controlled synthetic reasoning tasks but obtains a strong
paper by discovering a counterintuitive mechanism: memorization builds on rather than
bypasses reasoning.

This is a useful workload reference. A mechanistic phenomenon paper does not require a
large natural benchmark if the controlled tasks make the explanatory variable visible
and the mechanism causal.

Our dataset/task breadth is already larger.

---

# 14. Is the mechanism strong enough?

Yes for the intended paper.

The final mechanism does four useful things:

1. connects the behavioral residue to actual continued use of excluded evidence;
2. separates an earlier target-dependent rule state from a later answer decision;
3. causally transfers successful/failing prospective exclusion through that rule state;
4. replicates the core middle-layer causal window in a second architecture.

This is more than a probe-and-heatmap mechanism section.

The mechanism is slightly weaker than the most engineering-oriented Outstanding
examples in one respect: it does not yield a simple reusable cross-item direction or a
fully packaged mitigation.

That is not a fatal gap because:
- the EMNLP Outstanding filler-gap paper is causal-theory work without mitigation;
- CausalGym values causal interventions themselves;
- our causal intervention directly changes the paper's centerpiece behavior.

The correct response is therefore **strong writing and precise mechanistic framing**,
not another GPU round.

---

# 15. Can the explanation lead to a practical method?

Yes conceptually, but the current paper should distinguish **supported implication**
from **new evaluated method**.

Three implications are already experimentally supported.

### 15.1 Re-ground policies after retrieval

The same exclusion instruction is consistently more effective after the evidence has
arrived. A practical agent can therefore re-instantiate or restate a prospective
information-control policy after tool/retrieval output.

### 15.2 Encode meaningful target semantics or provenance

G18 and the tagged-stream experiments show that a meaningful target representation can
support stronger prospective control than an arbitrary resource identity alone.

### 15.3 Separate identifier scope from semantic scope

The D7→D9 agent counterfactual shows that “this document ID is forbidden” and “this
information is forbidden” are not equivalent policies.

A natural future method is therefore a **post-retrieval policy grounding/compiler**
step:

prospective policy
→ retrieval result
→ resolve which retrieved propositions satisfy the policy
→ restate/compile the exclusion against those instantiated targets
→ answer

This method follows directly from the explanation and could be evaluated in a future
engineering paper.

For the current paper, do **not** claim that such a compiler has been built or
validated. The current scientific contribution is the phenomenon and causal
explanation.

---

# 16. What belongs in the main text vs appendix

## Main text

- G0 broad reversal
- compact policy-access dissociation
- one compact localisation paragraph
- arithmetic/hard-suppression boundary in short form
- G18 design and full main result
- G18 decomposition
- agent D7→D9
- Qwen + Mistral mechanism

## Appendix

- full 12-model × 5-family tables
- eight ruling wordings
- distance/delay sweeps
- full weight sweep
- Stage 3 discovery ladder
- content×identity 2×2 full table
- redundancy audit and metric transition
- tagged stream
- full on-policy trajectory analysis
- full agent table
- G16 and G17
- failed shared steering direction
- Stage 5 correction
- readout pilots
- stopped hindsight branch only as repository provenance unless artifact policy
  requires more

The main text should look like a paper that asked one question, not a project that ran
189 commits.

---

# 17. Final narrative in six sentences

1. **Models often cannot decide in advance what evidence to ignore.**
2. **The problem is not simply that the exclusion policy is unavailable.**
3. **Prospective control depends on whether the policy has an addressable target when
   it is processed.**
4. **A fresh confirmatory factorial shows that semantic target representations enable
   substantially stronger exclusion than arbitrary reference or surface resemblance.**
5. **In an agent, semantic control follows information across a change of document
   identity.**
6. **Inside the model, target availability changes a mid-network rule state that
   causally controls whether later evidence is suppressed.**

That is the paper.
