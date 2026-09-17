# Connect and recover

Requirements: macOS 14+, Python 3, and a working Apple Swift compiler (Command Line Tools or Xcode). Run `python3 scripts/apple.py --build` from this skill directory. The helper caches a local binary under `~/Library/Caches/Steward/apple`; source changes trigger compilation. Notes uses the installed Notes scripting interface. No separate cloud service is required; existing Apple account synchronization still applies.

Send JSON on stdin to `python3 scripts/apple.py`. `{"op":"status"}` checks Calendar/Reminders authorization without prompting. `{"op":"connect","app":"calendar"}` requests Calendar access and lists containers. Repeat for `reminders` and `notes` when requested. macOS may show a permission prompt; follow the host's approval flow. If denied, explain the relevant Privacy & Security setting. The requester can appear under the host's name. Do not reset or edit privacy databases. Shell sandbox failures need the host's normal escalation mechanism.

Connection returns IDs, names, sources, and available metadata. It does not imply verified write access. Save personal choices in memory, not in the skill repository. Read all calendars relevant to availability, separately from choosing a write target. Do not silently route all activity into a single default when the user wants topic-based calendars.

## Private-container policy

Native writes fail closed without `~/Library/Application Support/Steward/apple-policy.json`. During authorized setup, create this local JSON after inspecting app sharing status:

```json
{
  "allowContainerCreation": true,
  "calendar": {
    "DISCOVERED_PRIVATE_ID": {"name":"Personal","write":true,"privateVerifiedAt":"2026-09-16T17:00:00Z"},
    "DISCOVERED_SHARED_ID": {"name":"Shared","write":false}
  },
  "reminders": {},
  "notes": {}
}
```

Each app maps discovered IDs to entries. Missing IDs and `write:false` block writes. `allowContainerCreation` permits the connector to execute requested creation; it is not blanket action authorization. Preserve existing policy entries; use an atomic file replacement and restrict its permissions to the local user. Shared destinations remain blocked unless the user explicitly changes that boundary after reviewing the audience and intended content.

EventKit exposes writability, not sufficient sharing information. Inspect Calendar's shared indicators and Reminders' “Shared”/“Manage Shared List” indicators through app control. Refresh an already authorized private entry's `privateVerifiedAt` only after this observation. Verification expires after 15 minutes; this bounds stale checks but is not a continuous monitor or protection against a sharing change between inspection and write. Never refresh from a saved assumption. Notes exposes live folder/note sharing; its entries need `write:true`, and every mutation additionally checks sharing. Newly created containers are private and are recorded by the connector.

If the host cannot inspect sharing, keep writes blocked and prepare the requested changes. Broad read access does not authorize shared writes, and bypassing the connector through UI or another script does not bypass the user's boundary.

## Requests

Use `--help` for the current field list. Supply JSON via a file/stdin or subprocess input; user prose must not become shell code. Writes return a local preview unless `--apply` is supplied.

```json
{"op":"list","app":"calendar","calendar":"ID","start":"2026-09-16T00:00:00-07:00","end":"2026-09-23T00:00:00-07:00"}
```

```json
{"op":"create","app":"reminders","calendar":"ID","token":"GENERATE_UUID","fields":{"title":"Prepare walking shoes","due":"2026-09-17T08:00:00-07:00","remindAt":"2026-09-17T07:45:00-07:00"}}
```

```json
{"op":"update","app":"reminders","calendar":"ID","id":"ITEM_ID","fields":{"completed":true}}
```

```json
{"op":"create","app":"notes","calendar":"FOLDER_ID","token":"GENERATE_UUID","fields":{"title":"Walking plan","text":"Bring water."}}
```

Calendar create requires title/start/end. `alertMinutesBefore` sets one relative alert; null removes alarms. Reminder `remindAt` sets one absolute alert; null clears it. Due times and alarms are distinct. Notes `appendText` preserves existing simple content; every Notes update requires `expectedModified` from the last `get`. Get/delete target the app/container/item IDs. Container creation uses `source` from discovery and `name`; renaming/deleting use `calendar`, with `name` for renaming. Container deletion refuses nonempty containers.

## Verification and limits

After setup, verify authorized writes with disposable items, record IDs before continuing, and resume cleanup by IDs after interruption. Container creation/deletion tests need explicit approval for that scope. Verify fields with a fresh get; do not count a preview, compile, or read as a successful write. Record the actual tested routes and limits.

- Calendar recurrence reads are expanded; recurring/invited writes and recurring-reminder writes use the app-control route with explicit scope.
- Notes update timestamps detect stale reads but the scripting API has no atomic compare-and-swap; avoid concurrent edits to the same note during a write.
- Notes rich content and locked/shared notes stop before editing. Locked content is not bypassed. Shared destinations remain read-only under the private-only policy.
- Tokens help recover identical creates. A moved event or changed marker can defeat destination matching; inspect before retrying and keep the original payload/token. Never generate a fresh token to recover an uncertain attempt.
- Identifier changes after account migration require rediscovery and reconciliation.
- All-day events require local-midnight boundaries and an exclusive end. Reminder date-only values and advanced alert types use app control.
- Notification configuration is verified by reading saved alarms, not by claiming notification delivery. Focus/device settings can affect display.
- Rebuilding an unsigned helper or changing execution hosts may require macOS access again. This is a local integration, not a signed distributable app.
