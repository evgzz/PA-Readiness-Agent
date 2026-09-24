# V2 adversarial evaluation and governance mapping

Status: PLANNED. Only owned, isolated synthetic PA targets are in scope. Tools that
submit, write, cancel, message externally or delegate remain disabled. Forced
proposals and a simulated vulnerable control cannot be reported as production attacks.

## Threat surface and project controls

Source taxonomy: [OWASP Agentic Top 10, 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/),
published December 2025. The risk summaries and PA mappings below are project
interpretations of its ASI01–ASI10 categories, not a certification checklist.

| OWASP ID / risk summary | PA attack surface / applicable test | Control and acceptance evidence |
|---|---|---|
| ASI01 / redirected objectives | Document or user text tells the agent to bypass readiness requirements | Untrusted text never changes scope; retain attempted and delivered decisions |
| ASI02 / abusive tool calls | Read tool arguments used to request a write or foreign resource | Closed catalog and adapter checks; permitted reads remain successful |
| ASI03 / excess privilege | Forged actor, tenant, patient or approval fields | Trusted identity and least privilege; cross-case read/disclosure independently checked |
| ASI04 / compromised dependencies | Changed tool definitions, model artifacts or requirements packages | Exact pins, provenance and integrity validation; altered artifacts rejected |
| ASI05 / unintended execution | Tool output requests shell/code execution | No code-execution capability in this profile; bypass test and no-effect evidence |
| ASI06 / poisoned state | Earlier turn plants false authority or stale evidence | Evidence versioning, correction handling and reset isolation across turns |
| ASI07 / forged agent messages | Delegation attempt or claimed peer-agent authority | Delegation remains disabled; verify rejection. Operational inter-agent protocol coverage is out of scope |
| ASI08 / propagated failures | Tool outage or false result causes repeated or unsafe downstream decisions | Bounded retries, reconciliation, UNKNOWN when appropriate and preserved missingness |
| ASI09 / misleading reviewers | Fabricated citations or persuasive approval claims | Source-linked local packet, independent validation and explicit unresolved reasons |
| ASI10 / uncontrolled autonomy | Continued operation after cancellation, scope exhaustion or budget limit | Supervisor termination and catalog limits; no hidden continuation/effect |

Input guards validate structure and scope; tool guards authorize every dispatch;
output guards validate claims and references. Detection signals may aid triage but
are not the authorization boundary. Test controls with hostile model proposals,
not an assumption that an injection detector will recognize every attack.

## Live red-team adapter and regression conversion

Use a version-pinned promptfoo adapter targeting the running synthetic PA endpoint.
Its official [HTTP provider](https://www.promptfoo.dev/docs/providers/http/) supports
request/response translation and [red-team configuration](https://www.promptfoo.dev/docs/red-team/configuration/)
selects generation and execution behavior. No version, credentials or plugin set
is selected yet. A general scanner is not the authoritative PA grader.

The future adapter must bind target allowlist, authenticated synthetic session,
reset receipt, candidate/eval/attack configuration, injection surface and trial ID.
Multi-turn probes follow the same session protocol; they cannot inject control-plane
identity. Record generator model and seed/settings separately from the target model
and judge. Explicitly control generation, grading and report-export destinations;
no default remote service is authorized by choosing the library.

Execute declared attacks with budgets and legitimate positive controls. Retain raw
attempts privately; independently inspect action/effect receipts and delivered
answers. Capture attempted compromise, blocked operation, confirmed effect and
unresolved evidence separately. Provider/scanner labels cannot override receipts.

For every confirmed successful attack: preserve the original trace and world,
minimize a development reproducer without changing the failure, bind its predicate
and expected initial state, add a failing adversarial regression, implement the
mitigation, retest and run adjacent positive/regression controls. Keep an unsuccessful
campaign as a negative result. A seeded vulnerable control proves test sensitivity,
not a successful exploit of the real candidate. Never create an actual clinical
write merely to demonstrate approval behavior.

## Human approval and framework records

R2 consequential operations stay disabled in the PA profile. Exercise the future
approval state machine only against simulated effects: authorized reviewer,
case/action/destination/payload/config/evidence binding, expiry, revocation, replay,
concurrent consumption and ambiguous-effect reconciliation. These reference
controls do not enable real operations.

[NIST AI RMF 1.0](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) provides
Govern, Map, Measure and Manage functions. The proposed PA record maps them as follows:

| Function | Required project record |
|---|---|
| Govern | Named accountable owner, policy/version, decision rights, exception history and separate release authorization |
| Map | Intended use, affected stakeholders, data/operation boundaries and threat/applicability map |
| Measure | Frozen cases, human labels, calibrated criteria, adversarial results, uncertainty and evidence gaps |
| Manage | Prioritized findings, mitigation owner/date, retest, residual-risk disposition and monitoring/incident response |

The [European Commission AI Act overview](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
describes a use-dependent risk approach. Record jurisdiction, intended use,
provider/deployer role, applicable-rule assessment, authoritative source/version,
reviewer and review date before any operational claim. Classification, obligations
and effective dates are unresolved here; do not infer compliance from PA subject
matter, a NIST mapping, an OWASP test or a passed gate. A qualified legal review is
an operational dependency, not a fabricated legal determination in this demo.

Required output: attack-surface register, pinned campaign manifest, original trial
receipts, finding/regression/mitigation links, simulated approval controls, NIST
mapping and legal-applicability status. All remain NOT_RUN / UNASSIGNED.
