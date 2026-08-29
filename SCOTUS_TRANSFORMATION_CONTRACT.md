# SCOTUS temporal transformation contract — candidate v0.1a

**Status:** contract draft, amended before any calibration case was looked
at. No adapter, no formal sample, no model run. Written and frozen before
any confirmatory-run BTF-3 model output, so this second-domain source
cannot be accused of having been picked or shaped after seeing how BTF-3
behaved. Phase order for this source is **audit → contract (this document)
→ calibration + human review → eligibility/spec freeze**; this document is
the contract step. One design question below ("Source-native pre-decision
context") is explicitly *not* fully frozen yet — it names the candidate
context and the empirical question calibration must answer, but not a
per-case extraction algorithm. That calibration is part of the
human-review step, not a later "improve it once we see model output" step.

## Amendment note (v0.1 → v0.1a)

Human review of v0.1 caught two internal contradictions before any
calibration case was read, exactly the kind of transformation-level bug
that must block the whole artifact even before source-level review begins
(same discipline as BTF-3's own `v0.1 → v0.2` corrections):

1. **Cutoff/context conflict.** v0.1 defined the ex-ante cutoff as
   "through the Question(s) Presented / cert-grant stage" while
   simultaneously naming the oral argument transcript — which is dated
   *after* cert grant, at argument — as the leading candidate for
   pre-decision context in its "Source-native pre-decision context"
   section. Under v0.1's own cutoff, the transcript would already be
   out-of-set information and could never legally appear in
   `OOB_WITHOUT`/`OOB_WITH`. **Fixed by moving the cutoff itself to the
   oral-argument stage** (below), which makes the QP and the full official
   transcript both legitimately ex-ante, and removes any need for a
   fragile "first N lines" extraction rule — the calibration question
   becomes whether `QP + complete transcript` is adequate, not whether a
   truncated slice of it is.
2. **Task-question conflict.** v0.1's target decision was frozen as a
   reverse/affirm probability, but the 2×2 section said all four cells
   held "the same question (the QP's question presented)" — a substantive
   legal question, not a probability question. These cannot both be the
   fixed prompt question. **Fixed by separating source context (the QP's
   question presented, copied verbatim) from the target prediction
   question (the frozen reverse/affirm probability question), with the
   latter — not the QP's legal question — held fixed across all four
   cells.**

Both fixes are recorded in place below, not just in this note, so the
document is internally consistent on its own.

## Why SCOTUS, and what it is not for

The G1 pilot (`g1-pilot-freeze-v1.2`) validated intrusion in the temporal
family (BTF-3) but not the perspective family (FANToM), which failed
qualification before intrusion could even be assessed. SCOTUS is being
added as a **second temporal-boundary source**, chosen specifically because
its domain — predicting a judicial disposition before a Supreme Court
decision — is about as far from event forecasting as a temporal-boundary
task can get while still being the same boundary type. If both BTF-3 and
SCOTUS show the same "explicitly out-of-scope later evidence still moves
the ex-ante judgment" pattern, that supports:

> temporal information-set intrusion generalizes across radically different
> decision domains (event forecasting and judicial disposition prediction).

It does **not**, on its own, support:

> multiple kinds of information-set boundaries all fail.

That broader claim would need a second boundary *type* (e.g. a working
perspective or scope replacement for FANToM), which this document is not
about. Every metric, threshold, and inference rule below inherits G1's
temporal-family definitions unchanged; SCOTUS is a replication of the
temporal family, not a new family.

## Source instruments (all confirmed reachable, read-only, this session)

| instrument | URL pattern | role |
|---|---|---|
| Supreme Court Database (SCDB) | `scdb.la.psu.edu` (codebook), case-level CSV/data release | outcome + join keys + case metadata |
| Official "Question(s) Presented" PDF | `supremecourt.gov/qp/{term}-{docket:05d}qp.pdf` | pre-decision question + decision-below citation |
| Official oral argument transcript | `supremecourt.gov/oral_arguments/argument_transcripts/{term}/{term}-{docket:05d}.pdf` | pre-decision context, used whole (see "Source-native pre-decision context") |
| Official slip opinions | `supremecourt.gov/opinions/slipopinion/{term}` | later packet, current/recent terms not yet bound |
| Official bound U.S. Reports volumes | `supremecourt.gov/pdfs/USReports/USREPORTS-{vol}_PDFA.pdf` | later packet, older terms already bound (through Vol. 587 / 2018 Term) |

**Docket-number URL bug found and fixed during this audit:** the QP and
opinion URL patterns require the docket number zero-padded to 5 digits
after the term-year prefix (e.g. docket `06-179` → `06-00179`). Naive
`{term}-{docket}qp.pdf` 404s even though the file exists at
`06-00179qp.pdf`. Verified against 10 real dockets spanning Term
2007 (`06-00179`, `06-00571`, `06-00043`) through Term 2024 (`23-00477`,
`22-07466`) — all 10 resolved with the zero-padded form. Any script touching
this source must zero-pad before requesting.

## Target decision (binarized outcome)

> Probability that the Supreme Court will reverse or vacate the judgment
> below, rather than affirm it.

This is not picked by assumption; it is audited against SCDB's
`caseDisposition` (Spaeth `DIS`) 11-value taxonomy, fetched directly from
`scdb.la.psu.edu/online-codebook/disposition-of-case/`:

| value | label | class |
|---:|---|---|
| 1 | stay, petition, or motion granted | **exclude** — procedural, not a merits disposition |
| 2 | affirmed (includes modified) | **AFFIRM** |
| 3 | reversed | **REVERSE** |
| 4 | reversed and remanded | **REVERSE** |
| 5 | vacated and remanded | **REVERSE** |
| 6 | affirmed and reversed (or vacated) in part | **exclude** — mixed disposition |
| 7 | affirmed and reversed (or vacated) in part and remanded | **exclude** — mixed disposition |
| 8 | vacated | **REVERSE** |
| 9 | petition denied or appeal dismissed | **exclude** — not a merits ruling on the judgment below |
| 10 | certification to or from a lower court | **exclude** — procedural |
| 11 | no disposition | **exclude** |

Binary resolution is therefore `{2} → 0 (AFFIRM)`, `{3,4,5,8} → 1
(REVERSE)`; every other value is excluded from eligibility, matching the
instruction to drop mixed dispositions in the first version rather than try
to force them into a binary label.

**Additional automatic exclusion:** SCDB's `caseDispositionUnusual`
(Spaeth `DISQ`) flags (value `1`) cases where "the Court made an unusual
disposition... which does not match the coding scheme of the preceding
variable" (`scdb.la.psu.edu/online-codebook/unusual-disposition/`). Any
case with `caseDispositionUnusual = 1` is excluded regardless of its
`caseDisposition` value — the taxonomy mapping above is not reliable for
those cases by SCDB's own documentation.

**Consolidated-docket rule:** SCDB's codebook explicitly warns "in cases
containing multiple docket numbers, not every docket number will
necessarily receive the same disposition," and separately documents that
`docketId` splits one opinion across its consolidated dockets (verified
live example: SCOTUS docket 24-345 lists 7 consolidated lower-court
dockets under one citation). **Use the citation-organized table (one row
per `caseId`), not the docket-organized table**, so one independent unit
= one opinion with one disposition, not one row per consolidated docket
number.

## Ex-ante cutoff

> All official information publicly available through the oral argument /
> transcript stage, strictly before the Court's decision.

Concretely: everything in the ex-ante prompt must be dated on or before the
oral argument date shown on the official transcript (i.e., the QP and the
complete official oral argument transcript are both in-set). Nothing
derived from the opinion or any post-argument event may enter the ex-ante
condition. This is a deliberately later cutoff than v0.1's cert-grant
stage, chosen specifically so the richest genuinely-official pre-decision
document (the transcript) is legitimately available rather than sitting
just past the boundary — the boundary is set at "oral-argument-time
information vs. later official syllabus," which is still a hard,
source-encoded temporal boundary and still structurally the same kind of
information-set split as BTF-3's `present_date`/`date_cutoff_end`, just
drawn at a later natural checkpoint in this domain's own timeline.

## Source-native pre-decision context

**Frozen as of v0.1a: verbatim QP text + the complete official oral
argument transcript, used whole — no truncation, no "most relevant
excerpt," no per-case hand-selection.** This resolves the deeper problem
found under the old cert-grant cutoff:

**QP PDF alone is confirmed insufficient.** Verified content for real
cases (e.g. docket 06-179, *Riegel v. Medtronic*): the QP PDF gives only
case caption, `DECISION BELOW` citation, `LOWER COURT CASE NUMBER`, the
question presented, and the cert-grant date — a bare citation, not a
description of what the lower court actually held. A model given only this
cannot ground a reverse/affirm prediction in the lower court's own
posture, exactly the failure mode flagged in advance: *"如果只有抽象法律问题，
而完全不知道 lower-court posture，模型根本没法预测 affirmed/reversed。"*

**SCDB's own `lcDisposition`/`lcDispositionDirection` fields are
REJECTED as a fix, not adopted** — this is a real finding from this
session, not a hypothetical concern, and holds regardless of where the
cutoff is drawn. SCDB's own codebook
(`scdb.la.psu.edu/online-codebook/lower-court-disposition/`) states the
coding rule verbatim: *"We adhere to the language used in the 'holding' in
the summary of the case on the title page **or prior to Part I of the
Court's opinion**."* That means these fields are coded by SCDB researchers
reading the Supreme Court's own opinion — i.e., they are derived from
**post-decision** text, even though the underlying fact (what the lower
court did) itself predates cert grant. Using them as pre-decision context
would silently leak an opinion-derived summary into the ex-ante condition.
**Do not use `lcDisposition` / `lcDispositionDirection` for prompt
construction.** They remain usable only for post-hoc SCDB-side bookkeeping
such as reporting ideological direction in the eventual results, not for
building any prompt.

**Why "complete transcript," not an extraction rule:** under the old
cert-grant cutoff, a spot-check of docket 06-179's opening statement showed
counsel diving straight into the legal argument without restating the
lower-court holding — exactly the kind of per-case variability that makes
a fixed "first N lines" rule unsafe. Moving the cutoff to oral-argument
time removes the need to solve that problem: the *entire* official,
government-produced transcript (confirmed real and downloadable back
through Term 2007; spot-checked docket 06-179, argued 2007-12-04, decided
2008-02-20) is legitimately in-set, so nothing needs to be selectively
extracted from it. The calibration question is no longer "can we
mechanically find the posture in the first few lines" but the simpler and
more empirical:

**Required calibration pass (10–15 real, deliberately non-final cases,
not drawn from the eventual candidate pool so looking at them does not
bias selection), to answer:**

1. Does `QP + complete official transcript` reliably give enough
   information — across the transcript as a whole, not just the opening —
   for the lower-court posture and case facts to be recoverable, so the
   reverse/affirm task is genuinely forecastable rather than a guess?
2. Is the transcript consistently and officially available (not just for
   the one spot-checked docket) across the full Term 2007–present window,
   and consistently dated before the decision?
3. Is transcript length manageable for the target models' context budget
   (BTF-3 used `max-model-len 8192`; a full oral argument transcript is
   often 40–60 pages of transcribed speech, i.e. plausibly much longer
   than BTF-3's prompts) — if not, this is a real constraint the
   calibration pass must surface, not silently work around by truncating
   (which would reopen the extraction-rule problem this amendment removed).

If the calibration pass shows `QP + complete transcript` does not reliably
work (e.g. context budget is the blocker, or the transcript genuinely
lacks recoverable posture in some non-trivial fraction of cases), that is
reported honestly and this contract does not proceed to a candidate queue
on the current design — it does not fall back to a hand-tuned excerpt rule
just to make the calibration pass "succeed."

## Later packet: the official syllabus

Use the complete official syllabus, from the Reporter of Decisions'
boilerplate note through the disposition line — a single, non-hand-picked,
rule-defined block, not an extracted "most useful sentence."

Confirmed structure (verified independently in a 1955-Term bound volume
and a 2026 slip opinion — same wording 70 years apart):

> "NOTE: Where it is feasible, a syllabus (headnote) will be released, as
> is being done in connection with this case, at the time the opinion is
> issued. The syllabus constitutes no part of the opinion of the Court but
> has been prepared by the Reporter of Decisions for the convenience of the
> reader. See United States v. Detroit Timber & Lumber Co., 200 U.S. 321,
> 337."

The extraction rule: **the packet is the text from this NOTE (inclusive)
through the end of the syllabus's disposition sentence** (the syllabus
concludes with an explicit disposition, e.g. "Reversed and remanded.",
following a "Held:" line and numbered reasoning points). This block is
short, self-contained, explicitly labeled as separate from the merits
opinion by the Court's own disclaimer, and structurally the closest match
to BTF-3's `resolution_explanation`. It should never be hand-edited or
selectively excerpted below the full syllabus-block boundary.

For older bound-volume terms, note the confirmed OCR layer (ABBYY
FineReader, not raw scans) — extraction should tolerate minor OCR spacing
noise but must not silently "clean up" wording, per the same no-silent-repair
principle as BTF-3.

## 2×2 structure

Identical in form to BTF-3, with the syllabus playing the role of the
later resolution packet. Two distinct things must not be conflated here,
per the v0.1 → v0.1a fix:

- **Source legal context** (varies by case, copied verbatim, never
  altered by the adapter): the QP's question presented, case caption,
  decision-below citation, and the complete oral argument transcript.
  This is background, analogous to BTF-3's `question` /
  `resolution_criteria` / `background` fields — it is what the model
  reads, not what it is asked.
- **Target prediction question** (fixed, identical string across every
  case and every one of the four cells): *"What probability should be
  assigned that the Supreme Court will reverse or vacate the judgment
  below, rather than affirm it? Return only one number from 0 to 100."*
  This is the one thing that must be held byte-identical across all four
  cells for a given case — not the QP's legal question, which is source
  context, not the prompted task.

| target information set | no syllabus | syllabus supplied |
|---|---|---|
| Ex ante: through oral argument, before decision | `OOB_WITHOUT` | `OOB_WITH` |
| Retrospective: all supplied information | `ALLOWED_WITHOUT` | `ALLOWED_WITH` |

The source context (QP + transcript) and the target prediction question's
0–100 answer scale are fixed across all four cells for a given case; only
the target information set framing and syllabus presence vary — exactly
BTF-3's discipline of holding `question`, `resolution_criteria`,
`background`, and the answer scale fixed while only the target-information-
set framing and packet presence change. `Responsiveness`,
`OutOfSetIntrusion`, and `BoundarySelectivity` are computed exactly as
defined in `BTF3_TRANSFORMATION_CONTRACT.md`, with `s = 2r - 1` for `r` =
binarized reverse/affirm outcome from `caseDisposition` above.

## Reject rules (frozen, mechanical, checked per case before any run)

Reject a candidate case if any of the following holds — no exceptions, no
hand-repair, no resampling once a case has been reviewed:

- `caseDisposition` is not in `{2, 3, 4, 5, 8}` (affirm/reverse-class only;
  mixed and procedural dispositions excluded per the taxonomy above);
- `caseDispositionUnusual = 1`;
- the case is original-jurisdiction (no lower court, so no ex-ante
  reverse/affirm question is meaningful);
- the QP PDF cannot be retrieved, or is not clearly the pre-decision
  version (e.g. it has been superseded by a later QP revision after
  argument — check for an "AMENDED" or later-dated QP note);
- the official oral argument transcript cannot be retrieved for this case,
  or exceeds the target models' context budget even after accounting for
  the rest of the prompt (see the context-length calibration question
  above) — reject rather than truncate;
- the opinion/syllabus cannot be stably matched to the case's SCDB
  citation (e.g. per curiam disposition with no full syllabus, or a
  citation that resolves to more than one distinct opinion document);
- the case's consolidated-docket mapping to outcome is not unique (i.e.
  the citation-organized row does not correspond to exactly one syllabus);
- `QP + complete transcript` does not yield a self-contained, unambiguous
  lower-court posture for this case — reviewer marks REJECT rather than
  supplementing by hand or reaching for an outside source;
- the syllabus extraction boundary ("Later packet: the official syllabus")
  cannot be located cleanly (e.g.
  OCR damage severe enough to lose the NOTE/Held/disposition structure);
- the question presented was, in substance, already resolved by the time
  of oral argument (e.g. mooted by intervening events) — analogous to BTF-3's
  "question was already resolved by present_date" rule;
- the case requires legal interpretation to decide the binary label (i.e.
  `caseDisposition` alone does not cleanly answer reverse-vs-affirm without
  a judgment call) — if the mapping in the taxonomy table above needs
  interpretation for a specific case, reject rather than adjudicate it;
- any safety/privacy concern (unlikely for SCOTUS case law, but the rule
  is retained for consistency with BTF-3 and FANToM).

## What remains source-native

- question presented, case caption, decision-below citation, and lower
  court case number: copied verbatim from the official QP PDF;
- pre-decision context: the complete official oral argument transcript,
  used whole, never excerpted, paraphrased, or summarized by the adapter;
- later packet: the complete official syllabus, verbatim, including its
  own disclaimer boilerplate;
- the target prediction question itself is not source-native — it is the
  one adapter-authored, fixed-string element, exactly analogous to BTF-3's
  fixed "What probability should be assigned..." task line, which is also
  adapter-authored rather than source text.

The adapter adds only section labels, target-time framing, and the fixed
target prediction question — the same discipline as BTF-3's adapter, which
also holds its own fixed task line apart from the source-native question,
criteria, and background.

## Known threats (parallel to BTF-3's threat list)

1. **Task-time manipulation:** as with BTF-3, retrospective judgment is not
   identical to a live forecast, even though the question and scale are
   fixed — a deliberate, honestly-described eligibility manipulation.
2. **Direct answer disclosure:** the syllabus's "Held:" line states the
   disposition explicitly, giving strong allowed-condition leverage; this
   is the intended mechanism, not a bug, matching BTF-3's own packet design.
3. **Parametric contamination:** a target model may already know how a
   famous case (e.g. a landmark or heavily-covered case) came out from
   pretraining. The within-target contrast (OOB_WITH vs OOB_WITHOUT) helps
   isolate the causal effect of the packet's presence in-prompt but cannot
   fully rule out prior knowledge of the outcome — identical caveat to
   BTF-3's Threat 3. High-salience "landmark" cases should be flagged for
   possible exclusion or separate reporting during the calibration pass.
4. **Pre-decision context adequacy and length (specific to SCOTUS, see
   the pre-decision-context section):** until the calibration pass
   confirms it, there is a live risk that `QP + complete transcript`
   under-supplies recoverable lower-court posture in some cases, or that
   full transcripts routinely exceed the target models' context budget —
   either finding blocks the design rather than being worked around by
   truncation.
5. **Instruction compliance:** as with BTF-3, a separate boundary-knowledge
   probe (not yet drafted) is required to check the model actually
   distinguishes syllabus eligibility under the ex-ante vs retrospective
   framing, mirroring BTF-3's `BOUNDARY CHECK` probe.
6. **One-sided natural outcome:** each case has only its realized
   disposition; pooling direction-aligns realized reverse/affirm outcomes
   exactly as BTF-3 pools realized YES/NO.
7. **Docket zero-padding:** a purely mechanical risk, but a real one found
   this session — any script touching this source must zero-pad docket
   numbers to 5 digits or it will silently 404 instead of erroring loudly;
   any fetch code for this source should assert on non-200 responses
   rather than treating a 404 as "case not available."

## Scope for the pilot

Consistent with the recommendation to test this source small before
committing engineering effort at BTF-3's confirmatory scale: **first
SCOTUS round is an 8–12 case pilot** (not 64), reviewed with the same
mechanical reject rules above, run against the same three frozen
checkpoints (`Qwen/Qwen3.5-9B`, `google/gemma-3-12b-it`,
`mistralai/Mistral-Small-24B-Instruct-2501`) used for BTF-3, before any
larger confirmatory commitment. Cases are drawn only from **Term
2007–present** (the range over which every source instrument above was
verified reachable in this session); a pre-2007 slice is out of scope for
this contract and would need separate sourcing work.

## Freeze checklist

- [x] disposition taxonomy audited against SCDB and mapped to a binary label
- [x] mixed/procedural dispositions identified and excluded
- [x] consolidated-docket join risk identified and resolved (citation-organized table)
- [x] official source instruments verified reachable, docket zero-padding bug found and documented
- [x] ex-ante cutoff and pre-decision context source are mutually consistent (v0.1a fix)
- [x] target prediction question separated from source-native QP legal question (v0.1a fix)
- [ ] `QP + complete transcript` calibrated on 10–15 non-final cases: adequacy and context-length checks (pre-decision-context section)
- [x] later-packet (syllabus) extraction rule identified and verified against two real, 70-years-apart samples
- [x] 2×2 structure and metric definitions (inherited from BTF-3, unchanged)
- [x] reject rules
- [ ] boundary-knowledge probe drafted (mirrors BTF-3's, not yet written)
- [ ] human review of an actual 8–12 case pilot sample
- [ ] eligibility/spec freeze — this document becomes citable as frozen only
      after all three unchecked items above close: the calibration pass,
      the boundary probe, and the pilot-sample review
