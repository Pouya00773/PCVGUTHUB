#!/usr/bin/env python3
"""
Gemeinsame Kartenlogik für die Word- und die HTML-Ausgabe.

Der Punkt dieses Moduls ist die Vergabe des ★: Sie erfolgt **mechanisch** aus
`lernskript/klausurmarker.md`, nicht von Hand im Kartentext. Vorher waren im
Kartentext 69 Sterne gesetzt, belegt waren aber nur 16 Folien — das Zeichen
behauptete mehr, als die Quellen hergeben. Jetzt kann es nicht mehr auseinander
laufen.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "lernskript"

FUNDSTELLE = re.compile(r"—\s*\*([^*]+)\*\s*(?:◆\s*)?$")
KARTE = re.compile(
    r"^\*\*V:\*\*\s*(.+?)\n\*\*R:\*\*\s*(.+?)(?=\n\n|\n>|\Z)", re.M | re.S
)
KAPITEL = re.compile(r"^## (.+?)$", re.M)
# Zeile einer Markertabelle: | Kap. 4.2/18 | Thema | Wortlaut |
MARKERZEILE = re.compile(r"^\|\s*(Kap\.\s*[\d.]+/\d+)\s*\|\s*([^|]+?)\s*\|", re.M)


def lies_marker(pfad=None):
    """Belegte Fundstellen aus klausurmarker.md.

    Rückgabe: (positiv, negativ) als Mengen normalisierter Fundstellen.
    Die negative Tabelle steht unter der Überschrift 'Negative Markierungen'.
    """
    pfad = pfad or (SRC / "klausurmarker.md")
    text = pfad.read_text(encoding="utf-8")
    schnitt = text.find("## Negative Markierungen")
    if schnitt == -1:
        oben, unten = text, ""
    else:
        oben, unten = text[:schnitt], text[schnitt:]
        ende = unten.find("## Hinweise auf den")
        if ende != -1:
            unten = unten[:ende]

    def sammle(abschnitt):
        return {norm(m.group(1)) for m in MARKERZEILE.finditer(abschnitt)}

    return sammle(oben), sammle(unten)


EINZELN = re.compile(r"kap[\d.]+/\d+")


def norm(fundstelle):
    """'Kap. 4.2/18' -> 'kap4.2/18'; toleriert Leerzeichen und Schreibweisen."""
    return fundstelle.strip().lower().replace(" ", "").replace("kap.", "kap")


def fundstellen(quelle):
    """Alle Einzelfundstellen einer Angabe.

    Eine Karte darf mehrere nennen („Kap. 4.2/3, Kap. 7/4"). Sie gilt als
    belegt, sobald **eine** davon in der Markerliste steht.
    """
    return set(EINZELN.findall(norm(quelle)))


def lies_karten(pfad=None, marker=None):
    """Karten mit den Stufen 'belegt', 'verwandt' und ''.

    Jede Karte ist ein dict mit kapitel, frage, antwort, quelle, stufe.
    """
    pfad = pfad or (SRC / "karteikarten.md")
    text = pfad.read_text(encoding="utf-8")
    positiv, _ = marker if marker else lies_marker()

    # Kapitelüberschriften mit ihrer Position, um jeder Karte eines zuzuordnen
    kapitel = [(m.start(), m.group(1).strip()) for m in KAPITEL.finditer(text)]

    karten = []
    for m in KARTE.finditer(text):
        frage = " ".join(m.group(1).split())
        antwort = " ".join(m.group(2).split())

        verwandt = "◆" in frage
        frage = frage.replace("◆", "").replace("★", "").strip()

        quelle = ""
        fm = FUNDSTELLE.search(frage)
        if fm:
            quelle = fm.group(1).strip()
            frage = FUNDSTELLE.sub("", frage).strip()

        belegt = bool(fundstellen(quelle) & positiv)
        stufe = "belegt" if belegt else ("verwandt" if verwandt else "")

        kap = ""
        for pos, name in kapitel:
            if pos < m.start():
                kap = name
            else:
                break
        karten.append({"kapitel": kap, "frage": frage, "antwort": antwort,
                       "quelle": quelle, "stufe": stufe})
    return karten


def kapitel_code(name):
    """'Kapitel 4.2 — Schaltwerke' -> 'K4.2'"""
    m = re.match(r"Kapitel\s+([\d.]+)", name)
    return "K" + m.group(1) if m else name.split()[0][:4].upper()


def pruefe(karten, positiv):
    """Bricht ab, wenn die Sternvergabe nicht zu den Belegen passt.

    Zwei Zusicherungen: kein ★ ohne Fundstelle, und jede belegte Fundstelle,
    die im Kartensatz vorkommt, trägt auch ein ★.
    """
    ohne_quelle = [k for k in karten if k["stufe"] == "belegt" and not k["quelle"]]
    if ohne_quelle:
        raise SystemExit(f"FEHLER: {len(ohne_quelle)} Karten mit ★ ohne Fundstelle")

    falsch = [k for k in karten
              if k["stufe"] == "belegt" and not (fundstellen(k["quelle"]) & positiv)]
    if falsch:
        raise SystemExit(f"FEHLER: {len(falsch)} Karten mit ★ ohne Beleg")

    verpasst = [k for k in karten
                if fundstellen(k["quelle"]) & positiv and k["stufe"] != "belegt"]
    if verpasst:
        raise SystemExit(f"FEHLER: {len(verpasst)} belegte Karten ohne ★")

    genutzt = set()
    for k in karten:
        if k["stufe"] == "belegt":
            genutzt |= fundstellen(k["quelle"]) & positiv
    return {
        "karten": len(karten),
        "belegt": sum(1 for k in karten if k["stufe"] == "belegt"),
        "verwandt": sum(1 for k in karten if k["stufe"] == "verwandt"),
        "marker_gesamt": len(positiv),
        "marker_ohne_karte": sorted(positiv - genutzt),
    }
