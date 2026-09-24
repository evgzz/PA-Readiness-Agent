"""Authenticated event boundary. Transport credential verification is injected.

No default authenticator, network endpoint, durable writer or exporter is provided.
"""
from pa_contracts.configuration import scope_claims
from pa_contracts.evidence_ports import Authenticator, IngressIdentity, ValidatedEvent
from pa_contracts.serialization import bytes_digest
from pa_contracts.validation import ContractError, load_json, resource, validate
from pa_contracts.workflows import evaluation_result, gate_result, workflow

WORKFLOWS = {"review.batch.created": "review-batch", "review.annotation.recorded": "annotation",
             "taxonomy.versioned": "failure-taxonomy", "calibration.finalized": "calibration",
             "experiment.registered": "experiment-plan", "experiment.finalized": "experiment-result",
             "monitoring.window.finalized": "monitoring-window"}


def validate_ingress(envelope_bytes: bytes, payload_bytes: bytes, credential: object,
                     authenticator: Authenticator) -> ValidatedEvent:
    try:
        identity = authenticator.authenticate(credential)
    except Exception:
        raise ContractError("AUTHENTICATION_FAILED") from None
    if not isinstance(identity, IngressIdentity) or not identity.principal_id:
        raise ContractError("AUTHENTICATION_FAILED")
    envelope = validate(load_json(envelope_bytes), "event-envelope-v1")
    if envelope["producer"] != identity.producer or envelope["producer_instance"] != identity.producer_instance:
        raise ContractError("FORGED_PRODUCER")
    if envelope["channel"] not in identity.channels or envelope["evidence_class"] not in identity.evidence_classes:
        raise ContractError("UNAUTHORIZED_CHANNEL_OR_EVIDENCE_CLASS")
    if bytes_digest(payload_bytes) != envelope["payload_sha256"]:
        raise ContractError("PAYLOAD_DIGEST_MISMATCH")
    event_type = envelope["event_type"]
    if event_type in {"run.started", "run.completed", "model.call.completed",
                      "action.proposed", "authorization.decided", "action.dispatched",
                      "effect.observed", "effect.reconciled", "assessment.validated",
                      "trial.graded", "run.finalized"}:
        if not envelope["run_id"] or not envelope["candidate_config_digest"]:
            raise ContractError("MISSING_RUN_IDENTITY")
    if event_type in {"trial.graded", "run.finalized"} and not envelope["evaluation_config_digest"]:
        raise ContractError("MISSING_EVALUATION_IDENTITY")
    catalog = {x["event_type"]: x for x in resource("event-catalog")["events"]}
    spec = catalog[event_type]
    if envelope["producer"] != spec["producer"] or envelope["channel"] != spec["channel"]:
        raise ContractError("PRODUCER_CHANNEL_MISMATCH")
    payload = validate(load_json(payload_bytes), spec["payload_schema"])
    if "actor_id" in payload and payload["actor_id"] not in identity.actor_ids:
        raise ContractError("UNAUTHORIZED_ACTOR")
    for key in ("run_id", "trial_id", "case_id", "action_id", "attempt_id", "finding_id", "candidate_config_digest", "evaluation_config_digest", "evidence_class"):
        if key in payload and payload[key] is not None and key in envelope and envelope[key] != payload[key]:
            raise ContractError("PAYLOAD_ENVELOPE_IDENTITY_MISMATCH", "$." + key)
    if event_type == "run.started":
        scope_claims(payload["scope"])
    if event_type == "run.completed" and payload["terminal_outcome"] == "DELIVERED" and not payload["assessment_ref"]:
        raise ContractError("MISSING_DELIVERED_ASSESSMENT")
    if event_type == "assessment.validated":
        if payload["delivered_outcome"] == "READY" and (payload["blockers"] or payload["unresolved_checks"] or not payload["evidence_refs"]):
            raise ContractError("UNSUPPORTED_DELIVERED_READY")
        if payload["delivered_outcome"] == "NOT_READY" and not payload["blockers"]:
            raise ContractError("MISSING_BLOCKER")
        if payload["delivered_outcome"] == "UNKNOWN" and (payload["blockers"] or not payload["unresolved_checks"]):
            raise ContractError("INVALID_UNKNOWN")
    if event_type == "trial.graded":
        evaluation_result(payload)
    if event_type == "release_gate.evaluated":
        gate_result(payload)
    if event_type in WORKFLOWS:
        workflow(WORKFLOWS[event_type], payload)
    if event_type in {"effect.observed", "effect.reconciled"}:
        if payload["observation"] != "UNRESOLVED" and not payload["receipt_refs"]:
            raise ContractError("MISSING_EFFECT_RECEIPT")
    if event_type == "run.finalized":
        if payload["completed_trials"] + payload["missing_trials"] != payload["scheduled_trials"]:
            raise ContractError("TRIAL_COUNT_MISMATCH")
        if payload["finalization_status"] == "COMPLETE" and payload["missing_trials"]:
            raise ContractError("INCOMPLETE_RUN")
    if event_type == "coverage.updated":
        if payload["complete_slices"] + payload["incomplete_slices"] != payload["required_slices"]:
            raise ContractError("COVERAGE_COUNT_MISMATCH")
    return ValidatedEvent(envelope_bytes, payload_bytes, identity.principal_id)


def validate_legacy_envelope(raw: bytes) -> dict:
    """Read-only archival validation. Never returns an ingestible ValidatedEvent."""
    return validate(load_json(raw), "event-envelope-legacy")
