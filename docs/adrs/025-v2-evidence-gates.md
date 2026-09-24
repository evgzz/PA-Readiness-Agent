# ADR 025 — V2 course-aligned evidence gates

Status: PROPOSED | 2026-09-24 | Owner roles: evaluation and engineering leads, UNASSIGNED

## Context
The v1 learning loop describes review and comparisons but does not make the
course's coding exercise, prevalence/reliability methods, agent CI tiers,
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
| Copy the commerce workload and fixed 500/150 counts | Would change the PA product and does not establish coverage or precision; adapt scenario coverage to PA instead. |
| Judge every trace without human coding | Would obscure unknown failure modes and judge error; human review precedes evaluator acceptance. |
| Show raw judge flags as population prevalence | Ignores sampling, abstention and classifier error; display separately with assumptions and uncertainty. |
| Build all backends and a full BI stack first | Delays actual traces; implement one selected path and artifact reports first. |
| Treat live red team as a safety certificate | Does not establish universal robustness; retain scope, controls and unresolved effects. |
| Automate prompt/weights search immediately | Risks reward hacking and wasted complexity; complete a manual fix and measured baseline first. |

## Consequences and acceptance
Additional review and experiment effort is explicit; owners, budgets, statistical
criteria and implementation versions remain unset until preregistration. The
60-trace exercise is a floor, not a power calculation. Five to eight modes is a
teaching target, not evidence to manufacture. Negative experiments and unsuccessful
attacks must be retained. No automatic deployment, provider fallback or PHI use
is introduced. Accept only after v2 schema checks and V2-A–D artifacts execute;
release still needs V2-Q and separate authenticated authorization.
