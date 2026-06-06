---
title: Sam Altman is starting to panic
author: Mo Bitar (atmoio)
source_id: 4
source_slug: mo-bitar-atmoio
url: https://www.youtube.com/watch?v=lwjVjD3oQJg
published_at: '2026-06-05T16:40:24Z'
duration_seconds: null
primary_theme: business
secondary_theme: tech
relevance: 7
hook: Enterprise AI spending is behaving like an addictive, unprofitable casino for everyone involved.
tldr: Uber’s internal AI demo and subsequent cost overrun reveal how generative AI use is structurally expensive and economically irrational at scale. Companies like Uber, Walmart, Microsoft, and GitHub are quietly slashing or restructuring AI usage as token-based billing exposes runaway costs. Meanwhile, OpenAI must IPO despite burning cash, leaning on growth stories and hype while the practical value of AI remains narrow and often unprofitable.
caveats: Skip it if you want rigorous systems analysis or audited numbers rather than a skeptical, hype-cutting business take built around a few high-profile anecdotes.
pitch: If you care about the economics of shipping LLMs in production, this is worth your time because it lays out the ugly cost dynamics, incentive failures, and enterprise rollback patterns that can bite real AI products like the ones you work on.
---

## Key Points

- Uber’s CTO ran a two‑hour internal LLM demo that cost $1,200 in tokens alone.
- Uber’s 2026 AI budget was completely exhausted by April, mostly on low‑value tasks like email summaries and specs.
- Uber initially celebrated teams by how many AI tokens they burned, then reversed to reward minimal spending.
- The speaker argues LLMs are structurally inefficient because each generated token rereads the entire prior context.
- Generative AI is likened to a slot machine using intermittent rewards to keep engineers repeatedly prompting despite low overall reliability.
- Walmart’s internal AI agent “Code Puppy” and Microsoft’s own AI cloud usage were both heavily cut back due to cost.
- GitHub Copilot’s switch to token‑based billing caused some customers’ prices to spike by 100x.
- OpenAI is losing more than a dollar for every dollar of revenue and needs an IPO to keep funding losses.

## Notes

## Uber’s AI Demo and Cost Shock

- Uber’s CTO, portrayed as an aging tech executive desperate not to appear outdated, stages a two‑hour live demo of an LLM to impress leadership.
- The session is framed as proof that AI will save money and transform workflows, and executives enthusiastically react as if witnessing something revolutionary.
- Afterward, the cost for the two‑hour demo is revealed: $1,200 in token spend alone.
- This demo was meant to showcase cost savings but instead cost more than the work it was supposed to replace, making it a symbolic contradiction.

## Token Leaderboards and Misaligned Incentives

- Uber maintained an internal dashboard ranking teams by how many AI tokens they consumed.
- The team burning through tokens fastest was praised and celebrated, effectively incentivizing waste rather than efficiency.
- The analogy used is ranking chefs by electricity usage rather than food output, making the biggest wasters “employee of the month.”

## Blowing the 2026 AI Budget by April

- Uber had set what it thought was a prudent AI budget for the entirety of 2026 to avoid runaway costs.
- That entire annual budget was blown by April, just four months in.
- The spend was not associated with major new features, market expansions, or transformative products.
- Instead, the money went to low‑leverage tasks: summarizing emails, writing specs, and generating huge amounts of text that mostly went unread.
- One spec is joked about as becoming so long it “gained sentience” and deleted itself as an act of mercy, emphasizing useless verbosity.
- Uber’s COO reportedly called the budget overrun a “head exploding moment,” signaling shock at how quickly costs spiraled.

## From Spend-Maximization to Spend-Minimization

- In response, Uber flips the incentives: now the lowest token spend wins rather than the highest.
- Each engineer is capped at $1,500 per month in AI usage, which is still significant when multiplied across roughly 5,000 engineers.
- The new frame is how long teams can “edge the machine” without “blowing their load,” i.e., how much they can restrain usage.

## Structural Inefficiency of LLMs

- The speaker initially held out hope that AI economics would eventually work out as companies optimized costs over time.
- He now questions this, arguing that the underlying autoregressive LLM architecture is structurally inefficient.
- For each new word generated, the model must reread the entire prior conversation, multiplying computational cost with context length.
- This is described as inefficiency “at the deepest level,” suggesting cost problems are not just implementation details but inherent to the design.

## AI as a Slot Machine and Addiction Mechanism

- The speaker insists he is being literal, not metaphorical, in calling LLMs “slot machines.”
- Users “pull the lever” by prompting the model; sometimes they get a helpful output, giving a strong dopamine hit.
- Roughly 20% of the time, code or answers are good enough to feel magical; about 80% of the time, outputs are “confident nonsense.”
- This intermittent reinforcement pattern mirrors known addictive designs, keeping users engaged despite frequent failure.
- Engineers agonize over whether to do work themselves or try “one more” AI prompt, reinforcing the slot‑machine dynamic.
- Leaderboards and enterprise pressure amplify this addiction by rewarding high usage.

## Industry-Wide Cost Hangover

- The Uber case is presented as a microcosm of a broader “psychosis” across the industry.
- Walmart built an internal agent called “Code Puppy” and gave teams effectively unlimited tokens.
- When the bill arrived, Walmart sharply curtailed the program, described as sending Code Puppy to a farm and neutering the initiative.
- Microsoft, despite owning a large stake in OpenAI, is reportedly canceling some of its own cloud licenses due to similar cost concerns.
- GitHub Copilot switched customers to token‑based billing, resulting in up to 100‑fold price increases for some users.
- Across these cases, AI is not widely praised for making companies efficient machines; instead, it is acknowledged as solving some problems while creating many new ones, especially around cost and reliability.

## The Economics of AI: No Profits Yet

- The claim is that no one has made AI profitable in a sustainable way so far.
- At best, AI provides pockets of value but is hard to integrate, expensive to run, and riddled with tradeoffs.
- The current phase is described as a “sobering up,” with companies realizing the mismatch between hype and economics.

## OpenAI’s Financial Pressure and IPO Imperative

- This environment is depicted as “really bad news” for Sam Altman, who needs to take OpenAI public.
- He is on an enterprise roadshow, and during a talk he notes that companies are suddenly complaining about pricing.
- He frames this as a new issue, but the speaker sees it as existential, suggesting the “bubble” is starting to crinkle.
- Altman does not present a convincing plan to control costs; he just moves past the concern.
- OpenAI is said to lose $1.22 for every $1 of revenue, meaning it is deeply unprofitable.
- Major funding sources such as SoftBank and Saudi capital are portrayed as largely tapped out, leaving the public markets as the remaining option.
- The IPO is framed as OpenAI needing money from regular investors to keep the “casino” running.

## Why IPO If It’s Unsustainable?

- The speaker gives two reasons: OpenAI has no choice, and markets reward growth and vision over present profitability.
- AI can be sold as the “birth of a new species,” allowing investors to overlook ongoing losses.
- When stock performance wobbles, leadership figures like Dario are imagined making moral arguments, accusing skeptics of trying to “short a conscious being.”
- The speaker suggests this storytelling is persuasive enough that the public will likely buy it, just as they are buying current AI narratives.

## Predicted Future of AI: Narrow, Supervised, and Costly

- The prediction is that AI will become real and useful but in narrow domains.
- Coding and other verifiable tasks may benefit, but only when humans vigilantly supervise outputs “like a disappointed Asian dad.”
- For most other uses, AI remains an expensive way to be confidently wrong, with addiction‑like feedback loops keeping usage high.

## Generative-Only Paradigm and Cost Explosion

- The speaker emphasizes that generative AI only knows how to create new content, not edit existing artifacts directly.
- When you ask for a small tweak, models regenerate the entire output from scratch instead of incrementally editing.
- In images, a tweak means fully rebuilding the image rather than moving pixels, exemplifying all‑or‑nothing generation.
- This “generate, generate, generate” behavior drives enormous volume, which directly translates into huge bills.
- The cost explosion is thus presented as a natural outcome of the technology’s fundamental operation, not just mismanagement.

## Closing Image: Hype, Ego, and the Lever

- Much of the AI mania is attributed to older executives’ fear of being labeled out‑of‑touch and mocked as “boomers.”
- To avoid that stigma, they over‑embrace AI in visible ways, contributing to irrational spending.
- The video ends by looping back to the slot‑machine metaphor, inviting the viewer to “pull the lever one more time” while mocking the Uber CTO’s expensive, underwhelming demo as “mid.”

