# V2 manual improvement, cost and model-upgrade drill

Status: PLANNED. Extends EXPERIMENTS.md; no improvement or cost saving is claimed.

## Manual fix before automation

Select a human-reviewed development failure with severity, frequency, confidence
and reproducible evidence. Examine the cheapest effective layer in order: prompt,
tool contract/retrieval, harness, then model/weights. Record why a layer was chosen
or skipped; a known authority defect belongs in code even if prompt changes are
cheaper. Preregister the changed factor and safety/quality constraints. Keep the
judge/rubric independent and frozen; changing it changes the measurement system.

Run one controlled manual fix, preserve original-case retest, related failures and
legitimate positives, and retain negative/inconclusive results. Select on development
comparisons; freeze a winner before independent qualification. Do not read test
results repeatedly to choose a winner and still call them held out.

A bounded automated optimizer or GEPA may be explored only after this manual loop
and an explicit later scope. Its budget, writable components and development data
must be limited; private test labels, graders, permission rules and release criteria
are not optimizer-controlled. Reward hacking tests include omissions, inappropriate
refusal and manipulation of grader-facing text. Distillation/SFT/RL remain deferred
until documented prompt/tool/harness limits and genuine capability gaps justify
separate data, compute, leakage and safety controls.

## Comparable frontier

Commit at least two complete candidate configuration files before the upgrade drill.
Each binds code, prompt, tools, harness, permissions, model/serving identity,
generation settings, source snapshots and artifact hashes. Compare points on the
same frozen workload, evaluation protocol, budgets and load/cache conditions except
for declared changed factors. A model-only comparison keeps prompt/tools/harness
fixed; a prompt/tool/harness experiment records that deliberate difference.
Never claim single-factor attribution for an optimized bundle.

Include a pinned strong baseline candidate, with selection rationale and provider
immutability limits. Do not assume a named vendor/model is universally strongest.
Report quality, safety, latency and full cost with uncertainty. Keep all measured
points and distinguish empirically non-dominated points from statistically supported
superiority. Safety constraints precede cost/quality ranking. Multiple viable
trade-off points may remain; an inconclusive comparison need not produce a winner.

## Cost attribution and prompt-caching experiment

Instrument each model attempt for input/output/cache tokens, rendered history,
retrieved context and repeated tool-schema contributions where measurable. Keep
provider-native billable units separate from component estimates; reconcile totals
and disclose tokenizer/overlap limits. Count retries, failed calls, routing and
warm-up separately. HF judge endpoints need time/replica allocation, not invented
token pricing. Runtime, evaluation and human costs remain separate.

Preregister a caching change and compare identical paired workloads under declared
cold and warm cache conditions. Measure provider-reported cached usage, hit/miss
or unknown state, actual cost, latency and quality/non-inferiority. Prompt caching
is distinct from evidence/result caching. Freeze model/prompt identity, TTL and
cache scope; ensure tenant/case/authorization/source-version changes cannot expose
or reuse invalid evidence. Do not assume caching reproduces model outputs.

Record baseline and treatment including initialization, misses, invalidations and
unknown billing. A zero/negative saving is a valid result. If the selected provider
cannot support the caching experiment, mark that milestone blocked or choose a
capable profile before preregistration; a retrieval-cache demo is not silently
substituted for the prompt-caching requirement.

## Calibrated model cascade

Define router features, cheap/strong model profiles, escalation policy, thresholds,
cost limits and allowed output behavior before audit. Train/tune only on development
labels. On a separate audit, review representative accepted cheap-path cases as well
as escalations, router bypasses and important slices. Measuring only escalations
cannot establish cheap-path safety. Include routing/model/judge error interactions,
coverage, false READY, over-refusal and all routing/fallback costs.

A router score or model confidence needs its own validation; no universal confidence
cutoff is assumed. The cascade is a new candidate, distinct from judge swapping.
If mandatory evidence is absent, abstain/escalate under the defined product policy.
A failed or inconclusive audit blocks cascade adoption; it can still complete an
honest experiment report. Do not retune on the same audit and reuse it as untouched.

## Upgrade drill and disposition

1. Freeze at least two committed candidate configs, the baseline frontier, data and
   evaluator identities. A real model revision is needed for a model-upgrade claim;
   a scripted changed response is labeled a reference rehearsal only.
2. Inspect the proposed model/serving change and compatibility. Run the full applicable
   T0–T2 development suite, including adversarial, multi-turn, legitimate, grounding,
   handoff, cost and reliability checks for each candidate. Preserve missing trials.
3. Redraw the comparable frontier and select using preregistered constraints. Report
   KEEP, PROPOSE_REPLACEMENT, PROPOSE_RETIREMENT or INCONCLUSIVE with evidence. These
   are experiment dispositions, not deployment commands or current gate enums.
4. Freeze the selected candidate before T3 independent qualification. If it fails,
   retain the outcome, return to development and obtain a fresh independent test
   for any renewed claim. No automatic endpoint replacement or deployment occurs.
5. Retain config commits, run/metric digests, deltas and uncertainty, regression
   findings, model/price changes, reviewers, proposed rollback and authorization state.

A release notification may trigger a planned drill when automation is later built;
this specification creates no scheduled job. The v2 demonstration performs one
explicit drill. Execution requires assigned owners, models, budgets and data.
