"""Stage-3C: the four adversarial tests of the narrow claim."""
import json, os, sys, statistics as st
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from schema import load_items
from analyze import wins
from analyze_stage2 import cluster_of
from analyze_png import cluster_boot
import conditions_v5 as v5

ROOT = os.path.join(os.path.dirname(__file__), "..")


def load(tag, suffix="stage5"):
    runs = defaultdict(dict)
    for line in open(os.path.join(ROOT, "results", "raw", f"{tag}_{suffix}.jsonl")):
        r = json.loads(line)
        runs[r["item_id"]][r["kind_name"]] = r
    return runs


def anch(runs, items, base_key, full_keys):
    out = {}
    for iid, r in runs.items():
        it = items.get(iid)
        if it is None or base_key not in r or r[base_key].get("value") is None:
            continue
        if any(k not in r or r[k].get("value") is None for k in full_keys):
            continue
        s = 1.0 if it.critical_direction == "increase" else -1.0
        y0 = r[base_key]["value"]
        L = st.mean(r[k]["value"] for k in full_keys) - y0
        if s * L <= 0:
            continue
        out[iid] = (y0, abs(L), s)
    return out


def rei(runs, a, iid, cond):
    r = runs[iid].get(cond)
    if r is None or r.get("value") is None:
        return None
    y0, absL, s = a[iid]
    return wins(s * (r["value"] - y0) / absL)


def col(runs, a, cond, items):
    v, c = [], []
    for iid in a:
        x = rei(runs, a, iid, cond)
        if x is not None:
            v.append(x)
            c.append(cluster_of(items[iid]))
    return v, c


def paired(runs, a, c1, c2, items):
    d, cl = [], []
    for iid in a:
        x, y = rei(runs, a, iid, c1), rei(runs, a, iid, c2)
        if x is not None and y is not None:
            d.append(x - y)
            cl.append(cluster_of(items[iid]))
    return d, cl


def run(tag, items, out):
    runs = load(tag)
    out.append(f"\n# {tag}\n")

    # ---------- P0-1 inclusion implicature ----------
    out.append("## P0-1 Inclusion implicature (H-D)\n")
    out.append("Presentation policy at the top of the file; it never mentions the item, "
               "exclusion, or zero. Rule is always `weight = exactly 0%`.\n")
    out.append("| presentation policy | REI pre | REI post | pre - post |")
    out.append("|---|---|---|---|")
    store = {}
    for v_ in v5.PRESENTATION:
        a = anch(runs, items, f"inc_{v_}_base", [f"inc_{v_}_full"])
        if not a:
            continue
        pv, _ = col(runs, a, f"inc_{v_}_pre", items)
        qv, _ = col(runs, a, f"inc_{v_}_post", items)
        d, cl = paired(runs, a, f"inc_{v_}_pre", f"inc_{v_}_post", items)
        m, lo, hi, p = cluster_boot(d, cl, n=4000, seed=1)
        store[v_] = (st.mean(pv), st.mean(qv), m)
        out.append(f"| `{v_}` (n={len(d)}) | {st.mean(pv):+.3f} | {st.mean(qv):+.3f} | "
                   f"**{m:+.3f}** [{lo:+.3f}, {hi:+.3f}] p={p:.4f} |")
    if "none" in store and "audit" in store:
        a = anch(runs, items, "inc_none_base", ["inc_none_full"])
        a2 = anch(runs, items, "inc_audit_base", ["inc_audit_full"])
        both = set(a) & set(a2)
        d = [rei(runs, a, i, "inc_none_pre") - rei(runs, a2, i, "inc_audit_pre")
             for i in both
             if rei(runs, a, i, "inc_none_pre") is not None
             and rei(runs, a2, i, "inc_audit_pre") is not None]
        cl = [cluster_of(items[i]) for i in both
              if rei(runs, a, i, "inc_none_pre") is not None
              and rei(runs, a2, i, "inc_audit_pre") is not None]
        m, lo, hi, p = cluster_boot(d, cl, n=4000, seed=2)
        out.append(f"\n- Rescue from the audit policy, prospective arm "
                   f"(`none_pre` - `audit_pre`): **{m:+.3f}** [{lo:+.3f}, {hi:+.3f}] p={p:.4f}")

    A0 = anch(runs, items, "inc_none_base", ["inc_none_full"])

    # ---------- P0-3 state externalisation ----------
    out.append("\n## P0-3 State externalisation\n")
    out.append("| condition | REI pre | REI post | pre - post | stated weight (pre) |")
    out.append("|---|---|---|---|---|")
    for key, nm in (("sc_a", "decision only"),
                    ("sc_b", "model writes ITEM DECISION WEIGHT first"),
                    ("sc_c", "weight teacher-forced to 0%")):
        pv, _ = col(runs, A0, f"{key}_pre", items)
        qv, _ = col(runs, A0, f"{key}_post", items)
        if not pv:
            continue
        d, cl = paired(runs, A0, f"{key}_pre", f"{key}_post", items)
        m, lo, hi, p = cluster_boot(d, cl, n=4000, seed=3)
        sw = [runs[i][f"{key}_pre"].get("stated_weight") for i in A0
              if f"{key}_pre" in runs[i] and runs[i][f"{key}_pre"].get("stated_weight") is not None]
        swtxt = f"{st.mean(sw):.2f}%" if sw else "—"
        out.append(f"| {nm} | {st.mean(pv):+.3f} | {st.mean(qv):+.3f} | "
                   f"**{m:+.3f}** [{lo:+.3f}, {hi:+.3f}] p={p:.4f} | {swtxt} |")

    # ---------- P0-4 identity vs arbitrary tag ----------
    out.append("\n## P0-4 Identity predicate vs arbitrary-tag predicate\n")
    out.append("Both conditional, both locally checkable when the item arrives, tag `Z9` "
               "carries no semantics.\n")
    out.append("| predicate | REI pre | REI post | pre - post |")
    out.append("|---|---|---|---|")
    for pred, nm in (("idp", "`if ID is E7 -> weight 0`"), ("tagp", "`if tag is Z9 -> weight 0`")):
        a = anch(runs, items, "inc_none_base", [f"{pred}_f_pre", f"{pred}_f_post"])
        if not a:
            continue
        pv, _ = col(runs, a, f"{pred}_z_pre", items)
        qv, _ = col(runs, a, f"{pred}_z_post", items)
        d, cl = paired(runs, a, f"{pred}_z_pre", f"{pred}_z_post", items)
        m, lo, hi, p = cluster_boot(d, cl, n=4000, seed=4)
        out.append(f"| {nm} (n={len(d)}) | {st.mean(pv):+.3f} | {st.mean(qv):+.3f} | "
                   f"**{m:+.3f}** [{lo:+.3f}, {hi:+.3f}] p={p:.4f} |")

    # ---------- P1-7 salience control ----------
    out.append("\n## P1-7 Salience control: the same preview stubs with NO rule\n")
    out.append("Effective weight of the evidence when nothing forbids it. If previews raise "
               "this, the Stage-3A ladder result is salience, not binding.\n")
    for c in v5.SAL_CONDITIONS:
        v_, _ = col(runs, A0, c, items)
        if v_:
            out.append(f"- `{c}`: leverage-normalised weight {st.mean(v_):+.3f}")

    # ---------- P1-8 occurrence vs content ----------
    out.append("\n## P1-8 Occurrence vs content binding\n")
    v_, _ = col(runs, A0, "occ_prevx", items)
    p_, _ = col(runs, A0, "sc_a_pre", items)
    q_, _ = col(runs, A0, "sc_a_post", items)
    if v_:
        out.append(f"- `E -> rule -> E again` (full content present when the rule is stated): "
                   f"REI {st.mean(v_):+.3f}")
        out.append(f"- reference: rule-first {st.mean(p_):+.3f}, rule-last {st.mean(q_):+.3f}")


def main(tags):
    items = {i.item_id: i for i in load_items(os.path.join(ROOT, "data", "items", "items_v1.jsonl"))}
    out = ["# Stage 3C — attacking the narrow claim", ""]
    for t in tags:
        try:
            run(t, items, out)
        except FileNotFoundError:
            out.append(f"\n# {t}: not run yet")
    txt = "\n".join(out)
    print(txt)
    open(os.path.join(ROOT, "results", "stage5_tables.md"), "w").write(txt + "\n")


if __name__ == "__main__":
    main(sys.argv[1:] or ["qwen3-8b", "gemma3-12b", "phi4-mini",
                          "mistral-small-24b", "qwen3.5-27b"])
