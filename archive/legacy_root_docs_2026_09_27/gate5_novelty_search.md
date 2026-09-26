# Novelty Gate 5 — Nearest-Prior Literature Search

**Reframed RQ2:** *Is prospective exclusion a smooth evidence-weighting problem, or is exact semantic zero a qualitatively different control boundary?*

**Date:** 2026-09-24 · **Method:** arXiv API abstract screening (~30 query families), Semantic Scholar + websearch unavailable (see Coverage Limits). Abstract-level only; no full papers read. Venue tags are taken from arXiv comment/metadata fields and marked *per arXiv* where not independently verified.

---

## Table A — Evidence-integration priors (search A)

| # | Title | Venue / Year | URL | Finding (2 lines) | Owns zero-boundary claim? |
|---|---|---|---|---|---|
| A1 | Evidence Integration in LLMs | arXiv preprint, 2026 | https://arxiv.org/abs/2609.04290 | 10M-trial design crossing receiver prior weight with evidence tilt; models integrate both gradedly, tilting toward a message even *after* judging it invalid. Directly establishes graded, non-Bayesian-but-continuous evidence weighting. | **No** — no w=0 condition, no instructed weight, no timing manipulation |
| A2 | BayesBench | arXiv preprint (under review), 2026 | https://arxiv.org/abs/2606.30850 | Bayesian-reasoning benchmark; quantifies deviation from normative updating. Measurements of *accuracy*, not of an instructed weight parameter. | **No** |
| A3 | Inference-Time Elicited Probability Transformations | arXiv preprint, 2026 | https://arxiv.org/abs/2603.19262 | Elicits probability transformations with a log-ratio / α evidence-gain structure — i.e., a *graded, nonlinear* combination function over evidence strength. | **No** — continuous gain, no boundary at zero |
| A4 | Overconfidence/underconfidence in change-of-mind | arXiv preprint, 2025 | https://arxiv.org/abs/2507.03120 | Models overweight inconsistent advice when revising beliefs; graded updating with a systematic bias. Shows nonlinearity ≠ discontinuity. | **No** |
| A5 | Martingale Score / belief entrenchment | NeurIPS 2025 *per arXiv* | https://arxiv.org/abs/2512.02914 | Belief updates violate the martingale property (entrenchment) under sequential evidence. A sequential-integration failure mode. | **No** |
| A6 | LLMs Anchor on Chief Complaint | arXiv preprint, 2026 | https://arxiv.org/abs/2609.22904 | Sequential evidence integration fails via anchoring on early evidence; later evidence underweighted. Failure is *degree of weight*, not a zero/nonzero switch. | **No** |
| A7 | Knowledge Conflicts for LLMs | ICLR 2024 spotlight | https://arxiv.org/abs/2305.13300 | Injected context conflicting with parametric memory: models sometimes override one source entirely. Closest thing to "evidence set to zero" — but it is *conflict resolution*, not an instructed weight. | **Partial** — source suppression exists, but no numeric weight, no 0-vs-1 contrast |
| A8 | DeReLab (confirmation bias in evidence reasoning) | EMNLP 2026 *per arXiv* | https://arxiv.org/abs/2608.30413 | Documents confirmation bias when reasoning over evidence collections. Directional bias in weighting, not a boundary at w=0. | **No** |
| A9 | RA-RAG (source-reliability weighting) | arXiv preprint, 2024 | https://arxiv.org/abs/2410.22954 | Adaptively weights retrieval sources by estimated reliability during generation — graded weighting is *learned/implicit*, not instructed. | **No** |
| A10 | Confirmation bias in chain-of-thought | ACL 2025 Findings *per arXiv* | https://arxiv.org/abs/2506.12301 | CoT amplifies confirmation bias over evidence; reasoning traces lock in early evidence. Again a graded-weight pathology. | **No** |

Also screened (not tabulated): collider/explaining-away https://arxiv.org/abs/2602.02983 , https://arxiv.org/abs/2502.10215 ; QUITE https://arxiv.org/abs/2410.10449 ; Evidence-Weighting in Psychiatric Screening https://arxiv.org/abs/2605.23148 ; Record Grouping Controls Evidence Weight https://arxiv.org/abs/2609.08698 . None condition on an instructed weight at or near zero.

---

## Table B — Numeric / graded instruction-compliance priors (search B + sanity check)

| # | Title | Venue / Year | URL | Finding (2 lines) | Owns zero-boundary claim? |
|---|---|---|---|---|---|
| B1 | Semantic Gravity Wells: Why Negative Constraints Backfire | arXiv preprint, 2026 | https://arxiv.org/abs/2601.08070 | Mechanistic account: negative/zero-valued constraints follow a logistic violation curve, with a 5.2pp vs 22.8pp suppression asymmetry — lexical negatives behave qualitatively differently from positives. **Closest overall prior.** | **Partial** — establishes a positive/negative *qualitative* asymmetry for lexical constraints; no numeric weight w, no prospective timing, no semantic-causal evidence |
| B2 | Via Negativa (position paper) | arXiv preprint, 2026 | https://arxiv.org/abs/2603.16417 | Position paper that negative instructions are systematically weaker/harder than positive ones. Argues the asymmetry, no quantitative weight sweep. | **Partial** |
| B3 | Ruler | NAACL 2025 *per arXiv* | https://arxiv.org/abs/2409.18943 | Numeric length constraints ("exactly N words") degrade with number magnitude and format; compliance is graded in difficulty, not examined at a zero boundary. | **No** |
| B4 | CAPITU (exact-counting failures) | arXiv preprint, 2026 | https://arxiv.org/abs/2603.22576 | Models fail *exact* counting/quantity instructions. Failure of exactness generally, not a 0-vs-1 asymmetry. | **Partial** |
| B5 | DIALEVAL (exact numeric predicates) | arXiv preprint, 2026 | https://arxiv.org/abs/2603.03321 | Exact numeric predicates in evaluation dialogues are brittle. Same pattern: exact-number handling is hard, but no weight=0 contrast. | **Partial** |
| B6 | Transformers Learn Gradient Descent by In-Context Update | ICLR 2023 *per arXiv* | https://arxiv.org/abs/2212.10559 | ICL implements (un)supervised gradient descent steps on the prompt — the mechanistic basis for treating in-context instruction as a *smooth* weight on data. | **No** — supports smoothness, no zero boundary tested |
| B7 | What Can Transformers Learn In-Context? (linear/ridge regression) | NeurIPS 2023 *per arXiv* | https://arxiv.org/abs/2211.15661 | ICL learns least-squares/ridge-like predictors — smooth interpolation over in-context evidence weights. | **No** |
| B8 | In-Context Task Vectors | ICLR 2024 *per arXiv* | https://arxiv.org/abs/2310.15916 | Tasks induce linear "task vectors" in activation space, scaling with demonstrations — graded, continuous task encoding. | **No** |
| B9 | Prospect-theory evaluation of LLM decision-making | arXiv preprint, 2024 | https://arxiv.org/abs/2406.05972 | LLMs overweight *small* probabilities (human-like probability weighting). Directly relevant to sanity check: small ≠ zero is already a known nonlinearity. | **Partial** — small-vs-large nonlinearity exists; says nothing about instructed exclusion at exactly 0 |
| B10 | Aligning LMs with Selective Prediction | arXiv preprint, 2026 | https://arxiv.org/abs/2607.03528 | Selective-prediction/abstention framing over thresholds; thresholds swept as continuous control. No treatment of threshold exactly zero as special. | **No** |

Also screened (not tabulated): scalar-output bunching around arbitrary numbers https://arxiv.org/abs/2509.03116 (EMNLP 2025 *per arXiv*) — LLM point estimates are attracted to round/arbitrary anchors, a *continuity* pathology; Transformers Don't ICL Least Squares https://arxiv.org/abs/2507.09440 ; SAIF instruction positioning https://arxiv.org/abs/2502.11356 ; HG-CRC conformal selective prediction https://arxiv.org/abs/2607.24562 ; FermiEval overconfidence https://arxiv.org/abs/2510.26995 . None owns a zero boundary.

---

## Per-search verdicts

| Search | Scope run | Verdict |
|---|---|---|
| **A. Evidence integration / calibration linearity** | ~15 arXiv query families: "evidence integration"+LM, Bayesian updating+LLM, evidence weighting, confirmation bias+evidence accumulation, source reliability+RALM, weight of evidence, anchoring, likelihood ratio, explaining away, conditional independence, probability matching, probability elicitation | **No prior owns the RQ2 claim.** The line firmly establishes (i) LLMs *do* integrate evidence gradedly (A1, A3), (ii) that integration is *biased/nonlinear but continuous* (A4, A5, A6, A8, A10), and (iii) occasionally source-suppressive under conflict (A7). Nothing manipulates an *instructed* weight prospectively, and nothing tests w=0 vs w>0. |
| **B. Numeric / graded instruction compliance** | ~12 arXiv query families: numeric instructions, numeric constraint+IF, exact+constraint+IF, negative constraint, instruction strength, ICL+task vector, ICL+gradient descent, small probabilities, probability weighting, instruction position, selective prediction | **No prior owns the RQ2 claim.** Nearest are B1/B2 (lexical negative constraints fail qualitatively differently) and B4/B5 (exact numeric predicates are brittle). Both are *lexical/exactness* results on constraint-type instructions, not a numeric weight applied to inferred semantic evidence, and neither has a prospective-timing arm. |
| **Sanity: contrastive / decaying instruction strength** | "instruction strength", decaying instruction, contrastive prompting | **No text-prompting prior found.** Only hit was image-editing strength control (Kontinuous Kontext, CVPR 2026 *per arXiv*, https://arxiv.org/abs/2510.08532 ) — out of scope. |
| **Sanity: "model ignores small probabilities" / probability matching** | probability matching, ignore small probabilities, in-context probability estimation | **No LLM prior found.** Probability-matching hits are human decision theory (e.g., https://arxiv.org/abs/2205.11561 ). The nearest LLM result cuts the *other* way: small probabilities are *over*weighted (B9). |
| **Sanity: abstention / selective prediction at threshold zero** | abstention threshold, threshold zero, selective prediction | **No prior treats 0 as special.** Thresholds are swept continuously (B10, https://arxiv.org/abs/2607.24562 ). |
| **Gap: "zero instruction" + LM; evidence+discontinuity+LM** | Final gap queries this round | **Empty / irrelevant** (3 hits, all name-matches: zero-init prompt optimization, speech zero-instruction tuning; discontinuity hits were metric-artefact and unrelated). |

---

## Refreshed reviewer one-liner

> **「零本来就是唯一的真指令，模型只是不执行小数权重，这不显然吗？」**
> *"Isn't it obvious — zero is the only real instruction; models just don't execute fractional weights."*

**Rebuttal the design must already support:** the arithmetic control (answer = base + w·delta), where **4/5 models execute w=0 exactly and prospectively**, refutes "models can't execute zero." The failure is confined to applying the weight to the *inferred causal contribution of semantic evidence*. A fractional-weights-only account also predicts a *monotone* degradation across w=1/25/50/100, which the data contradict: pre-vs-post influence gap is flat across w=100 (−0.27), w=50 (+4.51), w=25 (+4.99), w=1 (+5.59) and jumps only at w=0 (+13.86).

---

## Wording hazards (do not claim)

1. ❌ "LLMs cannot integrate evidence gradedly / nonlinearly." — Partly owned by A1, A3, A4. Safe form: *graded integration exists but is instructed-locally smooth; the discontinuity is at the semantic-zero boundary under prospective timing.*
2. ❌ "Zero/negative instructions uniquely fail." — Owned for *lexical* negative constraints by B1, B2. Safe form: *the asymmetry extends to numeric weights on inferred causal contributions, where it coincides with prospective timing.*
3. ❌ "Small/zero probabilities are ignored." — Contradicted by B9 (small probabilities *over*weighted).
4. ❌ "Evidence weight discontinuity in LLMs" as a headline — no prior says this, but Schaeffer-style metric-artefact critiques (https://arxiv.org/abs/2304.15004 ) will be raised against any claimed discontinuity; prereg must pre-specify a *linear-scale* contrast (w=1 vs w=0), not a thresholded metric.

---

## Gate-5 recommendation

**Remain OPEN — one narrow round — with provisional PASS.**

- **Why not FAIL:** no located prior owns the "discontinuity at exactly w=0 under prospective instructed weighting of inferred semantic evidence" claim. Searches A and B and all three sanity checks came back clear.
- **Why not yet CLOSE:** coverage is **arXiv-abstract-only**. Semantic Scholar returned HTTP 429 on every attempt; the websearch tool cancelled on every attempt; ACL Anthology's search endpoint is a JavaScript/Google-CSE page that returned no result items to a plain fetch. Non-arXiv venues (OpenReview, ACL Anthology full text, Google Scholar) are *unverified*, and all screening was abstract-level.

**Named further searches to close the gate:**
1. **OpenReview** (openreview.net API/search) for ICLR 2025–2027 / NeurIPS 2025–2026 submissions matching `("evidence weight" | "instruction weight" | "exclude evidence") AND ("language model" | LLM)`.
2. **ACL Anthology** via its Google CSE JSON endpoint (or a direct site-restricted fetch) for `"zero" + "evidence" + "instruct" + language model` and `"weight of evidence" + LLM`.
3. **Semantic Scholar** retry with backoff for `prospective instruction evidence exclusion LLM` and `numeric instruction compliance zero boundary`.
4. Read-verify (full text, not abstract) the two closest neighbors before prereg wording is frozen: **B1 Semantic Gravity Wells** (https://arxiv.org/abs/2601.08070 ) and **A1 Evidence Integration in LLMs** (https://arxiv.org/abs/2609.04290 ).

If those four come back empty or non-owning → **CLOSE as PASS**, scoped exactly as in the wording-hazards section.

---

## Round-2 coverage follow-ups (2026-09-24, main session, direct fetches)

The `websearch` tool was down for the entire session (`Web search cancelled`
on every attempt, both agents), so all four named searches were re-run as
direct HTTP fetches. Results, verbatim:

1. **OpenReview API** (`api2.openreview.net/notes/search?term=prospective
   evidence exclusion`) → 19 unique titles, all fuzzy-OR noise (runoff-voting
   "exclusion zones", "prospective learning", social-exclusion neuroscience).
   Single adjacent title: *A Within-Model Protocol for Auditing LLM Responses
   under Controlled Evidence Degradation* — TMLR 2026 submission, **Rejected**
   (abstract behind a bot-check; classified from title/venue: it audits
   response robustness while evidence quality is degraded, not instructed
   weights or timing). → **non-owning**.
2. **ACL Anthology site-restricted** (DuckDuckGo stand-in for the nonexistent
   public CSE JSON endpoint): `site:aclanthology.org "evidence exclusion"` →
   **0 results**; `site:aclanthology.org "exclusion policy" evidence exclude` →
   **0 results**; a third query then hit DDG's bot-CAPTCHA (coverage stops
   there, recorded below).
3. **Semantic Scholar retry**: paper **search** endpoint still HTTP 429 twice
   for both gate-5 queries; the **citations** endpoint did succeed (used for
   the RQ3 audit: 10 citations of arXiv:2410.00382, none relevant). arXiv's
   own search UI timed out twice; OpenAlex exact-phrase endpoint 503 once;
   OpenAlex fuzzy full-text search returned only noise for these phrasings.
   → phrase-level S2/arXiv coverage remains incomplete (residual, below).
4. **Full abstract read of the two closest neighbors** (fetched in full from
   arXiv, not snippets):
   - **B1 Semantic Gravity Wells** (https://arxiv.org/abs/2601.08070 ):
     lexical negative constraints ("do not use word X"); violation follows
     logistic semantic pressure (p = σ(−2.40 + 2.27·P₀), n = 40,000); priming
     failure 87.5% vs override failure 12.5%; layers 23–27 confirmed by
     activation patching. **Word-level, no numeric weight, no timing** →
     non-owning; wording hazard §3.2 unchanged (cite as the lexical neighbor).
   - **A1 Evidence Integration in LLMs**
     (https://arxiv.org/abs/2609.04290 ): receiver prior weight × candidate
     evidence tilt, 10M trials, 12 LLMs / 4 families / 8 domains; models
     integrate gradedly *and* keep integrating after internally verifying
     invalidity; verification is decodable but causally inert (late-network
     candidate-integration sequence). **Establishes smooth/graded integration
     with no w=0 condition and no instructed weight** → non-owning — and it
     *raises the prior expectation of smoothness*, which our flat-then-jump
     ladder contradicts (strengthens the surprise). New hazard note: do not
     claim their verification-vs-action dissociation as ours; our object stays
     timing + semantic zero.

## Final gate-5 verdict

**CLOSED as PASS**, scoped exactly as in the wording-hazards section above.

- All four named searches completed; none owns the claim.
- **Residual (recorded honestly):** S2 phrase search (429), arXiv search UI
  (timeouts), DDG beyond two queries (CAPTCHA), and ACL Anthology's JS search
  box were not covered; multi-channel convergence (30+ query-family abstract
  screening, OpenReview, DDG site ×2, Crossref/OpenAlex/S2 citation chasing)
  found no owning prior in any reachable channel. Same residual class as
  `PAPER_RQ3_SCOPE_NOVELTY_AUDIT.md` §6: one final manual pass over ACL
  Anthology 2026 + arXiv listing at prereg-freeze time.

## Freeze-time manual pass — COMPLETED 2026-09-24 (closes the residual above)

Executed as the prereg-mandated final pass, over every channel reachable
this session (websearch tool down all session; Semantic Scholar and one
OpenAlex query endpoint 429 on repeated retries):

1. **ACL Anthology official ACL-2026 event listing**
   (`https://aclanthology.org/events/acl-2026/` — 18.9 MB server-rendered
   HTML: ACL 2026 long/short/demo/srw/industry/findings + the co-located
   workshop volumes attached to the event): **6,422 papers parsed with
   titles, 6,365 with abstracts**; three-tier screen, every hit read:
   - **T1** title strong terms (`weight|exclus|abstain|prospectiv|zero|
     attenuat|nullif|disregard`): **149 hits — all reviewed**; classes:
     zero-shot * (TTS/NER/retrieval), lightweight/compression *,
     ensemble re-weighting * (shared-task systems), model-sparsity *.
   - **T2** title `eviden|context|information` × action co-terms
     (`ignor|discard|select|priorit|relevan|overrid|suppress|order|
     timing|position|attend|...`): **25 hits — all reviewed**; classes:
     retrieval/context selection, attention position, token pruning.
   - **T3** abstract claim-phrase patterns (`weight(ed|ing) of evidence`,
     `zero weight`, `w=0`, `prospective`, `ignore/exclude ... evidence`,
     `before seeing ...`, `evidence ... ordering|timing|sequence`,
     `instructed weight`): **91 hits — all reviewed**; classes: ensemble
     weights, position/attention mechanics, retrieval pipelines.
   - Named near-objects with one-line verdicts (all **non-owning**):
     `2026.bionlp-1.50` *When Evidence Conflicts: ... Order Effects* →
     order-effects class, already non-owning (Table A);
     `2026.acl-srw.91` *Neglect-Zero Effect* → **numerical** zero handling,
     not instructed semantic weight;
     `2026.trustnlp-main.33` *Prospective Memory Failures in LLMs* →
     prospective **memory** (forgetting intended future actions), not
     prospective evidence timing;
     `2026.acl-long.1151` *CUB: Context Utilisation benchmark* → no
     instructed weight, no w=0;
     `2026.acl-long.1365` / `2026.findings-acl.985` abstention
     calibration → output refusal, not evidence weighting;
     `2026.acl-long.1245` *Attention Weights as an Indicator* → diagnostic
     attention analysis, not instructed numeric weight.
2. **arXiv API, 4 phrase-query families, all hits read:** `abs:"evidence
   weight" AND abs:"language model"` (10), `abs:"prospective exclusion"
   OR abs:"evidence attenuation" OR abs:"weighted evidence integration"`
   (2), `abs:"evidence weighting"` (21), `abs:"evidence" AND abs:"zero
   weight"` (8) — 41 hits with overlap, zero matches on the claim; closest
   is a 2013 Bayesian-network simulation paper (pre-LLM, different object).
3. **OpenAlex:** `"prospective evidence"` (2025+) → 10 epidemiology/medical
   hits, zero NLP; `"evidence weighting" language model` → 429 on 3
   retries. **S2 paper search** → 429 on 3 retries (unchanged from round 1).

**Verdict: PASS — residual closed.** No owning or near-owning prior for a
*weight-ladder boundary under prospective exclusion* in any reachable
channel. Honest coverage caveats: Anthology screen is title+abstract level
(not full text); S2 / one OpenAlex query unreachable (429); arXiv covered by
phrase queries (not a full cs.CL enumeration); websearch tool unavailable.
