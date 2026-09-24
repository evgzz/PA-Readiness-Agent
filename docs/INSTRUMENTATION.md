# Instrumentation and evidence contracts

Status: producer/emitter integrations PLANNED. Task 00 implements contract validation
and telemetry/src/pa_telemetry/ingress.py; capture/export modules below remain future work.
The envelope schema and registries included in this revision are design contracts.

## Capture facts at the owning boundary

| Proposed location | Capture point / events | Authoritative record | Export channel |
|---|---|---|---|
| `harness/src/pa_harness/intake.py` | Admission/termination: `run.started`, `run.completed` | Run manifest and terminal record | OPERATIONAL |
| `model_adapters/src/pa_models/usage.py` | Model request/response/error: `model.call.completed` | Usage and provider receipt, including failed calls | OPERATIONAL |
| `harness/src/pa_harness/policy.py` | Before dispatch: `action.proposed`, `authorization.decided` | Action ledger | OPERATIONAL |
| `tool_adapters/src/pa_tools/receipts.py` | Dispatch response/reconciliation: `action.dispatched`, `effect.observed`, `effect.reconciled` | Adapter/service evidence and action ledger | OPERATIONAL |
| `harness/src/pa_harness/output_validation.py` | Proposed and delivered assessment: `assessment.validated` | Output validation record | OPERATIONAL |
| `evals/src/pa_evals/graders.py` | After independent grading: `trial.graded` | Private per-assertion and trial result | EVALUATOR_PRIVATE |
| `evals/src/pa_evals/completeness.py` | Trial/evidence reconciliation: `run.finalized`, `coverage.updated` | Finalized run and coverage snapshot | EVALUATOR_PRIVATE |
| `governance/src/pa_governance/findings.py` | Lifecycle transition: `finding.updated`, `finding.closed`, `finding.reopened` | Versioned finding and verification evidence | PROGRAM |
| `governance/src/pa_governance/program_metrics.py` | Snapshot refresh: `program_metrics.updated` | Owner/deadline/history projection | PROGRAM |
| `governance/src/pa_governance/release_gate.py` | Gate recomputation: `release_gate.evaluated` | Immutable/versioned gate snapshot | PROGRAM |
| `governance/src/pa_governance/approvals.py` | Authenticated decision: `release_authorization.recorded` | Authorization identity, scope, expiry and decision | PROGRAM |
| `telemetry/src/pa_telemetry/export.py` | Export acknowledgment/failure: `telemetry.export_status` | Delivery checkpoint and ingest health | PROGRAM |

Observability hooks do not authorize tool calls. `effect.observed` records what
the adapter observed; the evaluator independently determines whether that effect
was authorized and whether evidence is sufficient. A denial alone cannot prove
that another route did not execute an action.

## Common envelope

`contracts/schemas/event-envelope-v1.schema.json` defines v1 identity and
correlation metadata. Event bodies are referenced through protected, hashed payload
artifacts; diagnostic exports use a separate allowlist and omit payload contents
unless explicitly permitted. The schema does not authenticate the emitter or
validate referenced bytes; ingestion must verify identity, channel permissions,
payload type, digest, and allowed event types for that producer.

| Field group | Required meaning |
|---|---|
| Event identity | `event_id`, `event_type`, `schema_version`, `producer`, `producer_instance`, `sequence` |
| Time | `occurred_at`, `ingested_at`; UTC instants, with clock/skew handling |
| Candidate | `release_id`, `candidate_config_digest`; null only when no candidate is applicable |
| Evaluation | `evaluation_config_digest`, `run_id`, `trial_id`, `case_id`, `slice_id` where applicable |
| Action | `action_id` identifies logical intent; `attempt_id` identifies one execution attempt |
| Trace/work item | `trace_id`, `span_id`, `finding_id`, and `causation_event_id` as applicable |
| Evidence | `evidence_class`, `channel`, `payload_ref`, `payload_sha256` |

Identifiers are non-sensitive scoped pseudonyms in exported telemetry. Raw patient
IDs, document contents, credentials, prompts containing protected data, and answer
keys are not default attributes. High-cardinality case/run IDs belong in records
and trace links, not unbounded time-series metric labels.

Event class values: REFERENCE_CONTROL, SCRIPTED_DEMO, REAL_AGENT_SYNTHETIC,
REAL_AGENT_PRODUCTION. These identify execution type; none asserts qualification.
Current example events use SCRIPTED_DEMO and are not emitted run evidence.

## Required event payload facts

- Authorization: trusted scope reference, policy/version, operation, destination
  class, argument digest, ALLOW/DENY, reason code. Agent claims are separate inputs.
- Dispatch/effect: action/attempt IDs, service request ID, endpoint identity,
  idempotency key reference, response status, effect type, reconciliation state,
  receipt/world-state references. Include unauthorized reads/disclosures.
- Assessment: proposed outcome, delivered outcome, validator revision, blockers,
  unresolved checks, permitted evidence references. No evaluator reference label.
- Private grade: reference outcome, observed outcomes, assertion verdicts,
  grader/rubric identity, adjudication status, failure categories, input digests.
- Finding/approval: actor identity verified server-side, previous/new version,
  decision/reason, due-date history, retest evidence, expiry where applicable.

Task 00 implements event payload schemas and fail-closed authenticated ingress
validation. Task 06 must wire a real credential verifier, durable writer and
exporter. A parseable envelope alone is insufficient for accepting an event.

## Durable capture and delivery

Initial synthetic profile: append records to a local journal and finalize immutable
run artifacts with a content manifest. This is a development profile, not proof of
crash-safe production storage. Production/durable profile: commit state plus outbox
record in one application database transaction, then export with retry/checkpointing.

Consumers deduplicate identical `event_id` records. A same-ID/different-content
collision is an integrity error. Retries retain distinct attempt IDs. Do not depend
on ingestion order or wall-clock timestamps for causality; use causal links and
producer sequence. Detect gaps and leave affected metrics unresolved until repaired.
Outbox export may duplicate delivery; it does not make an external tool exactly-once.

Required evidence is not sampled. Optional diagnostic spans may be sampled only
under an explicit policy, with no claim that they establish complete coverage.
Telemetry outage can leave a dashboard STALE while a durable ledger continues;
loss of required ledger persistence prevents consequential dispatch and blocks
qualification. Distinguish the two failure modes.

## SDK and collector strategy

Use automatic instrumentation for supported model, HTTP, and database calls; add
manual semantic events at policy, reconciliation, grading, and governance boundaries.
An OpenTelemetry-compatible exporter/collector is proposed, not yet configured.
The SDK's built-in tracing must be explicitly configured to approved destinations.
Do not accidentally retain a default hosted exporter when enabling a local-only
profile. Verify actual destinations, including model inference and secondary tools.

Langfuse gets authorized observability projections and linked scores. Evaluation
labels and full qualification corpus remain in the private evaluation plane.
Score publication must follow dataset access policy: per-case correctness feedback
may reveal a held-out answer and is withheld from the runtime/optimizer.

## Acceptance checks to implement

Test duplicate/colliding events, delayed/out-of-order arrival, sequence gaps,
missing terminal events, invalid producer/channel combinations, hidden-label
export, crash before/after state commit, failed export recovery, metric recompute,
and SDK callback bypass. No required evidence gap may produce a green safety claim.

## V1 review, experiment and feedback capture

Use contracts/schemas/event-envelope-v1.schema.json for v1 producers. The old
v0.2 envelope remains for historical examples and must not silently accept new
event types. The versioned catalog is the producer/channel authority contract;
ingestion must enforce it. New workflow IDs reside in protected event payloads.

| Proposed location | Capture point / events | Required payload facts | Channel |
|---|---|---|---|
| evals/src/pa_evals/review.py | Persist selection: review.batch.created; accepted annotation: review.annotation.recorded; adjudication: review.adjudicated | Batch/population digests, sampling method, trial/annotation versions, reviewer, evidence refs, reviewability; original labels retained | EVALUATOR_PRIVATE |
| evals/src/pa_evals/review.py | Publish codebook: taxonomy.versioned | Taxonomy version, definitions, review record and affected classification versions | EVALUATOR_PRIVATE |
| evals/src/pa_evals/calibration.py | Reviewed rubric: rubric.reviewed; completed audit: calibration.finalized | Human references, judge/rubric/audit digests, class counts, errors, unresolved, acceptance limits and disposition | EVALUATOR_PRIVATE |
| evals/src/pa_evals/experiments.py and comparisons.py | Lock plan: experiment.registered; persist result: experiment.finalized | Plan digest, changed factors, baseline/candidate and dataset identities, complete/missing pairs, metrics, uncertainty, guardrails and decision | EVALUATOR_PRIVATE |
| evals/src/pa_evals/monitoring.py | Persist versioned window: monitoring.window.finalized | Window/cohort/reference digests, admission counts, completeness, label maturity, proxy/confirmed signal and uncertainty | EVALUATOR_PRIVATE |
| governance/src/pa_governance/monitoring_alerts.py | Create/update authorized alert: monitoring.alert.updated | Sanitized signal, cohort/window refs, owner, deadline, disposition and finding reference | PROGRAM |

Publish events only after the authoritative record is persisted. Event IDs and
record versions support idempotent projections; failed exports do not erase the
underlying review or comparison. Report exporters may send approved aggregates to
Langfuse or other selected consumers, with no private labels in default attributes.

For Q05/Q06, extend the existing owning boundaries: harness admission/terminal
records capture monotonic duration and outcome; model usage records capture each
attempt including errors, tokens, cache category and provider receipt; tool records
capture metered usage. Pricing is versioned separately. Missing provider usage is
explicitly unknown, not a zero token/cost event. Eval/judge calls and review effort
have separate cost categories so runtime efficiency remains interpretable.

## Jev capture plan
The [Jev specification](JEV_JUDGE.md) adds planned private judge request, attempt,
result and trajectory-projection records. pa_evals.trajectories persists the frozen
prefix/trajectory digest; pa_models.jev captures each provider attempt and usage;
pa_evals.judges persists raw typed outputs and normalized assertions;
pa_evals.calibration persists human alignment and repeatability results.

Correlate run/trial/trajectory/turn/step, judge request/repetition/attempt and
criterion IDs in controlled records. Capture requested/returned model, SDK,
rubric/threshold/context versions, evidence digest, response disposition, monotonic
latency, tokens and versioned cost/unknown usage. Use EVALUATOR_PRIVATE, including
provider failures: operational model-call events are not a safe default for judges.

These detailed records are future contracts, not accepted event payloads today.
Task 04 must add/version their schemas and port; Task 06 must register producers,
channels and payload references before ingress/export. Existing trial.graded,
calibration.finalized and experiment.finalized events link compatible persisted
results only through fields allowed by their current schema. Do not add unknown
attributes or publish unregistered judge events. Raw traces/labels stay private;
reporting receives authorized aggregate projections. Never export credentials or
provider response bodies to general telemetry.
