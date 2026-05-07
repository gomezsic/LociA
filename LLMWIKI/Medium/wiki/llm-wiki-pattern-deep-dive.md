# LLM Wiki Pattern — Deep Dive

**Summary**: Second deep-dive article on the LLM Wiki pattern, adding the "compilation vs retrieval" framing, three core operations (Ingest/Query/Lint), four scales of application, historical connection to Vannevar Bush's Memex, and practical tooling guidance.

**Sources**: `What is LLM Wiki Pattern_ Persistent Knowledge with LLM Wikis.md`

**Last updated**: 2026-05-07

**Tags**: `knowledge-management` `persistent-knowledge` `llm-wiki` `rag-alternative` `source-summary` `practical` `historical`

---

## The Core Reframe: Compilation vs Retrieval

> "Most of our knowledge infrastructure is designed for retrieval, not accumulation. Search engines retrieve. RAG retrieves. Even memory-augmented LLMs retrieve. They all ask: *What documents are relevant to this query?*"
>
> "The wiki pattern asks: *What would a diligent, tireless research assistant build over time if they never forgot anything?*"

The shift is from **stateless retrieval** to **stateful compilation**. Knowledge gets compiled once, then stays compiled and grows (source: What is LLM Wiki Pattern_ Persistent Knowledge with LLM Wikis.md).

## Karpathy's Personal Practice

Karpathy keeps an LLM agent open in one window and Obsidian open in another. The LLM makes edits as he discusses material. He watches the graph view expand. He clicks through links. He reads updated pages as they appear.

- Human role: supplies sources and questions
- LLM role: summarizing, cross-referencing, filing, bookkeeping
- Obsidian = IDE; LLM = programmer; wiki = codebase

(source: What is LLM Wiki Pattern_ Persistent Knowledge with LLM Wikis.md)

## Why Maintenance Is the Hard Part (and Why LLMs Solve It)

The tedious part of maintaining a knowledge base is not the reading or thinking — it's the bookkeeping: updating cross-references, keeping summaries current, noting contradictions, maintaining consistency across dozens of pages. Humans abandon wikis because maintenance burden grows faster than value. LLMs don't get bored. They can touch 15 files in one pass (source: What is LLM Wiki Pattern_ Persistent Knowledge with LLM Wikis.md).

## The Three Operations

### 1. Ingest

Drop a new source → the LLM reads it, discusses key takeaways, writes a summary page, updates the index, updates relevant entity and concept pages, appends to the log. A single source may touch 10–15 wiki pages.

Best practice: ingest one source at a time and stay involved — read the summaries, check the updates, guide emphasis.

### 2. Query

Ask questions against the wiki. The LLM reads relevant pages and synthesizes an answer with citations.

**Key practice**: good answers should be filed back into the wiki as new pages (comparisons, analyses, discovered connections). Don't let valuable synthesis disappear into chat history.

### 3. Lint

Periodic health-check. Ask the LLM to look for:
- Contradictions between pages
- Stale claims superseded by newer sources
- Orphan pages (no inbound links)
- Concepts mentioned but lacking their own page
- Missing cross-references

The LLM is also good at suggesting new questions to investigate and new sources to find.

(source: What is LLM Wiki Pattern_ Persistent Knowledge with LLM Wikis.md)

## The Two Special Files

| File | Purpose |
|------|---------|
| `index.md` | Content-oriented catalog: every page with a link + one-line summary. LLM reads this first on every query to find relevant pages. Works well up to ~100 sources / few hundred pages. |
| `log.md` | Chronological, append-only. Records Ingest / Query / Lint events. Helps the LLM understand what's been done recently without diffing every file. |

## Four Scales of Application

### 1. Individual Scale
Knowledge compounds — every source added, every question asked, makes the wiki richer not just bigger. Stop re-deriving what you already figured out.

### 2. Team Scale
LLM maintainer keeps the wiki evergreen by reading every Slack thread, meeting transcript, design doc, and updating relevant pages automatically. Eliminates the "maintenance tax" that kills internal wikis.

### 3. Research / Academic Scale
Continuously updating meta-review across hundreds of papers. LLM reads new papers, updates synthesis, flags contradictions, highlights where new evidence challenges old claims.

### 4. Societal Scale (in principle)
Automated, persistent knowledge compilation at civilizational scale — every news article, scientific preprint, public dataset feeding a wiki that compiles rather than indexes. A living, cross-referenced map of what we know, what we don't know, and where we disagree.

(source: What is LLM Wiki Pattern_ Persistent Knowledge with LLM Wikis.md)

## Practical Tooling

| Tool | Role |
|------|------|
| **Obsidian** | Primary editor; graph view shows wiki shape; supports Dataview, Marp, Excalidraw plugins |
| **Obsidian Web Clipper** | Converts web articles to markdown + downloads images locally |
| **Dataview** | Runs queries over YAML frontmatter; generates dynamic tables/lists |
| **Marp** | Generates presentations directly from wiki markdown |
| **git** | Version history, branching, collaboration — the wiki is just a git repo |

For images: LLM reads markdown text first, views referenced images separately via multimodal models (GPT-4o, Claude, Gemini). For PDFs: convert to markdown with `marker` or `pypdf` before ingesting.

## Scaling the Index Beyond ~100 Sources

The index file works well up to a few hundred pages and ~100 sources. Beyond that, add a lightweight search layer (e.g., `grep` + LLM reranker). The pattern itself scales; the bottleneck is page retrieval, not wiki size.

## Historical Connection: Vannevar Bush's Memex (1945)

Bush described the Memex in 1945 — a personal, curated knowledge store with associative trails between documents. His vision was closer to the LLM Wiki than to what the web became: private, actively curated, with connections between documents as valuable as the documents themselves.

The part he couldn't solve: who does the maintenance? Now we know.

See [[memex]] for more.

(source: What is LLM Wiki Pattern_ Persistent Knowledge with LLM Wikis.md)

## Division of Labor

| Human | LLM |
|-------|-----|
| Curates sources | Reads and extracts concepts |
| Directs analysis | Writes and updates wiki pages |
| Asks good questions | Maintains cross-references |
| Thinks about meaning | Handles all bookkeeping |

## Related pages

- [[llm-wiki]]
- [[rag-is-dead-llm-wiki]]
- [[rag]]
- [[memex]]
- [[llm-agents]]
