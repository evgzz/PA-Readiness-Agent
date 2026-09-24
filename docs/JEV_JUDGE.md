# Jev judge option

Status: SPECIFIED_NOT_IMPLEMENTED | Revision: 1.1 | 2026-09-24.
Jev is optional and is not the default or mandatory judge. Provider configuration
and calibration remain NOT_CONFIGURED / NOT_RUN. The common
[swappable judge specification](LLM_JUDGE.md) owns interfaces, J01–J07, trajectories,
selection, reporting and acceptance. This file supplies Jev-specific translation.

## Verified capabilities

TypeSafe Jev is one optional provider behind the common JudgePort in the
evaluation plane; it is a typed decision model, not a text-generating LLM. The
[LangChain article](https://www.langchain.com/blog/jev-agent-evals-langsmith)
compares judges on five fixed weather-agent runs repeated 100 times. Those are
five unique cases, not 500 independent scenarios. That experiment motivates a PA
comparison; it establishes no PA accuracy, calibration, latency or cost target.

[TypeSafe primitives](https://docs.typesafe.ai/primitives) offer Choice, Score and
Noul. Choice selects an option; Score returns a probability-weighted value across
ordered levels, potentially between levels; Noul returns the probability of yes.
Choice/Score include distributions and a distribution-derived confidence value.
[Noul has no separate confidence field](https://docs.typesafe.ai/confidence).
A confidence value is not an independently validated probability of PA correctness.

## Adapter and rubric mapping

Proposed adapter: model_adapters/src/pa_models/jev.py. apps/ injects it through the
same JudgePort as HF-hosted and closed API judges. Use TypeSafe's direct SDK by
default within this option; langchain-typesafe is an optional separately pinned
transport. No HF deployment or OpenAI-compatible Jev endpoint is assumed.

| Common criterion | Jev rendering | Normalization |
|---|---|---|
| J01 | Choice over SUPPORTED / CONTRADICTED / INSUFFICIENT | Favorable / adverse / unresolved |
| J02 | Noul: yes means the answer incorrectly establishes an unresolved check | Failure probability, with two audited cutoffs |
| J03 | Choice over RELEVANT / IRRELEVANT / INSUFFICIENT | Favorable / adverse / unresolved |
| J04 | Choice over INCORPORATED / IGNORED / INSUFFICIENT | Favorable / adverse / unresolved |
| J05 | Choice over ADEQUATE / INADEQUATE / INSUFFICIENT | Favorable / adverse / unresolved |
| J06 | Score: unusable, ambiguous, actionable | Weighted diagnostic score; retain legend and probabilities |
| J07 | Choice over CONSISTENT / CONTRADICTORY / INSUFFICIENT | Favorable / adverse / unresolved |

The controller supplies the complete atomic question and required evidence, not
just a criterion ID. Jev's [known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13)
include numeric precision, indirection and irrelevant long context. Exact checks
stay in code. Missing context cannot be overcome with a confident output.

For Choice, favorable/adverse values map to PASS/FAIL only when option probability
and provider confidence meet their separate frozen floors. INSUFFICIENT, ties or
unmet floors yield UNRESOLVED. For Noul, given 0 <= low < high <= 1, p <= low is
PASS, p >= high is FAIL and the middle is UNRESOLVED. Limits are per criterion and
initially null. J06 remains diagnostic. All accepted assertions require complete
evidence, valid output and calibration of this exact effective profile.

Reject wrong/missing/extra IDs, wrong types/options, invalid distributions,
non-finite/range violations, changed legends and model mismatch. Freeze numerical
tolerances and tie handling in the future adapter contract. Never invent a Noul
confidence field, generated rationale or citation. The controller links verified
input references; reason codes document the mapping and human notes are separate.
A deterministic failure always takes precedence over a favorable Jev result.

## Provider preflight

The proposed transport is the [TypeSafe Python SDK](https://docs.typesafe.ai/sdk/python)
(`typesafe-sdk`, `TypeSafeClient.system_one`) using an evaluation-only credential
referenced by `TYPESAFE_API_KEY`. The documented endpoint is
`https://api.typesafe.ai/v1/systemone`; secrets never enter configuration or traces.

[Model documentation](https://docs.typesafe.ai/models) currently lists
`jev-1.13.0`. Use that explicit candidate pin and verify the returned model;
`jev-latest` and `jev-preview` are moving aliases. Hosted service immutability
beyond the reported model ID is not established. Record this limitation and use
fixed sentinel cases to detect behavior changes requiring a fresh audit.
The documented input limits are 64k total request tokens and 32k for state plus
the longest question; verify against the selected service before enabling calls.

The disabled [configuration template](../recipes/jev-judge.template.json) requires
an exact SDK pin, compatible installation, an approved synthetic-data egress
profile, credential availability, request/attempt/time/token/cost budgets and
context limits before any call. No real PHI or qualification corpus is exported
by this template. Qualification access requires its own controlled profile.
Do not inherit unbounded SDK retries; coordinate retries at one layer, retain
attempts and stop at the declared limit. An unconfigured integration makes zero
network calls and reports NOT_CONFIGURED. Unknown billing remains unknown.

## Calibration and swapping

Use the common human audit and probability-calibration rules. Jev acceptance
cannot transfer to a generative model, and another judge's thresholds cannot
transfer to Jev. Switching to HF or a closed API selects another profile for a new
run/regrade, preserving the same rubric and evidence population. Default fallback
is NONE. The linked five-case weather experiment does not qualify PA behavior.
