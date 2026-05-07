# LLM Agents

**Summary**: An AI agent is a system that perceives its environment, reasons about context, and takes actions to achieve goals in a continuous loop; LLM-powered agents use language as interface and planning as the core reasoning strategy.

**Sources**: `From Hardcoded Tools to Reinforcement Learning to LLM Agents_ The Evolution of AI Systems.md`, `RAG is Dead. Karpathy's LLM Wiki is the future  Project Explained.md`, `LangChain Just Released Deep Agents — And It Changes How You Build AI Systems.md`

**Last updated**: 2026-05-07

**Tags**: `agentic-ai` `llm-fundamentals` `concept` `foundational` `ai-evolution`

---

## Definition

While traditional software produces a static output, an AI agent is designed for **interaction**: it perceives its environment, makes decisions based on reasoning or learned policies, and takes actions to achieve specific goals (source: From Hardcoded Tools to Reinforcement Learning to LLM Agents_ The Evolution of AI Systems.md).

## The Agent Loop

```
Observe → Reason → Act → (repeat)
```

1. **Observe**: Gather inputs from users, APIs, or digital environments
2. **Reason**: Interpret context and determine the next logical step
3. **Act**: Execute actions that affect the environment; use feedback to adjust the next move

## Why LLMs Enable Agents

Three properties of LLMs make them the foundation for modern agents (source: From Hardcoded Tools to Reinforcement Learning to LLM Agents_ The Evolution of AI Systems.md):

- **Language as Interface** — natural language replaces rigid scripts; any tool or API can be commanded in plain text
- **Generalization** — one model handles diverse tasks without domain-specific retraining
- **Planning** — LLMs decompose ambiguous goals into actionable steps

## Plausible Reasoning

LLMs don't "understand" the world the way humans do. They perform **Plausible Reasoning** — making highly coherent, contextual inferences within a semantic space. This is sufficient for most real-world agent tasks (source: From Hardcoded Tools to Reinforcement Learning to LLM Agents_ The Evolution of AI Systems.md).

## Core Challenges for Long-Running Agents

1. **Context limits** — long tasks fill the context window; solutions include offloading to filesystems, compression, and subagents (see [[context-window-management]])
2. **Planning** — breaking complex goals into trackable steps
3. **Memory** — retaining knowledge across sessions and threads
4. **Tool use** — calling external APIs, code execution, file operations
5. **Resource budgeting** — autonomous agents can rapidly deplete compute/API credits without hard limits (see [[openclaw]] for a concrete example)
6. **Human oversight** — autonomous operation requires checkpoints; misaligned decisions are a real failure mode

The [[langchain-deep-agents|deepagents]] library addresses all four out of the box.

## Historical Context

LLM agents represent the third wave of AI system evolution, following rule-based systems and reinforcement learning. See [[ai-systems-evolution]] for the full picture.

## Related pages

- [[ai-systems-evolution]]
- [[langchain-deep-agents]]
- [[langchain-ecosystem]]
- [[context-window-management]]
- [[llm-wiki]]
- [[reinforcement-learning]]
- [[openclaw]]
