# Claude project instructions

This is the default project context for Claude Code.

## Read these first

1. `PAPER_FRAME.md` — the authoritative scientific story.
2. `ACL_EMNLP_ALIGNMENT_STANDARD.md` — what we mean by aligning to strong
   ACL/EMNLP/NAACL Main and Outstanding papers.
3. `EXPERIMENTS.md` — concise registry of all experimental rounds.
4. `RESEARCH_HISTORY.md` — how the question moved, and why it moved back.
5. `PAPER_OUTLINE.md` — current paper narrative and figures.
6. `RELATED_WORK_2026.md` — conceptual neighbours and positive positioning.

Full main-line results are in `PROSPECTIVE_EXCLUSION_FINDINGS.md` and `stages/`.
For exact frozen experimental details, use `preregistrations/`. Dead research
branches live in `archive/` and must not override the current frame.

## Scientific objective

The paper asks one natural question:

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

The scientific object is **whether a stated exclusion policy actually governs the
decision**, and what determines when it does.

Do not replace this with technical meta-language. `Prospective binding failure` is
the mechanism's name and belongs in methods and analysis, never in the title or
introduction. Terms from the abandoned frames — `information set`, `out-of-set
intrusion`, `retrospective outcome entrainment`, `recipient-conditioned decision
state` — do not belong in this paper at all.

The positive explanatory chain is:

1. exclusion stated after the evidence is followed well; the identical exclusion
   stated before it is not — the reverse of the human pattern — while the model
   states the required weight as exactly zero on 100% of items in both arms;
2. it is not memory, not distance, not the causal attention mask, not one wording,
   and not inclusion implicature;
3. the failure is specific to driving a contribution to exactly zero, and vanishes
   when that contribution is arithmetically implementable;
4. what decides it is what the policy can bind to — a named future referent fails
   and is worse than saying nothing, while propositional content and class markers
   carried on the evidence succeed;
5. the same dissociation appears in an agent, where a `SYSTEM` identifier policy is
   worth nothing and suppression follows the proposition, not the document ID;
6. the excluded evidence is still read at the decision, gating is resolved late, and
   the binding state is causally exchangeable.

## What was stopped, and what must not be restarted

The BTF-3 hindsight paper was stopped on 2026-09-03. Its data and verdicts are
retained for provenance (`EXPERIMENTS.md` §C). Do not restart it, do not rewrite it,
and do not import its vocabulary into the current paper.

Specifically, **do not**:

- run the remaining 12 checkpoints of the preregistered G4 breadth panel;
- add frontier or reasoning models to a stopped branch;
- run further hindsight mechanism rounds;
- repair the frozen verdict redactor and re-run it. Its defect is disclosed in
  `preregistrations/POSTHOC_REDACTION_AUDIT_CORRECTION.md`; repairing a frozen
  instrument after seeing its outputs would convert a disclosed defect into an
  undisclosed one.

The one hindsight result worth keeping is held separately in
`SECOND_LEAD_EXPLICIT_OUTCOME_PARADOX.md`, with the single clean experiment that
would confirm or kill it. It is not scheduled and it is not part of this paper.

## Research style: no defense-first science

This project must not become a catalogue of reviewer objections.

Do **not** add experiments because "a reviewer might ask for another model / prompt /
benchmark / control / mitigation." Do not organise the paper as a sequence of
"not X, not Y, not Z." Strong ACL/EMNLP papers establish a natural phenomenon and
then descend through positive explanatory questions.

The main text should read:

> **question → phenomenon → sharper regularity → causal test → mechanism**

Section 3 of the paper does rule out four accounts, and that is legitimate because
each was run to discriminate between live explanations and each predicts a different
result. Ruling something out to pre-empt a reviewer is not the same activity.

More models is not more rigour. The behavioural breadth here — 12 instruct models,
4 vendors, 2 architectures, 5 task families — is already unusual; the missing piece
is never coverage, it is whether the mechanism explains the headline.

The default is **no new experiment**. The only planned one is
`preregistrations/PREREGISTRATION_G16_BINDING_INTERCHANGE.md`, and it must be
committed and tagged before any generation. If a genuinely new scientific question
emerges, formulate it first and only then decide whether an experiment is needed.

## Evidence discipline

- Preserve the real chronology, including the reversed original prediction, the
  detour into hindsight, and the return.
- Original preregistrations are preserved unchanged in `preregistrations/`; their
  freeze commits and tags remain the authority for chronology.
- Report the actual continuous results. Frozen thresholds are experiment
  bookkeeping, not the conceptual vocabulary of the paper.
- In-round corrections (the duplicate-control confound, the REI → rating-points
  metric change, the Stage-5 recovery-fraction withdrawal, the redaction-audit and
  Llama-scope corrections) stay visible. They are what makes the rest credible.
- Never report a number at one measurement scope alongside another number at a
  different scope. That is what produced the withdrawn "97.7–100%" panel figure.
- Mechanistic conclusions are Qwen3-8B-specific unless separately established.
- The 144-item vignette set is the instrument, not the identity of the question.

## Environment policy

Prefer the existing local project virtual/conda environment and existing shared
caches. First inspect and try the current environment. Create a new environment only
for a genuine incompatible CUDA/PyTorch/package-version conflict; document the
reason and keep the replacement minimal.

## GPU policy

Usable compute nodes when cards are actually idle: `fvcrc10`, `fvcrc11`, `fvcrc12`,
`fvcrc13`, `fvcrc15`, `fvcrc20`, `fvcrc21`.

Check occupancy before launching and use idle cards only. During daytime, avoid
occupying more than **8 GPUs total at once** unless the user explicitly overrides
this. Prefer compatible existing nodes/environments and be mindful of shared
NFS/checkpoint-loading bottlenecks.

## Git policy

Completed research/documentation changes should land directly on `main`. Keep
commits coherent and descriptive. Preserve scientific provenance when consolidating
old files: current narrative lives at the root, main-line stage records in `stages/`,
original preregistrations in `preregistrations/`, and dead research branches in
`archive/`.
