"""Source-native schema for external information-set benchmarks.

Unlike :mod:`schema`, this module deliberately has no universal prompt compiler
and no admit/exclude rule fields.  An adapter preserves each source's native
task representation and records only the paired intervention plus provenance.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
import hashlib
import json
from pathlib import Path
import re
from typing import Any, Iterable, Mapping


class BoundaryType(str, Enum):
    PERSPECTIVE = "perspective"
    TEMPORAL = "temporal"
    PROCEDURAL = "procedural"
    ROLE_ACCESS = "role_access"
    DECISION_SCOPE = "decision_scope"
    INVALIDITY_CONTRAST = "invalidity_contrast"


REQUIRED_PROVENANCE = {
    "source_url",
    "source_revision",
    "source_file",
    "source_file_sha256",
    "source_record_id",
    "reuse_status",
}
FORBIDDEN_COMPILER_KEYS = {"admit_rule", "exclude_rule"}
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_TRANSFORMATION_ID = re.compile(r"^[a-z0-9][a-z0-9._-]*$")


@dataclass(frozen=True)
class InformationSetItem:
    source_id: str
    independent_unit_id: str
    boundary_type: str
    reference_context: dict[str, Any]
    oob_variant: dict[str, Any]
    admissible_variant: dict[str, Any]
    provenance: dict[str, Any]
    transformation_id: str

    @property
    def record_id(self) -> str:
        return f"{self.source_id}:{self.independent_unit_id}:{self.transformation_id}"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, sort_keys=True)

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> "InformationSetItem":
        expected = set(cls.__dataclass_fields__)
        missing = expected - set(value)
        extra = set(value) - expected
        if missing or extra:
            raise ValueError(f"schema keys mismatch; missing={sorted(missing)}, extra={sorted(extra)}")
        item = cls(**dict(value))
        validate_item(item)
        return item


def file_sha256(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _walk_keys(value: Any) -> Iterable[str]:
    if isinstance(value, Mapping):
        for key, nested in value.items():
            yield str(key)
            yield from _walk_keys(nested)
    elif isinstance(value, list):
        for nested in value:
            yield from _walk_keys(nested)


def validate_item(item: InformationSetItem) -> None:
    for name in ("source_id", "independent_unit_id", "transformation_id"):
        value = getattr(item, name)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{name} must be a non-empty string")
    if item.boundary_type not in {b.value for b in BoundaryType}:
        raise ValueError(f"unknown boundary_type: {item.boundary_type}")
    if not _TRANSFORMATION_ID.fullmatch(item.transformation_id):
        raise ValueError("transformation_id must be a stable lowercase identifier")

    for name in ("reference_context", "oob_variant", "admissible_variant", "provenance"):
        value = getattr(item, name)
        if not isinstance(value, dict) or not value:
            raise ValueError(f"{name} must be a non-empty object")
    if item.oob_variant == item.admissible_variant:
        raise ValueError("oob_variant and admissible_variant must differ")

    all_keys = set(_walk_keys(item.to_dict()))
    leaked = all_keys & FORBIDDEN_COMPILER_KEYS
    if leaked:
        raise ValueError(f"universal compiler fields are forbidden: {sorted(leaked)}")

    missing_provenance = REQUIRED_PROVENANCE - set(item.provenance)
    if missing_provenance:
        raise ValueError(f"missing provenance keys: {sorted(missing_provenance)}")
    sha = item.provenance["source_file_sha256"]
    if not isinstance(sha, str) or not _SHA256.fullmatch(sha):
        raise ValueError("provenance.source_file_sha256 must be a lowercase SHA-256")
    for key in REQUIRED_PROVENANCE - {"source_file_sha256"}:
        value = item.provenance[key]
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"provenance.{key} must be a non-empty string")


def validate_collection(items: Iterable[InformationSetItem]) -> dict[str, Any]:
    records = list(items)
    if not records:
        raise ValueError("collection is empty")
    seen: set[str] = set()
    for item in records:
        validate_item(item)
        if item.record_id in seen:
            raise ValueError(f"duplicate record_id: {item.record_id}")
        seen.add(item.record_id)
    units = {(item.source_id, item.independent_unit_id) for item in records}
    return {
        "n_records": len(records),
        "n_independent_units": len(units),
        "n_sources": len({item.source_id for item in records}),
        "boundary_types": sorted({item.boundary_type for item in records}),
    }


def load_jsonl(path: str | Path) -> list[InformationSetItem]:
    result = []
    with Path(path).open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                result.append(InformationSetItem.from_dict(json.loads(line)))
            except (TypeError, ValueError, json.JSONDecodeError) as exc:
                raise ValueError(f"{path}:{line_number}: {exc}") from exc
    validate_collection(result)
    return result
