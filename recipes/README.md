# Reproducible recipes

Each recipe binds agent, model, harness, tool catalog, policy, data, evaluator,
environment, seed/trial schedule, and cost budget. Record exact artifact hashes,
not just paths. A recipe with unresolved pins must fail preflight, not select a
default model or silently drop a required evaluator.

mock-readonly.json is a proposed wiring definition, not an executable run. Add
actual commands only when the corresponding composition app is implemented.

jev-judge.template.json specifies one optional disabled evaluation-plane candidate. It is
not accepted by the runtime-config CLI and is not an executable provider recipe.
See docs/JEV_JUDGE.md for preflight, typed rubrics and required future contracts.
Null pins/budgets/thresholds are intentional missing configuration, not defaults.

judge-selection.template.json is the provider-neutral selection plan. Its
selected_profile_id is null. Options reference hf-endpoint-judge.template.json,
closed-api-judge.template.json, hf-providers-judge.template.json and the Jev template.
These are design templates, not executable profiles or runtime-config CLI inputs.
See docs/LLM_JUDGE.md for exact preflight, calibration and swapping requirements.
Changing a template does not deploy, resume or call an endpoint.
