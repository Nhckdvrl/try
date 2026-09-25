# G24A wider novelty search (v1, 2026-09-25): scope-locked arXiv sweep

Closes the "wider search with narrowed scope still required before any freeze" item
from `g24a_competing_accounts_v1.md` §5/§8 **at arXiv coverage** (method + limits in §1).
Discovery documentation only — this file creates **no RQ declaration, no prereg, no
gates, no claims beyond the registered scope discipline**.

## 0. Scope under test (verbatim discipline from §8)

Target of the search: *counterfactual correctness of evidence-control operators* — a
specific evidence already admitted into context that already changed a judgment,
removed by a natural-language ruling, scored by counterfactual correctness (restoring
the exact no-evidence judgment), with residual / overshoot / polarity-dependent
distortion as the claimable phenomena.

Explicitly **not** claimed: parametric knowledge deletion; optimized forget scores;
packaging as prompt unlearning; "first to observe retracted information still
influences reasoning"; first anything about human continued-influence.

A hypothetical **direct owner** had to satisfy all three:
(i) object = natural-language evidence-control operator (admit/exclude/strong-exclude/
counterfactual-delete) over **already-observed in-context evidence**, prompting-only;
(ii) criterion = **restoration to a shared evidence-free baseline Y0 of the same item**
(after the model has already integrated E), not dependence, not refusal, not flip-rate;
(iii) estimands decompose residual vs overshoot **and polarity** (support vs refute).

## 1. Method and coverage limits

- **Tooling**: the websearch integration was unavailable (three consecutive
  cancellations); fallback = arXiv REST API (`export.arxiv.org/api/query`), full
  all-fields metadata search (title + abstract + indexed fields), exact-phrase and
  conjunction queries, results screened by title+abstract.
- **Date**: all queries executed 2026-09-25, sorted by submission date (desc) unless
  relevance sorting is noted.
- **Query count**: 19 (ladder in §2).
- **Limits (residual risk, stated honestly)**: arXiv metadata only — not ACL Anthology,
  Google Scholar, Semantic Scholar, PsychINFO (human CIE literature), or full body
  text of arXiv papers; a phrase used only inside body text can be missed. CAP
  (ACL 2026), Findings ACL 2025 in-context unlearning, and EMNLP 2025 misinformation
  correction were identified in the earlier user-run passes (§5/§8) and are retained
  as registered; this pass neither re-derives nor weakens them. A non-arXiv venue
  sweep remains open as residual coverage before any freeze (status, not a gate).

## 2. Query ladder and outcomes

| # | arXiv query (all-fields) | Hits | Screened outcome |
|---|---|---:|---|
| 1 | `all:"evidence retraction" AND all:"language model"` | 0 | clean null |
| 2 | `all:"belief revision" AND all:"large language model"` | 12 | all prospective updating (Belief-R 2406.19764; MEDLEY-BENCH 2604.16009; DeReLab 2608.30413) — no deletion-to-baseline |
| 3 | `all:"in-context knowledge unlearning"` | 1 | = Takashiro et al. 2410.00382 (registered neighbor) |
| 4 | `all:"retracted" AND all:"language models"` | 39 | neighbors: SciUnlearn claim-level unlearning 2608.20960; retraction-status knowledge 2604.16872; TRACES 2608.11415; GPM non-revival 2608.12476 — none is operator counterfactual correctness |
| 5 | `all:"continued influence" AND all:"language model"` | 2 | both irrelevant (phrase variants) |
| 6 | `all:"prompt unlearning" AND all:"language model"` | 1 | = 2410.00382 again |
| 7 | `all:"evidence" AND all:"exclude" AND all:"instruction" AND all:"language models"` | 2 | irrelevant (gait retrieval etc.) |
| 8 | `all:"misinformation correction" AND all:"language model"` | 4 | note-generation/prompt-framing neighbors; surfaced RePAIR/IMU 2604.12820 (NL forget instruction at inference, activation steering) |
| 9 | `all:"belief perseverance" OR all:"belief persistence"` | 2 | non-LLM opinion dynamics only (2409.12933, 2407.01820) |
| 10 | `all:"disconfirming evidence" AND all:"language models"` | 3 | prospective (DeReLab; overseer criterion 2609.18204) |
| 11 | `all:"in-context unlearning"` | 3 | MLLM/training-free unlearning citations (2606.00105) — parametric targets |
| 12 | `all:"evidence leakage"` | 0 | clean null (our RQ1 phrasing owns no arXiv competitor) |
| 13 | `all:"counterfactual" AND all:"in-context" AND all:"evidence"` (relevance-sorted of 94) | 94 | screened top set: MedCounterFact 2601.11886; in-context counterfactual emergence 2506.05188; AML counterfactual checks 2604.19755; RAGONITE 2412.10571; audio counterfactual audits 2608.06718; CofCA/CRiT-QA (counterfactual entities vs memory); verifier evidence-removal dependence 2604.09537 — none restores to a pre-observation Y0 |
| 14 | `all:"counterfactual deletion"` | 3 | audio explanation faithfulness 2609.12663; recommender/PDE — mechanical ablation, not instruction |
| 15 | `all:"continued influence effect"` | 0 | clean null: phrase absent from arXiv (human CIE lives off-arXiv) |
| 16 | `all:"retraction" AND all:"belief" AND all:"language"` | 5 | self-retraction of own outputs (Yang & Jia 2505.16170, CoLM 2026); P-StaT belief stability 2511.19166; gaslighting belief reversal 2604.17873; DeReLab |
| 17 | `all:"retraction instruction" OR all:"retract the evidence"` | 1 | irrelevant (VB on manifolds) — operator phrasing owns nothing |
| 18 | `all:"evidence removal" AND all:"language models"` | 4 | ablation-as-dependence (MemLens 2605.14906; CulturalMenuBench 2609.03526) or preprocessing (CARE-RAG 2507.01281; CICL) |
| 19 | `all:"disregard the evidence" OR all:"ignore the evidence"` | 21 | nearest compliance relative: **WhatIfVis 2607.26326** — "even when explicitly instructed to use or ignore visual evidence … unstable context sensitivity" (visual modality, capability metrics, no sequential E→admit→ruling order, no Y0); also context-vs-memory grounding 2609.00925; MCR-BENCH 2508.15407 |

## 3. Neighbor taxonomy (why each is adjacent but not the owner)

**A. Prompt / in-context unlearning (training-requiring)**
- Takashiro et al., *Answer When Needed, Forget When Not* (2410.00382, Findings ACL
  2025): fine-tunes LLMs for test-time prompt unlearning of **trained** knowledge;
  their own framing: "pretend to forget". Not (i): parametric target + training; not
  (ii): evaluated by forget-utility scores, not restoration to a pre-observation
  judgment.
- CAP (ACL 2026, §8): RL-optimized prompts suppress knowledge that **recovers after
  prompt removal** — fragility of prompt suppression. Not (i): optimized prompts over
  parametric knowledge.
- RePAIR/IMU (2604.12820): natural-language forget instruction at inference time,
  implemented by **activation steering** (STAMP) over trained misinformation/harmful
  data; criterion = forget score. Closest to "NL instruction to forget" wording, but
  intervention is parametric, target is trained knowledge, no Y0, no polarity.
- SciUnlearn (2608.20960, EMNLP 2026): training-time unlearning of scientific
  claims; diagnoses "superficial suppression". Not prompting-only, not in-context
  evidence.

**B. Evidence ablation as explanation / dependence test (mechanical deletion)**
- RAGONITE counterfactual attribution (2412.10571, WSDM 2025): answer similarity
  with vs without a retrieved passage — an **explanation** method.
- Case-grounded verifier (2604.09537): "collapses when evidence is removed …
  indicating genuine evidence dependence".
- STAG audio counterfactual deletion (2609.12663); MemLens/CulturalMenuBench image
  ablations (2605.14906, 2609.03526).
- **Discriminating axis**: their ideal is **dependence** — removing evidence *should*
  move the output (removal = diagnostic intervention on the input, tokens physically
  gone, judged vs the with-evidence answer). Our ideal is **restoration** — a
  natural-language ruling issued *after* the model observed E and produced Y_admit
  should return Y to the same item's shared evidence-free Y0; movement is the failure
  mode, decomposed by polarity into residual vs overshoot. Opposite sign of the
  desideratum, different execution order, different baseline.

**C. Prospective belief updating (new evidence arrives)**
- Belief-R (2406.19764), DeReLab (2608.30413, EMNLP 2026: accepts congruent
  evidence, resists incongruent updates; "correctly identifies a weakening update yet
  fails to revise"), MEDLEY-BENCH (2604.16009).
- **Discriminating axis**: E arrives and should be integrated (or is resisted) —
  forward direction. DeReLab's failure-to-revise is conceptually kin to *residual*
  but occurs at update time, not after retrospective exclusion, and has no
  no-evidence counterfactual to restore.

**D. Counterfactual evidence acceptance (prospective, single shot)**
- MedCounterFact (2601.11886, Findings ACL 2026): models accept counterfactual /
  adversarial medical evidence at face value ("overly faithful"). What the model does
  when fake E is *presented* — no removal, no baseline, no polarity decomposition.
  Must be cited: it owns "acceptance of injected counterfactual evidence"; we own
  "restoration failure after removal of real evidence".

**E. Instructed use/ignore compliance (visual modality)**
- WhatIfVis (2607.26326): explicit "use or ignore visual evidence" instructions yield
  unstable context sensitivity; SFT and steering vectors improve controllability.
  **Discriminating axis**: capability/controllability framing on images, static
  instruction, no sequential admit-then-exclude design, no Y0, no polarity — but it
  is the closest *compliance-framing* relative and must be positively addressed:
  instruction-driven evidence-disregard instability has been measured for vision;
  our object is text evidence + counterfactual-correctness criterion + overshoot.

**F. "Retraction" of the model's own statements**
- Yang & Jia (2505.16170, CoLM 2026): spontaneous retraction of the model's own
  wrong answers, predicted by momentary-belief probes (mechanistic). Different
  retraction object (own output vs provided evidence), different question (when does
  it self-correct vs does exclusion restore the counterfactual).
- P-StaT (2511.19166): "belief retraction rates" under semantic reframing of
  statements (fictional vs synthetic) — stability measurement, no evidence channel.

**G. Context-vs-memory grounding / conflict**
- 2609.00925: models can ignore prompt evidence conflicting with memorized
  knowledge; post-training shares causal machinery with the starting checkpoint.
- MCR-BENCH (2508.15407, EMNLP 2025): text bias — disregards audio evidence.
- **Discriminating axis**: which source wins when both are present (use-vs-ignore
  balance); our operators issue an explicit ruling and we score the post-ruling
  judgment against Y0.

**H. Registered §5/§8 neighbors (unchanged, positively addressed)**
- Human continued influence effect (off-arXiv; exact phrase = 0 on arXiv):
  retracted misinformation keeps influencing *human* judgment — we claim LLM
  operator counterfactual correctness, not the persistence phenomenon itself.
- EMNLP 2025 misinformation correction: correction text at generation time, not
  operator-level restoration to a pre-evidence baseline.

## 4. Clean nulls (phrasings that own nothing)

`"evidence retraction"+"language model"` 0; `"continued influence effect"` 0;
`"evidence leakage"` 0; `"retraction instruction"`/`"retract the evidence"` → 0
relevant; `"prompt unlearning"`/`"in-context knowledge unlearning"` → single hit each
(= 2410.00382); `"belief perseverance"|"belief persistence"` → no LLM paper;
`"evidence"+"exclude"+"instruction"+"language models"` → no relevant hit.

## 5. Verdict

**SERIOUS maintained; no direct owner found at arXiv metadata coverage (19 queries).**
No paper found that (i) evaluates natural-language evidence-control operators over
already-observed evidence, prompting-only, (ii) against restoration to the same
item's shared evidence-free baseline, (iii) with polarity-decomposed residual/overshoot
estimands. The registered claim target stands: *evidence-control operators exhibit
residual, overshoot, and polarity-dependent distortion — removal ≠ counterfactual
deletion* (support-side over-correction included).

New citations to positively address in any related-work section (found this pass):
MedCounterFact 2601.11886; WhatIfVis 2607.26326; Yang & Jia 2505.16170;
P-StaT 2511.19166; RAGONITE 2412.10571; evidence-removal dependence 2604.09537;
RePAIR/IMU 2604.12820; SciUnlearn 2608.20960; DeReLab 2608.30413; grounding-vs-memory
2609.00925 — plus the four registered §8 neighbors (CAP, in-context unlearning,
misinformation correction, human CIE).

**Residual coverage (status, not a gate)**: non-arXiv venue sweep (ACL Anthology /
Google Scholar / Semantic Scholar; body-text-only phrasings) remains open per §1
limits before any freeze. No RQ declaration, no prereg, no gate is created here.
