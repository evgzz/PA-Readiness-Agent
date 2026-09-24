# Revised Codex build sequence

Eight implementation tasks; all PLANNED. Numerical order establishes the main
dependencies. Read-only report rendering can start after Task 04 and governance
fixtures in Task 06 without waiting for real-model access. No parallel agents are required.

| Task | Build | Status |
|---|---|---|
| 00 | [Contracts, packaging and configuration](tasks/00-contracts-and-packaging.md) | PLANNED |
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
