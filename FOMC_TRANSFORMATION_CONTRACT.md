# FOMC temporal transformation contract — candidate v0.1a

**Status: SEALED — pilot ran, did not clear its own preregistered gate
(2026-08-30). No further FOMC work (no prompt changes, no sample
expansion, no re-analysis with different clustering as the primary
metric) is authorized under this document.**

This was written as a genuine qualification gate *before* any FOMC model
output existed, precisely so that a failure could not be argued away
after the fact: "if FOMC fails [the pilot], this source is sealed exactly
as SCOTUS v0.1a was, with no prompt-patching or excerpt tricks to force a
pass" (original text below, retained). The pilot ran under
`g1-fomc-pilot-freeze-v1`: `qualified_models=2/3` (Qwen, Mistral; Gemma
missed only on responsiveness, 11.7 vs the 15-point floor),
`intrusion_pass_models=0/3` under the frozen primary year-clustered
bootstrap, `fomc_temporal_pilot_qualifies=false`. Full results:
`results/fomc_pilot_v1_results.md`.

**The correct scientific reading of this result is `inconclusive /
not validated`, not `effect absent`.** All three models' intrusion point
estimates were positive and of a similar order of magnitude to BTF-3's
confirmed effect (7–11 points here vs. 12.75–27.2 in the BTF-3
confirmatory run); the primary year-clustered analysis — deliberately
the more conservative choice this contract froze to account for FOMC's
real serial dependence — simply did not have enough power at N=24 across
14 distinct years to clear the pre-registered >5-point lower-CI bar. That
the frozen gate was not met is exactly why FOMC is sealed regardless: the
whole point of a preregistered qualification gate is that "the numbers
look promising but didn't quite clear the bar" is not a licensed reason
to keep going. Retroactively expanding to the 21 disjoint CHANGE / 41
disjoint HOLD the census showed were available would spend exactly the
credibility this preregistration process exists to protect.

**Consequence for the paper**: the "confirmed across two natural
sources" contribution is not available. `PREREGISTRATION_G1.md`'s BTF-3
confirmatory result stands on its own (3/3 validity, 100% boundary probe,
fresh 64-unit held-out replication of the pilot's own model pattern) and
remains the project's confirmed empirical core; FOMC is not usable to
broaden it further. The project's next phase
(`PREREGISTRATION_G1_FACTORIZATION.md`) pivots from breadth (more natural
sources) to depth (characterizing and partially mitigating the confirmed
BTF-3 effect itself) rather than attempting a third natural-source
search.

---

**Original status (superseded above):** contract draft, amended before
any candidate queue was built and before any calibration/pilot case was
looked at. No adapter, no formal sample, no model run. Written before any
BTF-3-informed cherry-picking of a second source, and before any FOMC
model output. Phase order for this source: **mechanical audit (done) →
contract (this document) → full pool census (next) → deterministic
candidate queue → human mechanical review → freeze artifact → immutable
tag → 3-model qualification pilot → \[only if that qualifies\] fresh
confirmatory freeze**. The pilot step is a genuine qualification gate,
not a rehearsal — if FOMC fails it, this source is sealed exactly as
SCOTUS v0.1a was, with no prompt-patching or excerpt tricks to force a
pass.

## Amendment note (v0.1 → v0.1a)

Human review of v0.1 caught one substantive labeling bug and three
freedoms that needed locking before the pool census, exactly the kind of
transformation-level correction that must happen before any candidate
selection begins (same discipline as BTF-3's `v0.1 → v0.2` and SCOTUS's
`v0.1 → v0.1a` corrections):

1. **Labeling bug: `realized_change` must not be defined by comparing the
   previous and next *scheduled* statements' ranges.** v0.1's own
   mechanical audit already found that each statement's own verb
   (raise/lower/maintain) states its own action — but the formal
   binarization rule then compared the two scheduled statements' ranges
   instead, which breaks whenever an *intermeeting/emergency* action falls
   between two scheduled meetings. Example: scheduled meeting A holds the
   range at 5.25–5.50; an intermeeting emergency cut lowers it to
   4.75–5.00; scheduled meeting B's own statement says **maintain** at
   4.75–5.00. Range-comparison would score this `4.75–5.00 != 5.25–5.50 →
   CHANGE`, but meeting B itself took no action — it held. **Fixed:
   `realized_change` is now defined solely by the next scheduled meeting's
   own statement verb**, never by comparing two statements' ranges. Range
   comparison is retained only as a secondary consistency-audit check
   (see below), not as the label.
2. **Next-meeting date must not be asserted as pre-known ex-ante
   background.** v0.1 fixed "both meeting dates" into the source context
   available at the ex-ante cutoff, assuming the next meeting's date was
   already public knowledge at the previous meeting. This is usually true
   but requires proving archive-time provenance whenever a meeting was
   historically rescheduled — an unnecessary complication. **Fixed: the
   ex-ante (`OOB`) context supplies only the previous meeting's own date
   and full statement; the next meeting's real date travels with the
   `WITH` packet itself**, not as asserted-known background.
3. **No "possible exclusion" for high-salience meetings.** v0.1's Threat 3
   left the door open to excluding "landmark" meetings from the primary
   sample. **Fixed: mechanically eligible units are never excluded for
   salience.** A descriptive salience flag may be recorded for later
   sensitivity analysis, but it never changes primary-sample membership.
4. **Pilot gate thresholds and sampling rule frozen now, not deferred.**
   v0.1's Scope said only "same kind of criteria as BTF-3" with exact
   numbers "TBD." **Fixed: exact thresholds, the source-qualification
   rule, the bootstrap cluster choice, and a meeting-disjoint sampling
   requirement are frozen below**, before the pool census that determines
   sample size.

All four fixes are recorded in place below, not just in this note, so the
document is internally consistent on its own.

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

Binarization rule, applied per adjacent scheduled-meeting pair — **the
label comes from the next meeting's own statement verb, never from
comparing two statements' ranges** (see the v0.1 → v0.1a amendment note:
range comparison breaks across an intervening intermeeting/emergency
action):

- parse the next scheduled meeting's own statement via the verb-first
  pattern for its own action: `raise` → `realized_change = 1`, `lower` →
  `realized_change = 1`, `maintain` (or equivalent frozen-hold wording,
  e.g. "leave the target range unchanged") → `realized_change = 0`;
- direction sign for pooling: `s = 2 * realized_change - 1` (mirrors
  BTF-3's `outcome_alignment_sign`), i.e. "change" pools like BTF-3's
  realized YES and "hold" pools like realized NO.

**Secondary consistency-audit check, not part of the label:** also
extract the target range from the **previous** meeting's statement and
compare it to the range implied by the next meeting's own statement.
Under normal conditions (no intervening intermeeting action) these should
agree with the verb-based label; a disagreement is a signal to inspect
the unit for an intervening intermeeting/emergency action or an
extraction bug — it does not itself relabel the unit or trigger automatic
exclusion, since intervening intermeeting actions are a real, expected
feature of the historical record, not a data error.

No intermediate/mixed class exists here the way BTF-3 or SCOTUS needed
one (the next meeting's own action is either a raise/lower or a hold) —
the label is unambiguous once that one statement's verb is correctly
extracted.

## Ex-ante cutoff

> All information available as of the previous scheduled meeting's
> statement (its release date/time), strictly before the next meeting.

Concretely: the ex-ante (`OOB`) prompt supplies only the previous
meeting's own date and its complete official statement — nothing dated
after it, and no assertion about when the next meeting will occur or
what it will decide. Fixed under the v0.1 → v0.1a amendment: the task
framing refers only to "the next scheduled FOMC meeting," never a
specific date, so no claim about the next meeting's date being
pre-known ex-ante is ever made or needs proving. The later packet (the
`WITH` cells) is the **next meeting's own statement, carrying its own
real date** — the date arrives with the packet, not as asserted
background available before it.

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

Source context (the previous meeting's date and full statement only —
not the next meeting's date, per the v0.1 → v0.1a amendment) and the
target prediction question's 0–100 answer scale are fixed across all four
cells for a given unit; only the target-information-set framing and
next-statement (with its own real date) presence vary. `Responsiveness`, `OutOfSetIntrusion`, and
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
   Per the v0.1 → v0.1a amendment, **a mechanically eligible unit is never
   excluded for salience** — a high-salience "landmark" meeting may carry
   a descriptive flag for later sensitivity analysis, but that flag never
   removes it from the primary sample.
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

## Scope, sampling rule, and frozen pilot gate

Per the user's own phased plan, this contract authorizes only a
**source-qualification pilot**, not a full confirmatory sample, and its
gate is frozen now rather than deferred to "same kind of criteria as
BTF-3":

### Meeting-disjoint sampling (frozen, not merely "preferred")

**No official FOMC statement may appear in more than one pilot unit.**
Concretely: once a meeting's statement has been used as either the
previous or the next member of a selected unit, no other candidate unit
using that same meeting (in either role) may also be selected. This
removes the sequential-adjacency overlap disclosed in Threat 4 entirely
for the pilot/confirmatory samples, rather than merely "preferring a
spread" as v0.1 said. Implementation: bucket eligible adjacent pairs by
`realized_change` (change / hold), fix a deterministic hash order within
each bucket (same scheme as BTF-3's `deterministic_candidate_queue`).

**Bucket processing order is frozen as CHANGE-first, not left as a free
choice at queue-build time.** The `CHANGE` bucket is walked to completion
first, reserving its selected units' meeting endpoints; only then is the
`HOLD` bucket walked, skipping any candidate whose previous or next
meeting is already reserved (by either bucket). This is not a new rule —
it is the same scarcer-class-first order the pool census itself used to
compute the achievable disjoint maximum — but it must be named explicitly
here as the queue-construction rule too, since `CHANGE` is the scarce
class (29 raw candidates vs. `HOLD`'s 111) and processing `HOLD` first
would silently shrink the achievable disjoint `CHANGE` count below what
the census actually measured. Reject-then-continue during human review
never changes this order: a `CHANGE` candidate that is rejected is simply
skipped in `CHANGE`'s own hash order, never causing a reshuffle into or
out of `HOLD`'s processing.

### Sample size (determined by the pool census, not assumed)

The full pool census (next step, before any candidate queue) determines
the achievable size under the meeting-disjoint constraint. **If the
disjoint pool supports at least 12 CHANGE + 12 HOLD, the pilot is fixed
at 12+12 (N=24) with no further discussion; otherwise use whatever
balanced count the disjoint pool actually supports** (e.g. 8+8, N=16) —
never loosen the binarization, the disjoint constraint, or the eligible-
pool start date to manufacture a larger balanced number.

### Frozen pilot qualification thresholds

| | 12+12 (N=24) | 8+8 (N=16, if the disjoint pool cannot support 12+12) |
|---|---:|---:|
| decision parse rate | ≥ 93/96 | ≥ 62/64 |
| boundary-probe accuracy | ≥ 42/48 | ≥ 28/32 |
| mean responsiveness | ≥ 15 points | ≥ 15 points |
| mean aligned `ALLOWED_WITH` | ≥ 70 | ≥ 70 |
| intrusion pass | bootstrap 95% lower bound > 5 | same |

(Ratios mirror BTF-3's own pilot ratios — `31/32` decisions,`14/16`
boundary probes — scaled to `N=24` → 4 decisions/unit = 96 decisions, 2
probes/unit = 48 probes; and to `N=16` → 64 decisions, 32 probes.)

**Source qualification rule:** at least 2 of 3 models qualify, and at
least 2 of 3 qualified models pass the intrusion criterion — identical
structure to BTF-3's per-family rule, applied here as the FOMC-source
pilot gate.

### Inference details

- 95% percentile cluster bootstrap, 10,000 resamples, seed `20260829`
  (unchanged from BTF-3/SCOTUS);
- **primary bootstrap cluster: the next meeting's calendar year**, not the
  individual meeting-pair. FOMC units have genuine serial dependence
  (Threat 4) that BTF-3's cross-domain forecasting questions do not, so
  treating each meeting-pair as an i.i.d. cluster the way BTF-3 treats
  each `question_id` would understate correlation within a
  Committee-composition/macro-regime period. Clustering by year is a
  coarser, more conservative choice;
- **meeting-pair-level clustering is retained as a secondary sensitivity
  check**, reported alongside the primary year-clustered estimate, not
  as a second primary analysis.

### After the pilot

A fresh, larger confirmatory freeze is authorized only if the pilot
qualifies per the table above. Exact confirmatory-scale thresholds (if
that point is reached) will be scaled from whichever pilot ratio actually
governed (12+12 or 8+8), the same way BTF-3's confirmatory thresholds were
scaled from its own pilot ratios.

No adapter code, no formal sample, and no model run are authorized by this
document alone — the next step is the full pool census described above,
then the deterministic candidate queue.

## Full pool census (2026-08-30, `scripts/fomc_pool_census.py`, `results/fomc_pool_census.json`)

Read-only; no candidate queue was built from this. **v2 methodology,
replacing an initial v1 run that violated this contract's own rules on
two points** (found by the user's own review of the code before any
candidate queue was built, corrected the same day):

- v1 resolved statement URLs by trying suffix `a`, then `b`, then `c`,
  verifying by `<title>` — this is exactly the "guessed suffix" pattern
  the contract explicitly prohibits, even though it happened to find the
  same right answer as v2 below (`monetary20081216b.htm`).
- v1 inferred emergency-meeting status from a text heuristic on each
  minutes page's opening wording, plus two hardcoded exception constants
  (`KNOWN_EMERGENCY_DATES`, `KNOWN_NON_ADJACENT_PAIRS`) — not the
  "derive from the official calendar" rule the contract actually
  requires.

**v2 derives everything structurally from the Fed's own archive page
markup, with no guessing and no hardcoded exceptions.** Direct inspection
of `fomchistorical2008.htm` and `fomchistorical2020.htm` found that each
meeting/action gets its own labeled panel, and the Fed's own heading text
already distinguishes the type: `"January 27-28 Meeting - 2009"` (a
genuine scheduled meeting) vs. `"January 16 Conference Call - 2009"`,
`"March 15 (unscheduled) Meeting - 2020"`, `"March 17-18 (cancelled)
Meeting - 2020"`, `"March 19 (notation vote) - 2020"` — none of which
contain the bare pattern `"... Meeting - {year}"` with nothing else in
parentheses. **A panel is scheduled if and only if its own official
heading matches that bare pattern** — this single structural rule
correctly separates all 4 non-scheduled action types without reading any
statement or minutes text. Each scheduled panel also carries its own
explicit `"Statement"` link (`fomccalendars.htm`, 2021–present, uses an
equivalent `"Statement:"`-labeled row instead) — that link's `href` is
used verbatim as the statement URL, never guessed. Fetching it also
incidentally found the March 2020 cancellation's mechanism directly:
because the panel is officially labeled `"(cancelled)"`, it is excluded
from the scheduled sequence by the same one rule, and `2020-01-29` and
`2020-04-29` become genuinely adjacent in the resulting scheduled-only
sequence — no separate non-adjacency exception is needed.

- **148 scheduled meetings, all time** — the same total v1 found, now via
  structural derivation instead of a minutes-link heuristic plus a
  hardcoded exclusion. `2020-03-15` never enters this list at all (its
  panel heading says `"(unscheduled) Meeting - 2020"`).
- **141 meetings in the eligible pool** (`2008-12-16` onward).
- **140 raw adjacent pairs** — one more than v1's 139, because
  `2020-01-29 → 2020-04-29` is correctly *not* excluded this time (see
  above): under the contract's own "adjacency on the official scheduled
  sequence" definition, it is adjacent. **140 labeled eligible units.**
  `2008-12-16` itself never serves as a "next" meeting (it establishes
  the range rather than raising/lowering/maintaining one), consistent
  with v1.
- **A real, honestly-flagged consequence of including that pair**: its
  secondary consistency check disagrees (previous statement's own range,
  1-1/2 to 1-3/4 percent, vs. the level implied by the next statement's
  own "maintain" action, 0 to 1/4 percent) — because two large
  intermeeting emergency cuts happened between them. Per the frozen rule,
  this is flagged for review, not relabeled and not excluded: the next
  meeting's own statement genuinely says "maintain," so `HOLD` is the
  correct label for what that meeting itself did, independent of how the
  broader context changed around it.
- **Action-verb wording inventory**: `raise` (20), `lower` (9), `maintain`
  (78), `keep` (33), `establish` (1, pool-start only) — six extraction
  methods needed (direct `decided to raise/lower/maintain/keep...`: 106;
  `will maintain/keep...`: 18; `reaffirmed its expectation/view that the
  current...`: 11 combined; `maintain the current X percent...`: 5;
  `establish`: 1) — confirming the reject rule's own premise that a
  single fixed regex is not safe to assume across eras.
- **`CHANGE = 29`, `HOLD = 111`** — confirms the anticipated class
  imbalance (Threat 6): 2009–2014 (ZIRP) and 2021 are entirely `HOLD`;
  `CHANGE` concentrates in 2015–2019 and 2022–2025, often in consecutive
  runs.
- **Secondary consistency audit: 1 flagged mismatch out of 140 units**
  (described above — the 2020 intermeeting-cuts pair), zero unexplained
  mismatches.
- **Meeting-disjoint maximum (`CHANGE` processed first, per the now-explicit
  CHANGE-first rule below): 21 disjoint `CHANGE` units; 41 disjoint `HOLD`
  units remain available afterward.** Identical to v1's figure — the one
  extra `HOLD` unit did not change the achievable disjoint maximum.
- **Pinned source manifest written to `data/external/fomc_source_manifest_v1.json`**
  (141 meetings): date, exact statement URL (verbatim from its official
  archive link), the specific archive page URL that link came from,
  statement-text SHA-256, and the extracted action/range/method — so the
  eventual 24-unit prompt set can be exactly reconstructed even if
  federalreserve.gov's pages change later.

**Result unchanged in substance: the disjoint pool supports 21 CHANGE +
41 HOLD — well above the 12+12 threshold.** Per the Scope section above,
**the pilot is fixed at 12+12 (N=24), no further discussion of 8+8.**

## Freeze checklist

- [x] mechanical source/schema audit (length, extractability, URL and
      calendar reliability)
- [x] target decision, binarization rule (fixed in v0.1a to use the next
      meeting's own action verb, not range comparison), and extraction
      pattern
- [x] ex-ante cutoff and pre-decision/later-packet content (fixed in
      v0.1a: only the previous meeting's date is ex-ante background; the
      next meeting's date travels with its own statement)
- [x] 2×2 structure and metric definitions (inherited from BTF-3, unchanged)
- [x] reject rules
- [x] known threats, including the sequential-adjacency limitation specific
      to this source, and the salience-exclusion door closed in v0.1a
- [x] meeting-disjoint sampling rule frozen (v0.1a), CHANGE-first bucket
      order made explicit (v0.1a census-fix pass)
- [x] pilot qualification thresholds, source-qualification rule, and
      bootstrap cluster choice frozen (v0.1a)
- [x] full pool census derived structurally from official archive markup,
      no guessed suffixes, no hardcoded exceptions (v2, superseding an
      initial v1 run that violated both rules) — `results/fomc_pool_census.json`
- [x] pinned source manifest (date, exact statement URL, source archive
      page, statement-text SHA-256, extracted action/range/method) for
      all 141 eligible meetings — `data/external/fomc_source_manifest_v1.json`
- [x] sample size fixed from the census: **12+12 (N=24)**, confirmed
      supportable (disjoint pool: 21 CHANGE, 41 HOLD available)
- [x] deterministic candidate-queue tooling for the pilot —
      `scripts/fomc_candidate_queue.py` (build-change/freeze-change/
      build-hold/freeze-hold), `src/adapters/fomc_temporal.py`
- [x] boundary-knowledge probe — no separate probe needed: the adapter's
      prompts end with the same `"\n\nTASK\n"` marker BTF-3/SCOTUS use, so
      `run_information_set.py`'s existing generic boundary-probe mechanism
      applies unmodified (packet block is labeled `LATER RESOLUTION
      PACKET` to match its wording)
- [x] human review of the pilot candidates — CHANGE reviewed to 12
      disjoint ACCEPT (quota reached at CHANGE-14, 2 valid ACCEPTs
      mechanically collision-skipped as predicted by the reviewer);
      HOLD reviewed to exactly 12 disjoint ACCEPT (HOLD-1 through
      HOLD-12, no collisions) — `data/external/review/
      fomc_pilot_v1_{change,hold}_reviewed.md`
- [x] frozen 24-unit artifact (12 CHANGE / 12 HOLD), schema + exact-
      transform + meeting-disjoint validated —
      `data/external/review/fomc_temporal_pilot_v1.jsonl`
- [x] pilot qualification result: **FAIL** (2/3 qualified, 0/3 intrusion
      pass) — no larger confirmatory freeze authorized; SEALED, not
      reopenable under this document — `results/fomc_pilot_v1_results.md`
- [x] immutable Git tag before first pilot-run model output: `g1-fomc-pilot-freeze-v1`
