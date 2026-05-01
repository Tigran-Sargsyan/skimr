---
title: 'GPT-5.5 vs Claude vs Gemini: The Real Difference Nobody''s Talking About'
author: Nate B Jones
source_id: 1
source_slug: nate-b-jones
url: https://www.youtube.com/watch?v=9aIYhjeYxzM
published_at: '2026-04-28T14:00:14Z'
duration_seconds: null
primary_theme: tech
secondary_theme: business
relevance: 8
hook: GPT-5.5 shifts AI from answering tasks to carrying entire workflows.
tldr: Nate B Jones argues GPT‑5.5 is currently the strongest general-purpose model, not just by benchmarks but by how far it can carry complex, messy work before dropping the thread. Through three demanding private evaluations—executive knowledge work, dirty data migration, and 3D visualization—he shows 5.5’s strengths in judgment, multi-artifact execution, and long-context reasoning, alongside weaknesses in visual taste and some back-end data hygiene. He concludes 5.5 in Codex is the best default for serious, multi-step, tool-heavy work, while Claude Opus still leads on blank-canvas visual design, and all models still require human validation for high-stakes outputs.
caveats: It’s still a commentary piece with some product flavor and private evaluations, so skip it if you want fully reproducible benchmarks or deep technical methodology rather than a sharp practitioner’s take.
pitch: You work on LLM agents and production AI systems, so this is worth your time because it focuses on how models behave in messy, tool-heavy workflows, where they fail, and why evals and validation matter more than benchmark slogans.
---

## Key Points

- GPT‑5.5 meaningfully raises the “floor” of default capability, feeling like a larger pretrain that needs less hand-holding and better understands user intent over long contexts.
- Public benchmarks (Terminal Bench, GPQA/GDP-Val, intelligence indices) show 5.5 as both smarter and more token-efficient than 5.4, but Jones emphasizes real-work evaluations over small, clean tasks.
- The main industry misconception he challenges is that “the best model matters less now”; he argues it matters most on ugly, under-specified, multi-step work with messy inputs and real risk.
- Modern evaluation should focus on whether a model can *carry* a task end-to-end—across formats, context shifts, and risk—rather than just answer isolated prompts.
- 5.5 should be judged as part of a system (Codex, Images 2.0, tools, file access, browser control) rather than as a standalone chatbot.
- In the Dingo & Co executive work test, 5.5 vastly outperformed Opus 4.7, Claude Sonnet 4.7, and Gemini 3.1 Pro on both artifact quality and legal/ethical posture.
- Dingo required 23 distinct deliverables (docs, decks, sheets, dashboards, comms, risk analysis) around a fictional, legally sensitive exotic-pet product; 5.5 produced real, usable files in all required formats.
- 5.5 showed strong judgment in Dingo by narrowing the target market, highlighting legal/ethical risk, separating curiosity from real buyers, and repeatedly clarifying that the product does not legalize exotic ownership.
- However, 5.5’s artifacts still had minor production defects (metadata, rounding, some stale pricing), which Jones classifies as “final mile” issues rather than misunderstandings of the assignment.
- In the Splash Brothers migration test, 5.5 became the first model to catch planted fake customers and absurd payments, but it still mishandled subtle schema and enum-hygiene details, so it cannot be the final authority on production data.
- Splash Brothers illustrates a pattern: 5.5 excels at semantically obvious correctness (fake records, duplicates, typos) but still struggles with boring but critical database clean-up (service codes, normalization, reconciliation).
- Compared directly to 5.4, 5.5 regressed slightly on some back-end hygiene behaviors even as it improved on intuitive error-catching, reinforcing the need for harnesses, validators, and good prompts.
- Jones’ practical recommendation for data work is to let 5.5 inventory, design schemas, extract, log provenance, and build review UIs, but always add validation layers before treating the result as canonical.
- In the Artemis 2 3D visualization test, both 5.5 and Opus 4.7 got the mission facts broadly right, but 5.5 produced a dense, cartoonish visualization while Opus produced a more visually authoritative but less information-dense scene.
- This test highlights Claude Opus’s continuing edge in visual composition and blank-canvas taste, and 5.5’s strength at information density and faithful implementation against a reference.
- Jones suggests a workflow where Images 2.0 (or Claude design) generates design references and 5.5 in Codex implements working UIs and visualizations, rather than asking 5.5 to invent style from scratch.
- He strongly prefers Codex over the ChatGPT UI for serious work because Codex lets 5.5 act in the real environment: reading/editing files, running commands, testing code, driving browsers, and iterating artifacts.5.5’s value compounds with tools: greater intelligence makes its tool use more effective, and richer tools make its intelligence more economically useful, especially in long, multi-step workflows.
- Service reliability is itself a differentiator: recent public status pages show OpenAI with materially higher uptime (more “nines”) than Anthropic, and users report Claude availability issues, which affects suitability for production use.
- Based on his testing, Jones routes work as follows: 5.5 in Codex for complex multi-step execution and engineering implementation; Opus 4.7 for blank-canvas visual design and taste; hybrid workflows for UI (reference + 5.5) and engineering (Opus for planning, 5.5 for execution).
- For long-form writing, 5.5 advances notably in structural coherence—holding arguments and shape—not just sentence quality, though it still requires human editing and taste.
- For data-heavy and research-heavy work, he uses 5.5 aggressively but insists on explicit validation: provenance, rejected records, duplicate logic, and personal review of important claims and sources.
- Artificial Analysis observed that 5.5 can feel overconfident even as it performs excellently, a nuance users should keep in mind for high-stakes domains.
- He argues the future is not single-model loyalty but intelligent routing between systems based on strengths: execution vs taste, planning vs implementation, ideation vs migration.5.5’s combination with Images 2.0 and Codex unlocks new small-business opportunities (e.g., palm-reading apps, custom Lego-set services) that were not realistic even a week prior.
- He contends that easy tasks (summaries, basic CRUD apps, simple SQL) are now saturated; to see real differences, users must test models on multi-artifact briefs, messy data piles, and long execution loops.
- Overall, he sees 5.5 as the new high-water mark for what a single model can reliably “carry” in real work, significantly expanding the ambition of tasks users can reasonably delegate while still requiring human judgment and validation for critical outputs.

## Notes

## Why GPT‑5.5 Matters

Jones argues GPT‑5.5 is currently the strongest general-purpose model because it raises the *floor* of default capability. Unlike gains that come only from more inference-time thinking or tool calls, 5.5 feels like a larger, smarter pretrain: it locks onto task shape faster, needs less hand-holding, and carries intent over long contexts. Benchmarks (Terminal Bench, GDP-Val, third-party intelligence indices) support this and suggest higher efficiency, but he stresses that benchmarks understate the real shift.

He criticizes the view that model choice no longer matters, noting that frontier models are indeed interchangeable for small, clean tasks. The real differences appear on “ugly” work: under-specified briefs, messy files, conflicting sources, legal/ethical risk, and multi-step artifact production. The key question becomes not “can it answer?” but “can it *carry* the work end-to-end?”

He also insists models be seen as systems, not just weights: tools, file access, browsers, memory, images, and compute all shape actual capability. 5.5 launches alongside Codex and Images 2.0, making its impact larger than a typical model-only release.

## Private Bench: Three Hard Tests

Jones uses a private, intentionally brutal benchmark to probe generalization beyond public exams.

### 1. Dingo & Co (Executive Knowledge Work)

Task: 23 deliverables for a fictional, legally fraught dingo-litterbox startup (docs, deck, spreadsheets, dashboard, comms, risk analysis). The model must grasp market reality, legal constraints, and ethics while producing real, openable artifacts.

Results: 5.5 scored ~87 vs Opus 4.7 (~67), Sonnet 4.7 (~65), Gemini 3.1 Pro (~50). All 23 outputs were proper file types (not mislabeled HTML). Decks had real slides and media, sheets had formulas and charts, the dashboard worked and used provided assets, and the research file contained dozens of credible URLs, especially on legal issues.

Most importantly, 5.5 adopted a cautious posture: narrow, qualified market; clear separation between product and risky import business; consistent statements that ownership remains legally/ethically complex. Defects were minor (metadata, a rounded metric, some imprecise pricing), implying it nailed the assignment but needed final polish.

### 2. Splash Brothers (Dirty Data Migration)

Task: migrate a chaotic folder (465 mixed-format files, corrupt data, fake records, duplicates, typos, inconsistent enums) into a clean database with audit trail and review UI.

5.5 became the first model to:
- Reject planted fake customers and fake $25,000 payment.
- Correctly merge all duplicate customer pairs and catch name-typo orders.
- Discover all files and produce a deterministic rebuild with a long migration report.

Yet it still:
- Omitted service codes from the schema, missing planted conflicts.
- Canonicalized an orphaned order to a real customer instead of routing to review.
- Left messy, unnormalized payment statuses/methods and inconsistent dashboard vs database counts.

Compared to 5.4, some back-end hygiene slightly regressed while intuitive catches improved. Jones’ prescription: use 5.5 for inventory, schema proposal, extraction, provenance, and UI, but never let it declare the database canonical—add validators, row-count checks, enum audits, and human approval.

### 3. Artemis 2 (3D Visualization & Research)

Task: research Artemis 2 from scratch, then build an interactive 3D browser visualization (rocket, trajectory, controls, educational overlays). Models can fail on research, visuals, controls, or pedagogy.

Both 5.5 and Opus 4.7 correctly treated Artemis 2 as a lunar flyby (not landing/orbit) and produced reasonable trajectories. Differences:
- 5.5 favored dense information (labels, panels, multiple fact surfaces) but the scene felt cartoonish, with off scale and proportions.
- Opus produced a more visually grounded, better-lit scene that felt “showable” but with less immediately accessible information.
- Controls in both needed another pass.

Jones would start from Opus’s visuals and layer 5.5’s information density on top. He concludes: Opus still leads on blank-canvas visual taste; 5.5 is strong at faithfully implementing a reference, especially when combined with Images 2.0.

## Codex, Tools, and Reliability

Jones now prefers Codex over ChatGPT for serious work. ChatGPT is for quick, consumer tasks; Codex is where the model works inside real environments: reading/editing files, running tests, driving browsers, iterating on outputs. 5.5 plus tools amplifies value: intelligence and agency compound.

Reliability also matters. Public status pages show OpenAI with higher uptime (more “nines”) than Anthropic recently, and users report Claude availability issues. For production use, availability becomes part of model quality.

## Routing Strategy & Use Cases

Jones’ routing today:
- **Complex multi-step execution & engineering implementation:** 5.5 in Codex as default.
- **Blank-canvas visual / design taste:** Opus 4.7.
- **UI with both taste and robustness:** generate a visual reference (Images 2.0 or Claude) then have 5.5 in Codex implement it.
- **Engineering planning vs execution:** Opus for planning and critique; 5.5 for code execution and testing.
- **Writing:** 5.5 for stronger long-form structure; still requires human editing.
- **Data & research:** 5.5 heavily, but always with explicit validation and personal review.

He notes 5.5 can feel overconfident, echoing Artificial Analysis. He emphasizes routing over single-model loyalty.

## Implications

5.5, Images 2.0, and Codex together enable new small businesses (e.g., palm-reading apps, custom Lego kits) that were not practical days earlier. More broadly, 5.5 is a new high-water mark for how much real work a single model can carry, expanding what users can reasonably delegate—provided they retain human judgment, especially wherever mistakes are expensive.

