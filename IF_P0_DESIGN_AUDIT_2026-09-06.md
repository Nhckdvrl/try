# IF-P0 Design Audit — Socially Constituted State Update

**Created:** 2026-09-06  
**Authority:** `DURABLE_RQ_SEARCH_2026-09-06_V3.md`  
**Status:** editable pre-freeze design. **No target-model output yet.**  
**Paper status:** **NOT MAINLINE**.

IF-P0 is a small discovery experiment.

It is not designed to prove that language models “understand institutions,” and it is
not a benchmark of ownership accuracy.

The discovery question is:

> **When physical state and socially constituted status are varied independently, do
> pretrained language models exhibit a reusable internal update structure for social
> status that is stronger than generic relation/event tracking?**

If the answer reduces to ordinary relation semantics, IF is killed as a paper identity.

---

# 1. Non-negotiable success definition

The following are **not** IF-P0 successes:

- owner/non-owner is linearly decodable;
- models answer ownership questions correctly;
- sale changes ownership answers;
- appointment changes office answers;
- explicit rules improve performance;
- role/status words cluster;
- one domain has a strong probe;
- one model has a visually attractive PCA plot.

A result is interesting enough for another audit only if it shows a **structural law**
beyond these facts.

The minimum acceptable discovery shape is:

> **Status-changing events create/update an internal state that generalizes across
> substantially different status domains, remains distinguishable when physical
> state changes are crossed independently, and cannot be explained equally well by
> matched ordinary relation updates.**

This is still not a paper claim. It only earns a post-P0 audit.

---

# 2. One-example core

## Physical change, social status fixed

> Omar owns a bicycle. He lends it to Lena, who takes it home.

Physical possession changes.

Ownership does not.

## Social-status change, physical state fixed

> Lena is still holding Omar's bicycle. Omar sells the bicycle to Lena while it
> remains in her hands.

Ownership changes.

Physical possession does not.

No words such as:
- institutional fact;
- constitutive rule;
- status function;
- social ontology;

are shown to the model.

---

# 3. Pilot domains

Use **four** ordinary domains with visibly different surface semantics.

## D1 — Ownership

Physical axis:
- possession / location of object.

Social axis:
- current owner.

Natural status-changing events:
- sale;
- gift/transfer.

Natural status-preserving physical events:
- lend;
- carry/move while ownership is unchanged.

Avoid disputed edge cases such as theft, abandoned property or inheritance law.

## D2 — Office holding

Physical axis:
- who is seated/present/using the office space or symbolic object.

Social axis:
- who currently holds the office.

Natural status-changing events:
- appointment/election;
- resignation/replacement.

Status-preserving physical events:
- leaving the room;
- another person sitting in the chair;
- moving nameplate/seat.

Avoid offices whose authority rules vary by jurisdiction.

## D3 — Membership

Physical axis:
- badge/card/lanyard possession or presence at a meeting.

Social axis:
- current membership.

Natural status-changing events:
- admission;
- resignation/expulsion.

Status-preserving physical events:
- putting on/removing a badge;
- entering/leaving the meeting room.

Avoid morally or politically charged organizations.

## D4 — Ticket / credential validity

Physical axis:
- location/holder/physical condition of the ticket or credential.

Social axis:
- whether it is currently valid.

Natural status-changing events:
- valid issuance/activation;
- cancellation/expiration where the relevant timing is explicit.

Status-preserving physical events:
- folding/moving/handing over the physical token when transfer does not itself affect
  validity.

Avoid legal identification documents and ambiguous transferability rules.

Authorization is intentionally **not** a primary IF-P0 domain because 2026 agent-memory
work already makes evolving authorization state a direct object.

---

# 4. Independent-unit budget

Target: **24 independent semantic skeletons**.

- 6 per domain;
- different entities/objects/events, not name substitutions;
- each skeleton should support both a physical-only and status-only transition without
  unnatural wording.

The semantic skeleton is the unit of uncertainty.

Do not count:
- paraphrases;
- state checkpoints;
- physical/status questions;
- multiple layers;

as independent samples.

---

# 5. Core trajectory classes

Each skeleton should have a minimal matched set.

## P — Physical-only update

A physical relation/state changes while social status remains fixed.

## S — Social-status-only update

The socially constituted status changes while the selected physical state remains
fixed.

## N — Neutral/persistence control

An ordinary event occurs that changes neither selected physical relation nor social
status.

Do not add additional event classes to P0 unless a specific confound makes the object
unidentifiable.

---

# 6. Direct behavioral gold

At the relevant checkpoint ask two independent direct questions:

1. physical-state question;
2. social-status question.

Examples:

> Is Lena currently holding the bicycle? TRUE/FALSE

> Does Lena currently own the bicycle? TRUE/FALSE

or a two-name exact-choice version when that is more natural.

Gold must be deterministic from the story.

Primary answer format:
- TRUE/FALSE; or
- exactly one of two explicitly named entities.

No explanations in the primary run.

Behavioral accuracy is a **qualification measurement**, not the scientific discovery.

If a model cannot track the explicit state reliably, its activations cannot support a
strong mechanistic interpretation.

---

# 7. Representation checkpoint

Do not extract the main representation immediately on the status-changing verb or
status noun.

After the event, append one short matched neutral continuation, for example an ordinary
time transition that contributes no relevant facts.

The representation checkpoint is taken after this matched neutral continuation and
before the direct query.

Purpose:
- reduce trivial lexical readout of “sold”, “appointed”, “cancelled”, etc.;
- ask what state remains after the event rather than what word was just processed.

Exact checkpoint text must be identical within each matched trajectory set.

---

# 8. Required nuisance crossing

Every status label must occur with both relevant physical states where natural.

Every selected physical state must occur with both status values where natural.

Example ownership:

```
possesses + owns
possesses + does-not-own
does-not-possess + owns
does-not-possess + does-not-own
```

These cells do not need to be shown as a static four-cell table to the model. They are
a material-construction invariant across trajectories.

If the dataset accidentally makes physical possession a proxy for ownership, stop.

---

# 9. Stronger-than-decoding analysis

## 9.1 Domain-specific decodability — diagnostic only

Within-domain status and physical readouts may be measured.

They are not a success criterion.

## 9.2 Leave-one-domain-out status-state transfer

Train any status-state readout only on three domains and evaluate on the fourth.

All person-name assignment, truth labels and physical-state values must be balanced.

This test asks whether anything reusable exists across very different institutional
domains.

A high score is still insufficient by itself.

## 9.3 Event-update geometry

For every trajectory, compute the hidden-state change from a common pre-event
checkpoint to the matched neutral post-event checkpoint.

Compare:
- status-only update deltas;
- physical-only update deltas;
- neutral deltas.

Question:

> Are status-changing deltas systematically aligned/structured across held-out domains
> in a way physical or neutral deltas are not?

The exact metric must be frozen before output.

Do not choose a layer because it gives the prettiest plot.

## 9.4 Generic relation-update control

The core kill control.

Include a shallow set of non-institutional relation updates matched for:
- two named entities;
- one relation change;
- similar story length;
- direct deterministic gold.

Examples can use:
- location;
- physical possession;
- adjacency/placement.

If the same cross-domain representation/update structure appears equally for generic
relations, the IF-specific interpretation fails.

## 9.5 Persistence test

After a social-status update, add one irrelevant physical event that leaves status
unchanged.

Ask whether the discovered status-state signal persists.

Conversely, after a physical update that preserves status, the status-state signal
should remain stable if it genuinely tracks current status.

This is a structural test, not a long-context memory test. Keep the continuation short.

---

# 10. Model strategy

## Behavioral qualification

Three modern open model families.

Freeze exact checkpoints/revisions before output.

Do not do a scale sweep.

## Representation discovery

Use **at most two open models** for IF-P0.

Prefer models for which:
- exact residual-stream extraction is reliable;
- tokenization/checkpoint positions can be reproduced;
- existing project infrastructure is stable.

Do not add a third mechanistic family just for breadth.

---

# 11. Statistics

Independent unit: semantic skeleton.

Required reporting:
- physical-state behavioral accuracy;
- status behavioral accuracy;
- per-domain accuracy;
- leave-one-domain-out transfer;
- update-geometry statistic;
- generic-relation control;
- persistence statistic.

Uncertainty:
- cluster bootstrap over skeletons.

Do not pseudo-replicate over:
- layers;
- tokens;
- queries;
- paraphrases.

Any layer-wise scan must be presented as a layer profile, not dozens of independent
tests.

---

# 12. Pre-output kill gates

Before target output, stop IF-P0 if material audit shows:

1. status and physical state are not independently crossed;
2. gold depends on debatable law/custom rather than the text;
3. status-changing stories require long legal/institutional procedures;
4. one domain can only be instantiated using technical metadata;
5. generic relation controls cannot be made comparably simple;
6. the model can solve a sample by a single explicit status adjective that is absent
   from the matched condition;
7. the final materials require an invented ontology to explain.

---

# 13. Post-output kill rules

Kill IF as a paper identity if any of the following is the best available summary:

1. “LLMs know who owns things.”
2. “Owner/non-owner is decodable.”
3. “Institutional relation labels are linearly separable.”
4. “Status-changing verbs have different representations from physical verbs.”
5. “The signal does not transfer to held-out status domains.”
6. “The signal is matched by generic relation-update controls.”
7. “Factorization disappears when physical state is crossed.”
8. “Only one model family exhibits the structure.”
9. “The result is entirely a generic memory/state-tracking effect.”
10. “The observed law maps directly onto prior relational-concept or rule-applicability
    work in the post-result novelty audit.”

A positive result may earn a new audit only if:
- behavior is qualified;
- at least two model families show compatible structural evidence;
- held-out-domain structure is practically visible;
- generic relation controls are materially weaker/different;
- persistence is compatible with a maintained state rather than a transient lexical
  event signal.

No numerical threshold should be invented after output.

---

# 14. What IF-P0 does NOT authorize

No:
- universal “institutional vector” claim;
- SAE search;
- steering;
- causal patching;
- training;
- LoRA/ReFT;
- long-horizon agent benchmark;
- legal benchmark;
- authorization benchmark;
- 10-domain expansion;
- model scale sweep.

Those become eligible only after IF-P0 yields a non-trivial structural law and that law
survives a fresh novelty assassination.

---

# 15. Freeze checklist

Before any target output:

1. all 24 skeletons finalized;
2. all P/S/N trajectories finalized;
3. physical/status gold unit-tested;
4. generic relation controls finalized;
5. manual naturalness audit completed;
6. exact neutral checkpoint text frozen;
7. exact model revisions frozen;
8. exact activation checkpoint/token definition frozen;
9. analysis code passes dummy-data tests;
10. leave-one-domain-out splits frozen;
11. update-geometry metric frozen;
12. cluster bootstrap frozen;
13. post-output kill rules copied into a dedicated preregistration;
14. commit/tag created.

Only after all 14 items pass may IF-P0 produce target-model outputs.

---

# 16. Strategic relation to CK

CK-P1 remains a valid separately authorized side pilot.

However, IF-P0 has higher current **mainline-selection priority** because:
- IF is a broader durable object;
- multiple outcomes remain useful;
- the method lattice exists independently of one anomaly;
- IF-P0 has now survived a broader conceptual assassination.

This is not a reason to cancel CK.

It is a reason not to let CK's sunk engineering cost determine the next paper.
