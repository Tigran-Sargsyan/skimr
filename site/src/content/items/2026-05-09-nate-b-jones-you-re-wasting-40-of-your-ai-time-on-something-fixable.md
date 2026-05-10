---
title: You're Wasting 40% Of Your AI Time On Something Fixable
author: Nate B Jones
source_id: 1
source_slug: nate-b-jones
url: https://www.youtube.com/watch?v=647pSnX5H_Y
published_at: '2026-05-09T15:00:09Z'
duration_seconds: null
primary_theme: tech
secondary_theme: thinking
relevance: 6
hook: Stop being your own AI plugin and start packaging real workflows instead.
tldr: The video explains a clear mental model for prompts, skills, plugins, MCPs/connectors, hooks, and scripts as parts of an AI “mech suit.” It argues most people waste time over-prompting instead of packaging reusable workflows and deterministic checks around the same underlying LLM intelligence. Non‑engineers with domain knowledge can now design this scaffolding themselves, which is where most practical AI leverage comes from in 2026.
caveats: Skip it if you want real production case studies, benchmarks, or failure modes, because this looks more like productized AI commentary than deep systems analysis.
pitch: If you're building agent tooling or RAG systems, this gives you a compact mental model for separating prompts, skills, connectors, and scripts so you can package deterministic workflow boundaries instead of hand-tuning prompts.
---

## Key Points

- A prompt is best for one-off, temporary, highly specific tasks that you do once.
- A skill is a reusable, shareable process description that lets an LLM follow your house style consistently.
- Skills are tool-agnostic markdown documents that can be used across different LLM platforms.
- A plugin is a named, installable package that wraps an entire workflow, not just one skill.
- Plugins can contain skills, prompts, MCP connectors, hooks, scripts, assets, and metadata in one bundle.
- MCPs and app connectors provide access to live external systems and data but are not full workflows.
- Hooks and scripts handle deterministic checks and actions that should not be left to model judgment.
- The core high-value skill is identifying clean workflow boundaries and deciding what should be a prompt, skill, plugin, connector, or script.

## Notes

## Big Picture: The “Mech Suit” Around LLMs

- The core claim is that LLMs only become truly useful when wrapped in scaffolding: prompts, skills, plugins, MCPs/connectors, hooks, and scripts.
- This scaffolding is likened to a mech suit or armor around the model, analogous to Darth Vader’s suit or Transformers’ metal bodies enabling them to operate.
- The intelligence inside (the LLM) may improve, but the huge leverage comes from how you package workflows and tools around it.
- Many people feel a foggy middle layer between “model is smart” and “work got done” because these components aren’t clearly distinguished.
- Understanding this harness is now accessible even to non‑engineers, and that understanding is what prevents wasted time and enables “messy, multi‑part” work.

## Why This Matters: Wasted Time and Messy Multi-Part Work

- OpenAI’s description of a newer ChatGPT version highlights strength in messy, multi-step tasks: planning, tool use, checking work, and ambiguity.
- However, most people stall not due to lack of tools, but because they don’t know how to structure the harness around the model.
- Over-reliance on giant prompts for recurring work leads to hours of repeated manual setup, effectively turning humans into “the plugin.”
- The goal is to move from ad hoc prompting to intentional design of reusable agentic workflows that carry tools, checks, and structure.

## Prompts: For One-Off, Temporary Tasks

- A prompt is defined as what you use when you want to do a thing once.
- It’s suitable for small, temporary, highly specific tasks like a one-off complex email with bespoke backstory.
- A prompt is just text: it doesn’t “carry” permissions, tools, or a packaged workflow.
- Prompts can describe processes but do not make those processes robustly repeatable or easily sharable.
- People tend to over-index on prompts, stuffing recurring processes into them and silently wasting hours redoing setup.

### When to Stay at Prompt Level

- Use prompts when:
  - The task is genuinely one-off.
  - The cost of formalizing a process or plugin exceeds the expected reuse.
- The video stresses prompts still matter and prompt-crafting skills from earlier years are not wasted; they’re just not enough for recurring workflows.

## Skills: Reusable Process Instructions

- A skill is a clear, reusable description of how to do a specific kind of work.
- It lives as a markdown file that explains steps, structure, and quality criteria for a process.
- Skills encode “house style” or standard ways of working—e.g., how your team reviews pull requests or writes marketing documents.
- They enable any LLM to apply that process consistently across a team.

### Prompt vs Skill

- Think of prompts as one-offs; think of skills as processes you want to reuse and re-invoke.
- Example:
  - Prompt: crafting a unique, context-heavy note to a specific client one time.
  - Skill: a repeatable method for cold outbound emails, specifying sections, data to pull, and how to close.
- Skills can be used for marketing, support, success, engineering, or any repeated LLM-amenable work.
- Skills are tool-agnostic: you don’t write “a Codex skill” or “a Claude skill”; you write one skill and use it with whatever LLM.

### Managing Many Skills

- Once people grasp skills, they often overproduce them, making organization difficult.
- Skills follow a power law: ~20% of skills generate ~80% of the value.
- You should identify the few high-impact skills that are frequently reused, highly sensitive to correctness, and worth careful design.

## Plugins: Workflow Packaging, Not Just Add-Ons

- Plugins are the next scale up from skills: they package entire workflows.
- A plugin can contain skills but also app integrations, MCP servers, hooks, scripts, assets, commands, and metadata.
- It “gives a workflow a name,” wraps all its components, and makes it installable and sharable.
- When you want to add an entire workflow in one go—bigger than a skill—you create a plugin.

### Example: Outbound Email Workflow

- A skill defines how to structure a good outbound email.
- A plugin might:
  - Include that email-writing skill.
  - Connect to Salesforce via an MCP/connector to pull customer data.
  - Possibly run scripts or checks before finalizing.
- Team members can install the plugin and get the entire working system without reconstructing setup manually.

### Humans as “Manual Plugins”

- Many serious users already perform plugin-like work manually:
  - Copy from App A, paste into chat, ask the model, fetch data from another system, verify outputs, repeat.
- This behavior is described as being “the human plugin.”
- The key idea: instead of manually orchestrating these steps, encode them once as an actual plugin.
- In 2026, non‑engineers can realistically build such plugins.

## MCPs and App Connectors: Access to Live Systems

- MCPs and connectors are how agents access the systems where real work and data live.
- They are likened to “internet plugs” that connect to external services, retrieve live data, and return it.
- Example: a Salesforce connector that fetches contact and account information for outbound email.

### Plugin vs MCP/Connector

- Many people conflate MCP connectors with plugins because both “plug into” something.
- Key distinction:
  - An MCP/connector is just the data or system access layer.
  - A plugin is a larger workflow package that may include one or more MCP calls plus process logic, skills, and checks.
- Increasingly, SaaS and work platforms are building MCPs/connectors themselves, so users don’t always need to.

## Hooks and Scripts: Deterministic, Non-LLM Steps

- Hooks and scripts handle workflow parts that should not depend on the model’s memory or discretion.
- They represent deterministic operations where you want guaranteed behavior, not probabilistic reasoning.

### When to Use Scripts/Hooks

- Use them when you need to:
  - Format code via a formatter instead of asking the model to remember style.
  - Validate schemas directly rather than hoping the model produces correct structure.
  - Actually run tests rather than having the model imagine test results.
  - Ensure generated files are valid JSON or meet a structural contract.
  - Enforce a review step before an agent stops.
- These are not MCPs, and they should not be left to “model judgment.”
- A good agent workflow separates deterministic parts (scripts/hooks) from the model’s reasoning.

### Relationship to Plugins

- Hooks and scripts usually live inside plugins as part of the workflow package.
- A plugin can be a “grab bag present” containing scripts, hooks, connectors, skills, and prompts in one bundled structure.

## Rethinking Plugins: Workflow Packaging, Not an App Store

- The common “app store” analogy for plugins is considered too small.
- If you see plugins as add-on apps, you tend to shop passively: “What can I install?”
- Instead, think of plugins as workflow packaging for your own repeated work structures.
- The better question becomes: “Which parts of my work have enough repeatable structure that the agent should inherit them?”
- Plugins are described as Lego builds: assembled from smaller bricks like prompts, skills, connectors, scripts, and hooks.

## Defining Good Plugin Boundaries

- A core human responsibility is deciding the “unit of work” each plugin should handle.
- Example: customer service in a small company might be split into separate plugins for refunds, activation, and upgrades, rather than one giant plugin.
- A workflow should have one job; bundling multiple distinct jobs into one plugin makes it unwieldy and error-prone.
- The valuable skill is recognizing where to draw semantic boundaries around workflows to make them composable and sharable.

## High-Value Skill: Workflow Decomposition and Packaging

- Knowing how to:
  - Analyze a workflow.
  - Draw clear edges around a coherent “job.”
  - Turn that into a plugin that teams can reuse.
- This is presented as a highly valuable and rare skill in 2026.
- People who understand their domain workflows deeply are best positioned to encode these boundaries and design effective plugins.

## Non-Technical Users as Scaffolding Designers

- “Non-technical” is increasingly a blurry label; many non-engineers are building real plugins.
- Examples include someone building an editorial review plugin to do a first-pass critique of text for roughness, coherence, and factual consistency.
- That plugin didn’t replace the editor’s judgment but dramatically sped up initial review.
- Another area is design workflows: connecting to tools like Figma, reading current designs and design language, and producing aligned outputs.
- Claude Design is described as essentially a significant plugin with a UI that became a product, illustrating how central plugins are.

## You Cannot Wait for the Perfect Off-the-Shelf Plugin

- Relying on Claude or ChatGPT to eventually ship every needed plugin is unrealistic.
- Users must proactively define where current workflows are too manual or prompt-heavy and design custom plugins.
- Typical plugin-worthy workflows include multi-source, recurring tasks like weekly business reports combining spreadsheets, Slack, docs, dashboards, past reports, and charts.

## Avoiding Vagueness: Making Scaffolding Understandable to Leadership

- If “scaffolding” is just “engineering stuff” in most people’s minds, only engineers will shape workflows.
- In 2026, encoding workflows should involve people who actually know the work: they know what data matters, what errors look like, and what steps are often forgotten.
- Many senior leaders lack any mental model of scripts, skills, connectors, and plugins, causing confusion about AI capabilities and requirements.
- Providing leadership this conceptual map helps them support AI transformation instead of blocking or misdirecting it.

## Canonical Mental Model Summary

- Prompt: for one-off, temporary work; good prompting remains valuable but is not the full solution.
- Skill: a sharable process description that helps an LLM follow a clear, repeatable procedure across people and tools.
- Plugin: a bundle that wraps skills, reusable prompt fragments, scripts, hooks, connectors, and assets into an installable workflow.
- MCP/App connector: the component that gives access to external systems and live data, often nested inside plugins.
- Scripts/Hooks: deterministic checks and operations that ensure structure, validation, and required steps, rather than trusting the LLM to self-check.

## Choosing the Right Level and Avoiding Over-Automation

- Not everything should be a plugin; some tasks should remain prompts or skills, some purely scripts, some human-only.
- The goal is not to create a “museum of unused plugins” but to package work that is repeated, valuable, and structured enough.
- Correctly choosing between prompt, skill, plugin, connector, and script is key to avoiding wasted time and poor automation.
- The overarching message: scaffolded agents with well-designed workflows can review work to your standards and use the right tools, turning the same base LLM into something vastly more powerful in practice.

