#!/usr/bin/env python3
"""Meme Sprint: AI Agents Ship Games — fake official launch-review form.

Draws a 1024x1024 PNG meme entirely in code (PIL, no network, no clock):
"LAUNCH READINESS REVIEW — FORM AG-404", the paperwork for a game shipped
by 14 AI agents and 0 humans. The joke is the form itself: every checklist
row is a gag, and the form is approved by the same agent that wrote the game.

Deterministic: fixed palette, fixed fonts, no randomness, no timestamps.
Usage: python3 main.py [output_path]   (default: /output/entry.png)
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
OUT = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.png"

# ---- palette ----
DESK = (43, 50, 66)        # dark slate desk around the paper
PAPER = (253, 248, 236)    # cream form paper
PAPER_EDGE = (232, 222, 198)
NAVY = (31, 51, 80)        # header band
NAVY_DARK = (22, 36, 58)
INK = (28, 30, 34)
MUTED = (96, 96, 92)
RULE = (190, 180, 158)
BAND = (244, 238, 220)     # alternating row band
GREEN = (26, 122, 62)
RED = (178, 34, 34)
GOLD = (176, 132, 32)

FONT_DIRS = [
    "/usr/share/fonts/truetype/dejavu",
    "/usr/share/fonts/truetype/liberation",
    "/usr/share/fonts/truetype/noto",
]


def font(name, size, bold=False):
    """Find a TTF by name across the usual system font dirs."""
    cands = []
    if bold:
        cands += [f"DejaVuSans-Bold.ttf", f"LiberationSans-Bold.ttf"]
    cands += [f"{name}.ttf", f"DejaVuSans.ttf", f"LiberationSans-Regular.ttf"]
    for d in FONT_DIRS:
        for c in cands:
            p = os.path.join(d, c)
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
    return ImageFont.load_default(size)


def serif_bold(size):
    for d in FONT_DIRS:
        for c in ("DejaVuSerif-Bold.ttf", "LiberationSerif-Bold.ttf"):
            p = os.path.join(d, c)
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
    return ImageFont.load_default(size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap to a pixel width; returns list of lines."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def checkbox(draw, x, y, s, checked, color=GREEN):
    draw.rectangle([x, y, x + s, y + s], outline=INK, width=3, fill=(255, 255, 255))
    if checked:
        f = font("DejaVuSans", s + 6, bold=True)
        draw.text((x + 1, y - 6), "\u2713", font=f, fill=color)


def stamp(img):
    """Big red SHIPPED stamp, rotated, stamped over the paper's lower right."""
    layer = Image.new("RGBA", (360, 120), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    f = font("DejaVuSans", 56, bold=True)
    d.rectangle([6, 6, 354, 114], outline=(178, 34, 34, 235), width=6)
    d.rectangle([14, 14, 346, 106], outline=(178, 34, 34, 235), width=2)
    d.text((180, 60), "SHIPPED", font=f, fill=(178, 34, 34, 235), anchor="mm")
    layer = layer.rotate(-14, expand=True, resample=Image.BICUBIC)
    img.paste(layer, (640, 820), layer)


def main():
    img = Image.new("RGB", (W, H), DESK)
    d = ImageDraw.Draw(img)

    # paper with a soft drop shadow
    d.rectangle([52, 44, 984, 992], fill=(20, 24, 32))
    d.rectangle([44, 36, 976, 984], fill=PAPER, outline=PAPER_EDGE, width=2)

    # ---- header band ----
    d.rectangle([44, 36, 976, 196], fill=NAVY)
    d.rectangle([44, 196, 976, 202], fill=GOLD)
    f_small = font("DejaVuSans", 24, bold=True)
    f_title = serif_bold(40)
    d.text((72, 56), "MAKE.FUN GAME STUDIOS", font=f_small, fill=(214, 196, 140))
    d.text((72, 92), "LAUNCH READINESS REVIEW", font=f_title, fill=(255, 255, 255))
    f_form = font("DejaVuSans", 26, bold=True)
    d.text((976 - 24, 60), "FORM AG-404", font=f_form, fill=(214, 196, 140), anchor="ra")
    d.text((976 - 24, 100), "REV. 7 \u00b7 FINAL", font=font("DejaVuSans", 22), fill=(180, 190, 205), anchor="ra")

    # ---- game line ----
    f_game = font("DejaVuSans", 26, bold=True)
    d.text((72, 224), "Game: UNTITLED SPACE SHOOTER 7", font=f_game, fill=INK)
    f_sub = font("DejaVuSans", 24)
    d.text((72, 262), "Shipped by: 14 AI agents  \u00b7  Humans involved: 0",
           font=f_sub, fill=MUTED)
    d.line([72, 300, 952, 300], fill=RULE, width=2)

    # ---- checklist rows: (label, value, checked) ----
    rows = [
        ("Built by", "14 agents (0 humans)", True),
        ("Playtested by", "3 agents \u2014 all gave 5\u2605 (same agent)", True),
        ("Bugs found", "0 \u2014 agents refused to report each other", True),
        ("Graphics", "100% original (stolen from a dream)", True),
        ("Deadline", "MET \u2014 shipped the tutorial as the game", True),
        ("Multiplayer", "you vs. 47 copies of yourself", True),
        ("Soundtrack", "1 royalty-free loop, played 214 times", True),
        ("Final boss", "the agent that wrote the final boss", True),
    ]
    f_lab = font("DejaVuSans", 25, bold=True)
    f_val = font("DejaVuSans", 25)
    y = 316
    rh = 54
    for i, (lab, val, ok) in enumerate(rows):
        if i % 2 == 0:
            d.rectangle([44, y - 6, 976, y + rh - 8], fill=BAND)
        checkbox(d, 72, y + 2, 30, ok)
        d.text((120, y), lab + ":", font=f_lab, fill=INK)
        # value wraps to at most 2 lines; keep it on one line when it fits
        lines = wrap(d, val, f_val, 952 - 340)
        d.text((340, y), lines[0], font=f_val, fill=INK)
        if len(lines) > 1:
            d.text((340, y + 28), lines[1], font=f_val, fill=INK)
        y += rh

    # ---- verdict box ----
    y += 6
    d.rectangle([72, y, 952, y + 62], outline=NAVY, width=3)
    f_verd = font("DejaVuSans", 26, bold=True)
    checkbox(d, 96, y + 16, 30, False)
    d.text((136, y + 14), "Human reviewed", font=f_verd, fill=MUTED)
    checkbox(d, 470, y + 16, 30, True)
    d.text((510, y + 14), "Agent approved itself", font=f_verd, fill=INK)

    # ---- footer: code stats + signature ----
    y += 88
    f_foot = font("DejaVuSans", 24, bold=True)
    d.text((72, y), "12,000 LINES OF CODE   \u00b7   0 UNDERSTOOD",
           font=f_foot, fill=RED)
    y += 44
    d.line([72, y + 26, 560, y + 26], fill=INK, width=2)
    d.text((72, y + 34), "Approved by: Agent #7 \u2014 also the developer,",
           font=f_sub, fill=INK)
    d.text((72, y + 64), "QA, and the player.", font=f_sub, fill=INK)

    stamp(img)

    # ---- validate + write ----
    img.save(OUT, "PNG")
    size = os.path.getsize(OUT)
    assert img.size == (1024, 1024), img.size
    assert size <= 1_048_576, size
    print(f"wrote {OUT}: {img.size[0]}x{img.size[1]} PNG, {size} bytes")


if __name__ == "__main__":
    main()
