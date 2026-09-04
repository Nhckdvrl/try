# ACL / EMNLP / NAACL alignment standard

The aspiration is **Outstanding-shaped scientific organisation**, with Main as the
realistic acceptance target. The point of using Outstanding papers as references is
not to imitate their page count or add experiments mechanically; it is to copy the way
they turn a broad failure into one memorable scientific regularity and then make the
mechanism act on that regularity.

## 1. Reference papers and what to copy

### ACL 2025 Outstanding — Llama See, Llama Do
https://aclanthology.org/2025.acl-long.791/

Arc:
context distraction → contextual entrainment → semantic modulation → entrainment-head
discovery → head ablation attenuates the behavioral effect.

What makes it Outstanding-shaped:
- the paper does not stop at “irrelevant context hurts”;
- it coins a sharper regularity that is measurable independently;
- mechanism and intervention are explicitly about that regularity;
- the final intervention changes the original behavior.

**Our analogue:** prospective exclusion gap → target addressability → G18 factorial →
target-dependent rule state → causal interchange.

### EMNLP 2025 Outstanding — Causal Interventions Reveal Shared Structure Across
English Filler–Gap Constructions
https://aclanthology.org/2025.emnlp-main.1271/

Arc:
natural theory question about shared structure → Distributed Interchange
Interventions → cross-construction causal transfer → factors that refine linguistic
theory.

What to copy:
- the theory question exists before the MI method;
- causal interchange is valuable because it answers the theory question;
- no deployment mitigation algorithm is required for an Outstanding paper when the
  causal result itself advances understanding.

**Our analogue:** the question is advance commitment to ignore evidence; interchange
tests whether target availability changes the rule state that later controls evidence.

### ACL 2024 Outstanding + SAC — CausalGym
https://aclanthology.org/2024.acl-long.785/

Arc:
behavioral psycholinguistic tests are not enough → benchmark causal interpretability
methods by whether they can change model behavior → identify the strongest method →
use it to discover discrete stages of mechanism learning.

What to copy:
- interpretability evidence is strongest when causal efficacy is measured, not when a
  probe merely decodes information;
- method validation and scientific inference must be separated.

**Our analogue:** separate declarative probes are supporting evidence; span gating and
interchange carry the causal mechanism claim.

### NAACL 2025 Main — Racing Thoughts
https://aclanthology.org/2025.naacl-long.155/

Arc:
natural contextualization failure → Race Conditions Hypothesis → correlational and
causal evidence → inference-time intervention implications.

What to copy:
- a controlled stress test is acceptable when it reveals an algorithmic failure;
- not every alternative account has to be eliminated;
- one coherent causal hypothesis is better than many defensive controls.

### ACL 2026 Main — Do LLMs Know Tool Irrelevance?
https://aclanthology.org/2026.acl-long.1473/

Arc:
tool-refusal failure → structural alignment bias → SABEval factorizes structural
alignment from semantic relevance → competing pathways → rebalancing mitigation.

What to copy:
- the centerpiece experiment factorizes the explanatory variable cleanly;
- the dataset is an instrument for the scientific question;
- a coarse known failure becomes novel when a previously conflated variable is
  separated.

**G18 is our SABEval moment:** target representation is manipulated directly on fresh
materials with its own baselines.

### ACL 2025 Main — Stochastic Chameleons
https://aclanthology.org/2025.acl-long.1458/

Arc:
irrelevant-context hallucination → structured class-based misgeneralization →
lower-layer abstraction / higher-layer answer refinement → competing circuits.

What to copy:
- behavioral errors should reveal a structured regularity, not be presented as random
  failure;
- internal analysis can identify which part of the behavioral abstraction is
  actually implemented.

### ACL 2026 Main — Patches of Nonlinearity
https://aclanthology.org/2026.acl-long.559/

Arc:
instruction representations → causal localization → non-linear interaction →
instruction vectors as circuit selectors.

What to copy:
- “we find an instruction representation” is no longer sufficient novelty;
- the interesting question is what information conditions that representation and how
  it changes downstream computation.

**Our distinction:** the novelty is not an instruction vector; it is that a rule state
depends on whether a semantic target was available before the evidence arrived.

## 2. What Outstanding-shaped papers have in common

### A natural question precedes terminology

Good:
> Can a language model commit in advance to ignore evidence it has not yet seen?

Bad:
> Do prospective semantic-binding states implement zero-weight routing?

The technical term belongs after the phenomenon.

### A centerpiece experiment makes the novelty visible

The reader should be able to point to one figure and say what the new variable is.

For this paper that is **G18**:
- fresh items and skeletons;
- semantic vs referential vs lexical target representation;
- per-preview baselines;
- raw-point ExclusionEffect;
- frozen Delta_semantic.

If Figure 2 does not make target addressability obvious without reading Stage 3
history, the writing has failed.

### Explanation is broader than an estimand but narrower than a universal theory

Strong ACL papers often use a useful scientific abstraction that is not proven in
every imaginable case. Do not shrink the story to “on this six-level factorial the
bootstrap contrast is positive.” Equally, do not inflate it to “all instruction
following requires semantic binding.”

Correct level:
> **For prospective evidence exclusion, how the future target is represented when the
> policy is processed is a causal determinant of later enforcement.**

### Mechanism must touch the center

Main mechanism:
- matched semantic vs unrelated target;
- rule state differs before later evidence;
- interchange changes later suppression;
- replicated in Qwen and Mistral.

Supporting mechanism:
- evidence-span gate;
- late answer-position resolution.

Do not center:
- G16 class-marker bridge;
- failed shared steering direction;
- generic instruction-state decoding.

### Breadth and depth can be distributed

Outstanding/Main papers do not run every mechanism on every behavioral model.

Our division is legitimate:
- phenomenon breadth: 12 instruct + 2 diffusion, five task families;
- explanatory confirmation: five models, three families, 100 fresh items / 30
  skeletons;
- mechanism depth: two architectures.

Do not borrow the 14-model breadth when describing G18, and do not demand 14-model
patching.

## 3. Final project against the bar

| dimension | current evidence | assessment |
|---|---|---|
| Natural question | advance commitment to ignore future evidence | strong |
| Broad phenomenon | G0, 12+2 models, five families | strong |
| Memorable explanatory variable | target addressability | strong after G18 |
| Clean centerpiece | G18 frozen fresh-item factorial | strong |
| Externalisation | SYSTEM→TOOL D7→D9 counterfactual | useful and directly tied to the variable |
| Causal mechanism | matched rule-state interchange in Qwen + Mistral | strong for Main, credible Outstanding-shaped depth |
| Practical method | **ReGround frozen, pending G19** | if successful, closes the largest remaining gap to the engineering-oriented Outstanding/Main references |
| Narrative risk | too many historical experiments and over-strong wording | writing problem, not experiment problem |

## 4. The practical-method question

The authors explicitly chose to reopen the programme once for **ReGround**, because
this is a positive consequence of the confirmed mechanism rather than a defensive
control.

ReGround implements the natural intervention suggested by the paper:

semantic prospective policy
→ retrieval instantiates possible targets
→ resolve policy-to-document matches
→ compile a trusted exclusion ledger
→ decide

The evaluation is deliberately stronger than “repeat the rule”:
- the primary baseline receives the **same semantic policy**;
- a same-position, comparable-length semantic generic reminder controls for recency;
- Semantic-Restate is a strong repeat-the-full-rule baseline;
- same-D9 tests whether the policy follows content across identity;
- wrong-D9 tests lexical similarity without semantic match.

If successful, the final paper adopts the first Outstanding/Main pattern:
phenomenon → factorized explanatory variable → causal mechanism → mitigation.

If it fails, the fixed scientific paper remains valid under the second pattern:
phenomenon/theory → causal mechanism that advances understanding.

## 5. Main-text discipline

The paper should read:

natural policy question
    ↓
broad prospective exclusion gap
    ↓
explicit policy access does not guarantee enforcement
    ↓
G18 factorizes target addressability
    ↓
agent identity swap externalizes the same distinction
    ↓
causal mid-network rule state explains the distinction
    ↓
ReGround mitigation, **only if the frozen G19 gates pass**

It should not read:

G0 → Stage2 → Stage3A → P0-1 → P0-2 → Stage3C → Stage3D → Stage3E → G16 → G17 → G18

Chronology is provenance, not narrative.

## 6. Experiment-stop rule

The explanatory programme closed at G18. It has been **reopened exactly once** for the
frozen G19 ReGround method evaluation by explicit author decision.

No other experiment is reopened merely to:
- include a 70B model;
- obtain a frontier API model;
- close G16/G17;
- add a naturally occurring corpus;
- add a third mechanism model;
- make every mechanism result universal.

Every G19 verdict—success, partial, or no-benefit—closes the programme permanently.
There is no ReGround-v2 before submission.
