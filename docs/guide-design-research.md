# A guide people can find and a conversation they can follow

Research date: 2026-09-16. This extends [the packaging research](product-packaging-research.md) with a narrower question: how should someone discover setup instructions, learn the everyday loop, and find a specialist when they want one? The first-party pages below were fetched and read directly. Their public documentation was inspected; their authenticated onboarding flows were not tested.

## Three patterns to adapt

| Source | Observation | Steward decision | Boundary |
|---|---|---|---|
| [Things support](https://culturedcode.com/things/support/) and [Getting Productive with Things](https://culturedcode.com/things/support/articles/6378414/) | The support landing page separates getting the app, learning basics, discovering features, and troubleshooting. Its usage guide teaches a sequence through everyday actions: capture, decide when, expand into projects when needed, and return to a daily routine. | Put visible **Set up Steward** and **Use Steward** links near the README opening. Make the usage guide about real requests and a repeatable loop. Introduce the complete skill map after a worked example. | Do not inherit Things' time estimate or promise equivalent results. Its list structure is one product's design, not a required taxonomy for every Steward user. |
| [Sunsama account setup](https://help.sunsama.com/docs/getting-started/setting-up-your-account/) | It distinguishes one-time setup from a first planning session and the normal daily flow. Tool selection happens before some connections are completed during real planning. The first session teaches using actual tasks, estimates, and deferral. | Keep technical installation distinct from personal orientation. Let the first conversation produce one useful outcome. Recover known choices, ask the next relevant question, and connect an optional app when its purpose is clear. | Sunsama gates workspace access on completing onboarding. Steward should preserve skipped connections, interruptions, and direct requests. Sunsama's scheduled daily prompts do not establish background behavior for a skill suite. |
| [GitHub CLI manual](https://cli.github.com/manual/) | The manual links available commands and usage examples separately. Installation has a distinct link; configuration is a short set of concrete actions. The full command hierarchy remains directly navigable. | Offer two paths: speak naturally to the AI agent, or choose a named specialist. Give each specialist a plain-language job and an example request. Keep installation detail in its own guide, linked from the first-use path. | A command catalog supports deliberate invocation. It does not prove that an AI host always selects the right skill implicitly. Describe automatic routing as behavior supported by the host and provide explicit selection as a fallback. |

## Recommended experience

Keep **Check in → Make progress → Adjust** as the public loop. Within it, show a typical goal journey as an example: focus on an area, define an outcome, plan a next step, make room for it, then review what happened. Let a person enter wherever their request belongs. A reply draft does not need a life-area interview; an existing goal does not need to be created again.

The conversational presentation is our adaptation of these patterns, not a claim that the reference products use conversational onboarding. Start from the user's words and saved context. Ask one meaningful question at a time, with a short optional suggestion when helpful. Skip answered questions and accept ordinary language. Keep saved setup state behind the conversation so an interruption does not cause a restart. End with what was actually produced and one clear way to return.

Use a small synthetic conversation in the guide to demonstrate this experience. Label it as an example rather than a transcript or testimonial. Show an undecided person, a useful follow-up question, a concrete first action, and a later adjustment. Follow it with the optional skill map for people who want precise control.

## Checks this design needs

- From the README opening, can a newcomer find setup and everyday usage without scanning the technical catalog?
- Can a first conversation begin with an uncertain request, accept a skipped connection, and yield a useful next step without exposing internal routing?
- Can a returning user resume without repeating known setup or a personal questionnaire?
- Can someone deliberately choose any specialist, and can a small direct request avoid the full loop?

These are evaluation questions, not measured usability results. This research changed only this note.
