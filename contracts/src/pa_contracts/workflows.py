"""Record consistency checks; not a reviewer, statistical estimator or gate engine."""
from datetime import datetime
import math

from .serialization import digest
from .validation import ContractError, validate


def workflow(kind: str, value: object) -> dict:
    record = validate(value, "workflow-" + kind)
    if kind == "review-batch":
        if record["selected_count"] != len(record["selected_trial_ids"]):
            raise ContractError("SELECTION_COUNT_MISMATCH")
        if record["selected_count"] > record["eligible_trial_count"]:
            raise ContractError("SELECTION_EXCEEDS_POPULATION")
        if record["completed_count"] + record["unreviewable_count"] > record["selected_count"]:
            raise ContractError("REVIEW_COUNT_MISMATCH")
        if record["adjudication_pending_count"] > record["completed_count"]:
            raise ContractError("ADJUDICATION_COUNT_MISMATCH")
        if not record["reviewer_ids"] or not record["selected_trial_ids"]:
            raise ContractError("UNASSIGNED_REVIEW")
    if kind == "annotation":
        if record["reviewability"] == "UNREVIEWABLE":
            if record["verdict"] != "UNRESOLVED" or not record["unreviewable_reason"]:
                raise ContractError("UNREVIEWABLE_VERDICT")
        elif not record["evidence_refs"] or not record["observed_behavior"]:
            raise ContractError("MISSING_REVIEW_EVIDENCE")
    if kind == "failure-taxonomy":
        ids = [x["category_id"] for x in record["categories"]]
        if len(set(ids)) != len(ids) or not record["reviewer_ids"]:
            raise ContractError("INVALID_TAXONOMY")
    if kind == "calibration":
        if record["development_set_digest"] == record["audit_set_digest"]:
            raise ContractError("CALIBRATION_SPLIT_COLLISION")
        counts, matrix = record["audit_class_counts"], record["confusion_matrix"]
        if matrix["tp"] + matrix["fn"] > counts["fail_count"] or matrix["tn"] + matrix["fp"] > counts["pass_count"]:
            raise ContractError("CALIBRATION_COUNT_MISMATCH")
        if record["calibration_disposition"] == "ACCEPTED":
            if record["rubric_review_disposition"] != "ACCEPTED" or record["invalidated_by"] is not None:
                raise ContractError("INVALID_CALIBRATION_ACCEPTANCE")
            if any(counts[k] < record["minimum_class_counts"][k] for k in counts):
                raise ContractError("INSUFFICIENT_CALIBRATION_DATA")
            pos, neg = matrix["tp"] + matrix["fn"], matrix["tn"] + matrix["fp"]
            total = sum(counts.values())
            if not pos or not neg or not total:
                raise ContractError("EMPTY_CALIBRATION_CLASS")
            if matrix["fn"] / pos > record["accepted_error_bounds"]["max_fnr"] or matrix["fp"] / neg > record["accepted_error_bounds"]["max_fpr"]:
                raise ContractError("CALIBRATION_ERROR_BOUND")
            if (pos + neg) / total < record["minimum_judge_coverage"] or record["abstentions"] / total > record["maximum_abstention_rate"]:
                raise ContractError("CALIBRATION_COVERAGE_BOUND")
            if record["unresolved_reference_count"]:
                raise ContractError("UNRESOLVED_CALIBRATION_REFERENCE")
    if kind == "experiment-plan":
        if not record["changed_factors"] or not record["candidate_config_digest"] or not record["evaluation_config_digest"]:
            raise ContractError("UNCONFIGURED_EXPERIMENT")
        if record["baseline_config_digest"] == record["proposed_candidate_config_digest"]:
            raise ContractError("IDENTICAL_CANDIDATE")
        if record["budget"]["max_trials"] < 2 * record["repetitions"]:
            raise ContractError("INSUFFICIENT_TRIAL_BUDGET")
        if record["plan_digest"] != digest({k: v for k, v in record.items() if k != "plan_digest"}):
            raise ContractError("PLAN_DIGEST_MISMATCH")
    if kind == "experiment-result":
        if record["complete_pairs"] + record["missing_pairs"] != record["scheduled_pairs"]:
            raise ContractError("PAIR_COUNT_MISMATCH")
        if record["cost_complete"] and record["uncosted_calls"]:
            raise ContractError("INCOMPLETE_COST")
        if record["decision"] == "ADOPT_FOR_QUALIFICATION":
            if record["missing_pairs"] or not record["complete_pairs"] or not record["qualification_candidate_digest"]:
                raise ContractError("INCOMPLETE_COMPARISON")
            if not record["cost_complete"] or any(x["outcome"] != "PASS" for x in record["guardrail_results"]):
                raise ContractError("FAILED_COMPARISON_GUARDRAIL")
        for key in ("runtime_cost", "evaluation_cost"):
            if record[key]["complete"] and record[key]["uncosted_calls"]:
                raise ContractError("INCOMPLETE_COST")
    if kind == "monitoring-plan":
        window = record["reference_window"]
        if _time(window["start"]) >= _time(window["end"]):
            raise ContractError("INVALID_WINDOW")
        if record["evidence_class"] == "REAL_AGENT_PRODUCTION":
            raise ContractError("PRODUCTION_NOT_SCOPED")
    if kind == "monitoring-window":
        if _time(record["window_start"]) >= _time(record["window_end"]):
            raise ContractError("INVALID_WINDOW")
        eligible = record["eligible_admitted_runs"]
        if eligible in (None, 0) or record["source_freshness"] != "FRESH":
            if record["signal_status"] not in ("INSUFFICIENT_DATA", "STALE"):
                raise ContractError("MISSING_MONITORING_EVIDENCE")
        if eligible is not None and record["complete_records"] is not None and record["missing_records"] is not None:
            if record["complete_records"] + record["missing_records"] != eligible:
                raise ContractError("MONITORING_COUNT_MISMATCH")
    return record


def _time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def metric_result(value: object) -> dict:
    record = validate(value, "metric-result-v1")
    if record["status"] != "COMPUTED" and record["value"] is not None:
        raise ContractError("UNRESOLVED_METRIC_VALUE")
    if record["status"] == "COMPUTED":
        if record["value"] is None or not record["source_snapshot_digest"] or not record["evidence_refs"]:
            raise ContractError("MISSING_METRIC_EVIDENCE")
        if record["denominator"] == 0:
            raise ContractError("ZERO_DENOMINATOR")
    if record["status"] == "N/A" and not record["applicability_reason"]:
        raise ContractError("MISSING_NA_REASON")
    if record["denominator"] is not None and record["denominator"] < 0:
        raise ContractError("NEGATIVE_DENOMINATOR")
    if record["metric_id"] == "M06" and record["status"] == "COMPUTED" and record["value"] not in ("GO", "NO_GO", "INCONCLUSIVE"):
        raise ContractError("INVALID_GATE_OUTCOME")
    if record["status"] == "COMPUTED":
        metric_id = record["metric_id"]
        if metric_id in {"M01", "M02", "M04", "Q01", "Q04", "Q08", "Q06"}:
            n, d, v = record["numerator"], record["denominator"], record["value"]
            if any(type(x) not in (int, float) for x in (n, d, v)) or d <= 0 or n < 0:
                raise ContractError("INVALID_RATIO")
            if metric_id != "Q06" and (n > d or int(n) != n or int(d) != d):
                raise ContractError("INVALID_COUNT_RATIO")
            if not math.isclose(v, n / d, rel_tol=1e-12, abs_tol=1e-12):
                raise ContractError("RATIO_VALUE_MISMATCH")
            if record["unresolved_count"] is None or record["missing_count"] is None:
                raise ContractError("MISSING_METRIC_COUNTS")
        if metric_id in {"M03", "Q02", "Q03", "Q05", "Q07", "Q09"}:
            # Structured Q/M outputs have their own closed value contract.
            validate(record["value"], "metric-value-" + metric_id.lower())
        if metric_id == "M05" and (type(record["value"]) is not int or record["value"] < 0):
            raise ContractError("INVALID_COUNT_METRIC")
    return record


def evaluation_result(value: object) -> dict:
    record = validate(value, "eval-result-v1")
    outcomes = {x["outcome"] for x in record["assertions"]}
    expected = "FAIL" if "FAIL" in outcomes else "UNRESOLVED" if "UNRESOLVED" in outcomes else "PASS"
    if record["outcome"] != expected:
        raise ContractError("EVALUATION_AGGREGATE_MISMATCH")
    return record


def gate_result(value: object) -> dict:
    record = validate(value, "gate-result-v1")
    expected = "NO_GO" if record["blockers"] else "INCONCLUSIVE" if record["missing_requirements"] else "GO"
    if record["outcome"] != expected:
        raise ContractError("GATE_AGGREGATE_MISMATCH")
    return record
