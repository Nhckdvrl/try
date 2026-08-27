import json, os, sys, statistics as st
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from analyze import boot_ci

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
d = json.load(open(os.path.join(ROOT, "results", "mech", "patch_matched.json")))
Ls, recs = d["layers"], d["records"]

out = ["# Stage 5 — same-chronology bidirectional patching", "",
       "FAILURE = unrelated preview -> rule(0%) -> evidence -> answer",
       "SUCCESS = paraphrase preview -> rule(0%) -> evidence -> answer",
       "Length-matched to within a few tokens; the evidence the decision reads sits after",
       "the rule on both sides, so token order is not the difference.", ""]

use = []
for r in recs:
    s = 1.0 if r["direction"] == "increase" else -1.0
    y = r["y"]
    gap = s * (y["UE"] - y["ME"])          # how much more the failure run leaks
    inter = s * ((y["ME"] - y["MA"]) - (y["UE"] - y["UA"]))
    if abs(y["UE"] - y["ME"]) < 2.0:
        continue
    r["s"], r["gap"], r["inter"] = s, gap, inter
    use.append(r)

g = [r["gap"] for r in use]
i2 = [r["inter"] for r in use]
m, lo, hi = boot_ci(g, n=4000, seed=1)
mi, loi, hii = boot_ci(i2, n=4000, seed=2)
out.append(f"n = {len(use)} of {len(recs)} items with a behavioural gap >= 2 points.")
out.append(f"- behavioural gap, failure - success: {m:+.1f} [{lo:+.1f}, {hi:+.1f}] rating points")
out.append(f"- 2x2 interaction (ME-MA)-(UE-UA), sign-aligned: {mi:+.1f} [{loi:+.1f}, {hii:+.1f}]")
out.append("")

for direction, nm in (("success_into_failure", "patch SUCCESS state into the FAILURE run "
                                                "(does it rescue?)"),
                      ("failure_into_success", "patch FAILURE state into the SUCCESS run "
                                                "(does it break it?)")):
    out.append(f"## {nm}\n")
    out.append("Recovery fraction: 1.0 = the patched run answers like the donor condition, "
               "0.0 = like its own.")
    out.append("")
    out.append("| layer | " + " | ".join(["preview end", "rule end", "rule SPAN", "evidence end", "answer"]) + " |")
    out.append("|---:|" + "---|" * 5)
    for li, L in enumerate(Ls):
        cells = []
        for site in ("preview_end", "rule_end", "rule_span", "evidence_end", "answer"):
            vals = []
            for r in use:
                res = r["patch"].get(direction, {}).get(site)
                if not res or res[li] is None:
                    continue
                own = r["y"]["UE"] if direction == "success_into_failure" else r["y"]["ME"]
                don = r["y"]["ME"] if direction == "success_into_failure" else r["y"]["UE"]
                if abs(don - own) < 2.0:
                    continue
                vals.append((res[li] - own) / (don - own))
            cells.append(f"{st.median(vals):+.2f}" if len(vals) >= 10 else "—")
        out.append(f"| {L} | " + " | ".join(cells) + " |")
    out.append("")

txt = "\n".join(out)
print(txt)
open(os.path.join(ROOT, "results", "mech", "patch_matched_report.md"), "w").write(txt + "\n")
