# Telemetry

Package: pa_telemetry. Status: INGRESS_CONTRACT_IMPLEMENTED; export/durability pending.

validate_ingress in ingress.py requires an injected Authenticator. It validates
producer instance, channel and evidence-class grants, authorized actor claims,
active envelope/payload versions, payload hashes, applicable correlation IDs and
record consistency. It returns immutable original bytes for an EvidenceWriter.
There is no permissive default authenticator and no network endpoint.

The production composition must supply an actual credential verifier and protected
identity grants. Test verifiers are synthetic fixtures. A caller inside the trusted
process can construct Python objects; this module is not process isolation.

validate_legacy_envelope reads v0.2 archival envelopes without producing an
accepted ingestion record. It does not validate old payloads or silently upgrade them.

Durable storage, replay/deduplication, transport identity integration, redaction,
export destinations and recovery remain Task 06. No Langfuse/OpenTelemetry exporter
or external telemetry destination is enabled. Tests run with:

```bash
python3 scripts/run_contract_tests.py
```
