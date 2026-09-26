# G28B: Matched irrelevant-read control after G28A preliminary results

Registered 2026-09-27 **after observing G28A preliminary outputs from Mistral-Small-24B, Qwen3-8B, and substitute Llama-3.1-8B**, before generating any G28B output. Entirely exploratory; G28A's 200 ConfB items and model panel are reused. This is a focused missing-control follow-up, not fresh confirmation. Frozen G28A RR outputs are immutable input to the comparison.

## Question

G28A's planned `RJ−IJ` contrast mixes earlier relevant content with a prior generated answer/rationale. Its `RR` condition contains relevant E1 but has no generated judgment; however `RR−IJ` still mixes content relevance and answer history. Does *revoked relevant content itself* change the final use of contradictory E2, when the prior turn contains no judgment in either history?

## New condition and contrast

`IR` matches G28A `RR` exactly except that its first user turn shows the **frozen irrelevant control sentence** in place of relevant E1. In both conditions the first user message says to read, the assistant turn is the same literal `Understood.`, the last user message is exactly the same retraction text and E2, and the same claim/final E2 are used. Thus final admissible information is `{C,E2}`. Run all 200 claim pairs and both E2 polarities without selection, on Mistral-Small-24B, Qwen3-8B, Gemma-3-12B, and the disclosed unplanned Llama-3.1-8B substitute (Qwen3.5-9B cannot load on the available compatible stack). Four hundred new final outputs/model; previous 400 RR outputs/model are reused, not regenerated.

Primary paired diagnostic: `T_read_matched = sign(revoked relevant E1) × (Y_RR−Y_IR)`, pooled and by E2 polarity, with claim-cluster bootstrap and per-model results. Positive = carryover toward revoked evidence; negative = movement toward contradictory E2 beyond the irrelevant-read control. Also report `|Y_RR−Y_IR|`, E2 support/refute separation, 50-threshold flips, row/parse/digit-mass/cap checks. No filtering by initial leverage or G28A outcome. The post hoc material-audit 142-pair stratum is sensitivity only.

Interpretation: `T_read_matched≈0` weakens a content-specific interpretation of G28A's negative `RJ−IJ`; a negative value supports content-driven contrastive overcorrection after revocation, even without a committed prior answer. But it does **not** isolate revocation from ordinary contradictory-evidence weighting or general recency. [Competing Biases underlie Overconfidence and Underconfidence in LLMs](https://doi.org/10.1038/s42256-026-01217-9) already documents overweighting of opposing advice. This experiment characterizes this natural evidence setting and decides where the research should go, not a novelty claim by itself.
