"""Runtime owns one loop; injected gateways retain execution authority.

These interfaces do not authenticate a caller or create a runtime sandbox.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Mapping, Protocol

from .ports import AnswerProposal, ModelRequest, ModelResponse, ToolProposal
from .validation import ContractError, validate, validate_schema


@dataclass(frozen=True)
class RuntimeResult:
    answer: AnswerProposal | None
    terminal_status: str
    evidence_refs: tuple[str, ...]


class MeteredModelGateway(Protocol):
    def infer(self, request: ModelRequest) -> ModelResponse: ...


class AuthorizedToolGateway(Protocol):
    def dispatch(self, proposal: ToolProposal) -> Mapping[str, object]: ...


@dataclass(frozen=True)
class RuntimeGateways:
    model: MeteredModelGateway
    tools: AuthorizedToolGateway


class RuntimePort(Protocol):
    def run(self, runtime_input: Mapping[str, object],
            gateways: RuntimeGateways) -> RuntimeResult: ...


def runtime_input(value: object) -> dict:
    """Allowlisted current-case view, never a full eval recipe or oracle record."""
    record = validate(value, "runtime-input")
    for evidence in record["evidence"]:
        if evidence["case_id"] != record["case_id"]:
            raise ContractError("FOREIGN_CASE")
    return record


def tool_proposal(value: object, tool_schemas: Mapping[str, dict]) -> ToolProposal:
    record = validate(value, "tool-proposal-v1")
    if record["tool_name"] not in tool_schemas:
        raise ContractError("UNKNOWN_TOOL")
    schema = tool_schemas[record["tool_name"]]
    if schema.get("type") != "object" or schema.get("additionalProperties") is not False:
        raise ContractError("OPEN_TOOL_ARGUMENT_SCHEMA")
    validate_schema(record["arguments"], schema)
    return ToolProposal(record["tool_name"], record["arguments"])


def answer_proposal(value: object) -> dict:
    record = validate(value, "readiness-answer-v1")
    if record["readiness"] == "READY" and (record["blockers"] or record["unresolved_checks"]):
        raise ContractError("READY_WITH_UNRESOLVED_REQUIREMENTS")
    if record["readiness"] == "NOT_READY" and not record["blockers"]:
        raise ContractError("MISSING_BLOCKER")
    if record["readiness"] == "UNKNOWN" and (record["blockers"] or not record["unresolved_checks"]):
        raise ContractError("INVALID_UNKNOWN")
    if record["readiness"] == "READY" and not record["evidence_refs"]:
        raise ContractError("MISSING_READY_EVIDENCE")
    return record
