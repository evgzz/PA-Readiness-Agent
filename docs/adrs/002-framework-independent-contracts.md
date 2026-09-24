# ADR 002: Keep domain contracts independent of frameworks

Status: PROPOSED | Date: 2026-09-24 | Implementation evidence: NOT_RUN
Accountable decision owner: UNASSIGNED.

## Context
Provider-specific types can couple policy, tools, and evaluation to one SDK.

## Proposed decision
Use standard-library draft types and JSON Schema contracts. Keep vendor payloads in adapter code; finalize versions in Task 00.

## Alternatives considered
Use SDK objects everywhere for convenience, at the cost of replacement and independent testing.

## Consequences and limitations
Explicit translation and compatibility testing are required; schema validity is not authenticity.

## Acceptance evidence required
Reject unknown/incompatible versions and malformed payloads; producer authentication and payload validation remain separate.

## Revisit trigger
Revisit when acceptance fails, intended-use or deployment requirements change,
or a pinned dependency changes materially. Record the superseding ADR and rerun
affected qualification; do not silently change the baseline.

References: [source register](../SOURCES.md), [system specification](../../SPEC.md).
