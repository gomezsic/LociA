"""
Caravaggio-prior — Versione A: background estetico.

Se public/caravaggio_judith.jpg esiste: lo usa come wallpaper.
Altrimenti: genera un background chiaroscuro sintetico (dark + luce dorata centrale).

L'utente può sostituire il file con qualsiasi opera pubblico dominio
salvandola in: public/caravaggio_judith.jpg
"""

from pathlib import Path
import numpy as np

ROOT = Path(__file__).parent.parent
BG_PATH = ROOT / "public" / "caravaggio_judith.jpg"
CANVAS = 1680, 1200  # px output


def load_or_generate(size: tuple[int, int] = CANVAS) -> "Image":
    from PIL import Image

    if BG_PATH.exists() and BG_PATH.stat().st_size > 10_000:
        bg = Image.open(BG_PATH).convert("RGB").resize(size, Image.LANCZOS)
        print(f"  Background: {BG_PATH.name} ({BG_PATH.stat().st_size // 1024}KB)")
        return bg

    print("  Background: generazione chiaroscuro sintetico (Caravaggio-style)")
    return _synthetic_chiaroscuro(size)


def _synthetic_chiaroscuro(size: tuple[int, int]) -> "Image":
    from PIL import Image, ImageFilter
    import colorsys

    w, h = size
    arr = np.zeros((h, w, 3), dtype=np.float32)

    # Base scura: seppia molto scura
    arr[:, :, 0] = 0.08   # R
    arr[:, :, 1] = 0.05   # G
    arr[:, :, 2] = 0.02   # B

    # Luce dorata principale: centro-sinistra (come Caravaggio illumina il soggetto)
    cx, cy = int(w * 0.38), int(h * 0.42)
    Y, X = np.ogrid[:h, :w]
    dist = np.sqrt((X - cx) ** 2 + (Y - cy) ** 2)
    light_radius = min(w, h) * 0.55
    falloff = np.clip(1.0 - (dist / light_radius) ** 1.6, 0, 1)

    arr[:, :, 0] += falloff * 0.52   # R warm
    arr[:, :, 1] += falloff * 0.32   # G warm
    arr[:, :, 2] += falloff * 0.08   # B cold

    # Luce secondaria in basso a destra (riflesso)
    cx2, cy2 = int(w * 0.72), int(h * 0.75)
    dist2 = np.sqrt((X - cx2) ** 2 + (Y - cy2) ** 2)
    falloff2 = np.clip(1.0 - (dist2 / (light_radius * 0.4)) ** 2, 0, 1)
    arr[:, :, 0] += falloff2 * 0.18
    arr[:, :, 1] += falloff2 * 0.10
    arr[:, :, 2] += falloff2 * 0.04

    # Vignettatura ai bordi
    vx = np.linspace(0, 1, w)
    vy = np.linspace(0, 1, h)
    vign_x = 4 * vx * (1 - vx)
    vign_y = 4 * vy * (1 - vy)
    vignette = np.outer(vign_y, vign_x) ** 0.5
    for c in range(3):
        arr[:, :, c] *= 0.5 + 0.5 * vignette

    # Grana (simulazione tela)
    noise = np.random.default_rng(42).normal(0, 0.015, (h, w, 3)).astype(np.float32)
    arr = np.clip(arr + noise, 0, 1)

    img = Image.fromarray((arr * 255).astype(np.uint8), "RGB")
    img = img.filter(ImageFilter.GaussianBlur(radius=1.2))
    return img


def composite(bg: "Image", map_layer: "Image", alpha: float = 0.72) -> "Image":
    """Sovrappone la mappa sul background con alpha blending."""
    from PIL import Image

    bg_rgba = bg.convert("RGBA")
    map_rgba = map_layer.convert("RGBA")

    # Riduci opacità del layer mappa
    r, g, b, a = map_rgba.split()
    a_scaled = a.point(lambda x: int(x * alpha))
    map_rgba = Image.merge("RGBA", (r, g, b, a_scaled))

    result = Image.alpha_composite(bg_rgba, map_rgba)
    return result.convert("RGB")
