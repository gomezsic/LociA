import json
import numpy as np
from pathlib import Path

EMBED_DIR = Path(__file__).parent.parent / "embeddings"
MAPS_DIR = Path(__file__).parent.parent / "maps"
CHUNKS_FILE = Path(__file__).parent.parent / "chunks" / "chunks.jsonl"


def build_label_list(labels: np.ndarray, chunks: list[dict], index: dict) -> list[str]:
    """Costruisce etichette per ogni punto: ultimo heading significativo."""
    chunk_map = {c["chunk_id"]: c for c in chunks}
    result = []
    for cid in index["chunk_ids"]:
        c = chunk_map.get(cid, {})
        hp = c.get("heading_path", [])
        label = hp[-1] if hp else cid[:30]
        result.append(label[:50])
    return result


def run():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    MAPS_DIR.mkdir(exist_ok=True)

    coords = np.load(EMBED_DIR / "coords_2d.npy")
    labels = np.load(EMBED_DIR / "labels.npy").astype(int)
    index = json.loads((EMBED_DIR / "index.json").read_text())
    chunks = [json.loads(l) for l in CHUNKS_FILE.read_text().splitlines() if l.strip()]
    point_labels = build_label_list(labels, chunks, index)

    # --- origin.png: canvas neutro ---
    fig, ax = plt.subplots(figsize=(14, 10), dpi=120)
    ax.set_facecolor("#f5f4f0")
    fig.patch.set_facecolor("#f5f4f0")
    for x in np.linspace(0, 1, 14):
        ax.axvline(x, color="#deddd8", linewidth=0.4)
    for y in np.linspace(0, 1, 10):
        ax.axhline(y, color="#deddd8", linewidth=0.4)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("lociA — origin canvas", fontsize=11, color="#aaa", pad=10)
    plt.tight_layout()
    plt.savefig(MAPS_DIR / "origin.png", dpi=120, bbox_inches="tight")
    plt.close()
    print("origin.png salvato")

    # --- snapshot con DataMapPlot ---
    try:
        import datamapplot

        # Mappa cluster_id → nome leggibile
        n_clusters = int(labels.max()) + 1
        cluster_names = np.array([f"Cluster {i}" for i in range(n_clusters)])
        label_names = cluster_names[labels]

        fig, ax = datamapplot.create_plot(
            coords,
            labels=label_names,
            label_font_size=11,
            point_size=5,
            label_wrap_width=16,
            dynamic_label_size=True,
            add_glow=True,
            darkmode=False,
            title="lociA — snapshot_001",
            sub_title=f"{len(coords)} chunks · {n_clusters} cluster",
        )
        fig.savefig(MAPS_DIR / "snapshot_001.png", dpi=150, bbox_inches="tight")
        plt.close(fig)
        print(f"snapshot_001.png salvato (DataMapPlot) → {MAPS_DIR / 'snapshot_001.png'}")

    except Exception as e:
        print(f"DataMapPlot non disponibile ({e}), fallback matplotlib")
        _render_matplotlib(coords, labels, point_labels, index, chunks)

    # --- Caravaggio-prior Versione A: background estetico ---
    _render_caravaggio_prior(coords, labels)


def _render_matplotlib(coords, labels, point_labels, index, chunks):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    import colorsys

    def cluster_color(lid, n):
        h = (lid / max(n, 1)) % 1.0
        r, g, b = colorsys.hsv_to_rgb(h, 0.72, 0.85)
        return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"

    n_clusters = int(labels.max()) + 1
    colors = [cluster_color(int(l), n_clusters) for l in labels]

    fig, ax = plt.subplots(figsize=(14, 10), dpi=120)
    ax.set_facecolor("#fafaf8")
    fig.patch.set_facecolor("#fafaf8")
    ax.scatter(coords[:, 0], coords[:, 1], c=colors, s=60, alpha=0.82,
               edgecolors="white", linewidths=0.6, zorder=3)

    for i, (x, y) in enumerate(coords):
        ax.annotate(point_labels[i], (x, y), fontsize=4, color="#555",
                    xytext=(3, 3), textcoords="offset points", alpha=0.75)

    patches = [mpatches.Patch(color=cluster_color(i, n_clusters), label=f"Cluster {i}")
               for i in range(n_clusters)]
    ax.legend(handles=patches, fontsize=7, loc="lower right", framealpha=0.7)
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 1.05)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("lociA — snapshot_001", fontsize=11, color="#666", pad=8)
    plt.tight_layout()
    plt.savefig(MAPS_DIR / "snapshot_001.png", dpi=120, bbox_inches="tight")
    plt.close()
    print(f"snapshot_001.png salvato (matplotlib fallback) → {MAPS_DIR / 'snapshot_001.png'}")


def _render_caravaggio_prior(coords: np.ndarray, labels: np.ndarray):
    """Versione A: mappa puntiforme composita su background chiaroscuro."""
    from PIL import Image, ImageDraw
    import colorsys
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    import prior

    W, H = prior.CANVAS
    n_clusters = int(labels.max()) + 1

    # 1. Background (reale o sintetico)
    bg = prior.load_or_generate((W, H))

    # 2. Layer mappa: punti colorati su trasparente
    map_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(map_layer)

    margin = 60
    for i, (x, y) in enumerate(coords):
        px = int(margin + x * (W - 2 * margin))
        py = int(margin + (1 - y) * (H - 2 * margin))
        lid = int(labels[i])
        hue = (lid / max(n_clusters, 1)) % 1.0
        r, g, b = colorsys.hsv_to_rgb(hue, 0.85, 1.0)
        col = (int(r * 255), int(g * 255), int(b * 255))

        # alone luminoso
        for radius, alpha in [(9, 30), (6, 70), (4, 140), (3, 220)]:
            draw.ellipse([px - radius, py - radius, px + radius, py + radius],
                         fill=(*col, alpha))

    # 3. Composite
    result = prior.composite(bg, map_layer, alpha=0.88)
    out = MAPS_DIR / "snapshot_001_caravaggio.png"
    result.save(out, quality=92)
    print(f"snapshot_001_caravaggio.png salvato → {out}")


if __name__ == "__main__":
    run()
