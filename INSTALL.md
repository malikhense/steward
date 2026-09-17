# Install Steward for the user

Use this procedure when the user gives this repository link and asks to install Steward. Complete the installation through the tools available in the current host. Do not merely relay these steps or ask the user to choose every skill. Install the full suite because its skills share relative references.

## 1. Resolve the host and current state

Identify the actual agent host, its documented skill or local-plugin installation route, filesystem access, and existing Steward installation. Read any applicable host installer guidance. Resolve the destination from host configuration or existing trusted installation conventions; ask only when the scope or location cannot be determined safely. Inspect local edits before replacing anything. Use one route, plugin or copied skills, to avoid duplicate entries.

A Mac is required for the bundled Apple helpers, not for Markdown memory and core planning. Required runtime and app capabilities are in [requirements](docs/install.md#requirements). Do not install compilers, change security settings, or connect accounts merely to complete a basic skill installation.

## 2. Obtain the released package

Use the public repository `malikhense/steward`; a GitHub account is not required to read it or download releases. Reuse existing authorized tooling when available, but do not make signing into GitHub a prerequisite for public downloads. Fetch the latest published release's `steward-<version>.zip` and `SHA256SUMS`, or the exact version the user requested. Use available GitHub tools or the public HTTPS release/API endpoints. Download into a fresh local staging folder, verify the archive's SHA-256 against the matching checksum entry, inspect archive paths before extraction, and read the packaged instructions and installer before executing it. Do not pipe downloaded text into a shell.

If the repository is inaccessible, identify the exact sign-in or repository-access dependency. If the host lacks local file access, explain that limit and provide the supported local route. Do not claim installation from a downloaded link alone. A checksum verifies artifact consistency, not independent trust or authorship.

## 3. Install and read back

For the copied-skill route, use the extracted package's `scripts/install.py` with the resolved destination. Preview first; apply when preflight succeeds. Installation is already requested, so do not introduce a second generic confirmation unless host policy requires it.

```text
python3 scripts/install.py --dest ACTUAL_SKILL_DIRECTORY
python3 scripts/install.py --dest ACTUAL_SKILL_DIRECTORY --apply
```

For an existing managed installation, use `--update` in both commands. The installer backs up managed changes, protects independent edits, and migrates earlier names. If it reports a conflict, inspect and reconcile it; preserve the user's changes. For a host plugin route, use its supported installer and verify the installed bundle rather than also copying its skill folders.

Verify every installed runtime file against the release and resolve the sibling references. Confirm how the host discovers the installed entry. If a refresh is necessary, perform it where supported or give the exact user step. File installation and live host discovery are separate observations. Report the installed version, location, and any actual remaining prerequisite.

## 4. Hand off to the conversation

Read the installed `steward/SKILL.md`. Reuse a known personal workspace or memory folder; the repository is product source, not the user's personal vault. Preserve the vault's name and existing records. If the user requested setup or help getting started, continue the session workflow conversationally from the next unresolved choice. If they only asked to install, finish with a short confirmation, one sentence explaining what Steward helps with, and a clear invitation: “Ready to set it up? I’ll walk you through memory, app connections, and one useful first task.” If the host requires a new turn, give the exact starting phrase: “Help me get started with Steward.” Do not force a life questionnaire into an install-only request.

Memory choices, app selection, and permission prompts belong to the relevant onboarding branches. Installing the suite does not select apps, grant access, authorize sends, or create background tasks. Complete independent work while optional access is pending.

The human-facing guides are [Get set up](docs/install.md), [Your first conversation](docs/first-use.md), and [Using Steward](docs/using-steward.md).
