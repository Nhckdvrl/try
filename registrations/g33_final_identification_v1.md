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
