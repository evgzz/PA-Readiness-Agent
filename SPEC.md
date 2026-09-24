# PA Readiness — v1 system specification

Version 1.0 | 2026-09-24 | DRAFT_FOR_IMPLEMENTATION

This specification consolidates the agent, harness, evaluation, instrumentation,
program-governance, and reporting requirements. It revises a scaffold; it does not
assert that these capabilities have been implemented. All ADRs remain PROPOSED. V1 adds human error analysis, evaluator calibration,
controlled improvement experiments and a synthetic monitoring exercise.

## 1. Purpose and scope

Given an authorized PA case, a selected requirement set, and case-scoped evidence,
produce a supported readiness assessment and a review packet. Preserve the
evidence needed to evaluate correctness, safety, reliability, and efficiency.
Connect evaluation findings to accountable owners, mitigations, retests, and a
candidate-specific release recommendation.

The first milestone is a bounded, synthetic, read-only PA preparation workflow.
It targets single-domain orchestration; it does not establish production maturity
or comprehensive base-model safety. Multi-domain submission and payer follow-up,
multi-agent delegation, multilingual/multimodal operation, and long-running case
management require separate scope and qualification.

| In initial scope | Outside initial scope |
|---|---|
| Fictional case inputs and explicit requirements | Real PHI or clinical eligibility determinations |
| Scoped retrieval and packet validation | Payer approval or adjudication |
| Multi-step, English-text workflow | Unqualified modality/language expansion |
| Local review packet and escalation reason | Submission, clinical writes, cancellation, external messaging |
| Independent synthetic evaluation | Claims of live deployment safety or accuracy improvements |

## 2. Users and authority

| Role | Authority |
|---|---|
| Reviewer / calling application | Submit an authorized case; inspect permitted evidence; resolve uncertainty |
| Agent policy | Propose actions and answers within the exposed catalog |
| Trusted harness | Establish scope; enforce execution policy; validate final output |
| Evaluation owner | Freeze datasets/trials; control labels; adjudicate and report results |
| Mitigation owner | Deliver a change and required closure evidence |
| Safety reviewer / release authority | Review severity and exceptions; authorize or reject a release |
| Dashboard reader | Inspect permitted projections; no implicit approval authority |

Named owners, reviewer identities, committed dates, model selections, and budgets
are unassigned. Role names in templates are responsibilities, not staffing claims.

## 3. Outcome semantics

| Layer | Values | Rule |
|---|---|---|
| Product | READY / NOT_READY / UNKNOWN | READY requires all applicable requirements supported; a confirmed blocker gives NOT_READY; otherwise unresolved required evidence gives UNKNOWN |
| Individual assertion | PASS / FAIL / UNRESOLVED | Missing observation or an unvalidated judgment is UNRESOLVED |
| Trial aggregate | PASS / FAIL / UNRESOLVED | Any demonstrated mandatory failure gives FAIL; otherwise any unresolved mandatory assertion gives UNRESOLVED; PASS requires all mandatory assertions resolved and passing |
| Run execution | NOT_RUN / RUNNING / COMPLETE / INCOMPLETE / ERROR | COMPLETE describes scheduled execution, not safety success |
| Release gate | GO / NO_GO / INCONCLUSIVE | NO_GO for demonstrated non-waived blockers; otherwise INCONCLUSIVE for missing mandatory evidence; GO only when all required gates are satisfied |
| Release authorization | PENDING / AUTHORIZED / REJECTED / EXPIRED / REVOKED | Separate authenticated human decision bound to the candidate and gate snapshot |

Preserve unresolved checks even when a confirmed blocker establishes NOT_READY
or a demonstrated failure establishes FAIL/NO_GO. `HOLD` is a dashboard display
label for INCONCLUSIVE or pending authorization; it is not a fourth gate enum.

## 4. Agent requirements

- A-01: Consume authorized case observations, tool descriptions, and bounded
  conversation state. No hidden labels, approval credentials, or unrestricted I/O.
- A-02: Select retrieval/validation steps and produce typed tool or answer proposals.
  Retrieved documents, tool returns, memory, and user text cannot grant authority.
- A-03: Preserve evidence identity, case lineage, source version, freshness, and
  availability. Distinguish confirmed absence from inability to retrieve.
- A-04: Proposed answers carry requirement-level findings, blockers, unresolved
  checks, evidence references, and a concise explanation. No fabricated citations
  or approval claims; private chain-of-thought is not an evidence requirement.
- A-05: Clarification is allowed within a trial's turn budget. Budget exhaustion
  terminates with visible unresolved work; it must not force READY.

## 5. Harness requirements

- H-01: Derive actor, tenant, patient, request, allowed operations, and destination
  from authenticated control-plane context. Agent arguments cannot replace scope.
- H-02: Select exactly one runtime loop per run. The mock loop and SDK loop are
  alternatives behind the same boundary, never nested orchestration owners.
- H-03: Every model call and tool callback passes through metering and policy
  gateways. No direct SDK-hosted tool, alternate credential, shell, browser, or
  network route may bypass this boundary in the qualified profile.
- H-04: Enforce request, time, token/cost, step, tool-call, and retry budgets. Pin
  limits in the run configuration; unknown cost is not zero cost.
- H-05: Recheck tenant/patient/request lineage and capability at the adapter.
  Validate output structure, requirement predicates, and evidence references.
- H-06: Persist proposals, decisions, dispatch attempts, receipts, and reconciled
  effects separately. Missing effect evidence remains unresolved.
- H-07: Keep consequential operations disabled initially. A future approval binds
  caller, case, operation, destination, payload digest, evidence revision, policy,
  configuration, expiry, and action state. Consume atomically; reconcile ambiguity
  before retry. Local idempotency alone cannot prove external exactly-once effects.
- H-08: Isolate sessions and trusted state. Resume only under validated identities,
  evidence freshness, configuration compatibility, and current authorization.

Detailed state, failure, and acceptance requirements: [harness](docs/HARNESS.md).

## 6. Evaluation requirements

- E-01: Preregister case families, splits, risk slices, trial schedule, reset
  procedure, graders, thresholds, stopping rules, and expected evidence.
- E-02: Send only the current authorized case input to the runtime. Hide all
  qualification answers, grader internals, and the full held-out corpus.
- E-03: Reset case and action state for independent trials; label replay versus
  live stochastic execution. Never silently substitute mocks for real failures.
- E-04: Use deterministic assertions for identity, authorization, effects, lineage,
  completeness, and duplicate actions. Use calibrated judges for semantic quality
  only where necessary, with human adjudication and disagreement records.
- E-05: Include multi-turn tool use, false READY, injection, wrong-patient access,
  unsafe tools, excessive autonomy, multi-step failures, stale evidence, and
  ambiguous outcomes. Pair attacks with legitimate positive controls.
- E-06: Report case counts, trial counts, missing/duplicate trials, error categories,
  eligible denominators, and uncertainty. Keep repeated trials grouped by case.
- E-07: Separate official benchmark scores from PA adaptations. Compare models
  with harness fixed; compare harnesses with model fixed; declare joint changes.
- E-08: Freeze selected configuration and criteria before qualification. Do not
  retune against opened held-out results and then call the same set independent.
- E-09: Support swappable judges behind JudgePort: HF Inference Endpoints for
  deployable models, supported closed APIs, and optional Jev. Freeze the selected
  profile per run and calibrate each effective configuration independently. Grade
  decision-time prefixes and full trajectories; preserve earlier failures,
  abstentions and errors. Track judge overhead separately. See
  [judge specification](docs/LLM_JUDGE.md).

See [evaluation specification](docs/EVALUATIONS.md) and the draft
[catalog](program/eval-catalog.json).

## 7. Instrumentation and reporting requirements

- I-01: Emit facts from their owning boundary: harness authorization, adapter
  receipts, evaluator verdicts, governance approvals. The agent cannot emit an
  authoritative PASS, approval, or effect confirmation.
- I-02: Use versioned event envelopes and distinct OPERATIONAL, EVALUATOR_PRIVATE,
  and PROGRAM channels. Correlation identifiers do not grant access.
- I-03: Retain complete required evaluation/action evidence in controlled stores.
  Diagnostic telemetry may be sampled; release evidence cannot depend on sampled
  traces alone. Detect failed export, missing sequence segments, and orphaned data.
- I-04: Apply explicit export destinations and payload allowlists. Synthetic-only
  is the current profile. A future local-only profile must verify both inference
  and telemetry egress controls; self-hosted dashboards alone do not prove this.
- I-05: Compute metric snapshots once from versioned definitions and source
  snapshots. The dashboard displays these results; it does not redefine formulas.
- I-06: Show coverage, execution, critical findings, mitigation progress, residual
  risk, release readiness, dependencies, and decisions required. Every metric has
  source, owner, freshness, scope, evidence class, and a drill-down path.
- I-07: Generate run scorecards, finding packets, executive reports, and release
  dossiers from the same snapshots. AI-written summaries are optional drafts;
  numeric claims must be source-linked and human-reviewed before external sharing.

See [instrumentation](docs/INSTRUMENTATION.md),
[metric registry](contracts/metric-definitions.json), and
[dashboard/report specification](docs/DASHBOARDS_REPORTS.md).

## 8. Governance requirements

- G-01: Each finding has severity, risk category, affected scope, accountable owner,
  committed date, reproducible evidence, mitigation, and measurable closure criteria.
- G-02: Closing a ticket is not evidence of mitigation. Require the original case
  retest, relevant regression and positive controls, and an authorized review.
- G-03: Separate code-based gate recommendation, runtime action approval, and
  release authorization. These are three different records and authorities.
- G-04: Exceptions have scope, rationale, controls, approver, expiry, and evidence.
  Missing mandatory evidence and critical boundary breaches are non-waivable in
  this proposed policy. Exception eligibility is evaluated, not inferred from text.
- G-05: Preserve all blockers and missing evidence even when one determines the
  overall disposition. A changed candidate, policy, or expired exception triggers
  reevaluation; previous authorization cannot silently carry forward.

Detailed proposal: [severity and release policy](governance/severity-and-release-policy.md).

## 9. Acceptance milestones

| Milestone | Required evidence | Present status |
|---|---|---|
| M0: Coherent specification | Static structure, metadata, references, archive integrity | Checked for this revision; see artifacts |
| M1: Synthetic workflow | Typed outcomes, scoped tools, bounded mock loop, full event trail | NOT_IMPLEMENTED |
| M2: Independent evaluation | Failure detection, completeness checks, calibrated semantic grading where used | NOT_IMPLEMENTED |
| M3: Program reporting | Six core metrics reconcile to evidence; gate snapshot and finding drill-down | NOT_IMPLEMENTED |
| M4: Selected real model | Pinned checkpoint/configuration, real trials, observed failure and mitigation cycle | NOT_CONFIGURED / NOT_RUN |
| M5: Qualification | Frozen held-out runs, reviewed residual risks, valid authorization record | NOT_RUN |

Numeric operational targets, model-specific sample sizes, budgets, and named
release authorities must be set before qualification. Unset values block GO.
No base-model frontier-risk, regulatory-conformance, or clinical-validity claim
follows from these application-level milestones.

## 10. V1 learning and improvement requirements

- V1-EA: Freeze a review population and sampling plan; preserve human annotations,
  taxonomy versions, disputes and failure-to-grader links.
- V1-CAL: Record domain/product-owner rubric agreement and independent reference
  labels. Audit semantic judges on an untouched calibration partition; unassigned
  criteria prevent acceptance. Qualifying labels stay outside optimizer access.
- V1-EXP: Preregister failure hypothesis, changed factors, paired workload, primary
  metric, safety limits, non-inferiority, budgets and uncertainty before execution.
  Preserve unsuccessful comparisons; selection is not release authorization.
- V1-MON: Demonstrate comparable-window monitoring, delayed labels and missing-data
  handling on synthetic runs. Operational deployment is a separate future profile.
- V1-REP: Implement Q01–Q09 alongside M01–M06, with declared denominators, uncertainty,
  missingness, source lineage and owning instrumentation points.

[V1 gap closure and acceptance](docs/V1_GAP_FIXES.md) is normative for v1. Read
[error analysis](docs/ERROR_ANALYSIS.md), [calibration](docs/EVALUATOR_CALIBRATION.md),
[experiments](docs/EXPERIMENTS.md), [monitoring](docs/MONITORING.md) and the
[worked-example contract](docs/WORKED_EXAMPLE.md). These supplement the existing
safety gates and do not replace the independent qualification requirement.
