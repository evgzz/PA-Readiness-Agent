# ADR 016: Separate gate computation, action approval and release authorization

Status: PROPOSED | Date: 2026-09-24 | Implementation evidence: NOT_RUN
Accountable decision owner: UNASSIGNED.

## Context
READY, PASS, GO and approval refer to different questions.

## Proposed decision
Compute GO/NO_GO/INCONCLUSIVE in pa_governance from validated records. Store authenticated release authorization separately. HOLD is a display label.

## Alternatives considered
Compute approval in the dashboard or reuse a runtime action token for release.

## Consequences and limitations
More records and policy checks; candidate/policy changes and expiry invalidate prior applicability.

## Acceptance evidence required
No-go precedence, missing-evidence inconclusive, exception expiry, mismatched candidate and unauthorized approver tests.

## Revisit trigger
Revisit when acceptance fails, intended-use or deployment requirements change,
or a pinned dependency changes materially. Record the superseding ADR and rerun
affected qualification; do not silently change the baseline.

References: [source register](../SOURCES.md), [system specification](../../SPEC.md).
