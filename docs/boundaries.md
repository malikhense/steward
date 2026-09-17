# Use cases and skill boundaries

## Design decision

Separate by the job the user can independently ask for, its working information, and its completion condition. A new area or goal changes the records. A different kind of work can change the skill. This gives thirteen personal-work specialists, a guided session workflow, an Apple integration skill, and the short `$steward` product entry. The product entry delegates to the session workflow; it does not duplicate its behavior or impose a mandatory pipeline.

The cut follows writing-great-skills and writing-for-agents: discriminate triggers, keep shared meanings in one home, disclose conditional detail, and define observable completion. It is a cut by invocation. No claim is made that reading another skill creates an isolated context or prevents premature completion through a new session.

## Representative use-case inventory

Each row names the primary owner. Supporting skills load only if the request actually needs them.

| # | Situation | Primary owner | Completion or meaningful boundary |
|---|---|---|---|
| 1 | “I feel stuck; where do I start?” | focus | Concrete focus options grounded in present constraints |
| 2 | Explore what better health would mean | focus | Desired outcomes separated from generic health advice |
| 3 | Choose between work, study, and recovery | focus | Priorities and displaced commitments made explicit |
| 4 | Reassess life areas after a move or new job | focus | Affected priorities revisited without resetting everything |
| 5 | Protect maintenance and recreation | focus | Capacity reserved without inventing achievement goals |
| 6 | Add a second or fifth goal | goals | Separate record; existing goals preserved |
| 7 | Clarify “get better with money” | goals | Useful outcome, reason, baseline, success signal |
| 8 | Set a maintenance goal | goals | Recognizable condition and review point |
| 9 | Change a goal's success criteria | goals | Updated outcome and affected plan links |
| 10 | Pause a goal during a busy period | goals | Status and related commitments reconciled |
| 11 | Resume a paused goal | goals | Stale context checked; open work restored |
| 12 | Complete or retire a goal | goals | Evidence or decision recorded; lingering actions addressed |
| 13 | Build a learning plan | plan | Materials, practice, milestones, realistic time |
| 14 | Plan a move or home project | plan | Dependencies, responsibilities, resources, usable checklist |
| 15 | Build a meal and grocery plan | plan | Portions, nutrition, pantry, packages, prep, payer, cost |
| 16 | Build an exercise program | plan | Baseline, exact instruction, progression, recovery, demos |
| 17 | Plan a trip or event | plan | Coherent itinerary, logistics, cost, open decisions |
| 18 | Transition toward an earlier wake time | plan | Workable present behavior and transition inside one plan |
| 19 | Create requested PDF or spreadsheet guide | plan | Actual checked artifact, using format specialist |
| 20 | Build a morning or evening sequence | routines | Trigger, order, resources, duration, fallback |
| 21 | Establish deliberate practice | routines | Repeatable behavior fitted to current capacity |
| 22 | Add measurement or medication logistics | routines | Confirmed instructions, reliable trigger and recording; uncertainties resolved |
| 23 | Repair a routine that is too long | routines | Usable minimum and normal version |
| 24 | Build automatic tracking calculations | routines | Working formulas tested with separate sample data |
| 25 | Organize recurring chores or maintenance | routines | Cadence, resources, ownership, completion |
| 26 | Plan today or next week | schedule | Actual capacity, anchors, dependencies, slack |
| 27 | Recover from a disrupted day | schedule | Feasible revised times and explicit deferrals |
| 28 | Move an existing calendar event | schedule | Correct event updated and verified within authorization |
| 29 | Set recurring check-ins | schedule | Verified scheduler, cadence, scope, stop condition |
| 30 | Switch shifts or timezones | schedule | Affected time commitments reconciled, linked constraints propagated |
| 31 | Choose a product or service | decide | Suitability, quality, full costs, evidence, recommendation |
| 32 | Choose between strategies for the same goal | decide | Parent purpose and actual tradeoffs resolved |
| 33 | Compare a membership or subscription | decide | Net result over the actual remaining/use horizon |
| 34 | Assess a supplement or health claim | decide | Appropriate evidence, suitability, uncertainty, next action |
| 35 | Decide whether to stop an activity | decide | Benefit, burden, user values, lost value considered |
| 36 | Fill a form or assemble application materials | admin | Complete artifact or verified authorized submission |
| 37 | Book an already chosen service | admin | Exact terms, scope, verified reservation or prepared action |
| 38 | Execute an approved grocery order | admin | Correct quantities and total; verified scoped action |
| 39 | Return an item or request a refund | admin | Evidence, prepared or authorized submitted request, next physical step |
| 40 | Cancel a chosen service | admin | Exact service, terms, authorized action, verified state |
| 41 | Coordinate household logistics | admin | Responsibilities and concrete follow-through resolved |
| 42 | Draft an everyday reply | messages | Actual recipient context and user's relationship-specific voice |
| 43 | Prepare a difficult conversation message | messages | Accurate intent, appropriate tone, no invented commitments |
| 44 | Revise a draft after tone feedback | messages | Usable revision and scoped preference learning |
| 45 | Send an explicitly authorized message | messages | Correct payload/recipient, verified result, no duplicate retry |
| 46 | Conduct a weekly or monthly review | review | Outcomes and burden assessed; warranted operational changes |
| 47 | Diagnose a repeatedly skipped plan | review | Causes and uncertainty separated; friction reduced |
| 48 | Ask whether a goal still matters | review | Goal's purpose revisited; decision or focus work follows |
| 49 | Compare actual spending/time against a plan | review | Meaningful divergence and adaptations, not just logging |
| 50 | Test two practice times | experiments | Question, bounded change, observations, decision criteria |
| 51 | Test a smaller routine | experiments | Executable test and burden-aware tracking |
| 52 | Interpret an experiment | experiments | Qualified result and keep/change/remove decision |
| 53 | Find avoidable fees or useful resources | opportunities | Grounded candidates with net value |
| 54 | Combine errands or remove repeated effort | opportunities | Concrete feasible preparation |
| 55 | Explore plausible income or learning opportunities | opportunities | Fit, evidence, effort, risk, useful next work |
| 56 | Remember a preference, constraint, or decision | memory | Canonical dated record with source/classification |
| 57 | Recall why an option was chosen | memory | Decision plus reason and provenance |
| 58 | Continue a known goal in a new task | memory → work owner | Correct current state recovered, actual work resumed |
| 59 | Correct a fact that affects several areas | memory → work owners | Superseded claim replaced; dependencies reconciled |
| 60 | Save a useful source into the knowledge base | memory | Preserved source and relevant synthesis, retrievable links |
| 61 | Set up a vault and trusted instructions | maintain | Real configured location and tested retrieval |
| 62 | Migrate an existing vault or change its layout | maintain | Sources and human content preserved; links verified |
| 63 | Repair duplicates, contradictions, or stale records | maintain | Supported repairs; unresolved factual issues explicit |
| 64 | Forget a fact or remove a record | maintain | Scoped deletion across retrieval surfaces; residual copies disclosed |
| 65 | Improve memory retrieval | maintain | Known-answer benchmark before and after changes |

## Boundaries that prevent overlap

| Neighboring skills | Decisive distinction |
|---|---|
| Focus / goals | Choose what deserves attention / define and manage an outcome already chosen |
| Goals / plan | What should become true and its status / how to get there from reality |
| Plan / routines | Coherent path and outputs / an executable repeated sequence |
| Routines / schedule | Trigger and behavior / fit into actual available time or calendar |
| Decide / admin | Choose an option / carry out the chosen practical action |
| Admin / messages | Finish an administrative transaction / produce correspondence in the right voice |
| Review / experiments | Interpret what happened and adapt / design or interpret a specific bounded test |
| Review / maintain | Improve the user's goal or plan / improve the integrity of the memory system |
| Opportunities / focus | Discover grounded improvements / choose what the user should prioritize |
| Memory / maintain | Everyday retrieval and record changes / system setup, broad repair, migration, forgetting |

Selection follows the requested outcome, not keyword matching. “Review whether this subscription is worth it” is a decision when the objective is comparing options; “review last month's spending against my plan” is a progress review. “I got a new schedule; update everything” starts with the changed context and uses the affected work owners. It does not run all thirteen skills.

## Composition and ongoing use

One request can require several skills. “Help me start running” may need goals, plan, routines, and scheduling. The requested scope determines when to stop; each internal skill completion is not a new user approval gate. “Draft a reply” generally ends with the draft. “Make this happen” requires reasonable implementation beyond recommendations.

The suite's shared working contract specifies continuation, mode, source quality, propagation, completion, and memory write-back. It lives in steward-memory's references and is loaded once per task. Substantive detail has an owning reference: evidence in decide, action authorization/state in admin, deliverable checks in plan, context/model/storage in memory, retrospective learning in review. Relative pointers retain one authoritative meaning instead of copying thirteen monoliths.

The vault stores distinct areas, goals, plans, routines, decisions, history, sources, and useful knowledge. Switching goals retrieves another set of records while retaining shared constraints. Starting a new task reads saved state; it does not depend on the previous task's transcript being available. No skill is permanently running. Reminders or monitoring require a real scheduler and authorization.

## Deliberately not separate skills yet

- **One per area, goal, or person.** Most differences are context and data. A domain skill is justified later by a recurring distinct procedure, evidence needs, or tools, not the existence of another goal.
- **Onboarding.** Relevant context acquisition happens wherever missing context matters. A separate universal intake would encourage questionnaires and restarting existing work.
- **Resume.** Retrieval restores the selected state; the relevant work owner continues. A separate resume skill would duplicate memory and routing.
- **Context propagation.** It is a shared obligation on any decision-changing correction, not something the user should have to remember to invoke.
- **Generic research, PDFs, spreadsheets, coding, or browsing.** Use existing specialist capabilities. Steward adds personal context and completion criteria instead of replacing those skills.
- **Purchasing as a separate initial skill.** Option selection belongs to decide; a chosen transaction belongs to admin. Split a shopping workflow later if actual repeated work needs substantial unique procedures.
- **Always-on agent.** Background execution is infrastructure, not an additional prompt file.
- **A broad umbrella router.** The session entry owns setup/orientation/return guidance and loads specialist instructions for actual work. It does not copy all workflows or intercept unrelated requests. Direct specialist entry remains supported.
- **Skill authoring or system redesign inside personal workflows.** Use writing-great-skills, writing-for-agents, and skill-creator as development tools. Routine goal work should not rewrite its own governing instructions from imported content.

## Naming and packaging

Steward was the user's tentative vault name. It is used provisionally as a namespace so these skills do not collide with generic skills such as research or plan. Functional suffixes explain the job even if the umbrella name changes later. The product is now named Steward; the steward-* namespace remains stable for compatibility.

All fourteen folders form one versioned suite with shared references. Installing a single folder without its referenced siblings is unsupported. The prior package remains archived as source and regression evidence. This local package is created and reviewable; it is not a claim that an actual vault, CLI integration, or background memory service is already active.

## Guided session entry

`steward-session` owns technical-setup guidance, personal onboarding, and open-ended check-ins in the configured personal workspace. Specific requests can still enter a specialist directly. Separate setup and onboarding references preserve distinct completion states; the session loop is Check in → Make progress → Adjust.

## Steward Apple

`steward-apple` owns native Apple access and private-container checks, separate from scheduling, correspondence, review, and memory. Direct connector operations expose a narrow verified schema; broader app features use current UI inspection. This is a capability boundary, not a new mandatory life-management step.
