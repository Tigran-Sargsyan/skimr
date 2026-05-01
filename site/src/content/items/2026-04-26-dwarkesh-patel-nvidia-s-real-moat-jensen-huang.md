---
title: NVIDIA's Real Moat – Jensen Huang
author: Dwarkesh Patel
source_id: 2
source_slug: dwarkesh-patel
url: https://www.youtube.com/watch?v=mW1KWTjaggk
published_at: '2026-04-26T13:45:20Z'
duration_seconds: null
primary_theme: tech
secondary_theme: null
relevance: 8
hook: Jensen Huang explains why CUDA, not just GPUs, is NVIDIA’s enduring moat in AI.
tldr: Jensen Huang argues that CUDA’s rich, well-tested software ecosystem makes it the natural foundation for building advanced AI systems. Developers prefer CUDA because their code will run across NVIDIA’s massive installed base of GPUs in every major cloud and many devices. This combination of ecosystem depth, installation scale, and deployment flexibility makes CUDA uniquely valuable for Frontier AI development.
caveats: It’s more platform strategy than hard engineering detail, so you should skip it if you want failure modes, benchmarks, or low-level implementation scars.
pitch: If you care about the real infrastructure moat behind AI systems, this gives you Jensen’s case for why CUDA’s software ecosystem, installed base, and cloud/on-prem portability matter more than GPU silicon alone.
---

## Key Points

- CUDA is a rich, programmable ecosystem that supports essentially every major AI framework and many emerging ones.
- NVIDIA contributes significant technology to frameworks like Triton, whose backend is heavily powered by NVIDIA code.
- Multiple new frameworks (e.g., Triton, vLLM, SGLang, Nemo RL, and other RL/post‑training tools) are rapidly emerging on top of CUDA.
- Developers benefit from building on CUDA because a huge, well-tested codebase underneath makes bugs more likely to be in their own code rather than in the platform.
- Despite remaining bugs, CUDA and NVIDIA’s stack are highly “wrung out,” providing a reliable foundation for complex AI systems.
- For any software developer, the most important factor is installed base: they want their software to run on many machines, not just one setup.
- NVIDIA’s CUDA ecosystem spans several hundred million GPUs across many generations (A10, A100, H100, H200, L‑series, P‑series, etc.).
- The breadth of NVIDIA’s GPU lineup and form factors lets the same CUDA stack run from data centers down into robots and other devices, increasing reuse of models and code everywhere CUDA exists.
- NVIDIA GPUs with CUDA are present in every major cloud provider, which is critical for AI builders who may not know in advance which cloud they will use or partner with.
- CUDA also runs on‑premises, giving developers flexibility to deploy across clouds and private infrastructure without changing their software stack.
- CUDA’s value comes from three combined factors: the richness of the ecosystem, the vast installed base, and the versatility of deployment locations (clouds and on‑prem).

## Notes

## CUDA as a Foundation for Frontier AI

Jensen Huang frames CUDA not just as a low-level interface, but as a broad, mature ecosystem that makes it the sensible first choice for building advanced AI systems. For anyone “building on any computer,” starting with CUDA is described as “incredibly smart” because of its depth, programmability, and accumulated reliability.

### Ecosystem Richness and Reliability

CUDA underpins a wide range of AI frameworks. Huang notes that NVIDIA supports “every framework,” highlighting especially:
- Triton, whose backend includes “huge amounts of NVIDIA technology,”
- vLLM,
- SGLang,
- Nemo RL and other emerging reinforcement learning and post‑training frameworks.

The sheer volume of underlying CUDA code matters for debugging and trust. When building large systems, developers face uncertainty: is a failure in their own code or in the platform? A “well wrung out” CUDA stack shifts that uncertainty toward the developer’s own code, because the underlying layers have been heavily tested at scale, even though NVIDIA still has “lots and lots of bugs” to fix. This reliability enables developers to treat CUDA as a stable foundation.

### Installed Base as a Primary Developer Concern

Huang emphasizes that for developers, the “single most important thing” is installed base. Framework authors and tool builders want their software to run on many machines and fleets, not just one environment.

CUDA’s installed base spans “several hundred million GPUs” across generations and product lines: A10, A100, H100, H200, L‑series, P‑series, and more. This diversity of GPUs in “all kinds of sizes and shapes” means that once software or a model is developed for CUDA, it can be used broadly. For example, a robotics company can run the same CUDA stack inside the robot itself.

### Ubiquity Across Clouds and On‑Prem

NVIDIA’s GPUs with CUDA are present in “every cloud,” which Huang says makes the company “genuinely unique.” AI companies often do not know upfront which cloud service provider they will partner with. Because NVIDIA hardware and CUDA are available everywhere, their software can run across clouds without a fundamental stack change.

CUDA also supports on‑premises deployments, offering a unified platform whether workloads run in public clouds or private infrastructure.

### The Combined Moat

Huang concludes that CUDA’s value arises from three intertwined elements:
1. **Rich ecosystem and programmability**,
2. **Vast and varied installed base of GPUs**,
3. **Versatile presence across all major clouds and on‑prem environments**.

Together, these make CUDA “invaluable” and central to how Frontier AI will be built on NVIDIA hardware.

