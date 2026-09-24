# Contracts, packaging and configuration

Status: COMPLETE_FOR_CONTRACT_LAYER. Read root/scoped AGENTS.md, SPEC.md and relevant ADRs.

## Build
Finalize package configuration and dependency lock only for selected integrations. Preserve pure contracts and independent component imports. Specify RuntimePort, metered model/tool gateways, evidence writer, evaluator result, metric snapshot and gate interfaces. Implement event-specific payload schemas, authentication checks at ingress, and version negotiation; draft envelope validation alone is insufficient.

## Completion evidence
Malformed scope, unknown enum/version, forged producer/channel and unsupported payload fail. Candidate/evaluation manifests hash reproducibly. No hidden label appears in runtime input. Import boundaries verified.

## Handoff
Record changed files, exact commands, actual results, evidence locations and
remaining inputs in component documentation and docs/BUILD_STATUS.json. Keep
evidence classes separate. Never invent test counts, model pins, owners or dates.

## V1 completion requirements

Finalize v1 review/annotation/taxonomy/calibration/experiment/monitoring field
contracts and payload validators; support the versioned v1 event envelope while
preserving historical v0.2 evidence. Validate required values before a template
can become an executable plan. Implement Q metric result fields and N/A rules.

## Execution evidence

See docs/TASK00_HANDOFF.md and artifacts/TASK00_VALIDATION.json. Runtime credential
verification adapters and durable ingestion wiring remain integration work; the
required verifier interface and fail-closed ingress checks are implemented.

## V2 completion requirements

Existing Task 00 execution remains complete for its original contract scope.
V2 extensions are NOT_IMPLEMENTED: versioned nested-span/usage fields, review
saturation, confusion/coverage detail, fixed-k results/missingness bounds,
prevalence method/results, CI tier and adversarial lineage, caching/cascade and
upgrade records. Specify required values and validators before execution; keep
the draft v2 learning/acceptance templates disabled. Do not change active M/Q
formulas or accept unknown event fields implicitly. See docs/V2_MEASUREMENT.md
and docs/INSTRUMENTATION.md.
