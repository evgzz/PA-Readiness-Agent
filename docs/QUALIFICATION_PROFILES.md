# Qualification profiles and full-program completion

Specification 2.1 | Status: SPECIFIED_NOT_IMPLEMENTED | Scope: SYNTHETIC_READ_ONLY

This is an explicit amendment to the dependency between P6 and P7 in plan 1.0 and
ADR 025. Full V2-A–D completion still requires every specified experiment. A frozen,
scoped candidate can enter P7 after the core evidence and every feature-dependent
requirement below are satisfied. This amendment does not waive safety, evaluator
acceptance, trace integrity, held-out isolation or authenticated authorization.

## Profiles

| Profile | Entry evidence | Meaning of completion |
|---|---|---|
| SCOPED_CANDIDATE | P0–P5, P6A and P6E; complete candidate-applicable V2-A/B/C evidence and manual-fix evidence; all conditional feature requirements below. | Independent assessment of the declared candidate and synthetic workload only. Full-program status can remain NOT_RUN/incomplete. |
| FULL_V2_PROGRAM | All scoped requirements plus parent P6 COMPLETE and the complete V2-A–D index, including caching, cascade and upgrade exercises. | Full development program evidence plus independent candidate qualification; neither implies production authority. |

P0–P5 remain required for both paths in this plan, including the controlled A/B/C
comparison, 60 distinct reviewable real-agent development traces and the observed
manual-fix experiment. A rules-only candidate cannot count deterministic or mock
traces toward that 60-trace floor. Relevant agent experiments may involve B/C while
A is retained; no model-performance claim is made about A. This plan does not add
a shortcut around human error analysis or invent a failure to satisfy the fix gate.

## Conditional requirements, frozen before qualification access

| Feature or change | Required evidence before P7 | When it may remain deferred |
|---|---|---|
| Prompt caching used, including implicit provider caching | P6B quality, scope, invalidation, usage/billing and cold/warm evidence bound to the selected configuration. Unknown cache behavior blocks applicability resolution. | Affirmatively absent in the selected implementation/provider profile, with reviewed evidence. No savings claim without a measured experiment. |
| Router or cascade used | P6C frozen router, route coverage, cheap-path/bypass audit, calibration, costs and accepted quality/safety bounds. | Absent with code/config evidence; a single model is not automatically a cascade. |
| Model/serving replacement against a previously qualified baseline | P6D full applicable regression comparison against the prior configuration, plus new independent qualification. | Initial qualification or no replacement, with explicit rationale; the full-program upgrade exercise stays pending. |
| Semantic judgment required | Accepted P4 evaluator profile and untouched human-reference audit for each mandatory semantic failure mode. | Only when reviewed applicability shows objective assertions cover the required criterion; choosing rules-only does not automatically remove semantic risks. |
| Human time-saving/productivity claim | Accepted P5 human-only/assisted utility experiment under the actual candidate/workload. | No such claim is made; record NOT_RUN and the deferred claim. |

A feature state is PRESENT, ABSENT or UNKNOWN with evidence and a reviewer. UNKNOWN
is not ABSENT and cannot support GO. Numeric safety/quality/coverage limits and
sample/precision plans must be assigned before execution, not inferred from results.
Predeclare all relevant features, including provider-managed behavior. A selected
candidate that uses caching or routing must satisfy its safety/quality controls even
if it makes no optimization claim. An unused experiment may remain PLANNED for the
scoped profile; never mark it COMPLETE or use N/A to close the full-program gate.

P6D may execute after P5 without waiting for unused P6B/P6C experiments. If caching or
routing is part of either compared configuration, their applicable evidence is a
prerequisite to the upgrade decision. Full P6 completion still requires all five
subphases. Changes to code, prompts, tools, policies, data, models, serving, evaluator
or material configuration after freeze reopen affected evidence and qualification;
initial-profile status is not a means to bypass replacement testing.

## Candidate-bound assessment

Freeze profile ID/version/hash, candidate kind/config digest, intended workload,
source/suite/evaluator identities, feature decisions, mandatory tier/criterion IDs,
thresholds, deferred experiments/claims and reviewer before access to qualification.
Record dependencies individually; a development pass from a different candidate
cannot satisfy the selected candidate's mandatory behavior. Threshold amendments
create a new protocol; they cannot be used to retroactively pass an opened suite.

T3 evaluates the actual selected implementation through the independent controller.
Rules-only execution uses REFERENCE_CONTROL plus explicit RULES_ONLY candidate kind,
real predicate/tool receipts and qualification status; it must not execute a scripted
answer mock or be reported as real-LLM evidence. B/C use REAL_AGENT_SYNTHETIC with
actual model receipts. Profile metadata does not change existing evidence enums.
Any new candidate/profile fields require versioned, validated contracts before use.

Keep scheduled, complete, failed, unresolved and missing trials; known mandatory
failures produce NO_GO under the release policy and are not hidden by missingness.
Unresolved mandatory evidence cannot produce GO. P7 procedural completion may record
NO_GO/INCONCLUSIVE only after its required execution and records exist. Missing
mandatory runs leave the phase incomplete. GO remains distinct from authenticated,
candidate-bound authorization; deployment, PHI and real effects remain outside scope.

## Activation and reporting

The [profile template](qualification-profile.template.json) is disabled planning
metadata. Existing runtime validators and release-policy schemas do not accept it
as an executable authority record. Implement versioned profile validation, dependency
resolution and candidate binding in Task 00/06 before use. Demonstrate that missing
features, stale identities, deferred mandatory controls and profile mismatch cannot
produce GO, and that an unused optimization does not falsely block a scoped profile.

Display profile, qualification execution/outcome, authorization state, full V2-A–D
status and outstanding experiments separately. Never summarize scoped GO as full v2
completion. See [phase plan](PHASED_DELIVERY_PLAN.md), [CI](CI_EVALUATION.md),
[release policy](../governance/severity-and-release-policy.md) and
[ADR 026](adrs/026-candidate-comparison-and-qualification-profiles.md).
