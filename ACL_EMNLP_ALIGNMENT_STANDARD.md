# ACL / EMNLP / NAACL alignment standard — post-novelty reset

The target is **Outstanding-shaped scientific organisation**, with NAACL Main as the
realistic acceptance goal. The point is not to imitate page count or add experiments
mechanically. The point is to copy how strong phenomenon papers turn an intuitive
failure into a **non-obvious computational regularity** and then make the mechanism
test that regularity.

The previous framing—"semantic target information helps prospective exclusion"—fails
this standard because the reader can predict it before seeing the experiment.

## 1. Reference papers

### ACL 2025 Outstanding — Llama See, Llama Do
https://aclanthology.org/2025.acl-long.791/

Arc:
context distraction → **contextual entrainment** → semantic modulation → entrainment
heads → causal ablation.

Lesson:
"irrelevant context hurts" is not enough. The paper earns its identity by exposing a
sharper regularity that was not obvious from the coarse failure.

Our target analogue:
prospective exclusion paradox → **binding deadline / scope collapse** → causal
rule-state computation.

Not:
prospective exclusion paradox → "more semantic detail helps".

### NAACL 2025 Main — Racing Thoughts
https://aclanthology.org/2025.naacl-long.155/

Arc:
contextualization errors → **Race Conditions Hypothesis** → causal tests of dependency
ordering → intervention implications.

This is now the closest narrative reference.

The useful lesson is that a model can possess all relevant information by final-answer
time yet still fail because one computation had to be resolved **before another
computation formed**.

Our potential analogue:
> the target may have to be instantiated before the exclusion rule is processed;
> revealing it later but still before evidence/answer may be too late unless the rule
> is reprocessed.

That is an algorithmic ordering claim, not a prompt-position observation.

### ACL 2026 Main — Do LLMs Know Tool Irrelevance?
https://aclanthology.org/2026.acl-long.1473/

Arc:
known tool-refusal failure → **structural alignment bias** → factorized controlled
benchmark → competing internal pathways → mitigation.

Lesson:
a coarse failure becomes Main-worthy when the paper separates two variables that
previous evaluations conflate.

Our candidate factorization after the reset:
- **binding strength** — does the rule actually control the future target?
- **scope precision** — does it control only the intended evidence source/occurrence?

If G20 and G21 pass, the paper exposes a genuine control trade-off rather than a
specificity benefit.

### EMNLP 2024 Main — Representational Analysis of Binding
https://aclanthology.org/2024.emnlp-main.967/

This paper already studies entity–attribute binding and Binding IDs, including causal
editing in a low-rank subspace.

Lesson:
generic "binding" is occupied. Our use of the word must be narrower:
**binding a control policy to a future evidence instance/source**.

Do not claim novelty from discovering that LLMs bind semantic objects internally.

### ACL 2026 Main — Patches of Nonlinearity
https://aclanthology.org/2026.acl-long.559/

This paper localizes instruction representations and finds that instruction vectors can
act as circuit selectors conditioned on earlier task representations.

Lesson:
"we found an instruction state in mid layers" is not enough.

Our Stage-5 result matters only if it supports the new computation:
- target state present at rule time vs revealed later;
- semantic identity vs provenance/source identity.

### ACL 2024 Findings — Instruction Position Matters
https://aclanthology.org/2024.findings-acl.693/

Already establishes that moving instructions after the input can improve following.

Lesson:
the G0 before/after sign is the entrance, not the novelty.

G20 must keep the rule fixed and move **target resolution** across the rule boundary.

### COLING 2025 — Chain-of-Specificity
https://aclanthology.org/2025.coling-main.164/

Explicitly emphasizing more specific constraints improves adherence.

Lesson:
"make the target more specific" is already a method-level idea and is too normal for
our scientific headline.

### NAACL 2024 Main — I3C
https://aclanthology.org/2024.naacl-long.379/

Identifies irrelevant conditions, verifies them, then explicitly instructs the model to
ignore them.

Lesson:
"identify target then tell the model to ignore it" is occupied in spirit. This is why
the cancelled ReGround design cannot carry paper novelty.

## 2. What the post-reset paper must achieve

### A. One non-obvious computational statement

A reader should not be able to predict the central result from common sense.

Candidate G20 statement:
> **An unresolved control rule has a binding deadline: target information arriving
> after rule processing does not reliably update it, even though it arrives before the
> evidence and final decision. Replaying the rule after target revelation repairs the
> failure.**

Candidate G21 statement:
> **Semantic binding can destroy provenance scope: excluding Source A suppresses an
> independent, explicitly admissible Source B when B expresses the same proposition.**

Both are substantially sharper than:
> semantic target information helps.

### B. The centerpiece must distinguish the new account from the obvious one

For G20, the obvious specificity account predicts:
- PRE target and LATE target should both help because the same semantic information is
  available before the answer.

The binding-deadline account predicts:
- PRE > LATE;
- replaying the same rule after late target revelation selectively repairs LATE.

For G21, a benign-generalization account predicts:
- a source-scoped rule should preserve B because B is explicitly allowed.

Scope-collapse predicts:
- B loses evidence weight only when it is semantically equivalent to excluded A.

### C. Mechanism must touch the new variable

Existing Stage 5 already shows:
- target-dependent rule state;
- mid-network localization;
- state exists before later evidence;
- causal interchange changes suppression;
- Qwen + Mistral replication.

If G20 passes, the ideal mechanistic result is not another layer localization. It is:
> late target revelation fails to reconstruct the successful rule state until rule
> replay.

If G21 passes:
> causal suppression follows proposition identity more strongly than provenance/source
> identity.

### D. Breadth should not replace novelty

Already sufficient:
- G0: 12 instruct + 2 diffusion / five families;
- G18 diagnostic: five models / three families / fresh set;
- mechanism: two architectures.

New experiments should prioritize clean causal discriminations, not model-count
inflation.

## 3. Current project against the higher bar

| dimension | current status | judgment |
|---|---|---|
| Natural question | future evidence control | strong |
| Broad surprising phenomenon | G0 reversal | strong |
| Old explanation | semantic target helps | **too obvious; retired** |
| G18 | excellent deconfounded diagnostic | valuable evidence, not novelty center |
| Existing mechanism | two-architecture causal rule state | strong asset |
| New explanatory object | binding deadline | high novelty if confirmed |
| New failure object | semantic source-scope collapse | high novelty if confirmed |
| Practical relevance | source/document/tool policies | strong if G21 transfers to agent roles |
| New method | ReGround | cancelled as too obvious |

## 4. Outstanding-shaped target story

Ideal final arc:

natural policy problem
    ↓
prospective exclusion paradox
    ↓
**binding deadline**:
late target information does not retroactively update an already processed rule
    ↓
**scope collapse**:
when semantic binding succeeds, it can cross source/occurrence boundaries
    ↓
causal target-dependent rule state formed during rule processing
    ↓
control problem:
models struggle to bind future rules both **strongly and precisely**

This is stronger than simply appending a mitigation.

## 5. Figure standard

### Figure 1
The broad paradox. Reviewer should understand it in ten seconds.

### Figure 2
If G20 passes, a 2x2 target-timing × rule-replay figure should visually establish the
binding deadline.

### Figure 3
If G21 passes, show retained contribution of allowed Source B by semantic relation.
The striking visual should be:
same proposition → B suppressed;
lexical lookalike / unrelated → B retained.

### Figure 4
Mechanism on relative layer depth, tied explicitly to the rule-processing computation.

G18 becomes a bridge/diagnostic, not the hero figure.

## 6. Experiment discipline

Active novelty-driven work only:
- G20 Binding Deadline
- G21 Source-Scope Collapse

Do not run:
- cancelled ReGround G19;
- another target-specificity ladder;
- generic reminder/restatement as a paper contribution;
- model-size sweep;
- third mechanism model before new behavior is confirmed;
- additional "semantic vs identifier" experiment without a binding-time or
  provenance-scope question.

If G20/G21 fail, the right response is to reconsider the paper, not to revive the
obvious story.
