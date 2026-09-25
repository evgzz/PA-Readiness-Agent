# Specification 2.1 and delivery plan 1.1

Date: 2026-09-25 | Status: SPECIFIED_NOT_IMPLEMENTED

| Change | Corresponding spec | Acceptance evidence still required |
|---|---|---|
| Rules-only baseline separate from mock; A/B/C comparison using one initial model | [Architecture comparison](ARCHITECTURE_COMPARISON.md) | P1 predicate execution; P3 controlled pilot; P5 selection with accepted evaluators |
| Property tests, tool-response replay and component diagnosis | [Architecture comparison](ARCHITECTURE_COMPARISON.md), [CI](CI_EVALUATION.md) | P2 controls and no-fallback replay; P5 diagnosis and end-to-end fix |
| Human-only versus assisted review | [Architecture comparison](ARCHITECTURE_COMPARISON.md) | P5 matched study before utility/productivity claims, or explicit deferral with no such claims |
| Candidate-scoped versus full-program qualification | [Qualification profiles](QUALIFICATION_PROFILES.md), [ADR 026](adrs/026-candidate-comparison-and-qualification-profiles.md) | P5/P6A/P6E plus all applicable feature evidence; full program still needs all P6 experiments |
| Trace/report mappings and explicit dependency/status records | [Phase plan](PHASED_DELIVERY_PLAN.md), [dashboards](DASHBOARDS_REPORTS.md) | Implemented validated records and reconciled source-linked reports |

This explicitly amends the unconditional P6-to-P7 dependency in plan 1.0; it does
not relax mandatory candidate safety/quality controls or close any full-program
gate. Existing V2-01–09 requirements remain required for full-program completion.
All active status records preserve P0 complete for original contracts, P1 next and
P1–P7 planned. New criteria are NOT_ASSESSED. Runtime and profile contracts remain
unimplemented; disabled templates stay disabled. Package versions, event schemas,
M01–M06/Q01–Q09 definitions and historical execution evidence are unchanged.

[Validation evidence](../artifacts/PLAN_REVISION_VALIDATION.json) covers documentation,
status consistency and scaffold checks only. It is not execution evidence for any
new phase, architecture, experiment or qualification profile.
