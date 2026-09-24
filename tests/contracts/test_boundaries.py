import copy
from pathlib import Path
import unittest

from pa_contracts.configuration import runtime_config, scope_claims
from pa_contracts.evidence_ports import IngressIdentity
from pa_contracts.runtime_ports import runtime_input, tool_proposal, answer_proposal
from pa_contracts.serialization import canonical_bytes, digest, bytes_digest
from pa_contracts.validation import ContractError, load_json, resource, validate
from pa_contracts.workflows import workflow, metric_result, evaluation_result, gate_result
from pa_telemetry.ingress import validate_ingress, validate_legacy_envelope

ROOT = Path(__file__).resolve().parents[2]
H = "a" * 64
T = "2026-09-24T00:00:00Z"


def sample(rule):
    if "const" in rule: return rule["const"]
    if "enum" in rule: return rule["enum"][0]
    if "anyOf" in rule: return sample(rule["anyOf"][0])
    kind = rule.get("type", "object")
    if isinstance(kind, list): kind = kind[0]
    if kind == "string":
        return H if "pattern" in rule else T if rule.get("format") == "date-time" else "fixture"
    if kind == "integer": return max(0, rule.get("minimum", 0))
    if kind == "number": return .95 if "exclusiveMaximum" in rule else max(0.0, rule.get("minimum", 0), rule.get("exclusiveMinimum", -1) + 1)
    if kind == "boolean": return False
    if kind == "null": return None
    if kind == "array": return [sample(rule["items"]) for _ in range(rule.get("minItems", 0))]
    return {k: sample(v) for k, v in rule.get("properties", {}).items()}


def valid_workflow(kind):
    v = sample(resource("workflow-" + kind))
    for k in ("candidate_config_digest", "evaluation_config_digest"):
        v[k] = H
    v["evidence_class"] = "REFERENCE_CONTROL"
    if kind == "review-batch":
        v.update(eligible_trial_count=1, selected_count=1, completed_count=0, selected_trial_ids=["trial"], reviewer_ids=["reviewer"])
    elif kind == "annotation":
        v.update(evidence_refs=["evidence"], unreviewable_reason=None)
    elif kind == "failure-taxonomy":
        v["reviewer_ids"] = ["reviewer"]
    elif kind == "calibration":
        v.update(development_set_digest="b"*64, audit_set_digest=H,
                 audit_class_counts={"pass_count":1,"fail_count":1},
                 confusion_matrix={"tp":1,"tn":1,"fp":0,"fn":0}, invalidated_by=None,
                 minimum_judge_coverage=1.0, maximum_abstention_rate=0.0)
    elif kind == "experiment-plan":
        v.update(changed_factors=["prompt"], baseline_config_digest="b"*64)
        v["budget"]["max_trials"] = 2
        v["plan_digest"] = digest({k: value for k, value in v.items() if k != "plan_digest"})
    elif kind == "experiment-result":
        v.update(scheduled_pairs=1,complete_pairs=1,missing_pairs=0,cost_complete=True,qualification_candidate_digest=H)
    elif kind == "monitoring-plan":
        v["reference_window"]["end"] = "2026-09-25T00:00:00Z"
    elif kind == "monitoring-window":
        v.update(window_end="2026-09-25T00:00:00Z",eligible_admitted_runs=1,complete_records=1,missing_records=0)
    return v


class Verifier:
    def __init__(self, producer="pa_harness", channel="OPERATIONAL"):
        self.identity = IngressIdentity("fixture-service", producer, "worker", frozenset([channel]), frozenset(["REFERENCE_CONTROL"]), frozenset(["fixture"]))
    def authenticate(self, credential):
        if credential != "fixture-credential": raise ValueError("Do not leak credential")
        return self.identity


def event(event_type="run.started"):
    spec = next(x for x in resource("event-catalog")["events"] if x["event_type"] == event_type)
    payload = sample(resource(spec["payload_schema"]))
    if event_type == "run.started":
        payload["scope"]["allowed_operations"] = ["case.read"]
    env = load_json((ROOT/"contracts/examples/event-envelope.example.json").read_bytes())
    env.update(schema_version="1.0", event_type=event_type, producer=spec["producer"], producer_instance="worker", channel=spec["channel"], evidence_class="REFERENCE_CONTROL", candidate_config_digest=H, evaluation_config_digest=H,run_id="run",case_id="case",trial_id="trial",action_id="action",attempt_id="attempt",finding_id="finding")
    for key in ("candidate_config_digest", "evaluation_config_digest", "run_id", "case_id", "trial_id", "action_id", "attempt_id", "finding_id", "evidence_class"):
        if key in payload: payload[key] = env[key]
    raw = canonical_bytes(payload)
    env["payload_sha256"] = bytes_digest(raw)
    return env, payload, Verifier(spec["producer"], spec["channel"])


def ingest(env, payload, verifier, credential="fixture-credential"):
    raw=canonical_bytes(payload)
    env=copy.deepcopy(env);env["payload_sha256"]=bytes_digest(raw)
    return validate_ingress(canonical_bytes(env), raw, credential, verifier)


class ParsingAndRuntimeTests(unittest.TestCase):
    def test_ambiguous_json_is_rejected(self):
        for raw in [b'{"x":1,"x":2}', b'{"x":NaN}', b'{"x":1e999}', b'"\\ud800"', b'['*100+b']'*100]:
            with self.subTest(raw=raw[:20]), self.assertRaises(ContractError):load_json(raw)
    def test_canonical_manifest_has_fixed_bytes_and_stable_hash(self):
        self.assertEqual(canonical_bytes({"z":2,"a":[True,None]}),b'{"a":[true,null],"z":2}')
        self.assertEqual(digest({"z":2,"a":[True,None]}),digest({"a":[True,None],"z":2}))
        self.assertNotEqual(digest({"x":1}),digest({"x":2}))
    def test_scope_cannot_enable_writes_or_blank_identity(self):
        s=sample(resource("scope"));s["allowed_operations"]=["case.read"]
        self.assertEqual(scope_claims(s),s)
        for key,value in [("allowed_operations",["submit"]),("patient_id"," ")]:
            bad=copy.deepcopy(s);bad[key]=value
            with self.assertRaises(ContractError):scope_claims(bad)
    def test_runtime_projection_rejects_labels_and_foreign_evidence(self):
        v=sample(resource("runtime-input"));self.assertEqual(runtime_input(v),v)
        for field in ["oracle","expected_readiness","grader","scope","approval"]:
            with self.subTest(field=field),self.assertRaises(ContractError):runtime_input({**v,field:"injected"})
        ev={"evidence_id":"e","case_id":"foreign","source_version":"v","availability":"FOUND","text":"synthetic"}
        with self.assertRaises(ContractError):runtime_input({**v,"evidence":[ev]})
        ev["case_id"]=v["case_id"];ev["expected_readiness"]="READY"
        with self.assertRaises(ContractError):runtime_input({**v,"evidence":[ev]})
    def test_tool_proposal_does_not_accept_authority_fields(self):
        rules={"read":{"type":"object","additionalProperties":False,"required":["evidence_id"],"properties":{"evidence_id":{"type":"string","minLength":1}}}}
        proposal={"schema_version":"1.0","tool_name":"read","arguments":{"evidence_id":"e"}}
        self.assertEqual(tool_proposal(proposal,rules).tool_name,"read")
        for bad in [{**proposal,"authorized":True},{**proposal,"tool_name":"submit"},{**proposal,"arguments":{"evidence_id":"e","tenant_id":"forged"}}]:
            with self.assertRaises(ContractError):tool_proposal(bad,rules)
    def test_configuration_rejects_second_loop_and_unbounded_budget(self):
        v=load_json((ROOT/"recipes/runtime-config.example.json").read_bytes());runtime_config(v)
        for key,val in [("runtime_adapter","openai_agents"),("external_effects_allowed",True),("extra_loop","mock_loop")]:
            with self.assertRaises(ContractError):runtime_config({**v,key:val})
        v["budgets"]["max_steps"]=True
        with self.assertRaises(ContractError):runtime_config(v)
    def test_answer_semantics_preserve_unknown_and_blockers(self):
        v={"schema_version":"1.0","readiness":"UNKNOWN","evidence_refs":[],"blockers":[],"unresolved_checks":["evidence unavailable"],"explanation":"review"}
        answer_proposal(v)
        with self.assertRaises(ContractError):answer_proposal({**v,"readiness":"READY"})
        v["blockers"]=["confirmed missing item"];v["readiness"]="NOT_READY";answer_proposal(v)
    def test_unknown_version_and_enums_fail(self):
        v=sample(resource("runtime-input"))
        with self.assertRaises(ContractError):runtime_input({**v,"schema_version":"2.0"})
        with self.assertRaises(ContractError):answer_proposal({**sample(resource("readiness-answer-v1")),"readiness":"APPROVED"})


class IngressTests(unittest.TestCase):
    def test_authenticated_event_preserves_original_bytes(self):
        env,p,v=event();result=ingest(env,p,v)
        self.assertEqual(result.payload_bytes,canonical_bytes(p));self.assertEqual(result.principal_id,"fixture-service")
    def test_authentication_failure_has_no_secret_in_error(self):
        env,p,v=event()
        with self.assertRaises(ContractError) as ctx:ingest(env,p,v,"wrong-private-token")
        self.assertEqual(str(ctx.exception),"AUTHENTICATION_FAILED at $")
    def test_forged_producer_channel_and_evidence_class_fail(self):
        env,p,v=event()
        for key,val in [("producer","pa_evals"),("producer_instance","other"),("channel","EVALUATOR_PRIVATE"),("evidence_class","REAL_AGENT_PRODUCTION")]:
            with self.subTest(key=key),self.assertRaises(ContractError):ingest({**env,key:val},p,v)
    def test_payload_tampering_fails_even_when_envelope_is_valid(self):
        env,p,v=event();raw=canonical_bytes({**p,"input_digest":"b"*64})
        with self.assertRaises(ContractError):validate_ingress(canonical_bytes(env),raw,"fixture-credential",v)
    def test_unsupported_payload_and_missing_effect_receipt_fail(self):
        env,p,v=event()
        with self.assertRaises(ContractError):ingest(env,{**p,"approval_granted":True},v)
        env,p,v=event("effect.observed")
        with self.assertRaises(ContractError):ingest(env,p,v)
        p["receipt_refs"]=["receipt"];ingest(env,p,v)
    def test_payload_identity_and_actor_must_match_trusted_context(self):
        env,p,v=event("finding.updated")
        with self.assertRaises(ContractError):ingest(env,{**p,"actor_id":"impostor"},v)
        with self.assertRaises(ContractError):ingest(env,{**p,"finding_id":"other"},v)
    def test_legacy_records_cannot_enter_active_ingress(self):
        raw=(ROOT/"contracts/examples/event-envelope.example.json").read_bytes();validate_legacy_envelope(raw)
        with self.assertRaises(ContractError):validate_ingress(raw,b'{}',"fixture-credential",Verifier())
    def test_every_catalog_event_has_a_closed_payload_contract(self):
        for e in resource("event-catalog")["events"]:
            rule=resource(e["payload_schema"])
            with self.subTest(event=e["event_type"]):
                self.assertIs(rule["additionalProperties"],False)
                with self.assertRaises(ContractError):validate({"schema_version":"1.0"},e["payload_schema"])


class WorkflowTests(unittest.TestCase):
    def test_all_workflows_have_valid_controls_and_reject_draft_templates(self):
        for p in sorted((ROOT/"contracts/v1").glob("*.template.json")):
            kind=p.name.split(".template")[0]
            with self.subTest(kind=kind):
                workflow(kind,valid_workflow(kind))
                with self.assertRaises(ContractError):workflow(kind,load_json(p.read_bytes()))
    def test_duplicate_selected_trials_do_not_inflate_review_coverage(self):
        v=valid_workflow("review-batch");v.update(selected_trial_ids=["trial","trial"],selected_count=2,eligible_trial_count=2)
        with self.assertRaises(ContractError):workflow("review-batch",v)
    def test_missing_trace_cannot_be_a_pass_annotation(self):
        v=valid_workflow("annotation");v.update(reviewability="UNREVIEWABLE",unreviewable_reason="missing",verdict="PASS")
        with self.assertRaises(ContractError):workflow("annotation",v)
    def test_judge_acceptance_rejects_data_reuse_and_class_error(self):
        v=valid_workflow("calibration");v["audit_set_digest"]=v["development_set_digest"]
        with self.assertRaises(ContractError):workflow("calibration",v)
        v=valid_workflow("calibration");v["confusion_matrix"].update(tp=0,fn=1)
        with self.assertRaises(ContractError):workflow("calibration",v)
    def test_experiment_cannot_activate_without_criteria(self):
        v=valid_workflow("experiment-plan");v["safety_constraints"]=[]
        with self.assertRaises(ContractError):workflow("experiment-plan",v)
        v=valid_workflow("experiment-plan");v["hypothesis"]="changed after registration"
        with self.assertRaises(ContractError):workflow("experiment-plan",v)
        v=valid_workflow("experiment-plan");v["qualified_for_execution"]=False
        with self.assertRaises(ContractError):workflow("experiment-plan",v)
    def test_negative_comparison_is_recordable_but_incomplete_adoption_fails(self):
        v=valid_workflow("experiment-result");v.update(decision="REJECT",complete_pairs=0,missing_pairs=1)
        workflow("experiment-result",v)
        v["decision"]="ADOPT_FOR_QUALIFICATION"
        with self.assertRaises(ContractError):workflow("experiment-result",v)
    def test_monitoring_does_not_invent_health_from_missing_data(self):
        v=valid_workflow("monitoring-window");v.update(eligible_admitted_runs=None,signal_status="NOT_DETECTED")
        with self.assertRaises(ContractError):workflow("monitoring-window",v)
        v["signal_status"]="INSUFFICIENT_DATA";workflow("monitoring-window",v)
        p=valid_workflow("monitoring-plan");p["production_enabled"]=True
        with self.assertRaises(ContractError):workflow("monitoring-plan",p)
    def test_metrics_keep_missingness_and_zero_denominators_visible(self):
        v=sample(resource("metric-result-v1"));v.update(status="NOT_RUN",value=None,numerator=None,denominator=None)
        metric_result(v)
        with self.assertRaises(ContractError):metric_result({**v,"value":0})
        with self.assertRaises(ContractError):metric_result({**v,"status":"COMPUTED","value":0,"denominator":0,"source_snapshot_digest":H,"evidence_refs":["x"]})
        v.update(status="N/A",applicability_reason="no eligible cases",denominator=0);metric_result(v)
        ratio={**v,"status":"COMPUTED","metric_id":"Q04","value":.5,"numerator":1,"denominator":2,"source_snapshot_digest":H,"evidence_refs":["evidence"],"unresolved_count":0,"missing_count":1}
        metric_result(ratio)
        with self.assertRaises(ContractError):metric_result({**ratio,"value":1.0})
    def test_eval_and_gate_precedence_prevents_green_on_missing_evidence(self):
        v=sample(resource("eval-result-v1"));v["assertions"][0]["outcome"]="UNRESOLVED"
        with self.assertRaises(ContractError):evaluation_result(v)
        v["outcome"]="UNRESOLVED";evaluation_result(v)
        gate=sample(resource("gate-result-v1"));gate["missing_requirements"]=["calibration"]
        with self.assertRaises(ContractError):gate_result(gate)
        gate["outcome"]="INCONCLUSIVE";gate_result(gate)
        gate["blockers"]=["unsafe effect"];gate["outcome"]="NO_GO";gate_result(gate)


if __name__=="__main__":unittest.main()
