# Codex instructions — Runtime harness

Read the root AGENTS.md and docs/ARCHITECTURE.md first.

Ownership: Own run supervision and the injected single-loop boundary, trusted scope, state, budgets, policy gateway, approval lifecycle, tracing, and effect reconciliation.

Boundary: Do not import hidden expected answers, score benchmark correctness, or trust model-supplied permission claims.

Build the interfaces before framework integrations. Use dependency injection and
typed failures. Preserve synthetic/read-only defaults. Keep raw private evidence
and credentials out of tests, debug output, and committed examples.

Verify these behaviors before marking the component implemented:
- A forced prohibited call produces a recorded denial and no effect.
- Changed packets invalidate approval; ambiguous effects stop retry.
- Timeout/crash/resume and duplicate requests cannot silently repeat consequential actions.

Update this component's README with the actual API, command, tests, and remaining
gaps. Run the structural check and the relevant implemented tests. Do not invent
test results for future files or treat a mock as a real model/client run.
