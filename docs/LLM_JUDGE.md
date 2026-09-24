# Swappable LLM and decision-model judge specification

Status: SPECIFIED_NOT_IMPLEMENTED | Revision: 1.1 | 2026-09-24.
No judge is selected by default. All provider adapters and live calibration remain
pending. This revision makes Jev one option alongside open-weight and closed
models; it replaces the earlier Jev-first selection language.

## Selection and hosting options

Keep the PA rubric, trajectory controller and JudgePort independent of model and
hosting service. Select one explicit, versioned judge profile per evaluation run.
Hugging Face (HF) Inference Endpoints is the preferred deployment route when model
weights are available and permitted to be deployed; it is not a universal proxy
for proprietary model APIs.

| Judge option | Route | Selection requirements / limitations |
|---|---|---|
| Open-weight generative LLM | HF dedicated Inference Endpoint | Exact Hub revision, license/access, compatible inference engine and capability checks; model family alone is not a pin |
| Private or licensed deployable model | HF dedicated Inference Endpoint, optionally custom container | Requires access to weights, deployment rights and compatible serving artifacts; a private repository is not itself a license |
| Closed API-only LLM | Vendor-native API or a verified compatible gateway | Pin available model/version and endpoint; unavailable weights cannot be assumed deployable on HF |
| HF Inference Providers model | HF router, only for a verified supported model/provider pair | Distinct service from dedicated Endpoints; freeze provider routing and record hosted-version limits |
| Jev | TypeSafe API behind its typed adapter | Optional decision-model judge; no HF hosting or OpenAI-compatible interface is assumed |

HF's [dedicated chat tutorial](https://huggingface.co/docs/inference-endpoints/tutorials/chat_bot)
demonstrates an OpenAI-compatible chat endpoint. Its
[custom-container support](https://huggingface.co/docs/inference-endpoints/guides/custom_container)
allows supplied serving images and model artifacts. The
[Providers API](https://huggingface.co/docs/inference-providers/tasks/chat-completion)
is a separate routed service. These capabilities do not establish support for
every model, engine, JSON schema or proprietary vendor. Verify the selected pair.

Model candidates can come from families such as Qwen, Llama, Nemotron or other
eligible models; no particular checkpoint is selected or qualified here. Open
weights, source availability, license, private visibility and hosted API access
are separate registry attributes. Record them separately.

Langfuse remains the proposed trace platform; LangSmith and langchain-typesafe
remain optional experiment adapters. Human review supplies independent references
and resolves disputes. Deterministic checks remain authoritative for observable
facts, authorization, effects, identity, dates, budgets and completeness.

## Common contract and component ownership

apps/ injects JudgePort into pa_evals. pa_evals owns evidence projections, rubrics,
output interpretation and calibration; pa_models owns transport, provider identity,
usage and typed errors. A separate evaluation gateway enforces destinations and
budgets. No judge SDK, credential or hidden label enters the agent/harness runtime.
Judges receive no action tools and cannot authorize PA operations or releases.

| Planned location | Responsibility |
|---|---|
| contracts/src/pa_contracts/judge_ports.py | Provider-neutral JudgeRequest, JudgeObservation, JudgeResult and error records |
| evals/src/pa_evals/judges.py | Rubric rendering, capability checks, normalized verdicts and applicability |
| evals/src/pa_evals/trajectories.py | Causal reconstruction and decision-time/full-trajectory evidence |
| model_adapters/src/pa_models/hf_endpoint.py | Dedicated endpoint transport and deployment identity |
| model_adapters/src/pa_models/hf_providers.py | Explicit HF router model/provider selection and identity |
| model_adapters/src/pa_models/closed_api.py | Selected vendor-native or verified compatible API translation |
| model_adapters/src/pa_models/jev.py | TypeSafe typed questions and answers |
| evals/src/pa_evals/calibration.py | Human alignment, coverage, uncertainty and acceptance per judge profile |
| apps/ | Concrete wiring, credentials, stores and optional reporting sinks |

These interfaces/modules are planned. Implementation must add versioned schemas,
validators, registry entries and conformance tests before accepting the records.
Do not insert draft fields into current Task 00 event/metric schemas.

JudgeRequest binds a trusted profile reference, candidate/evaluation identities,
criterion/rubric version, authorized evidence window, allowed evidence IDs and
context digest. Reference labels remain outside the inference request.
JudgeObservation preserves the raw provider output and its kind:
CATEGORICAL, ORDINAL or PROBABILITY. JudgeResult binds observation, accepted
PASS/FAIL/UNRESOLVED, reason code, evidence references and calibration reference.
An ordinal diagnostic can have a value without an accepted assertion verdict.

Both records retain provider, transport, requested/observed model, effective
profile digest, endpoint/deployment identity, SDK/engine versions, request/attempt
IDs, trajectory/prefix/turn/step IDs, generation settings, raw artifact digest,
usage, cost basis, latency and error status. Store only secret references.

## Common PA rubric and response interpretation

The evaluator inventories all required assertions; candidate-selected citations
cannot omit claims. Each criterion has applicability, evidence requirements and
anchored examples reviewed by PA domain/product and evaluation owners.

| Criterion | Judgment | Unit | Canonical semantic outcomes |
|---|---|---|---|
| J01 Claim support | Does scoped cited evidence support the claim? | Each material claim at its answer turn | SUPPORTED / CONTRADICTED / INSUFFICIENT |
| J02 Uncertainty communication | Does the answer present an unresolved required check as established? | Proposed and delivered answers separately | FAILURE / NO_FAILURE / INSUFFICIENT |
| J03 Clarification relevance | Can the clarification resolve the identified gap? | Clarification prefix | RELEVANT / IRRELEVANT / INSUFFICIENT |
| J04 Correction handling | Does the assessment incorporate an authenticated correction? | Correction transition | INCORPORATED / IGNORED / INSUFFICIENT |
| J05 Recovery explanation | Does the answer explain the failure and a permitted next step? | Error/retry/exhaustion transition | ADEQUATE / INADEQUATE / INSUFFICIENT |
| J06 Review packet clarity | Can a reviewer find evidence, blockers and remaining work? | Final packet | Unusable / ambiguous / actionable; diagnostic only |
| J07 Trajectory consistency | Do assessments respect the evidence available at each step? | Complete trajectory, decomposed by transition | CONSISTENT / CONTRADICTORY / INSUFFICIENT |

Generative profiles request one strict JSON response containing criterion_id,
semantic_outcome (or J06 ordinal level), evidence_ids from the supplied allowlist,
and an optional concise evidence-based explanation. Full rubric instructions and
observations remain separately identified; instructions embedded in observations
have no rubric authority. Pin the prompt rendering and test injection resistance.
No private chain-of-thought is required or stored.

For generative models, valid categorical output maps through a calibrated label
policy; no invented probability field is required. INSUFFICIENT, refusal, missing
context or invalid output yields UNRESOLVED. Prompted confidence and token
log-probabilities are not substitutes for validated failure probabilities. If a
profile later uses either, define its meaning and audit it separately. J06 ordinal
labels and Jev's weighted Score values are different scales; compare them only
under an explicit validated mapping.

[Jev-specific mapping](JEV_JUDGE.md) renders the same rubric as Choice/Score/Noul
questions and applies separately calibrated probability/confidence thresholds.
Retain raw values; do not fabricate generated explanations for Jev. The controller
attaches verified input evidence references. Generated explanations from other
models remain claims, with references checked against the input allowlist.

An accepted semantic verdict requires complete evidence, valid response and
accepted calibration for the effective profile. Shadow audit predictions from an
unaccepted judge are retained but cannot supply qualified PASS/FAIL evidence.
Aggregate mandatory assertions with FAIL precedence, then UNRESOLVED, then PASS.
A judge cannot erase a deterministic violation or an earlier trajectory failure.
Diagnostic quality scores do not average away mandatory failures.

Reject malformed JSON, unknown/missing/duplicate criterion IDs, invalid enums,
unsupported fields, foreign evidence IDs and invalid numeric values. A structurally
valid explanation is not proof of factual support. Test hallucinated citations,
refusal, output truncation, duplicate keys, model mismatch and partial responses.
Validated independent sibling judgments may survive a failed batch item; preserve
all scheduled items and missingness. No silent coercion, repair or retry-until-PASS.
A separately audited bounded repair procedure would be a new profile version.

## Multi-turn trajectory protocol

A trajectory is one trial's ordered interaction, not a bag of final responses.
Retain trajectory_id, trial_id, turn_id, step_id, causal parent IDs, producer
sequence, before/after observable-state digests, policy and evidence revisions,
reset receipt, proposed/delivered outputs and terminal reason. State means
observable application facts, not private model chain-of-thought.

1. Reconstruct the causal graph from complete persisted records. Validate scope,
   provenance, required steps, valid partial orders and receipts in code. Accept
   equivalent permitted tool paths; do not require one exact tool-call sequence.
2. Freeze each decision prefix using only observations available at that decision.
   Later corrections must never improve the grade of an earlier unsupported READY.
   Expected labels and human verdicts are excluded from the provider request.
3. Grade atomic claims and transitions on their minimal sufficient evidence.
   Preserve clarification, contradiction, revision, stale evidence, tool failure,
   retries, budget exhaustion and session-isolation cases as separate slices.
4. Grade whole-trajectory obligations after termination, retaining prefix findings.
   A successful ending cannot erase an earlier confirmed mandatory failure.
5. Replay the identical frozen state/question bytes to measure judge repeatability.
   Separately reset and rerun the agent to measure trajectory variability. A judge
   regrade is not a new agent trial. Keep both repetition IDs and denominators.

The controller assembles these projections; no native provider trajectory engine is
assumed. Oversized state must not be silently truncated or summarized by the
candidate. Freeze and validate any evidence selection/windowing policy. If a
criterion requires context that cannot fit or is missing, mark it UNRESOLVED.
Local transition grades alone cannot establish complete-trajectory consistency.

Example acceptance fixture: unavailable document -> UNKNOWN if no blocker is
confirmed; wrong-patient document -> reject it and preserve the gap; authenticated
correct document -> READY only if every requirement is now supported. If absence
of a required item is confirmed, use NOT_READY. Earlier inappropriate READY or
unauthorized disclosure remains a failure after recovery.

## HF dedicated endpoint profile

The planned hf_endpoint adapter supports a verified OpenAI-compatible chat
interface, or an explicitly implemented engine-specific protocol. The
[HF tutorial](https://huggingface.co/docs/inference-endpoints/tutorials/chat_bot)
shows base URL, served-model name and token configuration. Do not equate an HF
Hub repository ID with the served model identifier expected by the endpoint.
A compatible API shape does not prove semantic or structured-output equivalence.

Before enabling the profile, freeze:

- Hub repository and exact commit; weight/tokenizer digests, chat-template hash,
  quantization, license/access record and any custom code review.
- Endpoint/deployment revision and served-model identifier; cloud/region,
  hardware, inference engine/version, container image digest and configuration.
- Credential reference, approved destination/data profile, network/access mode,
  payload/logging policy and verified capabilities for this model and engine.
- SDK version, rubric/prompt/context projection, output schema, parsing policy,
  generation settings and limits. Record unsupported settings explicitly;
  temperature zero or a seed does not establish deterministic output.
- Total context/input/output limits, concurrency, timeouts, retry count, request
  and compute budget, replica/scale-to-zero policy and ownership of shutdown.

HF [configuration](https://huggingface.co/docs/inference-endpoints/guides/configuration)
supports a model repository commit revision and deployment settings. Preserve a
configuration snapshot: the URL alone cannot prove which artifacts were served.
Record returned identity plus verified deployment metadata; if the service cannot
prove immutable identity, disclose the limit and apply the preregistered identity
policy. Reject unexpected model/deployment changes rather than silently relabeling.

Explicitly verify schema support on the chosen engine. If constrained output is
unavailable, either reject the profile as UNSUPPORTED_CAPABILITY or use a separately
versioned, audited strict-JSON prompt/parser profile. Never silently downgrade.
HF's [structured-output guide](https://huggingface.co/docs/inference-providers/guides/structured-output)
likewise recommends selecting a specific model/provider for compatibility.

Separate queue/cold-start time from warm inference and total logical-call latency.
Health checks and warmup requests are distinct from evaluation trials and still
consume resources. Preserve retry attempts under one retry controller. Unavailable
endpoint, timeout or exhausted rate limits leave affected judgments unresolved.
Provisioning, resuming, scaling and deleting endpoints are operator actions outside
JudgePort. The disabled templates do not provision resources or make live calls.

## Closed APIs and HF routing

Closed API profiles use a supported vendor-native adapter or a tested compatible
API; protocol selection is explicit. Pin available model revision and capture
provider fingerprints where exposed without claiming weight immutability. Verify
context, refusal, JSON/schema, usage, reasoning controls and retention/egress for
the actual endpoint. Missing information stays unknown.

HF Inference Providers is optional when the required model/provider pair is
available. Freeze both identities and disable implicit auto/fastest/cheapest
routing for qualification. A served open-weight model does not become a closed
model merely because a commercial provider hosts it. Do not claim API-only
proprietary models or Jev are available through HF without verified support.
A custom proxy hosted on HF would remain a proxy to an external service; it would
not establish that model weights or inference stay inside the dedicated endpoint.

## Swapping and fallback policy

[Selection template](../recipes/judge-selection.template.json) chooses an explicit
profile reference. Each adapter normalizes its observations to the common rubric;
agent code and the evaluation controller do not change with the provider.

1. Choose the proposed profile, route and exact configuration; validate capabilities,
   deployment rights, approved destinations and limits. Missing prerequisites return
   NOT_CONFIGURED before any inference network call.
2. Run synthetic conformance checks and shadow grading on development evidence.
   Freeze the profile and judge-specific decision policy before the untouched audit.
3. Independently calibrate that profile. Reuse a prior accepted audit only for the
   identical effective profile and valid declared scope; a different judge inherits
   neither another judge's thresholds nor its acceptance.
4. Select the accepted profile for a new evaluation configuration/run. Retain the
   previous profile/results. A regrade uses the same frozen evidence with a new
   grading version and lineage; it never overwrites original findings or labels.
5. Compare judges on the same evidence population. Record why the swap was selected,
   quality/coverage changes, cost and latency. Preserve negative comparisons.

Freeze the effective profile at run admission; configuration updates apply to the
next run. Default automatic fallback is NONE. An optional future fallback chain
must be preregistered and calibrated as a composite policy, with explicit error
triggers, approved data destinations and separately identified attempts/results.
Disagreement does not trigger score shopping. An unplanned fallback cannot rescue
a qualification score; mark affected evidence unresolved and start a new run.
Human adjudication is separately authored and never silently overwrites predictions.

Effective profile identity binds provider/route/model/deployment, SDK/engine,
rubric/prompt/schema/context, decision policy, generation and retry/fallback settings.
A model, serving, prompt, rubric or material scope change invalidates affected
calibration until re-audited. A connection-compatible swap is not a qualified swap.

## Calibration, accounting and acceptance

Follow [calibration](EVALUATOR_CALIBRATION.md): case-family-separated development,
untouched audit and qualification; independent labels; human disagreement;
class/slice false passes and false fails; abstention, parsing and missingness;
coverage and uncertainty. Minimum counts, limits and owners remain unassigned.
Blind candidate/judge identity where feasible and test self-preference, verbosity,
answer-order and injection effects. Compare repeated fixed traces separately from
rerunning the stochastic agent; cluster uncertainty by source case/family.

Probability-specific analysis is optional by capability. For validated Noul failure
probabilities use preregistered Brier score mean((p-y)^2), y=1 for human-confirmed
failure, and reliability bins on all valid labeled p, including threshold
abstentions. For categorical-only judges mark probability calibration N/A with
reason, and still require label/coverage calibration. Confidence is not accuracy.

[HF dedicated billing](https://huggingface.co/docs/inference-endpoints/pricing)
is based on deployed compute time, unlike a per-token-only estimate. Track total
billed/estimated endpoint time and replicas, including initialization and idle
capacity, then allocate a declared evaluation share without double counting.
Retain allocation method, workload/window and unallocated shared capacity. Vendor
API calls use their own versioned billing semantics. Missing cost stays unknown.
All judge overhead remains separate from agent runtime Q05/Q06.

Task 04: common contracts, rubric rendering, prefix completeness, response and
abstention mapping, calibration identity and swap/regrade lineage tests.
Task 05: provider adapters, capability checks, returned/deployed model identity,
bounded retries, endpoint unavailability, cold starts, egress and metering.
Task 06: validated private records, authorized projections and recomputable reports.
No mock establishes real provider behavior. Live provider calls, judge calibration,
comparisons and deployment remain NOT_RUN. See [dashboard mapping](DASHBOARDS_REPORTS.md#judge-options-and-swapping).
