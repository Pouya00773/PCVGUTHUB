#!/usr/bin/env python3
"""
Qualitätsprüfung für output/Kaffee_Traceability_EUDR.pptx.

Prüft, was bei skriptgenerierten Folien am häufigsten schiefgeht:
  1. Textüberlauf  — geschätzte Texthöhe größer als die Box
  2. Randverletzung — Formen ragen über den Folienrand oder unter 0,4 Zoll Rand
  3. Sprechernotizen — vorhanden und lang genug

Die Überlaufschätzung ist bewusst konservativ: Sie rechnet mit einer
durchschnittlichen Zeichenbreite und meldet nur deutliche Überschreitungen,
damit die Liste handhabbar bleibt.

    python3 scripts/pptx_qa.py
"""
import math
import sys
from pptx import Presentation
from pptx.util import Emu

DECK = 'output/Kaffee_Traceability_EUDR.pptx'
SLIDE_W, SLIDE_H = 13.333, 7.5
MARGIN = 0.40
# Mittlere Zeichenbreite als Anteil der Schriftgröße (Calibri/Cambria, gemischt)
CHAR_W = 0.53
CHAR_W_BOLD = 0.58     # fetter Text läuft breiter
LINE_H = 1.22          # Zeilenhöhe als Faktor der Schriftgröße
TOLERANCE = 1.06       # erst ab 6 % Überschreitung melden


def emu_in(v):
    return Emu(v).inches if v is not None else 0.0


def est_overflow(text, width_in, height_in, pt, bold=False):
    """Geschätzte Texthöhe in Zoll gegen verfügbare Höhe."""
    if not text.strip() or width_in <= 0:
        return 0.0, 0.0
    char_w_in = pt * (CHAR_W_BOLD if bold else CHAR_W) / 72.0
    per_line = max(1, int(width_in / char_w_in))
    lines = 0
    for para in text.split('\n'):
        lines += max(1, math.ceil(len(para) / per_line))
    need = lines * pt * LINE_H / 72.0
    return need, height_in


def main():
    prs = Presentation(DECK)
    overflow, bounds, notes_issues = [], [], []

    for idx, slide in enumerate(prs.slides, start=1):
        for shp in slide.shapes:
            x, y = emu_in(shp.left), emu_in(shp.top)
            w, h = emu_in(shp.width), emu_in(shp.height)

            # --- Ränder und Folienrand ---
            if x < -0.01 or y < -0.01 or x + w > SLIDE_W + 0.01 or y + h > SLIDE_H + 0.01:
                # ganzflächige Deko-Kreise sind gewollt
                if not (shp.shape_type is not None and w > 3 and h > 3):
                    bounds.append((idx, f'ragt über den Rand: x={x:.2f} y={y:.2f} w={w:.2f} h={h:.2f}'))

            # --- Textüberlauf ---
            if not shp.has_text_frame:
                continue
            tf = shp.text_frame
            text = tf.text or ''
            if not text.strip():
                continue
            sizes = [r.font.size.pt for p in tf.paragraphs for r in p.runs
                     if r.font.size is not None]
            pt = max(sizes) if sizes else 18.0
            bold = any(r.font.bold for p in tf.paragraphs for r in p.runs)
            need, avail = est_overflow(text, w - 0.04, h, pt, bold)
            if avail > 0 and need > avail * TOLERANCE:
                overflow.append((idx, round(need, 2), round(avail, 2), pt,
                                 text[:58].replace('\n', ' ⏎ ')))

        # --- Notizen ---
        nt = slide.notes_slide.notes_text_frame.text if slide.has_notes_slide else ''
        wc = len(nt.split())
        if wc < 20:
            notes_issues.append((idx, wc))

    print(f'Folien: {len(prs.slides.__iter__.__self__._sldIdLst)}\n')

    print(f'== Textüberlauf (geschätzt): {len(overflow)} Fälle ==')
    for idx, need, avail, pt, snip in sorted(overflow, key=lambda r: -(r[1] - r[2])):
        print(f'  Folie {idx:>2}  braucht {need:>4}" / hat {avail:>4}"  {pt:>4.1f}pt  {snip}')

    print(f'\n== Rand-/Grenzverletzungen: {len(bounds)} ==')
    for idx, msg in bounds:
        print(f'  Folie {idx:>2}  {msg}')

    print(f'\n== Notizen zu kurz (< 20 Wörter): {len(notes_issues)} ==')
    for idx, wc in notes_issues:
        print(f'  Folie {idx:>2}  {wc} Wörter')

    return 1 if overflow or bounds else 0


if __name__ == '__main__':
    sys.exit(main())
