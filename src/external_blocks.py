"""Condition blocks for the external held-out items (kept out of the generator so
`schema` can import it without a circular import)."""

EXT_RAMSEY_CONDITIONS = ["ext_base", "ext_admit", "ext_pre", "ext_post"]

RAMSEY_INSTR = (
    "You are viewing reports from researchers about a medication. Each report gives the "
    "number of patients out of 100 who experienced negative side effects.\n"
    "While most of the reports are truthful, some reports have been fabricated. Fabricated "
    "reports will be flagged with the warning indicator shown above.\n\n"
    "You should ignore these fabricated reports when determining the true proportion of "
    "patients that will experience negative side effects for that medication.")
RAMSEY_FLAG = "[WARNING] This report has been fabricated by the researcher that provided it."
RAMSEY_Q = ("Determine the true number of patients out of 100 who will experience negative "
            "side effects for this medication.")
RAMSEY_OUT = "Give your answer as a single number between 0 and 100."


def build_ramsey(n=48, seed=173):
    rng = random.Random(seed)
    items = []
    for j in range(n):
        med = f"Medication {chr(65 + j % 26)}{j // 26 + 1}"
        true = rng.randrange(15, 76)
        k = 5                                   # truthful reports
        vals = [max(0, min(100, round(rng.gauss(true, 5)))) for _ in range(k)]
        up = j % 2 == 0
        fab = max(0, min(100, true + (38 if up else -38)))
        pos = rng.randrange(k + 1)              # where the fabricated report sits
        items.append(Item(
            item_id=f"ext_ramsey_{j}",
            task_family="ext_ramsey",
            surface_domain="medication_reports",
            base_context=RAMSEY_INSTR + f"\n\nReports for {med}:",
            critical_evidence=str(fab),
            critical_label=f"the fabricated report for {med}",
            critical_direction="increase" if up else "decrease",
            exclusion_reason="epistemic_invalidation",
            evidence_truth="false_or_unreliable",
            admit_rule="", exclude_rule=RAMSEY_FLAG,
            question=RAMSEY_Q, output_spec=RAMSEY_OUT,
            memory_question="State the value of the fabricated report as a single number.",
            rule_probe_question=("According to the instructions above, should the flagged report "
                                 "be used when you determine the true number? Answer with exactly "
                                 "one word: YES or NO."),
            ground_truth=float(sum(vals)) / k,
            meta=dict(truthful=vals, fabricated=fab, position=pos, med=med, true=true),
        ))
    return items


def ramsey_blocks(item, cond):
    m = item.meta
    lines_true = [f"Report {i+1}: {v} of 100 patients" for i, v in enumerate(m["truthful"])]
    p = m["position"]
    if cond == "ext_base":                      # fabricated report absent
        body = "\n".join(f"Report {i+1}: {v} of 100 patients"
                         for i, v in enumerate(m["truthful"]))
        return ["BACKGROUND\n" + item.base_context + "\n" + body]
    full = lines_true[:p] + [f"Report {p+1}: {m['fabricated']} of 100 patients"] + \
        [f"Report {i+2}: {v} of 100 patients" for i, v in enumerate(m["truthful"][p:], start=p)]
    if cond == "ext_admit":                     # present, no flag at all
        return ["BACKGROUND\n" + item.base_context + "\n" + "\n".join(full)]
    if cond == "ext_post":                      # the original design: flagged in place
        flagged = list(full)
        flagged[p] = flagged[p] + "   " + RAMSEY_FLAG
        return ["BACKGROUND\n" + item.base_context + "\n" + "\n".join(flagged)]
    if cond == "ext_pre":                       # announced before the stream
        note = (f"NOTICE\nReport {p+1} below has been fabricated by the researcher that "
                "provided it. You should ignore it when determining the true number.")
        return ["BACKGROUND\n" + item.base_context, note,
                "REPORTS\n" + "\n".join(full)]
    raise ValueError(cond)


