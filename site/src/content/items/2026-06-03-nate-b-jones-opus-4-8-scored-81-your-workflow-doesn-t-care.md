---
title: Opus 4.8 Scored 81. Your Workflow Doesn't Care.
author: Nate B Jones
source_id: 1
source_slug: nate-b-jones
url: https://www.youtube.com/watch?v=z73yuF14udI
published_at: '2026-06-03T14:00:38Z'
duration_seconds: null
primary_theme: tech
secondary_theme: business
relevance: 8
hook: Opus 4.8 is powerful, but your workflow still prefers something else.
tldr: Opus 4.8 is a strong, highly aligned model, but often overthinks and behaves inconsistently under higher reasoning settings. Its practical usefulness lags behind OpenAI’s 5.5 largely because Anthropic’s current harnesses and computer-use capabilities are weaker, especially for long-running, complex tasks. In 2026, the real competitive frontier is flexible, outcome-focused harness design and agentic pipelines, not isolated model benchmarks.
caveats: Skip it if you want hard experimental detail, because this reads more like informed product commentary than a deeply technical teardown with reproducible evals and architecture numbers.
pitch: 'You work on LLM agents and production AI infrastructure, so this is worth your time because it focuses on the part that actually matters to you: how model choice, harness design, and agentic workflows change real task performance beyond benchmark hype.'
---

## Key Points

- Opus 4.8 is a strong checkpoint model, but not Anthropic’s long-awaited Mythos-scale release.
- Opus 4.8 shows regressions on practical benchmarks like VendingBench compared to Opus 4.7, even at higher reasoning modes.
- Scaling Opus 4.8’s reasoning to max does not reliably improve results and can underperform its high setting.
- Opus 4.8 often overthinks alignment and constitutional issues, reducing its effectiveness on straightforward tasks.
- Daily-driver usefulness now depends more on harness quality than raw model intelligence or benchmark scores.
- OpenAI’s 5.5 in CodeX currently offers a far stronger harness for long-running, multi-hour agentic tasks than Opus 4.8’s tools.
- Anthropic’s /workflows command in Claude Code is a notable innovation, giving transparent, dynamically composed multi-agent workflows.
- Leaders should architect AI systems for model flexibility and agentic pipelines, rather than committing budgets to a single vendor or model.

## Notes

## Opus 4.8’s Place in the Race

- Opus 4.8 is not Anthropic’s long-teased “Mythos” supermodel; it’s a strong checkpoint release aligned with a funding announcement and valuation milestone.
- The release timing was driven by the need to pair a model drop with a major funding news cycle, not because 4.8 is their ultimate model.
- 4.8 advances long-running, agentic-style tasks and stays on task better than 4.7, which struggled with attention.
- However, it is not the massive intelligence jump many expected from Mythos, likely constrained by compute limits.
- The headline: 4.8 may be one of the most capable models on some metrics, but that no longer guarantees it is the best daily driver.

## Reasoning Modes and Overthinking

- A central problem: 4.8 does not behave predictably when you increase reasoning effort.
- For more than a year, the norm has been “scale up reasoning and get better results at higher cost.”
- With 4.8, sometimes max reasoning is best, sometimes high is better, and this inconsistency makes product decisions difficult.
- In contrast, OpenAI’s extra-high reasoning modes on 5.5 predictably improve performance, making them easier to use as a knob.

### Evidence from VendingBench

- VendingBench tests AI performance at running a simple business (a vending machine) and is considered a practical benchmark.
- Opus 4.7 outperforms Opus 4.8 on VendingBench; 4.8 is a regression there.
- This regression appears regardless of whether 4.8 is run on high or max reasoning modes.
- Strikingly, 4.8 on high beats 4.8 on max for this benchmark, confirming that “more thinking” does not equal “better results.”

### Alignment-Driven Overthinking

- 4.8 is very focused on alignment and constitutional constraints, which in moderation is desirable for safety.
- But reasoning traces from 4.8 max show the model ruminating about writing “warm paragraphs,” aligning with its constitution, and referencing Amanda Askell’s preferences.
- This suggests the model is devoting excessive internal effort to meta-considerations about alignment and tone instead of solving the user’s problem.
- That overthinking makes behavior less predictable and erodes trust in 4.8 as a daily driver, even though it remains strong in specific areas.

## Harnesses Now Matter More Than Models

- The “harness” is defined as the product layer around a model: UI, tools, workflows, computer use, file access, and agent orchestration.
- In 2026, daily-driver value is dominated by harness quality, not just model IQ or benchmark scores.
- The tasks being run have shifted; models can now sustain long agentic runs and self-review, so the harness must support multi-hour, multi-step autonomy rather than just prompt-in, answer-out.

### CodeX (OpenAI 5.5) vs Claude Code (Opus 4.8)

- Earlier in the year, Claude Code felt extremely ergonomic: natural language in the terminal, automatic sub-agents, RAFT loops for big jobs.
- That environment has not regressed, but the frontier has moved; OpenAI’s CodeX harness has advanced further.
- For complex, edge-of-capability work and multi-hour jobs, there is a “big gap” right now in favor of 5.5 in CodeX.

## Concrete Long-Running Task Comparison

- Example test: ask both 4.8 and 5.5 to design and build, end-to-end, a complete website for a Markdown-focused domain.
- Expectations: AI should handle multi-step work without constant hand-holding, reminders, or manual verification steps, and should produce more than a trivial single-page site.
- In practice, Opus 4.8 repeatedly errored out due to compute availability and handled only one task at a time slowly.
- OpenAI 5.5, through CodeX, built two such sites in parallel relatively quickly.
- Although the initial 5.5 designs were not ideal, the harness enabled an iterative loop: use ChatGPT’s images mode to mock up a better design, feed it back, and refine.
- Within the same time window, 5.5 completed two full sites—deployed with DNS and name servers—while 4.8 failed twice.

### File and Computer Use Ergonomics

- 5.5 in CodeX can readily search local files across the machine when asked, improving long-task ergonomics.
- 4.8 in the desktop app can only see limited locations (downloads, desktop), and does not proactively request broader access when it’s clearly needed.
- Such “small” friction points compound in multi-hour tasks, making large jobs unreliable on Claude compared to CodeX.

## Strategic Guidance: Don’t Bet on One Horse

- Many organizations have heavily committed to a single vendor (e.g., large Anthropic contracts) and are now frustrated by performance or cost issues.
- The recommendation is to allocate budget to outcomes, not vendors, and architect harnesses so models are swappable via simple API changes.
- The market history suggests an ongoing horse race where leadership will keep flipping, so systems should be built for flexibility.
- Anticipated 10-trillion-parameter models, including Mythos, 5.5, and upcoming open-source models, mean high-end capability will become broadly available.
- By the end of the year, such open-source models may effectively “solve” most generic knowledge work, making vendor lock-in even less rational.

## Where Opus 4.8 Excels

- Despite its issues, 4.8 remains very strong at:
  - Front-end design and aesthetic sense (“front-end taste”).
  - Writing quality, warmth, and non-robotic prose.
- These are established strengths of the Opus/Claude lineage and make 4.8 appealing for lower-volume writing and design workflows.
- For high-volume or production-critical needs, the advice is to lean on CodeX and fill design/writing gaps with skills or complementary tools.

## The /workflows Innovation in Claude Code

- Historically, users had two options for workflows:
  - Fully specify the workflow, sub-agents, and steps deterministically.
  - Let the model decide everything, with limited visibility into its plan.
- Claude Code’s `/workflows` command offers a middle ground.
- With `/workflows`, the user asks Claude to compose a workflow; 4.8 then:
  - Thinks through the problem.
  - Designs a multi-agent workflow.
  - Discloses that workflow explicitly.
  - Assigns sub-agent tasks consistent with this dynamic plan.
- This gives transparency into how the model intends to tackle a complex task while retaining flexibility.
- The pattern is expected to be widely copied for individual-productivity agents, and currently even CodeX lacks an equivalent.

## Agents, Pipelines, and the “Piling Problem”

- The term “agents” now ambiguously covers both:
  - Individual productivity agents for a single developer or knowledge worker.
  - Larger, team- or org-scale agentic pipelines.
- The effects of tools like `/workflows` differ dramatically depending on which context you’re responsible for.
- At scale, organizations face a piling problem: agents generate huge volumes of downstream work that bottleneck on human review.
- If you do not design an agentic pipeline end-to-end, you simply accumulate piles for humans to clean up.

### Designing Agent-Native Pipelines

- Leaders should aim for “dark factory” style pipelines in engineering:
  - Engineers submit PRs; agents handle merge conflicts.
  - Agents perform first, second, and third PR reviews.
  - Agents monitor production and review each other’s work.
- Humans are “over the loop” rather than “in the loop,” focusing on designing and supervising the system, not manually touching every artifact.
- If you introduce tools like `/workflows` without redesigning the pipeline, they will merely accelerate the rate at which work piles up.

## Knowledge Workers and Outcome Thinking

- Non-coder but code-adjacent knowledge workers should mentally model their work like an engineering pipeline.
- The key question: Does AI-generated work create unsustainable downstream burdens for colleagues, or does it move the organization toward outcomes?
- In the second half of 2026, businesses will focus on outcomes, not raw AI activity, and workers should align their usage accordingly.

## Why CodeX’s Harness Currently Leads

- CodeX is described as “more self-aware” as a harness:
  - It can strategize about desired outcomes and how to structure automations.
  - It can use computer use and a built-in browser to implement those automations.
- Example: Ask CodeX to set up an automation whose output format does not overwhelm ticket-triage colleagues; it can both design and implement this with computer use.
- Anthropic’s 4.8 scores very well on paper for computer use but, in practice, CodeX’s implementation is faster and more dependable.
- This reliability gap is decisive for unattended automations that run while the user is away.

## Role-Specific Takeaways

### For Knowledge Workers

- If you mainly need writing and front-end design help and are not high-volume, Opus 4.8/Claude is an excellent fit.
- If you are high-volume, consider using CodeX for the main workflow and patching design/writing with additional skills or ChatGPT-style tools.
- Always ask whether your AI usage creates sustainable progress toward business outcomes or just more work for others.

### For Engineers

- Most engineers currently use Claude Code, with a smaller but significant share using CodeX and some using open source.
- You should evaluate your tools based on how the harness supports your productivity in the team’s broader pipeline, not just your solo speed.
- `/workflows` can significantly boost individual developer productivity but will also amplify downstream workload unless paired with pipeline design.

### For CTOs and CIOs

- The market is a two-horse race right now (OpenAI and Anthropic), and leadership will keep changing.
- Systems must be architected so they can smoothly incorporate new leaders like Mythos or strong open-source 10T models.
- Budgets should be tied to outcomes and flexible harnesses, not locked into a single model provider.

## Final Synthesis on Opus 4.8

- Opus 4.8 is a very capable, highly aligned model with standout strengths in writing and design.
- Its main weaknesses are inconsistency at higher reasoning levels, overthinking alignment questions, and a weaker harness ecosystem compared with CodeX.
- In 2026, the decisive factor is not whether 4.8 is “smarter” than 5.5, but whether its harness lets you reliably execute long, complex, outcome-aligned workflows.
- Right now, 5.5 in CodeX fits its harness “hand in glove,” while 4.8 feels like an overthinking checkpoint that is not yet matched to an equally strong harness.
- The strategic move is to prioritize harness design and system flexibility so you can adopt whichever models—Claude, GPT, or open source—best serve your evolving goals.

