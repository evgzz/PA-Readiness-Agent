# V2 judge, prevalence and repeated-trial measurement

Status: SPECIFIED_NOT_IMPLEMENTED. These extend the design; they are not accepted
fields in current metric/event schemas. Task 00 must version schemas and validators,
and Task 04 must implement computation before exporting them. Existing M/Q metrics
retain their definitions. This document supplies proposed Q03/Q07/Q08/Q09 detail
reports, not permission to insert unknown keys into existing payloads.

## Binary evaluator unit and class errors

A failure category is a binary predicate with applicability, positive/negative
examples, boundaries, evidence dependencies and unresolved rules. Use one evaluator
per observed failure mode; multiple predicates can fail on one trace. Code checks
own objective facts. Semantic judges require independent calibration. J01–J07 are
candidate rubrics, not seven observed failures. J06 remains an ordinal diagnostic.

Human reference failure is the positive class. TP = detected failure; FN = human
failure incorrectly passed; FP = human pass incorrectly failed; TN = correct pass.
On resolved reference/prediction pairs:

- TPR (sensitivity) = TP/(TP+FN); FNR = FN/(TP+FN).
- TNR (specificity) = TN/(TN+FP); FPR = FP/(FP+TN).
- Precision = TP/(TP+FP), when its denominator is nonzero.

Report counts and class/slice denominators with every rate. These conditional rates
exclude unresolved predictions, so also show total human-positive/negative counts,
unresolved in each class, missing labels, parsing errors and accepted-decision
coverage. An abstention is neither a correct classification nor an invisible case.
Zero denominator yields N/A. Minimum counts, error bounds, coverage bounds and
uncertainty method must be preregistered; no fixed numeric acceptance is invented.

Judge/rubric rendering, thresholds, model/route/deployment and context projection
bind one effective profile. Preserve original human labels and adjudication.
Train/development data can refine a judge; an untouched audit assesses it. Opening
and retuning against an audit consumes it. Candidate selection uses development
comparisons; the final test is frozen and read once for independent qualification.
Do not pick the best candidate after repeatedly reading the same test labels.

## Failure prevalence and two distinct corrections

First define the target population, unit (trial or case), window, slices, label
maturity, reviewability and sampling mechanism. Targeted discovery counts support
prioritization within that sample, not a population failure-rate claim.

1. Sampling correction: for a probability sample with known nonzero inclusion
   probability pi_i, a proposed weighted ratio estimate is sum(w_i*y_i)/sum(w_i),
   w_i=1/pi_i, y_i the human binary failure label. For simple random samples use
   the ordinary mean. Record stratum population weights and inclusion probabilities;
   unknown selection probabilities prevent a general population estimate. Missing
   labels need declared handling/bounds, not automatic removal.
2. Judge-error correction: let q be the sampling-adjusted fraction flagged by a
   frozen binary judge, s=TPR and t=TNR on an independently labeled, relevant audit.
   Under transferable class-error rates, q=s*p+(1-t)*(1-p), giving
   p=(q+t-1)/(s+t-1). Report q, s, t, denominators, uncertainty and assumptions.

Only apply the second formula to a complete binary judged population (or an
explicitly conditional resolved stratum). If a judge abstains, report that stratum
separately; representative human review and weighting can combine it with the
resolved stratum. Do not extrapolate resolved-only calibration to everyone or mix
human and model labels under one error model. Apply correction within comparable
strata when error rates differ. Validate transfer to the monitoring window; drift
can invalidate the correction.

If s+t-1 is nonpositive, too close to zero under a preregistered stability bound,
or uncertain enough to make correction unstable, report INCONCLUSIVE. A corrected
estimate outside [0,1] is a diagnostic of incompatibility/noise: preserve the raw
estimate and use a preregistered constrained method or report inconclusive, never
silently clip it into a favorable result. No correction repairs missing population
coverage, bad human labels or leaked audit data.

## Bootstrap and uncertainty contract

Freeze confidence level, replicate count, RNG seed, estimator, resampling unit,
strata, minimum class/family counts and treatment of missingness before analysis.
Resample source families, retaining their paired candidate trials/repetitions;
respect stratified sampling weights. For corrected prevalence, propagate both
monitoring-sample and independent calibration uncertainty. If samples overlap,
preserve dependence explicitly rather than treating them as independent.

Persist intervals, class counts, effective sample diagnostics, invalid-replicate
fraction and method/code digest. Sparse classes, one/few clusters or zero observed
failures can yield misleading/degenerate bootstrap intervals. Flag these and use
a preregistered appropriate rare-event method or remain inconclusive; do not infer
zero risk from a zero-width bootstrap interval. Multiple comparisons and repeated
monitoring looks require a declared error-control or descriptive-only policy.

## pass^k reliability versus pass@k capability

Preregister k >= 1 reset-independent executions per case under the same candidate,
world, tool and policy configuration. Outcomes use all required assertions, not
just final answer quality. Regrade repetitions are not new agent executions.
For N scheduled cases with all k judgments resolved:

- pass^k = fraction of cases whose k executions all PASS (consistent reliability).
- pass@k = fraction of cases with at least one PASS (capability with k opportunities).

These are empirical case-level rates, not a license to retry a user task until it
looks successful. State whether a retry budget is inside a trial or across trials.
Neither statistic is obtained by raising one pooled average to a power unless its
strong modeling assumptions are separately justified. Fixed-k empirical analysis
is the v2 default; alternative estimators require versioned definitions.

For each scheduled case, P is confirmed PASS count, F is confirmed FAIL count,
U=k-P-F includes unresolved, missing and execution-error judgments without a
confirmed result. Keep known failures even when other evidence is missing.
Report uncertainty bounds over the full N scheduled cases:

| Measure | Confirmed lower bound | Possible upper bound |
|---|---|---|
| pass^k | mean(1[P=k]) | mean(1[F=0]) |
| pass@k | mean(1[P>0]) | mean(1[P+U>0]) |

These missingness bounds are distinct from statistical confidence intervals.
Incomplete required evidence blocks qualification even if capability is observed.
Show N, unique families, k, scheduled/completed/valid trials and all missing counts.
A deterministic reset checks isolation, not independence of hosted model randomness;
disclose provider drift and dependence limits.

## Subsystem measurement and acceptance

| Subsystem | Required checks / interpretation |
|---|---|
| Retrieval | Known relevant-evidence set: recall and scoped relevance; otherwise label adequacy/coverage unresolved. Test wrong patient, denied access, stale and unavailable sources. |
| Grounding | Claim inventory, reference identity/existence and semantic support; proposed versus delivered unsupported claims remain separate. |
| Local handoff | Correct blocker/unresolved reason, necessary case/evidence context, review destination identity and no misleading approval claim. No external message is sent. |

Acceptance controls include known TP/FN/FP/TN, abstentions, zero denominators,
unequal sampling weights, dependent repeated cases, unstable correction, sparse
bootstrap, missing trials and mixed judge versions. Analyses must recompute from
frozen snapshots. All statistics and acceptance controls above remain NOT_RUN.
