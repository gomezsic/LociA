---
title: "What is LLM Wiki Pattern? Persistent Knowledge with LLM Wikis"
source: "https://medium.com/@tahirbalarabe2/what-is-llm-wiki-pattern-persistent-knowledge-with-llm-wikis-3227f561abc1"
author:
  - "[[Tahir]]"
published: 2026-04-07
created: 2026-05-07
description: "More"
tags:
  - "clippings"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*JliTbd0eNKpVpOHxvxSDAg.png)

FULL CREDIT:[**Andrej Karpathy**](https://x.com/karpathy)

**TLDR:**  
Most of our knowledge infrastructure is designed for retrieval, not accumulation. Search engines retrieve. RAG retrieves. Even memory augmented LLMs retrieve. They all ask: “What documents are relevant to this query?”

***The wiki pattern asks: “What would a diligent, tireless research assistant build over time if they never forgot anything?”***

That is the shift. From retrieval to compilation. **From stateless to stateful knowledge.** On a grand scale, that changes how societies learn. Not faster searching. Slower, more careful, cumulative understanding, maintained by machines and guided by humans.

![https://x.com/karpathy/status/2039805659525644595?s=20](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*lEgfxpY2D0XwixQRyFYECA.png)

[https://x.com/karpathy/status/2039805659525644595?s=20](https://x.com/karpathy/status/2039805659525644595?s=20)

I saw this clearly when I started using LLMs for research. The standard pattern is RAG. You upload documents. The LLM finds relevant chunks. It generates an answer. Then you ask another question. The LLM does the same thing again. It has to rediscover everything from scratch. There’s no memory. No accumulation.

This is like having a research assistant who reads every book in your library but forgets everything the moment you finish talking. You ask a question. He runs to the shelves. He comes back with an answer. You ask a followup. He runs again. He never connects anything.

There’s a better way.

## The Core Idea

Give the LLM a wiki. A real one. A directory of markdown files that grows over time. When you add a source, the LLM doesn’t just index it. It reads the source. It extracts the important parts. It updates the existing pages. It adds new ones. It fixes cross-references. It notes where new information contradicts old claims.

The knowledge gets compiled once. Then it stays compiled.

Andrej Karpathy has been running this system for several months. He keeps an LLM agent open in one window and Obsidian open in another. The LLM makes edits based on whatever he is discussing. He watches the graph view expand. He clicks through links. He reads the updated pages as they appear.

For Karpathy, Obsidian functions as the IDE. The LLM acts as the programmer. The wiki becomes the codebase. The relationship is clean. The human directs. The machine executes. The knowledge accumulates.

He does not write the wiki himself. The LLM handles all of it. The summarizing. The cross-referencing. The filing. The bookkeeping that normally makes a knowledge base collapse under its own weight. Karpathy supplies the sources and the questions. The LLM supplies the maintenance.

This is the difference between a pile of documents and a living wiki. One is static. The other breathes. One requires you to remember where everything is. The other remembers for you. One forces you to re-derive insights. The other keeps them ready.

## Why This Works

The key insight is that the tedious part of maintaining a knowledge base is not the reading or the thinking. It’s the bookkeeping.

- Updating cross-references
- Keeping summaries current
- Noting contradictions
- Maintaining consistency across dozens of pages

Humans abandon wikis because the maintenance burden grows faster than the value.

LLMs don’t get bored. They don’t forget to update a cross-reference. They can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero.

## The Three Layers

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*puL5LPFa8rMMn7jF9jjNJw.png)

You need three layers to make this work.

### Raw Sources

Your curated collection of documents. Articles, papers, meeting transcripts, journal entries. These are immutable. The LLM reads from them but never changes them.

### The Wiki

A directory of markdown files. Summaries, entity pages, concept pages, comparisons, synthesis. The LLM owns this layer entirely. It creates pages. It updates them. It maintains cross-references. You read it. The LLM writes it.

### The Schema

A configuration file. It tells the LLM how the wiki is structured, what the conventions are, and what workflows to follow. This is what makes the LLM a disciplined wiki maintainer rather than a generic chatbot.

## The Three Operations

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*cIEtp7UAMenHel5fro1c0w.png)

You need three operations to keep the wiki alive.

### Ingest

You drop a new source into the raw collection and tell the LLM to process it. The LLM:

- Reads the source
- Discusses key takeaways with you
- Writes a summary page
- Updates the index
- Updates relevant entity and concept pages
- Appends to the log

A single source might touch 10 or 15 wiki pages. I prefer to ingest sources one at a time and stay involved. I read the summaries. I check the updates. I guide the LLM on what to emphasize.

### Query

You ask questions against the wiki. The LLM searches for relevant pages, reads them, and synthesizes an answer with citations.

The important thing is that good answers can be filed back into the wiki as new pages. A comparison you asked for. An analysis. A connection you discovered. These are valuable. They shouldn’t disappear into chat history.

### Lint

Periodically, ask the LLM to health-check the wiki. Look for:

- Contradictions between pages
- Stale claims that newer sources have superseded
- Orphan pages with no inbound links
- Important concepts mentioned but lacking their own page
- Missing cross-references

The LLM is good at suggesting new questions to investigate and new sources to look for.

## Two Special Files

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*y0huwXMj_9o9xr45u_4wtg.png)

Two files help you navigate as the wiki grows.

### index.md

Content-oriented. A catalog of everything in the wiki. Each page listed with a link and a one-line summary. The LLM updates it on every ingest. When answering a query, the LLM reads the index first to find relevant pages, then drills into them. This works surprisingly well at moderate scale. A hundred sources. A few hundred pages.

### log.md

Chronological. An append-only record of what happened and when. Ingest. Query. Lint. The log gives you a timeline of the wiki’s evolution. It helps the LLM understand what’s been done recently.

## What You Can Build

This pattern works for many contexts.

### 1\. The individual scale (you)

You read an article. You learn something. Two weeks later, you need that insight again. You have forgotten it. You re read the article. Or you search your notes, but your notes are scattered.

**What the wiki pattern solves:** Your knowledge compounds. Every source you add, every question you ask, makes the wiki richer, not just bigger. You stop re deriving what you already figured out.

### 2\. The team scale (a company)

A team has Slack threads, meeting transcripts, design docs, customer calls. Knowledge lives in silos. New people ask the same questions. Someone writes a wiki page, but it goes stale in a month because no one updates it.

**What the wiki pattern solves:** An LLM maintainer keeps the wiki evergreen. It reads every new Slack thread, every meeting, and updates the relevant pages automatically. The team stops paying the “maintenance tax” that kills internal wikis. Knowledge stays alive.

### 3\. The research scale (science / academia)

Researchers publish papers. Each paper is a snapshot. Synthesizing 200 papers into a coherent understanding is a massive human effort. Literature reviews take months. And as new papers come out, the synthesis breaks.

**What the wiki pattern solves:** A continuously updating meta review. The LLM reads every new paper, updates the synthesis, flags contradictions, highlights where new evidence challenges old claims. Researchers stop rediscovering what the field already knows. They build on a living document.

### 4\. The societal scale (human knowledge)

Think of Wikipedia. It is humanity’s wiki. But it is maintained by volunteers. It is slow. It has gaps. It cannot keep up with the rate of new information.

**What the wiki pattern solves (in principle):** Automated, persistent knowledge compilation at scale. Not replacing humans, but handling the bookkeeping that humans cannot do fast enough. Imagine every news article, every scientific preprint, every public dataset feeding into a wiki that compiles rather than just indexes. The result is not a search engine. It is a living, cross referenced map of what we know, what we do not know, and where we disagree.

## Other Uses

- Competitive analysis
- Due diligence
- Trip planning
- Course notes
- Hobby deep-dives

Anything where you’re accumulating knowledge over time and want it organized rather than scattered.

## Practical Tips

A few things that help.

Obsidian Web Clipper converts web articles to markdown. Very useful for quickly getting sources into your raw collection.

Download images locally. In Obsidian Settings, set an attachment folder path. After clipping an article, hit a hotkey and all images get downloaded. LLMs can’t read markdown with inline images in one pass. The workaround is to have the LLM read the text first, then view referenced images separately for additional context. It’s a bit clunky but works.

Obsidian’s graph view is the best way to see the shape of your wiki. What’s connected to what. Which pages are hubs. Which are orphans.

Marp is a markdown-based slide deck format. Obsidian has a plugin. Useful for generating presentations directly from wiki content.

Dataview runs queries over page frontmatter. If your LLM adds YAML frontmatter to wiki pages, Dataview can generate dynamic tables and lists.

The wiki is just a git repo of markdown files. You get version history, branching, and collaboration for free.

## The Division of Labor

The human’s job is to:

- Curate sources
- Direct the analysis
- Ask good questions
- Think about what it all means

The LLM’s job is everything else.

## A Note on Abstraction

This [tweet](https://x.com/karpathy/status/2039805659525644595?s=20) is intentionally abstract. It describes the idea, not a specific implementation. The exact directory structure, the schema conventions, the page formats, the tooling. All of that depends on your domain, your preferences, and your LLM of choice.

Everything I mentioned is optional. Pick what’s useful. Ignore what isn’t.

- Your sources might be text-only. You don’t need image handling.
- Your wiki might be small. The index file is enough. No search engine required.
- You might not care about slide decks. Just markdown pages.
- You might want a completely different set of output formats.

The right way to use this is to share it with your LLM agent and work together to instantiate a version that fits your needs. The document’s only job is to communicate the pattern. Your LLM can figure out the rest.

## The Deeper Connection

This idea is old. Vannevar Bush described something like it in 1945. He called it the Memex. A personal, curated knowledge store with associative trails between documents. His vision was closer to this than to what the web became. Private. Actively curated. With the connections between documents as valuable as the documents themselves.

The part he couldn’t solve was who does the maintenance.

Now we know.

## Further Reading:

[🐍 LiteLLM PyPI Supply Chain Attack Detection and Remediation](https://medium.com/@tahirbalarabe2/litellm-pypi-supply-chain-attack-detection-and-remediation-cef5e99270ed)

[🐍The LiteLLM PyPI Supply Chain Attack What You Need to Know](https://medium.com/@tahirbalarabe2/the-litellm-pypi-supply-chain-attack-what-you-need-to-know-6ab536d4aeb3)

[What is Moltbook? The Social Network for Ai Agents](https://medium.com/@tahirbalarabe2/what-is-moltbook-the-social-network-for-ai-agents-12f7a28a2d12)

[What is Clawdbot(Moltbot)?](https://medium.com/@tahirbalarabe2/what-is-moltbook-the-social-network-for-ai-agents-12f7a28a2d12)

[🦞(Clawdbot) MoltBot OpenClaw Local System Architecture](https://medium.com/@tahirbalarabe2/clawdbot-moltbot-openclaw-local-system-architecture-52acc37f1213)

[WHAT ARE AGENT SKILLS?](https://medium.com/@tahirbalarabe2/what-are-agent-skills-c7793b206daf)

[Agent Skills Vs MCP Vs Prompts Vs Projects Vs Subagents:A Comparative Analysis](https://medium.com/@tahirbalarabe2/agent-skills-vs-mcp-vs-prompts-vs-projects-vs-subagents-a-comparative-analysis-7a36cd85cb74)

[⌨️ What is LLM Prompt Engineering?](https://medium.com/@tahirbalarabe2/%EF%B8%8F-what-is-llm-prompt-engineering-e80c59bd522e)

[📈 Prompt Engineering Made Simple with the RISEN Framework](https://medium.com/@tahirbalarabe2/prompt-engineering-made-simple-with-the-risen-framework-038d98319574)

[💡 What is Prompt Engineering?:: RAG, CoT, ReAct & DSP Explained](https://medium.com/@tahirbalarabe2/what-is-prompt-engineering-rag-cot-react-dsp-explained-0aa0a9bd0a90)

[🔗What is Model Context Protocol? (MCP) Architecture Overview](https://medium.com/@tahirbalarabe2/what-is-model-context-protocol-mcp-architecture-overview-c75f20ba4498)

[How DRIFT Stops Prompt Injection Attacks in LLM Agents](https://medium.com/@tahirbalarabe2/how-drift-stops-prompt-injection-attacks-in-llm-agents-9454368f5e4c)

[Implementing Secure by Design Principles in AI System Development](https://medium.com/@tahirbalarabe2/implementing-secure-by-design-principles-in-ai-system-development-5ea2d199bb28)

[How to Build an Enterprise AI Compliance Program](https://medium.com/@tahirbalarabe2/how-to-build-an-enterprise-ai-compliance-program-58aba0861651)

[🕵️How to Monitor AI Models in Production](https://medium.com/@tahirbalarabe2/%EF%B8%8Fhow-to-monitor-ai-models-in-production-2f29820094f3)

[⚙️AWS Well-Architected Best Practices](https://medium.com/@tahirbalarabe2/%EF%B8%8Faws-well-architected-best-practices-5c36c6a9cde6)

[Building Cloud Agnostic Resilience After AWS Outage](https://medium.com/@tahirbalarabe2/building-cloud-agnostic-resilience-after-aws-outage-7dbe1f04becc)

[Building Secure AI Agents with Data Governance](https://medium.com/@tahirbalarabe2/building-secure-ai-agents-with-data-governance-dc7865eab9f7)

[Part 1: Building AI Data Governance](https://medium.com/@tahirbalarabe2/building-ai-data-governance-with-databricks-unity-catalog-e1d5ed4cab2f)

[**Part 2: Building The HR Agent**](https://medium.com/@tahirbalarabe2/build-your-ai-agent-with-tool-calling-5111eab61521)

[Part 3: Evaluating and Deploying the HR Analytics Agent](https://medium.com/@tahirbalarabe2/evaluating-and-deploying-ai-agent-0e878e27cc7f)

[How to Build a Secure Enterprise Sovereign AI Factory with Open-Source.](https://medium.com/@tahirbalarabe2/how-to-build-a-secure-enterprise-sovereign-ai-factory-with-open-source-361990805673)

[Build AI Customer Support Agents with PydanticAI](https://medium.com/@tahirbalarabe2/building-type-safe-ai-agents-with-pydanticai-fee757c6a00f)

[⚙️LangChain vs. LangGraph: A Comparative Analysis](https://medium.com/@tahirbalarabe2/%EF%B8%8Flangchain-vs-langgraph-a-comparative-analysis-ce7749a80d9c)

[🔗What is Model Context Protocol? (MCP) Architecture Overview](https://medium.com/@tahirbalarabe2/deepseek-r1-explained-chain-of-thought-reinforcement-learning-and-model-distillation-0eb165d928c9)

[🚀DeepSeek R1 Explained: Chain of Thought, Reinforcement Learning, and Model Distillation](https://medium.com/@tahirbalarabe2/deepseek-r1-explained-chain-of-thought-reinforcement-learning-and-model-distillation-0eb165d928c9)

[💻What is Ollama: Running Large Language Models Locally](https://medium.com/@tahirbalarabe2/what-is-ollama-running-large-language-models-locally-e917ca40defe)

[Model Context Protocol (MCP) vs. APIs: The New Standard for AI Integration](https://medium.com/@tahirbalarabe2/model-context-protocol-mcp-vs-apis-the-new-standard-for-ai-integration-d6b9a7665ea7)

[🧠Understanding LLM Context Windows: Tokens, Attention, and Challenges](https://medium.com/@tahirbalarabe2/understanding-llm-context-windows-tokens-attention-and-challenges-c98e140f174d)

[How DRIFT Stops Prompt Injection Attacks in LLM Agents](https://medium.com/@tahirbalarabe2/how-drift-stops-prompt-injection-attacks-in-llm-agents-9454368f5e4c)

## Frequently Asked Questions (FAQ)

## 1\. How is this different from RAG?

Standard RAG retrieves relevant chunks from raw documents at query time and generates an answer from scratch each time. The wiki approach compiles knowledge once into a structured, cross-referenced set of pages. When you ask a question, the LLM reads existing summaries and syntheses — the work has already been done. New sources update the wiki incrementally rather than forcing re-derivation.

## 2\. How large can the wiki grow before this breaks?

The index file works well up to a few hundred pages and ~100 sources. Beyond that, you’ll want a search engine (e.g., `qmd` or a simple `grep` +LLM reranker). The pattern itself scales; the limiting factor is how you retrieve relevant pages. Many users run wikis with thousands of pages by adding a lightweight search layer.

## 3\. Do I need to use Obsidian?

No. Obsidian is recommended because it gives you a live graph view, markdown editing, and plugins (Dataview, Marp, Excalidraw). But any markdown editor works — VS Code, Typora, even a plain text editor. The wiki is just a directory of `.md` files.

## 4\. What if the LLM makes mistakes in the wiki?

Treat the wiki as a living draft, not an immutable archive. Mistakes happen. The fix: ask the LLM to correct a specific page, or manually edit it yourself. Regular `lint` operations catch contradictions and stale claims. Version control (git) lets you roll back bad changes.

## 5\. Can multiple people collaborate on the same wiki?

Yes. Since the wiki is a git repo, multiple humans can push/pull. For LLM agents, you need coordination — typically one agent session at a time, or a shared schema that prevents conflicting updates. Some teams use a “wiki maintainer” LLM that processes pull requests from human reviewers.

## 6\. What about images, PDFs, and non-markdown sources?

- Images: Download locally (Obsidian Web Clipper + hotkey). LLMs can read markdown text first, then view referenced images separately via multi-modal models (GPT-4o, Claude 3.5 Sonnet, Gemini).
- PDFs: Convert to markdown using tools like `marker` or `pypdf` before ingesting. The LLM works best with plain text.
- Audio/video: Transcribe first (Whisper, etc.), then ingest the transcript.

## 7\. How do I avoid the LLM hallucinating when it writes wiki pages?

Ground every wiki update in the raw source files. The schema should enforce citations — every claim in a wiki page should reference a specific source (e.g., `(source: raw/article-2024-03-15.md)`). During `ingest`, the LLM reads the source and writes summaries that directly quote or paraphrase with attribution. Lint checks can flag uncited statements.

## 8\. Do I need to keep the raw sources after they’re ingested?

Yes. Raw sources are the source of truth. The wiki is a derived artifact. If you delete raw sources, you lose the ability to verify claims or re-ingest with a different schema. Keep them immutable in a `raw/` directory.

## 9\. What’s the point of the log file if I have git?

Git tracks file changes. The log tracks semantic events — ingests, queries, lint passes — with human-readable context. It helps the LLM understand what’s happened recently without diffing every file. Also, you can `grep` the log to see "when did we last process a source about X?"