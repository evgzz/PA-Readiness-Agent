# Codex instructions — Runtime adapters

Read root AGENTS.md, SPEC.md, relevant ADRs and docs/codex/BUILD_SEQUENCE.md.
Own exactly one selected execution loop per run and SDK-specific translation. Use injected model/tool gateways; never instantiate an alternate privileged client or a second competing loop.

Import shared contracts and approved third-party integrations only in their owning
adapter; no direct imports from other implementation packages. Concrete wiring is
in apps/. Preserve synthetic/read-only defaults and required evidence independently
of telemetry delivery. Keep qualification labels, credentials, and private records
outside agent access and public exports. Verify consequential boundaries and record
actual results. Planned modules remain NOT_IMPLEMENTED until built and checked.
