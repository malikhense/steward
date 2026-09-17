# Product entry, onboarding, and a repeatable loop

Status: researched proposal, 2026-09-16. This document changes no installed skill, starts no automation, and selects no product name. The existing skill suite implements specialist work; it lacks a coherent first-use and return experience.

## What excellence means here

Evaluate reference products against observable properties: one understandable starting point; a first useful result before extensive configuration; preservation of ongoing context; feasible action; adaptation from actual outcomes; recovery after interruption; and an explicit next step. These are proposed product criteria. The examples below demonstrate mechanisms, not comparative proof that any one system is universally best.

## Primary-source anchors

| Source | Observed mechanism | Proposed adaptation | Limit |
|---|---|---|---|
| [GTD fundamentals](https://gettingthingsdone.com/what-is-gtd/) | Capture, clarify, organize, reflect, and engage distinguish intake from action and review. | Accept an unstructured request, resolve its meaning, then support action and subsequent review. | A human productivity method; it does not specify agent routing or validate this new loop. |
| [Sunsama setup](https://help.sunsama.com/docs/getting-started/setting-up-your-account/) | Account/workspace configuration leads into a first guided planning session; settings remain adjustable. | Separate technical readiness from a first useful personal session. | Its mandatory first-use steps suit its product; this proposal allows skipping or resuming orientation. |
| [Sunsama daily planning](https://help.sunsama.com/docs/usage-guides/daily-planning/) | Guides reflection, task selection, workload checking, and plan finalization; planning can be re-entered when priorities change. | Recover current work, check capacity, and make returning easy. | Workday planning does not cover every personal request. Avoid requiring a full daily ritual for a small task. |
| [Sunsama weekly review](https://help.sunsama.com/docs/usage-guides/weekly-objectives/weekly-review/) | Reviews objectives and work completed; configured prompts support return. | Offer an optional review cadence that reconnects actions with intended outcomes. | Prompts require actual scheduler infrastructure and user choice. |
| [Bullet Journal migration](https://bulletjournal.com/pages/migration) | Periodically reconsiders which unfinished tasks merit carrying forward. | On return after a gap, reassess open work rather than accumulating overdue obligations. | Manual rewriting is specific to its medium; preserve reconsideration rather than copying its physical effort. |
| [PARA](https://fortelabs.com/blog/para/) | Distinguishes finite projects from continuing areas of responsibility and organizes information for current action. | Treat areas as navigation and context; show the current goal and next work in the daily view. | PARA is information organization, not a universal life-area taxonomy. |

## Recommended loop: Check in → Make progress → Adjust

This wording is a proposed synthesis, not a named method from a source or an empirically validated formulation.

**Check in:** The user can state a request, report a change, or say “What next?” The product retrieves relevant saved state and checks whether the request already supplies a clear direction. A known task proceeds directly. An ambiguous check-in offers a small set of grounded options or the smallest useful question. Exit: one selected request and the context needed to act.

**Make progress:** Invoke the specialist skills required by that request. Research, planning, usable deliverables, routines, and authorized execution belong here as needed. The agent finishes work it can do; physical participation and genuine user decisions remain with the person. Exit: a usable result, or exact open work with a supported reason.

**Adjust:** At a meaningful result or stopping point, verify what happened and save material context, status, and the next step. Later user observations may change the plan. Exit: saved state distinguishes prepared work from actual outcomes, and the next visit can resume without a transcript. A small request need not end with another questionnaire.

The loop can span sessions. A workout planned today is not completed today merely because the planning session ended. A simple draft can move through the loop in one response. A goal may require many passes. Direct specialist requests remain valid; the entry skill does not intercept unrelated coding, writing, or factual questions.

## Three separate experiences

| Experience | User-facing job | Completion |
|---|---|---|
| Installation and connection | Make the skills and durable memory usable on this host. | Installed entrypoints resolve; a selected store can be safely read/written; a saved record is retrievable. |
| Personal onboarding | Learn enough about the person's priorities and current circumstances to help. | One chosen focus or existing goal, a first useful result, and a demonstrated way to resume. |
| Ongoing sessions | Help with a request, continue work, or adjust from an outcome. | Requested work advances and relevant state/next work is saved. |

Installation is a bootstrap workflow: a skill cannot install itself before it is present. The repository needs a clear installation route plus a guided setup helper. Host capability differences, account authentication, and application installation are handled explicitly, with only the irreducible manual steps handed to the user.

Memory choices: reuse an existing compatible folder; create a plain Markdown folder; or register/use that folder with Obsidian. Obsidian is optional. A no-storage trial can produce a continuation note but must not claim cross-session durable memory. A missing integration should block only dependent work.

Personal onboarding should be separate and resumable. It can begin from an existing concrete goal or a sourced, editable area menu. It gathers decision-relevant context as needed, rather than requiring a complete life inventory. Technical setup success must not mark personal onboarding complete. Returning to the product must not silently restart either process.

## Life areas: sourced options, user-owned labels

The [life-area comparison](life-areas-research.md) examines SAMHSA, current Full Focus, Stanford Life Design, and OECD. Their purposes and category counts differ; the research establishes neither one optimal count nor a universal set. The note records retrieval limits, including indexed rather than fully retrieved text for two PDFs.

Recommend an optional nine-area synthesis: physical health; mental and emotional well-being; relationships and belonging; work and contribution; money; learning and growth; home and surroundings; play and rest; meaning and spirituality. This is a design proposal with source mappings, not a validated scale. Offer relationship, caregiving, civic, or safety refinements when useful. A user can start with their own goal without selecting from the menu, and can rename, merge, split, hide, or add areas.

An area can be maintained or simply enjoyed. It need not acquire an improvement goal. Onboarding should help the person recognize their situation, then reach one useful action. Test the menu's language and coverage in realistic onboarding before adopting it as the default.

## One entry skill, specialized work underneath

Add a thin session entry skill, with final name deferred. It owns recognizing setup/orientation/return state, guiding the current session, and handing substantive work to the existing owners. Technical memory operations remain owned by maintain; personal priority selection by focus; goal identity by goals; recall and writes by memory. The entry skill should link those instructions rather than repeat them.

Separate setup and personal-onboarding procedures can be disclosed references or independently invocable skills if their reach warrants it. Three distinct experiences do not automatically require three extra always-loaded descriptions. Decide packaging from realistic invocation cases, not a desired skill count.

This revises the earlier decision against an umbrella entry: the newly explicit need is a guided session experience. The entry owns that job; it is not a copy of all thirteen specialist workflows.

## Reduce remembering

A compact saved home view should show the current focus, proposed next action, pending user decisions, and anything that needs reconsideration. Normal phrases such as “continue,” “something changed,” or “help me with this” should enter the appropriate branch inside the configured product context.

When requested, connect a reminder to the user's preferred review cadence. The reminder should open a useful check-in, not demand maintenance of the system. When reminders are not requested, resumption occurs on the next interaction. A prompt file cannot make itself run in the background.

## Evidence and excellent examples

The installed research-quality reference already requires strong implementation examples for important decisions and deliverables. The previous arbitrary twelve-area suggestion did not apply it. The correction is an explicit design checkpoint: before settling a meaningful new approach, identify suitable examples, inspect their actual mechanisms, state what is adopted/rejected and why, then validate the result against the intended use.

Evidence for factual claims and examples of excellent implementation are different inputs. Popularity and polished marketing establish neither effectiveness nor personal suitability. Reuse existing findings when still applicable; reopen research when material uncertainty or context changes. Routine edits do not require restarting an exemplar search.

A reusable skill for this practice across products is a separate possible task. For this product, first give the rule one authoritative home and ensure the design/planning entry reaches it. Merely adding another optional skill would not ensure use.

## Naming

Keep product brand, installed technical namespace, and the user's workspace/vault name separate. Steward can remain a personal vault name. No brand has been selected; defer a repository or namespace rename until a candidate is chosen and availability is checked. A later rename must preserve relative references and existing memory configuration.

## Acceptance checks before calling this packaged

Test a first-time plain-folder user, an existing Obsidian user, and a user with no app installation rights. Interrupt both setup and personal onboarding, then resume without duplication. Return after a long gap without inferring completed actions. Accept both “What next?” and an already-specific request. Preserve distinct goals through a shared-context correction. Verify reminder creation only when requested, and verify the no-reminder path. Confirm the life-area menu can be skipped, renamed, extended, and revisited.

These are proposed checks, not tests executed in this research pass. The next implementation should prove the experience using realistic isolated fixtures before publication and installation.
