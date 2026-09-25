# Blind taxonomy audit batch 1/3 (G24A fresh-pair census)

Classify each group's contradiction form into exactly one of:
explicit_negation, antonym_opposite, exclusive_alternative,
numeric_value, indirect_contradiction (definitions in the task
prompt). This file contains NO pre-existing labels - it is blind.

## sha=dcfb5c9b8a source=scifact n_inc=4 n_dec=1
EVIDENCE: Remarkably, PDS reduces proliferation of HR-defective cells by inducing DSB accumulation, checkpoint activation, and deregulated G2/M progression and by enhancing the replication defect intrinsic to HR deficiency.
INC claims (4):
  [g24a_scifact_992] Pyridostatin deregulates G2/M progression.
  [g24a_scifact_996] Pyridostatin induces checkpoint activation.
  [g24a_scifact_997] Pyridostatin induces double-strand breaks accumulation.
  [g24a_scifact_999] Pyridostatin reduces proliferation of homologous recombination - defective cells.
DEC claims (1):
  [g24a_scifact_994] Pyridostatin encourages proliferation of homologous recombination - defective cells.

## sha=c1a3138125 source=fever n_inc=2 n_dec=4
EVIDENCE: X-Men: Apocalypse is a 2016 American superhero film based on the fictional X-Men characters that appear in Marvel Comics.
INC claims (2):
  [g24a_fever_42974] X-Men: Apocalypse is a motion picture.
  [g24a_fever_53017] X-Men: Apocalypse is a work.
DEC claims (4):
  [g24a_fever_124805] X-Men: Apocalypse was cancelled in 2013.
  [g24a_fever_139445] X-Men: Apocalypse is only a comic book.
  [g24a_fever_72485] X-Men: Apocalypse is a TV show.
  [g24a_fever_73733] X-Men: Apocalypse was announced in 1970.

## sha=2d6e47739f source=fever n_inc=4 n_dec=15
EVIDENCE: It is bordered by Virginia to the southeast, Kentucky to the southwest, Ohio to the northwest, Pennsylvania to the north (and, slightly, east), and Maryland to the northeast.
INC claims (4):
  [g24a_fever_32474] West Virginia borders Maryland to the northeast.
  [g24a_fever_50406] West Virginia borders Pennsylvania.
  [g24a_fever_52218] West Virginia borders Maryland.
  [g24a_fever_61195] West Virginia borders Kentucky.
DEC claims (15):
  [g24a_fever_106209] West Virginia borders Wendy's to the north.
  [g24a_fever_107731] West Virginia borders Maine to the southeast.
  [g24a_fever_110175] West Virginia only borders Ohio to the southeast.
  [g24a_fever_117447] West Virginia borders Maryland and Ohio to the northeast.
  [g24a_fever_133456] West Virginia borders Maine to the southwest.
  [g24a_fever_136031] West Virginia borders Maine to the northeast.
  [g24a_fever_138213] West Virginia borders Pennsylvania and Ohio to the north.
  [g24a_fever_138500] West Virginia only borders Ohio to the southwest.
  [g24a_fever_153803] West Virginia borders Vermont to the north.
  [g24a_fever_155704] West Virginia borders Maine and Kentucky to the southwest.
  [g24a_fever_51442] West Virginia borders Ohio and Virginia to the southeast.
  [g24a_fever_72495] West Virginia borders Chipotle to the northwest.
  [g24a_fever_78355] West Virginia only borders Maine to the north.
  [g24a_fever_88479] West Virginia only borders Vermont to the northeast.
  [g24a_fever_89171] West Virginia only borders Maine to the northwest.

## sha=7fb8cff259 source=fever n_inc=4 n_dec=3
EVIDENCE: It was adapted for television by Archie Comics' chief creative officer Roberto Aguirre-Sacasa and executive produced by Greg Berlanti.
INC claims (4):
  [g24a_fever_16007] Riverdale is an adaptation.
  [g24a_fever_23885] Riverdale's executive producer is Greg Berlanti.
  [g24a_fever_34527] Riverdale has an executive producer.
  [g24a_fever_99007] Roberto Aguirre-Sacasa was the one who adapted Riverdale for television.
DEC claims (3):
  [g24a_fever_149644] Riverdale's executive producer is Joaquim Dos Santos.
  [g24a_fever_82934] Riverdale's executive producer is someone other than Greg Berlanti.
  [g24a_fever_92103] Riverdale was adapted for tv by someone other than Roberto Aguirre-Sacasa.

## sha=a8e1c43172 source=fever n_inc=5 n_dec=6
EVIDENCE: Adidas AG ([ˈadiˌdas]) (stylised as adidas since 1949) is a German multinational corporation, headquartered in Herzogenaurach, Germany, that designs and manufactures shoes, clothing and accessories.
INC claims (5):
  [g24a_fever_122463] Adidas is from Germany.
  [g24a_fever_38275] Adidas designs things that you can wear.
  [g24a_fever_59358] Adidas manufactures items.
  [g24a_fever_7580] Adidas designs shoes.
  [g24a_fever_88619] Adidas is German.
DEC claims (6):
  [g24a_fever_116604] Adidas is Colombian.
  [g24a_fever_137159] Adidas is only Irish.
  [g24a_fever_42982] Adidas only manufactures candy.
  [g24a_fever_74645] Adidas designs buildings.
  [g24a_fever_84907] Adidas only designs posters.
  [g24a_fever_90098] Adidas only designs cars.

## sha=1fbc88c092 source=fever n_inc=7 n_dec=3
EVIDENCE: It achieved worldwide success by topping the charts in a variety of markets, ultimately selling 12 million copies worldwide, thus becoming one of the best-selling singles of all time.
INC claims (7):
  [g24a_fever_10164] Bad Romance was profitable around the world.
  [g24a_fever_112416] Bad Romance sold 12 million copies.
  [g24a_fever_124618] 12 million copies of Bad Romance were bought around the world.
  [g24a_fever_125037] Bad Romance was successful.
  [g24a_fever_144978] Bad Romance was released as a single.
  [g24a_fever_25824] Bad Romance sold 12 million copies worldwide.
  [g24a_fever_81847] Bad Romance achieved worldwide success.
DEC claims (3):
  [g24a_fever_156525] Bad Romance only sold copies in Australia.
  [g24a_fever_20605] Bad Romance was one of the worst-selling singles of all time.
  [g24a_fever_52572] Bad Romance was one of the best-selling stocks of all time.

## sha=87f335a320 source=scifact n_inc=1 n_dec=1
EVIDENCE: Exposed infants had a lower hospital death rate (14.2% vs 18.5%; OR, 0.73 [95% CI, 0.54 to 0.98]; ARR, 4.3 [95% CI, 0.3 to 8.3]) and a lower rate of pulmonary hemorrhage (5.6% vs 8.9%; OR, 0.60 [95% CI, 0.38 to 0.95]; ARR, 3.3 [95% CI, 0.4 to 6.3]). CONCLUSIONS AND RELEVANCE In this national population-based cohort of extremely preterm infants, screening echocardiography before day 3 of life was associated with lower in-hospital mortality and likelihood of pulmonary hemorrhage but not with differences in necrotizing enterocolitis, severe bronchopulmonary dysplasia, or severe cerebral lesions.
INC claims (1):
  [g24a_scifact_367] Early patent ductus ateriosus (PDA) screening decreases in-hospital mortality.
DEC claims (1):
  [g24a_scifact_368] Early patent ductus ateriosus (PDA) screening increases in-hospital mortality.

## sha=727e412419 source=scifact n_inc=1 n_dec=1
EVIDENCE: This conclusion was supported by experiments that showed that enhancing cSMAC formation reduced stimulatory capacity of the weak peptide.
INC claims (1):
  [g24a_scifact_1385] cSMAC formation enhances weak ligand signalling.
DEC claims (1):
  [g24a_scifact_1386] cSMAC formation represses weak ligand signalling.

## sha=540d5d0edb source=fever n_inc=6 n_dec=2
EVIDENCE: A dark satirical and dystopian take on the superhero genre, the film is set in an alternate history in the year 1985 at the height of the Cold War between the United States and the Soviet Union, as a group of mostly retired American superheroes investigates the murder of one of their own before uncovering an elaborate and deadly conspiracy, while their moral limitations are challenged by the complex nature of the circumstances.
INC claims (6):
  [g24a_fever_144309] The film Watchmen focuses on a group of mostly retired American superheroes.
  [g24a_fever_28495] Watchmen is a film about a group of mostly retired American superheroes.
  [g24a_fever_28496] Watchmen is a film about a group of mostly retired American superheroes, who investigate a murder.
  [g24a_fever_36843] Watchmen is a dark satirical and dystopian take on the superhero genre.
  [g24a_fever_36844] Watchmen explores the superhero genre through a dark satirical and dystopian lens.
  [g24a_fever_66473] Watchmen is a film set in an alternate history in the year 1985.
DEC claims (2):
  [g24a_fever_45522] Watchmen is a dark satirical and dystopian take on the French Revolution.
  [g24a_fever_54111] Watchmen is a film about a group of mostly retired Russian superheroes.

## sha=b6d5c2a224 source=fever n_inc=2 n_dec=2
EVIDENCE: Basildon [ˈbæzɪldən] is the largest town in the borough of Basildon in the county of Essex, England.
INC claims (2):
  [g24a_fever_131931] Basildon is a place.
  [g24a_fever_30270] Basildon is English.
DEC claims (2):
  [g24a_fever_111769] Basildon is far away from England.
  [g24a_fever_112890] Basildon is in Denmark.

## sha=f1a3ac1f42 source=fever n_inc=2 n_dec=1
EVIDENCE: He worked as an Inspector of Finances in the Inspectorate General of Finances (IGF), then became an investment banker at Rothschild & Cie Banque.
INC claims (2):
  [g24a_fever_123614] Emmanuel Macron worked as an investment banker at Rothschild & Cie Banque.
  [g24a_fever_23446] Emmanuel Macron worked as an inspector.
DEC claims (1):
  [g24a_fever_123762] Emmanuel Macron refused to work as an Inspector of Finances.

## sha=d39e5de6af source=fever n_inc=4 n_dec=3
EVIDENCE: Norman Bates is a fictional character created by Robert Bloch as the main antagonist in his 1959 novel Psycho, and portrayed by Anthony Perkins in the 1960 film of the same name directed by Alfred Hitchcock and its sequels, and by Freddie Highmore in the television series Bates Motel.
INC claims (4):
  [g24a_fever_162662] Norman Bates was published by Robert Bloch.
  [g24a_fever_162664] Norman Bates is a fictional character.
  [g24a_fever_162665] Norman Bates is a character.
  [g24a_fever_162668] Norman Bates is main antagonist in Psycho.
DEC claims (3):
  [g24a_fever_162657] Norman Bates is from the novel Harry Potter.
  [g24a_fever_162659] Norman Bates is a character exclusively from film.
  [g24a_fever_162680] Norman Bates is from the Steven King novel Psycho.

## sha=76755c263e source=fever n_inc=2 n_dec=1
EVIDENCE: Kerplunk is the second studio album by American punk rock band Green Day, released on December 17, 1991 by Lookout! Records was an independent record label, initially based in Laytonville, California and later in Berkeley, focusing on punk rock.
INC claims (2):
  [g24a_fever_125388] Kerplunk was released through a record label.
  [g24a_fever_155145] Lookout Records helped release Kerplunk.
DEC claims (1):
  [g24a_fever_129698] Kerplunk was released through online sale only.

## sha=fc194aedb7 source=fever n_inc=2 n_dec=5
EVIDENCE: For instance, in 2015, among Americans, 89% of adults had consumed alcohol at some point, 70% had drunk it in the last year, and 56% in the last month.
INC claims (2):
  [g24a_fever_124472] In 2015, among Americans, more than 50% of adults had consumed alcoholic drink at some point.
  [g24a_fever_99251] In 2015, among Americans, more than 50% of adults had consumed alcoholic drink in the last year.
DEC claims (5):
  [g24a_fever_24779] In 2015, among Americans, 30% of adults had consumed alcoholic drink in the last year.
  [g24a_fever_83351] In 2015, among Mexicans, 70% of adults had consumed alcoholic drink in the last year.
  [g24a_fever_86131] In 2015, among Americans, 5% of adults had consumed alcoholic drink in the last month.
  [g24a_fever_91798] In 2015, among Americans, 44% of adults had consumed alcoholic drink in the last month.
  [g24a_fever_96377] In 2015, among Americans, 11% of adults had consumed alcoholic drink at some point.

## sha=7f6d5f9bd8 source=fever n_inc=6 n_dec=2
EVIDENCE: In 1997, Moyer made his big-screen debut landing the lead role in the film adaptation of the long-running comic strip Prince Valiant by Hal Foster, working alongside Ron Perlman and Katherine Heigl.
INC claims (6):
  [g24a_fever_188131] Stephen Moyer acted in a film adaptation of a comic.
  [g24a_fever_188136] Stephen Moyer worked with Ron Perlman.
  [g24a_fever_188140] Stephen Moyer worked with Ron Perlman as his co-star in Prince Valiant.
  [g24a_fever_188141] Stephen Moyer acted in a film adaptation of a the Prince Valiant comic.
  [g24a_fever_188142] Stephen Moyer and Ron Perlman worked together.
  [g24a_fever_188147] Stephen Moyer was in Prince Valiant.
DEC claims (2):
  [g24a_fever_188129] Stephen Moyer was refused any role in Prince Valiant.
  [g24a_fever_188145] Stephen Moyer refused to ever work with Ron Perlman.

## sha=9ede29b5dd source=fever n_inc=3 n_dec=5
EVIDENCE: The Armenian Genocide (Հայոց ցեղասպանություն, Hayots tseghaspanutyun), also known as the Armenian Holocaust, was the Ottoman government's systematic extermination of 1.5 million Armenians, mostly Ottoman citizens within the Ottoman Empire and its successor state, the Republic of Turkey.
INC claims (3):
  [g24a_fever_140522] The Armenian Genocide was an extermination.
  [g24a_fever_3106] The Armenian Genocide was the Ottoman government's systematic extermination of 1.5 million Armenians.
  [g24a_fever_38125] The Armenian Genocide was the killing of Armenians who were mostly Ottoman natives.
DEC claims (5):
  [g24a_fever_120190] The Armenian Genocide was the extermination of Armenians who were mostly Turkish citizens.
  [g24a_fever_49192] The Armenian Genocide rarely was the extermination of Armenians who were mostly Ottoman citizens.
  [g24a_fever_5177] The Armenian Genocide also fails to be known as the Armenian Holocaust.
  [g24a_fever_93621] The Armenian Genocide was the Ottoman government's systematic extermination of 1.5 million Jews.
  [g24a_fever_9945] The Armenian Genocide took place outside the Ottoman Empire and the Republic of Turkey.

## sha=428b3ea1c3 source=scifact n_inc=1 n_dec=1
EVIDENCE: In vitro, increasing microtubule acetylation using deacetylase inhibitors or the tubulin acetylase αTAT1 prevents association of mutant LRRK2 with microtubules, and the deacetylase inhibitor trichostatin A (TSA) restores axonal transport. In vivo knockdown of the deacetylases HDAC6 and Sirt2, or administration of TSA rescues both axonal transport and locomotor behavior.
INC claims (1):
  [g24a_scifact_614] Increased microtubule acetylation repairs interference of axonal transport caused by LRRK2 Roc-COR domain mutations.
DEC claims (1):
  [g24a_scifact_615] Increased microtubule acetylation worsens interference of axonal transport caused by LRRK2 Roc-COR domain mutations.

## sha=cae3e50ea1 source=scifact n_inc=1 n_dec=1
EVIDENCE: Here Gpr124 conditional knockout (CKO) in the endothelia of adult mice did not affect homeostatic BBB integrity, but resulted in BBB disruption and microvascular hemorrhage in mouse models of both ischemic stroke and glioblastoma, accompanied by reduced cerebrovascular canonical Wnt–β-catenin signaling.
INC claims (1):
  [g24a_scifact_480] Gpr124 suppresses BBB breakdown in mouse models of ischemic stroke.
DEC claims (1):
  [g24a_scifact_479] Gpr124 increases BBB breakdown in mouse models of ischemic stroke.

## sha=70abb33f26 source=fever n_inc=3 n_dec=5
EVIDENCE: Wilhelmina Vivian Slater (born Wanda Slater) is a fictional character in the American dramedy series Ugly Betty.
INC claims (3):
  [g24a_fever_128243] Wilhelmina Slater is a person.
  [g24a_fever_149756] The middle name of Wilhelmina Slater is Vivian.
  [g24a_fever_9234] Wilhelmina Slater is portrayed in a comedy-drama television series.
DEC claims (5):
  [g24a_fever_43644] Wilhelmina Slater name at birth was Wanda Smith.
  [g24a_fever_46636] Wilhelmina Slater is portrayed only in comedy-drama radio.
  [g24a_fever_46883] Wilhelmina Slater is a fictional setting.
  [g24a_fever_48922] Wilhelmina Slater is a real person.
  [g24a_fever_66415] Wilhelmina Slater's business partner is Vivian.

## sha=c8bbf16b70 source=fever n_inc=2 n_dec=1
EVIDENCE: However, the Faroe Islands, also a Danish overseas territory, are sometimes included, as sometimes are Iceland, Finland, and the Finnish autonomous region of the Åland Islands, because of their historical association with the Scandinavian countries and the Scandinavian peoples and languages.
INC claims (2):
  [g24a_fever_63185] Finland is sometimes considered a part of Scandinavia.
  [g24a_fever_84673] Finland is sometimes thought to be a part of Scandinavia.
DEC claims (1):
  [g24a_fever_124986] Scandinavia does not include territory.

## sha=01df2d47f2 source=fever n_inc=1 n_dec=1
EVIDENCE: Mirny was a 20-gun sloop-of-war of the Imperial Russian Navy, the second ship of the First Russian Antarctic Expedition in 1819 -- 1821, during which Faddey Bellingshausen (commander of the lead ship Vostok) and Mikhail Lazarev (commanding Mirny) circumnavigated the globe, discovered the continent of Antarctica and twice circumnavigated it, and discovered a number of islands and archipelagos in the Southern Ocean and the Pacific. The Imperial Russian Navy was the navy of the Russian Empire.
INC claims (1):
  [g24a_fever_70780] The Mirny (sloop-of-war) was a ship of the navy of the Russian Empire.
DEC claims (1):
  [g24a_fever_99974] The Mirny (sloop-of-war) was a ship of the Royal Navy.

## sha=12eac1d2fd source=fever n_inc=7 n_dec=10
EVIDENCE: French Indochina (previously spelled as French Indo-China) (Indochine française សហភ ពឥណ ឌ ច ន Đông Dương thuộc Pháp, [ɗə̄wŋm jɨ̄əŋ tʰûək fǎp], frequently abbreviated to Đông Pháp; ຝຣັ່ງແຫຼັມອິນດູຈີນ Cantonese:), officially known as the Indochinese Union (Union indochinoise) after 1887 and the Indochinese Federation (Fédération indochinoise) after 1947, was a grouping of French colonial territories in Southeast Asia.
INC claims (7):
  [g24a_fever_100358] French Indochina was officially known as the Indochinese Union after 1887.
  [g24a_fever_100967] French Indochina was officially known as the Indochinese Union then the Indochinese Federation.
  [g24a_fever_103951] French Indochina was in Southeast Asia.
  [g24a_fever_121093] French Indochina was a grouping of French colonial territories.
  [g24a_fever_121094] There was a grouping of French colonial territories called French Indochina.
  [g24a_fever_158383] After 1887, French Indochina was officially known as the Indochinese Union.
  [g24a_fever_160864] Frequently, French Indochina is abbreviated.
DEC claims (10):
  [g24a_fever_104152] French Indochina was a grouping of French colonial dogs in Southeast Asia.
  [g24a_fever_106115] French Indochina was officially known as the Indochinese Federation after 1955.
  [g24a_fever_133963] French Indochina was only ever spelled in one way.
  [g24a_fever_143060] French Indochina was officially known as Mario after 1947.
  [g24a_fever_152634] French Indochina was only in Northeast Asia.
  [g24a_fever_160304] French Indochina was unofficially known as the Indochinese Union then the Indochinese Federation.
  [g24a_fever_160414] French Indochina was a grouping of British colonial territories in Southeast Asia.
  [g24a_fever_160932] French Indochina was a grouping of British colonial territories.
  [g24a_fever_160985] French Indochina is never abbreviated.
  [g24a_fever_161094] French Indochina was a grouping of territories.

## sha=828b973030 source=fever n_inc=3 n_dec=2
EVIDENCE: Khan was the first R&B artist to have a crossover hit featuring a rapper, with "I Feel for You" in 1984.
INC claims (3):
  [g24a_fever_119048] Chaka Khan had a music hit featuring at least one person.
  [g24a_fever_21221] A song by Chaka Khan was released in the 20th century.
  [g24a_fever_61937] A rapper was featured on a crossover hit by Chaka Khan.
DEC claims (2):
  [g24a_fever_47630] "I Feel for You" by Chaka Khan was released five years after 1984.
  [g24a_fever_84516] Chaka Khan had a crossover hit without any features.

## sha=68eee42d27 source=fever n_inc=4 n_dec=8
EVIDENCE: The Town of Watertown is a city in Middlesex County, Massachusetts, United States.
INC claims (4):
  [g24a_fever_106498] Watertown, Massachusetts is a city.
  [g24a_fever_29848] Watertown, Massachusetts is in the United States.
  [g24a_fever_32711] Watertown, Massachusetts is a city in Middlesex County.
  [g24a_fever_67572] Massachusetts contains Watertown, Massachusetts.
DEC claims (8):
  [g24a_fever_116464] Watertown, Massachusetts is a city in Suffolk County.
  [g24a_fever_118593] Middlesex County is home to the city of Watertown, Massachusetts.
  [g24a_fever_157022] Watertown, Massachusetts is in the United Kingdom.
  [g24a_fever_25008] Watertown, Massachusetts is in Vermont.
  [g24a_fever_29849] Watertown, Massachusetts is a Dutch city.
  [g24a_fever_39121] Watertown, Massachusetts is outside of any named county.
  [g24a_fever_4824] Watertown, Massachusetts is in France.
  [g24a_fever_81775] Watertown, Massachusetts is in Missouri.

## sha=43e9793d81 source=fever n_inc=3 n_dec=2
EVIDENCE: In 2016, Chatwin starred in the CBS summer mystery series American Gothic and in the Christmas 2016 episode of the BBC UK television series Doctor Who, "The Return of Doctor Mysterio", in which he played the character of Grant, loosely based upon Superman/Clark Kent.
INC claims (3):
  [g24a_fever_115628] Justin Chatwin performed in the CBS series American Gothic.
  [g24a_fever_157640] Justin Chatwin starred in Doctor Who.
  [g24a_fever_91165] Justin Chatwin performed in the BBC UK series Doctor Who.
DEC claims (2):
  [g24a_fever_150763] Justin Chatwin did not perform in American Gothic.
  [g24a_fever_89875] Justin Chatwin did not perform in Doctor Who.

## sha=4bca426c65 source=fever n_inc=3 n_dec=3
EVIDENCE: The Qin dynasty introduced several reforms: currency, weights and measures were standardized, and a uniform system of writing was established.
INC claims (3):
  [g24a_fever_14501] Qin dynasty introduced several legislation.
  [g24a_fever_47736] Qin dynasty worked with currency.
  [g24a_fever_53204] There was a uniform system of writing established in the Qin dynasty.
DEC claims (3):
  [g24a_fever_52788] Qin dynasty is incapable of working with measurements.
  [g24a_fever_71352] Qin dynasty was incapable of working with currency.
  [g24a_fever_95018] Qin dynasty is incapable of establishing a uniform system of writing.

## sha=f2894bdc91 source=fever n_inc=2 n_dec=3
EVIDENCE: Simon Phillip Cowell ([ˈkaʊəl]) (born 7 October 1959) is an English reality television judge and producer, entrepreneur, and philanthropist.
INC claims (2):
  [g24a_fever_27775] Simon Cowell is someone that donates money to certain causes.
  [g24a_fever_58234] Simon Cowell gives money.
DEC claims (3):
  [g24a_fever_66557] Simon Cowell is an English science-fiction television judge.
  [g24a_fever_92128] Simon Cowell is a English bulldog.
  [g24a_fever_97649] Simon Cowell is a miser.

## sha=9f31ced723 source=fever n_inc=3 n_dec=1
EVIDENCE: In 2013, he starred in Make Your Move, a Romeo and Juliet-inspired South Korean-American independent dance film.
INC claims (3):
  [g24a_fever_2406] Derek Hough starred in a movie.
  [g24a_fever_5985] Derek Hough starred in a Romeo and Juliet-inspired movie.
  [g24a_fever_60307] Derek Hough starred in an independent dance film.
DEC claims (1):
  [g24a_fever_55976] Derek Hough starred in an American song.

## sha=b32341abe6 source=fever n_inc=4 n_dec=3
EVIDENCE: The Hyksos practiced horse burials, and their chief deity, their native storm god, Baal, became associated with the Egyptian storm and desert god, Set.
INC claims (4):
  [g24a_fever_195923] Hyksos practiced horse burials.
  [g24a_fever_195925] The Hyksos' chief deity became associated with a god of the desert.
  [g24a_fever_195931] The Hyksos' chief deity was Baal.
  [g24a_fever_195933] Hyksos performed horse burials.
DEC claims (3):
  [g24a_fever_195924] Hyksos always banned horse burials.
  [g24a_fever_195940] The Hyksos' chief deity was Zeus.
  [g24a_fever_195943] The Hyksos' least important deity was Baal.

## sha=a0ac204db5 source=fever n_inc=2 n_dec=3
EVIDENCE: He also produced and directed music videos and aspired to be a film director.
INC claims (2):
  [g24a_fever_47222] Heath Ledger directed music videos.
  [g24a_fever_81439] Music videos have been directed by Heath Ledger.
DEC claims (3):
  [g24a_fever_47223] Heath Ledger did not direct music videos.
  [g24a_fever_68930] Heath Ledger aspired to be a doctor.
  [g24a_fever_81912] Heath Ledger did not aspire to be a film director.

## sha=918ac3db37 source=fever n_inc=4 n_dec=1
EVIDENCE: It was designed by renowned Bay Area architect John Galen Howard and built in 1915 as part of the Panama -- Pacific International Exposition.
INC claims (4):
  [g24a_fever_158635] Bill Graham Civic Auditorium was built in 1915.
  [g24a_fever_158636] Bill Graham Civic Auditorium was designed in 1915.
  [g24a_fever_158648] Bill Graham Civic Auditorium was built as part of an exposition.
  [g24a_fever_158654] Bill Graham Civic Auditorium was built in the 1910s.
DEC claims (1):
  [g24a_fever_158644] Bill Graham Civic Auditorium was built before 1915.

## sha=2cf137560e source=fever n_inc=3 n_dec=2
EVIDENCE: The critically acclaimed first season had a run of 23 episodes and garnered an average of 14.3 million viewers in the United States, receiving the highest rating for an NBC drama premiere in five years.
INC claims (3):
  [g24a_fever_84959] Heroes first season averaged 14.3 billion viewers.
  [g24a_fever_90980] Heroes first season averaged over a million viewers.
  [g24a_fever_96841] Heroes had a season with over 20 episodes.
DEC claims (2):
  [g24a_fever_110514] Heroes first season had less than 1 million viewers for each episode.
  [g24a_fever_144200] Heroes' first season had 12 episodes.

## sha=e8f0ed13cb source=fever n_inc=1 n_dec=2
EVIDENCE: Nicknamed "the Red Devils", the club was founded as Newton Heath LYR Football Club in 1878, changed its name to Manchester United in 1902 and moved to its current stadium, Old Trafford, in 1910.
INC claims (1):
  [g24a_fever_144102] Manchester United's first name was the Newton Heath LYR Football Club.
DEC claims (2):
  [g24a_fever_101906] Manchester United has had multiple home stadiums.
  [g24a_fever_57245] Manchester United's current name is the Newton Heath LYR Football Club.

## sha=c8185c1167 source=fever n_inc=1 n_dec=3
EVIDENCE: Jenna Jameson (born Jenna Marie Massoli; April 9, 1974) is an American entrepreneur, webcam model and former pornographic film actress, who has been called the world's most famous adult entertainment performer and "The Queen of Porn".
INC claims (1):
  [g24a_fever_8505] Jenna Jameson was photographed in the past.
DEC claims (3):
  [g24a_fever_226864] Jenna Jameson was incapable of modeling.
  [g24a_fever_226880] Jenna Jameson was only ever a stripper.
  [g24a_fever_90469] Jenna Jameson has only been in newspaper advertising.

## sha=52dd946655 source=fever n_inc=6 n_dec=7
EVIDENCE: Harrison's first marriage, to model Pattie Boyd in 1966, ended in divorce in 1977.
INC claims (6):
  [g24a_fever_129767] George Harrisongot married in 1966.
  [g24a_fever_2223] George Harrison's first marriage started in 1966.
  [g24a_fever_36298] George Harrison was married to Pattie Boyd.
  [g24a_fever_50143] Pattie Boyd and George Harrison divorced in 1977.
  [g24a_fever_69640] Pattie Boyd and George Harrison were married.
  [g24a_fever_97752] In 1966, George Harrison got married for the first time.
DEC claims (7):
  [g24a_fever_103941] George Harrison got divorced from Pattie Boyd in 1979.
  [g24a_fever_110925] George Harrison married his second wife in 1958.
  [g24a_fever_116686] George Harrison has been single his whole life.
  [g24a_fever_120026] George Harrison is still married to his first wife.
  [g24a_fever_127955] George Harrison's first marriage started in 1964.
  [g24a_fever_131584] George Harrison has yet to marry.
  [g24a_fever_85338] George Harrison was married to Pattie Boyd in 1970.

## sha=9a8e4ffa1e source=fever n_inc=6 n_dec=4
EVIDENCE: At the 2010 census, the city population was 145,170, and its metropolitan area had a population of 662,577.
INC claims (6):
  [g24a_fever_171594] Syracuse, New York, had a population of 145,170 according to the 2010 United States Census.
  [g24a_fever_171597] Syracuse, New York, had a population of 145,170 in 2010.
  [g24a_fever_171603] The 2010 population of Syracuse, New York, was 145,170.
  [g24a_fever_171604] In 2010, the metropolitan area of Syracuse, New York, had a metropolitan population of more than 600,000.
  [g24a_fever_171611] Syracuse, New York, claimed a population of 145,170 residents according to the 2010 United States Census.
  [g24a_fever_171614] Syracuse, New York, had a metropolitan area with a population of more than 600,000 residents according to the 2010 Census.
DEC claims (4):
  [g24a_fever_171595] Syracuse, New York, had a population of 50,000 according to the 2010 United States Census.
  [g24a_fever_171600] Syracuse, New York, had a metropolitan population of 600,000 in 2010.
  [g24a_fever_171605] Syracuse, New York, had a population of 145,170 according to the 1999 AAA TourBook.
  [g24a_fever_171613] Syracuse, New York, had a sparse metropolitan population of three hundred fifty in 2010.

## sha=3ae70069d7 source=scifact n_inc=1 n_dec=1
EVIDENCE: We demonstrate here that metabolism by intestinal microbiota of dietary L-carnitine, a trimethylamine abundant in red meat, also produces TMAO and accelerates atherosclerosis in mice. Chronic dietary L-carnitine supplementation in mice altered cecal microbial composition, markedly enhanced synthesis of TMA and TMAO, and increased atherosclerosis, but this did not occur if intestinal microbiota was concurrently suppressed.
INC claims (1):
  [g24a_scifact_524] Higher plasma levels of I-carnitine, when associated with trimethylamine N-oxide, are positively correlated with cardiovascular events in humans.
DEC claims (1):
  [g24a_scifact_523] Higher plasma levels of I-carnitine, when associated with trimethylamine N-oxide, are negatively correlated with cardiovascular events in humans.

## sha=87a4d1344c source=fever n_inc=4 n_dec=1
EVIDENCE: He spent the remaining years of his life on his ranch, the "Whispering Wind," near Creston, California, where he died in 1986.
INC claims (4):
  [g24a_fever_194742] L. Ron Hubbard died in California.
  [g24a_fever_194753] L. Ron Hubbard spent the remaining years of his life on a ranch.
  [g24a_fever_194754] L. Ron Hubbard spent the remaining years of his life at his ranch the "Whispering Wind."
  [g24a_fever_194758] L. Ron Hubbard spent the remaining years of his life on his ranch the "Whispering Wind."
DEC claims (1):
  [g24a_fever_194748] L. Ron Hubbard spent the remaining years of his life solely in Germany.

## sha=eea5f2f62e source=fever n_inc=2 n_dec=1
EVIDENCE: It also incorporates elements of other genres, such as reggae, soul and pop rock, in its production.
INC claims (2):
  [g24a_fever_54417] Paris (Paris Hilton album) incorporates elements of pop rock.
  [g24a_fever_93689] Paris (Paris Hilton album) is devoid of elements of soul.
DEC claims (1):
  [g24a_fever_96079] Paris (Paris Hilton album) is without elements of reggae.

## sha=f0a99e9777 source=fever n_inc=3 n_dec=2
EVIDENCE: In January 2016, a tenth season of The X-Files aired, featuring Carter as executive producer and writer, and starring David Duchovny and Gillian Anderson.
INC claims (3):
  [g24a_fever_174611] The X-Files starred David Duchovny.
  [g24a_fever_174615] The X-Files starred David Duchovny as the lead role.
  [g24a_fever_174628] The X-Files starred an actor.
DEC claims (2):
  [g24a_fever_174618] The X-Files had only eight seasons.
  [g24a_fever_174630] The X-Files refused to cast David Duchovny.

