# ADR 013: Revisit LangGraph for durable workflow requirements

Status: PROPOSED | Date: 2026-09-24 | Implementation evidence: NOT_RUN
Accountable decision owner: UNASSIGNED.

## Context
Future case management may require pause/resume and long-running orchestration.

## Proposed decision
Record LangGraph as a conditional runtime-adapter candidate. Evaluate it when durable workflow requirements exceed the selected runtime profile.

## Alternatives considered
Extend the existing adapter or use a dedicated workflow engine.

## Consequences and limitations
Changing orchestration changes behavior, retry/resume semantics and qualification evidence.

## Acceptance evidence required
Crash/resume, cancellation, stale evidence, revoked authority, replay and repeated side-effect tests under the same contracts.

## Revisit trigger
Revisit when acceptance fails, intended-use or deployment requirements change,
or a pinned dependency changes materially. Record the superseding ADR and rerun
affected qualification; do not silently change the baseline.

References: [source register](../SOURCES.md), [system specification](../../SPEC.md).
