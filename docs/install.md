# Get set up

Steward runs inside a local AI agent that supports skills. Setup gives it a place to save context and, if you choose, access to useful apps. Personal onboarding comes next: choosing something you actually want help with.

## Let your agent handle installation

Ask your local coding agent:

> Install Steward from https://github.com/malikhense/steward

Your agent should read the repository’s [installation procedure](../INSTALL.md), resolve the supported destination, install the whole suite, and verify it. You do not need to choose individual skill folders or copy commands yourself.

The repository is public; reading it and downloading a release do not require a GitHub account. Install the complete suite because skills use relative sibling references. Memory and app configuration belong outside the repository.

Once installed, you do not need to run commands for everyday use. Start a conversation with “Help me get started with Steward.” It checks what is ready and asks only for unresolved choices. [See the first conversation](first-use.md).

You are ready to begin when the skill suite is available and either your chosen memory folder can be saved/read or you have chosen a no-storage trial. Optional app permissions can stay pending. The agent should tell you what worked and name any step that only you can finish.

## Manual installation from a release or checkout

The release archive expands into a `steward/` folder containing a plugin manifest, every skill, and the same source/checks as the repository. A host that supports local plugins can install that folder through its documented plugin flow. Otherwise install the skill folders with the helper below. Choose one installation route to avoid duplicate skills.

Inside the extracted folder or checkout:

```sh
python3 scripts/install.py --dest /absolute/path/to/your/host/skills
python3 scripts/install.py --dest /absolute/path/to/your/host/skills --apply
```

Resolve the actual skill destination from the host; do not guess another assistant's folder. The first command previews. The second installs and verifies every runtime file. Repeating an identical install is harmless. Local conflicts stop before copying.

Start a task in your intended personal workspace and say **“Use Steward to get started.”** If the host does not discover the new skill immediately, refresh/restart it according to its instructions.

## Requirements

- A local agent host that supports skills and reading/writing your selected files. Python 3.9+ for the helpers.
- Apple helper operations: macOS 14+, a working Apple Swift compiler (Command Line Tools or Xcode), the relevant apps/accounts, and macOS permissions.
- Contacts/Mail/Messages and advanced app workflows: a supported computer-control tool in the host, with access to the unlocked Mac. No such tool means that route remains unavailable, not automatically connected.
- Obsidian is optional. Plain Markdown memory works without it. AI-host usage and third-party services retain their own terms and costs.

The package does not install a compiler, alter macOS privacy permissions, configure iCloud, register a workspace behind the host's back, or create background automations.

## Update without losing your edits

Install from a new release with `--update`:

```sh
python3 scripts/install.py --dest /absolute/path/to/your/host/skills --update
python3 scripts/install.py --dest /absolute/path/to/your/host/skills --update --apply
```

The managed installer records hashes in `.steward-installation.json`. It updates only files that still match the previous managed install and archives changed skill folders under `.steward-backups/` before replacement. Added or edited local files trigger a conflict, so ask your agent to reconcile them. An older/unmanaged installation must be compared and backed up deliberately before adoption; the updater does not guess its baseline.

The installer expects one writer. If interrupted by a filesystem error, inspect the partial result and backup before retrying. This is recoverable local installation, not a transactional package manager.

## Remove or disconnect

To stop a source from supplying context, ask Steward to disconnect it. To revoke OS access, use the appropriate macOS Privacy & Security setting; these are separate changes.

To remove the suite, use the host's plugin uninstall flow if installed as a plugin. For a copied-skill installation, ask your agent to inspect `.steward-installation.json`, identify exactly the installed Steward folders, preserve local changes, and remove only those folders and the receipt. Your personal memory folder, Apple data, and previous actions remain separate. Do not delete them as part of uninstall unless explicitly requested. The Apple helper cache and private policy can be removed separately after confirming they are no longer needed.

### Updating from 0.2.0

Use `--update` to migrate the managed `kernel-*` skill folders to `steward-*`. The installer verifies the old receipt, backs up the original folders, installs and verifies the new names, then removes only the unchanged old copies. Local edits stop migration for reconciliation. Update any workspace skill pointers to `steward-*`; retain the actual memory vault name and path. Old command names are retired rather than installed as duplicate aliases.

Ready? Continue with [your first conversation](first-use.md) or [everyday use](using-steward.md).
