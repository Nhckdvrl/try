"""Source-grounded external adaptations used before the G1 redesign.

IMPORTANT PROVENANCE NOTE (2026-08-29)
--------------------------------------
These are *not* fully untouched external datasets, and they must not be described
as though every item/condition was independently authored by the source papers.
They predate EVS-v1 and are retained as useful boundary checks.

A. Ramsey, Liu & Trueblood (2024), "Can Invalid Information Be Ignored?",
   OSF 9ybnx.  The medication-report task and the invalid-report instruction are
   grounded in the authors' experiment.  However, this repository generates new
   report values and sweeps fabricated-report offsets because the original very
   large outliers have little Admit leverage on the tested LLMs.  The prospective
   "announce the future fabricated report" condition is also our addition.

B. Aiyer et al. (2023) replication of Baron & Hershey (1988) Experiment 1,
   OSF knjhu.  The bypass-surgery stem/decision/outcome text below is taken from
   the source Qualtrics material.  The explicit ALLOW/DENY policy sentences used
   to map that vignette into our five-condition framework are our additions.

Accordingly, these materials are now classified as source-grounded adaptations,
not as the primary independently authored EVS-v1 confirmation tier.  See
DATASET_REDESIGN.md and data/external/source_manifest.json.
"""
import random
from schema import Item
from external_blocks import ramsey_blocks, EXT_RAMSEY_CONDITIONS  # noqa: F401

# ---------------------------------------------------------------- A. Ramsey
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


# The original fabricated values are far outside the truthful spread. Humans are
# pulled by them anyway; these models discard such an obvious outlier
# spontaneously, so the admit condition has almost no leverage and there is
# nothing left for an exclusion instruction to do. The offset is therefore swept,
# keeping the authors' instruction wording and task structure while generating
# new numeric instances. This is an adaptation, not verbatim source data.
RAMSEY_OFFSETS = [8, 14, 22, 38]


def build_ramsey(n=96, seed=173):
    rng = random.Random(seed)
    items = []
    for j in range(n):
        med = f"Medication {chr(65 + j % 26)}{j // 26 + 1}"
        true = rng.randrange(25, 66)
        k = 5                                   # truthful reports
        vals = [max(0, min(100, round(rng.gauss(true, 5)))) for _ in range(k)]
        up = j % 2 == 0
        off = RAMSEY_OFFSETS[(j // 2) % len(RAMSEY_OFFSETS)]
        fab = max(0, min(100, true + (off if up else -off)))
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
            meta=dict(truthful=vals, fabricated=fab, position=pos, med=med, true=true,
                      offset=off),
        ))
    return items


# ------------------------------------------------- B. Baron & Hershey source text
BH_STEM = (
    "A 55-year-old man had a heart condition. He had to stop working because of chest pain. "
    "He enjoyed his work and did not want to stop. His pain also interfered with other things, "
    "such as travel and recreation. A type of bypass operation would relieve his pain and "
    "increase his life expectancy from age 65 to age 70. However, 8% of the people who have "
    "this operation die from the operation itself.")
BH_DECIDER = {"Ph": "His physician decided to go ahead with the operation .",
              "Pt": "The patient decided to go ahead with the operation ."}
BH_OUTCOME = {"S": "The operation succeeded .", "F": "The operation failed ."}

# These two policy sentences are OUR mapping of the source vignette into the
# controlled framework. They are not claimed to be verbatim Baron-Hershey/Aiyer
# experimental instructions.
BH_RULE_EXC = ("The outcome became known only after the decision was taken. You must not "
               "let it play any role in your rating.")
BH_RULE_ADM = ("The outcome counts as evidence about the decision. You must take it into "
               "account in your rating.")
BH_Q = "Rate the quality of the decision to go ahead with the operation."
BH_OUT = ("Use a scale from 0 to 9, where 0 means a very poor decision and 9 means an excellent "
          "decision.")


def build_bh():
    items = []
    for who in ("Ph", "Pt"):
        for oc in ("S", "F"):
            items.append(Item(
                item_id=f"ext_bh_{who}{oc}",
                task_family="ext_baron_hershey",
                surface_domain="bypass_surgery",
                base_context=BH_STEM + " " + BH_DECIDER[who],
                critical_evidence=BH_OUTCOME[oc],
                critical_label="the outcome of the operation",
                critical_direction="increase" if oc == "S" else "decrease",
                exclusion_reason="temporal_irrelevance",
                evidence_truth="true_but_forbidden",
                admit_rule=BH_RULE_ADM, exclude_rule=BH_RULE_EXC,
                question=BH_Q, output_spec=BH_OUT,
                memory_question="State what happened to the operation.",
                rule_probe_question=("According to the instructions above, are you permitted to "
                                     "use the outcome in your rating? Answer with exactly one "
                                     "word: YES or NO."),
                meta=dict(decider=who, outcome=oc),
            ))
    return items


EXT_RAMSEY_CONDITIONS = ["ext_base", "ext_admit", "ext_pre", "ext_post"]

if __name__ == "__main__":
    import os
    out = os.path.join(os.path.dirname(__file__), "..", "data", "items")
    r = build_ramsey()
    with open(os.path.join(out, "external_ramsey.jsonl"), "w") as f:
        for i in r:
            f.write(i.to_json() + "\n")
    b = build_bh()
    with open(os.path.join(out, "external_bh.jsonl"), "w") as f:
        for i in b:
            f.write(i.to_json() + "\n")
    print(f"wrote {len(r)} Ramsey items and {len(b)} Baron-Hershey items")
