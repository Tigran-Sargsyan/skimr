---
title: NVIDIA's Real Moat – Jensen Huang
author: Dwarkesh Patel
source_id: 2
source_slug: dwarkesh-patel
url: https://www.youtube.com/watch?v=mW1KWTjaggk
published_at: '2026-04-26T13:45:20Z'
duration_seconds: null
primary_theme: tech
secondary_theme: business
relevance: 8
hook: CUDA’s power comes from ecosystem depth, massive install base, and cloud ubiquity.
tldr: Jensen Huang argues that CUDA’s real strength is its rich, stable, and deeply integrated software ecosystem. Developers benefit from extensive framework support, trusted underlying code, and the ability to build custom kernels confidently. CUDA’s massive install base across GPUs, robots, and every major cloud provider makes CUDA-built software and models broadly portable and commercially valuable.
caveats: Skip it if you want hands-on architecture or failure-mode detail, because this is more about NVIDIA’s strategic ecosystem advantage than about implementation-level technical scars.
pitch: You care about the real engineering substrate behind AI systems, and this is worth your time because it digs into why CUDA wins not as hype but as a deeply integrated software-and-distribution moat that shapes what you can actually ship on modern AI infrastructure.
---

## Key Points

- CUDA is a rich, mature ecosystem that supports almost every major AI and ML framework.
- NVIDIA contributes heavily to frameworks like Triton, embedding large amounts of NVIDIA technology in their backends.
- Developers can assume most bugs are in their own code, not CUDA’s deeply tested software stack.
- A massive global install base of hundreds of millions of NVIDIA GPUs makes CUDA software widely deployable.
- CUDA compatibility stretches across many GPU generations and product lines, maximizing reuse of software and models.
- CUDA runs on devices from data center servers to robots, extending AI applications to the physical world.
- NVIDIA GPUs with CUDA are available on every major cloud provider and on-premises deployments.
- This combination of ecosystem richness, install base, and deployment versatility makes CUDA strategically invaluable for AI developers.

## Notes

## CUDA as a Deep, Stable Ecosystem

Jensen Huang emphasizes that CUDA is not just an API but a rich, mature ecosystem. For anyone building on computers for AI or high-performance workloads, starting with CUDA is described as “incredibly smart” because of its breadth and stability. CUDA supports essentially every major AI framework, providing a common foundation across diverse tools.

This ecosystem includes support for users who want high-level abstractions as well as those writing custom kernels. Developers can work directly at lower levels when needed, while still leveraging the vast infrastructure that CUDA provides underneath.

Because so much code and engineering effort has gone into CUDA over time, the stack is heavily “wrung out.” When something goes wrong in a complex AI system, developers can usually assume the bug is more likely in their own code rather than in the underlying CUDA platform, which makes debugging and iteration more manageable.

## Integration with AI Frameworks

Huang notes that NVIDIA contributes substantially to important frameworks like Triton. The back end of Triton contains “huge amounts of NVIDIA technology,” making it tightly coupled with CUDA and NVIDIA GPUs.

Beyond Triton, CUDA supports many emerging and established AI systems: vLLM, SGLang, and numerous others. He highlights a wave of new reinforcement learning and post-training frameworks, mentioning examples like vLLM again in that context and Nemo RL.

The key point is that as the framework landscape proliferates—spanning inference, training, RL, and post-training—CUDA serves as the common, well-supported base. Framework authors can assume their users will have access to CUDA-enabled hardware and software, reducing fragmentation.

## Reliability and Developer Trust

Building large-scale AI systems involves interacting with “a mountain of code” beneath the application layer. For developers, it is crucial to know whether a failure stems from their own logic or from underlying infrastructure.

With CUDA’s maturity and testing, Huang argues developers can usually trust the “computer” side of the stack. While NVIDIA still has “lots and lots of bugs” in absolute terms, the system is stable enough that most issues arise from the developer’s own code. This trust speeds up development because engineers can focus on their algorithms instead of questioning the platform’s correctness.

## Install Base as Strategic Value

Huang identifies install base as the single most important factor for a software developer. Developers want their software to run on many machines, not just on one-off or niche hardware.

NVIDIA’s CUDA ecosystem runs on several hundred million GPUs worldwide, according to Huang. Every major cloud has NVIDIA GPUs exposed with CUDA. CUDA compatibility spans multiple GPU generations and product lines, including A10, A100, H100, H200, the L series, and the P series.

Because of this, once a model or framework is developed on CUDA, it can be used broadly without rewriting for each environment. This greatly increases the commercial and practical value of the software.

## From Data Centers to Robots

The CUDA stack is not limited to data center GPUs. Huang notes that if you are a robotics company, you want the same CUDA stack running inside the robot itself.

This means the same programming model and software artifacts can often be applied across cloud training, edge inference, and onboard robotics computing. The portability of CUDA across “all kinds of sizes and shapes” of GPUs allows AI developers to target a wide range of devices with one main codebase.

## Ubiquity Across Cloud Providers and On-Prem

Huang stresses that NVIDIA GPUs with CUDA are present in every major cloud service provider. For an AI company or AI developer, this matters because they may not know in advance which cloud they will partner with or run on.

CUDA’s presence across all clouds, and support for on-premises deployments, gives developers flexibility in choosing where to deploy. They are not forced to re-platform models or frameworks when switching providers.

## Why CUDA Is “Invaluable”

Huang sums up CUDA’s strategic advantage as a combination of three elements:

1. The richness and programmability of the ecosystem, including frameworks, tools, and custom-kernel capabilities.
2. The expansiveness of the install base across hundreds of millions of GPUs and many product generations.
3. The versatility of deployment, spanning every major cloud provider and on-premises, as well as form factors like robots.

Together, these make CUDA “invaluable” for developers building Frontier AI and other advanced systems, because their work gains maximal reach, reliability, and flexibility from a single foundational platform.

