# G28A: Equal-final-evidence path test (registered before model output)

Registration date: 2026-09-27. Status: **exploratory follow-up**, using the already evaluated ConfB 200 items. This cannot be called a fresh held-out confirmation. It is a deliberately simple falsification test of the proposed path-dependence abstraction. No selection on any model output, no pilot-dependent item replacements, no scientific stop gate.

Execution addendum, recorded before full-run output: the `fgvd` environment now has PyTorch 2.11 / CUDA 13, while fvcrc10's driver 550 supports an older CUDA stack; the 2-item smoke failed during CUDA initialization before producing any predictions. The pre-existing `verl-clean` environment (PyTorch 2.8+cu128, vLLM 0.11.0, Transformers 4.57.6) passed a 2-item Qwen3-8B smoke with 22/22 parseable rows and no rationale caps. Full runs use `verl-clean` with the **same frozen model snapshots, prompts, 110-token rationale cap, temp-0, and digit expectation**. This is an environment deviation from the prior ConfB runner, not a change in estimands or materials. Its effect on numerical cross-experiment comparability is unknown; G28A's paired contrasts are computed within each run.

Second execution addendum, after attempted model initialization but before any full-run results: planned Qwen3.5-9B cannot load under vLLM 0.11 / Transformers 4.57.6 (`qwen3_5` architecture unrecognized; current vLLM recipe requires at least 0.17), and the local newer `fgvd` stack cannot initialize on driver 550. The failed log is retained. The preplanned-model analysis will therefore report the three runnable planned models separately. To keep a four-model exploratory panel, run the existing ConfB Llama-3.1-8B snapshot on GPU 3 **as an unplanned substitute**, clearly marked as such; do not call the substituted four-model panel preregistered or treat the substitution as a positive outcome.

## Scientific question

For a fixed claim C and final admissible evidence E2, does the model's final judgment depend on whether it earlier saw and judged a now-revoked E1? Is any difference specifically related to E1's support/refute direction, or is it explained by generic extra dialogue and self-anchoring?

This is distinct from ConfB's one-rendered-prompt `C,E1,retract(E1)→Y`: it contains an actual prior assistant response, then a new user turn. The model is still a stateless function of its *textual* conversation history; do not infer a persistent hidden belief state.

## Data and models

All 200 frozen ConfB claim/case pairs, including any later-disputed items; evidence_s and evidence_r are the two alternative Wikipedia-revision sentences. The third ConfB control item supplies an irrelevant natural sentence. No new sampling, no exclusions, no outcome-dependent filtering. The blind independent material re-audit is conducted separately; audit-stratum analyses, if any, are post hoc. Planned four diverse frozen local models: `mistral-small-24b`, `qwen3-8b`, `gemma3-12b`, `qwen35-9b`. Snapshots and vLLM settings match the existing ConfB runner (reasoned mode, 110 rationale tokens, temp 0, digit expectation 0–100); single-GPU per model, four GPUs total.

## Conditions per claim and final evidence polarity

E2 is either the supporting revision (+) or refuting revision (−). Relevant E1 is always the *opposite* revision of the **same claim**. Irrelevant E1 is the control item's decision-unrelated natural sentence. Every pair is run in both E2 directions, fixed before model output.

1. `D` direct: one user turn gives C and E2, asks for the judgment.
2. `RJ` relevant judged history: first user turn gives C and relevant E1 and asks for a judgment; the assistant's actual greedily generated short rationale and digit are appended as a prior turn. Second user turn revokes E1, gives E2, and asks again.
3. `IJ` irrelevant judged history: same as RJ, with irrelevant E1; the same claim and final E2.
4. `RR` relevant read history: first user turn gives C and relevant E1 but requests no judgment; an explicit acknowledgment turn is appended. Second turn uses the **same** retraction+E2 text as RJ and IJ. This distinguishes exposure from an earlier committed score. RR uses a fixed acknowledgment, not a model-generated intermediate judgment, and is diagnostic only.

The first-turn judgment for IJ is shared across both E2 directions; RJ has one initial judgment per relevant E1 direction. Thus each model has 600 initial judged runs and 1,600 final runs, 2,200 output rows in total (initial rows are recorded separately and never treated as final observations). All conditions use the same claim, E2 text, final question, scale, rationale limit, and digit readout within a direction. `D` does not include retraction framing; `RJ−IJ` is the key matched-frame contrast.

## Frozen readout

Primary paired quantity (model×claim×E2): `T = sign(E1) × (Y_RJ − Y_IJ)`, where sign(E1)=+1 for support E1 (E2 refute), −1 for refute E1 (E2 support). `T>0` means revoked relevant content or the earlier answer pulls the final judgment toward E1 compared with a matched irrelevant revoked history. Report pooled mean with a claim-cluster paired bootstrap CI, each model separately, and the two E2 directions separately. No absolute threshold or pass/fail rule.

Secondary: `|Y_RJ−Y_D|`, `|Y_IJ−Y_D|`, and `|Y_RR−Y_D|` per item; separation between final E2 support and E2 refute for each condition; `T_read=sign(E1)×(Y_RR−Y_IJ)`. Initial evidence leverage is reported continuously; no leverage gate. Count opposite-direction final choices using digit score 50 only as a descriptive threshold. Report parse/mass/truncation and exact row completeness for all runs.

## Competing outcomes

- `T≈0`, with RJ and IJ similarly offset from D: generic dialogue/retraction frame or prior-answer effects dominate; no evidence-specific history law here.
- `T>0` in RJ and RR: revoked evidence content exerts a polarity-aligned effect after replacement, beyond prior-answer commitment.
- `T>0` in RJ but `T_read≈0`: previous answer or its rationale is the likelier carrier; relate directly to contextual-inertia prior work, not to a newly discovered evidence-update law.
- `T<0`: corrective overreaction, also path dependence but contrary to simple persistence.
- No RJ/D discrepancy at all: the original CRE is likely specific to terminal retraction without fresh admissible E2; narrow the research story.

## Important prior and claim ceiling

[ReviseQA](https://openreview.net/pdf?id=Z4KBiAYXlI) already tests multi-turn fact/rule removal. [Breaking Contextual Inertia](https://aclanthology.org/2026.findings-acl.313/) compares multi-turn correction to single-turn full-information anchors. Therefore this experiment does **not** by itself establish novelty. It tests whether the earlier suppression–restoration gap extends to *natural, same-claim revoked evidence* with a matched irrelevant history, and whether content direction survives beyond generic inertia. Any mechanism claim requires further evidence.
