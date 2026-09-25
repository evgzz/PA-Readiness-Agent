# ADR 026 — Compare candidate architectures and separate qualification profiles

Status: PROPOSED | 2026-09-25 | Owner roles: engineering, evaluation and release review; UNASSIGNED

## Context
The delivery plan specifies a mock, then one real agent, before measured improvement.
It does not test whether rules or a fixed extraction workflow satisfy the same task.
Requiring every cost experiment before initial qualification also couples evidence
for unused features to the selected candidate's independent assessment.

## Proposed decision
Adopt specification 2.1 and plan 1.1: compare rules-only A, fixed extraction workflow B
and bounded agent C under controlled inputs, enforcement and accounting. Add early
property/replay checks, component diagnosis and a claim-dependent human utility
study. Retain the 60-real-trace review floor and independent evaluator calibration.

Amend ADR 025's dependency interpretation: full V2-A–D completion retains all
experiments; SCOPED_CANDIDATE qualification requires the core path plus evidence for
every used feature. FULL_V2_PROGRAM still requires all five P6 subphases. Freeze
applicability before qualification; unknown capabilities do not qualify as absent.

## Alternatives and tradeoffs

| Option | Assessment |
|---|---|
| Build only the agent | Simpler comparison setup; no evidence that autonomy is needed. |
| Treat a scripted mock as rules-only performance | Reject: hard-coded answers do not test readiness predicates or generalization. |
| Trust schema-valid extraction | Reject: structured output can misrepresent source meaning. |
| Require all optimizations before any qualification | Retained for full-program completion; unnecessary coupling for a candidate with verified absent features. |
| Make all optimizations optional | Reject: used caching/routing/replacements require applicable evidence; full-program experiments remain mandatory. |
| Qualify only from development results | Reject: selection and independent held-out assessment remain separate. |

## Consequences and acceptance
More development comparisons are explicit, but only one model/provider is initially
needed for B/C. Replays and ablations diagnose components without establishing live
performance. Utility studies require qualified participants before productivity
claims. Implementation must validate profile/candidate binding and reject unknown
or stale applicability. Dashboards must distinguish scoped assessment from full
program completion. No runtime, model, deployment or performance gain is implemented
or accepted by this decision.

Corresponding specs: [comparison](../ARCHITECTURE_COMPARISON.md),
[qualification profiles](../QUALIFICATION_PROFILES.md),
[delivery plan](../PHASED_DELIVERY_PLAN.md).
