# Blind taxonomy audit batch 3/3 (G24A fresh-pair census)

Classify each group's contradiction form into exactly one of:
explicit_negation, antonym_opposite, exclusive_alternative,
numeric_value, indirect_contradiction (definitions in the task
prompt). This file contains NO pre-existing labels - it is blind.

## sha=ec9ceadbb9 source=fever n_inc=4 n_dec=9
EVIDENCE: Ibsen was present at the world premiere, which took place on 31 January 1891 at the Residenztheater in Munich.
INC claims (4):
  [g24a_fever_105835] Hedda Gabler's world premiere was in Munich.
  [g24a_fever_122692] The Residenztheater is where Hedda Gabler's world premiere took place.
  [g24a_fever_150905] Hedda Gabler's world premiere took place at a theater.
  [g24a_fever_67856] Hedda Gabler's world premiere was on January 31st, 1891.
DEC claims (9):
  [g24a_fever_102151] Hedda Gabler's world premiere was attended by pelicans.
  [g24a_fever_104982] Hedda Gabler's world premiere took place at the Globe Theatre.
  [g24a_fever_113302] Hedda Gabler's world premiere took place in Prague.
  [g24a_fever_26839] Hedda Gabler's world premiere took place at the Battle of Hastings.
  [g24a_fever_49268] Hedda Gabler's world premiere took place before January 31st, 1891.
  [g24a_fever_75538] Hedda Gabler's world premiere took place in Schwabing.
  [g24a_fever_75587] Hedda Gabler's world premiere took place outside Munich.
  [g24a_fever_77873] Hedda Gabler's world premiere had zero attendance.
  [g24a_fever_89719] Hedda Gabler's world premiere took place on May 31st, 1891.

## sha=c1007fe577 source=fever n_inc=3 n_dec=2
EVIDENCE: Shane Brandon McMahon (born January 15, 1970) is an American businessman and part-time professional wrestler who is a minority owner of WWE and the vice-chairman of Wecast Holdings Inc..
INC claims (3):
  [g24a_fever_30745] Shane McMahon worked for WWE.
  [g24a_fever_75389] Shane McMahon worked in professional wrestling.
  [g24a_fever_98875] Shane McMahon is an athlete.
DEC claims (2):
  [g24a_fever_145013] Shane McMahon is not a wrestler.
  [g24a_fever_97418] Shane McMahon is a balloon.

## sha=834907b420 source=fever n_inc=5 n_dec=4
EVIDENCE: Gin is a spirit which derives its predominant flavour from juniper berries (Juniperus communis).
INC claims (5):
  [g24a_fever_138949] Gin derives part of its flavour from berries.
  [g24a_fever_16161] Gin derives its main flavour from juniper berries.
  [g24a_fever_23147] Gin is a spirit.
  [g24a_fever_31885] Gin is a drink.
  [g24a_fever_86914] Gin is a berry flavoured spirit.
DEC claims (4):
  [g24a_fever_145624] Gin does not derive its main flavour from juniper berries.
  [g24a_fever_34545] Gin is a spirit which derives its predominant flavour from motor oil.
  [g24a_fever_46666] Gin derives its main flavour from strawberries.
  [g24a_fever_66351] Gin is not a spirit.

## sha=7610adaf66 source=scifact n_inc=1 n_dec=1
EVIDENCE: Analysis of the genome sequence indicates that the genome is 7489 bp in size and that the transcribed strand contains three open reading frames capable of encoding proteins of 23, 15 and 216 kd.
INC claims (1):
  [g24a_scifact_279] Commelina yellow mottle virus' (ComYMV) genome consists of 7489 baise pairs.
DEC claims (1):
  [g24a_scifact_278] Commelina yellow mottle virus' (ComYMV) genome consists of 2140 baise pairs.

## sha=489b15b6d8 source=fever n_inc=5 n_dec=5
EVIDENCE: Saturn is the sixth planet from the Sun and the second-largest in the Solar System, after Jupiter.
INC claims (5):
  [g24a_fever_198208] Saturn is smaller than Jupiter.
  [g24a_fever_198210] Saturn is the sixth planet from the Sun.
  [g24a_fever_198216] Saturn is the second-largest planet in the Solar System.
  [g24a_fever_198217] The second-largest planet in the Solar System is Saturn.
  [g24a_fever_198218] Saturn is a planet in the Solar System.
DEC claims (5):
  [g24a_fever_198221] Saturn is larger than Jupiter.
  [g24a_fever_198225] Saturn is the ninth planet from the Sun.
  [g24a_fever_198227] Saturn is only an asteroid.
  [g24a_fever_198231] Saturn is the third-largest planet in the Solar System.
  [g24a_fever_198234] Saturn is the second-largest moon in the Solar System.

## sha=dd91e1fa69 source=fever n_inc=2 n_dec=1
EVIDENCE: Dawood Ibrahim (Marathi: दाऊद इब्राहीम कासकर, born Dawood Ibrahim Kaskar 26 December 1955), known as Dawood Bhai or simply Bhai is a gangster and terrorist originally from Dongri in Mumbai, India. Mumbai ([mʊmˈbaɪ] also known as Bombay, the official name until 1995) is the capital city of the Indian state of Maharashtra.
INC claims (2):
  [g24a_fever_178855] Dawood Ibrahim is originally from the capital city of the Indian state of Maharashtra.
  [g24a_fever_178856] Dawood Ibrahim originally comes from the capital city of the Indian state of Maharashtra.
DEC claims (1):
  [g24a_fever_178909] Dawood Ibrahim is originally from the capital city of the Indian state of Kerala.

## sha=a4f72f7736 source=fever n_inc=3 n_dec=1
EVIDENCE: The popularity of The Beatles and other groups from the Merseybeat era contributes to Liverpool's status as a tourist destination.
INC claims (3):
  [g24a_fever_106010] Liverpool is a tourist destination because of The Beatles.
  [g24a_fever_44427] Liverpool is a tourist destination.
  [g24a_fever_68701] Liverpool was where The Beatles came together.
DEC claims (1):
  [g24a_fever_118068] Liverpool is unrelated to The Beatles.

## sha=a658b8dc16 source=scifact n_inc=1 n_dec=1
EVIDENCE: Here, we show that classical noncoding RNAs and 5' UTRs show the same ribosome occupancy as lincRNAs, demonstrating that ribosome occupancy alone is not sufficient to classify transcripts as coding or noncoding.
INC claims (1):
  [g24a_scifact_880] Occupancy of ribosomes by IncRNAs mirror 5 0-UTRs
DEC claims (1):
  [g24a_scifact_879] Occupancy of ribosomes by IncRNAs do not make functional peptides.

## sha=83952e3102 source=fever n_inc=1 n_dec=2
EVIDENCE: In 2015, she was named Esquires Sexiest Woman Alive.
INC claims (1):
  [g24a_fever_95547] In 2015, Emilia Clarke was named Esquires Sexiest Woman Alive.
DEC claims (2):
  [g24a_fever_122159] In 2015, Emilia Clarke was named Esquire's Ugliest Woman Alive.
  [g24a_fever_44787] In 2016, Emilia Clarke was named Esquire's Sexiest Woman Alive.

## sha=9c9b8e997b source=fever n_inc=7 n_dec=5
EVIDENCE: The Bermuda Triangle, also known as the Devil's Triangle, is a loosely-defined region in the western part of the North Atlantic Ocean, where a number of aircraft and ships are said to have disappeared under mysterious circumstances.
INC claims (7):
  [g24a_fever_186976] Bermuda Triangle is where a number of aircraft and ships have disappeared.
  [g24a_fever_186977] Bermuda Triangle is where a number of aircraft and ships have disappeared under mysterious circumstances.
  [g24a_fever_186978] Bermuda Triangle is also known as the Devil's Triangle.
  [g24a_fever_186979] Bermuda Triangle is also referred to as the Devil's Triangle.
  [g24a_fever_186987] Bermuda Triangle is where things have disappeared.
  [g24a_fever_186994] The western part of the Atlantic Ocean is the location of the Bermuda Triangle.
  [g24a_fever_186996] Bermuda Triangle is also known by another name.
DEC claims (5):
  [g24a_fever_186988] The Bermuda Triangle is known by no other name.
  [g24a_fever_186990] Bermuda Triangle is a loosely-defined region in the Pacific Ocean.
  [g24a_fever_186995] The Bermuda Triangle is located completely within the Dead Sea.
  [g24a_fever_186998] Bermuda Triangle is in the eastern part of the Atlantic Ocean.
  [g24a_fever_187000] Bermuda Triangle is in the western part of the Himalayas.

## sha=e77efdb9ab source=scifact n_inc=1 n_dec=1
EVIDENCE: Converting ApoE4 to ApoE3 by gene editing rescued these phenotypes, indicating the specific effects of ApoE4.
INC claims (1):
  [g24a_scifact_286] Converting apoE4 to apoE3 by gene editing prevents the pathology associated with apoE4 in human iPSCderived neurons.
DEC claims (1):
  [g24a_scifact_287] Converting apoE4 to apoE3 by gene editing worsens the pathology associated with apoE4 in human iPSCderived neurons.

## sha=f3361096a8 source=scifact n_inc=1 n_dec=1
EVIDENCE: Under inflammatory conditions elicited either by acute infection with Listeria monocytogenes or chronic infection with Leishmania major, there was a significant increase in immature Ly-6C(high) monocytes, resembling the inflammatory left shift of granulocytes. In addition, acute peritoneal inflammation recruited preferentially Ly-6C(med-high) monocytes.
INC claims (1):
  [g24a_scifact_726] Ly6C hi monocytes have a higher inflammatory capacity than Ly6C lo monocytes.
DEC claims (1):
  [g24a_scifact_728] Ly6C hi monocytes have a lower inflammatory capacity than Ly6C lo monocytes.

## sha=ea8f63b767 source=fever n_inc=3 n_dec=4
EVIDENCE: Superhuman abilities may result from human enhancement by genetic modification, cybernetic implants, nanotechnology, radiation or from human evolution in the future.
INC claims (3):
  [g24a_fever_43667] Superhuman abilities may result from human enhancement by genetic modification.
  [g24a_fever_60038] Superhuman abilities may result from human enhancement by nanotechnology.
  [g24a_fever_62779] Superhuman abilities may come about from human enhancement by cybernetic implants.
DEC claims (4):
  [g24a_fever_117552] Superhuman abilities may result from dog enhancement by genetic modification.
  [g24a_fever_153539] Superhuman abilities may be impeded by human enhancement by nanotechnology.
  [g24a_fever_51262] Superhuman abilities may result from antelope enhancement by human evolution.
  [g24a_fever_60039] Superhuman abilities may result from frog enhancement by nanotechnology.

## sha=0f75314153 source=fever n_inc=5 n_dec=7
EVIDENCE: Charles Milles Manson (born Charles Milles Maddox, November 12, 1934) is an American criminal and former cult leader who led what became known as the Manson Family, a quasi-commune that arose in California in the late 1960s.
INC claims (5):
  [g24a_fever_13069] Charles Manson is an American.
  [g24a_fever_143028] Charles Manson was the leader of what would later be known as the Manson Family.
  [g24a_fever_151357] Charles Manson is a former leader.
  [g24a_fever_18707] Charles Manson is a criminal.
  [g24a_fever_84839] Charles Manson led a sort-of-commune that came into being in California in the late 1960s.
DEC claims (7):
  [g24a_fever_137741] Charles Manson led a quasi-commune that arose in Massachusetts in the late 1960s.
  [g24a_fever_33011] Charles Manson led what became known as The Brethren.
  [g24a_fever_46004] Charles Manson is a Spaniard.
  [g24a_fever_68022] Charles Manson is a former cult leader.
  [g24a_fever_76482] Charles Manson led a quasi-commune that arose in Vermont in the late 1960s.
  [g24a_fever_84472] Charles Manson is a current cult leader.
  [g24a_fever_92816] Charles Manson is a former teacher.

## sha=aecedf3c2d source=fever n_inc=1 n_dec=2
EVIDENCE: Mohra (Pawn) is a 1994 Indian action thriller film directed by Rajiv Rai starring Akshay Kumar, Sunil Shetty, Raveena Tandon and Naseeruddin Shah in the lead roles with Paresh Rawal, Gulshan Grover, Raza Murad and Sadashiv Amrapurkar in supporting roles.
INC claims (1):
  [g24a_fever_147845] Mohra is a work.
DEC claims (2):
  [g24a_fever_128123] Mohra is a truck.
  [g24a_fever_24247] Mohra has yet to be made into a film.

## sha=d81bb3dfe4 source=fever n_inc=2 n_dec=1
EVIDENCE: It portrays soldiers of C Company, 1st Battalion, 27th Infantry Regiment, 25th Infantry Division, played by Sean Penn, Jim Caviezel, Nick Nolte, Elias Koteas and Ben Chaplin.
INC claims (2):
  [g24a_fever_168608] The Thin Red Line (1998 film) portrays soldiers.
  [g24a_fever_168612] The Thin Red Line (1998 film) features a performance by Sean Penn.
DEC claims (1):
  [g24a_fever_168634] The Thin Red Line (1998 film) has an all-female cast.

## sha=5adef5423d source=fever n_inc=2 n_dec=1
EVIDENCE: Marjorie Gross (April 18, 1956 -- June 7, 1996) was a television writer and producer.
INC claims (2):
  [g24a_fever_132151] Marjorie Gross wrote for a television show.
  [g24a_fever_190755] Marjorie Gross was a writer.
DEC claims (1):
  [g24a_fever_62877] Marjorie Gross is unable to write.

## sha=76f5fdd9ef source=scifact n_inc=1 n_dec=1
EVIDENCE: Compared to women with a score of zero, hazard ratios (95% confidence intervals) for women with four to five factors were 0.57 (0.44-0.74) for total mortality, 0.29 (0.16-0.54) for CVD mortality, and 0.76 (0.54-1.06) for cancer mortality. The population attributable risks for not having 4-5 healthy lifestyle factors were 33% for total deaths, 59% for CVD deaths, and 19% for cancer deaths. CONCLUSIONS In this first study, to our knowledge, to quantify the combined impact of lifestyle-related factors on mortality outcomes in Chinese women, a healthier lifestyle pattern-including being of normal weight, lower central adiposity, participation in physical activity, nonexposure to spousal smoking, and higher fruit and vegetable intake-was associated with reductions in total and cause-specific mortality among lifetime nonsmoking and nondrinking women, supporting the importance of overall lifestyle modification in disease prevention.
INC claims (1):
  [g24a_scifact_397] Exercise reduces cancer mortality rates among Chinese citizens.
DEC claims (1):
  [g24a_scifact_396] Exercise increases cancer mortality rates among Chinese citizens.

## sha=2c8997d469 source=fever n_inc=4 n_dec=7
EVIDENCE: Soyuz (Сою́з [sɐˈjʉs], "Union", as in Сове́тский Сою́з, "Sovetskiy Soyuz", "Soviet Union") is a series of spacecraft designed for the Soviet space programme by the Korolyov Design Bureau (now RKK Energia) in the 1960s that remains in service today.
INC claims (4):
  [g24a_fever_16527] Soyuz was designed in the 1960s.
  [g24a_fever_27040] Soyuz was part of a space program.
  [g24a_fever_3492] Soyuz was part of the Soviet space program.
  [g24a_fever_87195] Soyuz is still in existence.
DEC claims (7):
  [g24a_fever_141159] Soyuz is a series of movies.
  [g24a_fever_152117] Soyuz was designed in the 1930s.
  [g24a_fever_154905] Soyuz is a series of watercraft.
  [g24a_fever_28657] Soyuz was part of the American space program.
  [g24a_fever_33368] Soyuz was designed in the 1970s.
  [g24a_fever_63757] Soyuz is still in beta mode.
  [g24a_fever_76531] Soyuz was taken out of service in 1991.

## sha=f5da43e40c source=fever n_inc=1 n_dec=1
EVIDENCE: His most important role came as the highly energetic Prime Minister of the Wartime Coalition Government (1916 -- 22), during and immediately after the First World War.
INC claims (1):
  [g24a_fever_225722] David Lloyd George was a prime minister.
DEC claims (1):
  [g24a_fever_225744] David Lloyd George lost every bid to become prime minister.

## sha=3173d92130 source=fever n_inc=5 n_dec=5
EVIDENCE: Warming is expected to be greater over land than over the oceans and greatest in the Arctic, with the continuing retreat of glaciers, permafrost and sea ice.
INC claims (5):
  [g24a_fever_119437] Global warming is expected to result in the retreat of permafrost.
  [g24a_fever_120630] The retreat of permafrost is an expected outcome of global warming.
  [g24a_fever_138118] The retreat of sea ice is one of the expected outcomes of global warming.
  [g24a_fever_79601] Global warming is projected to result in reduced levels of sea ice.
  [g24a_fever_88907] Global warming is expected to be greatest in the Arctic.
DEC claims (5):
  [g24a_fever_120461] Global warming is expected to be greatest in the Caribbean.
  [g24a_fever_145079] Global warming will result in the expansion of permafrost.
  [g24a_fever_82780] Global warming will maintain the present levels of sea ice.
  [g24a_fever_85452] The glaciers will remain at their historic extent and size with global warming.
  [g24a_fever_96906] The Arctic will be unaffected by global warming.

## sha=45702fbb74 source=fever n_inc=1 n_dec=1
EVIDENCE: Christopher Emmanuel Paul (born May 6, 1985) is an American professional basketball player for the Los Angeles Clippers of the National Basketball Association (NBA).
INC claims (1):
  [g24a_fever_131375] Chris Paul is a basketball player.
DEC claims (1):
  [g24a_fever_45018] Chris Paul is a point guard for the Lakers.

## sha=4dbf7e8d3d source=fever n_inc=2 n_dec=2
EVIDENCE: The film was produced by Revolution Studios and New Line Cinema, and distributed by Columbia Pictures; it features the video art of Jeremy Blake in the form of visual interludes. Columbia Pictures Industries, Inc. (known as Columbia Pictures and Columbia, and formerly CBC Film Sales Corporation) is an American film studio, production company and film distributor that is a member of the Sony Pictures Motion Picture Group, a division of Sony Entertainment's Sony Pictures subsidiary of the Japanese conglomerate Sony.
INC claims (2):
  [g24a_fever_206992] Punch-Drunk Love was distributed by an American film studio.
  [g24a_fever_207003] Punch-Drunk Love had an American film studio as a distributor.
DEC claims (2):
  [g24a_fever_207007] Punch-Drunk Love was distributed exclusively by a Czech film studio.
  [g24a_fever_207010] Punch-Drunk Love was distributed by an American television studio.

## sha=2a3255de71 source=fever n_inc=1 n_dec=1
EVIDENCE: "Rehab" has become a critical and commercial success internationally, and has been referred to as Winehouse's "signature song".
INC claims (1):
  [g24a_fever_10650] Rehab is Amy Winehouse's signature song.
DEC claims (1):
  [g24a_fever_144800] Rehab is Amy Winehouse's most obscure song.

## sha=afc8355d00 source=scifact n_inc=2 n_dec=1
EVIDENCE: By transducing cortical neurons with genes that were expressed more highly in granule cell neurons, we identified three interferon-stimulated genes (ISGs; Ifi27, Irg1 and Rsad2 (also known as Viperin)) that mediated the antiviral effects against different neurotropic viruses.
INC claims (2):
  [g24a_scifact_1020] Rapid up-regulation and higher basal expression of interferon-induced genes increase survival of granule cell neurons that are infected by West Nile virus.
  [g24a_scifact_549] IRG1 has antiviral effects against neurotropic viruses.
DEC claims (1):
  [g24a_scifact_1021] Rapid up-regulation and higher basal expression of interferon-induced genes reduce survival of granule cell neurons that are infected by West Nile virus.

## sha=a442ff0b62 source=fever n_inc=5 n_dec=6
EVIDENCE: Soul Food is a 1997 American comedy-drama film produced by Kenneth "Babyface" Edmonds, Tracey Edmonds and Robert Teitel and released by Fox 2000 Pictures.
INC claims (5):
  [g24a_fever_122828] Tracey Edmonds produced Soul Food.
  [g24a_fever_137334] Fox 2000 Pictures released the film Soul Food.
  [g24a_fever_15674] Soul Food was produced by Tracey Edmonds.
  [g24a_fever_6079] Soul Food was produced by Kenneth Edmonds.
  [g24a_fever_610] Soul Food was created in 1997.
DEC claims (6):
  [g24a_fever_130158] Soul Food was manufactured in 1930.
  [g24a_fever_33075] Soul Food is a jaguar.
  [g24a_fever_36332] Soul Foods was produced only by Tracey Edmonds.
  [g24a_fever_68576] Soul Food was only produced by Kenneth Edwards.
  [g24a_fever_83758] Soul Food was released by DreamWorks Animation.
  [g24a_fever_92231] Soul Food was released by spirits.

## sha=d1e7110d86 source=fever n_inc=1 n_dec=2
EVIDENCE: The Challenge XXX: Dirty 30 is the thirtieth season of the MTV reality competition series, The Challenge. MTV (originally an initialism of Music Television) is an American cable and satellite television channel owned by Viacom Media Networks (a division of Viacom) and headquartered in New York City.
INC claims (1):
  [g24a_fever_12612] The Challenge XXX: Dirty 30 is a season of an American TV show.
DEC claims (2):
  [g24a_fever_148779] The Challenge XXX: Dirty 30 is a season of an Australian TV show.
  [g24a_fever_77113] The Challenge XXX: Dirty 30 is not a season of a TV series.

## sha=252ec64d13 source=scifact n_inc=1 n_dec=1
EVIDENCE: Progression to invasion was promoted by fibroblasts and inhibited by normal myoepithelial cells. Molecular profiles of isolated luminal epithelial and myoepithelial cells identified an intricate interaction network involving TGFbeta, Hedgehog, cell adhesion, and p63 required for myoepithelial cell differentiation, the elimination of which resulted in loss of myoepithelial cells and progression to invasion.
INC claims (1):
  [g24a_scifact_570] In breast cancer, the loss of myoepithelial cells promotes the transition of ductal carcinoma in situ to invasive carcinoma.
DEC claims (1):
  [g24a_scifact_571] In breast cancer, the loss of myoepithelial cells slows the transition of ductal carcinoma in situ to invasive carcinoma.

## sha=37c6427257 source=scifact n_inc=1 n_dec=1
EVIDENCE: By contrast, on a stiff hydrogel matrix, hESCs show elevated integrin-dependent GSK3 and Src activity that promotes β-catenin degradation and inhibits differentiation.
INC claims (1):
  [g24a_scifact_1102] Stiff substrates inhibit mesodermal differentiation by degrading beta-catenin in an integrin-dependent manner.
DEC claims (1):
  [g24a_scifact_1101] Stiff substrates encourage mesodermal differentiation by degrading beta-catenin in an integrin-dependent manner.

## sha=0bb87e11b6 source=fever n_inc=1 n_dec=2
EVIDENCE: It is a remake of the 1972 Fist of Fury, which starred Bruce Lee as the lead character. Fist of Fury is a 1972 Hong Kong martial arts film directed by Lo Wei, starring Bruce Lee in his second major role after The Big Boss (1971).
INC claims (1):
  [g24a_fever_30805] Fist of Legend is a 1972 movie's remake.
DEC claims (2):
  [g24a_fever_124817] Fist of Legend is a remake of a poem by Lo Wei.
  [g24a_fever_130726] Fist of Legend is based on a Stephen Spielberg film.

## sha=663a0f0655 source=fever n_inc=2 n_dec=2
EVIDENCE: How to Train Your Dragon 2 benefited from advances in animation technology and was DreamWorks' first film to use scalable multicore processing and the studio's new animation and lighting software.
INC claims (2):
  [g24a_fever_11345] How to Train Your Dragon 2 used scalable multicore processing.
  [g24a_fever_11346] How to Train Your Dragon 2 used some type of processing.
DEC claims (2):
  [g24a_fever_20770] How to Train Your Dragon 2 refused to use scalable multicore processing.
  [g24a_fever_76123] How to Train Your Dragon 2 used new filming software.

## sha=537392041e source=fever n_inc=2 n_dec=4
EVIDENCE: Winehouse died of alcohol poisoning on 23 July 2011, aged 27.
INC claims (2):
  [g24a_fever_28544] Amy Winehouse died at age 27.
  [g24a_fever_71639] Amy Winehouse died of alcohol poisoning at age 27.
DEC claims (4):
  [g24a_fever_121913] Amy Winehouse did not die at age 27.
  [g24a_fever_14984] Amy Winehouse died of brain poisoning.
  [g24a_fever_28545] Amy Winehouse died at age 31.
  [g24a_fever_84643] Amy Winehouse died of nicotine poisoning.

## sha=7bfcfe375c source=fever n_inc=3 n_dec=7
EVIDENCE: The first inauguration of Bill Clinton as the 42nd President of the United States was held on January 20, 1993 on the West Front of the United States Capitol Building in Washington, D.C..
INC claims (3):
  [g24a_fever_129557] The first inauguration of Bill Clinton was in the United States.
  [g24a_fever_140196] The first inauguration of Bill Clinton was at the United States Capitol Building.
  [g24a_fever_147118] At the first inauguration of Bill Clinton, he became the 42nd President of the United States.
DEC claims (7):
  [g24a_fever_103893] The first inauguration of Bill Clinton was on the West Front of the White House lawn.
  [g24a_fever_11432] The first inauguration of Bill Clinton made him the 50th President of the United States.
  [g24a_fever_129378] The first inauguration of Bill Clinton was on Neptune.
  [g24a_fever_39342] The first inauguration of Bill Clinton made him the 22nd Super Bowl Most Valuable Player.
  [g24a_fever_77824] The first inauguration of Bill Clinton took place in Vietnam.
  [g24a_fever_78816] The first inauguration of Bill Clinton was held on July 4th.
  [g24a_fever_79525] The first inauguration of Bill Clinton was held on June 20th, 1993.

## sha=9d61837d2a source=fever n_inc=4 n_dec=1
EVIDENCE: Danielle Cormack (born 26 December 1970) is a stage and screen actress from New Zealand.
INC claims (4):
  [g24a_fever_225236] Danielle Cormack is an actress.
  [g24a_fever_225237] Danielle Cormack is from New Zealand.
  [g24a_fever_225252] Danielle Cormack is a stage and screen actress.
  [g24a_fever_225254] Danielle Cormack was born on December 26, 1970.
DEC claims (1):
  [g24a_fever_225239] Danielle Cormack was born in May.

## sha=5db112a93e source=fever n_inc=2 n_dec=1
EVIDENCE: It is an Eastern Hindi language that has been subject to considerable influence by Awadhi, Bhojpuri, Magahi and other Bihari languages.
INC claims (2):
  [g24a_fever_217381] Fiji Hindi has been subject to considerable influence.
  [g24a_fever_217390] Fiji Hindi has been subject to impact by Magahi and other Bihari languages.
DEC claims (1):
  [g24a_fever_217379] Fiji Hindi has been isolated from influence by Magahi and other Bihari languages.

## sha=e83435f8a3 source=fever n_inc=4 n_dec=2
EVIDENCE: Frusciante has an active solo career, having released eleven solo albums and five EPs; his recordings include elements ranging from experimental rock and ambient music to new wave and electronica.
INC claims (4):
  [g24a_fever_26792] John Frusciante worked with electronica in his music.
  [g24a_fever_66539] John Frusciante released eleven solo albums.
  [g24a_fever_66540] John Frusciante was incapable of releasing eleven solo albums.
  [g24a_fever_92851] John Frusciante incorporated experimental rock into his music.
DEC claims (2):
  [g24a_fever_110538] John Frusciante released twelve solo albums.
  [g24a_fever_26793] John Frusciante was incapable of working with electronica in his music.

## sha=65f1f45c93 source=fever n_inc=1 n_dec=2
EVIDENCE: TakePart is the digital division of Participant Media, a motion picture studio that focuses on issues of social justice. Participant Media is an American film production company founded in 2004 by Jeffrey Skoll, dedicated to entertainment that inspires and compels social change.
INC claims (1):
  [g24a_fever_64622] TakePart is a division of an American film production company.
DEC claims (2):
  [g24a_fever_153440] TakePart is the digital division of a university.
  [g24a_fever_59626] TakePart is the digital division of a Turkish film production company.

## sha=374057e887 source=fever n_inc=6 n_dec=2
EVIDENCE: Forceps (plural forceps or forcipes) are a handheld, hinged instrument used for grasping and holding objects.
INC claims (6):
  [g24a_fever_181976] Forceps are used for grasping objects.
  [g24a_fever_181978] Forceps are a hinged instrument.
  [g24a_fever_181980] Forceps are used for grasping and holding objects.
  [g24a_fever_181982] Forceps are a tool.
  [g24a_fever_181983] Forceps are used for grasping.
  [g24a_fever_181994] Forceps are an instrument that are handheld.
DEC claims (2):
  [g24a_fever_181986] Forceps are a wheeled instrument.
  [g24a_fever_181992] Forceps are an instrument that is unable to be handheld.

## sha=1e0b5cb1ed source=fever n_inc=3 n_dec=3
EVIDENCE: The series stars James Roday as Shawn Spencer, a young crime consultant for the Santa Barbara Police Department whose "heightened observational skills" and impressive detective instincts allow him to convince people that he solves cases with psychic abilities.
INC claims (3):
  [g24a_fever_148947] Psych has a protagonist.
  [g24a_fever_55706] Psych's protagonist is Shawn Spencer.
  [g24a_fever_55707] Psych's main character is Shawn Spencer.
DEC claims (3):
  [g24a_fever_112326] Psych's protagonist is Olivia Dunham.
  [g24a_fever_138593] Psych's protagonist is not Shawn Spencer.
  [g24a_fever_87691] Psych takes place in Massachusetts.

## sha=0371d7058c source=fever n_inc=5 n_dec=5
EVIDENCE: Samwell Tarly, called Sam, is a fictional character in the A Song of Ice and Fire series of fantasy novels by American author George R. R. Martin, and its television adaptation Game of Thrones.
INC claims (5):
  [g24a_fever_206712] Samwell Tarly appears in novels by George R. R. Martin.
  [g24a_fever_206716] Samwell Tarly appears in the A Song of Ice and Fire series.
  [g24a_fever_206718] Samwell Tarly appears in novels.
  [g24a_fever_206722] Samwell Tarly appears in the series of A Song of Ice and Fire.
  [g24a_fever_206728] Samwell Tarly is a character.
DEC claims (5):
  [g24a_fever_206715] Samwell Tarly makes zero appearances in Game of Thrones.
  [g24a_fever_206717] Samwell Tarly appears only outside of the A Song of Ice and Fire series.
  [g24a_fever_206723] Samwell Tarly appears in novels only by J. R. R. Tolkien.
  [g24a_fever_206730] Samwell Tarly appears in The Lord of the Rings series.
  [g24a_fever_206737] Samwell Tarly is a nonfictional character.

