---
name: steward-schedule
description: Schedule personal work, resolve calendar clashes or disruptions, and manage requested reminders or follow-ups. Use steward-plan when the work itself needs definition.
---

# Shape the schedule

Read [working context](../steward-memory/references/working-context.md) and [actions](../steward-admin/references/actions.md), including mode, scheduling, and verification. This skill owns time placement and calendar reconciliation.

1. Retrieve the relevant plans, routines, actual calendar, timezone, anchors, and current availability. Identify dates explicitly when relative language could be ambiguous. Treat saved calendar summaries as observations requiring appropriate freshness checks. Completion: constraints reflect the current day or period, including travel, preparation, recovery, shared responsibilities, and flexible capacity.
2. Fit the requested work from today's baseline. Resolve collisions by tracing parent goals and commitments; use [focus](../steward-focus/SKILL.md) if the tradeoff needs a priority choice. Include a feasible minimum or deferral when capacity is insufficient. Completion: durations and dependencies reconcile, and the schedule leaves useful slack.
3. Inspect existing live items before writing. Preserve unrelated appointments; modify matching items instead of duplicating them. Respect the user's actual calendar and inspect relevant native/browser capabilities after a connector miss. In prototype, create a local preview or importable artifact. In authorized active work, apply the exact scoped changes and verify their identifiers or resulting state. Completion: each item is labeled proposed, prepared, verified, failed, or uncertain.
4. For recurring check-ins or monitoring explicitly requested by the user, use the host scheduler with scope, cadence, useful trigger, and stop condition. Verify creation; surface existing matching automations to avoid duplicates. Completion: promised future behavior has a verified mechanism, or the limitation and prepared alternative are clear.
5. Save verified identifiers, plan links, and pending changes via [memory](../steward-memory/SKILL.md). Present a compact local-time timeline. Completion: stored state agrees with what was actually scheduled; an import file is never reported as a live event.

For local Apple Calendar or Reminders access, use [Steward Apple](../steward-apple/SKILL.md).
