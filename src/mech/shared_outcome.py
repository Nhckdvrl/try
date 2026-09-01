"""Pure construction and analysis helpers for G13 shared-outcome interchange."""
from __future__ import annotations

import hashlib
import random
from dataclasses import dataclass

import numpy as np

LAYERS = (5, 11, 17, 23, 29, 35, 41, 47)
SEED = 20260829


def _key(unit_id: str) -> str:
    return hashlib.sha256(("g13-test|" + unit_id).encode()).hexdigest()


def frozen_split(pairs: list[dict], n_test: int = 64) -> dict[str, list[int]]:
    """Connected test block; train is strictly disjoint in donor identity."""
    donors = [
        {pair[side]["donor_unit_id"] for side in ("yes", "no")}
        for pair in pairs
    ]
    selected = {min(range(len(pairs)), key=lambda i: _key(pairs[i]["independent_unit_id"]))}
    while len(selected) < n_test:
        used = set().union(*(donors[i] for i in selected))
        frontier = [i for i in range(len(pairs)) if i not in selected and donors[i] & used]
        candidates = frontier or [i for i in range(len(pairs)) if i not in selected]
        selected.add(min(candidates, key=lambda i: _key(pairs[i]["independent_unit_id"])))
    test = sorted(selected)
    test_donors = set().union(*(donors[i] for i in test))
    train = [i for i in range(len(pairs)) if i not in selected and not (donors[i] & test_donors)]
    buffer = [i for i in range(len(pairs)) if i not in selected and i not in train]
    return {"train": train, "test": test, "buffer": buffer}


def split_digest(pairs: list[dict], split: dict[str, list[int]]) -> str:
    payload = "\n".join(sorted(pairs[i]["independent_unit_id"] for i in split["test"]))
    return hashlib.sha256(payload.encode()).hexdigest()


def learn_axis(yes: np.ndarray, no: np.ndarray) -> tuple[np.ndarray, float, float]:
    """Mean-difference unit vector and training class projection means."""
    delta = yes.mean(axis=0) - no.mean(axis=0)
    norm = float(np.linalg.norm(delta))
    if not norm:
        raise ValueError("zero mean-difference direction")
    axis = delta / norm
    return axis.astype(np.float32), float((yes @ axis).mean()), float((no @ axis).mean())


def balanced_accuracy(yes: np.ndarray, no: np.ndarray, axis: np.ndarray, ymu: float, nmu: float) -> float:
    threshold = 0.5 * (ymu + nmu)
    sign = 1.0 if ymu >= nmu else -1.0
    tpr = np.mean(sign * (yes @ axis - threshold) > 0)
    tnr = np.mean(sign * (no @ axis - threshold) < 0)
    return float(0.5 * (tpr + tnr))


def orthogonal_axis(axis: np.ndarray, *, layer: int, seed: int = SEED) -> np.ndarray:
    rng = np.random.default_rng(seed + layer)
    out = rng.standard_normal(axis.shape).astype(np.float32)
    out -= float(out @ axis) * axis
    out /= np.linalg.norm(out)
    return out


def bootstrap_mean(values: list[float], *, seed: int = SEED, n: int = 10_000) -> dict:
    rng = random.Random(seed)
    draws = sorted(sum(rng.choice(values) for _ in values) / len(values) for _ in range(n))
    return {"mean": float(np.mean(values)), "ci_low": draws[int(.025*n)],
            "ci_high": draws[int(.975*n)-1], "n": len(values),
            "n_resamples": n, "seed": seed}
