# Dashboard and report application

Status: NOT_IMPLEMENTED. The first implementation target is deterministic Markdown/
JSON scorecards. See [report specification](../../docs/DASHBOARDS_REPORTS.md).
Planned modules: loaders.py (versioned sources), projections.py (joins and freshness),
render_scorecard.py, render_executive.py, and later an optional UI.
Metric formulas stay in the shared registry and their eval/governance owners.
Release-gate computation stays in pa_governance, never in dashboard presentation.
