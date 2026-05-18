---
title: 5 Levers That Separate Winning AI Investments from Disasters
author: Nate B Jones
source_id: 1
source_slug: nate-b-jones
url: https://www.youtube.com/watch?v=LIkYVsxMpS8
published_at: '2026-05-17T18:00:14Z'
duration_seconds: null
primary_theme: business
secondary_theme: tech
relevance: 7
hook: Five clear levers decide whether your AI bets pay off or implode.
tldr: AI investment decisions must start from a precise understanding of workflows, not from tools or models. For each important workflow, leaders must choose among five levers—automate, build, buy, hire, or wait—based on work shape, risk, and market maturity. Firms that cannot clearly describe their work, define “good,” or match solutions to workflow shape will waste capital, mis-hire, and join the large share of failed AI projects.
caveats: Skip it if you want hard technical depth on model behavior, evals, or infrastructure, because this is mostly a business decision framework rather than a systems piece.
pitch: You’ll probably get value from this because it frames AI decisions at the workflow level with concrete levers—automate, build, buy, hire, or wait—which matches the kind of production-minded thinking you care about when deciding where LLM systems actually belong.
---

## Key Points

- AI failure rates are driven by cost, unclear business value, and weak risk controls, not agentic tech itself.
- Meaningful AI decisions must be made at the level of specific workflows, not departments or job titles.
- A workflow is the full operating loop of inputs, permissions, standards, checks, escalation, and accountable owners.
- Departments actually contain many distinct workflows, each with different AI needs and appropriate investment choices.
- Every workflow can be scored on repetition, error cost, judgment required, specificity, solution availability, and model progress risk.
- Leaders effectively have five levers per workflow: automate, build, buy, hire, or temporarily wait.
- Automation fits high-volume, patterned workflows where exceptions are rare, definable, and cheap to evaluate.
- You should not automate work you cannot describe clearly in plain language, including inputs, outputs, standards, and exceptions.

## Notes

## Core Problem: AI Failure Is a Workflow Problem
- Many AI projects will be shut down by 2027 due to cost, unclear value, and risk issues, not because agentic AI is inherently flawed.
- Vendor conversations often bypass the actual work; vendors pitch shapes of solutions that don’t map to what teams really do.
- The central determinant of AI investment success is how well you understand and shape the underlying work, not which model or vendor you pick.

## Think in Workflows, Not Roles or Tools
- AI investment is fundamentally a question about the shape of work, not an “AI question.”
- Model choice, vendor choice, dashboards, and interfaces are downstream of workflow design.
- The correct unit of decision is a discrete workflow, not a department or generic role.
- Example (Accounts Receivable): collections prioritization, invoice matching, customer follow-up, exception handling, cash application, dispute resolution, reporting, and escalation are all different workflows.
- Example (Product): user research synthesis, spec drafting, backlog grooming, design review, experiment analysis, roadmap judgment, launch coordination, and customer escalation each have distinct shapes.
- Bundling many different workflows into one RFP usually yields a mediocre, ill-fitting tool.

## What a Workflow Actually Is
- “Workflow” here means the entire operating loop, not just a prompt.
- Elements include: what information comes in, what the system may do, what good output looks like, who checks what, escalation paths, and accountability for outcomes.
- The AI model is only a small part of this loop, even if it powers the core reasoning.
- Value comes from improving the workflow as a whole, not from the model in isolation.

## Evaluating Workflows Before Investing
- Once you identify your high-priority workflows, each can be evaluated along several dimensions:
  - How often it repeats.
  - How costly mistakes are.
  - How much human judgment it requires.
  - How specific it is to your company.
  - Whether credible market solutions exist.
  - Whether upcoming model releases might commoditize it.
  - Where its outputs go and how they are used.
- Only after this analysis should you decide whether to build, buy, automate, hire, or wait.

## The Five Investment Levers
- For any workflow, you basically have five levers:
  1. Automate/eat/delete the workflow.
  2. Build an AI-rich workflow tailored to your context.
  3. Buy an off-the-shelf solution.
  4. Hire people with needed capabilities.
  5. Do nothing for now and wait.
- In practice, strategies often combine levers (e.g., hire to build; buy a component inside a broader build).

## Lever 1: Automate / Delete the Workflow
- Automation is the most intuitive lever for most teams.
- It is appropriate when:
  - The work repeats frequently.
  - It follows a clear pattern.
  - Exceptions are rare and clearly definable.
  - You can cheaply and reliably check if the output is good.
- Examples:
  - IBM’s “Ask HR” for routine HR questions.
  - Intercom’s Finn for repeatable customer support cases.
- You must avoid “automation religion” and instead focus on where the value lies and who—AI or human—handles that value-best portion.
- Do not automate when most of the value and complexity lives in the exceptions.
- Many bad enterprise AI rollouts happen because vendors demo routine cases, but real traffic is dominated by edge cases; this yields poor accuracy and disappointed executives.

## Lever 2: Build a Custom AI Workflow
- Building is appropriate when the workflow is ill-suited to a generic product because of:
  - Many edge cases and exceptions.
  - Strong company-specific context, data, standards, approvals, and risk thresholds.
  - “Secret sauce” aspects of how your team works.
- Building implies setting up repeatable agentic loops with skills, connectors (e.g., MCP), plugins, data calls, sub-agents, and perhaps third-party tools inside the loop.
- You may still buy small components (models, tools, connectors) while owning the overarching workflow.
- The crucial questions before building:
  - What data must flow into this workflow?
  - What does “good” output concretely look like?
  - How will you know the workflow’s outputs meet your standards?
- If humans currently handle this work well and you haven’t already automated it, it is likely complex; you must understand its boundaries and sub-tasks.
- Executives often demand builds without being able to specify success criteria; teams then declare success without a solid external standard.
- As a leader, you must be capable of acting as “honest eyes” on whether the built workflow actually works or needs rework, more hiring, or a different mission.

## Lever 3: Buy Solutions and Primitives
- Buying is about whether you can take a purchased solution and plug it into your workflows for immediate value.
- With workflows, this is more complex than with traditional bounded software.
- You need to know on what substrate the solution sits (data layer, systems, ticketing, etc.) and whether your dev team can integrate and operationalize it.
- Two broad “buy” categories:
  1. **Primitives / components / services** you can reuse across many workflows.
     - Examples: Stripe’s AI primitives; tools that help agents communicate context; orchestration or notebook-like tools for agent coordination.
     - Low-risk to adopt; if developers like them, usage will spread naturally.
  2. **End-to-end workflow solutions** that embody a vendor’s entire workflow design.
     - Example: Harvey for legal workflows, effectively selling an agentic pipeline.
- For full workflow solutions, the key question is whether your work is “Harvey-shaped” (or vendor-shaped).
  - You must understand the vendor’s workflow design deeply enough to judge 80–90% overlap with your own.
  - Low overlap means significant adaptation work, which is harder in the AI era than in traditional deterministic software.

## Lever 4: Hire Targeted Human Capability
- Many companies seek “purple unicorns”: domain experts who are also AI builders, systems architects, executives, and change leaders.
- Such candidates are rare and heavily contested; the market may clear them out before you decide.
- A better hiring approach: start from workflows and ask what human capability those workflows will need in 6–12 months.
- Typical gaps might be domain trust, workflow engineering, evaluation design, or executive ownership for AI changes.
- Write specific, realistic job descriptions mapped to concrete workflow needs instead of vague “AI expert” roles.
- The current hiring market is noisy: AI-generated resumes, potential deepfakes, hype, plus hiring managers who lack clarity on what they want.
- This leads to long time-to-fill, confusion, and frustration on both sides.
- Clarifying workflows and investment strategy makes it easier to define roles, assess candidates, and avoid over-hiring for skills your existing team could develop.
- If someone internal can level up in six months to cover the needed capability, prefer developing them instead of enduring a painful external search.

## Lever 5: Wait and Sequence Your Investments
- Waiting is counterintuitive amid pressure to “do AI,” but it is sometimes optimal.
- The question is not whether to transform with AI—almost all businesses must—but where to start for maximum leverage.
- Resources for change management are limited; prioritize workflows where transformation gives disproportionate benefit and learning.
- Lower-priority or low-leverage workflows can be deferred while you focus on areas with bigger impact.
- Waiting does not mean ignoring AI for years; it means stacking investments so the most leveraged changes happen first.
- Example: in analytics, you might delay changing SQL extraction if it already works well, and instead use AI for narrative analytics, explanations, and upstream storytelling where it adds unique value.

## Central Principle: Do Not Automate What You Cannot Describe
- The most important rule: “Do not automate what you cannot describe.”
- Every AI investment review should demand a plain-language description of the workflow:
  - Inputs.
  - Outputs.
  - Standards and success criteria.
  - Exceptions and how they are handled.
  - Ownership and accountability.
- Many AI projects fail because teams never reach a clear description, instead hiding many workflows inside vague requests to vendors or within broad job descriptions.
- Different stakeholders then interpret the same vague language differently, leading to misaligned expectations and poor results.

## Investment Matrix: Work Specificity vs. Market Maturity
- Two axes define a classic AI investment matrix:
  - Horizontal: how specific the work is to your company (general vs. company-specific).
  - Vertical: how mature AI solutions are for your vertical.
- If work is **common** and the market is **mature**:
  - It’s an obvious **buy** scenario.
  - Analogies: Workday for standard HR/payroll, Stripe for payment primitives, standard help desk tools.
- If work is **common** and the market is **immature**:
  - Either prototype narrowly or wait; avoid long contracts in a rapidly evolving category.
  - If aligned with your vision, you may build and try to win the category.
- If work is **company-specific** and the market has **some useful primitives**:
  - Buy primitives and building blocks but **own the workflow and standards**.
  - This is where most ambitious teams should be operating: buy models, connectors, orchestration; build your unique workflows.
- If work is **company-specific** and the market is **thin or immature**:
  - Strong case to build, aiming to own the emerging category.

## When Hiring Is the Next Investment
- Hiring cuts across the matrix; you must define workflows first to define hiring needs.
- A signal you should hire: the critical work cannot be clearly defined, trusted, or framed by existing staff, and someone needs to set standards and define “good.”
- In such cases, the next investment should likely be a person who can own and clarify the workflow and its outcomes.

## Changing Executive Responsibilities
- AI shifts executive work from generic “AI strategy” to precise capital allocation around workflows.
- Leaders must:
  - Understand enough about key workflows to allocate capital intelligently.
  - Define desired outcomes and problem frames.
  - Prioritize which workflows to transform first.
  - Decide where to allocate talent and which levers to pull.
- The executive role is not to personally evaluate every tool but to structure decisions around well-understood workflows.

## AI vs People: Reframing the Debate
- A shallow framing pits AI against humans; this is not useful.
- The serious conversation is about where people should spend time, where they should uplevel, where there are genuine talent gaps, and how tasks inside job families will be rebundled as automation advances.
- Remaining human work becomes more leveraged and impactful when AI and agentic systems are correctly placed at the business core.
- The ultimate goal is not headcount elimination but better capital allocation across automate/build/buy/hire/wait, yielding disproportionate value and avoiding the fate of failed AI projects.

## Final Takeaway
- Success in AI investment starts and ends with workflows.
- You must be able to name, describe, and bound workflows, then have discrete investment discussions per workflow.
- Conversations that start from “we need an AI strategy” without this workflow grounding are unlikely to produce durable value.

