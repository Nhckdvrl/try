# Dataset redesign: source-native Information-Set Reasoning

## Hard constraint

CDS-v1 cannot be the dataset identity of an ACL/EMNLP/NAACL main-paper claim.
Its 144 items share a limited number of latent templates and a common compiler:

```text
BACKGROUND -> RULING -> ADDITIONAL INFORMATION -> TASK
```

That is useful experimental control and weak evidence for cross-domain breadth.
CDS-v1 is therefore retained as a Controlled Discovery Suite and mechanism
instrument only.

## Scientific object

An Information-Set Reasoning task defines a target decision and the information
licensed to influence it. Every family must measure both:

```text
Responsiveness        = Y(allowed E+) - Y(allowed E-)
OutOfSetIntrusion     = Y(outside E+) - Y(outside E-)
BoundarySelectivity   = Responsiveness - OutOfSetIntrusion
```

Raw contrasts are primary. Ratios are secondary and only defined above a frozen
responsiveness floor.

## Source-native architecture

External items use `src/information_set_schema.py`:

```text
source_id / independent_unit_id / boundary_type / reference_context /
oob_variant / admissible_variant / provenance / transformation_id
```

There is no universal admit/exclude rule and no universal compiler. FANToM must
remain a perspective-taking task, BTF-3 a pastcasting task, ForecastBench a
forecast, and Aiyer an ex-ante decision-quality judgment.

## Transformation contract

Before an adapter exports items, its contract must identify:

- the target decision and scoring rule;
- the independent source unit;
- the critical information intervention;
- fields held identical between paired variants;
- source fields changed and why;
- whether text is verbatim, deterministically edited, or newly authored;
- which condition supplies allowed responsiveness;
- source-specific utility and boundary-knowledge checks.

The adapter is rejected if the intervention silently changes the target agent,
question semantics, answer space, or base difficulty.

## First-wave sources

| Boundary | Source | Current role | Main unresolved issue |
|---|---|---|---|
| Perspective | FANToM | primary candidate | clean matched allowed/OOB intervention without changing the question |
| Temporal | BTF-3 | primary candidate | deterministic post-cutoff information intervention |
| Temporal | ForecastBench | robustness | composite IDs and multi-date resolution join |
| Temporal evaluation | Aiyer | natural anchor | one semantic vignette; no native allowed task |
| Procedural | Engel et al. | phase 2 | material access/license and character/wiretap heterogeneity |
| Decision scope | Dutch hiring | held-out transfer | exact source and normative claim must be resolved |
| Role/access | PrivaCI-Bench, CI-Work | deployment extension | must not claim privacy/IFC novelty |
| Invalidity | Ramsey/CIE | contrast | distinguish false/invalid from true-but-out-of-set information |

## Independent-source-unit inference

The estimand equally weights original semantic units:

1. average all renderings/conditions contributing the same per-unit effect;
2. compute the mean of cluster means;
3. bootstrap cluster means.

Duplicating a rendering cannot change the estimate. Historical G0 item-level
bootstrap remains frozen and unchanged.

## Data and model gates

No model pilot begins until:

- official files and revisions are pinned;
- reuse status is honest;
- transformation contracts pass human audit;
- validators and unit tests pass;
- independent-unit rules are frozen.

The exploratory gate passes only if at least two different natural boundary
families show utility, boundary knowledge, and non-zero intrusion. Otherwise the
project narrows.
