# Related work — advance commitment to ignore evidence

The paper asks:

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

Five neighbouring questions, positioned positively. None of these is an objection to
answer; each is a place where our result sharpens or corrects an existing account.

## 1. Instructed disregard in people

Our preregistration was borrowed from this literature. A meta-analysis over 48
studies and 8,474 participants finds that jurors told to disregard evidence they
have already heard retain its influence, and can be *more* influenced after the
instruction (<https://pubmed.ncbi.nlm.nih.gov/16906469/>). Related work on hindsight
and the curse of knowledge documents the same general asymmetry between knowing now
and judging then.

We predicted the same ordering in models and got the opposite one. The human
literature therefore enters the paper as the source of a falsified prediction, not
as an analogy the results are then bent to fit. We make no claim that models
implement the human process.

## 2. Instruction position and instruction following

### *Instruction Position Matters in Sequence Generation* — ACL 2024 Findings
<https://aclanthology.org/2024.findings-acl.693/>

Liu et al. find that moving a task instruction *after* the input improves
performance, and attribute it to instruction forgetting over long inputs.

Our headline has the same sign and a different cause. In our setting the model has
not forgotten anything: a separate probe returns the required weight as exactly zero
on 100% of items in both arms, rule-to-answer distance has no main effect, and
within the prospective arm placing the rule *further* from the answer helps. The
same behavioural regularity therefore has an explanation other than forgetting when
the instruction is a suppression policy rather than a task description.

### *Did You Forget What I Asked? Prospective Memory Failures in LLMs* — 2026
<https://arxiv.org/html/2603.23530>

Compliance with deferred instructions degrades under concurrent load, and a salience
enhanced format recovers most of it. This is the closest existing framing to ours and
the contrast is the point: prospective-memory work asks whether the model remembers
to act. We hold retrieval constant at ceiling and ask whether a remembered policy
governs the decision. Our rule-to-evidence delay sweep — the gap intact out to ~1,000
tokens in four of six models — separates the two directly.

### Instruction hierarchy
<https://arxiv.org/pdf/2404.13208>, <https://aclanthology.org/2026.findings-acl.1960/>

This line assumes that a higher-privilege instruction, given earlier and from a more
trusted source, should dominate. Our agent result is a limiting case for that
assumption: a `SYSTEM`-level policy naming a document that has not yet been retrieved
is worth *nothing* relative to no policy at all in two of three models, while the
identical policy delivered after the tool output works. Privilege and position do not
determine enforcement; binding does.

## 3. Distraction and irrelevant context

### *Llama See, Llama Do* — ACL 2025 Outstanding
<https://aclanthology.org/2025.acl-long.791/>

Niu et al. show that tokens which appeared in context receive increased output
propensity even when random, identify entrainment heads, and attenuate the behaviour
by ablating them. It is the structural model for this paper: a coarse behavioural
failure becomes informative once the regularity beneath it is found, and the
mechanism earns its place by acting on that regularity.

The phenomena are different. Contextual entrainment is driven by token occurrence and
modulated by semantics; our effect is null under high lexical overlap with different
meaning and strong under a reworded paraphrase, so it is governed by propositional
content rather than by surface form.

### *Stochastic Chameleons* — ACL 2025 Main
<https://aclanthology.org/2025.acl-long.1458/>

Irrelevant cues produce structured class-based misgeneralisation rather than noise,
linked to competing internal computations. It is why "irrelevant context hurts" is
not a sufficient framing for our result either: our evidence is not irrelevant, it is
*prohibited*, and the model agrees that it is prohibited.

### *Large Language Models Can Be Easily Distracted by Irrelevant Context* — ICML 2023
<https://arxiv.org/abs/2302.00093>

The origin of the distraction line. Our contribution relative to it is that the
governing variable is not the presence of the extra material but the structure of the
policy that is supposed to exclude it.

## 4. Suppression and unlearning at inference time

### *Answer When Needed, Forget When Not* — ACL 2025 Findings
<https://aclanthology.org/2025.findings-acl.1276.pdf>

Models instructed to unlearn knowledge in context "pretend to forget": the decision to
emit a forgetting token is made only in the final layer, with the answer represented
internally before that.

This is the closest mechanistic neighbour and it is complementary. They study
suppression of *recall* of parametric knowledge; we study suppression of *evidential
weight* of in-context material, and find the same late-resolution shape — nothing
below layer 18, 50% recovery at 21 of 36 — plus the variable that decides whether the
gate closes at all.

### *Self-Blinding and Counterfactual Self-Simulation* — 2026
<https://arxiv.org/abs/2601.14553>

Prompting a model to ignore biasing information fails and sometimes backfires;
querying a genuinely blinded replica works better. That is a mitigation result for
demographic bias. Ours locates when in-context instructed ignoring works — it does,
reliably, once the policy can bind to content — which is why a structural fix inside
one context is available here.

## 5. Mechanistic accounts of contextualisation and competing pathways

### *Racing Thoughts* — NAACL 2025 Main
<https://aclanthology.org/2025.naacl-long.155/>

Contextualisation errors explained by a race condition between token-processing
steps, with causal interventions on processing order. The methodological model: the
mechanism must explain the headline failure. Our span gate, late patching curve and
matched-chronology interchange all target the pre/post gap itself.

### *Causal Interventions Reveal Shared Structure Across English Filler–Gap Constructions* — EMNLP 2025 Outstanding
<https://aclanthology.org/2025.emnlp-main.1271/>

Interchange interventions used to answer a theory question about shared abstract
structure. Our G16 has the same shape: whether tag-bound and identifier-bound
prospective policies differ in one causally exchangeable state.

### *Do LLMs Know Tool Irrelevance?* — ACL 2026 Main
<https://aclanthology.org/2026.acl-long.1473/>

A natural failure, an explanatory latent variable that separates semantic relevance
from structural alignment, then competing pathways that explain the wrong action.
The closest analogue to our descent: not "models cannot follow exclusion rules", but
*what the policy can be resolved against* determines whether it governs the decision.

## 6. Position of the present paper

The surrounding literature establishes that instruction position affects compliance,
that deferred instructions decay under load, that irrelevant context exerts
structured influence, and that instructed forgetting can be superficial.

We study the case where the model demonstrably holds the policy and still fails to
apply it, and show that the deciding factor is neither memory nor position but what
the policy can bind to. A named future item cannot be bound and is worse than saying
nothing; propositional content and class markers carried on the evidence can be, and
make prospective exclusion work — in vignettes and in an agent. The excluded material
is still read at the decision, gating is resolved late, and the binding state
transfers causally between matched runs.

That is the positive positioning the introduction and related-work section should
preserve.
