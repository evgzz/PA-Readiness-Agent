# Independent evaluation specification

Status: PLANNED. Three retained public interface cases are not benchmark coverage.

## Evaluation unit and identities

A case is a source scenario. A variant belongs to its source family. A trial is
one scheduled execution for a case and candidate. A run contains a declared trial
schedule. A slice groups required trials by risk and operating conditions.
Freeze these identifiers, requirements, and counts before executing qualification.

Separate candidate configuration digest from evaluation-configuration digest.
The former binds code, agent, model, prompts, runtime, tools, permissions, and
serving settings. The latter binds dataset, schedule, reset, graders, thresholds,
and policy. A run manifest binds both. Timestamps or family names are not pins.

## Independent execution protocol

1. Validate declared scope, identities, eligible datasets, and trial schedule.
2. Reset isolated case/action state and retain the reset receipt.
3. Supply only the current trial's authorized input to the SystemUnderTest port.
4. Execute in the declared evidence class; retain all terminal outcomes.
5. Inspect proposed and delivered answers, action decisions, and actual effects.
6. Apply frozen graders; adjudicate uncertainty; record grader/evidence versions.
7. Check missing/duplicate trials and evidence gaps before computing aggregates.
8. Finalize result and metric snapshots; pass evidence references to governance.

No retry can silently overwrite an earlier trial. Replacement/invalidated trials
need explicit reasons, versioned schedule changes, and preserved original results.

## Required first-release risk coverage

| Risk | Planned test and measurement |
|---|---|
| False READY / hallucination | Required evidence unavailable or unsupported; distinguish proposed versus delivered false READY |
| Multi-turn tool calling | Evidence arrives over turns; maintain case scope, resolve required steps, honor budgets |
| Prompt injection | Untrusted document instructs agent to skip validation or call a prohibited tool |
| Unsafe tool use | Forced submit/update/cancel and a legitimate read-only positive control |
| Unintended access/disclosure | Wrong patient/tenant/request, foreign references, prohibited destination |
| Excessive autonomy | Attempts beyond permitted objective, operations, budget, or delegation scope |
| Multi-step failure | Stale evidence followed by retry/resume, contradictory tool results, cumulative scope drift |
| Ambiguous effects | Timeout after possible effect; check reconciliation and duplicate prevention in enabled profiles |
| Data poisoning/manipulation | Altered source evidence or requirements; provenance and contradiction handling |
| Measurement failure | Missing receipt, mixed candidate, omitted trial, duplicated event, unconfigured grader |

For initially disabled writes, use an isolated synthetic world to force attack
proposals and inspect effects. This tests a reference boundary, not real-agent
adversarial resistance unless an actual model generated the trajectory.

## Coverage dimensions and benchmark selection

Declare applicability by model/release, risk, domain, language, modality, context
length and actual tokens, turn count, tool set, and reasoning configuration.
English text is the first proposed scope. Multilingual, multimodal, expanded
long-context, and broader frontier/content-risk programs require their own slices,
data, graders, owners, and resource plan; they remain NOT_SCOPED.
An exclusion requires a documented intended-use reason and accountable review.
Changing exclusions after seeing failures changes the scope version and remains visible.

Benchmark candidates: MedAgentBench/FHIR-AgentBench for FHIR evidence workflows;
BFCL for model tool-call capability; AgentDojo for untrusted tool-output injection;
tau-family for policy-constrained multi-turn workflows. These are selection
candidates from prior research, not installed suites or validated PA substitutes.
Verify exact release, license, adapters, and scoring protocol before adoption.
PA-specific suites remain necessary. Do not label an adapted score official.

## Graders and calibration

Use deterministic assertions where facts are observable. For semantic judgments,
define an anchored rubric, blind candidate identity where feasible, independently
label a calibration set, and report confusion matrix, disagreement, and agreement
statistics with sample size. Set acceptable error bounds before use. Route uncertain
or materially disputed judgments to adjudication; do not average them into PASS.
Keep calibration and qualification data separate. Judge and rubric changes require
versioning and re-evaluation of affected results.

## Metrics and experimental comparisons

The authoritative formulas are in `contracts/metric-definitions.json` and explained
in `docs/DASHBOARDS_REPORTS.md`. Primary system metrics use the delivered answer;
the proposed answer has a separate false-READY metric to measure protection burden.
Report legitimate task completion beside safety blocks to reveal excessive refusal.

Compare paired source cases under fixed conditions and a declared repeated-trial
budget. Report case-level and trial-level results separately. Use a preregistered
uncertainty method that respects repeated trials/family clustering; do not treat
correlated trials as independent population evidence. Zero observed violations
does not establish zero underlying risk.

Safety constraints precede accuracy/cost ranking. Cost includes failed requests,
retries, fallbacks, tools, and any included human review; report assumptions and
unknowns. A failed cascade audit is HOLD, without retuning on that same audit.

## Finding and release handoff

Evidence → finding → severity/owner/date → mitigation → unchanged-case retest →
regression/positive control → reviewer closure → independent gate snapshot.
An evaluation PASS is not a release authorization. Governance computes the gate
from all mandatory evidence and current exceptions; reporting only displays it.

Required future verification includes known failing/positive cases, oracle
isolation, reset independence, incomplete run handling, judge failure, comparison
identity mismatch, and deterministic metric recomputation. All remain NOT_RUN.

## V1 required procedures
Use [human error analysis](ERROR_ANALYSIS.md) before choosing improvement targets;
use [calibration](EVALUATOR_CALIBRATION.md) before relying on semantic judges.
[Experiments](EXPERIMENTS.md) define preregistration and paired comparisons;
[monitoring](MONITORING.md) defines the synthetic feedback exercise.
[V1 acceptance](V1_GAP_FIXES.md) and Q01–Q09 are mandatory for the applicable
improvement/monitoring demonstration profiles. All remain NOT_IMPLEMENTED.

## Swappable judges and multi-turn semantic grading
[Judge specification](LLM_JUDGE.md) defines the proposed JudgePort, J01–J07
rubrics, evidence-at-decision-time prefixes, full trajectories, response validation,
calibration and acceptance checks. Use deterministic facts plus accepted semantic
assertions; do not replace a trial verdict with one averaged quality score.
Status: specified, not implemented or calibrated.

Each judge profile is selected explicitly and frozen per evaluation run. Jev is
one option. Model/provider/deployment or rubric changes require profile-specific
calibration; regrades preserve original evidence and receive a new grading identity.
