# Prospective Llama-3.1-8B behavioral extension

**Created:** 2026-09-03  
**Status:** design written before any Llama output for G8, G11, or G12.

## 1. Scientific question

Does the paper's positive explanatory descent extend to a canonical Meta model
family of comparable scale to the Qwen and Gemma behavioral models?

```text
natural hindsight
    -> foreign-event outcome pull
    -> pull without an explicit verdict
    -> paired control by outcome-supporting evidence
```

This is not an attempt to replace a negative result. Mistral remains in every
original result and the original Qwen/Gemma/Mistral G12 panel verdict remains
`indeterminate`. The extension asks where Llama falls in the already defined
explanatory hierarchy; either result is informative.

## 2. Model and already-observed A1 result

- model: `NousResearch/Meta-Llama-3.1-8B-Instruct`
- revision: `d10aef7999a2b5ba950ab3974312feeedbfe0b77`
- local frozen snapshot: `/home/xiang/.cache/huggingface/hub/models--NousResearch--Meta-Llama-3.1-8B-Instruct/snapshots/d10aef7999a2b5ba950ab3974312feeedbfe0b77`
- tag: `llama31-8b`

This checkpoint was selected in the frozen G4 breadth panel before its output
existed. A1 has already been generated under that design and is **not rerun**.
Its known status is disclosed here: the original two-frame G4 qualification
failed because total boundary accuracy was 0.7363. The failure is asymmetric:
the out-of-set check is 250/256 correct, while the licensed/all-information
check is 127/256. Responsiveness is 45.99pp and hindsight intrusion is +28.23pp
[24.53, 31.85]. No threshold or old verdict is changed.

The new rounds have their own frozen OOB boundary checks and therefore remain
valid prospective tests even though G4's stronger two-frame qualification did
not pass.

## 3. Frozen experiments

Use the exact 256-item artifact, deterministic assignments, prompt builders,
decoding, parsers, estimands, bootstrap, and thresholds already frozen for:

1. **G8 foreign packet** — `src/run_packet_swap.py` and
   `src/analyze_packet_swap.py`;
2. **G11 verdict-redacted foreign packet** — `src/run_redacted_swap.py` and
   `src/analyze_redacted_swap.py`;
3. **G12 paired donor outcome** — `src/run_donor_outcome.py` and
   `src/analyze_donor_outcome.py`.

No prompt, assignment, redaction rule, metric, or threshold is changed for
Llama. Total new volume is 512 + 512 + 1,024 = **2,048 generations**.

## 4. Interpretation fixed in advance

- G8 is `foreign-outcome-pull` only if its inherited qualification and pairing
  validity pass and donor pull is at least 5pp with CI lower above zero.
- G11 is `verdict-independent` only if its inherited `survives` rule passes.
- G12 is `causal-outcome-entrainment`, `practically-null`, or `indeterminate`
  under the original G12 per-model rule, including the 5pp SESOI and recipient-
  aligned validity check.

The **full directional chain** is supported only if all three positive rows
pass. Otherwise Llama locates a boundary between the broader hindsight
phenomenon and a narrower explanatory regularity. Either outcome is reported.

The paper may use Qwen/Gemma/Llama as its canonical cross-family behavioral
backbone for representativeness, but it may not imply that Llama passed G4's
original two-frame qualification if it did not. Mistral remains a disclosed
additional family and its weaker, verdict-dependent directional result is not
deleted or relabeled.

## 5. Freeze checklist

- [x] model/revision fixed by the earlier G4 panel
- [x] known A1 result and qualification failure disclosed
- [x] exact existing G8/G11/G12 builders, estimands, and gates reused
- [x] one extension analyzer added without changing original panel analyzers
- [x] focused tests pass (19/19 including inherited builders)
- [x] three dry audits pass: G8 512 prompts / max 3,964 tokens / pairing
  `a51b80c7…cec1c2`; G11 512 / 3,951 / same pairing / 368 verdict
  sentences removed; G12 1,024 / 4,713 / assignment
  `19ce7ce1…a6c1` / 736 verdict sentences removed
- [x] design commit and tag precede all new Llama generation
