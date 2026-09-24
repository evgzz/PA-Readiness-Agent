# Dashboard and report specification

Status: PLANNED. One candidate/release is the default reporting scope. Mixed models,
configurations, evidence classes, metric versions, or incompatible evaluation
protocols cannot silently share one aggregate.

## Views and decisions

| View | Required content | Reader decision |
|---|---|---|
| Executive overview | Gate recommendation; required coverage; critical findings; overdue mitigations; residual risks; pending authorization; decisions needed | What blocks the release and who must act? |
| Evaluation coverage | Required/executed slices; case/trial counts; PASS/FAIL/UNRESOLVED/NOT_RUN; approved exclusions; grader readiness | What must be evaluated next? |
| Findings and mitigation | Severity, owner, original/committed deadline, affected candidate, retest, regression, reopening | Is the mitigation verified and on time? |
| Candidate delivery plan | Model revision, milestones, resources, dependencies, forecast and recovery action | Is the plan feasible? |
| Evidence drill-down | Run manifest, safe trace link, assertion results, tool receipts, finding and retest lineage | What supports this result? |
| Governance | Blockers, approvals, exception scope/expiry, residual risk and gate history | Is there a valid authorization for this exact scope? |

Header: candidate/model revision, intended-use scope, configuration digest,
evidence class, reporting `as_of`, source refresh status, and metric registry version.
Filter: release, risk, domain, language, modality, context bucket, reasoning mode,
owner, and severity when those dimensions exist. No synthetic numbers fill empty cards.

## Six core metrics: definition, tracking, instrumentation

| ID / metric | Definition | Tracking and authoritative source | How/where to instrument |
|---|---|---|---|
| M01 Evidence coverage | Required slices with all declared trials and complete required evidence / required slices | Frozen coverage manifest joined to finalized results; retain case/trial completeness separately | `pa_evals.completeness`: finalize each run and recompute slice evidence; `coverage.updated` |
| M02 Delivered false-READY rate | Delivered READY on a NOT_READY/UNKNOWN reference / evaluable trials with those reference outcomes | Private adjudicated label and delivered assessment; unknown label/output contributes unresolved count, not a silent exclusion | `pa_evals.graders` after grading; `trial.graded`; companion metric measures proposed false READY |
| M03 Unauthorized actions | Separate unique prohibited proposals, blocked attempts, confirmed unauthorized effects, and unresolved effects; no single blended rate | Join action ledger to adapter receipts/world state and independent policy grading | `pa_harness.policy` before dispatch; `pa_tools.receipts` after effect/reconciliation; evaluator assigns violation verdict |
| M04 Verified mitigation closure | Findings requiring mitigation and currently closed with valid verification / all findings requiring mitigation in the declared cohort | Versioned findings plus original failure, retest, regression, positive-control evidence and reviewer decision | `pa_governance.findings` at state changes; closure request validates evidence before transition |
| M05 Overdue mitigations | Open mitigation findings whose current committed deadline precedes `as_of` | Finding history; show original deadline, extensions, unknown/unassigned deadlines separately | `pa_governance.program_metrics` on changes and at least daily; do not store overdue as a manual flag |
| M06 Release readiness | Independent GO/NO_GO/INCONCLUSIVE recommendation with all blockers/missing evidence; separate authorization | Candidate-bound gate policy, metrics, findings, exceptions and authorization snapshot | `pa_governance.release_gate` on relevant changes; reporting reads the resulting snapshot |

The detailed machine-readable contract is `contracts/metric-definitions.json`.
For M01, a completed failing evaluation may establish coverage; complete evidence
does not imply a pass. Missing receipts make evidence incomplete. An unresolved
semantic judgment may have complete raw evidence; report judgment resolution
separately and keep the release gate inconclusive where it is mandatory.

For M02, show numerator, eligible denominator, unresolved count, total scheduled
trials, and reference-label class. This rate differs from false READY divided by
all READY predictions; if the latter is useful, name it explicitly as an additional
metric. Do not switch denominator definitions between reports.

For M03, proposal/attempt/effect are different units. If a rate is added, freeze
its opportunity denominator. Read/disclosure violations count as effects.
For M04, a growing finding cohort can change the percentage; expose cohort size
and fixed-cohort trends. Reopened findings leave the numerator immediately.

## Additional measurements to activate when evidence exists

| Measurement | Required interpretation |
|---|---|
| Legitimate task completion and over-refusal | Safety blocks paired with permitted positive controls |
| Repeat-run reliability | All-required-trials success per case, separately from per-trial success |
| Judge quality | Calibration n, class-specific errors, disagreement and adjudication |
| Efficiency | End-to-end latency, retries, tokens, tool costs, failed calls, review cost assumptions |
| Evidence health | Missing records, duplicate collisions, stale sources, exporter backlog |
| Residual risk | Exposure, scope, compensating controls, accountable acceptance, expiry |

No numeric thresholds are invented. Required thresholds, minimum sample sizes,
confidence rules, freshness limits, and owners are null until preregistered.
Null thresholds prevent a qualification GO. A zero denominator yields N/A, not 0%.

## Refresh and interaction requirements

- Evidence/run metrics update after validated run finalization; provisional data
  is visibly marked and excluded from release qualification.
- Findings refresh on authoritative version changes; overdue status also advances
  with time. Alert frequencies and escalation deadlines are deployment parameters.
- Gate recomputes on candidate, evidence, finding, policy, or exception changes
  and gate-relevant expiry boundaries. Reuse its snapshot when substantive inputs
  are unchanged. Approval/revocation/authorization expiry updates the separate
  authorization display; it does not change the gate snapshot being authorized.
  Historical snapshots never change in place.
- Every card shows source/version and computed time; a failed source refresh
  shows STALE/ERROR with last-good time. Missing findings is not zero findings.
- Authorized readers may drill down. Report links must enforce access at the
  destination; a shared correlation ID is not authorization.

## Report outputs

| Report | Trigger | Minimum fields |
|---|---|---|
| Run scorecard | Finalized evaluation | Candidate/eval digests, scope, scheduled/completed/valid counts, failures, unresolved, metrics, evidence links |
| Finding packet | New or changed finding | Reproducer, impact, severity rationale, owner/date, mitigation, closure criterion, retest/regression/positive controls |
| Executive brief | On demand or configured cadence | Release recommendation, coverage gaps, critical findings, overdue actions, residual risks, dependencies and decisions required |
| Release dossier | Candidate review | Frozen configuration, scope, gate policy/results, unresolved findings, exceptions, approvals, rollback/monitoring plan |

Proposed outputs: `reports/<snapshot>/scorecard.json`, `scorecard.md`,
`executive-brief.md`, and `release-dossier.md` in controlled artifact storage.
Commit only approved synthetic summaries. No report is generated by this scaffold.

## Delivery options and proposed first choice

Start with deterministic CI/Markdown scorecards and versioned program records.
Optionally use GitHub Projects for day-to-day finding ownership; export a versioned
snapshot for each gate. Add native Langfuse views for technical investigation when
runtime tracing exists. Use its supported APIs rather than private platform tables.

Metabase over curated PostgreSQL views is an executive reporting alternative;
Grafana over a project-owned ClickHouse reporting schema is an operational option.
Braintrust and Arize Phoenix remain observability alternatives. A custom reporting
UI becomes worthwhile when these choices cannot satisfy access or workflow needs.
See ADRs 006, 011, 017, and 018 for trade-offs and reevaluation triggers.

## V1 learning scorecard: tracking and instrumentation

All locations below are proposed modules. Q01–Q07 are required for the first
complete improvement demonstration; Q08–Q09 for the synthetic monitoring exercise.
N/A needs an applicability reason; unconfigured required evidence remains unresolved.

| ID / measure | How to track / authoritative source | How and where to instrument | Dashboard/report |
|---|---|---|---|
| Q01 human review coverage | Frozen review-batch manifest and latest valid annotation versions. selected distinct trials with completed review / all selected distinct trials in frozen review batch | `evals/src/pa_evals/review.py`; `review.batch.created`, `review.annotation.recorded`, `review.adjudicated` after persisted state changes | Human review queue: reviewed/selected; pending, unreviewable, disputed; population and selection method. |
| Q02 failure category incidence | Review-batch manifest, versioned taxonomy, coding and adjudication records. distinct coded trials assigned category / all reviewable coded distinct trials in declared batch | `evals/src/pa_evals/review.py`; `review.annotation.recorded`, `review.adjudicated`, `taxonomy.versioned` after persisted state changes | Failure analysis by category, severity and slice with sample denominator and trace links. |
| Q03 evaluator reliability | Frozen calibration audit, original human labels, adjudicated references and judge decisions. Independent adjudicated reference; untouched calibration audit; fixed judge/rubric; class counts and uncertainty. | `evals/src/pa_evals/calibration.py`; `rubric.reviewed`, `calibration.finalized` after persisted state changes | Calibration: confusion counts, class-specific FPR/FNR, disagreement, coverage and disposition. |
| Q04 legitimate task completion | Frozen eligible legitimate trial schedule and finalized independent assertion verdicts. scheduled eligible legitimate trials meeting all required task and safety assertions / all scheduled eligible legitimate trials in frozen schedule | `evals/src/pa_evals/metrics.py`; `trial.graded`, `run.finalized` after persisted state changes | Task quality: success/assigned, failure, missing, unresolved, correct escalation and over-refusal counts. |
| Q05 terminal latency | Trusted admission and terminal records with declared duration boundary. Same admission-to-terminal boundary, load, cache, concurrency, warm-up and workload; all terminal outcomes, with successful-only view separate. | `evals/src/pa_evals/metrics.py`; `run.completed`, `run.finalized` after persisted state changes | Latency p50/p95, terminal count, success/error/timeout split, missing/censored count. |
| Q06 runtime cost per success | All model/tool usage attempts for Q04 workload, receipts and versioned pricing assumptions. total runtime cost of all scheduled eligible workload trials including failed calls, retries, tools and fallbacks / successful legitimate tasks in the same workload | `evals/src/pa_evals/metrics.py`; `model.call.completed`, `effect.observed`, `run.finalized` after persisted state changes | Total and cost/success, tokens, retries, tools, failure costs, unpriced calls and pricing assumptions. |
| Q07 paired experiment comparison | Preregistered experiment plan, paired run manifests and finalized metric snapshots. Preregistered paired family-aware design; frozen baseline/candidate, primary outcome, guardrails, uncertainty and stopping rule. | `evals/src/pa_evals/comparisons.py`; `experiment.registered`, `experiment.finalized` after persisted state changes | Baseline/candidate deltas, uncertainty, guardrails, sample sizes, cost completeness and selection decision. |
| Q08 monitoring evidence coverage | Independent admission manifest joined to required evidence and monitoring-window snapshot. eligible admitted runs with complete required records for window / all eligible admitted runs from independent admission source | `evals/src/pa_evals/monitoring.py`; `monitoring.window.finalized` after persisted state changes | Window eligible/complete, missing, late, label-pending, source age and review backlog. |
| Q09 behavior change signal | Comparable reference/current snapshots, label provenance, signal method and triage history. Comparable reference/current cohorts; label maturity, method, cadence and repeated-testing controls; proxies distinct from verified quality. | `evals/src/pa_evals/monitoring.py`; `monitoring.window.finalized`, `monitoring.alert.updated` after persisted state changes | Reference/current change and uncertainty, confirmed/proxy signal, triage owner/state and linked findings. |

Review queue and category views use private annotation projections. Calibration
views show class errors and unresolved labels. Experiment reports bind hypotheses,
plans and both candidate snapshots. Monitoring views distinguish actual quality
labels from proxies and stale evidence. No card is populated with sample results.

Add reports/<snapshot>/review-summary.md, calibration-report.md,
experiment-report.md and monitoring-report.md, alongside JSON snapshots. Each
contains counts, missingness, method, scope, versioned evidence references, reviewer
disposition and next action. Raw examples require access checks at the destination.

Learning metrics do not silently become release thresholds. The selected profile
declares mandatory criteria before execution. Unknown cost yields an incomplete
cost total; targeted sample frequency is not an operational failure estimate.
A negative experiment can be complete while its candidate is rejected.

## Jev judge tracking

Status: PLANNED. Q03/Q07 can link these detailed audit/comparison reports; the table
does not extend today's metric payload schema or establish new release thresholds.
A versioned report/record contract is required before these cards are populated.

| Dashboard measure | How to track / denominator | How and where to instrument |
|---|---|---|
| Human alignment (Q03) | Confusion counts by criterion/slice; false pass = FN/(TP+FN), false fail = FP/(FP+TN) on resolved prediction/reference pairs. Show total human-labeled failures/passes and unresolved predictions in each class separately. | pa_evals.calibration joins immutable judge results to independent adjudicated labels; calibration.finalized references the persisted audit |
| Decision coverage and abstention (Q03) | Accepted PASS/FAIL / applicable scheduled judgments; separate uncertain, invalid, missing, unaccepted and unadjudicated counts. Show total scheduled and valid raw answers. | pa_evals.judges persists mapping reason and calibration reference; pa_evals.completeness reconciles the frozen judgment schedule |
| Probability calibration (Q03 detail) | Noul Brier score and preregistered reliability bins on valid labeled probabilities, including threshold abstentions; expose sample size and excluded/unlabeled counts | pa_evals.calibration uses raw p and human failure label; persist method/bin version and case-family uncertainty |
| Fixed-trace repeatability (Q03 detail) | Within-case score variance and verdict disagreement across declared repetitions; unique cases, families and repeats shown separately | pa_evals.runner replays fixed evidence/question digests; pa_evals.calibration groups by case, criterion and judge version |
| Trajectory quality | Prefix assertion outcomes, correction/recovery outcomes and full-trajectory verdict; incomplete traces and unresolved judgments visible | pa_evals.trajectories captures causal prefixes, state/evidence revisions and completeness; pa_evals.judges links each judgment to its window |
| Judge latency and errors | p50/p95 logical judgment latency including retries, per-attempt duration and error counts; report timeouts and incomplete requests separately | pa_models.jev records attempt timing/errors; evaluation gateway measures total duration and retry budget |
| Judge spend | Total known evaluation spend including failed/retried calls, unknown-cost count and known spend / completed judgments; incomplete cost totals labeled | pa_models.jev retains provider usage; evaluation gateway joins versioned pricing once per request/attempt; batched questions do not duplicate charges |
| Jev/challenger comparison (Q07) | Paired unique-case alignment, coverage, repeatability and overhead; missing pairs explicit | pa_evals.comparisons consumes preregistered experiment and frozen result snapshots; experiment.finalized links the comparison |

These judge overhead measures remain separate from runtime Q05 latency and Q06
cost per success. Filters bind candidate/eval/model/rubric/context/threshold versions
and evidence class. Do not plot confidence as measured accuracy. Case IDs belong
in evidence links, not unbounded metric labels. No data displays NOT_RUN, never 0.

Add reports/<snapshot>/jev-judge-report.json and .md when implemented: selection,
calibration disposition, unique case/repetition counts, uncertainty, errors,
missingness, model/version limits, private evidence links and reviewer action.
Langfuse receives permitted projections; optional LangSmith comparisons require
an approved export profile. Neither platform computes release authority.
