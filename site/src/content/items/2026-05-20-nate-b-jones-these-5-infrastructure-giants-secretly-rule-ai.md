---
title: These 5 Infrastructure Giants Secretly Rule AI
author: Nate B Jones
source_id: 1
source_slug: nate-b-jones
url: https://www.youtube.com/watch?v=woGB2vr5wTg
published_at: '2026-05-20T14:01:40Z'
duration_seconds: null
primary_theme: tech
secondary_theme: business
relevance: 7
hook: Five under-the-radar infrastructure layers will quietly decide which AI agents reach production.
tldr: Model providers do not decide whether agents ship; infrastructure operators that govern execution, identity, data, payments, and observability do. Control moves to companies like Cloudflare, Oso/Okta, Snowflake/Databricks, Stripe, and Datadog that define how agents act safely at scale. Teams must deliberately choose control points across seven layers—runtime, identity, data, tools, payments, observability, and kill switches—before putting serious agents into production.
caveats: Skip it if you want hard numbers, architecture diagrams, or battle-tested implementation details, because this reads more like industry positioning than an engineer's postmortem.
pitch: If you're thinking about shipping agents in production, this gives you a useful map of the control points—runtime, identity, data, observability, payments, and kill switches—that actually matter beyond the model layer.
---

## Key Points

- Physical compute and GPUs are necessary for AI scale but are not sufficient to govern agents in production.
- Runtime environments like Cloudflare Workers and AWS Agent Core become control points for stateful, long-lived agents.
- Identity providers such as Oso, Okta, WorkOS, and Entra must model delegated, revocable authority for agents.
- Data platforms like Snowflake and Databricks aim to be the governed semantic layer where agents reason safely with enterprise data.
- Stripe is positioning itself as the default operator for agentic payments, fraud controls, and commerce workflows.
- Card networks like Visa and Mastercard want agent payments to clear through their existing institutional trust rails.
- Observability platforms such as Datadog, LangSmith, BrainTrust, and Langfuse trace agents as work, not just API calls.
- A real kill switch must exist across runtime, identity, gateways, payments, and workflows, not only at the model level.

## Notes

## Big Idea: Power Shifts from Models to Control Infrastructure

- Model builders like OpenAI and Anthropic are only one part of the “agent economy.”
- The real gating factor for shipping agents is the infrastructure that decides where agents run, who they act for, what they can know and change, what they can spend, and who can stop them.
- Compute, GPUs, and data centers determine whether AI can be served at scale, but not whether agents are governable.
- As agents start doing real work, governance and control become the main bottlenecks.

## Why Compute Alone Is Not Enough

- Physical infrastructure (GPUs, power, networking, capex) matters for throughput, but it doesn’t answer governance questions.
- Key questions—where agents run, what they remember, who they represent, what they can spend, and who can interrupt them—must be solved at an infrastructure layer beneath the models.
- The “control layer” underpins whether agents can safely act in production environments.

## Runtime as a Control Point (Cloudflare, AWS, Vercel)

- Models are stateless: they take a prompt and return a response; conversations only persist if the client sends context each time.
- That stateless pattern is insufficient for agents that must remember past actions, resume after disconnects, run on schedules, recover from tool failures, or maintain real-time user connections.
- Real agents need a runtime with built-in memory and execution semantics.

### Cloudflare’s Runtime Bet

- Cloudflare’s Agents SDK runs each agent on a “durable object,” effectively a stateful microserver.
- Each durable object has its own SQL database, WebSocket connections, and scheduling.
- From this runtime, agents can:
  - Call tools and expose tools via MCP.
  - Schedule tasks and coordinate with sub-agents.
  - Browse the web and react to events.
- This turns Cloudflare’s runtime into a first-class control surface for agents.

### AWS and Vercel Variants

- AWS Agent Core inside Amazon Bedrock bundles runtime, memory, identity, gateway, browser, code interpreter, and observability into a stack.
- Vercel’s AI Gateway focuses on routing across models, enforcing budgets, monitoring, and load balancing.
- Different vendors emphasize different levers, but all treat runtime as a key control point.

### Why Runtime Sits at the Top of the Control Map

- Most production agents need durable work, deadlines, callbacks, streaming UI, tools, approvals, payments, and state.
- Because runtime shapes what is possible for identity, data access, and tools, it belongs at the top of the agent control map.

## Identity as a Control Point (Oso, Okta, WorkOS, Entra, AWS)

- Traditional identity: authenticate a human user, authorize them against app resources, proceed.
- This model breaks when agents act on behalf of humans, teams, companies, or even other agents, across many APIs.
- Agents may:
  - Call Google, Slack, GitHub, Salesforce, etc.
  - Receive approvals asynchronously while the user is away.
  - Retrieve documents where only a subset are visible to the principal.

### Oso’s Approach to Agent Identity

- Oso’s AI agent documentation covers:
  - User authentication.
  - OAuth-based API access.
  - Token vaults.
  - Asynchronous authorization flows.
  - Fine-grained authorization for RAG.
- Core mechanic: delegated authority with constraints.
  - Agents do not receive broad, permanent credentials just because a user signed in once.
  - Agents call APIs on behalf of a user under specific constraints.
  - Sensitive or long-running actions require explicit consent.
  - Token storage does not expose raw secrets directly to agents.
  - RAG retrieves only documents the user is authorized to access.

### Other Identity Players

- Okta, WorkOS, Microsoft Entra, AWS Agent Core Identity, and others converge on similar agent-identity problems.
- The most dangerous agent is often not the most capable one but the one with unclear authority boundaries.
- Risks arise when it’s unclear whether the agent acts as the user, the company, the application, or itself, and whether permissions persist or generalize beyond the original request.

### Why Identity Becomes Critical as Agents Transact

- Loose identity is manageable when agents only draft text.
- It becomes unacceptable when agents can transact, deploy, refund, schedule, provision, or make binding commitments.
- Serious agent products need clear answers to:
  - Who is the principal?
  - What can be delegated?
  - What can be revoked and how quickly?
  - What does the audit log show?
- Without robust identity, agents will hit adoption ceilings in serious organizations.

## Data as a Control Point (Snowflake, Databricks, BigQuery/Gemini)

- An agent’s usefulness is bounded by the data it can safely interpret.
- Generic agents often mishandle data:
  - Joining wrong tables and trusting wrong columns.
  - Misunderstanding metrics or using stale documents.
  - Answering confidently from ungoverned context or assumptions.
- These are data control failures, not pure model failures.

### Snowflake’s Cortex Agents

- Snowflake positions its platform as the governed perimeter where agents reason over data.
- Cortex Agents operate across structured and unstructured data:
  - Cortex Analyst handles structured queries.
  - Cortex Search handles unstructured retrieval.
  - The agent routes between them inside Snowflake’s governance boundary.
- Key idea: govern the “distribution of meaning.”
  - Data warehouses encode the business’s shared meaning: revenue, customers, inventory, churn, margin, forecasts.
  - Agents increase the importance of this semantic layer, not reduce it.

### Why Semantic Governance Matters

- Agents must distinguish, for example:
  - Current revenue vs forecast revenue.
  - Public documentation vs confidential customer commitments.
- Misunderstanding such distinctions makes agents unfit for tasks like drafting board narratives or answering support queries.

### Databricks, BigQuery, and Gemini

- Databricks’s Mosaic AI Agent Framework makes a parallel bet: building, deploying, evaluating, and monitoring agents inside the same governed environment where enterprise data already resides.
- Google’s BigQuery with Gemini is the hyperscaler-native variant of this “agents inside governed data platforms” approach.
- All are doing more than adding “chat to databases”; they aim to make governed data platforms the only place agents are allowed to meaningfully reason and act.

## Payments as a Control Point (Stripe, Card Networks)

- When agents touch money, control stakes sharply increase.
- Payments are a form of institutional trust: they encode fraud management, disputes, risk, and compliance.

### Stripe’s Strategic Position

- Stripe sits at the center of online commerce, already handling:
  - Payment credentials, fraud, disputes.
  - Risk and billing.
  - Subscriptions, issuing, treasury, merchant onboarding.
- Stripe supports multiple payments protocols (e.g., AP2, X42, others) but its power comes from operating across the whole bundle.
- Stripe is rapidly defining how agents can:
  - Issue payments and refunds.
  - Get authorization.
  - Integrate with fraud mitigation.
- Stripe’s thesis: the internet economy will expand via agentic commerce, and its mission to grow online commerce makes enabling agent transactions a natural extension.
- For most startups, Stripe is the default payments partner for agents; enterprises may extend their own stacks but must match similar agentic capabilities.

### Card Networks’ Different Incentives

- Card networks like Mastercard, Visa, and American Express focus on ensuring that agent payments run on their rails.
- They want agent transactions to clear the same institutional trust chains as card transactions.
- Their competition centers on proving that agents can fit into existing fraud, dispute, and merchant onboarding systems.
- Operators move quickly because if legitimate agent transactions are not rapidly enabled, fraudulent patterns will fill the gap.

## Observability as a Control Point (Datadog, LangSmith, BrainTrust, Langfuse, AWS)

- Observability for agents is more than logging requests and responses.
- Agents fail differently from classic software:
  - They may call the wrong tool with syntactically valid inputs.
  - They might ask the right agent the wrong question.
  - They can use authorized data yet draw incorrect conclusions.
  - They can complete tasks while violating user intent.
  - They can remain within permissions yet create expensive token loops or escalate too late.

### Observing “Work,” Not Just API Traffic

- Effective observability asks:
  - What was the goal of this agent run?
  - Which tools were called?
  - Who authorized actions taken?
  - Which data sources were used?
  - Which policy blocked or allowed steps?
  - What cost was incurred?
  - Did a human ultimately accept or reject the outcome?

### Key Observability Players

- Datadog’s LLM observability traces end-to-end agent runs:
  - Prompts, responses, tool calls, retrievals.
  - Ties agent behavior to backend services and user sessions.
- LangSmith focuses on teams using LangChain or LangGraph, tracing workflows and running evals on agent performance.
- BrainTrust leads with evals: quality checks on agent outputs.
- Langfuse emphasizes open-source tracing.
- AWS Agent Core Observability supports OpenTelemetry, enabling telemetry to flow into CloudWatch, Datadog, Langfuse, and others from a single integration.
- The market is converging toward unified control planes where traces, cost, tool calls, and eval outcomes are seen in one operational view.

## The Multi-Layer Kill Switch

- A real kill switch is a multi-layer capability, not just sending “stop” to the model.
- Potential intervention points:
  - Runtime: cancel or pause agent runs.
  - Identity: revoke credentials or delegated authority.
  - Gateway: block specific tool calls or destinations.
  - Payments: freeze payment instruments or enforce spending limits.
  - Workflow frameworks (e.g., LangGraph): interrupt execution before sensitive nodes.
- If the only control is “tell the model to stop,” you lack a true kill switch.
- Thoughtful kill switch architecture spans runtime, identity, gateway, payments, and workflow layers.

## Practical Framework: Seven Questions for a Single Agent Workflow

- Start with one concrete agent use case (e.g., support refunds, customer email responses, claims processing, usage-checking agent).
- For that workflow, answer these seven questions:
  1. **Where does the agent run?**  Runtime choice (Cloudflare, AWS Agent Core, etc.).
  2. **Who is the agent acting for?**  Identity layer details—company principal, delegated user access via Oso/Okta/others.
  3. **What can it know?**  Data layer and semantic governance (Snowflake, Databricks, BigQuery, etc.).
  4. **What can it change?**  Tooling layer—read vs write access and approval requirements.
  5. **What can it spend?**  Payments layer—refund limits, approval thresholds, Stripe or internal stack.
  6. **What gets observed?**  Observability—did it violate policy, get tricked, or incur unexpected costs (LangSmith, Datadog, AWS, etc.).
  7. **Who can stop it?**  Kill switch paths—runtime cancellation, payment freeze, identity revocation, workflow interruption.
- Any “TBD” in this matrix must be addressed before production, with clear ownership; otherwise, gaps get ignored as “someone else’s problem.”
- Agents do not respect organizational boundaries, so governance models must compensate for that reality.

## Real-World Governance Challenges

- A data team lead reported agents “hacking around” existing human permission structures inside internal systems.
- After a successful run, ambiguity arises:
  - Was the agent authorized to bypass those constraints?
  - Did the human see data they should not have seen?
  - Was the agent being usefully goal-oriented but with inadequate tools?
  - Or is the organization actually okay with that degree of chaos?
- Some companies tolerate high agent freedom today, but this stance will grow riskier as agents become more capable.
- Platform teams often encounter these control issues first as capabilities deepen.

## Macro View: Who Really Decides If Agents Ship?

- Compute demand will keep rising and hyperscalers and NVIDIA will remain important.
- Models will keep improving, but they do not decide if agents ship in real businesses.
- The decisive power lies with infrastructure companies that control whether and how agents act:
  - Runtime operators (e.g., Cloudflare).
  - Identity and authority providers (e.g., Oso, Okta, Entra).
  - Data platforms (e.g., Snowflake, Databricks).
  - Payments operators (e.g., Stripe and card networks).
  - Observability and control-plane providers (e.g., Datadog, LangSmith).
- These control layers define the practical conditions for agent deployment and success in 2024 and beyond.

