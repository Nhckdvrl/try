# G32: identifying content non-use, clean-context self-prediction and rule shifts

**Design frozen before G32 inference.** Date: 2026-09-28. Read the [nearest-prior matrix](g32_prior_estimand_matrix_v1.md). G32 is a construct-identification *exploration*, not independent confirmation and not a benchmark. Amendments and execution deviations must be appended, never silently incorporated here.

## Mother question

When a model is told to exclude a piece of evidence, does a clean-context restoration error reflect continued use of that evidence, an inability to predict its own clean-context response, or a change in the operative judgment rule? These are distinct *behavioral contrasts*, not claims of distinct internal modules. The simple suppression/restoration gap is already reported by Self-Blinding, so that gap alone cannot be the G32 result.

## Materials and frozen selection

Use 60 claims selected without looking at G32 outcomes from the 80 G31 candidate rows. `scripts/build_g32_items.py` ranks rows by SHA-256 of the fixed seed plus item ID, selects 60, and restores ID order. All 80 claim/E pairs came from the previously source-pinned G29 VitaminC sample, and constructed X pairs were separately role-blind audited before G31. The G32 selection overlaps the 60 G31 studied items in **45/60** rows and includes 15 G31-unused rows; none are wholly new to the project. Source file SHA-256 `8b07fbcfe8a9d24b79c297941e67cec236aeb7eeace5fb12da9689637c34fe00`; selected file SHA-256 `0fcd8f9e964ff4c42d4c01ebd3bdcaacfaeaf7145eb9540452aa1371e4e0d261`. X is an invented experimental note, not a real document. E is naturally sourced but many claims are numeric/threshold-like: 47/60 contain a digit or quantitative comparator; 13/60 do not. This is a sharp identification substrate, not a representative sample of ordinary prose judgments.

An extra G32-specific, outcome-blind material audit checks whether each selected claim is standalone and both E and X polarities support a meaningful record-only contrast. It may flag flaws, but the primary 60 remain frozen; report full and audit-viable sensitivity rather than silently substituting items. Because constructed X can paraphrase E, the two sources are textually distinct but not necessarily statistically independent factual events. The design independently *assigns* E/X polarity; it does not warrant a Bayesian independence assumption.

## Factorial conditions and frozen prompt

Two task contracts: `open_world` permits background knowledge plus admissible record E; `record_only` permits only E. For each, E is its natural support or refute sentence. The *same item* supplies X support/refute notes. Each contract×E has seven identification cells:

| Cell | X slot | Question |
|---|---|---|
| B | no X slot | direct judgment |
| F_D | `[REDACTED]`, excluded from display | direct judgment |
| F_S | identical redacted slot/status | predict fresh same model given only claim+E |
| D+, D− | excluded X support/refute content | direct judgment |
| S+, S− | excluded X support/refute content | predict fresh same model given only claim+E |

Two additional **material-calibration** cells A+, A− render the same X content as *admissible* and use the direct question. These are necessary to distinguish successful non-use from a powerless X. They are not a new primary construct. Total per model: `60 × 2 contracts × 2 E polarities × 9 cells = 2160` judgments. Three checkpoints yield 6480 judgments. Frozen prompt source: `scripts/run_g32_construct_identification.py`; its pre-inference SHA-256 is `20dfa3d7b2b72e531e932eb7fb948c6ffebba432f3f8b2cf9af92c059a2206a8`. Each output stores exact messages and their hashes.

All conditions use the same 0–100 probability readout, temperature zero, and chat-template tokenization. The direct and self-prediction questions share the response format. The prediction explicitly targets the *B prompt's information state*, not the redacted-frame prompt; thus S−B is a performance gap for that specified target, while F_S−F_D is specifically the query change **within** the frame. Neither by itself proves a psychological inability to self-simulate; pragmatic interpretation and calibration may contribute.

## Registered analysis

For item `i`, contract `t`, E polarity `e`, and query `q` (D direct / S self-prediction), let `Y(q,x,e,t)` be the output; let `F_q(e,t)` be redacted-frame output and `B(e,t)` the clean output.

1. **Content-dependent X effect:** within each E and contract, `ΔX_D = D+−D−`, `ΔX_S = S+−S−`, and active positive control `ΔX_A=A+−A−`. Report signed *and mean itemwise absolute* effects, distributions, zero fractions, and conditional patterns where active X has leverage. The polarity contrast removes the common effect of filling the X slot, but a zero signed mean can hide large itemwise effects. Do not choose a post hoc threshold to redefine the primary item set.
2. **X-versus-redaction displacement:** for each X arm, `D±−F_D` and `S±−F_S`; decompose into common center shift `((D++D−)/2)−F_D` and polarity half-contrast `(D+−D−)/2` (similarly S). This pair does *not* uniquely identify semantic leakage: simply showing any note can move an answer. The polarity component is stronger evidence of content dependence.
3. **Question and frame effects:** `Q=F_S−F_D`; `H_D=F_D−B`; `H_S=F_S−B`. Report signed, absolute, claim-paired intervals and model-level heterogeneity. `Q` is a query effect with X text absent; `H_D` is a redacted exclusion-frame effect; `H_S` mixes frame and self-prediction against the specified B target. Also report full `S±−B` and `D±−B`, without calling either “non-use ability” by itself.
4. **Permitted-E use:** for each condition `c`, `P_c=Y_c(E+)−Y_c(E−)`. The first preservation comparator is `P_D±−P_FD` (and `P_S±−P_FS`) because it matches the frame/query; `P_FD−P_B` then measures how the exclusion frame changes E leverage. `P_D≈P_B` is an overall desideratum but not a causal attribution. Report signed and absolute itemwise contrasts; no “everything goes to 50” response counts as success.
5. **Task contract interaction:** compare the same registered contrasts in record-only and open-world. Do not compare raw probability levels as if the contracts had the same semantics. Inspect whether record-only reduces X polarity dependence, self-prediction discrepancy, or query/frame effects while retaining E leverage. Record-only may be easier simply because it makes the rule more explicit; the result alone is not a universal mechanism.

Uncertainty: claim-cluster bootstrap (resample the 60 claims as units, retaining all model/contract/E/cell observations) with 5000 draws; report per-model descriptive estimates before pooling. No directional success threshold or kill threshold is predeclared. Missing parses remain visible; report complete-case and coverage. No item replacement based on behavior.

## Outcome-robust interpretation

- Small direct X effect **with active-X leverage and preserved legal-E leverage**, but large S discrepancy: strongest evidence that a restoration score can misdescribe direct selective control. A model-ranking reversal would be particularly consequential, but is not guaranteed.
- Large direct X effect **with preserved legal-E leverage**: a clean selective-control failure; internal mechanism becomes worth considering only if replicated on better natural material.
- Contract-specific dissociation: identifies a boundary in the *task contract*, not automatically a general cognitive law. Reproduce on a second material family before claiming a broad law.
- Large frame/query shifts with little additional X-content dependence: no evidence for a novel exclusion mechanism on this material. Treat ConfB as a strong but scientifically narrower observation; stop inventing names for the offset.
- Weak active-X leverage, weak clean-E leverage, or pervasive material flaws: the substrate cannot identify the proposed construct regardless of attractive metric values. Repair materials before inferential escalation.

No mechanism or training method is initiated as part of G32. A promising G32 interaction is still exploratory and overlapping with G31; a separate natural, fresh confirmation would be required for a main-paper claim.

## Pre-inference, outcome-blind material amendment

The specified G32-specific audit finished before any G32 model output. MiMo 2.6 Flash judged batches 01 and 03; Longcat 2.5 Preview judged 02 and 04. All 60 rows received one verdict. Four rows (`g29_068`, `g29_080`, `g29_083`, `g29_092`) failed **standalone claim** validity because “The film,” “It,” or “The song” had no resolved referent. The auditors judged E and X polarity contrasts valid in all 60. This was a material defect, not outcome-based pruning. The frozen inferential set is therefore the 56 audit-viable items; the original hashed 60 and all four audit inputs/outputs are preserved. The final item file SHA-256 is `1e4c04f366317564ea6414ccfd2934aadb949c7be0374afae92d6ff8ea5ca1bc`. The actual count is **2016 outputs/model, 6048 outputs across three models**, not the proposed 2160/6480. Of the 56, 44 are numeric/threshold claims and 12 are other prose claims. These free-model audits are not human gold; record-only viability remains an empirical assumption to check with clean E leverage and example-level inspection. No new item was added to replace a failed item.
