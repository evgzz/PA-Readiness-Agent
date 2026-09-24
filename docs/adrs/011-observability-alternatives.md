# ADR 011: Evaluate Braintrust and Arize Phoenix as alternatives

Status: PROPOSED | Date: 2026-09-24 | Implementation evidence: NOT_RUN
Accountable decision owner: UNASSIGNED.

## Context
Review workflow, deployment fit and portability may favor another observability platform.

## Proposed decision
Keep both as unselected alternatives. Compare identical trace/review/experiment/export tasks and data-boundary requirements before adoption.

## Alternatives considered
Run multiple overlapping primary platforms by default.

## Consequences and limitations
Parallel instrumentation and divergent scores increase operational and interpretation costs.

## Acceptance evidence required
Document feature/deployment fit, vendor version, migration/export fidelity, access controls, costs and a single primary source for each record.

## Revisit trigger
Revisit when acceptance fails, intended-use or deployment requirements change,
or a pinned dependency changes materially. Record the superseding ADR and rerun
affected qualification; do not silently change the baseline.

References: [source register](../SOURCES.md), [system specification](../../SPEC.md).
