# Paper outline

**Updated:** 2026-09-03

The paper should feel like one scientific investigation, not a sequence of defenses. The main arc is:

> **hindsight → directional outcome pull → causal outcome manipulation → late contextual decision state**

## Title

Recommended:

> **Can Language Models Unsee the Future? How Known Outcomes Shape Judgments of the Past**

Other viable forms:

- *Can Language Models Judge the Past without Hindsight?*
- *The Future Pulls the Past: Hindsight in Language Model Reasoning*

The title should keep **hindsight / judging the past** as the object. `Retrospective outcome entrainment` is a result discovered inside the paper, not the title-level object.

## Abstract draft

> Once an outcome is known, can a language model still judge an earlier situation without hindsight? We study this on natural forecasting questions whose later resolutions are known. Across three similarly sized, canonical open-model families, models identify with 97.7–100% accuracy that resolution evidence became available only after the historical point they are asked to judge. Yet seeing that evidence shifts their earlier probability judgments by 16.0–28.2 points. We then ask what structure this hindsight effect has. Resolution evidence from an unrelated event still moves the current judgment, and verdict-redacted evidence pulls Qwen, Gemma, and Llama toward the outcome it supports. In a paired intervention, replacing NO-supporting later evidence with YES-supporting later evidence raises the same recipient probability by 4.4–18.0 points across these families. A fully reported additional Mistral checkpoint shows the broad hindsight effect but a weaker, verdict-dependent directional effect. Finally, in the strongest mechanistic setting, we test how this outcome influence enters the decision. A shared packet-local outcome code is decodable but does not causally transfer behavior. Instead, a prospectively confirmed late answer-position state transfers 6.5–9.0 probability points after the later evidence has been integrated with the current question. These results show that language models can know which information came later while still allowing known outcomes to reshape judgments of the past, and reveal a directional pathway through which hindsight enters the decision.

## 1. Introduction — Can a model judge the past after it knows the ending?

Open with ordinary situations where retrospective judgment matters:

- evaluating an earlier forecast after the event resolved;
- auditing a past decision with information learned later;
- asking what an actor could have concluded before the outcome was known.

The difficulty is universal: once the ending is known, it is hard to reason as though it were not.

Then ask the paper's question:

> **Can language models judge the past without hindsight once they know the outcome?**

The introduction should make three contributions, positively:

1. **Phenomenon.** Known outcomes substantially change judgments of the past even when models correctly identify the evidence as later.
2. **Structure.** The influence is directional: outcome-shaped context from unrelated events pulls judgments toward the outcome it supports.
3. **Mechanism.** In Gemma, this outcome influence becomes causally effective after contextual integration in a late decision state.

Do not spend the introduction enumerating every alternative explanation tested in the repository.

## 2. Studying hindsight with natural resolved events

Introduce BTF-3 only here, after the question is clear.

Each item provides:

- an earlier forecasting situation;
- information available at that time;
- a later resolution packet;
- a realized YES/NO outcome;
- a continuous probability judgment.

The core comparison is intuitive: ask for the earlier judgment with versus without seeing the later resolution evidence. A separate timing probe asks whether the model knows that the evidence became available only after the target time.

Explain the 8-item discovery → 64-item prospective confirmation → 256-item fresh replication briefly. Technical sampling, transformation, and freeze details go to the appendix / preregistration archive.

## 3. Knowing the timing does not remove hindsight

Lead with the 256 fresh items.

Show, for the canonical Qwen3.5-9B, Gemma-3-12B, and Llama-3.1-8B comparison:

- time recognition: 97.7–100%;
- shift caused by later evidence: 16.02–28.23 probability points.

This is the first major figure.

The scientific message is:

> **Models can know that evidence belongs to the future and still let it reshape their view of the past.**

A short supporting paragraph can mention that the effect survives removal of the explicit resolution sentence and does not disappear monotonically over the tested Qwen3.5 sizes. Do not turn either into a separate story.

## 4. Known outcomes exert a directional pull

This is the conceptual center of the paper after the headline result.

### 4.1 Outcomes from other events still matter — G8

Give the historical question a resolution packet from a different event.

In the original panel, foreign packets still cause 50.7–100.1% as much absolute movement as the event's own resolution packet. This establishes cross-event influence. Do not make G8 carry the directional claim: only Gemma passes its frozen donor-direction gate, and Llama's later extension has accidental recipient imbalance under this random pairing.

This changes the interpretation of the phenomenon: hindsight is not only the rational integration of highly diagnostic future evidence about the target event.

### 4.2 The pull survives without the visible verdict — G11

Remove the explicit YES/NO verdict sentence from the foreign packet. This is where the paper first makes the cross-event directional claim.

Qwen, Gemma, and Llama retain a directional pull after verdict redaction; Mistral is more dependent on the explicit verdict.

Introduce the term here:

> **Retrospective outcome entrainment:** later context pulls a judgment of the past toward the outcome that context supports.

The term names the discovered regularity. It should not replace the paper's broader question about hindsight.

### 4.3 Changing outcome direction changes the same judgment — G12

For the same recipient history, replace a NO-supporting foreign packet with a YES-supporting foreign packet.

Report the paired shifts directly:

- Qwen +4.41pp;
- Gemma +17.50pp;
- Llama +18.03pp.

The important result is the directional causal relationship across the canonical comparison. Report Mistral's +1.55pp practical-null result in the same complete table or appendix and state that the original Qwen/Gemma/Mistral panel gate remains indeterminate. The prospective Llama replication does not rewrite that historical verdict.

## 5. How outcome information enters the decision

Move from behavior to mechanism with one question:

> **When does the outcome of the later evidence become part of the recipient decision?**

Compare two algorithms:

1. **packet-local transport** — a shared outcome code is formed while reading the later packet and carried to the answer;
2. **contextual decision construction** — outcome information becomes a causal variable only after it is integrated with the recipient question.

### 5.1 Packet states — G13

Outcome is decodable from packet states, but exchanging the tested one-dimensional packet code does not transfer the behavioral pull.

### 5.2 Answer state — G14/G15

G14 discovers the late answer-site pattern. G15 tests the recipient-conditioned version prospectively on a fresh donor assignment.

Fresh G15 result:

- behavioral donor contrast: +18.84pp [12.94, 24.97];
- late answer-position causal transfer: +6.52 to +9.04pp at layers 29–47;
- bidirectional transfer;
- matched orthogonal direction near zero.

The section conclusion:

> **In Gemma, known outcomes become causally expressed after they are integrated with the current question, in a late decision state.**

This closes the paper's current explanatory descent. The paper does not need another mechanism branch merely to look more comprehensive.

## 6. Related work

Organize conceptually, not defensively:

1. **Hindsight, outcome bias, and curse of knowledge** — the broader cognitive problem.
2. **Ex-ante and temporal reasoning in LLMs** — models reasoning about earlier states despite later knowledge.
3. **Contextual distraction and outcome-shaped influence** — adjacent work on irrelevant or conflicting context.
4. **Mechanistic explanations of contextualization and decision competition** — the methodological/intellectual neighborhood of the G13–G15 analysis.

The positioning sentence should be positive:

> Prior work establishes temporal leakage and contextual distraction; we study hindsight directly by controlling known outcomes and show that their influence has a directional, causally traceable structure.

## 7. Discussion and limitations

Discuss what the results mean for retrospective reasoning, evaluation, forecasting analysis, and historical decision audit.

Keep limitations compact:

- the main natural substrate is forecasting;
- effect magnitude varies substantially across models;
- the mechanistic result is established in Gemma;
- the task measures how known outcomes influence model judgments, not whether the model recovers a uniquely correct historical probability.

The failed experiments and exact preregistration gates are scientific provenance and belong in the appendix / `EXPERIMENTS.md`, not as a second main narrative.

## Figures

### Figure 1 — The hindsight problem

A single historical event shown at two times: what was known then versus what is known after resolution. Show that the model correctly labels the resolution as “later” but its earlier probability still moves.

### Figure 2 — Outcome pull across events

Own outcome evidence → unrelated outcome evidence → verdict-redacted unrelated evidence → paired NO-supporting vs YES-supporting replacement. The visual should make the directional pull obvious without requiring experiment codes.

### Figure 3 — Where the pull becomes causal

Packet position: outcome decodable, little causal transfer.

Answer position: late causal transfer after recipient integration, with orthogonal control shown compactly.

## Appendix organization

- exact experimental registry and original preregistrations;
- model-selection chronology: Qwen/Gemma/Mistral were the original frozen panel; Llama was preselected in G4 and added prospectively to the explanatory descent;
- full four-model tables, including Mistral's weak verdict-dependent result;
- Llama qualification details: G4 failed the stronger licensed-frame probe, and G8 failed its recipient-balance validity gate despite positive donor pull; G11 and G12 passed;
- sampling / freeze / data-quality details;
- supporting scale and model-breadth characterization;
- G3 exclusion-reason results;
- G14 discovery chronology;
- failed or indeterminate rounds (G5/G6/G7/G9/G10);
- earlier *Unring the Bell* / broad Information-Set Reasoning history where relevant.
