---
title: 'Codex Just Valued A Random House In India. I Wasn''t Ready. #codex'
author: Nate B Jones
source_id: 1
source_slug: nate-b-jones
url: https://www.youtube.com/watch?v=oWIXee9h3nU
published_at: '2026-05-14T22:01:02Z'
duration_seconds: null
primary_theme: tech
secondary_theme: business
relevance: 4
hook: A quick experiment shows Codex accurately valuing a random house from a Street View image.
tldr: The speaker tests whether Codex can combine image recognition, web search, and reasoning to price a house. Using only a Google Street View screenshot and map widget of a random home in Gwalior, India, Codex produced a detailed valuation report. A local real estate contact judged the estimate as solid, surprising both her and the experimenter about the system’s capabilities.
caveats: It’s mostly a flashy anecdote with almost no technical depth, eval rigor, or failure analysis, so if you want production substance you should skip it.
pitch: If you’re tracking what current agent tooling can actually do, this is a compact real-world demo of a multimodal model combining images, search, and reasoning on a messy task rather than a toy benchmark.
---

## Key Points

- The experimenter chose a small tier‑three city in India, Gwalior, to ensure an obscure domain.
- He captured a random house via Google Street View plus the neighborhood map widget screenshot.
- He prompted Codex in roughly two lines to determine the house’s value using only those images.
- Codex produced a one‑page report with price range, confidence level, and underlying rationale.
- The report also described what factors would change the valuation range and referenced other Gwalior properties.
- The entire Codex task took roughly one and a half to two minutes to run.
- A real estate professional familiar with the market graded the valuation as solid and accurate.
- The experiment convinced the speaker that combining search, reasoning, and images yields unexpectedly powerful results.

## Notes

## Experimental Setup

The speaker wanted to probe how far current AI models can go when combining multiple capabilities: image recognition, web search, and reasoning. To make the task nontrivial, he deliberately chose a “tier three” city in India, Gwalior, which he characterizes as a small city and therefore a relatively obscure market with high specificity. The goal was to see if a model could operate effectively in a domain that is not heavily documented or standardized in mainstream datasets.

He opened Google Maps, navigated to Street View in a residential neighborhood of Gwalior, and selected a completely random house. He emphasizes he had no prior knowledge of the property or its owners. He took a screenshot of the front of the house from Street View, capturing only what a typical user would see.

In addition to the facade screenshot, he also grabbed a screenshot of the little yellow Street View widget on the map, effectively giving spatial context for where in the city the house is located. These two images formed the full input beyond the short text prompt.

## Prompt and Model Interaction

He used Codex and provided a very short prompt—about two lines of text. The prompt essentially instructed Codex that its task was to use the provided information to determine the value of the house. There was no extensive engineering of instructions; the test was more about capability than careful guiding.

Codex had access to the house image and the neighborhood map widget image. Based on these, plus whatever search tools it could leverage, it was expected to infer approximate location, property type, and local context, then synthesize a valuation.

The whole process took on the order of one and a half to two minutes from submission to receiving a response, suggesting the model and its tools operated quickly even on this open‑ended estimation problem.

## Output: Valuation and Reasoning

Codex returned a full one‑page response rather than a short number. It specified a valuation range, essentially answering how much the house was likely worth. It also expressed a confidence level in its estimate, making its own uncertainty explicit.

The response explained what its estimate was based on. This included contextual reasoning drawn from the images and from information about other houses in Gwalior, implying that Codex used search to locate comparable properties or market data. It further articulated factors that would change its valuation range, pointing to variables that, if known more precisely, could tighten or shift the estimate.

Thus the output was not just a raw price guess but a structured piece of reasoning: range, justification, confidence, and sensitivity to additional information.

## Ground‑Truth Check with a Real Estate Professional

To assess whether Codex’s performance was actually good, the speaker sought ground truth from someone working in real estate who knew the Gwalior market. He showed this person the one‑page valuation and asked her to judge its quality on a letter‑grade scale, such as A, B, or C.

The real estate contact evaluated the answer as “solid.” She was apparently surprised at how accurate and reasonable it was, especially given that it was generated from only a facade image, a map widget, and a brief prompt. Her reaction served as external validation that the valuation was not lucky noise but within a credible range for that local market.

## Takeaways on Model Capabilities

The speaker himself was also surprised by the result, stating that the model “got it.” He notes that he did not know in advance whether this would work at all; the experiment was intentionally exploratory, essentially “throwing” a tough, unusual task at the model.

The experience leads him to a broader conclusion: when you combine search with reasoning and image understanding in a single system, you can get unexpectedly strong and practical results. In this example, those capabilities allowed Codex to infer a property’s approximate market value in an unfamiliar city from minimal visual and contextual cues.

He presents this as evidence that users should actively push models with ambitious, composite tasks instead of assuming their limits prematurely, because the integration of tools and modalities may enable performance that is not obvious from simpler, isolated tests.

