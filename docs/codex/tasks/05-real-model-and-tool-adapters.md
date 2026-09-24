# Selected real runtime and tool adapters

Status: PLANNED. Read root/scoped AGENTS.md, SPEC.md and relevant ADRs.

## Build
Select and pin one real model/serving configuration and its evidence/data profile. Implement the proposed OpenAI Agents SDK adapter as the exclusive real loop with gateway-backed tools and metered model transport. Verify export destinations and SDK bypass paths. Actual FHIR/requirements clients need explicit endpoint and standards pins. Missing dependencies remain NOT_CONFIGURED.

## Completion evidence
Observed real-model tool/structured-output behavior; all effects pass controls; no silent mock/model fallback; controlled telemetry/inference destinations; actual trial evidence. Missing credentials do not prevent finishing useful local work.

## Handoff
Record changed files, exact commands, actual results, evidence locations and
remaining inputs in component documentation and docs/BUILD_STATUS.json. Keep
evidence classes separate. Never invent test counts, model pins, owners or dates.

## V1 completion requirements

Collect the actual real-agent synthetic baseline needed by V1-A. Retain failed
requests, usage gaps and complete trace links. Return observed development traces
to Task 04 for human error analysis; do not delay review until a dashboard exists.

## Swappable judge provider integration
Add independently metered HF dedicated endpoint, supported closed API, optional HF
router and Jev adapters specified in docs/LLM_JUDGE.md. Jev is one option; pin
typesafe-sdk only when selected. Verify model/deployment identity and capabilities,
bound retries and budgets, and retain every attempt's usage/error evidence.
Missing configuration must make zero network calls. Live synthetic integration
proves transport only; return to Task 04 for independent human calibration.

For HF, bind Hub commit, serving engine/image, served-model ID and deployment
configuration. Verify schema support, cold-start/unavailability and time-based
compute billing. For closed APIs, use an explicit native/compatible protocol and
record hosted identity limits. HF Providers is a distinct pinned routing option.

## V2 completion requirements

Choose one supported runtime/model and one necessary judge path, independently.
Use docs/LLM_JUDGE.md; Jev is optional, HF Endpoints require deployable/licensed
artifacts, and API-only closed models use supported APIs. Preserve configuration
freeze, no silent fallback and recalibration on swaps. Provide an isolated running
synthetic endpoint for promptfoo, with pinned request/response/identity adapters.
Meter native usage, caching and router calls; verify provider capabilities before
the preregistered caching/cascade experiment. No external effects are enabled.
