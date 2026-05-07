# LLM Wiki Pattern

**Summary**: The LLM Wiki is a pattern where an AI agent actively builds and maintains a persistent, interlinked markdown knowledge base — shifting from stateless retrieval (RAG) to compounding, structured knowledge. Proposed by Karpathy in April 2026.

**Sources**: `RAG is Dead. Karpathy's LLM Wiki is the future  Project Explained.md`, `What is LLM Wiki Pattern_ Persistent Knowledge with LLM Wikis.md`

**Last updated**: 2026-05-07

**Tags**: `knowledge-management` `persistent-knowledge` `rag-alternative` `concept` `foundational` `practical`

---

## The Core Shift: Compilation vs Retrieval

> "Most knowledge infrastructure is designed for retrieval. The wiki pattern asks: what would a diligent, tireless research assistant build over time if they never forgot anything?"

This is the fundamental reframe: from **stateless retrieval** (find relevant chunks at query time, discard them after) to **stateful compilation** (build structured knowledge once, grow it forever).

Knowledge compiled once stays compiled. Cross-document synthesis is pre-built into page links, not re-derived at query time (source: What is LLM Wiki Pattern_ Persistent Knowledge with LLM Wikis.md).

## Origin

In April 2026, Andrej Karpathy (co-founder of OpenAI) published a [GitHub Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) proposing the LLM Wiki pattern. Karpathy runs the system himself: LLM agent in one window, Obsidian in another. He watches the graph view expand. The LLM handles all the bookkeeping (source: RAG is Dead. Karpathy's LLM Wiki is the future  Project Explained.md).

## Architecture: Three Layers

| Layer | Description |
|-------|-------------|
| `raw/` | Inbox — unorganized source files (PDFs, articles, notes). Immutable. LLM reads but never modifies. |
| `wiki/` | AI-maintained Wikipedia-style pages with `[[wikilinks]]`. LLM owns this layer entirely. |
| Schema file | Markdown config (e.g. `CLAUDE.md`) defining tone, page structure, naming conventions, update rules. |

The schema turns a general-purpose LLM into a disciplined, consistent wiki editor.

## The Three Operations

### Ingest
Drop a new source → LLM reads it, discusses key takeaways, writes a summary page, updates the index, updates concept/entity pages, appends to the log. A single source may touch 10–15 wiki pages.

### Query
Ask questions against the wiki. The LLM reads the index first, drills into relevant pages, synthesizes an answer with citations. **Good answers should be filed back into the wiki** — don't let valuable synthesis disappear into chat history.

### Lint
Periodic health-check. Find: contradictions between pages, stale claims, orphan pages, concepts lacking their own page, missing cross-references.

(source: What is LLM Wiki Pattern_ Persistent Knowledge with LLM Wikis.md)

## The Two Special Files

| File | Purpose |
|------|---------|
| `index.md` | Content catalog — every page with a link and one-line summary. LLM reads this first on every query. Works well up to ~100 sources / few hundred pages. |
| `log.md` | Append-only chronological record of ingest/query/lint events. Helps LLM understand recent history without diffing every file. |

## Why LLMs Solve the Maintenance Problem

The tedious part of a knowledge base is not reading or thinking — it's bookkeeping: updating cross-references, keeping summaries current, noting contradictions. Humans abandon wikis because maintenance burden grows faster than value. LLMs don't get bored. They can touch 15 files in one pass (source: What is LLM Wiki Pattern_ Persistent Knowledge with LLM Wikis.md).

## Division of Labor

| Human | LLM |
|-------|-----|
| Curates sources | Reads and extracts concepts |
| Directs analysis | Writes and updates pages |
| Asks questions | Maintains cross-references |
| Thinks about meaning | Handles all bookkeeping |

## The Compounding Effect

Every new source gets woven into the existing network, making every previous page richer. Knowledge compounds rather than stacks — the same reason an experienced engineer with ten years of context outperforms a brilliant newcomer on day one (source: RAG is Dead. Karpathy's LLM Wiki is the future  Project Explained.md).

## Four Scales of Application

1. **Individual** — personal research compounds; stop re-deriving what you already figured out
2. **Team** — LLM maintainer keeps internal wiki evergreen by reading Slack threads, meeting transcripts, docs
3. **Research/Academic** — continuously updating meta-review across hundreds of papers
4. **Societal** — automated persistent knowledge compilation at scale (speculative, but directionally clear)

(source: What is LLM Wiki Pattern_ Persistent Knowledge with LLM Wikis.md)

## Infrastructure Comparison

| | LLM Wiki | RAG |
|-|---------|-----|
| Setup | Folder + markdown schema | Embeddings + vector DB + retrieval + orchestration |
| State | Persistent and growing | Stateless, resets each session |
| Knowledge accumulation | Compounds | None |
| Cross-doc synthesis | Pre-built | At query time |

## Practical Tooling

- **Obsidian** — live graph view, Dataview queries, Marp slides, Web Clipper for ingesting articles
- **git** — version history, rollback, collaboration; the wiki is just a git repo
- **Multimodal models** — for images: read text first, view images separately

Beyond ~100 sources, add a lightweight search layer (grep + LLM reranker) for the index.

## Historical Predecessor

The Memex (Vannevar Bush, 1945) described a personal knowledge store with associative trails. His unsolved problem was: who maintains the trails? LLMs answer that question. See [[memex]].

## Limitations

- Requires a capable, consistent LLM agent to maintain quality
- Schema design matters — a poor schema leads to inconsistent pages
- Not suited for very large, frequently-changing collections where re-embedding is simpler
- Quality depends on quality of source material
- At scale, index retrieval becomes the bottleneck (solvable with search layer)

## Related pages

- [[rag]]
- [[rag-is-dead-llm-wiki]]
- [[llm-wiki-pattern-deep-dive]]
- [[memex]]
- [[llm-agents]]
