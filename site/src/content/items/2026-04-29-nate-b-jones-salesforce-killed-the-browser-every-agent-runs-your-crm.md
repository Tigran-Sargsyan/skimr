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
relevance: 7
hook: Use a five-question filter to cut through the AI agent hype and pick infrastructure.
tldr: The video argues that most AI agent launches are noise unless they improve infrastructure around your existing tools and data. It offers a five-question filter focused on integration, openness, data access, ecosystem, and stackability. Using this lens, it evaluates Workspace Agents, Salesforce Headless 360, Copilot Wave 3, Kimmi K 2.6, and Perplexity Personal Computer, then reframes “switching” tools as layering the right products for each job.
caveats: Skip it if you want deep technical architecture, eval data, or production scars; this sounds more like strategic product commentary than hands-on systems analysis.
pitch: You work on LLM agents and AI infrastructure, so this is worth your time as a fast framework for separating real agent plumbing from hype and for thinking about how agents should layer on top of existing tools, permissions, and data graphs.
---

## Key Points

- Most important agent launches are infrastructure that extends existing tools, not flashy standalone destinations.
- A five-question filter evaluates agents by integration, openness, data access, ecosystem strength, and stackability.
- Workspace Agents are OpenAI’s answer for shared, repeatable cross-tool workflows inside ChatGPT and Slack.
- Salesforce Headless 360 exposes the CRM stack as APIs and MCP tools so any agent can operate Salesforce data.
- Microsoft Copilot Wave 3 is powerful for Microsoft 365-native work because of deep graph and permissions access.
- Kimmi K 2.6 mainly matters as open-weights agent infrastructure for dev teams, not as a hosted enterprise product.
- Perplexity Personal Computer targets research-heavy workflows that end in artifacts, enhanced by local Mac integration.
- The real strategy is layering specialized agent products around data graphs and workflows, not switching to one default agent.

## Notes

## Why You Need a Filter for Agent Hype

Teams are overwhelmed by constant AI agent launches, benchmarks, and polished demos, and the dominant feeling is exhaustion, not excitement. The critical question is no longer “what launched this week?” but “which of these deserve my team’s attention?”

The core claim: the conversation has shifted from model quality to infrastructure. What matters is not the loudest demo or best benchmark, but which launches change:
- What your existing tools can reach
- What your agents can actually do
- How easily your team can stack and combine systems

The framing move: stop thinking in terms of switching from one agent to another and start thinking in terms of layering different products and infrastructure around your existing work.

---

## The Five-Question Filter

The speaker uses a five-question filter to evaluate any agent launch:

1. **Does it plug into tools my team already uses, or force a new environment?**  
   Infrastructure that reaches into where work already lives is valuable; new destinations requiring migration are costly. Migration is historically the most expensive ask in SaaS.

2. **Can other agents build on top of it, or is it closed?**  
   If you can point tools like Claude Code, CodeEX, Cursor, or internal agents at it, it’s infrastructure. Closed, standalone experiences are features. Features commoditize; infrastructure compounds.

3. **Does it own or access data I care about?**  
   Agent quality is downstream of data access. A mediocre agent with full customer history can beat a brilliant agent with empty context, which explains why Copilot is potent inside 365 and Salesforce inside revenue orgs.

4. **Is there an ecosystem forming around it?**  
   Ecosystems show staying power: marketplaces, SDKs, partner programs, dev tools, regular releases. A product with a real marketplace differs from a press-release-only launch.

5. **Can I stack my agents on top?**  
   Composable releases that let you layer agents are far more valuable than standalone agents that just add one more point solution to evaluate.

Applied rigorously, this filter makes most launches ignorable. Those that pass merit a serious afternoon of evaluation.

---

## Case 1: ChatGPT Workspace Agents

Workspace Agents are OpenAI’s shift from personal assistants to reusable team work units.

**What they are:**
- Shared, CodeEX-powered agents for teams
- Running in the cloud
- Able to work across connected tools
- Accessible via ChatGPT or Slack
- Schedulable and suited to repeatable business workflows, not one-off chats

**Conceptual shift:** from “I have a personal helper” to “our team has reusable agents,” e.g.:
- Product feedback routing
- Weekly metrics reporting
- Risk screening
- Software request triage

These workflows are hard because they span Slack, email, docs, sheets, ticketing systems, and human memory. Workspace Agents simplify automation across that mess.

**Where they fit the filter well:**
- Strong for **recurring, cross-tool workflows** initiated from ChatGPT or Slack
- Good when conversational builders, Slack surfaces, cloud execution, permissions, approvals, and shared directories matter more than direct control of systems of record

**Where they’re weaker:**
- Workflows deeply native to Salesforce: Salesforce has data advantage
- Workflows deeply native to Microsoft 365: Copilot has data advantage
- Frontier coding work: coding agents themselves matter more than the workspace shell

The right framing: Workspace Agents don’t replace all agents; they are OpenAI’s best answer for shared, repeatable, cross-tool workflows run from ChatGPT or Slack.

---

## Case 2: Salesforce Headless 360 – “Salesforce Killed the Browser”

Headless 360 is easy to overlook because it sounds like plumbing, but its importance is precisely that it is plumbing.

**Core move:** Salesforce is exposing essentially every major capability as:
- APIs
- MCP tools
- CLI commands

Result: the browser UI is no longer the only way to use Salesforce. Agents and tools can now:
- Reach into Salesforce directly
- Use live org context in coding agents
- Trigger workflows without human clicks

Parker Harris framed the goal as: “Why should you ever log into Salesforce again?” Headless 360 is the answer.

**Concrete elements and numbers:**
- 60+ new MCP tools
- 30+ preconfigured coding skills
- Support for Claude Code, Cursor, CodeEX, Windsurf
- An experience layer decoupling what an agent does from where output appears (Slack, mobile, Teams, ChatGPT, Claude, Gemini, any MCP client)
- Agent Exchange: a marketplace combining Slack apps, Agentforce agents, tools, MCP servers
- A builder fund backing the ecosystem

**Filter evaluation:**
- Plugs into an existing system where enterprises already live (CRM/RevOps)
- Explicitly open to external agent frameworks
- Owns the data revenue teams care about (customers, pipeline, workflows, permissions)
- Has a real ecosystem and funding
- Designed for stacking other agents on top

This is Salesforce attempting to be **infrastructure for the agent economy**, not just shipping an agent.

**Implications for teams running RevOps on Salesforce:**
- The question shifts from “Agentforce vs Workspace Agents for CRM?” to “Which existing agents can now do CRM work, since Salesforce exposed its data and logic?”
- Many agents may now:
  - Build Salesforce apps with live data
  - Update opportunities via permissions-respecting APIs
  - Trigger Salesforce flows
  - Act on CRM data from Slack without copy-paste

A key detail: Agentforce 5 uses Claude Sonnet 4.5 as the default coding model, with GPT‑4.5 (GPT‑5 in video language) as an option. This exemplifies Anthropic’s strategy: not just a product, but an embedded agent layer inside others’ stacks.

---

## Case 3: Microsoft Copilot Wave 3 (Co‑work and Work IQ)

Copilot’s significance is often underestimated in agent conversations.

**Two key pieces:**

1. **Copilot Co‑work** – long-running, multi-step agent execution inside Microsoft 365, built in collaboration with Anthropic to bring “Claude-style” agent behavior into the Copilot canvas.

2. **Work IQ** – the data layer, giving Copilot:
   - Email
   - Meetings
   - Chats
   - Files
   - SharePoint pages
   - Identity
   - Permissions
   - Org context

The point and moat is data access: Copilot doesn’t just see files via a connector; it operates within the organizational graph and identity system of Microsoft 365.

**Filter perspective:**
- Very strong for Microsoft 365-native companies on data access, permissions, and governance
- Especially strong when work lives in Excel, Outlook, SharePoint, Teams, PowerPoint, and adjacent tools

**Weaknesses:**
- Less open to external agent frameworks compared to Salesforce’s MCP approach
- Ecosystem is more closed
- Not attractive for serious production engineering workflows; engineering teams prefer tools like CodeEX or Claude Code

So Copilot Wave 3 **passes the filter** for Microsoft 365-centric, non-production-engineering workflows, and **fails** for organizations needing cross-ecosystem composability or heavy coding agent infrastructure.

The right question is not “Is Copilot good?” but “For which shapes of work is Copilot the right layer?”

---

## Case 4: Kimmi K 2.6 – Open-Weights Agent Infrastructure

Kimmi K 2.6 is a technically impressive open-weights model from Moonshot, but its strategic relevance is different from enterprise SaaS products.

**What it is:**
- Open-weights model under a modified MIT license
- Framed as a native multimodal agentic model
- Built for long-horizon coding, design, autonomous execution, and swarm orchestration
- Headline: swarm architecture of 300 sub-agents coordinating across up to 4,000 steps
- Strong coding and agentic benchmarks
- Self-hostable, enabling teams to keep data local and avoid closed providers

**Filter evaluation for typical enterprise buyers:**
- Does not own your work graph
- Not embedded in 365 or Salesforce
- Lacks the Western enterprise connector story
- Not solving, for most companies, the “route recurring work through our existing tools” problem

Instead, Kimmi 2.6 solves a **developer infrastructure problem**: giving dev teams open-weight, long-horizon agent capabilities they can run themselves.

**Two distinct user profiles:**
- **Self-hosted dev teams:** Kimmi is compelling as infrastructure; open weights, autonomy, inspectability, and freedom from closed labs matter.
- **Casual hosted users:** For a business team considering a hosted Kimmi product for sensitive work, the deciding factors are trust, governance, data boundaries, connectors, and fit with their environment—not raw benchmark scores. Here Kimmi is usually not the right answer.

Strategic takeaway: open-weight agent models are advancing fast outside Western labs, giving capable teams credible new options. But for immediate sales/ops/finance/product-team use, Kimmi is generally not the default tool to evaluate.

---

## Case 5: Perplexity Personal Computer (Mac)

Perplexity Computer already existed as a digital worker but felt cloud-bound and detached from the user’s actual machine.

**Problem before the Mac rollout:**
- Strong search, reasoning, and work production
- Weakness: did not fully live on the device; lacked deep local file and app access

**What the Mac “Personal Computer” adds:**
- Local file editing
- Local computer use
- Local browsing through Comet
- Voice orchestration
- Deeper background control of work

Perplexity made Claude Opus 4.7 the default orchestrator model, with other model options available. The product category crystallizes as a **digital worker** that:
- Researches and reasons
- Browses
- Edits files
- Creates artifacts
- Moves across connected apps

**Filter evaluation:**
- Strong on connectivity and chaining: research, analysis, docs, slides, email drafts, code, schedules, follow-ups
- Stronger now on local access via Mac integration
- Moderate on ecosystem and team-level governance; it’s not a Slack-native shared workflow system or an embedded enterprise graph like Copilot or Salesforce MCP

**Where it shines:**
- Research-heavy work that ends in an artifact, e.g.:
  - Competitive intelligence
  - Market research
  - Sales prospecting
  - Financial analysis
  - Document review
  - Weekly operations reports

**Where it falls short:**
- Shared, recurring team processes needing governance, ownership, and repeatability
- Deeply native 365 or Salesforce workflows where the internal graph matters more than external research

Perplexity is best viewed as an artifact-producing research worker, not an enterprise control plane.

---

## Matching Tool to Job: Routing Work Instead of Forcing One Product

Across these five examples, each tool is suited to specific job shapes:
- **Workspace Agents:** shared, recurring cross-tool workflows in ChatGPT/Slack
- **Salesforce Headless 360:** agent access to CRM data, business logic, and RevOps infrastructure
- **Copilot Co‑work:** Microsoft-native knowledge work where Work IQ’s graph and permissions are decisive
- **Kimmi K 2.6:** open-weight agent infrastructure for teams capable of self-hosting and building their own stack
- **Perplexity Personal Computer:** research-heavy workflows that culminate in a deliverable

Many teams mismanage this by buying one license and forcing it to cover all use cases, to avoid adding tools. The real cost, however, is **misrouting the work**, not having multiple tools.

Examples of better routing:
- Research-heavy deliverable → Perplexity: competitor analysis, news synthesis, market mapping, draft reports, human review
- Microsoft 365-centric org → Copilot: operate in the native emails, meetings, docs, sheets, and sites
- Coding/model-centric work → direct Claude, Claude Code, CodeEX, Cursor, or similar coding-centric environments
- RevOps on Salesforce → Headless 360: let many agents act inside Salesforce where customer and pipeline data already live
- Shared cross-tool workflows in ChatGPT or Slack → Workspace Agents, especially when needing scheduling, shared ownership, and iterative improvement

The skill to develop is routing work to the right agent layer rather than standardizing on a single agent for everything.

---

## The “Switching” Question Is Really About Layers

Teams keep asking “When should I switch from Claude/ChatGPT/Copilot/Gemini?” That question is misleading because the market is moving toward layers, not a single default agent.

Anthropic’s trajectory illustrates this layering:
- **Direct Claude:** model is the product
- **Embedded Claude:** hidden inside other vendors’ products that own workflows and data (e.g., Copilot Co‑work, Salesforce Agentforce, Perplexity Computer)
- **Managed Claude (Claude Managed Agents):** Anthropic runs the agent infrastructure layer for teams building long-running agents, without chat being the main interface

So often the right question is “Which wrapper around Claude is right for this job?” The same logic applies for other providers.

---

## Three Practical Questions for Layering

Instead of “switching,” use three questions to decide how to use models and wrappers:

### 1. When should you stay in your default agent’s direct product?

Stay direct when the model is the center of the work and integrations are secondary, such as:
- Coding
- Long-context reasoning
- Novel research
- Custom agents where you own workflow logic
- Tasks requiring direct control over model behavior

For Claude users, this explains why Claude Code is crucial for engineering teams. For ChatGPT users, direct ChatGPT or CodeEX is appropriate for open-ended reasoning. For Copilot users, this is often when they should **leave** Copilot, because Copilot’s strength is integration more than the model itself.

### 2. When should you use a different product that runs the same model?

Use the wrapper when it provides data access or workflow integration you cannot realistically replicate yourself:
- Copilot with Work IQ: Anthropic-style agent execution against the Microsoft 365 graph in a way connectors can’t match
- Salesforce with Claude inside: inherits Salesforce metadata, business logic, trust, and permissions
- Perplexity with Claude as orchestrator: gives a research-to-artifact workflow different from blank Claude chat

Here you aren’t “switching from” the model; you’re **moving the model** into a product layer that has the right data fabric.

### 3. When should you pick a product that uses a different model entirely?

Use a different model when the product’s surrounding layer matters more than marginal model quality:
- ChatGPT Workspace Agents for Slack-native recurring workflows, even if another model might write slightly better text
- Google Gemini in Workspace for teams that live in Google’s graph
- Self-hosted Kimmi K 2.6 for dev teams wanting open-weight agent capability without reliance on closed labs

The model still matters, but the wrapper, graph, permissions, connectors, workflow surfaces, and ecosystem increasingly matter more.

---

## Switching Costs and the New Literacy

Switching agents is costly:
- Prompts do not transfer smoothly
- Memory and context don’t port cleanly
- Skills are more portable than before but not fully plug-and-play
- Team habits around specifying work are fragile; moving tools can reset learning curves

Therefore, don’t switch casually. Instead:
- Keep your default where it excels
- Add specialists where they clearly win
- Build judgment about routing work according to task shape

This judgment—knowing how to route tasks across layered agents and infrastructure—is described as the new literacy of the agent era.

---

## Final Framework: How to Evaluate Agent Launches This Year

The key is to avoid lumping everything called an “AI agent” into one category or comparison chart. Agent launches span:
- Model products
- Workflow builders
- Enterprise data layers
- Open-weight infrastructure
- Research workers
- Wrappers around other models
- Control planes for existing corporate systems

They can’t be compared as if they’re solving the same job.

Instead, use the five-question filter:
1. Does it plug into tools your team uses?
2. Does it allow other agents to build on top?
3. Does it own or access data you care about?
4. Is an ecosystem forming around it?
5. Can you stack agents on top?

If the answer is yes across these, the launch deserves attention. If not, it may still be impressive but likely isn’t for your team right now.

So for the rest of the year:
- Filter for **infrastructure over features**
- Filter for **ecosystems over demos**
- Filter for **stackability over walled gardens**
- Filter for **data access over benchmarks**
- Match the **shape of the work** to the **shape of the tool**

Teams that master routing work across these layers will compound faster than those chasing whichever agent had the loudest launch.

