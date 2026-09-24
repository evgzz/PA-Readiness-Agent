# ADR 012: Defer LangChain unless a specific integration needs it

Status: PROPOSED | Date: 2026-09-24 | Implementation evidence: NOT_RUN
Accountable decision owner: UNASSIGNED.

## Context
The agent and contracts do not require a general integration framework.

## Proposed decision
Use narrowly scoped adapters first. Introduce LangChain only for a concrete connector with justified maintenance benefit.

## Alternatives considered
Add LangChain preemptively to every layer.

## Consequences and limitations
Fewer dependencies initially; later integrations may require translation work.

## Acceptance evidence required
Connector acceptance, pinning, model/tool gateway preservation and no duplicate loop ownership.

## Revisit trigger
Revisit when acceptance fails, intended-use or deployment requirements change,
or a pinned dependency changes materially. Record the superseding ADR and rerun
affected qualification; do not silently change the baseline.

References: [source register](../SOURCES.md), [system specification](../../SPEC.md).
