# Second lead — making an outcome less explicit makes it harder to ignore

**Status:** unconfirmed discovery, held for a single clean prospective test. It is
**not** part of the current paper and no work on it is scheduled. It becomes a
paper only if the test below replicates; if it does not, it is killed rather than
reinterpreted.

## 1. The observation

In G2 Experiment B the explicit YES/NO verdict sentence was removed from a
resolved event's own future packet, and hindsight contamination went **up** in
every model. The preregistration's interpretation table did not contain this
direction; it was recorded as `unanticipated` at the time.

`HC` is the shift the packet causes in a judgment the model has been told to make
from an earlier information set, sign-aligned to the realized outcome.

| model | `HC_direct` (verdict present) | `HC_red` (verdict removed) | difference | leak-free subset |
|---|---|---|---|---|
| Qwen3.5-9B | 16.02 | **23.35** | **+7.33 [5.80, 8.88]** | **+8.09 [6.50, 9.81]** |
| Gemma-3-12B | 27.73 | **34.55** | **+6.91 [5.21, 8.69]** | **+7.23 [5.35, 9.25]** |
| Mistral-Small-24B | 7.46 | **10.18** | **+2.72 [1.25, 4.19]** | **+3.22 [1.58, 4.87]** |

Two things make this more than a curiosity:

- **The packet does not lose evidential value.** Under the licensed frame the
  redacted packet's leverage is 45.3–47.2, against 47.27 for the unredacted one in
  Qwen. Removing the verdict costs the packet nothing and costs the model's defence
  a great deal.
- **It is not the redaction leak.** 34/256 redacted packets still assert the outcome
  (`preregistrations/POSTHOC_REDACTION_AUDIT_CORRECTION.md`). Those units make the
  redacted condition behave *more* like the unredacted one, so they attenuate the
  contrast — and indeed the effect is larger on the 221–222 leak-free units.

## 2. What may and may not be claimed

**May be claimed, on this evidence:**

> Removing the explicit outcome statement makes later evidence *more* influential,
> not less.

**May not be claimed, on this evidence:**

> The model gates the label rather than the information.

That is a mechanistic hypothesis, and the manipulation does not isolate it.
Redaction simultaneously changes the explicit verdict, the packet length, the
position of the remaining text relative to the task, the presence of
conclusion-shaped language, and how obviously the block reads as a post-hoc
summary. The `LATER RESOLUTION PACKET` header is also still present in both
conditions.

It is also not enough to say models are sensitive to labels; that is already
studied. The candidate novelty is only the counterintuitive direction:

> **Making an outcome less explicit can make it harder to ignore.**

## 3. The single experiment that would settle it

Everything below must be preregistered and frozen before any generation. Do not
reuse the regex redactor, and do not reuse the current prompt template.

**Materials.** A fresh set of resolved forecasting items whose packets are
**evidence-only by construction and independently audited**, not produced by
deleting sentences from an existing packet. Each item gets one evidence body,
written once, containing no resolution statement.

**Conditions.** The explicit outcome statement is the only manipulated variable:

| condition | packet |
|---|---|
| `verdict` | evidence body + a standardized explicit verdict sentence |
| `matched` | evidence body + a length- and position-matched sentence that states no outcome and no direction |

Both conditions therefore have identical evidence, identical length to within a
tolerance fixed in advance, and the added sentence in the same position. This
removes every confound listed in §2 except the header.

**Header control.** Run the same pair with and without the `LATER RESOLUTION
PACKET` header, so that "the model discounts what is marked as post-hoc" is tested
rather than assumed.

**Framing.** Replace the engineered information-set contract with natural
instructions:

> *Imagine you are making this forecast on 4 May 2026. Use only what was known by
> then.*

No `TARGET INFORMATION SET`, no `date_cutoff_end=`, no restatement of the answer to
the boundary probe inside the prompt it probes. If a recognition measure is kept,
it must not be answerable by copying a sentence of the prompt.

**Prediction.** `HC(matched) > HC(verdict)`, with a preregistered SESOI and a
panel rule fixed in advance.

**Decision rule.** If it replicates, it is a paper of its own about the direction.
If it does not, this lead is closed. There is no third option in which the design
is adjusted until it works.

## 4. Why this is not defensive work

The experiment is not a control added to protect an existing claim. It is the first
time the intended variable — the presence of an explicit outcome statement — is
actually isolated, and the first time the task is stated naturally. The current
result is a by-product of an instrument built for a different purpose.

## 5. Artifacts

- `results/g2_hindsight_depth_results.md` — the frozen Experiment B result,
  including its `unanticipated` direction note.
- `results/btf3_redaction_leakage_audit.json` — leak audit and leak-free
  re-estimates.
- `preregistrations/PREREGISTRATION_G2_HINDSIGHT_DEPTH.md` — original frozen design.
- `preregistrations/POSTHOC_REDACTION_AUDIT_CORRECTION.md` — why the redactor may
  not be reused.
