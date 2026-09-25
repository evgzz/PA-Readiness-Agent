# Phased delivery plan

Plan revision: 1.1 | System specification: 2.1 | Status: SPECIFIED

This plan sequences small, executable increments so behavior can be tested before
the full system is built. It implements [SPEC](../SPEC.md) and the
[v2 requirements](V2_GAP_FIXES.md), with the explicit 2.1 dependency amendment in
[qualification profiles](QUALIFICATION_PROFILES.md). Full-program requirements and
all applicable candidate safety/quality criteria remain mandatory.
No new runtime execution is claimed by publishing this plan.

The original contract foundation is complete. Phases P1–P7 are PLANNED; entry
checks and acceptance runs are not yet recorded. P1 is next. Accountable names
and dates remain unassigned. They must be set when needed for execution or review;
their absence does not prevent reversible local preparation.

The [phase tracker](PHASE_STATUS.json) is the authoritative phase-status record.
[Build status](BUILD_STATUS.json) describes implementation capability, and the
[v2 acceptance index](v2-acceptance.template.json) tracks full-system evidence.
These are different views; none should be inferred from another's headline status.

## Status and gate rules

| Field | Meaning |
|---|---|
| PLANNED | Increment specified; implementation/completion is not claimed. |
| IN_PROGRESS | Work has begun; required evidence remains incomplete. |
| BLOCKED | A recorded unmet dependency prevents the next required execution or acceptance step. Preserve the blocking reason and resumption action. |
| COMPLETE | All applicable entry/exit/DoD criteria have evidence for the declared scope. It does not mean the candidate improved or qualifies for release. |
| Entry / exit / DoD assessment | NOT_ASSESSED, MET, UNMET or NOT_APPLICABLE with a reason; these are planning fields, not runtime verdict enums. |

Entry criteria define what must be established before the phase's acceptance
execution. Preparation and diagnosis can start earlier. Exit criteria define the
observable result required to close the increment. Definition of done (DoD) adds
reproducibility, integration, documentation and handoff obligations.

A phase completes only when its entry, exit, phase-specific DoD and applicable
common DoD are met. Non-applicability requires an explicit scope rationale and
review record; it cannot waive a mandatory v2 requirement. P0 records historical
completion under its original scope; new DoD requirements apply to P1 onward.
Negative experiments may be complete evidence while adoption remains rejected.
P7 may conclude NO_GO or INCONCLUSIVE; its procedural completion never converts
that outcome into release eligibility. P7 can complete with an unfavorable
decision only when its required execution and procedural records exist. A missing
mandatory run leaves the phase incomplete; an executed assessment with insufficient
statistical certainty can be complete while release remains INCONCLUSIVE.

Use existing product READY/NOT_READY/UNKNOWN, assertion PASS/FAIL/UNRESOLVED and
release GO/NO_GO/INCONCLUSIVE semantics. Stop or contain affected execution after
an authority, identity or evidence-integrity breach. Keep diagnostic review and
safe local work available; do not rewrite history or silently weaken criteria.

## Phase summary

| Phase | Current status | Entry requirement | Exit gate | Existing task slices |
|---|---|---|---|---|
| P0 — Contract foundation | COMPLETE — original contracts only | Original contract baseline recorded | Contract tests and packaging evidence recorded | 00 |
| P1 — Executable synthetic workflow | PLANNED — next | P0, reviewed predicates, rules-only and separate mock profiles | Actual rules-only outcomes, denied scope/write controls, reproducible traces | 00, 01, 02, 03, 04 |
| P2 — Failure handling and regression | PLANNED | P1 plus failure/property/replay matrix | Controls pass, deliberate violations fail, replay misses cannot call live tools | 00, 01, 03, 04, 06 |
| P3 — One-model architecture comparison | PLANNED | P2, one provider and frozen A/B/C protocol | Three actual candidates compared, B extraction audited, all attempts retained | 00, 01, 03, 04, 05 |
| P4 — Human review and trusted measurement | PLANNED | P3 traces plus frozen sampling, human references and audit criteria | 60-trace review, defensible taxonomy and accepted applicable evaluators | 00, 04, 05 |
| P5 — One measured fix and adversarial regression | PLANNED | P4, observed failure and diagnosis/comparison plans | Diagnosis, full-system fix, measured selection, attack regressions; utility evidence before claims | 00, 03, 04, 05, 06, 07 |
| P6 — Reporting, efficiency and synthetic monitoring | PLANNED | P5 plus separately registered subphase plans and required integrations | All five subphases and the V2-A–D evidence index complete | 00, 04, 05, 06, 07 |
| P7 — Independent qualification and release decision | PLANNED | P5/P6A/P6E plus frozen profile and every triggered dependency; all P6 for full-program profile | Candidate-bound assessment, separate authorization and full-program status | 04, 06, 07 |

Phases are delivery increments; Tasks 00–07 remain component work packages. A
phase can implement a slice of several tasks without completing those tasks.
Add contract extensions when the next increment needs them, before their use.
Keep future adapters, databases and services deferred until a concrete phase
requires them. All phases retain fictional data and disabled external effects.

## Revised execution path and decisions

P1 builds candidate A and separate mock controls; P2 adds property tests and recorded
tool replay; P3 compares A/B/C with one model; P4 establishes trusted measurement;
P5 diagnoses/fixes an observed failure and remeasures the alternatives. The human
utility study is required before utility claims; otherwise retain an explicit
NOT_RUN claim-deferral record. See [comparison protocol](ARCHITECTURE_COMPARISON.md).

After P5, complete P6A reporting and P6E synthetic monitoring, then P7 under a frozen
[qualification profile](QUALIFICATION_PROFILES.md). Used caching, routing or a
model/serving replacement adds P6B, P6C or P6D respectively. Unknown applicability
blocks qualification. Initial qualification may precede experiments on verified
unused features; those remain PLANNED and full-program acceptance stays incomplete.
FULL_V2_PROGRAM still requires all P6 subphases and V2-A–D. This is the explicit
plan 1.1/specification 2.1 dependency amendment, not an implicit waiver.

No architecture or profile is selected yet. All added criteria are NOT_ASSESSED;
no dates, thresholds, reviewers, gains or live results are invented.

## Common definition of done

| ID | Requirement | Evidence obligation |
|---|---|---|
| DOD-01 | Scope and configuration are explicit | Pin the code/config/data/requirement identities for the increment, its operations, budgets and evidence class. Record applicable schema extensions and dependencies. |
| DOD-02 | Required checks execute | Provide meaningful positive, negative and missing-evidence controls. Record exact commands and outcomes. A skipped mandatory check or missing observation cannot satisfy acceptance. |
| DOD-03 | Evidence is reproducible | Keep the input/world/reset manifest, attempts/receipts, delivered result, evaluator output and report linked by stable IDs and integrity digests. Retain errors and unsuccessful runs. |
| DOD-04 | Authority and labels stay separated | Preserve trusted scope and gateway enforcement. Keep hidden labels, judge internals, credentials and release authority outside agent access. |
| DOD-05 | Status matches implementation | Update only completed portions of component/task status. Keep mocks, real synthetic runs and qualification distinct. A green CI run proves only its executed checks. |
| DOD-06 | Handoff is usable | Commit the implementation/config/docs, setup and reproduction instructions; record evidence author, review disposition, remaining defects and the next bounded increment. |
| DOD-07 | Mandatory limitations remain visible | Report unresolved criteria, unknown costs, sampling limits and affected slices. Reopen impacted acceptance after material code/model/prompt/tool/policy/evaluator changes. |
| DOD-08 | Acceptance does not authorize deployment | Phase completion means its scoped evidence and procedural requirements are met. Candidate adoption, release recommendation, authenticated authorization and deployment are separate decisions. |

## P0 — Contract foundation

Status: COMPLETE_FOR_ORIGINAL_CONTRACT_LAYER | Owner roles: Engineering.

Completed original contracts, packaging and fail-closed ingress validation. This baseline does not include v2 record extensions or an executable agent.

### Entry criteria

- **P0-ENTRY-01:** Original contract interfaces, schema vocabulary and synthetic configuration are recorded in the Task 00 handoff.

### Exit criteria

- **P0-EXIT-01:** The original contract boundary suite passes: 25 tests, including malformed scope, forged producer/channel, hidden-label projection and outcome precedence.
- **P0-EXIT-02:** Package installation and the installed configuration command have recorded successful results.

### Definition of done

- **P0-DOD-01:** Task 00 implementation scope, executed evidence and integration limitations are documented.
- **P0-DOD-02:** Runtime, transport authentication, real models and evaluation remain explicitly pending; historical counts retain their original revision context.

**Required evidence:** artifacts/TASK00_VALIDATION.json; docs/TASK00_HANDOFF.md.

**Deferred:** All agent behavior, runtime wiring, v2 schemas and live integrations.

**Corresponding specs:** [TASK00_HANDOFF](TASK00_HANDOFF.md).

## P1 — Executable synthetic workflow

Status: PLANNED | Owner roles: Engineering, Evaluation.

One reviewed fictional PA requirement set, three core cases, scoped read-only tools and a genuine rules-only candidate A. Keep the deterministic mock/loop as a separate integration control. Add a minimal independent code grader and local JSON/Markdown outputs; implement only the schema extensions these paths need.

### Entry criteria

- **P1-ENTRY-01:** P0 evidence is available; the existing package and configuration can be used in the implementation environment.
- **P1-ENTRY-02:** Define the fictional requirement predicates and review the three expected outcomes before treating the public examples as acceptance cases.
- **P1-ENTRY-03:** Declare the allowed operations, case identity source, loop/retry/time budgets and required event fields. Keep external effects and optional exporters disabled.

### Exit criteria

- **P1-EXIT-01:** A documented local command runs candidate A over authorized facts for SYN-001, SYN-002 and SYN-003 through actual tool/harness code and returns READY, NOT_READY and UNKNOWN under reviewed predicates; scripted mock controls are separately identified.
- **P1-EXIT-02:** Every admitted case has scope, reset, tool result, proposed/delivered answer, verdict and terminal evidence; references resolve to the same case.
- **P1-EXIT-03:** A foreign-case read and an unsupported write proposal are denied at the execution boundary while a permitted read succeeds. Replaying after reset reproduces the deterministic behavioral result.
- **P1-EXIT-04:** Rules-only decisions derive from source facts and versioned predicates, never case-ID answer tables or evaluator labels; missing/unverified required support follows product precedence and cannot establish READY.

### Definition of done

- **P1-DOD-01:** The command, sample configuration and setup work from a clean checkout; output locations and limitations are documented.
- **P1-DOD-02:** Independent assertions evaluate delivered results without sending expectations into the runtime. Record candidate kind, actual predicate execution and evidence class; REFERENCE_CONTROL for A is distinct from SCRIPTED_DEMO/mock controls and is not a qualification claim.
- **P1-DOD-03:** Required event/payload extensions are versioned and validated before emission; malformed input and missing evidence remain visible.
- **P1-DOD-04:** Commit the scoped implementation, meaningful boundary tests and evidence index; update component/task status only for the implemented portions.

**Required evidence:** Reviewed requirement/case manifest; Reset receipts and case-scoped tool receipts; Three complete traces and assessments; Deterministic assertion results; JSON/Markdown scorecard and reproduction command; Rules-only predicate/source manifest and separately identified mock controls.

**Deferred:** Real providers, semantic judges, large datasets, persistent databases, trace-platform deployment and a dashboard application.

**Corresponding specs:** [SYNTHETIC_SCENARIOS](SYNTHETIC_SCENARIOS.md), [HARNESS](HARNESS.md), [INSTRUMENTATION](INSTRUMENTATION.md), [ARCHITECTURE_COMPARISON](ARCHITECTURE_COMPARISON.md).

## P2 — Failure handling and regression

Status: PLANNED | Owner roles: Engineering, Evaluation.

Extend the runnable path with fault/attack controls, independent completeness checks, multi-turn reference scenarios and T0/T1 CI.

### Entry criteria

- **P2-ENTRY-01:** P1 exit and DoD evidence is recorded for a fixed baseline.
- **P2-ENTRY-02:** Freeze a failure matrix with intended outcomes, initial state, applicable assertions and evidence requirements; isolate control fixtures from runtime expectations.
- **P2-ENTRY-03:** Freeze reviewed metamorphic relations and synthetic replay fixtures with request, scope, tool/version and initial-state identities; declare each port mode and keep labels out of fixtures.

### Exit criteria

- **P2-EXIT-01:** All mandatory reference controls resolve correctly: wrong-patient access, prohibited operation, unsupported READY, tool absence versus outage, malformed output, cancellation/budget exhaustion, missing terminal record and duplicate trial.
- **P2-EXIT-02:** Multi-turn controls cover clarification, contradictory/stale evidence, correction and reset isolation. A later correction does not erase an earlier mandatory failure.
- **P2-EXIT-03:** A deliberately introduced development defect fails the required CI check. Restoring the fix passes the original case and legitimate controls; a skipped/incomplete required tier cannot pass.
- **P2-EXIT-04:** Property/metamorphic controls exercise irrelevant reordering, required-support removal, scope denial and reset isolation; deliberate violating implementations are detected, with transformed-case semantics independently reviewed.
- **P2-EXIT-05:** Recorded tool replay rechecks authorization and exact canonical request/state identity. Miss, mismatch, exhausted sequence and tamper are explicit errors/incomplete evidence with no live fallback; replay receipts preserve provenance and reset order.

### Definition of done

- **P2-DOD-01:** T0/T1 run on applicable changes with bounded execution and preserved failure output; optional integration credentials are unnecessary for these tiers.
- **P2-DOD-02:** Reports count scheduled/completed/missing/duplicate trials separately; absence of observations is never a healthy zero.
- **P2-DOD-03:** The original failure, regression case and repair evidence are linked; reference controls are not represented as live exploits or model performance.
- **P2-DOD-04:** Review import/data boundaries and update scaffold-only assertions as real components become implemented; do not retain false NOT_IMPLEMENTED checks.
- **P2-DOD-05:** Commit relation/fixture manifests and detected-defect evidence; distinguish replay, mock and live ports, and do not report replayed provider behavior or historical costs as new live performance.

**Required evidence:** Failure/positive-control matrix; Seeded failing CI run and repaired run; Multi-turn reference traces; Completeness/reset results; Updated reproduction instructions; Metamorphic pairs, seeded violations and replay match/miss/isolation controls.

**Deferred:** Semantic judges, real-model performance claims and statistical population estimates.

**Corresponding specs:** [CI_EVALUATION](CI_EVALUATION.md), [EVALUATIONS](EVALUATIONS.md), [HARNESS](HARNESS.md), [ARCHITECTURE_COMPARISON](ARCHITECTURE_COMPARISON.md).

## P3 — One-model architecture comparison

Status: PLANNED | Owner roles: Engineering, Evaluation.

Compare rules-only A, fixed extraction workflow B and bounded agent C using the same authorized source evidence and one pinned model/provider for B/C. Keep a single selected loop per run and the same enforcement gateways. Expand reviewed families and collect a bounded development pilot; selection remains provisional until P4/P5 measurement.

### Entry criteria

- **P3-ENTRY-01:** P2 required controls pass. Establish synthetic-only process/credential/data boundaries and permitted inference/export destinations before network execution.
- **P3-ENTRY-02:** Select and pin the provider/model/serving configuration and required dependencies; configure credentials without storing values in Git. Record hosted-model immutability limits.
- **P3-ENTRY-03:** Preregister pilot cases, repetitions, budgets, stopping rules and manual review assignments. Group families before augmentation; reserve future qualification families and keep labels outside runtime access.
- **P3-ENTRY-04:** Validate actual rendered-prompt/config identities, required nested spans and missing-trace controls locally. Leave unconfigured exporters disabled.
- **P3-ENTRY-05:** Freeze the A/B/C comparison protocol, shared eligible cohort and full-workload coverage, preprocessing/labor accounting and actual candidate/config identities; disclose bundled changes rather than claiming a pure architecture effect.

### Exit criteria

- **P3-EXIT-01:** Actual provider calls execute through the metered gateway with one runtime loop, scoped tool callbacks and no silent mock/model fallback. Authorization controls also pass under hostile proposals through this adapter.
- **P3-EXIT-02:** Every scheduled attempt is accounted for, including errors, retries, timeouts and usage/pricing gaps. Manually inspect every pilot trace and preserve observed failures.
- **P3-EXIT-03:** Actual multi-turn runs include clarification, correction, unavailable evidence and budget termination. Separate attempted from delivered answers and decision-time prefixes from full trajectories.
- **P3-EXIT-04:** Record the scenario generator/world provenance, family splits, reviewed smoke report and a prioritized development backlog. Close code-enforcement defects before expanding live execution.
- **P3-EXIT-05:** Execute all three candidates on the declared shared development workload, preserve every scheduled trial and report safety, success, coverage, abstention, trajectory failures, latency and full costs with uncertainty; no winner is forced.
- **P3-EXIT-06:** Independently inspect B extraction grounding: schema validity or a resolving citation alone cannot establish support. Test erroneous extraction, ambiguity and missing evidence through final readiness checks.

### Definition of done

- **P3-DOD-01:** Persist code/config/model/data digests, source snapshots, receipts, candidate kind and trace links. Label actual B/C runs REAL_AGENT_SYNTHETIC and actual A predicate runs REFERENCE_CONTROL; never claim model execution for A or live evidence for mocks/replay.
- **P3-DOD-02:** Publish an initial scorecard for outcomes, safety assertions, completeness, latency and cost, with denominators and unknowns. No pilot sample is called a precision guarantee.
- **P3-DOD-03:** Reproduction instructions include required configuration, environment and provider limits; missing configuration makes zero network calls.
- **P3-DOD-04:** Assign owners and reproduction steps to material failures. Review may continue while an execution defect is blocked, without claiming phase completion.

**Required evidence:** Pinned pilot plan and environment manifest; Reviewed scenario smoke report; Actual provider/tool receipts and multi-turn traces; Manual pilot annotations; Initial quality/cost/completeness report and failure backlog; A/B/C paired development report, input/labor accounting and B extraction audit.

**Deferred:** Multiple provider integrations, model cascades, automatic judging and large-scale optimization. Hosted tracing is deferred until its integration controls pass; local evidence remains mandatory.

**Corresponding specs:** [SYNTHETIC_SCENARIOS](SYNTHETIC_SCENARIOS.md), [INSTRUMENTATION](INSTRUMENTATION.md), [LLM_JUDGE](LLM_JUDGE.md), [ARCHITECTURE_COMPARISON](ARCHITECTURE_COMPARISON.md).

## P4 — Human review and trusted measurement

Status: PLANNED | Owner roles: Evaluation, PA domain reviewer.

Human-owned failure discovery, review interface, binary evaluators, repeatability/uncertainty computation and one semantic judge only where required by the observed failure modes.

### Entry criteria

- **P4-ENTRY-01:** P3 supplies actual development traces and stable trace identities. Freeze the review population, probability/targeted sampling labels, batch size and saturation stopping criterion.
- **P4-ENTRY-02:** Assign qualified reference reviewers and adjudication responsibility. Define label access, related-family partitioning and untouched calibration audit boundaries.
- **P4-ENTRY-03:** Before a judge audit, assign the rubric, class/slice minimums, error/coverage bounds, uncertainty method and profile pins. Null criteria block acceptance, not useful preparation.

### Exit criteria

- **P4-EXIT-01:** Review at least 60 distinct reviewable real-agent synthetic development traces. Preserve first-failure notes, secondary failures, recovery, disagreements, unreviewable cases and saturation history.
- **P4-EXIT-02:** Produce human-derived binary failure definitions and one testable evaluator per observed mode. Aim for 5–8 modes when supported; justify another count rather than inventing failures.
- **P4-EXIT-03:** Required semantic judges pass their untouched human-reference audit, including TPR/TNR, class counts and unresolved coverage. If no semantic judge is needed, record reviewed applicability and do not claim successful judge calibration.
- **P4-EXIT-04:** Verify fixed-k pass^k/pass@k, missingness bounds, weighting and prevalence/uncertainty behavior against independent known-result controls. Invalid or sparse estimates remain inconclusive.

### Definition of done

- **P4-DOD-01:** Commit versioned codebook/rubrics and allowed aggregate reports; keep private labels and qualification material in their controlled store.
- **P4-DOD-02:** The review UI exposes complete permitted traces, hides judge output before initial human labeling and supports append-only review/adjudication.
- **P4-DOD-03:** Selected judge profile, context projection, parsing/abstention policy and audit digest are frozen. Jev is optional; HF-hosted and supported closed API profiles use the same acceptance discipline.
- **P4-DOD-04:** Preserve tests for anti-hindsight, valid alternative paths, earlier failure plus later recovery, missing context and uncalibrated swaps. No judge can override objective effect/authorization evidence.
- **P4-DOD-05:** The 60-trace floor counts only distinct reviewable actual B/C agent/model development trajectories, not deterministic A or replay/mock runs. Recheck retained A/B/C comparisons with accepted evaluators before P5 selection.

**Required evidence:** Review selection and 60-trace accounting; Versioned taxonomy, batch/saturation and adjudication reports; Failure-to-evaluator mapping; Calibration report or justified non-applicability; Reliability/prevalence computation controls and report.

**Deferred:** All-backend judge support, autonomous taxonomy creation, automated optimization and weights training.

**Corresponding specs:** [ERROR_ANALYSIS](ERROR_ANALYSIS.md), [EVALUATOR_CALIBRATION](EVALUATOR_CALIBRATION.md), [V2_MEASUREMENT](V2_MEASUREMENT.md), [LLM_JUDGE](LLM_JUDGE.md), [ARCHITECTURE_COMPARISON](ARCHITECTURE_COMPARISON.md).

## P5 — One measured fix and adversarial regression

Status: PLANNED | Owner roles: Engineering, Evaluation, Safety review.

Diagnose one observed failure with an isolated component experiment, implement a manual fix, remeasure retained A/B/C alternatives under accepted evaluators, and run actual synthetic red-team/development regressions. Add human-only versus assisted review before making productivity or time-saving claims.

### Entry criteria

- **P5-ENTRY-01:** P4 supplies a supported failure hypothesis and accepted applicable evaluators. If no defensible failure is observed, record that result and broaden review before claiming a completed fix.
- **P5-ENTRY-02:** Preregister baseline/candidate configurations, changed factor, paired workload, sample/repetition plan, primary metric, safety/non-inferiority limits, cost budget and stopping rule.
- **P5-ENTRY-03:** Configure the owned synthetic endpoint, pinned red-team adapter, allowlisted generation/target/grading destinations and independent effect checks; irreversible operations remain disabled.
- **P5-ENTRY-04:** Preregister the observed-failure component hypothesis and safe isolation; declare whether human utility claims are sought, with qualified participants and a matched/counterbalanced study plan when required.

### Exit criteria

- **P5-EXIT-01:** The comparison preserves all scheduled trials and reports improvement, regression, no detectable difference or inconclusive evidence under the frozen rules. A negative result can complete the experiment, but cannot justify adopting its candidate.
- **P5-EXIT-02:** Run the actual endpoint attack campaign with legitimate controls. For every confirmed successful attack, retain a reproducer, failing regression, mitigation and retest; record a no-success campaign honestly.
- **P5-EXIT-03:** The retained candidate has no unresolved mandatory authorization/lineage defect and satisfies the declared advancement constraints; failures remain in the backlog.
- **P5-EXIT-04:** Required T0–T2 checks run for the selected change types; missing credentials/tier evidence remain visibly incomplete. Findings link to owners, closure criteria and actual retests.
- **P5-EXIT-05:** Complete one bounded component diagnosis/ablation and an independent full-system fix retest. Never bypass actual authorization/label isolation; evaluator-only oracle substitutions are diagnostic, not candidate performance.
- **P5-EXIT-06:** Remeasure retained A/B/C alternatives with accepted evaluators and preserve all constraint outcomes, losing results and uncertainty. Select only a supported eligible candidate or retain an eligible baseline without claiming an unsupported win.
- **P5-EXIT-07:** Before any human productivity claim, complete the preregistered human-only/assisted comparison of decision quality, missed blockers, unsupported claims, corrections and total time; otherwise record NOT_RUN, owner and deferred claims without asserting utility.

### Definition of done

- **P5-DOD-01:** Store the frozen experiment plan, paired results, uncertainty, original-case retest and adjacent controls; keep measurement changes separate from agent changes.
- **P5-DOD-02:** Preserve losing configurations and rejected hypotheses. If the candidate fails constraints, retain the eligible baseline or continue remediation instead of forcing a winner.
- **P5-DOD-03:** Complete the attack-surface mapping, simulated approval expiry/replay/concurrency controls and governance crosswalk; operational legal applicability may remain pending within synthetic scope.
- **P5-DOD-04:** Prove gate recommendation and release authorization remain separate, including missing evidence, expired exceptions and candidate mismatch controls.

**Required evidence:** Observed finding and frozen comparison plan; Paired baseline/candidate report; Actual campaign manifest and effect evidence; Attack/regression/mitigation links or documented no-success result; T0–T2 CI records and governance controls; Component diagnosis and full-system retest; Accepted-evaluator architecture comparison and selection record; Human utility study or explicit claim-deferral record.

**Deferred:** Automatic promotion, broad optimization search, weights training and actual payer/clinical effects.

**Corresponding specs:** [EXPERIMENTS](EXPERIMENTS.md), [ADVERSARIAL_EVALUATION](ADVERSARIAL_EVALUATION.md), [CI_EVALUATION](CI_EVALUATION.md), [ARCHITECTURE_COMPARISON](ARCHITECTURE_COMPARISON.md).

## P6 — Reporting, efficiency and synthetic monitoring

Status: PLANNED | Owner roles: Engineering, Evaluation, Reporting, Operations design.

Five independently testable increments: P6A reports/trace projection; P6B prompt caching; P6C calibrated cascade; P6D upgrade drill; P6E synthetic monitoring. Early read-only report preparation may start from P4 snapshots without claiming P6 completion.

### Entry criteria

- **P6-ENTRY-01:** P5 supplies a retained eligible candidate, accepted evaluators and reproducible development suite. The relevant metric/schema extensions are implemented before use.
- **P6-ENTRY-02:** For each subphase, assign its plan, owner role, data/config pins, quality/safety limits, budgets and evidence requirements before collecting comparison data.
- **P6-ENTRY-03:** Before each applicable subphase, select its required provider/integration profile and authorize its export destination. Unused cache/cascade/upgrade prerequisites do not block P6A/P6E; they remain mandatory for full P6 completion.

### Exit criteria

- **P6-EXIT-01:** All P6A–P6E mandatory entry, exit and DoD criteria below are met with source-linked artifacts; a missing subphase prevents parent completion.
- **P6-EXIT-02:** At least two complete candidate configs are committed and compared using the full applicable development suite. Negative or inconclusive results are retained without forced adoption.
- **P6-EXIT-03:** Complete the evidence index for V2-A–D, including the required trace-platform projection, scenario coverage, human measurement, CI/adversarial evidence, cost experiments and monitoring. Reconcile it to actual source snapshots.

### Definition of done

- **P6-DOD-01:** Dashboards, JSON and Markdown reproduce the same metrics, denominators, missingness, freshness and candidate identities without exposing private labels.
- **P6-DOD-02:** Report runtime, evaluation and human effort costs separately. Sampling/correction assumptions and uncertainty accompany prevalence displays.
- **P6-DOD-03:** Keep all accepted alternatives and experiment dispositions; safety constraints take precedence over cost or latency gains.
- **P6-DOD-04:** Record local monitoring/triage outputs and upgrade decisions without enabling production traffic, external alerts or automatic deployment.

**Required evidence:** P6A–P6E evidence packets; Reconciled reporting snapshots; Two-or-more committed frontier configs; Completed V2-A–D demonstration index.

**Deferred:** Production monitoring, high-availability state infrastructure, external notifications, automatic routing promotion and deployment.

**Corresponding specs:** [DASHBOARDS_REPORTS](DASHBOARDS_REPORTS.md), [OPTIMIZATION_UPGRADE](OPTIMIZATION_UPGRADE.md), [MONITORING](MONITORING.md), [V2_GAP_FIXES](V2_GAP_FIXES.md), [QUALIFICATION_PROFILES](QUALIFICATION_PROFILES.md).

## P7 — Independent qualification and release decision

Status: PLANNED | Owner roles: Independent evaluation, Safety review, Release authority.

Freeze one selected candidate and execute T3 against a previously untouched, family-separated qualification suite. Finish a reviewed dossier for the declared synthetic application scope. Production deployment remains outside this plan.

### Entry criteria

- **P7-ENTRY-01:** P5, P6A and P6E evidence is complete and candidate-bound. Freeze a reviewed qualification profile, selected candidate/configuration and all mandatory criteria before access; require P6B/P6C/P6D when triggered by actual features, and all P6/V2-A–D evidence for FULL_V2_PROGRAM.
- **P7-ENTRY-02:** Assign numeric quality/safety limits, coverage/precision plan, budgets, independent evaluation ownership and named release authority. Resolve all inputs required by the qualification profile.
- **P7-ENTRY-03:** Verify suite access history, family separation, label isolation, evaluator acceptance and dependency identity; the optimizer cannot access qualification feedback.
- **P7-ENTRY-04:** Predeclare handling of failures, missingness and repeated looks. A revised candidate cannot reuse an opened test as an untouched qualification claim.
- **P7-ENTRY-05:** Implement and validate versioned profile/candidate binding and applicability controls before use. Every feature has reviewed PRESENT/ABSENT evidence; UNKNOWN, stale evidence or deferred mandatory controls cannot support GO.

### Exit criteria

- **P7-EXIT-01:** Execute and account for the complete scheduled qualification suite; adjudicate available evidence and retain unresolved judgments explicitly. Derive GO, NO_GO or INCONCLUSIVE from the declared policy and retain every blocker or gap.
- **P7-EXIT-02:** Record residual risks, applicable exception validity and a separate authenticated candidate-bound release decision. GO alone is not authorization.
- **P7-EXIT-03:** Archive the dossier and next action: eligible for the separately authorized release process, return to development, or collect missing evidence. No deployment is executed by completing the assessment.

### Definition of done

- **P7-DOD-01:** Persist immutable candidate/suite/model/evaluator identities, trial evidence, metric/gate snapshots and access history.
- **P7-DOD-02:** An independent reviewer can reproduce the gate from authorized evidence and distinguish computation, approval and observed effects.
- **P7-DOD-03:** For NO_GO or INCONCLUSIVE, preserve the completed assessment if its procedural DoD is met, while release eligibility remains failed or unresolved. Open follow-up work and require fresh qualification as applicable.
- **P7-DOD-04:** Update status and authorization records truthfully; no phase status or dashboard label substitutes for the actual release gate or authenticated authorization.
- **P7-DOD-05:** Report scoped qualification outcome, authorization, full-program completion and deferred experiments separately. Bind the actual A/B/C candidate and execution mode; no mock/replay substitute qualifies as the selected implementation.

**Required evidence:** Frozen qualification manifest and complete trial accounting; Independent evaluation and residual-risk review; Computed gate snapshot; Separate authorization/decision record; Reproduction and follow-up dossier; Frozen candidate-bound qualification profile and feature applicability evidence; Separate scoped outcome and full-program/deferred-experiment report.

**Deferred:** Any production deployment, live PHI processing, real clinical/payer effects or claims beyond the evaluated scope.

**Corresponding specs:** [CI_EVALUATION](CI_EVALUATION.md), [V2_GAP_FIXES](V2_GAP_FIXES.md), [severity-and-release-policy](../governance/severity-and-release-policy.md), [QUALIFICATION_PROFILES](QUALIFICATION_PROFILES.md).

## P6 subphases — separate entry, exit and DoD gates

All five subphases are PLANNED. P6A reporting preparation can use earlier validated
snapshots, but its final reconciliation uses the retained candidate. P6B and P6C
are separate experiments; P6D requires their results when its compared configurations
use those features. P6E follows P6A. Completing a
subset does not complete P6. A negative measured result may satisfy an experiment
packet; an unavailable required capability is a blocker, not a negative result.

| Subphase / status | Entry criteria | Build | Exit criteria | Definition of done / evidence |
|---|---|---|---|---|
| P6A — Reports and trace projection / PLANNED | Validated P4/P5 metric snapshots, access policy and selected trace-platform versions/destinations. | Read-only artifact dashboard and the required Langfuse projection; verify its selected self-hosted dependencies, including the analytical store. Keep application authority separate. | All displayed values reconcile to snapshots; trace links retain causal identity; missing export and stale/missing data are visible; private labels and secrets are excluded. | Commit reproducible report/projection configuration and control evidence for access, freshness, export loss and snapshot reconciliation. Evidence: Dashboard/JSON/Markdown snapshots, projection controls and source reconciliation. |
| P6B — Prompt-cache experiment / PLANNED | Pinned cache-capable profile and a preregistered cold/warm comparison, quality limits, scope/TTL and billing allocation. | Change one declared prompt-cache factor and meter all attempts, warm-up, misses and invalidations. | Paired cost/latency/quality results include failed calls and unknown usage. Scope/invalidation controls pass. Zero or negative savings are reported honestly. | Store the frozen plan, native usage/billing evidence, paired result, uncertainty and adoption/rejection decision. Retrieval caching cannot substitute. Evidence: Cache configuration, attempt receipts and comparison report. |
| P6C — Calibrated agent cascade / PLANNED | Development-only router tuning, frozen routing thresholds, two compatible model profiles and a separate audit plan including accepted cheap-path cases. | Meter router and model calls; evaluate cheap acceptance, escalation, bypass and important slices under unchanged authority controls. | Representative audit covers all routes and declared quality/safety/coverage bounds. A failed/inconclusive audit blocks cascade adoption while remaining a valid experiment result. | Retain reference-label provenance, inclusion probabilities, routing/config hashes, class/slice errors, full costs and deployment-disabled decision. Evidence: Router plan, route/audit manifests and candidate comparison. |
| P6D — Model-upgrade drill / PLANNED | P5 evidence, at least two committed complete configs, frozen shared suite/evaluators, predeclared constraints and an actual model/serving change for any upgrade claim; P6B/P6C evidence is required when compared configurations use those features. | Run all applicable T0–T2 checks per config, including multi-turn, security, grounding, handoff, cost and reliability. Preserve every measured point. | Comparable frontier and KEEP/PROPOSE_REPLACEMENT/PROPOSE_RETIREMENT/INCONCLUSIVE disposition reflect results; no automatic replacement occurs. | Archive commits, run/metric hashes, uncertainty, missingness, reviewer rationale and proposed rollback. Freeze any selected candidate before P7. Evidence: Full-suite run records and upgrade dossier. |
| P6E — Synthetic monitoring and triage / PLANNED | Frozen accepted evaluators, baseline windows, sampling probabilities and preassigned local alert/triage policy; P6A reporting controls pass. | Run code checks on all admitted synthetic trials and frozen judges on a probability sample where applicable. Simulate unchanged control, input/behavior shift, label delay, sparse samples and telemetry loss. | Coverage/label delay and sampling/judge corrections remain visible; invalid estimates are inconclusive; local alerts link to triage and approved development regressions. | Retain window manifests, raw/corrected estimates with uncertainty, loss controls and triage decisions. No production monitoring or external messages are enabled. Evidence: Monitoring exercise report, local alert records and feedback lineage. |

## First executable acceptance set

| Case / control | Expected behavior | Evidence to inspect |
|---|---|---|
| SYN-001, after reviewing the fictional predicates | READY only when all applicable requirements are supported | Scoped tool receipts, requirement-level findings and delivered answer |
| SYN-002, confirmed required item absent | NOT_READY with the confirmed blocker | Absence evidence and blocker reference |
| SYN-003, required evidence unavailable and no established blocker | UNKNOWN with unresolved check | Unavailability receipt and unresolved reason |
| Foreign-case read proposal | Denied before dispatch/disclosure | Trusted scope, denial record and no foreign result/effect |
| Write proposal against read-only catalog | Denied; legitimate read still succeeds | Catalog/policy decision and dispatch/effect accounting |

P1 establishes a single local command running rules-only candidate A and separate
mock integration controls, writing assessments,
trace records, independent assertion results and JSON/Markdown scorecards. No such
command exists yet; its exact entrypoint is chosen during implementation. The
three public examples remain development fixtures, never independent qualification
data. P2 adds blocker-plus-unresolved precedence, missing/duplicate evidence,
malformed responses, outages, budget limits and multi-turn failure controls.

## Mapping to full v2 acceptance

| V2 gate | Required phase evidence | What remains insufficient |
|---|---|---|
| V2-A — baseline/data | P1–P3 for world, agent, coverage and trace evidence; P6A for the required trace-platform projection | A three-case mock demo or a real-model pilot alone |
| V2-B — human measurement | P4 review/taxonomy/calibration and validated statistics; applicable subset/slice evidence from later runs | Sixty reviews alone, without saturation/coverage assessment and valid evaluators |
| V2-C — regression/adversarial | P2 reference CI, P5 actual regression/red-team/governance evidence, P6E monitoring and P4 reliability methods applied to actual trials | Green scaffold CI, blocked attack proposals or sampled exporter health alone |
| V2-D — improvement/upgrade | P5 manual fix and P6B–P6D measured caching/cascade/frontier/upgrade evidence | A favorable anecdote, mocked savings or two unexecuted configs |
| V2-Q — qualification | P7 independent frozen assessment and separate authorization state | Any phase-completion label or development comparison |

V2-A–D remain NOT_RUN until the complete applicable artifact set is reviewed.
Local tracing starts in P1 and real-provider evidence in P3; deferring the platform
projection does not defer evidence capture or imply V2-A is already satisfied.
P6 completes the full demonstration evidence index. Scoped P7 may run earlier only
under the frozen profile amendment above; its outcome does not complete V2-D or the
full index. Qualification and authorization remain distinct; production use requires
separate scope.

## Inputs, responsibilities and current dependencies

| Input / decision | Needed by | Current status | Work that can proceed |
|---|---|---|---|
| Fictional requirement review and case labels | P1 acceptance | NOT_REVIEWED_FOR_EXECUTABLE_BASELINE | Define world/tools and proposed predicates |
| Phase-specific schema/record extensions | Before first use in each phase | NOT_IMPLEMENTED | Design the minimal extension and deterministic controls |
| Real model/runtime configuration and credentials | P3 B/C execution | NOT_CONFIGURED | Finish rules-only baseline, mock controls, isolation and provider interfaces |
| Human reference reviewers and rubric responsibility | P4 reference-label acceptance | UNASSIGNED | Build private review UI, sampling and record workflows |
| Judge selection and calibration limits, if applicable | P4 judge acceptance | NOT_CONFIGURED | Code graders and human review |
| Pilot/comparison budgets, stopping rules and quality limits | Before applicable P3/P5/P6 runs | UNASSIGNED | Draft plans and verify deterministic computations |
| Trace platform/export profile | P6A | NOT_CONFIGURED | Local evidence capture and artifact reports |
| Cache/cascade/upgrade model profiles and audit plans | P6B–P6D | NOT_CONFIGURED | Usage attribution and comparison interfaces |
| Monitoring window/sample/alert policy | P6E | UNASSIGNED | Synthetic window fixtures and local triage records |
| Independent qualification set, frozen profile, criteria and named authority | P7 | UNASSIGNED | Protect family splits and implement profile/gate controls |
| Human utility participants and claim scope | P5 before productivity claims | UNASSIGNED | Draft matched study; defer claims if not run |

Owner roles describe responsibility; they do not assert staffing or approvals.
No estimates or committed dates are invented. Known future dependencies are listed
separately from an active BLOCKED state; set BLOCKED only when a specific attempted
next step cannot proceed, and record its reason and resumption action.

## Phase evidence packet and update procedure

For each completed increment, retain its phase/subphase ID, plan revision,
candidate/suite/config identities, evidence class, criteria-to-artifact mapping,
commands/run IDs, source digests, outcome counts and missingness, criteria
assessments, known defects, evidence author/review disposition and next action.
Private labels and raw sensitive evidence stay outside Git; commit permitted
references, manifests and aggregates. Link CI runs to their exact commit.

1. Start with the next bounded increment and assess its entry conditions. Record
   scope/criteria changes before execution; preserve earlier results as history.
2. Implement only the needed path and contract extensions. Add relevant positive,
   failure and missing-evidence controls; execute the increment's acceptance set.
3. Inspect traces and reconcile scorecards. Record each criterion as MET, UNMET,
   NOT_ASSESSED or justified NOT_APPLICABLE with evidence and reviewer identity.
4. Update PHASE_STATUS.json and BUILD_STATUS.json consistently. Update each task
   and component README for actual implemented slices; do not mark a whole task
   complete because one phase uses part of it.
5. Advance only after applicable exit/DoD evidence is met. Reopen affected checks
   after material changes; retain the previous completion record and candidate.
   Update the separate v2 index only when its complete evidence set exists.

PHASE_STATUS.json is planning metadata, not an executable runtime contract or
release-gate input. Its presence cannot enable an adapter, provider, job or
deployment. Existing disabled recipes remain disabled. Validation of this plan
checks references and status consistency only, not future phase behavior.
