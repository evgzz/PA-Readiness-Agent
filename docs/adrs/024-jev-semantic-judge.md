# ADR 024: Use swappable semantic judge adapters; retain Jev as an option

Status: PROPOSED | Date: 2026-09-24 | Implementation evidence: NOT_RUN
Accountable decision owner: UNASSIGNED.
Revision 1.1 amends this proposed decision from Jev-first to provider-neutral
selection. The filename is retained for existing links; no implemented behavior
or previously accepted calibration is superseded.

## Context
PA semantic grading needs atomic criteria, trajectory evidence and human alignment.
Model and hosting choices must be replaceable without changing the PA rubric or
transferring trust from one judge to another.

## Proposed decision
Use JudgePort with explicit profiles for HF dedicated endpoints, supported closed
model APIs, optional HF Inference Providers and Jev. No default judge is selected.
Prefer HF dedicated hosting for deployable weights with verified rights and serving
compatibility. API-only closed models use a supported service route. Keep Jev as
an optional typed decision model through TypeSafe; do not assume HF hosting.
Freeze each effective profile per evaluation run and calibrate independently.
Keep deterministic checks authoritative and human labels independent.

## Alternatives considered
| Option | Disposition / trade-off |
|---|---|
| Jev-only grading | Rejected as the exclusive architecture; retained as an option |
| HF dedicated hosting | Preferred for deployable weights; adds engine, deployment and compute-cost ownership |
| Closed vendor API | Supported option; less artifact visibility and provider-specific behavior |
| HF Inference Providers | Optional supported pair; routing identity must be pinned |
| Automatic best-score fallback | Rejected; creates selection bias and obscures failures |
| Preregistered calibrated fallback chain | Future optional composite policy; default NONE |
| Deterministic and human checks | Required foundations; semantic automation remains independently audited |

## Consequences and limitations
Multiple adapters need conformance tests, native billing and profile-level
calibration. Typed Jev probabilities, generative labels and ordinal scores retain
their own semantics. No API call, endpoint deployment, new runtime loop or platform
migration is enabled by the specification.

## Acceptance evidence required
Common contracts and parsers; adapter capability and identity checks; HF cold-start
and compute-cost accounting; supported closed API calls; no unplanned fallback;
profile-specific human audits; trajectory evidence; reproducible report projections.
All live integration and calibration remain pending.

## Revisit trigger
Revisit on model/deployment drift, changed rubric/context/decision policy, failed
calibration or changed scope. Regrade with new lineage and preserve old results.

References: [common specification](../LLM_JUDGE.md), [Jev option](../JEV_JUDGE.md),
[sources](../SOURCES.md), [ADR 010](010-evaluation-authority.md).
