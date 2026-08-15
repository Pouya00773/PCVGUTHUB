#!/usr/bin/env python3
"""
Erzeugt die Bewerbungsunterlagen für die Stelle
"Praktikum / Werkstudent Quality Assurance Specialist – Public Sector & Energy (w/m/d)"
bei PwC Deutschland (Geschäftsbereich Transformation, Berlin, Req. 2512).

Quelle des Inhalts: bewerbungen/pwc-qa-public-sector-energy/{lebenslauf,anschreiben}.md
Ausgabe:            output/Lebenslauf_Pouya_Shakourpour_PwC_QA.docx
                    output/Anschreiben_Pouya_Shakourpour_PwC_QA.docx

ATS-Mechanik: einspaltig, keine Tabellen/Textboxen/Grafiken/Kopfzeilen, Standardüberschriften,
Kontaktdaten als Fließtext, Daten durchgehend MM/JJJJ.

Aufruf: python3 scripts/build_pwc_qa.py
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
    "untertitel": "B.Eng. Wirtschaftsingenieurwesen (HTW Berlin)  |  "
                  "Qualitätssicherung und Softwaretest",
    "adresse": ["Scheffelstr. 45", "10367 Berlin", "0176 80782540", "pouyapouya144@gmail.com"],
    "kontakt": "Scheffelstr. 45, 10367 Berlin  |  0176 80782540  |  pouyapouya144@gmail.com",
}

KURZPROFIL = (
    "Student des Wirtschaftsingenieurwesens mit abgeschlossener kaufmännischer Ausbildung, seit "
    "Dezember 2025 Werkstudent in der Qualitätssicherung eines Softwarehauses für Bahnplanung: Test "
    "und Abnahme neuer Funktionen, reproduzierbare Fehlerdokumentation und -nachverfolgung in Azure "
    "DevOps Server sowie Prüfung und Pflege der Produktdokumentation. Grundkenntnisse in Python, SQL "
    "und C#. Nächster Schritt ist der Weg vom manuellen zum automatisierten Testen."
)

ERFAHRUNG = [
    {
        "titel": "Werkstudent Qualitätssicherung (Quality Assurance) – Bahnbau",
        "firma": "AKG Software Consulting GmbH, Berlin",
        "zeit": "12/2025 – heute",
        "bullets": [
            "Test und Abnahme neuer Softwarefunktionen für zwei Produkte der Bahnplanung "
            "(Vestra-Infravision), einschließlich Prüfung von Ausnahme- und Randfällen",
            "Abweichungen reproduzierbar beschrieben, in Azure DevOps Server dokumentiert und bis "
            "zur Klärung mit der Entwicklung nachverfolgt",
            "Produktdokumentation für zwei Softwareprodukte gepflegt und überarbeitet – geprüft auf "
            "Vollständigkeit, Konsistenz und Verständlichkeit für Fachanwender ohne "
            "Software-Hintergrund",
            "Anforderungen und technische Inhalte zwischen Entwicklung und Fachbereich abgestimmt, "
            "offene Punkte nachgehalten",
            "KI-gestützte Aufbereitung von Produktinformationen eingeführt und wiederverwendbare "
            "Vorlagen für die laufende Dokumentationsarbeit entwickelt",
        ],
    },
    {
        "titel": "Werkstudent Projektkoordination & Vertrieb",
        "firma": "Schiller-Eventpersonal GmbH, Berlin",
        "zeit": "04/2025 – 11/2025",
        "bullets": [
            "Kunden- und Mitarbeiterdaten aus zwei Altsystemen in ein zentrales CRM migriert, "
            "Datenbestände bereinigt und Strukturen vereinheitlicht – Fehlerquote und "
            "Bearbeitungszeiten gingen spürbar zurück",
            "Markt- und Wettbewerbsinformationen recherchiert, auf Plausibilität geprüft und zu "
            "Entscheidungsvorlagen für die Geschäftsführung verdichtet",
            "Präsentationen für die Geschäftsführung erstellt, von der Argumentationslinie bis zum "
            "fertigen Foliensatz",
            "Personaleinsatz für Eventprojekte geplant und koordiniert, Termine und "
            "Zuständigkeiten nachgehalten",
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
            "SAP-gestützte Angebots- und Auftragserfassung im B2B-Geschäft mit Tiefbauunternehmen",
        ],
    },
]

AUSBILDUNG = [
    {
        "titel": "B.Eng. Wirtschaftsingenieurwesen",
        "firma": "HTW Berlin",
        "zeit": "seit 10/2024",
        "bullets": [
            "Relevante Module: Projektmanagement, Produkt- und Prozessgestaltung, Lean Management, "
            "Controlling",
            "Fachlicher Austausch mit Siemens Mobility über Prof. Böttger (ehem. Siemens Mobility)",
        ],
    },
    {
        "titel": "Kaufmann im Groß- und Außenhandelsmanagement",
        "firma": "Muffenrohr Tiefbauhandel GmbH, Berlin",
        "zeit": "08/2021 – 06/2024  |  Abschlussnote 1,7",
        "bullets": [
            "Doppelqualifizierung: Berufsausbildung und Fachhochschulreife parallel "
            "(Fachoberschule, Note 1,6)",
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

KENNTNISSE = [
    ("Qualitätssicherung und Test",
     "Test und Abnahme von Softwarefunktionen, Prüfung von Ausnahme- und Randfällen, "
     "reproduzierbares Fehlerreporting, Fehlernachverfolgung, Testdokumentation, technische "
     "Produktdokumentation, Prozessstandardisierung"),
    ("Tools",
     "Azure DevOps Server (Testdurchführung und Fehlernachverfolgung); SAP und MS Office (Excel, "
     "PowerPoint, Word) – sehr gut; Asana; Vestra-Infravision (Bahnplanung)"),
    ("Programmierung und Daten",
     "Python, SQL, C# – Grundkenntnisse; Power BI"),
    ("KI-Anwendungen",
     "ChatGPT und Claude: strukturierte Prompts, KI-gestützte Recherche und Datenaufbereitung, "
     "Automatisierung von Berichtsvorlagen"),
]

SPRACHEN = "Deutsch (Muttersprache), Persisch (Muttersprache), Englisch (fließend, B2)"

ANSCHREIBEN_BETREFF = (
    "Bewerbung als Werkstudent Quality Assurance Specialist – Public Sector & Energy (w/m/d)"
)

ANSCHREIBEN_ABSAETZE = [
    "die Software, die ich seit Dezember teste, nutzen Planungsingenieure für Bahntrassen. "
    "Öffentliche Auftraggeber, Infrastruktur, Mobilität – das ist ungefähr das Themenfeld, in dem "
    "Ihr PET AI Tech-Hub arbeitet, nur von der Softwareseite statt aus der Beratung. "
    "Qualitätssicherung mache ich also bereits; ich würde sie gern dort machen, wo die Ergebnisse "
    "in Digitalisierungs- und Energieprojekten der öffentlichen Hand landen.",

    "Mein Tagesgeschäft ist Test und Abnahme neuer Funktionen für zwei Produkte. Abweichungen "
    "beschreibe ich so, dass die Entwicklung sie reproduzieren kann, dokumentiere sie in Azure "
    "DevOps und halte sie nach, bis sie geklärt sind – Jira und TestRail bilden denselben Ablauf "
    "ab. Ihr Punkt zu den Unlucky Paths beschreibt dabei ziemlich genau, was den Reiz an der Arbeit "
    "ausmacht: Auf dem erwarteten Weg funktioniert fast alles. Interessant wird es bei der "
    "Trassenführung mit ungewöhnlicher Geometrie, dem unvollständigen Datensatz, der Eingabe, an "
    "die beim Entwurf niemand gedacht hat. Diese Fälle zu suchen, liegt mir.",

    "Zum Stand der Automatisierung sage ich lieber, wie es ist: Ich teste heute manuell. Mit "
    "Selenium oder Cypress habe ich noch nicht produktiv gearbeitet, Python und C# beherrsche ich "
    "auf Grundlagenniveau. Was ich mitbringe, ist das Handwerk dahinter – Testfälle durchdenken, "
    "Fehler sauber belegen, Ergebnisse nachvollziehbar dokumentieren – und das wende ich täglich "
    "an. Den Schritt zum automatisierten Testen möchte ich als Nächstes gehen, und dafür ist ein "
    "cross-funktionales Team mit echten Projekten der bessere Ort als ein Onlinekurs.",

    "Dazu kommt ein Hintergrund, den in einem Testteam nicht alle haben: kaufmännische Ausbildung, "
    "drei Jahre Baustoffgroßhandel für Tiefbauunternehmen, jetzt Wirtschaftsingenieurwesen. Ich "
    "kenne die Projekte, für die solche Software am Ende gebaut wird – das hilft beim Testen "
    "fachlicher Randfälle mehr als jede zusätzliche Toolkenntnis.",

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


def bullet(doc, text):
    b = doc.add_paragraph(text, style="List Bullet")
    b.paragraph_format.space_after = Pt(2)
    for run in b.runs:
        run.font.size = Pt(10.5)
    return b


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
        bullet(doc, text)


# ---------------------------------------------------------------------------
# Dokumente
# ---------------------------------------------------------------------------
def build_lebenslauf(pfad: Path):
    doc = basis_dokument()

    absatz(doc, PERSON["name"], size=20, bold=True, color=AKZENT, space_after=1)
    absatz(doc, PERSON["untertitel"], size=10.5, space_after=1)
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

    rubrik(doc, "Kenntnisse")
    for titel, inhalt in KENNTNISSE:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_after = Pt(2)
        r1 = p.add_run(f"{titel}: ")
        r1.bold = True
        r1.font.size = Pt(10.5)
        r2 = p.add_run(inhalt)
        r2.font.size = Pt(10.5)

    rubrik(doc, "Sprachen")
    absatz(doc, SPRACHEN)

    doc.save(pfad)
    print(f"geschrieben: {pfad.relative_to(ROOT)}")


def build_anschreiben(pfad: Path):
    doc = basis_dokument()

    absatz(doc, PERSON["name"], size=14, bold=True, color=AKZENT, space_after=1)
    for zeile in PERSON["adresse"]:
        absatz(doc, zeile, size=10, space_after=0)

    absatz(doc, "PwC Deutschland", size=10.5, space_before=18, space_after=0)
    absatz(doc, "Geschäftsbereich Transformation – Public & Energy Transformation", size=10.5, space_after=0)
    absatz(doc, "Berlin", size=10.5, space_after=0)

    absatz(doc, "Berlin, {{DATUM}}", size=10.5, space_before=18, space_after=14,
           align=WD_ALIGN_PARAGRAPH.RIGHT)

    absatz(doc, ANSCHREIBEN_BETREFF, size=11.5, bold=True, space_after=2)
    absatz(doc, "Referenz 2512", size=10, space_after=12)

    absatz(doc, "Sehr geehrte Damen und Herren,", space_after=10)

    for text in ANSCHREIBEN_ABSAETZE:
        absatz(doc, text, space_after=10, align=WD_ALIGN_PARAGRAPH.JUSTIFY)

    absatz(doc, "Mit freundlichen Grüßen", space_before=6, space_after=24)
    absatz(doc, PERSON["name"])

    doc.save(pfad)
    print(f"geschrieben: {pfad.relative_to(ROOT)}")


if __name__ == "__main__":
    build_lebenslauf(OUT / "Lebenslauf_Pouya_Shakourpour_PwC_QA.docx")
    build_anschreiben(OUT / "Anschreiben_Pouya_Shakourpour_PwC_QA.docx")
