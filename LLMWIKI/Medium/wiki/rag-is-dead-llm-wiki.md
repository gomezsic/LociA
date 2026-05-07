# RAG is Dead — Karpathy's LLM Wiki

**Summary**: Source article explaining why RAG's stateless retrieval cannot compound knowledge, and how Andrej Karpathy's LLM Wiki pattern (persistent markdown knowledge base maintained by an AI agent) solves this with a practical WhatsApp bot implementation.

**Sources**: `RAG is Dead. Karpathy's LLM Wiki is the future  Project Explained.md`

**Last updated**: 2026-05-07

**Tags**: `knowledge-management` `rag-alternative` `persistent-knowledge` `source-summary` `practical`

---

## The Core Problem with RAG

Every AI session starts with amnesia. [[rag|RAG]] solves retrieval but not retention: the pipeline is stateless — retrieve → stuff context → generate → forget. Knowledge never accumulates between sessions (source: RAG is Dead. Karpathy's LLM Wiki is the future  Project Explained.md).

> "RAG is a librarian who reads every book fresh each morning, with no notes from yesterday."

## Karpathy's Fix: The LLM Wiki Pattern

In April 2026, Andrej Karpathy (co-founder of OpenAI) published a [GitHub Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) proposing the [[llm-wiki]] pattern: instead of asking AI to *find* knowledge every time, ask it to *build* knowledge once and keep building it forever (source: RAG is Dead. Karpathy's LLM Wiki is the future  Project Explained.md).

## Architecture (Three Layers)

| Layer | Role |
|-------|------|
| `raw/` | Inbox — drop PDFs, articles, notes here, unorganized |
| `wiki/` | AI-maintained Wikipedia-style pages with `[[wikilinks]]` |
| Schema file (`CLAUDE.md`) | Rules for tone, structure, when to create vs update pages |

The heavy lifting happens *before* you ask anything. By query time, answers are already half-assembled. Cross-document synthesis is baked into the wiki, not a query-time miracle (source: RAG is Dead. Karpathy's LLM Wiki is the future  Project Explained.md).

## RAG vs LLM Wiki — Technical Comparison

| Dimension | RAG | LLM Wiki |
|-----------|-----|----------|
| State | Stateless (resets each session) | Persistent (grows over time) |
| Knowledge accumulation | None | Compounds with each source |
| Infrastructure | Embeddings + vector DB + retrieval layer + orchestration | A folder and a markdown file |
| Query-time work | Heavy (retrieve, rank, stuff) | Light (structured pages already exist) |
| Cross-document synthesis | At query time (expensive, lossy) | Pre-built into page links |

## Real-World Project: FreeBirdsCrew WhatsApp AI Bot

A practical implementation of the LLM Wiki concept wired into WhatsApp:

- **Stack**: Node.js + Express backend, `whatsapp-web.js` for WhatsApp, Gemini 3.0 Flash for AI, SQLite for logs, React + Vite + Tailwind dashboard
- **Brain**: A `wiki/` folder of markdown files (knowledge about the person's projects, YouTube content, mentorship resources)
- **Schema**: `SCHEMA.md` defines tone, boundaries, response style
- **Update cycle**: Edit a markdown file → bot knows something new instantly — no redeployment, no re-embedding

(source: RAG is Dead. Karpathy's LLM Wiki is the future  Project Explained.md)

## Broader Implications

The article argues AI is heading toward personal, local, persistent systems: assistants that know *you* specifically, live on *your* machine, grow quietly in the background. Compounding knowledge beats repeated retrieval every time — the same reason a senior engineer with ten years of context outperforms a brilliant graduate on day one (source: RAG is Dead. Karpathy's LLM Wiki is the future  Project Explained.md).

## Related pages

- [[llm-wiki]]
- [[rag]]
- [[llm-agents]]
