# Research history — from *Unring the Bell* to hindsight

This file preserves **why the question changed** over the life of the project. It is not the paper narrative and not a replacement for the original preregistrations in [`preregistrations/`](preregistrations/).

## 1. Starting question — *Can LLMs Unring the Bell?*

The project began from a familiar intuition: once evidence has been seen, perhaps it is especially hard to ignore when it is later declared inadmissible.

G0 preregistered the prediction that exclusion **after** evidence would be harder than exclusion **before** it.

The result went the other way. Across a broad model panel, models were generally *better* at suppressing evidence when the exclusion instruction came after the evidence. The original *Unring the Bell* headline therefore died.

What survived was more interesting: models could often state that evidence should receive zero weight while still letting it influence a later decision, especially when the rule was given before the evidence arrived.

That reversal started the next phase.

## 2. Controlled phase — prospective nullification

A long controlled program tested why prospective exclusion failed. It varied rule position, distance, weight, target description, tags, explicit weight retrieval, routing structure, and internal representations.

Several apparent explanations were later overturned by cleaner controls. The phase produced real behavioral and mechanistic observations, but the research was becoming increasingly tied to a synthetic prompt grammar: “a future item receives weight zero.”

The important lesson was broader than that grammar:

> a model can know a rule about what information should matter without that rule determining what actually influences the decision.

The submission, however, needed a more natural question.

## 3. Broad phase — Information-Set Reasoning

The project generalized from “weight this item zero” to a broader idea: can a model reason using only the information that belongs to a specified situation while other information is also available?

This motivated experiments across several candidate boundary types.

The program was useful conceptually but too broad empirically. The temporal BTF-3 branch qualified; the perspective-family FANToM branch did not. A later FOMC source attempt also failed its qualification gate.

Instead of forcing a multi-domain story, the project narrowed to the natural temporal phenomenon that was actually strong.

## 4. Return to a natural question — hindsight

BTF-3 contains real forecasting questions at an earlier point in time together with later resolution evidence. That gives a direct version of a very ordinary problem:

> **Once you know how something ended, can you still judge the earlier situation without hindsight?**

The evidence accumulated in three stages:

- 8-item discovery;
- 64-item prospective confirmation;
- 256-item fresh large replication.

In the 256-item replication, the three primary models identify almost perfectly that the resolution evidence came later, yet seeing it still shifts their earlier probability judgments by 7.46–27.73 points.

At this point the project had a strong hindsight phenomenon, but not yet a satisfying explanation of its structure.

## 5. Explanatory turn — outcomes pull other judgments too

### G8 — foreign outcomes

The next question was simple: is the effect only because the model is integrating highly diagnostic future evidence about the very event it is judging?

We replaced that evidence with the resolution of a **different event**.

The foreign resolution still moved the recipient judgment substantially, and the movement tended to follow the donor event's outcome.

### G11 — remove the visible verdict

Removing explicit YES/NO verdict sentences preserved much of the donor-directed pull in Qwen and Gemma, though substantially less in Mistral.

This suggested a more specific regularity beneath the broad hindsight effect:

> outcome-shaped later context can pull a judgment toward the outcome it supports, even when the context describes another resolved event.

We named this **retrospective outcome entrainment**. It is a discovered result, not the paper's top-level scientific object.

### G12 — change outcome direction

For the same recipient history, replacing a NO-supporting foreign packet with a YES-supporting packet moved the YES probability upward in all three primary models: +4.41pp, +17.50pp, and +1.55pp.

The effect is heterogeneous, but the directional relationship motivated a concrete mechanistic question: how does known outcome information become part of the current decision?

## 6. Mechanistic turn — from packet to decision

### G13 — packet-local hypothesis

The first hypothesis was that different future packets compress their outcomes into a shared one-dimensional signal that is then carried to the answer.

Outcome was decodable at packet states, but exchanging that tested packet-local signal did not causally transfer the behavior.

### G14 — answer-site discovery

Moving the intervention to the answer position revealed a late causal pattern. The round did not pass its original composite gate, but it generated a sharper hypothesis: the relevant outcome variable might be **recipient-conditioned**, becoming meaningful only after the future packet is interpreted together with the current question.

### G15 — prospective confirmation

That refined hypothesis was preregistered before a fresh donor assignment was opened.

The fresh behavioral contrast was +18.84pp [12.94, 24.97]. Late answer-position interventions transferred +6.52 to +9.04pp at layers 29–47, worked in both directions, and were near zero for a matched orthogonal direction.

This produced the current mechanistic result:

> **In Gemma, known outcome information becomes causally expressed after contextual integration, in a late decision state.**

## 7. What the failed branches contributed

Several failures mattered because they changed what question the project was asking:

- the original *Unring the Bell* direction reversed;
- the broad multi-boundary program did not qualify beyond the temporal branch;
- G5's deliberation instrument did not produce a clean result;
- G6's first mechanism experiment did not distinguish its intended algorithms;
- G7's external-forecast prediction failed in the opposite direction;
- G9 did not qualify as a second task;
- G10 did not yield a coherent mitigation story.

These results are preserved in `EXPERIMENTS.md`, original preregistrations, results, and Git history. They should not be promoted into equal-weight sections of the paper.

## 8. Current paper

The project has come full circle from a specific *Unring the Bell* prediction to a broader but still natural question:

> **Can language models judge the past without hindsight once they know the outcome?**

The current story is:

```text
known outcomes alter judgments of the past
although models know the evidence came later
        ↓
outcomes from unrelated events still exert a directional pull
        ↓
changing outcome direction changes which way the judgment moves
        ↓
in Gemma, the influence becomes causal after contextual integration
```

The next task is to write this story cleanly. The history explains how we found it; it should not dictate the structure of the final paper.
