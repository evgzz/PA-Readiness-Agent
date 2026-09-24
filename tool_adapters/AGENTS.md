# Codex instructions — Tool adapters

Read the root AGENTS.md and docs/ARCHITECTURE.md first.

Ownership: Own scoped FHIR/resource retrieval, requirement lookup, validation clients, typed evidence, and actual effect receipts.

Boundary: Do not grant authority based on prompt text, accept foreign resource lineage, or silently treat outages as absence.

Build the interfaces before framework integrations. Use dependency injection and
typed failures. Preserve synthetic/read-only defaults. Keep raw private evidence
and credentials out of tests, debug output, and committed examples.

Verify these behaviors before marking the component implemented:
- FOUND, CONFIRMED_ABSENT, UNAVAILABLE, and AMBIGUOUS are distinct.
- Tenant/patient/request scope is enforced before returning any data.
- FHIR transport success does not imply profile, business-rule, or readiness validity.

Update this component's README with the actual API, command, tests, and remaining
gaps. Run the structural check and the relevant implemented tests. Do not invent
test results for future files or treat a mock as a real model/client run.
