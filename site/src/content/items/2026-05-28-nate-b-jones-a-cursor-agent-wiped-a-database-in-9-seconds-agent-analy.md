---
title: A Cursor Agent Wiped a Database in 9 Seconds. Agent Analytics Would Have Seen It Coming.
author: Nate B Jones
source_id: 1
source_slug: nate-b-jones
url: https://www.youtube.com/watch?v=n0nC1kmztSk
published_at: '2026-05-28T14:00:28Z'
duration_seconds: null
primary_theme: tech
secondary_theme: business
relevance: 8
hook: Agents can 1000x productivity—or quietly destroy everything—depending on your analytics.
tldr: The talk argues that traditional product analytics and raw engineering traces are inadequate for AI agents. Instead, teams must treat each agent run as a unit of delegated work and track intent, tools, permissions, corrections, completion, and user acceptance. Without this product-level view, organizations will miss failure patterns like the infamous 9‑second database wipe and misjudge whether agents are actually creating value or just activity.
caveats: Skip it if you want implementation-level detail, because the core argument sounds useful but may stay at the product/measurement layer rather than showing a concrete instrumentation stack or hard numbers.
pitch: You work on LLM agents and production AI systems, so this is worth your time because it frames agent analytics around the real unit you care about—delegated work, permissions, corrections, and acceptance—not just chats and traces.
---

## Key Points

- AI agents massively amplify execution speed, so the ability to steer them in real time becomes critical.
- Conventional product analytics focused on clicks, sessions, and funnels cannot explain what happens inside an agent run.
- Chat logs alone are insufficient because key signals about tools, permissions, and corrections are buried in unstructured text.
- Engineering traces capture calls, tools, and errors but do not by themselves indicate user value or trust.
- The meaningful unit of analysis for agent products is the agent run, treated as delegated work.
- Teams should distinguish between task completion and user acceptance, because high completion with low acceptance indicates low trust.
- Mid‑run corrections and interruptions are high‑value labels that reveal misunderstandings, missing context, and unsafe actions.
- Product analytics for agents requires a schema that tracks run start, task completion, and user shaping events tied to a run ID.

## Notes

## Why Agent Analytics Is a New Kind of Problem

AI agents let us execute work at unprecedented scale and speed, equivalent to tens of thousands of developer years in code-like output. This changes the stakes: agents can accelerate useful work, but they can also cause catastrophic failures very quickly. The well-known example is a Cursor agent that erased a small company’s production database and volume-level backups in 9 seconds via a single Railway API call. That story is often framed as a “rogue AI” incident, but the speaker argues the deeper issue is product analytics: most teams lack visibility into what actually happens inside agent runs.

Historically, product analytics asked simple questions: did users arrive, click, move through funnels, return, and convert? Those questions remain relevant but are no longer sufficient when the “user” of the product is, in part, an agent doing delegated work.

## From Clicks to Delegated Work as the Core Unit

In an agent-based product, the meaningful unit of behavior is not just a click or a session; it is delegated work. The important “action” might be the instruction the user gives the agent rather than a UI click. The important “event” might be a tool call the agent makes rather than a page view. The important “failure” might be the agent repeatedly retrying an action, hitting a permission boundary, losing context, asking for unnecessary approval, or finishing work that the user ends up quietly rewriting.

The speaker proposes a new mental model: treat each agent run as the core analytical unit. A session only says someone showed up; an agent run says what work was actually attempted. A run might start when a user asks for support, reconciliation, meeting prep, pipeline updates, or account research. Regardless of domain, you can ask a consistent set of questions about that run: what was the user trying to do, what tools were used, where did failures occur, and how did the user respond?

## Limits of Chat Logs as a Primary Signal

Many current products use chat transcripts as their main window into agent behavior. Chat logs are helpful for qualitative review: they reveal user questions, agent responses, weak prompts, missing context, poor tone, hallucinations, and confusing product surfaces. However, they do not systematically show which tools were available, which tools the agent called, which calls failed, where retries occurred, when permissions blocked actions, or whether users accepted, corrected, or redid the work.

Even if some of that information appears in the text, it is trapped in unstructured form. Humans can read transcripts and extract insights, but dashboards cannot easily aggregate those signals across hundreds or thousands of agent runs. As a result, chat activity can look healthy while the underlying work is failing. A long chat, for instance, may indicate a genuinely complex task—or it may signal that the agent is forcing users to restate context, correct repeated errors, and work around missing product structure. Both cases collapse into the same “active session” metric, which is not enough for agent-native products.

## Why Engineering Traces Are Necessary but Insufficient

Developer observability tools are closer to what’s needed than traditional product analytics, but they still fall short. Tracing infrastructure can capture model calls, tool calls, handoffs, guardrails, latency, cost, and errors. These signals are critical for engineering teams to debug and tune systems.

Yet trace data is not automatically product analytics. Product analytics must answer different questions: did the failure matter to the user, did the workflow still complete, did the user trust the output, and should the product behavior change? For example, a trace can show that the agent asked for approval; product analytics must determine whether this approval step actually improved safety or merely added friction. A trace can show a run that cost $0.30; product analytics must say whether that cost was justified by the outcome.

The missing layer for most teams is this translation from raw execution data into product value signals tied to user outcomes.

## The Agent Run as the Fundamental Analytical Object

The speaker emphasizes that agent runs should become the basic unit in analytics. For each run, teams should track:
- What the user was trying to accomplish (intent and workflow context).
- Whether the agent correctly understood that intent.
- What tools were used and which calls failed.
- Whether approvals were requested and how permission policies affected actions.
- Whether the task completed, partially completed, failed, or was abandoned.
- Whether the user accepted the output or redid the work themselves.

These are product questions, not just engineering questions. They determine whether the agent is delivering meaningful, trusted work rather than just generating activity.

## Industry Example: Salesforce’s Agent Work Units (AWUs)

Salesforce offers an early example of this shift with “Agent Work Units” (AWUs), introduced in its February 2026 fiscal Q4 earnings release. AWUs measure tasks accomplished by AI agents across Agentforce and Slack. Salesforce reported 2.44 billion AWUs delivered to date, with 57% quarter-over-quarter growth.

This signals a move away from metrics like seats, sessions, or even tokens toward naming units of work. But simply naming work units is not enough; those units are only useful if teams know what kind of work occurred, what workflow the run belonged to, whether tool calls succeeded, whether users trusted the outputs, and whether business outcomes improved. Otherwise, “work unit volume” risks becoming just another vanity metric, like raw chat volume.

## Corrections, Interruptions, and the Link to Eval

One of the highest-value signals in agent analytics is user correction during a run. Corrections include interruptions, edits to outputs, denial of approvals, clarifications added mid-run, or reopening tasks. Each correction effectively labels the run, indicating where the agent misunderstood context, where information was missing, which actions felt unsafe, or which outputs failed quality expectations.

This is why agent analytics and evaluation (eval) should be tightly connected. A denied approval can function as a test of whether the agent should have proposed that action or should have located an applicable policy or preference. A failed tool call can become a schema test. An abandoned workflow can trigger investigation into whether the product structure or agent behavior caused drop-off.

While not every prompt, record, or output should automatically feed into training due to privacy and other constraints, product analytics should at least structure these signals to inform product and eval work.

## Completion vs Acceptance: Measuring Trust, Not Just Output

The speaker distinguishes sharply between completion and acceptance. Completion means the task reached a finish state from the system’s perspective. Acceptance means the user trusted and adopted the result.

Several scenarios follow:
- High completion, low acceptance: the agent finishes work users do not trust, indicating low trust and poor value.
- Low completion, low acceptance: users abandon before the product reaches a reviewable state, indicating serious usability or capability issues.
- Low completion, high acceptance: the agent may be overly conservative or limited, but highly valuable when it does act.
- High completion, high acceptance: the workflow may be suitable for more autonomy, since users both see finished work and trust it.

Most current dashboards struggle to represent the gap between completion and acceptance, yet that gap is central to understanding whether agents are actually helping.

## Minimal Schema: Three Events to Ship First

For teams starting to build agent analytics, the speaker suggests a minimal viable schema centered on three event types:
1. Agent run started.
2. Task completed.
3. User shaping events in the middle of the run (corrections, interruptions, approvals, denials, edits).

All of these must be tied to the same agent run ID. This linkage enables calculation of completion rates and correction rates by workflow. With that, teams can start asking meaningful questions: where are runs frequently interrupted, where are users regularly correcting outputs, and where do patterns predict potential high-risk behavior?

## Designing the “Rudder” for a 1000x Speedboat

Agents can accelerate work by 10x, 100x, or 1000x, which the speaker likens to building a speedboat. The key challenge is shaping this speedboat with a reliable rudder. That rudder is product analytics—not just engineering traces.

Teams should routinely ask whether they have the product analytics views needed to shape agent behavior at the speed agents operate. They must understand interruptions, retries, and handoffs, since these are the “new clicks” in the agent era. A strong agent product does more than answer questions; it:
- Moves through work with appropriate autonomy.
- Asks for help at the right moments.
- Recovers gracefully from failures.
- Respects permissions and policies.
- Uses memory correctly.
- Produces outcomes users trust.

Product analytics should be designed to measure to what extent these properties hold in real deployments.

## Avoiding Catastrophes Through Behavioral History

Returning to the database deletion story, the speaker argues that such catastrophic actions should be predictable and preventable if teams have proper agent analytics. Instead of only inspecting a single technical failure after the fact, teams should examine the history of agent behavior for the relevant workflow. Defective workflows and problematic run patterns would reveal themselves long before an agent is in a position to delete a production database.

Without product-level analytics, organizations see only raw activity and then are surprised by disasters. With a thoughtful data schema and agent-run-centric analytics, teams can anticipate and address failure modes before they manifest in high-stakes actions.

## Ownership and Next Steps

The speaker cautions against delegating agent analytics entirely to engineering. Engineering traces are necessary building blocks, but product teams must define the schema and views that express product value and user trust. The effectiveness and safety of agent deployments depend on this layer.

They close by pointing to a starter guide hosted on their Substack and stressing that, because AI work never really stops, teams that do not invest in agent analytics risk being left behind as agents grow faster and more autonomous.

