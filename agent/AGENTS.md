# Codex instructions — Agent policy

Read the root AGENTS.md and docs/ARCHITECTURE.md first.

Ownership: Own prompts, observation-to-model-request construction, tool/answer proposal parsing, and workflow strategy.

Boundary: Do not execute tools, issue approvals, read hidden oracles, own credentials, or decide deployment.

Build the interfaces before framework integrations. Use dependency injection and
typed failures. Preserve synthetic/read-only defaults. Keep raw private evidence
and credentials out of tests, debug output, and committed examples.

Verify these behaviors before marking the component implemented:
- Confirmed blockers yield NOT_READY; otherwise unverifiable required evidence yields UNKNOWN.
- Foreign document instructions cannot change the action catalog.
- An agent cannot directly call a payer or instantiate a privileged tool client.

Update this component's README with the actual API, command, tests, and remaining
gaps. Run the structural check and the relevant implemented tests. Do not invent
test results for future files or treat a mock as a real model/client run.
