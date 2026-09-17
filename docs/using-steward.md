# Using Steward

[Get set up](install.md) · [First conversation](first-use.md) · **Everyday use**

**Bring what’s on your mind. Leave with a useful next step. Come back with what happened.**

You can talk normally: “My week changed,” “Help me decide,” or “Let’s pick up that plan.” Steward selects the relevant skills and carries the work forward in the same conversation. You can also select a named skill directly when you know what you want.

## The loop

| Moment | What you might say | What Steward does |
|---|---|---|
| **Check in** | “What deserves my attention this week?” | Recovers relevant context and helps choose a focus. |
| **Make progress** | “Help me make room for two reading sessions.” | Builds a workable plan and completes the authorized parts. |
| **Adjust** | “I managed one session; the other evening got busy.” | Uses what actually happened to revise the plan and save the next step. |

The loop can fit one conversation or stretch across weeks. Return whenever you need it. A recurring review or reminder is created only if you ask and a scheduler is actually configured.

A longer goal might move through **focus → goals → plan → routines or schedule → review**, then back to the part that needs attention. Those are useful skill boundaries, not compulsory stages. A reply can go straight to messages. A changed appointment can go straight to schedule. Starting another goal does not erase existing work.

## Choose a skill when you want to

In the app, type **@** and select the skill. In Codex CLI or the IDE extension, use **$** followed by its exact name. Plain-language requests can also select a skill through its description. [Official invocation guidance](https://learn.chatgpt.com/docs/build-skills).

### Check in

| Skill | Use it for | Example |
|---|---|---|
| `steward` | The simplest way to start or return | “Help me get started.” |
| `steward-session` | Guided setup, onboarding, or a check-in | “Pick up where we left off.” |
| `steward-focus` | Choosing priorities or exploring an area | “Too many things need my attention.” |
| `steward-goals` | Defining, changing, pausing, or finishing a goal | “I want to make this a goal.” |

### Make progress

| Skill | Use it for | Example |
|---|---|---|
| `steward-plan` | A feasible path and usable materials | “Turn this goal into a plan.” |
| `steward-routines` | Repeated behavior and habits | “Make my evening routine easier.” |
| `steward-schedule` | Time, calendar changes, requested reminders | “Fit this around next week’s commitments.” |
| `steward-decide` | A choice with evidence and tradeoffs | “Help me choose between these options.” |
| `steward-admin` | A chosen practical task | “Help me complete this form.” |
| `steward-messages` | Correspondence in your voice | “Help me draft this reply.” |
| `steward-opportunities` | Worthwhile improvements when requested | “Find ways to reduce my recurring admin.” |

### Adjust

| Skill | Use it for | Example |
|---|---|---|
| `steward-review` | Learning from actual progress and friction | “This plan keeps slipping. Let’s adjust it.” |
| `steward-experiments` | Testing a particular uncertainty | “Help me compare two practice times.” |

### Support across the loop

| Skill | Use it for | Example |
|---|---|---|
| `steward-memory` | Recall, durable notes, and corrected facts | “Remember this preference.” |
| `steward-maintain` | Memory setup, repair, migration, or forgetting | “Help me move my memory folder.” |
| `steward-apple` | Supported Apple app actions and access | “Show which apps Steward can use.” |

## Useful things to say

- **Change direction:** “Pause that goal. I want to focus on something else.”
- **Correct context:** “That schedule is out of date. Here’s the new one.”
- **Stay with a draft:** “Plan it here without changing my calendar.”
- **Change connections:** “Stop using Messages for context.” This stops Steward’s context use; revoking macOS access or forgetting saved facts is separate.
- **Resume:** “Continue my reading plan.” Use the workspace connected to your memory folder. In a no-storage trial, bring the continuation note.

You should not need to choose a skill to resolve an internal handoff. If a result needs another specialist, Steward reads that skill and continues. If skill discovery fails, explicitly selecting Steward is a useful fallback, not a required step in every conversation.

For capability limits and how your information is handled, see [Apple support](../skills/steward-apple/references/capabilities.md) and [privacy](privacy.md).
