# Open development data

Publishable development assets: synthetic inputs, generation/curation code,
data cards, partition lineage, and reviewed public examples. Preserve parent-case
and family identity when generating variants. Keep labels out of agent inputs.

Held-out inputs and oracles belong in separately controlled storage while they
serve qualification. manifests/heldout.template.json is an empty descriptor,
not hidden data. A path convention or .gitignore does not enforce isolation.
Once inputs/answers are released, treat them as public benchmark/development data
for later work, not an untouched qualification set.

The three simple synthetic cases supplied here are interface examples. They are
not full FHIR resources, clinical policies, model training data, or validated tests.
No real patient records or production trajectories are included.
