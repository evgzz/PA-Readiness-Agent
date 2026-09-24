# V1 worked-example contract

Status: ILLUSTRATIVE_PLAN_ONLY. No steps below have been executed. These expected
behaviors are design examples, not baseline observations or measured improvements.

## Scenario and hypothesis

A fictional case requires a supporting document. The retrieval service returns
UNAVAILABLE rather than confirmed absence. With no separately established blocker,
the intended delivered outcome is UNKNOWN with a review reason; READY is invalid.
If a different required item is confirmed missing, NOT_READY remains correct while
the retrieval uncertainty stays visible. A complete-evidence positive control must
still permit READY. A confirmed-missing-document control must return NOT_READY.

Hypothesis to test if observed traces justify it: a specific agent prompt revision
may reduce confusion between unavailable and satisfied evidence. Keep harness,
model, tool behavior and evaluators fixed. If the harness already prevents invalid
delivery, measure proposed false READY separately; do not claim a delivered-quality
gain when delivered outcomes were unchanged. Any harness change is a new experiment.

## Required evidence chain

| Step | Artifact to produce | Completion rule |
|---|---|---|
| 1. Baseline | Actual real-agent synthetic run manifest, tool receipts and trace. | Record actual observations, including when the hypothesized failure does not occur. |
| 2. Human review | Selection manifest and annotation with evidence references. | Separate observed symptom, suspected cause and reference-label uncertainty. |
| 3. Taxonomy/finding | Versioned category and prioritized finding. | Reproduce the issue or retain the cause as unconfirmed. |
| 4. Measurement | Deterministic outcome/evidence assertion; semantic rubric only if needed. | Positive/negative controls pass; applicable judge audit accepted. |
| 5. Experiment | Preregistered plan, baseline/candidate paired schedule and fixed budgets. | Only declared factors change; required fields assigned before execution. |
| 6. Results | Q04–Q07 and M02/M03 snapshots, uncertainty and unresolved counts. | Report what happened; no synthetic improvement percentages or selective omissions. |
| 7. Regression | Original-case retest, permitted positive controls and related cases. | Task success and safety constraints hold under declared criteria. |
| 8. Decision | Experiment disposition and evidence-linked summary. | Selection for qualification is distinct from release authorization. |

If real execution yields no relevant failure, retain that result and select an
actually observed development failure for the improvement demonstration. A seeded
script can test the evaluator but cannot substitute for real-agent failure evidence.
Publish only reviewed synthetic summaries; private annotations and held-out
examples remain in controlled evidence storage.

## V2 completion extension

The example remains illustrative and NOT_RUN. Expand the eventual dossier with
the [v2 acceptance index](v2-acceptance.template.json): scenario smoke report;
60 distinct reviewable real-agent development traces and saturation assessment;
binary evaluator audit; fixed-k reliability and defensible prevalence; CI tiers
and red-team regressions; manual-fix, prompt-cache and cascade comparisons; a
two-configuration upgrade drill; synthetic monitoring; and separate qualification.
One example trace cannot satisfy the review floor or population uncertainty plan.
Keep simulated controls and actual endpoint/model trials clearly identified.
