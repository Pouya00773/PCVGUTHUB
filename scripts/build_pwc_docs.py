#!/usr/bin/env python3
"""
Erzeugt die ATS-optimierten Bewerbungsunterlagen für die konkrete Stelle:

    PwC Deutschland – Werkstudent/Praktikant Quality Assurance Specialist
    Public Sector & Energy (w/m/d) | Team "PET AI Tech-Hub"

Ausgabe:
- output/Lebenslauf_PwC_QA.docx
- output/Anschreiben_PwC_QA.docx

Design-Prinzipien (ATS-sicher, identisch zu scripts/build_docs.py):
- einspaltig, Standard-Überschriften, Kontaktdaten als reiner Text
- keine Tabellen/Textboxen/Kopfzeilen für Inhalte, keine Grafiken
- Wortlaut der Anzeige gespiegelt (Testmanagement, Testautomatisierung, Edge Cases ...)
- Leitplanke: nur ehrliche Angaben. Noch nicht Praxiserprobtes steht ausschließlich
  im Block "In Aneignung" und ist dort klar als solches gekennzeichnet.

Aufruf:  python3 scripts/build_pwc_docs.py
"""
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor

OUT = Path(__file__).resolve().parent.parent / "output"
OUT.mkdir(exist_ok=True)

# ---------------------------------------------------------------------------
# DATEN – hier bei Bedarf anpassen
# ---------------------------------------------------------------------------
PERSON = {
    "name": "{{NAME}}",
    "untertitel": "Werkstudent Qualitätssicherung · B.Sc. Wirtschaftsingenieurwesen (HTW Berlin)",
    "kontakt": [
        "{{ANSCHRIFT}}",
        "Telefon: {{TELEFON}}",
        "E-Mail: pouyapouya144@gmail.com",
        "Geburtsdatum: {{GEBURT}}",
        "LinkedIn: {{LINKEDIN}}",
    ],
    # erscheint nur im Lebenslauf-Kopf
    "verfuegbarkeit": "Verfügbarkeit: {{STUNDEN}} Stunden/Woche ab {{STARTDATUM}}",
}

STELLE = {
    "titel": "Werkstudent Quality Assurance Specialist – Public Sector & Energy (w/m/d)",
    "firma": "PwC Deutschland",
    "bereich": "Public & Energy Transformation – Team „PET AI Tech-Hub“",
}

PROFIL = (
    "Werkstudent in der Software-Qualitätssicherung mit Praxis in Testplanung, Produktabnahme, "
    "manuellem Testing und strukturierter Fehler- und Testdokumentation. Erstellung von "
    "Testplänen in enger Zusammenarbeit mit dem Produktmanagement – im agilen Umfeld, in Sprints "
    "und "
    "mit Azure DevOps (Test Plans, Boards, Repos) als Testmanagement- und Tracking-Umgebung. "
    "Studium des "
    "Wirtschaftsingenieurwesens an der HTW Berlin mit abgeschlossener kaufmännischer Ausbildung – "
    "dadurch die Brücke zwischen Business, Technologie und Beratung, wie sie in cross-funktionalen "
    "Teams gebraucht wird. Ausgeprägte Detailorientierung, systematisches Denken in Edge Cases und "
    "Ausnahmefällen sowie klares, nachvollziehbares Fehlerreporting. Testautomatisierung "
    "(Selenium, Cypress, JUnit) sowie API- und Performance-Tests werden aktuell im Selbststudium "
    "aufgebaut (Details siehe Abschnitt „Kenntnisse & Fähigkeiten“)."
)

ERFAHRUNG = [
    {
        "titel": "Werkstudent Qualitätssicherung (Produktabnahme)",
        "firma": "AKG Software Consulting GmbH, Berlin",
        "zeit": "12/2025 – heute",
        "bullets": [
            "Erstellung von Testplänen in enger Zusammenarbeit mit dem Produktmanagement – "
            "Ableitung von Testumfang, Testszenarien und Abnahmekriterien aus den "
            "Produktanforderungen",
            "Planung und Durchführung manueller Softwaretests in der Produktabnahme – von "
            "Testfallentwurf über Ausführung bis zur Abnahmeempfehlung; Verwaltung der "
            "Testfälle und Testläufe in Azure DevOps Test Plans",
            "Systematische Analyse von Edge Cases und Ausnahmefällen („Unlucky Paths“) "
            "über die fachlich erwarteten Standardabläufe hinaus",
            "Reproduzierbare Fehlererfassung, Priorisierung und Nachverfolgung bis zum Retest "
            "in Azure DevOps – inklusive Verifizierung behobener Fehler und versionsgenauer "
            "Zuordnung über Git / Azure Repos",
            "Erstellung strukturierter Test- und Projektdokumentation als Nachweis der "
            "Softwarequalität über alle Entwicklungsphasen",
            "Arbeit im agilen Umfeld in Sprints – enge teamübergreifende Abstimmung mit "
            "Entwicklungs- und Produktteams zu Anforderungen, Fehlerbildern und "
            "Abnahmekriterien entlang des Sprint-Zyklus",
        ],
    },
    {
        "titel": "Werkstudent Vertrieb & HR",
        "firma": "Schiller-Eventpersonal GmbH, Berlin",
        "zeit": "04/2025 – 11/2025",
        "bullets": [
            "Betreuung von Bestandskunden und eigenständige Neukundenakquise",
            "Durchführung von Vorstellungsgesprächen sowie Vertragsbearbeitung",
            "Schnittstellenrolle zwischen Kunden, Bewerbenden und Einsatzplanung – "
            "adressatengerechte Kommunikation komplexer Sachverhalte",
        ],
    },
    {
        "titel": "Kaufmann im Groß- und Außenhandelsmanagement (Vertrieb / Kasse)",
        "firma": "Muffenrohr Tiefbauhandel GmbH, Berlin",
        "zeit": "07/2024 – 09/2024",
        "bullets": [
            "Angebotsbearbeitung und Auftragsabwicklung im Vertrieb",
            "Kassenführung und Abrechnung mit Nachweispflicht – sorgfältiges, "
            "fehlerfreies Arbeiten unter Zeitdruck",
        ],
    },
]

AUSBILDUNG = [
    {
        "titel": "B.Sc. Wirtschaftsingenieurwesen",
        "firma": "HTW Berlin – Hochschule für Technik und Wirtschaft",
        "zeit": "seit 10/2024",
        "bullets": [
            "Schwerpunkte: Informationstechnik, Prozesse und Betriebswirtschaft",
            "Programmierung (Python, C#), Datenbanken/SQL sowie Prozess- und "
            "Qualitätsmanagement als Studieninhalte",
        ],
    },
    {
        "titel": "Ausbildung Kaufmann im Groß- und Außenhandelsmanagement "
        "(Schwerpunkt Großhandel) mit Fachhochschulreife",
        "firma": "Muffenrohr Tiefbauhandel GmbH, Berlin",
        "zeit": "08/2021 – 06/2024",
        "bullets": [
            "Abschlussnoten: Fachhochschulreife 1,6 · Ausbildung 1,7",
            "Stationen: Vertrieb (2 Jahre), Lager (6 Monate), Einkauf/Beschaffung, Buchhaltung",
        ],
    },
    {
        "titel": "Mittlerer Schulabschluss (MSA) mit gymnasialer Empfehlung",
        "firma": "Schule am Tierpark, Berlin",
        "zeit": "bis 2021",
        "bullets": [
            "Abschluss 1,7 · stellv. Schülersprecher, Klassensprecher, "
            "Koordinationsteam Schüler:innen-Haushalt 2020",
        ],
    },
]

# QA-/Test-Kompetenzen: praxiserprobt vs. ehrlich als "in Aneignung" gekennzeichnet
QA_PRAXIS = [
    "Testplanung und Testkonzeption",
    "Manuelles Testing & Produktabnahme",
    "Testfallentwurf und Testdurchführung",
    "Edge-Case-/Ausnahmefall-Analyse („Unlucky Paths“)",
    "Fehlererfassung, Priorisierung, Nachverfolgung und Retest",
    "Testmanagement mit Azure DevOps (Test Plans, Boards, Work Items)",
    "Agiles Arbeiten in Sprints (Scrum)",
    "Versionskontrolle mit Git / Azure Repos",
    "Test- und Projektdokumentation",
    "Zusammenarbeit mit Entwicklungs- und Produktteams",
]

QA_ANEIGNUNG = [
    "Testautomatisierung: Selenium, Cypress, JUnit",
    "API-Tests (Postman/REST), Performance- und Sicherheitstests (Grundlagen)",
    "Jira und TestRail (Umstieg von Azure DevOps, Grundlagen)",
    "Testen von KI-Modellen und datengetriebenen Systemen (Grundlagen)",
]

IT_PRAXIS = [
    "Azure DevOps (Test Plans, Boards, Repos)", "Git", "MS Excel", "MS PowerPoint",
    "MS Word", "SAP", "Asana", "CRM (Pipedrive, Zoho)",
]
IT_GRUND = ["Python", "SQL", "C#"]

SPRACHEN = [
    "Deutsch – muttersprachliches Niveau",
    "Englisch – fließend",
    "Persisch – Muttersprache",
]

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
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run(f"{titel} — {firma}")
    r.bold = True
    z = doc.add_paragraph()
    z.paragraph_format.space_after = Pt(2)
    zr = z.add_run(zeit)
    zr.italic = True
    zr.font.size = Pt(10)
    for b in bullets:
        bp = doc.add_paragraph(b, style="List Bullet")
        bp.paragraph_format.space_after = Pt(1)


def hinweis(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    r = p.add_run(text)
    r.italic = True
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(0x88, 0x88, 0x88)


# ---------------------------------------------------------------------------
# LEBENSLAUF
# ---------------------------------------------------------------------------
def build_cv():
    doc = Document()
    set_base_style(doc)

    h = doc.add_paragraph()
    h.paragraph_format.space_after = Pt(0)
    hr = h.add_run(PERSON["name"])
    hr.bold = True
    hr.font.size = Pt(20)

    sub = doc.add_paragraph()
    sub.paragraph_format.space_after = Pt(4)
    sr = sub.add_run(PERSON["untertitel"])
    sr.font.size = Pt(11)
    sr.italic = True

    for line in PERSON["kontakt"]:
        cp = doc.add_paragraph(line)
        cp.paragraph_format.space_after = Pt(0)

    vp = doc.add_paragraph(PERSON["verfuegbarkeit"])
    vp.paragraph_format.space_after = Pt(0)

    bew = doc.add_paragraph()
    bew.paragraph_format.space_before = Pt(6)
    br = bew.add_run(f"Bewerbung als: {STELLE['titel']} · {STELLE['bereich']}")
    br.bold = True
    br.font.size = Pt(10)

    heading(doc, "Profil")
    doc.add_paragraph(PROFIL)

    heading(doc, "Kenntnisse & Fähigkeiten – Qualitätssicherung und Testing")
    doc.add_paragraph("Praxiserprobt: " + ", ".join(QA_PRAXIS))
    doc.add_paragraph("Im Aufbau (Selbststudium): " + ", ".join(QA_ANEIGNUNG))

    heading(doc, "Berufserfahrung")
    for e in ERFAHRUNG:
        entry(doc, e["titel"], e["firma"], e["zeit"], e["bullets"])

    heading(doc, "Ausbildung")
    for e in AUSBILDUNG:
        entry(doc, e["titel"], e["firma"], e["zeit"], e["bullets"])

    heading(doc, "IT-Kenntnisse")
    doc.add_paragraph("Sicher: " + ", ".join(IT_PRAXIS))
    doc.add_paragraph("Grundkenntnisse: " + ", ".join(IT_GRUND))

    heading(doc, "Sprachen")
    for s in SPRACHEN:
        doc.add_paragraph(s, style="List Bullet")

    hinweis(
        doc,
        "HINWEIS (vor Versand löschen): Platzhalter {{...}} ersetzen und diese Zeile entfernen. "
        "Optional: konkrete Zahlen in die AKG-Bullets ergänzen (Testfälle pro Sprint, gemeldete "
        "Fehler, Teamgröße, betreute Module).",
    )

    path = OUT / "Lebenslauf_PwC_QA.docx"
    doc.save(path)
    return path


# ---------------------------------------------------------------------------
# ANSCHREIBEN
# ---------------------------------------------------------------------------
def build_cover_letter():
    doc = Document()
    set_base_style(doc)

    for line in [PERSON["name"]] + PERSON["kontakt"]:
        p = doc.add_paragraph(line)
        p.paragraph_format.space_after = Pt(0)

    doc.add_paragraph("")
    for line in [
        "PricewaterhouseCoopers GmbH",
        "Wirtschaftsprüfungsgesellschaft",
        "Public & Energy Transformation – PET AI Tech-Hub",
        "{{FIRMA_ADRESSE}}",
    ]:
        p = doc.add_paragraph(line)
        p.paragraph_format.space_after = Pt(0)

    doc.add_paragraph("")
    d = doc.add_paragraph("Berlin, {{DATUM}}")
    d.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    bt = doc.add_paragraph()
    bt.paragraph_format.space_after = Pt(10)
    btr = bt.add_run(
        "Bewerbung als Werkstudent Quality Assurance Specialist – "
        "Public Sector & Energy (w/m/d) | Referenz {{REFERENZ}}"
    )
    btr.bold = True

    absaetze = [
        "Sehr geehrte Damen und Herren,",

        "Software wird selten dort brüchig, wo alles nach Plan läuft, sondern in den Ausnahmen: "
        "im leeren Datensatz, im doppelten Klick, im Sonderfall, den niemand vorgesehen hat. Genau "
        "diese „Unlucky Paths“ zu finden, ist das, was ich seit Dezember 2025 als Werkstudent in "
        "der Qualitätssicherung bei der AKG Software Consulting GmbH täglich tue – und weshalb mich "
        "Ihre Ausschreibung im PET AI Tech-Hub unmittelbar angesprochen hat.",

        "In der Produktabnahme plane und führe ich manuelle Softwaretests durch: vom Testfallentwurf "
        "über die Ausführung bis zur Abnahmeempfehlung. Die Testpläne dazu erstelle ich in enger "
        "Zusammenarbeit mit unserem Produktmanager – aus den Produktanforderungen leiten wir "
        "gemeinsam Testumfang, Testszenarien und Abnahmekriterien ab. Meine Testfälle und "
        "Testläufe verwalte ich "
        "in Azure DevOps Test Plans, gefundene Fehler erfasse ich reproduzierbar, priorisiere sie "
        "und verfolge sie bis zum Retest nach – über Git beziehungsweise Azure Repos ordne ich sie "
        "dabei versionsgenau dem jeweiligen Codestand zu. Wir arbeiten in Sprints, sodass ich "
        "gewohnt bin, Testumfang und Abnahmekriterien eng am Entwicklungszyklus abzustimmen. Dabei "
        "habe ich gelernt, dass ein Fehlerbericht erst dann gut ist, wenn die Entwicklung ohne "
        "Rückfrage damit arbeiten kann – kommunikationsstarkes Fehlerreporting ist für mich kein "
        "Nebenprodukt, sondern Teil der Aufgabe.",

        "Mein Studium des Wirtschaftsingenieurwesens an der HTW Berlin bringt neben Programmierung "
        "(Python, C#) und Datenbanken vor allem eine zweite Perspektive mit: Ich denke Anforderungen "
        "von der fachlichen Seite her und übersetze zwischen Business und Technik. Für ein "
        "cross-funktionales Team, das gesellschaftliche Problemstellungen in Public Sector und "
        "Energy in reale Lösungen überführt, sehe ich darin einen echten Mehrwert. Offen sage ich "
        "auch, wo ich stehe: Testautomatisierung mit Selenium, Cypress und JUnit sowie API- und "
        "Performance-Tests baue ich derzeit gezielt im Selbststudium auf – strukturiert, mit eigenen "
        "kleinen Testprojekten und der klaren Absicht, das bei Ihnen in die Praxis zu bringen. Als "
        "Testmanagement-Umgebung nutze ich Azure DevOps; der Umstieg auf Jira oder TestRail ist für "
        "mich eine Frage von Tagen, nicht von Monaten – die Konzepte dahinter sind dieselben. "
        "Was ich sicher mitbringe, ist die Grundlage, auf "
        "der Automatisierung erst sinnvoll wird: systematisches Testdenken, Detailgenauigkeit und "
        "saubere Dokumentation.",

        "Die Verbindung aus Digitalisierung, Energiewende und öffentlichem Auftrag ist für mich der "
        "Bereich, in dem Qualitätssicherung am meisten zählt – dort trägt eine fehlerhafte Anwendung "
        "unmittelbar Konsequenzen für Menschen, die sie nicht umgehen können. Genau deshalb möchte "
        "ich meinen Weg in der Qualitätssicherung bei PwC weitergehen und dort deutlich tiefer "
        "einsteigen – insbesondere im Testen von KI-gestützten und datengetriebenen Systemen.",

        "Ab {{STARTDATUM}} stehe ich Ihnen mit {{STUNDEN}} Stunden pro Woche zur Verfügung, in der "
        "vorlesungsfreien Zeit gerne auch mit mehr. Über die Gelegenheit zu einem persönlichen "
        "Gespräch freue ich mich sehr.",

        "Mit freundlichen Grüßen",
        PERSON["name"],
    ]
    for a in absaetze:
        p = doc.add_paragraph(a)
        p.paragraph_format.space_after = Pt(8)

    hinweis(
        doc,
        "HINWEIS (vor Versand löschen): Platzhalter {{...}} ersetzen (Adresse des Standorts, auf den "
        "du dich bewirbst, Datum, Referenznummer aus der Anzeige) und diese Zeile entfernen.",
    )

    path = OUT / "Anschreiben_PwC_QA.docx"
    doc.save(path)
    return path


if __name__ == "__main__":
    created = [build_cv(), build_cover_letter()]
    print("Erstellt:")
    for p in created:
        print(" -", p)
