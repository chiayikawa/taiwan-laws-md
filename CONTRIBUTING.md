# Contributing

Thank you for helping improve taiwan-laws-md.

This project exists to make Taiwan's official law database easier to search, version, and use in developer and AI workflows. Contributions should preserve the official source text and make maintenance more reliable.

## Good First Contributions

- Report a Markdown formatting issue in a law file.
- Report a missing or stale law.
- Improve documentation for legal research, civic tech, or AI/RAG use cases.
- Improve validation checks for the converted dataset.
- Propose metadata fields for indexing and search.

## Rules For Data Changes

- Do not manually rewrite law text in `laws/`.
- Law text should come from the National Laws and Regulations Database Open API.
- If a generated file looks wrong, fix the converter or report the upstream data issue.
- Include the law name, file path, and official URL when opening an issue.

## Local Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 scripts/fetch_and_convert.py
python3 scripts/validate_dataset.py
```

## Pull Requests

Before opening a pull request:

1. Run `python3 scripts/validate_dataset.py`.
2. Keep changes focused.
3. Explain whether the PR changes code, documentation, generated data, or workflow behavior.
4. If changing the converter, include an example law file affected by the change.

## Maintainer Review

The maintainer will review whether the PR:

- Preserves official legal text.
- Keeps generated output deterministic.
- Improves access, search, validation, or maintenance.
- Avoids introducing legal advice or unofficial interpretation into generated law files.
