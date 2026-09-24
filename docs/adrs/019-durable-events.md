# ADR 019: Separate durable evidence from telemetry delivery

Status: PROPOSED | Date: 2026-09-24 | Implementation evidence: NOT_RUN
Accountable decision owner: UNASSIGNED.

## Context
A successful state update and a failed event export can otherwise disagree.

## Proposed decision
Local finalized artifacts for synthetic development; transactional state/outbox for durable runtime, idempotent consumers, protected versioned evidence store.

## Alternatives considered
Best-effort logging only, or attempt to make an external effect atomic with telemetry export.

## Consequences and limitations
Duplicate/reordered delivery and reconciliation remain necessary. An outbox alone does not prove exactly-once external effects.

## Acceptance evidence required
Crash windows, duplicate collisions, sequence gaps, delayed export, replay and loss of required persistence.

## Revisit trigger
Revisit when acceptance fails, intended-use or deployment requirements change,
or a pinned dependency changes materially. Record the superseding ADR and rerun
affected qualification; do not silently change the baseline.

References: [source register](../SOURCES.md), [system specification](../../SPEC.md).
