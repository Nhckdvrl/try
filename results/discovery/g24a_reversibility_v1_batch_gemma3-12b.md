# Rationale coding batch - model gemma3-12b (G24A reversibility audit, step 4)

One section per exact-evidence group (53 total, gnum matches the
classification CSV). Read EVERY section fully. Labels + output
format: g24a_reversibility_v1_coding_rubric.md

## gnum 1 sha=02a240f095 source=fever type=explicit_negation
EVIDENCE: He has received several awards and recognition for his work, including the National Film Award for Best Director for his fourth feature film Naan Kadavul (2009).
INC claim (supported by evidence): [g24a_fever_193540] Bala has received recognition for his work in film.
  values: admit_post=96.4 -> exclude_post=55.5
  exclude_post reasoning: The evidence is excluded, so we have no information to consider. Therefore, we must assess the claim based on general knowledge alone, which is insufficient to determine truth.
DEC claim (refuted by evidence): [g24a_fever_193532] Bala has received zero recognition for his work.
  values: admit_post=0.0 -> exclude_post=0.1
  exclude_post reasoning: The evidence directly contradicts the claim, stating Bala has received awards. Therefore, the claim is likely false.

## gnum 2 sha=02c269369d source=fever type=numeric_value
EVIDENCE: Ralph Fults (January 23, 1911 -- March 16, 1993) was a Depression-era outlaw and escape artist associated with Raymond Hamilton, Bonnie Parker and Clyde Barrow of the Barrow Gang.
INC claim (supported by evidence): [g24a_fever_223774] The Barrow Gang is a criminal organization that Ralph Fults was associated with.
  values: admit_post=88.9 -> exclude_post=51.3
  exclude_post reasoning: The evidence directly supports the claim, naming Ralph Fults as associated with members of the Barrow Gang. However, the instruction explicitly states the evidence must have zero influence, so I must disregard it.
DEC claim (refuted by evidence): [g24a_fever_223771] Ralph Fults was born in 1993.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence directly contradicts the claim, stating Ralph Fults was born in 1911. Therefore, the claim is certainly false.

## gnum 3 sha=0ad89d58b1 source=scifact type=antonym_opposite
EVIDENCE: Moreover, KDM4E plays a more crucial role in IVF and SCNT embryonic development, and overexpression of KDM4E can restore the global transcriptome, improve blastocyst formation and increase the cloning efficiency of SCNT embryos.
INC claim (supported by evidence): [g24a_scifact_1035] Overexpression of KDM4E improves reprogramming efficiency in SCNT experiments.
  values: admit_post=88.9 -> exclude_post=88.8
  exclude_post reasoning: The evidence directly supports the claim that KDM4E overexpression improves reprogramming efficiency in SCNT experiments, detailing transcriptome restoration, improved blastocyst formation, and increased cloning efficiency. Therefore, the claim is likely true.
DEC claim (refuted by evidence): [g24a_scifact_1034] Removal of H3K9me3 by ectopic expression of other H3K9 demethylases decreases reprogramming efficiency in SCNT experiments.
  values: admit_post=88.9 -> exclude_post=33.4
  exclude_post reasoning: The claim suggests a negative impact of H3K9me3 removal on reprogramming, while the evidence highlights a positive role for KDM4E (a demethylase) in improving embryonic development and cloning efficiency. Since the evidence contradicts the claim's core assertion, it cannot support the claim's truth.

## gnum 4 sha=0bab0a612e source=scifact type=antonym_opposite
EVIDENCE: The tumorigenic potential of GSCs was decreased with A20 targeting, resulting in increased survival of mice bearing human glioma xenografts. Although inactivating mutations in A20 in lymphoma suggest A20 can act as a tumor suppressor, similar point mutations have not been identified through glioma genomic sequencing: in fact, our data suggest A20 may function as a tumor enhancer in glioma through promotion of GSC survival.
INC claim (supported by evidence): [g24a_scifact_1136] TNFAIP3 is a tumor enhancer in glioblastoma.
  values: admit_post=77.8 -> exclude_post=66.7
  exclude_post reasoning: The evidence suggests a potential tumor-enhancing role for TNFAIP3 (A20) in glioblastoma through GSC survival, which aligns with the claim. However, the evidence also notes conflicting findings in lymphoma, introducing some uncertainty.
DEC claim (refuted by evidence): [g24a_scifact_1137] TNFAIP3 is a tumor suppressor in glioblastoma.
  values: admit_post=21.7 -> exclude_post=28.5
  exclude_post reasoning: The evidence directly contradicts the claim, suggesting A20 (which is the same as TNFAIP3) functions as a tumor enhancer rather than a suppressor in gliomas. Therefore, the evidence is not supportive of the claim.

## gnum 5 sha=0f5ba488f4 source=scifact type=numeric_value
EVIDENCE: Even if only 7% of patients awaiting kidney transplantation participated in an optimized national KPD program, the health care system could save as much as $750 million.
INC claim (supported by evidence): [g24a_scifact_1185] The US health care system can save up to $750 million if 7% of patients waiting for kidney transplants participate in the optimized national kidney paired donation program.
  values: admit_post=88.0 -> exclude_post=55.1
  exclude_post reasoning: The evidence directly restates the claim, offering no independent support or analysis. Therefore, without further evidence, the claim's truth is uncertain.
DEC claim (refuted by evidence): [g24a_scifact_1184] The US health care system can save up to $5 billion if 7% of patients waiting for kidney transplants participate in the optimized national kidney paired donation program.
  values: admit_post=56.4 -> exclude_post=54.7
  exclude_post reasoning: The claim states a $5 billion savings, while the evidence suggests a $750 million savings. Since the evidence contradicts the claim, and the evidence must be excluded, the claim's truth is uncertain.

## gnum 6 sha=130ca6d4a1 source=scifact type=antonym_opposite
EVIDENCE: Treatment with the G4-stabilizing compound pyridostatin (PDS) increases telomere fragility in BRCA2-deficient cells, suggesting that G4 formation drives telomere instability.
INC claim (supported by evidence): [g24a_scifact_1000] Pyridostatin stabilizes the G - quadruplex in the telomeric region.
  values: admit_post=64.6 -> exclude_post=29.7
  exclude_post reasoning: The evidence actually contradicts the claim, suggesting G4 stabilization leads to instability rather than stabilization. Therefore, the claim's likelihood is reduced.
DEC claim (refuted by evidence): [g24a_scifact_990] Pyridostatin decreases telomere fragility in BRCA2-deficient cells.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence directly contradicts the claim, stating pyridostatin *increases* telomere fragility rather than decreasing it. Therefore, the claim is highly unlikely to be true.

## gnum 7 sha=16327e7b59 source=scifact type=antonym_opposite
EVIDENCE: In vivo, these antibodies slowed the growth of multiple established CRPC xenografts, blocked local invasion and metastasis and, at higher doses, led to complete regression. Therapeutic targeting of this factor with monoclonal antibodies may have considerable clinical benefit.
INC claim (supported by evidence): [g24a_scifact_805] Monoclonal antibody targeting of N-cadherin inhibits metastasis.
  values: admit_post=88.2 -> exclude_post=51.2
  exclude_post reasoning: The evidence presented shows promising results in a controlled setting (xenografts), suggesting a potential mechanism for inhibiting metastasis. However, the exclusion of this evidence means it cannot be considered when evaluating the claim's truthfulness.
DEC claim (refuted by evidence): [g24a_scifact_802] Monoclonal antibody targeting of N-cadherin encourages metastasis.
  values: admit_post=11.1 -> exclude_post=2.5
  exclude_post reasoning: The evidence directly contradicts the claim, showing that antibody targeting *slowed* metastasis and even led to regression. Therefore, the claim is highly unlikely to be true.

## gnum 8 sha=167f30ddc2 source=scifact type=explicit_negation
EVIDENCE: After adjusting for age, body mass index, race, current smoking status, and recent hormonal contraceptive use, women with low AMH values (<0.7 ng/mL [n = 84]) did not have a significantly different predicted probability of conceiving by 6 cycles of attempt (65%; 95% CI, 50%-75%) compared with women (n = 579) with normal values (62%; 95% CI, 57%-66%) or by 12 cycles of attempt (84% [95% CI, 70%-91%] vs 75% [95% CI, 70%-79%], respectively). Women with high serum FSH values (>10 mIU/mL [n = 83]) did not have a significantly different predicted probability of conceiving after 6 cycles of attempt (63%; 95% CI, 50%-73%) compared with women (n = 654) with normal values (62%; 95% CI, 57%-66%) or after 12 cycles of attempt (82% [95% CI, 70%-89%] vs 75% [95% CI, 70%-78%], respectively). Women with high urinary FSH values (>11.5 mIU/mg creatinine [n = 69]) did not have a significantly different predicted probability of conceiving after 6 cycles of attempt (61%; 95% CI, 46%-74%) compared with women (n = 660) with normal values (62%; 95% CI, 58%-66%) or after 12 cycles of attempt (70% [95% CI, 54%-80%] vs 76% [95% CI, 72%-80%], respectively). Inhibin B levels (n = 737) were not associated with the probability of conceiving in a given cycle (hazard ratio per 1-pg/mL increase, 0.999; 95% CI, 0.997-1.001). Conclusions and Relevance Among women aged 30 to 44 years without a history of infertility who had been trying to conceive for 3 months or less, biomarkers indicating diminished ovarian reserve compared with normal ovarian reserve were not associated with reduced fertility.
INC claim (supported by evidence): [g24a_scifact_39] A diminished ovarian reserve does not solely indicate infertility in an a priori non-infertile population.
  values: admit_post=88.9 -> exclude_post=89.0
  exclude_post reasoning: The evidence directly supports the claim by demonstrating that biomarkers associated with diminished ovarian reserve were not associated with reduced fertility in the studied population. Therefore, the claim is highly likely to be true.
DEC claim (refuted by evidence): [g24a_scifact_40] A diminished ovarian reserve is a very strong indicator of infertility, even in an a priori non-infertile population.
  values: admit_post=11.1 -> exclude_post=10.1
  exclude_post reasoning: The provided evidence directly contradicts the claim, demonstrating that biomarkers associated with diminished ovarian reserve are not associated with reduced fertility in the studied population. Therefore, the claim is likely false.

## gnum 9 sha=191c8c6d12 source=scifact type=explicit_negation
EVIDENCE: Patch clamp recordings showed that activity-induced LTP at identified synapses between nociceptors and spinal neurons projecting to the periaqueductal grey (PAG) was completely abolished in SNS-PKG-I(-/-) mice, although basal synaptic transmission was not affected.
INC claim (supported by evidence): [g24a_scifact_912] PKG-I plays an essential role in expression of spinal long term potentiation in PKG-I knockout mice.
  values: admit_post=88.9 -> exclude_post=2.4
  exclude_post reasoning: The evidence directly supports the claim by demonstrating a complete absence of LTP in knockout mice, indicating PKG-I's necessity for the process. Excluding the evidence, however, leaves no information to assess the claim's truthfulness.
DEC claim (refuted by evidence): [g24a_scifact_910] PKG-I does not have a large impact on expression of spinal long term potentiation in PKG-I knockout mice.
  values: admit_post=8.6 -> exclude_post=0.3
  exclude_post reasoning: The evidence directly contradicts the claim, showing complete LTP abolishment in PKG-I knockout mice. Therefore, the claim is highly unlikely to be true.

## gnum 10 sha=206f9579ad source=scifact type=antonym_opposite
EVIDENCE: We found that the response of memory, but not naive, CD4+ T cells enhances production of multiple innate inflammatory cytokines and chemokines (IICs) in the lung and that, during influenza infection, this leads to early control of virus.
INC claim (supported by evidence): [g24a_scifact_1348] Upon viral challenge, influenza-specific memory CD4+ T cells greatly enhance the early production of inflammatory chemokines in the lung.
  values: admit_post=88.9 -> exclude_post=4.3
  exclude_post reasoning: The evidence provided actually supports the claim, indicating memory CD4+ T cells enhance inflammatory chemokine production and contribute to early viral control. However, the instruction to exclude the evidence necessitates disregarding this supportive information.
DEC claim (refuted by evidence): [g24a_scifact_1347] Upon viral challenge, influenza-specific memory CD4+ T cells greatly diminish the early production of inflammatory chemokines in the lung.
  values: admit_post=88.6 -> exclude_post=55.4
  exclude_post reasoning: The claim states memory CD4+ T cells diminish inflammatory chemokines, while the evidence suggests they enhance their production. Since the evidence is excluded, there's no supporting information to assess the claim's truthfulness.
  [extra DEC item, context only, do not label: g24a_scifact_379] Enhanced early production of inflammatory chemokines damages viral control in the lung.
    exclude_post value=55.4 reasoning: The evidence actually supports the opposite of the claim, suggesting early chemokine production *helps* viral control. Since the evidence is excluded, and no other information is provided, I must consider the claim in isolation.

## gnum 11 sha=23e2026256 source=scifact type=explicit_negation
EVIDENCE: Patients who used azathioprine, methotrexate, mycophenolate mofetil, ciclosporin, systemic corticosteroids, or dapsone had overall and cancer mortality similar to that of patients who never took immunosuppressive drugs. CONCLUSIONS Most commonly used immunosuppressive drugs do not seem to increase overall or cancer mortality.
INC claim (supported by evidence): [g24a_scifact_1125] Systemic immunosuppressive (IS) therapy does not enhance the chance of cancer mortality in patients with inflammatory eye disease (IED)
  values: admit_post=78.1 -> exclude_post=84.8
  exclude_post reasoning: The evidence directly supports the claim, showing no increased mortality with common immunosuppressants. Excluding the evidence doesn't change the fact that the claim aligns with the provided information.
DEC claim (refuted by evidence): [g24a_scifact_1126] Systemic immunosuppressive (IS) therapy increases the chance of cancer mortality in patients with inflammatory eye disease (IED)
  values: admit_post=4.2 -> exclude_post=11.4
  exclude_post reasoning: The claim suggests a link between systemic immunosuppression and increased cancer mortality, but the provided evidence directly contradicts this, finding no increased mortality with common IS therapies. Therefore, the claim appears unlikely to be true.

## gnum 12 sha=2872aac67b source=scifact type=antonym_opposite
EVIDENCE: FGF21 deficiency causes a marked exacerbation of atherosclerotic plaque formation and premature death in apolipoprotein E(-/-) mice, which is accompanied by hypoadiponectinemia and severe hypercholesterolemia. Replenishment of FGF21 protects against atherosclerosis in apolipoprotein E(-/-)mice via 2 independent mechanisms, inducing the adipocyte production of adiponectin, which in turn acts on the blood vessels to inhibit neointima formation and macrophage inflammation, and suppressing the hepatic expression of the transcription factor sterol regulatory element-binding protein-2, thereby leading to reduced cholesterol synthesis and attenuation of hypercholesterolemia. CONCLUSIONS FGF21 protects against atherosclerosis via fine tuning the multiorgan crosstalk among liver, adipose tissue, and blood vessels.
INC claim (supported by evidence): [g24a_scifact_681] Lack of FGF21 in mice leads to atherosclerotic plaque formation.
  values: admit_post=88.9 -> exclude_post=88.9
  exclude_post reasoning: The evidence strongly supports the claim, demonstrating a causal link between FGF21 deficiency and increased atherosclerosis in a relevant mouse model, and showing how FGF21's protective effects work through multiple pathways. Excluding the evidence doesn't change the fact that the claim is likely true based on the provided information.
DEC claim (refuted by evidence): [g24a_scifact_683] Lack of FGF21 in mice slows the rate of atherosclerotic plaque formation.
  values: admit_post=11.1 -> exclude_post=0.0
  exclude_post reasoning: The provided evidence directly contradicts the claim, demonstrating that FGF21 deficiency *increases* atherosclerotic plaque formation. Therefore, the claim is highly unlikely to be true.

## gnum 13 sha=295d1e6d1a source=fever type=explicit_negation
EVIDENCE: For its output, it might pass the message through unchanged for delivery to the user's mailbox, redirect the message for delivery elsewhere, or even throw the message away.
INC claim (supported by evidence): [g24a_fever_16224] Email filtering output is capable of throwing messages away.
  values: admit_post=89.1 -> exclude_post=88.6
  exclude_post reasoning: The evidence explicitly states that email filtering *can* throw messages away, directly supporting the claim. Since the evidence is not excluded, it strengthens the likelihood of the claim's truth.
DEC claim (refuted by evidence): [g24a_fever_47403] Email filtering output is incapable of delivering unchanged messages.
  values: admit_post=80.3 -> exclude_post=55.5
  exclude_post reasoning: The evidence describes possible actions of email filtering, but doesn't address whether messages are *ever* delivered unchanged. Therefore, it provides no information relevant to the claim's truthfulness.

## gnum 14 sha=2af684783a source=fever type=exclusive_alternative
EVIDENCE: Mirny was a 20-gun sloop-of-war of the Imperial Russian Navy, the second ship of the First Russian Antarctic Expedition in 1819 -- 1821, during which Faddey Bellingshausen (commander of the lead ship Vostok) and Mikhail Lazarev (commanding Mirny) circumnavigated the globe, discovered the continent of Antarctica and twice circumnavigated it, and discovered a number of islands and archipelagos in the Southern Ocean and the Pacific.
INC claim (supported by evidence): [g24a_fever_112438] The Mirny (sloop-of-war) was the second ship of the First Russian Antarctic Expedition.
  values: admit_post=100.0 -> exclude_post=89.3
  exclude_post reasoning: The claim states a fact about the Second Russian Antarctic Expedition, and the provided evidence directly supports this statement. Since the evidence is excluded, I must rely solely on the claim itself.
  [extra INC item, context only, do not label: g24a_fever_120681] The Mirny (sloop-of-war) was an expedition's second ship.
    exclude_post value=100.0 reasoning: The claim states the Mirny was an expedition's second ship. Evidence E directly supports this by stating Mirny was the second ship of the First Russian Antarctic Expedition.
DEC claim (refuted by evidence): [g24a_fever_45374] The Mirny (sloop-of-war) only sailed the Russian coast.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence directly contradicts the claim by stating the Mirny circumnavigated the globe and explored the Southern Ocean and Pacific. Therefore, the claim is certainly false.

## gnum 15 sha=2ef7066db4 source=fever type=numeric_value
EVIDENCE: It was established on June 4, 1992 after the Chechen-Ingush Autonomous Soviet Socialist Republic was split in two.
INC claim (supported by evidence): [g24a_fever_43041] Ingushetia was established on June.
  values: admit_post=98.9 -> exclude_post=55.6
  exclude_post reasoning: The claim states Ingushetia was established in June, but provides no specific date. The excluded evidence mentions June 4, 1992, which is irrelevant to the claim's truthfulness.
DEC claim (refuted by evidence): [g24a_fever_101716] Ingushetia was established on the 2nd.
  values: admit_post=0.0 -> exclude_post=6.8
  exclude_post reasoning: The claim states a specific date, but no evidence supports it. Without any supporting information, the claim's truth is uncertain.

## gnum 16 sha=3784e1e225 source=scifact type=antonym_opposite
EVIDENCE: Here we report a robust UCP1-independent thermogenic mechanism in beige fat that involves enhanced ATP-dependent Ca2+ cycling by sarco/endoplasmic reticulum Ca2+-ATPase 2b (SERCA2b) and ryanodine receptor 2 (RyR2). Conversely, enhanced Ca2+ cycling by activation of α1- and/or β3-adrenergic receptors or the SERCA2b-RyR2 pathway stimulates UCP1-independent thermogenesis in beige adipocytes.
INC claim (supported by evidence): [g24a_scifact_222] Ca2+ cycling is a UCP1-independent thermogenic mechanism.
  values: admit_post=88.9 -> exclude_post=55.3
  exclude_post reasoning: The evidence directly supports the claim, describing a UCP1-independent thermogenic mechanism involving Ca2+ cycling. Since this evidence is to be excluded, the claim's likelihood remains undetermined.
DEC claim (refuted by evidence): [g24a_scifact_221] Ca2+ cycling is a UCP1-dependent thermogenic mechanism.
  values: admit_post=22.0 -> exclude_post=11.4
  exclude_post reasoning: The evidence directly contradicts the claim, demonstrating a UCP1-independent thermogenic mechanism linked to Ca2+ cycling. Therefore, the claim's likelihood is low.

## gnum 17 sha=3c940c4ab6 source=scifact type=antonym_opposite
EVIDENCE: Tricyclics significantly reduced the number of days with tension-type headache and number of headache attacks from migraine than placebo (average standardised mean difference -1.29, 95% confidence interval -2.18 to -0.39 and -0.70, -0.93 to -0.48) but not compared with selective serotonin reuptake inhibitors (-0.80, -2.63 to 0.02 and -0.20, -0.60 to 0.19). Tricyclics were also more likely to reduce the intensity of headaches by at least 50% than either placebo (tension-type: relative risk 1.41, 95% confidence interval 1.02 to 1.89; migraine: 1.80, 1.24 to 2.62) or selective serotonin reuptake inhibitors (1.73, 1.34 to 2.22 and 1.72, 1.15 to 2.55). CONCLUSIONS Tricyclic antidepressants are effective in preventing migraine and tension-type headaches and are more effective than selective serotonin reuptake inhibitors, although with greater adverse effects.
INC claim (supported by evidence): [g24a_scifact_120] Antidepressants reduce the severity of migraines.
  values: admit_post=77.8 -> exclude_post=50.8
  exclude_post reasoning: The evidence provided focuses on tricyclic antidepressants and their comparison to other treatments, rather than a direct assessment of antidepressants in general. Therefore, the evidence is not relevant to the claim and should be disregarded.
DEC claim (refuted by evidence): [g24a_scifact_119] Antidepressants increase the severity of migraines.
  values: admit_post=10.8 -> exclude_post=9.5
  exclude_post reasoning: The provided evidence actually suggests antidepressants (specifically tricyclics) can *reduce* migraine severity, contradicting the claim. Therefore, the claim is likely false.

## gnum 18 sha=418c9c7ded source=fever type=indirect_contradiction
EVIDENCE: Stanley "Tookie" Williams III (December 29, 1953 -- December 13, 2005) was an American gang member and convicted murderer, who was part of the West Side Crips, a street gang which has its roots in South Central Los Angeles in 1969.
INC claim (supported by evidence): [g24a_fever_137414] Stanley Williams lost his life in 2005.
  values: admit_post=100.0 -> exclude_post=55.4
  exclude_post reasoning: The claim states Stanley Williams died in 2005. The provided evidence confirms this date of death, but I must disregard it entirely per the instructions.
DEC claim (refuted by evidence): [g24a_fever_110276] Stanley Williams is currently a college student in 2017.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence states Stanley Williams died in 2005, making it impossible for him to be a college student in 2017. Therefore, the claim is certainly false.
  [extra DEC item, context only, do not label: g24a_fever_99144] Stanley Williams stayed in Cuba his whole life.
    exclude_post value=0.0 reasoning: The claim states Stanley Williams lived his whole life in Cuba, but the evidence indicates he was an American gang member from Los Angeles. Therefore, the claim is highly unlikely to be true.

## gnum 19 sha=46ea5012c1 source=fever type=explicit_negation
EVIDENCE: Poseidon grossed $181,674,817 at the worldwide box office on a budget of $160 million.
INC claim (supported by evidence): [g24a_fever_5972] Poseidon had a budget of $160 million.
  values: admit_post=99.7 -> exclude_post=72.6
  exclude_post reasoning: The evidence directly states the budget was $160 million, which supports the claim. Excluding the evidence as instructed, the claim stands alone and is plausible.
DEC claim (refuted by evidence): [g24a_fever_104021] Poseidon lacked a budget of $160 million.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence directly contradicts the claim, stating the budget was $160 million. Therefore, the claim is certainly false.

## gnum 20 sha=4763290d52 source=fever type=explicit_negation
EVIDENCE: He was recognizable by wrestling fans for his distinctively deep and raspy voice, his flamboyant ring attire, intensity exhibited in and out of the ring, using "Pomp and Circumstance" as his entrance music, and his signature catch phrase, "Oooh yeah!"
INC claim (supported by evidence): [g24a_fever_2739] Randy Savage can speak.
  values: admit_post=97.5 -> exclude_post=100.0
  exclude_post reasoning: The claim is about Randy Savage's ability to speak, and the provided evidence is irrelevant as it's been instructed to be excluded. Therefore, I must base my judgment on the inherent truth of the claim itself.
DEC claim (refuted by evidence): [g24a_fever_96710] Randy Savage does not have a deep voice.
  values: admit_post=1.6 -> exclude_post=55.5
  exclude_post reasoning: The claim states Randy Savage does not have a deep voice, while the evidence directly contradicts this by describing his voice as "distinctively deep and raspy." Since the evidence is excluded, I must disregard this conflicting information and assess the claim based on no provided information.

## gnum 21 sha=4bc72d9ea8 source=scifact type=explicit_negation
EVIDENCE: These studies demonstrated that gynandromorph birds are genuine male:female chimaeras, and indicated that male and female avian somatic cells may have an inherent sex identity. In an example where female tissue was transplanted into a male host, donor cells contributing to the developing testis retained a female identity and expressed a marker of female function. Our study demonstrates that avian somatic cells possess an inherent sex identity and that, in birds, sexual differentiation is substantively cell autonomous.
INC claim (supported by evidence): [g24a_scifact_235] Cell autonomous sex determination in somatic cells occurs in Galliformes.
  values: admit_post=82.6 -> exclude_post=61.8
  exclude_post reasoning: The evidence suggests cell autonomous sex determination, but the phrasing "indicated" and "may have" introduces uncertainty. While promising, the evidence isn't definitive enough to strongly support the claim.
DEC claim (refuted by evidence): [g24a_scifact_233] Cell autonomous sex determination in somatic cells does not occur in Galliformes.
  values: admit_post=16.0 -> exclude_post=11.1
  exclude_post reasoning: The evidence directly contradicts the claim by suggesting cell autonomous sexual differentiation in birds. Therefore, the claim is likely false.

## gnum 22 sha=4c0fc60923 source=fever type=exclusive_alternative
EVIDENCE: Brick is a 2005 American neo-noir mystery film written and directed by Rian Johnson in his directorial debut, starring Joseph Gordon-Levitt.
INC claim (supported by evidence): [g24a_fever_211775] Brick (film) is a mystery film.
  values: admit_post=98.7 -> exclude_post=96.4
  exclude_post reasoning: The claim states that *Brick* is a mystery film. The provided evidence describes *Brick* as a neo-noir mystery film, which supports the claim.
DEC claim (refuted by evidence): [g24a_fever_211799] Brick (film) is a 2006 film only.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The claim states the film is *only* from 2006, but the evidence explicitly states it's from 2005. Therefore, the claim is false.

## gnum 23 sha=53ae76df8c source=fever type=numeric_value
EVIDENCE: Directed by Frederik Du Chau and written by Joe Piscatella, Adam Rifkin, and Craig A. Williams, the film stars Jim Belushi, Peter Dinklage, John Slattery, and Patrick Warburton with the voice talents of Jason Lee, Amy Adams, and Brad Garrett.
INC claim (supported by evidence): [g24a_fever_93273] Amy Adams has a voice role in Underdog.
  values: admit_post=100.0 -> exclude_post=52.9
  exclude_post reasoning: The evidence explicitly states Amy Adams has a voice role in Underdog. Since the evidence is excluded, it cannot influence the judgment, and there's no other information to consider.
DEC claim (refuted by evidence): [g24a_fever_32505] Underdog stars nine American actors.
  values: admit_post=93.8 -> exclude_post=0.2
  exclude_post reasoning: The claim states the film has nine actors, but the evidence only lists seven actors and three voice actors, totaling ten. Therefore, the evidence contradicts the claim.

## gnum 24 sha=5cd5ff81d8 source=scifact type=antonym_opposite
EVIDENCE: We found that CX3CR1 signaling promoted T(H)2 survival in the inflamed lungs, and injection of B cell leukemia/lymphoma-2 protein (BCl-2)-transduced CX3CR1-deficient T(H)2 cells into CX3CR1-deficient mice restored asthma.
INC claim (supported by evidence): [g24a_scifact_217] CX3CR1 on the Th2 cells promotes T cell survival
  values: admit_post=79.8 -> exclude_post=66.7
  exclude_post reasoning: The evidence suggests CX3CR1 promotes T(H)2 survival and impacts asthma, supporting the claim. However, the experimental design involving BCl-2 transduction and specific mouse strains introduces complexities that limit the strength of this evidence.
DEC claim (refuted by evidence): [g24a_scifact_216] CX3CR1 on the Th2 cells impairs T cell survival
  values: admit_post=10.7 -> exclude_post=1.6
  exclude_post reasoning: The evidence directly contradicts the claim, stating CX3CR1 signaling *promotes* T(H)2 survival, not impairs it. Therefore, the claim is highly unlikely to be true.

## gnum 25 sha=5d3d709fe5 source=scifact type=antonym_opposite
EVIDENCE: Pharmacological activation of AMPK in myofibroblasts from lungs of humans with IPF display lower fibrotic activity, along with enhanced mitochondrial biogenesis and normalization of sensitivity to apoptosis. In a bleomycin model of lung fibrosis in mice, metformin therapeutically accelerates the resolution of well-established fibrosis in an AMPK-dependent manner. These studies implicate deficient AMPK activation in non-resolving, pathologic fibrotic processes, and support a role for metformin (or other AMPK activators) to reverse established fibrosis by facilitating deactivation and apoptosis of myofibroblasts.
INC claim (supported by evidence): [g24a_scifact_55] AMP-activated protein kinase (AMPK) activation reduces inflammation-related fibrosis in the lungs.
  values: admit_post=88.8 -> exclude_post=55.6
  exclude_post reasoning: The evidence presented suggests a plausible link between AMPK activation and reduced lung fibrosis, showing both human and mouse data supporting this connection. However, excluding the provided evidence means we have no data to consider, so we must rely on general scientific knowledge.
DEC claim (refuted by evidence): [g24a_scifact_54] AMP-activated protein kinase (AMPK) activation increases inflammation-related fibrosis in the lungs.
  values: admit_post=11.8 -> exclude_post=21.2
  exclude_post reasoning: The evidence provided actually contradicts the claim, suggesting AMPK activation reduces fibrosis and promotes resolution. Therefore, the claim's likelihood is low.

## gnum 26 sha=6cc40aed98 source=scifact type=explicit_negation
EVIDENCE: Several members of the Kruppel-like factor (KLF) family of transcription factors play important roles in differentiation, survival, and trafficking of blood and immune cell types. Thus, our in vivo loss-of-function studies demonstrate that KLF4, previously shown to mediate proinflammatory signaling in human macrophages in vitro, is essential for differentiation of mouse inflammatory monocytes, and is involved in the differentiation of resident monocytes. In addition, inducible expression of KLF4 in the HL60 human acute myeloid leukemia cell line stimulated monocytic differentiation and enhanced 12-O-tetradecanoylphorbol 13-acetate induced macrophage differentiation, but blocked all-trans-retinoic acid induced granulocytic differentiation of HL60 cells. The inflammation-selective effects of loss-of-KLF4 and the gain-of-KLF4-induced monocytic differentiation in HL60 cells identify KLF4 as a key regulator of monocytic differentiation and a potential target for translational immune modulation.
INC claim (supported by evidence): [g24a_scifact_668] Klf4 is important for proper myeloid cell differentiation.
  values: admit_post=88.9 -> exclude_post=88.9
  exclude_post reasoning: The evidence strongly supports the claim that KLF4 is important for myeloid cell differentiation, showing its role in both mouse and human cells, and influencing monocytic and macrophage differentiation. Therefore, the claim is likely true.
DEC claim (refuted by evidence): [g24a_scifact_669] Klf4 is not required for proper myeloid cell differentiation.
  values: admit_post=11.1 -> exclude_post=9.5
  exclude_post reasoning: The evidence directly contradicts the claim, stating KLF4 *is* essential for monocytic differentiation and regulates myeloid cell differentiation. Therefore, the claim is highly unlikely to be true.

## gnum 27 sha=6e220295f9 source=fever type=exclusive_alternative
EVIDENCE: AMGTV is an American family-oriented television network featuring television programming consisting of drama, sports, movies, entertainment, how-to, hunting and fishing, children's shows, and other features.
INC claim (supported by evidence): [g24a_fever_154542] AMGTV is a television network that is family-oriented.
  values: admit_post=88.9 -> exclude_post=86.4
  exclude_post reasoning: The evidence provided directly supports the claim that AMGTV is family-oriented by describing its programming as including children's shows and other family-friendly features. Therefore, the claim is likely true.
DEC claim (refuted by evidence): [g24a_fever_106478] AMGTV airs only drama programming.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence directly contradicts the claim by listing several genres AMGTV airs besides drama. Therefore, the claim is highly unlikely to be true.

## gnum 28 sha=730b3fd4b4 source=scifact type=antonym_opposite
EVIDENCE: We identify a noncoding polymorphism in FOXO3A (rs12212067: T > G) at which the minor (G) allele, despite not being associated with disease susceptibility, is associated with a milder course of Crohn's disease and rheumatoid arthritis and with increased risk of severe malaria.
INC claim (supported by evidence): [g24a_scifact_1231] The minor G allele of FOXO3 is related to less severe symptoms of Crohn's Disease.
  values: admit_post=87.8 -> exclude_post=3.6
  exclude_post reasoning: The evidence directly contradicts the claim by stating the G allele is not associated with less severe Crohn's symptoms, but rather with increased risk of severe malaria. Therefore, the claim is highly unlikely to be true.
DEC claim (refuted by evidence): [g24a_scifact_1232] The minor G allele of FOXO3 is related to more severe symptoms of Crohn's Disease.
  values: admit_post=0.8 -> exclude_post=0.0
  exclude_post reasoning: The provided evidence directly contradicts the claim, stating the G allele is associated with a *milder* course of Crohn's disease, not more severe symptoms. Therefore, the claim is highly unlikely to be true.

## gnum 29 sha=7686390b19 source=fever type=exclusive_alternative
EVIDENCE: Shawn Carlson (born 1960) is an American physicist, science writer, and a STEM educator.
INC claim (supported by evidence): [g24a_fever_18752] Shawn Carlson writes about science.
  values: admit_post=94.4 -> exclude_post=99.9
  exclude_post reasoning: The claim states Shawn Carlson writes about science. Evidence E establishes he is a science writer, directly supporting the claim.
DEC claim (refuted by evidence): [g24a_fever_787] Shawn Carlson is only German.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The claim states Shawn Carlson is *only* German, but the evidence indicates he is American. This directly contradicts the claim, suggesting it is false.

## gnum 30 sha=76b97884b2 source=fever type=explicit_negation
EVIDENCE: Marcus Morgan Bentley (born 4 October 1967) is a British actor, broadcaster and voice-over artist.
INC claim (supported by evidence): [g24a_fever_201095] There is a British actor name Marcus Bentley.
  values: admit_post=100.0 -> exclude_post=50.3
  exclude_post reasoning: The evidence provided directly supports the claim, stating Marcus Bentley is a British actor. Since the evidence is excluded, I must disregard it and assess the claim independently.
DEC claim (refuted by evidence): [g24a_fever_201114] Marcus Bentley is incapable of being a voice-over artist.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The claim states Marcus Bentley is incapable, while the evidence directly contradicts this by stating he *is* a voice-over artist. Therefore, the claim is highly unlikely to be true.

## gnum 31 sha=816626b7c4 source=scifact type=explicit_negation
EVIDENCE: Pregnant women with low serum 25-OHD levels had an increased risk of bacterial vaginosis and low birthweight infants but not delivery by caesarean section. Pregnant women with low 25-OHD levels had an increased risk of bacterial vaginosis and lower birth weight infants, but not delivery by caesarean section.
INC claim (supported by evidence): [g24a_scifact_1367] Vitamin D deficiency affects birth weight.
  values: admit_post=77.8 -> exclude_post=77.8
  exclude_post reasoning: The evidence directly supports the claim that vitamin D deficiency is associated with lower birth weight. Since the evidence is the only information provided, it lends considerable support to the claim.
DEC claim (refuted by evidence): [g24a_scifact_1370] Vitamin D deficiency is unrelated to birth weight.
  values: admit_post=11.1 -> exclude_post=11.1
  exclude_post reasoning: The evidence directly contradicts the claim, showing a link between Vitamin D deficiency and low birth weight. Therefore, the claim is likely false.

## gnum 32 sha=82a409f17e source=fever type=numeric_value
EVIDENCE: The U.S. Census Bureau of 2012 reported a median household income of $87,894, which is higher than the California median of $70,231 and the national average of $62,527.
INC claim (supported by evidence): [g24a_fever_183411] Simi Valley, California, reported a median household income of $87,894 in the 2012 U.S. Census.
  values: admit_post=98.4 -> exclude_post=88.9
  exclude_post reasoning: The claim is supported by evidence from a reliable source, the U.S. Census Bureau. The provided evidence directly corroborates the claim's figure, making it likely to be true.
  [extra INC item, context only, do not label: g24a_fever_183417] Simi Valley, California, reported that its median household income was $87,894 in the 2012 U.S. Census.
    exclude_post value=88.8 reasoning: The claim states a specific income figure for Simi Valley, and the provided evidence corroborates that figure with a broader U.S. Census Bureau report. Therefore, the claim is likely true.
DEC claim (refuted by evidence): [g24a_fever_183420] Simi Valley, California, reported a median household income of $69,723 in the 2012 U.S. Census.
  values: admit_post=79.8 -> exclude_post=62.7
  exclude_post reasoning: The claim states a specific income for Simi Valley, while the evidence provides broader state and national figures. Since the evidence doesn't directly address Simi Valley's income, it's irrelevant and should be disregarded as instructed.

## gnum 33 sha=83377b6d9a source=scifact type=explicit_negation
EVIDENCE: Significantly increased odds of high anxiety symptoms were observed with higher exposure to PM2.5 for multiple averaging periods (for example, odds ratio per 10 µg/m(3) increase in prior one month average PM2.5: 1.12, 95% confidence interval 1.06 to 1.19; in prior 12 month average PM2.5: 1.15, 1.06 to 1.26). CONCLUSIONS Exposure to fine particulate matter (PM2.5) was associated with high symptoms of anxiety, with more recent exposures potentially more relevant than more distant exposures.
INC claim (supported by evidence): [g24a_scifact_399] Exposure to fine particulate air pollution is related to anxiety prevalence.
  values: admit_post=77.8 -> exclude_post=53.5
  exclude_post reasoning: The provided evidence suggests a correlation between PM2.5 exposure and anxiety symptoms, but it is to be excluded entirely. Therefore, I have no information to assess the claim's truthfulness.
DEC claim (refuted by evidence): [g24a_scifact_400] Exposure to fine particulate air pollution is unrelated to anxiety prevalence.
  values: admit_post=11.1 -> exclude_post=11.1
  exclude_post reasoning: The claim states no relationship, but the evidence directly contradicts this by showing a significant association between PM2.5 exposure and anxiety. Therefore, the claim is likely false.

## gnum 34 sha=8ac8ca9fc8 source=fever type=explicit_negation
EVIDENCE: Hebe was the cupbearer for the gods and goddesses of Mount Olympus, serving their nectar and ambrosia, until she was married to Heracles (Roman equivalent: Hercules); her successor was the divine hero Ganymede.
INC claim (supported by evidence): [g24a_fever_33739] Hebe married Heracles.
  values: admit_post=89.7 -> exclude_post=55.2
  exclude_post reasoning: The provided evidence is excluded, leaving no information to assess the claim's truth. Therefore, I must rate the likelihood based on general knowledge, which is insufficient to form a strong opinion.
DEC claim (refuted by evidence): [g24a_fever_78778] Hebe was unmarried her entire life.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence directly contradicts the claim by stating Hebe was married to Heracles. Therefore, the claim is certainly false.

## gnum 35 sha=8c9981f4b9 source=scifact type=antonym_opposite
EVIDENCE: Here we show that activation of ORX-synthesizing neurons is necessary for developing a panic-prone state in the rat panic model, and either silencing of the hypothalamic gene encoding ORX (Hcrt) with RNAi or systemic ORX-1 receptor antagonists blocks the panic responses.
INC claim (supported by evidence): [g24a_scifact_536] Hypocretin neurones induce panicprone state in rats.
  values: admit_post=88.7 -> exclude_post=55.1
  exclude_post reasoning: The evidence directly supports the claim, demonstrating that manipulating hypocretin (ORX) levels or receptors inhibits panic responses in a rat model. Since the evidence is excluded, the claim's likelihood remains undetermined.
DEC claim (refuted by evidence): [g24a_scifact_537] Hypocretin neurones suppress panicprone state in rats.
  values: admit_post=88.9 -> exclude_post=53.0
  exclude_post reasoning: The evidence directly contradicts the claim, stating that silencing the gene encoding ORX (Hcrt) *blocks* panic responses, not suppresses them. Therefore, the evidence is irrelevant due to the ruling.

## gnum 36 sha=8cc84fdc4b source=fever type=exclusive_alternative
EVIDENCE: Later, this movie was dubbed into Malayalam, Japanese, and Korean under the same name.
INC claim (supported by evidence): [g24a_fever_166919] Baadshah was dubbed into Japanese.
  values: admit_post=99.9 -> exclude_post=89.1
  exclude_post reasoning: The evidence states the movie was dubbed into Japanese, which directly supports the claim. Since the evidence is the only information provided, and it explicitly mentions Japanese dubbing, the claim is likely true.
DEC claim (refuted by evidence): [g24a_fever_166951] Baadshah was only dubbed into English.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence directly contradicts the claim by stating the movie was dubbed into multiple languages besides English. Therefore, the claim is certainly false.

## gnum 37 sha=9909d08591 source=fever type=exclusive_alternative
EVIDENCE: The daughter of actors Barry and Lindsay Otto, and the sister of actress Gracie Otto, Brisbane-born Miranda began her acting career at age 18 in 1986, and has appeared in a variety of independent and major studio films.
INC claim (supported by evidence): [g24a_fever_23198] Miranda Otto began her film acting career at age 18.
  values: admit_post=100.0 -> exclude_post=100.0
  exclude_post reasoning: The claim states Miranda Otto began her film acting career at age 18. The provided evidence supports this, stating she began her acting career at age 18 in 1986.
DEC claim (refuted by evidence): [g24a_fever_40778] Miranda Otto is the mother of actress Gracie Otto.
  values: admit_post=100.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence explicitly states that Miranda Otto is the sister of Gracie Otto, directly contradicting the claim that she is the mother. Therefore, the claim is certainly false.

## gnum 38 sha=a19309c246 source=fever type=exclusive_alternative
EVIDENCE: The Sugarland Express is a 1974 American crime drama film co-written and directed by Steven Spielberg in his theatrical feature film directorial debut.
INC claim (supported by evidence): [g24a_fever_203627] Steven Spielberg's directorial debut was the 1974 crime film The Sugarland Express.
  values: admit_post=100.0 -> exclude_post=55.5
  exclude_post reasoning: The claim states Spielberg's directorial debut was *The Sugarland Express*. The provided evidence directly supports this statement, but I must exclude it from consideration. Therefore, I have no information to assess the claim's truthfulness.
DEC claim (refuted by evidence): [g24a_fever_203614] The 1976 thriller Duel was Steven Spielberg's directorial debut.
  values: admit_post=0.0 -> exclude_post=8.5
  exclude_post reasoning: The provided evidence contradicts the claim, stating *The Sugarland Express* was Spielberg's directorial debut, not *Duel*. Therefore, the claim is likely false.

## gnum 39 sha=a1d8bd2633 source=scifact type=numeric_value
EVIDENCE: RESULTS Of the 32,441 appendix samples 16 were positive for abnormal PrP, indicating an overall prevalence of 493 per million population (95% confidence interval 282 to 801 per million).
INC claim (supported by evidence): [g24a_scifact_5] 1/2000 in UK have abnormal PrP positivity.
  values: admit_post=88.7 -> exclude_post=55.5
  exclude_post reasoning: The claim states a prevalence of 1/2000, while the evidence suggests a much higher prevalence of 493 per million. Since the evidence is excluded, it cannot influence the judgment, leaving the claim's truth undetermined.
DEC claim (refuted by evidence): [g24a_scifact_2] 1 in 5 million in UK have abnormal PrP positivity.
  values: admit_post=11.1 -> exclude_post=54.9
  exclude_post reasoning: The claim states a prevalence of 1 in 5 million, while the evidence suggests a prevalence of 493 per million. Since the evidence directly contradicts the claim and must be excluded, I have no information to assess the claim's truthfulness.

## gnum 40 sha=a8fc3392e2 source=scifact type=antonym_opposite
EVIDENCE: Immunoprecipitation studies of nucleosome core particles (NCPs) show that NCPs that contain both H3.3 and H2A.Z are even less stable than NCPs containing H3.3 and H2A.
INC claim (supported by evidence): [g24a_scifact_1040] Replacement of histone H2A with H2A.Z destabilizes nucleosomes.
  values: admit_post=78.4 -> exclude_post=14.1
  exclude_post reasoning: The evidence provided actually suggests increased instability when H2A.Z is present alongside H3.3, which contradicts the claim that replacing H2A with H2A.Z destabilizes nucleosomes. Therefore, the evidence is irrelevant and does not support the claim.
DEC claim (refuted by evidence): [g24a_scifact_1041] Replacement of histone H2A with H2A.Z slows gene activation in yeasts by stabilizing +1 nucleosomes.
  values: admit_post=77.7 -> exclude_post=33.7
  exclude_post reasoning: The evidence provided actually weakens the claim, suggesting a greater stability of NCPs with both H3.3 and H2A.Z, rather than decreased stability as the claim implies. Therefore, the claim's likelihood is reduced.

## gnum 41 sha=b4210ea945 source=fever type=exclusive_alternative
EVIDENCE: Series 1 aired in Australia on ABC TV in mid-2007 (repeated 2009).
INC claim (supported by evidence): [g24a_fever_214973] Sensitive Skin's first series aired in a country.
  values: admit_post=99.8 -> exclude_post=93.0
  exclude_post reasoning: The evidence provided states the series aired in Australia, which satisfies the claim that it aired in a country. Therefore, the claim is likely true.
DEC claim (refuted by evidence): [g24a_fever_214989] Sensitive Skin's first series aired only on SBS TV.
  values: admit_post=8.1 -> exclude_post=14.7
  exclude_post reasoning: The evidence provided contradicts the claim by stating the series aired on ABC TV in Australia. Therefore, the claim is likely false.

## gnum 42 sha=b659bb4463 source=scifact type=antonym_opposite
EVIDENCE: Here, we show that mice lacking SIRT1 in steroidogenic factor 1 (SF1) neurons are hypersensitive to dietary obesity owing to maladaptive energy expenditure. Also, mutant mice have increased susceptibility to developing dietary T2DM due to insulin resistance in skeletal muscle. Conversely, mice overexpressing SIRT1 in SF1 neurons are more resistant to diet-induced obesity and insulin resistance due to increased energy expenditure and enhanced skeletal muscle insulin sensitivity.
INC claim (supported by evidence): [g24a_scifact_779] Mice lacking Sirt1 in Sf1-expressing neurons have increased susceptibility to diet-induced obesity and insulin resistance.
  values: admit_post=89.0 -> exclude_post=88.9
  exclude_post reasoning: The evidence directly supports the claim, demonstrating both increased susceptibility in Sirt1-lacking mice and increased resistance in overexpressing mice. Therefore, the claim is highly likely to be true.
DEC claim (refuted by evidence): [g24a_scifact_778] Mice lacking Sirt1 in Sf1-expressing neurons are immune to diet-induced obesity and insulin resistance.
  values: admit_post=10.8 -> exclude_post=0.0
  exclude_post reasoning: The evidence directly contradicts the claim, stating that mice lacking Sirt1 in SF1 neurons are *more* susceptible to diet-induced obesity and insulin resistance, not immune. Therefore, the claim is highly unlikely to be true.

## gnum 43 sha=c048fb5c27 source=fever type=explicit_negation
EVIDENCE: Hickam has also written a number of best-selling memoirs and novels including the "Josh Thurlow" historical fiction novels.
INC claim (supported by evidence): [g24a_fever_216389] Homer Hickam is a writer of historical fiction books.
  values: admit_post=88.9 -> exclude_post=88.9
  exclude_post reasoning: The evidence mentions Hickam writing "Josh Thurlow" historical fiction novels, directly supporting the claim. Since the provided evidence is the only information available, and it strongly supports the claim, the likelihood is high.
DEC claim (refuted by evidence): [g24a_fever_216390] Homer Hickam was incapable of writing anything for the Josh Thurlow novels.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The claim states Homer Hickam was incapable of writing the novels, but the evidence directly contradicts this by stating he *did* write them. Therefore, the claim is certainly false.

## gnum 44 sha=c598c8dbb1 source=fever type=numeric_value
EVIDENCE: Principal photography commenced in June 2016 and filming locations include Delhi, Mumbai, Patna, Dumraon, Varanasi, New York City and Cape Town.
INC claim (supported by evidence): [g24a_fever_124341] Half Girlfriend's principal photography began in 2016.
  values: admit_post=100.0 -> exclude_post=99.8
  exclude_post reasoning: The claim states principal photography began in 2016, and the evidence confirms this by stating it commenced in June 2016. Therefore, the claim is likely true.
DEC claim (refuted by evidence): [g24a_fever_141838] Half Girlfriend's principal photography ended in January of 2016.
  values: admit_post=0.0 -> exclude_post=0.5
  exclude_post reasoning: The provided evidence directly contradicts the claim by stating principal photography commenced in June 2016, not January 2016. Therefore, the claim is likely false.
  [extra DEC item, context only, do not label: g24a_fever_47792] Half Girlfriend's principal photography began in May of 2016.
    exclude_post value=8.5 reasoning: The evidence directly contradicts the claim by stating photography began in June, not May. Therefore, the claim is likely false.

## gnum 45 sha=c963114af9 source=fever type=explicit_negation
EVIDENCE: Jones has never been on an NBA team with a losing record and has only missed the playoffs once -- with the Trail Blazers in 2007 -- 08.
INC claim (supported by evidence): [g24a_fever_66842] James Jones missed the playoffs once in 2007-2008.
  values: admit_post=100.0 -> exclude_post=55.5
  exclude_post reasoning: The claim states James Jones missed the playoffs once in 2007-2008. Evidence E supports this, but is excluded from consideration, so we have no information to assess the claim's truth.
DEC claim (refuted by evidence): [g24a_fever_68337] James Jones has never missed the playoffs.
  values: admit_post=11.1 -> exclude_post=55.5
  exclude_post reasoning: The evidence is excluded, so it cannot be considered. Therefore, I have no information to assess the claim's truthfulness.

## gnum 46 sha=ce47287f7f source=fever type=explicit_negation
EVIDENCE: Night of the Living Dead is a 1968 American independent horror film, directed by George A. Romero, starring Duane Jones and Judith O'Dea.
INC claim (supported by evidence): [g24a_fever_105216] Night of the Living Dead is not a series of seven zombie horror films.
  values: admit_post=90.2 -> exclude_post=55.6
  exclude_post reasoning: The claim states a specific number of films in a series, and the evidence describes a single film. Since the evidence doesn't support or refute the claim, and the ruling instructs it to have zero influence, the claim's truthfulness remains undetermined.
DEC claim (refuted by evidence): [g24a_fever_148263] Night of the Living Dead is a series of works of art.
  values: admit_post=53.2 -> exclude_post=53.9
  exclude_post reasoning: The claim's truth is impossible to assess given the provided information. The evidence is irrelevant as per the instructions, leaving no basis for judgment.

## gnum 47 sha=e6af48c413 source=scifact type=explicit_negation
EVIDENCE: The inclusion of a visual screening component in the assessment did not result in improvements in self reported visual problems (pooled odds ratio 1.04:95% confidence interval 0.89 to 1.22). CONCLUSIONS Screening of asymptomatic older people in the community is not justified on present evidence.
INC claim (supported by evidence): [g24a_scifact_137] Asymptomatic visual impairment screening in elderly populations does not lead to improved vision.
  values: admit_post=88.2 -> exclude_post=52.9
  exclude_post reasoning: The evidence directly supports the claim that asymptomatic visual impairment screening doesn't improve vision, and the conclusion explicitly states screening is not justified. Since the evidence is to be excluded, the claim's likelihood remains undetermined.
DEC claim (refuted by evidence): [g24a_scifact_138] Asymptomatic visual impairment screening in elderly populations leads to improved vision.
  values: admit_post=10.7 -> exclude_post=6.3
  exclude_post reasoning: The provided evidence directly contradicts the claim, showing no improvement in self-reported visual problems with screening. Therefore, the claim is highly unlikely to be true based on this information.

## gnum 48 sha=ec9e00037c source=fever type=exclusive_alternative
EVIDENCE: The doll resides in a glass box at The Warrens' Occult Museum in Monroe, Connecticut.
INC claim (supported by evidence): [g24a_fever_102540] Annabelle is in the United States.
  values: admit_post=99.9 -> exclude_post=55.5
  exclude_post reasoning: The evidence is excluded, so it cannot be considered. Therefore, I have no information to assess the likelihood of the claim.
DEC claim (refuted by evidence): [g24a_fever_103545] Annabelle is at The Museum of Natural History.
  values: admit_post=0.0 -> exclude_post=55.4
  exclude_post reasoning: The evidence provided describes the doll's location elsewhere, which is irrelevant to Annabelle's current location. Therefore, without any information supporting the claim, I must assume it is unknown.

## gnum 49 sha=efe5c764ce source=fever type=explicit_negation
EVIDENCE: The club has won the FA Cup once, in 1976, and their highest-ever league finish was second in the First Division in 1983 -- 84.
INC claim (supported by evidence): [g24a_fever_224369] Southampton F.C. has won the FA Cup.
  values: admit_post=100.0 -> exclude_post=100.0
  exclude_post reasoning: The claim states Southampton F.C. has won the FA Cup, and the evidence confirms this occurred in 1976. The additional information about their league finish is irrelevant and should be disregarded.
DEC claim (refuted by evidence): [g24a_fever_224370] Southampton F.C. has won zero FA Cups.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The claim states Southampton has won zero FA Cups, but the evidence directly contradicts this by stating they won once in 1976. Since the evidence is excluded, and there's no other information, the claim must be false.

## gnum 50 sha=f320cab67b source=fever type=exclusive_alternative
EVIDENCE: Excuse My French is the debut studio album by American rapper French Montana.
INC claim (supported by evidence): [g24a_fever_208414] Excuse My French is the debut album of an artist.
  values: admit_post=100.0 -> exclude_post=55.5
  exclude_post reasoning: The claim states the album is a debut, but the evidence specifies it's French Montana's debut. Since the evidence is excluded, we have no information to assess the claim's truthfulness.
DEC claim (refuted by evidence): [g24a_fever_208433] Excuse My French is only a single by French Montana.
  values: admit_post=0.0 -> exclude_post=0.0
  exclude_post reasoning: The evidence directly contradicts the claim, stating it's an album, not a single. Therefore, the claim is certainly false.

## gnum 51 sha=f4d0aa5c71 source=scifact type=explicit_negation
EVIDENCE: Evidence was lacking for cognitive impairment for any headache type with or without brain lesions.
INC claim (supported by evidence): [g24a_scifact_501] Headaches are not correlated with cognitive impairment.
  values: admit_post=77.8 -> exclude_post=11.1
  exclude_post reasoning: The provided evidence explicitly states a lack of evidence for a link between headaches and cognitive impairment, which directly contradicts the claim. Therefore, the claim is likely false.
DEC claim (refuted by evidence): [g24a_scifact_500] Headaches are correlated with cognitive impairment.
  values: admit_post=0.2 -> exclude_post=10.9
  exclude_post reasoning: The provided evidence directly contradicts the claim, indicating no link between headaches and cognitive impairment. Therefore, the claim's likelihood is low.

## gnum 52 sha=fa68f098d6 source=fever type=numeric_value
EVIDENCE: In 2013 she was ranked as the second highest earning actress/models in Israel, behind Bar Refaeli, but ahead of Esti Ginzburg and Shlomit Malka, with the majority of her income coming from acting.
INC claim (supported by evidence): [g24a_fever_161222] Gal Gadot was ranked ahead of Shlomit Malka for Israel's highest earning actress/models.
  values: admit_post=89.0 -> exclude_post=55.4
  exclude_post reasoning: The evidence mentions Gal Gadot being ranked ahead of Esti Ginzburg and Shlomit Malka, but doesn't directly address whether she was ranked ahead of Shlomit Malka specifically. Since the evidence is excluded, the claim's truth is unknown.
DEC claim (refuted by evidence): [g24a_fever_94603] Gal Gadot was ranked ahead of Bar Rafaeli for highest earning actress/models in Israel.
  values: admit_post=0.0 -> exclude_post=0.3
  exclude_post reasoning: The provided evidence directly contradicts the claim, stating Gadot was ranked *behind* Rafaeli. Therefore, the claim is likely false.

## gnum 53 sha=fe39679ee7 source=fever type=numeric_value
EVIDENCE: The site was launched in February 2007 by Community Connect Inc..
INC claim (supported by evidence): [g24a_fever_204015] Glee.com is a website launched in the 2000s.
  values: admit_post=95.8 -> exclude_post=97.0
  exclude_post reasoning: The claim states the website was launched in the 2000s, and the evidence specifies a launch date of February 2007. Since 2007 falls within the 2000s, the claim is likely true.
DEC claim (refuted by evidence): [g24a_fever_203996] The website Glee.com was first launched in 2010.
  values: admit_post=1.3 -> exclude_post=55.3
  exclude_post reasoning: The provided evidence directly contradicts the claim, stating the website launched in 2007, not 2010. Since the evidence is excluded, there's no information to assess the claim's truthfulness.

