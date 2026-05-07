# Idea: LLM Wiki + memoria efficiente (Markdown come layer di conoscenza)

**Data nota:** 2026-05-02  
**Origine:** pipeline che produce `.md` da documenti (es. Doc2MD) + integrazione di knowledge esterna.

## Intuizione centrale

Usare **documenti Markdown strutturati** come formato intermedio tra:

- sorgenti eterogenee (PDF, visure, note, API, chat),
- e ciò che un **agente** può **ricordare**, **aggiornare** e da cui **imparare** dalle esperienze.

Il Markdown è: leggibile da umani e LLM, diffabile in git, chunkabile per retrieval, facile da correggere a mano.

## Big picture: complessità `.md` + vista sintetica

L’idea non è solo accumulare file, ma **gestire documenti anche molto complessi** in Markdown e poi **vederli nel loro complesso**: una **big picture** della base di conoscenza. Una forma di vista sintetica è un’**immagine** generata a partire dalla conoscenza già presente: come un’**astrazione visiva** (es. tramite modelli che da testo/struttura producono layout o “mappe” grafiche) della rappresentazione di quella conoscenza.

## Immagine come indice multidimensionale (colore + spazio)

L’immagine funziona come **indice multidimensionale** del sapere codificato negli `.md`:

- **Posizione** dei pixel e **raggruppamenti** locali → **prossimità / coerenza** tra informazioni collegate; temi affini tendono a **vicinanza spaziale** o a **strutture cromatiche** correlate.
- **Il colore** non è decorazione: aggiunge **dimensioni** oltre allo spazio 2D (stesso punto “logico” può essere reso con tinte che codificano tipo di contenuto, certezza, dominio, versione, ecc., secondo una **legenda** concordata).

Non esiste un’unica regola universale scritta una volta per tutte: esistono **regole da definire e conoscere** sia in **fase di creazione** dell’immagine sia in **fase di interpretazione** (chi legge o chi decodifica deve condividere o recuperare quella legenda e il contesto).

## Reversibilità: traccia del processo `knowledge → immagine astratta`

La parte **critica** è **tenere traccia di come** la trasformazione **knowledge → immagine astratta** è avvenuta: parametri, legenda cromatica, modello, versione degli input, hash o riferimenti ai chunk `.md`, prompt, ordine di composizione. Solo così si può:

1. **tornare indietro** (audit, debug, aggiornamento),
2. **dall’immagine risalire a informazione utile** (almeno in modo controllato: l’immagine è compressione/astrazione; la traccia è il ponte verso il testo canonico).

In pratica: l’immagine è **vista veloce**; il grafo Markdown + metadati è **sorgente**; il **manifest di pipeline** è il contratto tra i due.

## Metafora: due ali di biblioteca, due immagini

Se un’**intera ala** (es. scienze matematiche) del “catalogo” è riassunta in **una** grande immagine e un’altra ala (es. architettura) in **una seconda**, due sezioni enormi di informazione diventano **due immagini** da consultare in modo **veloce** da leggere, da codificare (per umani o per modelli) e da tenere a mente — pur restando il dettaglio recuperabile tramite traccia e file sorgente.

## Obiettivi

1. **Ricordare:** knowledge stabile in file `.md` (o set di file) indicizzati o caricati on-demand.
2. **Aggiornare:** revisioni incrementali (patch al testo, frontmatter con `updated`, deprecazioni esplicite).
3. **Imparare dalle esperienze:** log sintetici “episodio → lezione” (es. `experiences/2026-05-02-fix-ocr.md`) che condensano errori, fix e decisioni, separati dai fatti canonici.

## Principi di efficienza (bozza)

- **Separare** *fatti / policy* da *diari di sessione* (evita rumore nel retrieval).
- **Chunk e titoli** coerenti (H2/H3 = unità di retrieval); evitare megafile monolitici dove possibile.
- **Un indice** (`INDEX.md` o manifest YAML) che punta alle pagine wiki per dominio.
- **Versioning** (git) come “memoria a lungo termine” auditabile; opzionale DB solo per metadati/query veloci.

## Legame con questo repo

Doc2MD alimenta il ramo “documenti → `.md`”; la wiki/memoria è il **consumo** di quegli artefatti + cura umana/agente per merge, deduplica e etichette.

## Estensione: immagine generatrice + modifica come informazione

Variante strategica descritta in dettaglio (e verifica di allineamento) in **`DOCUMENTO_IDEA_KNOWLEDGE_VISUALE.md`**: un’**origine** visiva fissa e snapshot successivi come **modifiche** rispetto a quell’origine, così che il **delta** (visivo e/o registrato in manifest) porti a sua volta informazione.

Illustrazione di concetto: `knowledge-origin-delta-concept.png`.

Il sistema visuale di memoria per immagini ha nome **lociA** (loci + ispirazione a Pico della Mirandola / memoria per immagini e film mentali; metafora **galleria**). Il valore operativo è nel **trio**: Markdown canonico + manifest/diff + immagine navigabile — vedi **`DOCUMENTO_IDEA_KNOWLEDGE_VISUALE.md`** §§6–7 (frase guida, MVP v0, criteri di sicurezza sul codec).

Manifesto esteso (fuzzy logic, pipeline, roadmap, agenti): **`LOCIA_MANIFESTO_KNOWLEDGE_VISUALE_FUZZY.md`**.
