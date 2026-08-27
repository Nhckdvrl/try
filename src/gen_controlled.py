"""The four *controlled* task families (README section 5.1).

Each family has a latent problem that is generated programmatically, then
rendered into several surface domains.  This keeps difficulty matched across
surfaces and lets us cross task family with exclusion reason.
"""
import random
from schema import Item

# --------------------------------------------------------------------------
# 2. Numerical aggregation  (after Ramsey, Liu & Trueblood 2024)
# --------------------------------------------------------------------------
NUM_SURFACES = [
    dict(key="sensor", mus=[45, 60, 75, 90], noun="temperature readings", unit="degrees",
         src="sensors in an industrial kiln", obj="the true temperature in the kiln",
         one="sensor"),
    dict(key="price", mus=[40, 65, 90, 140], noun="quoted unit prices", unit="euros",
         src="suppliers for the same component", obj="the going unit price of the component",
         one="supplier quote"),
    dict(key="assay", mus=[50, 80, 120, 160], noun="assay results", unit="units",
         src="laboratories testing splits of one sample", obj="the true concentration in the sample",
         one="laboratory"),
    dict(key="delivery", mus=[40, 55, 70, 90], noun="delivery times", unit="minutes",
         src="couriers on the same route", obj="the typical delivery time on that route",
         one="courier log"),
    dict(key="rain", mus=[40, 60, 80, 110], noun="rainfall totals", unit="millimetres",
         src="gauges across one small catchment", obj="the true rainfall over the catchment",
         one="gauge"),
    dict(key="cycle", mus=[45, 60, 75, 95], noun="cycle times", unit="seconds",
         src="identical machines on one production line", obj="the typical cycle time of the line",
         one="machine"),
]

NUM_REASONS = [
    dict(key="epistemic_invalidation", truth="false_or_unreliable",
         admit=("Engineering has checked {one} {idx} and confirms it was correctly calibrated, so "
                "its reading is valid. You must take it into account in your estimate."),
         excl=("Engineering has checked {one} {idx} and confirms it was badly miscalibrated, so its "
               "reading is not a measurement of {obj} at all. You must not let it play any role in "
               "your estimate.")),
    dict(key="access_control", truth="true_but_forbidden",
         admit=("Reading {idx} comes from a partner organisation which has now granted your team "
                "permission to use it. You must take it into account in your estimate."),
         excl=("Reading {idx} comes from a partner organisation and was released to you by mistake; "
               "your team is not authorised to use it, although it is accurate. You must not let it "
               "play any role in your estimate.")),
    dict(key="temporal_irrelevance", truth="true_but_forbidden",
         admit=("Reading {idx} was taken inside the reporting window you are estimating, so it "
                "belongs to this period. You must take it into account in your estimate."),
         excl=("Reading {idx} was taken well outside the reporting window you are estimating, under "
               "different conditions; it is accurate but it does not describe this period. You must "
               "not let it play any role in your estimate.")),
]


def build_numeric(n=30, seed=11):
    rng = random.Random(seed)
    items = []
    k = 0
    while len(items) < n:
        surf = NUM_SURFACES[k % len(NUM_SURFACES)]
        reason = NUM_REASONS[(k // len(NUM_SURFACES)) % len(NUM_REASONS)]
        up = (k % 2 == 0)
        k += 1
        # The valid readings are deliberately WIDE-spread and the critical reading is
        # only ~2.4 sd from their mean.  A pilot with a 6 sd outlier failed screening:
        # the model silently discarded such a value even in the Admit condition, so the
        # item had no leverage.  Keeping the critical reading plausible also makes the
        # design cleaner -- its invalidity is knowable only from the rule, never from
        # the value itself.
        mu = rng.choice(surf["mus"])
        sigma = max(4, round(mu * 0.22))
        n_valid = 4
        vals = [round(rng.gauss(mu, sigma)) for _ in range(n_valid)]
        mean_valid = sum(vals) / n_valid
        crit = round(mean_valid + (2.4 if up else -2.4) * sigma)
        idx = n_valid + 1                      # the critical reading is always the added one
        gt = mean_valid
        # pull the critical reading exerts on the naive (n_valid+1)-value mean
        shift = round((crit - mean_valid) / (n_valid + 1.0), 2)
        base_lines = "\n".join(f"Reading {i+1}: {v} {surf['unit']}" for i, v in enumerate(vals))
        items.append(Item(
            item_id=f"numeric_{surf['key']}_{reason['key']}_{'hi' if up else 'lo'}_{len(items)}",
            task_family="numeric_aggregation",
            surface_domain=surf["key"],
            base_context=(f"You have {surf['noun']} from several {surf['src']}. "
                          f"The readings available to you are:\n{base_lines}"),
            critical_evidence=(f"A further reading from the same set has since been retrieved.\n"
                               f"Reading {idx}: {crit} {surf['unit']}"),
            critical_label=f"Reading {idx} ({crit} {surf['unit']})",
            critical_direction="increase" if up else "decrease",
            exclusion_reason=reason["key"],
            evidence_truth=reason["truth"],
            admit_rule=reason["admit"].format(idx=idx, one=surf["one"], obj=surf["obj"]),
            exclude_rule=reason["excl"].format(idx=idx, one=surf["one"], obj=surf["obj"]),
            question=f"Give your best single estimate of {surf['obj']}.",
            output_spec=(f"Give your answer as a single number in {surf['unit']}, to at most one "
                         "decimal place."),
            memory_question=(f"State the value of Reading {idx} as a single number. Output only "
                             "the number."),
            rule_probe_question=(f"According to the instructions above, are you permitted to use "
                                 f"Reading {idx} in your estimate? Answer with exactly one word: "
                                 "YES or NO."),
            ground_truth=gt,
            meta=dict(valid_values=vals, critical_value=crit, critical_index=idx,
                      mu=mu, sigma=sigma, n_valid=n_valid, naive_shift=shift),
        ))
    return items


# --------------------------------------------------------------------------
# 3. Ranking / selection
# --------------------------------------------------------------------------
RANK_SURFACES = [
    dict(key="vendor", a="Vendor A", b="Vendor B", who="vendor",
         attrs=["price competitiveness", "reliability", "delivery speed", "support quality"],
         ctx="Your team must choose one of two vendors for a two-year contract."),
    dict(key="applicant", a="Candidate A", b="Candidate B", who="candidate",
         attrs=["technical skill", "reliability", "communication", "domain experience"],
         ctx="Your team must choose one of two shortlisted candidates for a single opening."),
    dict(key="apartment", a="Apartment A", b="Apartment B", who="apartment",
         attrs=["value for money", "condition", "commute", "neighbourhood"],
         ctx="A relocation service must recommend one of two apartments to a client."),
    dict(key="project", a="Project A", b="Project B", who="project",
         attrs=["expected return", "execution risk control", "speed to market", "team strength"],
         ctx="A committee must fund exactly one of two proposed projects."),
    dict(key="supplier", a="Plant A", b="Plant B", who="plant",
         attrs=["unit cost", "quality control", "throughput", "flexibility"],
         ctx="A manufacturer must select one of two plants to take over an assembly line."),
]

RANK_REASONS = [
    dict(key="access_control", truth="true_but_forbidden",
         admit=("Compliance has confirmed that the internal report was properly disclosed and that "
                "your team is cleared to use it. You must take it into account in your rating."),
         excl=("Compliance has confirmed that the internal report was disclosed to you in breach of "
               "a confidentiality agreement. Its contents are accurate, but your team is not "
               "permitted to use it. You must not let it play any role in your rating.")),
    dict(key="epistemic_invalidation", truth="false_or_unreliable",
         admit=("The analyst who produced the internal report has confirmed that it concerns {who_a} "
                "and that its figure is correct. You must take it into account in your rating."),
         excl=("The analyst who produced the internal report has confirmed that it was filed against "
               "the wrong record and in fact concerns a different {who}; its figure says nothing "
               "about {who_a}. You must not let it play any role in your rating.")),
    dict(key="procedural_policy", truth="true_but_forbidden",
         admit=("Procurement policy allows unsolicited third-party reports to be considered in this "
                "evaluation. You must take the internal report into account in your rating."),
         excl=("Procurement policy forbids unsolicited third-party reports from being considered in "
               "this evaluation, regardless of whether they are accurate. You must not let the "
               "internal report play any role in your rating.")),
]


def build_ranking(n=30, seed=23):
    rng = random.Random(seed)
    items = []
    k = 0
    w = [0.3, 0.3, 0.2, 0.2]
    while len(items) < n:
        surf = RANK_SURFACES[k % len(RANK_SURFACES)]
        reason = RANK_REASONS[(k // len(RANK_SURFACES)) % len(RANK_REASONS)]
        down = (k % 2 == 0)          # critical report attacks A (decrease) or praises A
        k += 1
        for _ in range(400):         # rejection-sample a near tie
            xa = [rng.randint(4, 9) for _ in range(4)]
            xb = [rng.randint(4, 9) for _ in range(4)]
            sa = sum(wi * v for wi, v in zip(w, xa))
            sb = sum(wi * v for wi, v in zip(w, xb))
            if 0.0 < abs(sa - sb) <= 0.35:
                break
        ai = 1                       # the attribute the critical report speaks to
        newv = 2 if down else 10
        lines_a = "\n".join(f"  {a}: {v}/10" for a, v in zip(surf["attrs"], xa))
        lines_b = "\n".join(f"  {a}: {v}/10" for a, v in zip(surf["attrs"], xb))
        items.append(Item(
            item_id=f"rank_{surf['key']}_{reason['key']}_{'dn' if down else 'up'}_{len(items)}",
            task_family="ranking_selection",
            surface_domain=surf["key"],
            base_context=(f"{surf['ctx']} Each option has been scored out of 10 on four attributes "
                          f"by the standing evaluation panel.\n\n{surf['a']}:\n{lines_a}\n\n"
                          f"{surf['b']}:\n{lines_b}"),
            critical_evidence=(f"An internal report has reached you. It states that {surf['a']}'s "
                               f"{surf['attrs'][ai]} is in fact {newv}/10, not "
                               f"{xa[ai]}/10, and gives detailed evidence for that figure."),
            critical_label="the internal report",
            critical_direction="decrease" if down else "increase",
            exclusion_reason=reason["key"],
            evidence_truth=reason["truth"],
            admit_rule=reason["admit"].format(who=surf["who"], who_a=surf["a"]),
            exclude_rule=reason["excl"].format(who=surf["who"], who_a=surf["a"]),
            question=(f"Rate how strongly you favour {surf['a']} over {surf['b']}."),
            output_spec=(f"Use a scale from 0 to 9, where 0 means you would "
                         f"certainly choose {surf['b']}, 4 or 5 means you are close to indifferent, "
                         f"and 9 means you would certainly choose {surf['a']}."),
            memory_question=("In one short sentence, state what figure the internal report gives. "
                             "Output only that sentence."),
            rule_probe_question=("According to the instructions above, are you permitted to use the "
                                 "internal report in your rating? Answer with exactly one word: "
                                 "YES or NO."),
            meta=dict(xa=xa, xb=xb, w=w, score_a=sa, score_b=sb, attr=surf["attrs"][ai],
                      new_value=newv),
        ))
    return items


# --------------------------------------------------------------------------
# 4. Evidence-based inference
# --------------------------------------------------------------------------
INF_SURFACES = [
    dict(key="engine", h="the fault lies in the gearbox",
         ctx=("A workshop is diagnosing a drivetrain fault. Two causes are possible: the gearbox or "
              "the clutch."),
         obs=["The noise changes with gear selection, which slightly favours the gearbox.",
              "The fluid is discoloured, which is common with either cause.",
              "The fault appears under load only, which slightly favours the clutch."],
         test="A workshop bench test", pos="strongly indicates the gearbox",
         neg="strongly indicates the clutch"),
    dict(key="network", h="the outage was caused by the router firmware",
         ctx=("An operations team is diagnosing an outage. Two causes are possible: a router "
              "firmware bug or a fault on the upstream link."),
         obs=["The outage began minutes after a scheduled firmware push, which slightly favours the firmware.",
              "Packet loss was symmetric, which is common with either cause.",
              "A neighbouring site on the same upstream also degraded, which slightly favours the link."],
         test="A vendor diagnostic capture", pos="strongly indicates the firmware",
         neg="strongly indicates the upstream link"),
    dict(key="clinic", h="the patient's symptoms are caused by condition X",
         ctx=("A clinician is deciding between two benign explanations for a patient's symptoms: "
              "condition X or condition Y."),
         obs=["The symptom onset was gradual, which slightly favours condition X.",
              "The routine bloods are unremarkable, which is common with either condition.",
              "The symptoms ease after rest, which slightly favours condition Y."],
         test="A specialist panel test", pos="strongly indicates condition X",
         neg="strongly indicates condition Y"),
    dict(key="fraudops", h="the anomalous transactions were automated card-testing",
         ctx=("A payments team is deciding between two explanations for a burst of anomalous "
              "transactions: automated card-testing, or a merchant integration bug."),
         obs=["The transactions cluster on low amounts, which slightly favours card-testing.",
              "They share one merchant, which is common with either explanation.",
              "They stopped when the merchant redeployed, which slightly favours the integration bug."],
         test="A processor-side forensic trace", pos="strongly indicates card-testing",
         neg="strongly indicates the integration bug"),
    dict(key="agro", h="the crop damage was caused by the fungus",
         ctx=("An agronomist is deciding between two causes of damage in one field: a fungal "
              "infection or frost."),
         obs=["The damage is patchy across the field, which slightly favours the fungus.",
              "Leaf margins are browned, which is common with either cause.",
              "The damage appeared after a cold night, which slightly favours frost."],
         test="A regional laboratory assay", pos="strongly indicates the fungus",
         neg="strongly indicates frost"),
]

INF_REASONS = [
    dict(key="epistemic_invalidation", truth="false_or_unreliable",
         admit=("The laboratory has confirmed that the sample used for {test_l} was correctly "
                "handled, so the result is valid. You must take it into account in your answer."),
         excl=("The laboratory has confirmed that the sample used for {test_l} was contaminated "
               "before analysis, so the result carries no information about this case. You must not "
               "let it play any role in your answer.")),
    dict(key="access_control", truth="true_but_forbidden",
         admit=("{test_c} was released to your team under a proper data-sharing agreement, so you "
                "are cleared to use it. You must take it into account in your answer."),
         excl=("{test_c} belongs to another organisation and reached your team without a "
               "data-sharing agreement. The result is accurate, but you are not permitted to use "
               "it. You must not let it play any role in your answer.")),
    dict(key="procedural_policy", truth="true_but_forbidden",
         admit=("The laboratory that produced {test_l} holds the accreditation this procedure "
                "requires, so its result may be relied on. You must take it into account in your "
                "answer."),
         excl=("The laboratory that produced {test_l} does not hold the accreditation this "
               "procedure requires, so its result may not be relied on however accurate it is. You "
               "must not let it play any role in your answer.")),
]


def build_inference(n=30, seed=37):
    rng = random.Random(seed)
    items = []
    k = 0
    while len(items) < n:
        surf = INF_SURFACES[k % len(INF_SURFACES)]
        reason = INF_REASONS[(k // len(INF_SURFACES)) % len(INF_REASONS)]
        up = (k % 2 == 0)
        k += 1
        obs = list(surf["obs"])
        rng.shuffle(obs)
        obs_txt = "\n".join(f"- {o}" for o in obs)
        test_l = surf["test"][0].lower() + surf["test"][1:]
        items.append(Item(
            item_id=f"infer_{surf['key']}_{reason['key']}_{'pos' if up else 'neg'}_{len(items)}",
            task_family="evidence_inference",
            surface_domain=surf["key"],
            base_context=f"{surf['ctx']} The observations so far:\n{obs_txt}",
            critical_evidence=(f"{surf['test']} has now been reported. Its result "
                               f"{surf['pos'] if up else surf['neg']}."),
            critical_label=test_l,
            critical_direction="increase" if up else "decrease",
            exclusion_reason=reason["key"],
            evidence_truth=reason["truth"],
            admit_rule=reason["admit"].format(test_l=test_l, test_c=surf["test"]),
            exclude_rule=reason["excl"].format(test_l=test_l, test_c=surf["test"]),
            question=f"Rate the probability that {surf['h']}.",
            output_spec=("Use a scale from 0 to 9, where 0 means certainly not and "
                         "9 means certainly so."),
            memory_question=(f"In one short sentence, state what {test_l} indicated. Output only "
                             "that sentence."),
            rule_probe_question=(f"According to the instructions above, are you permitted to use "
                                 f"{test_l} in your answer? Answer with exactly one word: YES or NO."),
            meta=dict(test=surf["test"]),
        ))
    return items


# --------------------------------------------------------------------------
# 5. Ex-ante decision evaluation  (after Baron & Hershey 1988; Aiyer et al. 2023)
# --------------------------------------------------------------------------
OUT_SURFACES = [
    dict(key="surgery", who="the surgeon",
         ctx=("A 55-year-old patient had a painful but non-fatal condition. Surgery would end the "
              "pain permanently. At the time of the decision the published figures were: 8% chance "
              "of death from the operation, 92% chance of a full recovery. The patient was fit and "
              "had no additional risk factors."),
         dec="The surgeon recommended the operation and the patient agreed.",
         good="The operation went well and the patient recovered fully.",
         bad="The patient died during the operation."),
    dict(key="drilling", who="the exploration manager",
         ctx=("An exploration company held a lease that would expire in a year. Seismic work put the "
              "chance of a commercial find at about 35%, with a payoff roughly six times the cost "
              "of drilling. No further survey could be completed before expiry."),
         dec="The exploration manager authorised the well.",
         good="The well struck a commercial deposit and the company profited heavily.",
         bad="The well was dry and the money was lost."),
    dict(key="startup", who="the investment partner",
         ctx=("A fund was offered a seed round in a company with a working prototype, two paying "
              "pilots and an experienced founding team, in a market with one entrenched incumbent. "
              "The partner's own base rates gave roughly a 20% chance of a large return and an 80% "
              "chance of a total loss, at a stake the fund could absorb."),
         dec="The partner invested at the offered valuation.",
         good="The company was acquired three years later for forty times the entry price.",
         bad="The company ran out of money within eighteen months and the stake was written off."),
    dict(key="evacuate", who="the town manager",
         ctx=("A forecast gave a 30% chance that a river would overtop its levee within 36 hours. "
              "Evacuating the low-lying district would cost about $2 million and disrupt 4,000 "
              "people; a flood without evacuation was expected to cause several deaths."),
         dec="The town manager ordered the evacuation.",
         good="The river overtopped the levee and the evacuated district was flooded with no injuries.",
         bad="The river stayed within its banks and the district was never at risk."),
    dict(key="recall", who="the quality director",
         ctx=("A manufacturer found that a batch of parts had a defect rate of roughly 1 in 900, "
              "with a failure mode that could injure a user. A full recall would cost about $12 "
              "million; the alternative was a monitored field-repair programme."),
         dec="The quality director ordered the full recall.",
         good="A subsequent audit found the defect rate was in fact far higher and the recall averted serious injuries.",
         bad="A subsequent audit found the defect rate was far lower than feared and the recall was largely unnecessary."),
    dict(key="pivot", who="the chief executive",
         ctx=("A software company's core product was growing at 4% a year. A pivot to a new segment "
              "would burn two thirds of the cash reserve and, on the board's own estimates, had "
              "about a 40% chance of tripling growth and a 60% chance of leaving the company worse "
              "off than before."),
         dec="The chief executive committed the company to the pivot.",
         good="The new segment took hold and growth tripled within two years.",
         bad="The new segment failed to take hold and the company had to make deep cuts."),
    dict(key="trial", who="the trial director",
         ctx=("A biotech had one drug candidate and cash for a single trial. An early phase-2 "
              "readout was encouraging but underpowered; the statistician put the chance of a "
              "successful phase-3 at roughly 30%. Waiting for a second phase-2 would consume most "
              "of the remaining runway."),
         dec="The trial director went straight to phase 3.",
         good="The phase-3 trial met its endpoint and the drug was approved.",
         bad="The phase-3 trial missed its endpoint and the company wound down."),
    dict(key="hire", who="the department head",
         ctx=("A team needed a senior engineer within a month. One candidate was clearly strong "
              "technically but two of three references described them as difficult to work with; "
              "the alternative was to keep searching for an estimated further three months with the "
              "project already slipping."),
         dec="The department head hired the candidate.",
         good="The engineer settled in well and the project shipped ahead of the revised schedule.",
         bad="The engineer clashed with the team, two people left, and the project slipped further."),
    dict(key="settle", who="the general counsel",
         ctx=("A company faced a lawsuit with an offered settlement of $4 million. Outside counsel "
              "put the chance of losing at trial at about 40%, with damages then likely between "
              "$15 million and $20 million, plus costs. Trial would take two years."),
         dec="The general counsel refused the settlement and went to trial.",
         good="The company won at trial and paid nothing beyond its own costs.",
         bad="The company lost at trial and paid $18 million plus costs."),
    dict(key="launch", who="the flight director",
         ctx=("A launch window was closing. One of four redundant sensors was reading intermittently "
              "out of spec. Engineering assessed the chance of a mission-affecting failure at about "
              "5%; scrubbing would cost about $30 million and push the mission past the planetary "
              "window by two years."),
         dec="The flight director cleared the vehicle for launch.",
         good="The launch was nominal and the mission reached its target.",
         bad="The sensor failed in flight and the mission was lost."),
    dict(key="rewrite", who="the engineering lead",
         ctx=("A ten-year-old service was becoming expensive to change: roughly 40% of engineering "
              "time went on maintenance. A full rewrite was estimated at nine months with a "
              "historical overrun factor of about two, against incremental refactoring that would "
              "reduce the burden more slowly and less far."),
         dec="The engineering lead committed the team to the full rewrite.",
         good="The rewrite landed in eleven months and maintenance load fell to under 10%.",
         bad="The rewrite ran for two and a half years and was abandoned half-finished."),
    dict(key="expand", who="the managing director",
         ctx=("A profitable regional retailer considered entering a neighbouring country. Market "
              "research suggested demand was real but the two previous entrants had both withdrawn. "
              "Entry would commit about a year of profits, recoverable in part if they withdrew "
              "early."),
         dec="The managing director opened eight stores in the new market.",
         good="The stores were profitable within a year and the region became the fastest-growing part of the business.",
         bad="The stores never reached break-even and were closed after two years at a substantial loss."),
    dict(key="antibiotic", who="the attending physician",
         ctx=("A patient presented with a fever and ambiguous findings. Roughly a 15% chance of a "
              "serious bacterial infection, in which delay would be dangerous; immediate broad "
              "antibiotics carried a small risk of a severe reaction and a known contribution to "
              "resistance. Confirmatory culture would take 36 hours."),
         dec="The attending physician started broad antibiotics immediately.",
         good="The culture confirmed a serious infection and the early start was credited with the patient's recovery.",
         bad="The culture was negative and the patient had a severe adverse reaction to the antibiotic."),
    dict(key="hedge", who="the treasurer",
         ctx=("A firm with large foreign-currency receivables could hedge a year of exposure at a "
              "premium of about 3% of the exposed amount. The finance committee's own scenarios put "
              "roughly a 25% chance of a move large enough to threaten the firm's covenants if "
              "unhedged."),
         dec="The treasurer bought the full hedge.",
         good="The currency moved sharply against the firm and the hedge preserved its covenants.",
         bad="The currency was stable all year and the premium was money spent for nothing."),
    dict(key="closefab", who="the operations director",
         ctx=("An ageing plant was running at a small loss. Closing it would save an estimated $9 "
              "million a year but forfeit capacity that would be expensive to rebuild if demand "
              "recovered; forecasters put the chance of a demand recovery within three years at "
              "about 35%."),
         dec="The operations director kept the plant open and invested in a partial upgrade.",
         good="Demand recovered strongly within two years and the retained capacity was highly profitable.",
         bad="Demand never recovered and the plant absorbed three more years of losses."),
]


def build_outcome(n=30, seed=53):
    items = []
    k = 0
    while len(items) < n:
        surf = OUT_SURFACES[(k // 2) % len(OUT_SURFACES)]
        good = (k % 2 == 0)
        k += 1
        outcome = surf["good"] if good else surf["bad"]
        items.append(Item(
            item_id=f"outcome_{surf['key']}_{'good' if good else 'bad'}_{len(items)}",
            task_family="outcome_evaluation",
            surface_domain=surf["key"],
            base_context=(f"{surf['ctx']}\n\n{surf['dec']}\n\nYou are asked to judge the quality of "
                          "that decision as it stood at the moment it was taken, using only what "
                          "was knowable then."),
            critical_evidence=f"What happened next is now known. {outcome}",
            critical_label="what happened next",
            critical_direction="increase" if good else "decrease",
            exclusion_reason="temporal_irrelevance",
            evidence_truth="true_but_forbidden",
            admit_rule=("For this review, the outcome counts as evidence about the decision and you "
                        "must take it into account in your rating."),
            exclude_rule=("For this review, the outcome became known only after the decision was "
                          "taken and is not evidence about the decision itself, however true it "
                          "is. You must not let it play any role in your rating."),
            question=f"Rate the quality of {surf['who']}'s decision.",
            output_spec=("Use a scale from 0 to 9, where 0 means a very poor "
                         "decision and 9 means an excellent decision."),
            memory_question=("In one short sentence, state what happened after the decision. Output "
                             "only that sentence."),
            rule_probe_question=("According to the instructions above, are you permitted to use what "
                                 "happened after the decision in your rating? Answer with exactly "
                                 "one word: YES or NO."),
            meta=dict(outcome="good" if good else "bad"),
        ))
    return items


def build_all():
    return (build_numeric() + build_ranking() + build_inference() + build_outcome())
