---
title: 'StrongDM''s three person team ships with zero human code review #ai #engineering'
author: Nate B Jones
source_id: 1
source_slug: nate-b-jones
url: https://www.youtube.com/watch?v=eY1u8Ni9ClQ
published_at: '2026-04-25T21:00:30Z'
duration_seconds: null
primary_theme: tech
secondary_theme: null
relevance: 4
hook: AI models are now writing—and optimizing—their own codebases.
tldr: Codex 5.3 was built largely by its own earlier versions, which directly wrote the code that produced the new model. This self-referential development loop improved build speed and efficiency by letting the model detect and fix its own inefficiencies. Anthropic’s Claude Code is following a similar path, with most of its code already written by Claude and human roles shifting toward specification and judgment rather than manual coding.
caveats: Skip it if you want real architectural detail, benchmarks, or failure modes, because this reads more like trend commentary and lab marketing than grounded engineering analysis.
pitch: If you want a fast read on how AI-assisted coding is being operationalized inside frontier labs, this is adjacent to your work on agent tooling and the shifting human role from coding to spec-and-judge.
---

## Key Points

- Codex 5.3 is described as the first frontier AI model that was directly created by its own predecessor’s coding work, not just metaphorically but in a literal development sense.
- Earlier Codex versions were already used to analyze training logs, flag failing tests, and suggest fixes to training scripts during model development.
- For Codex 5.3, OpenAI reports a 25% speed improvement and 93% reduction in wasted tokens during the build process, partly due to the model identifying its own inefficiencies.
- The development process represents a self-referential loop: the AI contributes to the code and infrastructure that are then used to train and run its successor.
- Claude Code is following a similar pattern, with 90% of the code in Claude Code, including the tool itself, written by Claude Code.
- Anthropic expects the proportion of AI-generated code for Claude Code to move rapidly from 90% toward 100%.
- Boris Trenne’s claim of not writing code for months reflects a role change from hands-on coding to focusing on specification, direction, and judgment of AI-generated outputs.
- Anthropic is estimating that their entire company is transitioning to entirely AI-generated code around the present time.

## Notes

## Self-Referential AI Development

The video describes a “self-referential loop” emerging in how leading AI models are built at OpenAI and Anthropic. This loop means that frontier models are directly involved in writing the code and infrastructure used to create their successors.

### Codex 5.3 Building Itself

Codex 5.3 is presented as the first frontier AI model that is a direct product of its predecessor’s coding labor. Earlier Codex versions already participated in the development pipeline: they analyzed training logs, flagged failing tests, and suggested fixes to training scripts. With Codex 5.3, this involvement deepened to the point where the model’s predecessor effectively wrote the code that enabled Codex 5.3 to be built and shipped.

OpenAI reports concrete efficiency gains from this approach: a 25% improvement in speed and 93% fewer wasted tokens in the build process. These gains are attributed in part to the model’s ability to identify its own inefficiencies and help correct them during development.

### Claude Code’s Similar Trajectory

Anthropic’s Claude Code is said to be on a similar path. According to the video, 90% of the code in Claude Code—including the tool itself—was built by Claude Code. That percentage is described as rapidly converging toward 100%, implying an imminent state where essentially all code is AI-generated.

### Changing Human Roles in Engineering

Boris Trenne’s statement about not writing code for months is interpreted as evidence of a role shift rather than literal non-participation. His work has moved from manual coding to setting specifications, providing direction, and exercising judgment over AI-generated code.

Anthropic is estimated to be at the point where the entire company is moving to entirely AI-generated code. In this framing, human engineers focus on defining what should be built and evaluating the results, while models handle most of the actual code production.

