# Agent policy and deterministic model

Status: PLANNED. Read root/scoped AGENTS.md, SPEC.md and relevant ADRs.

## Build
Implement pure agent instructions, evidence handling and typed proposals. Build deterministic model behavior behind the ModelPort. Keep runtime execution, tool authority, private oracles and credentials outside pa_agent. Retain proposed versus delivered outcomes for later protection analysis.

## Completion evidence
READY supported, confirmed blockers NOT_READY, unavailable evidence UNKNOWN absent blocker; no invented references; no direct I/O; malformed outputs and clarification budgets handled.

## Handoff
Record changed files, exact commands, actual results, evidence locations and
remaining inputs in component documentation and docs/BUILD_STATUS.json. Keep
evidence classes separate. Never invent test counts, model pins, owners or dates.

## V2 completion requirements

Preserve bounded multi-turn clarification, contradictory/stale evidence and
correction/recovery scenarios. Agent consumes only permitted current observations;
do not put expected labels, full world facts or evaluator controls in its context.
Distinguish attempted and delivered answers and decisions at each prefix. The
mock model supplies explicit controls, not real-agent review evidence.
