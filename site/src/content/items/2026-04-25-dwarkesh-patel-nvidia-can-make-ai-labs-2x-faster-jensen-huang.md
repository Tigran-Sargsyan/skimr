---
title: Nvidia Can Make AI Labs 2x Faster – Jensen Huang
author: Dwarkesh Patel
source_id: 2
source_slug: dwarkesh-patel
url: https://www.youtube.com/watch?v=LlCUZFfJvRE
published_at: '2026-04-25T10:30:12Z'
duration_seconds: null
primary_theme: business
secondary_theme: tech
relevance: 7
hook: Nvidia claims its AI stack doubles customers’ effective GPU capacity without new hardware.
tldr: Jensen Huang argues that Nvidia’s close, hands-on optimization of AI customers’ software stacks commonly yields 2–3× speedups on existing GPU fleets, directly doubling revenues and tokens produced per watt. He asserts that no competing platform, including Google’s TPUs, can match Nvidia’s performance per total cost of ownership (TCO) or performance per watt, and challenges rivals to prove otherwise in public benchmarks like Inference Max and MLPerf. Huang attributes Nvidia’s dominance to a reinforcing flywheel of best-in-class cost/performance, power efficiency, massive installed base, programmability, and ecosystem depth that makes Nvidia the default choice for AI startups and cloud providers.
caveats: Skip it if you want independent analysis or deep technical evidence, because most of it is Jensen’s own sales pitch and benchmark framing rather than a neutral teardown.
pitch: If you care about AI infrastructure in the real world, this is a useful look at the economics and engineering behind why Nvidia keeps winning—especially the claims about 2–3× stack optimizations, TCO, power efficiency, and how those translate into effective capacity for labs and cloud providers.
---

## Key Points

- Nvidia assigns a very large number of engineers to work directly with AI labs on optimizing their software stacks.
- Nvidia’s accelerators are likened to F1 race cars: anyone can get basic performance, but expert tuning is required to fully exploit the architecture.
- Nvidia uses extensive AI to generate and refine its compute kernels, contributing to high performance.
- Huang believes Nvidia’s internal expertise will remain essential for labs to reach peak performance on its hardware for a long time.
- With Nvidia’s optimization help, AI labs often see 2× speedups in their stack, and sometimes 3× or 50% improvements on specific models or kernels.
- Such speedups on existing fleets of Hopper and Blackwell GPUs effectively double usable compute and directly translate into doubled revenues for AI labs.
- Huang claims Nvidia’s computing stack has the best performance per TCO (total cost of ownership) of any platform in the world, with no exceptions.
- He states that no company has demonstrated a better performance/TCO ratio than Nvidia on public benchmarks like Inference Max and MLPerf inference tests, which are available to everyone to use for comparison.
- Huang challenges Google’s TPU (and “Training on,” likely referring to TPU-based training claims) to substantiate its frequently cited 40% cost advantage in public benchmarks, arguing their cost claims make “zero sense” on first principles to him.
- He asserts that in practice, no TPU results “show up” to challenge Nvidia on these standardized inference and training benchmarks.
- Huang attributes Nvidia’s success primarily to its strong TCO economics, which he says are the core reason customers keep choosing them.
- Around 60% of Nvidia’s customers by volume are the top five hyperscalers, but most of that consumption is for those clouds’ external customers rather than their own internal workloads.
- At AWS, most Nvidia usage is for AWS’s external customers; at Azure and OCI, Nvidia’s customers are entirely external users of those clouds.
- Cloud providers favor Nvidia because its ecosystem and market reach allow them to attract “all of the great customers in the world” who are already building on Nvidia.
- Nvidia’s installed base, programmability, and rich ecosystem create a flywheel that keeps drawing new AI companies onto its platform.
- There are now tens of thousands of AI startups, and Huang argues that a rational startup will choose the architecture that is most abundant, has the largest installed base, and the richest ecosystem—criteria he says Nvidia uniquely satisfies.
- Huang claims Nvidia delivers the best performance per dollar, allowing customers to have the lowest cost per token for AI workloads.
- He also claims Nvidia has the highest performance per watt (“tokens per watt”) of any architecture globally.
- For a partner building a 1 gigawatt data center, Huang argues Nvidia lets that facility generate the maximum number of tokens and thus the highest possible revenue from that fixed power budget.
- If a company’s goal is to rent out AI infrastructure, Nvidia’s platform is most attractive because it has the largest customer base in the world.
- These factors—cost/performance, power efficiency, installed base, programmability, and customer reach—mutually reinforce each other into a powerful flywheel for Nvidia’s continued dominance.

## Notes

### Nvidia’s Optimization Effort and Hardware Analogy

- Nvidia dedicates an “insane” number of engineers to work directly with AI labs, focusing on optimizing their software stacks.
- Nvidia’s accelerators are compared to F1 race cars: while most users can “drive” them at a basic level (e.g., 100 mph), only deep experts can push them to their true limits.
- Unlike general-purpose CPUs (likened to easy, comfortable Cadillacs), Nvidia’s GPUs require specialized knowledge to reach peak performance.
- Nvidia uses a large amount of AI internally to design and optimize the kernels that run on its accelerators.
- Huang believes this specialized expertise will be needed “for quite some time,” implying customers cannot yet fully self-optimize on Nvidia hardware.

### Impact of Stack Optimization on Customer Economics

- By collaborating with labs and tuning their stacks or specific kernels, Nvidia frequently achieves substantial performance improvements.
- Typical results Huang cites include 2× speedups; sometimes stack or model performance improves by 3× or by about 50%.
- These improvements apply to existing fleets of Hopper and Blackwell GPUs already installed in customers’ data centers.
- A 2× performance uplift on the installed base effectively doubles usable compute capacity without buying more hardware.
- Huang states this 2× performance increase “doubles their revenues,” because more tokens or model outputs can be sold over the same hardware base.

### Claims About TCO and Benchmark Superiority

- Huang asserts that Nvidia’s computing stack delivers the best performance per total cost of ownership (TCO) in the world, without exception.
- He says no other platform can demonstrate a superior performance/TCO ratio.
- Public benchmarks like “Inference Max” (an inference cost benchmark) are, according to him, available for everyone to use.
- He claims no TPU-based system has shown up to beat Nvidia there; similarly, in MLPerf inference, rivals do not present results that undercut Nvidia’s cost.
- Huang explicitly challenges TPU advocates and “Training on” (likely shorthand for TPU training claims) to prove their oft-cited 40% cost advantage.
- He says the claimed TPU cost superiority makes “absolutely zero sense” to him on first-principles grounds, and that no public benchmark supports it.
- He concludes that Nvidia’s outstanding TCO is a central reason for its commercial success.

### Customer Mix and Cloud Provider Incentives

- About 60% of Nvidia’s customers are concentrated in the top five hyperscale providers.
- For AWS, most Nvidia GPU usage serves AWS’s external customers, not AWS’s own internal workloads.
- At Azure and Oracle Cloud Infrastructure (OCI), Nvidia’s customers on those platforms are entirely external users.
- Cloud providers favor Nvidia because its ecosystem and reach bring them “all of the great customers in the world,” who already build on Nvidia.

### The Nvidia Flywheel: Installed Base, Ecosystem, and Efficiency

- Nvidia’s flywheel is described as a combination of:
  - A large installed base of Nvidia GPUs.
  - High programmability of the architecture.
  - A rich software and tools ecosystem.
  - Tens of thousands of AI companies already building on Nvidia.
- For a new AI startup choosing hardware, Huang argues they will rationally pick the most abundant architecture, with the largest installed base and richest ecosystem—criteria he claims Nvidia meets.
- He states Nvidia offers the best performance per dollar, yielding the lowest token costs for customers.
- Nvidia is also claimed to have the highest performance per watt, i.e., the most tokens produced per watt of power.
- For a 1 gigawatt data center, Huang says Nvidia enables the maximum possible token output and thus the highest revenue from a fixed power budget.
- If the business model is renting infrastructure, Nvidia’s platform is attractive because it has the largest pool of customers in the world.
- All of these factors—TCO advantage, power efficiency, installed base, programmability, ecosystem, and customer reach—reinforce each other into a self-sustaining flywheel that strengthens Nvidia’s position over time.

