# ADR 014: Enforce permissions outside the model

Status: PROPOSED | Date: 2026-09-24 | Implementation evidence: NOT_RUN
Accountable decision owner: UNASSIGNED.

## Context
Untrusted prompts and tool output may attempt to expand authority.

## Proposed decision
Gateway authorization and adapter scope checks precede every access/effect. Initial consequential operations remain disabled. Future approvals bind exact action and state.

## Alternatives considered
Prompt instructions, model refusals or SDK guardrails as sole authorization.

## Consequences and limitations
Additional enforcement code and trusted services; denials need legitimate positive controls.

## Acceptance evidence required
Wrong-patient, alternate route, approval replay/race, injected destination and ambiguous-effect cases plus allowed operations.

## Revisit trigger
Revisit when acceptance fails, intended-use or deployment requirements change,
or a pinned dependency changes materially. Record the superseding ADR and rerun
affected qualification; do not silently change the baseline.

References: [source register](../SOURCES.md), [system specification](../../SPEC.md).
