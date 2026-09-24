# Composition roots

Planned apps: runtime/, evaluate/, review/, reporting/, demo/.
Wire concrete implementations here through contracts. Runtime and evaluator use
separate identities/mounts; labels never enter runtime input. A selected loop is
mock or SDK, never both for one run. Reporting consumes metric/gate snapshots and
safe trace links. Authenticated approval actions belong to the governance service.
No application, API server, dashboard or runtime CLI is implemented in this scaffold.
