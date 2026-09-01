"""Generate the paper's figures from the committed result JSONs.

Each figure reads only files that already exist and is skipped with a message
if its inputs are missing, so this runs at any point in the campaign.

    python src/make_figures.py --out figures/
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

PANEL = ("qwen35-9b", "gemma3-12b", "mistral-small-24b")
LABEL = {
    "qwen35-9b": "Qwen3.5-9B",
    "gemma3-12b": "Gemma-3-12B",
    "mistral-small-24b": "Mistral-24B",
}
plt.rcParams.update({
    "figure.dpi": 160,
    "font.size": 9,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.25,
    "grid.linewidth": 0.5,
})


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def fig_dissociation(results: Path, out: Path) -> str | None:
    """Recognition at ceiling versus intrusion, per checkpoint."""
    data = load(results / "g4_model_breadth_interim.json") or load(
        results / "g4_model_breadth_analysis.json"
    )
    if not data:
        return None
    rows = [
        (m["tag"], m["boundary_accuracy"] * 100, m["metrics"]["out_of_set_intrusion"], m["qualified"], m["family"])
        for m in data["per_model"].values()
        if "metrics" in m
    ]
    if not rows:
        return None
    rows.sort(key=lambda r: r[2]["mean"])

    fig, ax = plt.subplots(figsize=(6.2, 3.4))
    for i, (tag, probe, intr, qual, family) in enumerate(rows):
        colour = "#1f77b4" if qual else "#bbbbbb"
        ax.errorbar(
            intr["mean"], i,
            xerr=[[intr["mean"] - intr["ci_low"]], [intr["ci_high"] - intr["mean"]]],
            fmt="o", ms=4, color=colour, capsize=2, lw=1,
        )
        ax.text(intr["ci_high"] + 1.2, i, f"{probe:.0f}%", va="center", fontsize=7, color=colour)
    ax.axvline(5.0, color="#d62728", ls="--", lw=0.8)
    ax.text(5.4, len(rows) - 0.6, "SESOI", color="#d62728", fontsize=7)
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r[0] for r in rows], fontsize=7)
    ax.set_xlabel("OutOfSetIntrusion (probability points, 95% cluster bootstrap CI)")
    ax.set_title("Recognition is at ceiling; enforcement is not\n"
                 "grey = failed the recognition floor; right label = boundary-probe accuracy",
                 fontsize=8, loc="left")
    fig.tight_layout()
    path = out / "fig1_dissociation.png"
    fig.savefig(path)
    plt.close(fig)
    return str(path)


def fig_exclusion_reason(results: Path, out: Path) -> str | None:
    """Four exclusion reasons, three models."""
    data = load(results / "g3_exclusion_reason_analysis.json")
    if not data:
        return None
    arms = ("temporal", "bare", "unreliable", "procedural")
    colours = {"temporal": "#333333", "bare": "#8c8c8c", "unreliable": "#d62728", "procedural": "#1f77b4"}

    fig, ax = plt.subplots(figsize=(6.2, 3.2))
    width = 0.2
    for j, arm in enumerate(arms):
        xs, ys, lo, hi = [], [], [], []
        for i, tag in enumerate(PANEL):
            m = data["per_model"].get(tag)
            if not m:
                continue
            e = m["intrusion"][arm]
            xs.append(i + (j - 1.5) * width)
            ys.append(e["mean"])
            lo.append(e["mean"] - e["ci_low"])
            hi.append(e["ci_high"] - e["mean"])
        ax.bar(xs, ys, width * 0.9, label=arm, color=colours[arm])
        ax.errorbar(xs, ys, yerr=[lo, hi], fmt="none", ecolor="black", capsize=2, lw=0.7)
    ax.axhline(5.0, color="#d62728", ls="--", lw=0.8)
    ax.set_xticks(range(len(PANEL)))
    ax.set_xticklabels([LABEL[t] for t in PANEL])
    ax.set_ylabel("OutOfSetIntrusion")
    ax.set_title("No stated reason for exclusion reduces the effect", fontsize=9, loc="left")
    ax.legend(fontsize=7, frameon=False, ncol=4)
    fig.tight_layout()
    path = out / "fig2_exclusion_reason.png"
    fig.savefig(path)
    plt.close(fig)
    return str(path)


def fig_outcome_entrainment(results: Path, out: Path) -> str | None:
    """G8 → G11 explanatory sequence: irrelevant packets and verdict redaction."""
    swap = load(results / "g8_packet_swap_analysis.json")
    red = load(results / "g11_redacted_swap_analysis.json")
    if not swap or not red:
        return None

    fig, axes = plt.subplots(1, 2, figsize=(8.2, 3.25), gridspec_kw={"width_ratios": [1.15, 1]})
    colours = ("#333333", "#3977a8", "#d9782d")
    width = 0.22

    # Panel A: the direction changes with the source of the packet. The real
    # packet is scored toward the recipient outcome; foreign packets are scored
    # toward the donor outcome.
    directional = (
        ("real packet\n(recipient outcome)", lambda s, r: s["I_real"]),
        ("foreign packet\n(donor outcome)", lambda s, r: s["I_donor"]),
        ("redacted foreign\n(donor outcome)", lambda s, r: r["donor_pull_redacted"]),
    )
    ax = axes[0]
    for j, (label, getter) in enumerate(directional):
        xs, means, lo, hi = [], [], [], []
        for i, tag in enumerate(PANEL):
            e = getter(swap["per_model"][tag], red["per_model"][tag])
            xs.append(i + (j - 1) * width)
            means.append(e["mean"])
            lo.append(e["mean"] - e["ci_low"])
            hi.append(e["ci_high"] - e["mean"])
        ax.bar(xs, means, width * 0.92, color=colours[j], label=label)
        ax.errorbar(xs, means, yerr=[lo, hi], fmt="none", ecolor="black", capsize=2, lw=0.7)
    ax.axhline(0, color="black", lw=0.7)
    ax.set_xticks(range(len(PANEL)))
    ax.set_xticklabels([LABEL[t] for t in PANEL], fontsize=7.5)
    ax.set_ylabel("Outcome-directed pull (points)")
    ax.set_title("A  Irrelevant future evidence pulls toward its own outcome", loc="left", fontsize=8.5)
    ax.legend(frameon=False, fontsize=6.7, ncol=1, loc="upper right")

    # Panel B: absolute movement shows that foreign text perturbs the judgment
    # substantially even when its donor pull is below the frozen 5-point SESOI.
    movement = (
        ("real", lambda s, r: s["S_real"]),
        ("foreign", lambda s, r: s["S_swap"]),
        ("redacted foreign", lambda s, r: r["S_redacted"]),
    )
    ax = axes[1]
    for j, (label, getter) in enumerate(movement):
        xs, means, lo, hi = [], [], [], []
        for i, tag in enumerate(PANEL):
            e = getter(swap["per_model"][tag], red["per_model"][tag])
            xs.append(i + (j - 1) * width)
            means.append(e["mean"])
            lo.append(e["mean"] - e["ci_low"])
            hi.append(e["ci_high"] - e["mean"])
        ax.bar(xs, means, width * 0.92, color=colours[j], label=label)
        ax.errorbar(xs, means, yerr=[lo, hi], fmt="none", ecolor="black", capsize=2, lw=0.7)
    ax.set_xticks(range(len(PANEL)))
    ax.set_xticklabels([LABEL[t] for t in PANEL], fontsize=7.5)
    ax.set_ylabel("Absolute movement (points)")
    ax.set_title("B  Foreign packets retain substantial causal influence", loc="left", fontsize=8.5)
    ax.legend(frameon=False, fontsize=6.7)

    fig.suptitle("Retrospective outcome entrainment survives relevance and verdict removal",
                 x=0.06, ha="left", fontsize=9.5, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    path = out / "fig2_outcome_entrainment.png"
    fig.savefig(path)
    plt.close(fig)
    return str(path)


def fig_restoration(results: Path, out: Path) -> str | None:
    """G6 restoration curve, if the sweep has run."""
    data = load(results / "g6_span_sweep_analysis.json")
    if not data or not data.get("per_model"):
        return None
    fig, ax = plt.subplots(figsize=(5.4, 3.2))
    for tag, m in data["per_model"].items():
        pairs = sorted(
            ((float(f), r) for f, r in m["restoration_curve"].items() if r), key=lambda kv: kv[0]
        )
        if not pairs:
            continue
        xs = [f for f, _ in pairs]
        ys = [r["mean"] for _, r in pairs]
        lo = [r["mean"] - r["ci_low"] for _, r in pairs]
        hi = [r["ci_high"] - r["mean"] for _, r in pairs]
        ax.errorbar(xs, ys, yerr=[lo, hi], fmt="o-", ms=3, lw=1, capsize=2,
                    label=LABEL.get(tag, tag))
        control = m.get("wrong_span_restoration")
        if control:
            ax.axhline(control["mean"], ls=":", lw=0.8, alpha=0.6)
    ax.axhline(0.5, color="#d62728", ls="--", lw=0.8)
    ax.set_xlabel("mask applied from this fraction of depth onward")
    ax.set_ylabel("fraction of the effect restored")
    ax.set_title("How late can the intervention be and still work?", fontsize=9, loc="left")
    ax.legend(fontsize=7, frameon=False)
    fig.tight_layout()
    path = out / "fig3_restoration.png"
    fig.savefig(path)
    plt.close(fig)
    return str(path)


def fig_decision_state(results: Path, out: Path) -> str | None:
    """G12 causal factorization and G15 fresh-confirmed mechanism trajectory."""
    paired = load(results / "g12_donor_outcome_analysis.json")
    mech = load(results / "mech" / "g15_decision_confirmation_analysis.json")
    if not paired or not mech:
        return None
    fig, axes = plt.subplots(1, 3, figsize=(10.2, 3.25),
                             gridspec_kw={"width_ratios": [0.9, 1.05, 1.25]})

    ax = axes[0]
    means=[]; lo=[]; hi=[]
    for tag in PANEL:
        e=paired["per_model"][tag]["causal_contrast"]
        means.append(e["mean"]);lo.append(e["mean"]-e["ci_low"]);hi.append(e["ci_high"]-e["mean"])
    xs=list(range(len(PANEL)))
    ax.bar(xs,means,color=("#3977a8","#d9782d","#6b8e23"),width=.68)
    ax.errorbar(xs,means,yerr=[lo,hi],fmt="none",ecolor="black",capsize=2,lw=.8)
    ax.axhline(0,color="black",lw=.7);ax.axhline(5,color="#b6423c",ls="--",lw=.7)
    ax.set_xticks(xs);ax.set_xticklabels([LABEL[t].replace("-","\n",1) for t in PANEL],fontsize=6.8)
    ax.set_ylabel("YES donor − NO donor (points)")
    ax.set_title("A  Donor outcome controls direction",loc="left",fontsize=8.3)

    layers=[int(x) for x in mech["representation"]["per_layer"]]
    layers.sort()
    ax=axes[1]
    ordering=[100*mech["representation"]["per_layer"][str(l)]["ordering_accuracy"] for l in layers]
    ax.plot(layers,ordering,"o-",color="#6a4c93",ms=3,lw=1.2)
    ax.axhline(75,color="#b6423c",ls="--",lw=.7,label="frozen gate")
    ax.set_ylim(45,102);ax.set_xlabel("decoder layer");ax.set_ylabel("Held-out paired ordering (%)")
    ax.set_title("B  Decision coordinate emerges late",loc="left",fontsize=8.3)
    ax.legend(frameon=False,fontsize=6.5,loc="lower right")

    ax=axes[2]
    for key,label,colour in (("outcome_axis","outcome coordinate","#d9782d"),
                             ("orthogonal_axis","orthogonal control","#777777")):
        es=[mech["causal"]["per_layer"][str(l)][key] for l in layers]
        means=[e["mean"] for e in es]
        ax.plot(layers,means,"o-",color=colour,ms=3,lw=1.2,label=label)
        ax.fill_between(layers,[e["ci_low"] for e in es],[e["ci_high"] for e in es],color=colour,alpha=.14,lw=0)
    ax.axhline(0,color="black",lw=.7);ax.axhline(3,color="#b6423c",ls="--",lw=.7)
    ax.set_xlabel("decoder layer");ax.set_ylabel("Bidirectional causal transfer (points)")
    ax.set_title("C  Only the late decision coordinate is causal",loc="left",fontsize=8.3)
    ax.legend(frameon=False,fontsize=6.5,loc="upper left")

    fig.suptitle("Future outcome is contextualized into a late causal decision state",
                 x=.04,ha="left",fontsize=9.5,fontweight="bold")
    fig.tight_layout(rect=(0,0,1,.93))
    path=out/"fig3_decision_state.png";fig.savefig(path);plt.close(fig);return str(path)


def fig_mitigation(results: Path, out: Path) -> str | None:
    """Every intervention tried, on one axis, against the direct baseline."""
    baseline = load(results / "g3_exclusion_reason_analysis.json")
    if not baseline:
        return None
    series: dict[str, dict[str, float]] = {}
    for tag in PANEL:
        m = baseline["per_model"].get(tag)
        if m:
            series.setdefault("stated reason (best arm)", {})[tag] = min(
                m["intrusion"][a]["mean"] for a in ("temporal", "bare", "unreliable", "procedural")
            )
            series.setdefault("direct", {})[tag] = m["intrusion"]["temporal"]["mean"]
    delib = load(results / "g5_deliberation_analysis.json")
    if delib:
        for tag in PANEL:
            m = delib["per_model"].get(tag)
            if m:
                series.setdefault("chain of thought", {})[tag] = m["intrusion"]["cot"]["mean"]
                series.setdefault("ex-ante state scaffold", {})[tag] = m["intrusion"]["state"]["mean"]
    few = load(results / "g10_fewshot_analysis.json")
    if few:
        for tag in PANEL:
            m = few["per_model"].get(tag)
            if m:
                series.setdefault("worked examples", {})[tag] = m["I_fewshot"]["mean"]
    sweep = load(results / "g6_span_sweep_analysis.json")
    if sweep:
        for tag, m in sweep.get("per_model", {}).items():
            full = m.get("full_depth_restoration")
            direct = series.get("direct", {}).get(tag)
            if full and direct is not None:
                series.setdefault("span masking (ours)", {})[tag] = direct * (1 - full["mean"])

    order = [k for k in (
        "direct", "stated reason (best arm)", "chain of thought",
        "ex-ante state scaffold", "worked examples", "span masking (ours)",
    ) if k in series]
    if len(order) < 2:
        return None

    fig, ax = plt.subplots(figsize=(6.4, 3.2))
    width = 0.8 / len(PANEL)
    for i, tag in enumerate(PANEL):
        xs = [j + (i - (len(PANEL) - 1) / 2) * width for j in range(len(order))]
        ys = [series[k].get(tag, float("nan")) for k in order]
        ax.bar(xs, ys, width * 0.9, label=LABEL[tag])
    ax.axhline(0, color="black", lw=0.8)
    ax.set_xticks(range(len(order)))
    ax.set_xticklabels(order, rotation=18, ha="right", fontsize=7.5)
    ax.set_ylabel("OutOfSetIntrusion")
    ax.set_title("What reduces it", fontsize=9, loc="left")
    ax.legend(fontsize=7, frameon=False, ncol=3)
    fig.tight_layout()
    path = out / "fig4_mitigation.png"
    fig.savefig(path)
    plt.close(fig)
    return str(path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", type=Path, default=Path("results"))
    parser.add_argument("--out", type=Path, default=Path("figures"))
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    for name, fn in (
        ("dissociation", fig_dissociation),
        ("outcome entrainment", fig_outcome_entrainment),
        ("decision state", fig_decision_state),
        ("appendix: exclusion", fig_exclusion_reason),
        ("restoration curve", fig_restoration),
        ("mitigation ladder", fig_mitigation),
    ):
        path = fn(args.results, args.out)
        print(f"{name:20s} {path if path else '(inputs not present yet)'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
