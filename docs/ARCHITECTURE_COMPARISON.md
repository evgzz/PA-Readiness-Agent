# Architecture comparison and earlier validation

Specification 2.1 | Status: PLANNED | Scope: SYNTHETIC_READ_ONLY

Choose the least complex candidate that meets the preregistered quality, safety,
coverage and operational constraints. No architecture is selected by this document.
All candidates use authenticated case scope, independent evaluation and the same
execution gateways. Expected labels and hidden qualification material remain outside
runtime access. External writes and real clinical/payer effects stay disabled.

## Three candidates

| Candidate | Implementation to test | Evidence required | Phase |
|---|---|---|---|
| A — rules only | Read authorized fictional facts through tools; evaluate reviewed readiness predicates in code. No model calls. | Actual predicate execution, requirement-level support/absence/unavailability and lineage; a known unsupported READY fails independent assertions. | P1 baseline; P3 comparison |
| B — fixed workflow with LLM extraction | Prescribed retrieval and extraction steps; model proposes structured fields and citations; code validates inputs and applies readiness rules. | Source-grounded extraction audit, missing/ambiguous evidence behavior, actual model/tool receipts and deterministic readiness checks. | P3 |
| C — bounded agent | Model chooses among permitted tools and proposes a result within fixed budgets; harness enforces authority and required evidence checks. | Actual trajectories, authorized partial orders, independent terminal/trajectory checks, budget and hostile-proposal controls. | P3 |

A is a usable candidate, not the deterministic mock model. It must read evidence and
compute predicates, never map case IDs to known answers or read grader labels. Keep
the scripted model as a separate loop/contract control. Existing evidence classes
remain unchanged: record A as REFERENCE_CONTROL with candidate kind RULES_ONLY and
actual execution identity; this class alone does not establish qualification.
B/C actual model runs are REAL_AGENT_SYNTHETIC. Mock/replayed execution is explicitly
marked and cannot establish live provider or model-performance claims.

For B, a schema-valid field or resolving citation is not proof that the source
supports the extraction. Define source admissibility and semantic verification,
independently audit extraction errors, and return UNKNOWN for unverified required
support unless another confirmed blocker establishes NOT_READY. Do not assume that
deterministic downstream rules remove upstream interpretation risk. Apply the same
product precedence and evidence standards to all three candidates.

## Fair comparison and selection

Freeze a development protocol before executing the comparison: case/family mix,
source snapshots, repetitions, reset/state, permissions, available evidence/tools,
budgets, evaluators, metrics, safety limits, non-inferiority margins, uncertainty,
stopping rules and config identities. B and C initially use one pinned model/provider.
The controlled B/C comparison holds prompts/tool contracts/model settings constant
where possible and identifies workflow/orchestration as the intervention. If a
representation, prompt, evidence pipeline or budget also changes, report a bundled
comparison; do not attribute the difference solely to agent autonomy.

A receives the same authorized source facts, never gold extracted fields. If a
rules-only input requires manual preparation, record that labor and source quality;
report input eligibility/coverage and any narrower workload. Compare the shared
eligible cohort and separately report full-workload coverage. Do not claim equivalent
accuracy by silently dropping documents A cannot process. Charge preprocessing,
retrieval, retries, evaluation and human effort to their declared cost categories.
No-LLM inference cost can be zero; total system or labor cost cannot be assumed zero.

P3 is a bounded feasibility comparison with independent code checks and human trace
inspection. P4 calibrates evaluators; P5 remeasures the retained alternatives under
accepted evaluators before selection. Include false READY, unauthorized access,
completeness/abstention, legitimate-task success, trajectory failures, latency and
cost with denominators, missingness and uncertainty. Analyze paired cases/families,
not independent-looking turns from the same trajectory. Preserve all candidates and
negative/inconclusive results. An inconclusive comparison selects no claimed winner;
a previously eligible baseline may be retained. Qualification uses untouched families
only after candidate/profile/evaluators are frozen.

## Earlier test methods

| Method | Entry and execution | Exit evidence / DoD | Phase |
|---|---|---|---|
| Property and metamorphic checks | Review each relation against the fictional predicates; generate bounded paired cases and seeded boundary defects. | Same semantics under irrelevant reordering; removing required support cannot newly establish READY; cross-scope variants are denied; isolation/reset invariants hold. A deliberate violating implementation is caught. Retain seeds, pairs, relation and evaluator version. | P2; real-candidate checks in P3/P5 |
| Recorded tool-response replay | Capture permitted synthetic tool fixtures with provenance; declare replay mode before execution. | Match canonical request, authenticated scope, tool/schema version and initial-state digest to the fixture. Miss, mismatch, exhausted sequence or tamper produces explicit incomplete/error evidence and zero live fallback. Every replay receipt links to original and fixture digests. | P2 |
| Component diagnosis and ablation | Use a human-reviewed observed failure, a development partition and a single component hypothesis. | Compare a replacement/bypass fixture at extraction, retrieval, planning, memory or rendering boundaries; retain paired results, changed factors and uncertainty. An inconclusive diagnosis remains explicit. | P5 |
| Human-only versus assisted utility | Qualified participants, matched synthetic case families, frozen rubric/time protocol and counterbalanced assignment. | Compare correct final decisions, missed blockers, unsupported claims, correction effort and end-to-end time. Report sample/participant counts, learning/order effects and uncertainty; preserve unfavorable results. | P5; required before any utility/productivity claim |

Metamorphic checks compare meaning, findings and authority, not exact prose. Freeze
how stochastic B/C behavior is evaluated; repeated samples cannot be retried until
an invariant appears to pass. NOT_READY may become UNKNOWN when a confirmed absence
becomes unavailable; neither supports READY. Scope changes are security tests, not
semantically equivalent cases. Review transformed labels independently and keep
related variants in one partition.

Replay is an additional test adapter. Canonicalization excludes only reviewed
nonsemantic fields; it never drops caller/case/operation identity. Preserve ordered
multi-turn fixture state and reset it per trial. Recheck current authorization
before serving a recorded response. Fixtures contain no private labels or protected
records. Replay cannot replace real endpoint, model, live-tool or latency/cost tests;
separate original measured cost from replay execution cost. Hybrid runs declare each
port's mode in advance and never silently switch on a replay miss.

Ablations run only in isolated evaluation with no live effects. Never disable actual
authorization, case isolation, label separation or evidence recording. Evaluator-only
oracle substitutions stay inside the evaluation process and are diagnostic upper
bounds, never deployable candidate performance. A proposed real fix needs a separate
unassisted end-to-end retest under unchanged enforcement.

The human utility study is claim-dependent. Without qualified participants, record
NOT_RUN, responsible owner and deferred claims; do not treat synthetic reviewer
simulation or LLM judging as human productivity evidence. Use distinct matched cases
or counterbalanced groups to limit answer recall; blind final adjudication where
practical. Select sample size and meaningful-effect/error bounds before execution.
Core safety and qualification remain mandatory even when utility claims are deferred.

## Instrumentation and corresponding specifications

These are proposed metadata/record extensions, not implemented event schemas. Add
validated contracts before emission; keep evidence collection in its owning component
and render read-only snapshots in reports. Do not create new metric IDs by implication.

| Record / measure | How and where to capture | Report / corresponding specs |
|---|---|---|
| Candidate comparison | Composition root records candidate kind/config; harness/model/tool gateways record actual modes, attempts, receipts and terminal result; evaluator pairs case/family trials. | Candidate quality, coverage, latency, cost and uncertainty; [Experiments](EXPERIMENTS.md), [Instrumentation](INSTRUMENTATION.md). |
| Properties and replay | Evaluation controller records relation/fixture/request/state digests, authorization receipt, result, mismatch and deliberate-defect detection. | Scheduled/passed/failed/unresolved/missing controls and replay/live split; [CI](CI_EVALUATION.md). |
| Component diagnosis | Evaluator records isolated component, replacement fixture, intervention and full-system retest IDs. | Diagnosed failure contribution with limitations; [Error analysis](ERROR_ANALYSIS.md). |
| Human utility | Controlled review interface records anonymized participant/assignment, start/end/active time, corrections and final adjudication. Labels stay evaluator-private. | Time and quality together, correction burden, missing sessions and uncertainty; [Dashboards](DASHBOARDS_REPORTS.md). |
| Qualification applicability | Governance consumes frozen profile, feature evidence and candidate-bound results; reporting displays both scoped outcome and full-program status. | Mandatory/deferred/unknown criteria with reasons; [Qualification profiles](QUALIFICATION_PROFILES.md). |
