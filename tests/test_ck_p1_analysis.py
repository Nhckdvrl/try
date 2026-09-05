from __future__ import annotations
import hashlib
import json
from pathlib import Path
import pytest
import analyze_ck_p1 as ck
from ck_p1_materials import build_contexts, write_jsonl

def _artifact(tmp_path: Path):
    path = tmp_path / "ck.jsonl"
    write_jsonl(path)
    return path, hashlib.sha256(path.read_bytes()).hexdigest(), build_contexts()

def _write_raw(path: Path, *, model_tag: str, artifact_sha: str, rows: list[dict], mode: str = "perfect"):
    with path.open("w", encoding="utf-8") as handle:
        handle.write(json.dumps({"record_type":"metadata","model_tag":model_tag,"artifact_sha256":artifact_sha}) + "\n")
        for context in rows:
            for query in context["queries"]:
                answer = "TRUE" if mode == "always_true" else query["gold"]
                handle.write(json.dumps({"record_type":"decision","context_id":context["context_id"],"depth":query["depth"],"text":answer}) + "\n")
            handle.write(json.dumps({"record_type":"qualification","context_id":context["context_id"],"text":context["qualification"]["gold"]}) + "\n")

def test_parser_is_fail_closed():
    assert ck.parse_bool("TRUE") == "TRUE"
    assert ck.parse_bool(" false \n") == "FALSE"
    assert ck.parse_bool("TRUE because...") is None
    assert ck.parse_bool("") is None
    assert ck.parse_bool(None) is None

def test_perfect_outputs_recover_full_ck_vs_k3_separation(tmp_path):
    artifact_path, artifact_sha, rows = _artifact(tmp_path)
    raw = tmp_path / "perfect.jsonl"
    _write_raw(raw, model_tag="perfect", artifact_sha=artifact_sha, rows=rows)
    report = ck.analyze_one(ck.load_artifact(artifact_path), raw, artifact_sha)
    assert report["parse"]["decisions"] == 1.0
    assert report["parse"]["qualifications"] == 1.0
    assert report["discovery_summaries"]["finite_beyond_boundary_true_rate"]["mean"] == 0.0
    assert report["discovery_summaries"]["ck_deep_true_rate_d4_d6"]["mean"] == 1.0
    assert report["discovery_summaries"]["ck_minus_k3_deep_true_rate"]["mean"] == 1.0

def test_always_true_model_is_detected_as_finite_overclosure(tmp_path):
    artifact_path, artifact_sha, rows = _artifact(tmp_path)
    raw = tmp_path / "always_true.jsonl"
    _write_raw(raw, model_tag="always-true", artifact_sha=artifact_sha, rows=rows, mode="always_true")
    report = ck.analyze_one(ck.load_artifact(artifact_path), raw, artifact_sha)
    assert report["discovery_summaries"]["finite_beyond_boundary_true_rate"]["mean"] == 1.0
    assert report["discovery_summaries"]["ck_minus_k3_deep_true_rate"]["mean"] == 0.0

def test_artifact_hash_mismatch_fails(tmp_path):
    artifact_path, artifact_sha, rows = _artifact(tmp_path)
    raw = tmp_path / "bad.jsonl"
    _write_raw(raw, model_tag="bad", artifact_sha="0"*64, rows=rows)
    with pytest.raises(ValueError, match="artifact hash"):
        ck.analyze_one(ck.load_artifact(artifact_path), raw, artifact_sha)

def test_missing_decision_fails_coverage_check(tmp_path):
    artifact_path, artifact_sha, rows = _artifact(tmp_path)
    raw = tmp_path / "missing.jsonl"
    _write_raw(raw, model_tag="missing", artifact_sha=artifact_sha, rows=rows)
    parsed = [json.loads(line) for line in raw.read_text(encoding="utf-8").splitlines()]
    kept, removed = [], False
    for row in parsed:
        if not removed and row.get("record_type") == "decision":
            removed = True
            continue
        kept.append(row)
    raw.write_text("\n".join(json.dumps(row) for row in kept) + "\n", encoding="utf-8")
    with pytest.raises(ValueError, match="coverage mismatch"):
        ck.analyze_one(ck.load_artifact(artifact_path), raw, artifact_sha)
