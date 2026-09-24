# ADR 009: Declare the full self-hosted observability dependency set

Status: PROPOSED | Date: 2026-09-24 | Implementation evidence: NOT_RUN
Accountable decision owner: UNASSIGNED.

## Context
Selecting ClickHouse alone does not specify a Langfuse deployment.

## Proposed decision
Record platform PostgreSQL, ClickHouse, Redis/Valkey, object storage and application services for the chosen Langfuse version; keep application-state ownership separate.

## Alternatives considered
Managed Langfuse or a different platform, evaluated against deployment/data requirements.

## Consequences and limitations
Operational overhead and version-specific compatibility; no deployment manifest or versions are selected by this draft.

## Acceptance evidence required
Pin the actual deployment manifest and verify ingestion, recovery, access and data destinations.

## Revisit trigger
Revisit when acceptance fails, intended-use or deployment requirements change,
or a pinned dependency changes materially. Record the superseding ADR and rerun
affected qualification; do not silently change the baseline.

References: [source register](../SOURCES.md), [system specification](../../SPEC.md).
