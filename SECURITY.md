# Security Policy

## Reporting a vulnerability

Please report suspected vulnerabilities **privately** via GitHub's
**Private Vulnerability Reporting** for this repository:
`Security` tab → `Report a vulnerability`.

Do **not** open a public issue for security reports.

You can expect an acknowledgement within 7 days. Please include steps to
reproduce, the affected version/commit, and impact as you understand it.
Coordinated disclosure is appreciated; we will credit reporters unless you
prefer otherwise.

## Scope

- The code in this repository and its published release artifacts.
- Out of scope: vulnerabilities in third-party runtime prerequisites
  (report those upstream), and issues requiring a compromised local machine.

## Supply-chain verification

Release artifacts carry:

- a **CycloneDX SBOM** attached to each GitHub Release, and
- **SLSA build provenance** attestations, verifiable with:

```
gh attestation verify <artifact> --repo <OWNER>/<PROJECT>
```

If verification fails for an artifact claiming to be from this project,
treat it as untrusted and report it.

## Hardening posture (what this project promises)

- No network calls and no telemetry in the shipped tool.
- Dependencies pinned via committed lockfile; audited in CI (`pip-audit`).
- Static analysis (CodeQL, bandit) and secret scanning gate every change.
- No long-lived signing keys: attestations use ephemeral OIDC (keyless) identities.
