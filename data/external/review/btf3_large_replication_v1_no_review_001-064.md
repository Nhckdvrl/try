# btf3_large_replication_v1 — realized NO review chunk NO-001–NO-064

> Display chunk of the immutable queue (`btf3_large_replication_v1_no_queue.json`). Review strictly top-to-bottom; stop only when this bucket reaches 128 ACCEPTs overall. Do not skip ahead, reorder, or prefer better-looking questions. A REJECT/UNSURE permanently consumes its queue slot and is never resampled, re-reviewed, or hand-repaired.

All four gates must hold to ACCEPT. On REJECT or UNSURE write exactly one line of reason.

### NO-1. `ee5e37c7-f82f-5d49-95b2-86ad466c9d50`

- Present date: `2026-05-03 12:56:37.381726`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

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

**Pre-cutoff background**

Google's Veo is a family of AI video generation models developed by Google DeepMind. As of May 2, 2026, the latest version is Veo 3.1, which was first released in October 2025 and updated in January 2026 with features like vertical video generation and reference image capabilities [Veo — Google DeepMind](https://deepmind.google/models/veo/). Prior versions include Veo 3 (released May 2025) and the original Veo (2024). Google has generally followed an incremental versioning pattern (e.g., Veo 3 → Veo 3.1) rather than jumping to major new version numbers.

Google I/O 2026 is scheduled for May 19–20, 2026, at Shoreline Amphitheatre in Mountain View, California (https://io.google/2026/about). Google I/O has historically served as the launch vehicle for major Veo versions (Veo 3 was announced at Google I/O 2025). This makes the May 19–20 window the most likely opportunity for a Veo 4 announcement within the resolution period.

Competition in the AI video generation space is intense, with OpenAI and Meta pushing their own models, which may incentivize Google to release a major new version. However, as of May 2, 2026, Google has not officially announced Veo 4. On Manifold Markets, the probability of Veo 4 releasing before June 2026 was estimated at approximately 20% [Veo 4 (Google) release date - Manifold Markets](https://manifold.markets/Bayesian/veo-4-google-release-date), though significant speculation exists that Google I/O 2026 could be the venue for such an announcement.

For the current official status of Veo, see: https://deepmind.google/models/veo/

**Exact later resolution packet**

The question resolves NO. The resolution requires Google to officially announce or release a model explicitly named "Veo 4" (or "Veo 4.x") on or after May 2, 2026 and by 23:59 UTC on June 1, 2026, via one of the specified official sources (Google DeepMind blog, Google's official blog, or an official Google I/O keynote).

Evidence from the specified official sources:

1) The official Google DeepMind Veo models page (https://deepmind.google/models/veo/) still identifies the current model as "Veo 3.1" with no mention of any "Veo 4" model [Veo 3.1 - Google DeepMind](https://deepmind.google/models/veo/).

2) The official Google Blog transcript of Sundar Pichai's Google I/O 2026 keynote (held May 19, 2026; https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) contains no mention of "Veo 4." The video-generation/media announcements at I/O 2026 centered on the Gemini family — specifically "Gemini Omni" and "Gemini Omni Flash" — not a "Veo 4." The word "Veo" appears only in reference to the existing Veo model [I/O 2026: Welcome to the agentic Gemini era - Google Blog](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/).

Since Google I/O 2026 (May 19-20, 2026) was the most likely venue and it did not feature a Veo 4 announcement, and no official Google blog post or product documentation using the "Veo 4" name exists through June 1, 2026, the antecedent (an official Veo 4 announcement/release) did not occur.

Third-party sources (e.g., YouTube/Instagram clickbait titles like "GEMINI 4 + VEO 4," and a "The Elites" Instagram post) circulated claiming a Veo 4, but these are not official Google sources and are explicitly excluded by the resolution criteria. Independent coverage (PixVerse, WaveSpeed) confirms that as of late May 2026 there was no official Google announcement, product page, or documentation for a "Veo 4" model.

Therefore the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-2. `c6c6f543-0d08-5e88-a85f-bb106cb74263`

- Present date: `2026-05-03 02:09:17.680723`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will a federal court issue a new injunction blocking the transfer of Department of Education programs to other agencies between May 1, 2026, and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between May 1, 2026, 00:00 UTC and June 1, 2026, 23:59 UTC, any U.S. federal court (district court, circuit court of appeals, or the Supreme Court) issues a new [injunction](https://www.law.cornell.edu/wex/injunction)—including a preliminary injunction, temporary restraining order (TRO), or emergency stay—that blocks, halts, or pauses the transfer of one or more programs, offices, or functions from the U.S. Department of Education to any other federal agency.

Injunctions issued before May 1, 2026, 00:00 UTC do **not** count toward a "Yes" resolution, even if they remain in effect during the resolution window. Only newly issued orders count.

"[Program transfers](https://federalnewsnetwork.com/reorganization/2026/02/congress-fully-funded-education-dept-but-its-moving-ahead-with-reassigning-employees-to-other-agencies/)" means the reassignment or relocation of programs, offices, employees, or functions from the Department of Education to other federal departments or agencies as part of the administration's restructuring or dismantling efforts.

Resolution will be verified using official court records available via [PACER](https://pacer.uscourts.gov/) or credible legal/news reporting from sources such as [Education Week](https://www.edweek.org/), [Reuters](https://www.reuters.com/), [SCOTUSblog](https://www.scotusblog.com/), or the [Brookings lawsuit tracker](https://www.brookings.edu/articles/tracking-lawsuits-challenging-the-trump-administrations-k-12-education-agenda/).

If no such new injunction is issued during the specified window, the question resolves **No**.

**Pre-cutoff background**

On March 20, 2025, President Trump issued an executive order to abolish the U.S. Department of Education (ED). The administration has pursued plans to transfer ED's functions—including career and technical education (CTE) oversight, student loan servicing, and other programs—to agencies such as the Department of Labor, the Small Business Administration, and others [Educators, School Districts, and Workers Sue to Stop Trump's Plan ...](https://democracyforward.org/work/legal/educators-school-districts-and-workers-sue-to-stop-trumps-plan-to-dismantle-the-department-of-education/).

A coalition of educators, school districts, unions, and state attorneys general filed suit in *New York v. McMahon* (U.S. District Court for the District of Massachusetts) on March 6, 2025, seeking to block the dismantling. On May 22, 2025, Judge Myong Joun granted a preliminary injunction halting the administration's restructuring efforts and ordering reinstatement of terminated employees [Educators, School Districts, and Workers Sue to Stop Trump's Plan ...](https://democracyforward.org/work/legal/educators-school-districts-and-workers-sue-to-stop-trumps-plan-to-dismantle-the-department-of-education/). However, the U.S. Supreme Court stayed that injunction on July 14, 2025, allowing the administration to resume dismantling activities [Educators, School Districts, and Workers Sue to Stop Trump's Plan ...](https://democracyforward.org/work/legal/educators-school-districts-and-workers-sue-to-stop-trumps-plan-to-dismantle-the-department-of-education/).

As of early 2026, the litigation remains active. The administration has continued transferring ED functions to other agencies, and multiple related lawsuits continue in various federal courts [Tracking lawsuits challenging the Trump administration's K-12 ...](https://www.brookings.edu/articles/tracking-lawsuits-challenging-the-trump-administrations-k-12-education-agenda/). The Brookings Institution maintains a tracker of lawsuits challenging the Trump administration's education agenda (https://www.brookings.edu/articles/tracking-lawsuits-challenging-the-trump-administrations-k-12-education-agenda/) [Tracking lawsuits challenging the Trump administration's K-12 ...](https://www.brookings.edu/articles/tracking-lawsuits-challenging-the-trump-administrations-k-12-education-agenda/). Additional court orders have addressed specific ED actions such as TRIO grant cancellations and student loan program changes. The Supreme Court's July 2025 stay of the main injunction remains a key factor, but district courts retain the ability to issue new, narrower injunctions on specific program transfers.

For purposes of this question, "program transfers" refers to the reassignment or relocation of programs, offices, or functions currently housed within the U.S. Department of Education to other federal agencies, as described in the executive order (https://www.whitehouse.gov/presidential-actions/improving-education-outcomes-by-empowering-parents-states-communities-and-teachers/) and related implementation plans. An "[injunction](https://www.law.cornell.edu/wex/injunction)" is a court order requiring a party to do or refrain from doing a specific act, including preliminary injunctions and temporary restraining orders (TROs).

**Exact later resolution packet**

The question resolves NO. No U.S. federal court issued a new injunction, TRO, or emergency stay between May 1, 2026, 00:00 UTC and June 1, 2026, 23:59 UTC that blocked, halted, or paused the transfer of Department of Education programs, offices, or functions to other federal agencies.

Evidence:
- The Rise Up: Federal Workers Legal Defense Network litigation tracker (workerslegaldefense.org/litigation-tracker), updated May 27, 2026, documented the status of the core Department of Education dismantling/transfer cases during the window. In Somerville Public Schools v. Trump (lead case State of New York v. McMahon, D. Mass.), the case was in the discovery phase with a summary judgment scheduling order entered April 21, 2026 — no new injunction. In NAACP v. U.S., on May 8, 2026 the court merely denied the government's second motion to dismiss (not an injunction). The Victim Rights Law Center injunction had been vacated in January 2026. None of these constituted a new injunction blocking program transfers in the window [5d0777].
- The Just Security litigation tracker (justsecurity.org/107087), updated May 28, 2026, listing 807 challenges to Trump administration actions, contained no Department of Education case with a new injunction/TRO/stay blocking transfer of programs or functions to other agencies issued between May 1 and June 1, 2026 [2a328f].
- The Brookings lawsuit tracker (the named primary resolution source) was last updated February 3, 2026 and thus did not cover the window, but provides no contrary evidence [50baf9, f2a977].

Department of Education-related litigation activity during the window concerned other matters, not agency transfers: the ACT Now Illinois case (N.D. Ill.) involved a preliminary injunction motion (filed April 30/May 1, 2026) over termination of Full-Service Community Schools grants — a funding/grant-cancellation issue, not a transfer of functions to another agency. The May 19, 2026 Maryland et al. v. U.S. Dept. of Education suit (per Reuters) challenged a May 1, 2026 Final Rule on student loan/professional degree restrictions — also not a program transfer, and it was a newly filed suit, not an injunction.

Multiple targeted searches for any injunction blocking ED transfers issued on or around June 1, 2026 returned nothing. Therefore, no qualifying new injunction was issued during the resolution window, and the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-3. `4e1869f7-70cc-5b9c-9cb5-e6d6fbfc77a5`

- Present date: `2026-05-02 19:29:04.149888`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the Sudanese Armed Forces (SAF) control the town of Kurmuk, Blue Nile State, on June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, as of June 1, 2026 at 23:59 UTC, the Sudanese Armed Forces (SAF, https://en.wikipedia.org/wiki/Sudanese_Armed_Forces) are reported to exercise military control over the town of Kurmuk (https://en.wikipedia.org/wiki/Kurmuk), Blue Nile State, Sudan.

"Control" means that the SAF (or allied government forces operating under SAF command) maintain a physical military presence in the town center of Kurmuk and are the dominant armed force in the town, as reported by credible sources.

The question resolves as **No** if:
- The RSF, SPLM-N al-Hilu, the Tasis Alliance, or any other non-SAF force controls Kurmuk; or
- The town is actively contested with no clear SAF dominance; or
- No credible reporting confirms SAF control.

**Resolution sources:** The question will be resolved based on reporting from at least one of the following credible sources: [Sudan War Monitor](https://sudanwarmonitor.com/), [ACLED](https://acleddata.com/), [Reuters](https://www.reuters.com/), [AP News](https://apnews.com/), [BBC](https://www.bbc.com/news), [Sudan Tribune](https://sudantribune.com/), or [Al Jazeera](https://www.aljazeera.com/). The most recent credible report available as of June 1, 2026 will be used. If sources conflict, Sudan War Monitor will be given priority as a specialist conflict tracker for the Sudanese civil war.

**Pre-cutoff background**

Kurmuk is a strategic town in Blue Nile State, Sudan, near the Ethiopian border (approximately 11.8°N, 34.3°E; see [Kurmuk on Wikipedia](https://en.wikipedia.org/wiki/Kurmuk)). It has been a key site of conflict during the ongoing Sudanese civil war.

In January 2026, the Rapid Support Forces ([RSF](https://en.wikipedia.org/wiki/Rapid_Support_Forces)) and the Sudan People's Liberation Movement–North faction led by Abdelaziz al-Hilu ([SPLM-N al-Hilu](https://en.wikipedia.org/wiki/Sudan_People%27s_Liberation_Movement-North_(al-Hilu))) launched a joint offensive in Blue Nile State as part of a coalition known as the Tasis Alliance [2026 Blue Nile campaign - Wikipedia](https://en.wikipedia.org/wiki/2026_Blue_Nile_campaign). On March 23–24, 2026, these forces captured Kurmuk, scattering SAF units [https://sudanwarmonitor.com/p/rebel-coalition-overran-sudan-army-garrison-north-of-kurmuk](https://sudanwarmonitor.com/p/rebel-coalition-overran-sudan-army-garrison-north-of-kurmuk)[2026 Blue Nile campaign - Wikipedia](https://en.wikipedia.org/wiki/2026_Blue_Nile_campaign).

The Sudanese Armed Forces ([SAF](https://en.wikipedia.org/wiki/Sudanese_Armed_Forces)) subsequently launched counter-operations in the region. On April 20, 2026, the SAF recaptured Magaja in the nearby Bau locality, but according to Sudan War Monitor (as of April 27, 2026), Kurmuk itself remains under Tasis Alliance control [https://sudanwarmonitor.com/p/rebel-coalition-overran-sudan-army-garrison-north-of-kurmuk](https://sudanwarmonitor.com/p/rebel-coalition-overran-sudan-army-garrison-north-of-kurmuk)[2026 Blue Nile campaign - Wikipedia](https://en.wikipedia.org/wiki/2026_Blue_Nile_campaign). Rebel forces have continued advancing north from Kurmuk, most recently capturing the garrison at Al-Keili [https://sudanwarmonitor.com/p/rebel-coalition-overran-sudan-army-garrison-north-of-kurmuk](https://sudanwarmonitor.com/p/rebel-coalition-overran-sudan-army-garrison-north-of-kurmuk).

The situation in Blue Nile State is highly fluid. The rainy season (typically beginning in May–June) could significantly affect military operations in the region. The SAF faces pressure on multiple fronts across Sudan, while the RSF-SPLM-N alliance has shown sustained offensive capability in this area.

**Exact later resolution packet**

The question resolves NO because no credible source confirms SAF military control over the town center of Kurmuk as of June 1, 2026, 23:59 UTC. The most recent reporting consistently shows the SAF was still only on the outskirts, attempting to recapture the town, while it remained under RSF/SPLM-N (Tasis Alliance) control.

Search process: I googled variations such as "Kurmuk SAF control Blue Nile May 2026," "Sudan Blue Nile campaign Kurmuk June 2026," "Kurmuk Sudan army '31 May' OR '1 June' 2026," and "sudanwarmonitor.com Kurmuk SAF outskirts pincer." I then queried the most relevant detailed sources exhaustively.

Key evidence:
- The Wikipedia "2026 Blue Nile campaign" article (last updated June 1, 2026) explicitly describes Kurmuk as an "opposition controlled town" as of May 28, 2026, noting the SAF was only "closing in" on it. The SAF had recaptured surrounding areas (Al-Barka on May 24, four areas in Geissan locality on May 26) but there is no report of the SAF entering or recapturing the Kurmuk town center [2fc6be].
- Peoples Dispatch (May 28, 2026) reports the SAF is "closing in on Kurmuk" and "positioning itself on the outskirts of Kurmuk" to recapture it from the RSF/SPLM-N alliance, explicitly describing efforts to "isolate RSF positions in Kurmuk" — confirming the rebels still held the town [d0911e]. URL: https://peoplesdispatch.org/2026/05/28/sudanese-army-on-a-counter-offensive-to-recapture-the-strategic-city-on-the-ethiopian-border/
- Sudan Tribune (article 314419, "Sudan army closes in on Kurmuk after destroying last rebel strongholds") reports the army advancing on Kurmuk "from two axes — north and south — in a pincer movement aimed at encircling rebel forces inside," again confirming rebels remained inside the town. URL: https://sudantribune.com/article/314419 ; related: https://sudantribune.com/article/314335
- Al Jazeera (May 16, 2026) framed SAF gains (Khor Hassan) as "part of the army's strategy to recapture the town of Kurmuk," indicating Kurmuk was not yet retaken. URL: https://www.aljazeera.com/news/2026/5/16/sudanese-army-captures-key-town-near-ethiopian-border-from-rsf

Wikipedia URL: https://en.wikipedia.org/wiki/2026_Blue_Nile_campaign

Per the resolution criteria, YES requires both a physical SAF presence in the Kurmuk town center AND SAF being the dominant force. The latest credible reporting (including the specialist tracker Sudan War Monitor's coverage reflected in Sudan Tribune and Wikipedia) shows the SAF was still outside the town, with rebel forces inside. The criteria also stipulate resolving NO if no credible reporting confirms SAF control. Therefore the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-4. `286335f7-a12d-58b6-8a45-1e4c2caace90`

- Present date: `2026-04-30 11:35:53.832098`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will a NATO member state not already contributing to Arctic Sentry officially announce a new contribution of military assets (aircraft, ships, or troops) to the mission between April 29 and June 1, 2026?

**Resolution criteria**

This question resolves as **YES** if, on or after April 29, 2026 (00:00 UTC) and by June 1, 2026 (23:59 UTC), a NATO member state that had not previously announced a contribution of military assets to Arctic Sentry officially announces a new contribution of one or more of the following categories of military assets to the mission:

- **Aircraft** (fixed-wing or rotary-wing military aircraft)
- **Ships** (naval vessels including submarines)
- **Troops** (military personnel deployed for the mission)

As of April 29, 2026, the following states are considered existing contributors and do NOT count for resolution: Sweden, Germany, United Kingdom, Denmark, and Norway.

A contribution from any other NATO member state (see full list: https://www.nato.int/cps/en/natohq/nato_countries.htm) qualifies.

**"Official announcement"** is defined as any of the following:
1. A press release or news article published on the NATO Newsroom (https://www.nato.int/cps/en/natohq/news.htm) or SHAPE news (https://shape.nato.int/news-releases)
2. An official statement from a contributing nation's Ministry of Defence or equivalent government portal
3. A report from a major wire service (Reuters, AP, or AFP) confirming the commitment

The announcement must explicitly reference Arctic Sentry by name and specify the type of asset (aircraft, ships, or troops) being contributed.

If no such announcement is made by 23:59 UTC on June 1, 2026, the question resolves **NO**.

**Pre-cutoff background**

NATO launched the Arctic Sentry mission on February 11, 2026, to strengthen the Alliance's defense and deterrence capabilities in the Arctic and High North, overseen by JFC Norfolk. The mission was announced amid tensions over U.S. President Trump's claims regarding Greenland [NATO Arctic Sentry - Wikipedia](https://en.wikipedia.org/wiki/NATO_Arctic_Sentry).

As of April 29, 2026, the following NATO member states have announced contributions of military assets to Arctic Sentry [NATO Arctic Sentry - Wikipedia](https://en.wikipedia.org/wiki/NATO_Arctic_Sentry):
- **Sweden**: Gripen fighter jets to patrol around Greenland (aircraft)
- **Germany**: Four Eurofighter Typhoon aircraft (aircraft)
- **United Kingdom**: Doubling troop presence in Norway (troops)
- **Denmark**: Participating country (including Greenland)
- **Norway**: Host nation for exercises including Cold Response

The mission is actively seeking to fill capability gaps, and Canada has urged NATO to make Arctic Sentry permanent. Several other NATO allies (e.g., Finland, France, the Netherlands, Canada, Iceland) have Arctic interests or capabilities but have not yet announced specific asset contributions. Given the mission's expansion trajectory and ongoing NATO summits and ministerial meetings, additional contributions are plausible but not certain within the resolution window.

**Exact later resolution packet**

RESOLUTION: NO (0).

The question asks whether, between April 29 (00:00 UTC) and June 1, 2026 (23:59 UTC), a NATO member state NOT already contributing to Arctic Sentry (i.e., any state other than Sweden, Germany, UK, Denmark, Norway) officially announced — via NATO Newsroom/SHAPE, a national MoD, or Reuters/AP/AFP — a NEW contribution of aircraft, ships, or troops, explicitly referencing Arctic Sentry by name.

Evidence and reasoning:
- The canonical tracking source, the Wikipedia "NATO Arctic Sentry" article (last edited May 6, 2026, i.e. after the window opened), lists ONLY Sweden (Gripen jets, 12 Feb 2026), Germany (4 Eurofighter Typhoons, Feb 2026), UK (doubling troops in Norway, 11 Feb 2026), Denmark (participating), and Norway (host). It records no additional contributing state and no new contribution dated in late April, May, or early June 2026; its latest contribution-timeline events are all February 2026 [bb20d2][5ef617][c22272][707d16].
- The official NATO Arctic security topic page and the official SHAPE Arctic Sentry mission page contain no list of new contributing nations or any announcement of a new contribution within the window [682a95][34f786].
- The USNI News launch report (Feb 16, 2026) likewise lists only Sweden, Germany, UK, Denmark, Norway as contributors and nothing later [79c4a9].
- Other states (Finland, Netherlands, France, Canada) appear only in the context of pre-existing exercises folded under the Arctic Sentry umbrella (e.g., Cold Response 26, Dynamic Mongoose, the Dutch HNLMS Johan de Witt sailing announced earlier in 2026) — not as NEW official asset-contribution announcements made within April 29–June 1, 2026 that explicitly commit assets to Arctic Sentry by name. The Anadolu Agency piece about Estonia/Netherlands/Finland readiness and the European Interest piece both predate the window (January 2026) [d859f0][09561b].
- The only large named deployment (UK carrier strike group) is from an already-excluded contributor (UK) and was announced in February 2026 [6ac461].

No source from an official portal (NATO Newsroom, SHAPE, MoD) or a major wire service (Reuters/AP/AFP) was found announcing a qualifying NEW contribution from a non-excluded NATO state within the resolution window. Per the criteria, if no such announcement is made by 23:59 UTC June 1, 2026, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-5. `88ed1cd7-f3d5-5320-ae05-5f5aafe3cf9a`

- Present date: `2026-05-16 12:11:41.064378`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the TBMM publish a 'separate and temporary' reintegration law for PKK militants who lay down arms in the Official Gazette by July 1, 2026?

**Resolution criteria**

This question resolves **YES** if, on or after May 12, 2026 (00:00 UTC) and by July 1, 2026 (23:59 UTC), a law is published in the Official Gazette of the Republic of Turkey (Resmî Gazete, https://www.resmigazete.gov.tr/) that establishes a separate and temporary legal framework for the reintegration of PKK militants who lay down their arms, as envisioned in Articles 6 and 7 of the TBMM "Terror-Free Türkiye" commission report.

The law must contain provisions for individual assessment of militants who disarm (i.e., not a blanket amnesty). Publication in the Official Gazette constitutes passage into law.

Verification can also be cross-referenced via the TBMM legislative database at https://www.tbmm.gov.tr/develop/owa/kanunlar_sd.sorgu_baslangic.

If no such law is published in the Official Gazette by 23:59 UTC on July 1, 2026, the question resolves **NO**.

**Pre-cutoff background**

On February 18, 2026, the Grand National Assembly of Türkiye (TBMM, https://www.tbmm.gov.tr/) Commission on National Solidarity, Brotherhood and Democracy adopted the "Terror-Free Türkiye" report with 47 votes in favor, 2 against, and 1 abstention [“Terror-Free Türkiye” Report Voted On Amid Objections: Time to Act](https://yetkinreport.com/en/2026/02/19/terror-free-turkiye-report-voted-on-amid-objections-time-to-act/). The report outlines a framework for ending PKK (Kurdistan Workers' Party) armed activity, including a key legislative proposal in Articles 6 and 7 for a "separate and temporary" law to facilitate the reintegration of militants who lay down their arms through individual assessment rather than blanket amnesty [“Terror-Free Türkiye” Report Voted On Amid Objections: Time to Act](https://yetkinreport.com/en/2026/02/19/terror-free-turkiye-report-voted-on-amid-objections-time-to-act/).

As of May 13, 2026, the report has passed the commission stage but still requires multiple legislative steps before becoming law: (1) a vote in the TBMM General Assembly to formalize the report, (2) referral to the Justice Commission for drafting of the specific law, and (3) full legislative passage through committee and plenary votes [“Terror-Free Türkiye” Report Voted On Amid Objections: Time to Act](https://yetkinreport.com/en/2026/02/19/terror-free-turkiye-report-voted-on-amid-objections-time-to-act/). The process faces political controversy, with objections from opposition parties, and the compressed legislative timeline makes passage by July 1, 2026, uncertain but not impossible.

The TBMM is the unicameral parliament of Türkiye (https://en.wikipedia.org/wiki/Grand_National_Assembly_of_Turkey). The PKK is designated as a terrorist organization by Türkiye, the EU, and the US (https://en.wikipedia.org/wiki/Kurdistan_Workers%27_Party). The "separate and temporary" law refers to the proposed legislation described in Articles 6 and 7 of the commission report, which would create a time-limited legal framework for individual-level assessment and reintegration of militants who disarm, distinct from any blanket amnesty.

**Exact later resolution packet**

The question resolves NO. It asked whether a "separate and temporary" reintegration law for PKK militants (as envisioned in Articles 6 and 7 of the TBMM "Terror-Free Türkiye"/Terörsüz Türkiye commission report) would be published in the Official Gazette (Resmî Gazete) between May 12, 2026 (00:00 UTC) and July 1, 2026 (23:59 UTC). It was not.

Key evidence, all indicating the law remained in the drafting stage and was not published by the July 1, 2026 deadline:

1. Sabah, June 30, 2026 (one day before the deadline): TBMM Speaker Numan Kurtulmuş stated that legislative preparations were still ongoing and had not yet reached the commission or General Assembly stage. He expressed hope that "in a very short time, the legal preparations will be completed and it will be brought to the commissions and then to the General Assembly" — confirming the law was still being drafted, not enacted [Son dakika | Terörsüz Türkiye yasası nasıl hazırlanacak? TBMM ...](https://www.sabah.com.tr/gundem/2026/06/30/son-dakika-terorsuz-turkiye-yasasi-nasil-hazirlanacak-tbmm-baskani-numan-kurtulmustan-dikkat-ceken-mesaj). (https://www.sabah.com.tr/gundem/2026/06/30/son-dakika-terorsuz-turkiye-yasasi-nasil-hazirlanacak-tbmm-baskani-numan-kurtulmustan-dikkat-ceken-mesaj)

2. Kurdistan24, June 2, 2026: The government was "finalizing a comprehensive legislative bill," with the draft "expected to be submitted to the Turkish Parliament before the July 15 summer recess" — i.e., a target submission (not passage) after July 1 [Türkiye Prepares Legislative Framework to Formalize PKK ...](https://www.kurdistan24.net/en/story/917598/t%C3%BCrkiye-prepares-legislative-framework-to-formalize-pkk-disarmament-and-reintegration). (https://www.kurdistan24.net/en/story/917598/)

3. Additional corroborating sources found via Google (search snippets): Turkish Minute (June 25, 2026) reported AKP sources saying the proposal "could be submitted to parliament in the first half of July and passed before lawmakers go on" recess; Basnews reported the bill would be "submitted to parliament after the NATO summit on July 7-8"; and Cumhuriyet/Indyturk reported the framework law was expected to be enacted around the end of July, before the mid-July recess. All of these place submission and passage after July 1, 2026.

4. The June 22, 2026 parliamentary action (reported as "Parliament approves PKK disarmament plan") was the General Assembly's approval/formalization of the commission's report/framework document — i.e., step (1) of the legislative process described in the question — not the enactment or Official Gazette publication of the actual law [Turkish lawmakers back plan to reintegrate PKK militants, rule out ...](https://thearabweekly.com/turkish-lawmakers-back-plan-reintegrate-pkk-militants-rule-out-amnesty).

Because the actual law had not even been submitted to parliament by the July 1, 2026 deadline (submission was planned for July, after the NATO summit, with passage targeted before the July 15 recess), no such law could have been published in the Official Gazette by 23:59 UTC on July 1, 2026. Per the resolution criteria, if no such law is published by that deadline, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-6. `9b7a20e1-e3de-5c0c-bd03-993cad053b72`

- Present date: `2026-05-16 16:55:47.950385`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Leasehold and Commonhold Reform Bill receive its first reading in the UK House of Commons by June 30, 2026?

**Resolution criteria**

This question resolves **Yes** if a bill titled "Leasehold and Commonhold Reform Bill," "Commonhold and Leasehold Reform Bill," or a bill with a substantially similar title and purpose (i.e., a bill that is clearly the final version of the draft Commonhold and Leasehold Reform Bill published in January 2026, as distinct from that draft) receives its **First Reading** in the **UK House of Commons** on or after **12 May 2026** and by **23:59 UTC on 30 June 2026**. Otherwise, this question resolves **No**.

**Definitions:**

- **First Reading** refers to the formal introduction of a bill to the House of Commons, as defined in the UK Parliament glossary: https://www.parliament.uk/site-information/glossary/first-reading/. This is the first stage of a bill's passage through the Commons, at which point the bill's title is read out and it is ordered to be printed.

- The **draft Commonhold and Leasehold Reform Bill** (published January 2026) is not the same as the final bill. The draft was published for pre-legislative scrutiny and does not constitute a formal introduction to Parliament. This question concerns the introduction of the final Government bill to the House of Commons.

**Resolution source:** The primary resolution source is the UK Parliament's bill tracking website: https://bills.parliament.uk/. The bill's page on this site will record the date of its First Reading in the House of Commons. If no such bill appears on the tracker with a Commons First Reading date on or before 30 June 2026, this question resolves No.

**Pre-cutoff background**

On 27 January 2026, the UK Government published a draft Commonhold and Leasehold Reform Bill for pre-legislative scrutiny by the Housing, Communities and Local Government (HCLG) Committee. The draft bill proposed making commonhold the default tenure for new flats, capping ground rents for existing leaseholders, and abolishing forfeiture in favour of a statutory lease-enforcement scheme [King's Speech 2026: Housing, communities and local government](https://lordslibrary.parliament.uk/research-briefings/lln-2026-0018/).

As of mid-May 2026, the HCLG Committee's pre-legislative scrutiny has involved oral evidence sessions and written submissions, but the committee has not yet published its final report [https://bills.parliament.uk/](https://bills.parliament.uk/). The committee's publications page (https://committees.parliament.uk/work/9587/prelegislative-scrutiny-of-the-draft-commonhold-and-leasehold-reform-bill/publications/) tracks progress.

The King's Speech took place on 13 May 2026, marking the start of the 2026–27 parliamentary session [What might be announced in the King's Speech 2026?](https://commonslibrary.parliament.uk/research-briefings/cbp-10585/). The Leasehold and Commonhold Reform Bill was widely expected to be included in the King's Speech legislative programme, based on pre-speech reporting from the BBC and other outlets. However, inclusion in the King's Speech does not guarantee immediate first reading — the government must decide when to formally introduce the bill to the House of Commons.

Historically, some bills announced in the King's Speech receive their first reading on the same day or within days, while others — particularly those that have undergone pre-legislative scrutiny as draft bills — may take weeks or months to be formally introduced. The 2026–27 session is expected to run from May 2026 through to spring 2027. A first reading by 30 June 2026 would require the government to finalise the bill text (incorporating any changes from the scrutiny process) and introduce it within roughly six weeks of the session opening — a tight but not impossible timeline. As of the time of writing, the bill does not yet appear on the UK Parliament Bills tracker (https://bills.parliament.uk/) as a formal bill of the 2026–27 session [https://bills.parliament.uk/](https://bills.parliament.uk/).

**Exact later resolution packet**

The question resolves NO. It asked whether the Leasehold/Commonhold Reform Bill would receive its First Reading in the UK House of Commons between 12 May 2026 and 23:59 UTC on 30 June 2026.

Evidence:

1. PRIMARY RESOLUTION SOURCE — UK Parliament Bills tracker (https://bills.parliament.uk/): A review of the current 2026-27 session bill list (140 bills including "Anonymity of Suspects Bill", "Armed Forces Bill", etc.) contains NO bill titled "Leasehold and Commonhold Reform Bill" or "Commonhold and Leasehold Reform Bill" [https://bills.parliament.uk/](https://bills.parliament.uk/). A session-filtered search of the tracker likewise returned no matching formal bill with a Commons First Reading date on or before 30 June 2026 [https://bills.parliament.uk/?SearchTerm=commonhold%20leasehold&Session=2026-27](https://bills.parliament.uk/?SearchTerm=commonhold%20leasehold&Session=2026-27). The resolution criteria explicitly state: "If no such bill appears on the tracker with a Commons First Reading date on or before 30 June 2026, this question resolves No."

2. The HCLG Committee's pre-legislative scrutiny 1st Report was published on 27 May 2026 (https://committees.parliament.uk/work/9587/...), with follow-up correspondence (e.g. a letter from the Minister of State for Housing and Planning dated 8 June 2026) extending to 17 June 2026 — indicating the process was still at the draft-scrutiny stage rather than formal introduction [Pre-legislative scrutiny of the draft Commonhold and Leasehold ...](https://committees.parliament.uk/work/9587/prelegislative-scrutiny-of-the-draft-commonhold-and-leasehold-reform-bill/publications/).

3. House of Commons Library briefing CBP-10653 (dated 23 June 2026) states the government "will consider the committee's report before introducing the final version of the bill to Parliament," and that the committee recommended the government "introduce the final bill in autumn 2026" [Leasehold reform in England and Wales: What's happening and ...](https://commonslibrary.parliament.uk/research-briefings/cbp-10653/).

4. Charles Russell Speechlys legal briefing "Commonhold and Leasehold Reform Bill: Where are we now?" (8 June 2026) states: "The expectation is that an amended Commonhold and Leasehold Reform Bill will be introduced to Parliament in Autumn 2026," and notes the government must respond to the committee's 27 May 2026 report within two months [Commonhold and Leasehold Reform Bill: Where are we now?](https://www.charlesrussellspeechlys.com/en/insights/expert-insights/real-estate/2026/commonhold-and-leasehold-reform-bill-where-are-we-now/).

All sources agree: as of end of June 2026 the bill had NOT received a First Reading in the Commons; the final government bill was expected to be introduced in autumn 2026, after the government responded to the pre-legislative scrutiny report. Only the January 2026 DRAFT bill existed within the window, which the resolution criteria explicitly exclude as it "does not constitute a formal introduction to Parliament." Therefore the bill did not receive its First Reading in the specified window, and the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-7. `d3d630d3-ef28-5e29-b290-885c2a9dbcac`

- Present date: `2026-04-30 17:56:04.534551`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the IDF reduce the geographic area under its military control in Gaza between April 30 and June 1, 2026?

**Resolution criteria**

This question resolves YES if, between April 30, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC), either of the following occurs:

1. The Israeli government or IDF officially announces a withdrawal of IDF ground forces from a specific named area or sector of Gaza that was previously within the "orange line" or "Yellow Line" restricted zone as of April 30, 2026; OR

2. Credible international news agencies (specifically Reuters, AP, or AFP) report, based on verifiable evidence, that the IDF has physically vacated a specific geographic area of Gaza that was previously under its military control as of April 30, 2026, resulting in a net reduction of the restricted zone boundary.

"Withdrawal" means a physical retreat of IDF ground forces from a defined geographic area such that the area is no longer under active IDF military control (i.e., no permanent checkpoints, fixed positions, or routine patrols by IDF personnel). Minor tactical redeployments, troop rotations, or repositioning of forces within the existing restricted zone that do not result in a reduction of the overall controlled territory do not qualify.

The deployment of international forces (ISF) into an area does NOT by itself constitute IDF withdrawal unless it is accompanied by the actual departure of IDF forces from that area.

This question resolves NO if no such withdrawal or announcement occurs by June 1, 2026 (23:59 UTC).

Resolution sources: Official IDF spokesperson statements (https://www.idf.il/en/) or reporting by Reuters (https://www.reuters.com/), AP (https://apnews.com/), or AFP.

**Pre-cutoff background**

Following the October 2025 ceasefire agreement, the IDF was expected to gradually withdraw from populated areas of Gaza. However, as of April 30, 2026, no comprehensive withdrawal has taken place ['Neither war nor peace': What Gaza looks like six months into ...](https://www.aljazeera.com/news/2026/4/10/neither-war-nor-peace-what-gaza-looks-like-six-months-into-ceasefire). Instead, the IDF has expanded its zone of military control. In mid-March 2026, the Israeli military issued new maps to aid organizations introducing an "orange line" that encompasses an estimated 64% of the Gaza Strip, an expansion beyond the earlier "Yellow Line" established after the ceasefire [Israeli maps outline expanded zone of military control in Gaza](https://www.reuters.com/world/israeli-maps-outline-expanded-zone-military-control-gaza-2026-04-29/). The IDF maintains effective control over large areas including portions of Rafah, Khan Younis, and northern Gaza ['Neither war nor peace': What Gaza looks like six months into ...](https://www.aljazeera.com/news/2026/4/10/neither-war-nor-peace-what-gaza-looks-like-six-months-into-ceasefire).

Phase 2 of the Gaza peace plan calls for progressive IDF withdrawal and handover of territory to the International Stabilization Force (ISF). Reports indicate Israel is preparing to deploy an international force in Gaza starting in May 2026, potentially including approximately 5,000 troops from Indonesia and smaller contingents from other countries. However, Hamas has conditioned disarmament talks on guarantees of full Israeli withdrawal, and far-right Israeli ministers have threatened full occupation if Hamas does not disband. The contradiction between the peace plan's withdrawal requirements and Israel's ongoing military consolidation creates genuine uncertainty about whether any withdrawal will occur in the near term.

For this question, "IDF forces" refers to any active-duty Israel Defense Forces personnel (ground troops, including infantry, armor, engineering, and intelligence units) operating within the Gaza Strip. This excludes Israeli Border Police and reserve units not deployed inside Gaza. "Military control" is defined by the geographic boundaries of the restricted zones as mapped by the IDF and communicated to aid organizations — specifically, the "orange line" maps issued in March 2026 or any subsequent official IDF operational maps [Israeli maps outline expanded zone of military control in Gaza](https://www.reuters.com/world/israeli-maps-outline-expanded-zone-military-control-gaza-2026-04-29/).

**Exact later resolution packet**

The question resolves YES only if, between April 30, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC), the IDF/Israeli government officially announced a withdrawal of ground forces from a named area previously within the "orange line"/"Yellow Line" restricted zone, OR Reuters/AP/AFP reported a physical IDF vacation of an area resulting in a net reduction of the restricted zone boundary. The evidence from the period shows the opposite: Israel expanded, not reduced, its area of control.

- A Reuters report (May 28, 2026) states that PM Netanyahu directed the Israeli military to expand its control in Gaza from an estimated 64% to 70% of the territory, quoting him: "We were at fifty, we moved to sixty. My directive is to move to ... seventy." No withdrawal occurred during the window [Netanyahu directs Israeli forces to expand Gaza control ...](https://www.reuters.com/world/middle-east/netanyahu-directs-israeli-forces-expand-gaza-control-70-percent-2026-05-28/).
- A Reuters report (May 29, 2026) confirms Netanyahu declared Israel would expand its area of control from ~64% (the "orange line" zone) to an initial 70%, with Hamas calling it a "dangerous escalation." Again, ongoing expansion, not reduction [Israeli push to take more of Gaza raises alarm as Hamas ... - Reuters](https://www.reuters.com/world/middle-east/hamas-calls-netanyahus-plan-expand-control-gaza-dangerous-escalation-2026-05-29/).
- A CNN report (May 14, 2026) describes Israel "deepening its control over the enclave," with the "orange line" (~64%) remaining the operational boundary and warns of permanent division — no withdrawal or net reduction reported [Gaza risks becoming permanently divided, top official warns | CNN](https://www.cnn.com/2026/05/14/middleeast/gaza-israel-ceasefire-permanent-division-intl).

Across all credible sources within the resolution window (April 30 – June 1, 2026), there was no official announcement of an IDF withdrawal from any named area, and no Reuters/AP/AFP report of a physical IDF retreat producing a net reduction of the restricted zone boundary. On the contrary, the documented trend was expansion of military control. The deployment of any international forces (ISF) was not accompanied by an actual IDF departure that reduced the zone. Therefore neither YES condition was met, and the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-8. `6ea80da1-bcbd-5d3d-ba24-5b48c681ca16`

- Present date: `2026-05-12 18:35:55.826272`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the 2026 Venice mayoral election go to a runoff (ballottaggio)?

**Resolution criteria**

This question resolves **Yes** if no candidate receives more than 50% of valid votes cast in the first round of the 2026 Venice mayoral election (scheduled for May 24–25, 2026), thereby necessitating a runoff (ballottaggio). It resolves **No** if any candidate receives more than 50% of valid votes in the first round and is declared the winner without a runoff.

Resolution is based solely on the official first-round results as published by the Italian Ministry of Interior (Ministero dell'Interno) on its official election portal, **Eligendo** (https://elezioni.interno.gov.it/). Results are expected to be available by May 26, 2026, 23:59 CEST.

Only the official certified results of the first round (May 24–25, 2026) determine resolution. If the election is postponed or cancelled before July 1, 2026, this question resolves ambiguously (N/A).

**Pre-cutoff background**

Venice, Italy is scheduled to hold municipal elections on May 24–25, 2026, to elect a new mayor following the end of Luigi Brugnaro's two terms as mayor leading a centre-right administration [Who Will Run Venice? Centre Right Backs Venturini - Wanted in Milan](https://www.wantedinmilan.com/news/who-will-run-venice-centre-right-backs-venturini.html).

Eight candidates are running for mayor. The two main contenders are:

- **Simone Venturini** (centre-right): Currently the city councillor for Social Cohesion, Economy, and Tourism, Venturini is Brugnaro's chosen successor. His coalition includes Fratelli d'Italia, Lega, Forza Italia, UDC, Partito dei Veneti, and a personal civic list [Who Will Run Venice? Centre Right Backs Venturini - Wanted in Milan](https://www.wantedinmilan.com/news/who-will-run-venice-centre-right-backs-venturini.html).

- **Andrea Martella** (centre-left): A former Member of Parliament for the Democratic Party (PD) and former Undersecretary for Publishing. His broad "campo largo" coalition includes PD, the Five Star Movement (M5S), Alleanza Verdi e Sinistra (AVS), and several civic lists [Who Will Run Venice? Centre Right Backs Venturini - Wanted in Milan](https://www.wantedinmilan.com/news/who-will-run-venice-centre-right-backs-venturini.html).

Other notable candidates include Giovanni Andrea Martini (left-wing/environmentalist civic coalition) and Michele Boldrin (Washington University economist running as an independent civic candidate) [Who Will Run Venice? Centre Right Backs Venturini - Wanted in Milan](https://www.wantedinmilan.com/news/who-will-run-venice-centre-right-backs-venturini.html) [Venice Mayoral Election Winner - Polymarket](https://polymarket.com/uk/event/venice-mayoral-election-winner).

Under Italian municipal electoral law (for cities with more than 15,000 inhabitants), a candidate must receive more than 50% of valid votes in the first round to win outright. If no candidate exceeds this threshold, a runoff (ballottaggio) between the top two candidates is held two weeks later, scheduled for June 8, 2026.

As of May 11, 2026, prediction market Polymarket prices imply Andrea Martella at ~86% to win the overall election and Venturini at ~15% [Venice Mayoral Election Winner - Polymarket](https://polymarket.com/uk/event/venice-mayoral-election-winner). However, these odds reflect the overall winner, not the first-round outcome specifically. The fragmented field of eight candidates creates uncertainty about whether any candidate can surpass 50% in the first round, even if Martella is the clear favourite to ultimately win.

**Exact later resolution packet**

RESOLUTION: NO (0).

The question asks whether the 2026 Venice mayoral election went to a runoff (ballottaggio), which would require that NO candidate exceed 50% of valid votes in the first round. It resolves NO if any candidate exceeded 50% and won outright in the first round.

ANTECEDENT / VALIDITY CHECK: The election was held as scheduled on May 24–25, 2026, and was neither postponed nor cancelled before July 1, 2026. It proceeded normally and produced certified first-round results [c451ef, 8e3f16, 773b21]. Therefore the question is valid and not annulled.

OUTCOME: Simone Venturini (centre-right) won outright in the FIRST ROUND. Official first-round results as documented from the Italian Ministry of Interior (Eligendo) data give Venturini 56,344 votes = 51.03% of valid votes, ahead of Andrea Martella (centre-left) at 39.21%, Michele Boldrin at 3.44%, and Giovanni Andrea Martini at 2.11% [c451ef]. La Stampa's official-data mirror reports Venturini at 51.0% and Martella at 39.2% [8e3f16], and Fanpage reports Venturini winning in the first round with ~51% vs Martella ~39% [773b21]. Campaign for a Living Venice (citing Venezia Today) reports 51.02% for Venturini [e0c77a].

Because Venturini received strictly more than 50% (≈51.0%) of valid votes in the first round, he was declared mayor without a runoff. No ballottaggio was necessary. Hence the question resolves NO.

RESOLUTION SOURCE: The specific Eligendo first-round results page for the Comune di Venezia is https://elezioni.interno.gov.it/risultati/20260524/comunali/scrutini/primoturno/050870420 . That page loads its data via JavaScript and could not be scraped directly by the retrieval tool [ca3763], but its underlying certified figures are reproduced on the Italian Wikipedia article for the 2026 Veneto municipal elections (56,344 votes = 51.03%) [c451ef] and corroborated by La Stampa's official results portal [8e3f16] and Italian press [773b21, e0c77a].

NOTE ON THE ca3763 RESULT: The tool returned "-1" for the raw Eligendo URL only because the JavaScript-rendered page contained no scrapeable text [ca3763]; this is a technical access limitation, not evidence of a postponement. Every accessible source confirms Venturini's first-round majority.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-9. `47cc7236-9764-5aa9-b180-2806b827d4dd`

- Present date: `2026-05-14 09:02:55.723987`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Belgian police unions carry out at least one actual work stoppage between May 13, 2026 and June 30, 2026?

**Resolution criteria**

This question resolves **Yes** if, between May 13, 2026 00:00 UTC and June 30, 2026 23:59 UTC, at least one actual work stoppage occurs involving Belgian police officers acting under a union-organized strike or industrial action. 

A "work stoppage" is defined as a deliberate, organized cessation of normal police duties by union members lasting at least 1 hour, undertaken as a form of collective industrial action. This includes full strikes, partial strikes, or organized work-to-rule actions explicitly described as a "strike" or "grève" by the organizing union. Mere filing or extension of a strike notice, without any actual cessation of work, does not count.

The work stoppage may be organized by the CGSP (https://www.cgsp.be/), the SLFP/VSOA, CSC Services Publics, or any other recognized Belgian police union.

Resolution sources: confirmation by at least one of the following: [The Brussels Times](https://www.brusselstimes.com/), [RTBF](https://www.rtbf.be/), [VRT NWS](https://www.vrt.be/vrtnws/en/), [Strike Tracker](https://striketracker.app/strikes-in-belgium), or official union communication (e.g., on https://www.cgsp.be/). If none of these sources report any police work stoppage by June 30, 2026, the question resolves **No**.

The work stoppage must occur on or after May 13, 2026, to exclude the May 12 national strike day.

**Pre-cutoff background**

The [CGSP](https://www.cgsp.be/) (Centrale Générale des Services Publics) is Belgium's major francophone public-sector trade union. As of May 13, 2026, the CGSP Police branch has filed a 7-week strike notice covering May 12 to June 30, 2026, citing a recruitment crisis, pay grievances, and lack of concrete government responses on end-of-career arrangements [https://striketracker.app/strikes-in-belgium](https://striketracker.app/strikes-in-belgium). Under Belgian labor law, a [strike notice](https://en.wikipedia.org/wiki/Strike_action) is a legal prerequisite that establishes the right to strike but does not itself constitute industrial action.

Belgium has experienced significant labor unrest in 2026, including a major national strike on May 12, 2026, organized by the country's largest trade unions against government austerity measures, which drew large protests in Brussels and caused widespread transport disruption. The CGSP police strike notice is separate from and extends well beyond this one-day national action.

As of May 13, 2026, no police-specific work stoppage under the CGSP's 7-week notice has been reported beyond participation in the May 12 national strike day. Whether actual police strikes materialize depends on the outcome of ongoing negotiations between the union and the Belgian government over police pay and staffing. Belgian police unions have a history of both escalating to action and settling through negotiation, making the outcome genuinely uncertain.

Resolution will be tracked via Belgian news outlets and the [Strike Tracker](https://striketracker.app/strikes-in-belgium) database.

**Exact later resolution packet**

The question resolves NO: no approved source reports an actual police work stoppage (a deliberate cessation of police duties lasting ≥1 hour) between May 13, 2026 and June 30, 2026.

Evidence, from the specified resolution sources:

1) CGSP Police 7-week notice (May 12–June 30, 2026): This was only a strike NOTICE ("préavis de grève"), not an action. Strike Tracker's own tracking entry documents the filing of the CGSP police strike notice but records NO actual work stoppage under it during the window [ad71c6][2d0082]. Multiple outlets (RTBF, Le Soir, 7sur7) only ever report the filing of the notice, never an actual stoppage.

2) Liège Federal Judicial Police notice (June 22–26, 2026): Unions (CSC SP, CGSP, SNPS, SLFP Police) filed a strike notice on June 9, 2026 (RTBF), but RTBF then reported on June 12, 2026 that this notice was SUSPENDED after commitments from Minister Vanessa Matz's cabinet regarding infrastructure at the Saint-Léonard site — so the June 22–26 action did not materialize [de877a]. Strike Tracker's dedicated page also describes it as a "préavis de grève specifying a window; concrete stoppage days may be confirmed closer to 22 June," with no confirmation any stoppage occurred [84abb6].

3) Other actual strikes that DID occur in the window were in non-police sectors (education/teachers June 4; Wallonia civil servants June 16; Brussels public services / CGSP Admi June 22–23; prison staff June 29; skeyes air-traffic control June 2; maritime pilots June 5) — none are police work stoppages. Police appeared in the news only as a deployed force at protests and as the subject of "police violence" demonstrations, not as strikers [2d0082].

4) The May 12 national strike (in which CGSP Police participated) is explicitly excluded by the resolution criteria.

Because Strike Tracker, RTBF, VRT NWS and The Brussels Times collectively report only strike NOTICES for police (with the Liège one suspended) and no actual police cessation of work during May 13–June 30, 2026, the criteria's default applies: the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-10. `4402e54f-60b1-59e6-a3de-d596b5319933`

- Present date: `2026-05-02 18:54:21.102290`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

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

**Pre-cutoff background**

China and the United States have been engaged in an escalating cycle of trade restrictions involving semiconductors and critical minerals. Key developments include:

**China's export control timeline:**
- In December 2024, China banned exports of gallium, germanium, antimony, and superhard materials to the US.
- On April 4, 2025, China's Ministry of Commerce (MOFCOM) introduced export restrictions on seven medium and heavy rare earth elements in retaliation for President Trump's tariffs [China's New Rare Earth and Magnet Restrictions Threaten ... - CSIS](https://www.csis.org/analysis/chinas-new-rare-earth-and-magnet-restrictions-threaten-us-defense-supply-chains).
- On October 9, 2025, China announced its strictest rare earth and permanent magnet export controls to date ("Announcement No. 61 of 2025"), applying a foreign direct product rule (FDPR) to foreign-produced magnets and semiconductor materials containing at least 0.1% heavy rare earth elements sourced from China, effective December 1, 2025 [China's New Rare Earth and Magnet Restrictions Threaten ... - CSIS](https://www.csis.org/analysis/chinas-new-rare-earth-and-magnet-restrictions-threaten-us-defense-supply-chains).
- On November 9, 2025, as part of a trade truce, China suspended its ban on dual-use exports of gallium, germanium, antimony, and superhard materials to the US until November 27, 2026. However, exports to US military end-users remain prohibited, and licensing requirements still apply.

**US actions:** The US has continued tightening semiconductor export controls targeting China, and the MATCH Act (aimed at multilateralizing chip equipment export controls) has been advancing in Congress. The US has also been building a critical minerals trading bloc to counter China's dominance.

**Current status as of May 1, 2026:** The suspension of the gallium/germanium/antimony dual-use export ban to the US remains in effect until November 27, 2026, subject to licensing. The rare earth export controls from April and October 2025 (including the FDPR-style magnet controls) remain active. China retains the ability to reimpose or expand controls at any time.

**Exact later resolution packet**

The question requires that, strictly between May 1, 2026 00:00 UTC and June 1, 2026 23:59 UTC, China officially announce NEW or expanded export controls on a critical mineral (on the IEA list) via an official MOFCOM notice (mofcom.gov.cn) or government gazette, explicitly linked to US semiconductor export control actions.

I examined the official MOFCOM 2026 announcements index (https://www.mofcom.gov.cn/zcfb/blgg/gg/2026/index.html). The only MOFCOM announcements published in the May 1–June 1, 2026 window were:
- 2026-05-02: Announcement No. 21 of 2026 — a blocking order against US sanctions on five Chinese enterprises related to Iranian oil (a sanctions blocking statute, NOT an export control on critical minerals) [a79ee9, af8530].
- 2026-05-22: A joint announcement by five departments adjusting the catalog of drug-precursor chemicals subject to export control to specific countries/regions (precursor chemicals, NOT IEA critical minerals or semiconductor materials) [a79ee9, af8530].

No announcement dated between May 23 and June 1, 2026 appears on the list [af8530].

Therefore, no MOFCOM announcement in the window imposed new/expanded export controls on any IEA critical mineral. Although the US tightened semiconductor controls in late May 2026 (e.g., the Commerce Department's May 31, 2026 step to halt Nvidia AI chip shipments to Chinese firms abroad, per Reuters https://www.reuters.com/world/china/us-takes-step-halt-nvidia-ai-chip-shipments-chinese-firms-outside-china-2026-05-31/), China did not respond with any new critical-mineral export control announcement during the window. China's existing rare-earth/critical-mineral export regime (from April and October 2025) remained largely unchanged following the 14–15 May 2026 Trump-Xi summit, per Benchmark Source reporting, and there was no new qualifying MOFCOM announcement.

Criterion 1 (new/expanded controls on a critical mineral) is not satisfied; thus criteria 2 and 3 are moot. The question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-11. `e1798612-8370-5d8c-9f6f-0053f800090d`

- Present date: `2026-05-03 03:54:41.779631`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the US and China sign a formal trade agreement during the Trump-Xi summit in Beijing in May 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 1, 2026, and by 11:59 PM UTC on May 31, 2026, the United States and China sign or officially announce a formal trade agreement in connection with the Trump-Xi summit.

**Definition of "formal trade agreement":** A formal trade agreement is defined as a written document — such as a trade deal, trade pact, memorandum of understanding on trade, or agreement explicitly labeled as a "phase" deal — that is signed by officials at or above the cabinet/ministerial level (e.g., the U.S. Trade Representative or Treasury Secretary, and a Chinese Vice Premier or Minister of Commerce, or higher) and that contains specific, binding commitments regarding tariffs, market access, trade volumes, or other trade-related obligations between the two countries. A joint communiqué, joint statement of intent, or verbal agreement without a signed document does not qualify.

**Resolution source:** The signing or official announcement must be confirmed by at least one of the following sources:
- The White House official statements page (https://www.whitehouse.gov/briefing-room/statements-releases/)
- The Chinese Ministry of Commerce newsroom (http://english.mofcom.gov.cn/)
- Major wire services (Reuters, AP, Bloomberg)

If no such formal trade agreement is signed and publicly announced by 11:59 PM UTC on May 31, 2026, this question resolves **No**.

**Pre-cutoff background**

U.S. President Donald Trump is scheduled to visit Beijing in mid-May 2026 for a summit with Chinese President Xi Jinping — his first visit to China in eight years. The trip was originally planned earlier but was delayed due to the Iran war [https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/](https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/). Preparatory talks were held in Paris involving U.S. Treasury Secretary Scott Bessent and Trade Representative Jamieson Greer on the American side, and Chinese Vice Premier He Lifeng and top trade negotiator Li Chenggang on the Chinese side. Both sides described these Paris preparatory talks as "constructive" [https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/](https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/). The summit is expected to focus on managed trade deals, particularly regarding agriculture [https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/](https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/).

As of early 2026, US-China trade relations remain volatile, characterized by tit-for-tat tariffs, export controls on critical minerals and software, and various trade truces and disputes throughout 2025 and early 2026 [https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/](https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/). A call between Chinese and U.S. economic chiefs ahead of the summit was described as "candid," suggesting unresolved tensions remain [https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/](https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/). Whether the summit produces a formal signed agreement — as opposed to a joint statement of principles or verbal commitments — is genuinely uncertain, given the complexity of outstanding issues including tariffs, market access, technology controls, and agricultural purchases.

**Exact later resolution packet**

The question resolves NO. The Trump-Xi summit did occur in Beijing on May 14-15, 2026, so the resolution window and context conditions were met, but no "formal trade agreement" as strictly defined by the resolution criteria (a written document signed by cabinet/ministerial-level officials containing specific binding commitments, explicitly excluding joint statements of intent or verbal agreements) was signed or officially announced.

Key evidence from mandated sources:

1. Reuters (May 16, 2026) reported that China's Commerce Ministry explicitly described the tariff, agricultural, and aircraft deals agreed during the visit as "preliminary," that discussions on details were continuing, and that agreements would be "finalised as soon as possible." The ministry "did not identify companies or provide details on volumes, values or timelines" [China says Trump visit deals are 'preliminary' | Reuters](https://www.reuters.com/world/china/china-says-trump-visit-deals-are-preliminary-2026-05-16/) [China says Trump visit deals are 'preliminary' | Reuters](https://www.reuters.com/world/china/china-says-trump-visit-deals-are-preliminary-2026-05-16/). A separate Reuters piece confirmed the agreements were "preliminary" and needed to be finalized [China signals tariff cuts, advances in farm market access after Trump ...](https://www.reuters.com/world/china/china-signals-tariff-cuts-advances-farm-market-access-after-trump-xi-summit-2026-05-16/).

2. Reuters (May 14-16) reported Trump "left China with no major breakthroughs on trade," with "scant details," and that the two sides merely agreed to establish a "Board of Trade" and "Board of Investment" rather than signing a formal trade agreement. No signing ceremony for a formal agreement was reported [Trump leaves Beijing with few wins but warm words for Xi | Reuters](https://www.reuters.com/world/china/trump-xi-set-second-day-talks-after-taiwan-warning-2026-05-14/) [Trump returns from China with stability and a stalemate | Reuters](https://www.reuters.com/world/china/trump-returns-china-with-stability-stalemate-2026-05-16/).

3. The two governments issued separate, conflicting readouts and did not produce a single mutually signed document. China did not confirm the U.S. claims (e.g., the 200 Boeing jets, the $17 billion agriculture purchase), and "neither side confirmed the other's claims"; "the Chinese statements make no reference to any specific business or trade agreements" [Trump-Xi summit: China, US disagree on what they agreed on](https://www.aljazeera.com/news/2026/5/15/trump-xi-summit-china-us-disagree-on-what-they-agreed-on). NPR (May 22, 2026) confirmed the U.S. and China issued separate readouts with inconsistencies and "stuck to their own interpretations," with no single mutually signed formal document [The aftermath of Trump-Xi summit: comparing U.S. and China ... - NPR](https://www.npr.org/2026/05/22/g-s1-123647/comparing-u-s-and-china-announcements).

4. The White House Fact Sheet (May 17, 2026) framed the outcome as a "consensus" and a "package of commitments" and the chartering of two new institutions (Board of Trade, Board of Investment), but described announcements/commitments rather than a signed bilateral written agreement [Fact Sheet: President Donald J. Trump Secures Historic Deals with ...](https://www.whitehouse.gov/fact-sheets/2026/05/fact-sheet-president-donald-j-trump-secures-historic-deals-with-china-delivering-for-american-workers-farmers-and-industry/). CNN (May 18) noted "Beijing's readout did not directly confirm those deals" and that announcements were "short on specifics" and Beijing called results "preliminary" [From a 'board of trade' to Boeing planes, what did Xi and Trump ...](https://www.cnn.com/2026/05/18/china/xi-trump-trade-agreements-china-visit-intl-hnk). The BBC (May 15) reported "neither side has announced trade breakthroughs or significant business deals" and "no confirmation of any deals or purchases from the Chinese" [Trump and Xi conclude 'very successful' talks but few deals confirmed](https://www.bbc.com/news/articles/clypj01189lo). China Briefing (May 21) confirmed there was no single formal signed trade agreement document and "no extension of the tariff truce," and MOFCOM "stopped short of confirming" the $17 billion commitment [The Xi-Trump Summit: What Was Agreed—and What Was Not](https://www.china-briefing.com/news/xi-trump-beijing-summit-what-was-agreed/).

Because the mandated sources show only preliminary, separately-announced, and disputed commitments — not a written document signed by cabinet/ministerial-level officials of both countries with specific binding obligations — the criteria for a "formal trade agreement" were not satisfied by the May 31, 2026 deadline. The question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-12. `6265737e-5024-5011-9af0-711be49976f8`

- Present date: `2026-05-02 20:25:04.436632`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will a federal court issue a new injunction blocking any provision of a Trump executive order related to elections between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between 00:00 UTC on May 1, 2026, and 23:59 UTC on June 1, 2026, any U.S. federal court issues a new injunction that blocks, stays, or halts the enforcement of any provision of a Trump executive order related to elections.

**Definitions:**

- **Federal court:** Any United States District Court, United States Court of Appeals (Circuit Court), or the Supreme Court of the United States, as defined at https://en.wikipedia.org/wiki/Federal_judiciary_of_the_United_States.

- **Injunction:** A court order requiring a party to do or refrain from doing a specific act. This includes Temporary Restraining Orders (TROs), Preliminary Injunctions, and Permanent Injunctions, as defined at https://www.law.cornell.edu/wex/injunction.

- **Executive order related to elections:** Specifically, Executive Order 14248 (signed March 2025, "Preserving and Protecting the Integrity of American Elections") and Executive Order 14339 (signed March 2026, "Ensuring Citizenship Verification and Integrity in Federal Elections"), or any subsequent executive order issued by President Trump that directly regulates, restricts, or modifies the administration or conduct of federal elections.

- **New injunction:** An injunction order entered on the court docket on or after May 1, 2026 (00:00 UTC). Extensions or modifications of previously issued injunctions count only if the court explicitly expands the scope of the injunction to cover provisions not previously blocked. Mere denials of motions to dissolve existing injunctions do not count.

**Resolution source:** Federal court docket entries accessible via [PACER](https://pacer.uscourts.gov/), or credible reporting from [Democracy Docket](https://www.democracydocket.com/), [Brennan Center](https://www.brennancenter.org/), [Reuters](https://www.reuters.com/), [AP News](https://apnews.com/), or [Law360](https://www.law360.com/).

This question resolves **No** if no such new injunction is issued within the specified timeframe.

**Pre-cutoff background**

As of May 1, 2026, the Trump administration has issued two major executive orders targeting federal election administration:

1. **Executive Order 14248 (March 2025):** This order attempted to assert presidential control over federal elections, including provisions requiring documentary proof of citizenship for voter registration (Section 2(a)), directing DHS/DOGE review of voter files (Section 2(b)), imposing citizenship assessments at registration agencies (Section 2(d)), requiring proof of citizenship for military/overseas voters (Section 3(d)), threatening to withhold EAC funding (Sections 4(a)-(b)), and banning states from counting mail-in ballots received after Election Day (Sections 7(a)-(b)) [Status of Trump's Anti-Voting Executive Order](https://www.brennancenter.org/our-work/research-reports/status-trumps-anti-voting-executive-order).

2. **Executive Order 14339 (March 2026):** This order attempts to require the U.S. Postal Service to decide who is allowed to vote by mail and to refuse to deliver ballots cast by anyone not on newly created lists of approved mail voters [Status of Trump's Anti-Voting Executive Order](https://www.brennancenter.org/our-work/research-reports/status-trumps-anti-voting-executive-order).

Multiple federal courts have already issued injunctions against various provisions of these orders. As of April 23, 2026, Section 2(a) has been blocked by three federal courts; Sections 2(d) and 3(d) are subject to both permanent and preliminary injunctions; Sections 4(a)-(b) have been blocked as applied to certain states; and Sections 7(a)-(b) have been blocked in 15 states [Status of Trump's Anti-Voting Executive Order](https://www.brennancenter.org/our-work/research-reports/status-trumps-anti-voting-executive-order). A permanent injunction was issued on January 9, 2026, by District Judge John H. Chun blocking core provisions of the March 2025 order [Federal court blocks key parts of Trump's anti-voting order, restores ...](https://www.democracydocket.com/news-alerts/federal-court-blocks-key-parts-of-trumps-anti-voting-order-restores-states-control-over-elections/). The March 2026 order is subject to new legal challenges filed by the Brennan Center and other groups [Status of Trump's Anti-Voting Executive Order](https://www.brennancenter.org/our-work/research-reports/status-trumps-anti-voting-executive-order).

Active litigation continues across multiple jurisdictions, with cases pending before several U.S. District Courts. Given the pace of litigation, the number of pending cases, and the new March 2026 executive order generating fresh lawsuits, there is genuine but not certain probability that another injunction will be issued in the May 1–June 1, 2026 window.

**Exact later resolution packet**

The question resolves NO. No U.S. federal court issued a new injunction blocking any provision of a Trump election-related executive order (EO 14248, EO 14339, or another such order) during the window of May 1, 2026 (00:00 UTC) to June 1, 2026 (23:59 UTC).

Key findings:

1. The major activity in the window concerned the challenges to EO 14339 (the March 31, 2026 mail-in voting executive order). In the consolidated cases (including the DSCC challenge and the LULAC/Campaign Legal Center challenge), the court held a preliminary-injunction hearing on May 14, 2026, and on May 28, 2026, U.S. District Judge Carl Nichols DENIED the motions for a preliminary injunction, ruling that the challenge was premature because the agencies/Postal Service had not yet implemented the order and plaintiffs had not suffered harm [US judge won't block Trump's mail-in voting executive order for now](https://www.reuters.com/legal/government/judge-allows-trump-implement-mail-in-voting-executive-order-2026-05-28/)[Judge denies attempt to stop Trump's mail voting order](https://www.democracydocket.com/news-alerts/judge-denies-attempt-to-stop-trumps-mail-voting-order/)[Trump Mail-In Voting Executive Order Challenge (DSCC)](https://www.democracydocket.com/cases/trump-mail-in-voting-executive-order-challenge-dscc/)[Defending Vote by Mail from the Trump Administration's ...](https://campaignlegal.org/cases-actions/defending-vote-mail-trump-administrations-unconstitutional-executive-overreach-lulac). A denial of an injunction does not satisfy the YES criteria. Democrats appealed this denial on June 1, 2026, but an appeal of a denial is not itself an injunction [Democrats appeal ruling that left Trump's anti-mail voting order in ...](https://www.democracydocket.com/news-alerts/democrats-appeal-ruling-that-left-trumps-anti-mail-voting-order-in-place/).

2. The pre-existing injunctions against EO 14248 (the March 2025 order) were all entered BEFORE the resolution window: the ACLU/LWV permanent injunction on the "show your papers" proof-of-citizenship requirement was issued October 31, 2025 [Court Strikes Down Key Part of Trump's Unlawful Voting Executive ...](https://www.aclu.org/press-releases/court-strikes-down-key-part-of-trumps-unlawful-voting-executive-order-permanently-blocking-show-your-papers-requirement); the Elias Law Group / Kollar-Kotelly permanent injunction on Sections 2(d) and 3(d) was issued January 30, 2026 [Federal Court Permanently Blocks Additional Provisions of ...](https://elias.law/press-release/federal-court-permanently-blocks-additional-provisions-of-president-trumps-executive-order-on-elections/); and Judge Chun's permanent injunction was January 9, 2026 (per question description). The Brennan Center tracker, last updated April 23, 2026, lists no injunction within the May 1–June 1 window [Status of Trump's Anti-Voting Executive Order](https://www.brennancenter.org/our-work/research-reports/status-trumps-anti-voting-executive-order). None of these fall within the May 1–June 1, 2026 window, and no expansion of scope to new provisions occurred in that window.

3. No reporting from Democracy Docket, Brennan Center, Reuters, AP, or Law360 indicated any new injunction granted between May 1 and June 1, 2026; the consistent reporting in that window was that judges DECLINED to block the order (Reuters, Democracy Docket, Roll Call, Washington Post, all dated May 28, 2026).

Therefore, no qualifying new injunction was issued in the window, and the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-13. `65802f66-e893-52c9-a10a-8fd12374a93b`

- Present date: `2026-05-14 11:35:08.076542`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Carles Puigdemont physically enter Spain between May 12, 2026, and July 1, 2026?

**Resolution criteria**

This question resolves YES if Carles Puigdemont (born December 29, 1962; https://en.wikipedia.org/wiki/Carles_Puigdemont) is confirmed to have been physically present within the sovereign territory of the Kingdom of Spain — including all autonomous communities, autonomous cities (Ceuta and Melilla), and island territories — at any point on or after May 12, 2026, 00:00 UTC and on or before July 1, 2026, 23:59 UTC.

"Return to Spain" is defined as any confirmed physical presence within Spain's sovereign territory, regardless of duration, manner of entry, or whether the entry was public, clandestine, voluntary, or resulted in arrest. A brief entry (as occurred in August 2024) counts, as does an entry resulting in immediate detention.

The question resolves NO if no such confirmed physical presence occurs within the specified timeframe.

Resolution will be based on reporting from at least two major, reputable news sources — such as Reuters (https://www.reuters.com), Associated Press (https://apnews.com), AFP, BBC (https://www.bbc.com), El País (https://elpais.com), or La Vanguardia (https://www.lavanguardia.com) — or an official announcement by the Spanish judiciary or government confirming Puigdemont's physical presence in Spain. A mere unverified claim of presence without corroboration from such sources is not sufficient for YES resolution.

**Pre-cutoff background**

Carles Puigdemont, the former President of the Generalitat of Catalonia, has been living in exile since fleeing Spain in October 2017 following the failed Catalan independence referendum. He briefly returned to Barcelona on August 8, 2024, delivered a public speech, and evaded arrest before returning to exile.

As of May 12, 2026, a national arrest warrant issued by the Spanish Supreme Court remains active against Puigdemont. On January 27, 2026, the Spanish Constitutional Court unanimously rejected a request by Puigdemont, Toni Comín, and Lluís Puig to lift their arrest warrants as a precautionary measure, ruling that doing so would constitute a "premature resolution" of the underlying case [The Constitutional Court takes a stand against Puigdemont](https://en.ara.cat/politics/the-constitutional-court-takes-stand-against-puigdemont-it-maintains-the-arrest-warrant-while-considering-amnesty_1_5630109.html) [TC rejects lifting Puigdemont arrest warrant Amnesty Law](https://diaricatalunya.cat/en/garrotxa/general/constitutional-court-unanimously-rejects-lifting-puigdemonts-arrest-warrant). The Constitutional Court is still considering the merits of Puigdemont's appeal regarding the application of Spain's 2024 amnesty law to his case. A ruling from the Court of Justice of the European Union (CJEU) on the amnesty law is also pending [The Constitutional Court takes a stand against Puigdemont](https://en.ara.cat/politics/the-constitutional-court-takes-stand-against-puigdemont-it-maintains-the-arrest-warrant-while-considering-amnesty_1_5630109.html).

Reports from April 2026 suggest that logistics for a potential return have been planned for months, but the timing remains contingent on favorable legal developments — specifically a ruling from the Constitutional Court on the amnesty's applicability or a CJEU decision [The operation of Puigdemont's return, with the government of 1-O ...](https://en.ara.cat/politics/the-operation-of-puigdemont-s-return-with-the-government-of-1-and-tarradellas-temperament_1_5712019.html). Some sources have suggested a return could be possible in mid-2026, but significant uncertainty remains regarding whether the legal situation will be resolved in time and whether Puigdemont would risk returning while the arrest warrant is still active.

**Exact later resolution packet**

The question asks whether Carles Puigdemont was physically present within Spanish sovereign territory at any point between May 12, 2026, 00:00 UTC and July 1, 2026, 23:59 UTC. The answer is NO — he was not.

Key evidence (all from within or just after the resolution window):

1. El Periódico, "Puigdemont y su camino de regreso" (June 13, 2026): As of this date Puigdemont had still not returned to Spain. He "still has not managed to have the arrest warrant in Spain withdrawn" and "risks being arrested if he crosses the border." His potential return is explicitly contingent on FUTURE legal events: a Court of Justice of the EU (TJUE/CJEU) ruling on the amnesty law expected July 16, 2026, followed by a Spanish Constitutional Court (TC) ruling expected September/October 2026 [090bb1]. (https://www.elperiodico.com/es/politica/20260613/puigdemont-regreso-cataluna-amnistia-tjue-tc-supremo-127242580)

2. Agencia EFE (June 27, 2026): As of June 27, 2026 — just four days before the window closed — Puigdemont "remains in exile and has not returned to Spain." The Spanish Constitutional Court maintains an active national arrest warrant against him and will not rule on his amnesty appeal until September or October 2026, as it awaits the CJEU ruling scheduled for July 16, 2026 [990465]. (https://efe.com/espana/2026-06-27/el-constitucional-resolvera-en-septiembre-u-octubre-sobre-la-amnistia-a-puigdemont/)

3. Corroborating context from multiple reputable outlets (El País, El Mundo, Infobae, La Vanguardia, El Periódico, EFE) consistently confirms: (a) the CJEU amnesty ruling was scheduled for July 16, 2026 — AFTER the window closed; (b) the Constitutional Court's decision on Puigdemont's amparo appeal is expected September/October 2026; (c) the national arrest warrant remained active throughout the window; and (d) Puigdemont was physically in Waterloo, Belgium, during June 2026 (e.g., El País coverage of the PP/Feijóo declining to travel to Waterloo to meet him).

No reputable source (Reuters, AP, AFP, BBC, El País, La Vanguardia, EFE, etc.) reported any physical presence of Puigdemont on Spanish territory during May 12 – July 1, 2026. His only prior brief return was on August 8, 2024. All 2026 reporting frames a return as a future, conditional event tied to legal rulings that had not yet occurred by July 1, 2026. Therefore the required condition for YES (confirmed physical presence in Spain within the window, corroborated by at least two reputable sources or an official judiciary/government announcement) was not met.

Resolution: NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-14. `488722fe-1ce5-5cac-8b87-ff4cd8fba0b8`

- Present date: `2026-05-14 00:54:15.067915`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-17T00:00:00`

**Question**

Will the Riksbank's June 2026 Monetary Policy Report revise its 2026 CPIF inflation forecast upward compared to the March 2026 report?

**Resolution criteria**

This question resolves **Yes** if the 2026 annual average CPIF inflation forecast published in the Riksbank's June 2026 Monetary Policy Report is strictly greater than 1.5% (the March 2026 baseline). Any increase, no matter how small (e.g., 1.6% vs 1.5%), constitutes an upward revision. It resolves **No** if the forecast is equal to or lower than 1.5%, or if the report is not published by July 1, 2026.

Key definitions:
- **CPIF** (Consumer Price Index with a Fixed interest rate): The CPI excluding effects of changes in mortgage interest rates, as defined by the Riksbank (https://www.riksbank.se/en-gb/monetary-policy/).
- The comparison is based on the **annual average** inflation forecast for the full calendar year 2026, as reported in the forecast tables of each respective report.
- The March 2026 baseline value of 1.5% is taken from Table 4 ("Inflation") of the Monetary Policy Report March 2026 [https://www.riksbank.se/globalassets/media/rapporter/ppr/penningpolitiska-rapporter-och-uppdateringar/engelska/2026/monetary-policy-report-march-2026.pdf](https://www.riksbank.se/globalassets/media/rapporter/ppr/penningpolitiska-rapporter-och-uppdateringar/engelska/2026/monetary-policy-report-march-2026.pdf).

Resolution source: The June 2026 Monetary Policy Report, expected to be published on June 17, 2026, at approximately 09:30 local Swedish time (07:30 UTC). It will be available at: https://www.riksbank.se/en-gb/monetary-policy/monetary-policy-report/

**Pre-cutoff background**

The Riksbank publishes Monetary Policy Reports several times per year containing forecasts for inflation and economic activity. In the March 2026 Monetary Policy Report (published March 19, 2026), the Riksbank forecast annual average CPIF inflation of 1.5% for 2026 [https://www.riksbank.se/globalassets/media/rapporter/ppr/penningpolitiska-rapporter-och-uppdateringar/engelska/2026/monetary-policy-report-march-2026.pdf](https://www.riksbank.se/globalassets/media/rapporter/ppr/penningpolitiska-rapporter-och-uppdateringar/engelska/2026/monetary-policy-report-march-2026.pdf). CPIF (Consumer Price Index with a Fixed interest rate) is the Riksbank's target measure of inflation, defined as the CPI excluding the effects of changes in mortgage interest rates (https://www.riksbank.se/en-gb/monetary-policy/).

In its May 2026 monetary policy decision, the Riksbank noted that "the risk of higher inflation has increased somewhat" [https://www.riksbank.se/en-gb/monetary-policy/monetary-policy-report/2026/monetary-policy-decision-may-2026/](https://www.riksbank.se/en-gb/monetary-policy/monetary-policy-report/2026/monetary-policy-decision-may-2026/), citing higher energy prices and global uncertainty from the Middle East conflict. The war is expected to push up CPIF inflation through higher energy prices that may also pass through to other prices [https://www.riksbank.se/globalassets/media/rapporter/ppr/penningpolitiska-rapporter-och-uppdateringar/engelska/2026/monetary-policy-report-march-2026.pdf](https://www.riksbank.se/globalassets/media/rapporter/ppr/penningpolitiska-rapporter-och-uppdateringar/engelska/2026/monetary-policy-report-march-2026.pdf).

The March 2026 Monetary Policy Report is available at: https://www.riksbank.se/globalassets/media/rapporter/ppr/penningpolitiska-rapporter-och-uppdateringar/engelska/2026/monetary-policy-report-march-2026.pdf

The next full Monetary Policy Report with updated forecasts is scheduled for publication on June 17, 2026 [https://www.riksbank.se/en-gb/monetary-policy/monetary-policy-report/2026/monetary-policy-decision-may-2026/](https://www.riksbank.se/en-gb/monetary-policy/monetary-policy-report/2026/monetary-policy-decision-may-2026/). The baseline March 2026 CPIF forecast for 2026 is 1.5% (annual average) [https://www.riksbank.se/globalassets/media/rapporter/ppr/penningpolitiska-rapporter-och-uppdateringar/engelska/2026/monetary-policy-report-march-2026.pdf](https://www.riksbank.se/globalassets/media/rapporter/ppr/penningpolitiska-rapporter-och-uppdateringar/engelska/2026/monetary-policy-report-march-2026.pdf).

**Exact later resolution packet**

The question resolves NO (0).

Antecedent/precondition check: The question resolves NO if the June 2026 Monetary Policy Report is not published by July 1, 2026, and otherwise on whether the 2026 annual-average CPIF forecast strictly exceeds 1.5%. The June 2026 Monetary Policy Report WAS published on time — on June 17, 2026 — as confirmed by the Riksbank's monetary policy report page [c77ff2] and the June 2026 monetary policy decision page [5d8b6a]. So the report-timeliness condition for NO is not triggered, and resolution turns on the forecast value.

Key finding — the forecast was revised DOWNWARD, not upward:
- The June 2026 Monetary Policy Report forecasts an annual average CPIF inflation of 1.1% for calendar year 2026, found in Table 5 ("Inflation"). This is confirmed by both the official English-language PDF [7defea, b42a93] and the official Swedish-language PDF ("Tabell 5. Inflation") [b84b75].
- Both PDFs explicitly show the previous (March 2026) forecast in brackets as 1.5%, and the new June figure of 1.1% is a downward revision [b42a93, b84b75].
- Table 5 also shows CPIF annual averages of 2.6% for 2025 and 1.7% for 2027 in the June report [b84b75, b42a93].

Since the June 2026 forecast for 2026 CPIF (1.1%) is NOT strictly greater than the 1.5% March baseline, the YES condition ("strictly greater than 1.5%") is not met. The question resolves NO.

Note on a minor discrepancy: One query of the June 2026 decision landing page returned 1.4% [5d8b6a], but this less-detailed page does not contain the full forecast table. The two authoritative full-report PDFs (English and Swedish) both clearly report 1.1% from Table 5 [b42a93, b84b75, 7defea]. Critically, every figure encountered (1.1% or even the outlier 1.4%) is below 1.5%, so the NO resolution is robust regardless of which value is exact.

Direct URL to the official June 2026 Monetary Policy Report (English PDF): https://www.riksbank.se/globalassets/media/rapporter/ppr/penningpolitiska-rapporter-och-uppdateringar/engelska/2026/monetary-policy-report-june-2026.pdf
Swedish version: https://www.riksbank.se/globalassets/media/rapporter/ppr/penningpolitiska-rapporter-och-uppdateringar/svenska/2026/penningpolitisk-rapport-juni-2026.pdf
The 2026 CPIF annual-average figure is located in Table 5 ("Inflation"), which is the inflation forecast table of the June 2026 report (Table 4 in this report is the policy rate forecast, not inflation) [7defea, b42a93].

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-15. `0a5a5a39-e2e8-5361-bf66-e7868c1f293e`

- Present date: `2026-04-30 14:53:09.084908`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Anthropic publicly disclose at least one zero-day vulnerability found by Claude Mythos Preview (by replacing a SHA-3 hash commitment with a full vulnerability report) by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after April 30, 2026 and by 23:59 UTC on June 1, 2026, at least one of the 13 SHA-3 hash commitments listed in the Appendix of the Anthropic blog post at https://red.anthropic.com/2026/mythos-preview/ has been replaced with a full vulnerability report. A "full vulnerability report" is defined as any of the following: (a) a technical write-up published directly on the page in place of the hash, (b) a hyperlink to a CVE entry in the National Vulnerability Database (https://nvd.nist.gov/), (c) a hyperlink to a vendor or third-party security advisory (e.g., a GitHub Security Advisory, a Chrome/Firefox/Windows security bulletin), or (d) a hyperlink to any other publicly accessible document that describes the vulnerability in technical detail (e.g., affected software, attack vector, impact). The replacement must appear on the page at https://red.anthropic.com/2026/mythos-preview/ or on an official Anthropic page directly linked from that Appendix section. The question resolves **No** if all 13 SHA-3 hash commitments remain unreplaced as of 23:59 UTC on June 1, 2026.

**Pre-cutoff background**

On April 7, 2026, Anthropic published a blog post titled "Assessing Claude Mythos Preview's cybersecurity capabilities" at https://red.anthropic.com/2026/mythos-preview/, detailing how their Claude Mythos Preview model discovered numerous zero-day vulnerabilities in major operating systems and browsers [https://red.anthropic.com/2026/mythos-preview/](https://red.anthropic.com/2026/mythos-preview/). The post's Appendix contains 13 SHA-3 hash commitments, each corresponding to a specific vulnerability that Anthropic has reported to affected vendors but cannot yet publicly disclose [https://red.anthropic.com/2026/mythos-preview/](https://red.anthropic.com/2026/mythos-preview/). Anthropic stated they will replace these hash commitments with links to full vulnerability reports once the responsible disclosure process for each vulnerability is complete, which typically follows a 90-day-plus-45-day timeline after initial reporting [https://red.anthropic.com/2026/mythos-preview/](https://red.anthropic.com/2026/mythos-preview/). As of April 30, 2026, all 13 hash commitments remain in place, with none yet replaced by full vulnerability reports. One CVE (CVE-2026-4747) and one GitHub security advisory (GHSA-v782-6fq4-q827) are referenced elsewhere on the page, suggesting at least some disclosure processes are underway [https://red.anthropic.com/2026/mythos-preview/](https://red.anthropic.com/2026/mythos-preview/). The tight timeline—announced April 7, with resolution by June 1—means only vulnerabilities with unusually fast vendor response and patching cycles would be disclosed in time.

**Exact later resolution packet**

The question resolves NO. It required that, by 23:59 UTC on June 1, 2026, at least one of the 13 SHA-3 hash commitments in the Appendix of the Anthropic blog post (https://red.anthropic.com/2026/mythos-preview/) be replaced with a "full vulnerability report" (a technical write-up, a CVE link, a vendor/third-party security advisory link, or any other public document describing the vulnerability in technical detail).

Evidence:
- The live page as queried still lists all 13 entries in the Appendix as raw SHA-3 hash strings (e.g., PoC: 5d314cca0ecf6b07547c85363c950fb6a3435ffae41af017a6f9e9f3, Report: 4fa6abd24d24a0e2afda47f29244720fee33025be48f48de946e3d27), none replaced with a vulnerability report. Although CVE-2026-4747 and GHSA-v782-6fq4-q827 are referenced elsewhere in the body text, the Appendix hash commitments themselves were NOT replaced [ffa92f].
- Critically, to confirm the state at the deadline, I examined the Wayback Machine snapshot dated May 31, 2026 (https://web.archive.org/web/20260531/https://red.anthropic.com/2026/mythos-preview/) — the latest archived capture before the June 1, 2026 23:59 UTC deadline (no June 1 or June 2 snapshots exist in the archive). This May 31 capture shows that all 13 Appendix entries remain as raw SHA-3 hash strings, with none replaced by a CVE link, technical write-up, security advisory, or any other vulnerability report [8a9e77].

Since all 13 hash commitments remained unreplaced through the closest snapshot to the deadline, the YES condition was not met, and the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-16. `2058d309-9cef-5fa3-b643-a1fce9f8ed92`

- Present date: `2026-05-14 05:53:04.688887`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the bill to split the Attorney General role advance from committee to the Knesset plenum with three separate positions (rather than two) by July 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after May 12, 2026 (00:00 IST, UTC+3), the Constitution, Law and Justice Committee advances to the Knesset plenum a version of the "Splitting the Post of the Attorney General" bill that explicitly creates three separate positions, defined as: (1) Attorney General / Legal Adviser to the government, (2) Prosecutor General / Head of the state prosecution, and (3) Representative of the state in legal proceedings (or functionally equivalent roles fulfilling these three distinct functions).

This question resolves NO if:
- The committee advances a version creating only two separate positions (e.g., only a Legal Adviser and a Director of Public Prosecutions, without a third distinct role); OR
- No version of the bill is advanced from committee to the plenum by July 1, 2026 (23:59 IST, UTC+3).

The primary bill to track is P/5808/25 ("Splitting the Post of the Attorney General Bill, 2025"), viewable at: https://main.knesset.gov.il/Activity/Legislation/Laws/pages/lawbill.aspx?t=lawsuggestionssearch&lawitemid=2226845

Resolution is determined by the official bill text as approved by the committee and recorded on the Knesset legislation database (https://main.knesset.gov.il/Activity/Legislation/Laws/pages/lawbill.aspx?t=lawsuggestionssearch&lawitemid=2226845) or committee records at https://main.knesset.gov.il/en/apps/committees/2215/sessions. "Three separate positions" means three distinct statutory officeholders with separate appointment processes, as opposed to "two separate positions" which would mean only two distinct officeholders replacing the current single Attorney General role.

**Pre-cutoff background**

The Israeli government has been advancing legislation to split the role of the Attorney General into separate positions. The government-backed version (Bill P/5808/25, "Splitting the Post of the Attorney General Bill, 2025"), sponsored by MKs Simcha Rothman, Ohad Tal, and Michal Woldiger, proposes splitting the role into three separate positions: (1) Attorney General (legal adviser to the government), (2) Prosecutor General (head of the state prosecution), and (3) Representative of the state in legal proceedings [Knesset Plenum approves in preliminary reading bill to split the post ...](https://m.knesset.gov.il/en/news/pressreleases/pages/press291025b.aspx). The bill passed a preliminary reading in the Knesset plenum on October 29, 2025 [Knesset Plenum approves in preliminary reading bill to split the post ...](https://m.knesset.gov.il/en/news/pressreleases/pages/press291025b.aspx) and was referred to the Constitution, Law and Justice Committee for preparation for its first reading.

However, competing versions of the bill exist. A 2008 draft memorandum that forms the basis of some committee discussions proposes only a two-way split: a Director of Public Prosecutions and a Legal Adviser [Explainer: The Proposals to “Split” the Role of the Attorney General](https://en.idi.org.il/articles/62285). Additional private member bills also exist (P/5289/25 from 2024, P/3825/25 from 2023), all currently in committee preparation for first reading.

As of May 13, 2026 (IST), the primary bill (P/5808/25) proposes three roles and has status "preparation for first reading" in the Constitution, Law and Justice Committee. The committee, chaired by MK Rothman, has been actively debating the bills, but the final structure—whether two or three positions—remains subject to intra-coalition negotiations. The IDI has noted that committee deliberations are incorporating "far-reaching changes" beyond the original proposals [Explainer: The Proposals to “Split” the Role of the Attorney General](https://en.idi.org.il/articles/62285).

**Exact later resolution packet**

The question resolves NO. Within the resolution window (on/after May 12, 2026 and before July 1, 2026), the Constitution, Law and Justice Committee (chaired by MK Simcha Rothman) DID advance a "Splitting the Post of the Attorney General" bill to the Knesset plenum — but the version advanced creates only TWO separate positions, not three, which is explicitly the NO condition.

Timeline and antecedent (advancement to plenum) confirmed:
- The committee approved the bill for its first reading on ~May 19, 2026, and re-approved it ("votes anew to approve for first reading") on May 25, 2026 [31a34d]. 
- The bill then passed its FIRST READING in the Knesset plenum by a vote of 65–47 on June 2, 2026 [f28e6c, 203401]. So the "advance from committee to plenum" antecedent did occur inside the window (after May 12 and before July 1, 2026).

Number of positions = TWO (not three), which triggers the explicit NO condition:
- The official Knesset Constitution Committee news page (committees/2215/news/27259) states: "The bill is designed to split the powers of the Attorney General into two separate posts: The Attorney General, who will be responsible for legal counsel to the Government, representation of the state in court on non-criminal affairs... and the Prosecutor General." Crucially, the "representation of the state" function is folded INTO the Attorney General role, not made a distinct third officeholder [2f10e2]. This exact wording is independently confirmed by a Google answer-box quoting the same Knesset page.
- Times of Israel (June 2, 2026): the bill "would split the attorney general's role into two separate positions... an attorney general... and a prosecutor general" [f28e6c].
- Jerusalem Post (June 2, 2026): the bill proposes "splitting the duties and powers currently held by the attorney-general between two separate officeholders: an attorney-general and a prosecutor-general" [203401].
- JNS: "dividing the role in two: 1) a legal counselor... 2) a public prosecutor" [373bb9].
- The Israel Democracy Institute explainer states the committee's working framework "included splitting the role into two separate officeholders (thereby abandoning an alternative model previously proposed and discussed, which envisaged splitting the role among three separate officeholders)" [343531].
- Committee chair Rothman himself stated no third position was created, and the approved measure was retitled the "Attorney General and Prosecutor General Bill" — a two-officeholder framing [31a34d].

Because the advanced/approved version defines only two distinct statutory officeholders with separate appointment processes (Attorney General and Prosecutor General), with the state-representation function assigned to the Attorney General rather than to a distinct third officeholder, the resolution criteria's NO condition ("The committee advances a version creating only two separate positions... without a third distinct role") is satisfied.

Key URLs: Knesset committee page https://main.knesset.gov.il/en/apps/committees/2215/news/27259 [2f10e2]; Knesset press release https://main.knesset.gov.il/EN/News/PressReleases/Pages/press25526w.aspx [31a34d]; bill page https://main.knesset.gov.il/activity/legislation/laws/pages/lawbill.aspx?t=lawsuggestionssearch&lawitemid=2226845 [e826b8].

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-17. `f8cd60e3-28bc-599c-a50b-0388e95f0057`

- Present date: `2026-05-01 09:41:58.181025`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-05-11 00:00:00`

**Question**

Will Russia and Ukraine both formally agree to observe a Victory Day ceasefire (May 8–10, 2026)?

**Resolution criteria**

This question resolves as **Yes** if, by 23:59 Moscow time (UTC+3) on May 10, 2026, both the Russian Federation and Ukraine have issued official, public statements on or after April 30, 2026, confirming their agreement to observe a ceasefire for the May 8–10, 2026 period. Specifically:

- **"Agreement"** means an explicit, official public statement from each government (e.g., from the Kremlin at [kremlin.ru](http://kremlin.ru) or the Office of the President of Ukraine at [president.gov.ua](https://www.president.gov.ua)) or from authorized government spokespeople, confirming that their armed forces will halt offensive military operations during the May 8–10 period. A unilateral declaration by one side alone does not count — both sides must formally agree.

- **"Observing the ceasefire"** refers to the formal agreement to do so, not the actual absence of kinetic activity during the period. Even if violations occur after the agreement, the question still resolves Yes if both sides formally agreed beforehand.

- The May 8–10 period is defined as 00:00 Moscow time (UTC+3) on May 8, 2026 through 23:59 Moscow time (UTC+3) on May 10, 2026, consistent with the Kremlin's stated timeframe.

This question resolves as **No** if either side explicitly rejects the proposal, if Ukraine fails to issue a formal agreement to observe the ceasefire by the deadline, or if the ceasefire is only declared unilaterally by Russia without a corresponding formal agreement from Ukraine.

**Resolution sources:** Official statements from [kremlin.ru](http://en.kremlin.ru) and [president.gov.ua](https://www.president.gov.ua/en/), supplemented by credible international news reporting from Reuters ([reuters.com](https://www.reuters.com)), BBC ([bbc.com](https://www.bbc.com)), or the Kyiv Independent ([kyivindependent.com](https://kyivindependent.com)).

**Pre-cutoff background**

On April 29, 2026, Russian President Vladimir Putin proposed a ceasefire in Ukraine for the duration of Victory Day celebrations during a phone call with U.S. President Donald Trump. Trump reportedly "actively supported" the initiative [Moscow, April 29, 2026 (AFP) - Putin offers Victory Day ceasefire in ...](https://www.nampa.org/text/22919087)[Putin Offers Victory Day Ceasefire in Ukraine on May 9, Kremlin ...](https://www.themoscowtimes.com/2026/04/29/putin-offers-victory-day-ceasefire-in-ukraine-on-may-9-kremlin-aide-says-a92641). The Kremlin stated that the 72-hour ceasefire would run from the start of May 8 to the end of May 10, 2026 (Moscow time).

As of April 30, 2026, Ukraine has not agreed to the proposal. Kremlin spokesperson Dmitry Peskov stated that Putin would declare the truce unilaterally and does not need a response from Kyiv [Ukraine proposes long-term ceasefire after Putin floats 'Victory Day ...](https://kyivindependent.com/ukraine-proposes-long-term-ceasefire-after-putin-floats-victory-day-truce/). In response, Ukrainian President Volodymyr Zelensky proposed a "long-term ceasefire" rather than a short-term truce, and instructed Ukrainian negotiators to seek clarification on the Russian proposal [Ukraine proposes long-term ceasefire after Putin floats 'Victory Day ...](https://kyivindependent.com/ukraine-proposes-long-term-ceasefire-after-putin-floats-victory-day-truce/).

This follows the precedent of the Orthodox Easter truce earlier in 2025, which both sides formally agreed to but which saw over 400 reported violations according to Ukraine [Ukraine proposes long-term ceasefire after Putin floats 'Victory Day ...](https://kyivindependent.com/ukraine-proposes-long-term-ceasefire-after-putin-floats-victory-day-truce/). The Easter truce experience creates significant uncertainty about whether Ukraine will agree to another short-term ceasefire, particularly one timed to coincide with Russia's Victory Day — a holiday with no equivalent significance for Ukraine.

**Exact later resolution packet**

Resolution: NO. The criteria required official public statements from both governments, on or after 2026-04-30 and by 23:59 Moscow time on 2026-05-10, agreeing to halt offensive/kinetic military operations for the entire May 8–10, 2026 period. The official Kremlin statement I found after the question date was the May 8 statement by Presidential Aide Yury Ushakov; it described the “key agreement” as a ceasefire period “from May 9 to May 11 inclusive,” not May 8–10 [Comment by Presidential Aide Yury Ushakov on a ceasefire ...](http://en.kremlin.ru/events/president/news/79702). Reuters likewise reported that the confirmed agreement between Russia and Ukraine was for a three-day ceasefire running May 9–11, with a suspension of all “kinetic activity,” and separately noted that Russia’s earlier May 8–9 unilateral ceasefire was not mutually accepted by Ukraine [Trump hopes for extension to agreed three-day Ukraine- ...](https://www.reuters.com/world/europe/russia-ukraine-accuse-each-other-violating-ceasefire-2026-05-08/). The earlier Kremlin page from April 29/30 only stated Russia’s readiness to declare a Victory Day ceasefire and did not evidence Ukraine’s agreement [http://en.kremlin.ru/events/president/news/79660](http://en.kremlin.ru/events/president/news/79660). Therefore, although there was evidence of a later mutual ceasefire arrangement, it was for May 9–11 rather than the specified May 8–10 window; the specified May 8–10 proposal remained unilateral/not formally agreed by both sides. This is not annulled because the question is not an IF/THEN conditional under Metaculus conditional-pair semantics; it is a direct binary question about whether the specified mutual agreement occurred.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-18. `c7af6cd2-33ce-5896-b390-ca06202a7129`

- Present date: `2026-05-03 02:19:05.781780`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will a formal command-and-control (C2) structure for the UK-France-led multinational Strait of Hormuz naval mission be publicly announced between May 1, 2026 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 1, 2026, and no later than 23:59 UTC on June 1, 2026, a **public announcement** is made confirming the establishment of a formal command-and-control (C2) structure for the UK-France-led multinational Strait of Hormuz naval mission.

**"Public announcement"** means an official statement, press release, or briefing published by at least one of the following authoritative sources:
- [UK Ministry of Defence](https://www.gov.uk/government/organisations/ministry-of-defence) (via gov.uk)
- [French Ministry of the Armed Forces](https://www.defense.gouv.fr/) (via defense.gouv.fr)
- A joint coalition statement from participating nations

Alternatively, credible reporting by major international news agencies such as [Reuters](https://www.reuters.com/), [Associated Press](https://apnews.com/), [BBC](https://www.bbc.com/news), or [Agence France-Presse](https://www.afp.com/) confirming such an announcement also qualifies.

**"Formal command-and-control (C2) structure"** means the announcement must confirm at least one of the following:
1. A designated **lead nation** or group of nations with operational command authority over the mission;
2. A **named operation** (e.g., "Operation [Name]") with an identified command framework;
3. A specific **headquarters location** from which the mission will be commanded; OR
4. The appointment of a named **operational commander** for the mission.

Mere continuation of planning discussions, expressions of intent, or references to ongoing negotiations do **not** qualify. The announcement must indicate that a C2 structure has been **decided upon and established**, not merely proposed or under consideration.

The announcement must occur on or after May 1, 2026 to exclude outcomes from the April 22–23, 2026 planning conference itself.

**Pre-cutoff background**

Since February 28, 2026, shipping traffic through the [Strait of Hormuz](https://en.wikipedia.org/wiki/Strait_of_Hormuz)—a critical maritime chokepoint for global energy trade—has been largely blocked by Iran [2026 Strait of Hormuz crisis - Wikipedia](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis). In response, the United Kingdom and France have taken the lead in organizing a multinational naval coalition to reopen the strait and protect commercial shipping.

On April 17, 2026, more than a dozen countries expressed willingness to join an international mission to protect shipping in the Strait of Hormuz. On April 22–23, 2026, the UK hosted a military planning conference at the UK's [Permanent Joint Headquarters](https://en.wikipedia.org/wiki/Permanent_Joint_Headquarters) in Northwood, North London, attended by military planners from over 30 nations [https://www.gov.uk/government/news/uk-and-france-to-lead-multinational-strait-of-hormuz-military-planning-conference](https://www.gov.uk/government/news/uk-and-france-to-lead-multinational-strait-of-hormuz-military-planning-conference). The conference focused on translating diplomatic consensus from a prior Paris summit (attended by 51 countries) into a concrete military plan, with discussions covering military capabilities, command and control (C2), and deployment logistics [https://www.gov.uk/government/news/uk-and-france-to-lead-multinational-strait-of-hormuz-military-planning-conference](https://www.gov.uk/government/news/uk-and-france-to-lead-multinational-strait-of-hormuz-military-planning-conference).

As of May 1, 2026, the mission remains in the planning phase. No formal C2 structure has been publicly announced. The mission is described as "independent and strictly defensive," intended to protect merchant vessels, reassure commercial shipping operators, and conduct mine clearance operations. Its activation is contingent upon a "sustainable ceasefire agreement" [https://www.gov.uk/government/news/uk-and-france-to-lead-multinational-strait-of-hormuz-military-planning-conference](https://www.gov.uk/government/news/uk-and-france-to-lead-multinational-strait-of-hormuz-military-planning-conference). Whether a formal C2 structure can be established and announced within approximately five weeks of the planning conference is uncertain—military coalitions often take months to formalize, but the urgency of the Hormuz crisis could accelerate the process.

**Exact later resolution packet**

The question resolves NO. It requires a public announcement, between May 1 and June 1, 2026, from one of the specified authoritative sources (UK MoD, French MoD, joint coalition statement, Reuters/AP/BBC/AFP) confirming that a formal C2 structure for the UK-France-led multinational Strait of Hormuz mission had been "decided upon and established" — specifically naming at least one of: a lead nation with operational command authority, a named operation, a specific headquarters location, or a named operational commander.

Key evidence:

1. The most significant development in the window was the 12 May 2026 joint statement published on gov.uk ("Joint statement on the Multinational Military Mission for the Strait of Hormuz"). Its full text only announces "political support" from 38 nations for "an independent and strictly defensive multinational military mission," and explicitly states operations "will only commence in a permissive environment" and that "there will be necessary national caveats and parliamentary procedures." It names no operation, no headquarters, no operational commander, and designates no lead nation with operational command authority — it is a political-support declaration, not an established C2 structure [3bfff2, a4d7f4].

2. The accompanying 11 May 2026 UK MoD release framed the upcoming ministerial meeting as advancing the mission and turning "diplomatic agreement into practical military plans," i.e. still planning, with no named operation, headquarters, or commander [49fb00].

3. The BBC report (12 May 2026) covered the UK pledging jets, drones and a warship, but announced no named operation, headquarters, or commander [52c82a].

4. NATO's top commander stated on 19 May 2026 (Reuters) that NATO was "not drawing up any plans for a potential mission" and that it would require a political decision — confirming no established command framework via NATO.

5. A French l'Opinion article (11–12 May 2026) noted only that the arrangement "could be operational at the end of May" and "could" include a multinational command embarked on the Charles de Gaulle — conditional/planning language, not an established, announced C2 structure [91265a].

6. Breaking Defense (15 May 2026) described the effort as the "Multinational Military Mission," a descriptive label rather than a formal named operation, with no designated operational commander, headquarters, or operational command authority, and noted the mission would "only begin once a ceasefire has been declared" [ab4707].

7. The Wikipedia articles on the 2026 Strait of Hormuz crisis and campaign (updated late May 2026) contain no reference to an established UK-France-led C2 structure, named operation, commander, or headquarters in the resolution window; the only named operation referenced is the separate US "Operation Project Freedom" [a2128e, 4d4c09, 12e801].

Throughout the entire window the mission remained in the planning / political-support phase, contingent on a sustainable ceasefire. No authoritative source confirmed a formal C2 structure had been "decided upon and established." Therefore the question resolves NO.

Sources:
- https://www.gov.uk/government/news/joint-statement-on-the-multinational-military-mission-for-the-strait-of-hormuz-12-may-2026
- https://www.gov.uk/government/news/uk-and-france-set-to-host-multinational-strait-of-hormuz-meeting-as-british-warship-to-pre-position-in-the-region
- https://www.bbc.com/news/articles/c5y909grldqo
- https://www.reuters.com/world/middle-east/potential-nato-mission-strait-hormuz-is-political-decision-top-commander-says-2026-05-19/
- https://www.lopinion.fr/international/detroit-dormuz-les-dessous-de-la-mission-du-charles-de-gaulle
- https://breakingdefense.com/2026/05/from-destroyers-to-drones-how-a-europe-led-coalition-aims-to-open-the-strait-of-hormuz/
- https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-19. `ca85ca1e-7405-5af3-8e40-656a508b9a40`

- Present date: `2026-05-01 10:53:41.493486`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-05-24 00:00:00`

**Question**

Will Ryusuke Hamaguchi's 'All of a Sudden' win the Palme d'Or at the 2026 Cannes Film Festival?

**Resolution criteria**

This question resolves **Yes** if Ryusuke Hamaguchi's film *All of a Sudden* is officially announced as the winner of the Palme d'Or at the 2026 Cannes Film Festival. The announcement must occur on or after April 30, 2026 (CEST, UTC+2).

A shared (ex-aequo) Palme d'Or also counts as a **Yes** resolution, provided *All of a Sudden* is one of the co-winners.

This question resolves **No** if any other film(s) win the Palme d'Or without *All of a Sudden* being included, or if the 2026 Cannes Film Festival is cancelled or the Palme d'Or is not awarded.

**Primary resolution source:** The official [Cannes Film Festival website](https://www.festival-cannes.com/en/) awards/palmares page. Secondary sources include credible entertainment industry outlets such as [Variety](https://variety.com/), [The Hollywood Reporter](https://www.hollywoodreporter.com/), [Screen Daily](https://www.screendaily.com/), or [Deadline](https://deadline.com/).

**Pre-cutoff background**

The [79th Cannes Film Festival](https://en.wikipedia.org/wiki/2026_Cannes_Film_Festival) is scheduled to take place from May 12 to May 23, 2026 (CEST, UTC+2) in Cannes, France [https://en.wikipedia.org/wiki/2026_Cannes_Film_Festival](https://en.wikipedia.org/wiki/2026_Cannes_Film_Festival). The closing ceremony and award announcements are expected on May 23, 2026.

South Korean filmmaker [Park Chan-wook](https://en.wikipedia.org/wiki/Park_Chan-wook) presides over the main competition jury [https://en.wikipedia.org/wiki/2026_Cannes_Film_Festival](https://en.wikipedia.org/wiki/2026_Cannes_Film_Festival). A total of 22 films have been selected for the main competition for the [Palme d'Or](https://en.wikipedia.org/wiki/Palme_d%27Or), the festival's highest prize.

Japanese director [Ryusuke Hamaguchi](https://en.wikipedia.org/wiki/Ryusuke_Hamaguchi) has a strong track record at Cannes: his film *Drive My Car* won the [Best Screenplay award at the 2021 Cannes Film Festival](https://en.wikipedia.org/wiki/2021_Cannes_Film_Festival), and *Evil Does Not Exist* won the Grand Jury Prize at the 2024 Venice Film Festival. Hamaguchi's new film *All of a Sudden* (original titles: *Soudain* / 急に具合が悪くなる) is among the 22 films competing for the Palme d'Or at the 2026 edition [https://en.wikipedia.org/wiki/2026_Cannes_Film_Festival](https://en.wikipedia.org/wiki/2026_Cannes_Film_Festival). Early buzz has positioned Hamaguchi as one of the frontrunners, though with 22 competitors and the inherent unpredictability of jury deliberations, the outcome remains highly uncertain. Base rates suggest any individual film in a 22-film competition has roughly a 5–10% chance of winning, though frontrunner status may push this to 10–20%.

**Exact later resolution packet**

The official Festival de Cannes winners' list for the 79th Festival de Cannes was published/announced on 2026-05-23, which is after the question's required date of 2026-04-30 [The 79th Festival de Cannes winners' list](https://www.festival-cannes.com/en/press/press-releases/the-79th-festival-de-cannes-winners-list/). On that official page (https://www.festival-cannes.com/en/press/press-releases/the-79th-festival-de-cannes-winners-list/), the Palme d'Or is listed as awarded to FJORD by Cristian Mungiu, with no shared/ex-aequo Palme d'Or co-winner indicated [The 79th Festival de Cannes winners' list](https://www.festival-cannes.com/en/press/press-releases/the-79th-festival-de-cannes-winners-list/). Ryusuke Hamaguchi's All of a Sudden is identified under its French title SOUDAIN on the same official winners' list, but it is not listed as the Palme d'Or winner or co-winner; it is listed only for Best Performance for an Actress, awarded to Virginie Efira and Tao Okamoto [The 79th Festival de Cannes winners' list](https://www.festival-cannes.com/en/press/press-releases/the-79th-festival-de-cannes-winners-list/). Therefore, under the stated criteria, another film won the Palme d'Or without All of a Sudden being included, so the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-20. `1d1d4a2b-b89a-5008-85e4-4fd4c53176c0`

- Present date: `2026-05-15 22:33:51.101412`
- Source cutoff boundary: `2026-05-16` (encodes end of UTC day `2026-05-15`)
- Expected resolution: `2026-07-01T00:00:00`

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

**Pre-cutoff background**

On May 7–8, 2026, China's Ministry of Foreign Affairs confirmed that a Chinese-crewed oil products tanker was attacked in the Strait of Hormuz amid the ongoing US-Israel-Iran war [China confirms attack on oil tanker in Strait of Hormuz earlier this week](https://www.reuters.com/world/china/china-confirms-attack-oil-tanker-strait-hormuz-earlier-this-week-2026-05-08/). In its initial response, the MFA expressed "deep concern about vessels affected by the ongoing conflict in the Middle East" but notably did not attribute blame to any specific party, stating the attacker was "unclear" [China confirms attack on oil tanker in Strait of Hormuz earlier this week](https://www.reuters.com/world/china/china-confirms-attack-oil-tanker-strait-hormuz-earlier-this-week-2026-05-08/).

China has maintained an official posture of "neutrality" throughout the 2026 Iran war, which began on February 28, 2026 [China in the 2026 Iran war](https://en.wikipedia.org/wiki/China_in_the_2026_Iran_war). While China has previously used critical language toward the US and Israel — Foreign Minister Wang Yi said the war "should never have happened" and China "condemned" the initial US-Israeli strikes on Iran in early March 2026 [China in the 2026 Iran war](https://en.wikipedia.org/wiki/China_in_the_2026_Iran_war) — Beijing has generally avoided direct, high-level attributions of blame for specific incidents affecting Chinese interests.

China imports more than 80% of Iran's shipped oil and has significant economic interests in maintaining stability in the Strait of Hormuz [China in the 2026 Iran war](https://en.wikipedia.org/wiki/China_in_the_2026_Iran_war). The US has imposed sanctions on Chinese refineries involved in Iranian oil trade, and China's Ministry of Commerce has ordered companies to disregard these sanctions [China in the 2026 Iran war](https://en.wikipedia.org/wiki/China_in_the_2026_Iran_war). There are also US intelligence allegations of China providing indirect support to Iran through dual-use technologies and intelligence [China in the 2026 Iran war](https://en.wikipedia.org/wiki/China_in_the_2026_Iran_war).

The tanker attack represents a direct threat to Chinese commercial interests. Whether Beijing will formally attribute blame to the US or Israel — a significant diplomatic escalation beyond general criticism of the war — remains uncertain as of May 13, 2026.

**Exact later resolution packet**

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

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-21. `dc811e76-fe74-53b5-90ec-b2c88c20dc67`

- Present date: `2026-04-29 23:48:16.272849`
- Source cutoff boundary: `2026-04-30` (encodes end of UTC day `2026-04-29`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Google officially announce a product or OS called 'Aluminium OS' (or 'Aluminum OS') by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after the question's open date and on or before June 1, 2026, 23:59 UTC, Google makes an **official announcement** of a product or operating system using the name 'Aluminium OS' or 'Aluminum OS.'

**Definition of 'Aluminium OS' / 'Aluminum OS':** The announced product must use one of these exact names (with either British or American spelling) as its primary consumer-facing product name or as an explicitly stated official name. An internal codename (e.g., 'Project Aluminium') revealed in passing or leaked does not count unless Google explicitly adopts 'Aluminium OS' or 'Aluminum OS' as the product's name in the announcement. Minor variations such as 'Aluminium' without 'OS,' or a completely different name (e.g., 'Pixel OS,' 'Google Desktop OS'), do **not** qualify.

**Definition of 'official announcement':** Any of the following counts:
1. A mention by name during a Google keynote or developer session (e.g., at Google I/O 2026);
2. A post on the official Google Blog (https://blog.google/) or the Google Developers Blog (https://developers.googleblog.com/);
3. A formal press release distributed via Google's official press channels.

The announcement must come from a Google-owned channel. Third-party reporting alone does not suffice, though it may be used to locate the official source.

**Source of truth:** The Google I/O 2026 landing page (https://io.google/), the official Google Blog (https://blog.google/), and/or archived keynote recordings on Google's official YouTube channel (https://www.youtube.com/@Google). If the announcement occurs outside of I/O, any official Google-owned channel as defined above is acceptable.

If Google announces the merged ChromeOS/Android platform under a name other than 'Aluminium OS' or 'Aluminum OS,' this question resolves **No**.

**Pre-cutoff background**

As of April 28, 2026 (UTC), 'Aluminium OS' (also spelled 'Aluminum OS') refers to a rumored Google project aimed at merging ChromeOS and Android into a unified desktop/laptop operating system. The name originates from references found in the Chromium Gerrit (Google's open-source code review system) under the project codename 'Project Aluminium,' and has been widely adopted by tech media [Google executive basically confirms 'Aluminium OS' is launching this ...](https://chromeunboxed.com/google-executive-basically-confirms-aluminium-os-is-launching-this-fall/). Google has not yet used the name 'Aluminium OS' in any official consumer-facing announcement.

However, at MWC 2026 (March 2026), Google's President of the Android Ecosystem, Sameer Samat, confirmed in an interview with Android Authority that a new premium consumer platform blending Android and ChromeOS is on track for a 2026 debut [Google talks Aluminium OS: Release plans, continuity, AI, and what ...](https://www.androidauthority.com/google-aluminium-os-sameer-samat-interview-3646400/). He described it as a 'premium consumer offering' with deep phone integration and AI features [Google executive basically confirms 'Aluminium OS' is launching this ...](https://chromeunboxed.com/google-executive-basically-confirms-aluminium-os-is-launching-this-fall/). Despite this, Samat did not explicitly use the name 'Aluminium OS,' leaving open the possibility that the final product will ship under a different brand.

Google I/O 2026 is scheduled for May 19–20, 2026, at Shoreline Amphitheatre in Mountain View, California, with the keynote beginning at 10:00 AM PT (17:00 UTC) on May 19. Multiple tech outlets (TechRadar, CNET, PCMag, Android Central) list an Aluminium OS announcement as a plausible but uncertain highlight of the event. The key uncertainty is whether Google will (a) announce the OS publicly at I/O under the 'Aluminium OS' or 'Aluminum OS' name, (b) announce it under a completely different consumer brand, or (c) delay any formal announcement beyond June 1, 2026.

**Exact later resolution packet**

The question resolves NO. Google did NOT make an official announcement of a product or OS using the name 'Aluminium OS' or 'Aluminum OS' on or before June 1, 2026, 23:59 UTC.

Key evidence:
- At the Android Show / Google I/O 2026 (mid-May 2026), Google officially announced its ChromeOS successor as the "Googlebook" line of laptops, with an official Google Blog post titled "Meet Googlebook" (blog.google/products-and-platforms/platforms/android/meet-googlebook/). The official announcement did NOT use the name 'Aluminium OS' or 'Aluminum OS' [https://www.theverge.com/tech/928479/google-googlebook-laptops-android-tease-aluminium-chromebook](https://www.theverge.com/tech/928479/google-googlebook-laptops-android-tease-aluminium-chromebook).
- Google explicitly disavowed 'Aluminium' as the consumer product name. A Google global communications team member (Peter Du) told The Verge on May 12, 2026: "We can confirm it is not Aluminium — that is the codename, not the official branding." Google said the final OS branding would be shared later in the year [https://www.theverge.com/tech/928479/google-googlebook-laptops-android-tease-aluminium-chromebook](https://www.theverge.com/tech/928479/google-googlebook-laptops-android-tease-aluminium-chromebook).
- The official Google Blog recap "100 things we announced at I/O 2026" (blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/) contains no mention of any product or OS named 'Aluminium OS' or 'Aluminum OS', nor a merged ChromeOS/Android OS under that name [100 things we announced at I/O 2026 - Google Blog](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/).

Per the resolution criteria, an internal codename ('Project Aluminium' / 'Aluminium') revealed or used does NOT count unless Google explicitly adopts 'Aluminium OS' or 'Aluminum OS' as the product's official name in the announcement. Google explicitly stated this is NOT the official name. Additionally, the criteria specify that if Google announces the merged platform under a different name (here, the hardware was branded "Googlebook" and the OS branding was deferred), the question resolves NO.

Sources of truth used: The Verge report on the announcement (theverge.com/tech/928479/...) confirming Google's codename clarification [https://www.theverge.com/tech/928479/google-googlebook-laptops-android-tease-aluminium-chromebook](https://www.theverge.com/tech/928479/google-googlebook-laptops-android-tease-aluminium-chromebook), and the official Google Blog I/O 2026 announcement recap [100 things we announced at I/O 2026 - Google Blog](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-22. `17f370f7-3250-5cf8-bc16-d8c931876975`

- Present date: `2026-05-02 16:10:26.865088`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will any open-weights model rank in the top 5 overall on the Artificial Analysis Intelligence Index on June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on June 1, 2026 at 11:59 PM UTC, at least one model categorized as "open weights" appears in the top 5 positions of the Artificial Analysis Intelligence Index leaderboard at the following URL:

**https://artificialanalysis.ai/leaderboards/models**

**Definitions:**
- **"Open weights" model:** As defined by Artificial Analysis: "A model whose weights have been released publicly by the model's creator" [Language Model Benchmarking Methodology - Artificial Analysis](https://artificialanalysis.ai/methodology). The model must be categorized or filterable as "open weights" (or equivalently "open source") on the Artificial Analysis leaderboard. See: https://artificialanalysis.ai/methodology
- **"Top 5":** The five models with the highest scores in the "Artificial Analysis Intelligence Index" column on the leaderboard. If multiple models are tied at the 5th-place score, all models at that score are considered to be in the top 5.
- **Ranking metric:** The "Artificial Analysis Intelligence Index" score as displayed on the leaderboard [https://artificialanalysis.ai/leaderboards/models](https://artificialanalysis.ai/leaderboards/models).

**Evaluation timing:** The leaderboard will be checked on June 1, 2026 at 11:59 PM UTC.

**Fallback protocol:** If the Artificial Analysis website (https://artificialanalysis.ai/leaderboards/models) is unreachable or the Intelligence Index leaderboard is no longer maintained on June 1, 2026, resolution will be based on the most recent archived snapshot of the page available via the Wayback Machine (https://web.archive.org/) captured on or after May 25, 2026. If no such snapshot exists from that period, the question resolves as **N/A** (ambiguous).

**Pre-cutoff background**

The Artificial Analysis Intelligence Index ranks Large Language Models (LLMs) by overall intelligence performance. As of May 1, 2026, the top 5 models on the index are all proprietary [https://artificialanalysis.ai/leaderboards/models](https://artificialanalysis.ai/leaderboards/models):

1. GPT-5.5 (xhigh) — Score: 60
2. GPT-5.5 (high) — Score: 59
3. Claude Opus 4.7 (max) — Score: 57
4. Gemini 3.1 Pro Preview — Score: 57
5. GPT-5.4 (xhigh) — Score: 57

The highest-ranked open-weights model is Kimi K2.6 with a score of 54, trailing the 5th-place model by 3 points [https://artificialanalysis.ai/leaderboards/models](https://artificialanalysis.ai/leaderboards/models). Other notable open-weights models include GLM-5 (Reasoning) at 50 and GLM-5 (Non-reasoning) at 41 [https://artificialanalysis.ai/leaderboards/models](https://artificialanalysis.ai/leaderboards/models).

The gap between the best open-weights model and the top 5 threshold has been a persistent feature of the leaderboard. However, the open-weights ecosystem has been rapidly improving, with models like Kimi K2.6 and GLM-5 closing the gap. Whether a new open-weights release (e.g., from DeepSeek, Meta, Mistral, or others) can bridge the remaining ~3-point gap within one month is the core uncertainty.

**Exact later resolution packet**

The question resolves NO.

Resolution source: The Wayback Machine snapshot of the Artificial Analysis Intelligence Index leaderboard (https://artificialanalysis.ai/leaderboards/models) captured on June 1, 2026 was retrieved [5ee67a]. According to this snapshot, the top 5 models by Artificial Analysis Intelligence Index were:
1. Claude Opus 4.8 (max) — 61
2. GPT-5.5 (xhigh) — 60
3. GPT-5.5 (high) — 59
4. Claude Opus 4.7 (max) — 57
5. Gemini 3.1 Pro Preview — 57

All five are proprietary models. The highest-ranked open-weights model was Kimi K2.6, with an Intelligence Index score of 54 — three points below the 5th-place threshold (57) [5ee67a]. There were no open-weights models tied at the 5th-place score of 57. A current Google search of the leaderboard corroborates that the top open-weights models (Kimi K2.6 at 54, MiMo-V2.5-Pro at 54, DeepSeek V4 Pro at 52) all sit at 54 or below, well outside the top 5.

Therefore, no model categorized as "open weights" appeared in the top 5 positions on June 1, 2026 at 11:59 PM UTC, and the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-23. `c0f5bb94-9b70-5dfc-a10c-cf370cd53cea`

- Present date: `2026-05-29 01:34:20.373314`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Australian government cancel or refuse at least one visa explicitly citing the new hate-conduct provisions of the Combatting Antisemitism, Hate and Extremism (Criminal and Migration Laws) Act 2026 between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after May 12, 2026, and on or before July 1, 2026 (11:59 PM AEST), the Australian government — specifically the Minister for Home Affairs, the Minister for Immigration, or the Department of Home Affairs — cancels or refuses at least one visa where the decision explicitly cites either:

(a) the Combatting Antisemitism, Hate and Extremism (Criminal and Migration Laws) Act 2026 by name, OR
(b) the specific amendments to Sections 500A or 501 of the Migration Act 1958 introduced by that Act (i.e., the new character test grounds related to hate-motivated conduct, association with prohibited hate groups, or promotion of hateful views).

The visa cancellation or refusal must occur on or after May 12, 2026.

Resolution is based on:
1. Official ministerial media releases from the Department of Home Affairs (https://minister.homeaffairs.gov.au/TonyBurke/Pages/media-releases.aspx) or the Minister for Immigration; OR
2. Credible reporting from major news outlets (e.g., ABC News at https://www.abc.net.au/news, The Guardian Australia, The Australian, Reuters, or the Sydney Morning Herald) that explicitly confirms a visa decision was made citing the new Act's provisions.

If no such publicly confirmed visa cancellation or refusal is identified by 11:59 PM AEST on July 1, 2026, the question resolves NO.

**Pre-cutoff background**

On January 20, 2026, the Australian Parliament passed the Combatting Antisemitism, Hate and Extremism (Criminal and Migration Laws) Act 2026 (Act No. 2 of 2026) [Combatting Antisemitism, Hate and Extremism (Criminal ...](https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/Bills_Search_Results/Result?bId=r7422). The Act significantly expanded the character test under Section 501 of the Migration Act 1958 and introduced new ministerial discretionary powers under Sections 500A and 501 to refuse or cancel visas on hate-related grounds [Migration Point-in-Time Service Updates - TimeBase](https://www.timebase.com.au/whats-new/2026/WN02077-whatsnew.html).

Under the new framework, a person may fail the character test if they: are or were a member of or associated with a prohibited hate group, terrorist organisation, or state sponsor of terrorism; have engaged in hate-motivated conduct even without a criminal conviction; have publicly promoted or supported hateful or racially superior views (including online) where this creates a risk of harm; or have encouraged others to spread hateful or extremist views. The risk threshold was lowered so that decision-makers need only establish a "reasonable possibility" that a person could engage in hateful or extremist activity [Combatting Antisemitism, Hate and Extremism laws reshape ...](https://absoluteimmigrationlegal.com/resources/combatting-antisemitism-hate-and-extremism-laws-reshape-australias-migration-system/).

The legislation was rushed through Parliament in response to the Bondi Beach terrorist attack [Parliament to be recalled for national security legislation](https://www.pm.gov.au/media/parliament-be-recalled-national-security-legislation). While the government has cancelled visas for hate-related conduct since the Act's passage — notably the visa of Israeli influencer Sammy Yahood in January 2026 — that cancellation was made under "existing laws" rather than explicitly citing the new Act's provisions [Australia cancels visa of Jewish influencer who previously called for ...](https://www.theguardian.com/australia-news/2026/jan/26/australia-cancels-visa-jewish-influencer-sammy-yahood-islam-banned-ntwnfb).

As of May 13, 2026, no publicly confirmed visa cancellation or refusal has been identified that explicitly cites the new provisions introduced by this Act. The question tracks whether the government will publicly exercise and acknowledge use of these specific new powers within the resolution window.

Key legislation references:
- Combatting Antisemitism, Hate and Extremism (Criminal and Migration Laws) Act 2026: https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/Bills_Search_Results/Result?bId=r7422
- Migration Act 1958, Sections 500A and 501 (as amended)

**Exact later resolution packet**

RESOLUTION: NO (0).

The question resolves YES only if, between May 12, 2026 and 11:59 PM AEST July 1, 2026, the Minister for Home Affairs, the Minister for Immigration, or the Department of Home Affairs completed a visa cancellation/refusal whose decision EXPLICITLY cited (a) the Combatting Antisemitism, Hate and Extremism (Criminal and Migration Laws) Act 2026 by name, or (b) the specific new amendments to Sections 500A/501 of the Migration Act introduced by that Act. Extensive searching of ministerial media releases and the specified major outlets (ABC, Guardian Australia, The Australian, Reuters, SMH) found no such qualifying event.

Key evidence within the resolution window (May 12 – July 1, 2026):
- May 15, 2026 — Home Affairs Minister Tony Burke's media release/press conference announced the listing of the group "White Australia" (formerly National Socialist Network) as a prohibited hate group. This is a Criminal Code listing action, NOT a visa cancellation or refusal decision, and no visa decision citing the amended migration provisions was announced ['WHITE AUSTRALIA' LISTED AS A PROHIBITED HATE GROUP ...](https://www.tonyburke.com.au/media-releases/2026/white-australia-listed-as-a-prohibited-hate-group).
- June 4, 2026 — The High Court dismissed "White Australia's" injunction attempt against its hate-group designation. This concerns the group's legal status, not an individual visa cancellation/refusal citing the new Act's migration provisions [Neo-Nazi group White Australia loses bid for temporary immunity ...](https://www.theguardian.com/australia-news/2026/jun/04/neo-nazi-group-white-australia-loses-injunction-attempt-against-hate-group-designation-ntwnfb).
- June 25, 2026 — In an ABC Radio (AM) interview, Burke discussed immigration/visa matters (e.g., a return permit for an ISIS-linked woman handled under existing frameworks and general remarks on making speaking-tour visas harder) but did NOT cite the new 2026 Act or the amended s.500A/s.501 grounds as the basis for any completed decision [ABC RADIO INTERVIEW - AM WITH MELISSA CLARKE - Tony Burke MP](https://www.tonyburke.com.au/speechestranscripts/transcript-abc-radio-interview-am-with-melissa-clarke-thursday-25-june-2026).
- June 30, 2026 — SMH reported the Executive Council of Australian Jewry was merely URGING the minister to deny a visa to comedian Bassem Youssef. This is a request/representation, not a completed decision, and no decision citing the new Act was made [Minister urged to deny visa to comedian who has accused Israel of ...](https://www.smh.com.au/politics/federal/minister-urged-to-deny-visa-to-comedian-who-has-accused-israel-of-false-flag-operation-20260630-p60b7p.html).

Supporting context:
- The Attorney-General's Department page on the Act describes the new powers but documents no specific visa cancellation/refusal citing them in the window [Combatting Antisemitism, Hate and Extremism (Criminal and ...](https://www.ag.gov.au/crime/hate-crime-offences/combatting-antisemitism-hate-and-extremism-criminal-and-migration-laws-act-2026), and a legal explainer (Go To Court) similarly describes the new character grounds without evidence of any actual use in the May–July 2026 window [New Character Grounds for Visa Refusals Australia 2026](https://www.gotocourt.com.au/immigration/new-character-grounds-for-visa-refusals-go-to-court-character).
- Prior hate-related visa cancellations (e.g., Israeli influencer Sammy Yahood, January 2026) predate the window and were made under "existing laws"/general character grounds rather than explicitly citing the new Act's provisions [Australia Cancels Another Israeli Speaker's Visa - The Blogs](https://blogs.timesofisrael.com/australia-cancels-another-israeli-speakers-visa/). This matches the question's own premise that, as of its May 13, 2026 creation, no cancellation had explicitly cited the new provisions.

Because no publicly confirmed visa cancellation or refusal explicitly citing the Act or its s.500A/s.501 amendments was identified within May 12 – July 1, 2026, and the resolution criteria specify that absence of such an identified action resolves NO, the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-24. `5daf5ef8-77b1-5320-a841-0645fc751f03`

- Present date: `2026-04-30 11:58:01.050692`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Ukrainian forces recapture any settlement in the Slovyansk direction between April 29 and June 1, 2026, as reported by ISW?

**Resolution criteria**

This question resolves **Yes** if all of the following conditions are met:

1. The Institute for the Study of War (ISW) explicitly reports in a daily "Russian Offensive Campaign Assessment" (published at https://understandingwar.org/research/russia-ukraine/) that Ukrainian forces have **recaptured** or **advanced into and taken control of** a settlement in the **"Slovyansk direction"** as identified by the section header in ISW's report.

2. The recapture and ISW's confirmation of it must occur **on or after April 29, 2026, 00:00 UTC** and **on or before June 1, 2026, 23:59 UTC**. Prior Ukrainian gains do not count.

3. A **"settlement"** is defined as any named city, town, or village (e.g., Zarichne, Dibrova, or any other named locality) that appears in the text of ISW's Slovyansk direction section or on ISW's "Assessed Control of Terrain" map accompanying the report.

4. The **"Slovyansk direction"** is defined as the operational area covered under that specific section header in ISW's daily assessment. This typically encompasses the area south and southeast of Slovyansk in Donetsk Oblast, including but not limited to the settlements along and near the M-03 Bakhmut–Slovyansk highway (e.g., Zarichne, Dibrova, and surrounding areas). Note: the adjacent "Kostyantynivka-Druzhkivka" tactical area is sometimes discussed within or alongside the Slovyansk direction section; a recapture reported in either sub-section counts.

5. **"Recaptured"** means ISW assesses that a settlement previously under Russian control or contested has transitioned to Ukrainian control, as indicated by ISW's text (e.g., "Ukrainian forces recaptured," "Ukrainian forces advanced into and took control of") or by a change on ISW's assessed control map from Russian-held/contested to Ukrainian-held.

If ISW does not publish such a report, or if no settlement recapture in the Slovyansk direction is reported by ISW by June 1, 2026, 23:59 UTC, this question resolves **No**.

**Primary resolution source:** ISW daily assessments at https://understandingwar.org/research/russia-ukraine/

**Pre-cutoff background**

As of late April 2026, the Slovyansk direction in eastern Ukraine remains an active combat zone. Russian forces continue offensive operations along this axis, while Ukrainian forces conduct periodic counterattacks. The ISW "Slovyansk direction" section of their daily assessments covers the area generally south and southeast of Slovyansk in Donetsk Oblast, including settlements along the M-03 Bakhmut–Slovyansk highway.

Key recent developments:
- On April 17, 2026, ISW confirmed Ukrainian forces recently advanced in the Slovyansk direction, with geolocated footage showing a Ukrainian-occupied trench northwest of Zarichne [Russian Offensive Campaign Assessment, April 17, 2026 | ISW](https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-april-17-2026/). Russian milbloggers claimed Russian advances along the M-03 highway southwest of Dibrova [Russian Offensive Campaign Assessment, April 17, 2026 | ISW](https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-april-17-2026/).
- The nearby Kostyantynivka-Druzhkivka tactical area (sometimes grouped with the Slovyansk direction) is highly contested, with Russian infiltration missions in Kostyantynivka, Berestok, and Maiske, and Russian claims of seizing Minkivka [Russian Offensive Campaign Assessment, April 17, 2026 | ISW](https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-april-17-2026/).
- On April 25–26, 2026, ISW reported continued Russian offensive operations in the Slovyansk direction with Ukrainian counterattacks ongoing, but no confirmed Russian advances [Russian Offensive Campaign Assessment, April 26, 2026 | ISW](https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-april-26-2026/).
- On April 28, 2026, ISW reported continued Russian offensive pressure in the Slovyansk direction with no Ukrainian recapture of settlements reported [https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-april-28-2026/](https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-april-28-2026/).

Ukrainian counterattacks in this area have been described as "limited" and "periodic," suggesting that while Ukrainian forces are active, full recapture of a named settlement remains uncertain. The primary resolution source is the ISW daily "Russian Offensive Campaign Assessment," published at https://understandingwar.org/research/russia-ukraine/.

**Exact later resolution packet**

Adjudicated: Across the April 29-June 1, 2026 window ISW never explicitly reported in its Slovyansk-direction (or Kostyantynivka-Druzhkivka) section that Ukrainian forces 'recaptured' or 'took control of' a named settlement, nor did the control map flip a settlement to Ukrainian-held. The May 10 report only says Ukrainian forces 'have likely cleared Lypivka from Russian infiltrators' (clearing infiltrators, not a Russian/contested-to-Ukrainian control transition, and hedged 'likely'); May 14 says Ukrainian forces 'advanced into central Zakitne' (a partial advance, and Russians were still striking Zakitne on May 31); and the May 18 'liberated Stavky' is explicitly a Russian-source claim, not an ISW assessment. Under the strict resolution criteria these fall short, so the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-25. `8652505a-de8f-568a-9506-3db07316451c`

- Present date: `2026-05-01 16:39:23.809153`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will either NaMA or EZEMA officially boycott the 2026 Ethiopian general election by June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after April 30, 2026 (00:00 UTC) and no later than June 1, 2026 (23:59 UTC), either the [National Movement of Amhara (NaMA)](https://en.wikipedia.org/wiki/National_Movement_of_Amhara) or the [Ethiopian Citizens for Social Justice (EZEMA)](https://en.wikipedia.org/wiki/Ethiopian_Citizens_for_Social_Justice) officially boycotts the [2026 Ethiopian general election](https://en.wikipedia.org/wiki/2026_Ethiopian_general_election).

An "official [boycott](https://en.wikipedia.org/wiki/Boycott)" is defined as meeting at least one of the following criteria:
1. A formal public statement by the party's authorized leadership (e.g., party chairperson or official spokesperson) declaring that the party will not participate in the June 1, 2026 general election; OR
2. The party formally withdrawing its candidate lists from the [National Election Board of Ethiopia](https://en.wikipedia.org/wiki/National_Election_Board_of_Ethiopia).

This question resolves as **No** if neither party meets the above criteria by 23:59 UTC on June 1, 2026.

**Resolution sources:** Credible reporting from international news agencies (e.g., [Reuters](https://www.reuters.com/), [Associated Press](https://apnews.com/), [BBC](https://www.bbc.com/)) or reputable Ethiopian outlets (e.g., [Addis Standard](https://addisstandard.com/), [Borkena](https://borkena.com/)), or official statements published on the parties' verified communication channels. Any boycott announced prior to April 30, 2026 (00:00 UTC) does not count toward resolution.

**Pre-cutoff background**

Ethiopia is scheduled to hold its 7th general election on June 1, 2026. The political environment has been described as "procedural authoritarianism," where the ruling Prosperity Party maintains the machinery of elections while restricting conditions for genuine political competition [Ethiopia's Election and the Death of Political Choice](https://africanarguments.org/2026/03/ethiopias-election-and-the-death-of-political-choice/). Ongoing armed conflicts persist in the Amhara, Oromia, and Tigray regions, and opposition groups have raised concerns about political inclusion and electoral legitimacy [Ethiopia elections put national fault lines in the spotlight](https://nai.uu.se/stories-and-events/news/2026-04-28-ethiopia-elections-put-national-fault-lines-in-the-spotlight.html).

The [National Movement of Amhara (NaMA)](https://en.wikipedia.org/wiki/National_Movement_of_Amhara) and the [Ethiopian Citizens for Social Justice (EZEMA)](https://en.wikipedia.org/wiki/Ethiopian_Citizens_for_Social_Justice) are among the most prominent opposition parties contesting the [2026 Ethiopian general election](https://en.wikipedia.org/wiki/2026_Ethiopian_general_election). As of late April 2026, both parties are listed as participating in the election [https://en.wikipedia.org/wiki/2026_Ethiopian_general_election](https://en.wikipedia.org/wiki/2026_Ethiopian_general_election). EZEMA recently replaced two senior leaders ahead of the election (as reported by Borkena in March 2026), and its new leader has spoken publicly about the election, suggesting continued engagement with the electoral process. However, some opposition coalitions have declared that conditions for a democratic process are absent [Ethiopia's Election and the Death of Political Choice](https://africanarguments.org/2026/03/ethiopias-election-and-the-death-of-political-choice/), and analysts have noted severely restricted media, detained journalists, and conflict-affected areas where political activity is curtailed [Ethiopia's Election and the Death of Political Choice](https://africanarguments.org/2026/03/ethiopias-election-and-the-death-of-political-choice/). Neither NaMA nor EZEMA has formally announced a boycott as of April 30, 2026, but the deteriorating political environment means a last-minute withdrawal remains plausible.

**Exact later resolution packet**

The question resolves NO. It asked whether either NaMA (National Movement of Amhara) or EZEMA (Ethiopian Citizens for Social Justice) would officially boycott the 2026 Ethiopian general election (held June 1, 2026) during the window April 30–June 1, 2026, via a formal leadership statement of non-participation or formal withdrawal of candidate lists from NEBE.

Evidence shows both parties participated in the election rather than boycotting:

- Al Jazeera's election guide published May 31, 2026 (one day before the vote) explicitly lists both parties as active participants: NaMA was "fielding candidates primarily within the Amhara region" and EZEMA was "contesting seats in both the House of Peoples' Representatives and regional councils" [1553ef].
- Al Jazeera's May 29, 2026 article describes opposition parties participating in the election (albeit under duress, to avoid license revocation) and contains no mention of an official boycott by NaMA or EZEMA [9eef96].
- The Wikipedia article on the 2026 Ethiopian general election (last updated May 15, 2026) lists both NaMA and EZEMA as participants with their leaders identified, and contains no record of any boycott or withdrawal by either party [c23f61].

While there was a general boycott narrative in Ethiopia, the bodies threatening/calling for boycott were distinct from NaMA and EZEMA: the "Peace for Ethiopia Coalition" (an alliance of eight smaller parties including the Agew National Council, Gamo Democratic Party, Gambella Peoples' Freedom Movement, Kaffa Green Party, and Tigray Democratic Cooperation) threatened withdrawal, and the Amhara Fano rebel movement urged opposition parties not to take part. Neither of these involved an official boycott declaration or candidate-list withdrawal by NaMA or EZEMA themselves [1553ef]. EZEMA, having recently replaced its leadership, continued engaging with the process, and NaMA fielded regional candidates who described the process as proceeding.

Because neither NaMA nor EZEMA met either criterion (no formal leadership statement of non-participation; no formal withdrawal of candidate lists from NEBE) within the April 30–June 1, 2026 window, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-26. `f4e752d2-cbc1-5cc4-b1ed-306106fa8b12`

- Present date: `2026-05-29 06:58:15.167596`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the U.S. Supreme Court rule in Watson v. Republican National Committee that federal law prohibits states from counting mail-in ballots received after Election Day?

**Resolution criteria**

This question resolves based on the official opinion of the U.S. Supreme Court in *Watson v. Republican National Committee* (No. 24-1260), as published on the Supreme Court's opinions page at https://www.supremecourt.gov/opinions/opinions.aspx.

The ruling must be issued on or after May 12, 2026 (12:00 UTC).

- **Resolves YES** if the Court issues a majority opinion holding that federal election-day statutes (2 U.S.C. § 7 and/or 3 U.S.C. § 1) preempt state laws that allow the counting of mail-in ballots received after Election Day—i.e., that federal law prohibits states from counting such late-arriving ballots for federal elections.

- **Resolves NO** if the Court issues a majority opinion holding that federal law does not prohibit states from counting mail-in ballots received after Election Day, or if the Court issues a ruling that does not reach the merits of whether federal law imposes such a prohibition (e.g., the case is dismissed for lack of standing, mootness, or other procedural grounds).

- If no opinion is issued by July 1, 2026 (23:59 UTC), the question resolves as **No**.

**Pre-cutoff background**

The U.S. Supreme Court is considering *Watson v. Republican National Committee* (Case No. 24-1260), which challenges a Mississippi law allowing mail-in ballots to be counted if postmarked by Election Day and received within five business days thereafter. The Republican National Committee and the Libertarian Party of Mississippi argue that federal statutes establishing Election Day—specifically 2 U.S.C. § 7 (congressional elections) and 3 U.S.C. § 1 (presidential elections)—preempt state laws permitting late-arriving ballots [https://www.scotusblog.com/2026/03/court-appears-ready-to-overturn-state-law-allowing-for-late-arriving-mail-in-ballots/](https://www.scotusblog.com/2026/03/court-appears-ready-to-overturn-state-law-allowing-for-late-arriving-mail-in-ballots/).

During oral arguments on March 23, 2026, the Court's conservative majority appeared skeptical of Mississippi's grace-period law, with several justices suggesting it conflicts with federal election-day statutes [https://www.scotusblog.com/2026/03/court-appears-ready-to-overturn-state-law-allowing-for-late-arriving-mail-in-ballots/](https://www.scotusblog.com/2026/03/court-appears-ready-to-overturn-state-law-allowing-for-late-arriving-mail-in-ballots/). SCOTUSblog reported the Court "appeared ready to overturn" the Mississippi law [https://www.scotusblog.com/2026/03/court-appears-ready-to-overturn-state-law-allowing-for-late-arriving-mail-in-ballots/](https://www.scotusblog.com/2026/03/court-appears-ready-to-overturn-state-law-allowing-for-late-arriving-mail-in-ballots/). However, oral argument signals do not always predict outcomes, and the Court could issue a narrow ruling, find procedural deficiencies, or rule in Mississippi's favor [https://news.wttw.com/2026/03/27/supreme-court-weighs-whether-limit-mail-ballot-counts-after-election-day-how-will-it](https://news.wttw.com/2026/03/27/supreme-court-weighs-whether-limit-mail-ballot-counts-after-election-day-how-will-it).

A ruling against Mississippi would have sweeping implications: over a dozen states, including Illinois (which allows a 14-day grace period), have similar laws permitting ballots postmarked by Election Day to be counted if received after that date [https://news.wttw.com/2026/03/27/supreme-court-weighs-whether-limit-mail-ballot-counts-after-election-day-how-will-it](https://news.wttw.com/2026/03/27/supreme-court-weighs-whether-limit-mail-ballot-counts-after-election-day-how-will-it). The decision is expected by late June 2026, consistent with the Court's typical end-of-term opinion schedule.

**Exact later resolution packet**

The question asks whether the U.S. Supreme Court would rule in Watson v. Republican National Committee (No. 24-1260) that federal law (2 U.S.C. § 7 and/or 3 U.S.C. § 1) prohibits states from counting mail-in ballots received after Election Day. The Court ruled the OPPOSITE, so the question resolves NO.

Key findings, from the official Supreme Court opinion (https://www.supremecourt.gov/opinions/25pdf/24-1260_g3cn.pdf) and SCOTUSblog:

1. Decision date and validity window: The opinion was issued on June 29, 2026 [[PDF] 24-1260 Watson v. Republican National Committee (06/29/2026)](https://www.supremecourt.gov/opinions/25pdf/24-1260_g3cn.pdf) [Justices uphold state law allowing for late-arriving mail-in ballots](https://www.scotusblog.com/2026/06/justices-uphold-state-law-allowing-for-late-arriving-mail-in-ballots/). This is on or after May 12, 2026 (12:00 UTC) and before the July 1, 2026 (23:59 UTC) deadline, so the ruling counts under the resolution criteria (it is neither too early nor absent).

2. Merits vs. procedural: The Court reached the MERITS. It did not dismiss for standing, mootness, or other procedural grounds. Justice Barrett's majority opinion held that the term "election" in the federal election-day statutes refers to the electorate's act of choosing a candidate, which is complete when a voter casts the ballot, so the statutes do not set a ballot-receipt deadline and do not preempt Mississippi's grace-period law [[PDF] 24-1260 Watson v. Republican National Committee (06/29/2026)](https://www.supremecourt.gov/opinions/25pdf/24-1260_g3cn.pdf).

3. Holding (directly opposite to the YES condition): The Court held that the federal election-day statutes (2 U.S.C. § 7 and 3 U.S.C. § 1) do NOT prevent Mississippi from counting absentee ballots postmarked by Election Day but received up to five days afterward. In other words, federal law does NOT prohibit states from counting such late-arriving ballots [[PDF] 24-1260 Watson v. Republican National Committee (06/29/2026)](https://www.supremecourt.gov/opinions/25pdf/24-1260_g3cn.pdf) [Justices uphold state law allowing for late-arriving mail-in ballots](https://www.scotusblog.com/2026/06/justices-uphold-state-law-allowing-for-late-arriving-mail-in-ballots/). The Court reversed the Fifth Circuit and upheld the Mississippi law [Justices uphold state law allowing for late-arriving mail-in ballots](https://www.scotusblog.com/2026/06/justices-uphold-state-law-allowing-for-late-arriving-mail-in-ballots/).

4. Vote: The decision was 5-4. The majority opinion was delivered by Justice Barrett, joined by Chief Justice Roberts and Justices Sotomayor, Kagan, and Jackson; Justice Alito filed a dissent joined by Justices Thomas and Gorsuch (with Kavanaugh joining in part) [[PDF] 24-1260 Watson v. Republican National Committee (06/29/2026)](https://www.supremecourt.gov/opinions/25pdf/24-1260_g3cn.pdf).

Because the resolution criteria state the question resolves NO "if the Court issues a majority opinion holding that federal law does not prohibit states from counting mail-in ballots received after Election Day," and that is exactly what happened, the correct resolution is NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-27. `188a20b2-d582-5f07-8279-4ed1926e4635`

- Present date: `2026-05-02 16:09:02.315138`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Google announce at I/O 2026 that AI-generated responses are the default primary result for over 50% of Google Search queries?

**Resolution criteria**

This question resolves YES if, on or after May 1, 2026, and by June 1, 2026 (23:59 UTC), Google publishes an official announcement meeting ALL of the following criteria:

1. **Source**: The announcement must appear on the official Google Keyword Blog (https://blog.google/), the official Google I/O event page (https://io.google/2026/), or be made during a livestreamed Google I/O 2026 keynote session (verifiable via the official YouTube recording at https://www.youtube.com/@Google).

2. **"Default experience" claim**: Google must explicitly state that AI-generated responses (powered by Gemini or successor models) are now the default, automatically displayed result format—not an opt-in feature, experimental mode, or Labs feature—for the specified query volume. "Default experience" means the AI-generated response is automatically shown as the primary content above or instead of the traditional list of ranked web page links (https://en.wikipedia.org/wiki/Search_engine_results_page) without requiring any user action to activate it.

3. **"Majority" threshold (>50%)**: Google must explicitly claim, using a specific number or percentage, that this default AI experience applies to more than 50% of all Google Search queries (not limited to a single country, query type, or user segment, unless Google specifies it covers all US queries, which would suffice). The >50% figure must be stated or clearly implied by Google's own language (e.g., "most queries," "the majority of searches"). Verification is based on Google's own stated figures in the announcement.

4. **"Replacing traditional ten blue links"**: The announcement must indicate that the standard ranked list of web page links is no longer the primary content in the main viewport for the covered queries—meaning the AI response occupies the dominant position and traditional links are either removed, collapsed, or pushed below the fold. Mere addition of an AI summary above an otherwise unchanged link list does NOT qualify.

If no such announcement meeting all four criteria is made by 23:59 UTC on June 1, 2026, the question resolves NO.

**Pre-cutoff background**

Google Search has historically presented results as a ranked list of web page links (commonly called "ten blue links," see https://en.wikipedia.org/wiki/Web_search_engine#Search_results). Since 2024, Google has been rolling out "AI Overviews" (https://blog.google/products/search/generative-ai-google-search-may-2024/), which are AI-generated summaries displayed above traditional link results.

As of April 2026, third-party tracking data from BrightEdge indicates AI Overviews appear in approximately 48% of Google Search queries in the United States, up from 34.5% in December 2025. Globally, estimates vary widely—some sources report approximately 13% of all queries worldwide trigger AI Overviews. Despite this expansion, traditional ranked links remain visible below AI Overviews on most results pages, and AI Overviews are not yet universally present across all query types and markets.

Google I/O 2026 (https://io.google/2026/) is scheduled for May 19–20, 2026, at Shoreline Amphitheatre in Mountain View, California, with livestreamed keynotes. Google I/O is the company's primary venue for announcing major product strategy shifts. Nick Fox, VP of Search at Google, has publicly stated that "search is becoming AI search," signaling intent to further integrate Gemini AI capabilities into the core search experience. Competitive pressure from ChatGPT Search and Perplexity AI creates incentive to accelerate this transition, while advertiser revenue concerns create counter-pressure.

The question asks whether Google will make a specific formal announcement—not merely whether AI Overviews continue to expand organically.

**Exact later resolution packet**

The question requires that, between May 1 and June 1, 2026, Google publish an official announcement (on the Keyword Blog, the I/O event page, or in an I/O 2026 keynote) meeting ALL FOUR criteria: (1) AI responses are the default/automatically-displayed format, (2) for >50% of all (or all US) Google Search queries, stated with a specific figure, and (3) with traditional ranked links removed/collapsed/pushed below the fold (mere addition of an AI summary above an unchanged link list does not qualify).

I reviewed the two primary official Google sources from Google I/O 2026 (held May 19-20, 2026):

1. Google's official Search I/O 2026 blog post ("A new era for AI Search," https://blog.google/products-and-platforms/products/search/search-io-2026/, published 2026-05-19) does NOT claim AI responses are the default for >50% of queries. It notes AI Mode surpassed 1 billion monthly users and queries doubling quarterly, and that Gemini 3.5 Flash is the new default model *in AI Mode* (i.e., the model powering the feature, not the search experience itself). Critically, it explicitly states the opposite of criterion 4: "You'll continue to get a range of results from Search, just like you do today" [Google Search's I/O 2026 updates: AI agents and more](https://blog.google/products-and-platforms/products/search/search-io-2026/).

2. Sundar Pichai's I/O 2026 keynote blog post (https://blog.google/innovation-and-ai/sundar-pichai-io-2026/, 2026-05-19) cites only adoption figures — AI Overviews has 2.5 billion monthly active users and AI Mode has 1 billion monthly active users — but makes NO claim that AI responses are the default for over 50% of all search queries, nor that traditional links are being removed/collapsed/pushed below the fold [I/O 2026: Welcome to the agentic Gemini era - Google Blog](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/).

Neither source states a specific percentage (>50%) of queries for which AI is the default primary result, neither declares AI responses the default replacing the traditional link list, and the Search blog post affirmatively states users continue to get traditional Search results "just like you do today." Thus criteria 3 and 4 (and arguably 2) were not satisfied. Since not all four criteria were met by the deadline, the question resolves NO.

Note: Some third-party/SEO commentary (e.g., a Modo25 blog post) loosely claimed "AI Mode is now the global default," but the resolution criteria restrict valid sources to Google's own official Keyword Blog, I/O event page, or the official YouTube keynote recording, and Google's own language does not support the >50%-default-replacement claim.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-28. `470e6be8-2f05-56ac-b19c-fa9a23937985`

- Present date: `2026-05-16 01:50:49.817576`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-06-30T00:00:00`

**Question**

Will both top-two finishers in the June 2, 2026, California gubernatorial primary be Democrats?

**Resolution criteria**

This question resolves **Yes** if both of the top two vote-getters in the June 2, 2026, California gubernatorial primary election have an official party preference of "Democratic" as listed by the California Secretary of State. It resolves **No** if one or both of the top two vote-getters have any other party preference (e.g., Republican, No Party Preference, etc.).

"Advancing" means being one of the top two vote-getters in the primary according to the official results.

"Democrats" means candidates whose ballot-qualified party preference is listed as "Democratic" by the California Secretary of State.

Resolution is based on the official or certified results published by the California Secretary of State at https://www.sos.ca.gov/elections/prior-elections/statewide-election-results — not on preliminary media projections or calls. If official results are not yet certified by the scheduled resolution date but the Secretary of State's website shows sufficiently complete results (e.g., semi-official or 100% reporting) that clearly indicate the top two finishers, those results may be used. If results remain too close to call or are subject to a recount as of 11:59 PM UTC on June 30, 2026, resolution is deferred until certification.

**Pre-cutoff background**

California uses a "top-two" primary system in which all candidates for governor, regardless of party affiliation, appear on a single ballot. The two candidates receiving the most votes advance to the November general election, meaning two candidates from the same party can advance.

The June 2, 2026, gubernatorial primary features a large and fragmented field. According to an Emerson College poll conducted April 14–15, 2026, the leading candidates and their support levels are: Republican Steve Hilton at 17%, Democrat Tom Steyer at 14%, Republican Chad Bianco at 14%, Democrat Xavier Becerra at 10%, Democrat Katie Porter at 10%, and Democrat Matt Mahan at 5%, with 23% of voters undecided [https://emersoncollegepolling.com/california-2026-poll-april/](https://emersoncollegepolling.com/california-2026-poll-april/). Former President Trump has endorsed Steve Hilton, boosting his profile among Republican voters.

The fragmented Democratic field—with at least four major Democratic candidates splitting the vote—creates a realistic scenario in which two Republicans could advance. Conversely, if Republican support remains split between Hilton and Bianco while Democratic voters consolidate behind one or two candidates, two Democrats could advance. The high proportion of undecided voters adds further uncertainty to the outcome.

**Exact later resolution packet**

The question resolves NO.

Resolution criteria: The question resolves YES only if BOTH of the top two vote-getters in the June 2, 2026 California gubernatorial primary have an official party preference of "Democratic" as listed by the California Secretary of State. It resolves NO if one or both have any other party preference.

Evidence from the official California Secretary of State results pages (https://electionresults.sos.ca.gov/returns/governor and its data-portal mirror https://dp.electionresults.sos.ca.gov/returns/governor), the designated resolution source:

Top finishers in the June 2, 2026 Governor primary:
1. Xavier Becerra — Party Preference: DEMOCRATIC — ~2,590,600–2,590,958 votes (~28.1%) [eb0ad3, 1f4b25]
2. Steve Hilton — Party Preference: REPUBLICAN — ~2,276,000–2,276,271 votes (~24.7%) [eb0ad3, 1f4b25]
3. Tom Steyer — Party Preference: DEMOCRATIC — ~2,109,692 votes (~22.8%), placing THIRD [1f4b25]

Because the second-place finisher, Steve Hilton, has an official party preference of "Republican" — not "Democratic" — the two advancing candidates are one Democrat and one Republican. Therefore the condition for YES (both top-two being Democratic) is NOT met, and the question resolves NO.

Certification / completeness check: The SoS results show 100% of precincts reporting (19,788 of 19,788), satisfying the resolution criteria's "sufficiently complete" (100% reporting) exception for use before final certification. Certification is scheduled for July 10, 2026 (after the June 30, 2026 resolution date), but the results clearly and unambiguously indicate the top two finishers, and the ~166,000-vote margin between Hilton (2nd, Republican) and Steyer (3rd, Democrat) is not too close to call and not subject to a recount [eb0ad3, 1f4b25]. This is corroborated by Ballotpedia and Wikipedia, which report that Xavier Becerra (D) and Steve Hilton (R) advanced to the November 3, 2026 general election [769406].

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-29. `2117e428-00b0-5612-995d-2b1640f2eb56`

- Present date: `2026-05-02 16:55:07.611390`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will a federal court issue a new injunction or TRO blocking National Guard deployment for immigration enforcement in any U.S. state between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if a United States federal court — defined as any U.S. District Court, U.S. Court of Appeals (Circuit Court), or the U.S. Supreme Court — issues a written order on or after May 1, 2026, 12:00 AM Eastern Time (ET), and on or before June 1, 2026, 11:59 PM ET, that explicitly blocks, halts, or prohibits the deployment or continued deployment of National Guard troops for immigration enforcement purposes in any U.S. state.

Key definitions:
- **Injunction**: Includes any Temporary Restraining Order (TRO), preliminary injunction, or permanent injunction issued by a federal court. Administrative stays or voluntary government withdrawals do not count.
- **Immigration enforcement**: Deployment of National Guard personnel for the purpose of supporting federal immigration operations, including but not limited to: protecting ICE facilities or personnel, assisting with border patrol, conducting immigration-related checkpoints, or detaining individuals based on immigration status. Routine National Guard activities such as disaster relief, counter-drug operations unrelated to immigration, or training exercises do not qualify.
- **Federal court**: Any court within the United States federal judiciary, specifically U.S. District Courts, U.S. Courts of Appeals, or the U.S. Supreme Court. State courts are excluded.

The order must be a new order issued within the specified window. Orders issued before May 1, 2026 that remain in effect do not count.

If no such order is issued by 11:59 PM ET on June 1, 2026, the question resolves **No**.

**Resolution sources**: Credible major news outlets (e.g., [Reuters](https://www.reuters.com/), [AP News](https://apnews.com/), [SCOTUSblog](https://www.scotusblog.com/)), legal databases such as [CourtListener](https://www.courtlistener.com/) or [PACER](https://pacer.uscourts.gov/), or official court filings.

**Pre-cutoff background**

The Trump administration has repeatedly attempted to federalize National Guard troops for immigration enforcement, prompting significant litigation. Key developments include:

- In October 2025, a federal judge in Illinois (U.S. District Judge April Perry) issued a temporary restraining order blocking National Guard deployment to Chicago during "Operation Midway Blitz." The Supreme Court declined to overturn this block in December 2025 in a 6-3 ruling [Judge Dismisses Lawsuit Challenging National Guard Deployment ...](https://news.wttw.com/2026/04/20/judge-dismisses-lawsuit-challenging-national-guard-deployment-illinois-months-after).

- In California, U.S. District Judge Charles Breyer issued a preliminary injunction ordering the end of the federalized National Guard deployment in Los Angeles. On December 31, 2025, the Ninth Circuit allowed this ruling to take effect, and Governor Newsom directed troops to return to state control [Federal court finally ends illegal federalization of National Guard ...](https://www.gov.ca.gov/2025/12/31/federal-court-finally-ends-illegal-federalization-of-national-guard-after-trump-gives-up-governor-newsom-directs-leadership-to-quickly-send-soldiers-home-to-families/).

- As of April 20, 2026, the Illinois lawsuit was dismissed with prejudice by Judge Perry as moot, since all federalized troops had been withdrawn [Judge Dismisses Lawsuit Challenging National Guard Deployment ...](https://news.wttw.com/2026/04/20/judge-dismisses-lawsuit-challenging-national-guard-deployment-illinois-months-after).

- Tennessee has also faced litigation challenging the governor's activation of the National Guard for immigration-related purposes.

As of May 1, 2026, the major prior injunctions have either been dissolved or rendered moot by troop withdrawals. However, the administration retains the legal authority to attempt new deployments, and new legal challenges could arise in any jurisdiction. The Supreme Court's December 2025 ruling in Trump v. Illinois established significant precedent limiting the president's authority to federalize Guard troops over a governor's objection, but did not categorically bar all such deployments.

**Exact later resolution packet**

The question resolves NO. It asked whether a U.S. federal court (District Court, Court of Appeals, or Supreme Court) would issue a NEW written TRO, preliminary injunction, or permanent injunction between May 1, 2026, 12:00 AM ET and June 1, 2026, 11:59 PM ET, explicitly blocking National Guard deployment for immigration-enforcement purposes in any U.S. state.

Findings from my research:

1) By early 2026, all the major prior National Guard injunctions had been dissolved or rendered moot. The California (LA) deployment ended after the Ninth Circuit allowed Judge Breyer's preliminary injunction to take effect on Dec. 31, 2025; the Illinois/Chicago TRO case (Judge April Perry) was dismissed with prejudice as moot on April 20, 2026; the Portland (Oregon) permanent injunction issued Nov. 2025; and the Supreme Court left the Chicago block in place in Trump v. Illinois (Dec. 2025). All of these orders predate the May 1, 2026 window and therefore do not count.

2) The comprehensive Wikipedia tracker "Domestic military deployments by the second Trump administration" (last edited May 19, 2026) contains no record of any new federal court order issued between May 1 and June 1, 2026 blocking Guard deployment for immigration enforcement; its timeline ends with troop withdrawals in early 2026 [7477d6].

3) The Capital B News city-by-city breakdown (updated Feb. 12, 2026) and the States United Democracy Center National Guard litigation tracker likewise contain no new injunction in the May 2026 window; major cases were paused, dismissed, or mooted by January 2026 [a419a0, db9876].

4) The only active relevant litigation in this period was in Minnesota (State of Minnesota et al. v. Noem et al., challenging the ICE "surge"/Operation Metro Surge). The federal judge DENIED Minnesota's requested preliminary injunction, and a May 6, 2026 Democracy Forward press release confirms the court "Allow[ed] Immigration Enforcement Activity Near Minnesota Schools to Continue." That case primarily concerns federal ICE/law-enforcement officers rather than National Guard deployment, and in any event the court did NOT issue an order blocking it. So even the one live case in the window produced no qualifying blocking order.

No credible source (Reuters, AP, SCOTUSblog, CourtListener, official filings, or legal trackers) reports any new federal TRO or injunction blocking National Guard deployment for immigration enforcement issued between May 1 and June 1, 2026. Therefore the question resolves NO.

Key sources:
- Wikipedia "Domestic military deployments by the second Trump administration": https://en.wikipedia.org/wiki/Domestic_military_deployments_by_the_second_Trump_administration
- States United litigation tracker: https://statesunited.org/resources/national-guard-litigation/
- Capital B News tracker: https://capitalbnews.org/trump-national-guard-city-updates/
- Democracy Forward (May 6, 2026): https://democracyforward.org/news/press-releases/court-allows-immigration-enforcement-activity-near-minnesota-schools-to-continue-lawsuit-proceeds/
- WTTW (Illinois dismissal April 20, 2026): https://news.wttw.com/2026/04/20/judge-dismisses-lawsuit-challenging-national-guard-deployment-illinois-months-after

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-30. `fc6adee8-aed5-5cbd-97d3-7cdb5cbee281`

- Present date: `2026-05-03 05:26:45.511246`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the World Bank Board of Executive Directors approve the proposed up-to-$2 billion guarantee for Argentina by June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if the World Bank's Board of Executive Directors formally approves the proposed guarantee of up to US$2 billion for Argentina on or after May 1, 2026, at 00:00 UTC, and on or before June 1, 2026, at 23:59 UTC.

This question resolves as **No** if no such approval is announced by that deadline, or if the proposal is formally rejected or withdrawn.

**Definitions:**
- **Board of Executive Directors**: The World Bank Group's main decision-making body for project and guarantee approvals, as described at https://www.worldbank.org/en/about/leadership/directors
- **Guarantee**: A financial instrument provided through the [IBRD](https://www.worldbank.org/en/who-we-are/ibrd) and/or [MIGA](https://www.miga.org/) that backs Argentina's debt refinancing obligations, as described in the World Bank Group's April 16, 2026 statement.
- **Approval**: A formal decision by the Board of Executive Directors to proceed with the guarantee, as evidenced by an official World Bank press release, project document, or statement.

**Resolution source:** The official World Bank News page (https://www.worldbank.org/en/news/all), the World Bank Projects portal (https://projects.worldbank.org/), or the World Bank Finances One portal (https://financesone.worldbank.org/countries/argentina). If the approval is announced via a credible wire service (Reuters, Bloomberg, AP) citing official World Bank confirmation, this may also be used.

**Pre-cutoff background**

On April 16, 2026, the World Bank Group issued an official statement confirming it is working on a guarantee of up to US$2 billion to help Argentina refinance a relevant portion of its debt, reduce financing costs, and create better conditions for increased domestic and international private investment [World Bank Group Backs Argentina's Efforts to Strengthen ...](https://www.worldbank.org/en/news/statement/2026/04/16/world-bank-group-backs-argentina-s-efforts-to-strengthen-growth-investment-and-jobs). Reuters reported the same day that the guarantee would be backed by the International Bank for Reconstruction and Development (IBRD) and the Multilateral Investment Guarantee Agency (MIGA), and that the operation is subject to approval by the World Bank's Board of Executive Directors [World Bank plans up to $2 billion guarantee to help Argentina ...](https://www.reuters.com/world/americas/world-bank-plans-up-2-billion-guarantee-help-argentina-refinance-debt-2026-04-16/).

As of May 1, 2026, the proposal remains in the planning/preparation stage and has not yet received formal Board approval [World Bank Group Backs Argentina's Efforts to Strengthen ...](https://www.worldbank.org/en/news/statement/2026/04/16/world-bank-group-backs-argentina-s-efforts-to-strengthen-growth-investment-and-jobs). The World Bank's project finance portal shows total Board approval amounts for Argentina of approximately US$4.58 billion across 120 projects as of April 17, 2026, indicating no new guarantee approval has been recorded yet.

This guarantee is part of a broader international support package for Argentina under President Milei's economic reform program, which also includes a $20 billion IMF Extended Fund Facility. The Board approval process involves review by the 25 Executive Directors representing the World Bank's member countries, and can be influenced by political considerations, technical readiness of the project documentation, and Argentina's compliance with reform commitments.

**Exact later resolution packet**

The question asks whether the World Bank's Board of Executive Directors formally approved the proposed up-to-US$2 billion guarantee for Argentina between May 1, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC).

Key findings:

1) The guarantee was announced on April 16, 2026 only as a proposal in the planning/preparation stage. The official World Bank Group statement ("World Bank Group Backs Argentina's Efforts to Strengthen Growth, Investment, and Jobs," April 16, 2026, https://www.worldbank.org/en/news/statement/2026/04/16/world-bank-group-backs-argentina-s-efforts-to-strengthen-growth-investment-and-jobs) states the Group "is working on a guarantee of up to US$2 billion" and that "The proposed operation is subject to approval by the World Bank's Board of Executive Directors." This is a planning/preparation statement, NOT formal Board approval. Reuters (https://www.reuters.com/world/americas/world-bank-plans-up-2-billion-guarantee-help-argentina-refinance-debt-2026-04-16/) confirmed the same, noting backing by IBRD and MIGA and that the operation remained subject to Board approval.

2) Checking the official resolution sources for evidence of formal approval within the window:
- The World Bank Group statement page, reviewed as of June 2, 2026, contains a "What's New" list of items running up to June 1, 2026, and makes NO mention of any Argentina guarantee approval [World Bank Group Backs Argentina's Efforts to Strengthen Growth ...](https://www.worldbank.org/en/news/statement/2026/04/16/world-bank-group-backs-argentina-s-efforts-to-strengthen-growth-investment-and-jobs).
- The World Bank Projects portal for Argentina (https://projects.worldbank.org/en/projects-operations/projects-list?countrycode_exact=AR), reviewed as of June 2, 2026, contains NO entry for a $2 billion guarantee approved between May 1 and June 1, 2026. The Argentina-related pipeline projects listed ("Enabling Private Sector Investment and Growth for Job Creation" – Pipeline, June 16, 2026; "Resilient Infrastructure... Salta Project" – Pipeline, July 6, 2026) are not Board-approved guarantees, and the only DPF-type approval predates the window (April 11, 2025) [https://projects.worldbank.org/en/projects-operations/projects-list?countrycode_exact=AR](https://projects.worldbank.org/en/projects-operations/projects-list?countrycode_exact=AR).

3) No credible wire service (Reuters, Bloomberg, AP) reported a formal Board approval citing official World Bank confirmation within the window. All located reporting (April 16–18, 2026) describes the operation as being negotiated/prepared and "subject to approval," with related items (IDB co-financing, IMF disbursements) but no World Bank Board approval of the guarantee.

The distinction between "planning/preparation" (the April 16 statement — "working on," "proposed operation... subject to approval") and "formal Board approval" is explicit: no formal Board of Executive Directors approval of the guarantee was announced on or before June 1, 2026, 23:59 UTC. Per the resolution criteria, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-31. `aa7f75d8-920e-5854-9a33-03e9c4c39cfa`

- Present date: `2026-05-01 17:46:42.075696`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the US Department of Defense announce a new critical minerals offtake agreement or investment exceeding $100 million between May 1, 2026, and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the US Department of Defense (or an entity acting on its behalf, such as the Defense Industrial Base Consortium) publicly announces a new offtake agreement or investment related to critical minerals with a total stated contract or agreement value exceeding $100 million USD. The announcement must be dated between 00:00 UTC on May 1, 2026 and 23:59 UTC on June 1, 2026.

**Key definitions:**

- **"Critical minerals"**: Any mineral on the [USGS Critical Minerals List](https://www.usgs.gov/news/national-news-release/us-geological-survey-releases-2022-list-critical-minerals) (currently 60 minerals), or rare earth elements as defined by the [USGS rare earths page](https://www.usgs.gov/centers/nmic/rare-earths-statistics-and-information).
- **"Offtake agreement"**: A contractual commitment by the DoD (or an agent thereof) to purchase a specified quantity of critical mineral output from a producer over a defined period, as described in [10 U.S.C. § 4022](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title10-section4022) or the [Defense Production Act, Title III](https://www.fema.gov/disaster/defense-production-act).
- **"Investment"**: A direct equity investment, grant, loan, loan guarantee, or convertible note from the DoD or DPA Title III funds into a critical minerals project.
- **"Exceeding $100 million"**: The total stated contract value, agreement value, or investment commitment must exceed $100 million USD as announced. This refers to the total value of the agreement (not just the initial obligation or first-year funding). If a press release states a range (e.g., "up to $150 million"), the upper bound must exceed $100 million.

**Resolution source:** Official DoD press releases at [https://www.defense.gov/News/Releases/](https://www.defense.gov/News/Releases/), the [DIBC website](https://www.dibconsortium.org/), or credible reporting from Reuters, Bloomberg, or AP confirming the announcement.

The announcement must be for a **new** agreement or investment — extensions or modifications of previously announced agreements (such as the existing MP Materials deal) do not count unless they constitute a separate, new commitment exceeding $100 million.

If no qualifying announcement is made by 23:59 UTC on June 1, 2026, the question resolves **No**.

**Pre-cutoff background**

The US Department of Defense (DoD) has been aggressively investing in domestic critical mineral supply chains, primarily through Defense Production Act (DPA) Title III authority. Key recent developments as of May 1, 2026 include:

- **Project Vault**, announced February 2, 2026, is a strategic minerals stockpile backed by a US$10 billion Export-Import Bank (EXIM) loan and approximately $2 billion in private capital, covering all 60 minerals on the USGS Critical Minerals List [US Critical Minerals Policy: What the $700 Billion Actually Buys and ...](https://kamoacap.com/uscriticalmineralspolicy).
- The DoD's July 2025 partnership with MP Materials included a 10-year offtake agreement for rare earth magnets worth over $400 million.
- On February 27, 2026, the Defense Industrial Base Consortium (DIBC) issued a new Request for Project Proposals (RPP) targeting 13 defense-critical minerals (arsenic, bismuth, gadolinium, germanium, graphite, hafnium, nickel, samarium, tungsten, vanadium, ytterbium, yttrium, and zirconium), with indicated funding levels ranging from approximately $100 million to over $500 million per project [Defense Industrial Base Consortium Issues New Critical Minerals ...](https://www.insidegovernmentcontracts.com/2026/03/defense-industrial-base-consortium-issues-new-critical-minerals-request-for-project-proposals/).
- DPA Title III authority is set to sunset in September 2026 without reauthorization, creating a "policy cliff" that may accelerate the pace of new announcements before that deadline [US Critical Minerals Policy: What the $700 Billion Actually Buys and ...](https://kamoacap.com/uscriticalmineralspolicy).
- In FY2026 so far, DoD has made smaller DPA awards (e.g., $11.8M and $43.4M), but the DIBC RPP pipeline suggests larger awards could be forthcoming.

The combination of the DPA sunset pressure, active DIBC solicitations with $100M+ project sizes, and strong political emphasis on critical minerals makes a large announcement plausible but far from certain within any given 31-day window.

**Exact later resolution packet**

The question resolves NO because no qualifying announcement was found between May 1, 2026 and June 1, 2026.

Reviewing the official resolution sources:

1. **Official DoD/War.gov press releases (May 2026):** A review of the Department of War (DoD) press releases page and the Industrial Base Policy news feed showed the only investment-related releases in the May 2026 window were: a $9.7B Microsoft/Dell enterprise software agreement (May 28, unrelated to minerals), the $191M Solid Rocket Motor Industrial Base investment (May 15 — solid rocket motors, NOT critical minerals; the specific DPA Title III piece was only $27.3M), and various personnel/diplomatic readouts. None concerned a new critical minerals offtake agreement or investment exceeding $100 million [1bcee5][2b2713][ea2841].

2. **Recent DoD critical-mineral deals fall OUTSIDE the window or BELOW threshold:**
   - The $245M US Antimony DLA contract was announced September 23, 2025 — far outside the window [4eda79].
   - The Lynas rare-earth oxide deal (~US$96M / A$137M) was announced March 16, 2026 — outside the window AND below the $100M threshold (the upper bound is $96M USD) [771565].
   - The Korea Zinc $7.4B smelter JV (DoD 40% stake) was announced December 15, 2025 — outside the window [16fa3d].
   - MP Materials ($400M+) was July 2025; USA Rare Earth ($1.6B) and ReElement (~$620M/$80M) deals trace to January–November 2025 / earlier. Bloomberg reported May 21, 2026 that the Pentagon was actually weighing scrapping an $80M (below threshold) conditional loan to ReElement — i.e., not a new $100M+ commitment [16fa3d].
   - Guardian Metal Resources received only $6.2M with a pending $100M+ application (an unfunded request, not an awarded agreement) [4eda79][72d5ed].

3. **Reuters coverage (May 27, 2026)** reviewing the defense-mining investment landscape reported no new $100M+ DoD critical minerals offtake/investment announced during the May 2026 window [72d5ed].

The DIBC critical minerals RPP (RPP-CM-26-01, issued Feb 27, 2026) had project agreements still in "Closed-Awaiting Award" status as of late May 2026, with no award announcement made within the window.

Since no new offtake agreement or investment related to critical minerals with a total stated value exceeding $100 million was announced by DoD (or an entity acting on its behalf) between 00:00 UTC May 1, 2026 and 23:59 UTC June 1, 2026, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-32. `8758751a-d682-598a-bd20-6b94b89ace13`

- Present date: `2026-05-16 11:46:59.618618`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the PBoC announce a cut to the Reserve Requirement Ratio (RRR) between May 12, 2026 and July 1, 2026?

**Resolution criteria**

This question resolves YES if the People's Bank of China (PBoC) officially announces a reduction in the Reserve Requirement Ratio (RRR) for any class of depository institutions, with the announcement occurring on or after May 12, 2026 (00:00 CST, i.e., UTC+8) and no later than July 1, 2026 (23:59 CST). The cut does not need to take effect within this window — only the official announcement must fall within it.

The announcement must be verifiable via the official PBoC website (http://www.pbc.gov.cn/) or through credible reporting by major financial news outlets such as Reuters (https://www.reuters.com), Bloomberg, or the Financial Times.

If no such announcement is made within this timeframe, the question resolves NO.

To be clear: any RRR cut announced before May 12, 2026 does not count toward resolution, even if it takes effect during the resolution window.

**Pre-cutoff background**

The Reserve Requirement Ratio (RRR) is the percentage of deposits that commercial banks must hold as reserves with the central bank, rather than lending out (https://en.wikipedia.org/wiki/Reserve_requirement). A "cut" refers to the PBoC officially announcing a reduction in this ratio for any class of financial institutions.

The People's Bank of China (PBoC) uses RRR adjustments as a key monetary policy tool to manage liquidity in the banking system. As of April 2026, the weighted average RRR for financial institutions stands at approximately 6.2% [China Reserve Requirement Ratio, 1985 – 2026 | CEIC Data](https://www.ceicdata.com/en/indicator/china/reserve-requirement-ratio). In January 2026, the average RRR was reported at 6.3% [China Reserve Requirement Ratio, 1985 – 2026 | CEIC Data](https://www.ceicdata.com/en/indicator/china/reserve-requirement-ratio), and PBoC Governor Pan Gongsheng stated the PBoC would continue implementing a "moderately loose" monetary policy in 2026, utilizing RRR cuts and interest rate reductions to ensure sufficient liquidity.

The most recent RRR adjustment prior to this question's window was a 50 basis point cut announced on May 7, 2025, effective May 15, 2025, as part of a broader easing package ahead of US-China trade talks [China unveils fresh monetary policy easing package ahead of this ...](https://think.ing.com/articles/china-unveils-fresh-monetary-policy-easing-package-ahead-of-this-weeks-trade-talks/). Since then, the RRR has been reduced further, reaching 6.2% by April 2026 [China Reserve Requirement Ratio, 1985 – 2026 | CEIC Data](https://www.ceicdata.com/en/indicator/china/reserve-requirement-ratio).

The PBoC has pledged further RRR and interest rate cuts in 2026 to support economic growth. However, the timing of any additional cut within the specific May 12–July 1 window is uncertain, as the PBoC must balance growth support against inflation risks, bank margin pressures, and external shocks. RRR cuts are a distinct tool from benchmark rate changes and are often used as a first step before or instead of rate cuts.

Official PBoC policy announcements can be found at: http://www.pbc.gov.cn/en/3688229/3688335/3730270/index.html

**Exact later resolution packet**

RESOLUTION: NO (0)

The question resolves YES only if the PBoC officially announced a reduction in the Reserve Requirement Ratio (RRR) for any class of depository institutions, with the ANNOUNCEMENT falling on/after May 12, 2026 (00:00 CST) and no later than July 1, 2026 (23:59 CST). No such announcement was made.

EVIDENCE THAT NO RRR CUT WAS ANNOUNCED IN THE WINDOW:

1. China's cash reserve ratio for large banks remained UNCHANGED at 7.50% in May 2026, per Trading Economics [China Reserve Requirement Ratio for Large Banks](https://tradingeconomics.com/china/cash-reserve-ratio) (https://tradingeconomics.com/china/cash-reserve-ratio). A cut would necessarily change this figure; it did not move.

2. Reuters (June 17, 2026, "China central bank's deepening control on short-term rates sparks debate over policy," https://www.reuters.com/world/asia-pacific/china-central-banks-deepening-control-short-term-rates-sparks-debate-over-policy-2026-06-17/) reported the PBoC was deepening control over short-term money markets by tying overnight borrowing costs to its 7-day reverse repo rate — NOT an RRR cut. The analysis explicitly noted these operations would not change interest rate levels via RRR [China central bank's deepening control on short-term rates ... - Reuters](https://www.reuters.com/world/asia-pacific/china-central-banks-deepening-control-short-term-rates-sparks-debate-over-policy-2026-06-17/). A Reuters social post summarizing this coverage stated "The PBOC's recent comments rule out an RRR or rate cut in the near term."

3. Instead of an RRR cut, in late June 2026 (June 25–30) the PBoC introduced a NEW overnight reverse repo liquidity tool (rate 1.25%) to manage month-end liquidity — reported by Reuters (e.g., "China debuts overnight reverse repos at 1.25%," 2026-06-29) and Bloomberg (2026-06-29). This distinct liquidity tool is not an RRR reduction.

4. China left its benchmark Loan Prime Rates (LPRs) unchanged for the 13th consecutive month in June 2026 (Reuters, "China keeps lending benchmark LPRs unchanged for 13th month in June," 2026-06-22), consistent with a policy hold, not fresh easing.

5. Analyst positioning corroborated the pause: Bloomberg (April 29, 2026) reported Goldman Sachs removed its call for a 50bp RRR cut in 2026, and a Wiley/Oxford Economics "World Economic Prospects Monthly" (May 2026) stated "We don't expect any policy rate or required reserve ratio (RRR) cuts in 2026."

The most recent actual RRR cut announcements found were the May 7, 2025 cut (effective May 15, 2025) reported by Central Banking [PBoC cuts rates and lowers reserve requirement ratios](https://www.centralbanking.com/central-banks/monetary-policy/7972834/pboc-cuts-rates-and-lowers-reserve-requirement-ratios) and by english.www.gov.cn — well before the window. No PBoC RRR-cut announcement occurred between May 12, 2026 and July 1, 2026.

CONCLUSION: Since the PBoC made no RRR-cut announcement within the resolution window, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-33. `1179a6da-9199-516e-90a7-d881fb0f3a26`

- Present date: `2026-05-02 15:32:03.626648`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the U.S. Department of Education announce a delay to the July 1, 2026 implementation of the PSLF employer eligibility rule before 11:59 PM ET on June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 1, 2026 and before 11:59 PM ET on June 1, 2026, the U.S. Department of Education issues an official announcement indicating that the July 1, 2026 effective date of the PSLF employer eligibility rule (Federal Register Document No. 2025-19729, "William D. Ford Federal Direct Loan Program," available at https://www.federalregister.gov/public-inspection/2025-19729/william-d-ford-federal-direct-loan-program) has been delayed, postponed, or suspended.

A "delay" is defined as any of the following:
1. A formal postponement of the effective date published in the Federal Register;
2. An official press release or statement on ed.gov announcing that the Department will not enforce or implement the rule on July 1, 2026;
3. An official announcement of a non-enforcement policy (i.e., stating the Department will not apply the new employer eligibility criteria despite the rule technically taking effect).

**Court-ordered delays count:** If the Department announces a delay in response to a court order (e.g., a preliminary injunction or permanent injunction), this also qualifies as a "Yes" resolution, provided the Department itself issues an official acknowledgment of the delay via ed.gov or the Federal Register.

If no such official announcement from the Department of Education is made by 11:59 PM ET on June 1, 2026, the question resolves as **No**.

**Resolution sources:**
- U.S. Department of Education news/press releases: https://www.ed.gov/about/news/press-releases
- Federal Register, Department of Education documents: https://www.federalregister.gov/agencies/education-department

**Pre-cutoff background**

On October 30, 2025, the U.S. Department of Education published a final rule titled "William D. Ford Federal Direct Loan Program" (Federal Register Document No. 2025-19729) amending the definition of "qualifying employer" for the Public Service Loan Forgiveness (PSLF) program. The rule excludes organizations deemed to engage in activities with a "substantial illegal purpose" from PSLF eligibility. It is scheduled to take effect on July 1, 2026 [https://www.ed.gov/about/news/press-release/us-department-of-education-announces-final-rule-public-service-loan-forgiveness-protect-american-taxpayers](https://www.ed.gov/about/news/press-release/us-department-of-education-announces-final-rule-public-service-loan-forgiveness-protect-american-taxpayers).

As of mid-April 2026, the rule faces multiple legal challenges from nonprofit organizations, labor unions, and a coalition of Democratic-led state and city governments. Three separate lawsuits have been filed, with plaintiffs seeking summary judgment to block or vacate the rule on a nationwide basis. Hearings on these motions were expected in late April or May 2026. The Department of Education has opposed these motions and has actively defended the rule's legality [New PSLF Rule to Disqualify Employers from Student Loan ...](https://www.studentloanplanner.com/pslf-employer-disqualification-rule-legal-challenges/). Congressional Democrats have also introduced legislation to undo the rule, though passage is unlikely given current political dynamics.

The Department has not announced any delay to the July 1, 2026 effective date as of early May 2026. The administration has shown commitment to the rule, but courts could issue injunctions that force a delay, or the Department could voluntarily postpone implementation in response to litigation pressure [New PSLF Rule to Disqualify Employers from Student Loan ...](https://www.studentloanplanner.com/pslf-employer-disqualification-rule-legal-challenges/).

Key references:
- ED press release: https://www.ed.gov/about/news/press-release/us-department-of-education-announces-final-rule-public-service-loan-forgiveness-protect-american-taxpayers
- Federal Register document: https://www.federalregister.gov/public-inspection/2025-19729/william-d-ford-federal-direct-loan-program
- Litigation overview: https://www.studentloanplanner.com/pslf-employer-disqualification-rule-legal-challenges/

**Exact later resolution packet**

The question resolves NO. It asked whether the U.S. Department of Education would issue an official announcement (via ed.gov or the Federal Register) on or after May 1, 2026 and before 11:59 PM ET on June 1, 2026 indicating that the July 1, 2026 effective date of the PSLF employer eligibility rule (Federal Register Doc. No. 2025-19729, "William D. Ford Federal Direct Loan Program") had been delayed, postponed, or suspended.

Evidence gathered:
- A Forbes article by Adam Minsky dated May 21, 2026 confirmed the Department was still moving forward with the July 1, 2026 implementation, with no court injunction and no ED announcement of any delay [Student Loan Forgiveness Approved For Another 11,500 Borrowers ...](https://www.forbes.com/sites/adamminsky/2026/05/21/student-loan-forgiveness-approved-for-another-11500-borrowers-but-new-rules-could-block-future-relief/).
- A Business Insider article dated May 23, 2026 stated the rule remained set to take effect July 1, 2026; the Senate rejected a Congressional Review Act resolution to overturn the rule on May 20, 2026; and a court hearing was scheduled for June 3, 2026 (after the question's deadline). No injunction had been issued and ED had made no announcement of a delay, postponement, or non-enforcement [Trump's plan to limit student-loan forgiveness for public servants is ...](https://africa.businessinsider.com/news/trumps-plan-to-limit-student-loan-forgiveness-for-public-servants-is-inching-closer/tmnrzcm).
- AASCU Federal Highlights – May 2026 (published ~May 29, 2026) likewise reported only the Senate's failed CRA resolution and did not report any ED announcement delaying the PSLF rule or any court order blocking it [AASCU Federal Highlights - May 2026](https://aascu.org/news/aascu-federal-highlights-may-2026/).
- StudentLoanPlanner (updated April 14, 2026) showed ED actively defending the rule and stating it would be effective July 1, 2026, with summary-judgment motions still pending [https://www.studentloanplanner.com/pslf-employer-disqualification-rule-legal-challenges/](https://www.studentloanplanner.com/pslf-employer-disqualification-rule-legal-challenges/).
- The Civil Rights Litigation Clearinghouse docket for Commonwealth of Massachusetts v. U.S. Department of Education showed the case ongoing with no relief granted and no injunction as of June 2, 2026 [Commonwealth of Massachusetts v. U.S. Department of Education](https://clearinghouse.net/case/47296/).

Since no court issued an injunction by June 1, 2026, and the Department of Education made no formal postponement in the Federal Register, no press release stating it would not enforce/implement on July 1, and no non-enforcement policy announcement, none of the three qualifying "delay" definitions were met within the resolution window (May 1 – June 1, 2026). The relevant court hearing was scheduled for June 3, 2026, after the deadline. The question therefore resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-34. `1ed76e90-dfbe-5bd5-b06b-bf0e9f967cad`

- Present date: `2026-05-03 10:27:18.972766`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the Florida House of Representatives pass the "AI Bill of Rights" by May 31, 2026?

**Resolution criteria**

This question resolves as **Yes** if the Florida House of Representatives passes any bill substantively titled or described as the "Artificial Intelligence Bill of Rights" (i.e., legislation based on SB 482 from the 2026 regular session or its special-session counterparts such as SB 2D, containing core provisions on AI consumer disclosure rights, parental controls, and governmental AI contracting restrictions) by a simple majority floor vote on or after May 2, 2026, and on or before May 31, 2026, at 11:59 PM ET.

This question resolves as **No** if no such bill receives a passing floor vote in the Florida House by that deadline.

"Pass" means a successful recorded floor vote (not merely a committee vote or referral). The passage of an amended or substitute version still counts, provided it retains the "AI Bill of Rights" title or substantially similar consumer-protection AI provisions.

**Primary resolution source:** Official bill tracking on the Florida Legislature website:
- https://www.flsenate.gov (Senate bills)
- https://www.myfloridahouse.gov (House bills and votes)

Secondary sources include credible news reporting from outlets such as the Miami Herald, Florida Politics, or POLITICO Florida.

**Pre-cutoff background**

Governor Ron DeSantis has been pushing for Florida's "Artificial Intelligence Bill of Rights," comprehensive legislation regulating AI use, including provisions on consumer disclosure, parental controls over children's AI usage, data collection restrictions, and governmental contracting requirements for AI providers.

During the 2026 regular session, the Senate passed CS/SB 482 (sponsored by Sen. Tom Leek) by a vote of 35-2 on March 4, 2026, but it died in the House on March 13, 2026, as House Speaker Daniel Perez refused to bring it to a floor vote, preferring federal-level regulation [CS/SB 482: Artificial Intelligence Bill of Rights - Florida Senate](https://www.flsenate.gov/Session/Bill/2026/482).

DeSantis then called a special session (April 28–May 1, 2026) that included the AI Bill of Rights among its agenda items. The Senate again passed a version of the bill (SB 2D) by a vote of 37-1. However, the House once again declined to advance the legislation during the special session.

As of May 2, 2026, the AI Bill of Rights has not passed the Florida House in any form. DeSantis retains the authority to call additional special sessions and has shown willingness to apply political pressure on the House. The question is whether mounting public and gubernatorial pressure will be sufficient to overcome Speaker Perez's resistance during May 2026.

**Exact later resolution packet**

The question asks whether the Florida House of Representatives passed the "AI Bill of Rights" by a simple-majority floor vote between May 2, 2026 and May 31, 2026. The answer is NO.

Key evidence:
- The original regular-session bill, CS/SB 482 ("Artificial Intelligence Bill of Rights"), passed the Senate 35-2 on March 4, 2026, but its official Florida Senate bill page lists its final action as "3/13/2026 House - Died in Messages," confirming the House never passed it during the regular session [43bab1]. (Source: https://www.flsenate.gov/Session/Bill/2026/482)
- DeSantis then called a special session running April 28–May 1, 2026, which included the AI Bill of Rights. The Senate again passed a counterpart bill (SB 2D), but House Speaker Daniel Perez refused to hear or advance the legislation, declaring AI bills "dead in the House" and arguing AI regulation belongs at the federal level [184eaf, 647ab3]. News broke on April 28, 2026 (the first day of the special session) that the House would not take up the bill, effectively killing it [647ab3].
- The special session ended May 1, 2026 — one day before the question's resolution window even opened (May 2). No subsequent House floor vote on the AI Bill of Rights occurred between May 2 and May 31, 2026 [f98009, 93a074].
- The only AI-related measure that became law in this period was SB 484 (data-center regulation), which DeSantis signed May 7, 2026 — a different bill, not the consumer-protection "AI Bill of Rights" with disclosure/parental-control/government-contracting provisions. Reporting explicitly noted "the other plank of his plan, aimed at protecting consumers from AI" (the AI Bill of Rights) was not passed.

Because no successful recorded House floor vote on the AI Bill of Rights (or a substitute retaining its core consumer-disclosure, parental-control, and governmental-contracting provisions) occurred in the May 2–31, 2026 window, the question resolves NO (0). This is a straightforward binary question (not a conditional), so it resolves on the consequent directly.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-35. `60f7e95d-8c28-5a32-8c34-0561f5fec83c`

- Present date: `2026-04-30 12:11:41.196157`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Iran's men's national football team be officially confirmed as withdrawn or excluded from the 2026 FIFA World Cup by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after April 29, 2026 and by 11:59 PM UTC on June 1, 2026, FIFA officially confirms that Iran's senior men's national football team (as defined by FIFA: https://www.fifa.com/en/teams/iran-men) will not participate in the 2026 FIFA World Cup—whether due to Iran's voluntary withdrawal, a FIFA-imposed ban, or any other reason.

This question resolves **No** if, as of 11:59 PM UTC on June 1, 2026, Iran remains officially listed as a participant in the 2026 FIFA World Cup with no confirmed withdrawal or exclusion.

**Key definitions:**
- "Iran" refers to the Iran senior men's national football team (https://en.wikipedia.org/wiki/Iran_national_football_team).
- "Officially confirmed" means an announcement published on FIFA.com (https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026) or an official FIFA media release, or credible major international news sources (e.g., Reuters, BBC Sport, AP) reporting on an official FIFA or Iranian Football Federation communication.
- A mere statement by an Iranian government official without corresponding formal action by Iran's football federation or FIFA does not count.

**Resolution source:** The FIFA World Cup 2026 official page at https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026 and specifically the team listings and any official announcements. Secondary sources include Reuters (https://www.reuters.com/sports/soccer/), BBC Sport (https://www.bbc.com/sport/football), and AP News.

**Pre-cutoff background**

Iran qualified for the 2026 FIFA World Cup through AFC qualification and was drawn into Group B alongside Spain, Turkey, and Ecuador. However, geopolitical tensions between Iran and the United States—which is co-hosting the tournament—have created significant uncertainty about Iran's participation.

As of early 2026, Iran's sports minister Ahmad Donyamali stated that Iran is "not in a position to participate" in the World Cup, and multiple reports indicated Iran was signaling withdrawal [World Cup 2026: Iraq qualify but Iran doubts loom - DW.com](https://www.dw.com/en/world-cup-2026-iraq-qualify-but-iran-doubts-loom/a-76621483). FIFA President Gianni Infantino publicly insisted that "Iran will be at the World Cup," but the Iranian government's position has remained ambiguous, with some officials calling it a "boycott" while others stopped short of a formal withdrawal [World Cup 2026: Iraq qualify but Iran doubts loom - DW.com](https://www.dw.com/en/world-cup-2026-iraq-qualify-but-iran-doubts-loom/a-76621483). Iran has requested that its group-stage matches be moved from the United States to Mexico, but no resolution has been publicly confirmed.

The original seed question asked about Iraq's intercontinental playoff qualification. Iraq defeated Bolivia 2-1 on April 1, 2026 to claim the final World Cup spot [Scores & Fixtures | FIFA World Cup 2026™ Play-Off Tournament](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/qualifiers/play-off-tournament/scores-fixtures), making that question already resolved. Iran's participation status—closely linked to Iraq's original qualification pathway and regional dynamics—remains the key unresolved question in this space.

As of April 29, 2026, there has been no official FIFA announcement confirming Iran's withdrawal or expulsion, nor a definitive confirmation that they will participate. The World Cup begins on June 11, 2026, so a final determination is expected in the coming weeks.

**Exact later resolution packet**

The question resolves NO. It asked whether, on or after April 29, 2026 and by 11:59 PM UTC on June 1, 2026, FIFA would officially confirm that Iran's senior men's national team would NOT participate in the 2026 FIFA World Cup. No such confirmation occurred; the opposite happened — Iran's participation was repeatedly affirmed.

Key evidence:

1. FIFA OFFICIAL TEAM LISTING (the designated primary resolution source): The official FIFA World Cup 2026 teams page (https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/teams) lists "IR Iran" as a qualified, participating team, assigned to Group G, with no indication of withdrawal or exclusion [https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/teams](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/teams). This directly satisfies the question's NO condition (Iran "remains officially listed as a participant ... with no confirmed withdrawal or exclusion").

2. The Iranian Football Federation itself confirmed participation. ESPN reported the federation said Iran would "definitely" take part in the 2026 World Cup [Iran will 'definitely' be at World Cup, but federation lays out concerns](https://www.espn.com/soccer/story/_/id/48724139/iran-definitely-2026-world-cup-federation-lays-concerns), and Anadolu Agency (May 9, 2026) reported the Iran Football Federation officially announced the team would participate, with visa procedures underway and matches scheduled vs New Zealand (June 15), Belgium (June 21), and Egypt (June 26) [Iran confirms participation in 2026 FIFA World Cup in US, Canada ...](https://www.aa.com.tr/en/us-israel-iran-war/iran-confirms-participation-in-2026-fifa-world-cup-in-us-canada-and-mexico/3932627).

3. As late as May 25-26, 2026, CNN reported Iran was still a participant, with FIFA confirming the team's base camp would be in Tijuana, Mexico, with travel to the US on match days — explicitly no withdrawal or exclusion [Iran to commute to World Cup games from Mexico after US refusal ...](https://edition.cnn.com/2026/05/25/sport/iran-mexico-fifa-world-cup-2026-intl-hnk). The Guardian (May 23, 2026) likewise reported Iran still scheduled to play and cited FIFA President Infantino's repeated insistence (as recently as April 30, 2026) that "Iran will be at the World Cup" [Iran say Fifa has approved World Cup base camp switch from US to ...](https://www.theguardian.com/football/2026/may/23/iran-world-cup-base-camp-tijuana-mexico-tuscon-war).

4. Per the resolution criteria, statements by Iranian government officials (e.g., the sports minister) signaling a possible "boycott" do NOT count without a corresponding formal action by Iran's football federation or FIFA. No such formal withdrawal action occurred; instead the federation formally confirmed participation [Iran will 'definitely' be at World Cup, but federation lays out concerns](https://www.espn.com/soccer/story/_/id/48724139/iran-definitely-2026-world-cup-federation-lays-concerns) [Iran confirms participation in 2026 FIFA World Cup in US, Canada ...](https://www.aa.com.tr/en/us-israel-iran-war/iran-confirms-participation-in-2026-fifa-world-cup-in-us-canada-and-mexico/3932627).

Conclusion: Within the window (April 29 – June 1, 2026), there was NO official FIFA confirmation of withdrawal/exclusion. Iran remained officially listed as a participant on FIFA.com [https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/teams](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/teams), and both FIFA and the Iranian Football Federation affirmed participation [Iran will 'definitely' be at World Cup, but federation lays out concerns](https://www.espn.com/soccer/story/_/id/48724139/iran-definitely-2026-world-cup-federation-lays-concerns) [Iran confirms participation in 2026 FIFA World Cup in US, Canada ...](https://www.aa.com.tr/en/us-israel-iran-war/iran-confirms-participation-in-2026-fifa-world-cup-in-us-canada-and-mexico/3932627) [Iran to commute to World Cup games from Mexico after US refusal ...](https://edition.cnn.com/2026/05/25/sport/iran-mexico-fifa-world-cup-2026-intl-hnk) [Iran say Fifa has approved World Cup base camp switch from US to ...](https://www.theguardian.com/football/2026/may/23/iran-world-cup-base-camp-tijuana-mexico-tuscon-war). The withdrawal was never "formally confirmed" — at most it was earlier "signaled" by government officials. Resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-36. `dab08b7f-71f1-5bc2-bfbe-6fcc9bf104d3`

- Present date: `2026-05-01 18:57:26.439964`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Indonesia announce specific tax rates for nickel exports by June 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after April 30, 2026, and before June 1, 2026 (23:59 UTC), the Indonesian government officially announces the specific tax rate(s) for nickel exports.

A "specific tax rate" is defined as a numerical percentage (e.g., "X% ad valorem") or a fixed monetary value per unit (e.g., "Y USD per metric ton") that will be applied to nickel product exports. General reaffirmations of the intent to tax nickel exports, or statements that rates are "under discussion," do not qualify.

Qualifying announcements must come from an authorized Indonesian government body (e.g., the Ministry of Finance, the President's office, or publication in the official government gazette). The announcement must represent a new, formally enacted regulation or decree — not a restatement of the March 25, 2026 policy approval, which did not include specific rates.

This question resolves NO if no such specific rate announcement is made by the deadline.

Resolution sources: Official Indonesian government gazette (https://jdih.kemenkeu.go.id/) or credible reporting from Bloomberg (https://www.bloomberg.com), Reuters (https://www.reuters.com), S&P Global (https://www.spglobal.com), or Mysteel (https://www.mysteel.net).

**Pre-cutoff background**

Indonesia is the world's largest nickel producer, controlling approximately 60% of global supply. The country manages nickel ore production through the Work Plan and Budget (RKAB) system administered by the Ministry of Energy and Mineral Resources (ESDM). As of April 2026, the approved 2026 RKAB nickel production quota stands at approximately 190–200 million wet metric tonnes (wmt), down sharply from the 379 million wmt set for 2025 [FLASH: Indonesia's Minerals and Coal Director General says 2026 ...](https://www.mysteel.net/news/5118741-flash-indonesias-minerals-and-coal-director-general-says-2026-approved-rkab-nickel-production-quota-expected-at-190-200-million-tonnes).

In addition to production quota cuts, the Indonesian government has been tightening control over nickel exports. On March 25, 2026, Bloomberg reported that Indonesian President Prabowo Subianto approved the implementation of export taxes on nickel (and coal). However, as of that date, the specific tax rates had not been finalized, with Finance Minister Purbaya Yudhi Sadewa stating that discussions on the rates were still underway [Nickel Spikes After Indonesia's President Approves Export ...](https://www.bloomberg.com/news/articles/2026-03-25/nickel-spikes-after-indonesia-s-president-approves-export-tax). Indonesia already bans the export of unprocessed nickel ore (in place since 2020), but this new export tax would apply to processed nickel products.

The ESDM also issued Ministerial Decree No. 144, adjusting the nickel ore HPM (benchmark price) formula effective April 15, 2026 [FLASH: Indonesia's Minerals and Coal Director General says 2026 ...](https://www.mysteel.net/news/5118741-flash-indonesias-minerals-and-coal-director-general-says-2026-approved-rkab-nickel-production-quota-expected-at-190-200-million-tonnes). These policy moves reflect Indonesia's broader strategy to maximize domestic value-added processing and support global nickel prices.

**Exact later resolution packet**

The question resolves NO because the Indonesian government did not officially announce a specific nickel export tax rate (a numerical percentage or fixed monetary value per unit) during the resolution window (April 30, 2026 – June 1, 2026). Instead, the available evidence from the question's designated resolution sources shows the policy was repeatedly delayed and remained "under discussion" throughout this period:

- Reuters, May 11, 2026: Indonesia explicitly decided to DELAY its plans to impose higher royalties and export duties on minerals (including nickel). Energy Minister Bahlil Lahadalia said the plan was put on hold to develop a "mutually beneficial formula." No specific rates were announced [d7fbe2]. (https://www.reuters.com/world/asia-pacific/indonesia-delays-plan-impose-higher-royalties-export-duties-minerals-2026-05-11/)

- Reuters, May 13/14, 2026: Confirmed that the government had "delayed planned increases in mineral royalties and export duties while it works on... a fairer formula." No specific tax rates were enacted [0c3f58]. (https://www.reuters.com/world/asia-pacific/chinese-firms-warn-indonesias-nickel-quotas-tax-hikes-threaten-investment-2026-05-13/)

- Reuters, May 20, 2026: Indonesia unveiled a plan to centralize commodity exports through a state agency. President Prabowo stated prices were still to be "formulated," indicating an ongoing process, not a finalized announced rate [0182ff]. (https://www.reuters.com/world/asia-pacific/indonesia-plans-centralise-commodity-exports-through-state-agency-sources-say-2026-05-20/)

- The export/windfall tax had already been postponed in late March 2026 (from the planned April 1, 2026 implementation), per Indonesia Business Post and Mysteel [949515].

The March 25, 2026 approval (cited in the question) did not include specific rates, and the resolution criteria explicitly exclude restatements of that approval and statements that rates are "under discussion." No new formally enacted regulation or decree with a specific numerical percentage or fixed monetary value per ton for nickel exports was announced by any authorized Indonesian government body or reported by Bloomberg, Reuters, S&P Global, or Mysteel during the April 30 – June 1, 2026 window. Therefore the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-37. `ec27a645-8361-5543-a733-f69babdb45cb`

- Present date: `2026-05-14 00:44:29.888806`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-16T00:00:00`

**Question**

Will Reliance Industries file the Draft Red Herring Prospectus (DRHP) for the Jio Platforms IPO with SEBI by June 15, 2026?

**Resolution criteria**

This question resolves as **Yes** if Reliance Industries (or Jio Platforms Ltd.) files a Draft Red Herring Prospectus (DRHP) for the Jio Platforms IPO with the Securities and Exchange Board of India (SEBI) on or after May 12, 2026, and on or before June 15, 2026 (end of business day, 23:59 IST / UTC+5:30).

The primary resolution source is the SEBI official "Draft Offer Documents" filing database: https://www.sebi.gov.in/sebiweb/home/HomeAction.do?doListing=yes&sid=3&ssid=15&smid=11

A filing appearing on this page for Jio Platforms (or a substantially similar entity name under Reliance Industries) constitutes a "Yes" resolution. If no such filing appears by the close of June 15, 2026 IST, the question resolves as **No**.

Secondary confirmation sources include credible financial news outlets such as [Reuters](https://www.reuters.com/), [Bloomberg](https://www.bloomberg.com/), [Livemint](https://www.livemint.com/), or [Economic Times](https://economictimes.indiatimes.com/).

**Pre-cutoff background**

Jio Platforms is the digital and telecom subsidiary of Reliance Industries Limited (RIL), and its planned Initial Public Offering (IPO) is expected to be one of the largest in Indian market history, with valuations estimated between $100–170 billion.

A [Draft Red Herring Prospectus (DRHP)](https://www.investopedia.com/terms/d/drhp.asp) is a preliminary offer document that a company must file with the [Securities and Exchange Board of India (SEBI)](https://www.sebi.gov.in/) before launching an IPO. It contains key financial, operational, and risk-related disclosures for potential investors.

The Jio IPO has experienced multiple delays. Originally targeted for H1 2026, the filing was then expected by March 2026, and subsequently pushed to May 2026. As of May 11, 2026, reports indicate that Reliance has restructured the IPO from an Offer for Sale (OFS) model—where existing shareholders sell their stakes—to a fresh issue model, where the company issues new shares to raise capital [https://www.kotakneo.com/news/market-news/jio-platforms-ipo-fresh-issue-ofs-reliance-industries-july-2026/](https://www.kotakneo.com/news/market-news/jio-platforms-ipo-fresh-issue-ofs-reliance-industries-july-2026/). This shift was reportedly driven by pricing disagreements with existing investors who pushed for a higher price band. According to Kotak Neo reporting from May 11, 2026, the company plans to file the DRHP "within a week or fortnight" [https://www.kotakneo.com/news/market-news/jio-platforms-ipo-fresh-issue-ofs-reliance-industries-july-2026/](https://www.kotakneo.com/news/market-news/jio-platforms-ipo-fresh-issue-ofs-reliance-industries-july-2026/).

Despite this stated timeline, the IPO's history of repeated delays introduces genuine uncertainty about whether the filing will occur by mid-June 2026. The restructuring to a fresh issue model requires significant changes to the DRHP documentation, which could introduce further delays.

**Exact later resolution packet**

RESOLUTION: NO (0).

The question resolves YES only if Jio Platforms Ltd / Reliance Industries filed a DRHP with SEBI between May 12, 2026 and June 15, 2026 (inclusive, 23:59 IST). The DRHP WAS filed, but on **June 19, 2026** — four days AFTER the deadline. Therefore the question resolves NO.

KEY EVIDENCE (all consistent, from multiple independent sources found via Google):

1. SEBI's own "Draft Offer Documents filed with SEBI" database — the designated primary resolution source — lists the filing in its "jun-2026" folder, dated "Jun 19, 2026": "Jio Platforms Ltd - DRHP / Jio Platforms Ltd - Abridged Prospectus. Jun 19, 2026. Public Issues: Draft Offer Documents filed with SEBI." URL: https://www.sebi.gov.in/filings/public-issues/jun-2026/jio-platforms-ltd-drhp_102248.html (the DRHP PDF is at https://www.sebi.gov.in/sebi_data/commondocs/jun-2026/Jio%20Platforms%20Ltd_p.PDF).

2. Zee Business explicitly quotes the filing statement: "Jio Platforms Limited (JPL) has today, i.e., June 19, 2026, filed the Draft Red Herring Prospectus ('DRHP') with the Securities and Exchange..." URL: https://www.zeebiz.com/markets/ipo/news-jio-platforms-files-drhp-for-ipo-plans-fresh-issue-of-27-crore-shares-397583

3. The filing was announced by Mukesh Ambani at Reliance's 49th AGM held on June 19, 2026, and executed the same day. Corroborating headlines: Deccan Herald "Jio Platforms gets board approval for 27 crore share sale; to file IPO papers on June 19" (https://www.deccanherald.com/business/jio-platforms-gets-board-approval-for-27-crore-share-sale-to-file-ipo-papers-on-june-19-4044944); Business Standard "RIL AGM: Reliance board approves Jio IPO; DRHP to be filed today with Sebi" dated 19-Jun-2026 (https://www.business-standard.com/companies/news/ril-agm-reliance-board-approves-jio-ipo-drhp-to-be-filed-today-with-sebi-126061900615_1.html); India Today (2026-06-19) "Mukesh Ambani announced at Reliance's 49th AGM that Jio Platforms will file its DRHP with Sebi today"; Business Upturn "Jio Platforms IPO DRHP filed June 19, 2026."

ENTITY & DOCUMENT-TYPE CHECKS (satisfied but irrelevant to outcome because of timing): The filer is Jio Platforms Limited, the digital arm of Reliance Industries — exactly the entity named in the question. The document is a genuine Draft Red Herring Prospectus (a pure fresh issue of up to 27 crore / 270,000,000 equity shares of face value Rs 10). These confirm the filing is the correct type and entity, but it fell outside the required window.

TIMING CONCLUSION: June 19, 2026 > June 15, 2026 (the last eligible day, 23:59 IST). No DRHP for Jio Platforms appeared in SEBI's database on or before June 15, 2026. Hence the resolution is NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-38. `7c1af7e2-2451-5e22-b3a1-ef809bbb2331`

- Present date: `2026-05-16 10:34:13.011260`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will a bill to remove the 'grandchild clause' from Israel's Law of Return pass a preliminary reading in the Knesset by July 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after May 12, 2026 and by July 1, 2026 (23:59 UTC), the Knesset plenum passes a bill to remove or substantially narrow the 'grandchild clause' from Israel's Law of Return in a **preliminary reading** (Hebrew: קריאה טרומית, kri'a tromit).

**Key definitions:**

- **'Grandchild clause'**: The provision in Amendment No. 2 (1970) to the Law of Return that extends immigration eligibility to the grandchildren of Jews, even if they are not themselves Jewish. See: https://en.wikipedia.org/wiki/Law_of_Return#Amendment_no._2 and https://en.idi.org.il/articles/47418

- **Preliminary reading (kri'a tromit)**: The initial vote on a private member's bill in the Knesset plenum, where the sponsoring MK presents the bill, a debate is held, and the plenum votes on whether to refer the bill to a committee for preparation for first reading. This is described in the Knesset Rules of Procedure (https://main.knesset.gov.il/EN/activity/Documents/RulesOfProcedure/ChapterG1.pdf) and on the Knesset legislative process page (https://m.knesset.gov.il/en/activity/pages/legislation.aspx). Government-sponsored bills skip this stage; only private member bills require it.

- **Law of Return**: Israeli law passed July 5, 1950, granting Jews the right to immigrate to Israel. See: https://en.wikipedia.org/wiki/Law_of_Return and https://www.gov.il/en/pages/the-law-of-return

**Resolution source:** Official Knesset voting records available at https://main.knesset.gov.il/EN/activity/Pages/VoteSearch.aspx or the Knesset bills database at https://main.knesset.gov.il/EN/activity/Pages/AllLegislation.aspx. If a vote occurs, it will also be reported by credible media outlets such as the Times of Israel (https://www.timesofisrael.com), Haaretz, or the Jerusalem Post.

The question resolves NO if no such preliminary reading vote passes by July 1, 2026. A vote that is held but fails (as occurred on July 16, 2025) does not count—the bill must pass the preliminary reading.

**Pre-cutoff background**

Israel's Law of Return (https://en.wikipedia.org/wiki/Law_of_Return), passed in 1950 and amended in 1970, grants Jews and their descendants the right to immigrate to Israel and obtain citizenship. The 1970 amendment introduced the 'grandchild clause,' which extends immigration eligibility to anyone with at least one Jewish grandparent, even if that person is not themselves Jewish (https://en.idi.org.il/articles/47418).

Multiple legislative attempts have been made to repeal or narrow this clause. On July 16, 2025, a bill proposed by MK Avi Maoz (Noam Party) to remove the grandchild clause was defeated 18-54 in a preliminary reading (kri'a tromit) in the Knesset plenum. Despite support from ultra-Orthodox (Haredi) parties—who broke their legislative boycott to vote in favor—the bill failed due to opposition from Likud and other coalition factions.

The governing coalition holds approximately 67 of the Knesset's 120 seats, but internal divisions—particularly between Religious Zionism/Haredi parties who support the change and Likud members who oppose it—have prevented passage. Elections are scheduled for no later than October 27, 2026, and political dynamics are shifting, with Bennett and Lapid announcing a new joint party in April 2026.

In early 2026, the coalition revived the effort, with the Ministerial Legislation Committee debating a new version of the bill. Most coalition parties were reportedly expected to support rescinding the grandchild clause. However, as of May 13, 2026, no new preliminary reading vote has taken place in the Knesset plenum on this bill. The political environment remains volatile, with upcoming elections potentially affecting legislative priorities.

**Exact later resolution packet**

The question resolves NO. No bill to remove or narrow the 'grandchild clause' of Israel's Law of Return passed a preliminary reading (kri'a tromit) in the Knesset plenum between May 12, 2026 and July 1, 2026 (23:59 UTC).

Evidence:

1) Official Knesset "News from the Knesset Plenum" page (m.knesset.gov.il/en/activity/pages/plenumnews.aspx), which lists all plenum legislative actions in the relevant period, records no preliminary-reading approval of any Law of Return / grandchild-clause bill. The only preliminary reading it lists in this window is the "Basic Law Proposal: Torah Study" (approved in preliminary reading June 10, 2026), plus first-reading approval of the Knesset dissolution bill — neither relates to the grandchild clause [News from the Knesset Plenum](https://m.knesset.gov.il/en/activity/pages/plenumnews.aspx).

2) The overriding political context is that during this window the Knesset was moving toward dissolution and early elections, not advancing the grandchild-clause bill. The Times of Israel (article dated June 2, 2026) reports the Knesset voted 106-0 in first reading on June 1, 2026 to dissolve itself, with elections targeted between September 8 and October 20, 2026; the article about legislative activity in this period makes no mention of any grandchild-clause vote [MKs advance bill to dissolve Knesset and potentially move up ...](https://www.timesofisrael.com/mks-advance-bill-to-dissolve-knesset-and-potentially-move-up-elections-to-september/).

3) Contemporaneous July 1, 2026 news coverage from the resolution-source outlets contains no report of such a vote: Jerusalem Post article-901070 (July 1, 2026, on a High Court ruling) [https://www.jpost.com/israel-news/politics-and-diplomacy/article-901070](https://www.jpost.com/israel-news/politics-and-diplomacy/article-901070), Jerusalem Post article-901106 (July 1, 2026, on President Herzog's Romania address) [https://www.jpost.com/israel-news/article-901106](https://www.jpost.com/israel-news/article-901106), and the Times of Israel July 1, 2026 liveblog [Likud said to weigh residency, not citizenship, for 'grandchild clause ...](https://www.timesofisrael.com/likud-said-to-weigh-residency-not-citizenship-for-grandchild-clause-immigrants/) — none report a grandchild-clause preliminary reading.

4) The Jerusalem Post's coverage of the coalition effort indicated the bill was "unlikely to advance in the near future," with the Knesset heading into recess until October [Israel debates repealing Law of Return's Grandchild Clause](https://www.jpost.com/israel-news/politics-and-diplomacy/article-860177).

5) The question's own description confirms that as of May 13, 2026 no new preliminary reading vote had taken place; nothing in any authoritative source (Knesset plenum records, Knesset voting records, Times of Israel, Haaretz, Jerusalem Post) indicates a passing preliminary-reading vote occurred before the July 1, 2026 deadline.

Per the resolution criteria, the question resolves NO if no such preliminary reading vote passes by July 1, 2026. Since none occurred/passed, the resolution is 0 (NO).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-39. `4eb17908-c440-599b-ae0f-516c6d773f9f`

- Present date: `2026-05-15 17:56:45.276485`
- Source cutoff boundary: `2026-05-16` (encodes end of UTC day `2026-05-15`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the STF Plenary lift the suspension of Brazil's Dosimetria Law (ADI 7966/7967) before July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 and by 11:59 PM Brasília Time (UTC-3) on July 1, 2026, the STF fully lifts the suspension of Law 15.402/2026 (the Dosimetria Law) that was imposed by Justice Moraes's monocratic decision of May 9, 2026 in ADI 7966/7967. Specifically:

1. **What counts as lifting:** The suspension must be fully revoked or overturned, allowing the law to be applied to January 8 defendants. A decision by the full STF Plenary (Plenário) explicitly lifting, revoking, or overturning the injunction qualifies. A monocratic decision by Justice Moraes himself revoking his own injunction also qualifies.

2. **What does NOT count:** A partial modification of the injunction that still restricts application of the law to January 8 defendants does NOT count as "Yes." A declaration that the law is unconstitutional (thereby nullifying it) does NOT count as "Yes." If the Plenary upholds the suspension or no decision is reached by the deadline, the question resolves **No**.

3. **Exclusion of prior events:** The initial suspension on May 9, 2026 is excluded; only actions on or after May 12, 2026 are relevant for resolution.

**Resolution source:** The official STF procedural tracking system at https://portal.stf.jus.br/ for ADI 7966 and ADI 7967, or the Diário de Justiça Eletrônico (DJe) at https://www.stf.jus.br/portal/diarioJustica/pesquisarDiarioJustica.asp. Credible major Brazilian news outlets (e.g., G1, Folha de S.Paulo, BBC Brasil) may be used as supplementary confirmation.

**Pre-cutoff background**

On May 8, 2026, Brazil's Dosimetria Law (Law 15.402/2026) was promulgated after Congress overrode a presidential veto of PL 2162/2023. The law modified the Penal Code and the Lei de Execução Penal, reducing penalties and expanding sentence reduction mechanisms — critically affecting those convicted for the January 8, 2023 anti-democratic acts (invasion of the Planalto, Congress, and STF buildings) [ADIs 7966 e 7967: o futuro da Lei da Dosimetria - IDPB](https://www.direitopenalbrasileiro.com.br/adis-7966-7967-lei-dosimetria-stf/).

On May 9, 2026, STF Justice Alexandre de Moraes, acting as rapporteur, issued a monocratic (single-justice) injunction suspending the application of Law 15.402/2026 specifically for criminal execution proceedings related to January 8 defendants. The suspension was granted in the context of two Ações Diretas de Inconstitucionalidade (ADIs): ADI 7966 (filed by the Associação Brasileira de Imprensa) and ADI 7967 (filed by the PSOL-Rede federation) [ADIs 7966 e 7967: o futuro da Lei da Dosimetria - IDPB](https://www.direitopenalbrasileiro.com.br/adis-7966-7967-lei-dosimetria-stf/). Moraes cited concerns about legal certainty (segurança jurídica) given the pending constitutional challenges [ADIs 7966 e 7967: o futuro da Lei da Dosimetria - IDPB](https://www.direitopenalbrasileiro.com.br/adis-7966-7967-lei-dosimetria-stf/). He also requested formal statements (manifestações) from the Procuradoria-Geral da República (PGR) and the Advocacia-Geral da União (AGU) before bringing the matter to the full Plenary [STF deve validar Lei da Dosimetria mesmo após suspensão por ...](https://www.cartacapital.com.br/justica/stf-deve-validar-lei-da-dosimetria-mesmo-apos-suspensao-por-moraes/).

As of May 13, 2026, the suspension remains in effect. Some analysts expect the STF to ultimately validate the law, but the timeline for a Plenary decision is uncertain [STF deve validar Lei da Dosimetria mesmo após suspensão por ...](https://www.cartacapital.com.br/justica/stf-deve-validar-lei-da-dosimetria-mesmo-apos-suspensao-por-moraes/). The STF Plenary must review the monocratic injunction, but procedural steps (PGR/AGU manifestations, scheduling) could delay this significantly. The court's composition includes justices appointed by different presidents with divergent views on the January 8 cases.

STF procedural tracking for these cases is available at: https://portal.stf.jus.br/processos/detalhe.asp?incidente=6759001 (ADI 7966).

**Exact later resolution packet**

The question resolves NO. The suspension of Brazil's Lei da Dosimetria (Law 15.402/2026), imposed by Justice Alexandre de Moraes's monocratic injunction of May 9, 2026, was NOT fully lifted by the STF Plenary or by Moraes himself at any point between May 12, 2026 and 11:59 PM Brasília Time on July 1, 2026. Instead, the plenary judgment of ADI 7966/7967 was postponed to August 2026 — after the resolution deadline.

Key evidence:

1) DECISIVE SOURCE — G1 (Globo), published July 1, 2026, "Dosimetria, uberização e mais: STF encerra semestre em sessão nesta quarta..." reports that the STF entered its July recess with the Dosimetria case left for the second semester; the court would only resume such judgments in August 2026. As of July 1, 2026, Moraes's May 9 injunction remained in effect and the Plenary had not reviewed or revoked it [464458]. URL: https://g1.globo.com/politica/noticia/2026/07/01/dosimetria-uberizacao-e-mais-stf-encerra-semestre-em-sessao-nesta-quarta-e-casos-de-repercussao-devem-ficar-para-agosto-veja-lista.ghtml

2) Folha de S.Paulo (Brasília Hoje blog), June 18, 2026: as of mid-June the suspension remained in effect; PGR Paulo Gonet submitted a manifestation defending the law's constitutionality, but it was up to rapporteur Moraes to release the case to the Plenary, which he had not done. No lifting occurred [69bcbb]. URL: https://www1.folha.uol.com.br/blogs/brasilia-hoje/2026/06/gonet-defende-lei-que-pode-reduzir-pena-de-bolsonaro-e-diz-ao-stf-que-congresso-tem-autonomia.shtml

3) SBT News/Instagram (dated ~late June): "A validade da Lei da Dosimetria será discutida no plenário do STF a partir de agosto. O caso só será liberado para pauta após o recesso do Judiciário, que começa em 1º de julho." (The case would only be released to the agenda after the recess beginning July 1, with plenary discussion starting in August.) This confirms no plenary decision occurred before the deadline.

4) The IDPB analysis and STF news page (as of May 11, 2026) confirmed the suspension was active and the timeline for a plenary decision was uncertain, still awaiting PGR/AGU manifestations [67c942, 115173].

Both required pathways to YES were checked: (a) a Plenary decision explicitly lifting/revoking the injunction — did not occur (judgment postponed to August); and (b) a monocratic revocation by Moraes of his own injunction — did not occur (as of June 18 he had not even released the case for judgment [69bcbb], and the July 1 G1 report confirms the suspension still stood [464458]). Notably, the AGU had argued the law was unconstitutional (May 19) and Moraes showed no inclination to revoke his suspension.

Since no full lifting of the suspension occurred on or after May 12, 2026 and by 11:59 PM Brasília Time on July 1, 2026, per resolution criterion (2) ("If the Plenary upholds the suspension or no decision is reached by the deadline, the question resolves No"), the question resolves NO.

Official STF procedural tracking URLs for the ADIs (per the question's stated resolution source): ADI 7966 — https://portal.stf.jus.br/processos/detalhe.asp?incidente=6759001 ; the ADIs can also be searched via the DJe at https://www.stf.jus.br/portal/diarioJustica/pesquisarDiarioJustica.asp . (Note: my direct query of the ADI 7966 detail URL returned mismatched/cached content, so resolution relies on the official STF news portal plus major outlets G1 and Folha, which the criteria explicitly permit as confirmation.)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-40. `f9563ff5-0a53-5e56-9496-c35d44a3a20b`

- Present date: `2026-05-01 19:42:08.927194`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will China's Ministry of Foreign Affairs use the term "condemn" (谴责/condemnation) regarding Japan's military activities in the Philippines between April 30 and June 1, 2026?

**Resolution criteria**

This question resolves as **YES** if, on or after April 30, 2026 (00:00 Beijing Time, UTC+8) and no later than June 1, 2026 (23:59 Beijing Time, UTC+8), a transcript or statement published on the official website of the Ministry of Foreign Affairs of the People's Republic of China (https://www.fmprc.gov.cn/mfa_eng/xw/fyrbt/ or https://www.fmprc.gov.cn/eng/xw/fyrbt/) meets ALL of the following criteria:

1. **Contains formal condemnation language:** The English-language transcript uses the word "condemn," "condemnation," "strongly condemn," or "firmly condemn" — OR — the Chinese-language transcript uses "谴责" or "强烈谴责." General expressions of "concern" (关切), "opposition" (反对), "criticism" (批评), or phrases like "urge prudence" or "express dissatisfaction" do NOT qualify.

2. **Explicitly references Japan:** The statement must mention "Japan" or "Japanese" (日本) by name.

3. **Explicitly references Japan's military activities in the Philippines:** The statement must reference Japan's military activities in the context of the Philippines. This includes, but is not limited to: participation in joint military exercises (e.g., Balikatan 2026), naval port calls, troop deployments, military logistics agreements, or defense cooperation activities conducted in or with the Philippines. A general condemnation of Japan's military build-up that does not mention the Philippines does not qualify.

4. **Date determination:** Resolution depends on the date the press conference or statement was delivered (i.e., the date spoken by the spokesperson), NOT the date the transcript was published on the website. All dates are interpreted in Beijing Time (UTC+8).

The question resolves as **NO** if no such statement meeting all four criteria above is published by 23:59 Beijing Time on June 1, 2026.

**Resolution source:** Official MFA spokesperson transcript pages at https://www.fmprc.gov.cn/mfa_eng/xw/fyrbt/ and https://www.fmprc.gov.cn/eng/xw/fyrbt/. If transcripts are delayed in publication, transcripts published up to June 7, 2026 covering press conferences held on or before June 1, 2026 will be accepted.

**Pre-cutoff background**

China's Ministry of Foreign Affairs (MFA) has repeatedly expressed criticism of Japan's expanding military role in the Philippines, particularly in the context of the annual Balikatan exercises. On April 20, 2026, MFA spokesperson Guo Jiakun stated that Japan bears "grave historical responsibilities" toward Southeast Asian countries and urged Japan to "exercise prudence both in words and actions in military and security areas" and stop "flexing muscles around and undermining stability in the region" [Foreign Ministry Spokesperson Guo Jiakun's Regular Press ...](https://www.fmprc.gov.cn/mfa_eng/xw/fyrbt/202604/t20260420_11895636.html). On April 24, 2026, the same spokesperson escalated the rhetoric, characterizing the situation as a "rampant and dangerous spread of neo-militarism in Japan" that poses "real threats," explicitly referencing the U.S.-Philippines joint military drill (Balikatan) as part of a pattern undermining regional peace [Foreign Ministry Spokesperson Guo Jiakun's Regular Press ...](https://www.fmprc.gov.cn/eng/xw/fyrbt/202604/t20260424_11899448.html).

However, China's MFA uses a spectrum of diplomatic language ranging from "expressing concern" (表示关切) and "criticism" (批评) to the much stronger "condemnation" (谴责/强烈谴责). As of April 30, 2026, publicly available MFA transcripts have used terms like "concern," "opposition," and "criticism" regarding Japan-Philippines military cooperation, but have not escalated to formal "condemnation" language in this specific context.

Balikatan 2026, described as the largest iteration of the annual exercise, involves approximately 10,000 U.S. service members along with Japanese forces, and runs through mid-May 2026. Japan's participation includes ground, maritime, and air components. China views this as a destabilizing external military presence in its near abroad.

The primary resolution source is the official English-language press conference transcript page of the Ministry of Foreign Affairs of the People's Republic of China: https://www.fmprc.gov.cn/mfa_eng/xw/fyrbt/ (and the alternative URL https://www.fmprc.gov.cn/eng/xw/fyrbt/).

**Exact later resolution packet**

The question resolves NO. The resolution criteria require the official MFA English transcript to use "condemn/condemnation/strongly condemn/firmly condemn" — OR the Chinese transcript to use "谴责"/"强烈谴责" — directed specifically at Japan's military activities in the Philippines, delivered between April 30 (00:00) and June 1 (23:59) Beijing Time. Explicitly excluded are "concern," "opposition," "criticism," "urge prudence," and "express dissatisfaction."

I examined the two strongest candidate statements within the window:

1) May 6, 2026 — Spokesperson Lin Jian's regular press conference, responding to a China-Arab TV question about Japan's Type 88 missile being fired for the first time during the "Balikatan" (肩并肩) exercise in the Philippines. This is squarely on-topic (Japan + military activity in the Philippines). However, the official MFA English transcript used only: "We urge the Japanese side to deeply reflect on its history of militarist aggression, and honor its commitments and stay prudent in military and security areas," along with language about "neo-militarism" and "grave historical responsibilities." It did NOT use "condemn." The only occurrence of "condemn"/"强烈谴责" in that day's transcript was about Eswatini/Taiwan ("China strongly condemns it" / "中方予以强烈谴责"), unrelated to Japan-Philippines [Foreign Ministry Spokesperson Lin Jian's Regular Press Conference ...](https://www.fmprc.gov.cn/eng/xw/fyrbt/202605/t20260506_11905648.html) [Foreign Ministry Spokesperson Lin Jian's Regular Press Conference ...](https://www.fmprc.gov.cn/eng/xw/fyrbt/202605/t20260506_11905648.html) [2026年5月6日外交部发言人林剑主持例行记者会 - 驻美国大使馆](https://us.china-embassy.gov.cn/chn/lcbt/wjbfyrbt/202605/t20260506_11905572.htm). While Wikipedia paraphrased the May 6 remarks as China having "condemned" the missile test [2025–2026 China–Japan diplomatic crisis - Wikipedia](https://en.wikipedia.org/wiki/2025%E2%80%932026_China%E2%80%93Japan_diplomatic_crisis), this is the editor's paraphrase, not the verbatim transcript wording, and the resolution criteria require the literal word in the MFA transcript.

2) May 29, 2026 — Spokesperson Mao Ning's regular press conference, responding to the Japan-Philippines joint statement (issued during President Marcos's May 28 visit to Japan) announcing GSOMIA military-intelligence talks and maritime delimitation talks. The official MFA English transcript stated: "China strongly deplores and firmly opposes that and has lodged serious protests with both countries," and "China urges Japan and the Philippines to immediately stop any violation..." The Chinese transcript used "强烈不满，坚决反对" (strong dissatisfaction, firm opposition). Neither version used "condemn"/"谴责" [Foreign Ministry Spokesperson Mao Ning's Regular Press ...](https://www.fmprc.gov.cn/eng/xw/fyrbt/202605/t20260529_11921368.html) [2026年5月29日外交部发言人毛宁主持例行记者会 - 常驻联合国代表团](https://un.china-mission.gov.cn/chn/fyrth/202605/t20260529_11921244.htm). Although third-party media (e.g., SCMP, Global Times headline) used the word "condemns," the verbatim spokesperson quote was "strongly deplores and firmly opposes," and "deplore/oppose/dissatisfaction" are explicitly excluded by the criteria ['Illegal, null and void': Chinese FM condemns Japan- ...](https://www.globaltimes.cn/page/202605/1362285.shtml).

The May 28 Mao Ning transcript did not even address Japan-Philippines military cooperation [Foreign Ministry Spokesperson Mao Ning's Regular Press ...](https://un.china-mission.gov.cn/eng/fyrth/202605/t20260528_11919951.htm). No other transcript in the window was found using the required "condemn"/"谴责" wording specifically regarding Japan's military activities in/with the Philippines. Therefore all four criteria are not jointly satisfied, and the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-41. `70297794-e5ee-5a40-9314-bc7086064088`

- Present date: `2026-05-02 21:12:40.297261`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will TAE Technologies or Trump Media & Technology Group file an S-4 registration statement with the SEC between May 1, 2026 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if an S-4 registration statement (or S-4/A amendment) related to the TAE Technologies–Trump Media & Technology Group merger is filed with the U.S. Securities and Exchange Commission on or after May 1, 2026, 12:00 AM ET, and on or before June 1, 2026, 11:59 PM ET. The filing must appear on either TMTG's or TAE Technologies' EDGAR filing page.

This question resolves **No** if no such S-4 filing appears by June 1, 2026, 11:59 PM ET.

**Resolution source:** The [SEC EDGAR full-text search](https://efts.sec.gov/LATEST/search-index?q=%22TAE+Technologies%22&dateRange=custom&startdt=2026-05-01&enddt=2026-06-01&forms=S-4) or the [TMTG SEC filings page](https://ir.tmtgcorp.com/financials/sec-filings/) and [TMTG EDGAR page](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001849635&type=S-4&dateb=&owner=include&count=40).

**Key definitions:**
- [S-4 registration statement](https://www.sec.gov/files/forms-4.pdf): A form filed with the SEC to register securities issued in business combinations (mergers/acquisitions).
- "File": The document is submitted to and accepted by the SEC, as evidenced by its appearance in the [EDGAR database](https://www.sec.gov/edgar/searchedgar/companysearch).

**Pre-cutoff background**

In December 2025, Trump Media & Technology Group (TMTG, Nasdaq/NYSE Texas: DJT) and TAE Technologies announced a definitive merger agreement in an all-stock transaction valued at over $6 billion. The deal would combine TMTG's access to capital markets with TAE's fusion energy technology. Under the terms of the merger agreement, TMTG agreed to provide up to $200 million in cash to TAE at signing, with an additional $100 million available upon the filing of regulatory documents, specifically the S-4 registration statement [https://techcrunch.com/2026/04/19/cracks-are-starting-to-form-on-fusion-energys-funding-boom/](https://techcrunch.com/2026/04/19/cracks-are-starting-to-form-on-fusion-energys-funding-boom/).

As of May 2, 2026, no S-4 registration statement related to this merger has been filed with the SEC. The TMTG investor relations SEC filings page shows no S-4 filing [SEC Filings - Trump Media | IR](https://ir.tmtgcorp.com/financials/sec-filings/), and the SEC EDGAR database for TMTG (CIK 0001849635) does not list a recent S-4 [https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001849635&type=S-4&dateb=&owner=include&count=40](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001849635&type=S-4&dateb=&owner=include&count=40). The transaction is expected to close in mid-2026, subject to shareholder approval, regulatory clearances, and other customary closing conditions. The S-4 filing is a critical prerequisite for holding the shareholder vote.

An [S-4 registration statement](https://www.sec.gov/files/forms-4.pdf) is a filing required by the SEC under the Securities Act of 1933 when companies are registering securities to be issued in connection with business combination transactions such as mergers or acquisitions. "File" means the document is submitted to and accepted by the SEC, as evidenced by its appearance on the [SEC EDGAR](https://www.sec.gov/edgar/searchedgar/companysearch) filing system.

**Exact later resolution packet**

The question resolves NO because no S-4 (or S-4/A) registration statement related to the TAE Technologies–Trump Media & Technology Group (TMTG) merger was filed with the SEC between May 1, 2026, 12:00 AM ET and June 1, 2026, 11:59 PM ET.

Evidence:
- The TMTG EDGAR S-4 filing page (CIK 0001849635) shows no S-4/A filing after 2024-02-14; nothing in the May 2026 window [626278].
- A targeted SEC EDGAR full-text search for "TAE Technologies" restricted to form type S-4 and the date range 2026-05-01 to 2026-06-01 returned zero hits [cd3690]. A broader search for "TAE" with form S-4 in the same window also returned zero hits [72c863].
- A full-text EDGAR search for "TAE Technologies" across ALL form types in the May 1–June 1, 2026 window returned filings (Form 425 business-combination communications, 8-K, 10-Q), but no S-4 or S-4/A [8703ec].
- The TMTG Investor Relations SEC filings page lists the company's May 2026 filings as Forms 144, 4, 3, 8-K, and 425 — no S-4 or S-4/A appears [cf020e].

Although TMTG repeatedly stated its intent to file a Form S-4 in connection with the merger (per 425 communications), the actual S-4 had not been filed during the resolution window. The resolution criteria specify the question resolves NO if no such S-4 filing appears by June 1, 2026, 11:59 PM ET, which is the case.

Direct sources:
- TMTG EDGAR S-4 page: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001849635&type=S-4&dateb=&owner=include&count=40
- EDGAR full-text search (S-4, TAE, window): https://efts.sec.gov/LATEST/search-index?q=%22TAE+Technologies%22&forms=S-4&startdt=2026-05-01&enddt=2026-06-01
- TMTG IR filings: https://ir.tmtgcorp.com/financials/sec-filings/

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-42. `72756beb-1bb9-55ae-a234-0db387e40c56`

- Present date: `2026-05-15 11:28:24.361846`
- Source cutoff boundary: `2026-05-16` (encodes end of UTC day `2026-05-15`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will NTT DOCOMO announce a price increase for any of its primary consumer mobile plans (eximo, ahamo, or irumo) between May 12, 2026 and July 1, 2026?

**Resolution criteria**

This question resolves **YES** if NTT DOCOMO publishes an official announcement on or after May 12, 2026, and no later than 23:59 JST (Japan Standard Time, UTC+9) on July 1, 2026, stating that the monthly base fee for any of its primary consumer mobile plans will increase.

**Definitions:**
- **Primary consumer mobile plans** are defined as: **eximo**, **ahamo** (including ahamo Oomori and ahamo poikatsu variants), and **irumo** — the three branded plan tiers listed on NTT DOCOMO's official charges page (https://www.docomo.ne.jp/english/charge/) [Charges | NTT DOCOMO](https://www.docomo.ne.jp/english/charge/).
- **Price increase** means an increase in the standard monthly recurring base fee (the advertised tax-included monthly charge) for an existing plan tier. This excludes: changes to data overage charges only, changes to one-time fees (e.g., activation or shop consultation fees), changes to optional add-on pricing, and expiration of limited-time promotional discounts. However, if an existing plan is discontinued and replaced by a successor plan at a higher base price, this counts as a price increase.
- The announcement must occur **on or after May 12, 2026** to exclude any prior announcements. The price increase itself does not need to take effect before July 1, 2026; only the official announcement must occur within the window.

**Resolution source:** NTT DOCOMO's official press release page at https://www.docomo.ne.jp/english/info/media_center/pr/ or the Japanese-language equivalent at https://www.docomo.ne.jp/info/news_release/. If the announcement appears on DOCOMO's official website but not on the press release page specifically, it still counts.

If no such announcement is made by 23:59 JST on July 1, 2026, the question resolves **NO**.

**Pre-cutoff background**

NTT DOCOMO is one of Japan's largest mobile network operators, offering three tiers of consumer mobile plans: eximo (premium, ¥4,565–¥7,315/month), ahamo (mid-range, ¥2,970/month for 30 GB), and irumo (budget, ¥550–¥3,377/month) [Charges | NTT DOCOMO](https://www.docomo.ne.jp/english/charge/). Japanese mobile pricing has historically been subject to government pressure to keep costs low for consumers.

On May 8, 2026, NTT DOCOMO President Yoshiaki Maeda stated during an earnings briefing that the company is considering revisions to its "overall rate structure," explicitly mentioning ahamo, which has maintained its ¥2,970 monthly fee since its 2021 launch [NTT Docomo President Maeda Hints at Price Hikes for ahamo and ...](https://finance.biggo.com/news/g1LhDp4BrX5PFN7BnRaO). The company has delayed its EBITDA target of 4 trillion yen by three years to fiscal 2030, and management described price revisions as becoming "unavoidable" given rising electricity, labor, and infrastructure costs [NTT Docomo President Maeda Hints at Price Hikes for ahamo and ...](https://finance.biggo.com/news/g1LhDp4BrX5PFN7BnRaO). DOCOMO's consumer EBITDA has been under pressure, and competitors such as KDDI (au) have already implemented price increases. The company previously introduced a higher-capacity plan called "docomo MAX" in June 2025 as a de facto per-unit price increase strategy.

Current monthly base prices as of May 12, 2026 (tax included):
- **eximo**: ¥4,565 to ¥7,315/month (usage-tiered)
- **ahamo**: ¥2,970/month (30 GB)
- **ahamo Oomori**: ¥4,950/month (110 GB)
- **irumo**: ¥550 to ¥3,377/month (usage-tiered)

The primary resolution source is NTT DOCOMO's official English-language press release page: https://www.docomo.ne.jp/english/info/media_center/pr/

**Exact later resolution packet**

The question resolves NO. It required NTT DOCOMO to publish an official announcement, on or after May 12, 2026 and no later than 23:59 JST on July 1, 2026, stating that the monthly base fee for one of its primary consumer mobile plans (eximo, ahamo including ahamo Oomori/poikatsu, or irumo) will increase. No such announcement was made.

Evidence:

1) Official English press release page (https://www.docomo.ne.jp/english/info/media_center/pr/): Reviewing all releases in the window (June 22, June 12, May 27, May 25 x2), none concern a price increase for the specified consumer mobile plans; they cover network technology, a new management team, agriculture/6G demonstrations, etc. [937084]

2) Official Japanese news release page (https://www.docomo.ne.jp/info/news_release/year.html?year=2026): The full list of releases from May 12 to July 1, 2026 contains no base-fee increase for eximo, ahamo, or irumo. The only fee-related release, dated May 15, 2026, concerns "mopera U" (「mopera U Uスタンダードプラン」提供終了ならびに「mopera U シンプルプラン」の月額料金改定) — mopera U is an ISP/internet-connection add-on service, NOT one of the primary consumer mobile plans defined in the question. The June 5, 2026 release "「JALモバイル powered by ahamo」を提供開始" explicitly keeps ahamo's fee unchanged at ¥2,970/month (30GB). [98435b]

3) Context confirming DOCOMO had NOT committed to a mobile base-fee hike: Business Insider Japan (published May 11, 2026, updated May 20, 2026) reports that DOCOMO President Maeda only stated the company is "considering" revisions and that a price increase is not yet decided; it notes SoftBank (not DOCOMO) announced a July 2026 increase. [cc2289]

4) BizPLUS (updated June 6, 2026) states ahamo has "no planned price increase" (既存プラン値上げ予定なし) as of June 2026. The July 1, 2026 increases referenced in various search results are SoftBank/Y!mobile, not DOCOMO. DOCOMO's only fee changes in this period were: docomo Hikari/ahamo Hikari construction (one-time) fees rising June 1, 2026; a Plala Hikari→docomo Hikari fixed-line integration (+¥440); and the "Itsudemo Kaedoki Program" device-return fee — none of which are monthly base fees of eximo/ahamo/irumo. [a10c38]

The "July 2026 price increase" hits in search results attribute to SoftBank/Y!mobile [cc2289, a10c38], not DOCOMO. The docomo Hikari/ahamo Hikari changes are one-time construction fees on a fixed fiber-optic product (explicitly excluded by the resolution criteria, which exclude one-time fees, and are not mobile plans anyway). The mopera U change is an add-on ISP service, not a primary consumer mobile plan.

Note on the "successor plan" clause: eximo→docomo MAX and irumo→docomo mini replacements occurred in June 2025, well before the May 12, 2026 window, so they do not count.

Therefore, no qualifying announcement occurred within the window, and the question resolves NO (0).

Sources:
- https://www.docomo.ne.jp/english/info/media_center/pr/
- https://www.docomo.ne.jp/info/news_release/year.html?year=2026
- https://www.businessinsider.jp/article/2605-ntt-docomo-profit-drop-network-investment/
- https://bizplus.jp/mobile/docomo-plan-price-up/

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-43. `f0011a23-22b3-550c-adc4-b233fd79a574`

- Present date: `2026-04-30 00:06:51.336905`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Google officially announce a model named 'Gemini 4' or 'Gemini 4.0' by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if Google officially announces a model with the name "Gemini 4," "Gemini 4.0," or any variant that includes "Gemini 4" in its name (e.g., "Gemini 4 Pro," "Gemini 4 Flash," "Gemini 4 Ultra," "Gemini 4.0 Pro") on or after the question's open date and on or before June 1, 2026, at 11:59 PM UTC.

An "official announcement" is defined as any of the following:
1. A verbal announcement by a Google representative during a keynote or official session (e.g., at Google I/O 2026);
2. A post on an official Google blog, such as The Keyword (https://blog.google/) or the Google DeepMind blog (https://deepmind.google/); or
3. An official press release issued by Google.

The primary resolution sources are:
- The Google Keyword blog: https://blog.google/
- The Google I/O 2026 website: https://io.google/
- The Google DeepMind blog: https://deepmind.google/

If no such announcement is made by June 1, 2026, 11:59 PM UTC, the question resolves **No**. Announcements of models branded differently (e.g., "Gemini 3.5," "Gemini 5") do not count. Leaks, rumors, or unofficial references do not count—only official Google communications qualify.

**Pre-cutoff background**

Google's Gemini model family is the company's flagship large language model series. As of March 2026, the latest released models are Gemini 3.1 Flash-Lite and Gemini 3.1 Flash Live [The latest AI news we announced in March 2026 - Google Blog](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-march-2026/). Google I/O 2026 is confirmed for May 19–20, 2026 (UTC-7, Mountain View, CA). There is widespread speculation that Google may announce Gemini 4 or Gemini 4.0 at Google I/O 2026, but no official confirmation exists. Polymarket has given only ~9% probability to Gemini 4.0 Flash being publicly released by June 30, 2026, though an announcement (without full public release) is a lower bar. The current versioning trajectory (3.1 as of March 2026) leaves open the possibility that Google could announce an incremental update (e.g., Gemini 3.5) rather than jumping to 4.0.

**Exact later resolution packet**

The question asks whether Google officially announced a model named "Gemini 4" or "Gemini 4.0" (or any variant including "Gemini 4") between the question's open date (April 29, 2026) and June 1, 2026, 11:59 PM UTC.

The key event in this window was Google I/O 2026 (May 19–20, 2026), where Google made its major Gemini model announcements. Google's official summary blog post "100 things we announced at I/O 2026" (published May 20, 2026, on blog.google) and the official "Google I/O 2026: News and announcements" collection page (blog.google) both confirm that the new models announced were **Gemini 3.5** (Gemini 3.5 Flash and Gemini 3.5 Pro) and **Gemini Omni** (including Gemini Omni Flash) — NOT Gemini 4 [fde131, cac4fe]. The collection page explicitly states "We're releasing two new models, Gemini Omni and Gemini 3.5." [cac4fe].

No official Google source (blog.google, deepmind.google, io.google, press release, or keynote) announced any model named "Gemini 4" or "Gemini 4.0" within the resolution window. The versioning trajectory went from Gemini 3.1 (March 2026) to Gemini 3.5 (May 2026), consistent with the incremental update path the question itself flagged as a possibility. All references to "Gemini 4" found online (e.g., WaveSpeed AI, YouTube videos) were pre-keynote speculation/rumors, which the resolution criteria explicitly exclude.

Therefore the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-44. `5b13d31d-7672-5d4e-838b-264df5817a7a`

- Present date: `2026-05-01 15:16:37.639666`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the U.S. House of Representatives pass H.R.8170 (the MATCH Act) by June 1, 2026?

**Resolution criteria**

This question resolves YES if H.R.8170 (the MATCH Act) receives a simple majority vote on the floor of the U.S. House of Representatives on or after April 30, 2026, and on or before June 1, 2026, 11:59 PM UTC. Committee approval alone does not count as "passing the House."

This question resolves NO if the bill has not passed a House floor vote by June 1, 2026, 11:59 PM UTC.

The primary resolution source is the official Congress.gov bill tracker for H.R.8170: https://www.congress.gov/bill/119th-congress/house-bill/8170. The "Actions" tab will serve as the definitive record of whether the bill has passed the House. If Congress.gov is unavailable, credible reporting from Reuters, AP, or Bloomberg may be used as a secondary source.

**Pre-cutoff background**

H.R.8170, the Multilateral Alignment of Technology Controls on Hardware (MATCH) Act, was introduced on April 2, 2026, by Rep. Michael Baumgartner (R-WA-5). The bill aims to impose stricter export controls on semiconductor manufacturing equipment destined for certain Chinese entities, including SMIC, Hua Hong, Huawei, CXMT, and YMTC. It was advanced as part of a package of 22 chip export control bills.

On April 22, 2026, the House Foreign Affairs Committee ordered the bill to be reported (in the nature of a substitute, amended) by a vote of 36–8 [https://www.congress.gov/bill/119th-congress/house-bill/8170](https://www.congress.gov/bill/119th-congress/house-bill/8170). A companion version (S.4281) has been introduced in the Senate Foreign Relations Committee.

As of April 30, 2026, the bill has not been scheduled for a House floor vote [https://www.congress.gov/bill/119th-congress/house-bill/8170](https://www.congress.gov/bill/119th-congress/house-bill/8170). While the bill enjoys strong bipartisan support (evidenced by the lopsided committee vote), passing a full House floor vote within roughly five weeks is uncertain. Bills routinely face delays due to competing legislative priorities, scheduling constraints set by House leadership, the need for potential Rules Committee action, and possible amendments or procedural hurdles. Many bills that clear committee never receive a floor vote in the same Congress, let alone within weeks.

**Exact later resolution packet**

The question asks whether the U.S. House of Representatives passed H.R.8170 (the MATCH Act, 119th Congress) on a full floor vote between April 30, 2026 and June 1, 2026, 11:59 PM UTC. The primary resolution source is the official Congress.gov bill tracker (https://www.congress.gov/bill/119th-congress/house-bill/8170).

Per the Congress.gov "All Info"/Actions record for H.R.8170, the most recent action on the bill was on April 22, 2026, when the House Committee on Foreign Affairs "Ordered to be Reported in the Nature of a Substitute (Amended) by the Yeas and Nays: 36 - 8." No subsequent action exists — there is NO record of a full House floor vote ("Passed/agreed to in House") [fe71a9]. The independent GovTrack.us tracker corroborates this, listing only two actions: "Introduced" (April 2, 2026) and "Ordered Reported" (April 22, 2026), with the bill's status remaining "Ordered Reported" as of June 2, 2026 [cc607a].

The committee action ("ordered to be reported") is explicitly distinguished from a full House floor vote in the resolution criteria, which state that "Committee approval alone does not count as 'passing the House.'" Since no floor vote occurred within (or even after) the April 30 – June 1, 2026 window, the consequent did not occur.

Therefore the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-45. `0e804a1b-4785-5fce-8f74-048fe941ac52`

- Present date: `2026-05-12 15:01:12.273900`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will at least one defendant in the Toti vote-trading case ("filone bis") formally conclude a patteggiamento (plea bargain) accepted by the court by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if at least one defendant in the "filone bis" (vote-trading branch) of the Toti investigation formally concludes a patteggiamento (plea bargain under Art. 444 of the Italian Code of Criminal Procedure, https://www.brocardi.it/codice-di-procedura-penale/libro-sesto/titolo-ii/art444.html) that is formally accepted by the court (i.e., a sentence is issued by the GUP or presiding judge ratifying the plea agreement) on or after May 10, 2026, and on or before July 1, 2026 (23:59 UTC).

A "formal conclusion" means a sentence (sentenza) issued by the GUP or judge formally accepting and ratifying the patteggiamento agreement between prosecution and defense, as reported by credible Italian news sources.

This question resolves **No** if no such plea bargain is formally accepted by the court for any defendant in this case branch by July 1, 2026, 23:59 UTC — whether because negotiations fail, the case proceeds to trial (dibattimento), or for any other reason.

**Resolution source:** Credible Italian news reporting from outlets such as [ANSA](https://www.ansa.it/), [Genova24](https://www.genova24.it/), [La Voce di Genova](https://www.lavocedigenova.it/), [GenovaToday](https://www.genovatoday.it/), or [Il Secolo XIX](https://www.ilsecoloxix.it/), confirming formal court acceptance of a patteggiamento for at least one defendant in the vote-trading branch of the investigation.

**Pre-cutoff background**

The Toti corruption investigation in Liguria, Italy, which began with the arrest of former regional president Giovanni Toti in May 2024, has branched into multiple legal proceedings. The primary defendants — Toti, Aldo Spinelli, and Paolo Emilio Signorini — concluded their cases via patteggiamento in December 2024 [Un anno dall'arresto di Giovanni Toti, l'inchiesta che ha sconvolto la ...](https://www.ivg.it/2025/05/un-anno-dallarresto-di-giovanni-toti-linchiesta-che-ha-sconvolto-la-liguria-la-tempesta-giudiziaria-e-le-elezioni/). In April 2025, three additional defendants (Moncada, Amico, Vianello) also requested patteggiamento [Un anno dall'arresto di Giovanni Toti, l'inchiesta che ha sconvolto la ...](https://www.ivg.it/2025/05/un-anno-dallarresto-di-giovanni-toti-linchiesta-che-ha-sconvolto-la-liguria-la-tempesta-giudiziaria-e-le-elezioni/).

A separate branch of the investigation (the "filone bis") concerns alleged vote-trading (voto di scambio) at the 2020 Liguria regional elections. This branch involves approximately 18 defendants, including Matteo Cozzani (Toti's former chief of staff), Venanzio Maurici (a former unionist), the Testa twins (Arturo and Angelo), Stefano Anzalone, Umberto Lo Grasso, and Paolo Piacenza [Voto di scambio, resta l'aggravante mafiosa per Maurici e i gemelli ...](https://www.lavocedigenova.it/2026/04/23/leggi-notizia/argomenti/cronaca-5/articolo/voto-di-scambio-resta-laggravante-mafiosa-per-maurici-e-i-gemelli-testa-udienza-rinviata-al-5-g.html).

Crucially, the prosecution has maintained the aggravante mafiosa (mafia aggravation, per Article 416-bis.1 of the Italian Penal Code) against Maurici and the Testa twins. This aggravation prevents these defendants from accessing messa alla prova (probation/community service) and complicates plea negotiations [Voto di scambio, resta l'aggravante mafiosa per Maurici e i gemelli ...](https://www.lavocedigenova.it/2026/04/23/leggi-notizia/argomenti/cronaca-5/articolo/voto-di-scambio-resta-laggravante-mafiosa-per-maurici-e-i-gemelli-testa-udienza-rinviata-al-5-g.html).

As of April 23, 2026, the GUP (Giudice dell'Udienza Preliminare) Giorgio Morando postponed the preliminary hearing to June 5, 2026, to allow parties to evaluate alternative solutions, including patteggiamento. If no agreement is reached by that date, the case may proceed toward rinvio a giudizio (indictment/trial) [Voto di scambio, resta l'aggravante mafiosa per Maurici e i gemelli ...](https://www.lavocedigenova.it/2026/04/23/leggi-notizia/argomenti/cronaca-5/articolo/voto-di-scambio-resta-laggravante-mafiosa-per-maurici-e-i-gemelli-testa-udienza-rinviata-al-5-g.html).

A **patteggiamento** (formally "applicazione della pena su richiesta delle parti") is a plea bargain procedure under Italian criminal law, governed by [Article 444 of the Italian Code of Criminal Procedure](https://www.brocardi.it/codice-di-procedura-penale/libro-sesto/titolo-ii/art444.html). It requires agreement between prosecution and defense, and must be formally ratified by the judge to take legal effect.

**Exact later resolution packet**

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

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-46. `43502e3a-7715-5a68-acc8-2a7f4cf3006f`

- Present date: `2026-04-30 16:28:26.243408`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the National Preparedness Level be raised to Level 3 or higher between April 30, 2026 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the National Preparedness Level is reported as 3, 4, or 5 at any point on or after April 30, 2026 (00:00 UTC) through the end of the day on June 1, 2026 (23:59 UTC).

This question resolves **No** if the National Preparedness Level does not reach 3 or higher by the end of the day (23:59 UTC) on June 1, 2026.

The resolution source is the official NIFC National Fire News page (https://www.nifc.gov/fire-information/nfn) or the NICC Situation Report (https://www.nifc.gov/nicc/sitreprt.pdf). If neither source is available, credible reporting from federal wildfire agencies or major news outlets confirming a preparedness level change will suffice.

**Pre-cutoff background**

The [National Preparedness Level](https://www.nifc.gov/fire-information/statistics) (NPL) is a scale from 1 to 5 used by the National Interagency Fire Center (NIFC) to indicate the level of wildland fire activity and demand for firefighting resources across the United States. Level 1 indicates minimal activity, while Level 5 indicates the most extreme nationwide fire activity with maximum resource commitment. The level is assessed and updated regularly by the National Interagency Coordination Center (NICC).

As of April 24, 2026, the National Preparedness Level is 2 [https://www.nifc.gov/fire-information/nfn](https://www.nifc.gov/fire-information/nfn). Earlier in the 2026 fire season, the Southern Area Geographic Area reached Preparedness Level 3 due to regional fire activity, but the national level has remained at 2. Whether the national level reaches 3 depends on significant fire activity occurring across multiple geographic areas simultaneously. Late spring is typically a transitional period—prescribed fire season winds down while early-season wildfires may increase depending on drought conditions and weather patterns.

The current national preparedness level is published on the NIFC National Fire News page at https://www.nifc.gov/fire-information/nfn and in the NICC Situation Report at https://www.nifc.gov/nicc/sitreprt.pdf.

**Exact later resolution packet**

The question asks whether the National Preparedness Level (NPL) was raised to Level 3 or higher between April 30, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC).

Evidence gathered:
- The official NICC website (https://www.nifc.gov/nicc), last updated June 1, 2026, reports the current National Preparedness Level as 2 [National Interagency Coordination Center (NICC)](https://www.nifc.gov/nicc).
- The NIFC official X/Twitter account (@NIFC_Fire) posted on May 1, 2026: "National Fire News: 05/01. Fire activity remains light nationwide and the preparedness level remains at 2." (https://x.com/NIFC_Fire)
- NIFC's May 15, 2026 National Fire News Facebook post states the "preparedness level remains at 2, with 118 new fires reported" (https://www.facebook.com/NIFCFire/posts/national-fire-news-may-15-2026-...).
- The NIFC National Fire News page (https://www.nifc.gov/fire-information/nfn) showed NPL 2 (set March 20, 2026), with no increase since.

The Southern Area's regional/Geographic Area Preparedness Level reaching 3 earlier in the season does not count — the question specifically concerns the NATIONAL Preparedness Level. Across the full window (April 30 – June 1, 2026), the National Preparedness Level remained at 2 and never reached 3, 4, or 5. Therefore the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-47. `a983bf40-5c05-5b94-b9d2-65ac640809e3`

- Present date: `2026-05-02 10:29:56.319235`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will at least one of Maersk, MSC, or CMA CGM publicly announce resumption of regular commercial container vessel transits through the Strait of Hormuz by June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 1, 2026 (00:00 UTC) and before June 1, 2026 (23:59 UTC), at least one of the following three companies publicly announces the resumption of regular commercial container vessel transits through the Strait of Hormuz:

- **A.P. Moller-Maersk** (via https://www.maersk.com/news or https://www.maersk.com/press)
- **MSC Mediterranean Shipping Company** (via https://www.msc.com/en/newsroom or https://www.msc.com/en/newsroom/press-releases)
- **CMA CGM Group** (via https://www.cmacgm-group.com/en/news-media)

**Definition of "public announcement":** A post on one of the official corporate websites listed above, or an official company statement reported by major news wires (Reuters: https://www.reuters.com, Bloomberg: https://www.bloomberg.com, or AP News: https://apnews.com). Internal customer advisories published on the companies' official websites also qualify.

**Definition of "regular commercial transits":** The acceptance of new bookings for, or the scheduled deployment of, container vessels on regular service rotations transiting the Strait of Hormuz as part of normal commercial operations. This excludes:
- One-off or ad hoc vessel movements (e.g., repositioning a single stranded ship)
- Military-escorted humanitarian or evacuation convoys
- Trial runs or test transits not accompanied by a resumption of scheduled service
- Transits by vessel types other than container ships operated by the named carriers

The announcement must explicitly indicate a return to scheduled or regular service, not merely acknowledge that an individual vessel has passed through the Strait.

This question resolves as **No** if no such qualifying announcement is made by any of the three carriers before 23:59 UTC on June 1, 2026.

**Pre-cutoff background**

Since late February 2026, the Strait of Hormuz has been effectively closed to most commercial shipping due to a "dual blockade" involving the United States Navy blockading Iranian ports and Iran blockading the Strait itself. As of April 27, 2026, approximately 2,000 ships and 20,000 mariners remain stranded in the Persian Gulf [https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis).

Major container shipping lines—Maersk, MSC, and CMA CGM—have suspended regular transits through the Strait and rerouted vessels around the Cape of Good Hope. A brief opening occurred on April 17, 2026, when Iran announced the Strait would reopen during a truce, but this was reversed on April 18 after the US continued its blockade of Iranian ports; traffic dropped sharply again by April 20 [https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis).

As of Maersk's April 27, 2026 operational update, shipping conditions in and around the Strait remain "constrained," the security situation is described as "unpredictable," and Maersk states that "safe transition of the Strait of Hormuz cannot be assured at this time" [Middle East Situation Overview 4 - Maersk](https://www.maersk.com/news/articles/2026/04/27/middle-east-situation-overview-4). MSC suspended all bookings for worldwide cargo to the Middle East as a precautionary measure. CMA CGM has been "fully mobilized in response to the rapidly evolving situation" and has deployed emergency multimodal solutions for customers in the UAE and northern Gulf region. One CMA CGM container ship did successfully transit the Strait in late April, but this appears to have been an individual vessel movement rather than a resumption of regular scheduled service.

A safe corridor proposal to free stranded seafarers was reported by Reuters in March 2026 but has not been successfully implemented [https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis). Resolution of the crisis depends on diplomatic progress between the US and Iran, insurance market conditions, and military security guarantees.

**Exact later resolution packet**

The question resolves NO. It asks whether Maersk, MSC, or CMA CGM publicly announced resumption of REGULAR/scheduled commercial container vessel transits through the Strait of Hormuz between May 1, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC).

Evidence reviewed:
- The Wikipedia article "2026 Strait of Hormuz crisis" shows that throughout May 2026 the Strait remained effectively closed or severely restricted. On May 4, 2026, President Trump launched "Operation Project Freedom," a US Navy mission to escort merchant ships out of the Gulf, precisely because commercial vessels were delayed or unable to transit. On May 5, 2026, the container ship CMA CGM San Antonio was reportedly struck by a cruise missile in the Strait — directly contradicting any return to safe, regular service. No official announcement from Maersk, MSC, or CMA CGM of resumed scheduled service appears for the May window [2026 Strait of Hormuz crisis - Wikipedia](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis) (https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis).
- The Reuters article of May 27, 2026 reports only a DRAFT US-Iran framework that would (prospectively) restore commercial shipping to pre-war levels within a month; the US and Iran remained divided and the White House rejected the report. No carrier announced resumption of its own regular service [Iran state TV says draft deal with US would reopen Hormuz shipping ...](https://www.reuters.com/world/middle-east/iran-says-draft-us-deal-would-reopen-hormuz-shipping-end-naval-blockade-2026-05-27/) (https://www.reuters.com/world/middle-east/iran-says-draft-us-deal-would-reopen-hormuz-shipping-end-naval-blockade-2026-05-27/).

Note any developments in May (Operation Project Freedom) were military-escort convoys, which the resolution criteria explicitly EXCLUDE, and a CMA CGM container ship being struck demonstrates that conditions did not permit a return to scheduled service. Therefore no qualifying public announcement of regular/scheduled container service resumption was made by any of the three carriers before the June 1, 2026 deadline. Resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-48. `a0fb8e02-15ac-5a1d-aa1d-ada77a5268e4`

- Present date: `2026-05-03 00:01:10.915583`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will MOL Group finalize the acquisition of Gazprom's 56.15% stake in Serbia's NIS by June 1, 2026?

**Resolution criteria**

This question resolves YES if, by 23:59 UTC on June 1, 2026, there is credible public confirmation that the sale of Gazprom Neft's and JSC Intelligence's combined 56.15% stake in Naftna Industrija Srbije (NIS) to a non-Russian entity has been finalized.

"Finalized" means either: (a) a binding sale-purchase agreement (SPA) has been signed and publicly announced, with formal registration of share transfers initiated or completed; or (b) the formal transfer of shares to the buyer has been registered with the Serbian Central Securities Depository.

"Non-Russian entity" means an entity that is (i) not incorporated in the Russian Federation, (ii) not majority-owned (50%+) by Russian state entities or Russian nationals, and (iii) not designated on the U.S. OFAC Specially Designated Nationals (SDN) list.

The finalization must occur on or after May 1, 2026. Events prior to May 1, 2026 (such as the January 2026 Heads of Agreement) do not count.

Resolution sources: official announcements from MOL Group (https://molgroup.info/en/media-centre/press-releases), the Serbian Government (https://www.srbija.gov.rs/), or credible international news agencies such as Reuters (https://www.reuters.com/), Bloomberg, or AP.

If the sale has not been finalized by 23:59 UTC on June 1, 2026, the question resolves NO.

**Pre-cutoff background**

Naftna Industrija Srbije (NIS) is Serbia's sole oil refiner, operating the Pančevo refinery and an extensive fuel station network. As of early 2026, the ownership structure is: Gazprom Neft holds 44.9% directly, and its affiliate JSC Intelligence holds 11.3%, for a combined Russian-controlled stake of 56.15%; the Serbian state holds 29.9%, with the remainder held by minority shareholders [MOL moves towards acquiring Russian stakes in Serbia's NIS - OSW](https://www.osw.waw.pl/en/publikacje/analyses/2026-01-23/mol-moves-towards-acquiring-russian-stakes-serbias-nis).

In October 2025, the U.S. imposed sanctions on NIS due to its Russian majority ownership. The U.S. set a deadline of March 24, 2026, for Serbia to arrange divestment of the Russian stake [https://www.atlanticcouncil.org/blogs/2026-will-be-a-big-year-in-the-western-balkans-heres-what-to-watch/](https://www.atlanticcouncil.org/blogs/2026-will-be-a-big-year-in-the-western-balkans-heres-what-to-watch/). On January 19, 2026, Hungary's MOL Group signed a binding Heads of Agreement with Gazprom Neft to acquire the 56.15% stake [MOL moves towards acquiring Russian stakes in Serbia's NIS - OSW](https://www.osw.waw.pl/en/publikacje/analyses/2026-01-23/mol-moves-towards-acquiring-russian-stakes-serbias-nis).

On March 24, 2026, MOL received U.S. (OFAC) approval to continue negotiations, with its negotiation license extended to May 22, 2026 [U.S. gives MOL two more months for talks to buy Russian stake in ...](https://seenews.com/news/u-s-gives-mol-two-more-months-for-talks-to-buy-russian-stake-in-serbias-nis-1291965). NIS separately secured a 60-day sanctions waiver lasting until June 16, 2026 [Hungary's MOL says talks on NIS acquisition 'ongoing' | Reuters](https://www.reuters.com/business/energy/hungarys-mol-says-talks-nis-acquisition-ongoing-2026-04-27/). As of April 27, 2026, MOL confirmed that talks are "ongoing" and that the transaction still requires further OFAC licenses and Serbian government approvals [Hungary's MOL says talks on NIS acquisition 'ongoing' | Reuters](https://www.reuters.com/business/energy/hungarys-mol-says-talks-nis-acquisition-ongoing-2026-04-27/).

Key sources for monitoring: Reuters (https://www.reuters.com/), MOL Group press releases (https://molgroup.info/en/media-centre/press-releases), Serbian Government official site (https://www.srbija.gov.rs/), and the Serbian Ministry of Mining and Energy (https://www.mre.gov.rs/).

**Exact later resolution packet**

The question resolves NO because, by 23:59 UTC on June 1, 2026, there was no credible public confirmation that the sale of Gazprom Neft's and JSC Intelligence's combined 56.15% stake in NIS to a non-Russian entity had been finalized (defined as either a signed binding SPA with share-transfer registration initiated/completed, or a registered share transfer with the Serbian Central Securities Depository).

Key evidence:
- As of May 14, 2026, Serbia and MOL remained at odds over terms; the Serbian government rejected a MOL proposal on May 7, 2026, and remained dissatisfied with a revised proposal. Negotiations were ongoing, with a competing bid having emerged. No SPA had been signed and the sale had not been finalized [d8f8fb].
- A Reuters article of May 22, 2026 confirmed the deal was NOT finalized: OFAC granted MOL a two-week extension, setting a new deadline of June 6, 2026 to finalize negotiations with Gazprom Neft, and MOL's CEO noted "certain terms and conditions remain to be finalised" [f1f038].
- A European Western Balkans article of May 25, 2026 reiterated that negotiations were still ongoing, no binding SPA had been signed, and the new completion deadline was June 6, 2026 [96251c].

Since the OFAC negotiation deadline itself was pushed to June 6, 2026 — beyond the question's June 1, 2026 cutoff — and talks were explicitly still ongoing with no SPA signed and no share transfer registered as of late May 2026, the qualifying "finalized" event could not have occurred on or after May 1, 2026 and before 23:59 UTC June 1, 2026. The question therefore resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-49. `0f63f1fc-815c-508c-86a8-b453230dadbb`

- Present date: `2026-05-16 02:15:37.119708`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-06-30T00:00:00`

**Question**

Will the Indian National Congress (INC) secure one of the two Jharkhand Rajya Sabha seats in the June 2026 biennial election?

**Resolution criteria**

This question resolves **Yes** if at least one candidate nominated by the [Indian National Congress](https://en.wikipedia.org/wiki/Indian_National_Congress) (INC) is officially declared **"Elected"** by the [Election Commission of India](https://en.wikipedia.org/wiki/Election_Commission_of_India) (ECI) for one of the two Jharkhand Rajya Sabha vacancies being filled in the 2026 biennial election cycle.

This question resolves **No** if:
- No INC candidate is declared elected for either of the two Jharkhand Rajya Sabha seats, OR
- The INC does not field a candidate for either seat, OR
- The election is not held or results are not declared by July 1, 2026.

"Securing" a seat means being officially declared "Elected" by the ECI. The authoritative resolution source is the Election Commission of India's official results portal at [https://results.eci.gov.in/](https://results.eci.gov.in/), supplemented by the ECI main site at [https://www.eci.gov.in/](https://www.eci.gov.in/). If official ECI results are unavailable online, credible reporting from major Indian news outlets (e.g., [The Hindu](https://www.thehindu.com/), [NDTV](https://www.ndtv.com/), [Hindustan Times](https://www.hindustantimes.com/)) citing official ECI declarations may be used.

Note: A candidate who is an INC member but contests on a JMM ticket or as an independent does not count. The candidate must be officially nominated by the INC.

**Pre-cutoff background**

In June 2026, two [Rajya Sabha](https://en.wikipedia.org/wiki/Rajya_Sabha) seats from Jharkhand are scheduled for biennial elections. One seat has been vacant since the death of [Jharkhand Mukti Morcha](https://en.wikipedia.org/wiki/Jharkhand_Mukti_Morcha) (JMM) patriarch Shibu Soren, and the other will fall vacant upon the expiration of the term of BJP leader Deepak Prakash [Jharkhand ruling alliance eligible for two Rajya Sabha seats](https://www.newindianexpress.com/nation/2026/May/01/jharkhand-ruling-alliance-eligible-for-two-rajya-sabha-seats-congress-demands-one-jmm-eyes-both).

The current composition of the 81-member [Jharkhand Legislative Assembly](https://en.wikipedia.org/wiki/Jharkhand_Legislative_Assembly), whose MLAs vote in Rajya Sabha elections, is as follows based on the November 2024 assembly election results [2024 Jharkhand Legislative Assembly election](https://en.wikipedia.org/wiki/2024_Jharkhand_Legislative_Assembly_election):
- **JMM**: 34 seats
- **[Indian National Congress](https://en.wikipedia.org/wiki/Indian_National_Congress) (INC)**: 16 seats
- **[Bharatiya Janata Party](https://en.wikipedia.org/wiki/Bharatiya_Janata_Party) (BJP)**: 21 seats
- Other INDIA bloc allies (RJD, CPI(ML), etc.): 6 seats
- Total INDIA bloc: 56 seats; NDA: 24 seats; Others: 1 seat

The ruling INDIA bloc, with 56 MLAs, has enough votes to win both seats (each seat requires approximately 28 votes in a house of 81). JMM has publicly claimed both seats, while Congress has demanded at least one, citing its role as a key alliance partner [Jharkhand ruling alliance eligible for two Rajya Sabha seats](https://www.newindianexpress.com/nation/2026/May/01/jharkhand-ruling-alliance-eligible-for-two-rajya-sabha-seats-congress-demands-one-jmm-eyes-both). This intra-alliance dispute creates genuine uncertainty about whether Congress will field and win a candidate.

As of May 13, 2026, the [Election Commission of India](https://en.wikipedia.org/wiki/Election_Commission_of_India) (ECI) has announced a June 19, 2026 date for Rajya Sabha biennial elections covering seats in Assam and Tamil Nadu [Biennial polls to eight Rajya Sabha seats to be held on June 19](https://www.thehindu.com/news/national/biennial-polls-to-eight-rajya-sabha-seats-on-june-19/article69620572.ece). A separate notification for the Jharkhand seats has not yet been confirmed in available reporting, though they are expected to be held around the same timeframe [Jharkhand ruling alliance eligible for two Rajya Sabha seats](https://www.newindianexpress.com/nation/2026/May/01/jharkhand-ruling-alliance-eligible-for-two-rajya-sabha-seats-congress-demands-one-jmm-eyes-both).

**Exact later resolution packet**

The question resolves NO.

**What happened:** The June 2026 biennial Rajya Sabha election for the two Jharkhand seats (one vacant after JMM patriarch Shibu Soren's death, the other upon expiry of BJP's Deepak Prakash's term) was held with voting on June 18, 2026. Three candidates contested: JMM's Baidyanath Ram, Congress's Pranav Jha, and NDA/BJP-backed Independent nominee Parimal Nathwani.

**The antecedent (INC fielding a candidate) was met:** The INC did officially nominate a candidate, Pranav Jha, for one of the two Jharkhand seats (New Indian Express, June 4, 2026: "Rajya Sabha Polls: Banking on INDIA Bloc support, Congress fields Pranav Jha from Jharkhand"). So this is NOT a case where INC failed to field a candidate.

**The consequent (INC candidate declared "Elected") did NOT occur:** The two seats were won by JMM's Baidyanath Ram and NDA-backed Independent Parimal Nathwani. Congress candidate Pranav Jha was DEFEATED. Per Hindustan Times (a mandated resolution source), Parimal Nathwani won with 28 valid votes (30 cast, 2 rejected), defeating Pranav Jha amid cross-voting by ruling-alliance legislators; the second seat went to JMM's Baidyanath Ram [4e78f4]. This is corroborated by The Hindu (June 18, 2026 coverage confirming the three candidates in the fray) [38226a], and by numerous other reports (NDTV, India Today, Times of India, Deccan Herald) confirming Nathwani defeated Congress's Pranav Jha (~28 votes to Jha's ~20).

**Timing requirement met (working against YES, not annulment):** Results were declared June 18, 2026 — well before the July 1, 2026 deadline. So the election was held and results declared on time; it simply did not produce an INC winner.

**Conclusion:** Since no INC-nominated candidate was declared "Elected" by the ECI for either Jharkhand seat (the INC's Pranav Jha lost, and the seats went to JMM and an NDA-backed Independent), the resolution criterion for YES is not satisfied. Per the stated NO conditions ("No INC candidate is declared elected for either of the two Jharkhand Rajya Sabha seats"), this resolves NO.

Sources: Hindustan Times, "Used money to secure votes: Congress after NDA-backed candidate's Rajya Sabha win in Jharkhand" (https://www.hindustantimes.com/india-news/used-money-to-secure-votes-congress-after-nda-backed-candidates-rajya-sabha-win-in-jharkhand-elections-parimal-nathwani-101781794650599.html) [4e78f4]; The Hindu, "Voting begins for election to two Rajya Sabha seats in Jharkhand" (https://www.thehindu.com/news/national/jharkhand/jharkhand-two-rajya-sabha-seats-voting-underway-june-18-2026-updates/article71116790.ece) [38226a].

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-50. `7ca74fd1-4826-50f4-8864-7487b115cb5e`

- Present date: `2026-05-02 22:11:28.640772`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Discharge Petition No. 17 on DHS funding reach 218 signatures and advance to a House floor vote by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between 12:00 AM UTC on May 1, 2026 and 11:59 PM UTC on June 1, 2026, [Discharge Petition No. 17](https://clerk.house.gov/DischargePetition/2026031817) (H.Res. 1096) both:

1. Reaches the required **218 signatures** as recorded by the [Office of the Clerk of the U.S. House of Representatives](https://clerk.house.gov/DischargePetition), AND
2. Is called up and receives a [floor vote](https://www.congress.gov/help/legislative-glossary#glossary_flooraction) in the U.S. House of Representatives, as recorded in the Clerk's [Legislative Activity logs](https://clerk.house.gov/FloorSummary).

"Successfully advance" means the [discharge petition](https://en.wikipedia.org/wiki/Discharge_petition) obtains the constitutionally required majority of 218 signatures under [House Rule XV](https://rules.house.gov/rules-and-resources/rules-of-the-house), and the resulting motion to discharge is subsequently brought to the House floor for a recorded vote.

The question resolves **No** if Petition No. 17 does not reach 218 signatures, or if it reaches 218 signatures but no floor vote occurs by 11:59 PM UTC on June 1, 2026.

Primary resolution source: [U.S. House Clerk's Discharge Petition Tracker](https://clerk.house.gov/DischargePetition) and [Legislative Activity page](https://clerk.house.gov/FloorSummary).

**Pre-cutoff background**

A [discharge petition](https://en.wikipedia.org/wiki/Discharge_petition) is a procedural tool under [House Rule XV](https://rules.house.gov/rules-and-resources/rules-of-the-house) that allows a majority of House members (218) to force a bill out of committee and onto the House floor for a vote, bypassing the Speaker and committee chairs. In the 119th Congress, Democrats have filed multiple discharge petitions, and one — on healthcare subsidies — already succeeded, garnering 214 Democratic and 4 Republican signatures to reach the 218 threshold [Discharge Petitions - House Clerk's Office](https://clerk.house.gov/DischargePetition).

Discharge Petition No. 17 (H.Res. 1096), filed on March 18, 2026, by Rep. Rosa L. DeLauro, seeks to force a [floor vote](https://www.congress.gov/help/legislative-glossary#glossary_flooraction) on H.R. 4213, a bill making appropriations for the Department of Homeland Security for fiscal year 2026. As of April 15, 2026, the petition has **209 signatures** [Discharge Petition No. 17 - House Clerk](https://clerk.house.gov/DischargePetition/2026031817), meaning it needs 9 additional signatures to reach the 218-member majority required to trigger discharge. With Democrats holding 213 seats in the current Congress [Discharge Petitions - House Clerk's Office](https://clerk.house.gov/DischargePetition), reaching 218 requires convincing at least 5 Republican members to sign.

A separate active petition, Discharge Petition No. 19 (H.Res. 1140), filed April 20, 2026 by Rep. Donald Norcross, had **184 signatures** as of April 29, 2026 [Discharge Petition No. 19 - House Clerk](https://clerk.house.gov/DischargePetition/2026042019). The DHS petition (No. 17) is significantly closer to the threshold and thus the focus of this question.

The success of the healthcare discharge petition earlier in this Congress demonstrated that a small number of Republican defections is possible. However, DHS funding is politically charged — Republican leadership has framed the Democratic petition as an effort to "defund the police" — making bipartisan cooperation uncertain. The petition's progress has stalled since April 15, 2026, with no new signatures recorded in two weeks [Discharge Petition No. 17 - House Clerk](https://clerk.house.gov/DischargePetition/2026031817).

Resolution source: The [U.S. House Clerk's discharge petition tracker](https://clerk.house.gov/DischargePetition) and [Legislative Activity page](https://clerk.house.gov/FloorSummary) provide official, real-time records of petition signatures and floor votes.

**Exact later resolution packet**

The question resolves NO.

Resolution criteria required that, between May 1, 2026 and June 1, 2026, Discharge Petition No. 17 (H.Res. 1096) on DHS funding (H.R. 4213) both (1) reach 218 signatures AND (2) be called up for a floor vote.

The official U.S. House Clerk's Discharge Petition tracker for Petition No. 17 (https://clerk.house.gov/DischargePetition/2026031817) shows the petition stalled at approximately 209–210 signatures, with the most recent signature recorded on April 15, 2026. No signatures were added after that date, so the petition never reached the required 218-signature majority [aca613].

Because the first condition (218 signatures) was never met, the petition could not be discharged from committee, and no motion to discharge / floor vote on H.R. 4213 via this petition could occur. The resolution criteria explicitly state the question resolves NO if Petition No. 17 does not reach 218 signatures. Since it failed to reach 218 (it remained at 209–210), the question resolves NO (0).

This determination is specific to Petition No. 17 (H.Res. 1096) and is not confused with Petition No. 19 (H.Res. 1140), which is a separate petition. The signature history confirmed (Nos. 1–210 added between March 18 and April 15, 2026) is unambiguously for Petition No. 17 on DHS appropriations [aca613].

Evidence URLs:
- Discharge Petition No. 17 tracker: https://clerk.house.gov/DischargePetition/2026031817
- Legislative Activity / Floor Summary: https://clerk.house.gov/FloorSummary
- Discharge Petitions list: https://clerk.house.gov/DischargePetition

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-51. `f7391cde-9b66-52b0-9561-a9e12d5fbc60`

- Present date: `2026-04-30 18:56:31.302761`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the International Stabilization Force (ISF) have physically deployed at least 50 uniformed personnel inside the Gaza Strip between April 30 and June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after April 30, 2026 (00:00 UTC) and before June 1, 2026 (23:59 UTC), credible reporting confirms that at least 50 uniformed military or police personnel belonging to the International Stabilization Force (ISF) — as defined by the Wikipedia article on the ISF (https://en.wikipedia.org/wiki/International_Stabilization_Force) [International Stabilization Force - Wikipedia](https://en.wikipedia.org/wiki/International_Stabilization_Force) — have physically entered and are present within the borders of the Gaza Strip.

Key definitions:
- **International Stabilization Force (ISF):** The multinational force authorized by UN Security Council Resolution 2803 (November 17, 2025), as described at https://en.wikipedia.org/wiki/International_Stabilization_Force [International Stabilization Force - Wikipedia](https://en.wikipedia.org/wiki/International_Stabilization_Force).
- **Physical deployment:** The confirmed physical presence of at least 50 uniformed military or police personnel (not civilian contractors, diplomats, or advance survey teams of fewer than 50) inside Gaza.
- **Personnel:** Uniformed military or police members serving under the ISF mandate. Civilian contractors, humanitarian workers, and diplomatic staff do not count.
- **Gaza / Inside Gaza:** The territory of the Gaza Strip as defined by its internationally recognized boundaries (see: https://en.wikipedia.org/wiki/Gaza_Strip#Geography). This includes all land area within the Strip's borders.
- **"On or after April 30, 2026":** Any deployment that occurred prior to April 30, 2026 (00:00 UTC) does not count toward resolution.

**Resolution sources:** Official UN statements (https://www.un.org/press/), U.S. State Department briefings (https://www.state.gov/), or credible international news agencies including Reuters (https://www.reuters.com/), Associated Press (https://apnews.com/), BBC (https://www.bbc.com/news), or Al Jazeera (https://www.aljazeera.com/).

If no credible source confirms such deployment by 23:59 UTC on June 1, 2026, the question resolves **No**.

**Pre-cutoff background**

The International Stabilization Force (ISF) is a UN-mandated multinational peacekeeping force established by United Nations Security Council Resolution 2803, adopted on November 17, 2025 (https://en.wikipedia.org/wiki/United_Nations_Security_Council_Resolution_2803). It is a core component of the US-backed "Comprehensive Plan to End the Gaza Conflict" (https://en.wikipedia.org/wiki/Gaza_peace_plan) [https://en.wikipedia.org/wiki/Gaza_peace_plan](https://en.wikipedia.org/wiki/Gaza_peace_plan). The ISF's mandate includes supporting demilitarization, destroying terror infrastructure, securing border areas, protecting civilians and humanitarian operations, and training vetted Palestinian police forces [International Stabilization Force - Wikipedia](https://en.wikipedia.org/wiki/International_Stabilization_Force).

As of April 30, 2026 (UTC), the ISF is in the planning and preparation phase. A command center has been established in El Arish, Egypt, and a planning conference was held in Qatar in December 2025. Major General Jasper Jeffers (USA) was appointed as force commander in January 2026 [International Stabilization Force - Wikipedia](https://en.wikipedia.org/wiki/International_Stabilization_Force). Confirmed troop-contributing nations include Indonesia (deputy commander role), Morocco, Kazakhstan, Kosovo, and Albania [International Stabilization Force - Wikipedia](https://en.wikipedia.org/wiki/International_Stabilization_Force).

As of mid-March 2026, Israeli broadcaster Kan reported that Israel was preparing for ISF deployment with an anticipated start date of May 1, 2026. The force is expected to consist of approximately 5,000 soldiers. Military delegations had arrived in Israel for reconnaissance and foreign soldiers were training in Jordan [Israel preparing for deployment of international force to Gaza in May](https://www.newarab.com/news/israel-preparing-deployment-international-force-gaza). However, earlier reporting indicated that Phase 2 measures, including the stabilization force, were largely "at a standstill," creating genuine uncertainty about whether the May deployment timeline will hold.

**Exact later resolution packet**

The question resolves NO. It required credible reporting that at least 50 uniformed ISF military/police personnel had physically entered the Gaza Strip on or after April 30, 2026 (00:00 UTC) and before June 1, 2026 (23:59 UTC).

Multiple sources within the allowed list confirm that no such deployment occurred during this window:

- An Associated Press report published May 28, 2026 ("Plans for the Gaza International Stabilization Force are in question as troop pledges stall"), accessed via a syndicating outlet, states that the ISF "has yet to materialize" three months after being announced, that force commander Maj. Gen. Jasper Jeffers "still has no force to lead as none of the five countries that pledged troops have come through with any significant contributions," that "no troops had yet been sent," and that none are "yet known to be on the ground" [Plans for the Gaza International Stabilization Force are in question ...](https://kdhnews.com/news/world/plans-for-the-gaza-international-stabilization-force-are-in-question-as-troop-pledges-stall/article_4ccb21aa-8b44-5c37-a44d-b8c342eb4a84.html). The original AP article: https://apnews.com/article/israel-hamas-gaza-trump-indonesia-stabilization-force-a5e1d4a894746104c1335b6962c0ab69

- A Euronews report dated May 28, 2026 ("Plans for Gaza International Stabilisation Force in question as troop pledges stall") similarly confirms "Forces committed but none known to be deployed," noting Indonesia put its commitment on hold and Albania confirmed no troops sent [Plans for Gaza Stabilisation Force in question as troop pledges stall](https://www.euronews.com/2026/05/28/plans-for-gaza-international-stabilisation-force-in-question-as-troop-pledges-stall). https://www.euronews.com/2026/05/28/plans-for-gaza-international-stabilisation-force-in-question-as-troop-pledges-stall

Since the most recent reporting (May 28, 2026), just three days before the window closed, confirms zero ISF personnel deployed inside Gaza—far short of the 50-personnel threshold—and no later credible source reports any deployment before the June 1, 2026 deadline, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-52. `1aae92e0-bdac-565e-bfed-2ed0be71c16d`

- Present date: `2026-05-14 05:31:38.765176`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will either Senator Collins or Senator Murkowski publicly announce opposition to Nicole Saphier's nomination for Surgeon General by July 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after May 12, 2026 and by 11:59 PM ET on July 1, 2026, either Senator Susan Collins (R-ME) or Senator Lisa Murkowski (R-AK) publicly announces opposition to the confirmation of Dr. Nicole Saphier as U.S. Surgeon General.

"Opposition" is defined as a clear, unambiguous public statement that the senator will vote against Saphier's confirmation or cannot/will not support the nomination. This includes statements such as "I will vote no," "I oppose this nomination," or "I cannot support this nominee." Statements expressing mere "concern," "reservations," "questions," or indicating they are "reviewing the record" do NOT qualify as opposition unless accompanied by an explicit declaration of intent to vote against or not support the nomination.

Qualifying announcements may take the form of official press releases, floor speeches, committee votes against the nominee, or on-the-record statements to reporters.

Resolution source: Credible news reporting from outlets such as The New York Times (nytimes.com), Politico (politico.com), Reuters (reuters.com), the Associated Press (apnews.com), or official Senate press releases (e.g., senator websites or the Senate Press Gallery).

If the nomination is withdrawn, rejected, or confirmed before either senator publicly announces opposition as defined above, the question resolves NO.

If no qualifying public announcement of opposition is made by either senator by the deadline, the question resolves NO.

**Pre-cutoff background**

On April 30, 2026, President Trump nominated Dr. Nicole Saphier, a board-certified radiologist and former Fox News medical contributor at Memorial Sloan Kettering, as his third pick for U.S. Surgeon General [https://www.houstonpublicmedia.org/npr/2026/05/02/nx-s1-5808313/can-trumps-latest-pick-for-surgeon-general-make-it-through-confirmation/](https://www.houstonpublicmedia.org/npr/2026/05/02/nx-s1-5808313/can-trumps-latest-pick-for-surgeon-general-make-it-through-confirmation/). This followed the withdrawal of Dr. Casey Means' nomination, which had stalled after Senators Susan Collins (R-ME) and Lisa Murkowski (R-AK) signaled opposition due to concerns about Means' qualifications and views [https://www.houstonpublicmedia.org/npr/2026/05/02/nx-s1-5808313/can-trumps-latest-pick-for-surgeon-general-make-it-through-confirmation/](https://www.houstonpublicmedia.org/npr/2026/05/02/nx-s1-5808313/can-trumps-latest-pick-for-surgeon-general-make-it-through-confirmation/).

Collins and Murkowski sit on the Senate Health, Education, Labor and Pensions (HELP) Committee, which is responsible for confirmation hearings. Their opposition was instrumental in blocking Casey Means [https://www.houstonpublicmedia.org/npr/2026/05/02/nx-s1-5808313/can-trumps-latest-pick-for-surgeon-general-make-it-through-confirmation/](https://www.houstonpublicmedia.org/npr/2026/05/02/nx-s1-5808313/can-trumps-latest-pick-for-surgeon-general-make-it-through-confirmation/). While Saphier is viewed as a more credentialed choice given her clinical background, she has drawn scrutiny for her public statements questioning CDC childhood vaccine schedules, including those for hepatitis B and COVID-19 [https://www.houstonpublicmedia.org/npr/2026/05/02/nx-s1-5808313/can-trumps-latest-pick-for-surgeon-general-make-it-through-confirmation/](https://www.houstonpublicmedia.org/npr/2026/05/02/nx-s1-5808313/can-trumps-latest-pick-for-surgeon-general-make-it-through-confirmation/).

As of May 13, 2026, no formal confirmation hearing has been scheduled for Saphier before the HELP Committee [https://www.houstonpublicmedia.org/npr/2026/05/02/nx-s1-5808313/can-trumps-latest-pick-for-surgeon-general-make-it-through-confirmation/](https://www.houstonpublicmedia.org/npr/2026/05/02/nx-s1-5808313/can-trumps-latest-pick-for-surgeon-general-make-it-through-confirmation/). Neither Collins nor Murkowski has publicly announced a position on the Saphier nomination.

**Exact later resolution packet**

The question resolves NO. It required that, on or after May 12, 2026 and by 11:59 PM ET July 1, 2026, Senator Susan Collins (R-ME) or Senator Lisa Murkowski (R-AK) make a clear, unambiguous public statement of opposition to Dr. Nicole Saphier's confirmation as U.S. Surgeon General (an explicit "will vote no"/"cannot support" declaration, not mere concern/reservations). No such statement occurred.

Key evidence:
- Trump nominated Saphier on April 30, 2026, after withdrawing Casey Means; Saphier's nomination (PN963) was formally received by the Senate on May 11, 2026 and referred to the HELP Committee, where it remained pending — no hearing, vote, withdrawal, rejection, or confirmation — through July 1, 2026 [34c4c4, be02c3]. The withdrawal message dated 05/11/2026 pertained to Casey Means (PN730-47), not Saphier [be02c3].
- As of June 30, 2026, Axios reported Saphier's confirmation hearing was still only planned to begin in July 2026, and HELP Chair Cassidy was "very favorably impressed"; no opposition from Collins or Murkowski was reported [04e155]. An ASTHO June 2026 update likewise indicated the HELP Committee had not yet noticed a hearing for her nomination [6ea59d].
- The NPR/Houston Public Media May 2, 2026 piece stated neither senator had announced a position on Saphier [e1dbe6]. A May 4, 2026 Fox News article found no opposition announced against Saphier [9511e6].
- The only Collins/Murkowski opposition or hesitancy statements found ("undecided," "not enthusiastic," "reservations") were directed at the prior nominee Casey Means, not Saphier, and predate the resolution window [6782fc, e1dbe6].

Because no qualifying public announcement of opposition to Saphier by Collins or Murkowski was made within the window, and the nomination was neither withdrawn, rejected, nor confirmed before any such announcement (it simply remained pending), the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-53. `d49e58a9-5b58-54a1-a971-1d7227483f8c`

- Present date: `2026-05-04 08:30:22.429266`
- Source cutoff boundary: `2026-05-05` (encodes end of UTC day `2026-05-04`)
- Expected resolution: `2026-05-24 00:00:00`

**Question**

Will the WHO World Health Assembly (WHA79) formally adopt the Pathogen Access and Benefit-Sharing (PABS) annex to the Pandemic Agreement by May 23, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 2, 2026 (00:00 UTC), the Seventy-ninth World Health Assembly (WHA79) formally adopts the PABS annex to the [Pandemic Agreement](https://www.who.int/health-topics/who-pandemic-agreement) by the close of the assembly on May 23, 2026 (23:59 UTC).

"Adoption" is defined as a formal action—recorded as a specific resolution or decision—by the WHA79 plenary or its main committee (Committee A) that explicitly incorporates the final text of the PABS annex into the Pandemic Agreement framework. This must be documented in the official WHA79 decisions or resolutions published on the [WHO WHA79 documents page](https://apps.who.int/gb/e/e_wha79.html) [https://www.who.int/about/governance/world-health-assembly/seventy-ninth](https://www.who.int/about/governance/world-health-assembly/seventy-ninth).

The "PABS annex" refers to the Pathogen Access and Benefit-Sharing system annex to the WHO Pandemic Agreement, as described in the [WHO Pandemic Agreement information page](https://www.who.int/health-topics/who-pandemic-agreement).

This question resolves **No** if:
- The WHA79 concludes without formal adoption of the PABS annex; or
- Adoption is deferred to a future session, intersessional process, or subsequent World Health Assembly; or
- Only a partial or framework agreement is adopted that does not constitute the full PABS annex text.

Resolution source: Official WHA79 decisions and resolutions at [https://apps.who.int/gb/e/e_wha79.html](https://apps.who.int/gb/e/e_wha79.html), or official WHO press releases confirming the outcome.

**Pre-cutoff background**

The [WHO Pandemic Agreement](https://www.who.int/health-topics/who-pandemic-agreement) was adopted by the World Health Organization in May 2025, but the Pathogen Access and Benefit-Sharing (PABS) system—the final unresolved component—was deferred for further negotiation. The PABS system is intended to govern how member states share pathogen samples and genomic sequence data with pandemic potential, and how the benefits derived from such sharing (e.g., vaccines, therapeutics, diagnostics) are distributed equitably.

As of May 2, 2026, negotiations on the PABS annex remain deadlocked [https://healthpolicy-watch.news/no-pandemic-agreement-annex-by-world-health-assembly-says-civil-society/](https://healthpolicy-watch.news/no-pandemic-agreement-annex-by-world-health-assembly-says-civil-society/). The central point of contention is a "hybrid" or "blended" model proposed by the European Union, which would combine mandatory and voluntary measures for pathogen information sharing and benefit distribution. While some countries (e.g., Brazil, Botswana) have signaled potential support for this compromise, the Africa Group remains firmly opposed [https://healthpolicy-watch.news/no-pandemic-agreement-annex-by-world-health-assembly-says-civil-society/](https://healthpolicy-watch.news/no-pandemic-agreement-annex-by-world-health-assembly-says-civil-society/). Civil society observers, including the Third World Network and the AIDS Healthcare Foundation, have expressed skepticism that agreement can be reached during the upcoming assembly, while WHO Director-General Dr. Tedros Adhanom Ghebreyesus maintains that consensus is still possible [https://healthpolicy-watch.news/no-pandemic-agreement-annex-by-world-health-assembly-says-civil-society/](https://healthpolicy-watch.news/no-pandemic-agreement-annex-by-world-health-assembly-says-civil-society/).

WHO member states agreed in March 2026 to extend PABS negotiations, with the [Seventy-ninth World Health Assembly (WHA79)](https://www.who.int/about/governance/world-health-assembly/seventy-ninth) scheduled for May 18–23, 2026 (UTC+1, Geneva) serving as the target deadline [https://www.who.int/about/governance/world-health-assembly/seventy-ninth](https://www.who.int/about/governance/world-health-assembly/seventy-ninth).

**Exact later resolution packet**

NO. The official WHA79 documents page identifies Decision WHA79(7), titled “Outcome of the open-ended Intergovernmental Working Group on the WHO Pandemic Agreement in relation to the drafting and negotiation of the Annex described in Article 12 of the WHO Pandemic Agreement,” with official PDF URL https://apps.who.int/gb/ebwha/pdf_files/WHA79/A79_%287%29-en.pdf [https://apps.who.int/gb/e/e_wha79.html](https://apps.who.int/gb/e/e_wha79.html). In that decision, dated 22 May 2026, WHA79 did not incorporate or adopt a final PABS annex; instead, it decided that the open-ended Intergovernmental Working Group “shall continue its work” to “draft and negotiate the Annex described in Article 12 of the WHO Pandemic Agreement,” and to “submit the outcome to the Eightieth World Health Assembly for its consideration or, as may be necessary, earlier by a special session of the World Health Assembly in 2026” [https://apps.who.int/gb/ebwha/pdf_files/WHA79/A79_%287%29-en.pdf](https://apps.who.int/gb/ebwha/pdf_files/WHA79/A79_%287%29-en.pdf). This is an explicit continuation/deferral of negotiations to a future WHA or special session, not full adoption by the May 23, 2026 deadline. The relevant formal action occurred by the deadline—Decision WHA79(7) is dated 22 May 2026—but that action was deferral/continuation rather than adoption [https://apps.who.int/gb/ebwha/pdf_files/WHA79/A79_%287%29-en.pdf](https://apps.who.int/gb/ebwha/pdf_files/WHA79/A79_%287%29-en.pdf). Therefore the resolution criteria require NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-54. `b5577074-7a36-5fe1-be5f-e27a6b69ab5c`

- Present date: `2026-04-30 13:13:30.043869`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the U.S. Army Corps of Engineers issue a solicitation for Phase 2 (dredging) of the Port of Nome Modification Project by June 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after April 29, 2026 and on or before June 1, 2026 (11:59 PM UTC), the U.S. Army Corps of Engineers (USACE) Alaska District posts either:

1. A formal solicitation (Request for Proposals or Invitation for Bids) for Phase 2 of the Port of Nome Modification Project on SAM.gov (https://sam.gov/), OR
2. A contract award announcement for Phase 2 on the USACE Alaska District news page (https://www.poa.usace.army.mil/Media/News-Releases/).

"Phase 2" refers specifically to the dredging of the deep and outer basins of the Port of Nome, as described in the USACE Port of Nome Modification Project (https://www.poa.usace.army.mil/Library/Reports-and-Studies/Port-of-Nome-Modification-Project/).

A "solicitation" means a formal procurement notice inviting bids or proposals, not a pre-solicitation notice or sources-sought notice.

If neither a solicitation nor a contract award for Phase 2 appears on SAM.gov or the USACE Alaska District news page by June 1, 2026 (11:59 PM UTC), this question resolves NO.

**Pre-cutoff background**

The Port of Nome Modification Project is a multi-phase infrastructure initiative managed by the U.S. Army Corps of Engineers (USACE) Alaska District, aimed at creating the nation's first deep-water Arctic port. The project enlarges Nome Harbor's outer basin and creates a new deep-draft basin at minus 40 feet depth. (See USACE project page: https://www.poa.usace.army.mil/Library/Reports-and-Studies/Port-of-Nome-Modification-Project/)

On August 15, 2025, USACE awarded a $399.4 million construction contract to Kiewit Infrastructure West Co. for Phase 1A, which includes a 1,200-foot causeway extension with 600 feet of dock face [USACE awards construction contract for portion of Port of Nome ...](https://www.poa.usace.army.mil/Media/News-Releases/Article/4276752/usace-awards-construction-contract-for-portion-of-port-of-nome-modification-pro/). The project has four planned phases: Phase 1A (awarded), Phase 2 (deep and outer basin dredging), Phase 1B (additional causeway extension and dock), and Phase 3.

As of mid-2025, USACE officials indicated they expected Phase 2 procurement to go out to bid in May 2026, followed by Phase 1B in fiscal year 2028 and Phase 3 later. However, federal infrastructure procurement timelines frequently shift due to funding availability, environmental reviews, and bureaucratic processes. The project has significant strategic importance given growing U.S. Arctic military and commercial interests, and has been highlighted as key to the Trump administration's global ambitions.

As of April 29, 2026, Phase 1A construction is underway. No Phase 2 solicitation or contract award has been confirmed.

**Exact later resolution packet**

The question resolves NO because no formal Phase 2 (dredging of deep and outer basins) solicitation appeared on SAM.gov, and no Phase 2 contract award was announced on the USACE Alaska District news page, between April 29, 2026 and June 1, 2026 (11:59 PM UTC).

Evidence:
- The USACE Alaska District news releases page (https://www.poa.usace.army.mil/Media/News-Releases/Tag/3983/alaska/) shows that the ONLY Alaska District news release in the resolution window was dated May 21, 2026, titled "USACE seeks public comment on draft Homer Harbor study" — unrelated to the Port of Nome Phase 2. The most recent Port of Nome news release was the August 15, 2025 Phase 1A award; no Phase 2 award announcement exists [2ba0ef, 703825].
- Multiple SAM.gov targeted searches (e.g., site:sam.gov "Port of Nome Modification Phase 2") returned no Phase 2 solicitation. SAM.gov only shows Port of Nome Phase 1 / Phase 1A notices.
- Planning documents consistently described the Phase 2 dredging bid package as only "anticipated" to be released around May 2026 with award "potentially in the Sep 2026 timeframe" — i.e., a forecast, not an actual issued solicitation. As of the March 23, 2026 Nome Common Council packet, the Phase 2 design/specs package was "still scheduled for bidding in 2026," and the engineering/design was only "near complete" as of the March 5, 2026 Port Director report [34dc76, b8a09d].
- The City of Nome meeting packets from April–May 2026 (including the May 11, 2026 Common Council packet) contain no indication that USACE had issued the Phase 2 solicitation or made a Phase 2 award [0e4f4a, 08fec8].
- The Metaculus question description itself states that as of April 29, 2026, "No Phase 2 solicitation or contract award has been confirmed."

Since the two qualifying resolution sources (SAM.gov solicitation OR USACE Alaska District news page award announcement) show no Phase 2 solicitation or award within the window, the question resolves NO. This is not a conditional question, so no annulment applies.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-55. `75a9b157-4271-5ef6-a7d8-789e69325b07`

- Present date: `2026-05-15 13:18:10.597107`
- Source cutoff boundary: `2026-05-16` (encodes end of UTC day `2026-05-15`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Senate Agriculture Committee hold a markup of the 2026 Farm Bill before July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if the U.S. Senate Committee on Agriculture, Nutrition, and Forestry holds a formal markup of a 2026 Farm Bill (i.e., legislation serving as the Senate's primary vehicle for reauthorizing farm, nutrition, and related programs, whether titled the "Farm, Food, and National Security Act of 2026" or otherwise) on or after May 12, 2026, and on or before June 30, 2026, at 11:59 PM ET.

A "markup" is defined as a formal committee session in which members consider, amend, and vote on proposed legislation, as described in the [Senate glossary](https://www.senate.gov/reference/glossary_term/markup.htm). This excludes hearings, informational sessions, listening sessions, or any other committee activity that does not involve amending and voting on a specific legislative text.

This question resolves as **No** if no such markup occurs by June 30, 2026, at 11:59 PM ET.

Resolution will be determined by the official record on the [Senate Agriculture, Nutrition, and Forestry Committee hearings/meetings page](https://www.agriculture.senate.gov/hearings) or by credible news reporting (e.g., Reuters, AP, Politico, Agri-Pulse) confirming the markup occurred.

**Pre-cutoff background**

The U.S. House of Representatives passed its version of the 2026 Farm Bill — the "Farm, Food, and National Security Act of 2026" (H.R. 7567) — on April 30, 2026 [https://farmpolicynews.illinois.edu/2026/05/senate-targeting-late-may-early-june-for-farm-bill-markup/](https://farmpolicynews.illinois.edu/2026/05/senate-targeting-late-may-early-june-for-farm-bill-markup/). Attention has now shifted to the Senate, where Agriculture Committee Chairman John Boozman (R-AR) has publicly stated a target of late May or early June 2026 for a committee markup of the Senate's version of the farm bill [https://farmpolicynews.illinois.edu/2026/05/senate-targeting-late-may-early-june-for-farm-bill-markup/](https://farmpolicynews.illinois.edu/2026/05/senate-targeting-late-may-early-june-for-farm-bill-markup/)[https://hpj.com/2026/05/08/with-house-farm-bill-passage-whats-the-outlook-in-the-senate/](https://hpj.com/2026/05/08/with-house-farm-bill-passage-whats-the-outlook-in-the-senate/).

However, the timeline faces significant constraints:

- **Senate recess:** The Senate is scheduled to be in recess from May 23 through June 1, 2026, narrowing the available window [https://farmpolicynews.illinois.edu/2026/05/senate-targeting-late-may-early-june-for-farm-bill-markup/](https://farmpolicynews.illinois.edu/2026/05/senate-targeting-late-may-early-june-for-farm-bill-markup/)[https://hpj.com/2026/05/08/with-house-farm-bill-passage-whats-the-outlook-in-the-senate/](https://hpj.com/2026/05/08/with-house-farm-bill-passage-whats-the-outlook-in-the-senate/).
- **60-vote threshold:** Unlike the House, the Senate requires 60 votes to overcome a filibuster, necessitating bipartisan agreement [https://hpj.com/2026/05/08/with-house-farm-bill-passage-whats-the-outlook-in-the-senate/](https://hpj.com/2026/05/08/with-house-farm-bill-passage-whats-the-outlook-in-the-senate/).
- **Contentious issues:** Key sticking points include SNAP cost-shifting to states, federal preemption of pesticide-labeling laws, and potential repeal of state animal-welfare laws such as California's Proposition 12 [https://hpj.com/2026/05/08/with-house-farm-bill-passage-whats-the-outlook-in-the-senate/](https://hpj.com/2026/05/08/with-house-farm-bill-passage-whats-the-outlook-in-the-senate/).

As of May 13, 2026, the Senate Agriculture Committee has not yet scheduled or held a markup for the farm bill. Bipartisan negotiations between Chairman Boozman and Democratic members are ongoing [https://hpj.com/2026/05/08/with-house-farm-bill-passage-whats-the-outlook-in-the-senate/](https://hpj.com/2026/05/08/with-house-farm-bill-passage-whats-the-outlook-in-the-senate/). The committee's recent activity has included hearings and a markup of crypto market structure legislation, but no farm bill markup has been noticed [https://farmpolicynews.illinois.edu/2026/05/senate-targeting-late-may-early-june-for-farm-bill-markup/](https://farmpolicynews.illinois.edu/2026/05/senate-targeting-late-may-early-june-for-farm-bill-markup/).

**Exact later resolution packet**

The question resolves NO. The Senate Committee on Agriculture, Nutrition, and Forestry did NOT hold a formal markup of the 2026 Farm Bill on or before June 30, 2026, at 11:59 PM ET.

Key evidence:

1. Official Senate Agriculture Committee hearings/meetings page (the primary resolution source): During the resolution window (May 12–June 30, 2026), the committee held only hearings (e.g., Fertilizer Industry on May 12, U.S. Forest Service on June 2, USDA on June 10) and a Business Meeting on June 8, 2026 — none of which was a markup of the 2026 Farm Bill. No farm bill markup was recorded before July 1 [9b9bff].

2. Timeline of the Senate bill: Chairman John Boozman's Senate version, the "Agricultural Act of 2026" (Farm Bill 2.0), was released only as a discussion draft text on June 23, 2026 — just one week before the deadline [3ab011, b6e541]. Committee Democrats issued a statement on the "Senate Republicans' Farm Bill Discussion Draft" on June 23, confirming it was still a draft, not marked-up legislation.

3. Explicit statements that markup was deferred to July (after the window): 
   - NACo reported the committee released text on June 23 and was "expecting to mark up the bill in July" [3ab011].
   - The Fence Post reported (based on The Hagstrom Report) that the Senate draft would be released in June but the markup would NOT be held before the July 4 recess [05ffaf].
   - The National Organic Coalition (June 10) reported the markup was only tentatively scheduled for July/August 2026 [e6a33c].
   - Holland & Knight's June 26 alert stated the draft was released June 23 and the committee would move to mark it up after returning from recess in mid-July 2026 [b6e541].

Because the markup was scheduled for July 2026 and no formal markup (consider/amend/vote on legislative text) of the 2026 Farm Bill occurred within the May 12–June 30, 2026 window, the question resolves NO. The antecedent (a markup being held in the window) simply did not occur, so this is a clear NO rather than an annulment.

Primary source URL: https://www.agriculture.senate.gov/hearings
Supporting URLs: https://www.naco.org/news/senate-agriculture-committee-introduces-2026-farm-bill-following-house-passage ; https://www.thefencepost.com/news/boozman-farm-bill-draft-in-june-markup-in-july/ ; https://www.hklaw.com/en/insights/publications/2026/06/senate-agriculture-committee-releases-draft-text-for-2026-farm-bill

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-56. `c3e01c3f-e0a8-5be2-88c6-d160793cba8d`

- Present date: `2026-05-03 01:55:17.311721`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Joby Aviation begin FAA "for credit" Type Inspection Authorization (TIA) flight testing by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 1, 2026 (00:00 UTC) and on or before June 1, 2026 (23:59 UTC), Joby Aviation officially announces or credible sources confirm that "for credit" TIA flight testing has commenced involving FAA test pilots flying a Joby FAA-conforming aircraft.

**Definitions:**
- **Type Inspection Authorization (TIA)**: An FAA authorization (FAA Form 8110-1) that permits official conformity inspections, airworthiness inspections, and flight tests for type certification purposes. See: https://www.faa.gov/sites/faa.gov/files/other_visit/aviation_industry/designees_delegations/resources/FAA_Form_8110-1.pdf
- **"For credit" flight testing**: Flight testing conducted by or under the direct oversight of FAA test pilots (not solely Joby company pilots) where data is formally applied toward demonstrating compliance with FAA certification requirements. Simulator-based testing alone does not qualify; the testing must involve actual flight of a physical FAA-conforming aircraft.

This question resolves **No** if no credible announcement or reporting confirms the commencement of such testing by 23:59 UTC on June 1, 2026.

**Resolution source**: Official Joby Aviation press releases (https://www.jobyaviation.com/news/ or https://ir.jobyaviation.com/news-events/press-releases), FAA newsroom (https://www.faa.gov/newsroom), or credible aerospace trade publications (e.g., Aviation Week, Reuters, Bloomberg).

**Pre-cutoff background**

Joby Aviation is pursuing FAA type certification for its electric vertical take-off and landing (eVTOL) air taxi. The FAA certification process involves five stages, with Stage 5 being the final compliance flight testing phase.

Key milestones reached so far:
- **March 11, 2026**: Joby's first FAA-conforming aircraft (N547JX) completed its maiden flight at its facility in Marina, CA [Joby's First FAA-Conforming Aircraft Takes Flight](https://www.jobyaviation.com/news/joby-s-first-faa-conforming-aircraft-takes-flight). This aircraft is the first of a fleet being built for Type Inspection Authorization (TIA) testing.
- **April 9, 2026**: Joby completed Stage 4 of FAA type certification, a critical airworthiness milestone.
- As of March 2026, Joby pilots are conducting initial flight testing of the conforming aircraft, with FAA pilots expected to begin "for credit" testing "later this year" [Joby's First FAA-Conforming Aircraft Takes Flight](https://www.jobyaviation.com/news/joby-s-first-faa-conforming-aircraft-takes-flight).

**Type Inspection Authorization (TIA)** is an FAA document (FAA Form 8110-1) prepared by the FAA Aircraft Certification Office (ACO) that authorizes official conformity inspections, airworthiness inspections, and flight tests necessary to fulfill requirements for a Type Certificate [https://www.faa.gov/sites/faa.gov/files/other_visit/aviation_industry/designees_delegations/resources/FAA_Form_8110-1.pdf](https://www.faa.gov/sites/faa.gov/files/other_visit/aviation_industry/designees_delegations/resources/FAA_Form_8110-1.pdf). See: https://www.faa.gov/sites/faa.gov/files/other_visit/aviation_industry/designees_delegations/resources/FAA_Form_8110-1.pdf

**"For credit" flight testing** refers to the formal phase where FAA test pilots conduct flight evaluations that count toward demonstrating compliance with certification requirements [Joby Successfully Conducts First FAA Testing under TIA, Begins ...](https://ir.jobyaviation.com/news-events/press-releases/detail/122/joby-successfully-conducts-first-faa-testing-under-tia). This is distinct from company-led flight testing or simulator-based evaluations. Joby conducted its first FAA testing under TIA in a simulator environment in December 2024 [Joby Successfully Conducts First FAA Testing under TIA, Begins ...](https://ir.jobyaviation.com/news-events/press-releases/detail/122/joby-successfully-conducts-first-faa-testing-under-tia), but "for credit" flight testing with FAA pilots in the actual aircraft has not yet been confirmed as started.

The timing of "for credit" flight testing depends on FAA scheduling, resolution of any open compliance findings, and Joby's technical readiness. Joby has indicated FAA pilots will begin this testing "later in 2026" [Joby's First FAA-Conforming Aircraft Takes Flight](https://www.jobyaviation.com/news/joby-s-first-faa-conforming-aircraft-takes-flight), making the question of whether it happens before June 1 genuinely uncertain.

**Exact later resolution packet**

The question resolves NO because no credible source confirms that FAA test pilots began "for credit" TIA flight testing of a Joby FAA-conforming aircraft during the resolution window (May 1, 2026 00:00 UTC – June 1, 2026 23:59 UTC).

Key findings:
- The antecedent/baseline events are well-documented: Joby's first FAA-conforming aircraft (N547JX) made its maiden flight on March 11, 2026, but this initial flight testing was conducted by JOBY COMPANY PILOTS, not FAA pilots. Joby's own March 11, 2026 announcement explicitly stated "FAA pilots expected to begin 'for credit' TIA flight testing later this year" — i.e., the for-credit FAA-pilot phase was a future event distinct from the company-pilot flights that began in March 2026.
- I reviewed the authorized resolution sources directly. Joby's investor relations press release page lists the most recent releases as: May 5, 2026 (Q1 2026 financial results), May 15, 2026 ("Joby's Commitment to Sustainable Aviation"), plus April releases — none announcing FAA-pilot "for credit" TIA flight testing [88e6e3, 8c50f0].
- The Q1 2026 financial results press release (May 5, 2026) reports the N547JX first flight and ongoing production of TIA aircraft, but does NOT report that FAA pilots had begun "for credit" testing [72d3b2].
- A May 6, 2026 AInvest trade article covering Joby's Q1 results explicitly states "the real test comes later this year when FAA pilots are expected to begin 'for credit' TIA flight testing" — confirming this had not yet occurred [69ac9d].
- A May 27, 2026 ZAG Daily article on a Joby testing milestone (piloted transition flight) contained no mention of FAA-pilot "for credit" testing having commenced [f9d0c2].

All sources consistently describe FAA-pilot "for credit" TIA flight testing as a still-future ("later this year"/"later in 2026") event throughout the May 2026 window, and the testing that had occurred was being done by Joby company pilots (which the resolution criteria explicitly exclude). Therefore the YES condition was not met within the window, and the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-57. `1059ecce-7633-59cc-9bab-df341bfe35b6`

- Present date: `2026-05-12 14:59:03.377445`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will any match in Group J of the 2026 FIFA World Cup end in a 0-0 draw?

**Resolution criteria**

This question resolves **Yes** if at least one of the six Group J matches at the 2026 FIFA World Cup ends with a final score of 0-0 at the end of regulation time (90 minutes plus any stoppage/injury time added by the referee). Extra time and penalty shootouts are not applicable in the group stage, but for the avoidance of doubt, only the score at the end of regulation/stoppage time counts — a "0-0 draw" means neither team has scored any goals by the final whistle of normal time.

The question resolves **No** if all six Group J matches end with at least one goal scored.

**Teams comprising Group J:** Argentina, Algeria, Austria, and Jordan [2026 FIFA World Cup Group J - Wikipedia](https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_Group_J).

**Matches considered:** Only Group J matches occurring on or after May 10, 2026 (UTC) are considered. The six scheduled matches are on June 16, June 22, and June 27, 2026 (all dates UTC) [2026 FIFA World Cup Group J - Wikipedia](https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_Group_J).

**Primary resolution source:** The official FIFA World Cup 2026 match results, available at https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/standings or the FIFA Match Centre at https://www.fifa.com/en/match-centre [FIFA/Coca-Cola World Rankings](https://www.fifa.com/en/world-rankings). If the FIFA website is unavailable, credible secondary sources such as ESPN (https://www.espn.com/soccer/standings/_/league/fifa.world) or UEFA/AFC official match reports may be used.

**Pre-cutoff background**

The 2026 FIFA World Cup Group J consists of Argentina, Algeria, Austria, and Jordan [2026 FIFA World Cup Group J - Wikipedia](https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_Group_J). The group features a wide range of team quality: Argentina are the defending champions and ranked 3rd in the FIFA Men's World Rankings (April 2026) [FIFA/Coca-Cola World Rankings](https://www.fifa.com/en/world-rankings), while Algeria are ranked approximately 28th, Austria approximately 24th, and Jordan approximately 63rd.

There are six group stage matches scheduled [2026 FIFA World Cup Group J - Wikipedia](https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_Group_J):
- June 16, 2026: Argentina vs. Algeria; Austria vs. Jordan
- June 22, 2026: Argentina vs. Austria; Jordan vs. Algeria
- June 27, 2026: Algeria vs. Austria; Jordan vs. Argentina

Historically, 0-0 draws occur in roughly 7–8% of FIFA World Cup matches. Across six matches, the probability of at least one 0-0 draw is approximately 35–40% based on base rates alone. However, team styles and tactical considerations can shift this estimate. Argentina's attacking quality makes 0-0 results less likely in their matches, but fixtures between more evenly matched or defensively oriented teams (e.g., Jordan vs. Algeria, Algeria vs. Austria) could be more prone to low-scoring draws. Jordan, in particular, tends to play a compact defensive style, which could produce goalless matches against opponents of similar quality.

**Exact later resolution packet**

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

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-58. `65ab10c3-bb24-5e73-873f-da584796c42e`

- Present date: `2026-05-14 11:42:23.407058`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

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

**Pre-cutoff background**

Section 702 of the Foreign Intelligence Surveillance Act (FISA) authorizes U.S. intelligence agencies to conduct warrantless surveillance of non-U.S. persons located abroad. The provision requires periodic congressional reauthorization.

Section 702 was set to expire on April 20, 2026 [Congress extends FISA 702 surveillance program for 45 days - NPR](https://www.npr.org/2026/04/29/g-s1-119094/congress-fisa-702). Congress failed to pass a long-term reauthorization due to disputes over warrant requirements for querying Americans' data, data broker restrictions, and an unrelated CBDC (central bank digital currency) rider. Instead, Congress resorted to two short-term extensions in April 2026:

1. A **10-day extension** passed around April 17, 2026, pushing the deadline to approximately April 30 [Congress extends FISA 702 surveillance program for 45 days - NPR](https://www.npr.org/2026/04/29/g-s1-119094/congress-fisa-702).
2. A **45-day extension** (H.R. 8322) passed on April 29–30, 2026, by a House vote of 261–111, extending the program to approximately June 13, 2026 [Congress extends FISA 702 surveillance program for 45 days - NPR](https://www.npr.org/2026/04/29/g-s1-119094/congress-fisa-702) [Congress Passes Another Short-Term Extension of Expiring ...](https://www.nytimes.com/2026/04/30/us/politics/congress-surveillance-extension.html).

As of May 13, 2026, Section 702 is operating under this 45-day extension, with the current expiration date around June 13, 2026. The House previously passed a 3-year reauthorization bill (S.1318), but it has stalled in the Senate due to disagreements over reform amendments. The key fault line is between privacy-minded lawmakers demanding warrant requirements and national security hawks opposing them [Congress Passes Another Short-Term Extension of Expiring ...](https://www.nytimes.com/2026/04/30/us/politics/congress-surveillance-extension.html).

**Exact later resolution packet**

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

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-59. `93c5cdba-1ced-53ca-895d-4b748609c8dc`

- Present date: `2026-05-13 23:18:02.312227`
- Source cutoff boundary: `2026-05-14` (encodes end of UTC day `2026-05-13`)
- Expected resolution: `2026-06-11T00:00:00`

**Question**

Will the Central Bank of the Republic of Türkiye (CBRT) raise its policy rate at the June 2026 MPC meeting?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 (Turkey Time, TRT/UTC+3), the CBRT announces that the one-week repo auction rate (the policy rate) has been set to a level strictly greater than the rate in effect immediately prior to that announcement. As of May 12, 2026, the rate in effect is 37%.

This question resolves **No** if no such increase is announced by July 1, 2026, 23:59 TRT (UTC+3).

The resolution source is the official CBRT "Press Releases on Interest Rates" page: https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/MPC/MPC+Meeting+Decisions

If the CBRT changes its primary policy instrument from the one-week repo auction rate to a different instrument, the question will resolve based on the successor instrument as officially designated by the CBRT. If no MPC meeting takes place during the resolution window, the question resolves **No**.

**Pre-cutoff background**

The Central Bank of the Republic of Türkiye (CBRT) uses the one-week repo auction rate as its primary policy instrument (the "policy rate"), as defined in its [Monetary Policy for 2026 document](https://tcmb.gov.tr/wps/wcm/connect/c2ac62b6-3112-4f33-a6ad-3817defff0be/December28.pdf?MOD=AJPERES). As of the most recent Monetary Policy Committee (MPC) decision on April 22, 2026 (Press Release 2026-17), the policy rate stands at 37% [Press Release on Interest Rates (2026-17) - TCMB](https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/MPC/MPC+Meeting+Decisions). The CBRT had previously cut rates by a cumulative 900 basis points from a peak of 50%, but paused its easing cycle amid persistent inflation. Turkey's annual inflation has been running above 30%, and Citi has warned that an additional rate hike may be needed. Reuters has reported that some investors see a rate hike as possible. The next MPC meeting is scheduled for June 11, 2026, which is the only meeting between now and July 1, 2026. The 2026 MPC calendar is published at the [CBRT calendar page](https://www.tcmb.gov.tr/wps/wcm/connect/en/tcmb+en/main+menu/announcements/calendar). A rate hike after months of easing would represent a dramatic policy reversal and a signal of institutional independence in the face of political pressure to keep rates low.

**Exact later resolution packet**

The question resolves NO (0).

The question resolves YES only if, on or after May 12, 2026 and by July 1, 2026 (23:59 TRT), the CBRT announced that the one-week repo auction rate (the policy rate) was set to a level strictly greater than the 37% rate in effect immediately prior. The only MPC meeting in this window was scheduled for June 11, 2026.

According to the official CBRT "Press Releases on Interest Rates" page (https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/MPC/MPC+Meeting+Decisions) and the specific press release for the June 2026 meeting (Press Release No. 2026-23, dated June 11, 2026, at https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/MPC/MPC+Meeting+Decisions/ANO2026-23), the Monetary Policy Committee "decided to keep the policy rate (the one-week repo auction rate) at 37 percent" [https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/MPC/MPC+Meeting+Decisions](https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/MPC/MPC+Meeting+Decisions) [https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/MPC/MPC+Meeting+Decisions/ANO2026-23](https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/MPC/MPC+Meeting+Decisions/ANO2026-23).

Because the rate was held at 37% (unchanged from the 37% level in effect prior to the announcement) rather than raised to a strictly greater level, the YES condition was not met. The one-week repo auction rate remained the primary policy instrument (no successor instrument was designated). Therefore the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-60. `0bcf7af9-981a-5207-8be0-4b8d54c62a52`

- Present date: `2026-05-03 10:10:43.034473`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the federal court grant final approval to the Bartz v. Anthropic $1.5 billion copyright settlement by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the presiding judge in *Bartz, et al. v. Anthropic PBC* (Case No. 3:24-cv-5417, N.D. Cal.) issues a final order granting approval of the class action settlement on or after May 2, 2026, and on or before June 1, 2026, at 11:59 PM UTC. "Approval" requires a signed order by the judge granting final approval of the settlement; preliminary or conditional approval does not suffice.

This question resolves **No** if any of the following occur:
- The court denies the motion for final approval.
- The court defers its decision or requests further briefing such that no final approval order is issued by June 1, 2026, at 11:59 PM UTC.
- The fairness hearing is postponed or rescheduled to a date after June 1, 2026.
- No final approval order is entered on the docket by the resolution date for any other reason.

Resolution will be determined by official court filings available via [PACER](https://pacer.uscourts.gov/) for Case No. 3:24-cv-5417 (N.D. Cal.), or by official updates posted on the [Anthropic Copyright Settlement website](https://www.anthropiccopyrightsettlement.com/dates).

**Pre-cutoff background**

In August 2025, Anthropic agreed to a $1.5 billion settlement in the class action copyright lawsuit *Bartz, et al. v. Anthropic PBC* (Case No. 3:24-cv-5417, N.D. Cal.), the largest AI copyright settlement in U.S. history. The settlement covers approximately 500,000 copyrighted books allegedly used without authorization to train Anthropic's Claude AI models.

The settlement has had a turbulent path to approval. In September 2025, Judge William Alsup rejected the initial proposed settlement, calling it "nowhere close to done" [Anthropic Judge Rejects $1.5 Billion AI Copyright Settlement (1)](https://www.reddit.com/r/technology/comments/1nc40k4/anthropic_judge_rejects_15_billion_ai_copyright/). Following revisions and Judge Alsup's retirement, the case was reassigned to Judge Martínez-Olguín [Key Dates - Anthropic settlement website](https://www.anthropiccopyrightsettlement.com/dates). Objection and opt-out deadlines have passed, and the claims filing deadline was March 30, 2026. There have been concerns about a law firm (ClaimsHero) allegedly misleading authors to opt out.

As of May 2, 2026, the Final Approval (fairness) hearing is scheduled for May 14, 2026, at 2:00 PM Pacific Time at the San Francisco Federal Courthouse, 450 Golden Gate Ave., Courtroom 12, 19th Floor [Key Dates - Anthropic settlement website](https://www.anthropiccopyrightsettlement.com/dates). The hearing is open to remote attendance. The settlement's prior rejection, the change of judge, and outstanding objections from class members create meaningful uncertainty about whether the court will grant final approval at this hearing.

**Exact later resolution packet**

The question resolves NO because no signed order granting final approval of the Bartz v. Anthropic class action settlement was entered on the docket between May 2, 2026 and June 1, 2026 11:59 PM UTC.

Key evidence:
- The Final Approval (fairness) hearing was held as scheduled on May 14, 2026 before Judge Araceli Martinez-Olguin, so the antecedent event (the hearing) did occur and was NOT postponed past June 1.
- At that hearing, the judge did NOT grant final approval. She took the matter under submission and issued an order requiring supplemental briefing: Anthropic was given until May 21, 2026 to file a supplemental brief of no more than two pages, and plaintiffs were directed to file a revised proposed order [Final Approval of Class Settlement Hearing in Bartz v. Anthropic recap](https://chatgptiseatingtheworld.com/2026/05/15/final-approval-of-class-settlement-hearing-in-bartz-v-anthropic-recap/). This squarely matches the question's NO trigger that "the court defers its decision or requests further briefing such that no final approval order is issued by June 1, 2026."
- The official docket confirms no final approval order was entered before the deadline. The CourtListener docket (PACER/RECAP) for Case No. 3:24-cv-05417, current through late May 2026, contains no final approval order; the most recent entries are routine filings with no approval order [Bartz v. Anthropic PBC, 3:24-cv-05417 – CourtListener.com](https://www.courtlistener.com/docket/69058235/bartz-v-anthropic-pbc/). The PacerMonitor docket, with entries extending through May 29, 2026, likewise shows no final approval order — the latest relevant entries were a Related Case Order (5/20/2026) and a Notice of Withdrawal of counsel, with no order granting final approval [Bartz et al v. Anthropic PBC - PacerMonitor](https://www.pacermonitor.com/public/case/54766054/Bartz_et_al_v_Anthropic_PBC).
- The official Anthropic Copyright Settlement website (anthropiccopyrightsettlement.com/dates) lists the May 14, 2026 fairness hearing as "Passed" but posts no final approval order [Key Dates - Anthropic Copyright Settlement](https://www.anthropiccopyrightsettlement.com/dates).

Because the court deferred its decision and requested further briefing, and no signed final approval order appears on the docket by the June 1, 2026 deadline, the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-61. `2366975e-e87b-5f7c-8483-d27184f9efe4`

- Present date: `2026-05-02 17:06:01.810241`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

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

**Pre-cutoff background**

On April 16, 2026, U.S. Transportation Secretary Sean P. Duffy and the FAA announced an order capping daily operations at Chicago O'Hare International Airport (ORD) at 2,708 flights per day, down from over 3,080 flights that airlines had originally scheduled for peak summer 2026 days [Trump's Transportation Secretary Sean P. Duffy Takes Action to ...](https://www.faa.gov/newsroom/trumps-transportation-secretary-sean-p-duffy-takes-action-prevent-endless-delays). The order was published in the Federal Register on April 20, 2026 (Document No. 2026-07665), with an original effective date of May 17, 2026, through October 24, 2026.

Subsequently, the FAA pushed back the effective date from May 17 to June 2, 2026, issuing an amendment via the Federal Register (Document No. 2026-08163). The cap allocates operations among airlines in proportion to their approved Summer 2025 schedules [Trump's Transportation Secretary Sean P. Duffy Takes Action to ...](https://www.faa.gov/newsroom/trumps-transportation-secretary-sean-p-duffy-takes-action-prevent-endless-delays).

United Airlines, which had planned a massive summer expansion at its largest hub, has expressed strong opposition to the caps. Industry analysis suggests the caps are unlikely to be fully reversed, but United's vocal opposition and the precedent of the FAA already amending the order once (changing the effective date) leave open the possibility of further modifications to the cap number or allocation methodology before the order takes effect [I Understand Why United is So Mad About Chicago Flight Caps](https://crankyflier.com/2026/04/28/i-understand-why-united-is-so-mad-about-chicago-flight-caps/).

A "[slot](https://www.faa.gov/about/office_org/headquarters_offices/ato/service_units/systemops/perf_analysis/slot_administration/slot_definition)" is an FAA authorization to conduct one takeoff or one landing at a capacity-constrained airport during a specific time period. "[Flight caps](https://www.faa.gov/about/office_org/headquarters_offices/ato/service_units/systemops/perf_analysis/slot_administration)" refer to limits on the total number of planned aircraft operations at an airport, used to manage congestion and prevent repeated delays. O'Hare is not currently a permanent Level 3 slot-controlled airport under the FAA's [slot administration framework](https://www.faa.gov/about/office_org/headquarters_offices/ato/service_units/systemops/perf_analysis/slot_administration/slot_administration_schedule_facilitation/level-3-airports); the current order establishes temporary scheduling limits.

As of May 1, 2026, the cap stands at 2,708 daily operations, with an effective date of June 2, 2026.

**Exact later resolution packet**

The question resolves NO. It asks whether, between May 1, 2026 and June 1, 2026 (23:59 UTC), the FAA published an official order, amendment, or notice changing the daily operations cap at Chicago O'Hare from the 2,708 figure established in the April 16, 2026 order (Federal Register Document No. 2026-07665).

Evidence:
- A direct search of the Federal Register limited to FAA documents mentioning "O'Hare" published between May 1 and June 1, 2026 returned "No documents were found" [ba4ad7]. This means no FAA order, amendment, or notice was published in that window — let alone one changing the cap number.
- The only amendment to the original order was Federal Register Document No. 2026-08163, published April 27, 2026, which solely changed the effective date from May 17 to June 2, 2026 (https://www.federalregister.gov/documents/2026/04/27/2026-08163/). Per the question's clarifications, an effective-date change does NOT trigger YES, and in any case it was published in April, outside the May 1–June 1 window.
- Numerous contemporaneous news reports from late April and May 2026 (e.g., CBS News Chicago, Chicago Business, NBC Chicago) consistently state the cap remained at 2,708 operations per day from June 2 through October 24, 2026, and that airlines (notably United) responded by cutting their schedules to fit under the 2,708 figure — confirming the cap number itself was unchanged.

Because the 2,708 daily operations cap remained unchanged as of 23:59 UTC on June 1, 2026, and no qualifying FAA order/amendment/notice was published in the resolution window, the question resolves NO.

The daily operations limit remained exactly 2,708 (neither increased nor decreased) as of the deadline.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-62. `e32addcd-ec31-5bb1-9ba9-4965c5e32803`

- Present date: `2026-05-03 04:00:03.444805`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the U.S. Department of Education announce a delay to the July 1, 2026, implementation date of the Workforce Pell Grant program by June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, between May 1, 2026, and June 1, 2026 (inclusive, 11:59 PM ET), the U.S. Department of Education issues an official announcement explicitly stating that the July 1, 2026, implementation date for the Workforce Pell Grant program is delayed, postponed, or moved to a later date. Qualifying announcements include:

- A notice published in the Federal Register (https://www.federalregister.gov/)
- A Dear Colleague Letter or Electronic Announcement posted on the Federal Student Aid Partners site (https://fsapartners.ed.gov/)
- An official press release on the ED website (https://www.ed.gov/about/news/press-releases)

A "delay" is defined as any official statement by ED that the statutory or regulatory effective date for Workforce Pell Grant disbursements will not be July 1, 2026, as originally scheduled. This includes formal postponement of the final rule's effective date, an announcement of a phased or partial rollout that explicitly defers Pell disbursements beyond July 1, 2026, or a statement that institutions cannot begin disbursing Workforce Pell funds on July 1, 2026. It does not include informal commentary, unofficial statements, or delays in ancillary guidance that do not change the effective date for Pell disbursements.

The question resolves as **No** if no such official announcement is made by 11:59 PM ET on June 1, 2026.

The "Workforce Pell Grant program" refers to the expansion of Pell Grant eligibility to eligible workforce programs (short-term credential programs of 150–599 clock hours) as established by the Working Families Tax Cuts Act and codified in proposed regulations at Federal Register Document 2026-04520 [Federal Register :: ACCOUNTABILITY IN HIGHER EDUCATION ...](https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant).

**Pre-cutoff background**

The Workforce Pell Grant program, established by the Working Families Tax Cuts Act (part of the "One Big Beautiful Bill Act" signed into law in 2025), extends federal Pell Grant eligibility to short-term "eligible workforce programs" of 150–599 clock hours that can be completed in as little as 8–15 weeks. The program is statutorily scheduled to launch on July 1, 2026 [Federal Register :: ACCOUNTABILITY IN HIGHER EDUCATION ...](https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant).

On March 6, 2026, the U.S. Department of Education (ED) published a Notice of Proposed Rulemaking (NPRM) in the Federal Register (Document 2026-04520, 91 FR 11378) to codify the regulations necessary for implementation [Federal Register :: ACCOUNTABILITY IN HIGHER EDUCATION ...](https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant). The public comment period closed on April 8, 2026 [https://www.ed.gov/about/news/press-release/us-department-of-education-issues-proposed-rules-implement-working-families-tax-cuts-acts-workforce-pell-grants](https://www.ed.gov/about/news/press-release/us-department-of-education-issues-proposed-rules-implement-working-families-tax-cuts-acts-workforce-pell-grants). ED is currently reviewing comments and may revise the regulations before issuing a final rule.

Implementation requires complex rulemaking, state-level lists defining "high-skill, high-wage, or in-demand" occupations, institutional readiness (including a "70/70" performance standard), and accreditation requirements. Given that the final rule has not yet been published as of May 1, 2026, and the launch date is only two months away, there is meaningful uncertainty about whether the July 1, 2026, timeline will hold.

Key sources:
- Federal Register NPRM: https://www.federalregister.gov/documents/2026/03/09/2026-04520/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant
- ED press release: https://www.ed.gov/about/news/press-release/us-department-of-education-issues-proposed-rules-implement-working-families-tax-cuts-acts-workforce-pell-grants
- Regulations.gov docket: https://www.regulations.gov/docket/ED-2026-OPE-0133

**Exact later resolution packet**

The question asked whether, between May 1, 2026 and June 1, 2026 (11:59 PM ET), the U.S. Department of Education (ED) issued an official announcement explicitly stating that the July 1, 2026 implementation date for the Workforce Pell Grant program (short-term programs of 150–599 clock hours) is delayed, postponed, or moved to a later date.

What actually happened during the window:
- On May 18–19, 2026, ED issued the FINAL RULE for the Workforce Pell Grant program ("Accountability in Higher Education and Access Through Demand-Driven Workforce Pell," Document 2026-10013), published in the Federal Register on May 19, 2026 (https://www.federalregister.gov/documents/2026/05/19/2026-10013/...).
- The final rule set an effective date of July 20, 2026 for the regulations, BUT explicitly permitted early implementation beginning July 1, 2026. The Federal Register final rule states: "The Secretary is exercising her authority under HEA section 482(c) to permit early implementation of all regulations pertaining to eligible workforce programs beginning July 1, 2026." [Accountability in Higher Education and Access Through Demand ...](https://www.federalregister.gov/documents/2026/05/19/2026-10013/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant)
- ED's official Fact Sheet (https://www.ed.gov/media/document/workforce-pell-grant-final-rule-fact-sheet-114075.pdf) similarly states: "The final rule's provisions related to eligible workforce programs will be effective as of July 20, 2026, with an option for early implementation on July 1, 2026, at the discretion of each institution." [[PDF] Fact Sheet: Trump Administration Implements Workforce Pell Grant ...](https://www.ed.gov/media/document/workforce-pell-grant-final-rule-fact-sheet-114075.pdf)

Why this resolves NO:
- The resolution criteria define a "delay" as an official ED statement that the effective date for Workforce Pell Grant DISBURSEMENTS "will not be July 1, 2026, as originally scheduled," including a phased/partial rollout that "explicitly defers Pell disbursements beyond July 1, 2026," or a statement that "institutions cannot begin disbursing Workforce Pell funds on July 1, 2026."
- The final rule does the opposite: it expressly authorizes institutions to begin Workforce Pell on July 1, 2026 (early implementation). Disbursements are NOT deferred beyond July 1; institutions retain the option to disburse on July 1, 2026. [Accountability in Higher Education and Access Through Demand ...](https://www.federalregister.gov/documents/2026/05/19/2026-10013/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant)[[PDF] Fact Sheet: Trump Administration Implements Workforce Pell Grant ...](https://www.ed.gov/media/document/workforce-pell-grant-final-rule-fact-sheet-114075.pdf)
- While the default regulatory effective date is July 20, 2026, ED did not state that Pell disbursements cannot occur on July 1, 2026; it explicitly preserved July 1 as an available implementation date. This therefore does not meet the criteria's definition of a delay.
- No qualifying announcement (Federal Register notice, Dear Colleague Letter/Electronic Announcement, or ED press release) within the May 1–June 1, 2026 window stated that the July 1, 2026 disbursement date was postponed.

Accordingly, the question resolves NO (0).

Primary sources:
- Federal Register final rule (May 19, 2026): https://www.federalregister.gov/documents/2026/05/19/2026-10013/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant [Accountability in Higher Education and Access Through Demand ...](https://www.federalregister.gov/documents/2026/05/19/2026-10013/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant)
- ED Fact Sheet PDF: https://www.ed.gov/media/document/workforce-pell-grant-final-rule-fact-sheet-114075.pdf [[PDF] Fact Sheet: Trump Administration Implements Workforce Pell Grant ...](https://www.ed.gov/media/document/workforce-pell-grant-final-rule-fact-sheet-114075.pdf)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-63. `6c9e6111-3b05-5c07-ab7c-4ef8b079d788`

- Present date: `2026-05-15 10:18:37.598668`
- Source cutoff boundary: `2026-05-16` (encodes end of UTC day `2026-05-15`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will a proprietary OpenAI model (e.g., GPT-4o, GPT-5) be available on Google Cloud Vertex AI by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 and by 23:59 UTC on July 1, 2026, at least one proprietary (non-open-weight) OpenAI model is listed as available to Google Cloud customers on Google Cloud Vertex AI. A "proprietary OpenAI model" is any model developed by OpenAI that is not labeled "oss," "open-weight," or released under an open-source license — examples include GPT-4o, GPT-5, GPT-5.4, GPT-5.5, o1, o3, or any successor. Availability in any access tier counts, including limited preview, public preview, or general availability.

"Available on Google Cloud Vertex AI" means the model is listed on the official Google Cloud Vertex AI documentation for OpenAI models (https://docs.cloud.google.com/vertex-ai/generative-ai/docs/maas/openai) or announced as available on the Google Cloud Blog (https://cloud.google.com/blog) or OpenAI's newsroom (https://openai.com/news/). Availability on Google Cloud Marketplace alone does not count; the model must be accessible through Vertex AI's Model-as-a-Service or equivalent managed API offering.

If no proprietary OpenAI model meets these criteria by the deadline, the question resolves **No**.

**Pre-cutoff background**

On April 27, 2026, Microsoft and OpenAI ended their cloud exclusivity agreement, allowing OpenAI to offer its products on rival cloud platforms while Azure remains the primary cloud partner with an IP license through 2032. The next day, April 28, 2026, OpenAI launched its latest proprietary models (including GPT-5.4 and GPT-5.5) in limited preview on Amazon Bedrock, making AWS the first non-Microsoft cloud platform to host OpenAI's frontier models.

As of May 13, 2026, Google Cloud Vertex AI hosts only OpenAI's open-weight "GPT-OSS" models (gpt-oss-120b-maas and gpt-oss-20b-maas), which are released under the Apache 2.0 license [OpenAI models | Generative AI on Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/maas/openai). No proprietary OpenAI models (such as GPT-4o, GPT-5, o1, or similar closed-source models) are listed on the Vertex AI Model-as-a-Service documentation page [OpenAI models | Generative AI on Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/maas/openai). Separately, Reuters reported that OpenAI plans to use Google Cloud infrastructure for compute capacity, but this pertains to OpenAI running its own workloads on GCP, not to Google Cloud customers accessing OpenAI models through Vertex AI.

Google Cloud's own AI strategy centers on its proprietary Gemini model family, TPU hardware, and AI Hypercomputer stack [AI infrastructure at Next '26 | Google Cloud Blog](https://cloud.google.com/blog/products/compute/ai-infrastructure-at-next26). The competitive tension between Google's own AI offerings and hosting a rival's models creates genuine uncertainty about whether proprietary OpenAI models will appear on Vertex AI in the near term.

**Exact later resolution packet**

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

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-64. `cf5c503c-6607-5653-ac22-a85f845c9baf`

- Present date: `2026-05-29 03:09:45.905260`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will at least one liberal justice (Sonia Sotomayor, Elena Kagan, or Ketanji Brown Jackson) join the majority opinion in Trump v. Slaughter?

**Resolution criteria**

This question resolves **Yes** if at least one of the three liberal justices—Sonia Sotomayor, Elena Kagan, or Ketanji Brown Jackson—fully joins the majority opinion (or the opinion of the Court/judgment of the Court) in Trump v. Slaughter (Docket No. 25-332), as reflected in the official opinion published on the U.S. Supreme Court website (https://www.supremecourt.gov/opinions/slipopinions.aspx).

**Definitions:**
- **"Joins" the majority opinion** means the justice's name appears in the list of justices who joined the opinion of the Court in full (i.e., without qualification such as "joining in part"). A justice who "joins in part" does NOT count as joining for purposes of this question.
- A justice who writes or joins only a **concurring opinion** (including a "concurring in the judgment" opinion) without joining the majority opinion in full does **not** cause this question to resolve Yes. The question specifically asks about joining the majority opinion.
- A justice who **dissents** or **dissents in part** does not count.

The ruling must be issued on or after May 12, 2026 (12:00 ET) and no later than July 1, 2026 (11:59 PM ET). If no opinion is issued in this window, the question resolves **No**.

**Resolution source:** The official slip opinion published at https://www.supremecourt.gov/opinions/slipopinions.aspx. The syllabus and opinion header list which justices joined the opinion of the Court.

**Pre-cutoff background**

Trump v. Slaughter (Docket No. 25-332) is a pending U.S. Supreme Court case concerning whether the President may remove Federal Trade Commission commissioners without cause, directly challenging the 1935 precedent Humphrey's Executor v. United States, which upheld Congress's power to restrict presidential removal of FTC commissioners to cases of "inefficiency, neglect of duty, or malfeasance in office." The Trump administration argues these for-cause removal protections violate the separation of powers [Trump v. Slaughter - Wikipedia](https://en.wikipedia.org/wiki/Trump_v._Slaughter).

Oral arguments were heard on December 8, 2025. During arguments, the conservative justices appeared sympathetic to the administration's position, while the three liberal justices—Sonia Sotomayor, Elena Kagan, and Ketanji Brown Jackson—expressed significant concern about expanding presidential removal power [Trump v. Slaughter - Wikipedia](https://en.wikipedia.org/wiki/Trump_v._Slaughter). As of the latest available information, no decision has been issued [Trump v. Slaughter - Wikipedia](https://en.wikipedia.org/wiki/Trump_v._Slaughter). The Court's current term ends in late June or early July 2026, and the decision is expected by then.

A key question for forecasters is whether the ruling will be narrow (e.g., distinguishing the FTC's current structure from Humphrey's Executor without formally overruling it) or broad (fully overruling Humphrey's Executor). A narrower ruling could potentially attract one or more liberal justices to join or concur, while a sweeping overruling would almost certainly produce a sharp ideological split. Analysis from SCOTUSblog has explored both narrow and broad ruling paths (https://www.scotusblog.com/2025/10/is-humphreys-executor-headed-for-slaughter/).

**Exact later resolution packet**

The question resolves NO (0).

**Timing (antecedent/window check):** The Supreme Court issued its decision in Trump v. Slaughter (Docket No. 25-332) on June 29, 2026. This falls squarely within the required resolution window of May 12, 2026 (12:00 ET) through July 1, 2026 (11:59 PM ET). The official slip opinion is published at https://www.supremecourt.gov/opinions/25pdf/25-332_qn12.pdf [[PDF] 25-332 Trump v. Slaughter (06/29/2026) - Supreme Court](https://www.supremecourt.gov/opinions/25pdf/25-332_qn12.pdf), reachable via the Court's slip opinions page (https://www.supremecourt.gov/opinions/slipopinions.aspx).

**Join status (the substantive test):** The official opinion header/syllabus states verbatim: "ROBERTS, C. J., delivered the opinion of the Court, in which ALITO, GORSUCH, KAVANAUGH, and BARRETT, JJ., joined, and in which THOMAS, J., joined as to all but Part III–B. GORSUCH, J., filed a concurring opinion. SOTOMAYOR, J., filed a dissenting opinion, in which KAGAN and JACKSON, JJ., joined." [[PDF] 25-332 Trump v. Slaughter (06/29/2026) - Supreme Court](https://www.supremecourt.gov/opinions/25pdf/25-332_qn12.pdf)

Thus the majority opinion (a 6-3 decision holding the FTC's for-cause removal protections unconstitutional) was joined only by Chief Justice Roberts and Justices Alito, Gorsuch, Kavanaugh, Barrett, and Thomas (Thomas except Part III–B). None of the three liberal justices appears in the majority join list. Justice Sotomayor wrote the dissent, joined in full by Justices Kagan and Jackson [[PDF] 25-332 Trump v. Slaughter (06/29/2026) - Supreme Court](https://www.supremecourt.gov/opinions/25pdf/25-332_qn12.pdf) [Trump v. Slaughter (Independent Agencies) (25-332) - SCOTUSblog](https://www.scotusblog.com/cases/trump-v-slaughter-2/).

**Conclusion:** The resolution criteria require that at least one of Sotomayor, Kagan, or Jackson fully join the majority opinion of the Court. All three instead dissented. Because none joined the majority opinion, the question resolves NO (0). This is corroborated by SCOTUSblog, which reports the judgment was "Reversed and remanded, 6-3, in an opinion by John Roberts on Jun 29, 2026," with Kagan's/Sotomayor's/Jackson's participation confined to the dissent [Trump v. Slaughter (Independent Agencies) (25-332) - SCOTUSblog](https://www.scotusblog.com/cases/trump-v-slaughter-2/).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):
