# Repository and Git handoff

Canonical repository: https://github.com/evgzz/PA-Readiness-Agent

This repository contains the v1 specification and source scaffold. Start with
README.md, SPEC.md and docs/V1_GAP_FIXES.md. Runtime components, real-agent
evaluations, dashboards and release gates remain NOT_IMPLEMENTED or NOT_RUN.
The repository does not deploy an application.

From the repository root:

```bash
python3 scripts/check_scaffold.py
```

Follow docs/codex/KICKOFF.md and scoped AGENTS.md instructions to implement the
eight tasks. Initial reference fixtures are synthetic and read-only. No model,
provider credential, qualification threshold or asset license has been selected.

MANIFEST.sha256 covers the tracked scaffold files except itself. Regenerate it
after source changes. It is an integrity list, not a signature or runtime result.
The GitHub Actions workflow runs static scaffold checks on pushes to main, pull
requests, merge groups and manual dispatch. Consult the actual workflow result
for each commit; historical local verification does not imply CI completion.

The earlier standalone archive remains a pre-publication snapshot. Revision
notes and artifacts retain the validation status recorded when they were produced.
