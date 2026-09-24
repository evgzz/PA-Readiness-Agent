# Human error analysis procedure

Status: PLANNED | Owner roles: evaluation lead and PA domain reviewer, UNASSIGNED.
Applies to development data. Qualification review is isolated and cannot silently
feed the optimizer. No clinical expertise or label validity is implied by a role name.

## Review cycle

1. Freeze the candidate, eligible run/trial population, intended behavior and
   evidence availability. Use contracts/v1/review-batch.template.json.
2. Select a reproducible sample. Separate RANDOM, STRATIFIED and TARGETED sources;
   retain seed, selected IDs, inclusion probabilities where known, stratum counts,
   exclusions and their reasons. Targeted failure samples support discovery, not
   an unbiased operational failure-rate estimate. Include success controls.
3. Review the observable trace: input, retrieved evidence, tool arguments/results,
   policy decisions, delivered answer and receipts. Do not require hidden model
   reasoning. Record inaccessible or incomplete evidence as UNREVIEWABLE with reason.
4. Annotate observable behavior in plain language before forcing taxonomy codes.
   Distinguish symptom, requirement violated, evidence reference and suspected
   cause. A suspected cause is a hypothesis until reproduced or otherwise supported.
5. Consolidate related descriptions into versioned categories with definitions,
   inclusion/exclusion rules and examples. Preserve OTHER and UNRESOLVED paths.
   Multiple categories may attach to one trial; category percentages need not sum
   to 100%. A blocked attack is not automatically a delivered system failure.
6. Independently double-review a preregistered subset and all material disputes.
   Reviewers are blind to candidate identity where practical. Preserve both
   original labels; adjudication adds a new decision and rationale.
7. Prioritize by severity, observed frequency within the declared sample, affected
   scope, evidence confidence and remediation cost. Show these dimensions rather
   than inventing a universal composite risk score. A rare critical boundary
   breach may take priority over a frequent minor defect.
8. Create a finding and reproducible development case. Link the failure category
   to a deterministic assertion or a reviewed semantic rubric. Track rejected
   hypotheses and benign cases as well as confirmed failures.

## Minimum annotation contract

Record annotation_id, record_version, review_batch_id, reviewer identity/role,
review time, candidate/evaluation digests, run/trial/case/family/trace references,
reviewability and reason, intended behavior, observed behavior, evidence references,
proposed category IDs and taxonomy version, symptom, suspected cause, cause status,
severity rationale, ambiguity, original verdict and adjudication reference.
Store decisions as append-only versions; corrections never erase earlier labels.
Templates are empty until actual review occurs.

## Starting taxonomy

The empty taxonomy template includes suggested dimensions, not observed findings:
readiness correctness, evidence retrieval/lineage, unsupported claim, tool selection,
authorization/scope, excessive refusal, budget/retry behavior and measurement error.
The initial codebook must be refined from actual traces. Keep proposed-answer
errors, delivered-answer errors and confirmed effects distinct.

For retrieval failures, distinguish missing relevant evidence, incorrect evidence,
stale/contradictory evidence, access denial and unavailable service. Measure recall
only when the relevant-evidence set is independently known. Otherwise report
reviewed relevance/adequacy and unresolved coverage without a false recall score.
For tool use, separate model proposal errors, dispatch failures and adapter effects.

## Reporting and instrumentation

Q01 measures completed human reviews / selected distinct trials and reports
pending, unreviewable and adjudication-pending counts. Q02 reports category
incidence among reviewable, coded trials, deduplicating each trial/category pair.
Never count reviewer duplicates as extra trials. Display selected population and
sampling method with both metrics.

Proposed module: evals/src/pa_evals/review.py. Persist the review manifest before
selection is exposed; emit review.batch.created. On accepted annotation versions,
emit review.annotation.recorded; on adjudication emit review.adjudicated. Taxonomy
publication emits taxonomy.versioned. All are EVALUATOR_PRIVATE. Authorized
aggregate projections feed the dashboard; raw labels and annotations stay private.

## Completion criteria

An independent reviewer can reconstruct selection and category counts, inspect a
disputed label and its resolution, and follow a confirmed failure to its test.
Duplicate annotations, missing traces, mixed sampling methods and category changes
must remain visible. A completed review is not automatically an agreed reference label.

## V2 review interface, coding and saturation

V2-04 requires at least **60 distinct reviewable real-agent synthetic development
traces**. Track selected, available, reviewed, unreviewable and adjudicated counts
separately; duplicate reviewers or repeat imports cannot inflate the floor. This
is an exercise minimum, not a sample-size justification for rare-risk estimates.

The review interface may start as a local application over frozen artifacts. It
must display the complete permitted multi-turn trace, input/evidence versions,
nested model/tool spans, denials, attempted versus delivered answers and receipts.
Support trace navigation, plain-language notes, first observable failure with a
causal step reference, secondary failures, uncertainty, save/resume, taxonomy
version and dispute resolution. Hide judge predictions until the initial human
label is saved; enforce evaluator-private access. No hidden reasoning is required.

1. **Open coding:** read complete traces and note the first observable failure in
   ordinary language, before imposing category names. Preserve subsequent failures
   and recovery; a corrected final answer cannot erase an earlier unsafe action.
2. **Axial coding:** group notes into binary failure modes. Give each mode a
   definition, inclusion/exclusion boundaries, positive/negative/ambiguous examples,
   applicability unit and links to traces. Aim for 5–8 observed modes, explaining
   fewer/more; never invent failures to meet a count. Resolve overlap explicitly.
3. **Saturation assessment:** preregister batch size, coverage requirements and a
   stopping criterion before review. Log new modes, changed boundaries, unresolved
   ambiguities and slice coverage after each batch. Sixty reviews alone cannot
   prove saturation. Retain SATURATED / NOT_SATURATED / INCONCLUSIVE as proposed
   review-report values, not existing gate enums; additional sampling may be needed.
4. Compare published taxonomies only after creating the human-derived codebook.
   Keep proposed security coverage separate from observed product failures.

Proposed review/saturation reports bind the sampling manifest, batch history,
taxonomy digest, reviewer/adjudication records and first-failure references.
Task 00 must version and validate these extensions; Task 04 implements the UI
and procedure. Export aggregate counts only to Q01/Q02 report detail.
