# G24B preregistration — donor-state vs recipient-context factorization

**Created:** 2026-09-24, after G24A completed with the frozen verdict
`prospective-only` and while G23C's frozen verdict
`target-conditioned-policy-state` stands.

**Status:** FROZEN DESIGN — committed and tagged
`g24b-donor-recipient-factorization-design-v1` on 2026-09-24, before any G24B
forward pass; §12 records the freeze and the interpretation points settled
before tagging.
**NO G24B TARGET-MODEL OR PATCHING COMPUTE IS AUTHORIZED BY THIS FILE.**
Repository-level authority for any compute lives in `STATUS.md` only.

G24B is the factorization experiment named in
`PAPER_SCALE_AUDIT_2026-09-23.md` §7 (execution-order step 5): it separates
the two explanations that G23C's positive result leaves open.

---

## 1. Scientific question

G23C found that a rule-end hidden state's causal effect on later evidence
suppression is target-conditioned: within-preview policy-value interchanges
transferred more under matched previews than under unrelated previews
(`TargetConditioning` positive at L14).

But G23C's contrast varied the **donor preview and the recipient preview
together**: `PolicyTransfer_M` averages interchanges whose recipients are the
matched cells, and `PolicyTransfer_U` averages interchanges whose recipients
are the unrelated cells. A positive `TargetConditioning` is therefore
consistent with two different explanations:

> **A. donor-side:** the donor rule-end state itself contains more
> target-conditioned policy information when the target proposition was
> available during policy processing.
>
> **B. recipient-side:** the state is generic, and the matched recipient
> context is simply more sensitive to it.

G24B asks:

> **With the recipient prompt held fixed, does the donor rule-end state
> carry a larger causally transportable zero-versus-full policy effect when
> the donor's preview was the matched target rather than an unrelated
> passage?**

Short form:

> **donor-state vs recipient-context factorization**

---

## 2. Why this is the missing link

The audit's standing summary of the confound
(`PAPER_SCALE_AUDIT_2026-09-23.md` §6, RQ3):

> stronger matched than unrelated transfer can reflect both donor-state
> structure and target-dependent sensitivity of the recipient/downstream
> context.

G24B orthogonalizes the two sides: inside every contrast the recipient prompt
is byte-identical across the compared cells, so any difference is carried by
the patched donor state alone. A positive donor-side target-by-policy
interaction with the recipient fixed is much stronger evidence that target
availability changes what policy information is present in the rule-time
state, rather than merely changing downstream susceptibility.

---

## 3. Existing 2×2 substrate

Reuse the exact Stage-5 matched chronology, the same two models for which the
direct readout reproduces the behavioral contrast, and the same frozen items:

- Qwen3-8B;
- Mistral-Small-24B;
- `legal_judgment` (45 items) + `evidence_inference` (30 items) = **75**
  frozen Stage-5 items, 40 increase / 35 decrease.

The four cells are the Stage-5 ME / MA / UE / UA cells (G23C §3 renaming):

```text
ME     = M0     matched   preview -> weight 0%    rule -> evidence -> answer
MA     = M100   matched   preview -> weight 100%  rule -> evidence -> answer
UE     = U0     unrelated preview -> weight 0%    rule -> evidence -> answer
UA     = U100   unrelated preview -> weight 100%  rule -> evidence -> answer
```

No new behavioral dataset is created. No item is added, removed, or
preselected (§4, §7).

---

## 4. Baseline bridge, before patching

The §4 bridge of G23C applies unchanged, recomputed from G24B's own four
baseline readouts:

```text
PolicyEffect_M = s · [Y(MA) - Y(ME)]
PolicyEffect_U = s · [Y(UA) - Y(UE)]
TargetPolicyInteraction = PolicyEffect_M - PolicyEffect_U
```

Frozen bridge gates (identical to G23C §4):

1. pooled `PolicyEffect_M >= 5.0` and its 95% CI lower bound > 0;
2. pooled `TargetPolicyInteraction >= 5.0` and its 95% CI lower bound > 0;
3. both quantities have positive model means in 2/2 models.

If the bridge fails, stop before any donor-recipient patching.

Because the bridge inputs are the same deterministic cells that produced the
frozen G23C bridge, the G24B bridge CLI cross-checks its boolean gate triple
against `results/mech/g23c_bridge_analysis.json` and aborts on any mismatch
(§12); a mismatch means the frozen baseline is no longer reproducible.

---

## 5. Intervention

Patch only the single rule-summary position G23C patched: the final token of
the rule block (`rule_end`).

Primary layer: **layer 14 in both models** (fixed from the completed Stage-5
localization; Qwen3-8B strong at L14–18, Mistral-Small-24B at L12–16).

Negative layer controls: **layer 4** and **layer 24** (or the nearest valid
layer if a model has fewer than 25 layers).

No layer search and no site search are performed in G24B.

---

## 6. The donor × recipient grid and estimands

### Recipients (frozen)

The recipient prompt is held fixed inside every contrast, at **both
policy-0 cells**:

```text
R ∈ { ME, UE }        (matched-zero recipient, unrelated-zero recipient)
```

Rationale, settled in §12: the RQ3 object is the executable **zero-use**
policy, so the recipient policy value is frozen at `weight 0%`; the audit's
minimal design ("keep one recipient prompt fixed ... repeat for matched and
unrelated recipients") fixes the repeat axis as the two preview contexts;
and the policy-0 recipients make G23C's passing `*_100to0` directions a
subset of this grid for direct comparability.

### Grid (8 patches)

Every cell is a donor; only `ME` and `UE` are recipients:

```text
ME -> ME     MA -> ME     UE -> ME     UA -> ME
ME -> UE     MA -> UE     UE -> UE     UA -> UE
```

`ME -> ME` and `UE -> UE` are identity patches and serve simultaneously as
grid cells and as §9.1 checks.

### Donor-side estimands (per item, per layer, sign-aligned by `s`)

```text
DonorPolicy_M(R) = s · [Y(MA -> R) - Y(ME -> R)]
DonorPolicy_U(R) = s · [Y(UA -> R) - Y(UE -> R)]

DonorTargetInteraction(R) = DonorPolicy_M(R) - DonorPolicy_U(R)
```

Pooled over the two frozen recipients (per item):

```text
DonorPolicy_M          = mean over R ∈ {ME, UE} of DonorPolicy_M(R)
DonorPolicy_U          = mean over R ∈ {ME, UE} of DonorPolicy_U(R)
DonorTargetInteraction = mean over R ∈ {ME, UE} of DonorTargetInteraction(R)
```

`DonorTargetInteraction` is the primary estimand. The recipient-specific
`DonorTargetInteraction(ME)` and `DonorTargetInteraction(UE)` are reported as
secondary quantities and are never gated.

All four terms of every contrast are grid outputs (the `X -> R` patched
readouts); the bridge (§4) alone uses the unpatched baselines. Positive
`DonorTargetInteraction` means: with the recipient prompt identical, the
matched-preview donor's zero-vs-full policy distinction moves the answer more
than the unrelated-preview donor's — the donor-side reading of G23C.

All quantities are raw sign-aligned rating points. No recovery fractions and
no division by behavioral gaps.

---

## 7. Frozen inference

- cluster bootstrap over independent case skeletons;
- seed `20260924`;
- 10,000 percentile resamples;
- pooled inference keeps model observations from the same skeleton in one
  cluster;
- per-model results reported separately;
- no trimming / winsorisation / post-result item filtering.

Meaningful floor: **3.0 rating points**.

---

## 8. Outcome map

### `donor-conditioned-policy-state`

Requires at primary L14:

1. `DonorTargetInteraction >= 3.0`, CI lower > 0, positive in 2/2 models;
2. the same signed pattern is absent or substantially weaker at the frozen
   negative layers 4 and 24 (operationalized in §12);
3. `DonorPolicy_M` passes (same floor / CI / 2-of-2 rule) — checked before
   the headline in the classifier's literal order.

Licensed claim:

> **With the recipient prompt held fixed, rule-end states from
> matched-target donors carry a larger causally transportable
> zero-versus-full policy effect than rule-end states from unrelated-target
> donors: target availability during policy processing changes what policy
> information the rule-time state itself contains.**

Do not call it a universal function vector or a single reusable direction.

### `donor-generic-policy-state`

`DonorPolicy_M` and `DonorPolicy_U` both pass, but
`DonorTargetInteraction` does not.

Licensed claim:

> **the rule-end state carries causally transportable policy value
> regardless of the donor's target context; the intervention does not show
> that the transported policy information is target-conditioned.**

This supports explanation B: G23C's within-preview contrast is then better
read as recipient-side sensitivity.

### `no-donor-policy-state`

The bridge passes but `DonorPolicy_M` does not.

Licensed claim:

> **the rule-end state is not shown to carry a causally transportable
> policy distinction into a fixed recipient; G23C's within-preview
> interchange alone cannot separate state-side target conditioning from
> matched-recipient sensitivity.**

### `bridge-failed`

The frozen behavioral bridge fails. Stop before donor-recipient patching.

### `unresolved`

Any other pattern.

Classifier order is strictly literal (settled in §12).

---

## 9. Controls

Required implementation checks:

1. **identity patch**: patch a cell's own rule-end state back into itself
   (all four cells, all three frozen layers); output must match its baseline
   within numerical tolerance;
2. exact same recipient prompt, model and readout across all four donors of
   a recipient (only the patched state differs);
3. evidence has not been processed at the patch site;
4. frozen negative layers 4 and 24;
5. report all eight grid cells before any averaging.

No orthogonal-direction, learned-vector, layer-search, site-search, model-add
or carrier-add controls: this primary factorization runs on the exact G23C
substrate or not at all.

---

## 10. Relation to nearest prior

Relative to G23C itself: G23C established that a within-preview
policy-value interchange transfers and that the transfer is larger for
matched than unrelated preview **pairs (donor and recipient varying
together)**. G24B holds the recipient fixed and moves only the donor's
preview context, so it identifies the donor side of that contrast.

Relative to function-vector and steering work: G24B does not search for a
transportable task vector; it factorizes an already-localized, already-causal
rule-time policy state along the donor/recipient axis that the paper's RQ3
requires.

---

## 11. Authorization boundary

Before any G24B model forward pass or activation patch:

1. build the donor × recipient grid by importing G23C's cell construction
   (no re-implementation of the Stage-5 cells);
2. implement the eight grid patches and the four-cell identity check at the
   frozen layers;
3. implement the frozen bridge (with the G23C cross-check) and the §8
   classifier;
4. add tests for sign conventions, identity patch, pooled skeleton
   clustering, fixed layers, the recipient freeze, the grid table and the
   stop rule;
5. commit and tag a dedicated G24B design freeze;
6. explicitly update `STATUS.md`.

Until then:

> **NO G24B COMPUTE.**

---

## 12. Freeze checklist and record

Design-audit points settled before tagging (no G24B output of any kind
exists: no forward pass, no activation capture, no patching):

- **§6 recipient freeze:** recipients are exactly the two policy-0 cells
  `ME`, `UE` (rationale in §6); the grid is exactly the 8 ordered pairs
  donors `{ME,MA,UE,UA}` × recipients `{ME,UE}`. Both `*_to_ME` and
  `*_to_UE` contrasts are computed; the primary pools the two recipients by
  a per-item mean, and the recipient-specific interactions are report-only.
- **§8 condition 2 ("absent or substantially weaker" at the negative
  layers), operationalized exactly as G23C §12:** `PASS(DonorTargetInteraction)`
  is false at that layer, **or** the pooled primary mean at L14 exceeds that
  layer's by ≥ 3.0 (one floor of raw points). Both L4 and L24 must satisfy
  it.
- **§8 classifier order (strictly literal):** `bridge-failed` →
  `no-donor-policy-state` (when `DonorPolicy_M` fails) →
  `donor-conditioned-policy-state` (primary passes and controls ok) →
  `donor-generic-policy-state` (`DonorPolicy_U` passes **and the primary
  does not**) → `unresolved`. A passing primary whose control clause fails
  yields `unresolved`, never `donor-generic-policy-state`.
- **§9.1 identity tolerance:** `IDENTITY_TOL` = 0.5 rating points over all
  4 cells × 3 frozen layers; a violation aborts the analysis with no
  scientific verdict.
- **§4 bridge cross-check:** the bridge CLI compares its boolean gate
  triple (gate1, gate2, gate3, passed) with
  `results/mech/g23c_bridge_analysis.json` and aborts on mismatch; the
  comparison helper is unit-tested, and `phase_bridge` itself stays
  input-parameterized so synthetic fixtures remain testable.
- **§7 skeleton key:** the repository-standard `cluster_of`
  (`src/cluster_robustness.py`): `legal:` + `meta.case` for
  `legal_judgment`, otherwise task family + `base_context[:60]` (latent
  problem). The 75 in-scope items give **15 clusters** (10 legal cases + 5
  latent problems); the pooled bootstrap keeps both models' observations of
  one skeleton in a single cluster.
- **§3 scope:** all **75** frozen items — 45 `legal_judgment` + 30
  `evidence_inference`, 40 increase / 35 decrease — with no limit and no
  behavioral-gap preselection (§4, §7).
- **§5 layers:** `frozen_layers(nL) = (4, 14, min(24, nL-1))`; Qwen3-8B
  (36 layers) and Mistral-Small-24B (40 layers) both resolve to
  **(4, 14, 24)**. The runner exposes no layer flag, and the analyzer
  refuses any input whose design block differs from this configuration.
- **§11.1 construction by import:** the runner imports `build_cells` from
  `src/mech/g23c_policy_state.py` (which itself imports the Stage-5
  builders and re-checks pairwise block identity and `rule_end`-before-
  evidence at runtime) instead of re-implementing any cell, and offers a
  tokenizer-only `--dry-run` audit (no forward pass) over all 75 items × 4
  cells for both models.
- **§4 / §6 / §8 wiring:** runner `src/mech/g24b_donor_state.py
  --phase bridge|patch` writes `results/mech/g24b_{bridge,patch}_{tag}.json`;
  frozen analyzer `src/mech/analyze_g24b.py --phase bridge|full` writes
  `results/mech/g24b_bridge_analysis.json` / `results/mech/g24b_analysis.json`.
  Two-phase execution is mandatory: the §4 gate is read from `--phase
  bridge` before `--phase patch` is ever launched.
- **§7 seed:** `20260924` (this design's freeze date; G23C's runs keep
  `20260923`), 10,000 percentile resamples, floor 3.0, identity tolerance
  0.5.

Freeze checklist (§11):

- [x] §11.1 exact Stage-5 cell reconstruction — by import from the G23C
      runner, plus its runtime pairwise-identity / site-order assertions and
      a tokenizer-only dry run over all 75 items × 4 cells for both models;
- [x] §11.2 the eight grid patches and the four-cell identity check —
      donors `{ME,MA,UE,UA}` × recipients `{ME,UE}` at `rule_end`, layers
      (4, 14, 24), both models (Qwen3-8B, Mistral-Small-24B);
- [x] §11.3 frozen bridge (with the G23C gate cross-check) and the §8
      five-outcome `classify` in its literal decision order;
- [x] §11.4 tests — `tests/test_g24b.py`: sign conventions, identity patch,
      pooled skeleton clustering, fixed layers, the recipient freeze and
      grid table, all three bridge gates, all five verdicts end to end, drop
      accounting, the frozen-design guard, runner wiring and the prereg
      wording lock;
- [x] §11.5 this document, code and tests committed and tagged
      `g24b-donor-recipient-factorization-design-v1` in the design commit,
      before any forward pass;
- [ ] §11.6 `STATUS.md` updated in the commit immediately following the tag
      — only that repository-level authority can permit compute.
