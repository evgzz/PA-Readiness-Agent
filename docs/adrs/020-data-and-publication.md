# ADR 020: Separate open development assets from qualification evidence

Status: PROPOSED | Date: 2026-09-24 | Implementation evidence: NOT_RUN
Accountable decision owner: UNASSIGNED.

## Context
Reproducibility, data rights, hidden answers and protected runtime data have different access needs.

## Proposed decision
Publish only reviewed assets with provenance and rights. Keep grouped partitions, private qualification labels, protected traces and credentials outside Git and runtime access.

## Alternatives considered
Treat all synthetic-looking data as automatically publishable or all public examples as held-out.

## Consequences and limitations
Asset-by-asset review and deployment access controls are required; this draft assigns no new license.

## Acceptance evidence required
Split-family leakage, hidden-label export, source/rights review, artifact integrity and explicit model/standards pins.

## Revisit trigger
Revisit when acceptance fails, intended-use or deployment requirements change,
or a pinned dependency changes materially. Record the superseding ADR and rerun
affected qualification; do not silently change the baseline.

References: [source register](../SOURCES.md), [system specification](../../SPEC.md).
