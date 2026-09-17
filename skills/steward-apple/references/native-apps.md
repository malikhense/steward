# Native app workflows

Use the host's computer-control tool and its documented APIs. Inspect the current interface after actions and use visible identifiers, recipients, dates, and status. Only operate the app relevant to the requested work. macOS prompts must follow the host's permission process; do not modify privacy databases. If computer control is unavailable or the Mac is locked, finish local preparation and state the missing access.

## Calendar, Reminders, and Notes extensions

Use the connector for supported operations; reach app control for features identified in the capability table. The private-container policy applies to both routes. Inspect the destination's sharing status before writing. If the UI hides or ambiguously labels sharing, stop before the write instead of assuming privacy. Recurrence edits must resolve occurrence/series scope; preserve unrelated instances. Distinguish reminder due dates from alert times and all-day events from timed events. Verify resulting dates and alerts in the app. For Notes, inspect the actual format and preserve tables, scans, attachments, and checklists when editing. A plain-text replacement is not a lossless rich-note edit.

## Mail and Messages

Use [correspondence](../../steward-messages/SKILL.md) for voice and recipient context. Open the specific account/conversation, inspect the exact recipient addresses/numbers and group membership, and retrieve only relevant context. Duplicate display names need disambiguation. Draft locally unless creating an in-app draft is requested or within the authorized workflow.

Before sending, reconcile recipient(s), account, subject/body, attachments, and reply/reply-all scope with the user's actual request. Connecting the app or testing access is not sending authorization. Do not send test messages. When sending is authorized, execute once and inspect the sent item/conversation; report “sent” separately from “delivered” or “read.” On uncertainty, inspect Sent/the conversation before retrying. Follow the host's action-time confirmation requirements for consequential communication.

Searching/reading, changing flags, moving mail, creating mailboxes, and composing replies are distinct outcomes; do not bundle destructive cleanup into an inbox summary. For Messages edits/unsends or group changes, inspect current UI availability and exact target rather than promising a time window or recipient-side effect.

## Contacts, Finder, and Shortcuts

Contacts: retrieve the specific person and exact channel needed; avoid exporting an address book for a single lookup. Edits can sync to other devices/accounts. Resolve account ownership before creating, merging, or removing contacts.

Finder: prefer filesystem tools for supported operations and app control for UI-only actions. Inspect paths and collision behavior, preserve unrelated files, and use recoverable Trash when deletion is requested. A local move does not establish cloud sync or change sharing permissions.

Shortcuts: discover with `shortcuts list`; inspect the selected shortcut's actions in the app before a first run. A shortcut may send messages, share data, delete files, or run scripts, so authorize its actual effects rather than treating a name as safe. Run via argument arrays or properly quoted names. Apple supports input/output paths; validate the resulting artifact or side effect. Creating a shortcut is not scheduling it.

For other Apple apps, inspect the actual host tools and app UI, then apply the requested scope and verification. Universal Apple feature coverage is not assumed.
