# Paper frame — the authoritative register

**Created:** 2026-09-01. This document, not `README.md`, is what the paper is
about. `README.md` records where the repository has been; this records what the
paper claims and which experiments are allowed to exist.

Every entry below is written to survive the eight gates that separate a
Main/Outstanding-shaped paper from a competent follow-up experiment. The gates
are stated in §9 and each is answered explicitly. A proposed experiment that
cannot be written as a sub-question of §1 does not get run.

---

## 1. The natural question

> **After a model has learned how something turned out, can it still say what
> it was reasonable to believe before?**

No dataset, model, metric, or condition name appears in that sentence, and it
is comprehensible to a reviewer who has never read an interpretability paper.
It was a question about minds before it was a question about language models:
hindsight bias, the curse of knowledge, and the law of inadmissible evidence
are all attempts to ask it.

It is stable under every result we could obtain. That is the point of §7.

## 2. The scientific object

**Reconstruction of a past epistemic state under hindsight.**

The object is not a benchmark, not a failure mode, and not a metric. It is the
operation of holding a judgment fixed to the information that was available at
a specified moment, when the reasoner has since acquired information that
settles the question.

This is a cognition/reasoning object of the same kind as *contextualization*
(Racing Thoughts), *property induction* (NAACL 2025), *abstract syntactic
structure* (EMNLP 2025 Outstanding), and *distraction* (ACL 2025 Outstanding).
It existed before BTF-3 and would survive BTF-3's deletion.

## 3. What is established

On 256 fresh, independently sampled natural forecasting questions, three
open checkpoints:

- identify per item, at 99.2–100% accuracy, that a piece of evidence postdates
  the moment they are asked to reason from;
- are nonetheless moved by that evidence by 7.5–27.7 probability points;
- remain moved after the explicit resolution verdict is mechanically removed
  (10.2–34.6 points, *larger* without it);
- remain moved at every available model size in one family (16.0–36.8 points at
  4B/9B/27B, largest checkpoint most contaminated);
- **remain moved under every stated reason for exclusion** (G3): a non-temporal
  licensing reason with the packet's accuracy affirmed, a reason that undercuts
  the packet's truth, and no reason at all all leave the effect intact, while
  per-item recognition stays at 97–100%.

G3 is what turned the phenomenon into a claim. The failure is not about time,
not about whether the model believes the evidence, and not about the reason
being unstated. Two manipulations that changed how much the prompt *talks about*
the packet — removing the verdict sentence (G2-B), adding clauses about it
(G3) — both made the effect **larger**.

One preregistered test has failed and is kept: G7 predicted the packet moves
the model away from BTF-3's independent ex-ante forecast, and it moves it
closer. The uncontaminated cell correlates only 0.28–0.33 with that forecast.
The paper therefore may not claim infidelity to an external ex-ante reference,
states that these models are weak pastcasters as a limitation, and keeps the
within-item causal estimand, which nothing in G7 touches.

## 4. The competing explanations

A paper at this level does not report a phenomenon; it adjudicates between the
accounts that could produce it. Four are live, and the design of every
remaining experiment is fixed by which pair it separates.

| tag | account | separated by |
|---|---|---|
| **H-copy** | the model reads the revealed answer | G2 Experiment B — **ruled out** |
| **H-scale** | small models; capability closes the gap | G2 size analysis — **ruled out within one family** |
| **H-truth** | the model has no machinery for making information it believes *true* causally inert; the temporal label is one instance | G3 — **ruled out**: undercutting the packet's truth does not reduce the effect either |
| **H-temporal** | licensing is enforceable in general; reconstructing a *past* state is the specific hard operation | G3 — **ruled out**: a non-temporal licensing reason is enforced no better |
| **H-inert** | no stated reason is enforced; the packet's presence dominates every licensing rule | G3 — **realized**. G8 asks whether the packet must even be *about* this question |
| **H-override** | the ex-ante belief state *is* constructed internally and then overridden by the packet-driven answer | G6 (deferred; see §8) |
| **H-absent** | no ex-ante belief state is ever constructed; recognition is a labeling computation running beside, not upstream of, the answer | G5 (behaviorally), G6 (internally) |

H-override and H-absent are the pair that mechanistic interpretability is
*required* for. Neither is decidable from outputs, which is the only condition
under which this project is permitted to open a model.

## 5. The novel explanatory step

Not "prior work did not measure X on Y." The step is the same one the reference
papers make: replace a coarse observed variable with a sharper latent one.

```text
observed:  "the model violates a temporal boundary it can state correctly"
latent:    the boundary's *reason* is not what fails -- no stated reason is
           enforced at all, temporal or otherwise, including one that undercuts
           the evidence's truth. What the model lacks is any route from a
           licensing statement it can restate to the computation that produces
           the judgment.
```

The factorization was designed to ask *which* reason is enforceable. The answer
came back **none**, which is a stronger and simpler claim than the one the
design was built to support, and it is what the paper now argues.

The nearest published neighbour (*When Do LLMs Apply the Wrong Law?*, arXiv
2608.14610) already owns the observed layer: models state a temporal rule and
violate it. We concede that in the introduction and do not compete on it. What
that work does not have is the within-item causal manipulation of a single
fixed piece of evidence, and it does not factor the boundary into licensing
versus reason. That factorization, and what it implies about which boundaries a
language model can enforce at all, is the contribution.

## 6. The measurement window

**BTF-3 is an instrument, not the object.** It supplies hundreds of natural
questions whose ex-ante state and ex-post resolution are both documented, which
is what makes the manipulation possible. It is not the paper's identity, and
nothing in §1 depends on it.

The lesson the reference papers teach here is explicit and was previously
mis-stated in this repository: **the scientific object must be natural; the
measurement instrument may be highly controlled.** ACL 2025's filler-gap
Outstanding paper runs on templated minimal pairs; Racing Thoughts constructs
its own QA items; the tool-irrelevance paper builds SABEval specifically to
orthogonalize two latent variables it named first. A synthetic instrument
derived from the question is correct; a question derived from an available
dataset is not.

Under that rule every manipulation in this project is legitimate exactly
because it is derived downward from §1:

| manipulation | the sub-question it exists to answer |
|---|---|
| packet present/absent × licensed/unlicensed | does the future change the reconstructed past, causally, within item? |
| verdict redaction | is the change evidence integration or answer copying? |
| within-family size | is it a capability deficit that scale closes? |
| position of the constraint | does *when* the constraint is stated change enforcement? |
| **reason for exclusion (G3)** | which kind of boundary can the model enforce at all? |
| **model breadth (G4)** | is this a property of three checkpoints or of the class? |
| **deliberation and the state scaffold (G5)** | does forcing explicit reconstruction of the ex-ante state recover the judgment? |
| **layerwise readout and intervention (G6)** | is the ex-ante judgment built and overridden, or never built — and can it be restored at inference time? |

## 7. Robustness of the title to failure

The test that matters: **if the favourite hypothesis dies, does the paper still
have its title?**

Racing Thoughts fails this test — if the race-condition predictions had all
failed, that title dies. It is a high-risk hypothesis-driven paper. Llama See,
Llama Do passes it — contextual entrainment survives even if no entrainment
head is found.

This paper is in the second class, and the claim has now been tested rather
than asserted. The title-level object is *whether a model can reconstruct a past
judgment after learning the outcome*, and the answer to that is already
measured. G3 returned H-inert rather than the H-truth row the design leaned
toward; G7's primary test failed outright and in the opposite direction. The
title did not move in either case — only the explanation section did. Nothing
downstream can retroactively unmake the 256-unit recognition–enforcement
dissociation, and if G6 finds no ex-ante state anywhere, that is a result about
*how* the failure happens, not about whether it does.

## 8. When mechanism is allowed

Mechanistic interpretability is not a credential and will not be added to make
the paper look mechanistic. The rule, taken from the reference papers:

> Open the model only when two competing explanations make the same behavioral
> prediction and differ only internally.

That is true of exactly one remaining pair: **H-override vs H-absent** (§4).
Both predict the same contaminated output; they differ in whether an ex-ante
estimate exists in the residual stream and is discarded, or was never computed.
G6 is therefore permitted, and is deliberately **not** preregistered until G3
and G5 resolve, because which mechanism question is worth asking depends on whether
enforcement turns out to be truth-keyed.

Any patching, probing, or head-ablation proposal that does not adjudicate a
named pair from §4 is refused.

## 9. The eight gates, answered

1. **Natural question** — §1. One sentence, no apparatus.
2. **Scientific object** — §2. Reconstruction of a past epistemic state; a
   cognition object that precedes the dataset.
3. **Competing explanations** — §4. Six named, two already eliminated by
   preregistered experiments.
4. **Novel explanatory step** — §5. Licensing/reason factorization, not a new
   scenario for an old observation. The nearest neighbour is conceded by name.
5. **Measurement window** — §6. BTF-3 isolates the variable; it did not create
   the question.
6. **Experiment coherence** — §6's table. Every experiment is a sub-question of
   §1 and can be written as one.
7. **Hypothesis robustness** — §7. The title survives every possible outcome of
   G3, G4, G5 and G6.
8. **Mechanism necessity** — §8. Mechanism is gated on a behaviorally
   undecidable pair, and refused otherwise.

## 10. Standing rule for new experiments

Before any new run, the proposal must be written as a completion of this
sentence:

> *This experiment further answers how a model reconstructs a past epistemic
> state that its own later knowledge has contaminated, by separating ___ from
> ___.*

If the blanks cannot be filled with two named accounts from §4, the experiment
is another condition, not another answer, and it does not get run.
