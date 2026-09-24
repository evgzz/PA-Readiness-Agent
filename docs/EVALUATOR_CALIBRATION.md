# Evaluator construction and calibration

Status: PLANNED. Deterministic checks are preferred for observable facts. An LLM
judge is optional and cannot establish authorization or external effects.

## Failure-to-evaluator mapping

Every assertion identifies requirement_id, failure_category_id, intended input,
output unit, applicability, PASS/FAIL/UNRESOLVED rules and evidence dependencies.
Examples: scope IDs and receipts use deterministic checks; adequacy of a cited
explanation may use an anchored rubric. Use executable positive/negative controls
for deterministic checks. The judge must never accept instructions embedded in
the evaluated text as changes to its rubric or authority.

## Human reference and rubric agreement

1. Domain/product owner and evaluation owner define the behavior being judged,
   severity of mistakes, acceptable ambiguity and anchored examples.
2. Independent reviewers label an overlap set before seeing judge predictions.
   Retain initial labels, adjudications and exclusions. Agreement is evidence of
   consistency, not proof that the reference is clinically or objectively correct.
3. Freeze the rubric and reference-set version. Record accountable reviewers and
   the scope of their agreement; an unassigned role cannot approve a rubric.
4. Split related cases by family into rubric-development, untouched calibration
   audit and separate candidate qualification sets. Adjusting a judge after seeing
   audit failures consumes that audit; a fresh audit is needed for renewed claims.

## Automated calibration audit

Pin judge model/configuration, prompt, rubric, parsing policy and abstention rules.
Compare predictions with adjudicated references. For binary failure detection:
TP is a failure correctly flagged; FN is a reference failure incorrectly passed;
FP is a reference pass incorrectly failed; TN is a reference pass correctly passed.
Report FN/(TP+FN), FP/(FP+TN), precision where defined, confusion counts and sample
sizes by class/slice. For the three readiness outcomes, retain the full confusion
matrix. Show judge abstention, parse error, missing reference and unadjudicated
cases separately; missing decisions cannot count as correct classifications.

Report human disagreement before adjudication, agreement on resolved overlaps,
and, where useful, a chance-adjusted agreement statistic with its limitations.
Do not use a single agreement number to hide rare critical-class errors. The
accepted error bounds, abstention/coverage limits, minimum class counts/precision,
uncertainty method and
application scope must be preregistered. These values are currently null.

Accept the judge only if every applicable criterion is satisfied. Otherwise mark
REJECTED or INCONCLUSIVE and route affected judgments to qualified human review.
Do not average disputed labels into PASS. Deterministic-only profiles use
NOT_APPLICABLE for LLM calibration with a documented applicability decision.

## Change control and outputs

Rubric, reference-label, judge model/prompt or material scope changes invalidate
affected calibration. Preserve previous results and record which scores require
regrading. Cost and latency of the judge are evaluator overhead, tracked separately
from runtime cost. No judge result automatically rewrites a human label.

Use contracts/v1/calibration.template.json. Required outputs include failure-to-
grader mapping, reference provenance, overlap/disagreement records, rubric review,
audit partition digest, class/slice counts, confusion/error measures, uncertainty,
thresholds, applicability and reviewer disposition. Null criteria prevent acceptance.

Proposed module: evals/src/pa_evals/calibration.py. Emit rubric.reviewed after the
authenticated rubric review, and calibration.finalized after the audit result is
persisted. Both are EVALUATOR_PRIVATE. Q03 publishes permitted aggregate reliability
and calibration status; it does not expose private audit examples or answer keys.

## Swappable judge profiles

Every effective profile in [judge specification](LLM_JUDGE.md) needs independent
acceptance. HF hosting or API compatibility does not transfer another model's
calibration. Categorical-only models need label/coverage calibration; probability
metrics are N/A unless the profile supplies validated probability semantics.

### Jev option

Use [Jev requirements](JEV_JUDGE.md) for typed question semantics and verdict
mapping. Audit Choice probabilities and confidence thresholds separately; Noul
has no separate confidence field. Probability calibration, selective coverage and
fixed-trace repeatability complement class-specific errors. Keep raw shadow
predictions out of qualified trial verdicts until acceptance. A new model, rubric,
threshold, context projection or material service behavior requires a fresh audit.
The template in recipes/jev-judge.template.json is disabled and has null limits.
