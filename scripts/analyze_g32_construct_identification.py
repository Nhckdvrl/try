"""Registered claim-paired G32 summaries. Run only on complete raw model files."""

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
ITEMS = ROOT / "data/items/g32_selected_v1.jsonl"
MODELS = ("qwen3-8b", "gemma3-12b", "mistral-small-24b")
CONTRACTS = ("open_world", "record_only")
E = ("support", "refute")
CELLS = ("B", "F_D", "F_S", "D+", "D-", "S+", "S-", "A+", "A-")


def mean_ci(x, seed):
    z = np.asarray(x, dtype=float)
    z = z[np.isfinite(z)]
    if not len(z):
        return {"n": 0, "mean": None, "ci95": [None, None]}
    rng = np.random.default_rng(seed)
    ind = rng.integers(0, len(z), size=(5000, len(z)))
    boot = z[ind].mean(axis=1)
    return {"n": int(len(z)), "mean": float(z.mean()),
            "ci95": [float(v) for v in np.quantile(boot, [.025, .975])]}


def metrics(v):
    """One claim/contract/model; both E arms are required for paired metrics."""
    m = {}
    avg = lambda cell: (v[("support", cell)] + v[("refute", cell)]) / 2
    m["x_direct_signed"] = avg("D+") - avg("D-")
    m["x_direct_abs"] = np.mean([abs(v[(e, "D+")] - v[(e, "D-")]) for e in E])
    m["x_sim_signed"] = avg("S+") - avg("S-")
    m["x_sim_abs"] = np.mean([abs(v[(e, "S+")] - v[(e, "S-")]) for e in E])
    m["x_active_signed"] = avg("A+") - avg("A-")
    m["x_active_abs"] = np.mean([abs(v[(e, "A+")] - v[(e, "A-")]) for e in E])
    m["direct_center_vs_frame"] = (avg("D+") + avg("D-")) / 2 - avg("F_D")
    m["sim_center_vs_frame"] = (avg("S+") + avg("S-")) / 2 - avg("F_S")
    m["direct_arm_mae_vs_frame"] = np.mean([abs(v[(e, c)] - v[(e, "F_D")]) for e in E for c in ("D+", "D-")])
    m["sim_arm_mae_vs_frame"] = np.mean([abs(v[(e, c)] - v[(e, "F_S")]) for e in E for c in ("S+", "S-")])
    m["query_shift_Q"] = avg("F_S") - avg("F_D")
    m["query_shift_Q_abs"] = np.mean([abs(v[(e, "F_S")] - v[(e, "F_D")]) for e in E])
    m["direct_frame_shift"] = avg("F_D") - avg("B")
    m["direct_frame_shift_abs"] = np.mean([abs(v[(e, "F_D")] - v[(e, "B")]) for e in E])
    m["sim_frame_to_B"] = avg("F_S") - avg("B")
    m["sim_frame_to_B_abs"] = np.mean([abs(v[(e, "F_S")] - v[(e, "B")]) for e in E])
    m["direct_to_B_abs"] = np.mean([abs(v[(e, c)] - v[(e, "B")]) for e in E for c in ("D+", "D-")])
    m["sim_to_B_abs"] = np.mean([abs(v[(e, c)] - v[(e, "B")]) for e in E for c in ("S+", "S-")])
    for c in CELLS:
        m["E_leverage_" + c] = v[("support", c)] - v[("refute", c)]
    m["E_leverage_direct_vs_frame"] = (m["E_leverage_D+"] + m["E_leverage_D-"]) / 2 - m["E_leverage_F_D"]
    m["E_leverage_sim_vs_frame"] = (m["E_leverage_S+"] + m["E_leverage_S-"]) / 2 - m["E_leverage_F_S"]
    m["E_leverage_frame_vs_B"] = m["E_leverage_F_D"] - m["E_leverage_B"]
    return m


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="results/g32/g32_construct_identification_v1.json")
    args = ap.parse_args()
    raw_items = ITEMS.read_bytes()
    item_ids = [json.loads(s)["id"] for s in raw_items.splitlines() if s]
    selected_sha = hashlib.sha256(raw_items).hexdigest()
    out = {"selected_sha256": selected_sha, "models": {}, "comparisons": {},
           "limitations": "Exploratory; G31/G29 material reuse; constructed X; numeric-heavy claims."}
    by_model = {}
    for tag in MODELS:
        path = ROOT / f"results/raw/{tag}_g32_construct_identification_v1.jsonl"
        rows = [json.loads(s) for s in path.read_text().splitlines() if s]
        assert len(rows) == len(item_ids) * len(CONTRACTS) * len(E) * len(CELLS), (tag, len(rows))
        assert all(r["items_sha256"] == selected_sha for r in rows)
        lookup = {(r["id"], r["contract"], r["e_role"], r["cell"]): r["value"] for r in rows}
        assert len(lookup) == len(rows)
        fail = sum(r["value"] is None for r in rows)
        out["models"][tag] = {"n_rows": len(rows), "parse_failures": fail,
                              "raw_sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "contracts": {}}
        by_model[tag] = {}
        for contract in CONTRACTS:
            claim_metrics = {}
            for item in item_ids:
                values = {(e, c): lookup[(item, contract, e, c)] for e in E for c in CELLS}
                if any(v is None for v in values.values()):
                    continue
                claim_metrics[item] = metrics(values)
            out["models"][tag]["contracts"][contract] = {
                "complete_claims": len(claim_metrics),
                "metrics": {k: mean_ci([v[k] for v in claim_metrics.values()], 3200 + j)
                            for j, k in enumerate(next(iter(claim_metrics.values())).keys())}
                if claim_metrics else {},
            }
            by_model[tag][contract] = claim_metrics
        common = set(by_model[tag]["open_world"]) & set(by_model[tag]["record_only"])
        out["comparisons"][tag] = {
            k: mean_ci([by_model[tag]["record_only"][i][k] - by_model[tag]["open_world"][i][k]
                        for i in sorted(common)], 4200+j)
            for j, k in enumerate(("x_direct_abs", "x_sim_abs", "query_shift_Q_abs",
                                   "direct_frame_shift_abs", "E_leverage_direct_vs_frame",
                                   "E_leverage_frame_vs_B", "direct_to_B_abs", "sim_to_B_abs"))
        }
    target = ROOT / args.out
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(target)


if __name__ == "__main__":
    main()
