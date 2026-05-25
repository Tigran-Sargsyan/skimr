---
title: Why the AI boom is about to hit a wall
author: Nate B Jones
source_id: 1
source_slug: nate-b-jones
url: https://www.youtube.com/watch?v=Poyi6X7rOwY
published_at: '2026-05-24T17:00:23Z'
duration_seconds: null
primary_theme: business
secondary_theme: tech
relevance: 8
hook: AI growth is constrained by industrial bottlenecks, not GPUs or software features.
tldr: Nate Jones argues that the current AI boom is running into hard industrial constraints far below GPUs, especially high-bandwidth memory, advanced packaging, power, and data center construction. This shifts hyperscalers from pure software businesses into capital-intensive factory operators, and turns every AI software deal into an implicit supply contract layered on their constrained capacity. Executives must therefore treat AI strategy as managing a production line for tokens, rewriting procurement, forecasting, and risk questions around capacity, routing, utilization, and hidden human supervision.
caveats: If you want hands-on engineering detail about model serving, evals, or agent systems rather than macro-level supply-chain and hyperscaler economics, this will feel a layer too high.
pitch: You should read this if you care about AI infrastructure because it treats the boom like a real production system — with HBM, packaging, power, datacenter buildouts, and capex constraints that directly affect how LLM capacity gets bought, routed, and monetized.
---

## Key Points

- Microsoft plans $190B in 2024 capex and still expects to be capacity constrained in AI infrastructure.
- The main AI bottlenecks lie in high-bandwidth memory and advanced packaging, not in logic die design.
- Hyperscalers now operate AI factories with physical bills of materials including chips, memory, power, cooling, and construction.
- AI software vendors depend on hyperscaler allocation, making AI contracts effectively supply contracts tied to upstream capacity.
- High-bandwidth memory shortages can strand GPUs, preventing usable accelerators despite ample compute on paper.
- Power, cooling, and multi‑year data center construction timelines increasingly determine when new AI capacity comes online.
- Token utilization and depreciation windows make underutilized AI capacity financially dangerous for hyperscalers and customers.
- Cheaper tokens from efficiency gains can paradoxically increase overall demand, sustaining capacity constraints via Jevons’ paradox.

## Notes

## From Software Contracts to Industrial Supply Contracts

- Microsoft’s Q3 call announced $190B in 2024 capex, yet Nadella still expects to be “capacity constrained.”
- “Capacity constrained” is not about running out of GPUs; it refers to deeper supply limits in the AI factory stack.
- Six months ago, AI vendor contracts mostly resembled traditional software contracts; now they function as de facto supply contracts.
- AI vendors must secure hyperscaler capacity and allocate tokens to customers, so contracts should include allocation tiers, capacity terms, and fallback plans.
- Developers and engineers must be at the table because token usage patterns and technical realities drive whether allocated capacity is actually usable.
- Example: Jones personally used ~500 million tokens in a week, illustrating how quickly engineering teams can consume capacity.

## AI as an Industrial System, Not Just Software

- Users see ChatGPT, Copilot, Gemini, Claude as familiar software interfaces, but each response is the output of a production chip system.
- Every word generated comes from an “AI factory” comprising chips, memory, packaging, networking, power, cooling, land, construction, and operations.
- Intelligence at scale now has a physical bill of materials in a way traditional software never did.
- Hyperscalers—Microsoft, Meta, Amazon, Google—have transitioned into physical infrastructure operators with huge, ongoing capex commitments.

## Hyperscaler Capex and Strategic Shift

- Meta plans to spend $125–145B this year, raising guidance because components are more expensive and more data centers are needed.
- Meta is losing the AI race yet still must spend heavily, demonstrating there is “no way out” of the infra build.
- Amazon deployed over 2.1 million AI chips in the last 12 months, more than half its own Trainium, plus commitments to Anthropic, OpenAI, and over a million Nvidia GPUs through 2027.
- Google spent $185B last year; Jones frames this as part of a broader pattern, not isolated strategies.
- The correct mental model is to treat hyperscalers as physical infrastructure companies whose unit economics resemble industrial operations.

## The AI Factory’s Core Building Block: Modules, Not GPUs

- The relevant physical unit is the module or rack-scale system, not an individual GPU.
- Example: Nvidia GB200 NVL72 module:
  - Liquid-cooled rack-scale system.
  - 72 Blackwell GPUs and 36 Grace CPUs in a single NVLink domain.
  - 13.5 TB of HBM3 and 576 TB/s of memory bandwidth.
  - Positioned as infrastructure for real-time trillion-parameter inference.
- A chip alone doesn’t produce intelligence at scale; it needs tightly coupled memory, packaging, networking, and a facility to run in.

## High-Bandwidth Memory and Packaging as Bottlenecks

- High-bandwidth memory (HBM) is the single most constrained input in the AI supply chain.
- Without sufficient HBM and data movement bandwidth, compute sits idle despite available GPUs.
- A provider can appear to have plenty of GPUs yet fail to ship usable AI accelerators because it cannot source enough HBM.
- Advanced packaging integrates logic dies and HBM stacks into a working chip package.
- TSMC’s CoWoS (referred to as co-ass) connects compute and memory at the bandwidth levels AI workloads require.
- Substrates and interposers carry signals and maintain alignment; low substrate yield can slow production regardless of chip design quality.
- Optics become crucial because large AI clusters are “communication machines” as much as compute engines.
- At the scale of hundreds of thousands of GPUs, copper’s heat and distance limits make optical networking mandatory.
- Nvidia’s Spectrum-X Photonics is cited as an example of shipping products embodying this optical infrastructure shift.

## Power, Cooling, and Data Center Construction Constraints

- Power availability is a central constraint: firms must secure guaranteed power at specific locations and timelines, not just overall grid capacity.
- National-level power availability figures (e.g., IEA’s 945 TWh data-center consumption projection by 2030) obscure local constraints.
- Local site power, grid interconnection, and transmission determine whether and when a data center can be built and energized.
- Communities and local regulators are increasingly pushing back on large data centers and their power draw.
- Dense AI racks generate heat beyond what older data center designs anticipated, making liquid cooling part of baseline production capacity.
- If cooling cannot support rack density, hardware cannot run at full power, reducing effective capacity.
- Traditional 12–18 month data center build timelines are no longer valid for 500 MW+ AI campuses.
- Transmission and interconnection complexities can stretch projects to four years or more.
- Example: Meta’s Hyperion campus in Louisiana (with Blue Owl Capital) is already a multi-year construction effort.

## Multi-Layer Supply Chain and Where the Real Bottlenecks Are

- AI factories span multiple layers: chips, HBM, packaging, substrates, optics, power, cooling, and construction.
- Each layer has distinct suppliers, lead times, and potential bottlenecks; any single layer can constrain a given data center.
- Epic AI estimates for 2025:
  - The four largest AI chip designers consume about 90% of global advanced chip packaging capacity.
  - They also consume about 90% of global HBM supply.
  - Yet they use only ~12% of advanced logic die production.
- This implies that the bottleneck is not chip design capability or sheer GPU count but integrated compute supply: combining logic, HBM, and packaging into usable accelerators.
- Nadella’s “capacity constrained” comment reflects these integrated supply limits, not just GPU counts.

## Financial and Capital Cycle Implications

- Traditional software finance looked at revenue growth, gross margin, sales efficiency, retention, and free cash flow.
- AI adds a much tougher capital cycle underneath these metrics.
- GPU assets depreciate over 3–5 years, whereas data center shells last longer, often unevenly matched with future rack generations.
- In some cases, existing shells cannot be reused for the newest racks, complicating asset life assumptions.
- CFOs must ask whether they can earn enough from capacity before hardware generations change cost curves.
- This question applies beyond hyperscalers because all customers rely on their factories for tokens.
- Low utilization is dangerous: depreciation clocks run regardless of tokens served, so unused capacity harms economics.

## Hyperscalers as Both Suppliers and Competitors for Compute

- Hyperscalers must juggle internal product needs and customer demand for the same compute resources.
- Microsoft needs GPUs for Copilot and Azure customers.
- Google needs them for Gemini, Cloud, Search, and Workspace.
- Amazon needs them for AWS, Bedrock, and Trainium commitments.
- Meta mostly consumes AI capacity internally, but then must self-fund the entire industrial base.
- Buyers must recognize cloud providers as both product competitors and chip-allocation competitors.

## How to Forecast Demand: Tokens, Not Seats

- Many organizations forecast AI demand in terms of seats, licenses, users, or projects; this is inadequate.
- Proper forecasting must include:
  - Tokens per workflow.
  - Context lengths.
  - Model calls per task.
  - Agent loop behaviors.
  - Concurrency levels.
  - Latency tiers and failure/retry rates.
- Different use cases have drastically different capacity profiles:
  - A customer support chatbot vs. an autonomous claims processing agent.
  - A simple coding assistant vs. an agent that reads repos, writes code, runs tests, and loops for hours.
- Forecasting adoption alone leads to under-budgeting capacity.
- Forecasting only budget leads to overpaying for the wrong infrastructure layer.

## Efficiency Gains vs. Jevons’ Paradox

- Serving costs per unit of performance are falling quickly across many AI tasks.
- Drivers of efficiency include smaller models, distillation, caching, batching, quantization, speculative decoding, and better routing.
- These improvements allow more work per unit of capacity.
- Jones suggests that a model like Opus 4.7 or ChatGPT 5.5 in May 2026 will likely have similar open-weight, self-hostable equivalents by December.
- Microsoft reported a 40% improvement in Copilot inference throughput in a single quarter via software and hardware optimization.
- Such gains are equivalent to building new factory capacity without construction.
- However, cheaper tokens also stimulate greater usage: longer contexts, more agents, more retries.
- This reflects Jevons’ paradox: efficiency gains can increase total consumption.
- If efficiency outruns demand growth, the current massive industrial buildout could be overshooting.
- So far, demand growth has outpaced efficiency, justifying continued capex.

## Why Jones Does Not See an AI Bubble (Yet)

- The industrial constraints and real utilization pressures distinguish the current cycle from a pure speculative bubble.
- He references a separate unit-economics framework for 2026 that offers a “capacity proof” and bubble test.
- By that test, he argues we are not in a bubble yet, though readers are encouraged to apply the framework themselves.

## Executive Imperatives and Contract Questions

- Every AI vendor contract sits atop this constrained industrial supply chain, even if parties avoid discussing it.
- Buyers often feel awkward probing supply chain details; vendors may lack clear answers on allocation and fallback.
- Executives should normalize honest conversations about uncertainty, allocation, and risk.
- Three core questions for AI investment reviews:
  1. What share of AI spend is reserved capacity versus best-efforts allocation, and what is the written fallback plan if the default provider is supply constrained for 1–2 months?
  2. What is the routing plan for sending work to cheaper models, and how will savings be measured without hurting user experience?
  3. In the top three workflows, where is hidden human supervision masking product failures, and how would you detect if that supervision disappears?
- Many vendors run clean demos because humans silently correct errors; in production, unseen human work can distort pricing and scalability assumptions.

## The End of “Invisible Cloud” and the New Executive Role

- In the 2010s cloud era, the winning abstraction was elastic compute; developers acted as if infrastructure were always available.
- That abstraction is now broken for intelligence: AI capacity is constrained by the industrial factory underneath.
- Microsoft’s $190B capex symbolizes how software giants must think like industrial operators.
- They need supply assurance, throughput optimization, capacity scheduling, utilization management, and depreciation discipline.
- Executives must treat AI strategy like managing a production line: understanding where tokens originate, which data centers serve them, and how capacity scales when new customers join.
- Buying AI is effectively buying a share of factory output—tokens from an industrial facility—not generic software licenses.
- This reality shifts the executive job description, requiring deeper due diligence across technical, contractual, and physical layers.
- Jones frames 2026 as a year when leaders must fully own decisions across every layer of the AI factory.
- He argues that this new, physically grounded intelligence economy is more complex and interesting than the homogeneous “software tastes like chicken” era, and demands that executives dive deep rather than rely on old MBA-era software playbooks.

