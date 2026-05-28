---
title: I Built a Deck With AI, Then Made a Second AI Attack It.
author: Nate B Jones
source_id: 1
source_slug: nate-b-jones
url: https://www.youtube.com/watch?v=MFzxIT88zfg
published_at: '2026-05-27T14:00:36Z'
duration_seconds: null
primary_theme: tech
secondary_theme: thinking
relevance: 6
hook: Turn AI-made PowerPoint and Excel files into trustworthy, checkable knowledge work instead of pretty lies.
tldr: The video explains how to move from one-off prompts to robust AI-centered workflows for Office documents. It proposes a four-stage pipeline—source preparation, structure, constrained creation, and hostile verification—to make AI-generated decks and spreadsheets trustworthy. The speaker argues that serious knowledge work remains deeply domain-specific, so teams must custom-build their own “truth layer” around AI tools.
caveats: Skip it if you want real implementation details, benchmarks, or infrastructure internals, because it sounds more like a product workflow talk than a deep technical teardown.
pitch: If you're building LLM systems, this is a concrete example of turning a brittle one-shot prompt into a staged pipeline with verification, which maps closely to the eval-and-guardrail problems you deal with in production.
---

## Key Points

- AI can now draft many Office documents in parallel, but reliability lags without proper workflows.
- Prompting for a finished deck or model from messy sources produces polished but ungrounded artifacts.
- A workflow defines stages an output must pass before it is trusted, unlike a single prompt.
- The proposed pipeline has four stages: source prep, structure, constrained creation, and verification.
- Source prep turns messy folders into indexed, status-labeled work packets with clear evidence metadata.
- File specifications act as blueprints, defining narrative, tab architecture, assumptions, and where “truth” lives.
- A hostile reviewer prompt makes an AI enumerate every unsupported claim, number, and formula inconsistency.
- Knowledge work is too domain-contingent for a generic push-button harness; teams must design their own systems.

## Notes

## From Single Prompts to Agentic Workflows

The speaker argues that Office documents still sit at the core of knowledge work: Word reports, Excel models, and PowerPoint decks. Traditional prompting guides for building individual assets were useful, but current models can do far more—such as drafting eight documents in parallel—if we stop thinking in terms of single prompts and start designing workflows with agents at the center.

He frames this as a shift from “bolt AI onto my existing process” to “rebuild the process around agents.” In this vision, agents are first-class participants in the workflow, and humans reconfigure their methods to take advantage of that. This change can yield order-of-magnitude productivity gains in knowledge work, but only if reliability is engineered in, rather than assumed.

## The Core Problem: Pretty Artifacts, Broken Truth

Modern tools can create Excel workbooks and PowerPoint decks quickly, but there is no built-in guarantee that the results are correct, accurate, or complete. The danger is not dramatic failures that immediately throw an error; it is subtle errors that look plausible and pass superficial review.

He gives a concrete example: a financial model that looked perfect on the surface—assumption inputs, revenue projections, valuation outputs, a written validation guide—but contained a fundamental formula error in the revenue growth row, copied across every future year. Excel reported no ref errors; the outputs looked neat, yet the model was “in a costume,” structurally convincing but numerically wrong.

This pattern recurs in production documents: neat layouts and polished language that hide incorrect cells or unsupported claims. The same risk exists with AI-generated decks that pull from unlabeled mixes of actuals and plan data, leading to clean-looking charts like “Revenue is ahead of plan” that actually blend incomparable data. The file appears finished but rests on no defensible foundation.

## Goal Orientation and Source Discipline

Models are goal-oriented: if you ask for a deck or spreadsheet, they will try to produce it from whatever materials they can see, even if those sources are messy or incomplete. When users do not explicitly define evidence structure or enforce source discipline, models treat that discipline as optional.

He stresses that this is not because models are getting worse; hyperscalers are training them to check claims and pay attention to sources. But if users do not mirror that discipline—by providing structured, labeled sources and well-designed workflows—the models will still “try to care” about sources, then end up guessing where information is missing. Their drive to produce a finished artifact then betrays the user.

The emerging standard for “serious knowledge work in 2026,” he suggests, is to make every important claim and calculation checkable and to actively invite scrutiny.

## Prompts vs. Workflows

He draws a sharp line between:

- **Prompt**: A request for a final output (“make me a deck,” “build this model”).
- **Workflow**: A defined series of stages that an output must pass through before being trusted.

Relying on prompts alone is what yields attractive but untrustworthy artifacts. To fix that, he proposes a four-stage workflow for Office files:

1. **Source preparation**
2. **Structure (file specification)**
3. **Constrained artifact creation**
4. **Verification by hostile review**

He emphasizes that this is not an edge-case process but what is required for trustworthy, scalable AI use in critical knowledge work.

## Stage 1: Source Preparation – Turn Messy Folders into Work Packets

Before asking for a deck or spreadsheet, the first step is to have AI inventory the available sources and organize them into a controlled work packet.

Key moves:

- Ask AI: What is in this folder? What can you see?
- Ensure every item has metadata: owner, date, file type.
- Create an index of evidence that lists all items with status:
  - Is the item current or superseded?
  - Is it an estimate, a transcript, raw data, a previous deck?
- Mark sensitivity: remove or flag sensitive material before any public-facing artifact is built.
- Check facts and estimates using web research, where appropriate.

By doing this, you prevent the model from blending disparate sources (like mixing transcripts, decks, spreadsheets, and half-remembered assumptions) into one confident answer. A messy folder becomes a coherent work packet with an explicit index, which constrains what the model can legitimately draw from.

He notes he has published a full source-packet template on his Substack, including an ID schema, status taxonomy, and conflict log, for teams who want to adopt this systematically.

## Stage 2: Structure – File Specifications as Blueprints

For serious work, no file should be created without first producing a clear file specification. The spec is a blueprint that explains where truth lives in the document.

### PowerPoint Specification

For a deck, the spec should include:

- **Narrative spine in plain English**: Who is the audience? What decision must they make? What must they believe first?
- **Slide list with claim headlines**: Each slide’s main claim spelled out clearly.
- **Source IDs** for each claim, pointing back to items in the evidence index.
- Identification of where charts are needed, what assumptions underlie them, and what questions remain open.

He warns that current models like “cute” or shorthand language; the spec should instead be in unambiguous, plain English that the human owner fully understands.

### Excel Specification

For a workbook, the spec should define the tab architecture and calculation flow:

- Which tab holds raw data.
- Where assumptions reside.
- Where calculations are performed.
- Where checks and validations are recorded.
- Which tab presents user-facing summaries and how those are driven.

The spec should make clear where authoritative values and logic live. He notes: if the blueprint does not explain where the truth resides, the finished file will not either.

Again, he references detailed templates on his Substack: PowerPoint narrative spine format, Excel tab architecture, assumption logs, conflict logs, and “checks tab” patterns.

## Stage 3: Constrained Creation – Building Under Spec and Source Limits

Only after sources are organized and a spec exists should AI build the artifact. The key principle is constraint: the model must build within the spec and the curated work packet, not by free-associating from its own training.

### PowerPoint: Two-Pass Creation

He recommends a two-pass approach for decks:

1. **Storyboard pass**:
   - Generate slide titles, claims, evidence links, and notes.
   - Do not design or render charts yet.
   - Focus solely on argument structure and evidence trail.

2. **Render pass**:
   - Once the storyboard is solid, then have AI render slides visually.

Separating argumentation from design prevents visual polish from hiding a weak or unsupported argument. Unsupported claims can be caught and fixed while still easy to edit.

In his own workflow, he currently uses Codeex for argumentation and Claude Opus 4.7 for deck rendering, as he finds Opus’s front-end polish particularly strong.

### Excel: Three-Layer Build

For workbooks, he uses a three-layer pattern:

1. **Layer 1 – Raw data**: Load the raw data exactly as-is.
2. **Layer 2 – Assumptions and calculation logic**: Implement formulas and assumptions.
3. **Layer 3 – Output views**: Build user-facing summaries and dashboards.

A key test: if you change a specific assumption, does the relevant output change for the right reason? A workbook that cannot recalculate meaningfully is not a model, and a model whose formulas cannot be inspected is not ready for decisions.

He currently has Codeex generate the Excel models for completeness of formulas, then uses Claude to make them visually cleaner.

## Task Risk Gradient – Where AI Is Safe vs. Dangerous

He introduces a “task risk gradient” for AI work inside Office files:

- **Low risk**: formatting, layout exploration, chart drafts, summary wording, consistency checks.
- **Medium risk**: source attribution, data extraction.
- **High risk**: numerical synthesis, financial calculations, regulatory or compliance language, and any claims destined for senior leadership decisions.

AI can accelerate all of these steps, but the review burden must scale with risk. High-risk tasks demand close human inspection, while low-risk tasks can be left more to the models.

## Stage 4: Verification – Hostile Reviewer Prompt

Verification is a distinct stage from proofreading. Its purpose is to determine whether the artifact can be trusted: whether claims, dates, formulas, assumptions, and charts are properly grounded and traceable.

He proposes a “hostile reviewer” pattern, where a model is instructed to read the artifact as if it suspects every claim and number. His prompt structure (paraphrased) is:

- Read this deck or workbook as a skeptical reviewer who doubts every claim and number.
- For each slide or sheet, list:
  - Claims without source attribution.
  - Numbers without a data source.
  - Charts whose underlying data is not traceable.
  - Formulas inconsistent across parallel rows or columns.
  - Assumptions presented as facts.
- Produce a written list of every issue.
- Do not fix anything; only enumerate issues.

The “don’t fix, just enumerate” instruction is crucial. It turns the task from generation to enumeration, letting the model focus on finding problems rather than maintaining a coherent revised artifact. Models are surprisingly good at catching their own earlier errors when reframed this way.

### The Ralph Loop: Playing Models Against Each Other

His personal workflow uses what he calls a “Ralph loop” between two models:

1. Use Codeex to create the document (deck or workbook).
2. Give the result to Claude Opus 4.7 with the hostile review prompt to generate a detailed edit list.
3. Feed that edit list back to Codeex and ask it to fix everything, producing a new version.
4. Return the new version to Opus and ask it to check the work.
5. Repeat until the artifact reaches “A-level” quality.

Near the end of this loop, he introduces an explicit language check: Opus is tasked with spotting LLM-isms like “you’re absolutely right” and pushing the text toward plain, human-readable English.

The goal is to have an autonomous loop that drives documents to very high quality with minimal human time, reserving human attention for final judgment: agreeing or disagreeing with key points and applying final polish.

## The System-Level View: Files as Outputs, Not the Whole System

He concludes that AI has already made it much easier to create Office files, and the productivity upside is large, because PowerPoint and Excel remain the primary way business judgment becomes visible. But the real upgrade is building a repeatable production system around these files.

In this new view:

- The file is just an output of a larger knowledge work system.
- The system includes source prep, structure, constrained creation, and verification.
- Simply dragging in sources and asking for a deck is the workflow that “loses you a meeting” when numbers cannot be defended.

Teams that build a “truth layer” around their AI-generated Office files—where every claim and calculation is traceable—will ship faster and be wrong less often. Teams that do not will ship impressive-looking decks with undefendable numbers, as illustrated by the example of OpenAI’s own launch chart that turned out to be famously wrong.

## Why This Isn’t Push-Button Simple

He anticipates the objection: why must individuals and teams build all this harness themselves? Why hasn’t someone made an easy push-button solution inside Office?

His answer: knowledge work is deeply contingent on domain knowledge. To produce specific, memorable, useful, and deep artifacts, you must understand the informational context well enough to custom-assemble the necessary pieces. You cannot assume a fixed template—like “five evidence slots per deck”—and expect serious work to fit.

Reality contains a surprising amount of detail, and good knowledge work mirrors that detail. This makes it hard to fully generalize a knowledge-work harness. Startups may improve pieces—information gathering, review communication, Excel checks—but the overall system must be shaped by domain experts.

He likens this to Luke Skywalker building his own lightsaber: to master the system, you must understand and assemble it yourself. It is also a rebuttal to the idea that AI will “turn our brains off”; in his framing, effective AI use actually requires keeping your brain fully engaged.

## Practical Next Steps for the Next AI-Built Deck

He suggests that the next AI-assisted deck should not begin with “make me a deck.” Instead:

- Write a narrative spine before opening the AI tool.
- Drop in source materials and ask for a source inventory.
- Ask for a conflict log before slide creation.
- Generate a storyboard with claims and notes before any visual rendering.
- Run the hostile reviewer prompt before sharing the document.

In every step, the model can help, but the human must remain responsible for the truth layer that makes the artifact trustworthy.

