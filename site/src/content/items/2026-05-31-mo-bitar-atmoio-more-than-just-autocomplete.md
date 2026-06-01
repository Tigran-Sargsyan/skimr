---
title: More than just autocomplete?
author: Mo Bitar (atmoio)
source_id: 4
source_slug: mo-bitar-atmoio
url: https://www.youtube.com/watch?v=-7RDU-piOVA
published_at: '2026-05-31T11:00:17Z'
duration_seconds: null
primary_theme: tech
secondary_theme: thinking
relevance: 4
hook: AI and brains may both be simple mechanisms massively scaled up.
tldr: The video traces how simple feature detectors in the brain inspired neural networks and, later, transformers. With enough computation, these naive algorithms become surprisingly powerful, echoing Richard Sutton’s “bitter lesson.” This raises unsettling questions about whether intelligence, and possibly even aspects of human meaning, are just simple processes scaled up.
caveats: Skip it if you’re looking for production details, benchmarks, or anything deeper than a broad explanation of why simple methods scale.
pitch: If you want a compact conceptual refresher on how feature detectors, CNNs, transformers, and Sutton’s bitter lesson fit together, this gives you a clean narrative from neuroscience to scaling laws that may spark useful ideas for your own AI work.
---

## Key Points

- A single neuron in a cat’s visual cortex fired only for an edge at a specific angle.
- Vision works through layers of simple feature detectors that build up to complex perceptions like faces.
- Convolutional neural networks mimic simple visual feature detectors and excel at image recognition tasks.
- Transformers let each token attend to all others, handling long-range dependencies better than convolutions in language.
- Modern AI progress relies heavily on massively parallel hardware enabling trillions of operations per second.
- The “bitter lesson” says general methods that scale with computation beat clever handcrafted approaches over time.
- LLMs are trained by penalizing wrong next-word guesses in context, not by raw word frequency counts.
- To predict words well, models must implicitly capture contextual meaning, hinting at an emergent “world model.”

## Notes

## From Cat Visual Experiments to Simple Feature Detectors

In 1958, researchers at Johns Hopkins wired a cat’s visual cortex neuron to a speaker while showing it visual stimuli. Initially, flashing black dots on glass slides produced no neural response. By accident, when a slide’s edge swept across the screen, the neuron fired intensely, like a machine gun in the speaker. The neuron did not respond to dots but specifically to an edge at a particular orientation. Tilting the edge away silenced it; tilting it back reactivated it. This demonstrated that certain neurons are tuned to detect very specific low-level features such as oriented lines.

This led to the idea that vision is not like a camera taking a full picture at once. Instead, the brain uses layers of neurons where each cell “cares” about one very narrow, “dumb” feature: a line at a given angle, an edge moving in a direction, and so on. These were called simple cells, and they feed into complex cells that integrate multiple simple features. Through this hierarchy, edges combine into corners, corners into shapes, and shapes into recognizable entities like faces. These discoveries in visual information processing earned a Nobel Prize in 1981.

## From Simple Cells to Convolutional Neural Networks

The biological insight that perception can emerge from stacks of simple feature detectors underpins convolutional neural networks (CNNs). CNNs use small filters, each responsible for detecting simple patterns in local patches of an image, such as edges. Sliding these filters across an image emphasizes that spatial proximity matters; only nearby pixels are directly compared at each step. Stacking many such layers allows the network to detect progressively larger and more abstract patterns, eventually distinguishing objects like cats and dogs.

CNNs proved extremely effective for vision tasks and are central to systems like self-driving car cameras. However, their reliance on local neighborhoods and proximity limited their suitability for language. In text, relationships can stretch across long distances: a pronoun like “it” may refer to something mentioned much earlier in a paragraph. CNN-style architectures struggled with such long-range dependencies.

## Transformers and Attention as the Basis of Modern LLMs

A major leap came in 2017 with the paper “Attention Is All You Need,” which introduced the transformer architecture. This is the “T” in GPT; the speaker jokingly suggests “GP” could stand for “guessing profusely.” In transformers, each token (often a subword piece rather than a whole word) can attend to all other tokens in a sequence. Conceptually, each token broadcasts a signal about what it represents while listening to signals from all others, weighting the most relevant ones more heavily.

This “all at once” relational mechanism allows the model to connect words and ideas even when they are far apart in the text, solving some of the long-distance connection problems that hindered earlier approaches. This capability formed the basis for today’s large language models (LLMs). The speaker frames this as another example of “simple things scaled up”: a relatively simple mechanism, attention, becomes powerful when stacked and expanded.

## Old Ideas, New Hardware: The Role of Scale

Many core ideas underpinning modern AI date back decades. Early artificial neuron models appeared in the 1940s and 1950s, and the main method for training neural networks (like backpropagation) was worked out in the 1980s. While transformer architectures are more recent, the main historical limitation was not conceptual but computational.

Today’s surge in AI is closely tied to hardware advances—chips that can run thousands of calculations in parallel and reach trillions of operations per second. Under this lens, LLMs are described as fundamentally simple and naive, so simplistic that one might expect them never to work. Yet when these “dumb” algorithms are combined with enormous computing power—enough to metaphorically “light up a small city”—they produce seemingly magical capabilities.

Initially, the speaker viewed this as a hack, doubting that scaling something so naive could count as “real science.” This perspective is challenged by Richard Sutton’s “bitter lesson.”

## The Bitter Lesson: Scale Beats Cleverness

The bitter lesson argues that, over the long run, attempts to engineer clever, human-like reasoning into AI tend to lose to more general methods that can exploit scaling and raw computation. Rather than handcrafting structured human understanding into machines, one lets them perform vast amounts of statistical computation. Over time and with sufficient data and compute, these general methods win.

The speaker compares this to animation. Humans have known how to draw for millennia, but static drawings alone do nothing. The apparent magic of movement arises when a machine shows frames in rapid succession—around 24 per second—so the brain fuses them into motion. The apparent life in animation is a projection emergent from simple frames plus temporal processing.

AI is described as similar: what seems like a “trick” or projection emerges from simple operations executed at vast scale. The speaker admits that this used to be reassuring, a reason not to be overly alarmed. But now they are reconsidering whether dismissing it as “just a projection” misses something deeper.

## Simple Things Scaled Up: Brains and Machines

The speaker reflects that perhaps much of what the brain does is also “simple things scaled up.” Evolution and learning have shaped billions of small processes operating in parallel over immense timescales and experiences. Even if brain mechanisms are not identical to LLMs, both can be seen as systems fitting curves to reality.

In this framing, the human brain approximates aspects of the real world sufficiently well to enhance survival. Machines, through training, can also fit a curve. This leads to the question of whether LLMs fit not just the training data’s surface patterns, but the generative process behind that data—a “world model.”

## Beyond Naive Autocomplete

The common assumption is that LLMs merely autocomplete by predicting the next word based on frequency statistics. The speaker challenges this as incomplete. During training, the model is not rewarded for picking the globally most frequent word; it is judged on whether it selects the correct next word for each specific context.

For example, suppose the most common word after “the” in the dataset is “man.” If, in a particular paragraph, the true continuation is different, predicting “man” is an error. Each wrong guess incurs a penalty, nudging the model’s internal parameters so that in similar contexts it becomes more likely to choose the correct word next time. Repeating this over millions of examples, the model converges to a very complex fit.

To succeed in this game, the model must go beyond crude frequency and start capturing what prior sentences and paragraphs “mean” in a functional sense. It ends up distilling a kind of essence of patterns in the data. This suggests the emergence of something akin to a world model: rather than just reflecting the data directly, the model may approximate the process that produced the data, one level up.

There is ongoing debate about whether LLMs truly have such a world model, but the possibility is noted as significant if true.

## Open-Ended Approximation and Human Centrality

The speaker wonders whether there is any limit to how well AI systems can approximate reality. They contemplate whether AI could eventually fit a “line of best fit” to the world that is even more functionally useful than the human brain’s approximation. They acknowledge these thoughts as speculative and unsettling, with “no present basis in reality,” yet still compelling enough to explore.

They describe a tendency to get drawn into futuristic, science-fiction style thinking and then needing to return to present reality to clarify their beliefs. Historically, they would respond by insisting AI cannot touch domains like love, qualia, feeling, and subjective experience. Recently, however, they feel haunted by the phrase “simple things scaled up,” questioning whether even those seemingly special aspects might ultimately reduce to large-scale simple processes.

This line of thought is not idle for them; it connects directly to the question of what it means to be human. First AI challenged our economic roles by threatening jobs; now, in their view, it is pressing on our spiritual and existential self-understanding. Humans have often preserved a sense of centrality to make reality and suffering more tolerable, to impose meaning on chaos.

Exploring the bitter lesson in this deeper sense is emotionally difficult for the speaker and “bumming” them out. They note that we often reserve intelligence and perhaps consciousness as categorically special, insisting they are not mere scaled-up simplicity. They personally want to believe that. Yet they return to the name “the bitter lesson,” implying that the uncomfortable possibility is that even those cherished capacities might, in some sense, be explainable as simple processes powerfully scaled up.

