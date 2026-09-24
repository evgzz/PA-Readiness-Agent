# Migration from legacy implementations

Legacy archives are source/reference material, not already migrated runtime
components. Preserve originals and their evidence provenance. Do not copy their
independent run-count claims into this repository's verification report.

| Legacy capability | Target ownership | Migration task |
|---|---|---|
| Agent, instrumentation and data | agent/, harness/, contracts/, data/, tool_adapters/ | Extract contracts; adapt synthetic inputs; implement real ports |
| Error analysis | evals/, apps/review/, data/ | Move review/taxonomy/calibration logic behind versioned schemas |
| CI/CD | evals/, telemetry/, governance/, .github/ | Migrate gate logic; bind authenticated execution evidence |
| Security and governance | harness/, tool_adapters/, evals/, governance/ | Replace reference approval store with isolated durable controls; retain attacks |
| Accuracy and cost | evals/, recipes/, models/ | Port analysis and accounting; add actual model-run ingestion |

Before each port, read the source implementation and its limitations. Add parity
checks for preserved semantics, then integration tests for the new boundaries.
The legacy approval gateway is an in-memory simulation; legacy accuracy/cost
results are scripted. Neither becomes a production component merely by moving
it into a package.
