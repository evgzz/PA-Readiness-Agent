# Model adapters

Package: pa_models. Implementation status: DRAFT_INTERFACES_ONLY.

Own inference protocol translation, model identity, structured-response normalization, usage metering, and provider error mapping.

Do not hard-code provider APIs inside the agent, execute PA tools, or silently substitute models/mocks.

Planned implementation files under src/pa_models: mock.py, openai_compatible.py, local_serving.py, usage.py.
Only files physically present are supplied; planned paths are not implemented.

Acceptance:
- Unconfigured endpoints return NOT_CONFIGURED, with no network call.
- Provider timeouts/malformed tool outputs become typed errors.
- Exact model/server/tokenizer/template settings and native billing semantics are recorded.

Follow AGENTS.md here and the root build sequence.

## Swappable evaluation adapter plan
Planned jev.py translates TypeSafe typed questions and responses behind JudgePort;
apps/ injects it into the evaluation plane, separate from runtime model calls.
Planned hf_endpoint.py, hf_providers.py and closed_api.py support other profiles.
See docs/LLM_JUDGE.md and the Jev appendix docs/JEV_JUDGE.md. No profile is selected;
disabled templates have no completed SDK pins or budgets.
The adapter, usage integration, credential preflight and live calls are pending.
