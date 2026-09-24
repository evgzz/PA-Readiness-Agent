# Tests

Implemented: tests/contracts/test_boundaries.py, run using the standard library:

```bash
python3 scripts/run_contract_tests.py
```

The suite exercises strict input handling, scope/proposal separation, hidden-label
field rejection, active versus legacy event versions, producer/channel/actor
identity, payload tampering, workflow activation, calibration/error criteria,
missingness, denominator rules and outcome precedence. Positive controls are
synthetic contract records; no test is a real-agent evaluation.

Runtime, process/network isolation, reset/replay, model/tool integration and
adversarial agent suites remain implementation work. Static import checks are
organizational checks, not a security sandbox. Full JSON Schema conformance is
not asserted by the owned-schema validator.
