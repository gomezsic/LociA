# Wiki Index

**Last updated**: 2026-05-07

This is the master table of contents for the AI & Coding knowledge base.
All pages are sourced from curated Medium articles.

---

## Tag taxonomy

Tags applied to every page for semantic navigation.

**Type tags**: `source-summary` · `concept`

**Topic tags**: `knowledge-management` · `rag` · `rag-alternative` · `persistent-knowledge` · `agentic-ai` · `langchain` · `context-management` · `reinforcement-learning` · `llm-fundamentals` · `tools` · `business-ai` · `ai-oversight` · `ai-evolution` · `historical`

**Depth tags**: `foundational` · `practical`

---

## LLM Fundamentals

Core concepts around Large Language Models — how they work, how they are trained,
and how they reason.

| Page | Summary | Tags |
|------|---------|------|
| [[reinforcement-learning]] | RL paradigm: trial-feedback-optimization, strengths, limits, role in LLM training | `reinforcement-learning` `llm-fundamentals` `ai-evolution` `foundational` |

---

## Agentic AI

Autonomous agents, multi-agent systems, tool use, memory, and planning.

| Page | Summary | Tags |
|------|---------|------|
| [[llm-agents]] | What AI agents are, the observe-reason-act loop, why LLMs enable agents, core challenges | `agentic-ai` `llm-fundamentals` `foundational` |
| [[langchain-deep-agents]] | `deepagents` library: planning, virtual filesystem, subagents, context compression, persistent memory | `langchain` `agentic-ai` `context-management` `practical` |
| [[langchain-ecosystem]] | LangChain / LangGraph / deepagents layered stack and when to use each | `langchain` `agentic-ai` `tools` `practical` |
| [[context-window-management]] | Strategies for handling context limits: offloading, compression, subagents, persistent memory | `context-management` `agentic-ai` `practical` |
| [[openclaw]] | OpenClaw AI automation tool: benefits, resource consumption risks, oversight lessons | `tools` `business-ai` `agentic-ai` `ai-oversight` |
| [[ai-systems-evolution]] | *(source)* Three waves of AI: rule-based → RL → LLM agents | `ai-evolution` `agentic-ai` `historical` |

---

## Reinforcement Learning

RL algorithms, RLHF, reward modeling, PPO, DPO, and alignment techniques.

| Page | Summary | Tags |
|------|---------|------|
| [[reinforcement-learning]] | RL as the second wave of AI evolution; strengths, limitations, and role in LLM training | `reinforcement-learning` `foundational` |

---

## Python

Language features, best practices, async, type hints, packaging, and idioms.

| Page | Summary |
|------|---------|
| *(empty)* | |

---

## PyTorch

Tensors, autograd, nn.Module, training loops, optimization, and GPU usage.

| Page | Summary |
|------|---------|
| *(empty)* | |

---

## ML Libraries

Hugging Face, LangChain, LlamaIndex, vLLM, Ollama, and other key tools.

| Page | Summary | Tags |
|------|---------|------|
| [[langchain-ecosystem]] | LangChain / LangGraph / deepagents — the full stack and when to use each layer | `langchain` `tools` |
| [[langchain-deep-agents]] | `deepagents`: the opinionated agent harness from LangChain | `langchain` `practical` |

---

## Vibe Coding

AI-assisted development workflows — Cursor, Copilot, prompt-driven coding,
code generation techniques, and best practices.

| Page | Summary |
|------|---------|
| *(empty)* | |

---

## Model Architecture

Emerging architectures beyond vanilla transformers — MoE, SSM, Mamba, and more.

| Page | Summary |
|------|---------|
| *(empty)* | |

---

## Inference & Optimization

Quantization, distillation, serving strategies, latency reduction, and deployment.

| Page | Summary |
|------|---------|
| *(empty)* | |

---

## Datasets & Training

Data curation, fine-tuning, pre-training, evaluation, and benchmarks.

| Page | Summary |
|------|---------|
| *(empty)* | |

---

## Knowledge & Memory Systems

Patterns for giving AI persistent, compounding knowledge — LLM Wiki, RAG, vector stores.

| Page | Summary | Tags |
|------|---------|------|
| [[llm-wiki]] | Karpathy's LLM Wiki pattern: compilation vs retrieval, three operations, four scales | `knowledge-management` `persistent-knowledge` `foundational` `practical` |
| [[rag]] | RAG explained: how it works, what it solves, and its core statelessness limitation | `rag` `knowledge-management` `foundational` |
| [[memex]] | Vannevar Bush's Memex (1945): historical predecessor to LLM Wiki and hypertext | `knowledge-management` `historical` |
| [[rag-vs-llm-vs-llm-wiki]] | Confronto diretto: plain LLM vs RAG vs LLM Wiki — quando usare ciascuno | `rag` `rag-alternative` `knowledge-management` `foundational` |
| [[rag-is-dead-llm-wiki]] | *(source)* RAG vs LLM Wiki deep dive + FreeBirdsCrew WhatsApp bot implementation | `rag-alternative` `practical` |
| [[llm-wiki-pattern-deep-dive]] | *(source)* Compilation vs retrieval, three operations, four scales, Memex connection, tooling | `knowledge-management` `persistent-knowledge` `practical` `historical` |

---

## Concept glossary

Key terms and definitions that appear across multiple pages.

| Term | Definition | Page |
|------|-----------|------|
| Agent harness | Higher-level framework with opinionated defaults on top of a graph runtime | [[langchain-deep-agents]] |
| Plausible Reasoning | LLMs make coherent contextual inferences without true understanding | [[llm-agents]] |
| LLM Wiki | Persistent markdown knowledge base maintained by an AI agent | [[llm-wiki]] |
| RAG | Retrieval-Augmented Generation — stateless retrieval pipeline at query time | [[rag]] |
| Compilation vs Retrieval | Wiki pattern builds knowledge upfront; RAG re-derives it on every query | [[llm-wiki]] |
| Context compression | Replacing full conversation history with an LLM-generated summary | [[context-window-management]] |
| Virtual filesystem | Agent-accessible storage for offloading large tool results out of context | [[context-window-management]] |
| Memex | Bush's 1945 vision of a personal curated knowledge store with associative trails | [[memex]] |
| Ingest / Query / Lint | The three operations of the LLM Wiki maintenance cycle | [[llm-wiki]] |
