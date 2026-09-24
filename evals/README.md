# Independent evaluation

Package: `pa_evals`. Status: NOT_IMPLEMENTED.
Own independent labels, schedules, resets, graders, calibration, completeness and
run metric computation. Emit private graded evidence and authorized summary
snapshots. Governance separately computes the release gate from these records.
See [evaluation specification](../docs/EVALUATIONS.md). Keep hidden labels outside
runtime/optimizer access. Planned modules are listed in docs/REPO_MAP.json.

## V1 scope
Planned modules review.py, calibration.py, experiments.py, comparisons.py and
monitoring.py implement the linked v1 procedures under independent evaluation
authority. All remain NOT_IMPLEMENTED. Draft records live in contracts/v1/;
Q01–Q09 definitions live in contracts/metric-definitions.json. Required verification
covers sampling provenance, duplicate reviews, calibration leakage, paired-case
missingness, full cost accounting and missing-data versus behavioral signals.

## Swappable judge plan
[Judge specification](../docs/LLM_JUDGE.md) adds planned judges.py and trajectories.py.
They own atomic rubrics, prefix/full-trajectory projection and calibrated verdicts.
No JudgePort, provider calls or live calibration are implemented by this update.
Task 04 owns these additions; Task 05 supplies the independently metered adapter.

Jev is optional. Selection, calibration acceptance and regrading bind an effective
profile; provider swaps preserve rubric semantics and original result lineage.
