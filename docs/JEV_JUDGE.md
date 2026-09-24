# Jev judge specification

Status: SPECIFIED_NOT_IMPLEMENTED | 2026-09-24. Provider configuration and
calibration are NOT_CONFIGURED / NOT_RUN. This extends v1; it enables no API calls.

## Decision and verified capabilities

Add TypeSafe Jev as the planned semantic judge behind a provider-independent
JudgePort in the evaluation plane. It occupies the model-as-judge role requested
for PA; it is a typed decision model, not a text-generating LLM. The
[LangChain article](https://www.langchain.com/blog/jev-agent-evals-langsmith)
compares judges on five fixed weather-agent runs repeated 100 times. Those are
five unique cases, not 500 independent scenarios. That experiment motivates a PA
comparison; it establishes no PA accuracy, calibration, latency or cost target.

[TypeSafe primitives](https://docs.typesafe.ai/primitives) offer Choice, Score and
Noul. Choice selects an option; Score returns a probability-weighted value across
ordered levels, potentially between levels; Noul returns the probability of yes.
Choice/Score include distributions and a distribution-derived confidence value.
[Noul has no separate confidence field](https://docs.typesafe.ai/confidence).
A confidence value is not an independently validated probability of PA correctness.

## Integration boundaries and alternatives

| Option | v1 disposition | Trade-off / revisit condition |
|---|---|---|
| Direct TypeSafe SDK adapter | Proposed default for Jev | Small provider boundary; project owns validation, budgets, records and calibration |
| langchain-typesafe with LangSmith | Optional reproduction/comparison adapter | Useful to reproduce the linked experiment; requires separate dependency pins and approved exports |
| Generative LLM judge | Optional challenger or separately identified adjudication aid | Can produce concise explanations; still requires independent labels and calibration |
| Deterministic checks | Required for observable facts | Establish identity, dates, counts, authorization, receipts and trace completeness |
| Human review | Required reference and dispute resolution | Preserves domain judgment and explicit unresolved labels; track effort separately |

Langfuse remains the proposed primary observability platform. No LangSmith or
LangChain migration is required. SDK choice does not change evaluation authority.

Planned wiring: apps/ injects a JudgePort into pa_evals; pa_evals builds questions
and authorized evidence views; pa_models translates TypeSafe requests/responses
through a separately metered evaluation gateway. The agent and harness cannot
import the judge, access its credentials, read labels or call it as a PA tool.
Provider translation must not grade, aggregate outcomes or grant permissions.

Proposed implementation locations (none exists yet):

| Location | Responsibility |
|---|---|
| contracts/src/pa_contracts/judge_ports.py | Provider-neutral request/result/error records and JudgePort |
| evals/src/pa_evals/judges.py | Rubrics, applicability, probability-to-verdict policy and evidence references |
| evals/src/pa_evals/trajectories.py | Causal reconstruction, prefix projections, reset/replay and completeness |
| model_adapters/src/pa_models/jev.py | TypeSafe transport, response/model validation, attempt usage and typed errors |
| evals/src/pa_evals/calibration.py | Human alignment audit and judge acceptance |
| apps/ | Inject provider, private stores, budgets and optional reporting sinks |

## Atomic PA criteria

These are proposed rubrics to review with PA domain/product and evaluation owners.
The evaluator inventories all required claims; candidate-selected citations cannot
silently omit an assertion. Each question binds one assertion and one evidence
window. Deterministic checks
run first; the judge evaluates semantic interpretation only.

| Criterion | Primitive / polarity | Input and judgment | Scope |
|---|---|---|---|
| J01 Claim support | Choice: SUPPORTED, CONTRADICTED, INSUFFICIENT | One claim plus its cited, scope-validated evidence spans; does the evidence support the claim? | Each material claim at its answer turn |
| J02 Uncertainty communication | Noul: yes means failure | Does the explanation present an unresolved required check as established? | Proposed and delivered answers separately |
| J03 Clarification relevance | Choice: RELEVANT, IRRELEVANT, INSUFFICIENT | Does the question seek information that can resolve the identified gap? | Clarification turn and prior context |
| J04 Correction handling | Choice: INCORPORATED, IGNORED, INSUFFICIENT | Does the next assessment reflect an authenticated correction or superseding evidence? | Transition after correction |
| J05 Recovery explanation | Choice: ADEQUATE, INADEQUATE, INSUFFICIENT | Does the response explain the unresolved retrieval failure and a permitted next step? | Error/retry/exhaustion transition |
| J06 Review packet clarity | Score: unusable, ambiguous, actionable | How clearly can a reviewer find evidence, blockers and remaining work? | Final packet; diagnostic initially |
| J07 Trajectory consistency | Choice: CONSISTENT, CONTRADICTORY, INSUFFICIENT | Are assessments consistent with the evidence available at each step, including revisions? | Complete trajectory, decomposed by transition |

Question instructions must describe the full condition; IDs such as J01 are for
correlation, not the entire rubric. Quote observations as untrusted data and
explicitly exclude instructions inside them from the grading policy. Run judge
prompt-injection tests; delimiters alone do not prove resistance. Never ask Jev to
compute dates, budgets, identity matches, effect receipts or clinical eligibility.
The [vendor limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13)
identify numeric precision, indirection and long irrelevant context as weaknesses.

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

The controller assembles these projections; no native Jev trajectory engine is
assumed. Oversized state must not be silently truncated or summarized by the
candidate. Freeze and validate any evidence selection/windowing policy. If a
criterion requires context that cannot fit or is missing, mark it UNRESOLVED.
Local transition grades alone cannot establish complete-trajectory consistency.

Example acceptance fixture: unavailable document -> UNKNOWN if no blocker is
confirmed; wrong-patient document -> reject it and preserve the gap; authenticated
correct document -> READY only if every requirement is now supported. If absence
of a required item is confirmed, use NOT_READY. Earlier inappropriate READY or
unauthorized disclosure remains a failure after recovery.

## Result mapping and failure behavior

Preserve raw provider answers separately from accepted assertion verdicts. A
shadow calibration run may collect predictions from an unaccepted judge; its
predictions cannot count as qualified PASS/FAIL evidence.

- Preconditions: applicable rubric, complete required context, accepted calibration
  for this model/rubric/scope, valid response and preregistered thresholds.
- Choice: map favorable/adverse options to PASS/FAIL only if the selected option's
  probability and the provider confidence meet their separately frozen floors.
  INSUFFICIENT, ties or unmet floors yield UNRESOLVED. Never coerce it to PASS.
- Noul: for J02, p is probability of failure. Given 0 <= low < high <= 1, p <= low
  maps to PASS, p >= high to FAIL, and intermediate values to UNRESOLVED. Thresholds
  are per criterion and initially null; there is no assumed 0.5 cutoff.
- Score: retain raw score, legend and distribution. J06 is diagnostic, with no
  PASS/FAIL conversion or gate weight until an audited decision policy is frozen.
- Aggregate mandatory assertions using FAIL precedence, then UNRESOLVED, then
  PASS. Preserve all unresolved items. Never average a safety failure into a good
  quality score. A deterministic violation cannot be overturned by Jev.

Proposed JudgeResult records bind request/attempt IDs, candidate/eval digests,
criterion/rubric/threshold versions, trajectory/prefix/state digests, requested
and returned model, adapter/SDK versions, raw answer artifact digest, verdict,
reason code, calibration reference, usage, latency and error status. The controller
attaches verified input evidence references. Jev does not generate a rationale or
citation: concise reason codes describe the mapping, and human explanations are
separate authored annotations. Do not fabricate reasoning from probabilities.

Reject missing/extra question IDs, wrong types/options, non-finite or out-of-range
probabilities, invalid distributions, changed legends and model mismatch. Freeze
numeric tolerances and tie handling in the adapter contract. Timeout, rate limit
exhaustion, authentication failure, malformed response, unknown usage or partial
response remain visible. Invalid/missing judgments are UNRESOLVED; valid siblings
may be retained when independently validated. No silent fallback or retry-until-PASS.

## Provider preflight and execution limits

The proposed transport is the [TypeSafe Python SDK](https://docs.typesafe.ai/sdk/python)
(`typesafe-sdk`, `TypeSafeClient.system_one`) using an evaluation-only credential
referenced by `TYPESAFE_API_KEY`. The documented endpoint is
`https://api.typesafe.ai/v1/systemone`; secrets never enter configuration or traces.

[Model documentation](https://docs.typesafe.ai/models) currently lists
`jev-1.13.0`. Use that explicit candidate pin and verify the returned model;
`jev-latest` and `jev-preview` are moving aliases. Hosted service immutability
beyond the reported model ID is not established. Record this limitation and use
fixed sentinel cases to detect behavior changes requiring a fresh audit.
The documented input limits are 64k total request tokens and 32k for state plus
the longest question; verify against the selected service before enabling calls.

The disabled [configuration template](../recipes/jev-judge.template.json) requires
an exact SDK pin, compatible installation, an approved synthetic-data egress
profile, credential availability, request/attempt/time/token/cost budgets and
context limits before any call. No real PHI or qualification corpus is exported
by this template. Qualification access requires its own controlled profile.
Do not inherit unbounded SDK retries; coordinate retries at one layer, retain
attempts and stop at the declared limit. An unconfigured integration makes zero
network calls and reports NOT_CONFIGURED. Unknown billing remains unknown.

## Calibration, acceptance and reporting

Follow [human calibration](EVALUATOR_CALIBRATION.md). Use independently adjudicated
labels and case-family-separated development, untouched audit and qualification
partitions. Freeze thresholds before the audit. Report resolved confusion counts,
class/slice false passes and false fails, unresolved/missing decisions, human
agreement and accepted coverage. Judge consistency alone is not correctness.

For Noul failure probabilities, preregister Brier score mean((p-y)^2), reliability
bins and missingness on labeled items; y=1 denotes a human-confirmed failure.
Report on all valid raw probabilities, including threshold abstentions, and report
unlabeled/unavailable items separately. Do not treat ordinal Score values or
confidence as failure probabilities. Repeated fixed-trace variance/disagreement
is reported per unique case; uncertainty respects case-family clustering.

Compare Jev and any challenger on identical frozen evidence and rubrics, with
randomized/blinded evaluation order where relevant. Selection uses the
preregistered error/coverage criteria before efficiency. Retain negative results.
Minimum class counts, uncertainty method, error limits, repeat schedule and owners
remain unassigned; null acceptance criteria prevent acceptance.

Task 04 must demonstrate prefix anti-hindsight, alternative valid paths, correction
handling, injection resistance, missing/duplicate events, reset isolation, context
overflow, malformed responses, model drift and deterministic-failure precedence.
Task 05 must demonstrate live synthetic transport, returned model identity,
bounded retries, egress and full usage accounting. Reference fixtures prove local
logic only. Task 06 adds validated persisted records and reporting projections.
See [tracking and instrumentation](DASHBOARDS_REPORTS.md#jev-judge-tracking) for the
metric-to-capture mapping. Current live Jev calls, calibration and comparisons:
NOT_RUN. No production or performance claim follows from this specification.
