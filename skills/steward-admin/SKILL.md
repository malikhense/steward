---
name: steward-admin
description: "Complete personal administration: forms, bookings, shopping, returns, bills, cancellations, or service coordination. Use steward-decide for choosing and steward-schedule for calendar placement."
---

# Handle administration

Read [working context](../steward-memory/references/working-context.md) and [actions](references/actions.md). This skill owns practical completion and verified external state.

1. Identify the requested result, current state, relevant account or service, exact scope, and existing authorization. Inspect available context and capability routes before asking for information. Completion: the target and permitted actions are unambiguous; outstanding prerequisites are specific.
2. Prepare the concrete action: form fields, exact products and quantities, appointment details, cancellation terms, return evidence, or service instructions. Use [decisions](../steward-decide/SKILL.md) only for a material unresolved choice; use [messages](../steward-messages/SKILL.md) when correspondence is part of the work. For shopping or budgets apply [planning criteria](../steward-plan/references/planning-deliverables.md). Completion: reasonable research, calculations, and preparation are finished before any required final approval.
3. Execute through the best relevant available capability within authorization and mode. Complete useful independent work if a branch is blocked. Check the destination before retrying an uncertain consequential action. Completion: each action has a verified result or an honest failed/uncertain state, with no false completion or duplicate transaction.
4. Resolve dependent follow-through: save receipts, provide exact next physical steps, reconcile affected plans, and use [scheduling](../steward-schedule/SKILL.md) for requested reminders or appointments. Check a concrete adjacent opportunity through [opportunities](../steward-opportunities/SKILL.md) when relevant, such as combining errands. Completion: the task is usable in practice and not left at a list of things the agent could do.
5. Save only useful decision and action records through [memory](../steward-memory/SKILL.md), avoiding secrets and unnecessary account data. Completion: verified identifiers, terms, and remaining steps can be recovered without treating an old observation as current live truth.
