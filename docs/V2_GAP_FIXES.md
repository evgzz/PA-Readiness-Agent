# V2 scope, course alignment and acceptance

Specification 2.0 | 2026-09-24 | DRAFT_FOR_IMPLEMENTATION.
V2 closes the identified L1–L9 specification gaps. It does not claim completed
coursework, working agents, measured improvements or production readiness.

## Authority and compatibility

SPEC.md and this v2 addendum are normative. V1 procedures remain applicable where
not explicitly amended here. This addendum prevails over conflicting v1 planning
text; metric changes require versioned implementation before use. The supplied
Hamel Husain/Shreya Shankar syllabus is the detailed alignment baseline; the
[public course page](https://maven.com/parlance-labs/evals) supplies context. PA
acceptance rules are project adaptations, not course certification or endorsement.

Task 00 implemented existing contracts, record validation and authenticated-ingress
checks. Transport authentication, durable wiring, runtime, agent, evaluations and
reporting remain pending. Specification 2.0 does not bump the Python package,
existing schema versions, M01–M06/Q01–Q09 definitions or historical evidence.
New fields/measures below are draft contracts until implemented under Task 00's
v2 extension. Null owners, statistical limits and provider pins block execution
or acceptance as applicable; they are not defaults or permission to pass.

## Operating scope and learning objective

One fictional PA case per trial; English text; bounded multi-turn retrieval,
clarification, validation, local review packet and escalation. Product outcomes
remain READY / NOT_READY / UNKNOWN. Real PHI, payer submission, clinical writes,
external messaging, autonomous delegation and production traffic remain excluded.
A local running endpoint for synthetic evaluation is in scope; a production
release is a separate decision. No commerce or analyst agent is required.

| Gulf | Workflow | PA evidence that closes it |
|---|---|---|
| Comprehension | Analyze | Read complete traces, identify the first observable failure and distinguish observation from suspected cause |
| Specification | Measure | Turn reviewed intended behavior and binary failure definitions into validated assertions, references and calibrated judges |
| Generalization | Improve, then independently test | Select changes on development evidence, freeze the candidate, and evaluate an untouched family-separated qualification set |

Application operation tiers are independent of incident severity S0–S3:
R0 scoped reads; R1 local drafts with no external effect; R2 consequential effects
requiring future bound human approval; R3 prohibited/out-of-scope operations.
Only explicitly allowlisted R0/R1 are eligible in the current synthetic profile.
R2/R3 remain disabled. Missing tier, scope or authorization yields denial. The
agent cannot declare its own tier; policy and adapters enforce it. These tiers
are project permissions, not legal AI Act classifications.

## L1–L9 requirements and corresponding specifications

| ID / lesson | Required v2 fix | Completion evidence | Corresponding specifications / task |
|---|---|---|---|
| V2-01 / L1 | Working bounded agent, explicit operation tiers and Three Gulfs loop | Pinned real-model synthetic run, typed output, code-enforced permissions and permitted positive controls | [System](../SPEC.md), [harness](HARNESS.md); Tasks 02, 03, 05 |
| V2-02 / L2 | Nested spans, model/tool calls, denials, prompt identities and reconstructable trace | A complete trace from admission to terminal outcome; missing-span case; tested Langfuse projection | [Instrumentation](INSTRUMENTATION.md), [reports](DASHBOARDS_REPORTS.md); Tasks 03, 05, 06 |
| V2-03 / L3 | Fictional authoritative world, scenario generator and reviewed smoke report | Frozen facts, generator provenance, family splits, reviewed labels, reset receipts and scenario counts | [Synthetic scenarios](SYNTHETIC_SCENARIOS.md); Task 01 |
| V2-04 / L4 | Review UI, open/axial coding and saturation record | At least 60 distinct reviewable real-agent synthetic development traces; binary codebook, overlap/adjudication and prioritized failures | [Error analysis](ERROR_ANALYSIS.md); Task 04 |
| V2-05 / L5 | One binary evaluator per observed failure mode; TPR/TNR and defensible prevalence | Independent references, class/slice counts, untouched audit, uncertainty, retrieval/grounding/handoff checks | [Calibration](EVALUATOR_CALIBRATION.md), [measurement](V2_MEASUREMENT.md), [judge options](LLM_JUDGE.md); Task 04 |
| V2-06 / L6 | Cost-tiered agent CI, pass^k/pass@k and sampled monitoring exercise | Seeded regression blocks CI, fixed-k reset/replay, complete run accounting, corrected-prevalence report with limitations | [CI](CI_EVALUATION.md), [measurement](V2_MEASUREMENT.md), [monitoring](MONITORING.md); Tasks 04, 06 |
| V2-07 / L7 | Attack-surface mapping, live synthetic red team and governance crosswalk | Pinned promptfoo adapter, actual endpoint attempts, independently checked effects, attack-to-regression lineage and governance record | [Adversarial evaluation](ADVERSARIAL_EVALUATION.md); Tasks 04–06 |
| V2-08 / L8 | Manual fix loop and comparable multi-configuration frontier | Observed top failure, declared intervention, paired comparison, retained losing/inconclusive configs and frozen selection | [Experiments](EXPERIMENTS.md), [optimization](OPTIMIZATION_UPGRADE.md); Task 07 |
| V2-09 / L9 | Token/cost attribution, prompt caching, audited cascade and upgrade drill | Measured caching change, cascade audit including bypasses, full-suite comparison of at least two committed frontier configs and decision | [Optimization](OPTIMIZATION_UPGRADE.md), [reports](DASHBOARDS_REPORTS.md); Task 07 |

All runtime evidence in this matrix is NOT_RUN. Sixty traces is an exercise floor,
not a precision guarantee. Aim for 5–8 human-derived binary modes if supported;
retain fewer/more with a documented explanation, never manufacture failures. The
course's roughly 500 support/150 analyst scenarios are not PA coverage targets;
PA counts follow the risk matrix and declared precision. No qualification labels
enter the review/tuning loop.

## Acceptance gates

| Gate | Mandatory artifact set | Disposition |
|---|---|---|
| V2-A Baseline and data | V2-01–03 manifests, trace evidence, scenario smoke report and reset checks | NOT_RUN |
| V2-B Human measurement | V2-04–05 annotations, saturation assessment, binary assertions, class errors, calibration and prevalence method | NOT_RUN |
| V2-C Regression and adversarial | V2-06–07 tier results, fixed-k report, attack regressions and synthetic monitoring/triage | NOT_RUN |
| V2-D Improvement and upgrade | V2-08–09 manual fix, caching comparison, cascade audit and two-config upgrade dossier | NOT_RUN |
| V2-Q Release qualification | Independently frozen candidate/suite, assigned gates/owners, residual-risk review and separate authorization | NOT_RUN |

V2-A–D establish completion of an evaluation demonstration. A negative or
inconclusive experiment may complete its evidence packet; it cannot establish an
improvement or justify adoption. A live red team with no successful attack must
report that honestly; a seeded vulnerable control demonstrates detection but is
not a real-agent exploit. V2-Q never becomes GO from missing mandatory evidence.
Demonstration completion is not a release recommendation or authorization.

## Build and deliver

Keep the existing eight-task work breakdown. Extend Task 00 only for new validated
records, then build Tasks 01–03 and minimal Task 04. Integrate Task 05 for actual
traces; return to Task 04 for human review and one needed calibrated judge. Add
Tasks 06–07 CI, reporting and experiments. Implement one selected model/judge
path first; Jev, HF and closed API options do not require simultaneous integration.

Required future dossier: source/config manifests; scenario smoke report; review
and saturation report; calibration report; reliability/prevalence report; CI and
red-team report; manual-fix/caching/cascade comparisons; upgrade decision; monitoring
exercise and pending/actual qualification state. JSON and Markdown render the
same frozen facts. See the disabled [learning plan](../recipes/v2-learning-plan.template.json)
and [acceptance template](v2-acceptance.template.json). Neither is an executed record.
