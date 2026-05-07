# LangChain Ecosystem

**Summary**: The LangChain ecosystem is a layered stack for building LLM-powered applications: LangChain provides building blocks, LangGraph adds stateful graph execution, and deepagents provides an opinionated agent harness on top.

**Sources**: `LangChain Just Released Deep Agents — And It Changes How You Build AI Systems.md`

**Last updated**: 2026-05-07

**Tags**: `langchain` `agentic-ai` `tools` `concept` `practical`

---

## The Three Layers

```
deepagents       ← Agent harness (opinionated defaults, built-in infrastructure)
─────────────────────────────────────────────────────────────────────────────
LangGraph        ← Runtime (stateful graph execution, streaming, persistence)
─────────────────────────────────────────────────────────────────────────────
LangChain        ← Foundation (models, tools, prompts, chains)
```

(source: LangChain Just Released Deep Agents — And It Changes How You Build AI Systems.md)

## LangChain

The base framework. Provides modular building blocks:
- Model integrations (OpenAI, Anthropic, etc.)
- Tool definitions
- Prompt templates
- Chain abstractions for simple pipelines

For simple 1–2 tool agents, `langchain.create_agent` is often sufficient.

## LangGraph

A runtime for **durable, stateful, graph-based agent execution**. Handles:
- State schemas and persistence
- Conditional edges and complex control flow
- Streaming
- Interrupts (human-in-the-loop)

LangGraph is a low-level primitive — extremely powerful but requires significant boilerplate for complex agents. Most teams end up re-implementing the same infrastructure patterns (planning, context management, subagents) on top of it (source: LangChain Just Released Deep Agents — And It Changes How You Build AI Systems.md).

## deepagents

A harness built on top of LangChain + LangGraph. It does **not** replace LangGraph — it uses LangGraph under the hood. What it adds is a higher-level API with opinionated defaults so teams don't reinvent infrastructure every time.

Built-in: planning (`write_todos`), virtual filesystem, subagent spawning, context compression, cross-session memory. See [[langchain-deep-agents]] for details.

**Analogy**: LangGraph gives you an engine and a transmission. deepagents gives you a car.

## When to Use Each Layer

| Use case | Recommended layer |
|----------|------------------|
| Simple pipeline, 1–2 tools | LangChain `create_agent` |
| Fine-grained graph control, custom state | Raw LangGraph |
| Long-running, multi-step, large context | `deepagents` |
| Custom subagent architectures | `deepagents` with custom `Subagent` config |

## Related pages

- [[langchain-deep-agents]]
- [[llm-agents]]
- [[context-window-management]]
