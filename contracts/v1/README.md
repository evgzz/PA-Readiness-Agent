# V1 workflow field contracts

Status: DRAFT_TEMPLATES_ONLY. These files describe required record fields. They
are not accepted labels, executed plans or computed results. Executable record
validators now live in pa_contracts.workflows and packaged workflow-*.json schemas.
Null means unassigned/unknown; empty lists are placeholders, not evidence of zero
failures. Completed records require status RECORDED and populated typed fields; the unchanged
draft templates intentionally fail validation. Workflow execution remains Tasks 04/06.

| Template | Use |
|---|---|
| review-batch.template.json | Frozen population, selection method and review accountability |
| annotation.template.json | Observable behavior, trace evidence, hypothesis and adjudication |
| failure-taxonomy.template.json | Versioned category definitions; no observed categories yet |
| calibration.template.json | Expert references, rubric review, independent audit and reliability |
| experiment-plan.template.json | Preregistered controlled comparison and acceptance criteria |
| experiment-result.template.json | Paired results, uncertainty, constraints and selection decision |
| monitoring-plan.template.json | Simulated windows, sampling, signals, triage and access |
| monitoring-window.template.json | Versioned observations, completeness, label maturity and signal |

Writer identity is verified server-side; a JSON actor_id is not authentication.
Retain append-only versions and digest-protected references in controlled stores.
Review, calibration, experiment and raw monitoring records are evaluator-private.
Governance emits authorized aggregate/alert projections without hidden labels.

V1 event producers use ../schemas/event-envelope-v1.schema.json with schema_version
1.0. The retained v0.2 schema and scripted example are legacy illustrations. Old
readers reject unknown event types; migration must route by declared version and
retain original bytes. Re-enveloping creates a new event with a provenance link.
No in-place rewriting of historical evidence is permitted.
