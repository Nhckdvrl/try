# Paper frame — authoritative scientific register

**Updated:** 2026-09-03

This file defines the paper's scientific story. Historical development is in `RESEARCH_HISTORY.md`; experiment bookkeeping is in `EXPERIMENTS.md`.

## 1. The question

> **After a language model learns how something turned out, can it still judge the past without hindsight?**

Equivalently: once the outcome is known, can the model evaluate an earlier situation without letting that outcome distort the judgment?

This is the paper's scientific object: **hindsight in language-model reasoning**.

It is deliberately a natural question, not a benchmark construct. BTF-3 gives us a clean place to study it because each item contains a real earlier forecasting situation and a later resolution.

## 2. The headline finding

We give models a historical forecasting question and later evidence revealing how the event resolved. We then ask for the judgment that should be made from the earlier point in time.

Across 256 fresh questions, Qwen, Gemma, and Llama identify with 97.7–100% accuracy that the resolution evidence comes from the future relative to the target judgment. Yet seeing that evidence still changes their probability by 16.02–28.23 points. These three similarly sized, canonical model families form the main behavioral comparison; the originally preregistered Mistral result remains fully reported as an additional heterogeneous family.

The basic result is simple:

> **Knowing that information came later is not enough to keep it from shaping a judgment of the past.**

The paper starts here, but does not stop here.

## 3. What kind of hindsight effect is this?

A natural first explanation is that models simply integrate highly diagnostic evidence about the event they are judging. G8 breaks that link: we replace the event's own resolution packet with a packet from a different resolved event.

Those foreign packets still move the recipient judgment substantially. This first step shows that the hindsight effect is not confined to diagnostic evidence about the target event.

G11 then asks whether this cross-event influence has directional structure. After removing the explicit YES/NO verdict sentence, a future packet supporting YES pulls another question upward and one supporting NO pulls it downward in Qwen, Gemma, and Llama. Mistral is much more dependent on the explicit verdict.

This reveals a more specific regularity beneath the headline hindsight effect:

> **Outcome-shaped later context can pull a judgment of the past toward the outcome it supports, even when that context describes a different event.**

We use **retrospective outcome entrainment** as a name for this discovered regularity. It is an explanatory result inside a paper about hindsight; it is not the scientific object of the paper.

## 4. Does outcome direction causally control the pull?

G12 holds the recipient history and the rest of the prompt fixed, then replaces a verdict-redacted foreign packet supporting NO with a different verdict-redacted packet supporting YES.

The recipient YES probability rises by:

- **+4.41pp** in Qwen;
- **+17.50pp** in Gemma;
- **+18.03pp** in Llama.

Mistral, retained as an additional family, moves only **+1.55pp** and meets the preregistered practical-null rule. The original Qwen/Gemma/Mistral panel verdict therefore remains `indeterminate`; the prospectively added Llama result is a separate positive replication, not a retroactive change to that gate.

This is the behavioral bridge from “later outcomes distort the past” to a mechanistic question: **how does information about an outcome become part of the current decision?**

## 5. How does the outcome influence the decision?

The strong-effect Gemma setting lets us distinguish two internal stories that can produce the same behavioral pull.

**Packet-local transport.** The model could compress the donor outcome into a shared scalar while reading the future packet and carry that scalar forward to the answer.

**Contextual decision construction.** The packet could first be interpreted together with the recipient question, with an outcome-related decision variable becoming causal only later at the answer state.

G13 finds that donor outcome is decodable from packet states, but exchanging the tested one-dimensional packet-local code does not transfer the behavior.

G14 discovers a late answer-position transfer pattern and motivates the recipient-conditioned formulation. G15 then tests that formulation prospectively on a fresh donor assignment.

On the fresh G15 assignment, the behavioral YES-vs-NO donor contrast is **+18.84pp [12.94, 24.97]**. Causal interchange at the answer position is near zero in early layers and reaches **+6.52 to +9.04pp** at layers 29–47; it works in both directions and is near zero for a matched orthogonal direction.

The resulting mechanistic conclusion is:

> **In Gemma, the later outcome becomes causally expressed only after it has been integrated with the current question, in a late answer-position decision state.**

The mechanism is therefore part of the explanation of hindsight, not a separate interpretability contribution bolted onto the paper.

## 6. The paper's explanatory arc

```text
Can models judge the past without hindsight?
                ↓
Later outcome evidence changes the past judgment
although the model knows that evidence came later
                ↓
Even outcomes from unrelated events exert a directional pull
                ↓
Changing the outcome direction of the later evidence changes
which way the same judgment moves
                ↓
In Gemma, that influence becomes causal only after contextual
integration, in a late decision state
```

This is the main paper. Supporting scale, breadth, prompt-reason, failed mitigation, and source-engineering rounds belong in compact characterization or the appendix rather than becoming competing narrative branches.

## 7. Scope

The positive natural evidence comes from one forecasting substrate, with mechanistic analysis in the strongest-effect model. That defines the empirical scope of the current paper; it does not change the natural question.

The next priority is writing and figures. Additional experiments are not part of the default plan. A new experiment is justified only if it answers a new scientific question about hindsight rather than defending the paper against a hypothetical reviewer objection.
