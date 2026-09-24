"""Configuration selection does not start a runtime or confer permissions."""
from .validation import ContractError, validate


def runtime_config(value: object) -> dict:
    return validate(value, "runtime-config")


def scope_claims(value: object) -> dict:
    """Validate claims supplied by trusted authentication code, never agent JSON."""
    record = validate(value, "scope")
    for key in ("actor_id", "tenant_id", "patient_id", "request_id"):
        if not record[key].strip() or record[key] != record[key].strip():
            raise ContractError("MALFORMED_SCOPE", "$." + key)
    permitted = {"case.read", "requirements.read", "evidence.read", "packet.validate", "review.draft"}
    if not set(record["allowed_operations"]) <= permitted:
        raise ContractError("UNSUPPORTED_OPERATION")
    return record
