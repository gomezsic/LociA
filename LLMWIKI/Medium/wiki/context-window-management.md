# Context Window Management

**Summary**: Strategies for managing LLM context limits in long-running agent tasks, including filesystem offloading, summarization, and subagent delegation — as implemented by deepagents and as a general challenge in agentic AI.

**Sources**: `LangChain Just Released Deep Agents — And It Changes How You Build AI Systems.md`

**Last updated**: 2026-05-07

**Tags**: `context-management` `agentic-ai` `langchain` `concept` `practical`

---

## The Problem

LLM context windows are finite. Long agent tasks accumulate conversation history, tool results, and intermediate outputs that can easily exceed the window. Naive approaches (truncation, chunking) lose information; long inputs slow inference and increase cost (source: LangChain Just Released Deep Agents — And It Changes How You Build AI Systems.md).

## Strategy 1: Filesystem Offloading

When a tool result exceeds a threshold (e.g., 20,000 tokens in deepagents), save it to a virtual filesystem and replace it in context with a file path reference + short preview. The agent calls `read_file` or `grep` only when it actually needs the content (source: LangChain Just Released Deep Agents — And It Changes How You Build AI Systems.md).

This is **purposeful offloading with on-demand retrieval** — not truncation, not [[rag|RAG]]-style chunking.

## Strategy 2: Context Compression / Summarization

When context reaches ~85% of the window limit, trigger LLM-generated summarization:
- Summarize: session intent, artifacts created, key decisions, next steps
- Replace full conversation history in working memory with the summary
- Preserve original messages to filesystem for recovery

This enables agents to run indefinitely on complex tasks (source: LangChain Just Released Deep Agents — And It Changes How You Build AI Systems.md).

## Strategy 3: Subagent Delegation

Delegate isolated subtasks to fresh agent instances with clean context windows. The main agent delegates, the subagent runs autonomously, returns a single summary. Main agent's context stays clean (source: LangChain Just Released Deep Agents — And It Changes How You Build AI Systems.md).

Benefits:
- Parallel execution possible
- Each subagent has full context budget for its subtask
- Errors are isolated

## Strategy 4: Persistent Cross-Session Memory

Store important artifacts (memories, conventions, project state) in persistent backends that survive conversation restarts. Agent retrieves only what it needs rather than re-establishing full context from scratch each session (source: LangChain Just Released Deep Agents — And It Changes How You Build AI Systems.md).

## Implementation in deepagents

`deepagents` combines all four strategies automatically:
1. Auto-offload tool results > 20K tokens to virtual filesystem
2. Auto-compress at 85% context capacity
3. Built-in `task` tool for subagent spawning
4. `CompositeBackend` + LangGraph Store for cross-session memory

See [[langchain-deep-agents]] for the full implementation.

## Related pages

- [[langchain-deep-agents]]
- [[langchain-ecosystem]]
- [[llm-agents]]
