"""Analyze CK-P1 outputs with skeleton-clustered uncertainty.

Expected raw JSONL:
- one metadata row: record_type=metadata, model_tag, artifact_sha256
- decision rows: record_type=decision, context_id, depth, text
- qualification rows: record_type=qualification, context_id, text

Gold is read only from the frozen material artifact. No automatic headline/go
decision is encoded because CK-P1 is discovery.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path
import random
import statistics as st

SEED = 20260906
N_RESAMPLES = 10_000
STRUCTURES = ("K1", "K2", "K3", "CK")
DEPTHS = (1, 2, 3, 4, 6)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_bool(text: object) -> str | None:
    if not isinstance(text, str):
        return None
    value = text.strip().upper()
    return value if value in {"TRUE", "FALSE"} else None


def load_artifact(path: Path) -> dict[str, dict]:
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    by_id = {row["context_id"]: row for row in rows}
    if len(rows) != 96 or len(by_id) != 96:
        raise ValueError("CK-P1 artifact must contain exactly 96 unique contexts")
    return by_id


def load_raw(path: Path) -> tuple[dict, list[dict]]:
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    metadata = [row for row in rows if row.get("record_type") == "metadata"]
    if len(metadata) != 1:
        raise ValueError(f"{path}: expected exactly one metadata row")
    return metadata[0], [row for row in rows if row.get("record_type") != "metadata"]


def clustered_summary(values: dict[str, list[float]], *, seed: int = SEED) -> dict:
    if not values:
        return {"n_clusters": 0, "n": 0, "mean": None, "ci_low": None, "ci_high": None}
    keys = sorted(values)
    cluster_means = {key: st.fmean(values[key]) for key in keys}
    rng = random.Random(seed)
    draws = []
    for _ in range(N_RESAMPLES):
        draws.append(st.fmean(cluster_means[keys[rng.randrange(len(keys))]] for _ in keys))
    draws.sort()
    return {
        "n_clusters": len(keys),
        "n": sum(len(v) for v in values.values()),
        "mean": st.fmean(cluster_means.values()),
        "ci_low": draws[int(0.025 * N_RESAMPLES)],
        "ci_high": draws[min(N_RESAMPLES - 1, int(0.975 * N_RESAMPLES))],
        "n_resamples": N_RESAMPLES,
        "seed": seed,
    }


def scalar_cluster_summary(values: dict[str, float]) -> dict:
    return clustered_summary({key: [value] for key, value in values.items()})


def analyze_one(artifact: dict[str, dict], raw_path: Path, artifact_sha256: str) -> dict:
    metadata, records = load_raw(raw_path)
    if metadata.get("artifact_sha256") != artifact_sha256:
        raise ValueError(f"{raw_path}: artifact hash does not match frozen CK-P1 material")
    model_tag = metadata.get("model_tag")
    if not isinstance(model_tag, str) or not model_tag:
        raise ValueError(f"{raw_path}: missing model_tag")

    decisions = {}
    qualifications = {}
    for row in records:
        context_id = row.get("context_id")
        if context_id not in artifact:
            raise ValueError(f"{raw_path}: unknown context_id {context_id!r}")
        if row.get("record_type") == "decision":
            key = (context_id, int(row["depth"]))
            if key in decisions:
                raise ValueError(f"{raw_path}: duplicate decision {key}")
            decisions[key] = row
        elif row.get("record_type") == "qualification":
            if context_id in qualifications:
                raise ValueError(f"{raw_path}: duplicate qualification {context_id}")
            qualifications[context_id] = row
        else:
            raise ValueError(f"{raw_path}: unknown record_type {row.get('record_type')!r}")

    expected = {
        (context_id, int(query["depth"]))
        for context_id, context in artifact.items()
        for query in context["queries"]
    }
    if set(decisions) != expected:
        missing = sorted(expected - set(decisions))[:10]
        extra = sorted(set(decisions) - expected)[:10]
        raise ValueError(f"{raw_path}: decision coverage mismatch missing={missing} extra={extra}")
    if set(qualifications) != set(artifact):
        raise ValueError(f"{raw_path}: qualification coverage mismatch")

    cell_acc = defaultdict(lambda: defaultdict(list))
    cell_true = defaultdict(lambda: defaultdict(list))
    cell_ptrue = defaultdict(lambda: defaultdict(list))
    qual_acc = defaultdict(lambda: defaultdict(list))
    parsed_decisions = 0
    parsed_qualifications = 0
    per_skeleton = defaultdict(lambda: {
        "ck_deep_true": [], "k3_beyond_true": [],
        "finite_beyond_true": [], "finite_licensed_accuracy": [],
    })

    for context_id, context in artifact.items():
        sid = context["skeleton_id"]
        structure = context["structure"]
        query_gold = {int(q["depth"]): q["gold"] for q in context["queries"]}

        for depth in DEPTHS:
            raw = decisions[(context_id, depth)]
            answer = parse_bool(raw.get("text"))
            if answer is None:
                continue
            parsed_decisions += 1
            correct = float(answer == query_gold[depth])
            true_value = float(answer == "TRUE")
            cell_acc[(structure, depth)][sid].append(correct)
            cell_true[(structure, depth)][sid].append(true_value)

            p_true = raw.get("p_true")
            if isinstance(p_true, (int, float)) and 0 <= float(p_true) <= 1:
                cell_ptrue[(structure, depth)][sid].append(float(p_true))

            if structure == "CK" and depth in {4, 6}:
                per_skeleton[sid]["ck_deep_true"].append(true_value)
            if structure == "K3" and depth in {4, 6}:
                per_skeleton[sid]["k3_beyond_true"].append(true_value)
            if structure in {"K1", "K2", "K3"} and query_gold[depth] == "FALSE":
                per_skeleton[sid]["finite_beyond_true"].append(true_value)
            if structure in {"K1", "K2", "K3"} and query_gold[depth] == "TRUE":
                per_skeleton[sid]["finite_licensed_accuracy"].append(correct)

        qanswer = parse_bool(qualifications[context_id].get("text"))
        if qanswer is not None:
            parsed_qualifications += 1
            qual_acc[structure][sid].append(float(qanswer == context["qualification"]["gold"]))

    cells = {}
    for structure in STRUCTURES:
        cells[structure] = {}
        for depth in DEPTHS:
            key = (structure, depth)
            cells[structure][str(depth)] = {
                "accuracy": clustered_summary(cell_acc[key]),
                "true_rate": clustered_summary(cell_true[key]),
                "p_true": clustered_summary(cell_ptrue[key]) if cell_ptrue[key] else None,
            }

    finite_beyond = {
        sid: st.fmean(v["finite_beyond_true"]) for sid, v in per_skeleton.items()
        if v["finite_beyond_true"]
    }
    finite_licensed = {
        sid: st.fmean(v["finite_licensed_accuracy"]) for sid, v in per_skeleton.items()
        if v["finite_licensed_accuracy"]
    }
    ck_deep = {
        sid: st.fmean(v["ck_deep_true"]) for sid, v in per_skeleton.items()
        if v["ck_deep_true"]
    }
    k3_beyond = {
        sid: st.fmean(v["k3_beyond_true"]) for sid, v in per_skeleton.items()
        if v["k3_beyond_true"]
    }
    shared = sorted(set(ck_deep) & set(k3_beyond))
    ck_minus_k3 = {sid: ck_deep[sid] - k3_beyond[sid] for sid in shared}

    return {
        "model_tag": model_tag,
        "artifact_sha256": artifact_sha256,
        "parse": {
            "decisions": parsed_decisions / len(expected),
            "qualifications": parsed_qualifications / len(artifact),
            "n_decisions": len(expected),
            "n_qualifications": len(artifact),
        },
        "qualification": {
            structure: clustered_summary(qual_acc[structure]) for structure in STRUCTURES
        },
        "cells": cells,
        "discovery_summaries": {
            "finite_beyond_boundary_true_rate": scalar_cluster_summary(finite_beyond),
            "finite_licensed_accuracy": scalar_cluster_summary(finite_licensed),
            "ck_deep_true_rate_d4_d6": scalar_cluster_summary(ck_deep),
            "k3_beyond_boundary_true_rate_d4_d6": scalar_cluster_summary(k3_beyond),
            "ck_minus_k3_deep_true_rate": scalar_cluster_summary(ck_minus_k3),
        },
        "note": "Discovery summaries are descriptive; no automatic headline/go decision is encoded.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact", type=Path, required=True)
    parser.add_argument("--raw", nargs="+", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    artifact_sha256 = sha256_file(args.artifact)
    artifact = load_artifact(args.artifact)
    results = [analyze_one(artifact, path, artifact_sha256) for path in args.raw]
    report = {
        "experiment": "CK-P1",
        "artifact": str(args.artifact),
        "artifact_sha256": artifact_sha256,
        "bootstrap": {"seed": SEED, "n_resamples": N_RESAMPLES, "cluster": "skeleton_id"},
        "models": results,
        "panel_complete": len({row["model_tag"] for row in results}) == 3,
        "warning": "Any observed law requires a fresh post-result novelty audit before C1.",
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
