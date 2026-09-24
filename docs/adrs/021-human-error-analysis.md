# ADR 021: Human review precedes automated failure metrics

Status: PROPOSED | Date: 2026-09-24 | Implementation evidence: NOT_RUN
Accountable decision owner: UNASSIGNED.

## Context
Existing finding tracking does not establish how failure categories or reference judgments are discovered.

## Proposed decision
Use a reproducible development-trace review batch, append-only annotations, versioned taxonomy and domain-owner rubric review before automated semantic scoring.

## Alternatives considered
Ad hoc spot checks; LLM-only taxonomy/labels; coding every trace without a sampling plan. LLM suggestions may assist but do not become reference truth without review.

## Consequences and limitations
Review costs and label disputes remain visible; targeted sampling supports discovery, not unbiased prevalence. Qualification feedback remains isolated.

## Acceptance evidence required
Reconstruct selected population and counts; preserve initial disagreement; trace category to grader; detect duplicate review inflation and private-label leakage.

## Revisit trigger
Review burden, domain scope, taxonomy stability or observed judge disagreement changes materially.

References: [v1 specification](../V1_GAP_FIXES.md), [source register](../SOURCES.md).
