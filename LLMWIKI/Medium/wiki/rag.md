# RAG (Retrieval-Augmented Generation)

**Summary**: RAG is a technique that augments LLM responses by retrieving relevant document chunks from a vector database at query time; it solves the knowledge boundary problem but is stateless — knowledge never accumulates between sessions.

**Sources**: `RAG is Dead. Karpathy's LLM Wiki is the future  Project Explained.md`

**Last updated**: 2026-05-07

**Tags**: `knowledge-management` `rag` `retrieval` `concept` `foundational`

---

## How RAG Works

The standard RAG pipeline:

> Upload files → chop into chunks → convert to embeddings → store in vector database → retrieve relevant chunks at query time → generate an answer

(source: RAG is Dead. Karpathy's LLM Wiki is the future  Project Explained.md)

## What RAG Solves

- Extends LLM knowledge beyond training data cutoff
- Grounds responses in specific documents, reducing hallucinations
- Allows private/proprietary data to inform LLM responses without fine-tuning

## The Core Limitation: Statelessness

RAG is fundamentally stateless. Every query triggers the same pipeline from scratch: retrieve → stuff into context → generate → **forget**. There is no accumulation of knowledge between sessions (source: RAG is Dead. Karpathy's LLM Wiki is the future  Project Explained.md).

> "RAG is a librarian who reads every book fresh each morning, with no notes from yesterday."

When you ask the same question tomorrow, RAG rediscovers the same answer the same way, from zero. Cross-document synthesis must happen at query time — expensive, and easily lost.

## Infrastructure Requirements

RAG needs: embeddings model + vector database + retrieval layer + orchestration framework. This is significantly more infrastructure than the [[llm-wiki]] pattern, which needs only a folder of markdown files.

## RAG vs LLM Wiki

| Dimension | RAG | LLM Wiki |
|-----------|-----|----------|
| State | Stateless | Persistent |
| Knowledge growth | None (flat) | Compounds |
| Infrastructure | High | Minimal |
| Cross-document synthesis | Query-time | Pre-built |
| Nuanced questions | No improvement over time | Improves over time |

The [[llm-wiki]] pattern is positioned as the next step beyond RAG for use cases that need compounding knowledge, not just retrieval.

(source: RAG is Dead. Karpathy's LLM Wiki is the future  Project Explained.md)

## When RAG Still Makes Sense

- Large document collections that change frequently (re-embedding is easier than wiki maintenance)
- One-shot Q&A with no compounding value
- Teams without an agent that can maintain a wiki

## Related pages

- [[llm-wiki]]
- [[rag-is-dead-llm-wiki]]
- [[llm-agents]]
