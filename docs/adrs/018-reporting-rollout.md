# ADR 018: Start with artifact scorecards and program records

Status: PROPOSED | Date: 2026-09-24 | Implementation evidence: NOT_RUN
Accountable decision owner: UNASSIGNED.

## Context
No runtime exists yet; a custom dashboard would add work before measured evidence.

## Proposed decision
Build deterministic CI/Markdown reports and versioned findings first. GitHub Projects can be the work-tracking source if explicitly configured; snapshots feed release dossiers. Add native Langfuse views when traces exist.

## Alternatives considered
Custom UI; Metabase/curated PostgreSQL for executive analytics; Grafana/project-owned ClickHouse schema for operational monitoring.

## Consequences and limitations
Initial reports are refreshed by jobs and may span two views. Reporting is read-only; choose one authority for work-item updates.

## Acceptance evidence required
Recompute all six metrics from a fixed snapshot; drill down to source evidence; display stale/missing data; preserve access boundaries.

## Revisit trigger
Revisit when acceptance fails, intended-use or deployment requirements change,
or a pinned dependency changes materially. Record the superseding ADR and rerun
affected qualification; do not silently change the baseline.

References: [source register](../SOURCES.md), [system specification](../../SPEC.md).
