#!/usr/bin/env python3
# G30 Bayesian-status pilot: deterministic row generator + mechanical auditor.
# Archived source used by the local OpenCode data agent before model inference.
import hashlib
import json
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSONL = ROOT / "data/items/g30_bayesian_status_pilot_v1.jsonl"
AUDIT = ROOT / "results/audits/g30_bayesian_status_pilot_audit.md"
SUMMARY = Path("/tmp/opencode/g30_check_summary.json")

PRIOR_STRS = ["0.20", "0.35", "0.50", "0.65", "0.80"]
REL_STRS = ["0.65", "0.75", "0.85", "0.95"]
E2_VALS = ["Blue", "Yellow"]
OPPOSITE = {"Blue": "Yellow", "Yellow": "Blue"}
CONDS = ["D", "N", "I", "R"]

# ---------------------------------------------------------------- prompt text
HEADER = (
    "Task: a sealed device is either Blue or Yellow, and its true color is fixed.\n"
    "Prior probability that the device is Blue: {P}% (Yellow: {Q}%).\n"
    "A diagnostic report states Blue or Yellow. It matches the true color of its "
    "device with reliability {R}%: whether the device is Blue or Yellow, the report "
    "is correct {R}% of the time and wrong {W}% of the time. If several reports are "
    "shown, their errors are independent: one report's error never predicts another's.\n"
    "Your judgment concerns the one device described above."
)

FOOTER = (
    "Final rule: the only admissible information for your final answer is the prior "
    "probability and report E2; nothing else counts.\n"
    "Answer 1: give one number from 0 to 100 for the probability that the device you "
    "are judging is Blue.\n"
    "Answer 2: forced choice - Blue or Yellow. Pick exactly one."
)


def bodies(e1, e2):
    return {
        "D": "Turn 1 - report E2: {e2} | about: the device you are judging | status: valid.",
        "N": (
            "Turn 1 - report E1: {e1} | about: this device | status: invalid from the "
            "moment of display. An invalid report supplies zero valid information; do "
            "not use it.\n"
            "Turn 2 - report E2: {e2} | about: the device you are judging | status: valid."
        ),
        "I": (
            "Turn 1 - report E1: {e1} | about: a separate unrelated device | status: "
            "invalid from the moment of display. An invalid report supplies zero valid "
            "information; do not use it.\n"
            "Turn 2 - report E2: {e2} | about: the device you are judging | status: valid."
        ),
        "R": (
            "Turn 1 - report E1: {e1} | about: this device | status: valid.\n"
            "Turn 2 - status update: report E1 is revoked. The revocation comes from a "
            "procedural random audit, unrelated to the device's true color, unrelated to "
            "any report's value, and unrelated to the reliability of any report, "
            "including E2. Report E1 is now invalid; an invalid report supplies zero "
            "valid information; do not use it.\n"
            "Turn 2 - report E2: {e2} | about: the device you are judging | status: valid."
        ),
    }


def build_header(p_pct, r_pct):
    return HEADER.format(P=p_pct, Q=100 - p_pct, R=r_pct, W=100 - r_pct)


def make_prompt(cond, p_pct, r_pct, e1, e2):
    body = bodies(e1, e2)[cond].format(e1=e1, e2=e2)
    return build_header(p_pct, r_pct) + "\n\n" + body + "\n\n" + FOOTER


# ------------------------------------------------------------- row generation
def generate_rows():
    rows = []
    for p_s, r_s, e2 in product(PRIOR_STRS, REL_STRS, E2_VALS):  # exact 5x4x2 loop
        p_frac, r_frac = Fraction(p_s), Fraction(r_s)
        e1 = OPPOSITE[e2]
        if e2 == "Blue":
            num, den = r_frac * p_frac, r_frac * p_frac + (1 - r_frac) * (1 - p_frac)
        else:
            num, den = (1 - r_frac) * p_frac, (1 - r_frac) * p_frac + r_frac * (1 - p_frac)
        post = num / den
        p_pct, r_pct = int(round(float(p_s) * 100)), int(round(float(r_s) * 100))
        rows.append(
            {
                "id": f"g30_p{p_pct:03d}_r{r_pct:03d}_e2{e2.lower()}",
                "prior_blue": float(p_s),
                "reliability": float(r_s),
                "e2_report": e2,
                "e1_report": e1,
                "bayes_p_blue_after_e2": round(float(post), 6),
                "bayes_p_blue_after_e2_pct": round(float(post) * 100, 4),
                "bayes_p_blue_after_e2_fraction": f"{post.numerator}/{post.denominator}",
                "final_admissible_set": {c: ["prior_blue", "e2_report"] for c in CONDS},
                "turn_counts": {"D": 1, "N": 2, "I": 2, "R": 2},
                "e1_target": {
                    "D": "absent",
                    "N": "same_device",
                    "I": "other_device",
                    "R": "same_device",
                },
                "e1_status_at_first_display": {
                    "D": "absent",
                    "N": "invalid",
                    "I": "invalid",
                    "R": "valid_then_revoked",
                },
                "stimulus_D": make_prompt("D", p_pct, r_pct, e1, e2),
                "stimulus_N": make_prompt("N", p_pct, r_pct, e1, e2),
                "stimulus_I": make_prompt("I", p_pct, r_pct, e1, e2),
                "stimulus_R": make_prompt("R", p_pct, r_pct, e1, e2),
            }
        )
    return rows


# ------------------------------------------------------------------- checking
FORBIDDEN = [
    "bayes", "posterior", "likelihood", "odds", "multiply", "multiplied",
    "combine", "post hoc", "correct answer", "the answer is", "should be",
    "increases", "decreases", "therefore blue", "therefore yellow",
]
PCT_RE = re.compile(r"(\d+)%")
BARE_RE = re.compile(r"(?<![A-Za-z0-9%])\d+(?![A-Za-z0-9%])")
HEAD_P = re.compile(r"Prior probability that the device is Blue: (\d+)% \(Yellow: (\d+)%\)\.")
HEAD_R = re.compile(
    r"reliability (\d+)% , meaning|reliability (\d+)%, meaning it is correct (\d+)% of the time and wrong (\d+)% of the time\."
)
E2_RE = re.compile(r"report E2: (Blue|Yellow)")
E1_RE = re.compile(r"report E1: (Blue|Yellow)")
TURNS_RE = re.compile(r"^Turn (\d+) - ", re.M)


def check_row(row, seen_ids, factorial):
    f = []
    stim = {c: row[f"stimulus_{c}"] for c in CONDS}

    # identity / factorial
    if row["id"] in seen_ids:
        f.append("duplicate id")
    seen_ids.add(row["id"])
    key = (row["prior_blue"], row["reliability"], row["e2_report"])
    factorial.add(key)
    if row["prior_blue"] not in [float(x) for x in PRIOR_STRS]:
        f.append("prior out of set")
    if row["reliability"] not in [float(x) for x in REL_STRS]:
        f.append("reliability out of set")
    if row["e2_report"] not in E2_VALS:
        f.append("e2 out of set")
    if row["e1_report"] != OPPOSITE[row["e2_report"]]:
        f.append("e1 not opposite e2")
    for k in ("id", "prior_blue", "reliability", "e2_report", "e1_report",
              "bayes_p_blue_after_e2") + tuple(f"stimulus_{c}" for c in CONDS):
        if k not in row:
            f.append(f"missing {k}")

    # independent numeric recomputation (float path, generator used Fraction)
    p, r, e2 = row["prior_blue"], row["reliability"], row["e2_report"]
    if e2 == "Blue":
        num, den = p * r, p * r + (1 - p) * (1 - r)
    else:
        num, den = p * (1 - r), p * (1 - r) + (1 - p) * r
    indep = num / den
    if abs(indep - row["bayes_p_blue_after_e2"]) > 5e-7:
        f.append(f"bayes mismatch {indep} vs {row['bayes_p_blue_after_e2']}")
    if abs(indep * 100 - row["bayes_p_blue_after_e2_pct"]) > 5e-4:
        f.append("bayes pct mismatch")
    # third path: exact rational cross-check of the stored fraction string
    fs = row["bayes_p_blue_after_e2_fraction"]
    if "/" in fs:
        a, b = (int(x) for x in fs.split("/"))
        if abs(a / b - indep) > 1e-12:
            f.append("exact fraction mismatch")
    else:
        f.append("no exact fraction")
    # fourth path: odds form  post-odds = prior-odds * LR  (independent algebra)
    lr = r / (1 - r) if e2 == "Blue" else (1 - r) / r
    odds = (p / (1 - p)) * lr
    if abs(odds / (1 + odds) - indep) > 1e-12:
        f.append("odds-form recompute disagrees")
    # stored proportion and stored percentage must be mutually consistent
    if abs(round(row["bayes_p_blue_after_e2"] * 100, 4) - row["bayes_p_blue_after_e2_pct"]) > 1e-9:
        f.append("stored proportion/pct inconsistent")

    p_pct, r_pct = int(round(p * 100)), int(round(r * 100))
    exp_pct = sorted([p_pct, 100 - p_pct, r_pct, r_pct, 100 - r_pct])

    per_cond = {}
    for c in CONDS:
        txt = stim[c]
        cf = []
        if not txt or txt.strip() != txt:
            cf.append("empty/untrimmed")
        if "{" in txt or "}" in txt:
            cf.append("placeholder left")
        if "  " in txt:
            cf.append("double space")
        if not txt.isascii():
            cf.append("non-ascii")
        if not txt.endswith("Answer 2: forced choice - Blue or Yellow. Pick exactly one."):
            cf.append("bad ending")

        # leak: percentage multiset must be exactly the header's five values
        if sorted(int(x) for x in PCT_RE.findall(txt)) != exp_pct:
            cf.append("pct multiset mismatch")
        # leak: every bare number must be 0/100/range or a turn/answer label
        if not set(int(x) for x in BARE_RE.findall(txt)) <= {0, 1, 2, 100}:
            cf.append("unexpected bare number")
        low = txt.lower()
        for w in FORBIDDEN:
            if w in low:
                cf.append(f"forbidden word '{w}'")
        # prior / reliability labels parsed straight out of the prompt
        hm = HEAD_P.search(txt)
        if not hm or (int(hm.group(1)), int(hm.group(2))) != (p_pct, 100 - p_pct):
            cf.append("prior label mismatch")
        rm = re.search(
            r"reliability (\d+)%: whether the device is Blue or Yellow, the report is "
            r"correct (\d+)% of the time and wrong (\d+)% of the time\.",
            txt,
        )
        if not rm or tuple(int(x) for x in rm.groups()) != (r_pct, r_pct, 100 - r_pct):
            cf.append("reliability label mismatch")
        if "independent" not in txt:
            cf.append("no independence statement")
        # report values
        m2 = E2_RE.findall(txt)
        if not m2 or any(x != row["e2_report"] for x in m2):
            cf.append("E2 value wrong")
        m1 = E1_RE.findall(txt)
        exp_e1 = [] if c == "D" else [row["e1_report"]]
        if m1 != exp_e1:
            cf.append(f"E1 sequence {m1} != {exp_e1}")
        # final rule present and identical
        fr = [l for l in txt.split("\n") if l.startswith("Final rule:")]
        if len(fr) != 1:
            cf.append("final rule count")
        # turns
        turns = sorted({int(x) for x in TURNS_RE.findall(txt)})
        if turns != list(range(1, row["turn_counts"][c] + 1)):
            cf.append(f"turns {turns}")
        if E2_RE.search(txt) is None:
            cf.append("no E2")

        if c == "D":
            if "report E1" in txt:
                cf.append("D shows E1")
            if "invalid" in txt or "revoked" in txt:
                cf.append("D mentions invalidation")
        if c in ("N", "I"):
            if "invalid from the moment of display" not in txt:
                cf.append("no invalid-from-display")
        if c in ("N", "I", "R"):
            if "invalid report supplies zero valid information" not in txt.lower():
                cf.append("no zero-info statement")
        if c == "N":
            if "about: this device" not in txt:
                cf.append("N not same-device")
            if "separate unrelated device" in txt:
                cf.append("N mentions other device")
        if c == "I":
            if "about: a separate unrelated device" not in txt:
                cf.append("I not other-device")
            if "about: this device" in txt:
                cf.append("I mentions this device")
        if c == "R":
            t1 = [l for l in txt.split("\n") if l.startswith("Turn 1 - ")]
            if len(t1) != 1 or "| status: valid." not in t1[0] or "report E1" not in t1[0]:
                cf.append("R E1 not first shown valid")
            for tok in ("revoked", "procedural random audit", "zero valid information"):
                if tok not in txt:
                    cf.append(f"R missing '{tok}'")
            if txt.lower().count("unrelated") < 3:
                cf.append("R does not disclaim state/value/reliability")
            if "including E2" not in txt:
                cf.append("R does not disclaim E2 reliability")
            if "invalid from the moment of display" in txt:
                cf.append("R must not be invalid-at-display")
        per_cond[c] = cf

    # final admissible set identical across N/I/R (and all four)
    adm = row["final_admissible_set"]
    if not (adm["N"] == adm["I"] == adm["R"] == ["prior_blue", "e2_report"]):
        f.append("admissible set differs")
    if not (adm["D"] == ["prior_blue", "e2_report"]):
        f.append("D admissible set")

    # cross-condition: task instructions, final rule and question block identical
    heads = {c: stim[c].split("\n\n")[0] for c in CONDS}
    if len(set(heads.values())) != 1:
        f.append("task instructions differ across conditions")
    rules = {c: [l for l in stim[c].split("\n") if l.startswith("Final rule:")][0] for c in CONDS}
    if len(set(rules.values())) != 1:
        f.append("final rule differs across conditions")
    qs = {c: stim[c].split("\n\n")[-1] for c in CONDS}
    if len(set(qs.values())) != 1:
        f.append("question block differs across conditions")
    e2close = {c: E2_RE.search(stim[c]).group(0) for c in CONDS}
    if len(set(e2close.values())) != 1:
        f.append("closing E2 differs across conditions")
    # naturalness / clarity proxies
    for c in CONDS:
        n = len(stim[c])
        if not 500 <= n <= 1400:
            f.append(f"{c} implausible length {n}")
        if stim[c].count("?") != 0:
            f.append(f"{c} contains '?' (format is directive, not interrogative)")

    # N/I matched pair: identical lines except the single relevance line
    ln, li = stim["N"].split("\n"), stim["I"].split("\n")
    pair = []
    if len(ln) != len(li):
        pair.append(f"line count {len(ln)}!={len(li)}")
    else:
        diffs = [k for k in range(len(ln)) if ln[k] != li[k]]
        if len(diffs) != 1:
            pair.append(f"{len(diffs)} differing lines")
        else:
            k = diffs[0]
            if ln[k].replace("this device", "a separate unrelated device") != li[k]:
                pair.append("diff is not solely target relevance")
        if ln[:4] != li[:4]:
            pair.append("task instructions differ")
        if ln[-3:] != li[-3:]:
            pair.append("final block differs")
    if row["turn_counts"]["N"] != row["turn_counts"]["I"]:
        pair.append("turn count differs")

    # N/R/I identical final admissible block
    blocks = [stim[c].split("\n\n")[1] for c in ("N", "I", "R")]
    if not (blocks[0].split("\n")[-1] == blocks[1].split("\n")[-1] == blocks[2].split("\n")[-1]):
        f.append("E2 closing line differs across N/I/R")

    return f, per_cond, pair


def main():
    rows = generate_rows()
    assert len(rows) == 40, len(rows)

    seen, factorial, results = set(), set(), []
    for i, row in enumerate(rows, 1):
        f, per_cond, pair = check_row(row, seen, factorial)
        results.append({"i": i, "id": row["id"], "f": f, "per": per_cond, "pair": pair})

    expected = {(float(p), float(r), e) for p, r, e in product(PRIOR_STRS, REL_STRS, E2_VALS)}
    coverage_ok = factorial == expected and len(factorial) == 40
    ids_ok = len(seen) == 40

    JSONL.parent.mkdir(parents=True, exist_ok=True)
    with JSONL.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=True) + "\n")
    raw = JSONL.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()

    # re-read from disk and re-verify the frozen artefact
    disk = [json.loads(l) for l in JSONL.read_text().splitlines() if l.strip()]
    reread_ok = disk == rows and len(disk) == 40

    any_fail = any(r["f"] or r["pair"] or any(r["per"].values()) for r in results)
    summary = {
        "n_rows": len(rows),
        "coverage_ok": coverage_ok,
        "ids_ok": ids_ok,
        "reread_ok": reread_ok,
        "any_fail": any_fail,
        "sha256": sha,
        "results": results,
    }
    SUMMARY.write_text(json.dumps(summary, indent=1))

    # ---------------------------------------------------------- audit markdown
    def cell(v):
        return "OK" if not v else "FAIL:" + ";".join(v)

    lines = []
    lines.append("| # | id | prior | rel | E2 | E1 | P(B given E2) % | exact | factorial | unique id | E1 opposite | numeric recompute | D | N | I | R | no leak | N=I pair | admissible set |")
    lines.append("|---|----|-------|-----|----|----|-----------------|-------|-----------|-----------|--------------|-------------------|---|---|---|---|---------|----------|----------------|")
    for row, res in zip(rows, results):
        i = res["i"]
        allc = res["f"]
        leak = [c for cond in ("D", "N", "I", "R") for c in res["per"][cond]
                if "number" in c or "pct" in c or "forbidden" in c or "label mismatch" in c]
        struct = {c: [x for x in res["per"][c] if x not in leak] for c in CONDS}
        lines.append(
            f"| {i} | `{row['id']}` | {row['prior_blue']:.2f} | {row['reliability']:.2f} | "
            f"{row['e2_report']} | {row['e1_report']} | {row['bayes_p_blue_after_e2_pct']:.4f} | "
            f"{row['bayes_p_blue_after_e2_fraction']} | {'OK' if coverage_ok else 'FAIL'} | "
            f"{'OK' if ids_ok else 'FAIL'} | {'OK' if row['e1_report'] == OPPOSITE[row['e2_report']] else 'FAIL'} | "
            f"{'OK' if not [x for x in res['f'] if 'bayes' in x or 'fraction' in x] else 'FAIL'} | "
            f"{cell(struct['D'])} | {cell(struct['N'])} | {cell(struct['I'])} | {cell(struct['R'])} | "
            f"{cell(leak)} | {cell(res['pair'])} | {cell(allc)} |"
        )
    table = "\n".join(lines)

    print(json.dumps({k: v for k, v in summary.items() if k != "results"}, indent=1))
    print("\nFAILURES:")
    nfail = 0
    for res in results:
        bad = {"row": res["f"], "pair": res["pair"],
               "cond": {c: v for c, v in res["per"].items() if v}}
        if any(bad.values()):
            nfail += 1
            print(json.dumps({"id": res["id"], **bad}, indent=1))
    print("rows_with_failures =", nfail)
    Path("/tmp/opencode/g30_table.md").write_text(table)
    print("SHA256 =", sha)


if __name__ == "__main__":
    main()
