# Open asset and publication model

The intended public package is code + model references/cards + synthetic data and
recipes + tools/contracts + reproducible, reviewed evaluation evidence. Model
weights may be hosted separately. Choose ownership, versioning, license, and
redistribution rights per artifact; one repository license does not resolve every
upstream model/dataset/tool's terms. License selection remains an owner decision.

| Asset | Intended public material | Controlled material |
|---|---|---|
| Models | Artifact references, exact revisions, cards, serving settings | Credentials, restricted weights, tenant adapters |
| Data | Reviewed synthetic development data and generation/curation recipes | PHI, proprietary payer rules, active qualification inputs/oracles |
| Tools | Contracts, permitted reusable clients, synthetic mocks | Secrets, payer endpoints/configuration, protected responses |
| Evals | Public cases, scorers, rubric definitions, reproduction instructions | Reserved answers, private annotations, raw protected traces |
| Results | Reviewed aggregate metrics, uncertainty, coverage, hashes | Raw clinical evidence and identifying examples |

Stage publication from an explicit reviewed inventory. Excluding files from Git
is insufficient for runtime data isolation. Secret/PII scanners are supporting
checks, not proof of release eligibility. Public benchmark contamination must be
considered when selecting fresh qualification data. No public release occurs
as part of this scaffold.
