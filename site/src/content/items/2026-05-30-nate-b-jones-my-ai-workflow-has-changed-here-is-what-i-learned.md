---
title: My AI Workflow Has Changed (Here is What I Learned)
author: Nate B Jones
source_id: 1
source_slug: nate-b-jones
url: https://www.youtube.com/watch?v=rqVzTX8w_w0
published_at: '2026-05-30T15:00:04Z'
duration_seconds: null
primary_theme: tech
secondary_theme: thinking
relevance: 6
hook: Nate radically reorganizes his AI workflow around local files and collaborative prompting.
tldr: Nate now builds large, clean context windows by having Codeex locate and copy relevant local files into dedicated working folders. With newer models like Codeex and Claude 5.5, he has shifted from tightly engineered, directive prompts to an exploratory, collaborative process that first clarifies the task shape. This combination lets him run long, complex, multi-threaded projects more reliably and efficiently without allegiance to any particular AI provider.
caveats: Skip it if you want hard evals, failure analysis, or architecture numbers rather than one person’s evolving workflow and tool preferences.
pitch: If you care about how people are actually organizing LLM work in practice, this gives you a concrete file-based workflow for handling long context, messy multi-step tasks, and local guardrails that you can compare against your own agent/RAG setup.
---

## Key Points

- Nate uses Codeex to search his local file system by natural-language descriptions of files.
- Codeex copies the matched files into a clean working folder, creating a curated context window.
- He then starts a fresh Codeex chat pointed specifically at that working folder for focused tasks.
- This workflow enables him to handle 30–50k-word documents and complex spreadsheets or code projects.
- He finds this folder-based workflow works well in Codeex but not in Claude Code or CoWork.
- His prompting style shifted from rigidly specifying tasks to collaboratively defining the task shape with the model.
- Newer models like Claude 5.5 and updated Codeex can stay on task through messy exploration and later execution.
- Using Codeex, he can multi-thread projects, run multiple prompts, and rely on strong auto-review guardrails locally.

## Notes

## Building Context Windows with Local Files

- Nate’s main shift this week is how he assembles context windows using Codeex on his local machine.
- Instead of manually tracking file names and locations, he relies on natural-language descriptions to find what he needs.
- He tells Codeex roughly what a file is about, when he created it, or other descriptive details rather than exact titles.
- Codeex reliably locates these files on his file system and then makes copies into a dedicated working folder.
- This working folder becomes a curated context window: a clean, isolated space containing only the relevant files for the current task.
- After that, he opens a new Codeex chat and instructs it to work exclusively within this folder.
- If he has detailed instructions, he saves them as a transcript or task file inside the folder so the model can reference them.

## Capabilities Unlocked by the Folder-Centric Workflow

- With this setup, Nate can handle very large text workloads—on the order of 30,000 to 50,000 words—with Codeex.
- The same approach works for complex document writing, spreadsheets, and coding tasks because the model can navigate the folder structure effectively.
- He views this as a natural extension of Codeex’s origins in a sandboxed, repo-style environment where everything lives in a GitHub repository.
- In that paradigm, code files and text files are fundamentally similar: both are files in folders that the model reads and relates to each other.
- Nate reports that this specific workflow performs well in Codeex but did not work when he tried similar approaches with Claude Code or CoWork.
- He speculates the difference might relate to Claude’s compute constraints or model versions (e.g., 4.7 vs 5.5), but he is not certain.
- Regardless of the cause, he emphasizes that Codeex’s current behavior makes it easy and efficient to assemble local context windows.

## Evolution of Prompting Strategy

- Nate notes a major evolution in his prompting habits over the past months and model generations.
- Before late 2024 (“before 2025 and the inflection point in December”), he focused heavily on prompt engineering and strict prompt structure.
- That older style emphasized ordering components of the prompt carefully, specifying instructions in detail, and engineering them for one-off workflows.
- Between December and about April 2026, his prompts mostly gave long-running, agentic models specific tasks, pointed them at files, and defined success criteria.
- Success criteria could be expressed via evaluations or within the prompt itself for smaller cases.
- Since around May—especially after Claude 4.7, 5.5, and the Codeex refresh—his style shifted again.
- Now he starts with “meaningful questions” around his standards and goals rather than a rigid task specification.
- He provides some potentially relevant files but first asks the model to help define the “shape” of the task.
- Only after jointly clarifying the task does he ask the model to execute it in a more agentic, autonomous way.

## Collaborative, Messy-Stage Work with Newer Models

- Nate feels that newer models, particularly Claude 5.5 and updated Codeex, handle this messy, exploratory phase well.
- He experiences them as capable of having a genuine back-and-forth collaboration while he is still figuring things out.
- Crucially, they do not “get lost” when he later shifts gears from exploration to directive execution—he can say “now go do it,” and they follow through.
- This robustness in switching from planning to doing underpins his confidence in using them as collaborators rather than just task executors.

## Multi-Threading and Sequential Prompt Execution

- The combination of strong file handling, long-run stability, and auto-review in Codeex enables more advanced workflows for him.
- He can perform simultaneous drafting within a local folder, working on multiple documents or components at once.
- He describes designing a series of eight or nine prompts collaboratively with the model, then running them together and having the model execute them sequentially.
- Codeex’s auto-review system provides guardrails when it runs on his computer, making longer, more autonomous sessions feel safer and more controlled.
- This leads to effective “multi-threading”: incubating multiple ideas or projects in parallel with the model.
- Nate reports that this multi-threaded capability makes AI work not only efficient but genuinely fun, because he can shape and direct many ideas at once.

## Neutrality in the AI “Race”

- Although he currently emphasizes Codeex because of its performance in his workflow, he does not identify with any particular AI vendor.
- He fully expects the landscape to keep shifting and anticipates future releases from Anthropic, such as a potential “4.8” or whatever comes next.
- His priority is not picking a side but becoming more efficient and effective using AI tools as they evolve.
- He frames this stance—focusing on what AI can do for personal and practical work—as the most compelling way to engage with the technology.

## Overall Takeaway

- Nate’s current approach centers on local, folder-based context assembly, collaborative prompt shaping, and multi-threaded execution in Codeex.
- This trio—file-centric context windows, exploratory then agentic prompting, and strong auto-review—has materially changed how he works with AI.
- He offers this as a snapshot of how his AI usage is evolving week by week rather than a fixed, final workflow.

