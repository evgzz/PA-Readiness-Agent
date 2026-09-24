# Governance, instrumentation and evidence gates

Status: PLANNED. Read root/scoped AGENTS.md, SPEC.md and relevant ADRs.

## Build
Implement pa_governance findings, verified closure, M04–M06, severity policy, exception validity and separate release authorization. Add telemetry projection/export and completeness reconciliation. Implement transactional state/outbox only for a selected durable profile, with crash/race checks. CI invokes the independent gates and emits source-linked scorecards.

## Completion evidence
NO_GO precedence, INCONCLUSIVE on missing requirements, expired exception and mismatched authorization rejection; finding reopen; ledger/export outage distinction. CI summaries are derived from retained results and never declare runtime safety from scaffold checks.

## Handoff
Record changed files, exact commands, actual results, evidence locations and
remaining inputs in component documentation and docs/BUILD_STATUS.json. Keep
evidence classes separate. Never invent test counts, model pins, owners or dates.

## V1 completion requirements

Add private v1 review/calibration/experiment events and authorized projections.
Run deterministic checks on changes; define the real-model CI tier and mark a
required skipped tier incomplete. Add governance alert records and the synthetic
monitoring exercise: unchanged window, behavior change, mix shift, source loss,
late labels and sparse data. No operational deployment is implied.
