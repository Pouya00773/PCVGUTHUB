#!/usr/bin/env python3
"""
Erzeugt die Unterlagen für die Wohnungsbewerbung (DOCX):
- Mieter-Selbstauskunft (für die ImmoScout24-Bewerbermappe)
- Anschreiben-Vorlage mit 3 Varianten (Portal-Kurznachricht, Standard, mit Bürgschaft)
- Bewerbermappe-Deckblatt inkl. Dokumenten-Checkliste
- Anfrage-Text an den Arbeitgeber für die Arbeitgeberbescheinigung

Design-Prinzipien:
- Vermieter überfliegen in Sekunden -> kurz, gescannt lesbar, keine Textwüsten
- nur wahrheitsgemäße Angaben; unzulässige Vermieterfragen sind bewusst nicht enthalten
- alle personenbezogenen Daten als {{PLATZHALTER}}, damit nichts Sensibles ins Repo wandert

Aufruf:  python3 scripts/build_wohnungsbewerbung.py
Ausgabe: output/Mieter-Selbstauskunft.docx
         output/Wohnungs-Anschreiben_Vorlage.docx
         output/Bewerbermappe_Deckblatt.docx
         output/Arbeitgeberbescheinigung_Anfrage.docx
"""
import sys
from pathlib import Path

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_docs import set_base_style, heading  # noqa: E402  (gleicher Ordner)

OUT = Path(__file__).resolve().parent.parent / "output"
OUT.mkdir(exist_ok=True)

# ---------------------------------------------------------------------------
# DATEN  (alles an EINER Stelle – hier bei Bedarf anpassen)
# Echte Werte NICHT hier eintragen, solange das Repo öffentlich ist.
# ---------------------------------------------------------------------------
PERSON = {
    "name": "{{NAME}}",
    "geburtsdatum": "{{GEBURTSDATUM}}",
    "anschrift": "{{ANSCHRIFT}}",
    "telefon": "{{TELEFON}}",
    "email": "{{EMAIL}}",
    "staatsangehoerigkeit": "{{STAATSANGEHOERIGKEIT}}",
    "familienstand": "{{FAMILIENSTAND}}",
}

BERUF = {
    "taetigkeit": "Werkstudent Qualitätssicherung",
    "arbeitgeber": "AKG Software Consulting GmbH, Berlin",
    "seit": "12/2025",
    "studium": "B.Sc. Wirtschaftsingenieurwesen, HTW Berlin (seit 10/2024)",
    "netto": "{{NETTO_GESAMT}} €",
    "netto_details": "{{NETTO_WERKSTUDENT}} € Werkstudententätigkeit + {{NETTO_SONSTIGES}} € {{QUELLE_SONSTIGES}}",
    "wochenstunden": "{{WOCHENSTUNDEN}}",
    "befristung": "{{BEFRISTUNG}}",
}

BUERGE = {
    "name": "{{BUERGE_NAME}}",
    "verhaeltnis": "{{BUERGE_VERHAELTNIS}}",
    "beruf": "{{BUERGE_BERUF}}",
    "arbeitgeber": "{{BUERGE_ARBEITGEBER}}",
    "netto": "{{BUERGE_NETTO}} €",
}

# Checkliste der Bewerbermappe: (Dokument, Pflicht?, Hinweis)
DOKUMENTE = [
    ("Mieter-Selbstauskunft", True, "vollständig ausgefüllt und unterschrieben"),
    ("SCHUFA-BonitätsCheck", True, "nicht älter als 3 Monate; als SuchenPlus-Mitglied bis zu 40 % günstiger"),
    ("Gehaltsabrechnungen der letzten 3 Monate", True, "geschwärzt bis auf Netto-Betrag ist zulässig"),
    ("Arbeitgeberbescheinigung / Arbeitsvertrag", True, "belegt, dass die Anstellung fortbesteht"),
    ("Immatrikulationsbescheinigung", True, "aktuelles Semester, HTW Berlin"),
    ("Kopie des Personalausweises", True, "Ausweisnummer darf geschwärzt werden"),
    ("Bürgschaftserklärung der Eltern", True, "für Studierende in Berlin faktisch Pflicht"),
    ("Einkommensnachweise des Bürgen", True, "ohne diese ist die Bürgschaft für Vermieter wertlos"),
    ("SCHUFA-Auskunft des Bürgen", False, "stark empfohlen – hebt die Mappe deutlich ab"),
    ("Mietschuldenfreiheitsbescheinigung", False, "entfällt bei erster eigener Wohnung"),
]


# ---------------------------------------------------------------------------
# HILFSFUNKTIONEN
# ---------------------------------------------------------------------------
def feld(doc, label, wert):
    """Eine Zeile 'Label: Wert' – Label fett, ATS-/scanfreundlich."""
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(f"{label}: ")
    r.bold = True
    p.add_run(str(wert))
    return p


def hinweis(doc, text):
    """Grauer Kleingedruckt-Hinweis, der vor dem Versand gelöscht wird."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    r = p.add_run(text)
    r.italic = True
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(0x88, 0x88, 0x88)
    return p


def kopf(doc, titel, untertitel=None):
    h = doc.add_paragraph()
    hr = h.add_run(titel)
    hr.bold = True
    hr.font.size = Pt(18)
    if untertitel:
        s = doc.add_paragraph()
        sr = s.add_run(untertitel)
        sr.italic = True
        sr.font.size = Pt(11)


# ---------------------------------------------------------------------------
# DOKUMENTE
# ---------------------------------------------------------------------------
def build_selbstauskunft():
    doc = Document()
    set_base_style(doc)
    kopf(doc, "Mieter-Selbstauskunft", "Angaben zur Person und zu den wirtschaftlichen Verhältnissen")

    heading(doc, "Person")
    feld(doc, "Name, Vorname", PERSON["name"])
    feld(doc, "Geburtsdatum", PERSON["geburtsdatum"])
    feld(doc, "Aktuelle Anschrift", PERSON["anschrift"])
    feld(doc, "Telefon", PERSON["telefon"])
    feld(doc, "E-Mail", PERSON["email"])
    feld(doc, "Staatsangehörigkeit", PERSON["staatsangehoerigkeit"])
    feld(doc, "Familienstand", PERSON["familienstand"])
    feld(doc, "Anzahl einziehender Personen", "{{ANZAHL_PERSONEN}}")

    heading(doc, "Beruf und Einkommen")
    feld(doc, "Aktuelle Tätigkeit", BERUF["taetigkeit"])
    feld(doc, "Arbeitgeber", BERUF["arbeitgeber"])
    feld(doc, "Beschäftigt seit", BERUF["seit"])
    feld(doc, "Wochenstunden", BERUF["wochenstunden"])
    feld(doc, "Vertragsart", BERUF["befristung"])
    feld(doc, "Studium", BERUF["studium"])
    feld(doc, "Monatliches Nettoeinkommen (gesamt)", BERUF["netto"])
    feld(doc, "davon", BERUF["netto_details"])

    heading(doc, "Wirtschaftliche Verhältnisse")
    feld(doc, "Laufende Kredite oder Ratenzahlungen", "{{KREDITE}}")
    feld(doc, "Eidesstattliche Versicherung in den letzten 5 Jahren abgegeben", "nein")
    feld(doc, "Privatinsolvenzverfahren eröffnet oder beantragt", "nein")
    feld(doc, "Mietrückstände gegenüber bisherigen Vermietern", "nein")
    feld(doc, "Räumungsklage in den letzten 5 Jahren", "nein")

    heading(doc, "Bürgschaft")
    feld(doc, "Bürge", BUERGE["name"])
    feld(doc, "Verhältnis zum Mietinteressenten", BUERGE["verhaeltnis"])
    feld(doc, "Beruf", BUERGE["beruf"])
    feld(doc, "Arbeitgeber", BUERGE["arbeitgeber"])
    feld(doc, "Monatliches Nettoeinkommen des Bürgen", BUERGE["netto"])
    doc.add_paragraph(
        "Eine unterschriebene Bürgschaftserklärung sowie Einkommensnachweise und SCHUFA-Auskunft "
        "des Bürgen liegen dieser Bewerbung bei."
    )

    heading(doc, "Sonstiges")
    feld(doc, "Haustiere", "{{HAUSTIERE}}")
    feld(doc, "Raucher", "{{RAUCHER}}")
    feld(doc, "Musikinstrumente", "{{INSTRUMENTE}}")
    feld(doc, "Gewerbliche Nutzung der Wohnung geplant", "nein")
    feld(doc, "Gewünschter Einzugstermin", "{{EINZUGSTERMIN}}")

    heading(doc, "Bestätigung")
    doc.add_paragraph(
        "Ich versichere, dass die vorstehenden Angaben vollständig und wahrheitsgemäß sind. "
        "Mir ist bekannt, dass falsche Angaben den Vermieter zur Anfechtung oder Kündigung des "
        "Mietvertrages berechtigen können."
    )
    doc.add_paragraph("")
    doc.add_paragraph("Ort, Datum: ______________________     Unterschrift: ______________________")

    hinweis(
        doc,
        "HINWEIS (vor Versand löschen): Alle {{...}} ersetzen. Felder mit vorbelegtem 'nein' "
        "bitte prüfen – falsche Angaben hier können später zur Kündigung führen. "
        "Fragen nach Schwangerschaft, Religion, Partei-/Mieterverein-Zugehörigkeit, Herkunft, "
        "Krankheiten oder Heiratsabsicht sind unzulässig und wurden bewusst weggelassen; "
        "wenn ein Formular danach fragt, darfst du das Feld leer lassen.",
    )

    path = OUT / "Mieter-Selbstauskunft.docx"
    doc.save(path)
    return path


def build_anschreiben():
    doc = Document()
    set_base_style(doc)
    kopf(doc, "Wohnungsbewerbung – Textbausteine", "3 Varianten für unterschiedliche Situationen")

    # --- Variante 1 -------------------------------------------------------
    heading(doc, "Variante 1 – Portal-Kurznachricht (ImmoScout24-Kontaktformular)")
    doc.add_paragraph(
        "Für die erste Kontaktaufnahme im Portal. Bewusst kurz: Vermieter bekommen bei einem "
        "Berliner Inserat oft über 100 Nachrichten und lesen die ersten drei Zeilen. "
        "Ziel ist nur die Besichtigungseinladung, nicht die vollständige Selbstdarstellung."
    )
    for a in [
        "Sehr geehrte/r {{ANREDE}},",
        "hiermit bewerbe ich mich um die Wohnung in der {{STRASSE}} ({{OBJEKT_ID}}). "
        "Ich bin {{ALTER}} Jahre alt, studiere Wirtschaftsingenieurwesen an der HTW Berlin und "
        "arbeite fest angestellt als Werkstudent in der Qualitätssicherung bei der AKG Software "
        "Consulting GmbH.",
        "Meine Unterlagen sind vollständig und liegen digital bereit: Selbstauskunft, "
        "SCHUFA-BonitätsCheck, Einkommensnachweise, Immatrikulationsbescheinigung sowie eine "
        "Bürgschaft meiner Eltern inklusive deren Einkommensnachweisen. Ich bin Nichtraucher, "
        "ruhig und suche ein langfristiges Mietverhältnis.",
        "Zu einer Besichtigung bin ich kurzfristig und flexibel verfügbar. Über eine Rückmeldung "
        "freue ich mich sehr.",
        "Mit freundlichen Grüßen",
        f"{PERSON['name']} · {PERSON['telefon']} · {PERSON['email']}",
    ]:
        p = doc.add_paragraph(a)
        p.paragraph_format.space_after = Pt(8)

    # --- Variante 2 -------------------------------------------------------
    doc.add_page_break()
    heading(doc, "Variante 2 – Standard-Anschreiben (PDF für die Bewerbermappe)")
    doc.add_paragraph(
        "Als erste Seite der Bewerbermappe oder für die Besichtigung ausgedruckt mitbringen."
    )
    for line in [PERSON["name"], PERSON["anschrift"], PERSON["telefon"], PERSON["email"]]:
        p = doc.add_paragraph(line)
        p.paragraph_format.space_after = Pt(0)
    doc.add_paragraph("")
    for line in ["{{VERMIETER_NAME}}", "{{VERMIETER_ADRESSE}}"]:
        p = doc.add_paragraph(line)
        p.paragraph_format.space_after = Pt(0)
    doc.add_paragraph("")
    d = doc.add_paragraph("Berlin, {{DATUM}}")
    d.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    bt = doc.add_paragraph()
    btr = bt.add_run("Bewerbung um die Wohnung {{STRASSE}}, {{PLZ_ORT}} ({{OBJEKT_ID}})")
    btr.bold = True

    for a in [
        "Sehr geehrte/r {{ANREDE}},",
        "Ihre Wohnung in der {{STRASSE}} hat mich sofort angesprochen – besonders {{DETAIL_INSERAT}}. "
        "Gerne stelle ich mich Ihnen kurz vor.",
        "Ich bin {{ALTER}} Jahre alt und studiere seit Oktober 2024 Wirtschaftsingenieurwesen an "
        "der HTW Berlin. Parallel arbeite ich als Werkstudent in der Qualitätssicherung bei der "
        "AKG Software Consulting GmbH in Berlin. Zuvor habe ich eine Ausbildung zum Kaufmann im "
        "Groß- und Außenhandel mit der Note 1,7 abgeschlossen. Mein monatliches Nettoeinkommen "
        "beträgt {{NETTO_GESAMT}} €; zusätzlich bürgen meine Eltern für das Mietverhältnis und "
        "legen ihre Einkommensnachweise bei.",
        "Als Mieter bin ich unkompliziert und zuverlässig: Ich bin Nichtraucher, halte mich an "
        "die Hausordnung, habe keine Haustiere und suche kein Zwischenquartier, sondern ein "
        "langfristiges Zuhause. Meine Miete war und ist immer pünktlich.",
        "Meine vollständigen Unterlagen – Selbstauskunft, SCHUFA-BonitätsCheck, "
        "Einkommensnachweise, Immatrikulationsbescheinigung, Ausweiskopie und Bürgschaftserklärung "
        "– sind dieser Bewerbung beigefügt und können bei Bedarf sofort im Original vorgelegt "
        "werden.",
        "Über eine Einladung zur Besichtigung würde ich mich sehr freuen. Sie erreichen mich "
        "jederzeit unter {{TELEFON}}.",
        "Mit freundlichen Grüßen",
        PERSON["name"],
    ]:
        p = doc.add_paragraph(a)
        p.paragraph_format.space_after = Pt(8)

    # --- Variante 3 -------------------------------------------------------
    doc.add_page_break()
    heading(doc, "Variante 3 – wenn das Einkommen allein nicht reicht")
    doc.add_paragraph(
        "Einsetzen, wenn die Warmmiete über einem Drittel deines Nettoeinkommens liegt. "
        "Die Regel lautet: das Problem offen ansprechen und in derselben Zeile lösen – nie "
        "hoffen, dass der Vermieter es überliest. Er rechnet ohnehin nach."
    )
    for a in [
        "Sehr geehrte/r {{ANREDE}},",
        "ich bewerbe mich um die Wohnung in der {{STRASSE}} ({{OBJEKT_ID}}) und möchte den "
        "Punkt, den Sie ohnehin prüfen werden, gleich transparent machen: Als Werkstudent "
        "verdiene ich {{NETTO_WERKSTUDENT}} € netto im Monat. Die Warmmiete von {{WARMMIETE}} € "
        "wird deshalb durch eine unbefristete Bürgschaft meiner Eltern abgesichert.",
        "Meine Eltern, {{BUERGE_NAME}} ({{BUERGE_BERUF}} bei {{BUERGE_ARBEITGEBER}}), verfügen "
        "über ein gemeinsames Nettoeinkommen von {{BUERGE_NETTO}} € monatlich. Die "
        "unterschriebene Bürgschaftserklärung, ihre Gehaltsnachweise der letzten drei Monate "
        "sowie ihre SCHUFA-Auskunft liegen bei – Sie können die Bonität also sofort prüfen, "
        "ohne nachfragen zu müssen.",
        "Meine eigene SCHUFA-Auskunft ist einwandfrei, mein Werkstudentenvertrag bei der AKG "
        "Software Consulting GmbH läuft {{BEFRISTUNG}}, und mein Studium an der HTW Berlin "
        "dauert noch bis voraussichtlich {{STUDIENENDE}}. Ich suche also ein Mietverhältnis "
        "über mehrere Jahre.",
        "Gerne überzeuge ich Sie bei einer Besichtigung persönlich. Ich bin kurzfristig "
        "verfügbar und unter {{TELEFON}} jederzeit erreichbar.",
        "Mit freundlichen Grüßen",
        PERSON["name"],
    ]:
        p = doc.add_paragraph(a)
        p.paragraph_format.space_after = Pt(8)

    hinweis(
        doc,
        "HINWEIS (vor Versand löschen): {{DETAIL_INSERAT}} ist der wichtigste Platzhalter im "
        "ganzen Dokument – ein konkreter Satz zum konkreten Inserat (Altbau, Balkon zum Hof, "
        "Nähe zur HTW). Genau daran erkennt ein Vermieter den Unterschied zwischen einer echten "
        "Bewerbung und einem Serienbrief. Wenn du einen KI-Dienst nutzt: diese Bausteine dort "
        "hinterlegen, statt die KI frei formulieren zu lassen.",
    )

    path = OUT / "Wohnungs-Anschreiben_Vorlage.docx"
    doc.save(path)
    return path


def build_deckblatt():
    doc = Document()
    set_base_style(doc)
    kopf(doc, "Bewerbungsmappe", "{{NAME}} – Bewerbung um die Wohnung {{STRASSE}}, {{PLZ_ORT}}")

    heading(doc, "Auf einen Blick")
    feld(doc, "Name", PERSON["name"])
    feld(doc, "Alter", "{{ALTER}} Jahre")
    feld(doc, "Beruf", f"{BERUF['taetigkeit']} bei {BERUF['arbeitgeber']}")
    feld(doc, "Studium", BERUF["studium"])
    feld(doc, "Nettoeinkommen", BERUF["netto"])
    feld(doc, "Bürgschaft", f"{BUERGE['name']} ({BUERGE['verhaeltnis']}), Nettoeinkommen {BUERGE['netto']}")
    feld(doc, "Einziehende Personen", "{{ANZAHL_PERSONEN}}")
    feld(doc, "Haustiere", "{{HAUSTIERE}}")
    feld(doc, "Raucher", "{{RAUCHER}}")
    feld(doc, "Gewünschter Einzug", "{{EINZUGSTERMIN}}")
    feld(doc, "Kontakt", f"{PERSON['telefon']} · {PERSON['email']}")

    heading(doc, "Inhalt dieser Mappe")
    for name, pflicht, _ in DOKUMENTE:
        if pflicht:
            doc.add_paragraph(name, style="List Number")

    heading(doc, "Checkliste – vor dem Versand prüfen")
    doc.add_paragraph(
        "Diese Seite ist für dich, nicht für den Vermieter. Vor dem Versand löschen."
    )
    for name, pflicht, note in DOKUMENTE:
        marker = "☐ PFLICHT" if pflicht else "☐ optional"
        p = doc.add_paragraph(f"{marker} – {name}", style="List Bullet")
        p.paragraph_format.space_after = Pt(0)
        sub = doc.add_paragraph(f"      {note}")
        sub.paragraph_format.space_after = Pt(4)
        for r in sub.runs:
            r.font.size = Pt(9)
            r.italic = True
            r.font.color.rgb = RGBColor(0x88, 0x88, 0x88)

    hinweis(
        doc,
        "HINWEIS (vor Versand löschen): Alles als EIN zusammengefügtes PDF verschicken, "
        "Dateiname 'Bewerbungsmappe_{{NAME}}.pdf'. Einzelne Anhänge in zehn Dateien werden von "
        "Vermietern erfahrungsgemäß seltener geöffnet. Ausweisnummer und Kontonummern vor dem "
        "Versand schwärzen – Name, Foto und Gültigkeit reichen zur Identitätsprüfung.",
    )

    path = OUT / "Bewerbermappe_Deckblatt.docx"
    doc.save(path)
    return path


def build_arbeitgeber_anfrage():
    doc = Document()
    set_base_style(doc)
    kopf(doc, "Anfrage Arbeitgeberbescheinigung", "E-Mail-Vorlage an die Personalabteilung")

    doc.add_paragraph("Betreff: Bitte um Arbeitgeberbescheinigung für Wohnungsbewerbung")
    doc.add_paragraph("")
    for a in [
        "Guten Tag {{HR_ANSPRECHPARTNER}},",
        "ich bin derzeit auf Wohnungssuche in Berlin. Vermieter verlangen dabei regelmäßig eine "
        "Arbeitgeberbescheinigung als Nachweis eines bestehenden Beschäftigungsverhältnisses.",
        "Könnten Sie mir bitte eine kurze Bescheinigung ausstellen, die folgende Angaben enthält?",
        "• Bestätigung des bestehenden Beschäftigungsverhältnisses als Werkstudent "
        "in der Qualitätssicherung\n"
        "• Beschäftigt seit 12/2025\n"
        "• Vereinbarte Wochenarbeitszeit\n"
        "• Befristung bzw. voraussichtliche Dauer des Vertrages\n"
        "• Bestätigung, dass das Arbeitsverhältnis ungekündigt ist",
        "Eine formlose Bescheinigung auf Firmenpapier genügt vollkommen; das monatliche "
        "Bruttoentgelt muss nicht enthalten sein, da ich die Gehaltsabrechnungen separat "
        "beilege.",
        "Da Wohnungsangebote in Berlin sehr schnell vergeben werden, wäre ich für eine "
        "Rückmeldung innerhalb der kommenden Woche sehr dankbar.",
        "Vielen Dank für Ihre Unterstützung und viele Grüße",
        PERSON["name"],
    ]:
        p = doc.add_paragraph(a)
        p.paragraph_format.space_after = Pt(8)

    hinweis(
        doc,
        "HINWEIS: Am besten sofort abschicken – die Bescheinigung ist erfahrungsgemäß der "
        "Posten mit der längsten Wartezeit (1–5 Werktage) und blockiert sonst die fertige Mappe.",
    )

    path = OUT / "Arbeitgeberbescheinigung_Anfrage.docx"
    doc.save(path)
    return path


if __name__ == "__main__":
    created = [
        build_selbstauskunft(),
        build_anschreiben(),
        build_deckblatt(),
        build_arbeitgeber_anfrage(),
    ]
    print("Erstellt:")
    for p in created:
        print(" -", p)
