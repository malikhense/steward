# Working on Steward skills

For a user request to install Steward from this repository, follow [INSTALL.md](INSTALL.md) and complete the authorized installation before handing back instructions.

This repository contains reusable skill source. Read the relevant entrypoint and linked references before changing behavior. Use writing-for-agents and skill authoring guidance when available.

Preserve independently useful skill boundaries and complete requested work across them without imposing a mandatory pipeline. Keep shared meanings in one authoritative reference and maintain relative sibling links. Personal goals, preferences, vault paths, and live action state belong in the user's separate memory store.

Run `python3 scripts/check.py` after runtime edits. For substantive behavioral changes, use realistic isolated fixtures and record the actual checks and limits; earlier evaluations do not certify a later revision. Do not import personal vault records or conversation transcripts into this repository.

Keep installation separate from source edits. Updating source does not authorize overwriting installed skills, publishing a release, or changing personal memory. Use the user's current explicit instructions and the host's action policy for those operations.

Product naming: Steward is the product and every runtime skill uses steward or steward-*. A user may independently name their memory vault. Use “AI agent” in product copy and use commas, periods, or parentheses instead of em dashes.

Public publishing: use the owner’s GitHub no-reply address for both author and committer metadata. Construct merge commits locally with that identity and inspect their metadata before pushing. GitHub-hosted merge operations can use the account email despite local Git configuration; do not use them without verified no-reply author control. Before publishing, inspect every new reachable commit, not just the tip.
