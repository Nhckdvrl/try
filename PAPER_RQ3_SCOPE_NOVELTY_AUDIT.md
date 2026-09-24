# RQ3 candidate — novelty audit: scope of a prospective exclusion policy

> **SUPERSEDED AS AN RQ3 CANDIDATE (2026-09-24, later the same day).** The
> six-candidate screen (`PAPER_RQ3_CANDIDATE_AUDIT_2026-09-24.md` §1, row E)
> **KILLED** this candidate as the third headline RQ after a broader
> nearest-prior pass surfaced closer parents than this file's channel set
> contained (selective withholding over entangled multi-turn instructions;
> essential-info retention while withholding sensitive context;
> authorized/unauthorized provenance; semantic-transformation information
> flow). The *PROCEED with narrowing* verdict below therefore **no longer
> stands** for headline use. This file is retained as (i) the audit record for
> candidate E and (ii) the source of the claim-boundary wording, which still
> binds any place scope/collateral is discussed (controls/appendix). The live
> third-RQ track is relevance emergence: `PAPER_RQ3_CANDIDATE_AUDIT_2026-09-24.md`.

**Updated:** 2026-09-24. **Status:** AUDIT RECORD for the candidate third RQ.
**Not registrable until the residual coverage note (§6) is accepted and the five
triviality gates are run on the narrowed claim.** No code, no prereg, no compute.

## 1. Candidate RQ (narrowed per the audit)

> **RQ3-candidate: What is the scope of a prospective exclusion policy?**
> Given a policy stated *before* evidence arrives that excludes one designated
> evidence item A, can an LLM (i.e.) (a) prevent A from leaking into the decision and
> (b) *without* collaterally suppressing related, admissible evidence B —
> measured jointly as **target leakage** and **collateral suppression**?

Manipulation sketch (design only): after a decision point, evidence A (policy:
exclude) and evidence B (policy: use normally) both arrive; B varies in its
relation to A (same proposition / paraphrase / lexically similar but different
proposition / same-direction different content / unrelated). Open outcomes:
A leaks & B normal = target-binding failure; A suppressed & B also suppressed
= coarse global suppression; only equivalent-B suppressed = proposition-level
scope generalization; prospective shows scope diffusion while retrospective is
precise = temporal scope-control failure. **No outcome is determined by the
manipulation.**

Claim boundary (keep verbatim in the paper):

> inference-time scope control over the causal eligibility of future evidence —
> NOT parameter/data-level unlearning, NOT generic in-context unlearning, NOT
> RAG source-weighting methods.

## 2. Search performed (2026-09-24)

Two-stage, before any registration:

1. **Systematic related-work audit (background research agent):** ~25 theme
   searches + 8 exact-phrase zero-result searches across ACL/EMNLP/NAACL/TACL/
   ICLR/NeurIPS/ICML 2024–2026 and arXiv 2025–2026. Channels: arXiv search UI,
   Crossref, OpenAlex, ACL Anthology pages. **Tooling caveat (recorded
   honestly):** the agent's `websearch` channel was down all session
   (`Web search cancelled`); Semantic Scholar API rate-limited it (429); DBLP
   behind a bot wall; ACL Anthology's own search box is client-side JS/CSE and
   was not exhaustively covered.
2. **Residual-hole follow-ups (main session, direct fetches):**
   - `site:aclanthology.org "evidence exclusion"` (DuckDuckGo) → **0 results**;
   - `site:aclanthology.org "exclusion policy" evidence exclude` → **0 results**
     (a third DDG query then hit a bot CAPTCHA — DDG coverage stops here);
   - Semantic Scholar citations of arXiv:2410.00382 (Takashiro) → **10 citing
     works**, all listed below — none studies inference-time evidence
     exclusion;
   - OpenAlex citations of the same paper → 2 (the medical-imaging + clinical
     compliance pair; S2 is strictly broader);
   - OpenReview API (`notes/search?term=prospective evidence exclusion`) → 19
     unique titles, all fuzzy-OR noise (runoff-voting "exclusion zones",
     "prospective learning", social-exclusion neuroscience); the single adjacent
     title — *A Within-Model Protocol for Auditing LLM Responses under
     Controlled Evidence Degradation* (TMLR 2026 submission, **Rejected**) —
     audits response robustness while evidence is degraded, not policy-scoped
     causal eligibility;
   - arXiv exact-phrase search UI timed out twice (recorded as a coverage
     limit; phrase already returned zero via other channels).

## 3. Closest priors (survivors of the audit; all URLs verified by fetch)

| # | Work | Venue/Year | What it does | Overlap | Parent-level prior? |
|---|---|---|---|---|---|
| 1 | Answer When Needed, Forget When Not (Takashiro et al.) — https://aclanthology.org/2025.findings-acl.1276/ | Findings ACL 2025 | Fine-tunes the model to conditionally forget target knowledge at test time; retain-side metric; last-layer "pretend to forget" | **Highest**: context-keyed selectivity + retention metric | **No**: knowledge recall, not exclusion of a discrete evidence item among several; no prospective policy; no leakage-of-A metric; requires fine-tuning |
| 2 | In-Context Unlearning (Pawelczyk et al.) — https://arxiv.org/abs/2310.07579 | ICML 2024 | In-context demonstrations to approximate training-data removal | names the space | **No** |
| 3 | Not Every Token Needs Forgetting — https://aclanthology.org/2025.findings-emnlp.96/ | Findings EMNLP 2025 | Parameter-level token-subset unlearning, forget-vs-retain utility | "selective" + retain side | **No**: parameter/data-side scope |
| 4 | RAG with Source Reliability estimation — https://aclanthology.org/2025.emnlp-main.1738/ | EMNLP 2025 | Per-source reliability, top-k reliable retrieval + weighted voting | **multi-evidence, inference-time per-item weighting** | **No**: reliability-driven soft weighting, no policy timing, no collateral metric |
| 5 | Instruction Hierarchy — https://arxiv.org/abs/2404.13208 | arXiv 2024 | Privilege hierarchy: ignore lower-privileged instructions | scope control over instructions | **No**: instructions, not evidence eligibility; no suppression-side measure |
| 6 | Instruction Position Matters — https://aclanthology.org/2024.findings-acl.693/ | Findings ACL 2024 | Instruction-before-input under-following; fix = put instruction after input | instruction-evidence ordering | **No**: no exclusion policy, single input, no scope |
| 7 | LLMs Struggle to Use Representations Learned In-Context — https://aclanthology.org/2026.acl-long.676/ | ACL 2026 Main | In-context-learned representations are not flexibly deployed | failure to apply in-context rules | **No**: no scoped evidence exclusion |
| 8 | PerMU / Erasing Without Remembering — https://arxiv.org/abs/2502.19982 | arXiv 2025 | Parameter-level forget scope over rephrased/neighbor data | **terminology collision: "unlearning scope"** | **No**: fine-tune forget-set design |
| 9 | GRAIL — https://arxiv.org/abs/2504.12681 | arXiv 2025 | Parameter-level unlearning targeting/scope | term overlap | **No** (abstract-level check) |
| 10 | ARIA test-time unlearning — https://arxiv.org/abs/2609.16229 | arXiv 2026 | Prompt-based test-time unlearning | wording adjacency | **No** (snippet-level; unverified) |
| 11 | ST²U / MLLMEraser — https://arxiv.org/abs/2608.23034, https://arxiv.org/abs/2510.04217 | arXiv 2025–26 | Test-time unlearning (multimodal) | adjacency | **No** (snippet-level; unverified) |
| 12 | LegalBench hearsay follow-ups — https://arxiv.org/abs/2506.16335, https://arxiv.org/abs/2601.01609 | arXiv 2025/26 | Single-statement hearsay-admissibility classification | legal admissibility theme | **No**: one-statement classification, no multi-evidence scope |

**The 10 Semantic Scholar citations of Takashiro 2410.00382** (checked
2026-09-24): CBD API-only unlearning; medical-imaging foundation-model
unlearning; clinical-study DPA compliance unlearning; multi-objective LLM
unlearning via logit distillation; refusal unlearning with 1,000 benign
samples; npj biomedicine survey; *A Survey on Unlearning in LLMs*; requirement
test-case generation; *SoK: Machine Unlearning for LLMs*; UniErase unlearning
token. **None** follows the in-context-unlearning line into scoped,
inference-time, evidence-level exclusion.

## 4. One-liner test ("这不是当然的吗？")

Strongest dismissal: *"Isn't this just prompting — 'ignore A, use the rest'?
Of course a model told to ignore A ignores it; any failure is known
prompt-robustness (instruction hierarchy, position effects)."* Each ingredient
is individually published (position effects, context-keyed forgetting,
multi-source weighting), so a reviewer can assemble "obvious" from three papers.

Why it does not kill the **narrowed** RQ: the naive prompt is the hypothesis,
not the answer — the content is whether the manipulation produces a
**non-trivial trade-off**: nonzero leakage through A *and* nonzero collateral
suppression of B, and whether policy timing (prospective vs retrospective)
changes that trade-off. Required design responses (write into any future
prereg): (a) leakage/collateral trade-off curve (a suppress-everything model
scores zero leakage and is useless — accuracy-only metrics cannot see this);
(b) prospective vs retrospective contrast as the manipulated variable;
(c) related-evidence controls over semantic distance from A (collateral should
decay with distance if scope is graded, not blanket refusal).

## 5. Verdict and recommendation

**PROCEED, with narrowing** — no parent-level prior found in any reachable
channel; the closest line (in-context unlearning) has 10 citations, none
colonizing the space. Narrowed claim = pure inference-time/prompting (no
fine-tuning), multiple simultaneous evidence items with one designated
exclusion, joint leakage + collateral metrics as the dependent variables,
prospective timing as the manipulated variable. Preempt the two loudest
"prior art" objections in related work: 2025.findings-acl.1276 (context-keyed
forgetting ≠ evidence eligibility) and 2025.emnlp-main.1738 (reliability
weighting ≠ policy exclusion), contrasting on the two axes each differs on.

**Do not self-label "in-context unlearning"** — it invites priors 1–2.

## 6. Residual coverage note (accept before registering)

`websearch` was unavailable all session; DuckDuckGo served two zero-result
site-restricted queries then rate-limited; arXiv's own search UI timed out;
ACL Anthology's JS search box was not exhaustively covered. Converged
independent channels (Crossref, OpenAlex ×2, Semantic Scholar, OpenReview,
DDG ×2, ~25 theme searches) all return no parent-level prior. The remaining
risk is a very recent Anthology/arXiv paper not indexed by any of these — the
standard pre-registration cost. If the candidate passes the five gates, one
final manual pass over ACL Anthology 2026 + arXiv listing for the exact claim
sentence is the last step before any prereg text is written.
