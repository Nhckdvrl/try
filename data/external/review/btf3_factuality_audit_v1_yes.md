# BTF-3 packet factuality audit v1 — realized YES (32 items)

> External lookup is REQUIRED here: open the citations named in each
> packet and check them. No target-model output may be consulted.
> Nothing decided here changes the frozen 256-unit primary sample.

For each item mark every check, then record one overall verdict:
`PASS` (no material error), `MATERIAL_ERROR` (one or more checks fail
in a way that changes the outcome or its support), or `UNVERIFIABLE`
(cited sources could not be reached or no longer exist). Give exactly
one line of reason for MATERIAL_ERROR and UNVERIFIABLE.

### YES-1. `513056b4-1fab-57a0-817f-480e1d55b703`

- Present date: `2026-05-02 19:35:07.641420` (information window ends end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`
- Recorded realized outcome: **YES**

**Question**

Will the 79th World Health Assembly adopt a resolution explicitly addressing the United States' withdrawal from WHO or its unpaid dues?

**Resolution criteria**

This question resolves as **Yes** if the 79th World Health Assembly (WHA79), during its session from 18–23 May 2026 (CEST, UTC+2), adopts a formal resolution that explicitly mentions the "United States," "US," or "USA" in the context of either (a) the US withdrawal from the WHO, or (b) unpaid US assessed contributions or dues.

This question resolves as **No** if no such resolution is adopted during the 79th WHA session, or if the matter is addressed only through informal discussions, decisions (as distinct from resolutions), Director-General reports, or other non-resolution mechanisms.

**Key definitions:**
- A "resolution" is a formal text adopted by the World Health Assembly, designated with a WHA79.X numbering scheme, as published on the official WHO Governing Bodies resolutions page for WHA79: https://apps.who.int/gb/e/e_wha79.html [WHA79 - World Health Organization (WHO)](https://apps.who.int/gb/e/e_wha79.html).
- The resolution must be adopted during the 79th World Health Assembly session (18–23 May 2026, CEST/UTC+2) to count toward a "Yes" resolution.
- "Addressing" the US withdrawal or unpaid dues means the text or title of the adopted resolution explicitly uses the terms "United States," "US," or "USA" in connection with the country's withdrawal from WHO or its outstanding financial obligations.
- Resolutions that merely reference assessed contributions generically, without specifically naming the United States, do not count.

**Resolution source:** The official list of resolutions adopted by the 79th World Health Assembly, available at https://apps.who.int/gb/e/e_wha79.html. If the definitive versions are not yet posted by 1 June 2026 at 23:59 UTC, resolution may be deferred by up to one week to allow for publication, but no later than 7 June 2026 at 23:59 UTC.

**Exact later resolution packet (the object under audit)**

Adjudicated: The official text of resolution WHA79.2 (adopted 22 May 2026, within the 18-23 May session) explicitly names 'the United States of America' twice in the list of Member States in arrears in the payment of their contributions to an extent justifying Article 7, and decides their voting privileges shall be suspended at WHA80 if still in arrears. This is a formal WHA79.X resolution that specifically names the US in connection with unpaid assessed contributions, satisfying the YES criteria; the 'generic contributions' exclusion does not apply because the US is specifically named.

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-2. `24fd6da5-881c-52a4-8ba1-072443ea34a3`

- Present date: `2026-05-07 22:33:58.056102` (information window ends end of UTC day `2026-05-07`)
- Expected resolution: `2026-06-11T00:00:00`
- Recorded realized outcome: **YES**

**Question**

Will the European Central Bank raise any of its three key interest rates at the June 10-11, 2026 Governing Council meeting?

**Resolution criteria**

This question resolves **Yes** if the European Central Bank announces an increase to any of its three key interest rates—the deposit facility rate, the main refinancing operations rate, or the marginal lending facility rate—as a result of the Governing Council monetary policy meeting scheduled for June 10-11, 2026 (CEST).

This question resolves **No** if the ECB announces that all three key interest rates remain unchanged or are decreased following that meeting.

**Resolution source:** The official ECB "Monetary policy decisions" press release, published at 14:15 CEST on the meeting day, available at: https://www.ecb.europa.eu/press/govcdec/mopo/html/index.en.html [Monetary policy decisions - European Central Bank](https://www.ecb.europa.eu/press/govcdec/mopo/html/index.en.html). The specific press release will follow the URL pattern: https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp260611~[unique_id].en.html [Monetary policy decisions - European Central Bank](https://www.ecb.europa.eu/press/govcdec/mopo/html/index.en.html).

**Exact later resolution packet (the object under audit)**

The question asks whether the ECB raised any of its three key interest rates at the June 10-11, 2026 Governing Council meeting. It resolves YES if an increase to any of the three rates (deposit facility, main refinancing operations, marginal lending facility) was announced as a result of that meeting.

RESOLUTION: YES.

The official ECB "Monetary policy decisions" press release, published 11 June 2026 at https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp260611~4d41bd5e83.en.html, states that the Governing Council decided to raise the three key ECB interest rates by 25 basis points. The new levels are: deposit facility rate 2.25% (up from 2.00%), main refinancing operations rate 2.40% (up from 2.15%), and marginal lending facility rate 2.65% (up from 2.40%), effective 17 June 2026 [7edad8].

This is an INCREASE to all three key rates, satisfying the YES condition (an increase to at least one of the three).

Corroboration:
- Reuters, "ECB raises interest rates in long-telegraphed move" (11 June 2026), reports the ECB increased the deposit rate to 2.25% and the refinancing rate to 2.40% as a result of the meeting [342989].
- Additional secondary sources confirm the hike: CNBC ("ECB hikes interest rates for first time since 2023") and Euronews ("ECB raises interest rates for the first time in three years... deposit facility rate by 0.25% to 2.25%"), and prediction markets (Polymarket/Kalshi) settled on "25 bps increase."

Note on a spurious data point: an initial query of the ECB index page (https://www.ecb.europa.eu/press/govcdec/mopo/html/index.en.html) returned an answer of "unchanged" but cited a URL ending in "81b7179e6f" — which is actually the identifier of the APRIL 30, 2026 press release (rates unchanged), not the June 11 release (whose real ID is "4d41bd5e83"). That was a confusion/hallucination between the April and June releases and is contradicted by the actual June 11 press release and all reputable news reporting [7edad8, 342989].

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-3. `7d4620a7-e855-5c4a-86af-3856e7176d02`

- Present date: `2026-05-11 13:27:02.786193` (information window ends end of UTC day `2026-05-11`)
- Expected resolution: `2026-06-11T00:00:00`
- Recorded realized outcome: **YES**

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

**Exact later resolution packet (the object under audit)**

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

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-4. `741b4bed-7502-5cd2-9cbe-949fbc70f857`

- Present date: `2026-05-07 22:07:47.186771` (information window ends end of UTC day `2026-05-07`)
- Expected resolution: `2026-05-21 00:00:00`
- Recorded realized outcome: **YES**

**Question**

Will Matthew Wale be elected as the next Prime Minister of Solomon Islands following the May 2026 no-confidence vote?

**Resolution criteria**

This question resolves **Yes** if Matthew Wale is formally elected or appointed as [Prime Minister](https://en.wikipedia.org/wiki/Prime_Minister_of_the_Solomon_Islands) of the Solomon Islands and sworn in by the Governor-General on or after May 7, 2026 (00:00 UTC+11, Solomon Islands Time), as the immediate successor to Jeremiah Manele following the May 7, 2026 no-confidence vote.

This question resolves **No** if:
- Any other individual is elected and sworn in as Prime Minister following the no-confidence vote; or
- No new Prime Minister has been sworn in by August 1, 2026 (23:59 UTC+11).

Resolution will be determined by official announcements from the [Solomon Islands Government](https://solomons.gov.sb/) or credible reporting from named news organizations including [ABC News Australia](https://www.abc.net.au/news/), [Radio New Zealand (RNZ)](https://www.rnz.co.nz/), [Reuters](https://www.reuters.com/), or [Associated Press](https://apnews.com/).

**Exact later resolution packet (the object under audit)**

The antecedent occurred, so the question should not be annulled: ABC News Australia reported on May 7, 2026 that Jeremiah Manele “has been voted out of office after a no-confidence motion,” with 26 MPs in the 50-seat parliament siding against him, and that no new leader had yet been identified at that time (URL: https://www.abc.net.au/news/2026-05-07/solomon-islands-new-prime-minister-jeremiah-manele-voted-out/106651634) [Solomon Islands to get new leader after Jeremiah Manele voted out ...](https://www.abc.net.au/news/2026-05-07/solomon-islands-new-prime-minister-jeremiah-manele-voted-out/106651634). The consequent also occurred: RNZ reported that Matthew Cooper Wale was elected Solomon Islands prime minister by secret ballot in Honiara on Friday, May 15, 2026, defeating Peter Shanel Agovaka 26 votes to 22 (URL: https://www.rnz.co.nz/news/pacific/595330/matthew-wale-longtime-opposition-leader-is-new-solomon-islands-prime-minister) [Matthew Wale, longtime opposition leader, is new Solomon Islands ...](https://www.rnz.co.nz/news/pacific/595330/matthew-wale-longtime-opposition-leader-is-new-solomon-islands-prime-minister). RNZ then reported that Wale was sworn in as the new Prime Minister by Governor-General Sir David Tiva Kapu at Government House immediately after his parliamentary election on Friday, May 15, 2026 (URL: https://www.rnz.co.nz/news/pacific/595515/prime-minister-matthew-wale-appoints-cabinet-to-lead-the-solomon-islands) [Prime Minister Matthew Wale appoints Cabinet to lead the Solomon ...](https://www.rnz.co.nz/news/pacific/595515/prime-minister-matthew-wale-appoints-cabinet-to-lead-the-solomon-islands). This swearing-in date is after May 7, 2026 and before the August 1, 2026 deadline [Prime Minister Matthew Wale appoints Cabinet to lead the Solomon ...](https://www.rnz.co.nz/news/pacific/595515/prime-minister-matthew-wale-appoints-cabinet-to-lead-the-solomon-islands). The evidence also rules out the specified NO trigger: ABC stated no replacement had yet been identified immediately after Manele’s ouster, RNZ identified Wale—not Agovaka or anyone else—as the candidate elected in the subsequent prime-ministerial vote, and RNZ stated Wale was sworn in immediately after that election [Solomon Islands to get new leader after Jeremiah Manele voted out ...](https://www.abc.net.au/news/2026-05-07/solomon-islands-new-prime-minister-jeremiah-manele-voted-out/106651634) [Matthew Wale, longtime opposition leader, is new Solomon Islands ...](https://www.rnz.co.nz/news/pacific/595330/matthew-wale-longtime-opposition-leader-is-new-solomon-islands-prime-minister) [Prime Minister Matthew Wale appoints Cabinet to lead the Solomon ...](https://www.rnz.co.nz/news/pacific/595515/prime-minister-matthew-wale-appoints-cabinet-to-lead-the-solomon-islands). Therefore Matthew Wale was the immediate sworn-in successor to Jeremiah Manele following the May 7, 2026 no-confidence vote, so the resolution is YES.

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-5. `66bb32a9-f09d-5c2e-80e8-73da6d84ac4c`

- Present date: `2026-05-14 11:44:34.354218` (information window ends end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`
- Recorded realized outcome: **YES**

**Question**

Will the Latvian Saeima pass a no-confidence motion or will an additional cabinet minister resign in connection with drone incursion incidents between May 12, 2026 and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 (00:00 UTC) and before July 1, 2026 (23:59 UTC), at least one of the following occurs:

1. **No-confidence vote**: The Saeima passes a motion of no confidence (as defined in Article 59 of the Constitution of Latvia: https://www.saeima.lv/en/legislative-process/constitution) in the Prime Minister, the entire Cabinet, or any individual minister, where the motion text or accompanying parliamentary debate explicitly references the drone incursion incidents of May 2026 or the government's handling thereof; OR

2. **Cabinet-level resignation or dismissal**: Any member of the Cabinet of Ministers of Latvia — defined as the Prime Minister or any minister holding a portfolio as listed on the official Cabinet website (https://www.mk.gov.lv/en/cabinet-ministers) — resigns or is dismissed, where the resigning/dismissed official, the Prime Minister, or a formal government statement explicitly cites the drone incursion incidents as a reason for the departure.

The resignation of Defence Minister Andris Sprūds on May 10, 2026 does NOT count, as it occurred before the resolution window.

This question resolves **No** if neither condition is met by July 1, 2026, 23:59 UTC.

**Resolution sources**: Official Latvian government websites (https://www.mk.gov.lv/en, https://www.saeima.lv/en), Latvian public media (https://eng.lsm.lv/), or credible international outlets (Reuters, AP, AFP).

**Exact later resolution packet (the object under audit)**

The question resolves YES via Condition 2 (Cabinet-level resignation), because Latvian Prime Minister Evika Siliņa resigned on May 14, 2026 — squarely within the resolution window (May 12, 2026 00:00 UTC to July 1, 2026 23:59 UTC) — and her departure was explicitly tied to the government's handling of the May 2026 Ukrainian drone incursion incidents.

Key points:

1. The resolution criteria (Condition 2) define an eligible resignation as any Cabinet member — explicitly including "the Prime Minister or any minister holding a portfolio" — resigning where the departure explicitly cites the drone incursion incidents. The Prime Minister therefore counts.

2. Latvian public media LSM (eng.lsm.lv, a specified resolution source) confirms that PM Evika Siliņa (New Unity) resigned on Thursday, May 14, 2026 [e245a6]. Her stated reason was the government crisis stemming directly from the drone-incident fallout: she cited the political blockade over her nominee to replace the Defence Minister who had resigned following the drone strikes, saying "political windbags have chosen a crisis – a government crisis. That is why I am announcing my resignation." The resignation occurred amid a government "seriously shaken by drone incidents" [e245a6].

3. Reuters (a specified resolution source) corroborates the explicit causal link: after "a Ukrainian drone hit an empty oil tank in Latvia on May 7, Silina sacked her defence minister over what she said were inadequate defensive measures by the military, which in turn led to the collapse of her coalition," and the parliament approved a new government under Andris Kulbergs on May 28, 2026 [d0858b].

4. The excluded May 10, 2026 resignation of Defence Minister Andris Sprūds is correctly not the basis for this resolution; the qualifying event is the PM's own May 14, 2026 resignation, which falls inside the window.

Because a Cabinet member (the Prime Minister) resigned within the window with the departure explicitly linked to the drone incidents, the question resolves YES (1). (This holds regardless of whether a formal no-confidence vote under Condition 1 was passed.)

Sources: eng.lsm.lv "Latvian Prime Minister Evika Siliņa steps down" (14.05.2026) https://eng.lsm.lv/article/politics/politics/14.05.2026-latvian-prime-minister-evika-silina-steps-down.a647082/ [e245a6]; Reuters "Latvia parliament approves new government after drone row topples coalition" (2026-05-28) https://www.reuters.com/world/latvia-parliament-approves-new-government-after-drone-row-topples-coalition-2026-05-28/ [d0858b].

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-6. `ec471fcf-d34d-5284-939d-d94961d6436d`

- Present date: `2026-05-12 21:56:41.933544` (information window ends end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`
- Recorded realized outcome: **YES**

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

**Exact later resolution packet (the object under audit)**

The question asks: "Will a first-time major winner be crowned at the 2026 PGA Championship?" It resolves YES if the winner of the 2026 PGA Championship had never previously won any of the four men's major golf championships (The Masters, PGA Championship, U.S. Open, The Open Championship) prior to the conclusion of the 2026 PGA Championship.

WINNER: The 2026 PGA Championship (108th edition), held May 14–17, 2026 at Aronimink Golf Club in Newtown Square, Pennsylvania, was won by Aaron Rai of England. The official PGA Championship website confirms "Aaron Rai wins the 2026 PGA Championship at Aronimink" [2026 PGA Championship Leaderboard - Live Scores](https://www.pgachampionship.com/leaderboard). He won by three strokes, finishing at -9 (271 total), with Jon Rahm and Alex Smalley tied for second at -6/274 (confirmed by multiple leaderboard sources including ESPN and NYT/The Athletic).

TOURNAMENT COMPLETED IN WINDOW: The tournament concluded on Sunday, May 17, 2026, well before the May 31, 2026 (23:59 UTC) cutoff specified in the edge-case criteria, so the question is not N/A.

FIRST-TIME MAJOR WINNER: Aaron Rai's Wikipedia page confirms this was his first career major championship victory. His major championship record shows zero prior major wins — best results were T27 at the 2025 Masters, T11 at the 2026 U.S. Open, and T19 at the 2021 Open Championship, with the PGA Championship listed as "Won: 2026" [https://en.wikipedia.org/wiki/Aaron_Rai](https://en.wikipedia.org/wiki/Aaron_Rai). He became the first Englishman to win the PGA Championship since Jim Barnes in 1919 [https://en.wikipedia.org/wiki/Aaron_Rai](https://en.wikipedia.org/wiki/Aaron_Rai). Thus he had zero wins in any of the four defined majors prior to this victory.

NOT THE 2026 MASTERS WINNER: The 2026 Masters was won by Rory McIlroy (as stated in the question's own description), not Aaron Rai. Therefore the "first-time major winner" criterion is satisfied — Rai did not have any prior major win, including the 2026 Masters.

Because the winner (Aaron Rai) was a first-time major champion, the question resolves YES.

SOURCES:
- Official 2026 PGA Championship results/leaderboard: https://www.pgachampionship.com/leaderboard (and article https://www.pgachampionship.com/news-media/articles/aaron-rai-wins-the-2026-pga-championship-at-aronimink) [2026 PGA Championship Leaderboard - Live Scores](https://www.pgachampionship.com/leaderboard)
- Winner's historical major record: https://en.wikipedia.org/wiki/Aaron_Rai [https://en.wikipedia.org/wiki/Aaron_Rai](https://en.wikipedia.org/wiki/Aaron_Rai)

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-7. `e6bf3057-e9c0-58b7-b18d-b737760937a9`

- Present date: `2026-05-03 04:16:28.735244` (information window ends end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`
- Recorded realized outcome: **YES**

**Question**

Will Apple officially announce a dedicated AI/ML hardware product between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves YES if, between May 1, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC), Apple officially announces a dedicated AI/ML hardware product, OR credible reporting from qualifying sources reveals specific new details about such a product (beyond what was already publicly known before May 1, 2026).

**Definition of 'dedicated AI/ML hardware product':** A standalone consumer electronic device or a dedicated server/chip product whose primary marketed purpose is to serve as an AI/ML interface or AI/ML processing platform. This includes, but is not limited to: an AI-focused home device, an AI wearable (e.g., AI pin, AI glasses), a standalone AI assistant device, or a dedicated AI server chip. This explicitly EXCLUDES: (a) standard annual refreshes of existing product lines (iPhone, iPad, Mac, Apple Watch, AirPods, Apple TV) that simply include updated chips or AI software features; (b) software-only announcements (e.g., new Siri capabilities or Apple Intelligence features announced without new dedicated hardware); (c) the Apple Vision Pro or iterations thereof, unless explicitly marketed as a dedicated AI device rather than a mixed-reality headset.

**Definition of 'official announcement':** A press release on Apple Newsroom (https://www.apple.com/newsroom/) or an official Apple keynote/event.

**Definition of 'credible leak':** Reporting by Bloomberg's Mark Gurman, The Information, The Wall Street Journal, Reuters, or The New York Times that provides specific new product details (e.g., form factor, features, timeline) about a dedicated AI/ML hardware product not previously reported before May 1, 2026. Repetition or elaboration of details already reported before May 1, 2026 does NOT count.

**Primary source of truth:** Apple Newsroom (https://www.apple.com/newsroom/) for official announcements; the publications listed above for leaks.

**Exact later resolution packet (the object under audit)**

The question resolves YES because credible reporting from a qualifying source (Bloomberg's Mark Gurman) revealed specific NEW product details about dedicated AI/ML hardware products during the May 1–June 1, 2026 window, satisfying the "credible leak" branch of the resolution criteria.

The resolution criteria offer an OR condition: YES if either (a) Apple officially announces a dedicated AI/ML hardware product, OR (b) credible reporting from Bloomberg's Mark Gurman, The Information, WSJ, Reuters, or NYT reveals specific NEW product details (form factor, features, timeline) not previously reported before May 1, 2026. No official Apple Newsroom/keynote announcement occurred (WWDC 2026 was June 8–12, after the window), but the leak branch was satisfied multiple times.

Two qualifying Bloomberg/Gurman reports during the window:

1. May 7, 2026 — Gurman/Bloomberg reported new details on Apple's AirTag-sized AI wearable "pendant": it would feature a clip for clothing or a hole for a cord/chain to be worn as a necklace, lacks a display and laser projector (distinguishing it from the Humane AI Pin), and has its own chip with limited performance that relies heavily on a paired iPhone for processing. The report also stated camera-equipped AirPods had reached an advanced testing stage. These form-factor and architecture details were not in the public record before May 1, 2026 [830acb]. (https://www.macrumors.com/2026/05/07/apple-still-working-on-pendant-report/)

2. May 31, 2026 — Gurman/Bloomberg reported new, previously-unreported specifics about Apple's AI smart glasses: a target price range of $200–$500; four potential frame designs (larger rectangular, slimmer rectangular, larger oval/circular, smaller oval/circular); specific colors (black, ocean blue, light brown); vertically-oriented oval camera lenses; turn-by-turn walking directions; and explicit clarification that the first generation will NOT have an in-lens AR display, plus a refined "late 2027" timeline. These specific design/feature/pricing details went well beyond the prior public knowledge that Apple was "working on smart glasses targeting 2027" [ed116d]. (https://www.macrumors.com/2026/05/31/apple-glasses-late-2027-report/ and https://9to5mac.com/2026/06/01/latest-apple-glasses-leak-has-me-way-more-excited-for-the-product/ [061a44])

These products (AI pendant/pin and AI smart glasses) are dedicated AI/ML hardware whose primary marketed purpose is to serve as AI interfaces, explicitly included in the question's definition ("an AI wearable (e.g., AI pin, AI glasses)"), and are not standard refreshes of iPhone/iPad/Mac/Watch/AirPods/Apple TV. The reporting comes from a named qualifying source (Mark Gurman/Bloomberg) and falls strictly within May 1–June 1, 2026. Therefore the question resolves YES.

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-8. `54b20761-0b2d-50b0-b7d6-7242e6c9cbda`

- Present date: `2026-05-14 10:00:32.986920` (information window ends end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`
- Recorded realized outcome: **YES**

**Question**

Will the MTA and all five LIRR unions reach a tentative agreement on a new contract by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026, and on or before July 1, 2026 (11:59 PM ET / 03:59 AM UTC July 2), the Metropolitan Transportation Authority (MTA) and **all five** of the following LIRR unions reach a tentative agreement on a new contract:

1. Brotherhood of Locomotive Engineers and Trainmen (BLET)
2. Brotherhood of Railroad Signalmen (BRS)
3. International Association of Machinists and Aerospace Workers (IAM)
4. International Brotherhood of Electrical Workers (IBEW)
5. Transportation Communications Union (TCU)

A **tentative agreement** is defined as a formal agreement announced by the negotiating parties that is subject to ratification by union membership—distinct from a fully ratified contract. All five unions must have reached tentative agreements for this question to resolve Yes; if even one union has not reached a tentative agreement by the deadline, the question resolves **No**.

Resolution will be determined by official press releases from the MTA (https://new.mta.info/press-releases) or credible news reporting from outlets such as Newsday, amNewYork, Reuters, or the Associated Press confirming that tentative agreements have been reached with all five unions.

**Exact later resolution packet (the object under audit)**

The question resolves YES. On the night of Monday, May 18, 2026 — within the required window of May 12, 2026 to July 1, 2026 — the MTA and the coalition of all five LIRR unions (BLET, BRS, IAM, IBEW, TCU) reached a tentative agreement on a new contract, ending a three-day strike.

Key evidence:
- CBS New York reported: "The Long Island Rail Road strike is over after the Metropolitan Transportation Authority and unions reached a tentative agreement Monday to end the three-day work stoppage," and Gov. Hochul stated "the MTA reached a fair deal with the five LIRR unions." Crucially, it noted "The deal must still be ratified by the five labor unions," satisfying the definition of a tentative agreement (announced but subject to ratification) [684b11].
- The LI Herald confirmed "The three-day Long Island Rail Road strike ended late Monday after five unions and the Metropolitan Transportation Authority reached a tentative agreement," subject to "a 30-day period in which union members will review and vote on the tentative deal before it becomes official" [6eeb01].
- amNewYork reported an MTA official "defended on Tuesday the agency's tentative deal with five Long Island Rail Road unions that ended their first strike in more than three decades," adding "The deal still must be ratified by members of the five unions" [ff0524].
- The International Brotherhood of Teamsters (parent of BLET) issued a May 19, 2026 press release confirming "Teamsters with the Brotherhood of Locomotive Engineers and Trainmen (BLET) and their union coalition have reached a tentative agreement" with LIRR, subject to ratification, referring to the coalition of five unions [790426].

All five named unions negotiated as a single coalition and reached the tentative agreement together, so the requirement that all five reach tentative agreements is met. The date (May 18, 2026) falls within the resolution window, and the agreement is a formally announced tentative deal subject to membership ratification (not a fully ratified contract, and not merely a handshake). Therefore the question resolves YES (1).

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-9. `ce975c54-f33a-55c6-a098-cc572538baf7`

- Present date: `2026-05-12 21:12:43.872694` (information window ends end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`
- Recorded realized outcome: **YES**

**Question**

Will the Council of the European Union formally adopt the EU-US trade deal implementing legislation by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the Council of the European Union formally adopts the legislation implementing the EU-US trade deal (the "Turnberry" agreement concluded in July 2025) on or after May 10, 2026, and on or before July 1, 2026, 23:59 UTC.

"Formal adoption" means the Council's official decision to adopt the implementing legislation, as evidenced by either:
1. Publication of the adopted act in the [Official Journal of the European Union](https://eur-lex.europa.eu/oj/direct-access.html), OR
2. An official press release from the [Council of the European Union](https://www.consilium.europa.eu/en/press/press-releases/) confirming final adoption of the implementing legislation.

If the Council has not formally adopted the implementing legislation by 23:59 UTC on July 1, 2026, this question resolves **No**.

Note: Approval by the European Parliament alone (which occurred in March 2026) does not satisfy this criterion. The Council's adoption is the final legislative step required.

**Exact later resolution packet (the object under audit)**

The question resolves YES.

The resolution criteria require that the Council of the European Union formally adopt the legislation implementing the EU-US ("Turnberry") trade deal on or after May 10, 2026, and on or before July 1, 2026, 23:59 UTC, as evidenced by either publication in the Official Journal OR an official Council of the EU press release confirming final adoption.

This condition was satisfied. On June 25, 2026, the Council of the European Union published an official press release ("EU-US trade: Council gives final approval for the tariff commitments under joint statement", https://www.consilium.europa.eu/en/press/press-releases/2026/06/25/eu-us-trade-council-gives-final-approval-for-the-tariff-commitments-under-joint-statement/) stating that the Council "formally adopted two regulations implementing the tariff-related commitments set out in the EU-US Joint Statement of 21 August 2025," and that "The adoption completes the legislative process" [EU-US trade: Council gives final approval for the tariff commitments ...](https://www.consilium.europa.eu/en/press/press-releases/2026/06/25/eu-us-trade-council-gives-final-approval-for-the-tariff-commitments-under-joint-statement/). June 25, 2026 falls squarely within the required window (May 10 – July 1, 2026).

This is corroborated by Reuters ("EU governments adopt legislation to fulfil EU side of US trade deal", https://www.reuters.com/business/eu-governments-adopt-legislation-fulfil-eu-side-us-trade-deal-2026-06-25/), which reported that "European Union governments adopted on Thursday [June 25, 2026] legislation to remove import duties on many U.S. goods, fulfilling the EU's side of a trade deal struck with U.S. President Donald Trump last year," specifically attributing the action to "the Council, the grouping of EU governments" [EU governments adopt legislation to fulfil EU side of US trade deal](https://www.reuters.com/business/eu-governments-adopt-legislation-fulfil-eu-side-us-trade-deal-2026-06-25/).

The action was taken by the Council of the European Union specifically — the final legislative step — and NOT merely the European Parliament (whose approval in March/June 2026 is explicitly excluded as a trigger). The two regulations implement the tariff commitments of the EU-US Joint Statement, which is the formal instrument stemming from the July 2025 Turnberry framework agreement between Trump and von der Leyen (the deal is widely referred to as the "Turnberry Deal"; the July 2025 Turnberry meeting produced the framework subsequently formalized in the 21 August 2025 Joint Statement).

Therefore, the Council formally adopted the Turnberry-implementing legislation on June 25, 2026, within the resolution window, and the question resolves YES.

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-10. `d345aa2e-74af-55d1-9b2e-e62e78291dd4`

- Present date: `2026-05-13 13:23:22.112950` (information window ends end of UTC day `2026-05-13`)
- Expected resolution: `2026-07-01T00:00:00`
- Recorded realized outcome: **YES**

**Question**

Will the Cour d'assises des Alpes-Maritimes maintain the legal qualification of "viol par surprise" in its appeal verdict against Jack Sion?

**Resolution criteria**

This question resolves **Yes** if the cour d'assises des Alpes-Maritimes, in a verdict issued on or after May 10, 2026 (UTC), explicitly convicts Jack Sion of "viol par surprise" (rape by surprise/deception) or "viol commis par stratagème" — i.e., maintains the legal qualification of rape based on the element of "surprise" as defined in Article 222-23 of the French Penal Code (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000052535571). "Maintaining the legal qualification" means the court finds Sion guilty of rape ("viol") on at least one count where the absence of consent is established through "surprise" (deception/stratagem).

This question resolves **No** if the court:
- Acquits Sion of all rape charges, OR
- Requalifies the acts as a lesser offense, such as "agression sexuelle" (sexual assault, defined under Articles 222-27 et seq. of the French Penal Code), that does not include the qualification of rape by surprise.

Resolution will be determined by credible reporting from major French news outlets such as AFP, Le Monde, Le Figaro, France Info, Nice-Matin, or CNews (e.g., https://www.cnews.fr/faits-divers/2026-05-06/affaire-jack-sion-le-faux-playboy-du-net-rejuge-partir-de-ce-mercredi). If no verdict is issued by June 30, 2026 (UTC), this question resolves **No**.

**Exact later resolution packet (the object under audit)**

The question resolves YES. On Wednesday, May 13, 2026, the cour d'assises des Alpes-Maritimes (the appeal court in Nice, referred to as the "cour d'appel de Nice") issued its verdict in the appeal trial of Jack Sion, convicting him of three counts of "viols par surprise" (rape by surprise) and sentencing him to 18 years of criminal imprisonment (réclusion criminelle), a heavier sentence than the 8 years imposed at first instance in 2021.

This satisfies every element of the resolution criteria:

1. Correct court (appeal court, not the original lower court): The verdict was issued by the cour d'assises des Alpes-Maritimes / cour d'appel de Nice, the appeal court, on the appeal of the 2021 conviction by the cour criminelle départementale de l'Hérault (Montpellier). France Info states: "Un homme de 79 ans... a été condamné par la cour d'appel de Nice, mercredi 13 mai, à 18 ans de prison pour 'viols par surprise' sur trois femmes, avec mandat de dépôt." [Un homme de 79 ans, qui se faisait passer pour un trentenaire sur ...](https://www.franceinfo.fr/faits-divers/un-homme-de-79-ans-qui-se-faisait-passer-pour-un-trentenaire-sur-des-sites-de-rencontres-condamne-a-18-ans-de-prison-pour-viols-par-surprise_8002418.html) Nice-Matin confirms the conviction "en appel par la cour d'assises des Alpes-Maritimes" [18 ans de réclusion criminelle pour le Niçois Jack Sion ... - Nice-Matin](https://www.nicematin.com/faits-divers/18-ans-de-reclusion-criminelle-pour-jack-sion-18-ans-de-reclusion-criminelle-pour-jack-sion-le-faux-play-boy-du-net-10680559).

2. Verdict date within window (May 10 – June 30, 2026 inclusive): The verdict was rendered on May 13, 2026 [Un homme de 79 ans, qui se faisait passer pour un trentenaire sur ...](https://www.franceinfo.fr/faits-divers/un-homme-de-79-ans-qui-se-faisait-passer-pour-un-trentenaire-sur-des-sites-de-rencontres-condamne-a-18-ans-de-prison-pour-viols-par-surprise_8002418.html) [18 ans de réclusion criminelle pour le Niçois Jack Sion ... - Nice-Matin](https://www.nicematin.com/faits-divers/18-ans-de-reclusion-criminelle-pour-jack-sion-18-ans-de-reclusion-criminelle-pour-jack-sion-le-faux-play-boy-du-net-10680559), which is within the required window.

3. Conviction for "viol" (rape) maintained on at least one count (not requalified to mere "agression sexuelle"): He was found guilty of THREE counts of "viols par surprise" [18 ans de réclusion criminelle pour le Niçois Jack Sion ... - Nice-Matin](https://www.nicematin.com/faits-divers/18-ans-de-reclusion-criminelle-pour-jack-sion-18-ans-de-reclusion-criminelle-pour-jack-sion-le-faux-play-boy-du-net-10680559), so the rape qualification was maintained on multiple counts.

4. Conviction based specifically on the "surprise" element (deception/stratagem) per Article 222-23: The conviction is explicitly for "viols par surprise." France Info explains the concept: "Le viol par surprise peut faire référence à un mensonge, lorsque l'auteur surprend sa victime en obtenant son consentement en lui faisant croire des choses erronées pour avoir une relation sexuelle." [Un homme de 79 ans, qui se faisait passer pour un trentenaire sur ...](https://www.franceinfo.fr/faits-divers/un-homme-de-79-ans-qui-se-faisait-passer-pour-un-trentenaire-sur-des-sites-de-rencontres-condamne-a-18-ans-de-prison-pour-viols-par-surprise_8002418.html)

Named resolution sources used: France Info (https://www.franceinfo.fr/faits-divers/un-homme-de-79-ans-qui-se-faisait-passer-pour-un-trentenaire-sur-des-sites-de-rencontres-condamne-a-18-ans-de-prison-pour-viols-par-surprise_8002418.html) [Un homme de 79 ans, qui se faisait passer pour un trentenaire sur ...](https://www.franceinfo.fr/faits-divers/un-homme-de-79-ans-qui-se-faisait-passer-pour-un-trentenaire-sur-des-sites-de-rencontres-condamne-a-18-ans-de-prison-pour-viols-par-surprise_8002418.html) and Nice-Matin (https://www.nicematin.com/faits-divers/18-ans-de-reclusion-criminelle-pour-jack-sion-18-ans-de-reclusion-criminelle-pour-jack-sion-le-faux-play-boy-du-net-10680559) [18 ans de réclusion criminelle pour le Niçois Jack Sion ... - Nice-Matin](https://www.nicematin.com/faits-divers/18-ans-de-reclusion-criminelle-pour-jack-sion-18-ans-de-reclusion-criminelle-pour-jack-sion-le-faux-play-boy-du-net-10680559). Additional corroboration appears in Midi Libre's headline "Jack Sion, le 'play-boy du Net', reconnu coupable de 'viols par surprise'... condamné à 18 ans de réclusion" and BFMTV's report of the same verdict.

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-11. `a605b42c-6c3a-5d87-bae3-7b8b37a42bc8`

- Present date: `2026-04-29 23:25:40.530726` (information window ends end of UTC day `2026-04-29`)
- Expected resolution: `2026-06-01 00:00:00`
- Recorded realized outcome: **YES**

**Question**

Will any U.S. congressional committee vote to report AI-specific legislation to the full House or Senate by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after the question's open date and on or before June 1, 2026 (23:59 UTC), any standing committee or subcommittee of the U.S. House of Representatives or U.S. Senate votes to order a bill "reported" (see [Senate glossary](https://www.senate.gov/reference/glossary_term/report.htm)) to the full chamber, where that bill is "AI-specific legislation" as defined below.

**AI-specific legislation** means a bill that has "artificial intelligence" or "AI" in its official title (short title or long title as shown on [Congress.gov](https://www.congress.gov/)), OR whose primary subject matter as categorized on Congress.gov falls under artificial intelligence policy.

A **vote to report** means the committee has completed a [markup](https://www.senate.gov/reference/glossary_term/markup.htm) and formally ordered the bill to be reported to the full House or Senate. This is tracked on each bill's "Actions" or "Committees" tab on Congress.gov (e.g., "Ordered to be reported" or "Reported by committee").

The resolution source is [Congress.gov](https://www.congress.gov/search?q=%7B%22source%22%3A%22legislation%22%2C%22congress%22%3A%22119%22%2C%22subject%22%3A%22Artificial+intelligence%22%7D), specifically the committee actions listed on individual bill pages. If Congress.gov shows that any AI-specific bill (as defined above) has been "ordered to be reported" by a committee on or after the question's open date and on or before June 1, 2026, the question resolves **Yes**. Otherwise, it resolves **No**.

**Exact later resolution packet (the object under audit)**

The question resolves YES because the House Committee on Small Business voted to report favorably (i.e., ordered to be reported) an AI-specific bill within the resolution window of April 29, 2026 through June 1, 2026.

Specifically, on May 20, 2026, the full House Committee on Small Business, chaired by Rep. Roger Williams (TX-25), held a markup and reported favorably to the House nine bills, including H.R. 8881, the "SBA Artificial Intelligence Utilization Act of 2026," by a recorded vote of 23 Yea to 0 Nay [c1a7b7]. FedScoop independently confirms the committee unanimously approved the SBA Artificial Intelligence Utilization Act (H.R. 8881) in a Wednesday markup [f7e95e].

This satisfies all resolution criteria:
1. AI-specific legislation: H.R. 8881's official short title contains "Artificial Intelligence" ("SBA Artificial Intelligence Utilization Act of 2026") [c1a7b7].
2. Vote to report: The committee completed a markup and ordered the bill reported ("Reported Favorably to the House," 23-0) — not a mere referral [c1a7b7]. The Congress.gov committees tab also shows "House Small Business — 05/20/2026 — Markup By" following the 05/19/2026 referral.
3. Timing: The markup/order to report occurred May 20, 2026, which falls within the window (on/after April 29, 2026 and on/before June 1, 2026 23:59 UTC).

URL for the qualifying bill: https://www.congress.gov/bill/119th-congress/house-bill/8881
Committee press release: https://smallbusiness.house.gov/news/documentsingle.aspx?DocumentID=407452

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-12. `82f810af-002d-5361-bec4-2546bb30b9df`

- Present date: `2026-05-16 11:15:22.967852` (information window ends end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`
- Recorded realized outcome: **YES**

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

**Exact later resolution packet (the object under audit)**

Adjudicated: An AFP wire report dated May 30, 2026 (byline AFP, republished at Arab News node/2645459, The News, New Arab, Frontier Post) describes an armed clash on Saturday May 30, 2026 on the outskirts of Baidoa (Idoow Dhagoole area, north of the city) between Somali federal government/army troops and fighters loyal to ousted South West State president Abdiaziz Hassan Mohamed 'Laftagareen'. The military commander Hussein Ali told AFP his forces counted ~six bodies of attackers and a resident reported two civilians wounded by stray bullets, satisfying the 'exchange of gunfire with at least one casualty' definition. This falls within the May 12 00:00 UTC - July 1 23:59 UTC window, is inside Baidoa district (~within 30 km), and Laftagareen loyalists explicitly qualify as 'South West State-aligned forces' / 'armed groups opposing federal forces in the context of the SWS political dispute.' The report comes from AFP, one of the named resolution sources. An earlier automated NO relied on failing to load the JS-rendered ReliefWeb page and missed the AFP reporting entirely.

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-13. `ee51ff77-017d-5b54-8523-09a424b7bee0`

- Present date: `2026-05-03 04:38:07.553426` (information window ends end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`
- Recorded realized outcome: **YES**

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

**Exact later resolution packet (the object under audit)**

RESOLUTION: YES (1).

ANTECEDENT/TIMING: Governor Jared Polis signed Senate Bill 26-189 into law on May 14, 2026, which falls within the question's resolution window of May 1, 2026 through June 1, 2026 (23:59 UTC). The official Colorado General Assembly bill page (https://leg.colorado.gov/bills/sb26-189) confirms the bill was signed by the Governor on May 14, 2026, and that it "repeals and reenacts" the provisions originally enacted via SB 24-205 [https://leg.colorado.gov/bills/sb26-189](https://leg.colorado.gov/bills/sb26-189). Multiple independent law-firm analyses corroborate the May 14, 2026 signing date [Colorado AI Act Repealed and Replaced by Narrower Statute ...](https://www.dwt.com/blogs/privacy--security-law-blog/2026/05/colorado-ai-act-repeal-new-transparency-law) [Colorado enacts revised AI law | United States - Norton Rose Fulbright](https://www.nortonrosefulbright.com/en-us/knowledge/publications/18733d31/colorado-enacts-revised-ai-law).

SUBSTANTIVE CRITERIA MET: The question requires the signed bill to do at least ONE of three things (strike the definition of "algorithmic discrimination" in 6-1-1701(1)(a); eliminate deployer impact assessments in 6-1-1703(3); or eliminate the affirmative duty to avoid algorithmic discrimination), and explicitly states that replacing substantive obligations with transparency-only/notice-only requirements qualifies as a "removal." SB 26-189 satisfies multiple of these criteria:
- It removes "the duty of care to mitigate algorithmic discrimination risks, requirements regarding algorithmic discrimination, and requirements to perform annual impact assessments and maintain a risk management program," replacing the high-risk AI framework with an "automated decision-making technology" (ADMT) framework centered on notice, documentation, and consumer rights [Colorado enacts revised AI law | United States - Norton Rose Fulbright](https://www.nortonrosefulbright.com/en-us/knowledge/publications/18733d31/colorado-enacts-revised-ai-law).
- DWT confirms the new law "abandons the CAIA's extensive risk-management and impact-assessment requirements" and shifts away from the CAIA's "duties of care" and "affirmative avoidance" requirements, replacing them with transparency/notice, documentation, and consumer-rights obligations [Colorado AI Act Repealed and Replaced by Narrower Statute ...](https://www.dwt.com/blogs/privacy--security-law-blog/2026/05/colorado-ai-act-repeal-new-transparency-law).
- Troutman confirms SB 189 "removes many of the hallmarks of the Colorado AI Act — such as a duty of care, risk management programs, and impact assessments — in favor of a disclosure-based framework" and "does not contain any reference to algorithmic discrimination, duties of care, risk management programs, impact assessments" [Colorado Legislature Passes Bill to Repeal and Replace Colorado ...](https://www.troutmanprivacy.com/2026/05/colorado-legislature-passes-bill-to-repeal-and-replace-colorado-ai-act/).

DELAY-VS-REMOVAL DISTINCTION: This is not merely a delay of the effective date (an earlier SB 25B-004 in August 2025 did that). SB 26-189 substantively repeals/replaces the impact assessment requirement and the affirmative duty to avoid algorithmic discrimination with a disclosure/transparency-based framework, which the resolution criteria explicitly count as qualifying "removal."

NOTE ON CONFLICTING TOOL OUTPUT: One automated read of the leg.colorado.gov page [https://leg.colorado.gov/bills/sb26-189](https://leg.colorado.gov/bills/sb26-189) suggested NO on the theory that "repeals and reenacts" maintains regulatory oversight. That reasoning is incorrect under the question's own resolution criteria, which expressly state that replacing the impact assessment/affirmative duty obligations with transparency-only or disclosure-only requirements DOES qualify as a removal. The substantive content (removal of impact assessments and the algorithmic-discrimination duty of care, replaced by a disclosure-based ADMT framework) is confirmed by three independent legal sources [Colorado AI Act Repealed and Replaced by Narrower Statute ...](https://www.dwt.com/blogs/privacy--security-law-blog/2026/05/colorado-ai-act-repeal-new-transparency-law) [Colorado enacts revised AI law | United States - Norton Rose Fulbright](https://www.nortonrosefulbright.com/en-us/knowledge/publications/18733d31/colorado-enacts-revised-ai-law) [Colorado Legislature Passes Bill to Repeal and Replace Colorado ...](https://www.troutmanprivacy.com/2026/05/colorado-legislature-passes-bill-to-repeal-and-replace-colorado-ai-act/).

PRIMARY SOURCE URL: https://leg.colorado.gov/bills/sb26-189

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-14. `ac8fbd78-aafd-573c-bddb-0b5f251d9fb4`

- Present date: `2026-05-16 20:47:01.321918` (information window ends end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`
- Recorded realized outcome: **YES**

**Question**

Will Junts per Catalunya vote in favor of any Spanish government-sponsored decreto-ley in the Congress of Deputies between May 12, 2026 and July 1, 2026?

**Resolution criteria**

This question resolves YES if, between May 12, 2026, 00:00 UTC and July 1, 2026, 23:59 UTC, Junts per Catalunya's parliamentary group in the Congress of Deputies casts a majority of its votes in favor of ratifying at least one gobierno-sponsored decreto-ley (Royal Decree-Law) in a plenary vote. Abstentions do not count as votes in favor.

This question resolves NO if either: (a) no gobierno-sponsored decreto-ley is put to a ratification vote in the Congress during this period, or (b) Junts votes against or abstains on every such decreto-ley voted on during this period.

A "gobierno-sponsored decreto-ley" is a Royal Decree-Law (Real Decreto-ley) approved by the Council of Ministers and submitted to the Congress for ratification under Article 86 of the Spanish Constitution.

Resolution source: Official voting records of the Congress of Deputies, available at https://www.congreso.es/en/votaciones, or credible reporting from major Spanish news outlets such as El País (https://elpais.com), La Vanguardia (https://www.lavanguardia.com), or agencies such as EFE or Reuters.

**Exact later resolution packet (the object under audit)**

The question resolves YES.

**Key event:** On Thursday, June 18, 2026, the Congress of Deputies convalidated (ratified) a government-sponsored Real Decreto-ley that updated the "entregas a cuenta" (advance financing transfers) for autonomous communities (~151,731 million euros) and municipalities (~29,247 million euros) for 2026. This is a Royal Decree-Law approved by the Council of Ministers and submitted to Congress for ratification under Article 86 of the Spanish Constitution — precisely the type of instrument specified in the resolution criteria.

**Junts' vote:** Junts per Catalunya's parliamentary group voted IN FAVOR of ratifying this Real Decreto-ley. La Vanguardia (a resolution-source outlet named in the criteria), published June 18, 2026, explicitly states Junts announced its "voto favorable" to the convalidation [El Congreso convalidará el decreto de entregas a cuenta a ...](https://www.lavanguardia.com/politica/20260618/11568156/congreso-convalidara-decreto-entregas-cuenta-comunidades-ayuntamientos-votos-junts-pnv.html). elDiario.es corroborates this: PNV and Junts confirmed their support, and Junts deputy Josep Maria Cruset "defended the 'yes' to the convalidation" on that Thursday (June 18, 2026) [PNV y Junts confirman su apoyo al decreto de entregas a ... - El Diario](https://www.eldiario.es/economia/pnv-junts-confirman-apoyo-decreto-entregas-cuenta-permitiran-salga-adelante-congreso_1_13313979.html). Reporting from Público and ABC (seen in search results) indicated Vox was essentially the only group voting against, meaning Junts' seven deputies backed the decree — a clear majority of the group's votes in favor, not abstentions.

**Timing:** June 18, 2026 falls strictly within the resolution window of May 12, 2026 (00:00 UTC) to July 1, 2026 (23:59 UTC).

**Contrast with rejections:** The question's context noted Junts had joined PP and Vox to reject the rental decree on April 28, 2026 (before the window). Search results also show that on June 25, 2026, Junts brought down another government decree and abstained on the "bono joven de transporte" decree. But the criteria only require Junts to vote a majority in favor of AT LEAST ONE decreto-ley ratification during the window, which the June 18 entregas a cuenta decree satisfies.

**Source URL:** La Vanguardia: https://www.lavanguardia.com/politica/20260618/11568156/congreso-convalidara-decreto-entregas-cuenta-comunidades-ayuntamientos-votos-junts-pnv.html ; elDiario.es: https://www.eldiario.es/economia/pnv-junts-confirman-apoyo-decreto-entregas-cuenta-permitiran-salga-adelante-congreso_1_13313979.html . The official congreso.es voting record for the June 18, 2026 plenary session would further document this ratification vote.

All resolution criteria conditions (a) a Real Decreto-ley ratification vote occurred in the window, and (b) Junts cast a majority of its votes in favor — are met. Resolution: YES (1).

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-15. `630b345d-eb03-534c-a3e5-5de067aaed7b`

- Present date: `2026-05-14 11:24:43.947611` (information window ends end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`
- Recorded realized outcome: **YES**

**Question**

Will the rapporteur of PEC 14/2021 in the Senate CCJ present a report recommending approval without substantive amendments by July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 12, 2026 and by 23:59 UTC on July 1, 2026, the rapporteur of PEC 14/2021 in the Senate CCJ (Senator Irajá) formally presents a report (parecer) to the CCJ that recommends the approval of the PEC without substantive amendments (emendas de mérito).

**Definition of "substantive amendments" (emendas de mérito):** Any amendments that alter the legal content, scope, eligibility criteria, benefit calculations, fiscal responsibilities, or any other provision of the PEC's text as received from the Chamber of Deputies. Substantive amendments are those that, under Brazilian legislative procedure, would require the PEC to return to the Chamber of Deputies for a new round of voting. Purely redactional or grammatical corrections that do not change the legal effect of the text are not considered substantive amendments.

**Definition of "presenting" a report:** The formal submission (apresentação) of the rapporteur's report to the CCJ, as recorded in the official legislative system of the Federal Senate. This is verified by the appearance of the report in the tramitação (legislative history) section of the PEC's official page on the Senate portal.

This question resolves as **No** if:
1. The rapporteur presents a report that includes one or more substantive amendments; or
2. The rapporteur presents a report recommending rejection of the PEC; or
3. No report is formally presented by the rapporteur by 23:59 UTC on July 1, 2026.

**Resolution source:** The official tracking page of PEC 14/2021 on the Brazilian Federal Senate portal: https://www25.senado.leg.br/web/atividade/materias/-/materia/170850. If this page is temporarily unavailable, credible reporting from major Brazilian news outlets (e.g., Agência Senado at https://www12.senado.leg.br/noticias, G1, Folha de S.Paulo, O Globo) may be used as a secondary source.

**Exact later resolution packet (the object under audit)**

RESOLUTION: YES (1).

The question resolves YES if, between May 12, 2026 and 23:59 UTC July 1, 2026, rapporteur Senator Irajá formally presented a report (parecer) to the Senate CCJ recommending approval of PEC 14/2021 WITHOUT substantive amendments (emendas de mérito). All conditions are satisfied.

1) A report WAS presented within the window by the designated rapporteur. The official Senate tramitação for PEC 14/2021 shows Senator Irajá presented his Relatório Legislativo on May 21, 2026, and the CCJ approved the resulting Parecer (P.S. 44/2026-CCJ) on June 10, 2026, recorded as "favorável à Proposta e contrário à Emenda nº 2" [499ec7]. May 21 falls within the May 12 – July 1, 2026 window, and Irajá is the designated rapporteur.

2) The report RECOMMENDS APPROVAL. The parecer's VOTO section reads verbatim: "...no mérito, pela sua aprovação e pela rejeição da Emenda nº 2" — i.e., on the merits, FOR its approval and FOR the rejection of Amendment No. 2 [5e2932]. The Senate news confirms the rapporteur's report was favorable and the PEC advanced to two rounds of plenary voting [77b91e].

3) The report does NOT include/adopt any substantive amendment (the crux). Only two amendments were tabled — by OTHER senators, not by Irajá. Emenda nº 1 was withdrawn by its own author, and Emenda nº 2 (Senator Veneziano Vital do Rêgo, MDB-PB), which sought to keep the current constitutional wording of art. 198 §10, was REJECTED by the rapporteur [5f03c6, 77b91e]. Rejecting amendments proposed by others is the opposite of "including" substantive amendments; it preserves the text exactly as received from the Chamber of Deputies.

4) The report explicitly keeps the PEC from returning to the Chamber. The parecer states that approving Emenda nº 2 "faria com que a PEC retornasse à Câmara dos Deputados para nova apreciação," which is precisely why Irajá rejected it [5f03c6]. Since the defining test of a "substantive amendment" per the resolution criteria is whether it would force the PEC back to the Chamber, and Irajá's report deliberately avoids any such change, the report recommends approval without substantive amendments. Consistent with this, contemporaneous reporting noted that if the Senate passed the text "sem alterações," it would go straight to promulgation (not back to the Chamber).

None of the three NO conditions is met: the report does not include substantive amendments (condition 1), does not recommend rejection (condition 2 — it is favorable), and was in fact presented before the deadline (condition 3). Therefore the question resolves YES.

Note on contradictory automated readings: Several document-extraction passes returned "NO," but each rested on a misreading — treating the mere discussion/rejection of an amendment as "including" one [77b91e, 5f03c6, 5e2932, 8452aa], or, in one case, speculating from the question's own preamble about a "consensus text" rather than citing article content [777a28]. The actual VOTO ("aprovação e rejeição da Emenda nº 2") and the withdrawal of Emenda 1 make clear no substantive amendment was adopted.

SOURCES:
- Official Senate tracking page (tramitação): https://www25.senado.leg.br/web/atividade/materias/-/materia/170850 [499ec7]
- Parecer PDF (Senado): https://legis.senado.leg.br/sdleg-getter/documento?dm=10229057&ts=1779404257771&rendition_principal=S&disposition=inline [5f03c6, 5e2932]
- Agência Senado (June 10, 2026): https://www12.senado.leg.br/noticias/materias/2026/06/10/aposentadoria-especial-para-agentes-de-saude-e-endemias-vai-a-plenario [77b91e]

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-16. `e9efc313-b658-5f08-9131-d6ebdeba1e68`

- Present date: `2026-05-01 19:14:36.536940` (information window ends end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`
- Recorded realized outcome: **YES**

**Question**

Will SpaceX launch Starship Flight 12 (first Version 3 / Block 3 flight) before 23:59 UTC on June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if SpaceX's Starship Flight 12—the first flight using Version 3 / Block 3 hardware—lifts off from the launch pad (defined as the vehicle clearing the launch mount/tower under its own power) on or after April 30, 2026, and before 23:59 UTC on June 1, 2026.

The question resolves **No** if no such liftoff occurs by that deadline.

"Launch" is defined as the vehicle lifting off the launch pad and clearing the tower under its own power. A launch abort after engine ignition that does not result in the vehicle leaving the pad does not count.

"Version 3" / "Block 3" refers to the third major hardware iteration of the Starship-Super Heavy system as described on the Wikipedia Starship page (https://en.wikipedia.org/wiki/SpaceX_Starship) and tracked on the List of Starship launches (https://en.wikipedia.org/wiki/List_of_Starship_launches).

**Resolution sources:** SpaceX's official launches page (https://www.spacex.com/launches), Next Spaceflight's Flight 12 page (https://nextspaceflight.com/launches/details/8002/), or credible spaceflight reporting from outlets such as Space.com, NASASpaceFlight.com, or Ars Technica.

**Exact later resolution packet (the object under audit)**

The question resolves YES. SpaceX's official Flight 12 page states that "On Friday, May 22, 2026, at 5:30 p.m. CT, Starship lifted off from Starbase, Texas on its twelfth flight test," and confirms it was the first flight of the Starship and Super Heavy V3 (Version 3 / Block 3) vehicles [a9e333]. Wikipedia's "Starship flight test 12" article gives a precise liftoff time of May 22, 2026, 22:30:22 UTC, with all engines lit at liftoff (confirming the vehicle cleared the launch mount/tower under its own power), and confirms it used Version 3 / Block 3 hardware with Booster 19 and Ship 39 [7a6ce9].

Window check: The resolution criteria require liftoff on or after April 30, 2026 and before 23:59 UTC on June 1, 2026. The liftoff at 22:30:22 UTC on May 22, 2026 falls squarely within this window. (Note: an initial attempt on May 21 was scrubbed, but the actual launch occurred May 22.)

All checklist conditions met: (1) liftoff within the window; (2) vehicle cleared the tower under its own power with all engines lit (not just ignition or pad abort); (3) it was the first Version 3 / Block 3 flight (Flight 12) using Booster 19 and Ship 39; (4) supported by allowed sources SpaceX (https://www.spacex.com/launches/starship-flight-12) and credible reporting; time zone correctly converted from 5:30 p.m. CT to 22:30 UTC, still before the deadline.

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-17. `f8b8e64a-1462-56e8-8e51-2378eaca309f`

- Present date: `2026-05-01 10:40:50.314413` (information window ends end of UTC day `2026-05-01`)
- Expected resolution: `2026-05-21 00:00:00`
- Recorded realized outcome: **YES**

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

**Exact later resolution packet (the object under audit)**

The question resolves YES. The official Federal Reserve FOMC calendar entry for the April 28–29, 2026 meeting lists the minutes at https://www.federalreserve.gov/monetarypolicy/fomcminutes20260429.htm and https://www.federalreserve.gov/monetarypolicy/files/fomcminutes20260429.pdf, with “Released May 20, 2026,” which is before the June 1, 2026 23:59 UTC deadline [The Fed - Meeting calendars and information - Federal Reserve](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm). In those official minutes, a qualifying rate-hike-openness sentiment is attributed to a stronger-than-“some” quantifier: “A majority of participants highlighted, however, that some policy firming would likely become appropriate if inflation were to continue to run persistently above 2 percent” [https://www.federalreserve.gov/monetarypolicy/files/fomcminutes20260429.pdf](https://www.federalreserve.gov/monetarypolicy/files/fomcminutes20260429.pdf). The quantifier over participants is “A majority of participants,” and the resolution criteria explicitly count “a majority of” as sufficient. The minutes also state: “To address this possibility, many participants indicated that they would have preferred removing the language from the postmeeting statement that suggested an easing bias regarding the likely direction of the Committee’s future interest rate decisions” [https://www.federalreserve.gov/monetarypolicy/files/fomcminutes20260429.pdf](https://www.federalreserve.gov/monetarypolicy/files/fomcminutes20260429.pdf). This matches the specified “removing or opposing the easing bias” sentiment, and “many” is strictly higher than “some” on the provided hierarchy. Therefore the April minutes did use a stronger quantifier than “some” for participants expressing openness to rate hikes [https://www.federalreserve.gov/monetarypolicy/files/fomcminutes20260429.pdf](https://www.federalreserve.gov/monetarypolicy/files/fomcminutes20260429.pdf).

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-18. `769d43d1-f7c7-5f51-bb05-562a4222c358`

- Present date: `2026-05-02 21:37:29.499567` (information window ends end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`
- Recorded realized outcome: **YES**

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

**Exact later resolution packet (the object under audit)**

The question resolves YES because Fitch Ratings upgraded the long-term foreign-currency sovereign credit rating of Argentina—a G20 member—within the resolution window (00:00 UTC May 1, 2026 to 23:59 UTC June 1, 2026).

Evidence: The official Fitch Ratings press release "Fitch Upgrades Argentina to 'B-'; Outlook Stable," dated New York, 05 May 2026, states that Fitch upgraded Argentina's Long-Term Foreign Currency (and Local Currency) Issuer Default Rating to 'B-' from 'CCC+' [Fitch Upgrades Argentina to 'B-'; Outlook Stable](https://www.fitchratings.com/research/sovereigns/fitch-upgrades-argentina-to-b-outlook-stable-05-05-2026). This is a notch upgrade (not merely an outlook change) of the precise rating type tracked by the question (Fitch's "Long-Term Foreign-Currency Issuer Default Rating"). URL: https://www.fitchratings.com/research/sovereigns/fitch-upgrades-argentina-to-b-outlook-stable-05-05-2026

Argentina is explicitly listed as one of the 19 sovereign G20 members in the question's criteria. The press release date (May 5, 2026) falls squarely within the May 1–June 1, 2026 window. This single qualifying event is sufficient for a YES resolution. (Other G20 reviews in the window—e.g., S&P affirming Italy at BBB+, Moody's changing South Africa's outlook to positive without a notch upgrade, S&P affirming Mexico, Fitch affirming France—did not produce upgrades, but they are immaterial given the Argentina upgrade already satisfies the criteria.)

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-19. `9e807f3f-c7c7-515d-895a-a18fbb170141`

- Present date: `2026-05-16 17:43:49.456916` (information window ends end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`
- Recorded realized outcome: **YES**

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

**Exact later resolution packet (the object under audit)**

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

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-20. `e35b83e5-edc5-5778-9c3a-7ac64e877a6f`

- Present date: `2026-04-30 18:28:43.603372` (information window ends end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`
- Recorded realized outcome: **YES**

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

**Exact later resolution packet (the object under audit)**

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

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-21. `fe39b56b-8133-5518-918a-09f312b235df`

- Present date: `2026-05-03 05:34:54.852556` (information window ends end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`
- Recorded realized outcome: **YES**

**Question**

Will Cerebras Systems' stock close above its IPO offer price on its first day of trading by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if all of the following conditions are met:

1. Cerebras Systems completes its initial public offering (IPO) and its Class A common stock begins trading on the Nasdaq (expected ticker: CBRS) on or before June 1, 2026, at 23:59 UTC.
2. The **closing price** on the first day of trading is strictly greater than the **IPO offer price** (also called the "IPO price").

**Definitions:**
- **IPO offer price** (also "offer price"): The price per share at which shares are sold to institutional and retail investors in the IPO, as set by the underwriters before trading begins. See [Investopedia: IPO](https://www.investopedia.com/terms/i/ipo.asp).
- **Closing price**: The final price at which the stock trades during regular trading hours (ending 4:00 PM ET / 20:00 UTC) on the first day of trading. See [Investopedia: Closing Price](https://www.investopedia.com/terms/c/closingprice.asp).

**Resolution source:** The IPO offer price and first-day closing price will be verified using the Nasdaq ticker page at https://www.nasdaq.com/market-activity/stocks/cbrs or, if that URL is not yet active, via credible financial data sources such as Bloomberg (https://www.bloomberg.com), Reuters (https://www.reuters.com), or Yahoo Finance (https://finance.yahoo.com/quote/CBRS/).

**If the IPO does not occur by June 1, 2026 (23:59 UTC):** The question resolves **No**.

**Exact later resolution packet (the object under audit)**

The question resolves YES. Both conditions were met:

1. IPO occurred before deadline: Cerebras Systems completed its IPO and its Class A common stock began trading on the Nasdaq under ticker CBRS on Thursday, May 14, 2026, which is on or before the June 1, 2026 23:59 UTC deadline [f3018b].

2. Closing price strictly above offer price: The IPO offer price was $185.00 per share (priced May 13, 2026, above its expected range), and the closing price on the first day of trading (May 14, 2026) was $311.07 per share — a 68% first-day gain. Since $311.07 > $185.00, the condition is satisfied [f3018b].

Supporting excerpts from CNBC: "Cerebras shares opened at $350, up from its $185 IPO price, and closed up 68% at $311.07" and "Cerebras Systems soared 68% in its Nasdaq debut on Thursday, closing at $311.07 after selling shares at $185, well above the company's expected range" [f3018b].

This is corroborated by multiple other credible sources including Reuters, WSJ, Fortune, IPOScoop (which reported the $185 IPO price and 68.15% first-day gain), and Hiive (which listed "Cerebras Systems IPO Price: $185.00/sh. Day 1 closing price: $311.07/sh").

Source URL: https://www.cnbc.com/2026/05/14/cerebras-cbrs-stock-trade-nasdaq-ipo.html

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-22. `96632c8c-1bdd-5deb-9f65-deab719ac39b`

- Present date: `2026-05-16 15:44:02.769519` (information window ends end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`
- Recorded realized outcome: **YES**

**Question**

Will any NATO member state shoot down a drone over Baltic state territory (Estonia, Latvia, or Lithuania) between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, between 00:00 UTC on May 12, 2026 and 23:59 UTC on June 30, 2026, any NATO member state's military forces kinetically destroy or force down an unmanned aerial vehicle (UAV) over the territory of Estonia, Latvia, or Lithuania.

**Key definitions:**

- **"Shoot down"**: The kinetic interception and destruction of the drone, or the use of directed energy or other weapons resulting in the physical destruction or forced crash of the drone. This does NOT include electronic warfare measures (e.g., GPS jamming or spoofing) that merely redirect or land a drone without physical destruction, unless such measures result in a crash that is officially characterized as a shoot-down by the relevant authorities.

- **"Drone" or "UAV"**: An unmanned aerial vehicle, as defined by NATO Allied Joint Publication AJP-3.3 and the NATO Standardization Agreement (STANAG), i.e., a powered aerial vehicle that does not carry a human operator, uses aerodynamic forces to provide vehicle lift, can fly autonomously or be piloted remotely, can be expendable or recoverable, and can carry a lethal or nonlethal payload. Reference: https://www.nato.int/cps/en/natolive/topics_48892.htm

- **"Baltic state territory"**: The sovereign land territory and sovereign airspace (up to the boundary of outer space) of Estonia, Latvia, and Lithuania. This includes their territorial waters (12 nautical miles from the baseline per UNCLOS) and the airspace above those waters. It does NOT include exclusive economic zones or international airspace.

- **Time window**: The event must occur on or after May 12, 2026, at 00:00 UTC and before July 1, 2026, at 00:00 UTC. This excludes all prior incidents, including the May 7, 2026 Latvia drone crashes.

**Resolution sources**: Official press releases or statements from:
- The Estonian Ministry of Defence (https://kaitseministeerium.ee/en)
- The Latvian Ministry of Defence (https://www.mod.gov.lv/en)
- The Lithuanian Ministry of National Defence (https://kam.lt/en/)
- NATO official communications (https://www.nato.int)

Alternatively, credible reporting from Reuters, AP, BBC, or similar major international news agencies confirming the event based on official statements.

If no such event is confirmed by these sources by July 1, 2026, the question resolves as **No**.

**Exact later resolution packet (the object under audit)**

The question resolves **YES**. Between 00:00 UTC May 12, 2026 and 23:59 UTC June 30, 2026, at least two qualifying events occurred in which NATO member state military forces kinetically shot down drones over Baltic state territory:

**Event 1 — May 19, 2026 (Estonia):** A Romanian Air Force F-16 fighter jet operating under NATO's Baltic Air Policing mission shot down a suspected Ukrainian drone that had entered Estonian airspace from Russia. The drone was destroyed with a single missile and crashed in a field near Kablaküla, Põltsamaa Municipality (inland sovereign Estonian territory). The Estonian military and NATO officially confirmed the shoot-down, with the Estonian military stating the drone was shot down to "minimise the impact on the civilian population and infrastructure." The incident occurred at 12:14 p.m. local time (09:14 GMT) [Ukrainian drone shot down by NATO jet over Estonia - Reuters](https://www.reuters.com/business/aerospace-defense/nato-jet-shoots-down-drone-estonia-news-website-delfi-reports-2026-05-19/) [2026 Ukrainian drone incursions into the Baltic states and Finland](https://en.wikipedia.org/wiki/2026_Ukrainian_drone_incursions_into_the_Baltic_states_and_Finland). Reuters: https://www.reuters.com/business/aerospace-defense/nato-jet-shoots-down-drone-estonia-news-website-delfi-reports-2026-05-19/ ; ERR: https://news.err.ee/1610027866/intruding-drone-shot-down-by-romanian-fighter-jet-in-estonia

**Event 2 — June 8, 2026 (Latvia):** A French Air Force Dassault Rafale fighter jet, part of the NATO Baltic Air Policing mission, shot down a drone that had entered Latvian airspace from Russia, over the eastern village of Bērzgale/Berzgale (inland sovereign Latvian territory). The Latvian Ministry of Defence, the Latvian Prime Minister, and Defence Minister Raivis Melnis confirmed the event; the final decision to shoot down was taken by NATO command. The drone was physically destroyed [French jet on NATO mission shoots down drone in Latvian airspace](https://www.reuters.com/business/aerospace-defense/latvias-military-issues-alert-over-drone-incursion-2026-06-08/) [2026 Ukrainian drone incursions into the Baltic states and Finland](https://en.wikipedia.org/wiki/2026_Ukrainian_drone_incursions_into_the_Baltic_states_and_Finland). Reuters: https://www.reuters.com/business/aerospace-defense/latvias-military-issues-alert-over-drone-incursion-2026-06-08/

**Criteria check:**
- Time window: Both events (May 19 and June 8, 2026) fall strictly within May 12, 2026 00:00 UTC – July 1, 2026 00:00 UTC, and both post-date the excluded May 7, 2026 Latvia crash [Ukrainian drone shot down by NATO jet over Estonia - Reuters](https://www.reuters.com/business/aerospace-defense/nato-jet-shoots-down-drone-estonia-news-website-delfi-reports-2026-05-19/) [French jet on NATO mission shoots down drone in Latvian airspace](https://www.reuters.com/business/aerospace-defense/latvias-military-issues-alert-over-drone-incursion-2026-06-08/).
- Location: Both drones were shot down over inland sovereign land territory/airspace of a Baltic state (Estonia — Kablaküla/Põltsamaa; Latvia — Bērzgale), not over EEZ or international airspace [2026 Ukrainian drone incursions into the Baltic states and Finland](https://en.wikipedia.org/wiki/2026_Ukrainian_drone_incursions_into_the_Baltic_states_and_Finland).
- Kinetic destruction: Both were kinetic shoot-downs by fighter aircraft (missile in the Estonia case), not electronic-warfare measures, and were officially characterized as shoot-downs by the relevant national militaries and NATO [Ukrainian drone shot down by NATO jet over Estonia - Reuters](https://www.reuters.com/business/aerospace-defense/nato-jet-shoots-down-drone-estonia-news-website-delfi-reports-2026-05-19/) [French jet on NATO mission shoots down drone in Latvian airspace](https://www.reuters.com/business/aerospace-defense/latvias-military-issues-alert-over-drone-incursion-2026-06-08/) [2026 Ukrainian drone incursions into the Baltic states and Finland](https://en.wikipedia.org/wiki/2026_Ukrainian_drone_incursions_into_the_Baltic_states_and_Finland).
- Actor: NATO member state military forces (Romanian Air Force; French Air Force), operating under NATO's Baltic Air Policing mission [Ukrainian drone shot down by NATO jet over Estonia - Reuters](https://www.reuters.com/business/aerospace-defense/nato-jet-shoots-down-drone-estonia-news-website-delfi-reports-2026-05-19/) [French jet on NATO mission shoots down drone in Latvian airspace](https://www.reuters.com/business/aerospace-defense/latvias-military-issues-alert-over-drone-incursion-2026-06-08/) [2026 Ukrainian drone incursions into the Baltic states and Finland](https://en.wikipedia.org/wiki/2026_Ukrainian_drone_incursions_into_the_Baltic_states_and_Finland).
- Sources: Confirmed by Reuters (a mandated major news agency) citing official Estonian/Latvian military and NATO statements [Ukrainian drone shot down by NATO jet over Estonia - Reuters](https://www.reuters.com/business/aerospace-defense/nato-jet-shoots-down-drone-estonia-news-website-delfi-reports-2026-05-19/) [French jet on NATO mission shoots down drone in Latvian airspace](https://www.reuters.com/business/aerospace-defense/latvias-military-issues-alert-over-drone-incursion-2026-06-08/).

The earliest qualifying event alone (May 19 Estonia shoot-down) is sufficient to resolve the question YES; the June 8 Latvia shoot-down provides additional confirmation.

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-23. `3f5d8fa9-7140-5215-b8b9-b71c501c738d`

- Present date: `2026-05-13 21:45:28.311211` (information window ends end of UTC day `2026-05-13`)
- Expected resolution: `2026-05-28 00:00:00`
- Recorded realized outcome: **YES**

**Question**

Will the SARB revise its 2026 headline inflation forecast upward in the May 28, 2026 MPC statement compared to the March 2026 statement?

**Resolution criteria**

This question resolves YES if the 2026 annual average headline inflation forecast stated in the SARB MPC statement released on May 28, 2026 (SAST, UTC+2) is strictly greater than 3.7% (the figure from the March 26, 2026 statement [[PDF] Repo rate held at 6.75%. No rate cuts expected in 2026 - Momentum](https://sls-fresco.momentum.co.za/files/documents/corporate/mim/updates-and-news/sarb-interest-rate-decision-26-march-2026.pdf)).

This question resolves NO if the 2026 annual average headline inflation forecast in the May 28, 2026 statement is equal to or less than 3.7%.

If the May 28, 2026 MPC statement does not provide a comparable 2026 annual average headline inflation forecast number, or if the statement is not published by July 1, 2026 (SAST), the question resolves N/A.

The resolution source is the official SARB Monetary Policy Committee statement published at: https://www.resbank.co.za/en/home/publications/publication-detail-pages/statements/monetary-policy-statements

For clarity: "headline inflation" refers to the overall Consumer Price Index (CPI) inflation rate as published by Statistics South Africa (https://www.statssa.gov.za/?page_id=735&id=1), encompassing all goods and services including food and energy.

**Exact later resolution packet (the object under audit)**

The official SARB Monetary Policy Committee statement used for resolution is the May 2026 statement at https://www.resbank.co.za/en/home/publications/publication-detail-pages/statements/monetary-policy-statements/2026/may, published/released on 2026-05-28 [Statement of the Monetary Policy Committee May 2026](https://www.resbank.co.za/en/home/publications/publication-detail-pages/statements/monetary-policy-statements/2026/may). In that statement, SARB states: “Our forecast now has headline inflation averaging 4.4% this year and 3.7% next year” [Statement of the Monetary Policy Committee May 2026](https://www.resbank.co.za/en/home/publications/publication-detail-pages/statements/monetary-policy-statements/2026/may). Because the statement is dated May 28, 2026, “this year” refers to the 2026 annual average headline inflation forecast; the relevant value is therefore 4.4% [Statement of the Monetary Policy Committee May 2026](https://www.resbank.co.za/en/home/publications/publication-detail-pages/statements/monetary-policy-statements/2026/may). The resolution criterion asks whether this 2026 annual average headline inflation forecast is strictly greater than 3.7%. Since 4.4% > 3.7%, the question resolves YES.

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-24. `72178d56-46a3-5048-a419-1a9d38fdba05`

- Present date: `2026-05-02 21:04:40.753974` (information window ends end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`
- Recorded realized outcome: **YES**

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

**Exact later resolution packet (the object under audit)**

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

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-25. `614badaa-58d1-51b1-a5a1-9faa933aa46d`

- Present date: `2026-05-12 17:59:49.260395` (information window ends end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`
- Recorded realized outcome: **YES**

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

**Exact later resolution packet (the object under audit)**

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

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-26. `b5a5f3eb-c6ff-53b8-af90-165b7a6edd91`

- Present date: `2026-04-30 17:30:41.033085` (information window ends end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`
- Recorded realized outcome: **YES**

**Question**

Will Nintendo officially announce a previously unrevealed first-party Nintendo Switch 2 game between April 30 and June 1, 2026?

**Resolution criteria**

This question resolves YES if, between April 30, 2026 00:00 UTC and June 1, 2026 00:00 UTC, Nintendo officially announces at least one new first-party game for the Nintendo Switch 2 (or whatever the official name of Nintendo's Switch successor is) that was not previously publicly revealed as of April 30, 2026 00:00 UTC.

**Definitions:**

- **"First-party game"**: A game where Nintendo is the publisher AND the intellectual property is owned by Nintendo. This includes games developed by internal studios (e.g., Nintendo EPD, Nintendo SPD) or Nintendo subsidiaries (e.g., Monolith Soft, Retro Studios, Next Level Games, Intelligent Systems, HAL Laboratory when publishing under Nintendo). Third-party games merely appearing on the platform do not count.

- **"New game"**: A game that has not been previously publicly announced or revealed in any form. Remasters, remakes, and reimaginings of existing games DO count as new games if they have not been previously announced. DLC or expansions for already-released or already-announced games do NOT count.

- **"Official announcement"**: A reveal via any of the following channels: (a) a Nintendo Direct presentation, (b) a post on Nintendo's verified social media accounts (e.g., @NintendoAmerica, @Nintendo on X/Twitter, or Nintendo's official YouTube channel at https://www.youtube.com/@Nintendo), (c) a press release or news post on Nintendo's official website (https://www.nintendo.com), or (d) a trailer or announcement published by Nintendo at an industry event. Leaks, rumors, and reports from unofficial sources do not count.

- **"Nintendo Switch 2"** refers to the hybrid video game console released by Nintendo on June 5, 2025, regardless of branding changes or alternative regional names.

**Resolution source:** Nintendo's official YouTube channel (https://www.youtube.com/@Nintendo), Nintendo's official newsroom/website (https://www.nintendo.com/us/whatsnew/), or credible gaming news outlets such as IGN (https://www.ign.com), Nintendo Life (https://www.nintendolife.com), or Eurogamer (https://www.eurogamer.net) reporting on an official Nintendo announcement.

If no such announcement occurs before June 1, 2026 00:00 UTC, the question resolves NO.

**Exact later resolution packet (the object under audit)**

The question resolves YES.

On May 6, 2026 — within the resolution window of April 30, 2026 00:00 UTC to June 1, 2026 00:00 UTC — Nintendo held a surprise "Star Fox Direct" (5.6.2026) and officially announced a brand-new first-party game titled "Star Fox" for the Nintendo Switch 2, set to release June 25, 2026 [8d810d][0a42af].

Each resolution criterion is satisfied:
- Timing: The Star Fox Direct aired May 6, 2026, squarely inside the April 30–June 1, 2026 window [0a42af].
- First-party: Star Fox is a Nintendo-owned IP, published by Nintendo; the game was revealed by Nintendo itself, satisfying the "Nintendo publishes AND owns the IP" definition [8d810d][0a42af].
- New game / not previously revealed: The title was the headline reveal of the Direct and had not been officially announced before April 30, 2026. Although leaks and rumors circulated in April 2026, the resolution criteria explicitly exclude leaks/rumors and count only official announcements; the official reveal came at the May 6 Direct [0a42af]. It is also not among the games listed as already revealed as of April 30 (Yoshi and the Mysterious Book, Splatoon Raiders, Rhythm Heaven Groove, Fire Emblem: Fortune's Weave). Even though the game is described as a cinematic reimagining of Star Fox 64, the criteria explicitly state that remakes/reimaginings count as new games if not previously announced [0a42af].
- Standalone new game, not DLC: It is a full standalone title with its own release date (June 25, 2026), priced as a full game [0a42af].
- Official channel: It was announced via an official Nintendo Direct presentation, one of the explicitly accepted channels. Nintendo's official site hosts the Star Fox Direct 5.6.2026 page (nintendo.com/en-ca/nintendo-direct/5-6-2026/) and Nintendo's official YouTube channel posted the "Star Fox Direct 5.6.2026" presentation [0a42af].

Direct reporting from credible outlets cited the official announcement: 9to5Toys (https://9to5toys.com/2026/05/06/surprise-starfox-nintendo-direct-showcase-starts-now/) [0a42af] and GameLuster (https://gameluster.com/nintendo-direct-may-2026-every-major-announcement/) [8d810d], plus Kotaku's coverage of the Star Fox Direct. The official Nintendo YouTube video "Star Fox Direct 5.6.2026" is at https://www.youtube.com/watch?v=ePZeyh5q9R8.

Therefore at least one previously-unrevealed first-party Switch 2 game (Star Fox) was officially announced in the window, resolving the question YES.

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-27. `d41b3f25-a551-57fd-a6f6-4a0c91bd91f7`

- Present date: `2026-05-29 03:50:50.147499` (information window ends end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`
- Recorded realized outcome: **YES**

**Question**

Will President Trump sign the $72B immigration enforcement reconciliation bill into law by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the immigration enforcement reconciliation bill originating from the process initiated by [S. Con. Res. 33](https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/33) is enacted into law on or after May 12, 2026, and on or before July 1, 2026 (11:59 PM ET).

Enactment means the bill has been signed by the President, OR has become law without the President's signature under the [Presentment Clause](https://en.wikipedia.org/wiki/Presentment_Clause) (i.e., the President neither signs nor vetoes the bill within 10 days while Congress is in session), OR Congress overrides a presidential veto by a two-thirds vote in both chambers.

The bill will be identifiable as the reconciliation measure reported pursuant to S. Con. Res. 33, primarily funding ICE and CBP. Once enacted, it will be assigned a Public Law number.

Resolution will be verified via the official [Congress.gov](https://www.congress.gov/) record of enrolled bills and public laws, or via the [Federal Register](https://www.federalregister.gov/). If no such law is enacted by 11:59 PM ET on July 1, 2026, this question resolves **No**.

**Exact later resolution packet (the object under audit)**

RESOLUTION: YES (1)

The immigration enforcement reconciliation bill originating from S. Con. Res. 33 was enacted into law on June 10, 2026 — squarely within the resolution window of May 12, 2026 to July 1, 2026 (11:59 PM ET).

**Identity of the bill.** The measure is S. 2, the "Secure America Act." Its official Congress.gov title is "An original bill to provide for reconciliation pursuant to title II of S. Con. Res. 33," directly matching the resolution criteria's requirement that the bill be "the reconciliation measure reported pursuant to S. Con. Res. 33, primarily funding ICE and CBP" [Info - S.2 - 119th Congress (2025-2026): Secure America Act](https://www.congress.gov/bill/119th-congress/senate-bill/2/all-info). It provides roughly $70 billion in funding to DHS, CBP, and ICE through Fiscal Year 2029 (originally scored/introduced at ~$72B) [S. 2 Signed into Law - The White House](https://www.whitehouse.gov/briefings-statements/2026/06/s-2-signed-into-law/).

**Legislative path (from Congress.gov official record) [Info - S.2 - 119th Congress (2025-2026): Secure America Act](https://www.congress.gov/bill/119th-congress/senate-bill/2/all-info):**
- 05/20/2026: Committee on the Budget — original measure reported to the Senate by Senator Graham.
- 06/05/2026: Passed the Senate with an amendment (52–47 per Senate roll call [Roll Call Vote 119 th Congress - 2 nd Session - Senate.gov](https://www.senate.gov/legislative/LIS/roll_call_votes/vote1192/vote_119_2_00163.htm)).
- 06/09/2026: Passed/agreed to in the House.
- 06/10/2026: Signed by the President; became Public Law No. 119-98.

**Enactment verification.**
- The official White House statement confirms: "On Wednesday, June 10, 2026, the President signed into law: S. 2, the 'Secure America Act,'... which provides funding to the Department of Homeland Security, U.S. Customs and Border Protection, and U.S. Immigration and Customs Enforcement through Fiscal Year 2029 for immigration enforcement and related activities" [S. 2 Signed into Law - The White House](https://www.whitehouse.gov/briefings-statements/2026/06/s-2-signed-into-law/).
- The official Congress.gov record shows S. 2 was signed by the President on June 10, 2026 and became Public Law No. 119-98 [Info - S.2 - 119th Congress (2025-2026): Secure America Act](https://www.congress.gov/bill/119th-congress/senate-bill/2/all-info).
- The Congress.gov Public Laws list for the 119th Congress lists "S.2 - Secure America Act" with enactment date 06/10/2026 and Public Law number PL 119-98 [Statutes at Large and Public Laws](https://www.congress.gov/public-laws/119th-congress).

**Checklist confirmation:**
1. Enacted bill is the reconciliation measure reported pursuant to S. Con. Res. 33 — confirmed by the bill's official title [Info - S.2 - 119th Congress (2025-2026): Secure America Act](https://www.congress.gov/bill/119th-congress/senate-bill/2/all-info).
2. Enactment date (June 10, 2026) falls strictly between May 12, 2026 and July 1, 2026 — confirmed [Info - S.2 - 119th Congress (2025-2026): Secure America Act](https://www.congress.gov/bill/119th-congress/senate-bill/2/all-info) [Statutes at Large and Public Laws](https://www.congress.gov/public-laws/119th-congress) [S. 2 Signed into Law - The White House](https://www.whitehouse.gov/briefings-statements/2026/06/s-2-signed-into-law/).
3. Verified using the official Congress.gov record — done [Info - S.2 - 119th Congress (2025-2026): Secure America Act](https://www.congress.gov/bill/119th-congress/senate-bill/2/all-info) [Statutes at Large and Public Laws](https://www.congress.gov/public-laws/119th-congress).
4. Direct URLs: bill status/all-info — https://www.congress.gov/bill/119th-congress/senate-bill/2/all-info ; public laws list — https://www.congress.gov/public-laws/119th-congress ; White House signing statement — https://www.whitehouse.gov/briefings-statements/2026/06/s-2-signed-into-law/
5. Public Law number assigned: Public Law No. 119-98 [Info - S.2 - 119th Congress (2025-2026): Secure America Act](https://www.congress.gov/bill/119th-congress/senate-bill/2/all-info) [Statutes at Large and Public Laws](https://www.congress.gov/public-laws/119th-congress).

All criteria for a YES resolution are met: the S. Con. Res. 33 reconciliation bill funding ICE/CBP was signed by the President and assigned a Public Law number within the specified window.

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-28. `a1ec0332-9728-5b5b-9120-43f5f7c13a43`

- Present date: `2026-05-01 17:32:01.956816` (information window ends end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`
- Recorded realized outcome: **YES**

**Question**

Will the U.S. Department of Education publish a final rule implementing the Workforce Pell Grant program in the Federal Register by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if a document categorized as a "Rule" or "Final Rule" (not a "Proposed Rule" or "Notice") implementing the [Workforce Pell Grant program](https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant) is published in the Federal Register on or after April 30, 2026, and no later than June 1, 2026, 11:59 PM Eastern Time.

The "Workforce Pell Grant program" refers to the program established under Section 401A of the Higher Education Act of 1965, as added by Section 30201 of the One Big Beautiful Bill Act (H.R. 1), which extends Pell Grant eligibility to eligible short-term workforce training programs [https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant](https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant).

A "final rule" means a document published in the Federal Register under the "Rules and Regulations" section, with document type classified as "Rule" — as distinct from a "Proposed Rule" (which the NPRM already is) or a "Notice."

The resolution source is the [Federal Register](https://www.federalregister.gov/) and specifically the [Department of Education's documents page](https://www.federalregister.gov/agencies/education-department). The question resolves **No** if no such final rule appears by the deadline.

This resolution criterion excludes the already-published NPRM (March 9, 2026), which is a proposed rule, not a final rule.

**Exact later resolution packet (the object under audit)**

The question resolves YES. The U.S. Department of Education published a final rule implementing the Workforce Pell Grant program in the Federal Register on May 19, 2026, which falls within the resolution window (on or after April 30, 2026 and no later than June 1, 2026, 11:59 PM ET).

The document is at https://www.federalregister.gov/documents/2026/05/19/2026-10013/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant and is titled "Accountability in Higher Education and Access Through Demand-Driven Workforce Pell: Pell Grant Exclusion Relating to Other Grant Aid; and Workforce Pell Grants."

Key verification points [108186]:
- Document type: The Federal Register classifies this document explicitly as a "Rule" (i.e., a Final Rule in the Rules and Regulations section), NOT a "Proposed Rule" or "Notice."
- Publication date: 05/19/2026, which is within the required window of April 30, 2026 to June 1, 2026.
- Subject matter: It implements the Workforce Pell Grant program established by H.R. 1 (the One Big Beautiful Bill Act / referred to in the rule as the Working Families Tax Cuts Act), signed into law July 4, 2025. The rule amends § 600.10 to require Secretary approval of eligible workforce programs and implements the Workforce Pell Grant provisions, matching the program defined under Section 401A of the HEA.

This is distinct from and supersedes the NPRM (a Proposed Rule) published March 9, 2026 (document 2026-04520), which the resolution criteria explicitly excluded. The May 19, 2026 document is the FINAL rule, sharing the same title but being a separate, later-published "Rule"-type document.

Note: An initial exhaustive scan of the Department of Education's agency listing page failed to surface this final rule and incorrectly suggested NO, but a direct query of the actual Federal Register document confirmed its existence, document type ("Rule"), and publication date (05/19/2026) [108186]. Multiple secondary sources (ed.gov press release titled "U.S. Department of Education Issues Final Rule to Create New Workforce Pell Grant Program," and fsapartners.ed.gov "Final" designation dated 2026-05-19) corroborate that this is the final rule.

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-29. `a653ccb0-0617-5d42-b6c1-5d05e8b8fbb9`

- Present date: `2026-05-16 19:25:38.361614` (information window ends end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`
- Recorded realized outcome: **YES**

**Question**

Will the U.S. Supreme Court rule in favor of the FCC (reversing the Fifth Circuit) in FCC v. AT&T, Inc. (No. 25-406) by June 30, 2026?

**Resolution criteria**

This question resolves **Yes** if, between May 12, 2026 and July 1, 2026 (11:59 PM Eastern Time), the U.S. Supreme Court issues an opinion in FCC v. AT&T, Inc. (No. 25-406) that **reverses** the Fifth Circuit's judgment—i.e., the Court holds that the FCC's forfeiture order process does not violate the Seventh Amendment or Article III, thereby upholding the FCC's authority to issue such orders. A "vacated and remanded" disposition also counts as **Yes** if the Court's opinion rejects the Fifth Circuit's core holding that the FCC's process violates the Seventh Amendment, even if the case is remanded on other grounds. A partial reversal that rejects the Seventh Amendment holding counts as Yes.

This question resolves **No** if:
- The Court affirms the Fifth Circuit's decision (upholding the carriers' Seventh Amendment claim), OR
- The Court dismisses the case as improvidently granted (DIG), which would leave the Fifth Circuit's judgment intact, OR
- No opinion is issued by July 1, 2026 at 11:59 PM Eastern Time.

**Primary resolution source:** The official Supreme Court docket page (https://www.supremecourt.gov/docket/docketfiles/html/public/25-406.html) and the Opinions of the Court page (https://www.supremecourt.gov/opinions/slipopinion/25). The disposition language in the Court's syllabus and opinion will determine resolution.

**Exact later resolution packet (the object under audit)**

The question resolves YES.

Resolution window: May 12, 2026 – July 1, 2026 (11:59 PM ET). The Supreme Court issued its opinion on June 4, 2026, squarely within this window.

Disposition: The official Supreme Court docket for No. 25-406 records the June 4, 2026 entry: "Judgment REVERSED and case REMANDED. No. 25-567, adjudged to be affirmed. Roberts, C. J., delivered the opinion of the Court, in which Alito, Sotomayor, Kagan, Gorsuch, Kavanaugh, Barrett, and Jackson, JJ., joined. Thomas, J., filed a dissenting opinion." [Docket for 25-406 - Supreme Court](https://www.supremecourt.gov/docket/docketfiles/html/public/25-406.html) (https://www.supremecourt.gov/docket/docketfiles/html/public/25-406.html)

This is a REVERSAL of the Fifth Circuit's judgment in FCC v. AT&T (No. 25-406), which is exactly the condition the resolution criteria specify for YES ("reverses the Fifth Circuit's judgment—i.e., the Court holds that the FCC's forfeiture order process does not violate the Seventh Amendment or Article III").

Merits: The 8-1 majority (Chief Justice Roberts) held that it does not violate the Seventh Amendment for the FCC to issue forfeiture orders without a jury, because forfeiture orders under §503(b) do not definitively resolve the parties' legal obligations until DOJ brings a court enforcement action. This is confirmed by the slip opinion (https://www.supremecourt.gov/opinions/25pdf/25-406_nmip.pdf) and corroborated by SCOTUSblog ("Reversed and remanded, 8-1, in an opinion by John Roberts on Jun 4, 2026. Justice Thomas wrote a dissenting opinion."), the Congressional Research Service, the FCC's own release, and numerous law firm summaries (Mayer Brown, Faegre Drinker, Morgan Lewis, etc.), all dated June 4, 2026.

None of the NO conditions apply: the Court did not affirm the Fifth Circuit, did not dismiss as improvidently granted (DIG), and an opinion was issued before the July 1, 2026 deadline. The companion case No. 25-567 (Verizon) was "adjudged to be affirmed," but that concerns Verizon's petition; the core FCC v. AT&T judgment reversing the Fifth Circuit and rejecting the Seventh Amendment holding is what governs this question, and it resolves YES.

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-30. `81d4c81e-bbd1-5da2-bd1a-d4f7677ea272`

- Present date: `2026-05-02 22:27:59.848494` (information window ends end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`
- Recorded realized outcome: **YES**

**Question**

Will SpaceX file a public S-1 registration statement on SEC EDGAR between April 30 and June 1, 2026?

**Resolution criteria**

This question resolves YES if a public S-1 registration statement filed by Space Exploration Technologies Corp. (commonly known as SpaceX) appears on the SEC's EDGAR system on or after April 30, 2026, 12:00 AM Eastern Time, and before June 1, 2026, 11:59 PM Eastern Time.

The primary resolution source is the SEC EDGAR full-text search system. To verify, search for SpaceX filings at: https://efts.sec.gov/LATEST/search-index?q=%22Space+Exploration+Technologies%22&forms=S-1

A "public S-1 registration statement" is defined as a Form S-1 filing (as classified by the SEC) that is publicly visible on the EDGAR system. This specifically excludes:
- Confidential draft registration statements (such as the one submitted on April 1, 2026), which are not publicly visible on EDGAR until converted to a public filing.
- Amendments to the S-1 (Form S-1/A), unless the original S-1 also appears within the specified date window.
- Any other SEC form types (e.g., Form D, Form 10-K, etc.).

The filing date as recorded on EDGAR (in Eastern Time) is the operative date. If no public S-1 from SpaceX appears on EDGAR within the specified window, the question resolves NO.

**Exact later resolution packet (the object under audit)**

The question resolves YES.

Resolution criteria require a public Form S-1 registration statement filed by Space Exploration Technologies Corp. (SpaceX) to appear on SEC EDGAR on or after April 30, 2026 12:00 AM ET and before June 1, 2026 11:59 PM ET.

Evidence: SEC EDGAR shows that Space Exploration Technologies Corp. (CIK 0001181412) filed a Form S-1 on May 20, 2026, under SEC Accession Number 0001628280-26-036936, File No. 333-296070, accepted 2026-05-20 16:40:21 ET. The EDGAR filing index explicitly lists "Filing Date: 2026-05-20" and "Type: S-1 | Act: 33." (Source: https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm). The SEC full-text S-1 search results for "Space Exploration Technologies" likewise list this S-1 dated 2026-05-20 [https://efts.sec.gov/LATEST/search-index?q=%22Space+Exploration+Technologies%22&forms=S-1](https://efts.sec.gov/LATEST/search-index?q=%22Space+Exploration+Technologies%22&forms=S-1) [https://efts.sec.gov/LATEST/search-index?q=%22Space Exploration Technologies%22&forms=S-1](https://efts.sec.gov/LATEST/search-index?q=%22Space Exploration Technologies%22&forms=S-1).

The actual registration statement document confirms it is a "FORM S-1 REGISTRATION STATEMENT UNDER THE SECURITIES ACT OF 1933" for Space Exploration Technologies Corp. (https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/spaceexplorationtechnologi.htm).

This is a genuine Form S-1 (not S-1/A), filed by the correctly named entity "Space Exploration Technologies Corp.", and its filing date of May 20, 2026 falls strictly within the resolution window (April 30 – June 1, 2026). This is distinct from the confidential draft registration statement reportedly submitted April 1, 2026, which would not have been publicly visible on EDGAR; the May 20 filing is the public S-1 that satisfies the criteria.

A subsequent Form S-1/A amendment was filed June 1, 2026 (Accession 0001628280-26-039276) [https://efts.sec.gov/LATEST/search-index?q=%22Space+Exploration+Technologies%22&forms=S-1](https://efts.sec.gov/LATEST/search-index?q=%22Space+Exploration+Technologies%22&forms=S-1), but the original public S-1 already appeared within the window, so the YES condition is met regardless.

Therefore the question resolves YES (1).

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-31. `bd90f010-d501-5c54-a6a0-f4ed25ba1757`

- Present date: `2026-05-14 01:24:17.608235` (information window ends end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-19T00:00:00`
- Recorded realized outcome: **YES**

**Question**

Will the European Commission announce a new Growth Plan disbursement for at least one Western Balkan country between June 5 and June 19, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 12, 2026, and no later than 23:59 UTC on June 19, 2026, the European Commission publishes an official announcement (press release, Implementing Decision, or statement) confirming that a new disbursement of funds under the Reform and Growth Facility for the Western Balkans has been authorized for at least one of the following countries: Albania, Bosnia and Herzegovina, Kosovo, Montenegro, North Macedonia, or Serbia.

The "Growth Plan" refers to the Reform and Growth Facility for the Western Balkans, as described at: https://enlargement.ec.europa.eu/funding-technical-assistance/reform-and-growth-facility-western-balkans_en

An "announcement of a disbursement" means an official press release or publication of a Commission Implementing Decision on the European Commission's website stating that a payment (whether grant or loan) has been authorized or approved for release to one or more of the listed countries. Pre-financing payments do not count; only milestone-based releases qualify.

"Western Balkan country" means one of: Albania, Bosnia and Herzegovina, Kosovo, Montenegro, North Macedonia, or Serbia.

The primary resolution source is the European Commission Press Corner (https://ec.europa.eu/commission/presscorner/home/en) and the Reform and Growth Facility page (https://enlargement.ec.europa.eu/funding-technical-assistance/reform-and-growth-facility-western-balkans_en).

If no such announcement is published by 23:59 UTC on June 19, 2026, the question resolves as **No**.

**Exact later resolution packet (the object under audit)**

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

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-32. `555d2be7-6581-5345-9052-655b8c898df0`

- Present date: `2026-05-14 10:00:12.053424` (information window ends end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`
- Recorded realized outcome: **YES**

**Question**

Will the Supreme Court's opinion in Mullin v. Doe feature at least one dissenting opinion?

**Resolution criteria**

This question resolves as **Yes** if the Supreme Court of the United States issues its opinion in Mullin v. Doe (Docket No. 25-1083, consolidated with Trump v. Miot, No. 25-1084) on or after May 12, 2026, and by July 1, 2026 (11:59 PM Eastern Time), and that opinion includes at least one dissenting opinion.

A **dissenting opinion** is defined as a separate opinion filed by one or more Justices who disagree with the judgment (i.e., the outcome or disposition) reached by the majority or plurality of the Court. An opinion that concurs in the judgment but disagrees with the reasoning (a "concurrence in the judgment") does NOT count as a dissent. Only opinions explicitly labeled as "dissenting" or "dissent" in the official slip opinion qualify.

This question resolves as **No** if:
- The opinion is issued within the specified window and is unanimous (no Justice files a dissenting opinion), OR
- No opinion is released by the Supreme Court in this case by July 1, 2026 (11:59 PM Eastern Time).

**Resolution source:** The official slip opinion as published on the Supreme Court of the United States website at https://www.supremecourt.gov/opinions/slipopinion/25 (the opinions page for the October 2025 Term).

**Exact later resolution packet (the object under audit)**

The Supreme Court issued its opinion in Mullin v. Doe (Docket No. 25-1083, consolidated with Trump v. Miot, No. 25-1084) on June 25, 2026 — squarely within the resolution window of May 12, 2026 through July 1, 2026 (11:59 PM ET).

The case was decided 6-3. Justice Alito announced the judgment of the Court and delivered the opinion of the Court (reversed and remanded), holding that Section 1254a(b)(5)(A) bars judicial review of non-constitutional TPS termination claims [201590].

Crucially, the official slip opinion at https://www.supremecourt.gov/opinions/25pdf/25-1083_f204.pdf includes a dissenting opinion. The syllabus explicitly states: "KAGAN, J., filed a dissenting opinion, in which SOTOMAYOR and JACKSON, JJ., joined." [ce9e12]. SCOTUSblog's case page corroborates that Justice Kagan filed a dissenting opinion joined by Justices Sotomayor and Jackson in this 6-3 decision [201590].

Because (a) the opinion was issued within the required window, and (b) it includes an opinion explicitly labeled "dissenting" — filed by Justices who disagreed with the judgment (a genuine dissent, not merely a concurrence in the judgment) — the question resolves YES.

Resolution source: The official October 2025 Term slip opinions page (https://www.supremecourt.gov/opinions/slipopinion/25), which lists the Mullin v. Doe opinion dated 06/25/2026, and the underlying slip opinion PDF (https://www.supremecourt.gov/opinions/25pdf/25-1083_f204.pdf) [ce9e12].

**Checks (open the cited sources):**
- [ ] realized outcome is correct against the cited/primary evidence
- [ ] cited sources exist and actually support what the packet says they support
- [ ] no cited evidence postdates the question's resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):
