---
title: OpenAI founder admits AI isn’t working
author: Mo Bitar (atmoio)
source_id: 4
source_slug: mo-bitar-atmoio
url: https://www.youtube.com/watch?v=ZugX7a99dLk
published_at: '2026-05-18T14:00:50Z'
duration_seconds: null
primary_theme: tech
secondary_theme: thinking
relevance: 6
hook: Karpathy’s candid anecdotes expose how fragile current AI coding really is.
tldr: Andrej Karpathy describes relying heavily on AI coding tools while admitting their outputs are often bloated, brittle, and occasionally catastrophic. Mo Bitar highlights the contradiction between claims of reduced oversight and Karpathy’s “heart attack” reactions to the generated code. The video also outlines how software hiring and individual preparation should shift toward spec‑writing and one‑shot agentic engineering, while stressing that even industry leaders lack clear answers about AI’s future impact on skills.
caveats: It looks more like commentary on Karpathy anecdotes than a deep technical postmortem, so skip it if you want hard evals, benchmarks, or architecture-level detail.
pitch: If you want a quick, builder-flavored reality check on AI coding hype, this gives you a useful reminder that even Karpathy sees the brittleness, bloat, and failure modes you worry about in real agentic systems.
---

## Key Points

- Karpathy claims he has mostly stopped checking AI-generated code because it now makes fewer mistakes.
- He also admits that inspecting AI-generated code sometimes gives him a “heart attack” due to its poor quality.
- AI code is often bloaty, copy‑pasted, and built on brittle abstractions, even when it works.
- Karpathy recounts an AI agent making a nonsensical assumption in his Menu Genen app that could have been catastrophic.
- He describes LLMs as sophisticated autocomplete systems limited by their base data and reinforcement learning coverage.
- Karpathy says that if a task is absent from training and RL data, an LLM simply cannot solve it.
- He proposes that software hiring should pivot from LeetCode puzzles to evaluating large, spec‑driven projects with agents.
- Bitar notes that even Karpathy struggles to say which human skills will remain valuable if AI improves significantly.

## Notes

## Karpathy’s Reliance on AI Coding vs. Its Failures

Andrej Karpathy, a key OpenAI founder associated with “vibe coding,” describes a heavy dependence on AI coding tools. He says he used to constantly correct AI-generated code but now has “stopped checking the output,” presenting this as productivity progress. Mo Bitar finds this framing disturbing, because reviewing code used to be the core responsibility of a software engineer. 

Immediately after saying he no longer checks results, Karpathy describes failures that undermine that confidence. He marvels that models can refactor 100,000-line codebases and handle complex engineering tasks, yet fail trivial reasoning questions like counting the letter “r” in “strawberry” or deciding whether to drive or walk to a car wash. Bitar emphasizes the contradiction: Karpathy is asking “How is this possible?” even though he helped design this system.

## Concrete Example: Menu Genen and Catastrophic Risks

Karpathy shares an example from his own app, Menu Genen, where an AI agent made a bizarre assumption related to reusing emails. Although the technical details are convoluted, the key point is that this mistake “didn’t make any sense” and could have been catastrophic if he had not caught it. He relays the story in a light, self-deprecating tone, as if it were a charming anecdote about silly AI behavior. 

Bitar pushes back strongly on the idea that this is funny. The same technology is being proposed for serious domains like medicine and tax preparation, where analogous “silly” errors would be unacceptable. For Bitar, catastrophic potential from subtle, nonsensical assumptions is a central reason AI cannot be treated casually.

## The “Heart Attack” Code Quality

Karpathy candidly admits that when he actually inspects AI-generated code, he sometimes gets “a little bit of a heart attack.” He describes the code as not “super amazing” and often “very bloaty,” with lots of copy‑paste and brittle, awkward abstractions. The code may function but is “really gross” from a design and maintainability perspective. 

Bitar interprets this as revealing the true frontier of current AI: it often produces operational but low-quality, hard-to-maintain software. He argues many engineers hyping AI will not admit this publicly because they rely on executives not knowing how bad the underlying code is. He jokes that startups will need defibrillators at the office for engineers reviewing AI-generated pull requests, framing the room’s laughter as missing the seriousness of the problem.

## Karpathy’s Agentic Workflow: Specs First, Code Second

Karpathy describes his workflow as heavily spec-driven. He writes an extremely detailed markdown document in English, specifying everything the code should do, including all edge cases, and tries to be as precise as possible. Only then does he have the AI generate code from that document. Bitar notes this mirrors writing a very detailed, complex logical document where correctness is crucial.

When Karpathy later examines the resulting code, he sometimes asks the model to simplify it. According to him, the model will claim it cannot simplify further, even when he, as a skilled engineer, clearly sees simplifications. This suggests that even for tasks like code simplification and abstraction, the model has notable limitations.

## Limits of LLMs: Data Coverage and RL

Karpathy repeatedly returns to reinforcement learning (RL) and training data as the core explanation of these limits. He describes RL as a curated “cherry on top” of the base training data, teaching the model specific skills. He stresses that if a task is not well represented in either the base data or the RL dataset, no force can make that LLM reliably solve the problem. 

From this, he effectively characterizes LLMs as very sophisticated autocomplete systems. Their competence is bounded by what they have been exposed to and shaped for, not by general reasoning capabilities that can universally extend beyond training coverage.

## Tension Between Optimism and Honest Doubt

There is a clear tension in Karpathy’s stance. On one side, he frames himself as an AI accelerationist, enthusiastic about agentic systems and vibe coding, and he tries to preface criticism by affirming he is “not an AI skeptic.” On the other side, his stories reveal fear and discomfort: catastrophic near-misses, “heart attack” code quality, and explicit acknowledgment of fundamental model limitations.

Bitar highlights this as a bizarre contradiction: Karpathy claims to have stopped checking AI output while simultaneously describing that the output routinely alarms him. The video suggests that even central figures of the field are navigating cognitive dissonance between their promotional narratives and their lived experience of AI systems.

## Rethinking Software Hiring for Agentic Engineering

Karpathy says many companies are now trying to hire “strong agentic engineers,” but their hiring processes have not been updated. Most still rely on LeetCode-style questions and puzzle-like technical problems. He argues hiring should instead resemble giving candidates a large project to implement with agents, such as building a Twitter (X) clone. The assessment should include making it “really good” and “really secure,” reflecting real-world complexity.

In this framework, the key skill is writing high-quality specs rather than hand-writing every line of code. Bitar emphasizes that candidates should practice writing specifications at home: for example, drafting a detailed spec for a Twitter clone. If they have never done this, they are likely to omit crucial aspects like tokens, session length, cookie expiration, password changes, and rate limiting. Those missing details would cause AI agents to choke or behave incorrectly during implementation.

## One-Shot Agentic Skill and Interview Preparation

Bitar reframes “agentic engineering” as being less about low-level coding and more about knowing when and how to feed problems to tools like Claude. The real skill lies in not handing tasks to the agent too early, which would create noisy back-and-forth. Instead, the goal is to “one‑shot” tasks with a very strong initial spec. 

In interviews, there is usually no time for four hours of iterative agent interaction, except in take-home assignments. So candidates will effectively be tested on their ability to one-shot: to write a spec that an agent can execute with minimal iteration. Bitar suggests practicing complex subsystems—like recommendation engines—beforehand. That way, in an interview, a candidate might impress by including “also build a recommender system algorithm” in the prompt, something they would not think to add without prior practice.

## Industry Uncertainty and Shared Confusion

Toward the end, the interviewer asks Karpathy what skills will remain valuable if AI continues to improve and what people should learn now. Bitar observes that Karpathy’s answer feels empty and unsatisfying, not because of a lack of intelligence, but because the questions themselves are extremely difficult and unresolved. 

Bitar concludes that even someone like Karpathy “doesn’t really have the answers” about where the industry is headed or which human capabilities will be durable. He suggests viewers who feel lost about their future in an AI-saturated world can find some comfort in the fact that even top insiders share this uncertainty. The overarching sentiment is one of honesty about powerful tools that are still poorly understood and dangerously fallible.

