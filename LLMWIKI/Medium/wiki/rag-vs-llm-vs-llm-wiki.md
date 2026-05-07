# RAG vs Plain LLM vs LLM Wiki

**Summary**: Confronto tra i tre approcci principali per dare conoscenza a un LLM: plain LLM (solo training data), RAG (retrieval at query time), e LLM Wiki (compilazione persistente). Ogni approccio risponde a una domanda diversa.

**Sources**: sintesi da `rag.md`, `llm-wiki.md`, `rag-is-dead-llm-wiki.md`

**Last updated**: 2026-05-07

**Tags**: `knowledge-management` `rag` `rag-alternative` `persistent-knowledge` `concept` `foundational`

---

## La domanda giusta da porsi

"Meglio RAG o LLM?" è una domanda incompleta perché i tre approcci **non sono in competizione diretta** — rispondono a use case diversi.

- **Plain LLM**: sa solo quello che c'è nel training
- **RAG**: sa anche quello che gli dai a query time
- **LLM Wiki**: sa quello che ha compilato nel tempo — e migliora ad ogni nuova fonte

---

## Confronto diretto

| Dimensione | Plain LLM | RAG | LLM Wiki |
|-----------|-----------|-----|----------|
| Conoscenza disponibile | Solo training data | Training + documenti recuperati | Training + wiki compilato |
| Dati privati / aggiornati | ✗ | ✓ | ✓ |
| Knowledge accumulation | ✗ | ✗ | ✓ |
| Cross-document synthesis | ✗ | Parziale (query-time) | ✓ (pre-built) |
| Riduzione allucinazioni su dominio | Bassa | Media | Alta (ancoraggio a wiki curato) |
| Infrastructure richiesta | Zero | Embeddings + vector DB + retrieval | Cartella markdown + schema |
| Costo per query | Basso | Medio (retrieval + generation) | Basso (pagine già strutturate) |
| Curva di setup | Zero | Alta | Media |
| Adatto per | Q&A generali | Lookup su corpus fisso | Knowledge che cresce nel tempo |

---

## Quando usare ciascuno

**Plain LLM**
- Task generici non ancorati a documenti specifici
- Brainstorming, scrittura, coding su pattern standard
- Quando la velocità di setup conta più della precisione documentale

**RAG**
- Corpus di documenti fisso e ben definito (manuale prodotto, FAQ, policy)
- Domande one-shot senza bisogno di sintesi cross-documento
- Team senza un workflow per mantenere un wiki
- Documenti che cambiano spesso (re-embedding è più semplice che aggiornare il wiki)

**LLM Wiki**
- Conoscenza che si accumula nel tempo (ricerca, note personali, knowledge base aziendale)
- Domande che richiedono sintesi tra più fonti
- Situazioni dove re-derivare le stesse conclusioni ogni volta è uno spreco
- Quando il valore sta nelle *connessioni* tra concetti, non solo nei documenti

---

## L'intuizione chiave

> RAG è un bibliotecario che ogni mattina rilegge tutti i libri da zero.
> L'LLM Wiki è un bibliotecario che prende appunti, li aggiorna e costruisce un indice ogni volta che arriva un nuovo libro.

RAG risolve il problema del *retrieval*. L'LLM Wiki risolve il problema dell'*accumulo*. Sono risposte a domande diverse — e in molti casi la scelta giusta è partire con RAG e migrare a LLM Wiki quando la conoscenza inizia a compoundare.

---

## Related pages

- [[rag]]
- [[llm-wiki]]
- [[rag-is-dead-llm-wiki]]
- [[llm-wiki-pattern-deep-dive]]
