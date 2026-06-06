---
title: My Codex Ran 800 Million Tokens in A Day. The Real Story Isn't Cost.
author: Nate B Jones
source_id: 1
source_slug: nate-b-jones
url: https://www.youtube.com/watch?v=l8BloTSLK6M
published_at: '2026-06-05T14:00:07Z'
duration_seconds: null
primary_theme: tech
secondary_theme: thinking
relevance: 4
hook: A personal “token burn” dashboard as a compass for delegated AI intelligence.
tldr: Nate Jones built a token burn dashboard to understand how he actually uses AI, not to brag about volume. By correlating token usage with concrete projects and days, he can see when new tools, workflows, and multi‑agent runs unlock better results and stretch his imagination. He argues that metering tokens is a crucial feedback loop for personal learning, shared community discovery, and future proof of AI fluency in work.
caveats: Skip it if you want hard technical substance, architecture details, or evals rather than a personal token-dashboard narrative and career-signaling take.
pitch: If you want a quick look at how one practitioner instruments heavy agent usage as a feedback loop for real workflows, this gives you a concrete example of token telemetry as a learning tool.
---

## Key Points

- The dashboard tracks daily token usage across tools like Codeex, Claude, and ChatGPT to reveal behavior patterns.
- Codeex is favored because it exposes token counts precisely, enabling accurate measurement and visualization.
- Higher token spend is treated as a proxy for more delegated intelligence and often better problem‑solving outcomes.
- Nate used an open‑source Tufty visualization skill and natural‑language instructions to have Codeex build the charts.
- He approximated Claude token usage by having Codeex reason from logs and artifacts to infer likely consumption ranges.
- Multi‑agent workflows, such as slashworkflows, significantly increase tokens burned but also raise solution quality and depth.
- Nate uses AI agents for email, Slack, file organization, research, and internal dashboards, driving very high daily token usage.
- He believes public token charts will become career signals and shared learning tools, similar in importance to GitHub profiles.

## Notes

## Core Idea: Token Burn as a Feedback Loop for Intelligence

- Nate built a “token burn” dashboard that tracks how many tokens he uses across AI tools each day.
- The purpose is not bragging about burning ~800 million tokens in one day but understanding how his AI usage translates into work, imagination, and results.
- He frames token burn as a measurable proxy for “delegated intelligence” – how much thinking you are offloading to AI agents.
- Studies from major labs, he notes, repeatedly show a strong correlation: more tokens spent generally produce better outcomes.
- To learn how to use AI effectively, he argues you need a feedback loop: see token usage, link it to specific work, and notice when higher usage leads to higher quality results.

## Why Codeex and Measurement Matter

- Codeex exposes precise token counts at the session level, making it easy to meter usage.
- In contrast, Claude’s consumer interfaces (chat, co‑work) do not show token counts; you only get them easily through the API.
- Nate therefore had to approximate his Claude usage for the dashboard by having Codeex reason from logs and artifacts to estimate Claude tokens.
- Codeex even “quizzed” him about his claims and then produced a tight range estimate for Claude token usage.
- He repeatedly calls for Anthropic to meter Claude tokens more transparently because token visibility is essential for this style of learning and accountability.

## Building the Dashboard with AI

- He used an open‑source “Tufty” skill (inspired by data visualizer Edward Tufte) for clean, information‑dense charts.
- He described, in plain English to Codeex, the features he wanted:
  - A GitHub‑style chart of token burn over days.
  - Same‑day usage views to see which activities consumed tokens.
  - Model distribution showing how much came from Claude, ChatGPT, Codeex, etc.
  - Top 10 highest‑usage days, annotated with what he did on those days.
- He specified a logarithmic Y‑axis so that days with a few million tokens and days near a billion could coexist on one chart without breaking the scale.
- He iterated by imagination rather than a detailed upfront spec: he held a mental image of the dashboard and kept asking Codeex to refine it until reality matched the picture.
- Codeex not only generated the charts but also deployed the app, handled DNS, and set it up at tokenburn.mmarkdown.

## Behavioral Insights from the Chart

- Once the dashboard was running, he saw visible behavioral shifts, especially when he began using Codeex heavily.
- Token volumes increased substantially, revealing that new tools (Codeex, multi‑agent workflows) were unlocking more ambitious work.
- The top 10 token days correlate with significant projects, often involving intensive database work or multiple agents.
- Seeing, for example, that he burned 100 million tokens in an hour and all eight parallel threads completed successfully makes him realize he should do more parallel computing.
- He uses the dashboard daily to compare today’s AI use with prior high‑usage days and ask, “What am I doing differently, and what should I do more of?”

## Example: Multi‑Agent Workflows and School Research

- A new feature, `/workflows`, dropped with the Claude Opus 4.8 release, enabling easy multi‑agent orchestration via Claude code.
- `/workflows` creates a plan and spawns sub‑agents to tackle different parts of a task.
- An open‑source skill quickly appeared; Nate ported it into Codeex and used `/workflows` inside Codeex the same day.
- He used it to research schools for his children, producing a large comparative report with three or four agents working in parallel.
- Multi‑agent workflows consumed many more tokens but produced a more useful, comprehensive result than a single‑agent interaction.
- The chart then showed a clear spike in token usage linked to that workflow and task, letting him see the behavioral and quality change in context.

## Efficient, Not Wasteful, Token Use

- Nate stresses he is not advocating mindless token burning.
- He has skills that pause unneeded automations and shrink context windows where large contexts are unnecessary.
- The goal is effective, not wasteful, usage: measure tokens so you can allocate delegated intelligence to where it matters most.
- The dashboard helps answer: Where am I actually spending intelligence, and is it paying off in better outcomes?

## Reimagining Computing with Delegated Intelligence

- For Nate, this dashboard is part of a broader shift in how he conceives of computing.
- He increasingly treats files, screenshots, and workflows as raw material for AI rather than something he personally micromanages.
- Example: he had Codeex open every screenshot, label it, categorize it, and arrange files into folders; he no longer knows or cares about the folder structure.
- He uses Codeex as a “chief of staff” thread that can spin up sub‑agents for projects, keeping a central context while child threads handle detailed work.
- He relies on AI heavily for:
  - Email triage.
  - Slack checking.
  - File organization and downloads clean‑up.
  - Internal dashboards and running automations.
  - Troubleshooting tasks like internet issues.
- He argues everyone’s time is better spent outside of email and Slack, so delegating those to AI is a valuable use of intelligence.

## Community, Transparency, and Career Signaling

- Nate believes token dashboards will become as important as GitHub profiles for showing AI fluency.
- Employers might compare candidates’ charts and question very low token usage relative to others.
- Public token charts create a form of accountability that nudges people to explore and use AI more deeply.
- He is sharing multiple dashboard templates on Substack, including variants for Codeex‑heavy, ChatGPT‑heavy, or mixed setups.
- He wants people to build their own, share screenshots or summaries, and describe the tasks behind their top token days.
- He references a “you’re cool” culture at OpenAI where novel AI uses earn social recognition for a day; he thinks this culture of sharing should spread beyond hyperscalers.
- Through his Substack and WhatsApp executive chat, he already learns new use cases from subscribers and wants mutual learning to scale.

## Why Models Require Exploration and Shared Discovery

- Nate emphasizes that modern AI models are “grown, not made.”
- With on the order of 10 trillion parameters and reinforcement learning, no one fully understands every capability of a model.
- Treating them like traditional software with fully known behavior is misleading, especially in journalism.
- Because capabilities emerge rather than being fully designed, users must discover what is possible through experimentation.
- Tools like a token dashboard serve three roles:
  1. Show that a person is genuinely using AI intelligence.
  2. Make usage patterns visible so others can learn specific applications.
  3. Suggest ideas for where to go next, based on what worked and how it felt.
- He notes that the emotional experience matters too: how it feels to have a “100‑million‑token hour” or finish a big project and see the corresponding spike.

## Two Futures: Light Users vs. Heavy Delegators

- Nate contrasts “light users” burning a few million tokens a day with “heavy users” approaching a billion tokens daily.
- In token terms that is roughly a 99% difference; in fluency and impact, he feels the difference is even larger because of multi‑agent multiplicity.
- Many people say AI has not improved in six months, but he argues their imagination has not caught up; they are not asking AI to do enough.
- Tasks like organizing all screenshots, cleaning the downloads folder, handling support chores, and multi‑agent research are within reach now.
- The models are “almost never at the frontier at capacity”; most users are far from saturating what they could be delegating.

## Invitation and Practical Takeaways

- Nate’s real invitation is not “copy my chart” but “build your own compass for intelligence use.”
- Decide what you want to see: GitHub‑style daily heatmap, top 10 days, model splits, or other views.
- Use AI itself (e.g., Codeex, Opus 4.8) to construct and deploy the dashboard; you can iterate lazily by refining prompts.
- Once built, use the chart to:
  - Link token spikes to specific projects and workflows.
  - Identify which tasks benefit most from heavy AI delegation.
  - Notice when parallel, multi‑agent workflows produce better outcomes.
  - Spot wasteful contexts or automations and trim them.
- Finally, he encourages sharing dashboards and stories so everyone can discover new ways to apply “grown” models – and collectively become smarter with AI.

