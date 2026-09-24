# PA Readiness

Repository: [evgzz/PA-Readiness-Agent](https://github.com/evgzz/PA-Readiness-Agent)

A reproducible foundation for assessing prior-authorization packet readiness and
managing the safety evidence for each application release.

**Specification version: 1.0 — 2026-09-24. Status: CONTRACTS_READY.**
This revision supplies specifications, proposed ADRs, contracts, templates, and
Codex build instructions. Agent execution, harness enforcement, evaluation,
telemetry export, dashboards, and release gates remain **NOT_IMPLEMENTED**.
Task 00 implements installable contracts, authenticated ingress validation and
25 standard-library boundary tests. The agent loop remains unimplemented.

## Responsibilities

| Component | Owns |
|---|---|
| Agent | Evidence interpretation, workflow policy, tool/answer proposals |
| Harness | Trusted scope, authorization, budgets, durable action state, output validation |
| Runtime adapter | Exactly one selected agent loop per run: mock first; OpenAI Agents SDK proposed for real integration |
| Evals | Independent cases, labels, repeated trials, graders, calibration, metrics |
| Governance | Findings, exceptions, release-gate computation, separate authorization records |
| Telemetry | Event validation, redaction, correlation, controlled export |
| Reporting | Read-only views of versioned metrics, findings, and gate snapshots |

**Agent proposes; harness authorizes; evals measure; governance decides; reporting displays.**
Product outcomes are `READY / NOT_READY / UNKNOWN`. Evaluation outcomes are
`PASS / FAIL / UNRESOLVED`. Gate outcomes are `GO / NO_GO / INCONCLUSIVE`.
`GO` means eligible for release approval; it is not deployment authorization.
`READY` never means payer approval, medical necessity, or permission to submit.

## Initial operating scope

One fictional PA case at a time, read-only evidence retrieval and validation,
English text, bounded multi-step interaction, and a local review packet. External
submission, clinical writes, cancellation, external messages, unrestricted tools,
and autonomous delegation are disabled. Missing evidence stays visible.
The three retained public cases are interface examples, not a qualified dataset.

## Repository map

| Path | Purpose |
|---|---|
| `SPEC.md` | Revised requirements, scope, semantics, acceptance criteria |
| `AGENTS.md` | Repository-wide Codex instructions |
| `agent/`, `harness/`, `evals/` | Independent core package skeletons |
| `runtime_adapters/` | Mock and SDK loop adapters, planned |
| `model_adapters/`, `tool_adapters/` | Model and FHIR/tool boundaries |
| `contracts/` | Draft interfaces, schemas, event and metric registries |
| `telemetry/` | Export and data-policy adapter skeleton |
| `governance/` | Gate package skeleton, severity policy, approval templates |
| `program/` | Evaluation catalog, coverage requirements, findings, dependencies |
| `models/`, `data/`, `tools/` | Asset registries, provenance, cards, licenses |
| `recipes/` | Explicit run profiles and configuration templates |
| `apps/reporting/` | Dashboard/report specification; no running application |
| `releases/` | Candidate evidence index and gate/authorization templates |
| `docs/adrs/` | Twenty-four proposed architecture decisions and alternatives |
| `docs/codex/` | Eight implementation tasks with v1 completion requirements |
| `scripts/`, `.github/workflows/` | Static scaffold validation |
| `artifacts/` | Reviewed static-check evidence; no live performance claims |

## Proposed technology profile

- Python packages with framework-independent contracts.
- Deterministic mock loop first. OpenAI Agents SDK is the proposed real-runtime
  adapter; the OpenAI API client is a separate model-transport concern.
- Local evidence artifacts and CI scorecards first; optional GitHub Projects for
  work tracking, with versioned exports for release snapshots.
- OpenTelemetry-compatible observability; Langfuse is the proposed trace platform.
- Durable application PostgreSQL when persistence is implemented. A self-hosted
  Langfuse deployment has its own platform services and data stores.
- Jev is the planned semantic judge; typed criteria, trajectory grading and human
  calibration are specified in [Jev judge](docs/JEV_JUDGE.md). Integration is disabled.
- Nemotron remains an unconfigured candidate: checkpoint, serving backend,
  tokenizer, license, and capability checks are not selected.

Braintrust, Arize Phoenix, LangGraph, Metabase, and Grafana remain recorded
alternatives. LangChain is optional. No vendor dependency is installed or locked
by this specification. See [ADR register](docs/adrs/README.md).

## Read and build

Start with [SPEC](SPEC.md), [architecture](docs/ARCHITECTURE.md),
[harness](docs/HARNESS.md), [evaluations](docs/EVALUATIONS.md),
[instrumentation](docs/INSTRUMENTATION.md), and
[dashboards/reports](docs/DASHBOARDS_REPORTS.md).
Follow [build sequence](docs/codex/BUILD_SEQUENCE.md) and scoped `AGENTS.md` files.

The contract package requires Python 3.12+. Run:

```bash
python3 -m pip install --no-deps .
pa-contracts runtime-config recipes/runtime-config.example.json
python3 scripts/run_contract_tests.py
python3 scripts/check_scaffold.py
```

The scaffold checker checks structure and selected import invariants. Contract
tests exercise executable validators for the owned schema vocabulary; they are
not full JSON Schema conformance tests or agent qualification. Packaging has no
runtime dependencies; its selected build dependency is pinned. Runtime commands
and model integration remain future tasks.

## Dashboard contract

Every displayed value identifies its candidate, configuration, metric definition,
evidence class, denominator where applicable, source snapshot, and freshness.
Missing evidence is `NOT_RUN`, `UNRESOLVED`, or `N/A`; it is never silently zero.
Reference checks, scripted demonstrations, real-agent synthetic trials, and
production observations are separate evidence classes.

## Open assets and evidence

Models: exact artifact references and model cards. Data: fictional development
inputs with provenance; held-out inputs and labels remain evaluator-controlled.
Tools: documented interfaces, validators, and reproduction recipes.
Publication rights and licenses are reviewed per asset; this revision grants no
new license and bundles no model weights. See [open assets](docs/OPEN_ASSETS.md).

Do not copy prior course-module counts into this repository's results. Read
[migration](docs/COURSE_MIGRATION.md) before porting code. Keep protected evidence
and secrets outside Git. See [status](docs/BUILD_STATUS.json),
[v1 revision notes](docs/REVISION_1_0.md), and [Git handoff](docs/GIT_HANDOFF.md).

## V1 learning workflow

Read [v1 requirements](docs/V1_GAP_FIXES.md) and the
[worked example](docs/WORKED_EXAMPLE.md). The example is an execution contract,
not a completed case study. Its missing evidence is explicit.

1. Build the bounded baseline and collect real-agent synthetic traces.
2. Review a declared sample; label symptoms, refine failure categories and prioritize.
3. Map failures to deterministic checks or independently calibrated semantic rubrics.
4. Preregister one change and measure quality, safety, latency and cost on paired cases.
5. Retain the decision, regressions and source-linked report; freeze selection
   before independent qualification.
6. Exercise monitoring with synthetic windows and triage; production stays unscoped.

The learning scorecard adds Q01 review coverage, Q02 failure categories, Q03
calibration, Q04 legitimate completion, Q05 latency, Q06 cost per success, Q07 paired
comparisons, Q08 monitoring coverage and Q09 behavioral signals. Every measure has
an authoritative definition in contracts/metric-definitions.json. M01–M06 remain
the release/program scorecard. See [dashboard mapping](docs/DASHBOARDS_REPORTS.md)
for tracking methods and [instrumentation](docs/INSTRUMENTATION.md) for capture points.

New procedures: [human review](docs/ERROR_ANALYSIS.md),
[calibration](docs/EVALUATOR_CALIBRATION.md), [experiments](docs/EXPERIMENTS.md),
[monitoring](docs/MONITORING.md). Draft record templates are in contracts/v1/.
No runtime command, selected provider, executed experiment or performance gain is
implied. All workflow implementation and real-agent evaluation remain pending.

## Implementation checkpoint

Task 00 is complete for the contracts layer. See [handoff](docs/TASK00_HANDOFF.md)
for APIs, migration rules, executed checks and deferred integrations. Task 01
(synthetic tools, requirements and reviewed case families) is next.
