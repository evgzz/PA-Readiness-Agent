# ADR 023: Stage monitoring through synthetic exercises before operational use

Status: PROPOSED | Date: 2026-09-24 | Implementation evidence: NOT_RUN
Accountable decision owner: UNASSIGNED.

## Context
The baseline covers evidence health but does not define behavioral feedback or comparable-window analysis.

## Proposed decision
Own monitoring analysis in the independent eval plane, authorized alert triage in governance, and begin with synthetic windows. Promote reviewed reproductions only into eligible development data.

## Alternatives considered
Exporter-health-only monitoring; unconditional automatic rollback/promotion; a full live data pipeline before scoped operational requirements.

## Consequences and limitations
Proxy drift does not prove quality loss. Delayed labels and missing denominator data remain explicit. No production deployment is authorized by this ADR.

## Acceptance evidence required
Distinguish seeded behavioral change, input-mix shift, missing telemetry, delayed labels and sparse windows; demonstrate controlled finding-to-development handoff.

## Revisit trigger
An operational deployment is proposed or monitoring cohorts, access policy, alert burden or data availability change.

References: [v1 specification](../V1_GAP_FIXES.md), [source register](../SOURCES.md).
