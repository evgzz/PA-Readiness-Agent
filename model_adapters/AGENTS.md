# Codex instructions — Model adapters

Read the root AGENTS.md and docs/ARCHITECTURE.md first.

Ownership: Own inference protocol translation, model identity, structured-response normalization, usage metering, and provider error mapping.

Boundary: Do not hard-code provider APIs inside the agent, execute PA tools, or silently substitute models/mocks.

Build the interfaces before framework integrations. Use dependency injection and
typed failures. Preserve synthetic/read-only defaults. Keep raw private evidence
and credentials out of tests, debug output, and committed examples.

Verify these behaviors before marking the component implemented:
- Unconfigured endpoints return NOT_CONFIGURED, with no network call.
- Provider timeouts/malformed tool outputs become typed errors.
- Exact model/server/tokenizer/template settings and native billing semantics are recorded.

Update this component's README with the actual API, command, tests, and remaining
gaps. Run the structural check and the relevant implemented tests. Do not invent
test results for future files or treat a mock as a real model/client run.
