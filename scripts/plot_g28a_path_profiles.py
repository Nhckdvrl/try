"""Exploratory scientific figure for G28A/G28B planned runnable models."""

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
TAGS = ("mistral-small-24b", "qwen3-8b", "gemma3-12b")
ROLES = ("support", "refute")
CONDS = ("D", "IJ", "RJ", "IR", "RR")


def main():
    data = {}
    for tag in TAGS:
        a = [json.loads(s) for s in (ROOT / f"results/raw/{tag}_g28a_path_v1.jsonl").read_text().splitlines() if s]
        b = [json.loads(s) for s in (ROOT / f"results/raw/{tag}_g28b_read_control_v1.jsonl").read_text().splitlines() if s]
        f = {(r["cfb_id"], r["final_role"], r["condition"]): r["value"]
             for r in a + b if r["stage"] == "final" and r["condition"] in CONDS}
        assert len(f) == 200 * 2 * 5
        data[tag] = f
    ids = sorted({k[0] for k in data[TAGS[0]]})
    assert len(ids) == 200
    arr = np.array([[[[data[t][(cid, role, cond)] for cond in CONDS]
                       for role in ROLES] for t in TAGS] for cid in ids])
    # (claim, model, E2 role, condition); resample whole claims across models.
    rng = np.random.default_rng(20260927)
    ix = rng.integers(0, len(ids), size=(3000, len(ids)))
    point = arr.mean(axis=(0, 1))
    boot = arr[ix].mean(axis=(1, 2))
    lo, hi = np.quantile(boot, [.025, .975], axis=0)

    fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.4), sharey=True, layout="constrained")
    specs = [([0, 1, 2], ["Direct", "Irrelevant\njudged", "Relevant\njudged"], "Earlier model judgment"),
             ([0, 3, 4], ["Direct", "Irrelevant\nread", "Relevant\nread"], "Read only; same acknowledgment")]
    colors = {"support": "#1678A8", "refute": "#C2583D"}
    for ax, (cols, labels, title) in zip(axes, specs):
        x = np.arange(3)
        for ri, role in enumerate(ROLES):
            y = point[ri, cols]
            err = np.vstack([y - lo[ri, cols], hi[ri, cols] - y])
            ax.errorbar(x, y, yerr=err, marker="o", capsize=3, linewidth=1.7,
                        markersize=5, color=colors[role], label="E2 " + role)
        ax.set_xticks(x, labels)
        ax.set_title(title)
        ax.set_ylim(0, 100)
        ax.grid(axis="y", alpha=.22)
    axes[0].set_ylabel("Final claim likelihood (0–100)")
    axes[1].legend(loc="center right", fontsize=8, frameon=False)
    fig.suptitle("Same final evidence, different revoked histories", fontsize=12)
    fig.text(.5, -.02,
             "ConfB 200 claims; three planned runnable models. Points are means; bars are claim-bootstrap 95% CIs. Exploratory.",
             ha="center", va="top", fontsize=8)
    png = ROOT / "figures/g28a_path_profiles_v1.png"
    pdf = ROOT / "figures/g28a_path_profiles_v1.pdf"
    fig.savefig(png, dpi=200, bbox_inches="tight")
    fig.savefig(pdf, bbox_inches="tight")
    print(png, pdf)


if __name__ == "__main__":
    main()
