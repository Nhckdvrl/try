# Rationale coding batch - model qwen3-8b (G24A reversibility audit, step 4)

One section per exact-evidence group (53 total, gnum matches the
classification CSV). Read EVERY section fully. Labels + output
format: g24a_reversibility_v1_coding_rubric.md

## gnum 1 sha=02a240f095 source=fever type=explicit_negation
EVIDENCE: He has received several awards and recognition for his work, including the National Film Award for Best Director for his fourth feature film Naan Kadavul (2009).
INC claim (supported by evidence): [g24a_fever_193540] Bala has received recognition for his work in film.
  values: admit_post=100.0 -> exclude_post=100.0
  exclude_post reasoning: The claim states that Bala has received recognition for his work in film. Evidence E, which mentions awards and recognition, is excluded and should not influence the judgment.
DEC claim (refuted by evidence): [g24a_fever_193532] Bala has received zero recognition for his work.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The claim states Bala has received zero recognition, but Evidence E directly contradicts this by mentioning multiple awards and recognition.

## gnum 2 sha=02c269369d source=fever type=numeric_value
EVIDENCE: Ralph Fults (January 23, 1911 -- March 16, 1993) was a Depression-era outlaw and escape artist associated with Raymond Hamilton, Bonnie Parker and Clyde Barrow of the Barrow Gang.
INC claim (supported by evidence): [g24a_fever_223774] The Barrow Gang is a criminal organization that Ralph Fults was associated with.
  values: admit_post=100.0 -> exclude_post=100.0
  exclude_post reasoning: The evidence directly supports the claim by naming Ralph Fults as an associate of the Barrow Gang.
DEC claim (refuted by evidence): [g24a_fever_223771] Ralph Fults was born in 1993.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The claim states Ralph Fults was born in 1993, but the evidence indicates he died in 1993, implying he was not born that year. The evidence directly contradicts the claim.

## gnum 3 sha=0ad89d58b1 source=scifact type=antonym_opposite
EVIDENCE: Moreover, KDM4E plays a more crucial role in IVF and SCNT embryonic development, and overexpression of KDM4E can restore the global transcriptome, improve blastocyst formation and increase the cloning efficiency of SCNT embryos.
INC claim (supported by evidence): [g24a_scifact_1035] Overexpression of KDM4E improves reprogramming efficiency in SCNT experiments.
  values: admit_post=100.0 -> exclude_post=0.3
  exclude_post reasoning: The claim suggests a direct link between KDM4E overexpression and improved reprogramming efficiency in SCNT, but the provided evidence is excluded. The ruling indicates that the evidence should not influence the judgment.
DEC claim (refuted by evidence): [g24a_scifact_1034] Removal of H3K9me3 by ectopic expression of other H3K9 demethylases decreases reprogramming efficiency in SCNT experiments.
  values: admit_post=59.7 -> exclude_post=0.0
  exclude_post reasoning: The evidence provided contradicts the claim by showing that overexpression of KDM4E improves SCNT efficiency, not decreases it.

## gnum 4 sha=0bab0a612e source=scifact type=antonym_opposite
EVIDENCE: The tumorigenic potential of GSCs was decreased with A20 targeting, resulting in increased survival of mice bearing human glioma xenografts. Although inactivating mutations in A20 in lymphoma suggest A20 can act as a tumor suppressor, similar point mutations have not been identified through glioma genomic sequencing: in fact, our data suggest A20 may function as a tumor enhancer in glioma through promotion of GSC survival.
INC claim (supported by evidence): [g24a_scifact_1136] TNFAIP3 is a tumor enhancer in glioblastoma.
  values: admit_post=89.3 -> exclude_post=0.2
  exclude_post reasoning: The evidence provided contradicts the claim by suggesting A20 may function as a tumor enhancer in glioma, aligning with the claim. However, the ruling excludes this evidence, so it cannot be used to support the claim.
DEC claim (refuted by evidence): [g24a_scifact_1137] TNFAIP3 is a tumor suppressor in glioblastoma.
  values: admit_post=33.3 -> exclude_post=4.3
  exclude_post reasoning: The evidence provided contradicts the claim by suggesting A20 may function as a tumor enhancer in glioma rather than a tumor suppressor.

## gnum 5 sha=0f5ba488f4 source=scifact type=numeric_value
EVIDENCE: Even if only 7% of patients awaiting kidney transplantation participated in an optimized national KPD program, the health care system could save as much as $750 million.
INC claim (supported by evidence): [g24a_scifact_1185] The US health care system can save up to $750 million if 7% of patients waiting for kidney transplants participate in the optimized national kidney paired donation program.
  values: admit_post=100.0 -> exclude_post=0.0
  exclude_post reasoning: The claim is presented with evidence that is explicitly excluded, leaving no supporting data to assess its validity. Without any additional information or evidence to evaluate the claim, its truth cannot be determined.
DEC claim (refuted by evidence): [g24a_scifact_1184] The US health care system can save up to $5 billion if 7% of patients waiting for kidney transplants participate in the optimized national kidney paired donation program.
  values: admit_post=37.3 -> exclude_post=34.4
  exclude_post reasoning: The claim suggests a $5 billion savings, but the evidence only supports $750 million. The discrepancy in scale reduces confidence in the claim's accuracy.

## gnum 6 sha=130ca6d4a1 source=scifact type=antonym_opposite
EVIDENCE: Treatment with the G4-stabilizing compound pyridostatin (PDS) increases telomere fragility in BRCA2-deficient cells, suggesting that G4 formation drives telomere instability.
INC claim (supported by evidence): [g24a_scifact_1000] Pyridostatin stabilizes the G - quadruplex in the telomeric region.
  values: admit_post=77.9 -> exclude_post=20.4
  exclude_post reasoning: The evidence provided contradicts the claim by suggesting that pyridostatin increases telomere fragility, implying it may destabilize rather than stabilize G-quadruplexes.
DEC claim (refuted by evidence): [g24a_scifact_990] Pyridostatin decreases telomere fragility in BRCA2-deficient cells.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence presented contradicts the claim by indicating that pyridostatin increases, rather than decreases, telomere fragility in BRCA2-deficient cells.

## gnum 7 sha=16327e7b59 source=scifact type=antonym_opposite
EVIDENCE: In vivo, these antibodies slowed the growth of multiple established CRPC xenografts, blocked local invasion and metastasis and, at higher doses, led to complete regression. Therapeutic targeting of this factor with monoclonal antibodies may have considerable clinical benefit.
INC claim (supported by evidence): [g24a_scifact_805] Monoclonal antibody targeting of N-cadherin inhibits metastasis.
  values: admit_post=90.5 -> exclude_post=0.0
  exclude_post reasoning: The evidence provided is excluded and thus cannot be considered in the evaluation. Since the only evidence is excluded, the likelihood cannot be determined from the given information.
DEC claim (refuted by evidence): [g24a_scifact_802] Monoclonal antibody targeting of N-cadherin encourages metastasis.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence presented directly contradicts the claim by showing that monoclonal antibodies targeting N-cadherin inhibit metastasis rather than encourage it.

## gnum 8 sha=167f30ddc2 source=scifact type=explicit_negation
EVIDENCE: After adjusting for age, body mass index, race, current smoking status, and recent hormonal contraceptive use, women with low AMH values (<0.7 ng/mL [n = 84]) did not have a significantly different predicted probability of conceiving by 6 cycles of attempt (65%; 95% CI, 50%-75%) compared with women (n = 579) with normal values (62%; 95% CI, 57%-66%) or by 12 cycles of attempt (84% [95% CI, 70%-91%] vs 75% [95% CI, 70%-79%], respectively). Women with high serum FSH values (>10 mIU/mL [n = 83]) did not have a significantly different predicted probability of conceiving after 6 cycles of attempt (63%; 95% CI, 50%-73%) compared with women (n = 654) with normal values (62%; 95% CI, 57%-66%) or after 12 cycles of attempt (82% [95% CI, 70%-89%] vs 75% [95% CI, 70%-78%], respectively). Women with high urinary FSH values (>11.5 mIU/mg creatinine [n = 69]) did not have a significantly different predicted probability of conceiving after 6 cycles of attempt (61%; 95% CI, 46%-74%) compared with women (n = 660) with normal values (62%; 95% CI, 58%-66%) or after 12 cycles of attempt (70% [95% CI, 54%-80%] vs 76% [95% CI, 72%-80%], respectively). Inhibin B levels (n = 737) were not associated with the probability of conceiving in a given cycle (hazard ratio per 1-pg/mL increase, 0.999; 95% CI, 0.997-1.001). Conclusions and Relevance Among women aged 30 to 44 years without a history of infertility who had been trying to conceive for 3 months or less, biomarkers indicating diminished ovarian reserve compared with normal ovarian reserve were not associated with reduced fertility.
INC claim (supported by evidence): [g24a_scifact_39] A diminished ovarian reserve does not solely indicate infertility in an a priori non-infertile population.
  values: admit_post=100.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence presented contradicts the claim by showing that diminished ovarian reserve biomarkers were not associated with reduced fertility in a non-infertile population. The study's conclusion directly challenges the claim's assertion.
DEC claim (refuted by evidence): [g24a_scifact_40] A diminished ovarian reserve is a very strong indicator of infertility, even in an a priori non-infertile population.
  values: admit_post=24.7 -> exclude_post=0.0
  exclude_post reasoning: The evidence presented contradicts the claim by showing that biomarkers of diminished ovarian reserve were not associated with reduced fertility in the studied population.

## gnum 9 sha=191c8c6d12 source=scifact type=explicit_negation
EVIDENCE: Patch clamp recordings showed that activity-induced LTP at identified synapses between nociceptors and spinal neurons projecting to the periaqueductal grey (PAG) was completely abolished in SNS-PKG-I(-/-) mice, although basal synaptic transmission was not affected.
INC claim (supported by evidence): [g24a_scifact_912] PKG-I plays an essential role in expression of spinal long term potentiation in PKG-I knockout mice.
  values: admit_post=100.0 -> exclude_post=98.9
  exclude_post reasoning: The evidence directly contradicts the claim by showing that LTP is abolished in PKG-I knockout mice, suggesting PKG-I is essential for LTP.
DEC claim (refuted by evidence): [g24a_scifact_910] PKG-I does not have a large impact on expression of spinal long term potentiation in PKG-I knockout mice.
  values: admit_post=100.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence directly contradicts the claim by showing that PKG-I is essential for LTP in the specified neural pathway.

## gnum 10 sha=206f9579ad source=scifact type=antonym_opposite
EVIDENCE: We found that the response of memory, but not naive, CD4+ T cells enhances production of multiple innate inflammatory cytokines and chemokines (IICs) in the lung and that, during influenza infection, this leads to early control of virus.
INC claim (supported by evidence): [g24a_scifact_1348] Upon viral challenge, influenza-specific memory CD4+ T cells greatly enhance the early production of inflammatory chemokines in the lung.
  values: admit_post=100.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence provided supports the claim by showing that memory CD4+ T cells enhance the production of inflammatory chemokines in the lung during influenza infection. However, the ruling excludes this evidence from consideration.
DEC claim (refuted by evidence): [g24a_scifact_1347] Upon viral challenge, influenza-specific memory CD4+ T cells greatly diminish the early production of inflammatory chemokines in the lung.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The claim suggests memory CD4+ T cells reduce early inflammatory chemokine production, while the evidence states memory CD4+ T cells enhance production of inflammatory cytokines and chemokines, leading to early viral control. These statements are contradictory.
  [extra DEC item, context only, do not label: g24a_scifact_379] Enhanced early production of inflammatory chemokines damages viral control in the lung.
    exclude_post value=0.0 reasoning: The evidence presented contradicts the claim by showing that enhanced early production of inflammatory chemokines actually aids in viral control during influenza infection.

## gnum 11 sha=23e2026256 source=scifact type=explicit_negation
EVIDENCE: Patients who used azathioprine, methotrexate, mycophenolate mofetil, ciclosporin, systemic corticosteroids, or dapsone had overall and cancer mortality similar to that of patients who never took immunosuppressive drugs. CONCLUSIONS Most commonly used immunosuppressive drugs do not seem to increase overall or cancer mortality.
INC claim (supported by evidence): [g24a_scifact_1125] Systemic immunosuppressive (IS) therapy does not enhance the chance of cancer mortality in patients with inflammatory eye disease (IED)
  values: admit_post=100.0 -> exclude_post=98.9
  exclude_post reasoning: The claim suggests that systemic immunosuppressive therapy does not increase cancer mortality in patients with inflammatory eye disease. Evidence E, while relevant, is excluded from consideration.
DEC claim (refuted by evidence): [g24a_scifact_1126] Systemic immunosuppressive (IS) therapy increases the chance of cancer mortality in patients with inflammatory eye disease (IED)
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence directly contradicts the claim by showing no increased cancer mortality with common immunosuppressive drugs. The claim is not supported by the provided evidence.

## gnum 12 sha=2872aac67b source=scifact type=antonym_opposite
EVIDENCE: FGF21 deficiency causes a marked exacerbation of atherosclerotic plaque formation and premature death in apolipoprotein E(-/-) mice, which is accompanied by hypoadiponectinemia and severe hypercholesterolemia. Replenishment of FGF21 protects against atherosclerosis in apolipoprotein E(-/-)mice via 2 independent mechanisms, inducing the adipocyte production of adiponectin, which in turn acts on the blood vessels to inhibit neointima formation and macrophage inflammation, and suppressing the hepatic expression of the transcription factor sterol regulatory element-binding protein-2, thereby leading to reduced cholesterol synthesis and attenuation of hypercholesterolemia. CONCLUSIONS FGF21 protects against atherosclerosis via fine tuning the multiorgan crosstalk among liver, adipose tissue, and blood vessels.
INC claim (supported by evidence): [g24a_scifact_681] Lack of FGF21 in mice leads to atherosclerotic plaque formation.
  values: admit_post=100.0 -> exclude_post=100.0
  exclude_post reasoning: The evidence provided directly supports the claim by showing that FGF21 deficiency leads to atherosclerotic plaque formation in mice, with detailed mechanisms explained.
DEC claim (refuted by evidence): [g24a_scifact_683] Lack of FGF21 in mice slows the rate of atherosclerotic plaque formation.
  values: admit_post=100.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence presented contradicts the claim by showing that FGF21 deficiency exacerbates atherosclerosis, not slows it. The claim is therefore false.

## gnum 13 sha=295d1e6d1a source=fever type=explicit_negation
EVIDENCE: For its output, it might pass the message through unchanged for delivery to the user's mailbox, redirect the message for delivery elsewhere, or even throw the message away.
INC claim (supported by evidence): [g24a_fever_16224] Email filtering output is capable of throwing messages away.
  values: admit_post=100.0 -> exclude_post=56.0
  exclude_post reasoning: The claim states that email filtering can throw messages away, but the provided evidence is excluded. Without considering the excluded evidence, the claim's truth remains uncertain.
DEC claim (refuted by evidence): [g24a_fever_47403] Email filtering output is incapable of delivering unchanged messages.
  values: admit_post=0.0 -> exclude_post=30.2
  exclude_post reasoning: The claim states that email filtering output is incapable of delivering unchanged messages. Evidence E discusses possible actions (pass, redirect, discard), which does not directly address whether messages can be delivered unchanged.

## gnum 14 sha=2af684783a source=fever type=exclusive_alternative
EVIDENCE: Mirny was a 20-gun sloop-of-war of the Imperial Russian Navy, the second ship of the First Russian Antarctic Expedition in 1819 -- 1821, during which Faddey Bellingshausen (commander of the lead ship Vostok) and Mikhail Lazarev (commanding Mirny) circumnavigated the globe, discovered the continent of Antarctica and twice circumnavigated it, and discovered a number of islands and archipelagos in the Southern Ocean and the Pacific.
INC claim (supported by evidence): [g24a_fever_112438] The Mirny (sloop-of-war) was the second ship of the First Russian Antarctic Expedition.
  values: admit_post=100.0 -> exclude_post=81.8
  exclude_post reasoning: The claim states that the Mirny was the second ship of the First Russian Antarctic Expedition, which is supported by the evidence provided. However, the ruling excludes the evidence, so I cannot use it to assess the claim's likelihood.
  [extra INC item, context only, do not label: g24a_fever_120681] The Mirny (sloop-of-war) was an expedition's second ship.
    exclude_post value=99.9 reasoning: The claim states that the Mirny was an expedition's second ship, which aligns with the evidence indicating it was the second ship of the First Russian Antarctic Expedition. However, the ruling excludes the evidence, so it must not be considered.
DEC claim (refuted by evidence): [g24a_fever_45374] The Mirny (sloop-of-war) only sailed the Russian coast.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The claim states that the Mirny only sailed the Russian coast, but the evidence shows it participated in an Antarctic expedition and circumnavigated the globe, which contradicts the claim.

## gnum 15 sha=2ef7066db4 source=fever type=numeric_value
EVIDENCE: It was established on June 4, 1992 after the Chechen-Ingush Autonomous Soviet Socialist Republic was split in two.
INC claim (supported by evidence): [g24a_fever_43041] Ingushetia was established on June.
  values: admit_post=91.9 -> exclude_post=0.0
  exclude_post reasoning: The claim states a specific date, but the evidence provided is excluded. Without valid evidence, the claim cannot be confirmed.
DEC claim (refuted by evidence): [g24a_fever_101716] Ingushetia was established on the 2nd.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The claim states Ingushetia was established on the 2nd, but the evidence provided refers to June 4, 1992. Since the evidence is excluded, it cannot be used to assess the claim's validity.

## gnum 16 sha=3784e1e225 source=scifact type=antonym_opposite
EVIDENCE: Here we report a robust UCP1-independent thermogenic mechanism in beige fat that involves enhanced ATP-dependent Ca2+ cycling by sarco/endoplasmic reticulum Ca2+-ATPase 2b (SERCA2b) and ryanodine receptor 2 (RyR2). Conversely, enhanced Ca2+ cycling by activation of α1- and/or β3-adrenergic receptors or the SERCA2b-RyR2 pathway stimulates UCP1-independent thermogenesis in beige adipocytes.
INC claim (supported by evidence): [g24a_scifact_222] Ca2+ cycling is a UCP1-independent thermogenic mechanism.
  values: admit_post=100.0 -> exclude_post=100.0
  exclude_post reasoning: The evidence provided directly supports the claim by describing a UCP1-independent thermogenic mechanism involving Ca2+ cycling. The ruling to exclude the evidence contradicts the provided data, which strongly indicates the claim is true.
DEC claim (refuted by evidence): [g24a_scifact_221] Ca2+ cycling is a UCP1-dependent thermogenic mechanism.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence presented directly contradicts the claim by showing a UCP1-independent thermogenic mechanism involving Ca2+ cycling. The claim is therefore not supported by the provided evidence.

## gnum 17 sha=3c940c4ab6 source=scifact type=antonym_opposite
EVIDENCE: Tricyclics significantly reduced the number of days with tension-type headache and number of headache attacks from migraine than placebo (average standardised mean difference -1.29, 95% confidence interval -2.18 to -0.39 and -0.70, -0.93 to -0.48) but not compared with selective serotonin reuptake inhibitors (-0.80, -2.63 to 0.02 and -0.20, -0.60 to 0.19). Tricyclics were also more likely to reduce the intensity of headaches by at least 50% than either placebo (tension-type: relative risk 1.41, 95% confidence interval 1.02 to 1.89; migraine: 1.80, 1.24 to 2.62) or selective serotonin reuptake inhibitors (1.73, 1.34 to 2.22 and 1.72, 1.15 to 2.55). CONCLUSIONS Tricyclic antidepressants are effective in preventing migraine and tension-type headaches and are more effective than selective serotonin reuptake inhibitors, although with greater adverse effects.
INC claim (supported by evidence): [g24a_scifact_120] Antidepressants reduce the severity of migraines.
  values: admit_post=97.5 -> exclude_post=0.0
  exclude_post reasoning: The evidence provided discusses the effectiveness of tricyclic antidepressants in reducing migraines and tension-type headaches, but it is excluded from consideration. The claim is not supported by the included evidence.
DEC claim (refuted by evidence): [g24a_scifact_119] Antidepressants increase the severity of migraines.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence provided shows that tricyclic antidepressants are more effective than placebos and selective serotonin reuptake inhibitors in reducing migraine frequency and intensity, contradicting the claim.

## gnum 18 sha=418c9c7ded source=fever type=indirect_contradiction
EVIDENCE: Stanley "Tookie" Williams III (December 29, 1953 -- December 13, 2005) was an American gang member and convicted murderer, who was part of the West Side Crips, a street gang which has its roots in South Central Los Angeles in 1969.
INC claim (supported by evidence): [g24a_fever_137414] Stanley Williams lost his life in 2005.
  values: admit_post=100.0 -> exclude_post=100.0
  exclude_post reasoning: The claim states that Stanley Williams lost his life in 2005. Evidence E confirms that Stanley "Tookie" Williams III died on December 13, 2005.
DEC claim (refuted by evidence): [g24a_fever_110276] Stanley Williams is currently a college student in 2017.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The claim states Stanley Williams is a college student in 2017, but Evidence E confirms he was a convicted murderer who died in 2005. This directly contradicts the claim.
  [extra DEC item, context only, do not label: g24a_fever_99144] Stanley Williams stayed in Cuba his whole life.
    exclude_post value=0.0 reasoning: The claim states Stanley Williams stayed in Cuba his whole life, but the evidence provided confirms he was an American gang member from Los Angeles. The evidence directly contradicts the claim.

## gnum 19 sha=46ea5012c1 source=fever type=explicit_negation
EVIDENCE: Poseidon grossed $181,674,817 at the worldwide box office on a budget of $160 million.
INC claim (supported by evidence): [g24a_fever_5972] Poseidon had a budget of $160 million.
  values: admit_post=100.0 -> exclude_post=100.0
  exclude_post reasoning: The claim states Poseidon had a budget of $160 million, but the evidence provided refers to its box office gross, not its budget. Since the evidence is excluded, it cannot support the claim.
DEC claim (refuted by evidence): [g24a_fever_104021] Poseidon lacked a budget of $160 million.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence directly contradicts the claim by showing that Poseidon had the exact budget mentioned. The ruling excludes the evidence, but the claim is clearly false based on the provided data.

## gnum 20 sha=4763290d52 source=fever type=explicit_negation
EVIDENCE: He was recognizable by wrestling fans for his distinctively deep and raspy voice, his flamboyant ring attire, intensity exhibited in and out of the ring, using "Pomp and Circumstance" as his entrance music, and his signature catch phrase, "Oooh yeah!"
INC claim (supported by evidence): [g24a_fever_2739] Randy Savage can speak.
  values: admit_post=100.0 -> exclude_post=100.0
  exclude_post reasoning: The claim that Randy Savage can speak is directly supported by the evidence, which describes his recognizable voice. The ruling to exclude evidence E does not affect the factual basis of the claim.
DEC claim (refuted by evidence): [g24a_fever_96710] Randy Savage does not have a deep voice.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: Randy Savage's deep and raspy voice is well-documented in wrestling history and media. The evidence directly contradicts the claim.

## gnum 21 sha=4bc72d9ea8 source=scifact type=explicit_negation
EVIDENCE: These studies demonstrated that gynandromorph birds are genuine male:female chimaeras, and indicated that male and female avian somatic cells may have an inherent sex identity. In an example where female tissue was transplanted into a male host, donor cells contributing to the developing testis retained a female identity and expressed a marker of female function. Our study demonstrates that avian somatic cells possess an inherent sex identity and that, in birds, sexual differentiation is substantively cell autonomous.
INC claim (supported by evidence): [g24a_scifact_235] Cell autonomous sex determination in somatic cells occurs in Galliformes.
  values: admit_post=100.0 -> exclude_post=100.0
  exclude_post reasoning: The evidence provided directly supports the claim by showing that avian somatic cells have an inherent sex identity and that sexual differentiation is cell autonomous.
DEC claim (refuted by evidence): [g24a_scifact_233] Cell autonomous sex determination in somatic cells does not occur in Galliformes.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence directly contradicts the claim by showing that avian somatic cells have an inherent sex identity, supporting cell autonomous sex determination.

## gnum 22 sha=4c0fc60923 source=fever type=exclusive_alternative
EVIDENCE: Brick is a 2005 American neo-noir mystery film written and directed by Rian Johnson in his directorial debut, starring Joseph Gordon-Levitt.
INC claim (supported by evidence): [g24a_fever_211775] Brick (film) is a mystery film.
  values: admit_post=100.0 -> exclude_post=100.0
  exclude_post reasoning: The claim states that "Brick (film) is a mystery film." Evidence E confirms that "Brick" is a 2005 neo-noir mystery film.
DEC claim (refuted by evidence): [g24a_fever_211799] Brick (film) is a 2006 film only.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The claim states that "Brick (film) is a 2006 film only," but the evidence indicates it was released in 2005. Therefore, the claim is false.

## gnum 23 sha=53ae76df8c source=fever type=numeric_value
EVIDENCE: Directed by Frederik Du Chau and written by Joe Piscatella, Adam Rifkin, and Craig A. Williams, the film stars Jim Belushi, Peter Dinklage, John Slattery, and Patrick Warburton with the voice talents of Jason Lee, Amy Adams, and Brad Garrett.
INC claim (supported by evidence): [g24a_fever_93273] Amy Adams has a voice role in Underdog.
  values: admit_post=100.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence mentions Amy Adams as a voice talent in the film, which directly supports the claim. However, the ruling excludes this evidence, so it cannot be considered.
DEC claim (refuted by evidence): [g24a_fever_32505] Underdog stars nine American actors.
  values: admit_post=52.6 -> exclude_post=31.2
  exclude_post reasoning: The claim states that "Underdog" stars nine American actors. Evidence E lists several actors, but does not confirm the total number of American actors in the film. The claim's specific number (nine) is not supported or contradicted by the provided evidence.

## gnum 24 sha=5cd5ff81d8 source=scifact type=antonym_opposite
EVIDENCE: We found that CX3CR1 signaling promoted T(H)2 survival in the inflamed lungs, and injection of B cell leukemia/lymphoma-2 protein (BCl-2)-transduced CX3CR1-deficient T(H)2 cells into CX3CR1-deficient mice restored asthma.
INC claim (supported by evidence): [g24a_scifact_217] CX3CR1 on the Th2 cells promotes T cell survival
  values: admit_post=100.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence provided is excluded and thus cannot be used to assess the claim. The claim's truth value cannot be determined from the given information.
DEC claim (refuted by evidence): [g24a_scifact_216] CX3CR1 on the Th2 cells impairs T cell survival
  values: admit_post=92.9 -> exclude_post=0.0
  exclude_post reasoning: The evidence provided contradicts the claim by showing that CX3CR1 signaling promotes T(H)2 survival, not impairs it. The claim is therefore not supported by the given evidence.

## gnum 25 sha=5d3d709fe5 source=scifact type=antonym_opposite
EVIDENCE: Pharmacological activation of AMPK in myofibroblasts from lungs of humans with IPF display lower fibrotic activity, along with enhanced mitochondrial biogenesis and normalization of sensitivity to apoptosis. In a bleomycin model of lung fibrosis in mice, metformin therapeutically accelerates the resolution of well-established fibrosis in an AMPK-dependent manner. These studies implicate deficient AMPK activation in non-resolving, pathologic fibrotic processes, and support a role for metformin (or other AMPK activators) to reverse established fibrosis by facilitating deactivation and apoptosis of myofibroblasts.
INC claim (supported by evidence): [g24a_scifact_55] AMP-activated protein kinase (AMPK) activation reduces inflammation-related fibrosis in the lungs.
  values: admit_post=100.0 -> exclude_post=74.8
  exclude_post reasoning: The evidence provided suggests a plausible mechanism by which AMPK activation may reduce lung fibrosis, though it is limited to specific models and cell types. The claim is supported by experimental data but lacks broader validation across different fibrotic conditions and human studies.
DEC claim (refuted by evidence): [g24a_scifact_54] AMP-activated protein kinase (AMPK) activation increases inflammation-related fibrosis in the lungs.
  values: admit_post=56.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence presented suggests that AMPK activation may reduce, rather than increase, inflammation-related fibrosis in the lungs. The claim contradicts the findings of the evidence, which indicate a potential therapeutic role for AMPK activators in fibrosis.

## gnum 26 sha=6cc40aed98 source=scifact type=explicit_negation
EVIDENCE: Several members of the Kruppel-like factor (KLF) family of transcription factors play important roles in differentiation, survival, and trafficking of blood and immune cell types. Thus, our in vivo loss-of-function studies demonstrate that KLF4, previously shown to mediate proinflammatory signaling in human macrophages in vitro, is essential for differentiation of mouse inflammatory monocytes, and is involved in the differentiation of resident monocytes. In addition, inducible expression of KLF4 in the HL60 human acute myeloid leukemia cell line stimulated monocytic differentiation and enhanced 12-O-tetradecanoylphorbol 13-acetate induced macrophage differentiation, but blocked all-trans-retinoic acid induced granulocytic differentiation of HL60 cells. The inflammation-selective effects of loss-of-KLF4 and the gain-of-KLF4-induced monocytic differentiation in HL60 cells identify KLF4 as a key regulator of monocytic differentiation and a potential target for translational immune modulation.
INC claim (supported by evidence): [g24a_scifact_668] Klf4 is important for proper myeloid cell differentiation.
  values: admit_post=100.0 -> exclude_post=77.7
  exclude_post reasoning: The evidence provided discusses KLF4's role in myeloid cell differentiation, including inflammatory monocytes and HL60 cell differentiation. However, the claim specifically mentions "proper myeloid cell differentiation," which is broader than what the evidence directly supports.
DEC claim (refuted by evidence): [g24a_scifact_669] Klf4 is not required for proper myeloid cell differentiation.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence presented directly contradicts the claim by showing that KLF4 is essential for monocyte differentiation and influences myeloid cell fate.

## gnum 27 sha=6e220295f9 source=fever type=exclusive_alternative
EVIDENCE: AMGTV is an American family-oriented television network featuring television programming consisting of drama, sports, movies, entertainment, how-to, hunting and fishing, children's shows, and other features.
INC claim (supported by evidence): [g24a_fever_154542] AMGTV is a television network that is family-oriented.
  values: admit_post=100.0 -> exclude_post=100.0
  exclude_post reasoning: The claim states that AMGTV is a family-oriented television network. Evidence E directly supports this claim by describing the network's family-oriented nature and the types of programming it features.
DEC claim (refuted by evidence): [g24a_fever_106478] AMGTV airs only drama programming.
  values: admit_post=25.8 -> exclude_post=0.5
  exclude_post reasoning: The claim states that AMGTV airs only drama programming, but the evidence shows it includes a variety of genres beyond drama.

## gnum 28 sha=730b3fd4b4 source=scifact type=antonym_opposite
EVIDENCE: We identify a noncoding polymorphism in FOXO3A (rs12212067: T > G) at which the minor (G) allele, despite not being associated with disease susceptibility, is associated with a milder course of Crohn's disease and rheumatoid arthritis and with increased risk of severe malaria.
INC claim (supported by evidence): [g24a_scifact_1231] The minor G allele of FOXO3 is related to less severe symptoms of Crohn's Disease.
  values: admit_post=99.9 -> exclude_post=0.0
  exclude_post reasoning: The evidence provided is excluded, so it cannot be used to assess the claim's likelihood. Without valid evidence, the claim's truth cannot be determined.
DEC claim (refuted by evidence): [g24a_scifact_1232] The minor G allele of FOXO3 is related to more severe symptoms of Crohn's Disease.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence presented contradicts the claim by indicating that the minor G allele is associated with a milder course of Crohn's disease, not more severe symptoms.

## gnum 29 sha=7686390b19 source=fever type=exclusive_alternative
EVIDENCE: Shawn Carlson (born 1960) is an American physicist, science writer, and a STEM educator.
INC claim (supported by evidence): [g24a_fever_18752] Shawn Carlson writes about science.
  values: admit_post=100.0 -> exclude_post=100.0
  exclude_post reasoning: Shawn Carlson is identified as a physicist, science writer, and STEM educator, which directly supports the claim that he writes about science. The evidence is relevant and directly supports the claim.
DEC claim (refuted by evidence): [g24a_fever_787] Shawn Carlson is only German.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The claim states Shawn Carlson is only German, but the evidence shows he is an American physicist. The ruling excludes the evidence, so it cannot be used to assess the claim's likelihood.

## gnum 30 sha=76b97884b2 source=fever type=explicit_negation
EVIDENCE: Marcus Morgan Bentley (born 4 October 1967) is a British actor, broadcaster and voice-over artist.
INC claim (supported by evidence): [g24a_fever_201095] There is a British actor name Marcus Bentley.
  values: admit_post=100.0 -> exclude_post=95.9
  exclude_post reasoning: The claim states there is a British actor named Marcus Bentley. Evidence E provides information about a British actor named Marcus Morgan Bentley, which is relevant but excluded per the ruling.
DEC claim (refuted by evidence): [g24a_fever_201114] Marcus Bentley is incapable of being a voice-over artist.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The claim contradicts the evidence, which directly states Marcus Bentley is a voice-over artist. Since the evidence is excluded, the claim's truth cannot be determined from the provided information.

## gnum 31 sha=816626b7c4 source=scifact type=explicit_negation
EVIDENCE: Pregnant women with low serum 25-OHD levels had an increased risk of bacterial vaginosis and low birthweight infants but not delivery by caesarean section. Pregnant women with low 25-OHD levels had an increased risk of bacterial vaginosis and lower birth weight infants, but not delivery by caesarean section.
INC claim (supported by evidence): [g24a_scifact_1367] Vitamin D deficiency affects birth weight.
  values: admit_post=96.4 -> exclude_post=0.0
  exclude_post reasoning: The evidence provided is excluded and thus does not influence the judgment. The claim's truth cannot be determined from the excluded evidence.
DEC claim (refuted by evidence): [g24a_scifact_1370] Vitamin D deficiency is unrelated to birth weight.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence directly contradicts the claim by showing a link between vitamin D deficiency and low birth weight. The ruling to exclude the evidence does not affect the factual relationship presented.

## gnum 32 sha=82a409f17e source=fever type=numeric_value
EVIDENCE: The U.S. Census Bureau of 2012 reported a median household income of $87,894, which is higher than the California median of $70,231 and the national average of $62,527.
INC claim (supported by evidence): [g24a_fever_183411] Simi Valley, California, reported a median household income of $87,894 in the 2012 U.S. Census.
  values: admit_post=100.0 -> exclude_post=100.0
  exclude_post reasoning: The claim states a specific median household income for Simi Valley, California, from the 2012 U.S. Census. Evidence E provides supporting data but is excluded as per the ruling.
  [extra INC item, context only, do not label: g24a_fever_183417] Simi Valley, California, reported that its median household income was $87,894 in the 2012 U.S. Census.
    exclude_post value=100.0 reasoning: The claim is supported by the evidence provided, which directly cites the 2012 U.S. Census data. The evidence, though excluded by the ruling, aligns with the claim.
DEC claim (refuted by evidence): [g24a_fever_183420] Simi Valley, California, reported a median household income of $69,723 in the 2012 U.S. Census.
  values: admit_post=66.0 -> exclude_post=99.6
  exclude_post reasoning: The claim states a specific median household income for Simi Valley, California, from the 2012 U.S. Census. Evidence E provides broader median figures for California and the nation, which do not directly confirm or refute the specific claim about Simi Valley.

## gnum 33 sha=83377b6d9a source=scifact type=explicit_negation
EVIDENCE: Significantly increased odds of high anxiety symptoms were observed with higher exposure to PM2.5 for multiple averaging periods (for example, odds ratio per 10 µg/m(3) increase in prior one month average PM2.5: 1.12, 95% confidence interval 1.06 to 1.19; in prior 12 month average PM2.5: 1.15, 1.06 to 1.26). CONCLUSIONS Exposure to fine particulate matter (PM2.5) was associated with high symptoms of anxiety, with more recent exposures potentially more relevant than more distant exposures.
INC claim (supported by evidence): [g24a_scifact_399] Exposure to fine particulate air pollution is related to anxiety prevalence.
  values: admit_post=100.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence provided suggests a statistical association between PM2.5 exposure and anxiety symptoms, but it is excluded from consideration.
DEC claim (refuted by evidence): [g24a_scifact_400] Exposure to fine particulate air pollution is unrelated to anxiety prevalence.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence directly contradicts the claim by showing a significant association between PM2.5 exposure and anxiety symptoms. The ruling to exclude the evidence does not affect the factual relationship presented.

## gnum 34 sha=8ac8ca9fc8 source=fever type=explicit_negation
EVIDENCE: Hebe was the cupbearer for the gods and goddesses of Mount Olympus, serving their nectar and ambrosia, until she was married to Heracles (Roman equivalent: Hercules); her successor was the divine hero Ganymede.
INC claim (supported by evidence): [g24a_fever_33739] Hebe married Heracles.
  values: admit_post=100.0 -> exclude_post=56.8
  exclude_post reasoning: The claim that Hebe married Heracles is a matter of interpretation in classical mythology, with varying sources offering different accounts. However, the provided evidence is excluded, so it cannot be used to assess the claim's likelihood.
DEC claim (refuted by evidence): [g24a_fever_78778] Hebe was unmarried her entire life.
  values: admit_post=21.8 -> exclude_post=0.0
  exclude_post reasoning: The claim contradicts the evidence, which states Hebe was married to Heracles. The ruling excludes the evidence, so it cannot be used to assess the claim's likelihood.

## gnum 35 sha=8c9981f4b9 source=scifact type=antonym_opposite
EVIDENCE: Here we show that activation of ORX-synthesizing neurons is necessary for developing a panic-prone state in the rat panic model, and either silencing of the hypothalamic gene encoding ORX (Hcrt) with RNAi or systemic ORX-1 receptor antagonists blocks the panic responses.
INC claim (supported by evidence): [g24a_scifact_536] Hypocretin neurones induce panicprone state in rats.
  values: admit_post=100.0 -> exclude_post=90.5
  exclude_post reasoning: The evidence provided suggests a direct link between hypocretin (ORX) neurons and the development of a panic-prone state in rats, supported by experimental manipulation. The claim is strongly supported by the evidence, though the exclusion of evidence E may limit the full scope of validation.
DEC claim (refuted by evidence): [g24a_scifact_537] Hypocretin neurones suppress panicprone state in rats.
  values: admit_post=100.0 -> exclude_post=100.0
  exclude_post reasoning: The evidence suggests a direct link between hypocretin (ORX) and panic-prone states in rats, showing that suppressing ORX reduces panic responses. The claim is supported by the experimental findings presented in the evidence.

## gnum 36 sha=8cc84fdc4b source=fever type=exclusive_alternative
EVIDENCE: Later, this movie was dubbed into Malayalam, Japanese, and Korean under the same name.
INC claim (supported by evidence): [g24a_fever_166919] Baadshah was dubbed into Japanese.
  values: admit_post=100.0 -> exclude_post=99.6
  exclude_post reasoning: The claim states that "Baadshah was dubbed into Japanese," but the provided evidence mentions it was dubbed into Malayalam, Japanese, and Korean under the same name. Since the ruling excludes the evidence, we cannot rely on it to confirm the claim.
DEC claim (refuted by evidence): [g24a_fever_166951] Baadshah was only dubbed into English.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence provided contradicts the claim by indicating that the movie was dubbed into multiple languages beyond just English.

## gnum 37 sha=9909d08591 source=fever type=exclusive_alternative
EVIDENCE: The daughter of actors Barry and Lindsay Otto, and the sister of actress Gracie Otto, Brisbane-born Miranda began her acting career at age 18 in 1986, and has appeared in a variety of independent and major studio films.
INC claim (supported by evidence): [g24a_fever_23198] Miranda Otto began her film acting career at age 18.
  values: admit_post=100.0 -> exclude_post=100.0
  exclude_post reasoning: Miranda Otto's career began at age 18 in 1986, as stated in the evidence, which is excluded but still provides direct support for the claim. The claim aligns with the evidence provided, despite the ruling to exclude it.
DEC claim (refuted by evidence): [g24a_fever_40778] Miranda Otto is the mother of actress Gracie Otto.
  values: admit_post=57.1 -> exclude_post=56.2
  exclude_post reasoning: The evidence provided confirms Miranda Otto is the sister of Gracie Otto, which implies a familial relationship, though not explicitly confirming motherhood. The claim about being a mother is not directly supported by the evidence given.

## gnum 38 sha=a19309c246 source=fever type=exclusive_alternative
EVIDENCE: The Sugarland Express is a 1974 American crime drama film co-written and directed by Steven Spielberg in his theatrical feature film directorial debut.
INC claim (supported by evidence): [g24a_fever_203627] Steven Spielberg's directorial debut was the 1974 crime film The Sugarland Express.
  values: admit_post=100.0 -> exclude_post=99.5
  exclude_post reasoning: The claim states that Steven Spielberg's directorial debut was *The Sugarland Express*, which is supported by the evidence provided. However, the ruling excludes the evidence, so it cannot be used to assess the claim's likelihood.
DEC claim (refuted by evidence): [g24a_fever_203614] The 1976 thriller Duel was Steven Spielberg's directorial debut.
  values: admit_post=0.0 -> exclude_post=100.0
  exclude_post reasoning: The claim states that *Duel* was Spielberg's directorial debut, but the evidence refers to *The Sugarland Express* as his debut. Since the evidence is excluded, we must rely on other knowledge. *Duel* (1971) was indeed Spielberg's first feature film as a director.

## gnum 39 sha=a1d8bd2633 source=scifact type=numeric_value
EVIDENCE: RESULTS Of the 32,441 appendix samples 16 were positive for abnormal PrP, indicating an overall prevalence of 493 per million population (95% confidence interval 282 to 801 per million).
INC claim (supported by evidence): [g24a_scifact_5] 1/2000 in UK have abnormal PrP positivity.
  values: admit_post=100.0 -> exclude_post=90.5
  exclude_post reasoning: The claim states a prevalence of 1/2000, but the evidence shows 493 per million, which is approximately 1 in 2048. This is very close to the claim's figure, suggesting the claim is likely true.
DEC claim (refuted by evidence): [g24a_scifact_2] 1 in 5 million in UK have abnormal PrP positivity.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The claim states a prevalence of 1 in 5 million, but the evidence shows a much higher rate of 493 per million. The evidence directly contradicts the claim.

## gnum 40 sha=a8fc3392e2 source=scifact type=antonym_opposite
EVIDENCE: Immunoprecipitation studies of nucleosome core particles (NCPs) show that NCPs that contain both H3.3 and H2A.Z are even less stable than NCPs containing H3.3 and H2A.
INC claim (supported by evidence): [g24a_scifact_1040] Replacement of histone H2A with H2A.Z destabilizes nucleosomes.
  values: admit_post=88.9 -> exclude_post=50.5
  exclude_post reasoning: The evidence provided is excluded and thus cannot be considered. The claim's truth value is not directly supported or refuted by the excluded evidence.
DEC claim (refuted by evidence): [g24a_scifact_1041] Replacement of histone H2A with H2A.Z slows gene activation in yeasts by stabilizing +1 nucleosomes.
  values: admit_post=56.1 -> exclude_post=31.7
  exclude_post reasoning: The evidence provided contradicts the claim by suggesting that NCPs with H3.3 and H2A.Z are less stable, which is opposite to what the claim suggests about H2A.Z stabilizing nucleosomes.

## gnum 41 sha=b4210ea945 source=fever type=exclusive_alternative
EVIDENCE: Series 1 aired in Australia on ABC TV in mid-2007 (repeated 2009).
INC claim (supported by evidence): [g24a_fever_214973] Sensitive Skin's first series aired in a country.
  values: admit_post=100.0 -> exclude_post=33.3
  exclude_post reasoning: The claim states that "Sensitive Skin's first series aired in a country," which is a general statement. Evidence E provides specific information about a country (Australia) and a network (ABC TV), but it is excluded per the ruling. Without any other evidence, the claim remains too vague to confirm or deny definitively.
DEC claim (refuted by evidence): [g24a_fever_214989] Sensitive Skin's first series aired only on SBS TV.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The claim states that Sensitive Skin's first series aired only on SBS TV, but evidence shows it aired on ABC TV in Australia. This directly contradicts the claim.

## gnum 42 sha=b659bb4463 source=scifact type=antonym_opposite
EVIDENCE: Here, we show that mice lacking SIRT1 in steroidogenic factor 1 (SF1) neurons are hypersensitive to dietary obesity owing to maladaptive energy expenditure. Also, mutant mice have increased susceptibility to developing dietary T2DM due to insulin resistance in skeletal muscle. Conversely, mice overexpressing SIRT1 in SF1 neurons are more resistant to diet-induced obesity and insulin resistance due to increased energy expenditure and enhanced skeletal muscle insulin sensitivity.
INC claim (supported by evidence): [g24a_scifact_779] Mice lacking Sirt1 in Sf1-expressing neurons have increased susceptibility to diet-induced obesity and insulin resistance.
  values: admit_post=100.0 -> exclude_post=100.0
  exclude_post reasoning: The evidence directly supports the claim by showing that Sirt1 deficiency in SF1 neurons leads to increased diet-induced obesity and insulin resistance. The claim is well substantiated by the provided evidence.
DEC claim (refuted by evidence): [g24a_scifact_778] Mice lacking Sirt1 in Sf1-expressing neurons are immune to diet-induced obesity and insulin resistance.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence presented contradicts the claim by showing that Sirt1 deficiency in SF1 neurons leads to increased susceptibility to diet-induced obesity and insulin resistance, not immunity.

## gnum 43 sha=c048fb5c27 source=fever type=explicit_negation
EVIDENCE: Hickam has also written a number of best-selling memoirs and novels including the "Josh Thurlow" historical fiction novels.
INC claim (supported by evidence): [g24a_fever_216389] Homer Hickam is a writer of historical fiction books.
  values: admit_post=100.0 -> exclude_post=79.8
  exclude_post reasoning: The claim states Homer Hickam is a writer of historical fiction books. Evidence E refers to memoirs and novels, not exclusively historical fiction, and is excluded per instruction.
DEC claim (refuted by evidence): [g24a_fever_216390] Homer Hickam was incapable of writing anything for the Josh Thurlow novels.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The claim contradicts the evidence, which directly states Hickam wrote the Josh Thurlow novels.

## gnum 44 sha=c598c8dbb1 source=fever type=numeric_value
EVIDENCE: Principal photography commenced in June 2016 and filming locations include Delhi, Mumbai, Patna, Dumraon, Varanasi, New York City and Cape Town.
INC claim (supported by evidence): [g24a_fever_124341] Half Girlfriend's principal photography began in 2016.
  values: admit_post=100.0 -> exclude_post=100.0
  exclude_post reasoning: The claim states that principal photography began in 2016, while the evidence specifies it started in June 2016. Since the evidence is excluded, the specific date is not considered.
DEC claim (refuted by evidence): [g24a_fever_141838] Half Girlfriend's principal photography ended in January of 2016.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The claim states that principal photography ended in January 2016, but the evidence indicates filming started in June 2016, which directly contradicts the claim.
  [extra DEC item, context only, do not label: g24a_fever_47792] Half Girlfriend's principal photography began in May of 2016.
    exclude_post value=0.0 reasoning: The claim states the principal photography began in May 2016, while the evidence indicates it started in June 2016. The evidence directly contradicts the claim.

## gnum 45 sha=c963114af9 source=fever type=explicit_negation
EVIDENCE: Jones has never been on an NBA team with a losing record and has only missed the playoffs once -- with the Trail Blazers in 2007 -- 08.
INC claim (supported by evidence): [g24a_fever_66842] James Jones missed the playoffs once in 2007-2008.
  values: admit_post=100.0 -> exclude_post=10.7
  exclude_post reasoning: The claim states that James Jones missed the playoffs once in the 2007-2008 season, which aligns with the evidence provided. However, the evidence is excluded, so it cannot be used to assess the claim's likelihood.
DEC claim (refuted by evidence): [g24a_fever_68337] James Jones has never missed the playoffs.
  values: admit_post=59.1 -> exclude_post=38.5
  exclude_post reasoning: The claim states James Jones has never missed the playoffs, but the evidence indicates he missed the playoffs once with the Trail Blazers in 2007-08.

## gnum 46 sha=ce47287f7f source=fever type=explicit_negation
EVIDENCE: Night of the Living Dead is a 1968 American independent horror film, directed by George A. Romero, starring Duane Jones and Judith O'Dea.
INC claim (supported by evidence): [g24a_fever_105216] Night of the Living Dead is not a series of seven zombie horror films.
  values: admit_post=0.0 -> exclude_post=100.0
  exclude_post reasoning: The claim states that "Night of the Living Dead is not a series of seven zombie horror films." The provided evidence confirms it is a single 1968 film, not a series. This directly supports the claim.
DEC claim (refuted by evidence): [g24a_fever_148263] Night of the Living Dead is a series of works of art.
  values: admit_post=44.5 -> exclude_post=37.0
  exclude_post reasoning: The claim states that "Night of the Living Dead is a series of works of art," but the provided evidence only describes a single film from 1968. The evidence does not support the claim about it being a series.

## gnum 47 sha=e6af48c413 source=scifact type=explicit_negation
EVIDENCE: The inclusion of a visual screening component in the assessment did not result in improvements in self reported visual problems (pooled odds ratio 1.04:95% confidence interval 0.89 to 1.22). CONCLUSIONS Screening of asymptomatic older people in the community is not justified on present evidence.
INC claim (supported by evidence): [g24a_scifact_137] Asymptomatic visual impairment screening in elderly populations does not lead to improved vision.
  values: admit_post=98.4 -> exclude_post=0.2
  exclude_post reasoning: The evidence provided is excluded, so it cannot be used to assess the claim's likelihood. Without additional evidence, the claim's truth cannot be determined.
DEC claim (refuted by evidence): [g24a_scifact_138] Asymptomatic visual impairment screening in elderly populations leads to improved vision.
  values: admit_post=21.2 -> exclude_post=0.0
  exclude_post reasoning: The evidence provided contradicts the claim by showing no improvement in self-reported visual problems from screening. The claim is not supported by the given evidence.

## gnum 48 sha=ec9e00037c source=fever type=exclusive_alternative
EVIDENCE: The doll resides in a glass box at The Warrens' Occult Museum in Monroe, Connecticut.
INC claim (supported by evidence): [g24a_fever_102540] Annabelle is in the United States.
  values: admit_post=100.0 -> exclude_post=28.4
  exclude_post reasoning: The claim about Annabelle being in the United States is not directly supported or contradicted by the provided evidence. The evidence pertains to a doll's location, not Annabelle's.
DEC claim (refuted by evidence): [g24a_fever_103545] Annabelle is at The Museum of Natural History.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The claim and evidence refer to different locations and items, making the evidence irrelevant. The claim about Annabelle's location is not supported or contradicted by the provided evidence.

## gnum 49 sha=efe5c764ce source=fever type=explicit_negation
EVIDENCE: The club has won the FA Cup once, in 1976, and their highest-ever league finish was second in the First Division in 1983 -- 84.
INC claim (supported by evidence): [g24a_fever_224369] Southampton F.C. has won the FA Cup.
  values: admit_post=100.0 -> exclude_post=0.0
  exclude_post reasoning: The claim states Southampton F.C. has won the FA Cup, but the evidence provided only mentions one FA Cup win in 1976, which contradicts the claim's implication of a more recent or ongoing victory.
DEC claim (refuted by evidence): [g24a_fever_224370] Southampton F.C. has won zero FA Cups.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The claim states Southampton F.C. has won zero FA Cups, but Evidence E contradicts this by stating they won the FA Cup once in 1976. Since the ruling excludes Evidence E, the claim's truth is not supported by any valid evidence.

## gnum 50 sha=f320cab67b source=fever type=exclusive_alternative
EVIDENCE: Excuse My French is the debut studio album by American rapper French Montana.
INC claim (supported by evidence): [g24a_fever_208414] Excuse My French is the debut album of an artist.
  values: admit_post=100.0 -> exclude_post=100.0
  exclude_post reasoning: The claim states that "Excuse My French" is the debut album of an artist, but the evidence provided refers specifically to French Montana, an American rapper. Since the evidence is excluded, we cannot rely on it to confirm the claim.
DEC claim (refuted by evidence): [g24a_fever_208433] Excuse My French is only a single by French Montana.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The claim states that "Excuse My French" is a single by French Montana, while the evidence claims it is his debut studio album. These are conflicting statements about the same title.

## gnum 51 sha=f4d0aa5c71 source=scifact type=explicit_negation
EVIDENCE: Evidence was lacking for cognitive impairment for any headache type with or without brain lesions.
INC claim (supported by evidence): [g24a_scifact_501] Headaches are not correlated with cognitive impairment.
  values: admit_post=77.5 -> exclude_post=41.4
  exclude_post reasoning: Headaches and cognitive impairment are complex topics with varying research outcomes. The lack of evidence for a correlation does not definitively prove the claim.
DEC claim (refuted by evidence): [g24a_scifact_500] Headaches are correlated with cognitive impairment.
  values: admit_post=19.8 -> exclude_post=0.0
  exclude_post reasoning: The claim suggests a correlation between headaches and cognitive impairment, but the provided evidence contradicts this by stating there is a lack of evidence for cognitive impairment in any headache type.

## gnum 52 sha=fa68f098d6 source=fever type=numeric_value
EVIDENCE: In 2013 she was ranked as the second highest earning actress/models in Israel, behind Bar Refaeli, but ahead of Esti Ginzburg and Shlomit Malka, with the majority of her income coming from acting.
INC claim (supported by evidence): [g24a_fever_161222] Gal Gadot was ranked ahead of Shlomit Malka for Israel's highest earning actress/models.
  values: admit_post=98.8 -> exclude_post=0.0
  exclude_post reasoning: The claim is not supported by the provided evidence, which explicitly excludes the ranking of Gal Gadot ahead of Shlomit Malka. The evidence also states she was ranked second in 2013, not ahead of Shlomit Malka.
DEC claim (refuted by evidence): [g24a_fever_94603] Gal Gadot was ranked ahead of Bar Rafaeli for highest earning actress/models in Israel.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The claim contradicts the evidence, which states that Bar Refaeli was ranked ahead of Gal Gadot in 2013. The evidence explicitly excludes any influence on the judgment, so the claim is not supported.

## gnum 53 sha=fe39679ee7 source=fever type=numeric_value
EVIDENCE: The site was launched in February 2007 by Community Connect Inc..
INC claim (supported by evidence): [g24a_fever_204015] Glee.com is a website launched in the 2000s.
  values: admit_post=100.0 -> exclude_post=99.9
  exclude_post reasoning: The claim states Glee.com was launched in the 2000s, but the provided evidence specifies a launch date in 2007, which is still within the 2000s. However, since the evidence is excluded, it cannot be used to confirm or deny the claim.
DEC claim (refuted by evidence): [g24a_fever_203996] The website Glee.com was first launched in 2010.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The claim contradicts the evidence, which states the site was launched in 2007. The ruling excludes the evidence, so it cannot be used to assess the claim's likelihood.

