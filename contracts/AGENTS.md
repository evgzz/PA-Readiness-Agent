# Codex instructions — Shared contracts

Read the root AGENTS.md and docs/ARCHITECTURE.md first.

Ownership: Own minimal versioned types, ports, schemas, and canonical serialization rules shared across components.

Boundary: Do not import agent frameworks, provider SDKs, domain clients, hidden oracles, or runtime implementations.

Build the interfaces before framework integrations. Use dependency injection and
typed failures. Preserve synthetic/read-only defaults. Keep raw private evidence
and credentials out of tests, debug output, and committed examples.

Verify these behaviors before marking the component implemented:
- Unknown enum values and incompatible versions are rejected.
- Proposal fields cannot mint execution capabilities.
- Schema changes have compatibility tests and migration notes.

Update this component's README with the actual API, command, tests, and remaining
gaps. Run the structural check and the relevant implemented tests. Do not invent
test results for future files or treat a mock as a real model/client run.
