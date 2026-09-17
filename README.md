# Steward

![Steward. A little less to carry. A winding path through a sunlit landscape.](assets/steward-cover.png)

Some days you have a clear goal. Some days you have a half-finished plan, a crowded week, and a few things you keep meaning to do. Bring either.

Steward gives your AI agent a practical way to help: **check in, make progress, adjust**. It can turn an intention into a plan, help with the next action, and save enough context to pick up later. Your memory lives in readable files. Your apps join in when you choose.

## Find your starting point

| If you want to… | Read |
|---|---|
| Install Steward and connect your memory | [Get set up](docs/install.md) |
| Know what the first conversation feels like | [Your first conversation](docs/first-use.md) |
| Use it day to day, or choose a specific skill | [Using Steward](docs/using-steward.md) |

You can speak normally. Steward selects the supporting skills for your request; their names are available when you want to choose one directly.

> “Help me make room for exercise this week.”
>
> “Find the commitment I made in that email and help me follow through.”
>
> “That plan didn’t survive Tuesday. Let’s adjust it.”

## Start with one sentence

Already installed? Say:

> **Use Steward to help me get started or pick up where I left off.**

In the app, type **@** and select **Steward**. In Codex CLI or the IDE extension, use **`$steward`**. You can also ask in plain language, as above. [Invocation guidance](https://learn.chatgpt.com/docs/build-skills)

Steward walks you through setup, recommends Obsidian for a readable personal wiki, and connects the sources you choose. It then reviews that context and offers a few things it could help with. You can also start with an area of life and work toward a goal, a routine, or a more manageable week. You can skip the tour. A small task stays small.

**Installing for the first time?** Send your AI agent the repository link and say:

> **Install Steward from https://github.com/malikhense/steward**

The agent follows the [installation instructions](INSTALL.md), checks your host, installs the complete suite, and verifies it. It handles the technical steps it has access to. The public repository can be read without a GitHub account. Host permissions may still need you. [Get set up →](docs/install.md)

## A loop you can come back to

| | What happens |
|---|---|
| **Check in** | Bring a request, tell Steward what changed, or ask “What next?” It recovers the relevant context and helps you choose a direction. |
| **Make progress** | Define an outcome, build a feasible plan, draft a reply, finish an administrative task, or make an authorized app change. |
| **Adjust** | Check what actually happened, change what no longer fits, and leave a clear next step for next time. |

You can start with work, health, relationships, home, learning, or your own category. Areas organize the conversation; they are not another scorecard to maintain. Goals can pause, change, or end.

## Bring the context that helps

Onboarding offers these connections together. Choose any combination, or skip them all.

| App | What it can contribute |
|---|---|
| **Calendar** | Real availability and existing commitments |
| **Reminders** | Open tasks and recorded completion |
| **Notes** | Plans and reference material you already keep |
| **Contacts** | The right person and contact details |
| **Mail** | Relevant decisions, requests, and commitments |
| **Messages** | Conversation context when a task calls for it |

Selected apps are checked individually. Steward remembers what you chose, what worked, and what still needs a permission or account step. It uses relevant context for the task at hand; it does not read every app at every check-in. Connections can be changed later.

Calendar, Reminders, and Notes have local Mac helpers. Mail, Messages, Contacts, and advanced features use the host's app-control tools when available. Finder and Shortcuts can help with documents and reusable actions. [See exactly what is supported →](skills/steward-apple/references/capabilities.md)

## Memory you can open

Use a plain Markdown folder or an existing **Obsidian** vault. Obsidian is optional. Steward saves useful decisions, current work, and next steps while keeping separate goals separate. You can inspect or edit those files yourself.

You can also try Steward without saving. It will give you a continuation note to bring to the next conversation; automatic cross-task recall needs a configured store.

Local memory does not mean the AI runs locally. Retrieved information is processed by your agent under that host's settings and policies. [Privacy and permissions →](docs/privacy.md)

## Helpful, with boundaries

- **Private writes by default.** Shared and unknown app destinations stay read-only until the relevant boundary is explicitly changed.
- **Permission for consequential actions.** Connecting an app is not permission to send messages, share information, spend money, or delete unrelated content.
- **Evidence before “done.”** A draft is a draft. A saved alarm is not proof it rang. Changes are checked, and uncertain results stay uncertain.
- **Your pace.** Optional connections can stay unfinished while useful work continues. No background watcher or recurring check-in is created merely by installing Steward.

The core Apple helpers have passed disposable live tests on one Mac. Broader app-control routes have instructions, not a promise that every Apple feature is automated or tested. [Validation and known limits →](docs/product-validation.md)

## Under the hood

Steward is a versioned skill suite, with one product entry and focused specialists for goals, planning, routines, decisions, scheduling, correspondence, review, and memory. Use Steward to begin; the supporting commands all use the `steward-` prefix.

- [Your first conversation](docs/first-use.md)
- [Everyday use and the skill map](docs/using-steward.md)
- [What each skill owns](docs/boundaries.md)
- [How the product was shaped by real examples](docs/product-packaging-research.md)
- [What shaped these guides](docs/guide-design-research.md)
- [Release notes](CHANGELOG.md)

For contributors:

```sh
python3 scripts/check.py
python3 -m unittest discover -s tests -v
node tests/test_notes_mock.js
```

Build a self-contained plugin folder and archive with `python3 scripts/package.py --out /path/to/new-output`. The archive contains source, skills, documentation, and checks. It excludes personal memory, account state, or credentials. Installation copies are updated deliberately rather than silently following repository edits.

Steward is an early personal project, shared under the [MIT license](LICENSE). Try it, adapt it, and keep what helps. The [validation notes](docs/product-validation.md) describe what has actually been checked.
