# ADR 025 — V2 evaluation evidence gates

Status: PROPOSED | 2026-09-24 | Owner roles: evaluation and engineering leads, UNASSIGNED

## Context
The v1 learning loop describes review and comparisons but does not make the
human review procedure, prevalence/reliability methods, agent CI tiers,
adversarial regressions and cost/upgrade exercises concrete enough to implement.
An existing contracts package does not prove those workflows have executed.

## Proposed decision
Adopt [V2 requirements](../V2_GAP_FIXES.md) as a normative spec addendum. Retain the
bounded synthetic/read-only PA product and existing trust boundaries. Extend the
eight tasks and require V2-A–D evidence; retain separate V2-Q qualification.
Add explicit capture/report mappings and versioned schemas before new records
execute. Use human-derived binary failures, independent judge calibration,
sampling-aware uncertainty and fixed-k missingness accounting. Preserve a manual
fix loop and measured caching, cascade and two-configuration upgrade drill.

## Alternatives and tradeoffs
| Option | Assessment |
|---|---|
| Reuse fixed scenario counts from an unrelated workload | Does not establish PA coverage or precision; size the dataset from the PA risk matrix and uncertainty requirements. |
| Judge every trace without human coding | Would obscure unknown failure modes and judge error; human review precedes evaluator acceptance. |
| Show raw judge flags as population prevalence | Ignores sampling, abstention and classifier error; display separately with assumptions and uncertainty. |
| Build all backends and a full BI stack first | Delays actual traces; implement one selected path and artifact reports first. |
| Treat live red team as a safety certificate | Does not establish universal robustness; retain scope, controls and unresolved effects. |
| Automate prompt/weights search immediately | Risks reward hacking and wasted complexity; complete a manual fix and measured baseline first. |

## Consequences and acceptance
Additional review and experiment effort is explicit; owners, budgets, statistical
criteria and implementation versions remain unset until preregistration. The
60-trace review minimum is a floor, not a power calculation. Five to eight modes
is a proposed working range; the actual taxonomy follows observed failures.
Negative experiments and unsuccessful attacks must be retained. No automatic
deployment, provider fallback or PHI use
is introduced. Accept only after v2 schema checks and V2-A–D artifacts execute;
release still needs V2-Q and separate authenticated authorization.

## Specification 2.1 dependency amendment

[ADR 026](026-candidate-comparison-and-qualification-profiles.md) makes the dependency
explicit: this ADR's full V2-A–D evidence requirement remains unchanged for program
completion. Scoped candidate qualification may follow P5/P6A/P6E plus all used-feature
requirements under a frozen profile; it cannot claim full-program completion.
