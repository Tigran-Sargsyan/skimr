---
title: Salesforce Killed The Browser. Every Agent Runs Your CRM Now.
author: Nate B Jones
source_id: 1
source_slug: nate-b-jones
url: https://www.youtube.com/watch?v=dQK_pTXrGDk
published_at: '2026-04-29T14:01:07Z'
duration_seconds: null
primary_theme: tech
secondary_theme: business
relevance: 6
hook: Stop asking which AI to switch to; start deciding what to layer where.
tldr: The video argues that AI agents should be evaluated as infrastructure layers, not just as models or flashy demos, using a five-question filter focusing on integration, openness, data access, ecosystem, and stackability. Applying this filter to ChatGPT Workspace Agents, Salesforce Headless 360, Microsoft Copilot Wave 3, Kimi K 2.6, and Perplexity Personal Computer shows each fits a specific job shape rather than being a universal default. Teams should stop chasing “one best agent,” keep a sensible default, and deliberately route different kinds of work to different agent layers based on where data, workflows, and governance actually live.
caveats: Skip it if you want hard technical details or benchmark evidence, because it reads more like strategic commentary on vendor positioning than an engineering deep dive.
pitch: If you care about how agent products fit into real stacks, this gives you a useful framework for thinking about integration, data access, and governance instead of chasing model hype.
---

## Key Points

- Agent launches are overwhelming, so teams need a clear filter to decide which ones merit attention rather than chasing every new model or demo.
- The key shift is from comparing model quality to assessing agent infrastructure: what tools an agent can reach, how it composes with others, and what data layer it sits on.
- A five-question filter screens launches: does it plug into existing tools, allow other agents to build on it, access important data, have a growing ecosystem, and let you stack agents on top.
- ChatGPT Workspace Agents are shared, cloud-run agents for recurring, cross-tool team workflows in ChatGPT and Slack, not a replacement for every agent category.
- Salesforce Headless 360 exposes nearly all Salesforce capabilities via APIs, MCP tools, and CLI so agents and coding tools can operate directly on CRM data without the browser UI.
- Salesforce’s move effectively turns it into infrastructure for the agent economy, letting many external agents (Claude, Cursor, Workspace Agents, Slack agents) act inside Salesforce with proper permissions.
- Microsoft Copilot Wave 3 (Co-work + Work IQ) tightly integrates agent execution with the Microsoft 365 graph, giving strong native data and governance advantages but a relatively closed ecosystem and weak fit for serious coding teams.
- Kimi K 2.6 is an open-weights, long-horizon multimodal agent model with a 300-agent swarm architecture, valuable mainly for developer teams who can self-host and build their own infrastructure, not as a typical enterprise SaaS product for business users.
- Perplexity Personal Computer on Mac turns Perplexity into a local, research-focused digital worker that can search, browse, edit local files, and orchestrate workflows to produce artifacts like reports and slide decks.
- Each tool has a “best-fit” job shape: Workspace Agents for shared cross-tool workflows, Salesforce for RevOps and CRM logic, Copilot for Microsoft-native knowledge work, Kimi for self-hosted agent infra, and Perplexity for research-heavy deliverables.
- Anthropic’s Claude strategy is increasingly layered: direct product, embedded engine inside others (Microsoft, Salesforce, Perplexity), and managed infrastructure for teams needing agent runtimes without building all plumbing.
- The classic “when should I switch from X to Y?” framing is wrong; the market is moving toward layered stacks where multiple agents and wrappers coexist and are chosen based on data graph and workflow, not just model quality.
- Teams should keep a capable default agent where model-centric reasoning is primary, then selectively use wrappers or different models when they provide unique data access, workflow integration, governance, or open-weight control.
- Switching wholesale is costly due to non-portable prompts, memories, and team habits; the real skill is routing work correctly across layers to avoid both tool sprawl and misfit usage.
- Agent products are not a single category; they span model frontends, workflow builders, enterprise data layers, open-weight infra, research workers, and control planes, so they should not all be compared on one flat chart.
- Going forward, teams that filter for infrastructure, ecosystems, stackability, and data access—and then match work shape to tool shape—will compound faster than those chasing headline benchmarks or demos.

## Notes

## Core Reframe: From Switching to Layering

- The AI landscape is flooded with new agents, models, and demos, leaving teams exhausted rather than excited.
- The important shift is away from “Which model is best?” toward “Which infrastructure and data layers actually matter for our work?”
- Instead of asking when to *switch* agents, treat agents as *layers* that sit on top of your existing tools and data graphs.

## The Five-Question Filter

1. **Does it plug into tools we already use?**
   - Infrastructure that reaches existing systems is valuable; new destinations that demand migration are costly and often not worth it.
2. **Can other agents build on it?**
   - Open APIs/MCP/CLIs = infrastructure; closed, self-contained experiences = features. Features commoditize; infrastructure compounds.
3. **Does it own or access data we care about?**
   - Agent usefulness is downstream of data access. A weaker model with full org history can outperform a stronger model with no context.
4. **Is there an ecosystem forming?**
   - Marketplaces, SDKs, partner programs, consistent shipping are signals a platform will persist and compound.
5. **Can we stack agents on top?**
   - Composable layers that let multiple agents orchestrate together are far more valuable than yet another siloed agent.

Most launches fail this filter; the few that pass deserve real evaluation time.

## Case 1: ChatGPT Workspace Agents

- Shared, code-executing agents for **recurring cross-tool workflows** (e.g., weekly metrics, risk screening, request triage) run in the cloud and surface in ChatGPT or Slack.
- They move from “personal assistant” to “team reusable work unit.”
- Strong fit when:
  - Work is recurring, cross-tool, and naturally lives in ChatGPT/Slack.
  - Team needs shared directory, permissions, scheduling, approvals.
- Weaker fit when:
  - Work is deeply native to Salesforce or Microsoft 365 (those have stronger data graphs).
  - The job is advanced coding, where specialist coding agents matter more.

## Case 2: Salesforce Headless 360 (Salesforce ‘kills the browser’)

- Salesforce exposes almost all capabilities as APIs, MCP tools, or CLI, so agents and coding tools can operate directly on CRM data without using the browser UI.
- Includes:
  - ~60 MCP tools, ~30 preconfigured coding skills, support for major coding agents, and an experience layer that renders outputs across Slack, Teams, ChatGPT, Claude, Gemini, etc.
  - Agent Exchange marketplace and a builder fund to grow the ecosystem.
- This effectively makes Salesforce **agent infrastructure** for RevOps and CRM: any compatible agent can now read/write CRM data under Salesforce’s trust, permissions, and business logic.
- Scores highly on the filter: plugs into existing orgs, is open to other agents, owns critical revenue data, has ecosystem momentum, and is built for stacking.

## Case 3: Microsoft Copilot Wave 3 (Co-work + Work IQ)

- **Co-work**: long-running, multi-step agent execution integrated into Microsoft 365, built with Anthropic-style agent tech.
- **Work IQ**: the data layer giving Copilot access to email, meetings, chats, files, SharePoint, identity, permissions, org context.
- Strengths:
  - Deep, native access to the Microsoft 365 graph, strong governance and permissions.
  - Ideal for knowledge work primarily inside Outlook, Excel, Teams, SharePoint, PowerPoint.
- Weaknesses:
  - Relatively closed to external agent frameworks.
  - Not suited for heavy production engineering workflows (teams prefer dedicated coding agents).

## Case 4: Kimi K 2.6 (Open-Weights Swarm Agent Model)

- Open-weights multimodal agent model under a modified MIT license with a **300-agent swarm** architecture and up to ~4,000 steps.
- Strong benchmark performance for coding and long-horizon agentic tasks.
- Best fit:
  - Developer teams able to self-host, fine-tune, and build their own agent infrastructure, wanting to avoid closed-lab lock-in.
- Poor fit for typical Western enterprise business users as a hosted SaaS tool due to data trust, governance, and integration gaps.

## Case 5: Perplexity Personal Computer (Mac)

- Evolves “Perplexity Computer” into a local **digital worker**:
  - Local file access and editing, local browsing, voice orchestration, deeper background task control.
  - Uses Claude Opus 4.7 as default orchestrator.
- Strong for **research-heavy tasks** that end in an artifact: market/competitive research, sales prospecting, financial analysis, doc review, ops reports.
- Weaker for:
  - Team-governed recurring workflows needing structured ownership.
  - Work fully embedded in Microsoft 365 or Salesforce graphs.

## Anthropic / Claude as a Layered Strategy

- Claude appears in three ways:
  1. **Direct product** (Claude chat, Claude Code).
  2. **Embedded engine** in others (Microsoft Copilot, Salesforce Agentforce, Perplexity).
  3. **Managed agent infrastructure** (Claude Managed Agents) for teams needing runtimes without building all infra.
- The question becomes: which wrapper around Claude (or any model) fits the job—direct, embedded, or managed?

## How to Decide: Three Routing Questions

1. **Stay in your default agent when** the model is central and integration is secondary (coding, long-context reasoning, custom workflows you control directly).
2. **Use a wrapper running the same model when** it gives you unique data/workflow integration you can’t replicate (e.g., Copilot with Work IQ, Salesforce with Claude inside, Perplexity with Claude orchestrating research and artifact creation).
3. **Use a different model/product when** its surrounding product, graph, and governance outweigh marginal model differences (e.g., Workspace Agents in Slack, Google Workspace with Gemini, self-hosted Kimi for infra control).

## Practical Guidance and Literacy

- Switching wholesale is expensive: prompts, memory, context, and habits don’t transfer cleanly.
- The costly mistake isn’t having multiple tools; it’s routing work to the wrong tool.
- Agents are heterogeneous (model frontends, workflow builders, data layers, infra, research workers, control planes), so don’t compare them as if they’re one flat category.
- Use the five-question filter, prioritize infrastructure/stackability/data access, and route each task to the tool whose *shape* matches the work’s *shape*—that routing judgment is the key skill of the agent era.

