# Runtime harness specification

Status: PLANNED. Proposed code locations are listed in `docs/REPO_MAP.json`.

## Admission and termination

Authenticate caller; derive trusted scope; validate input schema and selected
configuration; allocate session/run identifiers; reserve budgets; persist a
start record; select one loop implementation. Reject unconfigured real adapters
before execution. A local draft profile may operate without a real model, but
its evidence class must identify the mock.

Terminal outcomes distinguish completed assessment, budget exhaustion, policy
denial, unavailable dependency, cancellation, and runtime error. Preserve the
partial trajectory and unresolved checks. If the runtime cannot produce a valid
assessment, return a typed execution error plus unresolved product state; do not
invent a complete answer merely to satisfy a schema.

## Tool lifecycle

| Stage | Required record | Enforcement |
|---|---|---|
| Proposal received | Logical action ID; proposed tool and safe argument digest | Schema, allowed tool catalog, operation classification |
| Authorization | Actor/scope reference; policy/configuration; ALLOW or DENY | Caller, tenant, patient, request, destination, evidence freshness |
| Dispatch preparation | Attempt ID; approval reference if applicable; idempotency key | Persist intent before dispatch; atomically reserve allowed action |
| Dispatch | Endpoint identity; start time; budget state | Scoped credentials and adapter validation |
| Receipt | Service operation/request ID; response/effect reference | Preserve ambiguous outcomes and partial effects |
| Reconciliation | Confirmed effect, confirmed no effect, or unresolved | Query authoritative service/world state before consequential retry |

Read access and data disclosure are effects too. HTTP 200 alone does not establish
case correctness, readiness, permitted disclosure, or absence of side effects.
Record the proposed violation separately from whether a control blocked it.

For a future consequential operation, planned states are PROPOSED → DENIED, or
PROPOSED → AUTHORIZED → DISPATCH_PENDING → DISPATCHED → CONFIRMED / FAILED_NO_EFFECT /
RECONCILIATION_REQUIRED. These are lifecycle states, not evaluation verdicts.
On restart, DISPATCH_PENDING/DISPATCHED with insufficient external evidence must
be reconciled. Never automatically reuse consumed approval after an unknown effect.

## Budgets, retries, concurrency

- Freeze per-run step, tool, model, time, and cost caps. Model-provided confidence
  cannot override a cap. Budget fields left null block that runtime profile.
- Retry only typed eligible failures, with bounded attempts and elapsed-time cap.
  Distinguish a transport attempt from a logical action and from an effect.
- Serialize or otherwise atomically protect action reservations and approval
  consumption. Two concurrent requests cannot independently consume one approval.
- Expose cancellation and partial results. Restoring conversational memory cannot
  restore revoked permissions or stale evidence.

## Output and evidence validation

Validate the agent's answer against known predicates and acquired evidence, not
against hidden evaluation labels. An unsupported READY proposal must not pass
through; retain the proposal and validation failure, and produce UNKNOWN unless
a confirmed blocker establishes NOT_READY. Keep both proposed and delivered
answers so evaluations can distinguish model behavior from system protection.

Do not conflate local validation with payer policy correctness. Standards package,
profile, terminology, business requirement, and validator versions must be pinned
when used. Current standards pin templates remain unconfigured.

## Instrumentation and failure policy

The authorization/action ledger is required evidence. If required evidence cannot
be persisted, prevent consequential dispatch; fail or terminate the qualification
trial as unresolved. A failure of optional dashboard export can be buffered while
the ledger remains durable. Record export delay and failure explicitly.

The SDK's default tracing/export settings must be reviewed and explicitly
configured before use. Allowlisted destinations, input/output content controls,
and egress verification are part of integration acceptance; disabling a vendor
export must not remove the independent action ledger.

## Acceptance checks to implement

1. Valid read-only case completes and retains all required evidence.
2. Injection or a model-supplied actor/patient/destination cannot change authority.
3. Direct/alternate tool paths cannot bypass authorization; normal permitted reads work.
4. Unavailable evidence yields UNKNOWN absent a confirmed blocker; confirmed
   absence yields NOT_READY when the requirement makes absence a blocker.
5. Budget exhaustion, malformed response, timeout, and cancellation preserve gaps.
6. Output validator records proposed false READY and blocks its delivery.
7. Future durable profile: crash/restart, duplicated events, concurrent approvals,
   revoked approval, changed packet, and ambiguous service effects are reconciled.

These are acceptance requirements, all NOT_RUN in this repository.

## V2 operation risk tiers

[V2 scope](V2_GAP_FIXES.md) defines R0 case-scoped reads, R1 local packet/assessment
drafts, R2 future consequential operations (disabled), and R3 prohibited behavior.
These are operation authorization tiers, separate from incident severity S0–S3
and any legal risk classification. Enforce each tier in trusted policy code even
when the model is compromised; user/tool text cannot upgrade its authority.

V2 tests future R2 approval binding, expiry, replay, concurrent consumption and
ambiguous receipts only in an isolated simulator. This does not enable submission,
external handoff or real clinical effects. Input/output guards complement
scope enforcement and cannot substitute for it. See [adversarial acceptance](ADVERSARIAL_EVALUATION.md).
