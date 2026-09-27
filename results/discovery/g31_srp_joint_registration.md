# G31: joint suppression–restoration–preservation pilot

**Frozen before any G31 model output.** Date: 2026-09-27. This experiment follows known ConfB, G29/G29B, and G30 outcomes. It is an **exploratory joint-measurement pilot**, not an independent confirmation. Later deviations must be appended rather than rewriting this registration.

## Question

On the **same claim and model**, can an explicit exclusion rule substantially suppress the direct polarity effect of an old note X while (a) failing to restore the judgment based on current valid information and/or (b) changing sensitivity to a still-valid later evidence item E2? The intended comparison is three-dimensional: suppression (S), restoration (R), preservation (P). A shift in final rating alone is not P.

## Material and provenance

Reuse the 80 G29 frozen, source-pinned, item-by-item audited VitaminC same-claim pairs in `data/items/g29_selected_v1.jsonl`. Each has natural source evidence `E2+` and `E2−`; the original G29 audit and all its rejected candidates remain preserved. For this new design, local OpenCode MiMo 2.6 Flash will construct two **distinct, plausible experimental temporary case notes** `X+` and `X−` for every one of the 80 claims. X is constructed stimulus text, **not a historical source quote**; E2 remains the natural VitaminC revision evidence. The OpenCode model must never inspect G29/G31 model outputs while constructing or judging X. A separate blind audit pass must assess every candidate X pair, including relation to the claim, naturalness, grammatical completeness, comparable length/style, and nonidentity with both E2 texts. Preserve every generated candidate, failed item, and reason.

Select the **first 60 in frozen G29 seed order** passing the audit. If fewer than 60 pass, use all passing items; do not relax rules or replace on the basis of model behavior. No previous G29 response will determine selection. Hash selected items before inference. Report exact overlap with G29 and their constructed-X status.

## Conditions on every selected item

Cross both X polarities and both valid E2 polarities. All prompts use the same final judgment question and decoding.

- **D:** direct claim + valid E2 only; two E2 levels.
- **I:** an irrelevant temporary note marked excluded from first display, then valid E2; same irrelevant note for both E2 levels. The note must be independently audited as irrelevant. This is a framing/length reference, not a perfect text match.
- **N:** relevant X+ or X− marked excluded **from its first display**, followed by valid E2; four X×E2 cells. Final admissible set is `{C,E2}`.
- **A:** the identical X+ or X− is initially admitted and remains valid alongside E2; four X×E2 cells. This intentionally changes the final admissible set and serves only as the active-X suppression denominator.

N/I/A each use the same turn count, acknowledgement placement, final E2 sentence, output task, and approximately matched note lengths; admissibility wording differs where needed. D intentionally has shorter context. The primary output is a graded 0–100 truth probability for the claim, with a separately prompted direct TRUE/FALSE decision to test practical relevance. Reuse the established local checkpoints and deterministic decoding where possible. Run at least Qwen3-8B, Gemma-3-12B, and Mistral-Small-24B if the driver-compatible environments load. Retain all frozen items and all parseable outputs.

## Frozen estimands

For each model and item, let `Y_h(x,e)` be the 0–100 judgment under history `h`, old-note polarity `x ∈ {+,−}`, and valid-E2 polarity `e ∈ {+,−}`.

1. **S, direct old-note effect:** `sep_N = mean_e[Y_N(+,e)−Y_N(−,e)]`; compare with `sep_A` defined identically. Report both signed separations, item-wise absolute X effects, and the reduction `1−sep_N/sep_A` only when the pooled active denominator is stable and positive. A near-zero aggregate alone is not sufficient: also report absolute item-wise excluded X effect.
2. **R, paired restoration:** `CRE_N = mean_{x,e}|Y_N(x,e)−Y_D(e)|`. Also report signed N−D, `mean_e|Y_I(e)−Y_D(e)|` for frame cost, and N−I paired absolute differences. Do not attribute all N−D deviation to X semantics.
3. **P, valid-E2 leverage:** `L_N(x)=Y_N(x,+)−Y_N(x,−)`, `L_D=Y_D(+)−Y_D(−)`, `L_I=Y_I(+)−Y_I(−)`. Report signed and absolute `L_N(x)−L_D` and `L_N(x)−L_I`, per model and X polarity. The X polarity × E2 interaction is `L_N(+)−L_N(−)`; it can be zero despite general E2 attenuation. Require positive clean-E2 leverage descriptively but do **not** filter items by it in the primary analysis.

For binary decisions, report same-item N/D and N/I disagreement, X-polarity decision contrast, and the E2-directed choice-rate change. Bootstrap over **claims**, retaining all conditions and models inside each sampled claim, with 5,000 draws and per-model estimates. Keep source and response hashes, parse coverage, and any infrastructure deviations. The conceptual pattern of interest is **large S reduction while R and/or P remain poor on the same material**; heterogeneous/null findings narrow the framework.

## Interpretation limits

This joint pilot reuses an already studied natural-source set and constructs X notes. A positive result is a coherent within-item demonstration, not a new independent natural-source replication. G29 did not cross X and E2 polarities, so G31 adds an identifiable interaction rather than a larger rerun of G29. D's shorter prompt and I's different semantic content prevent clean mechanistic attribution from N−D or N−I alone. No internal-state claim follows from the behavioral factorial.

## Pre-inference material-audit execution addendum

The MiMo blind-audit runs for batches 01, 06, and 07 did not return verdict files after more than seven minutes, while the other five batches completed. Before any G31 model inference, those three batches were assigned to the local free Longcat 2.5 Preview as fallbacks, using the identical role-blind inputs and rubric. This is an audit-service substitution, not a change in eligibility criteria or experiment outcomes. The original attempted sessions and fallback logs are retained.
