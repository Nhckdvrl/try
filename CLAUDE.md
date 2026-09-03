# Claude project instructions

This is the default project context for Claude Code.

## Read these first

1. `PAPER_FRAME.md` — the authoritative scientific story.
2. `ACL_EMNLP_ALIGNMENT_STANDARD.md` — what we mean by aligning to strong ACL/EMNLP/NAACL Main and Outstanding papers.
3. `EXPERIMENTS.md` — one consolidated registry of all experimental rounds and preregistration history.
4. `RESEARCH_HISTORY.md` — how *Unring the Bell* evolved into the current hindsight paper.
5. `PAPER_OUTLINE.md` — current paper narrative and figures.
6. `RELATED_WORK_2026.md` — conceptual neighbours and positive positioning.

## Scientific objective

The paper asks one natural question:

> **After a language model learns how something turned out, can it still judge the past without hindsight?**

The scientific object is **hindsight in language-model reasoning**.

Do not replace this with technical meta-language such as “retrospective epistemic reconstruction,” “information-set conditioning,” or a benchmark-specific metric. Those can be useful in methods, but they are not what the paper is *about*.

The positive explanatory chain is:

1. later outcome evidence changes judgments of the past even when models recognize that the evidence came later;
2. outcomes from unrelated resolved events also exert a directional pull;
3. replacing NO-supporting later evidence with YES-supporting later evidence moves the same recipient judgment upward, with strongly model-dependent magnitude;
4. in Gemma, this outcome influence becomes causally expressed after contextual integration in a late answer-position decision state.

`retrospective outcome entrainment` is a name for the discovered regularity in steps 2–3. It is not the paper's scientific object and should not dominate the title or introduction.

## Research style: no defense-first science

This project must not become a catalogue of reviewer objections.

Do **not** add experiments because “a reviewer might ask for another model / prompt / benchmark / control / mitigation.” Do not organize the paper as a sequence of “not X, not Y, not Z.” Strong ACL/EMNLP papers usually establish a natural phenomenon and then descend through positive explanatory questions.

The main text should therefore read:

> question → phenomenon → sharper regularity → causal test → mechanism

not:

> claim → objection 1 → control → objection 2 → control → limitation list.

Failed experiments and preregistered reversals remain important scientific history, but they belong in `RESEARCH_HISTORY.md`, `EXPERIMENTS.md`, or the appendix unless they directly move the main explanatory story forward.

The default is **no new experiment**. If a genuinely new scientific question emerges, formulate it first and then decide whether an experiment is needed. “Reviewer defense” is not a scientific question.

## Evidence discipline

- Preserve the real chronology: especially the reversed original *Unring the Bell* prediction, the failed broad-family attempt, G7, and the G13 → G14 → G15 development.
- Do not rewrite historical preregistrations. Individual top-level preregistration files have been consolidated out of the root; their exact text remains in Git history/freeze commits and is summarized in `EXPERIMENTS.md`.
- Report the actual continuous results. Do not turn frozen decision thresholds into the paper's conceptual vocabulary.
- Mechanistic conclusions from G13–G15 are Gemma-specific unless separately established.
- BTF-3 is the natural experimental substrate, not the identity of the scientific question.

## Environment policy

Prefer the existing local project virtual/conda environment and existing shared caches. First inspect and try the current environment. Create a new environment only for a genuine incompatible CUDA/PyTorch/package-version conflict; document the reason and keep the replacement minimal.

## GPU policy

Usable compute nodes when cards are actually idle: `fvcrc10`, `fvcrc11`, `fvcrc12`, `fvcrc13`, `fvcrc15`, `fvcrc20`, `fvcrc21`.

Check occupancy before launching and use idle cards only. During daytime, avoid occupying more than **8 GPUs total at once** unless the user explicitly overrides this. Prefer compatible existing nodes/environments and be mindful of shared NFS/checkpoint-loading bottlenecks.

## Git policy

Completed research/documentation changes should land directly on `main`. Keep commits coherent and descriptive. Preserve scientific provenance in Git history even when obsolete top-level narrative/preregistration files are consolidated for readability.
