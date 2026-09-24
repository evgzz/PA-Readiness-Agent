# V2 fictional PA world and scenario generation

Status: PLANNED. The three existing public cases are interface examples only.
Owner roles: evaluation and PA-domain reviewer; unassigned.

The controller owns a versioned facts.yaml (or equivalent typed JSON) describing
fictional tenants, patients, requests, requirements, evidence IDs/versions, source
timestamps, allowed operations and simulated dependency behavior. These are
invented administrative cases, not medical policy or clinical reference standards.
Only authorized observations reach the agent; complete facts and expected outcomes
remain evaluator-controlled. Public world facts cannot qualify as hidden oracles.

| Coverage axis | Required development scenarios |
|---|---|
| Readiness | Fully supported, confirmed blocker, unavailable required evidence, blocker plus unresolved item |
| Evidence identity | Correct patient/request, foreign references, stale/superseded evidence and contradictory sources |
| Multi-turn | Clarification, correction, late evidence, retry, budget exhaustion and reset/session isolation |
| Tools | Successful reads, denied calls, missing/malformed response, timeout and unavailable service |
| Adversarial | Untrusted instructions, forged authority, prohibited write/delegation and positive read controls |
| Subsystems | Known relevant-evidence set, claim-to-evidence grounding, local escalation/handoff packet |

Create a versioned generation instruction/skill specification before generation;
record code/model/prompt/settings, seed when supported, source families and content
digests. The generation pipeline and any installable skill are not supplied here.
Deterministic world reset is required even if language generation is stochastic.
Every generated case receives automated consistency checks and a declared human
review policy; label provenance and unresolved references remain visible.

Split by source family before creating paraphrases and attack variants. Group
shared facts/templates that can leak answers; run exact/near-duplicate checks and
record residual leakage risks. Partition rubric development, candidate development,
untouched calibration audit and candidate qualification separately. Public examples
are development data. Repeated trials do not increase the count of unique cases.

Smoke report fields: world/generator/config digests; generated/accepted/rejected/
ambiguous counts; unique families and per-slice counts; input/label schema checks;
reset and scope controls; expected READY/NOT_READY/UNKNOWN distribution; label
review status; deduplication and split audit. A smoke run validates interfaces;
a real-agent baseline is a separately labeled evidence class.

Counts are fixed in the plan before acceptance. Sixty reviewable traces for V2-04
requires enough distinct scheduled trials, but does not establish scenario breadth
or statistical power. Do not expand to an analyst agent solely to match course
numbers. Missing required slices or unknown label validity prevent coverage claims.

Planned capture: pa_tools.synthetic owns world/reset receipts; pa_evals.splits owns
family assignment; pa_evals.runner owns schedule and terminal completeness. Task 01
produces the assets and smoke report; Task 04 independently verifies them.
