# btf3_large_replication_v1 — realized YES review chunk YES-129–YES-192

> Display chunk of the immutable queue (`btf3_large_replication_v1_yes_queue.json`). Review strictly top-to-bottom; stop only when this bucket reaches 128 ACCEPTs overall. Do not skip ahead, reorder, or prefer better-looking questions. A REJECT/UNSURE permanently consumes its queue slot and is never resampled, re-reviewed, or hand-repaired.

All four gates must hold to ACCEPT. On REJECT or UNSURE write exactly one line of reason.

### YES-129. `044eca74-078c-5b13-97a8-643d48941987`

- Present date: `2026-05-14 04:08:09.291057`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the U.S. Supreme Court rule in favor of Okello Chatrie (petitioner) in Chatrie v. United States by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the Supreme Court of the United States issues an opinion in Chatrie v. United States (No. 25-112) that **reverses or vacates** the judgment of the U.S. Court of Appeals for the 4th Circuit, in whole or in part. This constitutes "ruling in favor" of the petitioner, Okello Chatrie.

This question resolves **No** if the Supreme Court **affirms** the 4th Circuit's judgment.

If the Court **dismisses the writ of certiorari as improvidently granted (DIG)**, this question resolves **No**.

If no opinion is issued by **July 1, 2026, 11:59 PM Eastern Time**, this question resolves **No**.

**Resolution source:** The official Supreme Court slip opinions page at https://www.supremecourt.gov/opinions/slipopinion/25. The opinion's syllabus and disposition will determine resolution.

**Pre-cutoff background**

Chatrie v. United States (No. 25-112) concerns the constitutionality of a "geofence warrant"—a type of warrant that directs a technology company (in this case, Google) to identify all devices located within a defined geographic area during a specified time window (see https://en.wikipedia.org/wiki/Geo-fence_warrant). Law enforcement used such a warrant to obtain location data that helped identify and convict Okello Chatrie for a 2019 bank robbery in Virginia.

The federal district court denied Chatrie's motion to suppress the evidence, finding that while the geofence warrant lacked probable cause and particularity, the officers relied on it in "good faith." A divided panel of the U.S. Court of Appeals for the 4th Circuit affirmed, holding that the government had not conducted a "search" under the Fourth Amendment because Chatrie lacked a reasonable expectation of privacy in location data he voluntarily allowed Google to collect [Justices appear mixed on whether geofence warrant violated the ...](https://www.scotusblog.com/2026/04/justices-appear-mixed-on-whether-geofence-warrant-violated-the-fourth-amendment-/).

The Supreme Court granted certiorari on January 16, 2026. Oral arguments were held on April 27, 2026 [Justices appear mixed on whether geofence warrant violated the ...](https://www.scotusblog.com/2026/04/justices-appear-mixed-on-whether-geofence-warrant-violated-the-fourth-amendment-/). As of May 13, 2026, no opinion has been issued; one is expected before the end of the October 2025 term (typically late June 2026).

During oral arguments, the justices appeared divided [Justices appear mixed on whether geofence warrant violated the ...](https://www.scotusblog.com/2026/04/justices-appear-mixed-on-whether-geofence-warrant-violated-the-fourth-amendment-/):
- Justices Sotomayor and Gorsuch expressed concern about government overreach and warrantless access to digital location data.
- Chief Justice Roberts and Justices Alito and Barrett were skeptical of privacy expectations for data voluntarily shared with Google.
- Justice Alito suggested the case could be resolved on "good faith" grounds, potentially avoiding the broader Fourth Amendment question.

This division makes the outcome genuinely uncertain. The Court could rule broadly on the Fourth Amendment question, rule narrowly on good-faith grounds, or produce a fractured opinion.

**Exact later resolution packet**

The question resolves YES.

Key findings:
- The U.S. Supreme Court issued its opinion in Chatrie v. United States (No. 25-112) on June 29, 2026, which is before the resolution deadline of July 1, 2026, 11:59 PM ET. The official slip opinion is at https://www.supremecourt.gov/opinions/25pdf/25-112_0am4.pdf and is listed on the official slip opinions page https://www.supremecourt.gov/opinions/slipopinion/25 [27432f].
- The disposition was that the judgment of the U.S. Court of Appeals for the 4th Circuit was VACATED and the case REMANDED. This is confirmed by the official slip opinion page, which states the Court held that "Police officers conducted a Fourth Amendment search when they acquired Okello Chatrie's location data from Google because an individual has a reasonable expectation of privacy in his cell-phone location information" — contrary to the 4th Circuit's holding that no search had occurred [27432f].
- SCOTUSblog's case page independently confirms: "Vacated and remanded, 6-3, in an opinion by Elena Kagan on Jun 29, 2026" and "Judgment VACATED and case REMANDED. Kagan, J., delivered the opinion of the Court." (https://www.scotusblog.com/cases/chatrie-v-united-states/).

Per the resolution criteria: "This question resolves Yes if the Supreme Court ... issues an opinion ... that reverses or vacates the judgment of the U.S. Court of Appeals for the 4th Circuit, in whole or in part." The Court vacated the 4th Circuit's judgment, so this constitutes "ruling in favor" of petitioner Okello Chatrie.

The disposition was NOT an affirmance, and NOT a dismissal of the writ as improvidently granted (DIG), so neither of the NO conditions applies. The opinion was issued before the July 1, 2026 deadline, so the timing-based NO condition also does not apply.

Therefore the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-130. `9e807f3f-c7c7-515d-895a-a18fbb170141`

- Present date: `2026-05-16 17:43:49.456916`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will a constitutional challenge to the Combatting Antisemitism, Hate and Extremism Act 2026 be filed in an Australian court between May 12, 2026 and July 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after May 12, 2026 (00:00 AEST) and no later than July 1, 2026 (23:59 AEST), a formal constitutional challenge to the Combatting Antisemitism, Hate and Extremism Act 2026 (Act No. 48 of 2026), or any provision thereof, is filed in an Australian court.

**Definition of "constitutional challenge":** A legal proceeding in which a party files an originating application, writ of summons, statement of claim, or notice of a constitutional matter (under Section 78B of the Judiciary Act 1903) that explicitly challenges the validity of the Act or any of its provisions on constitutional grounds — for example, arguing it infringes the implied freedom of political communication under the Australian Constitution.

**Definition of "Australian court":** The High Court of Australia, any Federal Court (including the Federal Court of Australia and the Federal Circuit and Family Court of Australia), or any Supreme Court of an Australian State or Territory.

**Resolution source:** The question will be resolved by checking:
1. The High Court of Australia case search portal (https://www.hcourt.gov.au/cases/cases-search) and the Federal Court of Australia case search (https://www.fedcourt.gov.au/); or
2. Credible reporting from major Australian news organisations including ABC News Australia (https://www.abc.net.au/news), SBS News (https://www.sbs.com.au/news), The Guardian Australia (https://www.theguardian.com/australia-news), The Australian, or The Sydney Morning Herald confirming that such a filing has occurred.

If no such filing is confirmed by these sources by July 1, 2026 (23:59 AEST), the question resolves NO.

**Pre-cutoff background**

The Combatting Antisemitism, Hate and Extremism (Criminal and Migration Laws) Bill 2026 passed both Houses of the Australian Parliament on January 20, 2026, and received Royal Assent as Act No. 48 of 2026 [Combatting Antisemitism, Hate and Extremism (Criminal and ...](https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/Bills_Search_Results/Result?bId=r7422). The Act amends the Criminal Code Act 1995, the Crimes Act 1914, and other legislation to introduce new offences and penalties related to hate speech, radicalisation, and hate-motivated conduct.

The legislation has faced significant criticism on free speech grounds. Constitutional law expert Anne Twomey raised concerns during a NSW parliamentary inquiry about the "proliferation" of such laws and their potential to infringe on the implied freedom of political communication [Hate laws put free speech at risk, constitutional expert tells inquiry](https://www.abc.net.au/news/2026-02-19/concerns-laws-targeting-antisemitism-risk-free-speech/106363916). Reuters reported that Twomey said the proposed law could be challenged in the High Court. Separately, at the state level, pro-Palestinian protesters in Queensland have pledged to mount a constitutional challenge against Queensland's hate speech laws after arrests were made for using banned phrases [Protesters prepare legal challenge over 'absurd and stupid' anti-hate ...](https://www.sbs.com.au/news/article/constitutional-fight-looms-over-banned-protest-chants/mqifcopda). An NSW Court of Appeal has already struck down 'social cohesion' protest laws as unconstitutional.

As of May 13, 2026, no formal constitutional challenge to the federal Act has been reported in Australian courts [Hate laws put free speech at risk, constitutional expert tells inquiry](https://www.abc.net.au/news/2026-02-19/concerns-laws-targeting-antisemitism-risk-free-speech/106363916). However, the combination of active parallel litigation against state-level hate speech laws, stated intentions by civil liberties groups, and expert opinions suggesting challenges have "a reasonable chance of success" makes a filing plausible but uncertain within the timeframe.

**Exact later resolution packet**

The question resolves YES.

The Act in question exists: the Combatting Antisemitism, Hate and Extremism (Criminal and Migration Laws) Act 2026 (Cth), which passed both Houses on January 20, 2026 (Parliament of Australia record) [Combatting Antisemitism, Hate and Extremism (Criminal and ...](https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/Bills_Search_Results/Result?bId=r7422).

A formal constitutional challenge to this federal Act was filed within the resolution window (May 12, 2026 00:00 AEST – July 1, 2026 23:59 AEST). Specifically:

1) The High Court of Australia single-justice judgment White Australia Party Inc v The Commonwealth [2026] HCASJ 15 records that the plaintiffs (White Australia Party Inc & Anor) lodged an "application for a constitutional or other writ" (together with an interlocutory application) on May 15, 2026, with the principal relief sought being a declaration that the provisions of the Combatting Antisemitism, Hate and Extremism (Criminal and Migration Laws) Act 2026 are invalid. The constitutional grounds pleaded include: (i) unlawful proscription of a political party contrary to Australian Communist Party v The Commonwealth; (ii) impairment of the implied freedom of political communication; and (iii) vesting of punitive power in the Executive contrary to the Ch III separation of powers [White Australia Party Inc v The Commonwealth of Australia (2026 ...](https://en.wikisource.org/wiki/White_Australia_Party_Inc_v_The_Commonwealth_of_Australia_(2026_HCASJ_15)).

2) The Guardian Australia (a prescribed resolution source) reported on May 18, 2026 that the National Socialist Network / White Australia Party filed the constitutional challenge in the High Court on Friday, May 15, 2026, via solicitor Matthew Hopkins on behalf of Thomas Sewell, arguing the legislation "burdens the freedom of governmental and political communication" and unlawfully confers punitive power without judicial review [Neo-Nazi group challenges hate ban by arguing law 'operates as a ...](https://www.theguardian.com/law/2026/may/18/neo-nazi-group-national-socialist-network-white-australia-challenges-hate-ban-ntwnfb).

3) The Guardian Australia further confirmed on June 4, 2026 that "White Australia is also challenging the broader constitutionality of anti-hate speech laws passed after the Bondi Beach mass shooting," with a two-day constitutional hearing listed for September 2026, and that Chief Justice Gageler dismissed the group's injunction bid on June 4 while the constitutional challenge continued [Neo-Nazi group White Australia loses bid for temporary immunity ...](https://www.theguardian.com/australia-news/2026/jun/04/neo-nazi-group-white-australia-loses-injunction-attempt-against-hate-group-designation-ntwnfb).

4) The Queensland Council for Civil Liberties blog independently states the party's constitutional challenge was filed on May 15, 2026 [White Australia Party loses injunction bid against Commonwealth ...](https://qccl.org.au/newsblog/4agrb6nf1ji1hw0oqnhgr31yclsa9p).

Checklist verification:
- Filing date May 15, 2026 falls within May 12 – July 1, 2026 (AEST). ✓
- The target is the federal Act No. 48 of 2026 (Combatting Antisemitism, Hate and Extremism (Criminal and Migration Laws) Act 2026 (Cth)), not a state law. ✓
- Filed in an "Australian court" — the High Court of Australia (case M50-2026). ✓
- Constitutes a "constitutional challenge" — an originating application/application for a constitutional writ seeking a declaration of invalidity on constitutional grounds (implied freedom of political communication; separation of powers). ✓
- Evidence drawn from prescribed sources: the High Court judgment (HCASJ 15) and The Guardian Australia. ✓

Key URLs:
- High Court judgment text: https://en.wikisource.org/wiki/White_Australia_Party_Inc_v_The_Commonwealth_of_Australia_(2026_HCASJ_15) and https://www.hcourt.gov.au/sites/default/files/eresources/2026-05-22/HCA/White%20Australia%20Party%20Inc.%20v%20The%20Commonwealth%20%28M50-2026%29%20HCASJ%2015.pdf
- Guardian (May 18, 2026): https://www.theguardian.com/law/2026/may/18/neo-nazi-group-national-socialist-network-white-australia-challenges-hate-ban-ntwnfb
- Guardian (June 4, 2026): https://www.theguardian.com/australia-news/2026/jun/04/neo-nazi-group-white-australia-loses-injunction-attempt-against-hate-group-designation-ntwnfb
- QCCL: https://qccl.org.au/newsblog/4agrb6nf1ji1hw0oqnhgr31yclsa9p
- APH bill record: https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/Bills_Search_Results/Result?bId=r7422

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-131. `741b4bed-7502-5cd2-9cbe-949fbc70f857`

- Present date: `2026-05-07 22:07:47.186771`
- Source cutoff boundary: `2026-05-08` (encodes end of UTC day `2026-05-07`)
- Expected resolution: `2026-05-21 00:00:00`

**Question**

Will Matthew Wale be elected as the next Prime Minister of Solomon Islands following the May 2026 no-confidence vote?

**Resolution criteria**

This question resolves **Yes** if Matthew Wale is formally elected or appointed as [Prime Minister](https://en.wikipedia.org/wiki/Prime_Minister_of_the_Solomon_Islands) of the Solomon Islands and sworn in by the Governor-General on or after May 7, 2026 (00:00 UTC+11, Solomon Islands Time), as the immediate successor to Jeremiah Manele following the May 7, 2026 no-confidence vote.

This question resolves **No** if:
- Any other individual is elected and sworn in as Prime Minister following the no-confidence vote; or
- No new Prime Minister has been sworn in by August 1, 2026 (23:59 UTC+11).

Resolution will be determined by official announcements from the [Solomon Islands Government](https://solomons.gov.sb/) or credible reporting from named news organizations including [ABC News Australia](https://www.abc.net.au/news/), [Radio New Zealand (RNZ)](https://www.rnz.co.nz/), [Reuters](https://www.reuters.com/), or [Associated Press](https://apnews.com/).

**Pre-cutoff background**

On May 7, 2026, Solomon Islands Prime Minister Jeremiah Manele was ousted via a motion of no confidence, losing 22-26 in a parliamentary vote [Solomon Islands to get new leader after Jeremiah Manele voted out ...](https://www.abc.net.au/news/2026-05-07/solomon-islands-new-prime-minister-jeremiah-manele-voted-out/106651634). The no-confidence motion was tabled by a coalition led by Frederick Kologeto of the People's First Party. The 26-member winning coalition must now elect a new Prime Minister, with a vote expected in the week of May 11, 2026 [Solomon Islands to get new leader after Jeremiah Manele voted out ...](https://www.abc.net.au/news/2026-05-07/solomon-islands-new-prime-minister-jeremiah-manele-voted-out/106651634).

Two leading candidates have emerged for the premiership:
- **Matthew Wale**, the long-term Leader of the Opposition, who was instrumental in the legal challenges that forced the no-confidence vote [Court orders Solomon Islands PM Manele to face no-confidence ...](https://www.rnz.co.nz/news/pacific/592361/court-orders-solomon-islands-pm-manele-to-face-no-confidence-vote-within-three-days).
- **Peter Shanel Agovaka**, a former Foreign Minister who abandoned Manele's government in March 2026 to join the opposition. The Lowy Institute identified Agovaka as the "most likely PM candidate from the opposition" [Solomon Islands on the edge, again | Lowy Institute](https://www.lowyinstitute.org/the-interpreter/solomon-islands-edge-again).

The opposition coalition comprises approximately 26-28 MPs (out of 50 total parliamentary seats), drawn from six political parties [Solomon Islands on the edge, again | Lowy Institute](https://www.lowyinstitute.org/the-interpreter/solomon-islands-edge-again) [Court orders Solomon Islands PM Manele to face no-confidence ...](https://www.rnz.co.nz/news/pacific/592361/court-orders-solomon-islands-pm-manele-to-face-no-confidence-vote-within-three-days). Solomon Islands coalition politics are notoriously fluid; historically, the leader of a no-confidence motion does not always become PM, as coalition negotiations can produce compromise candidates. The process for electing a new [Prime Minister](https://en.wikipedia.org/wiki/Prime_Minister_of_the_Solomon_Islands) involves a vote among all Members of Parliament, as prescribed by the [Constitution of Solomon Islands](https://www.constituteproject.org/constitution/Solomon_Islands_1978).

**Exact later resolution packet**

The antecedent occurred, so the question should not be annulled: ABC News Australia reported on May 7, 2026 that Jeremiah Manele “has been voted out of office after a no-confidence motion,” with 26 MPs in the 50-seat parliament siding against him, and that no new leader had yet been identified at that time (URL: https://www.abc.net.au/news/2026-05-07/solomon-islands-new-prime-minister-jeremiah-manele-voted-out/106651634) [Solomon Islands to get new leader after Jeremiah Manele voted out ...](https://www.abc.net.au/news/2026-05-07/solomon-islands-new-prime-minister-jeremiah-manele-voted-out/106651634). The consequent also occurred: RNZ reported that Matthew Cooper Wale was elected Solomon Islands prime minister by secret ballot in Honiara on Friday, May 15, 2026, defeating Peter Shanel Agovaka 26 votes to 22 (URL: https://www.rnz.co.nz/news/pacific/595330/matthew-wale-longtime-opposition-leader-is-new-solomon-islands-prime-minister) [Matthew Wale, longtime opposition leader, is new Solomon Islands ...](https://www.rnz.co.nz/news/pacific/595330/matthew-wale-longtime-opposition-leader-is-new-solomon-islands-prime-minister). RNZ then reported that Wale was sworn in as the new Prime Minister by Governor-General Sir David Tiva Kapu at Government House immediately after his parliamentary election on Friday, May 15, 2026 (URL: https://www.rnz.co.nz/news/pacific/595515/prime-minister-matthew-wale-appoints-cabinet-to-lead-the-solomon-islands) [Prime Minister Matthew Wale appoints Cabinet to lead the Solomon ...](https://www.rnz.co.nz/news/pacific/595515/prime-minister-matthew-wale-appoints-cabinet-to-lead-the-solomon-islands). This swearing-in date is after May 7, 2026 and before the August 1, 2026 deadline [Prime Minister Matthew Wale appoints Cabinet to lead the Solomon ...](https://www.rnz.co.nz/news/pacific/595515/prime-minister-matthew-wale-appoints-cabinet-to-lead-the-solomon-islands). The evidence also rules out the specified NO trigger: ABC stated no replacement had yet been identified immediately after Manele’s ouster, RNZ identified Wale—not Agovaka or anyone else—as the candidate elected in the subsequent prime-ministerial vote, and RNZ stated Wale was sworn in immediately after that election [Solomon Islands to get new leader after Jeremiah Manele voted out ...](https://www.abc.net.au/news/2026-05-07/solomon-islands-new-prime-minister-jeremiah-manele-voted-out/106651634) [Matthew Wale, longtime opposition leader, is new Solomon Islands ...](https://www.rnz.co.nz/news/pacific/595330/matthew-wale-longtime-opposition-leader-is-new-solomon-islands-prime-minister) [Prime Minister Matthew Wale appoints Cabinet to lead the Solomon ...](https://www.rnz.co.nz/news/pacific/595515/prime-minister-matthew-wale-appoints-cabinet-to-lead-the-solomon-islands). Therefore Matthew Wale was the immediate sworn-in successor to Jeremiah Manele following the May 7, 2026 no-confidence vote, so the resolution is YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-132. `7279494c-a775-5a57-a5f2-ac22252fb286`

- Present date: `2026-05-14 00:35:12.390932`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-16T00:00:00`

**Question**

Will the Bank of Japan raise its short-term policy interest rate at the June 15–16, 2026 Monetary Policy Meeting?

**Resolution criteria**

This question resolves as **Yes** if the Bank of Japan, in its official "Statement on Monetary Policy" published following the conclusion of the Monetary Policy Meeting on June 15–16, 2026 (JST), announces a guideline for the uncollateralized overnight call rate that is higher than 0.75% (i.e., an increase of at least 1 basis point above the current ~0.75% target). The "Short-Term Policy Interest Rate" refers to the BOJ's guideline for the uncollateralized overnight call rate, as described on the BOJ's monetary policy page (https://www.boj.or.jp/en/mopo/outline/index.htm).

This question resolves as **No** if the BOJ decides to maintain the uncollateralized overnight call rate at approximately 0.75% or lower, or if the June 15–16, 2026 meeting does not take place.

The resolution source is the official "Statement on Monetary Policy" published on the Bank of Japan's Monetary Policy Releases page: https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/index.htm

**Pre-cutoff background**

As of May 13, 2026, the Bank of Japan (BOJ) maintains its short-term policy interest rate — the uncollateralized overnight call rate — at approximately 0.75% [[PDF] April 28, 2026 Bank of Japan Statement on Monetary Policy](https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/k260428a.pdf). This was confirmed at the most recent Monetary Policy Meeting on April 27–28, 2026, where the Policy Board voted 6–3 to keep the rate unchanged [[PDF] April 28, 2026 Bank of Japan Statement on Monetary Policy](https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/k260428a.pdf). Three dissenting members — Nakagawa Junko, Takata Hajime, and Tamura Naoki — proposed raising the rate to 1.0%, but their proposals were defeated [[PDF] April 28, 2026 Bank of Japan Statement on Monetary Policy](https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/k260428a.pdf). This 6–3 split represents the widest division under Governor Ueda's tenure.

Market expectations for a June hike are elevated but uncertain. Reuters reported the BOJ has "locked in" signals for a June rate hike, while nearly two-thirds of Reuters-polled economists expect the rate to reach 1.0% by end-June. However, some economists, such as Oxford Economics' Shigeto Nagai, argue the BOJ will not have sufficient data by June to justify a hike. Polymarket implied probability for a 25 basis point hike stands at approximately 63%.

The next scheduled Monetary Policy Meeting is June 15–16, 2026 (JST). The BOJ publishes its policy decision via the "Statement on Monetary Policy" on the final day of the meeting.

**Exact later resolution packet**

The question resolves YES (1).

The June 15–16, 2026 Bank of Japan Monetary Policy Meeting DID take place, and the BOJ raised its short-term policy interest rate above 0.75%.

Key evidence:
- The official BOJ policy release published June 16, 2026 (titled "Change in the Guideline for Money Market Operations," the document that serves as the Statement on Monetary Policy for meetings involving a rate change), URL: https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/k260616a.pdf , states: "The Bank will encourage the uncollateralized overnight call rate to remain at around 1.0 percent," decided by a 7-1 majority vote [75e563]. This raises the guideline from the prior ~0.75% level to ~1.0%.
- The BOJ "Statements on Monetary Policy 2026" index page (https://www.boj.or.jp/en/mopo/mpmdeci/state_2026/index.htm) and the "Monetary Policy Releases 2026" page (https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/index.htm) confirm the June 16, 2026 release announcing the change to ~1.0% [a36321].
- Corroborating high-quality news sources: CNBC ("Bank of Japan hikes rates to 1%, highest since 1995"), Nikkei ("The Bank of Japan decided on Tuesday to raise its benchmark interest rate to 1%"), and Trading Economics ("The Bank of Japan lifted its key short-term rate by 25bps to 1.0% in a 7-1 vote at its June meeting").

Since the announced guideline for the uncollateralized overnight call rate (~1.0%) is strictly higher than 0.75% (an increase of 25 basis points, well above the 1 bp threshold), the YES condition in the resolution criteria is met.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-133. `72178d56-46a3-5048-a419-1a9d38fdba05`

- Present date: `2026-05-02 21:04:40.753974`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Adrian Newey hold the title of Team Principal at Aston Martin Aramco F1 Team on June 1, 2026?

**Resolution criteria**

This question resolves YES if, at 23:59 UTC on June 1, 2026, Adrian Newey is officially listed as "Team Principal" of the Aston Martin Aramco Formula One Team.

The primary resolution source is the Aston Martin Aramco F1 Team's official website management/about page (https://www.astonmartinf1.com). If this page is unavailable or ambiguous, the FIA's official 2026 Entry List (published at https://www.fia.com/documents) may be used as an alternative authoritative source.

For the purposes of this question, "Team Principal" is defined as the individual officially designated as Team Principal per the FIA Formula One Sporting Regulations (the person who represents the team in official FIA communications and is listed as such on the FIA Entry List or the team's official website).

The question resolves NO if:
- Newey has been officially replaced as Team Principal by another individual, OR
- Newey has officially stepped down or resigned from the Team Principal role, OR
- The team has announced that another person holds the Team Principal title (whether permanent, interim, or acting).

Note: An "Interim" or "Acting" Team Principal appointment for someone other than Newey satisfies the NO resolution. Conversely, if Newey himself is listed as "Interim" or "Acting" Team Principal, the question resolves YES — what matters is whether Newey holds the Team Principal title in any capacity.

If credible sources (e.g., BBC Sport, Reuters, Associated Press, Formula1.com) report a confirmed change but the official website has not yet been updated, credible reporting may be used to resolve the question.

**Pre-cutoff background**

On November 26, 2025, Aston Martin Aramco Formula One Team officially announced that Adrian Newey would take on the role of Team Principal from the 2026 season, replacing Andy Cowell, who moved to become Chief Strategy Officer [Aston Martin Aramco announces changes to leadership structure ...](https://www.astonmartinf1.com/en-GB/news/announcement/aston-martin-aramco-announces-changes-to-leadership-structure). Newey had previously served as the team's Managing Technical Partner.

However, following a difficult start to the 2026 season, multiple credible outlets (Autosport, Motorsport.com, ESPN, The Race) reported in mid-March 2026 that Newey was set to step down as Team Principal to focus exclusively on technical matters, with Audi's Jonathan Wheatley reportedly targeted as his replacement. On March 19-20, 2026, Aston Martin officially denied these reports, with a team spokesperson stating that Newey "continues to lead the team as team principal and managing technical partner" [What we know about another Aston Martin F1 team principal move](https://www.the-race.com/formula-1/aston-martin-team-principal-search-f1-2026-adrian-newey-jonathan-wheatley-audi/). The team said it would not engage with media speculation.

As of May 1, 2026, the situation remains fluid. Newey reportedly took the Team Principal role to "fill a gap" rather than as a long-term commitment, and the team's poor early-season performance has intensified pressure for a leadership change. The question of whether a formal transition will occur by June 1 is genuinely uncertain.

**Exact later resolution packet**

RESOLUTION: YES (1) — Adrian Newey held the title of Team Principal at Aston Martin Aramco F1 Team as of 23:59 UTC on June 1, 2026.

PRIMARY SOURCE CHECK: The specified primary resolution source (https://www.astonmartinf1.com management/about page) could not be loaded/scraped during research (the team pages https://www.astonmartinf1.com/en-GB/the-team and /the-management returned no content). Per the resolution criteria, when the official website is unavailable/ambiguous, other authoritative and credible sources may be used.

KEY EVIDENCE AND TIMELINE:
- Nov 26, 2025: Aston Martin officially announced Newey would become Team Principal from 2026, replacing Andy Cowell (who became Chief Strategy Officer).
- Mid-March 2026: Multiple outlets (Autosport, Motorsport Italia, ESPN, SI.com) reported Newey was "set to step back/step down" to focus on technical matters, with Audi's Jonathan Wheatley as the likely replacement [6865d9, edaa95]. Wheatley left Audi on/around March 20, 2026 "due to personal reasons."
- CRUCIALLY, these were reports of an INTENDED/EXPECTED future move, not a completed one. Aston Martin officially DENIED them: an Aston Martin spokesperson said "Adrian Newey continues to lead the team as Team Principal and Managing Technical Partner" and that the team would not engage in media speculation [edaa95]. Lawrence Stroll reaffirmed Newey's role on ~March 20, 2026 [9f7dca].
- ~March 27, 2026: Aston Martin (via Pedro de la Rosa) stated Wheatley "isn't joining for the time being" and Newey's role "will remain unchanged" [f9e14a].
- Late May 2026: The "Aston Martin change tack" reporting noted de la Rosa "did not dismiss the possibility" of Wheatley joining eventually, but NO official appointment of Wheatley (or any other interim/acting Team Principal) was ever confirmed.
- The English Wikipedia "Aston Martin in Formula One" article, last edited May 25, 2026 (the datapoint closest to the June 1 resolution date), still lists Adrian Newey as "Team Principal and Managing Technical Partner" [e762f2]. The Adrian Newey Wikipedia article similarly listed him as Team Principal [b88ee6].

NO-RESOLUTION TRIGGERS CHECKED: I specifically verified whether any individual other than Newey was appointed Interim/Acting/permanent Team Principal (which would trigger NO). No such official appointment occurred before June 1, 2026. Wheatley was never officially confirmed/announced as Team Principal — reports through late May 2026 consistently described it as an expected-but-not-yet-finalized move, and the team explicitly said he was "not joining for the time being" [f9e14a]. No credible source from the allowed list (BBC Sport, Reuters, AP, Formula1.com) confirmed an actual change of Team Principal.

CONCLUSION: Newey was neither officially replaced nor officially stepped down as of June 1, 2026; he remained the designated Team Principal. The question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-134. `e5104a3c-9010-506f-8e58-83e40c658ed9`

- Present date: `2026-05-29 05:17:10.678707`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the STF First Panel deliver a verdict in the Eduardo Bolsonaro coercion case (Inquérito 4.995) before July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the STF First Panel delivers a verdict—defined as the conclusion of the voting session (sessão de julgamento) on the merits of the case, resulting in either a conviction or acquittal of Eduardo Bolsonaro in Inquérito 4.995—on or after May 12, 2026, and before July 1, 2026, 23:59 Brasília Time (UTC-3).

This question resolves **No** if no such verdict is delivered by that deadline.

A "verdict" means the First Panel has completed voting on the merits (i.e., all ministers have cast their votes and the result has been proclaimed by the presiding justice). Procedural decisions (such as scheduling, requests for vista, or preliminary motions) do not count. If the judgment session begins but is suspended (e.g., due to a pedido de vista) before a final result is proclaimed, the question resolves **No** unless voting is completed before the deadline.

**Resolution source:** The official STF case tracking portal at [https://portal.stf.jus.br/](https://portal.stf.jus.br/) (search for Inquérito 4.995) or the Diário da Justiça Eletrônico (DJE) at [https://dje.stf.jus.br/](https://dje.stf.jus.br/). Credible Brazilian media reporting (e.g., Agência Brasil, G1, Folha de S.Paulo) may also be used to confirm the outcome.

**Pre-cutoff background**

Eduardo Bolsonaro, a former federal deputy and son of ex-President Jair Bolsonaro, is a defendant (réu) before the First Panel (Primeira Turma) of Brazil's Supreme Federal Court (STF) in a case registered as Inquérito 4.995 [STF aceita denúncia do MPF por coação em processo judicial](https://www.mpf.mp.br/o-mpf/unidades/procuradoria-geral-da-republica-pgr/noticias/stf-aceita-denuncia-do-mpf-por-coacao-em-processo-judicial). He is charged with coercion in the course of a judicial proceeding (coação no curso do processo, Article 344 of the Brazilian Penal Code), for allegedly lobbying United States officials to impose sanctions on STF justices in order to obstruct the criminal proceedings against his father [STF aceita denúncia do MPF por coação em processo judicial](https://www.mpf.mp.br/o-mpf/unidades/procuradoria-geral-da-republica-pgr/noticias/stf-aceita-denuncia-do-mpf-por-coacao-em-processo-judicial).

On November 15, 2025, the First Panel unanimously accepted the criminal charges (denúncia) filed by the Federal Prosecution Service (MPF/PGR), formally making Eduardo Bolsonaro a defendant [STF aceita denúncia do MPF por coação em processo judicial](https://www.mpf.mp.br/o-mpf/unidades/procuradoria-geral-da-republica-pgr/noticias/stf-aceita-denuncia-do-mpf-por-coacao-em-processo-judicial). The Ação Penal was formalized on February 19, 2026, entering the instruction phase [STF formaliza ação que tornou Eduardo Bolsonaro réu na Corte](https://agenciabrasil.ebc.com.br/justica/noticia/2026-02/stf-formaliza-acao-que-tornou-eduardo-bolsonaro-reu-na-corte). Eduardo Bolsonaro is currently residing in the United States and is being represented by the Public Defender's Office (DPU) after failing to appoint private counsel [PGR pede condenação de Eduardo Bolsonaro por coação | VEJA](https://veja.abril.com.br/politica/pgr-pede-condenacao-de-eduardo-bolsonaro-por-coacao/).

As of May 2026, the instruction phase has concluded: witnesses were heard, the PGR submitted its request for conviction (on May 11, 2026), and Justice Alexandre de Moraes (the case rapporteur) opened a 15-day window for the defense to submit final arguments (alegações finais) [PGR pede condenação de Eduardo Bolsonaro por coação | VEJA](https://veja.abril.com.br/politica/pgr-pede-condenacao-de-eduardo-bolsonaro-por-coacao/). Once final arguments are submitted (or the deadline lapses), the case can be scheduled for judgment by the First Panel.

The STF has publicly indicated its intention to conclude the trial in the first half of 2026. However, Brazilian court timelines can slip due to procedural delays, requests for additional review (pedido de vista), or scheduling conflicts.

**Exact later resolution packet**

The question resolves YES.

The resolution criteria require that the STF First Panel (Primeira Turma) deliver a verdict on the merits — a conviction or acquittal — in Inquérito 4.995 against Eduardo Bolsonaro, with all ministers having voted and the result proclaimed, on or after May 12, 2026 and before July 1, 2026 23:59 Brasília Time.

Evidence, from the official STF news portal (the specified resolution source), confirms every element:
- On June 16, 2026, the First Panel (Primeira Turma) of the STF unanimously CONVICTED Eduardo Bolsonaro of "coação no curso do processo" (coercion in the course of a judicial proceeding, Art. 344), the exact charge in this case [STF condena Eduardo Bolsonaro por coação no curso do processo ...](https://noticias.stf.jus.br/postsnoticias/stf-condena-eduardo-bolsonaro-por-coacao-no-curso-do-processo-sobre-tentativa-de-golpe/).
- All four ministers of the panel (rapporteur Alexandre de Moraes, Cristiano Zanin, Cármen Lúcia, and Flávio Dino) cast their votes, and the result was proclaimed during the session, with a sentence of 4 years and 2 months in a semi-open (semiaberto) regime [STF condena Eduardo Bolsonaro por coação no curso do processo ...](https://noticias.stf.jus.br/postsnoticias/stf-condena-eduardo-bolsonaro-por-coacao-no-curso-do-processo-sobre-tentativa-de-golpe/).
- There was NO pedido de vista and NO suspension of the session; the session concluded with a final verdict on the merits [STF condena Eduardo Bolsonaro por coação no curso do processo ...](https://noticias.stf.jus.br/postsnoticias/stf-condena-eduardo-bolsonaro-por-coacao-no-curso-do-processo-sobre-tentativa-de-golpe/).
- The date, June 16, 2026, falls squarely within the resolution window (May 12, 2026 – July 1, 2026) [STF condena Eduardo Bolsonaro por coação no curso do processo ...](https://noticias.stf.jus.br/postsnoticias/stf-condena-eduardo-bolsonaro-por-coacao-no-curso-do-processo-sobre-tentativa-de-golpe/).

This is corroborated by multiple credible Brazilian outlets, including the official STF portal (https://noticias.stf.jus.br/postsnoticias/stf-condena-eduardo-bolsonaro-por-coacao-no-curso-do-processo-sobre-tentativa-de-golpe/), G1 (https://g1.globo.com/politica/noticia/2026/06/16/stf-condena-eduardo-bolsonaro-o-que-acontece-agora.ghtml), JOTA, UOL, and Conjur, all reporting the June 16, 2026 conviction by the Primeira Turma.

All conditions of the resolution criteria are satisfied: a final merits verdict (conviction) by the First Panel, all ministers voting, result proclaimed, no suspension, within the window. The question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-135. `f8b8e64a-1462-56e8-8e51-2378eaca309f`

- Present date: `2026-05-01 10:40:50.314413`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-05-21 00:00:00`

**Question**

Will the April 28–29, 2026 FOMC minutes use a stronger quantifier than "some" for participants expressing openness to rate hikes?

**Resolution criteria**

This question resolves **Yes** if the official minutes of the April 28–29, 2026 FOMC meeting, as published on the Federal Reserve Board's FOMC minutes page (https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm), use a quantifier strictly higher than "some" on the Fed's standard linguistic scale to describe participants who expressed openness to rate hikes.

"Openness to rate hikes" is defined as any of the following sentiments attributed to participants in the minutes:
1. Favoring a "two-sided" description of future rate decisions that includes the possibility of rate increases, OR
2. Explicitly noting that "further firming" or "upward adjustments" to the federal funds rate target range could be appropriate under certain conditions, OR
3. Expressing a preference for removing or opposing the "easing bias" in the post-meeting statement in a context that reflects willingness to raise rates.

The Fed's standard linguistic hierarchy, from fewer to more participants, is: "a couple" < "a few" < "several" < "some" < "many" < "most" < "almost all" < "all". The March 2026 baseline is "some."

The question resolves **Yes** if and only if the April minutes attribute any of the above sentiments to "many," "most," "almost all," "all," or "a majority of" participants (or equivalent phrasing clearly indicating a larger group than "some").

The question resolves **No** if:
- The April minutes use "some," "several," "a few," "a couple," or any weaker quantifier for these sentiments, OR
- The April minutes do not discuss openness to rate hikes at all, OR
- The minutes are not published by June 1, 2026, at 23:59 UTC.

Resolution source: The official FOMC minutes as published at https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm.

**Pre-cutoff background**

The Federal Reserve's FOMC minutes use a well-known hierarchy of quantifiers to describe how many participants expressed a given view. From fewest to most, the standard scale is: "a couple" (2) < "a few" (3–4) < "several" (roughly 4–5) < "some" (roughly 5–7) < "many" (roughly 7–10) < "most" (roughly 10+) < "almost all" / "all."

In the minutes of the March 17–18, 2026 FOMC meeting (released April 8, 2026), the Fed stated: "Some participants judged that there was a strong case for a two-sided description of the Committee's future interest rate decisions in the post-meeting statement, reflecting the possibility that upwards adjustments to the target range for the federal funds rate could be appropriate if inflation were to remain at above-target levels." [Fed minutes show growing openness to rate hikes at March meeting](https://www.reuters.com/markets/us/fed-minutes-show-growing-openness-rate-hikes-march-meeting-2026-04-08/) This represented an increase from the January 2026 minutes, where only "several" participants had expressed similar openness [Fed minutes show growing openness to rate hikes at March meeting](https://www.reuters.com/markets/us/fed-minutes-show-growing-openness-rate-hikes-march-meeting-2026-04-08/).

The April 28–29, 2026 FOMC meeting was notably divisive. The Committee held the federal funds rate at 3-1/2 to 3-3/4 percent. Four members dissented: Beth M. Hammack, Neel Kashkari, and Lorie K. Logan dissented because they opposed the inclusion of an "easing bias" in the statement, while Stephen I. Miran dissented because he preferred a 25 basis-point rate cut [https://www.federalreserve.gov/newsevents/pressreleases/monetary20260429a.htm](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260429a.htm). The minutes of this meeting are expected to be released approximately three weeks after the meeting, around May 20, 2026, per the Federal Reserve's standard schedule (https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm).

The baseline from the March 2026 minutes is the quantifier "some" for participants expressing openness to rate hikes.

**Exact later resolution packet**

The question resolves YES. The official Federal Reserve FOMC calendar entry for the April 28–29, 2026 meeting lists the minutes at https://www.federalreserve.gov/monetarypolicy/fomcminutes20260429.htm and https://www.federalreserve.gov/monetarypolicy/files/fomcminutes20260429.pdf, with “Released May 20, 2026,” which is before the June 1, 2026 23:59 UTC deadline [The Fed - Meeting calendars and information - Federal Reserve](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm). In those official minutes, a qualifying rate-hike-openness sentiment is attributed to a stronger-than-“some” quantifier: “A majority of participants highlighted, however, that some policy firming would likely become appropriate if inflation were to continue to run persistently above 2 percent” [https://www.federalreserve.gov/monetarypolicy/files/fomcminutes20260429.pdf](https://www.federalreserve.gov/monetarypolicy/files/fomcminutes20260429.pdf). The quantifier over participants is “A majority of participants,” and the resolution criteria explicitly count “a majority of” as sufficient. The minutes also state: “To address this possibility, many participants indicated that they would have preferred removing the language from the postmeeting statement that suggested an easing bias regarding the likely direction of the Committee’s future interest rate decisions” [https://www.federalreserve.gov/monetarypolicy/files/fomcminutes20260429.pdf](https://www.federalreserve.gov/monetarypolicy/files/fomcminutes20260429.pdf). This matches the specified “removing or opposing the easing bias” sentiment, and “many” is strictly higher than “some” on the provided hierarchy. Therefore the April minutes did use a stronger quantifier than “some” for participants expressing openness to rate hikes [https://www.federalreserve.gov/monetarypolicy/files/fomcminutes20260429.pdf](https://www.federalreserve.gov/monetarypolicy/files/fomcminutes20260429.pdf).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-136. `827eb0fa-d233-5346-be4a-29d03e90dcbd`

- Present date: `2026-05-03 11:23:14.120798`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the Starship upper stage (Ship) achieve a controlled splashdown on SpaceX's Starship Flight 12?

**Resolution criteria**

This question resolves **Yes** if, on or after April 30, 2026 (UTC), SpaceX launches Starship Flight 12 and the Starship upper stage (Ship) achieves a **controlled splashdown**, defined as all of the following:

1. The Ship survives atmospheric reentry (i.e., is not destroyed or broken apart before reaching the landing phase).
2. The Ship performs a landing burn (igniting one or more Raptor engines to decelerate for a vertical or near-vertical descent).
3. The Ship makes contact with the ocean surface in a controlled manner and is not destroyed on impact (i.e., it is intact enough that SpaceX characterizes the event as a "splashdown," "soft splashdown," "soft landing," or "controlled splashdown").

The question resolves **No** if:
- Flight 12 does not launch by June 1, 2026, 23:59 UTC, OR
- The Ship is lost during ascent, in space, or during reentry, OR
- The Ship fails to perform a landing burn, OR
- The Ship is destroyed on ocean impact (e.g., a hard impact or breakup).

**Resolution source:** Official SpaceX communications, including the SpaceX website (https://www.spacex.com), the official SpaceX account on X/Twitter (https://x.com/SpaceX), or SpaceX's live launch webcast. In the absence of official SpaceX communications, credible space journalism outlets such as Space.com (https://www.space.com), NASASpaceflight.com (https://www.nasaspaceflight.com), or Ars Technica's space section (https://arstechnica.com/space) may be used.

**Pre-cutoff background**

SpaceX's Starship program has conducted 11 integrated flight tests as of late 2025. The Starship upper stage (Ship) has achieved controlled ocean splashdowns on Flights 4, 5, 6, 10, and 11, while failing on Flights 3 and 9, and being precluded from attempting splashdown on Flights 1, 2, 7, and 8 [List of Starship launches - Wikipedia](https://en.wikipedia.org/wiki/List_of_Starship_launches).

On Flight 10 (August 2025), the Ship sustained substantial damage to its engine section during reentry but successfully performed a soft splashdown within three meters of the target site in the Indian Ocean. On Flight 11 (October 2025), the Ship reentered with several heat shield tiles intentionally removed, remained mostly undamaged, and landed on target in the Indian Ocean [List of Starship launches - Wikipedia](https://en.wikipedia.org/wiki/List_of_Starship_launches).

Flight 12 is scheduled for May 2026 and will be the first flight of the Block 3 vehicle version — a significantly redesigned Starship with both new booster and ship hardware. It will also be the first launch from Starbase's second launch pad (OLP-2) [List of Starship launches - Wikipedia](https://en.wikipedia.org/wiki/List_of_Starship_launches). The combination of a new vehicle version, new pad, and a gap of over six months since the last flight introduces meaningful uncertainty about whether the Ship will successfully complete reentry and splashdown. While SpaceX achieved controlled splashdowns on four of the last five attempts with Block 1/2 hardware, Block 3 represents a substantial design change.

For reference, see: https://en.wikipedia.org/wiki/List_of_Starship_launches

**Exact later resolution packet**

The question resolves YES because all conditions for a "controlled splashdown" on Starship Flight 12 were met.

1. **Launch date within window:** Per the official SpaceX mission page, "On Friday, May 22, 2026, at 5:30 p.m. CT, Starship lifted off from Starbase, Texas on its twelfth flight test" — this is the first flight of the Block 3 / V3 vehicle [Starship's Twelfth Flight Test - SpaceX](https://www.spacex.com/launches/starship-flight-12). May 22, 2026 falls on or after April 30, 2026 (UTC) and before June 1, 2026 23:59 UTC, satisfying the antecedent that Flight 12 launched within the resolution window.

2. **Survived reentry:** SpaceX states "Starship re-entered the Earth's atmosphere and was able to gather critical data on the performance of its heatshield and structural strength" [Starship's Twelfth Flight Test - SpaceX](https://www.spacex.com/launches/starship-flight-12), and Space.com reported the Ship (Ship 39) survived reentry with no heat-shield burnthrough [Starship V3 Ship makes fiery splashdown in Indian Ocean as planned](https://www.space.com/news/live/spacex-starship-flight-12-launch-updates-may-22-2026).

3. **Landing burn performed:** SpaceX explicitly states the Ship "guided itself using its four flaps to the pre-planned splashdown zone in the Indian Ocean, and executed a landing flip, landing burn, and splashdown on two Raptor engines" [Starship's Twelfth Flight Test - SpaceX](https://www.spacex.com/launches/starship-flight-12).

4. **Controlled splashdown / SpaceX terminology:** SpaceX itself characterizes the event as a "splashdown" [Starship's Twelfth Flight Test - SpaceX](https://www.spacex.com/launches/starship-flight-12). The resolution criteria explicitly require only that "SpaceX characterizes the event as a 'splashdown,' 'soft splashdown,' 'soft landing,' or 'controlled splashdown'." The fact that the vehicle subsequently tipped over and exploded after the splashdown (as expected, consistent with prior flights) does not negate the controlled splashdown, since the Ship made controlled contact with the ocean and SpaceX designated it a splashdown [Starship V3 Ship makes fiery splashdown in Indian Ocean as planned](https://www.space.com/news/live/spacex-starship-flight-12-launch-updates-may-22-2026).

Sources: Official SpaceX Flight 12 page (https://www.spacex.com/launches/starship-flight-12) [Starship's Twelfth Flight Test - SpaceX](https://www.spacex.com/launches/starship-flight-12) and Space.com live coverage (https://www.space.com/news/live/spacex-starship-flight-12-launch-updates-may-22-2026) [Starship V3 Ship makes fiery splashdown in Indian Ocean as planned](https://www.space.com/news/live/spacex-starship-flight-12-launch-updates-may-22-2026).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-137. `2662961b-1d2b-5ea9-bb5d-a482fa2a86fd`

- Present date: `2026-05-02 17:14:45.179479`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will a new open-weight Vision-Language-Action (VLA) model with more than 7 billion parameters be published on HuggingFace on or after May 1, 2026, and before June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 1, 2026, and before 23:59 UTC on June 1, 2026, a new model meeting ALL of the following criteria is publicly available on the HuggingFace Model Hub (https://huggingface.co/models):

1. **Open-weight**: The model's weights (e.g., `.safetensors` or `.bin` files) must be freely downloadable from HuggingFace without requiring special access approval. This distinguishes "open-weight" from "open-source" (which would additionally require open training code and data) and from closed/proprietary models. Gated models that require only accepting terms of use but grant access automatically still qualify.

2. **Vision-Language-Action (VLA) model**: The model must accept visual observations (images or video) and natural-language instructions as input, and output robot action predictions (e.g., joint torques, end-effector poses, or discrete action tokens for robotic control). This distinguishes VLAs from standard Vision-Language Models (VLMs), which output only text. The model's HuggingFace model card, associated paper, or official documentation must explicitly describe it as a VLA or Vision-Language-Action model.

3. **More than 7 billion parameters**: The total parameter count of the model must exceed 7,000,000,000 (7 billion). This will be verified by checking the model's `config.json` or `model.safetensors.index.json` file on the HuggingFace repository, or by referencing the official model card or paper. If the model uses a mixture-of-experts architecture, the total parameter count (not active parameters) is what matters.

4. **New release**: The model must have been first uploaded to HuggingFace on or after May 1, 2026 (UTC). Re-uploads or forks of previously existing models do not count. The upload date can be verified from the HuggingFace repository's commit history.

The resolution source is the HuggingFace Model Hub. A search such as https://huggingface.co/models?search=VLA or browsing relevant organization pages (e.g., openvla, HuggingFaceVLA, nvidia) will be used to identify candidate models. If multiple models meet the criteria, only one is needed for Yes resolution.

**Pre-cutoff background**

Vision-Language-Action (VLA) models are a rapidly growing class of AI models that extend Vision-Language Models (VLMs) by adding the ability to output robot action tokens — typically low-level motor commands such as joint positions or end-effector velocities — in addition to processing visual and language inputs. VLA research has seen explosive growth: submissions to ICLR grew from 1 VLA paper in 2024 to 164 in 2026.

As of May 1, 2026, the largest publicly available open-weight VLA models include:
- **OpenVLA** (7B parameters): Built on a Llama 2 backbone, trained on 970K robot episodes from the Open X-Embodiment dataset. Available at https://huggingface.co/openvla/openvla-7b.
- **NVIDIA GR00T N1.7** (~3B parameters): An open reasoning VLA model for humanoid robots.
- **SmolVLA** (~450M parameters): Hugging Face's compact VLA designed to run on consumer hardware.
- **RDT-1B** (~1B parameters): Another open-weight VLA baseline.

No open-weight VLA model with more than 7B parameters has yet been released publicly on HuggingFace. Meanwhile, closed-weight models such as Google's Gemini-Robotics and RT-2-X (55B) significantly exceed this scale, and open-weight models are reportedly two to three generations behind closed ones. The field is under active development, with multiple labs (Physical Intelligence, Google DeepMind, NVIDIA, Hugging Face, Figure AI) working on VLA models of increasing scale.

**Exact later resolution packet**

Adjudicated: RLWRLD's RLDX-1-MT-DROID is an open-weight Vision-Language-Action model (explicitly tagged vla/vision-language-action, outputs 16-step robot action chunks) with 8.1B parameters (built on Qwen3-VL 8B), exceeding the 7B threshold, and its weights are freely downloadable on HuggingFace. It was first uploaded in the qualifying window: the HF 'RLDX-1 Release' commit is dated ~May 6, 2026, the technical report (arXiv:2605.03269) is dated May 6, 2026, and the model was publicly unveiled May 7, 2026, all on or after May 1 and before June 1, 2026. Only one qualifying model is needed for YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-138. `790bf01d-3c5d-5495-80b0-cb7444866c78`

- Present date: `2026-05-03 11:18:30.385946`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the French government's "Conférence Travail Emploi Retraites" hold its planned intermediate spring 2026 session by June 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after May 2, 2026, and no later than June 1, 2026 (23:59 UTC), the French government holds the intermediate session ("conférence intermédiaire") of the "Conférence Travail Emploi Retraites," as evidenced by at least one of the following:

1. An official announcement or press release published on the French government's information portal (https://info.gouv.fr/actualite) or the Prime Minister's website (https://www.gouvernement.fr/) confirming the session took place; OR
2. An official communiqué on the Ministry of Labour website (https://travail-emploi.gouv.fr/conference-travail-emploi-retraites) confirming the session occurred; OR
3. Credible reporting from major news agencies or outlets (e.g., AFP via Le Monde at https://www.lemonde.fr/, Reuters at https://www.reuters.com/, or France 24 at https://www.france24.com/) confirming the session was held.

The session must involve representatives from at least two of the following categories of social partners: (a) representative trade unions (CFDT, CGT, FO, CFTC, CFE-CGC); (b) representative employer organizations (MEDEF, CPME, U2P). It must be an official, government-convened meeting focused on pension reform or the broader work-employment-retirement agenda, not merely informal bilateral consultations.

The question resolves NO if no such intermediate conference is held by 23:59 UTC on June 1, 2026.

**Pre-cutoff background**

In late 2025, French lawmakers adopted the 2026 Social Security Financing Bill (PLFSS 2026), which suspended the controversial 2023 pension reform that had raised the legal retirement age from 62 to 64. Following this suspension, the government launched a broader process called the "Conférence Travail Emploi Retraites" (Work, Employment, and Pensions Conference) to address the future of the pension system.

In parallel, a structured consultation process ("concertation") among social partners on pensions has been underway, facilitated by Jean-Jacques Marette. As of May 2025, the participating organizations include employer groups MEDEF (Mouvement des entreprises de France, https://www.medef.com/) and CPME (Confédération des petites et moyennes entreprises), and trade unions CFDT (Confédération française démocratique du travail, https://www.cfdt.fr/), CFTC (Confédération française des travailleurs chrétiens, https://www.cftc.fr/), and CFE-CGC. Notably, three organizations—U2P, FO (Force ouvrière), and CGT (Confédération générale du travail)—have withdrawn from this process [Concertation sur les retraites : les partenaires sociaux se donnent ...](https://www.boursorama.com/actualite-economique/actualites/concertation-sur-les-retraites-les-partenaires-sociaux-se-donnent-jusqu-au-17-juin-pour-trouver-un-accord-f1492631f9d8c6dad5c5b910318fc783). Plenary negotiation sessions are scheduled for June 5, 11, 12, and 17, 2026, with the social partners targeting June 17, 2026, as their deadline to reach agreement [Concertation sur les retraites : les partenaires sociaux se donnent ...](https://www.boursorama.com/actualite-economique/actualites/concertation-sur-les-retraites-les-partenaires-sociaux-se-donnent-jusqu-au-17-juin-pour-trouver-un-accord-f1492631f9d8c6dad5c5b910318fc783).

The government's "Conférence Travail Emploi Retraites" website (https://travail-emploi.gouv.fr/conference-travail-emploi-retraites) indicated that initial findings ("premières restitutions") would be presented at an intermediate conference ("conférence intermédiaire") in spring 2026. However, the exact date has not been publicly confirmed, and the politically sensitive nature of pension reform—combined with President Macron's reported pivot toward foreign policy and a stalled domestic agenda—creates genuine uncertainty about whether this intermediate session will occur on schedule.

Key topics under discussion include the retirement age, professional hardship ("pénibilité"), pensions for women (particularly mothers), and the financial equilibrium of the pension system [Concertation sur les retraites : les partenaires sociaux se donnent ...](https://www.boursorama.com/actualite-economique/actualites/concertation-sur-les-retraites-les-partenaires-sociaux-se-donnent-jusqu-au-17-juin-pour-trouver-un-accord-f1492631f9d8c6dad5c5b910318fc783). A "concertation" in French administrative practice refers to a formal, structured consultation process between the government and recognized social partners (representative trade unions and employer organizations), as defined in French labor law (see https://fr.wikipedia.org/wiki/Concertation). A "pension reform framework" here means any formal government proposal or set of principles for modifying the existing pension system's rules on retirement age, contribution periods, or financing.

**Exact later resolution packet**

The question resolves YES. The French government's "Conférence Travail Emploi Retraites" held its planned intermediate sessions within the resolution window (May 2 – June 1, 2026).

Key evidence:

1. ALLOWED SOURCE (Le Monde / AFP): Le Monde published an article on 2026-05-14 titled "Conférence sur le travail, l'emploi et les retraites : des syndicats en désaccord avec des documents soumis à discussion" (https://www.lemonde.fr/politique/article/2026/05/14/conference-sur-le-travail-l-emploi-et-les-retraites-des-syndicats-en-desaccord-avec-des-documents-soumis-a-discussion_6689096_823448.html). It reports that a "nouvelle réunion" of the government-launched conference took place on Tuesday 12 May 2026, with social partners reviewing documents on the pension system. Force ouvrière (FO) and CGT (trade unions) plus employer-side organizations were involved. The conference was launched at the government's initiative following the autumn 2025 suspension of the 2023 pension reform [b53bef].

2. The "réunion intermédiaire" / "conférence intermédiaire" presenting "premières restitutions" was specifically planned as a plenary on 22 May 2026 to draw up a "bilan intermédiaire" (intermediate assessment). This is corroborated by the CGT account of the 12 May 2026 meeting, which states a plenary was scheduled for 22 May to present the intermediate assessment, and confirms participation by all eight representative trade unions (including CFDT, CGT, FO, CFTC, CFE-CGC) and employer organizations CPME and U2P (with MEDEF boycotting) [850483]. The 22 May 2026 plenary in fact took place — described as the fifth session of the conference, which "a réuni les partenaires sociaux du public et du privé le 22 mai" (per La Gazette des communes reporting).

Both the 12 May and 22 May 2026 sessions fall strictly within the May 2 – June 1, 2026 window. Both were official, government-convened meetings (not informal bilateral consultations) of the Conférence Travail Emploi Retraites focused on the work-employment-retirement/pension agenda, and both included representatives from at least two distinct categories of social partners (trade unions AND employer organizations such as CPME/U2P) [b53bef][850483].

Therefore the intermediate session of the "Conférence Travail Emploi Retraites" was held by June 1, 2026, satisfying all resolution criteria. Resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-139. `21cd5ba6-ebae-599a-ae0b-d23e57b0da25`

- Present date: `2026-05-02 16:52:08.647222`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Hungary formally notify the UN Secretary-General of the revocation of its withdrawal from the Rome Statute between May 1, 2026 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between May 1, 2026 00:00 UTC and June 1, 2026 23:59 UTC, the United Nations Secretary-General receives a formal written notification from the Government of Hungary revoking its withdrawal from the Rome Statute of the International Criminal Court.

The formal notification must occur on or after May 1, 2026 00:00 UTC to fall within the resolution window.

**Resolution source:** The [United Nations Treaty Collection (UNTC) status page for the Rome Statute](https://treaties.un.org/pages/ViewDetails.aspx?src=TREATY&mtdsg_no=XVIII-10&chapter=18&clang=_en), including the [Depositary Notifications (CNs) section](https://treaties.un.org/pages/CNs.aspx?cnTab=tab1), will serve as the primary resolution source. If the UNTC has not yet been updated by June 1, 2026, official statements or press releases from the [UN Secretary-General's office](https://www.un.org/sg/en) or the [ICC Assembly of States Parties](https://www.icc-cpi.int/) confirming receipt of such notification may also be used.

If no such notification is recorded or confirmed by June 1, 2026 23:59 UTC, the question resolves **No**.

**Pre-cutoff background**

On April 3, 2025, Hungarian Prime Minister Viktor Orbán announced Hungary's withdrawal from the Rome Statute of the International Criminal Court (ICC). The formal notification of withdrawal was received by the UN Secretary-General on June 2, 2025, making the withdrawal effective on June 2, 2026, per Article 127 of the Rome Statute, which requires one year's notice [Hungary's Road Back to the Rule of Law Runs through the ICC](https://www.hrw.org/news/2026/04/24/hungarys-road-back-to-the-rule-of-law-runs-through-the-icc).

On April 12, 2026, Péter Magyar of the Tisza Party won Hungary's general election. Magyar has publicly pledged to reverse Hungary's withdrawal from the ICC. However, as of April 24, 2026, Magyar remains "Prime Minister-elect" and no formal revocation notification has been submitted to the UN Secretary-General [Hungary's Road Back to the Rule of Law Runs through the ICC](https://www.hrw.org/news/2026/04/24/hungarys-road-back-to-the-rule-of-law-runs-through-the-icc).

Under the [Vienna Convention on the Law of Treaties (1969), Article 68](https://legal.un.org/ilc/texts/instruments/english/conventions/1_1_1969.pdf), a notification of withdrawal may be revoked at any time before it takes effect. To do so, Hungary must formally notify ("formally notify") the UN Secretary-General — who serves as the [depositary](https://treaties.un.org/pages/Overview.aspx?path=overview/definition/page1_en.xml) of the Rome Statute — of the revocation ("revocation") of its withdrawal notification. "Formally notify" means submitting an official written communication to the UN Secretary-General in his capacity as depositary. "Revocation" means the act of rescinding or cancelling the previously submitted withdrawal notification, as contemplated under Article 68 of the Vienna Convention.

The withdrawal takes effect on June 2, 2026, creating a narrow window for action. Key uncertainties include: the timeline for Magyar's government formation, whether political or bureaucratic obstacles delay the formal notification, and whether the new government prioritizes this among competing early tasks.

The UN Treaty Collection status page for the Rome Statute currently lists Hungary as a party, with no withdrawal or revocation notation visible on the main status page [10. Rome Statute of the International Criminal Court - UNTC](https://treaties.un.org/pages/ViewDetails.aspx?src=TREATY&mtdsg_no=XVIII-10&chapter=18&clang=_en), though the depositary notification of withdrawal exists as a separate document (C.N.225.2025).

**Exact later resolution packet**

The question resolves YES. The UN Treaty Collection Depositary Notification C.N.180.2026.TREATIES-XVIII.10, titled "HUNGARY: WITHDRAWAL OF NOTIFICATION OF WITHDRAWAL," confirms that the UN Secretary-General, acting in his capacity as depositary of the Rome Statute, received Hungary's formal notification revoking its withdrawal, with the action effected on May 29, 2026 [fa7519]. This date falls squarely within the resolution window of May 1, 2026 00:00 UTC to June 1, 2026 23:59 UTC.

This is independently corroborated by the International Criminal Court's official press release welcoming Hungary's decision to remain a State Party, which states that the Government of Hungary formally notified the UN Secretary-General of the withdrawal of its notification of withdrawal on May 29, 2026, with immediate effect [949781].

Additional context: Hungary's Orbán government had withdrawn from the Rome Statute via notification received by the UN Secretary-General on June 2, 2025 (C.N.225.2025), with the withdrawal set to take effect on June 2, 2026. After Péter Magyar's election win, the Hungarian parliament voted on May 27, 2026 to reverse the withdrawal, and the formal revocation notification was deposited with the UN Secretary-General on May 29, 2026 — before the withdrawal would have taken effect.

The notification was specifically a revocation/withdrawal of the prior withdrawal notification (not merely a promise or intention), was a formal written communication to the UN Secretary-General as depositary, and was received within the required window. Direct source URL: https://treaties.un.org/doc/Publication/CN/2026/CN.180.2026-Eng.pdf

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-140. `2969b0a0-9166-54e6-9e29-1c68723e1175`

- Present date: `2026-05-14 06:37:08.801512`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Supreme Court's opinion in Sripetch v. SEC explicitly address whether disgorgement under Section 21(d)(7) triggers Seventh Amendment jury trial rights?

**Resolution criteria**

This question resolves based on the Supreme Court's opinion in *Sripetch v. SEC* (No. 25-466), issued on or after May 12, 2026.

**Resolves YES** if any written opinion filed by the Court—including the majority opinion, concurrences, or dissents—explicitly discusses whether disgorgement under Section 21(d)(7) of the Securities Exchange Act (15 U.S.C. § 78u(d)(7)) triggers the right to a jury trial under the Seventh Amendment to the U.S. Constitution. "Explicitly discusses" means the opinion contains substantive analysis or argumentation about the Seventh Amendment jury trial right in the context of disgorgement; a passing or hypothetical reference (e.g., "we do not reach the question of whether...") does NOT count.

**Resolves NO** if the Court issues its opinion without any justice substantively addressing the Seventh Amendment jury trial question in a written opinion, OR if no opinion is issued by July 1, 2026.

**Resolution source**: The text of the opinion as published on the [Supreme Court's Opinions of the Court page](https://www.supremecourt.gov/opinions/slipopinions.aspx).

**Pre-cutoff background**

In *Sripetch v. SEC* (No. 25-466), the U.S. Supreme Court is considering whether the Securities and Exchange Commission (SEC) must prove pecuniary harm to investors when seeking disgorgement in civil enforcement actions. Oral arguments were held on April 20, 2026 [Justices Appear Skeptical of Investor-Harm Requirement in Sripetch ...](https://www.foley.com/insights/publications/2026/04/justices-appear-skeptical-of-investor-harm-requirement-in-sripetch-sec-disgorgement-case/). The case follows the 2020 decision in *Liu v. SEC*, which characterized disgorgement as an equitable remedy limited to returning funds "for the benefit of investors." In 2021, Congress enacted [Section 21(d)(7) of the Securities Exchange Act](https://www.law.cornell.edu/uscode/text/15/78u#d_7), which explicitly authorizes the SEC to seek "disgorgement" but omits the "for the benefit of investors" language from *Liu*.

Key definitions:
- **Disgorgement**: A remedy requiring a party to give up profits obtained through illegal or wrongful conduct. See [Cornell LII definition](https://www.law.cornell.edu/wex/disgorgement).
- **Section 21(d)(7)**: A provision of the Securities Exchange Act of 1934 (codified at [15 U.S.C. § 78u(d)(7)](https://www.law.cornell.edu/uscode/text/15/78u#d_7)) that expressly authorizes federal courts to order disgorgement in SEC enforcement actions.
- **Seventh Amendment**: The [Seventh Amendment to the U.S. Constitution](https://www.law.cornell.edu/constitution/seventh_amendment) preserves the right to a jury trial in civil cases at common law where the value in controversy exceeds twenty dollars.

The petitioner, Sripetch, argues that disgorgement without a requirement to prove investor harm functions as a "civil penalty" rather than an equitable remedy. If the Court agrees, this classification could trigger the [Seventh Amendment](https://www.law.cornell.edu/constitution/seventh_amendment) right to a jury trial, fundamentally altering SEC enforcement by requiring jury trials for disgorgement claims [Justices Appear Skeptical of Investor-Harm Requirement in Sripetch ...](https://www.foley.com/insights/publications/2026/04/justices-appear-skeptical-of-investor-harm-requirement-in-sripetch-sec-disgorgement-case/).

A central uncertainty is whether the Court will reach this constitutional question at all. Under the **doctrine of constitutional avoidance**, courts prefer to resolve cases on the narrowest possible grounds—typically statutory interpretation—rather than reaching constitutional questions when not strictly necessary [Justices Appear Skeptical of Investor-Harm Requirement in Sripetch ...](https://www.foley.com/insights/publications/2026/04/justices-appear-skeptical-of-investor-harm-requirement-in-sripetch-sec-disgorgement-case/). In this case, the Court could decide the statutory question (whether Section 21(d)(7) requires proof of investor harm) without ever addressing the Seventh Amendment implications. During oral arguments, the justices appeared skeptical of the petitioner's investor-harm requirement, suggesting the Court may affirm the SEC's position on statutory grounds alone and never reach the constitutional issue [Justices Appear Skeptical of Investor-Harm Requirement in Sripetch ...](https://www.foley.com/insights/publications/2026/04/justices-appear-skeptical-of-investor-harm-requirement-in-sripetch-sec-disgorgement-case/).

As of May 12, 2026, the case has been argued and a decision is expected before the end of the Supreme Court's October 2025 term (typically by late June or early July 2026).

**Exact later resolution packet**

RESOLVES YES.

**The opinion was issued in time.** The Supreme Court decided Sripetch v. SEC, No. 25-466, on June 4, 2026 — before the July 1, 2026 deadline. The slip opinion is published on the official Supreme Court site at https://www.supremecourt.gov/opinions/25pdf/25-466_5i26.pdf [7bbfaa]. The Court unanimously held (Gorsuch, J.) that the SEC need not prove pecuniary loss to investors to obtain disgorgement.

**A written opinion substantively discusses the Seventh Amendment jury-trial question for Section 21(d)(7) disgorgement.** Justice Clarence Thomas filed a concurring opinion that does far more than make a passing reference. Per the slip opinion text and multiple independent analyses, Thomas argues that Congress's post-Liu codification of disgorgement (adding 15 U.S.C. § 78u(d)(7)) transformed disgorgement into a *legal* remedy for which the Seventh Amendment requires a jury trial. He wrote that "[i]n a future case, we should recognize that disgorgement is now a legal remedy for which the Seventh Amendment requires a jury trial" [7bbfaa]. His concurrence lays out a detailed, multi-pronged argument: (1) SEC disgorgement doesn't resemble any traditional equitable remedy (constructive trust, equitable lien, accounting for profits); (2) it more closely resembles legal restitution via assumpsit; (3) Congress enumerated disgorgement separately from "equitable relief," signaling a legal remedy; and (4) the SEC's practice of retaining most disgorged funds rather than returning them to victims makes it "a fines regime" — an inherently legal process [d08544, 942cea]. This constitutes "substantive analysis or argumentation about the Seventh Amendment jury trial right in the context of disgorgement," satisfying the YES criterion.

**Why this is not a mere "passing or hypothetical reference."** The resolution criteria exclude passing/hypothetical mentions (e.g., "we do not reach the question of whether..."). While the majority opinion largely avoided the constitutional question (assuming without deciding that § 21(d)(7) disgorgement remains equitable, and citing SEC v. Jarkesy only to note the boundary [7bbfaa, 47e5da]), Thomas's separate concurrence provides the full substantive analysis — a "road map to argue that disgorgement under § 78u(d)(7) is a legal remedy requiring a jury trial" [d08544] and an opinion that "argues that post-Liu statutory amendments transformed disgorgement into a legal remedy, triggering Seventh Amendment" jury-trial rights [942cea]. Because the criteria count ANY written opinion (majority, concurrence, or dissent), Thomas's concurrence alone is sufficient for YES.

**Sources of the specific opinion text** are corroborated across the official slip opinion [7bbfaa], Cornell LII's reproduction, SCOTUSblog [e1b0ce], O'Melveny [47e5da], Eye on Enforcement/Bradley [942cea], and Hogan Lovells [d08544], all consistent that Thomas's concurrence squarely addresses the Seventh Amendment jury-trial right for § 21(d)(7) disgorgement.

Slip opinion URL (resolution source): https://www.supremecourt.gov/opinions/25pdf/25-466_5i26.pdf

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-141. `cc5f270c-92de-51fe-9ca8-5724ccda77ce`

- Present date: `2026-05-29 03:04:18.970822`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Japan conduct a live-fire missile exercise outside Japanese territory between May 12, 2026, and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between May 12, 2026, 00:00 UTC and July 1, 2026, 23:59 UTC, the Japan Self-Defense Forces (JSDF) — including any branch (JGSDF, JMSDF, or JASDF) — conduct at least one live-fire missile exercise outside Japanese territory. This explicitly excludes the Balikatan 2026 Type 88 firing that occurred on May 6, 2026.

**Definitions:**

- **"Live-fire missile exercise"**: The actual launch and flight of a guided missile (not a rocket, bomb, torpedo, or unguided munition) by JSDF personnel or from a JSDF platform. This includes surface-to-ship missiles, surface-to-air missiles, air-to-surface missiles, cruise missiles (e.g., Tomahawk), and anti-ship missiles. Simulated launches, inert training rounds without propulsion, or launches conducted solely by non-Japanese forces do not count. The missile must be launched by JSDF personnel or from a JSDF-operated platform (e.g., a JMSDF destroyer).

- **"Outside Japanese territory"**: The launch must originate from a location outside Japan's sovereign territory as defined under international law, meaning outside Japan's land territory, internal waters, and territorial sea (extending 12 nautical miles from baselines per UNCLOS Article 3). Japan's Exclusive Economic Zone (EEZ) beyond the 12 nm territorial sea is considered "outside Japanese territory" for purposes of this question. Launches from Japanese soil or territorial waters do not count.

**Resolution source**: Official Japan Ministry of Defense press releases (https://www.mod.go.jp/en/), credible international news reporting from outlets such as Reuters, AP, Nikkei Asia, or Naval News, or official U.S. Department of Defense announcements (https://www.defense.gov/News/).

**Pre-cutoff background**

On May 6, 2026, Japan's Ground Self-Defense Force (JGSDF) fired two Type 88 surface-to-ship missiles from Philippine territory during the Balikatan 2026 joint military exercise, sinking a decommissioned Philippine Navy vessel (BRP Quezon) approximately 75 km offshore in the Luzon Strait. This marked Japan's first post-WWII offensive missile launch outside Japanese territory and represented a major threshold crossing in Japan's evolving military posture. China condemned the action, with the Global Times calling it "a major and dangerous gamble."

Separately, Japan has announced plans to test U.S.-made Tomahawk cruise missiles from the destroyer JS Chokai in the eastern Pacific during summer 2026, which would constitute another live-fire missile exercise outside Japanese territory.

The question asks whether Japan will conduct an additional such exercise after the Balikatan 2026 firing, signaling that overseas missile employment is becoming a new norm rather than remaining a one-off event. The Tomahawk test and other scheduled bilateral or multilateral exercises (e.g., RIMPAC 2026) make this plausible but not certain within the short window.

**Exact later resolution packet**

Adjudicated: During the Valiant Shield 2026 SINKEX on June 27, 2026 (within the May 12 - July 1, 2026 window), a JMSDF SH-60 helicopter fired an AGM-114 Hellfire missile and a JMSDF destroyer launched a Type 90 (SSM-1B) anti-ship missile at the decommissioned USS Juneau, more than 200 nautical miles off Guam in the Mariana Islands Range Complex (Philippine Sea), per USNI News citing photos released by Japan's Joint Staff Office. Both are guided missiles fired from JSDF-operated platforms, outside Japan's 12 nm territorial sea, satisfying every clause of the criteria (the Hellfire is an air-to-surface/anti-ship missile, the Type 90 an anti-ship missile). An initial automated pass only found the JMSDF submarine torpedo (which is excluded) and missed the two guided-missile launches, but the Hellfire and Type 90 independently trigger a YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-142. `4b771d76-4181-5d22-b2f7-75f999b3b4d5`

- Present date: `2026-05-03 10:56:52.644547`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the US-Iran ceasefire (initially agreed April 8, 2026) still be in effect on May 31, 2026?

**Resolution criteria**

This question resolves **Yes** if, at 23:59 UTC on May 31, 2026, the US-Iran ceasefire (as originally agreed on April 8, 2026, and extended on April 21, 2026) is still considered to be in effect. It resolves **No** otherwise.

The ceasefire is considered "in effect" if **both** of the following conditions are met on or after May 1, 2026, through May 31, 2026:

1. **No formal termination**: Neither the United States government (via official White House or Department of Defense statement) nor the Iranian government (via official statement from the President, Supreme Leader, or armed forces command) has declared the ceasefire terminated or expired.
2. **No resumption of major direct military hostilities**: There has been no resumption of direct US-Iran kinetic military operations — defined as airstrikes, missile strikes, or ground combat operations conducted by one party against the territory or military forces of the other. Note: continuation of the existing naval blockade, minor skirmishes or incidents involving proxy forces, and alleged violations that do not lead to a formal termination do **not** by themselves constitute a collapse of the ceasefire.

If the ceasefire is **replaced** by a formal peace agreement or new ceasefire agreement that supersedes the April 8 agreement, the question still resolves **Yes**, as the cessation of hostilities remains in effect.

**Resolution sources**: Official statements from the White House (https://www.whitehouse.gov), US Department of State (https://www.state.gov), Iranian government media (e.g., IRNA), or credible international news reporting from Reuters (https://www.reuters.com), Associated Press (https://apnews.com), BBC (https://www.bbc.com), or the UN News Centre (https://news.un.org).

Resolution depends on events occurring on or after May 1, 2026.

**Pre-cutoff background**

On April 8, 2026, the United States and Iran agreed to a two-week ceasefire in the 2026 Iran war, mediated by Pakistan. The agreement was intended to halt hostilities and facilitate negotiations for a permanent settlement. Negotiations in Islamabad failed on April 12, 2026, and the United States subsequently imposed a naval blockade on Iran [2026 Iran war ceasefire](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire).

On April 21, 2026, President Donald Trump announced an extension of the ceasefire with no set deadline, stating it would remain in place until Iran submitted a proposal and "discussions are concluded, one way or the other." The US naval blockade of Iranian ports has continued throughout the ceasefire period [2026 Iran war ceasefire](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire).

As of May 1, 2026, the ceasefire remains fragile but technically in effect. Key tensions include:
- Defense Secretary Pete Hegseth has argued that the 60-day War Powers Act deadline "pauses or stops in a ceasefire," a legally contested claim [Headlines for May 01, 2026 | Democracy Now!](https://www.democracynow.org/2026/5/1/headlines).
- Iranian President Masoud Pezeshkian has condemned the US naval blockade as "intolerable" [Headlines for May 01, 2026 | Democracy Now!](https://www.democracynow.org/2026/5/1/headlines).
- Both sides have accused each other of ceasefire violations [2026 Iran war ceasefire](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire).
- Iran submitted a new proposal for talks, but the Trump administration appeared unlikely to accept it as of late April 2026.
- US military officials were developing contingency plans to target Iran's capabilities in the Strait of Hormuz in the event the ceasefire collapses.

The two sides have conflicting positions: the US seeks nuclear constraints on Iran and a phased settlement, while Iran demands cessation of war on all fronts (including Iraq, Lebanon, and Yemen), lifting of all sanctions, release of frozen assets, and war reparations [2026 Iran war ceasefire](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire). For more background, see the Wikipedia article on the ceasefire: https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire

**Exact later resolution packet**

Adjudicated: At 23:59 UTC on May 31, 2026 no formal termination of the ceasefire had been declared by either government, and as of June 1-2 the ceasefire was still reported as 'in place but fragile, not formally terminated' (VP Vance on May 28: 'the ceasefire remains in place'). The direct US-Iran strikes in May (May 7, 25-27, 28) were uniformly characterized by both governments and authoritative sources as 'violations'/'defensive flare-ups' that did NOT lead to formal termination, and the criteria's controlling Note explicitly states such 'alleged violations that do not lead to a formal termination do not by themselves constitute a collapse.' Both parties continued treating the ceasefire as in force and were negotiating a 60-day extension, so under the literal criteria the ceasefire was still 'in effect.'

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-143. `62ec58a1-6c82-567a-9cfd-1473293ea2f1`

- Present date: `2026-05-07 22:44:42.018580`
- Source cutoff boundary: `2026-05-08` (encodes end of UTC day `2026-05-07`)
- Expected resolution: `2026-06-20T00:00:00`

**Question**

Will all four invited non-G7 leaders (India, South Korea, Brazil, Kenya) attend the 2026 G7 Évian Summit in person?

**Resolution criteria**

This question resolves **Yes** if all four of the following officeholders physically attend the 2026 G7 Summit at the summit venue in Évian-les-Bains, France, during any portion of the summit (15–17 June 2026, CEST / UTC+2):

1. **The Prime Minister of India** (as of summit date; currently Narendra Modi)
2. **The President of South Korea** (as of summit date; currently Lee Jae Myung)
3. **The President of Brazil** (as of summit date; currently Luiz Inácio Lula da Silva)
4. **The President of Kenya** (as of summit date; currently William Ruto)

"In person" means the leader is physically present at the summit venue in Évian-les-Bains at any point during 15–17 June 2026 (CEST / UTC+2). Virtual or remote participation does not count. Attendance by a deputy, foreign minister, or any other representative does not count.

If any of the four leaders does not attend in person — whether due to cancellation, sending a representative, virtual participation, or any other reason — the question resolves **No**.

If the summit itself is cancelled or postponed beyond 30 June 2026 (UTC), the question resolves **No**.

**Resolution source:** Official summit communiqués and attendee lists published at the [official G7 French Presidency website](https://www.elysee.fr/en/G7evian), official summit photography, or credible reporting from major wire services (Reuters, AP, AFP) confirming the physical presence or absence of these leaders.

**Pre-cutoff background**

The 52nd G7 Summit is scheduled for 15–17 June 2026 in Évian-les-Bains, Haute-Savoie, France [52nd G7 summit](https://en.wikipedia.org/wiki/52nd_G7_summit). France has invited four non-G7 countries to participate: India, South Korea, Brazil, and Kenya. The invited leaders are Prime Minister Narendra Modi (India), President Lee Jae Myung (South Korea), President Luiz Inácio Lula da Silva (Brazil), and President William Ruto (Kenya) [52nd G7 summit](https://en.wikipedia.org/wiki/52nd_G7_summit).

As of 7 May 2026 (UTC+1, Central European Summer Time):
- **South Korea:** President Lee Jae Myung has accepted French President Emmanuel Macron's official invitation to the summit [52nd G7 summit](https://en.wikipedia.org/wiki/52nd_G7_summit).
- **India:** Prime Minister Narendra Modi has been invited. No public confirmation of attendance has been reported as of this date.
- **Brazil:** President Lula da Silva has been invited and has attended every G7 summit since 2023. No formal confirmation for 2026 has been publicly reported.
- **Kenya:** President William Ruto has been invited. No formal confirmation of attendance has been publicly reported.

Leaders sometimes cancel attendance due to domestic crises, health issues, scheduling conflicts, or diplomatic disputes, and may send deputies or participate virtually instead. The question requires all four to attend in person for a "Yes" resolution.

**Exact later resolution packet**

RESOLUTION: YES (1).

The question resolves YES if all four invited non-G7 officeholders — the Prime Minister of India (Narendra Modi), the President of South Korea (Lee Jae Myung), the President of Brazil (Luiz Inácio Lula da Silva), and the President of Kenya (William Ruto) — physically attended the 2026 G7 Summit at the venue in Évian-les-Bains, France, at any point during 15–17 June 2026.

1) The summit occurred and was NOT cancelled or postponed. The G7 Summit was held in Évian-les-Bains, France, on 15–17 June 2026, hosted by President Emmanuel Macron, as confirmed by the official French Presidency (Élysée) day-three page and press conference transcript [32ad50] and by Reuters live coverage [f92102]. This defeats the "cancelled/postponed beyond 30 June 2026 = NO" clause.

2) DECISIVE SOURCE — all four leaders physically present. The Reuters live blog "G7 summit 2026 live" (https://www.reuters.com/world/g7-summit-2026-live-trump-discuss-iran-ukraine-with-world-leaders-2026-06-16/) reported, under an item about the leaders' "family photo" (16 June 2026), that "Egyptian President Abdel Fattah al-Sisi, South Korea's President Lee Jae Myung, India's Prime Minister Narendra Modi, Brazilian President Luiz Inacio Lula da Silva and Kenya's President William Ruto joined the G7 and European Union leaders for a family photo" in Évian-les-Bains [f92102]. Joining a physical group/family photo at the venue establishes in-person presence (not virtual) for all four required individuals.

3) INDEPENDENT CORROBORATION for South Korea. The Korea Herald ("In photos: S. Korea returns to G7 on second straight invite") states "South Korean President Lee Jae Myung attended the Group of Seven summit in Evian-les-Bains, France, on Tuesday as an invited guest," with photos of Lee in an expanded session, at the gala dinner, and in the official group photo alongside India's Modi and Brazil's Lula [e0ebc1].

4) Actual officeholders, not deputies/representatives. The named individuals who attended (Modi, Lee, Lula, Ruto) are the incumbent Prime Minister of India, President of South Korea, President of Brazil, and President of Kenya, respectively [f92102, e0ebc1]. No evidence of any substitution by deputy, foreign minister, or other representative.

5) On apparently conflicting readings: Queries against the France-diplomatie "outcomes" page [219a35] and the Élysée day-three transcript [32ad50] did not enumerate all four leaders by name and thus did not, on their own, confirm each individual — but they do NOT contradict attendance; they simply lack the roster detail. The Reuters family-photo item [f92102] and Korea Herald photos [e0ebc1] provide the explicit, name-level, in-person confirmation for all four. Reuters is one of the major wire services expressly named as an acceptable resolution source.

All four required leaders were physically present at the Évian venue during the summit window, so the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-144. `81580f62-1a98-5bc6-969b-69cbb1f75e00`

- Present date: `2026-04-30 17:00:55.659695`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the 2026 Israel-Lebanon ceasefire be extended beyond its mid-May 2026 expiration date?

**Resolution criteria**

This question resolves as **Yes** if, on or after April 30, 2026 (00:00 UTC), and by June 1, 2026 (23:59 UTC), there is an official announcement or credible reporting confirming that the ceasefire has been extended beyond the expiration date established by the April 23, 2026 extension (approximately May 14, 2026). For clarity, the April 23, 2026 extension itself does NOT count toward resolution.

An "extension" is defined as any of the following:
- A formal announcement by any of the relevant parties of a new end date for the ceasefire beyond approximately May 14, 2026.
- A formal announcement of an indefinite continuation of the ceasefire.
- A permanent peace agreement or new security treaty between Israel and Lebanon that supersedes the ceasefire. (This counts as Yes, since it effectively extends the cessation of hostilities beyond the expiration date.)

This question resolves as **No** if:
1. The ceasefire expires on or around May 14, 2026 without a formal extension, permanent agreement, or new security treaty.
2. Full-scale hostilities resume before or at the expiration date without any extension being announced.

**Authoritative resolution sources:** Official statements from the Israeli Government (https://www.gov.il/en), the Lebanese Government, or the U.S. Department of State (https://www.state.gov/), or reporting from major international wire services such as Reuters (https://www.reuters.com/), the Associated Press (https://apnews.com/), or AFP.

**Pre-cutoff background**

The 2026 Israel-Lebanon ceasefire is a temporary cessation of hostilities that began on April 16, 2026, amid the 2026 Lebanon war [https://en.wikipedia.org/wiki/2026_Israel%E2%80%93Lebanon_ceasefire](https://en.wikipedia.org/wiki/2026_Israel%E2%80%93Lebanon_ceasefire). The agreement, brokered by the United States, was initially set for 10 days. On April 23, 2026, U.S. President Donald Trump announced a three-week extension, moving the expiration date to approximately May 14, 2026 [https://en.wikipedia.org/wiki/2026_Israel%E2%80%93Lebanon_ceasefire](https://en.wikipedia.org/wiki/2026_Israel%E2%80%93Lebanon_ceasefire)[https://english.news.cn/20260429/33d546c9c45043058ab5c6a266c67f4e/c.html](https://english.news.cn/20260429/33d546c9c45043058ab5c6a266c67f4e/c.html).

Despite the ceasefire, violations have been reported from both sides, and the Israeli Defense Forces chief has stated there is "no ceasefire in southern Lebanon" as operations continue [https://en.wikipedia.org/wiki/2026_Israel%E2%80%93Lebanon_ceasefire](https://en.wikipedia.org/wiki/2026_Israel%E2%80%93Lebanon_ceasefire). Israeli officials have characterized this extension as the "final window" for reaching a permanent agreement and have threatened to escalate military operations against Hezbollah if a permanent deal is not reached by the mid-May deadline [https://english.news.cn/20260429/33d546c9c45043058ab5c6a266c67f4e/c.html](https://english.news.cn/20260429/33d546c9c45043058ab5c6a266c67f4e/c.html). Israeli Prime Minister Benjamin Netanyahu has stated that Israel will continue attacks and maintain a "security zone" inside Lebanon [https://english.news.cn/20260429/33d546c9c45043058ab5c6a266c67f4e/c.html](https://english.news.cn/20260429/33d546c9c45043058ab5c6a266c67f4e/c.html).

Whether the ceasefire is extended again, replaced by a permanent agreement, or collapses into renewed full-scale hostilities remains genuinely uncertain as of April 30, 2026.

**Exact later resolution packet**

The question resolves YES.

Resolution criteria: YES if, on or after April 30, 2026 (00:00 UTC) and by June 1, 2026 (23:59 UTC), there is an official announcement or credible reporting confirming the ceasefire was extended beyond the ~May 14, 2026 expiration date set by the April 23 extension. The April 23 extension explicitly does NOT count.

Evidence: On May 15, 2026, Israel and Lebanon agreed to a 45-day extension of the ceasefire following talks in Washington. This was announced by the U.S. State Department (spokesperson Tommy Pigott), who stated "The April 16 cessation of hostilities will be extended by 45 days to enable further progress" [Israel, Lebanon extend ceasefire by 45 days as Washington talks ...](https://www.reuters.com/world/middle-east/israel-lebanon-agree-extend-ceasefire-by-45-days-us-state-dept-says-2026-05-15/). This is confirmed by Reuters ("Israel, Lebanon extend ceasefire by 45 days as Washington talks...", https://www.reuters.com/world/middle-east/israel-lebanon-agree-extend-ceasefire-by-45-days-us-state-dept-says-2026-05-15/) [Israel, Lebanon extend ceasefire by 45 days as Washington talks ...](https://www.reuters.com/world/middle-east/israel-lebanon-agree-extend-ceasefire-by-45-days-us-state-dept-says-2026-05-15/) and corroborated by AP, the Guardian, PBS, BBC, CNBC, ABC, and the Wikipedia article on the ceasefire, which states "On 15 May, the truce was extended for another 45 days" [2026 Israel–Lebanon ceasefire - Wikipedia](https://en.wikipedia.org/wiki/2026_Israel%E2%80%93Lebanon_ceasefire).

This May 15 extension occurred squarely within the resolution window (April 30 – June 1, 2026), is distinct from and later than the April 23 extension, comes from authoritative sources (U.S. Department of State and Reuters), and moves the cessation of hostilities approximately 45 days beyond the ~May 14 deadline. Additionally, the Wikipedia article notes that on June 1, Israel and Hezbollah agreed to a further ceasefire commitment [2026 Israel–Lebanon ceasefire - Wikipedia](https://en.wikipedia.org/wiki/2026_Israel%E2%80%93Lebanon_ceasefire), further confirming the cessation extended beyond mid-May.

All conditions for a YES resolution are met. The April 23 extension was correctly excluded as the basis.

Source URLs:
- https://www.reuters.com/world/middle-east/israel-lebanon-agree-extend-ceasefire-by-45-days-us-state-dept-says-2026-05-15/
- https://en.wikipedia.org/wiki/2026_Israel%E2%80%93Lebanon_ceasefire

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-145. `9431f1f9-5f66-58c3-9f36-4f3392530ca6`

- Present date: `2026-05-16 15:12:16.325475`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Assimi Goïta remain as President of the Transition and Head of State of Mali on July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, as of 23:59 UTC on July 1, 2026, Assimi Goïta officially holds the title of President of the Transition, Head of State of Mali (or an equivalent supreme executive title such as "President of Mali"). This includes scenarios where he retains the formal title but is on temporary leave, hospitalized, or experiencing a temporary incapacity — so long as no official replacement or successor has been formally announced or sworn in.

This question resolves **No** if, by 23:59 UTC on July 1, 2026, any of the following have occurred:
- Goïta has been formally removed from power (via coup, forced resignation, or other means)
- Goïta has voluntarily resigned
- Goïta has died
- Goïta has gone into exile and a successor has been announced
- Another individual has been formally declared or sworn in as head of state of Mali

If there is ambiguity (e.g., competing claims to power), resolution will follow the consensus assessment of at least two of the following major international news outlets: [Reuters](https://www.reuters.com/), [Al Jazeera](https://www.aljazeera.com/), [France 24](https://www.france24.com/), or [BBC News](https://www.bbc.com/news). Official communications from the Malian government, if available, may also be consulted via the [Journal Officiel de la République du Mali](http://www.sgg.gov.ml/).

**Pre-cutoff background**

Assimi Goïta is a Malian military officer who has ruled Mali since leading a coup in 2021. He currently holds the title of President of the Transition, Head of State of Mali. In July 2025, a law was promulgated extending his mandate until 2030, granting him a five-year presidential term renewable "as many times as necessary" without elections [https://www.aljazeera.com/news/2026/5/6/al-qaeda-linked-fighters-storm-mali-prison-block-food-supplies-to-bamako](https://www.aljazeera.com/news/2026/5/6/al-qaeda-linked-fighters-storm-mali-prison-block-food-supplies-to-bamako).

On April 25–26, 2026, fighters from the al-Qaeda-linked Jama'at Nusrat al-Islam wal-Muslimin (JNIM) and Tuareg separatists (Azawad Liberation Front) launched a coordinated offensive across Mali. They attacked military bases in multiple cities, took control of the northern city of Kidal, and killed Defence Minister Sadio Camara along with his family at their home in Kati, a garrison town near Bamako [https://www.aljazeera.com/news/2026/5/6/al-qaeda-linked-fighters-storm-mali-prison-block-food-supplies-to-bamako](https://www.aljazeera.com/news/2026/5/6/al-qaeda-linked-fighters-storm-mali-prison-block-food-supplies-to-bamako).

Following the attacks, JNIM fighters established checkpoints around the capital Bamako using motorbikes and heavy machine guns, blocking incoming and outgoing traffic including food trucks — creating a de facto siege of the capital that has disrupted supply chains and caused food shortages [https://www.aljazeera.com/news/2026/5/6/al-qaeda-linked-fighters-storm-mali-prison-block-food-supplies-to-bamako](https://www.aljazeera.com/news/2026/5/6/al-qaeda-linked-fighters-storm-mali-prison-block-food-supplies-to-bamako).

In response, the military government initiated a wave of arrests targeting former and current military officers, civil society members, lawyers, and political opposition figures. The military prosecutor claims to have "solid evidence" of complicity among certain military personnel. Goïta also assumed the role of Defence Minister following Camara's death [https://www.aljazeera.com/news/2026/5/6/al-qaeda-linked-fighters-storm-mali-prison-block-food-supplies-to-bamako](https://www.aljazeera.com/news/2026/5/6/al-qaeda-linked-fighters-storm-mali-prison-block-food-supplies-to-bamako).

The situation is widely described as an existential threat to the junta, with analysts questioning whether the military government can maintain control amid the siege and internal purges.

**Exact later resolution packet**

The question resolves YES: As of 23:59 UTC on July 1, 2026, Assimi Goïta still officially holds the title of President of the Transition, Head of State of Mali, with no official replacement or successor announced or sworn in.

Key evidence:
- Goïta remained head of state throughout the crisis. Al Jazeera's April 30, 2026 crisis explainer describes "Assimi Goita: Colonel Goita, 42, is the country's head of state." Reuters (April 28, 2026) reported "President Goita vows to neutralize insurgents" after his first public appearance following the April 25–26 attacks.
- On May 4, 2026, Goïta additionally assumed the role of Defence Minister following Sadio Camara's assassination, via a presidential decree that explicitly stated he would REMAIN president while also taking on the new role (Al Jazeera, May 4, 2026). This confirms he retained the supreme executive title.
- As of June 12, 2026, JNIM offered a ~$2.3 million (over €2 million) bounty for Goïta's capture. Reuters' June 12, 2026 report identifies him as "the leader of the government in the capital, Bamako," confirming he was still the sitting head of state and had not been removed, killed, or replaced [https://www.reuters.com/world/africa/malis-al-qaeda-branch-offers-2-million-bounty-presidents-capture-2026-06-12/](https://www.reuters.com/world/africa/malis-al-qaeda-branch-offers-2-million-bounty-presidents-capture-2026-06-12/). The OkayAfrica June 12, 2026 roundup likewise refers to him as the "transitional president" targeted by the bounty [Today in Africa, June 12, 2026: Mali junta bounty, Niger anti-LGBTQ ...](https://www.okayafrica.com/today-in-africa-june-12-2026-mali-militant-group-targets-junta-leaders-niger-criminalizes-same-sex-relationships/1432444).
- Wikipedia's Assimi Goïta article (last updated ~June 15, 2026) lists him as the incumbent President of Mali, with no indication of removal, resignation, death, or a successor [Assimi Goïta](https://en.wikipedia.org/wiki/Assimi_Go%C3%AFta).
- No source from Reuters, Al Jazeera, France 24, or BBC News reported any formal removal, forced resignation, death, exile-with-successor, or the swearing-in of another individual as head of state before the July 1, 2026 deadline.

Distinguishing de facto vs. de jure: The JNIM "total siege" of Bamako and the killing of the Defence Minister created a severe de facto security threat to the junta, but these events did NOT constitute a de jure formal removal or replacement of Goïta. The resolution criteria explicitly require a formal removal, resignation, death, or a formally declared/sworn-in successor for a NO resolution — none of which occurred. He retained the formal title continuously.

Consensus of required outlets: Reuters (June 12, 2026 bounty article referring to him as the sitting government leader) and Al Jazeera (April 30 identifying him as head of state; May 4 confirming he remains president) both confirm continued incumbency, satisfying the requirement of at least two major outlets.

Sources:
- Reuters (June 12, 2026): https://www.reuters.com/world/africa/malis-al-qaeda-branch-offers-2-million-bounty-presidents-capture-2026-06-12/ [https://www.reuters.com/world/africa/malis-al-qaeda-branch-offers-2-million-bounty-presidents-capture-2026-06-12/](https://www.reuters.com/world/africa/malis-al-qaeda-branch-offers-2-million-bounty-presidents-capture-2026-06-12/)
- OkayAfrica (June 12, 2026): https://www.okayafrica.com/today-in-africa-june-12-2026-mali-militant-group-targets-junta-leaders-niger-criminalizes-same-sex-relationships/1432444 [Today in Africa, June 12, 2026: Mali junta bounty, Niger anti-LGBTQ ...](https://www.okayafrica.com/today-in-africa-june-12-2026-mali-militant-group-targets-junta-leaders-niger-criminalizes-same-sex-relationships/1432444)
- Al Jazeera (May 4, 2026): https://www.aljazeera.com/news/2026/5/4/mali-leader-goita-takes-defence-post-after-minister-killed
- Al Jazeera (April 30, 2026): https://www.aljazeera.com/news/2026/4/30/mali-crisis-who-are-the-key-leaders-to-know-about
- Reuters (April 28, 2026): https://www.reuters.com/world/mali-military-leader-goita-meets-russian-ambassador-after-attacks-office-says-2026-04-28/
- Wikipedia (Assimi Goïta): https://en.wikipedia.org/wiki/Assimi_Go%C3%AFta [Assimi Goïta](https://en.wikipedia.org/wiki/Assimi_Go%C3%AFta)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-146. `588c398a-0e3f-58d7-9f95-13053a098007`

- Present date: `2026-05-14 10:32:01.231531`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Montenegro provisionally close at least one additional EU accession negotiating chapter between May 12, 2026 and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 (00:00 UTC) and on or before July 1, 2026 (23:59 UTC), the Council of the European Union officially announces the provisional closure of at least one additional EU accession negotiating chapter for Montenegro.

A chapter is considered "provisionally closed" when the EU Accession Conference with Montenegro formally agrees to close it, as documented by an official Council of the European Union press release. For background on what "provisionally closed" means in the EU accession process, see: https://www.consilium.europa.eu/en/policies/how-enlargement-works/

**Resolution source:** Official press releases published on the Council of the European Union website at https://www.consilium.europa.eu/en/press/press-releases/ — specifically, announcements of Accession Conference meetings with Montenegro. An example of such a press release is: https://www.consilium.europa.eu/en/press/press-releases/2026/03/17/eu-and-montenegro-provisionally-close-chapter-on-trans-european-networks-in-accession-negotiations/

Only chapters provisionally closed on or after May 12, 2026 (00:00 UTC) and on or before July 1, 2026 (23:59 UTC) count toward resolution. If no such closure is announced by July 1, 2026, the question resolves **No**.

**Pre-cutoff background**

Montenegro is the most advanced candidate in the EU enlargement process. As of May 12, 2026 (UTC), Montenegro has provisionally closed 14 of its 33 negotiating chapters, with 19 chapters remaining open [EU and Montenegro provisionally close chapter on Trans-European ...](https://www.consilium.europa.eu/en/press/press-releases/2026/03/17/eu-and-montenegro-provisionally-close-chapter-on-trans-european-networks-in-accession-negotiations/). The most recent closures were Chapter 32 (Financial Control) on January 26, 2026, and Chapter 21 (Trans-European Networks) on March 17, 2026 [EU and Montenegro provisionally close chapter on Trans-European ...](https://www.consilium.europa.eu/en/press/press-releases/2026/03/17/eu-and-montenegro-provisionally-close-chapter-on-trans-european-networks-in-accession-negotiations/). The pace of closures has accelerated in 2026, with two chapters closed in the first three months of the year.

Montenegro's government has set an ambitious goal to close all remaining 19 chapters by the end of 2026 [2026 will be a big year in the Western Balkans. Here's what to watch.](https://www.atlanticcouncil.org/blogs/2026-will-be-a-big-year-in-the-western-balkans-heres-what-to-watch/). In April 2026, the EU moved to begin drafting Montenegro's accession treaty, signaling strong political momentum. A major EU-Western Balkans Summit is scheduled for June 1, 2026, in Montenegro, which could serve as a catalyst for additional chapter closures [2026 will be a big year in the Western Balkans. Here's what to watch.](https://www.atlanticcouncil.org/blogs/2026-will-be-a-big-year-in-the-western-balkans-heres-what-to-watch/).

However, provisionally closing a chapter requires both technical alignment with EU law (the acquis communautaire) and unanimous approval from all EU member states, making the timing of any individual closure uncertain [2026 will be a big year in the Western Balkans. Here's what to watch.](https://www.atlanticcouncil.org/blogs/2026-will-be-a-big-year-in-the-western-balkans-heres-what-to-watch/). For further context on the 2026 Western Balkans outlook, see the Atlantic Council analysis: https://www.atlanticcouncil.org/blogs/2026-will-be-a-big-year-in-the-western-balkans-heres-what-to-watch/ [2026 will be a big year in the Western Balkans. Here's what to watch.](https://www.atlanticcouncil.org/blogs/2026-will-be-a-big-year-in-the-western-balkans-heres-what-to-watch/).

**Exact later resolution packet**

The question resolves YES.

The resolution criteria require that, between May 12, 2026 (00:00 UTC) and July 1, 2026 (23:59 UTC), the Council of the European Union officially announces the provisional closure of at least one additional EU accession negotiating chapter for Montenegro (beyond the 14 already closed as of May 12, 2026), documented by an official Council press release at consilium.europa.eu.

This condition was met. On June 15, 2026, the 27th meeting of the Accession Conference with Montenegro provisionally closed TWO chapters: Chapter 2 (freedom of movement for workers) and Chapter 28 (consumer and health protection) [04ccb4].

Key evidence from the official Council of the EU press release (https://www.consilium.europa.eu/en/press/press-releases/2026/06/15/eu-and-montenegro-close-accession-negotiations-on-freedom-of-movement-of-workers-and-consumer-and-health-protection/):
- "Today, the 27th meeting of the Accession Conference with Montenegro provisionally closed accession negotiations on chapters 2 (freedom of movement for workers) and 28 (consumer and health protection)." [04ccb4]
- "With the provisional closure agreed today, a total of sixteen of these chapters have now been provisionally closed." [04ccb4]

Confirming the checklist requirements:
1. Based on an official Council of the EU press release (consilium.europa.eu) — YES [04ccb4].
2. Announcement occurred June 15, 2026, within the window May 12 – July 1, 2026 — YES [04ccb4].
3. The chapters (2 and 28) are explicitly described as "provisionally closed," not merely opened — YES [04ccb4].
4. Direct URL to the specific press release provided above.
5. The closure represents additional chapters beyond the 14 closed as of May 12, 2026 — the total rose to 16, meaning 2 additional chapters were closed within the window — YES [04ccb4].

Therefore the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-147. `8d2b72f9-e52c-5ae6-84a5-d21bf5da49ce`

- Present date: `2026-05-16 03:47:41.771870`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-06-20T00:00:00`

**Question**

Will the LA County Sheriff primary on June 2, 2026, result in a November runoff?

**Resolution criteria**

This question resolves **Yes** if no candidate receives more than 50% of the total votes cast (i.e., a majority, defined as 50% plus at least one vote) in the June 2, 2026, primary election for Los Angeles County Sheriff, thereby triggering a runoff between the top two candidates in the November general election. It resolves **No** if any single candidate receives more than 50% of total votes cast, winning the election outright.

**Key definitions:**
- "Primary" refers to the June 2, 2026, Statewide Direct Primary Election as conducted in Los Angeles County under California's [top-two nonpartisan primary system](https://en.wikipedia.org/wiki/Nonpartisan_blanket_primary).
- "Majority" means more than 50% of all votes cast for the office of Sheriff, consistent with [California Constitution Article II](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CONS&sectionNum=SEC.%205.&article=II) and the [LA County Charter, Section 13](https://lacounty.gov/wp-content/uploads/2022/03/Charter2008_with_links_rev2016.pdf) [[PDF] CHARTER | LA County](https://lacounty.gov/wp-content/uploads/2022/03/Charter2008_with_links_rev2016.pdf).
- "Total votes cast" includes all valid ballots cast for the office, including write-in candidates. Overvotes, undervotes, and invalid ballots are excluded from the denominator.
- "Runoff" means the top-two general election on November 3, 2026.
- "Candidate" means any person whose name appears on the official ballot or who is a qualified write-in candidate for the office.

**Resolution source:** The official certified election results published by the Los Angeles County Registrar-Recorder/County Clerk at [https://results.lavote.gov/](https://results.lavote.gov/). Preliminary (election night) results may be used for initial assessment, but if they are contested or too close to call, resolution will wait for the official certification.

**Certification deadline:** If official certified results are not available by July 1, 2026, 11:59 PM Pacific Time (UTC-7), the question will resolve based on the most recent official results update posted at the above URL as of that deadline. If no results at all have been posted by that time (e.g., election postponed), the question resolves N/A.

**Timezone:** All dates and times reference Pacific Time (UTC-7) unless otherwise noted.

**Pre-cutoff background**

The Los Angeles County Sheriff oversees the largest sheriff's agency in the nation, with a budget of nearly $4 billion [Los Angeles County Sheriff: Who's running in the June 2 ... - LAist](https://laist.com/news/politics/voter-guides/2026-election-california-primary-los-angeles-county-sheriff). The incumbent, Robert Luna, was elected in 2022 and is seeking a second four-year term. He faces eight challengers in the June 2, 2026, nonpartisan primary: Mike Bornman, Karla Carranza, Brendan Corbett, Oscar Antonio Martinez, Eric Strong, Alex Villanueva (the previous sheriff whom Luna defeated in 2022), Brian E. Warren, and André N. White [Los Angeles County Sheriff: Who's running in the June 2 ... - LAist](https://laist.com/news/politics/voter-guides/2026-election-california-primary-los-angeles-county-sheriff) [Robert Luna - Ballotpedia](https://ballotpedia.org/Robert_Luna).

Under California's [nonpartisan top-two primary system](https://en.wikipedia.org/wiki/Nonpartisan_blanket_primary), all candidates appear on the same ballot regardless of party. A candidate must receive a majority of all votes cast (more than 50%) to win the office outright at the primary [[PDF] CHARTER | LA County](https://lacounty.gov/wp-content/uploads/2022/03/Charter2008_with_links_rev2016.pdf). If no candidate reaches this threshold, the top two vote-getters advance to a runoff in the November 3, 2026, general election [Los Angeles County Sheriff: Who's running in the June 2 ... - LAist](https://laist.com/news/politics/voter-guides/2026-election-california-primary-los-angeles-county-sheriff).

With nine candidates on the ballot, vote-splitting is a significant factor. The presence of Alex Villanueva—who has name recognition and a dedicated base from his 2018–2022 tenure—alongside seven other challengers could fragment the vote enough to prevent any candidate from crossing 50%. However, incumbents in county-level races often consolidate substantial support, and Luna could potentially win outright if the opposition vote is sufficiently divided among many weaker candidates while he retains strong support.

Official election results will be published by the Los Angeles County Registrar-Recorder/County Clerk at [results.lavote.gov](https://results.lavote.gov/).

**Exact later resolution packet**

The question resolves YES because no candidate received a majority (more than 50%) in the June 2, 2026, Los Angeles County Sheriff primary, triggering a November runoff.

Official results from the LA County Registrar-Recorder/County Clerk resolution source (https://results.lavote.gov/text-results/4338), last updated 06/26/2026, show the Sheriff contest as follows [LA County - Election Results Text Version](https://results.lavote.gov/text-results/4338):
- Robert G. Luna: 859,070 votes (44.15%) — top vote-getter
- Alex Villanueva: 422,272 votes (21.70%)
- Eric Strong: 291,045 votes (14.96%)
- Karla Carranza: 114,615 votes (5.89%)
- Oscar Antonio Martinez: 80,885 votes (4.16%)
- Mike Bornman: 76,919 votes (3.95%)
- André N. White: 76,162 votes (3.91%)
- Brendan Corbett: 24,618 votes (1.27%)

The top-performing candidate, incumbent Robert Luna, received only 44.15% of the vote — far below the 50%-plus-one-vote majority threshold required by the LA County Charter to win outright [LA County - Election Results Text Version](https://results.lavote.gov/text-results/4338). Note the official percentages published by results.lavote.gov are already computed using a denominator that excludes undervotes and overvotes but includes valid votes for the office (including any qualified write-ins), exactly as the resolution criteria require; these are the official reported percentages.

Because no candidate exceeded 50%, the top two vote-getters — Luna and Villanueva — advance to a runoff in the November 3, 2026 general election. This is corroborated by NBC Los Angeles ("Los Angeles County Sheriff Robert Luna is set to face Alex Villanueva, his predecessor, in the November runoff") and the Daily News ("Luna and Villanueva head to November run-off"), though the resolution is grounded in the official results.lavote.gov data.

Certification status: The official results page did not explicitly display a "Certified" label; the figures used are the most recent official update (06/26/2026) posted at the resolution URL as of the July 1, 2026 11:59 PM PT deadline, which is exactly what the resolution criteria specify to use if certified results are unavailable [LA County - Election Results Text Version](https://results.lavote.gov/text-results/4338). Regardless of certification, the outcome is unambiguous: Luna's 44.15% margin below 50% is far too large to be overturned by remaining/late ballots, so a runoff is definitively triggered. Question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-148. `94ab0498-db23-5cb5-814d-d44aee9379f1`

- Present date: `2026-05-16 15:32:47.055951`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Brazil's Senate CCJ approve PEC 14/2021 by July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if the Comissão de Constituição, Justiça e Cidadania (CCJ) of the Brazilian Senate formally approves PEC 14/2021 — defined as a majority of committee members present voting in favor of the rapporteur's report (parecer) on the proposal — on or after May 12, 2026, and no later than 23:59 Brasília time (UTC-3) on July 1, 2026.

This question resolves as **No** if:
- The CCJ has not voted on PEC 14/2021 by the deadline, OR
- The CCJ votes to reject the proposal, OR
- The proposal is withdrawn or otherwise removed from the CCJ's agenda before a vote occurs.

**Resolution source:** The official legislative tracking page for PEC 14/2021 on the Senado Federal website: https://www25.senado.leg.br/web/atividade/materias/-/materia/170850. The "Tramitação" section of this page records all official legislative actions, including committee votes and their outcomes.

**Pre-cutoff background**

PEC 14/2021 is a Proposed Amendment to the Brazilian Constitution (Proposta de Emenda à Constituição) that seeks to establish special retirement rights (aposentadoria diferenciada) for Community Health Agents (Agentes Comunitários de Saúde - ACS) and Endemic Disease Combat Agents (Agentes de Combate às Endemias - ACE), altering Articles 40, 198, and 201 of the Constitution [PEC 14/2021 - Senado Federal](https://www25.senado.leg.br/web/atividade/materias/-/materia/170850). The proposal was approved by the Chamber of Deputies (Câmara dos Deputados) in October 2025 and subsequently sent to the Senate, where Senate President Davi Alcolumbre announced it would be forwarded to the CCJ in March 2026 [Irajá busca consenso para a proposta de aposentadoria especial ...](https://www12.senado.leg.br/radio/1/conexao-senado/2026/04/15/iraja-busca-consenso-para-a-proposta-de-aposentadoria-especial-para-agentes-de-saude).

As of May 13, 2026, PEC 14/2021 has the status "Em tramitação" (in progress) within the Senate's Comissão de Constituição, Justiça e Cidadania (CCJ). Senator Irajá (PSD-TO) was designated as rapporteur on March 17, 2026. The most recent recorded legislative action was on April 8, 2026, involving the receipt of a request to withdraw Amendment 1 [PEC 14/2021 - Senado Federal](https://www25.senado.leg.br/web/atividade/materias/-/materia/170850).

The proposal is highly contentious due to its fiscal impact. The Ministry of Social Security (Ministério da Previdência) estimates it would increase the pension deficit by R$ 29.31 billion over ten years, with R$ 18.46 billion impacting municipal pension systems and R$ 10.85 billion impacting the federal government. The federal government (including the Ministry of Finance, which has indicated it would recommend a full presidential veto if the PEC passes) and municipal governments are actively lobbying against the proposal [Governo federal e prefeituras tentam frear avanço da PEC ... - Globo](https://extra.globo.com/economia/servidor-publico/noticia/2026/04/governo-federal-e-prefeituras-tentam-frear-avanco-da-pec-da-aposentadoria-especial-de-agentes-de-saude-no-congresso.ghtml). On the other side, rapporteur Senator Irajá has publicly stated his intention to present a favorable report (parecer favorável), arguing the measure corrects a historical injustice, and is seeking to build a consensus text with stakeholders [Governo federal e prefeituras tentam frear avanço da PEC ... - Globo](https://extra.globo.com/economia/servidor-publico/noticia/2026/04/governo-federal-e-prefeituras-tentam-frear-avanco-da-pec-da-aposentadoria-especial-de-agentes-de-saude-no-congresso.ghtml) [Irajá busca consenso para a proposta de aposentadoria especial ...](https://www12.senado.leg.br/radio/1/conexao-senado/2026/04/15/iraja-busca-consenso-para-a-proposta-de-aposentadoria-especial-para-agentes-de-saude).

For context, the CCJ is the first committee stage for constitutional amendments in the Brazilian Senate. Its role is to assess the constitutionality, legality, and legislative merit of proposals. A favorable vote (parecer) by the CCJ is required before a PEC can proceed to a floor vote. More information on the CCJ's role is available at: https://www.senado.leg.br/atividade/comissoes/comissao.asp?com=34

**Exact later resolution packet**

The question resolves YES.

The resolution criteria required that the CCJ (Comissão de Constituição, Justiça e Cidadania) of the Brazilian Senate formally approve PEC 14/2021 — defined as a majority of committee members present voting in favor of the rapporteur's (parecer) report — on or after May 12, 2026 and no later than 23:59 Brasília time on July 1, 2026.

Evidence from the designated resolution source (the official Senado Federal legislative tracking page for PEC 14/2021, https://www25.senado.leg.br/web/atividade/materias/-/materia/170850): The "Tramitação" section records that on June 10, 2026, during the CCJ's 9th Extraordinary Meeting, the committee approved the rapporteur's report by Senator Irajá (favorable to the proposal, contrary to Amendment 2), which became the CCJ's formal opinion. It also approved Requerimento 26/2026 for a special calendar (urgency). The rapporteur's report had been formally received/presented on May 21, 2026, and the matter was placed on the meeting agenda on June 3, 2026 [PEC 14/2021 - Senado Federal](https://www25.senado.leg.br/web/atividade/materias/-/materia/170850).

This is corroborated by Agência Brasil, which reported on June 11, 2026 that on Wednesday, June 10, 2026, the CCJ voted in favor of the rapporteur's report presented by Senator Irajá (PSD-TO) supporting special retirement for community health agents and endemic-disease combat agents [CCJ do Senado aprova aposentadoria especial para agentes de ...](https://agenciabrasil.ebc.com.br/politica/noticia/2026-06/ccj-do-senado-aprova-aposentadoria-especial-para-agentes-de-saude). Numerous other outlets (Congresso em Foco, Poder360, TV Senado) reported the same CCJ approval on that date.

Checklist confirmation:
- The approval occurred in the CCJ specifically (not just the floor or another committee) [PEC 14/2021 - Senado Federal](https://www25.senado.leg.br/web/atividade/materias/-/materia/170850) [CCJ do Senado aprova aposentadoria especial para agentes de ...](https://agenciabrasil.ebc.com.br/politica/noticia/2026-06/ccj-do-senado-aprova-aposentadoria-especial-para-agentes-de-saude).
- The approval date, June 10, 2026, falls strictly within the window May 12, 2026 – July 1, 2026 [PEC 14/2021 - Senado Federal](https://www25.senado.leg.br/web/atividade/materias/-/materia/170850).
- The vote was a formal majority approval of the rapporteur's favorable parecer [PEC 14/2021 - Senado Federal](https://www25.senado.leg.br/web/atividade/materias/-/materia/170850) [CCJ do Senado aprova aposentadoria especial para agentes de ...](https://agenciabrasil.ebc.com.br/politica/noticia/2026-06/ccj-do-senado-aprova-aposentadoria-especial-para-agentes-de-saude).
- The proposal was NOT withdrawn or removed from the agenda before a vote; on the contrary, after CCJ approval it advanced (placed on the Plenary Order of the Day on June 26, 2026, with the first Plenary discussion session on June 30, 2026) [PEC 14/2021 - Senado Federal](https://www25.senado.leg.br/web/atividade/materias/-/materia/170850).

Therefore all conditions for a YES resolution are met.

Resolution source URL used: https://www25.senado.leg.br/web/atividade/materias/-/materia/170850 (Tramitação section), corroborated by https://agenciabrasil.ebc.com.br/politica/noticia/2026-06/ccj-do-senado-aprova-aposentadoria-especial-para-agentes-de-saude.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-149. `f7aa0547-d69b-52f2-afba-e395d888d6be`

- Present date: `2026-05-29 07:10:52.952181`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will LIRR workers go on strike, halting service for at least one full calendar day, between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 (Eastern Time) and before July 1, 2026, 11:59 PM ET, LIRR workers engage in a **strike** (defined as a work stoppage by employees to enforce demands, per [Wikipedia: Strike action](https://en.wikipedia.org/wiki/Strike_action)) that results in a **halt of service** (defined as the suspension or cessation of regular operations, per [Merriam-Webster: halt](https://www.merriam-webster.com/dictionary/halt)) across the LIRR network for at least one **full calendar day** — meaning that no scheduled LIRR train service operates for an entire calendar day (midnight 12:00 AM ET to 11:59 PM ET) on at least one date.

This question resolves **No** if no such strike-caused full-day service halt occurs by July 1, 2026, 11:59 PM ET.

**Resolution source:** Official MTA service alerts at https://www.mta.info/article/lirr-strike-may-2026 or the MTA homepage at https://new.mta.info/, supplemented by credible reporting from major news outlets such as [Newsday](https://www.newsday.com/), [NY Times](https://www.nytimes.com/), [CBS New York](https://www.cbsnews.com/newyork/), or [AP News](https://apnews.com/).

Note: A partial service reduction, management-operated trains, or a strike lasting only a few hours within a single calendar day does not qualify. The halt must be due to a strike by LIRR workers, not other causes (e.g., weather, infrastructure failure).

**Pre-cutoff background**

The Long Island Rail Road (LIRR), the busiest commuter railroad in North America with nearly 300,000 daily riders, faces a potential strike amid a contract dispute between its labor unions and the Metropolitan Transportation Authority (MTA).

The parties agreed on the first three years of a four-year contract but remain deadlocked on the final year (beginning June 2026). The unions demand a 5% wage increase, while the MTA has offered 3%, with a potential increase to 4.5% contingent on work-rule concessions [Are LIRR workers going on strike? What commuters need to know](https://www.usatoday.com/story/news/2026/05/11/what-happens-if-lirr-workers-go-on-strike-when-it-could-happen/90029219007/) [LIRR strike looms as negotiations continue between union and MTA](https://www.cbsnews.com/newyork/news/lirr-strike-2026-update-negotiations-mta/). Two Presidential Emergency Boards have been convened and sided closer to the unions' position. After multiple cooling-off periods, unions are legally permitted to strike beginning at 12:01 AM ET on May 16, 2026.

As of May 13, 2026, negotiations are ongoing but no deal has been reached. As of May 11, talks resumed after unions rejected the MTA's latest offer, calling it "phony," while the MTA claimed the sides were getting "closer" to a deal [LIRR strike looms as negotiations continue between union and MTA](https://www.cbsnews.com/newyork/news/lirr-strike-2026-update-negotiations-mta/). The MTA has prepared contingency plans including shuttle bus services to subway stations in Queens in the event of a shutdown [LIRR strike looms as negotiations continue between union and MTA](https://www.cbsnews.com/newyork/news/lirr-strike-2026-update-negotiations-mta/). Governor Hochul is involved, adding political pressure. The LIRR has not experienced a strike in over 30 years (the last was in 1994), but the current impasse is considered severe. Last-minute deals are common in rail labor disputes, making the outcome genuinely uncertain.

**Exact later resolution packet**

The question resolves YES. All resolution criteria are satisfied:

1. **A strike (labor work stoppage) occurred within the window.** The LIRR unions went on strike beginning at 12:01 a.m. ET on Saturday, May 16, 2026 [Long Island Rail Road resumes operations as deal reached to end ...](https://apnews.com/article/long-island-rail-road-strike-new-york-4d8d59478a543553606d8095114abb5d). This is a strike/work stoppage by employees (not weather or infrastructure failure). Multiple major outlets confirm it (AP News, NY Times "Long Island Rail Road Strike Ends as Deal Is Reached," CNN "Deal reached to end LIRR strike," CBS New York). The official MTA resolution page describes it as service being "suspended due to a labor action" [LIRR service has resumed - MTA](https://www.mta.info/article/lirr-strike-may-2026). This falls within the required window of on/after May 12, 2026 and before July 1, 2026, 11:59 PM ET.

2. **Service was halted across the entire LIRR network for at least one full calendar day.** Per AP News, the strike caused a complete halt of service across the LIRR network for three full calendar days — Saturday May 16, Sunday May 17, and Monday May 18, 2026 — with service not resuming until noon Tuesday, May 19, 2026 [Long Island Rail Road resumes operations as deal reached to end ...](https://apnews.com/article/long-island-rail-road-strike-new-york-4d8d59478a543553606d8095114abb5d). The MTA's official page confirms service was suspended and that the MTA Board approved refunds for "the four days that service was suspended due to a labor action" [LIRR service has resumed - MTA](https://www.mta.info/article/lirr-strike-may-2026). Either accounting confirms multiple entire calendar days (May 17 and May 18 unambiguously running midnight-to-midnight) during which no scheduled LIRR trains operated.

3. **Full-day, network-wide cessation confirmed.** Because service ran nowhere on the LIRR system for the entirety of at least May 17 and May 18, 2026, the requirement of "no scheduled LIRR train service for an entire calendar day (12:00 AM ET to 11:59 PM ET) on at least one date" is met — this was not merely a partial reduction, management-operated service, or a few-hours stoppage.

The strike ended when the MTA and the five LIRR unions reached a tentative deal on the evening of Monday, May 18, 2026, and service resumed Tuesday May 19 at noon [Long Island Rail Road resumes operations as deal reached to end ...](https://apnews.com/article/long-island-rail-road-strike-new-york-4d8d59478a543553606d8095114abb5d) [LIRR service has resumed - MTA](https://www.mta.info/article/lirr-strike-may-2026).

Sources: MTA official page https://www.mta.info/article/lirr-strike-may-2026 [LIRR service has resumed - MTA](https://www.mta.info/article/lirr-strike-may-2026); AP News https://apnews.com/article/long-island-rail-road-strike-new-york-4d8d59478a543553606d8095114abb5d [Long Island Rail Road resumes operations as deal reached to end ...](https://apnews.com/article/long-island-rail-road-strike-new-york-4d8d59478a543553606d8095114abb5d); corroborated by NY Times, CNN, CBS New York, and NBC New York reporting found via search.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-150. `7b077b07-ffe3-5893-9b8a-c42e6a352f6e`

- Present date: `2026-05-16 10:10:44.358058`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will any Republican Senator vote against final passage of the Senate immigration enforcement reconciliation bill by July 1, 2026?

**Resolution criteria**

This question resolves YES if at least one U.S. Senator who is a member of the Republican Party caucus at the time of the vote casts a "Nay" vote on final passage of the immigration enforcement reconciliation bill on the Senate floor. The vote must occur on or after May 12, 2026 (00:00 UTC) and on or before July 1, 2026 (23:59 UTC).

Key definitions:
- "Republican Senator": A Senator who is a member of the Senate Republican Conference (caucus) at the time of the vote. This includes any independents caucusing with Republicans, if applicable. See https://en.wikipedia.org/wiki/Senate_Republican_Conference for reference.
- "Vote against": A recorded "Nay" vote on the roll call for final passage. Abstentions, absences, or "Present" votes do not count as voting against.
- "Final passage": The roll call vote on passage of the reconciliation bill itself (not procedural motions, cloture votes, or amendments). This corresponds to a vote described as "On Passage of the Bill" or equivalent in Senate records.
- "Immigration enforcement reconciliation bill": The reconciliation legislation pursuant to S.Con.Res.33 (119th Congress), the FY2026 budget resolution focused on immigration enforcement funding. See https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/33

Resolution source: The official Senate roll call vote page on senate.gov (https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_119_2.htm) or the corresponding congress.gov page for the bill.

If no such final passage vote occurs on the Senate floor between May 12, 2026 (00:00 UTC) and July 1, 2026 (23:59 UTC), this question resolves NO.

**Pre-cutoff background**

In April 2026, Senate Republicans adopted a budget resolution (S.Con.Res.33) by a 50-48 vote, with Republican Senators Lisa Murkowski and Rand Paul breaking ranks to vote against it. The current Senate is composed of 53 Republicans and 47 Democrats (including independents who caucus with Democrats). Republicans can lose up to 3 votes on reconciliation and still pass legislation with Vice President Vance's tiebreaking vote.

The budget resolution set up a reconciliation process for an immigration enforcement bill with an estimated cost of approximately $70-72 billion, funding ICE and Customs and Border Protection operations. Senate committees are drafting the reconciliation bill text, which has generated intra-party controversy.

A key flashpoint is the inclusion of approximately $1 billion in funding for White House security construction, widely characterized as funding for a "Trump ballroom." Multiple Republican senators have publicly expressed discomfort with this provision, with some calling for more details. Democrats have seized on the issue, and Republican senators are split on whether the funding should remain in the final bill. Senators who voted against the budget resolution (Murkowski and Paul) or who have raised concerns about the ballroom provision are potential "no" votes on final passage.

The reconciliation bill is expected to reach a Senate floor vote in May or June 2026, though the exact timeline remains fluid as committees finalize their portions.

**Exact later resolution packet**

The question resolves YES.

Antecedent/consequent check: This is not a conditional question. The event required is (a) a Senate floor final-passage vote on the immigration enforcement reconciliation bill pursuant to S.Con.Res.33, occurring between May 12, 2026 and July 1, 2026, and (b) at least one Republican-caucus Senator casting a "Nay" vote on that final passage.

Evidence:
- The Senate voted on final passage of S. 2 — "An original bill to provide for reconciliation pursuant to title II of S. Con. Res. 33" — on June 5, 2026. This was Roll Call Vote No. 163 of the 119th Congress, 2nd Session, and the bill passed 52–47. This is confirmed from the official Senate roll call vote menu [Roll Call Votes 119th Congress - 2nd Session (2026) - U.S. Senate](https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_119_2.htm), with the official vote page at https://www.senate.gov/legislative/LIS/roll_call_votes/vote1192/vote_119_2_00163.htm. The vote date (June 5, 2026) falls squarely inside the required window (May 12 – July 1, 2026).
- The official roll call record shows Senator Lisa Murkowski (R-AK) cast a "Nay" vote on final passage; all other Nay votes were cast by Democrats/Independents, and Senator Bennet (D-CO) was the only Senator not voting [https://www.senate.gov/legislative/LIS/roll_call_votes/vote1192/vote_119_2_00163.htm](https://www.senate.gov/legislative/LIS/roll_call_votes/vote1192/vote_119_2_00163.htm). The arithmetic is internally consistent: 53 Republicans − 1 (Murkowski Nay) = 52 Republican Yeas = the 52 Yea total; the 47 Nays comprise Murkowski plus 46 Democrats, with Bennet (D) not voting.
- This is corroborated by multiple news outlets reporting on the same vote (E&E News: "Senators voted 52-47 on the bill... Sen. Lisa Murkowski of Alaska was the only Republican to [vote no]"; Juneau Independent: "Murkowski only GOP 'no' vote as Senate OKs $70B for immigration enforcement"; a poll-tracker post: "Senator Lisa Murkowski was the lone Republican who voted against. No Senate Democrats voted in favor").

Since Murkowski is a member of the Senate Republican Conference and cast a recorded "Nay" (not "Present," abstention, or absence) on the final passage roll call of the S.Con.Res.33 reconciliation bill within the specified window, the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-151. `235b42ef-20c9-5e86-84da-07d3b35f5606`

- Present date: `2026-05-12 16:04:20.063958`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the European Parliament and Council reach a trilogue agreement on the safeguard mechanism for the EU-US trade deal by June 15, 2026?

**Resolution criteria**

This question resolves YES if, by 23:59 UTC on June 15, 2026, there is an official announcement confirming that a trilogue agreement has been reached on the safeguard mechanism provisions of the EU-US trade deal implementing legislation.

A "trilogue" is a three-way negotiation between the European Parliament, the Council of the EU, and the European Commission used to reach agreement on EU legislation (see: https://www.europarl.europa.eu/topics/en/article/20140224STO36422/ordinary-legislative-procedure).

A "safeguard mechanism" refers to the legislative provisions allowing the EU to suspend, review, or terminate the trade deal under specified conditions, including the sunrise clause, sunset clause, and suspension triggers as debated in the current trilogue process.

The agreement must be reached on or after May 10, 2026, to exclude prior developments. The agreement must be confirmed via an official press release or communiqué from the European Parliament (https://www.europarl.europa.eu/news/en), the Council of the EU (https://www.consilium.europa.eu/en/press/), or credible reporting from Reuters, POLITICO, or Bloomberg citing official sources.

If no such agreement is reached by 23:59 UTC on June 15, 2026, or if negotiations are formally abandoned, this question resolves NO.

**Pre-cutoff background**

Following the EU-US trade deal agreed at Turnberry in July 2025, the EU has been working to pass implementing legislation through a trilogue process involving the European Parliament, the Council of the EU, and the European Commission. The deal involves the EU scrapping duties on U.S. industrial goods while the U.S. maintains a 15% duty on most European exports [EU agreement on US trade deal within reach, says top lawmaker](https://www.politico.eu/article/eu-us-agreement-trade-deal-within-reach-top-lawmaker/).

As of May 11, 2026, negotiations remain stalled over the "safeguard mechanism" — provisions that would allow the EU to suspend or terminate the deal under certain conditions. Key sticking points include [EU negotiators fail to agree on US trade deal - POLITICO](https://www.politico.eu/article/eu-negotiators-fail-to-agree-on-us-trade-deal/) [EU agreement on US trade deal within reach, says top lawmaker](https://www.politico.eu/article/eu-us-agreement-trade-deal-within-reach-top-lawmaker/):

- A "sunrise clause" making the deal conditional on the U.S. reducing steel and aluminum tariffs to 15%.
- A "sunset clause" — the Parliament wants the deal to expire by March 31, 2028, while the Commission and member states prefer a longer duration.
- Provisions to suspend the deal if the U.S. threatens EU territorial integrity (linked to concerns about Greenland).

The most recent trilogue on May 6-7, 2026, lasted approximately six hours but ended without a breakthrough, though officials described progress and convergence [EU negotiators fail to agree on US trade deal - POLITICO](https://www.politico.eu/article/eu-negotiators-fail-to-agree-on-us-trade-deal/). U.S. President Trump has set a July 4, 2026 deadline for the deal and threatened 25% tariffs on European automobiles. The next trilogue round is expected around May 12 or May 19, 2026 [EU agreement on US trade deal within reach, says top lawmaker](https://www.politico.eu/article/eu-us-agreement-trade-deal-within-reach-top-lawmaker/). Senior lawmaker Bernd Lange has indicated that a conclusion is expected at the next negotiating round [EU agreement on US trade deal within reach, says top lawmaker](https://www.politico.eu/article/eu-us-agreement-trade-deal-within-reach-top-lawmaker/).

**Exact later resolution packet**

The question resolves YES. On Wednesday, 20 May 2026 — within the resolution window (on/after 10 May 2026 and before 23:59 UTC 15 June 2026) — the EU institutions reached a trilogue/provisional agreement on the implementing legislation for the EU-US trade deal, explicitly covering the safeguard mechanism provisions (sunset clause, suspension triggers, steel/aluminium conditions).

Evidence:

1. Council of the EU official press release, "EU-US trade: Council and Parliament strike a deal to implement the tariff elements of the Joint Statement," dated 20 May 2026 (https://www.consilium.europa.eu/en/press/press-releases/2026/05/20/eu-us-trade-council-and-parliament-strike-a-deal-to-implement-the-tariff-elements-of-the-joint-statement/). It states the co-legislators "agreed to strengthen the main regulation by setting up a robust safeguard mechanism, reinforcing the suspension clause provisions and introducing a sunset clause," and describes the Commission's role in launching examinations of injury to EU producers [400ab2].

2. European Parliament official press release, "Agreement reached to put EU-US trade on a more stable footing" (https://www.europarl.europa.eu/news/en/press-room/20260518IPR43407/agreement-reached-to-put-eu-us-trade-on-a-more-stable-footing), dated 20 May 2026: "On Wednesday morning, Parliament and Council reached a provisional agreement on two pieces of legislation implementing EU tariff commitments under the August 2025 EU-US Joint Statement." It confirms the safeguard mechanism, a sunset clause (main regulation expires 31 December 2029), and a strengthened suspension clause allowing the Commission to suspend tariff preferences if by 31 December 2026 the US still applies >15% tariffs on EU steel and aluminium derivatives [5d4845, 0ce376].

3. POLITICO reporting, "EU strikes deal on Trump trade pact" (https://www.politico.eu/article/eu-strikes-deal-implement-us-trump-trade-pact-negotiations-compromise/), dated 20 May 2026, explicitly confirms the trilogue character citing official sources/negotiators and the final text seen by POLITICO: "Negotiators from the European Parliament, the Council of the EU and the European Commission reached a compromise after more than five hours of talks..." including the suspension trigger (Commission could suspend the deal if the US doesn't reduce steel/aluminium duties by end of 2026), the sunset clause (agreement expires December 2029), and safeguard investigation provisions [3fb7f7].

All checklist conditions are satisfied: (a) announcement dated 20 May 2026, within window; (b) covers the safeguard mechanism including sunset clause and suspension triggers; (c) evidence from official europarl.europa.eu and consilium.europa.eu sites plus POLITICO citing official sources; (d) confirmed as a trilogue agreement involving the European Parliament, the Council of the EU, and the European Commission (per POLITICO). Later steps (EP plenary final approval 11–16 June 2026 and Council final approval 25 June 2026) further corroborate the agreement was reached.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-152. `0a155bf9-e0a5-5195-b472-606fb0da06e2`

- Present date: `2026-05-03 10:10:44.785112`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Assimi Goïta remain the recognized head of state of Mali as of June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, at 23:59 UTC on June 1, 2026, Assimi Goïta is the recognized head of state of Mali (see: https://en.wikipedia.org/wiki/Head_of_state). "Recognized head of state" means he satisfies at least one of the following indicators:

1. He is listed as Mali's head of state by the United Nations (https://protocol.un.org/dgacm/pls/site.nsf/files/heads/$FILE/hsog.pdf) or the African Union (https://au.int/en/member_states); OR
2. At least two of the following major international news sources — Reuters (https://www.reuters.com), AP News (https://apnews.com), BBC (https://www.bbc.com/news), Al Jazeera (https://www.aljazeera.com) — describe him as Mali's president, head of state, or leader in their most recent reporting as of June 1, 2026.

The question resolves **No** if, on or after May 1, 2026:
- Goïta dies, resigns, is formally removed from office, or is replaced by another individual recognized as head of state by the sources above; OR
- A new governing authority is established that does not include Goïta as head of state.

**Important clarification on diminished powers:** If Goïta is alive but has been effectively stripped of powers — for example, placed under house arrest, reduced to a figurehead role, or sidelined by another junta member who exercises de facto authority — the question still resolves **Yes** as long as he retains the formal title and is recognized as head of state by the sources listed above. The question resolves **No** only if he loses formal recognition as head of state per those sources.

The evaluation period begins on May 1, 2026. Events prior to this date (e.g., earlier coup attempts or leadership changes) do not count for resolution purposes.

**Resolution sources:** The question will be resolved by checking the following live sources on or shortly after June 1, 2026:
- Reuters: https://www.reuters.com/world/africa/
- UN Heads of State list: https://protocol.un.org/dgacm/pls/site.nsf/files/heads/$FILE/hsog.pdf
- African Union member states page: https://au.int/en/member_states
- Al Jazeera Africa: https://www.aljazeera.com/where/mali/
- BBC News: https://www.bbc.com/news/topics/c77jz3mdq4lt

**Pre-cutoff background**

Assimi Goïta (born 1983) is a Malian military officer who seized power in a 2021 coup and has ruled Mali since. In July 2025, a bill granting him a five-year presidential term was signed into law, consolidating his position as President of Mali.

On April 25–26, 2026, coordinated attacks were launched by a coalition of separatist forces and al-Qaida-linked jihadists (Jama'at Nusrat al-Islam wal-Muslimin, JNIM). These forces seized the desert town of Kidal and launched an attack near the capital, Bamako [https://www.theguardian.com/world/2026/apr/28/russia-claims-its-africa-corps-group-prevented-coup-in-mali-after-rebels-seize-towns](https://www.theguardian.com/world/2026/apr/28/russia-claims-its-africa-corps-group-prevented-coup-in-mali-after-rebels-seize-towns). Defense Minister Sadio Camara was killed in a suicide bombing during the attacks [https://www.theguardian.com/world/2026/apr/28/russia-claims-its-africa-corps-group-prevented-coup-in-mali-after-rebels-seize-towns](https://www.theguardian.com/world/2026/apr/28/russia-claims-its-africa-corps-group-prevented-coup-in-mali-after-rebels-seize-towns). Reports emerged of fracturing within the ruling junta and questions about the loyalty of Russia's Africa Corps, which had been supporting the regime [https://www.theguardian.com/world/2026/apr/28/russia-claims-its-africa-corps-group-prevented-coup-in-mali-after-rebels-seize-towns](https://www.theguardian.com/world/2026/apr/28/russia-claims-its-africa-corps-group-prevented-coup-in-mali-after-rebels-seize-towns).

Goïta was not seen publicly between the onset of the attacks on April 25 and April 28, 2026, when the Malian presidency posted a photo showing him meeting with the Russian ambassador and he delivered a televised address to the nation declaring the situation "under control" [https://www.theguardian.com/world/2026/apr/28/russia-claims-its-africa-corps-group-prevented-coup-in-mali-after-rebels-seize-towns](https://www.theguardian.com/world/2026/apr/28/russia-claims-its-africa-corps-group-prevented-coup-in-mali-after-rebels-seize-towns). As of May 1, 2026, this April 28 televised address and meeting constitute Goïta's last verified public appearance.

The situation remains highly uncertain due to rebel momentum, reported junta fractures, the loss of a key defense minister, and questions about the reliability of Russian military support. Russia has claimed its Africa Corps prevented a coup, but independent verification is lacking [https://www.theguardian.com/world/2026/apr/28/russia-claims-its-africa-corps-group-prevented-coup-in-mali-after-rebels-seize-towns](https://www.theguardian.com/world/2026/apr/28/russia-claims-its-africa-corps-group-prevented-coup-in-mali-after-rebels-seize-towns).

**Exact later resolution packet**

The question resolves YES: Assimi Goïta remained the recognized head of state (President) of Mali as of 23:59 UTC on June 1, 2026.

Evidence:
- The Wikipedia article on Assimi Goïta (last edited May 18, 2026) lists him as the incumbent 6th President of Mali, and notes that on May 4, 2026 he appointed himself defense minister (replacing the killed Sadio Camara). There is no indication he died, resigned, or was removed [Assimi Goïta - Wikipedia](https://en.wikipedia.org/wiki/Assimi_Go%C3%AFta).
- Foreign Policy (dated May 20, 2026) explicitly states there had been no counter-coup or toppling of the junta, and continues to identify Goïta as Mali's military leader; the article refers to "Mali's junta-led government" [Mali Strikes Rebel-Held Kidal as Insurgency Worsens - Foreign Policy](https://foreignpolicy.com/2026/05/20/mali-rebels-kidal-fla-jnim-sahel-violence/).
- Multiple of the question's designated news sources continued to describe him as Mali's president/leader well into late May 2026:
  - Reuters (May 4, 2026): "Mali leader Goita assumes role of defence minister after attacks." Reuters consistently calls him "the leader of Mali's military government."
  - Al Jazeera (May 4, 2026): "Mali leader Goita takes defence post after minister killed," noting his five-year presidential mandate.
  - BBC reporting through May 2026 (e.g., May 21, 2026) continued treating him as the junta leader/president.
  - An Instagram post dated May 31, 2026 (the day before the resolution timestamp) refers to him as "Mali's interim president, Assimi Goïta," announcing he will also serve as defence minister.

This satisfies indicator #2 of the resolution criteria (at least two of Reuters, AP, BBC, Al Jazeera describing him as Mali's president/head of state/leader in their most recent reporting as of June 1, 2026). Under the "diminished powers" clause, even if his authority was challenged by the insurgency, he retained the formal title and recognition as head of state, which resolves YES. No event (death, resignation, formal removal, replacement) on or after May 1, 2026 was found that would trigger a NO resolution.

Sources:
- https://en.wikipedia.org/wiki/Assimi_Go%C3%AFta
- https://foreignpolicy.com/2026/05/20/mali-rebels-kidal-fla-jnim-sahel-violence/
- https://www.reuters.com/world/mali-leader-goita-assumes-role-defence-minister-after-attacks-state-media-says-2026-05-04/
- https://www.aljazeera.com/news/2026/5/4/mali-leader-goita-takes-defence-post-after-minister-killed
- https://www.bbc.com/news/articles/cy818zdv831o

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-153. `c8fd01f6-552b-536b-9826-c89d6abe749f`

- Present date: `2026-05-29 02:25:23.609098`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Bundesverwaltungsgericht fully dismiss the City of Marktredwitz's lawsuit against the Planfeststellungsbeschluss for SuedOstLink section C2 (case 9 A 1.26) if a judgment is issued by July 1, 2026?

**Resolution criteria**

This question resolves based on an official judgment or decision published or announced by the Bundesverwaltungsgericht (BVerwG) in case **9 A 1.26** between May 12, 2026, 00:00 CEST and July 1, 2026, 23:59 CEST (inclusive).

**Resolution as YES**: The question resolves YES if the BVerwG issues a judgment that dismisses the lawsuit in its entirety (Klage wird abgewiesen), upholding the Planfeststellungsbeschluss without modification.

**Resolution as NO**: The question resolves NO if any of the following occur:
1. The BVerwG fully annuls (aufhebt) the Planfeststellungsbeschluss.
2. The BVerwG partially annuls the Planfeststellungsbeschluss.
3. The BVerwG declares the Planfeststellungsbeschluss unlawful but not void (rechtswidrig und nicht vollziehbar) and orders a supplementary procedure (planergänzendes Verfahren) or remedial action (Heilung von Mängeln) to cure identified defects — even if the plan itself is not fully annulled.
4. No judgment in case 9 A 1.26 is published or announced by the BVerwG between May 12, 2026, 00:00 CEST and July 1, 2026, 23:59 CEST.

**Definition of "uphold in full" / "dismiss all claims"**: For the purpose of this question, the court is considered to have "upheld in full" or "dismissed all claims" ONLY if the operative part (Tenor) of the judgment contains no order for annulment, supplementary procedure (planergänzendes Verfahren), remedial action (Heilung von Mängeln), or any other modification to the Planfeststellungsbeschluss. A judgment that identifies defects but orders a supplementary procedure rather than full annulment does NOT count as "upholding in full" and resolves as NO.

**Resolution source**: The official BVerwG decision database (https://www.bverwg.de/suche) or BVerwG press release page (https://www.bverwg.de/pm).

**Pre-cutoff background**

The SuedOstLink is a major high-voltage direct current (HVDC) transmission line project connecting northeastern Germany to Bavaria. On February 13, 2025, the Bundesnetzagentur issued the Planfeststellungsbeschluss (planning approval decision) for section C2 (Marktredwitz to Pfreimd), approximately 90 km in length [Klagebegründung gegen den Planfeststellungsabschnitt C 2 des ...](https://www.baumann-rechtsanwaelte.de/2025/06/24/klagebegruendung-gegen-den-planfeststellungsabschnitt-c-2-des-suedostlink-eingereicht/).

The City of Marktredwitz filed a lawsuit (Anfechtungsklage) against this decision, with the Klagebegründung (statement of grounds) submitted on June 23, 2025 [Klagebegründung gegen den Planfeststellungsabschnitt C 2 des ...](https://www.baumann-rechtsanwaelte.de/2025/06/24/klagebegruendung-gegen-den-planfeststellungsabschnitt-c-2-des-suedostlink-eingereicht/). The case is registered at the Bundesverwaltungsgericht (BVerwG) under case number **9 A 1.26** [BVerwG 9 VR 10.26, Beschluss vom 29. April 2026](https://www.bverwg.de/290426B9VR10.26.0). The oral hearing (mündliche Verhandlung) is scheduled for **June 24, 2026** [BVerwG 9 VR 10.26, Beschluss vom 29. April 2026](https://www.bverwg.de/290426B9VR10.26.0).

Key legal arguments raised by Marktredwitz include:
- **Drinking water risks**: The proposed cable route passes within approximately 70 meters of the Glashütte drinking water source, described as the city's most productive well. The Wasserwirtschaftsamt Hof (water authority) has flagged risks to water quality and quantity. The city argues the Bundesnetzagentur's proposed measures for temporary replacement water supply are insufficient [Klagebegründung gegen den Planfeststellungsabschnitt C 2 des ...](https://www.baumann-rechtsanwaelte.de/2025/06/24/klagebegruendung-gegen-den-planfeststellungsabschnitt-c-2-des-suedostlink-eingereicht/).
- **Deficiencies in the Strategic Environmental Assessment (SEA)** [Klagebegründung gegen den Planfeststellungsabschnitt C 2 des ...](https://www.baumann-rechtsanwaelte.de/2025/06/24/klagebegruendung-gegen-den-planfeststellungsabschnitt-c-2-des-suedostlink-eingereicht/).
- **Violation of municipal planning sovereignty** under Art. 28(2) of the German Basic Law (Grundgesetz) [Klagebegründung gegen den Planfeststellungsabschnitt C 2 des ...](https://www.baumann-rechtsanwaelte.de/2025/06/24/klagebegruendung-gegen-den-planfeststellungsabschnitt-c-2-des-suedostlink-eingereicht/).
- **Nature protection errors** [Klagebegründung gegen den Planfeststellungsabschnitt C 2 des ...](https://www.baumann-rechtsanwaelte.de/2025/06/24/klagebegruendung-gegen-den-planfeststellungsabschnitt-c-2-des-suedostlink-eingereicht/).

As of the question's start date (May 12, 2026), the lawsuit is pending before BVerwG's 9th Senate with the oral hearing scheduled for June 24, 2026 [BVerwG 9 VR 10.26, Beschluss vom 29. April 2026](https://www.bverwg.de/290426B9VR10.26.0). The court has already rejected an application for interim relief (Eilrechtsschutz) against early possession (vorzeitige Besitzeinweisung) in a related case 9 VR 10.26 on April 29, 2026 [BVerwG 9 VR 10.26, Beschluss vom 29. April 2026](https://www.bverwg.de/290426B9VR10.26.0).

A relevant precedent exists: on November 5, 2025, the BVerwG (11th Senate) fully dismissed a similar lawsuit by the municipality of Trogen against SuedOstLink section C1 (case 11 A 26.24), finding that the planning approval adequately assessed water risks and that protective measures sufficiently reduced them [Pressemitteilung Nr. 84/2025 - Bundesverwaltungsgericht](https://www.bverwg.de/pm/2025/84). However, the Marktredwitz case involves different factual circumstances (notably the 70-meter proximity to the Glashütte source) and is before a different Senate (9th vs. 11th).

German courts historically show strong deference to Bundesnetzagentur planning decisions for nationally significant energy infrastructure, with full annulment being rare. More commonly, courts may order a supplementary procedure (planergänzendes Verfahren) to remedy identified defects while keeping the plan in force.

**Exact later resolution packet**

Adjudicated: The question concerns the City of Marktredwitz's lawsuit against the SuedOstLink section C2 Planfeststellungsbeschluss. On 24 June 2026 (within the 12 May - 1 July window) the BVerwG dismissed that lawsuit in its entirety, upholding the plan approval with no annulment and no supplementary procedure (planergaenzendes Verfahren) - confirmed by BVerwG press release Nr. 49/2026 (case BVerwG 9 A 2.26, 'Klage der Stadt Marktredwitz ... erfolglos') and corroborated by euwid-wasser and rechtundpolitik. The '9 A 1.26' label in the question is a scrivener's error: Marktredwitz's case is actually 9 A 2.26, while 9 A 1.26 is a private farmer's parallel C2 lawsuit whose hearing was also set for 24 June 2026 (per interim decision 9 VR 10.26 of 29 Apr 2026) and which was likewise dismissed, so even under the literal case-number anchor a full-dismissal judgment in 9 A 1.26 was announced within the window and NO-criterion #4 is not triggered. Both readings yield YES; an initial automated resolution wrongly treated the absence of a *published written* 9 A 1.26 judgment on bverwg.de as 'no judgment announced', ignoring that the criteria accept a judgment 'published OR announced' and that the ruling was pronounced in open court on 24 June 2026.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-154. `5e95949f-8063-5973-94aa-1e90942240a1`

- Present date: `2026-05-13 23:49:17.264414`
- Source cutoff boundary: `2026-05-14` (encodes end of UTC day `2026-05-13`)
- Expected resolution: `2026-06-15T00:00:00`

**Question**

Will the Council's Partial General Approach on the next EU Framework Programme (Horizon Europe 2028–2034) include a dedicated provision on 'Widening' measures?

**Resolution criteria**

This question resolves on the basis of the official Partial General Approach (PGA) text for the next EU Framework Programme for Research and Innovation (Horizon Europe 2028–2034), as produced during or immediately following the Competitiveness Council meeting expected on 29 May 2026.

The document to be reviewed must be published on or after 12 May 2026 (UTC) and by 1 July 2026 (UTC).

**Resolves YES** if the PGA text contains a "dedicated provision" on Widening measures—defined as at least one of the following within the operative part of the text (i.e., excluding recitals/preamble):
- A specific Article explicitly addressing "Widening" or "Widening participation" measures aimed at reducing the R&I gap between member states; OR
- A standalone section, chapter, or Annex explicitly titled or labeled as addressing "Widening" or "Widening participation and spreading excellence."

General references to reducing R&I disparities in recitals, preambles, or within articles primarily addressing other topics do NOT qualify.

**Resolves NO** if:
1. The PGA text is adopted but does not contain such a dedicated provision (including if Widening remains "in brackets" / excluded from the agreed text); OR
2. No PGA text is adopted by 1 July 2026.

**Resolution source:** The official Council document published via the Council of the European Union's public register of documents (https://www.consilium.europa.eu/en/documents/public-register/) or the Council's press release page for the Competitiveness Council configuration (https://www.consilium.europa.eu/en/meetings/compet/2026/05/29/). Supplementary reporting from ERA Portal Austria (https://era.gv.at/) may also be consulted.

**Pre-cutoff background**

The European Union is negotiating the next Framework Programme for Research and Innovation (Horizon Europe 2028–2034, sometimes called FP10). A key legislative milestone is the adoption of a "Partial General Approach" (PGA) by the Competitiveness Council. A PGA is a political agreement reached by the Council on specific parts of a legislative proposal that are considered sufficiently mature, while other parts remain under discussion (https://www.consilium.europa.eu/en/council-eu/decision-making/ordinary-legislative-procedure/) [https://www.consilium.europa.eu/en/council-eu/decision-making/ordinary-legislative-procedure/](https://www.consilium.europa.eu/en/council-eu/decision-making/ordinary-legislative-procedure/). The Cypriot Council Presidency aims to reach this PGA at the Competitiveness Council meeting scheduled for 29 May 2026 [https://era.gv.at/news-items/horizon-europe-is-moving-towards-a-partial-general-approach/](https://era.gv.at/news-items/horizon-europe-is-moving-towards-a-partial-general-approach/).

"Widening participation and spreading excellence" is a sub-programme within Horizon Europe designed to reduce the research and innovation (R&I) gap between EU member states. It funds instruments such as Teaming for Excellence, Twinning, ERA Chairs, Excellence Hubs, and ERA Fellowships, targeting countries with lower R&I performance (https://rea.ec.europa.eu/funding-and-grants/horizon-europe-widening-participation-and-spreading-excellence_en) [Horizon Europe: Widening participation and spreading excellence](https://rea.ec.europa.eu/funding-and-grants/horizon-europe-widening-participation-and-spreading-excellence_en). Under Horizon Europe 2021–2027, Widening received a dedicated budget of approximately €3.3 billion.

As of May 2026, the Widening provisions in the FP10 proposal have been placed "in brackets" by the previous Danish Presidency, meaning they were deferred from the research working party's agenda to broader Multiannual Financial Framework (MFF) negotiations [Widening, ECF links and priority setting top list of Horizon Europe ...](https://era.gv.at/news-items/sciencebusiness-widening-ecf-links-and-priority-setting-top-list-of-horizon-europe-sticking-points/). Several member states—including Estonia and the Czech Republic—have urged the current Cypriot Presidency to remove these brackets and return the discussion to the research working party, arguing it is the only body with relevant expertise [Widening, ECF links and priority setting top list of Horizon Europe ...](https://era.gv.at/news-items/sciencebusiness-widening-ecf-links-and-priority-setting-top-list-of-horizon-europe-sticking-points/). Whether the Cypriot Presidency successfully "untangles" Widening from the MFF discussions and includes it in the PGA text by 29 May 2026 remains a key point of uncertainty [Widening, ECF links and priority setting top list of Horizon Europe ...](https://era.gv.at/news-items/sciencebusiness-widening-ecf-links-and-priority-setting-top-list-of-horizon-europe-sticking-points/).

**Exact later resolution packet**

RESOLVES YES.

Step 1 — Was a PGA adopted by 1 July 2026? YES. The 29 May 2026 Competitiveness Council did NOT adopt a PGA; it only held a policy debate on FP10 and noted differing views on widening [1c1448]. However, the Council adopted its Partial General Approach (partial negotiating position) on Horizon Europe (FP10) on 26 June 2026, confirmed by the official Council press release "MFF 2028-2034: Council agrees its position on Horizon Europe…" (https://www.consilium.europa.eu/en/press/press-releases/2026/06/26/mff-2028-2034-council-agrees-its-position-on-horizon-europe-the-new-and-ambitious-framework-programme-for-research-and-innovation/) [fa4134, 4cc847] and by ERA-LEARN [1ce527]. This is within the resolution window (12 May–1 July 2026 UTC), so NO-condition #2 ("no PGA by 1 July 2026") is not triggered. Note: the question's "29 May 2026" was only the expected date at creation; the resolution criteria explicitly define the window as 12 May–1 July 2026 and only require that a PGA be adopted by 1 July.

Step 2 — Does the PGA text contain a dedicated Widening provision in the operative part (not recitals)? YES, in both PGA documents published 26 June 2026 in the Council's public register:
• Specific Programme implementing Horizon Europe — Council document 11203/… correction: ST-11208-2026-INIT (https://data.consilium.europa.eu/doc/document/ST-11208-2026-INIT/en/pdf). Its Annex contains "Article 15 – Widening participation and spreading excellence," which is NOT enclosed in square brackets and is therefore part of the agreed PGA text. The article explicitly targets reducing the R&I gap: "Disparities between leading and less advanced countries in terms of R&I performance shall be tackled through a differentiated portfolio of activities…" [356df1, 6227a1].
• Regulation establishing Horizon Europe — ST-11203-2026-INIT (https://data.consilium.europa.eu/doc/document/ST-11203-2026-INIT/en/pdf). Its Annex contains "Article 19 – Widening participation and spreading excellence." A careful reading shows the heading is NOT bracketed and most operative paragraphs (3, 4, 5, 5a, 6 — e.g., eligibility of widening/transition country entities as coordinators) are NOT bracketed and thus agreed; only definitional paragraphs 1, 2 and paragraph 7 are bracketed [93a627]. (An earlier, less careful read claimed Article 19 was "entirely bracketed" [3c1245]; the exact-text verification [93a627] supersedes it, showing the dedicated Widening Article is present and largely agreed.)

Either document independently satisfies the YES criteria: each contains "A specific Article explicitly addressing 'Widening participation' measures aimed at reducing the R&I gap between member states" AND "a standalone … Annex explicitly … labeled as addressing 'Widening participation and spreading excellence.'" The provisions are in the operative Annex text, not the recitals/preamble.

Step 3 — Corroboration. The official press release presents widening as part of the agreed Council position under Pillar IV (European Research Area): the position "sustains current widening instruments and allows for new measures… further develops the framework for widening measures" [4cc847, fa4134].

Because a PGA was adopted by 1 July 2026 and its operative text includes a dedicated Article titled "Widening participation and spreading excellence" (agreed, not bracketed), the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-155. `8a519cfa-20ab-5169-92ec-7c663bd4ce97`

- Present date: `2026-05-02 23:01:33.258955`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will SAG-AFTRA reach a new contract agreement with the AMPTP by June 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after May 1, 2026, and by 11:59 PM UTC on June 1, 2026, SAG-AFTRA and the AMPTP publicly announce a tentative agreement or ratify a new contract for the Television/Theatrical Agreement. This must be a new agreement negotiated in 2026, not the 2023 contract that resulted from the strike.

A "tentative agreement" approved by SAG-AFTRA's negotiating committee counts as a new contract agreement for purposes of resolution, even if full membership ratification has not yet occurred by June 1, 2026. A ratified one-year extension of the existing 2023 contract would also count as a new contract agreement.

Resolution will be determined by official announcements from SAG-AFTRA (https://www.sagaftra.org/) or the AMPTP, or by reporting from major entertainment trade publications including Variety (https://variety.com/), Deadline (https://deadline.com/), or The Hollywood Reporter (https://www.hollywoodreporter.com/).

If no tentative agreement or ratified contract is announced by 11:59 PM UTC on June 1, 2026, this question resolves NO.

**Pre-cutoff background**

The Screen Actors Guild-American Federation of Television and Radio Artists (SAG-AFTRA; https://en.wikipedia.org/wiki/SAG-AFTRA) is the labor union representing approximately 160,000 actors and media professionals. The Alliance of Motion Picture and Television Producers (AMPTP; https://en.wikipedia.org/wiki/Alliance_of_Motion_Picture_and_Television_Producers) is the trade association that negotiates labor agreements on behalf of major Hollywood studios and streamers.

SAG-AFTRA's current contract with the AMPTP — the Television/Theatrical Agreement ratified in late 2023 following a 118-day strike — expires on June 30, 2026. The union began formal negotiations with the AMPTP in February 2026, with initial sessions extending into March under a media blackout. Talks paused in March to allow the AMPTP to finalize its negotiations with the Writers Guild of America (WGA).

On April 4, 2026, the WGA reached a tentative agreement on a new four-year Minimum Basic Agreement (MBA) with the AMPTP, which was ratified by WGA members on April 24, 2026 with 90.38% voting in favor [WGA Ratifies Four-Year Contract, Accepting Cuts in Health Plan](https://variety.com/2026/film/news/wga-ratifies-amptp-contract-health-cuts-1236727987/). The WGA deal included a one-year extension beyond the traditional three-year cycle, $321 million in health fund contributions, and new AI-related provisions.

Following the WGA ratification, SAG-AFTRA and the AMPTP resumed formal negotiations on April 27, 2026. The Directors Guild of America (DGA) is scheduled to begin its own negotiations on May 11, 2026. Key issues for SAG-AFTRA include AI protections (particularly around digital replicas and voice performances), streaming residuals, and health and pension fund contributions. The WGA deal is expected to set precedents that influence the SAG-AFTRA negotiations, particularly on AI provisions.

As of May 1, 2026, SAG-AFTRA and the AMPTP are actively negotiating but no tentative agreement has been announced.

**Exact later resolution packet**

The question resolves YES. SAG-AFTRA and the AMPTP publicly announced a tentative agreement on a successor contract to the 2023 SAG-AFTRA TV/Theatrical Contracts on May 2, 2026, which falls squarely within the resolution window (on or after May 1, 2026 and by 11:59 PM UTC June 1, 2026).

Evidence:
- Variety, "SAG-AFTRA Reaches Tentative Deal on Studio Contract" (https://variety.com/2026/film/news/sag-aftra-tentative-deal-studio-contract-1236687517/), published May 2, 2026 at 3:41pm PT, states: "SAG-AFTRA and the AMPTP have reached a tentative agreement on terms for a successor contract to the 2023 SAG-AFTRA TV/Theatrical Contracts." [SAG-AFTRA Reaches Tentative Deal on Studio Contract - Variety](https://variety.com/2026/film/news/sag-aftra-tentative-deal-studio-contract-1236687517/)
- Deadline, "It's Official! Studios & SAG-AFTRA Confirm New Deal" (https://deadline.com/2026/05/studios-sag-aftra-confirm-new-deal-amptp-1236879173/), published May 2, 2026 at 4:15pm, confirms the same tentative agreement. [It's Official! Studios & SAG-AFTRA Confirm New Deal - Deadline](https://deadline.com/2026/05/studios-sag-aftra-confirm-new-deal-amptp-1236879173/)

The agreement is specifically the Television/Theatrical Agreement (a four-year successor contract to the 2023 TV/Theatrical Contracts), not Commercials or Interactive Media, satisfying that criterion. The publication timestamps (May 2, 2026, afternoon Pacific time) are well before the 11:59 PM UTC June 1, 2026 deadline. Subsequent developments (SAG-AFTRA National Board approval and member ratification vote scheduled through June 4, 2026) corroborate that a genuine tentative agreement was reached, but a board-approved tentative agreement alone is sufficient per the resolution criteria.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-156. `273985b1-0b1b-57ed-84cc-e6fbcdc67880`

- Present date: `2026-05-14 06:20:57.857835`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the U.S. Supreme Court reverse the Eleventh Circuit's decision in Havana Docks Corp. v. Royal Caribbean Cruises, Ltd. by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the U.S. Supreme Court issues an opinion or order on or after May 12, 2026 (12:00 AM UTC) and on or before July 1, 2026 (11:59 PM UTC) that **reverses** the judgment of the U.S. Court of Appeals for the Eleventh Circuit in *Havana Docks Corp. v. Royal Caribbean Cruises, Ltd.* (No. 24-983).

For the purposes of this question, "reverses" includes any of the following dispositions as stated in the Court's opinion or judgment:
- "Reversed"
- "Reversed and remanded"
- "Reversed in part" (even if affirmed in part)
- "Vacated" or "Vacated and remanded"

This question resolves **No** if:
1. The Supreme Court **affirms** the Eleventh Circuit's judgment (including affirmance by an equally divided Court).
2. The Supreme Court **dismisses** the case as improvidently granted (DIG).
3. No opinion or order disposing of the merits is issued by July 1, 2026 (11:59 PM UTC).

**Resolution source:** The official opinion or order as published on the Supreme Court's opinions page (https://www.supremecourt.gov/opinions/slipopinion/25) or the docket page (https://www.supremecourt.gov/docket/docketfiles/html/public/24-983.html).

**Pre-cutoff background**

Havana Docks Corporation v. Royal Caribbean Cruises, Ltd. (Docket No. 24-983) is a case pending before the U.S. Supreme Court concerning Title III of the LIBERTAD Act (Helms-Burton Act, [22 U.S.C. § 6082](https://www.law.cornell.edu/uscode/text/22/6082)). The central legal question is whether a plaintiff suing under Title III must prove that the defendant trafficked in property that the plaintiff owned at the time of confiscation, or whether the plaintiff must also prove it would have continued to own the property at the time of the alleged trafficking in a counterfactual world without expropriation.

The Eleventh Circuit reversed a district court judgment awarding over $400 million to Havana Docks Corporation against four cruise lines [Havana Docks Corporation v. Royal Caribbean Cruises, Ltd. (24-983)](https://www.scotusblog.com/cases/havana-docks-corporation-v-royal-caribbean-cruises-ltd/). The Supreme Court granted certiorari and heard oral arguments on February 23, 2026 [Havana Docks Corporation v. Royal Caribbean Cruises, Ltd. (24-983)](https://www.scotusblog.com/cases/havana-docks-corporation-v-royal-caribbean-cruises-ltd/). As of May 13, 2026, no opinion has been issued; the case remains pending [Havana Docks Corporation v. Royal Caribbean Cruises, Ltd. (24-983)](https://www.scotusblog.com/cases/havana-docks-corporation-v-royal-caribbean-cruises-ltd/). An opinion is expected before the end of the October 2025 term, typically by late June 2026.

The outcome is genuinely uncertain: the statutory interpretation question is complex, and legal analysts have disagreed on how the justices are likely to rule based on oral argument signals [Havana Docks Corporation v. Royal Caribbean Cruises, Ltd. (24-983)](https://www.scotusblog.com/cases/havana-docks-corporation-v-royal-caribbean-cruises-ltd/).

**Exact later resolution packet**

The question asks whether the U.S. Supreme Court "reversed" (a category that per the resolution criteria explicitly includes "Vacated" or "Vacated and remanded") the Eleventh Circuit's judgment in Havana Docks Corp. v. Royal Caribbean Cruises, Ltd. (Docket No. 24-983) via an opinion/order issued between May 12, 2026 (12:00 AM UTC) and July 1, 2026 (11:59 PM UTC).

Findings from official and corroborating sources:
- Official Supreme Court docket page (https://www.supremecourt.gov/docket/docketfiles/html/public/24-983.html): The docket records that on May 21, 2026, the "Judgment VACATED and case REMANDED," with Justice Thomas delivering the opinion of the Court [6a0c48].
- Official slip opinion (https://www.supremecourt.gov/opinions/25pdf/24-983_c07d.pdf): The opinion, authored by Justice Thomas and dated May 21, 2026, concludes with the disposition line "119 F. 4th 1276, vacated and remanded," and states "We therefore vacate the Court of Appeals' decision" [99f83e].
- Corroborating legal analysis from Faegre Drinker (dated May 2026) confirms the Supreme Court vacated the Eleventh Circuit's decision and ruled against the cruise lines [04ccea].

Application of resolution criteria:
1. The decision concerns Docket No. 24-983 — confirmed [6a0c48, 99f83e].
2. The opinion was issued on May 21, 2026, which falls within the required window (May 12, 2026 – July 1, 2026) [6a0c48, 99f83e].
3. The disposition is "vacated and remanded." The resolution criteria explicitly state that "reverses" includes "Vacated" or "Vacated and remanded." Therefore the question resolves YES [99f83e].
4. This is not an affirmance or a DIG, and an opinion was issued before the July 1, 2026 deadline, so none of the NO conditions apply.

Accordingly, the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-157. `8d2bc0c7-2a27-5f67-bbc4-2f462046906e`

- Present date: `2026-05-16 12:41:09.138366`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the UK government and the BMA reach a formal agreement to end the resident doctor pay dispute between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if a formal agreement between the British Medical Association (BMA) and the UK government (Department of Health and Social Care) to end the current resident doctor pay dispute in England is reached on or after May 12, 2026, and on or before July 1, 2026 (by 23:59 UTC on July 1, 2026).

A "formal agreement" requires BOTH of the following:
1. The BMA leadership/resident doctors' committee and the government must announce a deal (e.g., a joint statement, signed memorandum of understanding, or equivalent); AND
2. The deal must be put to BMA resident doctor membership for a ballot, and the membership must vote to accept it.

If condition (1) is met but a membership ballot has not concluded by 23:59 UTC on July 1, 2026, or the membership votes to reject the deal, the question resolves **No**.

If no such agreement is announced by the deadline, the question resolves **No**.

**Resolution sources:**
- GOV.UK newsroom: https://www.gov.uk/government/news
- BMA press releases: https://www.bma.org.uk/bma-media-centre
- Credible news reporting from outlets such as BBC News, The Guardian, Reuters, or The BMJ may be used as supplementary sources.

**Pre-cutoff background**

The pay dispute between resident doctors (formerly known as "junior doctors" — the BMA voted to adopt the term "resident doctor" in 2024 to better reflect the experience and qualifications of these doctors; see https://www.bma.org.uk/our-campaigns/resident-doctor-campaigns/pay-in-england/pay-restoration-for-resident-doctors-in-england) and the UK government has been ongoing since 2023. "Resident doctors" refers to qualified doctors in postgraduate training in the NHS, encompassing foundation year doctors through to senior specialty registrars.

The BMA's core demand is "full pay restoration" to 2008 real-terms levels, which the BMA calculates requires approximately a 26% pay rise. Since 2023, resident doctors have received cumulative pay rises totalling around 22% (2023-2024), plus 5.4% for 2025-26, and the DDRB recommended 3.5% for 2026-27.

As of May 13, 2026, the dispute remains unresolved. Key developments include:

- The government published a formal offer to the BMA UK Resident Doctors Committee (available at https://www.gov.uk/government/publications/pay-offer-to-resident-doctors/offer-to-bma-uk-resident-doctors-committee-accessible-version), which included the 3.5% DDRB-recommended pay rise for 2026-27 plus additional investment totalling approximately £700m over three years (£150m in 2026-27, £250m in 2027-28, £300m in 2028-29), along with pay structure reforms and reimbursement of royal college exam fees [Doctors' leader claims new reduced pay offer killed chances of ...](https://www.theguardian.com/society/2026/apr/10/resident-doctors-leader-reduced-pay-offer-killed-chances-ending-strikes).

- The BMA rejected this offer, calling the 3.5% DDRB recommendation "derisory" and objecting to the multi-year structure of the additional investment. The BMA's resident doctors' committee chair, Dr. Jack Fletcher, claimed the government reduced the offer at the last minute, killing chances of a deal [Doctors' leader claims new reduced pay offer killed chances of ...](https://www.theguardian.com/society/2026/apr/10/resident-doctors-leader-reduced-pay-offer-killed-chances-ending-strikes).

- Resident doctors undertook their 15th round of industrial action in April 2026 (a six-day strike from April 7-13) [Pay restoration for resident doctors in England - BMA](https://www.bma.org.uk/our-campaigns/resident-doctor-campaigns/pay-in-england/pay-restoration-for-resident-doctors-in-england).

- The BMA's legal strike mandate expires in August 2026. The BMA has stated its "door remains open for further talks" [Pay restoration for resident doctors in England - BMA](https://www.bma.org.uk/our-campaigns/resident-doctor-campaigns/pay-in-england/pay-restoration-for-resident-doctors-in-england).

- The government, through Health Secretary Wes Streeting, has maintained that the offer is fair and accused the BMA of making unreasonable demands.

Both sides face pressure: the government from ongoing NHS disruption (estimated cost of strikes: £3bn), and the BMA from the risk of declining public sympathy. The gap between the government's offer and the BMA's demands remains significant but has narrowed since 2023.

**Exact later resolution packet**

The question resolves YES. Both required conditions of the resolution criteria were satisfied within the window (May 12–July 1, 2026):

**Condition 1 — A deal was announced by both the government and the BMA:** In June 2026, the UK government (Department of Health and Social Care) made a revised offer to the BMA UK Resident Doctors Committee to end the dispute on jobs and pay. The BMA called off its planned 15–19 June 2026 strikes on June 13, 2026, and put the offer to a membership referendum (BMA "Government offer to resident doctors in England to end the dispute on jobs and pay (June 2026)" page; GOV.UK offer document dated June 2026). The offer included an average 6.6% pay uplift package, pay structure reform, and reimbursement of royal college exam fees.

**Condition 2 — The BMA membership voted to accept:** On Monday, June 29, 2026, the BMA's Resident Doctors Committee announced that its membership had voted to ACCEPT the government's offer. 53% of eligible BMA members voted in favour, on a turnout of 57%, with 32,932 doctors voting [Resident doctors in England accept pay deal and end strikes - BBC](https://www.bbc.com/news/articles/cwy01n5z48qo) [Resident doctors in England accept government offer on pay and jobs](https://www.theguardian.com/society/2026/jun/29/resident-doctors-england-accept-pay-jobs). The official UK government press release published June 29, 2026, confirms: "Resident doctors have voted to accept an offer from the government, bringing an end to a period of industrial action" [Resident doctors agree deal with government to end strikes](https://www.gov.uk/government/news/resident-doctors-agree-deal-with-government-to-end-strikes).

The ballot result was announced on June 29, 2026 — before the 23:59 UTC July 1, 2026 deadline. The dispute is specifically for resident doctors (formerly junior doctors) in England [Resident doctors in England accept pay deal and end strikes - BBC](https://www.bbc.com/news/articles/cwy01n5z48qo) [Resident doctors in England accept government offer on pay and jobs](https://www.theguardian.com/society/2026/jun/29/resident-doctors-england-accept-pay-jobs) [Resident doctors agree deal with government to end strikes](https://www.gov.uk/government/news/resident-doctors-agree-deal-with-government-to-end-strikes).

Sources:
- GOV.UK: https://www.gov.uk/government/news/resident-doctors-agree-deal-with-government-to-end-strikes [Resident doctors agree deal with government to end strikes](https://www.gov.uk/government/news/resident-doctors-agree-deal-with-government-to-end-strikes)
- BBC News (June 29, 2026): https://www.bbc.com/news/articles/cwy01n5z48qo [Resident doctors in England accept pay deal and end strikes - BBC](https://www.bbc.com/news/articles/cwy01n5z48qo)
- The Guardian (June 29, 2026): https://www.theguardian.com/society/2026/jun/29/resident-doctors-england-accept-pay-jobs [Resident doctors in England accept government offer on pay and jobs](https://www.theguardian.com/society/2026/jun/29/resident-doctors-england-accept-pay-jobs)

Because a deal was announced by both parties AND the membership ballot concluded with an acceptance vote (53% in favour) announced on June 29, 2026 — well before the July 1, 2026 deadline — the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-158. `eb6d9c97-3d83-5fde-970d-74dae4f60424`

- Present date: `2026-05-03 12:56:02.785913`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the U.S. Department of Education publish the final rule for the Workforce Pell Grant program in the Federal Register by June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if the U.S. Department of Education publishes a **final rule** implementing the Workforce Pell Grant program in the **Federal Register** on or after May 1, 2026, and on or before June 1, 2026, 11:59 PM UTC.

It resolves as **No** if no such final rule appears in the Federal Register by that deadline.

**Definitions:**
- **"Final rule"**: A rule published in the Federal Register as a final rule (not a proposed rule or interim final rule), implementing the Workforce Pell Grant provisions of the One Big Beautiful Bill Act. See the Federal Register's guide to rulemaking: https://www.federalregister.gov/uploads/2011/01/the_rulemaking_process.pdf
- **"Workforce Pell Grant"**: The expansion of Pell Grant eligibility to short-term workforce training programs as authorized by the One Big Beautiful Bill Act (H.R. 1, 119th Congress). See the NPRM: https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant

**Resolution source:** The Federal Register at https://www.federalregister.gov/. The question resolves by searching for final rules published by the Department of Education related to "Workforce Pell" between May 1 and June 1, 2026.

**Pre-cutoff background**

The Workforce Pell Grant program was established by the "One Big Beautiful Bill Act" (OBBBA), signed into law in July 2025. It expands federal Pell Grant eligibility to short-term workforce training programs (150–599 clock hours) and is statutorily set to take effect on July 1, 2026 [Federal Register :: ACCOUNTABILITY IN HIGHER EDUCATION ...](https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant).

On March 9, 2026, the U.S. Department of Education published a Notice of Proposed Rulemaking (NPRM) in the Federal Register (https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant) to implement the program [Federal Register :: ACCOUNTABILITY IN HIGHER EDUCATION ...](https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant). The public comment period closed on April 8, 2026, with over 400 comments received [Colleges Urge ED to Rethink Aspects of Workforce Pell](https://www.insidehighered.com/news/government/student-aid-policy/2026/04/10/colleges-urge-ed-rethink-aspects-workforce-pell). Stakeholders, including colleges and industry groups, have urged the Department to rethink key provisions such as job-placement rate calculations and program length requirements [Colleges Urge ED to Rethink Aspects of Workforce Pell](https://www.insidehighered.com/news/government/student-aid-policy/2026/04/10/colleges-urge-ed-rethink-aspects-workforce-pell).

As of May 2, 2026, the Department is reviewing the 400+ comments and has not yet published a final rule. The Department must finalize and publish the rule before the July 1, 2026, effective date. A separate related NPRM on the Student Tuition and Transparency System was published on April 20, 2026, with a comment period closing May 20, 2026, adding further complexity to the rulemaking timeline.

The key question is whether the Department can complete its review of comments and publish the final rule within roughly two months of the comment period closing—a tight but not unprecedented timeline for federal rulemaking, especially given political pressure to launch the program on schedule.

**Exact later resolution packet**

The question resolves YES.

The resolution criteria require that the U.S. Department of Education publishes a final rule implementing the Workforce Pell Grant program in the Federal Register on or after May 1, 2026 and on or before June 1, 2026 (11:59 PM UTC).

A Federal Register search filtered to Department of Education final rules ("RULE" type) containing "Workforce Pell" returns the document "Accountability in Higher Education and Access Through Demand-Driven Workforce Pell: Pell Grant Exclusion Relating to Other Grant Aid; and Workforce Pell Grants," published as a FINAL RULE by the Education Department on May 19, 2026 [https://www.federalregister.gov/documents/search?conditions%5Bagencies%5D%5B%5D=education-department&conditions%5Bterm%5D=Workforce+Pell&conditions%5Btype%5D%5B%5D=RULE](https://www.federalregister.gov/documents/search?conditions%5Bagencies%5D%5B%5D=education-department&conditions%5Bterm%5D=Workforce+Pell&conditions%5Btype%5D%5B%5D=RULE). The direct URL is https://www.federalregister.gov/documents/2026/05/19/2026-10013/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant.

This satisfies all checklist requirements:
- It is a Final Rule (Federal Register document type "Rule"), not an NPRM or interim final rule. The March 9, 2026 document (2026-04520) was the proposed rule; this May 19 document (2026-10013) is the corresponding final rule.
- The publication date, May 19, 2026, falls within the inclusive window of May 1, 2026 through June 1, 2026.
- The rule specifically implements the Workforce Pell Grant program (short-term workforce training programs of 150–599 clock hours) authorized by the One Big Beautiful Bill Act (OBBBA / H.R. 1, 119th Congress), amending § 600.10 to require Secretary approval of eligible workforce programs, with provisions taking effect July 1, 2026. The Department of Education's own press release titled "U.S. Department of Education Issues Final Rule to Create New Workforce Pell Grant Program" confirms this.

Therefore the consequent occurred and the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-159. `8941ab59-cdeb-5993-ad77-ac4d1b0d2eae`

- Present date: `2026-05-01 16:38:56.727379`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Pope Leo XIV's first encyclical be published with the title 'Magnifica Humanitas' by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if ALL of the following conditions are met:

1. An encyclical (as defined by the Vatican: https://www.britannica.com/topic/encyclical — a papal letter addressed to the whole Church on matters of doctrine, morals, or discipline) by Pope Leo XIV is published ("published" meaning it appears on the official Vatican website at https://www.vatican.va/content/leo-xiv/en/encyclicals.html or is announced via the Holy See Press Office at https://press.vatican.va/) on or after April 30, 2026 (00:00 UTC) and on or before June 1, 2026 (23:59 UTC).

2. The title of the encyclical — defined as the Latin incipit (the opening words of the official Latin text that serve as the document's conventional name, as displayed in the document's heading on vatican.va) — is "Magnifica Humanitas" (case-insensitive, with or without diacritical marks).

If no encyclical is published by June 1, 2026 (23:59 UTC), or if the encyclical is published with a different title/incipit, the question resolves **No**.

**Resolution source:** The official Vatican website (https://www.vatican.va/content/leo-xiv/en/encyclicals.html) or the Vatican Press Office (https://press.vatican.va/). If unavailable, credible reporting from outlets such as Catholic News Agency (https://www.catholicnewsagency.com/), National Catholic Register (https://www.ncregister.com/), or Reuters (https://www.reuters.com/) may be used.

**Pre-cutoff background**

Pope Leo XIV (Robert Francis Prevost), elected in May 2025, has been preparing his first encyclical (a formal papal letter addressed to the whole Church; see https://www.britannica.com/topic/encyclical). As of March 2026, multiple credible Catholic news outlets reported that the encyclical carries the working title "Magnifica Humanitas" ("Magnificent Humanity") and is expected to address ethical challenges posed by artificial intelligence, including its impact on human work, social relations, and the dignity of the person [Reports emerge on Pope Leo XIV's first encyclical](https://thecatholicherald.com/article/reports-emerge-on-pope-leo-xivs-first-encyclical) [Pope Leo XIV's first encyclical arrives after Easter](https://clericalwhispers.blogspot.com/2026/03/pope-leo-xivs-first-encyclical-arrives.html).

According to The Catholic Herald (March 16, 2026), the document is in its final stages of revision and "could appear shortly after Easter" 2026 (Easter fell on April 5, 2026) [Reports emerge on Pope Leo XIV's first encyclical](https://thecatholicherald.com/article/reports-emerge-on-pope-leo-xivs-first-encyclical). The blog Clerical Whispers, citing La Repubblica, similarly reported in March 2026 that publication was expected after Easter [Pope Leo XIV's first encyclical arrives after Easter](https://clericalwhispers.blogspot.com/2026/03/pope-leo-xivs-first-encyclical-arrives.html).

In Catholic tradition, the title of an encyclical is typically the Latin incipit — the first words of the official Latin text. Working titles frequently change during the revision process, introducing uncertainty about whether the final published title will indeed be "Magnifica Humanitas." As of April 30, 2026, no encyclical has yet appeared on the Vatican's official website (https://www.vatican.va/content/leo-xiv/en/encyclicals.html), though the Pope's other documents (letters, audiences) continue to be published through late April 2026.

**Exact later resolution packet**

The question resolves YES. All conditions of the resolution criteria are satisfied:

1. **An encyclical was published**: The official Vatican website lists "Encyclical Letter of His Holiness Leo XIV Magnifica Humanitas" at https://www.vatican.va/content/leo-xiv/en/encyclicals.html and the full document at https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html [c9e279]. It is explicitly categorized as an encyclical by the Vatican.

2. **Author is Pope Leo XIV**: The document is signed "LEO PP. XIV" and given "in Rome, at Saint Peter's, on 15 May, in the year 2026, the second of my Pontificate" — confirming authorship by Pope Leo XIV (Robert Francis Prevost) [c9e279].

3. **Title/incipit is 'Magnifica Humanitas'**: The Latin incipit and conventional name of the encyclical is "Magnifica Humanitas" ("On Safeguarding the Human Person in the Time of Artificial Intelligence"), as displayed in the document heading on vatican.va [c9e279].

4. **Within the resolution window (April 30, 2026 00:00 UTC – June 1, 2026 23:59 UTC)**: The encyclical was signed on May 15, 2026 and formally released/published by the Holy See on May 25, 2026. Both dates fall strictly within the required window. This is corroborated by Vatican News (https://www.vaticannews.va/en/pope/news/2026-05/pope-leo-xiv-first-encyclical-magnifica-humanitas.html), the National Catholic Register, EWTN News, and Chicago Catholic, all reporting the May 25, 2026 release.

Since an encyclical titled "Magnifica Humanitas" by Pope Leo XIV was published on the official Vatican website within the April 30 – June 1, 2026 window, the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-160. `460d351d-1699-5d03-9f58-b6af58e7e558`

- Present date: `2026-05-02 09:40:48.038456`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the US launch a kinetic military strike against Iranian territory between May 1, 2026 and June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if the United States Armed Forces conduct at least one offensive kinetic military strike against a target located within Iranian territory on or after May 1, 2026, and no later than 23:59 UTC on June 1, 2026. Otherwise, it resolves **No**.

**Definition of "kinetic military strike":** Any offensive use of physical force by US military assets, including but not limited to airstrikes, missile strikes, drone strikes, or naval bombardment. This follows the standard DoD usage of "kinetic" as involving physical force (see https://en.wikipedia.org/wiki/Kinetic_military_action). This explicitly **excludes**: cyberattacks, electronic warfare, economic sanctions, naval blockade enforcement (unless involving weapons fire against land targets), covert operations not publicly acknowledged, and purely defensive actions such as intercepting incoming missiles or drones.

**Definition of "Iranian territory":** The internationally recognized sovereign territory of the Islamic Republic of Iran, including its mainland, islands, and territorial waters as defined under international law (see https://en.wikipedia.org/wiki/Geography_of_Iran). This excludes Iranian diplomatic missions abroad, Iranian proxy forces outside Iran, and Iranian vessels or aircraft outside Iranian territorial waters/airspace.

**Temporal scope:** Only strikes occurring on or after 00:00 UTC on May 1, 2026, count toward resolution.

**Resolution source:** Official statements from the US Department of Defense (https://www.defense.gov/News/Releases/) or consistent reporting by at least two of the following major news organizations: Reuters (https://www.reuters.com), Associated Press (https://apnews.com), BBC (https://www.bbc.com/news), or The New York Times (https://www.nytimes.com).

**Pre-cutoff background**

Following a series of US and Israeli military strikes against Iran beginning on February 28, 2026, a conditional two-week ceasefire was brokered by Pakistan on April 8, 2026 [https://commonslibrary.parliament.uk/research-briefings/cbp-10637/](https://commonslibrary.parliament.uk/research-briefings/cbp-10637/). This ceasefire was extended on April 21, 2026, pending the outcome of ongoing diplomatic negotiations [https://commonslibrary.parliament.uk/research-briefings/cbp-10637/](https://commonslibrary.parliament.uk/research-briefings/cbp-10637/). President Trump has explicitly threatened that if a deal is not reached, the US will "knock out every single power plant, and every single bridge, in Iran" [https://commonslibrary.parliament.uk/research-briefings/cbp-10637/](https://commonslibrary.parliament.uk/research-briefings/cbp-10637/).

On April 28, 2026, Iran submitted a proposal to reopen the Strait of Hormuz in exchange for the US ending the war and lifting its naval blockade, while postponing discussions on Iran's nuclear program. The Trump administration rejected this proposal as insufficient, citing the lack of provisions addressing Iran's nuclear activities [https://www.aljazeera.com/news/2026/4/28/whats-in-irans-latest-proposal-and-how-has-the-us-responded](https://www.aljazeera.com/news/2026/4/28/whats-in-irans-latest-proposal-and-how-has-the-us-responded).

As of May 1, 2026, the ceasefire remains in effect but is fragile. The US maintains a significant military presence in the region, and the potential for resumed hostilities is high if diplomatic efforts continue to stall. The conflict has already caused major disruption to global energy supplies through the US naval blockade of the Strait of Hormuz [https://www.aljazeera.com/news/2026/4/28/whats-in-irans-latest-proposal-and-how-has-the-us-responded](https://www.aljazeera.com/news/2026/4/28/whats-in-irans-latest-proposal-and-how-has-the-us-responded).

**Exact later resolution packet**

The question resolves YES. Between May 1, 2026 and 23:59 UTC June 1, 2026, the US Armed Forces conducted multiple kinetic strikes against land-based targets located within internationally recognized Iranian territory (mainland and islands), reported consistently by the approved resolution sources.

KEY EVENTS WITHIN THE WINDOW:

1) May 7, 2026 — US strikes on Iran's Qeshm port and Bandar Abbas. Reported by Reuters (https://www.reuters.com/world/middle-east/us-military-strikes-irans-qeshm-port-bandar-abbas-fox-news-reporter-says-2026-05-07/), BBC, CNN (https://www.cnn.com/2026/05/07/politics/us-forces-strike-military-facilities-in-iran), and summarized in Wikipedia's "2026 Iran war" entry, which states "On 7 May, the US said that it struck Iranian military sites in Bandar Abbas... and Qeshm Island" [2026 Iran war - Wikipedia](https://en.wikipedia.org/wiki/2026_Iran_war). Qeshm Island and Bandar Abbas are both within Iranian sovereign territory.

2) May 25, 2026 — US "self-defense strikes" in southern Iran targeting Iranian missile launch sites and boats. Reported by BBC (https://www.bbc.com/news/articles/cvgzzn4y1n8o), which states the US "launched new strikes on southern Iran... targeting Iranian missile sites and boats" near Bandar Abbas [US launches new strikes on Iran, targeting missile sites and boats](https://www.bbc.com/news/articles/cvgzzn4y1n8o); by AP (https://apnews.com/article/iran-deal-trump-israel-abrams-01a13e9a63ece786a0a7fa4933dbf09b and https://www.pbs.org/newshour/world/u-s-says-it-carried-out-self-defense-strikes-in-iran-including-missile-sites-and-boats-placing-mines, AP byline); and by NYT (https://www.nytimes.com/2026/05/25/world/middleeast/us-iran-strikes.html). CNN's live coverage likewise quotes CENTCOM: "U.S. forces conducted self-defense strikes in southern Iran today" [May 25-26, 2026 - US strikes on Iranian missile launch sites ... - CNN](https://www.cnn.com/2026/05/25/world/live-news/iran-war-us-peace-deal).

3) May 27, 2026 — US struck an Iranian military site (ground control station) in Bandar Abbas, per Reuters (https://www.reuters.com/world/middle-east/us-carries-out-new-strikes-iran-against-military-site-official-says-2026-05-27/) [US carries out new strikes in Iran against a military site and drones ...](https://www.reuters.com/world/middle-east/us-carries-out-new-strikes-iran-against-military-site-official-says-2026-05-27/).

4) June 1, 2026 — NYT reported additional US strikes on military targets in southern Iran (Goruk and Qeshm Island): https://www.nytimes.com/2026/06/01/world/middleeast/us-strikes-iran-goruk-qeshm.html.

WHY THIS COUNTS AS AN OFFENSIVE KINETIC STRIKE (not an excluded defensive action): The resolution criteria exclude "purely defensive actions such as intercepting incoming missiles or drones." These US actions were NOT interceptions — they involved firing weapons against fixed land targets located inside Iran (missile launch sites, ground control/radar stations, ports, command-and-control facilities) on the Iranian mainland and on Qeshm Island. Striking targets physically located within Iranian territory is an "offensive use of physical force by US military assets" against a target within Iranian territory, exactly as defined in the resolution criteria. The fact that the US labeled them "self-defense strikes" (a legal/political justification) does not convert a strike on Iranian soil into one of the excluded categories (interception of incoming missiles/drones, cyber, electronic warfare, sanctions, blockade enforcement, or unacknowledged covert ops). These strikes were publicly acknowledged by the US military (CENTCOM).

SOURCE-RULE COMPLIANCE: The events are confirmed by official US military (CENTCOM) statements and by consistent reporting from at least two approved outlets — notably Reuters, AP, BBC, and the New York Times — well exceeding the "at least two" threshold.

Therefore, at least one (in fact several) offensive kinetic US military strike against targets within Iranian territory occurred within the May 1–June 1, 2026 window. Resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-161. `79537e84-15ff-5d71-b885-c6663265e2b7`

- Present date: `2026-05-16 09:46:22.660379`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the CHMP issue a positive opinion recommending marketing authorization for Daybu (trofinetide) for Rett syndrome following its re-examination by July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if the CHMP issues a positive opinion (i.e., a recommendation for marketing authorization) for Daybu (trofinetide) for the treatment of Rett syndrome on or after May 12, 2026 (00:00 UTC) and on or before July 1, 2026 (23:59 UTC).

This question resolves as **No** if:
- The CHMP confirms its previous negative opinion (maintaining the refusal of marketing authorization) by July 1, 2026; OR
- No final re-examination opinion is issued by the CHMP by July 1, 2026 (23:59 UTC).

**Primary resolution source:** The official EMA publication on the [Daybu EPAR page](https://www.ema.europa.eu/en/medicines/human/EPAR/daybu) or the [CHMP meeting highlights page](https://www.ema.europa.eu/en/news-events/committee-highlights). The outcome must be reflected in an official EMA publication to count toward resolution.

**Pre-cutoff background**

Daybu (trofinetide) is a medicine developed by Acadia Pharmaceuticals for the treatment of Rett syndrome, a rare genetic condition affecting the brain and nervous system. Trofinetide is already approved in the United States by the FDA under the brand name Daybue (approved February 2023).

On 26 February 2026, the European Medicines Agency's (EMA) Committee for Medicinal Products for Human Use (CHMP) issued a negative opinion recommending refusal of marketing authorization for Daybu [https://www.ema.europa.eu/en/medicines/human/EPAR/daybu](https://www.ema.europa.eu/en/medicines/human/EPAR/daybu). The CHMP's refusal was based on several concerns [[PDF] Refusal of the marketing authorisation for Daybu (trofinetide) - EMA](https://www.ema.europa.eu/en/documents/smop-initial/questions-answers-refusal-marketing-authorisation-daybu-trofinetide_en.pdf):

1. **Insufficient clinical meaningfulness:** The effect size observed after 12 weeks of treatment was deemed too small to be clinically meaningful.
2. **Incomplete symptom assessment:** The pivotal study failed to assess several key symptoms of Rett syndrome.
3. **Data limitations:** Conclusions regarding long-term effectiveness were undermined by a high number of patient withdrawals from the study.
4. **Lack of representativeness:** The study population did not include patients across the different disease stages of Rett syndrome.

On 17 March 2026, Acadia Pharmaceuticals requested a re-examination of the CHMP opinion [[PDF] Refusal of the marketing authorisation for Daybu (trofinetide) - EMA](https://www.ema.europa.eu/en/documents/smop-initial/questions-answers-refusal-marketing-authorisation-daybu-trofinetide_en.pdf). Under EU regulations, the CHMP has 60 days from receipt of the re-examination request to conclude its review. The re-examination is currently ongoing as of May 2026 [https://www.ema.europa.eu/en/medicines/human/EPAR/daybu](https://www.ema.europa.eu/en/medicines/human/EPAR/daybu). Historically, CHMP re-examinations rarely reverse initial negative opinions, though strong patient advocacy and the existing US approval may influence the outcome.

**Key terms:**
- **CHMP (Committee for Medicinal Products for Human Use):** The EMA committee responsible for providing opinions on medicines for human use. See: [EMA - CHMP](https://www.ema.europa.eu/en/committees/committee-medicinal-products-human-use-chmp)
- **Positive opinion:** A formal recommendation by the CHMP to the European Commission to grant a [marketing authorization](https://www.ema.europa.eu/en/glossary/marketing-authorisation) — the legal approval allowing a medicine to be placed on the EU market.
- **Marketing authorization:** The official approval granted by the European Commission (based on the CHMP opinion) permitting a medicine to be marketed and sold in the EU. See: [EMA glossary](https://www.ema.europa.eu/en/glossary/marketing-authorisation)

**Exact later resolution packet**

The question resolves YES.

Resolution criteria: YES if the CHMP issues a positive opinion recommending marketing authorization for Daybu (trofinetide) for Rett syndrome on or after May 12, 2026 (00:00 UTC) and on or before July 1, 2026 (23:59 UTC), as reflected in an official EMA publication.

Evidence from the primary resolution source — the official EMA Daybu EPAR page (https://www.ema.europa.eu/en/medicines/human/EPAR/daybu) — states verbatim: "On 25 June 2026, the Committee for Medicinal Products for Human Use (CHMP), following a re-examination procedure, adopted a positive opinion recommending the granting of a marketing authorisation for the medicinal product Daybu, intended for the treatment of neurobehavioural symptoms of Rett syndrome." [Daybu | European Medicines Agency (EMA)](https://www.ema.europa.eu/en/medicines/human/EPAR/daybu)

The CHMP re-examination followed the initial negative opinion of 26 February 2026 and Acadia's re-examination request of 17 March 2026 (documented in the EMA refusal Q&A PDF: https://www.ema.europa.eu/en/documents/smop-initial/questions-answers-refusal-marketing-authorisation-daybu-trofinetide_en.pdf).

The positive re-examination opinion date, 25 June 2026, falls squarely within the required window (12 May 2026 – 1 July 2026). It is documented in an official EMA publication (the EPAR page), satisfying the source requirement. This is further corroborated by the CHMP meeting highlights for 22–25 June 2026 (https://www.ema.europa.eu/en/news/meeting-highlights-committee-medicinal-products-human-use-chmp-22-25-june-2026), Acadia's press release dated 26 June 2026 (https://acadia.com/en-us/media/news-releases/daybu-trofinetide-recommended-for-approval-in-the-european-union-by-chmp), and independent coverage (BioWorld, Medscape, MarketWatch), all reporting that the CHMP reversed its earlier negative opinion and recommended approval following re-examination.

Therefore the antecedent conditions are met and the consequent (positive opinion within the window) occurred, resolving the question YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-162. `4b3368df-9ae1-5f73-9d06-8c144a90daa3`

- Present date: `2026-05-14 02:52:51.633224`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-30T00:00:00`

**Question**

Will Syrian government Internal Security Forces maintain operational control of their headquarters in central Qamishli through June 30, 2026?

**Resolution criteria**

This question resolves Yes if, on June 30, 2026 (23:59 UTC), Syrian government security forces are maintaining operational control of at least one Internal Security Forces (ISF) headquarters facility within the government security enclave in central Qamishli (defined as the area bounded by the Qamishli city center districts of Qudurbek, Hilaliyeh, and the area surrounding the former regime security square/government buildings cluster, approximately 37.05°N, 41.22°E).

**Definitions:**
- 'Syrian government security forces' means forces under the authority of the Syrian transitional government's Ministry of Interior, including the Internal Security Forces (ISF/General Security Service) and any police units formally reporting to Damascus. This excludes SDF Asayish forces and local Kurdish police (Asayish).
- 'Operational control' constitutes maintaining a permanent garrison with uniformed personnel present at the facility, conducting regular operations (administrative, patrol, or checkpoint functions) from that facility. A temporary evacuation of less than 48 hours due to a security incident does not constitute loss of operational control.
- This assessment applies to developments on or after May 12, 2026 (00:00 UTC). If government forces were expelled before May 12, 2026 and have not returned, the question resolves No.

This question resolves No if credible reporting indicates that Syrian government security forces have been permanently expelled from, voluntarily withdrawn from, or lost operational control of all ISF headquarters in central Qamishli by June 30, 2026 (23:59 UTC).

**Resolution sources:** Credible international media reporting from at least one of the following: Reuters (https://www.reuters.com), Al Jazeera (https://www.aljazeera.com), Associated Press (https://apnews.com), Enab Baladi (https://english.enabbaladi.net), or the Syrian Observatory for Human Rights (https://www.syriahr.com/en/). In the absence of reporting indicating expulsion or withdrawal, the question resolves Yes by default, as the government presence was established in February 2026.

**Pre-cutoff background**

On January 30, 2026, the Syrian transitional government and the Kurdish-led Syrian Democratic Forces (SDF) reached a US-backed agreement for phased integration of military and administrative structures into state institutions, including the deployment of security forces to the centers of Hasakah and Qamishli [https://www.longwarjournal.org/archives/2026/04/syrian-president-meets-syrian-democratic-forces-leader-to-discuss-next-phase-of-integration.php](https://www.longwarjournal.org/archives/2026/04/syrian-president-meets-syrian-democratic-forces-leader-to-discuss-next-phase-of-integration.php). On February 3, 2026, Syrian government Interior Ministry security forces entered Qamishli and were stationed at several state buildings and the city's airport.

However, the government's presence has been contested. In March 2026, following an incident where the Syrian flag was lowered during Nowruz celebrations in Kobani, local SDF-affiliated groups stormed several government Internal Security Forces (ISF) headquarters in Qamishli, causing material damage. The SDF's Asayish forces subsequently sealed off the government security enclave in Qamishli [Security tension following flag incident, official condemnations and ...](https://english.enabbaladi.net/archives/2026/03/security-tension-following-flag-incident-official-condemnations-and-calls-for-calm/). On April 16, 2026, the Syrian president met with the SDF leader in Damascus to discuss the next phase of integration [https://www.longwarjournal.org/archives/2026/04/syrian-president-meets-syrian-democratic-forces-leader-to-discuss-next-phase-of-integration.php](https://www.longwarjournal.org/archives/2026/04/syrian-president-meets-syrian-democratic-forces-leader-to-discuss-next-phase-of-integration.php).

As of May 13, 2026 (UTC), the Syrian government maintains a limited security enclave in Qamishli, including ISF headquarters and the airport, but its operational presence remains subject to periodic challenges from SDF-affiliated groups. The situation is volatile, and the government's ability to sustain its presence depends on the continued implementation of the January 30 agreement and management of local tensions.

**Exact later resolution packet**

RESOLUTION: YES (1).

BACKGROUND / ANTECEDENT: The question is not conditional. It resolves YES if, on June 30, 2026 (23:59 UTC), Syrian transitional government Ministry of Interior security forces (ISF/General Security Service, excluding SDF Asayish) maintained operational control of at least one ISF headquarters facility within the central Qamishli security enclave (Qudurbek/Hilaliyeh/government buildings cluster, ~37.05°N, 41.22°E). Crucially, the criteria state: "In the absence of reporting indicating expulsion or withdrawal, the question resolves Yes by default, as the government presence was established in February 2026."

The government presence was established in early February 2026 when Interior Ministry Internal Security Forces entered Qamishli and were stationed in state buildings within the security zone (Reuters, Feb 3, 2026: https://www.reuters.com/world/middle-east/syrian-security-convoy-heads-key-kurdish-city-under-us-backed-deal-2026-02-03/ ; Al Jazeera, Feb 3, 2026: https://www.aljazeera.com/news/2026/2/3/syrian-forces-enter-qamishli-under-ceasefire-deal-with-sdf-state-media). These forces occupy the "security square" in central Qamishli.

EVIDENCE THAT GOVERNMENT FORCES REMAINED IN CONTROL AFTER MAY 12, 2026 (the assessment window) THROUGH JUNE 30, 2026 — and were NOT expelled/withdrawn:

1. Security Council Report, June 2026 Monthly Forecast (https://www.securitycouncilreport.org/monthly-forecast/2026-06/syria-92.php): Reports the January 2026 SDF/DAANES integration agreement implementation is continuing (with obstacles over Hasakah judicial issues), and that SDF commander Mazloum Abdi announced an understanding with Damascus to continue integration. No report of ISF being expelled from or withdrawing from Qamishli [56a0b8].

2. Enab Baladi, June 5, 2026 ("9,000 Asayish Members Nominated for Integration") (https://english.enabbaladi.net/archives/2026/06/over-9000-asayish-members-up-for-integration/): Integration of Asayish members into the Interior Ministry's Internal Security Directorate is actively proceeding, with committees conducting interviews in al-Hasakah and al-Qamishli. Describes ongoing consolidation of government security institutions — no expulsion/withdrawal [7f8947].

3. Syrian Observatory for Human Rights (SOHR), June 19, 2026 (https://www.syriahr.com/en/date/2026/06/19/): SOHR reported "transitional government forces personnel seizing the house of a Kurdish..." in Qamishli — direct evidence that Syrian transitional government (Interior Ministry) forces were physically present and conducting operations in Qamishli as of June 19, 2026, well within the resolution window. No report of their expulsion/withdrawal [949e2c].

4. Enab Baladi, June 3, 2026 ("SDF Launches Month-Long Campaign in al-Hasakah") (https://english.enabbaladi.net/archives/2026/06/sdf-launches-month-long-campaign-in-al-hasakah/): Discusses SDF security activity in al-Hasakah city; does not report any expulsion or withdrawal of government ISF from the Qamishli enclave [7afe2e].

NO CONTRARY EVIDENCE: Across searches of the mandated sources (Reuters, Al Jazeera, AP, Enab Baladi, SOHR), there is no report of Syrian government Interior Ministry forces being permanently expelled from, voluntarily withdrawing from, or losing operational control of all ISF headquarters in central Qamishli during May 12 – June 30, 2026. The March 2026 flag-incident storming of ISF headquarters and Asayish sealing off the enclave predate the May 12 assessment window and did not result in a sustained (>48h) loss of control; government forces remained. The only reported June attacks on Internal Security headquarters were ISIS attacks in Raqqa (Enab Baladi, June 16), not Qamishli.

CONCLUSION: Government (Ministry of Interior) ISF forces remained present and operationally active in central Qamishli through June 30, 2026, and no source reported expulsion/withdrawal. Per both the affirmative evidence (SOHR June 19 sighting of government forces operating in Qamishli) and the explicit default rule, the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-163. `d8e6a8b4-c56a-51f5-b7d5-63e20731db38`

- Present date: `2026-05-01 11:06:37.113118`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-05-25 00:00:00`

**Question**

Will the New York Knicks reach the 2026 Eastern Conference Finals?

**Resolution criteria**

This question resolves **Yes** if the New York Knicks appear as a participant in the first game of the 2026 Eastern Conference Finals (i.e., the Knicks have won both their first-round series and their Conference Semifinals series). It resolves **No** if the Knicks are eliminated from the 2026 NBA Playoffs before the Eastern Conference Finals begins.

Resolution will be determined by the official NBA playoff bracket at https://www.nba.com/playoffs/2026/bracket or the ESPN playoff bracket at https://www.espn.com/nba/playoff-bracket. The 2026 NBA playoffs Wikipedia page (https://en.wikipedia.org/wiki/2026_NBA_playoffs) may also be used as a secondary source [2026 NBA playoffs - Wikipedia](https://en.wikipedia.org/wiki/2026_NBA_playoffs).

**Pre-cutoff background**

The 2026 NBA Playoffs are underway. The New York Knicks, seeded 3rd in the Eastern Conference, are facing the 6th-seeded Atlanta Hawks in the first round (best-of-seven). As of April 30, 2026, the Knicks lead the Hawks 3-2 in the series [2026 NBA playoff bracket: Matchups, schedule as Rockets, Pistons ...](https://www.cbssports.com/nba/news/2026-nba-playoff-bracket-matchups-schedule/).

To reach the Eastern Conference Finals (ECF), the Knicks must: (1) close out their first-round series against the Hawks, and (2) win the Eastern Conference Semifinals (also best-of-seven) against the winner of the Boston Celtics (2) vs. Philadelphia 76ers (7) series, where the Celtics currently lead 3-2 [2026 NBA playoff bracket: Matchups, schedule as Rockets, Pistons ...](https://www.cbssports.com/nba/news/2026-nba-playoff-bracket-matchups-schedule/).

On the other side of the Eastern Conference bracket, the (1) Detroit Pistons face the (8) Orlando Magic (Magic lead 3-1), and the (4) Cleveland Cavaliers face the (5) Toronto Raptors (series tied 2-2) [2026 NBA playoff bracket: Matchups, schedule as Rockets, Pistons ...](https://www.cbssports.com/nba/news/2026-nba-playoff-bracket-matchups-schedule/). The Conference Semifinals are scheduled to begin May 2–4, 2026, and the Eastern Conference Finals are scheduled to begin May 19, 2026 [2026 NBA playoff bracket: Matchups, schedule as Rockets, Pistons ...](https://www.cbssports.com/nba/news/2026-nba-playoff-bracket-matchups-schedule/).

The Eastern Conference Finals (https://en.wikipedia.org/wiki/NBA_conference_finals) is the final round of the NBA's Eastern Conference playoffs, determining which team advances to the NBA Finals. It is a best-of-seven series between the two remaining Eastern Conference teams.

**Exact later resolution packet**

YES. The resolution criteria are satisfied because the Knicks reached—and were listed in—the 2026 Eastern Conference Finals. The official NBA playoff bracket at https://www.nba.com/playoffs/2026/bracket lists the East Final as “Knicks vs. Cavaliers,” which directly verifies that the Knicks appeared as an Eastern Conference Finals participant, and therefore as a participant in Game 1 of that series [2026 NBA Playoffs | Bracket | webview for app](https://www.nba.com/playoffs/2026/bracket). ESPN’s bracket at https://www.espn.com/nba/playoff-bracket confirms the required path: in the first round, the Knicks defeated the Atlanta Hawks 4-2; in the Eastern Conference Semifinals, the Knicks defeated the Philadelphia 76ers 4-0; and in the Eastern Conference Finals, the Knicks played the Cleveland Cavaliers [https://www.espn.com/nba/playoff-bracket](https://www.espn.com/nba/playoff-bracket). The 2026 NBA playoffs Wikipedia page at https://en.wikipedia.org/wiki/2026_NBA_playoffs corroborates those same results: Knicks over Hawks 4-2 in Round 1, Knicks over 76ers 4-0 in the Eastern Semifinals, and Knicks vs. Cavaliers in the Eastern Conference Finals [https://en.wikipedia.org/wiki/2026_NBA_playoffs](https://en.wikipedia.org/wiki/2026_NBA_playoffs). Because the Knicks were not eliminated before the Eastern Conference Finals began and were an ECF participant, the correct Metaculus resolution is YES = 1.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-164. `e460de92-fe71-5cfc-87f6-5a7c87dfaf4a`

- Present date: `2026-05-03 09:50:23.658304`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-05-27 00:00:00`

**Question**

Will Donald Trump formally endorse a candidate in the Texas Senate Republican primary runoff between May 1, 2026, and the May 26, 2026, election?

**Resolution criteria**

This question resolves **Yes** if Donald Trump issues a formal endorsement of either John Cornyn or Ken Paxton for the Texas Senate Republican primary runoff **on or after May 1, 2026, at 00:00 UTC** and **before May 26, 2026, at 23:59 UTC** (the date of the runoff election).

A "formal endorsement" is defined as an explicit, unambiguous public statement of support naming a specific candidate (e.g., "I endorse [candidate]," "I am giving my Complete and Total Endorsement to [candidate]," or functionally equivalent language), posted via one or more of the following channels:
1. Donald Trump's official Truth Social account (https://truthsocial.com/@realDonaldTrump)
2. An official press release or statement from the White House or Trump's Save America PAC
3. An official statement on Trump's campaign website

Vague praise, expressions of admiration, or non-committal statements (e.g., "He's a great guy") do **not** constitute a formal endorsement.

If no such endorsement is issued by May 26, 2026, at 23:59 UTC, or if Trump endorses only after this deadline, the question resolves **No**.

Resolution will be determined by checking Trump's Truth Social profile (https://truthsocial.com/@realDonaldTrump) and credible news reporting from outlets such as the Texas Tribune (https://www.texastribune.org/), Reuters, AP, or Politico.

**Pre-cutoff background**

The Texas Senate Republican primary runoff is scheduled for May 26, 2026, between incumbent U.S. Senator John Cornyn and Texas Attorney General Ken Paxton. Neither candidate secured more than 50% of the vote in the March 3, 2026, primary, triggering the runoff [Trump stays out of Texas Senate runoff after vowing endorsement](https://www.texastribune.org/2026/04/07/texas-senate-gop-runoff-cornyn-paxton-trump-endorsement/).

On March 4, 2026, the day after the primary, President Donald Trump stated he would be endorsing "soon" in the race. However, as of April 7, 2026, Trump had remained on the sidelines despite both candidates actively courting his support [Trump stays out of Texas Senate runoff after vowing endorsement](https://www.texastribune.org/2026/04/07/texas-senate-gop-runoff-cornyn-paxton-trump-endorsement/). Multiple reports from the Texas Tribune, NBC News, Politico, and The Hill confirm that Trump has repeatedly teased an endorsement but has not issued one.

As of May 1, 2026, Trump has not formally endorsed either Cornyn or Paxton in this race. Polling from mid-April 2026 showed Paxton leading Cornyn by approximately 8 percentage points among likely Republican runoff voters. Trump's endorsement decision is seen as potentially decisive, and his delay has been interpreted as strategic — endorsing could alienate one faction of the Republican base.

**Exact later resolution packet**

YES. The resolution criteria are satisfied. The relevant event occurred on May 19, 2026, which is after May 1, 2026 at 00:00 UTC and before May 26, 2026 at 23:59 UTC. Multiple queried reports state that Donald Trump endorsed Texas Attorney General Ken Paxton in the Texas Republican Senate runoff against incumbent John Cornyn on that date [Trump endorses Ken Paxton in Senate GOP runoff](https://www.texastribune.org/2026/05/19/donald-trump-ken-paxton-endorsement-texas-senate-gop-primary-runoff-cornyn/) [Trump picks Paxton over Cornyn in Texas' GOP Senate primary ...](https://www.houstonpublicmedia.org/articles/news/politics/2026/05/19/552323/ken-paxton-trump-endorsement-texas-senate-republican-primary-runoff-cornyn/) [Trump endorses Paxton in Texas Republican primary, boosting ...](https://www.pbs.org/newshour/politics/trump-endorses-paxton-in-texas-republican-primary-boosting-effort-to-oust-sen-cornyn) [Trump endorses Ken Paxton in Texas Republican Senate runoff](https://cbsaustin.com/news/local/trump-says-he-will-endorse-in-texas-senate-race-by-early-afternoon). The endorsement was for one of the two specified candidates, Ken Paxton [Trump endorses Ken Paxton in Senate GOP runoff](https://www.texastribune.org/2026/05/19/donald-trump-ken-paxton-endorsement-texas-senate-gop-primary-runoff-cornyn/) [Trump picks Paxton over Cornyn in Texas' GOP Senate primary ...](https://www.houstonpublicmedia.org/articles/news/politics/2026/05/19/552323/ken-paxton-trump-endorsement-texas-senate-republican-primary-runoff-cornyn/) [Trump endorses Paxton in Texas Republican primary, boosting ...](https://www.pbs.org/newshour/politics/trump-endorses-paxton-in-texas-republican-primary-boosting-effort-to-oust-sen-cornyn) [Trump endorses Ken Paxton in Texas Republican Senate runoff](https://cbsaustin.com/news/local/trump-says-he-will-endorse-in-texas-senate-race-by-early-afternoon). The language was a formal endorsement, not merely praise: CBS Austin reports that Trump wrote, “Ken Paxton has my Complete and Total Endorsement to be the next United States Senator from the Great State of Texas” [Trump endorses Ken Paxton in Texas Republican Senate runoff](https://cbsaustin.com/news/local/trump-says-he-will-endorse-in-texas-senate-race-by-early-afternoon). Houston Public Media reports the endorsement appeared in a Truth Social post and gives the direct Truth Social URL, https://truthsocial.com/@realDonaldTrump/posts/116602192066577324 [Trump picks Paxton over Cornyn in Texas' GOP Senate primary ...](https://www.houstonpublicmedia.org/articles/news/politics/2026/05/19/552323/ken-paxton-trump-endorsement-texas-senate-republican-primary-runoff-cornyn/). CBS Austin likewise reports that Trump announced the endorsement on Truth Social [Trump endorses Ken Paxton in Texas Republican Senate runoff](https://cbsaustin.com/news/local/trump-says-he-will-endorse-in-texas-senate-race-by-early-afternoon). Truth Social is one of the allowed channels in the question’s criteria. Therefore the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-165. `28286f1c-7ece-5245-9226-e2a8c751bdde`

- Present date: `2026-05-14 02:44:34.061350`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-30T00:00:00`

**Question**

Will the EMA's PRAC conclude that the benefit-risk balance of Ixchiq remains favorable in its June 2026 PSUSA assessment (i.e., no recommendation for suspension or withdrawal)?

**Resolution criteria**

This question resolves based on the official "Meeting highlights from the Pharmacovigilance Risk Assessment Committee (PRAC)" for the June 8–11, 2026 meeting, published on the EMA website (expected URL pattern: https://www.ema.europa.eu/en/news/meeting-highlights-pharmacovigilance-risk-assessment-committee-prac-8-11-june-2026). Only PRAC recommendations regarding the Periodic Safety Update Single Assessment (PSUSA) or equivalent safety review procedure for Ixchiq are relevant.

**Definitions (per EMA terminology):**
- "Favorable benefit-risk balance" means the PRAC concludes that the benefits of Ixchiq continue to outweigh its risks for the approved indication(s), consistent with the EMA's standard PSUSA outcome language (see https://www.ema.europa.eu/en/human-regulatory-overview/post-authorisation/pharmacovigilance-post-authorisation/periodic-safety-update-reports-psurs).
- "Suspension" means a temporary halt of the marketing authorisation, and "withdrawal" means revocation of the marketing authorisation, as defined under EU pharmaceutical legislation.

**Resolution outcomes:**
- **YES**: The June 2026 PRAC meeting highlights state that the benefit-risk balance of Ixchiq remains favorable AND do not recommend suspension or withdrawal of the marketing authorisation. This includes outcomes where PRAC recommends additional contraindications, warnings, or other label changes without recommending suspension or withdrawal.
- **NO**: The June 2026 PRAC meeting highlights recommend the suspension or withdrawal of the marketing authorisation for Ixchiq, OR the PRAC concludes that the benefit-risk balance is no longer favorable.
- **Clarification on new restrictions**: If PRAC recommends only additional restrictions (e.g., new contraindications, updated warnings, additional risk minimisation measures) but does NOT recommend suspension or withdrawal, this resolves **YES**.
- If the June 2026 PRAC meeting highlights are not published by July 1, 2026 (23:59 UTC), or if the PSUSA assessment for Ixchiq is not concluded at the June 2026 meeting, the question resolves **NO**.

All dates and deadlines are in UTC.

**Pre-cutoff background**

Ixchiq is a live attenuated vaccine for the prevention of chikungunya virus disease, developed by Valneva SE. The vaccine has faced escalating regulatory actions across multiple jurisdictions:

- **US withdrawal**: In August 2025, the FDA suspended Ixchiq's biologics license citing serious adverse events. In January 2026, Valneva voluntarily withdrew its BLA and IND applications in the US [https://www.ema.europa.eu/en/news/meeting-highlights-pharmacovigilance-risk-assessment-committee-prac-9-12-march-2026](https://www.ema.europa.eu/en/news/meeting-highlights-pharmacovigilance-risk-assessment-committee-prac-9-12-march-2026).
- **UK restrictions**: In February 2026, the UK's MHRA issued a safety update restricting use of Ixchiq, citing "very rare fatal reactions" and serious adverse events. The vaccine was contraindicated for adults over 60 and individuals with hypertension, cardiovascular disease, diabetes mellitus, or chronic kidney disease [https://www.gov.uk/drug-safety-update/ixchiq-chikungunya-vaccine-updates-to-restrictions-of-use-following-safety-review](https://www.gov.uk/drug-safety-update/ixchiq-chikungunya-vaccine-updates-to-restrictions-of-use-following-safety-review).
- **EU review**: The EMA's Pharmacovigilance Risk Assessment Committee (PRAC) has been actively monitoring Ixchiq's safety. At its March 9–12, 2026 meeting, PRAC reviewed a safety signal regarding aseptic meningitis risk and recommended product information updates [https://www.ema.europa.eu/en/news/meeting-highlights-pharmacovigilance-risk-assessment-committee-prac-9-12-march-2026](https://www.ema.europa.eu/en/news/meeting-highlights-pharmacovigilance-risk-assessment-committee-prac-9-12-march-2026). PRAC is conducting a Periodic Safety Update Single Assessment (PSUSA) for Ixchiq, scheduled to conclude at the June 2026 PRAC meeting (June 8–11, 2026) [[PDF] PRAC meeting dates 2025-2026 - EMA - European Union](https://www.ema.europa.eu/en/documents/other/prac-meetings-2025-and-2026_en.pdf) [https://www.ema.europa.eu/en/news/meeting-highlights-pharmacovigilance-risk-assessment-committee-prac-9-12-march-2026](https://www.ema.europa.eu/en/news/meeting-highlights-pharmacovigilance-risk-assessment-committee-prac-9-12-march-2026).

The key question is whether EU regulators will diverge from US and UK actions or follow a similar path of restricting/withdrawing the vaccine. The EU has historically been more deliberative but also cautious in pharmacovigilance decisions.

**Exact later resolution packet**

RESOLUTION: YES (1).

RESOLUTION SOURCE: The official "Meeting highlights from the Pharmacovigilance Risk Assessment Committee (PRAC) 8-11 June 2026," published on the EMA website (https://www.ema.europa.eu/en/news/meeting-highlights-pharmacovigilance-risk-assessment-committee-prac-8-11-june-2026), dated 2026-06-12 [9a2d0c, 6a70e2]. This matches exactly the URL pattern specified in the resolution criteria and was published well before the July 1, 2026 23:59 UTC deadline.

WHAT PRAC DECIDED ON IXCHIQ: The verbatim Ixchiq section states: "Ixchiq: use should be restricted to people at high risk of chikungunya infection. The PRAC has recommended that the chikungunya vaccine Ixchiq should be restricted to individuals with a high risk of becoming infected with the chikungunya virus... This restriction of the indication follows a routine EMA review of available safety data which evaluated the impact of serious adverse events reported with the vaccine (including aseptic meningitis...) on the benefit-risk balance of Ixchiq." PRAC also endorsed a Direct Healthcare Professional Communication (DHPC) and reaffirmed the existing contraindication (immunocompromised patients) and no co-administration with other vaccines. The recommendation is to be sent to the CHMP for the Agency opinion [6a70e2]. Medscape independently confirms PRAC recommended restricting use to high-risk individuals aged 12+, not suspension/withdrawal [a0d5d8].

CHECKLIST VERIFICATION:
1. Published by deadline: YES — highlights published 2026-06-12, before 2026-07-01 [9a2d0c, 6a70e2].
2. PSUSA / equivalent safety review concluded: YES — PRAC concluded its "routine EMA review of available safety data" of the benefit-risk balance and issued a final recommendation (restriction of indication) forwarded to CHMP. The resolution criteria treat the "PSUSA or equivalent safety review procedure" as relevant; the review that the March 2026 highlights said "will conclude in June 2026" concluded with this recommendation [6a70e2].
3. Words "suspension"/"withdrawal": ABSENT from the Ixchiq section. PRAC did NOT recommend suspension or withdrawal of the marketing authorisation [6a70e2].
4. Additional restrictions vs. suspension/withdrawal: The outcome was restriction of the indication (limit to high-risk individuals) plus a DHPC — i.e., an "additional restriction," which the resolution criteria's clarification explicitly states resolves YES ("If PRAC recommends only additional restrictions... but does NOT recommend suspension or withdrawal, this resolves YES") [6a70e2].
5. Explicit word "favourable"/"favorable": The EMA text did NOT literally use the word "favourable" in the Ixchiq section [6a70e2]. However, this does not trigger a NO. Under the resolution criteria, NO requires that PRAC either recommend suspension/withdrawal OR "concludes that the benefit-risk balance is no longer favorable." Neither occurred: PRAC kept the marketing authorisation in force and merely restricted the indication, which under standard EMA logic means the benefit-risk balance remains favourable for the restricted (high-risk) population. Had PRAC found the benefit-risk balance no longer favourable, it would have recommended suspension/withdrawal.

CONCLUSION: The highlights were published on time, the review concluded, no suspension or withdrawal was recommended, and PRAC recommended only additional restrictions (restricted indication + DHPC). All YES conditions are met; no NO condition is met. Resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-166. `2c9b968c-ac22-5353-8eb4-8b29c572ec63`

- Present date: `2026-04-30 11:45:09.639334`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will any activist investor win a majority of their nominated board seats in a contested shareholder vote at a U.S. public company between April 29 and June 1, 2026?

**Resolution criteria**

This question resolves YES if, between April 29, 2026, 00:00 UTC and June 1, 2026, 23:59 UTC (inclusive), at least one activist investor wins more than 50% of the board seats they specifically nominated candidates for in their proxy statement, in a contested director election that proceeds to a formal shareholder vote at an Annual General Meeting (AGM) or Special Meeting of a U.S. public company. It resolves NO otherwise.

Definitions:
- **Activist investor**: Any person or entity that has filed an SEC Schedule 13D (https://www.sec.gov/about/forms/form13d.htm) with respect to the target company, or that has filed definitive proxy solicitation materials (DFAN14A or DEFC14A) with the SEC nominating an alternative slate of director candidates.
- **Contested shareholder vote**: A director election where shareholders vote on competing slates of nominees from both management and the activist. Seats obtained through settlements (i.e., agreements where the company adds activist nominees to its own slate without a contested vote), or through withdrawal of management nominees prior to the vote such that the activist's nominees run unopposed, do NOT count.
- **Majority**: The activist wins more than 50% of the board seats they specifically nominated candidates for in their definitive proxy filing. For example, if an activist nominates 3 candidates for 3 seats, they must win at least 2. If they nominate 1 candidate for 1 seat, they must win that seat.
- **U.S. public company**: A company whose common stock is listed on the New York Stock Exchange (NYSE) or the Nasdaq Stock Market (https://en.wikipedia.org/wiki/Nasdaq).

**Resolution source**: SEC Form 8-K filings reporting the results of the shareholder meeting (searchable at https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&type=8-K), or credible reporting from Insightia (formerly Activist Insight), Diligent, Reuters, Bloomberg, The Wall Street Journal, or The Activist Investor (https://theactivistinvestor.substack.com/).

**Pre-cutoff background**

The 2026 proxy season is shaped by the SEC's Universal Proxy Card (UPC) rules, which have been mandatory since September 1, 2022. These rules allow shareholders to mix and match nominees from both management and dissident slates on a single ballot, fundamentally changing the dynamics of contested director elections.

Key data points on activist success rates:
- Under UPC rules, activists have gained at least one board seat in 48% of contested elections that go to a vote [How Three Years of the SEC's Universal Proxy Card Have Changed ...](https://corpgov.law.harvard.edu/2025/09/09/how-three-years-of-the-secs-universal-proxy-card-have-changed-proxy-contests/).
- However, shareholders have supported at least half of the dissident slate in only 24% of UPC elections [How Three Years of the SEC's Universal Proxy Card Have Changed ...](https://corpgov.law.harvard.edu/2025/09/09/how-three-years-of-the-secs-universal-proxy-card-have-changed-proxy-contests/).
- Activist "clean sweeps" (winning all nominated seats) have effectively vanished under UPC, falling from 29% of pre-UPC contests to near zero [How Three Years of the SEC's Universal Proxy Card Have Changed ...](https://corpgov.law.harvard.edu/2025/09/09/how-three-years-of-the-secs-universal-proxy-card-have-changed-proxy-contests/).
- In H1 2025, activist investors sought 216 director seats and secured 112 (a 52% success rate), though the vast majority of these were obtained via settlements rather than contested votes.
- Most activist campaigns (~92% of board seats won) are resolved through settlements rather than contested proxy fights.

As of April 20, 2026, The Activist Investor reported tracking eleven pending proxy contests for the 2026 season, with four having AGMs scheduled for April or May 2026 and the remaining seven expected between May and July 2026 [UPCs We're Tracking - 4/20/26 - The Activist Investor](https://theactivistinvestor.substack.com/p/upcs-were-tracking-42026). Given that multiple contests are scheduled within the resolution window, there are several opportunities for an activist majority win, but the historical base rate under UPC rules makes this a genuinely uncertain outcome.

**Exact later resolution packet**

Adjudicated: At Ingles Markets (Nasdaq: IMKTA) 2026 Annual Meeting on April 30, 2026 (within the April 29-June 1 window), activist Summer Road LLC, which filed DEFC14A/DFAN14A nominating exactly one candidate (Rory A. Held) for a contested Class A board seat, won that seat in a genuinely contested vote against management nominees Rebekah Lowe and Dwight Jacobs (Held: 9,014,729 for vs 3,634,207 withheld; ~62% of shares outstanding). Management did not withdraw nominees and there was no settlement, so it was a formal contested shareholder vote. Summer Road nominated 1 candidate and won 1 seat = 100% > 50% of nominated seats, satisfying all criteria. An initial automated pass resolved NO only because it relied on paywalled Activist Investor text and missed the Ingles contest.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-167. `dbb6b42c-5bd0-5fe2-90ea-353d0f18534f`

- Present date: `2026-05-03 03:23:37.208245`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will a major Libyan oil terminal declare Force Majeure or halt crude oil exports for at least 48 hours due to a blockade or politically motivated shutdown between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves as **YES** if, at any point between 00:00 UTC on May 1, 2026, and 23:59 UTC on June 1, 2026, one or more of the following major Libyan oil terminals experiences an export halt lasting at least 48 consecutive hours due to a blockade, politically motivated shutdown, militia action, or labor strike:

- **Es Sider** (export capacity ~300,000 bpd)
- **Ras Lanuf** (export capacity ~220,000 bpd)
- **Zueitina** (export capacity ~70,000 bpd)
- **Brega** (export capacity ~60,000 bpd)
- **Mellitah** (export capacity ~100,000 bpd)
- **Zawiya** (export capacity ~120,000 bpd)
- **Hariga** (export capacity ~110,000 bpd)

A qualifying "blockade or shutdown" is defined as one of the following:
1. A formal declaration of Force Majeure by the National Oil Corporation (NOC) at any of the listed terminals; **OR**
2. A halt to crude oil loading/export operations at any of the listed terminals for at least 48 consecutive hours, caused by militia action, political directives, tribal blockades, or labor strikes—as confirmed by credible reporting.

**Exclusions:** Routine maintenance shutdowns and weather-related closures (e.g., storm suspensions) do NOT qualify.

The blockade or shutdown must occur or be in effect on or after 00:00 UTC May 1, 2026, and on or before 23:59 UTC June 1, 2026. Events that began before May 1 count only if they are still ongoing as of May 1.

**Resolution source:** Reporting from the National Oil Corporation of Libya (https://noc.ly) or credible international energy news desks, specifically Reuters Energy (https://www.reuters.com/business/energy/) or Bloomberg Energy (https://www.bloomberg.com/energy). At least one credible source must confirm the event for YES resolution. If no such reporting exists by 23:59 UTC June 1, 2026, the question resolves **NO**.

**Pre-cutoff background**

Libya's oil sector remains highly vulnerable to politically motivated disruptions despite recent progress toward national unity. As of April 2026, Libya's oil production has reached approximately 1.43 million barrels per day (bpd), the highest level in over a decade, with ambitions to reach 1.6 million bpd by end of 2026 [Libya approves first unified budget in more than a decade - Al Jazeera](https://www.aljazeera.com/news/2026/4/11/libya-approves-first-unified-budget-in-more-than-a-decade). On April 11, 2026, Libya's rival legislative bodies—the eastern-based House of Representatives and the Tripoli-based High Council of State—approved a unified state budget (190 billion dinars) for the first time in over 13 years, a US-mediated agreement intended to restore financial stability [Libya approves first unified budget in more than a decade - Al Jazeera](https://www.aljazeera.com/news/2026/4/11/libya-approves-first-unified-budget-in-more-than-a-decade).

However, significant tensions persist. Forces loyal to Khalifa Haftar's Libyan National Army (LNA) continue to control key oil export terminals along the northeastern coast and major southern oilfields [Libya approves first unified budget in more than a decade - Al Jazeera](https://www.aljazeera.com/news/2026/4/11/libya-approves-first-unified-budget-in-more-than-a-decade). Oil blockades have been repeatedly used as political leverage—most recently, in March 2026, the El Feel oilfield experienced a shutdown after the NOC redirected pipeline flows from the Sharara field due to pipeline damage [Libya's El Feel oilfield in shutdown since Thursday, engineers say](https://www.reuters.com/world/africa/libyas-el-feel-oilfield-shutdown-since-thursday-engineers-say-2026-03-23/). In August 2024, Libya's eastern government ordered a complete shutdown of all oil fields over a dispute involving the Central Bank. Weather-related closures at terminals including Brega, Ras Lanuf, and Zueitina have also occurred in recent months.

The unified budget agreement could either stabilize the situation by addressing oil revenue distribution grievances, or generate new friction if implementation falters—particularly regarding how oil revenues are allocated between eastern and western administrations. The fragility of Libya's political arrangements means that any perceived breach of the budget deal could trigger renewed oil infrastructure disruptions as a pressure tactic.

**Exact later resolution packet**

Adjudicated: Zawiya is an explicitly listed terminal and is Libya's second-largest crude export terminal (exporting Sharara crude), not merely a refinery. On Friday May 8, 2026, after armed clashes/heavy shelling (qualifying militia-action cause, not weather/maintenance), the operator 'shut the plant completely and evacuate all tankers from the port,' halting crude loading/export operations at the listed terminal; Reuters (carried by Al Jazeera) and Ecofin consistently describe a 'two-day shutdown' from Friday's early hours until full operations resumed Sunday May 10, meeting the 48-consecutive-hour threshold within the May 1-June 1 window. An initial automated resolution wrongly treated this as refinery-only and missed that the port/crude loading halted via the tanker evacuation; confidence is medium because exact Sunday resumption hour is not pinned down and one outlier summary framed it as ~24h.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-168. `d07718c9-f06d-5080-a5a7-afa1043ed3e7`

- Present date: `2026-05-03 12:33:30.025865`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the U.S. Trade Representative initiate a Section 301 investigation targeting Vietnam's intellectual property practices by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the Office of the United States Trade Representative (USTR) formally initiates a Section 301 investigation — as defined under [Section 301 of the Trade Act of 1974](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title19-section2411&num=0&edition=prelim) — specifically targeting Vietnam's **intellectual property practices** (as opposed to other trade issues such as currency, timber, forced labor, or industrial overcapacity), on or after May 2, 2026, and on or before June 1, 2026, at 11:59 PM UTC.

A Section 301 investigation is a formal trade enforcement proceeding initiated by the USTR to examine whether the acts, policies, or practices of a foreign country are unreasonable, unjustifiable, or discriminatory and burden or restrict U.S. commerce.

Formal initiation is established by one or more of the following:
1. Publication of a notice of initiation in the [Federal Register](https://www.federalregister.gov/), or
2. The investigation appearing on the USTR's official [Section 301 Investigations page](https://ustr.gov/issue-areas/enforcement/section-301-investigations), or
3. An official USTR press release at [ustr.gov](https://ustr.gov/about/policy-offices/press-office/press-releases/2026) explicitly announcing the initiation of such an investigation.

If no such initiation is confirmed by any of these sources by 11:59 PM UTC on June 1, 2026, the question resolves **No**.

**Pre-cutoff background**

On April 30, 2026, the Office of the United States Trade Representative (USTR) released its 2026 Special 301 Report, designating Vietnam as a "Priority Foreign Country" (PFC) — the first such designation in 13 years — due to concerns about the adequacy and effectiveness of Vietnam's intellectual property (IP) protection and enforcement [USTR Releases 2026 Special 301 Report on Intellectual Property ...](https://ustr.gov/about/policy-offices/press-office/press-releases/2026/april/ustr-releases-2026-special-301-report-intellectual-property-protection-and-enforcement). The USTR stated it "will decide within 30 days whether to initiate an investigation under Section 301 of the Trade Act of 1974 based on the grounds identified in this report as the basis for Vietnam's identification as a PFC" [USTR Releases 2026 Special 301 Report on Intellectual Property ...](https://ustr.gov/about/policy-offices/press-office/press-releases/2026/april/ustr-releases-2026-special-301-report-intellectual-property-protection-and-enforcement).

As of May 2, 2026, the USTR's Section 301 investigations page lists no active investigation targeting Vietnam's IP practices [Section 301 Investigations | United States Trade Representative](https://ustr.gov/issue-areas/enforcement/section-301-investigations). Existing Vietnam-related Section 301 investigations cover only currency and timber issues (both initiated October 2, 2020) [Section 301 Investigations | United States Trade Representative](https://ustr.gov/issue-areas/enforcement/section-301-investigations).

A [Section 301 investigation](https://ustr.gov/issue-areas/enforcement/section-301-investigations) is a trade enforcement tool under [Section 301 of the Trade Act of 1974](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title19-section2411&num=0&edition=prelim) that allows the USTR to investigate and take action against foreign trade practices that are unreasonable, unjustifiable, or discriminatory and burden U.S. commerce.

The 30-day decision window from April 30 means the USTR is expected to announce its decision by approximately May 30, 2026. The Trump administration faces competing incentives: enforcing IP protections for U.S. industries versus maintaining the strategic U.S.-Vietnam relationship, which has been elevated in recent years partly as a counterbalance to China.

**Exact later resolution packet**

The question resolves YES.

ANTECEDENT/SUBJECT: The question asks whether USTR formally initiated a Section 301 investigation specifically targeting Vietnam's intellectual property practices, on or after May 2, 2026 and on or before June 1, 2026 (11:59 PM UTC).

EVIDENCE FROM PERMITTED SOURCES:

1. USTR Official Press Release (permitted source #3): The press release titled "USTR Announces Section 301 Investigation of Vietnam's Acts, Policies, and Practices Related to Intellectual Property Protection and Enforcement" (https://ustr.gov/about/policy-offices/press-office/press-releases/2026/may/ustr-announces-section-301-investigation-vietnams-acts-policies-and-practices-related-intellectual) explicitly states U.S. Trade Representative Jamieson Greer initiated an investigation of Vietnam under Section 301 of the Trade Act of 1974, following the April 30 Special 301 priority foreign country (PFC) identification [USTR Announces Section 301 Investigation of Vietnam's Acts ...](https://ustr.gov/about/policy-offices/press-office/press-releases/2026/may/ustr-announces-section-301-investigation-vietnams-acts-policies-and-practices-related-intellectual).

2. USTR Federal Register Notice / FRN (permitted source #1): The official Initiation notice (Docket No. USTR-2026-0364), "Initiation of Section 301 Investigation and Request for Public Comments: Vietnam's Acts, Policies, and Practices Related to Intellectual Property Protection and Enforcement" (https://ustr.gov/sites/default/files/files/Press/Releases/2026/USTR%20301%20Vietnam%20IP%20FRN.pdf), states under DATES: "May 29, 2026: The Trade Representative initiated a Section 301 investigation," and confirms the investigation concerns "the acts, policies, and practices of Vietnam related to IP protection and enforcement that resulted in the priority foreign country identification" [[PDF] Billing Code 3390-F4 - USTR](https://ustr.gov/sites/default/files/files/Press/Releases/2026/USTR%20301%20Vietnam%20IP%20FRN.pdf).

TIMING: The initiation date of May 29, 2026, falls strictly within the resolution window (after May 2, 2026, and before June 1, 2026 at 11:59 PM UTC).

SUBJECT MATCH: The investigation explicitly targets Vietnam's intellectual property protection and enforcement — not currency, timber, forced labor, or industrial overcapacity. This is distinct from the pre-existing Vietnam currency and timber Section 301 investigations (both initiated October 2, 2020) that appear on the USTR Section 301 Investigations page [https://ustr.gov/issue-areas/enforcement/section-301-investigations](https://ustr.gov/issue-areas/enforcement/section-301-investigations), and is distinct from the April 30, 2026 Special 301 Report PFC designation (the designation triggered, but is separate from, the formal Section 301 investigation initiation).

CONCLUSION: A Section 301 investigation specifically targeting Vietnam's IP practices was formally initiated on May 29, 2026, confirmed by both an official USTR press release and the USTR Federal Register initiation notice. The question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-169. `6d7c9797-78c1-550a-a478-41bca8e1233d`

- Present date: `2026-05-01 15:57:35.115126`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Netflix announce an agreement to broadcast additional NFL regular-season or playoff games beyond its existing Christmas Day package by June 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after April 30, 2026 (12:00 AM UTC) and by 11:59 PM UTC on June 1, 2026, an official announcement confirms that Netflix has secured rights to broadcast additional live NFL regular-season or playoff games beyond its existing 2026 Christmas Day package (currently two games on December 25, 2026).

**Definition of "expanded partnership":** Netflix must acquire rights to at least one additional live NFL regular-season or playoff game that is not part of its existing Christmas Day package. Renewals or extensions of the Christmas Day package alone do not qualify. Non-game content (e.g., documentaries, highlight shows) does not qualify.

**Valid announcement format:** The announcement must take one of the following forms:
1. An official corporate press release published on the Netflix Newsroom (https://about.netflix.com/en/newsroom) or NFL Communications site (https://nflcommunications.com/); OR
2. An SEC filing by Netflix, Inc.; OR
3. A statement from a named Netflix or NFL spokesperson reported by at least one of the following: The Wall Street Journal, The New York Times, Reuters, AP, Bloomberg, CNBC, ESPN, or Variety.

If no qualifying announcement is made by 11:59 PM UTC on June 1, 2026, the question resolves NO.

**Pre-cutoff background**

Netflix currently holds a three-year deal (2024–2026) to broadcast NFL games on Christmas Day, worth a reported $150 million. For the 2026 season (the final year of this deal), Netflix will stream two Christmas Day games, with Fox televising a third [https://www.forbes.com/sites/rickellis/2026/04/17/netflix-emphasizes-importance-of-live-sports-nfl-game-rights/](https://www.forbes.com/sites/rickellis/2026/04/17/netflix-emphasizes-importance-of-live-sports-nfl-game-rights/).

As of April 2026, Netflix is actively seeking to expand this relationship. On March 30, 2026, The Wall Street Journal reported that Netflix wants to double its NFL package from two to four games, specifically targeting the league's new Thanksgiving Eve game and an international game [Netflix seeks to add more NFL games as league renegotiates media ...](https://nypost.com/2026/03/30/sports/netflix-seeks-four-game-nfl-package-as-league-renegotiates-media-rights-deals/) [Netflix Wants To Expand Its NFL Package - Report - Deadline](https://deadline.com/2026/03/netflix-wants-to-expand-nfl-package-thanksgiving-game-1236769618/). The NFL is currently renegotiating its media rights, creating smaller packages of four or five games available to streaming services. A five-game package became available following an equity deal between the NFL and ESPN [https://www.forbes.com/sites/rickellis/2026/04/17/netflix-emphasizes-importance-of-live-sports-nfl-game-rights/](https://www.forbes.com/sites/rickellis/2026/04/17/netflix-emphasizes-importance-of-live-sports-nfl-game-rights/).

During Netflix's Q1 2026 earnings call on April 16, 2026, co-CEO Ted Sarandos confirmed the company is "currently in discussions with the NFL to expand the relationship" [https://www.forbes.com/sites/rickellis/2026/04/17/netflix-emphasizes-importance-of-live-sports-nfl-game-rights/](https://www.forbes.com/sites/rickellis/2026/04/17/netflix-emphasizes-importance-of-live-sports-nfl-game-rights/). Netflix Chief Content Officer Bela Bajaria has also stated the company is "always going to have the conversation" with the NFL regarding new packages [Netflix Wants To Expand Its NFL Package - Report - Deadline](https://deadline.com/2026/03/netflix-wants-to-expand-nfl-package-thanksgiving-game-1236769618/). However, no formal agreement has been announced as of April 30, 2026. YouTube and Fox are also reportedly competing for parts of the available game packages.

**Exact later resolution packet**

The question resolves YES.

Antecedent/criteria: A qualifying official announcement between April 30, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC) confirming Netflix secured rights to at least one additional live NFL regular-season or playoff game beyond its existing 2026 Christmas Day package.

Evidence: On Wednesday, May 13, 2026, Netflix and the NFL officially announced an expanded, extended media-rights deal (through the 2029-30 season). Under it, Netflix gains rights to three additional regular-season game windows annually — a Week 1 game (the 49ers vs. Rams game in Australia for 2026), a new Thanksgiving Eve game (Packers at Rams, Nov. 25, 2026), and a Week 18 regular-season finale — plus the NFL Honors, in addition to Christmas Day inventory [e740b4]. This was reported by Sports Media Watch, which states "Netflix officially announced Wednesday" the acquisition of three additional NFL game windows [e740b4].

This is corroborated across multiple qualifying outlets dated May 13, 2026, including Variety ("Netflix Will Stream Five NFL Games", variety.com/2026/tv/news/netflix-stream-five-nfl-games-pro-football-1236747637/), The Wall Street Journal ("Netflix Secures Three More Football Games in New NFL Deal", wsj.com/business/media/netflix-secures-three-more-football-games-in-new-nfl-deal-7a7902c7), The New York Times/The Athletic (nytimes.com/athletic/7276673/2026/05/13/nfl-netflix-streaming-five-games-christmas/), and the NFL's own site (nfl.com/news/packers-rams-thanksgiving-eve-netflix-2026-nfl-schedule-release).

The announcement date (May 13, 2026) falls squarely within the required window (April 30 – June 1, 2026). The games added (Week 1, Thanksgiving Eve, Week 18) are live NFL regular-season games beyond the Christmas Day package, satisfying the "expanded partnership" definition. It is a secured, signed deal — not mere negotiations. Multiple listed news outlets (Variety, WSJ, NYT, ESPN) reported it, and the NFL publicly announced the matchups as part of the 2026 schedule release.

Therefore all resolution criteria are met and the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-170. `30b103ad-7768-5300-b210-eca632d24d04`

- Present date: `2026-05-02 17:36:43.132791`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the Illinois Senate pass HB 5511 (Children's Social Media Safety Act) by June 1, 2026?

**Resolution criteria**

This question resolves YES if, according to the official bill status page for HB 5511 on the Illinois General Assembly website (https://www.ilga.gov/legislation/BillStatus.asp?DocNum=5511&GAID=18&DocTypeID=HB&LegId=167486&SessionID=114&GA=104), the Illinois Senate passes HB 5511 on or after May 1, 2026 (12:00 AM CT) and by June 1, 2026 (11:59 PM CT).

"Passing" is defined as the bill successfully receiving a majority vote on Third Reading (the final floor vote) in the Illinois Senate. This includes passage of the bill in identical form to the House-passed version OR passage of an amended version (i.e., a Senate amendment that would then require House concurrence still counts as the Senate "passing" the bill for the purposes of this question).

The question resolves NO if the bill has not achieved a successful Third Reading vote in the Senate by 11:59 PM CT on June 1, 2026, regardless of reason (e.g., still in committee, failed vote, tabled, or not called for a vote).

**Pre-cutoff background**

HB 5511, the Children's Social Media Safety Act, would require online platforms and operating system providers to implement age verification and restrict addictive algorithmic features for users identified as minors. The bill was introduced in the Illinois House and passed on April 16, 2026, with a vote of 82-27-0 [https://www.ilga.gov/legislation/BillStatus.asp?DocNum=5511&GAID=18&DocTypeID=HB&LegId=167486&SessionID=114&GA=104](https://www.ilga.gov/legislation/BillStatus.asp?DocNum=5511&GAID=18&DocTypeID=HB&LegId=167486&SessionID=114&GA=104). It arrived in the Illinois Senate on April 21, 2026, where it underwent its first reading and was referred to the Assignments Committee. On April 28, 2026, it was assigned to the Senate Executive Committee, and on April 29, 2026, the alternate chief sponsor was changed to Sen. Laura Ellman [https://www.ilga.gov/legislation/BillStatus.asp?DocNum=5511&GAID=18&DocTypeID=HB&LegId=167486&SessionID=114&GA=104](https://www.ilga.gov/legislation/BillStatus.asp?DocNum=5511&GAID=18&DocTypeID=HB&LegId=167486&SessionID=114&GA=104).

As of May 1, 2026, the bill is pending in the Senate Executive Committee and has not yet received a committee hearing or vote in the Senate. The Illinois General Assembly's spring session typically runs through May 31. For the bill to pass the Senate, it must clear the Executive Committee and then pass a Third Reading floor vote. The bill is a priority of Gov. JB Pritzker, which may accelerate its progress, but the roughly five-week window before June 1 creates meaningful uncertainty about whether the Senate will act in time.

Primary resolution source: Illinois General Assembly bill status page at https://www.ilga.gov/legislation/BillStatus.asp?DocNum=5511&GAID=18&DocTypeID=HB&LegId=167486&SessionID=114&GA=104

**Exact later resolution packet**

The official Illinois General Assembly bill status page for HB 5511 confirms that the Illinois Senate passed the bill on Third Reading on June 1, 2026, with a vote of 057-000-000 [709bb2].

Key Senate action history from the official bill status page (https://www.ilga.gov/legislation/BillStatus.asp?DocNum=5511&GAID=18&DocTypeID=HB&LegId=167486&SessionID=114&GA=104) [709bb2]:
- 4/21/2026: Arrived in Senate; First Reading; Referred to Assignments.
- 4/28/2026: Assigned to Executive Committee.
- 5/27/2026: Senate Committee Amendment No. 1 adopted; Do Pass as Amended; Second Reading.
- 5/30/2026: Senate Floor Amendment No. 2 filed/recommended.
- 6/01/2026: Recalled to Second Reading; Floor Amendment No. 2 adopted; Third Reading – Passed (057-000-000).

This satisfies the resolution criteria:
1. The vote was a successful Third Reading (final floor vote) in the Senate — not a mere committee vote.
2. It occurred on June 1, 2026, which is on or after May 1, 2026 (12:00 AM CT) and no later than June 1, 2026 (11:59 PM CT).
3. Although the bill was amended in the Senate (Committee Amendment No. 1 and Floor Amendment No. 2), the resolution criteria explicitly state that passage of an amended version still counts as YES.

Therefore the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-171. `f573c286-e681-5094-83da-c5a340b0858a`

- Present date: `2026-05-03 05:05:09.219578`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will a backdoored package with over 1 million cumulative downloads be discovered on npm or PyPI and publicly reported between May 1 and May 31, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 1, 2026 (00:00 UTC) and before June 1, 2026 (00:00 UTC), at least one package hosted on npm (npmjs.com) or PyPI (pypi.org) is publicly reported as containing a backdoor and has over 1,000,000 cumulative (all-time) downloads at the time of reporting.

**Definition of "backdoor":** Per the NIST Computer Security Resource Center glossary (https://csrc.nist.gov/glossary/term/backdoor), a backdoor is "an undocumented way of gaining access to a computer system" or "a malicious program that listens for commands on a certain Transmission Control Protocol (TCP) or User Datagram Protocol (UDP) port" [https://csrc.nist.gov/glossary/term/backdoor](https://csrc.nist.gov/glossary/term/backdoor). For the purposes of this question, a package is considered "backdoored" if it was modified—whether through account compromise, malicious update, or code injection—to include unauthorized code that enables remote access, data exfiltration, or command execution, consistent with the NIST definition.

**Cumulative downloads verification:** The cumulative (all-time) download count must exceed 1,000,000 as verified by PePy.tech (https://pepy.tech/) for PyPI packages or npm-stat (https://npm-stat.com/) for npm packages, measured at the time the compromise is publicly reported.

**Public reporting requirement:** The discovery must be reported by at least one of the following credible sources:
- Official security advisories from npm or PyPI
- GitHub Security Advisories (https://github.com/advisories)
- BleepingComputer (https://www.bleepingcomputer.com/)
- The Hacker News (https://thehackernews.com/)
- Snyk vulnerability database (https://security.snyk.io/)
- Socket.dev security alerts

The report must be published on or after May 1, 2026 (00:00 UTC). The compromise itself may have been introduced before May 1, 2026, but the public discovery and report must fall within the resolution window. If no qualifying report is found by June 1, 2026, the question resolves **No**.

**Pre-cutoff background**

Supply chain attacks targeting open-source package repositories like npm and PyPI have escalated significantly in recent years. Attackers compromise popular packages—either by hijacking maintainer accounts or injecting malicious code into legitimate updates—to distribute malware to downstream users.

Recent high-profile incidents include:
- In April 2026, the PyPI package `elementary-data`, with 1.1 million monthly downloads, was compromised to push an infostealer [PyPI package with 1.1M monthly downloads hacked to push ...](https://www.bleepingcomputer.com/news/security/pypi-package-with-11m-monthly-downloads-hacked-to-push-infostealer/).
- In September 2025, a self-replicating worm ("Shai-Hulud") compromised over 500 npm packages including @ctrl/tinycolor in what was called the largest npm supply chain attack in history.
- In March 2026, the LiteLLM PyPI package was compromised.
- In April 2026, 36 malicious npm Strapi-plugin packages were discovered.

Compromises affecting packages with over 1 million cumulative downloads occur with some regularity—roughly every few months—but not predictably on a monthly basis. The `elementary-data` incident in late April 2026 [PyPI package with 1.1M monthly downloads hacked to push ...](https://www.bleepingcomputer.com/news/security/pypi-package-with-11m-monthly-downloads-hacked-to-push-infostealer/) demonstrates that such events are plausible within any given month, but the specific 1 million cumulative download threshold and the one-month window create meaningful uncertainty. Detection capabilities have improved with tools from Snyk, Socket, and others, which increases the likelihood of discovery but does not guarantee a high-download-count package will be found compromised in any specific month.

**Exact later resolution packet**

The question resolves YES.

EVIDENCE:
1. PUBLIC REPORT WITHIN WINDOW: BleepingComputer published an article titled "Backdoored PyTorch Lightning package drops credential stealer" on May 4, 2026 — within the resolution window (May 1, 2026 00:00 UTC to June 1, 2026 00:00 UTC) [b09d39]. BleepingComputer is one of the explicitly listed credible sources. The same incident was also covered by Socket.dev ("PyTorch Lightning PyPI Package Compromised in Supply Chain Attack") [85baff].

2. PACKAGE ON PyPI: The compromised package is `pytorch-lightning` (and the related `lightning` package), both hosted on PyPI [b09d39, 85baff].

3. BACKDOOR (NIST definition): The article describes a hidden execution chain that, upon import, downloads and executes a payload that performs data exfiltration (stealing API keys, secrets, environment files, tokens, cloud secrets) and supports arbitrary system command execution [b09d39, 85baff]. This satisfies the question's definition of a backdoor (unauthorized code enabling remote access, data exfiltration, or command execution).

4. OVER 1 MILLION CUMULATIVE DOWNLOADS (verified via PePy.tech): PePy.tech reports the cumulative all-time download count for `pytorch-lightning` as 334,739,023 [6b5ad9], and for the `lightning` package as 102,698,787 [99c046]. Both vastly exceed the 1,000,000 cumulative download threshold. The BleepingComputer article additionally notes more than 11 million downloads in the prior month alone [b09d39].

All resolution criteria are met: a backdoored PyPI package with over 1 million cumulative downloads (verified on PePy.tech) was publicly reported by a listed credible source (BleepingComputer/Socket.dev) within the May 2026 window.

URLs:
- Report: https://www.bleepingcomputer.com/news/security/backdoored-pytorch-lightning-package-drops-credential-stealer/
- Report: https://socket.dev/blog/lightning-pypi-package-compromised
- Download verification: https://pepy.tech/projects/pytorch-lightning and https://pepy.tech/projects/lightning

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-172. `a86f4c65-494a-5e5a-aafc-e9b446ba2e40`

- Present date: `2026-05-01 17:44:43.821467`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Google enable C2PA Content Credentials verification for external images in the Gemini app by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after April 30, 2026, and by 23:59 UTC on June 1, 2026, Google officially announces or makes available a feature in the public-facing Gemini app (web or mobile, accessible at https://gemini.google.com/ or via the official mobile apps) that allows users to verify C2PA Content Credentials on images — specifically, the ability to check the provenance of content created by models or products outside of Google's own ecosystem.

An "announcement" or "integration" is defined as any of the following:
1. An official blog post on Google's "The Keyword" blog (https://blog.google/) describing the feature as launched or rolling out.
2. A mention in official Gemini release notes or Google support documentation confirming the feature is live.
3. A functional, user-accessible UI element in the Gemini app that performs C2PA verification on uploaded or linked images, as confirmed by credible technology news outlets (e.g., The Verge at https://www.theverge.com/, TechCrunch at https://techcrunch.com/, or Reuters at https://www.reuters.com/).

The February 26, 2026 "Nano Banana 2" blog post (https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/) and the November 20, 2025 blog post (https://blog.google/innovation-and-ai/products/ai-image-verification-gemini-app/), which announced future plans but did not launch the feature, do NOT count toward resolution.

If the feature is only available via API, limited to enterprise/developer platforms, or only applies to Google-generated content (which already has C2PA metadata embedded), it does not resolve Yes.

This question resolves **No** if no such announcement or feature launch is confirmed by 23:59 UTC on June 1, 2026.

**Pre-cutoff background**

On November 20, 2025, Google published a blog post titled "How we're bringing AI image verification to the Gemini app," which announced that C2PA metadata would be embedded in images generated by Google's own models (e.g., Nano Banana Pro) in the Gemini app [How we're bringing AI image verification to the Gemini app](https://blog.google/innovation-and-ai/products/ai-image-verification-gemini-app/). The post also stated: "Over time, we will also extend our verification approach to support C2PA content credentials, meaning you'll be able to check the original source of content created by models and products that exist outside of Google's ecosystem" [How we're bringing AI image verification to the Gemini app](https://blog.google/innovation-and-ai/products/ai-image-verification-gemini-app/).

On February 26, 2026, Google published the "Nano Banana 2" blog post, which reiterated: "We'll soon be bringing C2PA verification to the Gemini app, too" [https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/). This confirmed that as of that date, C2PA verification (as distinct from embedding) had not yet launched in the Gemini app.

As of April 30, 2026, there is no publicly confirmed launch of a user-facing C2PA verification feature in the Gemini app that allows users to check the provenance of images created outside Google's ecosystem. Google already embeds C2PA metadata in its own AI-generated images, but the distinct verification capability for external content remains pending.

Key terms:
- **C2PA Content Credentials**: A technical standard developed by the Coalition for Content Provenance and Authenticity (https://c2pa.org/) that attaches tamper-evident metadata to media files, documenting their origin and edit history. See also: https://contentcredentials.org/
- **Gemini app**: Google's consumer-facing AI assistant application, available on web (https://gemini.google.com/) and mobile platforms, which includes image generation and analysis capabilities.

**Exact later resolution packet**

The question resolves YES.

Google published an official "The Keyword" blog post titled "Making it easier to understand how content was created and edited" on May 19, 2026, at https://blog.google/innovation-and-ai/products/identifying-ai-generated-media-online/ . The post explicitly states that C2PA Content Credentials verification is "rolling out in the Gemini app starting today," allowing users to "easily check if content is an unaltered original from a camera or if it has been modified, and by what tools" [Making it easier to understand how content was created and edited](https://blog.google/innovation-and-ai/products/identifying-ai-generated-media-online/). This describes checking the provenance of external content (e.g., camera-captured images and content edited by non-Google tools), which is precisely the verification capability for content outside Google's ecosystem required by the resolution criteria, as distinct from merely embedding C2PA metadata in Google's own AI images [Making it easier to understand how content was created and edited](https://blog.google/innovation-and-ai/products/identifying-ai-generated-media-online/).

The launch was corroborated by credible technology coverage and the EdTech Innovation Hub article (May 2026), which reported: "C2PA verification is rolling out in the Gemini app from today and will come to Search and Chrome in the coming months" [Google expands AI content verification tools - EdTech Innovation Hub](https://www.edtechinnovationhub.com/news/google-adds-ai-verification-tools-across-search-gemini-chrome-pixel-and-cloud).

Key points satisfying each resolution requirement:
- Window: Announced May 19, 2026, which is on or after April 30, 2026, and before 23:59 UTC June 1, 2026 [Making it easier to understand how content was created and edited](https://blog.google/innovation-and-ai/products/identifying-ai-generated-media-online/).
- Public-facing Gemini app: The feature is rolling out in the consumer Gemini app, not limited to API/enterprise [Making it easier to understand how content was created and edited](https://blog.google/innovation-and-ai/products/identifying-ai-generated-media-online/) [Google expands AI content verification tools - EdTech Innovation Hub](https://www.edtechinnovationhub.com/news/google-adds-ai-verification-tools-across-search-gemini-chrome-pixel-and-cloud).
- External/verification (not embedding): The feature verifies provenance of content including camera originals and content modified by external tools, i.e., outside Google's ecosystem [Making it easier to understand how content was created and edited](https://blog.google/innovation-and-ai/products/identifying-ai-generated-media-online/).
- Official source: A blog.google post on The Keyword describing the feature as rolling out [Making it easier to understand how content was created and edited](https://blog.google/innovation-and-ai/products/identifying-ai-generated-media-online/).

Therefore the consequent is satisfied and the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-173. `aa1644a6-cfd6-53b7-be9f-9c2e7323f674`

- Present date: `2026-05-12 20:27:46.144937`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Francesco Cannizzaro (centre-right) win the 2026 Reggio Calabria mayoral election?

**Resolution criteria**

This question resolves YES if Francesco Cannizzaro is officially declared the winner of the 2026 Reggio Calabria mayoral election (either in the first round on May 24–25, 2026, or in the runoff on June 8, 2026), as published on the Italian Ministry of Interior's Eligendo portal (https://elezioni.interno.gov.it/) or by the Reggio Calabria municipal electoral office. All dates refer to Central European Summer Time (CEST).

This question resolves NO if any other candidate is declared the winner.

If the election is postponed or cancelled such that no official winner is declared by July 1, 2026, 23:59 CEST, this question resolves NO.

**Pre-cutoff background**

The 2026 Reggio Calabria municipal election is scheduled for May 24–25, 2026, with a potential runoff (ballottaggio) two weeks later on June 8, 2026 [2026 Italian local elections - Wikipedia](https://en.wikipedia.org/wiki/2026_Italian_local_elections). Under Italian electoral law, municipalities with more than 15,000 inhabitants use a two-round system: if no candidate receives more than 50% of valid votes in the first round, the top two candidates proceed to a runoff [2026 Italian local elections - Wikipedia](https://en.wikipedia.org/wiki/2026_Italian_local_elections).

Francesco Cannizzaro is a Deputy in the Italian Chamber of Deputies (Camera dei Deputati) for Forza Italia. He is the centre-right candidate for mayor, supported by a broad coalition of 12 lists including Forza Italia, Fratelli d'Italia, Lega, Noi Moderati, Azione, and several civic lists [Reggio Calabria, Cannizzaro allarga il centrodestra, Battaglia ...](https://www.corrieredellacalabria.it/2026/04/23/reggio-calabria-cannizzaro-allarga-il-centrodestra-battaglia-ricompatta-il-centrosinistra/). Il Sole 24 Ore has described the centre-right as "betting on" Reggio Calabria as a key target.

His main opponent is Domenico (Mimmo) Battaglia, the current acting mayor (sindaco facente funzione), who is the centre-left candidate supported by 7 lists including the Partito Democratico and Alleanza Verdi Sinistra [Reggio Calabria, Cannizzaro allarga il centrodestra, Battaglia ...](https://www.corrieredellacalabria.it/2026/04/23/reggio-calabria-cannizzaro-allarga-il-centrodestra-battaglia-ricompatta-il-centrosinistra/). Battaglia assumed the role of acting mayor following the end of the previous administration. Two additional candidates are also running: Eduardo Lamberti Castronuovo and a candidate from Movimento 5 Stelle [2026 Italian local elections - Wikipedia](https://en.wikipedia.org/wiki/2026_Italian_local_elections).

Cannizzaro's larger coalition (12 vs. 7 lists) gives him a structural advantage, but Battaglia benefits from incumbency as acting mayor and local centre-left traditions. Runoff dynamics in Italian municipal elections can shift outcomes significantly, as smaller-party voters may consolidate behind one candidate in the second round. As of May 11, 2026 (CEST), no official polls with published results are available, though the race is widely considered competitive.

**Exact later resolution packet**

RESOLUTION: YES (1). Francesco Cannizzaro (centre-right, Forza Italia) won the 2026 Reggio Calabria mayoral election in the FIRST ROUND held May 24–25, 2026, exceeding the 50% threshold and avoiding any runoff.

KEY EVIDENCE:
- The official Italian Ministry of Interior Eligendo results page for the first round in the Comune di REGGIO DI CALABRIA is: https://elezioni.interno.gov.it/risultati/20260524/comunali/scrutini/primoturno/180670630 (municipality code 180670630, election date 20260524, "primoturno"). This is the official resolution source required by the question. (The page renders results only via JavaScript, so its raw text could not be extracted directly; a query to it returned no usable data and an accompanying fabricated "Battaglia won" statement that is contradicted by every authoritative source and is disregarded.)
- Wikipedia's "2026 Italian local elections" article lists Francesco Cannizzaro (Forza Italia) as the elected mayor of Reggio Calabria with 67.80% of the vote in the first round, with no runoff indicated [https://en.wikipedia.org/wiki/2026_Italian_local_elections](https://en.wikipedia.org/wiki/2026_Italian_local_elections).
- Rai News (national public broadcaster) reported Cannizzaro "espugnando Palazzo San Giorgio già al primo turno" (winning already in the first round) with percentages above 70% [Reggio Calabria, storica spallata del centrodestra: Cannizzaro eletto ...](https://www.rainews.it/articoli/2026/05/reggio-calabria-storica-spallata-del-centrodestra-cannizzaro-eletto-sindaco-4f10ae94-41ee-4c39-8e10-7e3f0f81eef6.html).
- Corroborating major outlets (from Google results): Il Post ("ha vinto le elezioni comunali a Reggio Calabria al primo turno, con oltre il 60 per cento"), La Repubblica ("passa al primo turno"), Il Sole 24 Ore, ANSA (Cannizzaro proclaimed mayor), and reggiotoday all confirm the same outcome. He received roughly 59,103–59,214 votes, decisively ahead of centre-left candidate Domenico (Mimmo) Battaglia.

CHECKLIST COMPLIANCE:
- Decided in the FIRST ROUND (May 24–25, 2026), not the runoff; the >50% first-round result meant no June 8 ballottaggio occurred for this race.
- Official results page URL: https://elezioni.interno.gov.it/risultati/20260524/comunali/scrutini/primoturno/180670630
- A winner WAS officially declared before July 1, 2026 (Cannizzaro was formally proclaimed sindaco in early June 2026), so the "no winner by deadline → NO" clause does not apply.
- Not an annulment (-1): a valid winner was declared. Because that winner is the named candidate (Cannizzaro), the question resolves YES rather than NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-174. `c92e3b52-b1b9-5f96-842b-8b119dd7efec`

- Present date: `2026-05-14 03:48:48.463987`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-30T00:00:00`

**Question**

Will the 2026 Israel-Lebanon ceasefire still be formally in effect on June 30, 2026?

**Resolution criteria**

This question resolves as **Yes** if, as of June 30, 2026 at 23:59 UTC, the April 16, 2026 Israel-Lebanon ceasefire (including any extensions or renewals of it) is formally in effect—meaning neither the Israeli government, the Lebanese government, nor the United States (as broker) has officially declared it terminated, expired without renewal, or void.

This question resolves as **No** if, at any point between May 12, 2026 00:00 UTC and June 30, 2026 23:59 UTC, any of the following occurs:
1. The Israeli government, Lebanese government, or the United States officially declares the ceasefire terminated, collapsed, or expired without renewal; OR
2. The ceasefire's current extension expires and no new extension or successor agreement is announced by the U.S. State Department or the parties within 72 hours of expiry.

**Treatment of ambiguous events:** Low-intensity military actions (e.g., isolated airstrikes, skirmishes, drone attacks, or artillery exchanges) that occur without a formal declaration ending the ceasefire do NOT by themselves trigger a "No" resolution. The ceasefire has already been accompanied by such actions since its inception. Only a formal declaration of termination/expiry or the lapse of extensions without renewal (per condition 2 above) constitutes collapse for resolution purposes.

**Resolution source:** The primary resolution source is the U.S. State Department's Office of the Spokesperson (https://www.state.gov/releases/office-of-the-spokesperson/). Secondary sources include official Israeli government statements (https://www.gov.il/en), UNIFIL press releases (https://unifil.unmissions.org/unifil-press-releases), and credible international news agencies (Reuters, AP, BBC, Al Jazeera). If these sources provide conflicting information, the U.S. State Department's position takes precedence as the ceasefire broker.

**Pre-cutoff background**

On April 16, 2026, at 17:00 EST (21:00 GMT), the United States announced a 10-day cessation of hostilities between Israel and Lebanon to enable peace negotiations [https://www.securitycouncilreport.org/monthly-forecast/2026-05/lebanon-38.php](https://www.securitycouncilreport.org/monthly-forecast/2026-05/lebanon-38.php). The ceasefire does not formally include Hezbollah as a party but establishes a cessation of hostilities while allowing Israel to "preserve its right to take necessary measures in self-defense against planned, imminent, or ongoing attacks." On April 23, 2026, following talks in Washington, the ceasefire was extended by three additional weeks [https://www.securitycouncilreport.org/monthly-forecast/2026-05/lebanon-38.php](https://www.securitycouncilreport.org/monthly-forecast/2026-05/lebanon-38.php).

Despite the ceasefire, military activity has continued at lower intensity. As of early May 2026, Israeli airstrikes—including strikes on Beirut's southern suburbs—and Hezbollah rocket and drone attacks have continued, with both sides accusing the other of violations. On May 7, 2026, Israel bombed Beirut for the first time since the ceasefire was announced. By May 10, 2026, CNN reported that "deadly Israeli strikes and continued Hezbollah attacks are fueling fears that the US-backed ceasefire between Israel and Lebanon may be collapsing."

The ceasefire's durability depends on several factors: Israeli strategic goals regarding its northern security buffer zone, Hezbollah's military posture, the progress of US-mediated peace talks, and whether additional extensions are agreed upon. The initial 10-day period plus the three-week extension would nominally expire around May 24, 2026, absent further extensions.

Key sources for monitoring: the U.S. State Department (https://www.state.gov/), UNIFIL press center (https://unifil.unmissions.org/unifil-press-releases), and the Wikipedia article tracking the ceasefire (https://en.wikipedia.org/wiki/2026_Israel%E2%80%93Lebanon_ceasefire).

**Exact later resolution packet**

RESOLUTION: YES (1) — The 2026 Israel–Lebanon ceasefire (including its extensions/renewals) was formally in effect as of June 30, 2026, 23:59 UTC, because none of the three parties named in the resolution criteria (the Israeli government, the Lebanese government, or the United States) officially declared it terminated, collapsed, expired without renewal, or void; and no extension lapsed for 72+ hours without a renewal/successor.

TIMELINE OF EXTENSIONS/RENEWALS (continuous chain, no unrenewed lapse):
- April 16, 2026: 10-day cessation of hostilities announced by the US; extended by 3 weeks on April 23, 2026 (per question description).
- May 15, 2026: US State Department (spokesperson Tommy Pigott) confirmed Israel and Lebanon agreed to extend the ceasefire by 45 days, describing talks as "highly productive" [https://www.reuters.com/world/middle-east/israel-lebanon-agree-extend-ceasefire-by-45-days-us-state-dept-says-2026-05-15/](https://www.reuters.com/world/middle-east/israel-lebanon-agree-extend-ceasefire-by-45-days-us-state-dept-says-2026-05-15/). A 45-day extension from mid-May runs to roughly the end of June / July 1, i.e. past the June 30 resolution date [https://www.reuters.com/world/middle-east/israel-lebanon-agree-extend-ceasefire-by-45-days-us-state-dept-says-2026-05-15/](https://www.reuters.com/world/middle-east/israel-lebanon-agree-extend-ceasefire-by-45-days-us-state-dept-says-2026-05-15/).
- June 3–4, 2026: Israel and Lebanon agreed to renew the ceasefire with US mediation and to create "pilot" security zones [Israel and Lebanon agree to implement ceasefire if Hezbollah stops ...](https://www.bbc.com/news/articles/c5y01pdqvkgo) [https://en.wikipedia.org/wiki/2026_Israel%E2%80%93Lebanon_ceasefire](https://en.wikipedia.org/wiki/2026_Israel%E2%80%93Lebanon_ceasefire).
- June 26, 2026: The United States, Lebanon, and Israel signed a trilateral FRAMEWORK AGREEMENT at the U.S. Department of State, announced by Secretary of State Marco Rubio, aimed at "lasting peace and security" and explicitly calling for the implementation/continuation of a ceasefire between the two governments [Israel, Lebanon reach framework agreement, ceasefire - CNBC](https://www.cnbc.com/2026/06/26/israel-lebanon-hezbollah-ceasefire-rubio.html) [https://en.wikipedia.org/wiki/2026_Israel%E2%80%93Lebanon_ceasefire](https://en.wikipedia.org/wiki/2026_Israel%E2%80%93Lebanon_ceasefire). The agreement was reached between "the sovereign government of Lebanon" and "the government of Israel" with US mediation, with no party declaring the prior ceasefire terminated — it was a continuation/evolution of the ceasefire [Israel, Lebanon reach framework agreement, ceasefire - CNBC](https://www.cnbc.com/2026/06/26/israel-lebanon-hezbollah-ceasefire-rubio.html).

WHY CONDITION 1 (formal termination) IS NOT MET: No formal declaration of termination, collapse, or expiry-without-renewal was issued by the Israeli government, the Lebanese government, or the United States between May 12 and June 30, 2026. To the contrary, on June 26 all three parties jointly signed a framework agreement upgrading and continuing the ceasefire [Israel, Lebanon reach framework agreement, ceasefire - CNBC](https://www.cnbc.com/2026/06/26/israel-lebanon-hezbollah-ceasefire-rubio.html) [https://en.wikipedia.org/wiki/2026_Israel%E2%80%93Lebanon_ceasefire](https://en.wikipedia.org/wiki/2026_Israel%E2%80%93Lebanon_ceasefire). The U.S. State Department (the designated primary/priority source and ceasefire broker) issued a joint trilateral statement and hosted the signing ceremony, affirming the ceasefire's continuation.

WHY CONDITION 2 (unrenewed expiry) IS NOT MET: The 45-day extension (mid-May) was renewed/superseded by the June 3–4 renewal and the June 26 framework agreement, all announced by the US State Department or the parties, so no extension expired without a new extension/successor within 72 hours [https://www.reuters.com/world/middle-east/israel-lebanon-agree-extend-ceasefire-by-45-days-us-state-dept-says-2026-05-15/](https://www.reuters.com/world/middle-east/israel-lebanon-agree-extend-ceasefire-by-45-days-us-state-dept-says-2026-05-15/) [Israel and Lebanon agree to implement ceasefire if Hezbollah stops ...](https://www.bbc.com/news/articles/c5y01pdqvkgo) [Israel, Lebanon reach framework agreement, ceasefire - CNBC](https://www.cnbc.com/2026/06/26/israel-lebanon-hezbollah-ceasefire-rubio.html).

WHY HEZBOLLAH'S REJECTIONS ARE IRRELEVANT: Reports that Hezbollah rejected deals or called the framework "null and void" (e.g., late June 2026) do NOT trigger a "No." The resolution criteria specify the ceasefire "does not formally include Hezbollah as a party," and only a formal termination declaration by the Israeli government, the Lebanese government, or the United States, or an unrenewed lapse of an extension, can trigger "No." Likewise, the criteria explicitly state that low-intensity military actions (isolated airstrikes, skirmishes, drone/rocket attacks) do not by themselves trigger "No," since such actions accompanied the ceasefire from its inception.

CONCLUSION: With a US-brokered ceasefire continuously extended (May 15), renewed (June 3–4), and formalized into a trilateral framework agreement signed by Israel, Lebanon, and the US (June 26) — and no formal termination by any of the three named parties — the ceasefire was formally in effect on June 30, 2026, 23:59 UTC. Resolves YES.

Sources: US State Department 45-day extension via Reuters (https://www.reuters.com/world/middle-east/israel-lebanon-agree-extend-ceasefire-by-45-days-us-state-dept-says-2026-05-15/) [https://www.reuters.com/world/middle-east/israel-lebanon-agree-extend-ceasefire-by-45-days-us-state-dept-says-2026-05-15/](https://www.reuters.com/world/middle-east/israel-lebanon-agree-extend-ceasefire-by-45-days-us-state-dept-says-2026-05-15/); BBC on June renewal/pilot zones (https://www.bbc.com/news/articles/c5y01pdqvkgo) [Israel and Lebanon agree to implement ceasefire if Hezbollah stops ...](https://www.bbc.com/news/articles/c5y01pdqvkgo); CNBC on June 26 framework agreement/ceasefire (https://www.cnbc.com/2026/06/26/israel-lebanon-hezbollah-ceasefire-rubio.html) [Israel, Lebanon reach framework agreement, ceasefire - CNBC](https://www.cnbc.com/2026/06/26/israel-lebanon-hezbollah-ceasefire-rubio.html); Wikipedia "2026 Israel–Lebanon ceasefire" timeline (https://en.wikipedia.org/wiki/2026_Israel%E2%80%93Lebanon_ceasefire) [https://en.wikipedia.org/wiki/2026_Israel%E2%80%93Lebanon_ceasefire](https://en.wikipedia.org/wiki/2026_Israel%E2%80%93Lebanon_ceasefire); and the referenced US State Department joint trilateral statement (https://www.state.gov/releases/office-of-the-spokesperson/2026/06/joint-statement-of-the-united-states-of-america-republic-of-lebanon-and-state-of-israel-on-the-latest-high-level-trilateral-meeting/).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-175. `365334c7-dad5-5c16-8574-782b30f2933c`

- Present date: `2026-05-15 20:03:02.617680`
- Source cutoff boundary: `2026-05-16` (encodes end of UTC day `2026-05-15`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the ICC Trial Chamber set a specific start date for the Duterte trial by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 and on or before July 1, 2026 (23:59 UTC), ICC Trial Chamber III issues a written order, scheduling order, or makes a public announcement during a status conference (as reflected in an official court record or transcript published on the ICC website) that specifies a precise calendar date (i.e., a specific day, month, and year) for the commencement of the trial of Rodrigo Duterte (Case No. ICC-01/21-01/25).

A "specific start date" means a precise calendar day (e.g., "October 15, 2026"). A reference to a general time period such as "late 2026" or "first quarter of 2027" does not qualify.

The question resolves **No** if no such specific calendar date is set by 23:59 UTC on July 1, 2026.

**Primary resolution source:** Official court records and filings on the ICC case page: https://www.icc-cpi.int/philippines/duterte. Secondary sources include ICC press releases at https://www.icc-cpi.int/news and credible international media reporting (e.g., Reuters, AP, BBC).

**Pre-cutoff background**

On April 23, 2026, the International Criminal Court (ICC) Pre-Trial Chamber I confirmed all charges of crimes against humanity (murder and attempted murder) against former Philippine President Rodrigo Duterte and committed him to trial [https://www.hrw.org/news/2026/04/23/icc-court-sends-duterte-case-to-trial](https://www.hrw.org/news/2026/04/23/icc-court-sends-duterte-case-to-trial). Duterte was arrested in Manila on March 11, 2025, and has been detained at the ICC detention centre in The Hague since.

Following the confirmation of charges, the case was assigned to Trial Chamber III. On April 30, 2026, Trial Chamber III scheduled the first status conference for May 27, 2026, to address trial preparation matters. ICC Assistant to Counsel Kristina Conti has estimated that the trial proper may begin between October 2026 and February 2027 [https://www.gmanetwork.com/news/topstories/nation/985157/duterte-icc-trial-may-begin-between-oct-2026-to-feb-2027-conti/story/](https://www.gmanetwork.com/news/topstories/nation/985157/duterte-icc-trial-may-begin-between-oct-2026-to-feb-2027-conti/story/).

At the May 27 status conference, judges are expected to discuss the trial preparation timeline and may set deadlines and scheduling orders. However, whether the Trial Chamber will formally set a specific trial start date before July 1, 2026 remains uncertain — ICC cases often involve lengthy pre-trial preparation, including disclosure, witness lists, and defense preparation time, which can delay the formal scheduling of trial commencement.

The official ICC case page is: https://www.icc-cpi.int/philippines/duterte (Case No. ICC-01/21-01/25).

**Exact later resolution packet**

The question resolves **YES**.

**Resolution criteria recap:** Resolves YES if, between May 12, 2026 and July 1, 2026 (23:59 UTC), ICC Trial Chamber III issues a written/scheduling order or makes a public announcement during a status conference (per an official court record/transcript on the ICC website) specifying a *precise calendar date* (day, month, year) for the commencement of Rodrigo Duterte's trial (Case No. ICC-01/21-01/25).

**Key evidence:**
- The official ICC press release, titled "Duterte case: Trial to open on 30 November 2026," states that on 27 May 2026, at the opening status conference held by Trial Chamber III at the seat of the Court in The Hague, the Chamber scheduled the opening of the Duterte trial for 30 November 2026 [e1b4cc]. This is a precise calendar day (30 November 2026), and the decision was announced on 27 May 2026 — squarely within the resolution window (May 12 – July 1, 2026).
- The official ICC case page (https://www.icc-cpi.int/philippines/duterte) confirms under "Next steps": "The opening of the trial is scheduled for 30 November 2026." [a749fa]
- Credible media corroboration: INQUIRER.net (globalnation.inquirer.net) reported that during the 27 May 2026 status conference, Presiding Judge Joanna Korner announced, "we are prepared to accede to the Prosecution's application of the 30th of November as the start of the trial," and that Trial Chamber III "has set the start of President Rodrigo Duterte's trial on Nov. 30, 2026" [9f5afb]. This matches reporting from Rappler, GMA, Philstar and ABS-CBN found in search.

**Addressing the checklist:**
- The trial start date is a precise calendar day: 30 November 2026 — not a general period. ✓
- The announcement/scheduling occurred on 27 May 2026, within May 12 – July 1, 2026 inclusive. ✓
- Primary evidence is the official ICC press release and ICC case page (https://www.icc-cpi.int/news/duterte-case-trial-open-30-november-2026 and https://www.icc-cpi.int/philippines/duterte) [e1b4cc, a749fa]. ✓
- Secondary sources are of equivalent international standing (INQUIRER/Global Nation) and are consistent with the ICC record [9f5afb]. ✓
- Yes — a specific date WAS set during the May 27, 2026 status conference. ✓
- Resolution is based on a public announcement made during a court session (the 27 May 2026 status conference), as reflected in the official ICC press release and case page (a written order/press release memorializing the announcement). ✓

**Note on a conflicting automated read:** One tool query of the case page returned a spurious "NO" reading, arguing the page didn't confirm the date was set within the window. This is incorrect: the official press release explicitly dates the scheduling decision to the 27 May 2026 status conference [e1b4cc], and the case page's scheduled trial date of 30 November 2026 [a749fa] is fully consistent with that. The scheduling occurred on 27 May 2026, well within the window.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-176. `02127194-22f2-5e77-be68-8f3686123b7c`

- Present date: `2026-05-13 22:54:42.044323`
- Source cutoff boundary: `2026-05-14` (encodes end of UTC day `2026-05-13`)
- Expected resolution: `2026-06-07T00:00:00`

**Question**

Will OPEC+ agree to a production quota increase for July 2026 at the June 7, 2026 ministerial meeting?

**Resolution criteria**

This question resolves as **Yes** if the official press release issued by the OPEC Secretariat following the 41st OPEC and non-OPEC Ministerial Meeting (scheduled for June 7, 2026) explicitly announces an agreed increase in the aggregate production quota for July 2026 relative to the June 2026 quota levels. A "production quota increase" means a higher combined required production level (in barrels per day) for the participating OPEC+ members compared to the previously agreed June 2026 levels.

This question resolves as **No** if:
- The official press release announces that production quotas will remain unchanged (flat) for July 2026;
- The official press release announces a production quota decrease for July 2026;
- No agreement on July 2026 quotas is reached at the meeting; or
- The meeting is postponed or cancelled and no replacement meeting occurs before June 14, 2026, 23:59 UTC.

The increase must be officially agreed upon and communicated in the post-meeting press release. Informal statements, leaks, or reports from unnamed sources do not count.

**Resolution source:** The official OPEC press releases page at https://www.opec.org/opec_web/en/press_room/28.htm. The specific press release from the June 7, 2026 meeting will be published there. If the OPEC website is unavailable, credible reporting from Reuters (reuters.com) or Bloomberg (bloomberg.com) confirming the official outcome may be used as a fallback.

**Pre-cutoff background**

The OPEC+ group (currently 21 members following the UAE's departure on May 1, 2026) has been implementing a series of monthly production quota increases. On May 3, 2026, seven key OPEC+ members (Saudi Arabia, Russia, Iraq, Kuwait, Kazakhstan, Algeria, and Oman) agreed to raise their combined production quota by 188,000 barrels per day (bpd) for June 2026 [OPEC+ agrees third oil output quota hike since Hormuz closure](https://www.reuters.com/business/energy/opec-set-agree-third-oil-output-quota-hike-since-hormuz-closure-sources-say-2026-05-03/). This was the third consecutive monthly increase and slightly below the prior month's 206,000 bpd hike, with the reduction reflecting the exclusion of the UAE's share following its exit from the group.

These quota increases are currently described as "largely symbolic" because the ongoing Iran conflict (which began on February 28, 2026) has resulted in the closure of the Strait of Hormuz since late March 2026, severely limiting the physical export capacity of key producers including Saudi Arabia, Iraq, and Kuwait [OPEC+ agrees third oil output quota hike since Hormuz closure](https://www.reuters.com/business/energy/opec-set-agree-third-oil-output-quota-hike-since-hormuz-closure-sources-say-2026-05-03/). Reuters noted that "the output hike will remain largely symbolic until shipping through the Strait of Hormuz reopens." Despite these physical constraints, OPEC+ has continued announcing quota hikes to signal market control, continuity, and readiness to supply once the conflict ends.

The 41st OPEC and non-OPEC Ministerial Meeting (ONOMM) is scheduled for June 7, 2026 [https://www.opec.org/opec_web/en/press_room/28.htm](https://www.opec.org/opec_web/en/press_room/28.htm). Key uncertainties for forecasters include: (1) whether the Strait of Hormuz remains closed, making further increases purely symbolic; (2) how the UAE's departure affects group cohesion and strategy; (3) whether Saudi Arabia and Russia prefer to continue the pattern of symbolic increases or pivot to a pause or reversal; and (4) broader oil market conditions and geopolitical developments between now and the meeting.

**Exact later resolution packet**

The question resolves **YES**.

**What the question asked:** Resolve YES if the official OPEC Secretariat press release following the 41st OPEC and non-OPEC Ministerial Meeting (scheduled June 7, 2026) explicitly announces an agreed increase in the aggregate production quota for July 2026 relative to June 2026 levels.

**Antecedent check (meeting occurred, not postponed/cancelled):** The 41st OPEC and non-OPEC Ministerial Meeting was held as scheduled on Sunday, June 7, 2026 (held via videoconference under the chairmanship of Saudi Energy Minister HRH Prince Abdulaziz bin Salman). There was no postponement or cancellation, so no replacement-meeting question arises.

**Primary source (official OPEC press release):** The official OPEC press release for the meeting, at https://www.opec.org/pr-detail/604-7-june-2026.html, states that the seven participating countries (Saudi Arabia, Russia, Iraq, Kuwait, Kazakhstan, Algeria, and Oman) decided to implement a production adjustment of 188 thousand barrels per day, to be implemented in July 2026 [659afb]. This is a higher combined required production level than the June 2026 quota, i.e., an increase.

**Comparison July 2026 vs. June 2026:** The July increase of 188,000 bpd is applied on top of the June 2026 level, raising the aggregate quota. This matches Reuters' framing ("OPEC+ raises targets by 188,000 bpd from July"; "the seven members decided to increase targets by 188,000 bpd from July... the same as the June hike") — confirming an actual increase relative to June levels [ff2ba0].

**Fallback source corroboration:** Reuters reporting (https://www.reuters.com/business/energy/opec-set-fourth-oil-quota-hike-since-hormuz-closure-sources-say-2026-06-07/) independently confirms the official outcome — a fourth consecutive monthly quota increase of 188,000 bpd for July 2026 [ff2ba0].

**Conclusion:** The official press release explicitly announced an agreed increase in the aggregate production quota for July 2026 relative to June 2026. None of the NO conditions (flat, decrease, no agreement, postponement/cancellation) apply. Resolution = YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-177. `6ffb20d3-2600-5196-b6c5-f297afc5b0b9`

- Present date: `2026-05-15 10:19:28.642096`
- Source cutoff boundary: `2026-05-16` (encodes end of UTC day `2026-05-15`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the MTA and the coalition of five LIRR unions reach a ratified contract agreement between May 12, 2026 and July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 12, 2026, and before 11:59 PM ET on July 1, 2026, a contract agreement between the MTA and the coalition of five LIRR unions is fully ratified by union membership.

A "ratified contract agreement" means a collective bargaining agreement that has been (1) tentatively agreed to by MTA and union negotiators, AND (2) approved by a vote of the union membership. A tentative agreement alone does not satisfy this criterion — final ratification by union members must be confirmed.

If a deal is reached between negotiators but has not yet been ratified by the membership by the deadline, this question resolves as **No**.

Resolution will be determined by official announcements from the MTA Newsroom (https://new.mta.info/press-releases) or official union communications, or by credible reporting from major news outlets such as the New York Times (nytimes.com), Associated Press (apnews.com), or amNewYork (amny.com). If no such ratification is confirmed by the deadline, the question resolves as **No**.

**Pre-cutoff background**

As of May 13, 2026, the Metropolitan Transportation Authority (MTA) and a coalition of five unions representing approximately 3,500 Long Island Rail Road (LIRR) workers are in active but stalled contract negotiations [LIRR strike threat: Unions, MTA offer different takes on ... - amNewYork](https://www.amny.com/news/lirr-strike-threat-unions-mta-talks-05082026/). The five unions include IBEW Local 589 and BLET, among others. The parties have agreed on retroactive raises for the first three years of a four-year contract: 3% for 2023, 3% for 2024, and 3.5% for 2025. However, they remain deadlocked on 2026 wages. The unions are demanding a 5% raise for 2026, while the MTA has offered 4.5% contingent on the unions accepting work-rule changes; without those concessions, the MTA's effective offer is lower [LIRR strike threat: Unions, MTA offer different takes on ... - amNewYork](https://www.amny.com/news/lirr-strike-threat-unions-mta-talks-05082026/). Two Presidential Emergency Boards (PEBs) have sided with the unions. The unions have threatened a strike beginning May 16, 2026, if no deal is reached. Even if a tentative agreement is reached between negotiators, ratification by the union membership is a separate and additional step that adds uncertainty to full contract resolution.

**Exact later resolution packet**

The question resolves **YES (1)**.

**Antecedent/window:** The question resolves YES if, on or after May 12, 2026 and before 11:59 PM ET on July 1, 2026, a contract agreement between the MTA and the coalition of five LIRR unions was FULLY RATIFIED by union membership (not merely a tentative agreement).

**Timeline of events:**
- After a three-day strike (May 16–18, 2026), the MTA and the coalition of five LIRR unions reached a *tentative* agreement on May 18, 2026. A tentative agreement alone would NOT satisfy the criteria — but membership ratification followed and completed within the window.
- **IBEW Local 589** membership ratified the Memorandum of Understanding with the LIRR on June 3, 2026, by a 98% margin (official union communication) [2580a7].
- **BLET (Brotherhood of Locomotive Engineers and Trainmen)** members ratified their LIRR contract by a 98% margin, with the vote reported on June 18/21, 2026; BLET was the last of the five unions in the coalition to ratify (official union communication) [7f63d1].
- **Newsday** reported that the MTA board gave final approval to the new LIRR union contracts on Wednesday, June 24, 2026, and explicitly stated "the unions ratified the agreements by large margins last week." The five unions are identified as representing locomotive engineers (BLET), signal inspectors, electricians (IBEW Local 589), machinists, and ticket clerks [e45f6d].

**Why YES:** All five unions in the coalition (including the specifically named IBEW Local 589 and BLET) completed full membership ratification by June 18, 2026 — with the MTA board formalizing all five contracts on June 24, 2026. Every one of these events occurred within the resolution window (after May 12, 2026 and before 11:59 PM ET on July 1, 2026). The MTA board's June 24 approval of all five contracts confirms all had been ratified by membership, since the board formalizes agreements only after ratification. This clears the criterion's requirement of (1) a tentative agreement between negotiators AND (2) approval by a vote of the union membership.

Sources: BLET official news release (blet.org/news/lirr-contract-ratifies-by-a-98-percent-margin/) [7f63d1]; IBEW Local 589 official ratification memo (ibew589.org) [2580a7]; Newsday (newsday.com/long-island/transportation/lirr-mta-strike-contract-approved-yl7otfoz) [e45f6d].

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-178. `5899b32b-a424-5218-8de8-28b417fb551c`

- Present date: `2026-05-03 11:04:29.823201`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the European Parliament and the Council of the European Union reach a political agreement on the EU Digital Omnibus on AI by June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after April 30, 2026 (00:00 UTC) and on or before June 1, 2026 (23:59 UTC), a "political agreement" (also called "provisional agreement") on the Digital Omnibus on AI is formally announced.

A "formal agreement" is defined as the publication of an official press release or news item on the Council of the European Union website (https://www.consilium.europa.eu/en/press/press-releases/) or the European Parliament newsroom (https://www.europarl.europa.eu/news/en) confirming that a trilogue deal has been reached between the European Parliament and the Council on the Digital Omnibus on AI (the regulation amending the AI Act as part of the EU digital simplification package).

The question resolves as **No** if no such announcement appears by 23:59 UTC on June 1, 2026.

The "Digital Omnibus on AI" refers to the European Commission's proposal COM(2025) 618 amending Regulation (EU) 2024/1689 (the AI Act), as separated from the broader Digital Omnibus package for expedited trilogue treatment. See: https://www.europarl.europa.eu/thinktank/en/document/EPRS_BRI(2026)782651

**Pre-cutoff background**

The European Commission introduced the "Digital Omnibus" package on November 19, 2025, proposing targeted amendments to simplify the EU's digital legislative framework, including changes to the AI Act, GDPR, ePrivacy, NIS2, and DORA. A key element is delaying high-risk AI Act compliance deadlines—including biometrics and facial recognition provisions—from August 2, 2026 to later dates. The AI-related portion was separated into a standalone file (the "Digital Omnibus on AI") due to urgency around the approaching August 2026 deadline.

Legislative timeline so far:
- The Council adopted its negotiating mandate on March 13, 2026 [EU countries, lawmakers fail to reach deal on watered-down AI rules](https://www.reuters.com/sustainability/boards-policy-regulation/eu-countries-lawmakers-fail-reach-deal-watered-down-ai-rules-2026-04-29/).
- The European Parliament's IMCO and LIBE committees adopted a joint report on March 18, 2026, and Parliament's plenary approved its position on March 26, 2026.
- Trilogue negotiations began but the session on April 28, 2026 failed to produce agreement after 12 hours of talks [EU countries, lawmakers fail to reach deal on watered-down AI rules](https://www.reuters.com/sustainability/boards-policy-regulation/eu-countries-lawmakers-fail-reach-deal-watered-down-ai-rules-2026-04-29/). The key disagreement concerns whether AI systems in products already governed by sectoral safety legislation (e.g., medical devices, toys, connected cars) should be exempted from the AI Act's requirements [AI Act Omnibus: What just happened and what comes next? - IAPP](https://iapp.org/news/a/ai-act-omnibus-what-just-happened-and-what-comes-next).
- A follow-up trilogue is anticipated in mid-May 2026 [AI Act Omnibus: What just happened and what comes next? - IAPP](https://iapp.org/news/a/ai-act-omnibus-what-just-happened-and-what-comes-next).

Official legislative file: https://www.europarl.europa.eu/thinktank/en/document/EPRS_BRI(2026)782651

As of April 30, 2026, no political agreement has been reached. The August 2, 2026 compliance deadline for high-risk AI systems creates strong pressure to conclude negotiations quickly, but significant policy disagreements remain.

**Exact later resolution packet**

The question resolves YES. The Council of the European Union published an official press release titled "Artificial Intelligence: Council and Parliament agree to simplify and streamline rules" dated 7 May 2026 at https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/ . This press release is also indexed on the Council's official policy pages: the "Simplification of EU rules" page (https://www.consilium.europa.eu/en/policies/simplification/) and the "Artificial intelligence act" page (https://www.consilium.europa.eu/en/policies/artificial-intelligence-act/), both listing "Artificial Intelligence: Council and Parliament agree to simplify and streamline rules (press release, 7 May 2026)."

This satisfies every resolution criterion:
- Source: It is an official Council of the EU press release on consilium.europa.eu (the exact domain specified in the resolution criteria), not a third-party report. The European Commission also welcomed the deal (ec.europa.eu/commission/presscorner/detail/en/ip_26_1024).
- Date: The announcement date of 7 May 2026 falls strictly within the window of 30 April 2026 (00:00 UTC) to 1 June 2026 (23:59 UTC). (The press release page was later "updated on 18 May 2026," but the original publication/announcement was 7 May 2026.)
- Stage: It is a "provisional agreement"/"political agreement" reached via trilogue between the Council and Parliament — not merely a committee adoption or a Council negotiating mandate. The Bird & Bird analysis states: "In the early hours of Thursday 7 May 2026, Council and Parliament negotiators reached a provisional agreement on the Digital Omnibus on AI" [e43495]. The Council's prior negotiating mandate (13 March 2026) and the failed 28 April 2026 trilogue are distinct earlier stages.
- Scope: The agreement specifically covers the "Digital Omnibus on AI" — the regulation amending the AI Act (Regulation (EU) 2024/1689, COM(2025) 618), as separated for expedited trilogue treatment — confirmed by the press release title and content (simplifying/streamlining AI rules, postponing high-risk obligations, banning AI-generated CSAM/nudification apps) [e43495].

Note: the antecedent (the existence of a political agreement) is the substance of the question itself (not a separate conditional), so the question resolves directly on whether the agreement was announced in-window, which it was.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-179. `c52ba0d5-ac39-515a-a247-01a9b23566a3`

- Present date: `2026-05-03 02:08:57.349236`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Iran's IRGC cease all attacks, seizures, and interdictions of commercial shipping in the Strait of Hormuz for at least 7 consecutive days before June 1, 2026?

**Resolution criteria**

This question resolves YES if, between May 1, 2026, 00:00 UTC and May 31, 2026, 23:59 UTC, there exists at least one continuous period of 7 or more calendar days during which no confirmed incidents of the following types are carried out by Iranian military forces (specifically the Islamic Revolutionary Guard Corps (IRGC), IRGC Navy (IRGCN), or the Islamic Republic of Iran Navy (IRIN)) against commercial shipping in the Strait of Hormuz or its immediate approaches:

1. Kinetic attacks (missiles, gunfire, drones) on commercial vessels;
2. Seizure or boarding of commercial vessels without the vessel's consent;
3. Deployment of naval mines in or near recognized shipping lanes;
4. Firing of warning shots or physical harassment (e.g., fast-boat swarming) aimed at deterring commercial transit.

"Commercial vessels" means non-military cargo ships, tankers, container ships, and bulk carriers of any flag state. Iranian-flagged vessels are excluded.

The question resolves NO if no such 7-day incident-free window occurs during the monitoring period.

Resolution will be determined based on reporting from the United Kingdom Maritime Trade Operations (UKMTO, https://www.ukmto.org/), Lloyd's List Intelligence, or major international news agencies (Reuters, AP, BBC, Al Jazeera). If these sources report no qualifying incidents during any 7-day window within May 2026, the question resolves YES. If incidents are reported continuously such that no 7-day gap exists, it resolves NO.

**Pre-cutoff background**

As of May 1, 2026, the Strait of Hormuz — the world's most critical maritime chokepoint for energy trade — is effectively closed to most commercial shipping due to a "dual blockade" involving both Iran and the United States [2026 Strait of Hormuz crisis - Wikipedia](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis).

The crisis began on February 28, 2026, following US/Israeli air strikes on Iran. The Islamic Revolutionary Guard Corps (IRGC) began issuing warnings to ships, attacking merchant vessels, laying sea mines, and demanding tolls exceeding $1 million per ship [2026 Strait of Hormuz crisis - Wikipedia](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis). On March 27, 2026, the IRGC officially prohibited vessel movement for ships going to or from "enemy" ports (US, Israel, and allies) [2026 Strait of Hormuz crisis - Wikipedia](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis). On April 13, 2026, the US Navy initiated a formal counter-blockade of Iranian ports [2026 Strait of Hormuz crisis - Wikipedia](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis).

A temporary ceasefire on April 8, 2026 briefly raised hopes, but Iran continued restricting traffic and charging tolls. On April 17, Iran announced the strait was open during the truce, but re-imposed restrictions one day later in response to the continued US blockade [2026 Strait of Hormuz crisis - Wikipedia](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis). On April 22, IRGC gunboats attacked and seized multiple cargo ships [2026 Strait of Hormuz crisis - Wikipedia](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis). As of April 30, 2026, the UN Secretary-General has called for the immediate reopening of the strait, but shipping traffic remains at a trickle with no resolution in sight.

The primary Iranian entity enforcing the blockade is the Islamic Revolutionary Guard Corps (IRGC), including its naval forces (IRGCN). The regular Islamic Republic of Iran Navy (IRIN) has also been involved in patrols and enforcement [2026 Strait of Hormuz crisis - Wikipedia](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis).

**Exact later resolution packet**

RESOLUTION: YES (1).

The question resolves YES if there exists at least one continuous 7+ calendar-day window between May 1, 2026 00:00 UTC and May 31, 2026 23:59 UTC during which NO confirmed incidents of four specific types — (1) kinetic attacks, (2) seizures/boardings without consent, (3) deployment of naval mines in shipping lanes, (4) warning shots/physical harassment — were carried out by the IRGC, IRGCN, or IRIN against non-Iranian-flagged commercial vessels in the Strait of Hormuz or its immediate approaches.

CRITICAL INTERPRETIVE POINT: The resolution criteria enumerate four concrete physical incident types. The continued existence of Iran's "blockade," its demands for tolls, its requirement that vessels obtain authorization/coordinate passage, and its general "control" of the strait are NOT among these four enumerated incident types. Several of my source queries incorrectly conflated "Iran maintaining control / running a protection racket / coordinating transits" with an "incident" and thus wrongly leaned NO. Read literally (as instructed), what matters is whether the four specific physical acts occurred against commercial vessels in any given 7-day stretch.

EVIDENCE OF A 7+ DAY INCIDENT-FREE WINDOW (approx. May 15–25):

1. ISW/Critical Threats Project "Iran Update Evening Special Report: May 21, 2026" states there were NO reports of kinetic attacks, seizures, boardings, mine-laying, or harassment against commercial vessels in the Strait of Hormuz between May 15 and May 21, 2026; during this period vessels transited with Iranian coordination/permission rather than being attacked [Iran Update Evening Special Report: May 21, 2026 | Critical Threats](https://www.criticalthreats.org/analysis/iran-update-evening-special-report-may-21-2026). The May 20 ISW report similarly describes vessels transiting (16 vessels May 19–20) under Iran's coordination/fee system with no reported attacks on commercial ships [Iran Update Special Report, May 20, 2026 | ISW](https://understandingwar.org/research/middle-east/iran-update-special-report-may-20-2026/).

2. The Wikipedia "2026 Strait of Hormuz crisis" article's incident list and timeline (last updated May 27, 2026) records confirmed incidents against commercial vessels up to May 14, 2026 (seizure of the Honduras-flagged Hui Chuan), and then lists NO further incidents through May 27 [https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis) [2026 Strait of Hormuz crisis - Wikipedia](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis).

3. UKMTO's recent-incidents data shows Strait of Hormuz / approaches incidents on May 3, 5, 10, and 14, then no qualifying Strait-of-Hormuz incident until an attack ~60NM east of Muscat on May 26 (the May 22–23 "suspicious activity" warnings were near Socotra / Gulf of Aden, far outside the Strait of Hormuz approaches and thus excluded) [Recent Incidents - UKMTO](https://www.ukmto.org/recent-incidents). This yields an ~11-day gap (May 15–25) free of qualifying incidents in the relevant geography.

4. Incidents resumed only at the end of the month: US struck IRGC mine-laying vessels on May 25 (a US action against Iranian vessels, not an Iranian act against commercial shipping), and the IRGC seized two commercial vessels and warned two others on May 28, 2026 [Iran claims it coordinated passage of 26 vessels out of Hormuz in 24 ...](https://www.aljazeera.com/news/2026/5/20/iran-says-it-coordinated-crossing-of-26-vessels-out-of-strait-of-hormuz) [Iran Update Evening Special Report: May 28, 2026 | Critical Threats](https://www.criticalthreats.org/analysis/iran-update-evening-special-report-may-28-2026). These late-May events do not negate the earlier mid-May incident-free window.

The HMM ship attack reported by Reuters on May 27 was an analysis of the EARLIER May 4 attack, not a new late-May incident [Iranian missile likely involved in attack on ship in Strait of Hormuz ...](https://www.reuters.com/world/asia-pacific/south-korea-says-attack-ship-strait-hormuz-likely-involved-an-iranian-missile-2026-05-27/), so it does not affect the mid-May window.

Because at minimum the May 15–21 period (and arguably May 15–25) contained no confirmed kinetic attacks, seizures/boardings, mine deployments, or warning-shot/harassment incidents by the IRGC/IRGCN/IRIN against non-Iranian commercial vessels in the Strait of Hormuz, a continuous window of 7+ calendar days satisfying the YES condition existed within the monitoring period. The question resolves YES.

Sources: ISW/CTP May 21 report (https://www.criticalthreats.org/analysis/iran-update-evening-special-report-may-21-2026) [Iran Update Evening Special Report: May 21, 2026 | Critical Threats](https://www.criticalthreats.org/analysis/iran-update-evening-special-report-may-21-2026); ISW May 20 report (https://understandingwar.org/research/middle-east/iran-update-special-report-may-20-2026/) [Iran Update Special Report, May 20, 2026 | ISW](https://understandingwar.org/research/middle-east/iran-update-special-report-may-20-2026/); Wikipedia 2026 Strait of Hormuz crisis (https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis) [https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis) [2026 Strait of Hormuz crisis - Wikipedia](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis); UKMTO recent incidents (https://www.ukmto.org/recent-incidents) [Recent Incidents - UKMTO](https://www.ukmto.org/recent-incidents); Reuters May 27 (https://www.reuters.com/world/asia-pacific/south-korea-says-attack-ship-strait-hormuz-likely-involved-an-iranian-missile-2026-05-27/) [Iranian missile likely involved in attack on ship in Strait of Hormuz ...](https://www.reuters.com/world/asia-pacific/south-korea-says-attack-ship-strait-hormuz-likely-involved-an-iranian-missile-2026-05-27/); CTP May 28 (https://www.criticalthreats.org/analysis/iran-update-evening-special-report-may-28-2026) [Iran Update Evening Special Report: May 28, 2026 | Critical Threats](https://www.criticalthreats.org/analysis/iran-update-evening-special-report-may-28-2026).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-180. `e31822b4-aed7-5e0b-b0db-b76a270b0e7d`

- Present date: `2026-04-30 13:44:10.587284`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will OpenAI make GPT-5.5 available to free-tier ChatGPT users by June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, at any point between April 29, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC), OpenAI makes any version of GPT-5.5 (including GPT-5.5 Thinking or GPT-5.5 Pro) selectable or usable by users on the free tier of ChatGPT (https://chatgpt.com).

"Free tier" refers to the $0/month ChatGPT plan as described on OpenAI's ChatGPT pricing page (https://openai.com/chatgpt/pricing/). "Available" means free-tier users can select and use GPT-5.5 for conversations, even if subject to rate limits or usage caps.

This question resolves as **No** if, by 23:59 UTC on June 1, 2026, GPT-5.5 remains unavailable to free-tier ChatGPT users.

Resolution source: The OpenAI Help Center article on GPT-5.5 in ChatGPT (https://help.openai.com/en/articles/11909943-gpt-5-1-in-chatgpt), the OpenAI ChatGPT pricing page (https://openai.com/chatgpt/pricing/), or credible reporting from outlets such as TechCrunch (https://techcrunch.com), The Verge, or Reuters confirming free-tier access.

**Pre-cutoff background**

On April 23, 2026, OpenAI released GPT-5.5 (codenamed "Spud"), its newest frontier model [Introducing GPT-5.5 - OpenAI](https://openai.com/index/introducing-gpt-5-5/). At launch, GPT-5.5 was made available to ChatGPT Plus, Pro, Business, and Enterprise users, but not to free-tier users [Introducing GPT-5.5 - OpenAI](https://openai.com/index/introducing-gpt-5-5/). API access, initially withheld at launch, was enabled on April 24, 2026 [GPT-5.5 - Wikipedia](https://en.wikipedia.org/wiki/GPT-5.5).

As of April 29, 2026, free-tier ChatGPT users remain on GPT-5.3 Instant and do not have access to GPT-5.5 (see https://fritz.ai/chatgpt-pricing/ and https://help.openai.com/en/articles/11909943-gpt-5-1-in-chatgpt). OpenAI has not announced a specific timeline for bringing GPT-5.5 to the free tier.

OpenAI has historically rolled out new models to paid tiers first, with free-tier access following weeks to months later. For reference, GPT-5.5 pricing in the API is $5/1M input tokens and $30/1M output tokens [https://openai.com/api/pricing/](https://openai.com/api/pricing/), suggesting significant compute costs that may delay free-tier availability.

Note: The original question about GPT-5.5 public API availability has already resolved, as OpenAI made GPT-5.5 available in the API on April 24, 2026 [Introducing GPT-5.5 - OpenAI](https://openai.com/index/introducing-gpt-5-5/). This reformulated question focuses on the still-uncertain free-tier rollout.

**Exact later resolution packet**

The question resolves YES. It asks whether OpenAI made any version of GPT-5.5 selectable/usable by free-tier ChatGPT users at any point between April 29, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC).

Evidence:
- OpenAI's official announcement "GPT-5.5 Instant: smarter, clearer, and more personalized" (https://openai.com/index/gpt-5-5-instant/), published May 5, 2026, explicitly states in its Availability section: "GPT-5.5 Instant is rolling out starting today to all ChatGPT users, replacing GPT-5.3 Instant as the default model," and describes it as "ChatGPT's default model, available to everyone" [468de7]. "All ChatGPT users" and "everyone" includes the $0/month Free tier.
- Wikipedia's GPT-5.5 article corroborates: "GPT-5.5 Instant was released to free-tier users on May 5, 2026, replacing GPT-5.3 Instant as ChatGPT's default model for all users" [ba1959].
- This means GPT-5.5 Instant became the default model for free-tier users (thus usable for conversations, subject to rate limits) on May 5, 2026, which falls squarely within the resolution window (April 29 – June 1, 2026).

The model was actually deployed/usable (not merely announced for a future date) — it became the default model for free users on the rollout day. This satisfies the "selectable or usable for conversations" requirement, even with usage caps. Therefore the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-181. `1ca4ab00-2aa4-5520-98b4-1c13a26efa1d`

- Present date: `2026-05-01 13:01:52.172297`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Sarah Friar still be CFO of OpenAI on June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, as of June 1, 2026 at 23:59 UTC, Sarah Friar holds the title of Chief Financial Officer (CFO) of OpenAI (including OpenAI Group PBC or any successor entity).

This question resolves **No** if, by that time, she has resigned, been terminated, or transitioned to a different role (e.g., advisor, board member, or any non-CFO title).

**Key definitional clarifications:**

- **Announced but not yet effective departures:** If Sarah Friar has publicly announced a resignation or departure but her departure date is after June 1, 2026 (i.e., she is still formally serving as CFO on June 1, 2026 at 23:59 UTC), the question resolves **Yes**.
- **Interim/Acting CFO:** If Sarah Friar's title has been changed to "Interim CFO" or "Acting CFO," this does NOT count as holding the CFO role, and the question resolves **No**. Conversely, if someone else is named "Interim CFO" or "Acting CFO" while Friar retains the CFO title, the question resolves **Yes**.
- **"CFO"** refers specifically to the title of Chief Financial Officer. Equivalent titles in other languages or slight variations (e.g., "Chief Financial & Strategy Officer") count, provided "Chief Financial Officer" is part of the title.

**Resolution source:** The primary resolution source is OpenAI's official website (https://openai.com/about/ or any official leadership/team page). If the website does not clearly indicate her status, resolution will be based on consistent reporting from at least two major news outlets (e.g., Reuters, Bloomberg, The Wall Street Journal, The New York Times, or Fortune).

**Pre-cutoff background**

Sarah Friar joined OpenAI in 2024 as its first Chief Financial Officer. As of late April 2026, she remains in the role but faces significant internal tension. According to reports from The Information and Fortune (April 6, 2026), CEO Sam Altman has excluded Friar from key financial planning meetings, and she has expressed skepticism about Altman's aggressive late-2026 IPO timeline [Things are getting weird on OpenAI's leadership team - Fortune](https://fortune.com/2026/04/06/openai-leadership-cfo-sarah-friar-china-drone-industry-north-korean-hackers-drift/). Friar's reporting structure is also unusual for a CFO: since August 2025, she has reported to Fidji Simo (CEO of Applications) rather than directly to Sam Altman [Things are getting weird on OpenAI's leadership team - Fortune](https://fortune.com/2026/04/06/openai-leadership-cfo-sarah-friar-china-drone-industry-north-korean-hackers-drift/). These dynamics have fueled speculation about a possible departure. However, as of April 30, 2026, no official announcement of her resignation or termination has been made, and she continues to hold the CFO title.

**Exact later resolution packet**

The question resolves YES: Sarah Friar held the title of Chief Financial Officer of OpenAI as of June 1, 2026 at 23:59 UTC.

Evidence:
- A Bloomberg article dated May 15, 2026 explicitly identifies Sarah Friar as "OpenAI Chief Financial Officer" reporting on OpenAI's fundraising plans, with no indication of any departure [2b297e]. URL: https://www.bloomberg.com/news/articles/2026-05-15/openai-may-raise-more-money-as-compute-crunch-deepens-cfo-says
- A Bloomberg article dated May 1, 2026 refers to her as "OpenAI Chief Financial Officer Sarah Friar." URL: https://www.bloomberg.com/news/articles/2026-05-01/openai-finance-chief-sees-vertical-wall-of-demand-for-products
- A Fortune article dated April 28, 2026 refers to her as "OpenAI's CFO Sarah Friar." URL: https://fortune.com/2026/04/28/openai-cfo-sam-altman-missed-revenue-target/
- CNBC video content (Sara Eisen interview) referring to her as "OpenAI CFO Sarah Friar" with viewing dates of May 31, 2026, and a Yahoo Finance video dated May 28, 2026 also calling her "OpenAI CFO Sarah Friar" — both well into late May with no departure.

The OpenAI official "About" page (the primary specified resolution source) did not list her or any leadership/CFO information [3f8b56], so per the resolution criteria I relied on consistent reporting from at least two major outlets (Bloomberg and Fortune, both on the approved list).

Despite well-documented internal tension with Sam Altman over IPO timing (reported by The Information, WSJ, Fortune in April 2026), no resignation, termination, or transition to a non-CFO/Interim/Acting title was ever announced. Her title remained "Chief Financial Officer" (not "Interim" or "Acting"). Therefore she was still formally serving as CFO at the June 1, 2026 23:59 UTC deadline, satisfying the YES condition.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-182. `33eb34d8-cdeb-5d66-884f-47879d1ad89b`

- Present date: `2026-05-14 07:24:00.635426`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Lisa Murkowski vote in favor of the motion to proceed on the Senate's $72 billion immigration reconciliation bill (pursuant to S.Con.Res.33)?

**Resolution criteria**

This question resolves YES if, between May 12, 2026 (00:00 UTC) and July 1, 2026 (23:59 UTC), Senator Lisa Murkowski casts a "Yea" vote on a motion to proceed related to the Senate's immigration reconciliation bill developed pursuant to S.Con.Res.33. 

For the purposes of this question, "motion to proceed" refers to either: (a) a simple motion to proceed to consideration of the reconciliation bill, or (b) a cloture motion on the motion to proceed to the reconciliation bill. If both votes occur, the question resolves based on the first such vote chronologically.

This question resolves NO if:
- Murkowski votes "Nay" on the motion to proceed (or cloture on the motion to proceed);
- Murkowski does not vote (e.g., due to absence or voting "present");
- No motion to proceed on the reconciliation bill is brought to a roll call vote by July 1, 2026 (23:59 UTC).

Resolution source: The official U.S. Senate Roll Call Vote records at https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_119_2.htm or the corresponding page on https://www.congress.gov.

**Pre-cutoff background**

On April 23, 2026, the U.S. Senate passed budget resolution S.Con.Res.33 by a vote of 50-48, setting the stage for a reconciliation bill focused on immigration enforcement funding [Sens. Murkowski and Paul break ranks on final Senate budget vote](https://thehill.com/homenews/senate/5844598-murkowski-paul-budget-resolution/). Senators Lisa Murkowski (R-AK) and Rand Paul (R-KY) were the only two Republicans to vote against the resolution, joining all Democrats in opposition [Sens. Murkowski and Paul break ranks on final Senate budget vote](https://thehill.com/homenews/senate/5844598-murkowski-paul-budget-resolution/).

Murkowski's objection was procedural rather than substantive: while she supports funding for Immigration and Customs Enforcement (ICE) and Customs and Border Protection (CBP), she opposed removing these agencies from the annual congressional appropriations and oversight process by funding them for 3.5 years through reconciliation [Sens. Murkowski and Paul break ranks on final Senate budget vote](https://thehill.com/homenews/senate/5844598-murkowski-paul-budget-resolution/).

On May 4-5, 2026, the Senate Judiciary Committee and the Senate Homeland Security and Governmental Affairs Committee released legislative text for a $72 billion reconciliation spending package pursuant to S.Con.Res.33 [Senate Committees release $72 billion budget reconciliation ...](https://news.ballotpedia.org/2026/05/07/senate-committees-release-72-billion-budget-reconciliation-spending-package/). The package provides over $38 billion for ICE and over $26 billion for CBP. The budget resolution directed committees to submit recommendations by May 15, 2026, and President Trump indicated a desire for Senate approval before June 1, 2026 [Senate Committees release $72 billion budget reconciliation ...](https://news.ballotpedia.org/2026/05/07/senate-committees-release-72-billion-budget-reconciliation-spending-package/).

Republicans hold a narrow Senate majority and can afford very few defections on reconciliation votes, which require only a simple majority (51 votes). Murkowski, along with Senators Susan Collins and Rand Paul, is considered a pivotal swing vote. Whether Senate leadership can address Murkowski's oversight concerns through amendments or commitments may determine her vote on the motion to proceed.

**Exact later resolution packet**

RESOLUTION: YES (1).

The question asks whether Senator Lisa Murkowski cast a "Yea" vote on a motion to proceed to the Senate's immigration reconciliation bill developed pursuant to S.Con.Res.33, between May 12, 2026 and July 1, 2026.

KEY FACTS:
- The reconciliation bill became S.2, the "Secure America Act," described as "An original bill to provide for reconciliation pursuant to title II of S. Con. Res. 33." This matches the antecedent condition (bill developed pursuant to S.Con.Res.33).
- On June 3, 2026, the Senate held Roll Call Vote No. 136 on the Motion to Proceed to S.2. The motion was agreed to 53–46. Congress.gov's S.2 action record confirms: "Motion to proceed to consideration of measure agreed to in Senate by Yea-Nay Vote. 53 - 46. Record Vote Number: 136." (search result) and GovTrack labels vote #136 as "Motion to Proceed on S. 2: Secure America Act, June 3, 2026."
- The official U.S. Senate Roll Call Vote record for Vote 136 (https://www.senate.gov/legislative/LIS/roll_call_votes/vote1192/vote_119_2_00136.htm) explicitly lists "Murkowski (R-AK), Yea" [7cb1f1]. Voteview independently confirms Murkowski cast a "Y" on this same motion to proceed [f7ac75].

VOTE TYPE VERIFICATION: This is a "motion to proceed" (not final passage). Because a reconciliation motion to proceed is non-debatable, there was no separate cloture vote on the motion to proceed; Vote 136 was the first and only motion-to-proceed vote, satisfying the "first chronologically" tie-breaker. Final passage was a separate, later vote (Roll Call 163, June 5, 2026, 52–47), on which Murkowski voted against the bill — but that is not the vote this question concerns.

TIMING: June 3, 2026 falls within the required window (May 12, 2026 00:00 UTC – July 1, 2026 23:59 UTC).

DISAMBIGUATION: One tool query returned a "Nay" claim, but it was derived from the Senate vote-menu index page, which does not list individual senators' votes; that claim was unsupported/hallucinated [24dea9]. The authoritative individual-vote record (Senate.gov Vote 136 page [7cb1f1]) and Voteview [f7ac75] both show "Yea." The arithmetic is fully consistent: 53 Yeas equals all 53 Republicans (including Murkowski) voting to proceed, whereas on final passage (52–47) she crossed over to vote with Democrats against the bill — explaining the widely-reported note that Murkowski "voted with Democrats against the bill" (that refers to final passage, not the motion to proceed).

Therefore Murkowski voted "Yea" on the motion to proceed → resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-183. `068d1820-e95a-58b6-ac21-9697ae7e402b`

- Present date: `2026-05-02 14:41:22.698680`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Google Cloud announce a new single-customer deal with a Total Contract Value of $5 billion or more between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves YES if, between 00:00 UTC on May 1, 2026 and 23:59 UTC on June 1, 2026, Google Cloud (or its parent company Alphabet Inc.) publicly announces a new cloud services contract with a single customer entity that has a reported Total Contract Value (TCV) of $5 billion USD or more.

Definitions and clarifications:
- "Total Contract Value (TCV)" means the total dollar amount committed over the full duration of the contract, as reported in the announcement or credible reporting. If only annual contract value or expected revenue is disclosed, this does not qualify unless the total commitment is explicitly stated or reliably reported to be $5 billion or more.
- "Single customer" means one legal entity or corporate group. Multi-party consortium deals where no single party commits $5 billion+ do not qualify.
- "Publicly announces" means either: (a) an official press release on the Google Cloud Press Corner (https://www.googlecloudpresscorner.com/press-releases), (b) a filing on Alphabet's SEC filings page (https://abc.xyz/investor/), or (c) credible reporting by major financial news outlets (Reuters, Bloomberg, The Wall Street Journal, Financial Times) citing official sources or people familiar with the matter.
- The announcement date (not the contract signing date) must fall within the specified window.
- If no qualifying announcement is made by 23:59 UTC on June 1, 2026, the question resolves NO.

**Pre-cutoff background**

Google Cloud has been landing increasingly large enterprise deals as AI demand accelerates. Notable recent mega-deals include a contract with Palo Alto Networks worth approximately $10 billion (announced December 2025), a $10 billion deal with Meta, and a multi-billion dollar agreement with Thinking Machines Lab (announced April 2026) [Google Targets AI Growth with Multi-Billion Dollar Cloud Deal](https://www.moroccoworldnews.com/2026/04/288234/google-targets-ai-growth-with-multi-billion-dollar-cloud-deal/). Google Cloud's remaining performance obligations (backlog) nearly doubled quarter-on-quarter to over $460 billion as of March 31, 2026, reflecting surging enterprise AI demand. Google Cloud revenue grew 63% year-over-year to exceed $20 billion in Q1 2026 [Press Releases - Google Cloud Press Corner](https://www.googlecloudpresscorner.com/press-releases?l=100).

During Google Cloud Next '26 (April 22–24, 2026), Google announced dozens of new customer partnerships and expansions — with companies including Deloitte, Accenture, McKinsey, PepsiCo, SAP, Salesforce, Merck, and many others — though most of these did not disclose specific dollar values [Press Releases - Google Cloud Press Corner](https://www.googlecloudpresscorner.com/press-releases?l=100). The pace of multi-billion dollar deal announcements has been roughly one every few months, making a $5 billion+ deal in any given 31-day window plausible but far from certain.

Alphabet's capital expenditure plans for 2026 range from $175 billion to $185 billion, underscoring the scale of investment in cloud and AI infrastructure.

**Exact later resolution packet**

Adjudicated: On May 5, 2026 (within the May 1 - June 1, 2026 window), Reuters - an explicitly allowed source - reported that Anthropic, a single legal entity, committed to spend $200 billion with Google Cloud over five years, far exceeding the $5 billion threshold. The figure is an explicit total committed spend over the full contract duration (Total Contract Value), not annual revenue, and covers Google Cloud services and TPU chip capacity. An initial automated resolution missed this report; the criteria for YES are fully met.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-184. `a34ac941-50c3-556f-b2cf-067e501e0ebc`

- Present date: `2026-05-03 11:46:02.920029`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will SpaceX's Starship Flight 12 successfully launch before June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if SpaceX's Starship Flight 12 vehicle achieves liftoff — defined as the vehicle fully clearing the launch tower — on or after April 30, 2026, at 00:00 UTC and before June 1, 2026, at 00:00 UTC.

This question resolves **No** if the vehicle does not achieve liftoff (clear the tower) within this window, regardless of the reason (delay, scrub, cancellation, or anomaly preventing liftoff).

A "successful launch" for the purposes of this question means only that the vehicle clears the launch tower. It does not require achieving orbit, completing mission objectives, or surviving the full flight profile.

**Resolution source**: Official SpaceX communications (https://www.spacex.com/launches or SpaceX's official X/Twitter account at https://x.com/SpaceX), or credible reporting from major space news outlets such as Space.com (https://www.space.com), NASASpaceFlight.com, Ars Technica, Reuters, or the Associated Press.

**Pre-cutoff background**

SpaceX is preparing for the 12th integrated flight test of its Starship launch vehicle. Flight 12 is a major milestone as it will be the first flight of the "Block 3" vehicle — a significantly upgraded version of Starship featuring design improvements over previous iterations — and the first launch from Orbital Launch Pad 2 (OLP-2), the newly constructed second launch site at Starbase in Boca Chica, Texas [https://en.wikipedia.org/wiki/List_of_Starship_launches](https://en.wikipedia.org/wiki/List_of_Starship_launches).

The Starship program has experienced repeated delays for Flight 12. Originally targeted for March 2026, the launch slipped to April, and then to May 2026 [When will SpaceX's Starship 12th launch take place? - FOX Weather](https://www.foxweather.com/earth-space/when-spacexs-starship-12th-launch). As of late April 2026, SpaceX is targeting a May 2026 launch window. An FCC license was granted covering the period April 5 – October 5, 2026 [https://en.wikipedia.org/wiki/List_of_Starship_launches](https://en.wikipedia.org/wiki/List_of_Starship_launches). Static fire tests of both the Super Heavy booster and Starship upper stage were completed in mid-April 2026. A wet dress rehearsal (WDR) has also been conducted.

Key definitions:
- **Starship**: SpaceX's fully reusable super heavy-lift launch vehicle system, consisting of the Super Heavy booster and Starship upper stage. See: https://en.wikipedia.org/wiki/SpaceX_Starship
- **Block 3 vehicle**: The third major design iteration of Starship, incorporating structural and performance upgrades. See: https://starship-spacex.fandom.com/wiki/Starship_Flight_Test_12
- **OLP-2 (Orbital Launch Pad 2)**: The second orbital launch pad at SpaceX's Starbase facility in Boca Chica, Texas. See: https://en.wikipedia.org/wiki/SpaceX_Starbase#Launch_site

Given SpaceX's history of Starship delays and the novelty of both the Block 3 vehicle and OLP-2 infrastructure, there is genuine uncertainty about whether the launch will occur before June 1, 2026.

**Exact later resolution packet**

The question resolves YES because SpaceX's Starship Flight 12 achieved liftoff (cleared the launch tower) on May 22, 2026, at 22:30 UTC — within the required window of April 30, 2026, 00:00 UTC to June 1, 2026, 00:00 UTC.

Evidence:
- The official SpaceX mission page (https://www.spacex.com/launches/starship-flight-12) states: "On Friday, May 22, 2026, at 5:30 p.m. CT, Starship lifted off from Starbase, Texas on its twelfth flight test." 5:30 p.m. CT (CDT = UTC-5) = 22:30 UTC on May 22, 2026 [Starship's Twelfth Flight Test - SpaceX](https://www.spacex.com/launches/starship-flight-12).
- Wikipedia's "Starship flight test 12" article confirms the launch date/time as May 22, 2026, 22:30:22 UTC, with the flight timeline listing "Liftoff" at T+00:00:00 with all engines lit, and the vehicle proceeding through Max q and stage separation — definitively clearing the tower [Starship flight test 12 - Wikipedia](https://en.wikipedia.org/wiki/Starship_flight_test_12).

The vehicle clearly cleared the launch tower (it reached stage separation and a suborbital trajectory before later anomalies), satisfying the question's definition of a "successful launch," which requires only clearing the tower and not achieving orbit or surviving the full flight profile. May 22, 2026 falls within the resolution window, so the answer is YES (1).

Note: An initial launch attempt on May 21, 2026 was scrubbed, but the actual liftoff on May 22, 2026 satisfies the criteria.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-185. `c9fc5d2e-2a6f-53e1-b465-fbb5f57e21dc`

- Present date: `2026-05-29 02:29:31.720129`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will mifepristone remain available via mail-order pharmacy in the United States continuously from May 12 through June 30, 2026, without any interruption due to court orders?

**Resolution criteria**

This question resolves **Yes** if, at all times between 12:00 a.m. UTC on May 12, 2026, and 11:59 p.m. UTC on June 30, 2026, it is legally permissible under federal law for mifepristone to be dispensed via mail-order pharmacy in the United States — i.e., no nationwide court order or injunction is in effect that prohibits such dispensing.

This question resolves **No** if, at any point during this period (on or after May 12, 2026 at 12:00 a.m. UTC), a court order from any U.S. federal court — including the U.S. Supreme Court, any U.S. Court of Appeals, or any U.S. District Court — effectively prohibits the nationwide distribution of mifepristone via mail-order pharmacy, even if only for a single calendar day. An "interruption" is defined as any period of one hour or more during which such a prohibition is legally in effect nationwide, regardless of whether individual pharmacies have already shipped orders.

For purposes of this question, a "mail-order pharmacy" is a pharmacy that dispenses prescription medications to patients via mail or common carrier delivery, as described by the National Association of Boards of Pharmacy (https://nabp.pharmacy/).

Only interruptions that apply nationwide count; state-level restrictions that existed prior to the 5th Circuit litigation do not constitute an interruption.

**Resolution sources:** Official Supreme Court orders (available at https://www.supremecourt.gov/orders/ordersofthecourt), reporting from SCOTUSblog (https://www.scotusblog.com/), Reuters (https://www.reuters.com/), and/or the Associated Press (https://apnews.com/). Resolution is expected to be determinable by July 1, 2026 at 11:59 p.m. UTC based on these sources.

**Pre-cutoff background**

Mifepristone is one of two drugs used in medication abortions in the United States. In 2024, the U.S. Supreme Court ruled in *FDA v. Alliance for Hippocratic Medicine* that the plaintiffs lacked standing to challenge FDA regulations permitting mifepristone to be prescribed via telehealth and dispensed through the mail. However, a new legal challenge arose when the state of Louisiana and other parties sued, and the U.S. Court of Appeals for the 5th Circuit ruled that Louisiana has standing and granted a request to restore an in-person dispensing requirement for mifepristone, effectively barring mail-order access [Court extends temporary order allowing access to abortion pill by mail](https://www.scotusblog.com/2026/05/court-extends-temporary-order-allowing-access-to-abortion-pill-by-mail/).

Manufacturers Danco Laboratories and GenBioPro appealed to the Supreme Court to stay the 5th Circuit's order. On May 4, 2026, Justice Samuel Alito issued an administrative stay temporarily blocking the 5th Circuit's ruling and restoring mail-order access [Supreme Court temporarily extends access to mail-order mifepristone](https://www.catholicworldreport.com/2026/05/11/supreme-court-temporarily-extends-access-to-mail-order-mifepristone/). This stay was initially set to expire on May 11, 2026, and was subsequently extended to at least 5:00 p.m. ET on May 14, 2026 [Court extends temporary order allowing access to abortion pill by mail](https://www.scotusblog.com/2026/05/court-extends-temporary-order-allowing-access-to-abortion-pill-by-mail/) [Supreme Court temporarily extends access to mail-order mifepristone](https://www.catholicworldreport.com/2026/05/11/supreme-court-temporarily-extends-access-to-mail-order-mifepristone/).

As of May 12, 2026, mail-order access to mifepristone is preserved only by this short-term administrative stay. The Supreme Court has not yet decided whether to grant a longer stay or take up the case for further review. If the administrative stay lapses without a longer stay being granted, the 5th Circuit's order barring mail delivery would take effect, interrupting access. The key uncertainty is whether and when the Supreme Court will issue a longer-term stay, and whether any gap in coverage might occur between successive short-term extensions.

**Exact later resolution packet**

The question resolves YES. It required that, at all times from 12:00 a.m. UTC May 12, 2026 through 11:59 p.m. UTC June 30, 2026, no nationwide federal court order barred mail-order dispensing of mifepristone, where an "interruption" is explicitly defined as a period of ONE HOUR OR MORE during which such a nationwide prohibition was legally in effect.

Timeline of the controlling federal orders:
- May 1, 2026: The 5th Circuit ordered restoration of the in-person dispensing requirement (barring mail-order), effective nationwide.
- May 4, 2026: Justice Alito issued an administrative stay pausing the 5th Circuit's order; it was extended on May 11 to expire at 5:00 p.m. ET on May 14, 2026. This stay covered the start of the question window (May 12–14), so mail-order access was legally permissible during those days.
- May 14, 2026: Alito's administrative stay expired at 5:00 p.m. ET. The Supreme Court's full stay order in Danco Laboratories v. Louisiana (No. 25A1207) / GenBioPro v. Louisiana (No. 25A1208) was not released to reporters until 5:26 p.m. ET [Supreme Court allows for access to abortion pill by mail for now](https://www.scotusblog.com/2026/05/court-allows-for-access-to-abortion-pill-by-mail-for-now/). Reed Smith similarly reports the Court acted "approximately 30 minutes after" the administrative stay expired [Supreme Court Reinstates Availability of Mifepristone without In ...](https://www.reedsmith.com/our-insights/blogs/health-industry-washington-watch/102mu2l/supreme-court-reinstates-availability-of-mifepristone-without-in-person-appointme/). This is the only potential gap in coverage during the entire window, and it lasted roughly 26–30 minutes — well under the one-hour threshold. Per the resolution criteria, a sub-one-hour gap does NOT constitute an interruption "regardless of whether individual pharmacies have already shipped orders."

- The Supreme Court's May 14 stay (25A1207) blocks the 5th Circuit's order and remains in effect pending disposition of the appeal in the 5th Circuit and any petition for certiorari; it terminates automatically only if certiorari is denied, or upon the sending down of the judgment if certiorari is granted [[PDF] 25A1207 Danco Laboratories, LLC v. Louisiana (05/14/2026)](https://www.supremecourt.gov/opinions/25pdf/25a1207_21p3.pdf). KFF confirms this preserved nationwide mail-order/telehealth access to mifepristone pending the litigation [Louisiana v. FDA: Access to Mifepristone Back at the Supreme Court](https://www.kff.org/womens-health-policy/louisiana-v-fda-access-to-mifepristone-back-at-the-supreme-court/).

- No later interruption: The Georgetown Law litigation tracker for State of Louisiana v. FDA, last updated June 24, 2026, records no court order after May 14, 2026 reinstating the in-person dispensing requirement or barring mail-order mifepristone nationwide; the most recent filing noted is an appellate order dated June 22, 2026, which did not remove the stay [State of Louisiana et al. v. Food and Drug Administration et al.](https://litigationtracker.law.georgetown.edu/litigation/state-of-louisiana-et-al-v-food-and-drug-administration-et-al/). Thus the stay held continuously through June 30, 2026.

Nationwide vs. state distinction: The resolution criteria count only nationwide federal orders; pre-existing state-level bans (e.g., the ~13 states with near-total mifepristone bans as of May 2026) do not count. Throughout the window, the only nationwide federal order that would have prohibited mail-order dispensing (the 5th Circuit's) was continuously stayed, save for the ~26–30 minute window on May 14 that falls below the one-hour interruption threshold.

Conclusion: Because the only lapse (≈26–30 minutes on May 14, 2026) was shorter than one hour, and the Supreme Court's stay preserved nationwide mail-order access for the remainder of the window, no qualifying "interruption" occurred. The question resolves YES.

Sources: Supreme Court order No. 25A1207 (https://www.supremecourt.gov/opinions/25pdf/25a1207_21p3.pdf) [[PDF] 25A1207 Danco Laboratories, LLC v. Louisiana (05/14/2026)](https://www.supremecourt.gov/opinions/25pdf/25a1207_21p3.pdf); SCOTUSblog, "Court allows for access to abortion pill by mail for now," May 14, 2026 (https://www.scotusblog.com/2026/05/court-allows-for-access-to-abortion-pill-by-mail-for-now/) [Supreme Court allows for access to abortion pill by mail for now](https://www.scotusblog.com/2026/05/court-allows-for-access-to-abortion-pill-by-mail-for-now/); Reed Smith, "Supreme Court Reinstates Availability of Mifepristone without In-Person Appointment" (https://www.reedsmith.com/our-insights/blogs/health-industry-washington-watch/102mu2l/) [Supreme Court Reinstates Availability of Mifepristone without In ...](https://www.reedsmith.com/our-insights/blogs/health-industry-washington-watch/102mu2l/supreme-court-reinstates-availability-of-mifepristone-without-in-person-appointme/); KFF, "Louisiana v. FDA: Access to Mifepristone Back at the Supreme Court" (https://www.kff.org/womens-health-policy/louisiana-v-fda-access-to-mifepristone-back-at-the-supreme-court/) [Louisiana v. FDA: Access to Mifepristone Back at the Supreme Court](https://www.kff.org/womens-health-policy/louisiana-v-fda-access-to-mifepristone-back-at-the-supreme-court/); Georgetown Law Litigation Tracker, State of Louisiana v. FDA (https://litigationtracker.law.georgetown.edu/litigation/state-of-louisiana-et-al-v-food-and-drug-administration-et-al/) [State of Louisiana et al. v. Food and Drug Administration et al.](https://litigationtracker.law.georgetown.edu/litigation/state-of-louisiana-et-al-v-food-and-drug-administration-et-al/).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-186. `6c4732f8-c6a3-59a2-b7c5-26696af55b72`

- Present date: `2026-05-01 11:55:44.204106`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-05-31 00:00:00`

**Question**

Will SpaceX receive FAA launch authorization for Starship Flight 12 by May 31, 2026?

**Resolution criteria**

This question resolves **Yes** if the Federal Aviation Administration (FAA) grants a launch license, license modification, or other official launch authorization permitting SpaceX to conduct Starship Flight 12 (the 12th integrated flight test of the Starship/Super Heavy vehicle, as tracked on [Wikipedia's List of Starship launches](https://en.wikipedia.org/wiki/List_of_Starship_launches)) on or after April 30, 2026 and no later than 23:59 UTC on May 31, 2026.

"FAA launch authorization" means any official FAA action — including a new license, license modification, or launch-specific authorization under an existing license (e.g., VOL 23-129) — that legally permits SpaceX to launch the Starship Flight 12 mission. This is distinct from FCC communications licenses or environmental assessments alone.

The question resolves **No** if no such FAA authorization for Flight 12 is issued by the deadline.

**Resolution source:** The primary resolution source is the [FAA's SpaceX Starship stakeholder engagement page](https://www.faa.gov/space/stakeholder_engagement/spacex_starship) and/or the [FAA commercial space licenses page](https://www.faa.gov/space/licenses). If neither page is updated in time, credible reporting from SpaceX official channels ([spacex.com/updates](https://www.spacex.com/updates)) or major aerospace outlets (e.g., SpaceNews, NASASpaceflight.com, Reuters) confirming FAA authorization may also be used. If Flight 12 actually launches, that constitutes proof of FAA authorization and the question resolves Yes.

**Pre-cutoff background**

SpaceX's Starship/Super Heavy is the largest and most powerful rocket ever built, currently undergoing iterative test flights from its Starbase facility in Boca Chica, Texas. The most recent flight, Flight 11, launched on October 13, 2025 [List of Starship launches](https://en.wikipedia.org/wiki/List_of_Starship_launches). Flight 12 is the next planned test flight and represents a major step: it will be the first launch of the Block 3 (V3) vehicle version and the first launch from Starbase's second orbital launch pad (OLP-2) [List of Starship launches](https://en.wikipedia.org/wiki/List_of_Starship_launches).

As of May 1, 2026, Flight 12 is targeting a launch window in the first two weeks of May 2026. SpaceX must obtain FAA authorization — specifically, a license modification or new launch authorization under its existing Vehicle Operator License (VOL 23-129) — before it can proceed. The FAA's evaluation covers public safety, national security, foreign policy, insurance, and environmental compliance [SpaceX Starship Super Heavy Project at the Boca Chica Launch Site](https://www.faa.gov/space/stakeholder_engagement/spacex_starship). A Final Environmental Assessment for updated Starship operations was completed as of February 13, 2026 [SpaceX Starship Super Heavy Project at the Boca Chica Launch Site](https://www.faa.gov/space/stakeholder_engagement/spacex_starship), but the FAA indicated it was still evaluating SpaceX's license modification request.

FAA licensing has historically been a recurring source of delay for Starship launches. The significant changes for Flight 12 — a new vehicle version (Block 3) and a new launch pad (OLP-2) — add regulatory complexity beyond routine license modifications. SpaceX already holds a launch license (VOL 23-129) for Starship/Super Heavy operations at Boca Chica, but each new vehicle configuration or launch site change requires FAA review and approval before flight.

Flight 11's authorization (the most recent precedent) was granted in October 2025, approximately seven months before the current date [List of Starship launches](https://en.wikipedia.org/wiki/List_of_Starship_launches).

**Exact later resolution packet**

YES. The affirmative evidence is sufficient under the question’s own criteria. SpaceNews reported that “Starship lifted off from the company’s facility at Starbase, Texas, at 6:30 p.m. Eastern on a mission designated Flight 12,” with the article published May 22, 2026 and updated May 23, 2026; URL: https://spacenews.com/spacex-launches-first-starship-v3/ [SpaceX launches first Starship V3 - SpaceNews](https://spacenews.com/spacex-launches-first-starship-v3/). May 22, 2026 is before the deadline of May 31, 2026 at 23:59 UTC, and the criteria state that if Flight 12 actually launches, that constitutes proof of FAA authorization and resolves the question Yes. The same article identifies the mission as “Flight 12,” satisfying the requirement that the evidence specifically concern Starship Flight 12 / the 12th integrated flight test [SpaceX launches first Starship V3 - SpaceNews](https://spacenews.com/spacex-launches-first-starship-v3/).

There is also official FAA licensing evidence: the FAA Dynamic Regulatory System page for VOL 23-129 Rev. 6.0 states that Space Exploration Technologies Corp. is authorized to conduct launches of the Starship-Super Heavy vehicle, and lists VOL 23-129 Rev. 6.0 as issued and effective on May 15, 2026; URL: https://drs.faa.gov/browse/excelExternalWindow/DRSDOCID173891218620231102140506.0001?modalOpened=true [DRS-VOL 23-129 (Rev 6) SpaceX Starship-Super Heavy](https://drs.faa.gov/browse/excelExternalWindow/DRSDOCID173891218620231102140506.0001?modalOpened=true). May 15, 2026 is within the required authorization window of on or after April 30, 2026 and no later than May 31, 2026 at 23:59 UTC.

I am not treating preliminary/non-launch-authorizing items as sufficient: the FAA stakeholder-engagement page did not itself show a Flight 12 launch authorization and instead contained environmental-review material, which is expressly excluded by the criteria as enough on its own; URL: https://www.faa.gov/space/stakeholder_engagement/spacex_starship [SpaceX Starship Super Heavy Project at the Boca Chica Launch Site](https://www.faa.gov/space/stakeholder_engagement/spacex_starship). Likewise, the SpaceX updates page mentioned Flight 12 as the first launch from Pad 2 but did not itself report FAA authorization or launch completion, so it is not the decisive source; URL: https://www.spacex.com/updates [Updates - SpaceX](https://www.spacex.com/updates). The decisive basis is the reported May 22 Flight 12 launch, supplemented by the official FAA VOL 23-129 Rev. 6.0 licensing record [SpaceX launches first Starship V3 - SpaceNews](https://spacenews.com/spacex-launches-first-starship-v3/) [DRS-VOL 23-129 (Rev 6) SpaceX Starship-Super Heavy](https://drs.faa.gov/browse/excelExternalWindow/DRSDOCID173891218620231102140506.0001?modalOpened=true).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-187. `f5cdec0f-f43f-5223-92a1-e53d9d014d23`

- Present date: `2026-05-29 07:00:27.080515`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Israel conduct an airstrike in Beirut's Dahiyeh (southern suburbs) between May 12 and June 30, 2026?

**Resolution criteria**

This question resolves **Yes** if at least one airstrike conducted by Israel strikes a target within Beirut's Dahiyeh (southern suburbs) on or after May 12, 2026, and on or before June 30, 2026 (23:59 UTC).

**Definition of Dahiyeh:** The southern suburbs of Beirut located in the Baabda District of Lebanon [Dahieh - Wikipedia](https://en.wikipedia.org/wiki/Dahieh), encompassing the municipalities of Ghobeiry, Haret Hreik, Bourj el-Barajneh, Ouzai, and Hay El-Saloum, as described in the Wikipedia article on Dahieh (https://en.wikipedia.org/wiki/Dahieh) [Dahieh - Wikipedia](https://en.wikipedia.org/wiki/Dahieh). Strikes on central or northern Beirut (within the Beirut Governorate proper) also count, but strikes in southern Lebanon outside the greater Beirut area do not.

**Definition of airstrike:** Any munition delivered from the air by Israeli forces, including but not limited to strikes from fixed-wing aircraft, helicopters, drones/UAVs, or sea-launched missiles (as the May 6 strike was reportedly launched from an Israeli naval vessel). The key criterion is that the munition impacts within the defined Dahiyeh area or central Beirut.

**Exclusion of prior events:** The May 6, 2026 strike on Haret Hreik that killed Ahmad Balout does NOT count toward resolution, as it occurred before May 12, 2026. Only strikes occurring on or after May 12, 2026 (00:00 UTC) are eligible.

**Resolution source:** Credible reporting from at least one of the following: Reuters (https://www.reuters.com), Associated Press (https://apnews.com), Agence France-Presse, BBC (https://www.bbc.com), Al Jazeera (https://www.aljazeera.com), or the Times of Israel (https://www.timesofisrael.com). Official IDF statements also qualify.

If no such strike is reported by these sources by July 1, 2026, the question resolves **No**.

**Pre-cutoff background**

A ceasefire between Israel and Hezbollah took effect on April 17, 2026. Despite this, on May 6, 2026, Israel carried out its first airstrike on Beirut since the ceasefire, targeting Haret Hreik in Beirut's southern suburbs (Dahiyeh) and killing Radwan Force commander Ahmad Ghaleb Balout. The strike was reported by multiple major outlets including Bloomberg, the Jerusalem Post, and Reuters. Hezbollah's response was described as minimal, though the group threatened retaliation. Al Jazeera commentary from May 11 questioned whether "even the pretence of a ceasefire" was over, suggesting further escalation is plausible but not certain.

Dahiyeh is a predominantly Shia Muslim suburb in the south of Beirut, located in Lebanon's Baabda District [Dahieh - Wikipedia](https://en.wikipedia.org/wiki/Dahieh). It comprises several municipalities including Ghobeiry, Haret Hreik, Bourj el-Barajneh, Ouzai, and Hay El-Saloum [Dahieh - Wikipedia](https://en.wikipedia.org/wiki/Dahieh). Dahiyeh is a known Hezbollah stronghold and has historically been a primary target of Israeli military operations, including during the 2006 Lebanon War and the 2024–2026 conflict.

The key question is whether Israel will repeat such a strike in the Dahiyeh area during the resolution window, given the fragile ceasefire, Hezbollah's ongoing military infrastructure in the area, and Israel's demonstrated willingness to conduct targeted assassinations despite ceasefire frameworks.

**Exact later resolution packet**

The question resolves YES. It asks whether Israel conducted at least one airstrike striking a target within Beirut's Dahiyeh (southern suburbs)—including the municipalities of Ghobeiry, Haret Hreik, Bourj el-Barajneh, Ouzai, and Hay El-Saloum—or central/northern Beirut, on or after May 12, 2026 and on or before June 30, 2026 (23:59 UTC). Multiple qualifying airstrikes occurred, all reported by Reuters (an approved resolution source), all involving munitions delivered from the air (missiles), and all after the excluded May 6 strike:

1. May 28, 2026: An Israeli strike hit a building in Beirut's southern suburbs (Dahiyeh). A Lebanese security source said it was carried out with two precision missiles; two Israeli security sources identified the target as Ali al-Husseini, head of the missile division within the Imam Hussein Division. URL: https://www.reuters.com/world/middle-east/israel-carries-out-strike-beirut-suburbs-first-near-capital-weeks-2026-05-28/ [Israel carries out strike on Beirut suburbs, first near capital in weeks](https://www.reuters.com/world/middle-east/israel-carries-out-strike-beirut-suburbs-first-near-capital-weeks-2026-05-28/)

2. June 7, 2026: The Israeli military struck Hezbollah infrastructure in Beirut's southern suburbs (Dahiyeh) in response to Hezbollah fire toward Israel; Lebanese state media reported two dead and 11 injured. URL: https://www.reuters.com/world/middle-east/israeli-military-says-it-intercepted-two-projectiles-that-crossed-lebanon-2026-06-07/ [Israeli military says it hit Hezbollah in Beirut suburbs](https://www.reuters.com/world/middle-east/israeli-military-says-it-intercepted-two-projectiles-that-crossed-lebanon-2026-06-07/)

3. June 14, 2026: The IDF attacked Hezbollah targets in the Dahiyeh neighbourhood of Beirut, striking an apartment; described as a targeted strike with two missiles. URL: https://www.reuters.com/world/middle-east/israeli-military-says-hezbollah-launched-three-projectiles-towards-northern-2026-06-14/ [Israel attacks Hezbollah targets in Beirut's southern suburbs](https://www.reuters.com/world/middle-east/israeli-military-says-hezbollah-launched-three-projectiles-towards-northern-2026-06-14/)

Each of these events (a) occurred within the resolution window (May 12–June 30, 2026), (b) struck within the defined Dahiyeh area (Haret Hreik/Dahiyeh southern suburbs), (c) is reported by Reuters, and (d) involved munitions delivered from the air (precision missiles). Any one of them alone is sufficient to resolve the question YES; there are three independent confirmations. The excluded May 6, 2026 strike plays no role in this resolution.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-188. `b02bd353-b1f5-5ef2-8db4-a27aeae32229`

- Present date: `2026-05-03 00:52:33.784466`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will a major open-source project (other than curl) publicly announce the suspension or cancellation of its bug bounty program citing AI-generated submissions between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves YES if all of the following conditions are met:

1. **Timing**: A public announcement is made on or after May 1, 2026 00:00 UTC and before June 1, 2026 23:59 UTC.

2. **Qualifying project**: The announcement comes from a major open-source project, defined as a project that meets at least one of the following criteria as of the announcement date:
   - Has 10,000 or more stars on GitHub (or equivalent primary repository host);
   - Is a member or graduated project of the Apache Software Foundation, the Cloud Native Computing Foundation (CNCF), or the Linux Foundation; OR
   - Is listed in the OpenSSF Critical Projects list (https://github.com/ossf/wg-securing-critical-projects).
   The project must NOT be curl (https://github.com/curl/curl).

3. **Action**: The announcement states that the project is suspending, cancelling, or permanently ending its bug bounty program (including withdrawal from a third-party bounty platform such as HackerOne or Bugcrowd).

4. **Stated reason**: The announcement explicitly cites "AI-generated content," "AI-generated submissions," "LLM-generated spam," "AI slop," or substantially similar phrasing referring to artificially-generated or automated low-quality submissions as a reason for the suspension or cancellation.

5. **Public announcement**: The announcement must appear in at least one of the following: (a) a post on the project's official blog or website; (b) a message to an official project mailing list; (c) a commit or pull request merged into the project's primary repository; or (d) an official post on the project's verified social media account. Third-party reporting alone (e.g., a news article) does not suffice unless it links to or quotes from such an official source.

If no qualifying announcement meeting all five conditions is identified by June 1, 2026 23:59 UTC, the question resolves NO.

Note: The IBB closure (March 27, 2026) and Node.js bounty suspension that occurred before May 1, 2026 do NOT count toward resolution, as they predate the eligible window.

**Pre-cutoff background**

In January 2026, the curl project—a widely used open-source networking tool with over 35,000 GitHub stars—terminated its bug bounty program. Maintainer Daniel Stenberg cited an "explosion in AI slop reports" as the primary driver, noting that the rate of confirmed vulnerabilities had plummeted below 5% starting in 2025. The program, which ran since 2019, had confirmed 87 vulnerabilities and paid out over $100,000 before its closure on January 31, 2026 [The end of the curl bug-bounty | daniel.haxx.se](https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/).

This was not an isolated incident. On March 27, 2026, the Internet Bug Bounty (IBB) program—backed by Microsoft, Adobe, and Meta—closed to new project submissions, citing AI-generated bug submissions overwhelming responders. This closure directly led to the suspension of the Node.js bug bounty program, which had relied on IBB for funding [This Week In Security: The Supply Chain Has Problems](https://hackaday.com/2026/04/03/this-week-in-security-the-supply-chain-has-problems/).

As of May 1, 2026, many open-source projects continue to operate bug bounty programs through platforms like HackerOne and Bugcrowd. The question is whether the trend of AI-spam-driven cancellations will claim another major project within the next month. The combination of increasingly capable LLMs, low barriers to automated submission, and limited maintainer resources suggests continued pressure, but projects may also adapt with better filtering or triage mechanisms.

**Exact later resolution packet**

Adjudicated: Turso published an official blog post 'The Wonders of AI: We Are Retiring Our Bug Bounty Program' on May 12, 2026 (within the May 1-June 1 window), explicitly retiring its bug bounty program and citing AI slop ('everybody is being inundated by the slop machine', maintainers spent days closing slop PRs). Turso's primary repo (tursodatabase/turso) has ~19,000 GitHub stars, far exceeding the 10,000 threshold, and is not curl. All five resolution conditions are satisfied via an official project blog source.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-189. `acfed4ef-d8f9-5541-b9a5-0fdcf1c1c0f7`

- Present date: `2026-05-01 17:54:25.748226`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the Israeli government officially begin implementing the High Court's April 26, 2026 ordered financial sanctions against Haredi draft evaders by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between April 30, 2026 00:00 UTC and June 1, 2026 23:59 UTC, the Israeli government or any relevant ministry (e.g., the Labor Ministry, Finance Ministry, or Israel Land Council) takes at least one of the following concrete implementation actions against Haredi yeshiva students who have not reported for IDF service:

1. Issues an official directive, circular, or updated eligibility guideline **revoking or conditioning** access to "target price" housing deals on military service status; OR
2. Issues an official directive **canceling or suspending** daycare center subsidies or after-school program subsidies for families of draft evaders; OR
3. Issues an official directive **canceling or suspending** municipal tax (arnona) discounts or public transportation discounts for draft evaders; OR
4. A formal cabinet decision or ministerial order is published directing the implementation of any of the above sanctions.

The question resolves **No** if none of the above actions are taken by June 1, 2026 23:59 UTC, including if the government seeks and obtains a court extension, passes legislation overriding the ruling, or simply fails to comply.

**Resolution source:** Credible reporting from at least one of the following outlets: [The Times of Israel](https://www.timesofisrael.com/), [Haaretz](https://www.haaretz.com/), [Jerusalem Post](https://www.jpost.com/), [Globes](https://en.globes.co.il/), Reuters, or AP; or official publications on [Israeli government websites](https://www.gov.il/en). Reports must describe an actual implementation step (directive issued, guidelines updated, benefits revoked), not merely a stated intention to comply.

**Pre-cutoff background**

On April 26, 2026, the Israeli [High Court of Justice](https://en.wikipedia.org/wiki/Supreme_Court_of_Israel) ordered the government to enforce the draft of ultra-Orthodox ([Haredi](https://en.wikipedia.org/wiki/Haredi_Judaism)) men into the IDF by implementing personal economic sanctions against draft evaders [The Dramatic High Court Ruling on Economic Sanctions Against ...](https://en.idi.org.il/articles/64062). The Court set "rapid and rigid timetables" of 21 to 35 days from the ruling date for the government to act, meaning deadlines fall between approximately May 17 and May 31, 2026.

The specific sanctions ordered include:
- **Housing:** Denial of access to "[target price](https://en.idi.org.il/articles/63535)" deals for discounted homes, to be implemented by the [Israel Land Council](https://land.gov.il/) within 21 days (by ~May 17, 2026).
- **Childcare:** Complete cancellation of subsidies for daycare centers and after-school programs for children of draft evaders, to be implemented by the [Labor Ministry](https://www.gov.il/en/departments/ministry_of_labor) within 21 days.
- **Municipal taxes and transit:** Cancellation of discounts on municipal taxes ([arnona](https://en.wikipedia.org/wiki/Arnona)) and public transportation, to be implemented within 35 days (by ~May 31, 2026) [The Dramatic High Court Ruling on Economic Sanctions Against ...](https://en.idi.org.il/articles/64062).

The affected population is Haredi yeshiva students of conscription age who have not reported for military service as required under existing law. As of May 1, 2026, these subsidies remain in effect and have not yet been revoked. The Israeli government faces intense political pressure from [Haredi coalition partners](https://www.timesofisrael.com/liveblog_entry/haredi-leaders-assail-oppressive-courts-order-to-sanction-draft-evaders/) — including [United Torah Judaism](https://en.wikipedia.org/wiki/United_Torah_Judaism) and [Shas](https://en.wikipedia.org/wiki/Shas) — who have publicly condemned the ruling as "oppressive" and are pressuring the government to delay or circumvent it. A proposed [draft exemption law was set aside](https://en.idi.org.il/articles/63729) as of March 2026, making a legislative override unlikely but not impossible within the timeframe. Government ministries have also raised objections about privacy and feasibility concerns regarding implementation [The Dramatic High Court Ruling on Economic Sanctions Against ...](https://en.idi.org.il/articles/64062).

**Exact later resolution packet**

Adjudicated: Within the resolution window, the Israel Land Authority Council passed a formal decision (reported May 17 and approved/published around May 24, 2026) conditioning eligibility for discounted 'target price' housing lotteries on IDF data showing neither applicant nor spouse is an unregularized draft-obligated person, thereby revoking access for Haredi draft evaders. This is a concrete implementation step satisfying criteria #1 and #4 and is reported by named resolution sources (Haaretz/TheMarker), not a mere statement of intent. An initial automated resolution missed the Land Authority Council decision; the Knesset daycare-restoration bill it cited does not negate the housing implementation.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-190. `8f4e1858-5e5f-5dfa-91e9-e1287287af3d`

- Present date: `2026-05-14 00:07:35.928612`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-15T00:00:00`

**Question**

Will the Quad Foreign Ministers' Meeting in New Delhi (May 2026) announce a new named initiative or agreement specifically on critical minerals?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 (00:00 UTC) and no later than July 1, 2026 (23:59 UTC), an official joint statement, communiqué, or press release issued in connection with the Quad Foreign Ministers' Meeting explicitly announces a **new named initiative or agreement** specifically focused on critical minerals.

**Definitions and requirements:**

1. **"Named initiative or agreement"**: A formally titled program, partnership, framework, or agreement that is given a distinct proper-noun name in the official text (e.g., "Quad Critical Minerals Partnership," "Quad Minerals Supply Chain Framework," "Quad Critical Minerals Trade Agreement"). The name must appear as a capitalized title or be introduced with language such as "we are launching," "we announce," or "we establish."

2. **"New"**: The initiative or agreement must not have been previously announced. Reaffirmations of the existing 2023 "Quad Critical Minerals Initiative" do not count unless a substantively new and distinctly named successor, expansion, or separate agreement is announced.

3. **"Specifically on critical minerals"**: The named initiative must be primarily dedicated to critical minerals (as defined by any Quad member's official critical minerals list—see background). A broader initiative on "technology" or "supply chains" that merely mentions critical minerals as one component does not qualify.

4. **General mentions excluded**: Statements containing only general language about "cooperation on critical minerals," "strengthening supply chains," "working together on minerals," or similar phrasing without a specific new proper-noun-titled initiative do not qualify.

**Resolution source**: The official joint statement or outcome document published on the India Ministry of External Affairs website (https://www.mea.gov.in/bilateral-documents.htm), the U.S. Department of State website (https://www.state.gov/), the Australian Department of Foreign Affairs and Trade website (https://www.dfat.gov.au/), or the Japanese Ministry of Foreign Affairs website (https://www.mofa.go.jp/). If no official statement is published on these sites, credible reporting from Reuters, AP, or Bloomberg confirming or denying the announcement will be used.

If no such announcement is made by July 1, 2026 (23:59 UTC), the question resolves **No**.

**Pre-cutoff background**

The Quadrilateral Security Dialogue ("Quad")—comprising Australia, India, Japan, and the United States—is scheduled to hold a Foreign Ministers' Meeting in New Delhi from approximately May 24–26, 2026 (UTC+5:30) [Rubio to Visit India for Quad Talks in May 2026 - GKToday](https://www.gktoday.in/rubio-to-visit-india-for-quad-talks-in-may-2026/). Critical minerals and emerging technology are key agenda items for this meeting, aimed at countering China's dominance in mineral supply chains [Quad foreign ministers meet in New Delhi to follow Donald Trump's ...](https://m.economictimes.com/news/india/quad-foreign-ministers-meet-in-delhi-to-follow-donald-trumps-china-visit/articleshow/130866902.cms).

**Prior Quad critical minerals cooperation:** In 2023, the Quad launched the "Quad Critical Minerals Initiative" at the Foreign Ministers' Meeting in Washington, described as "an ambitious expansion of our partnership to strengthen economic security" (see the 2024 Joint Statement at https://www.mea.gov.in/bilateral-documents.htm?dtl/38044/Quad+Foreign+Ministers+Meeting+Joint+Statement) [Quad Foreign Ministers' Meeting Joint Statement](https://www.mea.gov.in/bilateral-documents.htm?dtl/38044/Quad+Foreign+Ministers+Meeting+Joint+Statement). However, no Quad Foreign Ministers' Meeting has taken place since 2024, and the initiative has not been upgraded to a formal trade agreement or binding framework.

**U.S.-Japan Action Plan on Critical Minerals (March 2026):** On March 19, 2026, the U.S. and Japan announced a bilateral Action Plan on Critical Minerals, focused on reducing reliance on China for rare earths and other strategic minerals (https://ustr.gov/about/policy-offices/press-office/press-releases/2026/march/ambassador-jamieson-greer-announces-us-japan-action-plan-critical-minerals). This bilateral deal raises the question of whether a broader Quad-wide agreement could follow.

**Obstacles:** ASPI's 2026 Darwin Dialogue highlighted widespread disparities in national critical-mineral lists, priorities, capacities, and ambitions among Quad members. U.S. tariffs and trade policy tensions add further complexity. Think tanks such as AFSA have called for a formal "Quad Minerals Agreement" but achieving consensus among four nations with different mining interests remains challenging.

**Definition of "critical minerals":** For this question, "critical minerals" refers to minerals identified as critical or strategic by any Quad member government, including but not limited to those on the U.S. Geological Survey's Critical Minerals List (https://www.usgs.gov/news/national-news-release/us-geological-survey-releases-2022-list-critical-minerals), Australia's Critical Minerals Strategy list, Japan's list of specified critical minerals, or India's Critical Minerals list published by the Ministry of Mines.

**Exact later resolution packet**

The question resolves **YES**.

**Antecedent check (not a true conditional, but confirming the meeting occurred):** The Quad Foreign Ministers' Meeting took place in New Delhi on May 26, 2026, within the resolution window (May 12 – July 1, 2026). This is confirmed by the official joint statement published on U.S. government sites dated 2026-05-26 [2026 Quad Foreign Ministers' Meeting in New Delhi](https://www.state.gov/releases/office-of-the-spokesperson/2026/05/2026-quad-foreign-ministers-meeting-in-new-delhi) [Joint Statement from the Quad Foreign Ministers' Meeting in New Delhi](https://in.usembassy.gov/joint-statement-from-the-quad-foreign-ministers-meeting-in-new-delhi/).

**A new named initiative specifically on critical minerals was announced:**
- The official U.S. Department of State fact sheet for the 2026 Quad Foreign Ministers' Meeting states, under "Economic Prosperity and Security": "The Quad partners are pleased to announce **the new Quad Critical Minerals Initiative Framework**, which will guide Quad partners to leverage economic policy tools and coordinate investment to strengthen critical minerals supply chains, including in mining, processing, and recycling." (https://www.state.gov/releases/office-of-the-spokesperson/2026/05/2026-quad-foreign-ministers-meeting-in-new-delhi) [2026 Quad Foreign Ministers' Meeting in New Delhi](https://www.state.gov/releases/office-of-the-spokesperson/2026/05/2026-quad-foreign-ministers-meeting-in-new-delhi)
- The joint statement republished by the U.S. Embassy in India (paragraph 17) states: "To advance our vision for fair and diversified critical minerals markets, **we are pleased to announce the Quad Critical Minerals Framework**, which will guide how Quad partners can leverage economic policy tools and coordinate...investment to strengthen critical minerals supply chains, including in mining, processing, and recycling." (https://in.usembassy.gov/joint-statement-from-the-quad-foreign-ministers-meeting-in-new-delhi/) [Joint Statement from the Quad Foreign Ministers' Meeting in New Delhi](https://in.usembassy.gov/joint-statement-from-the-quad-foreign-ministers-meeting-in-new-delhi/)

**Checklist verification:**
1. Within the window (announced May 26, 2026). ✓
2. Specific proper-noun capitalized name: "Quad Critical Minerals Framework" / "Quad Critical Minerals Initiative Framework." ✓
3. Explicit launching language: "we are pleased to announce" and "the new." ✓ [2026 Quad Foreign Ministers' Meeting in New Delhi](https://www.state.gov/releases/office-of-the-spokesperson/2026/05/2026-quad-foreign-ministers-meeting-in-new-delhi) [Joint Statement from the Quad Foreign Ministers' Meeting in New Delhi](https://in.usembassy.gov/joint-statement-from-the-quad-foreign-ministers-meeting-in-new-delhi/)
4. Primarily and specifically dedicated to critical minerals (mining, processing, recycling, supply chains). ✓
5. Described as **new** — the State Dept text explicitly says "the new Quad Critical Minerals Initiative Framework," distinguishing it from the 2023 "Quad Critical Minerals Initiative." It is a distinctly-named Framework (a substantively new/expanded successor), not a mere reaffirmation. ✓
6. Sourced to official U.S. State Department and the joint statement text. ✓

All requirements of the resolution criteria are satisfied, so the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-191. `531f6881-c239-5a7f-92cf-139a4785b338`

- Present date: `2026-05-01 10:26:02.242608`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-05-20 00:00:00`

**Question**

Will the Democratic Party of Korea and the Rebuilding Korea Party announce a formal candidate unification agreement for at least one metropolitan mayor or provincial governor race between April 30 and May 20, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after April 30, 2026 (00:00 KST, UTC+9) and on or before May 20, 2026 (23:59 KST, UTC+9), the Democratic Party of Korea and the Rebuilding Korea Party publicly announce a formal candidate unification agreement for at least one of the 17 metropolitan mayor or provincial governor races in the June 3, 2026 local elections.

**Definitions:**

- **"Formal candidate unification agreement"** means a publicly announced, official agreement between both parties (confirmed by authorized representatives of both parties) in which either:
  1. **Candidate unification**: Both parties agree to support a single joint candidate in a specific race, replacing separate candidacies (see https://en.wikipedia.org/wiki/Candidate_unification for context on this Korean electoral practice); OR
  2. **Mutual withdrawal**: One party officially withdraws or declines to register its candidate in a specific race, pursuant to an explicit inter-party agreement, to consolidate support behind the other party's candidate.

- Informal endorsements, expressions of support, or unilateral decisions by one party without a confirmed bilateral agreement do **not** count.

- **The 17 metropolitan mayor/governor races** are the elections for the heads of South Korea's 17 first-level administrative divisions: Seoul, Busan, Daegu, Incheon, Gwangju, Daejeon, Ulsan, Sejong Special Autonomous City, Gyeonggi, Gangwon, North Chungcheong, South Chungcheong, North Jeolla, South Jeolla, North Gyeongsang, South Gyeongsang, and Jeju Special Self-Governing Province (listed at https://en.wikipedia.org/wiki/2026_South_Korean_local_elections).

**Resolution source:** The agreement must be reported by at least one of the following credible sources: Yonhap News Agency (https://en.yna.co.kr/), The Korea Herald (https://www.koreaherald.com/), The Korea Times (https://www.koreatimes.co.kr/), or Chosun Ilbo English (https://english.chosun.com/). If no such report appears by May 20, 2026 (23:59 KST), the question resolves **No**.

**Pre-cutoff background**

South Korea's 2026 local elections are scheduled for June 3, 2026, including races for all 17 first-level administrative division heads (metropolitan mayors and provincial governors) [2026 South Korean local elections - Wikipedia](https://en.wikipedia.org/wiki/2026_South_Korean_local_elections). The 17 races are: Seoul, Busan, Daegu, Incheon, Gwangju, Daejeon, Ulsan, Sejong, Gyeonggi, Gangwon, North Chungcheong, South Chungcheong, North Jeolla, South Jeolla, North Gyeongsang, South Gyeongsang, and Jeju (see https://en.wikipedia.org/wiki/2026_South_Korean_local_elections).

The Democratic Party of Korea (DPK, 더불어민주당) is the largest progressive party and currently the ruling party. The Rebuilding Korea Party (RKP, 조국혁신당), led by Cho Kuk, is a smaller progressive party whose support base overlaps significantly with the DPK's. Splitting the progressive vote in competitive races could benefit the conservative People Power Party.

As of late April 2026, the DPK has decided to centralize candidate unification discussions at the party headquarters level rather than leaving them to regional branches. DPK Secretary-General Cho Seungrye is scheduled to meet with counterparts from allied parties to discuss consolidation [Democratic Party: "Central Committee to Lead Initial Discussions on ...](https://www.asiae.co.kr/en/article/2026042711241255563). The DPK spokesperson stated that "the word 'concession' does not exist in the consolidation process" and any agreement must be reached through "mutual consensus" [Democratic Party: "Central Committee to Lead Initial Discussions on ...](https://www.asiae.co.kr/en/article/2026042711241255563). Specific races under discussion include Ulsan mayor and South Gyeongsang governor, among others. Earlier in 2026, the two parties discussed merger and alliance possibilities but had not reached a formal agreement. The RKP has demanded that the DPK withdraw candidates in certain key regions as a precondition, creating friction in negotiations.

The tight timeline before the June 3 election day—and the legal candidate registration deadlines—means that any formal unification must happen soon if it is to occur at all.

**Exact later resolution packet**

Adjudicated: A formal DPK-RKP candidate unification for the Ulsan mayoral race (one of the 17 metropolitan/provincial races) occurred on May 14, 2026 -- within the Apr 30-May 20 KST window -- when Rebuilding Korea Party candidate Hwang Myung-pil agreed to unify behind/withdrew in favor of Democratic Party candidate Kim Sang-wook, satisfying the 'mutual withdrawal'/candidate-unification prong. Seoul Economic Daily (May 15, 2026) independently confirms: 'Democratic Party candidate Kim Sang-wook and Rebuilding Korea Party candidate Hwang Myung-pil had already agreed to unify behind Kim.' opus48 cites a matching Chosun Ilbo English article (one of the four mandated sources), 'Pro-Government Parties Unify Ulsan Mayoral Candidate', dated May 15, 2026, reporting the same event with the same candidate names. chosun.com is entirely blocked to this web crawler so I could not independently load that exact URL (hence medium, not high, confidence), but the underlying event is firmly corroborated and gpt55's NO rested on an incomplete source sweep that missed the May 15 Chosun report (it checked only a May 10 and a May 18 article). Note: a SEPARATE, later DPK-Progressive Party primary (a different party) collapsed/was disputed after May 20 -- that is not the DPK-RKP agreement and does not bear on resolution.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-192. `bba43cbe-65ca-5a13-a040-271ecf0773f4`

- Present date: `2026-05-29 00:48:28.595690`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the U.S. Supreme Court rule in favor of Monsanto on federal preemption in Monsanto Co. v. Durnell (No. 24-1068) by July 1, 2026?

**Resolution criteria**

This question resolves YES if the Supreme Court of the United States issues a final opinion in Monsanto Co. v. Durnell (No. 24-1068) on or after May 12, 2026 (Eastern Time) and on or before July 1, 2026, 11:59 PM Eastern Time, that reverses the judgment of the Missouri Court of Appeals on the ground that the Federal Insecticide, Fungicide, and Rodenticide Act (FIFRA) preempts the state-law failure-to-warn claims at issue—i.e., holds that federal pesticide labeling law displaces state tort claims requiring additional cancer warnings on EPA-approved labels.

This question resolves NO if any of the following occur by July 1, 2026, 11:59 PM ET:
- The Court affirms the Missouri Court of Appeals judgment (ruling against Monsanto on preemption);
- The Court dismisses the case as improvidently granted (DIG);
- The Court issues a split or partial decision that does NOT reverse the lower court judgment on federal preemption grounds (e.g., remands on other grounds without reaching the preemption question, or rules in Monsanto's favor on narrow procedural grounds without establishing FIFRA preemption of failure-to-warn claims);
- No opinion is issued by July 1, 2026, 11:59 PM ET.

For clarity: a decision that vacates and remands with instructions consistent with a holding that FIFRA preempts state failure-to-warn claims counts as YES. A decision that vacates and remands on other grounds (e.g., for reconsideration of damages only) without holding that FIFRA preempts failure-to-warn claims counts as NO.

Primary resolution source: The official opinion as published on the Supreme Court of the United States website at https://www.supremecourt.gov/opinions/slipopinions.aspx. Secondary sources include SCOTUSblog (https://www.scotusblog.com/cases/monsanto-company-v-durnell/) and major wire services (Reuters, AP).

**Pre-cutoff background**

The U.S. Supreme Court is considering Monsanto Co. v. Durnell (Docket No. 24-1068), a landmark case that could reshape pesticide liability law in the United States. The case arises from a Missouri jury verdict awarding $1.25 million to John Durnell, who alleged his non-Hodgkin lymphoma was caused by exposure to Monsanto's herbicide Roundup (active ingredient: glyphosate) and that Monsanto failed to warn him of cancer risks [Justices debate who gets to decide that pesticide labels need a ...](https://www.scotusblog.com/2026/04/justices-debate-who-gets-to-decide-that-pesticide-labels-need-a-cancer-warning/).

The central legal question is whether the Federal Insecticide, Fungicide, and Rodenticide Act (FIFRA) — the federal statute governing pesticide registration and labeling (see https://www.law.cornell.edu/uscode/text/7/136v) — preempts state-law "failure-to-warn" claims. "Federal preemption" refers to the constitutional doctrine under which federal law displaces or supersedes state law when the two conflict. A "failure-to-warn" claim is a type of tort claim alleging that a product manufacturer failed to adequately warn consumers of known risks. Monsanto/Bayer argues that FIFRA's uniformity provision bars states from imposing labeling requirements different from those approved by the EPA, which has concluded glyphosate does not pose a cancer risk [US Supreme Court split over Bayer's fight against Roundup lawsuits](https://www.reuters.com/legal/government/us-supreme-court-hears-bayers-fight-against-roundup-lawsuits-2026-04-27/). Durnell argues that FIFRA does not explicitly bar state-level misbranding lawsuits and that state tort law should remain available for consumer protection [Justices debate who gets to decide that pesticide labels need a ...](https://www.scotusblog.com/2026/04/justices-debate-who-gets-to-decide-that-pesticide-labels-need-a-cancer-warning/).

The Supreme Court granted certiorari on January 16, 2026, and heard oral arguments on April 27, 2026 [Monsanto Co. v. Durnell - Oral Arguments - Supreme Court](https://www.supremecourt.gov/oral_arguments/audio/2025/24-1068). During arguments, the Court appeared divided. Justice Gorsuch questioned why preemption was necessary if the EPA could also pursue misbranding claims; Chief Justice Roberts and Justice Kavanaugh expressed concern about a "patchwork" of state standards undermining federal uniformity; Justice Jackson questioned whether states should be able to act during the EPA's 15-year reassessment cycle [Justices debate who gets to decide that pesticide labels need a ...](https://www.scotusblog.com/2026/04/justices-debate-who-gets-to-decide-that-pesticide-labels-need-a-cancer-warning/) [US Supreme Court split over Bayer's fight against Roundup lawsuits](https://www.reuters.com/legal/government/us-supreme-court-hears-bayers-fight-against-roundup-lawsuits-2026-04-27/). Reuters reported Bayer shares dropped 6.5% following arguments due to the apparent split. A ruling is expected by the end of the Court's term in late June 2026 [US Supreme Court split over Bayer's fight against Roundup lawsuits](https://www.reuters.com/legal/government/us-supreme-court-hears-bayers-fight-against-roundup-lawsuits-2026-04-27/). A Bayer victory could effectively eliminate tens of thousands of remaining Roundup lawsuits; Monsanto has proposed a $7.25 billion settlement to resolve remaining claims.

**Exact later resolution packet**

The question resolves YES.

The U.S. Supreme Court issued its final opinion in Monsanto Co. v. Durnell (No. 24-1068) on June 25, 2026, which falls squarely within the resolution window of May 12, 2026 to July 1, 2026 (11:59 PM ET).

Holding/disposition: The Court REVERSED the judgment of the Missouri Court of Appeals and remanded, holding that the Federal Insecticide, Fungicide, and Rodenticide Act (FIFRA) expressly preempts state-law failure-to-warn claims that would require a pesticide manufacturer to add a cancer warning to an EPA-approved label. This is precisely the preemption ground specified in the resolution criteria for a YES.

Sources confirming this:
- Official SCOTUS slip opinion (https://www.supremecourt.gov/opinions/25pdf/24-1068_n7ip.pdf): The Court reversed the Missouri Court of Appeals, holding FIFRA expressly preempts Durnell's state-law failure-to-warn claim; opinion delivered June 25, 2026 [[PDF] 24-1068 Monsanto v. Durnell (06/25/2026) - Supreme Court](https://www.supremecourt.gov/opinions/25pdf/24-1068_n7ip.pdf).
- SCOTUSblog case page: "Reversed and remanded, 7-2, in an opinion by Brett Kavanaugh on Jun 25, 2026. Justice Thomas wrote a concurring opinion. Justice Jackson wrote a dissenting..." confirming the Court reversed the Missouri Court of Appeals on FIFRA preemption grounds [Monsanto Company v. Durnell (24-1068) - SCOTUSblog](https://www.scotusblog.com/cases/monsanto-company-v-durnell/).
- Crowell & Moring client alert titled "Supreme Court Holds FIFRA Preempts State Failure-to-Warn Claims," describing a 7-2 ruling on June 25, 2026 that FIFRA preempts state failure-to-warn claims challenging EPA-approved labels [Supreme Court Rules FIFRA Preempts State Failure-to-Warn Claims](https://www.crowell.com/en/insights/client-alerts/supreme-court-holds-fifra-preempts-state-failure-to-warn-claims-challenging-epa-approved-pesticide-labels).
- Stanford Law School commentary confirming a 7-2 ruling in favor of Monsanto holding FIFRA preempts the state-law failure-to-warn claims [Thoughts on Supreme Court's Monsanto Co. v Durnell Decision](https://law.stanford.edu/2026/06/26/thoughts-on-monsanto-co-v-durnell/).
- Additional corroboration from Google results: Ballotpedia ("reversed and remanded. Vote 7-2"), Bayer press release ("7:2 landmark ruling"), Dechert/Mayer Brown/Holland & Knight/Dorsey & Whitney legal alerts, NPR, and Washington Post — all confirming the Court reversed the Missouri Court of Appeals on FIFRA express-preemption grounds.

This is a clean "reverse" (not a DIG, not an affirmance, not a remand on non-preemption/procedural grounds), issued within the window, and it establishes FIFRA preemption of failure-to-warn claims — satisfying the YES criteria exactly.

Note on a conflicting data point: One automated read of the Ballotpedia page returned a claim of a 5-4 affirmance authored by Justice Kagan holding FIFRA does NOT preempt. This is contradicted by the actual Ballotpedia snippet ("reversed and remanded. Vote 7-2. Majority [Kavanaugh]") and by every other authoritative source, including the official opinion PDF and SCOTUSblog. It is a hallucinated/erroneous read and is disregarded.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):
