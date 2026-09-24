# Open model assets

Keep checkpoint references, exact revisions/digests, model cards, tokenizer/chat
templates, serving/quantization settings, provenance, and license references here.
Weights remain in an approved registry/cache, not ordinary Git. Do not assume
every model in a family shares the same terms or resource requirements.

registry.json contains an unselected Nemotron candidate and the deterministic
mock baseline. No real model is selected or downloaded. Model adapters live in
model_adapters/; the agent depends on the common contract, not an NVIDIA SDK.

Select a real model only after pinning its artifact, supported inference backend,
hardware budget, relevant capabilities, usage rights, and evaluation plan.
Generic model benchmarks do not establish PA readiness performance.
