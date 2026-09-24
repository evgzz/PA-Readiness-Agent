# Shared contracts

Package: pa_contracts. Status: IMPLEMENTED_CONTRACT_LAYER (Task 00).
The package has no runtime dependency outside Python's standard library.
Agent, harness, SDK adapters and evaluation execution remain unimplemented.

## APIs

| Module | Implemented boundary |
|---|---|
| validation | Strict JSON loading; duplicate/nonfinite/deep/oversized input rejection; owned-schema validation |
| serialization | PA-JSON-1 canonical bytes and SHA-256 digests |
| configuration | Explicit bounded mock/read-only profile and scope-claim validation |
| runtime_ports | One RuntimePort with injected metered model and authorized tool gateways; allowlisted input/proposal parsers |
| evidence_ports | Authenticator, immutable ValidatedEvent bytes, EvidenceWriter, MetricSnapshotPort and GatePort |
| workflows | Eight workflow-record validators; metric, evaluation and gate consistency checks |
| cli | Local validation command; never executes an agent or tool |

Executable schemas are packaged in src/pa_contracts/resources/. There are 29
closed event payload schemas, eight workflow schemas and six structured metric
value schemas. The event catalog selects the permitted payload type for each
producer/channel. Root schemas retain the historical draft format and versioned
envelopes; they do not supersede the packaged executable record contracts.

## Validate locally

```bash
python3 -m pip install --no-deps .
pa-contracts runtime-config recipes/runtime-config.example.json
python3 scripts/run_contract_tests.py
python3 scripts/check_scaffold.py
```

Python 3.12+ is required. Build dependency setuptools is pinned in pyproject.toml.
The dependency inventory covers only selected build/runtime components; no model
SDK has been selected. The example budget is a synthetic contract fixture, not a
production or qualification policy.

## Versioning and semantic limits

Strict records require schema_version 1.0. Unknown versions and fields fail.
Legacy v0.2 envelopes have a separate read-only archival validator and cannot
enter active ingestion. Draft workflow templates intentionally fail execution
validation until completed. Do not mutate archived bytes during migration.

PA-JSON-1 sorts object keys, emits UTF-8 compact JSON, preserves array order and
uses Python JSON number rendering. It rejects nonfinite numbers, non-string keys,
unsafe integers and malformed Unicode. It is not RFC 8785, a signature or an
universal cross-language number representation. Store the serialization version
with digests. Event payload SHA-256 always covers original retained bytes.
Experiment plan_digest covers canonical record bytes with only plan_digest omitted.
Other digest fields reference separately retained records; cross-record resolution
and protected storage are work for later tasks.

The validator implements only the closed keyword vocabulary documented in
validation.py. It rejects unsupported keywords across all branches and does not
claim full Draft 2020-12 conformance. Authentication, access control and independent
label provenance do not follow from a valid JSON object. Scope dataclasses and
proposals are never capabilities. Stored reference strings must be resolved and
authorized by the owning integration; this package does not read arbitrary URLs.

Workflow validation checks shape and local consistency, not human judgment,
statistical adequacy, full trial scheduling, unique family partitions or release
eligibility. Metric computation remains Task 04; gate computation remains Task 06.
See docs/TASK00_HANDOFF.md for exact verification and remaining work.
