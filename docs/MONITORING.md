# Monitoring and feedback plan

Status: PLANNED. V1 requires a simulated exercise using controlled synthetic runs.
Live production collection, real patient data and autonomous remediation are
NOT_SCOPED. This plan does not authorize deployment or additional data collection.

## Cohorts, windows and completeness

The monitoring plan pins deployment/candidate, intended-use scope, evidence class,
baseline/current windows, timezone, minimum data, late-arrival grace, expected
refresh cadence, alert thresholds, sampling policy, label-delay assumptions and
accountable triage owner. Values remain null until a profile is selected.
Use contracts/v1/monitoring-plan.template.json.

Compare like cohorts by model/harness/configuration, task/risk slice, source
version and relevant operating conditions. A changed configuration starts a new
cohort unless a documented comparison design accounts for it. Windows and source
snapshots are versioned. Late labels cause a new snapshot, never silent mutation.

Compute eligible run count from admission/control-plane records independent of
the optional trace exporter. Q08 distinguishes required evidence completeness,
review sample coverage and label availability. Missing telemetry or a stale source
is an observability incident, not evidence of stable behavior. If admission counts
are unavailable, monitoring coverage is UNKNOWN, not 100%.

## Signal types and dashboard interpretation

| Signal | Evidence | Interpretation and action |
|---|---|---|
| Confirmed correctness/safety regression | Adjudicated or validated grader labels on comparable eligible cohorts. | Report measured change, uncertainty and sample/class counts; triage against preregistered limits. |
| Input/behavior shift | Task mix, tool use, outcomes, tokens, refusal/escalation or latency distribution. | Proxy signal for investigation; does not establish a correctness decline without suitable reference evidence. |
| Evidence/telemetry failure | Missing terminal records, exporter backlog, delayed labels, source age or unexplained count mismatch. | Display INCOMPLETE/STALE and route to the owning team; do not generate a healthy performance card. |
| Confirmed severe boundary breach | Independently verified forbidden effect or disclosure. | Escalate under the incident policy regardless of aggregate sample size. |

Q09 reports the change with reference/current window digests, method, sample sizes,
label maturity and status. Distinguish no detected signal from evidence of
equivalence. Alert rules need minimum sample/precision criteria, repeated-testing
handling and a planned cadence. Empty or underpowered windows are INSUFFICIENT_DATA.

## Triage and feedback

1. Persist a window snapshot and event before issuing an alert projection.
2. Deduplicate alerts by signal/cohort/window; retain occurrences and revisions.
3. Assign an owner, acknowledgement deadline and disposition: investigating,
   confirmed issue, benign shift, measurement failure or insufficient evidence.
4. Route confirmed issues to versioned findings with permitted trace references.
5. Review rights, de-identification and split lineage before adding a reproducer
   to development data. Keep family groups together. No active qualification labels
   enter optimizer access through annotations, scores, alerts or examples.
6. Fixes use the same experiment/regression/qualification path. Monitoring cannot
   silently change prompts, models, thresholds, permissions or release approval.

## Instrumentation and exercise

Proposed module: evals/src/pa_evals/monitoring.py consumes authorized operational
records and independent labels through ports. It emits monitoring.window.finalized
to EVALUATOR_PRIVATE. Governance creates sanitized alert projections and emits
monitoring.alert.updated to PROGRAM; dashboard access does not grant raw-label access.
apps/ owns scheduling and concrete integrations. Telemetry transports facts and
reports exporter health; it does not assign behavioral truth.

The synthetic exercise must include unchanged comparable windows, a seeded
behavior change, an input-mix shift without known quality change, missing telemetry,
delayed labels and a sparse window. Demonstrate correct distinctions and a traceable
finding-to-development-case handoff. Deterministic fixture injections are labeled
REFERENCE_CONTROL or SCRIPTED_DEMO; they are not observed production incidents.

Completion requires window records, Q08/Q09 snapshots, alert/triage history and an
access-control check. Production activation additionally requires an approved
deployment scope, data policy, retention/access configuration, operational owners,
thresholds, incident procedure and measured integration evidence.

## V2 sampled monitoring exercise

On all admitted synthetic trials, run applicable deterministic checks and account
for their execution coverage. Apply the frozen accepted judge to a preregistered
probability sample, logging stratum/inclusion probability; keep targeted incident
reviews separate. [V2 measurement](V2_MEASUREMENT.md) defines human prevalence,
judge-error correction, bootstrap intervals and invalid-estimate behavior.
Do not extrapolate resolved-only judgments across abstentions or assume an old
calibration transfers after cohort drift. Delayed labels, unknown inclusion
probabilities and unidentifiable correction yield missing/inconclusive evidence.

Exercise unchanged control, changed cohort, telemetry loss and delayed reference
labels with preassigned alert thresholds, destinations and triage ownership.
The demonstration creates local alert records and authorized aggregate reports;
production monitoring remains NOT_SCOPED. [CI tiers](CI_EVALUATION.md) describe
how synthetic endpoint runs feed these windows without implying deployment.
