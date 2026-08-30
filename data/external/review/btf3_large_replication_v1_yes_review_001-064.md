# btf3_large_replication_v1 — realized YES review chunk YES-001–YES-064

> Display chunk of the immutable queue (`btf3_large_replication_v1_yes_queue.json`). Review strictly top-to-bottom; stop only when this bucket reaches 128 ACCEPTs overall. Do not skip ahead, reorder, or prefer better-looking questions. A REJECT/UNSURE permanently consumes its queue slot and is never resampled, re-reviewed, or hand-repaired.

All four gates must hold to ACCEPT. On REJECT or UNSURE write exactly one line of reason.

### YES-1. `67bc3f9e-9e8d-509f-8c6b-3d6cfce483bb`

- Present date: `2026-04-30 16:50:14.584685`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the Israel-Lebanon ceasefire still be in effect on June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, as of June 1, 2026 at 23:59 UTC, a ceasefire or cessation of hostilities between Israel and Lebanon—whether the original April 16 ceasefire, its April 23 extension, or any successor/modified ceasefire agreement reached after the April 23 extension—is still in effect.

This question resolves **No** if the ceasefire is terminated before June 1, 2026 at 23:59 UTC. Termination is defined as any of the following occurring on or after April 30, 2026:

1. An official declaration by the government of Israel or Lebanon (including via a senior government spokesperson) that the ceasefire has ended or that military operations have resumed; OR
2. Credible reporting by at least two major international news agencies (e.g., Reuters, AP, BBC, NYT) that full-scale military operations (defined as sustained airstrikes or ground offensives beyond the existing buffer zone, not isolated incidents or skirmishes) have resumed between Israeli forces and Hezbollah/Lebanese forces, absent a ceasefire framework.

If the ceasefire expires on or around May 14 and no new extension or successor agreement is announced, the question resolves **No** unless a replacement ceasefire or cessation of hostilities is established before June 1, 2026 at 23:59 UTC.

**Resolution sources:** Reuters (https://www.reuters.com/world/middle-east/), AP News (https://apnews.com/hub/israel), and UNIFIL press releases (https://unifil.unmissions.org/unifil-press-releases).

**Pre-cutoff background**

On April 16, 2026, Israel and Lebanon implemented a cessation of hostilities for an initial period of ten days, brokered by the United States. On April 23, 2026, following high-level talks at the White House, President Trump announced that the ceasefire would be extended for an additional three weeks [Lebanon-Israel ceasefire extended by three weeks after Oval Office ...](https://www.reuters.com/world/middle-east/lebanon-seek-ceasefire-extension-us-hosted-talks-with-israel-2026-04-23/), putting the expiry of the current extension around May 14, 2026.

As of late April 2026, the ceasefire remains fragile. Israel continues to occupy a self-declared buffer zone extending 5–10 km into southern Lebanon [Lebanon-Israel ceasefire extended by three weeks after Oval Office ...](https://www.reuters.com/world/middle-east/lebanon-seek-ceasefire-extension-us-hosted-talks-with-israel-2026-04-23/). Israeli strikes have continued during the ceasefire period, killing civilians, and Hezbollah has not fully disarmed in the border area. Lebanon is seeking Israeli withdrawal, an end to demolitions, and border delineation, while Israel is focused on neutralizing Hezbollah [Lebanon-Israel ceasefire extended by three weeks after Oval Office ...](https://www.reuters.com/world/middle-east/lebanon-seek-ceasefire-extension-us-hosted-talks-with-israel-2026-04-23/). The ceasefire's survival through June 1 depends on whether the parties negotiate a further extension or permanent deal before the current extension expires around May 14, and whether escalatory incidents trigger a collapse before then.

**Exact later resolution packet**

The question resolves YES because a ceasefire/cessation of hostilities between Israel and Lebanon was still in effect as of June 1, 2026, 23:59 UTC.

Key evidence:
- On May 15, 2026, Israel and Lebanon agreed to a 45-day extension of the ceasefire following U.S.-brokered talks in Washington, as reported by Reuters (resolution source) [0595c8]. A 45-day extension from May 15 runs to approximately June 29, 2026 — well past the June 1 deadline [0595c8].
- The Wikipedia article on the 2026 Israel–Lebanon ceasefire confirms the May 15 (initial period followed by extension) and notes that on June 1, Israel and Hezbollah agreed to a ceasefire, with Israel committing not to target Beirut's southern suburbs and Hezbollah vowing not to attack Israel [3457ba]. This confirms a ceasefire framework remained in place at the deadline.
- While Israeli strikes and isolated incidents/violations occurred between April 30 and late May 2026 (e.g., strikes killing civilians), these are categorized as ceasefire violations rather than a formal termination, and there was no official declaration by either government that the ceasefire had ended, nor credible reporting of resumed full-scale military operations beyond the buffer zone absent a ceasefire framework [3457ba].

Therefore neither termination condition (official declaration of ending OR two-agency reporting of full-scale operations) was met. The ceasefire was in effect on June 1, 2026.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-2. `b68d6dee-5a6b-59e6-9e65-4490ce1e3347`

- Present date: `2026-04-30 17:30:58.483440`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will President Trump and President Xi Jinping hold an in-person bilateral meeting between April 30 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after April 30, 2026 and on or before June 1, 2026 (all dates interpreted in UTC), President Donald Trump and President Xi Jinping hold an in-person bilateral meeting.

**Definition of "in-person bilateral meeting":** A scheduled, formal meeting where both heads of state are physically present in the same room or venue for the purpose of diplomatic discussion between the United States and China, lasting at least 30 minutes. Brief informal encounters (e.g., a handshake or short exchange on the sidelines of a multilateral event without a dedicated bilateral session) do not count. A meeting held as a formal bilateral session on the sidelines of a multilateral summit does count, provided it is a dedicated U.S.-China session.

**Resolution source:** Official confirmation from the White House (https://www.whitehouse.gov/) or the Chinese Ministry of Foreign Affairs (https://www.fmprc.gov.cn/eng/), or consistent reporting from at least two of the following credible news agencies: Reuters (https://www.reuters.com/), Associated Press (https://apnews.com/), AFP, or Bloomberg. The source must confirm that the meeting physically took place (not merely that it was scheduled).

If no such meeting is confirmed by 23:59 UTC on June 1, 2026, the question resolves **No**.

**Pre-cutoff background**

As of late April 2026, U.S. President Donald Trump is scheduled to visit China for a summit with President Xi Jinping on May 14–15, 2026. This would be the first visit to China by an American president in eight years [https://www.reuters.com/world/us/with-tariffs-stalled-trumps-china-policy-drifts-2026-04-21/](https://www.reuters.com/world/us/with-tariffs-stalled-trumps-china-policy-drifts-2026-04-21/). However, the summit was previously postponed from late March 2026 due to the ongoing Iran conflict [https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/](https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/). The U.S.-China relationship remains tense, characterized by tit-for-tat tariffs and what has been described as an "adrift" and "erratic" China policy from the Trump administration [https://www.reuters.com/world/us/with-tariffs-stalled-trumps-china-policy-drifts-2026-04-21/](https://www.reuters.com/world/us/with-tariffs-stalled-trumps-china-policy-drifts-2026-04-21/). The volatile geopolitical environment—including the Iran war and unresolved trade disputes—creates genuine uncertainty about whether the summit will proceed as currently scheduled or face another postponement.

Key sources:
- Reuters, "Trump's trade war with China in focus ahead of May summit" (April 6, 2026): https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/
- Reuters, "With tariffs stalled, Trump's China policy drifts" (April 21, 2026): https://www.reuters.com/world/us/with-tariffs-stalled-trumps-china-policy-drifts-2026-04-21/

**Exact later resolution packet**

The question resolves YES. President Trump and President Xi Jinping held an in-person, formal bilateral meeting in Beijing on May 14–15, 2026, well within the question's resolution window (April 30 – June 1, 2026, UTC).

Evidence:
- Reuters ("Trump leaves Beijing with few wins but warm words for Xi," dated May 14, updated May 15, 2026) confirms Trump spent two days in Beijing holding closed-door talks with Xi Jinping [95ff62]. URL: https://www.reuters.com/world/china/trump-xi-set-second-day-talks-after-taiwan-warning-2026-05-14/
- Associated Press ("Takeaways from Trump's trip to China," dated May 16, 2026) confirms Trump made the trip to China and held "bilateral meetings" with Xi covering Iran, trade, technology, and Taiwan, with photos captioned Friday, May 15, 2026 [31b897]. URL: https://apnews.com/article/trump-xi-china-trade-iran-taiwan-f6c59000412653e445acbf9672ac7f47
- An official U.S. government readout ("Readout of President Trump's Meeting With Chinese President Xi Jinping," U.S. Embassy in China) confirms the formal meeting occurred on May 15, 2026, describing substantive diplomatic discussions [7333f2]. URL: https://china.usembassy-china.org.cn/readout-of-president-trumps-meeting-with-chinese-president-xi-jinping/

These satisfy all resolution criteria:
1. Duration ≥30 minutes: The leaders held a multi-day state-visit summit (two full days of talks at the Great Hall of the People and Zhongnanhai), vastly exceeding the 30-minute minimum [95ff62][31b897].
2. Within UTC date range: The talks occurred May 14–15, 2026, inside the April 30 – June 1, 2026 window [95ff62][31b897][7333f2].
3. Multiple allowed agencies: Both Reuters and AP (two of the explicitly permitted agencies) report consistently that the meeting physically took place [95ff62][31b897].
4. Formal bilateral session: This was a dedicated U.S.-China state-visit summit, not a sideline handshake; an official government readout confirms its formal bilateral nature [7333f2].
5. Meeting physically took place (not merely scheduled): All sources report on the completed meeting in the past tense, including Trump leaving Beijing afterward and calling the trip a success [95ff62][31b897].

Therefore the antecedent is fully met and the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-3. `9bad90f8-e1dd-50b2-8f05-4c54ca424c84`

- Present date: `2026-05-01 11:08:05.322528`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-05-26 00:00:00`

**Question**

Will incumbent Camera Bartolotta win the Republican primary for Pennsylvania Senate District 46 on May 19, 2026?

**Resolution criteria**

This question resolves YES if Camera Bartolotta receives the most votes cast in the Republican primary for Pennsylvania Senate District 46 on May 19, 2026, as reported by the official Pennsylvania Department of State election returns website (https://www.electionreturns.pa.gov/). It resolves NO if any other candidate (including Albert Michael Buchtan) receives more votes than Bartolotta.

If the official results on the PA Department of State website are not yet available by June 1, 2026 at 23:59 UTC, credible news reporting from the Associated Press, Spotlight PA, Pittsburgh Post-Gazette, or Philadelphia Inquirer confirming the winner may be used instead.

In the event of an exact tie in votes between Bartolotta and another candidate as reported by the official source, the question resolves NO (i.e., Bartolotta must have strictly more votes than all other candidates). If a recount is initiated and has not concluded by June 1, 2026 at 23:59 UTC, resolution is deferred until the recount is complete and official certified results are posted, but no later than July 1, 2026.

If Bartolotta withdraws before the election or the election is postponed beyond June 1, 2026, the question resolves NO.

**Pre-cutoff background**

Pennsylvania State Senator Camera Bartolotta (R) is the incumbent representing the 46th Senate District, which encompasses parts of Beaver, Greene, and Washington counties. She is facing a primary challenge from Albert Michael Buchtan, a masonry firm owner and former Carmichaels School Board member [https://www.spotlightpa.org/news/2026/03/key-2026-primary-elections-pennsylvana-state-house-senate-competitive/](https://www.spotlightpa.org/news/2026/03/key-2026-primary-elections-pennsylvana-state-house-senate-competitive/).

The race is considered competitive for several reasons. The Washington County GOP has issued a "vote of no confidence" against Bartolotta, signaling significant intra-party dissatisfaction. Additionally, the "skill games" lobby is expected to be heavily involved in this primary. Skill games are slot-like machines found in bars and convenience stores that operate in a legal gray area in Pennsylvania. Bartolotta has been a vocal critic of the industry. Capitol insiders expect the skill games industry—specifically entities like Pace-O-Matic and the conservative group Citizens Alliance of Pennsylvania—to be active in this primary, potentially supporting her challenger Buchtan [https://www.spotlightpa.org/news/2026/03/key-2026-primary-elections-pennsylvana-state-house-senate-competitive/](https://www.spotlightpa.org/news/2026/03/key-2026-primary-elections-pennsylvana-state-house-senate-competitive/). This outside spending and organized party opposition create genuine uncertainty about whether the incumbent can survive the primary.

The primary election is scheduled for May 19, 2026 (UTC-4). As of April 30, 2026, the Pennsylvania Department of State's election returns site is in testing mode ahead of the primary [https://www.spotlightpa.org/news/2026/03/key-2026-primary-elections-pennsylvana-state-house-senate-competitive/](https://www.spotlightpa.org/news/2026/03/key-2026-primary-elections-pennsylvana-state-house-senate-competitive/).

**Exact later resolution packet**

YES. I used the official Pennsylvania Department of State election returns site as required by the resolution criteria. Its 2026 General Primary office-results page for “Senator in the General Assembly” reports the Republican 46th Senatorial District results as Camera Bartolotta 11,445 votes (53.46%) and Al Buchtan 9,962 votes (46.54%) at https://www.electionreturns.pa.gov/Home/OfficeResults?officeId=12&ElectionID=117&ElectionType=P&IsActive=1 [Pennsylvania Elections - Office Results](https://www.electionreturns.pa.gov/Home/OfficeResults?officeId=12&ElectionID=117&ElectionType=P&IsActive=1). The official county-breakdown page gives the same total when summed across the district counties: Bartolotta 282 + 1,604 + 9,559 = 11,445 and Buchtan 256 + 2,049 + 7,657 = 9,962, at https://www.electionreturns.pa.gov/Home/CountyBreakDownResults?officeId=12&districtId=68&ElectionID=117&ElectionType=P&IsActive=1 [Pennsylvania Elections - County Breakdown Results](https://www.electionreturns.pa.gov/Home/CountyBreakDownResults?officeId=12&districtId=68&ElectionID=117&ElectionType=P&IsActive=1). Because Bartolotta’s 11,445 votes are strictly greater than Buchtan’s 9,962 votes, this is not a tie and satisfies the YES condition [Pennsylvania Elections - Office Results](https://www.electionreturns.pa.gov/Home/OfficeResults?officeId=12&ElectionID=117&ElectionType=P&IsActive=1) [Pennsylvania Elections - County Breakdown Results](https://www.electionreturns.pa.gov/Home/CountyBreakDownResults?officeId=12&districtId=68&ElectionID=117&ElectionType=P&IsActive=1).

The official returns were available by the June 1, 2026 resolution date, so the fallback to news reporting is unnecessary [Pennsylvania Elections - Office Results](https://www.electionreturns.pa.gov/Home/OfficeResults?officeId=12&ElectionID=117&ElectionType=P&IsActive=1) [Pennsylvania Elections - County Breakdown Results](https://www.electionreturns.pa.gov/Home/CountyBreakDownResults?officeId=12&districtId=68&ElectionID=117&ElectionType=P&IsActive=1). The official returns pages queried did not show or mention any recount being initiated or pending; therefore there is no unresolved recount requiring deferral [Pennsylvania Elections - Office Results](https://www.electionreturns.pa.gov/Home/OfficeResults?officeId=12&ElectionID=117&ElectionType=P&IsActive=1) [Pennsylvania Elections - County Breakdown Results](https://www.electionreturns.pa.gov/Home/CountyBreakDownResults?officeId=12&districtId=68&ElectionID=117&ElectionType=P&IsActive=1). The election was not postponed beyond June 1 because the Pennsylvania Department of State returns are for the May 19, 2026 General Primary, and Bartolotta is listed in those official returns as a Republican candidate receiving votes, so the “withdraws before the election” automatic-NO condition is not triggered on the official evidence used for resolution [Pennsylvania Elections - Office Results](https://www.electionreturns.pa.gov/Home/OfficeResults?officeId=12&ElectionID=117&ElectionType=P&IsActive=1) [Pennsylvania Elections - County Breakdown Results](https://www.electionreturns.pa.gov/Home/CountyBreakDownResults?officeId=12&districtId=68&ElectionID=117&ElectionType=P&IsActive=1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-4. `ce975c54-f33a-55c6-a098-cc572538baf7`

- Present date: `2026-05-12 21:12:43.872694`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Council of the European Union formally adopt the EU-US trade deal implementing legislation by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the Council of the European Union formally adopts the legislation implementing the EU-US trade deal (the "Turnberry" agreement concluded in July 2025) on or after May 10, 2026, and on or before July 1, 2026, 23:59 UTC.

"Formal adoption" means the Council's official decision to adopt the implementing legislation, as evidenced by either:
1. Publication of the adopted act in the [Official Journal of the European Union](https://eur-lex.europa.eu/oj/direct-access.html), OR
2. An official press release from the [Council of the European Union](https://www.consilium.europa.eu/en/press/press-releases/) confirming final adoption of the implementing legislation.

If the Council has not formally adopted the implementing legislation by 23:59 UTC on July 1, 2026, this question resolves **No**.

Note: Approval by the European Parliament alone (which occurred in March 2026) does not satisfy this criterion. The Council's adoption is the final legislative step required.

**Pre-cutoff background**

In July 2025, the United States and the European Union reached a trade agreement at Turnberry, Scotland, which set a 15% tariff on most EU goods exported to the US, while requiring the EU to eliminate tariffs on most US industrial goods and provide duty-free quotas on certain American agricultural and seafood products [Trump sets July 4 deadline for EU to comply with trade deal or face ...](https://www.reuters.com/world/trump-says-giving-eu-until-july-4-fulfill-trade-deal-or-will-raise-tariffs-2026-05-07/).

The European Parliament approved a conditional version of the implementing legislation in March 2026, adding safeguards such as making tariff cuts conditional on US compliance [Trump tariff tweaks smooth the way for EU-US trade deal approval](https://www.politico.eu/article/donald-trump-tariffs-ease-tensions-eu-us-trade-talks/). The deal then entered "trilogue" negotiations between the European Parliament, the European Commission, and the Council of the EU [Trump tariff tweaks smooth the way for EU-US trade deal approval](https://www.politico.eu/article/donald-trump-tariffs-ease-tensions-eu-us-trade-talks/).

On May 7, 2026, President Trump set a July 4, 2026 deadline for the EU to fully implement the deal, threatening that tariffs would "immediately jump to much higher levels" if the bloc fails to comply [Tariffs: Trump threatens EU if no trade deal is signed by new deadline](https://www.cnbc.com/2026/05/08/trump-tariffs-trade-eu-europe-deal.html). Trump had already raised tariffs on EU vehicles to 25% from the previously agreed 15% [Trump sets July 4 deadline for EU to comply with trade deal or face ...](https://www.reuters.com/world/trump-says-giving-eu-until-july-4-fulfill-trade-deal-or-will-raise-tariffs-2026-05-07/). European Commission President Ursula von der Leyen stated that "good progress" was being made, while the European Parliament's chief trade negotiator Bernd Lange indicated "there is still some way to go" [Tariffs: Trump threatens EU if no trade deal is signed by new deadline](https://www.cnbc.com/2026/05/08/trump-tariffs-trade-eu-europe-deal.html). EU negotiators were scheduled to meet on May 10, 2026 to continue discussions [Tariffs: Trump threatens EU if no trade deal is signed by new deadline](https://www.cnbc.com/2026/05/08/trump-tariffs-trade-eu-europe-deal.html).

There is significant uncertainty about whether the deal will be completed in time. Trump himself has reportedly characterized the chances as "50-50." Key divisions within the EU include disagreements over safeguard provisions and conditions for tariff reductions [Tariffs: Trump threatens EU if no trade deal is signed by new deadline](https://www.cnbc.com/2026/05/08/trump-tariffs-trade-eu-europe-deal.html). The final step required for formal approval is adoption by the Council of the European Union, following completion of the trilogue process [Trump tariff tweaks smooth the way for EU-US trade deal approval](https://www.politico.eu/article/donald-trump-tariffs-ease-tensions-eu-us-trade-talks/).

**Exact later resolution packet**

The question resolves YES.

The resolution criteria require that the Council of the European Union formally adopt the legislation implementing the EU-US ("Turnberry") trade deal on or after May 10, 2026, and on or before July 1, 2026, 23:59 UTC, as evidenced by either publication in the Official Journal OR an official Council of the EU press release confirming final adoption.

This condition was satisfied. On June 25, 2026, the Council of the European Union published an official press release ("EU-US trade: Council gives final approval for the tariff commitments under joint statement", https://www.consilium.europa.eu/en/press/press-releases/2026/06/25/eu-us-trade-council-gives-final-approval-for-the-tariff-commitments-under-joint-statement/) stating that the Council "formally adopted two regulations implementing the tariff-related commitments set out in the EU-US Joint Statement of 21 August 2025," and that "The adoption completes the legislative process" [EU-US trade: Council gives final approval for the tariff commitments ...](https://www.consilium.europa.eu/en/press/press-releases/2026/06/25/eu-us-trade-council-gives-final-approval-for-the-tariff-commitments-under-joint-statement/). June 25, 2026 falls squarely within the required window (May 10 – July 1, 2026).

This is corroborated by Reuters ("EU governments adopt legislation to fulfil EU side of US trade deal", https://www.reuters.com/business/eu-governments-adopt-legislation-fulfil-eu-side-us-trade-deal-2026-06-25/), which reported that "European Union governments adopted on Thursday [June 25, 2026] legislation to remove import duties on many U.S. goods, fulfilling the EU's side of a trade deal struck with U.S. President Donald Trump last year," specifically attributing the action to "the Council, the grouping of EU governments" [EU governments adopt legislation to fulfil EU side of US trade deal](https://www.reuters.com/business/eu-governments-adopt-legislation-fulfil-eu-side-us-trade-deal-2026-06-25/).

The action was taken by the Council of the European Union specifically — the final legislative step — and NOT merely the European Parliament (whose approval in March/June 2026 is explicitly excluded as a trigger). The two regulations implement the tariff commitments of the EU-US Joint Statement, which is the formal instrument stemming from the July 2025 Turnberry framework agreement between Trump and von der Leyen (the deal is widely referred to as the "Turnberry Deal"; the July 2025 Turnberry meeting produced the framework subsequently formalized in the 21 August 2025 Joint Statement).

Therefore, the Council formally adopted the Turnberry-implementing legislation on June 25, 2026, within the resolution window, and the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-5. `1a212384-33d7-5ab4-abf4-559c00ef7562`

- Present date: `2026-05-14 00:27:30.129476`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-16T00:00:00`

**Question**

Will the Bank of Japan raise its policy rate at the June 15-16, 2026 Monetary Policy Meeting?

**Resolution criteria**

This question resolves YES if the official "Statement on Monetary Policy" released by the Bank of Japan at the conclusion of the June 15-16, 2026 Monetary Policy Meeting (JST) announces a target for the uncollateralized overnight call rate that is numerically higher than the 0.75% target set at the April 26-27, 2026 meeting. It resolves NO if the announced target rate is equal to or lower than 0.75%.

The uncollateralized overnight call rate is the BOJ's primary policy rate tool, as described at: https://www.boj.or.jp/en/mopo/outline/index.htm

Resolution is based solely on the official policy statement published on the BOJ's Monetary Policy Decisions page: https://www.boj.or.jp/en/mopo/mpmdeci/index.htm

The question resolves based on the statement released at the conclusion of the June 15-16, 2026 meeting (expected June 16, 2026 JST), regardless of any subsequent market movements, press conference commentary, or later revisions. If the June 15-16, 2026 meeting is postponed or cancelled, this question resolves NO.

**Pre-cutoff background**

The Bank of Japan (BOJ) held its short-term policy rate — the uncollateralized overnight call rate — at 0.75% at its April 26-27, 2026 meeting. The decision was made by a 6-3 vote, the widest split under Governor Kazuo Ueda's tenure, with three dissenting board members (Nakagawa, Takata, and Tamura) voting to raise the rate to 1.0%. This hawkish division signals mounting internal pressure to continue policy normalization.

As of May 12, 2026, the BOJ's policy rate target stands at approximately 0.75% (the uncollateralized overnight call rate). Reuters has reported that the BOJ has effectively "locked in" a June rate hike, and the Financial Times reported that BOJ minutes suggest the next move will come in June. Prediction markets (Polymarket) price a 25bps hike at roughly 63%, reflecting genuine uncertainty. Key factors that could affect the decision include Japanese inflation dynamics (the BOJ raised its inflation outlook to 2.8% at the April meeting), global risks including Middle East tensions, and the trajectory of the yen.

The next BOJ Monetary Policy Meeting is scheduled for June 15 (Mon.) - 16 (Tues.), 2026 (JST), with the policy statement expected to be released on June 16, 2026 around midday JST.

**Exact later resolution packet**

The question resolves YES.

Resolution source: The official Bank of Japan "Statement on Monetary Policy" for the June 15–16, 2026 Monetary Policy Meeting — titled "Change in the Guideline for Money Market Operations," dated June 16, 2026 — published on the BOJ's Monetary Policy Decisions page. The specific statement URL is: https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/k260616a.pdf . It is listed under the BOJ's 2026 "Statements on Monetary Policy" index at https://www.boj.or.jp/en/mopo/mpmdeci/state_2026/index.htm [b5f614].

Key finding: The statement explicitly says, "The Bank will encourage the uncollateralized overnight call rate to remain at around 1.0 percent." This decision was made by a 7-1 majority vote of the Policy Board [8b1a00].

Comparison to April baseline: The April 26–27, 2026 meeting set the target for the uncollateralized overnight call rate at 0.75% (as stated in the question description and confirmed as the prior target). The new June 16, 2026 target of "around 1.0 percent" is numerically higher than 0.75% [8b1a00, b5f614].

Per the resolution criteria, the question resolves YES because the announced target (1.0%) is numerically higher than the 0.75% target set at the April meeting. This is based solely on the written statement released at the conclusion of the meeting, ignoring any press conference commentary or later market revisions.

The June 15–16, 2026 meeting was neither postponed nor cancelled (it concluded on June 16, 2026 with the rate-change statement released), so the NO-on-cancellation clause does not apply [8b1a00, b5f614].

Therefore: resolution = 1 (YES).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-6. `30c33338-f7cd-56af-a904-85fa7b9d4ec3`

- Present date: `2026-05-07 22:15:46.004962`
- Source cutoff boundary: `2026-05-08` (encodes end of UTC day `2026-05-07`)
- Expected resolution: `2026-05-26 00:00:00`

**Question**

Will Donald Trump formally endorse a candidate in the Texas Republican Senate runoff before May 27, 2026?

**Resolution criteria**

This question resolves **Yes** if Donald Trump issues a formal endorsement of either John Cornyn or Ken Paxton for the Texas Republican Senate runoff on or after May 7, 2026, and before 11:59 PM Central Time on May 26, 2026.

A "formal endorsement" is defined as an explicit public statement of support for one candidate over the other, made through any of the following channels:
- A post on Trump's official Truth Social account (https://truthsocial.com/@realDonaldTrump)
- A post on Trump's official X/Twitter account (@realDonaldTrump)
- An official statement or press release issued by the White House, the Trump campaign, or Trump's official spokesperson
- A direct, on-the-record quote attributed to Trump in reporting by major credible news organizations (e.g., Associated Press, Reuters, CNN, The New York Times, The Washington Post, Fox News)

Casual praise or positive comments about a candidate do **not** count unless they include explicit language of endorsement (e.g., "I endorse," "vote for," "he/she has my complete and total endorsement," or equivalent unambiguous language).

This question resolves **No** if no such formal endorsement is made by the deadline.

**Verification sources:** Trump's official Truth Social and X accounts, White House press releases (https://www.whitehouse.gov/), and reporting from the news organizations listed above.

**Pre-cutoff background**

The 2026 Texas Republican Senate primary runoff is scheduled for May 26, 2026, between incumbent U.S. Senator John Cornyn and Texas Attorney General Ken Paxton [2026 United States Senate election in Texas - Wikipedia](https://en.wikipedia.org/wiki/2026_United_States_Senate_election_in_Texas). The runoff was triggered after neither candidate secured a majority in the March 3, 2026, primary. As of May 7, 2026, Donald Trump has not endorsed either candidate, despite having described both as "good friends" and facing pressure from both campaigns to weigh in [2026 United States Senate election in Texas - Wikipedia](https://en.wikipedia.org/wiki/2026_United_States_Senate_election_in_Texas). CNN reporting from May 1, 2026, suggested Trump may not get involved at all. The race is widely viewed as a contest between establishment Republicans (Cornyn) and hardline conservative forces (Paxton) within the Texas GOP.

**Exact later resolution packet**

YES. Donald Trump formally endorsed Ken Paxton, not John Cornyn, during the allowed window.

Key evidence:
- Reuters, at https://www.reuters.com/world/us/trump-make-endorsement-texas-us-senate-republican-primary-2026-05-19/, reported that “President Donald Trump endorsed Texas conservative hardliner Ken Paxton on Tuesday in his primary challenge of veteran Republican U.S. Senator John Cornyn,” and identified the endorsement date as Tuesday, May 19, 2026, with the endorsement made online/through Truth Social [Trump backs hardliner Ken Paxton in critical Texas US Senate race ...](https://www.reuters.com/world/us/trump-make-endorsement-texas-us-senate-republican-primary-2026-05-19/). May 19, 2026 is on or after May 7, 2026 and before 11:59 PM Central Time on May 26, 2026.
- CNN, at https://us.cnn.com/2026/05/19/politics/cornyn-paxton-trump-texas-endorse, likewise reported on May 19, 2026 that “President Donald Trump on Tuesday endorsed Texas Attorney General Ken Paxton in his primary challenge to Sen. John Cornyn,” and said this came in a “lengthy Truth Social post” [Trump endorses Paxton, upending Senate GOP plans in Texas race](https://us.cnn.com/2026/05/19/politics/cornyn-paxton-trump-texas-endorse). CNN is one of the news organizations explicitly allowed by the resolution criteria.
- AP, at https://apnews.com/live/election-primary-texas-runoff-05-26-2026, later described Paxton as having been “endorsed by President Donald Trump last week” and reported the Truth Social-related endorsement context, including Paxton’s statement that Trump gave him his “complete and total endorsement” [Paxton wins Senate primary runoff, defeats Cornyn - AP News](https://apnews.com/live/election-primary-texas-runoff-05-26-2026). AP is also an explicitly allowed verification source.
- Houston Public Media’s May 19 article, at https://www.houstonpublicmedia.org/articles/news/politics/2026/05/19/552323/ken-paxton-trump-endorsement-texas-senate-republican-primary-runoff-cornyn/, identified the official Truth Social post URL as https://truthsocial.com/@realDonaldTrump/posts/116602192066577324 and reported that Trump backed Paxton on Tuesday, May 19, 2026 [Trump picks Paxton over Cornyn in Texas' GOP Senate primary ...](https://www.houstonpublicmedia.org/articles/news/politics/2026/05/19/552323/ken-paxton-trump-endorsement-texas-senate-republican-primary-runoff-cornyn/). A direct query of that Truth Social URL could not retrieve the post text because the page required JavaScript, but the URL itself is the official-channel post identified by reporting [https://truthsocial.com/@realDonaldTrump/posts/116602192066577324](https://truthsocial.com/@realDonaldTrump/posts/116602192066577324) [Trump picks Paxton over Cornyn in Texas' GOP Senate primary ...](https://www.houstonpublicmedia.org/articles/news/politics/2026/05/19/552323/ken-paxton-trump-endorsement-texas-senate-republican-primary-runoff-cornyn/).

Therefore, the resolution criteria are satisfied: the endorsement was for Ken Paxton over John Cornyn, was made on May 19, 2026 within the specified window, was reported by authorized major news organizations and tied to Trump’s official Truth Social channel, and was characterized as an endorsement rather than mere praise. The question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-7. `ee51ff77-017d-5b54-8523-09a424b7bee0`

- Present date: `2026-05-03 04:38:07.553426`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Governor Polis sign a bill by June 1, 2026, that removes the algorithmic discrimination and bias audit requirements from Colorado's AI regulatory framework (SB 24-205)?

**Resolution criteria**

This question resolves **Yes** if, on or after May 1, 2026, and before June 1, 2026 (23:59 UTC), Governor Jared Polis signs into law a bill that removes the algorithmic discrimination and bias audit requirements from Colorado's AI regulatory framework as established by Senate Bill 24-205.

Specifically, "removes the algorithmic discrimination and bias audit requirements" means the signed bill does at least ONE of the following:

1. **Strikes or repeals the definition of "algorithmic discrimination"** as set forth in Section 6-1-1701(1)(a) of the Colorado Revised Statutes (originally enacted via SB 24-205); OR
2. **Eliminates the requirement for deployers to conduct impact assessments** as set forth in Section 6-1-1703(3), including by replacing the impact assessment obligation with transparency-only or disclosure-only requirements; OR
3. **Eliminates the affirmative duty to avoid algorithmic discrimination** imposed on deployers under Section 6-1-1703, including by replacing it with a general requirement not to violate existing anti-discrimination laws (without the standalone AI-specific duty).

A "removal" includes: (a) total striking/repeal of the relevant statutory text; (b) replacing the substantive obligations (impact assessments, affirmative duty to avoid algorithmic discrimination) with transparency-only or notice-only requirements that do not require bias audits, impact assessments, or affirmative avoidance of algorithmic discrimination. A bill that merely delays the effective date of these provisions without removing them does NOT qualify.

**Resolution source:** The official Colorado General Assembly bill tracking website at https://leg.colorado.gov and/or the Governor's official signed legislation page at https://www.colorado.gov/governor. The signed bill text must be reviewed to confirm the relevant provisions are removed or replaced as described above.

If no such bill is signed by the Governor before 23:59 UTC on June 1, 2026, this question resolves **No**.

**Pre-cutoff background**

In May 2024, Colorado enacted Senate Bill 24-205 (the "Colorado AI Act"), the first comprehensive state AI law in the United States. The Act requires developers and deployers of "high-risk artificial intelligence systems" to use reasonable care to protect consumers from "algorithmic discrimination," defined in Section 6-1-1701(1)(a) as "any condition in which the use of an artificial intelligence system results in an unlawful differential treatment or unlawful disparate impact" on the basis of protected characteristics. Key obligations include: conducting impact assessments (Section 6-1-1702(2)(b) for developers; Section 6-1-1703(3) for deployers), implementing risk management policies, reporting instances of algorithmic discrimination to the Attorney General within 90 days (Section 6-1-1703(7)), and affirmatively avoiding algorithmic discrimination.

Following industry criticism, a special legislative session in August 2025 delayed the Act's effective date from February 1, 2026 to June 30, 2026 [State AI Laws – Where Are They Now? - Cooley](https://www.cooley.com/news/insight/2026/2026-04-24-state-ai-laws-where-are-they-now). Governor Polis convened an AI Policy Work Group, which on March 17, 2026, delivered unanimous support for a revised policy framework (the "Proposed ADMT Framework") to replace the Colorado AI Act [The Colorado AI Policy Work Group Proposes an Updated ...](https://www.mayerbrown.com/en/insights/publications/2026/03/the-colorado-ai-policy-work-group-proposes-an-updated-framework-to-replace-the-colorado-ai-act). The proposal explicitly removes requirements to report algorithmic discrimination, implement risk management policies, and conduct AI impact assessments, replacing them with transparency, recordkeeping, and consumer rights obligations [The Colorado AI Policy Work Group Proposes an Updated ...](https://www.mayerbrown.com/en/insights/publications/2026/03/the-colorado-ai-policy-work-group-proposes-an-updated-framework-to-replace-the-colorado-ai-act) [Colorado's Artificial Intelligence Law Could Be on the Chopping Block](https://www.littler.com/news-analysis/asap/colorados-artificial-intelligence-law-could-be-chopping-block).

As of late April 2026, the working group's proposal had not yet been formally introduced as a bill in the Colorado General Assembly [Colorado's Artificial Intelligence Law Could Be on the Chopping Block](https://www.littler.com/news-analysis/asap/colorados-artificial-intelligence-law-could-be-chopping-block). On April 28, 2026, a federal judge also issued an order delaying enforcement of the existing law. The Colorado legislature's regular session typically runs through early May, creating a narrow window for passage. Governor Polis has signaled support for lighter-touch regulation, but consumer advocacy groups and the AG's office may push back on fully removing anti-discrimination provisions.

**Exact later resolution packet**

RESOLUTION: YES (1).

ANTECEDENT/TIMING: Governor Jared Polis signed Senate Bill 26-189 into law on May 14, 2026, which falls within the question's resolution window of May 1, 2026 through June 1, 2026 (23:59 UTC). The official Colorado General Assembly bill page (https://leg.colorado.gov/bills/sb26-189) confirms the bill was signed by the Governor on May 14, 2026, and that it "repeals and reenacts" the provisions originally enacted via SB 24-205 [https://leg.colorado.gov/bills/sb26-189](https://leg.colorado.gov/bills/sb26-189). Multiple independent law-firm analyses corroborate the May 14, 2026 signing date [Colorado AI Act Repealed and Replaced by Narrower Statute ...](https://www.dwt.com/blogs/privacy--security-law-blog/2026/05/colorado-ai-act-repeal-new-transparency-law) [Colorado enacts revised AI law | United States - Norton Rose Fulbright](https://www.nortonrosefulbright.com/en-us/knowledge/publications/18733d31/colorado-enacts-revised-ai-law).

SUBSTANTIVE CRITERIA MET: The question requires the signed bill to do at least ONE of three things (strike the definition of "algorithmic discrimination" in 6-1-1701(1)(a); eliminate deployer impact assessments in 6-1-1703(3); or eliminate the affirmative duty to avoid algorithmic discrimination), and explicitly states that replacing substantive obligations with transparency-only/notice-only requirements qualifies as a "removal." SB 26-189 satisfies multiple of these criteria:
- It removes "the duty of care to mitigate algorithmic discrimination risks, requirements regarding algorithmic discrimination, and requirements to perform annual impact assessments and maintain a risk management program," replacing the high-risk AI framework with an "automated decision-making technology" (ADMT) framework centered on notice, documentation, and consumer rights [Colorado enacts revised AI law | United States - Norton Rose Fulbright](https://www.nortonrosefulbright.com/en-us/knowledge/publications/18733d31/colorado-enacts-revised-ai-law).
- DWT confirms the new law "abandons the CAIA's extensive risk-management and impact-assessment requirements" and shifts away from the CAIA's "duties of care" and "affirmative avoidance" requirements, replacing them with transparency/notice, documentation, and consumer-rights obligations [Colorado AI Act Repealed and Replaced by Narrower Statute ...](https://www.dwt.com/blogs/privacy--security-law-blog/2026/05/colorado-ai-act-repeal-new-transparency-law).
- Troutman confirms SB 189 "removes many of the hallmarks of the Colorado AI Act — such as a duty of care, risk management programs, and impact assessments — in favor of a disclosure-based framework" and "does not contain any reference to algorithmic discrimination, duties of care, risk management programs, impact assessments" [Colorado Legislature Passes Bill to Repeal and Replace Colorado ...](https://www.troutmanprivacy.com/2026/05/colorado-legislature-passes-bill-to-repeal-and-replace-colorado-ai-act/).

DELAY-VS-REMOVAL DISTINCTION: This is not merely a delay of the effective date (an earlier SB 25B-004 in August 2025 did that). SB 26-189 substantively repeals/replaces the impact assessment requirement and the affirmative duty to avoid algorithmic discrimination with a disclosure/transparency-based framework, which the resolution criteria explicitly count as qualifying "removal."

NOTE ON CONFLICTING TOOL OUTPUT: One automated read of the leg.colorado.gov page [https://leg.colorado.gov/bills/sb26-189](https://leg.colorado.gov/bills/sb26-189) suggested NO on the theory that "repeals and reenacts" maintains regulatory oversight. That reasoning is incorrect under the question's own resolution criteria, which expressly state that replacing the impact assessment/affirmative duty obligations with transparency-only or disclosure-only requirements DOES qualify as a removal. The substantive content (removal of impact assessments and the algorithmic-discrimination duty of care, replaced by a disclosure-based ADMT framework) is confirmed by three independent legal sources [Colorado AI Act Repealed and Replaced by Narrower Statute ...](https://www.dwt.com/blogs/privacy--security-law-blog/2026/05/colorado-ai-act-repeal-new-transparency-law) [Colorado enacts revised AI law | United States - Norton Rose Fulbright](https://www.nortonrosefulbright.com/en-us/knowledge/publications/18733d31/colorado-enacts-revised-ai-law) [Colorado Legislature Passes Bill to Repeal and Replace Colorado ...](https://www.troutmanprivacy.com/2026/05/colorado-legislature-passes-bill-to-repeal-and-replace-colorado-ai-act/).

PRIMARY SOURCE URL: https://leg.colorado.gov/bills/sb26-189

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-8. `769d43d1-f7c7-5f51-bb05-562a4222c358`

- Present date: `2026-05-02 21:37:29.499567`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Moody's, S&P, or Fitch upgrade the long-term sovereign credit rating of any G20 member country between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if at least one of the three major credit rating agencies—S&P Global Ratings, Moody's Investors Service, or Fitch Ratings—publicly announces an upgrade to the long-term foreign-currency sovereign credit rating of any G20 member country between 00:00 UTC on May 1, 2026, and 23:59 UTC on June 1, 2026. Otherwise, it resolves **No**.

**Definitions:**

- **Upgrade:** An increase of at least one notch on the agency's sovereign credit rating scale (e.g., BBB to BBB+, or Baa2 to Baa1). Changes in outlook only (e.g., Stable to Positive) or affirmations of existing ratings do **not** count as upgrades.

- **Rating type:** Only the long-term foreign-currency sovereign credit rating (or equivalent: S&P's "Long-Term Foreign Currency Issuer Credit Rating," Moody's "Long-Term Issuer Rating (Foreign Currency)," Fitch's "Long-Term Foreign-Currency Issuer Default Rating") is tracked.

- **G20 members:** The 19 sovereign nations that are members of the G20 as of May 1, 2026: Argentina, Australia, Brazil, Canada, China, France, Germany, India, Indonesia, Italy, Japan, Mexico, Russia, Saudi Arabia, South Africa, South Korea, Turkey, the United Kingdom, and the United States. The European Union and the African Union, while G20 participants, are excluded as they are not sovereign states with standard sovereign credit ratings. Membership is defined per https://en.wikipedia.org/wiki/G20. If G20 membership changes between question creation and resolution, the membership list as of May 1, 2026, applies.

- **Resolution source:** Official rating action press releases published by the agencies on their websites:
  - S&P Global Ratings: https://www.spglobal.com/ratings/en/
  - Moody's Investors Service: https://www.moodys.com/
  - Fitch Ratings: https://www.fitchratings.com/
  
  The date of the official press release determines whether the action falls within the resolution window.

**Pre-cutoff background**

Sovereign credit ratings assess a country's creditworthiness and are issued by three major agencies: S&P Global Ratings, Moody's Investors Service, and Fitch Ratings. Rating upgrades—where a country's rating moves up by at least one notch—are discrete events driven by assessments of fiscal policy, macroeconomic conditions, and reform progress.

As of early 2026, the G20 comprises 19 countries plus the European Union and the African Union: Argentina, Australia, Brazil, Canada, China, France, Germany, India, Indonesia, Italy, Japan, Mexico, Russia, Saudi Arabia, South Africa, South Korea, Turkey, the United Kingdom, the United States, the EU, and the African Union (https://en.wikipedia.org/wiki/G20).

Current ratings for key G20 members (S&P / Moody's) include [Credit Rating - Countries - List | G20 - Trading Economics](https://tradingeconomics.com/country-list/rating?continent=g20): Australia (AAA/Aaa), Canada (AAA/Aaa), Germany (AAA/Aaa), United States (AA+/Aa1), United Kingdom (AA/Aa3), France (A+/Aa3), Saudi Arabia (A+/Aa3), China (A+/A1), Japan (A+/A1), Italy (BBB+/Baa2), Indonesia (BBB/Baa2), Mexico (BBB/Baa2), India (BBB/Baa3), Brazil (BB/Ba1), Turkey (BB-/Ba3), Argentina (CCC+/Caa1), Russia (NR/NR).

Moody's global sovereign outlook for 2026 is negative. Fitch's global sovereign outlook is neutral, with 10 sovereigns globally on Positive Outlook entering 2026. S&P reports no sovereigns in the Americas currently carry a positive outlook. However, several G20 members have scheduled rating reviews in May 2026 [[PDF] Sovereign Rating Review Calendar – 2026 - MNI](https://media.marketnews.com/MNI_Sovereign_Rating_Review_Calendar_2026_29077cbd54.pdf): Germany (S&P May 8, Fitch May 15), Italy (S&P May 15), United Kingdom (S&P May 15 and May 22), South Africa (S&P May 22), France (Fitch May 29). S&P has noted room for a sovereign rating upgrade for Malaysia (not G20), and Turkey and Argentina have been discussed as potential upgrade candidates given reform progress. South Africa has expressed hope for an upgrade within 18 months. Rating actions can also occur on an ad-hoc basis outside scheduled reviews.

With approximately 20 G20 members and three agencies, there are many possible upgrade opportunities in a single month, but most reviews result in affirmations rather than upgrades, making the probability non-trivial but uncertain.

**Exact later resolution packet**

The question resolves YES because Fitch Ratings upgraded the long-term foreign-currency sovereign credit rating of Argentina—a G20 member—within the resolution window (00:00 UTC May 1, 2026 to 23:59 UTC June 1, 2026).

Evidence: The official Fitch Ratings press release "Fitch Upgrades Argentina to 'B-'; Outlook Stable," dated New York, 05 May 2026, states that Fitch upgraded Argentina's Long-Term Foreign Currency (and Local Currency) Issuer Default Rating to 'B-' from 'CCC+' [Fitch Upgrades Argentina to 'B-'; Outlook Stable](https://www.fitchratings.com/research/sovereigns/fitch-upgrades-argentina-to-b-outlook-stable-05-05-2026). This is a notch upgrade (not merely an outlook change) of the precise rating type tracked by the question (Fitch's "Long-Term Foreign-Currency Issuer Default Rating"). URL: https://www.fitchratings.com/research/sovereigns/fitch-upgrades-argentina-to-b-outlook-stable-05-05-2026

Argentina is explicitly listed as one of the 19 sovereign G20 members in the question's criteria. The press release date (May 5, 2026) falls squarely within the May 1–June 1, 2026 window. This single qualifying event is sufficient for a YES resolution. (Other G20 reviews in the window—e.g., S&P affirming Italy at BBB+, Moody's changing South Africa's outlook to positive without a notch upgrade, S&P affirming Mexico, Fitch affirming France—did not produce upgrades, but they are immaterial given the Argentina upgrade already satisfies the criteria.)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-9. `188b4bac-c174-5f53-ac02-2f431f9c72d4`

- Present date: `2026-05-16 08:53:06.420994`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-05-25 00:00:00`

**Question**

Will the Bank of Israel cut the interest rate at its May 25, 2026 monetary policy meeting?

**Resolution criteria**

This question resolves **Yes** if the Bank of Israel announces a decrease in its benchmark short-term interest rate from the current 4.00% (the rate in effect as of May 12, 2026) at the Monetary Committee meeting scheduled for May 25, 2026.

This question resolves **No** if the Bank of Israel announces that the interest rate will remain unchanged at 4.00% or be increased.

Resolution will be based on the official press release published by the Bank of Israel following the May 25, 2026 Monetary Committee meeting. The primary resolution source is the Bank of Israel's press releases page: [https://www.boi.org.il/en/communication-and-publications/press-releases/](https://www.boi.org.il/en/communication-and-publications/press-releases/)

If the meeting is rescheduled or postponed, resolution follows the rescheduled date. If no decision is announced by July 1, 2026, 23:59 UTC, the question resolves **No**.

**Pre-cutoff background**

As of May 12, 2026, the Bank of Israel's benchmark interest rate stands at 4.00%, following a surprise cut from 4.25% in January 2026 and subsequent holds in February and March 2026 [The Monetary Committee decides on March 30, 2026 to leave the ...](https://www.boi.org.il/en/communication-and-publications/press-releases/the-monetary-committee-decides-on-march-30-2026-to-leave-the-interest-rate-unchanged-at-400-percent/). Israel's inflation rate is approximately 1.9%, within the Bank's 1–3% target range, which would normally support further easing.

However, the Monetary Committee has cited significant geopolitical uncertainty as a key reason for caution. Operation Roaring Lion—Israel's military campaign in Lebanon—has created broad economic implications, including a sharp decline in activity at the campaign's outset followed by partial recovery [The Monetary Committee decides on March 30, 2026 to leave the ...](https://www.boi.org.il/en/communication-and-publications/press-releases/the-monetary-committee-decides-on-march-30-2026-to-leave-the-interest-rate-unchanged-at-400-percent/). The Committee also noted rising global energy prices contributing to inflationary pressures, and a tight labor market with supply constraints [The Monetary Committee decides on March 30, 2026 to leave the ...](https://www.boi.org.il/en/communication-and-publications/press-releases/the-monetary-committee-decides-on-march-30-2026-to-leave-the-interest-rate-unchanged-at-400-percent/). At its March 30, 2026 meeting, the Bank trimmed its 2026 GDP growth forecast to 3.8% from 5.2%.

The next Monetary Committee decision is scheduled for May 25, 2026, with the announcement expected at 16:00 Israel time (13:00 UTC). April CPI data, due May 15, will be a key input. Prediction markets (Polymarket) currently price a cut at roughly 60–67% and a hold at ~35–39%, reflecting genuine uncertainty driven by the interplay between moderating inflation (favoring a cut) and escalating regional tensions including Iran-US frictions (favoring a hold).

**Exact later resolution packet**

The question resolves YES. The official Bank of Israel press release at https://www.boi.org.il/en/communication-and-publications/press-releases/25-05-2026/ is titled “The Monetary Committee decides on May 25, 2026 to lower the interest to 3.75 percent,” and the queried official page reports the publication/decision date as 25/05/2026 [The Monetary Committee decides on May 25, 2026 to lower the ...](https://www.boi.org.il/en/communication-and-publications/press-releases/25-05-2026/). The rate prior to this meeting was 4.00%: the earlier official Bank of Israel March 30, 2026 press release states that the rate was left unchanged at 4.00% and that the next interest-rate decision would be published on Monday, May 25, 2026 [The Monetary Committee decides on March 30, 2026 to leave the ...](https://www.boi.org.il/en/communication-and-publications/press-releases/the-monetary-committee-decides-on-march-30-2026-to-leave-the-interest-rate-unchanged-at-400-percent/). The May 25 official release then announced a lower rate of 3.75% [The Monetary Committee decides on May 25, 2026 to lower the ...](https://www.boi.org.il/en/communication-and-publications/press-releases/25-05-2026/). Because the decision occurred on May 25, 2026—the scheduled date stated in the prior official release—there is no evidence that the meeting was rescheduled, so the original May 25 outcome applies [The Monetary Committee decides on March 30, 2026 to leave the ...](https://www.boi.org.il/en/communication-and-publications/press-releases/the-monetary-committee-decides-on-march-30-2026-to-leave-the-interest-rate-unchanged-at-400-percent/) [The Monetary Committee decides on May 25, 2026 to lower the ...](https://www.boi.org.il/en/communication-and-publications/press-releases/25-05-2026/). Comparing the pre-meeting rate of 4.00% with the meeting decision of 3.75%, the Bank of Israel decreased its benchmark short-term interest rate, satisfying the YES criterion [The Monetary Committee decides on March 30, 2026 to leave the ...](https://www.boi.org.il/en/communication-and-publications/press-releases/the-monetary-committee-decides-on-march-30-2026-to-leave-the-interest-rate-unchanged-at-400-percent/) [The Monetary Committee decides on May 25, 2026 to lower the ...](https://www.boi.org.il/en/communication-and-publications/press-releases/25-05-2026/).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-10. `ee0672d3-0838-5516-9ace-cb54cf371c21`

- Present date: `2026-05-13 20:55:31.854444`
- Source cutoff boundary: `2026-05-14` (encodes end of UTC day `2026-05-13`)
- Expected resolution: `2026-05-19 00:00:00`

**Question**

Will the 2026 Georgia Republican U.S. Senate primary go to a runoff?

**Resolution criteria**

This question resolves based on the certified results of the May 19, 2026, Georgia Republican U.S. Senate [primary election](https://sos.ga.gov/elections-division-georgia-secretary-states-office).

- **Resolves YES** if no candidate receives more than 50% of the total votes cast in the Republican U.S. Senate primary, thereby triggering a [runoff election](https://sos.ga.gov/page/georgia-election-results) as required under Georgia law (O.C.G.A. § 21-2-501).
- **Resolves NO** if any candidate receives more than 50% of the total votes cast, winning the nomination outright without a runoff.

The primary resolution source is the official Georgia Secretary of State election results page: [https://results.sos.ga.gov/results/public/Georgia](https://results.sos.ga.gov/results/public/Georgia) [Georgia Election Results | Georgia Secretary of State](https://sos.ga.gov/page/georgia-election-results). If official certified results are delayed, credible reporting from major outlets (e.g., the Associated Press, Atlanta Journal-Constitution) showing a definitive result may be used for preliminary resolution, subject to later confirmation by the Secretary of State.

Key definitions:
- **Primary**: The partisan election held on May 19, 2026, to select each party's nominee, as administered by the [Georgia Secretary of State](https://sos.ga.gov/elections-division-georgia-secretary-states-office).
- **Runoff**: A second election between the top two candidates, triggered when no candidate receives more than 50% of total votes cast in the primary, per [O.C.G.A. § 21-2-501](https://law.justia.com/codes/georgia/title-21/chapter-2/article-11/part-1/section-21-2-501/).
- **Total votes cast**: All valid votes recorded in the Republican U.S. Senate primary on May 19, 2026.

Resolution is determined as of 23:59 UTC on May 19, 2026, based on results reported for that election.

**Pre-cutoff background**

Georgia's 2026 Republican U.S. Senate primary is scheduled for May 19, 2026, with five candidates competing to challenge incumbent Democratic Senator Jon Ossoff in the November general election. Under [Georgia Code § 21-2-501](https://law.justia.com/codes/georgia/title-21/chapter-2/article-11/part-1/section-21-2-501/), a candidate must receive more than 50% of the total votes cast to win a primary outright; otherwise, a runoff between the top two vote-getters is held.

U.S. Rep. Mike Collins leads the field but is far from the 50% threshold. An Atlanta Journal-Constitution poll (April 18–26, 2026) showed Collins at approximately 21.6%, followed by Buddy Carter at 12.5% and Derek Dooley at 11%, with more than half of likely Republican primary voters still undecided [AJC Poll: Collins leads in Senate GOP primary, but most voters ...](https://www.ajc.com/politics/2026/05/ajc-poll-collins-leads-in-senate-gop-primary-but-most-voters-undecided/). Other recent polls (InsiderAdvantage, April 22–23) have placed Collins in the 23–31% range with leads of 3 to 10 points over his nearest rival. The large undecided bloc and crowded field make it uncertain whether any candidate can consolidate enough support to clear 50%.

If a runoff is triggered, it is scheduled for June 16, 2026.

**Exact later resolution packet**

YES. The official Georgia Secretary of State election-results index links to the May 19, 2026 General Primary results at https://results.sos.ga.gov/results/public/Georgia/GeneralPrimary51926 [https://results.sos.ga.gov/results/public/Georgia](https://results.sos.ga.gov/results/public/Georgia). On that official Georgia Secretary of State results page for the Republican U.S. Senate primary, the listed candidate results are: Mike Collins 369,629 votes (40.50%), Derek Dooley 275,524 (30.19%), Earl L. “Buddy” Carter 229,216 (25.12%), Jonathan “Jon” McColumn 28,446 (3.12%), and John F. Coyne III 9,850 (1.08%), for 912,665 total votes; the page also exposes the contest-specific URL https://results.sos.ga.gov/results/public/Georgia/elections/GeneralPrimary51926/ballot-items/01000000-f33c-bc21-a444-08dead340297 [https://results.sos.ga.gov/results/public/Georgia/GeneralPrimary51926](https://results.sos.ga.gov/results/public/Georgia/GeneralPrimary51926). Because the top Republican primary candidate, Mike Collins, received only 40.50%—not more than 50%—no candidate won the Republican U.S. Senate primary outright, so under the question’s stated criteria a runoff was triggered [https://results.sos.ga.gov/results/public/Georgia/GeneralPrimary51926](https://results.sos.ga.gov/results/public/Georgia/GeneralPrimary51926). Therefore the Metaculus question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-11. `3627cdd9-2f72-5ae1-8e2f-7eff4bc14873`

- Present date: `2026-05-15 20:07:01.330449`
- Source cutoff boundary: `2026-05-16` (encodes end of UTC day `2026-05-15`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Niger junta (CNSP) formally accuse France, Benin, or Côte d'Ivoire of involvement in an armed attack or sabotage in Niger between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves YES if, between May 12, 2026 00:00 UTC and July 1, 2026 23:59 UTC, the Niger junta — specifically the CNSP (National Council for the Safeguard of the Homeland) — formally accuses at least one of the following states of involvement in a security incident in Niger: France, Benin, or Côte d'Ivoire.

Definitions:

1. **"Formally accuses"**: A public statement by General Abdourahamane Tiani (CNSP chairman), the Prime Minister, the Foreign Minister, or an official CNSP spokesperson, delivered via any of the following channels: (a) a televised or broadcast address, (b) an official government press release, (c) a statement on an official Niger government or CNSP social media account, or (d) a statement reported by at least two of the following news agencies: Reuters (https://www.reuters.com), AFP/France24/RFI, Al Jazeera (https://www.aljazeera.com), or the Associated Press (https://apnews.com).

2. **"Security incident"**: An armed attack, bombing, sabotage operation, assassination attempt, or coup attempt occurring within Niger's borders. The accusation must allege that the named foreign state sponsored, directed, facilitated, or otherwise participated in the incident. The security incident itself may have occurred before or after May 12, 2026 — what matters is that the formal accusation is made within the resolution window.

3. **"Involvement"**: The accusation must allege direct or indirect state-level involvement (e.g., sponsoring, directing, facilitating, or providing material support to armed groups), not merely general complaints about diplomatic tensions or media hostility.

The question resolves NO if no such formal accusation is reported by credible international news sources by July 1, 2026 23:59 UTC.

**Verification sources**: Resolution will be determined by checking reporting from Reuters, Al Jazeera, AFP/RFI, and AP. If at least two of these outlets report a qualifying accusation, the question resolves YES.

**Pre-cutoff background**

Niger's military government, the National Council for the Safeguard of the Homeland (CNSP, https://en.wikipedia.org/wiki/National_Council_for_the_Safeguard_of_the_Homeland), seized power in a coup on July 26, 2023, and is led by General Abdourahamane Tiani. Since then, the junta has repeatedly accused France (Niger's former colonial power), Benin, and Côte d'Ivoire of destabilizing the country.

Most recently, on January 29–30, 2026, following an armed assault on a military air base at Niamey's international airport, General Tiani publicly accused the presidents of France, Benin, and Côte d'Ivoire of sponsoring the attack. This was reported by Reuters, Al Jazeera, AFP, and other major outlets. The Islamic State subsequently claimed responsibility for the attack, but the junta maintained its accusations against the three states. This led to a diplomatic escalation, with Côte d'Ivoire summoning Niger's ambassador.

As of May 2026, relations between Niger and these three states remain deeply strained. Niger cancelled its May 1 parades for security reasons, the junta has called on citizens to "prepare for war with France," banned nine French media organizations, and accused France of violating its airspace. The CNSP regularly uses accusations against foreign states for domestic political purposes, particularly following security incidents attributed to jihadist groups operating in the Sahel.

The pattern of accusations is recurring but not guaranteed in any given seven-week window. Whether a new formal accusation occurs depends on both the occurrence of significant security incidents and the junta's political calculus at the time.

**Exact later resolution packet**

Adjudicated: On June 18, 2026 (inside the May 12 - July 1 window), militants attacked Diori Hamani International Airport in Niamey (JNIM claimed responsibility) - a qualifying security incident. That same Thursday evening, Niger's Ministry of National Defence read a communique on state television formally accusing France of being behind the attack, describing the assailants as 'armed mercenaries under the funding of French president Emmanuel Macron' - an allegation of direct state-level involvement, satisfying the 'formally accuses' / 'involvement' clauses via an official government televised statement. This is corroborated by France24 and Al Jazeera (AFP/France24/RFI + Al Jazeera buckets), plus RFI, BBC Afrique, Pan African Visions and Wikipedia. An earlier automated NO relied on NYT/BBC-syndicated pieces that only covered the JNIM claim and missed the government's evening accusatory communique.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-12. `a605b42c-6c3a-5d87-bae3-7b8b37a42bc8`

- Present date: `2026-04-29 23:25:40.530726`
- Source cutoff boundary: `2026-04-30` (encodes end of UTC day `2026-04-29`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will any U.S. congressional committee vote to report AI-specific legislation to the full House or Senate by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after the question's open date and on or before June 1, 2026 (23:59 UTC), any standing committee or subcommittee of the U.S. House of Representatives or U.S. Senate votes to order a bill "reported" (see [Senate glossary](https://www.senate.gov/reference/glossary_term/report.htm)) to the full chamber, where that bill is "AI-specific legislation" as defined below.

**AI-specific legislation** means a bill that has "artificial intelligence" or "AI" in its official title (short title or long title as shown on [Congress.gov](https://www.congress.gov/)), OR whose primary subject matter as categorized on Congress.gov falls under artificial intelligence policy.

A **vote to report** means the committee has completed a [markup](https://www.senate.gov/reference/glossary_term/markup.htm) and formally ordered the bill to be reported to the full House or Senate. This is tracked on each bill's "Actions" or "Committees" tab on Congress.gov (e.g., "Ordered to be reported" or "Reported by committee").

The resolution source is [Congress.gov](https://www.congress.gov/search?q=%7B%22source%22%3A%22legislation%22%2C%22congress%22%3A%22119%22%2C%22subject%22%3A%22Artificial+intelligence%22%7D), specifically the committee actions listed on individual bill pages. If Congress.gov shows that any AI-specific bill (as defined above) has been "ordered to be reported" by a committee on or after the question's open date and on or before June 1, 2026, the question resolves **Yes**. Otherwise, it resolves **No**.

**Pre-cutoff background**

On March 20, 2026, the White House released its National Policy Framework for Artificial Intelligence, urging Congress to enact comprehensive federal AI legislation that would preempt state AI laws while addressing child safety, copyright, free speech, and energy policy. Two days earlier, on March 18, 2026, Senator Marsha Blackburn (R-TN) released a 291-page discussion draft titled the "TRUMP AMERICA AI Act," which would codify many of the framework's recommendations into law.

As of early April 2026, these efforts have stalled on Capitol Hill. According to Politico, the framework received a "frosty reception" from Democrats, who dismissed it as a partisan initiative lacking adequate consumer protections [https://www.politico.com/news/2026/04/03/trumps-partisan-ai-pitch-stalls-on-the-hill-00858101](https://www.politico.com/news/2026/04/03/trumps-partisan-ai-pitch-stalls-on-the-hill-00858101). No committee markup or vote has been scheduled for the TRUMP AMERICA AI Act or any other comprehensive AI bill related to the framework. Key lawmakers have warned that the legislative window is narrowing and that bipartisan support—currently lacking—is essential for passage [https://www.politico.com/news/2026/04/03/trumps-partisan-ai-pitch-stalls-on-the-hill-00858101](https://www.politico.com/news/2026/04/03/trumps-partisan-ai-pitch-stalls-on-the-hill-00858101).

Several AI-related bills have been introduced in the 119th Congress (e.g., the Protect American AI Act [H.R. 8037], the Future of Artificial Intelligence Innovation Act [S. 3952], the AI Grand Challenges Act), but as of late April 2026, none has advanced past referral to committee.

The compressed legislative calendar, partisan divisions, and the complexity of comprehensive AI regulation make committee action plausible but far from certain within this timeframe.

**Exact later resolution packet**

The question resolves YES because the House Committee on Small Business voted to report favorably (i.e., ordered to be reported) an AI-specific bill within the resolution window of April 29, 2026 through June 1, 2026.

Specifically, on May 20, 2026, the full House Committee on Small Business, chaired by Rep. Roger Williams (TX-25), held a markup and reported favorably to the House nine bills, including H.R. 8881, the "SBA Artificial Intelligence Utilization Act of 2026," by a recorded vote of 23 Yea to 0 Nay [c1a7b7]. FedScoop independently confirms the committee unanimously approved the SBA Artificial Intelligence Utilization Act (H.R. 8881) in a Wednesday markup [f7e95e].

This satisfies all resolution criteria:
1. AI-specific legislation: H.R. 8881's official short title contains "Artificial Intelligence" ("SBA Artificial Intelligence Utilization Act of 2026") [c1a7b7].
2. Vote to report: The committee completed a markup and ordered the bill reported ("Reported Favorably to the House," 23-0) — not a mere referral [c1a7b7]. The Congress.gov committees tab also shows "House Small Business — 05/20/2026 — Markup By" following the 05/19/2026 referral.
3. Timing: The markup/order to report occurred May 20, 2026, which falls within the window (on/after April 29, 2026 and on/before June 1, 2026 23:59 UTC).

URL for the qualifying bill: https://www.congress.gov/bill/119th-congress/house-bill/8881
Committee press release: https://smallbusiness.house.gov/news/documentsingle.aspx?DocumentID=407452

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-13. `614badaa-58d1-51b1-a5a1-9faa933aa46d`

- Present date: `2026-05-12 17:59:49.260395`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the U.S. Court of Appeals for the Federal Circuit grant a stay of the Court of International Trade's May 7, 2026 ruling on 10% global tariffs before July 1, 2026?

**Resolution criteria**

This question resolves YES if the U.S. Court of Appeals for the Federal Circuit grants a stay—whether full or partial—of the Court of International Trade's May 7, 2026 injunction against the 10% global tariffs, with such stay order issued on or after May 10, 2026, and before July 1, 2026, 23:59 UTC.

This question resolves NO if no such stay is granted by the Federal Circuit by that deadline, including if:
- No stay motion is filed;
- A stay motion is filed but denied;
- A stay motion is filed but not yet decided.

A "stay" is defined as a court order temporarily suspending the effect of the lower court's ruling pending appeal (https://www.law.cornell.edu/wex/stay). An administrative stay (a brief, temporary hold while the court considers a stay motion) counts as YES only if it remains in effect as of the date the question resolves.

Resolution will be determined by the Federal Circuit's official docket, accessible via PACER (https://pacer.uscourts.gov/), or credible reporting from major news organizations such as Reuters (https://www.reuters.com/), the Associated Press (https://apnews.com/), or The New York Times (https://www.nytimes.com/).

**Pre-cutoff background**

On May 7, 2026, a divided 2-1 panel of the U.S. Court of International Trade (CIT) ruled that President Trump's 10% global tariffs, imposed under Section 122 of the Trade Act of 1974, were unlawful. The court found the administration misread the statute's definition of "balance-of-payments deficits" and granted injunctive relief to the plaintiffs—two small businesses and the state of Washington [Trade court says Trump's 10% global tariffs are unlawful - ABC News](https://abcnews.com/US/trade-court-trumps-10-global-tariffs-unlawful/story?id=132761523). The tariffs remain in effect for non-plaintiff importers and were originally slated to expire in July 2026.

On May 8, 2026, the Department of Justice filed a Notice of Appeal at the Court of International Trade, signaling plans to challenge the ruling at the U.S. Court of Appeals for the Federal Circuit [Trump administration appeals latest court loss on tariffs - Reuters](https://www.reuters.com/world/trump-administration-appeals-latest-court-loss-tariffs-2026-05-08/). The administration is also pursuing alternative tariff authorities, including three ongoing Section 301 investigations [Trump administration appeals latest court loss on tariffs - Reuters](https://www.reuters.com/world/trump-administration-appeals-latest-court-loss-tariffs-2026-05-08/).

As of May 11, 2026, it is not yet known whether the Federal Circuit will grant any motion to stay (i.e., temporarily suspend) the CIT's injunction pending the appeal. The 2-1 split on the panel suggests the legal question is genuinely contested. The administration may seek an emergency or expedited stay to preserve the tariffs' applicability to the plaintiffs during the appeal process. Whether the Federal Circuit grants such relief depends on factors including likelihood of success on the merits, irreparable harm, and public interest—standard criteria under the four-factor test for stays pending appeal (see https://www.law.cornell.edu/wex/stay).

Case: The ruling stems from litigation at the CIT in New York. Appeals from the CIT go exclusively to the U.S. Court of Appeals for the Federal Circuit (https://en.wikipedia.org/wiki/United_States_Court_of_Appeals_for_the_Federal_Circuit).

**Exact later resolution packet**

The question resolves YES.

Resolution criteria: YES if the U.S. Court of Appeals for the Federal Circuit grants a stay (full or partial) of the CIT's May 7, 2026 injunction against the 10% global (Section 122) tariffs, with the stay order issued on or after May 10, 2026 and before July 1, 2026, 23:59 UTC. An administrative stay counts only if it remained in effect as of the resolution date.

Key evidence (from mandated sources Reuters and AP):

1) On June 11, 2026, the U.S. Court of Appeals for the Federal Circuit granted the government's motion for a stay pending appeal, keeping the 10% global tariffs in place for the three importer-plaintiffs who had won relief at the CIT, while the appeal proceeds. Reuters ("US appeals court extends block on ruling against Trump's 10% global tariff," 2026-06-11) reports: "A U.S. appeals court on Thursday extended its block on a lower court ruling against the Trump administration's 10% global tariff... keeping the tariffs in place for three importers that had won a reprieve" [fd3239]. This June 11 stay pending appeal is squarely within the window (after May 10, before July 1) and remained in effect through the deadline, as the appeal was still ongoing.

2) The Associated Press ("Appeals court says U.S. government can keep collecting 10% tariffs for now") confirms the Federal Circuit allowed the government to keep collecting the tariffs while legal challenges continue, finding the administration "likely to succeed on the merits" — the standard stay-pending-appeal test [402d3c].

3) Additionally, the Federal Circuit had issued an administrative stay on May 12, 2026 to give it time to consider the government's motion to stay [0edb61]. This too was within the window, but the dispositive event is the June 11, 2026 stay pending appeal, which was a definitive (not merely administrative) stay still in force at resolution.

Antecedent check: This is not a conditional question. The court that issued the stay was the Federal Circuit (the appeals court), not the CIT itself — indeed the CIT had earlier denied the government's stay request on May 20, 2026, which is why the government sought and obtained the stay from the Federal Circuit. Both the administrative stay (May 12) and the stay pending appeal (June 11) were issued by the Federal Circuit.

Nature of stay (full vs. partial): The CIT's injunctive relief was limited to the named plaintiffs, so the Federal Circuit's stay of that injunction keeps the tariffs collectible as to those plaintiffs during the appeal. The resolution criteria count a stay "whether full or partial," so this qualifies regardless. The June 11, 2026 stay pending appeal is best characterized as a full stay of the CIT's (plaintiff-limited) injunction.

Conclusion: A qualifying stay was granted by the Federal Circuit within the window and remained in effect through July 1, 2026. The question resolves YES (1).

Sources: Reuters, https://www.reuters.com/world/us-appeals-court-extends-block-ruling-against-trumps-10-global-tariff-2026-06-11/ [fd3239]; Associated Press, https://apnews.com/article/trump-tariffs-court-lawsuit-a95ef7309d89018477a3265ebf93d620 [402d3c]; ST&R Trade Report (administrative stay date), https://www.strtrade.com/trade-news-resources/str-trade-report/trade-report/may/appeals-court-temporarily-stays-cit-ruling-against-section-122-tariffs [0edb61].

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-14. `8927330f-7ff8-5eb2-bf0d-1cfcb782f96a`

- Present date: `2026-05-03 11:33:57.719403`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will OpenAI publicly announce the launch of ChatGPT advertising in at least one European country by June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 2, 2026, and by June 1, 2026, at 11:59 PM UTC, OpenAI publicly announces that ChatGPT advertising has launched or is being tested in at least one country located in Europe, as defined by the United Nations geoscheme for Europe (https://unstats.un.org/unsd/methodology/m49/). This includes any country in Northern, Southern, Eastern, or Western Europe (e.g., UK, France, Germany, etc.).

**Definitions:**

- **"ChatGPT advertising"** means any form of paid promotional content displayed within the ChatGPT user interface, including but not limited to sponsored search results, display ads, or sponsored product recommendations, on any user tier (Free, Go, Plus, or otherwise).

- **"Publicly announce"** means an official communication by OpenAI, such as a blog post on the OpenAI Newsroom (https://openai.com/news/) or official OpenAI blog (https://openai.com/index/), an official press release, or an official OpenAI social media post (e.g., on X/Twitter @OpenAI). Alternatively, credible reporting by major news outlets (e.g., Reuters at https://www.reuters.com, The Wall Street Journal at https://www.wsj.com, The New York Times at https://www.nytimes.com, or Bloomberg at https://www.bloomberg.com) confirming the launch also suffices.

- **"Beyond the United States"** for this question specifically means at least one European country as defined above. Expansions to non-European countries (such as the already-announced Canada, Australia, and New Zealand) do not count.

If no such announcement or credible report exists by 11:59 PM UTC on June 1, 2026, the question resolves as **No**.

**Pre-cutoff background**

On January 16, 2026, OpenAI announced it would begin testing advertisements in ChatGPT for users on the Free and "Go" tiers in the United States [Our approach to advertising and expanding access to ChatGPT](https://openai.com/index/our-approach-to-advertising-and-expanding-access/). Ads appear at the bottom of answers when there is a relevant sponsored product or service, clearly labeled and separated from organic content. Pro, Business, and Enterprise subscriptions remain ad-free [Our approach to advertising and expanding access to ChatGPT](https://openai.com/index/our-approach-to-advertising-and-expanding-access/).

By late March 2026, OpenAI's U.S. ad pilot had exceeded $100 million in annualized revenue within its first six weeks [OpenAI Expands ChatGPT Advertising to More Markets After US Pilot](https://www.pymnts.com/artificial-intelligence-2/2026/openai-expands-chatgpt-advertising-to-more-markets-after-us-pilot/). On March 26–27, 2026, OpenAI announced it would extend its ad pilot beyond its initial end date and expand internationally to Canada, Australia, and New Zealand "in the coming weeks" [Advertisers Say OpenAI Is Extending Its Ad Pilot Beyond April](https://www.adweek.com/media/openai-ads-pilot-extension/) [OpenAI Expands ChatGPT Advertising to More Markets After US Pilot](https://www.pymnts.com/artificial-intelligence-2/2026/openai-expands-chatgpt-advertising-to-more-markets-after-us-pilot/). The international expansion went live around April 16–17, 2026, with ads appearing on Free and Go tiers in those markets.

In April 2026, reports indicated OpenAI projects $2.5 billion in advertising revenue for 2026 and $100 billion by 2030. Separately, the Wall Street Journal reported that OpenAI missed key internal revenue and user targets, potentially increasing pressure to accelerate ad monetization and geographic expansion. As of May 2, 2026, ChatGPT ads are live in the US, Canada, Australia, and New Zealand, but no European market has been announced. OpenAI has stated it plans to expand to "many more markets" later in 2026 [OpenAI Expands ChatGPT Advertising to More Markets After US Pilot](https://www.pymnts.com/artificial-intelligence-2/2026/openai-expands-chatgpt-advertising-to-more-markets-after-us-pilot/), but the timing for European rollout remains uncertain due to regulatory considerations (e.g., GDPR, the EU AI Act) and strategic prioritization.

**Exact later resolution packet**

The question resolves YES.

Resolution criterion: YES if, on or after May 2, 2026 and by June 1, 2026 (11:59 PM UTC), OpenAI publicly announces that ChatGPT advertising has launched or is being tested in at least one country located in Europe per the UN geoscheme (explicitly listing the UK as an example).

Key evidence: The official OpenAI blog post titled "Testing ads in ChatGPT" (https://openai.com/index/testing-ads-in-chatgpt/) carries an update dated May 7, 2026, which states: "In the coming weeks, we plan to expand the ads pilot in ChatGPT in the United Kingdom, Mexico, Brazil, Japan, and South Korea." [Testing ads in ChatGPT - OpenAI](https://openai.com/index/testing-ads-in-chatgpt/)

This meets every element of the resolution criteria:
1. Timing — The announcement is dated May 7, 2026, which falls strictly within the required window (on/after May 2, 2026 and before June 1, 2026, 11:59 PM UTC).
2. Europe — The United Kingdom is a country in Northern Europe under the UN geoscheme, and the question's resolution criteria explicitly name the UK as a qualifying example.
3. Source — The announcement is on OpenAI's official blog (openai.com/index/), an explicitly accepted "publicly announce" channel. It is also corroborated by major outlets and trade press (e.g., Campaign "ChatGPT Ads to launch in UK", Adweek "OpenAI Aggressively Expands Ads Pilot to More Countries" reporting OpenAI said on May 7 it will expand to the UK, Digiday "OpenAI takes ChatGPT ads global").
4. "ChatGPT advertising" as defined — The pilot is the in-interface sponsored-content ad pilot (paid promotional content within the ChatGPT UI), exactly the form of advertising the question targets, not some other monetization.

The criterion explicitly covers advertising that "has launched or is being tested." Trade coverage of the same OpenAI announcement describes it as OpenAI starting to "test ads in ... the U.K." in the coming weeks (Digiday), confirming this is a public announcement that ChatGPT advertising is being tested in a European country. The "in the coming weeks" framing of the rollout does not change that the public announcement itself occurred within the window, which is what the criteria require.

Note: A separate Digiday article (May 1, 2026) about OpenAI "laying foundations" for EU ads only described technical preparation and did not announce a European launch [OpenAI starts laying foundations for ChatGPT ads in EU - Digiday](https://digiday.com/marketing/openai-starts-laying-foundations-for-chatgpt-ads-in-eu/); that pre-window article is not the basis for resolution. The qualifying announcement is the May 7, 2026 OpenAI blog update naming the UK [Testing ads in ChatGPT - OpenAI](https://openai.com/index/testing-ads-in-chatgpt/).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-15. `4867b39d-d365-54e1-b4b9-f0ee4f7ecb82`

- Present date: `2026-05-15 18:35:51.288723`
- Source cutoff boundary: `2026-05-16` (encodes end of UTC day `2026-05-15`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Donald Trump publicly criticize Giorgia Meloni (by name or as Italian PM) on social media or in official remarks between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves as **YES** if, between 00:00 UTC on May 12, 2026, and 23:59 UTC on July 1, 2026, Donald Trump makes at least one public statement that criticizes, disparages, or expresses negative judgment toward Giorgia Meloni. All of the following conditions must be met:

1. **Attribution:** The statement must be directly attributable to Donald Trump — posted from his verified accounts or spoken by him in a recorded/transcribed setting.

2. **Platforms and sources monitored:**
   - Trump's Truth Social account: https://truthsocial.com/@realDonaldTrump
   - Trump's X (Twitter) account: https://x.com/realDonaldTrump
   - Official White House transcript archive: https://www.whitehouse.gov/remarks/
   - Interviews or press conferences as reported by major wire services (Reuters, AP) or newspapers of record (NYT, Washington Post, Wall Street Journal)

3. **Identification of Meloni:** The statement must refer to Giorgia Meloni by name ("Meloni," "Giorgia Meloni") or by her official title ("Italian Prime Minister," "Prime Minister of Italy," "the Italian leader," or similar unambiguous references).

4. **Definition of criticism:** The statement must express disapproval, condemnation, or negative judgment regarding Meloni's actions, policies, character, or competence. This includes but is not limited to: questioning her courage or loyalty, calling her "unacceptable" or "weak," accusing her of policy failures, threatening consequences against Italy tied to her leadership, or using clearly derogatory language about her. Neutral mentions, factual descriptions without negative framing, and praise do not count.

5. **Timing:** The criticism must be posted or spoken on or after May 12, 2026 (00:00 UTC) and no later than July 1, 2026 (23:59 UTC).

If no statement meeting all the above criteria is identified by 23:59 UTC on July 1, 2026, the question resolves **NO**.

**Pre-cutoff background**

As of mid-May 2026, the relationship between U.S. President Donald Trump and Italian Prime Minister Giorgia Meloni has deteriorated sharply. Meloni was once considered one of Trump's closest European allies—she was the only European leader to attend his 2025 inauguration, and Trump previously praised her as a "fantastic woman" [Donald Trump's ire and Russian criticism are helping Giorgia Meloni ...](https://www.cnn.com/2026/04/24/world/giorgia-meloni-trump-italy-intl). However, in April 2026, the relationship fractured over multiple issues:

- **Iran War:** Meloni distanced Italy from the U.S.-led military campaign against Iran, refusing to allow U.S. fighters to use an airbase in Sicily and suspending a military cooperation pact with Israel [Trump turns on Meloni, says he is 'shocked' by Italian leader | Reuters](https://www.reuters.com/world/europe/trump-turns-meloni-says-he-is-shocked-by-italian-leader-2026-04-14/).
- **Pope Leo XIV:** Meloni publicly criticized Trump's verbal attacks on the new Pope, calling them "unacceptable" [Trump turns on Meloni, says he is 'shocked' by Italian leader | Reuters](https://www.reuters.com/world/europe/trump-turns-meloni-says-he-is-shocked-by-italian-leader-2026-04-14/).
- **Public rebuke:** In an interview with Italian newspaper *Corriere della Sera* published around April 14, 2026, Trump called Meloni "unacceptable," said she "lacks courage," and stated "I thought she had courage. I was wrong" [Trump turns on Meloni, says he is 'shocked' by Italian leader | Reuters](https://www.reuters.com/world/europe/trump-turns-meloni-says-he-is-shocked-by-italian-leader-2026-04-14/). He also accused her of not caring whether Iran obtains nuclear weapons [Donald Trump's ire and Russian criticism are helping Giorgia Meloni ...](https://www.cnn.com/2026/04/24/world/giorgia-meloni-trump-italy-intl).

As of late April 2026, the two leaders remain publicly at odds, with no reported reconciliation. Meloni has adopted an "allies, not vassals" posture, and her domestic approval ratings have slightly recovered following these international disputes [Donald Trump's ire and Russian criticism are helping Giorgia Meloni ...](https://www.cnn.com/2026/04/24/world/giorgia-meloni-trump-italy-intl). Trump has a well-documented pattern of publicly criticizing leaders who defy him, making further criticism plausible but not certain—a de-escalation or quiet diplomacy could also occur.

**Exact later resolution packet**

The question resolves **YES**. Between May 12 and July 1, 2026, Donald Trump made multiple public statements clearly criticizing/disparaging Giorgia Meloni (referred to by name and as "Italian Prime Minister"), attributable directly to him and reported by monitored sources (Reuters, CBS, CNN).

Key qualifying evidence (June 19–20, 2026 — squarely within the window):

1. **Italian TV (La7) interview, June 19, 2026:** In a recorded/transcribed call broadcast by La7, Trump disparaged Meloni, saying "She begged me to take a picture with her. She wanted a picture with me so badly. I wouldn't have taken it, but I felt sorry for her." This is directly attributable to Trump (spoken by him) and reported by Reuters (https://www.reuters.com/business/media-telecom/meloni-fights-back-after-trump-tells-italian-tv-she-begged-photo-with-him-g7-2026-06-19/) and CNN (https://www.cnn.com/2026/06/19/politics/italy-trump-meloni-tajani) [3d2b3f, 7a7763].

2. **Truth Social post, June 20, 2026:** Trump doubled down on his own verified Truth Social account (a monitored platform), writing that Meloni "asked, over and over, for a picture" during the G7, and disparaging her: "She is doing poorly in Italy with her level of popularity, possibly because she turned down the United States of America... when it came to denying Iran from obtaining or developing a Nuclear Weapon," adding she "wouldn't even let us use Italy's landing strips or runways, a great logistical inconvenience." Reported by CBS News (https://www.cbsnews.com/news/trump-giorgia-meloni-stunned-italy-nixes-tajani-visit/) [0e64d1].

These statements plainly meet all resolution conditions: (1) directly attributable to Trump (spoken in a transcribed interview and posted from his verified Truth Social account); (2) sourced from monitored platforms/outlets (Trump's Truth Social plus Reuters/CNN/CBS wire and newspaper coverage); (3) identify Meloni by name and as "Italian Prime Minister"; (4) clearly express disparagement and negative judgment (mocking her as begging for a photo out of pity, and accusing her of harming Italy/refusing U.S. requests); and (5) fall within the May 12–July 1, 2026 window. Additional corroborating criticism also appears in early/mid-May 2026 talks (e.g., Al Jazeera, May 8, 2026), but the June 19–20 statements alone conclusively satisfy the criteria.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-16. `82f810af-002d-5361-bec4-2546bb30b9df`

- Present date: `2026-05-16 11:15:22.967852`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will there be a reported armed clash between Federal Government of Somalia (FGS) forces and South West State-aligned forces in Baidoa between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, between May 12, 2026 00:00 UTC and July 1, 2026 23:59 UTC, at least one credible source reports an armed clash in or around Baidoa, Somalia (defined as within the Baidoa district of Bay Region, South West State).

**Definitions:**

- **Armed clash**: An incident involving an exchange of gunfire or use of explosive weapons (e.g., mortars, grenades, RPGs) between the two specified parties, resulting in at least one reported casualty (killed or wounded) or confirmed exchange of fire even without reported casualties. Protests, arrests, or purely political confrontations without weapons fire do not qualify.

- **Federal forces**: The Somali National Army (SNA), Somali National Police, or any other security personnel operating under the direct authority of the Federal Government of Somalia in Mogadishu.

- **South West State-aligned forces**: South West State regional police, Darwish (regional paramilitary), clan militias explicitly described as aligned with or fighting on behalf of the SWS regional administration or former President Laftagareen, or armed groups described as opposing federal forces in the context of the SWS political dispute.

- **Geographic scope**: Baidoa district within Bay Region, South West State, Somalia. This includes Baidoa city and its immediate surroundings within approximately 30 km of the city center.

**Resolution sources**: The question resolves based on reporting from at least one of the following: Reuters, AP, AFP, BBC, Al Jazeera, UN OCHA situation reports (via ReliefWeb at https://reliefweb.int/country/som), or ACLED event data (https://acleddata.com/country/somalia). If none of these sources report such an event by July 1, 2026, the question resolves **No**.

**Pre-cutoff background**

As of May 2026, Baidoa, the capital of Somalia's South West State (SWS), remains a flashpoint of federal-regional tensions. In March 2026, the SWS severed ties with the Federal Government of Somalia (FGS) after the federal government pushed through constitutional amendments and sought to unseat the state's president, Abdiaziz Laftagareen. Clashes between SWS forces and opposition-aligned groups occurred on March 19–20, 2026, displacing over 45,000 people from Baidoa [Somalia - Political tensions and armed conflict (DG ECHO, UN ...](https://reliefweb.int/report/somalia/somalia-political-tensions-and-armed-conflict-dg-echo-un-ingos-echo-daily-flash-30-march-2026). The FGS declared SWS regional elections held on March 28 illegal and deployed a military convoy from Buurhakaba toward Baidoa [Somalia - Political tensions and armed conflict (DG ECHO, UN ...](https://reliefweb.int/report/somalia/somalia-political-tensions-and-armed-conflict-dg-echo-un-ingos-echo-daily-flash-30-march-2026). By late March, the Somali National Army (SNA) took control of Baidoa and the regional leader resigned. As of May 6, 2026, the federal government has appointed a caretaker leader (Jibril Abdirashid Haji Abdi) and scheduled new elections, which opposition networks including the Somali Future Council and the Salvation Forum are boycotting [Southwest State leadership warns of power vacuum in Baidoa](https://somalistream.com/southwest-state-leadership-warns-of-power-vacuum-in-baidoa/). Reports indicate rising tensions, looting, and the symbolic removal of regional insignia in Baidoa [Southwest State leadership warns of power vacuum in Baidoa](https://somalistream.com/southwest-state-leadership-warns-of-power-vacuum-in-baidoa/). The exiled SWS leadership characterizes federal actions as overreach and a violation of constitutional principles. The situation remains volatile, with federal-aligned forces asserting control but facing resistance from regional political actors and potential clan militia mobilization.

**Exact later resolution packet**

Adjudicated: An AFP wire report dated May 30, 2026 (byline AFP, republished at Arab News node/2645459, The News, New Arab, Frontier Post) describes an armed clash on Saturday May 30, 2026 on the outskirts of Baidoa (Idoow Dhagoole area, north of the city) between Somali federal government/army troops and fighters loyal to ousted South West State president Abdiaziz Hassan Mohamed 'Laftagareen'. The military commander Hussein Ali told AFP his forces counted ~six bodies of attackers and a resident reported two civilians wounded by stray bullets, satisfying the 'exchange of gunfire with at least one casualty' definition. This falls within the May 12 00:00 UTC - July 1 23:59 UTC window, is inside Baidoa district (~within 30 km), and Laftagareen loyalists explicitly qualify as 'South West State-aligned forces' / 'armed groups opposing federal forces in the context of the SWS political dispute.' The report comes from AFP, one of the named resolution sources. An earlier automated NO relied on failing to load the JS-rendered ReliefWeb page and missed the AFP reporting entirely.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-17. `a260075d-f882-537e-8f6a-b2ca6d18f97c`

- Present date: `2026-05-03 11:45:56.285175`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will incumbent U.S. Senator John Cornyn lose the Texas Republican primary runoff on May 26, 2026?

**Resolution criteria**

This question resolves YES if John Cornyn receives fewer votes than Ken Paxton in the Texas Republican primary runoff held on May 26, 2026, according to official results from the Texas Secretary of State (https://www.sos.state.tx.us/elections/) or as called by the Associated Press (https://apnews.com/hub/election-results-2026).

This question resolves NO if:
- Cornyn receives more votes than Paxton in the runoff, OR
- The runoff does not take place by June 1, 2026 (11:59 PM ET) for any reason.

Key definitions and clarifications:
- "Incumbent" means a person currently serving as a U.S. Senator at the time of the primary vote, including senators who were appointed rather than elected.
- "Primary election" in this question refers specifically to the Texas Republican primary runoff on May 26, 2026. This is a runoff election triggered by no candidate receiving more than 50% in the initial March 3, 2026 primary, and is considered part of the primary election process under Texas law.
- If Cornyn withdraws or is disqualified before the May 26, 2026 vote occurs, the question resolves NO, as no primary loss will have occurred.
- If results are not officially certified or called by AP by June 1, 2026 (11:59 PM ET), but preliminary results clearly indicate a winner, resolution may rely on credible reporting from AP, Reuters, or the Texas Tribune (https://www.texastribune.org/).
- All dates and deadlines are in U.S. Eastern Time (ET) unless otherwise specified. The runoff election takes place on May 26, 2026 (polls close at 7:00 PM CT / 8:00 PM ET).

**Pre-cutoff background**

Incumbent U.S. Senator John Cornyn (R-TX), who has served in the Senate since 2002, is facing Texas Attorney General Ken Paxton in a Republican primary runoff election scheduled for May 26, 2026. The runoff was triggered after the March 3, 2026 primary, in which Cornyn led Paxton 42.0% to 40.5%, with neither candidate clearing the 50% threshold required to avoid a runoff [United States Senate election in Texas, 2026 (May 26 Republican ...](https://ballotpedia.org/United_States_Senate_election_in_Texas,_2026_(May_26_Republican_primary_runoff)).

Recent polling shows an extremely tight race. A co/efficient poll (April 11–14, 2026) showed Cornyn 44%, Paxton 43% with 13% undecided. A Peak Insights poll (April 6–9, 2026) showed Cornyn 44%, Paxton 43%. A Slingshot Strategies poll (April 6–7, 2026) showed Paxton leading 48% to Cornyn's 40% [United States Senate election in Texas, 2026 (May 26 Republican ...](https://ballotpedia.org/United_States_Senate_election_in_Texas,_2026_(May_26_Republican_primary_runoff)). Cornyn has significantly outraised Paxton, ending Q1 2026 with over $8 million in cash on hand. Neither candidate has received a formal endorsement from President Trump.

Historically, incumbent U.S. Senators losing primary elections is rare but not unprecedented. This race is notable because Paxton, a statewide elected official with strong support among the populist wing of the Republican Party, represents a credible challenger. The deadline for either candidate to withdraw from the runoff ballot has passed without either doing so.

Other May 2026 Senate primaries include Ohio Special (May 5), Nebraska/North Carolina/West Virginia (May 12), Alabama/Georgia/Idaho/Kentucky/Oregon (May 19), but the Texas runoff is the only May contest where an incumbent senator faces a serious primary challenge [2026 Senatorial Primaries at a Glance - The Green Papers](https://www.thegreenpapers.com/G26/spaag).

**Exact later resolution packet**

The question resolves YES if John Cornyn received fewer votes than Ken Paxton in the Texas Republican primary runoff held May 26, 2026, per official Texas Secretary of State results or as called by the AP.

- Official Texas Secretary of State election results (https://electionresults.sos.state.tx.us/results.html) show, for the 2026 Republican Primary Runoff for U.S. Senator: Ken Paxton 885,949 votes vs. John Cornyn (I) 501,725 votes. Cornyn received far fewer votes than Paxton [Election Results - Tuesday, May 26, 2026](https://electionresults.sos.state.tx.us/results.html).

- Cornyn was still the incumbent U.S. Senator (serving since 2002) and did NOT withdraw or get disqualified — he delivered a concession speech on election night, and the AP called the race for Paxton shortly after polls closed [Ken Paxton defeats John Cornyn in Texas U.S. Senate GOP runoff](https://www.texastribune.org/2026/05/26/texas-john-cornyn-ken-paxton-us-senate-republican-primary-runoff/). The "(I)" designation in the SoS results confirms incumbency [Election Results - Tuesday, May 26, 2026](https://electionresults.sos.state.tx.us/results.html).

- The runoff took place on May 26, 2026, well before the June 1, 2026 11:59 PM ET deadline, and the race was called the same night [Ken Paxton defeats John Cornyn in Texas U.S. Senate GOP runoff](https://www.texastribune.org/2026/05/26/texas-john-cornyn-ken-paxton-us-senate-republican-primary-runoff/).

All NO conditions are excluded: Cornyn did not receive more votes, he did not withdraw/get disqualified, and the runoff did take place on schedule. Therefore the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-18. `35b53909-8dfe-5194-b1bb-cece83ae2e51`

- Present date: `2026-05-14 07:36:07.214865`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the U.S. Supreme Court rule in favor of the petitioner (Mullin/DHS) in Mullin v. Al Otro Lado (Docket 25-5)?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 (12:00 AM UTC) and by July 1, 2026 (11:59 PM UTC), the Supreme Court of the United States issues an opinion in Mullin v. Al Otro Lado (Docket 25-5) that **reverses or vacates** the Ninth Circuit's judgment, thereby ruling in favor of the petitioner (Mullin/DHS).

This question resolves **No** if the Court **affirms** the Ninth Circuit's judgment or otherwise rules in favor of the respondent (Al Otro Lado) on the merits.

If the Court **dismisses the case as improvidently granted (DIG)** or issues any other procedural disposition that does not reach the merits, the question resolves **No**, as the Ninth Circuit's ruling in favor of the respondent would remain intact.

In the event of a split or partial decision, the question resolves based on the majority opinion's disposition of the judgment below: if the Ninth Circuit's judgment is reversed or vacated (in whole or in part), the question resolves Yes; if affirmed, it resolves No.

**Primary resolution source:** The official slip opinion published on the Supreme Court's website at https://www.supremecourt.gov/opinions/slipopinion/25 and the docket page at https://www.supremecourt.gov/docket/docketfiles/html/public/25-5.html.

**Pre-cutoff background**

Mullin v. Al Otro Lado (Docket 25-5) is a pending U.S. Supreme Court case concerning whether noncitizens stopped on the Mexican side of a U.S. land port of entry have "arrived in the United States" under the Immigration and Nationality Act (INA), specifically 8 U.S.C. §§ 1158(b)(1)(A), 1225(a)(1), and 1225(a)(3) [Mullin v. Al Otro Lado - Wikipedia](https://en.wikipedia.org/wiki/Mullin_v._Al_Otro_Lado). The case challenges the legality of the "metering" policy, under which U.S. Customs and Border Protection directed asylum seekers to remain in Mexico rather than processing them on U.S. soil [https://www.scotusblog.com/2026/03/court-appears-likely-to-side-with-trump-administration-on-rights-of-asylum-seekers/](https://www.scotusblog.com/2026/03/court-appears-likely-to-side-with-trump-administration-on-rights-of-asylum-seekers/).

The Ninth Circuit held that noncitizens who present themselves at the threshold of a U.S. port of entry—even if physically in Mexico—have "arrived in the United States" and are entitled to inspection and asylum processing [Mullin v. Al Otro Lado - Wikipedia](https://en.wikipedia.org/wiki/Mullin_v._Al_Otro_Lado). The government (petitioner, Secretary of Homeland Security Markwayne Mullin) appealed, arguing that "arrives in" requires physical presence within U.S. territory.

Oral arguments were held on March 24, 2026. According to SCOTUSblog, the Court "appeared likely to side with the Trump administration," with conservative justices favoring the government's textualist reading, while Justices Sotomayor, Jackson, and Kagan raised concerns about international treaty obligations and statutory construction [https://www.scotusblog.com/2026/03/court-appears-likely-to-side-with-trump-administration-on-rights-of-asylum-seekers/](https://www.scotusblog.com/2026/03/court-appears-likely-to-side-with-trump-administration-on-rights-of-asylum-seekers/). As of May 13, 2026, no opinion has been issued. A decision is expected by the end of the Court's October 2025 term in late June 2026.

**Exact later resolution packet**

The question resolves YES (1).

- Verification of date: The Supreme Court issued its opinion in Mullin v. Al Otro Lado (Docket 25-5) on June 25, 2026. This falls within the resolution window of May 12, 2026 through July 1, 2026, inclusive.

- Verification of disposition: The official Supreme Court slip opinion PDF (https://www.supremecourt.gov/opinions/25pdf/25-5_86qd.pdf) and the official docket (https://www.supremecourt.gov/docket/docketfiles/html/public/25-5.html) confirm that the Court REVERSED and REMANDED the Ninth Circuit's judgment. The docket entry for June 25, 2026 states "Judgment REVERSED and case REMANDED" [ef76b0]. The slip opinion holds that under the INA, an alien "arrives in the United States" only when the alien crosses the border into the United States — i.e., an alien standing at the border in Mexico is not entitled to apply for asylum or to inspection [e821d5]. This directly rejects the Ninth Circuit's contrary holding.

- The disposition was a merits reversal (6-3, opinion by Justice Alito), NOT a Dismissal as Improvidently Granted (DIG) and not any other non-merits procedural disposition. Therefore the DIG-triggered NO condition does not apply.

- Because the Ninth Circuit's judgment was reversed (in whole), the petitioner (Mullin/DHS) prevailed, satisfying the resolution criteria for a YES.

Primary official sources used:
- Official slip opinions list for OT2025: https://www.supremecourt.gov/opinions/slipopinion/25 [e821d5]
- Official docket for 25-5: https://www.supremecourt.gov/docket/docketfiles/html/public/25-5.html [ef76b0]
- Official slip opinion PDF: https://www.supremecourt.gov/opinions/25pdf/25-5_86qd.pdf

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-19. `d8d1e6cc-35f1-5c58-9056-7eaad25ddc20`

- Present date: `2026-05-29 04:20:21.958677`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Junts per Catalunya vote in favor of or abstain on any government-sponsored Real Decreto-ley in the Spanish Congress of Deputies between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, according to the official voting records of the Congreso de los Diputados (available at https://www.congreso.es/en/cem/febjun2026 and https://www.congreso.es/opendata/votaciones), the parliamentary group Junts per Catalunya (as listed in the official Congress records: https://www.congreso.es/busqueda-de-diputados) records a group-level vote of "Sí" (in favor) or "Abstención" (abstention) on the validation ("convalidación") of at least one Real Decreto-ley submitted by the Spanish government, in a plenary vote occurring on or after May 12, 2026, 00:00 UTC and before July 1, 2026, 23:59 UTC.

A "vote in favor" means the majority of Junts deputies present vote "Sí" in the official roll-call vote. An "abstention" means the majority of Junts deputies present vote "Abstención." These are recorded as such in the official plenary voting records (actas de votación) of the Congress.

If Junts votes "No" on all government-sponsored Real Decreto-ley validations during this period, or if no such validations are voted on during this period, the question resolves as **No**.

The resolution source is the official voting records of the Congreso de los Diputados: https://www.congreso.es/opendata/votaciones

**Pre-cutoff background**

Junts per Catalunya is a Catalan political party whose parliamentary group in the Spanish Congress of Deputies (Congreso de los Diputados) currently holds 7 seats, making it a critical swing vote for the minority government of Prime Minister Pedro Sánchez. A "Real Decreto-ley" (Royal Decree-Law) is an urgent legislative instrument issued by the Spanish government under Article 86 of the Spanish Constitution (https://www.boe.es/buscar/act.php?id=BOE-A-1978-31229), which must be validated or repealed by the Congress within 30 days of its promulgation.

Throughout 2026, Junts has increasingly distanced itself from the Sánchez government. In January 2026, PP, Vox, and Junts voted together to reject the government's "social shield" omnibus decree that included pension increases and eviction moratoriums. In late April 2026, Junts again voted against a housing decree extending rental contracts, further signaling its shift toward opposition. However, the political situation remains fluid: in January 2025, Sánchez and Junts reached a deal on "29 measures" covering pensions and social protections, and as recently as April 22, 2026, Sánchez stated his government has "the political will to finalise all the agreements with the parliamentary groups that supported the investiture." Additionally, in May 2026, the government was reportedly preparing new decree-laws on housing and other matters, with Junts' support remaining uncertain. Notably, Junts has previously voted in favor of some government decrees when they addressed narrow, specific issues (e.g., a decree on war-related measures), suggesting that cooperation on specific topics remains possible even amid broader political tensions.

As of May 13, 2026 (UTC), Junts has voted against the most recent government decree-laws but has not categorically ruled out supporting future narrow, issue-specific decrees.

**Exact later resolution packet**

The question resolves YES. Junts per Catalunya recorded a group-level vote of "Abstención" and/or "Sí" on the validation (convalidación) of at least two government-sponsored Reales Decretos-leyes in the Congreso de los Diputados within the resolution window (May 12, 2026 00:00 UTC – July 1, 2026 23:59 UTC). Either one alone is sufficient for YES.

DECREE 1 — Real Decreto-ley 11/2026, de 12 de mayo (pharmaceutical copayment / copago reform), convalidated on May 28, 2026 (within window):
• Junts ABSTAINED. Multiple quality sources report the validation passed with 164 votes in favor, 33 against, and 149 abstentions, and explicitly name the abstaining groups as PP, ERC and Junts. Confirmed by Diariofarma ("Una amplia abstención de PP, ERC y Junts permite convalidar la reforma del copago") [Una amplia abstención de PP, ERC y Junts permite convalidar la ...](https://diariofarma.com/2026/05/28/una-amplia-abstencion-de-pp-erc-y-junts-facilita-la-convalidacion-del-congreso-a-la-reforma-del-copago), El Global [El Congreso convalida el nuevo modelo de copago farmacéutico](https://elglobalfarma.com/farmacia/copago-farmaceutico-congreso-convalida-nuevo-modelo/), and El Periódico (149 abstentions from PP, ERC and Junts) [El Congreso da luz verde al nuevo copago farmacéutico, que ...](https://www.elperiodico.com/es/sociedad/20260528/congreso-convalida-copago-farmaceutico-rebaja-130745477). A Google-indexed post attributed to the Congreso de los Diputados' own LinkedIn likewise states the chamber approved "el Real Decreto-ley 11/2026" with "164 votos a favor y 149 abstenciones (PP, ERC y Junts)."
• This clearly satisfies the resolution rule: the majority of Junts deputies present voted "Abstención" on the convalidación of a government Real Decreto-ley.

DECREE 2 — Real Decreto-ley 13/2026, de 2 de junio (entregas a cuenta / territorial financing resources), convalidated on June 18, 2026 (within window):
• Junts VOTED IN FAVOR ("Sí"). The official Congreso de los Diputados press release states the Pleno validated RDL 13/2026 with 313 votes in favor and 33 against [Notas de prensa - Congreso de los Diputados](https://www.congreso.es/es/notas-de-prensa?p_p_id=notasprensa&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_notasprensa_mvcPath=detalle&_notasprensa_notaId=51874) [Notas de prensa - Congreso de los Diputados](https://www.congreso.es/es/notas-de-prensa?p_p_id=notasprensa&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_notasprensa_mvcPath=detalle&_notasprensa_notaId=51874). The 33 "against" votes correspond to Vox's seats; multiple outlets (Público [El Congreso convalida el decreto con las entregas a cuenta a las ...](https://www.publico.es/politica/congreso/congreso-convalida-decreto-entregas-cuenta-autonomias-unico-voto-vox.html), Demócrata/ "PNV y Junts avalan el decreto de entregas a cuenta" [PNV y Junts avalan el decreto de entregas a cuenta - Demócrata](https://www.democrata.es/economia/pnv-y-junts-garantizan-la-convalidacion-del-decreto-de-entregas-a-cuenta-en-el-congreso/), PSOE) confirm Vox was the ONLY party to vote against, meaning Junts's 7 deputies voted in favor. It was also dubbed the "decreto Junts" because it incorporated Junts' local-financing demands.

Both instruments are indisputably "Reales Decretos-leyes" (not ordinary Leyes) and both votes were "convalidación" votes submitted by the Sánchez government, occurring within the May 12 – July 1, 2026 window. Therefore the resolution is YES (1).

Note: The QUERY_DOCUMENT tool at times output "resolution 0" by wrongly assuming, from the question's narrative framing, that Junts must have voted "No"; however, the primary reporting (including the official Congress press release and multiple independent outlets) is explicit that Junts abstained on RDL 11/2026 and voted in favor of RDL 13/2026.

Key URLs:
- Diariofarma (RDL 11/2026 copago, PP/ERC/Junts abstention, 164-33-149): https://diariofarma.com/2026/05/28/una-amplia-abstencion-de-pp-erc-y-junts-facilita-la-convalidacion-del-congreso-a-la-reforma-del-copago
- El Periódico (copago, Junts among abstentions): https://www.elperiodico.com/es/sociedad/20260528/congreso-convalida-copago-farmaceutico-rebaja-130745477
- Congreso de los Diputados press release (RDL 13/2026, 313-33): https://www.congreso.es/es/notas-de-prensa?_notasprensa_notaId=51874
- Público (RDL 13/2026, único voto en contra de Vox): https://www.publico.es/politica/congreso/congreso-convalida-decreto-entregas-cuenta-autonomias-unico-voto-vox.html
- Congress open-data voting portal (resolution source): https://www.congreso.es/opendata/votaciones

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-20. `954bb27f-4c31-57a9-bac6-1b4d9af76f68`

- Present date: `2026-05-16 15:41:01.739123`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the President issue an Executive Order placing specific federal positions into Schedule Policy/Career before July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if an Executive Order is published—either in the Federal Register (https://www.federalregister.gov/presidential-documents/executive-orders) or announced via the official White House Briefing Room (https://www.whitehouse.gov/briefing-room/presidential-actions/)—on or after May 12, 2026, 12:00 AM Eastern Time, and before July 1, 2026, 11:59 PM Eastern Time, that explicitly places one or more specific federal positions into "Schedule Policy/Career" as defined under the 2026 OPM Final Rule (published February 6, 2026, in the Federal Register as document 2026-02375; see also CRS report LSB11412: https://www.congress.gov/crs-product/LSB11412).

"Schedule Policy/Career" refers to the excepted-service appointment category for positions of a "confidential, policy-determining, policy-making, or policy-advocating character" established under Executive Order 14171 and the 2026 final rule, as described in CRS report LSB11412 (https://www.congress.gov/crs-product/LSB11412) [https://www.congress.gov/crs-product/LSB11412](https://www.congress.gov/crs-product/LSB11412).

This question resolves as **No** if no such Executive Order is published or announced by 11:59 PM Eastern Time on July 1, 2026.

Resolution sources:
- Federal Register Executive Orders section: https://www.federalregister.gov/presidential-documents/executive-orders
- White House Briefing Room Presidential Actions: https://www.whitehouse.gov/briefing-room/presidential-actions/

**Pre-cutoff background**

On January 20, 2025, President Trump signed Executive Order 14171, "Restoring Accountability to Policy-Influencing Positions Within the Federal Workforce," which reinstated the framework for reclassifying certain career federal positions into a new excepted-service category called "Schedule Policy/Career" (formerly known as "Schedule F"). On February 6, 2026, the Office of Personnel Management (OPM) published a final rule implementing Schedule Policy/Career, which took effect on March 9, 2026 [https://www.congress.gov/crs-product/LSB11412](https://www.congress.gov/crs-product/LSB11412).

Critically, the 2026 final rule designates the President—rather than OPM—as the authority to place specific positions into Schedule Policy/Career via executive order. No positions can be moved into Schedule Policy/Career until the President issues such an order [https://www.congress.gov/crs-product/LSB11412](https://www.congress.gov/crs-product/LSB11412).

As of March 26, 2026 (the date of the CRS report LSB11412), the President had not yet issued this executive order [https://www.congress.gov/crs-product/LSB11412](https://www.congress.gov/crs-product/LSB11412). The Wikipedia article on Schedule F, last updated in the source reviewed, also confirms no such order had been issued as of its most recent update [Schedule F appointment - Wikipedia](https://en.wikipedia.org/wiki/Schedule_F_appointment). Based on available reporting as of May 13, 2026, there is no indication that such an executive order has been issued yet.

Regarding litigation: The National Treasury Employees Union (NTEU) filed a lawsuit challenging the legality of Schedule Policy/Career in the U.S. District Court for the District of Columbia. On March 17, 2026, the court accepted NTEU's proposal to file an amended complaint within 14 days of the President issuing an executive order that places positions in Schedule Policy/Career [https://www.congress.gov/crs-product/LSB11412](https://www.congress.gov/crs-product/LSB11412). This means the issuance of the EO would immediately trigger the next phase of litigation.

Agencies have been required to submit lists of proposed positions to OPM, and OPM estimated approximately 50,000 federal employees could be affected. The timing of the presidential EO depends on litigation strategy, political calculus, and administrative readiness.

**Exact later resolution packet**

The question resolves YES.

The question asks whether the President issued an Executive Order, published either in the Federal Register or the White House Briefing Room/Presidential Actions, on or after May 12, 2026 (12:00 AM ET) and before July 1, 2026 (11:59 PM ET), that explicitly places one or more specific federal positions into "Schedule Policy/Career" as defined under the 2026 OPM Final Rule.

Evidence:
- On June 3, 2026, President Trump signed Executive Order 14410, "Implementing Schedule Policy/Career in the Excepted Service," published on the official White House Presidential Actions page (https://www.whitehouse.gov/presidential-actions/2026/06/implementing-schedule-policy-career-in-the-excepted-service/). Section 5(b) of the order states: "The positions set forth in the Appendix to this order are hereby placed in Schedule Policy/Career of the excepted service." Section 5(a) determines those Appendix positions to have "a confidential, policy-determining, policy-making, or policy-advocating character." The order links to a specific Appendix (the ~229-page list of positions) [Implementing Schedule Policy/Career in the Excepted Service](https://www.whitehouse.gov/presidential-actions/2026/06/implementing-schedule-policy-career-in-the-excepted-service/).
- The same Executive Order was published in the Federal Register on June 10, 2026 (Volume 91, Number 111), which likewise includes Section 5(b): "The positions set forth in the Appendix to this order are hereby placed in Schedule Policy/Career of the excepted service" [Federal Register, Volume 91 Issue 111 (Wednesday, June 10, 2026)](https://www.govinfo.gov/content/pkg/FR-2026-06-10/html/2026-11594.htm).

Both of the designated resolution sources (Federal Register and White House Presidential Actions) contain the qualifying order, published within the window (June 3/June 10, 2026, which is on or after May 12, 2026 and before July 1, 2026). The order does not merely establish or discuss the framework — it explicitly places specific enumerated positions (listed in the Appendix) into "Schedule Policy/Career" as defined under the 2026 OPM Final Rule (document 2026-02375). This satisfies every element of the YES resolution criteria.

Specific URLs to the qualifying document:
- White House: https://www.whitehouse.gov/presidential-actions/2026/06/implementing-schedule-policy-career-in-the-excepted-service/ [Implementing Schedule Policy/Career in the Excepted Service](https://www.whitehouse.gov/presidential-actions/2026/06/implementing-schedule-policy-career-in-the-excepted-service/)
- Federal Register (via govinfo): https://www.govinfo.gov/content/pkg/FR-2026-06-10/html/2026-11594.htm [Federal Register, Volume 91 Issue 111 (Wednesday, June 10, 2026)](https://www.govinfo.gov/content/pkg/FR-2026-06-10/html/2026-11594.htm)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-21. `c642ff10-a88a-561a-a137-b1398888abde`

- Present date: `2026-05-29 01:52:37.700146`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Todd Blanche still be serving as Acting Attorney General on July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, as of 11:59 PM UTC on July 1, 2026, Todd Blanche holds the title of "Acting Attorney General" of the United States. An "Acting Attorney General" is defined as a person who temporarily performs the duties of the Attorney General without having been nominated and confirmed by the U.S. Senate for that specific role, as described by the Federal Vacancies Reform Act (see: https://www.law.cornell.edu/uscode/text/5/3345).

This question resolves as **No** if any of the following are true by 11:59 PM UTC on July 1, 2026:
- Blanche has resigned or been removed from the Acting Attorney General position.
- Blanche has been replaced by another individual (whether acting or Senate-confirmed) as Attorney General.
- Blanche has transitioned from "Acting" to a permanent, Senate-confirmed Attorney General. In this specific case, the question resolves **No**, because he would no longer be serving in an "acting" capacity but rather as the confirmed Attorney General.

The resolution source shall be the official DOJ leadership page (https://www.justice.gov/ag) or official White House announcements. If these sources are unavailable or ambiguous, credible reporting from major news outlets (e.g., AP at https://apnews.com, Reuters at https://www.reuters.com, The New York Times at https://www.nytimes.com, or POLITICO at https://www.politico.com) confirming his status as of that date will be used.

**Pre-cutoff background**

Todd Blanche has served as the Acting United States Attorney General since April 2, 2026, when he was appointed by President Donald Trump following the dismissal of Attorney General Pam Bondi [Todd Blanche](https://en.wikipedia.org/wiki/Todd_Blanche). Blanche previously served as Deputy Attorney General, a position he has held since his Senate confirmation on March 6, 2025 [Todd Blanche](https://en.wikipedia.org/wiki/Todd_Blanche). Before joining the DOJ, Blanche was Trump's personal defense attorney in multiple criminal cases.

As of May 13, 2026, Blanche remains the Acting Attorney General. Under the Federal Vacancies Reform Act, acting appointments are generally limited to 210 days, which would allow Blanche to serve until approximately October 29, 2026 [Todd Blanche could stay atop DOJ for months even without ...](https://www.politico.com/news/2026/04/27/todd-blanche-attorney-general-justice-department-00892530). President Trump has historically expressed a preference for "acting" officials, citing the flexibility it provides [Todd Blanche could stay atop DOJ for months even without ...](https://www.politico.com/news/2026/04/27/todd-blanche-attorney-general-justice-department-00892530). Blanche has publicly stated he would accept a formal nomination to become permanent Attorney General if asked [Todd Blanche could stay atop DOJ for months even without ...](https://www.politico.com/news/2026/04/27/todd-blanche-attorney-general-justice-department-00892530), but it remains unclear whether Trump intends to nominate Blanche, another candidate, or continue relying on the acting appointment [Todd Blanche could stay atop DOJ for months even without ...](https://www.politico.com/news/2026/04/27/todd-blanche-attorney-general-justice-department-00892530).

Blanche's tenure has been characterized by politically charged investigations and prosecutions. His position faces cross-pressures from multiple directions, including scrutiny over his loyalty and the outcomes of high-profile cases [Todd Blanche could stay atop DOJ for months even without ...](https://www.politico.com/news/2026/04/27/todd-blanche-attorney-general-justice-department-00892530). The Trump administration has a well-documented pattern of rapid leadership turnover at the DOJ and elsewhere in the Cabinet.

**Exact later resolution packet**

The question resolves YES: Todd Blanche was still serving as "Acting Attorney General" as of 11:59 PM UTC on July 1, 2026.

PRIMARY RESOLUTION SOURCE (as specified in criteria): The official DOJ leadership page (https://www.justice.gov/ag) explicitly lists Todd Blanche as the "Acting Attorney General," featuring a section titled "Meet the Acting Attorney General." The page contained news items as recent as June 29, 2026, confirming currency as of the resolution date [https://www.justice.gov/ag](https://www.justice.gov/ag). The corresponding DOJ staff profile (https://www.justice.gov/ag/staff-profile/meet-acting-attorney-general-0) states his title as "Acting Attorney General of the United States," with dates of service "2026 – Present," and shows no Senate confirmation to the AG role [https://www.justice.gov/ag/staff-profile/meet-acting-attorney-general-0](https://www.justice.gov/ag/staff-profile/meet-acting-attorney-general-0).

CRITICAL DISTINCTION (nomination ≠ confirmation): President Trump formally NOMINATED Blanche to be the permanent Attorney General on June 8, 2026 (the White House sent the nomination to the Senate). However, the resolution criteria only trigger a NO outcome if Blanche (a) resigned/was removed, (b) was replaced by another individual, or (c) TRANSITIONED to a permanent, Senate-CONFIRMED Attorney General. None of these occurred. A mere nomination does not change his "Acting" status. His Senate Judiciary Committee confirmation hearing was scheduled for July 15–16, 2026 — AFTER the July 1 deadline — so he had not been confirmed by the Senate as of July 1, 2026 (corroborated by Ballotpedia, Federal News Network, Washington Post, and POLITICO reporting). Senate Republicans were reportedly aiming to confirm him "by the end of the summer," further confirming no confirmation had occurred by July 1.

CONCLUSION: As of 11:59 PM UTC on July 1, 2026, Todd Blanche held the title of "Acting Attorney General" — performing the duties of AG without yet having been Senate-confirmed to that specific role — exactly matching the YES condition. No other individual (acting or confirmed) held the AG position. Resolution: YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-22. `7d4620a7-e855-5c4a-86af-3856e7176d02`

- Present date: `2026-05-11 13:27:02.786193`
- Source cutoff boundary: `2026-05-12` (encodes end of UTC day `2026-05-11`)
- Expected resolution: `2026-06-11T00:00:00`

**Question**

Will the UK-France 'one-in-one-out' pilot scheme be extended or renewed beyond its scheduled end date of June 11, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 8, 2026 and by 23:59 UTC on August 1, 2026, there is an official announcement confirming that the UK-France 'one-in-one-out' pilot scheme will continue operating beyond June 11, 2026. An "official announcement" means any of the following:

1. A press release or policy statement published on GOV.UK (https://www.gov.uk/government/news) or by the UK Home Office;
2. A formal statement by the UK Home Secretary or the French Minister of the Interior;
3. A new memorandum of understanding or bilateral agreement explicitly extending or renewing the scheme;
4. A public statement reported by at least two credible news outlets (e.g., BBC, Reuters, The Guardian, AP, The Times).

The question also resolves **Yes** if the scheme is replaced by a similar program — i.e., one that retains the core mechanism of returning small boat arrivals to France while admitting asylum seekers from France — provided the UK government explicitly describes it as a continuation, extension, or successor to the one-in-one-out pilot.

The question resolves as **No** if:
- The scheme expires on June 11, 2026, with no official announcement of extension or renewal;
- An official government source explicitly states the scheme has been terminated or will not be renewed;
- No official confirmation of an extension or successor program is published by 23:59 UTC on August 1, 2026.

Primary resolution sources: GOV.UK announcements (https://www.gov.uk/government/news), UK Parliament Commons Library briefing on UK-France border cooperation (https://commonslibrary.parliament.uk/research-briefings/cbp-9681/), and credible reporting from BBC, Reuters, or The Guardian.

**Pre-cutoff background**

The UK-France 'one-in-one-out' pilot scheme (internally known as "Operation Hillmore") was formalized in August 2025. Under the scheme, migrants arriving in the UK via small boats can be returned to France, while the UK accepts an equivalent number of asylum seekers from France who meet specific eligibility criteria (e.g., family ties in the UK, or originating from countries with high asylum success rates such as Afghanistan or Syria). The pilot is scheduled to end on June 11, 2026 [United Kingdom–France one in, one out plan - Wikipedia](https://en.wikipedia.org/wiki/United_Kingdom%E2%80%93France_one_in,_one_out_plan).

As of January 27, 2026, the scheme had facilitated the removal of 281 migrants from the UK to France and the acceptance of 350 migrants from France to the UK [United Kingdom–France one in, one out plan - Wikipedia](https://en.wikipedia.org/wiki/United_Kingdom%E2%80%93France_one_in,_one_out_plan). By March 2026, approximately 377 returns had been made to France, while over 21,172 small boat crossings had been recorded in the same period — highlighting the scheme's limited scale relative to the overall migration challenge. The scheme has also faced legal challenges, including cancelled flights in September 2025 and January 2026 [United Kingdom–France one in, one out plan - Wikipedia](https://en.wikipedia.org/wiki/United_Kingdom%E2%80%93France_one_in,_one_out_plan).

On April 23, 2026, the UK and France signed a separate, larger £662 million three-year deal focused on enforcement measures. This includes deployment of at least 50 riot-trained police officers, a 42% increase in law enforcement personnel in northern France (totaling nearly 1,100 officers), drones, two helicopters, a camera system, and a 140-capacity removal centre in Dunkirk [UK and France strike new £662m small boats deal - BBC](https://www.bbc.com/news/articles/cz0ev7enk2lo). Notably, the £662 million deal does not explicitly mention whether the one-in-one-out scheme will be extended, subsumed, or replaced [UK and France strike new £662m small boats deal - BBC](https://www.bbc.com/news/articles/cz0ev7enk2lo) [New UK-France agreement to reduce illegal crossings - GOV.UK](https://www.gov.uk/government/news/new-uk-france-agreement-to-reduce-illegal-crossings). This ambiguity creates genuine uncertainty about the pilot's future.

For further context, see the Wikipedia article on the scheme (https://en.wikipedia.org/wiki/United_Kingdom%E2%80%93France_one_in,_one_out_plan) and the UK government's April 2026 announcement (https://www.gov.uk/government/news/new-uk-france-agreement-to-reduce-illegal-crossings).

**Exact later resolution packet**

The question resolves YES. The UK-France 'one-in-one-out' pilot scheme was officially extended beyond its scheduled end date of June 11, 2026, to October 1, 2026, with the announcement occurring squarely within the required resolution window (on or after May 8, 2026 and before 23:59 UTC on August 1, 2026).

Evidence:

1. THE GUARDIAN (May 16, 2026) — "UK and France extend 'one in, one out' small boats pilot scheme until October." The Guardian reported, based on Home Office sources, that the scheme would be extended until October 1, 2026 [5fa8ae]. URL: https://www.theguardian.com/uk-news/2026/may/16/uk-and-france-extend-one-in-one-out-small-boats-pilot-scheme-until-october

2. EURONEWS (June 3, 2026) — "UK and France extend 'one-in, one-out' migrant deal until October, minister says." The UK Home Office confirmed the arrangement, and France's minister delegate for Europe, Benjamin Haddad, confirmed the extension to October 1, 2026, before a parliamentary committee on June 3, 2026 [27d1df]. URL: https://www.euronews.com/my-europe/2026/06/03/uk-france-one-in-one-out-migrant-deal-extended-until-october-minister-says

3. LE MONDE (June 3, 2026) — Reported that French minister Benjamin Haddad told a parliamentary committee: "It has been decided with our British partner to extend this agreement until October 1, 2026" [9f07d1]. URL: https://www.lemonde.fr/en/international/article/2026/06/03/france-britain-extend-one-in-one-out-migration-deal_6754110_4.html

4. INFOMIGRANTS (June 5, 2026) — Confirmed the extension to October 1, 2026, and explicitly noted the extended scheme retains the same core mechanism: deporting irregular small-boat arrivals back to France in exchange for the UK accepting an equivalent number of eligible asylum seekers from France [aadea6]. URL: https://www.infomigrants.net/en/post/71746/france-extends-one-in-one-out-migrant-swap-scheme-with-uk

This satisfies the resolution criteria in multiple independent ways:
- An official announcement confirming the scheme will continue beyond June 11, 2026 was made within the window (Guardian May 16, 2026; official statements June 3, 2026).
- The extension was reported by at least four credible news outlets (The Guardian, Euronews, Le Monde, InfoMigrants), far exceeding the "at least two credible news outlets" threshold (criterion 4).
- The UK Home Office confirmed the arrangement to Euronews (criterion 1), and a French government minister made a formal public statement (criterion 2, in spirit — Haddad is minister delegate for Europe rather than Interior Minister, but the news-reporting criterion is independently met).
- It is the same scheme being extended (not a replacement), retaining the core mechanism of returning small-boat arrivals to France while admitting asylum seekers from France [aadea6].

The scheme therefore did NOT expire on June 11, 2026 without renewal; it was extended to October 1, 2026 before the August 1, 2026 deadline. (Note: The House of Commons Library briefing CBP-9681, dated May 13, 2026, did not yet reflect the extension [308074], but this simply predates the widely-reported announcement and does not contradict it. The Wikipedia article snapshot [472ec2] was last updated March 25, 2026 and likewise predates the announcement.)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-23. `12949926-6a31-58fb-835a-5f9580d4fc45`

- Present date: `2026-05-02 15:36:50.632504`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will NFL owners approve a minority stake sale in any NFL team at the May 2026 Spring League Meeting?

**Resolution criteria**

This question resolves YES if, on or after May 1, 2026, 12:00 AM UTC, and on or before June 1, 2026, 11:59 PM UTC, NFL owners formally approve the sale of a minority stake in any NFL team.

Definitions:
- **"Minority stake"**: Any non-controlling ownership interest (less than 50% of total equity) in an NFL franchise, whether sold to a private equity firm, an individual, a family office, or any other entity. This includes both limited partnership (LP) stakes and any other form of minority ownership interest.
- **"NFL owner approval"**: A formal vote by NFL franchise owners meeting the league's required threshold of at least three-quarters (24 of 32) of owners voting in favor, as required by NFL ownership transfer rules. This includes votes taken at any official NFL meeting (such as the Spring League Meeting) or via any other formal voting mechanism the league uses.
- Teams whose minority stake sales were already approved prior to May 1, 2026 do not count toward resolution, even if the transaction closes during the resolution window. Only new approvals count.

Resolution sources: Official NFL Communications (https://nflcommunications.com/), NFL.com (https://www.nfl.com/news/), or credible sports news reporting from ESPN (https://www.espn.com/nfl/), The Athletic, Sports Business Journal, or AP/Reuters.

If no such approval is confirmed by these sources by 11:59 PM UTC on June 1, 2026, this question resolves NO.

**Pre-cutoff background**

The NFL has seen a wave of minority ownership transactions since August 2024, when owners passed Resolution JC-7 in a 31-1 vote, allowing private equity firms to purchase up to 10% of any franchise as passive, non-voting investors (minimum 3% per fund, six-year hold period). Since then, multiple minority stakes have been approved: the 49ers, Chargers, and Browns (May 2025); the Bills, Eagles, and Dolphins (winter 2025); and the Giants, Patriots, and 49ers (October 2025). At the March 29-31, 2026 annual league meeting in Phoenix, the Dolphins and Steelers LP stake sales were on the agenda, and at least one minority sale was approved on March 31, 2026. As of May 1, 2026, the next opportunity for NFL owners to vote on ownership transactions is the Spring League Meeting, scheduled for May 19-20, 2026, in Orlando, Florida [2026 National Football League important dates](https://www.nfl.com/news/2026-national-football-league-important-dates). NFL ownership sales require approval by at least three-quarters (24 of 32) of the league's owners. Additional minority stake deals may be in the pipeline, as NFL Commissioner Roger Goodell has discussed potentially raising the private equity ownership cap above 10%, and the Seahawks controlling-interest sale process is also ongoing. Whether any new minority stake sale will be put to a vote at the May spring meeting—rather than deferred to the fall meeting—is uncertain and depends on the readiness of pending deals.

**Exact later resolution packet**

The question resolves YES. NFL owners formally approved the sale of a minority stake in the Las Vegas Raiders at the May 2026 Spring League Meeting in Orlando on May 19, 2026 — squarely within the resolution window (May 1, 2026, 12:00 AM UTC to June 1, 2026, 11:59 PM UTC).

Evidence:
- A CNBC article (published May 14, 2026) reported that a group led by Egon Durban agreed to buy a 25% stake in the Las Vegas Raiders at a $9.9 billion valuation, with the deal "subject to league approval at the NFL owners meeting next week" (i.e., the May 19, 2026 Spring League Meeting). It confirmed Mark Davis would remain controlling owner with 36%, making this an unambiguously minority (non-controlling) interest of less than 50% [be0aba].
- A Yahoo Sports article confirmed the approval actually occurred: "The NFL approved the group's purchase of 25 percent of the club on Tuesday in Orlando," expanding Durban's stake to roughly 22% while Davis remained controlling owner [9e477c].

This satisfies all resolution criteria:
1. Timing: Approval on May 19, 2026, is within the May 1 – June 1, 2026 window.
2. New approval (not a closing): The CNBC source shows the vote was scheduled for and held at the May 19 meeting — it was a new approval, not the closing of a previously approved deal [be0aba].
3. Minority stake: 25% is less than 50% of total equity, and Davis retained controlling ownership [be0aba, 9e477c].
4. NFL owner approval threshold: NFL ownership transfers require approval by at least 24 of 32 owners; the transaction was formally approved by the owners at the league meeting [9e477c].

This is not a conditional (IF A, THEN B) question, so no annulment logic applies.

Note: A separate, smaller Raiders transaction (a 3.5% stake / succession plan) was approved earlier on March 31, 2026 [fcc9e5], which falls outside the window — but the 25% Durban-group purchase approved May 19, 2026 is the relevant new in-window approval that satisfies the criteria.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-24. `3f5d8fa9-7140-5215-b8b9-b71c501c738d`

- Present date: `2026-05-13 21:45:28.311211`
- Source cutoff boundary: `2026-05-14` (encodes end of UTC day `2026-05-13`)
- Expected resolution: `2026-05-28 00:00:00`

**Question**

Will the SARB revise its 2026 headline inflation forecast upward in the May 28, 2026 MPC statement compared to the March 2026 statement?

**Resolution criteria**

This question resolves YES if the 2026 annual average headline inflation forecast stated in the SARB MPC statement released on May 28, 2026 (SAST, UTC+2) is strictly greater than 3.7% (the figure from the March 26, 2026 statement [[PDF] Repo rate held at 6.75%. No rate cuts expected in 2026 - Momentum](https://sls-fresco.momentum.co.za/files/documents/corporate/mim/updates-and-news/sarb-interest-rate-decision-26-march-2026.pdf)).

This question resolves NO if the 2026 annual average headline inflation forecast in the May 28, 2026 statement is equal to or less than 3.7%.

If the May 28, 2026 MPC statement does not provide a comparable 2026 annual average headline inflation forecast number, or if the statement is not published by July 1, 2026 (SAST), the question resolves N/A.

The resolution source is the official SARB Monetary Policy Committee statement published at: https://www.resbank.co.za/en/home/publications/publication-detail-pages/statements/monetary-policy-statements

For clarity: "headline inflation" refers to the overall Consumer Price Index (CPI) inflation rate as published by Statistics South Africa (https://www.statssa.gov.za/?page_id=735&id=1), encompassing all goods and services including food and energy.

**Pre-cutoff background**

The South African Reserve Bank (SARB) Monetary Policy Committee (MPC) periodically publishes inflation forecasts alongside its interest rate decisions. "Headline inflation" refers to the total consumer price inflation in an economy, including volatile components such as food and energy prices, as measured by Statistics South Africa's Consumer Price Index (see https://www.statssa.gov.za/?page_id=735&id=1).

In the March 26, 2026 MPC statement, the SARB revised its 2026 headline inflation forecast to 3.7% (up from 3.3% in the January 2026 statement) [[PDF] Repo rate held at 6.75%. No rate cuts expected in 2026 - Momentum](https://sls-fresco.momentum.co.za/files/documents/corporate/mim/updates-and-news/sarb-interest-rate-decision-26-march-2026.pdf). The revision was driven primarily by higher international oil prices and a weaker rand resulting from geopolitical tensions, particularly the conflict in the Middle East, which caused prices for commodities like oil, gas, and fertiliser to move sharply higher [Statement of the Monetary Policy Committee March 2026](https://www.resbank.co.za/en/home/publications/publication-detail-pages/statements/monetary-policy-statements/2026/march). The SARB projected headline inflation would peak at 4.3% in April 2026, with a Q2 2026 average of 4.0%, before gradually unwinding back to 3% late in 2027 [[PDF] Statement of the Monetary Policy Committee March 2026](https://www.resbank.co.za/content/dam/sarb/publications/statements/monetary-policy-statements/2026/march/mar-statement.pdf). The SARB noted that inflation risks remained tilted to the upside but expected inflation to stay within the 2%–4% tolerance band around the 3% target [[PDF] Repo rate held at 6.75%. No rate cuts expected in 2026 - Momentum](https://sls-fresco.momentum.co.za/files/documents/corporate/mim/updates-and-news/sarb-interest-rate-decision-26-march-2026.pdf).

Key upside risks flagged in the March 2026 statement include: the persistence of the Middle East conflict as a supply shock affecting energy and fertiliser prices, potential second-round effects on broader prices, and rand weakness linked to geopolitical uncertainty [Statement of the Monetary Policy Committee March 2026](https://www.resbank.co.za/en/home/publications/publication-detail-pages/statements/monetary-policy-statements/2026/march) [[PDF] Statement of the Monetary Policy Committee March 2026](https://www.resbank.co.za/content/dam/sarb/publications/statements/monetary-policy-statements/2026/march/mar-statement.pdf).

The next MPC statement is scheduled for May 28, 2026 (South Africa Standard Time, UTC+2). The statement will be published on the SARB website at https://www.resbank.co.za/en/home/publications/publication-detail-pages/statements/monetary-policy-statements.

**Exact later resolution packet**

The official SARB Monetary Policy Committee statement used for resolution is the May 2026 statement at https://www.resbank.co.za/en/home/publications/publication-detail-pages/statements/monetary-policy-statements/2026/may, published/released on 2026-05-28 [Statement of the Monetary Policy Committee May 2026](https://www.resbank.co.za/en/home/publications/publication-detail-pages/statements/monetary-policy-statements/2026/may). In that statement, SARB states: “Our forecast now has headline inflation averaging 4.4% this year and 3.7% next year” [Statement of the Monetary Policy Committee May 2026](https://www.resbank.co.za/en/home/publications/publication-detail-pages/statements/monetary-policy-statements/2026/may). Because the statement is dated May 28, 2026, “this year” refers to the 2026 annual average headline inflation forecast; the relevant value is therefore 4.4% [Statement of the Monetary Policy Committee May 2026](https://www.resbank.co.za/en/home/publications/publication-detail-pages/statements/monetary-policy-statements/2026/may). The resolution criterion asks whether this 2026 annual average headline inflation forecast is strictly greater than 3.7%. Since 4.4% > 3.7%, the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-25. `9972c169-284b-52ad-8df3-1458684b4d4a`

- Present date: `2026-05-02 23:46:08.582035`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will SAG-AFTRA and the AMPTP reach a tentative agreement on a new TV/Theatrical/Streaming contract before June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if SAG-AFTRA and the AMPTP publicly announce a **tentative agreement** on a new TV/Theatrical/Streaming contract on or after May 1, 2026 and before 11:59 PM UTC on June 1, 2026.

A **tentative agreement** is defined as a deal reached and publicly announced by the negotiating committees of both SAG-AFTRA and the AMPTP, pending ratification by the union membership. This is consistent with standard labor relations terminology (see [Cornell Law - Tentative Agreement](https://www.law.cornell.edu/wex/tentative_agreement)).

This question resolves **No** if no such announcement has been made by 11:59 PM UTC on June 1, 2026.

**Resolution source:** Official [SAG-AFTRA press releases](https://www.sagaftra.org/news) or credible entertainment trade publications, specifically [Variety](https://variety.com/), [Deadline](https://deadline.com/), or [The Hollywood Reporter](https://www.hollywoodreporter.com/).

Note: If a tentative agreement was announced before May 1, 2026 (i.e., during the April 27–30 negotiating window), this question resolves **No**, as only agreements announced on or after May 1, 2026 count.

**Pre-cutoff background**

SAG-AFTRA (the [Screen Actors Guild‐American Federation of Television and Radio Artists](https://www.sagaftra.org/)) and the [AMPTP](https://www.amptp.org/) (Alliance of Motion Picture and Television Producers) are negotiating a new TV/Theatrical/Streaming contract. The current contract expires June 30, 2026 [SAG-AFTRA to Resume Talks With Studios in April - Variety](https://variety.com/2026/film/news/sag-aftra-resume-amptp-talks-april-1236709773/).

Negotiations began on February 9, 2026, under a mutually agreed media blackout. Talks paused in March 2026 to allow the Writers Guild of America (WGA) to negotiate its own deal with the AMPTP. The WGA reached a tentative agreement in early April 2026 and ratified a four-year deal [SAG-AFTRA To Resume Talks With AMPTP - Deadline](https://deadline.com/2026/04/sag-aftra-amptp-resume-negotiations-ahead-of-dga-1236871347/).

SAG-AFTRA and the AMPTP resumed formal negotiations on April 27, 2026 [SAG-AFTRA To Resume Talks With AMPTP - Deadline](https://deadline.com/2026/04/sag-aftra-amptp-resume-negotiations-ahead-of-dga-1236871347/). The parties are aiming to reach a tentative agreement before the Directors Guild of America (DGA) begins its own negotiations on May 11, 2026 [SAG-AFTRA To Resume Talks With AMPTP - Deadline](https://deadline.com/2026/04/sag-aftra-amptp-resume-negotiations-ahead-of-dga-1236871347/). Key unresolved issues include AI protections for performers, pension funding, and streaming residuals [SAG-AFTRA to Resume Talks With Studios in April - Variety](https://variety.com/2026/film/news/sag-aftra-resume-amptp-talks-april-1236709773/) [SAG-AFTRA To Resume Talks With AMPTP - Deadline](https://deadline.com/2026/04/sag-aftra-amptp-resume-negotiations-ahead-of-dga-1236871347/). A four-year contract length is expected, following the WGA precedent [SAG-AFTRA To Resume Talks With AMPTP - Deadline](https://deadline.com/2026/04/sag-aftra-amptp-resume-negotiations-ahead-of-dga-1236871347/).

The fact that the parties are targeting a deal before May 11 suggests a resolution before June 1 is plausible but not certain — AI protections and pension funding details remain contentious [SAG-AFTRA To Resume Talks With AMPTP - Deadline](https://deadline.com/2026/04/sag-aftra-amptp-resume-negotiations-ahead-of-dga-1236871347/).

**Exact later resolution packet**

The question resolves YES.

SAG-AFTRA and the AMPTP publicly announced a tentative agreement on a successor to the 2023 SAG-AFTRA TV/Theatrical Contracts on Saturday, May 2, 2026 — squarely within the resolution window of "on or after May 1, 2026 and before 11:59 PM UTC on June 1, 2026."

Key evidence:
- Deadline ("It's Official! Studios & SAG-AFTRA Confirm New Deal," published May 2, 2026 at 4:15pm) states: "SAG-AFTRA and the AMPTP have reached a tentative agreement on terms for a successor contract to the 2023 SAG-AFTRA TV/Theatrical Contracts," and that "Talks resumed April 27 and concluded May 2." [88625a] (https://deadline.com/2026/05/studios-sag-aftra-confirm-new-deal-amptp-1236879173/)
- NBC Los Angeles (published May 2, 2026): "The Screen Actors Guild-American Federation of Television and Radio Artists reached a tentative agreement with the major studios on Saturday." [063f25] (https://www.nbclosangeles.com/news/local/sag-aftra-amptp-tentative-agreement/3884839/)

The agreement specifically concerns the TV/Theatrical/Streaming contract (successor to the 2023 SAG-AFTRA TV/Theatrical Contracts), as confirmed by SAG-AFTRA's official summary documents and joint statement.

Addressing the NO condition: The resolution criteria specify NO if a tentative agreement was announced before May 1, 2026 (during the April 27–30 negotiating window). The Deadline source explicitly states talks "concluded May 2" — i.e., NO agreement was reached on or before April 30. Talks resumed April 27 and ran until May 2, when the deal was reached. Therefore the disqualifying early-announcement condition was not triggered.

The announcement (May 2, 2026, mid-afternoon Pacific/evening on May 2 even in UTC terms) is well before the 11:59 PM UTC June 1, 2026 deadline. Resolution: YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-26. `555d2be7-6581-5345-9052-655b8c898df0`

- Present date: `2026-05-14 10:00:12.053424`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Supreme Court's opinion in Mullin v. Doe feature at least one dissenting opinion?

**Resolution criteria**

This question resolves as **Yes** if the Supreme Court of the United States issues its opinion in Mullin v. Doe (Docket No. 25-1083, consolidated with Trump v. Miot, No. 25-1084) on or after May 12, 2026, and by July 1, 2026 (11:59 PM Eastern Time), and that opinion includes at least one dissenting opinion.

A **dissenting opinion** is defined as a separate opinion filed by one or more Justices who disagree with the judgment (i.e., the outcome or disposition) reached by the majority or plurality of the Court. An opinion that concurs in the judgment but disagrees with the reasoning (a "concurrence in the judgment") does NOT count as a dissent. Only opinions explicitly labeled as "dissenting" or "dissent" in the official slip opinion qualify.

This question resolves as **No** if:
- The opinion is issued within the specified window and is unanimous (no Justice files a dissenting opinion), OR
- No opinion is released by the Supreme Court in this case by July 1, 2026 (11:59 PM Eastern Time).

**Resolution source:** The official slip opinion as published on the Supreme Court of the United States website at https://www.supremecourt.gov/opinions/slipopinion/25 (the opinions page for the October 2025 Term).

**Pre-cutoff background**

Mullin v. Doe (Docket No. 25-1083), consolidated with Trump v. Miot (Docket No. 25-1084), is a pending U.S. Supreme Court case concerning whether the Trump administration lawfully terminated Temporary Protected Status (TPS) for Haitian and Syrian nationals [Mullin v. Doe (25-1083) - SCOTUSblog](https://www.scotusblog.com/cases/noem-v-doe-3/) [Mullin v. Doe - Wikipedia](https://en.wikipedia.org/wiki/Mullin_v._Doe). The case raises questions about: (1) whether courts may review TPS termination decisions at all, and (2) whether the Secretary of Homeland Security followed required statutory consultation and notice procedures when ending TPS [Mullin v. Doe (25-1083) - SCOTUSblog](https://www.scotusblog.com/cases/noem-v-doe-3/).

In the lower courts, Judge Ana C. Reyes blocked the termination, ruling that the Secretary lacked authority to end TPS and that the stated justifications were flawed and racially motivated [Mullin v. Doe - Wikipedia](https://en.wikipedia.org/wiki/Mullin_v._Doe). The D.C. Circuit declined to pause the district court's ruling, and the Supreme Court granted the government's emergency appeal on March 16, 2026 [Mullin v. Doe - Wikipedia](https://en.wikipedia.org/wiki/Mullin_v._Doe). Oral arguments were held on April 29, 2026 [Mullin v. Doe (25-1083) - SCOTUSblog](https://www.scotusblog.com/cases/noem-v-doe-3/). As of May 12, 2026, the Court is deliberating and no opinion has been issued.

Immigration cases at the Supreme Court have frequently produced divided opinions, though some statutory interpretation questions can achieve broader consensus. The politically salient nature of TPS and the multiple legal questions involved suggest a meaningful probability of dissent, but unanimity is possible if the statutory text clearly resolves the dispute.

**Exact later resolution packet**

The Supreme Court issued its opinion in Mullin v. Doe (Docket No. 25-1083, consolidated with Trump v. Miot, No. 25-1084) on June 25, 2026 — squarely within the resolution window of May 12, 2026 through July 1, 2026 (11:59 PM ET).

The case was decided 6-3. Justice Alito announced the judgment of the Court and delivered the opinion of the Court (reversed and remanded), holding that Section 1254a(b)(5)(A) bars judicial review of non-constitutional TPS termination claims [201590].

Crucially, the official slip opinion at https://www.supremecourt.gov/opinions/25pdf/25-1083_f204.pdf includes a dissenting opinion. The syllabus explicitly states: "KAGAN, J., filed a dissenting opinion, in which SOTOMAYOR and JACKSON, JJ., joined." [ce9e12]. SCOTUSblog's case page corroborates that Justice Kagan filed a dissenting opinion joined by Justices Sotomayor and Jackson in this 6-3 decision [201590].

Because (a) the opinion was issued within the required window, and (b) it includes an opinion explicitly labeled "dissenting" — filed by Justices who disagreed with the judgment (a genuine dissent, not merely a concurrence in the judgment) — the question resolves YES.

Resolution source: The official October 2025 Term slip opinions page (https://www.supremecourt.gov/opinions/slipopinion/25), which lists the Mullin v. Doe opinion dated 06/25/2026, and the underlying slip opinion PDF (https://www.supremecourt.gov/opinions/25pdf/25-1083_f204.pdf) [ce9e12].

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-27. `a1ec0332-9728-5b5b-9120-43f5f7c13a43`

- Present date: `2026-05-01 17:32:01.956816`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the U.S. Department of Education publish a final rule implementing the Workforce Pell Grant program in the Federal Register by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if a document categorized as a "Rule" or "Final Rule" (not a "Proposed Rule" or "Notice") implementing the [Workforce Pell Grant program](https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant) is published in the Federal Register on or after April 30, 2026, and no later than June 1, 2026, 11:59 PM Eastern Time.

The "Workforce Pell Grant program" refers to the program established under Section 401A of the Higher Education Act of 1965, as added by Section 30201 of the One Big Beautiful Bill Act (H.R. 1), which extends Pell Grant eligibility to eligible short-term workforce training programs [https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant](https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant).

A "final rule" means a document published in the Federal Register under the "Rules and Regulations" section, with document type classified as "Rule" — as distinct from a "Proposed Rule" (which the NPRM already is) or a "Notice."

The resolution source is the [Federal Register](https://www.federalregister.gov/) and specifically the [Department of Education's documents page](https://www.federalregister.gov/agencies/education-department). The question resolves **No** if no such final rule appears by the deadline.

This resolution criterion excludes the already-published NPRM (March 9, 2026), which is a proposed rule, not a final rule.

**Pre-cutoff background**

The [One Big Beautiful Bill Act](https://www.congress.gov/bill/119th-congress/house-bill/1) (H.R. 1), signed into law on July 4, 2025, established the Workforce Pell Grant program, which expands Pell Grant eligibility to short-term workforce training programs (8–14 weeks, 150–599 clock hours) starting July 1, 2026 [https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant](https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant).

On March 9, 2026, the U.S. Department of Education published a [Notice of Proposed Rulemaking (NPRM)](https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant) titled "Accountability in Higher Education and Access Through Demand-Driven Workforce Pell: Pell Grant Exclusion Relating to Other Grant Aid; and Workforce Pell Grants" [https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant](https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant). The public comment period closed on April 8, 2026 [https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant](https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant).

To comply with the Administrative Procedure Act's requirement that final rules be published at least 30 days before their effective date, the Department must publish the final rule by approximately June 1, 2026, to meet the statutory July 1, 2026 implementation date [https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant](https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant). This creates an extremely compressed timeline of roughly 7–8 weeks from the close of comments to finalization—far faster than typical federal rulemaking. The program includes complex requirements such as state governor approval, value-added earnings metrics, and 70% completion/placement rate thresholds, all of which may generate substantial public comments requiring review [https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant](https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant).

As of April 30, 2026, the comment period has closed but no final rule has been published.

**Exact later resolution packet**

The question resolves YES. The U.S. Department of Education published a final rule implementing the Workforce Pell Grant program in the Federal Register on May 19, 2026, which falls within the resolution window (on or after April 30, 2026 and no later than June 1, 2026, 11:59 PM ET).

The document is at https://www.federalregister.gov/documents/2026/05/19/2026-10013/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant and is titled "Accountability in Higher Education and Access Through Demand-Driven Workforce Pell: Pell Grant Exclusion Relating to Other Grant Aid; and Workforce Pell Grants."

Key verification points [108186]:
- Document type: The Federal Register classifies this document explicitly as a "Rule" (i.e., a Final Rule in the Rules and Regulations section), NOT a "Proposed Rule" or "Notice."
- Publication date: 05/19/2026, which is within the required window of April 30, 2026 to June 1, 2026.
- Subject matter: It implements the Workforce Pell Grant program established by H.R. 1 (the One Big Beautiful Bill Act / referred to in the rule as the Working Families Tax Cuts Act), signed into law July 4, 2025. The rule amends § 600.10 to require Secretary approval of eligible workforce programs and implements the Workforce Pell Grant provisions, matching the program defined under Section 401A of the HEA.

This is distinct from and supersedes the NPRM (a Proposed Rule) published March 9, 2026 (document 2026-04520), which the resolution criteria explicitly excluded. The May 19, 2026 document is the FINAL rule, sharing the same title but being a separate, later-published "Rule"-type document.

Note: An initial exhaustive scan of the Department of Education's agency listing page failed to surface this final rule and incorrectly suggested NO, but a direct query of the actual Federal Register document confirmed its existence, document type ("Rule"), and publication date (05/19/2026) [108186]. Multiple secondary sources (ed.gov press release titled "U.S. Department of Education Issues Final Rule to Create New Workforce Pell Grant Program," and fsapartners.ed.gov "Final" designation dated 2026-05-19) corroborate that this is the final rule.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-28. `a906fb0c-c6ae-52c2-8dfc-77d59967c7c7`

- Present date: `2026-05-12 20:25:44.190961`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the South Korean National Assembly pass at least one of the ~50 livelihood-related bills targeted by the PPP's May 8, 2026 filibuster threat by July 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after May 10, 2026, and before July 1, 2026, 23:59 KST (UTC+9), the South Korean National Assembly holds a formal vote passing at least one of the approximately 50 livelihood-related bills that were scheduled for the May 8-9, 2026 plenary session but blocked by the PPP's filibuster threat. "Resolved" means any of the following: (a) a formal vote is held and the bill passes, (b) the PPP withdraws its filibuster notification for one or more of these bills and they proceed to a vote, or (c) a cloture motion (의사진행 발언 종결, requiring three-fifths of seated members under Article 106 of the National Assembly Act) is passed to end debate and the bill proceeds to a vote and passes.

This question resolves NO if none of these bills are passed by the deadline.

The resolution source is the official South Korean National Assembly legislative information system at https://bill.assembly.go.kr or equivalent official records at https://www.assembly.go.kr. Credible English-language reporting from Yonhap News Agency (https://en.yna.co.kr), The Korea Herald (https://www.koreaherald.com), or Reuters may also be used to confirm passage.

**Pre-cutoff background**

On May 8, 2026, the People Power Party (PPP) notified National Assembly Speaker Woo Won-shik of its intent to filibuster approximately 50 livelihood-related bills that were scheduled for a plenary session alongside a constitutional amendment bill [Speaker blasts PPP as Assembly suspends push for constitutional ...](https://www.koreaherald.com/article/10734028). These bills had previously been agreed upon by both ruling and opposition parties as non-contentious legislation. The Speaker, in response, suspended the entire plenary session—declining to table either the constitutional amendment or the 50 livelihood bills—and declared adjournment, stating that the PPP's filibuster strategy could theoretically block proceedings for over 50 days [Speaker blasts PPP as Assembly suspends push for constitutional ...](https://www.koreaherald.com/article/10734028).

As of May 11, 2026, none of these ~50 bills have been voted on. The constitutional amendment effort (the first in 39 years) has been declared dead, but the livelihood bills remain in limbo due to the legislative standoff.

Key context: South Korea's nationwide local elections are scheduled for June 3, 2026 [2026 South Korean local elections - Wikipedia](https://en.wikipedia.org/wiki/2026_South_Korean_local_elections). Analysts widely predict a landslide defeat for the PPP in these elections. The post-election political dynamics—including potential PPP leadership changes and shifting bargaining positions—are expected to heavily influence whether the legislative gridlock is resolved. The ruling Democratic Party holds a majority but the filibuster mechanism under the National Assembly Act allows unlimited debate unless terminated by a three-fifths supermajority vote (180 out of 300 seats).

The specific list of ~50 bills was defined by the National Assembly's scheduled plenary agenda for May 8-9, 2026. These bills cover areas such as semiconductor industry support, and other economic and social welfare matters previously agreed upon in bipartisan negotiations (e.g., the January 2026 agreement to process ~90 non-contentious bills).

**Exact later resolution packet**

Adjudicated: The May 8, 2026 Donga/Daum report itemizing the ~50 blocked non-contentious bills explicitly named both the '6·25전쟁 무공훈장 수여 등에 관한 법률 개정안' (expanding eligible family members) and the '재난 및 안전관리 기본법 개정안' (mandating local-government evacuation plans for vulnerable populations) among them (https://v.daum.net/v/20260508171152065). On June 18, 2026 — within the window (after May 10, before July 1) — the National Assembly's plenary passed 32 items including those two exact bills with identical descriptions (6·25 무공훈장법 and the 재난안전기본법 evacuation amendment), per goodkyung and the official bill record for bill 2211688 (의결일자 2026-06-18, 수정가결). Criterion (a) 'a formal vote is held and the bill passes' is therefore satisfied by at least one (in fact two) of the specific May-8-blocked bills. An earlier automated NO rested on Speaker Cho's 'remaining ~50/57' quote, but 나머지 ('remaining') denotes leftovers AFTER the 30 non-contentious bills processed that day, and the floor-referred pool had grown past 50; the named June-18 passages match the blocked set item-for-item.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-29. `22f09a7e-ea1c-5fba-83c5-171df87540de`

- Present date: `2026-05-14 06:12:37.553259`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the U.S. and Iran begin formal follow-up negotiations beyond the MOU framework between May 12, 2026 and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 and by 23:59 UTC on July 1, 2026, the United States and Iran commence formal follow-up negotiations beyond the MOU framework.

**Definition of "formal follow-up negotiations":** A scheduled, in-person meeting or series of meetings between official representatives of the U.S. government and the Iranian government (whether direct or mediated through a third party such as Pakistan), where at least one participant on each side holds the rank of deputy minister / deputy secretary or higher (or is a formally designated chief negotiator), and where the purpose is explicitly to negotiate the detailed agreement envisioned by the MOU framework. This must be confirmed by at least one of the following:

1. An official joint statement or communiqué issued by the governments of the United States and/or Iran announcing the commencement of such negotiations; OR
2. Credible reporting from at least two major international news agencies (e.g., Reuters: https://www.reuters.com/, Associated Press: https://apnews.com/, AFP, or similarly authoritative outlets such as The New York Times: https://www.nytimes.com/) explicitly describing the event as the start of formal follow-up negotiations under the MOU framework.

For the definition of "Memorandum of Understanding," see: https://en.wikipedia.org/wiki/Memorandum_of_understanding

For the definition of "diplomatic negotiation," see: https://en.wikipedia.org/wiki/Negotiation#Diplomatic_negotiation

If no such negotiations commence by 23:59 UTC on July 1, 2026, this question resolves **No**.

**Pre-cutoff background**

As of May 13, 2026, the United States and Iran are in the final stages of negotiating a one-page, 14-point Memorandum of Understanding (MOU) aimed at ending the ongoing war between the two countries [US, Iran closing in on one-page memo to end war, officials say - Axios](https://www.axios.com/2026/05/06/iran-us-deal-one-page-memo). According to Axios (https://www.axios.com/2026/05/06/iran-us-deal-one-page-memo), the MOU framework envisions a 30-day period of deeper, formal negotiations on a detailed agreement covering topics including the reopening of the Strait of Hormuz, limitations on Iran's nuclear program, and the lifting of U.S. sanctions [US, Iran closing in on one-page memo to end war, officials say - Axios](https://www.axios.com/2026/05/06/iran-us-deal-one-page-memo). Potential venues for these follow-up talks include Islamabad or Geneva [US, Iran closing in on one-page memo to end war, officials say - Axios](https://www.axios.com/2026/05/06/iran-us-deal-one-page-memo).

Previous diplomatic efforts have been turbulent. The Islamabad Talks in April 2026 (April 11–12) concluded without agreement, with officials from both sides stating significant gaps remained [2025–2026 Iran–United States negotiations - Wikipedia](https://en.wikipedia.org/wiki/2025%E2%80%932026_Iran%E2%80%93United_States_negotiations). A U.S. naval blockade of Iranian ports was initiated on April 13, 2026, following the collapse of those talks [2025–2026 Iran–United States negotiations - Wikipedia](https://en.wikipedia.org/wiki/2025%E2%80%932026_Iran%E2%80%93United_States_negotiations). Pakistani mediators have facilitated the current memo formulation process [2025–2026 Iran–United States negotiations - Wikipedia](https://en.wikipedia.org/wiki/2025%E2%80%932026_Iran%E2%80%93United_States_negotiations). As of May 11, 2026, no formal follow-up negotiations beyond the memo formulation process have begun [2025–2026 Iran–United States negotiations - Wikipedia](https://en.wikipedia.org/wiki/2025%E2%80%932026_Iran%E2%80%93United_States_negotiations).

For further context on the broader negotiation history, see the Wikipedia article on the 2025–2026 Iran–United States negotiations: https://en.wikipedia.org/wiki/2025%E2%80%932026_Iran%E2%80%93United_States_negotiations

**Exact later resolution packet**

RESOLUTION: YES (1)

The question asks whether the U.S. and Iran commenced formal follow-up negotiations beyond the MOU framework — i.e., a scheduled in-person meeting between officials of at least deputy-minister/secretary rank (or designated chief negotiators) explicitly to negotiate the detailed agreement envisioned by the MOU — on or after May 12, 2026 and by 23:59 UTC on July 1, 2026. This occurred.

TIMELINE / ANTECEDENT FACTS:
- The one-page, 14-point MOU (the "Islamabad Memorandum") was reached in mid-June and remotely signed by President Trump and Iranian President Pezeshkian around June 15–17, 2026, with the official text released June 17. The MOU set a 60-day period for negotiating a detailed final deal (nuclear program, sanctions relief, Strait of Hormuz, Lebanon) — establishing the MOU framework referenced by the question.

THE FOLLOW-UP NEGOTIATIONS (satisfying every checklist requirement):
- WHEN: The first round of follow-up talks began Sunday, June 21, 2026 and concluded Monday, June 22, 2026 — squarely within the May 12 – July 1, 2026 window [2db0bc, 495db7, e28f0a].
- WHERE / IN-PERSON: Held in-person at Bürgenstock, Switzerland (near Lake Lucerne) [e28f0a, 495db7, 2db0bc]. (The MOU itself had been signed remotely/virtually; the follow-up talks were a physical, in-person summit.)
- PARTICIPANTS' RANK: The U.S. delegation was led by Vice President JD Vance (with special envoy Steve Witkoff); the Iranian delegation was led by parliament speaker Mohammad Bagher Qalibaf and Foreign Minister Abbas Araghchi [495db7, 86c23e, 2db0bc]. All are far above the deputy-minister/deputy-secretary threshold and functioned as chief negotiators.
- PURPOSE (detailed agreement, not MOU formulation): The explicit purpose was to negotiate the detailed final deal envisioned by the already-signed MOU. The parties agreed a "roadmap" toward a permanent/final agreement within 60 days and created working groups/committees on nuclear issues, sanctions and dispute resolution [86c23e, 2db0bc, e28f0a, 3e519d]. The Soufan Center described these talks as marking "the start of a 60-day period of negotiations" toward a permanent U.S.–Iran peace [3e519d]. This is negotiation of the detailed agreement, not formulation of the MOU (which was already concluded).

MULTIPLE MAJOR INTERNATIONAL NEWS AGENCIES describing it as the start of formal follow-up negotiations under the MOU framework:
- BBC: "First round of US-Iran talks end with 'encouraging progress'"; talks began Sunday in Switzerland after the agreement committing to a final deal within 60 days [e28f0a].
- Reuters: reported the Bürgenstock, Switzerland talks (June 22) as the first talks under the nascent peace deal, agreeing a roadmap toward a permanent agreement within 60 days [2db0bc].
- Associated Press (AP): confirmed the June 21–22 Switzerland talks led by VP Vance and Iranian officials, aimed at the final deal under the interim agreement's 60-day negotiation period [495db7].
- CNBC: "U.S., Iran agree on roadmap for final deal"; negotiators created oversight, sanctions and nuclear working groups [86c23e].

Because at least two (indeed four) major international agencies (BBC, Reuters, AP, CNBC) explicitly describe the June 21–22, 2026 Switzerland summit as the start of the formal follow-up negotiations on the detailed deal under the MOU framework — an in-person meeting led on both sides by officials well above deputy-minister/secretary rank, occurring within the resolution window — the question resolves YES.

SOURCE URLS:
- Reuters: https://www.reuters.com/world/asia-pacific/us-iran-talks-go-into-day-2-after-trump-threats-hormuz-closure-2026-06-22/ [2db0bc]
- AP: https://apnews.com/article/united-states-iran-war-nuclear-negotiations-4bbde727c7095c4ad9da0285ca79f1e1 [495db7]
- BBC: https://www.bbc.com/news/articles/cwy0q41v1lzo [e28f0a]
- CNBC: https://www.cnbc.com/2026/06/22/us-iran-roadmap-final-deal-switzerland-talks-lebanon-deconfliction.html [86c23e]
- Soufan Center: https://thesoufancenter.org/intelbrief-2026-june-22/ [3e519d]
- Wikipedia (2025–2026 Iran–United States negotiations): https://en.wikipedia.org/wiki/2025%E2%80%932026_Iran%E2%80%93United_States_negotiations [780351]

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-30. `bc1ffedf-cfa2-5d5d-a8b8-ec9eddb09483`

- Present date: `2026-04-30 17:48:30.480582`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will at least one Shanghai-manufactured Tesla vehicle arrive at a Canadian port on or after April 30, 2026, and before June 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after April 30, 2026 (00:00 UTC) and before June 1, 2026 (23:59 UTC), at least one Tesla vehicle manufactured at Giga Shanghai arrives at a Canadian port or is delivered to a Canadian customer.

A vehicle is considered "Shanghai-manufactured" if its Vehicle Identification Number (VIN) begins with the World Manufacturer Identifier (WMI) "LRW", which designates Tesla vehicles produced at the Shanghai Gigafactory [China-built Tesla models available for immediate delivery in B.C.](https://driving.ca/auto-news/industry/tesla-models-china-export-north-america).

"Arrives at a Canadian port" means the physical arrival of a vehicle carrier ship carrying Tesla vehicles at any Canadian port (e.g., Vancouver, Montreal), OR "delivered to a Canadian customer" means the handover of a vehicle to a retail buyer in Canada.

Resolution will be based on any of the following sources confirming the above:
- Credible news reporting from Reuters (https://www.reuters.com), Bloomberg, CBC (https://www.cbc.ca), or Drive Tesla Canada (https://driveteslacanada.ca)
- Tesla official communications or investor materials
- Canadian vehicle listing data showing LRW-prefix VINs available for delivery
- Ship tracking data (e.g., MarineTraffic at https://www.marinetraffic.com) confirmed by credible reporting

If no credible source confirms such an arrival or delivery by June 1, 2026 (23:59 UTC), the question resolves NO.

**Pre-cutoff background**

In October 2024, Canada imposed a 100% tariff on Chinese-made electric vehicles, effectively halting Tesla's imports from its Giga Shanghai facility to Canada. On January 16, 2026, Canada and China reached a new trade agreement reducing these tariffs to 6.1% on most-favored-nation terms for up to 49,000 vehicles annually, with potential expansion to 70,000 over five years [Giga Shanghai Teslas first in line as Canada reopens door to ...](https://globalchinaev.com/post/giga-shanghai-teslas-first-in-line-as-canada-reopens-door-to-chinese-ev-imports). Tesla is widely considered the primary early beneficiary of this deal due to its existing Canadian retail infrastructure and the fact that Giga Shanghai was previously configured to produce Canada-spec vehicles (Reuters, January 19, 2026).

However, as of late February 2026, the specific quota allocation details—which dictate how import capacity is divided among manufacturers—had not yet been published, and no confirmed shipments of Shanghai-made Teslas to Canada had occurred [Giga Shanghai Teslas first in line as Canada reopens door to ...](https://globalchinaev.com/post/giga-shanghai-teslas-first-in-line-as-canada-reopens-door-to-chinese-ev-imports). The article noted that "the gap between policy and car lot can stretch months" [Giga Shanghai Teslas first in line as Canada reopens door to ...](https://globalchinaev.com/post/giga-shanghai-teslas-first-in-line-as-canada-reopens-door-to-chinese-ev-imports). Tesla previously shipped Shanghai-made Model Y (RWD) and Model 3 (LR AWD) vehicles to Canada in 2023, identifiable by VINs starting with "LRW" [China-built Tesla models available for immediate delivery in B.C.](https://driving.ca/auto-news/industry/tesla-models-china-export-north-america).

Key uncertainties include: whether quota allocation has been finalized, Tesla's corporate strategy regarding politically sensitive China-to-Canada shipments amid US-Canada trade tensions, and ocean shipping logistics timelines (typically 3–5 weeks from Shanghai to Vancouver).

**Exact later resolution packet**

The question resolves YES. The antecedent/condition — at least one Giga Shanghai-manufactured Tesla (VIN prefix "LRW") arriving at a Canadian port OR being delivered to a Canadian customer between April 30, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC) — was confirmed by multiple sources explicitly named in the resolution criteria.

DISTINGUISHING THE TWO TRIGGERS:
1) CUSTOMER DELIVERY / DELIVERY-CENTRE ARRIVAL: Drive Tesla Canada (one of the explicitly authorized resolution sources), in an article published May 30, 2026, reported that "Over the past week, large numbers of Shanghai-built Model 3 vehicles have been spotted arriving at Tesla delivery centres across Canada, including locations in Ontario and Atlantic Canada," and that nearly all of the 2,910 EVs imported from China under the new quota were Tesla Model 3 sedans produced at Giga Shanghai [dcac0a]. A separate EV-trade article (May 29, 2026) corroborated that trucks were unloading new Shanghai-built Model 3s at the Etobicoke (Toronto) delivery centre on May 28 and that the Dartmouth (Halifax) lot was full of Model 3 Premium RWD units on May 29, 2026 [c7515f].

2) PORT ARRIVAL: Bloomberg News (carried by Financial Post, also an explicitly authorized source), published May 29, 2026, reported that "In recent days, hundreds of Tesla Inc. cars made at the U.S. automaker's Shanghai factory have started to show up under the new low-tariff regime," and referenced a vehicle carrier (Glovis Treasure) moored outside the Port of Vancouver since Sunday May 24, 2026 [14e3da, b14c82].

VIN/MANUFACTURING ORIGIN: The resolution criteria define "Shanghai-manufactured" as a VIN beginning with WMI "LRW." Drive Tesla Canada itself established (and reaffirms) that Giga Shanghai vehicles carry the "LRW" VIN prefix [27140a]. The May 2026 vehicles are repeatedly and specifically identified as "Shanghai-built"/"produced at Giga Shanghai" Model 3 sedans imported under the new Canada-China quota [dcac0a, 14e3da], which by definition carry LRW VINs.

TIMING: All reported arrival/delivery events (May 24–30, 2026) fall squarely within the resolution window of April 30, 2026 to June 1, 2026.

Because both an authorized port-arrival source (Bloomberg/Financial Post) and an authorized customer-delivery source (Drive Tesla Canada) independently confirm Giga Shanghai Teslas reaching Canada within the window, the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-31. `9f25adad-9403-5b8f-866c-4cd0739b6173`

- Present date: `2026-05-03 11:42:50.172478`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the U.S. House of Representatives pass a standalone year-round E15 bill between May 2 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 2, 2026, and on or before June 1, 2026 (11:59 PM Eastern Time), the U.S. House of Representatives passes a standalone bill whose primary purpose is to authorize year-round nationwide sales of E15 gasoline (fuel containing up to 15% ethanol by volume).

**Definitions:**
- **"Standalone"** means a bill that is primarily and substantially focused on authorizing year-round E15 sales. The bill may contain minor related provisions (e.g., labeling requirements, implementation timelines, small refinery exemption adjustments) but must not be a large omnibus bill (such as an appropriations bill, farm bill, or reconciliation package) where E15 is merely one provision among many unrelated topics. Bills like H.R. 1346 or H.R. 4864 would qualify; a broader energy omnibus would not.
- **"Pass"** means the bill receives a simple majority of votes cast in a recorded vote (yeas exceeding nays) on final passage in the U.S. House of Representatives, consistent with Article I, Section 5 of the U.S. Constitution and House standing rules (https://rules.house.gov/about).

**Resolution source:** The official House Clerk roll call vote records at https://clerk.house.gov/Votes, or the bill's status page on Congress.gov (e.g., https://www.congress.gov/bill/119th-congress/house-bill/1346 for H.R. 1346, or https://www.congress.gov/bill/119th-congress/house-bill/4864 for H.R. 4864). The passage must occur on or after May 2, 2026, to distinguish from the April 30, 2026 Farm Bill vote, which did not contain E15 provisions.

If no such standalone E15 bill passes the House by 11:59 PM Eastern Time on June 1, 2026, the question resolves **No**.

**Pre-cutoff background**

On April 30, 2026, the U.S. House passed the Farm, Food, and National Security Act of 2026 by a vote of 224-200, but the bill did not include provisions for year-round E15 (gasoline blended with 15% ethanol) sales [House passes farm bill without pesticide clause; E15 vote set for ...](https://www.agri-pulse.com/articles/24613-house-passes-farm-bill-without-pesticide-clause-e15-vote-set-for-may-13). The E15 provision was stripped from the farm bill due to opposition from MAHA-aligned Republicans and oil refinery interests, and House leadership scheduled a standalone E15 floor vote for May 13, 2026 [House passes farm bill without pesticide clause; E15 vote set for ...](https://www.agri-pulse.com/articles/24613-house-passes-farm-bill-without-pesticide-clause-e15-vote-set-for-may-13).

Several bills addressing year-round E15 have been introduced in the 119th Congress, including H.R. 1346 (Nationwide Consumer and Fuel Retailer Choice Act of 2025) and H.R. 4864 (Ethanol for America Act of 2025). Year-round E15 has bipartisan support, particularly from corn-state representatives, and proponents argue it would lower gas prices and boost corn demand for ethanol by an estimated ~2.4 billion bushels per year. However, opposition from oil refiners, some environmental groups, and MAHA-aligned Republicans who object to ethanol mandates creates significant uncertainty about passage. The E15 waiver has been issued on a temporary/emergency basis each summer since 2022, and permanent legislative authorization remains contentious.

For context on House voting procedures, bills in the U.S. House pass by a simple majority of those present and voting (see U.S. Constitution, Article I, Section 5; House Rules Manual: https://rules.house.gov/about).

**Exact later resolution packet**

The question resolves YES.

The U.S. House of Representatives passed H.R. 1346, the "Nationwide Consumer and Fuel Retailer Choice Act of 2025," on Wednesday, May 13, 2026, by a recorded roll-call vote of 218-203 (Roll no. 164) [https://www.congress.gov/bill/119th-congress/house-bill/1346](https://www.congress.gov/bill/119th-congress/house-bill/1346)[After Farm Bill Setback, E15 Passes House as Standalone Legislation](https://www.dtnpf.com/agriculture/web/ag/news/business-inputs/article/2026/05/13/farm-bill-setback-e15-passes-house). This vote occurred within the required resolution window of May 2, 2026 through June 1, 2026, and is distinct from (and after) the April 30, 2026 Farm Bill vote, which did not contain E15 provisions.

Standalone criterion: The bill was passed as standalone legislation, separate from the Farm Bill, after E15 provisions had been stripped from the farm bill due to opposition from MAHA-aligned Republicans and oil refining interests [After Farm Bill Setback, E15 Passes House as Standalone Legislation](https://www.dtnpf.com/agriculture/web/ag/news/business-inputs/article/2026/05/13/farm-bill-setback-e15-passes-house). H.R. 1346 is explicitly named in the question as a qualifying example of a standalone bill ("Bills like H.R. 1346 or H.R. 4864 would qualify"). Its primary purpose is authorizing permanent year-round nationwide sales of E15 gasoline [https://www.congress.gov/bill/119th-congress/house-bill/1346](https://www.congress.gov/bill/119th-congress/house-bill/1346)[After Farm Bill Setback, E15 Passes House as Standalone Legislation](https://www.dtnpf.com/agriculture/web/ag/news/business-inputs/article/2026/05/13/farm-bill-setback-e15-passes-house). It is not an omnibus, appropriations, farm, or reconciliation bill.

Pass criterion: Final passage was by a recorded vote with yeas (218) exceeding nays (203), a simple majority of votes cast [https://www.congress.gov/bill/119th-congress/house-bill/1346](https://www.congress.gov/bill/119th-congress/house-bill/1346)[After Farm Bill Setback, E15 Passes House as Standalone Legislation](https://www.dtnpf.com/agriculture/web/ag/news/business-inputs/article/2026/05/13/farm-bill-setback-e15-passes-house). The Hill and Fischbach.house.gov corroborate the 218-203 tally (122 Republicans, 95 Democrats, and 1 independent in favor).

All resolution criteria are satisfied: standalone bill, primary purpose authorizing year-round nationwide E15, recorded majority vote on final passage, within the May 2–June 1, 2026 window.

Resolution source: Congress.gov H.R. 1346 status page (https://www.congress.gov/bill/119th-congress/house-bill/1346) confirming House passage 218-203 on 2026-05-13 [https://www.congress.gov/bill/119th-congress/house-bill/1346](https://www.congress.gov/bill/119th-congress/house-bill/1346).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-32. `50189e8b-1bfb-5abe-8309-ecfc8090e56b`

- Present date: `2026-05-14 09:40:20.829358`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Mexican government's IEPS subsidy percentage for Magna (regular) gasoline exceed 30% for any weekly period between May 12, 2026, and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, for any weekly period that begins on or after May 12, 2026, and ends on or before July 1, 2026 (all dates interpreted in UTC-6, Mexico City time), the Mexican government publishes an IEPS fiscal stimulus (estímulo fiscal) percentage for Magna gasoline (gasolina menor a 91 octanos) that is **strictly greater than 30%** of the full IEPS rate.

This question resolves **No** if the published IEPS subsidy percentage for Magna gasoline remains at or below 30% for all weekly periods within the specified window.

**Primary resolution source:** The official weekly *Acuerdo por el que se dan a conocer los porcentajes y los montos del estímulo fiscal* published in the *Diario Oficial de la Federación* (DOF) at https://www.dof.gob.mx/. These agreements are published weekly by the Secretaría de Hacienda y Crédito Público (SHCP).

**Secondary resolution sources:** If the DOF publication is unavailable or delayed, credible reporting from Reuters, Bloomberg, El Economista, or Global Trade Alert (https://globaltradealert.org/) confirming the subsidy percentage may be used.

The fuel categories covered by this question are:
- **Magna/Regular gasoline** (gasolina menor a 91 octanos) — this is the sole fuel type relevant for resolution.

**Definitions:**
- "Extension" of the IEPS subsidy means the subsidy continues to be applied for weekly periods beyond May 12, 2026 (i.e., the government does not discontinue the stimulus).
- "Expansion" of the IEPS subsidy means the published percentage for Magna gasoline exceeds 30%, representing a meaningful increase from the ~24% level observed in late March 2026.

**Pre-cutoff background**

Mexico uses the *Impuesto Especial sobre Producción y Servicios* (IEPS) — a special excise tax on fuel — as a policy lever to manage domestic fuel prices. The government adjusts IEPS tax credits on a weekly basis, effectively subsidizing gasoline and diesel prices when global oil prices rise.

As of early 2026, in response to the Iran war-driven oil price spike, Mexico has been actively increasing these subsidies. Key parameters as of May 12, 2026:

- **Magna (regular) gasoline (<91 octanes):** The statutory IEPS rate is approximately 6.70 pesos per liter [Mexico Restores Fuel Subsidies as War in Iran Drives Up Oil Prices](https://www.telesurenglish.net/mexico-restores-fuel-subsidies-as-war-in-iran-drives-up-oil-prices/). For the week of March 21–27, 2026, the IEPS subsidy for Magna was set at 24.08%, equivalent to roughly 1.61 pesos per liter [Mexico Restores Fuel Subsidies as War in Iran Drives Up Oil Prices](https://www.telesurenglish.net/mexico-restores-fuel-subsidies-as-war-in-iran-drives-up-oil-prices/). Subsequent weekly agreements have continued to adjust this figure, with Agreement 62/2026 (April 30, 2026) increasing tax credits for the week of May 2–8, 2026 [Higher tax credits under the fuel subsidy scheme (2 - 8 May 2026)](https://globaltradealert.org/state-act/97658-mexico-higher-tax-credits-under-the-fuel-subsidy-scheme-2-8-may-2026).
- **Premium gasoline (≥91 octanes):** The IEPS subsidy was 7.47%, approximately 0.42 pesos per liter, as of the week of March 21–27, 2026 [Mexico Restores Fuel Subsidies as War in Iran Drives Up Oil Prices](https://www.telesurenglish.net/mexico-restores-fuel-subsidies-as-war-in-iran-drives-up-oil-prices/).
- **Diesel:** The IEPS subsidy was 61.8%, approximately 4.5 pesos per liter, as of the week of March 21–27, 2026 [Mexico Restores Fuel Subsidies as War in Iran Drives Up Oil Prices](https://www.telesurenglish.net/mexico-restores-fuel-subsidies-as-war-in-iran-drives-up-oil-prices/). The statutory IEPS rate for diesel is 7.3634 pesos per liter.

In parallel, the government maintains a voluntary agreement with approximately 96% of gas stations to cap the retail price of Magna gasoline at below 24 pesos per liter. This agreement was renewed on March 11, 2026, for six months (through approximately September 2026) [Mexico extends its gas price cap as the Iran war spikes oil prices](https://mexiconewsdaily.com/business/mexico-extends-its-gas-price-cap-as-the-iran-war-spikes-oil-prices/). A separate temporary agreement for diesel price reductions was announced on March 31, 2026 [Subject: Gas station owners and the Mexican government renew ...](https://www.pemex.com/en/press_room/press_releases/Paginas/2026-34_national.aspx).

The weekly IEPS subsidy percentages are published in the *Diario Oficial de la Federación* (DOF), Mexico's official government gazette, typically every Friday for the following week. The subsidy for Magna has been trending upward as oil prices remain elevated due to the Iran conflict. This question focuses on whether the Magna subsidy will cross the 30% threshold — a significant escalation from the 24.08% level observed in late March 2026.

**Exact later resolution packet**

RESOLUTION: YES (1).

The question resolves YES if, for ANY weekly period beginning on/after May 12, 2026 and ending on/before July 1, 2026, the Mexican government publishes an IEPS "estímulo fiscal" percentage for Magna (gasolina menor a 91 octanos) strictly greater than 30% of the full IEPS rate. Multiple independent sources confirm this threshold was cleared in several qualifying weeks.

KEY QUALIFYING WEEKS (all begin on/after May 12 and end on/before July 1):

1. Week of MAY 23–29, 2026: The DOF agreement (published May 22, 2026, DOF nota 5788359 confirms the period) set the Porcentaje de Estímulo for "Gasolina menor a 91 octanos" at 51.26% — with Premium at 43.56% and Diésel at 64.31% [ee8d55]. 51.26% > 30%. This alone resolves YES. (Corroborated by numerous outlets reporting the 23–29 May stimulus rose for a third consecutive week.)

2. Week of MAY 16–22, 2026: Consumers paid an IEPS cuota of only $3.3861/L for Magna against the full statutory rate of $6.7001/L, implying a stimulus of (6.7001−3.3861)/6.7001 ≈ 49.5% [1d5b61]. Well above 30%.

3. Week of JUNE 13–19, 2026: The DOF vespertina edition of June 12, 2026 set the Magna stimulus at 32.45% [0fc8bd]. Above 30%.

TREND CONTEXT: For the earlier week of May 2–8, 2026 (before the window), the Magna stimulus was already 38.08% [086707]. So the subsidy was already above 30% and stayed there through the qualifying weeks, in response to the elevated oil prices described in the question.

Therefore the answer is unambiguously YES — the Magna IEPS stimulus percentage exceeded 30% for multiple weekly periods within May 12 – July 1, 2026 (Mexico City time, UTC-6).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-33. `b221e989-edf3-5fa2-b5c4-8475fb734649`

- Present date: `2026-04-29 23:20:26.976777`
- Source cutoff boundary: `2026-04-30` (encodes end of UTC day `2026-04-29`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Kash Patel still be serving as FBI Director by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if Kash Patel is serving as FBI Director at 11:59 PM UTC on June 1, 2026. It resolves **No** if he is no longer serving in that role at that time.

**Primary resolution source:** The official FBI leadership page at https://www.fbi.gov/about/leadership-and-structure. If this page lists Kash Patel as "Director" on June 1, 2026 (checked at or after 11:59 PM UTC), the question resolves Yes.

**Secondary sources:** If the FBI website is unavailable or ambiguous, resolution may rely on official announcements from the White House or Department of Justice, or credible reporting from major outlets (e.g., Reuters, AP, NYT).

**Key definitions:**
- "FBI Director" refers to the principal head of the Federal Bureau of Investigation as defined under [28 U.S.C. § 532](https://www.law.cornell.edu/uscode/text/28/532) and described at https://en.wikipedia.org/wiki/Director_of_the_Federal_Bureau_of_Investigation. This includes both Senate-confirmed Directors and recess-appointed Directors, but does **not** include individuals serving in an "Acting Director" capacity. If Patel is replaced by an Acting Director, the question resolves No.
- "Serving as FBI Director" means holding the position in an official capacity. If Patel announces his resignation but his last day in office is on or after June 1, 2026 (11:59 PM UTC), the question resolves Yes. If his last day in office is before June 1, 2026 (11:59 PM UTC), it resolves No. The relevant date is the last day in office, not the date of any resignation announcement.

**Temporal scope:** Only events occurring on or after the question's open date and on or before June 1, 2026 (11:59 PM UTC) are relevant to resolution. If Patel was already removed before the question's open date, the question resolves No.

**Pre-cutoff background**

As of April 28, 2026, Kash Patel serves as the Director of the Federal Bureau of Investigation (FBI), a position he has held since his Senate confirmation in February 2025 [https://www.fbi.gov/about/leadership-and-structure](https://www.fbi.gov/about/leadership-and-structure). His tenure has recently been marked by significant controversy:

- **The Atlantic's allegations:** In April 2026, The Atlantic published a report alleging excessive drinking and unexplained absences by Patel during his time as FBI Director.
- **$250 million defamation lawsuit:** Patel filed a $250 million defamation lawsuit against The Atlantic in response to these allegations. On April 22, 2026, Patel and Acting Attorney General Todd Blanche publicly addressed the allegations.
- **Congressional scrutiny:** Democrats on the House Judiciary Committee have requested information from Patel and called for an alcohol-use screening.
- **White House statement of support:** On April 24, 2026, the White House stated that President Trump still has confidence in Patel (https://www.usatoday.com/story/news/politics/2026/04/24/trump-kash-patel-fbi-director-the-atlantic/89775681007/).
- **Reports of possible firing:** Multiple media outlets, including The Times (UK), have reported that Patel's firing may be "a matter of time," citing internal administration frustration with unflattering headlines.

As of April 28, 2026, Patel remains listed as FBI Director on the official FBI leadership page [https://www.fbi.gov/about/leadership-and-structure](https://www.fbi.gov/about/leadership-and-structure) and appeared at a DOJ press conference on April 27, 2026, regarding federal charges related to the White House Correspondents' Dinner shooting.

**Exact later resolution packet**

The question resolves YES because Kash Patel was still serving as FBI Director (not Acting Director) at 11:59 PM UTC on June 1, 2026.

Evidence:
- The primary resolution source specified in the question, the official FBI leadership page (https://www.fbi.gov/about/leadership-and-structure), lists Kash Patel under the heading "Director" with a portrait captioned "Portrait of FBI Director Kash Patel" — confirming Director (not Acting Director) status [https://www.fbi.gov/about/leadership-and-structure](https://www.fbi.gov/about/leadership-and-structure).
- The official FBI "Directors, Then and Now" history page (https://www.fbi.gov/history/directors) lists Kash Patel as the "Current Director" with tenure "February 21, 2025 – Present," confirming he had not left office [Directors, Then and Now | Federal Bureau of Investigation - FBI](https://www.fbi.gov/history/directors).
- Independent prediction-market tracking (Polymarket "Kash Patel out by...?") showed as of June 2, 2026 that "No confirmed removal or resignation has occurred," and markets for his departure had not resolved YES, corroborating that he remained in office through June 1, 2026 [Kash Patel out by...? Predictions & Odds 2026 - Polymarket](https://polymarket.com/event/kash-patel-out-by).
- Corroborating reporting through late May 2026: Patel delivered a Police Week message on/around May 11, 2026 as "the ninth director of the FBI" and testified before a Senate Appropriations Subcommittee on May 12, 2026 as FBI Director. While there was extensive speculation in April–May 2026 about a potential firing (The Atlantic allegations, defamation suit, "Trump poised to fire" reports), the White House repeatedly denied ouster reports and no actual removal or resignation took effect on or before June 1, 2026.

On the checklist items: (1) Status checked is "Director" not "Acting Director" — the FBI page explicitly shows him as Director [https://www.fbi.gov/about/leadership-and-structure](https://www.fbi.gov/about/leadership-and-structure). (2) No resignation took effect before the deadline; he was still listed as "Present" [Directors, Then and Now | Federal Bureau of Investigation - FBI](https://www.fbi.gov/history/directors). (3) He was NOT removed prior to April 29, 2026 (the question's open date) — he was still listed as Director and appeared at the April 27, 2026 DOJ press conference, so the "already removed" NO condition was not triggered.

All conditions for a YES resolution are met: Patel held the position of FBI Director in an official, non-acting capacity at the resolution time.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-34. `c4687ce5-2ff1-5788-8bfd-2289d7669ed4`

- Present date: `2026-05-01 18:25:52.979774`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the Carolina Hurricanes advance past the Philadelphia Flyers in the 2026 Stanley Cup Playoffs second round?

**Resolution criteria**

This question resolves YES if the Carolina Hurricanes win their 2026 Stanley Cup Playoffs second-round best-of-seven series against the Philadelphia Flyers (i.e., win four games in the series), with the series-clinching win occurring on or after April 30, 2026, and no later than 11:59 PM ET on June 1, 2026.

This question resolves NO if the Philadelphia Flyers win four games in the series and advance, or if the series has not been completed by 11:59 PM ET on June 1, 2026.

"Advancing" means winning the best-of-seven series by being the first team to win four games, as reflected in the official NHL playoff bracket at https://www.nhl.com/playoffs/2026/bracket.

Resolution source: The official NHL playoff bracket at https://www.nhl.com/playoffs/2026/bracket.

**Pre-cutoff background**

The 2026 Stanley Cup Playoffs are underway in the Eastern Conference. In the first round, the Carolina Hurricanes, the top seed in the East, swept the Ottawa Senators 4-0 (Game 1: 2-0, Game 2: 3-2 2OT, Game 3: 2-1, Game 4: 4-2). The Philadelphia Flyers, making their first playoff appearance since 2020, defeated the Pittsburgh Penguins 4-2 in their first-round series, clinching with a 1-0 overtime win in Game 6.

Carolina went 3-0-1 against Philadelphia during the regular season, with every game decided after regulation. The Hurricanes finished the regular season 52-22-7 as the Eastern Conference's top seed. The Flyers finished 42-27-12 as the third seed in the Metropolitan Division.

As of April 30, 2026, the second-round series between Carolina and Philadelphia has not yet begun. The second round is scheduled to start around May 6, 2026, with the Conference Finals beginning around May 22 and the Stanley Cup Final on June 3.

**Exact later resolution packet**

The Carolina Hurricanes swept the Philadelphia Flyers 4-0 in the 2026 Stanley Cup Playoffs Eastern Conference Second Round, becoming the first team to reach four wins. The series-clinching Game 4 win occurred on Saturday, May 9, 2026, a 3-2 overtime victory at Xfinity Mobile Arena, with Jackson Blake scoring the OT winner [37d4eb].

Game-by-game results from the official NHL playoff series page (https://www.nhl.com/schedule/playoff-series/2026/series-j/flyers-vs-hurricanes):
- Game 1: Carolina 3, Philadelphia 0
- Game 2: Carolina 3, Philadelphia 2 (OT)
- Game 3: Carolina 4, Philadelphia 1
- Game 4: Carolina 3, Philadelphia 2 (OT) — series-clinching win [37d4eb]

This was corroborated by multiple news sources (NHL.com recap "Blake scores in OT, Hurricanes complete sweep of Flyers in East 2nd Round" dated May 9, 2026; Sportsnet "Hurricanes make NHL history with sweep of Flyers in Round 2"; AP News; Spectrum News).

Resolution analysis:
- The Hurricanes won four games (the series 4-0), so they advanced. The question's YES condition is met.
- The series-clinching win (May 9, 2026) occurred on or after April 30, 2026: YES.
- The clinching win occurred no later than 11:59 PM ET on June 1, 2026 (it was on May 9, 2026, well before the deadline): YES.
- The series was completed by the deadline; the Hurricanes reached 4 wins first.

Therefore the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-35. `59be9f45-abb0-5270-8c80-566385621c0c`

- Present date: `2026-05-01 11:59:55.801735`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-05-31 00:00:00`

**Question**

Will the US naval blockade on Iranian ports still be in effect on May 31, 2026?

**Resolution criteria**

This question resolves **Yes** if, as of 11:59 PM UTC on May 31, 2026, the U.S. naval blockade on Iranian ports — as announced by CENTCOM on April 12, 2026 ([CENTCOM press release](https://www.centcom.mil/MEDIA/PRESS-RELEASES/Press-Release-View/Article/4457255/us-to-blockade-ships-entering-or-exiting-iranian-ports/)) — remains in effect. The question resolves **No** if the blockade has been officially lifted, terminated, or suspended by that time.

**Definition of "naval blockade":** For this question, a naval blockade means the physical military interdiction by U.S. naval forces of vessels entering or departing Iranian ports and coastal areas on the Persian Gulf and Gulf of Oman, as defined under the [San Remo Manual on International Law Applicable to Armed Conflicts at Sea (1994), Articles 93–108](https://ihl-databases.icrc.org/en/ihl-treaties/san-remo-manual-1994/article-93-108). This is distinct from economic sanctions or diplomatic restrictions; only a physical naval operation involving the interception or redirection of vessels qualifies.

**Geographic scope:** The blockade covers all Iranian ports on the Persian Gulf and the Gulf of Oman, encompassing the entirety of the Iranian coastline, as specified in the CENTCOM announcement [U.S. to Blockade Ships Entering or Exiting Iranian Ports - centcom](https://www.centcom.mil/MEDIA/PRESS-RELEASES/Press-Release-View/Article/4457255/us-to-blockade-ships-entering-or-exiting-iranian-ports/).

**How "in effect" is determined:** The blockade is considered "in effect" unless the U.S. government has issued an official statement declaring its termination or suspension. Specifically:
- An official statement from the White House ([whitehouse.gov/briefing-room](https://www.whitehouse.gov/briefing-room/)), the U.S. Department of Defense ([defense.gov](https://www.defense.gov/)), or CENTCOM ([centcom.mil/MEDIA/PRESS-RELEASES](https://www.centcom.mil/MEDIA/PRESS-RELEASES/)) explicitly announcing the end or suspension of the blockade would cause resolution as **No**.
- If no such official statement exists, credible reporting from Reuters ([reuters.com](https://www.reuters.com/)), the Associated Press ([apnews.com](https://apnews.com/)), or Bloomberg ([bloomberg.com](https://www.bloomberg.com/)) confirming the blockade's status will be used.
- A mere reduction in enforcement intensity or temporary operational pauses that are not officially described as a lifting or suspension of the blockade do **not** count as the blockade being "not in effect."
- Standard economic sanctions alone, without physical naval interdiction, do **not** constitute a blockade for the purposes of this question.

**Pre-cutoff background**

On April 13, 2026, the United States imposed a naval blockade on Iran, enforced by U.S. Central Command (CENTCOM), following the failure of the Islamabad Talks (April 11–12, 2026) to resolve the 2026 Iran war [https://en.wikipedia.org/wiki/2026_United_States_naval_blockade_of_Iran](https://en.wikipedia.org/wiki/2026_United_States_naval_blockade_of_Iran). The blockade covers the entirety of the Iranian coastline, including all Iranian ports on the Persian Gulf and the Gulf of Oman [U.S. to Blockade Ships Entering or Exiting Iranian Ports - centcom](https://www.centcom.mil/MEDIA/PRESS-RELEASES/Press-Release-View/Article/4457255/us-to-blockade-ships-entering-or-exiting-iranian-ports/). CENTCOM announced the blockade would be "enforced impartially against vessels of all nations entering or departing Iranian ports and coastal areas" while not impeding freedom of navigation for vessels transiting the Strait of Hormuz to and from non-Iranian ports [U.S. to Blockade Ships Entering or Exiting Iranian Ports - centcom](https://www.centcom.mil/MEDIA/PRESS-RELEASES/Press-Release-View/Article/4457255/us-to-blockade-ships-entering-or-exiting-iranian-ports/). As of April 22, 2026, 29 ships had been intercepted [https://en.wikipedia.org/wiki/2026_United_States_naval_blockade_of_Iran](https://en.wikipedia.org/wiki/2026_United_States_naval_blockade_of_Iran), and by April 23, at least 33 ships had been redirected (CNN reporting).

The IEA's April 2026 Oil Market Report identified the blockade as a critical factor constraining global oil supply, noting that the resumption of regular shipping flows through the Strait of Hormuz is the "single most important variable in easing the pressure on energy supplies" [https://www.iea.org/reports/oil-market-report-april-2026](https://www.iea.org/reports/oil-market-report-april-2026). Iran's oil production capacity of approximately 3–4 million barrels per day is effectively offline due to the blockade.

As of April 30, 2026, the blockade remains in full effect. Bloomberg reported on April 30, 2026 that the "US Signals No Letup of Naval Blockade." President Trump has stated the blockade will remain until a nuclear deal is reached, and Iran insists the blockade be lifted as a precondition for cease-fire talks, creating a diplomatic impasse. However, the situation remains fluid, with ongoing military and diplomatic developments that could alter the blockade's status.

A naval blockade, as defined under international law, is "a belligerent operation to prevent vessels and/or aircraft of all nations, enemy as well as neutral, from entering or exiting specified ports, airfields, or coastal areas belonging to, occupied by, or under the control of an enemy nation" (see the [San Remo Manual on International Law Applicable to Armed Conflicts at Sea, 1994](https://ihl-databases.icrc.org/en/ihl-treaties/san-remo-manual-1994/article-93-108) and the [ICRC Glossary](https://casebook.icrc.org/a_to_z/glossary/blockade)). This is distinct from economic sanctions, which restrict trade through legal and financial mechanisms rather than physical military interdiction of vessels.

**Exact later resolution packet**

YES. The question’s own criteria say the April 2026 U.S. naval blockade is considered “in effect” unless the U.S. government officially declares its termination or suspension, and that standard economic sanctions alone are not the relevant issue; the relevant operation is physical naval interdiction of vessels entering or departing Iranian ports. The official CENTCOM announcement page confirms that CENTCOM began implementing a blockade of maritime traffic entering and exiting Iranian ports on April 13, 2026, and that it would be enforced against vessels of all nations entering or departing Iranian ports and coastal areas [https://www.centcom.mil/MEDIA/PRESS-RELEASES/Press-Release-View/Article/4457255/us-to-blockade-ships-entering-or-exiting-iranian-ports/](https://www.centcom.mil/MEDIA/PRESS-RELEASES/Press-Release-View/Article/4457255/us-to-blockade-ships-entering-or-exiting-iranian-ports/). I found no official White House termination/suspension notice by the deadline: the White House briefing-room listing queried after the resolution window showed no relevant statement dated on or before May 31, 2026 [https://www.whitehouse.gov/briefing-room/](https://www.whitehouse.gov/briefing-room/). I also found no official CENTCOM termination/suspension notice by the deadline: the CENTCOM press-release archive contained no such statement through May 31, and instead included a May 23, 2026 release, “U.S. Blockade of Iran Reaches Milestone of Redirecting 100 Ships,” confirming continued blockade operations [https://www.centcom.mil/MEDIA/PRESS-RELEASES/](https://www.centcom.mil/MEDIA/PRESS-RELEASES/). The only Reuters item I found near the deadline described a May 27 draft/unofficial framework under which shipping might reopen and the blockade might end, but it was not finalized; Reuters also reported the White House rejected the Tehran TV report and Trump said the U.S. was not yet satisfied on an Iran deal [Iran state TV says draft deal with US would reopen Hormuz shipping ...](https://www.reuters.com/world/middle-east/iran-says-draft-us-deal-would-reopen-hormuz-shipping-end-naval-blockade-2026-05-27/). Because no official termination or suspension existed by 11:59 PM UTC on May 31, 2026, and the evidence concerns the physical naval interdiction/blockade rather than ordinary economic sanctions, the blockade remained in effect under the stated criteria.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-36. `d9973659-b764-5704-90ae-24d551e89a33`

- Present date: `2026-05-03 03:24:23.638658`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the UN Security Council hold an emergency or unscheduled meeting on the Iran/Gulf crisis between May 1 and May 31, 2026?

**Resolution criteria**

This question resolves as **Yes** if, between 00:00 UTC on May 1, 2026 and 23:59 UTC on May 31, 2026, the UN Security Council holds at least one formal meeting (public or private) on the Iran/Gulf crisis that was NOT included in the Council's original monthly programme of work for May 2026. The meeting must occur on or after May 1, 2026.

The meeting must appear in the official UN Security Council meeting records, accessible at:
- **Primary source**: UN Security Council Meetings & Outcomes Tables (https://research.un.org/en/docs/sc/quick/meetings)
- **Supporting source**: UN Journal – Security Council Official Meetings (https://journal.un.org/en/new-york/meeting/officials/)
- **Programme of work**: https://main.un.org/securitycouncil/en/content/programme-work

To qualify, the meeting record or associated press release (available at https://press.un.org/en/content/security-council/meetings-coverage) must indicate that:
1. The meeting's agenda item explicitly addresses the situation involving Iran and/or the Gulf states (e.g., "The situation in the Middle East" as it pertains to the Iran/Gulf crisis, or "Non-proliferation" regarding Iran), AND
2. The meeting was not part of the regularly scheduled programme of work published at the beginning of May 2026.

If no such unscheduled meeting is recorded in these sources by 23:59 UTC on May 31, 2026, the question resolves as **No**.

**Pre-cutoff background**

The UN Security Council has been actively engaged on the Iran and Gulf crisis throughout early 2026. In March 2026, the Council adopted Resolution 2817, which condemned Iran's attacks against Gulf Cooperation Council (GCC) states (Bahrain, Kuwait, Oman, Qatar, Saudi Arabia, and the UAE) and Jordan [UN Security Council Meetings & Outcomes Tables: 2026 (S/RES/2812](https://research.un.org/en/docs/sc/quick/meetings). The resolution demanded that Iran cease all attacks and halt threats to close strategic waterways, including the Strait of Hormuz. In April 2026, the Council held a high-level briefing on UN-GCC cooperation, and the GCC Secretary-General called on the UNSC to guarantee uninterrupted navigation through Gulf waterways.

As of May 2, 2026, the Security Council's published programme of work for May includes several scheduled agenda items, but the Iran/Gulf situation remains fluid, with ceasefire dynamics and Strait of Hormuz tensions creating the possibility that an unscheduled or emergency meeting could be convened at any time [Programme of Work | Security Council - the United Nations](https://main.un.org/securitycouncil/en/content/programme-work).

The UN Security Council does not formally use the term "emergency session" in its own Provisional Rules of Procedure (S/96/Rev.7). However, the Council can be convened urgently at any time. Under Rule 1, meetings are held "at the call of the President at any time he deems necessary." Under Rule 2, "the President shall call a meeting of the Security Council at the request of any member." Under Rule 3, the President must call a meeting when a dispute or situation is brought to the Council's attention under Articles 35 or 99 of the UN Charter [Provisional Rules of Procedure (S/96/Rev.7)](https://main.un.org/securitycouncil/en/content/rop/chapter-1). For the purposes of this question, an "emergency or unscheduled meeting" is defined below.

Key definitions:
- **Emergency or unscheduled meeting**: A formal public or private meeting of the UN Security Council on the Iran/Gulf crisis that is NOT listed in the Council's monthly programme of work as published at the start of May 2026 (see: https://main.un.org/securitycouncil/en/content/programme-work). This includes meetings requested urgently by any Council member under Rule 2 of the Provisional Rules of Procedure (https://main.un.org/securitycouncil/en/content/rop/chapter-1).
- **Iran/Gulf crisis**: Any situation involving armed conflict, military escalation, threats to navigation in the Strait of Hormuz, or attacks by or against Iran involving the Gulf states (Bahrain, Kuwait, Oman, Qatar, Saudi Arabia, UAE) and/or Jordan, as addressed in UNSC Resolution 2817 (2026) (https://en.wikipedia.org/wiki/United_Nations_Security_Council_Resolution_2817). The meeting agenda must explicitly reference Iran, the Gulf, or the broader Middle East crisis as it pertains to the 2026 Iran war.
- **Provisional Rules of Procedure**: The Security Council's procedural rules, available at https://main.un.org/securitycouncil/en/content/provisional-rules-procedure-0. Rules 1-3 govern the convening of meetings [Provisional Rules of Procedure (S/96/Rev.7)](https://main.un.org/securitycouncil/en/content/rop/chapter-1).

**Exact later resolution packet**

Adjudicated: On 19 May 2026 the UN Security Council held a formal meeting (its 10153rd meeting, press release SC/16362) at which IAEA Director-General Grossi briefed and delegations made statements on the Iranian drone strike on the Barakah Nuclear Power Plant in the UAE, explicitly invoking the Iran/Gulf crisis, the Strait of Hormuz, and Resolution 2817 (2026). A meeting/press-release number and a public IAEA briefing identify it as a formal meeting, not closed consultations; the original May 2026 programme of work scheduled no Iran/Gulf/Barakah meeting (only a generic 'follow closely' note), so it was unscheduled. An initial automated pass erred by asserting no formal meeting occurred, missing SC/16362.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-37. `ac8fbd78-aafd-573c-bddb-0b5f251d9fb4`

- Present date: `2026-05-16 20:47:01.321918`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Junts per Catalunya vote in favor of any Spanish government-sponsored decreto-ley in the Congress of Deputies between May 12, 2026 and July 1, 2026?

**Resolution criteria**

This question resolves YES if, between May 12, 2026, 00:00 UTC and July 1, 2026, 23:59 UTC, Junts per Catalunya's parliamentary group in the Congress of Deputies casts a majority of its votes in favor of ratifying at least one gobierno-sponsored decreto-ley (Royal Decree-Law) in a plenary vote. Abstentions do not count as votes in favor.

This question resolves NO if either: (a) no gobierno-sponsored decreto-ley is put to a ratification vote in the Congress during this period, or (b) Junts votes against or abstains on every such decreto-ley voted on during this period.

A "gobierno-sponsored decreto-ley" is a Royal Decree-Law (Real Decreto-ley) approved by the Council of Ministers and submitted to the Congress for ratification under Article 86 of the Spanish Constitution.

Resolution source: Official voting records of the Congress of Deputies, available at https://www.congreso.es/en/votaciones, or credible reporting from major Spanish news outlets such as El País (https://elpais.com), La Vanguardia (https://www.lavanguardia.com), or agencies such as EFE or Reuters.

**Pre-cutoff background**

Junts per Catalunya, a Catalan pro-independence party holding 7 seats in the Spanish Congress of Deputies, struck a parliamentary support deal with PSOE to enable Pedro Sánchez's investiture in November 2023. In October 2025, Junts' executive unanimously endorsed breaking this investiture agreement, and the party's membership ratified the decision with 87% support [Junts withdraws support for PSOE government](https://www.gbc.gi/news/junts-withdraws-support-for-psoe-government). The party cited PSOE's failure to uphold commitments on the amnesty law and other Catalan-related issues.

However, despite this declared rupture, Junts has continued to selectively support certain government measures it deems favorable to Catalan interests. As of March 26, 2026, Junts had voted in favor of or abstained on at least five government initiatives since the declared break, including the Law on Sustainable Mobility, a vote on nuclear power plants, and aid for the self-employed [Junts congela la ruptura "absoluta" con Sánchez](https://www.larazon.es/espana/junts-congela-ruptura-absoluta-sanchez-acumula-cinco-apoyos-decision-puigdemont_2026032669c503b583aca52e0e39e47e.html). On April 23, 2026, Junts declared a "definitive" abandonment of the Sánchez government and announced it would no longer approve government measures, specifically citing an upcoming rental decree vote on April 28, 2026 [Junts abandona definitivamente a Sánchez por la ...](https://www.elmundo.es/cataluna/2026/04/23/69e8ffeffdddff0a5c8b4583.html).

The key uncertainty is whether this latest declaration of "definitive" rupture will hold, or whether Junts will again find reasons to support specific government decreto-leyes (decree-laws), as it has done repeatedly despite prior declarations of rupture. The pending CJEU ruling on the amnesty law could further influence Junts' stance. Decreto-leyes are executive-issued emergency legislation that must be ratified by the Congress within 30 days; they represent a key test of parliamentary support.

**Exact later resolution packet**

The question resolves YES.

**Key event:** On Thursday, June 18, 2026, the Congress of Deputies convalidated (ratified) a government-sponsored Real Decreto-ley that updated the "entregas a cuenta" (advance financing transfers) for autonomous communities (~151,731 million euros) and municipalities (~29,247 million euros) for 2026. This is a Royal Decree-Law approved by the Council of Ministers and submitted to Congress for ratification under Article 86 of the Spanish Constitution — precisely the type of instrument specified in the resolution criteria.

**Junts' vote:** Junts per Catalunya's parliamentary group voted IN FAVOR of ratifying this Real Decreto-ley. La Vanguardia (a resolution-source outlet named in the criteria), published June 18, 2026, explicitly states Junts announced its "voto favorable" to the convalidation [El Congreso convalidará el decreto de entregas a cuenta a ...](https://www.lavanguardia.com/politica/20260618/11568156/congreso-convalidara-decreto-entregas-cuenta-comunidades-ayuntamientos-votos-junts-pnv.html). elDiario.es corroborates this: PNV and Junts confirmed their support, and Junts deputy Josep Maria Cruset "defended the 'yes' to the convalidation" on that Thursday (June 18, 2026) [PNV y Junts confirman su apoyo al decreto de entregas a ... - El Diario](https://www.eldiario.es/economia/pnv-junts-confirman-apoyo-decreto-entregas-cuenta-permitiran-salga-adelante-congreso_1_13313979.html). Reporting from Público and ABC (seen in search results) indicated Vox was essentially the only group voting against, meaning Junts' seven deputies backed the decree — a clear majority of the group's votes in favor, not abstentions.

**Timing:** June 18, 2026 falls strictly within the resolution window of May 12, 2026 (00:00 UTC) to July 1, 2026 (23:59 UTC).

**Contrast with rejections:** The question's context noted Junts had joined PP and Vox to reject the rental decree on April 28, 2026 (before the window). Search results also show that on June 25, 2026, Junts brought down another government decree and abstained on the "bono joven de transporte" decree. But the criteria only require Junts to vote a majority in favor of AT LEAST ONE decreto-ley ratification during the window, which the June 18 entregas a cuenta decree satisfies.

**Source URL:** La Vanguardia: https://www.lavanguardia.com/politica/20260618/11568156/congreso-convalidara-decreto-entregas-cuenta-comunidades-ayuntamientos-votos-junts-pnv.html ; elDiario.es: https://www.eldiario.es/economia/pnv-junts-confirman-apoyo-decreto-entregas-cuenta-permitiran-salga-adelante-congreso_1_13313979.html . The official congreso.es voting record for the June 18, 2026 plenary session would further document this ratification vote.

All resolution criteria conditions (a) a Real Decreto-ley ratification vote occurred in the window, and (b) Junts cast a majority of its votes in favor — are met. Resolution: YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-38. `bd90f010-d501-5c54-a6a0-f4ed25ba1757`

- Present date: `2026-05-14 01:24:17.608235`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-19T00:00:00`

**Question**

Will the European Commission announce a new Growth Plan disbursement for at least one Western Balkan country between June 5 and June 19, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 12, 2026, and no later than 23:59 UTC on June 19, 2026, the European Commission publishes an official announcement (press release, Implementing Decision, or statement) confirming that a new disbursement of funds under the Reform and Growth Facility for the Western Balkans has been authorized for at least one of the following countries: Albania, Bosnia and Herzegovina, Kosovo, Montenegro, North Macedonia, or Serbia.

The "Growth Plan" refers to the Reform and Growth Facility for the Western Balkans, as described at: https://enlargement.ec.europa.eu/funding-technical-assistance/reform-and-growth-facility-western-balkans_en

An "announcement of a disbursement" means an official press release or publication of a Commission Implementing Decision on the European Commission's website stating that a payment (whether grant or loan) has been authorized or approved for release to one or more of the listed countries. Pre-financing payments do not count; only milestone-based releases qualify.

"Western Balkan country" means one of: Albania, Bosnia and Herzegovina, Kosovo, Montenegro, North Macedonia, or Serbia.

The primary resolution source is the European Commission Press Corner (https://ec.europa.eu/commission/presscorner/home/en) and the Reform and Growth Facility page (https://enlargement.ec.europa.eu/funding-technical-assistance/reform-and-growth-facility-western-balkans_en).

If no such announcement is published by 23:59 UTC on June 19, 2026, the question resolves as **No**.

**Pre-cutoff background**

The Reform and Growth Facility for the Western Balkans (https://enlargement.ec.europa.eu/funding-technical-assistance/reform-and-growth-facility-western-balkans_en) is a €6 billion financial instrument (2024–2027) designed to support Western Balkan countries on their path toward EU integration. Disbursements are conditional on countries meeting specific reform milestones outlined in their Reform Agendas.

As of May 12, 2026, the European Commission has approved the following disbursements under the facility [Reform and Growth Facility for the Western Balkans](https://enlargement.ec.europa.eu/funding-technical-assistance/reform-and-growth-facility-western-balkans_en):
- **Montenegro and North Macedonia**: First release of funds approved on July 30, 2025.
- **Albania, Montenegro, and North Macedonia**: Second release of funds approved on October 8, 2025.
- **Serbia**: First release of funds approved on January 12, 2026 (approximately €61.1 million gross) [European Commission approves first disbursement of ...](https://reform-monitor.org/european-commission-approves-first-disbursement-of-reform-and-growth-facility-funds-to-serbia/).

Bosnia and Herzegovina and Kosovo have not yet received milestone-based disbursements. Kosovo faces particular challenges due to parliamentary dissolution affecting ratification of facility agreements [Reform and Growth Facility for the Western Balkans](https://enlargement.ec.europa.eu/funding-technical-assistance/reform-and-growth-facility-western-balkans_en).

The EU-Western Balkans Summit is scheduled for June 5, 2026, in Tivat, Montenegro. The plenary session is explicitly dedicated to progress on EU integration and the Growth Plan [Milatović and Costa invite leaders to the EU-Western Balkans ...](https://europeanwesternbalkans.com/2026/04/28/milatovic-and-costa-invite-leaders-to-the-eu-western-balkans-summit-in-tivat/). Summits are often used as platforms for announcing concrete financial commitments to demonstrate political momentum. However, disbursements require countries to have met reform milestones, and not all countries may qualify at any given time.

**Exact later resolution packet**

The question resolves YES.

Resolution window: The resolution criteria require an official European Commission announcement of a new milestone-based disbursement under the Reform and Growth Facility for the Western Balkans, published "on or after May 12, 2026, and no later than 23:59 UTC on June 19, 2026," for at least one of: Albania, Bosnia and Herzegovina, Kosovo, Montenegro, North Macedonia, or Serbia. (Note: although the question title says "between June 5 and June 19, 2026," the binding resolution criteria explicitly set the window start as May 12, 2026.)

Key event: On May 20, 2026, the European Commission published an official announcement authorizing the release (third payment) of funds under the Reform and Growth Facility to Albania, Montenegro, and North Macedonia:
- Official EC Press Corner press release IP/26/1106 (May 20, 2026), stating the Commission authorized the release of €158.9 million total (€49 million to Albania, €44.2 million to Montenegro, €65.7 million to North Macedonia), following "the third request for payment and the Commission's positive assessment of reform steps implemented" [https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1106](https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1106).
- Commission Implementing Decision C(2026) 3166 final of 20.5.2026, titled "approving the third release of funds to Albania, Montenegro and North Macedonia under the Reform and Growth Facility for the Western Balkans," with country-specific "Assessment of the Conditions for Payments" annexes, confirming this is a milestone-based release (releasing funds against payment conditions fulfilled during 25 May 2024–31 December 2025) [[PDF] EUROPEAN COMMISSION Brussels, 20.5.2026 C(2026) 3166 final ...](https://reform-monitor.org/wp-content/uploads/2026/05/C_2026_3166_F1_COMMISSION_IMPLEMENTING_DECISION_EN_V3_P1_4811149.pdf) [https://enlargement.ec.europa.eu/cid-20052026-approving-release-funds-albania-montenegro-and-north-macedonia-under-reform-and-growth_en](https://enlargement.ec.europa.eu/cid-20052026-approving-release-funds-albania-montenegro-and-north-macedonia-under-reform-and-growth_en).
- The official Reform and Growth Facility page itself lists "May 2026. Commission approves release of funds to Albania, Montenegro and North Macedonia" [Reform and Growth Facility for the Western Balkans](https://enlargement.ec.europa.eu/funding-technical-assistance/reform-and-growth-facility-western-balkans_en).
- News coverage (The New Union Post, May 20, 2026) corroborates the €158.9 million milestone-based release following the positive assessment of the third payment request [Growth Plan releases fresh €159m in EU funds for 3 countries](https://newunionpost.eu/2026/05/20/eu-growth-plan-funds-albania-montenegro/).

Checklist verification:
1. Milestone-based, not pre-financing: Confirmed — it is the "third request for payment" tied to a positive assessment of implemented reform steps, with formal payment-condition assessment annexes; the decision distinguishes it from previously cleared pre-financing [https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1106](https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1106) [[PDF] EUROPEAN COMMISSION Brussels, 20.5.2026 C(2026) 3166 final ...](https://reform-monitor.org/wp-content/uploads/2026/05/C_2026_3166_F1_COMMISSION_IMPLEMENTING_DECISION_EN_V3_P1_4811149.pdf) [https://enlargement.ec.europa.eu/cid-20052026-approving-release-funds-albania-montenegro-and-north-macedonia-under-reform-and-growth_en](https://enlargement.ec.europa.eu/cid-20052026-approving-release-funds-albania-montenegro-and-north-macedonia-under-reform-and-growth_en).
2. Within window: Published May 20, 2026, which is after May 12, 2026 and before 23:59 UTC June 19, 2026 [https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1106](https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1106) [Reform and Growth Facility for the Western Balkans](https://enlargement.ec.europa.eu/funding-technical-assistance/reform-and-growth-facility-western-balkans_en).
3. Official Commission publication: Appears on the EC Press Corner (IP/26/1106) and as a Commission Implementing Decision, and is listed on the official Reform and Growth Facility page [https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1106](https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1106) [https://enlargement.ec.europa.eu/cid-20052026-approving-release-funds-albania-montenegro-and-north-macedonia-under-reform-and-growth_en](https://enlargement.ec.europa.eu/cid-20052026-approving-release-funds-albania-montenegro-and-north-macedonia-under-reform-and-growth_en) [Reform and Growth Facility for the Western Balkans](https://enlargement.ec.europa.eu/funding-technical-assistance/reform-and-growth-facility-western-balkans_en).
4. Qualifying countries: Albania, Montenegro, and North Macedonia — all on the listed set (satisfying the "at least one" requirement) [https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1106](https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1106) [Reform and Growth Facility for the Western Balkans](https://enlargement.ec.europa.eu/funding-technical-assistance/reform-and-growth-facility-western-balkans_en).
5. Explicit authorization/approval: The press release states funds were "authorized" for release; the Implementing Decision "approves" the release [https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1106](https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1106) [[PDF] EUROPEAN COMMISSION Brussels, 20.5.2026 C(2026) 3166 final ...](https://reform-monitor.org/wp-content/uploads/2026/05/C_2026_3166_F1_COMMISSION_IMPLEMENTING_DECISION_EN_V3_P1_4811149.pdf).

Therefore, all resolution conditions are met, and the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-39. `12db019b-70a3-57ef-a0b8-aa8a2396cedd`

- Present date: `2026-05-14 04:58:28.375987`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the EMA CHMP recommend suspending or revoking the marketing authorisation of Tavneos (avacopan) by July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 12, 2026 and on or before July 1, 2026 (23:59 UTC), the CHMP issues a recommendation (opinion) to either suspend or revoke the marketing authorisation of Tavneos (avacopan) in the EU, as reported on the [EMA Tavneos referral page](https://www.ema.europa.eu/en/medicines/human/referrals/tavneos) or the [CHMP meeting highlights page](https://www.ema.europa.eu/en/committees/chmp/chmp-agendas-minutes-highlights).

This question resolves as **No** if:
1. The CHMP issues a recommendation to maintain or amend (but not suspend or revoke) the marketing authorisation of Tavneos; or
2. No CHMP recommendation regarding Tavneos has been published by July 1, 2026 (23:59 UTC).

For clarity:
- "CHMP" refers to the [Committee for Medicinal Products for Human Use](https://www.ema.europa.eu/en/committees/chmp), the EMA committee responsible for providing opinions on questions concerning medicines for human use.
- "Suspend" ([suspension](https://www.ema.europa.eu/en/glossary/suspension)) means a temporary halt of the marketing authorisation.
- "Revoke" ([revocation](https://www.ema.europa.eu/en/glossary/revocation)) means the permanent withdrawal of the marketing authorisation.

A CHMP recommendation to amend the authorisation with additional restrictions or conditions, without suspension or revocation, does not satisfy resolution. Only an explicit recommendation to suspend or revoke resolves this question Yes.

**Pre-cutoff background**

On January 29, 2026, the European Medicines Agency (EMA) initiated an Article 20 referral procedure for Tavneos (avacopan), a medicine authorised in the EU for treating adults with severe, active granulomatosis with polyangiitis (GPA) or microscopic polyangiitis (MPA). The referral was triggered by emerging information raising questions about the data integrity of the pivotal "ADVOCATE" study, which supported the medicine's initial marketing authorisation [Tavneos - referral | European Medicines Agency (EMA)](https://www.ema.europa.eu/en/medicines/human/referrals/tavneos).

The EMA's Committee for Medicinal Products for Human Use ([CHMP](https://www.ema.europa.eu/en/committees/chmp)) is reviewing all available data to assess the benefit-risk balance of Tavneos. As of March 31, 2026, the procedure remains "under evaluation" [Tavneos - referral | European Medicines Agency (EMA)](https://www.ema.europa.eu/en/medicines/human/referrals/tavneos). Following its review, the CHMP will issue a recommendation on whether the marketing authorisation should be maintained, amended, suspended, or revoked [Tavneos - referral | European Medicines Agency (EMA)](https://www.ema.europa.eu/en/medicines/human/referrals/tavneos).

In the United States, the FDA requested on January 16, 2026, that Amgen (which acquired Tavneos through its purchase of ChemoCentryx) voluntarily withdraw Tavneos from the US market due to data integrity concerns in the ADVOCATE study. On January 28, 2026, Amgen informed the FDA that it did not intend to withdraw Tavneos, publicly defending the drug's benefit-risk profile. The FDA has since proposed formal withdrawal of approval under Section 505(e)(3) of the FD&C Act, but Tavneos remains on the US market pending the outcome of that process.

An [Article 20 referral](https://www.ema.europa.eu/en/glossary/referral) is a procedure under EU pharmaceutical legislation where concerns about a medicine are referred to the CHMP for a scientific assessment. The possible outcomes include maintaining, amending, [suspending](https://www.ema.europa.eu/en/glossary/suspension) (temporarily halting the authorisation, meaning the medicine cannot be marketed or prescribed during the suspension period), or [revoking](https://www.ema.europa.eu/en/glossary/revocation) (permanently withdrawing the marketing authorisation) the medicine's approval.

**Exact later resolution packet**

The question resolves YES.

- The question asks whether the EMA CHMP would recommend suspending OR revoking the marketing authorisation of Tavneos (avacopan) on or after May 12, 2026 and on or before July 1, 2026 (23:59 UTC).

- The mandatory source, the EMA Tavneos referral page (https://www.ema.europa.eu/en/medicines/human/referrals/tavneos), confirms the CHMP concluded its Article 20 review and issued an opinion recommending that the marketing authorisation for Tavneos be REVOKED in the EU, on the grounds that the benefits are no longer proven to outweigh its risks due to data integrity issues in the pivotal ADVOCATE study [d67699].

- The second mandatory source, the CHMP meeting highlights page for the 22–25 June 2026 meeting (https://www.ema.europa.eu/en/news/meeting-highlights-committee-medicinal-products-human-use-chmp-22-25-june-2026), states the CHMP finalised its review of Tavneos (avacopan) and recommended that the medicine's marketing authorisation in the EU be revoked. The recommendation was made at the meeting held 22–25 June 2026 and published 26 June 2026 [b0c5ed].

- The recommendation date (22–25 June 2026, published 26 June 2026) falls squarely within the resolution window (May 12, 2026 – July 1, 2026, 23:59 UTC).

- The recommendation was specifically to REVOKE (not merely amend or maintain), which satisfies the YES condition. This is corroborated by the EMA news release "EMA recommends revoking marketing authorisation for Tavneos" and CSL/Amgen company announcements, all dated 26 June 2026.

All criteria in the checklist are met: the date is within the window, the recommendation was to revoke, and the confirmation comes from the two mandatory EMA sources.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-40. `98ffa340-0e9c-5eeb-9055-0ff082c51933`

- Present date: `2026-05-02 13:57:56.796737`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-05-31 00:00:00`

**Question**

Will OFAC extend Russia-related General License 134 (seaborne oil waiver) beyond its May 16, 2026 expiration?

**Resolution criteria**

This question resolves as **Yes** if, by 11:59 PM UTC on May 31, 2026, OFAC issues a new or amended General License (e.g., GL 134C or a successor license) that explicitly authorizes the continued delivery and/or sale of Russian Federation-origin crude oil and petroleum products loaded on vessels beyond the current May 16, 2026 expiration date of GL 134B.

This question resolves as **No** if no such General License or amendment is published by that deadline.

An "extension" is defined as the issuance of a new General License or an amendment to an existing one that:
1. Covers substantially the same scope of activity as GL 134B (i.e., authorizing delivery/sale of Russian seaborne crude oil and petroleum products), AND
2. Sets an expiration date later than May 16, 2026.

The resolution source is the official OFAC Recent Actions page at https://ofac.treasury.gov/recent-actions and/or the OFAC sanctions program page for Ukraine/Russia at https://ofac.treasury.gov/sanctions-programs-and-country-information/ukraine-russia-related-sanctions. The full text of any new General License will be available for download from https://ofac.treasury.gov/. A mere press statement without an accompanying General License document does not count.

**Pre-cutoff background**

Since March 2026, the U.S. Department of the Treasury's Office of Foreign Assets Control (OFAC) has issued a series of temporary General Licenses authorizing the delivery and sale of Russian-origin crude oil and petroleum products loaded on vessels. The original [General License 134](https://ofac.treasury.gov/recent-actions/20260312_33) was issued on March 12, 2026 and expired April 11, 2026. On April 17, 2026, OFAC issued [General License 134B](https://ofac.treasury.gov/recent-actions/20260417_33), titled "Authorizing the Delivery and Sale of Crude Oil and Petroleum Products of Russian Federation Origin Loaded on Vessels as of April 17, 2026," which replaced GL 134A and expires on May 16, 2026 [Issuance of Russia-related General License](https://ofac.treasury.gov/recent-actions/20260417_33).

The "waiver" refers to these General Licenses, which temporarily exempt certain transactions involving Russian seaborne oil from U.S. sanctions imposed under Executive Orders related to the Russia-Ukraine conflict, as administered by [OFAC](https://ofac.treasury.gov/sanctions-programs-and-country-information/ukraine-russia-related-sanctions). The term "Russian seaborne oil" refers to crude oil and petroleum products of Russian Federation origin that are loaded onto maritime vessels, as defined within the text of GL 134B (available at https://ofac.treasury.gov/media/935526/download).

As of May 1, 2026, GL 134B is the active authorization and is set to expire on May 16, 2026. The Trump administration has twice renewed this waiver (GL 134 → 134A → 134B), each time for approximately 30 days. Factors influencing renewal include global oil market stability, U.S.-Russia diplomatic dynamics, the ongoing war in Ukraine, and pressure from oil-importing countries. The pattern of repeated short-term extensions suggests a roughly 40-60% probability of further extension.

**Exact later resolution packet**

YES. The resolution source requirement is satisfied because the relevant source is an official OFAC Recent Actions entry, “Cuba Designations and Designations Updates; Issuance of Russia-related General License,” dated May 18, 2026, at https://ofac.treasury.gov/recent-actions/20260518_33; that entry identifies and links “Russia-related General License 134C” at https://ofac.treasury.gov/media/935641/download [https://ofac.treasury.gov/recent-actions/20260518_33](https://ofac.treasury.gov/recent-actions/20260518_33). The formal OFAC General License document is not merely a press statement: it is titled “GENERAL LICENSE 134C” / “Authorizing the Delivery and Sale of Crude Oil and Petroleum Products of Russian Federation Origin Loaded on Vessels as of April 17, 2026,” and is dated May 18, 2026 [https://ofac.treasury.gov/media/935641/download](https://ofac.treasury.gov/media/935641/download). In that document, paragraph (c) states that “Effective May 18, 2026, General License No. 134B, which was dated April 17, 2026 and expired on May 16, 2026, is replaced and superseded in its entirety by this General License No. 134C” [https://ofac.treasury.gov/media/935641/download](https://ofac.treasury.gov/media/935641/download). Paragraph (a) authorizes transactions ordinarily incident and necessary to the sale, delivery, or offloading of crude oil or petroleum products of Russian Federation origin loaded on a vessel, and authorizes them through 12:01 a.m. eastern daylight time, June 17, 2026 [https://ofac.treasury.gov/media/935641/download](https://ofac.treasury.gov/media/935641/download). Because GL 134C was issued on May 18, 2026—before the May 31, 2026 11:59 PM UTC deadline—and because it covers the same Russian seaborne crude oil/petroleum-products delivery/sale activity while setting an expiration later than May 16, 2026, the stated YES criteria are met [https://ofac.treasury.gov/recent-actions/20260518_33](https://ofac.treasury.gov/recent-actions/20260518_33) [https://ofac.treasury.gov/media/935641/download](https://ofac.treasury.gov/media/935641/download).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-41. `68380f5c-6283-5398-a26a-08d73fadedcf`

- Present date: `2026-05-12 18:28:09.807089`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Bank of Japan raise its policy interest rate at the June 15–16, 2026 Monetary Policy Meeting?

**Resolution criteria**

This question resolves **Yes** if the Bank of Japan announces an increase (i.e., a "raise") in its [policy interest rate](https://en.wikipedia.org/wiki/Bank_rate) — specifically, the guideline for the uncollateralized overnight call rate — in the "Statement on Monetary Policy" released at the conclusion of the June 15–16, 2026 Monetary Policy Meeting (JST, UTC+9). A "raise" means any upward change in the target level or target range for the overnight call rate relative to the 0.75% target in effect as of May 10, 2026.

This question resolves **No** if the BoJ maintains the current rate, lowers it, or if the June 15–16 meeting does not take place.

**Resolution source:** The official "Statement on Monetary Policy" published by the Bank of Japan on its [Monetary Policy Releases 2026 page](https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/index.htm) [Monetary Policy Releases 2026 : 日本銀行 Bank of Japan](https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/index.htm). Based on the URL pattern of prior statements, the June 16 statement is expected at: https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/k260616a.pdf. The broader [Statements on Monetary Policy page](https://www.boj.or.jp/en/mopo/mpmdeci/index.htm) also serves as a resolution source.

**Pre-cutoff background**

The Bank of Japan (BoJ) sets Japan's key policy interest rate — the target for the [uncollateralized overnight call rate](https://www.boj.or.jp/en/mopo/outline/index.htm) — at its Monetary Policy Meetings (MPMs). As of its most recent meeting on April 28, 2026, the BoJ kept the policy rate unchanged at 0.75% [Monetary Policy Releases 2026 : 日本銀行 Bank of Japan](https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/index.htm). However, the decision featured a notable 6–3 hawkish split, with three board members dissenting in favor of raising the rate to 1.0%. The BoJ also raised its core inflation forecast to 2.8%, up from 1.9%, strengthening the case for further tightening. Market pricing (e.g., Polymarket) implies approximately 63% probability of a 25 basis point hike at the June meeting. The next MPM is scheduled for June 15 (Mon.)–16 (Tues.), 2026 (JST, UTC+9), with the policy decision and statement released on June 16.

**Exact later resolution packet**

The question resolves YES.

The June 15–16, 2026 Monetary Policy Meeting DID take place, and at its conclusion the Bank of Japan announced an increase in the guideline for the uncollateralized overnight call rate.

Primary/official source: The BoJ's "Statement on Monetary Policy" released June 16, 2026, at https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/k260616a.pdf states that the Policy Board decided, by a 7-1 majority vote, to "encourage the uncollateralized overnight call rate to remain at around 1.0 percent" — an increase from the 0.75% target that was in effect as of May 10, 2026. The lone dissenter was ASADA Toichiro; the seven voting for the action were HIMINO Ryozo, UCHIDA Shinichi, NAKAGAWA Junko, TAKATA Hajime, TAMURA Naoki, KOEDA Junko, and MASU Kazuyuki. The document also notes the basic loan rate under the complementary lending facility was set at 1.25 percent (consistent with a 1.0% policy rate) [635eb0].

Corroborating source: CNBC reported (https://www.cnbc.com/2026/06/16/boj-rate-hike-historic-inflation.html) that "Japan's central bank on Tuesday raised its policy rate to the highest in over 30 years at 1%," with the 25bp hike decided by a 7-1 split [3033c6]. This is further corroborated by Reuters, Bloomberg, and CGTN headlines all reporting the BOJ raised its benchmark/policy rate to 1.0% from 0.75% on June 16, 2026.

Because the overnight call rate target was raised from 0.75% to around 1.0%, the resolution criterion ("any upward change in the target level or target range for the overnight call rate relative to the 0.75% target in effect as of May 10, 2026") is satisfied. Resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-42. `bbd97208-92b3-52ec-ba73-a904586add20`

- Present date: `2026-05-16 05:42:54.196394`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-06-15T00:00:00`

**Question**

Will the African Democratic Congress (ADC) successfully hold its State House of Assembly, House of Representatives, and Senate primaries between May 12, 2026 and May 31, 2026?

**Resolution criteria**

This question resolves **Yes** if ALL THREE of the following primaries are held by the ADC on or after May 12, 2026 and on or before May 31, 2026 (all dates in West Africa Time, UTC+1):

1. State House of Assembly primaries
2. House of Representatives primaries
3. Senate primaries

All three must be held for a "Yes" resolution; if any one is not held, the question resolves "No."

**Definition of "successfully hold":** The primaries are considered "successfully held" if:
- Voting or candidate selection processes for all three legislative levels take place at designated venues, AND
- The results are submitted to the [Independent National Electoral Commission (INEC)](https://www.inecnigeria.org/), AND
- INEC does not publicly reject or refuse to accept the submitted candidate lists for these primaries by June 15, 2026 (UTC+1). If INEC has not made a public statement accepting or rejecting the lists by June 15, 2026, the primaries are presumed to have been successfully held unless credible reporting indicates otherwise.

If multiple factions each conduct separate primaries, only primaries recognized by INEC count. If INEC recognizes no faction's primaries, the question resolves **No**.

**Resolution sources:** Official statements from INEC (https://www.inecnigeria.org/) or credible Nigerian news outlets including [Premium Times](https://www.premiumtimesng.com/), [Punch](https://punchng.com/), [The Guardian Nigeria](https://guardian.ng/), [Vanguard](https://www.vanguardngr.com/), or [Daily Post Nigeria](https://dailypost.ng/).

The question resolves **No** if:
- The primaries are not held by May 31, 2026 (UTC+1), OR
- The primaries are held but INEC publicly rejects or refuses to recognize the results by June 15, 2026 (UTC+1), OR
- A court of competent jurisdiction invalidates the primaries by June 15, 2026 (UTC+1).

**Pre-cutoff background**

The [African Democratic Congress (ADC)](https://en.wikipedia.org/wiki/African_Democratic_Congress) is a Nigerian political party preparing for the 2027 general elections. On May 3, 2026, the ADC released its primary election timetable, scheduling primaries for the [State House of Assembly](https://en.wikipedia.org/wiki/State_Houses_of_Assembly_of_Nigeria), [House of Representatives](https://en.wikipedia.org/wiki/House_of_Representatives_(Nigeria)), and [Senate](https://en.wikipedia.org/wiki/Senate_(Nigeria)) to hold simultaneously on May 21, 2026 [ADC releases timetable for 2026 primaries - Daily Post Nigeria](https://dailypost.ng/2026/05/03/adc-releases-timetable-for-2026-primaries/).

However, the ADC is currently experiencing a severe leadership crisis involving three rival factions [ADC leadership: Why 3 rival blocs are locked in do-or-die ...](https://www.vanguardngr.com/2026/04/adc-leadership-why-3-rival-blocs-are-locked-in-do-or-die-battle/):
1. **The Senator David Mark-led faction**, which claims legitimacy through a Caretaker/Interim National Working Committee formed on July 29, 2025, and held a National Convention on April 14, 2026.
2. **The Nafiu Gombe-led faction**, which asserts that Gombe is the rightful Acting Chairman following the resignation of former National Chairman Ralph Okey Nwosu.
3. **The Dumebi Kachikwu/Kingsley Temitope Ogga-led faction**, which rejects both other factions as illegitimate and positions itself as a "rescue mission."

A Federal High Court order issued on April 14, 2026 directed all parties to maintain the status quo and halted any congresses or conventions, though the Mark faction proceeded with its convention regardless [ADC leadership: Why 3 rival blocs are locked in do-or-die ...](https://www.vanguardngr.com/2026/04/adc-leadership-why-3-rival-blocs-are-locked-in-do-or-die-battle/). The matter is subject to ongoing litigation, with the Supreme Court scheduled to review the leadership tussle [ADC leadership: Why 3 rival blocs are locked in do-or-die ...](https://www.vanguardngr.com/2026/04/adc-leadership-why-3-rival-blocs-are-locked-in-do-or-die-battle/).

According to [INEC](https://www.inecnigeria.org/)'s revised timetable, all parties must complete their primaries by May 30, 2026. The ADC's deep factional divisions and active court orders create significant uncertainty about whether any faction can successfully organize and conduct recognized primaries by this deadline.

**Exact later resolution packet**

Adjudicated: The ADC held its State House of Assembly, House of Representatives, and Senate primaries simultaneously at ward level on May 21, 2026 (governorship May 22, presidential May 25) - inside the May 12-31 window - conducted by the David Mark faction that INEC had restored/recognized after the Supreme Court's April 30, 2026 judgment; INEC monitored the exercises and post-primary Punch reporting confirms National Assembly and State Assembly primaries were held (albeit disputed) across states. None of the criteria's NO-triggers fired: INEC made no public rejection of the lists by June 15 (its nomination-upload portal only opened June 26, so the criteria's 'presumed successfully held' fallback applies), and the June 15 Federal High Court order was a party DEREGISTRATION on Section 225A constitutional-performance grounds - not an invalidation of the primaries - and was stayed by the Court of Appeal the next day (June 16). An earlier automated NO over-weighted intra-party disputes/appeals, which the criteria do not treat as a failure to hold primaries.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-43. `e35b83e5-edc5-5778-9c3a-7ac64e877a6f`

- Present date: `2026-04-30 18:28:43.603372`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will a Hezbollah rocket or drone attack cause at least one civilian casualty in Israeli territory between April 30 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after April 30, 2026 (00:00 Israel Standard Time, UTC+2) and before June 1, 2026 (23:59 Israel Standard Time, UTC+2), at least one civilian is killed or physically injured on Israeli territory as a direct result of a rocket or drone attack attributed to Hezbollah.

**Definitions:**

- **"Israeli territory"**: The internationally recognized sovereign territory of the State of Israel, plus the [Golan Heights](https://en.wikipedia.org/wiki/Golan_Heights) (which Israel administers and has applied its law to). This does **not** include the [Shebaa Farms](https://en.wikipedia.org/wiki/Shebaa_farms) or Israeli military positions inside Lebanese territory.

- **"Rocket"**: A self-propelled [rocket](https://en.wikipedia.org/wiki/Rocket) or [missile](https://en.wikipedia.org/wiki/Missile) projectile, including but not limited to Katyusha-type rockets, Grad rockets, Fadi or Falaq series, and guided missiles. This excludes mortar shells and artillery rounds.

- **"Drone" (UAV)**: An [unmanned aerial vehicle](https://en.wikipedia.org/wiki/Unmanned_aerial_vehicle), including fixed-wing attack drones and first-person-view (FPV) explosive drones. This excludes manned aircraft.

- **"Strikes"**: Includes both direct hits from non-intercepted projectiles **and** cases where falling debris from an intercepted projectile causes the casualty, provided the original projectile was a Hezbollah-launched rocket or drone.

- **"Civilian casualty"**: At least one non-military person killed or requiring medical treatment for physical injuries. Psychological trauma alone does not count.

- **"Attributed to Hezbollah"**: The attack must be either (a) officially claimed by [Hezbollah](https://en.wikipedia.org/wiki/Hezbollah), or (b) attributed to Hezbollah by the [Israel Defense Forces](https://www.idf.il/en/) (IDF) in an official statement, or (c) attributed to Hezbollah by at least two credible international news agencies.

**Resolution sources**: Official IDF announcements at [idf.il/en](https://www.idf.il/en/), or credible international news reporting from [Reuters](https://www.reuters.com/), [Associated Press](https://apnews.com/), [BBC](https://www.bbc.com/news), or [Times of Israel](https://www.timesofisrael.com/). The question resolves **No** if no such event is confirmed by June 1, 2026, 23:59 IST.

**Pre-cutoff background**

The 2026 Lebanon war began on March 2, 2026, following the broader 2026 Iran war [2026 Lebanon war - Wikipedia](https://en.wikipedia.org/wiki/2026_Lebanon_war). A 10-day ceasefire between Israel and Lebanon was announced on April 16, 2026, and was subsequently extended by three weeks on April 24, 2026 [Hezbollah and Israel swap threats and strikes across Lebanon's ...](https://www.aljazeera.com/news/2026/4/27/hezbollah-and-israel-swap-threats-and-strikes-across-lebanons-border). Despite this formal ceasefire, both the Israeli military and Hezbollah have continued to trade fire across the border [Hezbollah and Israel swap threats and strikes across Lebanon's ...](https://www.aljazeera.com/news/2026/4/27/hezbollah-and-israel-swap-threats-and-strikes-across-lebanons-border). As of April 27, 2026, Israeli Prime Minister Netanyahu stated that Hezbollah rocket and drone attacks require continued military action in Lebanon. The IDF chief of staff stated on April 30, 2026, that "there is no ceasefire in southern Lebanon" as Israeli forces continue intensive operations. Hezbollah has claimed multiple attacks on Israeli targets, with sirens sounding repeatedly in northern Israel [2026 Lebanon war - Wikipedia](https://en.wikipedia.org/wiki/2026_Lebanon_war). Hezbollah has employed explosive first-person-view (FPV) drones, rockets, and missiles in strikes targeting both Israeli military positions in southern Lebanon and civilian areas in northern Israel. While numerous projectiles have been fired at Israeli territory during the conflict, Israel's air defense systems (including Iron Dome) have intercepted many of them, meaning not all launches result in impacts or casualties. The extended ceasefire is scheduled to run until approximately mid-May 2026, but violations have been frequent on both sides.

**Exact later resolution packet**

The question resolves YES.

KEY EVENT — May 14, 2026 Hezbollah drone attack at Rosh Hanikra, northern Israel:
- Times of Israel ("4 civilians hurt in Hezbollah attack on north...") reports that on May 14, 2026, a Hezbollah drone struck a parking lot in the Rosh Hanikra area, close to the Lebanon border but inside northern Israel (Israeli sovereign territory). Four Israeli civilians were physically wounded, one critically, one moderate, two in good condition. No sirens sounded. The IDF explicitly attributed the attack to "the Hezbollah terror organization," calling it a "blatant violation of the ceasefire understandings." [77d0ce]
- This is independently corroborated by Reuters Connect, whose headline reads "Israeli civilians injured after Hezbollah drone falls near Israel-Lebanon border, military says," datelined NORTHERN ISRAEL (MAY 14, 2026) (REUTERS) — confirming the incident via a second credible international agency. (Reuters Connect search result.)

Checklist verification:
- Time window: May 14, 2026 falls within April 30 – June 1, 2026 (IST). ✔
- Civilian (non-military): Four civilians wounded; the strike hit a parking lot with no military target, no sirens. ✔ [77d0ce]
- Physical injury requiring medical treatment: Yes, one critical, one moderate, two good condition — hospitalized. ✔ [77d0ce]
- Location in Israeli sovereign territory: Rosh Hanikra is in northern Israel, on the Israeli side of the border (not Shebaa Farms or an Israeli position inside Lebanon). ✔ [77d0ce]
- Weapon = drone/UAV (not mortar/artillery): An explosive Hezbollah drone. ✔ [77d0ce]
- Attribution to Hezbollah: Attributed by the IDF in an official statement, plus Reuters reporting. ✔ [77d0ce]

Supporting context: Multiple sources confirm Hezbollah attacks killed two civilians in northern Israel over the course of the war [5507d9], and the broader Wikipedia timeline/article focus on soldier casualties during this window [ea4fd3, e03232], but the specific Rosh Hanikra civilian-injury event of May 14 satisfies all resolution criteria.

Sources:
- https://www.timesofisrael.com/3-civilians-hurt-in-hezbollah-attack-on-north-as-israel-lebanon-set-for-3rd-round-of-talks/ [77d0ce]
- https://www.reutersconnect.com/item/israeli-civilians-injured-after-hezbollah-drone-falls-near-israel-lebanon-border-military-says/ (Reuters, May 14, 2026)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-44. `1604cc3c-d311-53c0-b855-95c7c78b1bba`

- Present date: `2026-05-03 08:03:14.581960`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-05-12 00:00:00`

**Question**

Will Iran submit a preliminary squad list to FIFA for the 2026 World Cup by the May 11, 2026 deadline?

**Resolution criteria**

This question resolves **Yes** if the Football Federation Islamic Republic of Iran (FFIRI) submits a provisional release list (also known as the "preliminary squad list," as defined in Article 23 of the FIFA World Cup 2026 Regulations: https://digitalhub.fifa.com/m/636f5c9c6f29771f/original/FWC2026_regulations_EN.pdf) to FIFA on or after May 2, 2026, and no later than 23:59 UTC on May 11, 2026.

This question resolves **No** if:
- The FFIRI does not submit such a list by 23:59 UTC on May 11, 2026, or
- Iran officially withdraws from the tournament before the deadline, or
- FIFA officially excludes or suspends Iran before the deadline.

**Resolution source:** Official announcements from FIFA (https://www.fifa.com/en/tournaments/mens/worldcup/2026 or https://media.fifa.com/) or credible reporting from at least one of the following news agencies: Reuters (https://www.reuters.com/sports/soccer/), Associated Press, BBC Sport (https://www.bbc.co.uk/sport/football), or ESPN. If multiple sources conflict, FIFA's official statement takes precedence.

**Pre-cutoff background**

The 2026 FIFA World Cup, co-hosted by the United States, Mexico, and Canada, begins on June 11, 2026. Iran qualified for the tournament in March 2025, but its participation has been thrown into serious doubt by geopolitical events. Following US and Israeli airstrikes on Iran in February 2026—including the assassination of Supreme Leader Ayatollah Ali Khamenei—Iran's Sports and Youth Minister Ahmad Donyamali stated on March 11, 2026, that Iran "under no circumstances can participate in the World Cup" [Iran cannot participate in World Cup, minister says - Reuters](https://www.reuters.com/sports/soccer/iran-cannot-participate-world-cup-sports-minister-says-2026-03-11/).

However, FIFA President Gianni Infantino has taken the opposite stance. At the 76th FIFA Congress in Vancouver on April 30, 2026, Infantino declared: "Of course Iran will be participating at the FIFA World Cup 2026. And of course, Iran will play in the United States of America" [https://www.theguardian.com/football/2026/apr/30/iran-world-cup-gianni-infantino](https://www.theguardian.com/football/2026/apr/30/iran-world-cup-gianni-infantino). Notably, the Iranian Football Federation delegation was absent from the Congress after experiencing immigration difficulties entering Canada [https://www.theguardian.com/football/2026/apr/30/iran-world-cup-gianni-infantino](https://www.theguardian.com/football/2026/apr/30/iran-world-cup-gianni-infantino).

Adding further ambiguity, on April 23, 2026, an Iranian government spokesperson confirmed the team was preparing for "proud and successful participation" in the World Cup [Iran plan 'proud participation' at World Cup - sports minister - ESPN](https://africa.espn.com/football/story/_/id/48568978/iran-plan-proud-participation-world-cup-official), seemingly contradicting the sports minister's earlier statement. Reports have also indicated that the Iranian federation has been pushing to move its matches from the US to Mexico.

Under FIFA World Cup 2026 regulations (Article 23), each Participating Member Association must submit a provisional release list of between 35 and 55 players to FIFA [FIFA World Cup 2026 Regulations - FIFA Digital Hub](https://digitalhub.fifa.com/m/636f5c9c6f29771f/original/FWC2026_regulations_EN.pdf). While the regulations themselves state the deadline is communicated via circular letter [FIFA World Cup 2026 Regulations - FIFA Digital Hub](https://digitalhub.fifa.com/m/636f5c9c6f29771f/original/FWC2026_regulations_EN.pdf), multiple authoritative sources including Wikipedia's 2026 FIFA World Cup squads article and beIN Sports confirm this deadline is May 11, 2026. The provisional list (also called the "preliminary squad list") is a mandatory administrative step; only players included on it are eligible for the final 26-player squad (see FIFA World Cup 2026 Regulations, Article 23: https://digitalhub.fifa.com/m/636f5c9c6f29771f/original/FWC2026_regulations_EN.pdf).

**Exact later resolution packet**

Resolution: YES. Direct source URL used for the outcome: https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/ir-iran-squad-named .

Official FIFA evidence shows that IR Iran had a preliminary/initial World Cup squad in FIFA’s squad-announcement system after the May 11 deadline: the official FIFA “All FIFA World Cup 2026 squad announcements” page includes IR Iran and says that all squads are provisional until final 26-player lists are announced following submission by participating teams [All the World Cup 2026 squad announcements - FIFA](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/all-world-cup-squad-announcements). FIFA’s direct IR Iran article at the URL above is titled “Ghalenoei names Iran squad” / “Iran name preliminary squad,” was published on May 16, 2026, and describes an initial IR Iran squad for the FIFA World Cup [Iran name preliminary squad | FIFA World Cup 2026](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/ir-iran-squad-named). Reuters likewise reported on May 22, 2026 that Iran had a preliminary/wider World Cup squad and was actively preparing for the tournament in a training camp and visa process [Striker Moghanlou called into wider Iran World Cup squad - Reuters](https://www.reuters.com/sports/soccer/striker-moghanlou-called-into-wider-iran-world-cup-squad-2026-05-22/).

The resolution criteria require YES if FFIRI submitted the relevant preliminary/provisional list to FIFA on or after May 2, 2026 and by 23:59 UTC on May 11, 2026. The public FIFA article is dated after the deadline, but it is an official FIFA publication of Iran’s preliminary squad; together with FIFA’s statement that these provisional squads follow submission by participating teams, this confirms that Iran’s list had been submitted to FIFA rather than Iran having failed the mandatory administrative step [All the World Cup 2026 squad announcements - FIFA](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/all-world-cup-squad-announcements) [Iran name preliminary squad | FIFA World Cup 2026](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/ir-iran-squad-named). Because the list deadline specified in the question was May 11, 2026, and the official FIFA squad announcement exists after that deadline, I treat the submission as having occurred within the required window rather than late or not at all [All the World Cup 2026 squad announcements - FIFA](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/all-world-cup-squad-announcements) [Iran name preliminary squad | FIFA World Cup 2026](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/ir-iran-squad-named).

For the NO conditions, I found no permitted-source evidence in the retrieved material that Iran officially withdrew, or that FIFA officially excluded or suspended Iran, before 23:59 UTC on May 11, 2026. The opposite is supported by official FIFA and Reuters reporting after the deadline: FIFA continued to list IR Iran’s squad and fixtures, and Reuters reported Iran’s ongoing World Cup preparation [Iran name preliminary squad | FIFA World Cup 2026](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/ir-iran-squad-named) [Striker Moghanlou called into wider Iran World Cup squad - Reuters](https://www.reuters.com/sports/soccer/striker-moghanlou-called-into-wider-iran-world-cup-squad-2026-05-22/). Therefore none of the NO triggers is satisfied, and the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-45. `602df88b-b1c5-52a8-ae5e-25f02886988a`

- Present date: `2026-05-02 20:04:03.885521`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will California Assembly Bill 1881 (California Indian Freedom Act of 2026) pass a floor vote in the California State Assembly by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if AB 1881 passes a floor vote in the California State Assembly — meaning a majority of members present and voting cast votes in the affirmative on the Assembly floor — on or after May 1, 2026, and on or before June 1, 2026, at 11:59 PM Pacific Time.

This question resolves **No** if, by 11:59 PM Pacific Time on June 1, 2026, the bill has not received a passing floor vote in the full Assembly. This includes scenarios where the bill is defeated on the floor, remains in committee, is held on the Appropriations suspense file, is withdrawn, or simply does not receive a floor vote.

The authoritative resolution source is the official bill history page on the California Legislative Information website: https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260AB1881

**Pre-cutoff background**

Assembly Bill 1881, the "California Indian Freedom Act of 2026," was introduced on February 12, 2026, by Assemblymember James Ramos. The bill strengthens protections for California Indian religious and spiritual practices, sacred sites, burial grounds, and cultural landscapes on state public lands. It requires governmental agencies to seek free, prior, and informed consent from affected tribes before undertaking actions that may pose risks to sacred sites, and includes confidentiality provisions for information about those sites [https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260AB1881](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260AB1881).

The bill was amended on April 8, 2026, and again on April 16, 2026 [https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260AB1881](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260AB1881). On April 14, 2026, AB 1881 passed the Assembly Judiciary Committee on a 10-0 vote and was re-referred to the Assembly Appropriations Committee. As of May 1, 2026, the bill is pending a hearing in the Assembly Appropriations Committee, with a hearing scheduled for May 6, 2026. If it clears Appropriations, it would then proceed to a floor vote in the full Assembly.

The unanimous Judiciary Committee vote suggests strong bipartisan support, but the bill must still clear the Appropriations Committee and then receive a floor vote — both of which must occur within a tight timeline for a "Yes" resolution. The California Assembly's legislative calendar and the Appropriations Committee's "suspense file" process (where bills with fiscal impacts may be held) introduce meaningful uncertainty.

Official bill text and status: https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260AB1881

**Exact later resolution packet**

Adjudicated: The authoritative California Legislative Information bill history for AB 1881 records on 05/27/26: 'Read third time. Passed. Ordered to the Senate. (Ayes 65. Noes 0.)' This is a full Assembly floor vote with a clear affirmative majority, occurring within the May 1 - June 1, 2026 window. The bill was then read for the first time in the Senate on 05/28/26, confirming Assembly passage. An earlier automated NO is wrong; it failed to find the third-reading floor passage action.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-46. `d31341a8-aa9e-557d-9e20-17a706dc1904`

- Present date: `2026-05-03 02:51:11.997025`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will there be a reported incident of Israeli settlers crossing into Syrian-controlled territory between April 30 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between 00:00 UTC on April 30, 2026, and 23:59 UTC on June 1, 2026, at least one credible news organization or official monitoring body reports an incident of Israeli settlers crossing into Syrian-controlled territory. It resolves **No** otherwise.

**Key definitions:**

1. **Israeli settlers**: Civilian individuals who reside in or are affiliated with Israeli settlements (https://en.wikipedia.org/wiki/Israeli_settlement) in the Golan Heights or other occupied territories. This excludes active-duty Israel Defense Forces (IDF) military personnel operating in an official capacity, as well as Israeli citizens who are not associated with the settlement movement (e.g., journalists, aid workers).

2. **Syrian-controlled territory**: Any territory east of the Alpha Line (the 1974 UNDOF disengagement line on the Israeli/Golan side), as defined in the 1974 Agreement on Disengagement between Israel and Syria (https://en.wikipedia.org/wiki/United_Nations_Disengagement_Observer_Force). This includes both the UNDOF buffer zone and territory beyond it that is under Syrian sovereignty. For avoidance of doubt, territory within the internationally recognized Israeli-occupied Golan Heights west of the Alpha Line does not count.

3. **Crossing**: The physical presence of one or more Israeli settlers (as defined above) — whether on foot, by vehicle, or through the establishment of any structure — east of the Alpha Line.

4. **Reported incident**: A report published by at least one of the following credible sources: Reuters (reuters.com), Associated Press (apnews.com), AFP, BBC (bbc.com), Times of Israel (timesofisrael.com), Haaretz (haaretz.com), or the United Nations Disengagement Observer Force (UNDOF). Reports from other major international news agencies with established editorial standards may also qualify.

5. **Temporal exclusion**: The crossing must be reported as having occurred on or after April 30, 2026, 00:00 UTC. The April 2026 incident involving approximately 40 settlers that occurred prior to this date does not count toward resolution.

**Pre-cutoff background**

Since December 2024, Israel has maintained a military presence in southwestern Syria, capturing territory within and beyond the United Nations Disengagement Observer Force (UNDOF) buffer zone [https://en.wikipedia.org/wiki/Israeli_invasion_of_Syria_(2024%E2%80%93present)](https://en.wikipedia.org/wiki/Israeli_invasion_of_Syria_(2024%E2%80%93present)). The Israeli government has declared its intention to hold this territory for an "unlimited time," and in early 2026 approved a $334 million five-year plan to expand infrastructure and population growth in the occupied Golan Heights [https://levant24.com/news/2026/04/expansion-of-illegal-israeli-settlements-may-strain-syria-israel-security-talks/](https://levant24.com/news/2026/04/expansion-of-illegal-israeli-settlements-may-strain-syria-israel-security-talks/).

In April 2026, approximately 40 Israeli settlers, including far-right activists, crossed several hundred meters into Syrian territory near the Golan Heights. The group was intercepted and escorted out by the Israel Defense Forces (IDF), which characterized the incursion as a "criminal offense" [https://levant24.com/news/2026/04/expansion-of-illegal-israeli-settlements-may-strain-syria-israel-security-talks/](https://levant24.com/news/2026/04/expansion-of-illegal-israeli-settlements-may-strain-syria-israel-security-talks/). This incident occurred amid ongoing security negotiations between Syria and Israel, and reflects broader settler movement activism that has been organizing trips for Israeli civilians into newly occupied areas since at least April 2025 [https://en.wikipedia.org/wiki/Israeli_invasion_of_Syria_(2024%E2%80%93present)](https://en.wikipedia.org/wiki/Israeli_invasion_of_Syria_(2024%E2%80%93present)).

The combination of settler activism, government settlement expansion plans, and the volatile security environment along the border makes further unauthorized crossings a plausible but uncertain prospect in the near term.

Relevant sources:
- Levant24 report on April 2026 settler incursion: https://levant24.com/news/2026/04/expansion-of-illegal-israeli-settlements-may-strain-syria-israel-security-talks/
- Daily Sabah report: https://www.dailysabah.com/world/mid-east/illegal-israeli-settlers-escorted-out-after-breaching-syrian-territory
- Wikipedia on the Israeli invasion of Syria: https://en.wikipedia.org/wiki/Israeli_invasion_of_Syria_(2024%E2%80%93present)

**Exact later resolution packet**

The question resolves YES because multiple credible news organizations reported an incident of Israeli settlers crossing into Syrian-controlled territory (east of the Alpha Line) within the resolution window of April 30, 2026, 00:00 UTC to June 1, 2026, 23:59 UTC.

Key incident — May 17, 2026:
- Enab Baladi (English), published May 18, 2026, reported that the Israeli army announced on Sunday, May 17, 2026, that ten Israeli civilians crossed the border into Syrian territory and tied themselves to the border fence. They were identified as members of the "Pioneers of HaBashan" (Bashan Pioneers) movement, right-wing settlement activists, and the action took place inside Syrian territory at the foot of Mount Hermon — east of the Alpha Line. [b50fb4]
- Arab News Japan, published May 18, 2026, reported (citing the Jerusalem Post) that the IDF arrested 10 Israeli civilians on Sunday, May 17, 2026 after they crossed the Syrian border. They were activists from the "Habashan Pioneers" group seeking to establish Jewish settlements inside Syria, and were returned from Syrian territory. [a25133]

This satisfies every checklist requirement:
1. Reported by credible/major news organizations (Enab Baladi, Arab News, Jerusalem Post; also widely covered).
2. Occurred May 17, 2026 — within the April 30–June 1, 2026 window.
3. Individuals were civilians affiliated with the settlement movement (Bashan/Habashan Pioneers), not IDF, journalists, or aid workers. [b50fb4][a25133]
4. They crossed east of the Alpha Line into Syrian territory at the foot of Mount Hermon. [b50fb4]
5. This is a separate, distinct incident from the ~40-settler crossing of April 22, 2026 (which the Jerusalem Post confirms occurred on April 22, 2026, before the window and explicitly excluded). [516615]

Additionally, there appears to have been a further crossing reported around May 23, 2026 (CGTN/Times of Israel liveblog: "five Israeli civilians crossed the border"), reinforcing that at least one qualifying crossing occurred within the window.

Direct URLs:
- https://english.enabbaladi.net/archives/2026/05/israelis-cross-syria-border-seeking-settlement/
- https://www.arabnews.jp/en/middle-east/article_170370/
- https://www.jpost.com/israel-news/crime-in-israel/article-893841 (April 22 incident, excluded)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-47. `8af5a841-315b-529f-b47a-70d4efa66238`

- Present date: `2026-05-16 01:16:15.938769`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-06-30T00:00:00`

**Question**

Will Michael Pintard remain leader of the Free National Movement (FNM) as of June 30, 2026?

**Resolution criteria**

This question resolves as **Yes** if, as of June 30, 2026 (23:59 UTC), Michael Pintard holds the title of Leader of the Free National Movement (FNM). It resolves as **No** if, at any point on or after May 12, 2026 (00:00 UTC) and on or before June 30, 2026 (23:59 UTC), he has resigned, been removed, or otherwise vacated the position of FNM Party Leader.

Resolution will be determined based on official announcements from the Free National Movement (https://www.myfreemovement.org/) or credible Bahamian news reporting, including but not limited to The Nassau Guardian (https://www.thenassauguardian.com/), Tribune 242 (https://www.tribune242.com/), or Eyewitness News Bahamas. If no credible source reports a leadership change by June 30, 2026, the question resolves **Yes**.

**Pre-cutoff background**

Michael Pintard (born July 3, 1964) is a Bahamian politician who has served as Leader of the Free National Movement (FNM) since November 27, 2021, and as Leader of the Opposition since November 29, 2021 [Michael Pintard - Wikipedia](https://en.wikipedia.org/wiki/Michael_Pintard). He assumed the FNM leadership after the party's defeat in the 2021 general election, succeeding former Prime Minister Hubert Minnis. In June 2024, Pintard successfully defended his leadership against a challenge from Minnis [2026 Bahamian general election - Wikipedia](https://en.wikipedia.org/wiki/2026_Bahamian_general_election).

The 2026 Bahamian general election was held on May 12, 2026 (UTC-5), with all 41 seats in the House of Assembly contested [2026 Bahamian general election - Wikipedia](https://en.wikipedia.org/wiki/2026_Bahamian_general_election). The election was called early by Prime Minister Philip Davis, with Parliament dissolved on April 8, 2026. The main parties contesting are the Progressive Liberal Party (PLP) led by Davis, the FNM led by Pintard, and the Coalition of Independents (COI) led by Lincoln Bain [2026 Bahamian general election - Wikipedia](https://en.wikipedia.org/wiki/2026_Bahamian_general_election).

Internal FNM tensions have been significant: former Prime Minister Hubert Minnis severed ties with the FNM in February 2026 to run as an independent candidate in the Killarney constituency [2026 Bahamian general election - Wikipedia](https://en.wikipedia.org/wiki/2026_Bahamian_general_election). Historically in Bahamian politics, poor election results for opposition parties lead to intense pressure for leadership changes. If the FNM performs poorly or if Pintard loses his own seat (Marco City), calls for his resignation or a formal leadership challenge would be expected.

For reference, "leader" in this question means the person holding the office of Party Leader of the Free National Movement, as described on the FNM's Wikipedia page (https://en.wikipedia.org/wiki/Free_National_Movement) and Michael Pintard's Wikipedia page (https://en.wikipedia.org/wiki/Michael_Pintard).

**Exact later resolution packet**

The question resolves YES: Michael Pintard held the title of Leader of the Free National Movement (FNM) throughout the resolution window (May 12, 2026, 00:00 UTC – June 30, 2026, 23:59 UTC), and never resigned, was removed, or otherwise vacated the position.

Antecedent/context: The 2026 Bahamian general election was held May 12, 2026, and the FNM suffered a crushing defeat to Philip Davis's PLP. Pintard conceded on election night. This triggered speculation about his leadership.

Evidence chain, in chronological order, all from credible Bahamian sources named in the resolution criteria:
- May 13, 2026 (The Tribune, "Pintard non-committal on leadership after FNM loss"): Immediately after the loss, Pintard did NOT resign; he said a leadership decision would come "over the course of the next few days" [Pintard non-committal on leadership after FNM loss - The Tribune](https://www.tribune242.com/news/2026/may/13/pintard-non-committal-on-leadership-after-fnm-loss/).
- May 15, 2026 (The Nassau Guardian, "Pintard to stay on as leader"): The FNM's parliamentary caucus, Central Council and executive committee met May 13, 2026 and unanimously endorsed Pintard to remain as leader [Pintard to stay on as leader | News | thenassauguardian.com](https://www.thenassauguardian.com/news/pintard-to-stay-on-as-leader/article_16557999-14b6-46e8-bf1f-1e0c17982669.html).
- May 22, 2026 (Magnetic Media, "Pintard Stays On As FNM Leader After Heavy Election Loss"): Confirms Pintard was unanimously endorsed to continue as leader and was sworn in as Leader of the Opposition on May 18, 2026; a national convention/renewal process was planned for later but no removal occurred [Pintard Stays On As FNM Leader After Heavy Election Loss](https://magneticmediatv.com/2026/05/pintard-stays-on-as-fnm-leader-after-heavy-election-loss/).
- June 3, 2026 (The Nassau Guardian, "FNM opts out of 2026 convention"): The FNM Central Council overwhelmingly agreed to hold the next convention by October 2027, opting out of any 2026 convention; Pintard remained leader with no successful leadership challenge [FNM opts out of 2026 convention | News | thenassauguardian.com](https://www.thenassauguardian.com/news/fnm-opts-out-of-2026-convention/article_3ffed200-9f1b-4a0c-8cfe-628ab6d1a5b0.html).
- June 18, 2026 (The Tribune, "Pintard declares FNM 'unbowed' after defeat"): Pintard is still explicitly referred to as "FNM leader," discussing the party's future; the council had voted against an early convention, maintaining the current leadership [Pintard declares FNM 'unbowed' after defeat in the general election](https://www.tribune242.com/news/2026/jun/18/pintard-declares-fnm-unbowed-after-defeat-in-the-general-election/).

No credible source reported any resignation, removal, or vacancy of the Party Leader position between May 12 and June 30, 2026. Per the resolution criteria, absent any reported leadership change by June 30, 2026, the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-48. `501ff822-d537-55b7-956b-60ed0a6435cc`

- Present date: `2026-05-02 13:50:51.885470`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-05-31 00:00:00`

**Question**

Will Reform UK win more English local council seats than the Conservative Party in the 7 May 2026 local elections?

**Resolution criteria**

This question resolves **Yes** if Reform UK wins strictly more English local council seats than the Conservative Party in elections held on 7 May 2026 (or any rescheduled date for these specific elections). It resolves **No** if the Conservative Party wins an equal or greater number of seats.

**Definitions:**
- "English local council seats" means seats on district, borough, unitary, metropolitan borough, and London borough councils in England contested in the 2026 local elections cycle. This **excludes** directly elected mayoral positions, Police and Crime Commissioner elections, and any other positions not classified as council seats.
- Only seats won in elections held on or after 1 May 2026 are counted. Prior by-election results are excluded.
- [Reform UK](https://en.wikipedia.org/wiki/Reform_UK) and [Conservative Party](https://en.wikipedia.org/wiki/Conservative_Party_(UK)) refer to candidates standing under those party labels as registered with the [Electoral Commission](https://www.electoralcommission.org.uk/).

**Resolution source:** The final seat count as reported by [BBC News election results](https://www.bbc.co.uk/news/election) or [PA Media](https://www.pamediagroup.com/) election results data. If these sources disagree, the BBC's final published totals take precedence. Results are expected to be substantially complete by 9 May 2026 (23:59 UTC), with final counts available by 31 May 2026 (23:59 UTC).

**Pre-cutoff background**

The 2026 English local elections are scheduled for 7 May 2026 (polls open 07:00 UTC+1, close 22:00 UTC+1). A total of 5,066 council seats across 136 English local authorities are being contested [https://en.wikipedia.org/wiki/2026_United_Kingdom_local_elections](https://en.wikipedia.org/wiki/2026_United_Kingdom_local_elections).

**Current seat holdings (seats being defended):**
- Conservative Party: 4,180 seats [https://en.wikipedia.org/wiki/2026_United_Kingdom_local_elections](https://en.wikipedia.org/wiki/2026_United_Kingdom_local_elections)
- Reform UK: 986 seats [https://en.wikipedia.org/wiki/2026_United_Kingdom_local_elections](https://en.wikipedia.org/wiki/2026_United_Kingdom_local_elections)

**Key entities:**
- [Reform UK](https://en.wikipedia.org/wiki/Reform_UK): A right-wing populist party registered with the [Electoral Commission](https://www.electoralcommission.org.uk/).
- [Conservative Party](https://en.wikipedia.org/wiki/Conservative_Party_(UK)): The main centre-right party, currently in opposition following their 2024 general election defeat.

**Polling and projections:**
As of April 2026, projections suggest Reform UK is poised to win significantly more seats than the Conservatives. Britain Elects projects Reform UK at 1,689 seats versus Conservative at 754 seats; More in Common projects Reform UK at 1,515 versus Conservative at 507 [https://en.wikipedia.org/wiki/2026_United_Kingdom_local_elections](https://en.wikipedia.org/wiki/2026_United_Kingdom_local_elections). Elections Etc projects Reform UK making net gains of approximately +2,260 seats while the Conservatives face net losses of approximately -1,010 [Local election seat projections for 2026 - Elections Etc](https://electionsetc.com/2026/03/25/local-election-seat-projections-for-2026/). National polling places Reform at around 24% ahead of Conservatives at 21% [Electoral Calculus MRP, April 2026].

However, converting national polling into local council wins is notoriously difficult for newer parties without established local infrastructure. Reform UK is contesting many wards for the first time, and local elections often reward incumbency and name recognition. The gap between the two parties' projected seat totals is substantial but not beyond the range of polling error, particularly given Reform's untested local ground game. A reasonable forecast for "Yes" would fall in the 55-75% range, reflecting that projections consistently favour Reform but with significant uncertainty about turnout patterns and local factors.

**Exact later resolution packet**

The designated resolution source gives a final BBC News result for the relevant English council contests: on the BBC News page at https://www.bbc.com/news/election/2026/england/results, the totals under “England council results” are Reform UK 1,454 councillors and Conservative Party 801 councillors, with counting complete after 136 of 136 councils declared [Local election results 2026 in England - BBC News](https://www.bbc.com/news/election/2026/england/results). The same BBC page separately lists “Mayoral results,” so these councillor totals are for English local council seats rather than directly elected mayoral offices; no PCC totals are included in the cited council-seat totals [Local election results 2026 in England - BBC News](https://www.bbc.com/news/election/2026/england/results). Because 1,454 is strictly greater than 801, Reform UK won more English local council seats than the Conservative Party, so the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-49. `78660adc-2473-50fb-b817-5a1b7b1a74b1`

- Present date: `2026-05-12 18:49:22.157407`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the U.S. Supreme Court rule that 18 U.S.C. § 922(g)(3) is unconstitutional as applied to the respondent in United States v. Hemani?

**Resolution criteria**

This question resolves based on the official opinion of the U.S. Supreme Court in *United States v. Hemani* (No. 24-1234), as published on the [Supreme Court's official opinions page](https://www.supremecourt.gov/opinions). The ruling must be issued on or after May 10, 2026 (Eastern Time).

**Resolves YES** if the Supreme Court issues a majority opinion explicitly holding that [18 U.S.C. § 922(g)(3)](https://www.law.cornell.edu/uscode/text/18/922) is [unconstitutional as applied](https://en.wikipedia.org/wiki/As-applied_challenge) to the respondent (i.e., affirming the Fifth Circuit's judgment that the statute violates the Second Amendment as applied to Hemani's circumstances).

**Resolves NO** if any of the following occur by 11:59 PM Eastern Time on July 1, 2026:
1. The Court issues a majority opinion upholding the constitutionality of § 922(g)(3) as applied to the respondent (i.e., reversing the Fifth Circuit).
2. The Court vacates and remands the case without reaching the constitutional question of whether § 922(g)(3) is unconstitutional as applied (e.g., remanding on statutory interpretation, vagueness, or procedural grounds). A remand or vacatur that does not include an explicit holding that the statute is unconstitutional as applied resolves NO.
3. The Court disposes of the case on other grounds (e.g., mootness, lack of standing, or procedural dismissal) without reaching the merits of the as-applied constitutional challenge.

**Resolves AMBIGUOUS** if no opinion is issued in this case by 11:59 PM Eastern Time on July 1, 2026.

**Pre-cutoff background**

The U.S. Supreme Court is considering *United States v. Hemani* (Docket No. 24-1234), a case challenging the constitutionality of [18 U.S.C. § 922(g)(3)](https://www.law.cornell.edu/uscode/text/18/922), the federal statute that prohibits firearm possession by any person who "is an unlawful user of or addicted to any controlled substance."

Ali Danial Hemani was indicted in February 2023 for violating § 922(g)(3). He moved to dismiss, arguing the law was [unconstitutional as applied](https://en.wikipedia.org/wiki/As-applied_challenge) to him—meaning the statute, while potentially valid in other contexts, violates his Second Amendment rights in his specific circumstances as a marijuana user who was not impaired at the time of possession.

The Fifth Circuit held that § 922(g)(3) is unconstitutional as applied to individuals absent proof of impairment at the moment of firearm possession [Supreme Court Grants Review in United States v. Hemani - Dentons](https://www.dentons.com/en/insights/alerts/2025/october/27/supreme-court-grants-review-in-united-states). This means the government cannot prosecute someone for firearm possession based solely on habitual drug use without showing actual impairment when the person possessed the firearm.

The Supreme Court granted certiorari on October 20, 2025, and heard oral arguments on March 2, 2026 [United States v. Hemani (24-1234) | SCOTUSblog](https://www.scotusblog.com/cases/united-states-v-hemani/). The question presented is whether 18 U.S.C. § 922(g)(3) violates the Second Amendment as applied to the respondent [United States v. Hemani (24-1234) | SCOTUSblog](https://www.scotusblog.com/cases/united-states-v-hemani/). Reports from oral argument suggest the Court appeared skeptical of the gun ban for drug users, though the government has multiple arguments for upholding the statute under the history-and-tradition framework established in *New York State Rifle & Pistol Ass'n v. Bruen* (2022) and *United States v. Rahimi* (2024). The opinion is expected before the end of the current Supreme Court term in late June 2026 [United States v. Hemani (24-1234) | SCOTUSblog](https://www.scotusblog.com/cases/united-states-v-hemani/).

**Exact later resolution packet**

The question resolves YES.

The U.S. Supreme Court issued its opinion in *United States v. Hemani* (No. 24-1234) on June 18, 2026, which falls within the required resolution window (on or after May 10, 2026 ET, and before 11:59 PM ET on July 1, 2026).

Key facts confirmed from the official opinion published on supremecourt.gov (https://www.supremecourt.gov/opinions/25pdf/24-1234_g2bh.pdf):
- The Court held: "The government's prosecution of Mr. Hemani under §922(g)(3)'s unlawful user provision is inconsistent with the Second Amendment." [47a532]
- The disposition was: "The judgment of the Fifth Circuit is affirmed." [47a532]
- The opinion was delivered by Justice Gorsuch, joined by Roberts, C.J., and Thomas, Sotomayor, Kavanaugh, Barrett, and Jackson, JJ. (a majority; the case was decided 9-0). [47a532]

This is precisely the scenario the resolution criteria specify for YES: the Supreme Court issued a majority opinion affirming the Fifth Circuit's judgment that § 922(g)(3) is unconstitutional as applied to the respondent (Hemani's circumstances as a marijuana user without proof of impairment at the time of possession). SCOTUSblog's analysis confirms this was an as-applied constitutional holding in the defendant's favor, not a remand or disposition on non-constitutional grounds. [14baa2]

This is NOT any of the NO scenarios: it was not a reversal, not a vacatur/remand without a constitutional holding, and not a procedural dismissal. It is also not AMBIGUOUS, since a merits opinion was issued well before the July 1, 2026 deadline.

The opinion is a majority opinion published on the official Supreme Court opinions page. Direct URL to the opinion: https://www.supremecourt.gov/opinions/25pdf/24-1234_g2bh.pdf (linked from https://www.supremecourt.gov/opinions).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-50. `c8a9c650-c3b9-5b07-ad24-38e7f03e1f31`

- Present date: `2026-05-03 05:37:28.566778`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-07T00:00:00`

**Question**

Will the China Coast Guard conduct 4 or more incursions into Taiwan's restricted or prohibited waters during May 2026?

**Resolution criteria**

This question resolves **Yes** if 4 or more distinct CCG incursion events into Taiwan's restricted or prohibited waters are recorded between 00:00 UTC May 1, 2026 and 23:59 UTC May 31, 2026. It resolves **No** otherwise.

**Definitions:**

- **"China Coast Guard (CCG) vessel"**: Any vessel bearing official China Coast Guard hull markings (typically prefixed "CCG" followed by a number) or identified as a CCG vessel by Taiwan's Coast Guard Administration (CGA) in official statements.

- **"Taiwan's restricted or prohibited waters"**: The designated "restricted waters" (限制水域) and "prohibited waters" (禁止水域) maintained by Taiwan around its outlying islands, including Kinmen (Jinmen), Matsu, Wuqiu, and Dongsha (Pratas), as referenced in CGA announcements. These are functionally equivalent to territorial waters but are specific regulatory zones established by Taiwan's authorities.

- **"Incursion"**: Any physical entry by one or more CCG vessels into the above-defined restricted or prohibited waters, as reported by official Taiwanese government sources. Each separately reported event counts as one incursion, even if multiple vessels are involved in a single event. Multiple incursions on the same day each count separately if reported as distinct events.

**Resolution source**: The primary resolution source is official reporting from the Taiwan Coast Guard Administration (CGA) (https://www.cga.gov.tw/GipOpen/wSite/mp?mp=eng) or the Ocean Affairs Council (OAC). The Taiwan Security Monitor's China Coast Guard Incident Tracker (https://tsm.schar.gmu.edu/trackers/china-coast-guard-incident-tracker/) may be used as a supplementary aggregation source. Third-party media reports alone are insufficient unless no official Taiwanese government source is available, in which case credible media reports (e.g., Reuters, AP, Taipei Times, TaiwanPlus) may be used.

**Pre-cutoff background**

The China Coast Guard (CCG) has conducted regular incursions into waters designated as "restricted" or "prohibited" by Taiwan around its outlying islands, particularly Kinmen, Matsu, and Dongsha (Pratas). These incursions represent a form of maritime gray-zone pressure aimed at eroding Taiwan's sovereignty claims. Taiwan does not claim standard territorial seas around Kinmen due to its proximity to mainland China (~2 miles), but maintains functionally equivalent "prohibited" and "restricted" water zones [https://understandingwar.org/research/china-taiwan/china-taiwan-update-april-3-2026/](https://understandingwar.org/research/china-taiwan/china-taiwan-update-april-3-2026/).

As of May 1, 2026, the Taiwan Security Monitor's China Coast Guard Incident Tracker (https://tsm.schar.gmu.edu/trackers/china-coast-guard-incident-tracker/) has recorded 10 CCG incursion incidents in 2026: 2 in February, 5 in March, and 3 in April [China Coast Guard Incident Tracker - Taiwan Security Monitor](https://tsm.schar.gmu.edu/trackers/china-coast-guard-incident-tracker/). In 2025, there were 44 CCG incursions into Kinmen's restricted and prohibited waters for the full year. The monthly frequency in early 2026 has averaged approximately 3–4 incursions per month, though with notable variation (ranging from 2 to 5).

CCG vessels involved are typically identified by hull numbers (e.g., CCG14608, CCG14527) and are officially designated as China Coast Guard vessels by Taiwan's Coast Guard Administration (CGA). Incursions are publicly announced by the CGA via press releases on its official website (https://www.cga.gov.tw/GipOpen/wSite/mp?mp=eng) and aggregated by the Taiwan Security Monitor tracker.

**Exact later resolution packet**

RESOLUTION: YES (resolves 1).

The question resolves YES if 4 or more distinct China Coast Guard (CCG) incursion events into Taiwan's restricted or prohibited waters (around Kinmen, Matsu, Wuqiu, or Dongsha) occurred between 00:00 UTC May 1, 2026 and 23:59 UTC May 31, 2026.

PRIMARY EVIDENCE — Taiwan Security Monitor's China Coast Guard Incident Tracker (https://tsm.schar.gmu.edu/trackers/china-coast-guard-incident-tracker/), the aggregator explicitly endorsed by the question and which draws on CGA releases. Two independent queries of the tracker returned the same set of May 2026 incursion events into restricted/prohibited waters [https://tsm.schar.gmu.edu/trackers/china-coast-guard-incident-tracker/](https://tsm.schar.gmu.edu/trackers/china-coast-guard-incident-tracker/) [https://tsm.schar.gmu.edu/trackers/china-coast-guard-incident-tracker/](https://tsm.schar.gmu.edu/trackers/china-coast-guard-incident-tracker/):
1. May 7, 2026 — Kinmen — CCG vessels 14606, 14530, 14609, 14531
2. May 21, 2026 — Kinmen — CCG vessels 14605, 14531, 14606, 14530
3. May 23, 2026 — Dongsha — CCG vessel 3501
4. May 26, 2026 — Kinmen — CCG vessels 14606, 14530, 14609, 14531
5. May 27, 2026 — Kinmen — CCG vessels 14531, 14606, 14530, 14602

That is 5 distinct incursion events, comfortably exceeding the threshold of 4. Even setting aside the Dongsha event, the four Kinmen incursions (May 7, 21, 26, 27) alone satisfy the ≥4 requirement.

CORROBORATION FROM OFFICIAL TAIWANESE SOURCES / CGA (海巡署) STATEMENTS reported in media (each cites CGA press releases):
- May 21: CNA (Central News Agency): "4艘中國海警船今天侵擾金門水域...海巡署" — https://www.cna.com.tw/news/acn/202605210308.aspx (confirms the May 21 Kinmen incursion; four China Coast Guard vessels).
- May 26 & May 27: Facebook repost of CGA press release: "民國115年(2026)5月26日中國海警侵擾金門海域...中國海警於5月27日再度侵擾金門海域" — https://www.facebook.com/m0069/posts/1580627160734986/ (confirms two separate Kinmen incursions on May 26 and May 27, each with CGA news release).
- Early May (fishing-moratorium context, consistent with the May 7 event): Yahoo News reproducing CGA 金馬澎分署 statement: "中國4海警船闖金門限制水域...中國5月1日起實施2026年海洋伏季休漁措施" — https://tw.news.yahoo.com/中國4海警船闖金門限制水域-海巡署-製造執法巡查假象-121100283.html

VESSEL IDENTIFICATION: All May Kinmen events involve vessels explicitly described as "中國海警船" (China Coast Guard ships) with hull numbers in the 14xxx series (e.g., 14602, 14530, 14606, 14531), which are CCG hull markings — not Maritime Safety Administration (MSA / 海巡 "Haixun") vessels. The tracker distinguishes MSA "Haixun" entries (e.g., the June 7 "Haixun 06/08/09" event) from CCG hull-numbered vessels [https://tsm.schar.gmu.edu/trackers/china-coast-guard-incident-tracker/](https://tsm.schar.gmu.edu/trackers/china-coast-guard-incident-tracker/); the qualifying May events are all CCG.

COUNTING RULE: Each event is counted once even though multiple CCG vessels were involved, consistent with the resolution criteria. This yields 5 distinct incursions (or a minimum of 4 counting Kinmen only).

CONCLUSION: With at least 4 (in fact 5) distinct CCG incursions into Taiwan's restricted/prohibited waters in May 2026, confirmed by the endorsed TSM tracker and corroborated by CGA-sourced reporting, the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-51. `d22bd1f1-7ea7-54ff-90fc-be0f01aee972`

- Present date: `2026-05-29 03:18:03.116878`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the U.S. Supreme Court rule in favor of petitioner Terry Pitchford in Pitchford v. Cain (24-7351) by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the U.S. Supreme Court issues an opinion on or after May 12, 2026, and on or before July 1, 2026 (by 11:59 PM UTC), that **reverses, vacates, or remands** the judgment of the lower court (the U.S. Court of Appeals for the Fifth Circuit / Mississippi Supreme Court) in *Pitchford v. Cain*, No. 24-7351. "Ruling in favor of the petitioner" means any disposition that does not affirm the lower court's judgment — including a reversal, vacatur, or remand for further proceedings.

This question resolves **No** if:
- The Court **affirms** the lower court's judgment, OR
- The case is **dismissed** (e.g., as improvidently granted) without a ruling on the merits in Pitchford's favor, OR
- No opinion is issued by July 1, 2026 (11:59 PM UTC).

**Resolution source:** The official U.S. Supreme Court opinions page at https://www.supremecourt.gov/opinions/slipopinion/25. The syllabus and disposition line of the slip opinion will determine resolution.

**Pre-cutoff background**

Terry Pitchford is a death-row inmate in Mississippi who was convicted of capital murder. During jury selection at his trial, prosecutors used [peremptory strikes](https://www.law.cornell.edu/wex/peremptory_challenge) to remove four Black jurors. Pitchford's defense counsel raised a [Batson challenge](https://en.wikipedia.org/wiki/Batson_v._Kentucky) — a constitutional objection under *Batson v. Kentucky* (1986), which prohibits excluding jurors based on race. The trial court found a prima facie case of discrimination and required the prosecution to offer race-neutral reasons, but the Mississippi Supreme Court later held that Pitchford had waived his right to rebut those reasons [https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/24-7351.html](https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/24-7351.html).

The [petitioner](https://www.law.cornell.edu/wex/petitioner) (the party asking the Supreme Court to review the case) argues that this waiver finding was unreasonable. The case reached the U.S. Supreme Court via a [writ of certiorari](https://www.law.cornell.edu/wex/certiorari), and the question presented is whether the Mississippi Supreme Court unreasonably determined — under the deferential standard of the [Antiterrorism and Effective Death Penalty Act (AEDPA)](https://en.wikipedia.org/wiki/Antiterrorism_and_Effective_Death_Penalty_Act_of_1996), 28 U.S.C. §2254(d) — that Pitchford waived his right to rebut the prosecutor's asserted race-neutral reasons for striking four Black jurors [https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/24-7351.html](https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/24-7351.html).

Oral arguments were held on **March 31, 2026** [https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/24-7351.html](https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/24-7351.html). According to SCOTUSblog's recap, a majority of justices appeared sympathetic to Pitchford during argument, with Justices Kavanaugh, Jackson, Gorsuch, and Barrett signaling support for the petitioner, while Justices Alito and Thomas expressed skepticism [https://www.scotusblog.com/2026/04/court-appears-sympathetic-to-death-row-inmates-attempt-to-challenge-racial-discrimination-in-jury-selection/](https://www.scotusblog.com/2026/04/court-appears-sympathetic-to-death-row-inmates-attempt-to-challenge-racial-discrimination-in-jury-selection/). As of May 13, 2026, the Court has not yet issued an opinion [https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/24-7351.html](https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/24-7351.html). Supreme Court opinions for argued cases are typically released by late June or early July.

**Case docket:** https://www.supremecourt.gov/docket/docketfiles/html/public/24-7351.html
**SCOTUSblog case page:** https://www.scotusblog.com/cases/pitchford-v-cain/

**Exact later resolution packet**

The question resolves YES.

**Resolution criteria:** The question resolves YES if the U.S. Supreme Court issues an opinion on or after May 12, 2026 and on or before July 1, 2026 (11:59 PM UTC) that reverses, vacates, or remands the judgment of the lower court in Pitchford v. Cain, No. 24-7351.

**Evidence:**
- The U.S. Supreme Court issued its opinion in Pitchford v. Cain, No. 24-7351, on **May 28, 2026** — squarely within the required resolution window (May 12 – July 1, 2026). The official slip opinion (https://www.supremecourt.gov/opinions/25pdf/24-7351_jiel.pdf) states in its syllabus and final paragraph: "**126 F. 4th 422, reversed and remanded.**" [[PDF] 24-7351 Pitchford v. Cain (05/28/2026) - Supreme Court](https://www.supremecourt.gov/opinions/25pdf/24-7351_jiel.pdf)
- The Court held, by a 5-4 vote, that the Mississippi Supreme Court unreasonably applied clearly established precedent and unreasonably determined that Pitchford waived his right to rebut the prosecutor's asserted race-neutral reasons. The majority opinion was authored by Justice Kavanaugh; Justice Gorsuch filed a dissent joined by Justices Thomas, Alito, and Barrett. [[PDF] 24-7351 Pitchford v. Cain (05/28/2026) - Supreme Court](https://www.supremecourt.gov/opinions/25pdf/24-7351_jiel.pdf)
- This is corroborated by SCOTUSblog's case page ("Reversed and remanded, 5-4, in an opinion by Brett Kavanaugh on May 28, 2026"), Ballotpedia's answer box ("The Court reversed and remanded the decision of the United States Court of Appeals for the Fifth Circuit in a 5-4 ruling"), and the Constitution Annotated ("The Supreme Court reversed the Fifth Circuit's judgment").

**Analysis:** A "reverse and remand" disposition is precisely the type of ruling in the petitioner's favor that the resolution criteria specify counts as YES ("any disposition that does not affirm the lower court's judgment — including a reversal, vacatur, or remand"). The opinion is not a dismissal as improvidently granted (DIG), and it was issued before the July 1, 2026 deadline. Even though it is a partial victory (remand for further proceedings), the criteria explicitly count reversals/remands as YES.

**Direct URL to official slip opinion:** https://www.supremecourt.gov/opinions/25pdf/24-7351_jiel.pdf

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-52. `642ce768-5920-5773-aee8-ba40784dcf3b`

- Present date: `2026-05-13 22:45:26.411254`
- Source cutoff boundary: `2026-05-14` (encodes end of UTC day `2026-05-13`)
- Expected resolution: `2026-06-06T00:00:00`

**Question**

Will Serbian President Aleksandar Vučić physically attend the EU-Western Balkans Summit in Tivat on June 5, 2026?

**Resolution criteria**

This question resolves **Yes** if Aleksandar Vučić, in his capacity as President of Serbia, is physically present at any official session of the EU-Western Balkans Summit in Tivat, Montenegro, on June 5, 2026 (CET/CEST timezone). "Official session" means the plenary meeting or the working lunch as described in the summit program.

This question resolves **No** if:
- Vučić does not attend the summit at all, or
- Serbia sends a different representative (e.g., Prime Minister, Foreign Minister, or other official) instead, or
- The summit is cancelled or postponed beyond June 30, 2026.

If the summit is rescheduled to a different date before June 30, 2026, Vučić's physical attendance at the rescheduled summit counts for resolution.

**Resolution sources:** The official European Council summit page (https://www.consilium.europa.eu/en/meetings/international-summit/2026/06/05/), the official summit website (https://www.euwb26.me/), or credible international news reporting from Reuters, AP, Politico Europe, or European Western Balkans (https://europeanwesternbalkans.com/).

**Pre-cutoff background**

The EU-Western Balkans Summit is scheduled for June 5, 2026, in Tivat, Montenegro, hosted by Montenegrin President Jakov Milatović and European Council President António Costa [Milatović and Costa invite leaders to the EU-Western Balkans ...](https://europeanwesternbalkans.com/2026/04/28/milatovic-and-costa-invite-leaders-to-the-eu-western-balkans-summit-in-tivat/). The program includes a plenary meeting and a working lunch [Milatović and Costa invite leaders to the EU-Western Balkans ...](https://europeanwesternbalkans.com/2026/04/28/milatovic-and-costa-invite-leaders-to-the-eu-western-balkans-summit-in-tivat/).

Serbian President Aleksandar Vučić has a notable history of boycotting these summits. He boycotted the December 2022 EU-Western Balkans Summit in Tirana, citing frustration with EU institutions. More recently, he boycotted the December 2025 EU-Western Balkans Summit in Brussels, announcing that no Serbian official would represent Serbia at the event. This was widely seen as deepening the rift between Belgrade and Brussels.

Serbia's relationship with the EU remains strained due to several factors: the unresolved Serbia-Kosovo normalization dialogue, ongoing large-scale student protests inside Serbia, Vučić's close ties with Russia, and broader geopolitical tensions in the Western Balkans. NATO Secretary General Rutte has publicly noted "actors trying to destabilize the Western Balkans" [Milatović and Costa invite leaders to the EU-Western Balkans ...](https://europeanwesternbalkans.com/2026/04/28/milatovic-and-costa-invite-leaders-to-the-eu-western-balkans-summit-in-tivat/). The Atlantic Council has flagged 2026 as a pivotal year for the region, with Vučić hinting at early elections.

Given that Vučić boycotted the two most recent summits (2022 and 2025) but attended others (e.g., the 2023 Brussels crisis meeting and the 2024 summit), his attendance at the Tivat summit is genuinely uncertain and would carry significant diplomatic weight.

**Exact later resolution packet**

The question resolves YES: Serbian President Aleksandar Vučić physically attended the EU-Western Balkans Summit in Tivat, Montenegro on June 5, 2026, in his capacity as President of Serbia.

Timeline and evidence:
- The summit took place as scheduled on June 5, 2026 in Tivat (not cancelled, postponed, or rescheduled), confirmed by the official European Council summit page and multiple outlets. This satisfies the antecedent (summit occurred before June 30, 2026). The official Council page describes "EU and Western Balkans leaders met in Tivat, Montenegro" [d0fd70].
- Ahead of the summit, Serbia's security agency (BIA) advised Vučić not to travel over security concerns; Parliament Speaker Ana Brnabić said he planned to travel anyway (Reuters) [0ed0b3].
- Balkan Insight (headline: "Serbia President Attends Summit in Montenegro Despite Intelligence Warnings") reports that "Serbian President Aleksandar Vučić arrived in Tivat, Montenegro on Thursday, to attend the EU-Western Balkans Summit," quoting him: "I am going to Montenegro because it is very important for me to represent Serbia there." This confirms his personal attendance (President himself, not a substitute official) [51bab6].
- European Western Balkans (a designated resolution source) live coverage confirms Vučić was in Tivat for the summit and met with Commission President von der Leyen, Council President Costa, French President Macron, and German Chancellor Merz [d5b677].
- The Western Balkans (Serbia's perspective analysis) states: "During the European Union–Western Balkans Summit held in Tivat, Montenegro, Serbian President Aleksandar Vučić held a dedicated press conference outlining Serbia's positions on the summit," and presented Serbia's reform efforts and held meetings with European leaders during the summit — confirming his active, physical participation at the event [68bf2b].
- The official EU Council TV News channel posted "Arrival and doorstep by Aleksandar VUČIĆ, President of Serbia, at the #EUWesternBalkans Summit taking place on 5 June 2026 in #Tivat" (x.com/EUCouncilTVNews), corroborating his physical arrival at the summit venue.

Official session criterion: The summit program (euwb26.me) included a Plenary Session (12:00) as the core official session; all attending Western Balkan leaders, including Vučić, participated. His arrival/doorstep at the venue, participation among the summit leaders, meetings with the top EU leaders during the summit, and his summit press conference collectively confirm his physical presence at the official session(s) [68bf2b, d5b677].

Distinguishing personal vs. substitute attendance: All sources confirm Vučić himself attended in person as President — not the Prime Minister, Foreign Minister, or another official. This is a notable reversal from his December 2025 Brussels boycott [51bab6].

Note on non-confirming queries: The AP article [e5bdba] and the official Council page [d0fd70] focused on Montenegro's accession and did not enumerate Vučić by name; this is absence of mention, not evidence of absence, and is outweighed by the explicit confirmations above.

Sources (URLs):
- https://europeanwesternbalkans.com/2026/06/05/eu-western-balkans-summit-in-tivat-live/ [d5b677]
- https://balkaninsight.com/2026/06/04/serbia-president-attends-summit-in-montenegro-despite-intelligence-warnings/bi/ [51bab6]
- https://thewesternbalkans.com/the-eu-western-balkans-summit-in-tivat-serbias-perspective/ [68bf2b]
- https://www.reuters.com/world/serbias-security-agency-advises-vucic-not-travel-eu-summit-montenegro-2026-06-04/ [0ed0b3]
- https://www.consilium.europa.eu/en/meetings/international-summit/2026/06/05/ [d0fd70]
- Official EU Council TV News (X/Twitter): https://x.com/EUCouncilTVNews/status/2062844003830186484 (arrival & doorstep by Vučić at the Tivat summit)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-53. `5e0b29a5-8ee9-5e46-b208-444af77252c6`

- Present date: `2026-05-16 06:17:06.419894`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-06-15T00:00:00`

**Question**

Will Pakistan's FY2026-27 Finance Bill include new measures specifically targeting retailer taxation?

**Resolution criteria**

This question resolves YES if the official FY2026-27 Federal Budget documents or the accompanying Finance Bill 2026, as presented to Pakistan's National Assembly and published on the Ministry of Finance website (https://www.finance.gov.pk/budget_wing.html) or the Federal Board of Revenue website (https://www.fbr.gov.pk/), contain one or more new measures announced or introduced on or after May 12, 2026, that specifically target the taxation of retailers.

Definitions:
- "Retailers" means businesses engaged in selling goods directly to end consumers, as defined in Pakistan's Sales Tax Act 1990 or Income Tax Ordinance 2001. This includes but is not limited to shopkeepers, store owners, and traders operating retail establishments.
- "New measures" means any of the following that were not already in force as of May 11, 2026: (a) a new tax rate, surcharge, or levy specifically applicable to retailers; (b) a new mandatory registration, POS integration, or digital invoicing requirement expanding coverage to a category of retailers not previously covered; (c) a new asset-based or turnover-based tax specifically for retailers; or (d) new penalties or enforcement mechanisms specifically targeting retailer tax compliance.
- Mere continuation or restatement of existing measures (such as the current POS integration program for tier-one retailers) does not count.

The measures must be contained within the official FY2026-27 Federal Budget documents or the Finance Bill 2026.

If the budget is not presented by July 1, 2026, the question resolves NO.

Resolution source: Official budget documents at https://www.finance.gov.pk/budget_wing.html or https://www.fbr.gov.pk/, supplemented by credible reporting from Dawn (https://www.dawn.com/), The News International, or Reuters.

**Pre-cutoff background**

Pakistan has struggled to bring its retail sector into the formal tax net, a key condition of its IMF Extended Fund Facility program. The IMF's third review (completed May 2026) emphasized "broadening the tax net and improving compliance" as a fiscal priority.

The previous "Tajir Dost Scheme" (TDS), launched to register and tax shopkeepers, was scrapped in March 2025 after tax revenue from retailers, wholesalers, and Associations of Persons exceeded Rs400 billion, far surpassing the initial Rs50 billion projection [IMF agrees to scrap Tajir Dost Scheme as FBR surpasses tax ...](https://profit.pakistantoday.com.pk/2025/03/15/imf-agrees-to-scrap-tajir-dost-scheme-as-fbr-surpasses-tax-collection-target-report/). Following TDS's cancellation, the FBR shifted toward electronic monitoring and digital compliance.

As of early 2026, the FBR has integrated 12,861 large retailers into its Point of Sale (POS) system for real-time sales monitoring, with plans to expand to 40,000 tier-one retailers. Businesses with annual turnover exceeding Rs50 crore are being integrated into a digital invoicing system. Penalties for non-compliance range from Rs500,000 to Rs3 million or closure of business operations [Another IMF Condition Met as FBR Expands Retail Tax Network](https://propakistani.pk/2026/03/24/another-imf-condition-met-as-fbr-expands-retail-tax-network/).

In March 2026, the IMF pressed Pakistan to introduce an asset-based tax system for traders outside the tax net, moving beyond previous location- or shop-size-based approaches. The FBR expressed reservations, arguing that many traders do not file returns, making asset determination difficult [IMF presses Pakistan to bring traders into tax net through asset ...](https://profit.pakistantoday.com.pk/2026/03/11/imf-presses-pakistan-to-bring-traders-into-tax-net-through-asset-based-levy/).

The FY2026-27 federal budget is expected to be presented in the first week of June 2026 (Pakistan Time, UTC+5). The official budget documents are published at https://www.finance.gov.pk/budget_wing.html and the FBR website at https://www.fbr.gov.pk/.

**Exact later resolution packet**

RESOLUTION: YES (1).

STEP 1 — Antecedent (budget presented by July 1, 2026): The FY2026-27 Federal Budget was presented to Pakistan's National Assembly by Finance Minister Muhammad Aurangzeb on June 12, 2026, well before the July 1, 2026 cutoff. Dawn confirms the budget (Rs18.8 trillion outlay) was presented for FY2026-27 [fbada8]. The Finance Bill 2026 is published on the official FBR site (fbr.gov.pk/Budget2026-27/FinanceBill/Finance-Bill-2026.pdf) and Ministry of Finance site. The condition triggering an automatic NO (budget not presented by July 1) therefore does NOT apply.

STEP 2 — New measures specifically targeting retailers (must be new as of May 12, 2026, and specific to retailers). The Finance Bill 2026 contains MULTIPLE such measures, satisfying several of the four "new measure" categories:

(a) NEW TAX RATE/LEVY ON RETAILERS: A new fixed/minimum tax of 1% of sales/turnover is imposed on small retail shops with annual turnover up to Rs200 million (~3.5 million retailers). Reuters (June 5, 2026) reported "Pakistan will impose a 1% income tax on small retail shops with a sales turnover up to 200 million rupees a year," specifically targeting retailers [57fe52]. PwC's Tax Memorandum on the Finance Bill 2026 confirms this fixed tax regime for small retailers at 1% of sales, replacing the scrapped Tajir Dost Scheme [805af2]. This is a NEW turnover-based tax specific to retailers (categories (a) and (c)).

(b) EXPANDED REGISTRATION/POS/INVOICING COVERAGE: The FBR Salient Features for Budget 2026-27 list "Streamlining of definition tier-1 retailers. Inclusion of retailer having two hundred million or more annual turnover, in the category of tier-1 retailer" and "Broadening of special procedure for small traders and shopkeepers" via section 99B [0e3fa4]. PwC confirms the Tier-1 retailer definition is amended to include wholesalers-cum-retailers and retailers with turnover exceeding Rs200 million [805af2]. The Bill also mandates that retailers issue invoices carrying the Board's unique verifiable FBR numbers for taxable supplies, exempt supplies and advance receipts — a new digital-invoicing requirement [7ef83f, 805af2].

(d) NEW PENALTIES/ENFORCEMENT: The Bill introduces new penalties for non-integration with FBR electronic systems (e.g., Rs1 million first default, Rs5 million subsequent defaults, plus sealing/blacklisting of premises) and new offenses relating to non-integration and fictitious invoices, with IR Commissioner empowered to seal Tier-1 retailers' outlets [7ef83f, 805af2].

These are documented as "proposed amendments" in the Finance Bill 2026 (not mere restatements of the pre-existing tier-one POS program), and all were announced/introduced with the June 12, 2026 budget — after the May 12, 2026 threshold.

CAVEAT: One query of Dawn's budget-day overview article (a summary of the finance minister's speech) found no explicit retailer measures [fbada8], but that article only summarized the speech's headline themes, not the detailed Finance Bill provisions. The authoritative Finance Bill/FBR Salient Features and independent analyses (PwC, EY, Reuters) all confirm the specific new retailer measures.

Because the budget was presented before July 1, 2026, and the Finance Bill 2026 contains multiple new measures specifically targeting retailer taxation (new 1% turnover tax on retailers, expanded tier-1 definition, mandatory FBR-number invoicing, and new penalties), the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-54. `f843833c-b0dd-515a-954d-2d466abcf0ab`

- Present date: `2026-05-03 13:01:39.721556`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the EU Council and Parliament reach a political agreement to delay the EU AI Act's August 2, 2026 high-risk AI system compliance deadline before June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after April 30, 2026 and before June 1, 2026 (23:59 UTC), a formal political agreement (i.e., a provisional trilogue agreement or formal legislative adoption) is reached between the European Parliament and the Council of the EU to delay the August 2, 2026 compliance deadline for high-risk AI systems as defined under Annex III of the EU AI Act (https://artificialintelligenceact.eu/annex/3/).

A mere proposal or negotiating mandate does not suffice; the agreement must be a confirmed political deal between co-legislators (Parliament and Council), as typically announced via a joint press statement or individual press releases.

The question resolves **No** if no such agreement is reached before June 1, 2026.

**Verification sources:** Official press releases from the Council of the EU (https://www.consilium.europa.eu/en/press/press-releases/), the European Parliament Press Room (https://www.europarl.europa.eu/news/en/press-room), or publication in the Official Journal of the EU via EUR-Lex (https://eur-lex.europa.eu/oj/direct-access.html).

**Pre-cutoff background**

The EU AI Act (Regulation 2024/1689) established August 2, 2026 as the compliance deadline for providers and deployers of high-risk AI systems classified under Annex III (https://artificialintelligenceact.eu/annex/3/), which covers areas such as biometric identification, critical infrastructure, employment, creditworthiness assessment, and law enforcement.

The European Commission missed its statutory February 2, 2026 deadline for publishing guidance on high-risk system classification under Article 6 [EU countries, lawmakers fail to reach deal on watered-down AI rules](https://www.reuters.com/sustainability/boards-policy-regulation/eu-countries-lawmakers-fail-reach-deal-watered-down-ai-rules-2026-04-29/). In November 2025, the Commission proposed the "Digital Omnibus on AI" package, which includes a provision to delay the Annex III high-risk compliance deadline. On March 13, 2026, the Council of the EU agreed on its negotiating mandate, proposing new application dates of December 2, 2027 for stand-alone high-risk AI systems and August 2, 2028 for high-risk AI systems embedded in products [Council agrees position to streamline rules on Artificial Intelligence](https://www.consilium.europa.eu/en/press/press-releases/2026/03/13/council-agrees-position-to-streamline-rules-on-artificial-intelligence/).

Trilogue negotiations between the Council and European Parliament began but failed to reach agreement on April 28, 2026 after 12 hours of talks, primarily due to disagreements over exemptions for industries already subject to sectoral regulations. The next round of negotiations is expected in mid-May 2026 [EU countries, lawmakers fail to reach deal on watered-down AI rules](https://www.reuters.com/sustainability/boards-policy-regulation/eu-countries-lawmakers-fail-reach-deal-watered-down-ai-rules-2026-04-29/). As of May 1, 2026, no political agreement has been reached, and the original August 2, 2026 deadline remains legally binding.

**Exact later resolution packet**

The question resolves YES. On May 7, 2026 — within the resolution window of April 30, 2026 to June 1, 2026 (23:59 UTC) — the Council of the EU and the European Parliament announced a provisional political agreement on targeted amendments to the EU AI Act (the "Digital Omnibus on AI"), which delays the compliance deadline for high-risk AI systems under Annex III.

Key evidence:
- The official Council of the EU press release dated May 7, 2026 ("Artificial Intelligence: Council and Parliament agree to simplify and streamline rules", https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/) announces the deal between the co-legislators, noting the provisions on high-risk AI systems due to enter into force on 2 August 2026.
- Reuters reported on May 7, 2026 that "EU governments and lawmakers agreed to delay rules on high-risk AI systems such as those involving biometrics or related to critical infrastructure and law enforcement to December 2, 2027, from a previous deadline of August 2 this year." [EU countries, lawmakers clinch provisional deal on watered-down ...](https://www.reuters.com/world/eu-countries-lawmakers-strike-provisional-deal-watered-down-ai-rules-2026-05-07/)
- Hogan Lovells confirms: "On May 7, 2026, the Council of the EU and the European Parliament announced their provisional agreement on targeted amendments to the EU AI Act," deferring standalone Annex III high-risk systems to December 2, 2027 and embedded high-risk systems to August 2, 2028 [EU legislators agree to delay for high-risk AI rules - Hogan Lovells](https://www.hoganlovells.com/en/publications/eu-legislators-agree-to-delay-for-highrisk-ai-rules).

This satisfies the resolution criteria: a provisional trilogue/political agreement between the co-legislators (Parliament and Council), specifically delaying the August 2, 2026 Annex III high-risk compliance deadline, reached within the specified window, and confirmed by an official source (the Council of the EU press room).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-55. `49b762aa-df15-56f0-8884-4ca7f5769565`

- Present date: `2026-05-02 19:02:26.963494`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the U.S. Department of Education publish a Notice Inviting Applications (NIA) referencing the 'Advancing Artificial Intelligence in Education' priority before June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, by 11:59 PM UTC on June 1, 2026, the U.S. Department of Education publishes at least one Notice Inviting Applications (NIA) for a discretionary grant competition that explicitly references the "Advancing Artificial Intelligence in Education" supplemental priority.

A "reference" to the priority means the NIA must do at least one of the following:
- Cite Federal Register Document Number 2026-07087 (the final rule establishing the priority); OR
- Use the exact phrase "Advancing Artificial Intelligence in Education" when listing applicable priorities.

The NIA's publication date (as shown on the Federal Register or Grants.gov) must be on or after May 13, 2026 (the effective date of the priority) and before June 1, 2026 (UTC).

**Resolution sources:**
- The [Federal Register](https://www.federalregister.gov/) (federalregister.gov), searching for Department of Education NIAs; OR
- The official [Grants.gov](https://www.grants.gov/) grant search tool for Department of Education discretionary grant opportunities.

If no qualifying NIA is found in either source by the deadline, the question resolves **No**.

**Pre-cutoff background**

On April 13, 2026, the U.S. Department of Education published a final rule in the Federal Register (Document Number 2026-07087) establishing a new Secretary's supplemental priority titled "Advancing Artificial Intelligence in Education" ([full text](https://www.federalregister.gov/documents/2026/04/13/2026-07087/final-priority-and-definitions-secretarys-supplemental-priority-and-definitions-on-advancing)) [https://www.federalregister.gov/documents/2026/04/13/2026-07087/final-priority-and-definitions-secretarys-supplemental-priority-and-definitions-on-advancing](https://www.federalregister.gov/documents/2026/04/13/2026-07087/final-priority-and-definitions-secretarys-supplemental-priority-and-definitions-on-advancing). The priority becomes effective on May 13, 2026 [https://www.federalregister.gov/documents/2026/04/13/2026-07087/final-priority-and-definitions-secretarys-supplemental-priority-and-definitions-on-advancing](https://www.federalregister.gov/documents/2026/04/13/2026-07087/final-priority-and-definitions-secretarys-supplemental-priority-and-definitions-on-advancing).

The priority enables the Secretary to incorporate AI-related objectives—such as AI literacy integration, educator professional development, and ethical AI use in education—into discretionary grant competitions [https://www.federalregister.gov/documents/2026/04/13/2026-07087/final-priority-and-definitions-secretarys-supplemental-priority-and-definitions-on-advancing](https://www.federalregister.gov/documents/2026/04/13/2026-07087/final-priority-and-definitions-secretarys-supplemental-priority-and-definitions-on-advancing). It defines key terms including "Artificial intelligence (AI)" (per 15 U.S.C. 9401(3)), "AI literacy," and "Computer science" [https://www.federalregister.gov/documents/2026/04/13/2026-07087/final-priority-and-definitions-secretarys-supplemental-priority-and-definitions-on-advancing](https://www.federalregister.gov/documents/2026/04/13/2026-07087/final-priority-and-definitions-secretarys-supplemental-priority-and-definitions-on-advancing).

Critically, establishing a supplemental priority does not automatically trigger any grant competition. The Department must separately publish a [Notice Inviting Applications (NIA)](https://www2.ed.gov/fund/grant/apply/appforms/appforms.html)—a Federal Register notice that opens a specific discretionary grant competition—that incorporates the priority as an absolute, competitive preference, or invitational priority.

As of May 1, 2026, no NIA referencing this priority has been published. The priority's effective date of May 13, 2026, leaves only approximately 18 days before the June 1, 2026, deadline. Historical practice suggests NIAs can take weeks to months to develop after a priority becomes effective, though the Department may have prepared competitions in advance of the effective date.

**Exact later resolution packet**

The question resolves YES because the U.S. Department of Education published at least one qualifying Notice Inviting Applications (NIA) within the resolution window.

Specifically, the Federal Register notice "Notice Announcing Strengthening Institutions Program Competition" (Federal Register Document Number 2026-10623, published May 28, 2026, at https://www.federalregister.gov/documents/2026/05/28/2026-10623/notice-announcing-strenthening-institutions-program-competition) is a Notice Inviting Applications soliciting applications for the FY 2026 Strengthening Institutions Program (ALN 84.031A). It explicitly lists "Advancing Artificial Intelligence in Education" as one of its priorities (Competitive Preference Priority 3), satisfying the requirement to use the exact phrase when listing applicable priorities [ea70a9].

The corresponding ED application notice for the Strengthening Institutions Program (84.031A) confirms this: "Competitive Preference Priority 3 is from the Final Priority and Definitions — Secretary's Supplemental Priority and Definitions on Advancing Artificial Intelligence in Education, published April 13, 2026 (91 FR 18774)" — referencing the priority by its exact title [4ea025].

Timing: The notice was published May 28, 2026, which is on or after the priority's May 13, 2026 effective date and before the June 1, 2026 (UTC) deadline [ea70a9].

Source: The evidence comes from federalregister.gov / its official govinfo.gov mirror (the resolution source specified by the question). Both the document type (NIA), the explicit reference to "Advancing Artificial Intelligence in Education," and the publication date within the required window are satisfied.

Note: Earlier broad-search summaries that suggested NO had incomplete listings and did not capture the Strengthening Institutions Program NIA's priority list [6f1c7b, 031138, 5b52d4]; the detailed reading of the actual notice text confirms the AI priority is referenced [ea70a9, 4ea025].

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-56. `19c51624-fb6a-5f03-b5b0-0362c9202cd1`

- Present date: `2026-05-12 15:36:26.891604`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the jury in the Iskander v. Grossman civil trial find defendant Scott Erickson liable for the deaths of the Iskander brothers?

**Resolution criteria**

This question resolves **Yes** if, on or after May 10, 2026 (12:00 AM UTC), a jury verdict, a judge's order, or a settlement in the Iskander v. Grossman civil trial (Los Angeles County Superior Court) finds or establishes that Scott Erickson is [liable](https://www.law.cornell.edu/wex/liability) for the wrongful deaths of Mark and/or Jacob Iskander. Specifically:

- **Jury verdict**: If the jury returns a verdict finding Erickson liable (i.e., assigning him any non-zero percentage of fault) for the wrongful death of either or both Iskander brothers, this resolves **Yes**.
- **Judge's order**: If the judge enters a directed verdict or judgment as a matter of law finding Erickson liable, this resolves **Yes**.
- **Settlement**: If Erickson enters into a settlement with the plaintiffs that includes an admission of liability or a payment of damages related to the wrongful deaths, this resolves **Yes**. A settlement without an admission of liability resolves **No**.

This question resolves **No** if:
- The jury returns a verdict finding Erickson not liable (i.e., 0% fault allocated to him), OR
- The case against Erickson is dismissed, OR
- A settlement is reached without any admission of liability by Erickson, OR
- No verdict, order, or settlement establishing Erickson's liability is reached by July 1, 2026 (11:59 PM UTC).

"[Liable](https://en.wikipedia.org/wiki/Legal_liability)" means legally responsible under [civil law](https://en.wikipedia.org/wiki/Civil_law_(common_law)) for damages arising from the wrongful death claims. A "[civil trial](https://en.wikipedia.org/wiki/Civil_procedure)" refers to a non-criminal court proceeding where liability and damages are determined.

**Resolution source**: Credible news reporting from outlets such as the [Los Angeles Times](https://www.latimes.com/), [NBC Los Angeles](https://www.nbclosangeles.com/), [FOX 11 Los Angeles](https://www.foxla.com/), [Associated Press](https://apnews.com/), or [Reuters](https://www.reuters.com/), or official court records from the [Los Angeles County Superior Court](https://www.lacourt.org/).

**Pre-cutoff background**

A wrongful death civil trial (Iskander v. Grossman et al.) began in late April 2026 at the Van Nuys Courthouse East in Los Angeles County Superior Court. The plaintiffs, Nancy and Karim Iskander, are the parents of Mark Iskander (age 11) and Jacob Iskander (age 8), who were fatally struck in a crosswalk in Westlake Village, California, in September 2020.

The defendants are Rebecca Grossman, who was convicted of second-degree murder in February 2024 and is currently serving 15 years to life in prison, and former MLB pitcher Scott Erickson, her then-boyfriend. The plaintiffs allege Erickson was racing his SUV alongside Grossman's vehicle at speeds exceeding 80 mph in a 45 mph zone when Grossman struck and killed the two boys [Rebecca Grossman, former Dodger face $100M civil trial over ...](https://www.foxla.com/news/grossman-erickson-civil-trial-wrongful-death-iskander-2026). The family is seeking damages potentially exceeding $100 million [Rebecca Grossman, former Dodger face $100M civil trial over ...](https://www.foxla.com/news/grossman-erickson-civil-trial-wrongful-death-iskander-2026).

Erickson was never criminally charged in connection with the crash. In the civil trial, he is a co-defendant, and both defendants deny liability and blame each other [Rebecca Grossman, former Dodger face $100M civil trial over ...](https://www.foxla.com/news/grossman-erickson-civil-trial-wrongful-death-iskander-2026). The civil standard of proof is a "[preponderance of the evidence](https://www.law.cornell.edu/wex/preponderance_of_the_evidence)" — meaning it must be "more likely than not" that Erickson is liable — which is a lower bar than the criminal standard of "beyond a reasonable doubt."

As of May 11, 2026, the trial is ongoing with testimony underway. The trial is expected to last approximately two months from its late April 2026 start date [Rebecca Grossman, former Dodger face $100M civil trial over ...](https://www.foxla.com/news/grossman-erickson-civil-trial-wrongful-death-iskander-2026), meaning a verdict could come in June or early July 2026.

**Exact later resolution packet**

The question resolves YES because a jury in the Iskander v. Grossman civil trial (Los Angeles County Superior Court, Van Nuys) found defendant Scott Erickson liable/negligent for the wrongful deaths of Mark (11) and Jacob (8) Iskander, well within the resolution window (verdict June 3, 2026; punitive phase June 10, 2026 — both on/after May 10, 2026 and before July 1, 2026).

Evidence from the required resolution sources:
- Associated Press: "The jury found both Rebecca Grossman and Scott Erickson, a former Los Angeles Dodgers pitcher, negligent in the deaths of 11-year-old Mark Iskander and 8-year-old Jacob Iskander," awarding $176 million in compensatory damages [5282d9]. URL: https://apnews.com/article/grossman-iskander-erickson-civil-trial-los-angeles-0eb1919707db6c7fa3d79ede1e65d056
- FOX 11 Los Angeles: "A jury found socialite Rebecca Grossman and former Dodger Scott Erickson negligent on Wednesday [June 3, 2026] in the 2020 deaths of Mark and Jacob Iskander, awarding their family $176 million in damages." The jury also found both defendants acted with malice, triggering a punitive damages phase [849085]. URL: https://www.foxla.com/news/rebecca-grossman-civil-trial-verdict-reached
- Los Angeles Times: "A civil jury in Van Nuys has found Rebecca Grossman and ex-Dodgers pitcher Scott Erickson liable in the deaths of two young brothers in a car crash." In the punitive phase (decided June 10, 2026), the jury ordered Scott Erickson to pay $1.17 million in punitive damages and Grossman $21 million [8ef5e6]. URL: https://www.latimes.com/california/story/2026-06-10/rebecca-grossman-scott-erickson-punitive-damages-boys-deaths

Distinguishing the co-defendants: Both were found liable, but the allocation differed — the jury separately assessed punitive damages of $21 million against Grossman versus $1.17 million against Erickson [8ef5e6]. The resolution criteria specify that assigning Erickson any non-zero percentage of fault resolves YES. Erickson being found liable/negligent AND being assessed $1.17 million in punitive damages confirms a non-zero share of fault was attributed to him. This is a jury verdict (not a settlement), so the settlement sub-criteria are inapplicable. Therefore the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-57. `d345aa2e-74af-55d1-9b2e-e62e78291dd4`

- Present date: `2026-05-13 13:23:22.112950`
- Source cutoff boundary: `2026-05-14` (encodes end of UTC day `2026-05-13`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Cour d'assises des Alpes-Maritimes maintain the legal qualification of "viol par surprise" in its appeal verdict against Jack Sion?

**Resolution criteria**

This question resolves **Yes** if the cour d'assises des Alpes-Maritimes, in a verdict issued on or after May 10, 2026 (UTC), explicitly convicts Jack Sion of "viol par surprise" (rape by surprise/deception) or "viol commis par stratagème" — i.e., maintains the legal qualification of rape based on the element of "surprise" as defined in Article 222-23 of the French Penal Code (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000052535571). "Maintaining the legal qualification" means the court finds Sion guilty of rape ("viol") on at least one count where the absence of consent is established through "surprise" (deception/stratagem).

This question resolves **No** if the court:
- Acquits Sion of all rape charges, OR
- Requalifies the acts as a lesser offense, such as "agression sexuelle" (sexual assault, defined under Articles 222-27 et seq. of the French Penal Code), that does not include the qualification of rape by surprise.

Resolution will be determined by credible reporting from major French news outlets such as AFP, Le Monde, Le Figaro, France Info, Nice-Matin, or CNews (e.g., https://www.cnews.fr/faits-divers/2026-05-06/affaire-jack-sion-le-faux-playboy-du-net-rejuge-partir-de-ce-mercredi). If no verdict is issued by June 30, 2026 (UTC), this question resolves **No**.

**Pre-cutoff background**

Jack Sion, a 79-year-old retiree from Nice, was convicted in October 2021 by the cour criminelle départementale de l'Hérault to eight years of imprisonment for "viols par surprise" (rape by surprise/deception) against three women [Viols "par surprise" : le retraité niçois qui se faisait passer pour ...](https://france3-regions.franceinfo.fr/provence-alpes-cote-d-azur/alpes-maritimes/nice/viols-par-surprise-le-retraite-nicois-qui-se-faisait-passer-pour-un-playboy-de-30-ans-de-retour-au-tribunal-3345433.html). Sion had created fake profiles on dating sites using photos of a young male model ("Anthony Laroche") to lure women into meeting him. Upon arrival, victims discovered a man decades older than advertised but were subjected to sexual acts. The prosecution argued this deception constituted "surprise" — one of the four elements (violence, constraint, threat, or surprise) that vitiate consent under French rape law.

Under Article 222-23 of the French Penal Code (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000052535571), rape ("viol") is defined as any act of sexual penetration committed against another person by violence, constraint, threat, or surprise ("par surprise"). The concept of "viol par surprise" encompasses situations where a stratagem is used to deceive the victim about the true nature of the situation or the identity of the perpetrator, thereby vitiating consent. In this case, the legal innovation was applying "surprise" to online identity deception — the use of a fake identity on dating platforms to obtain sexual encounters.

Sion appealed his conviction. His appeal trial opened on May 6, 2026, before the cour d'assises des Alpes-Maritimes in Nice and is scheduled to last five days, with a verdict expected around May 15, 2026 [Affaire Jack Sion : le faux playboy du net rejugé à partir de ...](https://www.cnews.fr/faits-divers/2026-05-06/affaire-jack-sion-le-faux-playboy-du-net-rejuge-partir-de-ce-mercredi) [Viols "par surprise" : le retraité niçois qui se faisait passer pour ...](https://france3-regions.franceinfo.fr/provence-alpes-cote-d-azur/alpes-maritimes/nice/viols-par-surprise-le-retraite-nicois-qui-se-faisait-passer-pour-un-playboy-de-30-ans-de-retour-au-tribunal-3345433.html). The defense contests the qualification of "viol par surprise," arguing the acts should either not constitute rape or should be requalified as a lesser offense such as "agression sexuelle" (sexual assault, punishable by up to 10 years rather than 15 years for rape). The court could maintain the rape qualification, requalify the offense, or acquit entirely.

**Exact later resolution packet**

The question resolves YES. On Wednesday, May 13, 2026, the cour d'assises des Alpes-Maritimes (the appeal court in Nice, referred to as the "cour d'appel de Nice") issued its verdict in the appeal trial of Jack Sion, convicting him of three counts of "viols par surprise" (rape by surprise) and sentencing him to 18 years of criminal imprisonment (réclusion criminelle), a heavier sentence than the 8 years imposed at first instance in 2021.

This satisfies every element of the resolution criteria:

1. Correct court (appeal court, not the original lower court): The verdict was issued by the cour d'assises des Alpes-Maritimes / cour d'appel de Nice, the appeal court, on the appeal of the 2021 conviction by the cour criminelle départementale de l'Hérault (Montpellier). France Info states: "Un homme de 79 ans... a été condamné par la cour d'appel de Nice, mercredi 13 mai, à 18 ans de prison pour 'viols par surprise' sur trois femmes, avec mandat de dépôt." [Un homme de 79 ans, qui se faisait passer pour un trentenaire sur ...](https://www.franceinfo.fr/faits-divers/un-homme-de-79-ans-qui-se-faisait-passer-pour-un-trentenaire-sur-des-sites-de-rencontres-condamne-a-18-ans-de-prison-pour-viols-par-surprise_8002418.html) Nice-Matin confirms the conviction "en appel par la cour d'assises des Alpes-Maritimes" [18 ans de réclusion criminelle pour le Niçois Jack Sion ... - Nice-Matin](https://www.nicematin.com/faits-divers/18-ans-de-reclusion-criminelle-pour-jack-sion-18-ans-de-reclusion-criminelle-pour-jack-sion-le-faux-play-boy-du-net-10680559).

2. Verdict date within window (May 10 – June 30, 2026 inclusive): The verdict was rendered on May 13, 2026 [Un homme de 79 ans, qui se faisait passer pour un trentenaire sur ...](https://www.franceinfo.fr/faits-divers/un-homme-de-79-ans-qui-se-faisait-passer-pour-un-trentenaire-sur-des-sites-de-rencontres-condamne-a-18-ans-de-prison-pour-viols-par-surprise_8002418.html) [18 ans de réclusion criminelle pour le Niçois Jack Sion ... - Nice-Matin](https://www.nicematin.com/faits-divers/18-ans-de-reclusion-criminelle-pour-jack-sion-18-ans-de-reclusion-criminelle-pour-jack-sion-le-faux-play-boy-du-net-10680559), which is within the required window.

3. Conviction for "viol" (rape) maintained on at least one count (not requalified to mere "agression sexuelle"): He was found guilty of THREE counts of "viols par surprise" [18 ans de réclusion criminelle pour le Niçois Jack Sion ... - Nice-Matin](https://www.nicematin.com/faits-divers/18-ans-de-reclusion-criminelle-pour-jack-sion-18-ans-de-reclusion-criminelle-pour-jack-sion-le-faux-play-boy-du-net-10680559), so the rape qualification was maintained on multiple counts.

4. Conviction based specifically on the "surprise" element (deception/stratagem) per Article 222-23: The conviction is explicitly for "viols par surprise." France Info explains the concept: "Le viol par surprise peut faire référence à un mensonge, lorsque l'auteur surprend sa victime en obtenant son consentement en lui faisant croire des choses erronées pour avoir une relation sexuelle." [Un homme de 79 ans, qui se faisait passer pour un trentenaire sur ...](https://www.franceinfo.fr/faits-divers/un-homme-de-79-ans-qui-se-faisait-passer-pour-un-trentenaire-sur-des-sites-de-rencontres-condamne-a-18-ans-de-prison-pour-viols-par-surprise_8002418.html)

Named resolution sources used: France Info (https://www.franceinfo.fr/faits-divers/un-homme-de-79-ans-qui-se-faisait-passer-pour-un-trentenaire-sur-des-sites-de-rencontres-condamne-a-18-ans-de-prison-pour-viols-par-surprise_8002418.html) [Un homme de 79 ans, qui se faisait passer pour un trentenaire sur ...](https://www.franceinfo.fr/faits-divers/un-homme-de-79-ans-qui-se-faisait-passer-pour-un-trentenaire-sur-des-sites-de-rencontres-condamne-a-18-ans-de-prison-pour-viols-par-surprise_8002418.html) and Nice-Matin (https://www.nicematin.com/faits-divers/18-ans-de-reclusion-criminelle-pour-jack-sion-18-ans-de-reclusion-criminelle-pour-jack-sion-le-faux-play-boy-du-net-10680559) [18 ans de réclusion criminelle pour le Niçois Jack Sion ... - Nice-Matin](https://www.nicematin.com/faits-divers/18-ans-de-reclusion-criminelle-pour-jack-sion-18-ans-de-reclusion-criminelle-pour-jack-sion-le-faux-play-boy-du-net-10680559). Additional corroboration appears in Midi Libre's headline "Jack Sion, le 'play-boy du Net', reconnu coupable de 'viols par surprise'... condamné à 18 ans de réclusion" and BFMTV's report of the same verdict.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-58. `66bb32a9-f09d-5c2e-80e8-73da6d84ac4c`

- Present date: `2026-05-14 11:44:34.354218`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Latvian Saeima pass a no-confidence motion or will an additional cabinet minister resign in connection with drone incursion incidents between May 12, 2026 and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 (00:00 UTC) and before July 1, 2026 (23:59 UTC), at least one of the following occurs:

1. **No-confidence vote**: The Saeima passes a motion of no confidence (as defined in Article 59 of the Constitution of Latvia: https://www.saeima.lv/en/legislative-process/constitution) in the Prime Minister, the entire Cabinet, or any individual minister, where the motion text or accompanying parliamentary debate explicitly references the drone incursion incidents of May 2026 or the government's handling thereof; OR

2. **Cabinet-level resignation or dismissal**: Any member of the Cabinet of Ministers of Latvia — defined as the Prime Minister or any minister holding a portfolio as listed on the official Cabinet website (https://www.mk.gov.lv/en/cabinet-ministers) — resigns or is dismissed, where the resigning/dismissed official, the Prime Minister, or a formal government statement explicitly cites the drone incursion incidents as a reason for the departure.

The resignation of Defence Minister Andris Sprūds on May 10, 2026 does NOT count, as it occurred before the resolution window.

This question resolves **No** if neither condition is met by July 1, 2026, 23:59 UTC.

**Resolution sources**: Official Latvian government websites (https://www.mk.gov.lv/en, https://www.saeima.lv/en), Latvian public media (https://eng.lsm.lv/), or credible international outlets (Reuters, AP, AFP).

**Pre-cutoff background**

On May 7, 2026, two Ukrainian drones flying from Russian airspace struck a fuel storage depot in Rēzekne, eastern Latvia [It appears there were actually two drone strikes at Latvian fuel depot](https://eng.lsm.lv/article/society/defence/08.05.2026-it-appears-there-were-actually-two-drone-strikes-at-latvian-fuel-depot.a646323/). The incident was initially reported as a single strike but was later confirmed to have been two separate impacts. On May 10, 2026, Latvian Prime Minister Evika Siliņa demanded the resignation of Defence Minister Andris Sprūds, citing the delayed deployment of anti-drone systems. Sprūds resigned the same day, and PM Siliņa assumed interim duties as Defence Minister [It appears there were actually two drone strikes at Latvian fuel depot](https://eng.lsm.lv/article/society/defence/08.05.2026-it-appears-there-were-actually-two-drone-strikes-at-latvian-fuel-depot.a646323/).

As of May 12, 2026, political scrutiny of the government's handling of the drone incursions remains high, with security experts publicly stating that Latvia's reaction to drone incidents "could be better" [It appears there were actually two drone strikes at Latvian fuel depot](https://eng.lsm.lv/article/society/defence/08.05.2026-it-appears-there-were-actually-two-drone-strikes-at-latvian-fuel-depot.a646323/). Under Article 59 of the Constitution of the Republic of Latvia (https://www.saeima.lv/en/legislative-process/constitution), the Prime Minister and Ministers must maintain the confidence of the Saeima (Latvia's 100-member parliament). If the Saeima expresses no confidence in the Prime Minister, the entire Cabinet must resign; if no confidence is expressed in an individual Minister, that Minister must resign [The Constitution of the Republic of Latvia - Saeima](https://www.saeima.lv/en/legislative-process/constitution). A no-confidence motion requires a quorum of at least 50 deputies to proceed [Opposition party demands vote of no confidence in PM, then doesn't ...](https://eng.lsm.lv/article/politics/politics/05.02.2026-opposition-party-demands-vote-of-no-confidence-in-pm-then-doesnt-bother-to-back-it.a633325/). In February 2026, an opposition party attempted a no-confidence vote against PM Siliņa but failed to secure sufficient support [Opposition party demands vote of no confidence in PM, then doesn't ...](https://eng.lsm.lv/article/politics/politics/05.02.2026-opposition-party-demands-vote-of-no-confidence-in-pm-then-doesnt-bother-to-back-it.a633325/), illustrating that such motions are plausible but not easily passed in the current parliamentary configuration.

Latvia's Cabinet of Ministers consists of the Prime Minister and ministers heading individual ministries, as defined by the Cabinet Structure Law (Ministru kabineta iekārtas likums), available at https://www.mk.gov.lv/en/regulatory-acts. The current coalition government is led by PM Siliņa.

**Exact later resolution packet**

The question resolves YES via Condition 2 (Cabinet-level resignation), because Latvian Prime Minister Evika Siliņa resigned on May 14, 2026 — squarely within the resolution window (May 12, 2026 00:00 UTC to July 1, 2026 23:59 UTC) — and her departure was explicitly tied to the government's handling of the May 2026 Ukrainian drone incursion incidents.

Key points:

1. The resolution criteria (Condition 2) define an eligible resignation as any Cabinet member — explicitly including "the Prime Minister or any minister holding a portfolio" — resigning where the departure explicitly cites the drone incursion incidents. The Prime Minister therefore counts.

2. Latvian public media LSM (eng.lsm.lv, a specified resolution source) confirms that PM Evika Siliņa (New Unity) resigned on Thursday, May 14, 2026 [e245a6]. Her stated reason was the government crisis stemming directly from the drone-incident fallout: she cited the political blockade over her nominee to replace the Defence Minister who had resigned following the drone strikes, saying "political windbags have chosen a crisis – a government crisis. That is why I am announcing my resignation." The resignation occurred amid a government "seriously shaken by drone incidents" [e245a6].

3. Reuters (a specified resolution source) corroborates the explicit causal link: after "a Ukrainian drone hit an empty oil tank in Latvia on May 7, Silina sacked her defence minister over what she said were inadequate defensive measures by the military, which in turn led to the collapse of her coalition," and the parliament approved a new government under Andris Kulbergs on May 28, 2026 [d0858b].

4. The excluded May 10, 2026 resignation of Defence Minister Andris Sprūds is correctly not the basis for this resolution; the qualifying event is the PM's own May 14, 2026 resignation, which falls inside the window.

Because a Cabinet member (the Prime Minister) resigned within the window with the departure explicitly linked to the drone incidents, the question resolves YES (1). (This holds regardless of whether a formal no-confidence vote under Condition 1 was passed.)

Sources: eng.lsm.lv "Latvian Prime Minister Evika Siliņa steps down" (14.05.2026) https://eng.lsm.lv/article/politics/politics/14.05.2026-latvian-prime-minister-evika-silina-steps-down.a647082/ [e245a6]; Reuters "Latvia parliament approves new government after drone row topples coalition" (2026-05-28) https://www.reuters.com/world/latvia-parliament-approves-new-government-after-drone-row-topples-coalition-2026-05-28/ [d0858b].

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-59. `b3c0c024-61af-58c4-8856-fe7dacb9f180`

- Present date: `2026-05-16 22:13:05.918050`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will any U.S. court grant a stay in a climate liability lawsuit against a fossil fuel company, citing the pending Suncor v. Boulder County case, between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 and on or before July 1, 2026 (all dates in UTC), any federal or state court in the United States issues a formal written order or docket entry granting a **stay** (i.e., a court order that halts or suspends proceedings in a case; see [Cornell Law Institute definition](https://www.law.cornell.edu/wex/stay)) in a **climate liability lawsuit** against a **fossil fuel company**, where that order explicitly **cites** the pending U.S. Supreme Court case *Suncor Energy (U.S.A.) Inc. v. County Commissioners of Boulder County* (No. 25-170).

Key definitions:
- **Climate liability lawsuit**: A civil action listed in the [Sabin Center Climate Case Chart](http://climatecasechart.com/) or any civil lawsuit seeking damages or equitable relief from a fossil fuel company for harms allegedly caused by climate change.
- **Fossil fuel company**: A company primarily engaged in the exploration, extraction, production, refining, or marketing of oil, natural gas, or coal (see [Investopedia definition](https://www.investopedia.com/terms/f/fossil-fuel.asp)).
- **Stay**: A formal court order suspending or halting proceedings in a case (see [Cornell LII](https://www.law.cornell.edu/wex/stay)). Orders holding a case "in abeyance" qualify.
- **Citing**: The written text of the court order, opinion, or docket entry must explicitly mention "Suncor v. Boulder County," "Boulder County v. Suncor," or Supreme Court docket number "25-170" as a reason or basis for the stay.

The stay must be **issued** (i.e., entered on the docket) on or after May 12, 2026 UTC. Stays granted before May 12, 2026 do not count.

If no such stay is identified by July 1, 2026, this question resolves **No**.

**Resolution source**: Court dockets accessible via [PACER](https://pacer.uscourts.gov/) or state court electronic filing systems, or reporting by credible legal news outlets including [E&E News/Climatewire](https://www.eenews.net/), the [Sabin Center Climate Litigation Updates](https://climate.law.columbia.edu/content/climate-change-litigation), [Reuters](https://www.reuters.com/), or [Bloomberg Law](https://www.bloomberglaw.com/).

**Pre-cutoff background**

On February 23, 2026, the U.S. Supreme Court granted certiorari in *Suncor Energy (U.S.A.) Inc. v. County Commissioners of Boulder County* (No. 25-170), agreeing to decide whether federal law precludes state-law climate liability claims against fossil fuel companies [Climate Litigation Updates (March 23, 2026)](https://climate.law.columbia.edu/news/climate-litigation-updates-march-23-2026). The case is scheduled for argument in the October 2026 term, with respondents' merits brief due July 27, 2026.

Since the cert grant, fossil fuel defendants in parallel climate cases have sought stays of proceedings. As of March 2026, the following developments have occurred [Climate Litigation Updates (March 23, 2026)](https://climate.law.columbia.edu/news/climate-litigation-updates-march-23-2026):
- **New Jersey** (*Platkin v. Exxon Mobil Corp.*): The Appellate Division held the appeal in abeyance pending the Supreme Court's decision in *Suncor*.
- **Washington state** (federal court): A federal judge paused a homeowner insurance climate lawsuit against Exxon Mobil and other oil producers [Judge pauses climate case pending Supreme Court ruling](https://www.eenews.net/articles/judge-pauses-climate-case-pending-supreme-court-ruling/).
- **Maryland** (*Baltimore v. BP*): The Maryland Supreme Court *denied* a motion to stay on March 19, 2026.
- **Washington** (*Shoalwater Bay* and *Makah* tribal cases): Defendants requested stays, but the court proceeded with hearings on motions to dismiss.
- **Hawai'i** (*State of Hawai'i v. BP*): Defendants requested a stay; outcome not yet confirmed as of late March 2026.

On April 17, 2026, the Supreme Court unanimously ruled in favor of Chevron in a separate case involving Louisiana coastal erosion lawsuits, holding that such cases could be removed to federal court. This ruling may further embolden defendants to seek stays in pending climate cases.

Approximately 86 climate lawsuits have been filed against major fossil fuel producers worldwide, including cases brought by cities, counties, states, and tribes in the U.S. against companies such as ExxonMobil, Chevron, BP, Shell, and Suncor. Given the pending Supreme Court decision, additional stay requests are expected in the May–June 2026 window, though courts have shown mixed willingness to grant them.

**Exact later resolution packet**

The question resolves YES.

The Sabin Center for Climate Change Law's "Climate Litigation Updates (June 30, 2026)" reports, under its U.S. Decisions and Settlements section, that "A Delaware Superior Court granted fossil fuel industry defendants' motion to stay proceedings in the State of Delaware's climate change lawsuit pending the U.S. Supreme Court's decision in Suncor Energy (U.S.A.) Inc. v. County Commissioners of Boulder County (No. 25-170)." The court found it was "unclear" whether the State's sole remaining claim (a Delaware Consumer Fraud Act claim) would fall within the scope of the Supreme Court's decision in Boulder [Climate Litigation Updates (June 30, 2026)](https://climate.law.columbia.edu/news/climate-litigation-updates-june-30-2026) [Climate Litigation Updates (June 30, 2026)](https://climate.law.columbia.edu/news/climate-litigation-updates-june-30-2026). Source: https://climate.law.columbia.edu/news/climate-litigation-updates-june-30-2026

Every element of the resolution criteria is satisfied:
- Timing: The stay was granted on June 8, 2026 in State of Delaware v. BP America Inc., No. N20C-09-097-EMD-CCLD (Del. Super. Ct.), which is on or after May 12, 2026 and on or before July 1, 2026 UTC [Climate Litigation Updates (June 30, 2026)](https://climate.law.columbia.edu/news/climate-litigation-updates-june-30-2026) [Delaware v. BP America Inc. - The Climate Litigation Database](https://www.climatecasechart.com/collections/delaware-v-bp-america-inc-_919ad5).
- Explicit citation: The order was entered expressly "pending the U.S. Supreme Court's decision in Suncor Energy (U.S.A.) Inc. v. County Commissioners of Boulder County (No. 25-170)," so the docket entry/order explicitly cites both the case name "Suncor v. Boulder County" and the docket number "25-170" as the basis for the stay [Climate Litigation Updates (June 30, 2026)](https://climate.law.columbia.edu/news/climate-litigation-updates-june-30-2026) [Delaware v. BP America Inc. - The Climate Litigation Database](https://www.climatecasechart.com/collections/delaware-v-bp-america-inc-_919ad5).
- Stay actually granted: The court "granted" the defendants' motion to stay — this was a ruling, not a mere pending request [Climate Litigation Updates (June 30, 2026)](https://climate.law.columbia.edu/news/climate-litigation-updates-june-30-2026) [Climate Litigation Updates (June 30, 2026)](https://climate.law.columbia.edu/news/climate-litigation-updates-june-30-2026).
- Climate liability lawsuit: State of Delaware v. BP America Inc. is listed in the Sabin Center Climate Case Chart as a "Lawsuit seeking to hold the fossil fuel industry liable for the physical, environmental, social, and economic consequences of climate change in Delaware" [Delaware v. BP America Inc. - The Climate Litigation Database](https://www.climatecasechart.com/collections/delaware-v-bp-america-inc-_919ad5). Source: https://www.climatecasechart.com/collections/delaware-v-bp-america-inc-_919ad5
- Fossil fuel company defendant: The defendants are fossil fuel industry companies (including BP America Inc.), engaged in the production, refining, and marketing of oil and natural gas [Delaware v. BP America Inc. - The Climate Litigation Database](https://www.climatecasechart.com/collections/delaware-v-bp-america-inc-_919ad5) [Climate Litigation Updates (June 30, 2026)](https://climate.law.columbia.edu/news/climate-litigation-updates-june-30-2026).

Corroboration/context: The immediately prior Sabin update (May 29, 2026) documented that during roughly the same period several courts had *denied* stay motions (Hawai'i Circuit Court on May 6, 2026; Oregon Circuit Court on May 7, 2026; Washington Superior Court in the Shoalwater Bay/Makah tribal cases), showing courts were split — but the Delaware grant on June 8, 2026 satisfies the YES condition regardless [Climate Litigation Updates (May 29, 2026)](https://climate.law.columbia.edu/news/climate-litigation-updates-may-29-2026). Source: https://climate.law.columbia.edu/news/climate-litigation-updates-may-29-2026

Because at least one qualifying stay (Delaware, June 8, 2026) was granted within the window citing Suncor/25-170, in a climate liability lawsuit against fossil fuel companies, the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-60. `e6bf3057-e9c0-58b7-b18d-b737760937a9`

- Present date: `2026-05-03 04:16:28.735244`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Apple officially announce a dedicated AI/ML hardware product between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves YES if, between May 1, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC), Apple officially announces a dedicated AI/ML hardware product, OR credible reporting from qualifying sources reveals specific new details about such a product (beyond what was already publicly known before May 1, 2026).

**Definition of 'dedicated AI/ML hardware product':** A standalone consumer electronic device or a dedicated server/chip product whose primary marketed purpose is to serve as an AI/ML interface or AI/ML processing platform. This includes, but is not limited to: an AI-focused home device, an AI wearable (e.g., AI pin, AI glasses), a standalone AI assistant device, or a dedicated AI server chip. This explicitly EXCLUDES: (a) standard annual refreshes of existing product lines (iPhone, iPad, Mac, Apple Watch, AirPods, Apple TV) that simply include updated chips or AI software features; (b) software-only announcements (e.g., new Siri capabilities or Apple Intelligence features announced without new dedicated hardware); (c) the Apple Vision Pro or iterations thereof, unless explicitly marketed as a dedicated AI device rather than a mixed-reality headset.

**Definition of 'official announcement':** A press release on Apple Newsroom (https://www.apple.com/newsroom/) or an official Apple keynote/event.

**Definition of 'credible leak':** Reporting by Bloomberg's Mark Gurman, The Information, The Wall Street Journal, Reuters, or The New York Times that provides specific new product details (e.g., form factor, features, timeline) about a dedicated AI/ML hardware product not previously reported before May 1, 2026. Repetition or elaboration of details already reported before May 1, 2026 does NOT count.

**Primary source of truth:** Apple Newsroom (https://www.apple.com/newsroom/) for official announcements; the publications listed above for leaks.

**Pre-cutoff background**

Apple has been increasingly active in the AI hardware space. In December 2025, Apple announced that John Giannandrea would retire as head of AI, replaced by Amar Subramanya, a former Microsoft and Google executive, as VP of AI reporting to Craig Federighi [Not to be outdone by OpenAI, Apple is reportedly developing an AI ...](https://techcrunch.com/2026/01/21/not-to-be-outdone-by-openai-apple-is-reportedly-developing-an-ai-wearable/) [Apple Working on Three AI Wearables: Smart Glasses, AI Pin, and ...](https://www.macrumors.com/2026/02/17/apple-ai-wearable-development/). This leadership change signaled Apple's renewed focus on AI capabilities.

As of early 2026, multiple credible leaks have revealed Apple's AI hardware ambitions. In January 2026, The Information reported that Apple is developing an AI wearable pin with two cameras, three microphones, a speaker, and a physical button [Not to be outdone by OpenAI, Apple is reportedly developing an AI ...](https://techcrunch.com/2026/01/21/not-to-be-outdone-by-openai-apple-is-reportedly-developing-an-ai-wearable/). In February 2026, Bloomberg reported Apple is working on three AI-focused wearables: smart glasses (targeting 2027), an AI pin (targeting 2027), and AirPods with cameras (planned for as early as 2026) [Apple Working on Three AI Wearables: Smart Glasses, AI Pin, and ...](https://www.macrumors.com/2026/02/17/apple-ai-wearable-development/). Meanwhile, Apple's planned smart home display (J490) has reportedly been delayed to Fall 2026.

Apple's WWDC 2026 is scheduled for June 8–12, 2026, just after this question's resolution window. Competitors including OpenAI (with Jony Ive's device) and Meta (Ray-Ban smart glasses) are pushing aggressively into AI hardware. Apple has not yet made any official announcement of a standalone AI hardware product as of May 1, 2026. The key uncertainty is whether Apple will make a pre-WWDC announcement or leak new details about a dedicated AI device during May 2026.

**Exact later resolution packet**

The question resolves YES because credible reporting from a qualifying source (Bloomberg's Mark Gurman) revealed specific NEW product details about dedicated AI/ML hardware products during the May 1–June 1, 2026 window, satisfying the "credible leak" branch of the resolution criteria.

The resolution criteria offer an OR condition: YES if either (a) Apple officially announces a dedicated AI/ML hardware product, OR (b) credible reporting from Bloomberg's Mark Gurman, The Information, WSJ, Reuters, or NYT reveals specific NEW product details (form factor, features, timeline) not previously reported before May 1, 2026. No official Apple Newsroom/keynote announcement occurred (WWDC 2026 was June 8–12, after the window), but the leak branch was satisfied multiple times.

Two qualifying Bloomberg/Gurman reports during the window:

1. May 7, 2026 — Gurman/Bloomberg reported new details on Apple's AirTag-sized AI wearable "pendant": it would feature a clip for clothing or a hole for a cord/chain to be worn as a necklace, lacks a display and laser projector (distinguishing it from the Humane AI Pin), and has its own chip with limited performance that relies heavily on a paired iPhone for processing. The report also stated camera-equipped AirPods had reached an advanced testing stage. These form-factor and architecture details were not in the public record before May 1, 2026 [830acb]. (https://www.macrumors.com/2026/05/07/apple-still-working-on-pendant-report/)

2. May 31, 2026 — Gurman/Bloomberg reported new, previously-unreported specifics about Apple's AI smart glasses: a target price range of $200–$500; four potential frame designs (larger rectangular, slimmer rectangular, larger oval/circular, smaller oval/circular); specific colors (black, ocean blue, light brown); vertically-oriented oval camera lenses; turn-by-turn walking directions; and explicit clarification that the first generation will NOT have an in-lens AR display, plus a refined "late 2027" timeline. These specific design/feature/pricing details went well beyond the prior public knowledge that Apple was "working on smart glasses targeting 2027" [ed116d]. (https://www.macrumors.com/2026/05/31/apple-glasses-late-2027-report/ and https://9to5mac.com/2026/06/01/latest-apple-glasses-leak-has-me-way-more-excited-for-the-product/ [061a44])

These products (AI pendant/pin and AI smart glasses) are dedicated AI/ML hardware whose primary marketed purpose is to serve as AI interfaces, explicitly included in the question's definition ("an AI wearable (e.g., AI pin, AI glasses)"), and are not standard refreshes of iPhone/iPad/Mac/Watch/AirPods/Apple TV. The reporting comes from a named qualifying source (Mark Gurman/Bloomberg) and falls strictly within May 1–June 1, 2026. Therefore the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-61. `a3d2afee-a683-5b3e-92d6-f78d192173d5`

- Present date: `2026-05-01 17:39:15.157097`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will California Resources Corporation (CRC) commence first CO₂ injection at the Elk Hills CTV I-26R storage reservoir by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after April 30, 2026 (12:00 AM PT) and on or before June 1, 2026 (11:59 PM PT), California Resources Corporation (CRC) or Carbon TerraVault (CTV) publicly confirms that first CO₂ injection into the CTV I-26R storage reservoir has commenced.

"Commencement of first CO₂ injection" is defined as the first instance of carbon dioxide being physically pumped into the CTV I-26R storage reservoir for the purpose of geological sequestration. This includes initial operational injection or commissioning-phase injection into the reservoir, but does **not** include surface-level equipment testing or pipeline pressure testing that does not involve injecting CO₂ into the subsurface reservoir.

**Resolution sources** (in order of preference):
1. CRC official press releases: https://www.crc.com/news-releases
2. SEC filings (Form 8-K or 10-Q): https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001609065&type=8-K&dateb=&owner=include&count=40
3. EPA Class VI Wells tracker: https://www.epa.gov/uic/current-class-vi-projects-under-review-epa
4. Credible reporting from major outlets (e.g., Reuters, Bloomberg, Hart Energy)

If no such confirmation is publicly available by June 1, 2026 (11:59 PM PT), this question resolves **No**.

**Pre-cutoff background**

California Resources Corporation (CRC), through its subsidiary Carbon TerraVault (CTV), is developing California's first carbon capture and storage (CCS) project at the Elk Hills Cryogenic Gas Plant in Kern County, California. The project aims to capture CO₂ from the gas plant and permanently store it underground in the CTV I-26R storage reservoir.

As of March 2026, CRC has completed construction of the carbon capture equipment and is in the commissioning phase [Carbon TerraVault Provides 2025 Update - Mon, 03/02/2026 - 08:00](https://www.crc.com/news-releases/news-release-details/carbon-terravault-provides-2025-update). The company is targeting first CO₂ injection in "spring 2026," but this remains subject to final EPA approval [California Resources Targets First CO₂ Injection at Elk Hills CCS ...](https://pgjonline.com/news/2026/march/california-resources-targets-first-co2-injection-at-elk-hills-ccs-project-in-spring-2026). CRC received initial EPA Class VI permits in December 2024, but the company is still anticipating the receipt of several additional draft EPA Class VI permits needed for operations [Carbon TerraVault Provides 2025 Update - Mon, 03/02/2026 - 08:00](https://www.crc.com/news-releases/news-release-details/carbon-terravault-provides-2025-update). CRC has submitted a CO₂ storage application to the EPA for 27 million metric tons (MMT) of total storage capacity [Carbon TerraVault Provides 2025 Update - Mon, 03/02/2026 - 08:00](https://www.crc.com/news-releases/news-release-details/carbon-terravault-provides-2025-update).

Key uncertainty factors include: (1) the timing of final EPA regulatory approval, which is a common bottleneck for CCS projects; (2) successful completion of facility commissioning; and (3) operational readiness of the injection wells. The EPA's Class VI Wells permit tracker can be found at https://www.epa.gov/uic/current-class-vi-projects-under-review-epa.

**Exact later resolution packet**

The question resolves YES.

Resolution criteria: YES if, between April 30, 2026 (12:00 AM PT) and June 1, 2026 (11:59 PM PT), CRC/CTV publicly confirms that first CO₂ injection into the CTV I-26R storage reservoir has commenced (physical pumping of CO₂ into the subsurface reservoir, excluding surface-level/pipeline pressure testing).

Evidence:
- California Resources Corporation issued an official press release titled "California Resources Corporation Achieves First CO₂ Injection at Carbon TerraVault I, a Major Milestone for Carbon Management in California," dated May 26, 2026. It explicitly states CRC "has achieved the first landmark carbon dioxide (CO₂) injection at Carbon TerraVault I (CTV I)," and identifies CTV I as composed of the depleted "26R" and "A1-A2" reservoirs, noting that "CTV I – 26R… is the first reservoir in California to receive final Class VI permits from the U.S. EPA" [1694d9]. URL: https://www.stocktitan.net/news/CRC/california-resources-corporation-achieves-first-co2-injection-at-9bahijemmskv.html (republishing the GlobeNewswire CRC press release).
- Corroborating trade press: Carbon Capture Journal (May 26, 2026), "California Resources starts CO2 injection at first CCS project," states "The company has begun CO2 injection at Carbon TerraVault I (CTV I), California's first operational CCS project," located at CRC's Elk Hills Field, and identifies CTV I-26R as the first reservoir in California to receive final EPA Class VI permits [0c6abe]. URL: https://www.carboncapturejournal.com/news/california-resources-starts-co2-injection-at-first-ccs-project/7259.aspx?Category=all
- Additional corroboration from RBN Energy ("CO2 Injections Begin at California's First CCS Site"), Bakersfield.com (describing an employee opening a wellhead valve "for the first injection of supercritical carbon dioxide"), and CRC's own LinkedIn/Facebook posts marking the milestone.

Analysis of checklist items:
1. Timing: The public confirmation (May 26, 2026) falls squarely within the required window of April 30 – June 1, 2026. ✓
2. Reservoir: The injection is into Carbon TerraVault I, which comprises the "26R" reservoir — i.e., CTV I-26R, the reservoir with final EPA Class VI permits. ✓
3. Physical injection vs. testing: The press release and reporting describe actual CO₂ injection ("achieved the first landmark CO₂ injection"; "has begun CO2 injection"; an employee opening a wellhead valve for "first injection of supercritical carbon dioxide"), confirming physical pumping into the subsurface reservoir, not mere surface/pipeline pressure testing. ✓
4. Source hierarchy: The primary source is CRC's official press release (top of the preference list), corroborated by trade press. ✓
5. "Commenced/started" vs. "targeted/planned": The language is unambiguously completed-action ("Achieves," "has achieved," "starts," "has begun"), not aspirational. ✓

All conditions are met, so the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-62. `4f2199de-01e2-52f1-b368-5c4765bd8c17`

- Present date: `2026-05-14 02:55:08.516636`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-30T00:00:00`

**Question**

Will the U.S. Supreme Court's decision in Hikma v. Amarin (No. 24-889) be unanimous?

**Resolution criteria**

This question resolves **Yes** if the Supreme Court's opinion in *Hikma Pharmaceuticals USA Inc. v. Amarin Pharma, Inc.* (No. 24-889), issued on or after May 12, 2026, is unanimous—meaning all participating justices join a single majority opinion with no separate concurrences or dissents.

This question resolves **No** if:
- Any participating justice files a concurring opinion (including concurrence in judgment only), a dissenting opinion, or a partial dissent; OR
- The Court issues a plurality opinion rather than a majority opinion.

**Definition of "unanimous":** A decision is unanimous if every justice who participates in the case joins the same single majority opinion. If one or more justices are recused or otherwise do not participate, unanimity is judged based on the participating justices only (e.g., an 8-0 or 7-0 decision with all participating justices joining one opinion counts as unanimous).

**Resolution source:** The official opinion as published on the Supreme Court of the United States opinions page: https://www.supremecourt.gov/opinions

The decision must be issued on or after May 12, 2026, to be valid for this question. If no decision is issued by June 30, 2026, this question resolves **N/A**.

**Pre-cutoff background**

The U.S. Supreme Court is reviewing *Hikma Pharmaceuticals USA Inc. v. Amarin Pharma, Inc.* (No. 24-889), a case concerning "skinny labeling" under the Hatch-Waxman Act and induced patent infringement. The central issue is whether a generic drug manufacturer that uses a "skinny label"—omitting a patented indication pursuant to 21 U.S.C. § 355(j)(2)(A)(viii)—can still be held liable for induced infringement based on its public marketing materials and statements referencing the branded drug.

**Federal Circuit ruling being challenged:** The Federal Circuit reversed a district court's dismissal of Amarin's induced infringement complaint, holding that while Hikma's skinny label alone might not induce infringement, the label *combined* with Hikma's public statements—describing its product as a "generic version" of Vascepa and citing sales figures attributable to off-label use—plausibly stated a claim for induced infringement sufficient to survive a motion to dismiss [https://ipwatchdog.com/2026/04/29/justices-voice-concern-upholding-cafcs-hikma-ruling-will-harm-generics-industry/](https://ipwatchdog.com/2026/04/29/justices-voice-concern-upholding-cafcs-hikma-ruling-will-harm-generics-industry/).

**Oral arguments (April 29, 2026):** During oral arguments, multiple justices across ideological lines raised concerns about the Federal Circuit's ruling. Justice Kavanaugh noted the ruling could leave generic companies uncertain about liability, potentially undermining the generics industry. Justices Thomas and Sotomayor questioned whether existing induced infringement standards would need to change if Hikma prevailed. Justice Alito challenged the government's interpretation, questioning whether the proposed standard created a "broad safe harbor." The U.S. government (Deputy Solicitor General Malcolm Stewart) argued against Amarin's position, warning it would deter generic manufacturers from using the Section VIII carve-out. Hikma's counsel argued that active inducement cannot depend on whether doctors might read infringing instructions into product descriptions consistent with non-infringing use [https://ipwatchdog.com/2026/04/29/justices-voice-concern-upholding-cafcs-hikma-ruling-will-harm-generics-industry/](https://ipwatchdog.com/2026/04/29/justices-voice-concern-upholding-cafcs-hikma-ruling-will-harm-generics-industry/).

The breadth of skepticism toward the Federal Circuit's ruling across ideological lines suggests potential for unanimity, but the complexity of balancing patent rights with the Hatch-Waxman generic drug framework—and the differing reasoning expressed by justices—could produce concurrences or partial dissents.

**Exact later resolution packet**

The question resolves YES.

1. TIMING (within window): The Supreme Court issued its decision in Hikma Pharmaceuticals USA Inc. v. Amarin Pharma, Inc. (No. 24-889) on June 4, 2026. This is on or after the May 12, 2026 threshold and on or before June 30, 2026, so the decision is valid for this question and does not resolve N/A [330eac][c91de0].

2. UNANIMITY (the key criterion): The official Supreme Court opinion (https://www.supremecourt.gov/opinions/25pdf/24-889_5i36.pdf) explicitly states on its final page: "JACKSON, J., delivered the opinion for a unanimous Court." This is the standard SCOTUS phrasing indicating a single majority opinion joined by all participating justices with no separate writings [330eac].

3. NO SEPARATE OPINIONS: The opinion text contains no concurring opinions (including concurrence in judgment only), no dissenting opinions, and no partial dissents. SCOTUSblog's case page likewise lists a 9-0 vote with no concurrences or dissents [330eac][c91de0].

4. NO RECUSALS / PLURALITY ISSUE: All nine justices participated (Jackson, Roberts, Thomas, Alito, Sotomayor, Kagan, Gorsuch, Kavanaugh, Barrett) — there were no recusals or non-participating justices, and the opinion is a majority opinion ("for a unanimous Court"), not a plurality [330eac][c91de0].

Because the opinion was issued within the required window and every participating justice joined a single majority opinion with no separate concurrences or dissents, the resolution criteria for YES are fully satisfied.

Resolution source: Official opinion at https://www.supremecourt.gov/opinions/25pdf/24-889_5i36.pdf (linked from https://www.supremecourt.gov/opinions).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-63. `04bdc911-bceb-558d-9332-272a2687bda2`

- Present date: `2026-05-02 14:38:56.281889`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will any US state beyond California, Ohio, and Utah enact legislation requiring data center developers to cover energy infrastructure costs between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if at least one US state, **excluding California, Ohio, and Utah**, enacts legislation on or after May 1, 2026, and before June 1, 2026 (all dates in UTC), that requires data center developers to pay for energy infrastructure costs associated with their facilities.

**Definition of "enacted":** A bill is considered enacted when it is signed into law by the state's governor, or when a gubernatorial veto is overridden by the legislature, or when the bill becomes law without the governor's signature under that state's constitutional procedures. The relevant date is the date of the governor's signature (or veto override, or effective-by-default date), which must fall on or after May 1, 2026 00:00 UTC and before June 1, 2026 00:00 UTC.

**Definition of "energy infrastructure costs":** The enacted legislation must require data center developers or operators to bear financial responsibility for at least one of the following: (a) electric grid transmission or distribution upgrades, (b) substation construction or upgrades, (c) new electricity generation capacity, or (d) interconnection costs — where such costs arise from the energy demands of the data center facility. Legislation that only mandates energy usage reporting, renewable energy procurement, or water usage does not qualify.

**Exclusions:** California, Ohio, and Utah are excluded, as they have already enacted qualifying legislation (California SB 57, Ohio SB 103, Utah HB 0507) [https://www.multistate.us/insider/2026/4/14/federal-ai-data-center-policy-meets-resistance-from-state-lawmakers](https://www.multistate.us/insider/2026/4/14/federal-ai-data-center-policy-meets-resistance-from-state-lawmakers).

**Resolution sources:** Official state legislature websites (e.g., leginfo.legislature.ca.gov, legislature.ohio.gov, or equivalent for the relevant state), the MultiState legislative tracker (https://www.multistate.us/issues/data-center-legislation), or credible news reporting from Reuters, Associated Press, Bloomberg, or major state-level newspapers confirming the governor's signature or equivalent enactment.

**Pre-cutoff background**

As of April 2026, the federal government has prioritized rapid data center construction through executive orders aimed at streamlining permitting. However, state legislatures have been pushing back with their own regulatory measures. According to MultiState's April 14, 2026 tracker, 27 states are advancing data center energy legislation [https://www.multistate.us/insider/2026/4/14/federal-ai-data-center-policy-meets-resistance-from-state-lawmakers](https://www.multistate.us/insider/2026/4/14/federal-ai-data-center-policy-meets-resistance-from-state-lawmakers). Three states have already enacted such laws: California (SB 57), Ohio (SB 103), and Utah (HB 0507) [https://www.multistate.us/insider/2026/4/14/federal-ai-data-center-policy-meets-resistance-from-state-lawmakers](https://www.multistate.us/insider/2026/4/14/federal-ai-data-center-policy-meets-resistance-from-state-lawmakers). Many state legislatures are in session through May and June 2026, meaning additional states could enact similar legislation during this window. The bills under consideration across states generally require data center developers to bear the costs of grid upgrades, new generation capacity, or transmission infrastructure needed to serve their facilities. Given that 24+ states have active bills but legislative timelines vary and many bills stall in committee, it is plausible but uncertain whether any additional state will complete the full legislative process and obtain a gubernatorial signature within this narrow one-month window.

**Exact later resolution packet**

The question resolves YES because Oklahoma — a state other than California, Ohio, or Utah — enacted qualifying legislation within the resolution window.

- Bill: Oklahoma House Bill 2992, the "Data Center Customer/Consumer Ratepayer Protection Act of 2026."
- Enactment date: The official Oklahoma Legislature bill information page (https://www.oklegislature.gov/BillInfo.aspx?Bill=hb2992&Session=2600) records "Approved by Governor 05/11/2026" [Bill Information for HB 2992 - Oklahoma Legislature](https://www.oklegislature.gov/BillInfo.aspx?Bill=hb2992&Session=2600). This was corroborated by KGOU/StateImpact Oklahoma, which reported that Gov. Kevin Stitt signed HB 2992 on Monday, May 11, 2026 [Stitt signs bill to prevent higher utility costs from data centers into law](https://www.kgou.org/energy/2026-05-13/stitt-signs-bill-to-prevent-higher-utility-costs-from-data-centers-into-law). (A separate ceremonial signing photo dated April 21 was noted by the Journal Record, but the official enactment/approval date is May 11, 2026 [Ratepayer protections signed into law by Oklahoma governor](https://journalrecord.com/2026/05/14/oklahoma-governor-signs-data-center-ratepayer-protection-law/).) May 11, 2026 falls strictly within the window of May 1, 2026 00:00 UTC to June 1, 2026 00:00 UTC.
- Content requirement: The law requires data center / large-load customers to bear financial responsibility for their own energy infrastructure costs. The Journal Record reported "House Bill 2992 requires new data centers to pay for their own infrastructure and the energy they consume," and that "Large-load customers would be required to sign contracts to pay for their infrastructure costs over 10 years" [Ratepayer protections signed into law by Oklahoma governor](https://journalrecord.com/2026/05/14/oklahoma-governor-signs-data-center-ratepayer-protection-law/). KGOU confirmed the law requires electricity suppliers to create separate terms for large-scale customers (data centers, crypto miners) so that existing customers do not subsidize their infrastructure needs [Stitt signs bill to prevent higher utility costs from data centers into law](https://www.kgou.org/energy/2026-05-13/stitt-signs-bill-to-prevent-higher-utility-costs-from-data-centers-into-law). This satisfies the definition of bearing financial responsibility for electric grid/generation/interconnection infrastructure costs (criteria a–d), and goes beyond mere energy reporting, water usage, or renewable procurement.
- The distinction between "passed" and "enacted" is honored: HB 2992 passed the legislature in early May and was formally signed/approved into law by the Governor on May 11, 2026 [Bill Information for HB 2992 - Oklahoma Legislature](https://www.oklegislature.gov/BillInfo.aspx?Bill=hb2992&Session=2600) [Stitt signs bill to prevent higher utility costs from data centers into law](https://www.kgou.org/energy/2026-05-13/stitt-signs-bill-to-prevent-higher-utility-costs-from-data-centers-into-law).

Therefore the resolution is YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-64. `ec471fcf-d34d-5284-939d-d94961d6436d`

- Present date: `2026-05-12 21:56:41.933544`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will a first-time major winner be crowned at the 2026 PGA Championship?

**Resolution criteria**

This question resolves **Yes** if the winner of the 2026 PGA Championship has never previously won any of the four men's major golf championships prior to the conclusion of the 2026 PGA Championship. It resolves **No** otherwise.

**Definitions:**
- A "major championship" (or "major") is defined as one of the following four annual men's professional golf tournaments: **The Masters Tournament**, **the PGA Championship**, **the U.S. Open**, and **The Open Championship** (see https://en.wikipedia.org/wiki/Men%27s_major_golf_championships).
- A "first-time major winner" is a player who has **zero wins** in any of the four defined majors at any point in their career prior to the conclusion of the 2026 PGA Championship. This means a player who won the 2026 Masters (Rory McIlroy) is **not** a first-time major winner.
- The "winner" is the player who is declared the official champion of the 2026 PGA Championship by the PGA of America. In the event of a tie after 72 holes of regulation play, the winner is determined by the official PGA Championship playoff procedure (currently a three-hole aggregate playoff on holes designated by the PGA of America, followed by sudden death if still tied), per the rules published at https://www.pgachampionship.com/.

**Resolution source:** The official 2026 PGA Championship results at https://www.pgachampionship.com/leaderboard, cross-referenced with historical major championship records available at authoritative sources such as https://en.wikipedia.org/wiki/List_of_men%27s_major_championships_winning_golfers or https://www.pgatour.com/.

**Edge cases:**
- If the 2026 PGA Championship is cancelled, suspended indefinitely, or not completed by May 31, 2026 (23:59 UTC), this question resolves **N/A**.
- If the tournament is reduced to fewer than 72 holes due to weather but an official winner is declared by the PGA of America, that winner counts for resolution.

**Pre-cutoff background**

The 2026 PGA Championship, the 108th edition of the tournament, is scheduled for May 14–17, 2026 (UTC-4 local time; tournament play begins Thursday May 14 at approximately 11:00 UTC and concludes no later than Sunday May 17 at approximately 23:59 UTC) at Aronimink Golf Club in Newtown Square, Pennsylvania [Official World Golf Ranking](https://www.owgr.com/).

As of May 10, 2026, the Official World Golf Ranking (OWGR) top 10 is [Official World Golf Ranking](https://www.owgr.com/):

1. **Scottie Scheffler** — Major winner (2024 Masters, 2025 PGA Championship)
2. **Rory McIlroy** — Major winner (2011 U.S. Open, 2012 PGA, 2014 Open, 2014 PGA, 2025 Masters, 2026 Masters)
3. **Cameron Young** — **Never won a major**
4. **Matt Fitzpatrick** — Major winner (2022 U.S. Open)
5. **Collin Morikawa** — Major winner (2020 PGA, 2021 Open)
6. **Tommy Fleetwood** — **Never won a major**
7. **Justin Rose** — Major winner (2013 U.S. Open)
8. **J.J. Spaun** — **Never won a major**
9. **Russell Henley** — **Never won a major**
10. **Chris Gotterup** — **Never won a major**

Five of the current top 10 players in the world have never won a major championship, including world No. 3 Cameron Young and No. 6 Tommy Fleetwood. LIV Golf players Jon Rahm and Bryson DeChambeau (both major winners) and Xander Schauffele are also expected to compete. Historically, first-time major winners emerge regularly—recent examples include Schauffele (2024 PGA), Morikawa (2020 PGA), and Fitzpatrick (2022 U.S. Open). The depth of highly-ranked non-major winners in the current field suggests a meaningful probability that the 2026 PGA Championship produces a first-time major champion.

The official tournament website is https://www.pgachampionship.com/ and the live leaderboard will be available at https://www.pgachampionship.com/leaderboard.

**Exact later resolution packet**

The question asks: "Will a first-time major winner be crowned at the 2026 PGA Championship?" It resolves YES if the winner of the 2026 PGA Championship had never previously won any of the four men's major golf championships (The Masters, PGA Championship, U.S. Open, The Open Championship) prior to the conclusion of the 2026 PGA Championship.

WINNER: The 2026 PGA Championship (108th edition), held May 14–17, 2026 at Aronimink Golf Club in Newtown Square, Pennsylvania, was won by Aaron Rai of England. The official PGA Championship website confirms "Aaron Rai wins the 2026 PGA Championship at Aronimink" [2026 PGA Championship Leaderboard - Live Scores](https://www.pgachampionship.com/leaderboard). He won by three strokes, finishing at -9 (271 total), with Jon Rahm and Alex Smalley tied for second at -6/274 (confirmed by multiple leaderboard sources including ESPN and NYT/The Athletic).

TOURNAMENT COMPLETED IN WINDOW: The tournament concluded on Sunday, May 17, 2026, well before the May 31, 2026 (23:59 UTC) cutoff specified in the edge-case criteria, so the question is not N/A.

FIRST-TIME MAJOR WINNER: Aaron Rai's Wikipedia page confirms this was his first career major championship victory. His major championship record shows zero prior major wins — best results were T27 at the 2025 Masters, T11 at the 2026 U.S. Open, and T19 at the 2021 Open Championship, with the PGA Championship listed as "Won: 2026" [https://en.wikipedia.org/wiki/Aaron_Rai](https://en.wikipedia.org/wiki/Aaron_Rai). He became the first Englishman to win the PGA Championship since Jim Barnes in 1919 [https://en.wikipedia.org/wiki/Aaron_Rai](https://en.wikipedia.org/wiki/Aaron_Rai). Thus he had zero wins in any of the four defined majors prior to this victory.

NOT THE 2026 MASTERS WINNER: The 2026 Masters was won by Rory McIlroy (as stated in the question's own description), not Aaron Rai. Therefore the "first-time major winner" criterion is satisfied — Rai did not have any prior major win, including the 2026 Masters.

Because the winner (Aaron Rai) was a first-time major champion, the question resolves YES.

SOURCES:
- Official 2026 PGA Championship results/leaderboard: https://www.pgachampionship.com/leaderboard (and article https://www.pgachampionship.com/news-media/articles/aaron-rai-wins-the-2026-pga-championship-at-aronimink) [2026 PGA Championship Leaderboard - Live Scores](https://www.pgachampionship.com/leaderboard)
- Winner's historical major record: https://en.wikipedia.org/wiki/Aaron_Rai [https://en.wikipedia.org/wiki/Aaron_Rai](https://en.wikipedia.org/wiki/Aaron_Rai)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):
