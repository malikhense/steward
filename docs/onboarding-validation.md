# Onboarding validation, 0.3.0

Tested on 2026-09-16. Personal conversations and vault contents are not included. Behavioral trials used isolated synthetic fixtures, not real accounts.

## Regressions reproduced before fixes

The previous scaffolder failed new tests for navigable wiki indexes and additive adoption of an existing vault. The connection helper rejected app-control evidence for Calendar after a native failure. The Apple helper described a compilation failure as an uncertain app operation even though no operation had started. Those cases pass after the changes.

An independent baseline trial also found that the previous instructions already required current context reads. This update does not claim that rule was absent. It makes novice orientation and the initial review explicit in the onboarding path, with observable completion criteria and coverage records. Compliance with instructions can still vary by host and model.

## Deterministic checks

Run from the repository:

```sh
python3 scripts/check.py
python3 -m unittest discover -s tests
node tests/test_notes_mock.js
```

31 Python tests cover installation, packages, source preservation, wiki creation, legacy scaffold upgrades, connection choices, fallback evidence, request validation, and pre-execution error state. The Notes mock checks preview/operation gates without accessing Apple apps. The checker validates 16 skills and their portable references.

New setup checks verify linked wiki sections, preview with no writes, preserved human Home/AGENTS files, nested symlink rejection, and repeatable additive upgrade of the original three-file scaffold. The fallback test seeds a compiler failure through a mocked probe and checks that recorded UI evidence retains the native failure without certifying writes.

## Independent forward trials

Separate evaluating agents received the revised skills, realistic user requests, and minimal raw fixtures. They executed local helpers and created real local records in isolated temporary folders. App reads and actions were explicitly simulated. These are bounded behavior trials, not a statistical reliability claim.

| Case | Observed behavior |
|---|---|
| Novice with no memory, Obsidian installed | Explains the product and setup path; creates the wiki, preserves app-registration and retrieval limits. |
| Six selected sources | Reviews synthetic content across sources, records coverage, proposes a due-soon reimbursement rather than treating an old trip note as the top priority. |
| Chosen reimbursement | Produces a local claim draft and linked return state; leaves missing receipt facts and ambiguous reminder time unresolved instead of inventing them. |
| Calendar/Reminders SDK mismatch | Records actual helper state using simulated app-control observations, retains the native compiler failure, and distinguishes reading from write support. |
| Installed Finances without callable tools | Checks available alternatives, avoids another mention/restart promise, and requests one useful export rather than a full intake questionnaire. |
| Health focus, debt concern, newer phone update | Preserves the chosen focus, corrects the stale trip action, and offers a bounded reimbursement detour without inventing financial urgency. |

The initial novice run read back 15 files and checked 34 local links without broken targets. After the fixture supplied the missing receipt fields and clarified 10 a.m., the evaluator completed the local claim and simulated a private reminder with a matching separate readback. It verified 10 changed files and 37 links. The claim was not submitted and no real reminder was created.

A system `/tmp` alias was rejected by the conservative symlink check; resolving the inspected alias to `/private/tmp` allowed the isolated trial. No actual Obsidian registration or fresh-host task was exercised.

## Limits

The trials do not establish real app access, notification delivery, account authentication, or universal compatibility. A skill cannot expose tools that a host does not supply or repair a remote Mac's developer tools. `record-ui` records the agent's evidence; it cannot independently prove that the observation occurred. The host must still perform and verify each actual read or write, honor source scope, and preserve the user's action boundaries.

A real novice trial on another machine remains valuable. Update the existing installation, preserve its vault, and resume from the saved step. Treat any new failure as evidence for a targeted correction rather than certifying onboarding from these fixtures alone.
