#!/usr/bin/env python3
"""
Erzeugt die Bewerbungsunterlagen für die Stelle
"Werkstudent AI Adoption & Enablement (w/m/d)" bei PwC Deutschland.

Quelle des Inhalts: bewerbungen/pwc-ai-adoption/{lebenslauf,anschreiben}.md
Ausgabe:            output/Lebenslauf_Pouya_Shakourpour_PwC.docx
                    output/Anschreiben_Pouya_Shakourpour_PwC.docx

Aufruf: python3 scripts/build_pwc.py
"""
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, RGBColor

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)

AKZENT = RGBColor(0x1F, 0x3B, 0x57)

PERSON = {
    "name": "Pouya Shakourpour",
    "untertitel": "B.Eng. Wirtschaftsingenieurwesen (HTW Berlin)",
    "kontakt": "Scheffelstr. 45, 10367 Berlin  |  0176 80782540  |  pouyapouya144@gmail.com",
}

KURZPROFIL = (
    "Wirtschaftsingenieurwesen-Student mit abgeschlossener kaufmännischer Ausbildung. Arbeite seit "
    "Dezember 2025 in der Qualitätssicherung eines Bahnbau-Softwarehauses und bereite dort technische "
    "Inhalte so auf, dass Fachanwender ohne Software-Hintergrund damit arbeiten können. KI-Tools setze "
    "ich dabei täglich ein – für Recherche, Strukturierung und die Automatisierung wiederkehrender "
    "Dokumente."
)

ERFAHRUNG = [
    {
        "titel": "Werkstudent Qualitätssicherung – Bahnbau",
        "firma": "AKG Software Consulting GmbH, Berlin",
        "zeit": "12/2025 – heute",
        "bullets": [
            "Produktdokumentation für zwei Softwareprodukte der Bahnplanung (Vestra-Infravision) "
            "gepflegt und überarbeitet, damit Fachanwender neue Funktionen ohne Rückfrage an die "
            "Entwicklung einsetzen können",
            "Test und Abnahme neuer Softwarefunktionen sowie strukturierte Dokumentation und "
            "Nachverfolgung identifizierter Qualitätsabweichungen (Azure DevOps Server)",
            "Technische Produktinformationen für Fachabteilungen verdichtet und als "
            "Entscheidungsgrundlage aufbereitet",
            "Anforderungen und technische Inhalte abteilungsübergreifend zwischen Entwicklung und "
            "Fachbereich abgestimmt",
            "KI-Tools zur Aufbereitung von Produktinformationen eingesetzt und daraus "
            "wiederverwendbare Prompt-Vorlagen für die laufende Dokumentationsarbeit entwickelt",
        ],
    },
    {
        "titel": "Werkstudent Projektkoordination & Vertrieb",
        "firma": "Schiller-Eventpersonal GmbH, Berlin",
        "zeit": "04/2025 – 11/2025",
        "bullets": [
            "Kunden- und Mitarbeiterdaten aus zwei Altsystemen in ein zentrales CRM migriert und "
            "dabei gewachsene Datenstrukturen vereinheitlicht – Fehlerquote und Bearbeitungszeiten "
            "gingen spürbar zurück",
            "Markt- und Wettbewerbsinformationen recherchiert und zu Entscheidungsvorlagen für die "
            "Geschäftsführung verdichtet",
            "Präsentationen für die Geschäftsführung erstellt, von der Argumentationslinie bis zum "
            "fertigen Foliensatz",
            "Personaleinsatz für Eventprojekte geplant und koordiniert, inklusive Abstimmung mit "
            "Kunden und Personal",
        ],
    },
    {
        "titel": "Kaufmann – Produktportfolio & Vertrieb B2B",
        "firma": "Muffenrohr Tiefbauhandel GmbH, Berlin",
        "zeit": "07/2024 – 09/2024",
        "bullets": [
            "Prozessoptimierung im dezentralen Einkauf unterstützt: neue Analyse-Tools eingeführt "
            "und wiederkehrende Abläufe standardisiert",
            "Produkt- und Marktdaten täglich in SAP ausgewertet und zu Kennzahlen für die "
            "Vertriebssteuerung aufbereitet",
            "Bestands- und Statusübersichten aufgebaut, die den Stand des Produktportfolios "
            "abteilungsübergreifend transparent machten",
            "Lieferkoordination zwischen Vertrieb, Lager und Einkauf für termingerechte "
            "Auftragsabwicklung",
        ],
    },
]

AUSBILDUNG = [
    {
        "titel": "B.Eng. Wirtschaftsingenieurwesen",
        "firma": "HTW Berlin",
        "zeit": "seit 10/2024",
        "bullets": [
            "Relevante Module: Projektmanagement, Controlling, Produkt- und Prozessgestaltung, "
            "Lean Management",
            "Fachlicher Austausch mit Siemens Mobility über Prof. Böttger (ehem. Siemens Mobility)",
        ],
    },
    {
        "titel": "Kaufmann im Groß- und Außenhandelsmanagement",
        "firma": "Muffenrohr Tiefbauhandel GmbH, Berlin",
        "zeit": "08/2021 – 06/2024  |  Ø 1,7",
        "bullets": [
            "Doppelqualifizierung: Ausbildung und Fachhochschulreife parallel (FOS Ø 1,6)",
            "Stationen: zwei Jahre Vertrieb, je sechs Monate Lager und Einkauf",
            "B2B-Projektabwicklung und Lieferantenkoordination im Baustoffgroßhandel",
        ],
    },
]

WEITERBILDUNG = [
    {
        "titel": "Summer School Künstliche Intelligenz",
        "firma": "Zürich",
        "zeit": "2026",
        "bullets": [
            "Aktuelle KI-Entwicklungen, Austausch mit Forschenden, praxisnahe Workshops",
        ],
    },
]

SKILLS = [
    ("KI & Automatisierung", [
        "ChatGPT und Claude im täglichen Arbeitseinsatz: strukturierte Prompts, wiederverwendbare Vorlagen",
        "KI-gestützte Recherche und Datenaufbereitung",
        "Automatisierung von Berichtsvorlagen und Erstellung von Präsentationen",
    ]),
    ("Weitere Tools", [
        "Sehr gut: PowerPoint, Excel, Word, SAP",
        "Gut: Power BI, Python, SQL, Asana",
        "Projekt & Dokumentation: Azure DevOps Server, Vestra-Infravision (Bahnbau)",
    ]),
    ("Sprachen", [
        "Deutsch (Muttersprache), Persisch (Muttersprache), Englisch (fließend, B2)",
    ]),
]

ANSCHREIBEN_ABSAETZE = [
    "seit Dezember pflege ich bei einem Softwarehaus die Produktdokumentation für eine "
    "Bahnbausoftware. Die Nutzer sind Planungsingenieure, die Gleistrassen entwerfen und sich für "
    "Software genau so weit interessieren, wie sie ihnen Arbeit abnimmt. Der schwierige Teil ist dort "
    "nie die Funktion selbst, sondern die Frage, wie man sie beschreibt, damit jemand sie am Montag "
    "tatsächlich benutzt. Bei AI stellt sich dieselbe Frage, nur mit deutlich mehr Skepsis auf der "
    "anderen Seite. Dass Ihre Stelle genau dort ansetzt und nicht beim reinen Ausrollen von Tools, "
    "ist der Grund für meine Bewerbung.",

    "Zwei Erfahrungen haben mich dahin gebracht. Während meiner Ausbildung im Baustoffgroßhandel habe "
    "ich im dezentralen Einkauf neue Analyse-Tools eingeführt und Abläufe standardisiert. Gelernt "
    "habe ich dabei vor allem, dass ein Werkzeug nicht genutzt wird, weil es besser ist, sondern wenn "
    "jemand konkret zeigt, welchen Handgriff es erspart. Später habe ich bei einem "
    "Eventpersonaldienstleister Kunden- und Mitarbeiterdaten aus zwei Altsystemen in ein zentrales "
    "CRM überführt. Die Migration war technisch überschaubar; der eigentliche Aufwand lag darin, "
    "gewachsene Datenstrukturen zu vereinheitlichen und dafür zu sorgen, dass am Ende alle im neuen "
    "System arbeiten konnten.",

    "KI-Tools nutze ich nicht nebenbei, sondern als Teil meiner Arbeitsweise: Ich strukturiere damit "
    "Recherchen, baue mir Vorlagen für wiederkehrende Berichte und entwickle Präsentationsgerüste. "
    "In wenigen Wochen nehme ich an einer Summer School in Zürich teil, um mich intensiver mit "
    "aktuellen KI-Entwicklungen und der Forschung dahinter auseinanderzusetzen.",

    "Was ich mitbringe, ist die Kombination aus kaufmännischer Ausbildung und "
    "Wirtschaftsingenieurwesen. Ich kann mit Fachabteilungen sprechen, ohne technische Inhalte zu "
    "verwässern, und umgekehrt technische Themen einordnen, ohne den betriebswirtschaftlichen Nutzen "
    "aus dem Blick zu verlieren. Für Enablement-Formate, die in einer großen Organisation wirklich "
    "ankommen sollen, halte ich das für die nützlichere Voraussetzung als reine Tool-Kenntnis.",

    "Über ein Gespräch freue ich mich.",
]


# ---------------------------------------------------------------------------
# Bausteine
# ---------------------------------------------------------------------------
def basis_dokument() -> Document:
    doc = Document()
    normal = doc.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(10.5)
    normal.paragraph_format.space_after = Pt(4)
    for section in doc.sections:
        section.top_margin = section.bottom_margin = Pt(48)
        section.left_margin = section.right_margin = Pt(56)
    return doc


def absatz(doc, text, *, size=10.5, bold=False, color=None, space_before=0, space_after=4,
           align=None, italic=False):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    if color is not None:
        run.font.color.rgb = color
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    if align is not None:
        p.alignment = align
    return p


def rubrik(doc, text):
    absatz(doc, text.upper(), size=11, bold=True, color=AKZENT, space_before=12, space_after=4)


def eintrag(doc, item):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run(item["titel"])
    run.bold = True
    run.font.size = Pt(10.5)

    absatz(doc, f'{item["firma"]}  |  {item["zeit"]}', size=9.5, italic=True, space_after=2)

    for text in item["bullets"]:
        b = doc.add_paragraph(text, style="List Bullet")
        b.paragraph_format.space_after = Pt(2)
        for run in b.runs:
            run.font.size = Pt(10.5)


# ---------------------------------------------------------------------------
# Dokumente
# ---------------------------------------------------------------------------
def build_lebenslauf(pfad: Path):
    doc = basis_dokument()

    absatz(doc, PERSON["name"], size=20, bold=True, color=AKZENT, space_after=1)
    absatz(doc, PERSON["untertitel"], size=11, space_after=1)
    absatz(doc, PERSON["kontakt"], size=9.5, space_after=6)

    rubrik(doc, "Kurzprofil")
    absatz(doc, KURZPROFIL, align=WD_ALIGN_PARAGRAPH.JUSTIFY)

    rubrik(doc, "Berufserfahrung")
    for item in ERFAHRUNG:
        eintrag(doc, item)

    rubrik(doc, "Ausbildung")
    for item in AUSBILDUNG:
        eintrag(doc, item)

    rubrik(doc, "Weiterbildung")
    for item in WEITERBILDUNG:
        eintrag(doc, item)

    for titel, zeilen in SKILLS:
        rubrik(doc, titel)
        for zeile in zeilen:
            b = doc.add_paragraph(zeile, style="List Bullet")
            b.paragraph_format.space_after = Pt(2)
            for run in b.runs:
                run.font.size = Pt(10.5)

    doc.save(pfad)
    print(f"geschrieben: {pfad.relative_to(ROOT)}")


def build_anschreiben(pfad: Path):
    doc = basis_dokument()

    absatz(doc, PERSON["name"], size=14, bold=True, color=AKZENT, space_after=1)
    for zeile in ["Scheffelstr. 45", "10367 Berlin", "0176 80782540", "pouyapouya144@gmail.com"]:
        absatz(doc, zeile, size=10, space_after=0)

    absatz(doc, "PwC Deutschland", size=10.5, space_before=18, space_after=0)
    absatz(doc, "Business Services – Products & Technology", size=10.5, space_after=0)

    absatz(doc, "Berlin, {{DATUM}}", size=10.5, space_before=18, space_after=14,
           align=WD_ALIGN_PARAGRAPH.RIGHT)

    absatz(doc, "Bewerbung als Werkstudent AI Adoption & Enablement (w/m/d)",
           size=11.5, bold=True, space_after=12)

    absatz(doc, "Sehr geehrte Damen und Herren,", space_after=10)

    for text in ANSCHREIBEN_ABSAETZE:
        absatz(doc, text, space_after=10, align=WD_ALIGN_PARAGRAPH.JUSTIFY)

    absatz(doc, "Mit freundlichen Grüßen", space_before=6, space_after=24)
    absatz(doc, PERSON["name"])

    doc.save(pfad)
    print(f"geschrieben: {pfad.relative_to(ROOT)}")


if __name__ == "__main__":
    build_lebenslauf(OUT / "Lebenslauf_Pouya_Shakourpour_PwC.docx")
    build_anschreiben(OUT / "Anschreiben_Pouya_Shakourpour_PwC.docx")
