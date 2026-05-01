---
title: 'StrongDM''s three person team ships with zero human code review #ai #engineering'
author: Nate B Jones
source_id: 1
source_slug: nate-b-jones
url: https://www.youtube.com/watch?v=eY1u8Ni9ClQ
published_at: '2026-04-25T21:00:30Z'
duration_seconds: null
primary_theme: tech
secondary_theme: null
relevance: 3
hook: AI models are now writing and optimizing the code that builds their own successors.
tldr: Codex 5.3 at OpenAI and Claude Code at Anthropic are concrete examples of AI systems building themselves. Earlier generations of these models now analyze logs, flag issues, and directly author production code for newer versions. As a result, engineering roles at these companies are shifting from manual coding toward specification, direction, and judgment over largely AI-generated codebases.
caveats: Skip it if you want concrete architecture, evals, or failure modes; this reads like hype about AI writing code rather than a substantive engineering case study.
pitch: You might skim this only as a signal of where AI-coding marketing is going, but it does not look like the kind of grounded, production-level engineering analysis you usually care about.
---

## Key Points

- Codex 5.3 is described as a frontier AI model that was instrumental in creating itself.
- Earlier Codex builds analyzed training logs, flagged failing tests, and suggested fixes to training scripts.
- Codex 5.3 shipped as a direct product of its own predecessor model’s coding labor.
- OpenAI reported Codex 5.3 development saw a 25% speed improvement over prior efforts.
- OpenAI also reported 93% fewer wasted tokens in building Codex 5.3 compared to before.
- Model-identified inefficiencies during the build process contributed to these Codex 5.3 improvements.
- Anthropic’s Claude Code produced about 90% of the code in the Claude Code tool, including itself.
- Anthropic leadership predicts the company is transitioning to entirely AI-generated code, changing engineers’ roles toward specification and judgment.

## Notes

## Self-Referential Development in Frontier Models

The speaker describes a "self-referential loop" emerging at both Anthropic and OpenAI, where advanced AI models are actively involved in building their own successors. This is not positioned as a metaphor or marketing flourish but as a concrete engineering practice involving real production tooling and code.

## Codex 5.3 Building Itself

Codex 5.3 is highlighted as the first frontier AI model that was fundamentally instrumental in its own creation. Earlier versions of Codex were already integrated into the development workflow: they analyzed training logs, flagged failing tests, and suggested fixes to training scripts. These earlier capabilities meant the model was functioning as an assistant that could understand the training pipeline and propose targeted interventions when issues appeared.

With Codex 5.3, the relationship deepened. The model is said to have shipped as a direct product of its own predecessor’s coding labor, meaning substantial portions of the code and configuration that produced Codex 5.3 were written by a prior Codex model. This goes beyond debugging suggestions and into primary authorship of production code that underpins the training and deployment process.

## Measurable Efficiency Gains at OpenAI

OpenAI reportedly observed specific quantitative improvements in the process of building Codex 5.3. Development was 25% faster compared to earlier efforts, indicating a significant reduction in time-to-ship for a new frontier model. Additionally, they saw 93% fewer wasted tokens during the build process, suggesting that compute and model-inference usage became far more efficient.

The speaker attributes these improvements in part to the model identifying its own inefficiencies during development. In other words, the AI system was used to introspect tooling and workflows, find waste or redundancy, and propose optimized alternatives, feeding into an iterative loop of self-improvement in its own training and deployment stack.

## Claude Code’s Self-Generated Codebase

Anthropic’s Claude Code exhibits a parallel pattern. According to the speaker, 90% of the code associated with Claude Code, including the tool itself, was built by Claude Code. This means the tool is largely self-authored, with only a small fraction of code written directly by human engineers.

The proportion of self-generated code is said to be rapidly converging toward 100%. This implies that, over time, maintenance, feature development, and refinements are increasingly delegated to the model, further reinforcing the self-referential development loop.

## Changing Role of Engineers at Anthropic

Boris Trenne is cited as saying he has not written code in the last few months. The speaker clarifies that this is not hyperbole but reflects a genuine shift in his work: his responsibilities have moved from hands-on coding to specification, direction, and judgment.

In this model, humans define what should be built, articulate requirements, and evaluate the quality and safety of the AI-generated outputs, rather than manually implementing most of the code. Anthropic is estimated to be at the point where the whole company is moving to entirely AI-generated code, marking a transition from human-centric coding to AI-centric code production overseen and guided by human decision-makers.

## Broader Implication in the Transcript

Across both organizations, the pattern described is of AI systems embedded deeply in the software development lifecycle, not just as assistants but as primary authors and optimizers. This yields measurable gains in speed and efficiency, while reconfiguring engineering roles around higher-level specification and critical judgment instead of routine implementation.

