#!/usr/bin/env python3
"""
Findet die grün hinterlegten Kästchen in den Vorlesungsfolien.

Zwei Verfahren, weil eines allein nicht reicht:

1. Vektorpass  – liest die Füllfarbe der Zeichenobjekte. Erfasst alle Kästen,
   die als Form im PDF stecken.
2. Pixelpass   – rendert die Folie und sucht grünstichige Pixelbänder im
   Folienkörper. Nötig, weil ein Teil der Kästen als Rastergrafik eingebettet
   ist und für den Vektorpass unsichtbar bleibt.

Zusätzlich wird die aufgedruckte Foliennummer aus der Fußzeile gelesen. Sie
weicht in einzelnen Foliensätzen von der PDF-Seitenzahl ab; Fundstellen im
Lernmaterial müssen die aufgedruckte Nummer nennen.

Aufruf:
    python3 scripts/finde_gruene_kaesten.py <verzeichnis-mit-pdfs> [--json datei]
"""
import argparse
import glob
import json
import os
import re
import sys
from collections import Counter

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("PyMuPDF fehlt:  pip install pymupdf")

# Reihenfolge der Kapitel, nicht alphabetisch
KAPITEL = [
    ("1", "GdA_1_Grund"),
    ("2", "GdA_2_Systeme"),
    ("2.1", "GdA_2.1_Signale"),
    ("3", "GdA_3_Digital"),
    ("4", "GdA_4_VPS"),
    ("4.2", "GdA_4.2_einfache"),
    ("5", "GdA_5_SPS"),
    ("6", "GdA_6_seq"),
    ("7", "GdA_7_Automaten"),
]

SCAN_DPI = 36           # grob genügt, es geht nur um Flächen
BAND_BREITE = 0.20      # Anteil der Folienbreite, ab dem ein Band zählt
BAND_HOEHE = 4          # Zeilen in Folge, ab denen es ein Kasten ist
KOERPER = (0.15, 0.88)  # Folienkörper ohne Titelleiste und Fußzeile


def ist_gruen_rgb(c):
    """Füllfarbe (0..1) eines Zeichenobjekts."""
    r, g, b = c
    return g > r + 0.05 and g > b + 0.05


def ist_gruen_pixel(r, g, b):
    """Pixel (0..255). Bewusst weit gefasst, der Sichtpass sortiert nach."""
    return g > r + 12 and g > b + 12 and g > 90


def vektor_kaesten(page):
    """Grüne Rechtecke aus den Zeichenobjekten, Folienhintergrund ausgenommen."""
    pw, ph = page.rect.width, page.rect.height
    roh = []
    for d in page.get_drawings():
        c = d.get("fill")
        if not c or not ist_gruen_rgb(c):
            continue
        r = d["rect"]
        if r.width > pw * 0.9 and r.height > ph * 0.9:
            continue                       # Folienhintergrund
        if r.width < 30 or r.height < 10:
            continue                       # Aufzählungspunkt, Linie
        roh.append(r)
    # überlappende und direkt angrenzende Rechtecke zusammenfassen
    roh.sort(key=lambda r: (round(r.y0), round(r.x0)))
    zusammen = []
    for r in roh:
        treffer = None
        for m in zusammen:
            angrenzend = abs(m.y1 - r.y0) < 6 and not (r.x1 < m.x0 or r.x0 > m.x1)
            if m.intersects(r) or angrenzend:
                treffer = m
                break
        if treffer:
            treffer |= r
        else:
            zusammen.append(+r)
    return zusammen


def pixel_kandidat(page):
    """True, wenn im Folienkörper ein grünes Band von Kastenhöhe liegt."""
    pm = page.get_pixmap(dpi=SCAN_DPI)
    W, H, n, s = pm.width, pm.height, pm.n, pm.samples
    lauf = beste = 0
    for y in range(int(H * KOERPER[0]), int(H * KOERPER[1])):
        breit = run = 0
        for x in range(W):
            o = (y * W + x) * n
            if ist_gruen_pixel(s[o], s[o + 1], s[o + 2]):
                run += 1
                breit = max(breit, run)
            else:
                run = 0
        if breit > W * BAND_BREITE:
            lauf += 1
            beste = max(beste, lauf)
        else:
            lauf = 0
    return beste >= BAND_HOEHE


FUSSZEILE = re.compile(r"Grundlagen der Automation\s+(\d{1,3})")


def folien_nummer(page):
    """Aufgedruckte Nummer aus der Fußzeile, sonst None.

    Die Nummer wird gezielt hinter dem Fußzeilentitel gelesen. Ein reines
    „letzte Zahl im unteren Bereich" verfängt sich in den handschriftlichen
    Notizen, die auf manchen Folien bis in die Fußzeile reichen.
    """
    r = fitz.Rect(0, page.rect.height * 0.88, page.rect.width, page.rect.height)
    text = " ".join(page.get_text("text", clip=r).split())
    m = FUSSZEILE.search(text)
    return int(m.group(1)) if m else None


def text_im_kasten(page, rect):
    teile = [t.strip() for t in page.get_text("text", clip=rect).split("\n") if t.strip()]
    return " | ".join(teile)


def analysiere(pfad, kapitel):
    doc = fitz.open(pfad)
    versatz = Counter()
    kaesten, kandidaten = [], []
    for i, page in enumerate(doc, 1):
        nr = folien_nummer(page)
        if nr is not None:
            versatz[nr - i] += 1
        gedruckt = nr if nr is not None else i

        vek = vektor_kaesten(page)
        for r in vek:
            txt = text_im_kasten(page, r)
            if len(txt) < 3:
                continue
            kaesten.append({"kapitel": kapitel, "pdf_seite": i, "folie": gedruckt,
                            "quelle": "vektor", "text": txt})
        if not vek and i > 2 and pixel_kandidat(page):
            # Rastergrafik: Text steht nicht in der Textebene, Sichtpruefung noetig
            kandidaten.append({"kapitel": kapitel, "pdf_seite": i, "folie": gedruckt,
                               "quelle": "pixel", "text": ""})
    return kaesten, kandidaten, versatz, len(doc)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("verzeichnis", help="Ordner mit den GdA-PDFs")
    ap.add_argument("--json", help="Ergebnis zusätzlich als JSON ablegen")
    args = ap.parse_args()

    alle_kaesten, alle_kandidaten = [], []
    print(f"{'Kap.':<6}{'Folien':>7}{'Vektor':>8}{'Sichtpruefung':>15}   Versatz Fusszeile")
    print("-" * 62)
    for kapitel, muster in KAPITEL:
        treffer = glob.glob(os.path.join(args.verzeichnis, f"*{muster}*.pdf"))
        if not treffer:
            print(f"{kapitel:<6}{'—':>7}   nicht gefunden")
            continue
        kaesten, kandidaten, versatz, seiten = analysiere(treffer[0], kapitel)
        alle_kaesten += kaesten
        alle_kandidaten += kandidaten
        stufen = sorted(versatz)
        beschreibung = ", ".join(f"{v:+d}" for v in stufen) or "—"
        hinweis = "" if stufen == [0] else "  <== driftet, Fundstellen pruefen"
        print(f"{kapitel:<6}{seiten:>7}{len(kaesten):>8}{len(kandidaten):>15}"
              f"   {beschreibung}{hinweis}")

    print("-" * 62)
    print(f"{'gesamt':<6}{'':>7}{len(alle_kaesten):>8}{len(alle_kandidaten):>15}")
    if alle_kandidaten:
        print("\nSeiten fuer die Sichtpruefung (Kasten liegt als Rastergrafik vor):")
        nach_kapitel = {}
        for k in alle_kandidaten:
            nach_kapitel.setdefault(k["kapitel"], []).append(k["folie"])
        for kap, folien in nach_kapitel.items():
            print(f"  Kapitel {kap}: {folien}")

    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump({"kaesten": alle_kaesten, "kandidaten": alle_kandidaten},
                      fh, ensure_ascii=False, indent=1)
        print(f"\ngeschrieben: {args.json}")


if __name__ == "__main__":
    main()
