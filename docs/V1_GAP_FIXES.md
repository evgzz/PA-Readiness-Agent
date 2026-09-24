# V1 implementation requirements and course alignment

Inherited specification baseline: 1.0 | 2026-09-24 | DRAFT_FOR_IMPLEMENTATION

[V2 requirements](V2_GAP_FIXES.md) governs the current additions and revised
acceptance criteria. This document preserves the original learning workflow.

V1 adds normative requirements to the existing agent, harness, evaluation and
governance design. It closes gaps in specification coverage; completion requires
the evidence below. No real-agent result or production capability is claimed.
The operating scope remains fictional, English-text, bounded and read-only.

## 1. Source and precedence

This revision responds to the review of the [Parlance Labs course](https://maven.com/parlance-labs/evals)
and its expanded public syllabus, inspected on 2026-09-24. Lesson mapping is an
independent assessment, not course certification. The detailed procedures and
threshold decisions below are PA project requirements, not quotations or endorsed
course assignments. Private course materials were not reviewed.

SPEC.md is the system contract. This document defines v1 completion requirements;
the linked procedures define their operation. Metric formulas are authoritative
in contracts/metric-definitions.json. Conflicts require a versioned correction,
not selection of the more favorable interpretation. Earlier revision notes are
historical. Unselected owners, budgets and thresholds remain null.

## 2. Gap closure and acceptance matrix

| ID / course area | V1 requirement | Completion evidence | Owner role / dependency |
|---|---|---|---|
| V1-01 / L1 agent construction | Execute one selected real model through the bounded harness and exactly one runtime adapter. | Pinned configuration, authorized case, actual tool/model receipts, delivered assessment and reconstructable trace; distinguish mocks from model execution. | Runtime owner / Tasks 00–05 |
| V1-02 / L2 evaluability | Reconstruct failures from admission through tool results, policy decisions, validation and final outcome. | Causal trace links and complete required ledger; a missing terminal record visibly prevents complete evidence. | Harness and telemetry owners / Tasks 03, 06 |
| V1-03 / L3 scenario coverage | Expand the three public interface examples into reviewed scenarios. Define a scenario matrix, provenance, reference outcomes and family-level splits. | Versioned manifest with counts by slice, label review, positive/negative/ambiguous cases and split-leakage check. Dataset size must follow required coverage and precision, not an arbitrary target. | Evaluation and domain owners / Tasks 01, 04 |
| V1-04 / L4 human error analysis | Review selected development traces, annotate observable failures, refine a taxonomy and prioritize action. | Frozen selection manifest, reviewer annotations, adjudication log, taxonomy version and prioritized findings linked to traces. | Evaluation and domain owners / Task 04 |
| V1-05 / L5 trusted evaluators | Convert observed failures into deterministic assertions or anchored semantic rubrics; validate automation against independent human reference decisions. | Failure-to-grader mapping, product/domain-owner rubric review, separate calibration audit, class-specific errors and accepted applicability limits. | Evaluation owner / Task 04 |
| V1-06 / L6 regression automation | Run deterministic checks on each change and real-model regression on the declared CI tier. Fail closed when a required tier is missing. | CI artifact showing a seeded regression detected, permitted positive controls preserved and missing evidence reported separately. | Engineering owner / Task 06 |
| V1-07 / L7 adversarial evaluation | Exercise injection, cross-case access, prohibited operations and excessive autonomy with positive controls. | Actual attack attempts, boundary decisions and independent effect evidence. A scripted attack proves only the scripted control path. | Safety and evaluation owners / Tasks 04–06 |
| V1-08 / L8 quality improvement | Complete a preregistered development experiment driven by a reviewed failure hypothesis. | Baseline and candidate manifests, controlled changes, paired trial schedule, uncertainty, regressions, decision and unsuccessful experiments retained. | Experiment owner / Task 07 |
| V1-09 / L9 efficiency | Compare quality, latency and fully accounted cost on the same declared workload under fixed safety constraints. | Q04–Q07 scorecard, pricing assumptions, failed-call costs, unknown-cost counts and non-inferiority criteria fixed before execution. | Experiment owner / Task 07 |
| V1-10 / operational feedback | Define monitoring windows, sampling, comparable cohorts, triage and promotion of approved failures into development data. | For v1: simulated monitoring exercise with drift and missing-data conditions. Production integration stays NOT_SCOPED until separately authorized and qualified. | Operations and evaluation owners / Tasks 06–07 |

All ten requirements are PLANNED. A completed specification does not satisfy any
runtime requirement in this matrix.

## 3. Required learning workflow

1. Declare intended behavior, risk slices and the bounded scenario matrix.
2. Execute the baseline; freeze its configuration and retain failures, errors and
   missing trials alongside successful outcomes.
3. Select traces with a reproducible sampling plan. Review development traces,
   including permitted success cases, failure cases and ambiguous evidence.
4. Record observed failure, evidence and suspected cause separately. Refine the
   taxonomy through human review; log uncertainty and taxonomy revisions.
5. Select deterministic checks where observable. For subjective judgments,
   establish expert reference labels and calibrate the rubric/judge separately.
6. Preregister a targeted change, primary metric, guardrails and comparison method.
7. Run the controlled development comparison. Record improvement, regression,
   no detectable difference or inconclusive evidence without forcing a winner.
8. Add approved development regressions. Freeze the selected candidate before
   an independent qualification set is opened. Governance computes the gate;
   an accountable authority separately records authorization.

Reviewed qualification examples never become continued tuning data while the
same evaluation is represented as held out. Feedback access is logged; a later
iteration requires a fresh independent set or an explicitly weaker claim.

## 4. Required records and procedures

| Record / procedure | Repository artifact | Required linkage |
|---|---|---|
| Trace selection, annotation and failure taxonomy | [Error analysis](ERROR_ANALYSIS.md); contracts/v1/review-batch.template.json; annotation.template.json; failure-taxonomy.template.json | Case family → trial → trace → annotation → finding |
| Rubric agreement and calibration | [Evaluator calibration](EVALUATOR_CALIBRATION.md); contracts/v1/calibration.template.json | Failure category → assertion/rubric → human reference → judge audit |
| Improvement experiment | [Experiments](EXPERIMENTS.md); contracts/v1/experiment-plan.template.json; experiment-result.template.json | Finding → hypothesis → baseline/candidate → paired results → decision |
| Feedback and monitoring | [Monitoring](MONITORING.md); contracts/v1/monitoring-plan.template.json; monitoring-window.template.json | Cohort/window → signal → human triage → finding or dismissal → approved development case |
| Worked example dossier | [Worked example](WORKED_EXAMPLE.md) | One complete chain; illustrative expectations remain distinct from observed results |

Task 00 implements validators for the existing workflow-record schemas. Their
empty templates are not executed workflows. New v2 fields and records still need
versioned schemas and validators. Null values remain unresolved requirements.
Authenticated ingress has a fail-closed contract implementation; production
authentication, durable storage, access control and runtime wiring remain pending.

## 5. Reporting requirements

Retain M01–M06 as the release/program scorecard. Add Q01–Q09 as the learning
scorecard. Q01–Q07 are required for the first complete improvement demonstration;
Q08–Q09 are required for the simulated monitoring exercise and later operational
profile. A deterministic-only evaluator may show semantic calibration as N/A
with a reviewed applicability reason, never as a successful judge calibration.

Each card must show scope, candidate/evaluation digest, evidence class, metric
version, source snapshot, timestamp, sample size, denominator or workload, missing
counts and permitted drill-down. Avoid mixing synthetic and operational evidence,
judge decisions and human reference labels, or model and harness changes.

The [dashboard specification](DASHBOARDS_REPORTS.md) maps each metric to its
tracking method and capture point. Initial reports remain JSON/Markdown generated
from snapshots. Langfuse is an optional authorized trace projection; no new vendor
is required for v1. Dashboards cannot compute their own alternate truth or expose
qualification labels through trace links.

## 6. Acceptance gates and limits

| Gate | Required evidence | Blocking conditions |
|---|---|---|
| V1-A: Reviewable baseline | Real-agent synthetic run with required scenario coverage and complete trace chain. | Unselected model, absent execution, missing receipts, mixed candidate identity. |
| V1-B: Reliable measurement | Human review records, taxonomy, deterministic assertions and applicable calibrated judges. | Unreviewed reference labels, unassigned rubric authority, failed/unconfigured calibration or leaked test labels. |
| V1-C: Improvement evidence | One complete preregistered experiment with a source-linked report. A null/negative result can complete the experiment. | Missing comparison plan, post-hoc threshold changes, omitted failed trials or fabricated performance claims. |
| V1-D: Candidate selection | Selected candidate satisfies preregistered task-quality, safety, cost and uncertainty requirements. | An inconclusive result cannot establish improvement or eligibility where evidence is mandatory. |
| V1-E: Monitoring exercise | Simulated cohort shift, unchanged control window, delayed labels and telemetry loss handled distinctly. | A missing source displayed as healthy; automatic candidate promotion or hidden-label feedback. |
| V1-F: Qualification | Independent frozen qualification, complete gates, residual-risk review and separate valid authorization. | Missing numeric limits, sample-size/precision plan, named accountable authority or mandatory evidence. |

V1-A–E establish an application evaluation demonstration within the stated scope.
V1-F is a separate release decision. None establishes clinical validity, payer
approval, regulatory conformance, comprehensive foundation-model safety, or live
production readiness. Existing READY/NOT_READY/UNKNOWN and PASS/FAIL/UNRESOLVED
semantics remain mandatory.

## 7. Delivery sequence and deferred options

Implement Tasks 00–03, then a minimal Task 04 runner. Integrate Task 05 to collect
real-agent development traces. Return to Task 04 for error analysis and calibration;
use Tasks 06–07 for CI, reports and measured changes. Do not postpone human review
until after a dashboard is built. Perform the monitoring simulation after a
baseline dataset and metric snapshots exist; deploy monitoring only in an
explicitly scoped operational profile.

Prompt revisions, retrieval corrections, tool changes, cheaper models, caching,
retry limits and model routing remain experiment candidates, not approved
optimizations. Evaluate one declared factor at a time unless an interaction design
is preregistered. Additional frameworks or custom UIs require demonstrated need.

ADR 021 covers human review; ADR 022 covers experiments; ADR 023 covers monitoring.
They remain PROPOSED. The README must link to a worked example and disclose
NOT_IMPLEMENTED/NOT_RUN status until evidence exists.
