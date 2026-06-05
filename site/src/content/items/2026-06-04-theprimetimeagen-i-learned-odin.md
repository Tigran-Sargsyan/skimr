---
title: I learned Odin
author: ThePrimeTimeagen
source_id: 5
source_slug: theprimetimeagen
url: https://www.youtube.com/watch?v=HwmqZTnb7Co
published_at: '2026-06-04T12:00:40Z'
duration_seconds: null
primary_theme: tech
secondary_theme: null
relevance: 5
hook: Rewriting an old tower-defense game in Odin rekindles his joy of programming.
tldr: He decided to rewrite an old Lua/LÖVE tower-defense game in Odin to learn the language and enjoy low-level game programming again. Odin’s C-like design, vendor integrations, function overloading, and `using` feature impressed him, especially alongside Raylib’s straightforward rendering model. Feeling burned out from chasing AI workflows, he wants this project and channel to focus on coding for its own sake, possibly even co-developing a Jai version later.
caveats: Skip it if you want deep technical analysis, benchmarks, or a production-grade postmortem, because this is mostly a personal learning/devlog piece with some performative energy.
pitch: If you want a quick, grounded look at Odin from someone actually rewriting a game in it, this gives you a real developer’s impressions of the language, Raylib, and why low-level coding can feel fun again.
---

## Key Points

- He previously built a Lua and Love2D tower-defense game prototype, including its UI system, during a week-long tower retreat.
- He grew dissatisfied with the original codebase as it reached tens of thousands of lines of Lua.
- He chose to rewrite the game in Odin as a way to learn the language and re-engage with game programming.
- Odin’s vendor import system makes using libraries like SDL3, Raylib, Box2D, Lua, and curl straightforward and dependency-light.
- He finds Raylib significantly nicer to use than Love2D, especially its texture and rectangle-based rendering model.
- Odin’s explicit function overloading and `using` feature feel elegant, convenient, and surprisingly enjoyable to him.
- He reports that AI tools work fine with Odin for tasks like generating JSON-loading code, though the output still needs refactoring.
- After feeling his passion drained by trying to optimize AI-assisted workflows, he wants to focus this channel on coding projects done for joy, possibly including a Jai version of the game.

## Notes

## Background: The Original Tower-Defense Game

- About a year earlier, he and friends spent seven days in a tower creating a video game in Lua using Love2D.
- The group included pixel artist Adam C. Eunice and others contributing systems like UI and animation.
- He built the UI system, aiming for flexible menus that could expand and collapse instead of being hard-coded.
- Another teammate, Teage, built a robust animation system that he praises but hadn’t previously highlighted.
- The project progressed to feeling like a real game, but eventually it stalled and was left untouched.
- A major pain point was scale: the codebase approached 70–80k lines of Lua, which he found unwieldy and error-prone.

## Decision to Rewrite in Odin

- He considered the classic “rewrite the project” idea, fully aware it risks never finishing.
- Instead of Lua, he chose Odin, which he sees as better suited to game development.
- He respects Ginger Bill (Odin’s creator) and finds Odin a compelling language worth learning.
- His immediate goal is not just to ship a game quickly but to use this rewrite as a vehicle to learn Odin deeply.
- He has already reached a point where level two renders correctly with Perlin-noise backgrounds, pathing, and JSON-loaded data.

## First Impressions of Odin

- Odin is described as “a lot like C” and is marketed as “the C alternative for the joy of programming.”
- Odin includes features specifically designed to support game programming, though he hasn’t yet used many of them.
- After around 20–30 hours of use, he found Odin extremely easy to pick up, assuming familiarity with manual memory management concepts.

## Vendor Imports and Ecosystem

- One of his favorite aspects is Odin’s `vendor` import style, which simplifies pulling in external libraries.
- Using SDL3, Raylib, Lua, curl, and others is straightforward; they’re effectively “right there” for use.
- This setup makes it easy to build a 2D game with minimal external complexity, especially with Box2D and Raylib available.
- His project effectively has no complicated dependency setup: JSON handling from the core, Raylib for rendering and controls, and that’s it.

## Raylib vs Love2D

- He strongly prefers Raylib over Love2D for this project.
- He praises Raylib’s interface design, calling it “so much better to use than Love.”
- A key feature he appreciates: you can draw to a texture and then draw that texture using a source rectangle.
- By flipping or resizing the source rectangle, the drawn result flips or scales accordingly.
- This source–destination rectangle model makes rendering behavior easy for him to reason about.

## Odin Language Features He Likes

### Explicit Function Overloading

- Odin supports a form of function overloading that he finds particularly well-designed.
- Instead of simply declaring multiple functions with the same name, you explicitly define which functions participate in an overload group.
- For example, a `cell_index` operation can be overloaded for either coordinate-based arguments or row-and-column arguments.
- The compiler automatically picks the correct overload based on the argument types.
- He appreciates that the overload set is explicit and limited, which counters the usual criticisms of overloaded functions.
- He did not expect to like this feature as much as he does, but calls it “a perfect version” and “really a good design.”

### `using` for Field Promotion and Conversions

- Odin’s `using` keyword is another feature he finds “pretty dang cool” and convenient.
- In his game, a coordinate is defined as a row and column, representing a grid square in the tower-defense layout.
- He can write `using coords` so that the row and column fields become directly accessible within a containing type.
- A `cell` type can contain a coordinate via `using`, meaning its fields behave as if they are directly on `cell`.
- As a result, when a function expects a coordinate, he can pass a `cell` instance and have it converted automatically to the required coordinate representation.
- This works seamlessly with his overloaded functions like `cell_index`, which accept either coordinate or row-and-column parameters.

### Features Not Yet Explored

- He notes there are features he hasn’t yet touched, such as swizzling and structures-of-arrays vs arrays-of-structures.
- He expects these will become relevant once he reaches more advanced game logic, like moving enemies.
- For now, his experience is limited to language basics and some data modeling, but he already “really, really” likes what he sees.

## Using AI with Odin

- He addresses the question of whether AI coding tools work well with Odin.
- In his experience, AI tools handle Odin without confusion, similar to mainstream languages.
- The AI still produces low-quality or incorrect code frequently, which he attributes partly to prompting but acknowledges as a general issue.
- He used AI to scaffold a feature that reads JSON level data files and transforms them into in-game structures.
- That initial AI-generated solution came quickly and felt “seamless,” though he then refactored it heavily.

## Channel Direction and Devlog Intent

- This video appears on a smaller channel (ThePrimegen) rather than his larger Vimage channel.
- The new channel has far fewer subscribers, and he’s uncertain about growth or audience activity.
- He invites viewers who enjoy this style of content to like and subscribe, as he’d love to maintain a devlog series.
- His personal goal is to release updates roughly weekly or bi-weekly, circumstances permitting.

## Possible Parallel Implementation in Jai

- He is considering implementing the game in Jai (Jonathan Blow’s language) alongside Odin.
- He jokes about the multiple names people use for Jai and notes some confusion about its official name.
- He describes Jai as significantly more expressive than Odin and “the best language ever written for macros.”
- A dual implementation would allow him to compare strengths, seeing which language excels in which aspects.
- He emphasizes he is in no rush to finish the game; the priority is exploration and learning.

## Reclaiming the Joy of Programming

- He candidly describes a period when his passion for programming declined.
- This was driven by an intense focus on AI-assisted workflows and the surrounding “AI programming world.”
- He saw promises of massive productivity gains but found that caring about code quality forced him to slow down.
- While AI can speed up work when he doesn’t care much about the outcome, it feels less effective when he does care deeply.
- This mismatch made him feel like he was “holding it wrong,” leading to frustration and burnout over six to twelve months.
- He compares his role in AI-assisted coding to being a co-pilot rather than the pilot, not understanding what happens internally.
- That lack of direct creation clashed with his reasons for entering programming, which were not about extreme pay but about love of the craft.

## Returning to Roots and Future Arc

- He wants this channel and project to mark a return to “coding for the joy of coding.”
- He feels programming’s landscape has shifted since he started, from a modestly paid craft to a more lucrative, hype-driven field.
- Despite audience interest in topics like AI, security, or tech news, he emphasizes that his first love is programming itself.
- This tower-defense rewrite in Odin, and perhaps Jai, represents a new arc focused on game programming and hands-on creation.
- He closes by acknowledging and appreciating those who have stuck around and hinting at a possible transformation into more of a “game programmer” persona.

