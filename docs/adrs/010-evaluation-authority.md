# ADR 010: Keep independent evaluation authority

Status: PROPOSED | Date: 2026-09-24 | Implementation evidence: NOT_RUN
Accountable decision owner: UNASSIGNED.

## Context
Candidate-generated self-assessments cannot serve as hidden benchmark truth.

## Proposed decision
Repository-owned evals control labels, schedules, graders, adjudication and metric snapshots. Observability receives only authorized result projections.

## Alternatives considered
Treat platform default scores or the candidate’s self-reported success as release evidence.

## Consequences and limitations
Independent storage and rubric calibration add work; vendor eval tools can still be adapters.

## Acceptance evidence required
Known failures detected, positives preserved, omitted trials visible, mixed identities rejected, and qualification labels isolated.

## Revisit trigger
Revisit when acceptance fails, intended-use or deployment requirements change,
or a pinned dependency changes materially. Record the superseding ADR and rerun
affected qualification; do not silently change the baseline.

References: [source register](../SOURCES.md), [system specification](../../SPEC.md).
