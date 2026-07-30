#!/usr/bin/env python3
"""
Findet die handschriftlichen Klausur-Markierungen in den Vorlesungsfolien.

Zwei Durchgänge, und beide sind nötig:

1. Textpass  – sucht Varianten von „klausurrelevant" in der Textebene. Die
   Handschrift wurde beim Erzeugen des PDFs mit erkannt, allerdings oft grob
   verstümmelt („K2lansar relevant", „1)lansurrelevant", „Kausurrelevant").
   Deshalb ist das Muster bewusst weit gefasst.
2. Markerpass – sucht die Spuren des türkisen Textmarkers. Nötig, weil der
   Textpass nachweislich Marker verfehlt: Auf Kap. 4.2/18 steht ein groß
   umkringeltes „Klausurrelevant!", das in der Textebene gar nicht ankommt.

   Zwei Einschränkungen, die man kennen muss:
   - Der Textmarker steht für Hervorhebung allgemein. Viele markierte Folien
     tragen gar kein Wort „Klausur", sondern nur eine betonte Stelle.
   - Manche Folien enthalten **gedruckte** hellblaue Flächen, etwa Tabellenköpfe.
     Die sehen wie Textmarker aus. Kap. 4.2/14 wird so gemeldet, obwohl dort
     keine einzige handschriftliche Notiz steht.

   Der Pass liefert also Kandidaten, keine Marker. Blaue Handschrift taugt als
   Signal noch weniger — die Folien enthalten selbst blaue Aufzählungspunkte und
   Diagrammlinien, damit wird praktisch jede Seite gemeldet.

WICHTIG: Das Skript garantiert keine Vollständigkeit. Es liefert Kandidaten;
was in `lernskript/klausurmarker.md` landet, muss an der gerenderten Folie
gesichtet worden sein.

Aufruf:
    python3 scripts/finde_klausurmarker.py <verzeichnis-mit-pdfs>
"""
import argparse
import glob
import os
import re
import sys

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("PyMuPDF fehlt:  pip install pymupdf")

# weit gefasst, weil die Handschrifterkennung den Wortanfang gern zerlegt
MARKER = re.compile(r"relevan|elevan|klausur|lausur|lausan|clausur", re.I)
NEGATIV = re.compile(r"nicht\s*klausur", re.I)
FUSSZEILE = re.compile(r"Grundlagen der Automation\s+(\d{1,3})")

# Fehlalarme aus dem Fließtext der Folien, die nichts mit Markierungen zu tun haben
IGNORIEREN = re.compile(r"technisch relevant|relevant[en]? Ausgangsgr|"
                        r"Auslegung von Hauptstromkreisen relevant", re.I)

SCAN_DPI = 40
MARKER_SCHWELLE = 400  # türkise Pixel bei 40 dpi; markierte Folien liegen bei 5000+


def folien_nummer(page):
    r = fitz.Rect(0, page.rect.height * 0.88, page.rect.width, page.rect.height)
    text = " ".join(page.get_text("text", clip=r).split())
    m = FUSSZEILE.search(text)
    return int(m.group(1)) if m else None


def ist_textmarker(r, g, b):
    """Türkis des Leuchtmarkers. Blaue Foliengrafik erfüllt das nicht."""
    return g > r + 40 and b > r + 40 and g > 170 and b > 170


def marker_menge(page):
    """Zählt Textmarker-Pixel. Ohne numpy, deshalb über Byte-Slices statt
    Pixelschleife — bei knapp 500 Folien ist der Unterschied erheblich."""
    pm = page.get_pixmap(dpi=SCAN_DPI)
    W, H, n, s = pm.width, pm.height, pm.n, pm.samples
    rot, gruen, blau = s[0::n], s[1::n], s[2::n]
    return sum(1 for r, g, b in zip(rot, gruen, blau) if ist_textmarker(r, g, b))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("verzeichnis")
    ap.add_argument("--marker", action="store_true",
                    help="zusätzlich nach Textmarker-Spuren suchen (langsamer)")
    args = ap.parse_args()

    pdfs = sorted(glob.glob(os.path.join(args.verzeichnis, "*.pdf")))
    if not pdfs:
        sys.exit("keine PDFs gefunden")

    print("== Textpass: Fundstellen im Textlayer ==")
    print(f"{'Datei':<34}{'Folie':>6}  {'Art':<8}Rohtext")
    print("-" * 104)
    gefunden = []
    for pfad in pdfs:
        name = os.path.basename(pfad).split("-", 1)[-1].replace(".pdf", "")
        try:
            doc = fitz.open(pfad)
        except Exception:
            continue
        for i, page in enumerate(doc, 1):
            text = page.get_text()
            treffer = {m.start() for m in MARKER.finditer(text)}
            for pos in sorted(treffer):
                roh = " ".join(text[max(0, pos - 45):pos + 30].split())
                if IGNORIEREN.search(roh):
                    continue
                nr = folien_nummer(page) or i
                art = "negativ" if NEGATIV.search(roh) else "positiv"
                schluessel = (name, nr)
                if schluessel in [g[:2] for g in gefunden]:
                    continue
                gefunden.append((name, nr, art, roh))
                print(f"{name[:33]:<34}{nr:>6}  {art:<8}{roh[:56]}")
    print("-" * 104)
    print(f"{len(gefunden)} Folien mit Fundstelle im Textlayer\n")

    if args.marker:
        print("== Markerpass: Folien mit türkisem Textmarker ==")
        bekannt = {(n, f) for n, f, _, _ in gefunden}
        offen = 0
        for pfad in pdfs:
            name = os.path.basename(pfad).split("-", 1)[-1].replace(".pdf", "")
            try:
                doc = fitz.open(pfad)
            except Exception:
                continue
            for i, page in enumerate(doc, 1):
                menge = marker_menge(page)
                if menge <= MARKER_SCHWELLE:
                    continue
                nr = folien_nummer(page) or i
                schon = "bereits im Textpass" if (name, nr) in bekannt else "SICHTEN"
                if schon == "SICHTEN":
                    offen += 1
                print(f"  {name[:33]:<34}{nr:>6}  {menge:>6} Pixel   {schon}")
        print(f"\n  davon noch nicht im Textpass erfasst: {offen}\n")

    print("Hinweis: Diese Ausgabe ist eine Kandidatenliste, kein Nachweis.")
    print("Die Handschrifterkennung ist unzuverlässig — Kap. 4.2/18 trägt einen")
    print("deutlich sichtbaren Marker, der im Textlayer fehlt. Massgeblich ist")
    print("lernskript/klausurmarker.md; dort steht nur, was an der gerenderten")
    print("Folie gesichtet wurde.")


if __name__ == "__main__":
    main()
