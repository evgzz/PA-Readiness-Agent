"""PA-JSON-1 canonical bytes. Not RFC 8785 or a signature scheme."""
import hashlib
import json
from typing import Any

from .validation import ContractError, MAX_BYTES, _json_value

SERIALIZATION_VERSION = "PA-JSON-1"


def canonical_bytes(value: Any) -> bytes:
    _json_value(value)
    raw = json.dumps(value, sort_keys=True, ensure_ascii=False,
                     allow_nan=False, separators=(",", ":")).encode("utf-8")
    if len(raw) > MAX_BYTES:
        raise ContractError("INPUT_SIZE_OR_TYPE")
    return raw


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def bytes_digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()
