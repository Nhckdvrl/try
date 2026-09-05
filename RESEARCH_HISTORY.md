# Research history — how the question moved, and why it moved back

This file preserves **why the question changed**, including the part where we
changed it away from a good result and later changed it back. It is not the paper
narrative and does not replace the original preregistrations in
[`preregistrations/`](preregistrations/).

## 1. Starting question — advance exclusion

The project began from the human literature on inadmissible evidence: a
meta-analysis over 48 studies and 8,474 participants finds that people told to
disregard evidence they have already heard retain its influence.

G0 preregistered the same ordering for models: exclusion **after** the evidence
would be the hard case.

**The result reversed.** Across twelve instruct models from four vendors, exclusion
after the evidence was followed well; the identical rule stated *before* it was
not. `Δ_time` was negative in all twelve models.

Two things made the reversal a finding rather than a failure. The separate probe
recovers the intended zero-weight policy at ceiling, while later trajectory-level
rounds show that explicit policy access and decision-time enforcement can dissociate
in Qwen/Gemma. And the asymmetry survives in bidirectional masked diffusion models,
so a left-to-right causal prompt mask is not necessary.

## 2. The controlled programme that followed

Stages 2–5 did not add controls to defend the reversal; they tried to say what it
was. In order:

- **distance** — no main effect; within the prospective arm, more distance helps;
- **directional anaphora** — stripping every `preceding`/`following` referent
  shrinks the effect but leaves it significant in 3 of 4 models;
- **requested weight** — the asymmetry exists only at exactly zero, pooled
  discontinuity **+0.295 [+0.185, +0.405]**;
- **an arithmetically implementable task** — the discontinuity disappears entirely,
  which bounds the claim;
- **inclusion implicature** — explicitly denying that display implies relevance
  rescues no model;
- **the announcement ladder** — naming a future item makes suppression *worse* than
  never mentioning it, uniformly across six models;
- **semantic addressability** — the rule binds to propositional content, graded by
  entailment, not by lexical overlap;
- **a duplicate control** — which found a real confound in the previous step, and
  forced the metric from REI to raw rating points;
- **class/tag policies** — a marker travelling with the evidence takes stream
  leakage from 0.48 to ≈0 in both arms;
- **an agent setting** — the same dissociation with real `SYSTEM`/`TOOL` roles;
- **mechanism** — span gating, late answer-position patching, and matched-chronology
  bidirectional interchange, including a correction that withdrew an earlier
  overstated recovery-fraction analysis.

At this point the line had a natural question, a reversed prediction, five
discriminating explanations, a working structural fix, and a mechanism.

## 3. Why we left it anyway

The concern was that the work was tied to a synthetic prompt grammar — "a future
item receives weight zero" — and that the materials were authored vignettes rather
than natural text. That concern was real, but the response was too large: instead
of naturalising the materials, the project changed the question.

## 4. The detour — Information-Set Reasoning, then hindsight

The question was generalised to "can a model reason using only the information that
belongs to a specified situation." Several boundary families were tried. The
temporal BTF-3 branch qualified; the FANToM perspective branch did not; a later
FOMC source attempt failed its gate.

The surviving temporal branch was reframed as **hindsight**: given a resolved
forecasting question and its resolution packet, can the model still judge the
earlier situation? That produced a real programme — an 8-item discovery, a 64-item
prospective confirmation, a 256-item fresh replication, foreign-packet and
verdict-redaction decompositions, a paired outcome-direction intervention, and a
three-round mechanistic sequence ending in a fresh preregistered confirmation.

## 5. Why the hindsight paper was stopped on 2026-09-03

Reviewed against the reference papers and the 2025–2026 literature, the branch had
three problems that were not fixable by rewriting:

1. **The instrument stopped matching the question.** The prompts are explicit
   information-set contracts — `TARGET INFORMATION SET`, `LATER RESOLUTION PACKET`,
   `date_cutoff_end=…` — and the boundary probe's answer is stated verbatim in the
   prompt it probes. What is measured is compliance with an engineered exclusion
   contract, not hindsight.
2. **The headline was covered.** ExAnte and the temporal-leakage line already
   establish that models violate stated cutoffs; work on auxiliary-information bias
   and on prompting models to ignore biasing information already reports failure and
   backfire. The genuinely new material sat in the middle of the paper.
3. **The panel narrowed under its results.** The original Qwen/Gemma/Mistral G12
   verdict is `indeterminate`; Llama was added afterwards and the three
   largest-effect models were labelled canonical in the same commit that added the
   Llama numbers, with the one model that fully passes the recognition check moved
   to an appendix. That is exactly the failure mode this project set out to avoid.

Two data-integrity defects were found in the same review and are corrected in
[`preregistrations/POSTHOC_REDACTION_AUDIT_CORRECTION.md`](preregistrations/POSTHOC_REDACTION_AUDIT_CORRECTION.md):
the redactor's conditional-marker bypass leaves 34/256 packets asserting the
outcome, and the frozen audit could not detect it because it used the same
heuristic; and the Llama boundary-probe figure was reported at single-frame scope
alongside other models' two-frame scope. Neither changes a preregistered verdict,
and both are now on the record.

## 6. What the detour produced that survives

- **One strong unconfirmed discovery.** Removing the explicit verdict sentence
  makes contamination *larger*, in all three models, without reducing the packet's
  evidential value. It is preserved as a separate lead in
  [`SECOND_LEAD_EXPLICIT_OUTCOME_PARADOX.md`](SECOND_LEAD_EXPLICIT_OUTCOME_PARADOX.md)
  with the single clean experiment that would confirm or kill it.
- **A methodological lesson that transfers.** The `outcome_evaluation` family in the
  original G0 items is the one family with order-*independent* residue — ordinary
  outcome bias, behaving like the human effect rather than like the positional one.
  The hindsight branch was, in retrospect, an eighteen-round expansion of that one
  family.
- **Provenance discipline.** Freeze tags, artifact hashes, human review gates and
  post-result corrections that the main line now inherits.

## 7. Current paper

The project has returned to the question it started with, without the human
analogy in the title and without the original prediction:

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

```text
advance exclusion fails where post-hoc exclusion succeeds,
while the model states the policy perfectly
        ↓
not memory, distance, causal masking, wording, or implicature
        ↓
the failure is specific to complete suppression
        ↓
what the policy can bind to decides it — content and
evidence-carried class markers work, named future items do not
        ↓
the same dissociation in an agent
        ↓
excluded evidence is still read at the decision; gating is late
and the binding state is causally exchangeable
```

The history explains how we found this, lost it, and came back. It should not
dictate the structure of the paper.


## 8. Novelty reset on 2026-09-04

After G18 prospectively confirmed the semantic-target effect, the project briefly
converged on "target addressability" as the paper's explanatory novelty and designed a
post-retrieval ReGround mitigation.

A second literature/narrative audit rejected that frame.

The problem was not empirical weakness. G18 is clean and strong. The problem was that
the headline could be compressed to a normal statement:

> if the model knows more specifically what future evidence it must ignore, the rule is
> easier to apply.

That is too close to instruction specificity and identify-then-ignore methods to carry
an Outstanding-shaped phenomenon paper. ReGround had the same issue at method level:
resolving the policy after retrieval and explicitly marking the matched document is a
reasonable system design, but too obvious as a new scientific contribution.

ReGround G19 was therefore **cancelled before freeze and before any generation**.

The audit re-read the odd parts of G18 and Stage 5 instead of trying to defend the old
story. Two stronger hypotheses emerged:

1. **Binding Deadline / Late Target Revelation.** The crucial variable may be whether
   target semantics exist **when the rule is processed**, not whether they exist
   somewhere before the final decision. Stage 5 already shows a causal target-dependent
   state at the rule span before later evidence is processed. G20 will move the same
   semantic target block across the fixed rule and test whether replaying the rule after
   late target revelation repairs the failure.
2. **Semantic Scope Collapse / Spillover.** G18's semantic condition drives judgments
   below the preview-only baseline, and semantic policies follow propositions across
   document identifiers. This may mean successful exclusion loses source/occurrence
   precision. G21 will exclude Source A while explicitly preserving independent Source
   B and ask whether B loses evidential weight only when it expresses the same
   proposition.

The new candidate abstraction is a **binding–scope trade-off**:

- unresolved target at rule time → **under-binding** and leakage;
- strong semantic binding → possible **over-binding** across provenance boundaries.

The current question is therefore not merely whether models can decide what to ignore,
but whether they can establish a future control relation that is both **effective and
precisely scoped**.


## 9. Second mainline audit later on 2026-09-04

The scope branch was then audited against the original paper question rather than only
against novelty.

That audit changed the priority again.

G21 Source–Proposition Scope Entanglement remains scientifically interesting, but it
does not naturally explain why the same exclusion rule is weaker before evidence than
after evidence. It asks a new question about the precision of successful semantic
control. For that reason it was **downgraded from the paper center before generation**.

The original G0 reversal was re-read directly as a change in composition order:

```
retrospective: target → EXCLUDE
prospective:   EXCLUDE → target
```

This made G18 fit the original paper more cleanly. Its semantic preview restores:

```
target semantics → EXCLUDE → later evidence
```

without moving the actual evidence used by the decision.

The new mainline hypothesis is therefore **deferred control composition**:

> when processing an exclusion rule, the model may construct a target-conditioned
> control state from whatever target representation already exists, rather than store a
> deferred exclusion operator that is reliably composed with a target later.

G20 was redesigned around a shared post-resolution checkpoint. TARGET-FIRST and
RULE-FIRST conditions contain the same target, rule, and neutral material by that
checkpoint, so both can in principle integrate all required information. The key test is
whether the histories nevertheless retain different causal control states, and whether
replaying the exclusion operator after late target resolution selectively repairs the
RULE-FIRST condition.

This redesign is intended to avoid the trivial decoder causal-mask explanation and keep
every main experiment on the original pre-commitment question.

The current authoritative audit is:
[MAINLINE_AUDIT_2026-09-04_V2.md](MAINLINE_AUDIT_2026-09-04_V2.md).


## 10. Third mainline audit — target knowledge vs evidential instantiation

A deeper audit of the actual prompts and raw condition structure found that the
second-reset “non-commutative exclusion” story was still one step too fast.

The key correction came from re-reading G18 itself.

Its semantic `para/entail` previews do not merely identify what a future evidence item
will mean. They substantively assert almost the same proposition as the later evidence.
This is visible behaviorally: under semantic previews, the later evidence's no-rule
marginal falls from roughly 32 rating points to roughly 3.

Therefore G18 had mixed two variables:

1. **target knowledge** — the model knows exactly what future evidence will say;
2. **evidential instantiation** — the same proposition has already entered the
   judgment as substantive information.

That distinction had never been cleanly tested.

The audit also found a second interpretive gap in Stage 3B. Tagged
`[verified]/[unverified]` routing succeeds prospectively, but the no-policy control
removes the labels themselves. Thus the experiment cannot distinguish standing-policy
execution from local semantic discounting caused by the `[unverified]` label.

These corrections changed experiment priority again:

- G21 remains downgraded because it does not explain G0.
- G20 remains a serious conditional hypothesis, but is no longer the authorized next
  experiment because its latest P/U swap still mixes target state and distance.
- G18 remains a strong prospectively confirmed diagnostic but no longer licenses
  “non-evidential future target semantics are sufficient.”
- Stage 3B remains a successful routing result but no longer licenses “standing tagged
  policies prove prospective gating works.”

The project registered a new design-audit candidate:

### G22 — Target Knowledge vs Evidential Instantiation

The intended factorization is:

```
U: unresolved future target
K: future target semantics exactly known but explicitly non-evidential
I: the same proposition already instantiated as evidence
```

The critical scientific requirement is that K be genuinely judgment-neutral. If a
clean K carrier cannot be constructed, the experiment must not run.

The branch logic is intentionally falsifiable:

- if K rescues exclusion, proceed to clean early-vs-late target mapping and deferred
  composition;
- if only I rescues, investigate retrospective evidence-state revision/cancellation;
- if neither cleanly separates, reassess rather than promote a side phenomenon.

A small D22-A routing diagnostic was also registered to distinguish standing-policy
execution from local semantic label effects. It is explicitly supporting-only.

The current authoritative ledger is:
[SCIENTIFIC_REGISTER_2026-09-04_V3.md](SCIENTIFIC_REGISTER_2026-09-04_V3.md).

No new generation was performed during this audit.


---

## 11. 2026-09-06 adversarial mainline reconstruction — V5 → V8

The G22 branch was subsequently stopped **before generation**.

The reason was not that its U/K/I distinction was logically incoherent. The problem
was methodological and scientific: constructing the crucial K state increasingly
required retrieval manifests, future-record specifications, non-evidential carriers,
interface/schema metadata, and explicit neutrality checks. The experiment had begun to
manufacture an unnatural world in order to identify a latent factor.

This triggered a broader reset:

> **Do not manufacture novelty by making the experiment more elaborate. Find a
> simple research object whose importance survives abstraction.**

### V5 — premature promotion of the zero/nonzero anomaly

A first simple-data audit noticed the old Stage-3 observation that order sensitivity
appeared concentrated at requested weight 0 and temporarily promoted:

> exact semantic non-use may be qualitatively different from arbitrarily weak use.

That promotion was too fast and is retained as an explicit research-judgment error.

### V6 — adversarial correction

A deeper audit re-read:
- the formal zero-specific interaction;
- raw generations without the unstable REI denominator;
- independent semantic skeleton counts;
- task-family heterogeneity;
- the arithmetic control;
- current 2024–2026 novelty threats.

The formal zero-specific law was not cross-model stable: only 2/6 models had a
significant positive zero-specific term, Mistral showed a significant reverse effect,
and the strongest descriptive effects concentrated in small task families.

The correct project state became:

> **no approved new mainline.**

G22 was killed as the next experiment. Zero became a high-risk anomaly rather than a
law. The explicit-outcome redaction paradox remained a high-risk anomaly.

### V7 — old-anomaly audit plus independent simple-data search

V7 tightened the decision further:
- zero/nonzero was **killed as a paper identity** and retained only as an archived
  empirical anomaly;
- the stopped BTF3 G12→G15 chain was explicitly recovered as a real mechanistic asset:
  in Gemma, an unrelated verdict-redacted future packet's outcome direction is
  transformed into a recipient-conditioned late decision coordinate with fresh causal
  confirmation;
- that mechanism was **not** promoted to a mainline because the behavioral effect is
  heterogeneous across Qwen/Gemma/Mistral and neighboring work on irrelevant-context
  interference, anchoring, and shared decision subspaces crowds the abstraction.

V7 also started a formal kill ledger for simple-data RQs. Multiple natural-looking
candidates were killed before any model run because current literature already occupied
their conceptual takeaway.

Its strongest temporary search shape — conditioning evidential value on the sampling /
observation process — was deliberately left PRE-PILOT.

### V8 — sampling killed; common-knowledge intersection remains only high-risk

Further 2026 search then killed V7's sampling-process candidate:
- CROWN-QA directly studies when absence can support a negative conclusion as a
  function of evidence completeness / coverage;
- 2026 hypothesis-updating work directly studies LLM sampling assumptions and reports
  strong-sampling bias;
- generic Bayesian belief updating is already heavily occupied.

The same kill-first search removed additional broad candidates around:
- source reliability / undercutting;
- conflict vs ignorance;
- value of information;
- disjunctive / set-valued uncertainty;
- joint commitment;
- pluralistic ignorance;
- informational cascades / herding;
- collective/distributive plurality;
- screening-off;
- reversible vs irreversible action / preserving optionality.

The only new shape surviving the current round is an intersection around **publicness
and common-knowledge closure**:

> when first-order factual knowledge is matched, does public observability induce a
> qualitatively distinct shortcut to recursive epistemic closure in LLMs, separable
> from ordinary finite-depth Theory-of-Mind reasoning?

Even this candidate is **not approved**.

Exact threat search found:
- MindGames (EMNLP Findings 2023) already uses S5/public-announcement logic and
  higher-order belief queries;
- a 2026 Knowledge-Based Systems benchmark already evaluates LLMs on Muddy Children
  and Cheryl's Birthday dynamic epistemic puzzles;
- OmniToM already labels Private / Shared / Public knowledge access;
- SimpleToM (ICLR 2026) already establishes an explicit-ToM → applied-ToM gap;
- common-ground and LLM-coordination literatures are substantial.

Therefore all generic claims about public/private knowledge, public announcements,
higher-order ToM, common-ground ability, or explicit-vs-applied ToM are unavailable.

The candidate remains alive only as:

> **HIGH-RISK INTERSECTION LEAD: publicness shortcut vs finite recursive mentalizing.**

No target-model generation has been authorized.

Current authority:
[MAINLINE_AUDIT_2026-09-06_V8.md](MAINLINE_AUDIT_2026-09-06_V8.md).

The project culture after these corrections is:

> **A classic distinction is allowed; a classic conclusion is not.**

and:

> **simple question → conceptual novelty assassination → scale/growth-path test →
> only then a tiny discovery pilot.**
