# Model

| Term | Meaning | Minimum useful information |
|---|---|---|
| Area | Part of life the user wants to care for | Name; relevant goals or maintenance |
| Goal | What the user wants to become true | Desired outcome, why it matters, practical success signal |
| Habit | A repeated behavior serving a goal; need not be automatic yet | Behavior, purpose, cadence |
| Plan | How current reality reaches the goal | Baseline, strategy, dependencies, steps, resources, review |
| Routine | Reusable sequence of behaviors that belong together | Trigger, order, timing, frequency, normal/fallback |
| Block | Actual reserved or proposed time | Date/cadence, start/end, timezone, action, location if useful, status |
| Rule | Boundary shaping decisions across the system | Meaning, reason, applicable scope, firm versus revisable |
| Context | A fact, preference or uncertainty that may change a decision | Source, observation date, confidence and affected decisions |
| Benchmark | What excellent looks like for this outcome | Evidence/exemplar and limits of transfer |
| Experiment | A bounded test of an uncertainty | Question, change, duration, observations, keep/change/remove criterion |
| Deliverable | A usable output of a Plan | Exact artifact and where/how the user uses it |

The core chain is a navigation aid, not strict containment. One routine can serve several habits/goals; one rule can constrain many plans. Goals may have parent goals. One-off work can go straight from Goal to Plan to action. A calendar describes what happens; tracing upward explains why.

Baseline is Context. A transition, dependency, gap or bridge belongs inside Plan. Actions and deliverables are Plan outputs. Add a first-class noun only if existing concepts cannot express the needed distinction.

For storing or retrieving these records, read [storage](storage.md). It owns provenance, freshness, status, canonical records, and write verification.
