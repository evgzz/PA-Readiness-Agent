# Architecture decision register

**All 25 decisions are PROPOSED; implementation acceptance is NOT_RUN.**
They record the revised baseline and alternatives, not an approved production stack.
Owner roles are unassigned. Adopt/reject/supersede each decision with rationale and evidence during implementation.

| ADR | Decision | Status |
|---|---|---|
| [001](001-component-boundaries.md) | Separate agent, harness, evals, governance and reporting | PROPOSED |
| [002](002-framework-independent-contracts.md) | Keep domain contracts independent of frameworks | PROPOSED |
| [003](003-single-runtime-loop.md) | Use one runtime adapter; propose OpenAI Agents SDK for real runs | PROPOSED |
| [004](004-model-selection.md) | Separate model selection from orchestration | PROPOSED |
| [005](005-telemetry-contract.md) | Use hybrid instrumentation and versioned event contracts | PROPOSED |
| [006](006-primary-observability.md) | Propose Langfuse as the primary trace platform | PROPOSED |
| [007](007-clickhouse-role.md) | Limit ClickHouse to analytical data | PROPOSED |
| [008](008-application-state.md) | Use PostgreSQL for the durable application profile | PROPOSED |
| [009](009-langfuse-services.md) | Declare the full self-hosted observability dependency set | PROPOSED |
| [010](010-evaluation-authority.md) | Keep independent evaluation authority | PROPOSED |
| [011](011-observability-alternatives.md) | Evaluate Braintrust and Arize Phoenix as alternatives | PROPOSED |
| [012](012-langchain-deferral.md) | Defer LangChain unless a specific integration needs it | PROPOSED |
| [013](013-durable-orchestration.md) | Revisit LangGraph for durable workflow requirements | PROPOSED |
| [014](014-execution-authority.md) | Enforce permissions outside the model | PROPOSED |
| [015](015-ci-evidence.md) | Use CI to preserve reproducible evidence | PROPOSED |
| [016](016-release-governance.md) | Separate gate computation, action approval and release authorization | PROPOSED |
| [017](017-metrics-as-contracts.md) | Version metric definitions and source snapshots | PROPOSED |
| [018](018-reporting-rollout.md) | Start with artifact scorecards and program records | PROPOSED |
| [019](019-durable-events.md) | Separate durable evidence from telemetry delivery | PROPOSED |
| [020](020-data-and-publication.md) | Separate open development assets from qualification evidence | PROPOSED |
| [021](021-human-error-analysis.md) | Human review precedes automated failure metrics | PROPOSED |
| [022](022-preregistered-improvement.md) | Preregister comparisons and account for full workload cost | PROPOSED |
| [023](023-monitoring-feedback.md) | Stage monitoring through synthetic exercises before operational use | PROPOSED |
| [024](024-jev-semantic-judge.md) | Use swappable HF/closed API judge adapters with Jev as an option | PROPOSED |
| [025](025-v2-evidence-gates.md) | Require course-aligned v2 evidence gates without expanding PA authority | PROPOSED |
