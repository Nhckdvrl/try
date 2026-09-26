"""Standalone G29/G29B figure: rating separation and binary E2 use."""

import json
import random
import statistics as st
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
TAGS=("mistral-small-24b","qwen3-8b","gemma3-12b")
NAMES=("Mistral 24B","Qwen3 8B","Gemma 12B","Pooled")
CONDS=("I","N","R")
COLORS={"I":"#457b9d","N":"#e09f3e","R":"#a63850"}


def read(path):
    return [json.loads(s) for s in path.read_text().splitlines() if s]


def main():
    ids=[r["id"] for r in read(ROOT/"data/items/g29_selected_v1.jsonl")]
    assert len(ids)==80
    cells={}
    for tag in TAGS:
        a=read(ROOT/f"results/raw/{tag}_g29_revocation_v1.jsonl")
        b=read(ROOT/f"results/raw/{tag}_g29b_irrelevant_v1.jsonl")
        keyed={(r["id"],r["final_role"],r["condition"],r["mode"]):r for r in a+b}
        assert len(keyed)==1600
        cells[tag]={}
        for pid in ids:
            cells[tag][pid]={}
            for cond in CONDS:
                rs=keyed[(pid,"support",cond,"rating")]["value"]
                rr=keyed[(pid,"refute",cond,"rating")]["value"]
                bs=keyed[(pid,"support",cond,"binary")]["choice"]
                br=keyed[(pid,"refute",cond,"binary")]["choice"]
                cells[tag][pid][cond]=(rs-rr,(int(bs=="TRUE")+int(br=="FALSE"))/2)
    rng=random.Random("g29_figure_bootstrap_v1")
    draws=[[rng.choice(ids) for _ in ids] for _ in range(3000)]
    fig,axes=plt.subplots(1,2,figsize=(10.8,4.1),layout="constrained")
    offsets={"I":-.20,"N":0,"R":.20}
    for j,metric in enumerate((0,1)):
        ax=axes[j]
        for cond in CONDS:
            ys,lo,hi=[],[],[]
            for k in range(4):
                tags=TAGS if k==3 else (TAGS[k],)
                values={pid:st.mean(cells[tag][pid][cond][metric] for tag in tags) for pid in ids}
                point=st.mean(values.values())
                boots=sorted(st.mean(values[pid] for pid in draw) for draw in draws)
                ys.append(point)
                lo.append(point-boots[int(.025*len(boots))])
                hi.append(boots[int(.975*len(boots))]-point)
            xs=[k+offsets[cond] for k in range(4)]
            ax.errorbar(xs,ys,yerr=[lo,hi],fmt="o",markersize=6,capsize=2.5,
                        color=COLORS[cond],label={"I":"Irrelevant, excluded","N":"Contradiction, excluded","R":"Contradiction, revoked"}[cond],
                        lw=1.6)
        ax.set_xticks(range(4),NAMES,rotation=18,ha="right")
        ax.grid(axis="y",color="#d5d9dc",alpha=.8,linewidth=.7)
        ax.spines[["top","right"]].set_visible(False)
        if metric==0:
            ax.set_ylabel("E2 support − refute rating (0–100)")
            ax.set_title("Graded evidence separation")
            ax.set_ylim(0,105)
        else:
            ax.set_ylabel("Choice aligned with E2")
            ax.set_title("Direct TRUE/FALSE decision")
            ax.set_ylim(.35,1)
            ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1))
    handles,labels=axes[0].get_legend_handles_labels()
    fig.legend(handles,labels,loc="upper center",ncol=3,bbox_to_anchor=(.5,1.08),frameon=False)
    out=ROOT/"figures"
    out.mkdir(exist_ok=True)
    fig.savefig(out/"g29_status_content_v1.pdf",bbox_inches="tight")
    fig.savefig(out/"g29_status_content_v1.png",dpi=210,bbox_inches="tight")
    print(out/"g29_status_content_v1.pdf")


if __name__=="__main__":main()
