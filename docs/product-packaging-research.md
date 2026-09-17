# Steward product packaging: patterns worth adapting

Research date: 2026-09-16. Scope: the public README, first use, optional app connections, and return experience for an agent skill suite with durable personal memory. These are design recommendations from first-party examples, not evidence that Steward has achieved another product's outcomes. Source pages were read directly; authenticated onboarding and live app behavior were not tested.

The strongest direction is to present one useful relationship: bring a request, make progress, and keep enough context to return. Show the real first result before the skill catalog. Make memory understandable as files and app connections understandable as specific capabilities. Preserve **Check in → Make progress → Adjust** as the recognizable loop, with short requests allowed to go directly to work.

## Five exemplars and their implications

| Exemplar | Observed pattern | Adaptation for Steward | Limit of the comparison |
|---|---|---|---|
| **Sunsama: setup that teaches through real work** | Its first-use guide asks which task tools people use, connects those tools later during planning, and distinguishes first-use planning from the normal daily ritual. Its planning basics move from choosing work to considering what can wait and finalizing a feasible plan. [Account setup](https://help.sunsama.com/docs/getting-started/setting-up-your-account/), [daily planning](https://help.sunsama.com/docs/getting-started/basics/daily-planning-the-basics/) | Offer a small connection menu early, then finish one actual request. Reuse the same vocabulary on return. Make “What can wait?” available when commitments exceed capacity. Save setup progress separately from the user's work. | Sunsama requires completion of onboarding before workspace access. Steward should retain direct requests and allow optional connections to remain unfinished. A skill suite also cannot inherit Sunsama's reminders or background behavior. |
| **Obsidian: a concrete explanation of ownership** | A vault is a folder containing plain Markdown files, editable with other tools. Its documentation describes application settings separately from note contents. [How Obsidian stores data](https://help.obsidian.md/Files+and+folders/How+Obsidian+stores+data) | Say “Your saved context lives in a folder of Markdown files.” Offer an existing folder first, then a new folder; using Obsidian is an optional way to view those files. Show the selected location and verify a useful save and retrieval. | Local files do not establish that an AI host processes data locally, or that sync and backup are configured. Avoid “everything stays on your device” unless the actual host and every connection justify it. |
| **Things: approachable concepts with detail on demand** | The product introduction names everyday outcomes before implementation. The features page explains that optional to-do fields stay tucked away and gives small checklists a place without requiring a project. [Introduction](https://culturedcode.com/things/), [features](https://culturedcode.com/things/features/) | Lead with examples such as choosing a priority, drafting a reply, or making a plan. Put fourteen technical entry names in a reference section. Keep a small request small; introduce goal structure only when useful. | Things' speed promises, awards, testimonials, and polished native interface are evidence about Things. They provide no support for equivalent Steward claims. Adapt the information hierarchy and concrete language, not the superlatives. |
| **GitHub CLI: separate installation, connection, and evidence** | Its README explains what the tool does and links installation separately from usage. Login and status have distinct commands; status tests known accounts and reports the active one. [README](https://github.com/cli/cli), [login](https://cli.github.com/manual/gh_auth_login), [status](https://cli.github.com/manual/gh_auth_status) | Give newcomers a short installation request and returning users a direct start prompt. Report “installed,” “memory verified,” and “Calendar access checked” separately. A saved selection is not a successful connection. Route technical depth to linked guides. | A command-line status check does not prove every app action works. For Steward, reading a calendar, writing an event, and verifying its fields need separate evidence. |
| **Apple: permissions tied to a capability and a reversal path** | Apple explains why a calendar-consuming app might ask for access, distinguishes full calendar access from permission to add events, and shows where access can be changed. Automation permission is another category. [Calendar access](https://support.apple.com/guide/mac-help/control-access-to-your-calendars-on-mac-mh43710/mac), [app automation](https://support.apple.com/en-euro/guide/mac-help/mchl108e1718/mac) | At connection time, name the app, purpose, access being requested, and the next manual step if one is required. Separate what can be read from approved write destinations. Explain how to revisit access. | macOS permission can be broader than the selected Steward destination. Selecting a private calendar in Steward does not narrow the operating system's permission. Account sharing and action authorization remain separate concerns. |

## Recommended first-use and return experience

The following is a proposed presentation of the suite's existing setup and session concepts. It is not a report of a completed implementation or usability test. Current behavior is defined in [setup](../skills/steward-session/references/setup.md), [session state](../skills/steward-session/references/session-state.md), and [Apple connection](../skills/steward-apple/references/connection.md).

1. **Recover before asking.** Inspect trusted configuration and the saved session record. If memory is already connected, identify it briefly and continue from the actual pending step. Do not treat a new conversation as a new person.
2. **Offer the unresolved choices together.** A new user should see memory and optional app choices before being sent through any lengthy personal questionnaire. The presentation can be one compact menu, while connection work proceeds one dependency at a time.
3. **Connect for the requested purpose.** An app choice records intent. Discover the available route, explain any needed access, complete authorized work, and verify the result. Mark missing permissions as pending while finishing independent work.
4. **Deliver something useful.** Use the user's existing request. When there is none, offer a small editable menu of life areas or practical requests. Orientation can end after one useful result; it need not inventory a whole life.
5. **Leave a clear return point.** Save the current focus, concrete next action, relevant constraints, and exact unresolved connection step. On return, check what happened before changing statuses.

Suggested connection menu:

| Choice | What the person should understand |
|---|---|
| Use my existing memory folder | Reuse the existing structure and context after inspection. |
| Create a Markdown folder | Save readable files in a selected location. Obsidian can be added later. |
| Use a folder with Obsidian | File access and opening the folder in Obsidian are checked separately. |
| Try it without saving | Continue now; carry a continuation note into the next conversation. |
| Connect Apple apps on this Mac | Choose Calendar, Reminders, Notes, or a needed app-control task. Report availability and permissions per app. |
| Skip app connections for now | Keep working with conversation and available files. |

Use observed states in the completion message. For example, after the relevant checks: “Memory is ready in your selected folder. Calendar can be read; choosing a private calendar for new events is still pending. Your draft plan is saved, and the next step is to choose a time.” This is synthetic copy illustrating the distinction, not a record of a test.

## README and copy recommendations

Put the README in the order a newcomer needs: what Steward helps with, three ordinary request examples, a start route, the loop, memory and optional connections, then the technical catalog and contributor documentation. Keep an already-installed path adjacent to installation. Use links for detailed host requirements, Apple limitations, and validation evidence.

Suggested opening, subject to checking against the final implementation:

> **Steward helps you turn personal goals and everyday responsibilities into useful next steps.** Work with it through your coding agent: choose what matters, make a plan, draft a message, or handle a practical task. With a connected memory folder, Steward can save the decisions and context needed to pick up later.
>
> **Check in → Make progress → Adjust**

Useful example requests:

- “I have too many things competing for this week. Help me choose what matters.”
- “Help me write a reply to this message.”
- “Pick up my walking plan and adjust it around what actually happened.”

Suggested installed-suite prompt:

> Use $steward-session to get Steward ready. Reuse any existing memory, show me the available memory and optional app connections, and help me finish one useful request. If setup is unfinished, resume where I left off.

Suggested connection copy:

> Connect the apps that help with the work you want to do. Steward checks access and available actions separately for each app. You can start with memory alone and add Apple apps later on a Mac.

Warmth should come from reducing repeated explanation and giving a clear next step. Avoid simulated intimacy, invented user quotes, guaranteed outcomes, “knows everything about you,” or an implied always-on assistant. A saved plan is preparation; a completed real-world activity needs evidence from the user or an appropriate source. “Ready” should name the capability that was actually verified.

## What remains to validate

These patterns are informed design choices, not causal claims about conversion or retention. Test the final experience with a new user, a returning user, an existing vault, a skipped onboarding, interrupted Apple permissions, and a no-storage session. Check whether each person can explain where context is saved, what an app connection permits, what was actually completed, and how to return. Do not publish a setup-time promise until measured on representative supported hosts.

Only this research note was added by this research pass. No runtime behavior, personal memory, app permissions, or external accounts were changed.
