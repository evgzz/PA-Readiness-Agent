# Task 00 — contracts, packaging and configuration

Status: COMPLETE_FOR_CONTRACT_LAYER | Date: 2026-09-24.
No agent, live model, external tool or production workflow was executed.

## Implemented

- Installable Python package with independent component namespaces and zero runtime
  third-party dependencies. setuptools 84.0.0 is the selected build dependency.
- One runtime-loop port with injected metered model and authorized tool gateways.
  Domain dataclasses are data, not credentials or execution capabilities.
- Strict JSON decoding, owned-schema validation and reproducible PA-JSON-1 hashing.
- Runtime-input allowlists, scope checks, typed proposals and mock/read-only config.
- 29 event payload schemas, eight workflow-record schemas and six structured metric
  value schemas, plus active/legacy envelope validation.
- An ingress function that requires an injected Authenticator and validates trusted
  producer instance/channel/evidence-class/actor grants, payload digest and record
  consistency before returning immutable event bytes.
- Metric/result missingness rules, evaluation/gate precedence, and plan-digest checks.
- Standard-library tests and an installed CLI that validates local record files.

## Commands and evidence

```bash
python3 -m pip install --no-deps .
pa-contracts runtime-config recipes/runtime-config.example.json
python3 scripts/run_contract_tests.py
python3 scripts/check_scaffold.py
```

Local installation was also checked with --no-build-isolation into an isolated
scratch target using the already installed pinned build dependency. No global
provider dependency or credential was introduced. See artifacts/TASK00_VALIDATION.json
for executed results. The example run budgets are explicitly synthetic development
fixtures; they do not supply qualification thresholds or release authorization.

## Migration and limitations

Specification version is 1.0; initial distribution version is 0.1.0. These are
separate version axes. New executable record schemas are package resources;
historical draft schemas/templates remain intact for traceability. Active ingress
accepts v1 envelopes only. The v0.2 archival reader returns a dict, never an accepted
ingestion record. Transport versions do not automatically upgrade payloads.

A recorded workflow has status RECORDED. A completed experiment plan has explicit
criteria and plan_digest over PA-JSON-1 bytes with only plan_digest omitted. For
complex template fields, follow the packaged schema (typed intervals, class counts,
cost records, constraints and cohort/window records); do not copy null templates
into a runtime and interpret them as configured defaults. Contract validity does
not establish reference truth, calibration adequacy or permission to execute.

The owned-schema validator is deliberately limited, rejects unsupported keywords,
and is not a general Draft 2020-12 engine. Producer authentication is checked via
a required verifier port; actual token/mTLS/identity-provider verification must
be supplied by the deployment composition. No permissive default exists. Python
import/dataclass boundaries do not establish process isolation. Reference access,
statistical computation, family-split provenance, repeated-trial independence,
durable transactions, idempotent ingestion and replay protection remain later tasks.

## Next task

Task 01: deterministic synthetic case/requirements/evidence/validation adapters,
reset receipts, reviewed cases and grouped data manifests. Preserve FOUND versus
CONFIRMED_ABSENT versus UNAVAILABLE/AMBIGUOUS. Do not enable real FHIR writes or claim
benchmark coverage from the three existing public interface examples.
