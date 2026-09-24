# NVIDIA role and open-asset mapping

The supplied JR2024325 JD informs this program design. It is not an NVIDIA
implementation, endorsement, internal standard, or proof of role experience.

| Responsibility | Specification / artifact | Demonstration still required |
|---|---|---|
| Identify/select/execute agentic-safety evals | eval catalog, coverage matrix, EVALUATIONS.md | Executed multi-turn, unsafe-tool, autonomy and multi-step cases |
| Findings to accountable mitigation | findings register and governance closure policy | Assigned owners/dates, observed failure, change, retest and regression |
| End-to-end Nemotron safety planning | model registry, safety plan, dependencies, candidate manifest | Exact model and serving pins, resources, schedule, actual results |
| Security/frontier/agentic/hallucination programs | scoped risk catalog and explicit exclusions | Intended-use review; additional workstreams where applicable |
| Multi-turn/modal/lingual/context/reasoning/release coverage | dimensioned coverage records | Executed slices; English-text initial scope cannot imply broader coverage |
| Severity/release/escalation/exception governance | severity policy, gate and authorization records | Authenticated decisions, expiry, escalation and recovery exercised |
| Dashboards and executive reporting | metric registry, instrumentation, report specification | Reconciled metrics and source-linked reports from actual runs |

Open models: swappable artifact/serving records, with Nemotron unconfigured.
Open data: reviewed fictional development cases and generation provenance.
Open tools: documented ports, validators and reproduction recipes.
Held-out answers and private runtime evidence retain separate access controls.

NeMo Agent Toolkit, NeMo Evaluator and NeMo Gym remain optional future integration
candidates from the original scaffold. No integration or benchmark score is claimed.
This PA application program cannot establish comprehensive base-model frontier
risk or safety across untested domains, languages, modalities and releases.
