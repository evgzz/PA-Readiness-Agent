# Tool adapters

Package: pa_tools. Implementation status: DRAFT_INTERFACES_ONLY.

Own scoped FHIR/resource retrieval, requirement lookup, validation clients, typed evidence, and actual effect receipts.

Do not grant authority based on prompt text, accept foreign resource lineage, or silently treat outages as absence.

Planned implementation files under src/pa_tools: synthetic.py, fhir_read.py, requirements.py, validator.py, review_draft.py.
Only files physically present are supplied; planned paths are not implemented.

Acceptance:
- FOUND, CONFIRMED_ABSENT, UNAVAILABLE, and AMBIGUOUS are distinct.
- Tenant/patient/request scope is enforced before returning any data.
- FHIR transport success does not imply profile, business-rule, or readiness validity.

Follow AGENTS.md here and the root build sequence.
