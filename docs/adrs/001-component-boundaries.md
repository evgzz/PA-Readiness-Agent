# ADR 001: Separate agent, harness, evals, governance and reporting

Status: PROPOSED | Date: 2026-09-24 | Implementation evidence: NOT_RUN
Accountable decision owner: UNASSIGNED.

## Context
Execution authority and evaluation truth must remain distinguishable.

## Proposed decision
Keep independent packages connected through versioned contracts and injected ports; wire concrete implementations only in apps/. Reporting reads snapshots.

## Alternatives considered
A framework-centric monolith has fewer interfaces but makes authority and score provenance harder to inspect.

## Consequences and limitations
Additional contract/transport work. Folder boundaries are not isolation; use separate identities and mounts.

## Acceptance evidence required
Import boundaries plus runtime isolation tests; scorer/oracle access denied to the agent process.

## Revisit trigger
Revisit when acceptance fails, intended-use or deployment requirements change,
or a pinned dependency changes materially. Record the superseding ADR and rerun
affected qualification; do not silently change the baseline.

References: [source register](../SOURCES.md), [system specification](../../SPEC.md).
