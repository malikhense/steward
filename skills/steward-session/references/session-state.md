# Resumable session state

Use [storage](../../steward-memory/references/storage.md) for all retrieval and writes. Keep lifecycle state in the configured vault, never in a skill folder. Respect existing equivalent fields instead of creating a parallel source of truth.

For a new vault, `System/Session.md` can hold the small state below; `Home.md` links to it and to the active work. In an existing vault, use its current index and records, adding only missing distinctions when needed.

| Field | Meaning |
|---|---|
| Setup | not-started, in-progress, ready, or blocked; evidence and the exact unresolved prerequisite |
| Memory | Actual location and mode: plain Markdown, Obsidian-backed Markdown, or no durable store |
| Onboarding | not-started, in-progress, complete, or skipped; last completed step and next unresolved question |
| Connections | Link to System/Connections.json or the existing equivalent; per-app choices, scope, verification and pending access remain there |
| Context review | Link to System/Context.md or equivalent: selected sources, scope, content coverage, observed time, gaps, and tentative proposals |
| Current work | Links to the selected goal/plan or bounded request; source of truth stays in those records |
| Next | Concrete next action and whether it belongs to the agent or the user |
| Pending | Only decisions, missing observations, or access that affect continuation |
| Return | Optional review trigger; scheduler status/identifier only when actually configured |
| Updated | Recording date and provenance for material decisions |

Setup ready means the installed suite is accessible, the intended store is resolved, and authorized saving and retrieval have been verified. It does not mean Obsidian is registered unless that was separately checked. Personal onboarding has its own completion criteria in [onboarding](onboarding.md).

For an existing user with no onboarding record, infer neither completion nor a need to restart. Continue their requested work using known context; offer orientation only when useful or requested. A skipped onboarding stays skipped until revisited. Preserve separate goal identities and let the user change focus without rewriting other goals' statuses.

At an interruption, preserve the last completed step and specific remaining work. On resumption, inspect actual files and current constraints before continuing. Readiness claims and prior scheduler observations need appropriate verification; elapsed time proves neither task completion nor participation.

For no-storage use, put these essentials in a compact continuation note the user can carry forward. State that resumption requires that note; a transcript or permanent cross-task memory is not assumed.
