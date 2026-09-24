# Contracts, packaging and configuration

Status: PLANNED. Read root/scoped AGENTS.md, SPEC.md and relevant ADRs.

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
