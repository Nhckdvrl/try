# btf3_large_replication_v1 — realized YES review chunk YES-065–YES-128

> Display chunk of the immutable queue (`btf3_large_replication_v1_yes_queue.json`). Review strictly top-to-bottom; stop only when this bucket reaches 128 ACCEPTs overall. Do not skip ahead, reorder, or prefer better-looking questions. A REJECT/UNSURE permanently consumes its queue slot and is never resampled, re-reviewed, or hand-repaired.

All four gates must hold to ACCEPT. On REJECT or UNSURE write exactly one line of reason.

### YES-65. `b41eb641-c931-50da-97bb-4711c8dd6c65`

- Present date: `2026-05-14 00:11:23.511108`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-15T00:00:00`

**Question**

Will Susan Collins vote in favor of the Senate immigration enforcement reconciliation bill (pursuant to S.Con.Res.33) on final passage?

**Resolution criteria**

This question resolves Yes if Senator Susan Collins (R-ME) casts a "Yea" or "Aye" vote on final passage (i.e., "passage of the bill") of the reconciliation bill produced pursuant to S.Con.Res.33 (119th Congress, 2nd Session), which provides funding for ICE, CBP, and immigration enforcement, in a Senate roll call vote occurring on or after May 12, 2026 (00:00 UTC) and no later than July 1, 2026 (23:59 UTC).

This question resolves No if:
- Collins votes "Nay" or "No" on final passage of the bill, or
- Collins votes "Present" or does not vote, or
- No final passage vote on the reconciliation bill occurs by July 1, 2026 (23:59 UTC).

Only a "Yea" or "Aye" vote on final passage (or "passage of the bill") counts as voting in favor. Votes on procedural motions (e.g., motions to proceed, cloture votes, amendments) do not count.

Resolution is determined by the official United States Senate roll call vote records published at https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_119_2.htm

**Pre-cutoff background**

In April 2026, Senate Republicans passed S.Con.Res.33, a budget resolution instructing the Senate Homeland Security and Governmental Affairs (HSGAC) Committee and the Senate Judiciary Committee to produce reconciliation legislation funding Immigration and Customs Enforcement (ICE) and Customs and Border Protection (CBP). The budget resolution passed 50-48 on April 23, 2026, with Republican Senators Lisa Murkowski (R-AK) and Rand Paul (R-KY) joining all Democrats in opposition [Senate Committees Introduce Reconciliation Bills Funding ICE and ...](https://www.fairus.org/legislation/congress/senate-committees-introduce-reconciliation-bills-funding-ice-and-border-patrol). Senator Susan Collins (R-ME) voted in favor of the budget resolution [Senate Committees Introduce Reconciliation Bills Funding ICE and ...](https://www.fairus.org/legislation/congress/senate-committees-introduce-reconciliation-bills-funding-ice-and-border-patrol).

On May 5-6, 2026, the two Senate committees introduced their respective titles of the reconciliation package, totaling approximately $72 billion in immigration enforcement funding through 2029 [Senate Committees Introduce Reconciliation Bills Funding ICE and ...](https://www.fairus.org/legislation/congress/senate-committees-introduce-reconciliation-bills-funding-ice-and-border-patrol). As of May 13, 2026, the Senate is expected to hold a floor vote on the combined reconciliation package imminently — possibly within days [Senate Committees Introduce Reconciliation Bills Funding ICE and ...](https://www.fairus.org/legislation/congress/senate-committees-introduce-reconciliation-bills-funding-ice-and-border-patrol). The reconciliation bill funds ICE, CBP, and related enforcement operations for the remainder of President Trump's term.

Senator Collins is widely regarded as a pivotal swing vote. While she supported the preliminary budget resolution (S.Con.Res.33), her vote on final passage remains uncertain given her history of breaking with her party on contentious legislation. The reconciliation package has drawn controversy over specific spending items (including White House security provisions) and broader concerns about the scale of immigration enforcement funding. Collins' decision could determine whether the bill achieves the simple majority needed for passage.

Resolution source: Official U.S. Senate roll call vote records at https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_119_2.htm

**Exact later resolution packet**

The question resolves YES.

The reconciliation bill produced pursuant to S.Con.Res.33 (119th Congress, 2nd Session) is S. 2, "An original bill to provide for reconciliation pursuant to title II of S. Con. Res. 33," funding ICE, CBP, and immigration enforcement.

The final passage vote occurred on **June 5, 2026** (Roll Call Vote No. 163), which is within the required window (on/after May 12, 2026 and no later than July 1, 2026). Per the official U.S. Senate roll call vote record, the question voted on was **"On Passage of the Bill (S. 2, As Amended)"** — i.e., final passage, not a procedural motion (cloture/motion to proceed/amendment). The tally was **52 Yeas to 47 Nays; the bill Passed** [Roll Call Vote 119 th Congress - 2 nd Session - Senate.gov](https://www.senate.gov/legislative/LIS/roll_call_votes/vote1192/vote_119_2_00163.htm).

On that vote, **Senator Susan Collins (R-ME) is listed among the YEAs** — she cast a "Yea" vote on final passage [Roll Call Vote 119 th Congress - 2 nd Session - Senate.gov](https://www.senate.gov/legislative/LIS/roll_call_votes/vote1192/vote_119_2_00163.htm). This is corroborated by:
- WMTW News 8, headlined "Susan Collins joins Senate Republicans in approving $70 billion for immigration enforcement," reporting the 52-47 passage on June 5, 2026 [Senate approves $70 billion for immigration enforcement - WMTW](https://www.wmtw.com/article/susan-collins-joins-senate-republicans-in-approving-70-billion-for-immigration-enforcement/71503891).
- An ABC7 News report noting that "Sen. Lisa Murkowski was the only Republican to join all Democrats in voting against the bill. All other Senate Republicans voted for it" — confirming Collins (a Republican) voted in favor (found via Google search snippet).

Because Collins cast a "Yea" vote on final passage of the bill within the specified window, the resolution criteria are satisfied and the question resolves **YES (1)**.

Official roll call vote URL: https://www.senate.gov/legislative/LIS/roll_call_votes/vote1192/vote_119_2_00163.htm (linked from the resolution source https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_119_2.htm).

Note on a conflicting reading: An initial query of the roll-call *menu* page returned an erroneous claim that Collins voted "Nay" [Roll Call Votes 119th Congress - 2nd Session (2026) - U.S. Senate](https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_119_2.htm). That menu page does not list individual senators' votes, and the response anomalously mimicked the answer schema, indicating a tool error. The direct roll call vote page [Roll Call Vote 119 th Congress - 2 nd Session - Senate.gov](https://www.senate.gov/legislative/LIS/roll_call_votes/vote1192/vote_119_2_00163.htm) and independent news sources uniformly confirm Collins voted Yea, so the "Nay" claim is rejected.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-66. `54b20761-0b2d-50b0-b7d6-7242e6c9cbda`

- Present date: `2026-05-14 10:00:32.986920`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

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

**Pre-cutoff background**

The Long Island Rail Road (LIRR) and a coalition of five unions representing approximately 3,500 workers have been in contract negotiations since their previous contract expired in 2022. The five unions are: the Brotherhood of Locomotive Engineers and Trainmen (BLET), the Brotherhood of Railroad Signalmen (BRS), the International Association of Machinists and Aerospace Workers (IAM), the International Brotherhood of Electrical Workers (IBEW), and the Transportation Communications Union (TCU) [Long Island Rail Road, five unions released from required mediation](https://www.trains.com/pro/passenger/commuter-regional/long-island-rail-road-five-unions-released-from-required-mediation/).

Two Presidential Emergency Boards (PEBs) have already been convened during this dispute. As of May 8, 2026, both sides have agreed on retroactive raises for the first three years of a four-year contract: 3% for 2023, 3% for 2024, and 3.5% for 2025 [Looming deadline threatens new LIRR strike - Amsterdam News](https://amsterdamnews.com/news/2026/05/07/looming-deadline-threatens-new-lirr-strike/). The key remaining disagreement is over the 2026 wage increase: the unions are demanding 5%, while the MTA has offered 3% without conditions or 4.5% contingent on work-rule changes [LIRR strike threat: Unions, MTA offer different takes on ... - amNewYork](https://www.amny.com/news/lirr-strike-threat-unions-mta-talks-05082026/). Additional sticking points include work-rule changes such as extra pay for engineers operating different types of trains [Looming deadline threatens new LIRR strike - Amsterdam News](https://amsterdamnews.com/news/2026/05/07/looming-deadline-threatens-new-lirr-strike/).

Union representatives have characterized the MTA's offers as "phony surface bargaining," while the MTA argues the unions' demands are unaffordable without fare hikes or service cuts [LIRR strike threat: Unions, MTA offer different takes on ... - amNewYork](https://www.amny.com/news/lirr-strike-threat-unions-mta-talks-05082026/). The unions have set a strike deadline of May 16, 2026, which would be the first LIRR strike affecting approximately 300,000 daily commuters. Political pressure and public impact could accelerate or complicate resolution.

**Exact later resolution packet**

The question resolves YES. On the night of Monday, May 18, 2026 — within the required window of May 12, 2026 to July 1, 2026 — the MTA and the coalition of all five LIRR unions (BLET, BRS, IAM, IBEW, TCU) reached a tentative agreement on a new contract, ending a three-day strike.

Key evidence:
- CBS New York reported: "The Long Island Rail Road strike is over after the Metropolitan Transportation Authority and unions reached a tentative agreement Monday to end the three-day work stoppage," and Gov. Hochul stated "the MTA reached a fair deal with the five LIRR unions." Crucially, it noted "The deal must still be ratified by the five labor unions," satisfying the definition of a tentative agreement (announced but subject to ratification) [684b11].
- The LI Herald confirmed "The three-day Long Island Rail Road strike ended late Monday after five unions and the Metropolitan Transportation Authority reached a tentative agreement," subject to "a 30-day period in which union members will review and vote on the tentative deal before it becomes official" [6eeb01].
- amNewYork reported an MTA official "defended on Tuesday the agency's tentative deal with five Long Island Rail Road unions that ended their first strike in more than three decades," adding "The deal still must be ratified by members of the five unions" [ff0524].
- The International Brotherhood of Teamsters (parent of BLET) issued a May 19, 2026 press release confirming "Teamsters with the Brotherhood of Locomotive Engineers and Trainmen (BLET) and their union coalition have reached a tentative agreement" with LIRR, subject to ratification, referring to the coalition of five unions [790426].

All five named unions negotiated as a single coalition and reached the tentative agreement together, so the requirement that all five reach tentative agreements is met. The date (May 18, 2026) falls within the resolution window, and the agreement is a formally announced tentative deal subject to membership ratification (not a fully ratified contract, and not merely a handshake). Therefore the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-67. `4a1e4fb7-aaeb-52f1-873d-ab20125c9951`

- Present date: `2026-05-02 12:33:45.918391`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-05-21 00:00:00`

**Question**

Will a U.S. federal court order blocking the termination of Yemen's TPS designation remain in effect on May 20, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on May 20, 2026 at 11:59 PM UTC, any order issued by a U.S. federal court — including U.S. District Courts, U.S. Courts of Appeals, or the U.S. Supreme Court — is in effect that blocks, enjoins, stays, or postpones the termination of Yemen's TPS designation (originally scheduled for May 4, 2026). The order must have been issued or affirmed on or after May 1, 2026.

This question resolves as **No** if no such order is in effect at that time — for example, if the May 1, 2026 order by Judge Ho is vacated, stayed, or reversed by an appellate court, or if the order expires by its own terms before May 20, 2026.

For the purposes of this question:
- An "[injunction](https://www.law.cornell.edu/wex/injunction)" or court order includes a preliminary injunction, temporary restraining order, or a stay/postponement of agency action under 5 U.S.C. § 705 — any judicial order that has the practical effect of preventing the TPS termination from taking effect.
- "U.S. federal court" includes any [Article III court](https://en.wikipedia.org/wiki/Article_Three_of_the_United_States_Constitution#Section_1:_Federal_courts) of the United States: U.S. District Courts, U.S. Courts of Appeals, and the Supreme Court of the United States.
- Both nationwide and localized orders qualify. A preliminary or temporary order is sufficient; a final judgment on the merits is not required.

**Resolution source:** The docket of *Doe v. Noem* (1:26-cv-02103) on [CourtListener/RECAP](https://www.courtlistener.com/docket/72493533/doe-v-noem/) or the official [PACER](https://pacer.uscourts.gov/) system, supplemented by reporting from credible legal news sources such as [SCOTUSblog](https://www.scotusblog.com/) or [Reuters](https://www.reuters.com/).

**Pre-cutoff background**

On March 3, 2026, the Department of Homeland Security published a Federal Register notice terminating the Temporary Protected Status (TPS) designation for Yemen, effective at 11:59 p.m. local time on May 4, 2026 (FR 2026-04179). As of May 1, 2026, approximately 1,700 Yemeni nationals hold TPS in the United States.

On March 14, 2026, nine Yemeni nationals filed a putative class action lawsuit, *Doe v. Noem* (1:26-cv-02103), in the U.S. District Court for the Southern District of New York, challenging the termination as arbitrary and capricious under the Administrative Procedure Act (APA) and as violating the Fifth Amendment [Case: Doe v. Noem - Civil Rights Litigation Clearinghouse](https://clearinghouse.net/case/47911/).

On May 1, 2026, Judge Dale E. Ho of the Southern District of New York granted the plaintiffs' motion to postpone the effective date of the Yemen TPS termination under 5 U.S.C. § 705, finding that the Secretary of Homeland Security failed to comply with the statutory procedural requirement to consult with appropriate agencies regarding country conditions before terminating the TPS designation [[PDF] united states district court - Southern District of New York](https://www.nysd.uscourts.gov/sites/default/files/2026-05/26cv2103%2C%2026cv2280%20Doe%20v.%20Noem%20-%20Granting%20Motion%20to%20Postpone.pdf). The court applied the same standard as for a preliminary injunction.

The U.S. government may seek an emergency stay of this order from the U.S. Court of Appeals for the Second Circuit or the Supreme Court, as it has done in other TPS-related cases. The Supreme Court heard oral arguments in a related TPS case the week of April 27, 2026, adding further uncertainty. Whether the order survives potential appellate review remains an open question.

**Exact later resolution packet**

YES. The qualifying court order was Judge Dale E. Ho’s May 1, 2026 Opinion and Order in Doe v. Noem / related Doe case, S.D.N.Y. Nos. 26 Civ. 2103 and 26 Civ. 2280, available at https://www.nysd.uscourts.gov/sites/default/files/2026-05/26cv2103%2C%2026cv2280%20Doe%20v.%20Noem%20-%20Granting%20Motion%20to%20Postpone.pdf. The order expressly granted plaintiffs’ motions “to postpone the effective date of the termination of Yemen’s TPS designation,” which is a court order blocking/postponing the May 4, 2026 Yemen TPS termination and was issued on the required date, May 1, 2026 [[PDF] 26cv2103, 26cv2280 Doe v. Noem - Southern District of New York](https://www.nysd.uscourts.gov/sites/default/files/2026-05/26cv2103%2C%2026cv2280%20Doe%20v.%20Noem%20-%20Granting%20Motion%20to%20Postpone.pdf). The order source did not identify any built-in expiration date or self-terminating provision before May 20, 2026 [[PDF] 26cv2103, 26cv2280 Doe v. Noem - Southern District of New York](https://www.nysd.uscourts.gov/sites/default/files/2026-05/26cv2103%2C%2026cv2280%20Doe%20v.%20Noem%20-%20Granting%20Motion%20to%20Postpone.pdf). The official CourtListener/RECAP docket for Doe v. Noem, 1:26-cv-02103, at https://www.courtlistener.com/docket/72493533/doe-v-noem/, shows the May 1, 2026 Opinion and Order as entry 39 and then only entry 40 on May 7, entry 41 on May 13, and entry 42 on May 21; the docket summary found no entry from May 1 through May 20, 2026 reflecting a stay, vacatur, reversal, or appellate order undoing entry 39 [Doe v. Noem, 1:26-cv-02103 – CourtListener.com](https://www.courtlistener.com/docket/72493533/doe-v-noem/). This also covers the required check for docket updates in the relevant period. As a cross-check, AILA’s TPS/parole status chart, updated May 28, 2026, states that on May 1, 2026 a judge of the U.S. District Court for the Southern District of New York issued an order staying the Yemen TPS termination in Doe v. Noem et al., Nos. 26-cv-2103 and 26-cv-2280, and notes USCIS guidance acknowledging the court order [Practice Alert: TPS and Parole Status Updates Chart](https://www.aila.org/library/practice-alert-tps-and-parole-status-updates-chart). Because no emergency stay, vacatur, or reversal by the Second Circuit or Supreme Court appears in the case docket before the target timestamp, and because the May 1 order had not expired by its own terms, an order postponing/blocking the Yemen TPS termination remained in effect at May 20, 2026, 11:59 PM UTC [Doe v. Noem, 1:26-cv-02103 – CourtListener.com](https://www.courtlistener.com/docket/72493533/doe-v-noem/) [[PDF] 26cv2103, 26cv2280 Doe v. Noem - Southern District of New York](https://www.nysd.uscourts.gov/sites/default/files/2026-05/26cv2103%2C%2026cv2280%20Doe%20v.%20Noem%20-%20Granting%20Motion%20to%20Postpone.pdf) [Practice Alert: TPS and Parole Status Updates Chart](https://www.aila.org/library/practice-alert-tps-and-parole-status-updates-chart).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-68. `2ac281ec-eec7-582a-998d-fc353801e484`

- Present date: `2026-05-14 06:41:34.017098`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Knesset vote on a bill to dissolve itself between May 12, 2026 and July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if the Knesset Plenum holds a formal vote on a "Dissolution of the Knesset" bill (חוק לפיזור הכנסת) on or after May 12, 2026, and by 11:59 PM IDT (UTC+3) on July 1, 2026. A qualifying "vote" includes any of the following: a preliminary reading (pre-vote), first reading, second reading, or third reading in the Knesset Plenum. The bill must specifically propose to dissolve the Knesset and call for early elections; standard no-confidence motions that do not propose dissolution do not count.

This question resolves as **No** if no such vote takes place by the deadline.

**Resolution source:** The official Knesset legislation database at https://main.knesset.gov.il/en/legislation/pages/default.aspx and/or the Knesset Plenum protocols at https://m.knesset.gov.il/en/activity/pages/plenum.aspx. If these sources are unavailable or ambiguous, credible reporting from Reuters (https://www.reuters.com), the Times of Israel (https://www.timesofisrael.com), or Haaretz (https://www.haaretz.com) may be used as secondary sources.

**Pre-cutoff background**

As of May 12, 2026, the Israeli Knesset is facing a renewed political crisis over the Haredi (ultra-Orthodox) military draft exemption law. Following the High Court's June 2025 ruling that declared previous exemptions illegal, the coalition has struggled to pass replacement legislation. Haredi spiritual leaders, including Rabbi Dov Lando of the Degel HaTorah faction, have called for dissolving the Knesset, and a dissolution vote in the plenum is expected in the coming days [https://www.timesofisrael.com/knesset-summer-session-to-focus-on-haredi-draft-efforts-to-curb-public-media/](https://www.timesofisrael.com/knesset-summer-session-to-focus-on-haredi-draft-efforts-to-curb-public-media/).

This mirrors the crisis of June 2025, when opposition parties brought a preliminary vote to dissolve the Knesset. That vote failed after an 11th-hour compromise, with Haredi coalition partners ultimately backing down (Reuters, NYT). Netanyahu survived but was politically weakened.

Under Israeli law, the Knesset can dissolve itself by passing a "Dissolution of the Knesset" bill (Hebrew: חוק לפיזור הכנסת), as provided under Section 34 of Basic Law: The Knesset. Such a bill follows the standard legislative process: a preliminary reading, committee discussion, and three readings in the plenum. However, even a preliminary reading vote is politically significant, as it signals the level of support for early elections [Everything You Need to Know About Dissolving the Knesset](https://en.idi.org.il/articles/59621).

The Knesset's 2026 summer session opened on May 12, with the Haredi draft issue as a central focus [https://www.timesofisrael.com/knesset-summer-session-to-focus-on-haredi-draft-efforts-to-curb-public-media/](https://www.timesofisrael.com/knesset-summer-session-to-focus-on-haredi-draft-efforts-to-curb-public-media/). Scheduled elections must be held by October 27, 2026, at the latest, per Wikipedia. The political dynamics—Haredi threats, opposition pressure, and coalition fragility—create genuine uncertainty about whether a dissolution vote will occur again before July 1, 2026.

**Exact later resolution packet**

The question resolves YES. The Knesset Plenum held formal votes on a bill to dissolve itself within the resolution window (May 12, 2026 – 11:59 PM IDT July 1, 2026).

Key evidence:

1. PRELIMINARY READING — May 20, 2026: The Knesset Plenum passed the dissolution bill in its preliminary reading with a 110-0 vote. This is confirmed by the Times of Israel article "Lawmakers to vote Monday on first reading of Knesset dissolution bill" (dated May 27, 2026), which references the bill having passed its preliminary reading 110-0 "last week" (i.e., May 20, 2026) [b0c90e]. The resolution criteria explicitly list a "preliminary reading (pre-vote)" as a qualifying vote type.

2. FIRST READING — June 2, 2026: The official Knesset legislation/press-release source (https://main.knesset.gov.il/News/PressReleases/pages/press02062026.aspx) confirms that the Knesset Plenum approved in FIRST READING the bill "הצעת חוק התפזרות הכנסת העשרים וחמש, התשפ״ו-2026" (Bill for the Dissolution/Dispersal of the Twenty-Fifth Knesset, 2026), submitted by MK Ofir Katz and a group of MKs, by a vote of 106 in favor, 0 against, 0 abstentions, after which it was returned to committee [e4b7cc]. The Times of Israel corroborates this first-reading vote of 106-0 (voted overnight June 1 into June 2, 2026), noting the bill specifically proposes to dissolve parliament and trigger early elections, potentially moving elections up to September [c2d62d].

The bill's Hebrew name (חוק התפזרות הכנסת / חוק לפיזור הכנסת — the "Dissolution of the Knesset" bill under Section 34 of Basic Law: The Knesset) and its explicit legislative intent to dissolve the Knesset and call early elections match the question's requirement exactly. This is a genuine dissolution bill, not a standard no-confidence motion.

Both qualifying votes (preliminary reading May 20 and first reading June 2, 2026) fall squarely within the window of May 12 – July 1, 2026. Either one alone satisfies the YES criteria.

Sources: Official Knesset press release https://main.knesset.gov.il/News/PressReleases/pages/press02062026.aspx [e4b7cc]; Times of Israel https://www.timesofisrael.com/mks-advance-bill-to-dissolve-knesset-and-potentially-move-up-elections-to-september/ [c2d62d]; Times of Israel https://www.timesofisrael.com/lawmakers-to-vote-on-first-reading-of-knesset-dissolution-bill-on-monday/ [b0c90e].

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-69. `88b874ff-e31d-5bf7-a836-ccb1cd5f9338`

- Present date: `2026-05-14 00:00:14.436025`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-15T00:00:00`

**Question**

Will the Knesset Constitution, Law and Justice Committee approve the "Splitting the Post of the Attorney General" bill for first reading by June 15, 2026?

**Resolution criteria**

This question resolves **Yes** if the Knesset Constitution, Law and Justice Committee takes a formal vote to approve the "Splitting the Post of the Attorney General Bill" (any version — 2023, 2024, or 2025, or a merged version thereof) to advance to first reading in the Knesset plenum. This approval must occur on or after May 12, 2026, and no later than June 15, 2026, 23:59 Israel Daylight Time (IDT, UTC+3).

"Approval for first reading" means a formal committee vote recommending the bill to the Knesset plenum for its first reading (הצבעה בוועדה להכנת הצעת החוק לקריאה ראשונה), as recorded in the official committee proceedings.

The question resolves **No** if no such committee vote occurs by the deadline, or if the vote is held but the bill is rejected.

**Primary resolution source:** Official Knesset committee records at [https://main.knesset.gov.il/en/APPS/committees/2215/sessions/](https://main.knesset.gov.il/en/APPS/committees/2215/sessions/) and the Knesset legislation database at [https://main.knesset.gov.il/EN/activity/Pages/Legislation.aspx](https://main.knesset.gov.il/EN/activity/Pages/Legislation.aspx). Credible news reporting from outlets such as the Times of Israel, Haaretz, or Jerusalem Post may serve as supplementary sources.

**Pre-cutoff background**

The "Splitting the Post of the Attorney General Bill" (Hebrew: הצעת חוק פיצול תפקיד היועץ המשפטי לממשלה) is Israeli legislation that would divide the current Attorney General's role into three separate positions: legal adviser to the government, head of the state prosecution (Prosecutor General), and government representative to the courts. The bill was sponsored by MK Mishel Buskila and passed its preliminary reading in the Knesset plenum on October 29, 2025, with 61 votes in favor and 46 against [Bill for splitting the post of the Attorney General](https://m.knesset.gov.il/EN/News/PressReleases/Pages/press291025u.aspx).

Following the preliminary reading, the bill was referred to the Constitution, Law and Justice Committee, chaired by MK Simcha Rothman, for deliberation before it can be approved for a first reading in the plenum. As of May 13, 2026, the committee has placed the bill (including its 2023, 2024, and 2025 versions) on its agenda, with a session held on May 12, 2026 [Committee meetings](https://main.knesset.gov.il/en/APPS/committees/2215/sessions/2242779). However, the committee has not yet voted to approve the bill for first reading.

The coalition has signaled intent to advance this bill rapidly as part of a broader legislative blitz following the Knesset's spring recess [Contentious proposals dominate planned legislative blitz ...](https://www.timesofisrael.com/contentious-proposals-punctuate-planned-legislative-blitz-as-knesset-gets-back-to-work/). However, the committee faces competing legislative priorities including haredi draft legislation, budget-related bills, and other judicial reform proposals. Opposition MKs and legal experts may slow proceedings through hearings and deliberations. The bill is part of a broader judicial overhaul effort that has generated significant public controversy in Israel since 2023.

**Exact later resolution packet**

The question resolves YES. The Knesset Constitution, Law and Justice Committee (chaired by MK Simcha Rothman) held a formal vote to approve the "Splitting the Post of the Attorney General" bill for its first reading on Tuesday, May 19, 2026 — squarely within the resolution window (on or after May 12, 2026 and no later than June 15, 2026, 23:59 IDT).

Evidence:
- The official Knesset committee news item dated May 19, 2026 states the Constitution, Law and Justice Committee held a formal vote and approved the bill for first reading, passing by a majority of nine MKs with no opposing votes (the opposition had left the meeting before the vote) [Constitution Committee approves for first reading bill for splitting the ...](https://m.knesset.gov.il/EN/apps/committees/2215/news/27259). (URL: https://m.knesset.gov.il/EN/apps/committees/2215/news/27259)
- JNS ("Bill to split attorney general role clears key Knesset committee hurdle") confirms the committee approved the bill 9-0 on Tuesday, May 19, 2026, with the opposition boycotting the vote on procedural grounds [Bill to split attorney general role clears key Knesset committee hurdle](https://www.jns.org/analysis/bill-to-split-attorney-general-role-clears-key-knesset-committee-hurdle).
- A subsequent official Knesset press release dated May 25, 2026 records that the committee voted "anew" to approve the bill for first reading, after opposition members raised a procedural objection about budgetary costing; the committee re-held the debate and again approved it [Constitution Committee votes anew to approve for first reading bill ...](https://main.knesset.gov.il/EN/News/PressReleases/Pages/press25526w.aspx). (URL: https://main.knesset.gov.il/EN/News/PressReleases/Pages/press25526w.aspx) Both the May 19 and May 25 votes fall within the required window.

Both the initial approval (May 19, 2026) and the re-affirmed approval (May 25, 2026) satisfy the resolution criterion of a formal committee vote to advance the bill to first reading occurring between May 12 and June 15, 2026. The bill subsequently passed its first reading in the Knesset plenum (reported 65-47), further confirming the committee advanced it. Therefore the criteria for YES are met.

Note: An initial automated read of the committee sessions index page returned NO, but that read only inspected upcoming July 2026 sessions and missed the May 19 and May 25 approval votes; it is superseded by the specific official committee news/press-release pages and multiple credible news reports above.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-70. `fe39b56b-8133-5518-918a-09f312b235df`

- Present date: `2026-05-03 05:34:54.852556`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

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

**Pre-cutoff background**

Cerebras Systems is an AI chipmaker that designs wafer-scale processors for AI training and inference. The company originally filed for an IPO in September 2024 but withdrew its plans in October 2025 due to a federal review of an investment from Abu Dhabi-based Group 42. On April 17, 2026, Cerebras revived its IPO with a new S-1 filing on the SEC, planning to list on the Nasdaq Global Select Market under the ticker symbol "CBRS" [Cerebras Systems Inc. (2026) - IPOScoop](https://www.iposcoop.com/ipo/cerebras/).

Key financial and funding details as of May 1, 2026:
- 2025 revenue: $510 million, up 76% year-over-year from $290 million in 2024.
- 2025 net income: $87.9 million, compared to a net loss of ~$485 million in 2024.
- Series G (September 2025): $1.1 billion at $8.1 billion valuation.
- Series H (January 2026): $1 billion at ~$23 billion valuation.
- Underwriters: Morgan Stanley, Citigroup, Barclays, and UBS.
- The company has a $24.6 billion order backlog, though with significant customer concentration risk (notably contracts with Middle Eastern entities).
- As of April 30, 2026, pre-IPO secondary market shares were trading at approximately $184.80 per share on Hiive.
- IPO terms (price range, share count) have not yet been disclosed as of May 1, 2026 [Cerebras Systems Inc. (2026) - IPOScoop](https://www.iposcoop.com/ipo/cerebras/).

Historically, approximately 60–70% of US IPOs close above their offer price on the first day of trading, though this rate varies significantly with market conditions and sector sentiment. Cerebras benefits from strong AI tailwinds but faces risks including customer concentration and a prior IPO withdrawal.

**Exact later resolution packet**

The question resolves YES. Both conditions were met:

1. IPO occurred before deadline: Cerebras Systems completed its IPO and its Class A common stock began trading on the Nasdaq under ticker CBRS on Thursday, May 14, 2026, which is on or before the June 1, 2026 23:59 UTC deadline [f3018b].

2. Closing price strictly above offer price: The IPO offer price was $185.00 per share (priced May 13, 2026, above its expected range), and the closing price on the first day of trading (May 14, 2026) was $311.07 per share — a 68% first-day gain. Since $311.07 > $185.00, the condition is satisfied [f3018b].

Supporting excerpts from CNBC: "Cerebras shares opened at $350, up from its $185 IPO price, and closed up 68% at $311.07" and "Cerebras Systems soared 68% in its Nasdaq debut on Thursday, closing at $311.07 after selling shares at $185, well above the company's expected range" [f3018b].

This is corroborated by multiple other credible sources including Reuters, WSJ, Fortune, IPOScoop (which reported the $185 IPO price and 68.15% first-day gain), and Hiive (which listed "Cerebras Systems IPO Price: $185.00/sh. Day 1 closing price: $311.07/sh").

Source URL: https://www.cnbc.com/2026/05/14/cerebras-cbrs-stock-trade-nasdaq-ipo.html

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-71. `4d01045b-3518-52b2-be59-875b24046d9d`

- Present date: `2026-05-01 14:39:35.997384`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Japan and the Philippines hold a bilateral defense ministerial meeting between April 30, 2026, and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after April 30, 2026 (00:00 UTC) and no later than June 1, 2026 (23:59 UTC), the Japanese Minister of Defense and the Philippine Secretary of National Defense hold a bilateral meeting (whether in person or via video conference).

**Definitions:**
- A **"bilateral defense ministerial meeting"** means a direct meeting—whether a standalone bilateral session, a "2+2" format (involving both foreign and defense ministers, as described by the [Japanese MOFA](https://www.mofa.go.jp/region/asia-paci/philippine/index.html)), or a meeting on the sidelines of a multilateral event—where the principal participants include the Japanese Minister of Defense (or acting equivalent) and the Philippine Secretary of National Defense (or acting equivalent).
- Both **in-person and virtual/video-conference** meetings count toward a "Yes" resolution, provided they are officially confirmed.
- Meetings involving only lower-level officials (Vice-Ministers, Undersecretaries, military chiefs of staff) do **not** count.

**Resolution source:** An official press release or announcement from any of the following:
- Japan Ministry of Defense: https://www.mod.go.jp/en/
- Japan Ministry of Foreign Affairs: https://www.mofa.go.jp/
- Philippine Department of National Defense: https://www.dnd.gov.ph/
- Philippine Department of Foreign Affairs: https://www.dfa.gov.ph/

If no such official confirmation exists by June 1, 2026 (23:59 UTC), the question resolves **No**.

**Pre-cutoff background**

Japan-Philippines defense cooperation has deepened rapidly in recent years. Key milestones include:

- The **Reciprocal Access Agreement (RAA)**, which entered into force in September 2025, establishing a framework for reciprocal visits by defense forces ([Wikipedia overview](https://en.wikipedia.org/wiki/Reciprocal_access_agreement)).
- The **Acquisition and Cross-Servicing Agreement (ACSA)**, signed on January 15, 2026, enabling the exchange of supplies and services between the Japanese Self-Defense Forces and the Armed Forces of the Philippines ([Reuters report](https://www.reuters.com/world/china/japan-philippines-sign-new-security-pacts-regional-tensions-rise-2026-01-15/)).

The most recent bilateral defense ministerial meeting occurred on **September 9, 2025**, when Japanese Defense Minister Nakatani met Philippine Secretary of National Defense Gilberto Teodoro on the sidelines of the 14th Seoul Defense Dialogue. They discussed operational collaboration under the RAA, defense equipment cooperation, and the "OCEAN" framework [Japan-Philippines Defense Ministerial Meeting](https://www.mod.go.jp/en/article/2025/09/703e90c6df125ae6334739da356eada3060bbef4.html). Prior to that, a defense ministerial meeting took place on February 24, 2025, in the Philippines. A Japan-Philippines "2+2" meeting (involving both foreign and defense ministers) was last held in July 2024 [Japan, Philippines to hold 2-plus-2 security talks in July - Kyodo News](https://english.kyodonews.net/articles/-/48002).

Notably, Philippine President Marcos Jr. is scheduled to undertake a **State Visit to Japan from May 26–29, 2026**. State visits of this nature often include or are accompanied by high-level ministerial meetings, making a defense ministerial encounter plausible—but not certain—within the forecasting window.

These meetings typically occur a few times per year, often on the sidelines of multilateral events or during bilateral visits, rather than on a fixed schedule.

**Exact later resolution packet**

The question resolves YES. The Japan Ministry of Defense published an official press release titled "Japan-Philippines Defense Ministerial Meeting (Joint Press Statement)" dated May 31, 2026, confirming that on May 31, 2026, Japanese Defense Minister Shinjiro Koizumi and Philippine Secretary of National Defense Gilberto Teodoro, Jr. held a bilateral Defense Ministerial Meeting in Singapore on the sidelines of the 23rd IISS Asia Pacific Security Conference (Shangri-La Dialogue) [e12760]. Source URL: https://www.mod.go.jp/en/article/2026/05/45c008f13e32cdb63ef16520e4337fe3fd601788.html

This satisfies every resolution requirement:
- Date (May 31, 2026) falls within the window April 30, 2026 (00:00 UTC) to June 1, 2026 (23:59 UTC).
- The principal participants were the Japanese Minister of Defense (Koizumi) and the Philippine Secretary of National Defense (Teodoro) — not lower-level officials.
- A sidelines-of-multilateral-event meeting explicitly counts per the resolution criteria.
- The source is one of the four specified official websites (Japan MoD, https://www.mod.go.jp/en/).

Additionally, an even earlier qualifying meeting occurred on May 5, 2026, in Makati City, Philippines, when the same two officials held a Defense Ministerial Meeting during Koizumi's visit ahead of President Marcos's state visit to Japan (also reported by Japan MoD and DND). Either meeting alone is sufficient for a YES resolution.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-72. `ee1a438a-563a-55e3-a7de-6faf60495f1d`

- Present date: `2026-05-03 04:32:11.164212`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the FBI or DOJ announce the arrest of at least one individual connected to the March 2026 IoT botnet disruption operation by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the U.S. Federal Bureau of Investigation (FBI) or U.S. Department of Justice (DOJ) publishes an official press release or announcement confirming the [arrest](https://www.law.cornell.edu/wex/arrest) (i.e., the taking of a person into custody by legal authority) of at least one individual [connected to](https://en.wikipedia.org/wiki/Complicity) (i.e., charged with, indicted for, or officially named as a participant in) the March 19, 2026 IoT botnet disruption operation targeting the Aisuru, Kimwolf, JackSkid, and/or Mossad botnets, as originally announced by the DOJ at https://www.justice.gov/usao-ak/pr/authorities-disrupt-worlds-largest-iot-ddos-botnets-responsible-record-breaking-attacks.

The official announcement of the arrest must be published on or after May 1, 2026, and by June 1, 2026 (23:59 UTC).

Primary resolution sources are:
- FBI press releases: https://www.fbi.gov/news/press-releases
- DOJ press releases: https://www.justice.gov/news

If no such announcement appears on these pages by the resolution deadline, the question resolves **No**.

**Pre-cutoff background**

On March 19, 2026, the U.S. Department of Justice, in coordination with authorities in Canada and Germany, dismantled the online infrastructure behind four major IoT botnets — Aisuru, Kimwolf, JackSkid, and Mossad — which had compromised over 3 million devices worldwide and were responsible for record-breaking DDoS attacks reaching 31.4 Tbps (https://www.justice.gov/usao-ak/pr/authorities-disrupt-worlds-largest-iot-ddos-botnets-responsible-record-breaking-attacks). No arrests were announced at the time of the operation [Feds Disrupt IoT Botnets Behind Huge DDoS Attacks](https://krebsonsecurity.com/2026/03/feds-disrupt-iot-botnets-behind-huge-ddos-attacks/).

KrebsOnSecurity identified two primary suspects: a 22-year-old Canadian man described as a core operator of the Kimwolf botnet, and a 15-year-old residing in Germany [Feds Disrupt IoT Botnets Behind Huge DDoS Attacks](https://krebsonsecurity.com/2026/03/feds-disrupt-iot-botnets-behind-huge-ddos-attacks/). German police confirmed they had identified two suspected administrators who would face legal proceedings. As of early April 2026, Canadian law enforcement — the OPP and Sûreté du Québec — confirmed they are conducting active investigations related to the dismantled networks. Cryptocurrency was reportedly seized in connection with the probe. As of May 2, 2026, no arrest of the Canadian suspect or any other individual has been officially announced by the FBI or DOJ in connection with this operation. The investigation remains ongoing, with cross-border law enforcement cooperation between the U.S., Canada, and Germany continuing.

**Exact later resolution packet**

The question resolves YES.

The U.S. Department of Justice published an official press release on its justice.gov site (one of the specified resolution sources) titled "Canadian man arrested by international authorities, charged with administrating KimWolf DDoS botnet," dated Thursday, May 21, 2026 (URL: https://www.justice.gov/usao-ak/pr/canadian-man-arrested-international-authorities-charged-administrating-kimwolf-ddos). This date falls squarely within the required resolution window (on or after May 1, 2026, and by June 1, 2026 23:59 UTC).

The press release announces the ARREST (taking into custody) of Jacob Butler, aka "Dort," 23, of Ottawa, Canada, who was charged with administrating/operating the KimWolf DDoS botnet. KimWolf is one of the four botnets (Aisuru, Kimwolf, JackSkid, Mossad) that were the subject of the March 19, 2026 disruption operation originally announced by the DOJ. The individual was both arrested and criminally charged (criminal complaint unsealed in the District of Alaska, where the original operation was announced), and U.S. authorities are seeking his extradition. Multiple corroborating sources confirm this: The Hacker News (reporting May 22, 2026, citing the DOJ) [Kimwolf DDoS Botnet Operator Arrested in Canada Over DDoS-for ...](https://thehackernews.com/2026/05/kimwolf-ddos-botnet-operator-arrested.html), SecurityWeek, The Record, and Help Net Security all report the arrest of the KimWolf botnet administrator and explicitly link it to the March 2026 multi-botnet takedown.

All resolution criteria are met: (1) the source is the DOJ (justice.gov), an official primary resolution source; (2) the announcement explicitly confirms an arrest, not merely an indictment; (3) the arrest is connected to the March 19, 2026 operation via the Kimwolf botnet; (4) the announcement date (May 21, 2026) is within the May 1 – June 1, 2026 window; (5) the individual (Jacob Butler) was charged as an administrator/participant.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-73. `e24fc009-8a42-5cab-b6aa-21d38b5bec34`

- Present date: `2026-05-03 12:49:04.265319`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will SpaceX successfully launch Starship Flight 12 (first V3 architecture flight) by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if SpaceX's Starship Flight 12 — the first flight of the V3 architecture (Ship 39 / Booster 19) — lifts off and clears the launch tower at Starbase, Texas, at any time on or after May 1, 2026, 00:00 UTC, and before June 1, 2026, 23:59 UTC.

"Successfully launch" is defined as the vehicle clearing the launch tower (i.e., full liftoff with vertical ascent visibly above the tower structure). The flight does not need to reach orbit, achieve any specific mission objective, or land successfully. Abort after liftoff, in-flight anomaly, or vehicle destruction after clearing the tower all still count as a successful launch for resolution purposes.

The identity of the vehicle as "V3 architecture" will be verified by SpaceX's own public designation of the flight as "Flight 12" using Ship 39 and Booster 19, which SpaceX has publicly confirmed as V3 hardware [Starship Flight 12 inches closer to launch with booster and ship ...](https://spaceexplored.com/2026/04/18/starship-flight-12-inches-closer-to-launch-with-booster-and-ship-static-fires/).

If the launch is scrubbed, delayed past June 1, 2026 23:59 UTC, or does not occur, the question resolves **No**.

**Resolution source**: SpaceX's official mission page (https://www.spacex.com/launches/mission/?missionId=starship-flight-12) or SpaceX's official X/Twitter account (https://x.com/SpaceX). Secondary confirmation via credible space journalism outlets such as NASA Spaceflight (https://www.nasaspaceflight.com/), Space Explored (https://spaceexplored.com/), or Ars Technica (https://arstechnica.com/space/).

All dates and times in these resolution criteria are in UTC.

**Pre-cutoff background**

SpaceX is preparing for Starship Flight 12, the first flight of the upgraded "Version 3" (V3) Starship architecture. The V3 configuration features significant upgrades including third-generation Raptor engines with greater thrust, a taller vehicle structure, and other improvements critical to SpaceX's Starship Human Landing System (HLS) for NASA's Artemis program.

As of May 1, 2026, SpaceX has completed key pre-flight milestones [Starship Flight 12 inches closer to launch with booster and ship ...](https://spaceexplored.com/2026/04/18/starship-flight-12-inches-closer-to-launch-with-booster-and-ship-static-fires/):
- On April 14, 2026, SpaceX conducted a "full duration static fire" of Ship 39 (the V3 upper stage) at Starbase's Massey's test outpost.
- On April 15, 2026, SpaceX conducted a 33-engine static fire of Booster 19 (the V3 Super Heavy booster) at Launch Pad 2 at Starbase, Texas.
- Both vehicles were subsequently returned to their respective integration bays (MegaBay 1 and MegaBay 2) for final checkouts and integration.

The launch is currently targeted for approximately May 12, 2026, with a CADENA advisory window opening on that date. However, a TFR (Temporary Flight Restriction) was posted for May 4–18 for a possible additional 33-engine static fire of Booster 19, suggesting some anomaly from the earlier test may require further testing. SpaceX's Starship test flights have historically experienced delays due to regulatory approvals (FAA launch license), technical issues, and weather.

Key definitions:
- **Starship V3**: The third major design iteration of SpaceX's Starship/Super Heavy launch system, featuring upgraded Raptor 3 engines, increased propellant capacity, and a taller ship stage. For this question, "V3" is identified per SpaceX's own designation. Flight 12 uses Ship 39 and Booster 19, which SpaceX has publicly identified as V3 hardware [Starship Flight 12 inches closer to launch with booster and ship ...](https://spaceexplored.com/2026/04/18/starship-flight-12-inches-closer-to-launch-with-booster-and-ship-static-fires/). See: https://en.wikipedia.org/wiki/SpaceX_Starship
- **Flight 12**: SpaceX's 12th integrated test flight of the Starship/Super Heavy system. See: https://en.wikipedia.org/wiki/SpaceX_Starship_integrated_flight_test_program

**Exact later resolution packet**

The question resolves YES because SpaceX's Starship Flight 12 — the first flight of the V3 architecture using Ship 39 and Booster 19 — lifted off and cleared the launch tower at Starbase, Texas, on May 22, 2026, well within the required window (May 1, 2026 00:00 UTC to June 1, 2026 23:59 UTC).

Key evidence:
- SpaceX's official mission page (https://www.spacex.com/launches/starship-flight-12) states that "On Friday, May 22, 2026, at 5:30 p.m. CT, Starship lifted off from Starbase, Texas on its twelfth flight test," and confirms "This was the first flight of the Starship and Super Heavy V3 vehicles" [Starship's Twelfth Flight Test - SpaceX](https://www.spacex.com/launches/starship-flight-12).
- SpaceNews (https://spacenews.com/spacex-launches-first-starship-v3/) corroborates: "Starship lifted off from the company's facility at Starbase, Texas, at 6:30 p.m. Eastern on a mission designated Flight 12," describing it as the first flight of the completely redesigned (V3) vehicle [SpaceX launches first Starship V3 - SpaceNews](https://spacenews.com/spacex-launches-first-starship-v3/).

The vehicle identity as V3 hardware (Ship 39 / Booster 19) is consistent with the question's own designation. The launch date of May 22, 2026 (≈22:30 UTC) falls squarely within the May 1–June 1, 2026 window. The vehicle achieved full liftoff and cleared the tower, which satisfies the "successful launch" definition regardless of subsequent flight performance. The flight actually proceeded successfully to a planned splashdown, but only clearing the tower was required.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-74. `b5f4ddc4-6c75-57c4-a46b-224a6ae80e67`

- Present date: `2026-05-03 01:13:16.970072`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Taiwan's Legislative Yuan pass the special defense budget bill by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if any version of the special defense budget bill (the Executive Yuan's proposed NT$1.25 trillion bill, or any consolidated/amended version thereof) completes its third reading in Taiwan's Legislative Yuan on or after May 1, 2026 (00:00 UTC) and on or before June 1, 2026 (23:59 UTC).

"Passing" is defined as completion of the third reading in the Legislative Yuan, per the legislative procedure described at https://www.ly.gov.tw/EngPages/Detail.aspx?nodeid=335&pid=43232. Presidential signature is not required.

This question resolves **No** if no such bill completes its third reading by June 1, 2026 (23:59 UTC).

Resolution will be determined by official records published on the Legislative Yuan website (https://www.ly.gov.tw/EngPages/index.aspx) or credible English-language reporting from [Taipei Times](https://www.taipeitimes.com/), [Focus Taiwan](https://focustaiwan.tw/), or [Reuters](https://www.reuters.com/).

**Pre-cutoff background**

In late November 2025, Taiwan's Executive Yuan proposed a NT$1.25 trillion (approximately US$40 billion) special defense budget covering 2026–2033, aimed at strengthening Taiwan's defense resilience and asymmetric warfare capabilities, including missiles, drones, and the "Taiwan Dome" air defense system [https://understandingwar.org/research/china-taiwan/china-taiwan-update-april-17-2026/](https://understandingwar.org/research/china-taiwan/china-taiwan-update-april-17-2026/).

The bill has faced significant political obstacles. The opposition Kuomintang (KMT) and Taiwan People's Party (TPP) have repeatedly blocked its review in the Legislative Yuan's Procedure Committee. Three competing versions of the bill exist: the Executive Yuan's original proposal, a KMT version, and a TPP-proposed reduced version. On March 22, 2026, the Legislative Yuan began reviewing the three competing bills, but by March 26 lawmakers failed to reach consensus on most articles. The KMT has boycotted committee meetings related to the bill, creating partisan gridlock [https://understandingwar.org/research/china-taiwan/china-taiwan-update-april-17-2026/](https://understandingwar.org/research/china-taiwan/china-taiwan-update-april-17-2026/).

On April 15, 2026, legislators agreed that Premier Cho Jung-tai would present a report on the budget on April 21, after which the bills would be forwarded for committee review [https://understandingwar.org/research/china-taiwan/china-taiwan-update-april-17-2026/](https://understandingwar.org/research/china-taiwan/china-taiwan-update-april-17-2026/). The KMT has submitted a supplementary resolution requiring individual approval for large-sum military purchases, further complicating passage.

The Legislative Yuan is Taiwan's unicameral legislature composed of 113 members ([Wikipedia](https://en.wikipedia.org/wiki/Legislative_Yuan)). Bills must pass three readings to become law ([Legislative Procedure](https://www.ly.gov.tw/EngPages/Detail.aspx?nodeid=335&pid=43232)).

**Exact later resolution packet**

The question resolves YES. Taiwan's Legislative Yuan completed the third reading of the special defense budget bill on Friday, May 8, 2026, which falls within the resolution window of May 1, 2026 (00:00 UTC) to June 1, 2026 (23:59 UTC).

KEY EVIDENCE FROM SPECIFIED SOURCES:
- Reuters (May 8, 2026): "Taiwan's opposition-controlled parliament approved extra defence spending of $25 billion on Friday," confirming approval on May 8, 2026 of a version worth NT$780 billion (~US$24.86 billion), less than the originally proposed NT$1.25 trillion [71422b]. URL: https://www.reuters.com/world/asia-pacific/taiwan-parliament-approves-extra-defence-spending-less-than-government-wanted-2026-05-08/
- Taipei Times (May 14, 2026): "The Legislative Yuan passed the third reading of a special defense budget of NT$780 billion (US$24.75 billion)," explicitly confirming the THIRD READING was completed and that it fell short of the eight-year NT$1.25 trillion budget requested by the government [77feff]. URL: https://www.taipeitimes.com/News/taiwan/archives/2026/05/14/2003857340
- Taipei Times front page (May 9, 2026): "Legislature passes defense budget bill" — URL: https://www.taipeitimes.com/News/front/archives/2026/05/09/2003857017

WHY THIS SATISFIES THE CRITERIA:
The resolution criteria state the question resolves YES if "any version of the special defense budget bill (the Executive Yuan's proposed NT$1.25 trillion bill, or any consolidated/amended version thereof) completes its third reading." The NT$780 billion bill passed on May 8, 2026 is precisely an amended/consolidated version of the NT$1.25 trillion special defense budget proposal — the KMT/TPP opposition version that cut the Executive Yuan's NT$1.25 trillion request to a NT$780 billion ceiling. The Chinese-language official sources (CNA, PTS) confirm this was the "保衛國家安全及強化不對稱戰力計畫採購特別條例" (the special defense procurement bill) passed in third reading (三讀通過) on May 8, 2026 — the same special defense budget covering 2026–2033 referenced in the question, not the standard annual defense budget.

NOTE ON DISTINCT BILL: There was also a separate, much smaller NT$8.81 billion "2026 defense procurement budget" passed on May 29, 2026 (Focus Taiwan, Taipei Times). That is the first-year appropriation budget under the special framework, distinct from the special defense budget bill/ordinance itself. The relevant bill for this question (the version of the NT$1.25 trillion special defense budget) passed third reading on May 8, 2026.

The third reading was therefore completed within the window, satisfying the YES condition (presidential signature is explicitly not required).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-75. `5c0765ed-cbd1-5af5-bce0-adbfebd4e0f6`

- Present date: `2026-05-07 16:41:54.496597`
- Source cutoff boundary: `2026-05-08` (encodes end of UTC day `2026-05-07`)
- Expected resolution: `2026-06-12T00:00:00`

**Question**

Will Apple announce visionOS 27 (or a successor major version to visionOS 26) at WWDC 2026?

**Resolution criteria**

This question resolves **Yes** if Apple announces a new major version of visionOS—whether named "visionOS 27," "visionOS 3," or any other name designating a major release successor to visionOS 26—on or after May 6, 2026, and no later than June 12, 2026 (end of WWDC 2026, 23:59 UTC).

A qualifying "announcement" means either:
1. The new major visionOS version is mentioned during the WWDC 2026 keynote (as streamed at https://developer.apple.com/wwdc26/), OR
2. An official Apple Newsroom press release at https://www.apple.com/newsroom/ announces the new major visionOS version.

The announcement must describe a new major release of visionOS (i.e., a version intended to succeed visionOS 26 as a distinct major OS release). A minor point update to visionOS 26 (e.g., visionOS 26.5 or 26.6) does **not** qualify. A major update under any name—including a rebrand, a non-numbered release, or a differently named successor—**does** qualify, provided it is clearly presented as a new major version of the operating system for Apple Vision Pro or a successor spatial computing device.

The question resolves **No** if no such announcement is made by June 12, 2026, 23:59 UTC.

**Resolution sources:** The WWDC 2026 keynote (https://developer.apple.com/wwdc26/) and/or the Apple Newsroom (https://www.apple.com/newsroom/).

**Pre-cutoff background**

Apple has historically announced major new versions of its operating systems at WWDC each June. The current version of visionOS is visionOS 26 (latest release: 26.4, March 24, 2026; latest preview: 26.5 RC, May 4, 2026). Note that Apple transitioned to year-based OS naming starting with WWDC 2025, so the third major release of visionOS was called "visionOS 26" rather than "visionOS 3."

However, reports indicate Apple has effectively abandoned the Vision Pro platform. According to MacRumors (April 29, 2026), the M5 refresh of Apple Vision Pro—which added a faster M5 chip, 120Hz refresh rate, and improved battery life while retaining the $3,499 price—failed to revive consumer interest, with total sales reaching only approximately 600,000 units and an unusually high return rate [https://www.macrumors.com/2026/04/29/apple-vision-pro-m5-flop/](https://www.macrumors.com/2026/04/29/apple-vision-pro-m5-flop/). Apple has reportedly stopped work on Vision Pro, redistributed the team to other projects (notably Siri, led by former Vision Pro chief Mike Rockwell since March 2025), cancelled the "Vision Air" project, and shifted focus toward AI-powered smart glasses without integrated displays [https://www.macrumors.com/2026/04/29/apple-vision-pro-m5-flop/](https://www.macrumors.com/2026/04/29/apple-vision-pro-m5-flop/). Apple has not officially discontinued the Vision Pro and continues to sell the M5 model, but reportedly has no plans for a new model.

WWDC 2026 runs June 8–12, with the keynote expected on June 8. Other expected announcements include iOS 27 and macOS 27.

**Exact later resolution packet**

The question resolves YES because Apple announced visionOS 27 — a new major version succeeding visionOS 26 — at WWDC 2026 on June 8, 2026, which falls within the resolution window (May 6, 2026 to June 12, 2026, 23:59 UTC).

Both officially designated resolution sources confirm this:

1. Apple Newsroom press release (https://www.apple.com/newsroom/2026/06/apple-unveils-next-generation-of-apple-intelligence-siri-ai-and-more/): Apple explicitly lists "visionOS 27" among its next-generation operating systems, stating that improvements come "with iOS 27, iPadOS 27, macOS 27, watchOS 27, visionOS 27, and tvOS 27," and confirming in the Availability section that Apple Intelligence features arrive "this fall with iOS 27, iPadOS 27, macOS 27, watchOS 27, and visionOS 27" [6fb8a9].

2. Apple Developer WWDC 2026 keynote/session content (https://developer.apple.com/videos/play/wwdc2026/287/): The session "Build next-generation experiences with visionOS 27" presents visionOS 27 as the next major version of the OS for Apple Vision Pro, with new capabilities in RealityKit, Reality Composer Pro, Spatial Preview, and third-party accessory support — explicitly positioning it as the successor to visionOS 26 [ffae4e].

Corroborating third-party coverage (9to5Mac, June 8, 2026) also states "Today at WWDC, Apple announced visionOS 27, its next major software version for Vision Pro" [912238].

This satisfies the criterion that a new major version of visionOS (successor to visionOS 26) was announced via either the WWDC 2026 keynote (developer.apple.com) or an official Apple Newsroom press release within the required window. It is a major version bearing the "27" designation, not a minor point update. Therefore the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-76. `96632c8c-1bdd-5deb-9f65-deab719ac39b`

- Present date: `2026-05-16 15:44:02.769519`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

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

**Pre-cutoff background**

Since March 2026, multiple Ukrainian military drones have strayed into Baltic state airspace after crossing from Russia during Ukrainian long-range strikes on Russian infrastructure. Key incidents include a drone crash near Lake Lavysas in Lithuania (March 23), drones striking Estonia's Auvere power station and crashing in Latvia (March 25), and most notably on May 7, 2026, two suspected stray Ukrainian drones entering Latvia from Russia, one of which exploded at an oil storage facility in Rēzekne, damaging four empty oil tanks [2026 Ukrainian drone incursions into Baltic states - Wikipedia](https://en.wikipedia.org/wiki/2026_Ukrainian_drone_incursions_into_Baltic_states). The May 7 incident led to the resignation of Latvia's Defense Minister on May 10, 2026 [Latvian army allowed to shoot down drones via 'special means'](https://eng.lsm.lv/article/society/defence/21.01.2026-latvian-army-allowed-to-shoot-down-drones-via-special-means.a630857/).

As of May 13, 2026, no drone has been shot down over any Baltic state territory. The drones have crashed on their own or been found after the fact. French military aircraft were scrambled during the May 7 alert but no interception occurred [2026 Ukrainian drone incursions into Baltic states - Wikipedia](https://en.wikipedia.org/wiki/2026_Ukrainian_drone_incursions_into_Baltic_states).

Regarding rules of engagement: In January 2026, Latvia authorized its National Armed Forces and National Guard to use "special means" to capture, land, or destroy drones, subject to the condition that such action will not cause harm to people, animals, or third-party property [Latvian army allowed to shoot down drones via 'special means'](https://eng.lsm.lv/article/society/defence/21.01.2026-latvian-army-allowed-to-shoot-down-drones-via-special-means.a630857/). At the NATO level, following Russian airspace incursions in September 2025, NATO allies "opened the door" to shooting down aircraft violating Alliance airspace, though specific ROE remain classified [NATO's new engagement rules mark a turning point in response to ...](https://www.lemonde.fr/en/opinion/article/2025/09/30/nato-s-new-engagement-rules-mark-a-turning-point-in-response-to-russian-incursions_6745924_23.html). Poland has precedent for more aggressive action against drones near its airspace. The Baltic states have jointly called for strengthened air defense and counter-drone capabilities, and Latvia's incoming defense minister has identified "safe sky" as a priority [Latvian army allowed to shoot down drones via 'special means'](https://eng.lsm.lv/article/society/defence/21.01.2026-latvian-army-allowed-to-shoot-down-drones-via-special-means.a630857/).

The question captures real uncertainty: the Baltic states now have legal authority and political motivation to shoot down drones, drone incursions are recurring, yet operational and safety constraints have so far prevented any shoot-down.

**Exact later resolution packet**

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

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-77. `4b901b95-42aa-5956-b877-f7d93ecc9faf`

- Present date: `2026-05-02 19:17:14.547198`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the European Court of Human Rights deliver a judgment finding a violation by Greece in a migration or asylum-related case between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, according to the HUDOC database (https://hudoc.echr.coe.int/), at least one judgment is published between 00:00 UTC on May 1, 2026 and 23:59 UTC on June 1, 2026 that meets ALL of the following criteria:

1. **Respondent State:** Greece (Hellenic Republic).
2. **Ruling against Greece:** The judgment finds a violation of one or more articles of the European Convention on Human Rights.
3. **Migration or asylum-related subject matter:** The case concerns the treatment, detention, reception, removal, expulsion, or pushback of asylum seekers, refugees, or migrants by Greek authorities. Specifically, the case must involve at least one complaint under Article 2 (right to life), Article 3 (prohibition of torture and inhuman or degrading treatment), Article 4 of Protocol No. 4 (prohibition of collective expulsion), Article 5 (right to liberty and security), or Article 13 (right to an effective remedy) in the context of migration or asylum.

The primary resolution source is the HUDOC database at https://hudoc.echr.coe.int/. A judgment is considered published on the date it appears in the HUDOC database. Only judgments (not decisions on admissibility, interim measures, or communicated cases) count for resolution. If the HUDOC database is unavailable, official ECtHR press releases (https://www.echr.coe.int/press) may be used as an alternative source.

If no such judgment is published within the specified timeframe, the question resolves **No**.

**Pre-cutoff background**

The European Court of Human Rights (ECtHR) has repeatedly ruled against Greece on migration and asylum matters. On January 22, 2026, the Court delivered a judgment in *A.N. and Others v. Greece*, finding a violation of Article 3 (prohibition of inhuman or degrading treatment) due to living conditions of unaccompanied minors at the Samos Reception and Identification Centre [CASE OF AN AND OTHERS v. GREECE - HUDOC](https://hudoc.echr.coe.int/?i=001-247913). As of early 2026, of the 53,194 applications pending before the Court, approximately 870 (around 1.5%) relate to immigration matters. At least eight additional cases concerning Greek pushback practices are pending before the ECtHR, involving applicants from Turkey, Iraq, Iran, Tunisia, Palestine, Lebanon, Syria, Central African Republic, Cameroon, Congo, and Afghanistan [Greece's systematic pushback practice confirmed by European ...](https://www.ecchr.eu/en/case/greece-before-the-european-court-of-human-rights/). In January 2025, the Court ruled on two pushback-related cases (*A.R.E. v. Greece* and *G.R.J. v. Greece*) [Greece's systematic pushback practice confirmed by European ...](https://www.ecchr.eu/en/case/greece-before-the-european-court-of-human-rights/). Greece's migration policies in 2025–2026 have drawn criticism from Amnesty International, Human Rights Watch, and the UN Special Rapporteur, particularly regarding the suspension of asylum applications and allegations of systematic pushbacks. The Committee of Ministers is scheduled to examine groups of migration-related cases against Greece at its Human Rights meeting in September 2026. Given the volume of pending cases, the ECtHR regularly issues judgments against Greece on migration matters, though the exact timing of any specific ruling is uncertain.

**Exact later resolution packet**

The question resolves YES. On 26 May 2026 — within the resolution window of 1 May to 1 June 2026 — the Third Section of the European Court of Human Rights delivered a Chamber judgment in J.B. v. Greece (Application no. 54796/16), published in the HUDOC database (item 001-250202) [5b24cd, 0e6a50].

All four resolution criteria are satisfied:
1. Respondent State: Greece (Hellenic Republic) [5b24cd, 0e6a50].
2. Ruling against Greece / finds a violation: The Court found a VIOLATION of Article 3 of the Convention (prohibition of inhuman or degrading treatment) on account of the applicant's conditions of detention in a police station (Mytilene). It found no violation of Article 13, but a violation of at least one article suffices [5b24cd, 0e6a50].
3. Migration/asylum subject matter with a qualifying complaint: The case concerned a Syrian national of Armenian origin who entered Greece irregularly in May 2016, his asylum claim and potential return to Türkiye under the EU-Türkiye Statement, and the conditions of his detention pending removal. It involved complaints under Article 3 (conditions of detention) and Article 13 in the migration/asylum context — both qualifying articles listed in criterion 3 [5b24cd, 0e6a50].
4. It is a Judgment (Chamber judgment), not a decision on admissibility or interim measure [0e6a50].

The judgment URL is https://hudoc.echr.coe.int/?i=001-250202 [5b24cd]. This is not a conditional question, so no antecedent check applies. Therefore the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-78. `e9efc313-b658-5f08-9131-d6ebdeba1e68`

- Present date: `2026-05-01 19:14:36.536940`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will SpaceX launch Starship Flight 12 (first Version 3 / Block 3 flight) before 23:59 UTC on June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if SpaceX's Starship Flight 12—the first flight using Version 3 / Block 3 hardware—lifts off from the launch pad (defined as the vehicle clearing the launch mount/tower under its own power) on or after April 30, 2026, and before 23:59 UTC on June 1, 2026.

The question resolves **No** if no such liftoff occurs by that deadline.

"Launch" is defined as the vehicle lifting off the launch pad and clearing the tower under its own power. A launch abort after engine ignition that does not result in the vehicle leaving the pad does not count.

"Version 3" / "Block 3" refers to the third major hardware iteration of the Starship-Super Heavy system as described on the Wikipedia Starship page (https://en.wikipedia.org/wiki/SpaceX_Starship) and tracked on the List of Starship launches (https://en.wikipedia.org/wiki/List_of_Starship_launches).

**Resolution sources:** SpaceX's official launches page (https://www.spacex.com/launches), Next Spaceflight's Flight 12 page (https://nextspaceflight.com/launches/details/8002/), or credible spaceflight reporting from outlets such as Space.com, NASASpaceFlight.com, or Ars Technica.

**Pre-cutoff background**

SpaceX is preparing Starship Flight 12, the inaugural flight of the "Version 3" (also called "Block 3") Starship vehicle. Version 3 / Block 3 refers to the third major iteration of the Starship-Super Heavy launch system, featuring increased power and payload capacity compared to the retired Block 1 and Block 2 vehicles (see https://en.wikipedia.org/wiki/SpaceX_Starship for details) [https://en.wikipedia.org/wiki/List_of_Starship_launches](https://en.wikipedia.org/wiki/List_of_Starship_launches).

Flight 12 is planned as the first launch from Starbase's second orbital launch pad (OLP-2) and will use Booster 19 (B19) and Ship 39 (S39), after the originally designated Booster 18 was scrapped following damage during testing [https://en.wikipedia.org/wiki/List_of_Starship_launches](https://en.wikipedia.org/wiki/List_of_Starship_launches). As of May 1, 2026, SpaceX is targeting a launch in May 2026 [https://en.wikipedia.org/wiki/List_of_Starship_launches](https://en.wikipedia.org/wiki/List_of_Starship_launches). However, the mission has experienced repeated delays—originally targeting mid-March 2026, then slipping multiple times. SpaceX conducted a full-duration static fire test of the V3 Starship upper stage in April 2026, clearing a significant milestone. Given the history of delays and the novelty of both the V3 hardware and the new launch pad, there is meaningful uncertainty about whether launch occurs before June 1, 2026.

**Exact later resolution packet**

The question resolves YES. SpaceX's official Flight 12 page states that "On Friday, May 22, 2026, at 5:30 p.m. CT, Starship lifted off from Starbase, Texas on its twelfth flight test," and confirms it was the first flight of the Starship and Super Heavy V3 (Version 3 / Block 3) vehicles [a9e333]. Wikipedia's "Starship flight test 12" article gives a precise liftoff time of May 22, 2026, 22:30:22 UTC, with all engines lit at liftoff (confirming the vehicle cleared the launch mount/tower under its own power), and confirms it used Version 3 / Block 3 hardware with Booster 19 and Ship 39 [7a6ce9].

Window check: The resolution criteria require liftoff on or after April 30, 2026 and before 23:59 UTC on June 1, 2026. The liftoff at 22:30:22 UTC on May 22, 2026 falls squarely within this window. (Note: an initial attempt on May 21 was scrubbed, but the actual launch occurred May 22.)

All checklist conditions met: (1) liftoff within the window; (2) vehicle cleared the tower under its own power with all engines lit (not just ignition or pad abort); (3) it was the first Version 3 / Block 3 flight (Flight 12) using Booster 19 and Ship 39; (4) supported by allowed sources SpaceX (https://www.spacex.com/launches/starship-flight-12) and credible reporting; time zone correctly converted from 5:30 p.m. CT to 22:30 UTC, still before the deadline.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-79. `2142164e-3686-5db9-bb27-9342b1e0ac58`

- Present date: `2026-05-07 22:42:04.905485`
- Source cutoff boundary: `2026-05-08` (encodes end of UTC day `2026-05-07`)
- Expected resolution: `2026-06-18T00:00:00`

**Question**

Will US President Trump attend the 52nd G7 Summit in Évian-les-Bains, France, in person?

**Resolution criteria**

This question resolves **Yes** if [US President Donald Trump](https://en.wikipedia.org/wiki/Donald_Trump) is physically present at the [52nd G7 summit](https://en.wikipedia.org/wiki/52nd_G7_summit) venue in Évian-les-Bains, France, during at least one official session or meeting of the summit between June 15, 2026, and June 17, 2026 (UTC).

This question resolves **No** if Trump does not physically attend any official session or meeting at the summit venue during June 15–17, 2026 (UTC). Sending a delegate or participating remotely (e.g., via video call) does not count as attending in person. Arriving at the venue but departing before participating in any official session also does not count.

Resolution will be determined based on official [G7 summit communications](https://www.elysee.fr/en), reporting from the [White House](https://www.whitehouse.gov/), or credible major news agencies such as [Reuters](https://www.reuters.com/), [AP](https://apnews.com/), or [The New York Times](https://www.nytimes.com/). If no credible source confirms Trump's physical presence at an official session by July 1, 2026, 23:59 UTC, the question resolves **No**.

**Pre-cutoff background**

The [52nd G7 summit](https://en.wikipedia.org/wiki/52nd_G7_summit) is scheduled for June 15–17, 2026, in Évian-les-Bains, Haute-Savoie, France. The summit was originally planned for June 14–16 but was postponed by one day to avoid a scheduling conflict with [US President Donald Trump](https://en.wikipedia.org/wiki/Donald_Trump)'s birthday (June 14) and a UFC event [52nd G7 summit - Wikipedia](https://en.wikipedia.org/wiki/52nd_G7_summit).

As of May 7, 2026, Trump's attendance remains uncertain but likely. On May 1, 2026, Trump stated he would "probably" attend the summit, according to [Bloomberg](https://www.bloomberg.com/news/articles/2026-05-01/trump-says-he-will-probably-go-to-g-7-summit-in-france) and other outlets. French President Emmanuel Macron has also extended a post-summit dinner invitation at Versailles to entice Trump's attendance, according to [Reuters](https://www.reuters.com/world/europe/macron-seeks-draw-trump-g7-with-post-summit-invite-versailles-2026-04-10/). However, Trump has a history of unpredictable behavior at multilateral summits, including leaving the 2018 G7 early and skipping sessions at other international gatherings. Ongoing US trade disputes with allies add further uncertainty to his participation.

**Exact later resolution packet**

The question resolves YES. US President Donald Trump was physically present at the 52nd G7 summit venue in Évian-les-Bains, France, and participated in at least one official session/meeting during June 15–17, 2026.

Evidence from the specifically permitted sources:

1. Reuters ("US President Trump has landed in Evian for G7 summit, French presidency says," June 15, 2026, https://www.reuters.com/world/europe/us-president-trump-has-landed-evian-g7-summit-french-presidency-says-2026-06-15/): The French presidency confirmed "U.S. President Donald Trump has landed in Evian-les-Bains to attend the G7 summit," with a photo caption "U.S. President Donald Trump arrives to attend the G7 Summit, in Evian-les-Bains, France, June 15, 2026." [22d4a5]

2. Associated Press (live coverage, June 15, 2026, https://apnews.com/live/g7-summit-trump-updates-06-15-2026): Confirms Trump arrived, held a bilateral meeting with French President Emmanuel Macron on the sidelines of the summit, and participated in a working dinner with the other G7 leaders (France, Germany, UK, Canada, Italy, Japan) at the Hotel Royal Évian on June 15, 2026, with photographic evidence of him at the leaders' table. [c55a66]

3. The White House (official video library, https://www.whitehouse.gov/videos/president-trump-attends-g7-in-evian-france/): Published videos including "President Trump meets with President of France Emmanuel Macron ahead of the G7 Summit" (June 15, 2026) and "President Trump breaks down the Iran deal to close out the G7 Summit in Evian, France" (June 17, 2026), confirming his participation across the summit dates. [078a28]

4. Wikipedia's article on the 52nd G7 summit (https://en.wikipedia.org/wiki/52nd_G7_summit) corroborates that Trump was a participant, that he attended a Ukraine working session, and that he remained in France through the post-summit dinner on June 17, 2026, with no indication he left before participating in official sessions. [de6809]

These confirm all checklist requirements: (a) physical presence at the specific Évian-les-Bains venue (not merely in France or at the Versailles dinner); (b) participation in official sessions/meetings (bilateral with Macron, working dinner, Ukraine working session, group photo) — he did not merely arrive and depart; (c) his personal physical presence, not a delegate or remote video participation; and (d) within the June 15–17, 2026 (UTC) window. Sources are from the permitted set (Reuters, AP, White House).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-80. `1cf01a42-0810-5a33-8697-d491d3a2b7b9`

- Present date: `2026-05-01 10:17:44.818231`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-05-16 00:00:00`

**Question**

Will Kevin Warsh be confirmed by the U.S. Senate as Federal Reserve Chair by May 15, 2026?

**Resolution criteria**

This question resolves as **Yes** if the U.S. Senate passes a [simple majority](https://en.wikipedia.org/wiki/Supermajority#United_States) floor vote confirming Kevin Warsh as a Member and Chair of the Board of Governors of the Federal Reserve System on or after April 30, 2026, and on or before May 15, 2026, 11:59 PM UTC. It resolves as **No** otherwise.

The confirmation event must be a roll call or voice vote on the Senate floor, as distinct from a committee vote. The resolution source is the official U.S. Senate roll call vote records at [https://www.senate.gov/legislative/votes.htm](https://www.senate.gov/legislative/votes.htm). Credible news reporting from sources such as [Reuters](https://www.reuters.com), [AP](https://apnews.com), or [CNBC](https://www.cnbc.com) may also be used to verify the outcome if Senate records are not yet updated.

**Pre-cutoff background**

As of May 1, 2026, Kevin Warsh's nomination to serve as Chair of the [Board of Governors of the Federal Reserve System](https://en.wikipedia.org/wiki/Chair_of_the_Federal_Reserve) is advancing toward a full Senate floor vote. On April 29, 2026, the Senate Banking Committee voted 13–11 along party lines to advance his nomination [Trump Fed pick Kevin Warsh clears key Senate hurdle, teeing up ...](https://www.cnbc.com/2026/04/29/trump-fed-nominee-kevin-warsh-senate-approval.html). Current Fed Chair Jerome Powell's term expires on May 15, 2026. Powell has indicated he would serve as "chair pro tem" if no successor is confirmed by that date.

Warsh's nomination had previously been delayed by Sen. Thom Tillis (R-NC), who vowed to block the confirmation vote until a Department of Justice criminal investigation into Fed Chair Powell regarding headquarters renovation cost overruns was resolved [Fed chair nominee Kevin Warsh vows not to be Trump's ' ...](https://www.cnn.com/2026/04/21/business/live-news/kevin-warsh-fed-confirmation-hearing). Following the DOJ's decision to drop the probe, Tillis lifted his hold, allowing the committee vote to proceed [Trump Fed pick Kevin Warsh clears key Senate hurdle, teeing up ...](https://www.cnbc.com/2026/04/29/trump-fed-nominee-kevin-warsh-senate-approval.html). The full Senate vote is expected during the week of May 11, 2026, meaning Warsh could potentially be confirmed before Powell's term ends [Trump Fed pick Kevin Warsh clears key Senate hurdle, teeing up ...](https://www.cnbc.com/2026/04/29/trump-fed-nominee-kevin-warsh-senate-approval.html).

All 11 Democrats on the Banking Committee voted against the nomination [Trump Fed pick Kevin Warsh clears key Senate hurdle, teeing up ...](https://www.cnbc.com/2026/04/29/trump-fed-nominee-kevin-warsh-senate-approval.html). Democratic senators, led by ranking member Elizabeth Warren, have raised concerns about Warsh's financial disclosures, his record during the 2008 financial crisis, and alleged ties to Jeffrey Epstein [Fed chair nominee Kevin Warsh vows not to be Trump's ' ...](https://www.cnn.com/2026/04/21/business/live-news/kevin-warsh-fed-confirmation-hearing). In the full Senate, Republicans hold a majority, making confirmation likely but not guaranteed given the narrow timeline and potential procedural delays.

**Exact later resolution packet**

YES. The resolution criteria required a U.S. Senate floor roll call or voice vote, not merely the April 29 committee vote, confirming Kevin Warsh as both Member and Chair of the Board of Governors of the Federal Reserve System during the window from April 30, 2026 through May 15, 2026 at 11:59 PM UTC. The official U.S. Senate roll call record for Vote 116 shows a Senate floor roll call vote on May 12, 2026, "On the Nomination (Confirmation: Kevin Warsh, of Florida, to be a Member of the Federal Reserve Board)," with the result "Nomination Confirmed" and a tally of 51 yeas, 45 nays, and 4 not voting [Roll Call Vote 119 th Congress - 2 nd Session - Senate.gov](https://www.senate.gov/legislative/LIS/roll_call_votes/vote1192/vote_119_2_00116.htm). The official U.S. Senate roll call record for Vote 120 shows a Senate floor roll call vote on May 13, 2026, "On the Nomination (Confirmation: Kevin Warsh, of Florida, to be Chairman of the Board of Governors, Federal Reserve Board)," with the result "Nomination Confirmed" and a tally of 54 yeas, 45 nays, and 1 not voting [Roll Call Vote 119 th Congress - 2 nd Session - Senate.gov](https://www.senate.gov/legislative/LIS/roll_call_votes/vote1192/vote_119_2_00120.htm). These were full Senate floor roll call votes, and both successful confirmation votes occurred after April 30, 2026 and before May 15, 2026 at 11:59 PM UTC; no edge-case time-zone conversion can move May 12 or May 13 past the UTC deadline. Direct official Senate URLs: Member vote, https://www.senate.gov/legislative/LIS/roll_call_votes/vote1192/vote_119_2_00116.htm ; Chair vote, https://www.senate.gov/legislative/LIS/roll_call_votes/vote1192/vote_119_2_00120.htm . Therefore the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-81. `56552737-e7f5-5c74-93af-d71bba888c59`

- Present date: `2026-05-14 10:17:03.423069`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Putin and Xi Jinping issue a joint statement mentioning Ukraine during Putin's visit to China between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if ALL of the following conditions are met:

1. **Putin visits China**: Vladimir Putin is physically present in mainland China on or after May 12, 2026 (UTC) and before July 1, 2026, 23:59 UTC, for an official state visit or bilateral meeting with Xi Jinping.

2. **A joint statement is issued**: The governments of Russia and China publish a joint document (titled "Joint Statement," "Joint Declaration," "Joint Communiqué," or equivalent) associated with that visit.

3. **The statement mentions Ukraine**: The English-language text of the joint statement contains the literal word "Ukraine" or "Ukrainian" (case-insensitive). If no official English-language version exists, the Russian-language version must contain "Украин" (as a root matching "Украина," "Украинский," etc.) or the Chinese-language version must contain "乌克兰."

The joint statement must be published on at least one of the following official government websites:
- The official website of the President of Russia: http://en.kremlin.ru/
- The Ministry of Foreign Affairs of the People's Republic of China: https://www.fmprc.gov.cn/eng/

The question resolves as **No** if:
- Putin does not visit mainland China on or after May 12, 2026 and before July 1, 2026 (UTC), OR
- No joint statement is issued during the visit, OR
- A joint statement is issued but does not contain the word "Ukraine" / "Ukrainian" (or equivalents as defined above).

**Pre-cutoff background**

Russian President Vladimir Putin is expected to visit China during the week beginning May 18, 2026, according to the Russian newspaper Vedomosti [Russia ready to help China with energy ahead of Putin's visit ...](https://www.reuters.com/world/china/putin-visit-china-first-half-2026-agencies-cite-lavrov-2026-04-15/). Russian Foreign Minister Sergei Lavrov confirmed in April 2026 that Putin would visit China in the first half of 2026 [Russia ready to help China with energy ahead of Putin's visit ...](https://www.reuters.com/world/china/putin-visit-china-first-half-2026-agencies-cite-lavrov-2026-04-15/). The visit follows U.S. President Donald Trump's state visit to China on May 13–15, 2026, making it a rare "diplomatic double-header" for Beijing [What does it mean for China if Donald Trump and Vladimir Putin visit ...](https://www.scmp.com/news/china/diplomacy/article/3348148/what-does-it-mean-china-if-donald-trump-and-vladimir-putin-visit-back-back).

Russia-China joint statements have varied in their treatment of Ukraine. During Xi Jinping's visit to Moscow in May 2025, China and Russia issued a joint statement that addressed the conflict. A separate "Joint Statement on Global Strategic Stability" issued on May 8, 2025, did not mention Ukraine [JOINT STATEMENT by the People's Republic of China and the ...](https://www.fmprc.gov.cn/mfa_eng/zy/jj/xjpdelsjxgsfwcxjnslwgzzslqd/202505/t20250509_11617864.html). In May 2025, China and Brazil also issued a joint statement on the Ukraine crisis welcoming Russia's proposal to open peace talks.

The key uncertainty is whether, in the context of evolving U.S.-brokered peace negotiations and Trump's diplomatic engagement with both sides, China will be willing to co-sign language explicitly referencing Ukraine in a bilateral statement with Russia—or whether Beijing will opt for more general language to preserve diplomatic flexibility as a potential mediator.

**Exact later resolution packet**

The question resolves YES because all three required conditions are satisfied:

**Condition 1 — Putin visited mainland China within the window (May 12 – July 1, 2026):** Vladimir Putin paid an official/state visit to Beijing on May 19–20, 2026, at Xi Jinping's invitation. This is confirmed by the official Kremlin website (en.kremlin.ru), which states Putin "arrived in China on an official visit" and records press statements dated May 20, 2026 [9fa23f, 3c5a48], and by China's Ministry of Foreign Affairs [33fa73] and Wikipedia [c9287a]. May 19–20, 2026 falls squarely within the May 12 – July 1, 2026 window.

**Condition 2 — A joint statement was issued:** Following the talks, Putin and Xi signed the "Joint Statement of the Russian Federation and the People's Republic of China On Further Strengthening Comprehensive Partnership and Strategic Cooperation and On Deepening Relations of Good-Neighbourliness, Friendship and Cooperation," along with a "Joint Declaration on the Formation of a Multipolar World and a New Type of International Relations." This is confirmed by en.kremlin.ru [3c5a48] and the Chinese MFA [33fa73, b9b715].

**Condition 3 — The statement mentions Ukraine:** The full text of the Joint Statement, published on the official Chinese Ministry of Foreign Affairs website (fmprc.gov.cn), explicitly contains "乌克兰" (Ukraine). The MFA text states: "双方认为必须在充分、完整、全面遵循《联合国宪章》原则基础上消除乌克兰危机根源... 俄方积极评价中方在乌克兰局势问题上的客观公正立场，欢迎中方愿为通过政治外交途径解决乌克兰危机发挥建设性作用" [b9b715]. The English/Russian versions likewise reference Ukraine: the statement says "the root causes of the Ukraine crisis must be eliminated" and "The Russian side positively evaluated China's objective and fair position on the situation in Ukraine and welcomed China's willingness to play a constructive role in resolving the Ukrainian crisis through political and diplomatic means" [bede64, aa52ab].

This satisfies the resolution criterion that the joint statement contains the literal word "Ukraine"/"Ukrainian" (or the Chinese equivalent "乌克兰"), published on an official government website (fmprc.gov.cn / en.kremlin.ru).

Official source URLs:
- Kremlin (visit + joint statement): http://en.kremlin.ru/events/president/news/79782 and http://en.kremlin.ru/events/president/news/79787
- Chinese MFA full text (contains 乌克兰): https://www.fmprc.gov.cn/zyxw/202605/t20260521_11914932.shtml

All conditions met → YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-82. `b5a5f3eb-c6ff-53b8-af90-165b7a6edd91`

- Present date: `2026-04-30 17:30:41.033085`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

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

**Pre-cutoff background**

The Nintendo Switch 2 launched on June 5, 2025, and is approaching its one-year anniversary. As of April 30, 2026, Nintendo has confirmed several first-party titles for the system including: Yoshi and the Mysterious Book (May 21, 2026), Splatoon Raiders (July 23, 2026), Rhythm Heaven Groove (July 2, 2026), and Fire Emblem: Fortune's Weave (2026, tentative) [Nintendo Switch 2: All Confirmed Games & Release Dates](https://www.nintendolife.com/guides/nintendo-switch-2-all-confirmed-games-and-release-dates). The most recent Nintendo Direct was a Partner Showcase on February 5, 2026, which focused on third-party titles. Multiple credible sources and leakers have indicated that the next major general Nintendo Direct is not expected until June 2026, though individual game reveals outside of Directs remain possible. Nintendo has historically used the May–June window for major announcements, and the Switch 2's first anniversary creates a natural occasion for new reveals. However, the absence of a confirmed Direct in the April 30–June 1 window introduces meaningful uncertainty about whether a new first-party game will be announced during this period.

**Exact later resolution packet**

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

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-83. `95af7649-c12e-5421-bfc5-b4602e9140db`

- Present date: `2026-05-12 19:50:20.669605`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Olympiacos win the 2026 EuroLeague Championship (Final Four held May 22–24 in Athens)?

**Resolution criteria**

This question resolves **Yes** if Olympiacos B.C. is declared the 2026 EuroLeague Basketball champion by the Euroleague Basketball organization, and **No** otherwise.

The winner is defined as the team declared champion by Euroleague Basketball, regardless of whether the victory occurred in regular time, overtime, or via forfeit/disqualification.

Resolution is based on the official results published on the EuroLeague website (https://www.euroleaguebasketball.net/euroleague/final-four/). The championship game is scheduled for May 24, 2026 at approximately 20:30 EEST (UTC+3).

If the Final Four tournament is postponed, cancelled, or not completed by July 1, 2026 (23:59 UTC), this question resolves **No**.

**Pre-cutoff background**

The 2026 EuroLeague Final Four is scheduled for May 22–24, 2026, at the Telekom Center in Athens, Greece [2026 EuroLeague Final Four - Wikipedia](https://en.wikipedia.org/wiki/2026_EuroLeague_Final_Four). This is the first Final Four to exclude a third-place play-off match [2026 EuroLeague Final Four - Wikipedia](https://en.wikipedia.org/wiki/2026_EuroLeague_Final_Four). The four qualified teams and bracket are as follows:

- **Semifinal A (May 22):** Olympiacos vs. Fenerbahçe Beko
- **Semifinal B (May 22):** TBD (Winners of Playoff D) vs. Real Madrid
- **Championship Game:** May 24, 2026

Olympiacos qualified on May 5, 2026, and is the #1 seed in the tournament, enjoying home-court advantage as an Athens-based club [2026 EuroLeague Final Four - Wikipedia](https://en.wikipedia.org/wiki/2026_EuroLeague_Final_Four). They face Fenerbahçe Beko in Semifinal A. Real Madrid qualified on May 7 and Fenerbahçe Beko on May 8 [2026 EuroLeague Final Four - Wikipedia](https://en.wikipedia.org/wiki/2026_EuroLeague_Final_Four).

**Historical context on home-court advantage in the EuroLeague Final Four:** Since the Final Four format began, the host city's team has won the championship only approximately 6 times out of 40 tournaments (roughly 15%), including wins by Real Madrid in Madrid (2015), Fenerbahçe in Istanbul (2017), and Panathinaikos in Athens (2007) [EuroLeague Final Four - Wikipedia](https://en.wikipedia.org/wiki/EuroLeague_Final_Four). This suggests that while playing at home provides some advantage, it is far from decisive. With four teams competing, a naive base rate for any single team winning is 25%. Forecasters should weigh Olympiacos's home-court edge, roster strength, and semifinal matchup dynamics against the historical evidence that host teams do not dominate Final Four outcomes.

Official results will be published at: https://www.euroleaguebasketball.net/euroleague/final-four/

**Exact later resolution packet**

The question resolves YES. Olympiacos B.C. was declared the 2026 EuroLeague Basketball champion by Euroleague Basketball.

Evidence:
- The official EuroLeague website (the specified resolution source) published a game report titled "Olympiacos crowned EuroLeague champions after thrilling tussle with Real Madrid," stating that Olympiacos Piraeus "finally claimed its first EuroLeague title since 2013 with a pulsating 92-85 victory over Real Madrid," played at the Telekom Center in Athens [Olympiacos crowned EuroLeague champions after thrilling tussle ...](https://www.euroleaguebasketball.net/euroleague/news/olympiacos-crowned-euroleague-champions-after-thrilling-tussle-with-real-madrid/). URL: https://www.euroleaguebasketball.net/euroleague/news/olympiacos-crowned-euroleague-champions-after-thrilling-tussle-with-real-madrid/
- The official EuroLeague Final Four hub page (https://www.euroleaguebasketball.net/euroleague/final-four/), the exact URL named in the resolution criteria, confirms Olympiacos as the 2026 champion, featuring the championship game highlights (Olympiacos-Real Madrid) and Olympiacos's trophy celebration in Piraeus [Final Four - Euroleague Basketball](https://www.euroleaguebasketball.net/euroleague/final-four/).

The Final Four was held on schedule (May 22–24, 2026) and completed well before the July 1, 2026 (23:59 UTC) deadline, so the fallback NO-resolution clause for postponement/cancellation/non-completion does not apply.

Corroborating sources (secondary, consistent): Wikipedia's "2026 EuroLeague Final Four" article lists Olympiacos as champions (4th title) with a 92-85 win over Real Madrid; ESPN and AP (via thestar.com) reported "Olympiakos beats Real Madrid 92-85 to win EuroLeague title"; and BasketNews reported Evan Fournier was named 2026 Final Four MVP. All independently confirm the same outcome and identical 92-85 score.

Therefore, per the resolution criterion ("resolves Yes if Olympiacos B.C. is declared the 2026 EuroLeague Basketball champion by the Euroleague Basketball organization"), this resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-84. `1a7c4056-3f4d-5ee7-a546-20cf0603b946`

- Present date: `2026-05-14 05:25:17.477287`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the U.S. Supreme Court rule in favor of Exxon Mobil in Exxon Mobil Corp. v. Corporación Cimex, S.A. by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the Supreme Court of the United States, in its opinion in *Exxon Mobil Corp. v. Corporación Cimex, S.A.* (No. 24-699), holds that Title III of the Helms-Burton Act abrogates foreign sovereign immunity under the FSIA for the claims at issue — meaning Exxon Mobil need not independently satisfy a separate FSIA exception to proceed with its lawsuit against the Cuban state-owned defendants. This includes any ruling (whether unanimous, majority, or plurality) whose holding permits Exxon Mobil's claims to proceed on the theory that the Helms-Burton Act itself overcomes FSIA immunity.

This question resolves **No** if:
- The Court holds that the FSIA's immunity protections remain in effect and Exxon Mobil must satisfy a separate FSIA exception (e.g., the commercial activity exception) to sue the Cuban entities; OR
- The Court dismisses the case as improvidently granted (DIG); OR
- The Court decides the case on grounds that do not address whether the Helms-Burton Act abrogates FSIA immunity (e.g., standing, ripeness, or other procedural grounds); OR
- No opinion is issued between May 12, 2026, and July 1, 2026 (inclusive).

The ruling must be issued between May 12, 2026, and July 1, 2026 (inclusive). The resolution source is the official opinion published on the [Supreme Court of the United States website](https://www.supremecourt.gov/opinions/slipopinion/25).

**Pre-cutoff background**

The U.S. Supreme Court case *Exxon Mobil Corp. v. Corporación Cimex, S.A.* (No. 24-699) concerns whether U.S. companies can sue Cuban state-owned entities under Title III of the [Cuban Liberty and Democratic Solidarity (LIBERTAD) Act of 1996](https://www.congress.gov/bill/104th-congress/house-bill/927), commonly known as the **Helms-Burton Act**, for property confiscated by the Cuban government — without separately satisfying an exception under the [Foreign Sovereign Immunities Act (FSIA)](https://www.law.cornell.edu/uscode/text/28/part-IV/chapter-97).

**Key legal question:** The Helms-Burton Act (Title III) creates a private right of action against those who "traffic" in confiscated property. The FSIA generally grants foreign states and their instrumentalities immunity from suit in U.S. courts unless a specific exception applies (e.g., the commercial activity exception). Exxon Mobil argues the Helms-Burton Act itself abrogates sovereign immunity for these claims, making a separate FSIA exception unnecessary. The Cuban defendants (Corporación Cimex and other state-owned companies) argue FSIA immunity remains intact as background law and must be independently satisfied [Court grapples with disputes over efforts to recover ... - SCOTUSblog](https://www.scotusblog.com/2026/02/court-grapples-with-disputes-over-efforts-to-recover-losses-from-cuban-confiscations/).

**Status as of May 12, 2026:** The Supreme Court granted certiorari on October 3, 2025, and heard oral arguments on February 23, 2026. During oral arguments, the Court appeared split: Justices Alito and Gorsuch expressed skepticism toward the FSIA immunity defense (favoring Exxon's position), while Justices Kagan, Sotomayor, and Jackson appeared sympathetic to the Cuban companies' argument that FSIA must be separately satisfied. Chief Justice Roberts, Justice Thomas, Justice Barrett, and Justice Kavanaugh were harder to read, making them potential swing votes [Court grapples with disputes over efforts to recover ... - SCOTUSblog](https://www.scotusblog.com/2026/02/court-grapples-with-disputes-over-efforts-to-recover-losses-from-cuban-confiscations/). A decision is expected by the end of the Court's October 2025 term, which traditionally concludes by late June 2026.

**Exact later resolution packet**

The question resolves YES.

On June 23, 2026 — within the required resolution window of May 12 to July 1, 2026 (inclusive) — the U.S. Supreme Court issued its opinion in Exxon Mobil Corp. v. Corporación Cimex, S.A. (No. 24-699). The Court held, in a 6-3 decision authored by Justice Brett Kavanaugh, that Title III of the Helms-Burton Act (Cuban Liberty and Democratic Solidarity Act of 1996) abrogates the foreign sovereign immunity of Cuban agencies and instrumentalities under the FSIA. As a result, Exxon Mobil need NOT independently satisfy a separate FSIA exception to proceed against the Cuban state-owned defendants [8905d2].

- The official slip opinion (https://www.supremecourt.gov/opinions/25pdf/24-699_f204.pdf) confirms the Court reversed the D.C. Circuit and remanded, holding the Helms-Burton Act itself abrogates FSIA immunity for these claims. The majority comprised Chief Justice Roberts and Justices Thomas, Alito, Gorsuch, Barrett, and Kavanaugh; Justice Kagan dissented, joined by Justices Sotomayor and Jackson [8905d2].
- SCOTUSblog's report ("Court rules for Exxon Mobil in Cuban confiscation case," June 23, 2026) confirms the same holding: writing for the majority, Justice Kavanaugh held the Helms-Burton Act abrogates FSIA immunity so that plaintiffs do not need to satisfy a separate FSIA exception [5c60b1].

This precisely matches the question's YES criteria: "the Supreme Court...holds that Title III of the Helms-Burton Act abrogates foreign sovereign immunity under the FSIA for the claims at issue — meaning Exxon Mobil need not independently satisfy a separate FSIA exception."

Checklist verification:
- Date within window (May 12 – July 1, 2026 inclusive): YES, decided June 23, 2026 [8905d2].
- Holding is specifically that Title III abrogates FSIA immunity (not a ruling based on a separate FSIA exception like commercial activity): YES [8905d2, 5c60b1].
- Not a DIG or procedural (standing/ripeness) disposition: correct — it was a merits ruling reversing the D.C. Circuit [8905d2].
- Official slip opinion URL: https://www.supremecourt.gov/opinions/25pdf/24-699_f204.pdf.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-85. `cf59bea6-ac3a-5950-9e4f-bdde52ce15df`

- Present date: `2026-04-30 17:52:43.349798`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the U.S. Senate confirm Arvind Raman as Director of the National Institute of Standards and Technology (NIST) by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the U.S. Senate votes to confirm Arvind Raman as Under Secretary of Commerce for Standards and Technology (i.e., [Director of the National Institute of Standards and Technology](https://www.nist.gov/director)) via a successful floor vote on or after April 30, 2026, and on or before June 1, 2026, 11:59 PM UTC.

This question resolves **No** if no such confirmation vote occurs, or if the vote fails, by June 1, 2026, 11:59 PM UTC.

"Confirmation" is defined as a successful majority floor vote in the U.S. Senate to approve the nomination, as recorded on the official Congress.gov nomination page: [https://www.congress.gov/nomination/119th-congress/730/54](https://www.congress.gov/nomination/119th-congress/730/54). If the "Actions" section of that page displays a "Confirmed by the Senate" entry with a date between April 30, 2026 and June 1, 2026 (inclusive), the question resolves Yes. Otherwise, it resolves No.

**Pre-cutoff background**

Arvind Raman, dean of engineering at Purdue University, was nominated by President Trump to serve as Under Secretary of Commerce for Standards and Technology, a position that also serves as Director of the [National Institute of Standards and Technology (NIST)](https://www.nist.gov/about-nist). NIST is a non-regulatory agency within the U.S. Department of Commerce that promotes innovation, industrial competitiveness, and oversees entities including the Center for AI Safety and Innovation (formerly the U.S. AI Safety Institute).

Raman testified at his confirmation hearing before the Senate Commerce, Science, and Transportation Committee on March 5, 2026 [NIST director nominee advances despite senators' MEP concerns](https://www.manufacturingdive.com/news/nist-director-nominee-arvind-raman-senate-confirmation/815356/). On March 12, 2026, the committee voted 16-12 (largely along party lines) to advance his nomination to the full Senate [NIST director nominee advances despite senators' MEP concerns](https://www.manufacturingdive.com/news/nist-director-nominee-arvind-raman-senate-confirmation/815356/). The nomination (PN730-54) was placed on the Senate Executive Calendar as Calendar No. 692 on that date [PN730-54 - Nomination of Arvind Raman for ... - Congress.gov](https://www.congress.gov/nomination/119th-congress/730/54).

As of April 30, 2026, Raman has not yet received a full Senate floor vote [PN730-54 - Nomination of Arvind Raman for ... - Congress.gov](https://www.congress.gov/nomination/119th-congress/730/54). His confirmation faced scrutiny over his stance on the Hollings Manufacturing Extension Partnership (MEP) and broader concerns about Commerce Department actions affecting NIST programs [NIST director nominee advances despite senators' MEP concerns](https://www.manufacturingdive.com/news/nist-director-nominee-arvind-raman-senate-confirmation/815356/). The agency is currently led by acting director Craig Burkhardt, who has held the position since January 2025 [NIST director nominee advances despite senators' MEP concerns](https://www.manufacturingdive.com/news/nist-director-nominee-arvind-raman-senate-confirmation/815356/). Senate floor scheduling is at the discretion of Senate leadership and can be delayed by competing priorities and procedural maneuvers.

**Exact later resolution packet**

The question resolves YES. The official Congress.gov nomination page for Arvind Raman (PN730-54) lists in its Actions section the entry: "05/18/2026 - Confirmed by the Senate by Yea-Nay Vote. 46 - 43. Record Vote Number: 125." [795947]. This is a successful majority floor vote by the full Senate (not merely a committee advancement), and the date of May 18, 2026 falls within the required resolution window of April 30, 2026 through June 1, 2026, 11:59 PM UTC (inclusive).

Supporting timeline from the Congress.gov Actions section [795947]:
- 05/12/2026: Motion to proceed agreed to; cloture motion presented.
- 05/14/2026: Cloture invoked (51-46, Record Vote 124).
- 05/18/2026: Considered and Confirmed by the Senate (46-43, Record Vote 125).

This is corroborated by multiple secondary sources reporting the Senate confirmed Raman as NIST Director and Under Secretary of Commerce for Standards and Technology (e.g., Purdue University newsroom, ANSI, MeriTalk, executivegov). The source URL used as the primary resolution source is https://www.congress.gov/nomination/119th-congress/730/54/actions.

Therefore, the "Confirmed by the Senate" entry exists with a date within the window, and the June 1, 2026 deadline was met, resolving the question YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-86. `84e716ac-125c-5b58-b2ab-ee7ebc630885`

- Present date: `2026-05-02 11:38:12.600644`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-05-16 00:00:00`

**Question**

Will the U.S. Senate Banking Committee complete its markup of the CLARITY Act (H.R. 3633) by May 15, 2026?

**Resolution criteria**

This question resolves as **Yes** if the U.S. Senate Committee on Banking, Housing, and Urban Affairs completes its [markup](https://www.senate.gov/about/glossary.htm) of H.R. 3633, the [Digital Asset Market Clarity Act of 2025 (CLARITY Act)](https://www.congress.gov/bill/119th-congress/house-bill/3633), between May 1, 2026, and 11:59 PM Eastern Time on May 15, 2026. It resolves **No** otherwise.

"Completes its markup" is defined as the committee voting to **order the bill to be reported** (favorably or with amendments) to the full Senate. This is the standard parliamentary indicator that a committee has concluded its markup of a bill. A markup that begins but does not conclude with such a vote by the deadline does not count.

**Verification sources** (in order of priority):
1. The [Congress.gov "All Actions" page for H.R. 3633](https://www.congress.gov/bill/119th-congress/house-bill/3633/all-actions), which will record the committee action if it occurs.
2. The [Senate Committee on Banking, Housing, and Urban Affairs website](https://www.banking.senate.gov/), specifically its hearings/markups schedule and press releases.
3. If neither official source is updated in time, consistent reporting from at least two major credible news outlets (e.g., Reuters, AP, Bloomberg, Politico) confirming the committee vote occurred.

**Pre-cutoff background**

The Digital Asset Market Clarity Act of 2025, known as the CLARITY Act ([H.R. 3633](https://www.congress.gov/bill/119th-congress/house-bill/3633)), is a bill establishing a regulatory framework for digital commodities. It passed the U.S. House of Representatives on July 17, 2025, by a bipartisan vote of 294–134 [https://www.congress.gov/bill/119th-congress/house-bill/3633/all-info](https://www.congress.gov/bill/119th-congress/house-bill/3633/all-info). On September 18, 2025, it was received in the Senate and referred to the Committee on Banking, Housing, and Urban Affairs, where it remains as of May 1, 2026, with no further actions recorded on Congress.gov [https://www.congress.gov/bill/119th-congress/house-bill/3633/all-info](https://www.congress.gov/bill/119th-congress/house-bill/3633/all-info).

Chairman Tim Scott initially announced a markup for January 15, 2026, but it was postponed. The committee missed a subsequent April 2026 target, largely because the committee calendar was consumed by the confirmation hearing for Federal Reserve chair nominee Kevin Warsh [CLARITY Act Misses April Deadline — What That Means For The ...](https://www.gfmreview.com/crypto/clarity-act-misses-april-deadline-what-that-means-for-the-industry). On April 27, 2026, the committee allowed April to close without scheduling a markup [CLARITY Act Misses April Deadline — What That Means For The ...](https://www.gfmreview.com/crypto/clarity-act-misses-april-deadline-what-that-means-for-the-industry).

Senator Cynthia Lummis has stated publicly that the committee intends to mark up the bill in May 2026, with the week of May 11 identified as the earliest likely window since the Senate is on recess prior to that date [CLARITY Act Markup Set For May, Says Senator Cynthia Lummis ...](https://stocktwits.com/news-articles/markets/cryptocurrency/clarity-act-markup-set-for-may-says-senator-cynthia-lummis-eyeing-finish-line-after-3-month-delay/cZBNU4aRePq). However, significant political and policy disagreements remain unresolved:

- **Stablecoin yields and rewards**: Senator Thom Tillis has requested additional time to review provisions on yield-bearing digital assets [CLARITY Act Markup Set For May, Says Senator Cynthia Lummis ...](https://stocktwits.com/news-articles/markets/cryptocurrency/clarity-act-markup-set-for-may-says-senator-cynthia-lummis-eyeing-finish-line-after-3-month-delay/cZBNU4aRePq).
- **CFTC staffing gaps**: Concerns about whether the CFTC has adequate resources to fulfill its expanded role under the bill [CLARITY Act Misses April Deadline — What That Means For The ...](https://www.gfmreview.com/crypto/clarity-act-misses-april-deadline-what-that-means-for-the-industry).
- **Iran-related crypto payment concerns**: National security implications of crypto transactions [CLARITY Act Misses April Deadline — What That Means For The ...](https://www.gfmreview.com/crypto/clarity-act-misses-april-deadline-what-that-means-for-the-industry).
- **Bank pushback**: Traditional banking institutions have raised objections to certain provisions [CLARITY Act Misses April Deadline — What That Means For The ...](https://www.gfmreview.com/crypto/clarity-act-misses-april-deadline-what-that-means-for-the-industry).
- **Prediction market politics**: Disputes over the treatment of prediction markets [CLARITY Act Misses April Deadline — What That Means For The ...](https://www.gfmreview.com/crypto/clarity-act-misses-april-deadline-what-that-means-for-the-industry).
- **48-hour review requirement**: The final text must be released for a mandatory 48-hour public review before any committee vote, and this text has not yet been released [CLARITY Act Misses April Deadline — What That Means For The ...](https://www.gfmreview.com/crypto/clarity-act-misses-april-deadline-what-that-means-for-the-industry).

The Senate is scheduled to begin its Memorial Day recess on May 21, 2026, creating a narrow window [CLARITY Act Misses April Deadline — What That Means For The ...](https://www.gfmreview.com/crypto/clarity-act-misses-april-deadline-what-that-means-for-the-industry). A May 15 deadline is uncertain given the compressed timeline and unresolved disagreements.

**Exact later resolution packet**

The question resolves YES. Under the stated criteria, a completed markup requires the Senate Committee on Banking, Housing, and Urban Affairs to vote to order H.R. 3633 reported to the full Senate by 11:59 PM ET on May 15, 2026. The highest-priority verification source, Congress.gov’s H.R. 3633 “All Actions” page (https://www.congress.gov/bill/119th-congress/house-bill/3633/all-actions), records that on May 14, 2026: “Committee on Banking, Housing, and Urban Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.” [Actions - H.R.3633 - 119th Congress (2025-2026): Digital Asset ...](https://www.congress.gov/bill/119th-congress/house-bill/3633/all-actions) May 14, 2026 falls within the required May 1–May 15, 2026 window, and “Ordered to be reported … favorably” is exactly the committee action specified in the resolution criteria as completing the markup. Therefore the correct resolution is YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-87. `a653ccb0-0617-5d42-b6c1-5d05e8b8fbb9`

- Present date: `2026-05-16 19:25:38.361614`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the U.S. Supreme Court rule in favor of the FCC (reversing the Fifth Circuit) in FCC v. AT&T, Inc. (No. 25-406) by June 30, 2026?

**Resolution criteria**

This question resolves **Yes** if, between May 12, 2026 and July 1, 2026 (11:59 PM Eastern Time), the U.S. Supreme Court issues an opinion in FCC v. AT&T, Inc. (No. 25-406) that **reverses** the Fifth Circuit's judgment—i.e., the Court holds that the FCC's forfeiture order process does not violate the Seventh Amendment or Article III, thereby upholding the FCC's authority to issue such orders. A "vacated and remanded" disposition also counts as **Yes** if the Court's opinion rejects the Fifth Circuit's core holding that the FCC's process violates the Seventh Amendment, even if the case is remanded on other grounds. A partial reversal that rejects the Seventh Amendment holding counts as Yes.

This question resolves **No** if:
- The Court affirms the Fifth Circuit's decision (upholding the carriers' Seventh Amendment claim), OR
- The Court dismisses the case as improvidently granted (DIG), which would leave the Fifth Circuit's judgment intact, OR
- No opinion is issued by July 1, 2026 at 11:59 PM Eastern Time.

**Primary resolution source:** The official Supreme Court docket page (https://www.supremecourt.gov/docket/docketfiles/html/public/25-406.html) and the Opinions of the Court page (https://www.supremecourt.gov/opinions/slipopinion/25). The disposition language in the Court's syllabus and opinion will determine resolution.

**Pre-cutoff background**

FCC v. AT&T, Inc. (No. 25-406), consolidated with Verizon Communications Inc. v. FCC (No. 25-567), is a case pending before the U.S. Supreme Court concerning whether the Federal Communications Commission's in-house process for imposing monetary forfeitures violates the Seventh Amendment right to a jury trial and Article III of the U.S. Constitution.

The case arose from an FCC investigation into AT&T's location-based services program, which led the FCC to impose a $57 million forfeiture order without a hearing or jury trial [Federal Communications Commission v. AT&T, Inc. - Ballotpedia](https://ballotpedia.org/Federal_Communications_Commission_v._AT%26T,_Inc.). The U.S. Court of Appeals for the Fifth Circuit vacated the FCC's forfeiture order, holding that the FCC's enforcement process—where the agency acts as prosecutor, judge, and jury—violated AT&T's Seventh Amendment and Article III rights [Federal Communications Commission v. AT&T, Inc. - Ballotpedia](https://ballotpedia.org/Federal_Communications_Commission_v._AT%26T,_Inc.). Other circuits (the Second and D.C. Circuits) have upheld similar FCC authority, creating a circuit split.

The Supreme Court heard oral arguments on April 21, 2026 [Court appears skeptical of right to jury trial in FCC proceedings](https://www.scotusblog.com/2026/04/court-appears-skeptical-of-right-to-jury-trial-in-fcc-proceedings/). At argument, several justices appeared skeptical of the carriers' Seventh Amendment claims. Chief Justice Roberts and Justices Barrett and Jackson suggested the forfeiture orders are non-binding—comparable to "parking tickets"—until the Department of Justice files a formal enforcement lawsuit, at which point a jury trial is available [Court appears skeptical of right to jury trial in FCC proceedings](https://www.scotusblog.com/2026/04/court-appears-skeptical-of-right-to-jury-trial-in-fcc-proceedings/). However, Justice Gorsuch expressed concern about the "domino problem," questioning the practical consequences for carriers who fail to pay assessed penalties [Court appears skeptical of right to jury trial in FCC proceedings](https://www.scotusblog.com/2026/04/court-appears-skeptical-of-right-to-jury-trial-in-fcc-proceedings/). The FCC argued its orders are non-binding until DOJ initiates enforcement proceedings, while the carriers contended the government effectively coerces payment [Court appears skeptical of right to jury trial in FCC proceedings](https://www.scotusblog.com/2026/04/court-appears-skeptical-of-right-to-jury-trial-in-fcc-proceedings/).

The case implicates the Court's 2024 decision in SEC v. Jarkesy, which held that the SEC's in-house adjudication of fraud penalties violated the Seventh Amendment. The carriers argue Jarkesy supports their position, while the FCC seeks to distinguish its non-binding forfeiture process.

As of May 13, 2026, the Court has not yet issued an opinion in this case [Docket for 25-406 - Supreme Court](https://www.supremecourt.gov/docket/docketfiles/html/public/25-406.html). The Supreme Court typically issues remaining opinions by late June or early July.

**Exact later resolution packet**

The question resolves YES.

Resolution window: May 12, 2026 – July 1, 2026 (11:59 PM ET). The Supreme Court issued its opinion on June 4, 2026, squarely within this window.

Disposition: The official Supreme Court docket for No. 25-406 records the June 4, 2026 entry: "Judgment REVERSED and case REMANDED. No. 25-567, adjudged to be affirmed. Roberts, C. J., delivered the opinion of the Court, in which Alito, Sotomayor, Kagan, Gorsuch, Kavanaugh, Barrett, and Jackson, JJ., joined. Thomas, J., filed a dissenting opinion." [Docket for 25-406 - Supreme Court](https://www.supremecourt.gov/docket/docketfiles/html/public/25-406.html) (https://www.supremecourt.gov/docket/docketfiles/html/public/25-406.html)

This is a REVERSAL of the Fifth Circuit's judgment in FCC v. AT&T (No. 25-406), which is exactly the condition the resolution criteria specify for YES ("reverses the Fifth Circuit's judgment—i.e., the Court holds that the FCC's forfeiture order process does not violate the Seventh Amendment or Article III").

Merits: The 8-1 majority (Chief Justice Roberts) held that it does not violate the Seventh Amendment for the FCC to issue forfeiture orders without a jury, because forfeiture orders under §503(b) do not definitively resolve the parties' legal obligations until DOJ brings a court enforcement action. This is confirmed by the slip opinion (https://www.supremecourt.gov/opinions/25pdf/25-406_nmip.pdf) and corroborated by SCOTUSblog ("Reversed and remanded, 8-1, in an opinion by John Roberts on Jun 4, 2026. Justice Thomas wrote a dissenting opinion."), the Congressional Research Service, the FCC's own release, and numerous law firm summaries (Mayer Brown, Faegre Drinker, Morgan Lewis, etc.), all dated June 4, 2026.

None of the NO conditions apply: the Court did not affirm the Fifth Circuit, did not dismiss as improvidently granted (DIG), and an opinion was issued before the July 1, 2026 deadline. The companion case No. 25-567 (Verizon) was "adjudged to be affirmed," but that concerns Verizon's petition; the core FCC v. AT&T judgment reversing the Fifth Circuit and rejecting the Seventh Amendment holding is what governs this question, and it resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-88. `4a605b39-ee84-5cc4-a585-ddef7a9d139f`

- Present date: `2026-05-03 10:53:57.002489`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will someone other than Jerome Powell be serving as Chair of the Federal Reserve Board of Governors as of June 1, 2026?

**Resolution criteria**

This question resolves YES if, as of 11:59 PM UTC on June 1, 2026, someone other than Jerome H. Powell is listed as "Chair" (or "Acting Chair" or "Chair Pro Tempore") of the Board of Governors of the Federal Reserve System on the official Federal Reserve Board Members page: https://www.federalreserve.gov/aboutthefed/bios/board/default.htm

This question resolves NO if Jerome H. Powell is still listed as "Chair" (including "Acting Chair" or "Chair Pro Tempore") on that page as of 11:59 PM UTC on June 1, 2026.

Key definitions:
- "Chair" refers to the Chair of the Board of Governors of the Federal Reserve System as defined under the Federal Reserve Act (https://www.federalreserve.gov/aboutthefed/fract.htm). This includes any person formally designated as Acting Chair or Chair Pro Tempore.
- An "Acting Chair" or "Chair Pro Tempore" designation for someone other than Powell DOES count as "someone other than Jerome Powell" for purposes of resolution.
- Only changes occurring on or after May 1, 2026 are relevant. If Powell had already been replaced before May 1, 2026 (hypothetically), that would not count.
- The resolution source is the Federal Reserve's official Board Members page at https://www.federalreserve.gov/aboutthefed/bios/board/default.htm, checked on or shortly after June 1, 2026. If that page is ambiguous or unavailable, credible news reporting (e.g., Reuters, AP, NYT) may be used as a secondary source.

**Pre-cutoff background**

Jerome Powell's current term as Chair of the Federal Reserve Board of Governors is scheduled to expire on May 15, 2026. President Trump has nominated Kevin Warsh to succeed Powell as Chair. On April 29, 2026, the Senate Banking Committee voted 13-11 along party lines to endorse Warsh's nomination, setting the stage for a full Senate confirmation vote [It's set to be Jerome Powell's last meeting as Fed chair - KASU.org](https://www.kasu.org/business-economy/2026-04-29/its-set-to-be-jerome-powells-last-meeting-as-fed-chair-as-trumps-pick-gets-a-green-light).

Powell has publicly stated he intends to remain on the Board of Governors even after his Chair term expires (his governor term runs until 2028). He has also indicated he would continue serving as acting Chair if Warsh has not been confirmed by May 15 [Who's in charge at the Fed after May 15? A new fight may be brewing.](https://www.washingtonpost.com/business/2026/04/14/trump-fed-acting-chairman-delay/). However, the Trump administration may challenge this, citing legal opinions from the Carter and Reagan administrations arguing the President—not the Fed—has authority to designate an acting chair when a successor has been nominated but not yet confirmed [Who's in charge at the Fed after May 15? A new fight may be brewing.](https://www.washingtonpost.com/business/2026/04/14/trump-fed-acting-chairman-delay/). There is speculation the administration could attempt to elevate another Fed board member to the role.

As of May 1, 2026, it remains uncertain whether: (1) Warsh will be confirmed by the full Senate before or shortly after May 15; (2) Powell will serve as acting chair in the interim; or (3) the administration will attempt to install a different acting chair. The next FOMC meeting is scheduled for June 2026 [It's set to be Jerome Powell's last meeting as Fed chair - KASU.org](https://www.kasu.org/business-economy/2026-04-29/its-set-to-be-jerome-powells-last-meeting-as-fed-chair-as-trumps-pick-gets-a-green-light).

**Exact later resolution packet**

The question resolves YES if, as of 11:59 PM UTC on June 1, 2026, someone other than Jerome H. Powell is listed as "Chair" (or "Acting Chair" or "Chair Pro Tempore") on the official Federal Reserve Board Members page (https://www.federalreserve.gov/aboutthefed/bios/board/default.htm).

Querying that exact official page returned its most recent state (last updated May 28, 2026), which lists "Kevin Warsh, Chairman" at the top of the board members list, while Jerome H. Powell is listed only as a member (not as Chair) [https://www.federalreserve.gov/aboutthefed/bios/board/default.htm](https://www.federalreserve.gov/aboutthefed/bios/board/default.htm).

Timeline corroborating this:
- Kevin Warsh was confirmed by the U.S. Senate on May 13, 2026 in a 54-45 vote (CNBC, BBC), then confirmed as a Board member on May 12 and as Chair (Federal Reserve press release other20260522a).
- Jerome H. Powell was named "chair pro tempore" by the Federal Reserve Board on May 15, 2026 and served in that acting capacity only from May 15 until Warsh was sworn in (Federal Reserve press release https://www.federalreserve.gov/newsevents/pressreleases/other20260515a.htm).
- Kevin Warsh took the oath of office as Chairman on May 22, 2026 (Federal Reserve press release https://www.federalreserve.gov/newsevents/pressreleases/other20260522a.htm; Wikipedia notes Powell served as acting chairman May 15–22, 2026).

Therefore, by June 1, 2026, Powell was no longer Chair (in any capacity); Kevin Warsh held the title of Chairman. This change occurred on May 22, 2026 — on or after the relevant May 1, 2026 cutoff. The official resolution source itself shows Warsh as Chairman and Powell merely as a member, satisfying the YES condition. Resolution: YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-89. `d6b23695-9cd2-5e95-9716-3a51e5d73e8b`

- Present date: `2026-05-03 03:03:44.672161`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will any U.S. state attorney general file a legal challenge to the DOJ's April 2026 marijuana rescheduling order by June 1, 2026?

**Resolution criteria**

This question resolves YES if at least one U.S. state attorney general (including the attorneys general of the 50 U.S. states and the District of Columbia, but excluding U.S. territories) files a legal challenge to the DOJ's April 23, 2026 marijuana rescheduling final order on or after May 1, 2026 (12:00 AM ET) and on or before June 1, 2026 (11:59 PM ET).

A "legal challenge" is defined as any of the following actions filed in a U.S. federal court:
- A lawsuit (complaint) seeking to vacate, enjoin, or otherwise block the order;
- A petition for review of the order filed in a U.S. Court of Appeals under the CSA's judicial review provisions (21 U.S.C. § 877);
- A motion for a temporary restraining order or preliminary injunction against enforcement of the order.

The challenge must be filed by or on behalf of a state attorney general's office (either individually or as part of a multi-state coalition). Challenges filed solely by private parties, industry groups, or other government officials do not count.

Resolution is determined by official court records available via PACER (https://pacer.uscourts.gov/), state attorney general office press releases, or credible news reporting from sources such as Reuters (https://www.reuters.com/), the Associated Press (https://apnews.com/), CNN (https://www.cnn.com/), or The New York Times (https://www.nytimes.com/).

**Pre-cutoff background**

On April 23, 2026, Acting U.S. Attorney General Todd Blanche signed a final order immediately rescheduling FDA-approved marijuana products and marijuana subject to qualifying state medical marijuana licenses from Schedule I to Schedule III of the Controlled Substances Act (CSA). This followed President Trump's December 18, 2025 executive order directing the Attorney General to expedite marijuana rescheduling. The DOJ also announced an expedited administrative hearing beginning June 29, 2026, to consider broader rescheduling of all marijuana.

The order has generated significant legal discussion. Legal commentators have noted the order will likely face legal challenges in federal court, with challengers potentially seeking a stay. Nebraska Attorney General Mike Hilgers has publicly spoken against marijuana rescheduling. State attorneys general have a well-established pattern of forming coalitions to challenge federal executive actions, and opposition could come from states with strict anti-marijuana policies. However, the rescheduling enjoys bipartisan support, and the order was narrowly tailored to FDA-approved products and state-licensed medical marijuana rather than broad legalization.

As of May 1, 2026, no state attorney general has publicly announced filing a legal challenge to the order.

**Exact later resolution packet**

The question resolves YES.

The question asks whether at least one U.S. state attorney general filed a legal challenge to the DOJ's April 23, 2026 marijuana rescheduling final order between May 1, 2026 (12:00 AM ET) and June 1, 2026 (11:59 PM ET).

Evidence: On May 22, 2026, the attorneys general of Nebraska, Indiana, and Louisiana filed a 15-page petition for review in the U.S. Court of Appeals for the District of Columbia Circuit, naming Acting Attorney General Todd Blanche and DEA Administrator Terrance Cole as respondents [3 States Challenge Trump DOJ's Schedule III Cannabis Rule](https://www.cannabisbusinesstimes.com/cannabis-rescheduling/news/15826182/3-states-challenge-trump-dojs-schedule-iii-cannabis-rule). This is corroborated by Marijuana Moment, which reported three Republican state attorneys general filed a lawsuit challenging the rescheduling action in the D.C. Circuit [State Attorneys General File Lawsuit To Block Trump ...](https://www.marijuanamoment.net/state-attorneys-general-file-lawsuit-to-block-trump-administrations-marijuana-rescheduling-move/), and by Nebraska Public Media, which reported the Nebraska, Indiana, and Louisiana AGs filed the suit headed into Memorial Day weekend (Memorial Day 2026 was May 25) [Nebraska, Indiana and Louisiana AGs sue to stop Trump admin ...](https://nebraskapublicmedia.org/en/news/news-articles/nebraska-indiana-and-louisiana-ags-sue-to-stop-trump-admin-marijuana-reclassification/).

Checklist verification:
- Timing: Filed May 22, 2026, which falls within the required window of May 1–June 1, 2026 [3 States Challenge Trump DOJ's Schedule III Cannabis Rule](https://www.cannabisbusinesstimes.com/cannabis-rescheduling/news/15826182/3-states-challenge-trump-dojs-schedule-iii-cannabis-rule).
- Filed by state AGs: Filed by the attorneys general of Nebraska, Indiana, and Louisiana — three of the 50 U.S. states, none being U.S. territories [3 States Challenge Trump DOJ's Schedule III Cannabis Rule](https://www.cannabisbusinesstimes.com/cannabis-rescheduling/news/15826182/3-states-challenge-trump-dojs-schedule-iii-cannabis-rule) [Nebraska, Indiana and Louisiana AGs sue to stop Trump admin ...](https://nebraskapublicmedia.org/en/news/news-articles/nebraska-indiana-and-louisiana-ags-sue-to-stop-trump-admin-marijuana-reclassification/).
- Target: Specifically challenges the DOJ's April 23, 2026 rescheduling order (FDA-approved products and state-licensed medical marijuana to Schedule III), naming Blanche and Cole as respondents [3 States Challenge Trump DOJ's Schedule III Cannabis Rule](https://www.cannabisbusinesstimes.com/cannabis-rescheduling/news/15826182/3-states-challenge-trump-dojs-schedule-iii-cannabis-rule).
- Type of action: A petition for review filed in a U.S. Court of Appeals (D.C. Circuit) under the CSA's judicial review provisions (21 U.S.C. § 877), which is one of the explicitly allowed forms of "legal challenge" in the resolution criteria [3 States Challenge Trump DOJ's Schedule III Cannabis Rule](https://www.cannabisbusinesstimes.com/cannabis-rescheduling/news/15826182/3-states-challenge-trump-dojs-schedule-iii-cannabis-rule).

All resolution criteria are satisfied, so the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-90. `75e58d45-3a3a-5c36-8777-9665b2b891f6`

- Present date: `2026-05-15 13:19:37.148951`
- Source cutoff boundary: `2026-05-16` (encodes end of UTC day `2026-05-15`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the South Korean Constitutional Court accept a constitutional complaint against the Prosecution Office Act or Serious Crimes Investigation Office Act for merits review by July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 12, 2026 (00:00 KST) and before July 2, 2026 (00:00 KST), the South Korean Constitutional Court officially announces that it has accepted a constitutional complaint (헌법소원심판) or request for constitutional review (위헌법률심판) regarding the Prosecution Office Act (검찰청법) or the Serious Crimes Investigation Office Act (중대범죪수사청법) for merits review.

"Acceptance for merits review" is defined as the complaint or request passing the designated three-justice panel's preliminary review (사전심사) and being formally transferred to the full bench (전원재판부) for substantive adjudication, as described in the Constitutional Court Act (헌법재판소법).

This question resolves as **No** if no such acceptance is officially announced by 23:59 KST on July 1, 2026.

**Resolution source:** Official announcements on the Constitutional Court of Korea's website (https://www.ccourt.go.kr), or credible reporting from major Korean news outlets such as Yonhap News Agency (https://en.yna.co.kr), The Korea Herald (https://www.koreaherald.com), or Korea JoongAng Daily (https://koreajoongangdaily.joins.com).

**Pre-cutoff background**

On March 20, 2026, South Korea's National Assembly passed legislation stripping prosecutors of their direct investigative powers, creating a new Public Prosecution Office focused solely on indictments and establishing a Serious Crimes Investigation Office under the Minister of the Interior and Safety. The laws were promulgated on March 24, 2026 (KST).

On April 22, 2026 (KST), the Constitutional Court of Korea dismissed a constitutional complaint filed by Professor Lee Ho-seon challenging both the Prosecution Office Act and the Serious Crimes Investigation Office Act. The dismissal was on procedural grounds — the Court did not reach the merits of whether the laws violate the Constitution [Constitutional Court dismisses challenge to Korea's prosecution and ...](https://biz.chosun.com/en/en-society/2026/04/22/UCK2YX53XFCQ5HWFPUYNYSXRY4/). The legal dispute remains active, with conservative legal groups and political opponents expected to file new complaints with stronger procedural standing.

Under the Constitutional Court Act, constitutional complaints undergo a preliminary review by a designated three-justice panel before being transferred to the full nine-justice bench for merits review. "Acceptance for merits review" in this context means that a complaint survives the designated panel's preliminary screening and is formally referred to the full bench for substantive adjudication.

As of May 13, 2026, no subsequent complaint on these laws is known to have been accepted for merits review. The Constitutional Court has been experiencing a surge in filings following the March 2026 judicial reform, which may affect processing timelines.

**Exact later resolution packet**

RESOLUTION: YES (1).

WHAT HAPPENED: On June 30, 2026 (KST), the Constitutional Court of Korea's designated three-justice panel (지정재판부) formally referred to full-bench merits review (정식심판 회부 = 전원재판부 회부) a constitutional complaint (헌법소원심판) challenging the Public Prosecution Office Act (공소청법). The complaint was filed on June 17, 2026 by Kim Seong-dong (김성동), the chief of the inspection department at the Supreme Prosecutors' Office (대검 감찰부장), against the addendum provision (부칙 제7조 제1항) that excludes fixed-term prosecutors from being transitioned into the new Public Prosecution Office — arguing it violates separation of powers, equality, and trust-protection principles. This "referral to formal review" is exactly the Constitutional Court Act mechanism defined in the question: passing the three-justice preliminary screening (사전심사) and being transferred to the full bench (전원재판부) for substantive adjudication.

- Newsis reported the panel decided on June 30, 2026 to refer the complaint to the full bench for merits review ["공소청법 위헌"…대검 감찰부장 헌법소원, 헌재 정식심리 회부 - 뉴시스](https://www.newsis.com/view/NISX20260630_0003690086).
- Segye Ilbo (via Daum) confirmed the June 30, 2026 referral of the same 공소청법 addendum complaint to formal adjudication [대검 감찰부장의 '공소청법 위헌' 헌법소원, 정식심판 회부 - Daum](https://v.daum.net/v/20260630175816462?f=p).
- Yonhap News TV confirmed the designated panel's referral to formal/merits review, with the decision made on June 30, 2026 [대검 감찰부장이 낸 공소청법 헌법소원, 헌재 정식심판 회부](https://www.yonhapnewstv.co.kr/news/MYH20260701060023LQA).
- Seoul Economic Daily (English) confirmed the designated three-justice panel referred Kim Sung-dong's complaint against the supplementary provision of the Public Prosecution (Service) Act to the full bench for merits review, reported June 30, 2026 [Prosecution Watchdog Chief's Constitutional Complaint Clears ...](https://en.sedaily.com/society/2026/06/30/prosecution-watchdog-chiefs-constitutional-complaint-clears).

TIMING (KST): The referral decision was made on June 30, 2026 KST — after May 12, 2026 00:00 KST and before July 2, 2026 00:00 KST. It therefore falls squarely within the resolution window. (A Yonhap News TV broadcast timestamp of July 1 refers to the airing time; the court's decision itself was June 30, per "헌재 지정재판부는 30일" in the reporting [대검 감찰부장이 낸 공소청법 헌법소원, 헌재 정식심판 회부](https://www.yonhapnewstv.co.kr/news/MYH20260701060023LQA)[대검 감찰부장의 '공소청법 위헌' 헌법소원, 정식심판 회부 - Daum](https://v.daum.net/v/20260630175816462?f=p).)

TERMINOLOGY NOTE (검찰청법 vs 공소청법): The question's English label "Prosecution Office Act" corresponds to the Public Prosecution Office Act (공소청법), the March 2026 reform law creating the new Public Prosecution Office (공소청) described in the question's own background. The Korean parenthetical "검찰청법" in the resolution criteria is a mislabel by the question author; the clear intent is the prosecution-reform statute. This is confirmed because the question describes the earlier April 22, 2026 dismissed complaint by Professor Lee Ho-seon as targeting "both the Prosecution Office Act and the Serious Crimes Investigation Office Act," which Korean media uniformly reported as 공소청법·중수청법. Thus a 헌법소원 against 공소청법 unambiguously satisfies the criterion.

CONCLUSION: An officially announced acceptance for merits review of a constitutional complaint regarding the Prosecution Office Act (공소청법) occurred on June 30, 2026 KST — within the window — so the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-91. `8042e84d-abd1-5dd7-ae5f-c794cb342f5b`

- Present date: `2026-05-12 19:03:17.855177`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Troy Jackson or Hannah Pingree finish ahead of Shenna Bellows in the 2026 Maine Democratic gubernatorial primary?

**Resolution criteria**

This question resolves based on the final official results of the Maine Democratic gubernatorial primary held on June 9, 2026 (ET), as published by the Maine Secretary of State at https://www.maine.gov/sos/elections-voting/election-results-data [Election Results/Data | SOS - Maine.gov](https://www.maine.gov/sos/elections-voting/election-results-data).

"Finish ahead of" is defined as follows: a candidate finishes ahead of another if they are eliminated in a later round of the RCV tabulation, or if they win the election. In Maine's RCV system (explained at https://en.wikipedia.org/wiki/Instant-runoff_voting), candidates are sequentially eliminated from last place; a candidate eliminated in Round 4 finishes ahead of a candidate eliminated in Round 3.

This question resolves **Yes** if, in the official round-by-round RCV tabulation, either Troy Jackson or Hannah Pingree (or both) finishes ahead of Shenna Bellows — i.e., Bellows is eliminated in an earlier round than at least one of Jackson or Pingree, or at least one of Jackson/Pingree wins the primary while Bellows does not.

This question resolves **No** if Shenna Bellows finishes ahead of both Troy Jackson and Hannah Pingree — i.e., both Jackson and Pingree are eliminated in earlier rounds than Bellows.

If any of the three candidates (Jackson, Bellows, Pingree) do not appear on the June 9, 2026 primary ballot, this question resolves **No**.

**Pre-cutoff background**

The 2026 Maine Democratic gubernatorial primary is scheduled for June 9, 2026. Maine uses Ranked Choice Voting (RCV) for primary elections, a system in which voters rank candidates by preference; if no candidate wins a majority of first-choice votes, the last-place candidate is eliminated and their votes are redistributed according to voters' next preferences, repeating until one candidate achieves a majority (see: https://en.wikipedia.org/wiki/Instant-runoff_voting).

The Democratic field includes several candidates, among them Troy Jackson, Shenna Bellows, and Hannah Pingree [2026 Maine gubernatorial election - Wikipedia](https://en.wikipedia.org/wiki/2026_Maine_gubernatorial_election). A March 2026 poll showed these three tightly clustered: Troy Jackson at 18%, Shenna Bellows at 17%, and Hannah Pingree at 16%. This near-three-way tie among the non-frontrunner tier makes their relative finishing order highly uncertain and sensitive to endorsements, campaign strategy, and RCV transfer dynamics.

Official round-by-round RCV results will be published by the Maine Secretary of State at https://www.maine.gov/sos/elections-voting/election-results-data [Election Results/Data | SOS - Maine.gov](https://www.maine.gov/sos/elections-voting/election-results-data).

**Exact later resolution packet**

RESOLUTION: YES (1).

The question asks whether Troy Jackson OR Hannah Pingree finished ahead of Shenna Bellows in the 2026 Maine Democratic gubernatorial primary (June 9, 2026), per the official Maine Secretary of State RCV tabulation.

BALLOT PRESENCE (threshold condition): All three named candidates — Shenna Bellows, Troy Jackson, and Hannah Pingree — appeared on the June 9, 2026 Democratic primary ballot. Five Democrats qualified: Shenna Bellows, Troy Jackson, Angus King III, Hannah Pingree, and Nirav Shah (confirmed across sources). So the "resolves NO if any of the three didn't appear" clause is NOT triggered.

OFFICIAL RCV TABULATION (round-by-round): Per the Maine Secretary of State's announcement of the completed ranked-choice tabulations, the Democratic Governor primary elimination order was: Round 1 — Angus King III eliminated; Round 2 — Shenna Bellows eliminated; Round 3 — Troy Jackson eliminated; final round — Hannah Pingree defeated Nirav Shah to win the nomination [Maine Secretary of State's Office announces ranked choice ...](https://www.maine.gov/sos/news/maine-secretary-states-office-announces-ranked-choice-tabulations) [Maine Secretary of State's Office announces ranked choice ...](https://www.maine.gov/sos/news/maine-secretary-states-office-announces-ranked-choice-tabulations). Maine Morning Star's report of the official tally likewise lists King eliminated first, then Bellows, then Jackson, with Pingree winning [Pingree clinches Democratic nomination for governor after lengthy ...](https://mainemorningstar.com/2026/06/19/pingree-clinches-democratic-nomination-for-governor-after-lengthy-ranked-choice-tally/). WMTW's report of the Secretary of State results gives the finishing order: Pingree (winner), Shah (2nd), Jackson (3rd), Bellows (4th), King (5th) [Ranked choice results for Maine gubernatorial primaries ... - WMTW](https://www.wmtw.com/article/maine-primary-ranked-choice-voting-results-governor-cd2/71631039). FairVote confirms Pingree won a come-from-behind victory over Shah (~56%) on transfers from Bellows/Jackson/King voters [Maine releases ranked choice voting primary results - FairVote](https://fairvote.org/maine-releases-ranked-choice-voting-primary-results/).

APPLYING THE CRITERIA:
- Hannah Pingree WON the primary while Bellows did not → Pingree finished ahead of Bellows. This alone satisfies the YES condition.
- Additionally, Troy Jackson was eliminated in Round 3, a LATER round than Bellows (Round 2) → Jackson also finished ahead of Bellows.
Both independent YES conditions are met; the NO condition (Bellows ahead of BOTH Jackson and Pingree) is false.

OFFICIAL SOURCE / URL: Maine Secretary of State — "Maine Secretary of State's Office announces ranked choice tabulations" (https://www.maine.gov/sos/news/maine-secretary-states-office-announces-ranked-choice-tabulations), linked from the required results page https://www.maine.gov/sos/elections-voting/election-results-data [Maine Secretary of State's Office announces ranked choice ...](https://www.maine.gov/sos/news/maine-secretary-states-office-announces-ranked-choice-tabulations) [Maine Secretary of State's Office announces ranked choice ...](https://www.maine.gov/sos/news/maine-secretary-states-office-announces-ranked-choice-tabulations).

NOTE ON A DISCREPANCY: One automated extraction of the dynamic SOS election-results-data page erroneously claimed Bellows won [https://www.maine.gov/sos/elections-voting/election-results-data](https://www.maine.gov/sos/elections-voting/election-results-data); this is contradicted by the official SOS tabulation announcement, WMTW's official-results report, Maine Morning Star, and FairVote, all of which agree Pingree won and Bellows was eliminated in Round 2. That single reading is an extraction error and is overwhelmingly outweighed.

Conclusion: The question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-92. `6eb48c32-a4a6-5b5d-aa5d-3b42a1901d38`

- Present date: `2026-05-02 21:08:27.357222`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the U.S. announce any new tariff exemptions or reductions specifically for Mexican goods between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 1, 2026, and on or before June 1, 2026 (11:59 PM UTC), any of the following U.S. government entities — the Office of the United States Trade Representative (USTR), the Department of Commerce, the White House, or U.S. Customs and Border Protection — officially announces a new tariff exemption or reduction specifically applicable to Mexican goods, relative to the tariff rates in effect on May 1, 2026.

**Definitions:**

- **"Mexican goods"**: Goods originating in Mexico as classified by U.S. Customs and Border Protection (CBP) or under USMCA rules of origin, per [19 CFR Part 182](https://www.ecfr.gov/current/title-19/chapter-I/part-182).

- **"Tariff exemptions or reductions"**: A formal policy change — announced via Executive Order, Presidential Proclamation, Federal Register notice, or official press release — that lowers the effective tariff rate or grants an exemption for one or more of the following: (a) broad product categories (e.g., all automotive parts), (b) specific Harmonized System (HS) code classifications, or (c) individual company-level exclusions (e.g., product exclusion processes similar to those used under prior Section 232 or Section 301 tariff programs). This includes partial reductions (e.g., lowering the auto tariff from 25% to 15%) and targeted exclusions. It does **not** include: continuation of existing USMCA duty-free treatment already in effect as of May 1, 2026; temporary customs processing delays or enforcement discretion; or informal statements of intent without a formal policy instrument.

- **"Official announcement"**: A document or statement published on an official U.S. government domain, including but not limited to [ustr.gov](https://ustr.gov), [whitehouse.gov](https://www.whitehouse.gov), [commerce.gov](https://www.commerce.gov), [federalregister.gov](https://www.federalregister.gov), or [cbp.gov](https://www.cbp.gov). Alternatively, if the announcement is reported by at least two of the following credible news outlets — [Reuters](https://www.reuters.com), [Associated Press](https://apnews.com), [The Wall Street Journal](https://www.wsj.com), [The New York Times](https://www.nytimes.com) — citing official U.S. government sources, that also suffices.

If no qualifying announcement is made by 11:59 PM UTC on June 1, 2026, this question resolves **No**.

**Pre-cutoff background**

As of May 1, 2026, the United States maintains several layers of tariffs on goods imported from Mexico [US Import Tariff Tracker - Current Rates & Status | Zonos Docs](https://zonos.com/docs/guides/us-tariff-changes):

- **25% tariff on automobiles and automobile parts** (global, under Section 232 of the Trade Expansion Act of 1962) [https://www.reuters.com/business/autos-transportation/us-trade-rep-tells-mexican-companies-trump-tariffs-here-stay-sources-say-2026-04-21/](https://www.reuters.com/business/autos-transportation/us-trade-rep-tells-mexican-companies-trump-tariffs-here-stay-sources-say-2026-04-21/)
- **50% tariff on steel and aluminum** (global, under Section 232; 25% on derivative goods containing at least 15% of the metals by weight) [https://www.reuters.com/business/autos-transportation/us-trade-rep-tells-mexican-companies-trump-tariffs-here-stay-sources-say-2026-04-21/](https://www.reuters.com/business/autos-transportation/us-trade-rep-tells-mexican-companies-trump-tariffs-here-stay-sources-say-2026-04-21/)
- **10% Section 122 global surcharge** on most imports, though USMCA-compliant goods are exempt from this surcharge [US Import Tariff Tracker - Current Rates & Status | Zonos Docs](https://zonos.com/docs/guides/us-tariff-changes)

The previous IEEPA-based 25% tariff on Mexican goods ended on February 24, 2026 [US Import Tariff Tracker - Current Rates & Status | Zonos Docs](https://zonos.com/docs/guides/us-tariff-changes).

USTR Jamieson Greer stated on April 21, 2026, that tariffs are "here to stay" and that the U.S. will "never go back to a zero-tariff world," signaling a hardline stance [https://www.reuters.com/business/autos-transportation/us-trade-rep-tells-mexican-companies-trump-tariffs-here-stay-sources-say-2026-04-21/](https://www.reuters.com/business/autos-transportation/us-trade-rep-tells-mexican-companies-trump-tariffs-here-stay-sources-say-2026-04-21/). However, the USMCA joint review is approaching (July 1, 2026 deadline), and the first official U.S.-Mexico bilateral negotiating round is scheduled for the week of May 25, 2026, in Mexico City [U.S. Sets Talks with Mexico as USMCA Review Approaches](https://www.strtrade.com/trade-news-resources/str-trade-report/trade-report/april/u-s-sets-talks-with-mexico-as-usmca-review-approaches). Topics include rules of origin for key industrial goods, critical minerals, and bilateral trade irritants [U.S. Sets Talks with Mexico as USMCA Review Approaches](https://www.strtrade.com/trade-news-resources/str-trade-report/trade-report/april/u-s-sets-talks-with-mexico-as-usmca-review-approaches). These negotiations create a plausible window for targeted concessions despite the hardline rhetoric.

U.S. industries dependent on Mexican imports (particularly automotive and manufacturing) face significant cost pressures from the current tariff regime, creating lobbying incentives for exemptions.

**Exact later resolution packet**

Adjudicated: On June 1, 2026 (within the May 1-June 1 window) the White House issued the Presidential Proclamation 'Further Adjusting the Tariff Regimes for Imports of Aluminum, Steel, and Copper,' which specifically provides that for 'products of Canada and Mexico that qualify for preferential tariff treatment under the USMCA,' the 25% duty applies only to the non-U.S. content of the product (with a 15% floor). This is a new reduction specifically applicable to Mexican goods relative to the May 1 baseline set by the April 2 proclamation, which applied tariffs to the full customs value with no Mexico/USMCA carve-out (only UK and U.S.-origin metals were favored). It was a formal Presidential Proclamation on whitehouse.gov, satisfying the official-announcement and policy-instrument requirements, so the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-93. `de2d60ab-051f-5a69-8dfb-29a3fca92a6f`

- Present date: `2026-05-02 13:24:35.247848`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-05-28 00:00:00`

**Question**

Will Mayes Middleton win the Republican primary runoff for Texas Attorney General on May 26, 2026?

**Resolution criteria**

This question resolves YES if Mayes Middleton receives the majority of votes in the May 26, 2026 Texas Republican primary runoff for Attorney General, as reported by the Texas Secretary of State's official election results page (https://results.texas-election.com/). It resolves NO if Chip Roy receives the majority of votes.

If official results are not available by 11:59 PM UTC on June 1, 2026 (e.g., due to a recount or legal challenge), resolution will be deferred until official results are certified by the Texas Secretary of State. If the runoff is cancelled or does not take place by June 1, 2026, the question resolves NO.

**Pre-cutoff background**

The 2026 Texas Attorney General Republican primary runoff is scheduled for May 26, 2026, between State Senator Mayes Middleton (R-Galveston) and U.S. Representative Chip Roy (R-TX-21) [https://www.houstonpublicmedia.org/articles/news/politics/election-2026/2026/04/22/549723/christian-nationalism-texas-republican-primary-runoff-paxton-patrick-middleton-talarico/](https://www.houstonpublicmedia.org/articles/news/politics/election-2026/2026/04/22/549723/christian-nationalism-texas-republican-primary-runoff-paxton-patrick-middleton-talarico/). In the March 3, 2026 primary, Middleton and Roy were the top two finishers among four candidates, with no candidate receiving a majority. Middleton has heavily self-funded his campaign, contributing almost $14 million of his own money. He has championed Christian nationalist themes, including advocating for Ten Commandments displays in public schools [https://www.houstonpublicmedia.org/articles/news/politics/election-2026/2026/04/22/549723/christian-nationalism-texas-republican-primary-runoff-paxton-patrick-middleton-talarico/](https://www.houstonpublicmedia.org/articles/news/politics/election-2026/2026/04/22/549723/christian-nationalism-texas-republican-primary-runoff-paxton-patrick-middleton-talarico/). Roy, a sitting U.S. Congressman, brings federal experience and name recognition. The race has been described as contentious, with both candidates seeking to lead what has been called a key driver of the conservative legal movement. Aaron Reitz, a former primary rival, has endorsed Middleton. The winner will face the Democratic nominee in the November 3, 2026 general election.

**Exact later resolution packet**

The resolution criteria require using the Texas Secretary of State official election results page; the relevant page I used is the Secretary of State Election Results page for Tuesday, May 26, 2026: https://electionresults.sos.state.tx.us/results.html, which the queried official page identifies as the 2026 Republican Primary Runoff Election page [Election Results - Tuesday, May 26, 2026](https://electionresults.sos.state.tx.us/results.html) [Election Results - Tuesday, May 26, 2026](https://electionresults.sos.state.tx.us/results.html). The page reports an Attorney General Republican runoff contest with Mayes Middleton receiving 755,593 votes and Chip Roy receiving 612,171 votes [Election Results - Tuesday, May 26, 2026](https://electionresults.sos.state.tx.us/results.html) [Election Results - Tuesday, May 26, 2026](https://electionresults.sos.state.tx.us/results.html). The total of those two candidates' votes is 1,367,764, so Middleton's share is 755,593 / 1,367,764 = 55.24%, while Roy's share is 44.76%; Middleton therefore received a majority, not merely a plurality [Election Results - Tuesday, May 26, 2026](https://electionresults.sos.state.tx.us/results.html) [Election Results - Tuesday, May 26, 2026](https://electionresults.sos.state.tx.us/results.html). The same official page identifies the election date as Tuesday, May 26, 2026, lists the 2026 Republican Primary Runoff Election, and reports 100% of polling locations reporting, which shows the runoff took place rather than being cancelled or not taking place by June 1, 2026 [Election Results - Tuesday, May 26, 2026](https://electionresults.sos.state.tx.us/results.html). The page's update timestamp is 05/27/2026 09:20 AM, so the official results page had the relevant results available before 11:59 PM UTC on June 1, 2026; although the page did not explicitly use the word "certified," it was the required official Texas Secretary of State results source and had complete 100% reporting [Election Results - Tuesday, May 26, 2026](https://electionresults.sos.state.tx.us/results.html). Therefore, under the stated criteria, the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-94. `8b63881a-0edd-5ead-b3da-376fc18e2ddf`

- Present date: `2026-04-30 12:36:01.934904`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Iran be listed as a participant in the 2026 FIFA World Cup on FIFA.com as of June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, as of 23:59 UTC on June 1, 2026, the Iran national football team (IR Iran) is listed as an active participating team on the official FIFA World Cup 2026 teams page at https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/teams or the equivalent tournament page on FIFA.com. "Listed as a participant" means Iran appears as a competing team in a group with scheduled or completed fixtures, without any notation indicating withdrawal, disqualification, or replacement by another team. If Iran is listed but with a caveat such as "suspended," "withdrawn," or "replaced," this resolves **No**.

If the FIFA.com page is inaccessible or does not clearly show the team list by 23:59 UTC on June 1, 2026, resolution may instead rely on official FIFA communications or credible reporting from major international news agencies (e.g., [Reuters](https://www.reuters.com), [AP News](https://apnews.com), [ESPN](https://www.espn.com)) confirming or denying Iran's active participation status in the tournament as of that date.

This question can resolve at any point between April 29, 2026 and June 1, 2026, based on the state of the FIFA.com listing or credible sources as of 23:59 UTC on June 1, 2026.

**Pre-cutoff background**

The 2026 FIFA World Cup is scheduled to be hosted by the United States, Mexico, and Canada, beginning June 11, 2026. Iran qualified for the tournament by topping its group in the third round of Asian qualification and is drawn into Group G with matches scheduled in the United States.

In March 2026, following the escalation of the U.S.-Iran conflict and the reported disappearance of Supreme Leader Ali Khamenei, Iranian sports minister Ahmad Donyamali announced that Iran would not participate in the World Cup [https://sports.yahoo.com/articles/2026-world-cup-iran-announces-141000146.html](https://sports.yahoo.com/articles/2026-world-cup-iran-announces-141000146.html). This was widely reported as an official withdrawal announcement on March 11, 2026 [https://sports.yahoo.com/articles/2026-world-cup-iran-announces-141000146.html](https://sports.yahoo.com/articles/2026-world-cup-iran-announces-141000146.html).

However, FIFA has not formally removed Iran from the tournament. FIFA President Gianni Infantino stated that Iran is "welcome" to compete and later said "The Iranian team is coming, for sure" [Is Iran in the World Cup? FIFA president says team 'coming for sure'](https://www.usatoday.com/story/sports/soccer/2026/04/16/iran-world-cup-2026-fifa/89641346007/) [https://www.espn.com/soccer/story/_/id/48174709/world-cup-2026-iran-iraq-travel-playoff-infantino-trump-fifa-explainer](https://www.espn.com/soccer/story/_/id/48174709/world-cup-2026-iran-iraq-travel-playoff-infantino-trump-fifa-explainer). FIFA indicated it was "monitoring" the situation and that no final decision needed to be made before the FIFA Congress on April 30, 2026 [https://www.espn.com/soccer/story/_/id/48174709/world-cup-2026-iran-iraq-travel-playoff-infantino-trump-fifa-explainer](https://www.espn.com/soccer/story/_/id/48174709/world-cup-2026-iran-iraq-travel-playoff-infantino-trump-fifa-explainer).

As of mid-April 2026, the situation has evolved further. Iran requested that FIFA relocate its group-stage matches from the United States to Mexico, citing security concerns. As of April 7, Iran was still awaiting FIFA's response, with Iran's final participation decision reportedly contingent on that response [Iran still awaiting FIFA response on World Cup venue switch - Reuters](https://www.reuters.com/sports/soccer/iran-awaiting-fifa-response-world-cup-venue-switch-2026-04-07/). By April 16, FIFA President Infantino reiterated that Iran would participate [Is Iran in the World Cup? FIFA president says team 'coming for sure'](https://www.usatoday.com/story/sports/soccer/2026/04/16/iran-world-cup-2026-fifa/89641346007/). On April 23, Iran's national team reportedly confirmed 2026 World Cup participation despite visa issues. On April 24, the U.S. State Department stated Iran can play but barred those with IRGC ties.

As of April 29, 2026, FIFA.com still lists Iran with fixtures for the tournament (https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/teams/ir-iran/fixtures). The FIFA Congress on April 30, 2026 may address Iran's status further, and the situation remains fluid given the volatile geopolitical environment.

**Exact later resolution packet**

The question resolves YES because Iran remained an active participating team in the 2026 FIFA World Cup through the resolution date of June 1, 2026, with no notation of withdrawal, disqualification, or replacement.

Key evidence:
- At the 76th FIFA Congress on April 30, 2026, FIFA President Gianni Infantino explicitly affirmed that Iran will participate in the World Cup and will play its matches in the United States. There was no decision to withdraw, suspend, or replace Iran with another team (e.g., Italy, which had been speculated as a potential replacement) [Infantino affirms at FIFA Congress that Iran will participate in World ...](https://apnews.com/article/world-cup-canada-fifa-congress-gianni-infantino-5580c8a59a11158f8c16059cea428169). This directly addresses the FIFA Congress outcome required by the checklist.
- Despite the Iranian sports minister's March 2026 "boycott"/non-participation rhetoric, no official withdrawal was ever submitted to FIFA, and FIFA never formally removed Iran. FIFA repeatedly affirmed Iran's "coming for sure" status.
- Iran's request to relocate matters: the "venue switch" / "security concerns" issue resolved into a base-camp relocation, NOT a withdrawal or replacement. As of late May 2026 (BBC, May 24, 2026), Iran's federation president Mehdi Taj announced FIFA had approved switching Iran's training base from Tucson, Arizona, to Tijuana, Mexico, while Iran remained scheduled to play its group-stage matches against New Zealand, Belgium, and Egypt. The article details ongoing preparations (training camp in Turkey, visa applications) for the tournament beginning June 11, 2026, with no indication Iran was withdrawn, disqualified, or replaced [Iran says World Cup base moved to Mexico from US - BBC](https://www.bbc.com/sport/football/articles/cx21e47e214o). This confirms Iran's active participant status persisted well past June 1, 2026.

Therefore, as of 23:59 UTC on June 1, 2026, Iran was listed/recognized as an active competing team in its group with scheduled fixtures, satisfying the YES criteria.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-95. `a7698b19-7df7-5ddf-8366-756fd5db4df3`

- Present date: `2026-05-14 01:33:48.433696`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-20T00:00:00`

**Question**

Will Keiko Fujimori win the 2026 Peruvian presidential runoff election on June 7, 2026?

**Resolution criteria**

This question resolves **Yes** if Keiko Fujimori obtains the most valid votes in the 2026 Peruvian presidential runoff election held on June 7, 2026 (Peru Time, PET / UTC−5), according to the official count published by the National Office of Electoral Processes (ONPE) at https://resultadoelectoral.onpe.gob.pe/.

This question resolves **No** if Roberto Sánchez obtains the most valid votes, or if the runoff election does not take place by June 14, 2026 (PET).

Resolution is based solely on the official vote count from ONPE. Any legal challenges, appeals, or annulment proceedings filed after the official count is published are excluded from consideration unless they are fully resolved by the National Jury of Elections (JNE) before July 1, 2026 (PET), in which case the JNE's final determination governs.

If ONPE has not published official results by June 30, 2026 (PET), resolution will be based on ONPE's most recent preliminary results available at that time.

**Pre-cutoff background**

Peru held its first-round general elections on April 12–13, 2026. Keiko Fujimori of Popular Force (Fuerza Popular) placed first with 17.14% of the vote, while Roberto Sánchez of Together for Peru (Juntos por el Perú) placed second with 12.04% [https://en.wikipedia.org/wiki/2026_Peruvian_general_election](https://en.wikipedia.org/wiki/2026_Peruvian_general_election). A runoff election between these two candidates is scheduled for June 7, 2026 [https://en.wikipedia.org/wiki/2026_Peruvian_general_election](https://en.wikipedia.org/wiki/2026_Peruvian_general_election).

Recent polling shows an extremely tight race. An IEP/La República poll conducted April 21–25, 2026 showed Sánchez at 50.8% vs. Fujimori at 49.2%. An Ipsos Perú/Perú21 poll conducted April 23–24, 2026 showed a 50–50 tie [https://en.wikipedia.org/wiki/Opinion_polling_for_the_2026_Peruvian_general_election](https://en.wikipedia.org/wiki/Opinion_polling_for_the_2026_Peruvian_general_election). The race is within the margin of error in all recent polls.

Fujimori has historically lost three consecutive presidential runoff elections (2011, 2016, 2021), making this her fourth attempt. The election takes place amid Peru's ongoing political instability, with multiple presidential removals in recent years [https://en.wikipedia.org/wiki/2026_Peruvian_general_election](https://en.wikipedia.org/wiki/2026_Peruvian_general_election).

The National Office of Electoral Processes (ONPE) is the official body responsible for managing the electoral process and tabulating results. Official results are published at https://resultadoelectoral.onpe.gob.pe/.

**Exact later resolution packet**

The question resolves YES because Keiko Fujimori obtained the most valid votes in the 2026 Peruvian presidential runoff.

Checklist against the resolution criteria:

1) Runoff took place on time: The runoff was held on June 7, 2026 — well before the June 14, 2026 cutoff. This is confirmed by the Wikipedia article on the 2026 Peruvian general election [https://en.wikipedia.org/wiki/2026_Peruvian_general_election](https://en.wikipedia.org/wiki/2026_Peruvian_general_election) [2026 Peruvian general election - Wikipedia](https://en.wikipedia.org/wiki/2026_Peruvian_general_election) and corroborated by contemporaneous reporting (Reuters, PBS, CGTN, Crisis Group). Therefore the NO condition ("runoff does not take place by June 14, 2026") was NOT triggered.

2) Winner by valid votes: According to the official ONPE count, Keiko Fujimori (Popular Force) obtained 9,223,396 valid votes (50.13% / 50.135%) versus Roberto Sánchez (Together for Peru) with 9,173,755 valid votes (49.87% / 49.865%). Fujimori won by a razor-thin margin of under 1%. These figures are reported on the Wikipedia page citing ONPE's second-round results page at https://resultadosegundavuelta.onpe.gob.pe/main/presidenciales [https://en.wikipedia.org/wiki/2026_Peruvian_general_election](https://en.wikipedia.org/wiki/2026_Peruvian_general_election) [2026 Peruvian general election - Wikipedia](https://en.wikipedia.org/wiki/2026_Peruvian_general_election), and the exact same totals (9,223,396 vs 9,173,755) were independently reported in news coverage (e.g., Instagram/press summaries citing the final results, and Le Monde, Bloomberg, DW, i24news, The Guardian all reporting Fujimori as the narrow winner).

3) JNE / official determination before July 1, 2026: The vote count was contested and reviewed for weeks. Peru's electoral authorities (electoral commission/JNE) declared Keiko Fujimori the winner around June 29–30, 2026, before the July 1, 2026 deadline. DW News reported "Peru's electoral commission declared Keiko Fujimori the winner of the presidential election," and prediction market Kalshi noted the outcome was "verified from National Jury of Elections (JNE)." The final determination therefore also supports Fujimori as winner — it does not overturn the ONPE count.

4) Official results available by June 30, 2026: Final official ONPE results were published (Fujimori 50.13%) before the June 30 deadline, as reflected in the Wikipedia article last updated 2026-07-01 [2026 Peruvian general election - Wikipedia](https://en.wikipedia.org/wiki/2026_Peruvian_general_election) and multiple June 29–30, 2026 news reports declaring her the winner.

Direct URL used to verify the vote counts: ONPE second-round presidential results page — https://resultadosegundavuelta.onpe.gob.pe/main/presidenciales (referenced on the Wikipedia article [https://en.wikipedia.org/wiki/2026_Peruvian_general_election](https://en.wikipedia.org/wiki/2026_Peruvian_general_election) [2026 Peruvian general election - Wikipedia](https://en.wikipedia.org/wiki/2026_Peruvian_general_election)).

Since Keiko Fujimori obtained the most valid votes per the official ONPE count, and this was upheld by the final electoral determination before July 1, 2026, the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-96. `910c18ab-33a5-560d-a068-1dafca5e6897`

- Present date: `2026-04-30 14:48:37.319384`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-05-31 00:00:00`

**Question**

Will GPT-Image-2 (ChatGPT Images 2.0) be ranked #1 on the LM Arena Image Generation leaderboard as of May 31, 2026?

**Resolution criteria**

This question resolves **Yes** if the model identified as GPT-Image-2 (also known as "ChatGPT Images 2.0," "gpt-image-2," or any variant name clearly attributable to OpenAI's GPT-Image-2 release) holds the sole #1 position (highest Elo score) on the LM Arena Image Generation leaderboard's overall text-to-image ranking at a snapshot taken at **23:59 UTC on May 31, 2026**.

The resolution source is the official LM Arena Image Generation leaderboard:
- Primary URL: https://lmarena.ai/leaderboard/image-generation
- Mirror: https://huggingface.co/spaces/lmarena-ai/arena-leaderboard

Specific resolution rules:
1. **Model identification:** The model must be clearly identified as OpenAI's GPT-Image-2 or a direct successor/renamed version of the same underlying model. If the leaderboard uses a technical name (e.g., "gpt-image-2," "GPT Image 2," "GPT Image 2.0," or similar), it qualifies as long as it corresponds to the same model released by OpenAI as "ChatGPT Images 2.0."
2. **Tie resolution:** If GPT-Image-2 is tied for #1 (i.e., shares the exact same Elo score with another model to the nearest integer), this resolves **No** — the model must hold the sole highest Elo score.
3. **Leaderboard unavailability:** If the LM Arena Image Generation leaderboard is offline or has not been updated for more than 14 consecutive days immediately preceding May 31, 2026, this question resolves **N/A** (ambiguous). If the leaderboard is temporarily offline on May 31 but was last updated within the prior 14 days, the most recent available snapshot before 23:59 UTC May 31 will be used.
4. **Category:** The "overall" or default text-to-image ranking is used. If no such default exists, the broadest available image generation category is used.

**Pre-cutoff background**

OpenAI released GPT-Image-2 (marketed as "ChatGPT Images 2.0") in April 2025. Within hours of launch, it reached the #1 spot on the LM Arena (formerly LMSYS Chatbot Arena) Image Generation leaderboard, scoring an Elo of approximately 1,512 on the text-to-image category — 242 points ahead of the second-place model [LM Arena Text-to-Image Rankings 2026 - WaveSpeed AI](https://wavespeed.ai/blog/posts/lm-arena-text-to-image-rankings-2026/). The leaderboard uses a crowdsourced blind pairwise comparison system where users vote on which model produces a better output, generating Elo ratings.

As of late April 2026, GPT-Image-2 remains highly ranked on the Image Arena leaderboard. However, the image generation space is extremely competitive, with Google (Gemini image models), Black Forest Labs (Flux 2 series), and others releasing frequent updates. A WaveSpeed AI analysis from late 2025 listed "GPT Image 1.5" at #1 with an Elo of 1264, followed by Gemini 3 Pro Image at 1235 [LM Arena Text-to-Image Rankings 2026 - WaveSpeed AI](https://wavespeed.ai/blog/posts/lm-arena-text-to-image-rankings-2026/), suggesting leaderboard positions have shifted over time and naming conventions may vary. More recent references indicate GPT-Image-2 currently holds the top position.

The leaderboard is publicly accessible at: https://lmarena.ai/leaderboard/image-generation (also mirrored at https://huggingface.co/spaces/lmarena-ai/arena-leaderboard).

**Exact later resolution packet**

YES. I resolved this using the broad/default text-to-image leaderboard snapshot at https://arena.ai/leaderboard/text-to-image, which the extracted page identifies as the Text-to-Image Arena leaderboard and gives a source/last-updated date of 2026-05-25 [Text-to-Image Leaderboard - Best AI Image Generators - Arena AI](https://arena.ai/leaderboard/text-to-image). That update date is within the required 14-day lookback before 2026-05-31, so the question is not annulled under the stale-leaderboard rule [Text-to-Image Leaderboard - Best AI Image Generators - Arena AI](https://arena.ai/leaderboard/text-to-image). On that snapshot, the #1 entry was “gpt-image-2 (medium)” with an Elo score of 1388, and the #2 entry was “gemini-3.1-flash-image-preview (nano-banana-2)” with an Elo score of 1271 [Text-to-Image Leaderboard - Best AI Image Generators - Arena AI](https://arena.ai/leaderboard/text-to-image). The model name “gpt-image-2 (medium)” is a direct variant of the qualifying GPT-Image-2 / gpt-image-2 name specified in the resolution criteria. Because 1388 is strictly higher than 1271, GPT-Image-2 held the sole highest Elo score rather than merely tying for #1 [Text-to-Image Leaderboard - Best AI Image Generators - Arena AI](https://arena.ai/leaderboard/text-to-image). Therefore the resolution criteria for YES are satisfied.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-97. `24fd6da5-881c-52a4-8ba1-072443ea34a3`

- Present date: `2026-05-07 22:33:58.056102`
- Source cutoff boundary: `2026-05-08` (encodes end of UTC day `2026-05-07`)
- Expected resolution: `2026-06-11T00:00:00`

**Question**

Will the European Central Bank raise any of its three key interest rates at the June 10-11, 2026 Governing Council meeting?

**Resolution criteria**

This question resolves **Yes** if the European Central Bank announces an increase to any of its three key interest rates—the deposit facility rate, the main refinancing operations rate, or the marginal lending facility rate—as a result of the Governing Council monetary policy meeting scheduled for June 10-11, 2026 (CEST).

This question resolves **No** if the ECB announces that all three key interest rates remain unchanged or are decreased following that meeting.

**Resolution source:** The official ECB "Monetary policy decisions" press release, published at 14:15 CEST on the meeting day, available at: https://www.ecb.europa.eu/press/govcdec/mopo/html/index.en.html [Monetary policy decisions - European Central Bank](https://www.ecb.europa.eu/press/govcdec/mopo/html/index.en.html). The specific press release will follow the URL pattern: https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp260611~[unique_id].en.html [Monetary policy decisions - European Central Bank](https://www.ecb.europa.eu/press/govcdec/mopo/html/index.en.html).

**Pre-cutoff background**

As of May 7, 2026, the European Central Bank's three key interest rates stand at: deposit facility rate 2.00%, main refinancing operations rate 2.15%, and marginal lending facility rate 2.40% [Monetary policy decisions - European Central Bank](https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp260430~81b7179e6f.en.html). The ECB has held rates unchanged throughout 2026 so far, but at its April 30, 2026 meeting, the Governing Council "extensively debated" a rate hike and signaled that a June increase is "firmly on the table" [ECB keeps rates unchanged but June hike firmly on table - Reuters](https://www.reuters.com/business/ecb-hold-rates-steady-keep-hikes-firmly-table-2026-04-29/).

The primary drivers of this potential policy shift are rising inflation—which hit 3% in April 2026, well above the ECB's 2% target—and the economic fallout from the ongoing Iran war, which has pushed oil prices to a four-year high and created industrial bottlenecks [ECB keeps rates unchanged but June hike firmly on table - Reuters](https://www.reuters.com/business/ecb-hold-rates-steady-keep-hikes-firmly-table-2026-04-29/). ECB policymakers have indicated that a June hike is likely unless a peace deal is reached and energy prices fall significantly. Bundesbank President Nagel has stated the ECB "may need to raise rates in June" unless the outlook improves markedly. Reuters sources report policymakers expect "at least two" rate hikes starting in June. Prediction markets (Polymarket) show approximately 77% probability of a 25 basis point hike in June. However, the outcome remains uncertain—a potential peace deal, energy price collapse, or deterioration in economic growth could alter the calculus [ECB keeps rates unchanged but June hike firmly on table - Reuters](https://www.reuters.com/business/ecb-hold-rates-steady-keep-hikes-firmly-table-2026-04-29/).

**Exact later resolution packet**

The question asks whether the ECB raised any of its three key interest rates at the June 10-11, 2026 Governing Council meeting. It resolves YES if an increase to any of the three rates (deposit facility, main refinancing operations, marginal lending facility) was announced as a result of that meeting.

RESOLUTION: YES.

The official ECB "Monetary policy decisions" press release, published 11 June 2026 at https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp260611~4d41bd5e83.en.html, states that the Governing Council decided to raise the three key ECB interest rates by 25 basis points. The new levels are: deposit facility rate 2.25% (up from 2.00%), main refinancing operations rate 2.40% (up from 2.15%), and marginal lending facility rate 2.65% (up from 2.40%), effective 17 June 2026 [7edad8].

This is an INCREASE to all three key rates, satisfying the YES condition (an increase to at least one of the three).

Corroboration:
- Reuters, "ECB raises interest rates in long-telegraphed move" (11 June 2026), reports the ECB increased the deposit rate to 2.25% and the refinancing rate to 2.40% as a result of the meeting [342989].
- Additional secondary sources confirm the hike: CNBC ("ECB hikes interest rates for first time since 2023") and Euronews ("ECB raises interest rates for the first time in three years... deposit facility rate by 0.25% to 2.25%"), and prediction markets (Polymarket/Kalshi) settled on "25 bps increase."

Note on a spurious data point: an initial query of the ECB index page (https://www.ecb.europa.eu/press/govcdec/mopo/html/index.en.html) returned an answer of "unchanged" but cited a URL ending in "81b7179e6f" — which is actually the identifier of the APRIL 30, 2026 press release (rates unchanged), not the June 11 release (whose real ID is "4d41bd5e83"). That was a confusion/hallucination between the April and June releases and is contradicted by the actual June 11 press release and all reputable news reporting [7edad8, 342989].

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-98. `9444f0a3-e659-545b-9140-ad18973f6d83`

- Present date: `2026-05-03 09:40:30.923984`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-05-27 00:00:00`

**Question**

Will Ken Paxton win the Texas Republican Senate primary runoff on May 26, 2026?

**Resolution criteria**

This question resolves YES if Ken Paxton receives the highest number of votes in the Texas Republican Senate primary runoff election held on May 26, 2026, according to official election results published by the Texas Secretary of State (https://www.sos.state.tx.us/elections/historical/index.shtml or https://electionresults.sos.state.tx.us/). It resolves NO if John Cornyn receives the highest number of votes.

The outcome is determined solely by the results of the runoff election occurring on or after April 30, 2026 (i.e., the May 26, 2026 runoff), not the earlier March 3 primary. All references to election day refer to May 26, 2026, Central Time (CT).

If the runoff is postponed beyond June 1, 2026, or if official results are not available by 11:59 PM CT on June 1, 2026, this question resolves based on the most authoritative unofficial tally available from the Texas Secretary of State at that time. If no results are available at all, the question resolves ambiguously (N/A).

**Pre-cutoff background**

The Texas Republican primary runoff for the U.S. Senate seat is scheduled for May 26, 2026. The race features incumbent U.S. Senator John Cornyn against Texas Attorney General Ken Paxton. Neither candidate secured a majority in the March 3, 2026 primary, triggering the runoff.

As of mid-April 2026, polling presents a competitive and uncertain picture. A poll conducted by Slingshot Strategies on behalf of the nonpartisan Texas Public Opinion Research (TPOR) shows Paxton leading Cornyn 48% to 40%, with 11% of voters undecided [https://www.houstonpublicmedia.org/articles/news/politics/election-2026/2026/04/17/549428/paxton-cornyn-poll-republican-primary-runoff-texas-senate-race/](https://www.houstonpublicmedia.org/articles/news/politics/election-2026/2026/04/17/549428/paxton-cornyn-poll-republican-primary-runoff-texas-senate-race/). A separate poll by the firm co/efficient reportedly shows Cornyn with a slight lead [https://www.houstonpublicmedia.org/articles/news/politics/election-2026/2026/04/17/549428/paxton-cornyn-poll-republican-primary-runoff-texas-senate-race/](https://www.houstonpublicmedia.org/articles/news/politics/election-2026/2026/04/17/549428/paxton-cornyn-poll-republican-primary-runoff-texas-senate-race/). The conflicting polls and significant undecided voter share make this a genuinely uncertain contest.

The official results will be published by the Texas Secretary of State on their election results page (https://electionresults.sos.state.tx.us/).

**Exact later resolution packet**

YES. The controlling source is the Texas Secretary of State election-results page at https://electionresults.sos.state.tx.us/results.html, queried for the May 26, 2026 Texas Republican U.S. Senate primary runoff. That official page is for “Election Results - Tuesday, May 26, 2026” and identifies the relevant contest under “2026 REPUBLICAN PRIMARY RUNOFF ELECTION,” not the earlier March 3, 2026 primary [Election Results - Tuesday, May 26, 2026](https://electionresults.sos.state.tx.us/results.html). In the U.S. Senator runoff, the Texas SOS page reported Ken Paxton with 885,949 votes and John Cornyn (incumbent) with 501,725 votes [Election Results - Tuesday, May 26, 2026](https://electionresults.sos.state.tx.us/results.html). Because Paxton’s vote total is higher than Cornyn’s, the resolution criterion for YES is met [Election Results - Tuesday, May 26, 2026](https://electionresults.sos.state.tx.us/results.html).

The runoff was not postponed beyond June 1, 2026: the official SOS page is specifically for the May 26, 2026 election and was already updated on 05/27/2026 at 09:20 AM, before the June 1, 2026 11:59 PM CT fallback deadline [Election Results - Tuesday, May 26, 2026](https://electionresults.sos.state.tx.us/results.html). Therefore it is unnecessary to use any unofficial fallback tally. The Texas SOS historical Election Results/Data page at https://www.sos.texas.gov/elections/historical/index.shtml also identifies the SOS official-results portal as the place for official election results, but the actual vote-count evidence used here comes from the May 26, 2026 SOS results page [Election Results/Data - the Texas Secretary of State](https://www.sos.texas.gov/elections/historical/index.shtml) [Election Results - Tuesday, May 26, 2026](https://electionresults.sos.state.tx.us/results.html).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-99. `a840a31b-b264-593d-bf08-d63125496da7`

- Present date: `2026-05-03 00:30:40.472133`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will CISA add a vulnerability in an AI-integrated software product to the Known Exploited Vulnerabilities (KEV) catalog between May 1, 2026, and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if at least one vulnerability associated with an "AI-integrated software product" (as defined below) is added to the [CISA Known Exploited Vulnerabilities (KEV) Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) with a "Date Added" value on or after May 1, 2026 (00:00 UTC) and on or before June 1, 2026 (23:59 UTC). Otherwise, it resolves **No**.

**Definition of "AI-integrated software product":** A software product whose primary purpose or widely recognized core functionality involves at least one of the following:

1. **LLM orchestration or chaining** — tools for building pipelines that connect large language models to data sources, APIs, or other models (e.g., [LangChain](https://en.wikipedia.org/wiki/LangChain), Flowise, LlamaIndex, Haystack, Semantic Kernel).
2. **AI agent frameworks** — platforms for building autonomous or semi-autonomous AI agents that take actions based on LLM reasoning (e.g., AutoGPT, CrewAI, AutoGen, BabyAGI).
3. **ML model serving and deployment platforms** — infrastructure specifically designed for deploying, serving, or managing machine learning or LLM models (e.g., MLflow, BentoML, Seldon Core, vLLM, Ollama, TensorFlow Serving).
4. **AI-native notebooks and development environments** — interactive development environments whose primary design purpose is AI/ML workflow development (e.g., Marimo, Jupyter with AI-specific extensions marketed as an AI product).
5. **AI-powered security or observability products** — products marketed primarily as using AI/ML for threat detection, response, or analysis (e.g., Darktrace, Vectra AI).

Products that merely *incorporate* AI features as an add-on (e.g., Microsoft Office with Copilot, Google Chrome with AI features) do **not** qualify. The product's primary function must be AI/ML-related as described above.

For reference on what constitutes AI infrastructure vulnerabilities, see the [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) and [NIST AI Risk Management Framework](https://www.nist.gov/artificial-intelligence/ai-risk-management-framework).

**Resolution source:** The official [CISA KEV Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) and its machine-readable feeds ([CSV](https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv), [JSON](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). The "vendorProject" and "product" fields in the catalog will be used to determine whether the affected product meets the definition above.

**Pre-cutoff background**

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) maintains the [Known Exploited Vulnerabilities (KEV) Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog), an authoritative, publicly accessible list of vulnerabilities confirmed to have been actively exploited in the wild. CISA adds new entries on a rolling basis, typically several per week.

As of May 1, 2026, the KEV catalog already contains at least two entries for AI-integrated software products: **Langflow** (an LLM orchestration framework) and **Marimo** (CVE-2026-39987, a reactive Python notebook used for AI/data science workflows) [Known Exploited Vulnerabilities Catalog | CISA](https://www.cisa.gov/known-exploited-vulnerabilities-catalog). The OWASP GenAI Exploit Round-up Report Q1 2026 has documented increasing real-world exploitation of AI infrastructure such as Flowise, indicating a trend of threat actors targeting AI-adjacent tools. The growing enterprise adoption of LLM orchestration tools, AI agent frameworks, and AI-powered security products makes it plausible—but not certain—that another such vulnerability will be added to the KEV catalog in any given month.

CISA typically adds 5–15 new vulnerabilities to the KEV catalog per week across all product categories. The subset involving AI-integrated products remains small but is growing.

**Exact later resolution packet**

The question resolves YES (1).

Resolution criteria: resolves YES if at least one vulnerability associated with an "AI-integrated software product" was added to the CISA KEV catalog with a "Date Added" on or after 2026-05-01 and on or before 2026-06-01.

I queried the official CISA KEV machine-readable feeds (JSON at https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json and CSV at https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv). Both feeds confirm the following qualifying entries were added within the window [334fe4, 9334a0]:

1. **Langflow** — vendorProject "Langflow", product "Langflow", CVE-2025-34291, Date Added 2026-05-21. Langflow is an LLM orchestration/chaining framework, which is explicitly named in the resolution criteria's qualifying definition (Category 1: LLM orchestration or chaining). This is the product's primary, core purpose — not an add-on feature. This alone satisfies the resolution condition [334fe4, 9334a0].

2. **BerriAI LiteLLM** — vendorProject "BerriAI", product "LiteLLM", CVE-2026-42208, Date Added 2026-05-08. LiteLLM is an LLM gateway/orchestration and model-serving proxy tool whose primary purpose is AI/LLM API standardization and serving (Categories 1/3). This corroborates the YES resolution [334fe4, 9334a0]. (Independently corroborated by reporting that "CISA added CVE-2026-42208 in BerriAI LiteLLM to the Known Exploited Vulnerabilities catalog" and "CISA Adds Critical Langflow Vulnerability (CVE-2025-34291) to KEV Catalog.")

Because at least one (in fact two) AI-integrated software products meeting the definition had vulnerabilities added to the KEV catalog within the May 1, 2026 – June 1, 2026 window, the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-100. `74d19d30-d036-5a2b-9b5a-ea56cd98d324`

- Present date: `2026-05-02 21:26:40.814176`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the United States and Iran hold a new round of formal negotiations between May 1 and May 31, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 1, 2026 (00:00 UTC) and on or before May 31, 2026 (23:59 UTC), the United States and Iran commence or hold a new round of formal, direct or indirect negotiations. Specifically:

1. **"New round of talks"** means a meeting or series of meetings that occurs on or after May 1, 2026 (UTC), distinct from the failed Islamabad talks of April 11–12, 2026. This includes:
   - **Direct negotiations**: Face-to-face or virtual meetings between official US and Iranian government representatives.
   - **Indirect negotiations**: Shuttle diplomacy or proximity talks mediated by a third party (e.g., Oman, Pakistan, or another mediator), where both the US and Iran have officially dispatched representatives to participate.

2. **What qualifies**: An officially acknowledged diplomatic engagement where both sides confirm (via official government statements, press conferences, or credible reporting) that representatives have been dispatched or are participating in discussions aimed at resolving issues related to Iran's nuclear program, sanctions, the naval blockade, or broader bilateral disputes.

3. **What does NOT qualify**: Informal back-channel contacts, unconfirmed reports of contacts, public statements or proposals exchanged via media without an in-person or virtual meeting, or UN General Assembly sideline encounters not specifically framed as US-Iran negotiations.

4. **Resolution source**: Credible reporting from at least one major international news agency (e.g., [Reuters](https://www.reuters.com/), [Associated Press](https://apnews.com/), [BBC](https://www.bbc.com/news)), or an official statement from the US State Department ([state.gov](https://www.state.gov/)) or Iran's Foreign Ministry confirming that such talks have taken place or been officially announced to take place within the resolution window.

If no such negotiations are confirmed by May 31, 2026 (23:59 UTC), the question resolves **No**.

**Pre-cutoff background**

As of May 2, 2026, US-Iran diplomatic efforts have reached a significant impasse. The most recent round of talks, held in Islamabad on April 11–12, 2026, involved US representatives (Vance, Witkoff, and Kushner) and Iranian representatives (Araghchi and Ghalibaf) but concluded without an agreement [https://en.wikipedia.org/wiki/2025%E2%80%932026_Iran%E2%80%93United_States_negotiations](https://en.wikipedia.org/wiki/2025%E2%80%932026_Iran%E2%80%93United_States_negotiations). US Vice President JD Vance stated that the negotiations produced no agreement, and Iranian officials noted that significant gaps remained and trust had not been established [https://en.wikipedia.org/wiki/2025%E2%80%932026_Iran%E2%80%93United_States_negotiations](https://en.wikipedia.org/wiki/2025%E2%80%932026_Iran%E2%80%93United_States_negotiations). Following the failure of these talks, the United States initiated a naval blockade of Iranian ports on April 13, 2026 [https://en.wikipedia.org/wiki/2025%E2%80%932026_Iran%E2%80%93United_States_negotiations](https://en.wikipedia.org/wiki/2025%E2%80%932026_Iran%E2%80%93United_States_negotiations).

Around April 27, 2026, Iran reportedly submitted a new proposal to decouple the Strait of Hormuz reopening from nuclear talks, which President Trump called "unsatisfactory." No new round of negotiations is currently scheduled, but both sides retain incentives to return to the table: Iran seeks sanctions relief and an end to the blockade, while the Trump administration wants a nuclear deal and faces domestic pressure related to energy prices.

For context on the broader negotiation history, see: [2025–2026 Iran–United States negotiations](https://en.wikipedia.org/wiki/2025%E2%80%932026_Iran%E2%80%93United_States_negotiations). The term "negotiations" here refers to [diplomatic negotiations](https://en.wikipedia.org/wiki/Negotiation) — a formal process of discussion between parties aimed at reaching an agreement.

**Exact later resolution packet**

The question resolves YES. Multiple credible sources confirm that the United States and Iran commenced/held a new round of formal negotiations (indirect, via mediation, plus a tentative agreement) within the May 1–31, 2026 window, distinct from the failed April 11–12, 2026 Islamabad talks.

Key evidence:
- An Al Jazeera article dated May 26, 2026, explicitly states "Iran and the United States continue negotiations through intermediaries to reach an understanding," describing indirect talks with Iranian officials in Qatar [3e4584].
- An Al Jazeera live blog dated May 26, 2026, reports US Secretary of State Marco Rubio confirming that "specific language" for a deal to end the war was being negotiated in Qatar and would "take a few days," and references Iranian officials being in Qatar for talks [47f766].
- An Al Jazeera article (May 29, 2026) on the US-Iran 60-day proposal notes an Iranian delegation traveled to Qatar for negotiations in late May 2026, and that Pakistan's FM Ishaq Dar was scheduled to meet Rubio in Washington on May 29 to continue negotiations to end the war [a4ac04].
- PBS NewsHour / Associated Press (May 29, 2026) report that US and Iranian negotiators reached a tentative agreement to extend the ceasefire and start new nuclear talks, with VP JD Vance confirming the tentative deal and ongoing work on "language points" [3983c9].

These engagements—officially acknowledged indirect negotiations in Qatar with both sides represented, confirmed by the US Secretary of State and reflected in a tentative agreement reached on May 28, 2026—satisfy the resolution criteria for a "new round of formal, direct or indirect negotiations" occurring between May 1 and May 31, 2026, distinct from the April Islamabad talks.

Note: The Wikipedia summary [fb363b] was less explicit about a discrete "meeting," but the primary news sources (Al Jazeera, AP via PBS) clearly document active negotiations, including representatives dispatched to Qatar and a tentative deal in late May.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-101. `54843f56-28cd-5268-ac2a-a572144b2c03`

- Present date: `2026-05-13 21:33:10.304551`
- Source cutoff boundary: `2026-05-14` (encodes end of UTC day `2026-05-13`)
- Expected resolution: `2026-05-27 00:00:00`

**Question**

Will Donald Trump formally endorse either John Cornyn or Ken Paxton in the Texas Senate Republican primary runoff before polls close on May 26, 2026?

**Resolution criteria**

This question resolves **Yes** if Donald Trump issues a formal endorsement of either John Cornyn or Ken Paxton on or after May 12, 2026, and before polls close on May 26, 2026, at 7:00 PM Central Time (i.e., before 2026-05-27 00:00 UTC).

A "formal endorsement" is defined as an explicit, unambiguous public statement of support for one of the two candidates, issued through any of the following channels:
- A post on Trump's Truth Social account (https://truthsocial.com/@realDonaldTrump)
- An official statement from Trump's office or campaign website
- A verbal endorsement made during a public appearance (e.g., rally, press conference, interview) that is recorded or broadcast

The endorsement must clearly name the candidate and express support for their Senate candidacy. Vague praise or comments that fall short of an explicit endorsement (e.g., "he's a great guy") do not count.

If no such endorsement is issued by 7:00 PM CT on May 26, 2026, the question resolves **No**.

**Resolution sources:** Trump's Truth Social account (https://truthsocial.com/@realDonaldTrump), or credible major news reporting from outlets such as the Associated Press (https://apnews.com), Reuters (https://reuters.com), CNN (https://cnn.com), or The New York Times (https://nytimes.com).

**Pre-cutoff background**

As of May 12, 2026, Donald Trump has not endorsed either candidate in the Texas Senate Republican primary runoff between incumbent Senator John Cornyn and Texas Attorney General Ken Paxton. The runoff election is scheduled for May 26, 2026.

Trump promised an endorsement "soon" on March 4, 2026, the day after the Texas Senate Republican primary, but has repeatedly failed to follow through ['It's a mess': With no Trump endorsement in Texas Senate race ...](https://www.cnn.com/2026/04/30/politics/texas-senate-runoff-john-cornyn-ken-paxton-donald-trump). CNN reported on April 30, 2026, that some people involved in the race no longer expect Trump to weigh in, though he could still change his mind ['It's a mess': With no Trump endorsement in Texas Senate race ...](https://www.cnn.com/2026/04/30/politics/texas-senate-runoff-john-cornyn-ken-paxton-donald-trump). The delay is attributed to competing internal pressures: the MAGA base has pushed strongly against endorsing Cornyn, viewing him as insufficiently aligned with Trump's agenda, while Senate Republican leadership—including NRSC chair Steve Daines—has reportedly hoped Trump would either endorse Cornyn or stay neutral ['It's a mess': With no Trump endorsement in Texas Senate race ...](https://www.cnn.com/2026/04/30/politics/texas-senate-runoff-john-cornyn-ken-paxton-donald-trump). Endorsing Paxton risks alienating key Senate allies. Paxton has attempted to secure the endorsement by linking his candidacy to the "Save America Act," legislation Trump supports ['It's a mess': With no Trump endorsement in Texas Senate race ...](https://www.cnn.com/2026/04/30/politics/texas-senate-runoff-john-cornyn-ken-paxton-donald-trump).

Both candidates have spent millions on advertising, and the race remains highly competitive. Trump's endorsement is widely viewed as potentially decisive in the outcome.

**Exact later resolution packet**

YES. The endorsement occurred within the eligible window: Reuters and AP both report the endorsement on May 19, 2026, which is after May 12, 2026 and before the May 26, 2026 7:00 PM CT deadline [Trump backs hardliner Ken Paxton in critical Texas US Senate race ...](https://www.reuters.com/world/us/trump-make-endorsement-texas-us-senate-republican-primary-2026-05-19/) [Trump endorses Paxton over Cornyn in Texas GOP Senate primary](https://apnews.com/article/trump-texas-senate-endorsement-paxton-cornyn-adb4c7213fc2d0db0b29d0ab65d49384). The endorsed candidate was Ken Paxton, not John Cornyn: Reuters states that “President Donald Trump endorsed Texas conservative hardliner Ken Paxton” in Paxton’s primary challenge to Sen. John Cornyn, and AP likewise states that Trump “endorsed Texas Attorney General Ken Paxton in the GOP primary for U.S. Senate” [Trump backs hardliner Ken Paxton in critical Texas US Senate race ...](https://www.reuters.com/world/us/trump-make-endorsement-texas-us-senate-republican-primary-2026-05-19/) [Trump endorses Paxton over Cornyn in Texas GOP Senate primary](https://apnews.com/article/trump-texas-senate-endorsement-paxton-cornyn-adb4c7213fc2d0db0b29d0ab65d49384). The statement was formal and explicit: the quoted language included, “Ken is a true MAGA Warrior who has ALWAYS delivered for Texas, and will continue to do so in the United States Senate,” and AP identifies it as an endorsement of Paxton for the U.S. Senate primary [Trump backs hardliner Ken Paxton in critical Texas US Senate race ...](https://www.reuters.com/world/us/trump-make-endorsement-texas-us-senate-republican-primary-2026-05-19/) [Trump endorses Paxton over Cornyn in Texas GOP Senate primary](https://apnews.com/article/trump-texas-senate-endorsement-paxton-cornyn-adb4c7213fc2d0db0b29d0ab65d49384). The channel also satisfies the criteria because AP reports that the endorsement was made via social media/Truth Social, one of the allowed channels [Trump endorses Paxton over Cornyn in Texas GOP Senate primary](https://apnews.com/article/trump-texas-senate-endorsement-paxton-cornyn-adb4c7213fc2d0db0b29d0ab65d49384). The specific allowed-source evidence used is Reuters, https://www.reuters.com/world/us/trump-make-endorsement-texas-us-senate-republican-primary-2026-05-19/ , and AP, https://apnews.com/article/trump-texas-senate-endorsement-paxton-cornyn-adb4c7213fc2d0db0b29d0ab65d49384 [Trump backs hardliner Ken Paxton in critical Texas US Senate race ...](https://www.reuters.com/world/us/trump-make-endorsement-texas-us-senate-republican-primary-2026-05-19/) [Trump endorses Paxton over Cornyn in Texas GOP Senate primary](https://apnews.com/article/trump-texas-senate-endorsement-paxton-cornyn-adb4c7213fc2d0db0b29d0ab65d49384). Therefore the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-102. `630b345d-eb03-534c-a3e5-5de067aaed7b`

- Present date: `2026-05-14 11:24:43.947611`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

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

**Pre-cutoff background**

PEC 14/2021 is a proposed constitutional amendment (Proposta de Emenda à Constituição) that alters Articles 40, 198, and 201 of Brazil's Federal Constitution to establish special retirement rights (aposentadoria diferenciada) for community health agents (Agentes Comunitários de Saúde) and endemic disease combat agents (Agentes de Combate às Endemias). The PEC was approved by the Chamber of Deputies and sent to the Senate, where it is currently under consideration by the Constitution, Justice and Citizenship Committee (Comissão de Constituição, Justiça e Cidadania — CCJ).

Senator Irajá (PSD-TO) was designated as rapporteur on March 17, 2026 [PEC 14/2021 - Senado Federal](https://www25.senado.leg.br/web/atividade/materias/-/materia/170850). As of May 13, 2026, no report (parecer) has been presented to the CCJ [PEC 14/2021 - Senado Federal](https://www25.senado.leg.br/web/atividade/materias/-/materia/170850). Senator Irajá has publicly stated that the PEC corrects a "historical injustice" and that he expects a vote "still in the first semester" of 2026, but he has also indicated he is "talking to all sectors involved to find a consensus text," suggesting amendments may be introduced [Aposentadoria especial para agentes de saúde será votada ainda ...](https://www12.senado.leg.br/tv/programas/argumento/2026/04/aposentadoria-especial-para-agentes-de-saude-sera-votada-ainda-no-primeiro-semestre-diz-relator).

The federal government and municipal governments (prefeituras) have been actively lobbying against the PEC in its current form due to its potential fiscal impact, estimated at up to R$54 billion over coming decades. The government's strategy may include pushing for amendments that would require the PEC to return to the Chamber of Deputies, effectively delaying or killing the proposal.

Official Senate tracking page: https://www25.senado.leg.br/web/atividade/materias/-/materia/170850

**Exact later resolution packet**

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

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-103. `8c1f48ad-6eab-5d12-bb1d-498e7ba1d4bc`

- Present date: `2026-05-01 11:24:00.926315`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-05-27 00:00:00`

**Question**

Will incumbent Chris Gebhard win the Republican primary for Pennsylvania Senate District 48 on May 19, 2026?

**Resolution criteria**

This question resolves Yes if Chris Gebhard receives the highest number of votes in the Republican primary for Pennsylvania Senate District 48 on May 19, 2026 (polls close at 8:00 PM Eastern Time). It resolves No if any other candidate receives the highest number of votes.

Resolution will be determined by the official results published on the Pennsylvania Department of State election returns website (https://www.electionreturns.pa.gov/). If official certified results are not yet available, unofficial results from the same source may be used, provided the margin is clear and undisputed. In the event of a recount or legal challenge, the question resolves based on the final certified outcome.

A "win" is defined as receiving the highest number of votes among all candidates in the Republican primary for PA Senate District 48 in the official certified results.

**Pre-cutoff background**

On May 19, 2026, Pennsylvania will hold its primary elections. In the Republican primary for Pennsylvania Senate District 48, incumbent Senator Chris Gebhard faces a challenge from Clovis Crane. This race has drawn significant attention due to the contentious issue of "skill games"—slot-like machines found in bars and convenience stores that operate in a legal gray area in Pennsylvania. Gebhard has sponsored legislation that skill games supporters oppose, making him a target for outside interest groups such as the Citizens Alliance of Pennsylvania and Pace-O-Matic, a major developer and distributor of these machines [https://www.spotlightpa.org/news/2026/03/key-2026-primary-elections-pennsylvana-state-house-senate-competitive/](https://www.spotlightpa.org/news/2026/03/key-2026-primary-elections-pennsylvana-state-house-senate-competitive/). Crane has marketed himself as "THE Conservative Republican for District 48" and has benefited from outside spending by skill games interests [https://www.spotlightpa.org/news/2026/03/key-2026-primary-elections-pennsylvana-state-house-senate-competitive/](https://www.spotlightpa.org/news/2026/03/key-2026-primary-elections-pennsylvana-state-house-senate-competitive/). As of April 30, 2026, the race is considered competitive, with outside spending and the skill games regulatory debate playing a central role in the contest [https://www.spotlightpa.org/news/2026/03/key-2026-primary-elections-pennsylvana-state-house-senate-competitive/](https://www.spotlightpa.org/news/2026/03/key-2026-primary-elections-pennsylvana-state-house-senate-competitive/). District 48 covers parts of Lebanon and Lancaster counties in south-central Pennsylvania.

**Exact later resolution packet**

YES. The Pennsylvania Department of State election returns page for the 2026 General Primary, queried at https://www.electionreturns.pa.gov/Home/OfficeResults?officeId=12&districtId=48&ElectionID=117&ElectionType=P&IsActive=1, is specifically for State Senator in the General Assembly, 48th Senatorial District, Republican primary, and lists Clovis Crane with 8,808 votes and Chris Gebhard with 18,201 votes [https://www.electionreturns.pa.gov/Home/OfficeResults?officeId=12&districtId=48&ElectionID=117&ElectionType=P&IsActive=1](https://www.electionreturns.pa.gov/Home/OfficeResults?officeId=12&districtId=48&ElectionID=117&ElectionType=P&IsActive=1). The page labels these as unofficial returns, but the vote margin is 9,393 votes, with Gebhard receiving 67.39% to Crane’s 32.61%, so no other listed candidate received more votes than Gebhard [https://www.electionreturns.pa.gov/Home/OfficeResults?officeId=12&districtId=48&ElectionID=117&ElectionType=P&IsActive=1](https://www.electionreturns.pa.gov/Home/OfficeResults?officeId=12&districtId=48&ElectionID=117&ElectionType=P&IsActive=1). A separate query of the Pennsylvania Department of State newsroom found no official notice on that page of a recount, court order, legal challenge, or amended/certified outcome affecting the 2026 Republican primary for Senate District 48 involving Chris Gebhard or Clovis Crane [https://www.pa.gov/agencies/dos/newsroom.html](https://www.pa.gov/agencies/dos/newsroom.html). Under the resolution criteria, unofficial Department of State results may be used if the margin is clear and undisputed; therefore Chris Gebhard received the highest number of votes in the relevant Republican primary and the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-104. `0e872d88-0696-5bab-bee7-8930a09e301e`

- Present date: `2026-05-02 09:09:03.333068`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the US announce a new bilateral trade deal or framework agreement with an additional country between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between May 1, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC), the White House (https://www.whitehouse.gov/fact-sheets/) or the Office of the United States Trade Representative (https://ustr.gov/trade-topics/presidential-tariff-actions) publishes an official fact sheet, press release, or joint statement announcing a new bilateral trade deal or framework agreement with a country **not** already listed in the background section above as having an announced deal as of April 30, 2026.

A "bilateral trade deal or framework agreement" is defined as any of the following, as announced by the White House or USTR: an Agreement on Reciprocal Trade (ART), a framework trade agreement, an "Economic Prosperity Deal," a trade and investment agreement, or any similarly titled bilateral trade arrangement that includes commitments on tariff reductions, market access, or trade facilitation between the US and a specific country or customs territory.

Memoranda of Understanding (MOUs) that relate solely to non-trade matters (e.g., defense cooperation, immigration) do not count. Agreements limited to a single commodity or product (e.g., a standalone agricultural purchase commitment) also do not count unless they are framed as part of a broader bilateral trade deal.

Updates, amendments, or upgrades to existing deals with countries already listed in the background section do **not** count. The announcement must involve a **new** country partner.

If no qualifying announcement is published by 23:59 UTC on June 1, 2026, the question resolves **No**.

**Pre-cutoff background**

Since April 2025, the Trump administration has aggressively pursued bilateral trade agreements under its "reciprocal trade" policy. As of early 2026, the US has announced framework agreements or finalized trade deals with at least 19 partners. According to the Council on Foreign Relations tracker (last updated March 17, 2026) [Tracking Trump's Trade Deals | Council on Foreign Relations](https://www.cfr.org/articles/tracking-trumps-trade-deals) and the USTR Presidential Tariff Actions page [Presidential Tariff Actions | United States Trade Representative](https://ustr.gov/trade-topics/presidential-tariff-actions), the following countries/entities have announced deals:

- **United Kingdom** (May 8, 2025)
- **Vietnam** (July 2, 2025 framework; October 26, 2025 agreement)
- **Indonesia** (July 15, 2025 framework; February 19, 2026 full agreement)
- **Japan** (July 22, 2025 framework; September 2025 updates)
- **European Union** (July 27–28, 2025 framework)
- **South Korea** (July 30, 2025 / November 2025)
- **Cambodia** (October 26, 2025)
- **Malaysia** (October 26, 2025)
- **Thailand** (October 26, 2025)
- **Argentina** (November 13, 2025 framework; February 5, 2026 full agreement)
- **Ecuador** (November 13, 2025 framework; March 13, 2026 full agreement)
- **El Salvador** (November 13, 2025 framework; January 29, 2026 full agreement)
- **Guatemala** (November 13, 2025 framework; January 30, 2026 full agreement)
- **Switzerland and Liechtenstein** (November 14, 2025)
- **Taiwan** (January 15, 2026 framework; February 12, 2026 full agreement)
- **India** (February 6–9, 2026)
- **Bangladesh** (February 9, 2026)
- **North Macedonia** (February 12, 2026)

The USTR's 2026 Trade Policy Agenda indicates the administration plans to continue negotiating and upgrading framework deals into legally-binding Agreements on Reciprocal Trade (ARTs), and to pursue new agreements with additional countries. The administration has maintained a rapid pace of deal announcements, averaging roughly 1–2 new country announcements per month. However, the pace may slow as the most willing partners have already signed, and remaining negotiations (e.g., with countries like Brazil, the Philippines, or others) may be more complex.

**Exact later resolution packet**

Adjudicated: An official White House fact sheet (May 17, 2026) and USTR press release (May 18, 2026) — both within the May 1–June 1, 2026 window — announced a US-China bilateral trade arrangement whose cornerstone is the U.S.-China Board of Trade (to 'manage bilateral trade across non-sensitive goods') and Board of Investment, plus explicit market-access commitments (restored access for 400+ U.S. beef facilities, resumed poultry imports, rare-earth supply). China is NOT on the question's excluded background list. The resolution criteria's catch-all definition counts 'any similarly titled bilateral trade arrangement that includes commitments on tariff reductions, market access, OR trade facilitation,' so it need not be a titled ART/framework/EPD; the market-access commitments satisfy it. An earlier automated disqualification rests on the CFR tracker classification, but the criteria's actual test is publication by the WH/USTR, which is met.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-105. `26ddb28f-3a4f-557e-9a35-dbbe6058f71f`

- Present date: `2026-05-11 13:27:06.323391`
- Source cutoff boundary: `2026-05-12` (encodes end of UTC day `2026-05-11`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Texas Senate Bill 4 (SB 4) be in effect and enforceable on July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, as of 11:59 PM Central Time on July 1, 2026, Texas Senate Bill 4 (SB 4) is legally in effect and enforceable by state or local law enforcement in Texas, and no court order (such as a temporary restraining order, preliminary injunction, or permanent injunction) fully blocks the law's enforcement statewide.

This question resolves **No** if, as of 11:59 PM Central Time on July 1, 2026, a federal or state court order fully blocks the enforcement of SB 4 statewide (including if such a block is under appeal but remains in effect pending appeal, i.e., an administrative stay alone does not count as the law being "in effect").

**Key clarifications:**
- "In effect" means that the law is legally enforceable and not blocked by any court order that applies statewide. A partial stay—where only some provisions are blocked but the core arrest and deportation provisions remain enforceable—still counts as "in effect" (resolves Yes).
- An administrative stay issued solely for procedural purposes (e.g., to allow briefing on a motion) that prevents enforcement counts as the law NOT being in effect (resolves No).
- If the law is enforced in some jurisdictions of Texas but blocked in others due to local or regional court orders (rather than a statewide order), this question resolves **Yes**, as the law would still be "in effect" in Texas generally.
- If the law has been repealed or otherwise rendered permanently unenforceable by July 1, 2026, this resolves No.

**Resolution sources:** Official court docket entries from the U.S. District Court for the Western District of Texas (accessible via PACER at https://www.txwd.uscourts.gov/) or the 5th U.S. Circuit Court of Appeals (https://www.ca5.uscourts.gov/), and/or credible news reporting from sources such as the Texas Tribune (https://www.texastribune.org/), Reuters, or the Associated Press.

**Pre-cutoff background**

Texas Senate Bill 4 (SB 4), signed into law in 2023, is a state immigration enforcement law that includes several controversial provisions [https://www.texastribune.org/2026/05/04/texas-senate-bill-4-lawsuit/](https://www.texastribune.org/2026/05/04/texas-senate-bill-4-lawsuit/):

- Creates a state-level crime for re-entering the country without authorization, even if the individual has since obtained legal status
- Grants state magistrates the authority to order a person's deportation
- Creates a crime for failing to comply with a magistrate's deportation order
- Requires magistrates to continue a prosecution even if the individual has a pending federal immigration case, such as an asylum claim

SB 4 was previously blocked by a federal preliminary injunction, but the 5th U.S. Circuit Court of Appeals vacated that injunction, finding the original plaintiffs lacked standing. The law is currently scheduled to take effect on May 15, 2026 [https://www.texastribune.org/2026/05/04/texas-senate-bill-4-lawsuit/](https://www.texastribune.org/2026/05/04/texas-senate-bill-4-lawsuit/).

On May 4, 2026, the ACLU of Texas and the Texas Civil Rights Project filed a new class-action lawsuit (LML v. Martin) challenging SB 4 [ACLU of Texas, Partners File New Lawsuit Challenging S.B. 4 ...](https://www.aclutx.org/press-releases/aclu-of-texas-partners-file-new-lawsuit-challenging-s-b-4-texas-deportation-scheme/). The plaintiffs argue the law is unconstitutional because immigration enforcement is exclusively the domain of the federal government and should preempt state law [https://www.texastribune.org/2026/05/04/texas-senate-bill-4-lawsuit/](https://www.texastribune.org/2026/05/04/texas-senate-bill-4-lawsuit/). The legal team is seeking emergency relief—including a temporary restraining order and preliminary injunction—to block several provisions of the law from taking effect on May 15 [ACLU of Texas, Partners File New Lawsuit Challenging S.B. 4 ...](https://www.aclutx.org/press-releases/aclu-of-texas-partners-file-new-lawsuit-challenging-s-b-4-texas-deportation-scheme/).

The core uncertainty is whether the new legal challenge will succeed in obtaining an emergency injunction before or shortly after the May 15 effective date, and whether any such injunction would survive an appeal to the 5th Circuit.

**Exact later resolution packet**

RESOLUTION: YES (1).

The question resolves YES if, as of 11:59 PM CT on July 1, 2026, SB 4 is legally in effect and enforceable in Texas with no court order fully blocking its enforcement statewide. The evidence shows SB 4 was in full effect statewide as of that deadline.

TIMELINE ESTABLISHED FROM SOURCES:
- April 24, 2026: The en banc Fifth Circuit vacated the original preliminary injunction (Las Americas/El Paso County challenge) by a 10-7 vote, holding plaintiffs lacked standing, clearing SB 4 to take effect (scheduled May 15).
- May 4, 2026: ACLU of Texas filed a new class action, LML v. Martin (No. 1:26-CV-01170-DAE, W.D. Tex.).
- May 14, 2026: The U.S. District Court (W.D. Tex.) granted a PARTIAL preliminary injunction blocking four key provisions of SB 4; the first-offense illegal-entry provision still took effect May 15.
- May 29, 2026: The Fifth Circuit STAYED the district court's May 14 preliminary injunction PENDING APPEAL, allowing enforcement of the previously-enjoined provisions. Multiple sources state SB 4 became "fully implemented"/"in effect in its entirety" as of this date.

KEY EVIDENCE THAT SB 4 WAS IN EFFECT ON JULY 1, 2026:
- The Texas Municipal Courts Education Center states: "On May 29, 2026, the 5th Circuit stayed the district court's preliminary injunction in L.M.L. & K.G.S. v. Martin pending appeal, allowing enforcement" of the provisions [2b9d4c]. This is a stay pending appeal, not merely a procedural administrative stay.
- The American Immigration Council (article dated June 29, 2026 — just two days before the deadline): "In late May, a Fifth Circuit Court of Appeals ruling allowed the law to take effect in its entirety while litigation continues, ending a years-long cycle of injunctions, appeals, and conflicting court orders." No subsequent re-blocking is reported [18f226].
- El Paso Matters/Texas Tribune (June 1, 2026): the Fifth Circuit's Friday (May 29) ruling "clears the law to take effect in its entirety" [8f978d].
- ACLU of Texas "Know Your Rights" page: "S.B.4 is in effect as of May 29, 2026" [df195c].
- Tahirih Justice Center: "On May 29, 2026, the Fifth Circuit granted a stay of the injunction... SB4 is now fully implemented" [7261d1].
- Fox 7 Austin (May 29, 2026): the Fifth Circuit granted Texas' appeal, "staying the previous injunction," making the law enforceable [5d9b8f].
- Jurist (June 2026): the Fifth Circuit "cleared the way for Texas to enforce Senate Bill 4 (SB 4), staying a district court" injunction on the core provisions [17e7a0].

APPLYING THE RESOLUTION CRITERIA:
1. Statewide vs. regional: The May 29 Fifth Circuit stay applies to the district court's statewide injunction; the result is that no court order blocks SB 4 anywhere in Texas. This satisfies the "no statewide block" condition for YES.
2. Administrative stay concern: The criteria specify that an administrative stay that PREVENTS enforcement counts as NO. Here, the opposite is true — the Fifth Circuit stayed the injunction that had been blocking the law, thereby ENABLING enforcement. Moreover, sources describe it as a stay "pending appeal" (a merits stay), not a mere procedural administrative stay. So the administrative-stay exception does not apply.
3. Partial vs. full: The criteria say even a partial stay (with core arrest/deportation provisions enforceable) resolves YES. Here the stay was full — sources say the law took effect "in its entirety" — so all provisions, including the core arrest and deportation provisions, were enforceable.
4. No repeal or permanent unenforceability occurred.

No source found any Supreme Court vacatur or new injunction re-blocking SB 4 between May 29 and July 1, 2026. (A June 10, 2026 SCOTUS emergency application was in a separate case, SEAT v. Paxton, No. 1:25-cv-1662-RP, not the SB 4 immigration-enforcement case LML v. Martin.) The most recent source (American Immigration Council, June 29, 2026) confirms the law remained fully in effect [18f226].

CONCLUSION: As of 11:59 PM CT on July 1, 2026, SB 4 was legally in effect and enforceable statewide with no statewide court order blocking it. Resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-106. `e5493956-07d2-5dc5-8278-30bd6555c1a2`

- Present date: `2026-05-03 03:56:09.757685`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Howard Lutnick still be serving as U.S. Commerce Secretary on June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if Howard Lutnick is the serving United States Secretary of Commerce as of 12:00 PM Eastern Time (ET) on June 1, 2026. It resolves **No** otherwise.

**Key definitions and clarifications:**

- "Commerce Secretary" refers to the [United States Secretary of Commerce](https://en.wikipedia.org/wiki/United_States_Secretary_of_Commerce), the head of the U.S. Department of Commerce and a member of the President's Cabinet.
- "Serving" means Lutnick holds the position of Secretary of Commerce in a confirmed (Senate-confirmed) capacity. If Lutnick has been removed or has resigned but is serving in an **Acting** capacity only, this does **not** count as serving and the question resolves **No**.
- If Lutnick has **announced** a resignation but has not yet formally vacated the office (i.e., the resignation has not taken effect) as of 12:00 PM ET on June 1, 2026, the question resolves **Yes**, since he would still technically hold the position.
- If Lutnick is temporarily absent (e.g., on medical leave) but has not resigned or been removed, the question resolves **Yes**.

**Primary resolution source:** The official U.S. Department of Commerce leadership page at [https://www.commerce.gov/about/leadership](https://www.commerce.gov/about/leadership) and the individual Secretary page at [https://www.commerce.gov/about/leadership/howard-lutnick](https://www.commerce.gov/about/leadership/howard-lutnick). If the official page is unavailable or ambiguous, credible reporting from major outlets such as [Reuters](https://www.reuters.com), [AP News](https://apnews.com), [Politico](https://www.politico.com), or official White House announcements at [https://www.whitehouse.gov/briefing-room/](https://www.whitehouse.gov/briefing-room/) may be used.

**Pre-cutoff background**

Howard Lutnick was sworn in as the 41st United States Secretary of Commerce on February 21, 2025. The [Commerce Secretary](https://en.wikipedia.org/wiki/United_States_Secretary_of_Commerce) is a Cabinet-level position heading the U.S. Department of Commerce, responsible for promoting economic growth, trade, and technological development.

As of May 1, 2026, Lutnick remains in office. However, on April 2, 2026, *Politico* reported that President Trump has expressed frustration with Lutnick and that a senior official described him as being on "thin ice" [https://www.politico.com/news/2026/04/02/trump-weighs-more-cabinet-changes-after-bondi-ouster-00856921](https://www.politico.com/news/2026/04/02/trump-weighs-more-cabinet-changes-after-bondi-ouster-00856921). The report characterized Lutnick as an "abrasive, polarizing figure" who has "underperformed" or "generated too much negative attention" [https://www.politico.com/news/2026/04/02/trump-weighs-more-cabinet-changes-after-bondi-ouster-00856921](https://www.politico.com/news/2026/04/02/trump-weighs-more-cabinet-changes-after-bondi-ouster-00856921). The article noted that Trump has previously contemplated firing Lutnick but backed off [https://www.politico.com/news/2026/04/02/trump-weighs-more-cabinet-changes-after-bondi-ouster-00856921](https://www.politico.com/news/2026/04/02/trump-weighs-more-cabinet-changes-after-bondi-ouster-00856921). A White House spokesperson and another official defended Lutnick, stating he is "doing a great job" and has the President's "full support" [https://www.politico.com/news/2026/04/02/trump-weighs-more-cabinet-changes-after-bondi-ouster-00856921](https://www.politico.com/news/2026/04/02/trump-weighs-more-cabinet-changes-after-bondi-ouster-00856921).

This question arises in the context of broader Cabinet turnover during Trump's second term, including the reported ouster of Attorney General Pam Bondi referenced in the same Politico article [https://www.politico.com/news/2026/04/02/trump-weighs-more-cabinet-changes-after-bondi-ouster-00856921](https://www.politico.com/news/2026/04/02/trump-weighs-more-cabinet-changes-after-bondi-ouster-00856921). Prediction markets as of late April 2026 assign roughly 14–38% probability to Lutnick leaving before September 2026, suggesting meaningful but not overwhelming uncertainty about his near-term tenure.

**Exact later resolution packet**

The question resolves YES if Howard Lutnick is the serving (Senate-confirmed) U.S. Secretary of Commerce as of 12:00 PM ET on June 1, 2026.

Evidence:
- Lutnick was confirmed as the 41st U.S. Secretary of Commerce (Senate-confirmed, sworn in February 21, 2025), holding the office in a confirmed capacity (not acting).
- Wikipedia's Howard Lutnick article, last edited May 18, 2026, lists him as the incumbent Secretary of Commerce with no indication of resignation or removal [53149c].
- A New York Times article published May 28, 2026 ("Bare-Knuckle Tactics and Brash Promises: How Howard Lutnick...") refers to him in the present tense as the serving Commerce Secretary, discussing his ongoing departmental activities and recent congressional hearings, with no indication he had resigned or vacated office [6e4ba2].
- Multiple May 2026 sources corroborate he was actively serving: congressional letters addressed to "The Honorable Howard Lutnick, Secretary, U.S. Department of Commerce" dated May 6 and May 14, 2026; a transcribed Oversight Committee interview on May 6, 2026; the SelectUSA Investment Summit remarks on May 4, 2026; and a CNBC interview aired around May 29, 2026.
- Despite ongoing political pressure and calls for resignation over his Epstein ties (Feb–May 2026) and reports of Trump's frustration (April 2026), no source indicates Lutnick actually resigned or was removed before June 1, 2026.

There is no evidence of any departure, resignation taking effect, or transition to an Acting capacity before the deadline. The most recent reporting (within days of the deadline) confirms he remained the confirmed Secretary. Therefore the question resolves YES.

Primary source URLs: https://www.commerce.gov/about/leadership and https://www.commerce.gov/about/leadership/howard-lutnick (the commerce.gov leadership page returned no extractable content during this research). Supporting URLs: https://en.wikipedia.org/wiki/Howard_Lutnick ; https://www.nytimes.com/2026/05/28/nyregion/lutnick-commerce-companies-business.html ; https://oversightdemocrats.house.gov/imo/media/doc/letter_to_the_honorable_howard_lutnick_secretary_usdepartmentofcommerce.pdf (May 6, 2026 interview reference); https://uaw.org/wp-content/uploads/2026/05/260514-UAW-Letter-on-Conn-Selmer.pdf (May 14, 2026 letter to Secretary Lutnick).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-107. `4c864e5d-4bb5-5d1b-805b-79af67f9cebf`

- Present date: `2026-05-01 14:34:43.372574`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the Musk v. Altman trial (Case No. 3:24-cv-04722, N.D. Cal.) result in a jury verdict or settlement on or after April 30, 2026, and before June 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after April 30, 2026, and before June 1, 2026, 11:59 PM Pacific Time, either of the following occurs in the case Musk v. Altman (CourtListener docket: https://www.courtlistener.com/docket/69013420/musk-v-altman/), filed in the U.S. District Court for the Northern District of California:

1. **Verdict**: The jury returns a signed verdict form in the liability phase of the trial, as reflected in the court's docket or reported by at least two of the following news organizations: Reuters, Associated Press, Bloomberg, CNBC, or the New York Times; OR

2. **Settlement**: A notice of settlement or stipulation of dismissal based on settlement is filed on the court docket, or a settlement is publicly announced by the parties and confirmed by at least two of the above-listed news organizations.

The question resolves NO if neither a verdict nor a settlement occurs before the deadline. A mistrial, continuance, or dismissal on procedural grounds without a settlement does not count as YES. Only events occurring on or after April 30, 2026, qualify.

**Pre-cutoff background**

On April 27, 2026, jury selection was completed in Musk v. Altman in the U.S. District Court for the Northern District of California (Oakland), before Judge Yvonne Gonzalez Rogers [Judge in Musk v. Altman seats nine-person jury. Opening ... - CNBC](https://www.cnbc.com/2026/04/27/musk-altman-trial-openai-jury-selection.html). A nine-person jury was seated, and opening arguments began on April 28, 2026 [Judge in Musk v. Altman seats nine-person jury. Opening ... - CNBC](https://www.cnbc.com/2026/04/27/musk-altman-trial-openai-jury-selection.html). Elon Musk's lawsuit alleges that OpenAI CEO Sam Altman and President Greg Brockman betrayed OpenAI's founding nonprofit mission by converting it into a for-profit entity. Musk seeks over $150 billion in damages and the removal of Altman and Brockman [AI showdown: Musk and Altman go to trial in fight over OpenAI's ...](https://apnews.com/article/musk-altman-artificial-intelligence-trial-openai-eb854fa682675f70267abd8a7b9a6a43).

The trial has been divided into two phases: a liability phase (to determine if wrongdoing occurred) and a remedies phase (to determine damages). The liability phase is expected to conclude by approximately May 21, 2026 [Judge in Musk v. Altman seats nine-person jury. Opening ... - CNBC](https://www.cnbc.com/2026/04/27/musk-altman-trial-openai-jury-selection.html). The jury's verdict in the liability phase is advisory, with Judge Gonzalez Rogers making the final decision [Judge in Musk v. Altman seats nine-person jury. Opening ... - CNBC](https://www.cnbc.com/2026/04/27/musk-altman-trial-openai-jury-selection.html).

As of April 30, 2026, testimony is underway, with Musk having testified on April 28–29, 2026 [Elon Musk trial against Sam Altman to reveal OpenAI power struggle ...](https://www.reuters.com/business/elon-musks-trial-against-sam-altman-reveal-ongoing-power-struggle-openai-2026-04-27/). High-profile witnesses including Microsoft CEO Satya Nadella are expected to testify [Elon Musk trial against Sam Altman to reveal OpenAI power struggle ...](https://www.reuters.com/business/elon-musks-trial-against-sam-altman-reveal-ongoing-power-struggle-openai-2026-04-27/). A settlement could occur at any point during the trial. The expected conclusion of the liability phase around May 21 puts a potential verdict within the resolution window, but trials frequently run longer than expected, creating genuine uncertainty about whether a verdict will be reached before June 1, 2026.

**Exact later resolution packet**

The question resolves YES because the jury returned a verdict in the liability phase of Musk v. Altman on Monday, May 18, 2026, which falls within the resolution window (on or after April 30, 2026, and before June 1, 2026, 11:59 PM Pacific Time).

Key facts:
- The nine-person jury in Oakland, California federal court returned a unanimous verdict on May 18, 2026, finding OpenAI, Sam Altman, and Greg Brockman not liable, on the grounds that Musk's claims were barred by the three-year statute of limitations [4841af, 8ee594].
- This verdict was reported by Reuters ("A U.S. jury on Monday ruled against Elon Musk in his lawsuit against OpenAI... In a unanimous verdict, the jury in Oakland, California, federal court said Musk brought his case too late") [4841af] and by CNBC ("A federal jury in Oakland, California, on Monday said Elon Musk waited too long to sue OpenAI... The jury found that Musk's claims were filed outside of the statute of limitations") [8ee594]. These are two of the five specified news organizations (Reuters, AP, Bloomberg, CNBC, NYT), satisfying the requirement of confirmation by at least two listed outlets. The New York Times also reported it.

The resolution criteria require ONLY that a jury return a signed verdict form in the liability phase (Option 1), regardless of which party prevailed. That condition was met: the jury reached and returned a unanimous verdict in the liability phase on May 18, 2026, within the window. Although the jury's verdict was advisory (with the judge making the final decision), the criteria explicitly key on "the jury returns a signed verdict form in the liability phase," which occurred. This is not a mistrial, continuance, or procedural dismissal without settlement — it is an actual jury verdict reached after deliberation. Therefore the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-108. `c72d9a92-4f4f-5a7d-a743-ba16f38cf7c9`

- Present date: `2026-05-03 02:10:21.202298`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the Musk v. Altman trial (Case No. 4:24-cv-04722) reach a jury verdict by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 1, 2026, a jury verdict (defined as a formal finding or recommendation returned by the seated jury to the court on the merits of any claim in the case) is delivered in *Musk v. Altman*, Case No. 4:24-cv-04722, U.S. District Court for the Northern District of California, by 11:59 PM Pacific Time (PT) on June 1, 2026.

This question resolves **No** if no jury verdict has been returned by that deadline — including if the trial is still ongoing, a mistrial is declared, or the case is settled or dismissed before a verdict is reached.

Note: Because the jury's verdict in this case is advisory, a "jury verdict" here means the jury's formal advisory recommendation to the judge, not the judge's final ruling.

Resolution will be verified via the official court docket on CourtListener (https://www.courtlistener.com/docket/69013420/musk-v-altman/) or credible reporting from major news outlets such as the New York Times (https://www.nytimes.com/), Reuters (https://www.reuters.com/), CNBC (https://www.cnbc.com/), or the Associated Press (https://apnews.com/).

**Pre-cutoff background**

On April 28, 2026, the trial in *Musk v. Altman* (Case No. 4:24-cv-04722) began in the U.S. District Court for the Northern District of California in Oakland [Musk v. Altman: The $134 Billion OpenAI Trial Explained](https://letsdatascience.com/blog/musk-sued-openai-for-134-billion-the-jury-decides-in-34-days). Elon Musk is suing OpenAI co-founders Sam Altman and Greg Brockman, as well as OpenAI itself, seeking approximately $134 billion in damages over claims including fraud, breach of charitable trust, and unjust enrichment. Musk alleges that Altman and others pulled OpenAI away from its nonprofit roots for personal gain.

The trial is scheduled to last approximately four weeks [Musk v. Altman: The $134 Billion OpenAI Trial Explained](https://letsdatascience.com/blog/musk-sued-openai-for-134-billion-the-jury-decides-in-34-days), which would place the expected conclusion in late May 2026. The jury's role is advisory, with the federal judge making the final decision. Jury selection began on April 27, 2026, and opening statements commenced on April 28, 2026.

However, complex civil trials frequently run over schedule due to extended cross-examinations, evidentiary disputes, mid-trial motions, or lengthy jury deliberations. Given the complexity of the claims, the number of parties involved, and the high stakes ($134B+), there is genuine uncertainty about whether the jury will return its advisory verdict before June 1, 2026.

**Exact later resolution packet**

The question resolves YES. The advisory jury in Musk v. Altman (Case No. 4:24-cv-04722, U.S. District Court for the Northern District of California, Judge Yvonne Gonzalez Rogers) returned its verdict on Monday, May 18, 2026 — well before the June 1, 2026 11:59 PM PT deadline and after the May 1, 2026 start of the window.

- Reuters reported that "In a unanimous verdict, the jury in Oakland, California, federal court said Musk brought his case too late," with deliberations lasting less than two hours [OpenAI defeats Elon Musk's lawsuit, removes obstacle to IPO | Reuters](https://www.reuters.com/legal/government/elon-musk-loses-lawsuit-against-openai-2026-05-18/).
- CNBC explicitly confirmed: "The advisory jury's verdict, which came after less than two hours of deliberations, was immediately adopted by District Court Judge Yvonne Gonzalez Rogers" [Musk slams Altman trial verdict as a 'technicality,' vows to appeal](https://www.cnbc.com/2026/05/18/musk-altman-openai-trial-verdict.html). This distinguishes the jury's formal advisory recommendation (the relevant event per the resolution criteria) from the judge's separate adoption/final ruling.

The case number (4:24-cv-04722) and jurisdiction (N.D. Cal., Oakland) match the question exactly. No settlement, dismissal, or mistrial occurred before a verdict — the jury did return a formal finding on the merits. Per the resolution criteria, the jury's advisory recommendation counts as a "jury verdict." Therefore the question resolves YES (1).

Source URLs:
- Reuters: https://www.reuters.com/legal/government/elon-musk-loses-lawsuit-against-openai-2026-05-18/ [OpenAI defeats Elon Musk's lawsuit, removes obstacle to IPO | Reuters](https://www.reuters.com/legal/government/elon-musk-loses-lawsuit-against-openai-2026-05-18/)
- CNBC: https://www.cnbc.com/2026/05/18/musk-altman-openai-trial-verdict.html [Musk slams Altman trial verdict as a 'technicality,' vows to appeal](https://www.cnbc.com/2026/05/18/musk-altman-openai-trial-verdict.html)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-109. `abd86c65-1733-557c-98c3-0b141a39781b`

- Present date: `2026-05-14 03:30:21.072100`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-30T00:00:00`

**Question**

Will the first EU accession negotiation cluster with Ukraine be formally opened by June 30, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026, and on or before June 30, 2026, 23:59 UTC, the first EU accession negotiation cluster with Ukraine is formally opened. 

A cluster is considered "formally opened" if an Intergovernmental Conference (IGC) is held at which the Council of the European Union and Ukraine officially open at least one negotiation cluster (expected to be Cluster 1, "Fundamentals"), as confirmed by an official press release or communiqué from the [Council of the European Union](https://www.consilium.europa.eu/en/press/press-releases/) or the [European Commission's press corner](https://ec.europa.eu/commission/presscorner/home/en).

A "negotiation cluster" refers to one of the six thematic groupings of EU acquis chapters used in accession negotiations, as described in the [European Commission's accession process factsheet](https://enlargement.ec.europa.eu/enlargement-policy/steps-towards-joining_en).

If no such formal opening occurs by June 30, 2026, 23:59 UTC, or if only technical/preparatory steps are taken without a formal IGC opening, the question resolves **No**.

**Pre-cutoff background**

Ukraine has held EU candidate status since June 2022, and accession negotiations have formally begun. The EU accession process is structured around six [negotiation clusters](https://en.wikipedia.org/wiki/Enlargement_of_the_European_Union), each grouping several policy chapters of the EU acquis. The first cluster, called "Fundamentals," covers rule of law, judiciary, anti-corruption, and other core areas, and must be opened first and closed last [Steps towards joining - Enlargement and Eastern Neighbourhood](https://enlargement.ec.europa.eu/enlargement-policy/steps-towards-joining_en).

As of May 12, 2026, no negotiation cluster has been formally opened with Ukraine [EU could open all Ukraine negotiation clusters in July - Ukrinform](https://www.ukrinform.net/rubric-polytics/4121870-eu-could-open-all-ukraine-negotiation-clusters-in-july-commissioner-kos.html). While technical screening work has been completed across all six clusters, the formal opening requires a unanimous decision by all EU member states in the Council of the European Union, followed by an Intergovernmental Conference (IGC) — the formal venue where ministers and ambassadors of EU governments meet with the candidate country to conduct negotiations [Steps towards joining - Enlargement and Eastern Neighbourhood](https://enlargement.ec.europa.eu/enlargement-policy/steps-towards-joining_en).

EU Enlargement Commissioner Marta Kos stated on May 11, 2026, that the first cluster could be opened during the Cypriot Council presidency, which runs until June 30, 2026, and that all clusters could potentially be opened by July [EU could open all Ukraine negotiation clusters in July - Ukrinform](https://www.ukrinform.net/rubric-polytics/4121870-eu-could-open-all-ukraine-negotiation-clusters-in-july-commissioner-kos.html). Ukrainian President Zelenskyy has said Ukraine expects clusters to begin opening in May–June 2026. However, the unanimity requirement means any single member state can block the process, and Hungary has previously vetoed steps in Ukraine's accession path. Some observers note that nothing has yet been formally committed on paper, creating genuine uncertainty about whether the June 30 target will be met.

**Exact later resolution packet**

The question resolves YES. The first EU accession negotiation cluster with Ukraine — Cluster 1, "Fundamentals" — was formally opened on 15 June 2026, well within the resolution window (on or after 12 May 2026 and on or before 30 June 2026, 23:59 UTC).

Key evidence:

1. Official Council of the European Union press release, "EU and Ukraine open first accession negotiations cluster," dated 15 June 2026: it states that "the EU and Ukraine reached a significant milestone by opening negotiations on the so-called 'fundamentals' cluster," describes the event as an "Accession Conference," and notes that "Negotiations on the Fundamentals cluster are the first ones to be opened and the last ones to be closed in the accession process." URL: https://www.consilium.europa.eu/en/press/press-releases/2026/06/15/eu-and-ukraine-open-first-accession-negotiations-cluster/ [EU and Ukraine open first accession negotiations cluster - Consilium](https://www.consilium.europa.eu/en/press/press-releases/2026/06/15/eu-and-ukraine-open-first-accession-negotiations-cluster/)

2. Official Council of the EU meeting page for the "Second Accession Conference with Ukraine," held 15 June 2026 in Luxembourg, which explicitly served to "open negotiations on cluster 1: fundamentals." This is the Intergovernmental Conference (IGC) / Accession Conference required by the resolution criteria. URL: https://www.consilium.europa.eu/en/meetings/international-ministerial-meetings/2026/06/15/ukraine/ [Second Accession Conference with Ukraine - consilium.europa.eu](https://www.consilium.europa.eu/en/meetings/international-ministerial-meetings/2026/06/15/ukraine/)

Distinguishing formal opening from technical/preparatory work: The resolution criteria require an IGC at which the Council and Ukraine officially open at least one cluster, not merely technical screening. The 15 June 2026 event was precisely such a formal IGC (the "Second Accession Conference with Ukraine"). This followed the necessary precursor steps: Hungary lifting its long-standing veto in early June 2026, and on 12 June 2026 the EU member states' ambassadors (Coreper) formally agreeing to open the cluster — but the binding formal opening event itself was the 15 June IGC/Accession Conference confirmed by the Council press release. This goes beyond the "only technical/preparatory steps" that the criteria say would resolve NO; the IGC constituted the formal opening.

Therefore, the antecedent condition (a formal IGC opening a cluster within the window) is satisfied, and the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-110. `08621383-abe1-5f08-a7cf-c2d428fb717f`

- Present date: `2026-05-13 23:17:56.170066`
- Source cutoff boundary: `2026-05-14` (encodes end of UTC day `2026-05-13`)
- Expected resolution: `2026-06-12T00:00:00`

**Question**

Will the European Parliament and the Council reach a provisional political agreement on the Returns Regulation (2025/0059(COD)) by June 12, 2026?

**Resolution criteria**

This question resolves YES if, on or after May 12, 2026 (00:00 UTC), a provisional political agreement on the Returns Regulation (legislative procedure 2025/0059(COD)) is formally announced by June 12, 2026 (23:59 UTC).

A "provisional political agreement" is defined as a formal announcement—via an official press release or statement—from the Council of the EU (https://www.consilium.europa.eu/en/press/press-releases/) and/or the European Parliament (https://www.europarl.europa.eu/news/en/press-room) confirming that co-legislators have reached political agreement on the text of the Returns Regulation.

This question resolves NO if no such announcement is published by June 12, 2026 (23:59 UTC). Any provisional agreements reached before May 12, 2026 (00:00 UTC) do not count toward resolution.

**Pre-cutoff background**

The Returns Regulation (legislative procedure 2025/0059(COD)) is a proposed EU regulation aimed at establishing a more effective framework for returning third-country nationals who have no legal right to stay in the EU. It is a key component of the broader Migration and Asylum Pact, which is scheduled to enter into force on June 12, 2026.

On March 26, 2026, the European Parliament approved its negotiating mandate on the Returns Regulation, enabling trilogue negotiations with the Council to begin. A second trilogue took place in late April 2026 and was described by EU sources as "constructive," with some technical progress made [https://euperspectives.eu/2026/04/deadline-looms-over-eu-migrant-return-rules/](https://euperspectives.eu/2026/04/deadline-looms-over-eu-migrant-return-rules/). However, key political groups—the Greens/EFA and The Left—have been absent from negotiations, weakening the Parliament's ability to project a unified position [https://euperspectives.eu/2026/04/deadline-looms-over-eu-migrant-return-rules/](https://euperspectives.eu/2026/04/deadline-looms-over-eu-migrant-return-rules/).

As of May 13, 2026, the next political trilogue is provisionally scheduled for June 1, 2026 (UTC) [https://euperspectives.eu/2026/04/deadline-looms-over-eu-migrant-return-rules/](https://euperspectives.eu/2026/04/deadline-looms-over-eu-migrant-return-rules/). Key disputed issues remain, including: mutual recognition of return decisions, the regulation's entry into force date, communication with non-recognised third-country entities, and cooperation with non-EU partners [https://euperspectives.eu/2026/04/deadline-looms-over-eu-migrant-return-rules/](https://euperspectives.eu/2026/04/deadline-looms-over-eu-migrant-return-rules/). The June 12, 2026 Pact implementation deadline creates strong political pressure to finalize the regulation, but the unresolved disputes and absent political groups introduce genuine uncertainty about whether a deal can be reached in time.

**Exact later resolution packet**

Adjudicated: On 1 June 2026 (within the May 12 - June 12 window) Parliament and Council negotiators reached a provisional political agreement on the Returns Regulation, announced by official press releases from both the Council (consilium.europa.eu press release dated 2026/06/01, 'Council and Parliament reach deal on returns of illegally staying third-country nationals') and the European Parliament ('Deal on new EU rules on migrant returns'), and welcomed by the Commission ('the political agreement reached between the European Parliament and the Council on 1 June 2026 on the Regulation establishing a new Common European System for Returns'). The criteria's parenthetical procedure code 2018/0329(COD) is a scrivener error: that file is the withdrawn 2018 'Return Directive (recast)' - a Directive, not a Regulation - whereas the actual Returns Regulation (proposed March 2025) is procedure 2025/0059(COD); the criteria's own operative subject is 'the Returns Regulation' (a Regulation), and the entire question/description context (March 2025 proposal, 26 Mar 2026 mandate, April/June 2026 trilogues, June 12 Pact deadline) unambiguously describes the 2025/0059 file that got the June 1 deal. An earlier automated NO rests on the mislabeled code alone; the substantive event required by the criteria plainly occurred.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-111. `1a72e885-3f5f-5b05-908f-d1917db3547e`

- Present date: `2026-05-14 05:20:21.640792`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will at least one federal agency issue reclassification notices to employees under Schedule Policy/Career between May 12, 2026 and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 and by 23:59 UTC on July 1, 2026, at least one U.S. federal agency (as defined by [5 U.S.C. § 105](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title5-section105&num=0&edition=prelim)) has issued formal reclassification notices to individual employees informing them that their positions are being moved into "Schedule Policy/Career" — a category of the excepted service established by [Executive Order 14171](https://www.federalregister.gov/documents/2025/01/27/2025-01953/restoring-accountability-to-policy-influencing-positions-within-the-federal-workforce) and the [OPM final rule published February 6, 2026](https://www.federalregister.gov/documents/2026/02/06/2026-02375/improving-performance-accountability-and-responsiveness-in-the-civil-service), distinct from other excepted service schedules (Schedule A, B, C, or D).

A "reclassification notice" means a formal written communication from an agency to an individual employee (or a class of employees) informing them that their position has been or will be transferred from the competitive service into Schedule Policy/Career.

**Required evidence for resolution:** The issuance of such notices must be confirmed by at least one of the following:
- An official agency press release or OPM announcement (e.g., at https://www.opm.gov/news/news-releases/)
- An official OPM report or guidance document (e.g., at https://www.opm.gov/policy-data-oversight/hiring-information/hiring-authorities/schedule-policycareer/)
- Credible news reporting from outlets such as Federal News Network (https://federalnewsnetwork.com/), Government Executive (https://www.govexec.com/), The Washington Post, Reuters, or the Associated Press, based on confirmed internal memos, employee testimony, or official statements
- Court filings referencing specific notices that have been issued

If no credible evidence of such notices emerges by 23:59 UTC on July 1, 2026, the question resolves **No**.

Note: General announcements about agency position lists submitted to OPM, or the signing of an executive order designating positions, do *not* by themselves satisfy resolution. The question requires evidence that individual employees have received or begun receiving formal notification of their reclassification.

**Pre-cutoff background**

On January 20, 2025, President Trump signed Executive Order 14171, directing the Office of Personnel Management (OPM) to reestablish a new excepted service schedule called "Schedule Policy/Career" (formerly known as "Schedule F"), targeting federal employees in policy-influencing positions. OPM published the final rule in the Federal Register on February 6, 2026, with an effective date of March 8–9, 2026 (https://www.opm.gov/news/news-releases/opm-finalizes-schedule-policycareer-rule-to-strengthen-accountability/).

Under the rule, agencies must submit lists of positions proposed for reclassification to OPM. However, no positions can actually be moved into Schedule Policy/Career until the President issues a separate executive order formally placing those positions into the new schedule (per OPM's FAQ: https://www.opm.gov/policy-data-oversight/hiring-information/hiring-authorities/schedule-policycareer/opm-answers-to-frequently-asked-schedule-policycareer-questions.pdf). OPM estimates approximately 50,000 positions could be reclassified [Critics argue new federal workforce rules increase the risk ...](https://www.govexec.com/management/2026/04/critics-argue-new-federal-workforce-rules-increase-risk-politicization-not-accountability/412558/).

As of May 13, 2026, it is not confirmed that the President has yet issued the executive order placing specific positions into Schedule Policy/Career. Additionally, a coalition including AFGE, AFSCME, and the AFL-CIO filed an amended lawsuit in March 2026 challenging the legality of Schedule Policy/Career, arguing it exceeds presidential authority [Lawsuit contends Schedule Policy/Career exceeds presidential ...](https://federalnewsnetwork.com/litigation/2026/03/lawsuit-contends-schedule-policy-career-exceeds-presidential-authority/). No court injunction blocking implementation had been reported as of that filing.

For reclassification notices to be issued, three conditions must be met: (1) the President must sign the executive order designating specific positions, (2) no court must block implementation, and (3) agencies must complete internal processes to notify individual employees. Each of these steps introduces uncertainty about timing.

**Exact later resolution packet**

Adjudicated: President Trump signed EO 14410 on June 3, 2026 placing ~8,000 positions into Schedule Policy/Career, and the order plus OPM guidance imposed a MANDATORY June 10, 2026 deadline (7 days) for agencies to notify encumbering employees and process SF-50 personnel actions with a June 3 effective date, well inside the window that closes July 1. OPM's official June 29, 2026 bulletin -- an explicitly-listed qualifying evidence type -- states 'Agencies are required to notify employees of their placement into the excepted service under Schedule Policy/Career' and 'should have completed the transition documentation by June 10, 2026,' and no court blocked implementation before July 1. The State Department separately emailed staff on June 4 (reported by GovExec from a confirmed internal memo) that 100 positions were placed into Schedule Policy/Career and encumbering employees would be individually notified within seven work days, a formal written communication to a class of employees. Given the binding June 10 deadline three weeks before window close and OPM's own June 29 document treating the notification/SF-50 documentation as a completed requirement across dozens of agencies, formal reclassification notices were issued to employees within the window; an earlier automated NO overweights the absence of a single 'confirmed receipt' headline against these directives and the settled ground truth.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-112. `d3a6d847-a02f-5d73-9933-26c7587b5ab2`

- Present date: `2026-05-02 12:49:35.399599`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-05-22 00:00:00`

**Question**

Will the EU's ban on exporting mixed municipal waste for recovery to non-EEA countries take effect on May 21, 2026, without any delay or exemption being formally enacted?

**Resolution criteria**

This question resolves **Yes** if, as of 23:59 UTC on May 21, 2026, no formal amendment, delegated act, implementing act, or other EU legislative instrument has been published in the Official Journal of the European Union (https://eur-lex.europa.eu/) that delays, modifies, or creates an exemption to the ban on exporting mixed municipal waste for recovery to non-EEA countries as established in Regulation (EU) 2024/1157. In other words, the ban takes effect on its scheduled date in its original, unmodified form.

This question resolves **No** if, by 23:59 UTC on May 21, 2026, any of the following has been published in the Official Journal of the European Union:
- A formal amendment to Regulation (EU) 2024/1157 (including but not limited to the proposed Switzerland exemption from the April 29, 2026 Commission proposal);
- A new delegated or implementing act that delays or modifies the application of the mixed municipal waste export ban;
- Any other binding EU legislative instrument that grants a delay or exemption to this ban for Switzerland or any other non-EEA country.

"Mixed municipal waste" is defined per Article 4(3) of Regulation (EU) 2024/1157 as waste collected from private households, from other waste producers, or from both, including waste that has been subject to a waste treatment operation that has not substantially altered its properties (including refuse-derived fuels processed from mixed municipal waste).

The sole authoritative resolution source is the Official Journal of the European Union, accessible at https://eur-lex.europa.eu/.

**Pre-cutoff background**

Regulation (EU) 2024/1157 on shipments of waste entered into force on May 20, 2024, and its main provisions apply from May 21, 2026 (Article 86(2)) [[PDF] REGULATION (EU) 2024/1157 OF THE EUROPEAN PARLIAMENT ...](https://cdn.climatepolicyradar.org/navigator/EUR/2024/regulation-eu-2024-1157-on-shipments-of-waste_27b4e88e1828606abeec67faba89794f.pdf). Among these provisions is a prohibition on the export of mixed municipal waste destined for recovery to countries outside the European Economic Area (EEA).

Under this regulation, "mixed municipal waste" refers to waste collected from private households, from other waste producers, or from both, as well as waste that has been subject to a waste treatment operation that has not substantially altered its properties, including refuse-derived fuels processed from mixed municipal waste (Article 4(3) of Regulation (EU) 2024/1157) [[PDF] REGULATION (EU) 2024/1157 OF THE EUROPEAN PARLIAMENT ...](https://cdn.climatepolicyradar.org/navigator/EUR/2024/regulation-eu-2024-1157-on-shipments-of-waste_27b4e88e1828606abeec67faba89794f.pdf).

On April 29, 2026, the European Commission proposed a targeted amendment to the Waste Shipment Regulation to allow continued export of mixed municipal waste for recovery (including recycling and energy recovery) to Switzerland [https://environment.ec.europa.eu/news/commission-proposes-change-waste-shipment-rules-2026-04-29_en](https://environment.ec.europa.eu/news/commission-proposes-change-waste-shipment-rules-2026-04-29_en). The rationale is that border regions in Austria, France, Germany, and Italy rely on Swiss waste treatment facilities, and the ban would force waste to be transported over longer distances within the EU [https://environment.ec.europa.eu/news/commission-proposes-change-waste-shipment-rules-2026-04-29_en](https://environment.ec.europa.eu/news/commission-proposes-change-waste-shipment-rules-2026-04-29_en). As of May 1, 2026, this proposal requires discussion and adoption by the European Parliament and the Council before it can take effect.

The key uncertainty is whether this amendment—or any other formal delay or exemption—can be adopted and published in the Official Journal of the European Union before the May 21, 2026 deadline. EU legislative procedures typically take weeks to months, making adoption within ~3 weeks exceptionally fast but not impossible for an urgent, targeted amendment.

**Exact later resolution packet**

YES. The controlling criterion is publication in the Official Journal by 23:59 UTC on 21 May 2026, not mere Commission proposal, Council/Parliament discussion, or adoption. The relevant EUR-Lex page for Regulation (EU) 2024/1157 confirms that the original regulation was published in the Official Journal on 30 April 2024 and that its main provisions apply from 21 May 2026; it also shows the April 2026 Switzerland measure only as “Amendment proposed by 52026PC0183,” not as an adopted/published amendment [https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1157](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1157).

The specific Switzerland document, CELEX 52026PC0183, is titled “Proposal for a REGULATION OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL amending Regulation (EU) 2024/1157 as regards the prohibition to export mixed municipal waste destined for recovery,” dated Brussels, 29.4.2026, and identified as COM(2026) 183 final; EUR-Lex presents it as a proposal, with no Official Journal publication information for an enacted regulation [https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52026PC0183](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52026PC0183). A proposal is not a binding legislative instrument and does not itself delay, modify, or exempt the ban.

I also checked for other listed subsequent amendments, delegated/implementing acts, corrigenda, or related instruments on the EUR-Lex Regulation (EU) 2024/1157 page. EUR-Lex did not list any binding act published by the deadline that delayed, modified, or created an exemption to the mixed-municipal-waste export ban for Switzerland or any other non-EEA country; the other items noted there were not such a delay/exemption, while the Switzerland item remained only a proposed amendment [https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1157](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1157). Direct EUR-Lex URLs used: original Regulation entry https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1157 ; Switzerland proposal https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52026PC0183 ; EUR-Lex search result URL for the Switzerland-related query https://eur-lex.europa.eu/search.html?type=advanced&DTS_DOM=ALL&DTS_SUBDOM=ALL_ALL&SUBDOM_INIT=ALL_ALL&CT_1_CODED=DECH&lang=en . Therefore, as of 23:59 UTC on 21 May 2026, no qualifying Official Journal publication existed, so the ban took effect as scheduled in its unmodified form.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-113. `a0321afa-c75a-51e9-abed-473012f40eba`

- Present date: `2026-04-30 17:15:08.709908`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Lamine Yamal be included in Spain's final World Cup squad submitted to FIFA by June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if Lamine Yamal (born July 13, 2007; FIFA player profile: https://www.fifa.com/fifaplus/en/players/lamine-yamal) is named in Spain's final squad list of up to 26 players for the 2026 FIFA World Cup, as published by FIFA on or after April 30, 2026, and by June 1, 2026 (23:59 UTC).

This question resolves as **No** if Lamine Yamal is not included in Spain's final squad list by that deadline.

The official resolution source is the FIFA squad list page for the 2026 FIFA World Cup, expected to be published at https://www.fifa.com/fifaplus/en/tournaments/mens/worldcup/canadamexicousa2026 and mirrored on the Wikipedia squad page at https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_squads.

Per the official FIFA World Cup 2026 Regulations (https://digitalhub.fifa.com/m/636f5c9c6f29771f/original/FWC2026_regulations_EN.pdf), the "final 26-player squad" refers to the squad of between 23 and 26 players (including three goalkeepers) that each participating member association must submit to FIFA by June 1, 2026 (23:59 UTC) [2026 FIFA World Cup squads - Wikipedia](https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_squads).

**Injury replacements:** If Lamine Yamal is initially included in Spain's final squad but is subsequently replaced due to injury before Spain's first match (per FIFA regulations allowing replacements up to 24 hours before a team's first match [2026 FIFA World Cup squads - Wikipedia](https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_squads)), the question still resolves **Yes**, as he was included in the submitted final squad. Conversely, if Yamal is not in the original final squad but is added as an injury replacement for another player before the first match, this also counts as **Yes**.

**Pre-cutoff background**

Lamine Yamal, the 18-year-old FC Barcelona and Spain forward, suffered a hamstring injury in his left leg (biceps femoris muscle) during Barcelona's 1-0 win over Celta Vigo on April 22, 2026 [Will Lamine Yamal play World Cup 2026? What hamstring injury ...](https://www.sportingnews.com/us/soccer/news/will-lamine-yamal-play-world-cup-2026-injury-spain/6eb978fdb910c8f7613dac22). On April 23, 2026, FC Barcelona confirmed he would miss the remainder of the club season but indicated he is expected to be available for the 2026 FIFA World Cup. Reports suggest the injury is a Grade 2 hamstring strain, which typically requires a 4–6 week recovery period [Will Lamine Yamal play World Cup 2026? What hamstring injury ...](https://www.sportingnews.com/us/soccer/news/will-lamine-yamal-play-world-cup-2026-injury-spain/6eb978fdb910c8f7613dac22).

Yamal was a key player in Spain's Euro 2024 triumph and is considered one of Spain's most important attacking players. His fitness for the World Cup is uncertain given the tight recovery timeline.

For the 2026 FIFA World Cup (June 11 – July 19, 2026), national teams must submit a provisional list of 35–55 players by May 11, 2026, and a final squad of 23 to 26 players (including three goalkeepers) by June 1, 2026 [2026 FIFA World Cup squads - Wikipedia](https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_squads). Injured players on the final squad list may be replaced up to 24 hours before the team's first match, subject to medical confirmation [2026 FIFA World Cup squads - Wikipedia](https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_squads). Spain's first World Cup match is scheduled for around June 12, 2026.

As of April 30, 2026, Yamal is undergoing conservative treatment for his hamstring injury. Multiple sources report he is expected to recover in time for the World Cup, but there remains genuine uncertainty about whether Spain's coaching staff will risk including a player who has not trained fully with the squad.

**Exact later resolution packet**

The question resolves YES because Lamine Yamal was named in Spain's final 26-man squad for the 2026 FIFA World Cup.

- The official FIFA squad announcement article ("Spain squad announcement | FIFA World Cup 2026", published May 25, 2026) confirms that coach Luis de la Fuente named a 26-man squad that explicitly includes Lamine Yamal under the Forwards section [Spain squad announcement | FIFA World Cup 2026](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/spain-squad-announcement-luis-de-la-fuente).
- The Wikipedia mirror page "2026 FIFA World Cup squads" lists Lamine Yamal as a forward (No. 19) in Spain's final squad, and states Spain announced their final squad on May 25, 2026 [2026 FIFA World Cup squads - Wikipedia](https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_squads).
- This announcement occurred before the June 1, 2026 (23:59 UTC) deadline. Spain's submitted final squad included Yamal despite his hamstring injury, satisfying the YES criterion.
- Per the resolution criteria, even if Yamal were later replaced due to injury before Spain's first match, the question still resolves YES because he was in the submitted final squad. The evidence shows he was indeed included [Spain squad announcement | FIFA World Cup 2026](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/spain-squad-announcement-luis-de-la-fuente) [2026 FIFA World Cup squads - Wikipedia](https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_squads).

URLs:
- FIFA: https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/spain-squad-announcement-luis-de-la-fuente
- Wikipedia: https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_squads

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-114. `cc65c42b-a42c-5592-9f73-795582542f79`

- Present date: `2026-05-07 16:42:34.997191`
- Source cutoff boundary: `2026-05-08` (encodes end of UTC day `2026-05-07`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will a named Atlantic tropical storm or hurricane form between May 7 and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if at least one tropical or subtropical cyclone is assigned a name by the National Hurricane Center (NHC) in the Atlantic basin, with its formation (i.e., the issuance of the first NHC advisory designating it as a named storm) occurring on or after May 7, 2026, and no later than 23:59 UTC on June 30, 2026. Otherwise, it resolves **No**.

A "named storm" includes any tropical storm, subtropical storm, or hurricane as classified by the NHC per [NOAA definitions](https://www.nhc.noaa.gov/aboutgloss.shtml).

**Resolution source:** The [National Hurricane Center (NHC)](https://www.nhc.noaa.gov/) advisory archive, accessible at https://www.nhc.noaa.gov/archive/2026/. The NHC is the authoritative source for Atlantic tropical cyclone classification and naming. If a named storm forms during the resolution window, it will appear in the NHC's active storm advisories and/or archived advisories for the 2026 season.

**Pre-cutoff background**

The Atlantic hurricane season officially runs from June 1 to November 30, but named storms can and do form outside this window. In recent years, early-season activity has become increasingly common—7 of the 10 years prior to 2025 had at least one named storm before June 1. Historically, pre-July named storms have occurred in roughly 40–60% of all years, though this rate has been increasing in recent decades.

**ENSO Status (as of April 2026):** ENSO-neutral conditions are currently present. The NOAA Climate Prediction Center's April 9, 2026 diagnostic discussion indicates ENSO-neutral is favored through April–June 2026 (80% chance), with El Niño likely to emerge during May–July 2026 (61% chance) and persist through at least the end of 2026 [https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_advisory/ensodisc.shtml](https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_advisory/ensodisc.shtml). El Niño conditions typically increase vertical wind shear across the tropical Atlantic, which suppresses tropical cyclone formation and tends to delay the start of the hurricane season.

**Atlantic Sea Surface Temperatures (SSTs):** Global SSTs have been running generally above average. The WMO Global Seasonal Climate Update for May–July 2026 notes above-normal sea surface temperatures across large portions of the Atlantic. Warm SSTs provide more energy for tropical cyclone development and could partially offset El Niño's suppressive effects. Daily SST monitoring for the Atlantic Hurricane Main Development Region (MDR, 10–20°N, 20–85°W) is available via the [Climate Reanalyzer](https://climatereanalyzer.org/clim/sst_daily/).

**Key tension for forecasters:** The developing El Niño would typically suppress early-season Atlantic activity, but anomalously warm Atlantic SSTs and a recent trend toward earlier storm formation create genuine uncertainty about whether a named storm will form before July 1, 2026.

**Definitions:**
- A **named storm** is a tropical or subtropical cyclone that has been assigned a name by the National Hurricane Center (NHC). Per [NOAA/NHC standards](https://www.nhc.noaa.gov/aboutgloss.shtml), a **tropical storm** is a tropical cyclone with maximum sustained winds of 39–73 mph (34–63 knots), and a **hurricane** is a tropical cyclone with maximum sustained winds of 74 mph (64 knots) or greater.
- The NHC names tropical cyclones once they reach tropical storm strength or are classified as subtropical storms.

**Exact later resolution packet**

RESOLUTION: YES (1).

The question resolves YES if at least one tropical or subtropical cyclone was assigned a name by the NHC in the Atlantic basin, with its first named-storm advisory issued on or after May 7, 2026 and no later than 23:59 UTC on June 30, 2026.

Key evidence:
- The NHC 2026 advisory archive (https://www.nhc.noaa.gov/archive/2026/) lists Tropical Storm ARTHUR as the first named Atlantic storm of the 2026 season [https://www.nhc.noaa.gov/archive/2026/](https://www.nhc.noaa.gov/archive/2026/). Arthur was the only/first Atlantic named storm in the archive at that time [https://www.nhc.noaa.gov/archive/2026/](https://www.nhc.noaa.gov/archive/2026/).
- Arthur's advisory archive (https://www.nhc.noaa.gov/archive/2026/ARTHUR.shtml) shows the system's advisory sequence beginning June 16, 2026, first as "Potential Tropical Cyclone One," then developing into Tropical Storm Arthur [Tropical Storm ARTHUR Advisory Archive - National Hurricane Center](https://www.nhc.noaa.gov/archive/2026/ARTHUR.shtml).
- Advisory #4 (issued 0900 UTC June 17, 2026) still designated the system as "Potential Tropical Cyclone One" — i.e., NOT yet a named storm [https://www.nhc.noaa.gov/archive/2026/al01/al012026.public.004.shtml](https://www.nhc.noaa.gov/archive/2026/al01/al012026.public.004.shtml).
- Advisory #5 (https://www.nhc.noaa.gov/archive/2026/al01/al012026.public.005.shtml), issued 1000 AM CDT = 1500 UTC on June 17, 2026, was the first advisory to explicitly designate the system as "Tropical Storm Arthur," a tropical storm (named storm) [https://www.nhc.noaa.gov/archive/2026/al01/al012026.public.005.shtml](https://www.nhc.noaa.gov/archive/2026/al01/al012026.public.005.shtml).

Timing check: The first named-storm advisory (Tropical Storm Arthur) was issued at 1500 UTC on June 17, 2026. This is on/after May 7, 2026 and before 23:59 UTC June 30, 2026 — squarely within the resolution window.

Classification check: Arthur was classified as a Tropical Storm (not merely a tropical depression, and not merely the pre-named "Potential Tropical Cyclone One" phase), satisfying the requirement that the name be assigned to a tropical/subtropical storm or hurricane [https://www.nhc.noaa.gov/archive/2026/al01/al012026.public.005.shtml](https://www.nhc.noaa.gov/archive/2026/al01/al012026.public.005.shtml) [https://www.nhc.noaa.gov/archive/2026/al01/al012026.public.004.shtml](https://www.nhc.noaa.gov/archive/2026/al01/al012026.public.004.shtml).

No earlier named Atlantic storm existed in the window; Arthur was the season's first named storm [https://www.nhc.noaa.gov/archive/2026/](https://www.nhc.noaa.gov/archive/2026/) [2026 Atlantic hurricane season - Wikipedia](https://en.wikipedia.org/wiki/2026_Atlantic_hurricane_season). Therefore the condition is met and the question resolves YES.

Direct URLs:
- NHC 2026 advisory archive: https://www.nhc.noaa.gov/archive/2026/
- Arthur advisory archive: https://www.nhc.noaa.gov/archive/2026/ARTHUR.shtml
- First "Tropical Storm Arthur" advisory (Advisory 5, 1500 UTC June 17, 2026): https://www.nhc.noaa.gov/archive/2026/al01/al012026.public.005.shtml

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-115. `d2fd04b8-f6d3-589d-bf27-12ad2ad89b68`

- Present date: `2026-05-12 21:14:52.362069`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the COB (Central Obrera Boliviana) officially call off or suspend its May 2026 indefinite general strike before July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 10, 2026, and before July 1, 2026 (23:59 UTC), the Central Obrera Boliviana (COB) officially calls off, suspends, or lifts its indefinite general strike that began on May 1, 2026. An "official" act is defined as either: (a) a formal public statement or announcement by the COB Executive Secretary (Secretario Ejecutivo) or the COB's official communication channels (e.g., their official social media accounts or press conferences), or (b) credible reporting by at least one major news outlet confirming the strike has been officially suspended or ended, from sources such as: El Deber (https://eldeber.com.bo/), La Razón (https://www.la-razon.com/), Reuters (https://www.reuters.com/), Associated Press (https://apnews.com/), AFP, Al Jazeera (https://www.aljazeera.com/), or BBC.

The question resolves as **No** if: (1) the strike remains officially active as of 23:59 UTC on June 30, 2026; (2) the COB transitions to a different form of protest (e.g., intermittent stoppages or marches) without explicitly announcing the suspension or end of the "indefinite general strike"; or (3) no credible reporting confirms an official suspension or cancellation.

Note: A temporary pause in activities (e.g., for a holiday or negotiation session) does not count unless the COB explicitly announces the strike is suspended or called off.

**Pre-cutoff background**

Bolivia's main trade union federation, the Central Obrera Boliviana (COB, https://en.wikipedia.org/wiki/Bolivian_Workers%27_Center), declared an indefinite general strike beginning May 1, 2026, amid an ongoing economic crisis marked by currency shortages and the removal of decades-old fuel subsidies [Protests in Bolivia escalate amid economic turmoil and policy ...](https://www.aljazeera.com/economy/2026/5/7/protests-in-bolivia-escalate-amid-economic-turmoil-and-policy-demands). The COB's key demands include a 20% increase to the national minimum wage, increases to pensions, and salary cuts for government officials [Protests in Bolivia escalate amid economic turmoil and policy ...](https://www.aljazeera.com/economy/2026/5/7/protests-in-bolivia-escalate-amid-economic-turmoil-and-policy-demands). President Rodrigo Paz's center-right government has firmly rejected the 20% wage demand, with Paz stating "If you want to raise salaries, first create jobs" and that he is "not afraid of mobilizations" [Protests in Bolivia escalate amid economic turmoil and policy ...](https://www.aljazeera.com/economy/2026/5/7/protests-in-bolivia-escalate-amid-economic-turmoil-and-policy-demands)[Bolivia Confirms $3.3B IMF Talks as National Strike Paralyzes Cities](https://www.riotimesonline.com/bolivia-imf-3-3-billion-cob-strike-paz-fuel-may-2026/). As of May 11, 2026, the strike remains active, with protests, road blockades, and clashes with police reported across major cities including La Paz, El Alto, Cochabamba, Oruro, and Sucre [Protests in Bolivia escalate amid economic turmoil and policy ...](https://www.aljazeera.com/economy/2026/5/7/protests-in-bolivia-escalate-amid-economic-turmoil-and-policy-demands). The government has signaled openness to dialogue but has not made a specific counter-offer on wages [Bolivia Confirms $3.3B IMF Talks as National Strike Paralyzes Cities](https://www.riotimesonline.com/bolivia-imf-3-3-billion-cob-strike-paz-fuel-may-2026/). Notably, the COB previously called an indefinite strike in late December 2025 over the same fuel subsidy issue (the "Gasolinazo"), which was called off in January 2026 after approximately three weeks following negotiations. Bolivia is also in talks with the IMF over a $3.3 billion program, adding fiscal pressure that may constrain the government's ability to meet wage demands [Bolivia Confirms $3.3B IMF Talks as National Strike Paralyzes Cities](https://www.riotimesonline.com/bolivia-imf-3-3-billion-cob-strike-paz-fuel-may-2026/).

**Exact later resolution packet**

RESOLUTION: YES (1).

The COB (Central Obrera Boliviana), through its Executive Secretary (Secretario Ejecutivo) Mario Argollo, officially lifted/suspended its indefinite general strike on the night of Friday, June 19, 2026 — squarely inside the resolution window (on/after May 10, 2026 and before July 1, 2026, 23:59 UTC). This satisfies criterion (a) (a formal public statement by the COB Executive Secretary) and criterion (b) (credible reporting by multiple listed outlets).

KEY EVIDENCE:
- La Razón (a specifically listed source): After signing an agreement with the government, Argollo declared: "A partir de este momento se están levantando las medidas de presión a nivel nacional, con un compromiso del Gobierno de cumplir de manera inmediata todo lo que se ha suscrito." The report says this ended 50 days of mobilizations and blockades. URL: https://larazon.bo/nacional/2026/06/19/tras-acuerdo-con-el-gobierno-mario-argollo-instruye-levantar-bloqueos/ [Tras acuerdo con el Gobierno, Mario Argollo instruye levantar ...](https://larazon.bo/nacional/2026/06/19/tras-acuerdo-con-el-gobierno-mario-argollo-instruye-levantar-bloqueos/)
- Associated Press (a listed source, via Boston Herald reprint): "La Central Obrera Boliviana (COB) pactó el viernes en la noche una tregua con el gobierno y se desmarcó de los sindicatos..." — i.e., the COB entered a truce, distanced itself from the ongoing protests, and Argollo called for withdrawal of measures. URL: https://www.bostonherald.com/2026/06/19/central-obrera-se-desmarca-de-las-protestas-y-pacta-con-el-gobierno-de-bolivia/ [Central Obrera se desmarca de las protestas y pacta con el ...](https://www.bostonherald.com/2026/06/19/central-obrera-se-desmarca-de-las-protestas-y-pacta-con-el-gobierno-de-bolivia/)
- Deutsche Welle: Argollo stated "A partir de este momento se están levantando las medidas de presión a nivel nacional" after the June 19, 2026 agreement to "pacify" the country. URL: https://www.dw.com/es/gobierno-bolivia-y-cob-logran-acuerdo-tras-50-d%C3%ADas-de-crisis/a-77633527 [Gobierno Bolivia y COB logran acuerdo tras 50 días de crisis](https://www.dw.com/es/gobierno-bolivia-y-cob-logran-acuerdo-tras-50-d%C3%ADas-de-crisis/a-77633527)
- ABC Color: Confirms Argollo announced on the night of June 19, 2026 that "from this moment, the pressure measures at the national level are being lifted," following the government-COB agreement to lift the protests. URL: https://www.abc.com.py/internacionales/2026/06/20/gobierno-de-bolivia-y-central-sindical-llegan-a-acuerdo-para-levantar-las-protestas/ [Gobierno de Bolivia y central sindical llegan a acuerdo ... - ABC Color](https://www.abc.com.py/internacionales/2026/06/20/gobierno-de-bolivia-y-central-sindical-llegan-a-acuerdo-para-levantar-las-protestas/)
- Agencia Boliviana de Información (ABI, state agency): "Argollo instruye levantar los bloqueos..." and the Gobierno-COB accord to restore normalcy and end the confrontation. URL: https://abi.bo/argollo-instruye-levantar-los-bloqueos-y-exhorta-a-las-20-provincias-a-sumarse-al-dialogo-para-pacificar-el-pais/ and https://abi.bo/acuerdo-gobierno-cob-fija-una-agenda-de-trabajo-para-la-pacificacion-y-la-atencion-de-demandas-sociales-y-economicas/ [Acuerdo Gobierno-COB fija una agenda de trabajo para la ... - ABI](https://abi.bo/acuerdo-gobierno-cob-fija-una-agenda-de-trabajo-para-la-pacificacion-y-la-atencion-de-demandas-sociales-y-economicas/)
- Wikipedia (2026 Bolivian protests): On June 19, 2026 the Paz administration and the COB reached an agreement to "move toward the suspension of the protest measures," and by June 23, 2026 the Bolivian Highway Administration announced all blockades had been cleared. URL: https://en.wikipedia.org/wiki/2026_Bolivian_protests [2026 Bolivian protests - Wikipedia](https://en.wikipedia.org/wiki/2026_Bolivian_protests)
- Reuters (a listed source): Confirms Bolivia signed a deal with the COB on June 19, 2026 after 50 days; Argollo called it a "first step to pacifying the country." Reuters emphasized the broader conflict was "far from over" because rural groups aligned with Evo Morales (NOT part of the COB) kept blocking roads. This does not contradict the COB's own strike being lifted. URL: https://www.reuters.com/world/americas/bolivia-signs-deal-with-cob-labor-union-after-50-days-anti-govt-protests-2026-06-19/ [Bolivia signs deal with labor union after 50 days of anti-government ...](https://www.reuters.com/world/americas/bolivia-signs-deal-with-cob-labor-union-after-50-days-anti-govt-protests-2026-06-19/)

WHY THIS IS NOT A "NO" UNDER THE EXCLUSIONS:
- This was not a mere transition to a "different form of protest" (exclusion 2). The COB Executive Secretary explicitly and nationally lifted the pressure measures — the indefinite general strike ("paro/huelga general indefinido") is the principal "medida de presión," so lifting all pressure measures nationwide is an explicit end of the strike. Even hostile/critical leftist coverage frames this unambiguously as the COB "calling off the strike": the International Socialist League wrote "The decision by the COB leadership, headed by Mario Argollo, to call off the strike was a tragedy for the activists and strikers" (https://lis-isl.org/en/2026/06/news-from-bolivia-the-cob-and-the-paz-administration-sign-an-agreement/) [News from Bolivia: The COB and the Paz Administration Sign an ...](https://lis-isl.org/en/2026/06/news-from-bolivia-the-cob-and-the-paz-administration-sign-an-agreement/), and WSWS described the COB as committing to "lift the 'pressure measures' and suspend the blockades" (https://www.wsws.org/en/articles/2026/06/26/hoed-j26.html; https://www.wsws.org/es/articles/2026/06/29/a432-j29.html).
- It was not a mere temporary holiday/negotiation pause (the Note exclusion). The COB signed a formal peace/pacification agreement with the government establishing sectoral dialogue tables to replace the strike, and instructed lifting of measures nationwide effective immediately.

The residual continuation of roadblocks by campesino sectors aligned with Evo Morales (e.g., Túpac Katari, Chapare cocaleros) does not affect resolution, because those groups are not the COB, and the COB itself distanced itself from them and lifted its own measures. Therefore the COB officially called off/suspended its May 2026 indefinite general strike before July 1, 2026 → resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-116. `f3d67bd2-328e-5071-bbb7-9488766b1c0b`

- Present date: `2026-05-29 06:44:48.937876`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the U.S. Supreme Court rule in favor of the respondent (Isabella County) in Pung v. Isabella County (No. 25-95)?

**Resolution criteria**

This question resolves **Yes** if the Supreme Court of the United States issues an opinion in Pung v. Isabella County (No. 25-95) that rules in favor of the respondent, Isabella County, on the [Takings Clause](https://en.wikipedia.org/wiki/Takings_Clause) question. Specifically, a "ruling in favor of the respondent" means an **affirmance** of the Sixth Circuit's judgment below, or any other disposition that upholds the constitutionality of the county's retention of surplus foreclosure proceeds against the petitioner's Takings Clause challenge.

This question resolves **No** if the Court reverses or vacates the Sixth Circuit's judgment in a manner that favors the petitioner on the Takings Clause question (e.g., holding that the practice constitutes an unconstitutional taking).

**Special cases:**
- If the Court issues a **split ruling** (e.g., ruling for the respondent on the Takings Clause but for the petitioner on other grounds, or remanding on some issues while affirming on others), this question resolves based solely on the Court's disposition of the Takings Clause issue. If the majority opinion affirms the Sixth Circuit on the Takings Clause question, this resolves Yes; if it reverses on the Takings Clause question, this resolves No.
- If the case is **dismissed as improvidently granted (DIG)**, this question resolves **Yes**, as the Sixth Circuit's pro-respondent ruling would remain in effect.
- If no opinion is issued by July 1, 2026, 11:59 PM UTC, this question resolves **ambiguous** and is voided.

**Resolution source:** The official Supreme Court opinions page at https://www.supremecourt.gov/opinions/slipopinion/25 or the SCOTUSblog case page at https://www.scotusblog.com/cases/case-files/pung-v-isabella-county-michigan/.

**Pre-cutoff background**

Pung v. Isabella County, Michigan (No. 25-95) is a case before the Supreme Court of the United States concerning whether tax-foreclosure auction sales that result in the government retaining surplus value beyond the tax debt owed violate the [Takings Clause](https://en.wikipedia.org/wiki/Takings_Clause) of the Fifth Amendment. The [petitioner](https://en.wikipedia.org/wiki/Petitioner) (the party asking the Supreme Court to review the case), Michael Pung, challenges the constitutionality of Isabella County's retention of surplus proceeds from the foreclosure sale of his property. The [respondent](https://en.wikipedia.org/wiki/Respondent) is Isabella County, Michigan, which defended the practice and prevailed in the U.S. Court of Appeals for the Sixth Circuit.

As of May 12, 2026, the case was argued on February 25, 2026, but no opinion has yet been released [https://www.scotusblog.com/cases/case-files/pung-v-isabella-county-michigan/](https://www.scotusblog.com/cases/case-files/pung-v-isabella-county-michigan/). The Supreme Court's current term ends in late June or early July 2026, so an opinion is expected by that time.

SCOTUSblog's oral argument analysis noted that justices appeared broadly skeptical of the petitioner's Takings Clause challenge, with Justices Thomas, Sotomayor, Kagan, Jackson, Barrett, and Kavanaugh all expressing reservations about the petitioner's core theory (see [SCOTUSblog argument analysis](https://www.scotusblog.com/2026/02/justices-appear-dubious-of-challenge-to-constitutionality-of-foreclosure-sales/)). However, some justices (notably Sotomayor and Gorsuch) appeared concerned by the procedural facts of the case, creating uncertainty about whether the Court might craft a narrow ruling favoring the petitioner on alternative grounds.

**Exact later resolution packet**

RESOLUTION: YES (1).

TIMELINESS CHECK: The Supreme Court issued its opinion in Pung v. Isabella County (No. 25-95) on June 23, 2026 — before the July 1, 2026, 11:59 PM UTC deadline. This is confirmed by the official slip opinion (https://www.supremecourt.gov/opinions/25pdf/25-95_dc8e.pdf) [[PDF] 25-95 Pung v. Isabella County (06/23/2026) - Supreme Court](https://www.supremecourt.gov/opinions/25pdf/25-95_dc8e.pdf) and the SCOTUSblog case page which states "Vacated and remanded, 9-0, in an opinion by Samuel Alito on Jun 23, 2026" (https://www.scotusblog.com/cases/case-files/pung-v-isabella-county-michigan/) [https://www.scotusblog.com/cases/case-files/pung-v-isabella-county-michigan/](https://www.scotusblog.com/cases/case-files/pung-v-isabella-county-michigan/). Because an opinion was issued before the deadline, the question is NOT annulled.

TAKINGS CLAUSE OUTCOME (the dispositive issue): The Court ruled in favor of the respondent, Isabella County, on the Takings Clause question. It rejected the petitioner's core theory that taking/selling a home and keeping the "surplus value" (the gap between fair market value and the auction price) as a windfall violates the Takings Clause. The Court held that "the proper baseline for measuring 'just compensation' following a tax sale is the auction sale price, not the property's hypothetical fair market value, at least when the sale is fairly conducted in light of the country's history of tax sales" [[PDF] 25-95 Pung v. Isabella County (06/23/2026) - Supreme Court](https://www.supremecourt.gov/opinions/25pdf/25-95_dc8e.pdf). SCOTUSblog headlined the decision "Justices reject constitutional attack on foreclosure rules," reporting that the decision "squarely rejects an argument that the longstanding use of tax foreclosure sales as a method to collect unpaid real-estate taxes violates the takings clause of the Fifth Amendment or the excessive fines clause of the Eighth Amendment," with Alito writing that "the auction price is the proper baseline" (https://www.scotusblog.com/2026/06/justices-reject-constitutional-attack-on-foreclosure-rules/) [https://www.scotusblog.com/2026/06/justices-reject-constitutional-attack-on-foreclosure-rules/](https://www.scotusblog.com/2026/06/justices-reject-constitutional-attack-on-foreclosure-rules/). This is a disposition that upholds the constitutionality of the county's practice against the petitioner's Takings Clause challenge — satisfying the YES criterion.

AFFIRMED vs. VACATED CLARIFICATION (per checklist): The overall final judgment line reads: "The judgment of the Sixth Circuit is vacated, and the case is remanded for further proceedings consistent with this opinion" [[PDF] 25-95 Pung v. Isabella County (06/23/2026) - Supreme Court](https://www.supremecourt.gov/opinions/25pdf/25-95_dc8e.pdf). However, this vacatur was NOT "in a manner that favors the petitioner on the Takings Clause question." The Court did NOT hold that the practice is an unconstitutional taking; it rejected that claim. The vacatur/remand was solely to let the Sixth Circuit consider Pung's "newfound procedural arguments" (e.g., fairness of the sale procedure) that fell outside the question presented — the opinion states: "We will not resolve any of Pung's newfound procedural arguments. On remand, the Sixth Circuit may decide whether they were properly preserved in that court, and, if they were, may entertain Pung's arguments" [[PDF] 25-95 Pung v. Isabella County (06/23/2026) - Supreme Court](https://www.supremecourt.gov/opinions/25pdf/25-95_dc8e.pdf). On the Takings Clause question itself, the majority agreed with the Sixth Circuit (auction-price baseline) and rejected Pung's windfall theory — i.e., it did NOT reverse on the Takings Clause question.

APPLYING THE RESOLUTION CRITERIA: The criteria state that a split/mixed disposition resolves "based solely on the Court's disposition of the Takings Clause issue": YES if the majority affirms the Sixth Circuit on the Takings Clause question, NO only if it reverses on the Takings Clause question in a manner favoring the petitioner (e.g., holding the practice is an unconstitutional taking). Here the Court rejected the Takings Clause challenge and upheld the county's practice, with a technical vacate/remand only on unrelated procedural preservation issues. This maps to YES.

CONCLUSION: Resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-117. `e69889d5-1620-5024-8a0c-9bc3bfc047fd`

- Present date: `2026-05-03 04:11:27.456206`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will California's AB 2694 pass the State Assembly by June 1, 2026?

**Resolution criteria**

This question resolves YES if California Assembly Bill 2694 (2025–2026 session) passes the California State Assembly (i.e., receives a majority floor vote and is ordered to the Senate) on or before June 1, 2026, at 23:59 Pacific Time (UTC-7). It resolves NO otherwise.

Legislative actions taken before May 1, 2026 (such as committee passage) are counted as part of the bill's progression, but the specific resolving event—passage of the Assembly floor vote—must occur on or after May 1, 2026 and no later than June 1, 2026.

Resolution is determined by the official bill status page on the California Legislative Information website: https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260AB2694. If the History tab shows the bill passed the Assembly (e.g., "Read third time. Passed." or "Ordered to the Senate") by the deadline, the question resolves YES.

**Pre-cutoff background**

California has multiple active bills aimed at expanding community college baccalaureate degree programs. AB 2694 (Alvarez) would create a statewide baccalaureate degree program for community colleges, while AB 2136 (Pacheco) would authorize a baccalaureate program specifically at Cerritos Community College District. Governor Newsom has vetoed three similar bills in prior sessions, and the UC and CSU systems have opposed expansion efforts.

As of May 1, 2026, AB 2694 is the more advanced of the two bills. It was amended and re-referred to the Assembly Appropriations Committee on April 27, 2026 [https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260AB2694](https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260AB2694). AB 2136 is less advanced—it had its first committee hearing on April 21, 2026 and remains in the Assembly Higher Education Committee [Bill Status - AB-2136 Community colleges](https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260AB2136).

The California legislative session runs through September 2026. The Assembly deadline to pass bills out of the house of origin is typically in late May or early June. AB 2694 still needs to clear Appropriations and pass an Assembly floor vote. Given Newsom's veto history and UC/CSU opposition, there is genuine uncertainty about whether the bill will advance on schedule. AB 2136 is further behind and unlikely to pass the Assembly by June 1.

**Exact later resolution packet**

The question resolves YES (1). According to the official California Legislative Information bill status/history page for AB 2694 (2025–2026 session), the Assembly floor vote passed on 05/26/2026 with the action: "Read third time. Passed. Ordered to the Senate. (Ayes 60. Noes 11.)" [609c23]. This date (May 26, 2026) falls within the required resolution window of on/after May 1, 2026 and on/before June 1, 2026 (Pacific Time), satisfying the resolving event of passing the Assembly floor vote and being ordered to the Senate.

Supporting history sequence from the official page [609c23]:
- 05/06/26: In committee: Set, first hearing. Referred to APPR. suspense file.
- 05/14/26: From committee: Do pass. (Ayes 10. Noes 4.)
- 05/18/26: Read second time. Ordered to third reading.
- 05/26/26: Read third time. Passed. Ordered to the Senate. (Ayes 60. Noes 11.) ← resolving event
- 05/27/26: In Senate. Read first time. To Com. on RLS. for assignment.

URL used for verification: https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260AB2694

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-118. `81d4c81e-bbd1-5da2-bd1a-d4f7677ea272`

- Present date: `2026-05-02 22:27:59.848494`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

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

**Pre-cutoff background**

On April 1, 2026, SpaceX (Space Exploration Technologies Corp.) confidentially filed draft registration paperwork with the U.S. Securities and Exchange Commission (SEC), setting the stage for what could be the largest IPO in history at an estimated valuation of $1.75–$2 trillion [SpaceX's public IPO filing confirms Musk and insiders retain ... - TNW](https://thenextweb.com/news/spacex-ipo-s1-musk-voting-control). A confidential filing allows a company to submit its IPO documents privately and receive SEC feedback before making anything public.

As of May 1, 2026, the public S-1 registration statement has not yet appeared on the SEC's EDGAR filing system under SpaceX's name. Various analyst estimates placed the public S-1 filing in the mid-to-late May 2026 timeframe, with a roadshow reportedly targeting the week of June 8, 2026. However, IPO timelines are notoriously fluid and subject to delays from regulatory review, market conditions, or company decisions. The TNW reported on April 21, 2026 that certain prospectus details had become publicly known [SpaceX's public IPO filing confirms Musk and insiders retain ... - TNW](https://thenextweb.com/news/spacex-ipo-s1-musk-voting-control), but the formal S-1 registration statement filing on EDGAR — the definitive legal record — may not yet have occurred.

SpaceX's confidential filing on April 1 is distinct from a public S-1 filing. The public S-1 is the document that becomes available on SEC EDGAR for all investors to read, marking a critical milestone in the IPO process before the roadshow and pricing can proceed.

**Exact later resolution packet**

The question resolves YES.

Resolution criteria require a public Form S-1 registration statement filed by Space Exploration Technologies Corp. (SpaceX) to appear on SEC EDGAR on or after April 30, 2026 12:00 AM ET and before June 1, 2026 11:59 PM ET.

Evidence: SEC EDGAR shows that Space Exploration Technologies Corp. (CIK 0001181412) filed a Form S-1 on May 20, 2026, under SEC Accession Number 0001628280-26-036936, File No. 333-296070, accepted 2026-05-20 16:40:21 ET. The EDGAR filing index explicitly lists "Filing Date: 2026-05-20" and "Type: S-1 | Act: 33." (Source: https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm). The SEC full-text S-1 search results for "Space Exploration Technologies" likewise list this S-1 dated 2026-05-20 [https://efts.sec.gov/LATEST/search-index?q=%22Space+Exploration+Technologies%22&forms=S-1](https://efts.sec.gov/LATEST/search-index?q=%22Space+Exploration+Technologies%22&forms=S-1) [https://efts.sec.gov/LATEST/search-index?q=%22Space Exploration Technologies%22&forms=S-1](https://efts.sec.gov/LATEST/search-index?q=%22Space Exploration Technologies%22&forms=S-1).

The actual registration statement document confirms it is a "FORM S-1 REGISTRATION STATEMENT UNDER THE SECURITIES ACT OF 1933" for Space Exploration Technologies Corp. (https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/spaceexplorationtechnologi.htm).

This is a genuine Form S-1 (not S-1/A), filed by the correctly named entity "Space Exploration Technologies Corp.", and its filing date of May 20, 2026 falls strictly within the resolution window (April 30 – June 1, 2026). This is distinct from the confidential draft registration statement reportedly submitted April 1, 2026, which would not have been publicly visible on EDGAR; the May 20 filing is the public S-1 that satisfies the criteria.

A subsequent Form S-1/A amendment was filed June 1, 2026 (Accession 0001628280-26-039276) [https://efts.sec.gov/LATEST/search-index?q=%22Space+Exploration+Technologies%22&forms=S-1](https://efts.sec.gov/LATEST/search-index?q=%22Space+Exploration+Technologies%22&forms=S-1), but the original public S-1 already appeared within the window, so the YES condition is met regardless.

Therefore the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-119. `513056b4-1fab-57a0-817f-480e1d55b703`

- Present date: `2026-05-02 19:35:07.641420`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

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

**Pre-cutoff background**

The United States formally completed its withdrawal from the World Health Organization (WHO) effective January 22, 2026, one year after President Trump signed the executive order initiating the process. The US has failed to pay approximately $260.6 million in assessed membership dues for the 2024–2025 biennium [Member States To Discuss US Withdrawal From WHO As Failure To ...](https://healthpolicy-watch.news/member-states-to-discuss-us-withdrawal-from-who-as-failure-to-pay-fees-violates-agreement/). WHO's constitution requires that withdrawing members settle all financial obligations before departure is complete, and WHO has stated it "regrets" the withdrawal. Member states have been scheduled to discuss the US withdrawal and unpaid fees at the World Health Assembly [Member States To Discuss US Withdrawal From WHO As Failure To ...](https://healthpolicy-watch.news/member-states-to-discuss-us-withdrawal-from-who-as-failure-to-pay-fees-violates-agreement/).

The 79th World Health Assembly (WHA79) is being held in Geneva, Switzerland, from 18–23 May 2026, and is the first full Assembly session since the US withdrawal took effect. The official WHA79 documents page is at https://apps.who.int/gb/e/e_wha79.html [WHA79 - World Health Organization (WHO)](https://apps.who.int/gb/e/e_wha79.html). Whether member states choose to formally address the US departure through an adopted resolution—versus handling it through quieter administrative or diplomatic channels—depends on complex geopolitical dynamics and institutional strategy. Some member states may push for a formal resolution asserting the US cannot fully withdraw until dues are paid, while others may prefer to keep the door open for re-engagement.

**Exact later resolution packet**

Adjudicated: The official text of resolution WHA79.2 (adopted 22 May 2026, within the 18-23 May session) explicitly names 'the United States of America' twice in the list of Member States in arrears in the payment of their contributions to an extent justifying Article 7, and decides their voting privileges shall be suspended at WHA80 if still in arrears. This is a formal WHA79.X resolution that specifically names the US in connection with unpaid assessed contributions, satisfying the YES criteria; the 'generic contributions' exclusion does not apply because the US is specifically named.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-120. `373def81-7e87-5a53-aa5e-eddea5ca5edc`

- Present date: `2026-05-02 17:59:39.981379`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Microsoft be actively rejecting (via SMTP 550 error) emails from bulk senders failing DMARC authentication for Outlook.com consumer domains by June 1, 2026?

**Resolution criteria**

This question resolves **YES** if, on or after May 1, 2026 (00:00 UTC), Microsoft is officially and actively rejecting — meaning returning an SMTP 5xx permanent failure error code (e.g., "550; 5.7.515 Access denied" [Outlook's New Requirements for High‐Volume Senders](https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730)) at the SMTP transaction level, as opposed to merely routing messages to the Junk/Spam folder — emails sent by **bulk senders** to Outlook.com, Hotmail.com, or Live.com consumer mailboxes that fail DMARC authentication.

Key definitions:

- **Bulk sender**: A sending domain that transmits more than 5,000 emails per day to Microsoft consumer mailboxes (Outlook.com, Hotmail.com, Live.com), as defined by Microsoft (https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730) [Outlook's New Requirements for High‐Volume Senders](https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730).

- **Rejecting**: Returning an SMTP 5xx series permanent error code (per RFC 5321, https://datatracker.ietf.org/doc/html/rfc5321#section-4.2.1) during or after the SMTP transaction, causing the message to bounce back to the sender. This is distinct from "junking," which means accepting the message at the SMTP level (returning a 2xx success code) but delivering it to the recipient's Junk/Spam folder.

- **DMARC authentication failure**: A message that does not pass DMARC validation as defined in RFC 7489 (https://datatracker.ietf.org/doc/html/rfc7489#section-4.2). DMARC passes when at least one of SPF or DKIM produces an aligned "pass" result. A DMARC "fail" occurs when neither SPF nor DKIM produces an aligned pass.

The question resolves **NO** if, as of June 1, 2026 (23:59 UTC), Microsoft's official policy for non-compliant bulk sender messages is still limited to routing them to the Junk folder without SMTP-level rejection, or if no official Microsoft communication confirms that rejection enforcement is active.

**Resolution source**: Microsoft's official Defender for Office 365 Blog at https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog or Microsoft Learn documentation at https://learn.microsoft.com. Updates to the original announcement post or subsequent posts on these platforms serve as the primary resolution source. Corroborating evidence from credible industry sources (e.g., Proofpoint, Valimail) reporting observed 550 5.7.515 bounce codes may supplement but not replace official Microsoft communications.

**Pre-cutoff background**

On April 2, 2025, Microsoft announced new authentication requirements for high-volume senders (domains sending over 5,000 emails per day to Outlook.com, Hotmail.com, and Live.com consumer mailboxes) [Outlook's New Requirements for High‐Volume Senders](https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730). The requirements mandate compliance with SPF, DKIM, and DMARC (at minimum p=none, aligned with either SPF or DKIM) [Outlook's New Requirements for High‐Volume Senders](https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730).

Microsoft's enforcement was announced in two phases: starting May 5, 2025 (UTC), non-compliant messages would be routed to the Junk folder. At a future date (to be announced), non-compliant messages would be outright rejected [Outlook's New Requirements for High‐Volume Senders](https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730). As of the last update to Microsoft's official blog post (April 30, 2025), no specific date had been confirmed for the transition from junking to rejection [Outlook's New Requirements for High‐Volume Senders](https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730).

However, some third-party sources reported that Microsoft updated its enforcement stance around April 29, 2025, potentially accelerating to outright SMTP rejection rather than junk folder routing. There is conflicting information across sources about whether full rejection enforcement is currently active as of May 1, 2026 (UTC), or whether Microsoft is still primarily routing non-compliant mail to Junk with rejection applied only in limited cases. Microsoft indicated it would announce updates on rollout schedules via future blog posts on the Microsoft Defender for Office 365 Blog [Outlook's New Requirements for High‐Volume Senders](https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730).

**Exact later resolution packet**

The question resolves YES. Microsoft's official Defender for Office 365 Blog post "Strengthening Email Ecosystem: Outlook's New Requirements for High‐Volume Senders" contains an "April 29th Update" in which Microsoft reversed its earlier junk-folder-only stance and decided to REJECT non-compliant messages. The blog explicitly strikes through the original junk-routing language ("After May 5th, 2025, Outlook will begin routing messages from high volume non‐compliant domains to the Junk folder...") and replaces it with: "we have made a decision to reject messages that don't pass the required authentication requirements," with the rejection taking effect May 5, 2025 as originally scheduled [Outlook's New Requirements for High‐Volume Senders](https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730).

Each checklist item is satisfied:
- Official Microsoft source: The Microsoft Defender for Office 365 Blog (techcommunity.microsoft.com) and Microsoft Learn/Support documentation are the basis [Outlook's New Requirements for High‐Volume Senders](https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730) [Fix NDR error "550 5.7.515" in Outlook.com - Microsoft Support](https://support.microsoft.com/en-us/topic/fix-ndr-error-550-5-7-515-in-outlook-com-34cfe8f8-6fbf-457e-9e8b-9e4dbaf4e0ef).
- SMTP 5xx permanent failure: Rejected messages return "550; 5.7.515 Access denied, sending domain [SendingDomain] does not meet the required authentication level," an SMTP 5xx permanent failure / NDR bounce — not a 2xx success followed by junk delivery [Outlook's New Requirements for High‐Volume Senders](https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730) [Fix NDR error "550 5.7.515" in Outlook.com - Microsoft Support](https://support.microsoft.com/en-us/topic/fix-ndr-error-550-5-7-515-in-outlook-com-34cfe8f8-6fbf-457e-9e8b-9e4dbaf4e0ef).
- Bulk senders defined as >5,000 emails/day to Microsoft consumer mailboxes (Outlook.com, Hotmail.com, Live.com) — this is the scope of the policy [Outlook's New Requirements for High‐Volume Senders](https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730) [Fix NDR error "550 5.7.515" in Outlook.com - Microsoft Support](https://support.microsoft.com/en-us/topic/fix-ndr-error-550-5-7-515-in-outlook-com-34cfe8f8-6fbf-457e-9e8b-9e4dbaf4e0ef).
- Enforcement active between May 1, 2026 and June 1, 2026 (23:59 UTC): Rejection took effect May 5, 2025 and has remained continuously active; the Microsoft Support page "Fix NDR error 550 5.7.515 in Outlook.com," live as of the resolution date, provides remediation instructions for this active rejection, confirming the policy remains in force [Fix NDR error "550 5.7.515" in Outlook.com - Microsoft Support](https://support.microsoft.com/en-us/topic/fix-ndr-error-550-5-7-515-in-outlook-com-34cfe8f8-6fbf-457e-9e8b-9e4dbaf4e0ef).
- Triggered by DMARC authentication failure: The rejection occurs when the sending domain fails to meet the required authentication level (SPF, DKIM, and DMARC alignment — i.e., neither SPF nor DKIM produces an aligned pass) [Outlook's New Requirements for High‐Volume Senders](https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730) [Fix NDR error "550 5.7.515" in Outlook.com - Microsoft Support](https://support.microsoft.com/en-us/topic/fix-ndr-error-550-5-7-515-in-outlook-com-34cfe8f8-6fbf-457e-9e8b-9e4dbaf4e0ef).

Source URLs:
- https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730 (April 29th Update)
- https://support.microsoft.com/en-us/topic/fix-ndr-error-550-5-7-515-in-outlook-com-34cfe8f8-6fbf-457e-9e8b-9e4dbaf4e0ef

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-121. `a0022abe-c384-5c95-bb3d-dc53e212aee1`

- Present date: `2026-05-12 19:56:34.900844`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Australian Labor Party candidate (Luke Richmond) win the 2026 Stafford state by-election?

**Resolution criteria**

This question resolves YES if the Electoral Commission of Queensland (ECQ) officially declares Luke Richmond (Australian Labor Party) as the elected member for the district of Stafford following the by-election held on May 16, 2026 (or otherwise held on or after May 10, 2026). It resolves NO if any other candidate is declared the winner.

The resolution source is the official ECQ results page at https://www.ecq.qld.gov.au/ or its dedicated results portal (https://www.ecq.qld.gov.au/elections/election-events/stafford-state-by-election). The question resolves based on the final official declaration of results. If the by-election is not held by June 30, 2026 (23:59 UTC), the question resolves NO.

All times referenced are in UTC.

**Pre-cutoff background**

The 2026 Stafford state by-election is scheduled for May 16, 2026, triggered by the death of independent MP Jimmy Sullivan on April 9, 2026 [https://en.wikipedia.org/wiki/2026_Stafford_state_by-election](https://en.wikipedia.org/wiki/2026_Stafford_state_by-election). Sullivan had originally been elected as a Labor MP but was expelled from the party in May 2025.

The electoral district of Stafford, located in Brisbane's northern suburbs, has historically been a safe Labor seat, won by Labor at every election since 2001 with at least 55% of the two-party-preferred (TPP) vote, except in 2012 [https://en.wikipedia.org/wiki/2026_Stafford_state_by-election](https://en.wikipedia.org/wiki/2026_Stafford_state_by-election). In the 2024 Queensland state election, the TPP result in Stafford was 55.32% Labor to 44.68% LNP [https://en.wikipedia.org/wiki/2026_Stafford_state_by-election](https://en.wikipedia.org/wiki/2026_Stafford_state_by-election).

Key candidates include Luke Richmond (Labor), Fiona Hammond (LNP), Jess Lane (Greens), and several minor party and independent candidates [https://en.wikipedia.org/wiki/2026_Stafford_state_by-election](https://en.wikipedia.org/wiki/2026_Stafford_state_by-election). By-elections historically tend to produce larger swings against governing parties; notably, the LNP currently governs Queensland, while Labor is in opposition. However, the unusual circumstances of the seat — previously held by an expelled Labor member running as an independent — and the presence of a Greens candidate add uncertainty to the outcome.

Resolution data will be available from the Electoral Commission of Queensland (ECQ) results portal: https://www.ecq.qld.gov.au/elections/election-events/stafford-state-by-election [https://en.wikipedia.org/wiki/2026_Stafford_state_by-election](https://en.wikipedia.org/wiki/2026_Stafford_state_by-election).

**Exact later resolution packet**

The question resolves YES.

Antecedent/window check: The by-election was held on 16 May 2026, which falls within the required window (on or after 10 May 2026 and no later than 30 June 2026). This is confirmed by Wikipedia [2026 Stafford state by-election - Wikipedia](https://en.wikipedia.org/wiki/2026_Stafford_state_by-election), ABC News [Stafford By-election 2026 - ABC News](https://www.abc.net.au/news/elections/stafford-by-election-2026), Antony Green [2026 – Stafford By-election – Result Summary](https://antonygreen.com.au/stafford-by-election-results/), and Poll Bludger [Stafford by-election live - The Poll Bludger](https://www.pollbludger.net/2026/05/16/stafford-by-election-live-2/). The event therefore occurred within the resolution window, so the question does not resolve NO on the "not held by June 30" clause.

Consequent (winner): Luke Richmond of the Australian Labor Party won the seat of Stafford. This is confirmed by multiple independent authoritative sources:
- Wikipedia: Richmond (Labor) defeated Fiona Hammond (LNP) with a two-party-preferred result of 51.36% to 48.64% [2026 Stafford state by-election - Wikipedia](https://en.wikipedia.org/wiki/2026_Stafford_state_by-election).
- Antony Green (ABC election analyst): Richmond (ALP) 51.3% vs Hammond (LNP) 48.7% [2026 – Stafford By-election – Result Summary](https://antonygreen.com.au/stafford-by-election-results/).
- ABC News election results: Richmond (ALP) 51.4% vs Hammond (LNP) 48.6% [Stafford By-election 2026 - ABC News](https://www.abc.net.au/news/elections/stafford-by-election-2026).
- The Poll Bludger (William Bowe): the result was called for Labor's Luke Richmond, TCP ~51.3% [Stafford by-election live - The Poll Bludger](https://www.pollbludger.net/2026/05/16/stafford-by-election-live-2/).
- Corroborating: The Guardian reported the LNP fell "agonisingly short" with Richmond ahead of Hammond; the Queensland Parliament Member List shows "Mr Luke Richmond" as the current Member for Stafford (committee appointment dated 4 Jun 2026), and the Wikipedia biography states Richmond "has represented the district of Stafford ... since a 2026 by-election" and "is a member of the Australian Labor Party." Labor's own site lists him as "Member for Stafford since May 2026."

Official ECQ declaration: The specified resolution source, the ECQ results portal at https://results.elections.qld.gov.au/Stafford2026 (and sub-pages such as https://results.elections.qld.gov.au/Stafford2026/stafford/indicative), shows the status "DECLARED — the elected candidate has received a majority of votes after preferences have been distributed," confirming the ECQ formally declared the result rather than a mere projection. That Richmond has since been sworn in and appointed to a Queensland Parliament committee (4 Jun 2026) further confirms the official declaration in his favour.

Name/affiliation match: The declared winner is exactly "Luke Richmond" of the "Australian Labor Party," matching the question [2026 Stafford state by-election - Wikipedia](https://en.wikipedia.org/wiki/2026_Stafford_state_by-election)[Stafford By-election 2026 - ABC News](https://www.abc.net.au/news/elections/stafford-by-election-2026)[2026 – Stafford By-election – Result Summary](https://antonygreen.com.au/stafford-by-election-results/).

Note on a conflicting reading: One automated query against the JavaScript-rendered ECQ portal erroneously reported Fiona Hammond (LNP) as the winner [https://www.ecq.qld.gov.au/elections/election-events/stafford-state-by-election](https://www.ecq.qld.gov.au/elections/election-events/stafford-state-by-election), while a separate query of the same URL returned only a "Loading..." state [2026 Stafford State By-election - Election Results](https://results.elections.qld.gov.au/Stafford2026). This single reading is a hallucination/rendering artifact: it directly contradicts every other source (Wikipedia, ABC, Antony Green, Poll Bludger, The Guardian, Queensland Parliament, Queensland Labor), all of which state Labor's Luke Richmond won. The weight of evidence is decisively that Richmond (ALP) was elected.

Therefore the ECQ officially declared Luke Richmond (Australian Labor Party) as the elected member for Stafford, and the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-122. `f1ed32cb-26da-54da-86fb-220ffdbc5b0c`

- Present date: `2026-05-29 06:34:19.618710`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the U.S. Supreme Court rule in favor of the petitioner in Wolford v. Lopez (No. 24-1046) by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the U.S. Supreme Court issues an opinion on or after May 12, 2026 (UTC) and before July 1, 2026, 11:59 PM UTC, in Wolford v. Lopez (No. 24-1046), in which the Court **reverses or vacates** the judgment of the U.S. Court of Appeals for the Ninth Circuit, in whole or in part. This includes:
- A full reversal of the Ninth Circuit's judgment;
- A partial reversal (e.g., reversing on some issues while affirming on others);
- A vacate-and-remand order (vacating the Ninth Circuit's judgment and remanding for further proceedings).

The question resolves **No** if:
- The Court affirms the Ninth Circuit's judgment in full; or
- The Court dismisses the case as improvidently granted (DIG); or
- No opinion is issued by July 1, 2026, 11:59 PM UTC.

**Resolution source:** The official slip opinion published on the U.S. Supreme Court's website at https://www.supremecourt.gov/opinions/slipopinion/25 (for October Term 2025 opinions). The opinion's syllabus and judgment line will be used to determine whether the Ninth Circuit's judgment was reversed, vacated, or affirmed.

Key term clarifications:
- "Petitioner" means Jason Wolford et al., the parties who filed the petition for certiorari challenging the Ninth Circuit's decision. See docket: https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/24-1046.html
- "Ruling in favor of the petitioner" means the Court reverses or vacates the lower court judgment, as described above. A concurrence that does not change the judgment does not count.
- "Private property open to the public" refers to privately owned property generally accessible to the public, as used in Hawaii's concealed-carry statute at issue in this case.

**Pre-cutoff background**

Wolford v. Lopez (Docket No. 24-1046) is a Second Amendment case before the U.S. Supreme Court. The petitioners—Jason Wolford and other gun owners—challenge a Hawaii statute (Haw. Rev. Stat. § 134-A) that makes it a crime for licensed concealed-carry permit holders to bring firearms onto "private property open to the public" (e.g., shops, restaurants, theaters) unless the property owner has given express, affirmative permission. The Ninth Circuit Court of Appeals upheld the Hawaii law, finding it consistent with historical tradition under the framework established in New York State Rifle & Pistol Association v. Bruen (2022).

The Supreme Court granted certiorari limited to Question 1 of the petition and heard oral argument on January 20, 2026 [Wolford v. Lopez (24-1046) - SCOTUSblog](https://www.scotusblog.com/cases/wolford-v-lopez/). As of May 12, 2026, no decision has been issued [Wolford v. Lopez (24-1046) - SCOTUSblog](https://www.scotusblog.com/cases/wolford-v-lopez/). The Court's current term typically concludes by late June or early July.

Analysts at the Duke Center for Firearms Law described the oral argument as featuring "hard questions" directed at both sides. The Court's 6-3 conservative majority has been receptive to Second Amendment claims in recent cases (Bruen in 2022, United States v. Rahimi in 2024), but the intersection of property rights and gun rights adds complexity. Multiple outcomes are possible, including a full reversal, a narrow ruling, a vacate-and-remand, or an affirmance.

Key definitions:
- "Petitioner" refers to Jason Wolford et al., the gun owners challenging the Hawaii law. See the Supreme Court docket: https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/24-1046.html
- "Private property open to the public" refers to privately owned property that is generally accessible to the public, such as retail stores and restaurants, as defined under Hawaii's concealed-carry statute.
- The Ninth Circuit decision being challenged held that Hawaii's default rule—prohibiting concealed carry on such property absent the owner's affirmative consent—is consistent with the Second Amendment under Bruen's historical-tradition test.

**Exact later resolution packet**

The question resolves YES.

The U.S. Supreme Court issued its opinion in Wolford v. Lopez (No. 24-1046) on June 25, 2026 — within the resolution window (on or after May 12, 2026 UTC and before July 1, 2026, 11:59 PM UTC).

The official slip opinion published on supremecourt.gov (https://www.supremecourt.gov/opinions/25pdf/24-1046_nmio.pdf) holds that Hawaii's law prohibiting licensed concealed-carry permit holders from carrying handguns on private property open to the public without the property owner's express authorization violates the Second and Fourteenth Amendments. The syllabus judgment line states: "116 F. 4th 959, reversed and remanded." The Ninth Circuit's judgment was therefore REVERSED and REMANDED, decided 6-3, with Justice Alito delivering the opinion of the Court [[PDF] 24-1046 Wolford v. Lopez (06/25/2026) - Supreme Court](https://www.supremecourt.gov/opinions/25pdf/24-1046_nmio.pdf).

The official Supreme Court docket (https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/24-1046.html) similarly records for June 25, 2026: "Judgment REVERSED and case REMANDED," with Justice Alito delivering the opinion of the Court [Wolford - Search - Supreme Court of the United States](https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/24-1046.html).

Per the resolution criteria, a reversal (or vacate-and-remand) of the Ninth Circuit's judgment resolves the question YES. The Court reversed the Ninth Circuit judgment in favor of the petitioners (Jason Wolford et al.). This satisfies the YES condition.

Resolution source URLs:
- Slip opinion: https://www.supremecourt.gov/opinions/25pdf/24-1046_nmio.pdf
- Docket: https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/24-1046.html

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-123. `08bb3a55-c266-546d-bdd5-3a706d12ed8c`

- Present date: `2026-05-14 01:48:32.949114`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-25T00:00:00`

**Question**

Will the Bank of Mexico's June 25, 2026, Monetary Policy Decision Be a Unanimous (5-0) Vote?

**Resolution criteria**

This question resolves **Yes** if the official monetary policy press release published by Banco de México (Banxico) on June 25, 2026, reports that the Governing Board's (Junta de Gobierno's) decision was reached by a **unanimous 5-0 vote**—meaning all five members of the Board voted for the same policy action (whether a hold, cut, or hike).

This question resolves **No** if the press release reports any vote split (e.g., 4-1, 3-2) or if the announcement is postponed beyond June 30, 2026 (UTC-6).

**Definitions:**
- "Unanimous" means all five sitting members of the Governing Board voted for the identical policy action, i.e., a 5-0 vote with no dissents.
- The "Governing Board" (Junta de Gobierno) is Banxico's five-member decision-making body as described at https://www.banxico.org.mx/getting-to-know-banco-de-mexico/board-of-governors-curriculum.html. It consists of one Governor and four Deputy Governors.
- If a Board vacancy reduces the voting members below five, a unanimous vote among all present members still counts as "Yes."

**Resolution source:** The official Banxico monetary policy statement for the June 25, 2026, decision, published at https://www.banxico.org.mx/publications-and-press/announcements-of-monetary-policy-decisions/monetary-policy-announcements.html. The vote breakdown is reported within the full text of the press release (PDF linked from that page).

**Pre-cutoff background**

The Bank of Mexico (Banco de México, or "Banxico") sets monetary policy through its five-member Governing Board (Junta de Gobierno), composed of Governor Victoria Rodríguez Ceja and Deputy Governors Jonathan Heath, Galia Borja Gómez, Omar Mejía Castelazo, and José Gabriel Cuadra García (https://www.banxico.org.mx/getting-to-know-banco-de-mexico/board-of-governors-curriculum.html).

At its May 7, 2026, meeting, Banxico cut the overnight interbank interest rate by 25 basis points to 6.50% in a 3-2 split vote. Governor Rodríguez, Deputy Governors Cuadra and Mejía voted for the cut, while Deputy Governors Borja and Heath voted to hold rates unchanged. Banxico signaled this was the final cut in a two-year easing cycle that brought rates down 475 basis points from 11.25%.

With the easing cycle now declared over, the June 25, 2026, meeting is widely expected to feature a hold at 6.50%. However, the question of unanimity remains uncertain: the two dissenters (Borja and Heath) who wanted to hold in May may now agree with a hold decision, producing unanimity—or dovish members could push for further easing, maintaining a split. Recent Banxico decisions have frequently featured divided votes (the March 2026 cut was also a split decision), making unanimity genuinely uncertain.

The next scheduled monetary policy announcement is June 25, 2026, at 13:00 Central Time (CT, UTC-6).

**Exact later resolution packet**

The question resolves **YES**.

**Question:** Will the Bank of Mexico's June 25, 2026, Monetary Policy Decision Be a Unanimous (5-0) Vote?

**Evidence from the official Banxico resolution source:**
The official Banco de México monetary policy statement press release for June 25, 2026 (PDF at https://www.banxico.org.mx/publications-and-press/announcements-of-monetary-policy-decisions/%7B1232328B-67C5-6882-B908-B200C19F3E3D%7D.pdf), linked from the resolution-source listing page (https://www.banxico.org.mx/publications-and-press/announcements-of-monetary-policy-decisions/monetary-policy-announcements.html), states verbatim: "With the presence of all its members, the Board decided unanimously to maintain the target for the overnight interbank interest rate at 6.50 per cent." [13adf3]

Key points relative to the resolution criteria:
- The vote was **unanimous** (all members voting for the identical policy action — a hold at 6.50%), with **all five members present** ("With the presence of all its members"). This satisfies the 5-0 unanimous requirement, with no dissents and no Board vacancy reducing membership. [13adf3]
- The announcement occurred **on June 25, 2026**, well before the June 30, 2026 cutoff, so no postponement clause is triggered.

**Corroborating sources:** Central Banking reported "The Bank of Mexico (Banxico) has held its benchmark interest rate at 6.5% in a unanimous decision by its governing board." [da5ba1] Banxico's own official X/Twitter post likewise stated "Con la presencia de todos sus miembros, la Junta de Gobierno del #BancodeMéxico decidió por unanimidad conservar la Tasa de Interés..." Additional outlets (Rio Times "First Unanimous Vote," mexicobusiness.news "Unanimous Decision," ai-market-station) all reported the same unanimous outcome.

**Note on a conflicting reading:** An initial exhaustive query of the announcements listing page returned a claim that the vote was a "3-2 split" with Borja and Heath dissenting [172c7d]. This is contradicted by the direct text of the official PDF [13adf3], Banxico's own social-media statement, and every independent news source, and is therefore treated as an erroneous/hallucinated result. The authoritative primary source (the PDF press release) unambiguously states the decision was unanimous with all members present.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-124. `828cf239-a556-5ff3-9467-44bf1325dfa5`

- Present date: `2026-05-03 11:30:10.101622`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the Colorado General Assembly pass a bill modifying or delaying the June 30, 2026 effective date of the Colorado AI Act (SB 24-205) that is signed by the Governor by June 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after May 2, 2026, and by 11:59 PM Mountain Time (UTC-6) on June 1, 2026, a bill that explicitly modifies or delays the June 30, 2026 effective date of Colorado SB 24-205 has both:

1. Passed both chambers of the Colorado General Assembly (i.e., received final passage in both the House and Senate), AND
2. Been signed into law by the Governor, OR allowed to become law without the Governor's signature.

For this question, "pass" means the bill has cleared both chambers AND received the Governor's signature (or become law without signature). A bill that has passed both chambers but is still awaiting the Governor's action as of June 1, 2026 does NOT count.

A "modification or delay" of the effective date means any legislative change that either (a) changes the June 30, 2026 date to a later date (e.g., January 1, 2027), (b) repeals the law entirely, or (c) makes the effective date contingent on another event or condition such that the law would not take full effect on June 30, 2026 as currently written.

Bills that amend the substance of SB 24-205 but leave the June 30, 2026 effective date unchanged do NOT count for resolution.

Resolution will be determined by checking the official bill status on the Colorado General Assembly website (https://leg.colorado.gov/) and any relevant bill tracking pages linked therein.

**Pre-cutoff background**

Colorado's SB 24-205, the "Consumer Protections for Artificial Intelligence" Act, was signed into law on May 17, 2024 [SB24-205 Consumer Protections for Artificial Intelligence | Colorado ...](https://leg.colorado.gov/bills/sb24-205). Its original effective date of February 1, 2026 was delayed to June 30, 2026 via SB 25B-004, signed by Governor Polis on August 28, 2025. This is the current effective date as of May 2, 2026.

In March 2026, the Colorado AI Policy Work Group released a unanimous proposed framework that would substantially revise the AI Act and delay its effective date from June 30, 2026 to January 1, 2027 [Colorado Takes a Major Step Towards Rewriting Its AI Law As Its ...](https://www.lawandtheworkplace.com/2026/04/colorado-takes-a-major-step-towards-rewriting-its-ai-law-as-its-effective-date-approaches/). A prior attempt to modify the law during the regular 2026 session, SB 25-318, was postponed indefinitely (defeated) on a 5-2 vote in committee. However, new legislation based on the Work Group's proposal may still be introduced and passed before session ends.

The Colorado General Assembly's 2026 regular session is scheduled to adjourn sine die on May 13, 2026. The Governor has until June 12, 2026 to act on bills passed during the session. Any bill not signed or vetoed by June 13 becomes law without signature.

Resolution source: The official Colorado General Assembly bill tracking website at https://leg.colorado.gov/ and its bill search function.

**Exact later resolution packet**

The question resolves YES. The Colorado General Assembly passed Senate Bill 26-189 ("Automated Decision-Making Technology"), which repeals and reenacts Colorado's AI Act (SB 24-205) and changes the law's effective date from June 30, 2026 to January 1, 2027. Governor Jared Polis signed SB 26-189 into law on May 14, 2026 [e80a2b, 17b315, ac0a03].

Walking through the resolution criteria:
1. PASSED BOTH CHAMBERS: SB 26-189 cleared both the Colorado Senate and House before being sent to the Governor. The 2026 regular session adjourned sine die May 13, 2026, and the bill was passed in the final days of session (Polis announced he would sign the "pared down AI bill that passed overnight" around May 12). Since the Governor signed it on May 14, 2026, it necessarily had received final passage in both chambers [17b315, ac0a03].
2. SIGNED BY GOVERNOR BY JUNE 1, 2026: Governor Polis signed SB 26-189 on May 14, 2026, well before the 11:59 PM MT June 1, 2026 deadline [e80a2b, 17b315, ac0a03].
3. ON OR AFTER MAY 2, 2026: Passage occurred in mid-May 2026 (session ended May 13, signed May 14), satisfying the requirement that the action occur on or after May 2, 2026 [17b315].
4. MODIFIES/DELAYS THE JUNE 30, 2026 EFFECTIVE DATE: The bill explicitly delays the effective date from June 30, 2026 to January 1, 2027 [e80a2b, 17b315, ac0a03]. The question's resolution criteria define a qualifying "modification or delay" to include both (a) changing the June 30, 2026 date to a later date AND (b) repealing the law entirely. SB 26-189 does both — it repeals and reenacts SB 24-205 with a new January 1, 2027 effective date — so the original June 30, 2026 effective date does NOT take effect. This squarely satisfies criteria (a) and (b).

The official Colorado General Assembly page (https://leg.colorado.gov/bills/sb26-189) confirms SB 26-189 was enacted and signed [c7f8d9]. One automated read of that page argued NO on the theory that the bill "replaces" rather than "delays" the effective date; however, that reasoning is incorrect under this question's explicit criteria, which count a full repeal as qualifying and which note the revised law takes effect January 1, 2027 rather than June 30, 2026. The "do NOT count" carve-out applies only to bills that "leave the June 30, 2026 effective date unchanged," which is not the case here — the June 30, 2026 date is superseded by January 1, 2027 [e80a2b, 17b315, ac0a03].

All conditions are met, so the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-125. `17dee13a-3f4c-5bdd-88fa-8ddff8403454`

- Present date: `2026-05-16 02:09:11.930531`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-06-30T00:00:00`

**Question**

Will Brooke Pinto finish in the top two in the June 16, 2026 Democratic primary for D.C. House Delegate?

**Resolution criteria**

This question resolves YES if Brooke Pinto is one of the two candidates receiving the highest number of votes in the June 16, 2026, Democratic primary for the District of Columbia's non-voting delegate to the U.S. House of Representatives, according to the official results published by the District of Columbia Board of Elections (DCBOE) at https://electionresults.dcboe.org/.

"Top two" means the two candidates with the most total votes. If Pinto is tied in vote count with another candidate such that more than two candidates share the top two positions, the question resolves YES as long as Pinto is among those tied candidates.

This question concerns the D.C. House Delegate race (non-voting member of the U.S. House of Representatives), not any D.C. Council race. Pinto's current role is Ward 2 Councilmember on the D.C. Council; the office she is running for is D.C. House Delegate.

Resolution will be based on the official certified results. If official results are not yet certified by June 30, 2026, 11:59 PM ET, unofficial results from DCBOE will be used. If the primary is postponed beyond June 30, 2026, the question resolves N/A.

**Pre-cutoff background**

The 2026 Democratic primary for the District of Columbia's non-voting delegate to the U.S. House of Representatives is scheduled for June 16, 2026. The incumbent, Eleanor Holmes Norton, announced on January 26, 2026, that she would not seek re-election [United States House of Representatives election in the District of ...](https://ballotpedia.org/United_States_House_of_Representatives_election_in_the_District_of_Columbia,_2026).

Brooke Pinto, currently a D.C. Council member representing Ward 2, is one of several candidates competing for the seat. As of January 31, 2026, Pinto had raised $843,496 with $608,868 cash on hand [2026 United States House of Representatives election in the District ...](https://en.wikipedia.org/wiki/2026_United_States_House_of_Representatives_election_in_the_District_of_Columbia). By March 31, 2026, her receipts had grown to $1,252,427 with $820,659 cash on hand [United States House of Representatives election in the District of ...](https://ballotpedia.org/United_States_House_of_Representatives_election_in_the_District_of_Columbia,_2026). In a November 2025 poll conducted by Lake Research Partners, Pinto polled at 14%, behind Robert White (29%) and Eleanor Holmes Norton (16%), with 31% undecided [2026 United States House of Representatives election in the District ...](https://en.wikipedia.org/wiki/2026_United_States_House_of_Representatives_election_in_the_District_of_Columbia).

The race is considered a battleground primary [United States House of Representatives election in the District of ...](https://ballotpedia.org/United_States_House_of_Representatives_election_in_the_District_of_Columbia,_2026). Three candidates lead in polling, fundraising, and media attention: Pinto, Robert White (D.C. Council member, At-Large), and Kinney Zalesne. As of March 31, 2026, White reported $414,432 in receipts and $73,489 cash on hand, while Zalesne reported $752,831 in receipts and $466,584 cash on hand [United States House of Representatives election in the District of ...](https://ballotpedia.org/United_States_House_of_Representatives_election_in_the_District_of_Columbia,_2026). Pinto received an endorsement from U.S. Senator Angela Alsobrooks [2026 United States House of Representatives election in the District ...](https://en.wikipedia.org/wiki/2026_United_States_House_of_Representatives_election_in_the_District_of_Columbia). Recent polling (circa April 2026) suggested a tightening race between Pinto and White, with Pinto closing the gap significantly from her earlier 14% showing.

**Exact later resolution packet**

The question resolves YES: Brooke Pinto finished in the top two (second place) in the June 16, 2026 Democratic primary for D.C. House Delegate (non-voting delegate to the U.S. House of Representatives).

Antecedent/window check: The primary was held as scheduled on June 16, 2026 (it was NOT postponed beyond June 30, 2026), so the N/A condition does not apply. This is confirmed by the DCBOE results page and multiple news outlets [ffcfd2].

Official resolution source — DCBOE (https://electionresults.dcboe.org/election_results/2026-Primary-Election): For the DEM DELEGATE TO THE U.S. HOUSE OF REPRESENTATIVES contest (ranked-choice voting, First Rank Results), the vote totals were [ffcfd2]:
- Robert White: 86,139 votes (63.58%) — 1st
- Brooke Pinto: 28,357 votes (20.93%) — 2nd
- Kinney Zalesne: 10,570 votes (7.8%) — 3rd
- Trent Holbrook: 6,057 votes (4.47%)
- Greg Jaczko: 3,901 votes (2.88%)
- Write-in: 451 votes (0.33%)

Brooke Pinto is unambiguously the second-highest vote-getter, trailing only Robert White, and finishing well ahead of the third-place candidate (Zalesne, 10,570 votes) by nearly 18,000 votes. There is no tie affecting the top two, so the tie-breaking rule is moot. She therefore is one of the two candidates with the most votes → YES.

Race identity check: These figures are specifically for the D.C. House Delegate (non-voting U.S. House member) race, not a D.C. Council race, matching the question's subject [ffcfd2].

Certification status: The DCBOE page labeled these as "Election Night Unofficial Results," last updated June 25, 2026 [ffcfd2]. The resolution criteria explicitly permit using DCBOE unofficial results if certified results were not available by June 30, 2026, 11:59 PM ET. Regardless of whether certification occurred by that deadline, the outcome (Pinto second by a wide margin) is not in dispute, and news outlets corroborate it: Roll Call reported Robert White won with ~63% and Pinto trailed with ~22% [ff8a6a], and NBC Washington, Politico, Fox5 and WJLA all report White defeated Pinto to win the nomination.

Note: The QUERY_DOCUMENT tool's auto-generated "resolution: 0" note in the Roll Call response [ff8a6a] was an erroneous interpretation by that tool — it correctly reported the underlying facts (White ~63%, Pinto ~22%, i.e., Pinto second) but wrongly concluded she was not top-two. The correct reading is that Pinto's second-place finish IS a top-two finish, consistent with the DCBOE data [ffcfd2].

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-126. `f794d090-ae6a-5b5a-9c6b-739a0fe1b063`

- Present date: `2026-04-30 18:54:33.681219`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will France be ranked #1 in the FIFA Men's World Rankings as of June 1, 2026 (23:59 UTC)?

**Resolution criteria**

This question resolves YES if France is listed as the #1 ranked team on the official FIFA Men's World Ranking page (https://inside.fifa.com/fifa-world-ranking/men) as of 23:59 UTC on June 1, 2026. The resolution source is the FIFA live ranking tracker at that URL.

If two or more teams have identical point totals (equal to the second decimal place), the team listed higher by FIFA's official ranking page is considered #1.

If the FIFA live ranking tracker is unavailable or non-functional at 23:59 UTC on June 1, 2026, the most recent ranking snapshot available on the official FIFA website prior to that time will be used. If no live data is available, the April 2026 official static rankings (the last static release before the June 9, 2026 update) will be used as the fallback.

**Pre-cutoff background**

As of the April 2026 FIFA Men's World Rankings update, France holds the #1 position with 1877.32 points, followed closely by Spain with 1876.4 points and Argentina with 1874.81 points [https://www.espn.com/soccer/story/_/id/46664763/fifa-mens-top-50-world-rankings](https://www.espn.com/soccer/story/_/id/46664763/fifa-mens-top-50-world-rankings). The margin between France and Spain is less than 1 point, making the top ranking highly volatile. The FIFA Men's World Ranking uses an Elo-based points system where points are added or subtracted based on match results, match importance, and opponent strength. FIFA introduced real-time live ranking updates in March 2026, meaning any international matches (including pre-World Cup friendlies in late May/early June 2026) can shift the rankings before the next official static release on June 9, 2026. The 2026 FIFA World Cup is scheduled to begin on June 11, 2026, so the rankings as of June 1 represent a key snapshot of team standings heading into the tournament.

**Exact later resolution packet**

The question resolves YES if France is listed as the #1 ranked team on the official FIFA Men's World Ranking page (https://inside.fifa.com/fifa-world-ranking/men) as of 23:59 UTC on June 1, 2026.

Evidence:
- The official FIFA Men's World Ranking page (https://inside.fifa.com/fifa-world-ranking/men) lists France at rank #1 with 1877.32 points, ahead of Spain (#2, 1876.40) and Argentina (#3, 1874.81), with the last official update being 1 April 2026 [f643a7].
- The independent live FIFA ranking tracker at football-ranking.com (https://football-ranking.com/fifa-world-rankings), which updates daily, shows the same standings as of early-to-mid June 2026: 1. France 1,877.32; 2. Spain 1,876.40; 3. Argentina 1,874.81 [a0df2e].

Effect of late May / early June 2026 matches:
- The point totals for France (1877.32), Spain (1876.40), and Argentina (1874.81) remained identical between the April 1, 2026 static release and the live tracker readings in June 2026 [f643a7, a0df2e]. This indicates that no international matches in late May or early June 2026 altered the top of the ranking before the June 1, 2026 deadline; France retained its lead of just under 1 point over Spain.

Since France was the #1 ranked team on the official FIFA page at the time of the June 1, 2026 deadline, the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-127. `d41b3f25-a551-57fd-a6f6-4a0c91bd91f7`

- Present date: `2026-05-29 03:50:50.147499`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will President Trump sign the $72B immigration enforcement reconciliation bill into law by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the immigration enforcement reconciliation bill originating from the process initiated by [S. Con. Res. 33](https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/33) is enacted into law on or after May 12, 2026, and on or before July 1, 2026 (11:59 PM ET).

Enactment means the bill has been signed by the President, OR has become law without the President's signature under the [Presentment Clause](https://en.wikipedia.org/wiki/Presentment_Clause) (i.e., the President neither signs nor vetoes the bill within 10 days while Congress is in session), OR Congress overrides a presidential veto by a two-thirds vote in both chambers.

The bill will be identifiable as the reconciliation measure reported pursuant to S. Con. Res. 33, primarily funding ICE and CBP. Once enacted, it will be assigned a Public Law number.

Resolution will be verified via the official [Congress.gov](https://www.congress.gov/) record of enrolled bills and public laws, or via the [Federal Register](https://www.federalregister.gov/). If no such law is enacted by 11:59 PM ET on July 1, 2026, this question resolves **No**.

**Pre-cutoff background**

In late April 2026, Congress adopted S. Con. Res. 33, a budget resolution enabling a second round of [budget reconciliation](https://en.wikipedia.org/wiki/Reconciliation_(United_States_Congress)) ("Reconciliation 2.0") to fund immigration enforcement. The Senate passed it on April 23, 2026 (50–48), and the House on April 29, 2026 (215–211) [House clears budget resolution, advancing Reconciliation 2.0 to ...](https://www.naco.org/news/house-clears-budget-resolution-advancing-reconciliation-20-fund-dhs-and-cbp).

On May 4–5, 2026, the Senate Judiciary and Homeland Security committees released the legislative text of a nearly $72 billion reconciliation bill funding Immigration and Customs Enforcement (ICE) and Customs and Border Protection (CBP) through 2029 [https://www.crfb.org/blogs/2025-reconciliation-tracker](https://www.crfb.org/blogs/2025-reconciliation-tracker). The Congressional Budget Office scored the legislation at $72 billion [https://www.crfb.org/blogs/2025-reconciliation-tracker](https://www.crfb.org/blogs/2025-reconciliation-tracker). The bill includes more than $38 billion for ICE and $26 billion for CBP, as well as a controversial $1 billion provision for White House security upgrades [Congress returns from recess facing high-stakes fights - The Hill](https://thehill.com/homenews/house/5870629-congress-reconciliation-immigration-fisa-farm-bill/).

As of May 13, 2026, Congress has returned from recess and committee markups are expected during the week of May 11 [Congress returns from recess facing high-stakes fights - The Hill](https://thehill.com/homenews/house/5870629-congress-reconciliation-immigration-fisa-farm-bill/). The House and Senate Judiciary and Homeland Security committees face a May 15, 2026 deadline to submit reconciliation text to their respective Budget Committees [House clears budget resolution, advancing Reconciliation 2.0 to ...](https://www.naco.org/news/house-clears-budget-resolution-advancing-reconciliation-20-fund-dhs-and-cbp). President Trump has set a deadline of June 1, 2026 for the bill to reach his desk [Congress returns from recess facing high-stakes fights - The Hill](https://thehill.com/homenews/house/5870629-congress-reconciliation-immigration-fisa-farm-bill/). House Budget Committee Chairman Jodey Arrington expects the reconciliation process to take "a few weeks" [Congress returns from recess facing high-stakes fights - The Hill](https://thehill.com/homenews/house/5870629-congress-reconciliation-immigration-fisa-farm-bill/).

Key obstacles include: the Senate "[Byrd Bath](https://en.wikipedia.org/wiki/Byrd_Rule)" process where the parliamentarian may strip non-budgetary provisions, political controversy over the White House ballroom funding, and the need for Speaker Johnson to secure support from both hardline and moderate House factions [Congress returns from recess facing high-stakes fights - The Hill](https://thehill.com/homenews/house/5870629-congress-reconciliation-immigration-fisa-farm-bill/). Because reconciliation bills bypass the [Senate filibuster](https://en.wikipedia.org/wiki/Filibuster_in_the_United_States_Senate), only a simple majority is needed in each chamber.

**Exact later resolution packet**

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

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-128. `485c3100-532f-57ee-ac85-37b010b3b5eb`

- Present date: `2026-05-01 14:26:25.547530`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Assimi Goïta remain the head of state of Mali on June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, as of June 1, 2026 at 23:59 UTC, Assimi Goïta holds the official title of President of the Transition (or any equivalent title designating him as the head of state) of Mali.

This question resolves **No** if, by that date and time, any of the following have occurred:
- Goïta has been removed from power (via coup, resignation, or other means)
- Goïta is confirmed deceased
- Goïta is missing or incapacitated and another individual has been publicly designated or is functioning as head of state by official Malian government communications
- A rival government or faction has taken de facto control of Bamako and installed a different head of state

**Resolution source:** Official Malian government communications (e.g., statements from the presidency or state broadcaster ORTM), or credible reporting from major international wire services including Reuters (https://www.reuters.com), Agence France-Presse, or the Associated Press (https://apnews.com).

**Competing claims:** If there are competing claims to the head of state position (e.g., a rival junta faction vs. Goïta), the question resolves based on which individual exercises de facto control of Bamako as reported by at least two of the three wire services listed above. If no clear consensus exists among these sources, the question resolves **No**.

**Deceased, missing, or incapacitated:** If Goïta is reported as deceased, missing, or incapacitated by at least two of the listed wire services, and no official Malian government communication affirms him as active head of state, the question resolves **No**.

**Pre-cutoff background**

As of May 1, 2026, Mali's military junta faces severe instability following a major rebel offensive on April 25–26, 2026. During this offensive, separatist rebels and al-Qaeda-linked jihadists (JNIM) launched coordinated attacks, seizing the northern town of Kidal from Russian Africa Corps forces and striking near the capital Bamako [https://www.theguardian.com/world/2026/apr/28/russia-claims-its-africa-corps-group-prevented-coup-in-mali-after-rebels-seize-towns](https://www.theguardian.com/world/2026/apr/28/russia-claims-its-africa-corps-group-prevented-coup-in-mali-after-rebels-seize-towns). Defense Minister Sadio Camara, a key Moscow ally within the junta, was killed in an apparent suicide bombing during the attacks [https://www.theguardian.com/world/2026/apr/28/russia-claims-its-africa-corps-group-prevented-coup-in-mali-after-rebels-seize-towns](https://www.theguardian.com/world/2026/apr/28/russia-claims-its-africa-corps-group-prevented-coup-in-mali-after-rebels-seize-towns).

Junta leader Assimi Goïta, who has held power as President of the Transition since a 2021 coup, was not seen publicly for several days after the offensive began, fueling intense speculation about his political survival and internal divisions within the military government [https://www.theguardian.com/world/2026/apr/28/russia-claims-its-africa-corps-group-prevented-coup-in-mali-after-rebels-seize-towns](https://www.theguardian.com/world/2026/apr/28/russia-claims-its-africa-corps-group-prevented-coup-in-mali-after-rebels-seize-towns). On April 28, 2026, the Malian presidency released a photograph showing Goïta meeting with the Russian ambassador, Igor Gromyko, though analysts questioned whether this demonstrated genuine control [https://www.theguardian.com/world/2026/apr/28/russia-claims-its-africa-corps-group-prevented-coup-in-mali-after-rebels-seize-towns](https://www.theguardian.com/world/2026/apr/28/russia-claims-its-africa-corps-group-prevented-coup-in-mali-after-rebels-seize-towns). Russia's defense ministry claimed its Africa Corps prevented a coup, although local reports suggest Russian forces negotiated their exit from Kidal with Algerian mediation [https://www.theguardian.com/world/2026/apr/28/russia-claims-its-africa-corps-group-prevented-coup-in-mali-after-rebels-seize-towns](https://www.theguardian.com/world/2026/apr/28/russia-claims-its-africa-corps-group-prevented-coup-in-mali-after-rebels-seize-towns).

Analysts describe the junta as "extremely weakened" [https://www.usnews.com/news/world/articles/2026-04-29/analysis-mali-turmoil-threatens-russian-push-for-influence-and-mineral-wealth-in-africa](https://www.usnews.com/news/world/articles/2026-04-29/analysis-mali-turmoil-threatens-russian-push-for-influence-and-mineral-wealth-in-africa), with ongoing uncertainty about internal cohesion and Goïta's ability to maintain power through May 2026. The situation remains fluid, with potential for further rebel advances, internal military challenges, or external pressure to force a leadership change.

**Exact later resolution packet**

The question resolves YES because Assimi Goïta remained Mali's head of state (President of the Transition) as of June 1, 2026, 23:59 UTC.

Evidence:
- Goïta survived the April 25–26, 2026 offensive and made his first public appearance on April 28, 2026, meeting the Russian ambassador and visiting wounded in Bamako, declaring the situation "under control" — reported directly by Reuters (https://www.reuters.com/world/mali-military-leader-goita-meets-russian-ambassador-after-attacks-office-says-2026-04-28/) [4c37b6].
- On May 4, 2026, Goïta, still acting as President of the Transition/junta leader, issued a decree appointing himself Minister of Defense to replace the late Sadio Camara — reported by Reuters (https://www.reuters.com/world/mali-leader-goita-assumes-role-defence-minister-after-attacks-state-media-says-2026-05-04/), AP, France24 and Al Jazeera. This action itself demonstrates he continued exercising the powers of head of state well into May [a5f925, 4c37b6].
- The Wikipedia article "2026 Mali offensives," last updated June 2, 2026 (i.e., covering the entire resolution window), contains no indication that Goïta was removed, resigned, killed, or incapacitated; it records him as continuing to issue decrees and lead the junta [4c37b6].
- The "Assimi Goïta" Wikipedia article (last updated May 18, 2026) lists him as the incumbent President of Mali and Minister of Defense, with no replacement [a5f925].

No reports from the Malian presidency, ORTM, Reuters, AFP, or AP indicate Goïta's removal, death, incapacitation, or any rival faction taking de facto control of Bamako before the deadline. Earlier coup speculation (and Russia's claim of having "prevented a coup") was resolved in Goïta's favor: he reappeared publicly, addressed the nation, and consolidated power by taking the defense portfolio. Therefore the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):
