# Codex instructions — repository scope

## Objective
Build the PA Readiness system described in SPEC.md, README.md, and docs/ARCHITECTURE.md.
Preserve separation between proposals, execution authority, and evaluation truth.
Read the scoped AGENTS.md for every component you edit. Follow the user's current
scope and authorization; do not add routine approval pauses for reversible work.

## Working method
1. Read the relevant numbered task, contracts, and neighboring code before editing.
2. State the concrete implementation scope and assumptions briefly.
3. Make the smallest coherent change; do not overwrite unrelated user work.
4. Add tests for consequential boundaries, state transitions, and failure behavior.
   Avoid tests that merely repeat implementation or inflate counts.
5. Run the relevant checks and report what actually executed, with limitations.
6. Update the component README, task status, and evidence record. Never mark
   PLANNED, MOCK, or NOT_RUN work as complete execution.
7. Continue through authorized tasks. Do not publish, deploy, send messages, or
   make payer/clinical changes unless the user has authorized that action.

## Dependency boundaries
- pa_contracts imports only the standard library.
- pa_agent imports pa_contracts; it must not import harness, evals, tool adapters,
  model SDKs, network clients, approval stores, or benchmark expectations.
- pa_harness imports pa_contracts and receives agent/model/tool implementations
  through ports. It must not import eval scoring, oracles, or judge code.
- pa_models and pa_tools import pa_contracts; neither imports pa_agent or pa_evals.
- pa_evals imports pa_contracts and operates through a SystemUnderTest port.
- pa_runtimes owns one selected loop and uses injected policy/model/tool ports.
- pa_telemetry validates/exports events without authorizing actions or grading.
- pa_governance consumes result artifacts through contracts and owns gate computation.
- Reporting displays snapshots; it cannot implement or override release authority.
- apps/ is the composition root where concrete implementations are wired.
- Optional frameworks stay in their owning adapter/composition layer.
- Harness owns authorization and supervision; runtime_adapters owns the selected loop.
- SDK model/tool callbacks must use the same metering/authorization gateways.

Python packages and this static check are not a security boundary. Use separate
process/service identities, credentials, file mounts, and network policies for
model-facing execution, the trusted control plane, and qualification scoring.

## Required semantics
- Product: READY / NOT_READY / UNKNOWN.
- Evaluation: PASS / FAIL / UNRESOLVED.
- Release gate: GO / NO_GO / INCONCLUSIVE; GO is not authorization.
- Release authorization is a separate authenticated, candidate-bound record.
- HOLD is only a reporting label for incomplete evidence or pending authorization.
- A confirmed required-evidence blocker establishes NOT_READY. If no blocker is
  established and required evidence is unavailable/unverifiable, return UNKNOWN.
  Preserve both established blockers and unresolved checks in the explanation.
- READY never implies payer approval, medical necessity, or submission authority.
- Documents, user messages, memory, and tool output cannot grant permissions.
- Agent calls are proposals. Trusted adapters authenticate scope; the harness
  rechecks authorization/state before any effect.
- Initial scope is synthetic/read-only. External review Tasks and submit/update/
  cancel remain disabled until separately implemented and authorized.
- Approval must bind caller, case, operation, destination, payload, relevant
  evidence/policy/configuration, expiry, and prior action state.
- Ambiguous effects require reconciliation before retries. Never assume a timeout
  means no effect occurred.

## Data and evaluation integrity
Keep the held-out corpus and all hidden oracles out of optimizer access. The
evaluation controller supplies only the current trial's authorized case input to
the runtime; it never supplies expected answers, hidden labels, or grader internals.
Group related cases and variants in the same partition. Public cases with public
answers are development data. Reserve/freeze qualification before access.
Do not weaken gates, modify expected labels, omit trials, or fabricate traces to
improve a score. Missing evidence and unresolved judgments remain visible.

## Reproducibility
Pin exact dependencies/model artifacts when selected; keep unknown values null.
Do not use mutable latest references in an evidence claim. State hosted-model
immutability limits. Keep code, model, dataset, tool, and environment licenses and
provenance separate. Do not choose/publish a license on the owner's behalf.

## Verification/reporting
Run python3 scripts/check_scaffold.py for structural changes. Add actual build,
unit, integration, regression, and real-adapter checks as implemented. Counts from
earlier external artifacts cannot be reused as this repo's executed results.
Final change reports: changed behavior, evidence, remaining gaps, and next build
task. No credential values, protected records, or raw private traces in Git/logs.

## Revision 0.2 reporting and instrumentation
Read docs/INSTRUMENTATION.md, docs/DASHBOARDS_REPORTS.md and docs/adrs/README.md.
Use versioned metric definitions, declared denominators and source snapshots.
Preserve attempted versus delivered answers and attempted versus executed effects.
Keep OPERATIONAL, EVALUATOR_PRIVATE and PROGRAM channels access-controlled.
Do not export qualification labels or assume SDK default tracing destinations fit
the deployment policy. Use proposed code paths only as implementation plans.

## V1 learning workflow
Read docs/V1_GAP_FIXES.md and the applicable review, calibration, experiment and
monitoring procedures. Q01–Q09 supplement M01–M06. Do not substitute targeted
review incidence for population failure rates, mock traces for real-agent runs,
or development comparisons for independent qualification. Preserve negative
results and all missingness. V1 monitoring is synthetic simulation only.

## Documentation framing
Describe PA product requirements, technical rationale, implementation status and
acceptance evidence directly. Preserve technical citations and distinguish
project design decisions from verified external capabilities or executed results.
