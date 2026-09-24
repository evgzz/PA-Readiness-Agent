"""Strict validators for this package's closed schema vocabulary.

This is not a general JSON Schema implementation. Unknown schema keywords fail
closed. Schemas are trusted package resources, never supplied by an agent.
"""
from __future__ import annotations

import json
import math
import re
from datetime import datetime
from importlib.resources import files
from typing import Any


class ContractError(ValueError):
    """A bounded error code and field path; never includes credential/payload values."""

    def __init__(self, code: str, path: str = "$") -> None:
        self.code, self.path = code, path
        super().__init__(f"{code} at {path}")


MAX_BYTES = 1_048_576
MAX_DEPTH = 64


def _json_value(value: Any, depth: int = 0) -> None:
    if depth > MAX_DEPTH:
        raise ContractError("DEPTH_LIMIT")
    if value is None or type(value) in (bool, str):
        if type(value) is str:
            try:
                value.encode("utf-8")
            except UnicodeError as exc:
                raise ContractError("INVALID_UNICODE") from exc
        return
    if type(value) is int:
        if abs(value) > 2**53 - 1:
            raise ContractError("UNSAFE_INTEGER")
        return
    if type(value) is float:
        if not math.isfinite(value):
            raise ContractError("NONFINITE_NUMBER")
        return
    if type(value) is list:
        for item in value:
            _json_value(item, depth + 1)
        return
    if type(value) is dict:
        for key, item in value.items():
            if type(key) is not str:
                raise ContractError("NONSTRING_KEY")
            _json_value(key, depth + 1)
            _json_value(item, depth + 1)
        return
    raise ContractError("NON_JSON_VALUE")


def load_json(raw: bytes) -> Any:
    if type(raw) is not bytes or len(raw) > MAX_BYTES:
        raise ContractError("INPUT_SIZE_OR_TYPE")

    def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
        out: dict[str, Any] = {}
        for key, val in items:
            if key in out:
                raise ContractError("DUPLICATE_KEY")
            out[key] = val
        return out

    def constant(_: str) -> None:
        raise ContractError("NONFINITE_NUMBER")

    try:
        result = json.loads(raw.decode("utf-8"), object_pairs_hook=pairs,
                            parse_constant=constant)
    except (UnicodeError, json.JSONDecodeError, RecursionError, ValueError) as exc:
        if isinstance(exc, ContractError):
            raise
        raise ContractError("INVALID_JSON") from exc
    _json_value(result)
    return result


def resource(name: str) -> dict[str, Any]:
    if not re.fullmatch(r"[a-z0-9._-]+", name):
        raise ContractError("UNKNOWN_CONTRACT")
    try:
        return load_json(files("pa_contracts").joinpath("resources", name + ".json").read_bytes())
    except FileNotFoundError as exc:
        raise ContractError("UNKNOWN_CONTRACT") from exc


KEYWORDS = frozenset({"$schema", "title", "description", "type", "const", "enum",
    "properties", "required", "additionalProperties", "items", "uniqueItems",
    "minItems", "minLength", "maxLength", "minimum", "maximum", "exclusiveMinimum",
    "exclusiveMaximum", "pattern", "format", "allOf", "if", "then", "anyOf"})


def _equal(a: Any, b: Any) -> bool:
    # JSON Schema distinguishes booleans from numbers, while Python does not.
    return type(a) is type(b) and a == b


def _check_rule(rule: dict[str, Any]) -> None:
    """Check the complete vocabulary, including branches not taken by this value."""
    if not isinstance(rule, dict) or set(rule) - KEYWORDS:
        raise ContractError("UNSUPPORTED_SCHEMA_KEYWORD")
    for child in rule.get("properties", {}).values():
        _check_rule(child)
    for key in ("items", "if", "then"):
        if key in rule:
            _check_rule(rule[key])
    for key in ("anyOf", "allOf"):
        for child in rule.get(key, []):
            _check_rule(child)


def _check(value: Any, rule: dict[str, Any], path: str) -> None:
    if set(rule) - KEYWORDS:
        raise ContractError("UNSUPPORTED_SCHEMA_KEYWORD", path)
    types = {"null": lambda x: x is None, "boolean": lambda x: type(x) is bool,
             "integer": lambda x: type(x) is int,
             "number": lambda x: type(x) in (int, float),
             "string": lambda x: type(x) is str, "array": lambda x: type(x) is list,
             "object": lambda x: type(x) is dict}
    if "type" in rule:
        names = rule["type"] if isinstance(rule["type"], list) else [rule["type"]]
        if any(name not in types for name in names):
            raise ContractError("UNSUPPORTED_SCHEMA_TYPE", path)
        if not any(types[name](value) for name in names):
            raise ContractError("TYPE", path)
    if "const" in rule and not _equal(value, rule["const"]):
        raise ContractError("CONST", path)
    if "enum" in rule and not any(_equal(value, x) for x in rule["enum"]):
        raise ContractError("ENUM", path)
    if "anyOf" in rule:
        for branch in rule["anyOf"]:
            try:
                _check(value, branch, path)
                break
            except ContractError as exc:
                if exc.code.startswith("UNSUPPORTED_"):
                    raise
        else:
            raise ContractError("ANY_OF", path)
    for branch in rule.get("allOf", []):
        _check(value, branch, path)
    if "if" in rule:
        try:
            _check(value, rule["if"], path)
        except ContractError as exc:
            if exc.code.startswith("UNSUPPORTED_"):
                raise
        else:
            if "then" in rule:
                _check(value, rule["then"], path)
    if type(value) is dict:
        props = rule.get("properties", {})
        if set(rule.get("required", [])) - set(value):
            raise ContractError("MISSING_FIELD", path)
        if rule.get("additionalProperties") is False and set(value) - set(props):
            raise ContractError("UNKNOWN_FIELD", path)
        for key in value.keys() & props.keys():
            _check(value[key], props[key], path + "." + key)
    if type(value) is list:
        if len(value) < rule.get("minItems", 0):
            raise ContractError("MIN_ITEMS", path)
        if rule.get("uniqueItems"):
            serialized = [json.dumps(x, sort_keys=True, ensure_ascii=True, separators=(",", ":")) for x in value]
            if len(set(serialized)) != len(value):
                raise ContractError("DUPLICATE_ITEM", path)
        if "items" in rule:
            for i, item in enumerate(value):
                _check(item, rule["items"], f"{path}[{i}]")
    if type(value) is str:
        if len(value) < rule.get("minLength", 0) or len(value) > rule.get("maxLength", MAX_BYTES):
            raise ContractError("STRING_LENGTH", path)
        if "pattern" in rule and re.search(rule["pattern"], value) is None:
            raise ContractError("PATTERN", path)
        if "format" in rule:
            if rule["format"] != "date-time":
                raise ContractError("UNSUPPORTED_FORMAT", path)
            try:
                if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})", value):
                    raise ValueError
                parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
                if parsed.utcoffset() is None:
                    raise ValueError
            except ValueError as exc:
                raise ContractError("DATE_TIME", path) from exc
    if type(value) in (int, float):
        for key, fail in (("minimum", lambda n: value < n), ("maximum", lambda n: value > n),
                          ("exclusiveMinimum", lambda n: value <= n), ("exclusiveMaximum", lambda n: value >= n)):
            if key in rule and fail(rule[key]):
                raise ContractError("NUMBER_BOUND", path)


def validate(value: Any, contract: str) -> dict[str, Any]:
    _json_value(value)
    rule = resource(contract)
    _check_rule(rule)
    _check(value, rule, "$")
    # Detach caller-owned containers; callers cannot mutate validated snapshots.
    return json.loads(json.dumps(value, allow_nan=False))


def validate_schema(value: Any, rule: dict[str, Any]) -> None:
    """For trusted tool-specific schemas using the same limited vocabulary."""
    _json_value(value)
    _check_rule(rule)
    _check(value, rule, "$")
