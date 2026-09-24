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
