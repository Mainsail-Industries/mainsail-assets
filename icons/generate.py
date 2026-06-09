#!/usr/bin/env python3
"""
Starlight app-icon generator.

Renders the eight-pointed M-star (starlight-star-b.png) into three themed
app icons — light, dark, blue — using tokens from starlight-design-system.json
and Apple's 2026 icon guidance (HIG + Liquid Glass):

  - Square 1024 master at the canvas Apple expects (no pre-baked corners;
    the OS applies its squircle/superellipse mask).
  - Star centered, scaled to ~60% of the canvas (inside the safe area).
  - Background per spec: one base + one accent glow. (The design system's
    ghost-star texture is for full-bleed backgrounds; on a small icon canvas
    it visually doubles the foreground glyph.)
  - Subtle top specular highlight + bottom vignette to read as glass.

Outputs full size ladder per theme. Re-run any time to regenerate.
"""
from __future__ import annotations
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageChops

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
STAR_SRC = REPO / "starlight-star-b.png"

MASTER = 2048
SIZES = [1024, 512, 256, 180, 167, 152, 128, 120, 87, 80, 76, 64, 60, 58, 40, 32, 29, 16]

BRAND = {
    "blue":   (0x00, 0x47, 0xBB),
    "blue_700": (0x00, 0x2D, 0x77),
    "blue_900": (0x00, 0x11, 0x2E),
    "black":  (0x21, 0x20, 0x20),
    "bg0":    (0x0B, 0x0D, 0x12),
    "bg950":  (0x06, 0x08, 0x0B),
    "white":  (0xFF, 0xFF, 0xFF),
    "n50":    (0xF5, 0xF6, 0xF8),
    "n100":   (0xE7, 0xE9, 0xED),
}


def vertical_gradient(size: int, top: tuple[int, int, int], bot: tuple[int, int, int]) -> Image.Image:
    img = Image.new("RGB", (size, size), top)
    px = img.load()
    for y in range(size):
        t = y / (size - 1)
        r = round(top[0] + (bot[0] - top[0]) * t)
        g = round(top[1] + (bot[1] - top[1]) * t)
        b = round(top[2] + (bot[2] - top[2]) * t)
        for x in range(size):
            px[x, y] = (r, g, b)
    return img


def radial_aurora(size: int, color: tuple[int, int, int], cx: float, cy: float,
                  radius: float, peak_alpha: int) -> Image.Image:
    """Soft off-center radial glow — the 'aurora' from the design system."""
    layer = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    px = layer.load()
    cx_px = cx * size
    cy_px = cy * size
    rad_px = radius * size
    for y in range(size):
        for x in range(size):
            dx = x - cx_px
            dy = y - cy_px
            d = (dx * dx + dy * dy) ** 0.5 / rad_px
            if d >= 1.0:
                continue
            falloff = (1 - d) ** 2
            px[x, y] = (*color, int(peak_alpha * falloff))
    return layer.filter(ImageFilter.GaussianBlur(size * 0.04))


def ghost_star_texture(size: int, star_mask: Image.Image, color: tuple[int, int, int],
                       alpha: int, scale: float = 1.05) -> Image.Image:
    """Full-bleed star glyph at 4–8% opacity as texture per design system."""
    target = int(size * scale)
    g = star_mask.resize((target, target), Image.LANCZOS)
    canvas = Image.new("L", (size, size), 0)
    off = (size - target) // 2
    canvas.paste(g, (off, off))
    rgba = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    fill = Image.new("RGBA", (size, size), (*color, alpha))
    rgba.paste(fill, mask=canvas)
    return rgba


def specular_highlight(size: int) -> Image.Image:
    """Top arc highlight — the glass-surface specular."""
    layer = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    inset = int(size * 0.02)
    d.ellipse(
        [inset, -int(size * 0.55), size - inset, int(size * 0.55)],
        fill=(255, 255, 255, 38),
    )
    return layer.filter(ImageFilter.GaussianBlur(size * 0.025))


def bottom_vignette(size: int) -> Image.Image:
    """Subtle bottom darkening for depth."""
    layer = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    px = layer.load()
    for y in range(size):
        t = y / (size - 1)
        if t < 0.55:
            continue
        a = int(((t - 0.55) / 0.45) ** 2 * 70)
        for x in range(size):
            px[x, y] = (0, 0, 0, a)
    return layer.filter(ImageFilter.GaussianBlur(size * 0.015))


def colored_star(star_mask: Image.Image, size: int, scale: float,
                 color: tuple[int, int, int]) -> Image.Image:
    target = int(size * scale)
    m = star_mask.resize((target, target), Image.LANCZOS)
    rgba = Image.new("RGBA", (target, target), (0, 0, 0, 0))
    fill = Image.new("RGBA", (target, target), (*color, 255))
    rgba.paste(fill, mask=m)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    # Optical centering: nudge up by ~1.5% — the glyph's bottom point
    # carries more visual weight than the top.
    cx = (size - target) // 2
    cy = (size - target) // 2 - int(size * 0.015)
    out.paste(rgba, (cx, cy), rgba)
    return out


def star_glow(star_layer: Image.Image, color: tuple[int, int, int], blur_frac: float,
              alpha: int) -> Image.Image:
    """Outer halo behind the star (Liquid Glass internal light)."""
    size = star_layer.size[0]
    mask = star_layer.split()[3]
    glow = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    fill = Image.new("RGBA", (size, size), (*color, alpha))
    glow.paste(fill, mask=mask)
    return glow.filter(ImageFilter.GaussianBlur(size * blur_frac))


def star_inner_drop(star_layer: Image.Image, color: tuple[int, int, int],
                    offset: int, blur_frac: float, alpha: int) -> Image.Image:
    """Soft drop shadow under the star — depth without harshness."""
    size = star_layer.size[0]
    mask = star_layer.split()[3]
    shadow = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    fill = Image.new("RGBA", (size, size), (*color, alpha))
    shadow.paste(fill, mask=mask)
    shadow = shadow.filter(ImageFilter.GaussianBlur(size * blur_frac))
    shifted = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    shifted.paste(shadow, (0, offset), shadow)
    return shifted


def build_master(theme: str, star_mask: Image.Image) -> Image.Image:
    size = MASTER

    if theme == "light":
        bg = vertical_gradient(size, BRAND["white"], BRAND["n100"])
        aurora_color = BRAND["blue"]
        aurora_alpha = 30
        star_color = BRAND["black"]
        glow_color = BRAND["blue"]
        glow_alpha = 22
        drop_color = (0, 0, 0)
        drop_alpha = 60
        specular_strength = 1.0
    elif theme == "dark":
        bg = vertical_gradient(size, BRAND["black"], BRAND["bg950"])
        aurora_color = BRAND["blue"]
        aurora_alpha = 130
        star_color = BRAND["white"]
        glow_color = BRAND["blue"]
        glow_alpha = 110
        drop_color = (0, 0, 0)
        drop_alpha = 120
        specular_strength = 0.65
    elif theme == "blue":
        bg = vertical_gradient(size, BRAND["blue"], BRAND["blue_700"])
        aurora_color = (0x5E, 0x96, 0xFF)
        aurora_alpha = 150
        star_color = BRAND["white"]
        glow_color = (0xC7, 0xD6, 0xF5)
        glow_alpha = 60
        drop_color = BRAND["blue_900"]
        drop_alpha = 140
        specular_strength = 0.85
    else:
        raise ValueError(theme)

    canvas = bg.convert("RGBA")

    # Aurora — off-center upper-left per design system rule.
    aurora = radial_aurora(size, aurora_color, cx=0.30, cy=0.28,
                           radius=0.75, peak_alpha=aurora_alpha)
    canvas.alpha_composite(aurora)

    # Specular — top arc, glass surface.
    spec = specular_highlight(size)
    if specular_strength != 1.0:
        r, g, b, a = spec.split()
        a = a.point(lambda v: int(v * specular_strength))
        spec = Image.merge("RGBA", (r, g, b, a))
    canvas.alpha_composite(spec)

    # Foreground star at ~60% canvas width.
    star = colored_star(star_mask, size, scale=0.60, color=star_color)

    # Depth: outer glow → drop shadow → star.
    canvas.alpha_composite(star_glow(star, glow_color, blur_frac=0.035, alpha=glow_alpha))
    canvas.alpha_composite(star_inner_drop(star, drop_color,
                                           offset=int(size * 0.008),
                                           blur_frac=0.012,
                                           alpha=drop_alpha))
    canvas.alpha_composite(star)

    # Bottom vignette — keeps the icon weighted at the base.
    canvas.alpha_composite(bottom_vignette(size))

    return canvas


def downsample(master: Image.Image, target: int) -> Image.Image:
    return master.resize((target, target), Image.LANCZOS)


def rounded_preview(square: Image.Image, radius_frac: float = 0.2237) -> Image.Image:
    """macOS-style rounded preview using the ~22.37% radius convention."""
    size = square.size[0]
    radius = int(size * radius_frac)
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, size, size], radius=radius, fill=255)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(square, (0, 0), mask)
    return out


def main() -> None:
    star_src = Image.open(STAR_SRC).convert("RGBA")
    star_mask = star_src.split()[3]
    # The source has whitespace padding — trim so scale math is precise.
    bbox = star_mask.getbbox()
    star_mask = star_mask.crop(bbox)
    s = max(star_mask.size)
    square_mask = Image.new("L", (s, s), 0)
    square_mask.paste(star_mask, ((s - star_mask.size[0]) // 2,
                                  (s - star_mask.size[1]) // 2))
    star_mask = square_mask

    for theme in ("light", "dark", "blue"):
        out_dir = ROOT / theme
        out_dir.mkdir(parents=True, exist_ok=True)
        print(f"[{theme}] rendering master @ {MASTER}")
        master = build_master(theme, star_mask)

        for size in SIZES:
            path = out_dir / f"starlight-icon-{theme}-{size}.png"
            downsample(master, size).save(path, "PNG", optimize=True)
            print(f"  {path.relative_to(REPO)}")

        # macOS-style rounded preview for web/docs.
        rp = rounded_preview(downsample(master, 1024))
        rp_path = out_dir / f"starlight-icon-{theme}-rounded-1024.png"
        rp.save(rp_path, "PNG", optimize=True)
        print(f"  {rp_path.relative_to(REPO)}")


if __name__ == "__main__":
    main()
