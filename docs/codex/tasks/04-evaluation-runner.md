# Independent evaluation and metric computation

Status: PLANNED. Read root/scoped AGENTS.md, SPEC.md and relevant ADRs.

## Build
Implement isolated SystemUnderTest controller, grouped schedules, reset/replay, deterministic graders, completeness checks and M01–M03 computation. Add semantic judge calibration only where needed. Preserve missing, duplicate, error and unresolved trials. Finalize result and metric snapshots from fixed definitions.

## Completion evidence
Known failure detection, legitimate positive controls, oracle isolation, absent receipt behavior, candidate mismatch, missing/duplicated trial detection and deterministic recomputation. Report cases separately from repeated trials.

## Handoff
Record changed files, exact commands, actual results, evidence locations and
remaining inputs in component documentation and docs/BUILD_STATUS.json. Keep
evidence classes separate. Never invent test counts, model pins, owners or dates.

## V1 completion requirements

Implement docs/ERROR_ANALYSIS.md and docs/EVALUATOR_CALIBRATION.md. Add review
selection, append-only annotations, adjudication, taxonomy versions and mapping to
graders. Compute Q01–Q06 as applicable; retain label provenance and unknown costs.
First exercise contracts on reference fixtures, then return to this task after
Task 05 supplies actual real-agent development traces. No fixture may be presented
as observed real-agent failure. Verify duplicate review handling, sampling labels,
class-specific judge errors and untouched calibration-audit separation.
