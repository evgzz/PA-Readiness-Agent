"""Static checks for this draft. Does not execute or qualify an agent.

Import lint catches ordinary Python imports only. It is not a sandbox or an
information-flow proof. JSON schemas are parsed here, not executed as validators.
"""
from __future__ import annotations

import ast
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
CHECKS = 0


def check(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        ERRORS.append(message)


def read_json(relative: str):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def rows(relative: str):
    return [json.loads(line) for line in (ROOT / relative).read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    required = [
        "README.md", "SPEC.md", "AGENTS.md", ".gitignore", ".env.example",
        ".github/workflows/scaffold.yml", "docs/ARCHITECTURE.md",
        "docs/OPEN_ASSETS.md", "docs/NVIDIA_MAPPING.md", "docs/COURSE_MIGRATION.md",
        "docs/BUILD_STATUS.json", "docs/REPO_MAP.json", "docs/codex/KICKOFF.md",
        "docs/codex/BUILD_SEQUENCE.md", "models/registry.json", "tools/catalog.json",
        "tools/standards-pins.template.json", "data/manifests/heldout.template.json",
        "contracts/src/pa_contracts/ports.py", "recipes/mock-readonly.json",
        "contracts/schemas/tool-proposal.schema.json",
        "contracts/schemas/readiness-answer.schema.json",
        "contracts/schemas/eval-result.schema.json",
        "docs/HARNESS.md", "docs/EVALUATIONS.md", "docs/INSTRUMENTATION.md",
        "docs/DASHBOARDS_REPORTS.md", "docs/REVISION_0_2.md", "docs/SOURCES.md",
        "docs/adrs/README.md", "contracts/schemas/event-envelope.schema.json",
        "contracts/metric-definitions.json", "contracts/event-catalog.json",
        "program/safety-plan.md", "program/eval-catalog.json", "program/coverage-matrix.csv",
        "program/findings.csv", "program/dependencies.csv", "governance/exceptions.csv",
        "governance/severity-and-release-policy.md", "governance/release-policy.template.json",
        "releases/candidate.template.json", "releases/authorization.template.json",
        "apps/reporting/README.md",
    ]
    for relative in required:
        check((ROOT / relative).is_file(), f"Missing {relative}")
    if ERRORS:
        return report(0, 0)

    for path in sorted(ROOT.rglob("*.json")):
        if any(part in {".git", "build", "dist", "__pycache__"} or part.endswith(".egg-info") for part in path.parts):
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
            check(True, "")
        except (ValueError, OSError) as exc:
            check(False, f"Invalid JSON: {path.relative_to(ROOT)}: {exc}")
    for path in sorted(ROOT.rglob("*.jsonl")):
        try:
            rows(str(path.relative_to(ROOT)))
            check(True, "")
        except (ValueError, OSError) as exc:
            check(False, f"Invalid JSONL: {path.relative_to(ROOT)}: {exc}")
    if ERRORS:
        return report(0, 0)

    components = read_json("docs/REPO_MAP.json")["components"]
    package_names = {component["python_package"] for component in components}
    syntax_count = 0
    for path in sorted(ROOT.rglob("*.py")):
        if any(part in {".git", ".venv", "build", "dist", "__pycache__"} for part in path.parts):
            continue
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            syntax_count += 1
            check(True, "")
        except SyntaxError as exc:
            check(False, f"Invalid Python syntax: {path.relative_to(ROOT)}: {exc}")

    for component in components:
        folder = component["path"]
        package = component["python_package"]
        for suffix in ["README.md", "AGENTS.md", f"src/{package}/__init__.py"]:
            check((ROOT / folder / suffix).is_file(), f"Missing {folder}/{suffix}")
        for path in sorted((ROOT / folder / "src").rglob("*.py")):
            try:
                tree = ast.parse(path.read_text(encoding="utf-8"))
            except SyntaxError:
                continue
            for node in ast.walk(tree):
                imports: list[str] = []
                if isinstance(node, ast.Import):
                    imports = [entry.name.split(".")[0] for entry in node.names]
                elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
                    imports = [node.module.split(".")[0]]
                for name in imports:
                    where = str(path.relative_to(ROOT))
                    check(name not in package_names or name in {package, "pa_contracts"},
                          f"Cross-component import in {where}: {name}")
                    if package == "pa_contracts":
                        check(name in sys.stdlib_module_names or name == package,
                              f"Non-stdlib contract dependency in {where}: {name}")
                    if package == "pa_agent":
                        check(name in sys.stdlib_module_names or name in {package, "pa_contracts"},
                              f"Undeclared agent dependency in {where}: {name}")
                        check(name not in {"http", "urllib", "socket", "subprocess", "ftplib", "smtplib"},
                              f"Direct network/process import in agent: {name}")

    tasks = sorted((ROOT / "docs/codex/tasks").glob("*.md"))
    check(len(tasks) == 8, "Expected eight numbered build tasks")
    for number, path in enumerate(tasks):
        check(path.name.startswith(f"{number:02d}-"), f"Unexpected task order: {path.name}")

    cases = rows("data/public/synthetic/pa_cases.jsonl")
    oracles = rows("evals/oracles/public_dev.jsonl")
    case_ids = [row["case_id"] for row in cases]
    oracle_ids = [row["case_id"] for row in oracles]
    check(len(set(case_ids)) == len(case_ids), "Duplicate public case IDs")
    check(len(set(oracle_ids)) == len(oracle_ids), "Duplicate public oracle IDs")
    check(set(case_ids) == set(oracle_ids), "Public case/oracle IDs differ")
    for row in cases:
        check(not {"expected_readiness", "expected", "oracle", "answer_key"}.intersection(row),
              f"Expected output in public input: {row['case_id']}")
    for row in oracles:
        check(row["expected_readiness"] in {"READY", "NOT_READY", "UNKNOWN"}, "Invalid public oracle label")
        check(row["status"] == "DRAFT_PUBLIC_DEV_ONLY", "Unexpected public oracle claim")

    status = read_json("docs/BUILD_STATUS.json")
    check(status["status"] == "CONTRACTS_READY", "Unexpected implementation stage")
    check(status["contracts"] == "IMPLEMENTED", "Contracts implementation missing")
    for name in ["agent", "runtime", "eval_runner"]:
        check(status[name] == "NOT_IMPLEMENTED", f"Draft incorrectly claims {name} implementation")
    recipe = read_json("recipes/mock-readonly.json")
    check(recipe["execution_mode"] == "MOCK", "Draft recipe must be a mock")
    check(recipe["external_effects_allowed"] is False, "Draft must disable external effects")
    check(recipe["entrypoint"] is None, "Draft entrypoint must be unconfigured")
    for name in ["dataset", "oracle"]:
        check((ROOT / recipe[name]).is_file(), f"Missing recipe {name}")
    for tool in read_json("tools/catalog.json")["tools"]:
        check(tool["enabled"] is False, f"Unimplemented tool enabled: {tool['name']}")
        check(tool["status"] == "NOT_IMPLEMENTED", f"Unexpected implementation claim: {tool['name']}")
    metric_registry = read_json("contracts/metric-definitions.json")
    metrics = metric_registry["metrics"]
    check({m["metric_id"] for m in metrics} == {f"M{i:02d}" for i in range(1, 7)}, "Missing core metric")
    check(len(metrics) == 6, "Duplicate core metric")
    learning_metrics = metric_registry["learning_metrics"]
    check({m["metric_id"] for m in learning_metrics} == {f"Q{i:02d}" for i in range(1, 10)}, "Missing v1 learning metric")
    check(len(learning_metrics) == 9, "Duplicate v1 learning metric")
    for relative in ["docs/V1_GAP_FIXES.md", "docs/ERROR_ANALYSIS.md", "docs/EVALUATOR_CALIBRATION.md", "docs/EXPERIMENTS.md", "docs/MONITORING.md", "docs/WORKED_EXAMPLE.md", "contracts/v1/README.md"]:
        check((ROOT / relative).is_file(), f"Missing v1 specification: {relative}")
    event_catalog = read_json("contracts/event-catalog.json")["events"]
    event_ids = {e["event_type"] for e in event_catalog}
    check(len(event_ids) == len(event_catalog), "Duplicate event type")
    for metric in metrics + learning_metrics:
        check(set(metric["events"]) <= event_ids, f"Unknown metric event: {metric['metric_id']}")
    v1_envelope = read_json("contracts/schemas/event-envelope-v1.schema.json")
    check(set(v1_envelope["properties"]["event_type"]["enum"]) == event_ids, "V1 event schema/catalog mismatch")
    snapshot = read_json("contracts/metric-snapshot.template.json")
    check({m["metric_id"] for m in snapshot["learning_metrics"]} == {m["metric_id"] for m in learning_metrics}, "Learning snapshot/registry mismatch")
    check(status["specification_revision"] == "1.0", "Expected specification v1.0")
    check(status["production_monitoring"] == "NOT_SCOPED", "V1 does not enable production monitoring")
    adr_files = sorted((ROOT / "docs/adrs").glob("[0-9][0-9][0-9]-*.md"))
    check(len(adr_files) == 23, "Expected twenty-three ADRs")
    for number, adr in enumerate(adr_files, start=1):
        check(adr.name.startswith(f"{number:03d}-"), f"ADR ordering error: {adr.name}")
        check("Status: PROPOSED" in adr.read_text(encoding="utf-8"), f"Unexpected ADR status: {adr.name}")
    for component in ["runtime_adapters", "instrumentation", "dashboards", "reports", "governance"]:
        check(status[component] == "NOT_IMPLEMENTED", f"Draft incorrectly claims {component} implementation")
    check(read_json("releases/gate-snapshot.template.json")["outcome"] is None, "Template is not a computed gate")
    check(read_json("governance/release-policy.template.json")["numeric_thresholds"] is None, "Do not invent qualification thresholds")
    return report(syntax_count, len(cases))


def report(syntax_count: int, case_count: int) -> int:
    print(json.dumps({
        "status": "FAIL" if ERRORS else "PASS",
        "scope": "STRUCTURE_AND_IMPORT_CHECKS_ONLY",
        "checks": CHECKS,
        "python_files_parsed": syntax_count,
        "public_interface_examples": case_count,
        "runtime_qualification": "NOT_RUN",
        "errors": ERRORS,
    }, indent=2))
    return 1 if ERRORS else 0


if __name__ == "__main__":
    raise SystemExit(main())
