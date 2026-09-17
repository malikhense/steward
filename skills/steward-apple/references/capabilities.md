# Choose the actual route

| App | Direct connector | Native app control when needed |
|---|---|---|
| Calendar | Container discovery; recurring occurrence reads; individual event create/read/update/delete; times, all-day blocks, location, notes, one relative notification alarm; create/rename calendars; delete empty calendars | Recurrence creation/changes with explicit occurrence-versus-series scope; moving events; multiple/custom alerts; calendar appearance. Invitations/sharing require explicit recipient and content authorization. |
| Reminders | List discovery; read/create/update/complete/delete tasks; due time and one absolute notification alarm; priority; create/rename lists; delete empty lists | Recurring reminders, date-only dates, subtasks, sections, tags, smart lists, location alerts, attachments, and supported moves. |
| Notes | Folder/account discovery; note metadata and content reads; create/rename/delete notes; append or replace simple text; create/rename folders; delete empty folders; current shared/locked checks | Tables, checklists, attachments, scans, tags, smart folders, nested folders and moves. Rich content editing must preserve the existing note. |
| Mail | No connector operations in this version | Search and read scoped messages, draft/reply/forward, attachments, organize mailboxes, flag/read status, and authorized sends. |
| Messages | No connector operations in this version | Read/search relevant conversations, prepare and send authorized messages or attachments, and supported conversation actions. |
| Contacts | No connector operations in this version | Resolve exact people and contact channels; create/edit contacts when requested. |
| Finder | Host filesystem tools for authorized file work | Browse, organize, rename, move to Trash, inspect sync/sharing when relevant. |
| Shortcuts | Apple's `shortcuts list` and `shortcuts run` | Inspect/create/edit reusable shortcuts in the app; run only after understanding their actions. |

“Native app control” is an execution route, not a promise that every feature is available or already tested. Inspect the live interface and host capabilities for the requested operation. If the app or host cannot expose it, explain the specific limit and prepare the smallest useful handoff. Do not invent API support or silently replace the user's app.

Other useful optional apps: Preview for forms/PDFs, Maps for routes and travel estimates, Photos for selected images/albums, and Safari for web tasks. Load their actual tools or specialist skills only when the task needs them. Health/Watch-only data, Wallet, passwords, and iCloud account controls are not implicitly connected by this skill.

Apple references: [EventKit](https://developer.apple.com/documentation/eventkit), [Calendar scripting](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/CalendarScriptingGuide/), [Shortcuts CLI](https://support.apple.com/guide/shortcuts-mac/run-shortcuts-from-the-command-line-apd455c82f02/mac), [Messages](https://support.apple.com/guide/messages/icht35827/mac), [Mail](https://support.apple.com/guide/mail/mlhl5094a9f2/mac). Installed scripting dictionaries describe the actual local app versions; they do not grant permissions or establish end-to-end success.
