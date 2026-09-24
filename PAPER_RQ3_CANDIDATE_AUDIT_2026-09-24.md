# RQ3 six-candidate novelty screen — decision record

**Date:** 2026-09-24 (user-run full novelty screen, later the same day as the
scope audit it partly supersedes).
**Status:** DECISION RECORD + audit trail. **No code, no prereg tag, no
compute** (STATUS: paper writing + novelty audit only). The next allowed step
is a design-level prereg *draft* for the survivor, gated exactly like RQ2's:
five triviality gates written down, then a STATUS flip before any harness work.

---

## 1. What was screened

Six candidate third-RQs, each confronted with its nearest prior and an
average-reviewer one-liner **before** any design work. Channels covered:
multi-hop reasoning, delayed interpretation / re-anchoring, belief revision,
selective withholding, provenance / information-flow, base-vs-instruct
post-training, irrelevant-evidence filtering.

| # | Candidate | Nearest prior / reviewer compression | Verdict |
|---|---|---|---|
| **A** | **Relevance emergence** — must an exclusion policy see the target's *content*, or must the target's *decision relevance* already be established when the policy is processed? | latent multi-hop composition (ACL 2024); weakest-link locate-vs-integrate (ACL 2026); deferred semantic drift reinterprets an earlier word after later clarification (Findings ACL 2026). **None asks whether a prior policy can bind a target whose relevance does not yet exist.** | **SURVIVOR → prereg-draft track** |
| **B** | **Exclusion vs negation** — is "do not use E" executed as removing E's contribution, or as distorting belief about E? | Belief-R / belief revision (EMNLP 2024) studies whether new evidence updates beliefs *correctly*; it does not distinguish an exclusion operator from an epistemic-negation operator. | **BACKUP pilot only** — gold semantics of "assume E is false" is dirty on natural evidence (no reason claim-likelihood should move in a fixed direction); needs a resource with a natural clean complement before prereg. |
| C | Hop depth (1/2/3-hop → exclusion degrades) | multi-hop failure literature is crowded; ACL 2026 already systematizes hop / recognition / synthesis failures; "more hops = harder" is obvious. | **KILL** |
| D | Post-training origin (does base→instruct *create* prospective-exclusion failure) | ACL 2025 instruction-tuning × misinformation susceptibility; ACL 2026 base-vs-instruct context-following. Parent collision; model-zoo shaped. | **KILL** |
| E | **Scope / collateral suppression** — exclude A without leaking through it or collaterally suppressing related B (the previous candidate, `PAPER_RQ3_SCOPE_NOVELTY_AUDIT.md`) | broader pass surfaced closer parents than that audit's 12-row table contained: selective withholding over entangled multi-turn instructions (Findings EMNLP 2025), retaining essential information while withholding sensitive context (CI-Work), authorized/unauthorized competing-evidence provenance, and semantic-transformation / source→sink information flow (arXiv 2604.23374 neighborhood). | **KILL as RQ3** — see §4 supersession |
| F | Inferential closure — does a conclusion *derived* from excluded A still influence the decision? | arXiv 2604.23374 ("Ghost in the Agent") explicitly extends LLM information-flow tracking to semantic transformation, causal influence, source→sink propagation. Easy reviewer re-parenting into security / IFC. | **KILL (HOLD)** |

## 2. Survivor A — relevance emergence (what the prereg draft must encode)

> **RQ3: Does prospective exclusion require the target content to be
> available, or must its decision relevance already be established when the
> policy is processed?**

Two-hop evidence chain `A + B ⇒ claim`, each component individually
insufficient (gates below). The final context is **identical** across
timings; only the state of the target when `RULE(A)` is processed varies:

```text
T0: RULE(A) → A  → B → judgment   # content unknown, relevance unknown
T1: A → RULE(A)  → B → judgment   # full content known, relevance not yet established
T2: A → B → RULE(A)   → judgment   # content known AND relevance established
```

Competing accounts — **none entailed by the manipulation**:

| Account | Prediction |
|---|---|
| content-bound | `T1 ≈ T2 ≫ T0` — content existing suffices for binding |
| relevance-bound | `T2 ≫ T1 ≈ T0` — the policy needs the target→decision relation established |
| staged | `T2 > T1 > T0` — binding builds progressively |
| composition-wide flat | `T0 ≈ T1 ≈ T2` — under multi-hop composition, exclusion loses its timing structure entirely |

**Materials.** HoVer (Findings EMNLP 2020) **2-hop only** at first — natural
many-hop fact verification, claim decomposed across Wikipedia articles; MuSiQue
(TACL 2022, connected single-hop composition, built to kill disconnected
shortcuts) as documented backup. Selection phase never shows any exclusion
rule. Anti-shortcut gates evaluated on **no-rule cells only**:

- `s · (Y_AB − Y_0) ≥ 15` — the joint chain has a real effect;
- `|Y_A − Y_0| ≤ 5` and `|Y_B − Y_0| ≤ 5` — **neither single component can
  explain the joint effect** (blocks the classic "your two-hop is really
  one-hop" reviewer attack).

Target ≈ 200–300 items surviving gates, 4 models.

**Outcome.** The ideal counterfactual for "A excluded" is `Y_B`, not base — B
remains admissible:

- `Residual_t = s · (Y_ExcludeA,t − Y_B)` — perfect exclusion = 0;
- `ContentGain = Residual_T0 − Residual_T1`;
- `RelevanceGain = Residual_T1 − Residual_T2`.

All four branches (content-bound / relevance-bound / staged / flat) are
informative; no branch is the manipulation's built-in answer.

**Required pre-registered control.** T2 places the rule closest to the
judgment, so without intervention the reviewer answer is *"that's just
instruction recency"* — and our own delay manipulations show recency is a
live effect here. Therefore: (a) length-match the three timings with
unrelated neutral blocks so rule→judgment token distance sits in one common
window; (b) run matched **Admit/Use-normal rule-timing controls** so generic
recency is measured and subtracted. The experiment then compares *relevance
state*, not *rule distance*.

**Why not the nearest priors** (binding text for related work):

- ACL 2024 `2024.acl-long.550` asks whether models latently build a bridge
  entity and use it (composition *capability*);
- ACL 2026 `2026.acl-long.1937` asks whether multi-hop failure is *locating*
  or *integrating* evidence, plus position bias;
- Findings ACL 2026 `2026.findings-acl.57` asks how later clarification
  reinterprets an already-processed ambiguous word (reactive re-anchoring).

None owns: *can a policy stated before a target's decision-relevance exists
ever become an effective constraint on a later composition?*

**Status:** survives novelty; the five triviality gates + one coverage
residual get written into the prereg draft next; harness/tag/compute only
after an explicit STATUS flip.

## 3. Existing assets are not wasted

Stage 5 / G23C / G24B remain supporting causal evidence. If RQ3-A lands a
content-bound / relevance-bound / staged structure, we then decide whether
those causal results *explain* that structure — **never the reverse**: no RQ
is reverse-engineered from existing patching results (standing rule).
G23C-R stays HOLD / NO COMPUTE (`c051821`).

## 4. Supersession of the scope audit

`PAPER_RQ3_SCOPE_NOVELTY_AUDIT.md` (earlier the same day) concluded *PROCEED
with narrowing* for candidate E. This screen ran a broader channel pass
(selective withholding, CI-Work, provenance, NeuroTaint-style semantic IFC)
and surfaced closer neighbors than that audit's table contained → **E is
killed as an RQ3 headline.** The older file remains as the audit record for
that candidate, and its claim-boundary wording ("inference-time/prompt-only,
one designated exclusion among multiple simultaneous evidence items, never
self-label *in-context unlearning*") still binds any place scope is discussed
(controls / appendix). A superseded banner sits at its top. Honest ledger:
the later, broader search wins; the earlier PROCEED no longer stands.

## 5. Paper skeleton after this decision

- **RQ1** — can models commit to exclude future evidence? (G0 + six controls
  + agent + G24A; section draft `PAPER_SECTION_RQ1.md` done).
- **RQ2** — smooth weighting problem, or exact-zero control boundary?
  (G23A ladder + arithmetic boundary + **natural near-zero confirmatory,
  quotas frozen at Option B**; `PAPER_RQ2_BOUNDARY_REFRAME.md`,
  stratum audit `PAPER_RQ2_SWEEP_STRATUM_AUDIT_2026-09-24.md`).
- **RQ3** — what must be known when an exclusion policy binds: the evidence
  content, or its decision relevance (**relevance emergence**, HoVer 2-hop;
  design stage — this file).
- If RQ3's gates fail: **accept the two-finding paper** — "如果找不到第三题，
  就不要凑".

## 6. Citations carried from the screen

Canonical URLs (tracking params stripped). **Spot-check status:**

- ✅ independently fetched and title/abstract verified this session:
  `2024.acl-long.550`, `2026.acl-long.1937`, `2026.findings-acl.57`
  (the three load-bearing neighbors of survivor A);
- cited by the screen, not independently re-fetched here: [2] [4] [5] [6]
  [7] [8] — same residual rule as RQ2 gate 5: one manual pass at
  prereg-freeze time. (Session websearch was unavailable throughout; coverage
  caveat recorded.)

| # | Reference | URL |
|---|---|---|
| 1 | Yang et al. — Do Large Language Models Latently Perform Multi-Hop Reasoning? (ACL 2024) ✅ | https://aclanthology.org/2024.acl-long.550/ |
| 2 | Belief Revision: The Adaptability of Large Language Models Reasoning (EMNLP 2024) | https://aclanthology.org/2024.emnlp-main.586/ |
| 3 | Zhang et al. — Failure Modes in Multi-Hop QA: The Weakest Link Effect and the Recognition Bottleneck (ACL 2026) ✅ | https://aclanthology.org/2026.acl-long.1937/ |
| 4 | Exploring the Impact of Instruction-Tuning on LLM's Susceptibility to Misinformation (ACL 2025) | https://aclanthology.org/2025.acl-long.1295/ |
| 5 | Can Language Models Follow Multiple Turns of Entangled Instructions? (Findings EMNLP 2025) | https://aclanthology.org/2025.findings-emnlp.1387/ |
| 6 | Ghost in the Agent: Redefining Information Flow Tracking for LLM Agents (arXiv) | https://arxiv.org/abs/2604.23374 |
| 7 | HoVer: A Dataset for Many-Hop Fact Extraction And Claim Verification (Findings EMNLP 2020) | https://aclanthology.org/2020.findings-emnlp.309/ |
| 8 | MuSiQue: Multihop Questions via Single-hop Question Composition (TACL 2022) | https://aclanthology.org/2022.tacl-1.31/ |
| 9 | Zeng et al. — Mechanistic Insights into Deferred Semantic Drift in LLMs (Findings ACL 2026) ✅ | https://aclanthology.org/2026.findings-acl.57/ |
