import json
import numpy as np
from pathlib import Path

EMBED_DIR = Path(__file__).parent.parent / "embeddings"


def run():
    import hdbscan

    # Clusteriamo sugli embedding originali (più ricchi) non sulle coords 2D
    embeddings = np.load(EMBED_DIR / "embeddings.npy")
    coords = np.load(EMBED_DIR / "coords_2d.npy")
    n = embeddings.shape[0]
    print(f"Clustering {n} punti (dim={embeddings.shape[1]})...")

    min_cluster = max(3, n // 12)
    clusterer = hdbscan.HDBSCAN(
        min_cluster_size=min_cluster,
        min_samples=1,
        prediction_data=True,   # abilita soft membership
        metric="euclidean",
    )
    clusterer.fit(embeddings)
    labels = clusterer.labels_.copy()

    # Soft membership: matrice (n_chunks, n_clusters)
    soft = hdbscan.all_points_membership_vectors(clusterer)  # shape (n, k)

    # Rumore (-1) → cluster extra con membership uniforme bassa
    noise_mask = labels == -1
    if noise_mask.any():
        noise_cluster_id = int(labels.max()) + 1
        labels[noise_mask] = noise_cluster_id
        noise_row = np.zeros((noise_mask.sum(), soft.shape[1] + 1))
        noise_row[:, -1] = 0.1
        # Ricostruisci soft con colonna aggiuntiva per il cluster rumore
        padded = np.zeros((n, soft.shape[1] + 1))
        padded[:, :soft.shape[1]] = soft
        padded[noise_mask, -1] = 0.1
        soft = padded

    np.save(EMBED_DIR / "labels.npy", labels)
    np.save(EMBED_DIR / "soft_membership.npy", soft)

    unique = np.unique(labels)
    print(f"Cluster trovati: {len(unique)}")
    print(f"Soft membership shape: {soft.shape} → {EMBED_DIR / 'soft_membership.npy'}")


if __name__ == "__main__":
    run()
