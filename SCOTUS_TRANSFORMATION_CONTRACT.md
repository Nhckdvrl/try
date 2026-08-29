# SCOTUS temporal transformation contract — candidate v0.1

**Status:** contract draft. No adapter, no formal sample, no model run.
Written and frozen before any confirmatory-run BTF-3 model output, so this
second-domain source cannot be accused of having been picked or shaped after
seeing how BTF-3 behaved. Phase order for this source is **audit → contract
(this document) → calibration + human review → eligibility/spec freeze**;
this document is the contract step. Two design questions below (§3, §4) are
explicitly *not* fully frozen yet — they name the candidate sources and the
rule for choosing among them, and require a small calibration pass on
real, non-final cases before the extraction rule itself can be locked. That
calibration is part of the human-review step, not a later "improve it once
we see model output" step.

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
| Official oral argument transcript | `supremecourt.gov/oral_arguments/argument_transcripts/{term}/{term}-{docket:05d}.pdf` | candidate pre-decision context source (see §3) |
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

> Information publicly available through the Question(s) Presented /
> cert-grant stage, strictly before oral argument and before decision.

Concretely: everything in the ex-ante prompt must be dated on or before the
`CERT. GRANTED` date shown on the official QP PDF. Nothing derived from
oral argument, the opinion, or any post-argument event may enter the
ex-ante condition. This mirrors BTF-3's `present_date`/`date_cutoff_end`
distinction exactly — a hard, source-encoded boundary, not a judgment call
per case.

## Source-native pre-decision context — NOT YET FROZEN, calibration required

This is the single most important open item, flagged explicitly because
getting it wrong would silently make the task unforecastable (too little
context) or contaminate the ex-ante condition (context secretly sourced
from the opinion). Findings from this session's spot checks:

**QP PDF alone is confirmed insufficient.** Verified content for real
cases (e.g. docket 06-179, *Riegel v. Medtronic*): the QP PDF gives only
case caption, `DECISION BELOW` citation, `LOWER COURT CASE NUMBER`, the
question presented, and the cert-grant date — a bare citation, not a
description of what the lower court actually held. A model given only this
cannot ground a reverse/affirm prediction in the lower court's own posture,
exactly the failure mode flagged in advance: *"如果只有抽象法律问题，而完全
不知道 lower-court posture，模型根本没法预测 affirmed/reversed。"*

**SCDB's own `lcDisposition`/`lcDispositionDirection` fields are
REJECTED as a fix, not adopted** — this is a real finding from this
session, not a hypothetical concern. SCDB's own codebook
(`scdb.la.psu.edu/online-codebook/lower-court-disposition/`) states the
coding rule verbatim: *"We adhere to the language used in the 'holding' in
the summary of the case on the title page **or prior to Part I of the
Court's opinion**."* That means these fields are coded by SCDB researchers
reading the Supreme Court's own opinion — i.e., they are derived from
**post-decision** text, even though the underlying fact (what the lower
court did) itself predates cert grant. Using them as "pre-decision context"
would silently leak an opinion-derived summary into the ex-ante condition,
exactly what the contract must not do. **Do not use `lcDisposition` /
`lcDispositionDirection` for prompt construction.** They remain usable
only for post-hoc SCDB-side bookkeeping such as reporting ideological
direction in the eventual results, not for building any prompt.

**Oral argument transcripts are officially hosted, pre-decision-dated
(argument date always precedes decision date), and government-produced**
— confirmed real and downloadable back through Term 2007 (spot-checked
docket 06-179, argued 2007-12-04, decided 2008-02-20). But **one live
spot-check shows the opening statement does not reliably restate the
lower-court posture**: counsel in the sampled case (*Riegel*) opened
directly with the legal question and the parties' competing statutory
readings, never explicitly stating what the Second Circuit held below.
A fixed rule like "first N lines of petitioner's opening" is therefore
**not yet safe to freeze** — it may or may not surface the needed posture
depending on how a given advocate chose to open, and that is exactly the
kind of per-case variability the mechanical-extraction discipline in this
project is meant to avoid deciding by hand.

**Required next step before any candidate queue is drawn:** a calibration
pass reading 10–15 real, deliberately non-final cases (not drawn from the
eventual candidate pool, so looking at them does not bias selection) to
determine which of the following actually delivers a self-contained,
purely-pre-decision, mechanically-extractable "lower court posture" block:

1. QP PDF alone (already shown insufficient by itself);
2. a fixed-length prefix of the oral argument transcript (needs testing —
   does a longer fixed window, e.g. through the first Justice interruption
   plus the next full answer, reliably surface the posture, or does it
   remain advocate-dependent even then?);
3. some other officially-hosted, pre-decision-dated document not yet
   checked this session (e.g. the cert petition itself, if freely hosted;
   not verified in this session).

Only after that calibration produces one fixed, mechanical extraction rule
(applied identically to every case, never hand-tuned per case) does this
section become frozen. This is analogous to BTF-3's own `v0.1 → v0.2 →
v0.2r2` process, where the transformation adapter itself went through
review-driven correction before the artifact was usable — the difference
is that here the correction happens before any candidate is drawn, not
after a rejected packet is found.

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
later resolution packet:

| target information set | no syllabus | syllabus supplied |
|---|---|---|
| Ex ante: through cert-grant / QP stage | `OOB_WITHOUT` | `OOB_WITH` |
| Retrospective: all supplied information | `ALLOWED_WITHOUT` | `ALLOWED_WITH` |

Same question (the QP's question presented) and same 0–100 answer scale
fixed across all four cells; only the target information set and syllabus
presence vary. `Responsiveness`, `OutOfSetIntrusion`, and
`BoundarySelectivity` are computed exactly as defined in
`BTF3_TRANSFORMATION_CONTRACT.md`, with `s = 2r - 1` for `r` = binarized
reverse/affirm outcome from `caseDisposition` above.

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
- the opinion/syllabus cannot be stably matched to the case's SCDB
  citation (e.g. per curiam disposition with no full syllabus, or a
  citation that resolves to more than one distinct opinion document);
- the case's consolidated-docket mapping to outcome is not unique (i.e.
  the citation-organized row does not correspond to exactly one syllabus);
- the calibrated pre-decision-context extraction rule (§3, once frozen)
  does not yield a self-contained, unambiguous lower-court posture for
  this case — reviewer marks REJECT rather than supplementing by hand;
- the syllabus extraction boundary (§4) cannot be located cleanly (e.g.
  OCR damage severe enough to lose the NOTE/Held/disposition structure);
- the question presented was, in substance, already resolved by the time
  of cert grant (e.g. mooted by intervening events) — analogous to BTF-3's
  "question was already resolved by present_date" rule;
- the case requires legal interpretation to decide the binary label (i.e.
  `caseDisposition` alone does not cleanly answer reverse-vs-affirm without
  a judgment call) — if the mapping in the taxonomy table above needs
  interpretation for a specific case, reject rather than adjudicate it;
- any safety/privacy concern (unlikely for SCOTUS case law, but the rule
  is retained for consistency with BTF-3 and FANToM).

## What remains source-native

- question presented: copied verbatim from the official QP PDF;
- decision-below citation and lower-court case number: copied verbatim;
- pre-decision context block (once §3 is calibrated): extracted by a fixed
  rule from an official, pre-decision-dated government document, never
  paraphrased or summarized by the adapter;
- later packet: the complete official syllabus, verbatim, including its
  own disclaimer boilerplate;
- output remains a 0–100 probability, matching BTF-3's answer scale.

The adapter adds only section labels, target-time framing, and a parseable
answer instruction — the same discipline as BTF-3's adapter.

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
4. **Pre-decision context adequacy (specific to SCOTUS, see §3):** until
   the calibration pass locks a rule, there is a live risk that the chosen
   context source under- or over-supplies information relative to what a
   real ex-ante forecaster would have had.
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
- [ ] pre-decision context extraction rule calibrated on 10–15 non-final cases (§3)
- [x] later-packet (syllabus) extraction rule identified and verified against two real, 70-years-apart samples
- [x] 2×2 structure and metric definitions (inherited from BTF-3, unchanged)
- [x] reject rules
- [ ] boundary-knowledge probe drafted (mirrors BTF-3's, not yet written)
- [ ] human review of an actual 8–12 case pilot sample
- [ ] eligibility/spec freeze (this document becomes citable as frozen only after the two unchecked items above close)
