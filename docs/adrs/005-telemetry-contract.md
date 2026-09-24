# ADR 005: Use hybrid instrumentation and versioned event contracts

Status: PROPOSED | Date: 2026-09-24 | Implementation evidence: NOT_RUN
Accountable decision owner: UNASSIGNED.

## Context
Automatic traces expose calls but do not establish policy decisions or correctness.

## Proposed decision
Combine supported OpenTelemetry instrumentation with manual domain events. Define producer, channel, correlation, evidence class and delivery semantics.

## Alternatives considered
Vendor-only events or fully manual logging of every low-level call.

## Consequences and limitations
Telemetry mapping and schema evolution need maintenance. Required evidence is retained independently of sampled diagnostic spans.

## Acceptance evidence required
Check producer/channel access, payload allowlists, missing/duplicate/colliding events, causality and complete trial reconstruction.

## Revisit trigger
Revisit when acceptance fails, intended-use or deployment requirements change,
or a pinned dependency changes materially. Record the superseding ADR and rerun
affected qualification; do not silently change the baseline.

References: [source register](../SOURCES.md), [system specification](../../SPEC.md).
