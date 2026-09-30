# G33: final, prospective attempt to identify an independent contribution

Frozen before any G33 research-model outputs. This is a discovery/diagnostic
experiment, not an independent confirmation of a newly established law.

## Question and novelty obligation

Does a request to decide as if excluded X had never been encountered disengage
still-admissible grounds E, beyond the effect of asking the same question with
X redacted? Can this make a seemingly good exclusion policy a worse decision
policy than ordinary direct exclusion?

Self-Blinding (Christian & Mazor, 2026) already establishes failures to restore
never-seen judgments and compares ignore and hypothetical-self instructions.
Hypothetical Consistency already studies predicting one's other-context answer.
Compared to What? (2026) already argues for matched counterfactual prompt controls.
G33 cannot claim any of those distinctions or simply rename their findings.
The only candidate advance here is a reproducible *content-dependent cost to
valid-ground use* and a resulting conflict between local exclusion performance
and actual decision quality. An ordinary hypothetical-query main effect,
model-specific wording sensitivity, or residual excluded influence is insufficient.

## Material, size, and selection

200 fresh, non-numeric-threshold claim families from real Wikipedia revision
pairs in the pinned VitaminC release. Exclude every claim and case found in
historical material/candidate pools. Mechanically screen then choose the first
200 passing families in a seeded, pre-output order, at most one per Wikipedia
page. Two different OpenCode free models perform row-level construction and
independent source-plus-paraphrase auditing. Auditors do not see research outputs
or the other auditor's judgments. Reject unclear omissions, overlap, spelling-only
changes, broken text, ambiguous referents, and non-faithful adaptations.

E+/E- retain natural source text with surface cleanup only. X+/X- are faithful
experimental paraphrases of the corresponding source E; they are not independent
real-world observations and must not be presented as authentic quotations.
This intentionally makes relevance explicit. E and X polarity are independently
crossed. Evaluate the claim using the record as authoritative, not real-world
truth inferred from a possibly vandalized revision. Report the construction and
rejection inventory, original lines, all model audits, hashes, and selected IDs.

200 independent claim/page clusters matches ConfB's material breadth and exceeds
Self-Blinding's 65 independent scenarios (its attributes are not independent
scenarios). It does not guarantee sensitivity to a five-point difference: an
unpaired proportion's worst-case 95% half-width is about seven points at n=200.
The paired factorial estimate can be sharper, depending on disagreement. A null
is not equivalence, and we will report interval bounds rather than declare perfect
control. The breadth is chosen for a substantial behavioral distinction, not to
turn arbitrarily small effects into a publishable claim.

## Frozen matrix and readout

Three models: Qwen3-8B, Gemma3-12B, Mistral-Small-24B. Two independently written
wordings, fixed before inference, no selection by model performance.

Record-only main substrate: E in {support,refute}, crossed with query D (current
direct verdict), C (as-if-never-seen verdict, E explicitly retained), S (predict a
fresh copy's answer given the clean permitted context). For every query, X is
redacted, supportive, or refuting. Add clean B and active-X A+/A- calibration.
12 cells per E and wording; 9,600 rows per model. All currently admissible records
are explicitly permitted, including X in A; this fixes G32's scope ambiguity.
No initial admissibility or initial model judgment is enacted; these are
single-rendering exclusion tests, not a demonstrated retraction-history effect.

Same-material no-E open-world bridge: same queries, X states, wordings, B/A,
background knowledge permitted; 4,800 rows/model. This checks whether the earlier
restoration shape survives on new natural material and a new readout. It is not a
replication of ConfB's numeric estimand and cannot rescue a failed main result.
Total 43,200 binary decisions. Constrain generation to one-token TRUE/FALSE;
record greedy verdict and normalized binary next-token probability. These are
format-controlled choices, not claimed calibrated belief probabilities.

Implementation and exact wording: scripts/run_g33_final.py. Cell codes DC+/DC-
mean direct query with content present; CC+/CC- mean as-if query; SC+/SC- mean
fresh-self query. FD/FC/FS are corresponding redacted frames.

## Estimands and decision

For record-only cells, correctness uses E's audited support/refute relation.
For q=D,C,S: content cost G_q = accuracy(F_q) - mean accuracy(qX+,qX-).
Primary interaction H = G_C-G_D. Compute this at the item level, average E and
wordings, bootstrap claim clusters (10,000 resamples, seed 20260930).
Also report H by wording, G_S-G_D, frame query costs, excluded-X absolute and
signed polarity effects, and E probability leverage. Legal-ground verdict flips
relative to same-item B and disagreement with E are actual decision consequences.
No correctness label is imposed on active cells with conflicting E and X.

A viable substrate requires clean B accuracy >=80% and E probability leverage
>=0.50 in at least two models. Otherwise interpretation is limited by record use.
A candidate independent story requires H>=5 percentage points with cluster CI
lower bound >0 in at least two models, positive H under *both* frozen wordings
in those models, and as-if X absolute probability sensitivity no worse than
D by more than 0.02. Report stronger ranking reversal only if as-if actually
reduces excluded-X sensitivity while degrading legal accuracy. Meeting numerical
criteria does not automatically establish novelty: the final scientific judgment
must show the conditional result exceeds the strongest prior's actual contrast.

If only no-X query effects, one-model/one-wording effects, ordinary direct leakage,
or a more effective instruction appear, close the current research line as lacking
an independent novel narrative. Preserve reliable old observations as assets;
no automatic G34, mechanism, LoRA, or new benchmark. Opposite and null outcomes
constrain this hypothesis; they are not relabeled as a new discovery. Exploratory
analyses must be explicitly labeled and cannot change this rescue criterion.

## Operational amendments before full inference (2026-09-30)

Free-provider timeouts/connection resets interrupted several construction and audit
calls. Retain every attempt; use a recovery provider (OpenCode's free Muse Spark
1.3 contributor model) with exactly the same instructions and schema. Every
canonical independent audit still uses a different model from its item's
constructor. Provider recovery follows file completeness and availability, never
acceptance rate or research-model behavior. Provenance names the actual provider.
Stalled original schedulers were stopped before recovery to avoid concurrent
canonical-file writes. Late attempt files remain artifacts, not silently substituted
for the selected canonical reviews. Selection requires a completed contiguous
candidate prefix, preventing quicker later batches from bypassing earlier items.

One fixed candidate (`g33_0001`) supplies a format-only smoke matrix for each
checkpoint. It does not change the predeclared selection order, is not selected
by performance, and smoke rows are excluded from all scientific estimates.
The original Mistral shim's cache links were broken. Restore the **same pinned
revision** `9527884be6e5616bdd54de542f9ae13384489724` in an isolated local cache,
using the committed recovery script; do not substitute another model. Exact
checkpoint metadata hashes and execution deviations will be retained.

Before full inference, add the original source page/topic to E's displayed record
metadata. Auditors already receive that topic, and many natural source sentences
use pronouns or “the film”; the research model must receive the same referent
context used to validate the pair. This adds no factual answer or publication
credentials. All record-only cells, including B and frames, receive the same topic.
The no-E bridge remains claim-only apart from its exclusion/query manipulation.
The earlier format smoke lacks this metadata line and remains format-only; no
cell outcomes were inspected to choose the change.

### Material challenge amendment, before full inference

A seeded 16-family manual inspection of the tentative selection found important
false refutations that the first two passes missed (different sunniest city vs
relative sunlight, different university vs ever attending, different DNA in one
test vs use in any test), plus alias/scope and review-category ambiguities.
**The tentative 200 file is not the final frozen dataset.** Add a source-only
objection audit to every provisionally eligible family, using the same exact-claim
criterion and no X, prior judgments, or research outputs. This is a separate
blind pass; it is not necessarily a third distinct provider for each family.
Require its roles to match, with decisive/clear_scope/readable all true. Keep
explicit outcome-blind manual exclusions with reasons. Source topic metadata
remains part of E. Select the first 200 passing ALL filters; expand the seeded
source prefix if needed rather than lowering quality or N. No research-model
output motivates these exclusions; the only completed runs remain format smokes.
Source-only instructions: data/items/g33_final/SOURCE_CHALLENGE.md.

Reserve expansion: append candidates 600–799 from the identical seeded source
sequence. The first 600 candidates, source hashes, historical exclusion pool, and
all decisions on them remain unchanged and are checked programmatically. This
expansion responds to stricter material screening and the fixed N=200 target,
not to research-model outputs. Selection may freeze once the first 200 fully
accepted families are known and every earlier potentially eligible candidate has
a completed challenge; incomplete *later* candidates cannot affect that boundary.
Pending challenge rows are unassessed, not material rejections.

### Actual-choice safeguard, before full inference

Also report item-wise X-induced TRUE/FALSE disagreement, not just normalized
probability displacement. A ranking reversal requires C's binary X sensitivity
to be no more than D+0.02, in addition to the original probability safeguard.
Otherwise shrinking probabilities toward a decision threshold could leave or
increase actual X-controlled verdicts: that would not establish successful local
non-use with collateral damage. This tightens the candidate criterion before
outputs and requires no extra cells. It is not a new rescue branch.

Execution resource amendment, before full inference: other users' jobs expanded
into previously available cards. Do not stop them. Limit sequence concurrency to
32 and batch tokens to 2048; choose a memory fraction appropriate to currently
free memory, without changing weights, precision, inputs or decoding. Device UUID
startup in vLLM 0.11 is unsupported; retain its failure log and use verified numeric
IDs. Smoke logs record device-allocation failures, not scientific outcomes.

### Runtime reporting repair after startup (no outcome analysis)
The first full runs wrote 10 Qwen, 72 Gemma and 168 Mistral valid rows before raising KeyError: vLLM raw top-two vocabulary logprobs omit one constrained answer token. Resume preserves these 250 rows verbatim. Further rows request processed_logprobs, which in vLLM 0.11 greedy sampling applies the allowed-token mask before softmax without temperature scaling. The TRUE/FALSE logprob difference and normalized binary probability have the same mathematical definition as before. Prompts, selected materials, sampling, estimands and decision criteria remain frozen. This repair follows partial execution, not preregistration; no outcome summaries were inspected to choose it.
