# ACL / EMNLP / NAACL alignment audit — locked after G15

This is a paper-level audit, not an experiment log. It evaluates the locked
submission against the scientific shape of the five primary rulers and the
eight gates in `PAPER_FRAME.md`.

## 1. One-sentence paper before any dataset

> **After learning how something turned out, can a language model reconstruct
> what was reasonable to believe before—and how does future outcome information
> enter that reconstructed decision?**

This question exists independently of BTF-3, forecasting, or any model family.
It is a natural question about retrospective epistemic reconstruction, adjacent
to hindsight bias, curse of knowledge, historical audit, and inadmissible
evidence.

## 2. The three contributions reviewers should retain

1. **Causal hindsight contamination despite boundary recognition.** On 256
   fresh natural questions, three open models identify the temporal boundary at
   99.2–100% yet the same future evidence moves reconstructed ex-ante judgments
   by 7.5–27.7pp.
2. **Retrospective outcome entrainment.** Influence does not require relevance
   to the current question or an explicit verdict. Under a direct within-question
   manipulation, changing whether an irrelevant redacted packet supports YES or
   NO changes the judgment in that direction in all three models, with strongly
   model-dependent magnitude.
3. **A fresh-confirmed late decision state.** In the strong-effect model,
   packet-local donor outcome is decodable but not a causal scalar bottleneck.
   After contextualization with the recipient question, a donor-general outcome
   coordinate emerges at the answer position. On new donor assignments it forms
   a layers-29–47 causal window, transfers both directions, recovers up to 48%
   of the effect, and disappears on an orthogonal axis.

Everything else is support, scope, provenance, or appendix.

## 3. Why the explanatory step is larger than a follow-up

The progression changes explanatory level three times:

```text
models use future information
    -> outcome-shaped irrelevant context entrains reconstructed judgments
    -> donor outcome itself is a within-question causal variable
    -> outcome influence is instantiated as a late recipient-conditioned
       decision coordinate rather than a transported packet-local scalar
```

This parallels the rulers' central moves:

| ruler | coarse observation | explanatory object |
|---|---|---|
| Llama See, Llama Do | irrelevant context distracts | contextual entrainment |
| Racing Thoughts | context is ignored/misused | layer-timed contextualization process |
| Filler–Gap | several constructions work | shared causal abstraction |
| Property Inference | models project properties | taxonomy vs representational similarity |
| Tool Irrelevance | models call irrelevant tools | structural match competing with semantic checking |
| **this paper** | future evidence changes past judgment | outcome entrainment and its late contextual decision state |

The novelty is therefore not a new condition on an existing benchmark. It names
a lower-level regularity, orthogonalizes its causal variable, and identifies the
internal computation through which that variable controls the answer.

## 4. Dataset versus scientific object

- **Scientific object:** reconstruction of a past epistemic state under known
  future outcomes.
- **Measurement window:** BTF-3 supplies documented pre-cutoff context,
  post-cutoff resolution evidence, and a natural continuous judgment.
- **Controlled instruments:** packet presence/admissibility, foreign donor,
  verdict redaction, paired donor outcome, and activation interchange are
  derived from the scientific question. They do not create it.

This meets the same design standard as templated filler–gap interventions,
Racing Thoughts' controlled QA, and SABEval's constructed factorization.

## 5. One coherent headline experiment tree

```text
Can the model reconstruct the past after seeing the future?
    |
    +-- E1: same future packet present vs absent
    |       -> large causal contamination despite recognized exclusion
    |
    +-- E2: different-question packet; then remove explicit verdict
    |       -> relevance and label copying are insufficient
    |
    +-- E3: same recipient, redacted YES donor vs redacted NO donor
    |       -> donor outcome causally sets direction; magnitude varies by model
    |
    +-- E4: packet site vs answer site; then rebuild donor assignment
            -> late recipient-conditioned causal decision coordinate
```

Each branch answers the headline. Scale, model breadth, exclusion reasons,
mitigation attempts, weak pastcasting, and source failures are not branches in
this tree.

## 6. Mechanism is contribution, not credential

The two internal algorithms predict the same G12 output:

- **packet-local transport:** an outcome scalar is extracted from the packet and
  carried to the answer;
- **contextual decision-state construction:** packet semantics first interact
  with the recipient question; only then does a shared causal coordinate form.

Held-out donor decodability cannot decide between them. Site-matched causal
interchange can. The packet axis is non-causal; the answer-site axis has a late
causal window and fresh replication. This is the role mechanism plays in the
reference papers: adjudicating a scientific explanation that behavior alone
cannot distinguish.

The mechanism does **not** establish that a clean ex-ante estimate was first
constructed and then overwritten. That separate override-vs-absence claim is
excluded.

## 7. Hypothesis robustness

If the late decision-state hypothesis had failed, the title and first two
contributions would remain. G13 in fact rejected the first internal account
without changing the paper's question. The mechanistic result improves
explanation depth; it is not the existence condition for the paper.

This gives the paper the robustness of *Llama See, Llama Do*: the phenomenon is
stable, while internal hypotheses remain genuinely falsifiable.

## 8. Main-text inclusion lock

### Main text

- natural question and causal 2×2 instrument;
- 256-unit recognition/enforcement replication;
- G8/G11 outcome entrainment;
- G12 paired donor-outcome intervention;
- G15 fresh-confirmed late decision state;
- concise breadth/scope and limitations.

### Appendix or one-sentence controls

- verdict-redaction details and audit;
- scale and model breadth;
- exclusion-reason factorization;
- G13 packet-site comparison;
- G14 discovery and its unchanged failed composite gate;
- G7/G9/G10 and source qualification failures;
- old G6 masking design and all exploratory campaign history.

The paper must never narrate “G13 failed, G14 almost passed, so G15 fixed it.”
The scientific narrative is “packet-local transport and contextual decision
construction predict the same behavior; a site contrast and prospectively
fresh confirmation support the latter.”

## 9. Honest venue-level assessment

### Why this is now Main-long shaped

- natural question predates the dataset;
- large prospectively accumulated natural measurement window;
- within-item causal estimand rather than benchmark accuracy;
- a named explanatory phenomenon below the observation layer;
- orthogonalized relevance, verdict, and outcome direction;
- competing algorithmic accounts;
- held-out donor identities, bidirectional intervention, matched causal control,
  layer trajectory, and fresh-assignment confirmation;
- title survives mechanism failure.

### What still separates it from a guaranteed Outstanding paper

- the primary natural source is one forecasting substrate;
- the confirmed internal mechanism is in one strong-effect model;
- G12's frozen 5pp panel verdict is indeterminate despite all three continuous
  paired intervals being positive;
- the paper identifies a contaminated late decision state, not the full process
  that constructs or protects a clean past epistemic state.

These are limitations to state, not invitations for defensive experiments. The
current workload and explanation are sufficient for a strong Main submission;
Outstanding competitiveness depends more on conceptual writing, figure clarity,
and reviewer judgment than on adding another condition.

## 10. Final writing test

Every main-text paragraph must advance one of these sentences:

> Future outcome information can causally enter a reconstructed past judgment
> even when the model recognizes that it is inadmissible.

> The influence follows outcome rather than relevance or an explicit verdict.

> The outcome becomes causally effective as a late, recipient-conditioned
> decision coordinate.

If a paragraph advances none of them, move it to the appendix or remove it.
