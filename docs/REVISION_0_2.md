# Revision 0.2 change record

Date: 2026-09-24. Supersedes the documentation in the original repository scaffold.

| Previous design ambiguity | Revision |
|---|---|
| Custom loop and proposed SDK loop both described | Exactly one runtime adapter per run; harness retains authority |
| Release-gate computation placed under reporting in discussion | Independent `governance/` package; reporting reads snapshots |
| Product, eval and HOLD/GO terms mixed | Preserve original gate enum; HOLD is a UI label; authorization separate |
| Dashboard hooks listed without evidence authority | Producer/channel contracts, action receipts, complete retained evidence |
| Metrics described informally | Versioned formulas, denominators, unresolved counts, snapshots and refresh rules |
| Program ownership and closure records absent | Catalog, coverage, findings, dependencies, exception/authorization templates |
| Vendor choices sounded implemented | Twenty PROPOSED ADRs; no installed/locked vendor stack |
| Default SDK telemetry destination unspecified | Explicit exporter/egress acceptance before integration |

Existing three public cases and their draft labels are retained. Legacy
implementations remain external source/reference artifacts. No historical test counts are
imported. Core runtime/eval package skeletons are retained; new governance,
telemetry, and runtime-adapter skeletons are added. The static checker is extended
to require the revision documents and selected registry invariants.

Schema note: existing v0.1 readiness/proposal/eval-result schemas remain draft
interfaces. Revision 0.2 adds an event envelope and reporting contract; implementation
Task 00 must version and reconcile the full payload/port family before runtime use.

No runtime code, live model execution, FHIR connectivity, real-agent red teaming,
dashboard deployment, release authorization, Git commit/push, or publication is
performed by this specification revision.
