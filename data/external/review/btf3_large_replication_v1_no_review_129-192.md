# btf3_large_replication_v1 — realized NO review chunk NO-129–NO-192

> Display chunk of the immutable queue (`btf3_large_replication_v1_no_queue.json`). Review strictly top-to-bottom; stop only when this bucket reaches 128 ACCEPTs overall. Do not skip ahead, reorder, or prefer better-looking questions. A REJECT/UNSURE permanently consumes its queue slot and is never resampled, re-reviewed, or hand-repaired.

All four gates must hold to ACCEPT. On REJECT or UNSURE write exactly one line of reason.

### NO-129. `1f4fcd81-59ce-5b8f-a614-453f9d871d80`

- Present date: `2026-05-14 05:42:28.440408`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Second Circuit's opinion in United States v. Combs (No. 25-2623), if issued by July 1, 2026, explicitly hold that the use of acquitted conduct in sentencing violates the U.S. Sentencing Guidelines?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026, and before July 1, 2026 (11:59 PM UTC), the U.S. Court of Appeals for the Second Circuit issues a written opinion in *United States v. Combs*, No. 25-2623, that explicitly holds that the district court's use of acquitted conduct in determining the defendant's sentence violated the U.S. Sentencing Guidelines (USSG).

For purposes of this question:
- "[Acquitted conduct](https://www.law.cornell.edu/wex/acquitted_conduct_sentencing)" means conduct for which the defendant was tried and acquitted by a jury but which the sentencing court nonetheless considered as a factor in determining the sentence.
- The "[U.S. Sentencing Guidelines (USSG)](https://www.ussc.gov/guidelines/2024-guidelines-manual)" refers to the federal sentencing guidelines promulgated by the U.S. Sentencing Commission, including amendments thereto.
- "Explicitly holding" means the opinion's holding or disposition states that the sentencing court's reliance on acquitted conduct was contrary to the USSG—whether by citing USSG Amendment 821 (effective November 1, 2024), USSG §1B1.3, USSG §5G1.1, or any other specific USSG provision. A holding that the sentence was erroneous solely on constitutional, statutory (e.g., 18 U.S.C. § 3553(a)), procedural, or plain-error grounds—without finding a USSG violation—does not satisfy this criterion.

This question resolves **No** if:
1. The court issues an opinion that does not explicitly hold that the use of acquitted conduct violated the USSG (e.g., it decides on narrower grounds); OR
2. No opinion is issued by 11:59 PM UTC on July 1, 2026.

**Resolution source:** The opinion text as published on [CourtListener](https://www.courtlistener.com/docket/71724945/united-states-of-america-v-combs/) or the [Second Circuit Court of Appeals opinions page](https://www.ca2.uscourts.gov/decisions).

**Pre-cutoff background**

United States v. Combs (No. 25-2623) is a criminal appeal pending before the U.S. Court of Appeals for the Second Circuit. The case involves Sean Combs, who was convicted of transportation to engage in prostitution under the Mann Act but acquitted on racketeering and sex trafficking charges [United States of America v. Combs, 25-2623 – CourtListener.com](https://www.courtlistener.com/docket/71724945/united-states-of-america-v-combs/). The central legal question on appeal is whether the sentencing court improperly relied on "[acquitted conduct](https://www.law.cornell.edu/wex/acquitted_conduct_sentencing)"—conduct for which the defendant was found not guilty—in determining the sentence, in violation of the [U.S. Sentencing Guidelines (USSG)](https://www.ussc.gov/guidelines/2024-guidelines-manual).

In 2024, the U.S. Sentencing Commission adopted [Amendment 821](https://www.ussc.gov/guidelines/amendment/821), which added USSG §1B1.3 commentary and a new §5G1.1 provision limiting the use of acquitted conduct in sentencing. The Second Circuit has described this case as a "question of first impression" regarding the application of this amendment [United States of America v. Combs, 25-2623 – CourtListener.com](https://www.courtlistener.com/docket/71724945/united-states-of-america-v-combs/).

**Procedural status as of May 12, 2026:** Oral arguments were held on April 9, 2026. No opinion has been issued [United States of America v. Combs, 25-2623 – CourtListener.com](https://www.courtlistener.com/docket/71724945/united-states-of-america-v-combs/). The case is fully briefed and sub judice. Amicus briefs were filed by organizations including the National Association of Criminal Defense Lawyers (NACDL), and by a retired federal judge and law professors.

The court could resolve the case on narrow grounds (e.g., procedural error, abuse of discretion, or plain error review) without reaching the broader question of whether acquitted conduct sentencing violates the USSG. Alternatively, it could issue a landmark holding explicitly addressing whether the amended guidelines prohibit reliance on acquitted conduct at sentencing.

**Exact later resolution packet**

The question resolves NO (0) because no written opinion was issued by the Second Circuit in United States v. Combs, No. 25-2623, by the deadline of 11:59 PM UTC on July 1, 2026.

Key evidence:
- The CourtListener docket for United States of America v. Combs, No. 25-2623 (https://www.courtlistener.com/docket/71724945/united-states-of-america-v-combs/) was last updated June 30, 2026, and shows NO written opinion, decision, judgment, or summary order filed after the oral argument. The most recent substantive docket entry (Entry 74) is dated April 9, 2026 (oral argument before the three-judge panel). No filings exist for May 2026 or June 2026 [405576, 3aea88].
- Oral arguments were held April 9, 2026, and multiple contemporaneous news reports (Reuters, NY1, NBC) noted the panel "did not immediately rule." As of late June 2026, the appeal is described as "still pending" with a decision expected "in the weeks" ahead — i.e., not yet decided.
- No credible news source reported any opinion being issued between May 12, 2026 and July 1, 2026.

The resolution criteria explicitly provide: "This question resolves No if ... No opinion is issued by 11:59 PM UTC on July 1, 2026." Because no opinion issued at all, the antecedent for a YES (an opinion explicitly holding that the use of acquitted conduct violated the USSG) was never triggered. Per the resolution criteria, the absence of any opinion resolves the question NO (0) — NOT annulled. There is therefore no basis for a -1 annulment.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-130. `5ab08383-f013-50d1-934e-d66f41489c8c`

- Present date: `2026-04-29 22:18:30.588303`
- Source cutoff boundary: `2026-04-30` (encodes end of UTC day `2026-04-29`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will a second major news outlet independently corroborate allegations of Kash Patel's excessive drinking or unexplained absences by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after the question's open date and on or before June 1, 2026 (11:59 PM UTC), at least one major news outlet publishes an investigative report that independently corroborates allegations of Kash Patel's excessive drinking or unexplained absences from his duties as FBI Director.

**Definitions:**

- **"Major news outlet"**: Any of the following organizations: The New York Times, The Washington Post, The Wall Street Journal, CNN, Reuters, Associated Press (AP), NBC News, CBS News, ABC News, Politico, or Bloomberg.

- **"Investigative report"**: A published article, longform piece, or equivalent written report (not a brief news hit, opinion column, editorial, or podcast transcript that merely references others' reporting). The piece must be primarily based on the outlet's own reporting — i.e., it must cite the outlet's own sources (whether named or anonymous), documents, or firsthand observations.

- **"Independently corroborates"**: The report must provide original sourcing or new evidence that supports the specific claims of excessive drinking or unexplained absences. This means the outlet must have conducted its own interviews, obtained its own documents, or otherwise gathered independent evidence — not merely summarized, cited, or discussed The Atlantic's original reporting. A report that only references The Atlantic's allegations without adding independent confirmation does NOT qualify.

- **"Excessive drinking"**: Allegations that Patel consumed alcohol to a degree that impaired or could impair his professional duties, including but not limited to: drinking on the job, arriving at work intoxicated, or engaging in heavy drinking that affected his performance or availability.

- **"Unexplained absences"**: Allegations that Patel was absent from his duties as FBI Director without adequate official explanation, including missing scheduled meetings, being unreachable during working hours, or failing to fulfill expected responsibilities.

Only events occurring on or after the question's open date count toward resolution. Reports published before the question's open date do not qualify, even if they otherwise meet the criteria above.

If no qualifying report is published by any listed outlet by June 1, 2026, the question resolves **No**.

**Pre-cutoff background**

On April 17, 2026, The Atlantic published an investigative report by Sarah Fitzpatrick titled "The FBI Director Is MIA," alleging that FBI Director Kash Patel has "alarmed colleagues with episodes of excessive drinking and unexplained absences" [The FBI Director Is MIA - The Atlantic](https://www.theatlantic.com/politics/2026/04/kash-patel-fbi-director-drinking-absences/686839/). The report detailed specific incidents, including an April 10, 2026 episode where Patel panicked after a technical login error and told aides he had been fired by the White House [The FBI Director Is MIA - The Atlantic](https://www.theatlantic.com/politics/2026/04/kash-patel-fbi-director-drinking-absences/686839/).

Patel has denied the allegations and filed a $250 million defamation lawsuit against The Atlantic on April 20, 2026 (https://www.reuters.com/world/fbi-director-kash-patel-sues-atlantic-court-records-show-2026-04-20/). House Judiciary Democrats have launched an investigation and demanded Patel submit to alcohol abuse screening (https://democrats-judiciary.house.gov/media-center/press-releases/judiciary-democrats-launch-investigation-into-reports-of-fbi-director-kash-patel-s-alcohol-abuse-demand-he-submit-to-alcohol-abuse-screening).

On April 22, 2026, The New York Times published "Inside Kash Patel's F.B.I." (https://www.nytimes.com/2026/04/22/podcasts/the-daily/kash-patel-fbi.html), a podcast and reporting project by Emily Bazelon and Rachel Poser focusing on the transformation of the FBI under Patel's leadership. However, the NYT piece did not independently corroborate the specific drinking or absence allegations — it mentioned The Atlantic's report only for context and did not present its own original sourcing on those claims [Inside Kash Patel's F.B.I. - The New York Times](https://www.nytimes.com/2026/04/22/podcasts/the-daily/kash-patel-fbi.html).

As of April 28, 2026, CNN has explicitly stated it "has not independently corroborated the anecdotes reported in The Atlantic's article." Multiple outlets (CNN, Washington Post, NBC News, Reuters) have covered the story and the lawsuit but none have published independent corroboration of the drinking/absence allegations with their own original sourcing.

Original Atlantic report: https://www.theatlantic.com/politics/2026/04/kash-patel-fbi-director-drinking-absences/686839/

**Exact later resolution packet**

The question resolves NO. It asks whether, between April 29, 2026 and June 1, 2026, at least one of the 11 listed major outlets (NYT, WaPo, WSJ, CNN, Reuters, AP, NBC, CBS, ABC, Politico, Bloomberg) published an investigative report independently corroborating Kash Patel's "excessive drinking" or "unexplained absences" using its OWN original sourcing (not merely referencing The Atlantic).

Evidence gathered shows that all coverage by these outlets during the window only referenced The Atlantic's original April 17, 2026 report rather than adding independent confirmation:

- The Washington Post's May 12, 2026 article ("Kash Patel lashes out as lawmakers question 'excessive drinking'") is hearing coverage that explicitly centers questions on "a recent news report" (The Atlantic) and provides no original Post sourcing for the drinking/absence claims [Kash Patel lashes out as lawmakers question 'excessive drinking'](https://www.washingtonpost.com/national-security/2026/05/12/kash-patel-lashes-out-lawmakers-question-excessive-drinking/).
- CNN's May 12, 2026 hearing takeaways article ("Takeaways from FBI Director Kash Patel's defensive Hill testimony") attributes allegations to The Atlantic and offers no independent corroboration [Takeaways from FBI Director Kash Patel's fiery Hill testimony](https://www.cnn.com/2026/05/12/politics/patel-van-hollen-reports-of-behavior-hill-testimony). (CNN had earlier, on April 28, explicitly stated it "has not independently corroborated" The Atlantic's anecdotes.)
- NBC News's article on House Judiciary Democrats demanding alcohol screening (April 22, 2026) consistently attributes the allegations to The Atlantic and presents no new independent evidence [Democrats want FBI Director Kash Patel to fill out alcohol use ...](https://www.nbcnews.com/politics/justice-department/democrats-want-fbi-director-kash-patel-fill-alcohol-use-screening-test-rcna341343).
- The Wikipedia "Kash Patel" article (last edited May 31, 2026) traces all drinking/absence allegations to The Atlantic and notes no listed outlet independently corroborated them during the window [Kash Patel - Wikipedia](https://en.wikipedia.org/wiki/Kash_Patel).
- The Advocate (May 7, 2026) recounting the controversy shows follow-up corroboration came from The Atlantic itself (a May 2026 "Ka$h" bourbon follow-up) and from MS NOW—neither of which is on the list of 11 qualifying outlets [New FBI alcohol controversy engulfs Kash Patel | Advocate.com](https://www.advocate.com/politics/national/kash-patel-alcohol-controversies).

The only fresh, document-based investigative reporting by qualifying outlets during the window concerned travel ethics, not the specific drinking/absence allegations:
- The AP's May 15, 2026 investigation based on government emails it obtained ("VIP snorkel" at Pearl Harbor) addressed misuse-of-resources/travel ethics, not excessive drinking or unexplained absences from duty [Emails show Kash Patel went on a 'VIP snorkel' at Pearl Harbor](https://apnews.com/article/fbi-kash-patel-snorkel-hawaii-pearl-harbor-192a81cde7a5879aab747bc0ba4b78b9).
- The NYT's May 15, 2026 article on Patel's travel (snorkeling, FBI jet trips) likewise focused on ethical/travel concerns, not corroborating the drinking or the "unexplained absences from his duties" allegations [Snorkeling at Pearl Harbor: Kash Patel's Travels Add to Focus on ...](https://www.nytimes.com/2026/05/15/us/politics/patel-fbi-travel-snorkeling-pearl-harbor.html).

These travel pieces, although independently sourced, do not corroborate the specific resolution-defined claims of "excessive drinking" (alcohol impairing duties) or "unexplained absences" (absent from duties without official explanation, missing meetings, being unreachable). They corroborate a different topic (mixing leisure/government travel).

Because no qualifying outlet published an investigative report with its own original sourcing corroborating the specific drinking or unexplained-absence allegations between April 29 and June 1, 2026, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-131. `05051656-5672-5441-a76d-fa51b8ce8273`

- Present date: `2026-05-14 00:46:45.943616`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-17T00:00:00`

**Question**

Will Jerome Powell attend the June 16–17, 2026, FOMC meeting as a voting member of the Board of Governors?

**Resolution criteria**

This question resolves **Yes** if Jerome Powell is listed as a participant and voting member in the official FOMC statement or meeting minutes for the June 16–17, 2026, meeting, as published on the Federal Reserve's "Meeting Calendars and Information" page at https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm.

Specifically, Powell must appear in the "Participants" section of the FOMC statement (released on the final day of the meeting, typically at 2:00 PM ET / 18:00 UTC on June 17, 2026) as a voting member—i.e., listed among the governors or members who voted on the policy decision, not as an "alternate" or observer.

**Key definitions:**
- **"Voting member"**: A member of the [Board of Governors of the Federal Reserve System](https://www.federalreserve.gov/aboutthefed/bios/board/default.htm) who participates in the FOMC vote on the federal funds rate target. All sitting governors are automatically voting members of the FOMC per [Federal Reserve Act Section 12A](https://www.federalreserve.gov/aboutthefed/section12a.htm).
- **"Attend as a voting member"**: Being listed among the voting participants in the official FOMC statement released at https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm. If Powell is listed as having voted (for or against the policy action, or as having dissented), this counts.
- **"Board of Governors"**: The [Board of Governors of the Federal Reserve System](https://www.federalreserve.gov/aboutthefed/bios/board/default.htm), the seven-member body that governs the Federal Reserve.

If the June 16–17, 2026, FOMC meeting is cancelled or rescheduled to after July 1, 2026 (all times UTC), this question resolves **N/A**.

If Powell attends the meeting but only in a non-voting capacity (e.g., as a special advisor), this resolves **No**.

**Pre-cutoff background**

Jerome Powell's term as Chair of the Federal Reserve ends on May 15, 2026. On April 29, 2026, Powell announced: "After my term as chair ends on May 15, I will continue to serve as a governor for a period of time to be determined." His term as a member of the Board of Governors does not expire until January 31, 2028. Kevin Warsh is expected to succeed him as Chair.

Powell cited ongoing Department of Justice legal actions against the Federal Reserve as a key reason for staying. However, he qualified his commitment as "for a period of time to be determined," leaving open the possibility of an earlier departure.

**Historical context:** No modern Fed Chair has remained on the Board of Governors as a regular governor after their chairmanship ended. Previous chairs (Bernanke, Yellen, Greenspan) all resigned from the Board when their chair terms expired. Powell's decision to stay is historically unprecedented, which adds uncertainty about whether he will follow through, especially given potential political pressure from the Trump administration and the dynamics of serving under new Chair Warsh.

**Status quo as of May 12, 2026:** Powell has publicly stated his intention to remain on the Board past May 15. His governor term runs through 2028. However, his language ("a period of time to be determined") leaves room for a resignation before the June FOMC meeting. Political dynamics, potential friction with incoming Chair Warsh, or resolution of the DOJ probe could all change the calculus.

The next FOMC meeting after Powell's chairmanship ends is scheduled for June 16–17, 2026 (see the [Federal Reserve's FOMC calendar](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)). All sitting members of the Board of Governors are voting members of the FOMC (per [12 U.S.C. § 263](https://www.law.cornell.edu/uscode/text/12/263) and [the Federal Reserve's FOMC structure page](https://www.federalreserve.gov/monetarypolicy/fomc.htm)).

**Exact later resolution packet**

RESOLUTION: NO (0).

The question resolves NO under an extremely literal reading of its own resolution criteria, even though Jerome Powell substantively remained a voting governor.

STEP 1 — The meeting happened, so no N/A. The June 16–17, 2026 FOMC meeting occurred as scheduled; it was Kevin Warsh's first meeting as Chair, and the FOMC voted 12–0 to hold the federal funds rate at 3.50%–3.75% [8f0ae4][e2160f][94cc9e][90069b]. It was not cancelled or rescheduled past July 1, 2026, so the N/A condition does not apply.

STEP 2 — What the resolution criteria literally require. The criteria state the question "resolves Yes if Jerome Powell is listed as a participant and voting member in the official FOMC statement or meeting minutes," and specify that Powell "must appear in the 'Participants' section of the FOMC statement … as a voting member—i.e., listed among the governors or members who voted." The operational definition of "Attend as a voting member" is: "Being listed among the voting participants in the official FOMC statement … If Powell is listed as having voted … this counts." So YES requires Powell to be NAMED/LISTED in the statement (or minutes).

STEP 3 — The decisive fact: the June 2026 statement names NO voters. Under Chair Warsh's reforms, the statement was rewritten and no longer lists individual voting members. J.P. Morgan Asset Management states verbatim: "The new statement does not name the voters but states it was a 12-0 vote" [e6fba1]. CNBC's redline analysis ("Chairman Warsh drastically alters Fed rate statement") confirms the statement "contained no information on how members voted, previously a fixture … under former … Chairman Jerome Powell" [bf1d00], and a direct read of the Fed's official statement page likewise found no individual names listed [90069b]. Because the statement lists NO names at all, Powell is not "listed as having voted" in it — the literal YES condition via the statement is not met.

STEP 4 — The minutes do not save it. The criteria allow "meeting minutes" as an alternative source, but (a) minutes for the June meeting are released ~3 weeks later (≈July 8, 2026), i.e., after the meeting and outside the July-1-anchored resolution window; and (b) the Fed's 2026 minutes format itself "do not identify individual participants," using anonymized characterizations like "some," "a few," "many" [3560cb]. So the minutes provide no listing of Powell as a named voter either.

STEP 5 — Why the substantive reality does not flip this to YES. It is true that Powell remained a sitting governor and was, in substance, one of the 12 FOMC voting members: Spectrum News reports "Warsh and Powell each get one vote for Federal Open Market Committee interest rate decisions" [e2160f]; Kiplinger explicitly lists "Fed Governor Jerome Powell" among the 12 2026 FOMC voters [8f0ae4]; Fortune notes "Jerome Powell—who stays on at the Fed as a governor" [9d09d7]; and Federal News Network states "Powell will get a vote on Fed policy" and "Powell remains on the Board of Governors" [2109bb]. However, the question's criteria do not resolve on Powell's mere status; they require him to be explicitly LISTED/named as a voting member in the official statement (or minutes). Being one of "12" unnamed votes is not the same as being "listed as having voted." Per the instruction to be extremely literal and let the resolution criteria supersede reasonable interpretations, this fails the YES condition.

STEP 6 — Not an annulment. The only specified N/A trigger is cancellation/rescheduling past July 1, which did not occur. The statement was published on time (June 17, 2026); it simply omits voter names. That is a resolvable NO, not an annullable situation.

Primary source URLs: Official statement — https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm ; Meeting page (on the Meeting Calendars and Information site) — https://www.federalreserve.gov/monetarypolicy/fomcpresconf20260617.htm ; Calendar hub — https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm .

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-132. `f96455a1-a3a2-5180-a110-d9c931bd3934`

- Present date: `2026-05-03 05:15:57.247039`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will any major Ethiopian opposition party formally announce a boycott of the June 1, 2026 general election between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if at least one major Ethiopian opposition party formally announces a boycott of the June 1, 2026 general election. The announcement must occur on or after May 1, 2026, and before voting begins at 06:00 EAT (03:00 UTC) on June 1, 2026.

**Definition of "major opposition party":** A party meeting at least one of the following criteria:
1. Held at least one seat in the House of People's Representatives (Ethiopia's lower house of parliament, see [Wikipedia](https://en.wikipedia.org/wiki/House_of_Peoples%27_Representatives)) as of the dissolution of the previous parliament; OR
2. Is one of the following specifically named parties: Ethiopian Citizens for Social Justice (EZEMA/Balderas), Oromo Federalist Congress (OFC), Oromo Liberation Front (OLF), Ethiopian People's Revolutionary Party (EPRP), National Movement of Amhara (NaMA/NAMA), Tigray Democratic Solidarity, or any coalition containing one of these parties.

**Definition of "boycott":** A public declaration by the party that it will not participate in the June 1, 2026 election—meaning the party directs its candidates to withdraw or instructs its supporters not to vote for the party. A boycott is distinct from merely criticizing the election or calling for protests while still fielding candidates (see [boycott definition](https://en.wikipedia.org/wiki/Election_boycott)).

**Definition of "formal announcement":** The boycott must be announced through at least one of: (a) an official press release or statement on the party's verified website or social media accounts; or (b) a direct quote from a senior party leader (chairperson, secretary-general, or spokesperson) reported by a credible news outlet, including but not limited to: [Addis Standard](https://addisstandard.com/), [The Reporter Ethiopia](https://www.thereporterethiopia.com/), [Reuters](https://www.reuters.com/), [Associated Press](https://apnews.com/), or [AFP](https://www.afp.com/).

If no qualifying announcement is made by any major opposition party before 06:00 EAT on June 1, 2026, this question resolves **No**.

**Pre-cutoff background**

Ethiopia is scheduled to hold its seventh national parliamentary election on June 1, 2026 (East Africa Time, UTC+3). The ruling Prosperity Party, led by Prime Minister Abiy Ahmed, is seeking to maintain its parliamentary majority. According to reports, 47 political parties have registered with the National Election Board of Ethiopia (NEBE) and over 10,900 candidates are participating [https://hornreview.org/2026/04/21/the-horn-in-2026-a-year-of-elections/](https://hornreview.org/2026/04/21/the-horn-in-2026-a-year-of-elections/).

The electoral environment is marked by significant tension. Opposition parties have criticized NEBE's "unaudited" digital election system and raised concerns about broader electoral conditions [https://hornreview.org/2026/04/21/the-horn-in-2026-a-year-of-elections/](https://hornreview.org/2026/04/21/the-horn-in-2026-a-year-of-elections/). The Tigray People's Liberation Front (TPLF), historically one of Ethiopia's most powerful parties, had its legal status revoked by NEBE in May 2025 [Ethiopia: Expanding Representation While Managing Centrifugal ...](https://africacenter.org/spotlight/en-elections-2026/ethiopia/). The Ethiopian People's Revolutionary Party (EPRP) has called for nationwide protests on May 8, 2026, amid concerns over electoral conditions. Tigray Democratic Solidarity has threatened to boycott the elections over unresolved disputes with the House of Federation. The government lowered the threshold for party participation in parliament from 15% to 10% to encourage broader representation [Ethiopia: Expanding Representation While Managing Centrifugal ...](https://africacenter.org/spotlight/en-elections-2026/ethiopia/).

Despite these tensions, the large number of registered parties and candidates suggests most opposition groups intend to participate. Security concerns persist in Tigray, Amhara, and Oromia regions, and journalists and civil society groups face intimidation [Ethiopia: Expanding Representation While Managing Centrifugal ...](https://africacenter.org/spotlight/en-elections-2026/ethiopia/). The question captures the tension between opposition parties' criticisms of the electoral process and their decision to participate or boycott.

Key sources for monitoring: [Addis Standard](https://addisstandard.com/), [The Reporter Ethiopia](https://www.thereporterethiopia.com/), [NEBE](https://nfrethiopia.org/), Reuters, and AP.

**Exact later resolution packet**

The question resolves NO. No qualifying "major opposition party" (one that held ≥1 seat in the House of Peoples' Representatives at the previous parliament's dissolution, OR is among the named parties EZEMA, OFC, OLF, EPRP, NaMA, Tigray Democratic Solidarity, or a coalition containing one of them) formally announced an election boycott within the required window of May 1, 2026 to 06:00 EAT June 1, 2026.

Evidence reviewed:
1) ONLF (Ogaden National Liberation Front) DID formally announce on May 6, 2026 that it "will not participate in Ethiopia's deceptive election" [8f0834] — this is the only in-window boycott-type announcement found. However, ONLF does NOT meet the "major opposition party" definition: per the 2021 election results, ONLF won zero seats (only 5,634 votes, 0.02%) and held no HoPR seat [4b95f2], and ONLF is not in the question's enumerated list of named parties. Thus it does not qualify.

2) Tigray Democratic Solidarity (Simret), a named party, only conditionally THREATENED to boycott in February 2026 (over the House of Federation constituency dispute) — outside the May 1–June 1 window — and subsequently withdrew its lawsuit and registered to participate [78a06c]. No in-window formal boycott announcement.

3) The Peace for Ethiopia Coalition (eight parties) threatened to WITHDRAW on April 17, 2026 — before the window — and it was a conditional threat ("unless widespread violations are addressed"); the coalition went on to campaign and contest seats [bfb124, f913ed]. Out of window and not an unconditional boycott.

4) OFC (named party) was "squeezed into fielding just ten candidates to escape deregistration" — i.e., it PARTICIPATED rather than boycotted; its chairman said this was to meet legal obligations [bfb124, f913ed]. Pre-election (May 29) and election-day (June 1) coverage confirm major opposition parties including NaMA and EZEMA (which held 5 and 4 seats respectively in 2021) fielded candidates and participated [8089af, b48cf2, 5b4c9f].

5) EPRP (named party) called for nationwide protests on May 8, 2026 — explicitly criticism/protest, not a boycott, and the resolution criteria distinguish protests from boycotts.

6) The registered OLF party's only located boycott-style press release dates to 2021 [7ef9f2]; the OLF-OLA statements come from an armed group, not the registered party.

Since the only in-window non-participation declaration (ONLF, May 6) came from a party that fails the "major opposition party" test, and all named/seated parties either participated or only threatened/protested (and Simret's and the coalition's threats fell outside the window), no qualifying formal boycott announcement occurred. Resolution: NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-133. `2fe00425-ecf9-5969-b063-8e7f02b0d6a6`

- Present date: `2026-05-14 07:05:53.352358`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Trump administration issue a new executive order or presidential memorandum further restricting federal employee union rights between May 12, 2026, and July 1, 2026?

**Resolution criteria**

This question resolves as **YES** if, on or after May 12, 2026, and no later than 11:59 PM UTC on July 1, 2026, the President of the United States signs a new Executive Order or Presidential Memorandum that further restricts federal employee union rights.

**Definitions:**

- **Executive Order** and **Presidential Memorandum** are defined per the Federal Register's classifications (https://www.federalregister.gov/presidential-documents). Only documents published or scheduled for publication in the Federal Register under these two categories qualify. Agency directives, OPM guidance, or secretarial orders issued under delegated authority from prior EOs do not count.

- **"Further restricting federal employee union rights"** means the document does at least one of the following:
  1. Excludes or suspends additional federal agencies, subdivisions, or categories of employees from coverage under the Federal Service Labor-Management Relations Statute (5 U.S.C. Chapter 71) beyond those already excluded by EO 14251 (March 27, 2025) and the August 28, 2025 order;
  2. Imposes new substantive limitations on the scope of collective bargaining for federal employees (e.g., restricting bargainable topics, limiting official time, restricting union access to facilities);
  3. Directs the decertification, derecognition, or termination of federal employee unions or their bargaining agreements by executive action beyond what is already required by EO 14251 and the August 28, 2025 order;
  4. Revokes or narrows existing statutory or regulatory protections for federal employee union activity.

- Orders that merely amend, clarify, or extend implementation timelines for EO 14251 or the August 28, 2025 order without expanding restrictions to new agencies/employees or imposing new limitations do **not** qualify.

**Resolution source:** The Federal Register (https://www.federalregister.gov/presidential-documents/executive-orders) and/or the White House official Presidential Actions page (https://www.whitehouse.gov/presidential-actions/).

If no qualifying document is published by 11:59 PM UTC on July 1, 2026, this question resolves **NO**.

**Pre-cutoff background**

The Trump administration has pursued an escalating campaign to restrict federal employee union rights through executive action. On March 27, 2025, President Trump signed Executive Order 14251, "Exclusions from Federal Labor-Management Relations Programs," which excluded approximately 40 federal agencies and subdivisions from coverage under the Federal Service Labor-Management Relations Statute (FSLMRS, Chapter 71 of title 5, United States Code), effectively stripping collective bargaining rights from roughly two-thirds of the federal workforce by citing national security justifications [Exclusions from Federal Labor-Management Relations Programs](https://www.whitehouse.gov/presidential-actions/2025/03/exclusions-from-federal-labor-management-relations-programs/). On August 28, 2025, the administration issued a follow-up executive order, "Further Exclusions from the Federal Labor-Management Relations Program," which expanded the list of excluded agencies to include NASA, the National Weather Service, the U.S. Agency for Global Media, and additional subdivisions of the Department of Commerce and Bureau of Reclamation [Further Exclusions from the Federal Labor-Management Relations ...](https://www.whitehouse.gov/presidential-actions/2025/08/further-exclusions-from-the-federal-labor-management-relations-program/).

These orders have faced significant legal challenges from federal employee unions, including the American Federation of Government Employees (AFGE). A federal judge issued a preliminary injunction in April 2025 blocking aspects of EO 14251. Despite ongoing litigation, in early 2026 the Office of Personnel Management directed agencies to proceed with terminating collective bargaining agreements and derecognizing unions. In April 2026, Defense Secretary Hegseth ordered termination of all DOD collective bargaining agreements not subject to a court order.

As of May 2026, the legal landscape remains contested, with courts issuing mixed rulings. The administration has demonstrated a pattern of issuing new executive actions to expand restrictions even while prior orders face litigation. The question is whether the administration will issue yet another distinct executive order or presidential memorandum on this topic during the specified window.

**Exact later resolution packet**

The question resolves NO. No qualifying Executive Order or Presidential Memorandum further restricting federal employee union rights (per the Federal Register's classifications) was signed between May 12, 2026 and 11:59 PM UTC July 1, 2026.

Evidence:

1) Complete list of Trump Executive Orders signed in the window (from the Federal Register 2026 EO index) is EO 14405 through EO 14413 [350459]:
 - EO 14405 Integrating Financial Technology Innovation Into Regulatory Frameworks (May 19, 2026)
 - EO 14406 Restoring Integrity to America's Financial System (May 19, 2026)
 - EO 14407 Realigning U.S. Core Childhood Vaccine Recommendations (May 29, 2026)
 - EO 14408 Removing Restrictions on Access to Federal Lands (May 29, 2026)
 - EO 14409 Promoting Advanced AI Innovation and Security (June 2, 2026)
 - EO 14410 Implementing Schedule Policy/Career in the Excepted Service (June 3, 2026)
 - EO 14411 Strengthening Customs Enforcement (June 3, 2026)
 - EO 14412 Securing the Nation Against Advanced Cryptographic Attacks (June 22, 2026)
 - EO 14413 Ushering in the Next Frontier of Quantum Innovation (June 22, 2026)
None of these are "further exclusions" / labor-management relations orders.

2) The only federal-workforce order in the window, EO 14410 "Implementing Schedule Policy/Career in the Excepted Service" (June 3, 2026), does NOT satisfy any of the four resolution criteria. Its full text (verified on both federalregister.gov and whitehouse.gov) contains no mention of "collective bargaining," "unions," "labor organizations," "official time," or the Federal Service Labor-Management Relations Statute (5 U.S.C. Chapter 71). It concerns only civil-service tenure protections — converting ~8,000 policy-influencing career positions into the excepted service (at-will, removing MSPB appeal rights) [949ef1, baa9a3]. It does not exclude agencies/employees from the FSLMRS, restrict collective-bargaining scope, direct decertification/termination of unions or CBAs, or revoke union-activity protections. (Commentators noted it may only indirectly "shrink bargaining units over time" — an indirect effect, not a restriction imposed by the order itself, and not covered by the criteria.)

3) No qualifying Presidential Memorandum was issued in the window. The frequently-cited Trump memo "limiting collective bargaining agreements reached with federal workers" dates to early 2025 (signed Feb/Jan 2025), not the window [d1d030]. The only presidential memoranda identified in the window (e.g., NSPM-12 of June 12, 2026, on securing National Security Systems) are unrelated to union rights.

Therefore, no Executive Order or Presidential Memorandum meeting the definition of "further restricting federal employee union rights" was signed in the window, and the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-134. `77eaf3ec-051d-517d-a7e9-13775913b49d`

- Present date: `2026-05-02 10:11:29.735457`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will any top-10 container shipping line (by Alphaliner TEU capacity) announce a new suspension or rerouting of services away from the Suez Canal between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves YES if, between 00:00 UTC on May 1, 2026, and 23:59 UTC on June 1, 2026, any of the top 10 container shipping lines by TEU capacity (as listed on Alphaliner's TOP 100 at https://alphaliner.axsmarine.com/PublicTop100/ as of April 30, 2026 — see background for the list) issues or is confirmed to have issued a public announcement constituting a new suspension or rerouting of container services away from the Suez Canal.

Definitions:
- "New suspension or rerouting" means an official company communication (press release, customer advisory, or investor notice) published on or after May 1, 2026 (00:00 UTC), stating that one or more container shipping services previously scheduled or operating via the Suez Canal will instead be routed via the Cape of Good Hope or otherwise diverted away from the Suez Canal / Red Sea / Bab el-Mandeb Strait. This explicitly excludes the continuation of existing Cape of Good Hope diversions that were already in effect before May 1, 2026, without a new announcement regarding a change in routing policy.
- "Top 10 container shipping lines" are defined by Alphaliner's publicly available TOP 100 ranking (https://alphaliner.axsmarine.com/PublicTop100/) as of the April 30, 2026 snapshot [Top 100](https://alphaliner.axsmarine.com/PublicTop100/).

Resolution sources (in order of preference):
1. Official carrier newsrooms/press releases:
   - MSC: https://www.msc.com/en/newsroom
   - Maersk: https://www.maersk.com/news
   - CMA CGM: https://www.cma-cgm.com/news
   - COSCO: https://lines.coscoshipping.com/home/news
   - Hapag-Lloyd: https://www.hapag-lloyd.com/en/press/press-releases.html
   - ONE: https://www.one-line.com/en/news
   - Evergreen: https://www.evergreen-line.com/tsp1/jsp/TBN1_News.jsp
   - HMM: https://www.hmm21.com/cms/company/engn/introduce/news/1193205_7702.jsp
   - Yang Ming: https://www.yangming.com/news/press_release.aspx
   - ZIM: https://www.zim.com/news
2. Credible maritime/general news sources: Reuters (https://www.reuters.com), Bloomberg, Lloyd's List, gCaptain (https://gcaptain.com), The Loadstar, Splash247, or Seatrade Maritime (https://www.seatrade-maritime.com).

The question resolves NO if no such new announcement is confirmed by 23:59 UTC on June 1, 2026.

**Pre-cutoff background**

Since late 2023, Houthi attacks in the Red Sea have forced major container shipping lines to divert vessels around the Cape of Good Hope instead of transiting the Suez Canal. Throughout early 2026, carriers oscillated between attempting returns to the Suez Canal and pulling back due to security escalations. CMA CGM and Maersk began tentative returns to Suez routing in January 2026, but by March 1, 2026, Maersk, Hapag-Lloyd, CMA CGM, and MSC had all suspended or rerouted services away from the Suez Canal following a deteriorating security situation in the Middle East, including strikes on Iran [Shipping companies divert vessels around Cape of Good Hope after ...](https://www.reuters.com/world/middle-east/maersk-pauses-sailings-through-suez-canal-bab-el-mandeb-strait-citing-escalating-2026-03-01/).

As of April 30, 2026, the top 10 container shipping lines by TEU capacity according to Alphaliner's TOP 100 list (https://alphaliner.axsmarine.com/PublicTop100/) are [Top 100](https://alphaliner.axsmarine.com/PublicTop100/):

1. Mediterranean Shipping Company (MSC) — 7,318,632 TEU
2. Maersk — 4,650,330 TEU
3. CMA CGM Group — 4,273,202 TEU
4. COSCO Group — 3,593,746 TEU
5. Hapag-Lloyd — 2,400,946 TEU
6. Ocean Network Express (ONE) — 2,134,872 TEU
7. Evergreen Line — 1,973,231 TEU
8. HMM Co Ltd — 1,029,773 TEU
9. Yang Ming Marine Transport Corp. — 741,908 TEU
10. ZIM — 698,205 TEU

Current routing status as of May 1, 2026: Most major carriers are predominantly routing via the Cape of Good Hope following the March 2026 suspensions [Shipping companies divert vessels around Cape of Good Hope after ...](https://www.reuters.com/world/middle-east/maersk-pauses-sailings-through-suez-canal-bab-el-mandeb-strait-citing-escalating-2026-03-01/). Some carriers had been experimenting with selective Suez transits on certain services, and the situation remains fluid with carriers potentially resuming Suez routing if security conditions improve. The Ocean Alliance (OOCL, Evergreen, CMA CGM, COSCO) has retained Cape of Good Hope routing for its network. The question is whether any carrier will announce a *new* suspension or rerouting away from Suez during May 2026 — this would require at least one carrier to have resumed or planned Suez transits and then reversed course, or for a carrier still partially using Suez to announce a new withdrawal.

**Exact later resolution packet**

The question resolves NO. It requires that, between 00:00 UTC May 1, 2026 and 23:59 UTC June 1, 2026, one of the listed top-10 container lines (MSC, Maersk, CMA CGM, COSCO, Hapag-Lloyd, ONE, Evergreen, HMM, Yang Ming, ZIM) issued a NEW official announcement rerouting services previously scheduled/operating via the Suez Canal to the Cape of Good Hope or otherwise away from Suez/Red Sea/Bab el-Mandeb. Continuation of pre-existing Cape diversions does not count.

Key findings:
- By March 1, 2026, Maersk, Hapag-Lloyd, CMA CGM and MSC had already suspended/rerouted services away from Suez via the Cape of Good Hope following the Iran strikes and Strait of Hormuz crisis. These were the last major rerouting announcements, all PREDATING the May 1 window (e.g., Maersk ME11 & MECL rerouting dated March 1, 2026).
- During May 2026, the dominant theme was a "Hormuz stalemate," with carriers already on Cape of Good Hope routing as the status quo. The Seatrade Maritime "May 2026 in review" round-up reports no new Suez rerouting/suspension by a major carrier during May; the situation was a continuation of existing diversions [77a2b3].
- Maersk's direction in May was the OPPOSITE of a new diversion: a WorldCargo News article dated May 7, 2026 reported Maersk CEO Vincent Clerc saying the company was "reviewing the possibility of resuming some of its services through the Red Sea" [7e6af4].
- Maersk's official news/advisory page (stay-ahead and /news) listed May 2026 items, none of which announced a new Suez/Red Sea rerouting. The May 25 "Middle East Operational Update 33" concerned landside/Gulf port bookings and Strait of Hormuz, not a new Suez diversion [d8e342, b24e4d]. The May 28 "Changes to cargo routed via Jeddah" was a transshipment-hub change (moving cargo from Jeddah to Salalah/Khor Fakkan), explicitly stating Saudi cargo continues via Jeddah — it is not a suspension/rerouting of services away from the Suez Canal [ae472b, 34bc2a, c9dee1].
- A May 28, 2026 industry overview ("Cape of Good Hope Route Diversions: A Permanent Shift in 2026?") characterized the May situation as a solidified "dual-route equilibrium"/continuation of the diversions established after the March 2026 escalations, with no new carrier announcements [d1d702].
- gCaptain's Red Sea tag showed only military/oil-market articles in May 2026 (France aircraft carrier May 6; Saudi oil windfall May 2), no new container-line rerouting [d722df].

No qualifying NEW suspension/rerouting announcement by a top-10 carrier was found within the May 1 – June 1, 2026 window; all such announcements occurred earlier (Jan–Mar 2026), and the existing Cape of Good Hope diversions merely continued. Per the resolution criteria, continuation without a new announcement does not qualify. Therefore the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-135. `f8f06082-83bb-50be-ae8c-4a323d115721`

- Present date: `2026-05-12 22:23:04.636672`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the PRAC recommend a label update for semaglutide-containing products (Ozempic, Wegovy, Rybelsus, Kayshild) regarding peripheral neuropathy at its May or June 2026 plenary meeting?

**Resolution criteria**

This question resolves as **Yes** if the EMA publishes official PRAC meeting highlights or PRAC recommendations on safety signals — available at https://www.ema.europa.eu/en/committees/pharmacovigilance-risk-assessment-committee-prac or https://www.ema.europa.eu/en/human-regulatory-overview/post-authorisation/pharmacovigilance-post-authorisation/signal-management/prac-recommendations-safety-signals — confirming that the PRAC has adopted a recommendation for a label update regarding peripheral neuropathy for any semaglutide-containing product (specifically Ozempic, Wegovy, Rybelsus, or Kayshild) at either the May 2026 (4–7 May) or June 2026 (8–11 June) PRAC plenary meetings.

A "recommendation for a label update" means a PRAC recommendation that the Summary of Product Characteristics (SmPC) and/or Package Leaflet (PL) of one or more of the named semaglutide products be amended to include information about peripheral neuropathy (e.g., as a warning, precaution, or listed adverse reaction).

This question resolves as **No** if:
- The PRAC closes the signal without recommending a label update at either the May or June 2026 plenary meetings; or
- The PRAC requests further data, additional studies, or a "follow-up" assessment instead of adopting a final recommendation for a label update at either meeting; or
- No recommendation regarding peripheral neuropathy for the named semaglutide products is adopted at either the May or June 2026 plenary meetings; or
- The relevant meeting highlights for the June 2026 PRAC plenary are not published by 23:59 UTC on June 30, 2026.

All deadlines and meeting windows referenced in these criteria are in UTC.

**Pre-cutoff background**

The European Medicines Agency's (EMA) Pharmacovigilance Risk Assessment Committee (PRAC) is responsible for assessing safety signals for medicines authorised in the EU. At its May 4–7, 2026 plenary meeting, the PRAC had a signal assessment for peripheral neuropathies associated with semaglutide-containing products — Ozempic, Wegovy, Rybelsus, and Kayshild — listed as Item 4.1.4 on the draft agenda, with the action "For adoption of PRAC recommendation" [Meeting highlights from the Pharmacovigilance Risk Assessment ...](https://www.ema.europa.eu/en/news/meeting-highlights-pharmacovigilance-risk-assessment-committee-prac-4-7-may-2026). However, the published May 2026 meeting highlights did not report a concluded outcome on this specific signal assessment [Meeting highlights from the Pharmacovigilance Risk Assessment ...](https://www.ema.europa.eu/en/news/meeting-highlights-pharmacovigilance-risk-assessment-committee-prac-4-7-may-2026), suggesting the matter may have been deferred or that details were not disclosed in the highlights summary. The next PRAC plenary meeting is scheduled for June 8–11, 2026, at which the signal could be carried over for a recommendation. PRAC signal assessments can result in a recommendation to update the product label (Summary of Product Characteristics and/or Package Leaflet), a request for further data from the marketing authorisation holder, or closure of the signal. A precedent exists for PRAC recommending label updates for semaglutide products — in 2024, PRAC recommended adding warnings regarding non-arteritic anterior ischaemic optic neuropathy (NAION) to semaglutide product information. The EMA publishes meeting highlights and PRAC recommendations on safety signals after each plenary meeting at: https://www.ema.europa.eu/en/committees/pharmacovigilance-risk-assessment-committee-prac

**Exact later resolution packet**

The question resolves **NO**. For a YES, the EMA would have had to publish PRAC meeting highlights or PRAC recommendations on safety signals confirming that the PRAC adopted a recommendation to update the SmPC and/or Package Leaflet regarding peripheral neuropathy for a named semaglutide product (Ozempic, Wegovy, Rybelsus, or Kayshild) at the May 2026 (4–7 May) or June 2026 (8–11 June) plenary meetings. No such recommendation was adopted/published by the 30 June 2026 deadline.

Evidence:

1) May 2026 meeting (4–7 May): The signal of peripheral neuropathies for semaglutide (Ozempic, Wegovy, Rybelsus, Kayshild), EPITT 20270, was on the agenda as item 4.1.4 "For adoption of PRAC recommendation," but the official EMA meeting highlights (published 8 May 2026) reported no concluded outcome on this specific signal — it was apparently deferred/not disclosed [Meeting highlights from the Pharmacovigilance Risk Assessment ...](https://www.ema.europa.eu/en/news/meeting-highlights-pharmacovigilance-risk-assessment-committee-prac-4-7-may-2026). https://www.ema.europa.eu/en/news/meeting-highlights-pharmacovigilance-risk-assessment-committee-prac-4-7-may-2026

2) The authoritative "PRAC recommendations on signals adopted at the 4-7 May 2026 PRAC meeting" document was published 22 June 2026 (within the resolution window). It does NOT contain any recommendation for a label update regarding peripheral neuropathy for any semaglutide product; the list of all signals discussed (updated 22 June 2026) likewise shows no such semaglutide peripheral-neuropathy recommendation adopted at the May or June 2026 meetings [PRAC recommendations on safety signals](https://www.ema.europa.eu/en/human-regulatory-overview/post-authorisation/pharmacovigilance-post-authorisation/signal-management/prac-recommendations-safety-signals) [Variation Applications - Referrals, PSUSA Procedures and PRAC ...](https://halmed.hr/en/Lijekovi/Arbitrazni-postupci-PSUSA-postupci-i-PRAC-signali-upute-za-prijavu-izmjena-/Upute-za-prijavu-izmjena-na-temelju-preporuka-PRAC-a-nakon-ocjene-sigurnosnih-signala/). https://www.ema.europa.eu/en/human-regulatory-overview/post-authorisation/pharmacovigilance-post-authorisation/signal-management/prac-recommendations-safety-signals

3) June 2026 meeting (8–11 June): The official EMA meeting highlights were published 12 June 2026 (before the 30 June 2026 23:59 UTC deadline), so the June-highlights-not-published NO clause does not apply. However, those highlights concerned other topics (valproate/neurodevelopmental disorders, Ixchiq, Tavneos) and contain no recommendation, conclusion, or label update regarding peripheral neuropathy for any semaglutide product [Meeting highlights from the Pharmacovigilance Risk Assessment ...](https://www.ema.europa.eu/en/news/meeting-highlights-pharmacovigilance-risk-assessment-committee-prac-8-11-june-2026). https://www.ema.europa.eu/en/news/meeting-highlights-pharmacovigilance-risk-assessment-committee-prac-8-11-june-2026

Because no PRAC recommendation for a label update on peripheral neuropathy for Ozempic, Wegovy, Rybelsus, or Kayshild was adopted and published (in either the highlights or the signal recommendations documents) for either the May or June 2026 meetings by the 30 June 2026 deadline, the question resolves NO. This is distinct from the separate 2024–2025 semaglutide review concerning NAION (non-arteritic anterior ischaemic optic neuropathy), which is a different condition and not the subject of this question.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-136. `4ef6a52f-9bcc-5b1d-9679-a6728298a048`

- Present date: `2026-05-02 09:48:01.250835`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the US-Iran ceasefire remain in effect continuously from May 1, 2026 (00:00 UTC) through May 31, 2026 (23:59 UTC)?

**Resolution criteria**

This question resolves **Yes** if, throughout the entire period from May 1, 2026 (00:00 UTC) through May 31, 2026 (23:59 UTC), the US-Iran ceasefire (or a successor permanent agreement) remains continuously in effect—meaning no breach or termination occurs during this period.

A **breach or termination** of the ceasefire is defined as any of the following, as reported by at least one of Reuters (https://www.reuters.com), the Associated Press (https://apnews.com), or UN News (https://news.un.org):

1. **An official declaration** by the US government or Iranian government that the ceasefire has ended or is no longer in effect.
2. **Kinetic military action**: Any airstrike, missile strike, or drone strike launched by US or Israeli forces against Iranian territory or Iranian military assets, OR any missile, drone, or rocket attack launched by Iran or Iranian-directed forces against US or Israeli territory or military assets.

The following do **not** constitute a breach for resolution purposes:
- Continuation of the US naval blockade and associated vessel seizures in the Strait of Hormuz.
- Cyberattacks, covert operations, or proxy actions not involving direct kinetic strikes between the named parties.
- Rhetorical threats or diplomatic breakdowns that do not result in the above kinetic actions or official declarations.

The question resolves **No** if any breach or termination (as defined above) is reported on or after May 1, 2026 (00:00 UTC) and before May 31, 2026 (23:59 UTC).

**Resolution sources**: Reuters (https://www.reuters.com/world/middle-east/), AP News (https://apnews.com/hub/iran), or UN News (https://news.un.org/en/news/topic/peace-and-security).

**Pre-cutoff background**

In late February 2026, the United States and Israel launched joint military strikes on Iran, beginning the 2026 Iran war. On April 8, 2026, a two-week ceasefire was brokered by Pakistan, halting direct air and missile attacks between the US and Iran [2026 Iran war ceasefire - Wikipedia](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire).

On April 21, 2026, President Trump unilaterally announced an indefinite extension of the ceasefire, stating it would last until Iran's "proposal is submitted, and discussions are concluded, one way or the other." The US naval blockade of Iranian ports remained in effect during this extension, and it was unclear whether Iran or Israel formally agreed to the terms [US announces ceasefire extension with Iran | Reuters](https://www.reuters.com/world/middle-east/us-positive-iran-deal-talks-still-uncertain-ceasefire-end-nears-2026-04-21/).

As of May 1, 2026, the ceasefire is described as "ongoing yet fragile." While direct air and missile strikes have largely halted since April 8, hostilities continue in and around the Strait of Hormuz—the US military seized the Iranian-flagged container ship *Touska* on April 20, and Iran captured two foreign commercial vessels shortly thereafter. The Trump administration argues the ceasefire has paused the 60-day War Powers Act clock, a position contested by lawmakers and legal experts [Has the US-Iran ceasefire reset the clock on War Powers Act ...](https://www.aljazeera.com/news/2026/5/1/has-the-us-iran-ceasefire-reset-the-clock-on-war-powers-act-deadline). No permanent agreement or deal is in sight, and multiple actors (Israel, Iran, the US, Pakistan as mediator) have competing incentives that could cause the ceasefire to collapse.

For definitions:
- "Ceasefire": A temporary suspension of fighting by mutual agreement (see https://en.wikipedia.org/wiki/Ceasefire).
- "Permanent agreement": A formal, binding diplomatic accord intended to definitively end hostilities, as distinct from a temporary ceasefire (see https://en.wikipedia.org/wiki/Peace_treaty).

**Exact later resolution packet**

The question resolves NO because multiple kinetic military breaches of the US-Iran ceasefire — exactly the type defined as a breach in the resolution criteria — occurred within the May 1–31, 2026 window, as reported by Reuters (an approved resolution source).

1. Reuters reported that on Tuesday, May 26, 2026, the US struck targets in Iran's southern Hormozgan province, with the US confirming the attacks as "defensive in nature, targeting missile sites and boats attempting to lay mines." Iran's foreign ministry called the strikes a "gross violation" of the ceasefire in place since April 8. The same article reports Iran's Revolutionary Guards fired at a US drone and a fighter jet over the Gulf [7a43fb]. URL: https://www.reuters.com/world/middle-east/rubio-says-iran-deal-could-take-days-us-launches-fresh-strikes-2026-05-26/

2. Reuters reported (May 28, 2026) further kinetic exchanges: US Central Command said its forces shot down five Iranian attack drones and struck a ground control station in the port city of Bandar Abbas about to launch a sixth; a ballistic missile was also fired toward Kuwait, which hosts a large US base [b92bdf]. URL: https://www.reuters.com/world/middle-east/iran-us-trade-air-strikes-after-trump-dismisses-report-hormuz-deal-2026-05-28/

Both the US airstrikes against Iranian territory/military assets (missile sites, the Bandar Abbas ground control station) and Iranian drone/missile attacks against US assets fall squarely within criterion 2 (kinetic military action) of the breach definition. These are distinct from the excluded categories (vessel seizures/naval blockade), as they involve airstrikes and drone strikes. Because at least one such breach occurred during the window, the ceasefire did NOT remain continuously in effect, so the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-137. `5be67ff8-3681-5a79-b241-2a1f025210ce`

- Present date: `2026-05-14 10:42:33.504202`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will SSE plc announce an asset disposal transaction valued at £200 million or more between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between 12 May 2026 00:00 UTC and 1 July 2026 23:59 UTC, SSE plc publishes an announcement via its official Regulatory News Service (RNS) feed (https://www.sse.com/investors/regulatory-news/) or on its official newsroom (https://www.sse.com/news-and-views/) confirming that it has entered into a definitive agreement for an asset disposal transaction valued at £200 million or more. Otherwise, it resolves **No**.

Key definitions:

1. **Asset disposal**: The sale, farm-down, or transfer by SSE of a stake (partial or whole) in a business unit, project, joint venture interest, or infrastructure asset (e.g., an offshore or onshore wind farm stake, a distribution or transmission network interest, a gas-fired power station, or a battery storage portfolio). This includes farm-downs of offshore wind project stakes. It does **not** include routine equipment sales, land sales below the threshold, refinancings, or securitisations that do not transfer ownership.

2. **Value of £200 million**: Refers to the total transaction value as stated in SSE's announcement, measured as the gross consideration (cash and/or non-cash) payable for SSE's interest being disposed of. If SSE's announcement states the value as an enterprise value, that figure is used. If only SSE's share of proceeds is stated, that figure is used. The £200 million threshold must be met by a single transaction (not aggregated across multiple smaller deals).

3. **Valid announcement**: A press release or regulatory filing published on SSE plc's official website (sse.com) or via the London Stock Exchange RNS. Unconfirmed media reports do not count.

4. **Announcement on or after 12 May 2026**: Only announcements dated on or after 12 May 2026 (UTC) count toward resolution, to exclude any prior disposals.

5. **Timezone**: All dates and times are in UTC.

**Pre-cutoff background**

SSE plc announced a £33 billion five-year capital investment plan in November 2025, designed to be approximately 90% self-funded. The remaining funding relies on two pillars: a £2 billion equity raise (completed via a share placing in November 2025) and £2 billion in targeted asset disposals. SSE has described these disposals as "asset rotations across the range of premium assets in our portfolio," which could include farm-downs of stakes in offshore wind projects, sales of electricity distribution or transmission interests, or disposals of other infrastructure assets.

As of SSE's full-year trading update on 2 April 2026, the company reported being on course to deliver around £3.5 billion of capital investment with just over £10 billion of adjusted net debt and hybrid capital, but did not disclose any completed or announced major asset disposals against the £2 billion target [Trading Update | SSE](https://www.sse.com/news-and-views/2026/04/trading-update/). This means, based on the latest publicly available information, SSE has completed £0 of the £2 billion disposal target.

The £200 million threshold represents approximately 10% of the total disposal target. Given SSE's portfolio of premium energy infrastructure assets (including stakes in offshore wind farms such as Dogger Bank, onshore wind, flexible generation, and electricity networks), individual transactions of this size are plausible. However, timing is uncertain — SSE management has not publicly committed to a specific disposal timeline, and energy infrastructure M&A processes can be lengthy.

Key sources for monitoring: SSE's Regulatory News Service (RNS) feed at https://www.sse.com/investors/regulatory-news/ and SSE's newsroom at https://www.sse.com/news-and-views/.

**Exact later resolution packet**

The question resolves NO. Between 12 May 2026 00:00 UTC and 1 July 2026 23:59 UTC, SSE plc did not publish any announcement via its RNS feed or official newsroom confirming a definitive agreement for an asset disposal transaction valued at £200 million or more.

Evidence gathered from the exact sources named in the resolution criteria:

1. SSE's official Regulatory News page (https://www.sse.com/investors/regulatory-news/) contains no asset disposal announcement in the window [d0d36a].

2. The complete RNS announcement list for SSE plc via Investegate (https://www.investegate.co.uk/company/SSE) shows every SSE RNS in the window: 28 May 2026 Preliminary Results; 01 Jun 2026 Admission to Trading and Total Voting Rights; 02 Jun 2026 Issue of Hybrid Capital Securities; 05/09/17 Jun 2026 Director/PDMR Shareholding; 09 Jun 2026 Notification of Admission to Trading; 12 Jun 2026 Annual Financial Report; 30 Jun 2026 "SSEN Transmission welcomes 'Beyond 2030 Update'"; 01 Jul 2026 Total Voting Rights. None is an asset disposal, sale, farm-down, or transfer of an interest [e00727].

3. A check of the earlier part of the window (7–28 May 2026) confirmed there were no intervening RNS announcements before the 28 May Preliminary Results [df8586].

4. SSE's Preliminary Results (RNS, 28 May 2026) reported no definitive agreement for a £200m+ asset disposal [a90547].

5. SSE's official newsroom (https://www.sse.com/news-and-views/) for the window contained only non-qualifying items: a 13 May 2026 SSE Airtricity/Activ8 solar funding initiative (a partnership launch, in euros, not a disposal), the 12 June Annual Report, a £150M training facility plan, a Sustainability Report, grid investment economic analysis, an Ofgem LDES statement, "Construction begins at Platin Power Station", and an Ireland EU Council Presidency note — none an asset disposal of £200m+ [5a073c].

Because no qualifying announcement (single transaction, actual ownership transfer, ≥£200m, from SSE's official RNS or newsroom, dated 12 May–1 July 2026) exists, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-138. `4bedb47c-2130-5cd4-9491-414fb3bfcbc7`

- Present date: `2026-05-01 14:28:52.545046`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Apple ship RCS end-to-end encryption as a non-beta feature in the general public release of iOS 26.5?

**Resolution criteria**

This question resolves **Yes** if, in the general public release of iOS 26.5 (not a beta, developer preview, or Release Candidate), released on or after April 30, 2026 (UTC), the RCS end-to-end encryption feature is available to users **without** a "Beta," "Preview," or equivalent experimental designation in the user interface (specifically in Settings > Messages > RCS Messaging).

This question resolves **No** if any of the following are true:
1. The RCS E2EE feature is removed entirely from the public release of iOS 26.5.
2. The feature is present but retains a "Beta," "Preview," or equivalent experimental label.
3. iOS 26.5 is not released to the general public by June 1, 2026, 23:59 UTC.

**Definitions:**
- "Shipping feature" means the feature is present in the general public release and is not labeled as "Beta," "Preview," or any equivalent experimental designation in the iOS Settings UI.
- "Beta feature" means the feature is present but carries a "Beta," "Preview," or equivalent experimental label in the iOS Settings UI.
- "General public release" means the version of iOS 26.5 made available to all users via Settings > General > Software Update, excluding any builds distributed solely through the Apple Beta Software Program or Apple Developer Program.

**Resolution source:** Apple's official release notes at https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-26_5-release-notes and/or the Apple Releases page at https://developer.apple.com/news/releases/, supplemented by credible tech reporting from 9to5Mac (https://9to5mac.com), MacRumors, or The Verge confirming the presence and labeling of the feature in the shipping build.

All dates and times in these criteria are in UTC.

**Pre-cutoff background**

Rich Communication Services (RCS) is a messaging protocol intended to replace SMS/MMS with richer features (see https://en.wikipedia.org/wiki/Rich_Communication_Services). End-to-end encryption (E2EE) is a method of communication where only the sender and recipient can read the messages, preventing intermediaries from accessing the content (see https://en.wikipedia.org/wiki/End-to-end_encryption).

Apple has been working on adding E2EE to RCS messaging on the iPhone. The feature was tested during the iOS 26.4 beta cycle but was ultimately pulled and did not ship in the final public release of iOS 26.4 [iOS 26.5: New features, release date, more - 9to5Mac](https://9to5mac.com/2026/04/28/ios-26-5-new-iphone-features/). The feature returned in the iOS 26.5 beta, where it is enabled by default and accessible via a toggle in Settings > Messages > RCS Messaging. As of iOS 26.5 beta 4 (released April 27, 2026), the toggle is explicitly labeled "End-to-End Encryption (Beta)" [iOS 26.5: New features, release date, more - 9to5Mac](https://9to5mac.com/2026/04/28/ios-26-5-new-iphone-features/).

iOS 26.5 is currently on its fourth developer/public beta. Apple has confirmed that iOS 26.5 will be released to the general public sometime in May 2026 [iOS 26.5: New features, release date, more - 9to5Mac](https://9to5mac.com/2026/04/28/ios-26-5-new-iphone-features/). Based on historical patterns (iOS 18.5 released May 12, iOS 17.5 released May 13), the public release is most likely around May 11–12, 2026.

The key uncertainty is whether Apple will graduate the RCS E2EE feature from its current "Beta" designation to a fully shipping feature, given that a similar attempt was abandoned during the iOS 26.4 cycle.

**Exact later resolution packet**

The question resolves **NO (0)**.

**Antecedent / timing check:** iOS 26.5 was released to the general public on May 11, 2026, which is within the required window (on or after April 30, 2026 and before June 1, 2026 23:59 UTC). Apple's official Newsroom confirms the public rollout date of May 11, 2026 [1ea3cc], and 9to5Mac confirms the public release earlier that month [7cb94f]. So condition #3 (failure to release by June 1) is NOT met.

**Feature presence and labeling:** The RCS end-to-end encryption feature IS present in the public release of iOS 26.5 (so it was not removed — condition #1 not met). However, it is explicitly labeled and described as "beta." Apple's official Newsroom article is titled "End-to-end encrypted RCS messaging begins rolling out today in beta" and states: "Starting today, end-to-end encrypted RCS messaging begins rolling out in beta for iPhone users running iOS 26.5..." [1ea3cc]. Apple's own iOS 26.5 release notes read "End-to-end encrypted RCS messaging (beta) in Messages is available with supported carriers and will roll out over time" (widely reported by PCMag, Engadget, CNET). 9to5Mac, in its May 27, 2026 article on checking the feature in Settings > Messages > RCS Messaging, states: "RCS end-to-end encryption is currently available in beta, and it's on by default in iOS 26.5" [7cb94f].

**Conclusion:** Because the feature is present in the general public release but retains a "Beta" designation, resolution criterion #2 ("The feature is present but retains a 'Beta,' 'Preview,' or equivalent experimental label") is satisfied. The question therefore resolves NO.

Sources:
- Apple Newsroom: https://www.apple.com/newsroom/2026/05/end-to-end-encrypted-rcs-messaging-begins-rolling-out-today-in-beta/ [1ea3cc]
- 9to5Mac (Settings UI verification): https://9to5mac.com/2026/05/27/ios-26-5-gave-messages-app-encrypted-rcs-heres-how-to-check-its-working/ [7cb94f]

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-139. `fedfc029-ad9c-570b-af0b-f8b626114644`

- Present date: `2026-04-30 14:45:47.262722`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-05-31 00:00:00`

**Question**

Will the National Committee for the Administration of Gaza (NCAG) be physically operating from within the Gaza Strip as of May 31, 2026?

**Resolution criteria**

This question resolves YES if, on or after April 30, 2026, and no later than 23:59 UTC on May 31, 2026, there is credible reporting from at least one major international news organization (e.g., Reuters: https://www.reuters.com, Associated Press: https://apnews.com, Agence France-Presse, Al Jazeera: https://www.aljazeera.com, or BBC News: https://www.bbc.com/news) or official confirmation from the NCAG's own website (https://www.ncag.ps/en/) confirming BOTH of the following:

1. **Operating:** The NCAG is actively performing administrative functions — defined as issuing administrative directives, managing public services (e.g., health, sanitation, utilities), coordinating aid distribution, or overseeing municipal operations within Gaza.

2. **Physically present in Gaza:** The NCAG maintains at least one staffed office or operational headquarters located within the geographic boundaries of the Gaza Strip (as defined by https://en.wikipedia.org/wiki/Gaza_Strip), with at least one senior NCAG official (committee member or chief commissioner) physically based there.

The question resolves NO if:
- The NCAG is operating exclusively from outside the Gaza Strip (e.g., from Cairo, Ramallah, or elsewhere);
- The NCAG has been dissolved or is not performing any of the administrative functions listed above;
- No credible reporting confirms both conditions above by 23:59 UTC on May 31, 2026.

**Pre-cutoff background**

The National Committee for the Administration of Gaza (NCAG) is a transitional, technocratic, apolitical Palestinian committee established in January 2026 as part of Phase 2 of the U.S.-backed Gaza peace plan (https://en.wikipedia.org/wiki/National_Committee_for_the_Administration_of_Gaza). It is chaired by Ali Shaath and composed of approximately 15 Palestinian technocrats, tasked with managing day-to-day public services, municipal operations, and reconstruction in the Gaza Strip [https://en.wikipedia.org/wiki/Gaza_peace_plan](https://en.wikipedia.org/wiki/Gaza_peace_plan). The NCAG operates under the oversight of an international "Board of Peace" chaired by U.S. President Donald Trump.

Phase 2 of the Gaza peace plan was announced as commencing on January 14, 2026 [https://en.wikipedia.org/wiki/Gaza_peace_plan](https://en.wikipedia.org/wiki/Gaza_peace_plan). However, the NCAG's inaugural meeting took place in Cairo, Egypt on January 15-16, 2026 — not inside Gaza [National Committee for the Administration of Gaza](https://ecfr.eu/special/mapping_palestinian_politics/administrative-committee-gaza/). As of early 2026, the NCAG has faced significant obstacles to establishing a physical presence inside Gaza. The Global Observatory noted in February 2026 that "the first obstacle is physical" — referring to the difficulty of operating on the ground given the security situation. The NCAG began recruiting police in February 2026 (per Reuters), but reporting from Le Monde in April 2026 described Phase 2 as being "in limbo." As of April 30, 2026, it remains uncertain whether the NCAG has moved its operations from Cairo into the Gaza Strip or established a functioning headquarters there.

**Exact later resolution packet**

NO. The YES criteria required a source dated from April 30 through May 31, 2026 confirming BOTH (1) active NCAG administrative functions inside Gaza and (2) a staffed NCAG office/headquarters inside the Gaza Strip with at least one senior NCAG official physically based there. I found no such confirmation. The Reuters article I checked was dated May 1, 2026, but it did not mention NCAG at all and therefore did not confirm either required condition; it instead concerned the U.S.-led CMCC/ISF and a stalled Gaza plan [Exclusive: US to close its flagship Gaza mission as Trump plan stalls ...](https://www.reuters.com/world/middle-east/us-close-its-flagship-gaza-mission-trump-plan-stalls-sources-say-2026-05-01/). The official NCAG homepage/news content I checked was dated as recently as May 26, 2026, but it only described NCAG’s mission/leadership and did not confirm any Gaza-based staffed office, headquarters, or senior official physically based in Gaza [National Committee for the Administration of Gaza (NCAG)](https://www.ncag.ps/en/). The official NCAG May 5 statement likewise used mandate/mission language about relief, services, recovery, and reconstruction, but did not confirm that NCAG was carrying out administrative functions on the ground in Gaza or that any senior NCAG official was physically based in a Gaza office/headquarters [Statement from NCAG](https://www.ncag.ps/en/news/ncag-statement-may5/). Under the resolution criteria, absence of credible reporting confirming both conditions by 23:59 UTC on May 31, 2026 requires a NO resolution.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-140. `2c37e841-7627-5ea5-899e-556f11d6dadb`

- Present date: `2026-05-14 06:58:31.684773`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will a blockade or forced shutdown be reported at a major Libyan oil terminal or oil field between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after May 12, 2026 (00:00 UTC) and before July 1, 2026 (23:59 UTC), a credible source reports that a blockade (https://en.wikipedia.org/wiki/Blockade) or forced shutdown has occurred at one or more of the following major Libyan oil facilities: Es Sider, Ras Lanuf, Zueitina, Hariga, Sharara, or El Feel.

Definitions:
- "Blockade" or "forced shutdown": A deliberate cessation or significant disruption of oil production or export operations lasting at least 24 consecutive hours, caused by political, military, tribal, or protest-related actions. This includes any event where the National Oil Corporation (NOC) declares force majeure (https://en.wikipedia.org/wiki/Force_majeure) on exports from the affected facility due to such actions.
- Shutdowns caused solely by technical failures, routine maintenance, or adverse weather conditions are EXCLUDED and do not count toward resolution.
- The disruption must be confirmed by at least one of the following sources: (1) an official statement on the National Oil Corporation of Libya's website (https://noc.ly/), or (2) reporting by at least two of the following international news agencies: Reuters (https://www.reuters.com/), Bloomberg (https://www.bloomberg.com/), Associated Press (https://apnews.com/), or AFP (https://www.afp.com/).

If no qualifying event is reported by July 1, 2026 (23:59 UTC), the question resolves NO.

**Pre-cutoff background**

Libya's economy depends on oil for over 95% of government revenue. As of early May 2026, Libya's oil production stands at approximately 1.43 million barrels per day (bpd), its highest level in over a decade [https://middle-east-online.com/en/libya-agrees-unified-budget-implementation-doubts-remain](https://middle-east-online.com/en/libya-agrees-unified-budget-implementation-doubts-remain). On April 11, 2026, Libya's rival political institutions—the eastern-based House of Representatives and the western-based High Council of State—approved a unified state budget of 190 billion Libyan dinars (~$29.95 billion), the first unified budget in over 13 years [https://middle-east-online.com/en/libya-agrees-unified-budget-implementation-doubts-remain](https://middle-east-online.com/en/libya-agrees-unified-budget-implementation-doubts-remain). However, analysts note that implementation risks remain high due to the country's fractured governance and the long history of eastern factions using oil blockades as political leverage [https://middle-east-online.com/en/libya-agrees-unified-budget-implementation-doubts-remain](https://middle-east-online.com/en/libya-agrees-unified-budget-implementation-doubts-remain).

Major oil blockades have occurred multiple times in recent years (2020, 2022, 2024), typically initiated by eastern-aligned armed groups or the Libyan National Army (LNA) under Khalifa Haftar. These blockades have historically targeted key export terminals and oil fields, sometimes reducing national output by hundreds of thousands of barrels per day. The unified budget agreement creates new incentives against blockades, but the underlying political divisions persist, and the UN Security Council has noted the political process remains stalled.

For this question, the following are defined as "major Libyan oil terminals or oil fields": Es Sider (capacity ~300,000 bpd), Ras Lanuf (~220,000 bpd), Zueitina (~70,000 bpd), Hariga (~110,000 bpd), Sharara oil field (~300,000 bpd), and El Feel oil field (~70,000 bpd). These six facilities collectively account for a large majority of Libya's oil production and export capacity.

**Exact later resolution packet**

RESOLUTION: NO (0).

The question resolves YES only if, between May 12, 2026 (00:00 UTC) and July 1, 2026 (23:59 UTC), a credible source reported a blockade or forced shutdown (≥24 consecutive hours or NOC force majeure, caused by political/military/tribal/protest action) at one of six named facilities — Es Sider, Ras Lanuf, Zueitina, Hariga, Sharara, or El Feel — confirmed by NOC (noc.ly) or ≥2 of Reuters/Bloomberg/AP/AFP. No such qualifying event occurred in the window.

Evidence AGAINST any qualifying disruption:
- The NOC's own website (noc.ly) showed NO force majeure, blockade, or forced-shutdown announcement for any of the six facilities in the window; its late-May–June 2026 news items concern operational improvements (new gas compressors on Sabratha platform June 29, energy-investment discussions June 28, grid-stability gas supply June 22) [2be3f2].
- Libya's oil output hit a 13-year high of ~1.5 million bpd on June 21, 2026 — the highest since 2013 — per NOC/AGBI reporting; this record is incompatible with the ~300,000 bpd Sharara field or major terminals being blockaded in the window [e830db]. Egypt Oil & Gas' July 1, 2026 coverage likewise reports output "nearing 1.5 mmbbl/d, highest since 2013," with no blockade or force majeure at the named facilities [ed19b2].
- An Amani Africa briefing dated June 8, 2026 lists only one oil-related disruption in the period: the "temporary shutdown of Libya's largest oil refinery in Zawiya" following armed clashes on 8 May 2026. That event is (a) before the May 12 window start and (b) Zawiya is NOT one of the six listed facilities, so it cannot count [5ba518].

Every article whose headline suggested a shutdown at the six facilities turned out, on inspection, to fall OUTSIDE the window (search-snippet "dates" like "June 2026"/"25 June 2026" were crawl-date/sidebar artifacts, not publication dates):
- Libya Observer "Protesters shut down Libya's Sharara oilfield over unanswered demands" = published March 1, 2024 [7dc2c3].
- Libya Update "Protests Continue at Libya's El Sharara Oilfield" = published January 6, 2024 [a5d858].
- Pipeline Journal "Libya Oil Exports Disrupted by Pipeline Fire" = published August 14, 2024 (Es Sider pipeline fire/Sharara protests) [48e815].
- Asharq Al-Awsat "Protests in Libya Disrupt Oil Loadings at Two Major Ports" (Es Sider & Ras Lanuf) = published January 28, 2025 [3b9e70].
- Asharq Al-Awsat "Libya's Eastern Government Says All Oilfields to Close" = published August 26, 2024 [e35561].
- Reuters coverage of Sharara/El Feel disruptions (explosion/pipeline fire March 17–18, El Feel shutdown, projectiles March 24) all resolved with full resumption by March 29–30, 2026 (Reuters "Libya fully resumes output at Sharara and El Feel oil fields," 2026-03-30) — before the window.

Because no blockade or forced shutdown at any of the six specified facilities was reported within May 12–July 1, 2026 by either the NOC or two of the four named wire agencies — and independent evidence shows record production and normal operations during the window — the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-141. `9a1d9059-cdfa-570e-80c7-cff7372b3e01`

- Present date: `2026-05-02 23:48:49.557356`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Mozilla Firefox enable JPEG XL decoding support by default in a stable desktop release by June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, by 23:59 UTC on June 1, 2026, Mozilla releases a stable-channel version of Firefox for desktop (i.e., not Nightly, Beta, or Developer Edition) that includes JPEG XL image decoding support enabled by default on at least one major desktop operating system (Windows, macOS, or Linux).

"Enabled by default" means that a user installing the standard stable version of Firefox can view JPEG XL images without needing to modify any settings in `about:config`, Firefox Labs, or any other internal configuration flags.

The feature must be available to the general public and not limited to a staged rollout or A/B test that has not reached 100% of stable-channel users by the deadline.

This question resolves as **No** if no such stable release exists by the deadline, or if JPEG XL support remains behind a flag (e.g., `image.jxl.enabled` in `about:config`).

**Primary resolution source:** The official Mozilla Firefox Release Notes at https://www.mozilla.org/en-US/firefox/releases/. If the release notes for a stable version shipped by the deadline list JPEG XL support as a new feature (without requiring manual flag changes), the question resolves Yes. Secondary confirmation may be obtained from the Mozilla Blog (https://blog.mozilla.org/) or Can I Use (https://caniuse.com/jpegxl).

**Pre-cutoff background**

JPEG XL (JXL) is a modern image format offering better compression than JPEG, PNG, and WebP. Safari has supported JPEG XL since Safari 17, and Google Chrome 145 shipped with native JPEG XL support in February 2026 using a Rust-based decoder (jxl-rs).

Mozilla Firefox has been the major browser holdout. Mozilla had indicated that adoption was contingent on the availability of a Rust-based decoder. While Firefox 149 (released March 2026) included the jxl-rs Rust-based JPEG-XL decoder in its codebase, the feature was restricted to the Nightly channel and did not ship in the stable Firefox 149 release [Firefox 149 Now Available With XDG Portal File Picker - Phoronix](https://www.phoronix.com/news/Mozilla-Firefox-149). As of May 1, 2026, JPEG XL support in Firefox remains behind a flag (`image.jxl.enabled` in `about:config`) and is not available to general users of the stable release channel. Firefox's standard release cycle is approximately every four weeks, meaning Firefox 150 and potentially Firefox 151 could ship before June 1, 2026.

The competitive pressure from both Chrome and Safari supporting JPEG XL natively, combined with JPEG XL being one of the top developer-requested features in Interop 2026, creates significant momentum for Mozilla to enable the feature. However, Mozilla has not publicly committed to a timeline for enabling JPEG XL by default in a stable release.

**Exact later resolution packet**

The question resolves NO. By the deadline of 23:59 UTC on June 1, 2026, the most recent stable-channel desktop release of Firefox was Firefox 151.0 (released May 19, 2026).

- The official Mozilla Firefox 151.0 Release Notes do not list JPEG XL / JXL support as a new feature anywhere in their New, Fixed, Changed, Enterprise, Developer, or Web Platform sections. JPEG XL decoding was therefore NOT enabled by default in the stable release [f9dd28]. URL: https://www.firefox.com/en-US/firefox/151.0/releasenotes/

- Phoronix's coverage of the Firefox 151 release (published May 18, 2026) explicitly confirms: "While there was talk of Firefox 151 shipping a native JPEG-XL image decoder, that feature was punted to Firefox 152 beta." This means JPEG XL was not in the stable 151 release [de10a6]. URL: https://www.phoronix.com/news/Firefox-151

- Firefox 152 (the next stable release, after a ~4-week cycle from May 19) would only ship in mid-to-late June 2026, after the June 1 deadline. Even then, the feature was only at the "152 beta" stage, not stable.

Since no stable-channel Firefox desktop release shipped JPEG XL decoding enabled by default (without requiring about:config/flag changes) on or before June 1, 2026, the question resolves NO.</parameter>
</invoke>

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-142. `2ce08cfc-b1c6-5da5-9903-56d71bdd61cd`

- Present date: `2026-04-30 11:49:29.772183`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the reconciliation bill passed by the U.S. House of Representatives include a provision extending the ban on Medicaid payments to Planned Parenthood?

**Resolution criteria**

This question resolves **Yes** if a reconciliation bill passed by the U.S. House of Representatives on or after April 29, 2026, and on or before June 1, 2026, contains a provision that explicitly prohibits, restricts, or extends the prohibition on federal Medicaid payments to [Planned Parenthood Federation of America](https://en.wikipedia.org/wiki/Planned_Parenthood) or its affiliates or clinics.

A "provision" is defined as any section, subsection, clause, or amendment within the enrolled or passed text of the bill that directly addresses the prohibition or restriction of Medicaid reimbursements or payments to Planned Parenthood or its affiliated entities. Merely referencing Planned Parenthood in a findings section or sense-of-Congress resolution does not count; the provision must have operative legal effect on Medicaid funding.

"Ban on Medicaid payments to Planned Parenthood" refers to the prohibition on federal Medicaid reimbursement to Planned Parenthood Federation of America, Inc., its affiliates, or its clinics, as described in [Section 50301 of H.R.1 (119th Congress)](https://www.congress.gov/bill/119th-congress/house-bill/1) and similar legislative mechanisms. This includes any extension, renewal, or making permanent of such a prohibition.

This question resolves **No** if:
- The House passes a reconciliation bill without such a provision, OR
- No reconciliation bill passes the U.S. House of Representatives by June 1, 2026.

**Resolution source:** The text of the bill as published on [Congress.gov](https://www.congress.gov/bill/119th-congress/house-bill/1) and any successor reconciliation bill tracker on Congress.gov, supplemented by credible reporting from outlets such as [Politico](https://www.politico.com), [Reuters](https://www.reuters.com), or [AP News](https://apnews.com).

**Pre-cutoff background**

As of late April 2026, the U.S. Congress is working on a second reconciliation bill focused primarily on immigration enforcement funding. On April 23, 2026, Politico reported that GOP leadership wants a narrow, "anorexic" party-line bill to ensure passage, but rank-and-file Republicans are lobbying to extend the block on Medicaid payments to family planning clinics, including Planned Parenthood ['Anorexic' reconciliation bill could mean Planned ...](https://www.politico.com/news/2026/04/23/anorexic-reconciliation-bill-could-mean-planned-parenthood-gets-re-funded-00889576). The current ban on Medicaid payments to Planned Parenthood, established in the earlier "One Big Beautiful Bill Act" (H.R.1, 119th Congress), is set to lapse in the summer of 2026. The Senate passed its budget resolution 50-48 on April 23, 2026, and rejected an amendment (S.Amdt.4794) that would have included the Planned Parenthood defunding extension ['Anorexic' reconciliation bill could mean Planned ...](https://www.politico.com/news/2026/04/23/anorexic-reconciliation-bill-could-mean-planned-parenthood-gets-re-funded-00889576). The bill now moves to the House, where the tension between leadership's desire for a narrow bill and pressure from the pro-life caucus creates genuine uncertainty about whether defunding provisions will be added. The first reconciliation bill (H.R.1) already included a temporary ban on Medicaid payments to Planned Parenthood; the question is whether this second, immigration-focused reconciliation bill will extend that ban.

**Exact later resolution packet**

The question resolves NO because no reconciliation bill passed the U.S. House of Representatives within the required window of April 29, 2026 through June 1, 2026.

Timeline of events:
- The Senate adopted its budget resolution 50-48 on April 23, 2026, and the House adopted the Senate-passed budget resolution on April 29-30, 2026 (per Roll Call and AHA reporting). This was only a budget resolution, NOT the reconciliation bill itself.
- Senate Republicans released a ~$72 billion reconciliation bill on May 5, 2026, to fund ICE/CBP, and a Senate committee passed it in mid-May.
- However, both the House and Senate left Washington for the Memorial Day recess (departing around May 22, 2026) WITHOUT voting on the "Reconciliation 2.0" legislative package [08baec][60a53b]. The NLIHC reported that "Members of Congress Leave D.C. for Memorial Day Recess Without Voting on Reconciliation 2.0" [08baec].
- CBS News (May 21, 2026) confirmed the House and Senate left for recess without voting, that Congress was not scheduled to return until June 1, 2026, and that lawmakers would "all but certainly miss" President Trump's June 1 deadline to get the bill to his desk [60a53b].

The resolution criteria explicitly state the question resolves NO if "No reconciliation bill passes the U.S. House of Representatives by June 1, 2026." Since no reconciliation bill was passed by the House within the April 29 – June 1, 2026 window (the House had only passed the budget resolution, not the actual reconciliation bill, and then left for recess), the question resolves NO regardless of whether the eventual bill would have contained a Planned Parenthood Medicaid defunding provision.

Sources:
- https://nlihc.org/resource/members-congress-leave-dc-memorial-day-recess-without-voting-reconciliation-20-legislative [08baec]
- https://www.cbsnews.com/news/senate-reconciliation-bill-white-house-ballroom-doj-anti-weaponization-fund/ [60a53b]
- https://www.politico.com/live-updates/2026/05/21/congress/house-ponders-reconciliation-delay-00931986 (House GOP leaders considered delaying the vote past Memorial Day, blowing the deadline)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-143. `1fc77f69-a7f6-5b47-8fa0-f357714747fa`

- Present date: `2026-05-03 10:35:19.555262`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the United States and Iran announce a permanent ceasefire or formal peace agreement in the 2026 Iran war by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 2, 2026 (00:00 UTC) and before June 2, 2026 (00:00 UTC), the United States and Iran jointly or separately announce a **permanent ceasefire, formal peace agreement, or comprehensive cessation of hostilities** in the 2026 Iran war.

Key definitions:
- **"Permanent ceasefire or formal peace agreement"**: A publicly announced agreement — distinct from the existing temporary/extended truce — that is described by both parties as a permanent or indefinite end to hostilities, or as a formal peace deal. This does NOT include further extensions of the existing temporary ceasefire, nor unilateral declarations by only one side.
- **"Ceasefire"** (https://en.wikipedia.org/wiki/Ceasefire): A temporary or permanent stoppage of active hostilities agreed upon by the parties to a conflict.
- **"Cessation of hostilities"** (https://dictionary.cambridge.org/dictionary/english/cessation): The stopping or ending of hostile military actions.
- **Parties involved**: The United States of America and the Islamic Republic of Iran, as the principal belligerents in the 2026 Iran war (https://en.wikipedia.org/wiki/2026_Iran_war). Israel's separate participation is not required for resolution, though an agreement that includes Israel would also qualify.

**Resolution source**: Official statements from the U.S. White House (https://www.whitehouse.gov/), U.S. Department of State (https://www.state.gov/), or Iran's Ministry of Foreign Affairs, OR credible reporting from at least two of the following: Reuters (https://www.reuters.com/), Associated Press (https://apnews.com/), BBC (https://www.bbc.com/), or The New York Times (https://www.nytimes.com/).

The question resolves **No** if no such permanent agreement is announced by the deadline.

**Pre-cutoff background**

On February 28, 2026, the United States and Israel launched military strikes against Iran, initiating the 2026 Iran war (https://en.wikipedia.org/wiki/2026_Iran_war). The conflict began after failed negotiations over Iran's nuclear program and amid Iran's crackdown on domestic protests [2026 Iran war](https://en.wikipedia.org/wiki/2026_Iran_war).

A temporary two-week ceasefire was agreed on April 8, 2026, mediated by Pakistan [2026 Iran war ceasefire - Wikipedia](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire). The Islamabad Talks, intended to produce a lasting agreement, collapsed, after which the U.S. imposed a naval blockade of Iranian ports on April 13, 2026 [2026 Iran war ceasefire - Wikipedia](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire). On April 21, 2026, President Trump unilaterally extended the ceasefire but gave Iran a 3-to-5 day window to engage in negotiations before the U.S. would resume attacks [2026 Iran war ceasefire - Wikipedia](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire).

As of May 1, 2026, the situation is characterized by a fragile, indefinitely extended temporary ceasefire alongside a "dual blockade" — the U.S. Navy blockading Iranian ports and Iran restricting traffic through the Strait of Hormuz [2026 Iran war](https://en.wikipedia.org/wiki/2026_Iran_war). Iran has submitted new proposals for talks, but President Trump has said he is "not satisfied." Formal peace negotiations have not resumed. The temporary ceasefire remains in effect but is under constant threat of collapse, and no permanent agreement has been reached [2026 Iran war](https://en.wikipedia.org/wiki/2026_Iran_war).

**Exact later resolution packet**

The question resolves NO. It asked whether, between May 2, 2026 (00:00 UTC) and June 2, 2026 (00:00 UTC), the U.S. and Iran would announce a PERMANENT ceasefire, formal peace agreement, or comprehensive cessation of hostilities — explicitly excluding further extensions of the existing temporary truce and unilateral declarations.

What actually happened in May 2026:
- Active hostilities continued throughout the month rather than ceasing. Per the Wikipedia "2026 Iran war ceasefire" article, the U.S. carried out "self-defense" strikes against Iranian military facilities on May 7, 2026 (after attacks on the USS Truxtun, USS Rafael Peralta, and USS Mason in the Strait of Hormuz), and again on May 25, 2026 against missile launch sites and boats in Bandar Abbas. Iran responded with its own attacks on U.S. vessels. This demonstrates the conflict remained active and no comprehensive cessation of hostilities was reached [43d069].
- The most advanced diplomatic development was a tentative agreement reached around May 28, 2026, which Reuters explicitly characterized as a 60-DAY EXTENSION of the existing temporary truce (a memorandum of understanding to extend the ceasefire and launch new nuclear talks), not a permanent or formal peace deal. Moreover, this agreement was still PENDING President Trump's approval and had not been finalized according to Iranian state media as of the reporting date [356c2e].

Because (a) the only relevant agreement was a temporary 60-day extension — exactly the type of extension the resolution criteria explicitly exclude — and (b) it had not even been finalized/jointly announced as a permanent deal before the June 2, 2026 deadline, and (c) active military strikes between the two parties continued through late May, no permanent ceasefire, formal peace agreement, or comprehensive cessation of hostilities was announced within the resolution window. The question therefore resolves NO.

Sources:
- Reuters, "Iran, US reach deal to extend ceasefire, pending Trump's approval" (May 28, 2026): https://www.reuters.com/world/middle-east/iran-us-trade-air-strikes-after-trump-dismisses-report-hormuz-deal-2026-05-28/ [356c2e]
- Wikipedia, "2026 Iran war ceasefire": https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire [43d069]

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-144. `e06c05ad-dfdf-52e7-9d25-c462ebb8ab24`

- Present date: `2026-05-07 16:43:29.054696`
- Source cutoff boundary: `2026-05-08` (encodes end of UTC day `2026-05-07`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will SpaceX successfully catch the Super Heavy booster during Starship Flight 12?

**Resolution criteria**

This question resolves **Yes** if, on or after May 6, 2026 and by August 1, 2026 (23:59 UTC), SpaceX's Starship Flight 12 mission results in a successful catch of the Super Heavy booster.

**Definitions:**
- **Starship Flight 12** refers to the 12th integrated flight test of the SpaceX Starship system, as identified on the [Wikipedia List of Starship launches](https://en.wikipedia.org/wiki/List_of_Starship_launches) and by SpaceX's official communications.
- A **successful catch** means the Super Heavy booster is gripped and secured by the launch tower's mechanical arms ("chopsticks") upon return, and remains secured through the end of the official SpaceX webcast of the mission. The booster does not need to be reused; it simply must be caught and held.
- The catch attempt must occur at the launch site (OLP-1 or OLP-2 at Starbase, Boca Chica, Texas).

This question resolves **No** if any of the following occur:
- Flight 12 launches but the booster is not caught (e.g., it is diverted to the ocean, crashes, or the catch is not attempted).
- Flight 12 does not launch by August 1, 2026 (23:59 UTC).
- The booster is caught but falls or is released before the end of the official SpaceX webcast.

**Resolution source:** The official [SpaceX X/Twitter account](https://x.com/SpaceX), the [SpaceX website mission page](https://www.spacex.com/launches/), or the SpaceX webcast. In the absence of official SpaceX communications, credible aerospace reporting from sources such as [NASA Spaceflight](https://www.nasaspaceflight.com/), Reuters, or AP may be used.

**Pre-cutoff background**

SpaceX's [Starship](https://en.wikipedia.org/wiki/SpaceX_Starship) is a fully reusable super heavy-lift launch system consisting of a [Super Heavy booster](https://en.wikipedia.org/wiki/SpaceX_Super_Heavy) first stage and a Starship upper stage. A key reusability milestone is catching the returning Super Heavy booster mid-air using mechanical arms (nicknamed "chopsticks") mounted on the launch tower.

As of early May 2026, SpaceX has conducted 11 Starship flights. Booster catch attempts have been successful on Flights 5, 7, and 8, all launched from Orbital Launch Pad 1 (OLP-1) at Starbase, Texas [https://en.wikipedia.org/wiki/List_of_Starship_launches](https://en.wikipedia.org/wiki/List_of_Starship_launches). Other flights either did not attempt a catch or the booster was intentionally diverted to the ocean.

Starship Flight 12 is scheduled for approximately May 12, 2026 [https://en.wikipedia.org/wiki/List_of_Starship_launches](https://en.wikipedia.org/wiki/List_of_Starship_launches). It represents two major firsts simultaneously: it is the inaugural flight of the **Block 3** vehicle—a significant hardware upgrade featuring structural and avionics changes—and the first launch from the newly constructed **OLP-2** (Orbital Launch Pad 2) at Starbase [https://en.wikipedia.org/wiki/List_of_Starship_launches](https://en.wikipedia.org/wiki/List_of_Starship_launches). The combination of untested hardware and a new launch pad introduces substantial uncertainty beyond what was present in prior catch attempts from OLP-1 with earlier vehicle blocks.

Previous successful catches (Flights 5, 7, 8) established the mechanical feasibility of booster catch, but the transition to Block 3 hardware and OLP-2 infrastructure means Flight 12 is not simply a repeat of a proven operation. Forecasters should weigh the demonstrated catch capability against the risks inherent in debuting a new vehicle variant on a new pad.

**Exact later resolution packet**

Starship Flight 12 launched on May 22, 2026, at 5:30 p.m. CT from Starbase, Texas (Orbital Launch Pad 2 / OLP-2) — this is within the question's resolution window of May 6, 2026 through August 1, 2026 (23:59 UTC), and at the required launch site [Starship's Twelfth Flight Test](https://www.spacex.com/launches/starship-flight-12) [Starship flight test 12 - Wikipedia](https://en.wikipedia.org/wiki/Starship_flight_test_12).

The official SpaceX mission page (https://www.spacex.com/launches/starship-flight-12) reports that after stage separation, the Super Heavy booster attempted to reignite its engines for the landing burn but experienced a hard splashdown in the Gulf — it was NOT caught by the launch tower's mechanical arms ("chopsticks") [Starship's Twelfth Flight Test](https://www.spacex.com/launches/starship-flight-12). Wikipedia's "Starship flight test 12" article corroborates this: during the landing burn only one engine ignited and the booster crashed into the Gulf at ~1,450 km/h rather than being caught [Starship flight test 12 - Wikipedia](https://en.wikipedia.org/wiki/Starship_flight_test_12).

Because the booster was never gripped/secured by the chopsticks (it was destroyed in a hard splashdown), the question's condition for a "successful catch" was not met. Per the resolution criteria, the question resolves NO when "Flight 12 launches but the booster is not caught (e.g., it is diverted to the ocean, crashes...)." The launch did occur (so no annulment applies), and the catch did not succeed, so the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-145. `2b593d2d-fa51-5715-ab5e-a1a1e52008bc`

- Present date: `2026-05-14 01:42:05.722038`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-23T00:00:00`

**Question**

Will the GUP in Turin issue a rinvio a giudizio (committal to trial) for John Elkann at or before the June 22, 2026 hearing?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026, and no later than the conclusion of the June 22, 2026 hearing (CEST, UTC+2), the GUP (Giudice dell'Udienza Preliminare) in Turin issues a formal "rinvio a giudizio" against John Elkann. A "rinvio a giudizio" is defined as the GUP's decree (decreto che dispone il giudizio) ordering the defendant to stand trial before a tribunal, as described in Articles 429–432 of the Italian Code of Criminal Procedure (see: https://en.wikipedia.org/wiki/Italian_Code_of_Criminal_Procedure).

This question resolves **No** if any of the following occur:
- The GUP issues a "sentenza di non luogo a procedere" (judgment of no case to answer/dismissal) for Elkann by the conclusion of the June 22, 2026 hearing.
- The June 22, 2026 hearing is adjourned or postponed without the GUP rendering a rinvio a giudizio decision, regardless of reason.
- No decision on rinvio a giudizio is reached by 23:59 CEST (UTC+2) on June 22, 2026.

Resolution will be determined by credible reporting from major news agencies and Italian newspapers, including but not limited to:
- ANSA (https://www.ansa.it/)
- Reuters (https://www.reuters.com/)
- Il Sole 24 Ore (https://www.ilsole24ore.com/)
- La Repubblica (https://www.repubblica.it/)
- Corriere della Sera (https://www.corriere.it/)

**Pre-cutoff background**

John Elkann, president of Stellantis and CEO of Exor, is the subject of a criminal investigation in Turin related to the inheritance of his grandmother, Marella Caracciolo. The investigation centers on whether Caracciolo falsely claimed tax residency in Switzerland to evade Italian taxes, with charges including truffa aggravata ai danni dello Stato (aggravated fraud against the state) and evasione fiscale fraudolenta (fraudulent tax evasion) [Eredità Agnelli, chiesto il rinvio a giudizio per John Elkann dopo il ...](https://www.ansa.it/sito/notizie/cronaca/2026/04/13/eredita-agnelli-chiesto-il-rinvio-a-giudizio-per-john-elkann-dopo-il-no-alla_ca468cb0-7216-4f0e-9270-a03e317599cc.html).

Key developments:
- In February 2026, a judge (GIP) rejected Elkann's request for "messa alla prova" (a probation/community service mechanism to avoid trial), and also rejected a plea bargain proposal from his co-accused accountant Gianluca Ferrero [Eredità Agnelli, chiesto il rinvio a giudizio per John Elkann dopo il ...](https://www.ansa.it/sito/notizie/cronaca/2026/04/13/eredita-agnelli-chiesto-il-rinvio-a-giudizio-per-john-elkann-dopo-il-no-alla_ca468cb0-7216-4f0e-9270-a03e317599cc.html).
- On April 13, 2026, the prosecution formally requested a "rinvio a giudizio" (indictment/committal to trial) for Elkann and Ferrero. The preliminary hearing (udienza preliminare) opened the same day but was immediately adjourned to June 22, 2026, to allow consolidation (riunificazione) with two other open case files, including one involving notary Remo Morone [Udienza preliminare Elkann, subito rinviata a giugno - Notizie - Ansa.it](https://www.ansa.it/piemonte/notizie/2026/04/13/udienza-preliminare-elkann-subito-rinviata-a-giugno_4324de76-fdd0-4eec-a738-6960ae1d791c.html).
- In 2025, Elkann paid €183 million to settle the underlying tax dispute, but this does not preclude criminal prosecution.

As of May 12, 2026, the case remains in the preliminary hearing phase. The GUP (Giudice dell'Udienza Preliminare) has not yet rendered a decision. The next hearing is scheduled for June 22, 2026, where the GUP will proceed with the consolidated case and decide whether to commit Elkann to trial or dismiss the case.

**Exact later resolution packet**

The question resolves NO (0).

Background/antecedent check: The question asks whether the GUP (Giudice dell'Udienza Preliminare) in Turin would issue a formal "rinvio a giudizio" (committal to trial / decreto che dispone il giudizio per Artt. 429–432 c.p.p.) against John Elkann on or after May 12, 2026 and no later than the conclusion of the June 22, 2026 hearing. This is a direct (non-conditional) question about events involving John Elkann in the Agnelli/Caracciolo inheritance criminal case in Turin.

Finding: The June 22, 2026 preliminary hearing (udienza preliminare) took place, but the GUP did NOT issue a rinvio a giudizio. Instead, the hearing was adjourned/postponed to September 11, 2026, with the statute of limitations (prescrizione) suspended. The postponement was to allow the defense to respond to Margherita Agnelli's request to become a civil party (costituzione di parte civile).

Evidence from mandated sources:
- ANSA (June 22, 2026): reports the hearing regarding Elkann, Ferrero and Morone was adjourned to September 11, 2026 to allow defense responses to Margherita Agnelli's civil-party request; no committal to trial was issued that day [c8f502].
- La Repubblica / Torino (June 22, 2026): explicitly states "Il gup non si è pronunciato oggi sul rinvio a giudizio" (the GUP did not rule on committal today) and "Disposto rinvio a settembre" (postponement to September ordered) [62d755].
- Additional corroboration from Il Fatto Quotidiano (June 22, 2026): the GUP Irene Giani adjourned the hearing to September 11, 2026, with prescrizione blocked; no rinvio a giudizio was decreed [d2985f].

Per the resolution criteria, the question resolves NO if "The June 22, 2026 hearing is adjourned or postponed without the GUP rendering a rinvio a giudizio decision, regardless of reason" and if "No decision on rinvio a giudizio is reached by 23:59 CEST (UTC+2) on June 22, 2026." Both conditions are satisfied: the hearing was postponed to September 11, 2026 with no committal decision reached. Therefore the resolution is NO (0).

Note on the term "richiesta di rinvio a giudizio": On April 13, 2026 the prosecution (Procura) merely *requested* a rinvio a giudizio. That is a prosecutorial request, not the GUP's decree ordering trial (Artt. 429–432 c.p.p.), and the question specifically requires the GUP's formal decree, which was not issued by June 22, 2026.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-146. `f1a5a777-1d09-5352-9b40-d2e259c70b63`

- Present date: `2026-05-01 19:28:59.558288`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the Peace for Ethiopia Coalition officially withdraw from the 2026 Ethiopian general election by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the Peace for Ethiopia Coalition — comprising the following eight parties: Agew National Council (Shengo), Gamo Democratic Party, Gambella Peoples' Freedom Movement, Kaffa Green Party, Agew for Justice and Democracy, Kaffa Peoples' Union, Tigray Democratic Cooperation, and Mocha Democratic Party — officially withdraws from the 2026 Ethiopian general election on or after April 30, 2026, and on or before June 1, 2026.

**"Official withdrawal"** is defined as any of the following:
- A formal notification or letter submitted to the National Election Board of Ethiopia (NEBE) declaring the coalition's withdrawal from the election; OR
- A public press release or statement by the coalition's authorized leadership confirming withdrawal from the election.

The withdrawal must be confirmed by credible reporting from sources such as [Addis Standard](https://addisstandard.com/), Reuters, AP, or the NEBE's official communications.

If the coalition withdraws only partially (i.e., some member parties withdraw while others remain), this resolves **No** — the withdrawal must be made on behalf of the coalition as a whole.

If no official withdrawal is confirmed by 23:59 UTC on June 1, 2026, this question resolves **No**.

**Pre-cutoff background**

On April 22, 2026, the Peace for Ethiopia Coalition — an alliance of eight opposition parties — issued an eight-day ultimatum to the Ethiopian government and the National Electoral Board of Ethiopia (NEBE), threatening to withdraw from the 7th general election unless 21 allegations of "widespread legal violations, intimidation, and administrative irregularities" were addressed [https://addisstandard.com/coalition-of-eight-political-parties-warns-it-will-withdraw-from-elections-unless-widespread-violations-against-members-are-immediately-addressed/](https://addisstandard.com/coalition-of-eight-political-parties-warns-it-will-withdraw-from-elections-unless-widespread-violations-against-members-are-immediately-addressed/). The coalition demanded a transparent investigation, guarantees of freedom of assembly, equal access to public infrastructure, and an end to voter registration manipulation [https://addisstandard.com/coalition-of-eight-political-parties-warns-it-will-withdraw-from-elections-unless-widespread-violations-against-members-are-immediately-addressed/](https://addisstandard.com/coalition-of-eight-political-parties-warns-it-will-withdraw-from-elections-unless-widespread-violations-against-members-are-immediately-addressed/).

The eight member parties are [https://addisstandard.com/coalition-of-eight-political-parties-warns-it-will-withdraw-from-elections-unless-widespread-violations-against-members-are-immediately-addressed/](https://addisstandard.com/coalition-of-eight-political-parties-warns-it-will-withdraw-from-elections-unless-widespread-violations-against-members-are-immediately-addressed/):
1. Agew National Council (Shengo)
2. Gamo Democratic Party
3. Gambella Peoples' Freedom Movement
4. Kaffa Green Party
5. Agew for Justice and Democracy
6. Kaffa Peoples' Union
7. Tigray Democratic Cooperation
8. Mocha Democratic Party

The eight-day ultimatum expired on or around April 30, 2026. As of April 30, 2026, it is unclear whether the coalition has followed through on its threat or reached a negotiated resolution with the government and NEBE. Opposition boycott threats are common in Ethiopian elections but are not always carried out, making the outcome genuinely uncertain.

**Exact later resolution packet**

The question resolves NO. The Peace for Ethiopia Coalition (the alliance of eight opposition parties: Agew National Council (Shengo), Gamo Democratic Party, Gambella Peoples' Freedom Movement, Kaffa Green Party, Agew for Justice and Democracy, Kaffa Peoples' Union, Tigray Democratic Cooperation, and Mocha Democratic Party) issued an eight-day withdrawal ultimatum on April 22, 2026, but did NOT follow through with an official withdrawal between April 30 and June 1, 2026.

Key evidence:
- An Al Jazeera article published May 31, 2026 ("Ethiopia's election: Parties, coalitions and candidates explained," https://www.aljazeera.com/news/2026/5/31/ethiopias-election-parties-coalitions-and-candidates-explained) lists the Peace for Ethiopia coalition among participating political entities, states the coalition "coordinates candidate lists across its member parties," and that its "members are contesting seats in both federal and regional councils." There is no mention of a withdrawal or boycott [97cd7d]. This dated coverage from one of the named credible sources (Al Jazeera, comparable to Reuters/AP) covers the entire resolution window up to the day before the June 1 deadline and shows the coalition still actively contesting.
- The Africa Research Bulletin (Wiley) likewise describes that "the Peace for Ethiopia Coalition HAD threatened to boycott the June elections" — past-tense framing of a threat that was not carried out, with no reporting of an actual withdrawal.
- The election proceeded on June 1, 2026 with 47 parties in the race (BBC/Reuters coverage), and no Addis Standard, Reuters, AP, or NEBE report of an official coalition-wide withdrawal between April 30 and June 1, 2026 was found despite targeted searches.

Because the coalition as a whole continued to participate (its member parties contesting seats per Al Jazeera's May 31 article), there was no official withdrawal — neither a formal NEBE notification nor a public statement of withdrawal by the coalition's leadership within the window. Per the resolution criteria, absence of a confirmed official withdrawal by 23:59 UTC on June 1, 2026 resolves the question NO. Additionally, since members continued participating rather than withdrawing, any partial-withdrawal scenario would also resolve NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-147. `ba5ea2ee-92af-5c3f-92eb-03f364e611b4`

- Present date: `2026-05-29 00:18:13.795575`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Pakistan implement daily fuel price adjustments for Motor Spirit (Petrol) and High-Speed Diesel (HSD) by July 1, 2026?

**Resolution criteria**

This question resolves Yes if, on or after May 12, 2026, and before July 1, 2026 (11:59 PM PKT, UTC+5), the Government of Pakistan or the Oil and Gas Regulatory Authority (OGRA) officially implements a daily fuel price adjustment mechanism for both Motor Spirit (MS/Petrol) and High-Speed Diesel (HSD). 

"Daily" is defined as price adjustments occurring at least once every calendar day or once every working day (i.e., excluding weekends/public holidays), as specified in the official notification.

The resolution source shall be the official notification published by the Pakistan Ministry of Energy (Petroleum Division) (https://www.petroleum.gov.pk/) or OGRA (https://www.ogra.org.pk/), or credible reporting from major Pakistani news outlets (e.g., Dawn at https://www.dawn.com/, Geo News at https://www.geo.tv/, Business Recorder at https://www.brecorder.com/) confirming that such a mechanism has been formally implemented and is in effect.

If no official daily pricing mechanism for both MS/Petrol and HSD is implemented and in effect before July 1, 2026 (11:59 PM PKT), the question resolves No. A mere announcement or proposal without actual implementation does not count; prices must actually be adjusted on a daily basis under the new mechanism for at least one full cycle.

**Pre-cutoff background**

Pakistan has historically adjusted retail fuel prices on a fortnightly basis through notifications issued by the Oil and Gas Regulatory Authority (OGRA) and the Finance Division. In early 2026, amid volatility caused by the conflict involving Iran and disruptions near the Strait of Hormuz, Pakistan shifted to weekly fuel price adjustments [Pakistan weighs daily fuel pricing under IMF review as war ...](https://www.arabnews.com/node/2637888/%7B%7B). As of May 13, 2026, Pakistan adjusts fuel prices on a weekly basis [Pakistan weighs daily fuel pricing under IMF review as war ...](https://www.arabnews.com/node/2637888/%7B%7B).

The International Monetary Fund (IMF), as part of Pakistan's Extended Fund Facility (EFF) program, has been pressing the government to further increase the frequency of price adjustments to daily revisions, in order to eliminate pricing distortions and keep domestic fuel prices in line with international costs [Pakistan weighs daily fuel pricing under IMF review as war ...](https://www.arabnews.com/node/2637888/%7B%7B). The IMF completed its third review of Pakistan's EFF arrangement on May 8, 2026, with energy pricing reform identified as a key condition.

Pakistani officials have publicly acknowledged that daily pricing is under consideration, with the IMF discussing adjustment frequencies of "a week or a day" with the government [Pakistan weighs daily fuel pricing under IMF review as war ...](https://www.arabnews.com/node/2637888/%7B%7B). However, officials have noted that governing daily price implementation at petrol pumps presents significant logistical challenges [Pakistan weighs daily fuel pricing under IMF review as war ...](https://www.arabnews.com/node/2637888/%7B%7B). The question carries genuine uncertainty: IMF pressure is strong, but political resistance and practical difficulties are real obstacles to implementation within this timeframe.

**Exact later resolution packet**

The question resolves NO. It asked whether, on or after May 12, 2026 and before July 1, 2026 (11:59 PM PKT), the Government of Pakistan or OGRA officially implemented and put into effect a DAILY fuel price adjustment mechanism (at least once every calendar day or working day) for BOTH Motor Spirit (Petrol) and High-Speed Diesel (HSD), with prices actually adjusted daily for at least one full cycle.

The evidence from allowed sources shows Pakistan remained on a WEEKLY pricing mechanism throughout the entire window and never implemented daily pricing:

1. OGRA's official "Notified Petroleum Prices" page (https://ogra.org.pk/notified-petroleum-prices) lists notifications effective May 23, May 30, June 6, June 13, June 20, and June 27, 2026 — spaced roughly seven days apart (weekly), not daily.

2. Business Recorder (article dated June 7, 2026) explicitly described the price change effective June 6, 2026 as part of the government's "weekly review of petroleum prices," confirming the framework was weekly, not daily [Govt jacks up petrol PL, reduces on HSD - Business Recorder](https://www.brecorder.com/news/40424357/govt-jacks-up-petrol-pl-reduces-on-hsd). (https://www.brecorder.com/news/40424357/govt-jacks-up-petrol-pl-reduces-on-hsd)

3. Dawn's article "Weekly oil pricing mechanism to stay," published June 24, 2026, reported that Petroleum Minister Ali Pervaiz Malik told oil-marketing company CEOs that "the seven-day pricing mechanism would not be changed now," and that any move toward daily pricing/deregulation would only be a gradual future shift — i.e., not implemented within this window [Weekly oil pricing mechanism to stay - Business - DAWN.COM](https://www.dawn.com/news/2010419). (https://www.dawn.com/news/2010419)

4. Dawn's article "Govt keeps petrol, diesel prices unchanged 'till further orders'" (published June 26, updated June 27, 2026) stated that "the government began revising petroleum prices every week on Friday night" and kept petrol (Rs299.50) and HSD (Rs311.47) unchanged "till further orders" — again confirming a weekly, not daily, cadence right at the end of the resolution window [Govt keeps petrol, diesel prices unchanged 'till further orders' - Dawn](https://www.dawn.com/news/2011069). (https://www.dawn.com/news/2011069)

There is no notification from the Ministry of Energy (Petroleum Division) or OGRA, nor any credible reporting from Dawn, Geo News, or Business Recorder, indicating that a daily price adjustment mechanism for both MS/Petrol and HSD was formally implemented and put into effect (i.e., actually adjusting prices daily for at least one full cycle) before July 1, 2026. At most, daily pricing remained under IMF-driven discussion as a possible future step. Per the resolution criteria, a mere announcement/proposal without actual daily implementation does not count. Therefore the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-148. `20650e4e-0a67-5c0e-90c0-6f91bb58b32f`

- Present date: `2026-05-02 16:50:21.174043`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the U.S. Department of Education announce the transfer of IDEA (special education) programs to another federal agency between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 1, 2026 and on or before June 1, 2026 (11:59 PM UTC), any of the following occurs:

1. The U.S. Department of Education, the White House Press Office, or the receiving federal agency (e.g., the Department of Health and Human Services) publishes an official announcement — such as a press release, signed interagency agreement (IAA), executive order, or departmental memorandum — confirming that administration of IDEA programs will be transferred from the Department of Education to another federal agency.

**"Transfer" is defined as:** A signed interagency agreement, executive order, or official departmental memorandum that formally assigns responsibility for administering IDEA programs (in whole or in substantial part) to a federal agency other than the Department of Education. A legislative proposal alone does not count; there must be an executive action or signed agreement.

**"IDEA programs" refers to:** Programs authorized under the Individuals with Disabilities Education Act (IDEA), as described at https://www.ed.gov/laws-and-policy/individuals-disabilities/individuals-disabilities-education-act-idea and https://www.congress.gov/crs_external_products/R/PDF/R41833/R41833.23.pdf — including Part B (special education grants to states) and Part C (early intervention).

**Resolution sources:** The announcement must be verifiable via at least one of the following official sources:
- Department of Education newsroom: https://www.ed.gov/news
- Federal Register: https://www.federalregister.gov/
- White House Press Office: https://www.whitehouse.gov/briefing-room/
- HHS newsroom: https://www.hhs.gov/about/news/index.html

If no such announcement is published by these sources by 11:59 PM UTC on June 1, 2026, this question resolves **No**.

**Pre-cutoff background**

The Trump administration has been systematically transferring programs out of the U.S. Department of Education to other federal agencies as part of its effort to dismantle the Department. As of April 1, 2026, the Department had struck 10 interagency agreements (IAAs) with five separate Cabinet-level agencies to transfer various programs. However, the Individuals with Disabilities Education Act (IDEA) programs — which provide federal funding and requirements for special education services to millions of students with disabilities — have not yet been transferred.

IDEA (https://www.congress.gov/crs_external_products/R/PDF/R41833/R41833.23.pdf) is a federal statute authorizing grant programs that support special education and early intervention services. The programs are currently administered by the Office of Special Education and Rehabilitative Services (OSERS) within the Department of Education (https://www.ed.gov/laws-and-policy/individuals-disabilities/individuals-disabilities-education-act-idea).

In February 2026, Politico reported that HHS was being considered as a potential destination for special education programs, but no plans had been announced at that time [https://www.politico.com/news/2026/02/23/trump-administration-to-shift-more-programs-out-of-education-department-00793309](https://www.politico.com/news/2026/02/23/trump-administration-to-shift-more-programs-out-of-education-department-00793309). As of late March 2026, disability advocates warned that "additional IAAs are expected very soon and may include transferring the programs of the Office of Special Education and Rehabilitative Services" [Ed Department May Offload Special Education Soon, Advocates Warn](https://www.disabilityscoop.com/2026/03/26/ed-department-may-offload-special-education-soon-advocates-warn/31925/). By April 29, 2026, Secretary of Education Linda McMahon confirmed the Department is "still working to offload" special education programs, but no official transfer has been finalized [Ed Department May Offload Special Education Soon, Advocates Warn](https://www.disabilityscoop.com/2026/03/26/ed-department-may-offload-special-education-soon-advocates-warn/31925/). Sources indicate an agreement to move IDEA to HHS is still expected but has not yet been executed.

This question tests whether the administration will formalize this politically sensitive transfer within the next month.

**Exact later resolution packet**

The question resolves NO. It asks whether, between May 1 and June 1, 2026, an official source (ED newsroom, Federal Register, White House Press Office, or HHS newsroom) published an announcement confirming an executive transfer (signed interagency agreement, executive order, or departmental memorandum) of IDEA programs (Part B or Part C) from the Department of Education to another federal agency.

Key dispositive evidence:
- The U.S. Department of Education's official newsroom press release dated May 13, 2026 ("Secretary McMahon Announces $144M Boost for Students with Disabilities") explicitly confirms the Department itself is STILL administering and investing in IDEA programs during the resolution window. It states funds "will be awarded this year for state and local agencies to use for Individuals with Disabilities Education Act (IDEA) programs," and references the Department's own guidance on FY 2026 IDEA Part C appropriations — i.e., ED, not HHS or any other agency, remains the administrator [f4d421]. This is direct evidence from a designated official resolution source (ed.gov/news) that no transfer occurred and IDEA stayed within ED.
- An Education Week program-transfer tracker (published April 1, 2026) tracking all interagency agreements does not list IDEA/OSERS as transferred, and contains no May 2026 update indicating such a transfer [d827ba].
- The Disability Scoop coverage (March 26, 2026), whose "latest news" runs through June 2, 2026, shows only that a transfer was anticipated/expected but not finalized; no announcement of an executed transfer appears in the May 1–June 1 window [ed9919].
- The Council for Exceptional Children blog "IDEA at Risk: Move to HHS Still Expected" (Nov 19, 2025) states OSERS "has not been relocated" and the move was only expected/forthcoming — predating the window and confirming no transfer had occurred [b4144a].

Across all official resolution sources and corroborating reporting, there is no signed IAA, executive order, or departmental memorandum published between May 1 and June 1, 2026 transferring IDEA programs out of ED. Throughout this period the transfer remained a stated intention ("still working to offload") but was never executed. Therefore the question resolves NO.

Relevant URLs:
- ED newsroom press release (May 13, 2026): http://www.ed.gov/about/news/press-release/secretary-mcmahon-announces-144m-boost-students-disabilities
- EdWeek tracker: https://www.edweek.org/policy-politics/see-which-ed-dept-programs-are-moving-to-new-agencies-a-tracker/2026/04
- Disability Scoop (Mar 26, 2026): https://www.disabilityscoop.com/2026/03/26/ed-department-may-offload-special-education-soon-advocates-warn/31925/
- Council for Exceptional Children: https://exceptionalchildren.org/blog/idea-risk-move-hhs-still-expected

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-149. `fe33f742-7506-5a1c-80c0-d3c6e73b2ce5`

- Present date: `2026-05-12 22:23:08.079894`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Alexander Bublik reach the semifinals or better at the 2026 Terra Wortmann Open (Halle Open)?

**Resolution criteria**

This question resolves **Yes** if Alexander Bublik reaches the semifinals or any later stage (semifinal, final, or wins the title) of the 2026 Terra Wortmann Open singles main draw. This question resolves **No** if any of the following occur:

1. Bublik is eliminated before the semifinal round (i.e., loses in the Round of 32, Round of 16, or Quarterfinals).
2. Bublik does not enter or withdraws from the tournament before his first match.
3. Bublik receives a walkover into the semifinals but then withdraws before playing the semifinal — this still counts as "reaching the semifinals" and resolves **Yes**.
4. If Bublik retires mid-match (withdrawal during a match) before the semifinal round, this counts as a loss and resolves **No**. If he retires mid-match during or after the semifinal round, this resolves **Yes** (he reached the semifinals).

"Reaching the semifinals" means appearing in the semifinal draw as a participant, regardless of the outcome of the semifinal match itself.

The relevant match or achievement must occur on or after May 10, 2026 (the tournament is scheduled for June 15–21, 2026, so this condition is naturally satisfied).

Resolution will be verified using the official ATP Tour results page for the 2026 Terra Wortmann Open: https://www.atptour.com/en/scores/archive/halle/500/2026/results

All tournament times reference Central European Summer Time (CEST, UTC+2), the local timezone for Halle, Germany. The resolution deadline is June 22, 2026, 23:59 UTC, to allow for any scheduling delays.

**Pre-cutoff background**

The Terra Wortmann Open (Halle Open) is an ATP 500 grass-court tennis tournament held annually in Halle, Germany. The 2026 edition is scheduled for June 15–21, 2026 [Halle | Overview | ATP Tour | Tennis](https://www.atptour.com/en/tournaments/halle/500/overview). The tournament features a 32-player singles main draw.

Alexander Bublik is a two-time champion of this event, having won in 2023 and 2025 [Halle | Overview | ATP Tour | Tennis](https://www.atptour.com/en/tournaments/halle/500/overview). As of early 2026, Bublik's ATP singles ranking is approximately No. 11, with a career-high of No. 10 reached on January 12, 2026 [Alexander Bublik | Overview | ATP Tour | Tennis](https://www.atptour.com/en/players/alexander-bublik/bk92/overview). He broke into the top 10 for the first time in January 2026 after winning the Hong Kong Open, completing a remarkable rise from No. 82 in March 2025.

The 2026 field is expected to include top players such as Zverev, Medvedev, Rublev, Fritz, Shelton, Tiafoe, and Cobolli. Recent champions include Sinner (2024) and Hurkacz (2022) [Halle | Overview | ATP Tour | Tennis](https://www.atptour.com/en/tournaments/halle/500/overview). Despite Bublik's strong track record at this venue, reaching the semifinals of an ATP 500 event with a 32-player draw requires winning at least two matches against high-caliber opponents, making the outcome uncertain even for a two-time defending champion.

**Exact later resolution packet**

The question asks whether Alexander Bublik reached the semifinals or better at the 2026 Terra Wortmann Open (Halle Open) singles main draw.

RESOLUTION: NO (0).

Evidence:
- The official ATP Tour results page for the 2026 Terra Wortmann Open (https://www.atptour.com/en/scores/archive/halle/500/2026/results) shows that Alexander Bublik played in the Round of 32 (first round) on Tuesday, June 16, 2026, and LOST to Mattia Bellucci with a score of 7-6(6), 6-1 [https://www.atptour.com/en/scores/archive/halle/500/2026/results](https://www.atptour.com/en/scores/archive/halle/500/2026/results). He was thus eliminated in the Round of 32.
- Wikipedia's "2026 Halle Open – Singles" page confirms Bublik was the 7th seed and the two-time defending champion, and that he was eliminated in the FIRST ROUND, losing to qualifier Mattia Bellucci 6-7, 1-6. This is corroborated by cited Reuters and TennisTourTalk articles describing it as a "shock" defeat of the defending champion [2026 Halle Open – Singles - Wikipedia](https://en.wikipedia.org/wiki/2026_Halle_Open_%E2%80%93_Singles).

Because Bublik lost in the Round of 32, he did NOT reach the Round of 16, Quarterfinals, or Semifinals. He did not appear in the semifinal draw as a participant. Per the resolution criteria, elimination before the semifinal round (specifically, a loss in the Round of 32) resolves the question NO.

Note on a potential red herring: An ATP video titled "Hot Shot: Bublik prevails in all-court battle with Bellucci in Halle 2026" exists, but this is a clip of a single point ("Watch Alexander Bublik fire a forehand to claim a fun point"), NOT the match outcome. The actual match was a loss for Bublik. This does not change the resolution.

None of the YES conditions apply: Bublik entered and played (so it was not a pre-match withdrawal), and he did not receive a walkover into the semifinals. He was straightforwardly beaten in the first round. Therefore the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-150. `9111682c-130e-5d07-a7d1-54933a671517`

- Present date: `2026-04-30 17:09:23.379889`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

IF President Trump and President Xi Jinping hold an in-person bilateral meeting between April 30 and June 1, 2026, THEN will the US and China issue a joint statement on trade following the May 2026 Trump-Xi summit?

**Resolution criteria**

This conditional question resolves YES if B resolves YES AND A resolves YES. It resolves NO if B resolves YES AND A resolves NO. If B resolves NO, this question is voided (no resolution / N/A).

=== Resolution Criteria for A (Will the US and China issue a joint statement on trade following the May 2026 Trump-Xi summit?) ===
This question resolves **Yes** if, on or after April 30, 2026 and before June 1, 2026 (23:59 UTC), the United States and the People's Republic of China publish a joint statement on trade—defined as meeting ALL of the following criteria:

1. **Joint statement format**: A single document issued by both governments, or simultaneous official releases by both the White House (https://www.whitehouse.gov/) and the Ministry of Foreign Affairs of the PRC (https://www.fmprc.gov.cn/eng/) that are explicitly described as a "joint statement," "joint communiqué," or "joint declaration."

2. **On trade**: The statement must substantively address commerce, tariffs, trade balances, market access, or other matters directly related to bilateral trade in goods or services. Statements that only address diplomatic, security, or other non-commercial topics do not qualify.

3. **Linked to the May 2026 summit**: The statement must be issued as a direct outcome of the planned May 2026 Trump-Xi summit.

If no such statement meeting all three criteria is published by 23:59 UTC on May 31, 2026, this question resolves **No**.

=== Resolution Criteria for B (Will President Trump and President Xi Jinping hold an in-person bilateral meeting between April 30 and June 1, 2026?) ===
This question resolves **Yes** if, on or after April 30, 2026 and on or before June 1, 2026 (all dates interpreted in UTC), President Donald Trump and President Xi Jinping hold an in-person bilateral meeting.

**Definition of "in-person bilateral meeting":** A scheduled, formal meeting where both heads of state are physically present in the same room or venue for the purpose of diplomatic discussion between the United States and China, lasting at least 30 minutes. Brief informal encounters (e.g., a handshake or short exchange on the sidelines of a multilateral event without a dedicated bilateral session) do not count. A meeting held as a formal bilateral session on the sidelines of a multilateral summit does count, provided it is a dedicated U.S.-China session.

**Resolution source:** Official confirmation from the White House (https://www.whitehouse.gov/) or the Chinese Ministry of Foreign Affairs (https://www.fmprc.gov.cn/eng/), or consistent reporting from at least two of the following credible news agencies: Reuters (https://www.reuters.com/), Associated Press (https://apnews.com/), AFP, or Bloomberg. The source must confirm that the meeting physically took place (not merely that it was scheduled).

If no such meeting is confirmed by 23:59 UTC on June 1, 2026, the question resolves **No**.

**Pre-cutoff background**

This is a conditional question linking two underlying binary events.

=== Background for A (Will the US and China issue a joint statement on trade following the May 2026 Trump-Xi summit?) ===
US President Donald Trump is scheduled to meet Chinese President Xi Jinping on May 14–15, 2026 in China [https://www.reuters.com/world/us/with-tariffs-stalled-trumps-china-policy-drifts-2026-04-21/](https://www.reuters.com/world/us/with-tariffs-stalled-trumps-china-policy-drifts-2026-04-21/). This summit follows a turbulent period in US-China trade relations. In February 2026, the US Supreme Court issued a ruling that invalidated many of the Trump administration's global tariffs, fundamentally undermining the administration's leverage in trade negotiations [https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/](https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/). Reuters has characterized the resulting US policy toward China as "adrift," with departments often acting in contradictory ways and no coherent "Plan B" for trade strategy [https://www.reuters.com/world/us/with-tariffs-stalled-trumps-china-policy-drifts-2026-04-21/](https://www.reuters.com/world/us/with-tariffs-stalled-trumps-china-policy-drifts-2026-04-21/).

Previous high-level meetings between the two leaders have produced joint statements: the May 2025 Geneva meeting and the October 2025 Busan meeting both resulted in trade truces accompanied by formal joint documents [https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/](https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/). A sixth round of trade talks took place in Paris in March 2026, which both sides described as "constructive" [https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/](https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/). However, the current diplomatic environment is considerably more uncertain due to the Supreme Court ruling and policy drift, making it unclear whether the May 2026 summit will produce a similar outcome.

Resolution will be based on official publications from the White House (https://www.whitehouse.gov/) and the Chinese Ministry of Foreign Affairs (https://www.fmprc.gov.cn/eng/).

=== Background for B (Will President Trump and President Xi Jinping hold an in-person bilateral meeting between April 30 and June 1, 2026?) ===
As of late April 2026, U.S. President Donald Trump is scheduled to visit China for a summit with President Xi Jinping on May 14–15, 2026. This would be the first visit to China by an American president in eight years [https://www.reuters.com/world/us/with-tariffs-stalled-trumps-china-policy-drifts-2026-04-21/](https://www.reuters.com/world/us/with-tariffs-stalled-trumps-china-policy-drifts-2026-04-21/). However, the summit was previously postponed from late March 2026 due to the ongoing Iran conflict [https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/](https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/). The U.S.-China relationship remains tense, characterized by tit-for-tat tariffs and what has been described as an "adrift" and "erratic" China policy from the Trump administration [https://www.reuters.com/world/us/with-tariffs-stalled-trumps-china-policy-drifts-2026-04-21/](https://www.reuters.com/world/us/with-tariffs-stalled-trumps-china-policy-drifts-2026-04-21/). The volatile geopolitical environment—including the Iran war and unresolved trade disputes—creates genuine uncertainty about whether the summit will proceed as currently scheduled or face another postponement.

Key sources:
- Reuters, "Trump's trade war with China in focus ahead of May summit" (April 6, 2026): https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/
- Reuters, "With tariffs stalled, Trump's China policy drifts" (April 21, 2026): https://www.reuters.com/world/us/with-tariffs-stalled-trumps-china-policy-drifts-2026-04-21/

**Exact later resolution packet**

This is a Metaculus conditional question: IF Trump and Xi hold an in-person bilateral meeting between April 30 and June 1, 2026 (B), THEN will the US and China issue a joint statement on trade following the summit (A)?

ANTECEDENT B = YES (the meeting occurred):
- President Trump made a state visit to China from May 13-15, 2026, and held formal bilateral talks with President Xi Jinping at the Great Hall of the People on May 14, 2026. The talks lasted approximately two hours in total, far exceeding the 30-minute minimum and satisfying the "formal in-person bilateral meeting" definition [c5da5e]. Reuters confirmed the meeting physically took place over two days (May 14-15, 2026) [989e41]. NPR also confirms the summit occurred on May 14-15, 2026 [1beb29]. This meets the credible-source requirement (Reuters reporting plus official readouts). The White House published a "Readout of President Trump's Meeting With Chinese President Xi Jinping" (china.usembassy-china.org.cn), and a White House fact sheet (whitehouse.gov/fact-sheets/2026/05/...) confirmed the summit. Thus B resolves YES; the conditional is "live" and resolves on A.

CONSEQUENT A = NO (no qualifying joint statement on trade):
- The resolution criteria for A require a single document issued by both governments, OR simultaneous official releases by BOTH the White House and the PRC Ministry of Foreign Affairs that are EXPLICITLY described as a "joint statement," "joint communiqué," or "joint declaration" on trade.
- Instead, each side issued its OWN separate readout/announcement, and the two readouts were inconsistent. NPR's May 22, 2026 article "comparing U.S. and China announcements" explicitly contrasts the separate readouts and notes "minor inconsistencies" on agriculture, tariffs, and rare earths, with each side sticking to its own interpretation [1beb29]. Reuters described a separate "U.S. summary of Thursday's talks" and a separate "statement released by [China's] ministry" — i.e., separate documents, not a joint one [989e41]. CSIS analysis ("What did the Trump-Xi Summit Achieve?") explicitly stated: "We're not seeing a joint statement or joint readout" (search result, CSIS). Al Jazeera reported "Trump-Xi summit: China, US disagree on what they agreed on... Neither side confirmed the other's claims" (search result).
- The White House fact sheet (whitehouse.gov) was a unilateral US document titled "Fact Sheet: President Donald J. Trump Secures Historic Deals with China," not a joint statement. No document explicitly titled "joint statement," "joint communiqué," or "joint declaration" was issued by both governments.

Because B resolved YES but A resolved NO, the conditional question resolves NO (0). (Per the criteria: "It resolves NO if B resolves YES AND A resolves NO.")

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-151. `5665d6d9-60a3-5121-bd6f-8c94ab972ab6`

- Present date: `2026-05-14 10:17:45.505680`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the HCLG Committee's pre-legislative scrutiny report on the draft Commonhold and Leasehold Reform Bill recommend a ground rent cap lower than £250/year?

**Resolution criteria**

This question resolves **Yes** if the HCLG Committee's final pre-legislative scrutiny report on the draft Commonhold and Leasehold Reform Bill, published on or after May 12, 2026, includes a recommendation in its "Conclusions and recommendations" section (or equivalent numbered/listed recommendations) for a ground rent cap figure that is strictly lower than £250 per year. A recommendation for "peppercorn rent," "zero ground rent," "nominal rent," or any specific figure below £250 satisfies this condition.

This question resolves **No** if:
1. The report is published but recommends maintaining the £250/year cap or a higher figure; or
2. The report is published but does not include a specific recommendation regarding the numerical value of the ground rent cap in its conclusions/recommendations; or
3. No report is published by the committee by July 1, 2026 (23:59 UTC).

**Resolution source:** The official UK Parliament publications page for this inquiry: https://committees.parliament.uk/work/9587/prelegislative-scrutiny-of-the-draft-commonhold-and-leasehold-reform-bill/publications/

A "recommendation" is defined as a statement appearing in the report's formal "Conclusions and recommendations" chapter or section (standard in select committee reports), or if no such section exists, any paragraph explicitly identified as a recommendation using bold text or numbered recommendation formatting, that calls for the ground rent cap to be set at a specific figure below £250/year or at peppercorn/zero.

**Pre-cutoff background**

On 27 January 2026, the UK Government published a draft Commonhold and Leasehold Reform Bill for pre-legislative scrutiny [Pre-legislative scrutiny of the draft Commonhold and Leasehold ...](https://committees.parliament.uk/work/9587/prelegislative-scrutiny-of-the-draft-commonhold-and-leasehold-reform-bill/). The draft bill proposes capping ground rents at £250 per year for existing leasehold properties. The Housing, Communities and Local Government (HCLG) Committee (https://committees.parliament.uk/committee/17/housing-communities-and-local-government-committee/) was asked to conduct pre-legislative scrutiny of the bill (https://committees.parliament.uk/work/9587/prelegislative-scrutiny-of-the-draft-commonhold-and-leasehold-reform-bill/).

The £250/year ground rent cap has been a major point of contention. Leaseholder campaign groups and residents' associations have argued for "peppercorn" rents (i.e., zero or nominal ground rent), while property industry groups such as the British Property Federation and Residential Freehold Association have submitted evidence regarding the financial implications of lower caps [Pre-legislative scrutiny of the draft Commonhold and Leasehold ...](https://committees.parliament.uk/work/9587/prelegislative-scrutiny-of-the-draft-commonhold-and-leasehold-reform-bill/publications/). "Pre-legislative scrutiny" refers to the examination of draft legislation by a parliamentary committee before it is formally introduced to Parliament (https://www.parliament.uk/site-information/glossary/pre-legislative-scrutiny/). "Ground rent" is a payment made by a leaseholder to a freeholder under the terms of a lease (https://www.legislation.gov.uk/ukpga/2022/1/contents/enacted).

The committee completed oral evidence sessions on 24 March 2026 and the written evidence deadline was 25 February 2026 [Pre-legislative scrutiny of the draft Commonhold and Leasehold ...](https://committees.parliament.uk/work/9587/prelegislative-scrutiny-of-the-draft-commonhold-and-leasehold-reform-bill/). The committee indicated it would publish its report "later in the spring" [Pre-legislative scrutiny of the draft Commonhold and Leasehold ...](https://committees.parliament.uk/work/9587/prelegislative-scrutiny-of-the-draft-commonhold-and-leasehold-reform-bill/). As of 13 May 2026, no final report has been published [Pre-legislative scrutiny of the draft Commonhold and Leasehold ...](https://committees.parliament.uk/work/9587/prelegislative-scrutiny-of-the-draft-commonhold-and-leasehold-reform-bill/publications/). The most recent publication was a letter from the Spectrum Residents Association dated 22 April 2026 [Pre-legislative scrutiny of the draft Commonhold and Leasehold ...](https://committees.parliament.uk/work/9587/prelegislative-scrutiny-of-the-draft-commonhold-and-leasehold-reform-bill/publications/).

**Exact later resolution packet**

RESOLUTION: NO (0)

**1. The report was published within the resolution window.**
The HCLG Committee published its "1st Report — Pre-legislative scrutiny of the draft Commonhold and Leasehold Reform Bill" (HC 40) on **27 May 2026**, available at https://publications.parliament.uk/pa/cm5902/cmselect/cmcomloc/40/report.html and listed on the official inquiry publications page https://committees.parliament.uk/work/9587/prelegislative-scrutiny-of-the-draft-commonhold-and-leasehold-reform-bill/publications/ [1a07da, e00c0c, 90457a, fc64c9]. This falls inside the required window (on/after 12 May 2026 and before 1 July 2026, 23:59 UTC), so the "no report published" NO condition does not apply.

**2. The report did NOT recommend a ground rent cap strictly lower than £250/year.**
In its Conclusions and recommendations, the Committee explicitly endorsed the Government's £250 cash cap. It states: "We agree with the government's rationale for a £250 cash cap, as this is a threshold where ground rent frequently affects the saleability and mortgageability of properties. A cap at this value will ensure leaseholders are protected from increases in ground rent to onerous levels" [e00c0c, 90457a]. The Committee described the £250 cap as reasonable and fair [e00c0c]. The Leasehold Advisory Service's summary likewise confirms the Committee did not recommend a numerical cap lower than £250 nor endorse an immediate peppercorn/zero cap in its recommendations [fc64c9].

**3. The peppercorn-related recommendation does not satisfy the YES condition.**
The Committee did address a transition to peppercorn ground rent, but only in the context of the timeline for the Government's already-planned eventual phase-out — recommending the transitional period be reduced from 40 years to 20 years, and recommending a commencement clause so the £250 cap comes into force two months after Royal Assent [90457a, 9c6dea]. This is a recommendation about the timing of the pre-existing transition mechanism, not a recommendation to set the ground rent cap figure itself strictly below £250. The recommended ground rent cap figure remains £250 [e00c0c, 90457a].

**Conclusion:** Because the report was published (27 May 2026) but recommends maintaining the £250/year cap rather than a figure strictly lower than £250 (or peppercorn/zero as the cap), NO condition #1 of the resolution criteria is met. The question resolves NO.

Resolution source (parliament.uk): https://publications.parliament.uk/pa/cm5902/cmselect/cmcomloc/40/report.html (linked from https://committees.parliament.uk/work/9587/prelegislative-scrutiny-of-the-draft-commonhold-and-leasehold-reform-bill/publications/)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-152. `101bf24c-e52c-5639-9a6f-fd1114c13048`

- Present date: `2026-05-02 15:27:18.487988`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will California AB 222 (Data Centers: Energy Usage Reporting) pass the California State Senate by June 1, 2026?

**Resolution criteria**

This question resolves YES if California Assembly Bill 222 (2025–2026 session) successfully passes a floor vote (third reading) in the California State Senate on or after May 1, 2026 (00:00 UTC) and on or before June 1, 2026 (23:59 UTC). "Passing" is defined as the bill receiving a majority vote on the Senate floor as recorded in the official legislative history.

This question resolves NO if AB 222 does not pass the Senate floor vote by June 1, 2026 (23:59 UTC), including if the bill remains held in committee, fails a floor vote, or is otherwise inactive.

Resolution source: The official California Legislative Information website bill history page at https://leginfo.legislature.ca.gov/faces/billHistoryClient.xhtml?bill_id=202520260AB222

**Pre-cutoff background**

California Assembly Bill 222 (AB 222), authored by Assemblymember Bauer-Kahan, addresses data center energy usage reporting requirements. The bill requires AI model developers to publicly report energy used to train models and mandates data centers to report energy usage to the California Energy Commission.

AB 222 was introduced on January 8, 2025, and progressed through multiple Assembly committees before passing the Assembly floor on June 2, 2025, with a vote of 57 Ayes to 18 Noes [https://leginfo.legislature.ca.gov/faces/billHistoryClient.xhtml?bill_id=202520260AB222](https://leginfo.legislature.ca.gov/faces/billHistoryClient.xhtml?bill_id=202520260AB222). The bill then moved to the Senate, where it was referred to the Committees on Energy, Utilities & Communications and Judiciary. It passed the Senate Judiciary Committee on July 15, 2025 (Ayes 11, Noes 2) and was re-referred to Senate Appropriations [https://leginfo.legislature.ca.gov/faces/billHistoryClient.xhtml?bill_id=202520260AB222](https://leginfo.legislature.ca.gov/faces/billHistoryClient.xhtml?bill_id=202520260AB222). On August 18, 2025, the bill was referred to the suspense file in Senate Appropriations, and on August 29, 2025, it was "held under submission" in committee [https://leginfo.legislature.ca.gov/faces/billHistoryClient.xhtml?bill_id=202520260AB222](https://leginfo.legislature.ca.gov/faces/billHistoryClient.xhtml?bill_id=202520260AB222).

Being "held under submission" in Senate Appropriations effectively stalls the bill. However, the California Legislature operates on a two-year session (2025–2026), meaning the bill remains alive and can be reconsidered when the legislature reconvenes in January 2026. Bills held in Appropriations suspense can be revived in the second year of the session, but this is not guaranteed — significant industry opposition to data center regulation in California has previously thwarted similar efforts. As of May 1, 2026, the bill's status should be checked for any movement since the legislature reconvened.

Resolution source: The official California Legislative Information bill history page at https://leginfo.legislature.ca.gov/faces/billHistoryClient.xhtml?bill_id=202520260AB222

**Exact later resolution packet**

The question resolves NO because California AB 222 (2025–2026 session) did not pass a Senate floor (third reading) vote between May 1, 2026 and June 1, 2026.

Evidence:
- The official California Legislative Information bill history page (https://leginfo.legislature.ca.gov/faces/billHistoryClient.xhtml?bill_id=202520260AB222) shows that the last recorded legislative action for AB 222 was on August 29, 2025: "In committee: Held under submission" in the Senate Appropriations Committee. There are NO subsequent entries for the remainder of 2025 or for 2026, meaning no Senate floor vote occurred and the bill never moved out of the Senate Appropriations suspense process [https://leginfo.legislature.ca.gov/faces/billHistoryClient.xhtml?bill_id=202520260AB222](https://leginfo.legislature.ca.gov/faces/billHistoryClient.xhtml?bill_id=202520260AB222).
- The bill was placed in the suspense file on August 18, 2025, and held under submission on August 29, 2025; as of June 1, 2026, it had not received a Senate Third Reading floor vote and remained stalled in committee [https://leginfo.legislature.ca.gov/faces/billHistoryClient.xhtml?bill_id=202520260AB222](https://leginfo.legislature.ca.gov/faces/billHistoryClient.xhtml?bill_id=202520260AB222).
- Independent reporting corroborates that the effort effectively died: a CalMatters article (December 2025) reports that "California's push to regulate AI data center energy use was reduced to a 2027 report after Big Tech lobbied against stricter rules," confirming the bill did not advance to passage in its original form.

Per the strict resolution criteria, the question resolves NO if AB 222 does not pass the Senate floor vote on or before June 1, 2026 (23:59 UTC), including if the bill remains held in committee or is otherwise inactive. The bill remained held under submission in the Senate Appropriations Committee beyond the June 1, 2026 deadline and never received the required Senate floor vote. Therefore the resolution is NO (0).

Resolution source: https://leginfo.legislature.ca.gov/faces/billHistoryClient.xhtml?bill_id=202520260AB222

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-153. `ca7d1be5-c084-5d6e-8768-30c3c4c4908b`

- Present date: `2026-05-07 22:53:23.363301`
- Source cutoff boundary: `2026-05-08` (encodes end of UTC day `2026-05-07`)
- Expected resolution: `2026-06-20T00:00:00`

**Question**

Will the 2026 G7 Évian Summit Leaders' Communiqué explicitly mention 'China' by name?

**Resolution criteria**

This question resolves as **Yes** if the word "China" appears in the official final Leaders' Communiqué (or equivalent principal outcome document such as a "Chair's Summary" or "Leaders' Declaration") issued at the conclusion of the 52nd G7 Summit in Évian-les-Bains, France.

**Definitions and clarifications:**

1. **"Communiqué"** refers to the principal official outcome document issued by the G7 leaders at the conclusion of the summit. For reference, the 2024 equivalent was the "Apulia G7 Leaders' Communiqué" (https://www.g7italy.it/en/apulia-g7-leaders-communique-2/). If the French presidency uses a different title (e.g., "Chair's Summary," "Leaders' Declaration"), the principal outcome document serves as the resolution source. Ancillary ministerial statements, press releases, or topic-specific side statements do not count.

2. **"Explicitly mention"** means the English-language version of the document contains any of the following terms (case-insensitive): "China", "Chinese", "People's Republic of China", or "Beijing" when used to refer to the government or state of China (not, e.g., a reference to "Beijing time" or an unrelated proper noun).

3. **Authoritative language version:** The **English-language** version of the communiqué will be the authoritative text for resolution purposes.

4. **Resolution source:** The communiqué is expected to be published on the official French G7 presidency site at https://www.elysee.fr/en/G7evian or its news subsection at https://www.elysee.fr/en/G7evian/all-actualities. If unavailable there, the University of Toronto G7 Research Group archive at https://g7.utoronto.ca/ may be used as a secondary source.

5. If no principal outcome document is released by 23:59 UTC on July 31, 2026, the question resolves as **No**.

**Pre-cutoff background**

The 52nd G7 Summit is scheduled for June 15–17, 2026, in Évian-les-Bains, France, hosted by President Emmanuel Macron [52nd G7 summit - Wikipedia](https://en.wikipedia.org/wiki/52nd_G7_summit). The G7 brings together leaders from Canada, France, Germany, Italy, Japan, the United Kingdom, the United States, and the European Union.

In November 2025, Macron floated the idea of inviting Chinese leader Xi Jinping to the summit, but Japan objected due to an ongoing diplomatic crisis with China. Ultimately, China was not invited; the invited outreach partners are Brazil, India, Kenya, and South Korea [52nd G7 summit - Wikipedia](https://en.wikipedia.org/wiki/52nd_G7_summit).

At the most recent summit — the 2025 Kananaskis Summit in Canada — the Canadian presidency opted not to issue a traditional "Leaders' Communiqué," instead releasing a "Chair's Summary" along with several topic-specific leaders' statements [China Isn't on the G7 Agenda, but It's Still the Main Event - CSIS](https://www.csis.org/analysis/china-isnt-g7-agenda-its-still-main-event) [2025 Kananskis Summit Official Documents - g7@utoronto.ca](https://g7.utoronto.ca/summit/2025kananaskis/index.html). Notably, China was not on the public agenda at Kananaskis, though it remained a central topic behind closed doors, with G7 leaders coordinating on Indo-Pacific security, economic resilience, and countering Chinese economic practices [China Isn't on the G7 Agenda, but It's Still the Main Event - CSIS](https://www.csis.org/analysis/china-isnt-g7-agenda-its-still-main-event). A subsequent G7 Foreign Ministers' Meeting in November 2025 explicitly raised alarm over China's military buildup [51st G7 summit - Wikipedia](https://en.wikipedia.org/wiki/51st_G7_summit).

Previous G7 leaders' communiqués — such as the 2024 Apulia communiqué — have extensively mentioned China by name, addressing topics including trade practices, military buildup, and the South China Sea. However, France's pragmatic diplomatic approach (e.g., keeping climate off the G7 environment ministers' agenda to avoid a US clash) introduces uncertainty about whether the 2026 communiqué will name China explicitly or use softer, indirect language.

The official website for the 2026 G7 summit is https://www.elysee.fr/en/G7evian [2026 G7 SUMMIT OF EVIAN](https://www.elysee.fr/en/G7evian), where summit documents are expected to be published.

**Exact later resolution packet**

Adjudicated: The 52nd G7 Évian Summit (June 15-17, 2026) did NOT issue a single principal outcome document: no Leaders' Communiqué, no Chair's Summary, and no single overarching Leaders' Declaration. Instead the French presidency released nine co-equal topic-specific leaders' declarations/statements (verified on the Élysée outcomes page, which says 'Leaders adopted no fewer than nine declarations' and does not name China, and on the U. Toronto G7 Research Group archive at g7.utoronto.ca/summit/2026evian/). The word 'China' appears (twice: 'East and South China Seas ... Taiwan Strait' and 'with the participation of China') only in the thematic 'G7 Leaders' Statement on Geopolitical Issues' — but resolution criterion 1 requires a single 'principal official outcome document' and explicitly states 'topic-specific side statements do not count.' Read literally (criteria supersede reasonable interpretation), that thematic statement is a topic-specific document and no comprehensive principal communiqué/equivalent naming China exists, so the question resolves NO. (Note: this is genuinely contestable — an intent-based reading would resolve YES since leaders did name China.)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-154. `9cad0ef3-0d36-5e3f-8f21-b87dbaa2f8c0`

- Present date: `2026-05-16 17:17:52.581651`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the French assisted dying bill ("Droit à l'aide à mourir") be definitively adopted by the French Parliament by July 1, 2026?

**Resolution criteria**

This question resolves YES if the *Proposition de loi relative au droit à l'aide à mourir* (PPL n° 661) is definitively adopted by the French Parliament — meaning it has been passed in identical terms by both the National Assembly and the Senate, or adopted via the *dernier mot* procedure — on or after May 12, 2026 (12:00 CEST) and no later than July 1, 2026 (23:59 CEST).

"Definitively adopted" means the bill has completed its parliamentary journey and has been transmitted to the President of the Republic for promulgation, as indicated on the official legislative dossier page: https://www.senat.fr/dossier-legislatif/ppl24-661.html

The question resolves NO if the bill has not been definitively adopted by July 1, 2026 (23:59 CEST), including if:
- The bill is still undergoing readings (third reading, CMP, etc.)
- A CMP is convened but fails and the *dernier mot* procedure has not been completed
- The bill is withdrawn or abandoned
- The bill is adopted but with the core assisted dying provisions (formerly Article 2, establishing the *procédure d'aide à mourir*) deleted — i.e., if the final text does not include any provision establishing a right or procedure for assisted dying, the question resolves NO even if the bill is technically adopted

Note on "rejection" of Article 1 from the original question: During the second reading, the Senate deleted Article 2 (the article establishing the assisted dying procedure) by a vote of 151 to 118 on May 11, 2026 [Le Sénat supprime l'aide à mourir, clé de voûte de la proposition de ...](https://www.publicsenat.fr/actualites/parlementaire/le-senat-supprime-laide-a-mourir-cle-de-voute-de-la-proposition-de-loi-sur-la-fin-de-vie), and subsequently rejected the entire bill on May 12, 2026 [Droit à l'aide à mourir - Sénat](https://www.senat.fr/dossier-legislatif/ppl24-661.html). This question now asks whether the legislative process will ultimately result in definitive adoption of the bill with its assisted dying provisions intact, capturing the core uncertainty of whether the Senate's opposition will ultimately prevail.

Resolution source: The official legislative dossier at https://www.senat.fr/dossier-legislatif/ppl24-661.html and/or credible French news sources (Le Monde, Libération, Public Sénat).

**Pre-cutoff background**

France's assisted dying bill (*Proposition de loi relative au droit à l'aide à mourir*, PPL n° 661) has been the subject of a protracted legislative battle between the National Assembly and the Senate. The National Assembly adopted the bill in first reading on May 27, 2025, and in second reading on February 25, 2026 [Droit à l'aide à mourir - Sénat](https://www.senat.fr/dossier-legislatif/ppl24-661.html). The Senate, however, has consistently opposed the core assisted dying provisions: it rejected the bill in first reading on January 28, 2026, and again rejected it in second reading on May 12, 2026 [Droit à l'aide à mourir - Sénat](https://www.senat.fr/dossier-legislatif/ppl24-661.html).

During the Senate's second reading debate on May 11, 2026, senators voted 151 to 118 to delete Article 2 — the article establishing the assisted dying procedure (*procédure d'aide à mourir*), considered the keystone of the bill [Le Sénat supprime l'aide à mourir, clé de voûte de la proposition de ...](https://www.publicsenat.fr/actualites/parlementaire/le-senat-supprime-laide-a-mourir-cle-de-voute-de-la-proposition-de-loi-sur-la-fin-de-vie). On May 12, 2026, the Senate rejected the bill as a whole in a solemn vote [Droit à l'aide à mourir - Sénat](https://www.senat.fr/dossier-legislatif/ppl24-661.html).

As of May 12, 2026, the bill has been transmitted to the National Assembly for a third reading [Droit à l'aide à mourir - Sénat](https://www.senat.fr/dossier-legislatif/ppl24-661.html). For definitive adoption, the bill must either be passed in identical terms by both chambers, or the government must convene a Joint Committee (*Commission Mixte Paritaire*, CMP). If the CMP fails to reach agreement, the National Assembly can have the final word (*dernier mot*) after one more reading in each chamber.

The full legislative dossier is available at: https://www.senat.fr/dossier-legislatif/ppl24-661.html

The text of the bill as adopted by the Senate in second reading (Texte n° 109) is available via the legislative dossier page above [Droit à l'aide à mourir - Sénat](https://www.senat.fr/dossier-legislatif/ppl24-661.html). Public votes (*scrutins publics*) are recorded at: https://www.senat.fr/scrutin-public/scr-scrutin-public.html

**Exact later resolution packet**

The question resolves NO. The *Proposition de loi relative au droit à l'aide à mourir* (PPL n° 661) had NOT been definitively adopted by the French Parliament and had NOT been transmitted to the President of the Republic for promulgation by the July 1, 2026 (23:59 CEST) deadline.

Timeline established from the two official legislative dossiers:

1. Official Senate dossier (https://www.senat.fr/dossier-legislatif/ppl24-661.html): After the Senate rejected the bill on May 12, 2026, a Commission Mixte Paritaire (CMP) met and FAILED to reach agreement. The National Assembly then conducted a "nouvelle lecture" and adopted a text on June 30, 2026. The bill was transmitted back to the Senate for a "nouvelle lecture," with the Senate Commission des affaires sociales filing its report around July 1, 2026 and the public-session discussion scheduled for July 7 and 8, 2026 — i.e., the process was still ongoing past the deadline [https://www.senat.fr/dossier-legislatif/ppl24-661.html](https://www.senat.fr/dossier-legislatif/ppl24-661.html).

2. Official National Assembly dossier (https://www.assemblee-nationale.fr/dyn/17/dossiers/fin_de_vie_17e): Confirms the CMP resulted in a "Désaccord" (disagreement/failure), the National Assembly adopted a text in nouvelle lecture on June 30, 2026 (T.A. n° 323), and the bill was then transmitted to the Senate for nouvelle lecture (n° 814). The legislative process was still ongoing as of the July 1, 2026 deadline [https://www.assemblee-nationale.fr/dyn/17/dossiers/fin_de_vie_17e](https://www.assemblee-nationale.fr/dyn/17/dossiers/fin_de_vie_17e).

Why this is NO:
- The bill was NOT passed in identical terms by both chambers (the Senate had rejected it and the process returned to the Senate for another reading).
- The "dernier mot" (final word) procedure was NOT completed: under Article 45 of the Constitution, after a failed CMP, the National Assembly can only have the final word AFTER a further "nouvelle lecture" in each chamber. As of July 1, 2026, the Senate's nouvelle lecture had not yet taken place (scheduled for July 7–8, 2026), so the National Assembly's final vote could only occur later [https://www.senat.fr/dossier-legislatif/ppl24-661.html](https://www.senat.fr/dossier-legislatif/ppl24-661.html)[https://www.assemblee-nationale.fr/dyn/17/dossiers/fin_de_vie_17e](https://www.assemblee-nationale.fr/dyn/17/dossiers/fin_de_vie_17e).
- The bill had NOT been transmitted to the President of the Republic for promulgation, which the resolution criteria explicitly require for "definitively adopted" [https://www.senat.fr/dossier-legislatif/ppl24-661.html](https://www.senat.fr/dossier-legislatif/ppl24-661.html)[https://www.assemblee-nationale.fr/dyn/17/dossiers/fin_de_vie_17e](https://www.assemblee-nationale.fr/dyn/17/dossiers/fin_de_vie_17e).

The resolution criteria's condition on the assisted-dying provisions (formerly Article 2) does not even need to be reached, because the antecedent for a YES — definitive adoption/transmission to the President by July 1, 2026 — never occurred. The bill was still undergoing readings, which the resolution criteria explicitly list as a NO condition ("The bill is still undergoing readings (third reading, CMP, etc.)").

Note: The two official sources show a minor discrepancy on the exact CMP date (the Senate dossier indicated the CMP around June 2, 2026, while the National Assembly dossier indicated a CMP disagreement with reports deposited June 2, 2026 / possibly convened May 19), but both agree the CMP FAILED and that definitive adoption had not occurred by July 1, 2026, so this does not affect the resolution.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-155. `7b536549-ccf6-5e10-92b6-d300b6c79bd4`

- Present date: `2026-05-02 21:57:55.551495`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Congress pass legislation fully funding ICE and CBP via reconciliation by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 1, 2026 (12:00 AM ET) and on or before June 1, 2026 (11:59 PM ET), the President of the United States signs into law legislation that provides new appropriations or budget authority specifically for both Immigration and Customs Enforcement (ICE) (https://en.wikipedia.org/wiki/U.S._Immigration_and_Customs_Enforcement) and Customs and Border Protection (CBP) (https://en.wikipedia.org/wiki/U.S._Customs_and_Border_Protection). This includes legislation passed via the budget reconciliation process or any other legislative vehicle.

The question resolves **No** if no such legislation is signed into law by 11:59 PM ET on June 1, 2026.

The April 30, 2026 DHS funding bill (which excluded ICE and CBP funding) does not count toward resolution.

**Resolution source:** Official government sources, including [congress.gov](https://www.congress.gov/) for enacted legislation and public law numbers, or official White House statements confirming the signing of such legislation.

**Pre-cutoff background**

On April 30, 2026, President Trump signed a bipartisan bill ending a 76-day partial shutdown of the Department of Homeland Security (DHS). This bill funded most DHS agencies—including TSA, the Coast Guard, FEMA, and the Secret Service—but explicitly excluded funding for [Immigration and Customs Enforcement (ICE)](https://en.wikipedia.org/wiki/U.S._Immigration_and_Customs_Enforcement) and [Customs and Border Protection (CBP)](https://en.wikipedia.org/wiki/U.S._Customs_and_Border_Protection), which includes the Border Patrol [Trump signs bill funding DHS, ending record-breaking 76-day ...](https://www.cbsnews.com/news/dhs-shutdown-house-vote/).

ICE and CBP are currently operating under funding provided by last year's "One Big Beautiful Bill Act," so their operations were not interrupted by the shutdown [Trump signs bill funding DHS, ending record-breaking 76-day ...](https://www.cbsnews.com/news/dhs-shutdown-house-vote/). However, that funding is temporary, and Congress has initiated a budget reconciliation process to provide new, multi-year funding for these agencies.

During the week of April 30, 2026, both chambers of Congress adopted a budget resolution instructing committees to draft legislation funding ICE and Border Patrol for three years via the reconciliation process, which allows Republicans to bypass Democratic opposition in the Senate [Trump signs bill funding DHS, ending record-breaking 76-day ...](https://www.cbsnews.com/news/dhs-shutdown-house-vote/) [Trump signs bill to fund DHS after lengthy shutdown over ICE ...](https://www.reuters.com/legal/government/house-republicans-undecided-dhs-funding-secret-service-tsa-pressure-action-2026-04-30/). President Trump has publicly stated he wants this reconciliation package on his desk by June 1, 2026 [Trump signs bill funding DHS, ending record-breaking 76-day ...](https://www.cbsnews.com/news/dhs-shutdown-house-vote/). Republicans are hoping to pass this legislation in May 2026 [Trump signs bill to fund DHS after lengthy shutdown over ICE ...](https://www.reuters.com/legal/government/house-republicans-undecided-dhs-funding-secret-service-tsa-pressure-action-2026-04-30/).

Key uncertainties include: internal Republican disagreements between House and Senate over funding levels and policy riders; the compressed legislative timeline; and potential procedural obstacles in the reconciliation process. The reconciliation bill must go through committee markups, floor votes in both chambers, and likely a conference process—all within roughly one month.

**Exact later resolution packet**

The question resolves NO. It required that, between May 1 and June 1, 2026 (11:59 PM ET), the President sign into law legislation providing new appropriations/budget authority for BOTH ICE and CBP (e.g., the reconciliation package).

Timeline of events found:
- After the April 30, 2026 DHS funding bill (which explicitly excluded ICE and CBP), Republicans pursued a budget reconciliation package to fund ICE and Border Patrol. Senate Republicans unveiled a ~$72 billion reconciliation package on May 5, 2026, and committees marked it up in early/mid-May.
- Trump set a self-imposed June 1, 2026 deadline to get the bill to his desk.
- However, the bill stalled. On May 21, 2026, both chambers left Washington for the Memorial Day recess WITHOUT voting on the reconciliation package, amid GOP backlash over a $1.8 billion "anti-weaponization" fund and White House ballroom/security provisions. The vote was postponed until after the recess (reported as June 8). [b4491f]
- The CBS News article (updated May 21, 2026) explicitly states: "The developments mean lawmakers will all but certainly miss a deadline imposed by Mr. Trump to get the reconciliation bill on his desk by June 1." Senate Majority Leader John Thune said the chamber would "pick up where we left off" upon return — meaning no vote, let alone a signing, occurred before June 1. [8eeb33]

Because the reconciliation bill (the only vehicle providing new funding for both ICE and CBP in this window) was not even passed by both chambers before June 1, 2026, no such legislation was signed into law by the President within the resolution window. The April 30, 2026 DHS funding bill is explicitly excluded by the resolution criteria and in any case excluded ICE/CBP funding.

Therefore the question resolves NO (0).

Key sources:
- localnewslive.com (May 21, 2026): vote delayed until after Memorial Day recess; bill not yet signed [b4491f]
- CBS News (May 21, 2026): lawmakers "all but certainly miss" the June 1 deadline; recess with no vote [8eeb33]

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-156. `d6290ca7-6c3f-562b-9ddc-667112a22f3a`

- Present date: `2026-05-03 12:47:52.141344`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the 79th World Health Assembly formally adopt the Pathogen Access and Benefit-Sharing (PABS) system annex to the WHO Pandemic Agreement by 23 May 2026?

**Resolution criteria**

This question resolves **Yes** if the 79th World Health Assembly (18–23 May 2026, Geneva) formally adopts the PABS system annex to the WHO Pandemic Agreement. "Formally adopt" means the WHA passes a resolution or decision—whether by consensus or by vote—that specifically adopts the PABS system annex as part of the WHO Pandemic Agreement framework. This is distinct from the broader Pandemic Agreement itself, which was already adopted in May 2025; this question concerns only the PABS system annex that was deferred for further negotiation.

This question resolves **No** if:
- The WHA concludes on or before 23 May 2026 (23:59 UTC) without formally adopting the PABS annex;
- The WHA adopts the broader Pandemic Agreement text or amendments but does not separately adopt the PABS annex;
- The WHA defers or refers the PABS annex for further negotiation; or
- The PABS annex is presented but not put to a formal adoption decision.

**Resolution source:** Official WHO 79th World Health Assembly documents, meeting records, resolutions, and decisions, available at https://apps.who.int/gb/e/e_wha79.html, or official WHO press releases and news items at https://www.who.int/news. Resolution will be determined by 1 June 2026 (23:59 UTC).

**Pre-cutoff background**

The WHO Pandemic Agreement was adopted by the World Health Assembly in May 2025, but the Pathogen Access and Benefit-Sharing (PABS) system annex—a core component intended to ensure the rapid sharing of pathogens with pandemic potential and the equitable distribution of benefits such as vaccines, therapeutics, and diagnostics—was deferred for further negotiation [https://www.who.int/news/item/23-01-2026-countries-progress-negotiations-in-support-of-who-pandemic-agreement](https://www.who.int/news/item/23-01-2026-countries-progress-negotiations-in-support-of-who-pandemic-agreement).

An Intergovernmental Working Group (IGWG) was established to negotiate the PABS annex text. As of January 2026, Member States were engaged in text-based negotiations, with emerging consensus in some areas but complex issues remaining [https://www.who.int/news/item/23-01-2026-countries-progress-negotiations-in-support-of-who-pandemic-agreement](https://www.who.int/news/item/23-01-2026-countries-progress-negotiations-in-support-of-who-pandemic-agreement). By March 2026, Member States agreed to extend negotiations, with key sticking points including the definition and distribution of benefits, contractual arrangements, and governance matters [https://www.who.int/news/item/28-03-2026-who-member-states-agree-to-extend-negotiations-on-key-annex-to-the-pandemic-agreement](https://www.who.int/news/item/28-03-2026-who-member-states-agree-to-extend-negotiations-on-key-annex-to-the-pandemic-agreement). A final negotiating session was scheduled for 27 April–1 May 2026, with the goal of presenting the completed text to the 79th World Health Assembly [https://www.who.int/news/item/28-03-2026-who-member-states-agree-to-extend-negotiations-on-key-annex-to-the-pandemic-agreement](https://www.who.int/news/item/28-03-2026-who-member-states-agree-to-extend-negotiations-on-key-annex-to-the-pandemic-agreement).

As of 1 May 2026 (UTC), the IGWG's final negotiating session (27 April–1 May 2026) has just concluded or is concluding. It remains uncertain whether negotiators reached agreement on the outstanding issues. The United States withdrew from WHO in January 2025, removing a major player from negotiations but also potentially simplifying some dynamics. The 79th World Health Assembly is scheduled for 18–23 May 2026 in Geneva, Switzerland.

Status of IGWG negotiations as of 1 May 2026 (UTC): The seventh and final session of the IGWG (27 April–1 May 2026) was the last scheduled opportunity for negotiators to finalize the PABS annex text before the WHA [https://www.who.int/news/item/28-03-2026-who-member-states-agree-to-extend-negotiations-on-key-annex-to-the-pandemic-agreement](https://www.who.int/news/item/28-03-2026-who-member-states-agree-to-extend-negotiations-on-key-annex-to-the-pandemic-agreement). Whether this session produced a consensus text is the key determinant of whether the WHA will be in a position to adopt the annex.

**Exact later resolution packet**

The question asked whether the 79th World Health Assembly (18–23 May 2026) would formally adopt the Pathogen Access and Benefit-Sharing (PABS) system annex to the WHO Pandemic Agreement by 23 May 2026. It resolves NO.

Key evidence:
- The official WHO news release dated 1 May 2026 ("WHO Member States agree to extend negotiations on Pathogen Access and Benefit Sharing annex," https://www.who.int/news/item/01-05-2026-who-member-states-agree-to-extend-negotiations-on-pathogen-access-and-benefit-sharing-annex) confirms that the IGWG's final negotiating session did NOT produce a consensus text. Member States agreed more time was needed; the Assembly was to be asked to continue the IGWG's work, with the outcome submitted to the next Assembly in May 2027 (or earlier via a possible special session in 2026). The IGWG scheduled its next meeting for 6–17 July 2026 [a01a48].
- This means the consensus text required for WHA79 adoption did not exist by the time the Assembly convened, so the WHA was not in a position to adopt the annex.
- Corroborating sources: a WHA79 wrap-up summary states "Pandemic Agreement: the PABS Annex timeline confirmed for consideration at WHA80 in May 2027," and a Health Policy Watch / Devex / BMJ report ("WHO fails to agree final part of pandemic agreement") confirm the annex missed the WHA79 submission and negotiations were extended.

Because the WHA79 concluded on 23 May 2026 without formally adopting the PABS annex—and instead deferred/extended negotiations to a future session (WHA80, 2027, or an earlier special session)—the question resolves NO per its resolution criteria, which explicitly state a NO resolution if "the WHA defers or refers the PABS annex for further negotiation."

This is clearly distinct from the broader WHO Pandemic Agreement, which was already adopted at the 78th WHA in May 2025 (resolution WHA78.1, https://apps.who.int/gb/ebwha/pdf_files/WHA78/A78_R1-en.pdf). The PABS annex—the specific subject of this question—was not adopted at WHA79.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-157. `29202589-68cc-5f7e-8bf0-a923acdb2d07`

- Present date: `2026-05-14 06:39:47.263369`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the California Department of Insurance announce an enforcement action against any insurer other than State Farm for LA wildfire claims handling between May 12, 2026 and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the California Department of Insurance (CDI) publicly announces, on or after May 12, 2026 and on or before July 1, 2026 (11:59 PM Pacific Time), a formal enforcement action against any insurer other than State Farm General Insurance Company, related to the handling of claims from the January 2025 Los Angeles wildfires.

**Definitions:**
- **Insurer**: An entity licensed by the California Department of Insurance to transact insurance business in California (see https://interactive.web.insurance.ca.gov/companyprofile/companyprofile?event=companyProfile).
- **Enforcement action**: A formal regulatory action by CDI such as a fine, penalty, cease-and-desist order, license suspension or revocation, accusation, order to show cause, or consent order. Informal actions such as letters of inquiry, warnings, or voluntary compliance agreements do not qualify.
- **LA wildfire claims**: Claims arising from the January 2025 Los Angeles wildfires, including the Palisades and Eaton fires.

This question explicitly **excludes** the May 4, 2026 enforcement action against State Farm General Insurance Company announced via CDI press release (https://www.insurance.ca.gov/0400-news/0100-press-releases/2026/release019-2026.cfm).

**Resolution source**: The CDI Newsroom and Press Releases page at https://www.insurance.ca.gov/0400-news/index.cfm or the Governor's official newsroom at https://www.gov.ca.gov/newsroom/. If CDI announces such an action via an official press release or public statement posted on either site, the question resolves Yes. If no such announcement appears by 11:59 PM Pacific Time on July 1, 2026, the question resolves No.

**Pre-cutoff background**

On May 4, 2026, California Insurance Commissioner Ricardo Lara announced a major enforcement action against State Farm General Insurance Company after an expedited Market Conduct Examination uncovered 398 violations of the Unfair Insurance Claims Practices Act related to the January 2025 Los Angeles wildfires (Eaton and Palisades fires) [Governor Newsom warns insurance companies after major state ...](https://www.gov.ca.gov/2026/05/04/governor-newsom-warns-insurance-companies-after-major-state-enforcement-against-state-farm/). The California Department of Insurance (CDI) filed an "Accusation and Order to Show Cause" against State Farm, seeking up to $4 million in penalties and potentially a suspension of State Farm's license for up to one year. Investigators found unlawful behavior in nearly half of the sampled claims, including slow and inadequate investigations, underpayment of claims, and low settlement offers.

Governor Newsom simultaneously issued a public warning to the broader insurance industry, stating that other insurers may face similar legal action if they illegally delay or deny claims from LA wildfire survivors [Governor Newsom warns insurance companies after major state ...](https://www.gov.ca.gov/2026/05/04/governor-newsom-warns-insurance-companies-after-major-state-enforcement-against-state-farm/). CDI has reported recovering more than $280 million from all insurance companies for wildfire survivors since January 2025, suggesting ongoing scrutiny of multiple carriers. Whether CDI will pursue formal enforcement actions against additional insurers depends on the findings of any ongoing investigations, political momentum, and agency resources.

As of May 13, 2026, no additional enforcement actions against other insurers for LA wildfire claims handling have been publicly announced beyond the State Farm action.

**Exact later resolution packet**

The question resolves NO. It asks whether the California Department of Insurance (CDI) publicly announced, on or after May 12, 2026 and on or before July 1, 2026 (11:59 PM PT), a FORMAL enforcement action against an insurer OTHER than State Farm General Insurance Company, related to handling of January 2025 LA wildfire (Eaton/Palisades) claims, via the CDI Newsroom or the Governor's newsroom.

Evidence:

1. The only 2026 LA-wildfire enforcement action found was against State Farm, announced May 4, 2026 (CDI release019-2026, and the Governor's May 4, 2026 warning post). This is explicitly EXCLUDED by the resolution criteria.

2. There IS a second insurer that faced a CDI enforcement action for LA wildfire claims — the California FAIR Plan. However, that action (an "Order to Show Cause" accusing the FAIR Plan of illegally denying smoke-damage claims) was filed/announced on JULY 30, 2025 (CDI release054-2025) — nearly a year BEFORE the question window opened. The 2025 press-release index lists it under "July 30, 2025," and a February 2, 2026 CDI release (release005-2026) references it as an already-existing action linking back to the 2025 press release [62cc2f]. Because the FAIR Plan action predates May 12, 2026, it does not satisfy the requirement that the announcement occur "on or after May 12, 2026." (This also explains why PBS and ABC7 described State Farm as the "second" insurer to face legal action — the FAIR Plan was first, back in 2025.)

3. A review of the complete CDI 2026 press-release archive shows the ONLY releases dated within the May 12 – July 1, 2026 window were: Release 020-2026 (May 27, 2026) about a staged-crash insurance-fraud scheme, and Release 021-2026 (June 12, 2026) about safeguarding Californians' financial future from future insurance crises [93381b, c8d366]. Neither is a formal enforcement action against an insurer for LA wildfire claims.

4. The Governor's official newsroom (gov.ca.gov/newsroom) contained no announcement of any enforcement action against an insurer (other than the excluded May 4 State Farm action) for LA wildfire claims during the window [b54ede].

Because no qualifying formal enforcement action against a non-State-Farm insurer for LA wildfire claims was announced by CDI (or the Governor) between May 12 and July 1, 2026, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-158. `2a57a88c-7bca-5b25-8fce-922c1d0e9df8`

- Present date: `2026-05-03 10:36:31.558521`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Germany officially announce a formal arrangement to supply the PCK Schwedt refinery via the Gdansk-to-Schwedt pipeline route between May 2 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 2, 2026 (00:00 UTC) and by June 1, 2026 (23:59 UTC), an official announcement is made confirming a formal arrangement to supply the PCK Schwedt refinery with crude oil via the Gdańsk-to-Schwedt pipeline route. 

**"Officially announce"** means a public statement, press release, or confirmed on-the-record comment by any of the following:
- The German Federal Ministry for Economic Affairs and Climate Action ([BMWK](https://www.bmwk.de/Navigation/EN/Home/home.html))
- The German Federal Government spokesperson (Bundespresseamt)
- The Polish Ministry of Climate and Environment ([gov.pl](https://www.gov.pl/web/climate))
- PERN S.A. (the Polish pipeline operator)

**"Formal arrangement to supply"** means any of: a signed contract, a memorandum of understanding (MOU), or an official declaration by one of the bodies listed above that oil deliveries via the Gdańsk-to-Schwedt route have commenced or will commence under agreed terms. Statements limited to "ongoing discussions," "exploring options," or "technical readiness" do **not** qualify.

**"Gdańsk-to-Schwedt pipeline route"** refers to the pipeline infrastructure connecting the [port of Gdańsk](https://en.wikipedia.org/wiki/Port_of_Gda%C5%84sk) in Poland to the PCK refinery in Schwedt, Germany, via the northern spur of the Druzhba pipeline system operated by [PERN](https://en.wikipedia.org/wiki/PERN).

**Resolution sources:** Official press releases from [BMWK](https://www.bmwk.de/Navigation/EN/Press/press.html) or credible international news agencies including [Reuters](https://www.reuters.com/), [Associated Press](https://apnews.com/), [Bloomberg](https://www.bloomberg.com/), or [Financial Times](https://www.ft.com/).

If no qualifying announcement is made by 23:59 UTC on June 1, 2026, this question resolves **No**.

**Pre-cutoff background**

The [PCK Schwedt refinery](https://en.wikipedia.org/wiki/PCK_refinery) in Brandenburg, Germany, is a critical energy facility supplying most of the fuel for the Berlin metropolitan area. Following Russia's announcement that it would halt Kazakh crude oil transit via the [Druzhba pipeline](https://en.wikipedia.org/wiki/Druzhba_pipeline) effective May 1, 2026, the refinery faces a significant supply disruption [Germany in talks with Poland over oil deliveries after Russia says to ...](https://www.reuters.com/business/energy/germany-talks-with-poland-over-oil-deliveries-after-russia-says-halt-supplies-2026-04-28/).

As of April 29, 2026, the state of Brandenburg reported that up to 80% of crude oil supplies for PCK Schwedt are secured for May 2026 through existing contracts and alternative sources [Germany reassures on oil supplies as it seeks alternatives for Schwedt](https://www.reuters.com/business/energy/germany-reassures-oil-supplies-it-seeks-alternatives-schwedt-2026-04-29/). However, the remaining shortfall—previously filled by Kazakh crude transiting Russia—must be replaced.

Germany is in active talks with Poland to explore using the [port of Gdańsk](https://en.wikipedia.org/wiki/Port_of_Gda%C5%84sk) and the existing pipeline infrastructure connecting Gdańsk to Schwedt (part of the northern branch of the Druzhba system running through Poland) as an alternative supply route. As of April 28, 2026, a spokesperson for the German Federal Ministry for Economic Affairs and Climate Action (BMWK) confirmed ongoing discussions but declined to provide details. Poland's energy ministry stated it has the technical capacity to handle such deliveries, but actual implementation depends on operational, logistical, and market factors [Germany in talks with Poland over oil deliveries after Russia says to ...](https://www.reuters.com/business/energy/germany-talks-with-poland-over-oil-deliveries-after-russia-says-halt-supplies-2026-04-28/). No formal agreement had been announced as of May 2, 2026 [Germany reassures on oil supplies as it seeks alternatives for Schwedt](https://www.reuters.com/business/energy/germany-reassures-oil-supplies-it-seeks-alternatives-schwedt-2026-04-29/).

**Exact later resolution packet**

The question resolves NO. It requires that, between May 2 and June 1, 2026, one of the four authorized bodies (BMWK, German Federal Government spokesperson, Polish Ministry of Climate and Environment, or PERN S.A.) officially announces a FORMAL arrangement (signed contract, MOU, or official declaration that deliveries via the Gdansk-to-Schwedt route have commenced/will commence under agreed terms) to supply PCK Schwedt via the Gdansk-to-Schwedt pipeline route, as reported by a BMWK press release or Reuters/AP/Bloomberg/FT. Mere "ongoing discussions," "exploring options," or "technical readiness" do not qualify.

Key evidence:
- The Reuters article of April 28, 2026 (pre-window) confirmed only that Germany was "in talks" with Poland and that supply contracts are a matter for the companies involved, with the government "closely accompanying the process" [1c44a3]. No formal agreement existed as of late April.
- The Reuters article of May 11, 2026 (within the window) explicitly states that "Berlin has been in talks with Poland about possibly raising deliveries" — i.e., still only ongoing discussions, with no signed contract, MOU, or official declaration of commenced/agreed deliveries via the Gdansk route [054014]. https://www.reuters.com/business/world-at-work/germany-extends-employment-guarantee-schwedt-pck-refinery-2026-05-11/
- German regional reporting throughout/after the window corroborates the absence of any deal: the Märkische Allgemeine Zeitung (MAZ) headline "Öl aus den USA, aber noch kein Durchbruch mit Polen" ("Oil from the USA, but still no breakthrough with Poland") and a follow-up "Auch nach einem Monat noch kein Durchbruch für PCK" ("Even after a month, still no breakthrough for PCK") — meaning that around the June 1 cutoff there was still no agreement on the Gdansk/Poland route (https://www.maz-online.de/politik/ and https://www.maz-online.de/politik/regional/oel-aus-den-usa-aber-noch-kein-durchbruch-mit-polen-...).
- No Reuters, AP, Bloomberg, FT, or BMWK source reporting a signed contract/MOU/official commencement declaration for the Gdansk-to-Schwedt route within the May 2–June 1, 2026 window could be found despite extensive searching in English and German.

Since no qualifying official announcement of a formal arrangement was made by an authorized body and reported by an authorized source within the window, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-159. `d3f2bbc3-ac28-572f-a5b1-b6b5968d537d`

- Present date: `2026-05-03 02:52:10.933746`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Figure AI announce a commercial deployment of Figure 03 robots at a customer facility by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 1, 2026, and by 23:59 UTC on June 1, 2026, there is a public announcement — either via Figure AI's official press release page (https://www.figure.ai/news) or via reporting from a major credible news outlet (e.g., Reuters, Bloomberg, AP, Forbes, TechCrunch) — confirming that at least one Figure 03 robot has been commercially deployed at a customer facility.

Key definitions:
- **"Figure 03"**: Figure AI's third-generation humanoid robot, also referred to as "F.03," as introduced in October 2025 (https://www.figure.ai/news/introducing-figure-03). Earlier models (Figure 01, Figure 02) do not qualify.
- **"Commercial deployment"**: The active, ongoing operation of at least one Figure 03 unit performing productive tasks (not merely a demo, tour, or temporary exhibition) at a customer's site. A confirmed sale or lease where the robot is physically present and operational at the customer location qualifies.
- **"Customer facility"**: A location owned, leased, or operated by an entity other than Figure AI. Figure AI's own offices, labs, manufacturing plants (including BotQ), and test facilities are excluded. Joint ventures where Figure AI is the primary operator of the facility are also excluded.

The qualifying announcement or deployment must occur on or after May 1, 2026 (00:00 UTC) and by June 1, 2026 (23:59 UTC). If no such announcement exists by that deadline, the question resolves **No**.

**Primary resolution source**: Figure AI's official news page at https://www.figure.ai/news. Secondary sources include credible reporting from Reuters, Bloomberg, AP, Forbes, or TechCrunch.

**Pre-cutoff background**

Figure AI is a leading humanoid robotics startup that introduced the Figure 03 (F.03) robot in October 2025. The company previously completed a successful 11-month deployment of its earlier Figure 02 model at BMW Group Plant Spartanburg, where it contributed to the production of 30,000 cars [News - Figure AI](https://www.figure.ai/news). As of late April 2026, Figure AI is rapidly scaling Figure 03 production, with its most recent press release titled "Ramping Figure 03 Production" (April 29, 2026) focused on manufacturing scale-up at its BotQ facility [News - Figure AI](https://www.figure.ai/news). Forbes reported on April 23, 2026 that Figure is doubling Figure 03 shipments every month, though it did not confirm specific customer deployments of the Figure 03 model [This Humanoid Robot Maker Is Doubling Deliveries Every Month](https://www.forbes.com/sites/johnkoetsier/2026/04/23/figure-is-doubling-humanoid-robot-deliveries-every-month/). While production is ramping quickly, there is no public confirmation as of May 1, 2026 that a Figure 03 unit has been commercially deployed at an external customer's facility — the company's newsroom shows no such announcement [News - Figure AI](https://www.figure.ai/news). This creates meaningful uncertainty about whether such a deployment will be announced within May 2026.

**Exact later resolution packet**

The question resolves NO. It requires a public announcement between May 1, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC) confirming that at least one Figure 03 (F.03) robot has been COMMERCIALLY DEPLOYED — defined as the active, ongoing operation of at least one Figure 03 unit performing productive tasks (not a demo/tour/exhibition) — at an external customer's facility.

Survey of all candidate events in the window:

1) Catalyst Brands agreement (announced May 26, 2026 on figure.ai/news, "Figure Signs Agreement with Catalyst Brands to Scale Humanoid Operations," and on JCPenney/Catalyst's newsroom). This is the closest candidate but fails the criteria on two grounds: (a) It is a commercial AGREEMENT/partnership to deploy robots in the future, using future/intent-tense language ("agreement... to deploy," "collaboration starts at," "the partnership will begin," "the pair aim to automate," "as the partnership begins... will identify the optimal use cases"). It does not confirm that robots are already physically present and operationally performing productive tasks at Catalyst's Reno, Nevada distribution center [03a931, 427734, c1c380, 0bc9ed, a9ee5e]. The humanoid.guide coverage explicitly says Catalyst "plans to introduce" the robots and that "the announcement did not specify how many robots will be deployed, how quickly the Reno program will expand" [c1c380]. (b) The announcements refer only to "Figure humanoids," "Figure's next-gen robots," or "Figure's humanoids" and do NOT explicitly identify the units as the "Figure 03"/"F.03" model, which the resolution criteria require [03a931, 427734, 0bc9ed].

2) The 200-hour / package-sorting "marathon" (starting ~May 13, 2026) involving three Figure 03 units. This was a Figure-run live test/demonstration of the Figure 03 platform, not a commercial deployment at an external customer's facility, so it is explicitly excluded by the criteria ("not merely a demo... at a customer's site").

3) BMW Spartanburg — the celebrated 30,000-car deployment used Figure 02, which was retired after the 11-month run (announced earlier in 2026); it does not qualify as a Figure 03 deployment. The lone iFactory blog claiming "Figure 03 at BMW Spartanburg" with Q3 2024 dates [36e109] is internally inconsistent (Figure 03 was only introduced October 2025) and is not a credible/authoritative source (not one of the specified outlets and contradicts BMW's own statements and Figure's news page).

4) BMW Group Germany — the BMW PressClub release states only that "The BMW Group and Figure are currently evaluating additional use cases for deploying the Figure 03 robot." This is evaluation, not an active deployment, and the German pilot referenced a different robot (Hexagon's AEON) [7681aa].

No announcement on Figure AI's official news page (figure.ai/news) or from Reuters, Bloomberg, AP, Forbes, or TechCrunch within the window confirms a Figure 03 robot physically present and operational performing productive tasks at a customer facility. Therefore the question resolves NO.

Key URLs:
- https://www.figure.ai/news/figure-signs-agreement-with-catalyst-brands
- https://corporate.jcpenney.com/2026/05/26/catalyst-brands-taps-figure-ai-for-humanoid-automation/
- https://humanoid.guide/catalyst-brands-deploys-figure-ai-humanoid-robots-in-reno-dc/
- https://roboticsandautomationnews.com/2026/05/27/figure-signs-commercial-agreement-with-catalyst-brands-to-deploy-humanoid-robots-in-logistics-operations/101950/
- https://www.press.bmwgroup.com/global/article/detail/T0455864EN/...

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-160. `5a84fa61-45c5-5b08-ab54-64d971c1db09`

- Present date: `2026-05-12 17:52:07.984886`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the United States conduct a Freedom of Navigation Operation (FONOP) within 12 nautical miles of Scarborough Shoal between May 10, 2026, and July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 10, 2026, and before 23:59 UTC on June 30, 2026, the United States Navy conducts a Freedom of Navigation Operation (FONOP) within 12 nautical miles of Scarborough Shoal, as officially confirmed by the U.S. Department of Defense or U.S. Navy.

**Definitions and sources:**

- **Freedom of Navigation Operation (FONOP):** An operation conducted under the [U.S. Freedom of Navigation Program](https://policy.defense.gov/ousdp-offices/fon/) in which a U.S. naval vessel transits through waters to challenge excessive maritime claims. The operation must be explicitly identified as a FONOP (or "freedom of navigation operation") by U.S. official sources—joint patrols, maritime cooperative activities, or routine transits do not qualify.

- **Scarborough Shoal:** The feature located at approximately 15°11'N, 117°46'E in the South China Sea, as described in the [Wikipedia article on Scarborough Shoal](https://en.wikipedia.org/wiki/Scarborough_Shoal) and the [CSIS Asia Maritime Transparency Initiative page](https://amti.csis.org/scarborough-shoal/). "Within 12 nautical miles" refers to 12 nautical miles measured from the feature's baseline, consistent with the territorial sea definition under [UNCLOS](https://en.wikipedia.org/wiki/United_Nations_Convention_on_the_Law_of_the_Sea).

- **Resolution source:** Official press releases from the [U.S. Navy 7th Fleet](https://www.c7f.navy.mil/) or the [U.S. Department of Defense](https://www.defense.gov/), or credible reporting from major outlets (Reuters, AP, Stars and Stripes, USNI News, Naval News) confirming a FONOP within 12 nautical miles of Scarborough Shoal.

If no such FONOP is confirmed by 23:59 UTC on June 30, 2026, this question resolves as **No**.

**Pre-cutoff background**

The United States periodically conducts Freedom of Navigation Operations (FONOPs) in the South China Sea to challenge what it considers excessive maritime claims. Scarborough Shoal (approximately 15°11'N, 117°46'E) is a disputed feature in the South China Sea claimed by China, the Philippines, and Taiwan.

**Recent U.S. operations near Scarborough Shoal:**
- In August 2025, the USS Higgins (DDG 76) conducted a FONOP near Scarborough Shoal. China's Southern Theater Command claimed it "warned and expelled" the vessel, which the U.S. 7th Fleet rejected as false [7th Fleet denies China drove US warship away from South ...](https://www.stripes.com/branches/navy/2025-08-14/higgins-scarborough-china-phillipines-7th-fleet-18758627.html) [U.S. Navy Holds South China Sea FONOP at Scarborough Shoal](https://www.navalnews.com/naval-news/2025/08/u-s-navy-holds-south-china-sea-fonop-at-scarborough-shoal/).
- In January 2026, the USS John Finn (DDG-113) conducted joint maritime drills with Philippine Navy and Coast Guard vessels near Scarborough Shoal. This was characterized as a "Maritime Cooperative Activity" (MCA), not a FONOP [U.S. Destroyer Drills with Philippine Forces Near Scarborough Shoal](https://news.usni.org/2026/01/28/u-s-destroyer-drills-with-philippine-forces-near-scarborough-shoal).
- In February 2026, Japan, Philippine, and U.S. forces conducted a Multilateral Maritime Cooperative Activity in the South China Sea.
- From April 20 to May 8, 2026, the annual Balikatan exercises were held, involving the Philippines, the U.S., and allies including Australia, Japan, Canada, New Zealand, and France [China holds naval, air patrols near Scarborough Shoal as ... - Reuters](https://www.reuters.com/world/china/china-conducts-combat-readiness-patrols-scarborough-shoal-2026-04-30/).
- On April 30, 2026, China conducted "combat readiness patrols" near Scarborough Shoal in response to Balikatan, characterizing allied exercises as provocations [China holds naval, air patrols near Scarborough Shoal as ... - Reuters](https://www.reuters.com/world/china/china-conducts-combat-readiness-patrols-scarborough-shoal-2026-04-30/).
- In April 2026, Australia, Canada, and the U.S. conducted multilateral operations in the South China Sea [Australia, Canada, and U.S. conduct multilateral operations in ...](https://www.navy.mil/Press-Office/News-Stories/display-news/Article/4464141/australia-canada-and-us-conduct-multilateral-operations-in-south-china-sea/).

**Key context:** Joint patrols and MCAs are distinct from FONOPs. A FONOP within 12 nautical miles specifically challenges territorial sea claims and is a more provocative action. The last confirmed FONOP at Scarborough Shoal was in August 2025 [U.S. Navy Holds South China Sea FONOP at Scarborough Shoal](https://www.navalnews.com/naval-news/2025/08/u-s-navy-holds-south-china-sea-fonop-at-scarborough-shoal/). U.S. strategic attention is also partly directed toward the Middle East, with ongoing operations against Iran [7th Fleet denies China drove US warship away from South ...](https://www.stripes.com/branches/navy/2025-08-14/higgins-scarborough-china-phillipines-7th-fleet-18758627.html), which may affect force availability and willingness to escalate in the South China Sea.

**Exact later resolution packet**

The question resolves NO. It required the U.S. Navy to conduct an operation explicitly identified as a Freedom of Navigation Operation (FONOP) within 12 nautical miles of Scarborough Shoal, officially confirmed by U.S. DoD/Navy (or credibly reported by Reuters, AP, Stars and Stripes, USNI News, or Naval News), between May 10, 2026 and 23:59 UTC June 30, 2026. No such FONOP occurred in that window.

Key evidence:

1. The only significant U.S. naval activity near Scarborough Shoal during the window was a joint patrol from May 26–30, 2026 involving the U.S. Coast Guard cutter USCGC Midgett (WMSL-757) and Philippine vessels. USNI News (May 31, 2026) explicitly characterized this as a "maritime cooperative activity"/"joint patrol," NOT a FONOP, and reported the activity took place roughly 35–40 nautical miles from Scarborough Shoal — well outside the 12-nm territorial sea [5d1af6]. The question's resolution criteria state that "joint patrols, maritime cooperative activities, or routine transits do not qualify." Source URL: https://news.usni.org/2026/05/31/u-s-coast-guard-patrols-near-scarborough-shoal-with-philippine-forces-amid-concerns-of-potential-chinese-build-up

2. A review of the official U.S. 7th Fleet news feed (https://www.c7f.navy.mil/Media/News/) for the May 10, 2026–July 1, 2026 period showed only "Maritime Cooperative Activity" press releases (dated around May 30, June 19, and June 29, 2026) with the Philippines/U.S. Coast Guard — no FONOP near Scarborough Shoal was announced [40e637].

3. Reuters coverage of Scarborough Shoal throughout June 2026 focused on Chinese activity (e.g., "China conducts patrols around Scarborough Shoal," June 29–30, 2026, https://www.reuters.com/world/china-conducts-patrols-around-scarborough-shoal-disputed-south-china-sea-2026-06-30/; and a floating platform being removed, https://www.reuters.com/world/asia-pacific/philippines-says-floating-platform-removed-scarborough-shoal-2026-06-17/) and Philippine investigations of new structures — none reported a U.S. FONOP at the shoal.

4. All sources indicate the last confirmed FONOP at Scarborough Shoal was in August 2025 (USS Higgins, DDG-76), per Naval News (https://www.navalnews.com/naval-news/2025/08/u-s-navy-holds-south-china-sea-fonop-at-scarborough-shoal/) and USNI News (https://news.usni.org/2025/08/13/navy-denies-china-chased-off-u-s-warship-from-scarborough-shoal). No subsequent FONOP at the shoal was reported within the question's window.

Because no operation explicitly identified as a FONOP within 12 nm of Scarborough Shoal was confirmed by 23:59 UTC on June 30, 2026, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-161. `0d3ada70-cff5-5d35-9cd6-b0d91409ae98`

- Present date: `2026-05-14 01:40:54.192297`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-22T00:00:00`

**Question**

Will the PBoC cut the 1-year Loan Prime Rate (LPR) at or before its June 2026 fixing?

**Resolution criteria**

This question resolves **Yes** if the [PBoC](https://en.wikipedia.org/wiki/People%27s_Bank_of_China) announces a 1-year [Loan Prime Rate (LPR)](http://www.chinamoney.com.cn/english/bmklpr/) that is numerically lower than **3.00%** (the rate as of May 12, 2026) at any monthly LPR fixing announced on or after May 12, 2026 and no later than June 22, 2026, 17:00 China Standard Time (UTC+8).

A "cut" is defined as any numerical decrease from 3.00%, regardless of magnitude (e.g., a reduction to 2.95% or 2.90% would qualify).

The question resolves **No** if the 1-year LPR remains at 3.00% or higher at all fixings through and including the June 2026 fixing (expected around June 20, 2026).

**Resolution source:** The official LPR announcement published by the [National Interbank Funding Center (CFETS)](http://www.chinamoney.com.cn/english/bmklpr/) or the [PBoC's official LPR page](http://www.pbc.gov.cn/en/3688229/3688335/3883798/index.html). Alternatively, reporting from [Reuters](https://www.reuters.com/business/finance/china-leaves-lending-benchmarks-unchanged-11th-month-april-2026-04-20/) or Bloomberg covering the fixing outcome may be used.

**Pre-cutoff background**

The [People's Bank of China (PBoC)](https://en.wikipedia.org/wiki/People%27s_Bank_of_China) sets the [Loan Prime Rate (LPR)](http://www.chinamoney.com.cn/english/bmklpr/) on a monthly basis, typically around the 20th of each month. The 1-year LPR serves as the benchmark for general lending in China.

As of May 12, 2026, the 1-year LPR stands at **3.00%**, a level it has held for 11 consecutive months since the last cut in May 2025 (from 3.10% to 3.00%). The 5-year LPR is at 3.50%. The most recent fixing was on April 20, 2026, when rates were held steady as expected by all 20 participants in a Reuters survey.

China's economy grew 5% in Q1 2026, reducing urgency for immediate easing. However, Capital Economics forecasts 30 basis points of policy rate cuts by end-2026, implying cuts must begin soon. Complicating the picture, Middle East-driven energy price increases have introduced imported inflation pressures, while domestic growth still needs support. Bank net interest margin compression also constrains the PBoC's willingness to cut.

Within the resolution window, there are two upcoming LPR fixings: approximately May 20, 2026 and approximately June 20, 2026. Market consensus currently leans toward a hold at both, but the probability of a cut is non-trivial given the need to begin the easing cycle forecasters expect for H2 2026.

**Exact later resolution packet**

The question resolves NO (0).

The question asks whether the PBoC would announce a 1-year Loan Prime Rate (LPR) numerically lower than 3.00% at any fixing announced on or after May 12, 2026 and no later than June 22, 2026, 17:00 China Standard Time. Two fixings fell within this window: May 20, 2026 and June 22, 2026.

1) May 2026 fixing (May 20, 2026): Reuters reported "China leaves lending benchmarks unchanged for 12th month in May," stating explicitly that "The one-year loan prime rate (LPR) was kept at 3.00%, while the five-year LPR was unchanged at 3.50%." [869a46]

2) June 2026 fixing (June 22, 2026): Reuters reported "China keeps lending benchmark LPRs unchanged for 13th month in June," stating "The one-year loan prime rate (LPR) was kept at 3.00%, while the five-year LPR was unchanged at 3.50%." [343515]

3) The official National Interbank Funding Center (CFETS) LPR page confirms the LPR fixing dated 22/06/2026 shows the 1-year term rate at 3.00% (and 5-year at 3.50%) [625bc7].

Because the 1-year LPR remained at exactly 3.00% (not numerically lower) at every fixing through and including the June 2026 fixing, the "cut below 3.00%" condition was never triggered. Per the resolution criteria, "The question resolves No if the 1-year LPR remains at 3.00% or higher at all fixings through and including the June 2026 fixing." Therefore the resolution is NO.

Resolution source URLs:
- CFETS: http://www.chinamoney.com.cn/english/bmklpr/
- Reuters (June): https://www.reuters.com/world/asia-pacific/china-keeps-lending-benchmark-lprs-unchanged-13th-month-june-2026-06-22/
- Reuters (May): https://www.reuters.com/business/finance/china-leaves-lending-benchmarks-unchanged-12th-month-may-2026-05-20/

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-162. `10b89b51-e7de-5f14-8b00-29d0e1b627ba`

- Present date: `2026-05-03 10:17:08.649261`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the Canada Strong Fund Transition Office be formally established with a named head by June 1, 2026?

**Resolution criteria**

This question resolves YES if both of the following conditions are met on or after May 2, 2026, and no later than 11:59 PM UTC on June 1, 2026:

1. **Formally established**: The Canada Strong Fund Transition Office has been formally established, as evidenced by at least one of the following:
   - An Order in Council published in the Canada Gazette (https://gazette.gc.ca/),
   - An official press release or news release on Canada.ca (https://www.canada.ca/en/department-finance/news.html) or the Prime Minister's website (https://www.pm.gc.ca/en/news), or
   - An update to a Government of Canada organizational directory listing the Transition Office.

2. **Named head**: A specific individual has been publicly named as the head, lead, director, or equivalent chief officer of the Transition Office, as announced via one of the official sources listed above.

If either condition is not met by 11:59 PM UTC on June 1, 2026, the question resolves NO.

Note: Only announcements or appointments made on or after May 2, 2026 count toward resolution. Any establishment or naming that occurred before this date is excluded.

**Pre-cutoff background**

On April 27, 2026, Prime Minister Mark Carney announced the creation of the Canada Strong Fund, Canada's first national sovereign wealth fund, with an initial endowment of C$25 billion. As part of the Spring Economic Update 2026, the government stated it would establish a "dedicated Canada Strong Fund Transition Office" to lead targeted engagement with market participants and regulators and to "rapidly finalise the Fund" [Canada Strong Fund](https://www.canada.ca/en/department-finance/news/2026/04/canada-strong-fund.html).

As of May 2, 2026, no public announcement has been made regarding the formal establishment of the Transition Office or the appointment of its head. The government backgrounder indicated the fund would be finalized "in the coming months" but provided no specific timeline for standing up the Transition Office or naming its leader [Canada Strong Fund](https://www.canada.ca/en/department-finance/news/2026/04/canada-strong-fund.html).

Key sources:
- Department of Finance Canada backgrounder: https://www.canada.ca/en/department-finance/news/2026/04/canada-strong-fund.html
- PM announcement: https://www.pm.gc.ca/en/news/news-releases/2026/04/27/prime-minister-carney-announces-canada-strong-fund-canadas-first

**Exact later resolution packet**

The question resolves NO. It required BOTH (1) the formal establishment of the Canada Strong Fund Transition Office AND (2) the public naming of a specific individual as its head/lead/director/CEO, via official sources (gazette.gc.ca, canada.ca, or pm.gc.ca), occurring on or after May 2, 2026 and no later than 11:59 PM UTC June 1, 2026.

Key evidence against YES:
- The original April 27, 2026 announcements (pm.gc.ca and canada.ca/department-finance) only stated the government "will establish" a dedicated Canada Strong Fund Transition Office in the future — these predate May 2, 2026 and explicitly do not count toward resolution. They named no head.
- Most decisive: House of Commons Written Question Q-1226, submitted May 26, 2026, explicitly asks "With regard to the Canada Strong Fund Transition Office: (a) how will the position of Chief Executive Officer be selected, and who will make the final hiring decision..." The question was "Awaiting response," with the government's response not expected until September 21, 2026 [Q-1226 (45-1) - Written Questions - House of Commons of Canada](https://www.ourcommons.ca/written-questions/45-1/q-1226). The very fact that an MP was, on May 26, 2026, asking how the CEO would be selected confirms that no CEO/head had been named as of that date — well within the resolution window.
- I searched official sources (canada.ca, pm.gc.ca) and general news for any announcement between May 2 and June 1, 2026 naming a head of the Transition Office; none was found. The only canada.ca/pm.gc.ca content remains the original April 27 announcement of intent.

Since no specific individual was named as head of the Transition Office through an official source within the resolution window (and arguably the office itself was not yet formally stood up), condition (2) — and likely condition (1) — was not met. Per the resolution criteria, if either condition is not met by the deadline, the question resolves NO.

Sources:
- https://www.ourcommons.ca/written-questions/45-1/q-1226 [Q-1226 (45-1) - Written Questions - House of Commons of Canada](https://www.ourcommons.ca/written-questions/45-1/q-1226)
- https://www.pm.gc.ca/en/news/news-releases/2026/04/27/prime-minister-carney-announces-canada-strong-fund-canadas-first (April 27 announcement of intent, predates window)
- https://www.canada.ca/en/department-finance/news/2026/04/canada-strong-fund.html (April 27 backgrounder, predates window)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-163. `aabd7d8b-bc18-508e-b05d-eb1abaf01176`

- Present date: `2026-05-12 20:28:31.278681`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Iran's Supreme Leader approve an amnesty or pardon covering prisoners convicted of national security offenses between May 10 and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 10, 2026 and no later than July 1, 2026 (23:59 UTC), the Supreme Leader of Iran (currently Mojtaba Khamenei) approves an amnesty or pardon—upon recommendation of the Head of the Judiciary—that either:

1. Explicitly names "political prisoners," "security prisoners," or prisoners convicted of "crimes against national security" (جرائم امنیتی) as a covered category, **OR**
2. Is a general amnesty that is credibly reported by at least two major international news sources (e.g., [Reuters](https://www.reuters.com), [AP](https://apnews.com), [BBC](https://www.bbc.com)) or the Iranian judiciary's official news agency [Mizan Online](https://www.mizan.news/) or [IRNA](https://en.irna.ir/) as including individuals convicted under Articles 498–512 of Book Five of the Islamic Penal Code (crimes against national and external security), or equivalent charges such as "propaganda against the state" (تبلیغ علیه نظام) or "assembly and collusion against national security" (اجتماع و تبانی علیه امنیت ملی).

A general amnesty that does **not** specifically name or demonstrably include security/political offense categories does **not** suffice for Yes resolution. Routine individual pardons or prisoner exchanges with foreign governments also do not count; the announcement must be a formal amnesty or mass pardon decree.

The official authority that must issue the amnesty is the Supreme Leader, upon the recommendation of the Head of the Judiciary, as is standard practice under Article 110(11) of the Iranian Constitution. The announcement is expected to be first published on [Mizan Online](https://www.mizan.news/) or [IRNA](https://en.irna.ir/).

If no qualifying announcement is made by 23:59 UTC on July 1, 2026, this question resolves **No**.

**Pre-cutoff background**

Iran's leadership periodically grants amnesties and pardons, typically timed to coincide with national or religious holidays. These pardons are issued by the Supreme Leader upon recommendation of the Head of the Judiciary, as provided under Article 110 of the Iranian Constitution. Following the death of Ayatollah Ali Khamenei on February 28, 2026, his son Mojtaba Khamenei was appointed as the new Supreme Leader on March 9, 2026 [https://www.nytimes.com/live/2026/03/09/world/iran-war-trump-israel-lebanon](https://www.nytimes.com/live/2026/03/09/world/iran-war-trump-israel-lebanon).

Recent precedent: In September 2024, an amnesty covering 2,887 prisoners—including 39 convicted of "anti-state crimes"—was announced to mark the birthday of the Prophet Muhammad [Iran's top leader pardons prisoners, including foreigners and people ...](https://apnews.com/article/iran-khamenei-prisoner-pardon-amnesty-c8f41e8421b2b69f24f4465d2f0b8d17). In early 2025, another amnesty covered over 2,100 prisoners. Iran does not officially recognize the category of "political prisoner"; instead, individuals prosecuted for political activism or dissent are typically charged under Chapter 1 of Book Five of the Islamic Penal Code ("Crimes Against National and External Security"), particularly Articles 498–512, which cover offenses such as forming groups to disrupt national security (Art. 498), propaganda against the state (Art. 500), espionage, and related charges.

Key Iranian holidays falling within the May 10–July 1, 2026 window that are traditional occasions for amnesties include [Holidays and Observances in Iran in 2026 - Time and Date](https://www.timeanddate.com/holidays/iran/2026):
- Eid al-Adha (Eid-e-Qorban): ~May 27–28, 2026
- Anniversary of Imam Khomeini's Death: June 4, 2026
- Eid-e-Ghadir: ~June 4, 2026
- Khordad National Uprising (June 5, 1963 anniversary): June 5, 2026

The new Supreme Leader Mojtaba Khamenei may use amnesty announcements to consolidate legitimacy, but the ongoing military conflict with the US and Israel and a reported surge in executions (over 600 in early 2026 per NPR) [https://www.nytimes.com/live/2026/03/09/world/iran-war-trump-israel-lebanon](https://www.nytimes.com/live/2026/03/09/world/iran-war-trump-israel-lebanon) create cross-cutting pressures. The probability of an amnesty announcement is moderate—Iran frequently grants pardons around holidays, but the current wartime context and new leadership dynamics introduce significant uncertainty about whether such an amnesty would include security/political prisoners specifically.

**Exact later resolution packet**

RESOLUTION: NO (0).

WHAT HAPPENED (the antecedent — an amnesty by the Supreme Leader — did occur, so the question is NOT annulled):
- On June 5, 2026 (for the Shia holiday Eid al-Ghadir, within the May 10–July 1, 2026 window), Iran's Supreme Leader Mojtaba Khamenei approved a pardon/sentence-reduction for over 2,000 prisoners (including ~139 death-row inmates) upon the recommendation of the Head of the Judiciary, Gholamhossein Mohseni Ejei. This is confirmed by Anadolu Agency (https://www.aa.com.tr/en/middle-east/iran-s-supreme-leader-approves-pardon-for-over-2-000-convicts/3957513) [Iran's supreme leader approves pardon for over 2,000 convicts](https://www.aa.com.tr/en/middle-east/iran-s-supreme-leader-approves-pardon-for-over-2-000-convicts/3957513) and The Jerusalem Post (https://www.jpost.com/international/article-899344) [Khamenei pardons 139 Iranians sentenced to death to relieve int'l ...](https://www.jpost.com/international/article-899344). So the issuing authority and mechanism required by the question (Supreme Leader, upon recommendation of the Head of the Judiciary, per Article 110(11)) were satisfied, and it was a formal mass-pardon decree (not a routine individual pardon or a foreign prisoner exchange).

WHY IT RESOLVES NO (the amnesty did NOT cover national-security/political prisoners):
- The question resolves YES only if the amnesty (1) explicitly names "political prisoners," "security prisoners," or "crimes against national security" as a COVERED category, OR (2) is credibly reported by ≥2 major international sources or Mizan/IRNA as INCLUDING prisoners convicted under Articles 498–512 (e.g., "propaganda against the state," "assembly and collusion against national security").
- The opposite is documented: multiple credible sources report the amnesty EXPLICITLY EXCLUDED these categories. Anadolu Agency states "inmates convicted of security-related offenses, espionage, actions against Iran's internal or external security, and crimes threatening public security are not eligible for pardon" [Iran's supreme leader approves pardon for over 2,000 convicts](https://www.aa.com.tr/en/middle-east/iran-s-supreme-leader-approves-pardon-for-over-2-000-convicts/3957513). The Jerusalem Post, citing Iran's ISNA, states "detainees convicted of security-related offenses, espionage, actions against Iran's internal or external security, and crimes threatening public security were not eligible for the pardon" [Khamenei pardons 139 Iranians sentenced to death to relieve int'l ...](https://www.jpost.com/international/article-899344).
- This exclusion is further corroborated by numerous other outlets found in search (headlines such as Rudaw: "Khamenei pardons dozens of death row inmates, security cases excluded"; "Iran Announces Mass Prisoner Pardon, National Security Cases Excluded"; Demócrata: "excluding those convicted of state security"; thenewregion.com: "Khamenei pardons exclude state security convicts: Judiciary"), all consistent with the two documents I read.

CONCLUSION: A qualifying amnesty (Supreme Leader + Head of Judiciary recommendation + within window) did occur, but it specifically EXCLUDED national-security/political-offense categories rather than covering them. Under the resolution criteria (a general amnesty that does not name or demonstrably include security/political offense categories does not suffice), the question resolves NO.

KEY URLS:
- https://www.aa.com.tr/en/middle-east/iran-s-supreme-leader-approves-pardon-for-over-2-000-convicts/3957513 [Iran's supreme leader approves pardon for over 2,000 convicts](https://www.aa.com.tr/en/middle-east/iran-s-supreme-leader-approves-pardon-for-over-2-000-convicts/3957513)
- https://www.jpost.com/international/article-899344 [Khamenei pardons 139 Iranians sentenced to death to relieve int'l ...](https://www.jpost.com/international/article-899344)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-164. `3fd31303-a1fa-5fe2-8d15-523a2c8da568`

- Present date: `2026-05-12 17:07:59.718067`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the June 17, 2026 FOMC statement retain the phrase "additional adjustments to the target range for the federal funds rate"?

**Resolution criteria**

This question resolves YES if the official FOMC statement released following the June 16-17, 2026 meeting contains the phrase "additional adjustments to the target range for the federal funds rate." This question resolves NO if that phrase is absent from the statement, including if it has been modified to remove the word "additional" or replaced with materially different language (e.g., "maintain," "further evaluate," or neutral phrasing that does not reference future rate changes in a directional manner).

The determination will be based solely on the official text of the FOMC statement as published on the Federal Reserve's website (https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm) [The Fed - Meeting calendars and information - Federal Reserve](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm), not on subsequent press conferences, dot plot projections, minutes, or media interpretations.

For clarity: the key easing bias phrase from the April 2026 statement was "In considering the extent and timing of additional adjustments to the target range for the federal funds rate, the Committee will carefully assess incoming data, the evolving outlook, and the balance of risks" [Fed sees three dissents over an 'easing bias.' What's that? - Reuters](https://www.reuters.com/business/fed-sees-three-dissents-over-an-easing-bias-whats-that-2026-04-29/). The presence of "additional adjustments" is the specific test, as this is the language the three dissenters (Hammack, Kashkari, Logan) objected to as constituting an easing bias.

**Pre-cutoff background**

The Federal Open Market Committee (FOMC) releases a policy statement after each of its scheduled meetings. At the April 28-29, 2026 meeting, the FOMC held rates steady at 3.50-3.75% but retained language widely interpreted as an "easing bias": the phrase "In considering the extent and timing of additional adjustments to the target range for the federal funds rate, the Committee will carefully assess incoming data, the evolving outlook, and the balance of risks" [Fed sees three dissents over an 'easing bias.' What's that? - Reuters](https://www.reuters.com/business/fed-sees-three-dissents-over-an-easing-bias-whats-that-2026-04-29/). This language signals that the Committee's next rate move is likely to be a cut, since the word "additional" references prior rate cuts.

Three regional Fed presidents — Beth Hammack, Neel Kashkari, and Lorie Logan — dissented specifically because they opposed the inclusion of this easing bias language [Fed sees three dissents over an 'easing bias.' What's that? - Reuters](https://www.reuters.com/business/fed-sees-three-dissents-over-an-easing-bias-whats-that-2026-04-29/). A fourth dissenter, Governor Stephen Miran, dissented in the opposite direction, favoring a rate cut. Boston Fed President Susan Collins also publicly stated she sympathized with the dissenters' concerns about the easing bias language [Fed sees three dissents over an 'easing bias.' What's that? - Reuters](https://www.reuters.com/business/fed-sees-three-dissents-over-an-easing-bias-whats-that-2026-04-29/).

Inflation remains elevated, with the Producer Price Index (PPI) running at approximately 4% year-over-year. The combination of persistent inflation, growing internal dissent, and potential leadership changes at the Fed makes the survival of this easing bias language in the June 2026 statement a genuinely uncertain outcome. The June 16-17 meeting also includes the release of the Summary of Economic Projections (dot plot), which may influence the Committee's messaging strategy [The Fed - Meeting calendars and information - Federal Reserve](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm).

**Exact later resolution packet**

RESOLUTION: NO (0). The June 17, 2026 FOMC statement does NOT contain the phrase "additional adjustments to the target range for the federal funds rate." The easing-bias sentence was removed entirely.

KEY EVIDENCE (based solely on the official federalreserve.gov statement, per resolution criteria):
- The official FOMC statement published at https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm (HTML) and https://www.federalreserve.gov/monetarypolicy/files/monetary20260617a1.pdf (PDF) was a dramatically shortened statement (approved 12–0). Its policy text reads: "The Committee decided to maintain the target range for the federal funds rate at 3-1/2 to 3-3/4 percent... Inflation remains elevated relative to the Committee's 2 percent goal... The Committee will deliver price stability." The phrase "additional adjustments to the target range for the federal funds rate" is entirely absent [de2e67, 4c04e4].

CORROBORATION (independent sources confirming removal, not used as the determining source but resolving an initial apparent conflict):
- The New York Times redline/comparison article ("See How the First Fed Statement Under Warsh Evolved," June 17, 2026) explicitly states that the phrase — "which three members of the rate-setting committee objected to in April — was removed" [8f20bc].
- Yardeni Research's FOMC statements archive confirms the phrase appeared in the April 29, 2026 and December 10, 2025 statements but was removed from the June 17, 2026 statement [d5ea2d].
- TradingView's full reproduction of the June 2026 statement matches the shortened official text, without the phrase [bb9253].
- News coverage (RSM realeconomy: "Gone is the sentence, 'In considering the extent and timing of additional adjustments to the target range for the federal funds rate...'"; CNBC: "removal of key language indicating a bias toward future cuts within a dramatically shorter policy statement"; CFO Dive: "Fed ends bias toward more easing"; Sherwood: "Federal Reserve removes easing bias") all independently confirm removal.

RESOLVING AN APPARENT CONFLICT: Some Google snippets (e.g., NYT live blog, Facebook posts) appeared to show the phrase in quotes; these were quoting the prior April 2026 language for comparison/redline purposes, not the new June text. The RSM article's "Gone is the sentence..." and the NYT redline's "was removed" make clear the phrase is absent from the actual June 17 statement.

Per the resolution criteria, YES requires the phrase to be present; since it is absent (removed entirely, not merely modified), the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-165. `82f2d46e-be72-5be6-bf08-cbe61d0d6698`

- Present date: `2026-05-16 11:16:01.249322`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Israeli government formally initiate new dismissal proceedings against Attorney-General Gali Baharav-Miara between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after May 12, 2026 and before July 1, 2026 (23:59 UTC), the Israeli Justice Minister formally submits a request to the public-professional committee (as established under the 2000 government procedure for dismissal of the Attorney General, described by the Israel Democracy Institute at https://en.idi.org.il/articles/58656) to initiate the process of dismissing Attorney-General Gali Baharav-Miara, OR if the Israeli cabinet votes to approve the start of a new dismissal process through any legally valid procedure.

"Formally initiate dismissal proceedings" means the Justice Minister officially submits a written request to the relevant oversight committee or the cabinet passes a formal resolution to begin the dismissal process. Informal statements, political declarations, or media reports of intent do not count — there must be an official governmental action documented in government records or confirmed by at least two credible news outlets.

This question resolves NO if no such formal initiation occurs by July 1, 2026, or if Baharav-Miara is no longer serving as Attorney General for other reasons (e.g., resignation, end of term).

Resolution will be determined based on official Israeli government announcements or credible reporting from major news outlets such as Haaretz (https://www.haaretz.com), Times of Israel (https://www.timesofisrael.com), The Jerusalem Post (https://www.jpost.com), Reuters (https://www.reuters.com), or AP News (https://apnews.com).

**Pre-cutoff background**

Attorney-General Gali Baharav-Miara has been in an escalating conflict with the Israeli government led by Prime Minister Benjamin Netanyahu. In March 2025, the Israeli cabinet passed a no-confidence motion against her to begin the dismissal process. The government then created a revised dismissal procedure on June 8, 2025, replacing mandatory consultation with a public-professional committee with a new ministerial committee and a 75% majority vote requirement [ca66e5]. On August 4, 2025, the government voted unanimously to dismiss Baharav-Miara, but the High Court immediately froze the decision [162b1d]. On December 14, 2025, the Israeli Supreme Court ruled the government's dismissal was "null and void," citing "numerous procedural defects" and finding the government failed to follow the established legal mechanism requiring consultation with a public-professional committee [162b1d].

Under the original 2000 procedure (which the Supreme Court upheld as the valid process), the dismissal of the Attorney General requires: (1) the Justice Minister submitting a request to the public-professional committee (comprising a retired Supreme Court justice, a former justice minister or AG, a Knesset member, a lawyer, and an academic); (2) that committee determining whether grounds for dismissal exist; (3) a hearing for the AG; and (4) a government vote [ca66e5].

As of May 13, 2026, Baharav-Miara remains in office following the Supreme Court's December 2025 ruling. The coalition has signaled continued interest in her removal, but faces the constraint of having to follow the 2000 procedure validated by the court. Whether the government will restart formal proceedings through the proper legal channel remains uncertain.

**Exact later resolution packet**

RESOLUTION: NO (0)

The question resolves YES only if, between May 12, 2026 and July 1, 2026 (23:59 UTC), the Israeli Justice Minister formally submitted a request to the public-professional (Grunis) committee to dismiss Attorney-General Gali Baharav-Miara, OR the cabinet voted to approve the start of a new dismissal process through any legally valid procedure. Neither occurred.

KEY EVIDENCE:

1) During the resolution window, the government's action against the AG was LEGISLATIVE, not a dismissal proceeding. In the early hours of Tuesday June 2, 2026, the Knesset passed in first reading a pair of bills to SPLIT and WEAKEN the role of the Attorney-General (dividing it into an Attorney-General and a Prosecutor-General), by a 65–47 vote. Two separate credible outlets confirm this: The Times of Israel ("Legislation to split and weaken role of attorney general passes first Knesset reading," dated June 2, 2026) [Legislation to split and weaken role of attorney general passes first ...](https://www.timesofisrael.com/legislation-to-split-and-weaken-role-of-attorney-general-passes-first-knesset-reading/) and The Jerusalem Post ("Knesset votes in favor of bill to split role of attorney-general," article-898054, dated June 2, 2026) [Knesset votes in favor of bill to split role of attorney-general](https://www.jpost.com/israel-news/politics-and-diplomacy/article-898054). Both make clear this is a legislative restructuring of the office, NOT the formal initiation of dismissal proceedings against Baharav-Miara under the 2000 procedure. The Jerusalem Post article explicitly does not report any request to the public-professional committee or a cabinet vote to begin dismissal [Knesset votes in favor of bill to split role of attorney-general](https://www.jpost.com/israel-news/politics-and-diplomacy/article-898054), and the Times of Israel article likewise reports no such formal dismissal initiation [Legislation to split and weaken role of attorney general passes first ...](https://www.timesofisrael.com/legislation-to-split-and-weaken-role-of-attorney-general-passes-first-knesset-reading/).

2) No formal dismissal initiation via the proper channel occurred. After the Supreme Court's December 14, 2025 ruling that the government's prior firing was "null and void," the government would have needed to route any dismissal through a fully staffed Grunis (public-professional) committee. That committee had been left without a chair since around October 2025 (its chair's term ended, creating a vacuum), and there is no reporting that it was reconstituted or that Justice Minister Levin submitted a new request to it during May 12–July 1, 2026. Extensive searches across Haaretz, Times of Israel, Jerusalem Post, Reuters, and AP found no report of a new written request to the committee or a cabinet resolution starting a new dismissal process in the window.

3) Baharav-Miara remained in office throughout the window and did not resign or reach end of term. June 2026 articles refer to her as the "current A-G" and describe her actively speaking against the legislation (e.g., at the Israel Bar Association on June 1, 2026) [Knesset votes in favor of bill to split role of attorney-general](https://www.jpost.com/israel-news/politics-and-diplomacy/article-898054)[Legislation to split and weaken role of attorney general passes first ...](https://www.timesofisrael.com/legislation-to-split-and-weaken-role-of-attorney-general-passes-first-knesset-reading/). Wikipedia (last updated April 16, 2026) confirms she remains the incumbent Attorney General with no resignation reported [Gali Baharav-Miara - Wikipedia](https://en.wikipedia.org/wiki/Gali_Baharav-Miara). She was appointed in February 2022 to a six-year, non-renewable term (ending ~February 2028), so her term did not end in the window.

Because (a) no formal request to the public-professional committee was submitted and (b) no cabinet vote to start a new dismissal process occurred between May 12 and July 1, 2026 — the only relevant government action being legislation to restructure the office, which does not meet the resolution criteria — and (c) Baharav-Miara remained in office, the question resolves NO.

SOURCES:
- Times of Israel, "Legislation to split and weaken role of attorney general passes first Knesset reading" (June 2, 2026): https://www.timesofisrael.com/legislation-to-split-and-weaken-role-of-attorney-general-passes-first-knesset-reading/ [Legislation to split and weaken role of attorney general passes first ...](https://www.timesofisrael.com/legislation-to-split-and-weaken-role-of-attorney-general-passes-first-knesset-reading/)
- Jerusalem Post, "Knesset votes in favor of bill to split role of attorney-general" (article-898054, June 2, 2026): https://www.jpost.com/israel-news/politics-and-diplomacy/article-898054 [Knesset votes in favor of bill to split role of attorney-general](https://www.jpost.com/israel-news/politics-and-diplomacy/article-898054)
- Wikipedia, "Gali Baharav-Miara" (last updated April 16, 2026): https://en.wikipedia.org/wiki/Gali_Baharav-Miara [Gali Baharav-Miara - Wikipedia](https://en.wikipedia.org/wiki/Gali_Baharav-Miara)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-166. `ab593c1a-6055-552c-85bc-9979b0e97fc6`

- Present date: `2026-05-03 00:36:48.276862`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Starlink receive a commercial spectrum allocation from India's Department of Telecommunications (DoT) for satellite broadband services by June 1, 2026?

**Resolution criteria**

This question resolves YES if, on or before June 1, 2026, at 23:59 UTC, the Indian Department of Telecommunications (DoT) formally grants Starlink Satellite Communications Private Limited (or its parent/subsidiary) a commercial spectrum allocation or spectrum assignment for satellite-based broadband services in India. "Granting" is defined as the issuance of a formal spectrum assignment letter, an official listing on a government portal such as DoT's saralsanchar.gov.in (https://saralsanchar.gov.in) or dot.gov.in (https://dot.gov.in), or a press release from the Press Information Bureau (PIB) at https://pib.gov.in confirming the allocation. Trial or provisional spectrum for testing purposes does not count; the allocation must be for commercial operations.

This question resolves NO if no such commercial spectrum allocation has been granted by June 1, 2026, at 23:59 UTC.

Resolution will be determined based on official information published on Indian government portals, specifically:
- DoT website: https://dot.gov.in
- Saral Sanchar portal: https://saralsanchar.gov.in
- Press Information Bureau: https://pib.gov.in

Credible reporting from Reuters, The Economic Times, or NDTV confirming the allocation with reference to official government sources may also be used.

**Pre-cutoff background**

As of May 2, 2026, Starlink Satellite Communications Private Limited has already been granted a Unified License (UL) with authorization for Global Mobile Personal Communication by Satellite (GMPCS) service by the Indian Department of Telecommunications (DoT), as confirmed in a Ministry of Communications press release dated January 29, 2026 [Satellite Communication Services - PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2220346&reg=3&lang=1). Two other companies—OneWeb India Communications and JIO Satellite Communications—also received the same license [Satellite Communication Services - PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2220346&reg=3&lang=1).

However, holding a GMPCS license alone does not permit commercial satellite broadband operations. Companies must also receive a formal spectrum allocation from DoT to begin offering services. As of September 2025, Starlink had received only provisional/trial spectrum for testing purposes, not a full commercial spectrum allocation. India's Telecom Regulatory Authority (TRAI) recommended allotting satellite spectrum for commercial communication services for five years, but the final allocation by DoT to individual operators remains pending. Key outstanding requirements include security clearances from Indian intelligence agencies, establishment of local ground gateways within India, and compliance with data localization rules. The spectrum pricing framework and assignment methodology are still being finalized by DoT.

This question tracks whether Starlink will move beyond the GMPCS license and trial spectrum stage to receive a formal commercial spectrum allocation—the critical remaining regulatory hurdle before a full commercial launch in India.

**Exact later resolution packet**

The question resolves NO: as of the June 1, 2026 deadline, India's DoT had NOT granted Starlink a formal commercial spectrum allocation/assignment for satellite broadband services.

Key evidence:
- Starlink already holds the GMPCS Unified License (granted/confirmed by the Jan 29, 2026 PIB release, as stated in the question itself), but the question explicitly requires a separate COMMERCIAL spectrum allocation, distinct from the GMPCS license and distinct from trial/provisional spectrum.
- As of May 13, 2026, Starlink India submitted formal responses to TRAI's Consultation Paper on the "Framework for Satellite Communication Network Authorisation, and Assignment of Spectrum to Satellite Communication Network Providers." This document confirms the spectrum-assignment framework was still in the consultation stage; final commercial spectrum had not been assigned [[PDF] Starlink India Responses to](http://trai.gov.in/sites/default/files/2026-05/Starlink_14052026.pdf). The underlying TRAI consultation paper itself dates to April 8, 2026, showing the process was still ongoing.
- At the Rising Bharat Summit 2026 (reported Feb 2026), Telecom Minister Jyotiraditya Scindia said three licences with "normative spectrum assignment" had been issued to Starlink, Jio and OneWeb, but explicitly stated the "next policy call is the price of spectrum" — i.e., spectrum pricing had not been finalized and commercial assignment had not occurred [Satellite licences cleared for Starlink, Jio and OneWeb](https://www.moneycontrol.com/news/business/satellite-licences-cleared-for-starlink-jio-and-oneweb-spectrum-pricing-next-says-scindia-13845467.html). The "normative spectrum assignment" was a placeholder to allow security-compliance verification, not a commercial allocation enabling service.
- Multiple credible outlets in 2026 (Economic Times/Telecom, New Indian Express, Total Telecom) reported that Starlink "currently cannot start services in India because it has not been allocated satellite spectrum to operate commercially," and that "the regulator has yet to formally allocate satellite spectrum" — with the minister saying DoT would assign spectrum only once security requirements are met and pricing is finalized.
- As of May 2026, reports still described Starlink's India launch as delayed/pending spectrum allocation and pricing, with DoT having referred TRAI's pricing recommendations back for re-examination.

No PIB release, DoT/Saral Sanchar portal listing, or Reuters/ET/NDTV report citing government sources documented a formal COMMERCIAL spectrum assignment letter to Starlink on or before June 1, 2026, 23:59 UTC. The only spectrum Starlink had received prior was provisional/trial spectrum (Sept 2025), which the resolution criteria explicitly exclude. Therefore the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-167. `5fcaa409-ba75-5f5e-80f1-0de4013f719b`

- Present date: `2026-05-14 11:10:24.626723`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Courts and Tribunals Bill pass its Third Reading in the House of Commons without a division?

**Resolution criteria**

This question resolves based on the official record of House of Commons proceedings for the Third Reading of the Courts and Tribunals Bill 2024-26.

**Key definitions:**
- A **"division"** in the House of Commons is a formal recorded vote in which members physically or electronically register their vote, resulting in a count of Ayes and Noes. See the UK Parliament glossary: https://www.parliament.uk/site-information/glossary/division/
- A **"vote on the nod"** (also called a voice vote) occurs when the Speaker puts the question and members call out "Aye" or "No" without a formal count. If no member challenges the result, no division is held.

**Resolution:**
- This question resolves **Yes** if the Third Reading of the Courts and Tribunals Bill (https://bills.parliament.uk/bills/4083) in the House of Commons takes place on or after 12 May 2026 (00:00 UTC) and on or before 1 July 2026 (23:59 UTC), and the motion "That the Bill be now read the Third time" is agreed to without a division (i.e., passed on the nod via voice vote). A "vote on the nod" — where no division is called — results in a **Yes** resolution.
- This question resolves **No** if:
  - (a) The Third Reading takes place in the specified window and a division is called (i.e., the Hansard record shows "The House divided: Ayes X, Noes Y"), OR
  - (b) The Third Reading does not take place on or before 1 July 2026 (23:59 UTC).

**Resolution source:** The official Hansard record of the House of Commons (https://hansard.parliament.uk/) and/or the UK Parliament bill tracker (https://bills.parliament.uk/bills/4083).

**Pre-cutoff background**

The Courts and Tribunals Bill 2024-26 (Bill 422) was introduced to the House of Commons on 25 February 2026. The bill proposes significant reforms to the criminal justice system in England and Wales [https://commonslibrary.parliament.uk/research-briefings/cbp-10515/](https://commonslibrary.parliament.uk/research-briefings/cbp-10515/). Key controversial provisions include:

- **Jury trial restrictions (Clauses 1–7):** Removing the right to elect a jury trial for "either-way" offences and allowing judge-only trials for certain offences [https://commonslibrary.parliament.uk/research-briefings/cbp-10515/](https://commonslibrary.parliament.uk/research-briefings/cbp-10515/).
- **Increased magistrates' sentencing powers:** Raising the maximum custodial sentence magistrates can impose from 12 to 18 or 24 months [https://commonslibrary.parliament.uk/research-briefings/cbp-10515/](https://commonslibrary.parliament.uk/research-briefings/cbp-10515/).
- **Restrictions on appeals:** Limiting the right to appeal from magistrates' courts to the Crown Court [https://commonslibrary.parliament.uk/research-briefings/cbp-10515/](https://commonslibrary.parliament.uk/research-briefings/cbp-10515/).
- **Parental involvement:** Amending section 1 of the Children Act 1989 regarding the presumption of parental involvement in a child's life [https://bills.parliament.uk/bills/4083](https://bills.parliament.uk/bills/4083).

These proposals have faced substantial opposition from the legal profession (including the Criminal Bar Association) and from within the Labour Party itself, with nearly 40 Labour MPs writing to the Prime Minister opposing the jury trial restrictions, noting these changes were absent from the 2024 Labour manifesto [https://commonslibrary.parliament.uk/research-briefings/cbp-10515/](https://commonslibrary.parliament.uk/research-briefings/cbp-10515/). Backbench MP Karl Turner has been negotiating a possible compromise involving pilot schemes [https://commonslibrary.parliament.uk/research-briefings/cbp-10515/](https://commonslibrary.parliament.uk/research-briefings/cbp-10515/).

As of 30 April 2026, the bill has completed its Report stage in the House of Commons and is awaiting Third Reading [https://bills.parliament.uk/bills/4083](https://bills.parliament.uk/bills/4083). Whether the government can secure Third Reading without a formal recorded vote depends on the success of concessions made at Report stage and the level of remaining opposition.

**Exact later resolution packet**

The question resolves NO (0) under resolution criterion (b): "The Third Reading does not take place on or before 1 July 2026 (23:59 UTC)."

Evidence gathered (as of the resolution window closing 1 July 2026):

1. UK Parliament bill tracker (official resolution source), https://bills.parliament.uk/bills/4083/stages: The Courts and Tribunals Bill (Bill 4083) completed 1st Reading (25 Feb 2026), 2nd Reading (10 Mar 2026), Money Resolution/Carry-over (10 Mar 2026), and Committee Stage (from 25 Mar 2026). The Bill was reintroduced in the 2026-27 session on 14 May 2026. The Report Stage is listed as "Date to be announced," and no Third Reading is listed at all [1cf47f, 1b7623, 3cc8f3]. The bill's news page shows the most recent substantive update was the reintroduction, with no Report stage or Third Reading scheduled/completed [a6b2dd].

2. Hansard, House of Commons, 18 June 2026 (https://hansard.parliament.uk/Commons/2026-06-18/debates/D05D1644-C86D-4C31-8CEA-1B31C5F8C6C9/CourtsAndTribunalsBill): This was only a Select Committee statement on the Justice Committee's report, NOT a Third Reading. Justice Committee Chair Andy Slaughter explicitly stated there was "no confirmed date for the Bill's return to this House on Report" — meaning Report stage (which must precede Third Reading) had not even been scheduled by that date [3e8363].

3. The only Third Reading division in the relevant window I found on 10 June 2026 (Division 2372) was for the Railways Bill's Third Reading (278 Ayes, 149 Noes), NOT the Courts and Tribunals Bill [3b017a].

Because the Report stage had not been scheduled as of 18 June 2026, and the bill tracker still showed Report stage "Date to be announced" with no Third Reading recorded as of 1 July 2026, the Third Reading of the Courts and Tribunals Bill in the House of Commons did not occur within the resolution window (12 May 2026 – 1 July 2026). Therefore the question resolves NO. (Since no Third Reading occurred, there is naturally no Hansard "The House divided" record for a Third Reading division, and the "on the nod" YES condition was never met.)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-168. `089be930-58f2-50cb-962d-db630e7c7cd3`

- Present date: `2026-05-02 14:47:58.146390`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will there be a reported armed clash between Israeli forces and armed groups in the Quneitra Governorate between April 30 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if at least one credible source reports an armed clash between Israeli forces and any armed group within the [Quneitra Governorate](https://en.wikipedia.org/wiki/Quneitra_Governorate) occurring on or after April 30, 2026 (00:00 UTC) and before June 2, 2026 (00:00 UTC).

**Definition of "armed clash":** An event involving a verified exchange of fire (e.g., small arms fire, rocket/missile fire, artillery, or anti-tank weapons) between [Israeli military](https://en.wikipedia.org/wiki/Israel_Defense_Forces) personnel and members of any armed group, OR an event in which at least one casualty (killed or wounded) is reported on either side as a direct result of hostile engagement. Unilateral actions—such as Israeli airstrikes, raids, checkpoint operations, or demolitions where no return fire or hostile engagement from an opposing armed group is reported—do **not** qualify.

**"Armed group"** includes any non-state armed faction, militia, insurgent group, or state military force (e.g., Syrian government forces) that engages Israeli forces with weapons.

**Resolution sources:** Credible reporting from any of the following:
- [Reuters](https://www.reuters.com/world/middle-east/)
- [Associated Press](https://apnews.com/hub/middle-east)
- [AFP/France24](https://www.france24.com/en/middle-east/)
- [Al Jazeera](https://www.aljazeera.com/where/syria/)
- [Syrian Observatory for Human Rights](https://www.syriahr.com/en/)
- [IDF official website](https://www.idf.il/en/)
- [Enab Baladi](https://english.enabbaladi.net/)

The event must have occurred on or after April 30, 2026 to exclude any clashes prior to the start of the forecasting period. If no credible report of a qualifying armed clash is found by June 1, 2026, the question resolves **No**.

**Pre-cutoff background**

Following the fall of the Assad regime in December 2024, Israel declared the 1974 disengagement agreement void and established a military presence within the Syrian buffer zone in the [Quneitra Governorate](https://en.wikipedia.org/wiki/Quneitra_Governorate). As of late April 2026, [Israeli forces](https://en.wikipedia.org/wiki/Israel_Defense_Forces) have significantly expanded their presence in the region, conducting frequent raids, establishing temporary checkpoints (e.g., on roads linking Khan Arnabeh to Al-Samdaniyah), installing prefabricated structures at strategic locations like Tal al-Ahmar, and searching homes in towns such as Jubata al-Khashab [Israeli Fortifications Expand in Quneitra - Enab Baladi](https://english.enabbaladi.net/archives/2026/04/israeli-fortifications-expand-in-quneitra/). On April 25, 2026, Israeli forces raided two areas in the Quneitra countryside, setting up temporary checkpoints and searching civilians [Israeli forces raid Syria's Quneitra countryside, set up temporary ...](https://www.middleeastmonitor.com/20260425-israeli-forces-raid-syrias-quneitra-countryside-set-up-temporary-checkpoints/). The Syrian government has demanded withdrawal of these forces. The area remains volatile, with multiple incursions reported weekly and ongoing Israeli airstrikes in southern Syria more broadly. Despite this heavy military activity, most reported incidents to date have been unilateral Israeli operations (raids, checkpoints, airstrikes) rather than two-way armed engagements with opposing forces in Quneitra specifically. However, the [Southern Syria clashes (July 2025–present)](https://en.wikipedia.org/wiki/Southern_Syria_clashes_(July_2025%E2%80%93present)) demonstrate that armed confrontations in the broader region are ongoing, and various armed groups remain active in southern Syria.

**Exact later resolution packet**

The question resolves NO. It requires a qualifying "armed clash" — a verified two-way exchange of fire between Israeli forces and an armed group, OR at least one casualty from hostile engagement — occurring specifically within the Quneitra Governorate between April 30, 2026 (00:00 UTC) and June 2, 2026 (00:00 UTC), reported by one of the permitted sources (Reuters, AP, AFP/France24, Al Jazeera, SOHR, IDF, Enab Baladi).

Every reported event in Quneitra during the window was a UNILATERAL Israeli action, which the criteria explicitly exclude:
- SOHR (May 20, 2026): "Extensive shooting from Israeli base shocks southern Al-Quneitra" — shooting fired by Israeli forces from their Tel Ahmar base at agricultural lands; "no casualties were reported," and no return fire/hostile engagement described [Extensive shooting from Israeli base shocks southern Al-Quneitra ...](https://www.syriahr.com/en/382536/).
- SOHR (May 23, 2026): "Amid gunfire | Israeli forces advance into Daraa and Al-Quneitra countryside and establish military checkpoints" — Israeli patrol opened machinegun fire on farmlands and artillery fire near Taranjeh (Quneitra); no casualties and no return fire reported [Amid gunfire | Israeli forces advance into Daraa and Al ...](https://www.syriahr.com/en/382601/) [23/05/2026 - The Syrian Observatory For Human Rights](https://www.syriahr.com/en/date/2026/05/23/).
- Other Quneitra reports in the window (SOHR May 14, 19, 25, 27; Enab Baladi May; AA) describe Israeli incursions, checkpoints, artillery/mortar fire on farmland, flare grenades, demolitions, and arrests — all unilateral, repeatedly noted with "no casualties."

The two-way clashes in the broader region during this period (e.g., May 18–19, 2026: Israeli forces vs. armed gunmen with returned fire) occurred in the Yarmouk Basin of DARAA province, not Quneitra Governorate — confirmed by the dated SOHR May 25 page noting "Daraa | Military member injured" and multiple reports geolocating the Yarmouk Basin clashes to Daraa. These are outside the required location.

A civilian was killed in Quneitra by an Israeli tank shell on his vehicle (SOHR #380414), but that is a unilateral strike on a civilian, not an armed clash with an armed group, and does not satisfy the "hostile engagement on either side" definition.

The ACLED Middle East Overview for May 2026 likewise records no qualifying Israel–armed group clash in Quneitra within the window [Middle East Overview: May 2026 - ACLED](https://acleddata.com/update/middle-east-overview-may-2026).

The only documented instance of gunmen opening fire on Israeli forces in Quneitra (village of Turnejeh) dates to January 31, 2025 — far outside the window [Israeli forces come under fire in Syria in first since invasion](https://www.newarab.com/news/israeli-forces-come-under-fire-syria-first-invasion).

Permitted-source URLs reviewed: https://www.syriahr.com/en/382536/ ; https://www.syriahr.com/en/382601/ ; https://www.syriahr.com/en/date/2026/05/23/ ; https://www.syriahr.com/en/date/2026/05/25/ ; https://www.syriahr.com/en/378983/ (Rif Dimashq, March 2026). No permitted source reports a qualifying Quneitra clash in the window, so the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-169. `3c13677f-185b-5f70-8c61-084ca64fc527`

- Present date: `2026-05-02 18:31:05.592228`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the Morgan Stanley Solana Trust begin trading on a US exchange by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if shares of the Morgan Stanley Solana Trust (SEC File No. 333-292587, CIK 0002103547) execute their first trade on a national securities exchange registered with the SEC (as defined under Section 6 of the Securities Exchange Act of 1934; e.g., NYSE, NYSE Arca, Nasdaq, Cboe BZX) on or after May 1, 2026 (00:00 UTC) and no later than June 1, 2026 (23:59 UTC).

"Begin trading" is defined as the first execution of a trade of the trust's shares on such an exchange, evidenced by either: (a) the appearance of a ticker symbol with non-zero trading volume on the exchange, or (b) an official exchange notice or SEC filing confirming the commencement of trading.

A "US exchange" refers exclusively to a national securities exchange registered with the SEC pursuant to Section 6 of the Securities Exchange Act of 1934 (https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&type=1-N&dateb=&owner=include&count=40&search_text=&action=getcompany). Examples include NYSE, NYSE Arca, Nasdaq, and Cboe BZX. OTC markets do not qualify.

**Resolution sources:** The SEC EDGAR system (https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002103547&type=&dateb=&owner=include&count=40), official exchange listing notices, or credible financial news sources (e.g., Reuters, Bloomberg, CoinDesk) confirming the commencement of trading.

If shares began trading before May 1, 2026 (00:00 UTC), this question resolves **No** (as the event occurred outside the resolution window). If shares have not begun trading by June 1, 2026 (23:59 UTC), this question resolves **No**.

**Pre-cutoff background**

On January 6, 2026, Morgan Stanley Investment Management filed a Form S-1 registration statement (SEC File No. 333-292587, CIK 0002103547) with the U.S. Securities and Exchange Commission for the "Morgan Stanley Solana Trust," a passive investment vehicle designed to track the price of Solana (SOL) [EDGAR Filing Documents for 0001104659-26-000988](https://www.sec.gov/Archives/edgar/data/2103547/000110465926000988/0001104659-26-000988-index.htm). This was filed alongside a similar Form S-1 for the Morgan Stanley Bitcoin Trust. The SEC EDGAR filing is available at: https://www.sec.gov/Archives/edgar/data/2103547/000110465926000988/0001104659-26-000988-index.htm [EDGAR Filing Documents for 0001104659-26-000988](https://www.sec.gov/Archives/edgar/data/2103547/000110465926000988/0001104659-26-000988-index.htm).

As of early April 2026, the Morgan Stanley Bitcoin Trust (MSBT) has launched and begun trading with a 0.14% annual fee [Morgan Stanley Enters ETF Race - GSR Weekly](https://www.gsr.io/insights/gsr-weekly-update-april-13th-2026). However, the Morgan Stanley Solana Trust has not yet commenced trading as of that date [Morgan Stanley Enters ETF Race - GSR Weekly](https://www.gsr.io/insights/gsr-weekly-update-april-13th-2026). The regulatory pathway for a Solana-based trust product may face additional hurdles compared to Bitcoin, given the SEC's more established framework for Bitcoin ETPs. The trust must have its S-1 registration declared effective by the SEC and receive exchange listing approval before shares can trade.

The timeline from filing to trading for crypto trust products varies significantly. Bitcoin spot ETFs took roughly 6-12 months from initial filings to trading, though the regulatory environment has evolved since then. Morgan Stanley's Bitcoin Trust took approximately 3 months from filing to launch, but Solana products may face a different timeline given the SEC's varying stance on different crypto assets.

**Exact later resolution packet**

The question asks whether shares of the Morgan Stanley Solana Trust (SEC File No. 333-292587, CIK 0002103547) executed their first trade on a US national securities exchange between May 1, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC).

Evidence shows the Trust had NOT begun trading by the June 1, 2026 deadline:

- Morgan Stanley filed the initial Form S-1 on January 6, 2026 (https://www.sec.gov/Archives/edgar/data/2103547/000110465926000988/tm2534148d1_s1.htm). The filing stated shares are "expected to be listed for trading, subject to notice of issuance" — i.e., not yet trading.

- As of early April 2026, while the related Morgan Stanley Bitcoin Trust (MSBT) had launched and begun trading, the Morgan Stanley Solana Trust had NOT commenced trading (per the question's own description and Fortune coverage at https://fortune.com/2026/04/08/morgan-stanley-bitcoin-etf-msbt-launch-ethereum-solana/).

- Critically, on May 20, 2026 — within the resolution window — Morgan Stanley filed an AMENDED registration statement for the proposed spot Solana ETF, and the product was still in "regulatory negotiation" and did not yet carry a fee, indicating it was still not ready for launch [1b6897]. A registration that is still being amended and negotiated as of May 20, 2026 cannot have commenced trading. Yahoo Finance video coverage dated May 20, 2026 ("Morgan Stanley pushes into crypto with Solana staking ETF filing") corroborates that the May 20 event was a filing, not a trading launch.

- No SEC filing, exchange notice, or credible news source (Reuters, Bloomberg, CoinDesk) reported the commencement of trading or a non-zero-volume ticker for the Solana Trust during the May 1 – June 1, 2026 window. All coverage in that period refers to filings and regulatory negotiations, not a live listing.

Because shares of the Morgan Stanley Solana Trust did not begin trading on a national securities exchange on or before June 1, 2026 (23:59 UTC), the resolution criterion "If shares have not begun trading by June 1, 2026 (23:59 UTC), this question resolves No" is satisfied. The question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-170. `bd7e9821-6ab0-560e-ac91-e94679fd4ab3`

- Present date: `2026-05-29 01:03:12.245874`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will China's SAMR or State Council issue formal binding regulations specifically targeting instant retail/quick commerce subsidies by July 1, 2026?

**Resolution criteria**

This question resolves **YES** if, on or after May 12, 2026 and by 23:59 UTC on July 1, 2026, China's State Administration for Market Regulation (SAMR) or the State Council publishes a formal, binding regulation that explicitly targets, restricts, caps, or prohibits subsidies in the instant retail or quick commerce sector.

**"Formal, binding regulation"** means a document that carries legal force and mandates compliance, specifically one of the following Chinese legal categories:
1. **Administrative Regulations** (行政法规) issued by the State Council;
2. **Departmental Rules** (部门规章) issued by SAMR; or
3. **Normative documents** (规范性文件) with explicit enforcement mechanisms and penalties for non-compliance.

The regulation must **specifically** address instant retail, quick commerce, food delivery platforms, or on-demand retail subsidy/pricing practices. A regulation that only addresses general e-commerce pricing without specific reference to instant retail/quick commerce/food delivery platforms does **not** count.

**The following do NOT qualify:**
- Non-binding "guidance" (指导意见), "opinions" (意见), or "suggestions"
- Warnings, window guidance, or verbal instructions issued during meetings
- Reposting of media articles or editorials
- Fines or enforcement actions under existing law (such as the April 2026 food safety fines)
- Broad platform-economy guidelines that do not specifically target instant retail subsidies

**Resolution sources:** Official announcements on the SAMR website (https://www.samr.gov.cn/) or the State Council website (https://www.gov.cn/), or credible reporting by Reuters (https://www.reuters.com/), Bloomberg, South China Morning Post, or Xinhua confirming such issuance.

**Pre-cutoff background**

China's "instant retail" (即时零售, also called "quick commerce") sector—defined as on-demand delivery of goods (typically groceries, meals, and consumer products) within one hour via platforms such as Meituan, Alibaba's Ele.me/Taobao Shangou, JD.com, and ByteDance's Douyin—has been embroiled in an escalating price war fueled by platform subsidies (coupons, discounts, and below-cost promotional pricing designed to acquire users and market share).

Regulatory pressure has intensified in 2026:

- **March 25, 2026**: The state-run *Economic Daily* published an opinion piece criticizing the "vicious cycle" of the price war. SAMR reposted this article on its official website, signaling regulatory endorsement [Chinese food delivery giants surge as regulator, state media call ...](https://www.reuters.com/world/china/chinese-food-delivery-giants-surge-regulator-state-media-call-end-price-war-2026-03-25/).
- **April 3, 2026**: SAMR held a meeting with major food delivery platforms (Meituan, Taobao Shangou, JD.com) ordering them to strengthen food safety measures "ahead of new regulations taking effect in June" [China regulator orders food delivery giants to strengthen safety ...](https://www.reuters.com/world/asia-pacific/china-regulator-orders-food-delivery-giants-strengthen-safety-controls-2026-04-03/).
- **April 10, 2026**: China released broad guidelines on online platform pricing practices that instruct platforms to "strictly regulate subsidy practices, avoid malicious price competition and not make false or exaggerated claims about the scale or intensity of their subsidies" [E-commerce guidelines to foster orderly growth - Chinadaily.com.cn](https://global.chinadaily.com.cn/a/202604/14/WS69de3122a310d6866eb43612.html).
- **April 17, 2026**: SAMR fined and confiscated a total of 3.6 billion yuan ($527 million) from seven e-commerce platforms for food safety violations [Chinese regulator fines, confiscates $527 million from food ... - Reuters](https://www.reuters.com/world/asia-pacific/chinese-regulator-fines-confiscates-36-billion-yuan-food-delivery-platforms-2026-04-17/).
- The **State Council** has also become involved, launching an investigation into competition among food delivery platforms.

Despite these escalating actions, as of May 12, 2026, no formal binding regulation (as defined below) has been issued that specifically targets instant retail/quick commerce subsidies. The April 10 guidelines address platform pricing broadly but are not sector-specific binding rules. Reuters reported in April 2026 that new regulations were expected to take effect in June 2026, creating genuine uncertainty about whether formal rules will materialize within the resolution window [China regulator orders food delivery giants to strengthen safety ...](https://www.reuters.com/world/asia-pacific/china-regulator-orders-food-delivery-giants-strengthen-safety-controls-2026-04-03/).

**Key definitions:**
- **"Instant retail" / "quick commerce"**: On-demand delivery of goods (food, groceries, consumer products) typically within one hour, operated by platforms such as Meituan, Ele.me, JD.com Daojia, and Douyin. See: https://en.wikipedia.org/wiki/Quick_commerce
- **"Subsidies"**: Below-cost pricing, coupons, promotional discounts, or cash incentives funded by the platform (rather than the merchant) to attract or retain consumers.

**Exact later resolution packet**

The question resolves NO.

RESOLUTION CRITERIA: The question resolves YES only if, between May 12, 2026 and 23:59 UTC on July 1, 2026, China's SAMR or the State Council published a FORMAL, BINDING regulation (Administrative Regulation, Departmental Rule, or a Normative document with explicit enforcement mechanisms/penalties) specifically targeting/restricting/capping/prohibiting subsidies in the instant retail/quick commerce/food delivery sector. It explicitly states that non-binding drafts, guidance, opinions, and suggestions do NOT qualify.

WHAT ACTUALLY HAPPENED: On June 17, 2026, SAMR published the "外卖平台补贴行为规范十条（征求意见稿）" ("Ten Rules on Food Delivery Platform Subsidy Practices — Draft for Public Comment"). This is the only relevant regulatory instrument issued within the window, and it is explicitly a DRAFT for public comment (征求意见稿), NOT a finalized binding regulation.

KEY EVIDENCE THAT IT IS NOT YET BINDING:
- Reuters reported "China's market regulator issued draft rules to regulate subsidies by food delivery platforms" and that "The draft rules... are open for feedback until July 17" [China issues draft rules on food delivery subsidy in effort to curb ...](https://www.reuters.com/world/asia-pacific/china-issues-draft-rules-food-delivery-subsidy-effort-curb-price-wars-2026-06-17/) (https://www.reuters.com/world/asia-pacific/china-issues-draft-rules-food-delivery-subsidy-effort-curb-price-wars-2026-06-17/).
- Channel News Asia reported SAMR "proposed draft regulations" and that "The draft measures are open for public comment until Jul 17" [China seeks to curb 'unfair' competition in food delivery sector - CNA](https://www.channelnewsasia.com/east-asia/china-food-delivery-unfair-competition-rules-6192361) (https://www.channelnewsasia.com/east-asia/china-food-delivery-unfair-competition-rules-6192361).
- Xinhua's report confirmed the title is a "征求意见稿" (Draft for Comments), open for comment from June 17 to July 17, 2026, and that "下一步，市场监管总局将根据各方面意见，对征求意见稿进一步修改完善并抓紧制定出台" — i.e., SAMR will FURTHER modify the draft based on feedback and issue it in the future (after the window) [我国将规范外卖平台补贴行为征求意见稿出台 - 新华网客户端](https://app.xinhuanet.com/news/article.html?articleId=202606175c7d110d94e9437f9460450d982bcd48) (https://app.xinhuanet.com/news/article.html?articleId=202606175c7d110d94e9437f9460450d982bcd48).

DECISIVE LOGIC: The public consultation period runs June 17 – July 17, 2026, and SAMR stated it would finalize/issue the rules only AFTER considering feedback. Since the consultation deadline (July 17) falls AFTER the resolution window's close (July 1, 2026), it was structurally impossible for a finalized, binding version to have been published by July 1. As of July 1, 2026, only a non-binding draft for public comment existed. A draft for public comment does not carry legal force and does not satisfy the "formal, binding regulation" requirement — indeed, the resolution criteria's exclusion of "non-binding" instruments squarely applies.

Therefore no qualifying formal, binding regulation was published within the window, and the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-171. `07db4c8f-3c9b-53e0-9283-5a4e95400580`

- Present date: `2026-05-01 12:35:16.836769`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will there be a confirmed new kinetic strike (by the US or Israel) on any Iranian nuclear facility between April 30, 2026, and June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if at least one **kinetic strike** on an **Iranian nuclear facility** is **confirmed** between **00:00 UTC on April 30, 2026** and **23:59 UTC on June 1, 2026**. Otherwise, it resolves **No**.

**Definitions:**

- **Kinetic strike:** An attack involving the delivery of physical ordnance—including but not limited to missiles, aerial bombs, cruise missiles, artillery shells, or other explosive munitions—that causes or is intended to cause physical damage to a target. This explicitly excludes cyberattacks, electronic warfare, sabotage not involving physical ordnance, and sanctions.

- **Iranian nuclear facility:** Any site designated or referenced by the [International Atomic Energy Agency (IAEA)](https://www.iaea.org/topics/iran) as part of Iran's nuclear program, including but not limited to:
  - Natanz Fuel Enrichment Plant
  - Fordow Fuel Enrichment Plant
  - Isfahan (Esfahan) Nuclear Technology Center
  - Bushehr Nuclear Power Plant
  - Khondab (Arak) Heavy Water Production Plant/Reactor
  - Shahid Rezayee Nejad Yellow Cake Production Facility

- **Confirmed:** The strike must be reported by at least two of the following major international news organizations: [Reuters](https://www.reuters.com/), [Associated Press (AP)](https://apnews.com/), [BBC News](https://www.bbc.com/news), [Al Jazeera](https://www.aljazeera.com/), or [The New York Times](https://www.nytimes.com/). Official statements from the US Department of Defense, CENTCOM, or the Israeli Defense Forces (IDF) also qualify as confirmation.

- The strike must occur **on or after 00:00 UTC April 30, 2026, and no later than 23:59 UTC June 1, 2026**, to exclude all prior military actions.

**Resolution source:** Credible reporting from the outlets listed above, or official government/military statements. The IAEA updates page (https://www.iaea.org/topics/iran) may also serve as a supplementary source.

**Pre-cutoff background**

The United States and Israel have been conducting military operations against Iranian nuclear facilities since mid-2025. Key milestones include:

- **June 2025 ("Operation Midnight Hammer"):** US and Israeli forces struck the Natanz fuel enrichment plant, the Esfahan nuclear site, and the Fordow fuel enrichment plant, using GBU-57 bunker-buster bombs among other munitions [https://www.ans.org/news/article-7911/iaea-provides-updates-on-iran-nuclear-facilities/](https://www.ans.org/news/article-7911/iaea-provides-updates-on-iran-nuclear-facilities/).
- **March 2026:** Strikes intensified under "Operation Epic Fury," the current US military operation aimed at ensuring Iran "never acquires a nuclear weapon." Targets included the Natanz enrichment complex (March 2 and March 21), the Bushehr nuclear power plant (March 18), the Khondab heavy water production plant (March 27), and the Shahid Rezayee Nejad Yellow Cake Production Facility (March 27) [https://www.ans.org/news/article-7911/iaea-provides-updates-on-iran-nuclear-facilities/](https://www.ans.org/news/article-7911/iaea-provides-updates-on-iran-nuclear-facilities/).
- **April 2026:** Further strikes hit Bushehr (April 4). As of late April 2026, ceasefire negotiations are reportedly underway, but the US and Israel remain determined to eliminate Iran's nuclear expertise. CENTCOM has briefed President Trump on new strike plans [https://www.ans.org/news/article-7911/iaea-provides-updates-on-iran-nuclear-facilities/](https://www.ans.org/news/article-7911/iaea-provides-updates-on-iran-nuclear-facilities/).

The IAEA has been providing regular updates on the safety status of Iran's nuclear facilities. The question captures genuine uncertainty: while strikes have been frequent, ceasefire talks and diplomatic pressure create a real possibility of a pause in kinetic operations during this window.

**Exact later resolution packet**

The question resolves NO. No confirmed kinetic strike on an Iranian nuclear facility occurred within the window 00:00 UTC April 30, 2026 – 23:59 UTC June 1, 2026.

Background/context: A US-Iran ceasefire began April 8, 2026, after the heavy strike phase (February 28 – April 8, 2026). The major confirmed strikes on actual nuclear facilities (Natanz, Fordow, Isfahan, Bushehr, Khondab/Arak heavy water, Ardakan/Yazd yellowcake) all occurred BEFORE the resolution window — in March 2026 and up to the April 4–8 timeframe [US and Israeli strikes hit Iran sites tied to nuclear weapon work, think ...](https://www.iranintl.com/en/202605087856)[Iran says Natanz nuclear enrichment complex hit again in US-Israeli ...](https://www.aa.com.tr/en/middle-east/iran-says-natanz-nuclear-enrichment-complex-hit-again-in-us-israeli-attack/3873810)[List of attacks during the 2026 Iran war - Wikipedia](https://en.wikipedia.org/wiki/List_of_attacks_during_the_2026_Iran_war). The Natanz strikes were March 2 and March 21, 2026 [Iran says Natanz nuclear enrichment complex hit again in US-Israeli ...](https://www.aa.com.tr/en/middle-east/iran-says-natanz-nuclear-enrichment-complex-hit-again-in-us-israeli-attack/3873810).

Within the actual window (Apr 30 – Jun 1, 2026), military action continued during a fragile ceasefire, but the confirmed strikes targeted NON-nuclear sites:
- The 7 May 2026 US "self-defense" strikes hit military facilities at Bandar Abbas and Qeshm/Hormozgan ports, plus tankers in the Gulf of Oman — not nuclear facilities [Portal:Current events/May 2026 - Wikipedia](https://en.wikipedia.org/wiki/Portal:Current_events/May_2026).
- On 25 May 2026, US strikes targeted surface-to-air missile launch sites in Bandar Abbas and IRGC Navy boats [Portal:Current events/May 2026 - Wikipedia](https://en.wikipedia.org/wiki/Portal:Current_events/May_2026).
- The 26 May 2026 Reuters reporting confirms US strikes targeted "missile sites and boats attempting to lay mines" near the Strait of Hormuz in Hormozgan province — not nuclear facilities [Iran says new US strikes violate ceasefire - Reuters](https://www.reuters.com/world/middle-east/rubio-says-iran-deal-could-take-days-us-launches-fresh-strikes-2026-05-26/)[Iran says Washington violated ceasefire after new US strikes - Reuters](https://www.reuters.com/world/iran-war-live-us-launches-new-strikes-talks-stall-2026-05-26/).
- The 27 May 2026 Reuters reporting confirms US strikes hit a "ground control station" in Bandar Abbas and shot down four Iranian one-way attack drones — defensive actions, no nuclear facility hit [US carries out new strikes in Iran against a military site and drones ...](https://www.reuters.com/world/middle-east/us-carries-out-new-strikes-iran-against-military-site-official-says-2026-05-27/).
- Al Jazeera's May 27 timeline of attacks during the ceasefire lists no strikes on Iranian nuclear facilities in this window; the only nuclear-related items were a drone strike near the UAE's Barakah plant (a UAE facility, not Iranian) [US, Iran have launched multiple attacks during ceasefire: A timeline](https://www.aljazeera.com/news/2026/5/27/us-iran-have-launched-multiple-attacks-during-ceasefire-a-timeline).

The comprehensive Wikipedia "2026 Iran war" article and "List of attacks during the 2026 Iran war" likewise record no kinetic strike on any of the listed Iranian nuclear facilities (Natanz, Fordow, Isfahan, Bushehr, Khondab, Shahid Rezayee Nejad) during the window; May 2026 strikes are consistently described as targeting military, missile, and naval sites [2026 Iran war](https://en.wikipedia.org/wiki/2026_Iran_war)[List of attacks during the 2026 Iran war - Wikipedia](https://en.wikipedia.org/wiki/List_of_attacks_during_the_2026_Iran_war).

The resolution criteria require a NEW kinetic strike specifically on an IAEA-recognized Iranian nuclear facility, confirmed by ≥2 named outlets or an official US/IDF statement. While Reuters confirms strikes occurred in the window, those strikes were on military/naval/missile targets, not nuclear facilities. Therefore the YES condition is not satisfied and the question resolves NO.

(Note: A non-credible Facebook post claimed nuclear facilities were bombed around May 26; this is contradicted by the specific target descriptions in Reuters and Al Jazeera reporting and is disregarded under source-quality standards.)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-172. `0cb80752-f0f2-527b-a80f-417b6fccb936`

- Present date: `2026-05-14 04:39:17.484494`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the UK government or Ofwat apply to the High Court to place Thames Water into Special Administration by July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 12, 2026 (00:00 UTC) and on or before July 1, 2026 (23:59 UTC), either the Secretary of State for Environment, Food and Rural Affairs or Ofwat formally applies to the High Court to place Thames Water Utilities Limited into a Special Administration Regime (SAR), as defined under the [Water Industry Act 1991](https://www.legislation.gov.uk/ukpga/1991/56/contents) and the [Water Industry (Special Administration) Regulations 2024](https://www.legislation.gov.uk/uksi/2024/297/contents).

"Initiation" is defined specifically as the filing of an application to the High Court for a special administration order — not merely the announcement of contingency planning or preliminary steps.

This question resolves as **No** if no such application has been filed by 23:59 UTC on July 1, 2026.

**Resolution sources:** Official announcements on [GOV.UK](https://www.gov.uk/), [The Gazette](https://www.thegazette.co.uk/), or [Ofwat's website](https://www.ofwat.gov.uk/), supplemented by credible reporting from BBC, Reuters, or the Financial Times confirming the filing.

**Pre-cutoff background**

Thames Water Utilities Limited, the UK's largest water and wastewater company serving 16 million customers, has been in severe financial distress with approximately £16–27 billion in debt. As of March 2026, the company is in non-binding discussions with the London & Valley Water (L&VW) consortium regarding a recapitalisation proposal involving £3.35 billion of new equity and up to £6.55 billion of new debt [Recapitalisation Update - Press Speculation on London & Valley ...](https://www.thameswater.co.uk/news/2026/mar/recapitalisation-update-press-speculation-on-london-valley-water-s-proposal). No decision has been made by Thames Water's board, Ofwat, or other regulators to accept or implement this proposal. Discussions with financial stakeholders regarding terms were expected to continue in the weeks following the March 16, 2026 announcement [Recapitalisation Update - Press Speculation on London & Valley ...](https://www.thameswater.co.uk/news/2026/mar/recapitalisation-update-press-speculation-on-london-valley-water-s-proposal).

If the creditor rescue deal fails, the primary alternative is a Special Administration Regime (SAR). A SAR is a legal process under the [Water Industry Act 1991](https://www.legislation.gov.uk/ukpga/1991/56/contents) and the [Water Industry (Special Administration) Regulations 2024](https://www.legislation.gov.uk/uksi/2024/297/contents), whereby a Special Administrator is appointed to manage the company's affairs, ensuring continued water and sewerage services while facilitating a transfer to new ownership [Contractual risks if Thames Water enters special administration](https://beale-law.com/article/contractual-risks-if-thames-water-enters-special-administration/). Only Ofwat or the Secretary of State for Environment, Food and Rural Affairs has the legal power to apply to the High Court to initiate this process [Contractual risks if Thames Water enters special administration](https://beale-law.com/article/contractual-risks-if-thames-water-enters-special-administration/). The UK government has engaged insolvency specialist FTI Consulting to advise on contingency planning for a potential SAR [Contractual risks if Thames Water enters special administration](https://beale-law.com/article/contractual-risks-if-thames-water-enters-special-administration/), and has signaled readiness to act if necessary.

**Exact later resolution packet**

RESOLUTION: NO (0).

The question resolves YES only if, between May 12, 2026 (00:00 UTC) and July 1, 2026 (23:59 UTC), either the Secretary of State for Environment, Food and Rural Affairs or Ofwat FORMALLY FILED an application to the High Court for a Special Administration Order (SAR) under the Water Industry Act 1991. The resolution criteria explicitly exclude "the announcement of contingency planning or preliminary steps."

No such application was filed during the window. The evidence shows the situation only reached the stage of the government objecting to the creditor rescue deal, with Ofwat still deliberating — a formal High Court SAR application had NOT been filed by July 1, 2026:

- On 16 June 2026, Environment Secretary Emma Reynolds wrote to Ofwat objecting to the London & Valley Water (L&VW) £10bn rescue deal on the grounds it placed an "undue burden" on consumers. This letter was published on GOV.UK ("Environment Secretary of State's letter to Ofwat outlining concerns on proposals to recapitalise Thames Water," published 16 June 2026: https://www.gov.uk/government/publications/environment-secretary-of-states-letter-to-ofwat-outlining-concernson-proposals-to-recapitalise-thames-water). This was an objection/letter, not a High Court filing.

- BBC (16 June 2026) reported that Thames Water "moves step closer to nationalisation after government objects to rescue deal," and that Ofwat "has been reviewing the proposal and a decision is expected this summer" — i.e., no High Court application had been made; the process was still at the review/objection stage [247c91] (https://www.bbc.com/news/articles/cly089d0wl7o).

- As of 1 July 2026, the Reuters Thames Water company news feed showed the most recent development as the 16 June 2026 rejection of the rescue proposal, with no report of any formal High Court application for special administration having been filed [397107] (https://www.reuters.com/company/thames-water-ltd/).

- Contemporaneous coverage consistently framed SAR as "edging closer," "looming," or being "prepared for" — the FT reported the environment secretary had "stepped up preparations" for special administration (https://www.ft.com/content/1e05a7ff-391d-44f4-96d6-800cba2d2e8c), and Sky News reported ministers had "lined up" an administrator — all contingency/preparatory steps explicitly excluded by the resolution criteria, not an actual court filing.

ON THE SAR-SPECIFIC REQUIREMENT: Because no application of any kind was filed to the High Court by either the Secretary of State or Ofwat within the window, there was in particular no application for a Special Administration Order (SAR) as defined under the Water Industry Act 1991 and the Water Industry (Special Administration) Regulations 2024. The consequent (a formal SAR application) did not occur.

Since no application had been filed by 23:59 UTC on July 1, 2026, the question resolves NO per its own terms.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-173. `ab093507-8074-5400-8b54-8777ec74a7bf`

- Present date: `2026-05-16 20:35:20.644016`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Israel and Iran reach a formal ceasefire agreement by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 and before July 1, 2026 (23:59 UTC), a formal ceasefire agreement is reached between the United States (acting on behalf of or jointly with Israel) and Iran that explicitly ends or suspends hostilities in the current conflict.

**Definition of "formal ceasefire agreement":** A signed written agreement, or a joint official public declaration by authorized representatives, that explicitly commits to a cessation of hostilities. Authorized representatives are: for the United States, the President or Secretary of State; for Israel, the Prime Minister or Minister of Defense; for Iran, the Supreme Leader, President, or Foreign Minister. An agreement brokered by a third party (e.g., the United Nations, Pakistan, or another sovereign state mediator) counts if it is publicly accepted by the above-listed officials on both sides.

A unilateral ceasefire declaration, a temporary pause in fighting without a formal agreement, or an extension of an existing informal ceasefire does **not** count. The agreement must be described as a "ceasefire agreement," "peace agreement," or "cessation of hostilities agreement" in official statements.

**Verification sources:** The agreement must be confirmed by at least two of the following international news agencies: Reuters (reuters.com), Associated Press (apnews.com), Agence France-Presse, or BBC News (bbc.com). Alternatively, confirmation via an official government portal (e.g., whitehouse.gov, gov.il, or president.ir) suffices.

If no such agreement is confirmed by 23:59 UTC on June 30, 2026, this question resolves **No**.

**Pre-cutoff background**

As of May 12, 2026, the United States and Iran are engaged in negotiations to end an ongoing military conflict, but talks appear stalled. On May 11, 2026, President Trump rejected Iran's response to a U.S. 14-point ceasefire proposal, calling it "TOTALLY UNACCEPTABLE" on Truth Social and stating the ceasefire is "on life support." Iran has vowed to continue fighting. A temporary ceasefire has been in place since April 8, 2026, but its continuation is uncertain.

The Bank of Israel, in its March 30, 2026 monetary policy statement, left interest rates unchanged at 4.00%, citing geopolitical uncertainty related to "Operation Roaring Lion" and fighting in Lebanon. The BOI's macroeconomic forecast assumed fighting would end toward the end of April 2026, but this has not materialized [https://www.boi.org.il/en/communication-and-publications/press-releases/the-monetary-committee-decides-on-march-30-2026-to-leave-the-interest-rate-unchanged-at-400-percent/](https://www.boi.org.il/en/communication-and-publications/press-releases/the-monetary-committee-decides-on-march-30-2026-to-leave-the-interest-rate-unchanged-at-400-percent/). The BOI noted that the "expected duration and intensity of the fighting and how it will end" remained a key source of uncertainty affecting inflation and economic activity [https://www.boi.org.il/en/communication-and-publications/press-releases/the-monetary-committee-decides-on-march-30-2026-to-leave-the-interest-rate-unchanged-at-400-percent/](https://www.boi.org.il/en/communication-and-publications/press-releases/the-monetary-committee-decides-on-march-30-2026-to-leave-the-interest-rate-unchanged-at-400-percent/).

Negotiations are being conducted via Pakistani mediators, with Iran's proposals being relayed through intermediary channels. The key sticking points appear to involve the scope of Iran's nuclear program and security guarantees. Despite the negative signals, diplomatic channels remain open, and breakthroughs in such negotiations can occur rapidly.

**Exact later resolution packet**

RESOLUTION: NO (0).

WHAT HAPPENED: Within the resolution window (May 12 – July 1, 2026), the United States and Iran did sign a formal written agreement — the "Islamabad Memorandum" / 14-point Memorandum of Understanding (MOU). US President Trump and Iranian President Masoud Pezeshkian signed it remotely on June 17, 2026 [Islamabad Memorandum - Wikipedia](https://en.wikipedia.org/wiki/Islamabad_Memorandum) [Read the 14 points of the agreement between Iran and the U.S.](https://www.cbsnews.com/news/us-iran-deal-memorandum-of-understanding-text/) [US and Iran presidents sign ceasefire agreement, but Trump says ...](https://www.reuters.com/world/middle-east/g7-leaders-demand-ceasefire-lebanon-welcome-iran-deal-2026-06-17/). Reuters explicitly described it as a "ceasefire agreement" and "memorandum of understanding" [US and Iran presidents sign ceasefire agreement, but Trump says ...](https://www.reuters.com/world/middle-east/g7-leaders-demand-ceasefire-lebanon-welcome-iran-deal-2026-06-17/), and the text commits to "immediate and permanent termination of military operations on all fronts, including in Lebanon" [Islamabad Memorandum - Wikipedia](https://en.wikipedia.org/wiki/Islamabad_Memorandum) [Read the 14 points of the agreement between Iran and the U.S.](https://www.cbsnews.com/news/us-iran-deal-memorandum-of-understanding-text/). It was widely reported by Reuters, BBC, CBS, CNN, and France24. Substantively it extended the tenuous April 2026 ceasefire by another 60 days [2026 Iran war ceasefire - Wikipedia](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire) [Islamabad Memorandum - Wikipedia](https://en.wikipedia.org/wiki/Islamabad_Memorandum).

WHY THIS RESOLVES NO — the agreement fails the specific resolution criteria:

The criteria require "a formal ceasefire agreement ... between the United States (acting on behalf of or jointly with Israel) and Iran," and (for a third-party-brokered deal, which this was — mediated by Pakistan) that it be "publicly accepted by the above-listed officials on both sides." The listed authorized representatives explicitly include, for Israel, the Prime Minister or Minister of Defense.

The evidence conclusively shows the United States was NOT acting on behalf of, or jointly with, Israel:
- Reuters: Israel "was not part of the negotiations," PM Netanyahu "distanced Israel from the U.S.-Iran agreement," Israel "retains the right to use force," and fighting in Lebanon continued after the agreement was reached [US and Iran presidents sign ceasefire agreement, but Trump says ...](https://www.reuters.com/world/middle-east/g7-leaders-demand-ceasefire-lebanon-welcome-iran-deal-2026-06-17/).
- The Islamabad Memorandum record states that PM Netanyahu and Defense Minister Katz "explicitly rejected the agreement, stating that Israel was not bound by it and would continue military operations in Lebanon"; Israel was not a party [Islamabad Memorandum - Wikipedia](https://en.wikipedia.org/wiki/Islamabad_Memorandum).
- BBC live coverage: Israel was "not a signatory," Netanyahu said the "fight is not over" and that Israel would "remain in the security zone," continuing operations despite the US-Iran deal [Iran and US agree deal to end war as Israel says its forces will ... - BBC](https://www.bbc.com/news/live/cj0grpyg4v1t).

Consequently: (1) The US was neither "acting on behalf of" Israel (Israel disavowed and did not authorize the deal) nor "jointly with" Israel (Israel was cut out and opposed it), so the specific US/Israel–Iran agreement described in the criteria did not occur. (2) Israel's authorized representatives (PM Netanyahu, Def. Min. Katz) did NOT publicly accept the agreement — they rejected it — so the requirement that the deal be "publicly accepted by the above-listed officials on both sides" is not met. (3) Hostilities in the current conflict did not actually end; Israel continued military operations [US and Iran presidents sign ceasefire agreement, but Trump says ...](https://www.reuters.com/world/middle-east/g7-leaders-demand-ceasefire-lebanon-welcome-iran-deal-2026-06-17/) [Islamabad Memorandum - Wikipedia](https://en.wikipedia.org/wiki/Islamabad_Memorandum). (4) The ceasefire component was characterized as a 60-day extension of the pre-existing April ceasefire, which the criteria say does not count on its own.

Because the US–Iran MOU was not an agreement between "the United States (acting on behalf of or jointly with Israel) and Iran," and Israel's listed officials rejected rather than accepted it, the question resolves NO.

SOURCES:
- Reuters (June 17–18, 2026), "US and Iran presidents sign ceasefire agreement...": https://www.reuters.com/world/middle-east/g7-leaders-demand-ceasefire-lebanon-welcome-iran-deal-2026-06-17/ [US and Iran presidents sign ceasefire agreement, but Trump says ...](https://www.reuters.com/world/middle-east/g7-leaders-demand-ceasefire-lebanon-welcome-iran-deal-2026-06-17/)
- Wikipedia, "Islamabad Memorandum": https://en.wikipedia.org/wiki/Islamabad_Memorandum [Islamabad Memorandum - Wikipedia](https://en.wikipedia.org/wiki/Islamabad_Memorandum)
- CBS News, US–Iran MOU text: https://www.cbsnews.com/news/us-iran-deal-memorandum-of-understanding-text/ [Read the 14 points of the agreement between Iran and the U.S.](https://www.cbsnews.com/news/us-iran-deal-memorandum-of-understanding-text/)
- BBC News live, "Iran and US agree deal to end war as Israel says its forces will...": https://www.bbc.com/news/live/cj0grpyg4v1t [Iran and US agree deal to end war as Israel says its forces will ... - BBC](https://www.bbc.com/news/live/cj0grpyg4v1t)
- Wikipedia, "2026 Iran war ceasefire": https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire [2026 Iran war ceasefire - Wikipedia](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire) [2026 Iran war ceasefire - Wikipedia](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-174. `fcd6a603-a15a-52e0-90f4-bc08aad3be2c`

- Present date: `2026-05-14 00:56:24.883451`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-17T00:00:00`

**Question**

Will the Riksbank cut the policy rate at its June 17, 2026 monetary policy meeting?

**Resolution criteria**

This question resolves **Yes** if the Riksbank announces at its June 17, 2026 monetary policy meeting that the policy rate (styrränta, as defined at https://www.riksbank.se/en-gb/monetary-policy/the-policy-rate/) is set to a value strictly lower than 1.75%.

This question resolves **No** if:
- The Riksbank announces that the policy rate is held at 1.75% or increased above 1.75%; or
- The June 17, 2026 meeting is cancelled or postponed beyond July 1, 2026 (00:00 UTC), and no policy rate decision is announced before that date.

The resolution is based on the official Riksbank press release or monetary policy decision document published at https://www.riksbank.se/en-gb/monetary-policy/monetary-policy-report/. The announcement is expected on June 17, 2026 at approximately 09:30 CEST (07:30 UTC). If the announcement is delayed but still occurs on or before July 1, 2026 (23:59 UTC), the announced rate will be used for resolution.

**Pre-cutoff background**

The Sveriges Riksbank (Sweden's central bank) has held its policy rate ([styrränta](https://www.riksbank.se/en-gb/monetary-policy/the-policy-rate/)) at 1.75% since late 2024, maintaining this level through five consecutive meetings. At its most recent monetary policy decision on May 7, 2026, the Riksbank left the policy rate unchanged at 1.75%, noting that while inflation is currently low, "the risk of higher inflation has increased somewhat," and that growth was weak at the beginning of the year despite fundamentally favorable conditions for stronger economic activity [https://www.riksbank.se/en-gb/monetary-policy/monetary-policy-report/2026/monetary-policy-decision-may-2026/](https://www.riksbank.se/en-gb/monetary-policy/monetary-policy-report/2026/monetary-policy-decision-may-2026/).

The next monetary policy decision is scheduled for June 17, 2026 (meeting on June 16, decision announced June 17) [https://www.riksbank.se/en-gb/monetary-policy/monetary-policy-report/2026/monetary-policy-decision-may-2026/](https://www.riksbank.se/en-gb/monetary-policy/monetary-policy-report/2026/monetary-policy-decision-may-2026/).

Market expectations are divided. Nordea recently changed its forecast to call for a 25 basis point cut at the June meeting (to 1.50%), citing weak growth dynamics. However, the majority of forecasters expect a hold — an SEB survey showed approximately 75% expecting no change and roughly 20% expecting a cut to 1.50%. This divergence among professional forecasters makes the outcome genuinely uncertain.

Resolution source: The official Riksbank monetary policy decision page at https://www.riksbank.se/en-gb/monetary-policy/monetary-policy-report/

**Exact later resolution packet**

The question asks whether the Riksbank cut the policy rate (styrränta) to a value strictly lower than 1.75% at its June 17, 2026 monetary policy meeting.

RESOLUTION: NO (0).

Key facts established from the official resolution source and corroborating reports:

1. The meeting took place as scheduled. The monetary policy meeting was held on June 16, 2026, with the decision announced June 17, 2026. It was NOT cancelled or postponed. (Minutes titled "Minutes of the monetary policy meeting on 16 June 2026.")

2. The Riksbank left the policy rate UNCHANGED at 1.75%. The official monetary policy decision page for June 2026 states: "The policy rate is left unchanged at 1.75 per cent, some probability that it will be raised later this year." [Monetary policy decision June 2026 - Riksbanken](https://www.riksbank.se/en-gb/monetary-policy/monetary-policy-report/2026/monetary-policy-decision-june-2026/) The associated official press release confirms: "The Executive Board has decided to leave the policy rate unchanged at 1.75 per cent." [Policy rate unchanged at 1.75 per cent | Sveriges Riksbank](https://www.riksbank.se/en-gb/press-and-published/notices-and-press-releases/press-releases/2026/policy-rate-unchanged-at-14.75-per-cent)

3. The rate of 1.75% applies from 24 June 2026, per the Riksbank's main monetary policy page.

Since the announced policy rate (1.75%) is NOT strictly lower than 1.75% — it was held unchanged — the question resolves NO under the criterion: "This question resolves No if: The Riksbank announces that the policy rate is held at 1.75% or increased above 1.75%."

IMPORTANT NOTE ON A CONFLICTING TOOL OUTPUT: An initial automated read of the top-level monetary policy report index page erroneously reported a cut to 1.50%. This was a hallucination/error, contradicted by (a) the direct read of the June 2026 decision page, (b) the direct read of the official press release, and (c) numerous independent reports: FocusEconomics ("On 17 June, the Riksbank left its policy rate unchanged at 1.75% for its sixth straight hold"), Central Banking ("Sveriges Riksbank held rates at 1.75% at its policy meeting today (June 17)"), Trading Economics ("Sweden's central bank held its policy rate at 1.75% in June 2026"), and the official Riksbank main page ("Policy rate. 1.75%. Applies from 24 June 2026"). The overwhelming, authoritative evidence confirms a HOLD at 1.75%.

Official resolution source URLs:
- Decision page: https://www.riksbank.se/en-gb/monetary-policy/monetary-policy-report/2026/monetary-policy-decision-june-2026/
- Press release: https://www.riksbank.se/en-gb/press-and-published/notices-and-press-releases/press-releases/2026/policy-rate-unchanged-at-14.75-per-cent (title: "Policy rate unchanged at 1.75 per cent")

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-175. `1b03e056-63f6-5271-b6b0-22f8ae3ad0c6`

- Present date: `2026-05-14 02:41:23.830153`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-30T00:00:00`

**Question**

Will the RMT announce additional London Underground strike dates beyond June 19, 2026, on or before June 30, 2026?

**Resolution criteria**

This question resolves **Yes** if, between May 12, 2026 (00:00 UTC) and June 30, 2026 (23:59 UTC), the RMT union officially announces one or more new London Underground strike dates that are scheduled to begin on a date **after June 19, 2026**.

**Definitions and requirements:**

1. **"Announcement"**: An official press release published on the RMT's news page (https://www.rmt.org.uk/news/), OR a verified post on the RMT's official social media accounts (e.g., @RMTunion on X/Twitter or their official Facebook page), OR confirmed reporting by a major credible news outlet (BBC: https://www.bbc.com/news, The Guardian, Reuters, or the Associated Press).

2. **"London Underground strike"**: Industrial action involving a withdrawal of labour (i.e., a strike or walkout) by RMT members who are employed as London Underground train operators/drivers. This includes 24-hour strikes of the type already scheduled in this dispute. Action-short-of-a-strike (e.g., overtime bans, refusal to use devices) does NOT count. Strikes by other unions (e.g., Aslef) do not count.

3. **"Additional strike dates beyond June 19, 2026"**: The announced strike date(s) must be scheduled to commence (i.e., the start of the walkout) on or after June 20, 2026 (London time, UTC+1 during BST).

4. **Timing of announcement**: The announcement itself must be published on or after May 12, 2026, and no later than 23:59 UTC on June 30, 2026.

5. **Resolution source**: The primary resolution source is the RMT press/news page at https://www.rmt.org.uk/news/. Secondary sources include the TfL strikes page at https://tfl.gov.uk/campaign/strikes and credible news reporting from BBC News (https://www.bbc.com/news).

If no such announcement is made by 23:59 UTC on June 30, 2026, this question resolves **No**.

**Pre-cutoff background**

As of May 13, 2026, the Rail, Maritime and Transport (RMT) union is engaged in an ongoing dispute with Transport for London (TfL) over the imposition of a "compressed four-day working week" for London Underground tube drivers. London Underground management proposed reducing the working week from 36 hours to 35 hours spread over four days instead of five, which the RMT argues results in unacceptably long daily shifts (over 8 hours), raising fatigue and safety concerns [London Tube strikes: What you need to know - BBC](https://www.bbc.com/news/articles/c0ljyd03n88o). The RMT states the plan was imposed despite being rejected by a majority of Train Operators in internal e-referendums [RMT launches Tube strike action over imposed four-day ...](https://www.rmt.org.uk/news/rmt-launches-tube-strike-action-over-imposed-four-day/). The rival Aslef union, which represents a larger share of drivers, has accepted the proposal [London Tube strikes: What you need to know - BBC](https://www.bbc.com/news/articles/c0ljyd03n88o).

The dispute has followed a pattern of escalation: the RMT initially announced strike dates in March, which were suspended to allow negotiations, but when talks failed, additional dates in June were added. The full list of announced strike dates as of May 13, 2026 is:

- March 24–25 and March 26–27 (suspended/cancelled to allow negotiations) [RMT launches Tube strike action over imposed four-day ...](https://www.rmt.org.uk/news/rmt-launches-tube-strike-action-over-imposed-four-day/)
- April 21–22 and April 23–24 (completed) [RMT launches Tube strike action over imposed four-day ...](https://www.rmt.org.uk/news/rmt-launches-tube-strike-action-over-imposed-four-day/)
- May 19–20 and May 21–22 (upcoming) [London Tube strikes: What you need to know - BBC](https://www.bbc.com/news/articles/c0ljyd03n88o)
- June 16–17 and June 18–19 (upcoming) [London Tube strikes: What you need to know - BBC](https://www.bbc.com/news/articles/c0ljyd03n88o)

Each strike is a 24-hour walkout beginning at midday (12:00 London time). The current period of announced industrial action ends on June 19, 2026. Negotiations between the RMT and TfL remain unresolved, and no settlement has been announced. The RMT has also instructed members not to use company-issued electronic devices (including iPads) since March 21, 2026 [RMT launches Tube strike action over imposed four-day ...](https://www.rmt.org.uk/news/rmt-launches-tube-strike-action-over-imposed-four-day/).

**Exact later resolution packet**

RESOLUTION: NO (0).

The question resolves YES only if, between May 12 and June 30, 2026, the RMT officially announced one or more NEW London Underground train-operator/driver strike dates scheduled to COMMENCE on or after June 20, 2026. No such announcement was made.

TIMELINE OF THE 2026 FOUR-DAY-WEEK DISPUTE (from the RMT strike calendar) [c34441]:
- 11 Mar 2026: RMT launched Tube strike action over the imposed four-day compressed-hours plan.
- 26 Mar 2026: RMT suspended March strikes; new dates added.
- 20 Apr 2026: April strikes proceed.
- 18 May 2026: RMT suspended the planned May strikes and called FRESH strikes for June 2 and June 4, 2026.
The originally-scheduled June 16-17 / June 18-19 dates were called off and replaced by the EARLIER June 2 and June 4 walkouts. Both of these fall BEFORE June 20, so they do not satisfy the "commence on or after June 20, 2026" requirement.

NO DATES ON/AFTER JUNE 20 WERE ANNOUNCED:
- BBC "London Tube strikes: What you need to know" (updated 5 June 2026) explicitly states under "When is the next Tube strike?": "No dates are currently scheduled but the RMT has a strike mandate until late August." [e1581a]
- The RMT official news page and news archive were reviewed through 26 June 2026; the only late-June items concern other groups (e.g., Heavy Haul Rail Ltd, Carlisle Support Services) — none announce new London Underground driver strike dates beyond June 19 [be632d, 4187cc].
- Time Out London (11 June 2026): "no more strikes have been announced for the London Underground." [43c222]
- Tube Alerter (updated 4 June 2026): "No further Tube strike dates are currently announced." [7a08df]

RULING OUT A FALSE POSITIVE: Search results mentioning RMT "rolling strike action across the London Underground beginning on Friday 5 September for seven days" refer to SEPTEMBER 2025 (a separate pay/conditions dispute); the strike-calendar entry for that announcement is dated 21 August 2025, not 2026 [c34441]. It is therefore outside both the subject (four-day-week dispute) and the announcement window, and does not count.

Because no RMT announcement of London Underground driver strike dates commencing on or after June 20, 2026 was published on the RMT news page/social media or reported by BBC/Guardian/Reuters/AP between May 12 and June 30, 2026, the question resolves NO.

KEY EVIDENCE URLS:
- RMT news page: https://www.rmt.org.uk/news/ [be632d]
- RMT news archive: https://www.rmt.org.uk/news/archive/ [4187cc]
- BBC: https://www.bbc.com/news/articles/c0ljyd03n88o [e1581a]
- Strike calendar (2026 timeline; Sept 5 = 2025): https://www.strikecalendar.co.uk/union/rmt/londonundergroundstaffrmt [c34441]
- Time Out summer 2026 summary: https://www.timeout.com/london/news/london-tube-and-train-strikes-spring-2026-full-list-of-dates-and-lines-impacted-how-to-travel-everything-you-need-to-know-march-april-may-031026 [43c222]
- Tube Alerter: https://tubenotifications.co.uk/tube-strikes [7a08df]

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-176. `ccdfcdda-e872-5611-96ea-1af8b18c6c81`

- Present date: `2026-05-02 12:49:22.461835`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-05-25 00:00:00`

**Question**

Will the G7 Finance Ministers' communiqué from the May 18–19, 2026 Paris meeting contain the word "tariff" or "tariffs"?

**Resolution criteria**

This question resolves as **Yes** if the official G7 Finance Ministers and Central Bank Governors' communiqué or statement issued following the May 18–19, 2026 meeting contains the word "tariff" or "tariffs" in a context that specifically addresses US tariff policy. "Specifically addressing US tariff policy" is defined as: the word "tariff" or "tariffs" appearing in the same paragraph as any of the following terms: "United States," "US," "U.S.," "American," "Section 232," "Section 301," or "IEEPA."

References to tariffs solely in other contexts (e.g., tariffs on Russia, general trade principles without reference to the US) do not count.

**Primary resolution source:** The official communiqué as published on the G7 Information Centre at the University of Toronto (https://www.g7.utoronto.ca/finance/) or the French Treasury's G7 presidency page (https://www.tresor.economie.gouv.fr/tresor-international/france-s-g7-presidency-in-2026). If both sources are available and differ, the French Treasury version takes precedence as the host nation's official publication.

**If no communiqué is issued** (e.g., the meeting is canceled, or ministers fail to agree on a joint statement) by June 1, 2026 (23:59 UTC), this question resolves as **No**.

All dates are interpreted in UTC.

**Pre-cutoff background**

The G7 Finance Ministers and Central Bank Governors are scheduled to meet May 18–19, 2026 in Paris, under France's G7 presidency [G7 Finance Ministers' Communiqué - G7 Information Centre](https://www.g7.utoronto.ca/finance/260309-communique.html). This meeting occurs amid significant US trade policy upheaval following the US Supreme Court's February 20, 2026 ruling in *Learning Resources, Inc. v. Trump*, which held 6-3 that the International Emergency Economic Powers Act (IEEPA) does not authorize the President to impose tariffs, striking down sweeping tariffs imposed by President Trump (https://www.supremecourt.gov/opinions/25pdf/24-1287_4gcj.pdf).

G7 finance communiqués are carefully negotiated documents. Recent precedent suggests the word "tariff" is not guaranteed to appear in these statements. In the May 2025 Banff communiqué under Canada's presidency, the ministers acknowledged that "trade and economic policy uncertainty was high and weighing on global growth" but did not use the word "tariff" in relation to US policy, instead referencing tariffs only in the context of cutting off Russian revenues [G7 Finance Ministers and Central Bank Governors' Communiqué](https://www.canada.ca/en/department-finance/news/2025/05/g7-finance-ministers-and-central-bank-governors-communique.html). Reuters reported that Canada "glossed over tariffs" and the communiqué avoided direct references to US tariff policy. The March 9, 2026 Brussels communiqué under France's presidency focused on Middle East conflict, energy markets, and global economic conditions, and did not explicitly address US tariff or trade policy [G7 Finance Ministers' Communiqué - G7 Information Centre](https://www.g7.utoronto.ca/finance/260309-communique.html).

The post-Supreme Court landscape creates fresh uncertainty: the ruling invalidated IEEPA tariffs but Congress may attempt to legislate new tariff authority, and other tariff authorities (e.g., Section 232, Section 301) remain in force. France's presidency may push for stronger trade language, but US opposition to being singled out in communiqués is well-documented.

**Exact later resolution packet**

The question resolves NO. The French Treasury’s G7 presidency page identifies the relevant May 18–19, 2026 Paris Finance Ministerial Meeting materials and lists the official attached documents, including “G7 Finance Ministers' and Central Bank Governors' communiqué” and “G7 Finance Ministers' and Central Bank Governors' communiqué on the global economy, agreed following an exchange with partner countries,” both published May 19, 2026, which is before the June 1, 2026 23:59 UTC deadline [France's G7 Presidency in 2026 - Direction générale du Trésor](https://www.tresor.economie.gouv.fr/tresor-international/france-s-g7-presidency-in-2026). The specific French Treasury URLs found are:
- https://www.tresor.economie.gouv.fr/Institutionnel/Niveau2/Pages/66f48ea4-5474-48a9-8b8f-e9d8863999c7/files/2dbaafdc-795b-48c1-ae8b-bb9ff7c71cc1
- https://www.tresor.economie.gouv.fr/Institutionnel/Niveau2/Pages/66f48ea4-5474-48a9-8b8f-e9d8863999c7/files/4a536bce-5308-411e-8e59-d772abecebe5

Under the resolution criteria, a YES requires “tariff” or “tariffs” to appear in the same paragraph as one of “United States,” “US,” “U.S.,” “American,” “Section 232,” “Section 301,” or “IEEPA.” The main communiqué was reviewed and does not contain “tariff” or “tariffs” anywhere, so it cannot satisfy that paragraph-level US-tariff-policy test [https://www.tresor.economie.gouv.fr/Institutionnel/Niveau2/Pages/66f48ea4-5474-48a9-8b8f-e9d8863999c7/files/2dbaafdc-795b-48c1-ae8b-bb9ff7c71cc1](https://www.tresor.economie.gouv.fr/Institutionnel/Niveau2/Pages/66f48ea4-5474-48a9-8b8f-e9d8863999c7/files/2dbaafdc-795b-48c1-ae8b-bb9ff7c71cc1). The related communiqué/statement on the global economy was also reviewed and likewise does not contain “tariff” or “tariffs” anywhere [https://www.tresor.economie.gouv.fr/Institutionnel/Niveau2/Pages/66f48ea4-5474-48a9-8b8f-e9d8863999c7/files/4a536bce-5308-411e-8e59-d772abecebe5](https://www.tresor.economie.gouv.fr/Institutionnel/Niveau2/Pages/66f48ea4-5474-48a9-8b8f-e9d8863999c7/files/4a536bce-5308-411e-8e59-d772abecebe5). Because the official host-nation French Treasury versions were available by the deadline and neither relevant official text contains the required word in any context—let alone in the same paragraph as a US-related trigger term—the YES condition is not met, so the correct resolution is NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-177. `3e3b9901-688a-5e45-b03b-7b8c98511077`

- Present date: `2026-05-12 17:00:48.394975`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Vereinigung Cockpit call at least one strike at Lufthansa or its subsidiaries between May 10, 2026 and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if Vereinigung Cockpit (VC) officially calls or announces at least one strike action — including warning strikes (Warnstreiks) and full strikes — that is scheduled to begin on or after May 10, 2026 (00:01 CEST) and before July 1, 2026 (23:59 CEST), affecting pilots at any of the following Lufthansa Group airlines:

- **Deutsche Lufthansa AG** (mainline/Passage)
- **Lufthansa Cargo**
- **Lufthansa CityLine**
- **Eurowings**
- **Discover Airlines** (formerly Eurowings Discover)
- **Air Dolomiti**

A "strike" is defined as any organized work stoppage called by VC in which pilots represented by VC are instructed to cease work for any duration. Both warning strikes (Warnstreiks) and indefinite/full strikes count. A strike that was called before May 10 but extends into the resolution window also counts.

The question resolves **No** if no such strike is called or announced by 23:59 CEST on June 30, 2026.

**Resolution source:** Official announcements on the Vereinigung Cockpit newsroom at https://www.vcockpit.de/newsroom/, supplemented by credible news reporting from Reuters, AP, dpa, or major German outlets (FAZ, Handelsblatt, Tagesschau, Die Zeit).

**Pre-cutoff background**

The pilot union Vereinigung Cockpit (VC) has been engaged in an escalating labor dispute with the Lufthansa Group since late 2025, centered on demands for higher employer contributions to company pension schemes (betriebliche Altersversorgung) for Lufthansa and Lufthansa Cargo pilots, and higher salaries for CityLine pilots [Pilotengewerkschaft kündigt im Tarifstreit Gespräche mit Lufthansa an](https://www.handelsblatt.com/unternehmen/handel-konsumgueter/tarifkonflikt-pilotengewerkschaft-kuendigt-im-tarifstreit-gespraeche-mit-lufthansa-an/100210279.html).

The following strikes have been called by VC in this dispute during 2026:
- **February 12, 2026:** First strike at Lufthansa and Lufthansa Cargo [Die ersten Monate des Jahres 2026 sind geprägt durch Tarifkonflikte](https://www.vcockpit.de/newsroom/die-ersten-monate-des-jahres-2026-sind-gepraegt-durch-tarifkonflikte/).
- **March 12–13, 2026:** Strike at Lufthansa Passage and Lufthansa Cargo [Die ersten Monate des Jahres 2026 sind geprägt durch Tarifkonflikte](https://www.vcockpit.de/newsroom/die-ersten-monate-des-jahres-2026-sind-gepraegt-durch-tarifkonflikte/).
- **April 13–14, 2026:** 48-hour strike at Lufthansa, Lufthansa CityLine, and Eurowings.
- **April 16–17, 2026:** Further strike action at Lufthansa and subsidiaries [Die ersten Monate des Jahres 2026 sind geprägt durch Tarifkonflikte](https://www.vcockpit.de/newsroom/die-ersten-monate-des-jahres-2026-sind-gepraegt-durch-tarifkonflikte/).

As of April 17, 2026, VC announced it had no immediate plans for further strikes, following a week described as one of the most eventful in the union's history [Tarifkonflikt: Piloten beenden vorerst Streiks bei der Lufthansa](https://www.zeit.de/news/2026-04/17/nach-aus-fuer-lufthansa-cityline-piloten-streiken-weiter). The union offered mediation, but the parties could not agree on the scope of topics [Tarifkonflikt: Piloten beenden vorerst Streiks bei der Lufthansa](https://www.zeit.de/news/2026-04/17/nach-aus-fuer-lufthansa-cityline-piloten-streiken-weiter). Exploratory talks on pensions were scheduled but substantial progress remained uncertain [Pilotengewerkschaft kündigt im Tarifstreit Gespräche mit Lufthansa an](https://www.handelsblatt.com/unternehmen/handel-konsumgueter/tarifkonflikt-pilotengewerkschaft-kuendigt-im-tarifstreit-gespraeche-mit-lufthansa-an/100210279.html). The dispute is unresolved as of the latest available reporting, and the approach of the summer travel season creates both pressure to settle and leverage for the union.

**Exact later resolution packet**

RESOLUTION: NO (0).

The question resolves YES only if Vereinigung Cockpit (VC) officially called/announced at least one strike (Warnstreik or full strike) affecting pilots at Deutsche Lufthansa AG, Lufthansa Cargo, Lufthansa CityLine, Eurowings, Discover Airlines, or Air Dolomiti, scheduled to begin between May 10, 2026 (00:01 CEST) and June 30/July 1, 2026. Multiple sources confirm that no such strike was called in that window.

KEY EVIDENCE:

1) Official VC newsroom (the primary resolution source), reviewed for the entire May–June 2026 period, contains NO strike announcement. The releases in that window concern unrelated topics: May 12, 2026 recommendation not to discharge the Lufthansa board at the AGM; May 13 statement on a Federal Labour Court (BAG) Ryanair/Malta Air ruling; May 19 board-member retirement; May 27 podcast; May 29 interview about employer pressure (no strike announced); June 1 obituary; June 2 statement on the Working Hours Act; June 11 medical-referral model; June 24 women-in-cockpit article; June 29 Ryanair statement and a Leipzig podcast. The last strike-related announcements were in April 2026 [62d72f, 241ec0]. (VC newsroom: https://www.vcockpit.de/newsroom/ and https://www.vcockpit.de/newsroom/presse/)

2) Süddeutsche Zeitung, dated May 10, 2026 ("Bei der Lufthansa herrscht Ruhe im Tarifkonflikt – zumindest vorerst"), reports calm ("Ruhe") in the dispute at the very start of the resolution window, with the parties quietly seeking a solution and no new strike called [07bd28] (https://www.sueddeutsche.de/wirtschaft/lufthansa-vereinigung-cockpit-streik-li.3480707).

3) airliners.de (published May 4, 2026) reports that the mediation talks (Schlichtungsgespräche of April 23, 24, 27, 2026) failed, and that following the failure VC did NOT announce or call any new strike — it remained open to mediation under conditions instead [329149] (https://www.airliners.de/vereinigung-cockpit-schlichtungsgespraeche-lufthansa-gescheitert/87548).

4) hessenschau interview (April 21, 2026) noted VC had announced it would refrain from short-term strikes for the time being to pursue possible mediation, with hope for a "strike-free summer" [20d475].

The strikes described in the question (Feb 12; Mar 12–13; Apr 13–14; Apr 16–17, 2026) all preceded the resolution window and did not extend into it. After April 17, 2026 VC paused strikes; the April mediation attempt failed in early May but was NOT followed by any new strike call during May 10 – June 30, 2026. All strikes referenced were pilot strikes called specifically by VC (not Verdi/ground staff or UFO/cabin crew), but none fall within the required window. Therefore the consequent condition was not met and the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-178. `cb846579-9e62-51fc-983e-dffd075b20b5`

- Present date: `2026-05-03 02:31:02.847155`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will a bill specifically addressing AI companies' obligation to license news content be introduced in the US Congress between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves YES if, between May 1, 2026 (00:00 ET) and June 1, 2026 (23:59 ET) inclusive, at least one bill is introduced in the US Congress (House of Representatives or Senate) that specifically addresses AI companies' obligation to license news content.

**Definitions:**

- **"Introduced"** means the bill has been formally assigned an official bill number (e.g., H.R. XXXX or S. XXXX) in either chamber of Congress, as recorded on the official US Congress legislative database at https://www.congress.gov/.

- **"Specifically addresses AI companies' obligation to license news content"** means the bill's text must contain at least one provision that either (a) requires AI companies or developers to obtain a license from, or make payment to, news publishers or journalists before using their content for AI training or inference, OR (b) establishes a collective licensing or bargaining framework specifically for news content used by AI systems. A bill that only addresses AI transparency, labeling, deepfakes, or general copyright law without a specific news-content licensing mandate does not qualify.

- **"News content"** means journalistic works produced by news publishers, newspapers, news agencies, or similar organizations engaged in reporting current events.

**Resolution source:** The official US Congress legislative database at https://www.congress.gov/. The bill text or summary must be publicly available and must meet the criteria above. If congress.gov is unavailable, credible reporting from Reuters, AP, or major US newspapers confirming the bill's introduction and content may be used as a secondary source.

The question resolves NO if no qualifying bill is found on congress.gov by June 1, 2026 (23:59 ET).

**Pre-cutoff background**

On March 20, 2026, the White House released a "National Policy Framework for Artificial Intelligence," a set of legislative recommendations to guide Congress on federal AI regulation. Among its recommendations, the Framework urges Congress to "consider enabling licensing frameworks or collective rights systems for rights holders to collectively negotiate compensation from AI providers." This marked the first explicit signal from the Trump Administration that AI companies should compensate content creators, including news publishers.

Separately, on February 2, 2026, the Interactive Advertising Bureau (IAB) unveiled draft federal legislation called the "AI Accountability for Publishers Act" at its Annual Leadership Meeting. The proposed law would allow publishers to bring claims of "unlawful enrichment" against AI companies that scrape and use publisher content without authorization or compensation. IAB CEO David Cohen has been actively lobbying Congress to introduce this or similar legislation.

As of May 1, 2026, no bill has been formally introduced in the US Congress (i.e., assigned a bill number in either the House or Senate) that specifically mandates AI companies to obtain licenses or make payments for the use of news content in AI training or outputs. Multiple AI-related bills have been introduced in the 119th Congress on other topics (deepfakes, child safety, transparency), but none specifically targeting a licensing obligation for news content used by AI systems. The question is whether the combination of the White House Framework's recommendation and the IAB's lobbying push will translate into a formal bill introduction within the next month.

**Exact later resolution packet**

The question asks whether, between May 1, 2026 (00:00 ET) and June 1, 2026 (23:59 ET), at least one bill was formally introduced in the US Congress (assigned an H.R. or S. number on congress.gov) that specifically addresses AI companies' obligation to license/pay for news content (either mandating licenses/payment to news publishers, or establishing a collective licensing/bargaining framework specifically for news content used by AI systems).

The evidence indicates NO such qualifying bill was introduced:

1. The most cited candidate, the IAB's "AI Accountability for Publishers Act," remained only a DRAFT proposal. As of early 2026 the IAB had merely circulated the draft to Senate staff and members of Congress and was still seeking a sponsor to introduce it; there is no evidence it was ever assigned a bill number [9e1bf2]. The draft itself centers on "unlawful enrichment" claims against AI scrapers rather than a clean licensing mandate, and in any case it was never formally introduced.

2. The Nieman Lab report (dated May 27, 2026) on the emerging AI content-licensing market discusses only private-sector marketplaces (Cloudflare, Microsoft, TollBit, ProRata) and an Open Markets Institute report; it mentions no federal bill introduced in Congress mandating news-content licensing [9ef1e3].

3. The Transparency Coalition's comprehensive "AI Legislative Update: May 29, 2026" covers AI legislation but only at the state level, with no mention of any federal bill introduced in the May 1–June 1, 2026 window requiring AI companies to license or pay for news content [cf0a85].

4. Federal AI bills found on congress.gov around this window concern other topics (e.g., CREATE AI Act S.4441 introduced 04/29/2026; LIFT AI Act S.4414 introduced 04/28/2026; AI for America Act; Expanding AI Voices Act; deepfakes; copyright disclosure such as the TRAIN Act and CLEAR Act S.3813). None establish a news-content licensing or bargaining mandate for AI systems. Existing copyright-disclosure bills address transparency, not a licensing/payment obligation for news content, and thus are explicitly excluded by the resolution criteria.

No qualifying bill (news-content-specific AI licensing/bargaining mandate) was found introduced on congress.gov within the resolution window. Therefore the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-179. `59bbf28a-98e2-58a8-8e6c-ba46a61fe404`

- Present date: `2026-05-14 10:34:00.491513`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Mayor Muriel Bowser publicly endorse a candidate in the 2026 DC Democratic mayoral primary between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves YES if Muriel Bowser publicly endorses a candidate in the 2026 DC Democratic mayoral primary on or after May 12, 2026, and before 11:59 PM ET on July 1, 2026. It resolves NO otherwise.

**Definition of "publicly endorse":** A clear, unambiguous statement of support for a specific candidate, made by Bowser herself or her official office, via at least one of the following: (a) a press release or official statement from the Mayor's office, (b) a post from one of Bowser's verified/official social media accounts, or (c) a direct quote attributed to Bowser in a major news outlet. Appearing at a campaign event without an explicit verbal or written endorsement does not qualify.

**Definition of "candidate":** An individual who has officially filed to run in the 2026 Democratic primary for Mayor of the District of Columbia with the DC Board of Elections (https://www.dcboe.org/).

**Resolution sources:** Credible reporting from The Washington Post (https://www.washingtonpost.com/), DCist (https://dcist.com/), POLITICO (https://www.politico.com/), or official statements from the DC Mayor's office (https://mayor.dc.gov/). The endorsement must be on or after May 12, 2026, to exclude any prior actions.

**Pre-cutoff background**

Washington, D.C.'s incumbent Mayor Muriel Bowser is not seeking a fourth term, creating an open-seat race for the 2026 mayoral election [2026 Washington, D.C., mayoral election - Wikipedia](https://en.wikipedia.org/wiki/2026_Washington,_D.C.,_mayoral_election). The Democratic primary is scheduled for June 16, 2026. The two frontrunners are Janeese Lewis George (a current city councilmember) and Kenyan McDuffie (a former city councilmember), both of whom have positioned themselves as more confrontational toward the Trump administration than Bowser, who has maintained a working relationship with the White House [DC mayoral candidates contend with Trump's shadow - POLITICO](https://www.politico.com/news/2026/05/06/dc-mayoral-race-donald-trump-00908554). Other declared Democratic candidates include Yaida Ford, Gary Goodweather, Robert L. Gross, Regan Jones, Talib Karim Muhammad, Vincent Orange, Rini Sampath, and Hope Solomon [2026 Washington, D.C., mayoral election - Wikipedia](https://en.wikipedia.org/wiki/2026_Washington,_D.C.,_mayoral_election). As of May 12, 2026, Bowser has not publicly endorsed any candidate in the race [2026 Washington, D.C., mayoral election - Wikipedia](https://en.wikipedia.org/wiki/2026_Washington,_D.C.,_mayoral_election) [DC mayoral candidates contend with Trump's shadow - POLITICO](https://www.politico.com/news/2026/05/06/dc-mayoral-race-donald-trump-00908554). Her endorsement is considered politically significant given her prominence in D.C. politics, but she faces conflicting incentives: backing a winner could cement her legacy, while backing a loser could damage it. In late 2025, Bowser hinted at the possibility of an endorsement but did not commit.

**Exact later resolution packet**

The question resolves NO. Mayor Muriel Bowser did not make a clear, unambiguous public endorsement of any candidate in the 2026 DC Democratic mayoral primary within the May 12 – July 1, 2026 window.

Key event: On June 9, 2026, at an Axios AM Live event, Bowser stated: "I support Kenyan McDuffie and I have always supported Kenyan McDuffie," but immediately added, "I'm not endorsing or making any endorsements for mayor, because I'm stepping off the political stage." (This quote appears verbatim across many outlets; the underlying event was widely reported.)

Why this does not meet the resolution bar:
- The resolution criteria define "publicly endorse" as "a clear, unambiguous statement of support for a specific candidate." Bowser's statement was explicitly self-contradictory/ambiguous with respect to endorsement — she simultaneously expressed support for McDuffie AND declared she was "not endorsing or making any endorsements for mayor." An explicit refusal to endorse cannot constitute an unambiguous endorsement.
- Among the specifically approved resolution sources (Washington Post, DCist, POLITICO, mayor.dc.gov), POLITICO's June 18, 2026 primary-results article characterizes McDuffie as having gained only Bowser's "tacit support," not a formal endorsement [876b09]. This is the strongest approved-source signal and confirms she did not formally endorse.
- The Washington Post's June 14, 2026 pre-primary article covering the final days of the race contains no report of any Bowser endorsement of any candidate [784527].
- POLITICO's May 23, 2026 "delicate dance" article, covering the race in the middle of the window, likewise reports no Bowser endorsement of any of the Democratic candidates [7ff209].

The Democratic primary was held June 16, 2026, and was won by Janeese Lewis George — a candidate running explicitly against Bowser's legacy — so there is no indication Bowser endorsed the eventual nominee either. No approved source reports a formal endorsement at any point in the window.

Corroborating (non-approved) sources reinforce the same conclusion using language that all stops short of "endorsement": Axios headline "Bowser backs McDuffie in DC mayor's race, but stops short of endorsement" (June 9, 2026) [7d1441]; Washington Examiner "Bowser soft-endorses Kenyan McDuffie"; WUSA9 "closest thing to an endorsement… Bowser said she is not endorsing anyone." These are consistent with the approved sources but were not relied upon for the resolution.

Approved-source URLs:
- POLITICO (June 18, 2026): https://www.politico.com/news/2026/06/18/lewis-george-dc-mayor-primary-00966879 [876b09]
- Washington Post (June 14, 2026): https://www.washingtonpost.com/dc-md-va/2026/06/14/dc-cusp-change-june-elections-leaving-voters-fretting/ [784527]
- POLITICO (May 23, 2026): https://www.politico.com/news/2026/05/23/dc-mayor-election-trump-00935105 [7ff209]

Because the strongest characterization in an approved source is "tacit support," and because Bowser explicitly stated she was "not endorsing," the criterion of a "clear, unambiguous" endorsement was not satisfied. Resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-180. `b1cb749a-50bb-523c-95b2-ec9fa17962fe`

- Present date: `2026-05-02 11:07:19.896768`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-05-14 00:00:00`

**Question**

Will Labour finish third or lower in constituency vote share in the 2026 Scottish Parliament election?

**Resolution criteria**

This question resolves YES if the Scottish Labour Party receives a lower percentage of the total valid constituency votes cast than at least two other parties in the 2026 Scottish Parliament election held on 7 May 2026 (UTC+1).

This question resolves NO if the Scottish Labour Party finishes first or second in constituency vote share.

Definitions and clarifications:
- "Constituency vote" refers specifically to the first-past-the-post ballot (the "first vote"), NOT the regional/list vote (the "second vote"). These are two separate tallies. Only the constituency vote is relevant for resolution.
- "Vote share" means the percentage calculated as: (total valid constituency votes cast for the party across all 73 constituencies) ÷ (total valid constituency votes cast across all 73 constituencies) × 100.
- In the event of an exact tie in vote share percentage (to two decimal places) between Labour and another party for second place, this question resolves NO (i.e., Labour is not considered to have finished "lower" than a party it is tied with).
- If the election is postponed beyond 31 May 2026 (UTC), this question resolves N/A.

Resolution source: The official results as published on the BBC Scotland election results page at https://www.bbc.co.uk/news/election/2026/scotland/results or the Electoral Management Board for Scotland. If these sources are unavailable, credible reporting from Reuters, PA Media, or STV News may be used.

**Pre-cutoff background**

The 2026 Scottish Parliament election is scheduled for Thursday 7 May 2026 (UTC+1), electing 129 MSPs. Each voter casts two votes: a constituency vote (first-past-the-post for 73 seats) and a regional/list vote (proportional representation for 56 seats).

Recent polling suggests a tight race for second and third place in the constituency vote between Labour and Reform UK. As of late April 2026, Ballot Box Scotland's constituency polling tracker shows the SNP leading at approximately 36%, with Labour at approximately 18.8% and Reform UK at approximately 18.4% [Scottish Parliament Polling - Ballot Box Scotland](https://ballotbox.scot/scottish-parliament/polling-scottish-parliament/). Earlier YouGov polling from January 2026 had Labour as low as 15% on constituency voting intention. Some more recent polls have shown Labour edging ahead of Reform, while others show the race essentially tied.

The battle between Labour and Reform for second place in the constituency vote is historically significant. Labour has traditionally been one of Scotland's dominant parties, and finishing third behind Reform UK—a party with no established presence in Holyrood—would represent a major shift in Scottish politics. The BBC has identified several key battleground constituencies where Labour and Reform are competing for votes [Key battlegrounds in the 2026 Scottish Parliament election - BBC](https://www.bbc.com/news/articles/cyv1m396n3eo).

The Scottish Parliament uses the Additional Member System. The constituency vote share discussed here refers to the aggregate percentage of valid votes cast across all 73 constituency contests.

**Exact later resolution packet**

The question should not be annulled for postponement: the election occurred on 7 May 2026, which is before the 31 May 2026 cutoff [SPICe general election Scotland 2026 results and analysis](https://spice-spotlight.scot/2026/05/09/the-results-are-in-general-election-2026/).

Using the required metric—the Scotland-wide constituency vote/first-past-the-post vote, not the regional/list vote—the reported party totals and shares were: SNP 877,077 votes (38.18%); Labour 440,708 votes (19.18%); Reform UK 361,994 votes (15.76%); Conservative 271,740 votes (11.83%); Liberal Democrat 261,408 votes (11.38%); Green 52,528 votes (2.29%); Minor 27,746 votes (1.21%); Others 3,958 votes (0.17%) [Scottish Parliament Election 2026 Results](https://www.electionpolling.co.uk/results/2026s). These figures sum to 2,297,159 valid constituency votes, so Labour’s share is 440,708 / 2,297,159 × 100 = 19.18% to two decimals, matching the cited table [Scottish Parliament Election 2026 Results](https://www.electionpolling.co.uk/results/2026s).

Labour therefore finished second in constituency vote share: only the SNP (38.18%) was above Labour’s 19.18%, while Reform UK was below Labour at 15.76% [Scottish Parliament Election 2026 Results](https://www.electionpolling.co.uk/results/2026s). There was no two-decimal tie for second place involving Labour, since Labour’s 19.18% exceeded Reform UK’s 15.76% [Scottish Parliament Election 2026 Results](https://www.electionpolling.co.uk/results/2026s). Because the YES condition requires Labour to have a lower constituency vote percentage than at least two other parties, and only one party finished above Labour, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-181. `82ee0f1f-0658-5903-97c7-adadece0c10e`

- Present date: `2026-05-16 11:08:59.597359`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will OFAC designate at least one new UAE-based entity or individual under Sudan-related sanctions between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 and no later than July 1, 2026 (23:59 UTC), OFAC publicly announces the addition of at least one new entity or individual to the Specially Designated Nationals (SDN) List under a Sudan-related sanctions program, where that entity or individual has a listed address in the United Arab Emirates in the OFAC designation announcement or SDN entry.

Key definitions:

- **"UAE-based"**: An entity or individual whose SDN List entry includes a physical address located in the United Arab Emirates, as displayed on the [OFAC SDN List Search tool](https://sanctionssearch.ofac.treas.gov/) or the corresponding [Recent Actions announcement](https://ofac.treasury.gov/recent-actions). This includes entities incorporated in the UAE, individuals residing at a UAE address, or entities headquartered in the UAE. The UAE is defined per its [Wikipedia entry](https://en.wikipedia.org/wiki/United_Arab_Emirates) as the federation of seven emirates.

- **"Sudan-related sanctions"**: Designations made pursuant to any of the executive orders listed on the [OFAC Sudan and Darfur Sanctions page](https://ofac.treasury.gov/sanctions-programs-and-country-information/sudan-and-darfur-sanctions), including but not limited to E.O. 14098, E.O. 13400, E.O. 13412, and E.O. 13067 [Sudan and Darfur Sanctions | Office of Foreign Assets Control](https://ofac.treasury.gov/sanctions-programs-and-country-information/sudan-and-darfur-sanctions). The designation must be explicitly tagged to the Sudan/Darfur sanctions program in the OFAC announcement.

- **"New designation"**: The entity or individual must be newly added to the SDN List. Modifications to existing entries or re-designations under additional programs do not count. The designation must occur on or after May 12, 2026 to exclude prior designations, including the April 17, 2026 action [Counter Terrorism Designations; Sudan Designations](https://ofac.treasury.gov/recent-actions/20260417).

**Resolution source**: The [OFAC Recent Actions page](https://ofac.treasury.gov/recent-actions) and/or the [OFAC SDN List Search tool](https://sanctionssearch.ofac.treas.gov/).

If no qualifying designation is announced by 23:59 UTC on July 1, 2026, the question resolves **No**.

**Pre-cutoff background**

The U.S. Department of the Treasury's Office of Foreign Assets Control (OFAC) maintains sanctions programs targeting those destabilizing Sudan, primarily authorized under Executive Order 14098 (May 4, 2023) and earlier orders such as E.O. 13400 (April 26, 2006), governed by the Sudan Stabilization Sanctions Regulations (31 CFR Part 546) [Sudan and Darfur Sanctions | Office of Foreign Assets Control](https://ofac.treasury.gov/sanctions-programs-and-country-information/sudan-and-darfur-sanctions).

On April 17, 2026, OFAC designated Jose Oscar Garcia Batte—a Colombian national with a listed address in Dubai, UAE—along with two Colombia-based entities (FENIX HUMAN RESOURCES S.A.S. and GLOBAL QOWA AL BASHERIA S.A.S.) under the Sudan sanctions program [Counter Terrorism Designations; Sudan Designations](https://ofac.treasury.gov/recent-actions/20260417). As of May 12, 2026, this is the most recent Sudan-related designation involving a UAE-addressed individual.

International pressure on the UAE's role in Sudan's conflict has been mounting. Amnesty International published investigations in May 2025 identifying advanced Chinese-made weaponry (GB50A bombs and AH-4 howitzers) provided by the UAE to Sudan's Rapid Support Forces (RSF) in breach of the UN arms embargo. In April 2026, Amnesty reiterated calls for the UAE to halt arms transfers to the RSF. In February 2026, Sudan rejected a UN call for a nationwide arms embargo while denouncing UAE involvement. These reports and diplomatic tensions create an environment in which further OFAC designations targeting UAE-based networks are plausible but uncertain, given the strategic importance of the U.S.-UAE relationship and competing Middle East priorities (Iran, Israel).

No additional UAE-based entities or individuals beyond the April 17, 2026 designation are currently listed under Sudan-related sanctions with UAE addresses [Counter Terrorism Designations; Sudan Designations](https://ofac.treasury.gov/recent-actions/20260417).

**Exact later resolution packet**

The question resolves NO.

Resolution criteria: Between May 12, 2026 and July 1, 2026 (23:59 UTC), OFAC must have added at least one NEW entity/individual to the SDN List under a Sudan-related sanctions program (E.O. 14098, 13400, 13412, 13067, etc.) where that entity/individual has a listed address in the United Arab Emirates.

Findings:
1. The only Sudan-related OFAC designation action in the resolution window was the "Sudan-related Designations" published June 26, 2026 (https://ofac.treasury.gov/recent-actions/20260626; Treasury press release "Treasury Sanctions Networks Fueling Sudan's Civil War and Worsening Humanitarian Crisis," https://home.treasury.gov/news/press-releases/sb0544). The OFAC Recent Actions / Press Releases pages list this as the most recent Sudan action, confirming no other Sudan-related designations occurred in the window.

2. That action added 5 individuals and 3 entities under the SUDAN-EO14098 program. Per the Treasury press release [Treasury Sanctions Networks Fueling Sudan's Civil War and ...](https://home.treasury.gov/news/press-releases/sb0544) and the Federal Register notice (Doc. 2026-13279) [[PDF] Office of Foreign Assets Control Notice of OFAC Sanctions Actions](https://public-inspection.federalregister.gov/2026-13279.pdf), and corroborated by the OFAC action page [https://ofac.treasury.gov/recent-actions/20260626](https://ofac.treasury.gov/recent-actions/20260626), the designees and their listed addresses are:
   - CHOUDHARI, Alok — Raipur, Chhattisgarh, India
   - DERMAN GUZMAN, Jack Peter — Panama City, Panama
   - LOPEZ OCAMPO, Fredy Alejandro — Panama City, Panama (Colombian national)
   - MADANI, Tariq Hussain Muhammad — Sudan
   - PALACIOS QUINTANILLA, Enrique Daniel — Panama City, Panama
   - PORTS ENGINEERING COMPANY LTD — Port Sudan, Sudan
   - SBL ENERGY LIMITED — Raipur, Chhattisgarh, India
   - TARGET MULTIACTIVITIES COMPANY LTD — Khartoum, Sudan

3. NONE of these eight new SDN additions has a listed address in the United Arab Emirates (UAE), Dubai, or Abu Dhabi [Treasury Sanctions Networks Fueling Sudan's Civil War and ...](https://home.treasury.gov/news/press-releases/sb0544) [[PDF] Office of Foreign Assets Control Notice of OFAC Sanctions Actions](https://public-inspection.federalregister.gov/2026-13279.pdf). The press release mentions that Ports Engineering imported uniforms from an "Emirati company," but that Emirati company was NOT itself designated in this action [Treasury Sanctions Networks Fueling Sudan's Civil War and ...](https://home.treasury.gov/news/press-releases/sb0544).

Therefore, the "UAE-based" and "Sudan-related" criteria were NOT met simultaneously for any single entity in the window. Although a genuine, new Sudan-related SDN designation occurred (June 26, 2026), no designee had a UAE address, so the question resolves NO.

Primary sources: OFAC Recent Actions entry for June 26, 2026 (https://ofac.treasury.gov/recent-actions/20260626); Treasury press release https://home.treasury.gov/news/press-releases/sb0544 [Treasury Sanctions Networks Fueling Sudan's Civil War and ...](https://home.treasury.gov/news/press-releases/sb0544); Federal Register notice https://public-inspection.federalregister.gov/2026-13279.pdf [[PDF] Office of Foreign Assets Control Notice of OFAC Sanctions Actions](https://public-inspection.federalregister.gov/2026-13279.pdf).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-182. `32a4ca25-4a4b-52f4-a73f-2e24a94c7899`

- Present date: `2026-05-14 07:15:56.842073`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the U.S. and Iran reach a publicly announced agreement including a nuclear enrichment moratorium of 10 years or longer by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026, and on or before July 1, 2026 (23:59 UTC), the U.S. and Iranian governments publicly announce an agreement that includes a nuclear enrichment moratorium of 10 years or longer. It resolves **No** otherwise.

**Key definitions:**

- **"Agreement"**: A signed memorandum of understanding (MOU), a joint public statement by authorized officials of both governments (e.g., the U.S. President or Secretary of State and Iran's President or Foreign Minister), or a formal treaty or framework document. A verbal statement by only one side, or leaked draft texts without official confirmation from both governments, do not qualify. (See https://en.wikipedia.org/wiki/Memorandum_of_understanding for MOU definition.)

- **"Nuclear enrichment moratorium"**: A formal commitment by Iran to halt all uranium enrichment activities (https://en.wikipedia.org/wiki/Uranium_enrichment), meaning the process of increasing the concentration of uranium-235 in natural uranium. This includes enrichment at all levels (whether above 3.67%, 20%, or 60%) and at all facilities. A partial halt covering only certain enrichment levels (e.g., only above 20%) qualifies only if the agreement explicitly describes it as a "moratorium" or "suspension" of enrichment.

- **"10 years or longer"**: The agreement must specify a moratorium duration of at least 120 months (10 years), measured from either (a) the date of implementation specified in the agreement, or (b) if no implementation date is specified, from the date of signing. An agreement that states a specific expiration date at least 10 years from implementation/signing also qualifies. Conditional extension clauses (e.g., "10 years, extendable to 15") qualify as long as the base commitment is at least 10 years.

- **"Deal framework"**: Refers to any of the document types listed under "Agreement" above. (See https://en.wikipedia.org/wiki/Framework_agreement.)

**Resolution sources:** Official statements from the White House (https://www.whitehouse.gov/) or Iran's presidency, or credible reporting from Reuters (https://www.reuters.com/), Associated Press (https://apnews.com/), the New York Times (https://www.nytimes.com/), or Axios (https://www.axios.com/).

**Pre-cutoff background**

As of May 12, 2026, the U.S. and Iran are negotiating a 14-point memorandum of understanding (MOU) aimed at ending the ongoing war and establishing a framework for further nuclear negotiations [https://www.axios.com/2026/05/06/iran-us-deal-one-page-memo](https://www.axios.com/2026/05/06/iran-us-deal-one-page-memo). According to an Axios report published May 6, 2026, the two sides are closer to an agreement than at any point since the war began, but nothing has been formally agreed upon yet [https://www.axios.com/2026/05/06/iran-us-deal-one-page-memo](https://www.axios.com/2026/05/06/iran-us-deal-one-page-memo).

A central point of contention is the duration of a moratorium on uranium enrichment (https://en.wikipedia.org/wiki/Uranium_enrichment). Iran initially proposed a 5-year moratorium, while the U.S. demanded 20 years [https://www.axios.com/2026/05/06/iran-us-deal-one-page-memo](https://www.axios.com/2026/05/06/iran-us-deal-one-page-memo). As of early May 2026, reports indicate negotiators are discussing a duration of "at least 12 years," with one source suggesting 15 years as a potential compromise [https://www.axios.com/2026/05/06/iran-us-deal-one-page-memo](https://www.axios.com/2026/05/06/iran-us-deal-one-page-memo). Separately, Anadolu Agency reported that the U.S. conveyed "conditional willingness" to accept a 10-year moratorium under certain conditions.

The proposed MOU would also involve the U.S. lifting sanctions and releasing frozen Iranian funds, both sides lifting restrictions on transit through the Strait of Hormuz, Iran committing to never seek a nuclear weapon, not operating underground nuclear facilities, and allowing enhanced inspections including snap inspections by UN inspectors [https://www.axios.com/2026/05/06/iran-us-deal-one-page-memo](https://www.axios.com/2026/05/06/iran-us-deal-one-page-memo). However, Iranian leadership remains divided, and previous rounds of talks have failed to produce a deal [https://www.axios.com/2026/05/06/iran-us-deal-one-page-memo](https://www.axios.com/2026/05/06/iran-us-deal-one-page-memo).

**Exact later resolution packet**

The question resolves NO. Although the U.S. and Iran did publicly announce and sign an agreement within the resolution window (a memorandum of understanding, June 15–17, 2026), that agreement did NOT include a nuclear enrichment moratorium of 10 years or longer. The moratorium/enrichment issue was explicitly deferred to a future "final Deal," and no such final deal specifying a ≥10-year moratorium was reached on or before July 1, 2026.

Key evidence:

1. The actual full text of the 14-point pact that the White House sent to Congress (Reuters, published June 17/updated June 18, 2026) is described as an "interim" agreement that "defers many of the most difficult issues, such as how to wind down Iran's nuclear program, until a final deal is reached." Point 8 states only that "the two Parties also agree to discuss the issue of enrichment ... based on a satisfactory framework being agreed upon in the final Deal." There is no 10-year (or any long-term) moratorium commitment in the signed text. [8d32c7] (https://www.reuters.com/world/middle-east/14-point-draft-us-iran-deal-2026-06-17/)

2. Reuters' summary of what both sides say is in the memorandum (June 15, 2026) confirms only a temporary freeze pending a final agreement: "pending a final agreement Iran would freeze its nuclear activity, refraining from further uranium enrichment," with the nuclear issue "conducted over the following 60 days." A ~60-day freeze is not a ≥10-year moratorium. [99faa5] (https://www.reuters.com/world/asia-pacific/what-us-iran-say-they-have-agreed-memorandum-end-war-2026-06-15/)

3. Reuters reporting on the signed MOU (June 15, 2026) states the pact "defers potentially complicated talks on containing Tehran's nuclear program." [bb1a63] (https://www.reuters.com/world/middle-east/trump-vance-irans-parliament-speaker-signed-mou-2026-06-15/)

4. AP (June 18, 2026) reports the signed initial agreement calls for Iran to "dilute its stockpile of highly enriched uranium" and starts a "60-day negotiating clock to reach a final deal," with no 10-year moratorium commitment. [621c9b] (https://apnews.com/article/iran-us-israel-war-oil-deal-june-17-2026-19652f4611b704c0a991bf1f5bc9a4b9)

5. Carnegie Endowment analysis (James Acton, June 18, 2026) of the MOU confirms it contains no long-term suspension of enrichment — the parties only agreed "to discuss the issue of enrichment" with the goal of a final agreement within 60 days. [8f8804] (https://carnegieendowment.org/emissary/2026/06/iran-deal-nuclear-weapons-clarity-history)

6. As of late June 2026, no final deal had been reached: NYT (June 28, 2026) reports negotiations were stalled and it was "not clear yet when or where Iran and the United States might meet again for talks." [bbc9a4] (https://www.nytimes.com/2026/06/28/world/europe/iran-us-strait-of-hormuz-peace-talks.html)

Note on conflicting reports: Some secondary/social-media summaries (e.g., Facebook posts attributed to CNN/The Hindu) claimed the 14-point deal included a "12–15 year" moratorium. However, these describe negotiating proposals rather than the actual signed text; the authoritative full-text reporting from Reuters and AP (both listed resolution sources) shows enrichment (including its duration) was explicitly deferred to a not-yet-concluded final deal. Since the agreement actually announced/signed by both governments within the window did not itself specify a ≥10-year enrichment moratorium, the resolution criteria are not met.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-183. `1d93e3be-4cae-573f-9cc6-908878b367c6`

- Present date: `2026-05-02 09:08:49.711625`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the Australian federal government announce a new policy or subsidy program specifically supporting domestic lithium chemical processing by June 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after April 30, 2026 (00:00 UTC+10 AEST) and on or before June 1, 2026 (23:59 UTC+10 AEST), the Australian federal government officially announces a new policy, subsidy program, grant program, or dedicated funding initiative that meets ALL of the following criteria:

1. **Explicitly names lithium processing**: The announcement must specifically reference "lithium" and domestic processing, refining, or chemical conversion (e.g., production of lithium hydroxide, lithium carbonate, or lithium sulfate from raw ore or spodumene concentrate). Spodumene concentrate production (i.e., crushing and concentrating ore) alone does not qualify — the program must target downstream chemical processing.

2. **Is a new federal initiative**: The program must be a new initiative not in effect prior to April 30, 2026, OR a formally announced expansion of an existing program that creates a distinct new lithium-processing-specific component with a specific new dollar commitment. Reaffirmations of existing programs (e.g., the Australia-US Critical Minerals Framework as announced on April 12–13, 2026) do not qualify unless they are formally expanded with a new, explicitly lithium-processing-targeted component.

3. **Constitutes a concrete policy or subsidy program**: The announcement must include at least one of the following: (a) a specific dollar amount of new funding allocated, (b) a new legislative bill introduced to Parliament, or (c) a formal grant or loan program with defined eligibility criteria. General statements of intent, aspirational policy positions, or feasibility studies alone do not qualify.

4. **Is a federal government initiative**: State-level programs (e.g., Western Australia's fee waivers) do not qualify.

**Resolution sources**: Official announcements on Australian government websites, including but not limited to pm.gov.au, minister.industry.gov.au, budget.gov.au, and industry.gov.au. In the absence of a direct government source, credible major news reporting from Reuters (reuters.com), ABC News Australia (abc.net.au), the Australian Financial Review (afr.com), or The Australian (theaustralian.com.au) may be used.

If no qualifying announcement is found by 23:59 AEST on June 1, 2026, the question resolves NO.

**Pre-cutoff background**

Australia is the world's largest lithium miner but exports most of its lithium as raw spodumene concentrate, with limited domestic chemical processing (e.g., conversion to lithium hydroxide or lithium carbonate). In February 2026, Albemarle shut down its Kemerton lithium hydroxide plant in Western Australia, widely described as a blow to the federal government's "Future Made in Australia" strategy [Australia and US boost support for critical minerals with $3.5 billion](https://www.reuters.com/world/china/australia-us-boost-support-critical-minerals-with-35-billion-2026-04-12/). This closure intensified political pressure on the government to support domestic lithium processing.

As of May 1, 2026, the Australian government has several broad critical minerals initiatives in place but none specifically dedicated to lithium processing:
- The "Future Made in Australia" plan commits A$22.7 billion to net-zero manufacturing broadly.
- A A$1.2 billion Critical Minerals Strategic Reserve was established in 2025.
- On April 12–13, 2026, Australia and the US announced over A$5 billion in funding for critical minerals projects under the Australia-US Critical Minerals Framework, supporting nickel, cobalt, gallium, magnesium, vanadium, graphite, and rare earths — but not specifically lithium processing [Australia-US Critical Minerals Framework investing in additional ...](https://www.minister.industry.gov.au/ministers/king/media-releases/australia-us-critical-minerals-framework-investing-additional-projects) [Australia and US boost support for critical minerals with $3.5 billion](https://www.reuters.com/world/china/australia-us-boost-support-critical-minerals-with-35-billion-2026-04-12/).
- Western Australia's state government extended a $30 million fee waiver for lithium hydroxide producers, but this is a state-level measure, not a new federal program.

No new federal policy or subsidy program specifically targeting domestic lithium processing has been announced as of April 30, 2026. The Australian federal budget is typically delivered in May, which could be a vehicle for such an announcement.

**Exact later resolution packet**

The question resolves NO. To resolve YES it required the Australian FEDERAL government to officially announce, between April 30 and June 1, 2026, a NEW policy/subsidy/grant/funding initiative that explicitly names lithium downstream chemical processing/refining (hydroxide/carbonate/sulfate), includes a concrete dollar amount/bill/eligibility-defined program, is genuinely new (not a reaffirmation of the April 12-13, 2026 Australia-US Critical Minerals Framework), and is federal (not WA state).

No such qualifying announcement was found:

1) The main potential vehicle was the 2026-27 federal budget, delivered in May 2026. The budget's "Security and investment" chapter (budget.gov.au) contains no new lithium-processing-specific initiative; its Critical Minerals Strategic Reserve focus is on antimony, gallium and rare earth elements, and other measures target aluminium, steel and manganese — lithium processing is not named as a dedicated new program [cbb400].

2) Industry analysis of the 2026-27 budget (Discovery Alert, published 2026-05-13) confirms the budget's critical minerals measures (Critical Minerals Production Tax Credit ~$7bn over 10 years covering all 31 listed minerals including lithium; Green Aluminium Production Credit $2bn; Green Iron Investment Fund $1bn; Green Metals Innovation Fund $750m; Resourcing Australia's Prosperity $566.1m) are broad-based and not a new lithium-processing-specific component with a distinct new dollar commitment. The production tax credit is an existing program (legislated Feb 2025) covering all 31 critical minerals, not a new lithium-processing-dedicated initiative [5bd6de].

3) The Wikipedia summary of the 2026 budget (budget delivered ~May 12, 2026) likewise shows the major new spending was on fuel security (~$10bn) and no lithium-processing-specific program [9afe9f].

4) The only lithium-hydroxide-specific support in this period was Western Australia's state-level $30m fee-waiver extension (April 21, 2026), which is explicitly excluded as a state measure (per search results, wa.gov.au).

5) The April 12-13, 2026 Australia-US Critical Minerals Framework (~A$5bn) explicitly did NOT include lithium processing and, being a reaffirmation/existing program, is excluded by the resolution criteria (Reuters; minister.industry.gov.au).

No federal announcement during the window naming lithium chemical processing/refining with a concrete new dollar commitment, bill, or defined grant/loan program was found in official Australian government sources or in Reuters/ABC/AFR/The Australian reporting. Per the resolution criteria, absent such an announcement, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-184. `8b451799-5178-5305-a946-aad3a6cd3626`

- Present date: `2026-05-16 12:38:24.059806`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Governor Hochul issue an emergency executive action explicitly mentioning the Long Island Rail Road (LIRR) between May 12, 2026 and July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 12, 2026 and on or before July 1, 2026 (11:59 PM Eastern Time / UTC-4), Governor Kathy Hochul issues an emergency executive action whose text explicitly mentions "Long Island Rail Road" or "LIRR."

An "emergency executive action" is defined as either:
1. A **New York State Executive Order** declaring or extending a State Disaster Emergency under Article 2-B, Section 28 of the New York Executive Law (https://www.nysenate.gov/legislation/laws/EXC/28), or
2. Any other **Executive Order** invoking emergency powers in connection with LIRR service, labor disputes, or transportation disruptions.

The text of the executive action itself must explicitly include the phrase "Long Island Rail Road" or "LIRR" to qualify.

**Resolution source:** The official New York State Governor's Executive Orders page at https://www.governor.ny.gov/executiveorders or the New York State Register at https://dos.ny.gov/state-register. The full text of any qualifying executive order must be publicly available at one of these sources.

If no such executive action is published on these sources by 11:59 PM ET on July 1, 2026, this question resolves **No**.

**Pre-cutoff background**

As of May 13, 2026, five unions representing approximately 3,500 Long Island Rail Road (LIRR) workers—including engineers, signalmen, and trainmen—are in active contract negotiations with the Metropolitan Transportation Authority (MTA). The unions have set a strike deadline of 12:01 a.m. on Saturday, May 16, 2026 [Possible LIRR strike could happen Saturday if no deal is reached](https://abc7ny.com/live-updates/possible-lirr-strike-2026-could-happen-saturday-no-deal-is-reached/19080853/). Negotiations are ongoing, with the most recent face-to-face session held on May 11, 2026 and another scheduled for May 13, 2026 [Possible LIRR strike could happen Saturday if no deal is reached](https://abc7ny.com/live-updates/possible-lirr-strike-2026-could-happen-saturday-no-deal-is-reached/19080853/).

Governor Kathy Hochul has stated she is "immersed in the details" of the negotiations and is receiving daily briefings, but as of May 13, 2026, she has not issued any executive order or emergency declaration related to LIRR [Possible LIRR strike could happen Saturday if no deal is reached](https://abc7ny.com/live-updates/possible-lirr-strike-2026-could-happen-saturday-no-deal-is-reached/19080853/). The MTA has prepared contingency plans including shuttle bus services in the event of a work stoppage [Possible LIRR strike could happen Saturday if no deal is reached](https://abc7ny.com/live-updates/possible-lirr-strike-2026-could-happen-saturday-no-deal-is-reached/19080853/).

At the federal level, President Trump previously established a Presidential Emergency Board (PEB) in September 2025 to investigate the dispute under the Railway Labor Act. The PEB sided with the union coalition, recommending raises and back pay. However, the 60-day cooling-off period following the PEB report is set to expire, allowing a strike as early as May 16, 2026 [Possible LIRR strike could happen Saturday if no deal is reached](https://abc7ny.com/live-updates/possible-lirr-strike-2026-could-happen-saturday-no-deal-is-reached/19080853/).

Governor Hochul's most recent executive orders include EO 60 (April 22, 2026, regarding insider information), EO 59 (April 10, 2026, naming the DOL building), and EO 58 (February 21, 2026, a disaster emergency declaration for winter weather in multiple counties) [Executive Orders | Governor Kathy Hochul | New York State](https://www.governor.ny.gov/executiveorders). None of these relate to LIRR.

Under New York Executive Law Article 2-B, Section 28, the Governor has authority to declare a State Disaster Emergency when conditions pose an imminent threat to public safety or welfare. Whether a transportation labor dispute qualifies is legally uncertain given that railroad labor relations are governed by the federal Railway Labor Act, which may preempt state action. This legal complexity, combined with political pressure to act, makes the question genuinely uncertain.

**Exact later resolution packet**

The question resolves NO. It required that, between May 12, 2026 and July 1, 2026, Governor Hochul issue an "emergency executive action" — defined as either (1) a NYS Executive Order declaring/extending a State Disaster Emergency under Executive Law Art. 2-B §28, or (2) another Executive Order invoking emergency powers in connection with LIRR service/labor disputes/transportation disruptions — whose official text explicitly contains "Long Island Rail Road" or "LIRR," published on governor.ny.gov/executiveorders or the NY State Register.

Evidence against any such executive order:
- The official NYS Governor's Executive Orders page (https://www.governor.ny.gov/executiveorders) shows the most recent executive orders were EO No. 60 (April 22, 2026), EO No. 59 (April 10, 2026), and EO No. 58 (February 21, 2026). No new Executive Order mentioning "Long Island Rail Road" or "LIRR" was issued during the May 12 – July 1, 2026 window [https://www.governor.ny.gov/executiveorders](https://www.governor.ny.gov/executiveorders).
- Although a LIRR strike did occur May 16–18, 2026, it was resolved through a voluntarily negotiated contract agreement between the MTA and the five unions, not via any state executive order or emergency declaration (the dispute was governed by the federal Railway Labor Act) [Governor Hochul Holds Briefing on Long Island Rail Road Strike](https://www.governor.ny.gov/news/b-roll-video-audio-photos-rush-transcript-governor-hochul-holds-briefing-long-island-rail-road) [Statement from Governor Kathy Hochul - NY.Gov](https://www.governor.ny.gov/news/statement-governor-kathy-hochul-165).
- Governor Hochul's actions during the strike were limited to press statements, public briefings (e.g., her May 17, 2026 briefing at https://www.governor.ny.gov/news/b-roll-video-audio-photos-rush-transcript-governor-hochul-holds-briefing-long-island-rail-road [Governor Hochul Holds Briefing on Long Island Rail Road Strike](https://www.governor.ny.gov/news/b-roll-video-audio-photos-rush-transcript-governor-hochul-holds-briefing-long-island-rail-road)), and a public statement (https://www.governor.ny.gov/news/statement-governor-kathy-hochul-165 [Statement from Governor Kathy Hochul - NY.Gov](https://www.governor.ny.gov/news/statement-governor-kathy-hochul-165)) urging parties back to the bargaining table and describing MTA contingency plans (shuttle buses, work-from-home). These are press releases/statements — NOT Executive Orders invoking emergency powers — and therefore do not satisfy the resolution criteria [Governor Hochul Holds Briefing on Long Island Rail Road Strike](https://www.governor.ny.gov/news/b-roll-video-audio-photos-rush-transcript-governor-hochul-holds-briefing-long-island-rail-road) [Statement from Governor Kathy Hochul - NY.Gov](https://www.governor.ny.gov/news/statement-governor-kathy-hochul-165).

Because no qualifying Executive Order (with text explicitly including "Long Island Rail Road" or "LIRR") was published on the specified official sources within the resolution window, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-185. `c280ee84-3ae8-5cdc-9b57-9cdf04f940a9`

- Present date: `2026-05-03 01:50:01.305577`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the European Commission approve a new price undertaking agreement for a Chinese-made battery electric vehicle model (beyond the Cupra Tavascan) between April 30 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the European Commission officially approves at least one new price undertaking agreement for a Chinese-made BEV model **on or after April 30, 2026, and by 23:59 UTC on June 1, 2026**. The Cupra Tavascan agreement approved on February 10, 2026 does not count.

A **"price undertaking agreement"** is defined as a binding commitment accepted by the European Commission under which an exporter agrees to minimum import prices and/or volume limits, thereby gaining exemption from countervailing or anti-dumping duties, as described in [Regulation (EU) 2016/1037, Article 13](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R1037).

A **"Chinese-made BEV model"** refers to any battery electric vehicle exported from China to the EU that is subject to the countervailing duties imposed under the Commission's anti-subsidy investigation into imports of BEVs originating in the People's Republic of China (Commission Implementing Regulation (EU) 2024/1866).

**Resolution source:** Official announcements on the European Commission DG TRADE newsroom at https://policy.trade.ec.europa.eu/news_en, or publication in the Official Journal of the European Union at https://eur-lex.europa.eu/. Confirmation from credible reporting (e.g., Reuters, Financial Times) of an official Commission decision is also sufficient.

**Pre-cutoff background**

The European Commission imposed countervailing duties on battery electric vehicles (BEVs) imported from China following an anti-subsidy investigation. Under EU trade law, exporters can negotiate a "price undertaking" — a commitment to sell at or above a minimum price and adhere to import volume limits — to be exempted from these duties.

On January 12, 2026, the Commission published a Guidance Document on the submission of price undertaking offers for BEVs from China (https://policy.trade.ec.europa.eu/news/commission-issues-guidance-document-submission-price-undertaking-offers-battery-electric-vehicles-2026-01-12_en). On February 10, 2026, the Commission accepted its first price undertaking from Volkswagen (Anhui) Automotive Company Ltd. for the Cupra Tavascan model, with its related EU party SEAT S.A. [https://www.reuters.com/business/aerospace-defense/china-commerce-minister-says-reached-soft-landing-with-eu-over-ev-tariffs-2026-04-28/](https://www.reuters.com/business/aerospace-defense/china-commerce-minister-says-reached-soft-landing-with-eu-over-ev-tariffs-2026-04-28/) [https://www.reuters.com/world/china/eu-tariffs-imports-china-made-evs-2026-02-11/](https://www.reuters.com/world/china/eu-tariffs-imports-china-made-evs-2026-02-11/). This remains the only approved price undertaking as of May 1, 2026.

China softened its stance in February 2026 on allowing individual Chinese EV makers to negotiate directly with the EU, and Chinese Commerce Minister Wang Wentao stated on April 28, 2026 that China and the EU had reached a "soft landing" in the broader tariff dispute [https://www.reuters.com/business/aerospace-defense/china-commerce-minister-says-reached-soft-landing-with-eu-over-ev-tariffs-2026-04-28/](https://www.reuters.com/business/aerospace-defense/china-commerce-minister-says-reached-soft-landing-with-eu-over-ev-tariffs-2026-04-28/). Multiple Chinese automakers are reportedly seeking similar deals, but the regulatory process is complex and politically sensitive, and no additional agreements have been confirmed.

**Exact later resolution packet**

RESOLUTION: NO (0).

The question asks whether the European Commission officially approved at least one NEW price undertaking agreement for a Chinese-made BEV model (beyond the Cupra Tavascan) on or after April 30, 2026, and by 23:59 UTC on June 1, 2026.

Evidence and method:
1. I searched Google for any new EU price undertaking decisions for Chinese BEVs in May 2026, then directly examined the two designated/most authoritative resolution sources.

2. European Commission DG TRADE Newsroom (https://policy.trade.ec.europa.eu/news_en) — the primary named resolution source. A review of the news feed covering the period April 20, 2026 through June 2, 2026 contained NO announcement of any new price undertaking for Chinese BEVs. The only undertaking-acceptance news item remains the February 10, 2026 announcement for Volkswagen (Anhui)/SEAT (Cupra Tavascan) [https://policy.trade.ec.europa.eu/news_en](https://policy.trade.ec.europa.eu/news_en).

3. The official EU trade defence investigation case history for the Chinese BEV anti-subsidy case (https://tron.trade.ec.europa.eu/investigations/case-history?caseId=2684) lists only ONE Commission Implementing Decision accepting a price undertaking: Commission Implementing Decision (EU) 2026/328 of 9 February 2026 (the Cupra Tavascan undertaking). No further undertaking-acceptance decision is recorded dated between April 30 and June 1, 2026 [battery electric vehicles - Trade defence investigations](https://tron.trade.ec.europa.eu/investigations/case-history?caseId=2684).

4. Broader Google searches (Reuters/FT/Borderlex and trade-press coverage) surfaced only the January 12, 2026 guidance document and the February 2026 first/only undertaking; multiple automakers were reportedly seeking deals, but no additional Commission approval was confirmed within the window.

Because the antecedent event (Commission approval of a new, non-Tavascan price undertaking within the window) did NOT occur, the question resolves NO. (The Tavascan undertaking that does exist is itself a price undertaking under Article 13 of Regulation (EU) 2016/1037, accepted via Decision (EU) 2026/328, confirming the regulatory mechanism the question references — but it is explicitly excluded and falls outside the resolution window in any case.)

Sources:
- https://policy.trade.ec.europa.eu/news_en
- https://tron.trade.ec.europa.eu/investigations/case-history?caseId=2684
- https://policy.trade.ec.europa.eu/news/commission-accepts-price-undertaking-chinese-electric-car-producer-2026-02-10_en

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-186. `22d31016-8936-57f0-bbb4-0e368d5c7db1`

- Present date: `2026-05-02 16:59:15.198229`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will any G7 nation announce a new broad-based energy price cap or untargeted energy subsidy program between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if any G7 nation—defined as **Canada, France, Germany, Italy, Japan, the United Kingdom, or the United States**—officially announces a new broad-based energy price cap or untargeted energy subsidy program on or after 00:00 UTC May 1, 2026 and on or before 23:59 UTC June 1, 2026. It resolves **No** otherwise.

**Definitions:**

- **"Broad-based" / "Untargeted":** A program that is not restricted by income level, means-testing, or specific vulnerability criteria, and is available to the general population or all consumers of a particular energy type (e.g., all retail gasoline consumers, all residential electricity customers). A program limited to a specific industry sector (e.g., only farming or fishing) does NOT qualify.
- **"Energy price cap":** A government-mandated maximum price that can be charged for an energy commodity (electricity, natural gas, gasoline, diesel, heating oil) at the retail or wholesale level.
- **"Energy subsidy program":** A government-funded program that directly reduces the retail price of energy for consumers, including direct payments, tax reductions, or excise duty cuts applied broadly to all consumers of the energy type.

**Exclusions:**
- Programs announced before May 1, 2026 do not count, even if they remain in effect during the resolution window.
- Extensions or renewals of existing programs without a materially new untargeted component do not count.
- Strategic petroleum reserve releases do not count.
- Regulatory price caps that existed prior to May 1, 2026 (e.g., the UK's Ofgem price cap) do not count unless a new, additional broad cap is announced.

**Resolution source:** Official government press releases, government gazettes, or reporting from at least one of the following: Reuters (https://www.reuters.com), Bloomberg (https://www.bloomberg.com), Associated Press (https://apnews.com), or Agence France-Presse (https://www.afp.com).

**Pre-cutoff background**

The 2026 Iran war and closure of the Strait of Hormuz have triggered the most significant energy market disruption since the 2022 European gas crisis. Brent crude surged 10–13% to $80–82/barrel by early March 2026 and briefly touched ~$118/barrel, with forecasts of further increases [https://www.imf.org/en/blogs/articles/2026/04/14/war-darkens-global-economic-outlook-and-reshapes-policy-priorities](https://www.imf.org/en/blogs/articles/2026/04/14/war-darkens-global-economic-outlook-and-reshapes-policy-priorities). The IMF has explicitly warned against "untargeted measures—price caps, subsidies, and similar interventions," recommending instead that fiscal support be "narrowly targeted and temporary" [https://www.imf.org/en/blogs/articles/2026/04/14/war-darkens-global-economic-outlook-and-reshapes-policy-priorities](https://www.imf.org/en/blogs/articles/2026/04/14/war-darkens-global-economic-outlook-and-reshapes-policy-priorities).

As of late March 2026, G7 nations have adopted the following energy measures [What G7 countries are doing to cap energy prices - Reuters](https://www.reuters.com/business/energy/what-g7-countries-are-doing-cap-energy-prices-2026-03-30/):

- **United States:** Contributing 172 million barrels to a coordinated IEA strategic reserve release. No broad consumer subsidies announced.
- **Canada:** Contributing 23.6 million barrels to the IEA reserve release. No broad consumer subsidies announced.
- **Germany:** Has opted not to subsidize prices; instead restricting petrol stations to one daily price increase.
- **France:** Providing targeted sector support (€70M+ for transport, farming, fishing) and a €150 benefit for 3.8 million low-income households. No broad untargeted subsidy.
- **United Kingdom:** Households protected by Ofgem-regulated tariffs until July 2026. A £53M package for heating oil users announced. No new broad subsidy.
- **Italy:** Implemented excise duty cuts on petrol and diesel (effective until April 7, 2026).
- **Japan:** Using ¥800 billion in reserve funds to subsidize gasoline prices, aiming for an average of ¥170/liter.

The G7 comprises: **Canada, France, Germany, Italy, Japan, the United Kingdom, and the United States**.

Political pressure to expand interventions beyond targeted measures remains high. During the 2022 energy crisis, multiple G7 nations adopted broad price caps despite similar IMF advice against them [https://www.imf.org/en/blogs/articles/2026/04/14/war-darkens-global-economic-outlook-and-reshapes-policy-priorities](https://www.imf.org/en/blogs/articles/2026/04/14/war-darkens-global-economic-outlook-and-reshapes-policy-priorities). The question tests whether any G7 government will move from targeted to broad-based interventions during May 2026.

Note: Italy's excise duty cuts and Japan's gasoline subsidies, as described above, are pre-existing programs announced before May 1, 2026, and do not count toward resolution unless a new, broader program is announced.

**Exact later resolution packet**

The question resolves NO. No G7 nation (Canada, France, Germany, Italy, Japan, UK, US) announced a *new* broad-based/untargeted energy price cap or subsidy program between 00:00 UTC May 1, 2026 and 23:59 UTC June 1, 2026. Reviewing each country using Reuters and the IEA tracker:

- ITALY: On May 19, 2026, Italy prolonged its fuel excise duty cut due to expire May 22. Reuters confirms this "measure was introduced in March and first extended in late April," making the May action an extension of a pre-existing program — explicitly excluded by the resolution criteria ("Extensions or renewals of existing programs without a materially new untargeted component do not count") [c61f47]. (https://www.reuters.com/business/italy-extend-fuel-excise-duty-cut-expiring-this-week-minister-says-2026-05-19/)

- FRANCE: On May 21, 2026, PM Sébastien Lecornu explicitly RULED OUT broad fuel tax cuts, saying "We refuse any general, indiscriminate reduction of fuel taxes." The €710M package announced May 21–22 consisted entirely of TARGETED measures: extension of fishing/farming sector support, a bonus for taxi drivers, increased low-income commuter subsidies, and an employee tax-free commuting bonus — none broad-based [1db864, 7e20d9]. A €100 fuel aid scheme that opened May 27 is means-tested/targeted (eligibility criteria) [d56540]. (https://www.reuters.com/business/energy/french-pm-rules-out-broad-tax-cuts-fuels-amid-tight-budget-constraints-2026-05-21/)

- JAPAN: Activity in May 2026 (e.g., setting subsidy at ¥42.6/liter on May 13, switching the crude benchmark on May 27) were adjustments/operations of the pre-existing ¥800 billion gasoline subsidy program announced before May 1, 2026 — explicitly excluded by the question. No new broad program was created in the window. (https://www.reuters.com/business/energy/japan-switch-back-dubai-crude-gasoline-subsidy-calculation-june-4-2026-05-27/)

- GERMANY: Germany's industrial electricity price subsidy is restricted to energy-intensive companies (specific sectors), not the general population, so it is not "broad-based/untargeted"; it also began January 1, 2026, predating the window.

- UK: Households remain under the pre-existing Ofgem regulated price cap (explicitly excluded). No new additional broad cap was announced in the window.

- CANADA & US: No new broad consumer energy subsidy or price cap announced in the window.

The IEA 2026 Energy Crisis Policy Response Tracker (last updated May 28, 2026) and the Reuters roundup "Governments worldwide shield households from rising energy costs" (May 26, 2026) corroborate that no G7 nation introduced a new broad-based untargeted energy subsidy/price cap in the May window [9e3622, ddbd72]. Strategic petroleum reserve releases are excluded by the criteria. Therefore the answer is NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-187. `09d47e52-182a-550f-80ee-fd70a0a422ae`

- Present date: `2026-05-07 16:46:22.667326`
- Source cutoff boundary: `2026-05-08` (encodes end of UTC day `2026-05-07`)
- Expected resolution: `2026-06-13T00:00:00`

**Question**

Will Apple announce a new third-party AI model integration for Apple Intelligence (beyond OpenAI/ChatGPT and Google Gemini) at WWDC 2026?

**Resolution criteria**

This question resolves YES if, on or after May 6, 2026, Apple officially announces during the WWDC 2026 keynote (June 8, 2026, expected ~10:00 AM PT / 17:00 UTC) or in official Apple Newsroom press releases (https://www.apple.com/newsroom/) published between June 8–12, 2026, a new integration of a third-party generative AI model into Apple Intelligence features.

For this question:
- "Third-party AI model" means a large language model or generative AI model developed by a company other than Apple — for example, Anthropic's Claude, Meta's Llama, Mistral, or any other external AI provider.
- This explicitly **excludes** OpenAI/ChatGPT and Google Gemini, as those integrations were already announced prior to May 6, 2026.
- "Integration" means the model is officially announced as being incorporated into user-facing Apple Intelligence features (e.g., Siri, Writing Tools, Image Playground, Visual Intelligence, or similar).
- The announcement must come from Apple itself (via the WWDC keynote video at https://developer.apple.com/wwdc26/ or Apple Newsroom at https://www.apple.com/newsroom/), not from third-party reports or rumors.

This question resolves NO if no such new third-party AI model integration is announced by Apple during WWDC 2026 (June 8–12, 2026).

**Pre-cutoff background**

Apple Intelligence is Apple's suite of AI-powered features integrated across its devices, first announced at WWDC 2024 (https://en.wikipedia.org/wiki/Apple_Intelligence). At WWDC 2025 (June 9, 2025), Apple announced expanded ChatGPT integration into Apple Intelligence features including Image Playground, Visual Intelligence, Writing Tools, Siri, and Shortcuts [Apple Intelligence gets even more powerful with new capabilities ...](https://www.apple.com/newsroom/2025/06/apple-intelligence-gets-even-more-powerful-with-new-capabilities-across-apple-devices/). No additional third-party AI model integrations were announced at WWDC 2025.

In January 2026, Apple and Google announced a non-exclusive, multi-year partnership under which Google's Gemini models and cloud technology would power future Apple foundational models and a revamped Siri [Google's Gemini to power Apple's AI features like Siri - TechCrunch](https://techcrunch.com/2026/01/12/googles-gemini-to-power-apples-ai-features-like-siri/). Reports indicate Apple may be paying Google approximately $1 billion annually for this access [Google's Gemini to power Apple's AI features like Siri - TechCrunch](https://techcrunch.com/2026/01/12/googles-gemini-to-power-apples-ai-features-like-siri/). The partnership is explicitly non-exclusive, meaning Apple retains the ability to work with other AI providers [Google's Gemini to power Apple's AI features like Siri - TechCrunch](https://techcrunch.com/2026/01/12/googles-gemini-to-power-apples-ai-features-like-siri/).

WWDC 2026 is scheduled for June 8–12, 2026, with the keynote on June 8 at Apple Park in Cupertino (https://developer.apple.com/wwdc26/). A major focus is expected to be iOS 27 and an updated version of Siri described as a "chatbot version" [WWDC 2026: Everything to Expect - MacRumors](https://www.macrumors.com/roundup/wwdc/). As of May 7, 2026, Apple has confirmed partnerships with OpenAI (ChatGPT) and Google (Gemini) for Apple Intelligence but has not announced any additional third-party AI model integrations. Apple reportedly tested technology from Anthropic during the lead-up to the Google deal [Google's Gemini to power Apple's AI features like Siri - TechCrunch](https://techcrunch.com/2026/01/12/googles-gemini-to-power-apples-ai-features-like-siri/), leaving open the possibility of future partnerships with other providers.

"Third-party AI model integration" refers to a publicly announced partnership where a generative AI model developed by a company other than Apple is incorporated into Apple Intelligence features (such as Siri, Writing Tools, Image Playground, or similar) in a user-facing capacity, analogous to the existing ChatGPT or Gemini integrations.

**Exact later resolution packet**

RESOLUTION: NO (0).

The question resolves YES only if, during WWDC 2026 (June 8–12, 2026), Apple itself (via the keynote or Apple Newsroom) officially announced a NEW third-party generative AI model — other than OpenAI/ChatGPT and Google Gemini — integrated into USER-FACING Apple Intelligence features (e.g., Siri, Writing Tools, Image Playground, Visual Intelligence). It resolves NO otherwise.

WHAT APPLE OFFICIALLY ANNOUNCED (all from official Apple Newsroom, June 8, 2026):
- The Siri AI press release states Siri AI is "powered by Apple Intelligence" using "the next generation of Apple Foundation Models that run on device and on servers using Private Cloud Compute," and gets world knowledge generically ("Siri AI can use broad world knowledge to get up-to-date information from the web"). It names NO third-party AI provider — no ChatGPT, no Claude, no Extensions model-picker [db37e1, 743a82].
- The "Apple Intelligence brings powerful AI capabilities into everyday experiences" release states the features are powered by "the next generation of Apple Foundation Models, custom-built in collaboration with Google and its Gemini models." No other third-party model (Anthropic Claude, Meta Llama, Mistral, etc.) is named [6dc30b].
- The main "Apple unveils next generation of Apple Intelligence, Siri AI, and more" release and the "across services" release name no new third-party model integration into user-facing features [95fed3, 05acc9].
- The Apple Intelligence product page lists no third-party model choice for users [897000]; Apple Support still documents only the ChatGPT extension for user-facing Siri/Writing Tools world knowledge (no Claude equivalent found).

THE ONE NEW THIRD-PARTY MODEL ("Claude") APPLE DID MENTION IS DEVELOPER-FACING, NOT USER-FACING:
- The "Apple aids app development with new intelligence frameworks and advanced tools" release says developers "can also easily leverage models of their choice, like Claude and Gemini, or those from any other provider that implements the new language model protocol," and that Xcode 27 brings "models and agents from Anthropic, Google, and OpenAI directly into a developer's workflow." This is the Foundation Models framework / Xcode coding tools — for developers to build features into THEIR OWN apps, not Apple integrating Claude into Apple's own user-facing Apple Intelligence features [e050c8].
- The WWDC26 developer guide confirms this is a developer Swift API ("You can now work with any language model, including Apple Foundation Models, cloud models like Claude and Gemini, or any other provider that conforms to the Language Model protocol"), not a user-facing setting to swap the model behind Siri/Writing Tools [3ebadb].
- MacRumors' coverage of the Platforms State of the Union likewise describes "server-side model integration allowing developers to call third-party models like Claude and Gemini through the same Swift API" — developer-facing [ef4a15].

The resolution criteria explicitly define "Integration" as the model being "incorporated into user-facing Apple Intelligence features (e.g., Siri, Writing Tools, Image Playground, Visual Intelligence, or similar)." The developer Foundation Models framework does not meet this bar.

USER-FACING CLAUDE FOR SIRI WAS ONLY RUMORED, NOT OFFICIALLY ANNOUNCED:
- WIRED's full WWDC 2026 recap confirms Apple's official story centered on Apple's own models integrated with Google Gemini, and that Claude integration "remains a matter of third-party speculation or past testing, not an official announcement from Apple at WWDC 2026" [8f8fb0].
- Numerous secondary outlets describe an iOS 27 "Extensions" system letting users pick Claude, but consistently qualify it as "reportedly" (e.g., Tom's Guide, eCorpIT), i.e., rumor/report — which the resolution criteria explicitly exclude ("must come from Apple itself... not from third-party reports or rumors").

CONCLUSION: Apple did not officially announce, in the WWDC 2026 keynote or in Apple Newsroom releases (June 8–12, 2026), a new integration of a third-party generative AI model (beyond OpenAI/ChatGPT and Google Gemini) into user-facing Apple Intelligence features. The only new third-party model reference (Claude) was a developer framework capability, which does not satisfy the user-facing requirement. Therefore the question resolves NO.

Key sources:
- Siri AI release: https://www.apple.com/newsroom/2026/06/apple-introduces-siri-ai-a-profoundly-more-capable-and-personal-assistant/
- Apple Intelligence everyday experiences: https://www.apple.com/newsroom/2026/06/apple-intelligence-brings-powerful-ai-capabilities-into-everyday-experiences/
- Developer frameworks release (Claude, developer-facing): https://www.apple.com/newsroom/2026/06/apple-aids-app-development-with-new-intelligence-frameworks-and-advanced-tools/
- WWDC26 developer guide: https://developer.apple.com/wwdc26/guides/apple-intelligence/

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-188. `953e756d-9a3f-50d9-a181-0f4cbe273d7b`

- Present date: `2026-05-02 23:36:57.525447`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will NASA begin stacking the Artemis III SLS core stage onto the Mobile Launcher in the Vehicle Assembly Building by June 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after May 1, 2026 (00:00 UTC) and on or before June 1, 2026 (23:59 UTC), NASA officially confirms that the Artemis III SLS core stage has been lifted by crane for vertical integration onto the Mobile Launcher inside the Vehicle Assembly Building (VAB) at Kennedy Space Center. Specifically, "stacking" is defined as the moment the core stage is first lifted by crane for placement onto the Mobile Launcher; pre-stacking activities such as horizontal processing, inspections, mating of the core stage upper section to the engine section, or transportation within the VAB transfer aisle do NOT count.

The arrival and preparation activities that occurred in late April 2026 (including the April 27-28 delivery and roll into the VAB) are explicitly excluded from resolution.

Resolution will be determined by official NASA sources, primarily the NASA Artemis Blog (https://www.nasa.gov/blogs/artemis/) or the Kennedy Space Center Newsroom (https://www.nasa.gov/kennedy/news/). If NASA confirms stacking has begun via an official blog post, press release, or verified NASA social media account by the deadline, the question resolves YES. Otherwise, it resolves NO.

**Pre-cutoff background**

On April 27, 2026, the top four-fifths of the SLS (Space Launch System) core stage for NASA's Artemis III mission arrived at Kennedy Space Center (KSC) via the Pegasus barge, and was offloaded and rolled into the transfer aisle of the Vehicle Assembly Building (VAB) on April 28, 2026 [NASA's Artemis Core Stage Arrives at Kennedy](https://www.nasa.gov/blogs/missions/2026/04/27/nasas-artemis-core-stage-arrives-at-kennedy/) [NASA's Artemis III Moon Rocket Hardware Progressing](https://www.nasa.gov/blogs/missions/2026/04/28/nasas-artemis-iii-moon-rocket-hardware-arrives-artemis-ii-capsule-returns-to-kennedy/). The engine section and boat-tail had previously been delivered and integrated in High Bay 2 of the VAB in August 2025 [NASA's Artemis III Moon Rocket Hardware Progressing](https://www.nasa.gov/blogs/missions/2026/04/28/nasas-artemis-iii-moon-rocket-hardware-arrives-artemis-ii-capsule-returns-to-kennedy/).

The next major processing milestone is joining the core stage upper section with the engine section/boat-tail in High Bay 2, followed by vertical integration ("stacking") of the assembled core stage onto the Mobile Launcher—the platform from which the rocket will eventually launch. As of late April 2026, NASA teams are conducting inspections and preparation work on the core stage before stacking can begin [NASA's Artemis III Moon Rocket Hardware Progressing](https://www.nasa.gov/blogs/missions/2026/04/28/nasas-artemis-iii-moon-rocket-hardware-arrives-artemis-ii-capsule-returns-to-kennedy/). Historical Artemis processing timelines have experienced delays, creating genuine uncertainty about whether stacking will commence within roughly one month of arrival.

Key terms:
- **SLS core stage**: The largest element of NASA's Space Launch System rocket, containing liquid hydrogen and liquid oxygen tanks and serving as the rocket's backbone. See: https://www.nasa.gov/humans-in-space/space-launch-system/
- **Vehicle Assembly Building (VAB)**: The massive facility at Kennedy Space Center where NASA's rockets are assembled vertically. See: https://en.wikipedia.org/wiki/Vehicle_Assembly_Building
- **Mobile Launcher**: The tower and platform structure used to assemble, process, and launch the SLS rocket. See: https://www.nasa.gov/humans-in-space/exploration-ground-systems/mobile-launcher/
- **Stacking**: In this context, the act of lifting the assembled core stage vertically by crane and placing it onto the Mobile Launcher inside the VAB for integration with the solid rocket boosters.

**Exact later resolution packet**

The question resolves NO. It asked whether NASA officially confirmed, between May 1 and June 1, 2026, that the Artemis III SLS core stage was lifted by crane for vertical integration ("stacking") onto the Mobile Launcher inside the VAB.

Key evidence:

1. NASA's official Artemis III mission page ("NASA Outlines Preliminary Artemis III Mission Plans," nasa.gov/missions/artemis/artemis-3/, last updated May 19, 2026) states that as of May 12, 2026, the Artemis III core stage was sitting in High Bay 2 of the VAB with the core stage tank attached to its engine section [2c9f6b]. This event — mating the core stage upper section/tank to the engine section — is explicitly EXCLUDED by the question's resolution criteria. There is no NASA confirmation of the core stage being lifted by crane onto the Mobile Launcher up to that point [2c9f6b].

2. An Aerospace America article (April 13, 2026) reporting NASA's stated schedule says: "The agency is targeting August to stack the SRBs and October to stack the core stage" [5d4474]. With core-stage stacking targeted for October 2026, it could not possibly have begun by the June 1, 2026 deadline.

The distinction required by the checklist is clearly met: the May 12, 2026 milestone was the horizontal mating of the core stage tank to the engine section in High Bay 2 (excluded), NOT the crane lift onto the Mobile Launcher (the target event), which NASA scheduled for October 2026. Therefore no qualifying event occurred within the May 1 – June 1, 2026 window, and the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-189. `405a8bae-e80e-5e7c-ab38-eab1d264be5a`

- Present date: `2026-05-14 08:33:27.801387`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Costa Rica's Constitutional Chamber (Sala IV) issue a ruling challenging or suspending Rodrigo Chaves's appointment as a cabinet minister by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026, and no later than July 1, 2026, 23:59 Costa Rica time (UTC-6), the Constitutional Chamber of the Supreme Court of Costa Rica (Sala IV) issues a formal ruling that does any of the following regarding Rodrigo Chaves's appointment as Minister of the Presidency or Minister of Finance in the Fernández administration:

1. **Injunction**: Issues an injunction (medida cautelar) suspending or halting the appointment;
2. **Declaration of unconstitutionality**: Declares the appointment unconstitutional; or
3. **Stay of appointment**: Orders a stay preventing Chaves from exercising ministerial functions.

The question resolves **No** if no such ruling is issued by the deadline.

**Included courts**: Only rulings from the Constitutional Chamber (Sala IV) of the Supreme Court of Costa Rica count. Rulings from lower courts, other chambers of the Supreme Court, or administrative bodies do not qualify.

**Resolution sources**: Resolution will be determined by official publications on the Costa Rican judiciary portal (Poder Judicial de Costa Rica: https://www.poder-judicial.go.cr/) or credible reporting from at least one of the following: AP News (https://apnews.com), Reuters (https://reuters.com), La Nación Costa Rica (https://www.nacion.com), or El País (https://elpais.com).

**Pre-cutoff background**

On May 8, 2026, Laura Fernández was sworn in as President of Costa Rica. Outgoing President Rodrigo Chaves was immediately appointed to serve as both Minister of the Presidency and Minister of Finance in the new Fernández administration [https://apnews.com/article/laura-fernandez-costa-rica-chaves-trump-aa0c3ea1712f6ee67235fb1bf6317ac2](https://apnews.com/article/laura-fernandez-costa-rica-chaves-trump-aa0c3ea1712f6ee67235fb1bf6317ac2). This appointment is highly controversial because it grants Chaves continued legal immunity from prosecution on concusión (extortion/coercion) charges that had been pursued by the Public Prosecutor's Office. The Costa Rican legislature twice failed to strip Chaves's presidential immunity — in September 2025 and December 2025 [https://apnews.com/article/laura-fernandez-costa-rica-chaves-trump-aa0c3ea1712f6ee67235fb1bf6317ac2](https://apnews.com/article/laura-fernandez-costa-rica-chaves-trump-aa0c3ea1712f6ee67235fb1bf6317ac2). The Constitutional Chamber of the Supreme Court (Sala IV) had previously sought to strip his immunity in July 2025. Critics view the appointment as a maneuver to shield Chaves from criminal prosecution. As of May 12, 2026, Chaves holds both ministerial posts and retains immunity. The Fernández administration holds a legislative majority, which may complicate judicial intervention, but the Sala IV has historically demonstrated independence in constitutional matters.

**Exact later resolution packet**

RESOLUTION: NO (0).

The question resolves YES only if, between May 12, 2026 and July 1, 2026 (23:59 UTC-6), Costa Rica's Constitutional Chamber (Sala IV) issued a formal ruling that (1) issued an injunction/medida cautelar suspending the appointment, (2) declared the appointment unconstitutional, or (3) ordered a stay preventing Chaves from exercising ministerial functions. No such ruling was issued within that window.

Key evidence:

1. OFFICIAL SOURCE (Poder Judicial): The Constitutional Chamber's own press-release page (salaconstitucional.poder-judicial.go.cr/index.php/sala-de-prensa/comunicados) contains no ruling of any kind regarding Chaves's ministerial appointment. The most recent communication as of the review was dated June 11–12, 2026, and concerned the lack of appointment of substitute magistrates by the Legislative Assembly — not Chaves's cabinet posts [c9022b].

2. NO CHALLENGE TO THE APPOINTMENT BEFORE SALA IV: The three legal actions pending before the Sala IV that were reported by La Nación (recursos de amparo exp. 26-008255-0007-CO and 26-008226-0007-CO, and acción de inconstitucionalidad exp. 26-008212-0007-CO) all challenge the March 2026 "Joint Security Declaration"/"Escudo de las Américas" military-alliance matter, not Chaves's appointment as Minister of the Presidency or Finance [9849fd].

3. CHAVES CONTINUED TO EXERCISE MINISTERIAL FUNCTIONS UNIMPEDED through the entire window and beyond: he appeared before the Legislative Assembly (June 3, 2026), presented a fiscal plan to President Fernández, and on June 24, 2026 announced budget cuts (~₡27,000 million) as Minister of Finance, and questioned the Attorney General. This is direct evidence that no stay/injunction/unconstitutionality declaration removed him from office (per contemporaneous reporting from El Financiero, Semanario Universidad, and multiple outlets found via search).

4. CONTEXT REDUCING LIKELIHOOD OF ANY RULING: The Sala IV was operating at reduced capacity during this period because the Legislative Assembly had not appointed substitute magistrates; reporting (CRHoy, June 14, 2026) noted that this even blocked advancement of the pre-existing criminal case against Chaves — making a decisive ruling against his appointment even less feasible.

5. The Divergentes analysis of the "superminister" appointment (published/updated through June 30, 2026) confirms the appointment and the resulting immunity but reports no Sala IV ruling invalidating or suspending it [762dd3].

The premise/antecedent of the question (that Chaves was appointed and holds both ministerial posts) did occur, so the question is not annulled; it resolves on the consequent, which did not occur. Therefore: NO.

Sources:
- https://salaconstitucional.poder-judicial.go.cr/index.php/sala-de-prensa/comunicados [c9022b]
- https://www.nacion.com/politica/tres-acciones-legales-buscan-anular-acuerdos-de/O2KZRFATZRD7FLJ6YYX34ANNTA/story/ [9849fd]
- https://www.divergentes.com/rodrigo-chaves-superministro-laura-fernandez-costa-rica-analisis/ [762dd3]
- Contemporaneous reporting of Chaves acting as Minister of Finance/Presidency in June 2026 (e.g., elfinancierocr.com plan-fiscal coverage; crhoy.com "Falta de magistrados suplentes impide avance de causa penal contra Rodrigo Chaves", June 14, 2026).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-190. `e1f9b58f-6963-5950-abae-814ea7f10967`

- Present date: `2026-05-03 03:53:43.826487`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will a veto be cast in the UN Security Council between May 1, 2026, and May 31, 2026?

**Resolution criteria**

This question resolves **Yes** if at least one veto is cast by a permanent member of the UN Security Council (China, France, Russia, the United Kingdom, or the United States) on a substantive (non-procedural) draft resolution between **00:00 UTC on May 1, 2026** and **23:59 UTC on May 31, 2026**. It resolves **No** otherwise.

A "veto" is defined as a negative vote cast by a permanent member on a substantive (non-procedural) matter, in accordance with [Article 27 of the UN Charter](https://en.wikipedia.org/wiki/United_Nations_Security_Council_veto_power), which prevents the adoption of the draft resolution.

Resolution will be determined by the official vetoes list maintained by the United Nations Dag Hammarskjöld Library, available at: https://research.un.org/en/docs/sc/quick [https://research.un.org/en/docs/sc/quick](https://research.un.org/en/docs/sc/quick). If this list reflects one or more vetoes occurring within the specified time window, the question resolves Yes. If the UN source is temporarily unavailable, credible reporting from Reuters, AP, or the UN News website (https://news.un.org) may serve as a secondary source.

**Pre-cutoff background**

The [United Nations Security Council](https://en.wikipedia.org/wiki/United_Nations_Security_Council) (UNSC) is the principal organ responsible for international peace and security. Under [Article 27 of the UN Charter](https://en.wikipedia.org/wiki/United_Nations_Security_Council_veto_power), each of the five permanent members (P5)—China, France, Russia, the United Kingdom, and the United States—holds veto power over substantive (non-procedural) resolutions. A single negative vote from any P5 member blocks adoption of a draft resolution, regardless of the level of support from other Council members.

The most recent veto was cast on April 7, 2026, when Russia and China vetoed a draft resolution concerning the Strait of Hormuz [https://research.un.org/en/docs/sc/quick](https://research.un.org/en/docs/sc/quick). Prior vetoes in 2025 occurred on September 18, June 4, and February 24, indicating a rough frequency of one veto every 2–4 months. The current geopolitical environment—marked by ongoing Middle East tensions, the Hormuz crisis, and other active conflicts—creates conditions where new draft resolutions could be tabled and vetoed during May 2026. However, vetoes do not occur every month, making the outcome uncertain.

The official record of all UNSC vetoes is maintained by the UN Dag Hammarskjöld Library at https://research.un.org/en/docs/sc/quick [https://research.un.org/en/docs/sc/quick](https://research.un.org/en/docs/sc/quick).

**Exact later resolution packet**

Adjudicated: The only relevant veto (China and Russia on the Strait of Hormuz draft resolution) was cast on 7 April 2026, outside the May 1-31, 2026 window. Per the UN veto record and corroborating UN News, PBS, and the Wikipedia veto list, no veto was cast in May 2026; the most recent veto as of June 2026 remains 7 April 2026. An initial automated pass misattributed the April 7 veto to 'May 7' — May 7 was only when the US circulated a modified draft to evade the veto, which was never put to a vote in May.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-191. `c7840c6b-b160-5789-9ad7-ec52fddb8840`

- Present date: `2026-05-29 02:10:18.201151`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will France fully enact its under-15 social media ban into law before July 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after May 12, 2026 (00:00 UTC) and before July 1, 2026 (23:59 UTC), France fully enacts legislation establishing a minimum age of 15 for independent access to social media platforms.

**"Fully enacts"** means the legislation has completed all stages of the French legislative process, including: (a) adoption of an identical text by both the National Assembly and the Senate (or adoption via the procedure in Article 49.3 of the Constitution), AND (b) promulgation (signature) by the President of the Republic, AND (c) publication in the Journal Officiel de la République Française (https://www.legifrance.gouv.fr/). Publication in the Journal Officiel is the definitive indicator of enactment.

**"Social media platforms"** refers to online platforms whose primary purpose is enabling users to create and share content or participate in social networking, as defined in the legislation itself. This includes platforms such as Instagram, TikTok, Snapchat, and Facebook, but excludes messaging services, email, online gaming platforms, and news websites, unless the legislation explicitly includes them.

**"Minimum age of 15"** means the law must prohibit children under the age of 15 from independently creating or maintaining accounts on covered social media platforms, regardless of parental consent (parental-consent-only regimes do not count).

**Resolution sources:** The primary resolution source is the Journal Officiel, available at https://www.legifrance.gouv.fr/. Secondary confirmation may come from credible international news agencies such as Reuters (https://www.reuters.com/), the Associated Press (https://apnews.com/), or AFP.

**"Country"** is not directly relevant here as the question is France-specific, a UN member state.

If the legislation is not published in the Journal Officiel before July 1, 2026 (23:59 UTC), the question resolves NO.

**Pre-cutoff background**

Governments worldwide are increasingly restricting children's access to social media. Australia became the first country to enact an under-16 social media ban in December 2025. Indonesia followed on March 28, 2026, banning social media for children under 16 [Which European countries are banning children from social media?](https://newseu.cgtn.com/news/2026-04-28/Which-European-countries-are-banning-children-from-social-media--1MGYIkenpKg/p.html). Turkey's parliament passed legislation banning social media for children under 15 in late April 2026 [Which European countries are banning children from social media?](https://newseu.cgtn.com/news/2026-04-28/Which-European-countries-are-banning-children-from-social-media--1MGYIkenpKg/p.html).

France's National Assembly (lower house) passed a bill in January 2026 banning social media for children under 15. However, the French Senate adopted the bill in late March 2026 with reservations and attached several conditions through amendments [Which European countries are banning children from social media?](https://newseu.cgtn.com/news/2026-04-28/Which-European-countries-are-banning-children-from-social-media--1MGYIkenpKg/p.html). This means the two chambers have not yet agreed on an identical text, which is typically required before the legislation can be sent to the President for signature and publication in the Journal Officiel (France's official gazette). The bill may need to go through a joint committee (commission mixte paritaire) or additional readings before final adoption. France has stated the ban is designed to take effect by September 2026 (the start of the school year), creating some urgency but also allowing potential delays. As of May 13, 2026, the bill has not yet been fully enacted into law [EU countries push under-15 social media ban, Brussels presents app](https://www.euronews.com/my-europe/2026/04/22/eu-countries-push-under-15-social-media-ban-brussels-presents-age-verification-app).

Denmark has struck a political deal on a similar ban but has not yet passed formal legislation [EU countries push under-15 social media ban, Brussels presents app](https://www.euronews.com/my-europe/2026/04/22/eu-countries-push-under-15-social-media-ban-brussels-presents-age-verification-app). Spain is weighing proposals, and Greece has announced a ban starting January 2027. The European Commission has signaled plans for an EU-wide approach but no legislation has been proposed yet.

**Exact later resolution packet**

The question resolves NO: France did NOT fully enact its under-15 social media ban (promulgation + publication in the Journal Officiel) between May 12, 2026 and July 1, 2026 (23:59 UTC).

Legislative timeline of the relevant bill — the "proposition de loi visant à protéger les mineurs des risques auxquels les expose l'utilisation des réseaux sociaux" (deputy Laure Miller), which sets a minimum age of 15 for access to social media:
- Deposited 18 November 2025; adopted in first reading by the National Assembly on 26 January 2026; adopted with modifications (a divergent version) by the Senate on 31 March 2026. As of the vie-publique.fr tracking (updated 1 April 2026), the bill was pending a commission mixte paritaire (CMP) to reconcile the two chambers' texts, and had NOT been definitively adopted, promulgated, or published in the Journal Officiel [Protéger les mineurs Risques des réseaux sociaux - Proposition de loi](https://www.vie-publique.fr/loi/301799-proteger-les-mineurs-risques-des-reseaux-sociaux-proposition-de-loi).
- The two chambers still disagreed months later. A Public Sénat article dated 29 June 2026 is titled "Interdiction des réseaux sociaux aux moins de 15 ans : le Sénat adopte sa propre version, quitte à perturber l'agenda de l'exécutif" — i.e., on 29 June 2026 (just two days before the deadline) the Senate again adopted its OWN divergent version, so the chambers had NOT agreed on an identical text and no lecture définitive/promulgation had occurred [Interdiction des réseaux sociaux aux moins de 15 ans - Public Sénat](https://www.publicsenat.fr/actualites/politique/interdiction-des-reseaux-sociaux-aux-moins-de-15-ans-le-senat-adopte-sa-propre-version-quitte-a-perturber-lagenda-de-lexecutif) [Interdiction des réseaux sociaux aux moins de 15 ans - Public Sénat](https://www.publicsenat.fr/actualites/politique/interdiction-des-reseaux-sociaux-aux-moins-de-15-ans-le-senat-adopte-sa-propre-version-quitte-a-perturber-lagenda-de-lexecutif).
- Corroborating this, on 15 June 2026 Libération reported Macron wanting to close under-15 accounts only "d'ici à la fin de l'année" (by the end of the year), consistent with the law not yet being enacted in mid-June 2026.

Because the Senate adopted a divergent text on 29 June 2026, it was legislatively impossible for an identical text to then be adopted by both chambers (or via Article 49.3), promulgated by the President, and published in the Journal Officiel — all within the remaining ~2 days before 1 July 2026. No source shows any such promulgation/JO publication.

Note on a potential false positive: vie-publique.fr references a "loi sur la majorité numérique … promulguée le 7 juillet" — but that is the earlier French "digital majority" law of 7 July 2023, a parental-consent regime that was never applied. Under the resolution criteria, a parental-consent-only regime does not count, and in any case its promulgation date (2023) falls outside the required window. Therefore it cannot support a YES.

Per the resolution criteria, "If the legislation is not published in the Journal Officiel before July 1, 2026 (23:59 UTC), the question resolves NO." The legislation was not published, so the resolution is NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-192. `eebf64ff-d823-5b07-93c8-f13eec1c3009`

- Present date: `2026-05-29 06:25:58.279713`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the German Bundestag pass the Infrastructure Future Act (Infrastruktur-Zukunftsgesetz, InfZuG) into law by July 1, 2026?

**Resolution criteria**

This question resolves YES if the Infrastruktur-Zukunftsgesetz (InfZuG) is published in the German Federal Law Gazette (Bundesgesetzblatt, https://www.recht.bund.de/bgbl/1/) on or before July 1, 2026, 23:59 CEST. Publication in the Bundesgesetzblatt constitutes passage into law, as it follows Bundestag approval, any required Bundesrat consent, and presidential signature.

This question resolves NO if the act has not been published in the Bundesgesetzblatt by that date.

The primary resolution source is the Federal Law Gazette (Bundesgesetzblatt) at https://www.recht.bund.de/bgbl/1/. The legislative tracking system DIP (https://dip.bundestag.de/) may also be consulted to verify the status of the bill.

**Pre-cutoff background**

The original question concerned the Bundeswehr Planning and Procurement Acceleration Act (BwPBBG). However, the BwPBBG was already passed by the Bundestag on January 15, 2026, published in the Federal Law Gazette (BGBl. 2026 I Nr. 40) on February 12–13, 2026, and entered into force on February 14, 2026. The question is therefore already resolved and cannot serve as a forecasting question.

As a closely related alternative involving German legislative acceleration efforts, this question focuses on the Infrastructure Future Act (Infrastruktur-Zukunftsgesetz, InfZuG). The German Federal Cabinet approved the draft InfZuG on December 17, 2025. The act aims to accelerate planning and approval procedures for transport and energy infrastructure projects across Germany — a key companion to the defense spending surge enabled by the constitutional debt brake reform of March 2025.

As of early 2026, the InfZuG had its first reading in the Bundestag (week 9 of 2026, late February/early March), receiving both praise and criticism in plenary debate. The act is scheduled to come into force in mid-2026 but must still complete the full parliamentary process, including committee deliberations, second and third readings in the Bundestag, and Bundesrat approval (as it affects state-level planning procedures). The timeline is ambitious and subject to political negotiation, making its passage by July 1, 2026 uncertain.

**Exact later resolution packet**

The question resolves NO because the Infrastruktur-Zukunftsgesetz (InfZuG) was NOT published in the German Federal Law Gazette (Bundesgesetzblatt) on or before July 1, 2026, 23:59 CEST.

Key evidence and reasoning:

1. Bundestag passage (necessary but NOT sufficient for YES): The Deutscher Bundestag passed ("gebilligt") the government's draft InfZuG on Friday, June 26, 2026, with the votes of CDU/CSU and SPD. The official Bundestag textarchiv page states: "Mit den Stimmen von CDU/CSU und SPD hat der Bundestag am Freitag, 26. Juni 2026, den Entwurf der Bundesregierung für ein 'Infrastruktur-Zukunftsgesetz' [...] gebilligt." [Parlament billigt „Infrastruktur-Zukunftsgesetz“ - Deutscher Bundestag](https://www.bundestag.de/dokumente/textarchiv/2026/kw26-de-infrastruktur-zukunftsgesetz-1184312) (https://www.bundestag.de/dokumente/textarchiv/2026/kw26-de-infrastruktur-zukunftsgesetz-1184312)

2. The act still required Bundesrat consent (it is a Zustimmungsgesetz affecting state-level planning procedures, and the government had to respond to a 138-point Bundesrat Stellungnahme). Per the resolution criteria, publication in the Bundesgesetzblatt only follows AFTER Bundestag approval, required Bundesrat consent, and presidential signature.

3. As of the deadline, the Bundesrat had NOT yet given consent. The official Bundesrat legislative record for the InfZuG (Drucksache 390/26) shows that after the June 26, 2026 Bundestag vote, the matter was merely assigned to committees (Vk – AV – U) and had not received a final consent vote; there is no record of Bundesrat consent nor of any Bundesgesetzblatt publication [Suche - Infrastruktur-Zukunftsgesetz - Bundesrat](https://www.bundesrat.de/SharedDocs/beratungsvorgaenge/2026/0301-0400/0390-26.html) (https://www.bundesrat.de/SharedDocs/beratungsvorgaenge/2026/0301-0400/0390-26.html).

4. The Bundesregierung's own page on the InfZuG explicitly states that "der Bundesrat soll am 10. Juli darüber beraten" (the Bundesrat is to deliberate on it on July 10) — i.e., AFTER the July 1, 2026 deadline (source: https://www.bundesregierung.de/breg-de/aktuelles/infrastruktur-zukunftsgesetz-2399998, seen in Google search snippets; page itself timed out on direct query).

Because the mandatory Bundesrat consent was not scheduled until July 10, 2026, it was legally impossible for the act to have received presidential signature and to have been published in the Bundesgesetzblatt (https://www.recht.bund.de/bgbl/1/) by July 1, 2026, 23:59 CEST. No BGBl entry for the InfZuG exists by the deadline [Suche - Infrastruktur-Zukunftsgesetz - Bundesrat](https://www.bundesrat.de/SharedDocs/beratungsvorgaenge/2026/0301-0400/0390-26.html). Hence the question resolves NO.

Note on the checklist: This resolution is based specifically on the InfZuG (not the BwPBBG mentioned only in the question's description text). The BwPBBG was a separate, already-enacted law and was not used here.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):
