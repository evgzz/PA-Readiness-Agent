# ADR 007: Limit ClickHouse to analytical data

Status: PROPOSED | Date: 2026-09-24 | Implementation evidence: NOT_RUN
Accountable decision owner: UNASSIGNED.

## Context
Trace analytics and transactional action/approval state have different consistency needs.

## Proposed decision
Use the selected Langfuse deployment’s ClickHouse for platform analytics. If needed, maintain a separate project-owned reporting schema and supported ingestion path.

## Alternatives considered
Put application approvals in analytics storage, or couple dashboards directly to undocumented platform tables.

## Consequences and limitations
Separate authoritative stores and projections require reconciliation. An analytics query cannot authorize an action.

## Acceptance evidence required
Supported integration path, scoped read permissions, version compatibility and source-to-projection reconciliation.

## Revisit trigger
Revisit when acceptance fails, intended-use or deployment requirements change,
or a pinned dependency changes materially. Record the superseding ADR and rerun
affected qualification; do not silently change the baseline.

References: [source register](../SOURCES.md), [system specification](../../SPEC.md).
