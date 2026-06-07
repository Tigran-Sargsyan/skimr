---
title: 'Where AI hits a wall #ai #tech #learning'
author: Nate B Jones
source_id: 1
source_slug: nate-b-jones
url: https://www.youtube.com/watch?v=yOGLr2IwAWk
published_at: '2026-06-07T01:00:29Z'
duration_seconds: null
primary_theme: business
secondary_theme: tech
relevance: 6
hook: AI stops where unspoken, expert-only constraints begin to matter.
tldr: The clip argues that AI-produced work often looks right but misses subtle, crucial constraints. Human domain experts spot the gap between plausibility and actual correctness, then articulate missing rules or nuances. Those expert-specified constraints transform generic AI outputs into differentiated, firm-specific solutions instead of commodities.
caveats: It looks more like product commentary than deep technical analysis, so skip it if you want architecture, evals, or concrete implementation details.
pitch: If you’re building LLM systems, this is a useful reminder that the real failure mode is not obvious hallucination but missing domain constraints, and the examples around expert-only business logic map well to the kind of edge cases you have to encode in production.
---

## Key Points

- Domain experts can see the gap between work that looks plausible and work that is actually correct.
- Experts articulate constraints that were not explicit rules before they described them.
- AI-generated outputs risk being generic because any firm can access the same underlying model.
- A strategy partner may reject AI analysis that lacks proprietary insight on customer switching costs.
- Differentiation comes from adding firm-specific insights on top of AI-generated commodity framing.
- A loan officer might reject an AI covenant tracking prototype that equates different financial covenants.
- Debt service coverage ratios and minimum net worth requirements require different monitoring triggers.
- Certain business logic is too nuanced to be fully captured in a traditional requirements document.

## Notes

## Core Idea: Where AI Hits Its Limits

The core argument is that AI often produces work that appears correct but lacks the subtle, domain-specific constraints necessary for it to actually be correct in practice. Human domain experts are uniquely able to detect and specify those missing constraints, turning vague unease into concrete rules. This expert intervention is what separates commodity AI output from differentiated, high-value work.

## The Expert’s Role: From “Looks Right” to “Is Right”

Experts can identify a precise gap between something that merely looks plausible and something that withstands real-world scrutiny. They do this by naming constraints, dependencies, or distinctions that were not written down as rules before. Once expressed, those constraints become part of the system’s logic, but they originate in the expert’s judgment rather than in the AI model or a preexisting specification.

## Example 1: Strategy and Competitive Analysis

In a strategy context, AI can generate a competitive analysis that seems structurally sound and professionally framed. However, a strategy partner may push back, asking where the firm’s proprietary insight on customer switching costs is represented. The key critique is that any competitor with the same AI access could have created an identical framing. The missing element is the firm-specific, experience-based understanding of what actually drives customer behavior and switching costs in their particular market. By insisting on that insight, the partner is effectively drawing a line between generic analysis and the firm’s differentiated intellectual capital.

## Example 2: Lending and Covenant Tracking

In a lending or credit risk context, AI might propose a covenant tracking prototype that treats different financial covenants similarly. A loan officer rejects this, noting that a debt service coverage ratio cannot be handled the same way as a minimum net worth requirement. The two types of covenants have distinct monitoring triggers and operational implications. This distinction is obvious to the practitioner but nontrivial to encode without domain input. The loan officer’s feedback is not just preference; it is a piece of business logic that governs how risk is monitored and managed.

## Limits of Requirements Documents

These kinds of nuanced constraints and distinctions often do not appear in standard requirements documents. They instead live in tacit knowledge, accumulated practice, and context-sensitive judgment. When experts challenge AI prototypes, they are surfacing that tacit logic and converting it into explicit constraints. This process shows that the “wall” for AI is not just data or compute, but the absence of these deeply embedded, unarticulated rules.

## Differentiation Beyond Commodity AI

Because many organizations can use the same models, unrefined AI outputs tend to converge on similar, generic framings. Differentiation arises when domain experts overlay proprietary insights and specific business logic onto those outputs. The result is work that reflects the firm’s unique understanding of its customers, markets, and risk profile, rather than a commodity product of shared AI capabilities.

