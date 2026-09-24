"""Draft interfaces. Runtime validation/authentication are not implemented here."""
from dataclasses import dataclass
from enum import Enum
from typing import Mapping, Protocol, Sequence


class Readiness(str, Enum):
    READY = "READY"
    NOT_READY = "NOT_READY"
    UNKNOWN = "UNKNOWN"


class EvalOutcome(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    UNRESOLVED = "UNRESOLVED"


class ReleaseOutcome(str, Enum):
    GO = "GO"
    NO_GO = "NO_GO"
    INCONCLUSIVE = "INCONCLUSIVE"


@dataclass(frozen=True)
class Observation:
    session_id: str
    case_id: str
    evidence: Sequence[Mapping[str, object]]
    available_tools: Sequence[str]


@dataclass(frozen=True)
class ToolProposal:
    tool_name: str
    arguments: Mapping[str, object]


@dataclass(frozen=True)
class AnswerProposal:
    readiness: Readiness
    evidence_refs: Sequence[str]
    unresolved_checks: Sequence[str]
    explanation: str


@dataclass(frozen=True)
class ModelRequest:
    messages: Sequence[Mapping[str, str]]
    tool_schemas: Sequence[Mapping[str, object]]


@dataclass(frozen=True)
class ModelResponse:
    content: Mapping[str, object]
    usage: Mapping[str, object]
    model_identity: Mapping[str, object]


@dataclass(frozen=True)
class TrustedScope:
    # Created by authenticated gateway code, never deserialized from agent arguments.
    actor_id: str
    tenant_id: str
    patient_id: str
    request_id: str
    allowed_operations: Sequence[str]


class AgentPort(Protocol):
    def build_request(self, observation: Observation) -> ModelRequest: ...
    def propose(self, observation: Observation, response: ModelResponse) -> ToolProposal | AnswerProposal: ...


class ModelPort(Protocol):
    def infer(self, request: ModelRequest) -> ModelResponse: ...


class ToolPort(Protocol):
    def execute(self, scope: TrustedScope, proposal: ToolProposal) -> Mapping[str, object]: ...


class TraceSink(Protocol):
    def append(self, event: Mapping[str, object]) -> None: ...


class SystemUnderTest(Protocol):
    def reset(self, input_snapshot: Mapping[str, object], initial_state: Mapping[str, object]) -> str: ...
    def run(self, reset_receipt: str) -> Mapping[str, object]: ...
