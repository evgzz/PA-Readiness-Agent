# ADR 008: Use PostgreSQL for the durable application profile

Status: PROPOSED | Date: 2026-09-24 | Implementation evidence: NOT_RUN
Accountable decision owner: UNASSIGNED.

## Context
Approval consumption, concurrency and crash recovery require transactional state.

## Proposed decision
Plan a separate application PostgreSQL database for sessions, action intents, approval state, receipts and outbox. Local artifacts suffice only for the first synthetic profile.

## Alternatives considered
In-memory stores for production, or reuse the observability platform metadata schema.

## Consequences and limitations
Schema migrations, backup, access and crash-recovery obligations. A database transaction cannot atomically cover an arbitrary external service.

## Acceptance evidence required
Concurrent reservation/approval, crash/restart, stale state, revocation and ambiguous dispatch tests.

## Revisit trigger
Revisit when acceptance fails, intended-use or deployment requirements change,
or a pinned dependency changes materially. Record the superseding ADR and rerun
affected qualification; do not silently change the baseline.

References: [source register](../SOURCES.md), [system specification](../../SPEC.md).
