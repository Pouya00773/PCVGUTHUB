#!/usr/bin/env python3
"""
Erzeugt Präsentationsunterlagen für das Siemens-Mobility-Interview:
  1. input/marktdaten_weichenantriebe.xlsx  – Rohdaten für Power BI
  2. output/Vortrag_Weichenantriebe.pptx    – 2-Folien-Präsentation (Siemens-Design)

Aufruf: python3 scripts/build_presentation.py
"""

from pathlib import Path
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

ROOT = Path(__file__).resolve().parent.parent
INPUT = ROOT / "input"
OUT = ROOT / "output"
INPUT.mkdir(exist_ok=True)
OUT.mkdir(exist_ok=True)

# ---------------------------------------------------------------------------
# SIEMENS-FARBEN
# ---------------------------------------------------------------------------
PETROL     = RGBColor(0x00, 0x99, 0x99)   # #009999
DARKBLUE   = RGBColor(0x00, 0x30, 0x5E)   # #00305E
LIGHTGREY  = RGBColor(0xF2, 0xF2, 0xF2)   # #F2F2F2
MIDGREY    = RGBColor(0xA8, 0xA8, 0xA8)   # #A8A8A8
WHITE      = RGBColor(0xFF, 0xFF, 0xFF)
BLACK      = RGBColor(0x1A, 0x1A, 0x1A)

# openpyxl hex strings (no #)
XL_PETROL    = "009999"
XL_DARKBLUE  = "00305E"
XL_LIGHTGREY = "F2F2F2"
XL_WHITE     = "FFFFFF"
XL_BLACK     = "1A1A1A"


# ===========================================================================
# 1. EXCEL – Rohdaten für Power BI
# ===========================================================================
TRENDS = [
    # Trend-Name, Reifegrad (1-5), Relevanz für Siemens (1-5), Marktpotenzial Mrd EUR
    ("Condition Monitoring / Predictive Maintenance", 4, 5, 3.2),
    ("Digitale Stellwerksintegration (EULYNX)",       3, 5, 2.8),
    ("Elektrifizierung & Energieeffizienz",           4, 4, 1.9),
    ("Cybersecurity (NIS2 / IEC 62443)",              3, 4, 1.5),
    ("Remote Diagnostics & Cloud-Integration",        4, 5, 2.4),
]

# Umsatz Signaling-Segment (geschätzt, Mrd EUR) – repräsentative Werte aus öffentlichen Berichten
WETTBEWERBER = [
    # Unternehmen, Region, Umsatz Signaling Mrd EUR
    ("Siemens Mobility",  "Europa",    2.1),
    ("Siemens Mobility",  "Asien",     0.9),
    ("Siemens Mobility",  "Americas",  0.7),
    ("Alstom",            "Europa",    1.8),
    ("Alstom",            "Asien",     0.7),
    ("Alstom",            "Americas",  0.5),
    ("Hitachi Rail",      "Europa",    1.2),
    ("Hitachi Rail",      "Asien",     1.0),
    ("Hitachi Rail",      "Americas",  0.2),
    ("Vossloh/Voestalpine", "Europa",  0.6),
    ("Vossloh/Voestalpine", "Asien",   0.1),
    ("Vossloh/Voestalpine", "Americas",0.1),
    ("CRRC / CASCO",      "Europa",    0.3),
    ("CRRC / CASCO",      "Asien",     1.5),
    ("CRRC / CASCO",      "Americas",  0.2),
]

MARKTANTEILE = [
    # Unternehmen, Marktanteil % (Schätzung Weichenantriebe Europa)
    ("Siemens Mobility",    32),
    ("Alstom",              27),
    ("Hitachi Rail",        18),
    ("Vossloh/Voestalpine", 11),
    ("Hanning & Kahl",       6),
    ("Sonstige / CRRC",      6),
]


def _header_row(ws, cols, row=1):
    """Schreibt eine Header-Zeile in Petrol."""
    for col, name in enumerate(cols, 1):
        c = ws.cell(row=row, column=col, value=name)
        c.font = Font(bold=True, color=XL_WHITE, name="Calibri")
        c.fill = PatternFill("solid", fgColor=XL_PETROL)
        c.alignment = Alignment(horizontal="center", wrap_text=True)
    ws.row_dimensions[row].height = 28


def _border_range(ws, min_row, max_row, max_col):
    thin = Side(style="thin", color="CCCCCC")
    for row in ws.iter_rows(min_row=min_row, max_row=max_row, max_col=max_col):
        for cell in row:
            cell.border = Border(
                left=thin, right=thin, top=thin, bottom=thin
            )
            cell.alignment = Alignment(horizontal="center")


def build_excel():
    wb = openpyxl.Workbook()

    # ---- Sheet 1: Technologische Trends ----
    ws1 = wb.active
    ws1.title = "Technologische Trends"
    _header_row(ws1, ["Trend", "Reifegrad (1–5)", "Relevanz Siemens (1–5)", "Marktpotenzial (Mrd. EUR)"])
    ws1.column_dimensions["A"].width = 44
    for ci in ["B", "C", "D"]:
        ws1.column_dimensions[ci].width = 22

    for i, (name, reife, relevanz, potenzial) in enumerate(TRENDS, 2):
        ws1.cell(i, 1, name).alignment = Alignment(wrap_text=True)
        ws1.cell(i, 2, reife)
        ws1.cell(i, 3, relevanz)
        ws1.cell(i, 4, potenzial)
        if i % 2 == 0:
            for col in range(1, 5):
                ws1.cell(i, col).fill = PatternFill("solid", fgColor=XL_LIGHTGREY)

    _border_range(ws1, 1, len(TRENDS) + 1, 4)

    # Hinweis für Power BI
    note_row = len(TRENDS) + 3
    ws1.cell(note_row, 1,
             "Power BI: Scatter/Bubble-Chart – X=Reifegrad, Y=Relevanz, Größe=Marktpotenzial"
             ).font = Font(italic=True, color="888888")

    # ---- Sheet 2: Wettbewerber-Umsatz ----
    ws2 = wb.create_sheet("Wettbewerb – Umsatz nach Region")
    _header_row(ws2, ["Unternehmen", "Region", "Umsatz Signaling (Mrd. EUR)"])
    ws2.column_dimensions["A"].width = 26
    ws2.column_dimensions["B"].width = 14
    ws2.column_dimensions["C"].width = 28

    for i, (firma, region, umsatz) in enumerate(WETTBEWERBER, 2):
        ws2.cell(i, 1, firma)
        ws2.cell(i, 2, region)
        ws2.cell(i, 3, umsatz)
        if i % 2 == 0:
            for col in range(1, 4):
                ws2.cell(i, col).fill = PatternFill("solid", fgColor=XL_LIGHTGREY)

    _border_range(ws2, 1, len(WETTBEWERBER) + 1, 3)
    note_row2 = len(WETTBEWERBER) + 3
    ws2.cell(note_row2, 1,
             "Power BI: Gruppiertes Balkendiagramm – X=Region, Y=Umsatz, Legende=Unternehmen"
             ).font = Font(italic=True, color="888888")

    # ---- Sheet 3: Marktanteile ----
    ws3 = wb.create_sheet("Marktanteile Europa (Schätzung)")
    _header_row(ws3, ["Unternehmen", "Marktanteil % (Weichenantriebe Europa, Schätzung)"])
    ws3.column_dimensions["A"].width = 28
    ws3.column_dimensions["B"].width = 44

    for i, (firma, anteil) in enumerate(MARKTANTEILE, 2):
        ws3.cell(i, 1, firma)
        ws3.cell(i, 2, anteil)
        if i % 2 == 0:
            for col in range(1, 3):
                ws3.cell(i, col).fill = PatternFill("solid", fgColor=XL_LIGHTGREY)

    _border_range(ws3, 1, len(MARKTANTEILE) + 1, 2)
    note_row3 = len(MARKTANTEILE) + 3
    ws3.cell(note_row3, 1,
             "Power BI: Donut-Diagramm – Marktanteile nach Unternehmen"
             ).font = Font(italic=True, color="888888")

    path = INPUT / "marktdaten_weichenantriebe.xlsx"
    wb.save(path)
    return path


# ===========================================================================
# 2. POWERPOINT – 2-Folien-Präsentation
# ===========================================================================
SLIDE_W = Inches(13.33)   # 16:9 Widescreen
SLIDE_H = Inches(7.5)

MARGIN_L = Inches(0.5)
MARGIN_T = Inches(0.5)


def _add_rect(slide, left, top, width, height, fill_rgb, line_rgb=None):
    from pptx.util import Emu
    shape = slide.shapes.add_shape(
        1,  # MSO_SHAPE_TYPE.RECTANGLE
        left, top, width, height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_rgb
    if line_rgb:
        shape.line.color.rgb = line_rgb
    else:
        shape.line.fill.background()
    return shape


def _add_textbox(slide, text, left, top, width, height,
                 font_size=18, bold=False, color=BLACK,
                 align=PP_ALIGN.LEFT, italic=False, wrap=True):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = wrap
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    run.font.name = "Calibri"
    return txBox


def _add_bullet_box(slide, items, left, top, width, height, font_size=14):
    """Textbox mit Bullet-Punkten (→ Pfeil als Bullet)."""
    from pptx.util import Pt
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    first = True
    for item in items:
        if first:
            p = tf.paragraphs[0]
            first = False
        else:
            p = tf.add_paragraph()
        p.space_before = Pt(4)
        run = p.add_run()
        run.text = f"→  {item}"
        run.font.size = Pt(font_size)
        run.font.name = "Calibri"
        run.font.color.rgb = BLACK
    return txBox


def _add_footer(slide, source_text):
    """Quellen-Footer ganz unten."""
    _add_rect(slide,
              left=0, top=SLIDE_H - Inches(0.4),
              width=SLIDE_W, height=Inches(0.4),
              fill_rgb=DARKBLUE)
    _add_textbox(slide, source_text,
                 left=MARGIN_L, top=SLIDE_H - Inches(0.38),
                 width=SLIDE_W - Inches(1),
                 height=Inches(0.36),
                 font_size=9, color=WHITE,
                 align=PP_ALIGN.LEFT)


def _add_header_bar(slide, title_text, subtitle_text=""):
    """Petrol-Header-Balken oben."""
    _add_rect(slide,
              left=0, top=0,
              width=SLIDE_W, height=Inches(1.35),
              fill_rgb=PETROL)
    _add_textbox(slide, title_text,
                 left=MARGIN_L, top=Inches(0.1),
                 width=SLIDE_W - Inches(1),
                 height=Inches(0.65),
                 font_size=24, bold=True, color=WHITE,
                 align=PP_ALIGN.LEFT)
    if subtitle_text:
        _add_textbox(slide, subtitle_text,
                     left=MARGIN_L, top=Inches(0.72),
                     width=SLIDE_W - Inches(1),
                     height=Inches(0.5),
                     font_size=14, bold=False, color=WHITE,
                     align=PP_ALIGN.LEFT)


# ---- Folie 1: Technologische Trends ----
TREND_BULLETS = [
    "Condition Monitoring & Predictive Maintenance\n"
    "    IoT-Sensoren + KI-Analyse → Wartungskosten –20–30 %",
    "Digitale Stellwerksintegration (EULYNX)\n"
    "    EU-Norm ersetzt analoge Relaistechnik → offene Schnittstellen",
    "Elektrifizierung & Energieeffizienz\n"
    "    Ablösung hydraulischer Antriebe; Rückspeisung beim Schaltvorgang",
    "Cybersecurity (NIS2 / IEC 62443)\n"
    "    Security-by-Design in Firmware und Feldbusse verpflichtend",
    "Remote Diagnostics & Cloud (z.B. Railigent X)\n"
    "    Fernüberwachung → Vor-Ort-Einsätze signifikant reduziert",
]

TREND_CHART_NOTE = (
    "Power-BI-Chart (Bubble Chart)\n"
    "X = Reifegrad | Y = Relevanz für Siemens | Größe = Marktpotenzial"
)

# ---- Folie 2: Wettbewerbssituation ----
WETTBEWERB_BULLETS = [
    "Siemens Mobility – Systemführer, EULYNX-Kompetenz, Railigent X-Plattform",
    "Alstom (+Bombardier) – starke CBTC/Metro-Präsenz, Konsolidierungspotenzial",
    "Hitachi Rail – Systemintegration, solide Europa/Asien-Basis",
    "Vossloh/Voestalpine & Hanning & Kahl – Spezialisten, Nischenstärke",
    "CRRC/CASCO – aggressiver Preiswettbewerb, wachsender Export in Osteuropa",
]

WETTBEWERB_CHART_NOTE = (
    "Power-BI-Chart (Balkendiagramm)\n"
    "Umsatz Signaling-Segment nach Region (Mrd. EUR) – Top-3 Anbieter"
)

IMPLICATION_1 = (
    "Implikation für Siemens:  "
    "Differenzierung nicht über Hardware-Preis, sondern über digitale Plattform (Railigent X) "
    "und EULYNX-Systemkompetenz."
)
IMPLICATION_2 = (
    "Implikation für Siemens:  "
    "Premium-Positionierung + Software/Service-Anteil erhöhen "
    "– Wachstumshebel in Europa durch Deutschlandtakt & TEN-T-Investitionen."
)

SOURCE_1 = (
    "Quellen: Siemens Mobility GB 2024 | Europe's Rail JU Roadmap 2025 | "
    "Bundesministerium für Digitales und Verkehr (Deutschlandtakt) | Eigene Schätzung"
)
SOURCE_2 = (
    "Quellen: Siemens Mobility GB 2024 | Alstom AR 2024 | Hitachi Rail AR 2024 | "
    "Mordor Intelligence Rail Signaling Market Summary 2024 | Eigene Schätzung"
)


def build_pptx():
    prs = Presentation()
    prs.slide_width  = SLIDE_W
    prs.slide_height = SLIDE_H

    blank_layout = prs.slide_layouts[6]  # vollständig leer

    # =========================================================
    # FOLIE 1 – Technologische Trends
    # =========================================================
    s1 = prs.slides.add_slide(blank_layout)

    # Hintergrund weiß
    _add_rect(s1, 0, 0, SLIDE_W, SLIDE_H, WHITE)

    # Header
    _add_header_bar(
        s1,
        "Technologische Trends – Weichenantriebe",
        "Digitalisierung und Predictive Maintenance definieren die nächste Generation"
    )

    content_top  = Inches(1.45)
    content_h    = SLIDE_H - Inches(1.45) - Inches(0.55)
    col_mid      = SLIDE_W / 2

    # Linke Seite: Chart-Platzhalter (Rahmen)
    chart_box = _add_rect(
        s1,
        left=MARGIN_L, top=content_top,
        width=col_mid - MARGIN_L - Inches(0.15),
        height=content_h - Inches(0.4),
        fill_rgb=LIGHTGREY,
        line_rgb=PETROL
    )
    _add_textbox(
        s1, "[ Power BI Chart hier einfügen ]\n\n" + TREND_CHART_NOTE,
        left=MARGIN_L + Inches(0.1),
        top=content_top + Inches(0.15),
        width=col_mid - MARGIN_L - Inches(0.35),
        height=content_h - Inches(0.6),
        font_size=11, italic=True, color=MIDGREY,
        align=PP_ALIGN.CENTER
    )

    # Trennlinie
    _add_rect(s1,
              left=col_mid - Inches(0.02), top=content_top,
              width=Inches(0.04), height=content_h - Inches(0.4),
              fill_rgb=MIDGREY)

    # Rechte Seite: Bullets
    RIGHT_L = col_mid + Inches(0.15)
    RIGHT_W = SLIDE_W - col_mid - Inches(0.15) - MARGIN_L

    _add_textbox(s1, "Fünf Schlüsseltrends",
                 left=RIGHT_L, top=content_top,
                 width=RIGHT_W, height=Inches(0.38),
                 font_size=14, bold=True, color=DARKBLUE)

    # Trend-Bullets einzeln für sauberes Spacing
    bullet_texts = [
        ("Condition Monitoring & Predictive Maintenance",
         "IoT-Sensoren + KI → Wartungskosten –20–30 %"),
        ("Digitale Stellwerksintegration (EULYNX)",
         "EU-Norm ersetzt analoge Relaistechnik"),
        ("Elektrifizierung & Energieeffizienz",
         "Ablösung hydraulischer Antriebe; Energierückspeisung"),
        ("Cybersecurity (NIS2 / IEC 62443)",
         "Security-by-Design in Firmware verpflichtend"),
        ("Remote Diagnostics & Cloud (Railigent X)",
         "Fernüberwachung → Vor-Ort-Einsätze signifikant ↓"),
    ]

    b_top = content_top + Inches(0.42)
    b_h   = (content_h - Inches(0.85)) / len(bullet_texts)

    for (title, sub) in bullet_texts:
        _add_rect(s1,
                  left=RIGHT_L, top=b_top,
                  width=Inches(0.08), height=b_h - Inches(0.05),
                  fill_rgb=PETROL)
        _add_textbox(s1, title,
                     left=RIGHT_L + Inches(0.14), top=b_top,
                     width=RIGHT_W - Inches(0.18), height=Inches(0.28),
                     font_size=12, bold=True, color=DARKBLUE)
        _add_textbox(s1, sub,
                     left=RIGHT_L + Inches(0.14), top=b_top + Inches(0.26),
                     width=RIGHT_W - Inches(0.18), height=Inches(0.22),
                     font_size=10, color=BLACK)
        b_top += b_h

    # Implikation-Box
    impl_top = content_top + content_h - Inches(0.4)
    _add_rect(s1,
              left=MARGIN_L, top=impl_top,
              width=SLIDE_W - MARGIN_L * 2, height=Inches(0.36),
              fill_rgb=DARKBLUE)
    _add_textbox(s1, IMPLICATION_1,
                 left=MARGIN_L + Inches(0.1), top=impl_top + Inches(0.03),
                 width=SLIDE_W - MARGIN_L * 2 - Inches(0.2), height=Inches(0.32),
                 font_size=10, bold=True, color=WHITE)

    _add_footer(s1, SOURCE_1)

    # =========================================================
    # FOLIE 2 – Wettbewerbssituation
    # =========================================================
    s2 = prs.slides.add_slide(blank_layout)
    _add_rect(s2, 0, 0, SLIDE_W, SLIDE_H, WHITE)

    _add_header_bar(
        s2,
        "Wettbewerbssituation – Weichenantriebe",
        "Konsolidierter Markt, 3–4 globale Platzhirsche – Differenzierung über Digitalisierung"
    )

    # Linke Seite: Chart-Platzhalter
    _add_rect(
        s2,
        left=MARGIN_L, top=content_top,
        width=col_mid - MARGIN_L - Inches(0.15),
        height=content_h - Inches(0.4),
        fill_rgb=LIGHTGREY,
        line_rgb=PETROL
    )
    _add_textbox(
        s2, "[ Power BI Chart hier einfügen ]\n\n" + WETTBEWERB_CHART_NOTE,
        left=MARGIN_L + Inches(0.1),
        top=content_top + Inches(0.15),
        width=col_mid - MARGIN_L - Inches(0.35),
        height=content_h - Inches(0.6),
        font_size=11, italic=True, color=MIDGREY,
        align=PP_ALIGN.CENTER
    )

    _add_rect(s2,
              left=col_mid - Inches(0.02), top=content_top,
              width=Inches(0.04), height=content_h - Inches(0.4),
              fill_rgb=MIDGREY)

    # Rechte Seite
    _add_textbox(s2, "Key Competitors",
                 left=RIGHT_L, top=content_top,
                 width=RIGHT_W, height=Inches(0.38),
                 font_size=14, bold=True, color=DARKBLUE)

    wett_bullets = [
        ("Siemens Mobility",     "EULYNX-Leader, Railigent X, globales Servicenetz"),
        ("Alstom (+Bombardier)", "Breites Signaling-Portfolio, CBTC-Stärke"),
        ("Hitachi Rail",         "Systemintegration, Europa & Asien"),
        ("Vossloh / Hanning & Kahl", "Nischenspezialisten, hohe Qualität"),
        ("CRRC / CASCO",         "Preiswettbewerb, wachsender Europa-Export"),
    ]

    b_top2 = content_top + Inches(0.42)
    b_h2   = (content_h - Inches(0.85)) / len(wett_bullets)

    for (title, sub) in wett_bullets:
        is_siemens = "Siemens" in title
        bar_color = PETROL if is_siemens else MIDGREY
        _add_rect(s2,
                  left=RIGHT_L, top=b_top2,
                  width=Inches(0.08), height=b_h2 - Inches(0.05),
                  fill_rgb=bar_color)
        _add_textbox(s2, title,
                     left=RIGHT_L + Inches(0.14), top=b_top2,
                     width=RIGHT_W - Inches(0.18), height=Inches(0.28),
                     font_size=12, bold=True,
                     color=DARKBLUE if is_siemens else BLACK)
        _add_textbox(s2, sub,
                     left=RIGHT_L + Inches(0.14), top=b_top2 + Inches(0.26),
                     width=RIGHT_W - Inches(0.18), height=Inches(0.22),
                     font_size=10, color=BLACK)
        b_top2 += b_h2

    # Implikation
    _add_rect(s2,
              left=MARGIN_L, top=impl_top,
              width=SLIDE_W - MARGIN_L * 2, height=Inches(0.36),
              fill_rgb=DARKBLUE)
    _add_textbox(s2, IMPLICATION_2,
                 left=MARGIN_L + Inches(0.1), top=impl_top + Inches(0.03),
                 width=SLIDE_W - MARGIN_L * 2 - Inches(0.2), height=Inches(0.32),
                 font_size=10, bold=True, color=WHITE)

    _add_footer(s2, SOURCE_2)

    path = OUT / "Vortrag_Weichenantriebe.pptx"
    prs.save(path)
    return path


# ===========================================================================
if __name__ == "__main__":
    xl = build_excel()
    print(f"Excel erstellt:      {xl}")
    pptx_path = build_pptx()
    print(f"PowerPoint erstellt: {pptx_path}")
    print()
    print("Nächste Schritte:")
    print("  1. Öffne die Excel-Datei in Power BI Desktop")
    print("  2. Erstelle Bubble-Chart (Sheet 1) + Balkendiagramm (Sheet 2)")
    print("  3. Exportiere Charts als PNG (Datei → Als Bild exportieren)")
    print("  4. Öffne die PPTX und ersetze die grauen Platzhalter durch die PNG-Charts")
    print("  5. Schriftart prüfen: Calibri ist voreingestellt (Siemens Sans falls verfügbar)")
