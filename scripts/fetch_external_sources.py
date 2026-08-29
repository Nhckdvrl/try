#!/usr/bin/env python3
"""Fetch the pinned first-wave sources into the ignored raw cache.

Run with the repository's existing environment:
  /home/xiang/miniconda3/envs/fgvd/bin/python scripts/fetch_external_sources.py
"""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import tarfile
import urllib.request


SOURCES = {
    "fantom/fantom.tar.gz": (
        "https://storage.googleapis.com/ai2-mosaic-public/projects/fantom/fantom.tar.gz",
        "1d08dfa0ea474c7f83b9bc7e3a7b466eab25194043489dd618b4c5223e1253a4",
    ),
    "forecastbench/2025-03-02-llm.json": (
        "https://raw.githubusercontent.com/forecastingresearch/forecastbench-datasets/d4834ccc58310539400974fc4664923db7b71417/datasets/question_sets/2025-03-02-llm.json",
        "0ff5ecc9a77890c6b2499ba3a9914d30fad2e30306d2e61d703ad9182d924eab",
    ),
    "forecastbench/2025-03-02_resolution_set.json": (
        "https://raw.githubusercontent.com/forecastingresearch/forecastbench-datasets/d4834ccc58310539400974fc4664923db7b71417/datasets/resolution_sets/2025-03-02_resolution_set.json",
        "8259019c962b58b8179d3550c9577ec882efd13924d939add62f1ea19fe62ac0",
    ),
    "btf3/README.md": (
        "https://huggingface.co/datasets/BTF-2/BTF-3/resolve/4b426627e19cd86202de69a40bc9dadb7f5ccd59/README.md",
        "3ad491f7df03f6b986107a5650899905392539ae95130872196db82783752c34",
    ),
    "btf3/btf3_binary_questions_and_forecasts.parquet": (
        "https://huggingface.co/datasets/BTF-2/BTF-3/resolve/4b426627e19cd86202de69a40bc9dadb7f5ccd59/btf3_binary_questions_and_forecasts.parquet",
        "b28f8fe5634f81afa8e4b37d815f875b6e33c24edf590484f1948efea8db051a",
    ),
    "btf3/btf3_numeric_questions_and_forecasts.parquet": (
        "https://huggingface.co/datasets/BTF-2/BTF-3/resolve/4b426627e19cd86202de69a40bc9dadb7f5ccd59/btf3_numeric_questions_and_forecasts.parquet",
        "1bee10210dabcfcc41d052e7d6458d3674f87b40e1a8f07ab1796fc040ca0747",
    ),
    "aiyer/20189_replication.csv": (
        "https://osf.io/download/hdgsf/",
        "d238fddea76a2aa64af11c9dbc1bde26c2eab8db0b4c366ceebaa9801f00936d",
    ),
    "aiyer/OutcomeBiasAnalysis-v4-Raj.Rmd": (
        "https://osf.io/download/tpabz/",
        "69cb879b96f4f46a7a2a37fed2c7255b42db19d4a207aba490265286c0b25ca6",
    ),
    "aiyer/codebook.xlsx": (
        "https://osf.io/download/rhcmd/",
        "eee40c419b8e63d97435e1d04926c9a22ed8f6df0078361a9ecb5fcddad43bca",
    ),
    "aiyer/outcome_bias.qsf": (
        "https://osf.io/download/u9dbp/",
        "6a7ae91c9e6a583f22a9152228a2492eb34eb7c2691c0c22e501509073e638c4",
    ),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fetch(path: Path, url: str, expected: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and sha256(path) == expected:
        print(f"verified {path}")
        return
    temporary = path.with_suffix(path.suffix + ".partial")
    with urllib.request.urlopen(url) as response, temporary.open("wb") as output:
        while chunk := response.read(1024 * 1024):
            output.write(chunk)
    actual = sha256(temporary)
    if actual != expected:
        temporary.unlink(missing_ok=True)
        raise RuntimeError(f"hash mismatch for {path}: expected {expected}, got {actual}")
    temporary.replace(path)
    print(f"downloaded {path}")


def extract_fantom(root: Path) -> None:
    archive = root / "fantom/fantom.tar.gz"
    target = root / "fantom"
    with tarfile.open(archive) as bundle:
        members = bundle.getmembers()
        for member in members:
            destination = (target / member.name).resolve()
            if target.resolve() not in destination.parents and destination != target.resolve():
                raise RuntimeError(f"unsafe archive member: {member.name}")
        bundle.extractall(target, filter="data")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="data/external/raw")
    args = parser.parse_args()
    root = Path(args.root)
    for relative, (url, expected) in SOURCES.items():
        fetch(root / relative, url, expected)
    extract_fantom(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
