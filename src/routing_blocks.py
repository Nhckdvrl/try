"""Condition blocks for the selective-routing family.

Kept separate from the generator so that `schema` can import it without a
circular import back through `Item`.
"""

ROUTING_CONDITIONS = ["rt_oracle", "rt_naive", "rt_pre", "rt_post"]


def blocks(item, cond):
    B = "BACKGROUND\n" + item.base_context
    R = item.exclude_rule
    reports = item.critical_evidence
    if cond == "rt_oracle":
        # only the admitted reports exist: the ideal answer
        keep = [ln for ln in reports.split("\n")[1:] if "[verified]" in ln]
        keep = [ln.replace(" [verified]", "") for ln in keep]
        renum = [f"Report {i+1}:" + ln.split(":", 1)[1] for i, ln in enumerate(keep)]
        return [B, "REPORTS\n" + "\n".join(renum)]
    if cond == "rt_naive":
        strip = [ln.replace(" [verified]", "").replace(" [unverified]", "")
                 for ln in reports.split("\n")[1:]]
        return [B, "REPORTS\n" + "\n".join(strip)]
    if cond == "rt_pre":
        return [B, R, reports]
    if cond == "rt_post":
        return [B, reports, R]
    raise ValueError(cond)


