# V2 evaluation CI and monitoring tiers

Status: PLANNED. Current scaffold.yml validates contracts, packaging and structure.
It does not execute or qualify the PA agent. No new workflow is enabled by this spec.

| Tier | Trigger / cost policy | Required coverage | Evidence class |
|---|---|---|---|
| T0 deterministic | Each change; no model calls | Contracts, scope rules, objective assertions, math/completeness and known positive/negative controls | REFERENCE_CONTROL |
| T1 mocked integration | Relevant pull requests; bounded local world | Full loop wiring, reset, permissions, trace completeness, errors and attack control fixtures | SCRIPTED_DEMO or REFERENCE_CONTROL, explicitly assigned |
| T2 real-agent regression | Trusted changes on a frozen synthetic development suite; pinned budget | Model/tool behavior, calibrated semantic criteria, fixed-k reliability and successful-attack regressions | REAL_AGENT_SYNTHETIC |
| T3 qualification | Frozen candidate and untouched family-separated suite under independent controller | All mandatory quality/safety/coverage criteria plus required adjudication | REAL_AGENT_SYNTHETIC; qualification is a separate status |

Preregister which tiers are mandatory for each change type. Prompt/model/tool/
permission/harness changes need the applicable agent tiers, not just T0. A skipped,
unconfigured, cancelled or incomplete mandatory tier is INCOMPLETE/INCONCLUSIVE,
not PASS. Known non-waived failures block; missing evidence does not hide them.
Set trusted runner identities, least-privilege tokens and data mounts. Untrusted
pull requests receive no private labels or provider credentials; never execute
unreviewed fork code in a privileged qualification context. Pin action/dependency
versions when the workflow is implemented.

Regression case contract: case/family ID, initial state/world version, authorized
input, expected behavioral predicates (private where required), permitted partial
orders, reset procedure, candidate/eval configuration, grader version and evidence
requirements. Inputs never contain the expected answer. A case extracted from an
opened qualification set cannot return to that same independent test claim.

Reset and replay the same world before each trial. Capture all requests, failures,
retry attempts and terminal outcomes. Compute pass^k/pass@k with the versioned
[V2 measurement](V2_MEASUREMENT.md) definitions. Freeze k, cost cap and stopping
rules; do not omit failing repeats or automatically retry the whole suite to green.

CI acceptance: a seeded development regression fails the required tier, a corrected
candidate passes the original case plus positive controls, missing provider access
is visibly incomplete, and reports reconcile to retained trial manifests. Reference
controls demonstrate checker behavior separately from real-agent performance.

## Monitoring after the synthetic deployment

V2 demonstrates monitoring on the running synthetic endpoint or replayed synthetic
windows. Run applicable deterministic checks on every admitted trial; use frozen
judges on a declared probability sample. Keep targeted red-team samples separate.
Track admission counts independently of optional trace export. Review sampling,
judge errors and prevalence correction follow V2_MEASUREMENT.md. Simulate unchanged
control, behavior shift, input-mix shift, delayed labels, sparse samples and source
loss; route alerts to human triage and approved development regressions.

Production monitoring stays NOT_SCOPED. A future operational profile additionally
needs deployment/data scope, accountable operators, access/retention, alert and
incident policies, measured integration and separate authorization. A healthy
exporter or unchanged proxy metric cannot establish correct behavior.
