---
title: Shopify CEO Reveals Their Secret AI Developer
author: Nate B Jones
source_id: 1
source_slug: nate-b-jones
url: https://www.youtube.com/watch?v=NRBQmwlILjk
published_at: '2026-05-26T14:00:15Z'
duration_seconds: null
primary_theme: tech
secondary_theme: thinking
relevance: 7
hook: Shopify turns private AI tinkering into public apprenticeship with one simple design constraint.
tldr: Shopify’s AI agent River is powerful not just because of volume, but because it only runs in public Slack channels. Public AI work closes an emerging “apprenticeship gap” where senior judgment and agent use stay hidden in private chats. Companies that design safe public spaces, senior-led examples, and reuse-focused metrics will compound organizational learning instead of paying repeatedly for the same AI lessons.
caveats: It’s more about organizational learning and AI workflow design than technical architecture, evals, or failure modes, so skip it if you want deeper systems substance.
pitch: You’ll get a useful real-world example of how an AI agent gets embedded into a production engineering workflow, and the “public Slack only” constraint is the kind of operational detail that matters if you care about how teams actually learn to use agents at scale.
---

## Key Points

- River, Shopify’s internal coding agent, accounts for about one in eight merged pull requests.
- All River interactions must occur in public Slack channels, never in private DMs.
- Most companies’ AI use is fragmented and private, so individuals improve while the organization does not.
- The speaker calls this growing disconnect between private AI thinking and shared learning the apprenticeship gap.
- What teams must expose publicly is the task, context, interaction, and human review around AI work.
- Prompt libraries alone fail because they miss messy context, revisions, and moments of human rejection and correction.
- Senior operators’ AI workflows are the most valuable to show publicly, yet are usually the least visible.
- A key enabling constraint is forbidding private agent use, forcing collaborative learning in declared public channels.

## Notes

## River at Shopify and why it matters
- Shopify’s internal coding agent is named River.
- In one 30-day period, 5,938 employees used River across more than 4,400 Slack channels.
- In a single week, River opened 1,800 pull requests in Shopify’s main monorepo.
- About one in every eight merged pull requests at Shopify now comes from River.
- The crucial design choice: River cannot be used in private; all interactions occur in public Slack channels.
- Every engineer’s conversation with River is scrollable by others, exposing how tasks are framed, context is loaded, failures occur, and results are evaluated.

## The hidden AI problem: private gains, no organizational learning
- Across companies, employees already use AI heavily: for emails, reasoning through issues, coding assistance, summarizing long documents, and small custom workflows.
- Almost all of this AI use happens in private tools and browser tabs.
- Effective prompts, clever corrections, and working workflows stay trapped in single users’ histories.
- Colleagues recreate similar workflows repeatedly because no one sees or shares what already works.
- Within large firms, multiple redundant internal tools emerge for the same problem due to this fragmentation.
- Result: individuals get smarter and faster, but the company as a whole does not, creating a gap between individual and organizational intelligence.

## The apprenticeship gap in the age of private AI
- Historically, skilled work was learned by proximity to experts: watching how they frame problems and make tradeoffs.
- Much of the important craft knowledge never appeared in manuals; it lived in process and judgment.
- When most serious thinking now happens in private AI windows, juniors lose this proximity.
- They cannot see how seniors instruct models, verify outputs, and refine workflows.
- Each person is “alone with their model,” rediscovering the same lessons over and over.
- The speaker names this widening disconnect the “apprenticeship gap.”

## Lessons from hard-to-digitize physical expertise
- Manufacturing illustrates how difficult it is to capture tacit knowledge in systems.
- Companies like John Deere face aging experts with deep, fingertip-level skill in complex tooling.
- Product managers attempting to turn such expertise into machine learning algorithms find it extremely difficult.
- Polanyi’s paradox applies: “we know more than we can tell”; lived skill exceeds explicit description.
- Supply chains can hinge on single individuals with unique physical skills, like painting Rolls-Royce racing stripes or testing specific Boeing screws.
- Software has similar tacit craftsmanship in how experienced engineers think and work, even if it appears more digital.

## What “public AI work” should actually expose
- Simply dumping all AI chat transcripts into Slack would create noise, not learning.
- The speaker highlights four critical elements to make visible:
  1. **Task** – What the person was trying to accomplish.
  2. **Context** – What they told the model, what they pasted in, and what they omitted.
  3. **Interaction** – How they prompted, what the first answer looked like, how they pushed back and iterated.
  4. **Review** – What they accepted, rejected, manually verified, rewrote, and why.
- Sharing only final answers teaches almost nothing; sharing all four elements builds shared taste about quality and correctness.
- Shared taste is identified as a major bottleneck in effective AI adoption.

## Why prompt libraries aren’t enough
- Prompt libraries capture static instructions but omit the messy, iterative reality of effective AI use.
- They miss the revisions, disagreements, and nuanced constraints applied during real work.
- Crucial teaching moments occur when the model’s plausible output is rejected for being wrong for a customer, off-tone, or missing critical constraints.
- The speaker notes they often quickly say “no” to model outputs, surprising onlookers used to passive consumption.
- The most valuable aspect of AI work is the surrounding habit, not the raw prompt.
- Prompts are easy to copy; habits of review, rejection, and refinement are what enable learning.

## Designing declared spaces and boundaries instead of default surveillance
- Privacy is a legitimate concern; employees should not feel that all AI chats suddenly become company property.
- Many employment agreements technically grant companies rights over input to corporate AI, but behavior rarely aligns with this.
- Making every AI chat default-public would likely push good work underground as people stop using AI.
- The proposed alternative is **declared public spaces with clear rules**.
- Shopify’s example shows senior people running real work with River in designated public channels.
- Teams can have specialized AI workbench channels: product workbenches, sales research channels, finance analysis channels, and engineering agent channels for nonsensitive tasks.
- Clarity about what belongs and what is forbidden (customer data, HR issues, legal strategy) is essential.

## Regulated environments and safe public surfaces
- Highly regulated contexts, like healthcare and banking, cannot simply expose raw operational data.
- Yet, if regulations like HIPAA are interpreted too rigidly, they can inadvertently block AI learning rather than just protect privacy.
- The goal is to creatively design workflows that strip PII and sensitive details while preserving reasoning patterns.
- For example, clinical decision support, anonymized patient summaries, or treatment reasoning might be shared in compliant forms.
- The lesson is not to make regulated work public unsafely, but to create safe public surfaces that still teach others how AI is used.

## The central role of senior operators’ public AI workflows
- The most valuable AI work to expose is that of senior people, because they have the strongest judgment.
- In most organizations, senior thinking is highly opaque; others see memos and decisions, not the process.
- AI can make this worse, letting leaders quietly use agents to stress-test plans, rewrite communications, or explore risks without visibility.
- The fix is to ask senior people to run some real but nonsensitive work in public, with proper tooling support.
- Examples include:
  - A leader asking an agent to critique a launch plan in a team channel.
  - A senior engineer debugging a low-risk bug with an agent while narrating their review.
  - A sales leader transforming stripped-down account notes into a call brief.
  - A product leader using AI to probe weak assumptions in a roadmap narrative.
- Juniors then observe how ambiguity is framed, how much context is enough, and how often first answers are wrong.
- They learn that effective AI use is active supervision, not passive acceptance.

## How Toby at Shopify models public AI use
- Shopify’s CEO, Tobi Lütke, both leads the company and considers himself an individual contributor.
- He uses River in public channels, letting others see and interact with his agent.
- Colleagues can question the agent, critique his choices, and co-work within the same channel.
- The process is somewhat chaotic but still directed by him.
- This “open room” model allows him to teach and socialize how he wants AI used across the company.

## Getting started: channels, defaults, and turning patterns into playbooks
- The speaker recommends starting with one declared AI channel per team.
- A pinned message should clearly define the channel’s purpose, such as reusable workflows, useful failures, and prompt revisions.
- Make public channels the default place for agent interactions, not an exception.
- Shopify enforces that River cannot be used in DMs at all, structurally favoring public work.
- As patterns repeat, they should be converted into playbooks, agent skills, or structured inputs for future challenges.
- AI can be used to mine these channels for lessons learned and reusable workflows.
- This approach lets organizations convert individual discoveries into team-level capabilities.

## Measuring learning and reuse, not just AI usage
- Traditional metrics like token volume and task count have some value but miss learning dynamics.
- More meaningful metrics include:
  - Number of reusable workflows created from public channels.
  - How many of those workflows are adopted by others or other teams.
  - How many examples are pinned because they significantly changed someone’s work.
  - How often public workflows prevent duplicated effort.
  - How many outdated examples are retired.
  - How many failures are converted into improved review rules.
- Sometimes the best signal is not “AI usage is up,” but “certain mistakes are happening less often.”
- Reduced error rates may be the clearest indicator of organizational learning.

## The strategic choice: private acceleration vs. shared compounding
- The key leadership question is not whether employees use AI; most already do.
- It is which AI work is making one person better while others do not benefit.
- If valuable experiments and workflows stay private, companies pay repeatedly for the same lessons.
- This is the critical apprenticeship moment: either senior people work in visible ways, or each individual accelerates alone.
- Organizations that prioritize learning from one another begin to compound their capabilities over time.

## The power of constraints in shaping collaboration
- The strongest takeaway is the role of thoughtful constraints in enabling collaboration.
- Shopify’s ban on using River in DMs is a simple but powerful rule.
- DMs are popular but are demonstrably bad for teamwork and shared learning.
- By insisting agents only run in public channels, Shopify imposes a binding constraint that favors collective learning over individual convenience.
- Leaders should audit their environments to identify where intentional constraints could promote public, collaborative AI learning.
- Constraints that are “creative and careful” can be frustrating individually but beneficial organizationally, driving compounding learning from AI use.

