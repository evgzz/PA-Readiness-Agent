# ADR 017: Version metric definitions and source snapshots

Status: PROPOSED | Date: 2026-09-24 | Implementation evidence: NOT_RUN
Accountable decision owner: UNASSIGNED.

## Context
Different denominators or eligibility filters can yield misleadingly similar charts.

## Proposed decision
Use the shared metric registry. Evals computes run metrics; governance computes program metrics. Dashboards consume values and source lineage.

## Alternatives considered
Define each formula separately in UI widgets, CI scripts and executive slides.

## Consequences and limitations
Metric evolution requires versioning; history comparisons need compatible cohorts and definitions.

## Acceptance evidence required
Zero denominators, unresolved counts, duplicate ingestion, mixed configuration, reopened findings and time-based overdue recomputation.

## Revisit trigger
Revisit when acceptance fails, intended-use or deployment requirements change,
or a pinned dependency changes materially. Record the superseding ADR and rerun
affected qualification; do not silently change the baseline.

References: [source register](../SOURCES.md), [system specification](../../SPEC.md).
