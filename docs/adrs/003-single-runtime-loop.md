# ADR 003: Use one runtime adapter; propose OpenAI Agents SDK for real runs

Status: PROPOSED | Date: 2026-09-24 | Implementation evidence: NOT_RUN
Accountable decision owner: UNASSIGNED.

## Context
The original scaffold described a custom loop while the course baseline selected an SDK.

## Proposed decision
Select one RuntimePort implementation per run: deterministic mock first; OpenAI Agents SDK adapter for a selected real profile. Harness gateways retain policy and model/tool metering.

## Alternatives considered
Custom production loop or a LangGraph adapter. Never nest competing orchestration loops for one run.

## Consequences and limitations
SDK callbacks, retries, model transport, guardrails, and exporters need verification. API SDK handles transport; Agents SDK handles orchestration.

## Acceptance evidence required
All SDK model/tool paths traverse required gateways; denied calls have no authorized dispatch; permitted calls succeed; no silent mock fallback.

## Revisit trigger
Revisit when acceptance fails, intended-use or deployment requirements change,
or a pinned dependency changes materially. Record the superseding ADR and rerun
affected qualification; do not silently change the baseline.

References: [source register](../SOURCES.md), [system specification](../../SPEC.md).
