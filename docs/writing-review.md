# Skill writing review, 2026-09-16

Applied writing-great-skills, its glossary, writing-for-agents, and native skill-creator guidance to every entrypoint and shared reference. The review prioritizes predictable selection, explicit branches, checkable completion, and one authoritative home for shared rules.

## Decisions

Keep all thirteen skills automatically discoverable. Each owns an independently requested job; people should be able to ask normally without remembering thirteen commands. New goals and areas remain records, not additional skills. There is no demonstrated need for a router or another sequence split.

Descriptions fell from 397 to 284 whitespace-separated words (28% fewer). This measures text size, not model token use or improved selection accuracy. Distinct triggers and likely routing boundaries remain explicit; examples that merely repeated a branch were removed.

Keep the small memory, maintenance, and experiment branches inline: each entrypoint remains short enough to read as a whole. Their headings separate conditional reference from the shared steps. Creating more files would add navigation without a demonstrated need.

## Review by owner

| Owner | Result |
|---|---|
| focus | Retain priority selection and parent-goal tradeoffs; shorten discovery text. |
| goals | Retain separate identities, lifecycle transitions, and action-mode separation; shorten discovery text. |
| plan | Retain detailed deliverable, feasibility, and consistency criteria; shorten discovery text. |
| routines | Retain triggers, fallbacks, working tracking calculations, and adaptation; shorten discovery text. |
| schedule | Retain calendar reconciliation, freshness, and verified scheduling; shorten discovery text. |
| decide | Add an explicit completion criterion for requested implementation; retain actual-horizon cost comparison. |
| admin | Point correspondence work to messages instead of duplicating its voice rules. |
| messages | Own recipient history and voice in one place; read action details when sending. |
| review | Point prospective tests to experiments instead of repeating experiment design rules. |
| experiments | Recover the actual phase, then design, continue, or interpret; preserve the saved criteria and record design changes. |
| opportunities | Retain bounded search and net benefit; shorten discovery text. |
| memory | Separate recall/resumption, capture, and correction; use storage's write procedure by a direct pointer. |
| maintain | Separate setup/migration, audit/repair, forgetting, and retrieval improvement; allow an audit to finish with findings. |

Removed the obsolete “Menu is outside v0” fragment and the undefined “FINISH THE JOB” reference. Storage now owns the continuity material previously repeated in the model reference. Presentation points to artifact verification criteria instead of repeating them. Requirements for permissions, provenance, forgetting, freshness, actual baselines, calculations, and verified live state remain in their authoritative references.

## Checks and limits

All thirteen entrypoints passed native skill validation. The repository check passed for thirteen skills and 91 local references. The diff passed whitespace checks. The host Python initially lacked PyYAML; native validation succeeded using the existing local validator dependency directory without modifying the user's Python installation.

These checks validate structure. They do not prove better automatic selection or behavior across all requests. This revision does not inherit a blanket behavioral pass from earlier versions.

An independent agent then exercised three synthetic requests: recall a goal without writing, report broken links without repairing, and interpret an experiment with no recorded observations. All three returned the appropriate bounded result; before/after hashes confirm the four fixture files were unchanged. [Raw fixtures, responses, and execution evidence](writing-review-evidence.md) preserve the actual run and runtime fingerprint. This was one agent with three scenarios, not three fresh sessions or an auto-selection benchmark.

The source revision is on local branch `codex/skill-writing-review`. Installation and publication are separate operations; this review does not update installed copies or the GitHub branch.
