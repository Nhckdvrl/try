# G12 preregistration — Does an irrelevant donor outcome causally set the direction of the pull?

**Created:** 2026-09-01. No target-model output may be generated before this
design, builder, runner, analyzer, audit, and tests are committed and tagged.

## 1. Scientific question

G8 assigned one random foreign resolution packet to each recipient question.
G11 removed explicit verdict sentences and found donor-directed pull survived
in two of three models. Those results estimate direction across recipients. G12
turns donor outcome into a direct within-recipient intervention:

> Holding the historical question and every non-packet token fixed, does
> replacing irrelevant future evidence for a NO outcome with irrelevant future
> evidence for a YES outcome causally raise the reconstructed past probability?

This is the decisive behavioral test of **retrospective outcome entrainment**.

## 2. Construction

Every one of the frozen 256 recipient questions receives two packets:

- a packet from a realized-YES donor question;
- a packet from a realized-NO donor question.

Both packets undergo G2's frozen mechanical explicit-verdict redaction before
insertion. The recipient's question, criteria, background, target information
set, packet header, and task are byte-identical between the two prompts. Each
of the 128 YES and 128 NO donor packets is used exactly twice. Assignments are
deterministic (`seed=20260901`), never use the recipient's own packet, and never
reuse that recipient's frozen G8 donor. No target-model output participates.

Conditions: `redacted_donor_yes`, `redacted_donor_no`, and the unchanged
out-of-set boundary probe for each. Volume: 3 models × 256 units × 4 records =
**3,072 generations**.

## 3. Estimands

For recipient `i`:

```text
C_i = p_i(redacted donor YES) - p_i(redacted donor NO)
C   = mean_i C_i
A   = mean_i |C_i|
```

`C` is primary. `A` describes effect heterogeneity and carries no decision
rule. The recipient-aligned contrast `mean_i s_i C_i` is a validity check: its
95% CI must lie inside `[-5,+5]`, because donor assignment is independent of the
recipient's realized outcome.

Inference: paired 10,000-draw cluster bootstrap over recipient question ID,
seed `20260829`. Per-condition parse floor `248/256`; boundary accuracy floor
`224/256`.

## 4. Frozen decision rule

Per qualified model:

- **causal outcome entrainment:** `C >= 5.0` and its 95% CI lower bound is above
  zero;
- **practically null:** the 95% CI for `C` lies inside `[-5,+5]`;
- otherwise **indeterminate**.

Panel conclusion requires at least 2 of 3 qualified, validity-passing models in
the same non-indeterminate row.

If causal outcome entrainment passes, the permitted claim is:

> The outcome supported by an irrelevant future evidence packet causally sets
> the direction of its influence on a reconstructed past judgment, even after
> explicit verdict sentences are removed.

If it fails, G8/G11 remain valid but the paper may not describe donor outcome
as a within-recipient causal variable.

## 5. Why this advances the paper

This is not a defence against copying; G11 already addresses that. It upgrades
the scientific object from a directional association under random packet swap
to an orthogonalized causal factor. A positive result supplies the behavioral
variable for the next and only licensed mechanism question: whether unrelated
packets share a causally transferable internal outcome representation.

## 6. Freeze checklist

- [x] preregistration written
- [x] builder, runner, analyzer, and tests written
- [x] tests and dry-run pass
- [ ] design commit and tag precede first generation

Frozen dry-run audit: 256 units, 1,024 prompts, maximum prompt length 4,978
tokens, 736 explicit-verdict sentences removed, 38 packets mechanically
unchanged, assignment SHA-256
`19ce7ce190ab88b11ece52fe332934d64555a8f71133196e1b223d657e51a6c1`.
