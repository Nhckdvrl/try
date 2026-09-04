# Related work — advance commitment to ignore evidence

The paper asks:

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

and isolates one dependency:

> **When a policy is processed before its evidential target exists, the target
> representation itself affects whether that policy later controls the evidence.**

The novelty claim must be built on this dependency. “LLMs are bad at ignoring things,”
“early instructions are weaker,” and “instruction states exist” are all occupied
territory.

## 1. Occupied neighbouring questions

| work | established question/result | remaining distinction |
|---|---|---|
| **I3C**, NAACL 2024 Main — https://aclanthology.org/2024.naacl-long.379/ | identify irrelevant conditions and instruct models to ignore them across math datasets | the irrelevant condition is already present when judged; no not-yet-instantiated target |
| **IHEval**, NAACL 2025 Main — https://aclanthology.org/2025.naacl-long.425/ | instruction hierarchy conflicts across system/user/history/tool | co-present instruction conflict, not prospective evidence targeting |
| **COMPASS**, ACL 2026 Main — https://aclanthology.org/2026.acl-long.2139/ | organization policy following; denylist/prohibition failures are severe | establishes prohibition difficulty but not what representation of a future target controls enforcement |
| **Instruction Position Matters**, ACL 2024 Findings — https://aclanthology.org/2024.findings-acl.693/ | instructions after input can outperform instructions before input | same coarse sign, but target representation is not manipulated or explained |
| **Prospective-memory failures**, 2026 — https://arxiv.org/abs/2603.23530 | deferred instructions degrade under load and reminders help | primarily asks whether the model remembers to execute a future action |
| **LoCoMo-Plus**, ACL 2026 Main — https://aclanthology.org/2026.acl-long.1150/ | semantically disconnected cue/trigger dependencies in long-term agent memory | retrieval of a past cue is the bottleneck; our policy is already in context |
| **Patches of Nonlinearity**, ACL 2026 Main — https://aclanthology.org/2026.acl-long.559/ | causal instruction representations and circuit selection | an instruction state itself is not our novelty; target-dependent conditioning of the rule state is |
| **Semantic Gravity Wells**, 2026 — https://arxiv.org/abs/2601.08070 | negative output constraints can backfire through forbidden-token priming and late override | forbidden output tokens, not causal weighting of in-context evidence; our semantic preview improves rather than primes the forbidden target |

## 2. Human instructed disregard

The G0 preregistration was motivated by human inadmissible-evidence research. A
meta-analysis of 48 studies and 8,474 participants reports persistent influence of
evidence after people are instructed to disregard it:
https://pubmed.ncbi.nlm.nih.gov/16906469/

The paper should not claim that we ran a matched human comparison. Correct framing:

> **A human-literature-motivated preregistered prediction was reversed in LLMs.**

The human work supplies the motivating hypothesis, not a claim of shared or opposite
cognitive mechanism.

## 3. Instruction position, prospective memory and hierarchy

**Instruction Position Matters in Sequence Generation**
https://aclanthology.org/2024.findings-acl.693/

The same broad before/after sign is therefore not our novelty. Our contribution starts
after that observation: explicit policy access remains available, ordinary distance
does not explain the gap, and G18 manipulates the representation of the future target
while holding the later evidence fixed.

**Prospective memory**
https://arxiv.org/abs/2603.23530

The closest conceptual overlap is the requirement to act on an earlier instruction
later. Our stronger dissociation is that in some models an explicitly recovered or
teacher-forced zero-weight policy still fails to make the evidence causally inert.
Thus policy accessibility and evidence enforcement can separate.

**Instruction hierarchy / system policy**
https://aclanthology.org/2025.naacl-long.425/
https://aclanthology.org/2026.acl-long.2139/

Our agent setting does not rely on a lower-priority conflicting instruction. The
important counterfactual is scope: an identifier policy can protect its named D7, but
that protection does not follow the same proposition to D9, whereas proposition-level
control does.

## 4. Irrelevant context and distraction

### ACL 2025 Outstanding — Llama See, Llama Do
https://aclanthology.org/2025.acl-long.791/

This is the closest Outstanding-shaped narrative reference. It turns the broad problem
of distraction into a sharper regularity, **contextual entrainment**, then identifies
entrainment heads and attenuates the behavior by ablating them.

Our phenomenon is not generic distraction: the evidence is decision-relevant but
explicitly prohibited. Our corresponding explanatory move is **target addressability**,
confirmed prospectively in G18. High lexical overlap with the wrong proposition does
not reproduce the semantic-target effect.

### ACL 2025 Main — Stochastic Chameleons
https://aclanthology.org/2025.acl-long.1458/

Irrelevant-context errors are shown to be structured class-based misgeneralization
with competing internal computations. This supports our narrative standard: a failure
becomes scientifically valuable when it reveals a structured variable beneath the
error, not because “extra context hurts.”

## 5. In-context suppression and unlearning

**Answer When Needed, Forget When Not**
https://aclanthology.org/2025.findings-acl.1276/

This work studies selective suppression of parametric knowledge and finds late-layer
“pretend to forget” behavior. Our object is different: controlling the causal
contribution of newly provided in-context evidence. The mechanistic similarity—late
decision-level resolution—is a useful neighbour, while target addressability is an
additional variable specific to prospective evidence control.

**Self-Blinding and Counterfactual Self-Simulation**
https://arxiv.org/abs/2601.14553/

This work shows that simply asking a model to ignore biasing information can fail and
proposes genuinely blinded alternatives. Our paper does not compete on mitigation; it
asks when an in-context exclusion policy succeeds and identifies the target
representation as a determinant.

## 6. Mechanistic interpretability references

### NAACL 2025 Main — Racing Thoughts
https://aclanthology.org/2025.naacl-long.155/

Natural contextualization failure → algorithmic race hypothesis → correlational and
causal evidence → inference-time implications. It is the closest NAACL structural
reference for our behavior-to-mechanism descent.

### EMNLP 2025 Outstanding — Causal Interventions Reveal Shared Structure
https://aclanthology.org/2025.emnlp-main.1271/

Distributed Interchange Interventions answer a pre-existing theory question about
shared structure. This is an important precedent for our mechanism: causal transfer
does not need to become a deployment algorithm to be scientifically central when it
tests the paper's explanatory claim.

### ACL 2024 Outstanding — CausalGym
https://aclanthology.org/2024.acl-long.785/

CausalGym evaluates interpretability methods by their ability to alter behavior and
then uses the strongest method to study mechanism learning. This is why our mechanism
claim rests on causal span gating and interchange, not on the fact that a probe can
decode policy information.

### ACL 2026 Main — Do LLMs Know Tool Irrelevance?
https://aclanthology.org/2026.acl-long.1473/

This is the closest factorization reference: structural alignment is separated from
semantic relevance in a dedicated controlled benchmark, then traced to competing
pathways and mitigated.

G18 plays the analogous centerpiece role for this paper:
- future target representation is directly manipulated;
- fresh items/skeletons are used;
- every target representation has its own baseline;
- the semantic contrast is frozen prospectively.

## 7. Positioning of the present paper

Prior work establishes that:
- irrelevant information can distract models;
- models can fail to obey prohibitions and policy hierarchies;
- instruction position affects compliance;
- deferred instructions can be forgotten;
- instruction representations can be causally localized.

We study a dependency not isolated by these lines:

> **When an exclusion policy is processed before its evidential target exists, what
> representation of that target is needed for the policy to control the target's later
> causal contribution?**

G18 confirms that sufficiently specific semantic target representations support
substantially stronger exclusion than referential or merely surface-similar
representations. The agent identity-swap shows that semantic and identifier scope
remain distinct in a SYSTEM→TOOL setting. Matched rule-state interchange then shows
that target availability causally changes a mid-network state that controls later
suppression in two architectures.

## 8. Retrieval-time control and mitigation

Two 2026 neighbours are useful for positioning the method without overclaiming novelty.

**SPARKLE**, ACL 2026 Main
https://aclanthology.org/2026.acl-long.1793/

SPARKLE introduces a separate proxy model that learns an adaptive retrieval policy and
decides when/how to retrieve. ReGround also separates a control module from the final
LLM decision, but its object is different: retrieval has already happened, and the
module resolves a pre-existing **exclusion policy** to the concrete documents that
arrived. ReGround uses no RL or model training.

**EPRAG**, Knowledge-Based Systems 2026
https://www.sciencedirect.com/science/article/pii/S0950705126016552

EPRAG performs epistemic diagnosis and action selection over multi-source enterprise
RAG evidence. It shows that retrieval-time governance can benefit from an explicit
policy layer. ReGround studies a narrower causal problem: how a semantic policy stated
before retrieval is instantiated against its later evidential targets so that those
targets become causally inert in the final decision.

These works mean the paper should not claim “the first policy layer for RAG” or “the
first post-retrieval control system.” The method contribution, if G19 succeeds, is the
**mechanism-derived grounding operation** tied specifically to the target-addressability
phenomenon established in this paper.

## 9. ReGround positioning

ReGround is prospectively frozen as G19. All fair primary baselines receive the same
semantic policy. The method adds one operation after retrieval: resolve that policy to
the actual matching document IDs and compile a trusted exclusion ledger.

The decisive controls are:
- Semantic-Pre: same semantic policy, no grounding;
- Semantic-Generic: same policy plus a comparable-length post-retrieval reminder;
- Semantic-Restate: repeat the full semantic policy after retrieval;
- wrong-D9: lexical overlap without proposition match.

If successful, the claim is:

> **Explicit post-retrieval grounding makes a prospective semantic exclusion policy
> more reliable and selective.**

It is not a claim that ReGround solves access control, RAG security, or arbitrary
identifier-only policies in general.



The paper should be explicit that it is primarily a **phenomenon + causal explanation**
paper, not a new mitigation paper.

Existing experiments nevertheless support practical implications:
- restating a policy after retrieval is more reliable;
- semantic/provenance targeting is safer than assuming an arbitrary resource name
  defines semantic scope;
- identifier and semantic scope should be represented separately in agent policies.

A post-retrieval policy-grounding/compiler step is a natural future method, but has not
been evaluated here and is not claimed as a contribution.
