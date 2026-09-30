# Source-only contradiction challenge before any research inference

Read ONLY this instruction and the assigned challenge input. You have not seen
previous judgments, X paraphrases, gold roles, or research-model responses.
Your job is to try to falsify the proposed source contrast, not approve it.
A/B roles are arbitrary; every row needs your own judgment.

For each E_A and E_B, determine support/refute/unclear for the EXACT claim.
Support must warrant the exact proposition. Refutation requires incompatible
information about that proposition under the ordinary matched-time/same-subject
interpretation; a different compatible fact, an omission, or a stronger claim
about someone else is not refutation. Do not demand contrived possibilities
for obvious single-valued attributes (a person's birthplace, the credited actor
for a specified role in a specified film), but DO reject ordinary possibilities
that make both statements true:
- naming a different sunniest city does not refute that the claim city is sunnier
  than other regions;
- attending a different university does not refute ever attending this university;
- a different person's DNA used in one experiment does not refute the claimed
  person's DNA being used in another experiment;
- overlapping review categories, genres, regions or aliases are not exclusive;
- a professional player's role can coexist with management or league-specific
  retirement; unclear scope is not a clean contradictory record.
Look particularly at existential versus exclusive claims, quantifier changes,
entity aliases, scope/time mismatches, overlapping categories, and malformed
claims/sentences. False real-world facts may appear in real Wikipedia revisions:
do NOT reject solely because the record contradicts your world knowledge. The
record is authoritative for the hypothetical task. Page/topic resolves referents.

`decisive` requires exactly one support and one genuine refute. `clear_scope`
requires the claim and both records concern the same referent/time/attribute
and do not depend on an unresolved alias, unstated exclusivity or missing detail.
`readable` requires a sufficiently natural and unambiguous proposition; cast-list
fragments and minor punctuation are fine, seriously mangled syntax is not.
Do not repair or rewrite stimuli. Explain concrete item-specific arguments.
Return EXACTLY one JSONL per input, keys: id, a_relation, b_relation, decisive
(boolean), clear_scope (boolean), readable (boolean), reason. Valid relations:
support/refute/unclear. Write only the assigned file. Check count and IDs.
