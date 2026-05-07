import pickle
import numpy as np
from pathlib import Path

EMBED_DIR = Path(__file__).parent.parent / "embeddings"
MODELS_DIR = Path(__file__).parent.parent / "models"


def run():
    import pacmap

    MODELS_DIR.mkdir(exist_ok=True)
    embeddings = np.load(EMBED_DIR / "embeddings.npy")
    n = embeddings.shape[0]
    print(f"Proiezione PaCMAP di {n} vettori (dim={embeddings.shape[1]})...")

    reducer = pacmap.PaCMAP(
        n_components=2,
        n_neighbors=min(10, n - 1),
        MN_ratio=0.5,
        FP_ratio=2.0,
        random_state=42,
        verbose=True,
    )
    coords = reducer.fit_transform(embeddings)

    # Normalizza 0-1
    coords -= coords.min(axis=0)
    coords /= coords.max(axis=0) + 1e-8

    np.save(EMBED_DIR / "coords_2d.npy", coords)

    # Salva modello per transform() su nuovi punti
    with open(MODELS_DIR / "pacmap_model.pkl", "wb") as f:
        pickle.dump(reducer, f)

    print(f"Coordinate salvate: {coords.shape} → {EMBED_DIR / 'coords_2d.npy'}")
    print(f"Modello salvato → {MODELS_DIR / 'pacmap_model.pkl'}")


if __name__ == "__main__":
    run()
