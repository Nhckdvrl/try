# Rationale paired coding rubric — G24A reversibility audit (step 4)

## Scope and honesty rules

- You are producing a **behavioral description of the rationale text only**. Not
  mechanism evidence, not claims about internal computation. Label what the text
  does, not what you think the model "really" did.
- Code the `exclude_post` rationale of the **primary INC item and primary DEC
  item** in each of the 53 sections of your batch file (section header gives
  `gnum`, `sha`, `source`, `type`).
- **No cherry-picking: all 53 sections must be coded.** Read each section
  completely (evidence, both claims, values, both reasonings) before labeling.

## Context of each cell

Identical evidence text for both claims. INC claim = claim the evidence supports
(judgment pushed up); DEC claim = claim the evidence refutes (judgment pushed
down). The `exclude_post` cell means: the model saw the evidence first, then a
ruling says the evidence must NOT be used; `values: admit_post -> exclude_post`
shows where the judgment was and where it landed after the ruling.

## Labels (apply independently to each side's exclude_post reasoning)

- `reset_to_uncertainty` — the reasoning treats the evidence as unavailable or
  invalid under the ruling and withdraws toward uncertainty: "without evidence I
  cannot determine", "the claim cannot be assessed", "insufficient
  information", hedging toward the middle, refusing to commit. (Label by the
  TEXT; the value line is context only.)
- `still_cites_for_falsity` — the reasoning acknowledges the exclusion ruling
  (directly or implicitly) but still uses the CONTENT of the evidence — or its
  conclusion — to sustain the pre-existing verdict. On the DEC side this is
  typically "evidence excluded, but the evidence shows the claim is false". On
  the INC side the same operative move applies (still leaning on the excluded
  evidence content to keep the claim supported). The label name is kept uniform
  on both sides; the operative feature is "uses the excluded evidence content
  despite the ruling".
- `other` — neither: pure world-knowledge reasoning that ignores the evidence
  altogether, discussion of the ruling's wording, formatting, or anything
  unrelated to the evidence-vs-uncertainty question.
- `unclear` — empty, truncated to meaninglessness, or genuinely ambiguous
  between the above.

When the reasoning both resets AND cites (rare), pick the dominant move in the
text and say why in `note`.

## Output file

Write EXACTLY this file (create or overwrite):

    results/discovery/g24a_reversibility_v1_coding_<model>.jsonl

where `<model>` is your assigned model tag. One JSON object per line, **53
lines, in batch order (gnum 1..53)**:

    {"gnum": 1, "group_sha": "<sha copied from section header>", "model": "<model tag>",
     "inc_item": "<primary INC item id>", "dec_item": "<primary DEC item id>",
     "inc_label": "<one of the 4 labels>", "dec_label": "<one of the 4 labels>",
     "inc_quote": "<verbatim snippet, <=20 words, from the INC reasoning>",
     "dec_quote": "<verbatim snippet, <=20 words, from the DEC reasoning>",
     "note": "<short note or empty string>"}

Requirements:

- `gnum` values exactly 1..53, each once; `group_sha` copied character-exact
  from the section header; item ids copied from the section.
- Quotes must be **verbatim substrings** of the corresponding reasoning text.
- Valid labels: `reset_to_uncertainty`, `still_cites_for_falsity`, `other`,
  `unclear`.
- No extra lines, no comments; every line must parse as JSON.

## Self-validation (required before finishing)

Run a python check that: parses the file back; line count == 53; gnums ==
1..53 exactly once; all labels valid; every quote is a character-exact
substring of the corresponding reasoning in the batch file. Fix and re-run
until it passes; report the check output in your final reply.
