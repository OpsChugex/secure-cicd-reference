# Reference pipeline contract

The executable workflow follows this sequence:

1. Source checkout from the tested commit
2. Python compilation
3. Unit test
4. Static security analysis with Bandit
5. Dependency review with pip-audit
6. Container image build
7. Container image scan with Trivy
8. Runtime smoke test of the built image
9. Evidence summary attached to the workflow run

A successful build alone is not treated as a validated release.

This repository intentionally stops before deployment. Deployment credentials, target environments and production rollback controls are outside the scope of this reference.
