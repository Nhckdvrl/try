# FOMC temporal transformation contract — candidate v0.1

**Status:** contract draft. No adapter, no formal sample, no model run.
Written and frozen before any BTF-3-informed cherry-picking of a second
source, and before any FOMC model output. Phase order for this source:
**mechanical audit (done) → contract (this document) → small
source-qualification pilot (8+8 or 12+12) → \[only if that qualifies\]
fresh confirmatory freeze**. This document is the contract step. The pilot
step is a genuine qualification gate, not a rehearsal — if FOMC fails it,
this source is sealed exactly as SCOTUS v0.1a was, with no prompt-patching
or excerpt tricks to force a pass.

## Why FOMC, and what it is not for

The BTF-3 confirmatory replication (`g1-btf3-confirmatory-freeze-v1`)
confirmed temporal information-set intrusion on a fresh, 64-unit,
held-out sample: 3/3 models qualified, 2/3 (Qwen, Gemma) showed intrusion
clearing the SESOI, replicating the pilot's own pattern. The live risk is
no longer "does this effect exist" but **"is this specific to BTF-3's
event-forecasting-question construct?"** FOMC is chosen because it is a
genuinely different decision process from BTF-3, not a relabeled version
of the same one:

- BTF-3: heterogeneous real-world forecasting questions, sourced from a
  forecasting-tournament corpus, with a machine-generated (partially
  spot-checked) resolution explanation as the later packet.
- FOMC: a single, recurring, real institutional decision (the target
  federal funds range), made by the same body on a fixed public schedule,
  with the later packet being the Committee's own verbatim, official,
  human-drafted statement — not a forecasting question at all.

If both sources show the same "explicitly out-of-scope later evidence
still moves the ex-ante judgment" pattern, that is evidence the temporal
intrusion finding generalizes across genuinely different decision
domains, not just within one forecasting-dataset construct. It does
**not** unlock the `PREREGISTRATION_G1.md` mechanism gate, which requires
validated intrusion in **at least two families** (boundary types —
temporal, perspective, procedural), not two sources within the temporal
family. FOMC is pursued to strengthen the temporal-generalization claim,
not to reach mechanism work.

ForecastBench was deliberately not re-tried here: it is itself an
event-forecasting corpus, structurally too close to BTF-3 to answer the
"is this just a BTF-3-shaped artifact" question even if it had passed its
earlier schema audit (which it did not — see `DATA_AUDIT.md` and the
project's ForecastBench scouting notes).

## Mechanical audit (complete, before this contract was drafted)

Performed against real official `federalreserve.gov` statements sampled
across Term-equivalent eras 2008–2025 (12 real meeting dates), read-only,
no adapter:

- **Length: no problem.** Real statements run ~370–620 words (~500–800
  tokens) each. A two-statement prompt (previous + next, plus framing) is
  nowhere near the `max_model_len=8192` ceiling that killed SCOTUS.
- **Target-range wording: stable and mechanically extractable.** From
  December 16, 2008 (the range era's start: "establish a target range for
  the federal funds rate of 0 to 1/4 percent") through September 17, 2025,
  every sampled statement uses the same verb-first pattern: *"the
  Committee decided to **raise**/**lower**/**maintain** the target range
  for the federal funds rate ... to/at X to Y percent."* The verb alone
  gives the change/hold label; no interpretation is required.
- **Pre-December-2008 meetings are out of scope by construction**: before
  the range era, the Committee targeted a single rate, not a range, so the
  extraction pattern above does not apply and older meetings are excluded
  by the eligible-pool start date rather than by a per-case judgment call.
- **Real gotcha #1 — statement URLs cannot be safely guessed.** The usual
  pattern is `federalreserve.gov/newsevents/pressreleases/monetary
  {YYYYMMDD}a.htm`, confirmed working for 11 of 12 real meeting dates
  tested. The exception: `monetary20081216a.htm` resolves to an unrelated
  same-day press release (a $150B TAF auction-results announcement); the
  actual FOMC statement for that date is `monetary20081216b.htm` (title:
  "FOMC statement"). Crisis-era dates can carry multiple same-day
  releases sharing the date prefix. **Statement URLs must be resolved
  from the official calendar/historical index pages (which explicitly
  label each link as the FOMC statement), never guessed from a date and a
  suffix letter.**
- **Real gotcha #2 — scheduled vs. emergency/intermeeting actions are not
  self-identifying.** Both of the 2020 intermeeting emergency actions
  checked (March 3 and the Sunday March 15 cut, both before the regularly
  scheduled March 17–18, 2020 meeting) carry the identical generic title
  ("Federal Reserve issues FOMC statement") as any regular scheduled
  meeting. **Scheduled-meeting eligibility must be checked against the
  official scheduled-meeting calendar
  (`federalreserve.gov/monetarypolicy/fomccalendars.htm` and the
  historical-materials page for older years), never inferred from the
  statement text itself.**

Neither finding is fatal — both have a concrete, always-applicable fix
(resolve from the official index, cross-check the official calendar) —
unlike SCOTUS's context-length wall, which had none. This is why FOMC
proceeds to a contract instead of being sealed.

## Target decision (binarized outcome)

> Probability that the target federal funds range will change at the next
> scheduled FOMC meeting, rather than stay the same.

Binarization rule, applied per adjacent scheduled-meeting pair:

- extract the target range stated in the **previous** meeting's statement
  and the target range stated in the **next** meeting's statement, both
  via the verb-first pattern above;
- `realized_change = 1` if the next statement's range differs from the
  previous statement's range (any direction, any size);
- `realized_change = 0` if the ranges are identical;
- direction sign for pooling: `s = 2 * realized_change - 1` (mirrors
  BTF-3's `outcome_alignment_sign`), i.e. "change" pools like BTF-3's
  realized YES and "hold" pools like realized NO.

No intermediate/mixed class exists here the way BTF-3 or SCOTUS needed
one (a target range either matches the previous one exactly or it does
not) — the label is unambiguous once the two ranges are correctly
extracted, which is exactly why the extraction-rule discipline above
matters so much.

## Ex-ante cutoff

> All information available as of the previous scheduled meeting's
> statement (its release date/time), strictly before the next meeting.

Concretely: the ex-ante prompt supplies the previous meeting's date and
its complete official statement, and nothing dated after it except the
bare fact that another scheduled meeting is coming (the meeting calendar
itself is public well in advance and is not a leak of the *outcome*, only
of the *timing* — the next meeting's date is treated as source-native
background, not as the later packet). The later packet is specifically
the **next meeting's statement content**, not the fact that a meeting will
occur.

## Independent unit and pre-decision / later-packet content

- **Unit** = one adjacent scheduled-meeting pair (previous meeting,
  next meeting).
- **Pre-cutoff context** (source-native, verbatim): the previous
  meeting's complete official statement text, plus its date.
- **Later packet** (source-native, verbatim): the next meeting's complete
  official statement text, plus its date. Used whole — no excerpting to a
  single sentence, matching the same "use the complete instrument, don't
  hand-pick the useful part" discipline SCOTUS's syllabus rule and BTF-3's
  `resolution_explanation` rule both use, and consistent with FOMC
  statements already being short enough (per the mechanical audit above)
  that no truncation question exists in the first place.
- The **target prediction question** is fixed and adapter-authored, held
  byte-identical across all four cells and every unit — not the previous
  statement's own content — mirroring the SCOTUS v0.1a fix that separated
  source legal context from the fixed target question: *"What probability
  should be assigned that the target federal funds range will change at
  the next scheduled FOMC meeting, rather than stay the same? Return only
  one number from 0 to 100."*

## 2×2 structure

| target information set | no next statement | next statement supplied |
|---|---|---|
| Ex ante: through the previous meeting, before the next meeting | `OOB_WITHOUT` | `OOB_WITH` |
| Retrospective: all supplied information | `ALLOWED_WITHOUT` | `ALLOWED_WITH` |

Source context (previous statement, both meeting dates) and the target
prediction question's 0–100 answer scale are fixed across all four cells
for a given unit; only the target-information-set framing and next-
statement presence vary. `Responsiveness`, `OutOfSetIntrusion`, and
`BoundarySelectivity` are computed exactly as defined in
`BTF3_TRANSFORMATION_CONTRACT.md`, with `s = 2 * realized_change - 1`.

## Boundary probe

Mirrors BTF-3's and SCOTUS's: at the evaluation point defined above, is
the next meeting's statement part of the target information set? OOB
target expects `NO`; retrospective target expects `YES`.

## Source instruments

| instrument | URL pattern | role |
|---|---|---|
| FOMC scheduled-meeting calendar | `federalreserve.gov/monetarypolicy/fomccalendars.htm` (recent/current years), `federalreserve.gov/monetarypolicy/fomc_historical.htm` (older years) | authoritative list of scheduled meeting dates — never inferred from a statement |
| Official FOMC statement | `federalreserve.gov/newsevents/pressreleases/monetary{YYYYMMDD}{suffix}.htm`, suffix resolved from the calendar/index page, never guessed | pre-cutoff context and later packet |

## Reject rules (mechanical, checked per candidate unit before any run)

Reject a candidate meeting-pair if any of the following holds — no
exceptions, no hand-repair, no resampling once a unit has been reviewed:

- either meeting in the pair is not on the official scheduled-meeting
  calendar (excludes intermeeting/emergency actions and any notation-vote
  action not tied to a scheduled meeting — per the audit, this cannot be
  inferred from the statement text and must be checked against the
  calendar);
- either meeting predates December 16, 2008 (single-target-rate era, no
  "target range" to extract);
- the statement URL for either meeting cannot be resolved from an
  official calendar/index page (no guessed date+suffix combination is
  accepted as a substitute);
- the target range cannot be extracted from either statement via the
  frozen verb-first pattern (e.g. unusual wording not matching
  raise/lower/maintain — flag for manual review rather than force a
  regex match);
- the previous and next meeting are not genuinely adjacent on the
  official calendar (i.e. a meeting was skipped, rescheduled, or a
  scheduled meeting was itself later converted to an emergency/off-
  calendar action — verify calendar adjacency explicitly, do not assume
  it from date arithmetic alone);
- the next meeting's statement had not actually been released as of the
  point the unit is being drawn (i.e. the "next" meeting is still in the
  future relative to dataset construction) — this excludes the single
  most recent scheduled meeting from ever being a valid "previous" member
  of a pair until its own next meeting has occurred;
- any safety/privacy concern (retained for consistency with BTF-3 and
  SCOTUS; not expected to trigger for FOMC statements).

## What remains source-native

- previous meeting's date and complete official statement: copied
  verbatim;
- next meeting's date and complete official statement (the later packet):
  copied verbatim;
- the target prediction question is the one adapter-authored, fixed-string
  element, exactly analogous to BTF-3's and SCOTUS's fixed task line.

The adapter adds only section labels, target-time framing, and the fixed
target prediction question.

## Known threats

1. **Task-time manipulation:** as with BTF-3/SCOTUS, a retrospective
   judgment is not identical to a live forecast, even though the question
   and scale are fixed — a deliberate, honestly-described eligibility
   manipulation.
2. **Direct answer disclosure:** the next statement's verb
   (raise/lower/maintain) states the outcome explicitly; this is the
   intended mechanism, not a bug, matching BTF-3's and SCOTUS's own
   later-packet design.
3. **Parametric contamination:** a target model may already know how a
   famous, heavily-covered meeting resolved (e.g. the December 2008 cut
   to the zero lower bound, the first 2015 hike, the March 2022
   tightening-cycle start) from pretraining. The within-target contrast
   (`OOB_WITH` vs `OOB_WITHOUT`) helps isolate the causal effect of the
   packet's in-prompt presence but cannot fully rule out prior knowledge
   of the outcome — identical caveat to BTF-3's and SCOTUS's Threat 3.
   High-salience "landmark" meetings should be flagged for possible
   exclusion or separate reporting during the qualification pilot.
4. **Sequential adjacency between neighboring units:** because meetings
   occur on a fixed recurring schedule (~8/year), consecutive candidate
   units share a statement — meeting *k*'s statement is the later packet
   for unit *(k-1, k)* and the pre-cutoff context for unit *(k, k+1)*.
   This does not create any leakage risk for a single model generation
   (each prompt is independently sampled; the model has no memory across
   prompts within a run), but it does mean neighboring units are not
   fully independent draws of the underlying economic/political
   environment (same Committee composition, same macro regime) the way
   BTF-3's cross-domain forecasting questions are. This is disclosed as a
   limitation on the independent-unit assumption, analogous to BTF-3's own
   "one-sided natural outcome" threat, not a reason to exclude any
   specific unit; the qualification-pilot and confirmatory samples should
   be drawn to avoid unnecessary adjacency overlap where the pool size
   allows (e.g. preferring a spread across years over an unbroken run of
   consecutive meetings) without being asked to force strict
   non-overlap that the natural 8-per-year cadence cannot support at
   larger sample sizes.
5. **Instruction compliance:** a separate boundary-knowledge probe (above)
   is required to check the model actually distinguishes next-statement
   eligibility under the ex-ante vs. retrospective framing.
6. **Class imbalance risk:** unlike BTF-3 and SCOTUS, "hold" (no change)
   is likely to be the majority class over the full 2008–present window,
   especially during extended pause periods (e.g. 2009–2015,
   2020–2022 near-zero period, various 2023–2025 pause stretches).
   The eligible pool's actual change/hold balance must be counted before
   any sample-size commitment (see "Scope" below) — do not loosen the
   binarization or extraction rule to manufacture balance if the natural
   pool is skewed.

## Scope

Per the user's own phased plan, this contract authorizes only:

1. **A source-qualification pilot of 8+8 or 12+12** (change/hold),
   deterministic candidate-queue selection from the eligible pool
   (December 16, 2008 onward, scheduled meetings only, reject rules
   above), reviewed with the same mechanical-gate discipline as BTF-3's
   confirmatory queue, run against the same three frozen checkpoints
   (`Qwen/Qwen3.5-9B`, `google/gemma-3-12b-it`,
   `mistralai/Mistral-Small-24B-Instruct-2501`).
2. Before drawing that pilot, **count the actual eligible pool's
   change/hold balance** (December 16, 2008 – present, scheduled meetings
   only, adjacent pairs, minus any pairs failing the reject rules) and
   report it plainly; if natural balance cannot support 12+12, use
   whatever balanced count the pool actually supports (e.g. 8+8) rather
   than changing the binarization to force a larger number.
3. **A fresh, larger confirmatory freeze is authorized only if this pilot
   qualifies** on the same kind of validity/intrusion criteria used for
   BTF-3 (utility/parse rate, boundary-probe accuracy, non-zero
   `OutOfSetIntrusion` with a cluster-aware interval excluding the SESOI)
   — exact confirmatory-scale thresholds to be defined at that point,
   analogous to how BTF-3's confirmatory thresholds were scaled from its
   own pilot ratios.

No adapter code, no formal sample, and no model run are authorized by this
document alone — the next step is drawing and reviewing the 8+8/12+12
qualification-pilot candidates.

## Freeze checklist

- [x] mechanical source/schema audit (length, extractability, URL and
      calendar reliability)
- [x] target decision, binarization rule, and extraction pattern
- [x] ex-ante cutoff and pre-decision/later-packet content (no cutoff/
      context conflict this time — the "next statement" is unambiguously
      post-cutoff by construction, unlike SCOTUS v0.1's first draft)
- [x] 2×2 structure and metric definitions (inherited from BTF-3, unchanged)
- [x] reject rules
- [x] known threats, including the sequential-adjacency limitation specific
      to this source
- [ ] eligible-pool change/hold balance actually counted
- [ ] deterministic candidate-queue tooling for the 8+8/12+12 pilot
- [ ] human review of the pilot candidates
- [ ] pilot qualification result (go/no-go for a larger confirmatory freeze)
- [ ] immutable Git tag before first pilot-run model output
