---
title: Your SaaS Bill Just Got a Second Meter. You're About to Pay It.
author: Nate B Jones
source_id: 1
source_slug: nate-b-jones
url: https://www.youtube.com/watch?v=adNErrz2aA0
published_at: '2026-05-15T14:00:04Z'
duration_seconds: null
primary_theme: business
secondary_theme: tech
relevance: 7
hook: AI agents are reshaping SaaS pricing from human seats to metered machine work.
tldr: Vendors are quietly adding a second pricing meter that bills for agentic actions, not just human seats. This shift moves the commercial unit of software from users to measurable work units across systems like Salesforce, Microsoft, ServiceNow, and SAP. Builders and buyers must now negotiate agent access, meters, and policies up front or risk opaque, rent-seeking costs once agents are embedded in production workflows.
caveats: Skip it if you want deep systems engineering or hard implementation detail, because this is more about SaaS economics and vendor behavior than architecture or evals.
pitch: You should read this if you’re building AI agents or platform tooling because it spells out the new pricing and policy traps you’ll run into when agents start doing real work inside SaaS ecosystems, which is directly relevant to how you design and cost production workflows.
---

## Key Points

- SaaS vendors are introducing a second pricing meter that charges for agentic work units in addition to seats.
- Salesforce, Microsoft, and ServiceNow now bill for discrete agent-triggered actions across their platforms.
- Token-based thinking is insufficient because vendors increasingly meter workflow units, not just model usage.
- SAP’s 2026 API policy restricts unsanctioned AI agents, making agent access a contractual issue first.
- Fair agent licensing requires transparent meters, forecastable units, and different treatment for failed versus completed work.
- Rent-seeking models hide meters, bill vague AI access, and make third-party agents impractical or hostile.
- Developers must understand billing units, policy constraints, and operation types to design cost-aware production agents.
- Negotiating agent access and economics before workflows depend on agents preserves leverage and avoids double-paying seats plus opaque usage bills.

## Notes

## The Core Shift: From Seats to Metered Agent Work

For decades, SaaS economics relied on a simple pattern: convert work into seats, creating predictable recurring revenue and growth. A human user was the unit of software value, because people logged in, clicked around, updated records, and vendors charged per seat. AI agents break this logic because they can perform work in systems without “sitting” in the UI, while still relying on those systems’ data, permissions, and audit trails. 

Vendors are responding by layering a second meter on top of seats, charging for machine-executed work units. The commercial unit of software is shifting from humans using software to measurable, delegated actions taken by agents.

## Concrete Examples of the New Meters

### Salesforce: Agentic Work Units

Salesforce’s Agentforce product has reached an $800 million ARR run rate with huge year-over-year growth. It counts 2.44 billion “agentic work units” processed, explicitly distinct from tokens. Actions like updating a record, summarizing a case, answering an inquiry, executing a prompt, or running a workflow all draw from the same pool of credits. 

Under the old model, only the service rep’s seat was billed; under the new model, the rep may still have a seat, but the agent that identifies customers, retrieves history, and triggers workflows also consumes credits. The seat remains but no longer represents the full bill; the second meter measures delegated work.

### Microsoft: Hybrid Seat + Runtime Credits

Microsoft still charges per seat for Microsoft 365 Copilot, but Copilot Studio introduces an explicit runtime meter. Copilot credits measure agent usage, with different features consuming credits at different rates. Examples include standard answers, generative answers, agent actions, grounding in the Microsoft Graph, flow actions, and “premium reasoning.”

For a 100-seat company running modest agent workloads, the realistic monthly cost can rise substantially as runtime credits accumulate, especially with premium reasoning and workflows. What was once a clear per-seat price becomes a forest of credit types and trade-offs. Rapidly expanding token usage (e.g., developers burning billions of tokens monthly) compounds planning difficulty when vendors also meter non-token work units.

### ServiceNow: Operational Action Units

ServiceNow reframes its platform around “action fabric,” where agents trigger operational work via governed pathways with identity, permissions, and audit. Charged units are not generic API calls but operational actions like provisioning access, escalating incidents, kicking off onboarding, or opening change requests.

Because ServiceNow provides the operational substrate and reliability for these actions, it claims the right to meter and bill them as work units. Again, seats persist but are supplemented by a meter on governed operational actions executed by agents.

## Policy Control and Toll Booths: SAP as a Warning

New pricing rules are emerging alongside these meters, often expressed in policy language. SAP’s 2026 API policy draws a firm boundary around how customers and third-party systems can use SAP APIs. It includes restrictions on AI systems that plan, select, or execute sequences of API calls outside SAP-endorsed architectures.

Translated: if an external or internal agent (from another vendor or provider) wants to act on SAP data, the primary gate is contractual, not technical. SAP will at minimum want its own toll booth and may disallow certain agent patterns entirely. This means agent builders must understand whether their contracts even permit autonomous execution against such systems.

## Platform Incentives: Who Defines the “Work Primitive” Wins

Pricing follows platform control. The vendor that defines the new work primitive can argue it should price the work executed in that primitive. 

Salesforce defines customer workflow actions, so it meters agent actions there. ServiceNow defines much of the enterprise action layer, so it charges for governed operational actions. Microsoft sits across the productivity graph, so it wants Copilot credits for activity in that graph. SAP owns high-consequence systems, so it demands sanctioned pathways for agents, citing operational risk.

If you build agents on these platforms without understanding their incentives and metering tendencies, your agent economics effectively become controlled by the platform owner.

## What a Fair Agent License Should Look Like

A fair agent licensing model has several characteristics:

- The meter is visible, and the unit of measure is clear and intuitive.
- Customers can reasonably forecast usage based on those units.
- Failed or low-value work is not billed the same as successfully completed work.
- Third-party agents have a governed, documented path to operate, not an outright blocked path.
- Vendors distinguish between reading, drafting, writing, approving, and executing actions for agents, and bill differently when appropriate.
- Buyers can set caps, for example per department, workflow, or agent.
- Usage data is exportable so customers can analyze and optimize.
- The rate card remains stable for the contract term and does not shift mid-adoption.

These traits let buyers align costs with value and control budgets as agentic workloads scale.

## What Rent-Seeking Agent Licensing Looks Like

A rent-seeking model exhibits opposite traits:

- It charges for vague “AI access” without specifying what is consumed.
- It makes the vendor’s own agent the only practical route while treating external agents as hostile or unsupported.
- It charges customers to use their own data in their own workflows.
- It bills failed work or low-value attempts as if they were fully successful actions.
- It hides the meter until renewal, when usage is already entrenched.
- It bundles credits that expire unused while billing overages immediately.
- It disguises commercial lock-in with security or compliance language.

If your contract mixes seat counts, opaque API clauses, bot policies, and scattered AI pilots without coherent production coverage, you lack both a robust solution and a clear cost envelope.

## Developer Responsibilities: Beyond Tokens to Workflow Economics

Most agent-building teams still think primarily in terms of token costs. But as vendors meter workflow units and operational actions, the true cost structure extends well beyond tokens. A prototype may be cheap at low volume, yet become economically untenable at scale under actual contract terms.

Builders must ask:

- Does the signed API policy even permit autonomous execution by agents?
- What exactly is the billing unit: completed work, partial work, attempts, or raw tokens?
- How are different operation types billed: reading data, drafting content, writing changes, approvals, or fully executed actions?

Understanding where agents spend tokens and work units (read vs. write vs. approve vs. execute) and their blast radius in terms of value is critical. These distinctions directly affect vendor metering and therefore the viability of deploying the agent in production. An agent that treats all tool calls as equal, regardless of cost or reversibility, becomes an incident risk, not a production asset.

## Negotiating Before You Lose Leverage

The worst move is to delay negotiation until agent usage becomes mission-critical, because then turning agents off becomes painful and leverage shifts to the vendor. Vendors recognize when value has moved to agents and will price accordingly.

The better approach is to negotiate agent access and economics up front, before workflows depend on them. Buyers should clarify:

- What is included in current seat entitlements, and what is not.
- Whether agents acting on behalf of users are covered by those seats.
- Whether stand-alone agents require separate licenses.
- Whether third-party agents can use the same governed paths as the vendor’s own agents.
- Which actions consume credits, and whether failed actions count.
- Whether rate cards are fixed for the contract term.
- Whether usage logs are exportable.
- Whether caps can be set by agent, workflow, or department.

Most crucially, buyers should ask how the commercial model changes when agent work reduces human seat usage. If agents resolve many support tickets, keep CRM data updated, or handle routine HR questions, can seat counts or tiers be reduced accordingly? Sometimes there are valid reasons for “no,” but without asking, customers risk paying both the old seat model and a new, opaque agent consumption bill.

## The New Commercial Unit of Software

The agent era is not only changing interfaces; it is changing the economic unit of value in software. Historically, the seat was a proxy for human work and value creation. Now, the agent license is becoming the meter for that same value, but delegated to machines.

Builders and buyers who understand how agent work is billed versus human work will design, deploy, and negotiate more sustainable systems. Those who ignore the second meter risk shipping agents that seem successful until the bill arrives and reveals that the real value and economics have already been ceded to the platforms’ pricing models.

