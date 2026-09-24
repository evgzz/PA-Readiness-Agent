# Harness and single mock loop

Status: PLANNED. Read root/scoped AGENTS.md, SPEC.md and relevant ADRs.

## Build
Implement trusted admission, budgets, authorization gateway, adapter scope checks, local action journal and output validation. Implement one mock runtime adapter and wire it in apps/. Emit required domain records independently of optional telemetry. Keep consequential operations disabled and real integrations NOT_CONFIGURED.

## Completion evidence
Forced violations denied, authorized reads succeed, proposed false READY blocked, scope/budget/cancellation/timeout checks preserve evidence. Declare local journal limitations; do not claim production durability.

## Handoff
Record changed files, exact commands, actual results, evidence locations and
remaining inputs in component documentation and docs/BUILD_STATUS.json. Keep
evidence classes separate. Never invent test counts, model pins, owners or dates.
