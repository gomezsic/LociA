import json
import re
import hashlib
from pathlib import Path

PDF_CHUNK_PAGES = 3   # quante pagine per chunk PDF (finestra scorrevole)

ROOT = Path(__file__).parent.parent
CORPUS_DIR = ROOT / "corpus"
CHUNKS_DIR = ROOT / "chunks"

# Tutte le directory che contengono .md da embeddare
SOURCE_DIRS = [
    CORPUS_DIR,
    ROOT / "LLMWIKI" / "Medium" / "wiki",
]

# File da ignorare
SKIP_FILES = {"index.md", "log.md", "CLAUDE.md", "Benvenuto.md", "crea un collegamento.md"}


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "_", text)
    return text[:60]


def split_markdown(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    chunks = []
    current_h1 = ""
    current_h2 = ""
    current_h3 = ""
    current_lines: list[str] = []
    heading_path: list[str] = []

    def flush(hp: list[str]):
        content = "\n".join(current_lines).strip()
        if not content or len(content) < 30:
            return
        h_slug = slugify("_".join(hp)) if hp else "intro"
        uid = hashlib.md5((str(path) + h_slug + content[:80]).encode()).hexdigest()[:8]
        chunk_id = f"{path.stem}__{h_slug}__{uid}"
        chunks.append({
            "chunk_id": chunk_id,
            "source_file": f"corpus/{path.name}",
            "heading_path": list(hp),
            "text": content,
            "tokens": len(content.split()),
            "status": "canonical",
        })

    for line in lines:
        m1 = re.match(r"^# (.+)", line)
        m2 = re.match(r"^## (.+)", line)
        m3 = re.match(r"^### (.+)", line)

        if m1:
            flush(heading_path)
            current_lines = []
            current_h1 = m1.group(1).strip()
            current_h2 = ""
            current_h3 = ""
            heading_path = [current_h1]
        elif m2:
            flush(heading_path)
            current_lines = []
            current_h2 = m2.group(1).strip()
            current_h3 = ""
            heading_path = [x for x in [current_h1, current_h2] if x]
        elif m3:
            flush(heading_path)
            current_lines = []
            current_h3 = m3.group(1).strip()
            heading_path = [x for x in [current_h1, current_h2, current_h3] if x]
        else:
            current_lines.append(line)

    flush(heading_path)
    return chunks


def split_pdf(path: Path) -> list[dict]:
    """Estrae testo dal PDF e lo chunka a finestre di PDF_CHUNK_PAGES pagine."""
    try:
        import fitz  # PyMuPDF
    except ImportError:
        print(f"  [skip PDF] PyMuPDF non installato: {path.name}")
        return []

    doc = fitz.open(str(path))
    pages_text = []
    for page in doc:
        text = page.get_text().strip()
        if text:
            pages_text.append(text)
    doc.close()

    if not pages_text:
        return []

    chunks = []
    step = max(1, PDF_CHUNK_PAGES)
    for i in range(0, len(pages_text), step):
        window = pages_text[i:i + step]
        content = "\n\n".join(window).strip()
        if len(content) < 60:
            continue
        page_range = f"pp.{i+1}-{min(i+step, len(pages_text))}"
        heading_path = [path.stem, page_range]
        h_slug = slugify(f"{path.stem}_{page_range}")
        uid = hashlib.md5((str(path) + h_slug + content[:80]).encode()).hexdigest()[:8]
        chunks.append({
            "chunk_id": f"{path.stem}__{h_slug}__{uid}",
            "source_file": f"corpus/{path.name}",
            "heading_path": heading_path,
            "text": content[:2000],   # tronca chunk molto lunghi
            "tokens": len(content.split()),
            "status": "canonical",
            "domain": "sailing",
        })
    return chunks


def run():
    CHUNKS_DIR.mkdir(exist_ok=True)
    all_chunks = []
    for src_dir in SOURCE_DIRS:
        if not src_dir.exists():
            print(f"  [skip] {src_dir} non trovata")
            continue
        print(f"\n[{src_dir.relative_to(ROOT)}]")
        for f in sorted(src_dir.iterdir()):
            if f.is_dir():
                continue
            if f.suffix.lower() == ".md":
                if f.name in SKIP_FILES:
                    continue
                chunks = split_markdown(f)
            elif f.suffix.lower() == ".pdf":
                chunks = split_pdf(f)
            else:
                continue
            all_chunks.extend(chunks)
            print(f"  {f.name}: {len(chunks)} chunks")

    out = CHUNKS_DIR / "chunks.jsonl"
    with out.open("w", encoding="utf-8") as f:
        for c in all_chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    print(f"\nTotale: {len(all_chunks)} chunks → {out}")
    return all_chunks


if __name__ == "__main__":
    run()
