# G24A source-data audit v1 — FEVER + SciFact

Generated 2026-09-24 02:33:19 by `src/audit_g24a_sources.py` (130.6s). Machine census: `G24A_SOURCE_DATA_AUDIT_v1.json`.

## 1. Verdict

**AUDIT PASS** — all gates green.

## 2. Pinned sources (SHA-256 re-verified this run)

| file | sha256 |
| --- | --- |
| `fever/shared_task_dev.jsonl` | `e89865bfe1b4dd054e03dd57d7241a6fde24862905f31117cf0cd719f7c78df7` |
| `fever/train.jsonl` | `eba7e8f87076753f8494718b9a857827af7bf73e76c9e4b75420207d26e588b6` |
| `fever/wiki-pages.zip` | `4b06d95da6adf7fe02d2796176c670dacccb21348da89cba4c50676ab99665f2` |
| `scifact/data.tar.gz` | `11c621288d41ac144d29b13b0f8503b3820b7d6e8b1f6ff24dff335c196d76be` |

Licenses (official cards): FEVER data CC-BY-SA-3.0 / code GPL-3.0; SciFact CC-BY-NC-2.0 (non-commercial research).

## 3. Integrity gates

| gate | result | detail |
| --- | --- | --- |
| sha256 fever/shared_task_dev.jsonl | PASS | e89865bfe1b4dd05 |
| sha256 fever/train.jsonl | PASS | eba7e8f87076753f |
| sha256 fever/wiki-pages.zip | PASS | 4b06d95da6adf7fe |
| sha256 scifact/data.tar.gz | PASS | 11c621288d41ac14 |
| fever dev line count | PASS | 19998 |
| fever dev label balance | PASS | {'NOT ENOUGH INFO': 6666, 'SUPPORTS': 6666, 'REFUTES': 6666} |
| fever verifiable field consistent with label | PASS |  |
| fever NEI records carry zero sentence refs | PASS | 0 |
| fever dev flatten == HF card labelled_dev | PASS | 37566 |
| fever train line count | PASS | 145449 |
| fever train flatten == HF card train | PASS | 311431 |
| fever verifiable records | PASS | 13332 |
| fever text-once pool size | PASS | 12884 |
| fever pool label balance (pre text-quality) | PASS | {'SUPPORTS': 6449, 'REFUTES': 6435} |
| fever refs requested | PASS | 3462 |
| fever all refs resolved | PASS | missing=0 |
| fever no empty sentences | PASS | empty=0 |
| fever pool emitted == pool | PASS | 12648 |
| fever pool labels | PASS | {'SUPPORTS': 6326, 'REFUTES': 6322} |
| fever every block non-empty | PASS |  |
| fever text-quality [malformed] excluded | PASS | 66 |
| fever text-quality [quote-unpaired] excluded | PASS | 32 |
| fever text-quality [paren-unbalanced] excluded | PASS | 51 |
| fever text-quality [wiki-residue] excluded | PASS | 89 |
| fever group0 tuples reading-ordered | PASS | 110 |
| conflicts among verifiable claims | PASS | 3 |
| conflicts counting NEI siblings (dev) | PASS | 54 |
| normalization idempotent + self-consistent | PASS |  |
| fever kept blocks paren-balanced | PASS | 0 violations |
| fever kept blocks quote-paired | PASS | 0 violations |
| fever residual token | PASS | 0 hits |
| fever residual quote | PASS | 0 hits |
| fever residual tab_or_nl | PASS | 0 hits |
| fever residual multispace | PASS | 0 hits |
| fever residual space_before_punct | PASS | 0 hits |
| fever residual not_nfc | PASS | 0 hits |
| fever residual wiki_residue | PASS | 0 hits |
| scifact claims_train count | PASS | 809 |
| scifact claims_dev count | PASS | 300 |
| scifact claims_test count | PASS | 300 |
| scifact corpus count | PASS | 5183 |
| scifact pool size | PASS | 635 |
| scifact pool labels | PASS | {'CONTRADICT': 218, 'SUPPORT': 417} |
| scifact malformed excluded | PASS | 6 |
| scifact text-quality excluded | PASS | 5 |
| scifact exclusions | PASS | {'claims_total': 1409, 'no_evidence': 716, 'multi_doc_excluded': 47, 'mixed_label_excluded': 0, 'missing_doc_excluded': 0, 'out_of_bounds_excluded': 0, 'malformed_excluded': 6, 'text_quality_excluded': 5, 'text_quality_examples': [{'scifact_id': 1097, 'claim': 'Splenomegaly is observed in knockin mouse lacking the SHP-2 MAPK pathway.', 'block': 'The SHP2 signal-deficient mice (gp130F759/F759 were born normal but displayed splenomegaly and lymphadenopathy and an enhanced acute phase reaction.'}, {'scifact_id': 528, 'claim': 'Human T-lymphotropic virus type-I-associated myelopathy / tropical spastic paraparesis (HAM/TSP) patients produce Immunoglobulin G (IgG) antibodies which cross-react with an immunodominant epitope in Tax.', 'block': 'Antibodies to hnRNP-A1 cross-reacted with HTLV-1-tax, the immune response to which is associated with HAM/TSP (refs.'}, {'scifact_id': 532, 'claim': 'Hyperfibrinogenemia decreases rates of femoropopliteal bypass thrombosis.', 'block': 'RESULTS Markers for smoking (blood carboxyhaemoglobin concentration (p less than 0.05) and plasma thiocyanate concentration (p less than 0.01) and plasma concentrations of fibrinogen (p less than 0.001) and apolipoprotei'}, {'scifact_id': 533, 'claim': 'Hyperfibrinogenemia increases rates of femoropopliteal bypass thrombosis.', 'block': 'RESULTS Markers for smoking (blood carboxyhaemoglobin concentration (p less than 0.05) and plasma thiocyanate concentration (p less than 0.01) and plasma concentrations of fibrinogen (p less than 0.001) and apolipoprotei'}, {'scifact_id': 729, 'claim': 'Lymphadenopathy is observed in knockin mouse lacking the SHP-2 MAPK pathway.', 'block': 'The SHP2 signal-deficient mice (gp130F759/F759 were born normal but displayed splenomegaly and lymphadenopathy and an enhanced acute phase reaction.'}], 'records_emitted': 635} |
| scifact no mixed labels | PASS |  |
| scifact no missing docs / no out-of-bounds | PASS |  |
| scifact every block non-empty | PASS |  |
| scifact normalization idempotent | PASS |  |
| scifact residual (tab/nl/space/nfc/residue) | PASS | [] |
| scifact normalization whitespace-only (content preserved) | PASS |  |
| no claim-text overlap fever vs scifact | PASS | 0 |

## 4. FEVER construction

- dev 19998 lines = {'NOT ENOUGH INFO': 6666, 'SUPPORTS': 6666, 'REFUTES': 6666}; `verifiable` field agrees with label on every record; NEI records carry zero sentence refs.
- flatten arithmetic matches the HF card exactly: dev 37566 == 37,566; train 311431 == 311,431 (row-level provenance proven).
- text-once pool (verifiable + unique claim text): 12884 → text-quality gates → **12648 records {'SUPPORTS': 6326, 'REFUTES': 6322}**.
- excluded: NEI (6,666 records), 205 duplicated texts (243 extra records, including 3 verifiable-pool label conflicts (54 counting NEI siblings of the same claim text; both excluded): “An island is part of the ABC Islands.”; “Janet Leigh was a person.”; “The Hundred Years' War includes the Civil War.”), then text-quality gates: 66 malformed-sentence, 32 unpaired-quote, 51 unbalanced-paren, 89 wiki-residue claims (overlapping counts; full lists reviewed item-by-item on 2026-09-24).
- evidence block = group 0 (first annotated evidence set), tuples in reading order (page first-appearance, then line; 110 claims reordered), NFC page matching, first TAB field only (hyperlink annotations stripped), per-sentence normalization then join.
- resolution: 3462 refs over 2022 pages → 3462 resolved, 0 missing, 0 empty.

## 5. Text normalization

Rules (order): NFC → bracket parse tokens → ``...'' paired quotes → claims whose raw sentences still contain unpaired ``/'' are **excluded** (quote-pair gate; a defensive " / ' fallback exists in code but never fires on the kept pool) → glued `'s` → tokenized spacing before punctuation and after open brackets/currency → whitespace collapse. Word content is never altered.

- residual scan over all 12648 FEVER blocks: token=0, quote=0, tab_or_nl=0, multispace=0, space_before_punct=0, not_nfc=0, wiki_residue=0
- idempotence + self-consistency: PASS
- kept-pool verification: 0 paren-imbalance, 0 unpaired-quote blocks (expected 0 — gates above)

### 5.1 Before/after samples

**paren + IPA (accented wiki markup)** (fever id=111897, REFUTES)

- claim: Telemundo is a English-language television network.
- raw: Telemundo -LRB- -LSB- teleˈmundo -RSB- -RRB- is an American Spanish-language terrestrial television network owned by Comcast through the NBCUniversal division NBCUniversal Telemundo Enterprises .
- normalized: Telemundo ([teleˈmundo]) is an American Spanish-language terrestrial television network owned by Comcast through the NBCUniversal division NBCUniversal Telemundo Enterprises.

**quoted nickname** (fever id=137334, SUPPORTS)

- claim: Fox 2000 Pictures released the film Soul Food.
- raw: Soul Food is a 1997 American comedy-drama film produced by Kenneth `` Babyface '' Edmonds , Tracey Edmonds and Robert Teitel and released by Fox 2000 Pictures .
- normalized: Soul Food is a 1997 American comedy-drama film produced by Kenneth "Babyface" Edmonds, Tracey Edmonds and Robert Teitel and released by Fox 2000 Pictures.

**glued possessive** (fever id=90809, REFUTES)

- claim: Sean Penn is only ever a stage actor.
- raw: Following his film debut in the drama Taps -LRB- 1981 -RRB- and a diverse range of film roles in the 1980s , including Fast Times at Ridgemont High -LRB- 1982 -RRB- , Penn garnered critical attention for his roles in the crime dramas At Close Range -LRB- 1986 -RRB- , State of Grace -LRB- 1990 -RRB- , and Carlito 's Way -LRB- 1993 -RRB- .
- normalized: Following his film debut in the drama Taps (1981) and a diverse range of film roles in the 1980s, including Fast Times at Ridgemont High (1982), Penn garnered critical attention for his roles in the crime dramas At Close Range (1986), State of Grace (1990), and Carlito's Way (1993).

**accented evidence page** (fever id=197381, REFUTES)

- claim: Simón Bolívar is only known as Simón Bolívar.
- raw: Simón José Antonio de la Santísima Trinidad Bolívar y Palacios -LRB- -LSB- siˈmon boˈliβar -RSB- ; 24 July 1783 -- 17 December 1830 -RRB- , known as El Libertador , was a Venezuelan military and political leader who played a leading role in the establishment of Venezuela , Bolivia , Colombia , Ecuador , Peru and Panama as sovereign states , independent of Spanish rule .
- normalized: Simón José Antonio de la Santísima Trinidad Bolívar y Palacios ([siˈmon boˈliβar]; 24 July 1783 -- 17 December 1830), known as El Libertador, was a Venezuelan military and political leader who played a leading role in the establishment of Venezuela, Bolivia, Colombia, Ecuador, Peru and Panama as sovereign states, independent of Spanish rule.

**multi-sentence joint evidence set** (fever id=227362, REFUTES)

- claim: Giada at Home was only available on DVD.
- raw: It first aired on October 18 , 2008 on the Food Network . Food Network -LRB- legally known as Television Food Network -RRB- is an American basic cable and satellite television channel that is owned by Television Food Network , G.P. , a joint venture between Scripps Networks Interactive -LRB- which owns 70 % of the network -RRB- and the Tribune -LRB- FN -RRB- Cable Ventures Inc. -LRB- which owns the remaining 30 % -RRB- .
- normalized: It first aired on October 18, 2008 on the Food Network. Food Network (legally known as Television Food Network) is an American basic cable and satellite television channel that is owned by Television Food Network, G.P., a joint venture between Scripps Networks Interactive (which owns 70% of the network) and the Tribune (FN) Cable Ventures Inc. (which owns the remaining 30%).

**plain single sentence** (fever id=89891, REFUTES)

- claim: Damon Albarn's debut album was released in 2011.
- raw: His debut solo studio album Everyday Robots -- co-produced by XL Recordings CEO Richard Russell -- was released on 28 April 2014 and featured collaborations with Brian Eno , Natasha Khan and the Leytonstone City Pentecostal Mission Church Choir as well as sampling several rants by Lord Buckley .
- normalized: His debut solo studio album Everyday Robots -- co-produced by XL Recordings CEO Richard Russell -- was released on 28 April 2014 and featured collaborations with Brian Eno, Natasha Khan and the Leytonstone City Pentecostal Mission Church Choir as well as sampling several rants by Lord Buckley.

**REFUTES single page** (fever id=108281, REFUTES)

- claim: Andrew Kevin Walker is only Chinese.
- raw: Andrew Kevin Walker -LRB- born August 14 , 1964 -RRB- is an American BAFTA-nominated screenwriter .
- normalized: Andrew Kevin Walker (born August 14, 1964) is an American BAFTA-nominated screenwriter.

**longest block** (fever id=221137, SUPPORTS)

- claim: Ted Cruz is an American male.
- raw: Rafael Edward `` Ted '' Cruz -LSB- ˈkruːz -RSB- -LRB- born December 22 , 1970 -RRB- is an American politician and attorney , who has served as the junior United States Senator from Texas since 2013 . He was a candidate for the Republican nomination for President of the United States in the 2016 election . From 1999 to 2003 , he served in various political appointee positions : the Director of the Office of Policy Planning at the Federal Trade Commission -LRB- FTC -RRB- , an Associate Deputy Attorney General at the United States Department of Justice , and a Domestic Policy Advisor to George W. Bush on the 2000 George W. Bush Presidential campaign . He was the first Hispanic , and the longest-serving , Solicitor General in Texas history . From 2004 to 2009 , Cruz was an Adjunct Professor at the University of Texas School of Law in Austin , Texas , where he taught U.S. Supreme Court litigation . He defeated former State Representative Paul Sadler in the November 2012 general election , winning 56 -- 41 % . He is the first Hispanic American to serve as a U.S. Senator representing Texas , and is one of three senators of Cuban descent . He chairs the Senate Judiciary Subcommittee on Oversight , Federal Rights and Agency Activities , and is the Chairman of the Senate Commerce Subcommittee on Space , Science and Competitiveness . In November 2012 , he was appointed Vice-Chairman of the National Republican Senatorial Committee . During the primary campaign , his base of support was strongest with `` women , white evangelical Protestants , people over the age of 50 , and those who identified themselves as conservatives '' , though he had crossover appeal to other factions within his party , including libertarian conservatives and millennials . He eventually emerged as the main challenger to frontrunner Donald Trump . He suspended his campaign for president on May 3 , 2016 , after losing the Republican primary in Indiana to Trump .
- normalized: Rafael Edward "Ted" Cruz [ˈkruːz] (born December 22, 1970) is an American politician and attorney, who has served as the junior United States Senator from Texas since 2013. He was a candidate for the Republican nomination for President of the United States in the 2016 election. From 1999 to 2003, he served in various political appointee positions: the Director of the Office of Policy Planning at the Federal Trade Commission (FTC), an Associate Deputy Attorney General at the United States Department of Justice, and a Domestic Policy Advisor to George W. Bush on the 2000 George W. Bush Presidential campaign. He was the first Hispanic, and the longest-serving, Solicitor General in Texas history. From 2004 to 2009, Cruz was an Adjunct Professor at the University of Texas School of Law in Austin, Texas, where he taught U.S. Supreme Court litigation. He defeated former State Representative Paul Sadler in the November 2012 general election, winning 56 -- 41%. He is the first Hispanic American to serve as a U.S. Senator representing Texas, and is one of three senators of Cuban descent. He chairs the Senate Judiciary Subcommittee on Oversight, Federal Rights and Agency Activities, and is the Chairman of the Senate Commerce Subcommittee on Space, Science and Competitiveness. In November 2012, he was appointed Vice-Chairman of the National Republican Senatorial Committee. During the primary campaign, his base of support was strongest with "women, white evangelical Protestants, people over the age of 50, and those who identified themselves as conservatives", though he had crossover appeal to other factions within his party, including libertarian conservatives and millennials. He eventually emerged as the main challenger to frontrunner Donald Trump. He suspended his campaign for president on May 3, 2016, after losing the Republican primary in Indiana to Trump.

**SciFact SUPPORT union rationale** (scifact id=12, SUPPORT)

- claim: 40mg/day dosage of folic acid and 2mg/day dosage of vitamin B12 does not affect chronic kidney disease (CKD) progression.
- raw: RESULTS Mean baseline homocysteine level was 24.0 micromol/L in the vitamin group and 24.2 micromol/L in the placebo group. CONCLUSION Treatment with high doses of folic acid and B vitamins did not improve survival or reduce the incidence of vascular disease in patients with advanced chronic kidney disease or end-stage renal disease.   

- normalized: RESULTS Mean baseline homocysteine level was 24.0 micromol/L in the vitamin group and 24.2 micromol/L in the placebo group. CONCLUSION Treatment with high doses of folic acid and B vitamins did not improve survival or reduce the incidence of vascular disease in patients with advanced chronic kidney disease or end-stage renal disease.

**SciFact CONTRADICT union rationale** (scifact id=28, CONTRADICT)

- claim: A T helper 2 cell (Th2) environment impedes disease development in patients with systemic lupus erythematosus (SLE).
- raw: We report that activation of basophils by autoreactive IgE causes their homing to lymph nodes, promoting T helper type 2 (T(H)2) cell differentiation and enhancing the production of self-reactive antibodies that cause lupus-like nephritis in mice lacking the Src family protein tyrosine kinase Lyn (Lyn(-/-) mice). Individuals with SLE also have elevated serum IgE, self-reactive IgEs and activated basophils that express CD62 ligand (CD62L) and the major histocompatibility complex (MHC) class II molecule human leukocyte antigen-DR (HLA-DR), parameters that are associated with increased disease activity and active lupus nephritis. Thus, in Lyn(-/-) mice, basophils and IgE autoantibodies amplify autoantibody production that leads to lupus nephritis, and in individuals with SLE IgE autoantibodies and activated basophils are factors associated with disease activity and nephritis.
- normalized: We report that activation of basophils by autoreactive IgE causes their homing to lymph nodes, promoting T helper type 2 (T(H)2) cell differentiation and enhancing the production of self-reactive antibodies that cause lupus-like nephritis in mice lacking the Src family protein tyrosine kinase Lyn (Lyn(-/-) mice). Individuals with SLE also have elevated serum IgE, self-reactive IgEs and activated basophils that express CD62 ligand (CD62L) and the major histocompatibility complex (MHC) class II molecule human leukocyte antigen-DR (HLA-DR), parameters that are associated with increased disease activity and active lupus nephritis. Thus, in Lyn(-/-) mice, basophils and IgE autoantibodies amplify autoantibody production that leads to lupus nephritis, and in individuals with SLE IgE autoantibodies and activated basophils are factors associated with disease activity and nephritis.

### 5.2 Accented-page resolution (NFC fix)

- claim: Simón Bolívar is only known as Simón Bolívar.
- page (NFC): Simón_Bolívar
- resolved: Simón José Antonio de la Santísima Trinidad Bolívar y Palacios ([siˈmon boˈliβar]; 24 July 1783 -- 17 December 1830), known as El Libertador, was a Venezuelan military and political leader who played a leading role in the establishment of Venezuela, Bolivia, Colombia, Ecuador, Peru and Panama as sovereign states, independent of Spanish rule.

### 5.3 Text-quality exclusions (examples from the frozen build)

Every excluded claim's full list was reviewed item-by-item on 2026-09-24 (dump artifacts only; content never rewritten). Counts: malformed 66 / unpaired-quote 32 / unbalanced-paren 51 / wiki-residue 89. Examples:

- malformed [91884] “The Lincoln-Douglas debates happened in Freeport, Illinois.” → “Freeport on August 27”
- malformed [44512] “The Lincoln-Douglas debates happened in Quincy, Illinois.” → “Quincy on October 13”
- malformed [43042] “Ingushetia was established in the U.S South Peninsula.” → “The Chechen-Ingush Autonomous Soviet Socialist Republic, or Chechen-Ingush ASSR (Нохч-ГІалгІайн Автономнин Советски Социалистически Республи”
- malformed [118048] “The Lincoln-Douglas debates happened in Milton” → “Ottawa on August 21”
- malformed [69641] “Youtube is ranked as one of the top three most popular sites in the world.” → “, the website is ranked as the second most popular site in the world by Alexa Internet, a web traffic analysis company.”
- malformed [60351] “Shinji Mikami is a person who directs.” → “is a Japanese video game director and producer.”
- unpaired-quote [75599] “This is an ethnic group called Lithuanians.” → “Lithuanians '' ' -LRB- lietuviai , singular lietuvis/lietuv ė '' -RRB- are a Baltic ethnic group , native to Lithuania , where they number a”
- unpaired-quote [115185] “Qui-Gon Jinn is a fictional person in the Star Wars franchise.” → “Qui-Gon Jinn is a fictional character in the Star Wars franchise , portrayed by Liam Neeson as the main protagonist of the 1999 film Star Wa”
- unpaired-quote [143075] “Qui-Gon Jinn is a fictitious character.” → “Qui-Gon Jinn is a fictional character in the Star Wars franchise , portrayed by Liam Neeson as the main protagonist of the 1999 film Star Wa”
- unpaired-quote [153900] “Qui-Gon Jinn is a nonfiction character.” → “Qui-Gon Jinn is a fictional character in the Star Wars franchise , portrayed by Liam Neeson as the main protagonist of the 1999 film Star Wa”
- unpaired-quote [142951] “Qui-Gon Jinn is a real person.” → “Qui-Gon Jinn is a fictional character in the Star Wars franchise , portrayed by Liam Neeson as the main protagonist of the 1999 film Star Wa”
- unpaired-quote [66005] “Gordan Ramsay's earnings was reported only on a Canadian business magazine in 20” → “In 2015 , Forbes '' listed his earnings at $ 60 million for the previous 12 months , and ranked him the 21st highest earning celebrity in th”
- unbalanced-paren [140691] “Vietnam is a place.” → “Vietnam (ˌ; [vîət nāːm]), officially the Socialist Republic of Vietnam (SRV;, is the easternmost country on the Indochina Peninsula in South”
- unbalanced-paren [120210] “Yara Shahidi is a dog.” → “Yara Sayeh Shahidi شهیدی [jɑːɾɑː sɑːje ʃæhiːdiː]) (born February 10, 2000) is an American actress and model.”
- unbalanced-paren [36496] “Vietnam is not a country.” → “Vietnam (ˌ; [vîət nāːm]), officially the Socialist Republic of Vietnam (SRV;, is the easternmost country on the Indochina Peninsula in South”
- unbalanced-paren [143041] “Augustus died in 140 AD.” → “23 September 63 BC -- 19 August 14 AD) was the founder of the Roman Principate and considered the first Roman emperor, controlling the Roman”
- unbalanced-paren [84506] “Yara Shahidi was born on February 10, 1900.” → “Yara Sayeh Shahidi شهیدی [jɑːɾɑː sɑːje ʃæhiːdiː]) (born February 10, 2000) is an American actress and model.”
- unbalanced-paren [10312] “The 14th Dalai Lama is a leader.” → “The 14th Dalai Lama ([ˈdɑːlaɪ_ˈlɑːmə] (US), [ˌdælaɪ_ˈlɑːmə] (UK) (religious name: Tenzin Gyatso, shortened from Jetsun Jamphel Ngawang Lobsa”
- wiki-residue [43776] hit '`' → “Colin Rand Kaepernick ([` kæpərnɪk]; born November 3, 1987) is an American football quarterback who is currently a free agent.”
- wiki-residue [18823] hit '`' → “The Quran ([kɔrˈɑːn]; القرآن, literally meaning "the recitation"; also romanized Qur ` an or Koran) is the central religious text ”
- wiki-residue [189447] hit '`' → “Yandex ([` yʌndɛks] Яндекс) is a Russian multinational technology company specializing in Internet-related services and products.”
- wiki-residue [132865] hit '`' → “Colin Rand Kaepernick ([` kæpərnɪk]; born November 3, 1987) is an American football quarterback who is currently a free agent.”
- wiki-residue [98475] hit '`' → “The Quran ([kɔrˈɑːn]; القرآن, literally meaning "the recitation"; also romanized Qur ` an or Koran) is the central religious text ”
- wiki-residue [189453] hit '`' → “Yandex ([` yʌndɛks] Яндекс) is a Russian multinational technology company specializing in Internet-related services and products.”
- SciFact text-quality [id=1097] “Splenomegaly is observed in knockin mouse lacking the SHP-2 MAPK pathway.” → “The SHP2 signal-deficient mice (gp130F759/F759 were born normal but displayed splenomegaly and lymphadenopathy and an enhanced acute phase r”
- SciFact text-quality [id=528] “Human T-lymphotropic virus type-I-associated myelopathy / tropical spastic parap” → “Antibodies to hnRNP-A1 cross-reacted with HTLV-1-tax, the immune response to which is associated with HAM/TSP (refs.”
- SciFact text-quality [id=532] “Hyperfibrinogenemia decreases rates of femoropopliteal bypass thrombosis.” → “RESULTS Markers for smoking (blood carboxyhaemoglobin concentration (p less than 0.05) and plasma thiocyanate concentration (p less than 0.0”
- SciFact text-quality [id=533] “Hyperfibrinogenemia increases rates of femoropopliteal bypass thrombosis.” → “RESULTS Markers for smoking (blood carboxyhaemoglobin concentration (p less than 0.05) and plasma thiocyanate concentration (p less than 0.0”
- SciFact text-quality [id=729] “Lymphadenopathy is observed in knockin mouse lacking the SHP-2 MAPK pathway.” → “The SHP2 signal-deficient mice (gp130F759/F759 were born normal but displayed splenomegaly and lymphadenopathy and an enhanced acute phase r”

## 6. SciFact construction

- claims train/dev/test = 809/300/300; corpus = 5183 abstracts.
- pool = evidence-bearing, single-document, single-label claims: 635 {'CONTRADICT': 218, 'SUPPORT': 417} (excluded: 716 no-evidence, 47 multi-doc; mixed-label=0, out-of-bounds=0, missing-doc=0).
- rationale indices are 0-based (verified against claim↔sentence content on independent samples); block = union of rationale sentences, ascending.
- normalization changed 105 of 635 blocks (whitespace only: trailing blanks/newlines and space-before-punctuation such as `P = .04` → `P =.04`; verified by the whitespace-only content-preservation gate — no non-whitespace character ever changes).

## 7. Pool shape

- FEVER block chars: {'min': 24, 'p50': 145, 'p90': 274, 'p99': 501, 'max': 1879}; sentences/block: {1: 11393, 2: 1087, 3: 109, 4: 32, 5: 8, 6: 6, 7: 4, 8: 5, 10: 1, 11: 1, 12: 2}; multi-group claims: 3413.
- SciFact block chars: {'min': 43, 'p50': 309, 'p90': 715, 'p99': 1004, 'max': 1586}; sentences/block: {1: 318, 2: 186, 3: 88, 4: 35, 5: 7, 6: 1}.
- cross-dataset claim-text overlap: 0.

## 8. Downstream hooks

- cluster keys frozen for the G24A prereg: FEVER → first evidence wiki page (NFC); SciFact → evidence doc_id.
- selection must use Base/Admit leverage only; Exclude outcomes are never seen during selection (PAPER_SCALE_AUDIT §7).
