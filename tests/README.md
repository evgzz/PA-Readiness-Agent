# Planned test suites

- unit/: proposal parsing, typed evidence, deterministic readiness, accounting.
- boundaries/: imports plus actual identity/network/file isolation, denied tools.
- integration/: model/tool adapters, trace linking, reset/replay, timeout/resume.
- adversarial/: injected documents, scope abuse, approval replay, ambiguous effects.
- reproducibility/: manifest integrity, grouped splits, complete trial coverage.

These suites are not implemented here. scripts/check_scaffold.py checks only the
draft's structure and static source properties. Required runtime/safety gates
must not depend solely on this structural check.
