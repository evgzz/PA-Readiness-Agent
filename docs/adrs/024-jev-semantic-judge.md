# ADR 024: Add Jev behind the independent semantic judge port

Status: PROPOSED | Date: 2026-09-24 | Implementation evidence: NOT_RUN
Accountable decision owner: UNASSIGNED.

## Context
PA semantic grading needs atomic criteria, multi-turn evidence and measured human
alignment. A final-answer score alone cannot establish trajectory safety.

## Proposed decision
Add Jev as the planned typed semantic judge, using a narrow TypeSafe SDK adapter
in the evaluation plane. Keep deterministic checks authoritative, human labels
independent, and calibration mandatory before relying on semantic verdicts.
Evaluate frozen prefixes and full trajectories through controller-owned evidence
projections. Keep provider probabilities separate from accepted verdicts.

## Alternatives considered
Direct SDK is preferred for a small integration boundary. langchain-typesafe and
LangSmith remain optional experiment adapters. A generative LLM may be a calibrated
challenger or separately identified adjudication aid. Deterministic-only grading
cannot cover all semantic quality; human-only grading remains the fallback when
automated judgments are unresolved. See the detailed option table in the spec.

## Consequences and limitations
No new agent loop, authority, platform migration or runtime dependency is enabled.
Jev cannot supply generated explanations. Hosted version limitations, context
selection, egress, errors, abstention and judge costs require explicit records.
The linked weather experiment does not qualify PA behavior.

## Acceptance evidence required
Implement the provider-neutral port and schemas, validate the SDK/model pin,
exercise failure boundaries, run live synthetic calls, audit against independent
human labels, and reconcile dashboard aggregates to private evidence. All pending.

## Revisit trigger
Revisit on failed calibration, model/service drift, materially changed rubrics,
context policy or use scope. Invalidate affected calibration and regrade explicitly.

References: [Jev specification](../JEV_JUDGE.md), [sources](../SOURCES.md),
[ADR 010](010-evaluation-authority.md), [ADR 012](012-langchain-deferral.md).
