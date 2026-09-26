# Independent blind re-audit of the final ConfB 200

Conducted 2026-09-27 by local OpenCode MiMo v2.6 Flash, one 50-pair batch per call. The agent saw only claim plus randomly swapped evidence A/B, not prior labels or model outputs. This is an **LLM-assisted semantic audit**, not a human gold annotation. No original materials or full-sample model results were changed. The reviewer can make errors; individual issue notes are retained below and in batch files.

## Validation

All 200 IDs appear once; each audit record has the expected schema; all blind text and A/B swaps reproduce the frozen selected data. Counts:

| Flag | Count / 200 |
|---|---:|
| Pair marked valid | 190 |
| A/B relations match frozen S/R labels | 189 |
| Natural | 147 |
| Awkward | 48 |
| Broken | 5 |
| Valid, relation-correct, and natural | 142 |

## Invalid pairs

- `g24cfb_001`: 'Unreasonable reviews' is odd wording; A's 'mixed reviews' is a different dimension and neither entails nor contradicts it; only B matches.
- `g24cfb_010`: Claim's 'more than the second smallest' has unclear comparison direction; B asserts exactly second smallest (refutes under either reading); B also has missing area value.
- `g24cfb_054`: A shows 3-0 (contradicts 2-0); B only reports an interim 2-0 lead, not a completed loss, so it does not entail the claim. Claim itself impossible: a best-of-7 WCF cannot be lost 2-0.
- `g24cfb_105`: 'Jud' (Jud Birza) is Fabio's real name, so A likely supports too; if so no refuting evidence, and 'Jud' lacks a referent link in-text
- `g24cfb_149`: B states nine titles but enumerates ten championship years - internally inconsistent, so it cannot cleanly support the claim.
- `g24cfb_210`: B says three members quit vs claim's 'one' - refutes only under an exactly-one reading, while an existential reading makes B compatible. Typo 'gutarist'.
- `g24cfb_211`: A says first 'possible' case, claim says first 'confirmed' - different statuses but not mutually exclusive, so no clear contradiction.
- `g24cfb_224`: A only lists other channels and omits Al-Hayat; omission is not a contradiction. B explicitly includes Al-Hayat.
- `g24cfb_231`: B names 'Bang'; in One-Punch Man Bang is Silver Fang, i.e. apparently the same master as 'Fang', so B does not genuinely contradict.
- `g24cfb_245`: A is hedged ('may be a Guru in a Gurukul') and never identifies 'Pandit'; B names a Pathsala but does not deny a Gurukul role - no genuine contradiction.

## Relation-label mismatches

- `g24cfb_001`: A=neutral, B=support; 'Unreasonable reviews' is odd wording; A's 'mixed reviews' is a different dimension and neither entails nor contradicts it; only B matches.
- `g24cfb_010`: A=ambiguous, B=refute; Claim's 'more than the second smallest' has unclear comparison direction; B asserts exactly second smallest (refutes under either reading); B also has missing area value.
- `g24cfb_054`: A=refute, B=neutral; A shows 3-0 (contradicts 2-0); B only reports an interim 2-0 lead, not a completed loss, so it does not entail the claim. Claim itself impossible: a best-of-7 WCF cannot be lost 2-0.
- `g24cfb_105`: A=ambiguous, B=support; 'Jud' (Jud Birza) is Fabio's real name, so A likely supports too; if so no refuting evidence, and 'Jud' lacks a referent link in-text
- `g24cfb_149`: A=refute, B=ambiguous; B states nine titles but enumerates ten championship years - internally inconsistent, so it cannot cleanly support the claim.
- `g24cfb_210`: A=support, B=ambiguous; B says three members quit vs claim's 'one' - refutes only under an exactly-one reading, while an existential reading makes B compatible. Typo 'gutarist'.
- `g24cfb_211`: A=ambiguous, B=support; A says first 'possible' case, claim says first 'confirmed' - different statuses but not mutually exclusive, so no clear contradiction.
- `g24cfb_224`: A=neutral, B=support; A only lists other channels and omits Al-Hayat; omission is not a contradiction. B explicitly includes Al-Hayat.
- `g24cfb_231`: A=support, B=ambiguous; B names 'Bang'; in One-Punch Man Bang is Silver Fang, i.e. apparently the same master as 'Fang', so B does not genuinely contradict.
- `g24cfb_245`: A=ambiguous, B=neutral; A is hedged ('may be a Guru in a Gurukul') and never identifies 'Pandit'; B names a Pathsala but does not deny a Gurukul role - no genuine contradiction.
- `g24cfb_253`: A=support, B=refute; Claim wording is clumsy ('after the age of 49 years, after 2001'); A gives retired 2001 at 49, B gives 2002 at 50. Evidence omits the film title.

## All flagged item notes

- `g24cfb_001` (awkward, valid=False): 'Unreasonable reviews' is odd wording; A's 'mixed reviews' is a different dimension and neither entails nor contradicts it; only B matches.
- `g24cfb_002` (awkward, valid=True): A: 16-14-1 (16 wins) vs B: 17-14-1 (17 wins); both evidences contain mojibake separators (ï¿½).
- `g24cfb_009` (awkward, valid=True): 0 recoveries vs 1 recovery; claim has no referent/context (which outbreak).
- `g24cfb_010` (awkward, valid=False): Claim's 'more than the second smallest' has unclear comparison direction; B asserts exactly second smallest (refutes under either reading); B also has missing area value.
- `g24cfb_027` (broken, valid=True): Claim corrupted ('row German' for Low German); A contains vandalized/vulgar definition of a different word; B gives Low German 'Brack'.
- `g24cfb_040` (awkward, valid=True): 35th is worse (lower) than #33; 32nd is better. Evidence text is garbled: run-on sentences and stray '? v=Zv0WlHbBhdc' fragment.
- `g24cfb_047` (broken, valid=True): Evidence A is corrupted: 'Raymond' substituted with 'Railroad' in several names plus a broken URL fragment; A asserts confirmation name Railroad, B asserts Richard.
- `g24cfb_048` (awkward, valid=True): Eleven vs twelve countries; claim passive 'were originated from' is unnatural; both evidences carry stray '; Algeria' fragment.
- `g24cfb_051` (awkward, valid=True): Persepolis vs Al-Gharafa; evidence A has missing birth date '( , born' and typo 'persepolise F C'.
- `g24cfb_054` (awkward, valid=False): A shows 3-0 (contradicts 2-0); B only reports an interim 2-0 lead, not a completed loss, so it does not entail the claim. Claim itself impossible: a best-of-7 WCF cannot be lost 2-0.
- `g24cfb_055` (awkward, valid=True): Jacksonville Jaguars vs Dublin Shamrocks; B pairs a non-NFL club with 'of the National Football League'.
- `g24cfb_061` (awkward, valid=True): Claim name 'Ryan Urie' looks corrupted (real departing guitarist Ryan Ross; Brendon Urie stayed). A names Urie as leaver, B names Ross, contradicting the claim's first clause.
- `g24cfb_075` (awkward, valid=True): both evidences have subject-verb disagreement ('upcoming projects ... is set')
- `g24cfb_078` (awkward, valid=True): claim wording vague: 'dedicates his life to what he always wanted after thirty years' has unclear modifier placement
- `g24cfb_080` (awkward, valid=True): A's 'overwhelming laughable reviews' is garbled; claim's 'diverse reviews' is unusual wording for mixed reviews
- `g24cfb_090` (awkward, valid=True): B internally inconsistent: claims three solo albums but then lists four titles
- `g24cfb_092` (awkward, valid=True): claim's 'after defeating the Nevada Wolf Pack' appears in neither evidence; claim phrasing 'have got 1st place' is non-idiomatic
- `g24cfb_105` (natural, valid=False): 'Jud' (Jud Birza) is Fabio's real name, so A likely supports too; if so no refuting evidence, and 'Jud' lacks a referent link in-text
- `g24cfb_108` (awkward, valid=True): evidence_a has corrupted casing: 'washington redskins'
- `g24cfb_109` (awkward, valid=True): claim phrasing 'until before 1968' is unnatural and boundary-ambiguous
- `g24cfb_112` (awkward, valid=True): evidence_a producer 'kulbir yadav' looks like vandalized/inserted text and is lowercased
- `g24cfb_124` (broken, valid=True): '264 bytes' is corrupted rendering of 2^64 (lost superscript) in claim and both evidences
- `g24cfb_135` (awkward, valid=True): claim has title typo 'Eigh Below'; both evidences describe the 1958 event rather than the film
- `g24cfb_144` (awkward, valid=True): both evidences have broken punctuation/capitalization ('Prime Minister . :', 'Aircrafts')
- `g24cfb_149` (natural, valid=False): B states nine titles but enumerates ten championship years - internally inconsistent, so it cannot cleanly support the claim.
- `g24cfb_152` (awkward, valid=True): Garbled quotation nesting in both evidences; also 56% would be 'rotten' on RT, so B's own figure undercuts its 'fresh' label.
- `g24cfb_158` (awkward, valid=True): Claim has no referent - no date, disease, place or event given for 'cases'.
- `g24cfb_161` (awkward, valid=True): Evidences name him only 'Kgositsile' (Earl Sweatshirt's real name); reader must infer the referent.
- `g24cfb_163` (awkward, valid=True): Claim has agreement error 'The Steelers has' and drops context (it is a postseason record).
- `g24cfb_176` (awkward, valid=True): Sentences glued together in both evidences ('25 March 2015.Birdy is a soprano .').
- `g24cfb_177` (broken, valid=True): Mojibake in the scores ('2i??2'); 'United' also has no club referent.
- `g24cfb_178` (awkward, valid=True): Glued sentence boundary in both evidences ('...to premiere in 2013.A sequel titled...').
- `g24cfb_179` (awkward, valid=True): Missing citation punctuation before 'Annex III of EC Regulation 110/2008 , amended .' in both evidences.
- `g24cfb_180` (awkward, valid=True): Stray comma in claim and B ('from , Duncanville'); B also has 'an Trinidadian' and a trailing ', .'.
- `g24cfb_189` (awkward, valid=True): Metric mismatch: claim says 'scored ... wins'; A's 3-margin is regulation/overtime wins (41-38), B's is total wins (44-43).
- `g24cfb_192` (awkward, valid=True): Claim and B have a stray comma after 'from'; Oak Cliff/Dallas and Duncanville are distinct places.
- `g24cfb_196` (awkward, valid=True): A is hedged ('perhaps second ... at least after China'); B asserts largest; Hydro-Quebec/Quebec spelling differs.
- `g24cfb_198` (awkward, valid=True): Claim conflates actress Clara Rugaard with the character, whom A names 'Daughter'.
- `g24cfb_200` (awkward, valid=True): Unnatural article in claim ('the COVID-19'); claim says 'reported' vs evidence 'confirmed to have reached'.
- `g24cfb_201` (awkward, valid=True): A has odd glosses ('eldest son aka Just Doo', '( nana )') though its count of 3 children is clear.
- `g24cfb_202` (awkward, valid=True): Truncated citation fragment at the end of both evidences ('... Origins Of Excellence Pt .').
- `g24cfb_203` (awkward, valid=True): Dangling '( or ;' fragment (a name was dropped) in both evidences.
- `g24cfb_210` (awkward, valid=False): B says three members quit vs claim's 'one' - refutes only under an exactly-one reading, while an existential reading makes B compatible. Typo 'gutarist'.
- `g24cfb_211` (natural, valid=False): A says first 'possible' case, claim says first 'confirmed' - different statuses but not mutually exclusive, so no clear contradiction.
- `g24cfb_212` (awkward, valid=True): 'Edgar economics' is not a real school of economic thought - fabricated/nonsensical term in claim and B.
- `g24cfb_217` (awkward, valid=True): Cast-list fragment with an asterisk used as separator ('Two-Face 's Thug* Ed Begley Jr').
- `g24cfb_218` (awkward, valid=True): Wikitext braces leaked into both evidences ('Kyra Robinson ( 2019 ) } } Michael Elliot Epps ...').
- `g24cfb_224` (natural, valid=False): A only lists other channels and omits Al-Hayat; omission is not a contradiction. B explicitly includes Al-Hayat.
- `g24cfb_231` (natural, valid=False): B names 'Bang'; in One-Punch Man Bang is Silver Fang, i.e. apparently the same master as 'Fang', so B does not genuinely contradict.
- `g24cfb_233` (broken, valid=True): Both records contain an injected URL/query fragment ('? detail=writerid & page=1 ...') between name and birth date; dates themselves are 9 vs 29 November.
- `g24cfb_236` (awkward, valid=True): A matches eighth-wealthiest and $61.5bn but contains typo 'eigth-wealthiest'; B says seventh and $61.8bn.
- `g24cfb_245` (awkward, valid=False): A is hedged ('may be a Guru in a Gurukul') and never identifies 'Pandit'; B names a Pathsala but does not deny a Gurukul role - no genuine contradiction.
- `g24cfb_246` (awkward, valid=True): B gives 'Jon Weiner'; A gives the garbled/renamed '( I. Juan Weiner )', which does not match the claim's referent.
- `g24cfb_248` (awkward, valid=True): Randers FC vs Dynamo Dresden loan; both texts are truncated mid section-header ('==NBA re' / '==NB').
- `g24cfb_253` (awkward, valid=True): Claim wording is clumsy ('after the age of 49 years, after 2001'); A gives retired 2001 at 49, B gives 2002 at 50. Evidence omits the film title.
- `g24cfb_258` (awkward, valid=True): A matches the claim but is internally odd ('four-and-a-half out of four stars'); B's scale is out of five.
- `g24cfb_281` (awkward, valid=True): Claim contains typo 'New York Jest' (Jets); A says he is a free agent, B says New York Jets.
- `g24cfb_297` (awkward, valid=True): Claim garbles the verb 'band' into a noun ('the band was under four evacuees'); A says four band together (not under four), B says three.

A valid-natural subset can be used only for **post hoc sensitivity**, never as a new held-out confirmation or replacement for the 200-pair primary result. The audit did not check source attribution or historical factual truth outside the shown sentences.
