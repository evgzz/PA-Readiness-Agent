# Agent policy

Package: pa_agent. Implementation status: DRAFT_INTERFACES_ONLY.

Own prompts, observation-to-model-request construction, tool/answer proposal parsing, and workflow strategy.

Do not execute tools, issue approvals, read hidden oracles, own credentials, or decide deployment.

Planned implementation files under src/pa_agent: workflow.py, prompt_builder.py, proposal_parser.py.
Only files physically present are supplied; planned paths are not implemented.

Acceptance:
- Confirmed blockers yield NOT_READY; otherwise unverifiable required evidence yields UNKNOWN.
- Foreign document instructions cannot change the action catalog.
- An agent cannot directly call a payer or instantiate a privileged tool client.

Follow AGENTS.md here and the root build sequence.
