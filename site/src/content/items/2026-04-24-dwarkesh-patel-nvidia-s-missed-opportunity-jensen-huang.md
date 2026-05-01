---
title: NVIDIA's Missed Opportunity – Jensen Huang
author: Dwarkesh Patel
source_id: 2
source_slug: dwarkesh-patel
url: https://www.youtube.com/watch?v=eyBePxoY0FY
published_at: '2026-04-24T14:27:12Z'
duration_seconds: null
primary_theme: business
secondary_theme: tech
relevance: 8
hook: Jensen Huang explains how Nvidia missed deeply funding Anthropic and what it learned.
tldr: Jensen Huang argues that Anthropic’s reliance on non‑Nvidia accelerators is a one-off case driven by early financing deals, not a broad shift away from Nvidia. He says Nvidia once lacked both the capital and the appreciation of how much up‑front supplier investment AI labs like Anthropic and OpenAI require, which led hyperscalers to fund them in exchange for using their own chips. Huang calls this Nvidia’s major “miss,” insists alternatives still must outperform Nvidia to matter, and says he will not repeat the mistake, now eagerly investing in leading AI labs to help them scale on Nvidia hardware.
caveats: Skip it if you’re looking for hands-on engineering detail, because this is mostly strategic and economic framing rather than a deep technical teardown of chips or systems.
pitch: If you care about how AI infrastructure really gets funded and why accelerator ecosystems win or lose, this gives you Jensen Huang’s own read on Nvidia’s biggest strategic miss and the economics behind Anthropic, TPUs, and custom silicon.
---

## Key Points

- Anthropic’s large TPU and Broadcom deals are described as a unique, company-specific case rather than evidence of a broad industry movement away from Nvidia GPUs.
- Huang claims TPU growth and related training growth are effectively 100% attributable to Anthropic, implying limited overall TPU traction without that single customer.
- OpenAI and other top labs are still characterized as being “vastly Nvidia,” even if they experiment with AMD or build in‑house accelerators like Titan.
- Huang is not bothered by customers trying other accelerators, arguing experimentation ultimately reinforces Nvidia’s relative strength if rivals underperform.
- He emphasizes that simply deciding to build an AI accelerator ASIC is insufficient; the resulting product must be better than Nvidia’s, which he argues is very difficult given Nvidia’s scale and yearly performance leaps.
- Huang dismisses the idea that custom ASICs can be much cheaper by accepting worse performance, noting ASIC vendors themselves retain high margins (around mid‑60%), so savings versus Nvidia’s ~70% margins are limited.
- Historically, Nvidia lacked the financial ability to make multi‑billion‑dollar upfront investments into foundation model labs like Anthropic in exchange for committed GPU usage.
- Huang says he did not fully internalize that labs such as Anthropic and OpenAI needed massive supplier capital because traditional VCs would not fund $5–10 billion bets on speculative AI research labs alone. This is the “miss” he identifies in hindsight as too modest in scale and commitment at the time, not recognizing they “had no other options.” It let hyperscalers like Google and AWS step in with huge investments tied to their own compute, pushing Anthropic’s workloads onto TPUs and other non‑Nvidia accelerators and allowing those alternatives to gain share entirely due to that financing structure.### Anthropic as exception, not trendHuang frames Anthropic’s heavy use of TPUs as an anomaly driven by its financing history. He argues that without Anthropic there would be virtually no growth in TPU usage or TPU‑based training, suggesting that most other major AI workloads remain on Nvidia. In contrast, he depicts OpenAI—despite AMD partnerships and its Titan project—as still predominantly running on Nvidia hardware and continuing deep collaboration.### Economics and difficulty of competing ASICsHuang challenges the logic that custom accelerators only need to be “within 70%” of Nvidia’s performance because Nvidia has high margins. He claims ASIC providers like Broadcom also keep very high margins (around 65%), so users do not save dramatically on unit cost. Given Nvidia’s scale and annual “big leaps,” he asserts designing an ASIC that is actually better than Nvidia is “not sensible” and very hard; many announced ASIC projects have been canceled.### Nvidia’s missed strategic opportunity and new stanceLooking back, Huang says Nvidia could not and did not write the multibillion‑dollar checks hyperscalers did to fund Anthropic early in exchange for locked‑in compute usage. He now sees that as a major strategic miss tied to underestimating both the capital intensity and funding constraints of foundation AI labs. He believes Nvidia might have grown much faster had it funded Anthropic earlier. Going forward, he vows not to repeat this mistake, saying he is now “delighted” to invest in OpenAI and, when possible, Anthropic, viewing direct capital support as essential to helping leading labs scale on Nvidia infrastructure.

## Notes

## Anthropic and TPU use as an exception

- Anthropic’s recent multi‑gigawatt deal with Broadcom and Google for TPUs is presented as a special case, not a general industry realignment.
- Huang asserts that TPU growth is essentially “100% Anthropic,” and similarly that training growth on TPUs is also entirely driven by Anthropic.
- Without Anthropic, he claims there would be no real TPU or TPU‑training growth, implying that most serious AI training still resides on Nvidia hardware.

## Other labs: still predominantly Nvidia

- While recognizing that OpenAI has deals with AMD and is developing its own Titan accelerator, Huang states they are still “vastly Nvidia.”
- He expects Nvidia and OpenAI to continue doing “a lot of work together,” suggesting Nvidia remains the primary compute provider even as OpenAI experiments with alternatives.
- Huang is not offended by customers trying other accelerators; he sees experiments as a way for them to benchmark and ultimately appreciate Nvidia’s performance.

## Economics and difficulty of custom ASICs

- Huang argues that building an AI ASIC is not enough; the resulting chip must be better than Nvidia’s GPUs to be viable, which he portrays as extremely hard.
- He highlights Nvidia’s scale and “velocity,” emphasizing that Nvidia delivers large performance improvements every year.
- The notion that a custom ASIC merely needs to be within 70% of Nvidia’s performance due to Nvidia’s high margins is rejected.
- He notes Nvidia’s margins are around 70%, but ASIC vendors (e.g., Broadcom) also enjoy very high gross margins, around 65%, so end users do not gain as much cost advantage as presumed.

## Nvidia’s missed opportunity with Anthropic

- Huang says that, historically, Nvidia did not have the ability to make multi‑billion‑dollar investments into labs like Anthropic.
- He now realizes he failed to deeply internalize how hard it is to build a foundation AI lab such as Anthropic or OpenAI.
- These labs required huge upfront capital from their compute suppliers because traditional venture capitalists would not risk $5–10 billion on speculative AI labs.
- As a result, Google and AWS stepped in with major early investments, with the understanding that Anthropic would use their compute (e.g., TPUs).
- Huang identifies this as his “miss”: not recognizing that labs “had no other options” and thus underestimating the strategic necessity of Nvidia acting as a capital provider.

## Changed strategy going forward

- Huang says that even if he had perfectly understood the situation back then, Nvidia might not have been financially capable of writing checks at the required scale.
- He believes that, had Nvidia been able to invest similarly, the company could have been as large then as it is now.
- He asserts he will not repeat this mistake: he is now “delighted” to invest in OpenAI and to help them scale.
- When Anthropic later approached Nvidia, he was also pleased to become an investor and support their scaling, once Nvidia was in a position to do so.
- He now views such strategic investments in leading AI labs as essential to Nvidia’s future role in AI and science.

