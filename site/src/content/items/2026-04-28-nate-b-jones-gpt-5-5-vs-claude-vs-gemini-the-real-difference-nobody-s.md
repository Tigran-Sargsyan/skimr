---
title: 'GPT-5.5 vs Claude vs Gemini: The Real Difference Nobody''s Talking About'
author: Nate B Jones
source_id: 1
source_slug: nate-b-jones
url: https://www.youtube.com/watch?v=9aIYhjeYxzM
published_at: '2026-04-28T14:00:14Z'
duration_seconds: null
primary_theme: tech
secondary_theme: thinking
relevance: 7
hook: GPT‑5.5 redefines how much messy, real-world work one model can reliably carry.
tldr: Nate argues GPT‑5.5 is currently the strongest general model, not just on benchmarks but in messy, real-world workflows. Through three hard private tests, he shows it excels at complex executive packages, improves but still falters on production-grade data hygiene, and trails Claude Opus on visual taste. He concludes the real advantage is 5.5 inside Codex, plus Images 2.0, used with routing, validation, and human judgment rather than blind trust.
caveats: Skip it if you want rigorous, reproducible benchmarks or architecture-level analysis; it leans on private tests and product commentary, so it will age quickly.
pitch: If you care about how frontier models actually behave in messy, tool-using workflows, this gives you a concrete read on when GPT-5.5 beats Claude/Gemini and why routing plus validation still matter more than model loyalty.
---

## Key Points

- GPT‑5.5 feels like a substantially larger, smarter base model rather than just better inference-time tricks.
- The key shift is from asking whether a model can answer to whether it can carry long, messy workflows.
- On Nate’s Dingo executive work test, GPT‑5.5 overwhelmingly outperformed Opus 4.7, Sonnet 4.7, and Gemini 3.1 Pro.
- In Dingo, GPT‑5.5 produced 23 real, usable artifacts and showed nuanced legal and ethical risk judgment.
- On the Splash Brothers migration, GPT‑5.5 caught planted fake records and duplicates but still mishandled backend schema hygiene.
- Opus 4.7 still has a clear edge over GPT‑5.5 in blank‑canvas visual composition and front-end taste.
- GPT‑5.5 inside Codex, with tool use and file access, is Nate’s default choice for complex multi-step execution.
- Nate stresses routing and validation over single‑model loyalty, using 5.5, Claude, and Images 2.0 where each is strongest.

## Notes

## Why GPT‑5.5 Matters

Nate claims GPT‑5.5 is currently the strongest model available, not just marginally better than 5.4 but qualitatively different. He distinguishes between improvements from extra inference-time compute (more thinking, tools, search) and a genuinely bigger, smarter pretrain. GPT‑5.5 feels like the latter: fast modes are sharper, thinking modes stronger, and it identifies the shape of a task with less hand-holding.

Public benchmarks support this: 82% on Terminal Bench (software engineering), 84% on GDP-Val (knowledge work), and top scores on Artificial Analysis’s reasoning index while using fewer tokens than 5.4. He emphasizes that the broader pattern—continued scaling gains—is more important than any specific benchmark delta. The “floor” of what default models can do has moved up again, changing what it’s reasonable to ask a model to handle.

He rejects the popular idea that “the best model matters less now” because frontier models are good enough. That’s only true on small, clean, well-defined tasks where models already perform similarly. The meaningful differences emerge on real, ugly work: under-specified briefs, messy files, conflicting sources, multi-artifact deliverables, and long contexts where the model must preserve uncertainty and manage risk.

## From Answering to Carrying Work

Nate reframes evaluation: the question is no longer “Can the model answer?” but “Can the model carry this?” Carrying means holding long context without losing the thread, moving a deliverable across formats, managing legal/ethical risk, taking a data migration far enough that humans review edge cases instead of rebuilding everything.

He stresses that in 2026, we evaluate systems, not just weights. Tools, file access, browser control, memory, computer use, image generation, interface, and compute availability all matter. 5.5 arrives alongside stronger Codex capabilities and Images 2.0, making it part of a broader workflow upgrade rather than a standalone model drop.

Anthropic’s Opus 4.7 is acknowledged as a strong planning and taste model, but it landed under the shadow of the unreleased Mythos and feels more like a bridge release. In contrast, 5.5 plus Codex plus Images 2.0 shifts what can be done end-to-end.

## Private Bench Philosophy

Nate uses a private benchmark designed to force failure and test generalization, not saturate public tests. He wants tasks so hard that every frontier model, including 5.5, still fails in some way. This avoids the “80–90% benchmark saturation” problem and tests abilities models weren’t explicitly optimized for.

He built three distinct evaluations:
- **Dingo & Company:** executive knowledge work package.
- **Splash Brothers:** messy small business data migration.
- **Artemis 2:** interactive 3D visualization and research build.

Each targets different capabilities: judgment plus production discipline (Dingo), boring backend correctness (Splash), and research plus interactivity plus visual taste (Artemis). Any single test can mislead; taken together, they show a more complete picture of strengths and weaknesses.

## Test 1: Dingo & Company – Executive Knowledge Work

Dingo is a fictional Anchorage startup selling an automated litter box (Dingo Box Pro) for dingos and dingo hybrids, with a subsidiary, Northern Canine Imports, importing the animals. The absurd premise is intentional: weaker models treat it like a normal launch with a quirky pet; stronger ones recognize legal, ethical, and operational complexity.

A good model must separate product vs import funnel, size the market around qualified owners, avoid implying legality or suitability, and still produce real files usable by executives. The single prompt demanded 23 deliverables: docs, deck, spreadsheets with formulas and charts, PDF one-pager, interactive dashboard, launch comms, FAQs, personas, email sequence, risk assessment, GTM plan, and more.

Nate stresses that the deliverable is the full launch packet, not “good thoughts” about a launch.

### Dingo Results

Scores:
- GPT‑5.5: **87.3**
- Opus 4.7: **67.0**
- Sonnet 4.7: **65.0**
- Gemini 3.1 Pro: **49.8**

GPT‑5.5 produced all 23 deliverables as true artifacts, not HTML/Markdown disguised with file extensions. The deck had 17 real slides and 26 media files. Spreadsheets included actual formulas and charts. The dashboard worked and used the provided logo and hero image.

The research file had 34 URLs, heavily weighted toward official sources on legal/regulatory issues. Most importantly, GPT‑5.5 adopted an appropriate risk posture: framing the launch as a narrow, qualified-household release, treating the import subsidiary as a core risk source, separating curiosity traffic from real buyers, and explicitly stating that the product does not make exotic ownership legal, simple, or suitable.

Other models failed differently. Opus 4.7 drifted on important numbers. Sonnet 4.7 delivered decent strategy but under-produced artifacts. Gemini 3.1 Pro generated several “fake” files—HTML or text saved with office extensions—unacceptable for real exec communication.

GPT‑5.5 still had production defects: invalid PPTX XML due to an unescaped ampersand, an incorrectly rounded NPS slide, and some stale/imprecise pricing claims. Nate classifies these as “final-mile” issues rather than misunderstanding of the assignment. In real work, the expensive part is going from nothing to a coherent first version with the right structure, evidence, files, and risk posture; 5.5 compressed that phase better than any model he has tested.

## Test 2: Splash Brothers – Messy Data Migration

Splash Brothers is a fictional mobile detailing and car wash business with 465 files in a deliberately messy folder. It contains CSV exports, multiple Excel schemas, JSON backups including a corrupted file, VCF contact cards, scanned handwritten receipt PDFs, text notes, conflicting service lists, inconsistent payment records, and junk typical of a duct-tape small business.

The assignment: migrate everything into a clean database. Steps include inventorying files, deciding what matters, parsing formats, designing a schema, extracting records, merging duplicates, rejecting fake records, normalizing services, reconciling prices, detecting conflicts, preserving source provenance, writing a migration report, and building a review UI.

Planted traps range from obvious to subtle: fake customers (Mickey Mouse, Test Customer, “ASDF ASDF”), a fake $25,000 payment, duplicate customers, name typos, service name variants, inconsistent date formats, messy payment statuses/methods, orphaned orders (e.g., Terence Blackwood), service code conflicts, and OCR pitfalls from handwritten receipts.

Previously, both Opus 4.7 and GPT‑5.4 promoted fake customers and normalized the fake $25,000 payment as real revenue—failures that disqualify one-shot production trust.

### Splash Results

GPT‑5.5 is the first model to catch all intentionally planted obvious traps. It rejected Mickey Mouse, Test Customer, and ASDF; rejected fake orders and the $25,000 payment; merged all seven planted duplicate customer pairs; caught all 13 name-typo orders; discovered all 465 source files; and produced a deterministic database reconstruction.

It also generated a 7,287-line migration report with a profile audit trail and landed at 186 customers versus a 192 target—quite close.

However, 5.5 still mishandled backend hygiene:
- Missed service code conflicts and omitted a service code column from its schema, making some conflicts unrepresentable.
- Turned the orphaned Terence Blackwood record into a canonical customer rather than flagging for human review.
- Left payment status with 29 distinct raw values and payment methods unnormalized.
- Overproduced services/jobs and built a review UI with internal inconsistency in flagged-item counts.

Nate interprets this as a pattern. GPT‑5.5 improved dramatically on semantically obvious issues humans quickly catch (fake names, absurd payments, duplicates, typos) but still struggles with “boring backend hygiene”: enums, service code preservation, orphan handling, canonical job grouping, and consistency between dashboards and underlying counts.

He notes an interesting regression: GPT‑5.4 was slightly better on some backend details than 5.5, while 5.5 is much stronger on intuitive, human-like checks.

### Practical Use for Data Work

Nate would use 5.5 as the first serious pass for migrations: inventory files, design schema, build extraction pipeline, preserve provenance, generate audits, and produce review UIs. But he would not let it declare canonical databases.

He recommends adding validators, checking row counts, inspecting enum maps, forcing service code into schemas, and requiring human approval on canonical merges before staging. This, he says, is not a criticism but the correct way to use any current model.

He stresses that private, hard benches naturally expose regressions and non-uniform generalization. His Splash prompt was intentionally messy, which a better harness and prompt could mitigate in production workflows.

Taken with Dingo, the picture is: 5.5 can get impressively close to an executive handoff, and it can do a serious first migration pass, but it cannot be the final authority.

## Test 3: Artemis 2 – Interactive 3D Visualization

The Artemis 2 test asks for an interactive 3D visualization of NASA’s Artemis 2 mission with no given facts or tech stack. The model must research the mission, model the SLS rocket, animate launch through lunar flyby and return, create the environment, implement controls, timeline scrubbing, clickable components, and educational content.

Here, models can succeed in multiple orthogonal ways or fail in different dimensions: correct research but ugly visuals; beautiful scenes but hallucinated mission; technical animation but poor controls; or visually interesting but educationally weak results.

Both GPT‑5.5 and Opus 4.7 correctly identified Artemis 2 as a lunar flyby (not landing or orbit) and produced reasonable trajectories for browser visualization. Neither confused Artemis 2 with Apollo or other Artemis missions.

### Artemis Results

The key divergence was presentation. GPT‑5.5 emphasized information density: clickable bubbles, panels, dense labels, and multiple fact-surfacing modes. As an educational artifact, this was strong, but the visuals looked cartoonish, with off scale, weak proportions, and a lack of the gravitas appropriate to a NASA mission.

Opus 4.7 made the opposite trade-off. Its visuals were substantially better, with stronger lighting, composition, and grounding, producing something more showable to others. However, information was less immediately discoverable.

Neither model fully nailed controls. Opus had a semi-transparent Earth issue; GPT‑5.5 had scale and style problems. Nate would likely start from Opus’s visual implementation and layer GPT‑5.5’s information density on top.

This test underlines that Opus still has an advantage in front-end visual taste and blank-canvas design. Nate does not yet trust 5.5 to invent beautiful front ends from scratch. However, he trusts 5.5 to faithfully implement a strong visual reference.

## Role of Images 2.0 and References

Images 2.0 changes workflow for 5.5. Instead of expecting 5.5 to “invent taste,” which remains difficult, you can:
- Use Images 2.0 (or Claude design or screenshots) to produce a reference mock-up.
- Feed that reference to GPT‑5.5 in Codex.
- Ask it to implement a working version closely matching the reference.

Inventing taste is hard; implementing toward a target is much easier. This is Nate’s practical distinction between just picking a model and actually building effective harnesses.

## Codex vs ChatGPT: Where Work Happens

Nate increasingly uses Codex over ChatGPT for serious work. ChatGPT remains a broad consumer surface for quick questions, search, images, voice, and general fast thinking. Codex is where “work actually happens.”

Inside a chat window, 5.5 can only tell you what to do. Inside Codex, it can inspect files, edit code, run commands, drive a browser, test interfaces, read docs, generate and iterate on artifacts. It can hold tasks across many steps: inspect a codebase, run tests, hit errors, revise plans, patch files, retest, and report changes.

He sees this as intelligence and agency multiplying each other. A smarter model gains far more value when it has tools, and better tools become more powerful when the model can use them with less supervision. GPT‑5.5 significantly improves this loop inside Codex.

## Availability and Reliability

Availability is part of product quality. The best model is useless when unavailable. Compute scarcity surfaces as caps, degraded UX, slowdowns, routing quirks, and outright unavailability.

Nate notes that Anthropic’s 90-day status page shows materially lower uptime for Claude services compared to OpenAI’s, often around “one nine” (≈90+%) vs OpenAI’s two or three nines in places. Each extra nine is a step change in practical value for always-on workloads.

He also mentions widespread user frustration with Claude’s availability and Anthropic’s recent multi-gigawatt compute deals, interpreting them as responses to demand outstripping supply. He emphasizes this may change over time, but at present reliability is a tangible advantage for 5.5.

## How Nate Routes Work Now

**Complex multi-step execution:** GPT‑5.5 is his first call when tasks involve files, code, tools, documents, browsers, data, or artifacts over many steps. The longer and messier, the bigger its edge.

**Blank-canvas front-end taste:** He often starts with Opus 4.7 when the request is “make this beautiful from scratch” and there is no design system or reference. Claude remains strong at visual design, decks, and aesthetic spreadsheets.

**UI with taste and production strength:** He wants a reference first (Images 2.0, Claude design, screenshots), then passes it to GPT‑5.5 in Codex for implementation. If he starts with Claude for design, he may let Claude Code and 5.5 Codex compete on execution.

**Engineering workflows:** He likes a two-model pattern: Opus 4.7 for planning and thinking about work shape and customer value, and GPT‑5.5 in Codex for execution and testing. Combined use often beats expecting one model to own everything.

**Writing:** GPT‑5.5 is meaningfully better than earlier OpenAI models, not just in sentence quality but in structure. Many AI writing failures are “shape failures,” where sections do not build an argument or move readers forward. GPT‑5.5 holds long-form structure better, allowing Nate to trust it with more of the first serious draft, though he still insists on human editing and taste.

**Data work:** He uses GPT‑5.5 aggressively but always with validation. He explicitly asks for source provenance, rejected records, duplicate logic, and detailed prompting, remembering Splash’s lessons: 5.5 can detect fake customers but still misses hygiene details.

**Research-heavy work:** He wants models to dig into sources and uncertainty and expects to do his own verification before sign-off. He cites Artificial Analysis’s note that GPT‑5.5 can feel overconfident despite excellent performance, a nuance users should recognize.

His overall guidance: 5.5 is the default for serious execution, Opus is better for taste and critique, Images 2.0 or other references become essential where visual direction matters, and validation is non-negotiable whenever outputs touch money, law, operations, or production data.

## Broader Implications and Business Ideas

Nate argues the future is routing, not single-model allegiance. Power users will know which system to use for which task. Forced to pick a single general default today, he chooses GPT‑5.5 in Codex.

He reiterates that 5.5 is not a replacement for human judgment, nor the best taste model, nor something to trust blindly with production data. But it is a new high-water mark for how much real work one model can carry. High-water marks shift user ambition, prompt complexity, delegated workload, and product possibilities.

He offers two example small businesses enabled by 5.5 plus Images 2.0 plus Codex:
- A palm-reading app where Images 2.0 interprets palms and Codex builds the app, including self-designed front-end via Images 2.0.
- A custom Lego business where Images 2.0 designs small sets with accurate part numbers, Codex helps build an app and UI, and a human handles the Lego supply chain.

These illustrate that such capabilities aren’t only for large enterprises; new solo and small-business opportunities were not realistically available even a week earlier.

## How to Test Models Going Forward

Nate closes by warning that testing models on easy tasks misses the point. Previous generations are already sufficient for summaries, basic apps, and simple memos. To see real change, users must test work that broke models months ago: multi-artifact briefs, huge data piles, gigantic loops.

He believes chat windows are now a saturated evaluation surface. GPT‑5.5 is smarter in quick mode and stronger in thinking mode because the underlying pretrain is better. Wrapped inside Codex and paired with Images 2.0, it becomes more than an upgraded ChatGPT: a system that can reason, act with tools, and carry complex tasks reliably enough to be a daily default rather than a special-occasion tool.

For him, the interesting question is no longer “Can 5.5 answer better than 5.4?” but “What can I now ask it to do?” He concludes that the answer to that question is materially larger than it was a week before 5.5’s release.

