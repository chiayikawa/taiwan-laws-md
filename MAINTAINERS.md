# Maintainers

## Primary Maintainer

- GitHub: [@chiayikawa](https://github.com/chiayikawa)

## Maintainer Responsibilities

- Keep the weekly update workflow operational.
- Review data formatting issues and converter changes.
- Triage issues related to missing, stale, or malformed law files.
- Review pull requests for deterministic output and source integrity.
- Maintain documentation for legal research, civic tech, and AI/RAG use cases.

## Project Health Checks

The maintainer should periodically verify:

- The GitHub Actions weekly update job succeeds.
- The converter still matches the National Laws and Regulations Database API format.
- `python scripts/validate_dataset.py` passes.
- Documentation accurately explains source, license, limitations, and usage.
