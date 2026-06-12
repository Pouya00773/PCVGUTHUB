#!/usr/bin/env python3
"""
Erzeugt ATS-/AI-Filter-freundliche Bewerbungsunterlagen (DOCX):
- 4 branchenspezifische Lebenslauf-Varianten
- 1 Anschreiben-Vorlage mit Platzhaltern

Design-Prinzipien (ATS-sicher):
- einspaltig, Standard-Überschriften, Kontaktdaten als Text
- keine Tabellen/Textboxen/Grafiken für Inhalte
- Aktiv-Verben + (wo möglich) quantifizierte Wirkung
- Leitplanke: nur ehrliche Angaben; Aufzubauendes ist als "(Grundkenntnisse)" markiert

Aufruf:  python3 scripts/build_docs.py
Ausgabe: output/Lebenslauf_<Branche>.docx, output/Anschreiben_Vorlage.docx
"""
from pathlib import Path
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = Path(__file__).resolve().parent.parent / "output"
OUT.mkdir(exist_ok=True)

# ---------------------------------------------------------------------------
# DATEN  (alles an EINER Stelle – hier bei Bedarf anpassen)
# ---------------------------------------------------------------------------
PERSON = {
    "name": "{{NAME}}",
    "untertitel": "B.Sc. Wirtschaftsingenieurwesen (HTW Berlin)",
    "kontakt": [
        "{{ANSCHRIFT}}",
        "Telefon: {{TELEFON}}",
        "E-Mail: {{EMAIL}}",
        "Geburtsdatum: {{GEBURT}}",
        "LinkedIn: {{LINKEDIN}}",
    ],
}

ERFAHRUNG = [
    {
        "titel": "Werkstudent Qualitätssicherung",
        "firma": "AKG Software Consulting GmbH, Berlin",
        "zeit": "12/2025 – heute",
        "bullets": [
            "Durchführung manueller Softwaretests in der Produktabnahme",
            "Systematische Erfassung, Dokumentation und Nachverfolgung von Fehlern",
            "Erstellung strukturierter Test- und Projektdokumentation zur Qualitätssicherung",
            "Enge Abstimmung mit der Entwicklung zur Verifizierung behobener Fehler",
        ],
    },
    {
        "titel": "Werkstudent Vertrieb & HR",
        "firma": "Schiller-Eventpersonal GmbH, Berlin",
        "zeit": "04/2025 – 11/2025",
        "bullets": [
            "Betreuung von Bestandskunden und eigenständige Neukundenakquise",
            "Durchführung von Vorstellungsgesprächen und Vertragsbearbeitung",
            "Schnittstelle zwischen Kunden, Bewerbern und Einsatzplanung",
        ],
    },
    {
        "titel": "Kaufmann Groß- & Außenhandel (Vertrieb/Kasse)",
        "firma": "Muffenrohr Tiefbauhandel GmbH",
        "zeit": "07/2024 – 09/2024",
        "bullets": [
            "Angebotsbearbeitung und Auftragsabwicklung im Vertrieb",
            "Kassenführung und Abrechnung",
        ],
    },
]

AUSBILDUNG = [
    {
        "titel": "B.Sc. Wirtschaftsingenieurwesen",
        "firma": "HTW Berlin – Hochschule für Technik und Wirtschaft",
        "zeit": "seit 10/2024",
        "bullets": [
            "Schwerpunkte: Prozesse, Technik und Betriebswirtschaft",
        ],
    },
    {
        "titel": "Ausbildung Kaufmann im Groß- & Außenhandel (Schwerpunkt Großhandel)",
        "firma": "Muffenrohr Tiefbauhandel GmbH – mit Fachhochschulreife",
        "zeit": "08/2021 – 06/2024",
        "bullets": [
            "Abschlussnoten: FOS 1,6 · Ausbildung 1,7",
            "Stationen: Vertrieb (2 J.), Lager (6 Mon.), Einkauf/Beschaffung, Buchhaltung",
        ],
    },
]

SPRACHEN = [
    "Deutsch – muttersprachliches Niveau",
    "Englisch – fließend",
    "Persisch – Muttersprache",
]

# Skills: ("Bezeichnung", praxiserprobt? True/False)  -> False wird als (Grundkenntnisse) markiert
SKILLS = {
    "praxis": [
        "MS Excel", "MS PowerPoint", "MS Word",
        "CRM (Pipedrive, Zoho)", "SAP", "Asana",
    ],
    "grund": [
        "SQL", "Python", "C#", "Power BI",
        "Lean Management / KVP / 5S",
    ],
}

# Branchen-spezifische Konfiguration
BRANCHEN = {
    "Industrie": {
        "profil": (
            "Wirtschaftsingenieur-Student mit kaufmännischer Ausbildung im Groß- und "
            "Außenhandel und erster Werkstudenten-Praxis in Qualitätssicherung und Vertrieb. "
            "Verbindet technisches Verständnis mit Prozess- und Zahlenaffinität – interessiert "
            "an Lean Management, Prozessoptimierung und Produktionsabläufen."
        ),
        "skills_order": ["grund", "praxis"],
    },
    "Pharma-MedTech": {
        "profil": (
            "Wirtschaftsingenieur-Student mit Erfahrung in Qualitätssicherung und strukturierter "
            "Dokumentation sowie kaufmännischem Hintergrund im Groß- und Außenhandel. Sorgfältige, "
            "prozessorientierte Arbeitsweise mit Interesse an Supply Chain und Qualitätsprozessen."
        ),
        "skills_order": ["praxis", "grund"],
    },
    "Consulting-Finance": {
        "profil": (
            "Analytisch denkender Wirtschaftsingenieur-Student (Abschlussnoten Ausbildung 1,7 / "
            "FOS 1,6) mit kaufmännischer Ausbildung und Werkstudenten-Praxis in Vertrieb und "
            "Qualitätssicherung. Kommunikationsstark, strukturiert und sicher in Excel & PowerPoint."
        ),
        "skills_order": ["praxis", "grund"],
    },
    "Tech-Konsum": {
        "profil": (
            "Wirtschaftsingenieur-Student mit kaufmännischem Hintergrund und Werkstudenten-Praxis "
            "in Qualitätssicherung und Vertrieb. Daten- und prozessaffin, mit Interesse an Supply "
            "Chain, Continuous Improvement und Automatisierung."
        ),
        "skills_order": ["grund", "praxis"],
    },
}

# ---------------------------------------------------------------------------
# FORMAT-HELFER
# ---------------------------------------------------------------------------
def set_base_style(doc):
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)
    style.paragraph_format.space_after = Pt(2)


def heading(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text.upper())
    run.bold = True
    run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(0x1F, 0x3B, 0x57)
    # dünne untere Linie (rein dekorativ, bleibt ATS-lesbar)
    pPr = p._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "2")
    bottom.set(qn("w:color"), "1F3B57")
    pbdr.append(bottom)
    pPr.append(pbdr)
    return p


def entry(doc, titel, firma, zeit, bullets):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    r = p.add_run(f"{titel} — {firma}")
    r.bold = True
    z = doc.add_paragraph()
    zr = z.add_run(zeit)
    zr.italic = True
    zr.font.size = Pt(10)
    for b in bullets:
        bp = doc.add_paragraph(b, style="List Bullet")
        bp.paragraph_format.space_after = Pt(1)


def skills_line(branch):
    order = BRANCHEN[branch]["skills_order"]
    parts = []
    for key in order:
        for s in SKILLS[key]:
            parts.append(s if key == "praxis" else f"{s} (Grundkenntnisse)")
    return parts


# ---------------------------------------------------------------------------
# DOKUMENTE
# ---------------------------------------------------------------------------
def build_cv(branch):
    doc = Document()
    set_base_style(doc)

    # Kopf
    h = doc.add_paragraph()
    hr = h.add_run(PERSON["name"])
    hr.bold = True
    hr.font.size = Pt(20)
    sub = doc.add_paragraph()
    sr = sub.add_run(PERSON["untertitel"])
    sr.font.size = Pt(11)
    sr.italic = True
    for line in PERSON["kontakt"]:
        cp = doc.add_paragraph(line)
        cp.paragraph_format.space_after = Pt(0)

    heading(doc, "Profil")
    doc.add_paragraph(BRANCHEN[branch]["profil"])

    heading(doc, "Berufserfahrung")
    for e in ERFAHRUNG:
        entry(doc, e["titel"], e["firma"], e["zeit"], e["bullets"])

    heading(doc, "Ausbildung")
    for e in AUSBILDUNG:
        entry(doc, e["titel"], e["firma"], e["zeit"], e["bullets"])

    heading(doc, "IT- & Methodenkenntnisse")
    doc.add_paragraph(" · ".join(skills_line(branch)))

    heading(doc, "Sprachen")
    for s in SPRACHEN:
        doc.add_paragraph(s, style="List Bullet")

    path = OUT / f"Lebenslauf_{branch}.docx"
    doc.save(path)
    return path


def build_cover_letter():
    doc = Document()
    set_base_style(doc)

    # Absender
    for line in [PERSON["name"]] + PERSON["kontakt"]:
        p = doc.add_paragraph(line)
        p.paragraph_format.space_after = Pt(0)
    doc.add_paragraph("")
    for line in ["{{FIRMA}}", "z. Hd. {{ANSPRECHPARTNER}}", "{{FIRMA_ADRESSE}}"]:
        p = doc.add_paragraph(line)
        p.paragraph_format.space_after = Pt(0)
    doc.add_paragraph("")
    d = doc.add_paragraph("Berlin, {{DATUM}}")
    d.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    bt = doc.add_paragraph()
    btr = bt.add_run("Bewerbung als Werkstudent {{ROLLE}} (m/w/d) – Referenz {{REFERENZ}}")
    btr.bold = True

    absaetze = [
        "Sehr geehrte Damen und Herren,",
        "mit großem Interesse habe ich Ihre Stellenausschreibung als Werkstudent {{ROLLE}} "
        "gelesen. Als Studierender des Wirtschaftsingenieurwesens an der HTW Berlin mit "
        "abgeschlossener kaufmännischer Ausbildung im Groß- und Außenhandel verbinde ich "
        "technisches Verständnis mit betriebswirtschaftlichem Denken – genau die Kombination, "
        "die {{FIRMA}} für diese Position sucht.",
        "In meiner aktuellen Werkstudententätigkeit in der Qualitätssicherung führe ich "
        "Softwaretests durch und erstelle strukturierte Dokumentationen; in einer vorherigen "
        "Rolle habe ich Kunden betreut und Prozesse im Vertrieb mitgestaltet. Dabei arbeite ich "
        "sorgfältig, eigenständig und lösungsorientiert. Mit MS Excel, SAP und CRM-Systemen "
        "arbeite ich routiniert; meine Kenntnisse in {{SKILL_FOKUS}} baue ich aktuell gezielt "
        "im Selbststudium weiter aus.",
        "Besonders reizt mich an {{FIRMA}} die Verbindung aus internationalem Umfeld und starker "
        "Präsenz in der Schweiz ({{CH_STANDORT}}). Ich plane ab April 2027 ein Auslandssemester "
        "in der Schweiz und sehe darin eine ideale Möglichkeit, mich langfristig und über Grenzen "
        "hinweg in Ihr Unternehmen einzubringen.",
        "Über die Gelegenheit zu einem persönlichen Gespräch freue ich mich sehr.",
        "Mit freundlichen Grüßen",
        PERSON["name"],
    ]
    for a in absaetze:
        p = doc.add_paragraph(a)
        p.paragraph_format.space_after = Pt(8)

    note = doc.add_paragraph()
    nr = note.add_run(
        "HINWEIS (vor Versand löschen): Platzhalter {{...}} ersetzen. "
        "{{SKILL_FOKUS}} = je nach Stelle z. B. SQL, Power BI oder Lean Management. "
        "Schweiz-Absatz nur lassen, wenn er zur Stelle passt."
    )
    nr.italic = True
    nr.font.size = Pt(9)
    nr.font.color.rgb = RGBColor(0x88, 0x88, 0x88)

    path = OUT / "Anschreiben_Vorlage.docx"
    doc.save(path)
    return path


if __name__ == "__main__":
    created = [build_cv(b) for b in BRANCHEN]
    created.append(build_cover_letter())
    print("Erstellt:")
    for p in created:
        print(" -", p)
