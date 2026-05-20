---
title: Google Spent a Year Stitching MCP, A2A, AG-UI Together. I/O Today.
author: Nate B Jones
source_id: 1
source_slug: nate-b-jones
url: https://www.youtube.com/watch?v=zP6TnEiueEc
published_at: '2026-05-19T14:01:16Z'
duration_seconds: null
primary_theme: tech
secondary_theme: business
relevance: 8
hook: Six emerging protocols quietly define how real AI agents will actually work and behave.
tldr: The video outlines six emerging agent protocols and argues that only three form a core, general-purpose stack today. MCP handles tools and data access, A2A handles inter-agent delegation, and AGUI enables human control over long-running agent workflows. A2UI, AP2, and X42 are important but narrower or more contested, especially in payments and UI rendering, and should be adopted based on specific workflow needs rather than hype.
caveats: Skip it if you want implementation detail or benchmarks, because this sounds more like strategic protocol mapping than a deep dive into failure modes or deployment scars.
pitch: You’re building agent infrastructure, so this is worth your time because it separates the small set of protocols that actually matter in production agent systems—MCP for tools, A2A for delegation, and AG-UI for human oversight—from the narrower standards you can ignore for now.
---

## Key Points

- Agent protocols answer three questions: what tools an agent can use, which agents it can work with, and how humans stay in control.
- MCP standardizes how agents discover and invoke external tools and data sources across systems like GitHub, Slack, and internal APIs.
- MCP was designed for high-trust environments and does not by itself make tool use safe or controlled.
- A2A uses agent cards so agents can discover, describe, and delegate work to other agents across products and companies.
- A2A introduces coordination costs and unpredictability, so it is only necessary when workflows truly require delegated expertise or authority.
- AGUI targets human oversight of long-running, non-deterministic agents by supporting streaming state, approvals, steering, and inspection beyond simple chat UIs.
- A2UI constrains agent-generated interfaces to structured, declarative components, solving part of UI safety but not the broader human control problem.
- AP2 and X42 both address payments for agents, but AP2 focuses on user-authorized commerce while X42 focuses on machine-to-machine resource payments over HTTP.

## Notes

## Overall framing: why agent protocols matter

- The talk frames Google I/O’s flashy agent demos as less important than the underlying “substrates” that make agent systems work.
- Six protocols are highlighted: MCP, A2A, AGUI, A2UI, AP2, and X42.
- The claim: only three of these are emerging as a broadly applicable “core stack,” while the others are narrower, contested, or domain-specific.
- Protocols are not just plumbing; they directly shape customer experience and constraints for agent products.

The speaker reduces the protocol landscape to three core questions:
1. What can the agent use? (tools and data)
2. Who else can the agent work with? (other agents)
3. How does the human stay in control while the agent is working? (interaction and oversight)

Three protocols map directly to these questions:
- MCP → tools/data layer.
- A2A → agent coordination layer.
- AGUI → human interaction/control layer.

The remaining three sit in narrower slices:
- A2UI → agent-generated UI rendering.
- AP2 → agent-led payments and authorization.
- X42 → machine-to-machine payments at the HTTP layer.

---

## MCP: tool and data layer

- Before MCP, every integration between an LLM-based agent and a work system (GitHub, Slack, Drive, Postgres, Stripe, Linear, Salesforce, internal APIs, calendars) was custom glue.
- Each integration required bespoke tool definitions, auth patterns, parameter schemas, and error handling.
- MCP standardizes this pattern: a server exposes tools and resources, an agent host connects, and the model gets structured descriptions of capabilities.
- This allows “composable” capabilities without every agent platform rebuilding all connectors.
- Adoption is broad: Cloud Desktop supports local MCP servers, many agent tools (including Codeex) support it, and there are reportedly 14,000+ MCP servers.

### MCP’s security and trust model

- It is tempting to treat MCP as making tool use “safe” because it’s a standardized interface, but it does not.
- Tool access equates to arbitrary code execution and arbitrary data access, which is the point of MCP but also its risk.
- MCP was created for high-trust environments where agents can use tools freely; it does not embed a security posture.
- Invariant Labs has published research on “tool poisoning” attacks, where malicious instructions are hidden in tool descriptions or metadata exposed via MCP.
- These malicious instructions can influence the agent via the same metadata used for tool discovery and invocation.
- Therefore, tool access is not a simple feature toggle; it’s a security boundary.

### What teams must still solve around MCP

- Teams exposing MCP servers must still define:
  - Scopes: which tools and which data an agent can see in which contexts.
  - Approval flows: when human confirmation is required before tool use.
  - Audit trails: how actions are recorded and reviewed.
- MCP “gets the agent close to the work”; it does not decide if the agent should do the work.
- Secure agents require complementary designs in scopes and approvals; these are not inherent to MCP.

---

## A2A: agent delegation and coordination

- Once an agent can act via MCP, a second problem appears: no single agent can know or do everything.
- Work is distributed by domain, expertise, permissions, and ownership:
  - Procurement agents might need supplier agents.
  - Travel agents might need hotel agents.
  - Finance agents might need tax agents.
  - Software agents might need security-review agents.
- A2A is the coordination layer that lets agents reason about this distribution and delegate.

### Agent cards as operating contracts

- The central primitive is the “agent card.”
- An agent card describes:
  - What the agent is.
  - What it does and which skills it exposes.
  - Where it is reachable.
  - How another agent should interact with it.
- The agent card acts as a first version of an operating contract: terms, interfaces, responsibilities.

### Ecosystem and cross-boundary delegation

- Google launched A2A with many partners (Atlassian, Box, Cohere, MongoDB, PayPal, Workday, and more than 50 organizations overall).
- The list of partners matters because A2A only realizes its value if agents can truly delegate across product and company boundaries.
- The goal is discoverable delegation across the ecosystem, not isolated “agent swarms” inside a single product.

### Tradeoffs and when A2A is appropriate

- Coordination has real costs:
  - New latency and failure surfaces.
  - Additional permission and observability challenges.
  - Less predictability in workflows when one agent asks another to do work.
- A2A is not appropriate for every product, e.g., products with a small, self-contained tool set may not need delegation.
- The crucial design question: does this workflow require delegated expertise or authority outside the primary agent?
- If yes, teams must specify ahead of time:
  - What the agent can say about itself.
  - What it can accept from others.
  - What it cannot share.
  - What requires human approval.
  - How downstream results get validated.
- Agent cards help standardize part of this, but a full control layer is still missing.

---

## AGUI: human control and interaction layer

- AGUI is often misinterpreted as just a way for agents to drive UI components, but the speaker frames it differently.
- Properly understood, AGUI is about enabling trust and control for long-running, non-deterministic agents that affect external systems.

### Why chat UIs and traditional apps are insufficient

- Long-running agents need more than a final answer; users must:
  - Observe the agent’s ongoing work.
  - Approve sensitive steps.
  - Correct course midstream.
  - Inspect state.
  - Understand why the agent is waiting.
- Traditional web apps are built for request/response, not streaming, evolving workflows:
  - They don’t handle agents discovering new info mid-task well.
  - Chat UIs alone also fail to express complex, multi-step workflows with approvals and state.

### AGUI as candidate human control layer

- AGUI is positioned as an open candidate protocol for this human control layer.
- The docs emphasize features agent apps need:
  - Streaming and shared state between front-end and back-end.
  - Front-end tool calls with back-end tool rendering.
  - Custom events and steering interactions.
  - Sub-agent composition.
- Many teams will ignore this layer until agents are doing real work that affects real money or operations, then scramble for:
  - Approval buttons.
  - Logs.
  - Progress indicators and status views.

### Core design problem AGUI targets

- None of those UI components alone solve the deeper issue: correctly placing control points.
- Teams must understand:
  - What the agent is trying to do.
  - What it is waiting for.
  - At which steps users must approve, deny, edit, or cancel.
- The speaker argues AGUI belongs with MCP and A2A in the core stack, even if the exact protocol winner is not settled.
- AGUI itself may or may not win; a close cousin might, but the human control layer is essential.
- Without it, agents that “can’t show their work” build up supervision debt for humans.

### Ecosystem links

- The Substack article (not detailed in the transcript) reportedly connects AGUI to ecosystems like LangGraph, CrewAI, Amazon Bedrock Agent Core, PydanticAI, Mastra, and CopilotKit.
- If choosing a framework, you are encouraged to study how it aligns with AGUI-like control needs.

---

## A2UI: agent-generated interfaces

- A2UI is Google’s project for safe agent-generated UIs.
- Naively allowing a remote agent to send arbitrary HTML or JavaScript is framed as a security disaster.
- A2UI instead sends a structured, declarative UI representation.
- The client renders UIs using trusted components, and the agent can only request components from an approved catalog.
- This prevents arbitrary interface code execution while allowing flexible, generated experiences.

### Why A2UI is not part of the “core stack” in this framing

- A2UI addresses one slice: how generated interfaces are rendered safely.
- It does not attempt to solve the larger human control problem that AGUI targets.
- Therefore, A2UI is seen as useful and helpful for some generated experiences but narrower in scope.
- Many agents may rely more heavily on the broader control substrate than on A2UI specifically.

---

## AP2 and X42: payments for agents

### AP2: agentic payments with user authorization

- AP2 is Google’s agentic payments protocol with more than 60 collaborators.
- Collaborators include global players such as American Express, Coinbase, Mastercard, PayPal, Salesforce, UnionPay, Worldpay, and others.
- Despite the impressive list, in payments a big collaborator list does not automatically make something a final standard.
- AP2 centers on the “mandate,” a cryptographically signed proof of what the user authorized.
- AP2 tackles a core problem in agentic commerce: how the ecosystem can know that an agent was authorized to make a purchase.

### X42: HTTP-native machine-to-machine payments

- X42 is Coinbase’s HTTP-native payment protocol, with Cloudflare as an adopter.
- It targets agent-to-agent payment for resources.
- Examples: an agent pays for an API call, data source, document, or benchmark run.
- The design aims to avoid setting up accounts or negotiating subscriptions for every resource.

### Relationship between AP2 and X42

- They are adjacent but tackle different problems:
  - AP2 is about commercial trust and verifying user authorization.
  - X42 is about settling payments for resources between agents programmatically over HTTP.
- Payments as a domain are so valuable that many competing protocols and approaches are emerging.

### Wider payment ecosystem and implications

- Beyond AP2 and X42, other initiatives include:
  - Stripe’s work on agent-auth flows and human trust in agentic commerce.
  - Mastercard’s “agentic tokens.”
  - Visa’s “intelligent commerce.”
  - American Express’s agentic commerce developer kits.
  - PayPal’s support for AP2 plus its own commerce layer.
- The speaker highlights Stripe’s suggested pattern: send users to a link to get an authorization token, creating a smooth, trust-focused experience.
- For builders, payment protocol choice is framed as a customer experience decision, not just a technical one.
- Teams must design for users who need to trust agents with their wallets and still feel secure about authorization and completion.

---

## How substrates shape customer experience

- Protocols embed assumptions and defaults that affect real customer experience.
- When tasked with “shipping an AI strategy” or “making an AI agent,” teams must first clarify the actual workflow: support triage, procurement, sales territory analysis, renewal preparation, etc.
- Once the workflow is clear, they must ask how each substrate affects the intended experience.

### Mapping workflows to layers

- MCP: Often necessary when agents must work “close to the work” in real systems.
- A2A: Needed if workflows require cross-agent reasoning or delegation to external specialists.
- AGUI: Critical for workflows that require long-running, human-approved agent processes.
  - Example given: a CSM viewing a packet being assembled for a customer and deciding on-the-fly whether to include billing context.
- A2UI: Useful where the agent must render specific structured visualizations (usage charts, contract summaries) with guarantees about component authenticity.
- AP2: Relevant when the agent must spend money or authorize transactions on behalf of a user.
- X42 (or similar): Relevant when the agent must autonomously pay for resources programmatically.

### Payment protocols and biased defaults

- Payments vary by geography, methods, and user comfort with agents and compute.
- A given payment experience may be biased toward US payment methods or assumptions such as “humans don’t make micropayments.”
- Builders are encouraged to inspect seemingly boring protocol details:
  - How fees are handled.
  - How returns and refunds are handled.
  - How delivery is handled.
  - How authorization is handled and how long it lasts.
- Example: if a protocol assumes short-lived authorization tokens and users dislike frequent reauthorization, friction and frustration will result.
- Protocols can be opinionated in ways that suit some customers and workflows but not others; teams must align these opinions with their own customers.

---

## Six design questions for teams

The speaker proposes six questions to connect protocol choices to concrete workflows:

1. What tools and data does the agent need, and does it therefore require MCP-level integration?
2. What other agent surfaces or specialists must it call, suggesting an A2A need?
3. Where must the user approve, edit, interrupt, or steer the work, implying an AGUI-style control layer?
4. Does the workflow need structured UI beyond text, which might require A2UI?
5. Does the agent need to spend money or authorize transactions, indicating an AP2-like solution?
6. Does the agent need to autonomously pay for resources programmatically, pointing to X42 or similar protocols?

The speaker argues that teams are typically over-focused on choosing the model and under-specified on the operating surface around that model:
- They may know which LLM they want.
- They often have only a vague idea of which tools the agent should see.
- They may prototype API calls but lack a clear interaction model for user approvals.
- They may imagine multiple agents coordinating but have no enforcement or validation mechanisms.

The “actual work” is to answer these substrate and control questions, not only to pick models.

---

## Looking ahead: Google I/O and stack coherence

- The talk closes by linking back to Google I/O.
- The suggested lens for watching I/O: whether Google can make the agent stack feel like a single operating model.
- Questions raised:
  - Does Gemini Enterprise coherently stitch A2A agents, MCP tools, A2UI interfaces, and AP2 payments into a buildable target?
  - Or does I/O add yet more standards and acronyms without a unified operating surface?
- The speaker argues 2026 will be remembered as the period when agent workflows for developers unlocked, making the present a “golden time” for building important agent systems.
- Teams that learn to build against protocols in ways that shape real customer experiences, rather than just adopting acronyms, are framed as likely winners.

