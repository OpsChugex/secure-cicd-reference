# OCX-CICD-001: Secure CI/CD Reference

[![Secure CI/CD reference pipeline](https://github.com/OpsChugex/secure-cicd-reference/actions/workflows/pipeline.yml/badge.svg)](https://github.com/OpsChugex/secure-cicd-reference/actions/workflows/pipeline.yml)

**Classification:** Executable reference pipeline

This repository turns the documented delivery sequence into a reproducible pipeline using a small, self-contained Python service.

## Gates executed

- Python compilation
- unit test
- Bandit static analysis
- pip-audit dependency review
- container image build
- Trivy container scan
- runtime smoke test against the built image

The security tools are version-pinned, GitHub Actions are pinned to immutable commit SHAs, and repository permissions are read-only.

## Reproduce the application test locally

```bash
python -m unittest -v
```

The sample application uses only the Python standard library. `requirements.txt` is intentionally empty of runtime packages so dependency evidence is explicit rather than hidden.

## Delivery boundary

This workflow does not deploy to AWS, Azure, Kubernetes or any customer environment. It uses no deployment credentials and makes no production-outcome claim.

A production delivery pipeline would add environment approval, signed or attested artifacts, target-specific deployment, post-deployment verification and rollback controls.

## Evidence interpretation

A passing run proves that the tested commit passed the gates listed above at that time. It does not prove customer delivery, production availability, SOC 2 compliance or the absence of every possible security issue.

See [pipeline.md](pipeline.md) for the reference sequence.
