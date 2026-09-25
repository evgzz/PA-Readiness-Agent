# Reports, controlled improvements and qualification handoff

Status: PLANNED. Read root/scoped AGENTS.md, SPEC.md and relevant ADRs.

## Build
Build deterministic scorecard, executive brief and release dossier from snapshots; optionally configure Projects and native Langfuse views. Check access, freshness and all six metric denominators. Run controlled candidate/cost experiments on development data, freeze selection, then execute separate qualification when requirements are assigned. Review asset rights and reproducibility for any requested publication.

## Completion evidence
All reports reconcile to source snapshots; stale/missing values visible; no label leakage; paired comparisons distinguish model/harness changes; unsafe candidates cannot win on cost; held-out access recorded; release authorization separate. Publication/deployment require their own user-authorized action.

## Handoff
Record changed files, exact commands, actual results, evidence locations and
remaining inputs in component documentation and docs/BUILD_STATUS.json. Keep
evidence classes separate. Never invent test counts, model pins, owners or dates.

## V1 completion requirements

Execute docs/EXPERIMENTS.md after human review identifies a supported hypothesis.
Implement Q07 and learning reports with Q01–Q06. Use WORKED_EXAMPLE.md as the dossier
contract, replacing illustrative expectations only with actual observed evidence.
Implement Q08/Q09 for the monitoring simulation and retain triage history. Confirm
all report values reconcile to metric snapshots, including negative/inconclusive
results. Complete V1-A–E demonstration criteria before claiming the learning loop;
V1-F remains independent qualification and separate authorization.

## V2 completion requirements

Complete docs/OPTIMIZATION_UPGRADE.md and the v2 dashboard/report table. Start
with the reviewed top failure and manual fix, then comparable frontier, history/
retrieval/tool-schema cost attribution, prompt-cache experiment, audited cascade
and full-suite upgrade drill across two or more committed configs. Preserve
negative results, bypass failures and missing costs. V2-A–D supersede the v1
demonstration checklist with stricter evidence; V2-Q remains independent and
cannot authorize release automatically. Render JSON/Markdown from common snapshots.

## Plan 1.1 implementation slice

Render A/B/C, properties/replay, component/utility evidence and separate scoped qualification/full-program status. Complete P6A/P6E early; unused optimization experiments remain planned until full-program execution.

Corresponding specs: [comparison](../../ARCHITECTURE_COMPARISON.md),
[qualification profiles](../../QUALIFICATION_PROFILES.md),
[delivery plan](../../PHASED_DELIVERY_PLAN.md). Status remains unchanged; these are planned additions.
