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

## V2 completion requirements

Implement docs/CI_EVALUATION.md and docs/ADVERSARIAL_EVALUATION.md. Add T0–T3
with explicit required-tier policy, secret isolation, reset/replay and complete
evidence. Map ASI01–10 and governance records; run actual attacks on the isolated
endpoint and turn confirmed successes into reproductions/failing regressions,
then mitigation/retest. Preserve no-success outcomes honestly. Demonstrate code
checks on all admitted synthetic traffic and sampled frozen judges, correction
limits, alert triage and missing-data controls; production remains NOT_SCOPED.

## Plan 1.1 implementation slice

Implement frozen candidate/profile dependency resolution before P7: core P5/P6A/P6E plus feature-triggered evidence, all P6 for full program. UNKNOWN features and missing mandatory controls cannot produce GO.

Corresponding specs: [comparison](../../ARCHITECTURE_COMPARISON.md),
[qualification profiles](../../QUALIFICATION_PROFILES.md),
[delivery plan](../../PHASED_DELIVERY_PLAN.md). Status remains unchanged; these are planned additions.
