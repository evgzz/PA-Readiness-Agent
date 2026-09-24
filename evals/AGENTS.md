# Codex instructions — Evaluation system

Read the root AGENTS.md and docs/ARCHITECTURE.md first.

Ownership: Own cases/splits, reset/replay, independent oracles, code graders, judge calibration, analysis, and release evidence.

Boundary: Do not expose test expectations to the agent, let candidates edit graders, or convert missing execution to PASS.

Build the interfaces before framework integrations. Use dependency injection and
typed failures. Preserve synthetic/read-only defaults. Keep raw private evidence
and credentials out of tests, debug output, and committed examples.

Verify these behaviors before marking the component implemented:
- Missing/duplicate trials and mixed candidate identities prevent qualification.
- Judges are checked against independently adjudicated labels.
- Dev-selected candidates and thresholds are frozen before independent test access.

Update this component's README with the actual API, command, tests, and remaining
gaps. Run the structural check and the relevant implemented tests. Do not invent
test results for future files or treat a mock as a real model/client run.
