# Runtime adapters

Package: `pa_runtimes`. Status: NOT_IMPLEMENTED.

Own exactly one selected execution loop per run and SDK-specific translation. Use injected model/tool gateways; never instantiate an alternate privileged client or a second competing loop.

Planned files under `src/pa_runtimes/`: mock_loop.py, openai_agents.py.
Only this package skeleton and specification are supplied. The planned modules
do not yet exist. Read the root SPEC, architecture, and this folder's AGENTS.md.
