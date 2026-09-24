# G26A preregistration — relevance emergence: what must be known when an exclusion policy binds (RQ3)

**DRAFT — NOT FROZEN. NOT TAGGED. NO COMPUTE AUTHORIZED.**
Born 2026-09-24 under `STATUS = paper writing + novelty audit + third-RQ
search only`. **This document does not authorize itself**: no dataset work
beyond the audit noted in §11, no harness, no design tag, no forward pass
until (i) §0 open items are signed off, (ii) §12 is complete with the tag
recorded, (iii) STATUS flips explicitly in the ledger.

**Proposed experiment id:** `G26A` / `g26` (name only; the G-series has no
other claim past G24B/G25A).

Parent documents:

- `PAPER_RQ3_CANDIDATE_AUDIT_2026-09-24.md` — six-candidate screen; this is
  the SURVIVOR's design (§2 there);
- `PREREGISTRATION_G24A_NATURAL_EVIDENCE.md` — selection-blindness and
  panel discipline this design inherits;
- register claim boundary: exclusion is **inference-time causal-eligibility
  control, never self-labelled "in-context unlearning"**.

---

## 0. Open items to sign off before freeze

| # | Item | Proposal (defaults, until overruled) |
|---|---|---|
| O1 | Selector | `mistral-small-24b` computes the gate cells (selection phase), excluded from the pooled four — G24A discipline (no self-conditioning). |
| O2 | Panel | `qwen3-8b`, `gemma3-12b`, `llama31-8b`, `qwen35-9b` (same pooled-4 as G25A). |
| O3 | Main-pass cells | **11** per item: `Y0, YA, YB, YAB` (no-rule, all four, so the single-component gates are re-verifiable **on the panel itself**, not only on the selector) + `EXCL × {T0,T1,T2}` + `ADMIT × {T0,T1,T2}`. |
| O4 | Final n | all gate-passing items in frozen order, **capped at 300** (user target 200–300; actual funnel pinned at freeze after the HoVer data audit); sufficiency gate S1: ≥ 200 final items. |
| O5 | Equivalence ROPE | **δ = 1.5 raw rating points** for "≈ 0 / no gain" claims (branch labels `content-bound`/`relevance-bound` require one primary *equivalent* within ±δ, not merely CI-straddling 0). |
| O6 | Panel usability floor | per model: `s·(Y_AB − Y_0) ≥ 5` raw points (chain effect measurable on that model), else unusable for that model only, reported `n/n_total`. |
| O7 | Distance window | rule→judgment token distance equal across T0/T1/T2 **within ±10 tokens**, padded with a fixed neutral filler bank (hand-authored, never LLM-generated); asserted by test. |
| O8 | Cluster key | HoVer decomposition **title path** (page pair) for the bootstrap. |
| O9 | Seed / cap | seed `20260924`; selection-pass budget N pinned at data audit. |

---

## 1. Scientific question

> **RQ3: Does prospective exclusion require the target content to be
> available, or must its decision relevance already be established when the
> policy is processed?**

Two-hop chain `A + B ⇒ claim` where neither component alone suffices (gates
§5). The **final context is identical** across timings; only the state of the
target when `RULE(A)` is processed differs:

```text
T0: RULE(A) → A      → B → judgment     # content unknown, relevance unknown
T1: A → RULE(A)      → B → judgment     # full content known, relevance not yet established
T2: A → B → RULE(A)  → PAD → judgment   # content known AND relevance established
```

| Account | Predicts |
|---|---|
| **content-bound** | `T1 ≈ T2 ≫ T0` — content existing suffices for binding |
| **relevance-bound** | `T2 ≫ T1 ≈ T0` — the policy needs the target→decision relation already established |
| **staged** | `T2 > T1 > T0` — binding builds progressively |
| **timing-insensitive** | all equal — under multi-hop composition the timing structure disappears |

**No account is entailed by the manipulation** (triviality gates 1–4
preflight, §10): the manipulation moves *when the rule is processed relative
to relevance emergence*; which layer the model actually needs is not written
anywhere in the visible content. The headline lives in **T1 vs T2** — the one
contrast no "obvious" story settles.

## 2. Data (to be audited pre-freeze; not yet in the repo)

- **Primary:** **HoVer** (Findings EMNLP 2020, `2020.findings-emnlp.309`) —
  many-hop fact extraction/claim verification over Wikipedia with gold
  decompositions. **2-hop subset only.** Each item contributes: claim, gold
  label, fact A (page 1), fact B (page 2), title path (cluster key, O8).
- **Backup:** MuSiQue (TACL 2022) — connected single-hop composition,
  built to eliminate disconnected shortcuts; used only if HoVer's 2-hop
  funnel fails sufficiency (recorded deviation path, not silent substitution).
- **Not in the repo yet.** Pre-freeze data work is download + structural audit
  only (version, license, sha256, label balance, 2-hop funnel counts, dedup
  against G0/G24A items) — **zero model calls**; §11.
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
EXCL_t / ADMIT_t  for t ∈ {T0, T1, T2}:   layouts exactly as §1,
rule position varies; neutral padding (O7) equalises rule→judgment
token distance within ±10; all other content byte-identical.
```

- Rule sentences are **character-identical across timings** (position is the
  only variable; construction constant + test).
- Padding: fixed hand-authored neutral filler bank, unrelated to claim or
  pages, length-matched per placement; never LLM-generated.
- Same question, output spec, answer format, 0–100 readout across all cells
  (test), per G0/G24A conventions.

## 4. Models (O2)

Pooled primary: `qwen3-8b`, `gemma3-12b`, `llama31-8b`, `qwen35-9b`.
Selector (O1) runs the selection phase only; excluded from pooled inference;
reported as reference. No other model, site, layer, carrier.

## 5. Selection rule (no-rule cells only — blind by construction)

Gates, evaluated on the **selector's** `Y0, YA, YB, YAB` only:

1. **chain works:** `s · (Y_AB − Y_0) ≥ 15`;
2. **A alone insufficient:** `|Y_A − Y_0| ≤ 5`;
3. **B alone insufficient:** `|Y_B − Y_0| ≤ 5`.

(`s` = gold-label direction, G0 mapping: TRUE-claim establishing → +1,
refuting → −1; recorded per item at build; analyzer tested both directions.)

- Gate 2–3 kill the classic *"your two-hop is really one-hop"* shortcut
  (the failure mode MuSiQue was built to expose in datasets) — the reviewer
  attack is designed out at selection, before any exclusion output exists.
- Eligible items taken in frozen HoVer order, **no quotas** (single corpus,
  single label-balanced structure reported descriptively), cap O4.
- Selector blindness: the selection pass provably contains no `EXCL`/`ADMIT`
  rule cell (kind check + test). No outcome of the experiment exists at
  selection time.
- Panel usability (O6) applied **per model** on the panel's own `Y0/YAB`
  (main pass), reported `n/n_total`, never used to drop items post hoc.

## 6. Estimands

Per item × model, raw sign-aligned rating points (house primary metric):

```text
R_t   = s · ( Y_EXCL_t − Y_B )        leakage of A at timing t
        (ideal exclusion = 0: B stays admissible, so Y_B is the counterfactual — not base)

CG    = R_T0 − R_T1                   ContentGain:   content availability at binding
RG    = R_T1 − R_T2                   RelevanceGain: decision relevance at binding
```

`R_t > 0` = excluded A still pulls toward gold; `R_t < 0` = over-suppression
relative to the B-only counterfactual (reported, not clipped).

**Admit-timing control:** `M_t = s · ( Y_ADMIT_t − Y_AB )` — with the chain
fully admissible, timing per se should not move judgments (`M_t ≈ 0`). A
timing slope in `M` means generic rule-position/recency structure → integrity
flag I3 (§8) plus pre-registered sensitivity: `R̃_t = R_t − M_t` (difference-
in-differences), reported alongside regardless.

Usability (O6): all 11 cells present for that model and `s·(Y_AB − Y_0) ≥ 5`.

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
  per timing. No item removed after results exist; reruns only for mechanical
  incompleteness.
- **Power note (design-stage):** CG/RG are within-item differences of
  within-item differences on ≥ 200 items / clustered paths; G23A's simpler
  paired Gap already reached ±4.5 half-width at n=190/68 clusters — the
  1.5-point ROPE (O5) is the number most likely to need power discussion at
  freeze; optional pre-freeze bootstrap note (same pattern as G25A O7).

## 8. Outcome map

Order: **I-gates → S-gates → branches.**

- **I1** rule sentences byte-identical across timings; **I2** distance
  assertion (±10 tokens); **I3** admit-timing control: `M_T0 − M_T2`
  CI contains 0 (else `order-artifact`);
- **I4** RuleAcc ≥ 0.8 on the rule probes (both rule types);
- **S1** ≥ O4-min items (200) after panel usability (O6).

| Verdict | Conditions | Meaning / required action |
|---|---|---|
| `content-bound` | I✓ S✓; **CG positive**; **RG equivalent** | policy binds on content alone; relevance emergence irrelevant → RQ3 answer = content |
| `relevance-bound` | I✓ S✓; **RG positive**; **CG equivalent** | content insufficient — the target→decision relation must exist first → **the non-obvious headline** |
| `staged` | I✓ S✓; CG > 0 **and** RG > 0 | binding builds in stages; both layers matter |
| `timing-insensitive / flat-leaky` | I✓ S✓; CG, RG both equivalent **and** `R` pooled > 0 | composition erases the timing structure while leakage persists |
| `exclusion-robust` | I✓ S✓; CG, RG equivalent **and** all `R_t` equivalent to 0 | chains are excluded cleanly at every timing — sharp contrast with single-hop G24A leak; equally publishable, honestly unexpected |
| `non-monotone` | any primary negative | report as measured; no ordering claim |
| `order-artifact` | I3 (or I2) fails | recency/position structure — no claim until explained via `R̃` |
| `unresolved` | S1 fails, or a needed label is neither positive nor equivalent | report everything; no verdict |

Every row is reachable a priori; none is the manipulation's built-in answer
(gates 3–4, §10).

## 9. Controls and integrity checks

1. Rule identity across timings (byte test) — position is the only variable.
2. Distance assertion test (O7): rule→judgment ±10 tokens across T0/T1/T2;
   pad bank fixed, hand-authored, no LLM generation.
3. Admit-timing control (I3) + DiD sensitivity `R̃` reported unconditionally.
4. Selection blindness: no rule cell in the selection pass (kind check +
   test); gates computable only from `Y0/YA/YB/YAB`.
5. Single-component gates re-verified on the panel's own no-rule cells
   (O3) and reported — the shortcut objection is answerable with panel data.
6. Sign convention tested both directions (establish/refute labels).
7. Same readout/output spec across all 11 cells (test).
8. Cluster integrity in the bootstrap (test).
9. Disjointness from G0/G24A item ids (trivially true — different corpora —
   asserted anyway); dedup recorded at data audit.
10. **No scope creep:** no new site/layer/carrier/model; no LLM-generated
    materials; MuSiQue substitution only as the recorded deviation path in §2.
11. **Wording:** inference-time causal-eligibility control; never "in-context
    unlearning", never generic "representation-vs-deployment" (ACL 2026 Main
    owns that frame).

## 10. Relation to nearest prior (triviality gates)

Five-gate preflight for this design:

1. **Treatment ≠ answer:** the manipulation is *when the rule is processed*;
   no text states which layer (content vs relevance) binding needs. **PASS.**
2. **Reviewer one-liners blocked:** "rule recency" → distance equalisation +
   admit-timing control + DiD (I3/§6); "content must obviously exist first" →
   that is only the content-bound branch, coequal with relevance-bound,
   staged, flat, and robust — none derivable from the prompt. **PASS.**
3. **Two+ live accounts under identical visible content:** content-bound vs
   relevance-bound (+staged/flat), same final context, four live branches.
   **PASS.**
4. **Unexpected-result requirement:** `exclusion-robust`, `flat-leaky`,
   `non-monotone` and both orderings of CG/RG are all publishable surprises.
   **PASS.**
5. **Nearest prior:** verified this session by direct fetch —
   `2024.acl-long.550` (does the model latently compose bridge facts:
   composition *capability*), `2026.acl-long.1937` (multi-hop failure =
   locate vs integrate; position bias), `2026.findings-acl.57` (later
   clarification reinterprets an already-processed word: reactive
   re-anchoring). **None asks whether a policy stated before the target's
   decision-relevance exists can bind it for a later composition.**
   KILLed neighbors (hop depth, base-vs-instruct, withholding, semantic IFC)
   and their priors are catalogued in
   `PAPER_RQ3_CANDIDATE_AUDIT_2026-09-24.md` §1/§6. **PASS**, with the
   standing residual: one manual Anthology/arXiv pass at freeze (session
   websearch unavailable; coverage caveat on record).

## 11. Authorization boundary

**Today (STATUS):** this draft, its review, edits to it, and — flagged for
the ledger's explicit OK — HoVer download + structural audit (zero model
calls). Nothing else.

**Before any G26A forward pass** (all STATUS-gated):

1. §0 O1–O9 signed off; §12 complete with design tag;
2. data audit recorded (version/license/sha256/label balance/2-hop funnel,
   dedup);
3. conditions module (11 cells × layouts × padding), selection module,
   analyzer (R/CG/RG, ROPE logic, order-map), and all tests green;
4. full suite green (current baseline 334 passed / 849 s, five standard
   `--ignore` flags).

**Compute budget (stated up front; the STATUS flip authorizes exactly
this):**

- **Selection pass (selector only):** `N_2hop-audited × 4 no-rule cells × 1
  model` — N pinned at data audit (O9); this is *new* selection compute,
  unlike G25A, hence listed explicitly;
- **Main pass:** ≤ 300 items × 11 cells × 4 models = **13,200** rows, plus
  rule probes ≤ 300 × 4 × 2 = 2,400 → **≤ 15,600** rows;
- no retries-by-outcome; no fifth model; MuSiQue fallback only as the §2
  recorded deviation (requires a prereg amendment **before** any fallback
  compute — post-tag rule).

## 12. Freeze checklist and record

- [ ] §0 open items O1–O9 signed off
- [ ] HoVer data audit recorded (sha256, license, label balance, 2-hop
      funnel, dedup vs G0/G24A); funnel supports S1 ≥ 200 after gates
- [ ] manual nearest-prior pass (Anthology/arXiv) done and recorded
- [ ] rule/padding byte-strings pinned; identity + distance tests green
- [ ] selection-blindness test green (no rule cell in selection pass)
- [ ] selector gate funnel recorded (n passing 1/2/3, capped O4)
- [ ] analyzer tests green: both sign directions, ROPE/positive/undetermined
      trichotomy, outcome-map firing order
- [ ] full test suite green at updated baseline
- [ ] **design tag assigned:** ____________________ (recorded here + ledger)
- [ ] **STATUS flip recorded** (ledger entry authorizing the §11 budget)

No boxes may be checked after the design tag is set (prereg freeze rule);
this file is immutable from the tag onward.
