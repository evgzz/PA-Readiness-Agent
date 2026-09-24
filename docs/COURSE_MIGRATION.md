# Migration from the five module packages

The prior module archives are source/reference material, not already migrated
runtime components. Preserve originals and their evidence provenance. Do not copy
their independent run-count claims into this scaffold's verification report.

| Prior module | Target ownership | Migration task |
|---|---|---|
| 1 — Build/instrument/data | agent/, harness/, contracts/, data/, tool_adapters/ | Extract contracts; adapt synthetic inputs; implement real ports |
| 2 — Error analysis | evals/, apps/review/, data/ | Move review/taxonomy/calibration logic behind versioned schemas |
| 3 — CI/CD | evals/, telemetry/, governance/, .github/ | Migrate gate logic; bind authenticated execution evidence |
| 4 — Security/governance | harness/, tool_adapters/, evals/, governance/ | Replace reference approval store with isolated durable controls; retain attacks |
| 5 — Accuracy/cost | evals/, recipes/, models/ | Port analysis and accounting; add actual model-run ingestion |

Before each port, read the module's current source and limitations. Add parity
checks for preserved semantics, then integration tests for the new boundaries.
The Module 4 gateway is an in-memory simulation; Module 5 results are scripted.
Neither is a production component merely because it is moved into a package.
