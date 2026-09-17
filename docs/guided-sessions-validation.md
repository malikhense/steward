# Guided session validation

Checked 2026-09-16. Source adds steward-session, four conditional references, a new-folder memory scaffolder, a local suite installer, first-use guidance, and an explicit exemplar checkpoint. The product is named Steward; the technical namespace stays steward-*. The recorded behavioral trials preceded this display-name change; their original evidence is preserved.

## Repeatable checks

- Native skill validation passed for all 14 entrypoints.
- `python3 scripts/check.py` passed: 14 skills, 121 local references.
- `python3 -m unittest discover -s tests -v` passed seven tests: preview without mutation; create/read-back/repeat preserving human edits; existing-vault preservation; partial-scaffold preservation; symlink refusal; full installation preview/apply/repeat; and installation conflict stopping before other copies.
- Git whitespace checks passed.

The helpers were executed only against temporary test directories. The suite installer is intentionally a first-install tool: conflicting installed versions require a deliberate managed update. Both helpers require a single writer. A filesystem failure can leave partial files; they preserve those for inspection rather than promising atomic recovery.

## Independent forward trials

Two independent agents executed five synthetic user requests with the revised source. The evaluators were given raw requests and fixtures, not expected answers. Actual outputs and before/after records were inspected by the implementing agent.

| Case | Observed behavior |
|---|---|
| New plain Markdown user, unable to install apps, unsure of focus | Created and verified local memory; offered a meaningful preference choice and saved it as pending without inventing a goal. |
| Existing Obsidian vault and move goal, app unavailable | Preserved existing prose and goal identity; produced a furniture inventory while stating that Obsidian integration was unverified. |
| Interrupted personal onboarding | Used the supplied fifteen-minute availability, retained the drawing goal, and prepared a first-session guide; actual participation remained unknown. |
| Return after a gap | Recovered reading as the selected focus and asked for actual experience; kept a separate garden goal paused and made no redundant writes. |
| Specific reply with onboarding skipped | Produced the requested short draft without onboarding, a new goal, or sending. |

The first-use agent reread the final research-quality reference after duplicate exemplar language was consolidated during its run. Its two material deliverables already contained inspected exemplar sources and adaptation notes. The return/draft cases required no new exemplar search. The final runtime file hashes and path-normalized actual artifacts are preserved in [execution evidence](guided-sessions-evidence.json).

## Limits

These were five scenarios across two agents, not five fresh host sessions or a probabilistic automatic-selection benchmark. Technical connections were simulated in fixture instructions. No real user records, global configuration, messages, calendars, reminders, app installation, or live integrations were changed. No live Obsidian registration, CLI behavior, sync, backup, or actual scheduler delivery was tested. A local retrieval pass is not a new-task host continuity test. The no-storage branch and agent-led recovery from an interrupted technical setup were reviewed but not forward-tested; the unit test verifies partial files are preserved, not that every repair succeeds.

Onboarding completion in the goal cases means a first useful artifact, saved next step, and return instructions were delivered. It does not imply user acceptance, physical action, or goal completion. The new user's preference choice remains genuinely open.
