import json
import numpy as np
from pathlib import Path

CHUNKS_FILE = Path(__file__).parent.parent / "chunks" / "chunks.jsonl"
EMBED_DIR = Path(__file__).parent.parent / "embeddings"


def run():
    from sentence_transformers import SentenceTransformer

    EMBED_DIR.mkdir(exist_ok=True)

    chunks = [json.loads(l) for l in CHUNKS_FILE.read_text().splitlines() if l.strip()]
    texts = [c["text"] for c in chunks]
    ids = [c["chunk_id"] for c in chunks]

    MODEL_NAME = "nomic-ai/nomic-embed-text-v1.5"
    print(f"Embedding {len(texts)} chunks con {MODEL_NAME}...")

    # nomic-embed richiede il prefisso task per i documenti
    prefixed = [f"search_document: {t}" for t in texts]

    model = SentenceTransformer(MODEL_NAME, trust_remote_code=True)
    embeddings = model.encode(
        prefixed,
        show_progress_bar=True,
        normalize_embeddings=True,
        batch_size=32,
    )

    np.save(EMBED_DIR / "embeddings.npy", embeddings)
    (EMBED_DIR / "index.json").write_text(
        json.dumps({"chunk_ids": ids, "model": MODEL_NAME, "dim": embeddings.shape[1]},
                   ensure_ascii=False, indent=2)
    )
    print(f"Salvati {embeddings.shape} (dim={embeddings.shape[1]}) → {EMBED_DIR}")


if __name__ == "__main__":
    run()
