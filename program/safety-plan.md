# PA safety program plan — proposed

Scope: one candidate configuration in a synthetic, read-only PA preparation flow.
Program state: PLANNED. Model, named owners, committed dates and resources: unassigned.

| Workstream | Accountable role (unassigned) | Deliverable / dependency |
|---|---|---|
| Agent and runtime | Engineering owner | Typed agent, one loop, bounded execution |
| Authorization and effects | Security/control owner | Gateway enforcement, receipts, reconciliation |
| Cases and grading | Evaluation owner | Frozen datasets, calibrated graders, required slices |
| Model integration | Model/inference owner | Selected checkpoint, serving configuration, resource budget |
| Findings and closure | Finding-specific owner | Mitigation, retest, regression and positive controls |
| Release governance | Release authority | Versioned gate policy, exceptions, authorization |
| Reporting | Program reporting owner | Source-linked scorecard and executive brief |

Record assignments and dates before program execution. Use `dependencies.csv` for
critical-path blockers, decision deadlines, impact and recovery plans. Use
`findings.csv` for real findings only; the delivered file has headers and no invented
failures or owners. `coverage-matrix.csv` defines planned first-scope slices, not
measured coverage. `eval-catalog.json` records proposed selection rationale.

Initial milestone evidence follows SPEC M0–M5. Model access, compute capacity,
serving/API configuration, benchmark rights, isolated qualification storage,
reviewer availability, and actual FHIR/requirements endpoints are unresolved
dependencies. Estimate GPU hours, API spend, engineering and review capacity only
after selecting workload and model; no budget or date is committed by this draft.

First target demonstration: execute a bounded real-agent synthetic suite; observe
and triage a failure; mitigate; retest the unchanged case plus regression/positive
controls; publish a source-linked recommendation with remaining risks. If no
failure is observed, report that result and the sampling limits; do not manufacture
a failure to complete the narrative.

Suggested review cadence to agree before execution: run-level triage on finalized
evaluations, regular owner/dependency review, and a formal candidate review before
authorization. Critical findings require prompt containment and escalation under
the assigned response policy. Automation may prepare reports; sending or deploying
remains a separately authorized operation.
