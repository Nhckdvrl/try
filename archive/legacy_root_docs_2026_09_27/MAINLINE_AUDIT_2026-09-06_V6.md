# Mainline audit V6 — correction after adversarial data and novelty audit

**Date:** 2026-09-06  
**Target:** NAACL / ACL / EMNLP Main.  
**Status:** current experiment-priority authority.  
**Supersedes for priority:** `MAINLINE_AUDIT_2026-09-06_V5.md`.  
**Does not erase:** V5, earlier audits, preregistrations, failed experiments, or frozen results. They remain research-history provenance.

---

# 0. Why V6 exists

V5 moved too quickly from an interesting old anomaly to a candidate mainline:

> exact zero may be a qualitative boundary in semantic influence control.

That was premature.

A deeper audit of:
- the frozen Stage-3 design;
- the formal zero-kink test;
- raw generations;
- cluster structure;
- the REI estimand;
- the verifiable arithmetic control;
- 2024–2026 work on forgetting, unlearning, advice weighting, nonlinear belief updating, negated constraints, and the special status of zero;

shows that the repository does **not** currently establish a cross-model “0% vs 1% cliff”, and the conceptual novelty bar is substantially higher than V5 stated.

The correction is deliberate:

> **An anomaly is not a research question. A significant pooled effect is not a law. A law is not novel merely because its exact prompt has not appeared before.**

No model generation is authorized by this audit.

---

# 1. Executive decisions

| object | V6 verdict | reason |
|---|---|---|
| G0 prospective exclusion reversal | **HIGH-RISK ASSET / NOT DEFAULT MAINLINE** | empirically strong, conceptual neighborhood crowded |
| G18 semantic targeting | **SUPPORTING ONLY** | strong effect; old interpretation confounded and obvious at higher abstraction |
| G22 U/K/I | **KILL AS NEXT EXPERIMENT** | K requires contrived carriers; complexity is now evidence against the question |
| Zero/nonzero anomaly | **HIGH-RISK DATA-AUDIT LEAD — NOT KEEP** | raw effect exists in parts of the data, but formal cross-model kink is inconsistent, family/skeleton heterogeneity is large, novelty is threatened |
| Explicit-outcome paradox | **HIGH-RISK / POSSIBLE SMALL PILOT ONLY AFTER NOVELTY AUDIT** | 3/3 counterintuitive direction, but current intervention is confounded and hindsight literature already says outcome-information format matters |
| Same-proposition collateral suppression | **KILL / FUTURE SIDE LEAD ONLY** | G18 does not cleanly identify source-local spillover; selective-unlearning/forget-retain separability literature strongly crowds the abstraction |
| G3 salience/backfire observations | **SUPPORTING / NO MAINLINE** | likely compressible to known salience, misinformation, ignore/backfire phenomena |
| New simple-data RQ search | **ACTIVE PRIORITY** | no current old-project anomaly has yet cleared all gates |

The most important change from V5 is:

> **There is currently no approved new mainline.**

---

# 2. Zero/nonzero: what the formal old analysis actually says

Stage 3 uses one sentence template:

> “The causal weight assigned to X is exactly W% of its normal evidential weight.”

Only W changes.

This is a good lexical control. However, the formal zero-specific temporal kink is **not stable across models**.

The fitted Stage-3 term is:

`I[w=0] × Before`

where `Before` means the weighting rule precedes the evidence.

| model | zero-specific kink | 95% CI | verdict |
|---|---:|---:|---|
| Qwen3-8B | +0.105 | [+0.018,+0.188] | positive |
| Gemma-3-12B | +0.063 | [−0.019,+0.141] | not identified |
| Mistral-Small-24B | **−0.118** | [−0.228,−0.019] | **opposite** |
| Qwen3.5-27B | +0.207 | [+0.067,+0.354] | positive |
| Qwen3-32B | −0.043 | [−0.133,+0.057] | not identified |
| Phi-4-mini | +0.119 | [−0.028,+0.288] | not identified |

Therefore the attractive sentence

> “0% creates a universal cliff across models”

is false on the repository's own formal test.

Likewise, the often-quoted:

> Qwen3-8B gap(0) / gap(1%) = 38×

is a **single-model descriptive ratio**, not a cross-model law.

---

# 3. Is the effect just a bad REI ratio? No — but that does not rescue the law

Stage 3 reports REI:

`REI = sign × (Y - base) / |evidence leverage|`

Later G17 showed that REI can become pathological when the leverage denominator is small; one G17 item produced REI ≈ 8,492. G17's preregistered ratio-based verdict therefore failed as an instrument, and a later raw-point analysis was explicitly classified as post hoc.

This creates a legitimate concern that Stage-3 zero behavior might be a ratio artifact.

To check that, V6 re-analyzed the raw Stage-3 generations using no leverage denominator. For the four common digit-rating families, define per item:

`raw_kink = sign × [(Y_0_pre − Y_0_post) − (Y_1%_pre − Y_1%_post)]`

All outputs are on the same 0–100 readout scale.

Cluster-bootstrap pooled raw kink:

| model | independent clusters | raw 0%-minus-1% temporal kink | 95% CI |
|---|---:|---:|---:|
| Qwen3-8B | 32 | +8.65 | [+2.27,+15.18] |
| Gemma-3-12B | 32 | +6.98 | [+1.97,+12.19] |
| Mistral-Small-24B | 32 | −0.39 | [−4.67,+3.25] |
| Qwen3.5-27B | 32 | +9.87 | [+3.12,+16.89] |
| Qwen3-32B | 32 | +5.11 | [+1.04,+9.52] |
| Phi-4-mini | 32 | +6.05 | [+1.75,+10.57] |

So:

- the phenomenon is **not purely an REI denominator artifact**;
- but Mistral remains a clear counterexample;
- this is still not evidence for a universal categorical zero mechanism.

The correct reading is:

> **There is a reproducible aggregate zero-vs-1% order interaction in several models on these materials, but its computational interpretation is unresolved and its generality is weak.**

---

# 4. The largest data-quality problem: family and skeleton dependence

The 144 frozen G0/Stage-3 items are not 144 independent semantic situations.

The original 180-item pool contains five manually constructed families:
- legal judgment;
- numeric aggregation;
- ranking selection;
- evidence inference;
- outcome evaluation.

The four common digit-rating families in the raw zero audit reduce to only **32 independent clusters** under the repository's own cluster definition.

Most importantly:

- `ranking_selection`: only **5** independent base-context clusters;
- `evidence_inference`: only **5** independent base-context clusters;
- `legal_judgment`: 10 case clusters, all in one criminal-trial surface domain;
- `outcome_evaluation`: 12 independent clusters in the frozen set.

Yet the visually strongest zero-vs-1% effects are concentrated in `ranking_selection` and, for some models, `evidence_inference`.

Cluster-bootstrap family effects:

### Qwen3-8B
- legal: +2.48 [−3.26,+8.25]
- ranking: **+32.15 [+24.34,+38.84]**
- inference: **+31.14 [+25.31,+38.08]**
- outcome: −5.37 [−11.15,+1.30]

### Gemma-3-12B
- legal: +3.56 [−1.10,+8.54]
- ranking: **+25.20 [+19.61,+31.61]**
- inference: **+21.24 [+8.54,+30.77]**
- outcome: −3.70 [−8.14,+1.52]

### Mistral-Small-24B
all four families are compatible with zero; outcome is negative in point estimate.

### Qwen3.5-27B
- legal: **+23.38 [+12.07,+34.56]**
- ranking/inference/outcome: not identified.

### Qwen3-32B
- legal: +6.15 [+0.61,+12.34]
- other families: not identified.

### Phi-4-mini
- ranking: **+22.35 [+16.95,+29.90]**
- other families: not identified.

This is not the structure of a mature general law.

A particularly important warning is `outcome_evaluation`: its base context already tells the model to judge the decision “using only what was knowable then.” That family therefore contains an early information-boundary instruction even before the numeric weight rule. It is structurally different from the other families and cannot be treated as just another domain replicate.

Current conclusion:

> **The old dataset is useful as discovery evidence, but it is not a sufficiently clean substrate for establishing a zero-boundary paper.**

---

# 5. The arithmetic boundary is real, but narrower than V5 implied

The separate verifiable linear-weighting task explicitly defines:

`answer = base + w × delta`

and screens items on whether a model tracks 25/50/75% retrospectively **before looking at w=0**.

Qualified item counts:
- Qwen3-8B: 13/48;
- Gemma-3-12B: 34/48;
- Phi-4-mini: 16/48;
- Mistral-Small-24B: 29/48;
- Qwen3.5-27B: 48/48.

On qualified items:
- Qwen3-8B: w=0 pre/post = 0/0;
- Gemma: 0/0;
- Mistral: 0/0;
- Qwen3.5-27B: 0/0;
- Phi-4-mini is anomalous in the opposite direction: pre=0, post≈0.438.

Qwen3.5-27B tracks every tested weight essentially exactly in both orders.

This supports a useful boundary:

> semantic evidence control is not reducible to failure to parse the number zero or execute a future scalar computation.

But it does **not** prove that semantic zero is a unique operation. The semantic materials and arithmetic materials differ in far more than “semantic vs arithmetic”, and several models have low arithmetic qualification counts.

---

# 6. Novelty assassination: the abstraction “zero is special” is already unsafe

V5 implicitly leaned toward a broad conceptual story that zero may be a special point for neural language models.

That framing is no longer available.

Zeng, Griffiths & Lake (2026), **Nothing from Something: Can a Language Model Discover 0?**, directly studies zero as a qualitatively difficult generalization boundary for transformer language models. Their task is arithmetic OOD generalization, not semantic evidence control, so it is not an exact kill. But it kills any contribution phrased as:

> “LLMs treat zero as fundamentally special.”

The only potentially defensible novelty would need to be much narrower and stronger, e.g.:

> a specific discontinuity in **causal semantic influence control** that cannot be explained by generic zero representation, scalar instruction following, negation, or evidence-weighting behavior.

The current data do not establish that.

---

# 7. Novelty assassination: graded evidence updating is already a research object

A second threat is that “models do not smoothly weight evidence according to reliability/strength” is itself not new.

Recent work on LLM confidence and advice integration compares model updates to Bayesian ideals and finds:
- systematic overweighting of contradictory advice;
- dependence on advice accuracy;
- sharp threshold-like transitions in change-of-mind behavior rather than smooth updating.

Therefore the project cannot claim novelty from:

> “LLMs integrate evidence nonlinearly.”

Nor can it claim novelty from:

> “source reliability or evidence strength does not map smoothly to influence.”

A surviving Candidate A would have to isolate a much more specific law than generic nonlinear evidence integration.

---

# 8. Candidate A revised verdict

## Research question candidate

> Is complete semantic non-use computationally distinct from arbitrarily weak use?

This remains understandable and potentially important.

## Current evidence

Mixed:
- strong raw interaction in several models;
- absent in Mistral;
- formal zero-specific kink positive in only 2/6;
- strongest family effects often come from only five independent synthetic skeletons;
- semantic fractional weights themselves are poorly followed over much of 1–50%.

## Novelty

Not killed exactly, but heavily threatened by:
- in-context forgetting/unlearning;
- negated instruction following;
- generic instruction position/dependency-order work;
- nonlinear Bayesian/advice updating;
- explicit recent work on zero as a special neural generalization boundary.

## Verdict

> **HIGH-RISK / NO PILOT AUTHORIZED YET**

Do not design mechanism experiments.  
Do not call it the new mainline.  
Do not write “zero cliff” as an established fact.

A pilot becomes justified only if continued literature search finds a clean conceptual gap **and** the pilot can be built from fresh, transparent materials with several genuinely independent semantic domains.

---

# 9. Candidate B — explicit-outcome paradox

Repository observation:

Removing explicit YES/NO verdict sentences from BTF-3 future packets increased contamination in all three models:
- Qwen3.5-9B: +7.33 points; +8.09 on leak-free subset;
- Gemma-3-12B: +6.91; +7.23 leak-free;
- Mistral-Small-24B: +2.72; +3.22 leak-free.

The packet's licensed evidential leverage remained high, so the effect is not simply “redaction removed the useful evidence.”

This is a stronger empirical anomaly than many old side results because its direction was unanticipated and 3/3 consistent.

However, the current manipulation is not clean:
- verdict presence changes packet length;
- verdict position;
- conclusion-shaped language;
- how obviously the block reads as a resolution artifact;
- 34/256 supposedly redacted packets retained outcome assertions due to an audit/redactor shared failure.

The leak-free reanalysis strengthens the effect, but does not remove the other confounds.

### Conceptual novelty threat

Human hindsight research has long shown that the magnitude of hindsight bias depends on the **type of outcome information presented**. Therefore “outcome format matters” is not a new scientific takeaway.

A future LLM paper would need a sharper law, such as:

> **explicit conclusions are more quarantinable than equally diagnostic distributed evidence.**

That exact law has not yet been established in the current search, but neither has it been cleanly demonstrated by this project.

### Verdict

> **HIGH-RISK / POSSIBLE SINGLE CLEAN PILOT, BUT ONLY AFTER A DEDICATED NOVELTY AUDIT**

It currently ranks above G22 as a discovery lead, but not above the bar for an approved mainline.

---

# 10. Candidate C — same-proposition collateral suppression

G18 shows strong below-baseline suppression when a semantic preview already states the same proposition as later evidence.

The tempting interpretation is:

> excluding the later occurrence suppresses the proposition more broadly, including an earlier allowed occurrence.

This would be a natural question:
> Can a model suppress one source/occurrence of P while preserving an allowed occurrence of the same P?

But G18 does not identify that claim cleanly:
- the preview is evidence-like;
- semantic redundancy collapses the later evidence marginal;
- “overcorrection” and source-scope failure remain confounded.

The conceptual neighborhood is also crowded:
- selective unlearning explicitly studies forget-vs-retain separation;
- EMNLP 2025 SEPS studies forget and retain queries coexisting in the same prompt and reports indiscriminate collateral forgetting for some methods;
- 2026 work studies semantically local collateral damage and forget-retain boundary problems.

Those are not the same inference-time source-occurrence manipulation, but they make a generic “selective suppression causes collateral damage” contribution too weak.

### Verdict

> **KILL AS CURRENT MAINLINE / FUTURE SIDE LEAD ONLY**

Reopen only if a simple natural experiment reveals a source-occurrence-specific law not reducible to existing forget-retain separability.

---

# 11. What the award-paper comparison actually teaches

Recent award papers reinforce a stricter standard than V5 used.

Examples:
- **Mind the Value-Action Gap**: a clear, independently important dissociation—stated values vs actions—then broad empirical characterization.
- **Measuring CoT Faithfulness by Unlearning Reasoning Steps**: one major unresolved scientific object—whether verbalized reasoning reflects parametric beliefs—plus a causal measurement framework.
- **Causal Interventions Reveal Shared Structure Across Filler-Gap Constructions**: causal analysis answers a pre-existing linguistic-theory question and reveals overlooked factors.
- ACL 2026 **The Imperfective Paradox in LLMs**: a simple linguistic contrast yields a named behavioral bias and representational/behavioral dissociation.

The important commonality is not “simple examples”.
It is:

> **the research object is important before the experiments become complicated.**

A curve where 0% happens to differ from 1% is not yet such an object.

There is also a cautionary lesson: a 2026 post-publication reanalysis of the Imperfective-Paradox benchmark argues that substantial parts of the benchmark are conceptually mis-specified. Regardless of how that debate resolves, it reinforces the present project's rule that dataset semantics are part of the scientific claim, not an implementation detail.

---

# 12. Current ranking of old-project leads

1. **No approved mainline.**
2. **Explicit-outcome paradox** — empirically counterintuitive, but needs conceptual novelty audit before even one pilot.
3. **Zero/nonzero anomaly** — interesting but more heterogeneous and more literature-threatened than V5 recognized.
4. **G0** — strong foundational asset, not safe paper identity.
5. **G18** — supporting mechanism/behavior asset.
6. **Same-proposition spillover / G21-like scope** — not current priority.
7. **G22** — do not run.

This ranking is intentionally conservative.

---

# 13. What should happen before any new generation

## A. Complete novelty assassination for the two surviving anomalies

### Zero/nonzero
Search not only exact wording but:
- graded evidence integration;
- advice weighting and source reliability;
- nonlinear confidence updating;
- abstention / hard gating;
- negated constraints;
- selective forgetting;
- zero-boundary cognition and neural OOD generalization.

### Explicit outcome
Search:
- hindsight/outcome bias moderators;
- explicit vs implicit outcome information;
- conclusion-vs-evidence representations;
- labels vs distributed evidence;
- epistemic vigilance and discourse structure;
- salience / marking effects.

## B. Continue simple-data RQ search independently of old anomalies

Do not force the next paper to inherit “ignore evidence”.

## C. For any surviving candidate, run the six-field candidate audit

1. one-sentence RQ;
2. one example;
3. 2–4-cell minimal dataset;
4. direct gold;
5. 3–10 closest works and reviewer-compression test;
6. C1→C2→C3 growth path.

## D. Only then design a 50–300-item discovery pilot

No mechanism first.
No 12-model breadth first.
No rescue experiments.

---

# 14. Current project statement

The correct project state after V6 is:

> **We have several valuable old empirical anomalies, but none has yet earned the right to become the new paper.**

The next success criterion is not “find a significant effect”.

It is:

> **find a simple research object whose importance survives abstraction, whose novelty survives an adversarial literature search, and whose first clean dataset does not need interpretation gymnastics.**
