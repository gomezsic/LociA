# CLAUDE.md — lociA

## Cos'è questo progetto

**lociA** è un sistema di memoria visuale per LLM Wiki.

Trasforma una knowledge base di file Markdown in uno **spazio cognitivo navigabile**: ogni chunk di testo viene proiettato in uno spazio 2D, colorato per dominio, raggruppato per vicinanza semantica. L'immagine prodotta non è decorazione — è un indice spaziale e fuzzy sopra la wiki testuale.

Formula: `Markdown canonico + manifest tracciabile + mappa fuzzy spaziale + delta incrementale`

La knowledge base testuale resta la fonte di verità. La mappa visuale è la superficie navigabile. Il manifest è il contratto tra i due. Il delta è la memoria evolutiva.

---

## Stack

### Frontend / Viewer
- React 18 + Vite 5 + TypeScript 5
- Viewer interattivo della mappa: click su zona → mostra chunk Markdown collegato
- Canvas API o SVG per rendering mappa
- Nessuna dipendenza UI pesante — componenti custom, zero librerie UI opinionated

### Pipeline (Python)
- Python 3.11+
- `sentence-transformers` — embedding locali, no API cost
- `umap-learn` — riduzione dimensionale a 2D
- `hdbscan` — clustering semantico
- `matplotlib` / `Pillow` — rendering PNG/SVG
- Pipeline pura: nessun framework, script Python diretti

### Storage / File system
- Tutto su filesystem locale, versionato in git
- Nessun database esterno nell'MVP
- Struttura canonica:

```
lociA/
  corpus/           ← file .md sorgente (la wiki)
  chunks/           ← chunks.jsonl (ID, testo, fonte, heading_path)
  embeddings/       ← embeddings.npy + index.json
  maps/             ← origin.png, snapshot_001.svg
  manifests/        ← manifest_001.json
  deltas/           ← delta_001.yaml
  wiki/             ← documentazione tecnica del progetto in .md
  pipeline/         ← script Python (ingest, embed, project, render, manifest)
  src/              ← React viewer
```

---

## Architettura pipeline

### Step 1 — Ingest (`pipeline/ingest.py`)
- Legge ogni `.md` in `corpus/`
- Split per heading H2/H3 → ogni sezione è un chunk
- Output: `chunks/chunks.jsonl`
- Schema chunk:
```json
{
  "chunk_id": "filename__h2_slug__001",
  "source_file": "corpus/file.md",
  "heading_path": ["H1 title", "H2 section"],
  "text": "...",
  "tokens": 0,
  "status": "canonical"
}
```

### Step 2 — Embed (`pipeline/embed.py`)
- Modello: `all-MiniLM-L6-v2` (leggero, buona qualità semantica)
- Output: `embeddings/embeddings.npy` + `embeddings/index.json` (chunk_id → row index)

### Step 3 — Project (`pipeline/project.py`)
- UMAP 2D su embeddings
- Output: `embeddings/coords_2d.npy` (x, y normalizzati 0-1)

### Step 4 — Cluster (`pipeline/cluster.py`)
- HDBSCAN su coords 2D (o su embeddings originali)
- Output: `embeddings/labels.npy` (cluster ID per chunk)

### Step 5 — Render (`pipeline/render.py`)
- `origin.png`: griglia neutra 2000×2000, macro-zone vuote
- `snapshot_001.svg`: chunk come punti colorati per cluster, con label testuale delle zone
- Palette colori per cluster assegnata deterministicamente (HSV equidistante)

### Step 6 — Manifest (`pipeline/manifest.py`)
- Output: `manifests/manifest_001.json`
- Schema:
```json
{
  "lociA_version": "0.1",
  "snapshot_id": "snapshot_001",
  "origin_image": "maps/origin.png",
  "codec": {
    "color_scheme": "cluster_hue_v1",
    "layout_strategy": "umap_2d_hdbscan"
  },
  "chunks": [
    {
      "chunk_id": "...",
      "coords": [0.42, 0.71],
      "cluster_id": 2,
      "source_file": "corpus/...",
      "heading_path": ["..."]
    }
  ]
}
```

### Step 7 — Delta (`pipeline/delta.py`)
- Confronto manifest precedente vs attuale
- Output: `deltas/delta_001.yaml`
- Tipi di evento: `new_chunk`, `moved_chunk`, `new_cluster`, `cluster_intensity_change`, `deprecated_chunk`

---

## Viewer React

Il viewer carica `manifest_001.json` e `snapshot_001.svg`.

Funzioni minime MVP:
- Mostra la mappa SVG
- Click su punto → sidebar con testo del chunk e link al file sorgente
- Hover → tooltip con heading_path
- Filtro per cluster (colore)
- Nessun routing per ora — single page

File chiave:
- `src/App.tsx` — root
- `src/components/MapViewer.tsx` — SVG interattivo
- `src/components/ChunkPanel.tsx` — sidebar con testo chunk
- `src/hooks/useManifest.ts` — carica manifest.json

---

## Regole di codifica

### Generale
- Zero commenti sul COSA fa il codice — i nomi parlano da soli
- Commenta solo il PERCHÉ quando non è ovvio (vincolo nascosto, workaround specifico)
- Nessuna astrazione prematura: tre funzioni simili sono meglio di un'astrazione inutile
- Nessun error handling per scenari impossibili — fidati delle garanzie del framework
- Nessuna feature aggiuntiva rispetto a quanto richiesto
- Nessun file di documentazione aggiuntivo a meno che esplicitamente richiesto

### Python pipeline
- Script autonomi, eseguibili direttamente: `python pipeline/ingest.py`
- Nessun framework (FastAPI, Django, ecc.) nell'MVP
- Dipendenze minimali: solo quelle elencate sopra
- Output sempre su filesystem con path relativi alla root del progetto
- Ogni script accetta argomenti via `argparse` ma ha default ragionevoli

### TypeScript / React
- Componenti funzionali, nessuna classe
- Tipi espliciti — no `any`
- `useManifest` carica il JSON con fetch da `/public/manifests/manifest_001.json`
- I file di dati (manifest, SVG) vengono messi in `public/` per essere serviti da Vite

### Git
- Commit atomici per step pipeline o per componente
- Nessun commit con `node_modules`, `__pycache__`, `.npy`, `.png` pesanti
- `.gitignore` include: `node_modules/`, `__pycache__/`, `*.npy`, `embeddings/`, `dist/`

---

## LLM Wiki del progetto — file `.md` in `wiki/`

Ogni decisione tecnica non ovvia, ogni schema dati, ogni scelta di design va documentata in `wiki/` come file Markdown con frontmatter. Questo è il corpus che lociA userà per mappare se stesso (meta-prototipo).

### Schema frontmatter standard
```yaml
---
id: "dominio_topic_slug"
title: "Titolo leggibile"
domain: "locia"
type: "decision|protocol|schema|reference"
status: "canonical|draft|deprecated"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
tags:
  - locia
  - pipeline
---
```

### File wiki da creare progressivamente
- `wiki/architecture.md` — architettura generale, scelte stack
- `wiki/pipeline.md` — step-by-step pipeline con esempi I/O
- `wiki/chunk_schema.md` — schema canonico del chunk
- `wiki/manifest_schema.md` — schema manifest con esempi
- `wiki/delta_schema.md` — tipi di evento delta con esempi YAML
- `wiki/codec.md` — legenda colori, forme, intensità
- `wiki/viewer.md` — spec del viewer React

---

## Corpus iniziale

Il primo corpus è la documentazione di lociA stessa (meta-prototipo):
- `corpus/IDEA_LLM_WIKI_MEMORIA.md` — copia da `/Users/giacomofelicesiccardi/Python/Memory/`
- `corpus/DOCUMENTO_IDEA_KNOWLEDGE_VISUALE.md` — copia da stesso path
- `corpus/LOCIA_MANIFESTO_KNOWLEDGE_VISUALE_FUZZY.md` — copia da stesso path

Questo permette al sistema di mappare se stesso al primo run.

---

## Criterio di successo MVP

Il MVP funziona se l'utente può:
1. Eseguire `python pipeline/run_all.py` e ottenere `maps/snapshot_001.svg` + `manifests/manifest_001.json`
2. Aprire il viewer React (`npm run dev`)
3. Vedere la mappa con punti colorati per cluster
4. Cliccare un punto e leggere il chunk Markdown collegato
5. Riconoscere macro-aree corrispondenti ai 3 documenti sorgente

---

## Stato progetto (inizializzato 2026-05-07)

- [x] Scaffold React+Vite+TS creato
- [x] Git init + remote GitHub configurato (`https://github.com/gomezsic/lociA.git`)
- [ ] Corpus copiato in `corpus/`
- [ ] Pipeline Python scritta (ingest → embed → project → cluster → render → manifest)
- [ ] Viewer React implementato (MapViewer + ChunkPanel)
- [ ] Primo run end-to-end
- [ ] Push su GitHub (repo da creare su github.com)

---

## Note operative

**Per pushare su GitHub:** il repo `gomezsic/lociA` va creato manualmente su [github.com/new](https://github.com/new) (nome: `lociA`, public), poi:
```bash
cd ~/Claude_progetti/lociA
git push -u origin main
```

**Per avviare il viewer:**
```bash
cd ~/Claude_progetti/lociA
npm run dev
```

**Per eseguire la pipeline completa:**
```bash
cd ~/Claude_progetti/lociA
python pipeline/run_all.py
```
