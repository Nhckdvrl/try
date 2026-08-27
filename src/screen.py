"""Item screening (README section 8).

Screening uses ONLY base / admit / admit-rule-probe.  The exclude conditions are
not generated at this point, so it is structurally impossible for the phenomenon
to be written into the dataset by item selection.
"""
import argparse, json, os, sys
from collections import defaultdict, Counter
sys.path.insert(0, os.path.dirname(__file__))
from schema import load_items

ROOT = os.path.join(os.path.dirname(__file__), "..")

# family -> (base_lo, base_hi, min_leverage)
# For the 0-100 families the leverage floor is on the raw rating scale; for the
# numeric family it is expressed as a fraction of the analytic pull the critical
# reading would exert on a naive six-value mean.
RULES = {
    "legal_judgment":     dict(lo=15, hi=85, min_lev=8.0),
    "ranking_selection":  dict(lo=15, hi=85, min_lev=8.0),
    "evidence_inference": dict(lo=15, hi=85, min_lev=8.0),
    "outcome_evaluation": dict(lo=15, hi=85, min_lev=8.0),
    "numeric_aggregation": dict(lo=None, hi=None, min_lev=0.40),   # fraction of naive_shift
}


def load_runs(paths):
    d = defaultdict(dict)
    for p in paths:
        for line in open(p):
            r = json.loads(line)
            d[r["item_id"]][r["kind_name"]] = r
    return d


def screen(items, runs, verbose=True):
    rows = []
    for it in items:
        r = runs.get(it.item_id, {})
        if not all(k in r for k in ("base", "admit_pre", "admit_post", "rule_probe_admit_post")):
            continue
        y0 = r["base"]["value"]
        ya1, ya2 = r["admit_pre"]["value"], r["admit_post"]["value"]
        if None in (y0, ya1, ya2):
            continue
        ya = (ya1 + ya2) / 2.0
        L = ya - y0
        sgn = 1.0 if it.critical_direction == "increase" else -1.0
        rule = RULES[it.task_family]
        if it.task_family == "numeric_aggregation":
            denom = abs(it.meta["naive_shift"])
            lev_ok = (sgn * L) >= rule["min_lev"] * denom
            base_ok = abs(y0 - it.ground_truth) <= 0.75 * denom   # base aggregation is sane
        else:
            lev_ok = (sgn * L) >= rule["min_lev"]
            base_ok = rule["lo"] <= y0 <= rule["hi"]
        # Direction must be stable across the two admit orders.  Models emit heavily
        # quantised ratings, so a tie is not evidence of instability; only an actual
        # reversal in one of the two orders disqualifies the item.
        dir_ok = (sgn * (ya1 - y0) >= 0) and (sgn * (ya2 - y0) >= 0)
        py = r["rule_probe_admit_post"].get("p_yes")
        rule_ok = (py is not None) and (py >= 0.80)   # must clearly know E is usable here
        keep = lev_ok and base_ok and dir_ok and rule_ok
        rows.append(dict(item_id=it.item_id, task_family=it.task_family,
                         exclusion_reason=it.exclusion_reason,
                         evidence_truth=it.evidence_truth,
                         direction=it.critical_direction,
                         base=y0, admit_pre=ya1, admit_post=ya2, admit=ya, p_yes_admit=py,
                         L=L, signed_L=sgn * L,
                         base_ok=base_ok, lev_ok=lev_ok, dir_ok=dir_ok, rule_ok=rule_ok,
                         keep=keep))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", nargs="+", required=True)
    ap.add_argument("--items", default=os.path.join(ROOT, "data", "items", "items_v1.jsonl"))
    ap.add_argument("--out", required=True)
    ap.add_argument("--report", required=True)
    args = ap.parse_args()

    items = load_items(args.items)
    rows = screen(items, load_runs(args.runs))
    kept = [r for r in rows if r["keep"]]

    lines = [f"screened {len(rows)} items, kept {len(kept)}", ""]
    per = defaultdict(Counter)
    for r in rows:
        per[r["task_family"]]["n"] += 1
        per[r["task_family"]]["keep"] += int(r["keep"])
        for f in ("base_ok", "lev_ok", "dir_ok", "rule_ok"):
            per[r["task_family"]][f] += int(r[f])
    lines.append(f"{'family':22s} {'n':>4s} {'kept':>5s} {'base_ok':>8s} {'lev_ok':>7s} {'dir_ok':>7s} {'rule_ok':>8s}  median|L|")
    for f, c in per.items():
        med = sorted(abs(r["L"]) for r in rows if r["task_family"] == f)
        lines.append(f"{f:22s} {c['n']:4d} {c['keep']:5d} {c['base_ok']:8d} {c['lev_ok']:7d} "
                     f"{c['dir_ok']:7d} {c['rule_ok']:8d}  {med[len(med)//2]:.1f}")
    lines.append("")
    kc = Counter((r["task_family"], r["direction"]) for r in kept)
    lines.append("kept direction balance: " + json.dumps({f"{a}/{b}": v for (a, b), v in sorted(kc.items())}))
    kr = Counter(r["exclusion_reason"] for r in kept)
    lines.append("kept exclusion reasons:  " + json.dumps(dict(sorted(kr.items()))))
    kt = Counter(r["evidence_truth"] for r in kept)
    lines.append("kept evidence truth:     " + json.dumps(dict(sorted(kt.items()))))
    txt = "\n".join(lines)
    print(txt)

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    json.dump([r["item_id"] for r in kept], open(args.out, "w"), indent=1)
    json.dump(rows, open(args.report, "w"), indent=1)
    print(f"\nfrozen item list -> {args.out}")


if __name__ == "__main__":
    main()
