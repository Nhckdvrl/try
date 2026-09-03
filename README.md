# Can Language Models Unsee the Future?

## How known outcomes shape judgments of the past

This project studies one natural question:

> **After a language model learns how something turned out, can it still judge the past without hindsight?**

The answer, in our current experiments, is often **no**. Models can correctly recognize that a piece of evidence became available only later, yet knowing that later evidence still changes what they say about the earlier situation.

The paper is therefore about **hindsight in language-model reasoning**.

## Start here

1. [`CLAUDE.md`](CLAUDE.md) — default project instructions, research style, environment, GPU, and Git policy.
2. [`PAPER_FRAME.md`](PAPER_FRAME.md) — the current scientific story.
3. [`ACL_EMNLP_ALIGNMENT_STANDARD.md`](ACL_EMNLP_ALIGNMENT_STANDARD.md) — the quality bar learned from strong ACL/EMNLP/NAACL Main and Outstanding papers.
4. [`EXPERIMENTS.md`](EXPERIMENTS.md) — compact registry of every experimental round.
5. [`preregistrations/`](preregistrations/) — original preregistration documents for exact designs, thresholds, and frozen hypotheses.
6. [`RESEARCH_HISTORY.md`](RESEARCH_HISTORY.md) — how the project evolved from *Unring the Bell* to the current hindsight question.
7. [`PAPER_OUTLINE.md`](PAPER_OUTLINE.md) — paper structure and figure plan.
8. [`RELATED_WORK_2026.md`](RELATED_WORK_2026.md) — conceptual positioning.

## The result in one paragraph

On a fresh 256-question natural forecasting set, the canonical Qwen, Gemma, and Llama comparison identifies at 97.7–100% accuracy that the supplied resolution evidence comes from after the historical point being judged. Nevertheless, seeing that evidence shifts their earlier probability judgments by 16.02–28.23 points. The effect becomes more revealing when the future evidence comes from a **different resolved event**: verdict-redacted outcome evidence still pulls the current judgment in the direction it supports. Replacing NO-supporting later evidence with YES-supporting later evidence moves the same recipient judgment upward by 4.41–18.03 points across these three families. Mistral remains fully reported as an additional family with a broad hindsight effect but a much weaker directional effect. In the strongest mechanistic setting, Gemma, causal interventions show that outcome influence becomes effective only after later evidence has been integrated with the current question, in a late answer-position decision state.

## Scientific story

### 1. Models know which evidence came later — and are still influenced by it

BTF-3 gives us real historical forecasting situations with information available before a cutoff and a later resolution. We compare the same earlier judgment with and without the later resolution evidence and separately ask whether the model recognizes that the evidence comes from the future relative to the target time.

Recognition is near perfect. Hindsight influence remains large.

### 2. Hindsight is not confined to the event being judged

We then replace the event's own resolution evidence with the resolution of a different event. These unrelated future packets still move the judgment substantially, showing that the influence is not confined to evidence about the target event.

Removing the explicit YES/NO verdict sentence reveals a directional pull in Qwen, Gemma, and Llama: evidence supporting YES pulls upward and evidence supporting NO pulls downward. We call this discovered regularity **retrospective outcome entrainment**: outcome-shaped later context can pull a judgment of the past toward the outcome it supports.

### 3. Outcome direction controls the pull

In a paired intervention, the recipient question stays fixed while a NO-supporting foreign future packet is replaced by a YES-supporting one. The recipient YES probability rises by +4.41pp in Qwen, +17.50pp in Gemma, and +18.03pp in Llama. Mistral's additional-family result is +1.55pp and practically null under its frozen threshold.

The effect size is model-dependent, but the directional structure is consistent.

### 4. In Gemma, the influence becomes causal late in the decision

A mechanistic experiment asks whether outcome information is carried forward as a shared packet-local scalar or becomes causal only after the future evidence is interpreted together with the current question.

The tested packet-local scalar is decodable but does not causally transfer the behavior. A fresh prospective confirmation instead finds a late answer-position state whose interchange transfers 6.52–9.04 probability points at layers 29–47, works in both directions, and is near zero for a matched orthogonal direction.

This gives the paper a positive explanatory arc:

```text
hindsight changes judgments of the past
        ↓
unrelated outcomes still exert directional pull
        ↓
outcome direction causally controls that pull
        ↓
in Gemma, the influence becomes causal after contextual integration
```

## Where the project came from

The project began as *Can LLMs Unring the Bell?* The original prediction was actually reversed: models were often better at suppressing evidence when the exclusion instruction came after the evidence than before it. That failure led through a controlled prospective-nullification program, then a broader Information-Set Reasoning attempt, and finally to the natural hindsight problem studied here.

That chronology is preserved in [`RESEARCH_HISTORY.md`](RESEARCH_HISTORY.md). It is important scientific history, but it is not the paper's main narrative.

## Current priority

The experimental program is not looking for more defensive controls. The priority is to write the strongest, cleanest version of the paper: introduction, figures, main results, mechanism, related work, and appendix.

See [`EXPERIMENTS.md`](EXPERIMENTS.md) for the full experimental record and [`REPRODUCE.md`](REPRODUCE.md) for execution entry points.
