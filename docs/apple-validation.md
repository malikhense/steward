# Apple integration validation, 2026-09-16

## Evidence

- 14 Python tests passed: seven setup/install tests and seven Apple request-validation tests. Apple tests cover nonmutating previews, explicit-offset dates, bounded queries, all-day boundaries, exact IDs, unsupported fields, alarm payloads, stale-note requirements, and container inputs.
- A Node mock exercised all six native Notes mutation previews and unknown operations with app access configured to throw. All gates passed without accessing Apple apps.
- Structural check: 15 skills, 134 portable runtime references. New skill frontmatter validated with the host skill validator.
- Independent review found invalid all-day boundaries, inconsistent date parsing, malformed-token handling, missing reminder recurrence metadata, a native Notes preview gap, and silently ignored note content. These were corrected and covered by the local checks.
- With explicit user approval, live EventKit/JXA tests created one disposable calendar, reminder list, and Notes folder per successful test run. They created/read/updated/deleted items, retried identical creates without duplicates, renamed containers, refused nonempty container deletion, and removed empty containers. Calendar relative alarms and reminder absolute alarms were read back, then cleared. A fresh read verified item changes. Notes escaped text and timestamp-checked replacement were verified.
- Live shared-destination requests with nonexistent item IDs were refused by policy before item access or mutation.
- First Calendar container cleanup exposed a broken native scripting delete path on the host. The corrected route resolves the ID in EventKit, checks a unique native calendar is empty, and removes through EventKit. The successful rerun covered this route. No disposable containers remained after final discovery.
- Installed source was verified byte-for-byte. Personal IDs, policy, notes, and test traces remain outside this repository.

## Limits

Tests ran on one Mac, not every macOS/device/account combination. No real user event, reminder, or note was changed; disposable notes may remain in the apps' normal Recently Deleted recovery area. No Mail or Messages send was tested or performed. Contacts, Finder, Shortcuts, and advanced native app-control workflows have guidance, not end-to-end certification. Calendar recurrence uses EventKit's occurrence predicate, but recurrence creation/editing is an app-control route. Notification alarm storage was verified, not actual notification presentation. No background monitoring, universal Apple feature support, signed app distribution, or zero-error guarantee is claimed.

Calendar/Reminders sharing is inspected through current app UI; a local policy expires private verification after 15 minutes. This is not continuous detection of sharing changes. Notes checks exposed sharing flags on each mutation. Notes scripting has no atomic compare-and-swap, so modification checks reduce rather than eliminate concurrent-edit races. Container deletion is empty-only, and API item operations refuse recurring/invited items rather than guessing their scope.
