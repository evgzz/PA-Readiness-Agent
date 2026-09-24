# Reproducible recipes

Each recipe binds agent, model, harness, tool catalog, policy, data, evaluator,
environment, seed/trial schedule, and cost budget. Record exact artifact hashes,
not just paths. A recipe with unresolved pins must fail preflight, not select a
default model or silently drop a required evaluator.

mock-readonly.json is a proposed wiring definition, not an executable run. Add
actual commands only when the corresponding composition app is implemented.
