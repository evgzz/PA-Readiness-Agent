# Revised Codex build sequence

Eight implementation tasks; Task 00 contracts complete, Tasks 01–07 PLANNED. Numerical order establishes the main
dependencies. Read-only report rendering can start after Task 04 and governance
fixtures in Task 06 without waiting for real-model access. No parallel agents are required.

| Task | Build | Status |
|---|---|---|
| 00 | [Contracts, packaging and configuration](tasks/00-contracts-and-packaging.md) | CONTRACTS_COMPLETE |
| 01 | [Synthetic world, requirements and grouped data](tasks/01-synthetic-tools-and-data.md) | PLANNED |
| 02 | [Agent policy and deterministic model](tasks/02-agent-and-mock-model.md) | PLANNED |
| 03 | [Harness and single mock loop](tasks/03-runtime-harness.md) | PLANNED |
| 04 | [Independent evaluation and metric computation](tasks/04-evaluation-runner.md) | PLANNED |
| 05 | [Selected real runtime and tool adapters](tasks/05-real-model-and-tool-adapters.md) | PLANNED |
| 06 | [Governance, instrumentation and evidence gates](tasks/06-ci-and-release-evidence.md) | PLANNED |
| 07 | [Reports, controlled improvements and qualification handoff](tasks/07-accuracy-cost-and-open-release.md) | PLANNED |

M1: Tasks 00–03. M2: Task 04. M3: Task 06 and reporting portion of 07.
M4: Task 05 real execution. M5: independently frozen qualification and authorization.
Preserve missing integration statuses; finish useful local work without inventing evidence.

## V1 dependency loop
Tasks 00–03 → minimal Task 04 → Task 05 actual synthetic traces → return to Task 04
for human review/calibration → Tasks 06–07 for CI, experiment and learning reports.
The eight files remain the work breakdown; numerical order is not a reason to
skip returning to measurement after real execution. Monitoring follows baseline
snapshots and is simulated in v1. Apply V1-A–F in docs/V1_GAP_FIXES.md; all are pending.

## V2 dependency loop and evidence gates

Read docs/V2_GAP_FIXES.md and docs/REVISION_2_0.md. Task 00's original contract
milestone is complete; implement its v2 schema extensions before emitting new
records. Task 01 is the next baseline build. Continue Tasks 02–03, minimal 04,
then 05 for actual synthetic traces, returning to 04 for review/calibration.
Complete 06–07 with tiered CI, adversarial regressions, reporting and measured
manual-fix/caching/cascade/upgrade exercises. V2-A–D replace the demonstration
checklist; V2-Q is separately frozen qualification. Every gate remains NOT_RUN.
Do not implement every optional judge/backend before collecting the first traces.

## Phased execution

Use [PHASED_DELIVERY_PLAN](../PHASED_DELIVERY_PLAN.md) for the next executable
increment and its entry/exit/DoD criteria. [PHASE_STATUS](../PHASE_STATUS.json)
records P0 original contracts complete, P1–P7 planned and P1 next. Tasks 00–07
remain component work packages; phase completion can cover only part of a task.
P1 builds the smallest path across Tasks 01–04 with only the required Task 00
extensions. P2 adds failure controls/CI; P3 adds one real model; P4 adds human
measurement; P5 measures one fix and adversarial regressions; P6 completes
reporting/cost/monitoring increments; P7 performs independent qualification.
