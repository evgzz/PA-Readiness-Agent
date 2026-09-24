# ADR 015: Use CI to preserve reproducible evidence

Status: PROPOSED | Date: 2026-09-24 | Implementation evidence: NOT_RUN
Accountable decision owner: UNASSIGNED.

## Context
A build pass is distinct from safety qualification.

## Proposed decision
Keep scaffold CI explicit. Add frozen evaluation jobs and source-linked scorecards only as implemented; bind source/config/dataset/grader identities.

## Alternatives considered
Use a dashboard green tile or total unit-test count as release qualification.

## Consequences and limitations
CI artifacts need retention/access policy and model/resource availability. Live jobs must not silently degrade to mocks.

## Acceptance evidence required
Failing mandatory evaluations and incomplete evidence block recommendation; capture real commands and run results.

## Revisit trigger
Revisit when acceptance fails, intended-use or deployment requirements change,
or a pinned dependency changes materially. Record the superseding ADR and rerun
affected qualification; do not silently change the baseline.

References: [source register](../SOURCES.md), [system specification](../../SPEC.md).
