# Shared contracts

Package: `pa_contracts`. Status: DRAFT_INTERFACES_ONLY.
Own domain types, interface definitions, schemas, and the shared metric/event
registries. No provider/framework/network dependency belongs here.

Existing v0.1 proposal/readiness/eval-result schemas and `ports.py` are retained as
drafts. Version 0.2 adds an event envelope, event catalog, metric definitions, and
run/metric templates. Finalize the entire family in Task 00; do not imply the old
ports already implement the new runtime/ledger/gate boundary.

Candidate digest binds source, model, agent, prompt, runtime, tool, policy and
serving configuration. Evaluation digest binds dataset, schedule, reset, graders,
thresholds and qualification protocol. Record each manifest's serialization
version; hash its retained bytes with SHA-256. A hash provides integrity comparison,
not producer authentication or clinical truth.

The envelope omits raw payload contents and references a protected artifact.
Event-specific payload validators, producer authentication, schema migration,
canonical manifest serialization and digest verification are implementation work.
The scripted example is schema illustration, not a recorded run.

## V1 contracts
Version 1.0 extends the catalog with human review, rubric/calibration, experiment
and monitoring events. Use schemas/event-envelope-v1.schema.json for v1 producers;
the v0.2 schema and scripted example remain historical illustrations. Metric
registry 1.0-proposed preserves M01–M06 and adds Q01–Q09 in learning_metrics.
See [workflow field contracts](v1/README.md) for versioning and migration rules.
Event payload schemas, workflow validators and runtime authentication are still
TO_IMPLEMENT; draft templates are not evidence of completed work.
