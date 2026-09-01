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
  per-item recognition stays at 97–100%;
- do so **against the same evidence's full measurable influence**: it moves a
  licensed retrospective judgment by 39–47 points, and 41–81% of that influence
  is absent from the ex-ante judgment. Models are therefore not inert to the
  instruction — what G3 shows is that how much survives is a property of the
  model rather than of the reason it was given. (The licensed frame also asks a
  different target question, by design; it normalizes the effect, it is not a
  minimal pair for the licence.)
- are perturbed even by a post-cutoff packet from a **different question**:
  foreign packets cause 50.7–100.1% as much undirected movement as real
  packets. Donor-outcome pull is positive with intervals above zero in all
  three models (2.93–12.26 points), although G8's preregistered 5-point
  strong-form threshold is cleared only by Gemma, so its frozen panel row is
  `H-presence-weak`;
- still import the foreign question's outcome after explicit YES/NO verdict
  sentences are removed. G11 retains 73.9% of donor pull in Qwen and 67.1% in
  Gemma, while Mistral retains 35.0%; the preregistered panel verdict is
  `survives` (2/3).

G3 establishes that changing the stated reason does not reduce the effect at
panel level. It does **not** establish that the model actually comes to believe
the `unreliable` packet false, and it therefore cannot rule out a general
belief-sensitive account. Two manipulations that changed how much the prompt
talks about the packet — removing the verdict sentence (G2-B), adding clauses
about it (G3) — made the effect larger in at least one model. G8 and G11 provide
the sharper explanatory step: outcome-shaped context exerts directional
influence even when it concerns another question and lacks an explicit verdict.

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
| **H-truth** | evidence believed true is hard to make causally inert | G3's `unreliable` wording does not reduce intrusion, but this does not prove the model believed it false; the general account remains unresolved |
| **H-temporal** | reconstructing a past state is specifically hard | disfavored within this prompt slot, not globally ruled out: a non-temporal procedural reason is enforced no better |
| **H-reason-inert** | changing the stated justification does not improve enforcement | G3 — **realized at panel level**; no reason reduces the effect, while two added clauses increase Gemma's effect |
| **H-own-diagnostic** | contamination is integration of evidence diagnostic of this question | G8 — **insufficient**: unrelated packets cause large movement and donor-directed pull |
| **H-explicit-label** | foreign outcome import is explicit YES/NO copying | G11 — **insufficient at panel level**: redacted donor pull survives in 2/3 models; Mistral is the stated exception |
| **H-outcome-context** | outcome-shaped later context enters the judgment even when it concerns another question | G8 + G11 — **supported behaviorally**; G12 directly changes donor outcome within recipient, with positive paired intervals in all three models and strongly heterogeneous magnitude |
| **H-packet-scalar** | unrelated outcome evidence is carried to the answer through one shared packet-local scalar | G13 — **not established**: held-out donor outcome is decodable (peak BA 0.758), but one-dimensional packet-span interchange has no ≥3pp causal window |
| **H-decision-state** | outcome evidence is contextualized into a recipient-conditioned variable at the answer position | G14 — strong provisional evidence: layers 29--47 form a bidirectional, axis-specific causal window (peak +5.39pp, 32% recovery), but the inherited global-classification gate misses by 0.008; fresh-assignment paired confirmation required |
| **H-override / H-absent** | an ex-ante estimate is built then overridden / never built | unresolved. The current G6 suffix mask localizes packet-to-answer access but does not establish either internal-state claim |

H-override and H-absent remain a legitimate mechanistic pair, but the existing
G6 intervention does not distinguish them. Opening the model is permitted only
after a causal variable and intervention make the two accounts predict
different outcomes.

## 5. The novel explanatory step

Not "prior work did not measure X on Y." The step is the same one the reference
papers make: replace a coarse observed variable with a sharper latent one.

```text
observed:  future evidence shifts a reconstructed past judgment
latent:    retrospective outcome entrainment -- outcome-shaped later context
           pulls the judgment toward the outcome it supports even when the
           context concerns a different question and contains no explicit
           verdict sentence
```

This is the paper's forward explanatory step. G8 orthogonalizes relevance from
outcome direction: the donor packet is irrelevant to the recipient question,
yet produces large movement and donor-directed pull. G11 orthogonalizes
explicit verdict visibility from the remaining outcome evidence: the pull
survives at panel level. Together they identify a lower-level regularity beneath
generic hindsight contamination, analogous to contextual entrainment beneath
generic distraction.

The nearest published neighbour (*When Do LLMs Apply the Wrong Law?*, arXiv
2608.14610) already owns the observed layer: models state a temporal rule and
violate it. We concede that in the introduction and do not compete on it. What
that work does not have is the within-item causal manipulation of a single
fixed piece of evidence, and it does not identify donor-directed outcome
entrainment from irrelevant future context. The paper's contribution is this
positive phenomenon and its controlled decomposition, not a catalogue of
accounts that failed.

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
| **foreign packet (G8)** | does outcome-shaped future context pull the judgment when it is causally irrelevant to this question? |
| **redacted foreign packet (G11)** | is that donor-directed pull an explicit-verdict artifact or an evidential effect? |

Only the first, G8, and G11 belong to the main explanatory tree. G2/G3/G4 are
compact characterization or alternative-account checks; G5/G7/G9/G10 are
reported failures or boundaries and belong outside the headline sequence.

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
measured. G3 did not support its favoured reason-sensitive account; G7's primary
test failed outright and in the opposite direction. The title did not move in
either case — only the explanation section did. G8 and G11 then strengthened
the paper by isolating retrospective outcome entrainment. Even if a future
neural account fails, the causal phenomenon and its donor-directed structure
remain.

## 8. When mechanism is allowed

Mechanistic interpretability is not a credential and will not be added to make
the paper look mechanistic. The rule, taken from the reference papers:

> Open the model only when two competing explanations make the same behavioral
> prediction and differ only internally.

The frozen G6 implementation does not meet this bar. Its suffix attention mask
can show when direct access from answer positions to packet tokens remains
causally effective. Late masking failure can equally arise because packet
information was copied into other token residuals early; late masking success
does not establish that an ex-ante estimate was previously constructed. The
curve is therefore a timing/localization instrument, not an adjudication of
`H-override` versus `H-absent`. Full G6 is deferred until a stronger causal
variable and intervention are specified.

Any patching, probing, or head-ablation proposal that does not adjudicate a
named pair from §4 is refused.

## 9. The eight gates, answered

1. **Natural question** — §1. One sentence, no apparatus.
2. **Scientific object** — §2. Reconstruction of a past epistemic state; a
   cognition object that precedes the dataset.
3. **Competing explanations** — §4. The main sequence distinguishes
   own-question diagnostic integration, explicit-verdict copying, and
   outcome-context entrainment; internal-state accounts remain unresolved.
4. **Novel explanatory step** — §5. Generic hindsight contamination becomes
   donor-directed retrospective outcome entrainment. The nearest neighbour is
   conceded by name.
5. **Measurement window** — §6. BTF-3 isolates the variable; it did not create
   the question.
6. **Experiment coherence** — §6's table. Every experiment is a sub-question of
   §1 and can be written as one.
7. **Hypothesis robustness** — §7. The natural question and replicated effect
   survive failure of any favoured explanation.
8. **Mechanism necessity** — §8. The current mechanism design is deferred
   because it does not identify its named internal contrast.

## 10. Standing rule for new experiments

Before any new run, the proposal must be written as a completion of this
sentence:

> *This experiment further answers how a model reconstructs a past epistemic
> state that its own later knowledge has contaminated, by separating ___ from
> ___.*

If the blanks cannot be filled with two named accounts from §4, the experiment
is another condition, not another answer, and it does not get run.
