"""Local contract validation only; never starts a model, tool or exporter."""
import argparse
from pathlib import Path
import sys

from .configuration import runtime_config, scope_claims
from .runtime_ports import runtime_input, answer_proposal
from .serialization import digest
from .validation import ContractError, load_json, validate
from .workflows import workflow, metric_result, evaluation_result, gate_result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("contract", help="resource contract name; runtime-config, workflow-*, metric-result-v1")
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    try:
        record = load_json(args.file.read_bytes())
        structural_only = False
        if args.contract == "runtime-config":
            record = runtime_config(record)
        elif args.contract in {"runtime-input", "scope", "readiness-answer-v1"}:
            record = {"runtime-input": runtime_input, "scope": scope_claims,
                      "readiness-answer-v1": answer_proposal}[args.contract](record)
        elif args.contract.startswith("workflow-"):
            record = workflow(args.contract.removeprefix("workflow-"), record)
        elif args.contract in {"metric-result-v1", "eval-result-v1", "gate-result-v1"}:
            record = {"metric-result-v1": metric_result, "eval-result-v1": evaluation_result, "gate-result-v1": gate_result}[args.contract](record)
        else:
            record = validate(record, args.contract)
            structural_only = True
        print(("VALID_STRUCTURE " if structural_only else "VALID_CONTRACT ") + digest(record))
        return 0
    except (ContractError, OSError) as exc:
        print(str(exc) if isinstance(exc, ContractError) else "FILE_READ_FAILED", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
