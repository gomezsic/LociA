# LangChain Deep Agents

**Summary**: Overview of `deepagents`, LangChain's "agent harness" library that sits on top of LangGraph and provides built-in planning, virtual filesystem, subagent spawning, context compression, and persistent memory out of the box.

**Sources**: `LangChain Just Released Deep Agents — And It Changes How You Build AI Systems.md`

**Last updated**: 2026-05-07

**Tags**: `langchain` `agentic-ai` `context-management` `tools` `source-summary` `practical`

---

## What It Is

`deepagents` is a standalone Python library (`pip install deepagents`) that acts as a higher-level harness over [[langchain-ecosystem]]. The central entry point is `create_deep_agent()`, which returns a fully configured agent with five capabilities baked in by default (source: LangChain Just Released Deep Agents — And It Changes How You Build AI Systems.md).

```python
from deepagents import create_deep_agent

agent = create_deep_agent(
    tools=[my_tool],
    system_prompt="You are a helpful assistant",
)
agent.invoke({"messages": [{"role": "user", "content": "..."}]})
```

## The Five Built-In Capabilities

### 1. Planning — `write_todos`

Every deep agent has a `write_todos` tool that breaks work into discrete steps with statuses (`pending`, `in_progress`, `completed`). The to-do list is persisted in agent state, not just a prompt trick (source: LangChain Just Released Deep Agents — And It Changes How You Build AI Systems.md).

### 2. Virtual Filesystem

Built-in tools: `ls`, `read_file`, `write_file`, `edit_file`, `glob`, `grep`. When a tool result exceeds 20,000 tokens, the library automatically saves it to the configured backend and replaces the result in context with a file path reference + 10-line preview. This is purposeful offloading with on-demand retrieval — not chunking or truncation (source: LangChain Just Released Deep Agents — And It Changes How You Build AI Systems.md).

Backends are pluggable: in-memory (default), local disk, LangGraph Store, or sandboxed environments (Modal, Daytona).

### 3. Subagent Spawning

A built-in `task` tool lets the main agent delegate isolated subtasks to fresh subagent instances with clean context windows. Subagents run autonomously and return a single summary to the main agent, keeping the orchestrator's context manageable. Custom subagents can be configured with their own tools and system prompts (source: LangChain Just Released Deep Agents — And It Changes How You Build AI Systems.md).

### 4. Automatic Context Compression

When context reaches 85% of the model's window limit, the harness triggers LLM summarization: session intent, artifacts, and next steps are compressed into a structured summary that replaces the full history in working memory. Original messages are preserved to the filesystem for recovery (source: LangChain Just Released Deep Agents — And It Changes How You Build AI Systems.md).

See [[context-window-management]] for the broader concept.

### 5. Long-term Memory Across Conversations

Using a `CompositeBackend` with LangGraph Store, files at `/memories/` persist across sessions and threads. This enables agents that remember preferences, conventions, and multi-day project progress (source: LangChain Just Released Deep Agents — And It Changes How You Build AI Systems.md).

## Stack Positioning

| Layer | Role |
|-------|------|
| LangChain | Building blocks: models, tools, prompts |
| LangGraph | Runtime: stateful graph execution, streaming, persistence |
| deepagents | Harness: opinionated defaults + infrastructure on top of both |

"LangGraph gives you an engine and a transmission. Deep Agents gives you a car." (source: LangChain Just Released Deep Agents — And It Changes How You Build AI Systems.md)

## When to Use It

Use `deepagents` when: tasks require multi-step planning, tool results are large, subagent delegation is needed, or persistent memory is required.

Stick with `create_agent` or raw LangGraph when: agents are simple (1–2 tool calls), fine-grained graph control is needed, or you're already deep in a custom LangGraph workflow.

## CLI

`deepagents` also ships a command-line coding agent (`deepagents` command) with interactive mode, pipe mode (`-n` flag), custom skills, and persistent memory — similar to Claude Code or Aider (source: LangChain Just Released Deep Agents — And It Changes How You Build AI Systems.md).

## Related pages

- [[langchain-ecosystem]]
- [[context-window-management]]
- [[llm-agents]]
