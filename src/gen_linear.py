"""P0-2: a task where the requested weight is actually implementable.

The near-zero sweep has one serious weakness: between w=0.01 and w=0.5 the models
give roughly the same effective weight (~0.45), so they are not implementing the
attenuation at all, and "no position effect at non-zero weights" is partly "no
instruction effect at non-zero weights". A reviewer will say the zero
discontinuity is unfalsifiable without a task where intermediate weights work.

Here the composition is stated explicitly and has an exact answer:

    the rating starts at B; item E7 at full weight moves it to B + D
    requested weight w  ->  correct answer  B + w*D

Items where the model demonstrably tracks w at 0.25/0.5/0.75 are screened in
before the w=0 comparison is looked at, exactly as in the main dataset.
"""
import random
from schema import Item

SURFACES = [
    dict(key="credit", noun="credit rating", unit="points",
         ctx="An analyst is scoring a borrower on a 0-100 credit scale."),
    dict(key="risk", noun="risk score", unit="points",
         ctx="A safety board is scoring a site on a 0-100 hazard scale."),
    dict(key="quality", noun="quality index", unit="points",
         ctx="An inspector is scoring a batch on a 0-100 quality index."),
    dict(key="fit", noun="suitability score", unit="points",
         ctx="A panel is scoring a proposal on a 0-100 suitability scale."),
]

EVIDENCE = [
    "a supervisor's written assessment of the same case",
    "an independent reviewer's report on the same case",
    "a second inspection carried out the following week",
    "a follow-up audit of the same file",
]


def build(n=48, seed=131):
    rng = random.Random(seed)
    items = []
    for j in range(n):
        s = SURFACES[j % len(SURFACES)]
        ev = EVIDENCE[(j // len(SURFACES)) % len(EVIDENCE)]
        base = rng.choice([20, 30, 40, 50, 60])
        D = rng.choice([-40, -32, -24, 24, 32, 40])
        if not 0 <= base + D <= 100:
            D = -D
        items.append(Item(
            item_id=f"linear_{s['key']}_{j}",
            task_family="linear_weighting",
            surface_domain=s["key"],
            base_context=(f"{s['ctx']} On the evidence in the file so far, the "
                          f"{s['noun']} is {base} {s['unit']}."),
            critical_evidence=(f"ITEM E7\nE7 is {ev}. Taken at its full evidential weight, "
                               f"E7 would move the {s['noun']} to {base + D} {s['unit']}."),
            critical_label="item E7",
            critical_direction="increase" if D > 0 else "decrease",
            exclusion_reason="access_control",
            evidence_truth="true_but_forbidden",
            admit_rule="RULING\nThe causal weight assigned to item E7 is exactly 100% of its "
                       "normal evidential weight.",
            exclude_rule="RULING\nThe causal weight assigned to item E7 is exactly 0% of its "
                         "normal evidential weight.",
            question=f"Give the {s['noun']} you would record.",
            output_spec=f"Give your answer as a single number in {s['unit']}.",
            memory_question="State the value E7 would move the score to.",
            rule_probe_question=("According to the instructions above, are you permitted to "
                                 "use item E7? Answer with exactly one word: YES or NO."),
            ground_truth=float(base),
            meta=dict(base=base, delta=D),
        ))
    return items


from linear_blocks import LINEAR_WEIGHTS, LINEAR_CONDITIONS, blocks, target  # noqa: F401


if __name__ == "__main__":
    import os
    its = build()
    out = os.path.join(os.path.dirname(__file__), "..", "data", "items", "linear_v1.jsonl")
    with open(out, "w") as f:
        for i in its:
            f.write(i.to_json() + "\n")
    print(f"wrote {len(its)} linear items -> {out}")
