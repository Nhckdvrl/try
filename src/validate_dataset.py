"""Structural validation of the compiled dataset.

This runs *before* any model is touched.  Its whole job is to guarantee that the
five conditions differ from one another only in the ways the design says they
do, so that any Y difference we later measure cannot be a wording artefact.
"""
import os, sys, json
from collections import Counter
sys.path.insert(0, os.path.dirname(__file__))
from schema import load_items, compile_prompt, compile_probe, CONDITIONS, PROBES

PATH = os.path.join(os.path.dirname(__file__), "..", "data", "items", "items_v1.jsonl")


def blocks_of(prompt):
    return prompt.split("\n\n")


def check(items):
    errs, warns = [], []

    def bad(item, msg):
        errs.append(f"[{item.item_id}] {msg}")

    for it in items:
        ps = {c: compile_prompt(it, c) for c in CONDITIONS}

        # 1. the base condition must contain neither the critical evidence nor any rule
        b = ps["base"]
        if it.critical_evidence.split("\n")[0][:40] in b:
            bad(it, "critical evidence leaks into base")
        if "RULING" in b:
            bad(it, "a rule leaks into base")
        for tok in (it.admit_rule[:40], it.exclude_rule[:40]):
            if tok in b:
                bad(it, "rule text leaks into base")

        # 2. every non-base condition contains the evidence exactly once and one rule
        for c in CONDITIONS[1:]:
            p = ps[c]
            if p.count("ADDITIONAL INFORMATION") != 1:
                bad(it, f"{c}: evidence block not present exactly once")
            if p.count("RULING") != 1:
                bad(it, f"{c}: rule block not present exactly once")
            rule = it.admit_rule if c.startswith("admit") else it.exclude_rule
            other = it.exclude_rule if c.startswith("admit") else it.admit_rule
            if rule not in p:
                bad(it, f"{c}: wrong rule text")
            if other in p:
                bad(it, f"{c}: opposite rule leaked in")

        # 3. pre vs post differ ONLY by block order (same multiset of blocks)
        for a, bb in (("admit_pre", "admit_post"), ("exclude_pre", "exclude_post")):
            if sorted(blocks_of(ps[a])) != sorted(blocks_of(ps[bb])):
                bad(it, f"{a} vs {bb}: block content differs, not just order")
            if ps[a] == ps[bb]:
                bad(it, f"{a} vs {bb}: identical prompts")

        # 4. admit vs exclude at the same position differ ONLY in the rule block
        for a, bb in (("admit_pre", "exclude_pre"), ("admit_post", "exclude_post")):
            ba, bx = blocks_of(ps[a]), blocks_of(ps[bb])
            if len(ba) != len(bx):
                bad(it, f"{a} vs {bb}: different number of blocks")
                continue
            diff = [i for i, (x, y) in enumerate(zip(ba, bx)) if x != y]
            if len(diff) != 1 or not ba[diff[0]].startswith("RULING"):
                bad(it, f"{a} vs {bb}: differ outside the RULING block ({diff})")

        # 5. the base prompt is a strict prefix-structure of the others
        if blocks_of(ps["base"])[0] != blocks_of(ps["admit_pre"])[0]:
            bad(it, "background block differs across conditions")
        if blocks_of(ps["base"])[-1] != blocks_of(ps["admit_pre"])[-1]:
            bad(it, "task block differs across conditions")

        # 6. rules must be direction-symmetric in the obvious lexical sense
        if "must not" not in it.exclude_rule:
            bad(it, "exclude rule does not contain a prohibition")
        if "must take it into account" not in it.admit_rule and "must take the" not in it.admit_rule:
            bad(it, "admit rule does not contain an obligation to use")

        # 7. probes compile and ask a single yes/no or recall question
        for pr in PROBES:
            q = compile_probe(it, pr)
            if pr.startswith("rule_probe") and "YES or NO" not in q:
                bad(it, f"{pr}: not a forced-choice probe")
            if "Rate " in q.split("TASK")[-1] and pr.startswith("rule_probe"):
                bad(it, f"{pr}: decision question leaked into probe")

        # 8. the decision prompts must not contain the probe question
        if it.rule_probe_question in ps["exclude_post"]:
            bad(it, "rule probe question leaked into the decision prompt")

        if it.critical_direction not in ("increase", "decrease"):
            bad(it, "bad direction")
        if len(it.base_context) < 120:
            warns.append(f"[{it.item_id}] very short base context")

    return errs, warns


def main():
    items = load_items(PATH)
    errs, warns = check(items)
    print(f"items: {len(items)}")
    for k in ("task_family", "exclusion_reason", "critical_direction", "evidence_truth"):
        print(f"  {k}: {dict(Counter(getattr(i, k) for i in items))}")
    # per-family direction balance
    fam = {}
    for i in items:
        fam.setdefault(i.task_family, Counter())[i.critical_direction] += 1
    print("  direction balance per family:")
    for f, c in fam.items():
        print(f"    {f}: {dict(c)}")
    lens = sorted(len(compile_prompt(i, "exclude_post")) for i in items)
    print(f"  prompt chars: min {lens[0]}  median {lens[len(lens)//2]}  max {lens[-1]}")
    print(f"\nERRORS: {len(errs)}")
    for e in errs[:40]:
        print("  " + e)
    print(f"WARNINGS: {len(warns)}")
    for w in warns[:10]:
        print("  " + w)
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
