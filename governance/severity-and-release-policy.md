# Proposed severity, findings, and release policy

Status: DRAFT; policy version 0.2-proposed. No named release authority is assigned.
This is a project policy proposal, not a regulatory certification or NVIDIA policy.

## Severity and triage

| Severity | Example impact | Proposed release treatment |
|---|---|---|
| S0 Critical | Confirmed cross-case disclosure, unauthorized consequential effect, approval bypass | Immediate release block; non-waivable under this policy; contain exposure and escalate |
| S1 High | Delivered false READY, material unsupported claim, repeatable safety-boundary weakness | Blocks release until verified mitigation or an explicitly eligible, approved exception |
| S2 Medium | Recoverable reliability failure, excessive refusal, incomplete noncritical reporting | Owner/date and measurable closure; assess against release scope and mandatory gates |
| S3 Low | Minor usability/documentation defect without changed safety behavior | Track and schedule; verify no hidden impact |
| UNTRIAGED | Impact or exploitability not yet established | Cannot be treated as low; block if potentially material to mandatory scope |

Severity considers actual/potential impact, exposure, exploitability, and controls.
A blocked attack attempt is evidence to analyze, not automatically a critical
executed-effect finding. Keep attempted and realized impact distinct.
The rubric owner must assign response and escalation deadlines before live use;
no fabricated SLA or owner assignment appears in the templates.

## Finding lifecycle and closure

NEW → TRIAGED → MITIGATION_IN_PROGRESS → RETEST_PENDING → VERIFIED_CLOSED.
Reopen upon failed reproduction/regression, invalidated evidence, or recurrence.
RISK_ACCEPTED is a separate state; it does not count as verified mitigation closure.

Closure requires: affected candidate and original failing case; implemented change;
unchanged-case retest; relevant regression and legitimate positive control; recorded
residual risk; and an authenticated reviewer. If the original oracle was wrong,
use an adjudicated label correction and rerun affected evidence; do not mislabel
that correction as a demonstrated code mitigation.

## Gate algorithm (to implement in pa_governance)

1. Validate candidate identity, evaluation identity, policy version, source snapshot,
   intended-use scope, required coverage, and evidence integrity/completeness.
2. Evaluate mandatory thresholds using versioned metrics and declared uncertainty.
3. Evaluate open findings, closure validity, dependency readiness, and exceptions.
4. If any demonstrated non-waived mandatory blocker exists: NO_GO. Preserve all
   concurrent missing evidence and additional blockers.
5. Otherwise, if required configuration, labels, samples, thresholds, scope review,
   owners, evidence, or gate-relevant dependency is missing/stale: INCONCLUSIVE.
6. Otherwise: GO, meaning eligible for independent release authorization.

Thresholds and numerical sample sizes must be preregistered; template nulls do not
default to permissive values. No weighted average can override a mandatory blocker.

## Exceptions and authorization

An exception identifies finding/gate, candidate and use scope, rationale, residual
risk, compensating controls, approver identity, review date, and expiry. It must
be permitted by the versioned policy. S0 boundary breaches and missing mandatory
evidence are non-waivable in this proposal. Expired/revoked/mismatched exceptions
have no effect. Risk acceptance remains visible and never counts as a fix.

Runtime approval permits a specific action. A GO gate recommends a candidate.
Release authorization is a separate authenticated record bound to candidate,
evaluation scope, policy and gate snapshot, with approver, time, expiry/revocation,
and rationale. A dashboard button cannot invent this authority. Production
deployment consumes only a valid authorization and current GO snapshot.

The gate snapshot does not include its later authorization record in its input
digest. An approval references the existing gate snapshot. Reuse that snapshot
while substantive gate inputs are unchanged; refreshing an approval display must
not create a new gate digest that invalidates the same approval.

Retain approvals and exceptions as versioned records. Changes to the candidate,
policy, mandatory evidence or risk state require reevaluation. A prior signature
is not portable to a different configuration. The dashboard shows HOLD for an
inconclusive gate or pending approval; BLOCKED for NO_GO; AUTHORIZED only when
the separately checked authorization is valid.

## Planned qualification-profile integration — specification 2.1

[Qualification profiles](../docs/QUALIFICATION_PROFILES.md) amend the planning
prerequisites for P7, not the current release-policy schema or gate algorithm.
Before activating them, implement validated candidate/profile identities, frozen
mandatory-criterion resolution and feature applicability with evidence. A known
mandatory failure retains NO_GO precedence; UNKNOWN or missing mandatory evidence
cannot yield GO. SCOPED_CANDIDATE does not imply FULL_V2_PROGRAM completion.
Planning templates cannot authorize execution or be passed as active policy records.
