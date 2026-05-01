---
title: Nvidia Can Make AI Labs 2x Faster – Jensen Huang
author: Dwarkesh Patel
source_id: 2
source_slug: dwarkesh-patel
url: https://www.youtube.com/watch?v=LlCUZFfJvRE
published_at: '2026-04-25T10:30:12Z'
duration_seconds: null
primary_theme: tech
secondary_theme: business
relevance: 8
hook: Jensen Huang explains why Nvidia’s stack dominates AI performance, cost, and adoption.
tldr: Jensen Huang argues Nvidia can often double or triple AI lab performance by deeply optimizing their software stack and kernels. He claims Nvidia offers the best performance-per-dollar and performance-per-watt for AI workloads, beating alternatives like TPUs on total cost of ownership. This superior efficiency, massive install base, and rich ecosystem create a flywheel that attracts cloud providers, startups, and customers to standardize on Nvidia.
caveats: It’s still Jensen selling Nvidia’s story, so treat the benchmark and TCO claims as claims unless you already want a strategic read on the company rather than a neutral technical teardown.
pitch: If you care about the real performance and cost levers behind AI infrastructure, this gives you Jensen Huang’s inside view on how Nvidia squeezes 2–3x gains out of the stack and why that ecosystem keeps winning in production.
---

## Key Points

- Nvidia assigns many engineers to AI labs to co-optimize their software stack and models.
- Nvidia GPUs are likened to F1 cars that require expertise to reach peak performance.
- Nvidia uses extensive AI techniques to generate and optimize its CUDA kernels.
- Jensen claims Nvidia’s optimizations often yield 2–3x model speedups, sometimes 50% gains, on existing fleets.
- He argues Nvidia has the best performance-per-TCO ratio in the world for AI computing.
- Jensen challenges TPU and Training AI claims, saying they do not show benchmarks like Inference Max or MLPerf to validate cost advantages.
- Cloud providers favor Nvidia because its ecosystem and reach bring them many external customers.
- Nvidia’s flywheel rests on performance-per-dollar, performance-per-watt, large install base, and ecosystem attracting tens of thousands of AI startups.

## Notes

## Nvidia’s Deep Involvement with AI Labs

- Nvidia dedicates a very large number of engineers to work directly with AI labs.
- These engineers help optimize the labs’ software stacks and specific kernels on Nvidia hardware.
- Huang emphasizes that no one understands Nvidia’s architecture better than Nvidia itself, and that this expertise matters because GPUs are not as general purpose as CPUs.

## GPU as F1 Racer vs CPU as Cadillac

- Huang compares CPUs to Cadillacs: comfortable, predictable, easy to drive, and never too fast.
- In contrast, he likens Nvidia accelerators to F1 race cars: powerful but requiring significant expertise to be pushed to the limit.
- He suggests many users can “drive” Nvidia hardware at a basic high speed, but true peak performance demands specialized knowledge.

## AI-Driven Kernel Optimization and Performance Gains

- Nvidia uses a large amount of AI internally to generate and optimize CUDA kernels.
- This AI-assisted kernel work is a key factor in extracting maximum performance from the hardware.
- Huang claims Nvidia’s involvement often yields substantial speedups for AI labs’ models.
- He cites typical gains of 2x speedups across the stack, with some cases reaching 3x or around 50% improvements.
- These improvements apply to the already-deployed fleet of Hopper and Blackwell GPUs at large labs.

## Revenue and TCO Impact of Performance Gains

- Huang stresses that a 2x performance gain on an existing GPU fleet is economically huge.
- Doubling performance on the same infrastructure effectively doubles the revenue-generating capacity of that fleet.
- He directly links increased tokens served or model throughput to higher revenues for AI labs and cloud providers.
- This framing leads to his core claim: Nvidia’s computing stack delivers the best performance per total cost of ownership (TCO) in the world.

## Claims of Performance-per-TCO Leadership

- Huang asserts that no other platform can demonstrate a better performance-to-TCO ratio than Nvidia for AI workloads.
- He says there is not a single company today that can show superior TCO performance.
- Public benchmarks, in his view, support Nvidia’s leadership.
- He references “Inference Max” as a benchmark available for others to use to demonstrate inference cost advantages but says no TPU competitor has done so.
- He also mentions MLPerf, inviting “Training on” and TPU providers to substantiate their repeated claims of a 40% advantage.
- He argues their cost-advantage stories make “zero sense” to him on first principles.

## Why Cloud Providers Favor Nvidia

- Approximately 60% of Nvidia’s customers are the top five customers, but most usage through clouds is external.
- At AWS, most Nvidia usage is for AWS’s external customers, not Amazon’s internal workloads.
- At Azure and OCI, Nvidia’s customers are likewise external users renting infrastructure.
- Huang argues clouds favor Nvidia because Nvidia’s ecosystem reach brings them many customers.
- Many of the world’s leading AI companies are already built on Nvidia, so clouds using Nvidia can attract those customers more easily.

## The Ecosystem Flywheel and Install Base

- Huang describes a “flywheel” built on install base, programmability, and ecosystem richness.
- Nvidia has a large, programmable architecture with a rich software and tooling ecosystem.
- There are now tens of thousands of AI companies globally, by his estimate.
- He argues that if you are one of these AI startups, you will choose the most abundant architecture.
- The deciding factors for startups are: where hardware is most available, where the install base is largest, and where the ecosystem is richest.
- Nvidia, in his telling, leads on all three, reinforcing its position.

## Performance per Dollar and per Watt

- Huang claims Nvidia’s performance per dollar (“perf per dollar”) gives customers the lowest cost per token.
- This is crucial for AI businesses whose revenue directly scales with tokens generated or inferences served.
- He also claims Nvidia has the highest performance per watt (“perf per watt”) of any architecture.
- For a partner building a 1 gigawatt data center, he argues the goal is to maximize tokens and thus revenues from that fixed power budget.
- Nvidia, he says, offers the highest tokens per watt, making it the best choice for maximizing revenue from power-constrained data centers.

## Renting Infrastructure and Customer Reach

- For companies whose goal is to rent AI infrastructure, customer access matters as much as raw performance.
- Nvidia claims to have the most customers in the world using its platform.
- This deep customer base and ecosystem make Nvidia the default choice for clouds that want to attract AI tenants.
- Huang concludes that these elements—perf per dollar, perf per watt, install base, and ecosystem—are what make Nvidia’s flywheel work and sustain its market dominance.

