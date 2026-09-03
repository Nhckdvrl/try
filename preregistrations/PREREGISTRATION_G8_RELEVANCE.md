# G8 preregistration — Does the packet have to be about this question?

**Created:** 2026-09-01
**Status:** design frozen. Tag `g8-relevance-design-v1`, before any generation.

---

## 1. The sub-question, and the pair it separates

Sub-question of `PAPER_FRAME.md` §1:

> Does the future evidence move the judgment because of what it says about
> *this* question, or because it is present in the context at all?

G3 made this the sharpest open question in the project. No stated reason
reduces the effect — not a temporal one, not a non-temporal licensing one, not
one that undercuts the packet's truth — and in Gemma, *adding a clause about
the packet* raised the effect by 8 points, just as *removing* the verdict
sentence did in G2 Experiment B. Two manipulations that change how much the
prompt talks about the packet both moved the effect upward.

That pattern has a name in the neighbouring literature — contextual entrainment
— and it makes a prediction the project has never tested.

- **H-content.** The packet moves the answer because it is diagnostic evidence
  about this question. A packet about a *different* question carries no
  information about this one and should move the answer very little, and in no
  systematic direction.
- **H-presence.** What drives the effect is the presence of a confident,
  outcome-shaped block of post-cutoff text in context. A foreign packet is the
  same kind of object and should still move the answer — and, in the strong
  form, should move it toward the *foreign* question's outcome.

These predictions are opposite and cheap to separate.

## 2. The manipulation

Unit *i* keeps its question, resolution criteria, background, target
information set, and task. Only the contents of its `LATER RESOLUTION PACKET`
are replaced, by the packet of a different unit π(i). The section header, its
position, and every out-of-set label are unchanged, so the packet is still
explicitly marked as post-cutoff and still out of set.

π is a **fixed single-cycle derangement** of the frozen artifact's order, seeded
`20260901`, computed in `src/adapters/btf3_packet_swap.py` before any run: no
unit gets its own packet, every packet is used exactly once, and the pairing is
built by construction rather than by rejection sampling. Its SHA-256 digest is
recorded in the freeze report.

The pairing is deliberately **not** stratified by realized outcome. The
analysis needs units whose foreign packet points the opposite way; the resulting
same-direction / opposite-direction cross-tabulation is reported.

### Conditions

| condition | prompt |
|---|---|
| `swap_with` | out-of-set WITH prompt carrying π(i)'s packet |
| `boundary_swap_with` | unchanged boundary probe on that prompt |

The `WITHOUT` cell is the frozen artifact's own `oob_without` — identical text
in every arm, since a swapped packet that is absent is the same absent packet.
The `oob_with` cell is the frozen `temporal` baseline. Neither is re-run.

**Volume:** 3 models × 2 conditions × 256 units = **1,536 generations**.

## 3. Estimands, fixed now

With `s_i` the own-outcome sign and `t_i = s_{π(i)}` the donor's:

```text
I_own    = mean_i s_i ( p_i[swap_with] - p_i[oob_without] )      own-outcome pull
I_donor  = mean_i t_i ( p_i[swap_with] - p_i[oob_without] )      donor-outcome pull
S_swap   = mean_i | p_i[swap_with] - p_i[oob_without] |          undirected movement
S_real   = mean_i | p_i[oob_with]   - p_i[oob_without] |          same, real packet
```

`I_temporal` (the published 16.02 / 27.73 / 7.46) is the reference.

All intervals: 95% percentile cluster bootstrap over `question_id`, 10,000
resamples, seed `20260829`. Qualification per condition: decision parse rate
≥ `248/256`, boundary-probe accuracy ≥ `224/256`.

## 4. Decision rules and the interpretation table

- `I_donor` **positive** if its mean ≥ 5.0 and the 95% CI excludes 0.
- `I_own` **null** if its 95% CI lies within `[−5, +5]`.
- `S_swap` is reported as a fraction of `S_real`; a **substantial** undirected
  movement is `S_swap ≥ 0.5 · S_real`.
- Panel rule: ≥ 2 of 3 qualified models.

| `I_donor` | `S_swap` vs `S_real` | permitted conclusion |
|---|---|---|
| positive | any | **H-presence, strong form.** The model imports an unrelated question's resolution. This would be the single most striking result in the project and would place the phenomenon squarely in the contextual-entrainment family. |
| not positive | substantial | **H-presence, weak form.** A foreign packet moves the answer without pointing anywhere: presence perturbs the judgment even when the content cannot bear on it. |
| not positive | not substantial | **H-content.** The effect requires the packet to be about this question. The G3 amplification pattern then needs an explanation that is not salience, and the paper says so. |

`I_own` is a sanity quantity, not a test: it should be null under every row,
because a foreign packet carries no information about this unit's outcome. A
non-null `I_own` would mean the pairing leaked outcome information and would
invalidate the round; that check is run first and reported first.

## 5. What this does not do

- It does not claim the foreign packet is a "distractor" in the sense of prior
  irrelevant-context work. It is the same kind of object as the real packet —
  confident, post-cutoff, explicitly out of set — differing only in what it is
  about. That is the whole point of swapping rather than inserting noise.
- It does not test random or shuffled text. A single manipulation is run.
- It does not re-select, drop, or re-review any unit, and it re-uses both
  reference cells rather than regenerating them.

## 6. Freeze checklist

- [x] `PREREGISTRATION_G8_RELEVANCE.md` committed
- [x] `src/adapters/btf3_packet_swap.py` committed
- [x] `src/run_packet_swap.py` committed
- [x] `src/analyze_packet_swap.py` committed
- [x] `tests/test_packet_swap.py` committed and passing
- [ ] `g8-relevance-design-v1` tagged
- [ ] first generation only after the tag exists
