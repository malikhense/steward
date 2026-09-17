# Choose connections, then prove access

Reach this branch during first onboarding, a request to connect/change/disconnect apps, or a task that needs a missing source. Use [the connection helper](../scripts/connections.py) with the actual memory folder; inspect `--help` and `catalog`. It stores choices and observed access in `System/Connections.json`, outside the skill repository. In a no-storage trial, keep equivalent state in the portable continuation note and explain that it will not persist automatically.

## Offer the choice

Recover existing choices first. First inspect current host tools and discover relevant supported connectors. Include non-Apple options the host can actually expose, such as a finance or task service; record those choices, scope, route, and observed access in System/Context.md rather than inventing an Apple helper identifier. An installed plugin without callable tools is not connected. For a new user on a Mac, offer Calendar, Reminders, Notes, Contacts, Mail, and Messages together in one short question. Explain the benefit before any permission prompt:

- Calendar and Reminders ground plans in real availability and tasks.
- Notes provides selected plans and reference material.
- Contacts, Mail, and Messages provide relevant people, conversations, and commitments.

Offer “Calendar + Reminders,” “Choose apps,” “All six,” and “Skip for now” where the host allows that many options; otherwise ask a concise free-text question listing the apps. The user can choose any subset. Before the choice, explain that selected sources will support an initial review of upcoming commitments, open tasks, and recent relevant material, followed by scoped use for later requests. “All six” selects that explained review and ongoing relevant context use; it does not authorize unrestricted historical collection or sending. Finder folders and Shortcuts are optional additions when relevant. On other hosts, discover equivalent available connectors rather than offering unusable Apple access. The product remains usable with memory alone.

Record selected and skipped apps with the helper. Preserve a previous opt-out; do not repeat the menu every session or automatically select an app merely because macOS permission is already granted. A direct request to use a skipped app authorizes that scoped task; clarify only whether the user also wants a persistent choice changed. It does not erase their general preference.

## Connect chosen apps

1. For Calendar, Reminders, and Notes, use `probe` on each selected app. The helper calls the actual local connector, requests permission if needed, and saves verified discovery or a specific blocked result. If a probe fails, retain its error and use the recovery branch below rather than ending setup at the error. For private write targets, use [Apple setup](../../steward-apple/references/connection.md); read verification does not enable or certify writes.
2. For Contacts, Mail, and Messages, read [native workflows](../../steward-apple/references/native-apps.md). Use the actual host app-control tool to verify that the intended account/interface and relevant content can be read. An installed app or an empty welcome/login screen is not connected account access. Record the observation using `record-ui`, with no private message contents in its evidence. Distinguish blocked permission, unavailable host/app, and verified reading. Test sends are never part of onboarding.
3. Confirm source scope only when it changes privacy or usefulness: relevant calendars, notes folders, mail accounts, conversation boundaries, or exclusions. Store it in the registry. Use private writes by default; shared/unknown destinations remain read-only. Offer requested write tests separately with their exact effects; never create disposable containers just to mark onboarding complete.
4. Perform the initial content review through [connected context](../../steward-memory/references/connected-context.md), then show a compact result: which sources can provide context, which are skipped, and which need a specific step. Continue a first useful task while optional apps remain pending. State actual verification time and route rather than promising permanent access.

Example helper calls from the skill directory (resolve the actual vault first):

```sh
python3 scripts/connections.py --vault "$VAULT" --apply select --apps calendar reminders --scope "Relevant planning context; shared calendars read-only"
python3 scripts/connections.py --vault "$VAULT" --apply probe --app calendar
python3 scripts/connections.py --vault "$VAULT" status
```

Use argument arrays or safe shell quoting for paths and user scope text. `record-ui` records evidence supplied by the agent after an actual observation; it is not an automatic access test. `status` is a saved-state view, not a fresh probe.

## Resume, change, and disconnect

The registry distinguishes not-offered, selected, skipped, and disconnected choices from unverified, verified, blocked, and unavailable access. Resume only selected unresolved apps. A previous successful check is evidence of past access, not a substitute for a current read when planning or editing. If access fails, record the failure and continue from saved context with its age made clear.

Use `disconnect` to stop Steward's future context use and clear saved connection metadata. This does not revoke macOS permissions, remove app data, or remove previously saved goal facts. Explain the distinction and, if the user wants operating-system revocation or forgetting, perform that separately through approved settings/maintenance. Do not silently change a global Mac permission because one workspace changed its context preferences.

## Recover a blocked connection

For a Calendar or Reminders compiler/SDK failure, the native helper is blocked, not necessarily the app. Inspect the actual host capabilities and try supported native app control or another verified read route within the selected scope. Record an actual successful app read with `record-ui`, including the route and scope; retain the native helper failure as a limitation. Metadata visibility alone is insufficient. A UI route can support reading without certifying every write feature. Never install or repair developer tools silently, and do not repeatedly run the same failed build.

When the host cannot control the app, give the exact next step supported by the observed error or current official instructions. If the remedy needs software repair, identify that as pending and offer a usable bounded fallback, such as importing an exported calendar or continuing the user's plan with its availability unknown. Avoid generic “repair later” handoffs. An unsupported external plugin follows [connected context](../../steward-memory/references/connected-context.md): actual tool discovery, verified alternative if available, then one clear fallback. Do not promise that mentioning a plugin or switching chats fixes missing tools.

Completed onboarding means the connection choice was offered and recorded (including skip), selected checks were attempted or explicitly deferred, the initial content review was completed or its limits/skips recorded, one useful result was produced, and the next step was saved. It does not require every optional app to connect.
