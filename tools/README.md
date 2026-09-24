# Open tool catalog

Document tool names, schemas, read/write classification, resource scope, typed
failures, timeouts, idempotency/effect semantics, and dependency/version identity.
Actual clients live in tool_adapters/. Policy is enforced by the harness and
service adapters; neither a model's reasoning nor this catalog grants authority.

Pin FHIR version, IG package/version, terminology, validator, endpoint contracts,
and expected profile rules before claiming conformance. The draft pins remain
unset rather than assuming a current PAS/DTR/CRD version fits the deployment.
