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

## Swappable judges and trajectories
Implement docs/LLM_JUDGE.md and the Jev option in docs/JEV_JUDGE.md: provider-neutral JudgePort and validated records,
atomic J01–J07 rubrics, causal prefix/full-trajectory views, threshold mapping,
shadow calibration and human audit. Add schemas before emitting new fields/events.
Verify anti-hindsight, correction/recovery, valid alternative paths, missing context,
invalid responses, abstention, label isolation and deterministic-failure precedence.
Keep status NOT_IMPLEMENTED until this work executes; this revision specifies it.

Verify shared-rubric rendering for typed and generative judges, categorical output
without fabricated confidence, configuration freeze, rejected uncalibrated swaps,
regrade lineage and disabled fallback. Compare judge profiles on identical evidence.
