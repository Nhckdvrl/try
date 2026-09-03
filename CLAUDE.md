# Claude project instructions

This file is the first project-level context for Claude Code. Anthropic documents `./CLAUDE.md` as shared project memory loaded automatically when Claude Code starts in the repository.

## Read these first

Before proposing experiments, editing claims, or running code, read in this order:

1. `PAPER_FRAME.md` — authoritative scientific object, current claims, forbidden overclaims, and experiment gate.
2. `ACL_EMNLP_ALIGNMENT_STANDARD.md` — the submission-quality standard. We align to strong ACL/EMNLP/NAACL Main papers and Outstanding papers, not to the median accepted paper and not to Findings as the target bar.
3. `RESEARCH_HISTORY.md` — how the project moved from *Unring the Bell* to the current question. Preserve this epistemic chronology even when old trial documents are removed.
4. `PAPER_OUTLINE.md` — current paper narrative and figure plan.
5. `RELATED_WORK_2026.md` — novelty boundaries and closest conceptual neighbours.

Preregistrations, frozen transformation contracts, result files, and raw analysis artifacts are evidence/provenance. Do not rewrite their historical claims to match the current story.

## Scientific objective

The paper asks:

> **After learning how something turned out, can a language model still condition a reconstructed past judgment only on the information that was available beforehand?**

The object is **retrospective epistemic reconstruction / information-set conditioning under hindsight**, not BTF-3, not generic temporal leakage, not generic distractor robustness, and not a benchmark-specific failure.

The current evidence chain is:

1. future evidence violates information-set invariance despite near-ceiling boundary recognition;
2. the influence is not restricted to evidence about the target event: outcome-shaped evidence from unrelated resolved events produces donor-directed retrospective pull, including after explicit verdict redaction in 2/3 primary models;
3. replacing a NO-supporting irrelevant future packet with a YES-supporting one raises the same recipient probability in all three primary models, with strongly heterogeneous magnitude and an indeterminate preregistered 5pp panel gate;
4. in the strong-effect model (Gemma), the tested one-dimensional packet-local bottleneck is not supported; after recipient contextualization, future-outcome influence becomes causally actionable in a late answer-position decision state, prospectively confirmed on a fresh donor assignment.

Do **not** silently strengthen this into “changing only an abstract outcome bit,” “robust causal outcome entrainment across models,” “a dedicated hindsight circuit,” or “the full mechanism of hindsight contamination.”

## Standard for new experiments

The default is **no new experiment**. The current project is Main-shaped and should prioritize writing, figures, claim discipline, and reviewer-facing coherence.

A new experiment is allowed only if, before any run, we can write two algorithms/accounts that explain all evidence through G15 but make opposite causal predictions under one clean intervention. The only currently plausible Outstanding-ambition branch is:

> **How does a represented information boundary interact with the late outcome pathway?**

Possible account family: a causal gate that should suppress outcome influence vs. a parallel recognition computation that is readable but not used by the decision pathway vs. a readout-only recognition representation. Do not create “G16” unless the intervention actually discriminates such accounts. No extra prompt, benchmark, model, redaction, CoT, mitigation, or scale sweep merely for reviewer defense.

## Evidence discipline

- Preserve preregistered failures and reversals (especially G7, G13, G14 chronology).
- Separate exploratory discovery from prospective confirmation. G14 motivated the recipient-conditioned estimand; G15 prospectively confirmed it on a fresh assignment.
- Report continuous estimates together with frozen categorical gates when they differ.
- Mechanism claims in the main paper are Gemma-specific unless independently established elsewhere.
- BTF-3 is a measurement window, not the scientific identity of the paper.
- Do not claim external ex-ante fidelity: G7 failed in the opposite direction and uncontaminated judgments correlate only weakly with the independent ex-ante forecast.

## Environment policy

Prefer the **existing local project virtual/conda environment** and existing shared caches. First inspect the current environment and try to run with it. Do not create a fresh environment merely for cleanliness.

Create a new environment only when the existing environment is genuinely unusable (for example an irreconcilable CUDA/PyTorch/package-version conflict). If a new environment is necessary, document why and keep it minimal/reproducible.

## GPU policy

Usable compute nodes when GPUs are actually idle: `fvcrc10`, `fvcrc11`, `fvcrc12`, `fvcrc13`, `fvcrc15`, `fvcrc20`, `fvcrc21`.

Before launching, inspect GPU occupancy (for example with `nvidia-smi`) and use **idle cards only**. During daytime, avoid occupying more than **8 GPUs total at once** unless the user explicitly overrides this. The reason is shared-lab fairness: do not monopolize classmates' cards.

Prefer packing work onto already-compatible nodes/environments rather than creating many node-specific environments. Be cautious about shared NFS/checkpoint-loading bottlenecks.

## Git policy

The user wants completed research/documentation changes landed directly on `main`. Keep commits coherent and descriptive. Never rewrite or delete provenance needed to audit preregistered experiments. Clean obsolete narrative documents only after their scientifically useful history has been preserved in `RESEARCH_HISTORY.md`.
