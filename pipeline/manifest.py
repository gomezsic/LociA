import json
import numpy as np
from pathlib import Path
from datetime import date

EMBED_DIR = Path(__file__).parent.parent / "embeddings"
CHUNKS_FILE = Path(__file__).parent.parent / "chunks" / "chunks.jsonl"
MANIFESTS_DIR = Path(__file__).parent.parent / "manifests"
PUBLIC_MANIFESTS = Path(__file__).parent.parent / "public" / "manifests"


def run():
    MANIFESTS_DIR.mkdir(exist_ok=True)
    PUBLIC_MANIFESTS.mkdir(parents=True, exist_ok=True)

    coords = np.load(EMBED_DIR / "coords_2d.npy")
    labels = np.load(EMBED_DIR / "labels.npy").astype(int)
    index = json.loads((EMBED_DIR / "index.json").read_text())
    chunks = [json.loads(l) for l in CHUNKS_FILE.read_text().splitlines() if l.strip()]
    chunk_map = {c["chunk_id"]: c for c in chunks}

    soft_path = EMBED_DIR / "soft_membership.npy"
    soft = np.load(soft_path) if soft_path.exists() else None

    entries = []
    for i, cid in enumerate(index["chunk_ids"]):
        c = chunk_map.get(cid, {})

        membership = {}
        if soft is not None:
            row = soft[i]
            for k, v in enumerate(row):
                if v > 0.05:
                    membership[str(k)] = round(float(v), 4)

        entries.append({
            "chunk_id": cid,
            "coords": [round(float(coords[i, 0]), 4), round(float(coords[i, 1]), 4)],
            "pixel": [int(coords[i, 0] * 4095), int((1 - coords[i, 1]) * 4095)],
            "cluster_id": int(labels[i]),
            "cluster_membership": membership,
            "source_file": c.get("source_file", ""),
            "heading_path": c.get("heading_path", []),
            "token_count": c.get("tokens", 0),
            "status": c.get("status", "canonical"),
            "text_preview": c.get("text", "")[:200],
        })

    manifest = {
        "lociA_version": "0.2",
        "snapshot_id": "snapshot_001",
        "date": str(date.today()),
        "embedding_model": index.get("model", "nomic-ai/nomic-embed-text-v1.5"),
        "embedding_dim": int(index.get("dim", 768)),
        "projection_model": "pacmap",
        "canvas_size": [4096, 4096],
        "origin_image": "maps/origin.png",
        "snapshot_image": "maps/snapshot_001.png",
        "codec": {
            "color_scheme": "cluster_hue_v1",
            "layout_strategy": "pacmap_hdbscan_soft",
        },
        "chunks": entries,
    }

    out = MANIFESTS_DIR / "manifest_001.json"
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
    # Copia in public/ per il viewer React
    (PUBLIC_MANIFESTS / "manifest_001.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
    print(f"Manifest salvato: {len(entries)} chunks → {out}")


if __name__ == "__main__":
    run()
