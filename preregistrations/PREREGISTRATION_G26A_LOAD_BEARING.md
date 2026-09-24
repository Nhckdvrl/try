# G26A preregistration — load-bearing emergence: must the target evidence already be decision-effective through composition when the exclusion policy binds? (RQ3)

**DRAFT v2 — NOT FROZEN. NOT TAGGED. NO COMPUTE AUTHORIZED.**
Born 2026-09-24 (v1); **full rewrite to v2 the same day**, ordered by the
user design audit, executed after the HoVer structural audit **PASSED**
(`HOVER_STRUCTURAL_AUDIT_2026-09-24.md`). v1 was banner'd
`DO-NOT-FREEZE` with five mandatory items; all five are now built into this
text (§1 construct, §2 audit findings, §3 padding, §0-O5/§7 ROPE power
requirement, §11 two-phase authority). **This document does not authorize
itself**: no harness until §0 is signed, no design tag until §12A is
complete, no compute until an explicit STATUS flip in the ledger — and
Phase A / Phase B require **two separate flips** (§11).

**Proposed experiment id:** `G26A` / `g26` (name only; the G-series has no
other claim past G24B/G25A).

**v1 banner → v2 resolution map (2026-09-24):**

1. construct `decision relevance established` → **load-bearing emergence /
   compositional activation** — §1;
2. HoVer zero-model structural audit FIRST → **DONE, PASS** — §2;
3. padding = identical filler multiset across the three timings — §3;
4. ROPE δ=1.5 power note mandatory before freeze — §0 O5 + §7;
5. two-phase authority (selector funnel ≥ 200 or hard stop) — §11.

Parent documents:

- `PAPER_RQ3_CANDIDATE_AUDIT_2026-09-24.md` — six-candidate screen; this is
  the SURVIVOR's design (§2 there; its RQ wording superseded by this §1);
- `HOVER_STRUCTURAL_AUDIT_2026-09-24.md` + `src/audit_hover.py` +
  `results/audits/hover_structural_v1.json` — the data audit of record (§2);
- `PREREGISTRATION_G24A_NATURAL_EVIDENCE.md` — selection-blindness and
  panel discipline this design inherits;
- register claim boundary: exclusion is **inference-time causal-eligibility
  control, never self-labelled "in-context unlearning"**.

---

## 0. Open items to sign off before the Phase A tag

| # | Item | Proposal (defaults, until overruled) |
|---|---|---|
| O1 | Selector | `mistral-small-24b` computes the gate cells (selection phase), excluded from the pooled four — G24A discipline (no self-conditioning). |
| O2 | Panel | `qwen3-8b`, `gemma3-12b`, `llama31-8b`, `qwen35-9b` (same pooled-4 as G25A). |
| O3 | Main-pass cells | **11** per item: `Y0, YA, YB, YAB` (no-rule, all four, so the single-component gates are re-verifiable **on the panel itself**, not only on the selector) + `EXCL × {T0,T1,T2}` + `ADMIT × {T0,T1,T2}`. |
| O4 | Final n | all gate-passing items in frozen order, **capped at 300**; **split = train, pinned** (§2: 3,642 survivors / 2,320 clusters — 18× the S1 floor *before any gate*); sufficiency gate S1: ≥ 200 final items. |
| O5 | Equivalence ROPE — **power note mandatory before freeze** | δ = 1.5 raw rating points for "≈ 0 / no gain" claims (branch labels need one primary *equivalent* within ±δ, not merely CI-straddling 0). An unpowered 1.5 is an arbitrary threshold (v1 banner item 4): the O5 note (zero-model, G25A-O7 pattern) must establish a declarable-equivalence half-width at the design n — method + standing algebra in §7. |
| O6 | Panel usability floor | per model: `s·(Y_AB − Y_0) ≥ 5` raw points (chain effect measurable on that model), else unusable for that model only, reported `n/n_total`. |
| O7 | Distance window | rule→judgment token distance equal across T0/T1/T2 **within ±10 tokens**, realized by **repositioning one shared filler multiset** (§3); asserted by test. |
| O8 | Cluster key | HoVer decomposition **title path** (page pair) for the bootstrap. |
| O9 | Seed / Phase A size | seed `20260924`; Phase A pool pinned at **N_A = 3,642** train-split structural survivors (audit `T6_post_rule_funnel.by_split.train`). |

## 1. Scientific question (construct: load-bearing emergence)

> **RQ3: Does prospective exclusion require the target evidence merely to be
> present, or must it already be load-bearing through composition when the
> policy is processed?**

Two-hop chain `A + B ⇒ claim` where neither component alone suffices — and
"alone insufficient" is not an assumption but the **selection gates'
observable** (§5: `s·(Y_AB − Y_0) ≥ 15` while `|Y_A − Y_0| ≤ 5` and
`|Y_B − Y_0| ≤ 5`). The final context is identical across timings; only the
state of A when `RULE(A)` is processed differs — absent / present but not
load-bearing / already load-bearing:

```text
T0: RULE → A → B → judgment      # A not yet present when the policy is processed
T1: A → RULE → B → judgment      # A present; A alone cannot move the decision (gates 2–3)
T2: A → B → RULE → judgment      # A already load-bearing through the A∘B composition
```

Rule→judgment token distance is equalised within ±10 (O7) by repositioning
**one shared filler multiset** across the three timings (§3) — no
timing-unique pad block.

Why the wording is *load-bearing* and not *relevance* (v1 banner item 1):
the gates show `A alone is not behaviorally effective` — **not** that the
model fails to recognise A's topical relevance (the claim is visible from
the start, so topical relevance may be recognised while A still cannot move
the verdict). Claims therefore speak about exactly what the observables
show — compositional activation — and the headline contrast **T1 vs T2
holds both sides' evidence present**, defeating the one-liner "present is
obviously easier" (only the composition state differs there).

| Account | Predicts |
|---|---|
| **presence-bound** | `T1 ≈ T2 ≫ T0` — mere presence of A suffices for the policy to bind |
| **load-bearing-bound** | `T2 ≫ T1 ≈ T0` — A must already be decision-effective through composition → **the non-obvious headline** |
| **staged** | `T2 > T1 > T0` — binding builds progressively |
| **timing-insensitive** | all equal — under multi-hop composition the timing structure disappears |

**No account is entailed by the manipulation** (triviality gates 1–4
preflight, §10): the manipulation moves *when the rule is processed relative
to composition emergence*; which state the model actually needs is written
nowhere in the visible content. The headline lives in **T1 vs T2** — the one
contrast no "obvious" story settles.

## 2. Data — HoVer v1.1, structural audit PASSED (2026-09-24)

- **Source pin:** HoVer release v1.1 (Findings EMNLP 2020,
  `2020.findings-emnlp.309`): train/dev/test claims JSONs +
  `wiki_wo_links.db` (2,156,273,664 B, frozen 2020-11-03); sha256s in
  `data/external/source_manifest.json` entry `hover_v1.1`; **CC BY-SA 4.0**.
  **Test split blind** — never read; the audit used train + dev only.
- **Record:** `src/audit_hover.py` →
  `results/audits/hover_structural_v1.json`; report
  `HOVER_STRUCTURAL_AUDIT_2026-09-24.md` (verdict **PASS**; MuSiQue
  fallback **not triggered and not armed**).
- **Funnel:** 6,912 two-hop candidates → 6,832 materialized → 4,270
  orientation-unique → **4,105 survivors / 2,683 title-pair clusters
  (2,710 hpqa)** = 13.4× the S1 floor of 200.
- **Page coverage:** 9,189/9,189 claims resolve after the raw→NFD→NFC
  lookup chain (the 249 initial misses were diacritic normalisation
  mismatches; true missing pages = 0).
- **Sentence reconstruction `smart_sents` v2** (abbreviation-aware; never
  splits at single-letter initials) validated by gold-vs-rotated controls —
  gold sentences recalled 0.536 / bridge 0.609 vs rotated 0.283 / 0.166
  (S-label), 0.488 / 0.728 vs 0.264 / 0.203 (NS) — a 3.6–3.7× separation —
  and beats v1-naive on both metrics, both labels (record-of-truth note in
  the JSON).
- **Structural exclusions:** 80 out-of-bridge (1.16%); 77 with
  single-sentence leak recall ≥ 0.9 (36 at 1.0); selector constants
  `R2: 8..80 words`, `R3: leak < 0.9`.
- **Orientation:** chain order follows supporting-fact **mention direction**
  `sf0→sf1` (61.4% of oriented items); list order equals chain order in
  98.2% of oriented items but **75 survivors are reversed → A/B orientation
  is assigned by mention direction, never by list order** (test-asserted,
  §9.3).
- **Defect taxonomy** (one-by-one read of a 20-item deterministic sample:
  0 fragments / 0 misalignments in survivors): Class A splitter drift
  (fixed by `smart_sents` v2, e.g. uid `71006039`); Class B DB page shorter
  than annotation time (no bridge → drops out); Class C claim/gold noise —
  uid `961688da` (claim labelled SUPPORTED contradicts its own gold
  sentence): **recorded as gold noise, excluded from the candidate pool by
  the gates, original data never modified, human judgment never substituted
  for gold** (user ruling).
- **Split pin (O4/O9): TRAIN ONLY** — 3,642 survivors / 2,320 title-pair
  clusters / 2,339 hpqa clusters (dev 463 / 368 / 371 stays untouched as a
  potential future replication pool). Drawing within one split makes
  cross-split cluster overlap structurally impossible; clustering keys are
  hpqa_id / title-pair (O8).
- The selection phase **never contains an exclusion rule of any kind** (user
  design constraint, enforced in code + test).

## 3. Items and conditions

**No-rule cells (selection + panel):**

```text
Y0   BACKGROUND → judgment
YA   BACKGROUND → A → judgment
YB   BACKGROUND → B → judgment
YAB  BACKGROUND → A → B → judgment
```

**Rule cells (panel only), rule = one of two byte-fixed sentences:**

```text
EXCL(A):  "…Evidence A must not influence your final judgment."   (G24A exclusion lineage)
ADMIT:    control rule, use-normally wording                      (G24A admission lineage)
```

```text
EXCL_t / ADMIT_t  for t ∈ {T0, T1, T2}:   content byte-identical to §1;
the rule sentence is the only content variable in position; the three
timings share ONE filler multiset — only filler positions move, so
rule→judgment distance lands within ±10 tokens (O7). No timing-unique PAD
block exists (v1's trailing-PAD T2 layout is retired).
```

- Rule sentences are **character-identical across timings** (position is the
  only variable; construction constant + byte test).
- Filler: fixed hand-authored neutral bank, unrelated to claim or pages,
  never LLM-generated; the **multiset (token inventory) is identical across
  T0/T1/T2 — only its placement differs** (tests: multiset equality + ±10
  distance assertion).
- **A/B assignment follows mention direction** (`sf0→sf1`, §2) — never the
  supporting-facts list order (test-asserted).
- Same question, output spec, answer format, 0–100 readout across all cells
  (test), per G0/G24A conventions.

## 4. Models (O2)

Pooled primary: `qwen3-8b`, `gemma3-12b`, `llama31-8b`, `qwen35-9b`.
Selector (O1) runs Phase A only; excluded from pooled inference; reported as
reference. No other model, site, layer, carrier.

## 5. Selection rule (no-rule cells only — blind by construction)

Gates, evaluated on the **selector's** `Y0, YA, YB, YAB` in Phase A (§11):

1. **chain works:** `s · (Y_AB − Y_0) ≥ 15`;
2. **A alone insufficient:** `|Y_A − Y_0| ≤ 5`;
3. **B alone insufficient:** `|Y_B − Y_0| ≤ 5`.

(`s` = gold-label direction, G0 mapping: TRUE-claim establishing → +1,
refuting → −1; recorded per item at build; analyzer tested both directions.)

- Gates 2–3 kill the classic *"your two-hop is really one-hop"* shortcut at
  selection, before any exclusion output exists — and they are precisely
  what makes "present, not load-bearing" (T1) an **observable** label (§1).
- Eligible items taken in **frozen HoVer train order**, no quotas (single
  corpus, label balance reported descriptively), cap O4 = 300.
- Selector blindness: Phase A provably contains no `EXCL`/`ADMIT` cell
  (kind check + test). No outcome of the experiment exists at selection
  time.
- Panel usability (O6) applied **per model** on the panel's own cells (main
  pass), reported `n/n_total`, never used to drop items post hoc.

## 6. Estimands

Per item × model, raw sign-aligned rating points (house primary metric):

```text
R_t = s · ( Y_EXCL_t − Y_B )      leakage of A at timing t
      (ideal exclusion = 0: B stays admissible, so Y_B is the counterfactual — not base)

PG  = R_T0 − R_T1                 PresenceGain:  presence of A at binding
LG  = R_T1 − R_T2                 LoadGain:      load-bearing emergence at binding
```

(`PG`/`LG` rename v1's `CG`/`RG` to match the §1 construct.) `R_t > 0` =
excluded A still pulls toward gold; `R_t < 0` = over-suppression relative to
the B-only counterfactual (reported, not clipped).

**Admit-timing control:** `M_t = s · ( Y_ADMIT_t − Y_AB )` — with the chain
fully admissible, timing per se should not move judgments (`M_t ≈ 0`). A
timing slope in `M` means generic rule-position/recency structure →
integrity flag I3 (§8) plus pre-registered sensitivity
`R̃_t = R_t − M_t` (difference-in-differences), reported alongside
regardless. Usability (O6): all 11 cells present for that model and
`s·(Y_AB − Y_0) ≥ 5`.

## 7. Frozen inference

- **Cluster bootstrap** over title paths (O8): resample K clusters with
  replacement, all their rows (items × models) move together; `B = 10,000`,
  percentile 95% CIs, two-sided `boot_p`, `seed = 20260924`.
- **Branch decision procedure (union logic, not intersection–union):** a
  primary is *positive* iff CI low > 0; *equivalent* iff CI ⊆ [−δ, +δ]
  (O5 = 1.5); otherwise *undetermined*. Branch table §8 evaluated in order
  integrity → sufficiency → branches. Claims never exceed the branch that
  actually fired; "≈" in any published sentence maps to the ROPE, not to
  "p > .05".
- Strata reported: pooled-4, per model, label direction (establish/refute),
  per timing. No item removed after results exist; reruns only for
  mechanical incompleteness.
- **ROPE δ=1.5 power note — MANDATORY before the Phase A tag (O5; v1 banner
  item 4).** Zero-model, G25A-O7 pattern (script → JSON → prose recorded
  here). **Standing algebra the note must resolve:** equivalence is only
  *declarable* when the CI half-width < δ, i.e. `1.96 · SE < 1.5`. Taking
  the frozen G23A Δ_zero constant (half-width 4.47 at 68 clusters — a
  four-cell contrast) as a conservative upper bound gives `C > 604` clusters
  to declare equivalence — **impossible at cap 300**. But `PG`/`LG` are
  two-cell contrasts with strictly smaller variance, so the binding
  constants must come from a **two-cell frozen CI** (G23A Gap CIs / G24A
  cell-level CIs on natural materials). The note must state (a) the
  declarable half-width at n ≤ 300 / C ≤ 300 under the two-cell constants,
  (b) the verdict on δ=1.5 vs the noise floor, (c) if δ or n must move:
  **user decision before the Phase A tag — never after outcomes exist.**

## 8. Outcome map

Order: **I-gates → S-gates → branches.**

- **I1** rule sentences byte-identical across timings; **I2** shared-filler
  multiset equality + distance assertion (±10 tokens); **I3**
  admit-timing control: `M_T0 − M_T2` CI contains 0 (else `order-artifact`);
- **I4** RuleAcc ≥ 0.8 on the rule probes (both rule types);
- **S1** ≥ O4-min items (200) after panel usability (O6).

| Verdict | Conditions | Meaning / required action |
|---|---|---|
| `presence-bound` | I✓ S✓; **PG positive**; **LG equivalent** | presence suffices for binding; composition state irrelevant → RQ3 answer = presence |
| `load-bearing-bound` | I✓ S✓; **LG positive**; **PG equivalent** | content present is not enough — A must already be decision-effective through composition → **the non-obvious headline** |
| `staged` | I✓ S✓; PG > 0 **and** LG > 0 | binding builds in stages; both layers matter |
| `timing-insensitive / flat-leaky` | I✓ S✓; PG, LG both equivalent **and** pooled `R` > 0 | composition erases the timing structure while leakage persists |
| `exclusion-robust` | I✓ S✓; PG, LG equivalent **and** all `R_t` equivalent to 0 | chains are excluded cleanly at every timing — sharp contrast with single-hop G24A leak; equally publishable, honestly unexpected |
| `non-monotone` | any primary negative | report as measured; no ordering claim |
| `order-artifact` | I3 (or I2) fails | recency/position structure — no claim until explained via `R̃` |
| `unresolved` | S1 fails, or a needed label is neither positive nor equivalent | report everything; no verdict |

Every row is reachable a priori; none is the manipulation's built-in answer
(gates 3–4, §10).

## 9. Controls and integrity checks

1. Rule identity across timings (byte test) — position is the only content
   variable.
2. **Shared filler multiset** across T0/T1/T2 (multiset-equality test) +
   distance assertion ±10 tokens (O7); hand-authored bank only, no LLM
   generation.
3. **Mention-direction orientation** test: A/B follow `sf0→sf1`; the 75
   list-order-reversed survivors must construct A/B by mention direction,
   never list order.
4. **Single-split assertion:** every selected item is from `train`
   (O4/O9) — a cross-split draw is structurally impossible.
5. Admit-timing control (I3) + DiD sensitivity `R̃` reported
   unconditionally.
6. Selection blindness: no rule cell in Phase A (kind check + test); gates
   computable only from `Y0/YA/YB/YAB`.
7. Single-component gates re-verified on the panel's own no-rule cells (O3)
   and reported — the shortcut objection is answerable with panel data.
8. Sign convention tested both directions (establish/refute labels).
9. Same readout/output spec across all 11 cells (test).
10. Cluster integrity in the bootstrap (test).
11. Disjointness from G0/G24A item ids (trivially true — different corpora —
    asserted anyway; dedup recorded).
12. **No scope creep:** no new site/layer/carrier/model; no LLM-generated
    materials; MuSiQue path not armed (structural audit PASS).
13. **Wording:** inference-time causal-eligibility control; never "in-context
    unlearning", never generic "representation-vs-deployment" (ACL 2026 Main
    owns that frame).

## 10. Relation to nearest prior (triviality gates)

Five-gate preflight for this design:

1. **Treatment ≠ answer:** the manipulation is *when the rule is processed
   relative to composition emergence*; no text states which state binding
   needs. **PASS.**
2. **Reviewer one-liners blocked:** "rule recency" → distance equalisation +
   shared filler multiset + admit-timing control + DiD (I3/§6); "present
   must obviously suffice" → that is only the presence-bound branch,
   coequal with load-bearing-bound, staged, and flat — none derivable from
   the prompt. **PASS.**
3. **Two+ live accounts under identical visible content:** presence-bound vs
   load-bearing-bound (+ staged/flat), same final context, four live
   branches. **PASS.**
4. **Unexpected-result requirement:** `exclusion-robust`, `flat-leaky`,
   `non-monotone` and both orders of PG/LG are all publishable surprises.
   **PASS.**
5. **Nearest prior:** verified by direct fetch —
   `2024.acl-long.550` (latent composition *capability*),
   `2026.acl-long.1937` (multi-hop failure = locate vs integrate),
   `2026.findings-acl.57` (later clarification reinterprets an
   already-processed word). **None asks whether a policy stated before its
   target is load-bearing through composition can bind it for a later
   judgment.** KILLed neighbours (hop depth, post-training origin,
   scope/collateral, inferential closure) catalogued in
   `PAPER_RQ3_CANDIDATE_AUDIT_2026-09-24.md` §1/§6.
   **Freeze-time manual pass for RQ3 phrasings COMPLETED 2026-09-24:**
   arXiv 5 query families — `evidence exclusion`/`exclude evidence` (3),
   `exclusion policy`+LLM (1), `load-bearing`+evidence (33),
   `(multi-hop|two-hop)`+exclusion (23), `instructed`+evidence+
   (`ignore`|`exclude`) (32) = **92 hits, all read individually — zero
   owners** (nearest classes: instructed-ignoring of presentation cues in
   LLM-as-judge debiasing; agent context-eviction = system memory
   management; both different objects) — plus the shared ACL-2026
   event-listing screen (6,422 titles / 6,365 abstracts; its T3 patterns
   included `prospective`, `ignore … evidence`, `evidence …
   ordering|timing|sequence`, `instructed weight`; record:
   `gate5_novelty_search.md` §"Freeze-time manual pass", coverage caveats
   recorded there). **PASS — residual closed.**

## 11. Authorization boundary — TWO-PHASE (v1 banner item 5)

**Phase A — selector only:**

- Scope: `Y0, YA, YB, YAB` × **N_A = 3,642** train structural survivors ×
  1 model (O1) = **14,568 rows**. No rule cell of any kind (blind by
  construction).
- After the run: **freeze the output file (sha256 recorded)**, compute the
  §5 gates, record the funnel (n passing 0/1/2/3 gates).
- **≥ 200 gate-passing →** take items in frozen order, cap 300 (O4),
  record selected item IDs + sha256 in §12B → then request **STATUS flip
  #2**.
- **< 200 gate-passing → HARD STOP.** No threshold loosening, no dev-split
  switch, no MuSiQue rescue, no new corpus. Escalate to the user as a
  project-level decision; any change requires a prereg amendment **before**
  any further compute.
- **STATUS flip #1** authorizes exactly Phase A (≤ 14,568 rows) — nothing
  else.

**Phase B — the actual RQ3 experiment:** ≤ 300 selected × 11 cells ×
4 models = 13,200 rows + rule probes ≤ 300 × 4 × 2 = 2,400 →
**≤ 15,600 rows**. Requires **STATUS flip #2**, recorded only after §12B's
Phase-A output boxes are filled.

**Two separate STATUS flips; one flip never authorizes both.**
Sequence: user signs §0 (incl. the v2 wording and the O5 plan) →
implementation + tests → §12A complete → **Phase A design tag** → flip #1 →
Phase A run → funnel + selection recorded → flip #2 → Phase B run → frozen
analyzer, one-shot verdict.

No retries-by-outcome; no fifth model; budgets stated up front — the flip
authorizes exactly them.

## 12. Freeze checklists (two-phase; design immutable from each tag)

**§12A — Phase A tag:**

- [ ] §0 open items O1–O9 signed off (incl. user sign-off of the v2 wording)
- [ ] **ROPE O5 power note completed (zero-model; §7) and its outcome (δ, n) pinned**
- [x] HoVer structural audit recorded — sha256 / license / funnel / by-split (done 2026-09-24: `hover_v1.1` manifest, `hover_structural_v1.json`, report §5)
- [ ] tests green: rule identity, shared-multiset + ±10 distance, mention-direction orientation, single-split assertion, selection blindness, both sign directions, ROPE trichotomy, outcome-map firing order
- [ ] full test suite green at updated baseline (334 passed / 849 s, five standard `--ignore` flags)
- [ ] **Phase A design tag assigned:** ____________ (recorded here + ledger)
- [ ] **STATUS flip #1 recorded** (ledger: authorizes Phase A ≤ 14,568 rows)

**§12B — Phase A outputs → Phase B authorization (recording only; no design edits):**

- [ ] Phase A output frozen: sha256 + gate funnel (0/1/2/3-gate counts) recorded
- [ ] **funnel ≥ 200 confirmed** (else §11 hard stop)
- [ ] selected item IDs + sha256 (n ≤ 300) recorded
- [ ] **STATUS flip #2 recorded** (ledger: authorizes Phase B ≤ 15,600 rows)

The design is immutable from the §12A tag onward (prereg freeze rule);
§12B admits only the recording of Phase-A outputs and flip #2 — never
design changes.
