# BTF-3 packet factuality audit v1 — result

**Protocol:** `PROTOCOL_BTF3_PACKET_FACTUALITY_AUDIT.md`, frozen with its
subsample under tag `g2-packet-factuality-audit-protocol-v1` **before any
citation was opened**. Scoring: `results/btf3_factuality_audit_v1.json`.

## Provenance

| items | auditor | access |
|---|---|---|
| YES-1 … YES-14, YES-16, YES-18 (16) | Claude Opus 5 | live web search + page fetch |
| remaining 48 | ChatGPT (GPT-5.6 Sol, OpenAI) | external lookup; commit `736c7fa` |

Neither auditor opened any file under `results/raw/`, and neither modified the
frozen sample or the 256-unit artifact — commit `736c7fa` touches the verdict
ledger and nothing else. The scorer, which does read model outputs for the
secondary sensitivity analysis, was run on the project side only after the
audit closed, keeping the auditors' no-outputs rule intact.

The first 16 were audited by the same model that produced the selection
review, so that block is a with-lookup re-check rather than an independent
audit; the remaining 48 were audited by a different vendor's model and are
independent of both the selection review and this repository's tooling.

## Result

| verdict | count |
|---|---|
| PASS | **63** |
| MATERIAL_ERROR | **1** |
| UNVERIFIABLE | **0** |

`E = 1 ≤ 2`, so the preregistered rule does **not** trigger expanded review.
Material-error rate 1/64 = 1.56%, Clopper–Pearson exact 95% CI
**[0.04%, 8.40%]**.

## The one material error

`bd90f010-…` (YES-31), Western Balkans Reform and Growth Facility.

The question asks for a disbursement announced **between June 5 and June 19,
2026**. Its own resolution criteria set the window as **on or after May 12**
through June 19. The packet resolves YES on a **May 20** release
(EC IP/26/1106, €158.9m to Albania, Montenegro, North Macedonia) — inside the
criteria window, outside the window stated in the question.

Two points matter for how this is reported:

1. **It is outcome-changing, not cosmetic.** Under the question's own window
   the packet cites no qualifying release, so the recorded YES depends on which
   text binds. That is why it was scored MATERIAL_ERROR rather than logged as a
   date slip.
2. **It is a specification defect, not a fabrication.** The packet did not
   invent an event: the May 20 disbursement is real and correctly cited, and
   the packet explicitly flags the discrepancy in its own text before choosing
   the criteria. The defect is a self-contradictory source item.

The failure therefore sits on the *criteria unambiguous* gate of the selection
review, not on the *exact packet factually valid* gate — and it is precisely
the kind of defect a review without external lookup can still catch in
principle, since both texts were in front of the reviewer. That is worth one
honest sentence in the limitations rather than a claim that the audit
vindicated the review.

## Secondary sensitivity (descriptive only)

Recomputing `OutOfSetIntrusion` over the 256 minus the single flagged unit:

| model | preregistered primary | excluding the flagged unit |
|---|---|---|
| Qwen3.5-9B | 16.02 [14.18, 17.89] | 15.92 [14.02, 17.80] |
| Gemma-3-12B-it | 27.73 [25.15, 30.39] | 27.65 [25.04, 30.27] |
| Mistral-Small-24B | 7.46 [5.41, 9.57] | 7.59 [5.54, 9.68] |

Nothing moves materially, and nothing here replaces the primary estimate: the
subsample is defined by a post-output audit and is reported as robustness only.
The 256-unit membership is unchanged, as the protocol requires.

## Wording for the paper

Permitted: *"A preregistered audit of a hash-fixed 64-item subsample, conducted
with external source lookup and without access to model outputs, returned 63
PASS, 1 material error, and 0 unverifiable items (1/64; exact binomial 95% CI
[0.04%, 8.40%]), which did not trigger the preregistered expanded review. The
single material error is a question/criteria window contradiction rather than a
fabricated event; excluding it moves no model's estimate materially."*

Forbidden: any claim that factual validity was *established*. The exact upper
bound is 8.4%; this audit shows that expanded review was not triggered, not
that the packets are sound.
