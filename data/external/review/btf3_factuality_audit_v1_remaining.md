# BTF-3 packet factuality audit v1 — remaining items worksheet

Only the items with no verdict yet. Order and numbering are the frozen sample's;
do not renumber. Working procedure: `BTF3_FACTUALITY_AUDIT_HOWTO.md`.
Record verdicts in `btf3_factuality_audit_v1_verdicts.md`, not in this file.

## Realized YES — 16 items remaining

### YES-15. `630b345d-eb03-534c-a3e5-5de067aaed7b`

- Recorded outcome: **YES** · present date `2026-05-14 11:24:43.947611` (window ends end of UTC day `2026-05-14`) · expected resolution `2026-07-01T00:00:00`

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

**Exact later resolution packet — this is the object under audit**

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
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-17. `f8b8e64a-1462-56e8-8e51-2378eaca309f`

- Recorded outcome: **YES** · present date `2026-05-01 10:40:50.314413` (window ends end of UTC day `2026-05-01`) · expected resolution `2026-05-21 00:00:00`

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

**Exact later resolution packet — this is the object under audit**

The question resolves YES. The official Federal Reserve FOMC calendar entry for the April 28–29, 2026 meeting lists the minutes at https://www.federalreserve.gov/monetarypolicy/fomcminutes20260429.htm and https://www.federalreserve.gov/monetarypolicy/files/fomcminutes20260429.pdf, with “Released May 20, 2026,” which is before the June 1, 2026 23:59 UTC deadline [The Fed - Meeting calendars and information - Federal Reserve](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm). In those official minutes, a qualifying rate-hike-openness sentiment is attributed to a stronger-than-“some” quantifier: “A majority of participants highlighted, however, that some policy firming would likely become appropriate if inflation were to continue to run persistently above 2 percent” [https://www.federalreserve.gov/monetarypolicy/files/fomcminutes20260429.pdf](https://www.federalreserve.gov/monetarypolicy/files/fomcminutes20260429.pdf). The quantifier over participants is “A majority of participants,” and the resolution criteria explicitly count “a majority of” as sufficient. The minutes also state: “To address this possibility, many participants indicated that they would have preferred removing the language from the postmeeting statement that suggested an easing bias regarding the likely direction of the Committee’s future interest rate decisions” [https://www.federalreserve.gov/monetarypolicy/files/fomcminutes20260429.pdf](https://www.federalreserve.gov/monetarypolicy/files/fomcminutes20260429.pdf). This matches the specified “removing or opposing the easing bias” sentiment, and “many” is strictly higher than “some” on the provided hierarchy. Therefore the April minutes did use a stronger quantifier than “some” for participants expressing openness to rate hikes [https://www.federalreserve.gov/monetarypolicy/files/fomcminutes20260429.pdf](https://www.federalreserve.gov/monetarypolicy/files/fomcminutes20260429.pdf).

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-19. `9e807f3f-c7c7-515d-895a-a18fbb170141`

- Recorded outcome: **YES** · present date `2026-05-16 17:43:49.456916` (window ends end of UTC day `2026-05-16`) · expected resolution `2026-07-01T00:00:00`

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

**Exact later resolution packet — this is the object under audit**

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
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-20. `e35b83e5-edc5-5778-9c3a-7ac64e877a6f`

- Recorded outcome: **YES** · present date `2026-04-30 18:28:43.603372` (window ends end of UTC day `2026-04-30`) · expected resolution `2026-06-01 00:00:00`

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

**Exact later resolution packet — this is the object under audit**

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
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-21. `fe39b56b-8133-5518-918a-09f312b235df`

- Recorded outcome: **YES** · present date `2026-05-03 05:34:54.852556` (window ends end of UTC day `2026-05-03`) · expected resolution `2026-06-01 00:00:00`

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

**Exact later resolution packet — this is the object under audit**

The question resolves YES. Both conditions were met:

1. IPO occurred before deadline: Cerebras Systems completed its IPO and its Class A common stock began trading on the Nasdaq under ticker CBRS on Thursday, May 14, 2026, which is on or before the June 1, 2026 23:59 UTC deadline [f3018b].

2. Closing price strictly above offer price: The IPO offer price was $185.00 per share (priced May 13, 2026, above its expected range), and the closing price on the first day of trading (May 14, 2026) was $311.07 per share — a 68% first-day gain. Since $311.07 > $185.00, the condition is satisfied [f3018b].

Supporting excerpts from CNBC: "Cerebras shares opened at $350, up from its $185 IPO price, and closed up 68% at $311.07" and "Cerebras Systems soared 68% in its Nasdaq debut on Thursday, closing at $311.07 after selling shares at $185, well above the company's expected range" [f3018b].

This is corroborated by multiple other credible sources including Reuters, WSJ, Fortune, IPOScoop (which reported the $185 IPO price and 68.15% first-day gain), and Hiive (which listed "Cerebras Systems IPO Price: $185.00/sh. Day 1 closing price: $311.07/sh").

Source URL: https://www.cnbc.com/2026/05/14/cerebras-cbrs-stock-trade-nasdaq-ipo.html

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-22. `96632c8c-1bdd-5deb-9f65-deab719ac39b`

- Recorded outcome: **YES** · present date `2026-05-16 15:44:02.769519` (window ends end of UTC day `2026-05-16`) · expected resolution `2026-07-01T00:00:00`

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

**Exact later resolution packet — this is the object under audit**

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
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-23. `3f5d8fa9-7140-5215-b8b9-b71c501c738d`

- Recorded outcome: **YES** · present date `2026-05-13 21:45:28.311211` (window ends end of UTC day `2026-05-13`) · expected resolution `2026-05-28 00:00:00`

**Question**

Will the SARB revise its 2026 headline inflation forecast upward in the May 28, 2026 MPC statement compared to the March 2026 statement?

**Resolution criteria**

This question resolves YES if the 2026 annual average headline inflation forecast stated in the SARB MPC statement released on May 28, 2026 (SAST, UTC+2) is strictly greater than 3.7% (the figure from the March 26, 2026 statement [[PDF] Repo rate held at 6.75%. No rate cuts expected in 2026 - Momentum](https://sls-fresco.momentum.co.za/files/documents/corporate/mim/updates-and-news/sarb-interest-rate-decision-26-march-2026.pdf)).

This question resolves NO if the 2026 annual average headline inflation forecast in the May 28, 2026 statement is equal to or less than 3.7%.

If the May 28, 2026 MPC statement does not provide a comparable 2026 annual average headline inflation forecast number, or if the statement is not published by July 1, 2026 (SAST), the question resolves N/A.

The resolution source is the official SARB Monetary Policy Committee statement published at: https://www.resbank.co.za/en/home/publications/publication-detail-pages/statements/monetary-policy-statements

For clarity: "headline inflation" refers to the overall Consumer Price Index (CPI) inflation rate as published by Statistics South Africa (https://www.statssa.gov.za/?page_id=735&id=1), encompassing all goods and services including food and energy.

**Exact later resolution packet — this is the object under audit**

The official SARB Monetary Policy Committee statement used for resolution is the May 2026 statement at https://www.resbank.co.za/en/home/publications/publication-detail-pages/statements/monetary-policy-statements/2026/may, published/released on 2026-05-28 [Statement of the Monetary Policy Committee May 2026](https://www.resbank.co.za/en/home/publications/publication-detail-pages/statements/monetary-policy-statements/2026/may). In that statement, SARB states: “Our forecast now has headline inflation averaging 4.4% this year and 3.7% next year” [Statement of the Monetary Policy Committee May 2026](https://www.resbank.co.za/en/home/publications/publication-detail-pages/statements/monetary-policy-statements/2026/may). Because the statement is dated May 28, 2026, “this year” refers to the 2026 annual average headline inflation forecast; the relevant value is therefore 4.4% [Statement of the Monetary Policy Committee May 2026](https://www.resbank.co.za/en/home/publications/publication-detail-pages/statements/monetary-policy-statements/2026/may). The resolution criterion asks whether this 2026 annual average headline inflation forecast is strictly greater than 3.7%. Since 4.4% > 3.7%, the question resolves YES.

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-24. `72178d56-46a3-5048-a419-1a9d38fdba05`

- Recorded outcome: **YES** · present date `2026-05-02 21:04:40.753974` (window ends end of UTC day `2026-05-02`) · expected resolution `2026-06-01 00:00:00`

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

**Exact later resolution packet — this is the object under audit**

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
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-25. `614badaa-58d1-51b1-a5a1-9faa933aa46d`

- Recorded outcome: **YES** · present date `2026-05-12 17:59:49.260395` (window ends end of UTC day `2026-05-12`) · expected resolution `2026-07-01T00:00:00`

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

**Exact later resolution packet — this is the object under audit**

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
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-26. `b5a5f3eb-c6ff-53b8-af90-165b7a6edd91`

- Recorded outcome: **YES** · present date `2026-04-30 17:30:41.033085` (window ends end of UTC day `2026-04-30`) · expected resolution `2026-06-01 00:00:00`

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

**Exact later resolution packet — this is the object under audit**

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
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-27. `d41b3f25-a551-57fd-a6f6-4a0c91bd91f7`

- Recorded outcome: **YES** · present date `2026-05-29 03:50:50.147499` (window ends end of UTC day `2026-05-29`) · expected resolution `2026-07-01T00:00:00`

**Question**

Will President Trump sign the $72B immigration enforcement reconciliation bill into law by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the immigration enforcement reconciliation bill originating from the process initiated by [S. Con. Res. 33](https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/33) is enacted into law on or after May 12, 2026, and on or before July 1, 2026 (11:59 PM ET).

Enactment means the bill has been signed by the President, OR has become law without the President's signature under the [Presentment Clause](https://en.wikipedia.org/wiki/Presentment_Clause) (i.e., the President neither signs nor vetoes the bill within 10 days while Congress is in session), OR Congress overrides a presidential veto by a two-thirds vote in both chambers.

The bill will be identifiable as the reconciliation measure reported pursuant to S. Con. Res. 33, primarily funding ICE and CBP. Once enacted, it will be assigned a Public Law number.

Resolution will be verified via the official [Congress.gov](https://www.congress.gov/) record of enrolled bills and public laws, or via the [Federal Register](https://www.federalregister.gov/). If no such law is enacted by 11:59 PM ET on July 1, 2026, this question resolves **No**.

**Exact later resolution packet — this is the object under audit**

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
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-28. `a1ec0332-9728-5b5b-9120-43f5f7c13a43`

- Recorded outcome: **YES** · present date `2026-05-01 17:32:01.956816` (window ends end of UTC day `2026-05-01`) · expected resolution `2026-06-01 00:00:00`

**Question**

Will the U.S. Department of Education publish a final rule implementing the Workforce Pell Grant program in the Federal Register by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if a document categorized as a "Rule" or "Final Rule" (not a "Proposed Rule" or "Notice") implementing the [Workforce Pell Grant program](https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant) is published in the Federal Register on or after April 30, 2026, and no later than June 1, 2026, 11:59 PM Eastern Time.

The "Workforce Pell Grant program" refers to the program established under Section 401A of the Higher Education Act of 1965, as added by Section 30201 of the One Big Beautiful Bill Act (H.R. 1), which extends Pell Grant eligibility to eligible short-term workforce training programs [https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant](https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant).

A "final rule" means a document published in the Federal Register under the "Rules and Regulations" section, with document type classified as "Rule" — as distinct from a "Proposed Rule" (which the NPRM already is) or a "Notice."

The resolution source is the [Federal Register](https://www.federalregister.gov/) and specifically the [Department of Education's documents page](https://www.federalregister.gov/agencies/education-department). The question resolves **No** if no such final rule appears by the deadline.

This resolution criterion excludes the already-published NPRM (March 9, 2026), which is a proposed rule, not a final rule.

**Exact later resolution packet — this is the object under audit**

The question resolves YES. The U.S. Department of Education published a final rule implementing the Workforce Pell Grant program in the Federal Register on May 19, 2026, which falls within the resolution window (on or after April 30, 2026 and no later than June 1, 2026, 11:59 PM ET).

The document is at https://www.federalregister.gov/documents/2026/05/19/2026-10013/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant and is titled "Accountability in Higher Education and Access Through Demand-Driven Workforce Pell: Pell Grant Exclusion Relating to Other Grant Aid; and Workforce Pell Grants."

Key verification points [108186]:
- Document type: The Federal Register classifies this document explicitly as a "Rule" (i.e., a Final Rule in the Rules and Regulations section), NOT a "Proposed Rule" or "Notice."
- Publication date: 05/19/2026, which is within the required window of April 30, 2026 to June 1, 2026.
- Subject matter: It implements the Workforce Pell Grant program established by H.R. 1 (the One Big Beautiful Bill Act / referred to in the rule as the Working Families Tax Cuts Act), signed into law July 4, 2025. The rule amends § 600.10 to require Secretary approval of eligible workforce programs and implements the Workforce Pell Grant provisions, matching the program defined under Section 401A of the HEA.

This is distinct from and supersedes the NPRM (a Proposed Rule) published March 9, 2026 (document 2026-04520), which the resolution criteria explicitly excluded. The May 19, 2026 document is the FINAL rule, sharing the same title but being a separate, later-published "Rule"-type document.

Note: An initial exhaustive scan of the Department of Education's agency listing page failed to surface this final rule and incorrectly suggested NO, but a direct query of the actual Federal Register document confirmed its existence, document type ("Rule"), and publication date (05/19/2026) [108186]. Multiple secondary sources (ed.gov press release titled "U.S. Department of Education Issues Final Rule to Create New Workforce Pell Grant Program," and fsapartners.ed.gov "Final" designation dated 2026-05-19) corroborate that this is the final rule.

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-29. `a653ccb0-0617-5d42-b6c1-5d05e8b8fbb9`

- Recorded outcome: **YES** · present date `2026-05-16 19:25:38.361614` (window ends end of UTC day `2026-05-16`) · expected resolution `2026-07-01T00:00:00`

**Question**

Will the U.S. Supreme Court rule in favor of the FCC (reversing the Fifth Circuit) in FCC v. AT&T, Inc. (No. 25-406) by June 30, 2026?

**Resolution criteria**

This question resolves **Yes** if, between May 12, 2026 and July 1, 2026 (11:59 PM Eastern Time), the U.S. Supreme Court issues an opinion in FCC v. AT&T, Inc. (No. 25-406) that **reverses** the Fifth Circuit's judgment—i.e., the Court holds that the FCC's forfeiture order process does not violate the Seventh Amendment or Article III, thereby upholding the FCC's authority to issue such orders. A "vacated and remanded" disposition also counts as **Yes** if the Court's opinion rejects the Fifth Circuit's core holding that the FCC's process violates the Seventh Amendment, even if the case is remanded on other grounds. A partial reversal that rejects the Seventh Amendment holding counts as Yes.

This question resolves **No** if:
- The Court affirms the Fifth Circuit's decision (upholding the carriers' Seventh Amendment claim), OR
- The Court dismisses the case as improvidently granted (DIG), which would leave the Fifth Circuit's judgment intact, OR
- No opinion is issued by July 1, 2026 at 11:59 PM Eastern Time.

**Primary resolution source:** The official Supreme Court docket page (https://www.supremecourt.gov/docket/docketfiles/html/public/25-406.html) and the Opinions of the Court page (https://www.supremecourt.gov/opinions/slipopinion/25). The disposition language in the Court's syllabus and opinion will determine resolution.

**Exact later resolution packet — this is the object under audit**

The question resolves YES.

Resolution window: May 12, 2026 – July 1, 2026 (11:59 PM ET). The Supreme Court issued its opinion on June 4, 2026, squarely within this window.

Disposition: The official Supreme Court docket for No. 25-406 records the June 4, 2026 entry: "Judgment REVERSED and case REMANDED. No. 25-567, adjudged to be affirmed. Roberts, C. J., delivered the opinion of the Court, in which Alito, Sotomayor, Kagan, Gorsuch, Kavanaugh, Barrett, and Jackson, JJ., joined. Thomas, J., filed a dissenting opinion." [Docket for 25-406 - Supreme Court](https://www.supremecourt.gov/docket/docketfiles/html/public/25-406.html) (https://www.supremecourt.gov/docket/docketfiles/html/public/25-406.html)

This is a REVERSAL of the Fifth Circuit's judgment in FCC v. AT&T (No. 25-406), which is exactly the condition the resolution criteria specify for YES ("reverses the Fifth Circuit's judgment—i.e., the Court holds that the FCC's forfeiture order process does not violate the Seventh Amendment or Article III").

Merits: The 8-1 majority (Chief Justice Roberts) held that it does not violate the Seventh Amendment for the FCC to issue forfeiture orders without a jury, because forfeiture orders under §503(b) do not definitively resolve the parties' legal obligations until DOJ brings a court enforcement action. This is confirmed by the slip opinion (https://www.supremecourt.gov/opinions/25pdf/25-406_nmip.pdf) and corroborated by SCOTUSblog ("Reversed and remanded, 8-1, in an opinion by John Roberts on Jun 4, 2026. Justice Thomas wrote a dissenting opinion."), the Congressional Research Service, the FCC's own release, and numerous law firm summaries (Mayer Brown, Faegre Drinker, Morgan Lewis, etc.), all dated June 4, 2026.

None of the NO conditions apply: the Court did not affirm the Fifth Circuit, did not dismiss as improvidently granted (DIG), and an opinion was issued before the July 1, 2026 deadline. The companion case No. 25-567 (Verizon) was "adjudged to be affirmed," but that concerns Verizon's petition; the core FCC v. AT&T judgment reversing the Fifth Circuit and rejecting the Seventh Amendment holding is what governs this question, and it resolves YES.

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-30. `81d4c81e-bbd1-5da2-bd1a-d4f7677ea272`

- Recorded outcome: **YES** · present date `2026-05-02 22:27:59.848494` (window ends end of UTC day `2026-05-02`) · expected resolution `2026-06-01 00:00:00`

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

**Exact later resolution packet — this is the object under audit**

The question resolves YES.

Resolution criteria require a public Form S-1 registration statement filed by Space Exploration Technologies Corp. (SpaceX) to appear on SEC EDGAR on or after April 30, 2026 12:00 AM ET and before June 1, 2026 11:59 PM ET.

Evidence: SEC EDGAR shows that Space Exploration Technologies Corp. (CIK 0001181412) filed a Form S-1 on May 20, 2026, under SEC Accession Number 0001628280-26-036936, File No. 333-296070, accepted 2026-05-20 16:40:21 ET. The EDGAR filing index explicitly lists "Filing Date: 2026-05-20" and "Type: S-1 | Act: 33." (Source: https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm). The SEC full-text S-1 search results for "Space Exploration Technologies" likewise list this S-1 dated 2026-05-20 [https://efts.sec.gov/LATEST/search-index?q=%22Space+Exploration+Technologies%22&forms=S-1](https://efts.sec.gov/LATEST/search-index?q=%22Space+Exploration+Technologies%22&forms=S-1) [https://efts.sec.gov/LATEST/search-index?q=%22Space Exploration Technologies%22&forms=S-1](https://efts.sec.gov/LATEST/search-index?q=%22Space Exploration Technologies%22&forms=S-1).

The actual registration statement document confirms it is a "FORM S-1 REGISTRATION STATEMENT UNDER THE SECURITIES ACT OF 1933" for Space Exploration Technologies Corp. (https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/spaceexplorationtechnologi.htm).

This is a genuine Form S-1 (not S-1/A), filed by the correctly named entity "Space Exploration Technologies Corp.", and its filing date of May 20, 2026 falls strictly within the resolution window (April 30 – June 1, 2026). This is distinct from the confidential draft registration statement reportedly submitted April 1, 2026, which would not have been publicly visible on EDGAR; the May 20 filing is the public S-1 that satisfies the criteria.

A subsequent Form S-1/A amendment was filed June 1, 2026 (Accession 0001628280-26-039276) [https://efts.sec.gov/LATEST/search-index?q=%22Space+Exploration+Technologies%22&forms=S-1](https://efts.sec.gov/LATEST/search-index?q=%22Space+Exploration+Technologies%22&forms=S-1), but the original public S-1 already appeared within the window, so the YES condition is met regardless.

Therefore the question resolves YES (1).

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-31. `bd90f010-d501-5c54-a6a0-f4ed25ba1757`

- Recorded outcome: **YES** · present date `2026-05-14 01:24:17.608235` (window ends end of UTC day `2026-05-14`) · expected resolution `2026-06-19T00:00:00`

**Question**

Will the European Commission announce a new Growth Plan disbursement for at least one Western Balkan country between June 5 and June 19, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 12, 2026, and no later than 23:59 UTC on June 19, 2026, the European Commission publishes an official announcement (press release, Implementing Decision, or statement) confirming that a new disbursement of funds under the Reform and Growth Facility for the Western Balkans has been authorized for at least one of the following countries: Albania, Bosnia and Herzegovina, Kosovo, Montenegro, North Macedonia, or Serbia.

The "Growth Plan" refers to the Reform and Growth Facility for the Western Balkans, as described at: https://enlargement.ec.europa.eu/funding-technical-assistance/reform-and-growth-facility-western-balkans_en

An "announcement of a disbursement" means an official press release or publication of a Commission Implementing Decision on the European Commission's website stating that a payment (whether grant or loan) has been authorized or approved for release to one or more of the listed countries. Pre-financing payments do not count; only milestone-based releases qualify.

"Western Balkan country" means one of: Albania, Bosnia and Herzegovina, Kosovo, Montenegro, North Macedonia, or Serbia.

The primary resolution source is the European Commission Press Corner (https://ec.europa.eu/commission/presscorner/home/en) and the Reform and Growth Facility page (https://enlargement.ec.europa.eu/funding-technical-assistance/reform-and-growth-facility-western-balkans_en).

If no such announcement is published by 23:59 UTC on June 19, 2026, the question resolves as **No**.

**Exact later resolution packet — this is the object under audit**

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
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### YES-32. `555d2be7-6581-5345-9052-655b8c898df0`

- Recorded outcome: **YES** · present date `2026-05-14 10:00:12.053424` (window ends end of UTC day `2026-05-14`) · expected resolution `2026-07-01T00:00:00`

**Question**

Will the Supreme Court's opinion in Mullin v. Doe feature at least one dissenting opinion?

**Resolution criteria**

This question resolves as **Yes** if the Supreme Court of the United States issues its opinion in Mullin v. Doe (Docket No. 25-1083, consolidated with Trump v. Miot, No. 25-1084) on or after May 12, 2026, and by July 1, 2026 (11:59 PM Eastern Time), and that opinion includes at least one dissenting opinion.

A **dissenting opinion** is defined as a separate opinion filed by one or more Justices who disagree with the judgment (i.e., the outcome or disposition) reached by the majority or plurality of the Court. An opinion that concurs in the judgment but disagrees with the reasoning (a "concurrence in the judgment") does NOT count as a dissent. Only opinions explicitly labeled as "dissenting" or "dissent" in the official slip opinion qualify.

This question resolves as **No** if:
- The opinion is issued within the specified window and is unanimous (no Justice files a dissenting opinion), OR
- No opinion is released by the Supreme Court in this case by July 1, 2026 (11:59 PM Eastern Time).

**Resolution source:** The official slip opinion as published on the Supreme Court of the United States website at https://www.supremecourt.gov/opinions/slipopinion/25 (the opinions page for the October 2025 Term).

**Exact later resolution packet — this is the object under audit**

The Supreme Court issued its opinion in Mullin v. Doe (Docket No. 25-1083, consolidated with Trump v. Miot, No. 25-1084) on June 25, 2026 — squarely within the resolution window of May 12, 2026 through July 1, 2026 (11:59 PM ET).

The case was decided 6-3. Justice Alito announced the judgment of the Court and delivered the opinion of the Court (reversed and remanded), holding that Section 1254a(b)(5)(A) bars judicial review of non-constitutional TPS termination claims [201590].

Crucially, the official slip opinion at https://www.supremecourt.gov/opinions/25pdf/25-1083_f204.pdf includes a dissenting opinion. The syllabus explicitly states: "KAGAN, J., filed a dissenting opinion, in which SOTOMAYOR and JACKSON, JJ., joined." [ce9e12]. SCOTUSblog's case page corroborates that Justice Kagan filed a dissenting opinion joined by Justices Sotomayor and Jackson in this 6-3 decision [201590].

Because (a) the opinion was issued within the required window, and (b) it includes an opinion explicitly labeled "dissenting" — filed by Justices who disagreed with the judgment (a genuine dissent, not merely a concurrence in the judgment) — the question resolves YES.

Resolution source: The official October 2025 Term slip opinions page (https://www.supremecourt.gov/opinions/slipopinion/25), which lists the Mullin v. Doe opinion dated 06/25/2026, and the underlying slip opinion PDF (https://www.supremecourt.gov/opinions/25pdf/25-1083_f204.pdf) [ce9e12].

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

## Realized NO — 32 items remaining

### NO-1. `d2c5fcaa-b273-5787-9846-32c25c11f11b`

- Recorded outcome: **NO** · present date `2026-05-03 02:44:56.648996` (window ends end of UTC day `2026-05-03`) · expected resolution `2026-06-01 00:00:00`

**Question**

Will the U.S. government announce a final decision on the Section 232 investigation into polysilicon imports by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 1, 2026 (00:00 UTC) and on or before June 1, 2026 (23:59 UTC), the U.S. government publicly announces a final decision on the Section 232 national security investigation into polysilicon and its derivatives.

A "final decision" is defined as either:
1. A **Presidential Proclamation** imposing, modifying, or declining to impose tariffs, quotas, or other trade remedies based on the investigation; or
2. An official announcement from the **Secretary of Commerce** or the **White House** that the President has made a final determination on the investigation (including a determination to take no action).

The announcement must appear on an official U.S. government source, such as:
- The White House Briefing Room (https://www.whitehouse.gov/briefing-room/)
- The Department of Commerce Newsroom (https://www.commerce.gov/news)
- The Federal Register (https://www.federalregister.gov/)

Interim reports, leaked drafts, or unofficial statements do not count. The question resolves **No** if no such formal announcement is made by June 1, 2026 (23:59 UTC).

**Exact later resolution packet — this is the object under audit**

The question resolves NO because no Presidential Proclamation or official Commerce/White House announcement of a final determination on the Section 232 polysilicon investigation was made between May 1, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC).

Key evidence:
- A Covington & Burling LLP alert dated April 23, 2026 explicitly listed the "Polysilicon & Its Derivatives" Section 232 investigation as still "Pending," with an expected "Announcement of Action (If Any)" not until "Mid-July 2026" [295812]. This confirms no final decision had been made before the resolution window, and that the anticipated decision date falls AFTER the June 1, 2026 deadline.
- A Congressional Research Service report (R48549), updated January 12, 2026, listed polysilicon under "Potential Tariff Actions: Section 232" with status "Under Investigation," with no final determination or proclamation [57e6a9].
- The PV-Tech page on polysilicon Section 232 tariffs (originally Oct 2025), whose live news feed contained items dated June 1–2, 2026, contained no report of any final decision/proclamation on polysilicon as of the close of the resolution window [cb4689].

While the Trump administration issued numerous other Section 232 proclamations in early 2026 (e.g., advanced semiconductors on Jan 14, 2026; steel/aluminum/copper on April 2, 2026; pharmaceuticals on April 2, 2026), none of these concerned polysilicon. The official BIS Section 232 investigations page continued to list the polysilicon investigation (initiated July 1, 2025) without any final determination.

Because the resolution window (May 1 – June 1, 2026) closed with no qualifying final decision announced on any official U.S. government source, the question resolves NO (0).

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-2. `987d2afa-d57c-55fd-aba5-1121bac875c0`

- Recorded outcome: **NO** · present date `2026-05-16 16:30:50.564395` (window ends end of UTC day `2026-05-16`) · expected resolution `2026-07-01T00:00:00`

**Question**

Will the Italian Constitutional Court declare any provision of Law 74/2025 unconstitutional in the joined Campobasso/Mantua proceedings, with a ruling issued on or after May 12, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 (00:00 CEST) and on or before July 1, 2026 (23:59 CEST), the Italian Constitutional Court (Corte Costituzionale) publishes a judgment (sentenza) declaring any provision of Law No. 74/2025 unconstitutional (illegittimità costituzionale) in the joined proceedings originating from the courts of Campobasso and Mantua scheduled for hearing on June 9, 2026. The March 12, 2026 ruling rejecting the Turin challenge does not count toward resolution.

This question resolves **No** if, by July 1, 2026 (23:59 CEST):
- The Court upholds the law as constitutional;
- The Court declares the challenges inadmissible or unfounded;
- The Court issues only an "admonitory" ruling (monito) without a formal declaration of unconstitutionality; or
- No ruling on these proceedings has been published.

**Clarifications:**
- A **partial declaration of unconstitutionality** (e.g., striking down one provision while upholding others, or an "interpretive" declaration that a provision is unconstitutional insofar as it is interpreted in a certain way — sentenza interpretativa di accoglimento) **does** count as a Yes resolution.
- A mere admonitory ruling (monito), in which the Court signals concerns but does not formally declare any provision unconstitutional, does **not** count as a Yes resolution.
- The "Mantua referral" refers to the ordinanza from the Tribunale di Mantova and the "Campobasso referrals" refer to the two ordinanze from the Tribunale di Campobasso, all challenging provisions of Law 74/2025 and consolidated for the June 9, 2026 hearing.

**Primary resolution source:** The official website of the Italian Constitutional Court at [https://www.cortecostituzionale.it/](https://www.cortecostituzionale.it/), specifically the decisions/pronunce section. Secondary confirmation may be obtained from credible legal news sources such as Mondaq, Mazzeschi, or major Italian legal publications.

**Exact later resolution packet — this is the object under audit**

The question resolves NO.

**Antecedent / setup:** The Italian Constitutional Court did hold the consolidated public hearing on the Campobasso and Mantua proceedings challenging Law 74/2025 on June 9, 2026. These are the correct joined proceedings: ordinanza n. 4/2026 (Tribunale di Mantova) and ordinanze nn. 40/2026 and 41/2026 (Tribunale di Campobasso), all challenging Article 3-bis of Law 91/1992 as introduced by Law 74/2025 (Decreto Tajani). This is distinct from the earlier Turin challenge (ordinanza 167/2025 Torino), which was decided by sentenza n. 63/2026, deposited April 30, 2026, and declared "non fondata" (unfounded) — that decision is both outside the resolution window and about a different referral, so it does not count [Italian citizenship: Constitutional Court hearing held June 9th about ...](https://www.mazzeschi.it/italian-citizenship-constitutional-court-hearing-held-june-9th-about-legitimacy-of-new-citizenship-rules/) [Italian Constitutional Court: June 9, 2026 Hearing](https://www.apriglianos.com/en/italian-constitutional-court-hearing-of-june-9-2026-on-citizenship-by-descent-what-happened-and-when-the-ruling-is-expected/).

**Core finding — no qualifying ruling published in the window:** After the June 9, 2026 hearing, the Court reserved its decision. As of June 11–12, 2026, no decision on the Campobasso/Mantua proceedings had been announced or published, and the ruling was expected only "between mid-July and September 2026" [Italian Constitutional Court: June 9, 2026 Hearing](https://www.apriglianos.com/en/italian-constitutional-court-hearing-of-june-9-2026-on-citizenship-by-descent-what-happened-and-when-the-ruling-is-expected/), with Mazzeschi similarly reporting that "A decision is expected in the short term, but there is no fixed timeframe for its publication" and that no official press release anticipating the outcome had been issued [Italian citizenship: Constitutional Court hearing held June 9th about ...](https://www.mazzeschi.it/italian-citizenship-constitutional-court-hearing-held-june-9th-about-legitimacy-of-new-citizenship-rules/). Because the resolution window closes July 1, 2026 (23:59 CEST), and no sentenza declaring any provision of Law 74/2025 unconstitutional in these proceedings was published by that date, the "No ruling on these proceedings has been published" branch of the No criteria applies.

**Ruling out the one document that was published in-window:** The only Constitutional Court pronouncement tied to these proceedings that was published within the window is ordinanza n. 102/2026 (deliberated June 8, 2026, deposited/"Depositata in Cancelleria il 9 giugno 2026"). However, this is a purely procedural order in the joined proceedings (reg. ord. 40 and 41 of 2026) that only declared inadmissible the interventions of third parties (Confederazione degli Italiani nel mondo and certain individuals). It did NOT address the merits and did NOT declare any provision of Law 74/2025 unconstitutional [Corte Costituzionale - Sito ufficiale](https://www.cortecostituzionale.it/scheda-pronuncia/2026/102). Therefore it does not trigger a YES.

Since no partial or interpretive declaration of unconstitutionality (sentenza interpretativa di accoglimento) — and indeed no merits decision at all — was published on the Campobasso/Mantua proceedings between May 12 and July 1, 2026, the question resolves NO.

Primary source (Italian Constitutional Court official site): https://www.cortecostituzionale.it/scheda-pronuncia/2026/102 (procedural ordinanza only) [Corte Costituzionale - Sito ufficiale](https://www.cortecostituzionale.it/scheda-pronuncia/2026/102). Secondary legal sources confirming the decision was reserved with publication expected after July 1: https://www.apriglianos.com/en/italian-constitutional-court-hearing-of-june-9-2026-on-citizenship-by-descent-what-happened-and-when-the-ruling-is-expected/ [Italian Constitutional Court: June 9, 2026 Hearing](https://www.apriglianos.com/en/italian-constitutional-court-hearing-of-june-9-2026-on-citizenship-by-descent-what-happened-and-when-the-ruling-is-expected/) and https://www.mazzeschi.it/italian-citizenship-constitutional-court-hearing-held-june-9th-about-legitimacy-of-new-citizenship-rules/ [Italian citizenship: Constitutional Court hearing held June 9th about ...](https://www.mazzeschi.it/italian-citizenship-constitutional-court-hearing-held-june-9th-about-legitimacy-of-new-citizenship-rules/).

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-3. `1059ecce-7633-59cc-9bab-df341bfe35b6`

- Recorded outcome: **NO** · present date `2026-05-12 14:59:03.377445` (window ends end of UTC day `2026-05-12`) · expected resolution `2026-07-01T00:00:00`

**Question**

Will any match in Group J of the 2026 FIFA World Cup end in a 0-0 draw?

**Resolution criteria**

This question resolves **Yes** if at least one of the six Group J matches at the 2026 FIFA World Cup ends with a final score of 0-0 at the end of regulation time (90 minutes plus any stoppage/injury time added by the referee). Extra time and penalty shootouts are not applicable in the group stage, but for the avoidance of doubt, only the score at the end of regulation/stoppage time counts — a "0-0 draw" means neither team has scored any goals by the final whistle of normal time.

The question resolves **No** if all six Group J matches end with at least one goal scored.

**Teams comprising Group J:** Argentina, Algeria, Austria, and Jordan [2026 FIFA World Cup Group J - Wikipedia](https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_Group_J).

**Matches considered:** Only Group J matches occurring on or after May 10, 2026 (UTC) are considered. The six scheduled matches are on June 16, June 22, and June 27, 2026 (all dates UTC) [2026 FIFA World Cup Group J - Wikipedia](https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_Group_J).

**Primary resolution source:** The official FIFA World Cup 2026 match results, available at https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/standings or the FIFA Match Centre at https://www.fifa.com/en/match-centre [FIFA/Coca-Cola World Rankings](https://www.fifa.com/en/world-rankings). If the FIFA website is unavailable, credible secondary sources such as ESPN (https://www.espn.com/soccer/standings/_/league/fifa.world) or UEFA/AFC official match reports may be used.

**Exact later resolution packet — this is the object under audit**

The question resolves NO because none of the six 2026 FIFA World Cup Group J matches (Argentina, Algeria, Austria, Jordan) ended in a 0-0 draw. All six matches were played on the scheduled dates (June 16, 22, and 27, 2026 — all on/after the May 10, 2026 cutoff) and every one had at least one goal scored.

The six final scores (regulation time; group-stage matches have no extra time, so the final score IS the regulation-time score), confirmed consistently across sources:
- June 16: Argentina 3–0 Algeria [143643][7223af]
- June 16: Austria 3–1 Jordan [143643][7223af]
- June 22: Argentina 2–0 Austria [143643][7223af]
- June 22: Jordan 1–2 Algeria [143643][7223af]
- June 27: Jordan 1–3 Argentina (Argentina 3–1) [143643][7223af]
- June 27: Algeria 3–3 Austria [143643][7223af]

Every match had goals; the lowest goal totals were the three 2-goal games (3–0, 2–0), none of which were goalless. Therefore the condition "at least one match ends 0-0" was not met, resolving NO.

Sources used to verify:
- Wikipedia "2026 FIFA World Cup Group J" (https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_Group_J), which listed all six results [143643].
- AS "World Cup 2026 Group J final standings" (https://en.as.com/soccer/world-cup/world-cup-2026-group-j-final-standings-results-and-teams-qualified-for-the-round-of-32-f202606-n/), listing identical results [7223af].
- FIFA official match report for the opener confirms Argentina 3–0 Algeria (https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/argentina-v-algeria-highlights-match-report); the FIFA Group J focus page also confirms the group composition [9fd4bf]. The FIFA primary standings/match centre pages (https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/standings) corroborate these outcomes.

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-4. `752483bd-c61e-58a0-9fd5-6033eceea25f`

- Recorded outcome: **NO** · present date `2026-05-02 21:24:38.401461` (window ends end of UTC day `2026-05-02`) · expected resolution `2026-06-01 00:00:00`

**Question**

Will Missouri's SB 838 (nuclear energy expansion bill) be signed into law by the Governor by June 1, 2026?

**Resolution criteria**

This question resolves YES if Missouri Senate Bill 838 (2026 session) is signed into law by the Governor of Missouri, becomes law without the Governor's signature, or is vetoed and subsequently overridden by the legislature, with such action occurring on or after May 1, 2026 and no later than 11:59 PM Central Time on June 1, 2026.

This question resolves NO if none of the above conditions are met by 11:59 PM CT on June 1, 2026—including if the bill is vetoed without override, fails to pass either chamber, or remains unsigned.

The primary resolution source is the Missouri General Assembly official bill tracking page for SB 838: https://www.senate.mo.gov/BillTracking/Bills/BillInformation?year=2026&billid=274. Secondary sources include the Missouri Governor's official website and credible news reporting (e.g., Missouri Independent, Missourinet, AP).

**Exact later resolution packet — this is the object under audit**

The question resolves NO. To resolve YES, Missouri SB 838 (2026 session) would have had to be signed into law, become law without the Governor's signature, or be vetoed and overridden, with that action occurring between May 1, 2026 and 11:59 PM CT on June 1, 2026.

Evidence:
- The official Missouri General Assembly bill tracking page for SB 838 (https://www.senate.mo.gov/BillTracking/Bills/BillInformation?year=2026&billid=274) shows the bill's last status as "Informal Calendar S Bills for Third Reading" [2f6eeb]. This means the bill never even passed the Senate on Third Reading; it never advanced to the House and was never sent to the Governor. None of the three YES conditions (signature, law without signature, veto override) were met.
- The 2026 Missouri legislative session adjourned (sine die) on Friday, May 15, 2026, with the legislature concluding its work (corroborated by Missouri Bar 2026 Legislative Updates and Missouri Independent's "Missouri legislature ends 2026 session" reporting found via Google). Because SB 838 was still stuck on the Senate's Informal Calendar at adjournment, the bill died without passage. Consequently, it could not have been signed, become law, or undergone a veto/override during the May 1 – June 1, 2026 window.

Since the bill never passed either chamber and never reached the Governor, none of the YES conditions occurred by the June 1, 2026 deadline, so the question resolves NO.

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-5. `2d86237a-cccc-5df6-9d54-5af3e37a7de8`

- Recorded outcome: **NO** · present date `2026-05-02 17:24:58.775760` (window ends end of UTC day `2026-05-02`) · expected resolution `2026-06-01 00:00:00`

**Question**

Will the 11th Circuit Court of Appeals issue a ruling on American Oversight's appeal (No. 25-13400-A) regarding the release of Volume 2 of the Special Counsel's report by June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if the U.S. Court of Appeals for the Eleventh Circuit issues a ruling on or after May 1, 2026, and on or before June 1, 2026, 11:59 PM Eastern Time (ET), in the appeal filed by American Oversight (Docket No. 25-13400-A) concerning the release of Volume 2 of Special Counsel Jack Smith's final report on the classified documents investigation involving Donald Trump, Walt Nauta, and Carlos De Oliveira.

A "ruling" is defined as a written opinion (published or unpublished), order, or judgment that resolves the merits of the appeal—i.e., affirming, reversing, vacating, or remanding the district court's order. Procedural or interlocutory orders (such as scheduling orders, motions for extensions of time, stays pending further proceedings, or orders related to briefing) do **not** count as a ruling for resolution purposes.

If no such merits-resolving ruling is issued by 11:59 PM ET on June 1, 2026, the question resolves as **No**.

**Resolution source:** The official docket of the U.S. Court of Appeals for the Eleventh Circuit, accessible via PACER at https://ecf.ca11.uscourts.gov/, and/or credible legal reporting (e.g., Reuters, AP, Law.com, SCOTUSblog).

**Exact later resolution packet — this is the object under audit**

The question resolves NO. It asks whether the 11th Circuit Court of Appeals issued a merits-resolving ruling (affirming, reversing, vacating, or remanding) on American Oversight's appeal (No. 25-13400-A) concerning the release of Volume 2 of Special Counsel Jack Smith's report, during the window May 1, 2026 through June 1, 2026, 11:59 PM ET.

The Knight First Amendment Institute maintains a detailed case tracker for this litigation (United States v. Trump et al.) at https://knightcolumbia.org/cases/united-states-v-trump-et-al. As of late May 2026, the status of the appeal was "Briefing ongoing on appeal" [b92236]. The only docketed 11th Circuit activity in the relevant window was an "Order Consolidating Appeals and Setting Briefing Schedule" dated May 28, 2026 [b92236]. That is a procedural/scheduling order, which the resolution criteria explicitly exclude from counting as a "ruling" (procedural or interlocutory orders such as scheduling orders or orders related to briefing do not count).

Since briefing was still ongoing and no opinion, order, or judgment resolving the merits of the appeal was issued by 11:59 PM ET on June 1, 2026, the question resolves NO.

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-6. `82a5ef9e-4c98-5f0e-b972-dd99c657be88`

- Recorded outcome: **NO** · present date `2026-05-07 22:32:53.199959` (window ends end of UTC day `2026-05-07`) · expected resolution `2026-06-10T00:00:00`

**Question**

Will the United States and Iran announce a formal peace agreement ending the 2026 Iran war by June 10, 2026?

**Resolution criteria**

This question resolves YES if, on or after May 7, 2026, and before June 10, 2026 at 12:00 UTC (the start of the ECB Governing Council monetary policy meeting), the United States and Iran announce a formal peace agreement intended to permanently end the 2026 Iran war.

Specifically, all of the following must be met:

1. **Parties**: The agreement must be announced or signed by authorized representatives of both the United States government (e.g., the President, Secretary of State, or their designated negotiator) and the Iranian government (e.g., the Supreme Leader's office, the President, or the Foreign Minister).

2. **Scope**: The agreement must address the core US-Iran military conflict that began on February 28, 2026 (as described in the Wikipedia article on the 2026 Iran war: https://en.wikipedia.org/wiki/2026_Iran_war). It need not resolve all proxy conflicts but must cover the direct US-Iran hostilities.

3. **Nature of agreement**: The agreement must be described as a "peace agreement," "peace deal," "permanent ceasefire," or "comprehensive ceasefire" — i.e., an accord intended to end hostilities on a permanent or indefinite basis. A temporary ceasefire (https://en.wikipedia.org/wiki/Ceasefire) of defined duration (e.g., "14-day ceasefire," "humanitarian pause") does NOT count, nor does a mere extension of a prior temporary ceasefire. The agreement must explicitly go beyond a time-limited truce.

4. **Verification**: The announcement must be confirmed by at least two of the following sources: Reuters (https://www.reuters.com), Associated Press (https://apnews.com), BBC News (https://www.bbc.com/news), or official US State Department statements (https://www.state.gov).

If no such agreement is announced before June 10, 2026 at 12:00 UTC, the question resolves NO.

**Exact later resolution packet — this is the object under audit**

The question resolves NO. It required that, on or after May 7, 2026 and BEFORE June 10, 2026 at 12:00 UTC, authorized representatives of both the US and Iranian governments announce/sign a formal permanent peace agreement (or "comprehensive/permanent ceasefire") covering the direct US–Iran conflict, verified by at least two of Reuters/AP/BBC/State Dept.

None of these conditions were met within the window:

1. No agreement existed by June 10, 2026 — the war was still actively being fought. Per the Wikipedia "Timeline of the 2026 Iran war," Iran ended peace talks on June 1, 2026; on June 9 a US AH-64 Apache collided with an Iranian drone, triggering US strikes; and on June 10 Iran launched strikes at the US Fifth Fleet and US bases while the US struck Iranian targets — i.e., open hostilities, not peace, on the deadline date [Timeline of the 2026 Iran war - Wikipedia](https://en.wikipedia.org/wiki/Timeline_of_the_2026_Iran_war).

2. The negotiations timeline confirms the deal came AFTER the deadline. Per Wikipedia "2025–2026 Iran–United States negotiations," a preliminary framework/MOU was only reached on June 15, 2026, and the signing (the "Islamabad Memorandum") occurred June 17, 2026 [2025–2026 Iran–United States negotiations - Wikipedia](https://en.wikipedia.org/wiki/2025%E2%80%932026_Iran%E2%80%93United_States_negotiations).

3. As of May 28, 2026, only a draft 60-day MOU had been reached by negotiators; it still lacked Trump's final approval and Iran's confirmation — not a formal announced agreement by both governments [U.S. and Iran reach deal but need Trump's final approval, officials say](https://www.axios.com/2026/05/28/iran-peace-deal-trump-approval).

4. The two required verification sources both date the deal to after June 10:
   - Reuters reported Trump saying "the deal's all signed" on June 15, 2026, describing a memorandum of understanding that extends the ceasefire for a 60-day negotiation period — i.e., an interim framework, not a permanent peace accord [Trump says the US and Iran have signed a deal to end the war](https://www.reuters.com/world/iran-war-live-trump-says-us-tehran-have-reached-peace-deal-2026-06-15/).
   - BBC reported the US and Iranian presidents signed the initial deal on June 18, 2026, again a memorandum committing to negotiate a final deal within a maximum of 60 days [US and Iranian presidents sign deal aiming to end war - BBC](https://www.bbc.com/news/articles/crr8z4z2er9o).

Both the timing (all announcements/signings occurred June 14–18, 2026, after the June 10 12:00 UTC cutoff) and the nature of the eventual agreement (a 60-day interim MOU/ceasefire extension rather than a permanent peace deal) independently fail the resolution criteria. Therefore the question resolves NO.

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-7. `1fb9b683-64a4-5c17-8ab3-ff891d17af08`

- Recorded outcome: **NO** · present date `2026-05-01 13:03:17.830063` (window ends end of UTC day `2026-05-01`) · expected resolution `2026-06-01 00:00:00`

**Question**

Will the Super Heavy booster on Starship Flight 12 be successfully caught by the launch tower arms during the mission?

**Resolution criteria**

This question resolves **Yes** if, on or after April 30, 2026 (all times UTC), the Super Heavy booster from Starship Flight 12 is successfully caught by the launch tower's mechanical arms ("chopsticks") at the landing site. "Successfully caught" is defined as the booster being held by the mechanical arms without the booster touching the ground, ocean, or any surface other than the arms themselves, and remaining stably supported by the arms for at least 30 seconds after engine shutdown, as confirmed by the official SpaceX webcast or official SpaceX communications (X/Twitter account @SpaceX, or spacex.com/updates).

This question resolves **No** if:
- Flight 12 launches but the booster is diverted to the ocean, performs a splashdown, or is otherwise not caught by the tower arms;
- Flight 12 launches but the catch attempt fails (e.g., booster contacts the ground or is dropped);
- Flight 12 does not launch by June 1, 2026, 23:59 UTC.

Primary resolution sources:
- SpaceX official YouTube channel: https://www.youtube.com/@SpaceX
- SpaceX updates page: https://www.spacex.com/updates

**Exact later resolution packet — this is the object under audit**

The question asks whether the Super Heavy booster on Starship Flight 12 was successfully caught by the launch tower arms (chopsticks). It resolves NO if the booster is diverted to the ocean, performs a splashdown, or is otherwise not caught.

Antecedent check (did Flight 12 launch by June 1, 2026, 23:59 UTC?): YES. The official SpaceX mission page states Starship lifted off from Starbase, Texas on its twelfth flight test on Friday, May 22, 2026 [a9d708]. This is corroborated by Wikipedia's List of Starship launches [f19d87]. So the question is not annulled and resolves on the consequent.

Consequent check (was the booster caught by the tower arms?): NO. The official SpaceX update for Starship's Twelfth Flight Test states the booster "attempted to reignite its engines for the landing burn before experiencing a hard splashdown in the Gulf of America," and that it "was unable to light all planned engines and performed a partial boostback burn that ended early" [a9d708]. The flight plan for the V3 booster never intended a tower catch—it called for a controlled splashdown in the Gulf of Mexico. Wikipedia independently confirms the booster landing outcome as "Failure (gulf)," noting that "during the landing sequence, only one engine relit, leading the vehicle to impact the water at high speed" [f19d87].

Since the booster was not caught by the mechanical arms (it instead hit the water), the "Successfully caught" condition (held by arms for at least 30 seconds after engine shutdown without touching any other surface) was not met. The question resolves NO.

Primary source URL: https://www.spacex.com/launches/starship-flight-12 [a9d708]
Corroborating: https://en.wikipedia.org/wiki/List_of_Starship_launches [f19d87]

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-8. `a60885bc-7464-5844-abe0-7a49c0c4d6c4`

- Recorded outcome: **NO** · present date `2026-05-01 17:43:22.872565` (window ends end of UTC day `2026-05-01`) · expected resolution `2026-06-01 00:00:00`

**Question**

Will Russian Africa Corps forces re-establish a military presence in Kidal, Mali, by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after April 30, 2026 (00:00 UTC) and before June 1, 2026 (23:59 UTC), credible reporting confirms that the Russian Africa Corps has re-established a military presence in Kidal, Mali. It resolves **No** otherwise.

**Definition of "Russian Africa Corps":** The Russian Africa Corps (formerly associated with the Wagner Group) refers to the Russian state-controlled mercenary force operating in Mali under the authority of the Russian Defence Ministry. This excludes the Malian Armed Forces (FAMa) and any other non-Russian armed groups, even if operating alongside Russia. The presence must be attributed specifically to Africa Corps personnel or units.

**Definition of "military presence":** At least one of the following observable indicators must be confirmed:
- Stationing of identifiable Africa Corps personnel (uniformed troops, military advisors, or mercenaries) within the city limits of Kidal;
- Control or occupation of specific infrastructure in Kidal (e.g., the airport, military camp, or government buildings) by Africa Corps forces;
- Official Russian or Malian government statements confirming Africa Corps deployment to Kidal.

**Verification sources:** Resolution will be based on reporting from at least one of the following credible sources:
- Reuters (https://www.reuters.com/world/africa/)
- Agence France-Presse / AFP (https://www.france24.com/en/africa/)
- Associated Press (https://apnews.com/hub/africa)
- ACLED conflict data (https://acleddata.com/data-export-tool/)
- The Guardian Africa coverage (https://www.theguardian.com/world/africa)

If none of these sources report on Africa Corps presence in Kidal by June 1, 2026 (23:59 UTC), the question resolves **No**.

**Exact later resolution packet — this is the object under audit**

The question resolves NO. It asked whether the Russian Africa Corps would re-establish a military presence in Kidal, Mali between April 30, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC), as confirmed by one of five approved sources (Reuters, AFP/France 24, AP, ACLED, or The Guardian).

Background: Africa Corps withdrew from Kidal around April 26–27, 2026 after the FLA/JNIM offensive, with the Reuters-confirmed withdrawal ("Russia's Africa Corps confirms withdrawal from Mali's Kidal", 2026-04-27). Kidal then fell under rebel (Azawad Liberation Front) control.

Key approved-source evidence within the resolution window:
- The Guardian, "Mali's forces target rebel alliance in junta's fight to keep power" (2026-05-15) confirms that as of mid-May, government forces (despite the support of 2,000–2,500 Russian mercenaries) had "failed to retake much of the territory lost last month," and that the Africa Corps were withdrawing from outlying posts to reinforce Bamako's defences. The former Africa Corps barracks in Kidal were shown under rebel control, with rebel fighters in the town [Mali's forces target rebel alliance in junta's fight to keep power](https://www.theguardian.com/world/2026/may/15/mali-airstrikes-rebel-alliance-separatists).
- This is corroborated by CNN (2026-05-10), which states Kidal "returns to rebel hands" and the FLA declared the town "free," with no indication of any Russian return [Rebels jeered Putin's Africa Corps out of a key Sahel town. Now his ...](https://www.cnn.com/2026/05/10/africa/putin-africa-corps-kidal-mali-intl-cmd).

No approved verification source (Reuters, AFP/France 24, AP, ACLED, or The Guardian) reported the re-establishment of an Africa Corps presence in Kidal during the window. A social-media (Instagram) claim dated May 6 alleged the Malian Army "fully controls Kidal," but (a) it is not an approved source and (b) it refers to FAMa, which the resolution criteria explicitly exclude — the presence must be specifically attributed to Russian Africa Corps personnel/units. The Guardian's May 15 reporting also contradicts any such full recapture, showing Kidal still under rebel control.

Because none of the three required indicators (Africa Corps personnel stationed within Kidal city limits, Africa Corps control of specific Kidal infrastructure, or official Russian/Malian government statements confirming Africa Corps deployment to Kidal) were confirmed by an approved source before June 1, 2026 (23:59 UTC), the question resolves NO.

URLs used:
- The Guardian: https://www.theguardian.com/world/2026/may/15/mali-airstrikes-rebel-alliance-separatists [Mali's forces target rebel alliance in junta's fight to keep power](https://www.theguardian.com/world/2026/may/15/mali-airstrikes-rebel-alliance-separatists)
- CNN (corroborating, non-approved): https://www.cnn.com/2026/05/10/africa/putin-africa-corps-kidal-mali-intl-cmd [Rebels jeered Putin's Africa Corps out of a key Sahel town. Now his ...](https://www.cnn.com/2026/05/10/africa/putin-africa-corps-kidal-mali-intl-cmd)
- Reuters (withdrawal context): https://www.reuters.com/world/africa/russias-africa-corps-confirms-withdrawal-malis-kidal-2026-04-27/

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-9. `1aae92e0-bdac-565e-bfed-2ed0be71c16d`

- Recorded outcome: **NO** · present date `2026-05-14 05:31:38.765176` (window ends end of UTC day `2026-05-14`) · expected resolution `2026-07-01T00:00:00`

**Question**

Will either Senator Collins or Senator Murkowski publicly announce opposition to Nicole Saphier's nomination for Surgeon General by July 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after May 12, 2026 and by 11:59 PM ET on July 1, 2026, either Senator Susan Collins (R-ME) or Senator Lisa Murkowski (R-AK) publicly announces opposition to the confirmation of Dr. Nicole Saphier as U.S. Surgeon General.

"Opposition" is defined as a clear, unambiguous public statement that the senator will vote against Saphier's confirmation or cannot/will not support the nomination. This includes statements such as "I will vote no," "I oppose this nomination," or "I cannot support this nominee." Statements expressing mere "concern," "reservations," "questions," or indicating they are "reviewing the record" do NOT qualify as opposition unless accompanied by an explicit declaration of intent to vote against or not support the nomination.

Qualifying announcements may take the form of official press releases, floor speeches, committee votes against the nominee, or on-the-record statements to reporters.

Resolution source: Credible news reporting from outlets such as The New York Times (nytimes.com), Politico (politico.com), Reuters (reuters.com), the Associated Press (apnews.com), or official Senate press releases (e.g., senator websites or the Senate Press Gallery).

If the nomination is withdrawn, rejected, or confirmed before either senator publicly announces opposition as defined above, the question resolves NO.

If no qualifying public announcement of opposition is made by either senator by the deadline, the question resolves NO.

**Exact later resolution packet — this is the object under audit**

The question resolves NO. It required that, on or after May 12, 2026 and by 11:59 PM ET July 1, 2026, Senator Susan Collins (R-ME) or Senator Lisa Murkowski (R-AK) make a clear, unambiguous public statement of opposition to Dr. Nicole Saphier's confirmation as U.S. Surgeon General (an explicit "will vote no"/"cannot support" declaration, not mere concern/reservations). No such statement occurred.

Key evidence:
- Trump nominated Saphier on April 30, 2026, after withdrawing Casey Means; Saphier's nomination (PN963) was formally received by the Senate on May 11, 2026 and referred to the HELP Committee, where it remained pending — no hearing, vote, withdrawal, rejection, or confirmation — through July 1, 2026 [34c4c4, be02c3]. The withdrawal message dated 05/11/2026 pertained to Casey Means (PN730-47), not Saphier [be02c3].
- As of June 30, 2026, Axios reported Saphier's confirmation hearing was still only planned to begin in July 2026, and HELP Chair Cassidy was "very favorably impressed"; no opposition from Collins or Murkowski was reported [04e155]. An ASTHO June 2026 update likewise indicated the HELP Committee had not yet noticed a hearing for her nomination [6ea59d].
- The NPR/Houston Public Media May 2, 2026 piece stated neither senator had announced a position on Saphier [e1dbe6]. A May 4, 2026 Fox News article found no opposition announced against Saphier [9511e6].
- The only Collins/Murkowski opposition or hesitancy statements found ("undecided," "not enthusiastic," "reservations") were directed at the prior nominee Casey Means, not Saphier, and predate the resolution window [6782fc, e1dbe6].

Because no qualifying public announcement of opposition to Saphier by Collins or Murkowski was made within the window, and the nomination was neither withdrawn, rejected, nor confirmed before any such announcement (it simply remained pending), the question resolves NO.

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-10. `97cec3a5-eaeb-5fb0-9ef4-20df60713baa`

- Recorded outcome: **NO** · present date `2026-05-16 16:07:26.326308` (window ends end of UTC day `2026-05-16`) · expected resolution `2026-07-01T00:00:00`

**Question**

Will Prime Minister Edi Rama testify before the GJKKO court in the Sali Berisha 'Partizani' corruption trial by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 (00:00 CEST) and on or before July 1, 2026 (23:59 CEST), Prime Minister Edi Rama physically appears and provides testimony as a witness before the GJKKO in the "Partizani" trial involving Sali Berisha. Rama is being summoned in his capacity as former Mayor of Tirana regarding the privatization of the "Partizani" sports complex.

This question resolves **No** if Rama does not testify before the GJKKO in the "Partizani" case by July 1, 2026 (23:59 CEST). The court having accepted the summons request or having issued a summons alone is not sufficient — Rama must actually appear and testify.

**Resolution sources:** Credible reporting from BIRN Albania / Balkan Insight (https://balkaninsight.com), Albanian Daily News (https://albaniandailynews.com), Balkan Web (https://www.balkanweb.com/en/), Hashtag.al (https://www.hashtag.al/en/), or other major Albanian or international news outlets (Reuters, AP). Official GJKKO court records may also be consulted if publicly available.

**Exact later resolution packet — this is the object under audit**

The question resolves NO: there is no evidence that Prime Minister Edi Rama physically appeared and testified as a witness before the GJKKO in the Sali Berisha "Partizani" trial between May 12, 2026 (00:00 CEST) and July 1, 2026 (23:59 CEST).

Timeline of the 2026 merits trial ("gjyq në themel"), reconstructed from credible/approved Albanian outlets:
- April 30, 2026 (before the resolution window opened): The merits trial began and Taulant Balla testified. When journalists asked whether Rama would appear following his summons, Balla said appearing in court is an "individual responsibility." No confirmation Rama had appeared. (BalkanWeb) ["I hope to come here again for..."/ Balla concludes testimony in the ...](https://www.balkanweb.com/en/shpresoj-te-vij-serish-ketu-per-balla-perfundon-deshmine-ne-gjyqin-per-partizanin-a-do-paraqitet-rama-ne-seance-eshte-pergjegjesi-individuale/)
- May 11, 2026: Witness Albert Xhani testified (boldnews.al/2026/05/11 referenced in [Zbardhet dëshmia e vajzës së Fatos Lubonjës për dosjen " ...](https://boldnews.al/2026/06/22/zbardhet-deshmia-e-vajzes-se-fatos-lubonjes-per-dosjen-partizani/)).
- June 8, 2026: Former Economy Minister Genc Ruli testified (and Violeta Shqevi); the witness that day was Ruli, not Rama. (BalkanWeb) [VIDEO/ Witness in the trial against Berisha for the "Partizani" file ...](https://www.balkanweb.com/en/video-deshmitar-ne-procesin-ndaj-berishes-per-dosjen-partizani-ish-ministri-genc-ruli-shkon-ne-gjkko/); corroborated [Gjyqi për dosjen “Partizani”/ Nis seanca gjyqësore në GJKKO ...](https://dosja.al/politike/gjyqi-per-dosjen-partizani-nis-seanca-gjyqesore-ne-gjkko-berisha-nuk-es-i501344)[Zbardhet dëshmia e vajzës së Fatos Lubonjës për dosjen " ...](https://boldnews.al/2026/06/22/zbardhet-deshmia-e-vajzes-se-fatos-lubonjes-per-dosjen-partizani/).
- June 22, 2026: Former Sports Minister Ylli Pango testified; Berisha absent. Rama did not appear. (Dosja.al) [Gjyqi për dosjen “Partizani”/ Nis seanca gjyqësore në GJKKO ...](https://dosja.al/politike/gjyqi-per-dosjen-partizani-nis-seanca-gjyqesore-ne-gjkko-berisha-nuk-es-i501344); (BoldNews.al) [Zbardhet dëshmia e vajzës së Fatos Lubonjës për dosjen " ...](https://boldnews.al/2026/06/22/zbardhet-deshmia-e-vajzes-se-fatos-lubonjes-per-dosjen-partizani/).

Throughout the window, a succession of other witnesses (Balla, Xhani, Ruli, Shqevi, Pango, Fatos Lubonja's daughter) gave testimony, but Rama did not. The BalkanWeb article page from the April 30 session, whose live news feed extended through July 1, 2026, contains no report of Rama testifying ["I hope to come here again for..."/ Balla concludes testimony in the ...](https://www.balkanweb.com/en/shpresoj-te-vij-serish-ketu-per-balla-perfundon-deshmine-ne-gjyqin-per-partizanin-a-do-paraqitet-rama-ne-seance-eshte-pergjegjesi-individuale/); the June 22 BoldNews and Dosja.al reports likewise show only other witnesses and no Rama appearance [Zbardhet dëshmia e vajzës së Fatos Lubonjës për dosjen " ...](https://boldnews.al/2026/06/22/zbardhet-deshmia-e-vajzes-se-fatos-lubonjes-per-dosjen-partizani/)[Gjyqi për dosjen “Partizani”/ Nis seanca gjyqësore në GJKKO ...](https://dosja.al/politike/gjyqi-per-dosjen-partizani-nis-seanca-gjyqesore-ne-gjkko-berisha-nuk-es-i501344). During June 2026 Rama was preoccupied with large anti-government protests demanding his resignation (Hashtag.al coverage on 2026-06-17/20/24/26), and Malltezi/Berisha's side continued to complain that Rama had still not been brought to testify.

The resolution criteria explicitly state that the court accepting the summons or issuing a summons is NOT sufficient — Rama had to actually appear and testify, which did not occur by the July 1, 2026 deadline. Therefore the question resolves NO (0).

Key source URLs:
- https://www.balkanweb.com/en/video-deshmitar-ne-procesin-ndaj-berishes-per-dosjen-partizani-ish-ministri-genc-ruli-shkon-ne-gjkko/ (June 8, 2026: Genc Ruli, not Rama, testified) [VIDEO/ Witness in the trial against Berisha for the "Partizani" file ...](https://www.balkanweb.com/en/video-deshmitar-ne-procesin-ndaj-berishes-per-dosjen-partizani-ish-ministri-genc-ruli-shkon-ne-gjkko/)
- https://www.balkanweb.com/en/shpresoj-te-vij-serish-ketu-per-balla-perfundon-deshmine-ne-gjyqin-per-partizanin-a-do-paraqitet-rama-ne-seance-eshte-pergjegjesi-individuale/ (April 30 session; page news feed runs through July 1, 2026 with no Rama testimony) ["I hope to come here again for..."/ Balla concludes testimony in the ...](https://www.balkanweb.com/en/shpresoj-te-vij-serish-ketu-per-balla-perfundon-deshmine-ne-gjyqin-per-partizanin-a-do-paraqitet-rama-ne-seance-eshte-pergjegjesi-individuale/)
- https://boldnews.al/2026/06/22/zbardhet-deshmia-e-vajzes-se-fatos-lubonjes-per-dosjen-partizani/ (June 22, 2026; only other witnesses testifying) [Zbardhet dëshmia e vajzës së Fatos Lubonjës për dosjen " ...](https://boldnews.al/2026/06/22/zbardhet-deshmia-e-vajzes-se-fatos-lubonjes-per-dosjen-partizani/)
- https://dosja.al/politike/gjyqi-per-dosjen-partizani-nis-seanca-gjyqesore-ne-gjkko-berisha-nuk-es-i501344 (June 22, 2026; Ylli Pango testified, no Rama) [Gjyqi për dosjen “Partizani”/ Nis seanca gjyqësore në GJKKO ...](https://dosja.al/politike/gjyqi-per-dosjen-partizani-nis-seanca-gjyqesore-ne-gjkko-berisha-nuk-es-i501344)

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-11. `4402e54f-60b1-59e6-a3de-d596b5319933`

- Recorded outcome: **NO** · present date `2026-05-02 18:54:21.102290` (window ends end of UTC day `2026-05-02`) · expected resolution `2026-06-01 00:00:00`

**Question**

Will China announce new export controls on any critical mineral in response to US semiconductor export control actions between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between May 1, 2026 00:00 UTC and June 1, 2026 23:59 UTC, China officially announces **new** export controls on any critical mineral—defined as any mineral on the International Energy Agency's (IEA) Critical Minerals List (https://www.iea.org/reports/critical-minerals)—that meet ALL of the following criteria:

1. **New or expanded controls:** The announcement must impose new licensing requirements, quotas, or total bans on one or more critical minerals or products containing them, OR expand existing controls to cover additional minerals, lower thresholds, or add new restricted end-users/destinations. Reimposition of previously suspended controls (e.g., lifting the current suspension on gallium/germanium/antimony exports) also qualifies.

2. **Responsive to US actions:** The announcement must be explicitly linked to US semiconductor export control actions. This is satisfied if ANY of the following occurs:
   - An official statement from China's Ministry of Commerce (MOFCOM) or spokesperson references US semiconductor/chip export controls as a reason or context for the new controls;
   - Chinese state media (Xinhua, People's Daily, Global Times, or CCTV) reports the controls as a response or retaliation to US semiconductor export control actions;
   - The MOFCOM announcement itself cites national security concerns and is issued within 14 calendar days of a new US semiconductor export control action (e.g., new BIS rule, executive order, or legislative action such as the MATCH Act being signed into law).

3. **Official announcement:** The controls must be announced via an official MOFCOM notice published on http://www.mofcom.gov.cn/ or through an official Chinese government gazette.

This question resolves **No** if no such announcement meeting all three criteria is made by June 1, 2026 23:59 UTC.

**Resolution source:** Official announcements on MOFCOM's website (http://www.mofcom.gov.cn/), supplemented by credible international news reporting from Reuters (https://www.reuters.com/), Associated Press, or Bloomberg confirming the announcement and its stated rationale.

**Exact later resolution packet — this is the object under audit**

The question requires that, strictly between May 1, 2026 00:00 UTC and June 1, 2026 23:59 UTC, China officially announce NEW or expanded export controls on a critical mineral (on the IEA list) via an official MOFCOM notice (mofcom.gov.cn) or government gazette, explicitly linked to US semiconductor export control actions.

I examined the official MOFCOM 2026 announcements index (https://www.mofcom.gov.cn/zcfb/blgg/gg/2026/index.html). The only MOFCOM announcements published in the May 1–June 1, 2026 window were:
- 2026-05-02: Announcement No. 21 of 2026 — a blocking order against US sanctions on five Chinese enterprises related to Iranian oil (a sanctions blocking statute, NOT an export control on critical minerals) [a79ee9, af8530].
- 2026-05-22: A joint announcement by five departments adjusting the catalog of drug-precursor chemicals subject to export control to specific countries/regions (precursor chemicals, NOT IEA critical minerals or semiconductor materials) [a79ee9, af8530].

No announcement dated between May 23 and June 1, 2026 appears on the list [af8530].

Therefore, no MOFCOM announcement in the window imposed new/expanded export controls on any IEA critical mineral. Although the US tightened semiconductor controls in late May 2026 (e.g., the Commerce Department's May 31, 2026 step to halt Nvidia AI chip shipments to Chinese firms abroad, per Reuters https://www.reuters.com/world/china/us-takes-step-halt-nvidia-ai-chip-shipments-chinese-firms-outside-china-2026-05-31/), China did not respond with any new critical-mineral export control announcement during the window. China's existing rare-earth/critical-mineral export regime (from April and October 2025) remained largely unchanged following the 14–15 May 2026 Trump-Xi summit, per Benchmark Source reporting, and there was no new qualifying MOFCOM announcement.

Criterion 1 (new/expanded controls on a critical mineral) is not satisfied; thus criteria 2 and 3 are moot. The question resolves NO.

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-12. `c291b187-a2de-5dfc-af3b-6d61a5c703f8`

- Recorded outcome: **NO** · present date `2026-05-03 01:51:49.425831` (window ends end of UTC day `2026-05-03`) · expected resolution `2026-06-01 00:00:00`

**Question**

Will Arizona SB 1347 (requiring insurance coverage for iatrogenic infertility) be signed into law by June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if Arizona SB 1347 (57th Legislature, 2nd Regular Session — "health insurance; fertility preservation; coverage") becomes law on or after May 1, 2026, and on or before June 1, 2026 (11:59 PM US Mountain Standard Time). "Becomes law" means either: (a) the Governor of Arizona signs the bill into law, or (b) the bill becomes law without the Governor's signature pursuant to Arizona constitutional provisions (Article V, Section 7), or (c) a gubernatorial veto is overridden by the legislature.

The question resolves as **No** if the bill has not become law by June 1, 2026, including if it was vetoed (without override), failed in either chamber, or simply was not acted upon by the Governor by that date.

"Iatrogenic infertility" is defined per the bill text as "an impairment of fertility that is caused directly or indirectly by surgery, chemotherapy, radiation or other medical treatment" (https://www.azleg.gov/legtext/57leg/2R/bills/sb1347p.pdf). See also: https://en.wikipedia.org/wiki/Iatrogenesis.

**Resolution source:** The official Arizona State Legislature bill tracking page at https://apps.azleg.gov/BillStatus/BillOverview/84896, which displays the Governor's action on the bill. Secondary confirmation may come from the Governor's office at https://azgovernor.gov or credible reporting (e.g., Arizona Capitol Times, AP, Reuters).

**Exact later resolution packet — this is the object under audit**

The question resolves NO. Arizona SB 1347 (57th Legislature, 2nd Regular Session — "health insurance; fertility preservation; coverage") did not become law on or before June 1, 2026.

Evidence from the official Arizona State Legislature bill status page (https://apps.azleg.gov/BillStatus/BillOverview/84896): the bill passed the Senate on 03/02/2026 and was transmitted to the House, where it cleared the House Health & Human Services committee (03/16/2026) but then stalled — there is no record of it passing the House floor, being transmitted to the Governor, or receiving any gubernatorial action [https://apps.azleg.gov/BillStatus/BillOverview/84896](https://apps.azleg.gov/BillStatus/BillOverview/84896).

This is corroborated by BillTrack50 (https://www.billtrack50.com/billdetail/1946298), which lists the bill's status as "Dead," with its last recorded action on or around March 17, 2026 (a Senate floor amendment), and no record of House passage or a Governor's signature [AZ SB1347 | BillTrack50](https://www.billtrack50.com/billdetail/1946298).

Because the bill never reached the Governor, none of the three "becomes law" paths in the resolution criteria occurred: (a) no gubernatorial signature, (b) no becoming law without signature under Article V, Section 7, and (c) no veto override. The bill was simply not enacted before the June 1, 2026 deadline, which the resolution criteria explicitly state resolves the question NO.

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-13. `2366975e-e87b-5f7c-8483-d27184f9efe4`

- Recorded outcome: **NO** · present date `2026-05-02 17:06:01.810241` (window ends end of UTC day `2026-05-02`) · expected resolution `2026-06-01 00:00:00`

**Question**

Will the FAA amend its 2,708 daily operations cap for Chicago O'Hare (ORD) before the cap takes effect on June 2, 2026?

**Resolution criteria**

This question resolves **YES** if, between May 1, 2026, and June 1, 2026, at 23:59 UTC, the FAA publishes an official order, amendment, or notice that changes the daily operations cap at Chicago O'Hare (ORD) from the current 2,708 figure established in the April 16, 2026 order (Federal Register Document No. 2026-07665). A change to the cap number includes any increase or decrease in the 2,708 daily operations limit.

This question resolves **NO** if the 2,708 daily operations cap remains unchanged as of 23:59 UTC on June 1, 2026.

**Clarifications:**
- A change to the effective date alone (as already occurred with the shift from May 17 to June 2) does NOT count as amending the cap and would not trigger a YES resolution.
- Modifications to how operations are allocated among airlines, without changing the total 2,708 cap, do NOT count.
- The renewal or reissuance of the existing order at the same 2,708 cap level does NOT count as a "new" restriction.
- Only the total daily cap number matters for resolution purposes.

**Resolution source:** Official announcements on the [FAA Newsroom](https://www.faa.gov/newsroom) or publications in the [Federal Register](https://www.federalregister.gov/).

**Exact later resolution packet — this is the object under audit**

The question resolves NO. It asks whether, between May 1, 2026 and June 1, 2026 (23:59 UTC), the FAA published an official order, amendment, or notice changing the daily operations cap at Chicago O'Hare from the 2,708 figure established in the April 16, 2026 order (Federal Register Document No. 2026-07665).

Evidence:
- A direct search of the Federal Register limited to FAA documents mentioning "O'Hare" published between May 1 and June 1, 2026 returned "No documents were found" [ba4ad7]. This means no FAA order, amendment, or notice was published in that window — let alone one changing the cap number.
- The only amendment to the original order was Federal Register Document No. 2026-08163, published April 27, 2026, which solely changed the effective date from May 17 to June 2, 2026 (https://www.federalregister.gov/documents/2026/04/27/2026-08163/). Per the question's clarifications, an effective-date change does NOT trigger YES, and in any case it was published in April, outside the May 1–June 1 window.
- Numerous contemporaneous news reports from late April and May 2026 (e.g., CBS News Chicago, Chicago Business, NBC Chicago) consistently state the cap remained at 2,708 operations per day from June 2 through October 24, 2026, and that airlines (notably United) responded by cutting their schedules to fit under the 2,708 figure — confirming the cap number itself was unchanged.

Because the 2,708 daily operations cap remained unchanged as of 23:59 UTC on June 1, 2026, and no qualifying FAA order/amendment/notice was published in the resolution window, the question resolves NO.

The daily operations limit remained exactly 2,708 (neither increased nor decreased) as of the deadline.

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-14. `a0fb8e02-15ac-5a1d-aa1d-ada77a5268e4`

- Recorded outcome: **NO** · present date `2026-05-03 00:01:10.915583` (window ends end of UTC day `2026-05-03`) · expected resolution `2026-06-01 00:00:00`

**Question**

Will MOL Group finalize the acquisition of Gazprom's 56.15% stake in Serbia's NIS by June 1, 2026?

**Resolution criteria**

This question resolves YES if, by 23:59 UTC on June 1, 2026, there is credible public confirmation that the sale of Gazprom Neft's and JSC Intelligence's combined 56.15% stake in Naftna Industrija Srbije (NIS) to a non-Russian entity has been finalized.

"Finalized" means either: (a) a binding sale-purchase agreement (SPA) has been signed and publicly announced, with formal registration of share transfers initiated or completed; or (b) the formal transfer of shares to the buyer has been registered with the Serbian Central Securities Depository.

"Non-Russian entity" means an entity that is (i) not incorporated in the Russian Federation, (ii) not majority-owned (50%+) by Russian state entities or Russian nationals, and (iii) not designated on the U.S. OFAC Specially Designated Nationals (SDN) list.

The finalization must occur on or after May 1, 2026. Events prior to May 1, 2026 (such as the January 2026 Heads of Agreement) do not count.

Resolution sources: official announcements from MOL Group (https://molgroup.info/en/media-centre/press-releases), the Serbian Government (https://www.srbija.gov.rs/), or credible international news agencies such as Reuters (https://www.reuters.com/), Bloomberg, or AP.

If the sale has not been finalized by 23:59 UTC on June 1, 2026, the question resolves NO.

**Exact later resolution packet — this is the object under audit**

The question resolves NO because, by 23:59 UTC on June 1, 2026, there was no credible public confirmation that the sale of Gazprom Neft's and JSC Intelligence's combined 56.15% stake in NIS to a non-Russian entity had been finalized (defined as either a signed binding SPA with share-transfer registration initiated/completed, or a registered share transfer with the Serbian Central Securities Depository).

Key evidence:
- As of May 14, 2026, Serbia and MOL remained at odds over terms; the Serbian government rejected a MOL proposal on May 7, 2026, and remained dissatisfied with a revised proposal. Negotiations were ongoing, with a competing bid having emerged. No SPA had been signed and the sale had not been finalized [d8f8fb].
- A Reuters article of May 22, 2026 confirmed the deal was NOT finalized: OFAC granted MOL a two-week extension, setting a new deadline of June 6, 2026 to finalize negotiations with Gazprom Neft, and MOL's CEO noted "certain terms and conditions remain to be finalised" [f1f038].
- A European Western Balkans article of May 25, 2026 reiterated that negotiations were still ongoing, no binding SPA had been signed, and the new completion deadline was June 6, 2026 [96251c].

Since the OFAC negotiation deadline itself was pushed to June 6, 2026 — beyond the question's June 1, 2026 cutoff — and talks were explicitly still ongoing with no SPA signed and no share transfer registered as of late May 2026, the qualifying "finalized" event could not have occurred on or after May 1, 2026 and before 23:59 UTC June 1, 2026. The question therefore resolves NO.

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-15. `bc18b8dc-6ab4-5cc2-98a1-8c73306d10a3`

- Recorded outcome: **NO** · present date `2026-05-16 06:46:56.345876` (window ends end of UTC day `2026-05-16`) · expected resolution `2026-06-13T00:00:00`

**Question**

Will at least one living D-Day veteran be physically present at the official international ceremony at Langrune-sur-Mer on June 6, 2026?

**Resolution criteria**

This question resolves YES if at least one D-Day veteran is confirmed to have been physically present at the official international ceremony at Langrune-sur-Mer on June 6, 2026. It resolves NO otherwise.

**Key definitions:**

- **D-Day veteran**: A person who served in the Allied armed forces (of any nation) and participated in [Operation Overlord](https://en.wikipedia.org/wiki/Normandy_landings) on June 6, 1944, including the amphibious landings, airborne operations, or direct naval support operations on that date.

- **Physical presence**: The veteran must be bodily present at the ceremony site in Langrune-sur-Mer during the official international ceremony. Virtual attendance, video messages, or participation in other D-Day commemorative events elsewhere in Normandy do not count.

- **Official international ceremony**: The ceremony organized by the [Comité du Débarquement](https://www.comitedudebarquement.fr/en/) at Langrune-sur-Mer on June 6, 2026, scheduled for 4:30 PM CEST (UTC+2) [Why is the international ceremony being held in Langrune-sur-Mer?](https://www.comitedudebarquement.fr/en/ceremonie-internationale-82e-anniversaire-du-debarquement/).

**Resolution sources**: Credible reporting from major news agencies such as [AP](https://apnews.com/), [Reuters](https://www.reuters.com/), [BBC](https://www.bbc.com/news), [AFP](https://www.afp.com/), or major French outlets such as [Le Monde](https://www.lemonde.fr/) or [Ouest-France](https://www.ouest-france.fr/), confirming that at least one D-Day veteran attended the ceremony. The veteran's D-Day participation must be identified in reporting (by name and service record) rather than merely described as a "WWII veteran."

**Edge cases:**
- If the ceremony is cancelled or relocated to a different municipality, this question resolves NO.
- If a veteran's claimed D-Day participation is disputed in credible reporting, that veteran does not count for resolution purposes unless at least one credible source affirms their participation without contradiction from equally credible sources.
- If a D-Day veteran is present at Langrune-sur-Mer for other events on June 6 but not confirmed at the official international ceremony itself, this resolves NO.

**Exact later resolution packet — this is the object under audit**

RESOLUTION: NO (0)

**Step 1 — The antecedent/edge case is satisfied (the ceremony was NOT cancelled or relocated).**
The official international ceremony for the 82nd anniversary of D-Day was held at Langrune-sur-Mer on Saturday, June 6, 2026, presided over by French PM Sébastien Lecornu, with representatives of ~11 nations including UK Defence Secretary John Healey and US Under Secretary of Defense Elbridge Colby (who replaced Pete Hegseth). Confirmed by Ouest-France [à la cérémonie internationale de Langrune-sur-Mer, des hommages ...](https://www.ouest-france.fr/d-day/en-images-82-ans-du-debarquement-a-la-ceremonie-internationale-de-langrune-sur-mer-des-hommages-et-un-grand-absent-333d4d7a-61b4-11f1-8c24-b38534c94fba)[82 ans du Débarquement en Normandie : entre cérémonies et ...](https://www.ouest-france.fr/d-day/direct-82e-anniversaire-du-debarquement-en-normandie-ceremonies-commemorations-suivez-la-journee-du-6-juin-06c14f59-5870-4779-9a02-7648779ec75f)[VIDÉO. 82e D-Day : la cérémonie internationale, présidée par ...](https://www.ouest-france.fr/d-day/video-82e-d-day-la-ceremonie-internationale-presidee-par-sebastien-lecornu-sacheve-a-langrune-sur-mer-991fb665-33d3-4935-9f56-d72fb4be509f), Le Monde [https://www.lemonde.fr/en/france/article/2026/06/06/on-d-day-anniversary-hegseth-urges-europe-to-counter-present-day-invasion-of-beaches_6754207_7.html](https://www.lemonde.fr/en/france/article/2026/06/06/on-d-day-anniversary-hegseth-urges-europe-to-counter-present-day-invasion-of-beaches_6754207_7.html), France 3 [EN IMAGES. Retour sur les commémorations du 82e anniversaire ...](https://france3-regions.franceinfo.fr/normandie/en-images-retour-sur-les-commemorations-du-82e-anniversaire-du-d-day-en-normandie-3364039.html), and Reuters/AP photo galleries [World War II D-Day anniversary commemorated in France](https://www.staradvertiser.com/2026/06/06/photo-gallery/world-war-ii-d-day-anniversary-commemorated-in-france/)[82nd D-Day landings anniversary commemorated in France. See ...](https://www.usatoday.com/picture-gallery/news/world/2026/06/06/d-day-commemorated-in-france-see-pete-hegseth-wwii-veterans-more/90435504007/). Note: US Secretary of War Pete Hegseth pulled out of the Langrune ceremony (the "grand absent") and instead went to the Normandy American Cemetery at Colleville-sur-Mer plus a private visit [à la cérémonie internationale de Langrune-sur-Mer, des hommages ...](https://www.ouest-france.fr/d-day/en-images-82-ans-du-debarquement-a-la-ceremonie-internationale-de-langrune-sur-mer-des-hommages-et-un-grand-absent-333d4d7a-61b4-11f1-8c24-b38534c94fba)[https://www.lemonde.fr/en/france/article/2026/06/06/on-d-day-anniversary-hegseth-urges-europe-to-counter-present-day-invasion-of-beaches_6754207_7.html](https://www.lemonde.fr/en/france/article/2026/06/06/on-d-day-anniversary-hegseth-urges-europe-to-counter-present-day-invasion-of-beaches_6754207_7.html)[EN IMAGES. Entre cérémonie internationale et visite privée de Pete ...](https://www.ouest-france.fr/d-day/en-images-entre-ceremonie-internationale-et-visite-privee-de-pete-hegseth-retour-sur-un-6-juin-dense-pour-le-82e-d-day-58c96aa8-61b2-11f1-8a5e-13fc958a9977). So the "cancelled/relocated → NO" edge case does not apply on that ground; the ceremony happened at Langrune as planned.

**Step 2 — WWII veterans were physically present at Langrune, but only described generically.**
AP (via USA Today) and Reuters (via Honolulu Star-Advertiser) photo galleries carry captions reading "WWII veterans attend an International commemorative ceremony for the 82nd anniversary of the World War II 'D-Day' Normandy landings in Langrune-sur-Mer" — but NO individual veterans are named, and none is identified as a D-Day (June 6, 1944) participant with a service record [82nd D-Day landings anniversary commemorated in France. See ...](https://www.usatoday.com/picture-gallery/news/world/2026/06/06/d-day-commemorated-in-france-see-pete-hegseth-wwii-veterans-more/90435504007/)[World War II D-Day anniversary commemorated in France](https://www.staradvertiser.com/2026/06/06/photo-gallery/world-war-ii-d-day-anniversary-commemorated-in-france/).

**Step 3 — No credible source names a D-Day veteran (by name and service record) at the Langrune ceremony.**
I checked every relevant report from the specified credible sources (AP, Reuters, BBC, Le Monde, Ouest-France) plus Euronews, France 3, franceinfo, actu.fr and Tendance Ouest. None identifies a specific June-6-1944 participant as physically present at the official Langrune ceremony:
- Ouest-France's detailed coverage of the Langrune ceremony names only officials (Lecornu, Vautrin, Healey, Colby) and discusses Hegseth's absence — no veteran named at Langrune [à la cérémonie internationale de Langrune-sur-Mer, des hommages ...](https://www.ouest-france.fr/d-day/en-images-82-ans-du-debarquement-a-la-ceremonie-internationale-de-langrune-sur-mer-des-hommages-et-un-grand-absent-333d4d7a-61b4-11f1-8c24-b38534c94fba)[82 ans du Débarquement en Normandie : entre cérémonies et ...](https://www.ouest-france.fr/d-day/direct-82e-anniversaire-du-debarquement-en-normandie-ceremonies-commemorations-suivez-la-journee-du-6-juin-06c14f59-5870-4779-9a02-7648779ec75f)[VIDÉO. 82e D-Day : la cérémonie internationale, présidée par ...](https://www.ouest-france.fr/d-day/video-82e-d-day-la-ceremonie-internationale-presidee-par-sebastien-lecornu-sacheve-a-langrune-sur-mer-991fb665-33d3-4935-9f56-d72fb4be509f)[EN IMAGES. Entre cérémonie internationale et visite privée de Pete ...](https://www.ouest-france.fr/d-day/en-images-entre-ceremonie-internationale-et-visite-privee-de-pete-hegseth-retour-sur-un-6-juin-dense-pour-le-82e-d-day-58c96aa8-61b2-11f1-8a5e-13fc958a9977)[82 ans du Débarquement en Normandie : entre cérémonies et ...](https://www.ouest-france.fr/d-day/direct-82e-anniversaire-du-debarquement-en-normandie-ceremonies-commemorations-suivez-la-journee-du-6-juin-06c14f59-5870-4779-9a02-7648779ec75f).
- Le Monde: no veteran named at Langrune; states Hegseth skipped the "main international ceremony... later in the afternoon" [https://www.lemonde.fr/en/france/article/2026/06/06/on-d-day-anniversary-hegseth-urges-europe-to-counter-present-day-invasion-of-beaches_6754207_7.html](https://www.lemonde.fr/en/france/article/2026/06/06/on-d-day-anniversary-hegseth-urges-europe-to-counter-present-day-invasion-of-beaches_6754207_7.html).
- Euronews: mentions "six of the last veterans" but at the British Normandy Memorial, not Langrune [D-Day 82nd anniversary honoured in France - Euronews](https://www.euronews.com/my-europe/2026/06/06/d-day-82nd-anniversary-honoured-in-france).
- BBC: names D-Day veterans Kenneth (Ken) Hay (100) and Henry Rice — but at the British Normandy Memorial at Ver-sur-Mer, not Langrune [World War Two veterans arrive in France on anniversary of D-Day](https://www.bbc.com/news/articles/cvgm53nqvndo).
- France 3: names WWII veterans Harold Terence and Alan Shapiro — but at the Carentan parade / Colleville cemetery, not Langrune [EN IMAGES. Retour sur les commémorations du 82e anniversaire ...](https://france3-regions.franceinfo.fr/normandie/en-images-retour-sur-les-commemorations-du-82e-anniversaire-du-d-day-en-normandie-3364039.html).
- The famous Omaha Beach D-Day veteran Charles Norman Shay had died (honored posthumously) [Ouest-France snippet, uncited article].

**Step 4 — The veterans who could have been at Langrune are not confirmed there by name/service-record.**
The Best Defense Foundation brought 25 WWII veterans (welcomed at Deauville by Brigitte Macron) [25 vétérans accueillis à Deauville par Brigitte Macron - ICI](https://www.ici.fr/normandie/calvados-14/deauville/en-images-82e-anniversaire-du-debarquement-en-normandie-25-veterans-accueillis-a-deauville-par-brigitte-macron-2568221)[Calvados. 25 vétérans américains présents pour ... - Tendance Ouest](https://www.tendanceouest.com/actualite-437811-calvados-25-veterans-americains-presents-pour-les-commemorations-du-6-juin); its roster does include some genuine D-Day participants (e.g., Robert P. Gibson — Utah Beach June 6, 1944; Carl T. Felton — off Omaha Beach June 6, 1944), but its own June 6 schedule listed the Normandy American Cemetery (Colleville) ceremony and a Carentan parade, NOT Langrune [Battlefield Return: Normandy 2026 – 82nd Anniversary](https://bestdefensefoundation.org/battlefield-return/battlefield-return-normandy-2026-82nd-anniversary/). Pre-event Tendance Ouest said the group "would" attend Langrune, but this was a plan, was unnamed, and is not post-event confirmation [Calvados. 25 vétérans américains présents pour ... - Tendance Ouest](https://www.tendanceouest.com/actualite-437811-calvados-25-veterans-americains-presents-pour-les-commemorations-du-6-juin). franceinfo named veterans Jack Ray and Jack Wingate but did not place them at Langrune [D-Day : "J'étais ici il y a 80 ans", confie un vétéran ... - franceinfo](https://www.franceinfo.fr/societe/seconde-guerre-mondiale/d-day-j-etais-ici-il-y-a-80-ans-confie-un-veteran-accueilli-par-brigitte-macron-avant-le-82e-anniversaire-du-debarquement_8044439.html).

**Conclusion.** The resolution criteria explicitly require that "the veteran's D-Day participation must be identified in reporting (by name and service record) rather than merely described as a 'WWII veteran,'" and that presence be at the official Langrune ceremony specifically (not other Normandy events). Applying this literally: although unnamed "WWII veterans" were photographed at Langrune, no credible source names any D-Day (June 6, 1944) participant with a service record as present at the Langrune ceremony. Every named D-Day veteran is documented at other sites (Ver-sur-Mer, Carentan, Colleville). Therefore the YES condition is not met, and the question resolves NO.

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-16. `5b13d31d-7672-5d4e-838b-264df5817a7a`

- Recorded outcome: **NO** · present date `2026-05-01 15:16:37.639666` (window ends end of UTC day `2026-05-01`) · expected resolution `2026-06-01 00:00:00`

**Question**

Will the U.S. House of Representatives pass H.R.8170 (the MATCH Act) by June 1, 2026?

**Resolution criteria**

This question resolves YES if H.R.8170 (the MATCH Act) receives a simple majority vote on the floor of the U.S. House of Representatives on or after April 30, 2026, and on or before June 1, 2026, 11:59 PM UTC. Committee approval alone does not count as "passing the House."

This question resolves NO if the bill has not passed a House floor vote by June 1, 2026, 11:59 PM UTC.

The primary resolution source is the official Congress.gov bill tracker for H.R.8170: https://www.congress.gov/bill/119th-congress/house-bill/8170. The "Actions" tab will serve as the definitive record of whether the bill has passed the House. If Congress.gov is unavailable, credible reporting from Reuters, AP, or Bloomberg may be used as a secondary source.

**Exact later resolution packet — this is the object under audit**

The question asks whether the U.S. House of Representatives passed H.R.8170 (the MATCH Act, 119th Congress) on a full floor vote between April 30, 2026 and June 1, 2026, 11:59 PM UTC. The primary resolution source is the official Congress.gov bill tracker (https://www.congress.gov/bill/119th-congress/house-bill/8170).

Per the Congress.gov "All Info"/Actions record for H.R.8170, the most recent action on the bill was on April 22, 2026, when the House Committee on Foreign Affairs "Ordered to be Reported in the Nature of a Substitute (Amended) by the Yeas and Nays: 36 - 8." No subsequent action exists — there is NO record of a full House floor vote ("Passed/agreed to in House") [fe71a9]. The independent GovTrack.us tracker corroborates this, listing only two actions: "Introduced" (April 2, 2026) and "Ordered Reported" (April 22, 2026), with the bill's status remaining "Ordered Reported" as of June 2, 2026 [cc607a].

The committee action ("ordered to be reported") is explicitly distinguished from a full House floor vote in the resolution criteria, which state that "Committee approval alone does not count as 'passing the House.'" Since no floor vote occurred within (or even after) the April 30 – June 1, 2026 window, the consequent did not occur.

Therefore the question resolves NO (0).

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-17. `f0c57160-d1d9-552b-9d20-41ea4b4902d0`

- Recorded outcome: **NO** · present date `2026-05-03 04:40:15.754182` (window ends end of UTC day `2026-05-03`) · expected resolution `2026-06-01 00:00:00`

**Question**

Will Christian Horner hold an official role at any F1 team by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, at any point between May 1, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC), Christian Horner is confirmed to hold or have been announced for an official role at any F1 team officially entered in the 2026 FIA Formula One World Championship.

**Definitions:**
- **"Official role"** means any of the following positions, whether paid or unpaid: Team Principal, CEO, Managing Director, Chief Executive, Technical Director, Consultant, Advisor, or member of the board of directors. An ownership stake alone (without an accompanying operational or advisory role) does not qualify.
- **"F1 team"** means any of the constructors officially entered in the 2026 FIA Formula One World Championship, as listed on the [FIA entry list](https://www.fia.com/regulation/category/110) or [F1.com team profiles](https://www.formula1.com/en/teams).
- The role must be **active or formally announced** during the May 1–June 1, 2026 window. Horner's prior role at Red Bull Racing (which ended in 2025) does not count.

**Resolution sources:** Official press releases or team announcements from the relevant F1 team, or credible reporting from major sports news outlets such as [F1.com](https://www.formula1.com), [BBC Sport](https://www.bbc.com/sport/formula1), [ESPN F1](https://www.espn.com/f1/), [Autosport](https://www.autosport.com), Reuters, or AP.

If no such confirmation exists by 23:59 UTC on June 1, 2026, the question resolves **No**.

**Exact later resolution packet — this is the object under audit**

The question resolves NO. Between May 1 and June 1, 2026, Christian Horner was NOT confirmed or announced for any qualifying "official role" (Team Principal, CEO, Managing Director, Chief Executive, Technical Director, Consultant, Advisor, or board member) at any F1 team officially entered in the 2026 FIA Formula One World Championship.

Evidence found within the resolution window:

1. ESPN (May 21, 2026) reported Horner was still only "assessing his options for an F1 comeback," with discussions about a potential BYD partnership. The article states "BYD do not appear ready to launch a serious bid any time soon," and notes BYD is a Chinese electric manufacturer "exploring options for entering the sport in some capacity in the future" — i.e., NOT an F1 team entered in 2026. Horner's return "appears to be a way off" with "few other viable options" open to him [fa7ad7].

2. The only confirmed new job Horner took on (per Express, May 21, 2026) is as an adviser to investment company Oakley Capital — an investment firm, NOT an F1 team. This does not satisfy the criteria of an official role at an F1 team entered in 2026 [e7872b].

3. The Alpine situation remained an unresolved ownership-stake negotiation only. As of May 31, 2026, GPFans reported "there is no official confirmation that Horner is interested in the deal at all," and Renault held a veto over the share sale until September. No operational/advisory appointment was made [ea5e46]. Notably, the question explicitly states an ownership stake alone (without an accompanying operational/advisory role) does not qualify.

4. An earlier ESPN piece (March 13, 2026) likewise confirmed Horner was only part of a consortium pursuing a 24% Alpine stake — a negotiation over ownership, not an appointment to any operational/advisory role [ebb14a].

The Audi Team Principal links (from April 2026) were purely speculation/tips by pundits, never an actual appointment, and the only "Exclusive" claiming his Audi appointment was an April 1 piece (April Fools' / unreliable, not an allowed source).

His prior Red Bull Racing role (ended 2025) is explicitly excluded by the resolution criteria.

Since no qualifying official role at a 2026-entered F1 team was active or formally announced during the May 1–June 1, 2026 window, the question resolves NO.

Key sources:
- ESPN (BYD): https://www.espn.com/f1/story/_/id/48826861/christian-horner-targets-formula-1-return-byd-10-months-red-bull-sacking-sources
- Express (Oakley Capital): https://www.express.co.uk/sport/f1-autosport/2208297/christian-horner-new-job-f1
- GPFans (Alpine, May 31): https://www.gpfans.com/en/f1-news/1084825/christian-horner-alpine-price-path-to-f1-return/
- ESPN (Alpine/Mercedes): https://www.espn.com/f1/story/_/id/48193300/christian-horner-route-back-f1-alpine-faces-mercedes-obstacle

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-18. `b37ed4ff-8c07-5ba3-a337-fb226eda2710`

- Recorded outcome: **NO** · present date `2026-05-03 01:06:24.467305` (window ends end of UTC day `2026-05-03`) · expected resolution `2026-06-01 00:00:00`

**Question**

Will the Caspian Pipeline Consortium (CPC) experience an unscheduled shutdown of 48+ hours due to a security incident between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if all of the following conditions are met:

1. **Unscheduled shutdown**: The CPC pipeline system or its marine terminal at Novorossiysk experiences a cessation or substantial reduction (below 25% of normal throughput) of oil export operations that was not pre-announced as planned maintenance. This includes both pipeline throughput stoppages and terminal loading halts.

2. **Duration of 48+ hours**: The shutdown lasts at least 48 consecutive hours, measured from the time the stoppage or substantial reduction is first reported by a credible source (Reuters, Bloomberg, AP, or official CPC statements) to the time resumption of operations is officially announced or confirmed by a credible source. All times are measured in UTC.

3. **Security incident**: The shutdown is primarily caused by a security incident, defined as a deliberate hostile act including but not limited to: drone strikes, missile attacks, naval drone attacks, sabotage, or armed assault on CPC infrastructure. This excludes technical failures, weather-related disruptions (e.g., storms), scheduled maintenance, regulatory actions, or sanctions-related stoppages.

4. **Timing**: The shutdown must commence (or be ongoing) at any point between May 1, 2026, 00:00 UTC and June 1, 2026, 23:59 UTC.

**Resolution source**: Official CPC consortium statements (https://www.cpc.ru/EN/press/Pages/default.aspx) or major international news wires such as Reuters (https://www.reuters.com/business/energy/), Bloomberg, or Associated Press. At least one credible source must attribute the shutdown to a security incident.

If no qualifying shutdown occurs during this period, the question resolves **No**.

**Exact later resolution packet — this is the object under audit**

The question resolves NO. It requires a CPC (Caspian Pipeline Consortium) pipeline/marine-terminal unscheduled shutdown of 48+ consecutive hours (throughput below 25% of normal) caused primarily by a security incident, commencing or ongoing between May 1, 2026 00:00 UTC and June 1, 2026 23:59 UTC.

Findings:
- The principal security event during the window was a large Ukrainian drone strike on Novorossiysk over the weekend of May 22-24, 2026. However, that attack hit the Sheskharis oil terminal (a Transneft facility), not the CPC terminal. The Reuters report (May 22, updated May 23) said falling drone debris triggered a fire at "an oil terminal" and did not identify the CPC terminal or report any CPC export suspension [bf3eba, abfbd0]. The AP/Fortune account (May 23) likewise identifies the Sheskharis/Transneft terminal as the target and reports no CPC shutdown [fdd7f3].
- Bloomberg (May 26, 2026) reported that following the weekend attack, all three crude berths of the Sheskharis terminal were operational with tankers loading per satellite imagery — i.e., no 48-hour cessation, and no CPC shutdown [08928a].
- Quantum Commodity Intelligence (May 26, 2026) reported CPC shipped 25.95 million mt of crude from its Black Sea terminal from Jan 1 to May 24, 2026, with ongoing loadings and no reported 48+ hour security-caused CPC shutdown in May 2026 [49a62f, 112f18].
- Earlier 2026 CPC/Novorossiysk disruptions (the Nov 29, 2025 SPM attack, the April 6-10, 2026 Sheskharis attack, the planned 72-hour maintenance ending April 10) all fall outside the May 1 - June 1, 2026 window [004baf, 56bd00, bae844].

No credible allowed source (CPC statements, Reuters, Bloomberg, AP) reported a 48+ hour CPC shutdown attributable to a security incident within the resolution window. Therefore the question resolves NO.

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-19. `17e0010e-2915-5ccc-8f2e-370b5620a78f`

- Recorded outcome: **NO** · present date `2026-05-02 16:08:13.374285` (window ends end of UTC day `2026-05-02`) · expected resolution `2026-06-01 00:00:00`

**Question**

Will a federal court issue an injunction blocking the $100,000 H-1B presidential proclamation fee between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 1, 2026, and before 11:59 PM Eastern Time on June 1, 2026, any U.S. federal court—including U.S. District Courts, U.S. Courts of Appeals (Circuit Courts), or the U.S. Supreme Court—issues an order that blocks, stays, enjoins, or otherwise prevents the enforcement of the $100,000 H-1B fee established by Presidential Proclamation 10973. This includes preliminary injunctions, permanent injunctions, temporary restraining orders (TROs), or stays pending appeal, regardless of whether the order applies nationwide or only to specific plaintiffs or jurisdictions.

This question resolves **No** if no such order is issued by any federal court within the specified timeframe.

A ruling that merely expresses disapproval of the fee or remands the case without an accompanying injunction or stay does not count. The order must have the practical effect of halting fee collection for at least some parties.

**Resolution source:** Official court dockets accessible via PACER (https://pacer.uscourts.gov/) or credible legal news reporting from outlets such as Reuters (https://www.reuters.com/legal/), Bloomberg Law (https://news.bloomberglaw.com/), Law360 (https://www.law360.com/), or Lawfare (https://www.lawfaremedia.org/).

**Exact later resolution packet — this is the object under audit**

The question resolves NO because no U.S. federal court issued any order blocking, staying, enjoining, or otherwise preventing enforcement of the $100,000 H-1B fee (Presidential Proclamation 10973) between May 1, 2026 and 11:59 PM ET June 1, 2026. I verified the status of all three named lawsuits:

1. **Chamber of Commerce v. DHS (D.C. Circuit, No. 25-5473):** The official PACER/CourtListener docket shows only procedural activity during the window — a May 6, 2026 response to a Rule 28(j) letter and a May 15, 2026 notice of attorney withdrawal. No decision, opinion, stay, or injunction was issued in May 2026 [Chamber of Commerce of the United States of Ameri v. DHS, 25-5473](https://www.courtlistener.com/docket/72095497/chamber-of-commerce-of-the-united-states-of-ameri-v-dhs/). (The underlying district court had previously upheld the fee on Dec. 23, 2025 and denied an injunction.)

2. **Global Nurse Force v. Trump (N.D. Cal., No. 4:25-cv-08454):** The docket shows no entries at all in May 2026; the last filing was a transcript order dated April 22, 2026. No injunction, stay, or order blocking the fee was issued during the window [Global Nurse Force v. Trump, 4:25-cv-08454 – CourtListener.com](https://www.courtlistener.com/docket/71541425/global-nurse-force-v-trump/).

3. **Multistate Attorneys General lawsuit (D. Mass., before Judge Leo Sorokin):** Reuters reported on May 29, 2026 that Judge Sorokin held a hearing at which he merely questioned the government's lawyer about the scope of the President's authority. This was oral argument only — no injunction, stay, or TRO was issued [US judge questions scope of Trump's power to impose ... - Reuters](https://www.reuters.com/legal/government/us-judge-questions-scope-trumps-power-impose-100000-h-1b-visa-fee-2026-05-29/). Law360 and Bloomberg Tax similarly reported only that the government was "pressed" on its authority at the hearing, not that any order issued.

Because the resolution criteria require an actual order with the practical effect of halting fee collection for at least some parties — and a mere ruling/hearing expressing disapproval or questioning the fee does not count — and because no such order issued in any of the three cases (or any other federal court) during May 1–June 1, 2026, the question resolves NO.

Sources:
- Chamber D.C. Circuit docket: https://www.courtlistener.com/docket/72095497/chamber-of-commerce-of-the-united-states-of-ameri-v-dhs/
- Global Nurse Force docket: https://www.courtlistener.com/docket/71541425/global-nurse-force-v-trump/
- Reuters (May 29, 2026): https://www.reuters.com/legal/government/us-judge-questions-scope-trumps-power-impose-100000-h-1b-visa-fee-2026-05-29/

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-20. `83077271-dd90-5017-8107-0d3fba6b8872`

- Recorded outcome: **NO** · present date `2026-05-02 22:34:40.635063` (window ends end of UTC day `2026-05-02`) · expected resolution `2026-06-01 00:00:00`

**Question**

Will the Federal Reserve issue a proposed rule implementing the GENIUS Act by June 1, 2026?

**Resolution criteria**

This question resolves YES if the Board of Governors of the Federal Reserve System publishes a proposed rule—defined as a Notice of Proposed Rulemaking (NPRM) or equivalent document containing draft regulatory text and an invitation for public comment (see the Federal Reserve's own definition at https://www.federalreserve.gov/aboutthefed/board-vote-category-definitions.htm [Board Vote Category Definitions - Federal Reserve](https://www.federalreserve.gov/aboutthefed/board-vote-category-definitions.htm))—specifically implementing provisions of the GENIUS Act of 2025, on or after May 1, 2026 (00:00 UTC) and by June 1, 2026 (23:59 UTC).

This question resolves NO if no such proposed rule has been published by 23:59 UTC on June 1, 2026.

Resolution will be determined by checking:
1. The Federal Reserve's press releases page: https://www.federalreserve.gov/newsevents/pressreleases.htm
2. The Federal Register's Federal Reserve section: https://www.federalregister.gov/agencies/federal-reserve-system

A proposed rule announced by the Federal Reserve Board but not yet published in the Federal Register by 23:59 UTC on June 1, 2026 still counts, provided the Board has voted to approve it and issued an official press release.

**Exact later resolution packet — this is the object under audit**

The question resolves NO because the Federal Reserve Board did not publish (or vote to approve) a Notice of Proposed Rulemaking implementing the GENIUS Act of 2025 between May 1, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC).

Evidence from the two resolution sources specified in the question:

1. Federal Reserve press releases page (https://www.federalreserve.gov/newsevents/pressreleases.htm): A review of all press releases issued during May 1 – June 1, 2026 shows none constitutes an NPRM implementing the GENIUS Act or regulating payment stablecoins. The releases covered enforcement actions, leadership changes (Kevin Warsh taking office as chairman May 22, Powell as chair pro tempore, Miran resignation), discount rate/FOMC minutes, surveys, and a May 20, 2026 request for comment on a "payment account" proposal — but that payment-account proposal does not mention the GENIUS Act or stablecoins [42499f].

2. Federal Register, Federal Reserve System section (https://www.federalregister.gov/agencies/federal-reserve-system): The Fed did publish several proposed rules on May 26, 2026 — Regulation D (Reserve Requirements), Regulation A (Extensions of Credit), and revisions to the Payment System Risk policy — all concerning new "special-purpose payment accounts." However, none of these documents implement the GENIUS Act of 2025 or regulate payment stablecoins [573ce6].

By contrast, the other two primary regulators had already issued their GENIUS Act NPRMs earlier (OCC in late February 2026, FDIC in April 2026), but the Federal Reserve had not done so by the June 1, 2026 deadline. The statutory deadline for implementing regulations was July 18, 2026, leaving the Fed room to act after the question's window closed.

Since no qualifying proposed rule was published or approved by the Fed within the May 1 – June 1, 2026 window, the question resolves NO (0).

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-21. `0e804a1b-4785-5fce-8f74-048fe941ac52`

- Recorded outcome: **NO** · present date `2026-05-12 15:01:12.273900` (window ends end of UTC day `2026-05-12`) · expected resolution `2026-07-01T00:00:00`

**Question**

Will at least one defendant in the Toti vote-trading case ("filone bis") formally conclude a patteggiamento (plea bargain) accepted by the court by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if at least one defendant in the "filone bis" (vote-trading branch) of the Toti investigation formally concludes a patteggiamento (plea bargain under Art. 444 of the Italian Code of Criminal Procedure, https://www.brocardi.it/codice-di-procedura-penale/libro-sesto/titolo-ii/art444.html) that is formally accepted by the court (i.e., a sentence is issued by the GUP or presiding judge ratifying the plea agreement) on or after May 10, 2026, and on or before July 1, 2026 (23:59 UTC).

A "formal conclusion" means a sentence (sentenza) issued by the GUP or judge formally accepting and ratifying the patteggiamento agreement between prosecution and defense, as reported by credible Italian news sources.

This question resolves **No** if no such plea bargain is formally accepted by the court for any defendant in this case branch by July 1, 2026, 23:59 UTC — whether because negotiations fail, the case proceeds to trial (dibattimento), or for any other reason.

**Resolution source:** Credible Italian news reporting from outlets such as [ANSA](https://www.ansa.it/), [Genova24](https://www.genova24.it/), [La Voce di Genova](https://www.lavocedigenova.it/), [GenovaToday](https://www.genovatoday.it/), or [Il Secolo XIX](https://www.ilsecoloxix.it/), confirming formal court acceptance of a patteggiamento for at least one defendant in the vote-trading branch of the investigation.

**Exact later resolution packet — this is the object under audit**

RESOLUTION: NO (0).

The question asks whether at least one defendant in the Toti "filone bis" (vote-trading / voto di scambio branch) formally concluded a patteggiamento (plea bargain under Art. 444 CPP) that was ratified by the court (via a sentenza) on or after May 10, 2026 and on or before July 1, 2026.

KEY EVENT: The decisive preliminary hearing before GUP Giorgio Morando (which the description noted had been postponed to June 5, 2026 to allow evaluation of alternative solutions including patteggiamento) took place on June 5, 2026. Five independent, high-quality Italian sources report the same outcome, and NONE report any patteggiamento being accepted by the court:

1. On June 5, 2026, the GUP ordered rinvio a giudizio (indictment/sending to trial) for 12 defendants — including Matteo Cozzani (Toti's former chief of staff), the Testa twins, and Venanzio Maurici — with the mafia aggravation (aggravante mafiosa) maintained. The trial (dibattimento) is set to begin September 16, 2026 [1cde3f, 6434d6, c6c8da, 06eb8c, 0a74e8].

2. DISTINGUISHING PATTEGGIAMENTO FROM OTHER OUTCOMES: Six defendants (Umberto Lo Grasso, Santo Inturri, Ivana Catarinolo, Giovanni Di Carlo, Biagio Zambitto, Giovanni Ferroni) requested MESSA ALLA PROVA (probation/community service), NOT patteggiamento. The court did not conclude/accept this either — the decision was postponed to November 2026, pending presentation of a plan to the UEPE [6434d6, c6c8da, 1cde3f, 0a74e8]. Messa alla prova is a distinct procedure from a patteggiamento (Art. 444 CPP plea bargain) and, in any case, was not ratified within the window. No defendant obtained a rito abbreviato either [c6c8da].

3. Paolo Piacenza's position was "stralciata" (severed), with the acts returned to the prosecutor for direct citation to trial (citazione diretta) — again, not a patteggiamento [6434d6, c6c8da, 06eb8c].

4. Crucially, negotiations for a plea agreement FAILED: GenovaToday reports "Non c'è stato accordo tra procura e difesa" (there was no agreement between prosecution and defense), confirming no patteggiamento accord was reached in this branch [06eb8c].

CONFIRMATION THIS IS THE "FILONE BIS" (not the primary Toti case): This is the second branch (secondo filone) concerning alleged vote-trading at the 2020 Liguria regional elections, involving ~18 defendants including Cozzani, Maurici, and the Testa twins — exactly the defendants named in the question. The primary corruption case (Toti, Spinelli, Signorini) had already concluded via patteggiamento back in December 2024, which is a separate proceeding and outside this question's scope [6434d6].

Therefore, no patteggiamento was formally accepted/ratified by the court for any "filone bis" defendant between May 10 and July 1, 2026. The case instead proceeded toward trial. The question resolves NO.

SOURCES (URLs):
- Il Fatto Quotidiano (June 5, 2026): https://www.ilfattoquotidiano.it/2026/06/05/voto-scambio-mafia-regione-liguria-cozzani-toti/8410323/ [1cde3f]
- ANSA (June 5, 2026): https://www.ansa.it/sito/notizie/cronaca/2026/06/05/voto-di-scambio-a-genova-a-processo-matteo-cozzani-e-altri-11_b289d9ca-4584-4b5a-96de-b0fc7ad66783.html [0a74e8]
- Genova24 (June 5, 2026): https://www.genova24.it/2026/06/inchiesta-voto-di-scambio-liguria-rinviato-a-giudizio-matteo-cozzani-e-altri-11-465720/ [c6c8da]
- GenovaToday (June 5, 2026): https://www.genovatoday.it/cronaca/toti-bis-cozzani-processo-aggravante-mafiosa.html [06eb8c]
- Antimafia Duemila (June 9, 2026): https://antimafiaduemila.com/home/mafie-news/giustizia/toti-bis-cozzani-a-processo-con-laggravante-mafiosa [6434d6]

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-22. `ee5e37c7-f82f-5d49-95b2-86ad466c9d50`

- Recorded outcome: **NO** · present date `2026-05-03 12:56:37.381726` (window ends end of UTC day `2026-05-03`) · expected resolution `2026-06-01 00:00:00`

**Question**

Will Google announce or release a Veo 4 video generation model by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 2, 2026, and by 23:59 UTC on June 1, 2026, Google officially announces or releases a video generation model explicitly named "Veo 4" (including minor variants such as "Veo 4.0", "Veo 4 Ultra", or "Veo 4 Pro").

**Definitions:**

- **"Veo 4"**: A model explicitly branded by Google using the name "Veo 4" (or "Veo 4.x" where x is any sub-version number, e.g., 4.0, 4.1). Incremental updates to existing versions (e.g., "Veo 3.2" or "Veo 3.1 Ultra") do NOT count. A rebranded successor under a completely different name (e.g., "Google Video AI" or "Imagen Video 2") also does NOT count — the model must use the "Veo 4" name.

- **"Announcement or release"**: Any of the following count as a qualifying announcement or release:
  1. An official blog post on the Google DeepMind blog (https://deepmind.google/discover/blog/) or Google's official blog (https://blog.google/) describing the model as "Veo 4."
  2. A mention by name during an official Google keynote (e.g., Google I/O), as confirmed by the official livestream or Google's event page (https://io.google/).
  3. Public availability of the model via Google AI Studio, Vertex AI, or a consumer product (e.g., integrated into Gemini or Flow), accompanied by official documentation using the "Veo 4" name.

  A leaked benchmark appearance, rumor, or third-party report without official Google confirmation does NOT count. Closed/invite-only testing also does NOT count unless accompanied by an official public announcement meeting one of the criteria above.

**Resolution source**: The Google DeepMind models page (https://deepmind.google/models/veo/), the Google DeepMind blog (https://deepmind.google/discover/blog/), or the official Google Blog (https://blog.google/). If the announcement occurs during a keynote, the official Google I/O page (https://io.google/) or official YouTube livestream recording serves as the resolution source.

If no qualifying announcement or release occurs by 23:59 UTC on June 1, 2026, this question resolves **No**.

**Exact later resolution packet — this is the object under audit**

The question resolves NO. The resolution requires Google to officially announce or release a model explicitly named "Veo 4" (or "Veo 4.x") on or after May 2, 2026 and by 23:59 UTC on June 1, 2026, via one of the specified official sources (Google DeepMind blog, Google's official blog, or an official Google I/O keynote).

Evidence from the specified official sources:

1) The official Google DeepMind Veo models page (https://deepmind.google/models/veo/) still identifies the current model as "Veo 3.1" with no mention of any "Veo 4" model [Veo 3.1 - Google DeepMind](https://deepmind.google/models/veo/).

2) The official Google Blog transcript of Sundar Pichai's Google I/O 2026 keynote (held May 19, 2026; https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) contains no mention of "Veo 4." The video-generation/media announcements at I/O 2026 centered on the Gemini family — specifically "Gemini Omni" and "Gemini Omni Flash" — not a "Veo 4." The word "Veo" appears only in reference to the existing Veo model [I/O 2026: Welcome to the agentic Gemini era - Google Blog](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/).

Since Google I/O 2026 (May 19-20, 2026) was the most likely venue and it did not feature a Veo 4 announcement, and no official Google blog post or product documentation using the "Veo 4" name exists through June 1, 2026, the antecedent (an official Veo 4 announcement/release) did not occur.

Third-party sources (e.g., YouTube/Instagram clickbait titles like "GEMINI 4 + VEO 4," and a "The Elites" Instagram post) circulated claiming a Veo 4, but these are not official Google sources and are explicitly excluded by the resolution criteria. Independent coverage (PixVerse, WaveSpeed) confirms that as of late May 2026 there was no official Google announcement, product page, or documentation for a "Veo 4" model.

Therefore the question resolves NO.

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-23. `467952fd-881f-5403-ad3f-a9d6c89e07ee`

- Recorded outcome: **NO** · present date `2026-05-14 08:55:14.960614` (window ends end of UTC day `2026-05-14`) · expected resolution `2026-07-01T00:00:00`

**Question**

Will the Wisconsin Supreme Court rule that Notice of Voting Eligibility forms are public records subject to disclosure in Wisconsin Voter Alliance v. Secord?

**Resolution criteria**

This question resolves **Yes** if the Wisconsin Supreme Court, in a written opinion or order issued on or after May 12, 2026 and on or before July 1, 2026 (11:59 PM CT / 04:59 AM UTC July 2), rules that Notice of Voting Eligibility (NVE) forms are public records subject to disclosure under Wisconsin law in *Wisconsin Voter Alliance v. Secord* (Case No. 2023-AP-36). A ruling that allows disclosure only with redactions of personally identifying information still counts as **Yes**, since it affirms the records' status as public records subject to disclosure.

This question resolves **No** if:
1. The Court rules that NVE forms are not public records subject to disclosure; or
2. The Court dismisses the case, declines to reach the merits, or resolves it on procedural grounds without classifying the records as public records; or
3. No ruling is issued by 11:59 PM CT on July 1, 2026 (04:59 AM UTC July 2, 2026).

**Resolution source:** The official opinion published on the Wisconsin Court System's Supreme Court opinions page (https://www.wicourts.gov/supreme/scopin.htm) or the case docket accessible via the Wisconsin Circuit Court Access system (https://wcca.wicourts.gov/).

**Exact later resolution packet — this is the object under audit**

The question resolves NO (0) because the Wisconsin Supreme Court did NOT issue any ruling in Wisconsin Voter Alliance v. Secord (Case No. 2023AP36 / 2023-AP-36) during the resolution window of May 12, 2026 through July 1, 2026 (11:59 PM CT). This triggers resolution criterion #3: "No ruling is issued by 11:59 PM CT on July 1, 2026."

Key evidence (all from the specified/authoritative sources):

1. OFFICIAL COURT SOURCE — The Wisconsin Supreme Court's official "Table of Pending Cases" (https://www.wicourts.gov/sc/SCCASES.pdf), dated June 10, 2026, lists case 2023AP36 (Wisconsin Voter Alliance v. Kristina Secord) as still PENDING: accepted by the court on 01/07/2026 with oral arguments held 04/21/2026, and NO decision date or mandate recorded. The highest opinion citation issued by that date was only 2026 WI 19 [7c0d32]. This is the closest authoritative snapshot to the deadline and shows no decision had issued.

2. Votebeat's Wisconsin news page, checked as of July 1, 2026, contains NO article reporting any Supreme Court decision in the case; the most recent relevant coverage was the April 20, 2026 oral-argument preview [192202]. The Votebeat case article itself, last updated June 1, 2026, stated the court was still deliberating after the April 21, 2026 arguments [4439be].

3. Law Forward's case tracker (a party in the case, tracking it closely) shows no events past the April 21, 2026 oral arguments [eb7c23]; State Court Report's case tracker lists status as "Pending" [2cc158]; and the Wisconsin Justice Initiative's June 2026 blog archive contains no post announcing a Secord decision [5df84f].

4. Context: The only prior Wisconsin Supreme Court action, on January 17, 2025 (2025 WI 2), was a procedural disposition that vacated the District II Court of Appeals ruling and remanded on procedural grounds (appellate-conflict rules) WITHOUT reaching the merits of whether NVE forms are public records [cbedcc]. That decision (a) predates the window and (b) would not have counted as YES anyway.

No source — official or news — indicates any opinion or order classifying NVE forms as public records was issued between May 12 and July 1, 2026. Therefore the antecedent for a YES (a merits ruling that NVE forms are public records subject to disclosure, even with redactions) never occurred, and criterion #3 (no ruling by the deadline) controls, resolving the question NO.

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-24. `6c9e6111-3b05-5c07-ab7c-4ef8b079d788`

- Recorded outcome: **NO** · present date `2026-05-15 10:18:37.598668` (window ends end of UTC day `2026-05-15`) · expected resolution `2026-07-01T00:00:00`

**Question**

Will a proprietary OpenAI model (e.g., GPT-4o, GPT-5) be available on Google Cloud Vertex AI by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 and by 23:59 UTC on July 1, 2026, at least one proprietary (non-open-weight) OpenAI model is listed as available to Google Cloud customers on Google Cloud Vertex AI. A "proprietary OpenAI model" is any model developed by OpenAI that is not labeled "oss," "open-weight," or released under an open-source license — examples include GPT-4o, GPT-5, GPT-5.4, GPT-5.5, o1, o3, or any successor. Availability in any access tier counts, including limited preview, public preview, or general availability.

"Available on Google Cloud Vertex AI" means the model is listed on the official Google Cloud Vertex AI documentation for OpenAI models (https://docs.cloud.google.com/vertex-ai/generative-ai/docs/maas/openai) or announced as available on the Google Cloud Blog (https://cloud.google.com/blog) or OpenAI's newsroom (https://openai.com/news/). Availability on Google Cloud Marketplace alone does not count; the model must be accessible through Vertex AI's Model-as-a-Service or equivalent managed API offering.

If no proprietary OpenAI model meets these criteria by the deadline, the question resolves **No**.

**Exact later resolution packet — this is the object under audit**

The question resolves **NO**. It asks whether at least one proprietary (non-open-weight) OpenAI model was listed as available to Google Cloud customers on Vertex AI (via Model-as-a-Service / managed API), verifiable through the official Vertex AI documentation, the Google Cloud Blog, or the OpenAI newsroom, between May 12, 2026 and 23:59 UTC on July 1, 2026.

Evidence from the specified resolution sources:

1. Official Vertex AI OpenAI-models documentation page. Note that Vertex AI was rebranded to the "Gemini Enterprise Agent Platform" at Google Cloud Next '26, and the documentation URL cited in the question (docs.cloud.google.com/vertex-ai/generative-ai/docs/maas/openai) now resolves to docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/openai. As of the deadline (page last updated June 30, 2026), this page lists ONLY two OpenAI models available as managed APIs: gpt-oss-120b-maas and gpt-oss-20b-maas, both described as open-weight models released under the Apache 2.0 license. No proprietary OpenAI models (GPT-4o, GPT-5, GPT-5.4, GPT-5.5, o1, o3, or any successor) are listed [053fa3].

2. Official Vertex AI release notes (docs.cloud.google.com/vertex-ai/docs/release-notes). A review covering May 12, 2026 through June 30, 2026 shows no announcement of any proprietary OpenAI model being added. The only OpenAI models referenced remain the open-weight gpt-oss models (originally added August 13, 2025) [8acc22].

3. Contemporary reporting confirms OpenAI launched its proprietary frontier models (GPT-5.4, GPT-5.5) on AWS Bedrock on April 28, 2026 — not on Google Cloud. The Forbes article (May 6, 2026) discusses OpenAI proprietary models on AWS Bedrock and the end of Microsoft exclusivity, and provides no confirmation of any proprietary OpenAI model being available on Google Cloud Vertex AI [82d43c].

No Google Cloud Blog post or OpenAI newsroom announcement was found announcing a proprietary OpenAI model on Vertex AI within the resolution window; searches surfaced only the open-weight gpt-oss availability and general rebranding/partnership news.

Since only open-weight GPT-OSS models — explicitly excluded by the resolution criteria — were available on Vertex AI / Gemini Enterprise Agent Platform through the July 1, 2026 deadline, and no proprietary OpenAI model met the criteria, the question resolves **NO (0)**.

Key URLs:
- https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/openai (formerly the cited Vertex AI MaaS OpenAI docs URL) — lists only gpt-oss-120b-maas and gpt-oss-20b-maas.
- https://docs.cloud.google.com/vertex-ai/docs/release-notes — no proprietary OpenAI model additions in the window.
- https://www.forbes.com/sites/jonmarkman/2026/05/06/openai-brings-gpt-55-to-aws-bedrock-as-microsoft-exclusive-era-ends/ — OpenAI proprietary models on AWS Bedrock, not Google Cloud.

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-25. `49907cf8-ca9f-505f-9a20-e0471c9b2493`

- Recorded outcome: **NO** · present date `2026-05-02 19:00:54.078555` (window ends end of UTC day `2026-05-02`) · expected resolution `2026-06-01 00:00:00`

**Question**

Will a proposed constitutional amendment restricting the office of pastor to men be formally included in the 2026 SBC Annual Meeting Order of Business by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, by June 1, 2026 (23:59 UTC), the SBC Committee on Order of Business or another official SBC body (e.g., Baptist Press at https://www.baptistpress.com/ or SBC.net at https://www.sbc.net/) publishes an official agenda, Order of Business, Book of Reports, or other formal notice confirming that a proposed constitutional amendment restricting the office of pastor or elder to men will be considered at the 2026 SBC Annual Meeting (June 9–10, 2026, Orlando, FL).

A "constitutional amendment" means a proposed change to the [SBC Constitution](https://www.sbc.net/about/what-we-believe/the-constitution-of-the-southern-baptist-convention/), not a bylaw change or a non-binding resolution.

The question resolves **No** if no such official publication confirms the inclusion of such a constitutional amendment on the Order of Business by June 1, 2026 (23:59 UTC). It also resolves **No** if only bylaw amendments (not constitutional amendments) regarding women pastors are scheduled.

Only official SBC publications released on or after May 1, 2026 count toward resolution. Earlier preliminary schedules that do not specifically list constitutional amendment items do not count unless they explicitly include such an amendment.

Resolution source: Official SBC publications, specifically the Book of Reports or Order of Business at https://www.sbc.net/resources/ or reporting by Baptist Press at https://www.baptistpress.com/resource-library/topic-index/sbc-annual-meetings/.

**Exact later resolution packet — this is the object under audit**

The question resolves NO because, by the June 1, 2026 (23:59 UTC) deadline, no official SBC publication confirmed that a proposed constitutional amendment restricting the office of pastor/elder to men was formally included in the 2026 SBC Annual Meeting Order of Business.

Key evidence:

1. The official "2026 SBC Annual Meeting schedule released" article from Baptist Press lists the Order of Business / program, and it does NOT include any constitutional amendment restricting the office of pastor or elder to men. The latest SBC news entries on that page (through June 1, 2026) likewise show no such amendment being added to the agenda [e3daa6].

2. The only relevant development is Albert Mohler's announcement (published May 18, 2026 on Baptist Press and his personal blog) that he INTENDS to propose a "Truth & Unity" amendment to Article III of the SBC Constitution. Crucially, this is a motion he plans to make from the floor at the meeting. He explicitly states he will move to suspend Standing Rule 6 so that the Committee on Order of Business MAY schedule the motion for debate — confirming the amendment is NOT yet on the official Order of Business [20d242, f5a2bf].

3. Mohler's proposed wording would add to the Constitution that cooperating churches do "not act to affirm, appoint, or endorse a woman serving in the office or function of a pastor/elder/overseer." While this is indeed a constitutional amendment (not a bylaw change or resolution) addressing restricting the pastor/elder office to men, the resolution criteria require an official publication confirming it has been placed ON the Order of Business — not merely an announced intent to introduce it from the floor [f5a2bf].

Because the procedure described is a floor motion requiring suspension of standing rules to even be scheduled, and no official Order of Business / Book of Reports published by June 1, 2026 lists such a constitutional amendment as a confirmed agenda item, the YES condition is not met. The question resolves NO.

Sources:
- Baptist Press, "Mohler to call for 'Truth & Unity' amendment to SBC Constitution at annual meeting" (May 18, 2026): https://www.baptistpress.com/resource-library/news/mohler-to-call-for-truth-unity-amendment-to-sbc-constitution-at-annual-meeting/ [20d242]
- AlbertMohler.com, "Truth and Unity Amendment" (May 18, 2026): https://albertmohler.com/2026/05/18/truth-and-unity-amendment/ [f5a2bf]
- Baptist Press, "2026 SBC Annual Meeting schedule released": https://www.baptistpress.com/resource-library/news/2026-sbc-annual-meeting-schedule-released/ [e3daa6]

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-26. `1d1d4a2b-b89a-5008-85e4-4fd4c53176c0`

- Recorded outcome: **NO** · present date `2026-05-15 22:33:51.101412` (window ends end of UTC day `2026-05-15`) · expected resolution `2026-07-01T00:00:00`

**Question**

Will China officially attribute blame to the United States or Israel for the attack on its oil tanker in the Strait of Hormuz by July 1, 2026?

**Resolution criteria**

This question resolves as **YES** if, on or after May 12, 2026, and before 23:59 UTC on July 1, 2026, any of the following Chinese government entities officially and publicly attribute blame or responsibility for the Strait of Hormuz tanker attack (confirmed May 8, 2026) to the United States or Israel:

- The **Ministry of Foreign Affairs** (MFA) of the People's Republic of China, via an official statement, press conference transcript, or spokesperson remark published on fmprc.gov.cn;
- The **President of the People's Republic of China** (Xi Jinping), via an official address or statement carried by Xinhua News Agency (xinhuanet.com);
- The **State Council** of the People's Republic of China, via an official statement.

"Publicly attribute blame" means the entity explicitly states or directly implies that the United States, Israel, or their military forces were responsible for, or caused, the attack on the Chinese-crewed tanker. General criticism of the war or expressions of concern do not qualify — the statement must specifically connect the US or Israel to the tanker attack.

**Resolution source:** The official MFA website (https://www.fmprc.gov.cn/eng/), Xinhua (https://english.news.cn/), or credible major international news outlets such as Reuters (https://www.reuters.com/), AP News (https://apnews.com/), or the New York Times (https://www.nytimes.com/).

If no qualifying statement is found by 23:59 UTC on July 1, 2026, the question resolves **NO**.

**Exact later resolution packet — this is the object under audit**

The question resolves NO. No qualifying statement was found in which China's MFA, President Xi Jinping, or the State Council specifically attributed blame for the Strait of Hormuz tanker attack (confirmed May 8, 2026) to the United States or Israel during the window (on/after May 12, 2026 and before 23:59 UTC July 1, 2026).

Key evidence:

1) The actual attacker of the Chinese-owned tanker (the JV Innovation, hit May 4, 2026 near the UAE) was widely identified as Iran/the IRGC — e.g., US UN envoy Mike Waltz accused Iran of conducting the attack. There is no record of China blaming the US or Israel for this specific attack in the resolution window [fa34c2, eb4c37].

2) China's initial official response was explicitly non-attributive: at the MFA regular press conference (May 7, 2026), spokesperson Lin Jian expressed that China was "deeply concerned" and opposed escalation, protecting civilians/non-military assets, but did NOT name a perpetrator [763c46]. Reuters' May 8 report likewise confirmed the MFA expressed "deep concern" and that the attacker was "unclear" [ced9fb]. The resolution criteria state that if the evidence only shows "deep concern" or calls the attacker "unclear," the question resolves NO.

3) China's repeated "root cause" language — that "the illegal military actions of the United States and Israel against Iran" are the root cause of obstacles/disruptions to navigation in the Strait of Hormuz (e.g., MFA spokesperson Mao Ning) — is a general criticism of the war and its effect on navigation/blockage, NOT a statement connecting the US/Israel to the specific tanker attack. Moreover, these statements date from early April 2026 (e.g., April 2, 2026), before the May 12 window opens [0d9b07]. The resolution criteria expressly exclude general war criticism and require a statement specifically connecting the US/Israel to the tanker attack.

4) Wikipedia summaries of "China in the 2026 Iran war" and the "2026 Strait of Hormuz crisis" (edited late June 2026) describe China maintaining a neutrality posture and avoiding direct, high-level attributions of blame for the specific incident; neither documents any MFA/Xi/State Council statement blaming the US or Israel for the tanker attack in the window [0d5135, fa34c2, eb4c37].

Searches of the allowed sources (fmprc.gov.cn, Xinhua/english.news.cn, Reuters, AP News, NYT) for May 12–July 1, 2026 turned up no statement from the MFA, Xi Jinping, or the State Council explicitly stating or directly implying that the US, Israel, or their forces were responsible for/caused the attack on the Chinese-crewed tanker. Therefore the question resolves NO.

Primary URLs:
- Reuters (May 8, 2026): https://www.reuters.com/world/china/china-confirms-attack-oil-tanker-strait-hormuz-earlier-this-week-2026-05-08/
- MFA press conference (May 7, 2026): https://www.fmprc.gov.cn/eng/xw/fyrbt/202605/t20260507_11906405.html
- Wikipedia "2026 Strait of Hormuz crisis": https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis
- Wikipedia "China in the 2026 Iran war": https://en.wikipedia.org/wiki/China_in_the_2026_Iran_war

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-27. `e0385127-5ec1-592f-8846-2c8b36ffe68f`

- Recorded outcome: **NO** · present date `2026-05-29 04:55:07.046399` (window ends end of UTC day `2026-05-29`) · expected resolution `2026-07-01T00:00:00`

**Question**

Will Carla Zambelli be physically transferred to Brazilian custody by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if Carla Zambelli (https://en.wikipedia.org/wiki/Carla_Zambelli) is physically transferred to Brazilian custody on or after May 12, 2026 (00:00 UTC), and on or before July 1, 2026 (23:59 UTC). It resolves **No** otherwise.

**Definition of "physically transferred":** Zambelli is considered physically transferred when at least one of the following has occurred:
- She has boarded an aircraft under the guard or escort of Brazilian or Italian law enforcement officials for the purpose of extradition to Brazil; OR
- She has been formally received by Brazilian authorities (e.g., the Brazilian Federal Police) on Brazilian soil or at a designated handover point.

**Definition of "Brazilian custody":** Zambelli is in Brazilian custody when she is under the physical control and legal authority of Brazilian government officials, including but not limited to the Brazilian Federal Police (Polícia Federal).

The transfer must occur on or after May 12, 2026 (00:00 UTC).

**Verification sources:** Resolution will be determined based on official statements from the Italian Ministry of Justice (https://www.giustizia.it/) or the Brazilian Federal Police (https://www.gov.br/pf/), or credible reporting from at least one of the following news agencies/outlets:
- Reuters (https://www.reuters.com/)
- Associated Press (https://apnews.com/)
- Agência Brasil (https://agenciabrasil.ebc.com.br/)
- G1/Globo (https://g1.globo.com/)
- BBC News Brasil (https://www.bbc.com/portuguese)
- Folha de S.Paulo (https://www1.folha.uol.com.br/)

**Exact later resolution packet — this is the object under audit**

The question resolves NO. Carla Zambelli was NOT physically transferred to Brazilian custody within the window of May 12, 2026 (00:00 UTC) through July 1, 2026 (23:59 UTC). Instead, the extradition was definitively blocked and she was released.

Key evidence, all from resolution-approved sources:

1. Agência Brasil ("Zambelli é libertada na Itália após tribunal negar extradição," dated 2026-05-22, https://agenciabrasil.ebc.com.br/justica/noticia/2026-05/zambelli-e-libertada-na-italia-apos-tribunal-negar-extradicao): On May 22, 2026, the Italian Court of Cassation (Italy's highest judicial instance) denied Brazil's request to extradite Zambelli. As a result, she was released from prison in Italy. The court found errors in the prior decisions that had authorized the extradition [Zambelli é libertada na Itália após tribunal negar extradição](https://agenciabrasil.ebc.com.br/justica/noticia/2026-05/zambelli-e-libertada-na-italia-apos-tribunal-negar-extradicao).

2. BBC News Brasil ("Em reviravolta, Carla Zambelli é solta na Itália após Justiça anular...," dated 2026-05-22, https://www.bbc.com/portuguese/articles/ckgplj8yp0yo): On May 22, 2026, the Italian Supreme Court of Cassation annulled the extradition of Zambelli to Brazil and ordered her immediate release; she was freed from detention that same evening. She was not transferred to Brazilian custody [Em reviravolta, Carla Zambelli é solta na Itália após Justiça anular ... - BBC](https://www.bbc.com/portuguese/articles/ckgplj8yp0yo).

3. G1/Globo ("Entenda a condenação de Zambelli...," dated 2026-05-22, https://g1.globo.com/politica/noticia/2026/05/22/carla-zambelli-entenda-extraditacao-italia.ghtml): On May 22, 2026, the Court of Cassation ruled against the extradition, reversing the Court of Appeal, and ordered her release from the women's penitentiary near Rome. The judicial process was considered exhausted, and she was not transferred to Brazilian custody [Entenda a condenação de Zambelli no Brasil e pedido de extradição - G1](https://g1.globo.com/politica/noticia/2026/05/22/carla-zambelli-entenda-extraditacao-italia.ghtml).

Because the extradition was judicially annulled (a "no remand" quashing at the final judicial instance), the Italian Minister of Justice could not authorize a surrender, and Zambelli was set free rather than handed over. Additional confirmation that no transfer occurred by July 1: reporting from late June 2026 (e.g., Folha de S.Paulo, June 2026; Agência Brasil, June 2026) shows the Brazilian government (AGU) was still filing renewed appeals/manifestations in Italy attempting to secure her extradition — behavior that would be nonsensical had she already been transferred. This is consistent with the definition of "physically transferred" (boarding an escorted aircraft or being received by Brazilian authorities) not having been met at any point in the window.

Therefore, none of the "physically transferred to Brazilian custody" conditions were satisfied between May 12 and July 1, 2026, and the question resolves NO (0).

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-28. `f96455a1-a3a2-5180-a110-d9c931bd3934`

- Recorded outcome: **NO** · present date `2026-05-03 05:15:57.247039` (window ends end of UTC day `2026-05-03`) · expected resolution `2026-06-01 00:00:00`

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

**Exact later resolution packet — this is the object under audit**

The question resolves NO. No qualifying "major opposition party" (one that held ≥1 seat in the House of Peoples' Representatives at the previous parliament's dissolution, OR is among the named parties EZEMA, OFC, OLF, EPRP, NaMA, Tigray Democratic Solidarity, or a coalition containing one of them) formally announced an election boycott within the required window of May 1, 2026 to 06:00 EAT June 1, 2026.

Evidence reviewed:
1) ONLF (Ogaden National Liberation Front) DID formally announce on May 6, 2026 that it "will not participate in Ethiopia's deceptive election" [8f0834] — this is the only in-window boycott-type announcement found. However, ONLF does NOT meet the "major opposition party" definition: per the 2021 election results, ONLF won zero seats (only 5,634 votes, 0.02%) and held no HoPR seat [4b95f2], and ONLF is not in the question's enumerated list of named parties. Thus it does not qualify.

2) Tigray Democratic Solidarity (Simret), a named party, only conditionally THREATENED to boycott in February 2026 (over the House of Federation constituency dispute) — outside the May 1–June 1 window — and subsequently withdrew its lawsuit and registered to participate [78a06c]. No in-window formal boycott announcement.

3) The Peace for Ethiopia Coalition (eight parties) threatened to WITHDRAW on April 17, 2026 — before the window — and it was a conditional threat ("unless widespread violations are addressed"); the coalition went on to campaign and contest seats [bfb124, f913ed]. Out of window and not an unconditional boycott.

4) OFC (named party) was "squeezed into fielding just ten candidates to escape deregistration" — i.e., it PARTICIPATED rather than boycotted; its chairman said this was to meet legal obligations [bfb124, f913ed]. Pre-election (May 29) and election-day (June 1) coverage confirm major opposition parties including NaMA and EZEMA (which held 5 and 4 seats respectively in 2021) fielded candidates and participated [8089af, b48cf2, 5b4c9f].

5) EPRP (named party) called for nationwide protests on May 8, 2026 — explicitly criticism/protest, not a boycott, and the resolution criteria distinguish protests from boycotts.

6) The registered OLF party's only located boycott-style press release dates to 2021 [7ef9f2]; the OLF-OLA statements come from an armed group, not the registered party.

Since the only in-window non-participation declaration (ONLF, May 6) came from a party that fails the "major opposition party" test, and all named/seated parties either participated or only threatened/protested (and Simret's and the coalition's threats fell outside the window), no qualifying formal boycott announcement occurred. Resolution: NO (0).

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-29. `1f4fcd81-59ce-5b8f-a614-453f9d871d80`

- Recorded outcome: **NO** · present date `2026-05-14 05:42:28.440408` (window ends end of UTC day `2026-05-14`) · expected resolution `2026-07-01T00:00:00`

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

**Exact later resolution packet — this is the object under audit**

The question resolves NO (0) because no written opinion was issued by the Second Circuit in United States v. Combs, No. 25-2623, by the deadline of 11:59 PM UTC on July 1, 2026.

Key evidence:
- The CourtListener docket for United States of America v. Combs, No. 25-2623 (https://www.courtlistener.com/docket/71724945/united-states-of-america-v-combs/) was last updated June 30, 2026, and shows NO written opinion, decision, judgment, or summary order filed after the oral argument. The most recent substantive docket entry (Entry 74) is dated April 9, 2026 (oral argument before the three-judge panel). No filings exist for May 2026 or June 2026 [405576, 3aea88].
- Oral arguments were held April 9, 2026, and multiple contemporaneous news reports (Reuters, NY1, NBC) noted the panel "did not immediately rule." As of late June 2026, the appeal is described as "still pending" with a decision expected "in the weeks" ahead — i.e., not yet decided.
- No credible news source reported any opinion being issued between May 12, 2026 and July 1, 2026.

The resolution criteria explicitly provide: "This question resolves No if ... No opinion is issued by 11:59 PM UTC on July 1, 2026." Because no opinion issued at all, the antecedent for a YES (an opinion explicitly holding that the use of acquitted conduct violated the USSG) was never triggered. Per the resolution criteria, the absence of any opinion resolves the question NO (0) — NOT annulled. There is therefore no basis for a -1 annulment.

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-30. `65ab10c3-bb24-5e73-873f-da584796c42e`

- Recorded outcome: **NO** · present date `2026-05-14 11:42:23.407058` (window ends end of UTC day `2026-05-14`) · expected resolution `2026-07-01T00:00:00`

**Question**

Will Congress pass a long-term reauthorization of FISA Section 702 (extending it by 1 year or more) between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026, and before July 1, 2026 (23:59 UTC), the President signs into law a bill that reauthorizes FISA Section 702 for a period of **1 year (365 days) or longer** from the date of enactment or from the current expiration date, whichever is later.

This question resolves **No** if any of the following occur by July 1, 2026 (23:59 UTC):
- Congress passes only another short-term extension (defined as an extension of **less than 1 year / 365 days**).
- Congress allows Section 702 to lapse without passing any legislation.
- A bill passes both chambers but is not signed by the President.
- No reauthorization legislation of any kind is enacted.

**"Passing"** means passage by both chambers of the U.S. Congress (House and Senate) AND signature by the President (i.e., enacted into law).

The duration of the extension is determined by the text of the enacted legislation. Resolution will be verified using the official legislative record on Congress.gov: https://www.congress.gov/search?q=%7B%22source%22%3A%22legislation%22%2C%22search%22%3A%22FISA+section+702%22%7D

If the enacted law specifies a new sunset date rather than a duration, the extension length is calculated from the current expiration date (~June 13, 2026) to the new sunset date.

**Exact later resolution packet — this is the object under audit**

The question resolves **NO (0)**.

**Resolution criteria:** YES requires that, on or after May 12, 2026 and before July 1, 2026 (23:59 UTC), the President signs into law a bill reauthorizing FISA Section 702 for 1 year (365 days) or longer. NO if only a short-term extension passes, if 702 lapses without legislation, if a bill passes both chambers but isn't signed, or if nothing is enacted.

**What actually happened:**

1. **No long-term reauthorization was enacted in the resolution window.** The official legislative record on Congress.gov shows the only FISA Section 702 bill that became a Public Law in 2026 was S.4465, which became Public Law No. 119-87 on April 30, 2026 [e557b6]. That was a short-term (~45-day) extension and, critically, it was enacted on April 30 — *before* the May 12, 2026 start of the resolution window — so it cannot satisfy the "on or after May 12, 2026" requirement, and in any case it was far less than 365 days. A later Congress.gov review of all 702-related legislation confirms that no bill reauthorizing or extending Section 702 was enacted or signed into law between May 12 and July 1, 2026; the only 2026 Public Law on the subject remained PL 119-87 (April 30, 2026) [aa9e38].

2. **Congress failed to pass any reauthorization, and Section 702 LAPSED.** The Senate's FISA reauthorization stalled in an early-morning vote on June 5, 2026 (47–52 motion to proceed failed). A House measure (H.R.9238) to extend/reauthorize failed passage on June 11, 2026 [aa9e38]. Section 702 then expired at midnight on June 12, 2026. NPR reported June 12–13, 2026 that "Congress has let a key spy tool, Section 702 of the Foreign Intelligence Surveillance Act, lapse," and that both chambers "made a series of failed bids to extend Section 702, then ... left town" [e71d61]. The EFF confirmed the authority expired at midnight on June 12, 2026, noting "the House refused to approve even a short-term renewal" [c225cf].

3. **Status remained lapsed through the end of the window.** As of mid-to-late June 2026, lawmakers were still negotiating with no enacted reauthorization, and the Senate was still meeting on the matter as late as June 29, 2026 (with nothing signed into law by July 1, 2026) [aa9e38].

**Both-chamber passage + Presidential signature check:** No bill reauthorizing Section 702 for 1 year or more passed both the House and Senate and was signed by the President during May 12 – July 1, 2026. In fact, no reauthorization passed both chambers at all — the House and Senate both rejected the relevant measures, and the program lapsed [e71d61][c225cf][aa9e38].

Because no bill reauthorizing FISA Section 702 for 365 days or longer was signed into law by the President within the window (and indeed the program was allowed to lapse), the question resolves **NO (0)**.

Verifying sources:
- Congress.gov legislation search (source specified in resolution criteria): only 702 Public Law in 2026 is PL 119-87, enacted 04/30/2026 — https://www.congress.gov/bill/119th-congress/senate-bill/4465 [e557b6][aa9e38]
- NPR, "FISA 702, a key U.S. spy tool, has lapsed. Now what?" (June 12, 2026): https://www.npr.org/2026/06/12/nx-s1-5856291/fisa-702-surveillance-expiration-bill-pulte [e71d61]
- EFF, "Victory! 702 has Expired!" (June 12, 2026): https://www.eff.org/deeplinks/2026/06/victory-702-has-expired [c225cf]

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-31. `a51291e6-e7a6-551f-ae98-84c0fd9ba7ca`

- Recorded outcome: **NO** · present date `2026-05-03 00:19:34.329209` (window ends end of UTC day `2026-05-03`) · expected resolution `2026-06-01 00:00:00`

**Question**

Will the IRS or Treasury Department publish formal guidance on Section 280E relief for state-licensed medical cannabis businesses between May 1, 2026 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the IRS or Treasury Department publishes formal guidance on or after May 1, 2026 (00:00 UTC) and on or before June 1, 2026 (23:59 UTC) that explicitly addresses the application of, or relief from, Section 280E of the Internal Revenue Code for state-licensed medical cannabis businesses following the DOJ rescheduling order.

**Definition of "formal guidance":** For purposes of this question, "formal guidance" means any of the following published guidance types as defined by the IRS (https://www.irs.gov/newsroom/understanding-irs-guidance-a-brief-primer): a Notice, Revenue Ruling, Revenue Procedure, Treasury Decision (final or temporary regulation), or Announcement [Understanding IRS guidance - A brief primer](https://www.irs.gov/newsroom/understanding-irs-guidance-a-brief-primer). Informal communications such as press releases, blog posts, FAQ pages, or oral statements do not qualify. The April 23, 2026 Treasury press release (https://home.treasury.gov/news/press-releases/sb0471) does not qualify and is explicitly excluded.

**Definition of "Section 280E relief":** Guidance that addresses whether and how Section 280E of the Internal Revenue Code (26 U.S.C. § 280E, https://www.law.cornell.edu/uscode/text/26/280E) ceases to apply, or applies differently, to state-licensed medical cannabis businesses as a result of cannabis rescheduling from Schedule I to Schedule III.

**Resolution source:** The guidance must appear on the IRS published guidance page (https://www.irs.gov/newsroom/irs-guidance) or in the Internal Revenue Bulletin (https://www.irs.gov/irb), or on the Treasury Department website (https://home.treasury.gov), or in the Federal Register (https://www.federalregister.gov/). If no qualifying guidance is published by 23:59 UTC on June 1, 2026, the question resolves **No**.

**Exact later resolution packet — this is the object under audit**

The question resolves NO. It asks whether the IRS or Treasury published formal guidance (a Notice, Revenue Ruling, Revenue Procedure, Treasury Decision, or Announcement) explicitly addressing Section 280E relief for state-licensed medical cannabis businesses between May 1, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC).

Key facts established:
- On April 23, 2026, Treasury and the IRS issued only a PRESS RELEASE announcing their *plan* to issue future guidance addressing Section 280E consequences of the DOJ rescheduling order. This press release (home.treasury.gov/news/press-releases/sb0471) is explicitly excluded by the question's resolution criteria and is dated before the resolution window [Treasury, IRS Announce Process for Tax Guidance Following DOJ ...](https://home.treasury.gov/news/press-releases/sb0471).
- As of April 27–28, 2026 (before the window opened), commentators confirmed only the announcement existed and no formal guidance had been published; practitioners were advised to monitor the Internal Revenue Bulletin for future publication [Cannabis Rescheduling: DOJ, Treasury, and DEA Updates Since ...](https://foleyhoag.com/news-and-insights/blogs/cannabis-and-the-law/2026/april/cannabis-rescheduling-doj-treasury-and-dea-updates-since-the-april-23-order/) [Is the Most Impactful Part of Marijuana Rescheduling an Obscure ...](https://www.jdsupra.com/legalnews/is-the-most-impactful-part-of-marijuana-9981895/).
- Decisively, on May 29, 2026 — just two days before the window closed — both Cannabis Business Times and Marijuana Moment reported that seven U.S. House Democrats sent a letter urging the IRS and Treasury to issue "prompt"/"swift and clear" tax guidance on Section 280E, expressly because no such guidance had yet been issued (roughly five weeks after the April 23 announcement) [7 House Democrats Demand IRS, Treasury Provide 280E ...](https://www.cannabisbusinesstimes.com/legislation-and-regulation/cannabis-tax-law/news/15826367/7-house-democrats-demand-irs-treasury-provide-280e-cannabis-guidance) [Lawmakers want cannabis tax guidance from IRS (Newsletter](https://www.marijuanamoment.net/lawmakers-want-cannabis-tax-guidance-from-irs-newsletter-may-29-2026/). Lawmakers actively demanding guidance days before the deadline confirms that no qualifying formal guidance (Notice, Rev. Rul., Rev. Proc., TD, or Announcement) was published on any of the specified sources (IRS guidance page, Internal Revenue Bulletin, Treasury website, or Federal Register) within the resolution window.

Since no qualifying formal guidance was published by 23:59 UTC on June 1, 2026, the question resolves NO (0).

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):

### NO-32. `826dafc3-01da-575f-97af-e3c07a999d0f`

- Recorded outcome: **NO** · present date `2026-05-12 19:13:26.898565` (window ends end of UTC day `2026-05-12`) · expected resolution `2026-07-01T00:00:00`

**Question**

Will the USTR formally announce new Section 301 tariffs on imports from at least one country before July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 10, 2026, and before 11:59 PM UTC on July 1, 2026, the USTR makes a **formal announcement** of new tariffs under Section 301 of the Trade Act of 1974 (19 U.S.C. § 2411) on imports from at least one country. A "formal announcement" is defined as either:

- An official press release published on the [USTR press releases page](https://ustr.gov/about/policy-offices/press-office/press-releases), **or**
- A notice published in the [Federal Register](https://www.federalregister.gov/agencies/trade-representative-office-of-united-states)

that explicitly states the USTR is imposing, or has determined to impose, new tariffs under Section 301 authority on imports from one or more countries.

**Clarification on "proposed" vs. "final":** The announcement of a mere *proposed* list of products for public comment does **not** satisfy resolution. The announcement must reflect a **final determination** or **action** to impose tariffs—i.e., the USTR must have determined that tariffs will be applied, not merely that tariffs are being considered. A Federal Register notice requesting public comment on a proposed tariff list would not count.

If no such announcement meeting these criteria is made by 11:59 PM UTC on July 1, 2026, the question resolves **No**.

**Exact later resolution packet — this is the object under audit**

The question resolves NO. It required a USTR FORMAL announcement (official press release or Federal Register notice) of a FINAL determination or action to IMPOSE new Section 301 tariffs on imports from at least one country, made on/after May 10, 2026 and before 11:59 PM UTC July 1, 2026. The resolution criteria explicitly state that a mere PROPOSED tariff list open for public comment does NOT satisfy resolution.

Every relevant USTR Section 301 tariff action in the window was a PROPOSAL, not a final determination:

1. Brazil (announced June 1, 2026): USTR determined Brazil's practices are actionable under Section 301(b) but only "proposed responsive action for public comment," inviting written comments by July 1, 2026, with a hearing scheduled for July 6, 2026 [36047c]. This is a proposal, and the hearing/implementation postdate July 1.

2. Forced Labor – 60 economies (announced June 2, 2026): USTR made findings of actionability and "proposed responsive action for public comment," with written comments due July 6, 2026 and hearings beginning July 7, 2026 [2c43a1]. Legal analyses confirm these were proposed 10%–12.5% tariffs to be "finalized and implemented after USTR completes the public comment and hearing process," with USTR aiming to be ready to impose them around the July 24, 2026 expiration of the Section 122 tariffs [cc7c2c].

3. Structural Excess Capacity – 16 economies: As of mid-June 2026, no final determination to impose tariffs had been issued; determinations were described as pending/imminent, and any tariffs were expected to align with the ~July 25, 2026 timeframe (after Section 122 expires July 24) [cc7c2c, 2fa6dd].

Because all announcements before the July 1, 2026 deadline were proposals with hearings scheduled July 6–7, 2026 and expected implementation in late July 2026 — and the resolution criteria explicitly exclude proposals/requests for comment — no qualifying final determination or action to impose Section 301 tariffs was announced within the window. The question resolves NO (0).

Key sources: USTR press release "USTR Makes Findings and Proposes Action in 60 Section 301 Investigations..." (June 2, 2026) [2c43a1]; USTR press release "USTR Section 301 Determination on Brazil's Unreasonable Acts, Policies, and Practices" (June 1, 2026) [36047c]; White & Case alert (June 5, 2026) [cc7c2c]; American Action Forum "The New Section 301 Tariff Regime" [2fa6dd].

**Checks (open the cited sources):**
- [ ] recorded outcome is correct against the cited/primary evidence
- [ ] cited sources exist and support what the packet says they support
- [ ] no cited evidence postdates the resolution deadline in a way the packet relies on
- [ ] no temporal-logic error inside the packet
- [ ] criteria and the claimed outcome genuinely align

- Verdict: `[ ] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason (required for MATERIAL_ERROR / UNVERIFIABLE, one line):
