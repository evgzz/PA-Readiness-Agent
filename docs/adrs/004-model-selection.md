# ADR 004: Separate model selection from orchestration

Status: PROPOSED | Date: 2026-09-24 | Implementation evidence: NOT_RUN
Accountable decision owner: UNASSIGNED.

## Context
A runtime choice does not establish model capability or pin a checkpoint.

## Proposed decision
Retain a model registry and model adapters. Nemotron is a candidate with null checkpoint/revision/serving fields until selected and tested.

## Alternatives considered
Hardwire one hosted model, or select multiple models immediately.

## Consequences and limitations
Protocol compatibility does not prove tool, schema, context, reasoning, or modality compatibility. Hosted revision immutability limits must be disclosed.

## Acceptance evidence required
Exact artifact/provider identity, tokenizer/template/quantization/serving settings, license review, and observed capability checks.

## Revisit trigger
Revisit when acceptance fails, intended-use or deployment requirements change,
or a pinned dependency changes materially. Record the superseding ADR and rerun
affected qualification; do not silently change the baseline.

References: [source register](../SOURCES.md), [system specification](../../SPEC.md).
