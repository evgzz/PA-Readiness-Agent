# Controlled improvement and efficiency experiments

Status: PLANNED. An experiment may end with no improvement. Evidence must support
the outcome; no target reduction or accuracy gain is claimed by this specification.

## Preregister before execution

Use contracts/v1/experiment-plan.template.json. Record experiment_id and immutable
plan digest, finding/category, hypothesis, changed factor(s), baseline/candidate
digests, dataset/family split, case slices, trial counts/repetitions, reset process,
ordering/randomization, cache/concurrency/warm-up policy, model settings, tool
versions, evaluation digest, primary metric, minimum meaningful change, safety
constraints, non-inferiority margins, budget, stopping rule and uncertainty method.
Freeze these fields before collecting the comparison data.

Preregistration is complete only after required values are assigned and validated.
Development experiments cannot access qualification labels. A plan change creates
a new version and identifies which observations preceded the change; it is not
retroactive preregistration.

## Execute and compare

Pair baseline and candidate by source case and declared repetition. Reset the
synthetic world independently. Randomize or counterbalance order where practical;
record timing and provider changes. A seed alone does not guarantee hosted-model
reproducibility. Pin the strongest available model identity and disclose limits.

Keep model fixed for a harness change, and harness fixed for a model change.
If multiple factors change, report the bundle or use a preregistered interaction
design; do not attribute all improvement to one factor. Preserve every scheduled
trial, terminal error, retry, timeout and excluded observation with its reason.

Estimate uncertainty at the case/family level so repeated trials are not treated
as independent cases. State the estimator, confidence rule and handling of ties,
unresolved outcomes and incomplete pairs. Missing pairs are reported; incomplete
mandatory evidence cannot support a favorable qualification claim. Mark exploratory
slices and adjust or qualify claims when many candidates/comparisons were searched.

## Quality and cost rules

- Primary task-quality metric: Q04, successful legitimate trials / all scheduled
  eligible legitimate trials. Successful means required behavior and applicable
  safety predicates pass. A correct NOT_READY or necessary UNKNOWN/escalation can
  be successful; gratuitous refusal of a fully supported case is not.
- Guardrails: M02 false READY, M03 unauthorized effects/ambiguity, over-refusal and
  required slice performance. Safety limits are not traded away for lower cost.
- Q05 records end-to-end terminal latency, including failed trials, with missing
  and timeout/censoring counts. Compare equivalent workload and load conditions.
- Q06 divides total runtime cost for the full eligible workload, including failures,
  retries and fallbacks, by successful tasks. Show total cost, success count and
  component assumptions. Missing prices/usage means an incomplete total, not zero.
- Separate runtime cost, evaluation/judge cost, and human-review effort. If reporting
  a combined cost, state included components, currency, pricing version and review
  rate assumptions. Never treat evaluation overhead as free.
- The default Q06 workload is the same scheduled legitimate-task cohort as Q04.
  Adversarial stress runs and calibration work are separate workloads/cost lines;
  an expanded aggregate must explicitly name its case mix and denominator.

Selection may use a quality/cost frontier after mandatory safety and quality
constraints pass. Set non-inferiority and minimum meaningful improvement before
execution. A failed or inconclusive constraint disqualifies the claimed win.

## Candidate interventions

| Option | Hypothesis | Required control / known risk |
|---|---|---|
| Prompt or rubric clarification | Reduce unsupported readiness proposals. | Prompt-only change; keep evaluation rubric independent and frozen. |
| Retrieval/validation change | Correct missing, stale or mis-scoped evidence. | Version the source snapshot; audit relevance/lineage and false denial. |
| Cheaper model | Preserve required quality at lower workload cost. | Same harness/tools; capability and rare-risk slices; disclose hosted revision limits. |
| Caching | Avoid repeated deterministic retrieval or computation. | Include tenant/case, authorization, source version and expiry in cache scope; test isolation and invalidation; compare warm/cold conditions. |
| Retry policy | Avoid unnecessary repeated calls. | No blind retries after ambiguous effects; measure completion loss and unresolved outcomes. |
| Router/cascade | Reserve expensive inference for difficult cases. | Freeze routing criteria on development data; audit bypassed cases, routing cost, escalation and subgroup performance. |

Fine-tuning, distillation and autonomous optimization require separate data,
compute and leakage controls; none is necessary to complete v1.

## Decision and evidence packet

Use contracts/v1/experiment-result.template.json. Bind plan, run manifests, metric
snapshots, missing/exclusion lists and analysis code digest. Record measured deltas
with uncertainty, constraint outcomes, regressions, cost completeness and decision:
ADOPT_FOR_QUALIFICATION, REJECT, NO_DETECTABLE_DIFFERENCE or INCONCLUSIVE.
These are experiment decisions, not release-gate or authorization states.

The experiment owner may propose selection; independent qualification and release
authority remain separate. A positive development comparison cannot be reused as
an unbiased held-out score. Preserve negative results and link any candidate change
back to the reviewed finding and original case retest.

Proposed modules: evals/src/pa_evals/experiments.py and comparisons.py. Emit
experiment.registered when the plan is locked; experiment.finalized after complete
result persistence. Both are EVALUATOR_PRIVATE. Q07 renders the signed-off paired
comparison, primary/guardrail results and uncertainty from the frozen snapshots.

## V2 required experiment evidence

[Optimization and upgrade](OPTIMIZATION_UPGRADE.md) adds mandatory v2 exercises:
an observed-failure manual fix; token attribution; a measured prompt-caching
change; a calibrated/audited agent cascade; and a full-suite upgrade drill across
at least two committed frontier configurations. Reuse the preregistered comparison
contract above. Retrieval caching in the option table is a separate candidate and
does not satisfy the prompt-cache exercise. No proposed optimization must win.

Select the cheapest effective intervention layer supported by evidence: prompt,
tool design, harness, then model/weights. Authorization defects always require
code enforcement. Try a manual loop before considering GEPA or a bounded automated
optimizer, which remain deferred scope. Preserve safety constraints and hold-out
isolation; weights training is not required for v2. Candidate selection and any
later deployment continue to require distinct decisions.

## Plan 1.1 comparison sequence

[Architecture comparison](ARCHITECTURE_COMPARISON.md) requires actual rules-only A,
fixed extraction workflow B and bounded agent C; one model serves B/C initially.
P3 establishes feasibility, P4 accepts evaluators and P5 remeasures retained options
and diagnoses/fixes an observed component failure. Keep all losing/inconclusive
results and account for input eligibility and preparation labor. A human-only versus
assisted study is required before productivity claims; absent participants require
an explicit deferred-claim record, not simulated human evidence.

The full-program experiments above remain mandatory. Only the timing of scoped
qualification changes under [qualification profiles](QUALIFICATION_PROFILES.md).
