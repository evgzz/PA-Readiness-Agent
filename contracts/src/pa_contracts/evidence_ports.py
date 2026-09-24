"""Ports separate producer authentication, durable evidence, metrics and gates."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Mapping, Protocol


@dataclass(frozen=True)
class IngressIdentity:
    principal_id: str
    producer: str
    producer_instance: str
    channels: frozenset[str]
    evidence_classes: frozenset[str]
    actor_ids: frozenset[str] = frozenset()


class Authenticator(Protocol):
    def authenticate(self, credential: object) -> IngressIdentity: ...


@dataclass(frozen=True)
class ValidatedEvent:
    """Immutable original bytes, not a mutable dict passed to a writer later."""
    envelope_bytes: bytes
    payload_bytes: bytes
    principal_id: str


class EvidenceWriter(Protocol):
    def append(self, event: ValidatedEvent) -> str: ...


class MetricSnapshotPort(Protocol):
    def read(self, snapshot_digest: str) -> Mapping[str, object]: ...


class GatePort(Protocol):
    def evaluate(self, candidate_digest: str, evidence_snapshot_digest: str,
                 policy_digest: str) -> Mapping[str, object]: ...
