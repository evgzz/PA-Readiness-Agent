# Source register

Design synthesis date: 2026-09-24. Architectural prescriptions in this package are
project proposals. Product documentation supports the narrow capability statements
below; it does not validate this PA implementation or confer compliance.

| Source | Claim or use |
|---|---|
| [OpenAI Agents SDK](https://developers.openai.com/api/docs/guides/agents/sdk) | SDK loop runs in the application; application retains tools, state, and approval decisions |
| [OpenAI integrations and observability](https://developers.openai.com/api/docs/guides/agents/integrations-observability) | Built-in tracing requires explicit review of content and export settings |
| [Langfuse self-hosting](https://langfuse.com/self-hosting) | Platform deployment dependencies; verify against the selected version |
| [Langfuse custom dashboards](https://langfuse.com/docs/metrics/features/custom-dashboards) | Native trace/score analytics widgets |
| [Langfuse Metrics API](https://langfuse.com/docs/metrics/features/metrics-api) | Supported analytical export; endpoint/version compatibility must be checked |
| [OpenTelemetry instrumentation](https://opentelemetry.io/docs/concepts/instrumentation/) | Code-based and automatic instrumentation can be combined |
| [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects) | Custom fields, charts, issue/PR integration and automation |
| [GitHub Actions summaries](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands#adding-a-job-summary) | Markdown job scorecards |
| [Metabase documentation](https://www.metabase.com/docs/latest/) | SQL and BI dashboard option |
| [Grafana ClickHouse data source](https://grafana.com/docs/plugins/grafana-clickhouse-datasource/latest/) | Analytical dashboards and alerting option |
| [Transactional outbox](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html) | State/event dual-write pattern and idempotent consumption |

These official pages were retrieved during this revision or its immediately
preceding dashboard design discussion. No versions or prices are inferred from
the documentation URLs. Braintrust, Arize Phoenix, LangGraph and benchmark suites
are recorded selection candidates; exact capabilities, versions, terms and
compatibility require a separate integration review.

The supplied NVIDIA JD (JR2024325) supplies the program responsibility mapping.
The original PA scaffold supplies the retained three example cases, draft ports,
and initial source layout. The prior five-module discussions supply design intent,
not imported execution evidence. See `COURSE_MIGRATION.md`.

## V1 course alignment source
[Parlance Labs: AI Evals for Engineers & PMs](https://maven.com/parlance-labs/evals),
public page and expanded syllabus inspected 2026-09-24. Used for the L1–L9 topic
mapping and advertised monitoring outcome in docs/V1_GAP_FIXES.md. The PA procedures,
metric definitions and acceptance gates are independent project design choices;
no private course content, course completion or endorsement is claimed.

## Jev judge sources
Inspected 2026-09-24. Capability facts are separated from the PA-specific design
in docs/JEV_JUDGE.md; no vendor experiment is imported as repository evidence.

| Source | Use |
|---|---|
| [LangChain: Jev-as-a-Judge](https://www.langchain.com/blog/jev-agent-evals-langsmith) | Supplied article; fixed-run comparison with a small unique-case corpus |
| [Reproduction repository](https://github.com/danielgshea/jev-as-a-judge) | Experiment structure and provenance; no code or results imported |
| [TypeSafe state](https://docs.typesafe.ai/concepts/state) | Structured text context for independent questions |
| [Primitives](https://docs.typesafe.ai/primitives) and [confidence](https://docs.typesafe.ai/confidence) | Typed decisions and uncertainty semantics |
| [API](https://docs.typesafe.ai/api) and [Python SDK](https://docs.typesafe.ai/sdk/python) | Proposed transport boundary and response fields |
| [Models](https://docs.typesafe.ai/models) | Versioned candidate, moving aliases, input limits; reverify before integration |
| [Jev 1.13 limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13) | Targeted failure slices and keeping exact computations in code |

## Swappable judges and HF integration sources
Inspected 2026-09-24. The primary design is now docs/LLM_JUDGE.md; Jev is an option.
No commercial endpoint was deployed and no provider capability was live-tested.

| Source | Narrow capability / design use |
|---|---|
| [HF dedicated chat tutorial](https://huggingface.co/docs/inference-endpoints/tutorials/chat_bot) | Compatible chat endpoint, base URL, served-model identifier and token |
| [HF endpoint configuration](https://huggingface.co/docs/inference-endpoints/guides/configuration) | Hub commit revision and deployment/access settings |
| [HF custom container](https://huggingface.co/docs/inference-endpoints/guides/custom_container) | Supplied serving images and model artifacts; no general closed-model hosting claim |
| [HF Providers chat API](https://huggingface.co/docs/inference-providers/tasks/chat-completion) | Separate routed inference service; verify current model/provider support |
| [HF structured outputs](https://huggingface.co/docs/inference-providers/guides/structured-output) | Schema support is checked for the selected model/provider combination |
| [HF dedicated billing](https://huggingface.co/docs/inference-endpoints/pricing) | Compute-time billing informs allocation, not per-token-only costing |

Routing API-only closed models to their supported service, profile freeze, swap
calibration and no silent fallback are PA design requirements, not claims that HF
hosts every proprietary model. Exact model/SDK/engine selections remain unset.

## V2 alignment and governance sources

The detailed L1–L9 syllabus supplied by the user is the alignment baseline,
including the 60-trace coding exercise and caching/cascade/upgrade homework.
PA-specific counts, adaptation, formulas and acceptance rules are project design
decisions; they are not attributed as quotations from unavailable course material.
The public course page supports the advertised evaluation lifecycle. Official
resources below were retrieved 2026-09-24; pin tool versions before integration.

| Source | Narrow use |
|---|---|
| [OWASP agentic Top 10, 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | ASI01–10 attack-surface crosswalk; project tests do not imply certification |
| [NIST AI RMF core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | Govern, Map, Measure and Manage record organization |
| [Promptfoo HTTP provider](https://www.promptfoo.dev/docs/providers/http/) | Proposed endpoint request/response adapter |
| [Promptfoo red-team configuration](https://www.promptfoo.dev/docs/red-team/configuration/) | Separate generation, target and attack execution configuration |
| [European Commission AI Act overview](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) | Basis for a future use/role/jurisdiction-specific applicability review; no PA legal classification or compliance claim |
