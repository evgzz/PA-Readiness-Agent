# ADR 006: Propose Langfuse as the primary trace platform

Status: PROPOSED | Date: 2026-09-24 | Implementation evidence: NOT_RUN
Accountable decision owner: UNASSIGNED.

## Context
The course baseline uses Langfuse and the project needs trace review plus linked scores.

## Proposed decision
Adopt Langfuse provisionally for trace inspection, subject to deployment/version evaluation. Use native dashboards and supported APIs where sufficient.

## Alternatives considered
Arize Phoenix, Braintrust, or another approved platform assessed using the same acceptance workflow.

## Consequences and limitations
Operating the self-hosted stack adds services. It remains a projection, not the sole action ledger or release authority.

## Acceptance evidence required
Trace/score correlation, export, access controls, hidden-label isolation, egress policy, upgrade behavior and freshness verified on the selected version.

## Revisit trigger
Revisit when acceptance fails, intended-use or deployment requirements change,
or a pinned dependency changes materially. Record the superseding ADR and rerun
affected qualification; do not silently change the baseline.

References: [source register](../SOURCES.md), [system specification](../../SPEC.md).
