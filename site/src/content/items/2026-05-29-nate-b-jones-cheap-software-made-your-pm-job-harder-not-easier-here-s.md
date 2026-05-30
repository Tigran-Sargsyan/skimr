---
title: Cheap software made your PM job harder, not easier. Here's the new job.
author: Nate B Jones
source_id: 1
source_slug: nate-b-jones
url: https://www.youtube.com/watch?v=b6J387xJvHg
published_at: '2026-05-29T14:00:08Z'
duration_seconds: null
primary_theme: tech
secondary_theme: business
relevance: 6
hook: Cheap software flipped PM work from gatekeeping ideas to judging what should truly exist.
tldr: AI and low-code tools make software generation cheap and ubiquitous, flooding companies with working prototypes instead of just feature requests. Product management shifts from rationing scarce engineering capacity to exercising deep technical and market judgment over what should be promoted, contained, or deleted. The new core PM skill is classifying this “prototype commons” with a production-class ladder while aligning it to customer value, risk, and company bets.
caveats: Skip it if you want concrete architecture, evals, or failure-mode detail; this is mostly a product-management argument rather than a deep engineering piece.
pitch: You’ll get a useful product-side lens on how cheap AI and low-code change the bottleneck from building features to deciding which prototypes deserve to become real systems, which is directly relevant if you build AI platforms or internal tooling.
---

## Key Points

- AI and low-code tools make software creation easy for many employees, not just engineers.
- The PM role is shifting from filtering ideas pre-build to judging already-built artifacts.
- Future PMs must be technical enough to reason about models, data, workflows, and failure modes.
- The new scarcity is not prototypes but high-quality judgment about what should exist and why.
- Broad experimentation is valuable, but without judgment it becomes risky, invisible sprawl.
- PMs should practice open discovery of grassroots tools instead of reflexively shutting them down.
- A production class ladder distinguishes personal tools, team betas, supported internal products, and customer-facing products.
- Intentional promotion and demotion decisions prevent a junk drawer of unsupported, zombie software becoming new tech debt.

## Notes

## From Prototyping Hype to a Deeper PM Shift

AI and low-code tools have made it easy for PMs and non-PMs alike to prototype using platforms like Lovable, Claude Code, and Codex. The speaker argues that focusing PM education on “becoming prototypers” misses the real shift. Generation is now cheap and easy, so the bottleneck has moved. The scarce resource is no longer the ability to produce first versions, but the human judgment that determines what should matter, what should be deleted, and what the business should bet on.

Traditional PM methods—PRDs, roadmap reviews, long planning cycles, and prioritization meetings—were optimized for an environment where software was expensive and engineering capacity scarce. In that world, PMs served as filters on what ideas could reach engineering. AI breaks that filter because many people can now create working tools before PMs or engineers are even involved.

## Software Abundance: Microsoft and Secret Sprawl

Microsoft illustrates this abundance: internally they have over a million Power Platform assets—tens of thousands of apps, flows, agents, and chatbots. These artifacts are not just ideas; they are working software touching real systems, workflows, and sometimes customers. The same pattern is appearing in many companies.

At the same time, reports like GitGuardian’s show a surge in exposed AI-related secrets on GitHub, with millions of credentials and integrations leaking and rapid year-over-year growth. Faster software creation means more scripts, workflows, and integrations, and more surfaces for risk. Product leaders inherit that sprawl and its associated risk when useful but unmanaged tools spread without classification or ownership.

## The New Core PM Question

Historically, the fundamental PM question was “Should we even build this?” Today, the conversation often starts later: “Somebody already built something—should this matter?” PMs must determine whether a working artifact is:

- True market value the company should invest in.
- Useful internal tooling that should be supported at some level.
- Or a candidate to be explicitly deleted or kept small and local.

This reframes PM work from rationing engineering to classifying and steering software abundance. The PM’s job becomes to map artifacts to value, risk, and strategy.

## Why PMs Must Become More Technical

AI products are deeply technical systems whose behavior is determined by model characteristics, data access, agent loops, retrieval mechanisms, and system boundaries. Product decisions now routinely involve understanding model behavior, evaluation strategies, latency, cost structures, permissioning, data access, workflow topology, and failure modes.

A PM who cannot reason about these dimensions is “missing the product,” because technical choices drive user experience, reliability, trust, and business viability. The speaker does not claim PMs must be full-time engineers, but insists that non-technical PM roles have little room left. Technical literacy is central to exercising sound product judgment in AI-era systems.

## Judgment as the New Bottleneck

With software cheap to produce, the scarcest resource becomes judgment about:

- What should exist and what should be deleted.
- Who a product is truly for.
- What standard of quality and reliability it must meet.
- What the company is actually willing to rely on and support.

This is described as “product judgment” rather than just “product management.” The PM must distinguish between superficial requests and symptoms of deeper issues, between competitor noise and meaningful differentiation, and between local convenience tools and artifacts that reveal scalable demand.

## The Prototype Commons: Broad Building and Its Risks

The “prototype commons” is the informal ecosystem where scripts, dashboards, agents, automations, and half-real products emerge because employees finally can solve previously neglected problems. This commons is messy but valuable: it reveals hidden demand, missing platform primitives, customer pain, and internal bottlenecks that formal product processes have missed.

However, without stewardship, this commons leads to two failures:

- Useful work remains invisible, unsupported, and fragile.
- Risky work spreads without governance, potentially touching sensitive data or critical systems.

If product only shows up to say “no,” employees will hide tools until something breaks. A healthy prototype commons therefore needs intentional stewardship, not suppression.

## Open Discovery as PM Posture

The speaker advocates an “open discovery” posture for PMs:

- Invite employees to show what they’ve built.
- Ask what problem it solves and who uses it.
- Clarify what data and systems it touches.
- Extract what the builder has learned from real usage.

This approach encourages broad building, ensures that useful signals are visible, and turns grassroots experimentation into structured input for product judgment, instead of underground shadow IT.

## The Production Class Ladder

To make sense of the messy prototype commons, PMs should use a “production class ladder” with distinct rungs:

### 1. Personal Tools

These are scrappy tools for a single individual. They can be loose in structure but should stay away from sensitive data unless clear local handling rules exist. They have minimal formal standards and no broad support obligations.

### 2. Team Betas

Team betas are used by a small group. They require:

- A primary owner and a backup owner.
- A short written description.
- Clarity on which systems they touch and what benefit they deliver.
- A failure plan for what happens if the tool breaks or its owner leaves.

### 3. Supported Internal Products

These are internal tools the company depends on. They need:

- Explicit product ownership.
- Partnership with platform or infrastructure teams.
- Access management, monitoring, and logging.
- Documentation, support expectations, and auditability.
- A defined change process.

This rung represents serious commitments about reliability and support.

### 4. Customer-Facing Products or Features

These are external surfaces customers interact with. They require all usual product standards plus AI-specific evaluations and governance where appropriate, such as behavior evals, safety constraints, and compliance considerations.

The crucial insight is that each rung represents a different class of promises and responsibilities. The first version of something and the supported version do not have to be the same artifact.

## Promotion, Demotion, and Tech Debt of Abundance

In the old model, what entered engineering was what became official, supported software. In the new model, PMs must also decide what gets promoted out of the prototype commons and what gets intentionally left at a lower rung or removed.

Promotion up the ladder should be deliberate, based on value, risk, and alignment to strategy. Demotion is equally important. A ladder that only moves upward becomes a junk drawer in which everything eventually becomes a support obligation.

If PMs fail to make these calls, the company accumulates “new tech debt”: support burden on dead or marginal software, faster than it can even name the assets. That tech debt is not just code complexity, but a proliferation of unowned tools and unexamined promises.

## Governance Without Killing Innovation

Microsoft’s internal governance response to its Power Platform ecosystem focuses on inventory, telemetry, permission reviews, environment controls, and data policy. These mechanisms are presented as enablers of broad building, not as reasons to shut it down.

The recommended pattern is a “default allow” environment for experimentation, coupled with a very intentional promotion path for anything the business will rely on. Central product and engineering should not be the only builders, or the organization will waste the creative capacity unleashed by AI.

## The PM’s New Decision Rule

PMs should update their core questions:

1. First, ask what class of software a given artifact is: personal tool, team beta, supported internal product, or customer-facing promise.
2. Then ask the tougher questions: Should this exist? Who is it for? What standard must it meet? What is the company willing to rely on and support?

PMs also need sharper market judgment in a world where first versions are cheap. They must know which customer problems truly matter, which workflows are close to revenue, retention, or trust, which competitor features are distractions, and which internal tools indicate real, scalable demand.

## The Opportunity for PMs

The speaker frames this era as an exciting inversion of the traditional PM constraint. Instead of constantly saying “we can’t build everything,” PMs can assume “we can build almost anything,” and must decide what should be built and supported.

The invitation is to become a “post-prototype” PM: someone who doesn’t stop at faster building, but builds and applies a robust production class ladder, exercises disciplined product judgment, and channels organizational creativity into software the business can safely, profitably, and sustainably rely on.

