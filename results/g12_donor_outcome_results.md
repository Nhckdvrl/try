# G12 — paired donor-outcome intervention

Frozen design: `g12-donor-outcome-design-v1`. Each of 256 historical
questions was evaluated twice. The recipient question and every non-packet
token were identical; only a verdict-redacted foreign packet was replaced,
from evidence supporting a realized NO to evidence supporting a realized YES.

| model | parsed pairs | boundary acc. | YES donor − NO donor (pp) | preregistered verdict |
|---|---:|---:|---:|---|
| Qwen3.5-9B | 256 | 100% / 100% | +4.41 [1.27, 7.55] | indeterminate |
| Gemma-3-12B-IT | 255 | 100% / 100% | +17.50 [14.76, 20.33] | causal outcome entrainment |
| Mistral-Small-24B | 256 | 100% / 100% | +1.55 [0.55, 2.55] | practically null (<5pp SESOI) |

The frozen panel rule requires at least two qualified, validity-passing models
in the same non-indeterminate row. It therefore returns **indeterminate**:
Gemma passes the 5pp causal-entrainment gate, Mistral satisfies the practical
null rule, and Qwen misses the 5pp magnitude threshold; Qwen's recipient-aligned
validity interval also exceeds its equivalence band by 0.16pp at the upper end.
No threshold or gate was changed after observing output.

The continuous result is nevertheless scientifically informative and must be
reported separately from that categorical gate: the paired contrast is
positive with a 95% interval above zero in all three models. Thus changing the
outcome supported by an irrelevant future packet predictably changes the
direction of the same reconstructed judgment, while the magnitude is strongly
model-dependent (1.55–17.50pp). The large Gemma effect licenses the next
mechanism question: whether semantically unrelated packets form a shared,
causally transferable internal outcome variable.

Source: `results/g12_donor_outcome_analysis.json`; three raw files in
`results/raw/isr_*_g12_donor_outcome.jsonl` (1 metadata + 1,024 records each).
