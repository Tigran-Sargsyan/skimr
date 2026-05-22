---
title: Opus 4.7 and OpenAI 5.5 Made Your Prompting Style Obsolete.
author: Nate B Jones
source_id: 1
source_slug: nate-b-jones
url: https://www.youtube.com/watch?v=ogTLWGBc3cE
published_at: '2026-05-21T14:01:12Z'
duration_seconds: null
primary_theme: tech
secondary_theme: thinking
relevance: 4
hook: Treat frontier AI like a senior partner, not a junior assistant you micromanage.
tldr: Nate argues that classic “prompt engineering” is now table stakes because modern agentic models like Opus 4.7 and OpenAI 5.5 are vastly more capable. Instead of crafting rigid task prompts for a junior-like model, you should adopt an “AI question method” that treats the system as a senior partner doing deep, high-leverage knowledge work alongside you. This method centers on asking intent-rich questions, inviting synthesis across complex inputs, and explicitly tying your thesis and data together so the AI can contend with and even challenge your perspective.
caveats: It looks more like trend-driven commentary than engineering evidence, so skip it if you want concrete evals, benchmarks, or production failure modes.
pitch: If you want to sanity-check how the current AI discourse is reframing prompting for agentic models, this is a quick way to see the mental model some users and product people are picking up.
---

## Key Points

- Prompt engineering as a standalone discipline is now table stakes rather than a differentiating skill.
- Recent models like Opus 4.7 and OpenAI 5.5 enable far more powerful, persistent agentic workflows.
- Most people still prompt as if AI were a junior assistant needing tightly scoped tasks.
- Nate’s “AI question method” reframes interactions as a manager partnering with a senior colleague.
- Principle one is to ask questions that clearly convey your perspective and focus, like a flashlight beam.
- Principle two is to ask multiple open-ended questions that force the AI to synthesize what good looks like.
- Principle three is to ask questions that make the AI wrestle with both hard data and your explicit thesis.
- Modern AI memory lets you even prime the system to remind you when you are not asking strong questions.

## Notes

## From Prompt Engineering to the “AI Question Method”

- Classic prompt engineering is described as a “2025 conversation”: still necessary but no longer sufficient.
- Knowing how to prompt is now table stakes; you need to be good at it but you no longer get special credit.
- The real frontier now is *what comes on top* of prompt engineering, especially with powerful agentic workflows.
- Labs often say, “just ask AI for what you want,” but this only works if people actually know what they want.
- As workflows become more complex, people struggle to articulate their needs clearly enough for that advice to work.

## Why the Shift Now: 4.7 and 5.5

- In the last few months, new models like Anthropic’s Opus 4.7 and OpenAI’s 5.5 have changed what is possible.
- These models can:
  - Call tools more effectively.
  - Work with data more flexibly.
  - Sustain longer, more complex work sessions.
- Nate claims these agents are “100 times more powerful” than models from six to eight months ago, in practical terms.
- However, human prompting habits have *not* evolved at the same pace, creating a mismatch between model power and how people use it.

## Senior Partner vs Junior Partner Mental Model

- Last year, AI behaved more like a junior team member: you needed to give very specific, carefully scoped tasks.
- Prompt engineering, in that world, was about decomposing tasks and instructing the model precisely.
- Nate argues that current frontier models should be treated like *senior partners*, not juniors.
- A senior partner mental model means:
  - You are not specifying every step.
  - You are engaging them in co-discovery and strategic thinking.
  - You rely on their ability to explore, synthesize, and push back.
- The shift is from “give the AI a task” to “partner with the AI on a problem.”

## What Nate Means by “Agents” vs “Agentic Pipelines”

- Nate defines an *agent* here as a setup where you sit with a frontier model and do heavy knowledge work together.
- This includes tools like co-work, claude code, codeex, and similar high-context, tool-using environments.
- This mode can be applied when planning coding projects or doing any deep thinking where the end output might be code, documents, decks, etc.
- He distinguishes this from *agentic pipelines*:
  - Pipelines handle structured, repeatable workflows (e.g., routing customer service tickets, processing invoices).
  - They are supposed to be buttoned up and predictable, with minimal open-ended reasoning.
  - They still use tools and can be called “agents,” but you don’t interact with them conversationally.
- The talk focuses on the *interactive* heavy-knowledge-work agents, not pipelines.

## The AI Question Method: Core Idea

- Nate wants to move beyond the word “prompting” because it implies a simple ask-and-answer pattern.
- He proposes the “AI question method,” which reframes the interaction as a manager working with a senior partner.
- Your core job becomes: *formulating questions* that let the agent do its best strategic and creative work.
- This involves:
  - Understanding your own thesis or perspective.
  - Expressing that perspective within questions.
  - Giving enough structure to guide, but enough openness for exploration.
- He notes that many people’s current prompts reflect the older junior-partner mental model and fail to exploit modern capabilities.

## Principle 1: Questions with a Clear “Flashlight” of Intent

- Principle one: your questions must convey a clear center of intent plus room to explore—like a flashlight beam.
- Good managers shape questions to signal where they are looking, even if they don’t know the final answer.
- Being clear about your perspective is essential.
  - Weak example: “Help me learn more about the Mona Lisa.”
  - Stronger example: “I want you to learn more about the Mona Lisa from the perspective of Da Vinci’s later life and how the painting shaped his relationships with peers, because I have a thesis that the Mona Lisa influenced those relationships.”
- In business terms, you might say: “I have a thesis that our marketing attribution is broken because we haven’t correctly separated Google organic. Investigate the data with that in mind.”
- The question conveys:
  - A center of the bullseye (your thesis).
  - Space for the AI to explore around it.
- You should also explicitly define boundaries and exclusions.
  - Example: Combining meeting notes and files into a report but asking the AI to completely exclude a 15-minute tangential topic from the output.
- The art is avoiding both overly open-ended and overly closed questions, while still signaling direction and edges.

## Principle 2: Questions That Explore “What Good Looks Like” via Synthesis

- Principle two: ask questions that invite the AI to explore what a good outcome looks like, not just follow an eval.
- Nate values evals, especially for agentic pipelines, but emphasizes they are not enough for complex, creative outputs.
- For documents like Amazon-style PR FAQs, it’s hard to encode “goodness” fully in a formal eval.
- Instead, you can:
  - State the context (e.g., a new Prime Video feature with 3D sports figures on your living room floor).
  - Ask the AI to reason about user experience challenges, such as:
    - Making the experience accessible to people unfamiliar with 3D.
    - Consciously adopting a customer perspective.
  - Then ask further questions: how to convey the interplay between software and hardware in both press release and internal FAQ.
- Crucially, you are not dictating the exact text; you are asking the AI to wrestle with multiple, difficult questions and synthesize.
- This pattern—multiple open-ended but targeted questions—takes advantage of the model’s increased power versus older versions.
- Nate observes that when he looks at how people prompt, he rarely sees them using this multi-question, synthesis-inviting style.
- He suggests you can build muscle for these questions by leaning into curiosity and consistently thinking of AI as a senior partner.

## Principle 3: Questions That Tie Data and Your Thesis Together

- Principle three: ask questions that make the AI engage both with your data/files and with your explicit opinions.
- Good managers present:
  - Concrete artifacts (documents, metrics, transcripts).
  - Their own working hypotheses or theses about what those artifacts mean.
- Nate uses Codeex as an example environment where he:
  - Copies and reorganizes diverse files into a single working context folder (docs, decks, spreadsheets, code, meeting transcripts).
  - Leverages large context windows to have the AI pull from many sources.
- A common failure mode is prompts that cause the AI to focus heavily on just one file or narrow subset of data.
- To counter this, he asks questions that explicitly demand breadth:
  - Name the types of data and artifacts you want it to consider.
  - State your thesis and ask it to test or refine that thesis across *all* sources.
- Example product-management scenario:
  - Goal: increase monthly recurring revenue for a product with multiple levers.
  - Data sources: previous experiments, voice-of-customer transcripts, support tickets, PRDs, launch docs, analytics.
  - First, have the AI organize all these into a clean folder.
  - Then ask a long, structured question:
    - State a hypothesis, e.g., product-led growth is not yielding good margins.
    - Point to evidence you suspect: flat MRR, weak launch performance, patterns in PRDs.
    - Ask the AI to look across *all* these data sources and return its own best explanatory thesis.
    - Allow disagreement: it can conclude that product-led growth is not the true issue.
- The question challenges the AI to:
  - Use your perspective as a starting point.
  - Digest all data sources.
  - Produce a clean, elegant, explanatory view of the problem.

## Using Memory and Meta-Prompting to Improve Your Questioning

- Modern systems with memory let you set up the AI to help you improve your own questioning habits.
- Nate notes you can:
  - Prime the AI with instructions about the kind of questions you *want* to ask.
  - Have it remind or nudge you when you fall back into shallow or task-only prompting.
- He mentions having quick-start guides and example prompts on his Substack that:
  - Teach the question method.
  - Help you practice by conversing with the AI itself about how you’re asking questions.

## Overall Takeaways

- The world of prompt engineering as a differentiated practice is largely “behind us,” in Nate’s framing.
- Prompt engineering still matters, but as baseline competence rather than a source of advantage.
- The next level is learning to:
  - Treat powerful models as senior partners.
  - Use an AI question method focused on intent-rich, exploratory, and data-conscious questioning.
- The words of prompts were never the deepest part; *intent* was always central.
- Now, that intent is best expressed through a sharp series of questions that:
  - Clarify focus and boundaries.
  - Invite synthesis across complex, overlapping concerns.
  - Explicitly integrate your theses with the data you provide.
- Nate encourages taking the transcript itself to an AI companion, practicing these patterns, and iterating on the questioning style as a new core skill for 2026-level AI work.

