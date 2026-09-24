# ADR 022: Preregister comparisons and account for full workload cost

Status: PROPOSED | Date: 2026-09-24 | Implementation evidence: NOT_RUN
Accountable decision owner: UNASSIGNED.

## Context
Comparison safeguards existed, but executable improvement records and decision rules were underspecified.

## Proposed decision
Use a versioned experiment plan and immutable result packet with paired family-aware analysis, fixed safety constraints and separate runtime/evaluation/review costs.

## Alternatives considered
Post-hoc prompt comparisons; a blended cost-quality score; automatic optimization on qualification labels. Multi-factor designs are permitted only when declared and analyzed accordingly.

## Consequences and limitations
Some experiments end inconclusive; negative results are retained. Selection for qualification is separate from release approval.

## Acceptance evidence required
Detect incomplete pairs and criteria changes; include failed/retry costs; preserve positive controls; independently reproduce the comparison from retained snapshots.

## Revisit trigger
Workload, model identity, noise, budget, objectives or needed interaction design changes.

References: [v1 specification](../V1_GAP_FIXES.md), [source register](../SOURCES.md).
