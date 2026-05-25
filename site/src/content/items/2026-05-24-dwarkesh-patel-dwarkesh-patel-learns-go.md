---
title: Dwarkesh Patel Learns Go
author: Dwarkesh Patel
source_id: 2
source_slug: dwarkesh-patel
url: https://www.youtube.com/watch?v=xoLxmsiJl9c
published_at: '2026-05-24T19:09:02Z'
duration_seconds: null
primary_theme: science
secondary_theme: thinking
relevance: 4
hook: Go’s rules reveal deep tradeoffs between human intuition and algorithmic clarity.
tldr: The video explains Go’s basic rules for placing stones, capturing, and surrounding territory. It contrasts human-oriented rule sets with the unambiguous Tromp–Taylor rules used for Go AIs. It also shows how scoring and game-ending conditions differ between human judgment and algorithmic resolution.
caveats: 'Skip it if you want depth: most of it is just basic Go rules and not much beyond what a competent beginner guide covers.'
pitch: If you like the boundary between human intuition and machine-formalized rules, this is a clean illustration of why games like Go expose the gap between tacit judgment and algorithmic clarity—a theme that overlaps with your interest in expertise and AI systems.
---

## Key Points

- A stone is captured when all four orthogonal neighboring intersections are occupied by the opponent’s stones.
- In typical human Go rules, playing a stone with no remaining liberties is illegal because it is suicidal.
- Under Tromp–Taylor rules, suicidal moves are allowed but immediately resolved as dead stones with equivalent outcomes.
- Local threats in Go can force immediate responses, similar to checks in chess that must be answered.
- Go strategy often involves sacrificing local stones to gain larger territorial advantages elsewhere on the board.
- Territory control can be ambiguous for humans when a surrounded group might still connect to the outside and live.
- Humans end a game by mutually agreeing it is finished and then agreeing which groups are alive and whose territory it is.
- Tromp–Taylor scoring counts each player’s stones and empty intersections not adjacent to any opponent stones, making results algorithmically unambiguous.

## Notes

## Basic Objective and Play

- The goal of Go is to place black and white stones on a grid to occupy as much territory as possible.
- Black moves first, then players alternate turns placing one stone at a time on intersections.
- The example game in the clip is played informally, with moves often chosen at random just to illustrate rules.

## Capturing Stones and Liberties

- Each stone’s “life” is determined by its four orthogonal neighbors (up, down, left, right), not diagonals.
- A stone has “liberties” equal to the number of empty orthogonal neighboring intersections.
- When all those neighboring intersections are occupied by the opponent’s stones, the surrounded stone has no liberties and is considered dead.
- Once a stone is captured, the capturing player controls those stones and the now-empty intersections they vacate.

## Tactical Pressure and Forcing Moves

- Placing a stone that removes an opponent group’s liberties can create an immediate threat that must be answered.
- The teacher compares such a move to a check in chess: if the opponent does not respond correctly on the very next move, their stones can be captured.
- In the example, an exposed white stone with only one remaining liberty forces white to respond at the specific liberty point or lose that stone.
- A sequence is shown where black can foresee a chain of moves leading to the capture of multiple white stones if white defends locally in the obvious way.

## Local Sacrifice vs Global Advantage

- The student recognizes that a small cluster of white stones is effectively doomed and “gone.”
- The teacher emphasizes that in Go it is acceptable—and often correct—to allow some stones to be captured.
- What matters is whether sacrificing a local group enables a larger-scale positional or territorial gain elsewhere.
- As the board size grows, the interplay between local battles and overall board strategy becomes more complex and interesting.

## Territory and Life-and-Death Ambiguity

- A configuration is shown where black appears to have completely surrounded a region containing white stones.
- From a human perspective, most players would judge that black effectively controls this territory and white has no realistic chance of living inside it.
- However, if white can, in principle, break out and connect to stones outside the enclosure, the status could flip.
- This possibility makes evaluating territory and life-and-death situations nontrivial for computers and, at times, ambiguous for humans.

## Different Rule Sets: Human vs AI

### Suicide and Tromp–Taylor

- In many traditional human rule sets (e.g., Japanese or Chinese rules), a move that results in your own stone or group having no liberties is illegal, because it is immediate suicide.
- Under Tromp–Taylor rules, placing such a stone is allowed; the stone is then immediately resolved as dead.
- Although the intermediate legality differs, the final outcome is effectively the same in many positions.
- Tromp–Taylor exists to make the rules fully unambiguous and is what Go AIs typically train against and resolve with.

### How Humans Close and Score a Game

- Human players usually end a game when one player says they think the game is done and the other agrees.
- Then they verbally or tacitly declare which groups are alive and which territories belong to whom.
- If both players’ internal “value functions” (their judgments) agree on the status of stones and territories, that becomes the consensus result.
- If there is disagreement about life, death, or territory, they keep playing until the dispute is resolved on the board.

### Tromp–Taylor Scoring Procedure

- Tromp–Taylor scoring is designed to be perfectly algorithmic and unambiguous.
- After the game ends under Tromp–Taylor, scoring proceeds in two steps:
  1. Count how many stones each player has on the board; this part is straightforward.
  2. Count the number of empty intersections that are not adjacent to any opponent stones.
- Empty intersections connected to both black and white stones are neutral and do not count for either player.
- An example shows that if an area of three empty intersections is entirely surrounded by white and not adjacent to black, white gets three points.
- In a more complex example, Tromp–Taylor may count certain points for white that a human would intuitively think white is actually losing, illustrating a divergence between AI scoring and human evaluation.

## Game Termination

- The game can end in two main ways:
  - One player resigns, conceding the game.
  - Both players pass consecutively, signaling that they believe there are no more profitable moves.
- After termination, scoring is applied according to the chosen rule set, with humans relying on mutual agreement and AIs relying on formal rules like Tromp–Taylor.

## Context Within the Clip

- The clip is part of a larger episode in which Dwarkesh Patel is learning Go and discussing AI.
- It concludes with a transition toward correcting an AI implementation bug related to these rule subtleties and then a prompt to watch the full episode.

