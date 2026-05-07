# Wiki Log

Append-only record of all operations. Never delete entries.

---

## 2026-05-07 (query → wiki)

**Action**: Risposta a query "Meglio RAG o LLM?" salvata come pagina wiki

**Page created**: `rag-vs-llm-vs-llm-wiki.md` — confronto plain LLM vs RAG vs LLM Wiki con tabella, quando usare ciascuno, intuizione chiave

---

## 2026-05-07 (lint)

**Action**: Full wiki audit — 5 issues found, all resolved

**Findings and fixes**:
1. **Contradiction** — `rag.md`: "Nuanced questions → Degrades" → corretto in "No improvement over time" (le fonti dicono stateless, non deterioramento attivo)
2. **Contradiction** — `reinforcement-learning.md` Summary: "largely superseded" contraddiceva il body della stessa pagina → riformulato per includere il ruolo di RL in RLHF/DPO/PPO
3. **Orphan** — `openclaw.md` non aveva link in entrata → aggiunto link e punti 5-6 in `llm-agents.md` (resource budgeting, human oversight)
4. **Uncited claim** — `memex.md`: "Ted Nelson's Project Xanadu" non attestato da nessuna fonte → rimosso dalla lista, aggiunta nota "needs verification"
5. **Uncited claim** — `reinforcement-learning.md`: "RLHF, DPO, PPO" senza source → aggiunta nota "needs verification"

**Concepts flagged as needing future pages** (quando arriveranno fonti):
- Plausible Reasoning (in glossary ma senza pagina dedicata)
- RLHF / DPO / PPO / alignment techniques
- Tool use / tool calling

---

## 2026-05-07 (second ingest)

**Action**: Ingested 2 new Medium articles; updated existing pages; added semantic tags across all wiki pages

**Sources**:
- `What is LLM Wiki Pattern_ Persistent Knowledge with LLM Wikis.md`
- `Navigating the World of Openclaw_ The Pros and Cons of This AI Tool.md`

**Pages created** (3):
- `llm-wiki-pattern-deep-dive.md` — compilation vs retrieval, three operations, four scales, Memex, tooling
- `memex.md` — Vannevar Bush's Memex (1945) as historical predecessor to LLM Wiki
- `openclaw.md` — OpenClaw AI automation tool: benefits, resource risks, oversight lessons

**Pages updated** (2):
- `llm-wiki.md` — major expansion: compilation framing, three operations (Ingest/Query/Lint), four scales, division of labor table, Memex reference, practical tooling, scaling guidance
- `index.md` — added tag column to all tables, added tag taxonomy section, added Memex + new source pages, expanded glossary to 9 terms

**Tags added**: Semantic tags (`type`, `topic`, `depth`) added to all 12 wiki pages. Tag taxonomy documented in index.md.

**Key connections discovered**:
- LLM Wiki ↔ Memex (1945): same vision, different era — Karpathy's pattern finally answers Bush's unsolved maintenance problem
- OpenClaw ↔ LLM Agents: resource budgeting and human oversight are universal challenges for autonomous agents, not tool-specific
- LLM Wiki three operations (Ingest/Query/Lint) directly map to how this wiki itself operates

---

## 2026-05-07

**Action**: Ingested 3 new Medium articles
**Sources**:
- `LangChain Just Released Deep Agents — And It Changes How You Build AI Systems.md`
- `RAG is Dead. Karpathy's LLM Wiki is the future  Project Explained.md`
- `From Hardcoded Tools to Reinforcement Learning to LLM Agents_ The Evolution of AI Systems.md`

**Pages created** (9 total):

*Source summaries:*
- `langchain-deep-agents.md` — deepagents library overview
- `rag-is-dead-llm-wiki.md` — RAG vs LLM Wiki article + WhatsApp bot project
- `ai-systems-evolution.md` — three waves of AI systems article

*Concept pages:*
- `llm-agents.md` — what agents are, the agent loop, LLM-specific properties
- `rag.md` — RAG explained, limitations, comparison with LLM Wiki
- `llm-wiki.md` — Karpathy's LLM Wiki pattern
- `langchain-ecosystem.md` — LangChain / LangGraph / deepagents stack
- `context-window-management.md` — strategies for managing context limits
- `reinforcement-learning.md` — RL as second wave of AI evolution

**Index updated**: Added new "Knowledge & Memory Systems" section; populated Agentic AI, ML Libraries, Reinforcement Learning sections; added 6 glossary terms.

---

## 2026-05-06

**Action**: Wiki initialized
**Changed**: Created `wiki/index.md` with 10 topic categories, created `wiki/log.md`
**Notes**: No articles ingested yet. Ready to receive first Medium articles in `raw/`.
