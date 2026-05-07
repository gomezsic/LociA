"""
Converte i file in corpus/raw/ in wiki .md canonici per lociA.
  - .md  → strip frontmatter clipping, aggiungi frontmatter lociA
  - .png/.jpg/.jpeg → Claude Vision → descrizione strutturata → wiki .md
  - .pdf → estrazione testo → wiki .md
Output: corpus/wiki_<slug>.md
"""

import re
import base64
import os
from pathlib import Path
from datetime import date

import anthropic

RAW_DIR = Path(__file__).parent.parent / "corpus" / "raw"
CORPUS_DIR = Path(__file__).parent.parent / "corpus"

client = anthropic.Anthropic()


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "_", text)
    return text[:60].strip("_")


def infer_domain_tags(text: str) -> list[str]:
    keywords = {
        "embedding": "embeddings",
        "vector": "vector_search",
        "qdrant": "vector_search",
        "umap": "dimensionality_reduction",
        "clip": "multimodal",
        "multimodal": "multimodal",
        "image search": "image_search",
        "semantic": "semantic_search",
        "wiki": "knowledge_management",
        "memory": "knowledge_management",
        "llm": "llm",
        "pixel": "computer_vision",
        "mappa": "locia",
        "fuzzy": "locia",
    }
    found = set()
    low = text.lower()
    for kw, tag in keywords.items():
        if kw in low:
            found.add(tag)
    return sorted(found)


def strip_clipping_frontmatter(text: str) -> tuple[dict, str]:
    meta = {}
    body = text
    m = re.match(r"^---\n(.+?)\n---\n", text, re.DOTALL)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, _, v = line.partition(":")
                meta[k.strip()] = v.strip().strip('"')
        body = text[m.end():]
    # Rimuovi immagini esterne (link miro.medium, cdn, ecc.)
    body = re.sub(r"!\[.*?\]\(https?://[^\)]+\)", "", body)
    # Rimuovi link vuoti
    body = re.sub(r"\n{3,}", "\n\n", body)
    return meta, body.strip()


def process_md(path: Path) -> Path:
    raw = path.read_text(encoding="utf-8")
    meta, body = strip_clipping_frontmatter(raw)

    title = meta.get("title", path.stem)
    source = meta.get("source", "")
    published = meta.get("published", "")
    tags = infer_domain_tags(body)

    frontmatter = f"""---
id: "{slugify(title)}"
title: "{title}"
domain: "vector_search"
type: "reference_article"
status: "canonical"
created: "{date.today()}"
source: "{source}"
published: "{published}"
tags:
{chr(10).join(f'  - {t}' for t in tags)}
---

"""
    out_name = f"wiki_{slugify(title)}.md"
    out_path = CORPUS_DIR / out_name
    out_path.write_text(frontmatter + body, encoding="utf-8")
    print(f"  ✓ {path.name} → {out_name}")
    return out_path


def process_image(path: Path) -> Path:
    print(f"  Claude Vision: {path.name}…")
    img_data = base64.standard_b64encode(path.read_bytes()).decode()
    ext = path.suffix.lower().lstrip(".")
    media_type = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg"}.get(ext, "image/png")

    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=2000,
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {"type": "base64", "media_type": media_type, "data": img_data},
                },
                {
                    "type": "text",
                    "text": (
                        "Sei un assistente che converte immagini in documentazione wiki Markdown.\n"
                        "Analizza questa immagine nel dettaglio e produci un documento wiki strutturato con:\n"
                        "- Un titolo H1 descrittivo\n"
                        "- Sezioni H2 per ogni concetto principale presente nell'immagine\n"
                        "- Descrizione tecnica precisa di ogni elemento, schema, diagramma o testo visibile\n"
                        "- Se ci sono frecce, pipeline, flussi: descrivili step by step\n"
                        "- Se ci sono termini tecnici: spiegali brevemente\n"
                        "Scrivi solo il corpo Markdown, senza frontmatter. Lingua: italiano se il contenuto è italiano, inglese altrimenti."
                    ),
                },
            ],
        }],
    )

    body = response.content[0].text
    title_match = re.search(r"^# (.+)", body, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else path.stem
    tags = infer_domain_tags(body)

    frontmatter = f"""---
id: "{slugify(title)}"
title: "{title}"
domain: "vector_search"
type: "image_wiki"
status: "canonical"
created: "{date.today()}"
source_image: "corpus/raw/{path.name}"
tags:
{chr(10).join(f'  - {t}' for t in tags)}
---

"""
    out_name = f"wiki_{slugify(title)}.md"
    out_path = CORPUS_DIR / out_name
    out_path.write_text(frontmatter + body, encoding="utf-8")
    print(f"  ✓ {path.name} → {out_name}")
    return out_path


def process_pdf(path: Path) -> Path:
    import fitz  # pymupdf
    doc = fitz.open(str(path))
    pages_text = [page.get_text() for page in doc]
    body = "\n\n".join(pages_text).strip()
    title = path.stem
    tags = infer_domain_tags(body)

    frontmatter = f"""---
id: "{slugify(title)}"
title: "{title}"
domain: "reference"
type: "pdf_extract"
status: "canonical"
created: "{date.today()}"
source_file: "corpus/raw/{path.name}"
tags:
{chr(10).join(f'  - {t}' for t in tags)}
---

"""
    # Struttura base: titolo H1 + testo
    body_md = f"# {title}\n\n{body}"
    out_name = f"wiki_{slugify(title)}.md"
    out_path = CORPUS_DIR / out_name
    out_path.write_text(frontmatter + body_md, encoding="utf-8")
    print(f"  ✓ {path.name} → {out_name}")
    return out_path


def run():
    files = sorted(RAW_DIR.iterdir())
    print(f"File in raw/: {len(files)}\n")
    for f in files:
        if f.suffix.lower() == ".md":
            process_md(f)
        elif f.suffix.lower() in (".png", ".jpg", ".jpeg"):
            process_image(f)
        elif f.suffix.lower() == ".pdf":
            process_pdf(f)
        else:
            print(f"  skip: {f.name}")
    print("\nProcessing completato.")


if __name__ == "__main__":
    run()
