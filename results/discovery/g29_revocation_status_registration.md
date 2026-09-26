# G29: Does revocation itself change use of later evidence?

Registered before any G29 model inference. Date: 2026-09-27. G28A/B results were already known, so G29 is a **fresh-material discriminating follow-up**, not an independent discovery of the contrast direction. This file is never to be rewritten based on outcomes; deviations go in appendices.

## Question and boundary

G28 found stronger uptake of a later, opposite-polarity E2 after exposure to a revoked relevant E1, but ordinary contradiction exposure could explain it. G29 holds the claim, E1 text, E2 text, turn count, assistant acknowledgment, final admissible information, and response format fixed to compare whether E1 **had been admissible and was revoked** versus **was declared inadmissible from first display**. The model sees both histories as text. This is behavioral revocation status, not evidence of a persistent hidden state.

## Material before model outputs

`scripts/prepare_g29_materials.py` mechanically sampled 160 VitaminC real-revision same-claim support/refute pairs from the pinned source, excluding prior P2, ConfB and pilot pools by case and normalized claim, after text-length/encoding and overlap heuristics. Fixed seed `20261001`; no model scores read. The 160 are in source rank order in `data/items/g29_candidate_pool_v1.jsonl`. MiMo v2.6 Flash via local OpenCode audits **every** item in eight 20-item batches with the support/refute source labels hidden and no access to model outputs. Keep exactly the first **80** seed-rank items satisfying: `pair_valid=true`, `naturalness=natural`, and audited orientation matches the source support/refute roles. If fewer than 80 pass, run all passing items without relaxing the rule; report the count. The audit is LLM-assisted, not human gold. Preserve all rejected candidates and reasons. No output-based replacement.

## Conditions

For each frozen pair run both directions: E2=support, E1=refute; E2=refute, E1=support. E1 and E2 are the actual same-claim revision alternatives. Same model and decoding for all conditions.

- **R (revoked):** first turn presents E1 as currently admissible; second turn explicitly withdraws E1 and presents E2 as the sole admissible evidence.
- **N (never admissible):** first turn displays identical E1 but labels it excluded from the moment shown; second turn reiterates it remains excluded and presents E2 as the sole admissible evidence.
- **A (active conflict):** first turn presents E1 as admissible; second turn retains it and presents E2 as additionally admissible. Reference condition; final admissible set differs intentionally.
- **D (direct):** C and E2 only. Context/turn structure differs intentionally; baseline for final E2 use.

R and N have the same final admissible set `{C,E2}` and exactly the same E1/E2 wording. The status language necessarily differs, so a R−N effect could reflect instruction framing as well as the prior permission history; we will avoid claiming a hidden process mechanism.

## Readouts and analysis frozen before inference

Primary outcome: a directly elicited TRUE/FALSE decision with no rating or rationale in that call. Report paired R−N decision disagreement and, for each E2 direction, the change in choosing the E2-implied decision. Also report a signed contrast `T_binary = sign(E1) × (P_R(TRUE) − P_N(TRUE))`, where sign(E1)=+1 for supporting E1 and −1 for refuting E1. Negative means revocation enhances use of opposite E2, as G28 suggests. With deterministic binary output, pooled signed contrast averages −1/0/+1 observations.

Secondary outcome: separately prompted 0–9 rating, mapped to 0–100 with G28's frozen digit-expectation readout. Define `T_rating = sign(E1) × (Y_R − Y_N)` on the same model×claim×E2 cells. Also report absolute R−N, R/N/A/D E2 separation, and per-model/per-E2 direction results. No filtering by prior model behavior, leverage, rating, or decision. Use paired claim-cluster bootstrap CIs (5,000 resamples) across frozen items; report all model rows and parse/truncation diagnostics. The audit pass set is selected before inference.

## Interpretations

- R≈N for binary and rating: G28's content effect may mainly be exposure to contradictory E1, with no detectable additional revocation-status trace in this task. The central ConfB suppression–restoration gap remains separately established.
- R differs from N, especially on direct decisions across models: revocation history has a measurable behavioral effect beyond exposure to the same contradictory sentence. Its direction may be overcorrection, inertia, or mixed; report it rather than choosing a new story post hoc.
- R−N only on ratings: narrow the added result to confidence elicitation; do not claim decision consequences.
- R−N only for one E2 polarity: report the asymmetry; do not generalize to polarity-invariant law.

This is one task family and one source. A positive result supports a distinctive revocation-status phenomenon, not a universal inverse-update theorem or internal mechanism.

## Execution addendum before G29 model inference

The MiMo v2.6 Flash free service stalled on blind batch 05 for over ten minutes without returning verdicts. The attempted run was stopped, and the same blind per-item rubric was run through local OpenCode's free Longcat 2.5 Preview for batches 05 and 06. MiMo completed batches 01–04 and 07–08. Longcat batch 05 initially left explanatory `issue` fields empty for some valid rows; a separate blind follow-up requested item-specific explanations and correction of any mistaken verdict before freeze. The freeze script requires a nonempty reason for every row. This model substitution is a material-audit execution deviation, not a change in item eligibility or model outcome analysis; no G29 inference had run at the time of this addendum.
