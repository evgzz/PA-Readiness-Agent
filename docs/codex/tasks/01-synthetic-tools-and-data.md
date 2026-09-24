# Synthetic world, requirements and grouped data

Status: PLANNED. Read root/scoped AGENTS.md, SPEC.md and relevant ADRs.

## Build
Build deterministic read-only case/requirements/evidence/validation adapters with reset receipts and explicit FOUND/CONFIRMED_ABSENT/UNAVAILABLE/AMBIGUOUS states. Expand the three examples into reviewed cases for the catalog; declare source families, partitions and labels. Keep all related variants in one split. Disabled writes can be attacked only in an isolated synthetic world.

## Completion evidence
Reproducible reset, correct lineage, foreign-scope denial, outage distinct from absence, and reviewed positive/negative cases. Record actual dataset/version/counts; do not infer coverage from catalog rows.

## Handoff
Record changed files, exact commands, actual results, evidence locations and
remaining inputs in component documentation and docs/BUILD_STATUS.json. Keep
evidence classes separate. Never invent test counts, model pins, owners or dates.

## V1 completion requirements

Create a reviewed scenario matrix, with intended behavior and evidence states,
positive controls and ambiguous cases. Declare grouped development, calibration
and qualification partitions; synthetic generator provenance and human label review
are required. Three retained interface examples do not satisfy coverage.

## V2 completion requirements

Implement docs/SYNTHETIC_SCENARIOS.md: deterministic fictional facts, controlled
generator instructions and provenance, reviewed coverage matrix and smoke report.
Group families before split/augmentation; enforce hidden-fact isolation, ambiguous
cases, negative/positive controls and reset receipts. Counts follow PA coverage
and precision. Document the sample-size rationale before acceptance.
