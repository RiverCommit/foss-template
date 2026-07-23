# foss-template

A reusable template for privacy-respecting, supply-chain-transparent FOSS projects.
Clone/instantiate this for each new project; replace every `<PLACEHOLDER>`.

## What this template gives you

| Concern | Mechanism | Where |
|---|---|---|
| License | Apache-2.0 (patent grant) | `LICENSE`, `NOTICE` |
| Vulnerability disclosure | Policy + GitHub private reporting | `SECURITY.md` |
| Third-party attribution | Aggregated notices | `THIRD_PARTY_NOTICES.md` |
| Pinned dependencies | `pyproject.toml` + committed `uv.lock` | repo root |
| CI: tests + SAST + dep audit | pytest, bandit, pip-audit on every push/PR | `.github/workflows/ci.yml` |
| SAST (deep) | CodeQL | `.github/workflows/codeql.yml` |
| Dependency updates | Dependabot (pip + actions, weekly) | `.github/dependabot.yml` |
| Release: SBOM | CycloneDX via syft, attached to release | `.github/workflows/release.yml` |
| Release: provenance | SLSA build provenance attestation | `.github/workflows/release.yml` |
| Release: audit gate | pip-audit must pass before release | `.github/workflows/release.yml` |

## Per-project checklist (do these after instantiating)

1. Replace `<PROJECT>`, `<YEAR>`, `<OWNER>` in: `README.md`, `NOTICE`, `SECURITY.md`, `pyproject.toml`.
2. `uv lock` and commit `uv.lock` — the SBOM and audits read from it.
3. In repo Settings → Security: enable **Private vulnerability reporting**,
   **Secret scanning** + **Push protection**, **Dependabot alerts**.
4. In repo Settings → Branches: protect `main` (require PR or at minimum block force-push).
5. First release: `git tag v0.1.0 && git push --tags` — the release workflow
   builds, audits, generates the SBOM, attests provenance, and publishes.
6. Verify a release artifact's provenance:
   `gh attestation verify <file> --repo <OWNER>/<PROJECT>`.

## Principles baked in

- **Offline-respecting:** nothing in this template phones home; CI runs only in GitHub Actions.
- **No secrets in CI:** signing and attestation use the workflow's OIDC identity (keyless) —
  there are no long-lived keys to leak.
- **Fail loud:** audits and scans are blocking gates, not advisory noise.
- **Pin what you can:** dependencies are pinned via lockfile. Actions are version-tagged;
  for maximum supply-chain rigor, pin each action to a full commit SHA (marked TODO in workflows).

## License

Apache-2.0 — see `LICENSE`.
