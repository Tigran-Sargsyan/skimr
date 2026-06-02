---
title: The Hidden Problem With MCTS – Eric Jang
author: Dwarkesh Patel
source_id: 2
source_slug: dwarkesh-patel
url: https://www.youtube.com/watch?v=A3H_hKKa9Tk
published_at: '2026-06-01T19:13:34Z'
duration_seconds: null
primary_theme: tech
secondary_theme: science
relevance: 8
hook: Monte Carlo Tree Search can quietly degrade your policy instead of improving it.
tldr: MCTS is often treated as a way to strictly improve a policy by suggesting better actions for training. In practice, this improvement is only heuristic and can fail when value estimates and search are flawed. Late-game evaluation errors, narrow training data, and low simulation counts can make MCTS produce worse action distributions than the underlying policy network.
caveats: Skip it if you want something directly about LLM agents or production infrastructure rather than RL/search dynamics and training pathologies.
pitch: 'If you care about how AI systems fail in practice, this is worth your time because it digs into a real failure mode of MCTS and self-play training: search can quietly make a policy worse when value estimates, late-game data, or simulation budgets are bad.'
---

## Key Points

- MCTS is used to propose actions that are assumed to be strictly better than the policy’s original choices.
- Training the policy network on MCTS-chosen actions is intended to improve future performance under the same states.
- This setup resembles DAGGER-style interventions in robotics and imitation learning, where corrective actions are provided from bad states.
- There is no theoretical guarantee that MCTS must outperform the current policy in practice.
- If value estimates at terminal or leaf states are poor, their errors propagate up the tree and distort MCTS decisions.
- A collapse in self-play diversity or frequent resignations can deprive the value network of accurate late-game training data.
- Low numbers of simulations in MCTS increase variance, so the search may not reliably explore good actions.
- AlphaGo Lee likely used full playouts and can force some games to end without resignation to anchor late-game value estimates with real outcomes.

## Notes

## MCTS as a Policy Improver

MCTS is often used in conjunction with a policy network in games like Go. Conceptually, it is treated as a mechanism that, given a state where the agent might ultimately lose, returns a set of actions that are each strictly better than the policy’s original proposals. These MCTS-selected actions, paired with their originating states, form training tuples. The policy network is then retrained to predict these MCTS-improved actions instead of its initial choices. Under this view, repeatedly training on such tuples should make the policy network better over time.

This is analogous to ideas from DAGGER in robotics and imitation learning. In those settings, even if the agent finds itself in a bad state, an expert can still provide a corrective action that steers it back toward safety or success. Similarly, even from a poor game position, MCTS is treated as providing a corrective action that is better than the agent’s raw policy output.

## No Formal Guarantee of Superiority

There is an intuitive question about whether MCTS is always better than the base policy. Since MCTS uses a value network to evaluate leaf nodes, early in training the value network may be poorly trained, especially on finished games. In that regime, it is possible that search guided by inaccurate value estimates leads to worse decisions than just following the raw, perhaps randomly initialized, policy. Thus, in practice, the belief that MCTS is better than the policy is a heuristic, not a theoretical guarantee.

The speaker offers a concrete failure mode that can arise even after training has progressed significantly. Self-play training might reach a strong level, but then the system collapses or degrades because of issues like insufficient data diversity. This can lead to regions of the state space being poorly evaluated.

## How Bad Value Estimates Corrupt MCTS

Consider a board state where the policy network’s action distribution is good: it recommends strong moves for that position. However, the value network might be miscalibrated on the resulting late-game states. For example, if most self-play games end by resignation rather than being played to a terminal outcome, the training data may lack accurate examples of late-stage positions and their true values.

In such a scenario, the replay buffer might contain almost exclusively losing examples or mis-evaluated positions in a particular late-game pattern, such as a specific corner sequence. As a result, the value function at those terminal or near-terminal states becomes very inaccurate, perhaps systematically pessimistic or otherwise wrong. When MCTS expands the tree and evaluates leaf nodes, it relies on these flawed terminal values.

Because MCTS backups aggregate information from the leaves back to the root, errors at the leaves propagate upward. The selection criterion (e.g., PUCT) uses these backed-up values to decide which branches to explore further. If the backed-up values are distorted, the search will be biased toward suboptimal moves and away from genuinely strong actions. Consequently, the final visitation distribution over actions that MCTS produces at the root can diverge significantly from the original, good policy distribution.

In this way, the MCTS-improved distribution can actually be worse than the base policy. Training the policy to imitate this degraded distribution would then harm performance instead of improving it.

## Role of Simulation Count and Variance

Another practical issue is the number of simulations used in MCTS. The convergence guarantees of Monte Carlo Tree Search rely on taking the number of simulations to infinity. With a small number of simulations, the search is subject to high variance and may not explore enough of the action space.

Limited simulations can cause the search to overfit to noisy initial evaluations or random fluctuations in rollouts or value estimates. This variance further undermines the assumption that MCTS always yields a better action distribution than the underlying policy. Thus, both inaccurate value estimates and low simulation counts can “screw with” the quality of the MCTS output.

## Mitigations via Full Playouts

The speaker connects these issues to design choices in systems like AlphaGo Lee. They suspect that the inclusion of full playouts to the end of the game during training was intended to ground value estimates in actual terminal outcomes, rather than relying solely on intermediate estimates.

One practical approach is to prevent agents from resigning in a fraction of self-play games, for example, in 10% of them. For these games, the system forces play to continue until a true terminal result is reached. This strategy enriches the replay buffer with late-game positions and their correct final outcomes, counteracting the bias that arises when most games end early by resignation.

By anchoring value estimates with more accurate late-stage data, MCTS can be better aligned with true game outcomes. This reduces the risk that search will be misled by poorly trained value functions in late-game situations, making the heuristic that MCTS improves the policy more reliable in practice, even though no strict guarantee exists.

